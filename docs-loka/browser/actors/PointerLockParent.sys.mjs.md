# browser/actors/PointerLockParent.sys.mjs

source: browser/actors/PointerLockParent.sys.mjs
source-hash: 8ee3f0e13af9badf4bd356369098a14aa2503fd7
lines: 24

## <module>
- 役割: (未記入)

## PointerLockParent.receiveMessage()
- 位置: L6-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.documentGlobal.PointerLock.entered()`, `browser.documentGlobal.PointerLock.exited()`
- 参照: `message.name`, `this.manager.browsingContext.top.currentWindowGlobal.documentPrincipal .originNoSuffix`, `this.manager.browsingContext.top.embedderElement`
