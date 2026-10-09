# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Fill the unwritten summary fields of an index doc from a JSON file.

  apply_summaries.py <doc.md> <summaries.json>

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
    return filled


if __name__ == "__main__":
    with open(sys.argv[2], encoding="utf-8") as f:
        data = json.load(f)
    print(apply(sys.argv[1], data))
