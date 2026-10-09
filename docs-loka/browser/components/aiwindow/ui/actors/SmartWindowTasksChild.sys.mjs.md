# browser/components/aiwindow/ui/actors/SmartWindowTasksChild.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartWindowTasksChild.sys.mjs
source-hash: bac8de6c6ac8afc30b11439c7973d340b64a5208
lines: 77

## <module>
- 役割: Smart Window タスク(モニター)の content 側要求を親プロセスへ中継する子アクター。

## SmartWindowTasksChild.handleEvent()
- 位置: L36-75
- 役割: SmartWindowTasks:Request* イベントを許可リストで検査し、対応表で親向けメッセージ名に変換して sendQuery する。結果は :Response か :Error として要素へ返す。
- 触るとき: Smart Window のモニター操作を新しく追加するとき、許可リスト(#VALID_EVENTS_FROM_CONTENT)と対応表(#eventToMessageMap)の両方に足す必要がある。片方だけだと警告を出して捨てられる。
- 呼び出し先: `Cu.cloneInto()`, `SmartWindowTasksChild.#VALID_EVENTS_FROM_CONTENT.has()`, `event.target.dispatchEvent()`, `this.#eventToMessageMap.get()`, `this.sendQuery()`, `this.sendQuery(messageName, event.detail).then()`
- 条件付き依存: `if (!SmartWindowTasksChild.#VALID_EVENTS_FROM_CONTENT.has(event.type))` → `console.warn()`
- 条件付き依存: `if (!messageName)` → `console.warn()`
- 参照: `error.message`, `event.detail`, `event.type`, `this.contentWindow`, `this.contentWindow.CustomEvent`
