#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Search the source index in docs-loka/ the way rg and jq search text.

  idx.py callers PATTERN   functions that call something matching PATTERN
  idx.py callees PATTERN   what the functions whose name matches PATTERN call
  idx.py fn PATTERN        functions whose name matches PATTERN
  idx.py uses PATTERN      functions using an XPCOM interface, contract ID or
                           Services.xxx matching PATTERN

PATTERN is a regular expression searched inside the name, like rg. Matching is
by name, not by resolved type: `gBrowser.addTabGroup` and `this.addTabGroup`
both match `addTabGroup`.

Exit status is 0 when something matched and 1 otherwise.
"""

import argparse
import fnmatch
import json
import os
import re
import sys

TOPSRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_ROOT = os.path.join(TOPSRC, "docs-loka")

SOURCE_RE = re.compile(r"^source: (\S+)$")
LINES_RE = re.compile(r"^lines: (\d+)$")
POS_RE = re.compile(r"^- 位置: (?:async )?L(\d+)-(\d+)$")
CODE_RE = re.compile(r"`([^`]+)`")
CALL_RE = re.compile(r"`(.+?)\(\)`(?:, |$)")
COND_RE = re.compile(r"^- 条件付き依存: `if \((.*)\)` → `(.+)\(\)`$")
XPCOM_LINK_RE = re.compile(r"\[`(nsI\w+|mozI\w+)`\]\([^)]*\)")
JS_SUFFIXES = (".js", ".mjs", ".jsm")


def parse_doc(path):
    """Yield one dict per function section of an index doc."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    source = None
    total = 0
    entry = None
    for line in lines:
        m = SOURCE_RE.match(line)
        if m and source is None:
            source = m.group(1)
            if not source.endswith(JS_SUFFIXES):
                return
            continue
        m = LINES_RE.match(line)
        if m and total == 0:
            total = int(m.group(1))
            continue
        if line.startswith("## "):
            if entry:
                yield entry
            name = line[3:]
            name = name[:-2] if name.endswith("()") else name
            entry = {
                "path": source,
                "name": name,
                "start": 1 if name == "<module>" else 0,
                "end": total if name == "<module>" else 0,
                "role": "",
                "calls": [],
                "conditional": [],
                "xpcom": [],
            }
            continue
        if entry is None:
            continue
        m = POS_RE.match(line)
        if m:
            entry["start"], entry["end"] = int(m.group(1)), int(m.group(2))
        elif line.startswith("- 役割: "):
            entry["role"] = line[len("- 役割: "):]
        elif line.startswith("- 呼び出し先: "):
            entry["calls"] = CALL_RE.findall(line[len("- 呼び出し先: "):])
        elif line.startswith("- 条件付き依存: "):
            m = COND_RE.match(line)
            if m:
                entry["conditional"].append((m.group(1), m.group(2)))
        elif line.startswith("- XPCOM: "):
            rest = line[len("- XPCOM: "):]
            entry["xpcom"] = XPCOM_LINK_RE.findall(rest) + [
                c.split(" → ")[0] for c in CODE_RE.findall(XPCOM_LINK_RE.sub("", rest))
            ]
    if entry:
        yield entry


def iter_entries(root, globs):
    for dirpath, _, names in sorted(os.walk(root)):
        for n in sorted(names):
            if not n.endswith(".md"):
                continue
            for e in parse_doc(os.path.join(dirpath, n)):
                if not globs or any(fnmatch.fnmatch(e["path"], g) for g in globs):
                    yield e


def compile_pattern(args):
    pat = re.escape(args.pattern) if args.fixed else args.pattern
    if args.word:
        pat = rf"\b(?:{pat})\b"
    return re.compile(pat, re.I if args.ignore_case else 0)


def matches(args, entry, rx):
    """Yield (kind, matched text, condition) for each hit in an entry."""
    if args.command == "fn":
        if rx.search(entry["name"]):
            yield "definition", entry["name"], None
    elif args.command == "callees":
        if rx.search(entry["name"]):
            for c in entry["calls"]:
                yield "call", c, None
            for cond, c in entry["conditional"]:
                yield "conditional", c, cond
    elif args.command == "callers":
        for c in entry["calls"]:
            if rx.search(c):
                yield "call", c, None
        for cond, c in entry["conditional"]:
            if rx.search(c):
                yield "conditional", c, cond
    elif args.command == "uses":
        for x in entry["xpcom"]:
            if rx.search(x):
                yield "xpcom", x, None


def format_text(hit, summary):
    e = hit["entry"]
    loc = f"{e['path']}:{e['start']}-{e['end']}"
    out = f"{loc} {e['name']}"
    if hit["kind"] != "definition":
        out += f" -> {hit['match']}"
    if hit["condition"]:
        out += f"  [if ({hit['condition']})]"
    if summary and e["role"]:
        out += f"  # {e['role']}"
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("command", choices=["callers", "callees", "fn", "uses"])
    p.add_argument("pattern")
    p.add_argument("-i", "--ignore-case", action="store_true")
    p.add_argument("-F", "--fixed", action="store_true",
                   help="treat PATTERN as a literal string")
    p.add_argument("-w", "--word", action="store_true",
                   help="match whole words only")
    p.add_argument("-g", "--glob", action="append", default=[],
                   help="only source paths matching GLOB (repeatable)")
    p.add_argument("-l", "--files-with-matches", action="store_true")
    p.add_argument("-c", "--count", action="store_true",
                   help="print the number of matches per file")
    p.add_argument("--json", action="store_true",
                   help="one JSON object per match, for jq")
    p.add_argument("-s", "--summary", action="store_true",
                   help="append the role line of each function")
    p.add_argument("--root", default=DEFAULT_ROOT, help="index directory")
    args = p.parse_args(argv)

    rx = compile_pattern(args)
    hits = []
    for entry in iter_entries(args.root, args.glob):
        for kind, text, cond in matches(args, entry, rx):
            hits.append({"entry": entry, "kind": kind, "match": text, "condition": cond})

    if args.files_with_matches:
        for path in sorted({h["entry"]["path"] for h in hits}):
            print(path)
    elif args.count:
        counts = {}
        for h in hits:
            counts[h["entry"]["path"]] = counts.get(h["entry"]["path"], 0) + 1
        for path, n in sorted(counts.items()):
            print(f"{path}:{n}")
    elif args.json:
        for h in hits:
            e = h["entry"]
            print(json.dumps({
                "path": e["path"], "name": e["name"], "start": e["start"],
                "end": e["end"], "kind": h["kind"], "match": h["match"],
                "condition": h["condition"], "role": e["role"],
            }, ensure_ascii=False))
    else:
        for h in hits:
            print(format_text(h, args.summary))
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main())
