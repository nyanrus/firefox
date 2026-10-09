# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Fill the unwritten summary fields of an index doc from a JSON file.

  apply_summaries.py <doc.md> <summaries.json>
  apply_summaries.py --keys <doc.md>          list the unwritten sections as
                                              "key<TAB>first-last line"

The JSON maps "<function name>@<start line>" (or "<module>") to
{"role": "...", "when": "..."}. Only lines still marked as unwritten are
replaced; every other line is left alone.
"""

import json
import re
import sys

TODO = "(未記入)"
HEADING_RE = re.compile(r"^## (.+?)\(?\)?$")
POS_RE = re.compile(r"^- 位置: (?:async )?L(\d+)-\d+$")


def section_keys(lines):
    """Yield (index, key, start, end) for each section of an index doc."""
    key = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            name = line[3:]
            name = name[:-2] if name.endswith("()") else name
            key = name
            if name == "<module>":
                yield i, key, None, None
        pos = POS_RE.match(line)
        if pos and key and key != "<module>":
            key = f"{key.split('@')[0]}@{pos.group(1)}"
            yield i, key, int(pos.group(1)), int(line.split("-")[-1])


def list_keys(doc_path):
    with open(doc_path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    todo = set()
    key = None
    for line in lines:
        if line.startswith("## "):
            name = line[3:]
            key = name[:-2] if name.endswith("()") else name
        pos = POS_RE.match(line)
        if pos and key and key != "<module>":
            key = f"{key.split('@')[0]}@{pos.group(1)}"
        if line == f"- 役割: {TODO}" and key:
            todo.add(key)
    for _, k, start, end in section_keys(lines):
        if k in todo:
            span = f"{start}-{end}" if start else "-"
            print(f"{k}\t{span}")


def apply(doc_path, summaries):
    with open(doc_path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    key = None
    filled = 0
    for i, line in enumerate(lines):
        if line.startswith("## "):
            name = line[3:]
            name = name[:-2] if name.endswith("()") else name
            key = "<module>" if name == "<module>" else name
        pos = POS_RE.match(line)
        if pos and key != "<module>":
            key = f"{key.split('@')[0]}@{pos.group(1)}"
        entry = summaries.get(key) if key else None
        if not entry:
            continue
        if line == f"- 役割: {TODO}" and entry.get("role"):
            lines[i] = f"- 役割: {entry['role'].strip()}"
            filled += 1
        elif line == f"- 触るとき: {TODO}" and entry.get("when"):
            lines[i] = f"- 触るとき: {entry['when'].strip()}"
            filled += 1
    with open(doc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    known = {k for _, k, _, _ in section_keys(lines)}
    for k in sorted(set(summaries) - known):
        print(f"unmatched key: {k}", file=sys.stderr)
    return filled


if __name__ == "__main__":
    if sys.argv[1] == "--keys":
        list_keys(sys.argv[2])
        sys.exit(0)
    with open(sys.argv[2], encoding="utf-8") as f:
        data = json.load(f)
    print(apply(sys.argv[1], data))
