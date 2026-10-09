# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Extract interfaces, methods and attributes from an XPIDL file."""

import json
import os
import subprocess
import sys

TOPSRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(TOPSRC, "third_party", "python", "ply"))
sys.path.insert(0, os.path.join(TOPSRC, "xpcom", "idl-parser", "xpidl"))

import xpidl  # noqa: E402


def git_blob_hash(path):
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def first_doc_line(doccomments):
    for comment in doccomments or []:
        lines = [
            line.strip(" */\t")
            for line in comment.splitlines()
            if line.strip(" */\t")
        ]
        if lines:
            return lines[0]
    return ""


def param_text(p):
    return f"{p.type} {p.name}"


def member_dict(m):
    doc = first_doc_line(getattr(m, "doccomments", None))
    if isinstance(m, xpidl.Method):
        params = ", ".join(param_text(p) for p in m.params)
        return {
            "kind": "method",
            "name": m.name,
            "signature": f"{m.type} {m.name}({params})",
            "doc": doc,
        }
    if isinstance(m, xpidl.Attribute):
        ro = "readonly " if m.readonly else ""
        return {
            "kind": "attribute",
            "name": m.name,
            "signature": f"{ro}attribute {m.type} {m.name}",
            "doc": doc,
        }
    if isinstance(m, xpidl.ConstMember):
        return {
            "kind": "const",
            "name": m.name,
            "signature": f"const {m.type} {m.name}",
            "doc": doc,
        }
    return None


def extract(path):
    with open(path, encoding="utf-8") as f:
        data = f.read()
    idl = xpidl.IDLParser().parse(data, filename=path)
    interfaces = []
    for p in idl.productions:
        if not isinstance(p, xpidl.Interface):
            continue
        members = [d for d in (member_dict(m) for m in p.members) if d]
        interfaces.append({
            "name": p.name,
            "base": p.base,
            "scriptable": p.attributes.scriptable,
            "doc": first_doc_line(p.doccomments),
            "members": members,
        })
    return {
        "path": path,
        "source_hash": git_blob_hash(path),
        "interfaces": interfaces,
    }


if __name__ == "__main__":
    json.dump(extract(sys.argv[1]), sys.stdout, indent=2)
    print()
