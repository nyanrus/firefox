# browser/components/urlbar/UrlbarProviderInputHistory.sys.mjs

source: browser/components/urlbar/UrlbarProviderInputHistory.sys.mjs
source-hash: 74113d386e1308d6df25f079915e55835821bd39
lines: 264

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## UrlbarProviderInputHistory.type()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderInputHistory.isActive()
- 位置: async L90-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`

## UrlbarProviderInputHistory.startQuery()
- 位置: async L106-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `addCallback()`, `conn.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.PlacesUtils.toDate()`, `lazy.PlacesUtils.toDate(bookmarkDatePRTime).getTime()`, `lazy.PlacesUtils.toDate(lastVisitPRTime).getTime()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.getIconForUrl()`, `lowerCaseTag.includes()`, `queryContext.tokens.some()`, `row.getResultByName()`, `tag.toLocaleLowerCase()`, `tags.split()`, `tags.split(",").filter()`, `this._getAdaptiveQuery()`
- 条件付き依存: `if (openPageCount > 0 && lazy.UrlbarPrefs.get("suggest.openpage"))` → `row.getResultByName()`
- 条件付き依存: `if (openPageCount > 0 && lazy.UrlbarPrefs.get("suggest.openpage"))` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if (openPageCount > 0 && lazy.UrlbarPrefs.get("suggest.openpage"))` → `UrlbarUtils.getUserContextData()`
- 条件付き依存: `if (openPageCount > 0 && lazy.UrlbarPrefs.get("suggest.openpage"))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (openPageCount > 0 && lazy.UrlbarPrefs.get("suggest.openpage"))` → `UrlbarUtils.createTabSwitchSecondaryAction()`
- 条件付き依存: `if (openPageCount > 0 && lazy.UrlbarPrefs.get("suggest.openpage"))` → `addCallback()`
- 条件付き依存: `if (!(bookmarked && lazy.UrlbarPrefs.get("suggest.bookmark")))` → `lazy.UrlbarPrefs.get()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.currentPage`, `this.queryInstance`, `token.lowerCaseValue`
- XPCOM: `Services.urlFormatter`

## UrlbarProviderInputHistory.onEngagement()
- 位置: L220-237
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( details.selType == "dismiss" && result.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `UrlbarUtils.removeInputHistory( result.payload.url, queryContext.searchString ).catch()`
- 条件付き依存: `if ( details.selType == "dismiss" && result.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `UrlbarUtils.removeInputHistory()`
- 条件付き依存: `if ( details.selType == "dismiss" && result.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `lazy.PlacesUtils.history.remove(result.payload.url).catch()`
- 条件付き依存: `if ( details.selType == "dismiss" && result.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if ( details.selType == "dismiss" && result.type == lazy.UrlbarShared.RESULT_TYPE.URL )` → `controller.removeResult()`
- 参照: `console.error`, `details.selType`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.searchString`, `result.payload.url`, `result.type`

## UrlbarProviderInputHistory._getAdaptiveQuery()
- 位置: L247-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`
- 参照: `Ci.mozIPlacesAutoComplete.MATCH_ANYWHERE`, `lazy.PlacesUtils.tagsFolderId`, `lazy.SQL_ADAPTIVE_QUERY`, `queryContext.isPrivate`, `queryContext.lowerCaseSearchString`, `queryContext.maxResults`
