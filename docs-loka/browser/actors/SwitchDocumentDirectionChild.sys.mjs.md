# browser/actors/SwitchDocumentDirectionChild.sys.mjs

source: browser/actors/SwitchDocumentDirectionChild.sys.mjs
source-hash: 044d32779d7ee4f31fb22941f5f63de92d1f20f7
lines: 27

## <module>
- 役割: 文書の文字方向(ltr と rtl)を切り替える子側アクター。

## SwitchDocumentDirectionChild.receiveMessage()
- 位置: L6-12
- 役割: SwitchDocumentDirection を受け、現在の文書に方向切り替えを適用する。
- 触るとき: 切り替えの起点を変えるとき。
- 条件付き依存: `if (message.name == "SwitchDocumentDirection")` → `docShell.QueryInterface()`
- 条件付き依存: `if (message.name == "SwitchDocumentDirection")` → `this.switchDocumentDirection()`
- 参照: `Ci.nsIWebNavigation`, `docShell.QueryInterface(Ci.nsIWebNavigation).document`, `message.name`, `this.manager.browsingContext.docShell`
- XPCOM: [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md)

## SwitchDocumentDirectionChild.switchDocumentDirection()
- 位置: L14-25
- 役割: dir を ltr と rtl で反転し、子フレームにも再帰的に適用する。auto の文書は変えない。
- 触るとき: 切り替えの対象範囲や条件を変えるとき。
- 呼び出し先: `this.switchDocumentDirection()`
- 参照: `document.defaultView.frames`, `document.dir`, `frame.document`
