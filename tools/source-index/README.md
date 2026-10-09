# source-index

Generates `docs/index/`, a per-file map of chrome JS and the XPCOM interfaces it uses.
Dependencies (functions, calls, XPCOM usage) are extracted mechanically; the
"役割" and "触るとき" fields are left as `(未記入)` for a summarizer to fill in.

    pip install tree-sitter tree-sitter-javascript
    python3 tools/source-index/build.py generate browser/components/tabbrowser
    python3 tools/source-index/build.py check

`check` lists index docs whose `source-hash` no longer matches the source blob.
