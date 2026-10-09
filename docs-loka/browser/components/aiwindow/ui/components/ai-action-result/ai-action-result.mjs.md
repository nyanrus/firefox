# browser/components/aiwindow/ui/components/ai-action-result/ai-action-result.mjs

source: browser/components/aiwindow/ui/components/ai-action-result/ai-action-result.mjs
source-hash: 2b08f2076c3d8b9ad43cc8e3f0505487e9905544
lines: 394

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIActionResult.constructor()
- 位置: L65-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.canUndo`, `this.isExpanded`, `this.isLoading`, `this.label`, `this.labelL10nArgs`, `this.labelL10nId`, `this.labelLink`, `this.rows`, `this.summary`, `this.summaryL10nArgs`, `this.summaryL10nId`

## AIActionResult.willUpdate()
- 位置: L91-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`
- 条件付き依存: `if (this.isLoading)` → `this.#cancelSweepAnim()`
- 条件付き依存: `if (this.isLoading)` → `this.removeAttribute()`
- 条件付き依存: `if (this.isLoading)` → `this.#clearSweepTimer()`
- 条件付き依存: `if (!(this.isLoading))` → `changed.has()`
- 条件付き依存: `if (!(this.isLoading))` → `changed.get()`
- 条件付き依存: `if ( changed.has("isLoading") && changed.get("isLoading") && this.#loadingLabelSnapshot )` → `this.#clearSweepTimer()`
- 条件付き依存: `if ( changed.has("isLoading") && changed.get("isLoading") && this.#loadingLabelSnapshot )` → `setTimeout()`
- 条件付き依存: `if ( changed.has("isLoading") && changed.get("isLoading") && this.#loadingLabelSnapshot )` → `this.#finishSweep()`
- 条件付き依存: `if (!shimmering)` → `this.removeAttribute()`
- 条件付き依存: `if (!shimmering)` → `this.#cancelSweepAnim()`
- 参照: `AIActionResult.SWEEP_MAX_MS`, `this.#awaitingSweep`, `this.#loadingLabelSnapshot`, `this.#sweepTimer`, `this.isLoading`, `this.label`, `this.labelL10nArgs`, `this.labelL10nId`, `this.labelLink`

## AIActionResult.updated()
- 位置: L131-135
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#awaitingSweep && !this.#sweepAnim)` → `this.#finishCurrentSweep()`
- 参照: `this.#awaitingSweep`, `this.#sweepAnim`

## AIActionResult.#finishCurrentSweep()
- 位置: L142-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `Math.pow()`, `Number()`, `label ?.getAnimations()`, `label ?.getAnimations?.() .find()`, `label.animate()`, `this.#finishSweep()`, `this.#sweepAnim.finished .then()`, `this.#sweepAnim.finished .then(() => this.#finishSweep()) .catch()`, `this.renderRoot?.querySelector()`, `this.setAttribute()`
- 条件付き依存: `if (!label || !loop)` → `this.#finishSweep()`
- 参照: `AIActionResult.SHIMMER_CYCLE_MS`, `a.animationName`, `loop.currentTime`, `this.#sweepAnim`

## AIActionResult.connectedCallback()
- 位置: L185-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.renderRoot.addEventListener()`
- 参照: `this.#handleLabelLinkClick`

## AIActionResult.disconnectedCallback()
- 位置: L194-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#cancelSweepAnim()`, `this.#clearSweepTimer()`, `this.renderRoot.removeEventListener()`
- 参照: `this.#handleLabelLinkClick`

## AIActionResult.#clearSweepTimer()
- 位置: L205-210
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#sweepTimer)` → `clearTimeout()`
- 参照: `this.#sweepTimer`

## AIActionResult.#cancelSweepAnim()
- 位置: L212-217
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#sweepAnim)` → `this.#sweepAnim.cancel()`
- 参照: `this.#sweepAnim`

## AIActionResult.#finishSweep()
- 位置: L219-228
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#awaitingSweep)` → `this.#clearSweepTimer()`
- 条件付き依存: `if (this.#awaitingSweep)` → `this.requestUpdate()`
- 参照: `this.#awaitingSweep`

## AIActionResult.#handleUndo()
- 位置: L230-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AIActionResult.#handleLabelLinkClick()
- 位置: L236-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.classList.contains()`, `event .composedPath()`, `event .composedPath() .some()`
- 条件付き依存: `if (onLabelLink)` → `event.stopPropagation()`

## AIActionResult.#handleToggle()
- 位置: L249-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.isExpanded`

## AIActionResult.#renderLabelContent()
- 位置: L263-277
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (link)` → `html()`
- 参照: `link.href`, `link.l10nName`

## AIActionResult.render()
- 位置: L279-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `keyed()`, `this.#renderDetails()`, `this.#renderLabelContent()`
- 参照: `label.label`, `label.labelL10nArgs`, `label.labelL10nId`, `label.labelLink`, `this.#awaitingSweep`, `this.#handleToggle`, `this.#loadingLabelSnapshot`, `this.isExpanded`, `this.isLoading`, `this.label`, `this.labelL10nArgs`, `this.labelL10nId`, `this.labelLink`

## AIActionResult.#renderDetails()
- 位置: L326-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `keyed()`, `this.#renderLabelContent()`, `this.rows.map()`
- 参照: `row.items`, `row.items?.length`, `row.label`, `row.labelL10nArgs`, `row.labelL10nId`, `row.link`, `this.#handleUndo`, `this.canUndo`, `this.isExpanded`, `this.summary`, `this.summaryL10nArgs`, `this.summaryL10nId`
