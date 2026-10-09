# browser/actors/PointerLockParent.sys.mjs

source: browser/actors/PointerLockParent.sys.mjs
source-hash: 8ee3f0e13af9badf4bd356369098a14aa2503fd7
lines: 24

## <module>
- 役割: 子からのポインターロック通知を受け、トップ文書の PointerLock モジュールへ渡す親側アクター。

## PointerLockParent.receiveMessage()
- 位置: L6-22
- 役割: Entered では発信元のオリジンを添えて entered を、Exited では exited を呼ぶ。
- 触るとき: ロック開始時に渡す情報を変えるとき。
- 呼び出し先: `browser.documentGlobal.PointerLock.entered()`, `browser.documentGlobal.PointerLock.exited()`
- 参照: `message.name`, `this.manager.browsingContext.top.currentWindowGlobal.documentPrincipal .originNoSuffix`, `this.manager.browsingContext.top.embedderElement`
