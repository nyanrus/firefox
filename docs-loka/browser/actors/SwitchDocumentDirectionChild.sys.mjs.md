# browser/actors/SwitchDocumentDirectionChild.sys.mjs

source: browser/actors/SwitchDocumentDirectionChild.sys.mjs
source-hash: 044d32779d7ee4f31fb22941f5f63de92d1f20f7
lines: 27

## <module>
- 役割: (未記入)

## SwitchDocumentDirectionChild.receiveMessage()
- 位置: L6-12
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name == "SwitchDocumentDirection")` → `docShell.QueryInterface()`
- 条件付き依存: `if (message.name == "SwitchDocumentDirection")` → `this.switchDocumentDirection()`
- 参照: `Ci.nsIWebNavigation`, `docShell.QueryInterface(Ci.nsIWebNavigation).document`, `message.name`, `this.manager.browsingContext.docShell`
- XPCOM: [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md)

## SwitchDocumentDirectionChild.switchDocumentDirection()
- 位置: L14-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.switchDocumentDirection()`
- 参照: `document.defaultView.frames`, `document.dir`, `frame.document`
