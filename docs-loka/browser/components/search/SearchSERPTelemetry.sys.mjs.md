# browser/components/search/SearchSERPTelemetry.sys.mjs

source: browser/components/search/SearchSERPTelemetry.sys.mjs
source-hash: 6e716a3a494fdd724f7197530f2b91a8ed812722
lines: 2289

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## logConsole()
- 位置: L20-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.createInstance()`
- 参照: `lazy.SearchUtils.loggingEnabled`

## TelemetryHandler.setBrowserContentSource()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserContentSourceMap.set()`

## TelemetryHandler.constructor()
- 位置: L384-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findItemForBrowser.bind()`
- 参照: `this._contentHandler`

## TelemetryHandler.init()
- 位置: async L395-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.addListener()`, `Services.wm.getEnumerator()`, `lazy.RemoteSettings()`, `lazy.logConsole.error()`, `this._contentHandler.init()`, `this._registerWindow()`, `this._setSearchProviderInfo()`, `this._telemetrySettings.get()`, `this._telemetrySettings.on()`
- 参照: `this.#telemetrySettingsSync`, `this._initialized`, `this._originalProviderInfo`, `this._telemetrySettings`
- XPCOM: `Services.wm`

## this.#telemetrySettingsSync()
- 位置: L408-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onSettingsSync()`

## TelemetryHandler.#onSettingsSync()
- 位置: async L426-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (current)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (current)` → `this._setSearchProviderInfo()`
- 条件付き依存: `if (current)` → `Services.ppmm.sharedData.set()`
- 条件付き依存: `if (current)` → `Services.ppmm.sharedData.flush()`
- 条件付き依存: `if (!(current))` → `lazy.logConsole.debug()`
- 参照: `SEARCH_TELEMETRY_SHARED.PROVIDER_INFO`, `event.data?.current`, `this._originalProviderInfo`
- XPCOM: `Services.obs` / `Services.ppmm`

## TelemetryHandler.uninit()
- 位置: L450-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `Services.wm.removeListener()`, `lazy.logConsole.error()`, `this._contentHandler.uninit()`, `this._telemetrySettings.off()`, `this._unregisterWindow()`
- 参照: `this.#telemetrySettingsSync`, `this._initialized`, `this._telemetrySettings`
- XPCOM: `Services.wm`

## TelemetryHandler.recordBrowserSource()
- 位置: L485-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._browserSourceMap.set()`

## TelemetryHandler.recordBrowserNewtabSession()
- 位置: L498-500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._browserNewtabSessionMap.set()`

## TelemetryHandler.recordAbandonmentTelemetry()
- 位置: L511-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.serp.abandonment.record()`, `impressionIdsWithoutEngagementsSet.delete()`, `lazy.logConsole.debug()`

## TelemetryHandler.handleEvent()
- 位置: L530-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._browserNewtabSessionMap.delete()`, `this.stopTrackingBrowser()`
- 条件付き依存: `if (event.type != "TabClose")` → `console.error()`
- 参照: `SearchSERPTelemetryUtils.ABANDONMENTS.TAB_CLOSE`, `event.target.linkedBrowser`, `event.type`

## TelemetryHandler.overrideSearchTelemetryForTests()
- 位置: L551-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentHandler.overrideSearchTelemetryForTests()`, `this._setSearchProviderInfo()`
- 参照: `this._originalProviderInfo`

## TelemetryHandler._setSearchProviderInfo()
- 位置: L565-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `provider.ignoreLinkRegexps.map()`, `provider.nonAdsLinkRegexps.map()`, `provider.subframes ?.filter()`, `provider.subframes ?.filter(obj => obj.inspectRegexpInParent) .map()`, `providerInfo.map()`
- 条件付き依存: `if (provider.extraAdServersRegexps)` → `provider.extraAdServersRegexps.map()`
- 条件付き依存: `if (provider.impressionAttributes?.length)` → `provider.impressionAttributes.map()`
- 条件付き依存: `if (attribute.url?.regexp)` → `structuredClone()`
- 参照: `attribute.url.regexp`, `attribute.url?.regexp`, `newAttribute.url.regexp`, `newProvider.extraAdServersRegexps`, `newProvider.ignoreLinkRegexps`, `newProvider.impressionAttributes`, `newProvider.nonAdsLinkQueryParamNames`, `newProvider.nonAdsLinkRegexps`, `newProvider.shoppingTab`, `newProvider.subframes`, `obj.inspectRegexpInParent`, `obj.regexp`, `provider.extraAdServersRegexps`, `provider.ignoreLinkRegexps?.length`, `provider.impressionAttributes?.length`, `provider.nonAdsLinkQueryParamNames`, `provider.nonAdsLinkRegexps?.length`, `provider.searchPageRegexp`, `provider.shoppingTab.regexp`, `provider.shoppingTab.selector`, `provider.shoppingTab?.regexp`, `this._contentHandler._searchProviderInfo`, `this._searchProviderInfo`

## TelemetryHandler.reportPageAction()
- 位置: L620-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentHandler._reportPageAction()`

## TelemetryHandler.reportPageWithAds()
- 位置: L624-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentHandler._reportPageWithAds()`

## TelemetryHandler.reportPageWithAdImpressions()
- 位置: L628-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentHandler._reportPageWithAdImpressions()`

## TelemetryHandler.reportPageDomains()
- 位置: async L632-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentHandler._reportPageDomains()`

## TelemetryHandler.reportPageImpression()
- 位置: L636-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._contentHandler._reportPageImpression()`

## TelemetryHandler.updateTrackingStatus()
- 位置: L652-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `lazy.BrowserSearchTelemetry.shouldRecordSearchCount()`, `this.#browserToItemMap.set()`, `this._browserInfoByURL.get()`, `this._browserNewtabSessionMap.has()`, `this._checkURLForSerpMatch()`, `this._extractPostParams()`, `this._generateImpressionInfo()`, `this._reportSerpPage()`
- 条件付き依存: `if (postParams)` → `URL.fromURI()`
- 条件付き依存: `if (postParams)` → `postParams.entries()`
- 条件付き依存: `if (postParams)` → `augmentedUrl.searchParams.has()`
- 条件付き依存: `if (!augmentedUrl.searchParams.has(key))` → `augmentedUrl.searchParams.set()`
- 条件付き依存: `if (!info)` → `this._browserNewtabSessionMap.delete()`
- 条件付き依存: `if (!info)` → `this.stopTrackingBrowser()`
- 条件付き依存: `if (!(loadType & Ci.nsIDocShell.LOAD_CMD_HISTORY))` → `this._browserSourceMap.has()`
- 条件付き依存: `if (this._browserSourceMap.has(browser))` → `this._browserSourceMap.get()`
- 条件付き依存: `if (this._browserSourceMap.has(browser))` → `this._browserSourceMap.delete()`
- 条件付き依存: `if (this._browserNewtabSessionMap.has(browser))` → `this._browserNewtabSessionMap.get()`
- 条件付き依存: `if (item)` → `item.browserTelemetryStateMap.set()`
- 条件付き依存: `if (!(item))` → `new WeakMap().set()`
- 条件付き依存: `if (!(item))` → `parseInt()`
- 条件付き依存: `if (!(item))` → `this._browserInfoByURL.set()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `Ci.nsIDocShell.LOAD_CMD_RELOAD`, `PRESCAN.NOT_RUN`, `Services.appinfo.version`, `augmentedUrl.href`, `browser.originalURI.spec`, `browser.originalURI?.spec`, `info.isSPA`, `info.pageType`, `info.searchQuery`, `item.count`, `item.newtabSessionId`, `item.source`, `lazy.Region.home`, `lazy.SearchUtils.MODIFIED_APP_CHANNEL`, `uri.spec`, `webProgress?.loadType`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md) / `Services.appinfo`

## TelemetryHandler.updateTrackingSinglePageApp()
- 位置: async L788-896
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item?.browserTelemetryStateMap.get()`, `this._checkURLForSerpMatch()`, `this._getPageTypeFromUrl()`, `this._getProviderInfoForURL()`, `this._isTrackablePageType()`, `this.findItemForBrowser()`, `this.urlSearchTerms()`
- 条件付き依存: `if (searchTermChanged)` → `browser.browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (searchTermChanged)` → `actor.sendQuery()`
- 条件付き依存: `if (shouldRecordEngagement)` → `impressionIdsWithoutEngagementsSet.delete()`
- 条件付き依存: `if (shouldRecordEngagement)` → `providerInfo.pageTypeParam.pageTypes.find()`
- 条件付き依存: `if (shouldRecordEngagement)` → `Glean.serp.engagement.record()`
- 条件付き依存: `if (shouldRecordEngagement)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (shouldUntrack)` → `browser.browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (shouldUntrack)` → `actor.sendAsyncMessage()`
- 条件付き依存: `if (shouldUntrack)` → `this.stopTrackingBrowser()`
- 条件付き依存: `if ( this._isTrackablePageType(pageType, providerInfo) && !browserIsTracked && (!providerInfo.requireTopLevelImpressionOrigin || !!this._checkURLForSerpMatch(bro...)` → `this.updateTrackingStatus()`
- 条件付き依存: `if ( this._isTrackablePageType(pageType, providerInfo) && !browserIsTracked && (!providerInfo.requireTopLevelImpressionOrigin || !!this._checkURLForSerpMatch(bro...)` → `Services.io.newURI()`
- 条件付き依存: `if ( this._isTrackablePageType(pageType, providerInfo) && !browserIsTracked && (!providerInfo.requireTopLevelImpressionOrigin || !!this._checkURLForSerpMatch(bro...)` → `browser.browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if ( this._isTrackablePageType(pageType, providerInfo) && !browserIsTracked && (!providerInfo.requireTopLevelImpressionOrigin || !!this._checkURLForSerpMatch(bro...)` → `actor.sendAsyncMessage()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `SearchSERPTelemetryUtils.ABANDONMENTS.NAVIGATION`, `SearchSERPTelemetryUtils.ACTIONS.CLICKED`, `SearchSERPTelemetryUtils.COMPONENTS.NON_ADS_LINK`, `browser.originalURI?.spec`, `p.name`, `providerInfo.pageTypeParam.pageTypes.find(p => p.name == pageType) ?.target`, `providerInfo.requireTopLevelImpressionOrigin`, `providerInfo?.pageTypeParam?.enableSPAHandling`, `telemetryState.impressionId`, `telemetryState.searchBoxSubmitted`, `telemetryState?.currentPageType`, `telemetryState?.searchQuery`, `webProgress.loadType`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## TelemetryHandler._getPageTypeFromUrl()
- 位置: L909-936
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pageTypeParam.pageTypes.find()`, `parsedUrl.searchParams.get()`
- 条件付き依存: `if (paramValue)` → `pageType.values.includes()`
- 参照: `defaultConfig.name`, `pageType.isDefault`, `pageType.name`, `pageTypeParam.keys`, `pageTypeParam.pageTypes`, `providerInfo?.pageTypeParam`

## TelemetryHandler._isTrackablePageType()
- 位置: L948-957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `providerInfo.pageTypeParam.pageTypes.find()`
- 参照: `config?.enabled`, `pageTypeConfig.name`, `providerInfo?.pageTypeParam`

## TelemetryHandler.stopTrackingBrowser()
- 位置: L970-1003
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.browserTelemetryStateMap.has()`, `this.#browserToItemMap.delete()`
- 条件付き依存: `if (item.browserTelemetryStateMap.has(browser))` → `item.browserTelemetryStateMap.get()`
- 条件付き依存: `if ( telemetryState.impressionInfo && !telemetryState.impressionRecorded )` → `this._contentHandler._recordFallbackPageImpression()`
- 条件付き依存: `if (item.browserTelemetryStateMap.has(browser))` → `impressionIdsWithoutEngagementsSet.has()`
- 条件付き依存: `if (impressionIdsWithoutEngagementsSet.has(impressionId))` → `this.recordAbandonmentTelemetry()`
- 条件付き依存: `if ( lazy.SERPCategorization.enabled && telemetryState.categorizationInfo )` → `lazy.SERPCategorizationEventScheduler.sendCallback()`
- 条件付き依存: `if (item.browserTelemetryStateMap.has(browser))` → `item.browserTelemetryStateMap.delete()`
- 条件付き依存: `if (!item.count)` → `this._browserInfoByURL.delete()`
- 参照: `item.count`, `lazy.SERPCategorization.enabled`, `telemetryState.categorizationInfo`, `telemetryState.impressionId`, `telemetryState.impressionInfo`, `telemetryState.impressionRecorded`, `this._browserInfoByURL`

## TelemetryHandler.compareUrls()
- 位置: L1034-1068
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (url1.pathname == url2.pathname)` → `url2.searchParams.has()`
- 条件付き依存: `if (url2.searchParams.has(key1))` → `url2.searchParams.get()`
- 参照: `matchOptions.paramValues`, `matchOptions.path`, `url1.hash`, `url1.href`, `url1.origin`, `url1.pathname`, `url1.searchParams`, `url2.hash`, `url2.href`, `url2.origin`, `url2.pathname`

## TelemetryHandler.urlSearchTerms()
- 位置: L1080-1091
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (providerInfo?.queryParamNames?.length)` → `searchParams.get()`
- 参照: `providerInfo.queryParamNames`, `providerInfo?.queryParamNames?.length`

## TelemetryHandler.findItemForBrowser()
- 位置: L1099-1101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserToItemMap.get()`

## TelemetryHandler.onOpenWindow()
- 位置: L1111-1130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._registerWindow()`, `win.addEventListener()`, `win.document.documentElement.getAttribute()`
- 参照: `appWin.docShell.domWindow`

## TelemetryHandler.onCloseWindow()
- 位置: L1138-1152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._unregisterWindow()`, `win.document.documentElement.getAttribute()`
- 参照: `appWin.docShell.domWindow`

## TelemetryHandler._registerWindow()
- 位置: L1159-1161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.tabContainer.addEventListener()`

## TelemetryHandler._unregisterWindow()
- 位置: L1169-1178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stopTrackingBrowser()`, `win.gBrowser.tabContainer.removeEventListener()`
- 参照: `SearchSERPTelemetryUtils.ABANDONMENTS.WINDOW_CLOSE`, `tab.linkedBrowser`, `win.gBrowser.tabs`

## TelemetryHandler._getProviderInfoForURL()
- 位置: L1188-1194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info.searchPageRegexp.test()`, `this._searchProviderInfo?.find()`

## TelemetryHandler._extractPostParams()
- 位置: L1207-1224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `history.getEntryAtIndex()`, `lazy.logConsole.debug()`, `this._getProviderInfoForURL()`
- 参照: `history.getEntryAtIndex(history.index)?.postData?.data?.data`, `history.index`, `uri.spec`, `webProgress.browsingContext.sessionHistory`

## TelemetryHandler._checkURLForSerpMatch()
- 位置: L1235-1364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `k.toLowerCase()`, `queries.forEach()`, `queries.get()`, `queries.set()`, `this._getProviderInfoForURL()`
- 条件付き依存: `if (isSPA)` → `this._getPageTypeFromUrl()`
- 条件付き依存: `if (isSPA)` → `this._isTrackablePageType()`
- 条件付き依存: `if (searchProviderInfo.codeParamName)` → `queries.get()`
- 条件付き依存: `if (searchProviderInfo.codeParamName)` → `searchProviderInfo.codeParamName.toLowerCase()`
- 条件付き依存: `if (code)` → `searchProviderInfo.taggedCodes.includes()`
- 条件付き依存: `if (searchProviderInfo.taggedCodes.includes(code))` → `searchProviderInfo.followOnParamNames.some()`
- 条件付き依存: `if (searchProviderInfo.taggedCodes.includes(code))` → `queries.has()`
- 条件付き依存: `if (!(searchProviderInfo.taggedCodes.includes(code)))` → `searchProviderInfo.organicCodes.includes()`
- 条件付き依存: `if (!(searchProviderInfo.organicCodes.includes(code)))` → `searchProviderInfo.expectedOrganicCodes?.includes()`
- 条件付き依存: `if (followOnCookie.extraCodeParamName)` → `queries.get()`
- 条件付き依存: `if (followOnCookie.extraCodeParamName)` → `followOnCookie.extraCodeParamName.toLowerCase()`
- 条件付き依存: `if (followOnCookie.extraCodeParamName)` → `followOnCookie.extraCodePrefixes.some()`
- 条件付き依存: `if (followOnCookie.extraCodeParamName)` → `eCode.startsWith()`
- 条件付き依存: `if (searchProviderInfo.followOnCookies)` → `Services.cookies.getCookiesFromHost()`
- 条件付き依存: `if (searchProviderInfo.followOnCookies)` → `cookie.value ?.split("&") .map(p => p.split("=")) .filter()`
- 条件付き依存: `if (searchProviderInfo.followOnCookies)` → `cookie.value ?.split("&") .map()`
- 条件付き依存: `if (searchProviderInfo.followOnCookies)` → `cookie.value ?.split()`
- 条件付き依存: `if (searchProviderInfo.followOnCookies)` → `p.split()`
- 条件付き依存: `if (cookieItems.length == 1)` → `searchProviderInfo.taggedCodes.includes()`
- 条件付き依存: `if (searchProviderInfo.searchMode)` → `Object.entries()`
- 条件付き依存: `if (searchProviderInfo.searchMode)` → `queries.has()`
- 参照: `cookie.name`, `cookieItems.length`, `followOnCookie.codeParamName`, `followOnCookie.extraCodeParamName`, `followOnCookie.host`, `followOnCookie.name`, `new URL(url).searchParams`, `searchProviderInfo.alwaysMatchSERP?.parent`, `searchProviderInfo.codeParamName`, `searchProviderInfo.followOnCookies`, `searchProviderInfo.followOnParamNames`, `searchProviderInfo.pageTypeParam?.enableSPAHandling`, `searchProviderInfo.queryParamNames`, `searchProviderInfo.searchMode`, `searchProviderInfo.telemetryId`
- XPCOM: `Services.cookies`

## TelemetryHandler._reportSerpPage()
- 位置: L1376-1388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `p.toUpperCase()`, `source.replace()`
- 条件付き依存: `if (name in Glean.browserSearchContent)` → `Glean.browserSearchContent[name][payload].add()`
- 条件付き依存: `if (!(name in Glean.browserSearchContent))` → `Glean.browserSearchContent.unknown[payload].add()`
- 参照: `Glean.browserSearchContent`, `Glean.browserSearchContent.unknown`, `info.code`, `info.provider`, `info.type`

## TelemetryHandler._generateImpressionInfo()
- 位置: L1422-1493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uuid.generateUUID()`, `Services.uuid.generateUUID().toString()`, `Services.uuid.generateUUID().toString().slice()`, `impressionIdsWithoutEngagementsSet.add()`, `info.type.startsWith()`, `this.#browserContentSourceMap.has()`, `this._getProviderInfoForURL()`
- 条件付き依存: `if (this.#browserContentSourceMap.has(browser))` → `this.#browserContentSourceMap.get()`
- 条件付き依存: `if (this.#browserContentSourceMap.has(browser))` → `this.#browserContentSourceMap.delete()`
- 条件付き依存: `if (attribute.url?.regexp)` → `attribute.url.regexp.test()`
- 条件付き依存: `if (!isPrivate && searchProviderInfo.signedInCookies)` → `searchProviderInfo.signedInCookies.some()`
- 条件付き依存: `if (!isPrivate && searchProviderInfo.signedInCookies)` → `Services.cookies .getCookiesFromHost( cookieObj.host, browser.contentPrincipal.originAttributes ) .some()`
- 条件付き依存: `if (!isPrivate && searchProviderInfo.signedInCookies)` → `Services.cookies .getCookiesFromHost()`
- 参照: `attribute.key`, `attribute.url?.regexp`, `attribute.value`, `browser.contentPrincipal.originAttributes`, `browser.contentPrincipal.originAttributes.privateBrowsingId`, `c.name`, `cookieObj.host`, `cookieObj.name`, `data.impressionId`, `data.impressionInfo`, `info.code`, `info.provider`, `info.searchMode`, `searchProviderInfo.impressionAttributes`, `searchProviderInfo.impressionAttributes?.length`, `searchProviderInfo.signedInCookies`, `searchProviderInfo?.components?.length`
- XPCOM: `Services.cookies` / `Services.uuid`

## ContentHandler.constructor()
- 位置: L1512-1514
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `options.findItemForBrowser`, `this._findItemForBrowser`

## ContentHandler.init()
- 位置: L1523-1539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.ppmm.sharedData.set()`
- 参照: `SEARCH_TELEMETRY_SHARED.LOAD_TIMEOUT`, `SEARCH_TELEMETRY_SHARED.PROVIDER_INFO`, `SEARCH_TELEMETRY_SHARED.SPA_LOAD_TIMEOUT`
- XPCOM: `Services.obs` / `Services.ppmm`

## ContentHandler.uninit()
- 位置: L1544-1547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## ContentHandler.overrideSearchTelemetryForTests()
- 位置: L1555-1557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.sharedData.set()`
- XPCOM: `Services.ppmm`

## ContentHandler.observe()
- 位置: L1559-1566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observeActivity()`

## ContentHandler.observeActivity()
- 位置: L1575-1725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChannelWrapper.get()`, `Services.tm.dispatchToMainThread()`, `console.error()`, `info?.extraAdServersRegexps?.some()`, `item.browserTelemetryStateMap.get()`, `item.source.replace()`, `lazy.logConsole.debug()`, `p.toUpperCase()`, `regex.test()`, `this._searchProviderInfo?.find()`
- 条件付き依存: `if (wrappedChannel._adClickRecorded)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (wrappedChannel.statusCode == 204)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (channelBrowser)` → `this._findItemForBrowser()`
- 条件付き依存: `if (!(item))` → `channelBrowser .getTabBrowser() ?.getTabForBrowser()`
- 条件付き依存: `if (!(item))` → `channelBrowser .getTabBrowser()`
- 条件付き依存: `if (!(item))` → `this._findItemForBrowser()`
- 条件付き依存: `if (!(item))` → `lazy.BrowserWindowTracker.orderedWindows.at()`
- 条件付き依存: `if (selectedBrowser)` → `this._findItemForBrowser()`
- 条件付き依存: `if (serpBrowser != channelBrowser)` → `info?.searchPageRegexp?.test()`
- 条件付き依存: `if (serpBrowser != channelBrowser)` → `info?.subframes?.some()`
- 条件付き依存: `if (serpBrowser != channelBrowser)` → `sf.regexp.test()`
- 条件付き依存: `if (!isFromSERP && !isFromSponsoredSubframe)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (telemetryState)` → `this.#maybeRecordSERPTelemetry()`
- 条件付き依存: `if (telemetryState)` → `lazy.logConsole.error()`
- 条件付き依存: `if (name in Glean.browserSearchAdclicks)` → `Glean.browserSearchAdclicks[name][ `${info.telemetryId}:${item.info.type}` ].add()`
- 条件付き依存: `if (!(name in Glean.browserSearchAdclicks))` → `Glean.browserSearchAdclicks.unknown[ `${info.telemetryId}:${item.info.type}` ].add()`
- 条件付き依存: `if (item.newtabSessionId)` → `Glean.newtabSearchAd.click.record()`
- 条件付き依存: `if (item.newtabSessionId)` → `item.info.type.endsWith()`
- 条件付き依存: `if (item.newtabSessionId)` → `item.info.type.startsWith()`
- 参照: `Ci.nsIChannel`, `Glean.browserSearchAdclicks`, `Glean.browserSearchAdclicks.unknown`, `channelBrowser .getTabBrowser() ?.getTabForBrowser(channelBrowser)?.openerTab`, `info.telemetryId`, `item.info.provider`, `item.info.type`, `item.newtabSessionId`, `item.source`, `provider.telemetryId`, `tab.linkedBrowser`, `tab?.linkedBrowser`, `win?.gBrowser.selectedBrowser`, `wrappedChannel._adClickRecorded`, `wrappedChannel.browserElement`, `wrappedChannel.finalURL`, `wrappedChannel.originURI`, `wrappedChannel.originURI.spec`, `wrappedChannel.statusCode`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / `Services.tm`

## ContentHandler.#maybeRecordSERPTelemetry()
- 位置: L1740-1921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info.extraAdServersRegexps.some()`, `info.ignoreLinkRegexps.some()`, `info.nonAdsLinkRegexps.some()`, `r.test()`
- 条件付き依存: `if (wrappedChannel._recordedClick)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (info.ignoreLinkRegexps.some(r => r.test(url)))` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( info.nonAdsLinkRegexps.some(r => r.test(originURL)) || info.extraAdServersRegexps.some(r => r.test(originURL)) )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( browser?.browsingContext.webProgress?.loadType & Ci.nsIDocShell.LOAD_CMD_HISTORY )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( wrappedChannel.channel.isDocument && (wrappedChannel.channel.loadInfo.isTopLevelLoad || info.nonAdsLinkRegexps.some(r => r.test(url))) )` → `ChromeUtils.now()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `info.searchPageRegexp?.test()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `ChromeUtils.now()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `info.nonAdsLinkRegexps.some()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `r.test()`
- 条件付き依存: `if ( info.nonAdsLinkQueryParamNames.length && info.nonAdsLinkRegexps.some(r => r.test(url)) )` → `parsedUrl.searchParams.get()`
- 条件付き依存: `if (paramValue)` → `/^https?:\/\//.test()`
- 条件付き依存: `if (paramValue)` → `URL.parse()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `telemetryState.urlToComponentMap?.entries()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `SearchSERPTelemetry.compareUrls()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!type)` → `info.extraAdServersRegexps?.some()`
- 条件付き依存: `if (!type)` → `regex.test()`
- 条件付き依存: `if ( type == SearchSERPTelemetryUtils.COMPONENTS.REFINED_SEARCH_BUTTONS )` → `SearchSERPTelemetry.setBrowserContentSource()`
- 条件付き依存: `if (isSerp && isFromNewtab)` → `SearchSERPTelemetry.setBrowserContentSource()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `impressionIdsWithoutEngagementsSet.delete()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `AD_COMPONENTS.includes()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `Glean.serp.engagement.record()`
- 条件付き依存: `if (telemetryState && !telemetryState.searchBoxSubmitted)` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( wrappedChannel.channel.isDocument && (wrappedChannel.channel.loadInfo.isTopLevelLoad || info.nonAdsLinkRegexps.some(r => r.test(url))) )` → `ChromeUtils.addProfilerMarker()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `SearchSERPTelemetryUtils.ACTIONS.CLICKED`, `SearchSERPTelemetryUtils.COMPONENTS.AD_UNCATEGORIZED`, `SearchSERPTelemetryUtils.COMPONENTS.NON_ADS_LINK`, `SearchSERPTelemetryUtils.COMPONENTS.REFINED_SEARCH_BUTTONS`, `SearchSERPTelemetryUtils.INCONTENT_SOURCES.OPENED_IN_NEW_TAB`, `SearchSERPTelemetryUtils.INCONTENT_SOURCES.REFINE_ON_SERP`, `browser?.browsingContext.webProgress?.loadType`, `info.nonAdsLinkQueryParamNames`, `info.nonAdsLinkQueryParamNames.length`, `parsedUrl.origin`, `telemetryState.adsClicked`, `telemetryState.impressionId`, `telemetryState.searchBoxSubmitted`, `wrappedChannel._recordedClick`, `wrappedChannel.browserElement`, `wrappedChannel.channel.isDocument`, `wrappedChannel.channel.loadInfo.isTopLevelLoad`, `wrappedChannel.finalURL`, `wrappedChannel.originURI?.spec`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md)

## ContentHandler._reportPageWithAds()
- 位置: L1937-1998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `item.browserTelemetryStateMap.get()`, `item.source.replace()`, `lazy.logConsole.debug()`, `p.toUpperCase()`, `this._findItemForBrowser()`
- 条件付き依存: `if (!item)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (telemetryState.adsReported)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (name in Glean.browserSearchWithads)` → `Glean.browserSearchWithads[name][ `${item.info.provider}:${item.info.type}` ].add()`
- 条件付き依存: `if (!(name in Glean.browserSearchWithads))` → `Glean.browserSearchWithads.unknown[ `${item.info.provider}:${item.info.type}` ].add()`
- 条件付き依存: `if (item.newtabSessionId)` → `Glean.newtabSearchAd.impression.record()`
- 条件付き依存: `if (item.newtabSessionId)` → `item.info.type.endsWith()`
- 条件付き依存: `if (item.newtabSessionId)` → `item.info.type.startsWith()`
- 参照: `Glean.browserSearchWithads`, `Glean.browserSearchWithads.unknown`, `PRESCAN.FOUND`, `PRESCAN.NONE_FOUND`, `PRESCAN.NOT_RUN`, `info.hasAds`, `info.url`, `item.info.provider`, `item.info.type`, `item.newtabSessionId`, `item.source`, `telemetryState.adsReported`, `telemetryState.prescan`
- XPCOM: `Services.obs`

## ContentHandler._reportPageWithAdImpressions()
- 位置: L2019-2057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.browserTelemetryStateMap.get()`, `this._findItemForBrowser()`
- 条件付き依存: `if ( info.adImpressions && telemetryState && !telemetryState.adImpressionsReported )` → `info.adImpressions.entries()`
- 条件付き依存: `if ( info.adImpressions && telemetryState && !telemetryState.adImpressionsReported )` → `AD_COMPONENTS.includes()`
- 条件付き依存: `if ( info.adImpressions && telemetryState && !telemetryState.adImpressionsReported )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( info.adImpressions && telemetryState && !telemetryState.adImpressionsReported )` → `Glean.serp.adImpression.record()`
- 条件付き依存: `if ( info.adImpressions && telemetryState && !telemetryState.adImpressionsReported )` → `urlToComponentMap.set()`
- 条件付き依存: `if ( info.adImpressions && telemetryState && !telemetryState.adImpressionsReported )` → `Services.obs.notifyObservers()`
- 参照: `data.adsHidden`, `data.adsLoaded`, `data.adsVisible`, `info.adImpressions`, `info.hrefToComponentMap`, `telemetryState.adImpressionsReported`, `telemetryState.adsHidden`, `telemetryState.adsLoaded`, `telemetryState.adsVisible`, `telemetryState.impressionId`, `telemetryState.urlToComponentMap`
- XPCOM: `Services.obs`

## ContentHandler._recordUncategorizedAdImpression()
- 位置: L2066-2073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.serp.adImpression.record()`, `lazy.logConsole.debug()`
- 参照: `SearchSERPTelemetryUtils.COMPONENTS.AD_UNCATEGORIZED`, `telemetryState.adImpressionsReported`, `telemetryState.impressionId`

## ContentHandler._reportPageAction()
- 位置: L2089-2129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.browserTelemetryStateMap.get()`, `this._findItemForBrowser()`
- 条件付き依存: `if (info.target && impressionId)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (info.target && impressionId)` → `Glean.serp.engagement.record()`
- 条件付き依存: `if (info.target && impressionId)` → `impressionIdsWithoutEngagementsSet.delete()`
- 条件付き依存: `if ( info.target == SearchSERPTelemetryUtils.COMPONENTS.INCONTENT_SEARCHBOX && info.action == SearchSERPTelemetryUtils.ACTIONS.SUBMITTED )` → `SearchSERPTelemetry.setBrowserContentSource()`
- 条件付き依存: `if (info.target && impressionId)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(info.target && impressionId))` → `lazy.logConsole.warn()`
- 参照: `SearchSERPTelemetryUtils.ACTIONS.SUBMITTED`, `SearchSERPTelemetryUtils.COMPONENTS.INCONTENT_SEARCHBOX`, `SearchSERPTelemetryUtils.INCONTENT_SOURCES.SEARCHBOX`, `info.action`, `info.target`, `telemetryState.impressionId`, `telemetryState.searchBoxSubmitted`, `telemetryState?.impressionId`
- XPCOM: `Services.obs`

## ContentHandler._reportPageImpression()
- 位置: L2131-2188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item?.browserTelemetryStateMap.get()`, `this._findItemForBrowser()`
- 条件付き依存: `if (!telemetryState?.impressionInfo)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (impressionId && !telemetryState.impressionRecorded)` → `Glean.serp.impression.record()`
- 条件付き依存: `if (impressionId && !telemetryState.impressionRecorded)` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( info.scan == SCAN.ERROR && telemetryState.prescan == PRESCAN.FOUND && !telemetryState.adImpressionsReported )` → `this._recordUncategorizedAdImpression()`
- 条件付き依存: `if (impressionId && !telemetryState.impressionRecorded)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (telemetryState.impressionRecorded)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!(telemetryState.impressionRecorded))` → `lazy.logConsole.debug()`
- 参照: `PRESCAN.FOUND`, `SCAN.ERROR`, `impressionInfo.isPrivate`, `impressionInfo.isSignedIn`, `impressionInfo.partnerCode`, `impressionInfo.provider`, `impressionInfo.searchMode`, `impressionInfo.source`, `impressionInfo.tagged`, `impressionInfo.urlBasedAttributes?.is_shopping_page`, `info.elementBasedAttributes`, `info.elementBasedAttributes?.has_ai_summary`, `info.elementBasedAttributes?.shopping_tab_displayed`, `info.scan`, `telemetryState.adImpressionsReported`, `telemetryState.impressionId`, `telemetryState.impressionInfo`, `telemetryState.impressionRecorded`, `telemetryState.prescan`, `telemetryState?.impressionInfo`
- XPCOM: `Services.obs`

## ContentHandler._recordFallbackPageImpression()
- 位置: L2190-2230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.serp.impression.record()`, `Services.obs.notifyObservers()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (telemetryState.prescan == PRESCAN.FOUND)` → `this._recordUncategorizedAdImpression()`
- 参照: `PRESCAN.FOUND`, `SCAN.NOT_RUN`, `impressionInfo.isPrivate`, `impressionInfo.isSignedIn`, `impressionInfo.partnerCode`, `impressionInfo.provider`, `impressionInfo.searchMode`, `impressionInfo.source`, `impressionInfo.tagged`, `impressionInfo.urlBasedAttributes?.is_shopping_page`, `telemetryState.impressionId`, `telemetryState.impressionInfo`, `telemetryState.impressionRecorded`, `telemetryState.prescan`, `telemetryState?.impressionInfo`
- XPCOM: `Services.obs`

## ContentHandler._reportPageDomains()
- 位置: async L2245-2285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `item?.browserTelemetryStateMap.get()`, `this._findItemForBrowser()`
- 条件付き依存: `if (lazy.SERPCategorization.enabled && telemetryState)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.SERPCategorization.enabled && telemetryState)` → `Array.from()`
- 条件付き依存: `if (lazy.SERPCategorization.enabled && telemetryState)` → `lazy.SERPCategorization.maybeCategorizeSERP()`
- 条件付き依存: `if (result)` → `lazy.SERPCategorizationEventScheduler.addCallback()`
- 参照: `info.adDomains`, `info.nonAdDomains`, `lazy.SERPCategorization.enabled`, `telemetryState.categorizationInfo`
- XPCOM: `Services.obs`

## callback()
- 位置: L2257-2277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SERPCategorizationRecorder.recordCategorizationTelemetry()`
- 参照: `impressionInfo.partnerCode`, `impressionInfo.provider`, `impressionInfo.tagged`, `impressionInfo.urlBasedAttributes?.is_shopping_page`, `item.channel`, `item.majorVersion`, `item.region`, `telemetryState.adsClicked`, `telemetryState.adsHidden`, `telemetryState.adsLoaded`, `telemetryState.adsVisible`, `telemetryState.categorizationInfo`, `telemetryState.impressionInfo`
