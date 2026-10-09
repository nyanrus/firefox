# source-index

Generates `docs-loka/`, a per-file map of chrome JS and the XPCOM interfaces it uses.
Dependencies (functions, calls, XPCOM usage) are extracted mechanically; the
"役割" and "触るとき" fields are left as `(未記入)` for a summarizer to fill in.

    pip install tree-sitter tree-sitter-javascript
    python3 tools/source-index/build.py generate browser/components/tabbrowser
    python3 tools/source-index/build.py check

`check` lists index docs whose `source-hash` no longer matches the source blob.

## Searching the index

`idx.py` searches `docs-loka/` like rg and jq search text. It reads only the
index, so it needs no parser. Matching is by name, not by resolved type.

    python3 tools/source-index/idx.py callers -w addTabGroup     # who calls it
    python3 tools/source-index/idx.py callees -w handle_drop     # what it calls
    python3 tools/source-index/idx.py refs -w tabGroupMenu       # calls and plain property reads
    python3 tools/source-index/idx.py fn -s 'moveTabs|ToGroup'   # find definitions
    python3 tools/source-index/idx.py uses -w nsIDragService     # XPCOM users
    python3 tools/source-index/idx.py callers addTabGroup --json | jq .path

`callers` sees call targets only; `refs` also sees property reads such as
`gBrowser.tabGroupMenu.nextUnusedColor`.

Options follow rg: `-i`, `-F`, `-w`, `-l`, `-c`, `-g GLOB` on the source path.
`--json` prints one object per match, `-s` appends each function's role line.
The exit status is 1 when nothing matched.

## Coverage

`docs-loka/` indexes the JS under `browser/` (tests, bundled output and
vendored code left out) and the XPCOM interfaces it uses. Everything the
extractor produces (functions, positions, calls, property reads, XPCOM use,
conditional calls) is there for all of it. The role lines are written for
`actors/`, `base/`, most of `components/`, and the core of `modules/` and
`components/{urlbar,places,customizableui,sessionstore,search,downloads,extensions}`;
the rest, and most IDL member descriptions, still read `(未記入)`.

## Filling summaries

Summaries are written by an agent that reads the function body, never typed
into the docs by hand:

    python3 tools/source-index/apply_summaries.py --keys <doc.md>        # what is missing
    python3 tools/source-index/apply_summaries.py <doc.md> <summaries.json>

`generate` keeps every summary already written (JS docs by function, IDL docs
by interface and member) and refreshes the machine-made lines, so it is safe to
re-run after the source changes. `check` lists docs whose source changed.
