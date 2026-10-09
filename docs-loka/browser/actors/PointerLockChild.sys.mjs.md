# browser/actors/PointerLockChild.sys.mjs

source: browser/actors/PointerLockChild.sys.mjs
source-hash: f042fff98fbd3c26fb2acfe2964e9dd57e588012
lines: 18

## <module>
- 役割: ページのポインターロック開始・終了の DOM イベントを親プロセスへ中継する子側アクター。

## PointerLockChild.handleEvent()
- 位置: L6-16
- 役割: MozDOMPointerLock:Entered と :Exited を、対応する PointerLock:Entered と :Exited メッセージに変えて送る。
- 触るとき: ロック状態の通知内容やイベント名を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `event.type`
