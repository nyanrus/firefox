# browser/components/aiwindow/ui/actors/SmartWindowTasksChild.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartWindowTasksChild.sys.mjs
source-hash: bac8de6c6ac8afc30b11439c7973d340b64a5208
lines: 77

## <module>
- 役割: (未記入)

## SmartWindowTasksChild.handleEvent()
- 位置: L36-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `SmartWindowTasksChild.#VALID_EVENTS_FROM_CONTENT.has()`, `event.target.dispatchEvent()`, `this.#eventToMessageMap.get()`, `this.sendQuery()`, `this.sendQuery(messageName, event.detail).then()`
- 条件付き依存: `if (!SmartWindowTasksChild.#VALID_EVENTS_FROM_CONTENT.has(event.type))` → `console.warn()`
- 条件付き依存: `if (!messageName)` → `console.warn()`
- 参照: `error.message`, `event.detail`, `event.type`, `this.contentWindow`, `this.contentWindow.CustomEvent`
