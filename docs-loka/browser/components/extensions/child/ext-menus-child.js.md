# browser/components/extensions/child/ext-menus-child.js

source: browser/components/extensions/child/ext-menus-child.js
source-hash: 2819ec219e4b3378e338b48ccf1b8b33d146ded4
lines: 39

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getAPI()
- 位置: L12-37
- 役割: (未記入)
- 触るとき: (未記入)

## getTargetElement()
- 位置: L15-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContextMenuChild.getLastTarget()`, `Math.floor()`, `element.getRootNode()`
- 条件付き依存: `if ( lastMenuTarget && Math.floor(lastMenuTarget.timeStamp) === targetElementId )` → `lastMenuTarget.targetRef.get()`
- 参照: `context.contentWindow.docShell.browsingContext`, `context.contentWindow.document`, `lastMenuTarget.timeStamp`
