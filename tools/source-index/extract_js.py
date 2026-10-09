# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Extract functions, call targets and XPCOM usage from a chrome JS file."""

import json
import re
import subprocess
import sys

import tree_sitter_javascript as tsjs
from tree_sitter import Language, Parser

PARSER = Parser(Language(tsjs.language()))

FUNCTION_TYPES = {
    "function_declaration",
    "generator_function_declaration",
    "function_expression",
    "arrow_function",
    "method_definition",
}
IDENT_TYPES = {"identifier", "property_identifier", "private_property_identifier"}
CI_RE = re.compile(r"^Ci\.(nsI\w+)$")
CC_RE = re.compile(r"""^Cc\[\s*["']([^"']+)["']\s*\]$""")
SERVICES_RE = re.compile(r"^Services\.(\w+)")
COMPONENTS_RE = re.compile(r"^Components\.interfaces\.(nsI\w+)$")


def text(node):
    return node.text.decode("utf-8")


def git_blob_hash(path):
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def function_name(node, class_name):
    """Return the qualified name of a function node, or None if anonymous."""
    parent = node.parent
    own = node.child_by_field_name("name")
    if node.type == "method_definition" and own is not None:
        name = text(own)
        return f"{class_name}.{name}" if class_name else name
    if own is not None and own.type in IDENT_TYPES:
        return text(own)
    if parent is None:
        return None
    if parent.type == "variable_declarator":
        return text(parent.child_by_field_name("name"))
    if parent.type == "pair":
        key = parent.child_by_field_name("key")
        return text(key) if key is not None else None
    if parent.type == "assignment_expression":
        return text(parent.child_by_field_name("left"))
    if parent.type in {"field_definition", "public_field_definition"}:
        prop = parent.child_by_field_name("property") or parent.child_by_field_name(
            "name"
        )
        if prop is not None:
            name = text(prop)
            return f"{class_name}.{name}" if class_name else name
    return None


def callee_text(call):
    fn = call.child_by_field_name("function")
    if fn is None:
        return None
    t = " ".join(text(fn).split())
    return t if len(t) <= 120 else None


def normalize_condition(node):
    t = " ".join(text(node).split())
    if t.startswith("(") and t.endswith(")"):
        t = t[1:-1]
    return t if len(t) <= 160 else t[:157] + "..."


class FunctionInfo:
    def __init__(self, name, node, class_name):
        self.name = name
        self.class_name = class_name
        self.start = node.start_point[0] + 1
        self.end = node.end_point[0] + 1
        self.is_async = any(c.type == "async" for c in node.children)
        self.calls = {}
        self.conditional = []
        self.xpcom_interfaces = set()
        self.xpcom_contracts = set()
        self.services = set()

    def add_call(self, name, condition):
        if condition is None:
            self.calls.setdefault(name, 0)
            self.calls[name] += 1
        else:
            entry = (condition, name)
            if entry not in self.conditional:
                self.conditional.append(entry)

    def as_dict(self):
        return {
            "name": self.name,
            "class": self.class_name,
            "start": self.start,
            "end": self.end,
            "async": self.is_async,
            "calls": sorted(self.calls),
            "conditional_calls": [
                {"condition": c, "call": n} for c, n in self.conditional
            ],
            "xpcom_interfaces": sorted(self.xpcom_interfaces),
            "xpcom_contracts": sorted(self.xpcom_contracts),
            "services": sorted(self.services),
        }


class Extractor:
    def __init__(self, source):
        self.tree = PARSER.parse(source)
        self.functions = []
        self.top_level = FunctionInfo("<module>", self.tree.root_node, None)
        self.top_level.start = 1

    def run(self):
        self.visit(self.tree.root_node, None, self.top_level, None, None)
        result = [f.as_dict() for f in self.functions]
        module = self.top_level.as_dict()
        return module, result

    def record_xpcom(self, node, info):
        t = " ".join(text(node).split())
        if node.type == "member_expression":
            m = CI_RE.match(t) or COMPONENTS_RE.match(t)
            if m:
                info.xpcom_interfaces.add(m.group(1))
                return
            m = SERVICES_RE.match(t)
            if m:
                info.services.add(m.group(1))
        elif node.type == "subscript_expression":
            m = CC_RE.match(t)
            if m:
                info.xpcom_contracts.add(m.group(1))

    def visit(self, node, class_name, info, condition, parent_info):
        t = node.type
        if t == "class_declaration" or t == "class":
            name_node = node.child_by_field_name("name")
            class_name = text(name_node) if name_node is not None else class_name
        if t in FUNCTION_TYPES:
            name = function_name(node, class_name)
            if name is not None:
                child = FunctionInfo(name, node, class_name)
                self.functions.append(child)
                for c in node.children:
                    self.visit(c, class_name, child, None, info)
                return
        if t == "call_expression":
            name = callee_text(node)
            if name is not None:
                info.add_call(name, condition)
        elif t in {"member_expression", "subscript_expression"}:
            self.record_xpcom(node, info)
        if t == "if_statement":
            cond = normalize_condition(node.child_by_field_name("condition"))
            for c in node.children:
                if c.type == "parenthesized_expression":
                    self.visit(c, class_name, info, condition, parent_info)
                elif c.type != "else_clause" and c is not node.children[0]:
                    self.visit(c, class_name, info, cond, parent_info)
                elif c.type == "else_clause":
                    self.visit(c, class_name, info, f"!({cond})", parent_info)
            return
        for c in node.children:
            self.visit(c, class_name, info, condition, parent_info)


def extract(path):
    with open(path, "rb") as f:
        source = f.read()
    module, functions = Extractor(source).run()
    return {
        "path": path,
        "source_hash": git_blob_hash(path),
        "line_count": source.count(b"\n") + 1,
        "module": module,
        "functions": functions,
    }


if __name__ == "__main__":
    json.dump(extract(sys.argv[1]), sys.stdout, indent=2)
    print()
