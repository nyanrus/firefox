# browser/components/search/SearchSERPTelemetry.sys.mjs

source: browser/components/search/SearchSERPTelemetry.sys.mjs
source-hash: 6e716a3a494fdd724f7197530f2b91a8ed812722
lines: 2289

## <module>
- 役割: 検索結果ページ(SERP)の表示、広告、クリックを Glean と従来のテレメトリに記録する仕組みを定義する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## logConsole()
- 位置: L20-25
- 役割: SearchTelemetry 用のログを作る。search の logging が有効なら Debug、無ければ Warn まで出す。
- 触るとき: SERP テレメトリのログが出ないとき、またはログの詳細度を変えるとき。
- 呼び出し先: `console.createInstance()`
- 参照: `lazy.SearchUtils.loggingEnabled`

## TelemetryHandler.setBrowserContentSource()
- 位置: L376-378
- 役割: コンテンツ側から来た SERP の読み込み元(検索ボックス、新規タブなど)を browser ごとに保存する。
- 触るとき: 検索結果ページの開き方を新しい経路で記録させたいとき。
- 呼び出し先: `this.#browserContentSourceMap.set()`

## TelemetryHandler.constructor()
- 位置: L384-388
- 役割: ContentHandler を作り、browser から追跡情報を引く関数を渡す。
- 触るとき: TelemetryHandler と ContentHandler の結び付けを変えるとき。
- 呼び出し先: `this.findItemForBrowser.bind()`
- 参照: `this._contentHandler`

## TelemetryHandler.init()
- 位置: async L395-424
- 役割: Remote Settings からプロバイダ情報を読み、同期を登録し、ContentHandler と各ウィンドウの初期化を行う。
- 触るとき: 起動時に SERP のプロバイダ情報が読めない、または登録されたウィンドウの扱いを確かめるとき。
- 呼び出し先: `Services.wm.addListener()`, `Services.wm.getEnumerator()`, `lazy.RemoteSettings()`, `lazy.logConsole.error()`, `this._contentHandler.init()`, `this._registerWindow()`, `this._setSearchProviderInfo()`, `this._telemetrySettings.get()`, `this._telemetrySettings.on()`
- 参照: `this.#telemetrySettingsSync`, `this._initialized`, `this._originalProviderInfo`, `this._telemetrySettings`
- XPCOM: `Services.wm`

## this.#telemetrySettingsSync()
- 位置: L408-408
- 役割: Remote Settings の sync イベントを #onSettingsSync に渡す。
- 触るとき: 同期イベントの受け取り方を変えるとき。
- 呼び出し先: `this.#onSettingsSync()`

## TelemetryHandler.#onSettingsSync()
- 位置: async L426-445
- 役割: current の内容でプロバイダ情報を更新し、共有データを子プロセスへ送って、同期完了の通知を出す。
- 触るとき: プロバイダ情報の更新が子プロセスに届かないときや、同期後の挙動を変えるとき。
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
- 役割: ContentHandler を終了し、全ウィンドウの登録を外し、Remote Settings の登録を解除する。
- 触るとき: SERP テレメトリを無効化するときの後始末を変えるとき。
- 呼び出し先: `Services.wm.getEnumerator()`, `Services.wm.removeListener()`, `lazy.logConsole.error()`, `this._contentHandler.uninit()`, `this._telemetrySettings.off()`, `this._unregisterWindow()`
- 参照: `this.#telemetrySettingsSync`, `this._initialized`, `this._telemetrySettings`
- XPCOM: `Services.wm`

## TelemetryHandler.recordBrowserSource()
- 位置: L485-487
- 役割: 検索を始めた browser の検索元(検索バーなど)を記録する。
- 触るとき: 新しい検索の入口を SERP の読み込みの由来として残したいとき。
- 呼び出し先: `this._browserSourceMap.set()`

## TelemetryHandler.recordBrowserNewtabSession()
- 位置: L498-500
- 役割: 新規タブの session id を browser に紐づけて記録する。
- 触るとき: 新規タブ経由の検索を新規タブのセッションに結び付けたいとき。
- 呼び出し先: `this._browserNewtabSessionMap.set()`

## TelemetryHandler.recordAbandonmentTelemetry()
- 位置: L511-522
- 役割: impression の engagement 未記録集合から外し、Glean の abandonment に理由付きで記録する。
- 触るとき: 離脱の記録の理由や項目を変えるとき。
- 呼び出し先: `Glean.serp.abandonment.record()`, `impressionIdsWithoutEngagementsSet.delete()`, `lazy.logConsole.debug()`

## TelemetryHandler.handleEvent()
- 位置: L530-541
- 役割: TabClose を受けると、そのタブの新規タブ session を消し、離脱(tab_close)として追跡を止める。
- 触るとき: タブを閉じたときの離脱記録が出ない、または誤って記録されるとき。
- 呼び出し先: `this._browserNewtabSessionMap.delete()`, `this.stopTrackingBrowser()`
- 条件付き依存: `if (event.type != "TabClose")` → `console.error()`
- 参照: `SearchSERPTelemetryUtils.ABANDONMENTS.TAB_CLOSE`, `event.target.linkedBrowser`, `event.type`

## TelemetryHandler.overrideSearchTelemetryForTests()
- 位置: L551-555
- 役割: テスト用に、与えたプロバイダ情報か元の情報で ContentHandler と本体の情報を上書きする。
- 触るとき: テストでプロバイダ情報を差し替えたいとき。
- 呼び出し先: `this._contentHandler.overrideSearchTelemetryForTests()`, `this._setSearchProviderInfo()`
- 参照: `this._originalProviderInfo`

## TelemetryHandler._setSearchProviderInfo()
- 位置: L565-618
- 役割: プロバイダ情報の正規表現を RegExp に直し、広告サーバー、除外リンク、ショッピングタブ、subframes、impression 属性を作る。
- 触るとき: プロバイダ情報のスキーマに新しい項目を足したとき、またはそれが RegExp に変換されているかを確かめるとき。
- 呼び出し先: `provider.ignoreLinkRegexps.map()`, `provider.nonAdsLinkRegexps.map()`, `provider.subframes ?.filter()`, `provider.subframes ?.filter(obj => obj.inspectRegexpInParent) .map()`, `providerInfo.map()`
- 条件付き依存: `if (provider.extraAdServersRegexps)` → `provider.extraAdServersRegexps.map()`
- 条件付き依存: `if (provider.impressionAttributes?.length)` → `provider.impressionAttributes.map()`
- 条件付き依存: `if (attribute.url?.regexp)` → `structuredClone()`
- 参照: `attribute.url.regexp`, `attribute.url?.regexp`, `newAttribute.url.regexp`, `newProvider.extraAdServersRegexps`, `newProvider.ignoreLinkRegexps`, `newProvider.impressionAttributes`, `newProvider.nonAdsLinkQueryParamNames`, `newProvider.nonAdsLinkRegexps`, `newProvider.shoppingTab`, `newProvider.subframes`, `obj.inspectRegexpInParent`, `obj.regexp`, `provider.extraAdServersRegexps`, `provider.ignoreLinkRegexps?.length`, `provider.impressionAttributes?.length`, `provider.nonAdsLinkQueryParamNames`, `provider.nonAdsLinkRegexps?.length`, `provider.searchPageRegexp`, `provider.shoppingTab.regexp`, `provider.shoppingTab.selector`, `provider.shoppingTab?.regexp`, `this._contentHandler._searchProviderInfo`, `this._searchProviderInfo`

## TelemetryHandler.reportPageAction()
- 位置: L620-622
- 役割: 子プロセスから届いた操作を ContentHandler の _reportPageAction に渡す。
- 触るとき: ページ内の操作の記録経路を調べるとき。
- 呼び出し先: `this._contentHandler._reportPageAction()`

## TelemetryHandler.reportPageWithAds()
- 位置: L624-626
- 役割: 子プロセスの広告有無の結果を ContentHandler の _reportPageWithAds に渡す。
- 触るとき: 広告ありの判定の報告経路を調べるとき。
- 呼び出し先: `this._contentHandler._reportPageWithAds()`

## TelemetryHandler.reportPageWithAdImpressions()
- 位置: L628-630
- 役割: 子プロセスの広告表示数を ContentHandler の _reportPageWithAdImpressions に渡す。
- 触るとき: 広告の表示数の報告経路を調べるとき。
- 呼び出し先: `this._contentHandler._reportPageWithAdImpressions()`

## TelemetryHandler.reportPageDomains()
- 位置: async L632-634
- 役割: 子プロセスから届いたドメイン群を ContentHandler の _reportPageDomains に渡し、完了を待つ。
- 触るとき: カテゴリ分類に渡るドメインの経路を調べるとき。
- 呼び出し先: `this._contentHandler._reportPageDomains()`

## TelemetryHandler.reportPageImpression()
- 位置: L636-638
- 役割: 子プロセスの表示情報を ContentHandler の _reportPageImpression に渡す。
- 触るとき: impression の記録を遅らせたり、項目を足したりするとき。
- 呼び出し先: `this._contentHandler._reportPageImpression()`

## TelemetryHandler.updateTrackingStatus()
- 位置: L652-768
- 役割: 読み込まれた URL が SERP かを判定し、該当すれば impression の状態を作って browser を追跡する。SERP でなければ追跡を止める。
- 触るとき: どの URL を SERP として数えるかや、追跡の開始条件を変えるとき。
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
- 役割: SPA の SERP で、検索語やページ種別が変わったときにエンゲージメントの記録、追跡の解除、追跡の再開を順に行う。
- 触るとき: SPA の検索結果で別タブや別種別に移ったときの記録がずれるとき。
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
- 役割: URL の page type パラメータから種別を探し、無ければ既定の種別を返す。
- 触るとき: 画像検索などのページ種別の判定を変えるとき。
- 呼び出し先: `pageTypeParam.pageTypes.find()`, `parsedUrl.searchParams.get()`
- 条件付き依存: `if (paramValue)` → `pageType.values.includes()`
- 参照: `defaultConfig.name`, `pageType.isDefault`, `pageType.name`, `pageTypeParam.keys`, `pageTypeParam.pageTypes`, `providerInfo?.pageTypeParam`

## TelemetryHandler._isTrackablePageType()
- 位置: L948-957
- 役割: ページ種別の設定で enabled のものだけを追跡対象と判定する。
- 触るとき: 追跡するページ種別を増やしたり減らしたりするとき。
- 呼び出し先: `providerInfo.pageTypeParam.pageTypes.find()`
- 参照: `config?.enabled`, `pageTypeConfig.name`, `providerInfo?.pageTypeParam`

## TelemetryHandler.stopTrackingBrowser()
- 位置: L970-1003
- 役割: browser の追跡を止める。未記録の impression は fallback で記録し、engagement の無いものは離脱として記録し、分類の予約を送る。
- 触るとき: タブの追跡が止まったときに記録が抜けたり二重になったりするとき。
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
- 役割: 2 つの URL の一致度を、origin、path、クエリ、hash の一致数で点数にする。
- 触るとき: 広告リンクやコンポーネントの URL の照合の厳しさを変えるとき。
- 条件付き依存: `if (url1.pathname == url2.pathname)` → `url2.searchParams.has()`
- 条件付き依存: `if (url2.searchParams.has(key1))` → `url2.searchParams.get()`
- 参照: `matchOptions.paramValues`, `matchOptions.path`, `url1.hash`, `url1.href`, `url1.origin`, `url1.pathname`, `url1.searchParams`, `url2.hash`, `url2.href`, `url2.origin`, `url2.pathname`

## TelemetryHandler.urlSearchTerms()
- 位置: L1080-1091
- 役割: プロバイダの queryParamNames のうち最初に値があるものから検索語を取り出す。
- 触るとき: 検索語の取り出し元のパラメータを増やすとき。
- 条件付き依存: `if (providerInfo?.queryParamNames?.length)` → `searchParams.get()`
- 参照: `providerInfo.queryParamNames`, `providerInfo?.queryParamNames?.length`

## TelemetryHandler.findItemForBrowser()
- 位置: L1099-1101
- 役割: browser に紐づく追跡情報を返す。
- 触るとき: ある browser の SERP 情報を他から取りたいとき。
- 呼び出し先: `this.#browserToItemMap.get()`

## TelemetryHandler.onOpenWindow()
- 位置: L1111-1130
- 役割: 新しく開いたブラウザウィンドウの load 後に、そのウィンドウを登録する。
- 触るとき: 新規ウィンドウで TabClose の監視が効かないとき。
- 呼び出し先: `this._registerWindow()`, `win.addEventListener()`, `win.document.documentElement.getAttribute()`
- 参照: `appWin.docShell.domWindow`

## TelemetryHandler.onCloseWindow()
- 位置: L1138-1152
- 役割: 閉じたブラウザウィンドウの登録を外す。
- 触るとき: ウィンドウを閉じたときの離脱処理を調べるとき。
- 呼び出し先: `this._unregisterWindow()`, `win.document.documentElement.getAttribute()`
- 参照: `appWin.docShell.domWindow`

## TelemetryHandler._registerWindow()
- 位置: L1159-1161
- 役割: ウィンドウのタブ群に TabClose の監視を付ける。
- 触るとき: タブを閉じたときのイベントが届かないとき。
- 呼び出し先: `win.gBrowser.tabContainer.addEventListener()`

## TelemetryHandler._unregisterWindow()
- 位置: L1169-1178
- 役割: ウィンドウ内の全タブを window_close の離脱として追跡から外し、監視を外す。
- 触るとき: ウィンドウを閉じたときの離脱記録を変えるとき。
- 呼び出し先: `this.stopTrackingBrowser()`, `win.gBrowser.tabContainer.removeEventListener()`
- 参照: `SearchSERPTelemetryUtils.ABANDONMENTS.WINDOW_CLOSE`, `tab.linkedBrowser`, `win.gBrowser.tabs`

## TelemetryHandler._getProviderInfoForURL()
- 位置: L1188-1194
- 役割: searchPageRegexp に一致する最初のプロバイダ情報を返す。読み込み直後はまだ無いことがある。
- 触るとき: ある URL がどのプロバイダに属するかを調べるとき。
- 呼び出し先: `info.searchPageRegexp.test()`, `this._searchProviderInfo?.find()`

## TelemetryHandler._extractPostParams()
- 位置: L1207-1224
- 役割: プロバイダの SERP が POST のとき、セッション履歴の本文を URLSearchParams にして返す。失敗時は null。
- 触るとき: POST 検索の検索語やパラメータを読み取る処理を直すとき。
- 呼び出し先: `history.getEntryAtIndex()`, `lazy.logConsole.debug()`, `this._getProviderInfoForURL()`
- 参照: `history.getEntryAtIndex(history.index)?.postData?.data?.data`, `history.index`, `uri.spec`, `webProgress.browsingContext.sessionHistory`

## TelemetryHandler._checkURLForSerpMatch()
- 位置: L1235-1364
- 役割: URL がプロバイダの SERP かを判定し、検索語、タグや partner code、検索モードを含む情報を返す。
- 触るとき: SERP の判定条件やタグ付きの種類(tagged、organic、follow-on など)を変えるとき。
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
- 役割: プロバイダ、種類、code を組み合わせて browser_search_content の該当項目に 1 件加算する。
- 触るとき: SERP の表示のテレメトリの項目名や集計先を変えるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `p.toUpperCase()`, `source.replace()`
- 条件付き依存: `if (name in Glean.browserSearchContent)` → `Glean.browserSearchContent[name][payload].add()`
- 条件付き依存: `if (!(name in Glean.browserSearchContent))` → `Glean.browserSearchContent.unknown[payload].add()`
- 参照: `Glean.browserSearchContent`, `Glean.browserSearchContent.unknown`, `info.code`, `info.provider`, `info.type`

## TelemetryHandler._generateImpressionInfo()
- 位置: L1422-1493
- 役割: SERP ごとに UUID の impression id を振り、プロバイダの属性、private、サインイン状態を集めて返す。
- 触るとき: impression に載せる項目を増やすとき、またはサインイン判定を直すとき。
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
- 役割: browser から追跡情報を引く関数を保存する。
- 触るとき: ContentHandler が追跡情報を引く経路を変えるとき。
- 参照: `options.findItemForBrowser`, `this._findItemForBrowser`

## ContentHandler.init()
- 位置: L1523-1539
- 役割: プロバイダ情報と読み込み待ちの時間(通常 1000 ms、SPA 2500 ms)を子プロセスと共有し、HTTP 応答の監視を登録する。
- 触るとき: 広告のクリック判定を待つ時間を変えるとき、または子プロセスに情報が渡らないとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.ppmm.sharedData.set()`
- 参照: `SEARCH_TELEMETRY_SHARED.LOAD_TIMEOUT`, `SEARCH_TELEMETRY_SHARED.PROVIDER_INFO`, `SEARCH_TELEMETRY_SHARED.SPA_LOAD_TIMEOUT`
- XPCOM: `Services.obs` / `Services.ppmm`

## ContentHandler.uninit()
- 位置: L1544-1547
- 役割: HTTP 応答の監視を外す。
- 触るとき: 終了時に監視が残らないか確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## ContentHandler.overrideSearchTelemetryForTests()
- 位置: L1555-1557
- 役割: テスト用に、子プロセスと共有するプロバイダ情報を上書きする。
- 触るとき: テストで子プロセス側のプロバイダ情報を差し替えたいとき。
- 呼び出し先: `Services.ppmm.sharedData.set()`
- XPCOM: `Services.ppmm`

## ContentHandler.observe()
- 位置: L1559-1566
- 役割: HTTP の応答(通常と cache)を observeActivity に渡す。
- 触るとき: ネットワーク監視の対象の応答種別を増やすとき。
- 呼び出し先: `this.observeActivity()`

## ContentHandler.observeActivity()
- 位置: L1575-1725
- 役割: リクエストの元の SERP browser を探し(タブ、開いたタブ、直前のウィンドウ)、クリックとして記録し、広告クリックなら数える。204 応答は無視する。
- 触るとき: 広告クリックや SERP からのリンククリックを取りこぼす、または二重に数えるとき。
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
- 役割: 文書の読み込みを SERP のエンゲージメントとして記録する。除外リンク、リダイレクト予定、履歴からの読み込みは除く。コンポーネント種別は URL の照合で決め、見つからなければ広告 (uncategorized) か非広告リンクにする。
- 触るとき: SERP のクリックの種別判定や、クリックを記録する条件を変えるとき。
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
- 役割: 広告の有無の結果を状態に入れ、広告ありなら一度だけ with_ads の件数を加算し、新規タブ経由なら広告の impression を記録する。
- 触るとき: 広告ありの SERP の件数の数え方を変えるとき。
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
- 役割: 広告の表示数(読み込み、表示、非表示)を状態に足して Glean の adImpression に記録し、href とコンポーネントの対応を URL の対応表にする。
- 触るとき: 広告の表示数や広告コンポーネントの記録内容を変えるとき。
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
- 役割: 分類できなかった広告を、広告 (uncategorized) の表示として Glean に 1 件記録する。
- 触るとき: 分類できなかった広告の扱いを変えるとき。
- 呼び出し先: `Glean.serp.adImpression.record()`, `lazy.logConsole.debug()`
- 参照: `SearchSERPTelemetryUtils.COMPONENTS.AD_UNCATEGORIZED`, `telemetryState.adImpressionsReported`, `telemetryState.impressionId`

## ContentHandler._reportPageAction()
- 位置: L2089-2129
- 役割: ページ内の操作を engagement として記録し、検索ボックスからの送信なら検索ボックス経由の情報を browser に残す。
- 触るとき: ページ内の操作の記録項目や、検索ボックス経由の扱いを変えるとき。
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
- 役割: impression を Glean に一度だけ記録する。スキャンが失敗し広告が見つかっていれば、分類できない広告も記録する。
- 触るとき: impression の項目を増やしたり、スキャン失敗時の扱いを変えるとき。
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
- 役割: スキャンされなかったページの impression を、未確認の項目つきで記録する。広告ありなら分類できない広告も記録する。
- 触るとき: 途中で離れたページの impression の値を変えるとき。
- 呼び出し先: `Glean.serp.impression.record()`, `Services.obs.notifyObservers()`, `lazy.logConsole.debug()`
- 条件付き依存: `if (telemetryState.prescan == PRESCAN.FOUND)` → `this._recordUncategorizedAdImpression()`
- 参照: `PRESCAN.FOUND`, `SCAN.NOT_RUN`, `impressionInfo.isPrivate`, `impressionInfo.isSignedIn`, `impressionInfo.partnerCode`, `impressionInfo.provider`, `impressionInfo.searchMode`, `impressionInfo.source`, `impressionInfo.tagged`, `impressionInfo.urlBasedAttributes?.is_shopping_page`, `telemetryState.impressionId`, `telemetryState.impressionInfo`, `telemetryState.impressionRecorded`, `telemetryState.prescan`, `telemetryState?.impressionInfo`
- XPCOM: `Services.obs`

## ContentHandler._reportPageDomains()
- 位置: async L2245-2285
- 役割: 分類が有効で追跡中なら広告と非広告のドメインを分類し、結果があれば記録の予約を追跡情報に登録する。
- 触るとき: 分類の対象ドメインや、分類結果をいつ記録するかを変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `item?.browserTelemetryStateMap.get()`, `this._findItemForBrowser()`
- 条件付き依存: `if (lazy.SERPCategorization.enabled && telemetryState)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (lazy.SERPCategorization.enabled && telemetryState)` → `Array.from()`
- 条件付き依存: `if (lazy.SERPCategorization.enabled && telemetryState)` → `lazy.SERPCategorization.maybeCategorizeSERP()`
- 条件付き依存: `if (result)` → `lazy.SERPCategorizationEventScheduler.addCallback()`
- 参照: `info.adDomains`, `info.nonAdDomains`, `lazy.SERPCategorization.enabled`, `telemetryState.categorizationInfo`
- XPCOM: `Services.obs`

## callback()
- 位置: L2257-2277
- 役割: 分類結果に impression の情報と広告の件数を足し、SERP categorization のテレメトリとして記録する。
- 触るとき: categorization のイベントに載せる項目を増やすとき。
- 呼び出し先: `lazy.SERPCategorizationRecorder.recordCategorizationTelemetry()`
- 参照: `impressionInfo.partnerCode`, `impressionInfo.provider`, `impressionInfo.tagged`, `impressionInfo.urlBasedAttributes?.is_shopping_page`, `item.channel`, `item.majorVersion`, `item.region`, `telemetryState.adsClicked`, `telemetryState.adsHidden`, `telemetryState.adsLoaded`, `telemetryState.adsVisible`, `telemetryState.categorizationInfo`, `telemetryState.impressionInfo`
