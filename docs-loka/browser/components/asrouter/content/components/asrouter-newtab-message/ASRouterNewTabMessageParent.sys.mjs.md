# browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageParent.sys.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/ASRouterNewTabMessageParent.sys.mjs
source-hash: 14c91eac62dd5af51a0b3c919ca69cb007201130
lines: 63

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ASRouterNewTabMessageParent.receiveMessage()
- 位置: L16-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SpecialMessageActions.handleAction()`, `this.#evaluateTargetings()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `message.data.action`, `message.data.targetings`, `message.name`, `this.browsingContext.top.embedderElement`, `this.manager.remoteType`

## ASRouterNewTabMessageParent.#evaluateTargetings()
- 位置: L44-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.ASRouter.evaluateExpression()`, `targetings.map()`
- 条件付き依存: `if (!result.evaluationStatus.success)` → `console.error()`
- 参照: `lazy.ASRouterTargeting.Environment`, `result.evaluationStatus.result`, `result.evaluationStatus.success`
