# browser/components/urlbar/UrlbarProviderSemanticHistorySearch.sys.mjs

source: browser/components/urlbar/UrlbarProviderSemanticHistorySearch.sys.mjs
source-hash: d3d6a9490a6308ff7a4a2687c404aa9c32f9a489
lines: 287

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getFloatPref()`, `getPlacesSemanticHistoryManager()`, `lazy.UrlbarShared.getLogger()`

## UrlbarProviderSemanticHistorySearch.semanticManager()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.semanticManager`

## UrlbarProviderSemanticHistorySearch.type()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderSemanticHistorySearch.isActive()
- 位置: async L95-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 条件付き依存: `if (canUse)` → `lazy.semanticManager.hasSufficientEntriesForSearching()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.semanticManager.canUseSemanticSearch`, `lazy.semanticManager.isEnabledForSmartWindow`, `queryContext.sapName`, `queryContext.searchMode?.source`, `queryContext.searchString.length`

## UrlbarProviderSemanticHistorySearch.startQuery()
- 位置: async L130-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarProviderOpenTabs.getOpenTabUrls()`, `lazy.semanticManager.infer()`, `openTabs.get()`, `this.#addAsSwitchToTab()`, `this.#maybeRecordExposure()`
- 条件付き依存: `if ( !this.#addAsSwitchToTab( openTabs.get(res.url), queryContext, res, addCallback ) )` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if ( !this.#addAsSwitchToTab( openTabs.get(res.url), queryContext, res, addCallback ) )` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if ( !this.#addAsSwitchToTab( openTabs.get(res.url), queryContext, res, addCallback ) )` → `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.isPrivate`, `res.frecency`, `res.title`, `res.url`, `resultObject.results`, `this.queryInstance`
- XPCOM: `Services.urlFormatter`

## UrlbarProviderSemanticHistorySearch.#addAsSwitchToTab()
- 位置: L185-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.createTabSwitchSecondaryAction()`, `UrlbarUtils.getUserContextData()`, `addCallback()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `openTabs?.size`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.tabGroup`, `queryContext.userContextId`, `res.lastVisit`, `res.title`, `res.url`

## UrlbarProviderSemanticHistorySearch.#maybeRecordExposure()
- 位置: L230-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.urlbar.getEnrollmentMetadata()`, `lazy.NimbusFeatures.urlbar.recordExposureEvent()`, `lazy.logger.debug()`, `lazy.logger.warn()`
- 参照: `UrlbarProviderSemanticHistorySearch.#exposureRecorded`, `lazy.EnrollmentType.EXPERIMENT`, `lazy.EnrollmentType.ROLLOUT`, `metadata.slug`, `metadata?.slug`

## UrlbarProviderSemanticHistorySearch.getPriority()
- 位置: L269-271
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderSemanticHistorySearch.onEngagement()
- 位置: L278-285
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove(result.payload.url).catch()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `console.error`, `details.selType`, `result.payload.url`
