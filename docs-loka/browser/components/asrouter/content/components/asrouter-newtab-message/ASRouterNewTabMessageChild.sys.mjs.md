# browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageChild.sys.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageChild.sys.mjs
source-hash: a9d264edf76d3726a890fe8288da3fe77f4604ee
lines: 51

## <module>
- 役割: (未記入)

## ASRouterNewTabMessageChild.handleEvent()
- 位置: L6-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enqueueTargetingEvaluation()`, `this.sendAsyncMessage()`
- 参照: `event.detail`, `event.target`, `event.type`

## ASRouterNewTabMessageChild.#enqueueTargetingEvaluation()
- 位置: async L29-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Cu.waiveXrays()`, `Cu.waiveXrays(el).setMatchedState()`, `results.findIndex()`, `this.sendQuery()`
- 参照: `Cu.waiveXrays(detail).targetings`, `el.isConnected`
