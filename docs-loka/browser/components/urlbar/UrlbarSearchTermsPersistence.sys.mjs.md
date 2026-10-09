# browser/components/urlbar/UrlbarSearchTermsPersistence.sys.mjs

source: browser/components/urlbar/UrlbarSearchTermsPersistence.sys.mjs
source-hash: 05db07d0ed434bdac88487acdbc0332e1e8c9f37
lines: 508

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.UrlbarShared.getLogger()`

## _UrlbarSearchTermsPersistence.init()
- 位置: async L66-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings()`, `lazy.logger.error()`, `this.#setSearchProviderInfo()`, `this.#urlbarSearchTermsPersistenceSettings.get()`, `this.#urlbarSearchTermsPersistenceSettings.on()`
- 参照: `this.#initialized`, `this.#originalProviderInfo`, `this.#urlbarSearchTermsPersistenceSettings`, `this.#urlbarSearchTermsPersistenceSettingsSync`

## this.#urlbarSearchTermsPersistenceSettingsSync()
- 位置: L81-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onSettingsSync()`

## _UrlbarSearchTermsPersistence.uninit()
- 位置: L94-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logger.error()`, `this.#urlbarSearchTermsPersistenceSettings.off()`
- 参照: `this.#initialized`, `this.#urlbarSearchTermsPersistenceSettings`, `this.#urlbarSearchTermsPersistenceSettingsSync`

## _UrlbarSearchTermsPersistence.getSearchProviderInfo()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#searchProviderInfo`

## _UrlbarSearchTermsPersistence.overrideSearchTermsPersistenceForTests()
- 位置: L127-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setSearchProviderInfo()`
- 参照: `this.#originalProviderInfo`

## _UrlbarSearchTermsPersistence.getSearchTerm()
- 位置: L145-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^https?:\/\//.test()`, `Services.uriFixup.getFixupURIInfo()`, `searchTerm.replaceAll()`, `searchTermWithSpacesRemoved.startsWith()`, `this.#getProviderInfoForURL()`
- 条件付き依存: `if (provider)` → `lazy.SearchService.parseSubmissionURL()`
- 条件付き依存: `if (provider)` → `this.isDefaultPage()`
- 条件付き依存: `if (!(provider))` → `lazy.SearchService.parseSubmissionURL()`
- 条件付き依存: `if (!(provider))` → `result.engine.searchTermFromResult()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `info.keywordAsSent`, `lazy.ConfigSearchEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `result.engine`, `result.terms`, `searchTerm.length`, `uri.spec`, `uri?.spec`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## _UrlbarSearchTermsPersistence.shouldPersist()
- 位置: L215-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.fromURI()`, `this.isDefaultPage()`, `this.searchModeMatchesState()`
- 参照: `persist.searchTerms`, `state.persist`, `state.persist.origin`, `state.persist.pathname`, `state.persist.provider`, `state.searchModes?.confirmed`, `url.origin`, `url.pathname`

## _UrlbarSearchTermsPersistence.setPersistenceState()
- 位置: L276-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.fromURI()`, `this.#getProviderInfoForURL()`, `this.#searchModeForUrl()`, `this.getSearchTerm()`
- 参照: `result.engineName`, `result.isDefaultEngine`, `state.persist`, `state.persist.isDefaultEngine`, `state.persist.origin`, `state.persist.originalEngineName`, `state.persist.originalURI`, `state.persist.pathname`, `state.persist.provider`, `state.persist.searchTerms`, `uri.spec`, `uri?.spec`, `url.origin`, `url.pathname`

## _UrlbarSearchTermsPersistence.searchModeMatchesState()
- 位置: L351-359
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `searchMode?.engineName`, `state.persist?.isDefaultEngine`, `state.persist?.originalEngineName`

## _UrlbarSearchTermsPersistence.onSearchModeChanged()
- 位置: L361-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchModeMatchesState()`, `window.gURLBar.getBrowserState()`
- 条件付き依存: `if ( state.persist.shouldPersist && !this.searchModeMatchesState(state.searchModes?.confirmed, state) )` → `window.gURLBar.removeAttribute()`
- 参照: `state.persist.shouldPersist`, `state.searchModes?.confirmed`, `state?.persist`, `window.gBrowser.selectedBrowser`

## _UrlbarSearchTermsPersistence.#onSettingsSync()
- 位置: async L378-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (current)` → `lazy.logger.debug()`
- 条件付き依存: `if (current)` → `this.#setSearchProviderInfo()`
- 条件付き依存: `if (!(current))` → `lazy.logger.debug()`
- 参照: `event.data?.current`, `this.#originalProviderInfo`
- XPCOM: `Services.obs`

## _UrlbarSearchTermsPersistence.#searchModeForUrl()
- 位置: L397-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.parseSubmissionURL()`
- 参照: `lazy.ConfigSearchEngine`, `lazy.SearchService.defaultEngine`, `result.engine`, `result.engine.name`

## _UrlbarSearchTermsPersistence.#setSearchProviderInfo()
- 位置: L420-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `providerInfo.map()`
- 参照: `provider.searchPageRegexp`, `this.#searchProviderInfo`

## _UrlbarSearchTermsPersistence.#getProviderInfoForURL()
- 位置: L438-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info.searchPageRegexp.test()`, `this.#searchProviderInfo.find()`

## _UrlbarSearchTermsPersistence.isDefaultPage()
- 位置: L455-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.fromURI()`
- 条件付き依存: `if (provider.includeParams?.length)` → `searchParams.has()`
- 条件付き依存: `if (provider.includeParams?.length)` → `searchParams.get()`
- 条件付き依存: `if (provider.includeParams?.length)` → `param?.values.includes()`
- 条件付き依存: `if (provider.excludeParams)` → `searchParams.get()`
- 条件付き依存: `if (provider.excludeParams)` → `param.values?.includes()`
- 参照: `param.canBeMissing`, `param.key`, `param.values?.length`, `provider.excludeParams`, `provider.includeParams`, `provider.includeParams?.length`, `searchParams.size`
