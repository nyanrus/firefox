# nsITypeAheadFind (toolkit/components/typeaheadfind/nsITypeAheadFind.idl)

source: toolkit/components/typeaheadfind/nsITypeAheadFind.idl
source-hash: b2c33fed23a92a7bf00024748766883964d23be7

- 継承: nsISupports
- 役割: nsTypeAheadFind
- 実装: (未記入)
- 使っているJS: [`browser/components/genai/content/page-assist.mjs`](../../../browser/components/genai/content/page-assist.mjs.md)

## メソッド / 属性
- `void init(nsIDocShell aDocShell)`: Initializer
- `unsigned short find(AString aSearchString, boolean aLinksOnly, unsigned long aMode, boolean aDontIterateFrames)`: Core functions
- `Range getFoundRange()`: (未記入)
- `void setDocShell(nsIDocShell aDocShell)`: Helper functions
- `void setSelectionModeAndRepaint(short toggle)`: (未記入)
- `void collapseSelection()`: (未記入)
- `boolean isRangeVisible(Range aRange, boolean aMustBeInViewPort)`: (未記入)
- `boolean isRangeRendered(Range aRange)`: (未記入)
- `readonly attribute AString searchString`: Attributes
- `attribute boolean caseSensitive`: (未記入)
- `attribute boolean matchDiacritics`: (未記入)
- `attribute boolean entireWord`: (未記入)
- `readonly attribute Element foundLink`: (未記入)
- `readonly attribute Element foundEditable`: (未記入)
- `readonly attribute mozIDOMWindow currentWindow`: (未記入)
- `const unsigned long FIND_INITIAL`: Constants
- `const unsigned long FIND_NEXT`: (未記入)
- `const unsigned long FIND_PREVIOUS`: (未記入)
- `const unsigned long FIND_FIRST`: (未記入)
- `const unsigned long FIND_LAST`: (未記入)
- `const unsigned short FIND_FOUND`: (未記入)
- `const unsigned short FIND_NOTFOUND`: (未記入)
- `const unsigned short FIND_WRAPPED`: (未記入)
- `const unsigned short FIND_PENDING`: (未記入)
