# nsIDocumentViewerEdit (docshell/base/nsIDocumentViewerEdit.idl)

source: docshell/base/nsIDocumentViewerEdit.idl
source-hash: 549cd17b1b3bc7cf817789a01c05c364b1064a1d

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/ContextMenuChild.sys.mjs`](../../browser/actors/ContextMenuChild.sys.mjs.md)

## メソッド / 属性
- `void clearSelection()`: (未記入)
- `void selectAll()`: (未記入)
- `void copySelection()`: (未記入)
- `readonly attribute boolean copyable`: (未記入)
- `void copyLinkLocation()`: (未記入)
- `readonly attribute boolean inLink`: (未記入)
- `const long COPY_IMAGE_TEXT`: (未記入)
- `const long COPY_IMAGE_HTML`: (未記入)
- `const long COPY_IMAGE_DATA`: (未記入)
- `const long COPY_IMAGE_ALL`: (未記入)
- `void copyImage(long aCopyFlags)`: (未記入)
- `readonly attribute boolean inImage`: (未記入)
- `AString getContents(string aMimeType, boolean aSelectionOnly)`: (未記入)
- `readonly attribute boolean canGetContents`: (未記入)
- `void setCommandNode(Node aNode)`: (未記入)
