# browser/components/extensions/child/ext-menus-child.js

source: browser/components/extensions/child/ext-menus-child.js
source-hash: 2819ec219e4b3378e338b48ccf1b8b33d146ded4
lines: 39

## <module>
- 役割: 拡張の子側(コンテンツ側)で menus.getTargetElement を提供する ExtensionAPI 定義のファイル。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getAPI()
- 位置: L12-37
- 役割: menus.getTargetElement だけを持つ API オブジェクトを返す。
- 触るとき: menus API の子側の公開範囲を変えるとき、または getTargetElement が undefined になる問題を調べるとき。

## getTargetElement()
- 位置: L15-34
- 役割: ContextMenuChild の最後の対象の timeStamp を floor した値が引数 ID と一致し、かつ同じ文書内にある要素だけを返し、それ以外は null を返す。
- 触るとき: 拡張が受け取った target element ID から要素を引けず null になる問題を調べるとき。
- 呼び出し先: `ContextMenuChild.getLastTarget()`, `Math.floor()`, `element.getRootNode()`
- 条件付き依存: `if ( lastMenuTarget && Math.floor(lastMenuTarget.timeStamp) === targetElementId )` → `lastMenuTarget.targetRef.get()`
- 参照: `context.contentWindow.docShell.browsingContext`, `context.contentWindow.document`, `lastMenuTarget.timeStamp`
