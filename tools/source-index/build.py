# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Generate and check the source index under docs-loka/.

  build.py generate [--force] <dir-or-file>...
                                       write index docs for JS files and the
                                       XPCOM interfaces they use; docs whose
                                       source-hash is unchanged are kept
                                       unless --force is given; summaries
                                       already written are carried over, and
                                       IDL docs are only rewritten when their
                                       source changed
  build.py check                       list index docs whose source changed
  build.py check-links                 list links in index docs that do not
                                       resolve to a file
"""

import ast
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))

import extract_idl  # noqa: E402
import extract_js  # noqa: E402

TOPSRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INDEX_ROOT = "docs-loka"
IDL_SEARCH_DIRS = ["xpcom", "netwerk", "dom", "toolkit", "browser", "services",
                   "uriloader", "caps", "docshell", "extensions", "devtools"]
TODO = "(未記入)"
HASH_RE = re.compile(r"^source-hash: (\w+)$", re.M)
SOURCE_RE = re.compile(r"^source: (\S+)$", re.M)
INTERFACE_RE = re.compile(r"^\s*interface\s+(nsI\w+|mozI\w+)\b", re.M)


def git_files(*patterns):
    out = subprocess.check_output(
        ["git", "ls-files", *patterns], cwd=TOPSRC, text=True
    )
    return out.split()


def collect_js(targets):
    files = []
    for t in targets:
        if os.path.isfile(os.path.join(TOPSRC, t)):
            files.append(t)
            continue
        files += [
            f for f in git_files(t)
            if f.endswith((".js", ".mjs", ".sys.mjs", ".jsm"))
            and "/test/" not in f
            and "/tests/" not in f
        ]
    return sorted(set(files))


def build_idl_index():
    """Map interface name -> repo-relative .idl path."""
    index = {}
    pats = [f"{d}/**/*.idl" for d in IDL_SEARCH_DIRS]
    for path in git_files(*pats):
        with open(os.path.join(TOPSRC, path), encoding="utf-8", errors="replace") as f:
            for m in INTERFACE_RE.finditer(f.read()):
                index.setdefault(m.group(1), path)
    return index


def build_contract_index():
    """Map contract id -> {conf, cls} parsed from components.conf files."""
    index = {}
    for path in git_files("**/components.conf"):
        try:
            with open(os.path.join(TOPSRC, path), encoding="utf-8") as f:
                tree = ast.parse(f.read())
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in tree.body:
            if not (isinstance(node, ast.Assign)
                    and any(getattr(t, "id", "") == "Classes" for t in node.targets)):
                continue
            try:
                classes = ast.literal_eval(node.value)
            except ValueError:
                continue
            for c in classes:
                impl = c.get("js_name") or c.get("type") or c.get("constructor", "")
                if c.get("jsm") or c.get("esm"):
                    impl = c.get("esm") or c.get("jsm")
                entry = {"conf": path, "impl": impl,
                         "interfaces": c.get("interfaces", [])}
                for contract in c.get("contract_ids", []):
                    index[contract] = entry
    return index


def rel_link(from_doc, to_doc):
    return os.path.relpath(to_doc, os.path.dirname(from_doc))


def doc_path(source):
    return f"{INDEX_ROOT}/{source}.md"


def read_summaries(path):
    """Return {section key: (role line, when line)} from an existing doc."""
    full = os.path.join(TOPSRC, path)
    if not os.path.exists(full):
        return {}
    with open(full, encoding="utf-8") as f:
        lines = f.read().split("\n")
    found, key, role, when = {}, None, None, None
    for line in lines + ["## "]:
        if line.startswith("## "):
            if key and (role or when):
                found[key] = (role, when)
            name = line[3:]
            key, role, when = (name[:-2] if name.endswith("()") else name), None, None
        elif line.startswith("- 位置: "):
            m = re.search(r"L(\d+)-", line)
            key = f"{key}@{m.group(1)}" if m and key else key
        elif line.startswith("- 役割: ") and line != f"- 役割: {TODO}":
            role = line
        elif line.startswith("- 触るとき: ") and line != f"- 触るとき: {TODO}":
            when = line
    return found


def keep_summaries(rendered, old):
    """Put the summaries of an older doc back into a freshly rendered one."""
    lines, key = rendered.split("\n"), None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            name = line[3:]
            key = name[:-2] if name.endswith("()") else name
        elif line.startswith("- 位置: "):
            m = re.search(r"L(\d+)-", line)
            key = f"{key}@{m.group(1)}" if m and key else key
        elif key in old and line == f"- 役割: {TODO}" and old[key][0]:
            lines[i] = old[key][0]
        elif key in old and line == f"- 触るとき: {TODO}" and old[key][1]:
            lines[i] = old[key][1]
    return "\n".join(lines)


def render_js(data, idl_index, contract_index, idl_users):
    path = data["path"]
    me = doc_path(path)
    out = [f"# {path}", "", f"source: {path}", f"source-hash: {data['source_hash']}",
           f"lines: {data['line_count']}", ""]
    mod = data["module"]
    out.append("## <module>")
    out.append(f"- 役割: {TODO}")
    if mod["calls"]:
        out.append("- 呼び出し先: " + ", ".join(f"`{c}()`" for c in mod["calls"]))
    out.append("")
    for fn in data["functions"]:
        label = "async " if fn["async"] else ""
        out.append(f"## {fn['name']}()")
        out.append(f"- 位置: {label}L{fn['start']}-{fn['end']}")
        out.append(f"- 役割: {TODO}")
        out.append(f"- 触るとき: {TODO}")
        if fn["calls"]:
            out.append("- 呼び出し先: " + ", ".join(f"`{c}()`" for c in fn["calls"]))
        for cc in fn["conditional_calls"]:
            out.append(f"- 条件付き依存: `if ({cc['condition']})` → `{cc['call']}()`")
        if fn["refs"]:
            out.append("- 参照: " + ", ".join(f"`{r}`" for r in fn["refs"]))
        xp = []
        for iface in fn["xpcom_interfaces"]:
            idl = idl_index.get(iface)
            xp.append(f"[`{iface}`]({rel_link(me, doc_path(idl))})" if idl else f"`{iface}`")
        for contract in fn["xpcom_contracts"]:
            known = contract_index.get(contract)
            suffix = f" → `{known['impl']}` ({known['conf']})" if known else ""
            xp.append(f"`{contract}`{suffix}")
        for svc in fn["services"]:
            xp.append(f"`Services.{svc}`")
        if xp:
            out.append("- XPCOM: " + " / ".join(xp))
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_idl(data, contract_index, idl_users):
    path = data["path"]
    me = doc_path(path)
    out = []
    for iface in data["interfaces"]:
        out += [f"# {iface['name']} ({path})", "", f"source: {path}",
                f"source-hash: {data['source_hash']}", ""]
        out.append(f"- 継承: {iface['base'] or 'なし'}")
        out.append(f"- 役割: {iface['doc'] or TODO}")
        impls = [
            (c, v) for c, v in sorted(contract_index.items())
            if iface["name"] in v["interfaces"]
        ]
        if impls:
            out.append("- 実装: " + "; ".join(
                f"`{v['impl']}` ({v['conf']})" for _, v in impls))
            out.append("- contract ID: " + ", ".join(f"`{c}`" for c, _ in impls))
        else:
            out.append(f"- 実装: {TODO}")
        users = sorted(idl_users.get(iface["name"], []))
        if users:
            out.append("- 使っているJS: " + ", ".join(
                f"[`{u}`]({rel_link(me, doc_path(u))})" for u in users))
        out += ["", "## メソッド / 属性"]
        for m in iface["members"]:
            out.append(f"- `{m['signature']}`: {m['doc'] or TODO}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def write(path, content):
    full = os.path.join(TOPSRC, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def is_current(path, source_hash):
    full = os.path.join(TOPSRC, path)
    if not os.path.exists(full):
        return False
    with open(full, encoding="utf-8") as f:
        m = HASH_RE.search(f.read())
    return bool(m) and m.group(1) == source_hash


def generate(targets, force=False):
    js_files = collect_js(targets)
    idl_index = build_idl_index()
    contract_index = build_contract_index()
    extracted = [extract_js.extract(os.path.join(TOPSRC, p)) for p in js_files]
    for data, rel in zip(extracted, js_files):
        data["path"] = rel
    idl_users = {}
    for data in extracted:
        for fn in data["functions"] + [data["module"]]:
            for iface in fn["xpcom_interfaces"]:
                idl_users.setdefault(iface, set()).add(data["path"])
    for data in extracted:
        path = doc_path(data["path"])
        if not force and is_current(path, data["source_hash"]):
            continue
        rendered = render_js(data, idl_index, contract_index, idl_users)
        write(path, keep_summaries(rendered, read_summaries(path)))
    used_idls = {idl_index[i] for i in idl_users if i in idl_index}
    for idl in sorted(used_idls):
        data = extract_idl.extract(os.path.join(TOPSRC, idl))
        data["path"] = idl
        if is_current(doc_path(idl), data["source_hash"]):
            continue
        write(doc_path(idl), render_idl(data, contract_index, idl_users))
    print(f"wrote {len(extracted)} JS docs and {len(used_idls)} IDL docs")


def check():
    stale = []
    root = os.path.join(TOPSRC, INDEX_ROOT)
    for dirpath, _, names in os.walk(root):
        for n in names:
            if not n.endswith(".md"):
                continue
            with open(os.path.join(dirpath, n), encoding="utf-8") as f:
                text = f.read()
            src, h = SOURCE_RE.search(text), HASH_RE.search(text)
            if not (src and h):
                continue
            src_path = os.path.join(TOPSRC, src.group(1))
            if not os.path.exists(src_path):
                stale.append((src.group(1), "missing"))
            elif extract_js.git_blob_hash(src_path) != h.group(1):
                stale.append((src.group(1), "changed"))
    for path, why in sorted(stale):
        print(f"{why}: {path}")
    return 1 if stale else 0


LINK_RE = re.compile(r"\]\(([^)#]+\.md)\)")


def check_links():
    broken = []
    root = os.path.join(TOPSRC, INDEX_ROOT)
    for dirpath, _, names in os.walk(root):
        for n in names:
            if not n.endswith(".md"):
                continue
            doc = os.path.join(dirpath, n)
            with open(doc, encoding="utf-8") as f:
                text = f.read()
            for target in LINK_RE.findall(text):
                if not os.path.exists(os.path.normpath(os.path.join(dirpath, target))):
                    broken.append((os.path.relpath(doc, TOPSRC), target))
    for doc, target in sorted(set(broken)):
        print(f"{doc}: {target}")
    return 1 if broken else 0


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "check-links":
        sys.exit(check_links())
    if len(sys.argv) >= 3 and sys.argv[1] == "generate":
        args = [a for a in sys.argv[2:] if a != "--force"]
        generate(args, force="--force" in sys.argv[2:])
    elif len(sys.argv) == 2 and sys.argv[1] == "check":
        sys.exit(check())
    else:
        print(__doc__)
        sys.exit(2)
