# browser/components/urlbar/UrlbarProviderAiChat.sys.mjs

source: browser/components/urlbar/UrlbarProviderAiChat.sys.mjs
source-hash: 176fcfff0171b8dc3a060608b778480703fe608c
lines: 307

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## stringsAreUnrelated()
- 位置: L46-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `str1.includes()`, `str2.includes()`
- 参照: `str1.length`, `str2.length`

## UrlbarProviderAiChat.constructor()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderAiChat.type()
- 位置: L75-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderAiChat.isActive()
- 位置: async L90-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `queryContext.restrictInSearchMode()`
- 参照: `UrlbarProviderAiChat.MIN_CHARS_FOR_CHAT`, `controller.browserWindow`, `queryContext.trimmedSearchString.length`

## UrlbarProviderAiChat.startQuery()
- 位置: async L113-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`, `this.#determineIntent()`
- 条件付き依存: `if (!canReturnHeuristicResult)` → `this.logger.info()`
- 条件付き依存: `if (!canReturnHeuristicResult)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (heuristic)` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if (heuristic)` → `UrlbarUtils.getEngineIconUrl()`
- 条件付き依存: `if (heuristic)` → `addCallback()`
- 参照: `UrlbarProviderAiChat.CHAT_ICON_URL`, `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.AI_CHAT`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `new SkippableTimer({ name: "ProviderAiChat", time: lazy.UrlbarPrefs.get("delay"), logger: this.logger, }).promise`, `queryContext.isPrivate`, `queryContext.sapName`, `queryContext.searchString`, `this.logger`, `this.queryInstance`

## UrlbarProviderAiChat.onEngagement()
- 位置: async L190-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.ask()`, `controller.input.getContextPageUrl()`, `controller.input.getResolvedContextWebsites()`, `details.event?.type.startsWith()`
- 条件付き依存: `if (queryContext.sapName == "urlbar")` → `lazy.AIWindow.isAIWindowNewTabPage()`
- 条件付き依存: `if ( selectedBrowser && lazy.AIWindow.isAIWindowNewTabPage(selectedBrowser.currentURI) )` → `selectedBrowser.browsingContext?.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (!( selectedBrowser && lazy.AIWindow.isAIWindowNewTabPage(selectedBrowser.currentURI) ))` → `this.#getSidebarBrowser()`
- 条件付き依存: `if (!( selectedBrowser && lazy.AIWindow.isAIWindowNewTabPage(selectedBrowser.currentURI) ))` → `browser.browsingContext?.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (!(queryContext.sapName == "urlbar"))` → `win.browsingContext?.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (!actor)` → `this.logger.error()`
- 参照: `controller.input.inputField.documentGlobal`, `controller.input.sapLocation`, `queryContext.sapName`, `queryContext.searchString`, `selectedBrowser.currentURI`, `this.#lastIntentEvaluation.intent`, `win.closed`, `win.gBrowser?.selectedBrowser`

## UrlbarProviderAiChat.#getSidebarBrowser()
- 位置: async L234-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindowUI.isSidebarOpen()`, `win.document.getElementById()`
- 条件付き依存: `if (!lazy.AIWindowUI.isSidebarOpen(win))` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if (browser.currentURI?.spec !== lazy.AIWINDOW_URL)` → `browser.addEventListener()`
- 条件付き依存: `if (browser.currentURI.spec === lazy.AIWINDOW_URL)` → `resolve()`
- 参照: `browser.currentURI.spec`, `browser.currentURI?.spec`, `lazy.AIWINDOW_URL`, `lazy.AIWindowUI.BROWSER_ID`

## UrlbarProviderAiChat.#determineIntent()
- 位置: async L261-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.UrlbarProviderHeuristicFallback.matchUnknownUrl()`, `stringsAreUnrelated()`
- 条件付き依存: `if ( !intent || Date.now() - this.#lastIntentEvaluation.timestamp > MAX_TIME_FOR_DEBOUNCE_MS || stringsAreUnrelated( queryContext.searchString, this.#lastIntentE...)` → `lazy.IntentClassifier.getPromptIntent()`
- 条件付き依存: `if ( !intent || Date.now() - this.#lastIntentEvaluation.timestamp > MAX_TIME_FOR_DEBOUNCE_MS || stringsAreUnrelated( queryContext.searchString, this.#lastIntentE...)` → `this.logger.error()`
- 条件付き依存: `if ( !intent || Date.now() - this.#lastIntentEvaluation.timestamp > MAX_TIME_FOR_DEBOUNCE_MS || stringsAreUnrelated( queryContext.searchString, this.#lastIntentE...)` → `Date.now()`
- 参照: `queryContext.searchString`, `this.#lastIntentEvaluation`, `this.#lastIntentEvaluation.intent`, `this.#lastIntentEvaluation.queryString`, `this.#lastIntentEvaluation.timestamp`
