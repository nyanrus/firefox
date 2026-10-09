# browser/extensions/newtab/lib/Widgets/RecentSearchesFeed.sys.mjs

source: browser/extensions/newtab/lib/Widgets/RecentSearchesFeed.sys.mjs
source-hash: 2b2f778334100af6ec4bde8590c0cec7018fbc01
lines: 374

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `WIDGET_REGISTRY.find()`

## RecentSearchesFeed.#onTrendingTab()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState()?.Prefs.values`

## RecentSearchesFeed.enabled()
- 位置: L87-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isWidgetEnabled()`, `this.store.getState()`
- 参照: `this.store.getState()?.Prefs.values`

## RecentSearchesFeed.#fetchSearches()
- 位置: async L104-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `entries .sort()`, `entries .sort((a, b) => b.lastUsed - a.lastUsed) .slice()`, `entries .sort((a, b) => b.lastUsed - a.lastUsed) .slice(0, MAX_SEARCHES) .map()`, `lazy.FormHistory.search()`, `lazy.SearchService.init()`, `lazy.UrlbarPrefs.get()`, `parseInt()`
- 条件付き依存: `if (lastDefaultChanged !== -1)` → `Math.min()`
- 参照: `a.lastUsed`, `b.lastUsed`, `engine.name`, `entry.lastUsed`, `entry.value`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.SearchService.defaultEngine`

## RecentSearchesFeed.#fetchTrending()
- 位置: async L145-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(fetchData?.remote ?? []).map()`, `controller.fetch()`, `lazy.SearchService.init()`, `lazy.SearchSuggestionController.engineOffersSuggestions()`
- 参照: `engine.name`, `fetchData?.remote`, `lazy.SearchService.defaultEngine`, `lazy.SearchSuggestionController`, `suggestion.value`

## RecentSearchesFeed.#startObserving()
- 位置: L171-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`, `this.#observing`
- XPCOM: `Services.obs`

## RecentSearchesFeed.#stopObserving()
- 位置: L180-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`, `this.#observing`
- XPCOM: `Services.obs`

## RecentSearchesFeed.observe()
- 位置: L200-216
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === FORM_HISTORY_TOPIC)` → `FORM_HISTORY_CHANGES.has()`
- 条件付き依存: `if (FORM_HISTORY_CHANGES.has(data))` → `this.#queueUpdate()`
- 条件付き依存: `if ( topic === lazy.SearchUtils.TOPIC_ENGINE_MODIFIED && data === lazy.SearchUtils.MODIFIED_TYPE.DEFAULT )` → `this.#queueUpdate()`
- 条件付き依存: `if ( topic === lazy.SearchUtils.TOPIC_ENGINE_MODIFIED && data === lazy.SearchUtils.MODIFIED_TYPE.DEFAULT )` → `this.#onTrendingTab()`
- 条件付き依存: `if (this.#onTrendingTab())` → `this.updateTrending()`
- 参照: `lazy.SearchUtils.MODIFIED_TYPE.DEFAULT`, `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`

## RecentSearchesFeed.#queueUpdate()
- 位置: L225-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (this.#observing && this.enabled)` → `this.updateSearches()`
- 参照: `this.#observing`, `this.#updateQueued`, `this.enabled`
- XPCOM: `Services.tm`

## RecentSearchesFeed.updateSearches()
- 位置: async L242-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `console.error()`, `this.#fetchSearches()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_RECENT_SEARCHES_UPDATE`

## RecentSearchesFeed.updateTrending()
- 位置: async L260-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `console.error()`, `this.#fetchTrending()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_RECENT_SEARCHES_UPDATE`

## RecentSearchesFeed.removeSearch()
- 位置: async L282-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.FormHistory.update()`, `this.updateSearches()`
- 参照: `action.data`, `lazy.DEFAULT_FORM_HISTORY_PARAM`

## RecentSearchesFeed.openSearch()
- 位置: async L305-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `console.error()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.SearchUIUtils.loadSearch()`
- 参照: `action._target?.window`, `action.data`
- XPCOM: `Services.scriptSecurityManager`

## RecentSearchesFeed.#start()
- 位置: async L329-335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onTrendingTab()`, `this.#startObserving()`, `this.updateSearches()`
- 条件付き依存: `if (this.#onTrendingTab())` → `this.updateTrending()`

## RecentSearchesFeed.onAction()
- 位置: async L337-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ENABLEMENT_PREFS.has()`, `this.#stopObserving()`, `this.openSearch()`, `this.removeSearch()`
- 条件付き依存: `if (this.enabled)` → `this.#start()`
- 条件付き依存: `if ( action.data?.name === TAB_PREF && action.data.value === TRENDING_TAB && this.enabled )` → `this.updateTrending()`
- 条件付き依存: `if (!(this.enabled))` → `this.#stopObserving()`
- 参照: `action.data.value`, `action.data?.name`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.UNINIT`, `at.WIDGETS_RECENT_SEARCHES_OPEN_LINK`, `at.WIDGETS_RECENT_SEARCHES_REMOVE_SEARCH`, `this.enabled`
