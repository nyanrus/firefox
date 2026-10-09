# browser/components/genai/content/page-assist.mjs

source: browser/components/genai/content/page-assist.mjs
source-hash: b03ddf77300d43aa91b167148ab645b48ed878ab
lines: 377

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## PageAssistInput.inputTemplate()
- 位置: L27-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.accessKey`, `this.ariaLabel`, `this.class`, `this.disabled`, `this.handleInput`, `this.name`, `this.parentDisabled`, `this.placeholder`, `this.redispatchEvent`, `this.title`, `this.value`

## PageAssist.constructor()
- 位置: L71-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.aiResponse`, `this.currentMatchIndex`, `this.highlightAll`, `this.isCurrentPageReaderable`, `this.matchCountQty`, `this.snippets`, `this.userPrompt`

## PageAssist._browserWin()
- 位置: L82-84
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.documentGlobal?.browsingContext?.topChromeWindow`

## PageAssist._gBrowser()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._browserWin?.gBrowser`

## PageAssist.connectedCallback()
- 位置: L89-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this._attachReaderModeListener()`, `this._initURLChange()`, `this._setupFinder()`, `this.documentGlobal.addEventListener()`
- 参照: `this._onUnload`

## this._onUnload()
- 位置: L93-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanup()`

## PageAssist.disconnectedCallback()
- 位置: L100-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this._cleanup()`
- 条件付き依存: `if (this.browser && this.browser.finder)` → `this.browser.finder.removeResultListener()`
- 条件付き依存: `if (this._onUnload)` → `this.documentGlobal.removeEventListener()`
- 参照: `this._onUnload`, `this.browser`, `this.browser.finder`

## PageAssist._setupFinder()
- 位置: L114-141
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!gBrowser)` → `console.warn()`
- 条件付き依存: `if (this.browser && this.browser.finder)` → `this.browser.finder.removeResultListener()`
- 条件付き依存: `if (this.browser && this.browser.finder)` → `this.browser.finder.addResultListener()`
- 条件付き依存: `if (!(this.browser && this.browser.finder))` → `console.warn()`
- 参照: `gBrowser.selectedBrowser`, `this._gBrowser`, `this.browser`, `this.browser.finder`

## PageAssist._cleanup()
- 位置: L143-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`
- 条件付き依存: `if (gBrowser && this._progressListener)` → `gBrowser.removeTabsProgressListener()`
- 条件付き依存: `if (gBrowser?.tabContainer && this._onTabSelect)` → `gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this._onReaderModeChange)` → `lazy.AboutReaderParent.removeMessageListener()`
- 参照: `gBrowser?.tabContainer`, `this._gBrowser`, `this._onReaderModeChange`, `this._onTabSelect`, `this._progressListener`

## PageAssist._attachReaderModeListener()
- 位置: L170-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutReaderParent.addMessageListener()`
- 参照: `this._onReaderModeChange`

## receiveMessage()
- 位置: L172-181
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browser.isArticle`, `msg?.target`, `this._gBrowser?.selectedBrowser`, `this.isCurrentPageReaderable`

## PageAssist._initURLChange()
- 位置: L193-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.addTabsProgressListener()`, `gBrowser.tabContainer.addEventListener()`, `this._onTabSelect()`
- 参照: `this._gBrowser`, `this._onTabSelect`, `this._progressListener`

## this._onTabSelect()
- 位置: L199-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setupFinder()`
- 参照: `browser?.isArticle`, `gBrowser.selectedBrowser`, `this.isCurrentPageReaderable`

## onLocationChange()
- 位置: L207-212
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browser?.isArticle`, `this.isCurrentPageReaderable`, `webProgress?.isTopLevel`

## PageAssist._fetchPageData()
- 位置: async L233-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.fetchPageData()`, `windowGlobal.getActor()`
- 参照: `gBrowser?.selectedBrowser?.browsingContext?.currentWindowGlobal`, `this._gBrowser`

## PageAssist._clearFinder()
- 位置: L248-256
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.browser?.finder)` → `this.browser.finder.removeSelection()`
- 条件付き依存: `if (this.browser?.finder)` → `this.browser.finder.highlight()`
- 参照: `this.browser?.finder`, `this.currentMatchIndex`, `this.matchCountQty`, `this.snippets`

## PageAssist._handlePromptInput()
- 位置: L258-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browser.finder.fastFind()`, `this.browser.finder.requestMatchesCount()`
- 条件付き依存: `if (!value)` → `this._clearFinder()`
- 条件付き依存: `if (this.highlightAll)` → `this.browser.finder.highlight()`
- 参照: `e.target.value`, `this.highlightAll`, `this.userPrompt`

## PageAssist.onMatchesCountResult()
- 位置: L283-287
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.current`, `result.snippets`, `result.total`, `this.currentMatchIndex`, `this.matchCountQty`, `this.snippets`

## PageAssist.onHighlightFinished()
- 位置: L290-292
- 役割: (未記入)
- 触るとき: (未記入)

## PageAssist.onFindResult()
- 位置: L295-306
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsITypeAheadFind.FIND_NOTFOUND`, `result.result`, `this.currentMatchIndex`, `this.matchCountQty`, `this.snippets`
- XPCOM: [`nsITypeAheadFind`](../../../../toolkit/components/typeaheadfind/nsITypeAheadFind.idl.md)

## PageAssist._handleSubmit()
- 位置: async L308-319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PageAssist.fetchAiResponse()`, `this._fetchPageData()`
- 参照: `this.aiResponse`, `this.userPrompt`

## PageAssist.render()
- 位置: L321-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.snippets.map()`
- 参照: `snippet.after`, `snippet.before`, `snippet.match`, `this._handlePromptInput`, `this._handleSubmit`, `this.aiResponse`, `this.snippets.length`, `this.userPrompt`
