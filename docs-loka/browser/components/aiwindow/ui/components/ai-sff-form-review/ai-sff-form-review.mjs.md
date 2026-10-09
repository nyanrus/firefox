# browser/components/aiwindow/ui/components/ai-sff-form-review/ai-sff-form-review.mjs

source: browser/components/aiwindow/ui/components/ai-sff-form-review/ai-sff-form-review.mjs
source-hash: 6c83d3cefe5e0f92c07de93fb32bdebd1c1dd8f7
lines: 676

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AiSffFormReview.constructor()
- 位置: L81-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `FORM_REVIEW_STATES.PROGRESS`, `this.errorType`, `this.fields`, `this.filledFieldCount`, `this.filling`, `this.state`

## AiSffFormReview.firstUpdated()
- 位置: async L105-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#focusCurrentState()`, `this.dispatchEvent()`

## AiSffFormReview.updated()
- 位置: L121-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.get()`, `changedProperties.has()`, `super.updated()`, `this.#observeReviewFields()`, `this.#updateScrollListeners()`
- 条件付き依存: `if (changedProperties.get("state") !== undefined || retryCompleted)` → `this.#focusCurrentState()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `FORM_REVIEW_STATES.PROGRESS`, `this.#retryUsed`, `this.#reviewedAllFields`, `this.filling`, `this.state`

## AiSffFormReview.#observeReviewFields()
- 位置: L151-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#reviewFieldsElement.addEventListener()`, `this.#reviewFieldsObserver.observe()`, `this.#stopObservingReviewFields()`
- 参照: `FORM_REVIEW_STATES.REVIEW`, `this.#reviewFieldsElement`, `this.#reviewFieldsObserver`, `this.#reviewedAllFields`, `this.#updateReviewCompletion`, `this.reviewFields`, `this.state`

## AiSffFormReview.#stopObservingReviewFields()
- 位置: L173-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#reviewFieldsElement?.removeEventListener()`, `this.#reviewFieldsObserver?.disconnect()`
- 参照: `this.#reviewFieldsElement`, `this.#reviewFieldsObserver`, `this.#updateReviewCompletion`

## AiSffFormReview.#updateReviewCompletion()
- 位置: L183-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopObservingReviewFields()`, `this.requestUpdate()`
- 参照: `this.#reviewFieldsElement`, `this.#reviewedAllFields`

## AiSffFormReview.disconnectedCallback()
- 位置: L198-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#stopObservingReviewFields()`, `this.#teardownScrollListeners()`

## AiSffFormReview.#focusCurrentState()
- 位置: async L209-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ownerDocument.l10n?.translateFragment()`
- 条件付き依存: `if ( section.isConnected && this.state === state && this.stateSection === section )` → `section.focus()`
- 参照: `section.isConnected`, `this.state`, `this.stateSection`

## AiSffFormReview.#updateScrollListeners()
- 位置: L233-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fields.addEventListener()`, `jumpButton.addEventListener()`, `this.#overflowObserver.observe()`, `this.#teardownScrollListeners()`, `this.#updateJumpButtonState()`
- 参照: `FORM_REVIEW_STATES.REVIEW`, `this.#jumpClickHandler`, `this.#overflowObserver`, `this.#scrollHandler`, `this.jumpButton`, `this.reviewFields`, `this.state`

## this.#scrollHandler()
- 位置: L246-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `this.#updateJumpButtonState()`
- 参照: `this.#scrollRafId`

## this.#jumpClickHandler()
- 位置: L257-259
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `fields.scrollHeight`, `fields.scrollTop`

## AiSffFormReview.#updateJumpButtonState()
- 位置: L280-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `jumpButton.hasAttribute()`
- 条件付き依存: `if (jumpButton.hasAttribute("visible") !== show)` → `jumpButton.toggleAttribute()`
- 参照: `fields.clientHeight`, `fields.scrollHeight`, `fields.scrollTop`, `this.jumpButton`, `this.reviewFields`

## AiSffFormReview.#teardownScrollListeners()
- 位置: L302-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#overflowObserver?.disconnect()`
- 条件付き依存: `if (this.#scrollRafId)` → `cancelAnimationFrame()`
- 条件付き依存: `if (this.#scrollHandler)` → `this.reviewFields?.removeEventListener()`
- 条件付き依存: `if (this.#jumpClickHandler)` → `this.jumpButton?.removeEventListener()`
- 参照: `this.#jumpClickHandler`, `this.#overflowObserver`, `this.#scrollHandler`, `this.#scrollRafId`

## AiSffFormReview.#dispatchAction()
- 位置: L331-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AiSffFormReview.#handleInput()
- 位置: L350-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fields.map()`
- 参照: `event.currentTarget.value`, `field.id`, `this.fields`, `this.filling`

## AiSffFormReview.#handleFill()
- 位置: L370-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchAction()`, `this.fields.map()`
- 参照: `FORM_REVIEW_ACTIONS.FILL_FORM`, `this.#reviewedAllFields`, `this.filling`

## AiSffFormReview.#handleRetry()
- 位置: L387-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleFill()`
- 参照: `this.#retryUsed`, `this.filling`

## AiSffFormReview.#handleCancel()
- 位置: L401-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchAction()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `this.filling`

## AiSffFormReview.#handleStop()
- 位置: L414-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchAction()`
- 参照: `FORM_REVIEW_ACTIONS.STOP`

## AiSffFormReview.#handleClose()
- 位置: L423-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchAction()`
- 参照: `FORM_REVIEW_ACTIONS.CLOSE`

## AiSffFormReview.#renderReviewField()
- 位置: L434-449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.#handleInput()`
- 参照: `field.id`, `field.label`, `field.name`, `field.placeholder`, `field.value`, `this.filling`

## AiSffFormReview.#renderReview()
- 位置: L457-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#renderReviewField()`
- 参照: `field.id`, `this.#handleCancel`, `this.#handleFill`, `this.#reviewedAllFields`, `this.fields`, `this.fields.length`, `this.filling`

## AiSffFormReview.#renderProgress()
- 位置: L519-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#handleStop`

## AiSffFormReview.#renderFinal()
- 位置: L554-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `FORM_REVIEW_ERRORS.FILL_FAILED`, `FORM_REVIEW_ERRORS.NO_SUGGESTIONS`, `this.#handleClose`, `this.#handleRetry`, `this.#retryUsed`, `this.errorType`, `this.filledFieldCount`, `this.filling`

## AiSffFormReview.render()
- 位置: L648-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderFinal()`, `this.#renderProgress()`, `this.#renderReview()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `FORM_REVIEW_STATES.PROGRESS`, `FORM_REVIEW_STATES.REVIEW`, `this.state`
