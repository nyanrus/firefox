# browser/components/aiwindow/ui/actors/SmartFormFillReviewChild.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillReviewChild.sys.mjs
source-hash: 4209ce623c7906a4ae3e0af003d102c8eaf3e67a
lines: 260

## <module>
- 役割: (未記入)

## SmartFormFillReviewChild.actorCreated()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.addEventListener()`

## SmartFormFillReviewChild.didDestroy()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#destroyed`

## SmartFormFillReviewChild.receiveMessage()
- 位置: async L71-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Cu.cloneInto()`, `VALID_FORM_REVIEW_GENERATION_ERRORS.includes()`, `this.#getReview()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `FORM_REVIEW_STATES.PROGRESS`, `FORM_REVIEW_STATES.REVIEW`, `data.errorType`, `data.fields`, `data?.errorType`, `data?.fields`, `review.errorType`, `review.fields`, `review.filledFieldCount`, `review.filling`, `review.state`, `review.updateComplete`, `this.contentWindow`

## SmartFormFillReviewChild.handleEvent()
- 位置: L122-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `VALID_FORM_REVIEW_ACTIONS.includes()`, `this.#sendAction()`
- 条件付き依存: `if (event.key === "Escape")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape")` → `event.stopPropagation()`
- 条件付き依存: `if (!this.#fillPending)` → `this.#sendAction()`
- 条件付き依存: `if (event.type === FORM_REVIEW_READY_EVENT)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type === FORM_REVIEW_ACTIONS.FILL_FORM)` → `Array.isArray()`
- 条件付き依存: `if (event.type === FORM_REVIEW_ACTIONS.FILL_FORM)` → `event.detail.fields .filter( field => typeof field.id === "string" && typeof field.value === "string" ) .map()`
- 条件付き依存: `if (event.type === FORM_REVIEW_ACTIONS.FILL_FORM)` → `event.detail.fields .filter()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `FORM_REVIEW_ACTIONS.FILL_FORM`, `action.fields`, `event.detail`, `event.detail.fields`, `event.key`, `event.type`, `field.id`, `field.value`, `this.#fillPending`

## SmartFormFillReviewChild.#sendAction()
- 位置: L171-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sendFillAction()`
- 条件付き依存: `if (action.type !== FORM_REVIEW_ACTIONS.FILL_FORM)` → `this.sendAsyncMessage()`
- 参照: `FORM_REVIEW_ACTIONS.FILL_FORM`, `action.type`, `this.#fillPending`

## SmartFormFillReviewChild.#sendFillAction()
- 位置: async L191-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#showResult()`, `this.sendQuery()`
- 条件付き依存: `if (!this.#destroyed)` → `this.#showResult()`
- 条件付き依存: `if (result?.cancelled)` → `this.#sendAction()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `FORM_REVIEW_ERRORS.FILL_FAILED`, `result.hasErrors`, `result?.cancelled`, `result?.filledFieldCount`, `this.#destroyed`, `this.#fillPending`

## SmartFormFillReviewChild.#showResult()
- 位置: L232-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getReview()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `review.errorType`, `review.filledFieldCount`, `review.filling`, `review.state`, `this.#destroyed`, `this.#fillPending`

## SmartFormFillReviewChild.#getReview()
- 位置: L255-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.waiveXrays()`, `this.document.querySelector()`
