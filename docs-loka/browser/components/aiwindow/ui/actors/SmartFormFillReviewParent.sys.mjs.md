# browser/components/aiwindow/ui/actors/SmartFormFillReviewParent.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillReviewParent.sys.mjs
source-hash: c3a3c87a0d818520e38ffa74336899799a16432f
lines: 196

## <module>
- 役割: (未記入)

## SmartFormFillReviewParent.connect()
- 位置: L47-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#assertRemoteType()`
- 参照: `this.#actionHandler`, `this.#destroyHandler`

## SmartFormFillReviewParent.disconnect()
- 位置: L58-61
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#actionHandler`, `this.#destroyHandler`

## SmartFormFillReviewParent.initialize()
- 位置: L70-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#assertRemoteType()`, `this.sendQuery()`

## SmartFormFillReviewParent.showSuggestions()
- 位置: L83-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#assertRemoteType()`, `this.sendQuery()`

## SmartFormFillReviewParent.showGenerationError()
- 位置: L96-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `VALID_FORM_REVIEW_GENERATION_ERRORS.includes()`, `this.#assertRemoteType()`, `this.sendQuery()`
- 条件付き依存: `if (!VALID_FORM_REVIEW_GENERATION_ERRORS.includes(errorType))` → `Promise.resolve()`

## SmartFormFillReviewParent.receiveMessage()
- 位置: L125-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `VALID_FORM_REVIEW_ACTIONS.includes()`, `this.#actionHandler()`, `this.#assertRemoteType()`
- 条件付き依存: `if (name === FORM_REVIEW_READY_EVENT)` → `this.#notifyReady()`
- 参照: `data?.type`, `this.#actionHandler`

## SmartFormFillReviewParent.#notifyReady()
- 位置: L153-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.dispatchEvent()`
- 参照: `browser?.documentGlobal`, `chromeWindow.CustomEvent`, `this.browsingContext.embedderElement`

## SmartFormFillReviewParent.didDestroy()
- 位置: L170-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.disconnect()`
- 条件付き依存: `if (destroyHandler)` → `destroyHandler()`
- 参照: `this.#destroyHandler`

## SmartFormFillReviewParent.#assertRemoteType()
- 位置: L185-194
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `this.manager.isInProcess`, `this.manager.remoteType`
