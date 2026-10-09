# browser/modules/BrowserUsageTelemetry.sys.mjs

source: browser/modules/BrowserUsageTelemetry.sys.mjs
source-hash: 747591972bd724d6b4ac2dbd1a5f7c0819f5e219
lines: 2173

## <module>
- 役割: ブラウザの利用状況(タブ数、窓数、UI 操作、タブグループ、URI 訪問、インストール)を Glean の指標として記録するモジュール。
- 呼び出し先: `BrowserUsageTelemetry.recordPinnedTabsCount()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `getOpenTabsAndWinsCounts()`, `getPinnedTabsCount()`

## telemetryId()
- 位置: L225-271
- 役割: ウィジェット ID を、テレメトリに送れる形(アドオンは隠した名前)に変換する。
- 触るとき: テレメトリに出す操作名の表記を変えるとき。アドオンの ID を出さないための仕組みもここにある。
- 呼び出し先: `widgetId.endsWith()`, `widgetId.replace()`
- 条件付き依存: `if (widgetId.endsWith("-browser-action"))` → `addonId()`
- 条件付き依存: `if (widgetId.endsWith("-browser-action"))` → `widgetId.substring()`
- 条件付き依存: `if (!(widgetId.endsWith("-browser-action")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("pageAction-"))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("pageAction-urlbar-"))` → `widgetId.substring()`
- 条件付き依存: `if (!(widgetId.startsWith("pageAction-urlbar-")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("pageAction-panel-"))` → `widgetId.substring()`
- 条件付き依存: `if (actionId)` → `lazy.PageActions.actionForID()`
- 条件付き依存: `if (actionId)` → `addonId()`
- 条件付き依存: `if (!(widgetId.startsWith("pageAction-")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("ext-keyset-id-"))` → `addonId()`
- 条件付き依存: `if (widgetId.startsWith("ext-keyset-id-"))` → `widgetId.substring()`
- 条件付き依存: `if (!(widgetId.startsWith("ext-keyset-id-")))` → `widgetId.startsWith()`
- 条件付き依存: `if (widgetId.startsWith("ext-key-id-"))` → `widgetId.substring()`
- 条件付き依存: `if (widgetId.startsWith("ext-key-id-"))` → `widgetId.endsWith()`
- 条件付き依存: `if (widgetId.endsWith("-sidebar-action"))` → `addonId()`
- 条件付き依存: `if (widgetId.endsWith("-sidebar-action"))` → `widgetId.substring()`
- 参照: `"-browser-action".length`, `"-sidebar-action".length`, `"ext-key-id-".length`, `"ext-keyset-id-".length`, `"pageAction-panel-".length`, `"pageAction-urlbar-".length`, `action?._isMozillaAction`, `widgetId.length`

## addonId()
- 位置: L227-238
- 役割: アドオン ID を既知の一覧の番号で addonN の形に置き換える。obscureAddons が false ならそのまま返す。
- 触るとき: アドオン ID を隠す規則を変えるとき。新しい ID は一覧の末尾に追加される。
- 呼び出し先: `KNOWN_ADDONS.indexOf()`
- 条件付き依存: `if (pos < 0)` → `KNOWN_ADDONS.push()`
- 参照: `KNOWN_ADDONS.length`

## getOpenTabsAndWinsCounts()
- 位置: L273-302
- 役割: 全窓のタブ数、読み込み済みタブ数、窓数、グループ内外のタブ数を数える。
- 触るとき: タブ数や窓数の指標の定義を変えるとき。読み込み済みは pending 属性が付いていないタブを数える。
- 呼び出し先: `Services.wm.getEnumerator()`, `tab.getAttribute()`
- 参照: `win.gBrowser.tabs`, `win.gBrowser.tabs.length`
- XPCOM: `Services.wm`

## getPinnedTabsCount()
- 位置: L304-312
- 役割: 全窓のピン留めタブの数を数える。
- 触るとき: ピン留めタブの指標の定義を変えるとき。
- 呼び出し先: `Services.wm.getEnumerator()`, `[...win.gBrowser.tabs].filter()`
- 参照: `[...win.gBrowser.tabs].filter(t => t.pinned).length`, `t.pinned`, `win.gBrowser.tabs`
- XPCOM: `Services.wm`

## isHttpURI()
- 位置: L323-326
- 役割: URI が http か https かを返す。
- 触るとき: 訪問数の集計対象を広げたり狭めたりするとき。
- 呼び出し先: `uri.schemeIs()`

## addRestoredURI()
- 位置: L328-334
- 役割: 復元されたタブの URI を記録し、後の読み込みを訪問として数えないようにする。
- 触るとき: セッション復元で再読み込みされたページの数え方を変えるとき。
- 呼び出し先: `this._restoredURIsMap.set()`, `this.isHttpURI()`
- 参照: `uri.spec`

## onLocationChange()
- 位置: L336-471
- 役割: トップレベルの場所変化ごとに、URI とドメインの訪問数、検索結果ページの追跡、タブ数の記録を行う。
- 触るとき: URI 数やユニークドメイン数、プライベートモードでの計数条件を変えるとき。初期ページやエラーページは数えない。
- 呼び出し先: `BrowserUsageTelemetry._recordTabCounts()`, `Glean.browserEngagement.uriCount.add()`, `Glean.browserEngagement.uriCountNormalMode.add()`, `Services.eTLD.getBaseDomain()`, `Services.prefs.getBoolPref()`, `browser.documentGlobal.gInitialPages.includes()`, `getOpenTabsAndWinsCounts()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this._domain24hrSet.get()`, `this._domain24hrSet.set()`, `this._restoredURIsMap.get()`, `this.isHttpURI()`
- 条件付き依存: `if ( !(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT) && webProgress.isTopLevel )` → `lazy.SearchSERPTelemetry.stopTrackingBrowser()`
- 条件付き依存: `if (shouldCountURI)` → `Glean.browserEngagement.unfilteredUriCount.add()`
- 条件付き依存: `if (this._restoredURIsMap.get(browser) === uriSpec)` → `this._restoredURIsMap.delete()`
- 条件付き依存: `if (!(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT))` → `lazy.SearchSERPTelemetry.updateTrackingStatus()`
- 条件付き依存: `if (!(!(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT)))` → `lazy.SearchSERPTelemetry.updateTrackingSinglePageApp()`
- 条件付き依存: `if (this._domainSet.size < MAX_UNIQUE_VISITED_DOMAINS)` → `this._domainSet.add()`
- 条件付き依存: `if (this._domainSet.size < MAX_UNIQUE_VISITED_DOMAINS)` → `Glean.browserEngagement.uniqueDomainsCount.set()`
- 条件付き依存: `if (timeoutId)` → `lazy.clearTimeout()`
- 条件付き依存: `if (lazy.gRecentVisitedOriginsExpiry)` → `lazy.setTimeout()`
- 条件付き依存: `if (lazy.gRecentVisitedOriginsExpiry)` → `this._domain24hrSet.delete()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_ERROR_PAGE`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `browser.documentGlobal`, `lazy.SearchSERPTelemetryUtils.ABANDONMENTS.NAVIGATION`, `lazy.gRecentVisitedOriginsExpiry`, `this._domainSet.size`, `uri.spec`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.eTLD` / `Services.prefs`

## reset()
- 位置: L476-478
- 役割: セッション内のユニークドメインの集合を空にする。
- 触るとき: セッションを区切る時の集計リセットを確かめるとき。
- 呼び出し先: `this._domainSet.clear()`

## uniqueDomainsVisitedInPast24Hours()
- 位置: L484-486
- 役割: 過去 24 時間に訪れたユニークドメインの数を返す。
- 触るとき: 24 時間分の訪問ドメイン数の指標を読むとき。
- 参照: `this._domain24hrSet.size`

## resetUniqueDomainsVisitedInPast24Hours()
- 位置: L491-494
- 役割: 24 時間分のドメインの期限タイマーを解除し、集合を空にする。
- 触るとき: 24 時間分の集計を手動でリセットするとき。
- 呼び出し先: `lazy.clearTimeout()`, `this._domain24hrSet.clear()`, `this._domain24hrSet.forEach()`

## getTelemetryClientId()
- 位置: async L509-509
- 役割: テストで差し替えられる、テレメトリのクライアント ID の取得。
- 触るとき: プロファイル数の集計をテストするとき。
- 呼び出し先: `lazy.ClientID.getClientID()`

## getUpdateDirectory()
- 位置: L510-510
- 役割: テストで差し替えられる、更新ディレクトリの取得。
- 触るとき: プロファイル数ファイルの保存先を変えるとき、テストで差し替えるとき。
- 呼び出し先: `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## readProfileCountFile()
- 位置: async L511-511
- 役割: テストで差し替えられる、プロファイル数ファイルの読み込み。
- 触るとき: プロファイル数ファイルの読み方をテストで変えるとき。
- 呼び出し先: `IOUtils.readUTF8()`

## writeProfileCountFile()
- 位置: async L512-512
- 役割: テストで差し替えられる、プロファイル数ファイルの書き込み。
- 触るとき: プロファイル数ファイルの書き方をテストで変えるとき。
- 呼び出し先: `IOUtils.writeUTF8()`

## init()
- 位置: L531-564
- 役割: 起動時に最大値の初期値を設定し、窓と通知の監視を始め、遅延実行のタスクを用意する。
- 触るとき: 起動時の初期化順序や、受け取る通知を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `this._doOnSavedTabGroupsChange()`, `this._doOnTabGroupChange()`, `this._doOnTabGroupExpandOrCollapse()`, `this._onSavedTabGroupsChangedTask.arm()`, `this._onTabsOpened()`, `this._recordPrefValues()`, `this._recordUITelemetry()`, `this._setupAfterRestore()`, `this.recordPinnedTabsCount()`
- 参照: `lazy.DeferredTask`, `this._inited`, `this._lastRecordLoadedTabCount`, `this._lastRecordTabCount`, `this._onSavedTabGroupsChangedTask`, `this._onTabGroupChangeTask`, `this._onTabGroupExpandOrCollapseTask`, `this._onTabsOpenedTask`
- XPCOM: `Services.obs` / `Services.prefs`

## maxTabCountGleanQuantity()
- 位置: L568-572
- 役割: 縦タブか横タブかに応じて、最大タブ数の指標を返す。
- 触るとき: 最大タブ数の指標を縦タブと横タブで分けるとき。
- 参照: `Glean.browserEngagement.maxConcurrentTabCount`, `Glean.browserEngagement.maxConcurrentVerticalTabCount`, `lazy.sidebarVerticalTabs`

## updateMaxTabPinnedCount()
- 位置: L575-586
- 役割: ピン留めタブ数が最大値を超えた時に、最大値を更新して指標に記録する。
- 触るとき: ピン留めの最大数の記録条件を変えるとき。
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.browserEngagement.maxConcurrentVerticalTabPinnedCount.set()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.browserEngagement.maxConcurrentTabPinnedCount.set()`
- 参照: `lazy.sidebarVerticalTabs`, `this.maxTabPinnedCount`

## recordPinnedTabsCount()
- 位置: L588-594
- 役割: ピン留めタブ数を、縦タブか横タブの指標へ記録する。
- 触るとき: ピン留め数の指標の送り先を変えるとき。
- 呼び出し先: `getPinnedTabsCount()`
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.pinnedTabs.count.sidebar.set()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.pinnedTabs.count.horizontalBar.set()`
- 参照: `lazy.sidebarVerticalTabs`

## _resetAddonIds()
- 位置: L599-601
- 役割: テスト用に、隠したアドオン ID の一覧を空にする。
- 触るとき: テストでアドオン ID の番号付けをリセットしたいとき。
- 参照: `KNOWN_ADDONS.length`

## afterSubsessionSplit()
- 位置: L606-614
- 役割: サブセッションが区切られた後、最大値を再計算し、URI の計数をリセットする。
- 触るとき: サブセッション区切りの時に何を引き継ぐかを変えるとき。
- 呼び出し先: `URICountListener.reset()`, `this._initMaxTabAndWindowCounts()`

## uninit()
- 位置: L621-629
- 役割: 登録した通知の監視を外す。初期化されていなければ何もしない。
- 触るとき: 終了時に監視が残らないかを確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this._inited`
- XPCOM: `Services.obs`

## observe()
- 位置: L631-657
- 役割: 通知の種類ごとに、窓の生成、サブセッション分割、保存済みタブグループの変化、日次の処理、ツールバー表示の変化へ振り分ける。
- 触るとき: 監視する通知を増やしたり、通知の処理先を変えたりするとき。
- 呼び出し先: `this._onSavedTabGroupsChange()`, `this._onWindowOpen()`, `this._recordPrefValues()`, `this._recordWidgetChange()`, `this.afterSubsessionSplit()`
- 参照: `Services.appinfo.drawInTitlebar`
- XPCOM: `Services.appinfo`

## handleEvent()
- 位置: L659-715
- 役割: タブ・タブグループの DOM イベントを、それぞれの処理へ振り分ける。
- 触るとき: タブ関連の指標の集計先を追加するとき。
- 呼び出し先: `URICountListener.addRestoredURI()`, `getOpenTabsAndWinsCounts()`, `this._onTabClosed()`, `this._onTabGroupChange()`, `this._onTabGroupCreateByUser()`, `this._onTabGroupExpandOrCollapse()`, `this._onTabGroupRemoveRequested()`, `this._onTabGroupSave()`, `this._onTabGroupUngroup()`, `this._onTabMove()`, `this._onTabOpen()`, `this._onTabPinned()`, `this._onTabSelect()`, `this._onTabUnpinned()`, `this._recordTabCounts()`, `this._unregisterWindow()`
- 参照: `browser.currentURI`, `event.target`, `event.target.linkedBrowser`, `event.type`

## _initMaxTabAndWindowCounts()
- 位置: L717-723
- 役割: 現在のタブ数と窓数を、最大値の初期値として設定する。
- 触るとき: 起動時やサブセッション分割時の最大値の基準を変えるとき。
- 呼び出し先: `Glean.browserEngagement.maxConcurrentWindowCount.set()`, `getOpenTabsAndWinsCounts()`, `this.maxTabCountGleanQuantity.set()`
- 参照: `counts.tabCount`, `counts.winCount`, `this.maxTabCount`, `this.maxWindowCount`

## _setupAfterRestore()
- 位置: L730-743
- 役割: セッション復元後に、窓の生成とサブセッション分割、保存済みタブグループの通知を登録し、既存の窓を登録して最大値を初期化する。
- 触るとき: 復元完了後に行う登録の内容や順序を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.wm.getEnumerator()`, `this._initMaxTabAndWindowCounts()`, `this._registerWindow()`
- XPCOM: `Services.obs` / `Services.wm`

## _buildWidgetPositions()
- 位置: L745-827
- 役割: ツールバー、メニューバー、タイトルバー、カスタマイズ可能な各領域、ページアクションの配置を一覧にする。
- 触るとき: ツールバーの配置の指標の内容を変えるとき。
- 呼び出し先: `Services.xulStore.getValue()`, `lazy.CustomizableUI.getWidgetsInArea()`, `toolbarState()`, `widget.id.startsWith()`, `widgetMap.set()`
- 条件付き依存: `if (action.pinnedToUrlbar)` → `widgetMap.set()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `BROWSER_UI_CONTAINER_IDS.PersonalToolbar`, `Services.appinfo.drawInTitlebar`, `action.id`, `action.pinnedToUrlbar`, `lazy.CustomizableUI.areas`, `lazy.PageActions.actions`, `widget.id`
- XPCOM: `Services.appinfo` / `Services.xulStore`

## toolbarState()
- 位置: L748-770
- 役割: ブックマークツールバーなどの表示状態を on か off の文字列で返す。
- 触るとき: ツールバーの表示状態の判定を変えるとき。
- 呼び出し先: `Services.xulStore.getValue()`
- 条件付き依存: `if (nodeId == "PersonalToolbar")` → `Services.prefs.getCharPref()`
- 参照: `AppConstants.BROWSER_CHROME_URL`
- XPCOM: `Services.prefs` / `Services.xulStore`

## _getWidgetID()
- 位置: L829-936
- 役割: DOM ノードから、テレメトリで使うウィジェット ID を探す。共有メニュー、カスタマイズ可能なウィジェット、ID や属性の順に調べ、無ければ親をたどる。
- 触るとき: クリックされた要素の名付け方を変えるとき。
- 呼び出し先: `node.classList.contains()`, `node.classList?.contains()`, `node.getRootNode()`, `node.hasAttribute()`, `node.parentElement.id.includes()`, `this._getWidgetID()`
- 条件付き依存: `if (node.classList?.contains("share-copy-link"))` → `node.closest()`
- 条件付き依存: `if (node.ownerDocument.URL == AppConstants.BROWSER_CHROME_URL)` → `node.closest()`
- 条件付き依存: `if (node.ownerDocument.URL == AppConstants.BROWSER_CHROME_URL)` → `CSS.escape()`
- 条件付き依存: `if (node.closest(`#${CSS.escape(area)}`))` → `lazy.CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (node.closest(`#${CSS.escape(area)}`))` → `node.closest()`
- 条件付き依存: `if (node.closest(`#${CSS.escape(area)}`))` → `CSS.escape()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `node.getRootNode()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `host.closest()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `this._getWidgetID()`
- 条件付き依存: `if (node.localName != "key")` → `possibleAttributes.unshift()`
- 条件付き依存: `if (node.hasAttribute(idAttribute))` → `node.getAttribute()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `lazy.CustomizableUI.areas`, `node.getRootNode().host`, `node.id`, `node.localName`, `node.ownerDocument.URL`, `node.parentElement`, `settingControl.setting.id`, `settingControl?.setting?.id`, `shareItem.browsersToShare`

## _getBrowserWidgetContainer()
- 位置: L938-954
- 役割: ブラウザ窓内で、ノードを含むコンテナの名前(メニューバー、タブバーなど)を返す。
- 触るとき: UI 操作の集計先の分類を変えるとき。タブに関するコンテキストメニューも含む。
- 呼び出し先: `Object.keys()`, `container.contains()`, `node.closest()`, `node.getAttribute()`, `node.ownerDocument.getElementById()`
- 参照: `BROWSER_UI_CONTAINER_IDS.tabContextMenu`

## _getWidgetContainer()
- 位置: L956-990
- 役割: ノードの所属先(キーボード、ブラウザ窓のコンテナ、設定画面のペイン)を判定する。
- 触るとき: 操作の分類先を増やしたり、設定画面のペイン名の扱いを変えるとき。
- 呼び出し先: `node.getRootNode()`, `url.startsWith()`
- 条件付き依存: `if (node.localName == "a" && node.getRootNode().host)` → `node.getRootNode()`
- 条件付き依存: `if (url == AppConstants.BROWSER_CHROME_URL)` → `this._getBrowserWidgetContainer()`
- 条件付き依存: `if ( url.startsWith("about:preferences") || url.startsWith("about:settings") )` → `node.closest()`
- 条件付き依存: `if ( url.startsWith("about:preferences") || url.startsWith("about:settings") )` → `container.getAttribute()`
- 条件付き依存: `if ( url.startsWith("about:preferences") || url.startsWith("about:settings") )` → `PREFERENCES_PANES.includes()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `node.getRootNode().host`, `node.localName`, `node.ownerDocument`

## ignoreEvent()
- 位置: L994-996
- 役割: イベントを無視対象として記録し、後の _recordCommand で数えないようにする。
- 触るとき: 特定の操作を UI 操作の集計から外すとき。
- 呼び出し先: `IGNORABLE_EVENTS.set()`

## _recordCommand()
- 位置: L998-1122
- 役割: クリックやコマンドのイベントを対象要素まで遡って、UI 操作の指標に記録する。クリックとコマンドの重複を除き、利用回数や利用済みの pref も更新する。
- 触るとき: UI 操作の対象要素、重複の扱い、利用回数の pref を変えるとき。
- 呼び出し先: `IGNORABLE_EVENTS.get()`, `UI_TARGET_ELEMENTS.get()`, `node.classList?.contains()`, `node.getAttribute()`, `node.ownerDocument.URL.startsWith()`, `sourceEvent.target.contains()`, `targetElements.has()`, `this._getWidgetContainer()`, `this._getWidgetID()`, `this.lastClickTarget?.get()`, `url.schemeIs()`
- 条件付き依存: `if (sourceEvent.type == "click")` → `Cu.getWeakReference()`
- 条件付き依存: `if (sourceEvent.type === "command")` → `PLACES_OPEN_COMMANDS.includes()`
- 条件付き依存: `if ( PLACES_OPEN_COMMANDS.includes(command) || parentNode?.parentNode?.id === PLACES_OPEN_IN_CONTAINER_TAB_MENU_ID )` → `ownerDocument.getElementById()`
- 条件付き依存: `if (item && source)` → `this.recordInteractionEvent()`
- 条件付き依存: `if (isAboutPreferences)` → `node.documentGlobal.recordSettingChangeTelemetry()`
- 条件付き依存: `if (item && source)` → `source .replace(/-/g, "_") .replace()`
- 条件付き依存: `if (item && source)` → `source .replace()`
- 条件付き依存: `if (item && source)` → `p.toUpperCase()`
- 条件付き依存: `if (item && source)` → `Glean.browserUiInteraction[name]?.[telemetryId(item)].add()`
- 条件付き依存: `if (item && source)` → `telemetryId()`
- 条件付き依存: `if (item && source)` → `SET_USAGECOUNT_PREF_BUTTONS.includes()`
- 条件付き依存: `if (SET_USAGECOUNT_PREF_BUTTONS.includes(item))` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (SET_USAGECOUNT_PREF_BUTTONS.includes(item))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (item && source)` → `SET_USAGE_PREF_BUTTONS.includes()`
- 条件付き依存: `if (SET_USAGE_PREF_BUTTONS.includes(item))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (ENTRYPOINT_TRACKED_CONTEXT_MENU_IDS[source])` → `this._getWidgetContainer()`
- 条件付き依存: `if (ENTRYPOINT_TRACKED_CONTEXT_MENU_IDS[source])` → `node.closest()`
- 条件付き依存: `if (triggerContainer)` → `this.recordInteractionEvent()`
- 条件付き依存: `if (triggerContainer)` → `contextMenu .replace(/-/g, "_") .replace()`
- 条件付き依存: `if (triggerContainer)` → `contextMenu .replace()`
- 条件付き依存: `if (triggerContainer)` → `p.toUpperCase()`
- 条件付き依存: `if (triggerContainer)` → `Glean.browserUiInteraction[name]?.[telemetryId(triggerContainer)].add()`
- 条件付き依存: `if (triggerContainer)` → `telemetryId()`
- 参照: `Glean.browserUiInteraction`, `event.type`, `node.closest("menupopup")?.triggerNode`, `node.localName`, `node.parentNode`, `node?.parentNode`, `ownerDocument.getElementById(PLACES_CONTEXT_MENU_ID).triggerNode`, `parentNode?.parentNode?.id`, `sourceEvent.button`, `sourceEvent.originalTarget`, `sourceEvent.originalTarget?.localName`, `sourceEvent.sourceEvent`, `sourceEvent.target`, `sourceEvent.target.localName`, `sourceEvent.target.ownerDocument.documentURIObject`, `sourceEvent.type`, `this.lastClickTarget`
- XPCOM: `Services.prefs`

## recordInteractionEvent()
- 位置: L1127-1150
- 役割: UI 操作を、5 分以上の間隔が空くまで同じフローとして扱い、フローの ID 付きで記録する。新しいフローの開始時には prototypeNoCodeEvents を送る。
- 触るとき: 操作ログのフロー区切りや記録する項目を変えるとき。
- 呼び出し先: `ChromeUtils.now()`, `Glean.browserUsage.interaction.record()`, `telemetryId()`
- 条件付き依存: `if (!this._flowId || this._flowIdTS + FLOW_IDLE_TIME < ChromeUtils.now())` → `GleanPings.prototypeNoCodeEvents.submit()`
- 条件付き依存: `if (!this._flowId || this._flowIdTS + FLOW_IDLE_TIME < ChromeUtils.now())` → `Services.uuid.generateUUID()`
- 参照: `this._flowId`, `this._flowIdTS`
- XPCOM: `Services.uuid`

## _addUsageListeners()
- 位置: L1155-1160
- 役割: 窓に、change、toggle、click、command の捕捉用リスナーを登録する。
- 触るとき: UI 操作として捕捉するイベントの種類を増やすとき。
- 呼び出し先: `UI_TARGET_ELEMENTS.keys()`, `UI_TARGET_ELEMENTS.keys().forEach()`, `this._recordCommand()`, `win.addEventListener()`

## recordWidgetChange()
- 位置: L1168-1185
- 役割: ウィジェットの配置変化を記録する。nav-bar は URL バーの前後で -start と -end に分ける。
- 触るとき: 配置変化の指標での位置名の付け方を変えるとき。
- 呼び出し先: `console.error()`, `this._recordWidgetChange()`
- 条件付き依存: `if (newPos == "nav-bar")` → `lazy.CustomizableUI.getPlacementOfWidget()`

## recordToolbarVisibility()
- 位置: L1187-1196
- 役割: ツールバーの表示・非表示の変化を、内部の記録へ渡す。
- 触るとき: ツールバー表示の指標の値(on または off)を変えるとき。
- 呼び出し先: `this._recordWidgetChange()`

## _recordWidgetChange()
- 位置: L1198-1256
- 役割: ウィジェットの追加・移動・削除を前回の配置と比べて記録する。URL バーの移動は前後の nav-bar の要素の変化に置き換える。
- 触るとき: 配置変化の指標のキー(操作、前後の位置、理由)の作り方を変えるとき。widgetMap が無い時は何もしない。
- 呼び出し先: `Glean.browserUi.customizedWidgets[key].add()`, `telemetryId()`, `this.widgetMap.get()`
- 条件付き依存: `if (widgetId == "urlbar-container")` → `lazy.CustomizableUI.getWidgetsInArea()`
- 条件付き依存: `if (widgetId == "urlbar-container")` → `widget.id.startsWith()`
- 条件付き依存: `if (widgetId == "urlbar-container")` → `this._recordWidgetChange()`
- 条件付き依存: `if (newPos)` → `this.widgetMap.set()`
- 条件付き依存: `if (!(newPos))` → `this.widgetMap.delete()`
- 参照: `Glean.browserUi.customizedWidgets`, `this.widgetMap`, `widget.id`

## _recordUITelemetry()
- 位置: L1258-1277
- 役割: 起動時に、ツールバーの配置を指標へ記録する。
- 触るとき: 起動時のツールバー指標の内容や形式を変えるとき。
- 呼び出し先: `Glean.browserUi.mirrorForToolbarWidgets[key].set()`, `telemetryId()`, `this._buildWidgetPositions()`, `this.widgetMap.entries()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `Glean.browserUi.toolbarWidgets.set()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `this.widgetMap .entries() .map()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `this.widgetMap .entries()`
- 条件付き依存: `if ("toolbarWidgets" in Glean.browserUi)` → `telemetryId()`
- 参照: `Glean.browserUi`, `Glean.browserUi.mirrorForToolbarWidgets`, `this.widgetMap`

## _recordPrefValues()
- 位置: L1284-1287
- 役割: 起動時と日次の処理で、現在のタブ設定と Nova の値を指標へ記録する。
- 触るとき: 定期的に記録する設定値を増やすとき。
- 呼び出し先: `this._recordNovaEnabledValue()`, `this._recordOpenNextToActiveTabSettingValue()`

## _isOpenNextToActiveTabSettingEnabled()
- 位置: L1292-1300
- 役割: 外部リンクの開き先が現在のタブの隣かどうかを、Nimbus の openBehavior で判定する。
- 触るとき: 現在のタブの隣で開く設定の判定条件を変えるとき。
- 呼び出し先: `lazy.NimbusFeatures.externalLinkHandling.getVariable()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB_AFTER_CURRENT`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md)

## _recordOpenNextToActiveTabSettingValue()
- 位置: L1302-1306
- 役割: 現在のタブの隣で開く設定の有効・無効を指標に記録する。
- 触るとき: その指標の送り先や形式を変えるとき。
- 呼び出し先: `Glean.linkHandling.openNextToActiveTabSettingsEnabled.set()`, `this._isOpenNextToActiveTabSettingEnabled()`

## _recordNovaEnabledValue()
- 位置: L1308-1312
- 役割: browser.nova.enabled の値を指標に記録する。
- 触るとき: Nova 設定の指標を見直すとき。
- 呼び出し先: `Glean.nova.enabled.set()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## _registerWindow()
- 位置: L1319-1340
- 役割: 窓に、UI 操作の監視、タブとタブグループのイベント、タブの読み込み監視を登録する。
- 触るとき: 窓ごとに監視するイベントを増やすとき。
- 呼び出し先: `this._addUsageListeners()`, `win.addEventListener()`, `win.gBrowser.addTabsProgressListener()`, `win.gBrowser.tabContainer.addEventListener()`

## _unregisterWindow()
- 位置: L1345-1367
- 役割: _registerWindow で登録したイベントと読み込み監視を窓から外す。
- 触るとき: 窓を閉じた時に監視が残らないことを確かめるとき。登録と対応を保つこと。
- 呼び出し先: `win.defaultView.gBrowser.removeTabsProgressListener()`, `win.defaultView.gBrowser.tabContainer.removeEventListener()`, `win.removeEventListener()`

## _onTabOpen()
- 位置: L1375-1422
- 役割: タブが開いたことを数え、外部アプリからの開き方に応じた位置を記録し、コンテナのタブの開きを記録して、タブ数の集計を予約する。
- 触るとき: タブを開く操作の指標や、外部アプリからのリンクの扱いを変えるとき。多数のタブを同時に開く場合は集計をまとめる。
- 呼び出し先: `event?.target?.getAttribute()`, `this._onTabsOpenedTask.arm()`, `this._onTabsOpenedTask.disarm()`
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.browserEngagement.verticalTabOpenEventCount.add()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.browserEngagement.tabOpenEventCount.add()`
- 条件付き依存: `if (event?.target?.group)` → `Glean.tabgroup.tabInteractions.new.add()`
- 条件付き依存: `if (event.detail?.fromExternal)` → `this._isOpenNextToActiveTabSettingEnabled()`
- 条件付き依存: `if (event.detail?.fromExternal)` → `Glean.linkHandling.openFromExternalApp.record()`
- 条件付き依存: `if (wasOpenedNextToActiveTab)` → `externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.add()`
- 条件付き依存: `if (!(wasOpenedNextToActiveTab))` → `externalTabMovementRegistry.externallyOpenedTabsAtEndOfTabStrip.add()`
- 条件付き依存: `if (!(event.detail?.fromExternal))` → `externalTabMovementRegistry.internallyOpenedTabs.add()`
- 条件付き依存: `if (userContextId)` → `Glean.containers.containerTabOpened.record()`
- 条件付き依存: `if (userContextId)` → `String()`
- 参照: `event.detail?.containerSource`, `event.detail?.fromExternal`, `event.target`, `event?.target?.group`, `lazy.sidebarVerticalTabs`

## _onTabsOpened()
- 位置: L1427-1435
- 役割: 複数のタブが開いた後に、タブ数と最大値を更新して記録する。
- 触るとき: タブ数の記録タイミングを変えるとき。
- 呼び出し先: `getOpenTabsAndWinsCounts()`, `this._recordTabCounts()`
- 条件付き依存: `if (tabCount > this.maxTabCount)` → `this.maxTabCountGleanQuantity.set()`
- 参照: `this.maxTabCount`

## _onTabClosed()
- 位置: L1442-1485
- 役割: タブが閉じた時に、タブグループ、通常の閉じ方、コンテナ、ピン留めの指標を記録し、外部から開いたタブの追跡を解除する。
- 触るとき: 閉じる操作の指標を増やすとき、外部から開いたタブの追跡を見直すとき。
- 呼び出し先: `event?.target?.getAttribute()`
- 条件付き依存: `if ( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_STRIP )` → `Glean.tabgroup.tabInteractions.close_tabstrip.add()`
- 条件付き依存: `if ( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_MENU || metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU )` → `Glean.tabgroup.tabInteractions.close_tabmenu.add()`
- 条件付き依存: `if (!( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_MENU || metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU ))` → `Glean.tabgroup.tabInteractions.close_tab_other.add()`
- 条件付き依存: `if (userContextId)` → `Glean.containers.containerTabClosed.record()`
- 条件付き依存: `if (userContextId)` → `String()`
- 条件付き依存: `if (event.target?.pinned)` → `getPinnedTabsCount()`
- 条件付き依存: `if (event.target?.pinned)` → `this.recordPinnedTabsCount()`
- 条件付き依存: `if (event.target?.pinned)` → `Glean.pinnedTabs.close.record()`
- 条件付き依存: `if (event.target)` → `Object.values(externalTabMovementRegistry).forEach()`
- 条件付き依存: `if (event.target)` → `Object.values()`
- 条件付き依存: `if (event.target)` → `set.delete()`
- 参照: `event.detail.metricsContext`, `event.target`, `event.target?.group`, `event.target?.pinned`, `lazy.TabMetrics.METRIC_SOURCE.TAB_MENU`, `lazy.TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU`, `lazy.TabMetrics.METRIC_SOURCE.TAB_STRIP`, `lazy.sidebarVerticalTabs`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`

## _onTabPinned()
- 位置: L1487-1502
- 役割: ピン留めの操作を数え、最大数と現在の数を記録する。
- 触るとき: ピン留めの指標の内容を変えるとき。
- 呼び出し先: `Glean.pinnedTabs.pin.record()`, `getPinnedTabsCount()`, `this.recordPinnedTabsCount()`, `this.updateMaxTabPinnedCount()`
- 条件付き依存: `if (lazy.sidebarVerticalTabs)` → `Glean.browserEngagement.verticalTabPinnedEventCount.add()`
- 条件付き依存: `if (!(lazy.sidebarVerticalTabs))` → `Glean.browserEngagement.tabPinnedEventCount.add()`
- 参照: `event.detail.metricsContext.telemetrySource`, `lazy.sidebarVerticalTabs`

## _onTabUnpinned()
- 位置: L1504-1506
- 役割: ピン留めを外した時に、現在のピン留め数を記録する。
- 触るとき: ピン留め解除の指標を変えるとき。
- 呼び出し先: `this.recordPinnedTabsCount()`

## _onTabGroupCreateByUser()
- 位置: L1508-1519
- 役割: ユーザーがタブグループを作った時に作成の指標を記録し、グループ変化の集計を予約する。
- 触るとき: タブグループ作成の指標の項目を変えるとき。
- 呼び出し先: `Glean.tabgroup.createGroup.record()`, `this._onTabGroupChange()`
- 参照: `event.detail.metricsContext.telemetrySource`, `event.target.id`, `event.target.tabs.length`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `lazy.sidebarVerticalTabs`

## _onTabGroupSave()
- 位置: L1521-1534
- 役割: タブグループの保存を記録し、ユーザー操作の場合は保存の回数を増やす。
- 触るとき: 保存の指標を変えるとき。
- 呼び出し先: `Glean.tabgroup.save.record()`, `this._onTabGroupChange()`
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.groupInteractions.save.add()`
- 参照: `event.detail`, `event.target.id`, `metricsContext.isUserTriggered`

## _onTabGroupChange()
- 位置: L1536-1539
- 役割: タブグループの変化による集計を、短時間に重なった呼び出しをまとめて遅らせて予約する。
- 触るとき: グループ変化の集計の頻度を変えるとき。
- 呼び出し先: `this._onTabGroupChangeTask.arm()`, `this._onTabGroupChangeTask.disarm()`

## _onTabGroupUngroup()
- 位置: L1544-1558
- 役割: ユーザーが解除した時に解除の指標を記録し、タブグループのメニューからの解除だけ回数に加える。
- 触るとき: グループ解除の指標や回数の数え方を変えるとき。
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.ungroup.record()`
- 条件付き依存: `if ( metricsContext.telemetrySource == lazy.TabMetrics.METRIC_SOURCE.TAB_GROUP_MENU )` → `Glean.tabgroup.groupInteractions.ungroup.add()`
- 参照: `event.detail`, `lazy.TabMetrics.METRIC_SOURCE.TAB_GROUP_MENU`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`

## _getSummaryStats()
- 位置: L1566-1580
- 役割: 数値の配列から最大・最小・中央値・平均を求める。
- 触るとき: グループの統計値の定義を変えるとき。引数の配列を並べ替えるので、呼び出し元で順序に依存しないこと。
- 呼び出し先: `Math.floor()`, `data.at()`, `data.reduce()`, `data.sort()`
- 参照: `data.length`

## _doOnTabGroupChange()
- 位置: L1582-1606
- 役割: 全窓のタブ数、グループ内外のタブ数、グループごとのタブ数の統計値を指標に記録する。
- 触るとき: タブグループの指標の定義や送り先を変えるとき。
- 呼び出し先: `Glean.tabgroup.tabCountInGroups.inside.set()`, `Glean.tabgroup.tabCountInGroups.outside.set()`, `Glean.tabgroup.tabsPerActiveGroup.average.set()`, `Glean.tabgroup.tabsPerActiveGroup.max.set()`, `Glean.tabgroup.tabsPerActiveGroup.median.set()`, `Glean.tabgroup.tabsPerActiveGroup.min.set()`, `Services.wm.getEnumerator()`, `tabGroupLengths.push()`, `this._getSummaryStats()`
- 参照: `group.tabs.length`, `win.gBrowser.tabGroups`, `win.gBrowser.tabs.length`
- XPCOM: `Services.wm`

## _onSavedTabGroupsChange()
- 位置: L1608-1611
- 役割: 保存済みタブグループの変化による集計を、短時間にまとめて遅らせて予約する。
- 触るとき: 保存済みグループの集計頻度を変えるとき。
- 呼び出し先: `this._onSavedTabGroupsChangedTask.arm()`, `this._onSavedTabGroupsChangedTask.disarm()`

## _doOnSavedTabGroupsChange()
- 位置: L1613-1624
- 役割: 保存済みタブグループの数と、グループごとのタブ数の統計値を指標に記録する。
- 触るとき: 保存済みグループの指標を変えるとき。
- 呼び出し先: `Glean.tabgroup.savedGroups.set()`, `Glean.tabgroup.tabsPerSavedGroup.average.set()`, `Glean.tabgroup.tabsPerSavedGroup.max.set()`, `Glean.tabgroup.tabsPerSavedGroup.median.set()`, `Glean.tabgroup.tabsPerSavedGroup.min.set()`, `lazy.SessionStore.getSavedTabGroups()`, `savedGroups.map()`, `this._getSummaryStats()`
- 参照: `group.tabs.length`, `savedGroups.length`

## _onTabGroupExpandOrCollapse()
- 位置: L1626-1629
- 役割: タブグループの展開・折りたたみによる集計を、まとめて遅らせて予約する。
- 触るとき: 展開・折りたたみの集計頻度を変えるとき。
- 呼び出し先: `this._onTabGroupExpandOrCollapseTask.arm()`, `this._onTabGroupExpandOrCollapseTask.disarm()`

## _doOnTabGroupExpandOrCollapse()
- 位置: L1631-1647
- 役割: 全窓のタブグループを折りたたみと展開に分けて数え、指標に記録する。
- 触るとき: 展開・折りたたみの指標の定義を変えるとき。
- 呼び出し先: `Glean.tabgroup.activeGroups.collapsed.set()`, `Glean.tabgroup.activeGroups.expanded.set()`, `Services.wm.getEnumerator()`
- 参照: `group.collapsed`, `win.gBrowser.tabGroups`
- XPCOM: `Services.wm`

## _onTabGroupRemoveRequested()
- 位置: L1652-1662
- 役割: ユーザーがグループの削除を依頼した時に、削除の指標と削除の回数を記録する。
- 触るとき: グループ削除の指標を変えるとき。
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.delete.record()`
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `Glean.tabgroup.groupInteractions.delete.add()`
- 参照: `event.detail`, `event.target.id`, `lazy.TabMetrics.UNKNOWN_CONTEXT`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`

## _onTabMove()
- 位置: L1674-1719
- 役割: ユーザー操作によるタブの移動を、移動元の種類とグループ状態ごとに集約し、グループへの追加などの指標を記録する。
- 触るとき: タブ移動の指標を変えるとき。同じ種類の移動は 1 件にまとめて送る。
- 呼び出し先: `[metricsContext.telemetrySource, groupType].join()`, `this._recordExternalTabMovement()`, `this._tabMovementsBySegment.get()`
- 条件付き依存: `if (tabMovementsRecord.numberAddedToTabGroup)` → `Glean.tabgroup.addTab.record()`
- 条件付き依存: `if (!tabMovementsRecord)` → `this._tabMovementsBySegment.delete()`
- 条件付き依存: `if (!tabMovementsRecord)` → `this._tabMovementsBySegment.set()`
- 条件付き依存: `if (!tabMovementsRecord)` → `this._updateTabMovementsRecord()`
- 条件付き依存: `if (!tabMovementsRecord)` → `deferredTask.arm()`
- 条件付き依存: `if (!(!tabMovementsRecord))` → `tabMovementsRecord.deferredTask.disarm()`
- 条件付き依存: `if (!(!tabMovementsRecord))` → `this._updateTabMovementsRecord()`
- 条件付き依存: `if (!(!tabMovementsRecord))` → `tabMovementsRecord.deferredTask.arm()`
- 参照: `event.detail`, `event.target.group`, `event.target.group.collapsed`, `lazy.DeferredTask`, `lazy.TabMetrics.METRIC_GROUP_TYPE.COLLAPSED`, `lazy.TabMetrics.METRIC_GROUP_TYPE.EXPANDED`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `lazy.TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `lazy.sidebarVerticalTabs`, `metricsContext.isUserTriggered`, `metricsContext.telemetrySource`, `tabMovementsRecord.numberAddedToTabGroup`

## _updateTabMovementsRecord()
- 位置: L1725-1744
- 役割: 移動の前後のタブの状態を比べて、グループへの追加、並べ替え、グループからの除外を数える。
- 触るとき: 移動の種類の判定条件を変えるとき。
- 条件付き依存: `if (!previousTabState.tabGroupId && currentTabState.tabGroupId)` → `Glean.tabgroup.tabInteractions.add.add()`
- 条件付き依存: `if ( previousTabState.tabGroupId && previousTabState.tabGroupId == currentTabState.tabGroupId && previousTabState.tabIndex != currentTabState.tabIndex )` → `Glean.tabgroup.tabInteractions.reorder.add()`
- 条件付き依存: `if (previousTabState.tabGroupId && !currentTabState.tabGroupId)` → `Glean.tabgroup.tabInteractions.remove_same_window.add()`
- 参照: `currentTabState.tabGroupId`, `currentTabState.tabIndex`, `event.detail`, `previousTabState.tabGroupId`, `previousTabState.tabIndex`, `record.numberAddedToTabGroup`

## _recordExternalTabMovement()
- 位置: L1750-1766
- 役割: 外部アプリから開かれたタブの移動を、開かれ方(内部、隣、末尾)に応じて記録する。
- 触るとき: 外部から開いたタブの移動の指標を変えるとき。
- 呼び出し先: `externalTabMovementRegistry.internallyOpenedTabs.has()`
- 条件付き依存: `if (externalTabMovementRegistry.internallyOpenedTabs.has(event.target))` → `Glean.browserUiInteraction.tabMovement.not_from_external_app.add()`
- 条件付き依存: `if (!(externalTabMovementRegistry.internallyOpenedTabs.has(event.target)))` → `externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.has()`
- 条件付き依存: `if ( externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.has( event.target ) )` → `Glean.browserUiInteraction.tabMovement.from_external_app_next_to_active_tab.add()`
- 条件付き依存: `if (!( externalTabMovementRegistry.externallyOpenedTabsNextToActiveTab.has( event.target ) ))` → `externalTabMovementRegistry.externallyOpenedTabsAtEndOfTabStrip.has()`
- 条件付き依存: `if ( externalTabMovementRegistry.externallyOpenedTabsAtEndOfTabStrip.has( event.target ) )` → `Glean.browserUiInteraction.tabMovement.from_external_app_tab_strip_end.add()`
- 参照: `event.target`

## _onTabSelect()
- 位置: L1768-1781
- 役割: グループ内やピン留めのタブを選んだ操作を、折りたたみ状態と表示モードに応じて記録する。
- 触るとき: タブ選択の指標を変えるとき。
- 条件付き依存: `if (event.target.group)` → `interaction.add()`
- 条件付き依存: `if (event.target.pinned)` → `counter.add()`
- 参照: `Glean.pinnedTabs.activations.horizontalBar`, `Glean.pinnedTabs.activations.sidebar`, `Glean.tabgroup.tabInteractions.activate_collapsed`, `Glean.tabgroup.tabInteractions.activate_expanded`, `event.target.group`, `event.target.group.collapsed`, `event.target.pinned`, `lazy.sidebarVerticalTabs`

## _onWindowOpen()
- 位置: L1788-1820
- 役割: 開かれた窓が通常のブラウザ窓なら、読み込み後に登録する処理を予約する。
- 触るとき: 窓が開いた時の処理の入口を変えるとき。
- 呼び出し先: `win.addEventListener()`
- 参照: `Ci.nsIDOMWindow`
- XPCOM: [`nsIDOMWindow`](../../dom/base/nsISlowScriptDebug.idl.md)

## onLoad()
- 位置: L1794-1818
- 役割: 窓の読み込み完了後に、通常の窓なら監視を登録し、窓の開き数と最大窓数を記録して、最初のタブが開いたものとして扱う。
- 触るとき: 窓を開いた時の記録の仕方を変えるとき。
- 呼び出し先: `Glean.browserEngagement.windowOpenEventCount.add()`, `getOpenTabsAndWinsCounts()`, `this._onTabOpen()`, `this._registerWindow()`, `win.document.documentElement.getAttribute()`, `win.removeEventListener()`
- 条件付き依存: `if (counts.winCount > this.maxWindowCount)` → `Glean.browserEngagement.maxConcurrentWindowCount.set()`
- 参照: `counts.winCount`, `this.maxWindowCount`

## _recordTabCounts()
- 位置: L1833-1853
- 役割: タブ数と読み込み済みタブ数を、前回の記録から一定間隔が空いた時だけ記録する。
- 触るとき: タブ数の記録頻度(MINIMUM_TAB_COUNT_INTERVAL_MS)や記録する値を変えるとき。
- 呼び出し先: `Date.now()`
- 条件付き依存: `if ( tabCount !== undefined && currentTime > this._lastRecordTabCount + MINIMUM_TAB_COUNT_INTERVAL_MS )` → `Glean.browserEngagement.tabCount.accumulateSingleSample()`
- 条件付き依存: `if ( loadedTabCount !== undefined && currentTime > this._lastRecordLoadedTabCount + MINIMUM_TAB_COUNT_INTERVAL_MS )` → `Glean.browserEngagement.loadedTabCount.accumulateSingleSample()`
- 参照: `this._lastRecordLoadedTabCount`, `this._lastRecordTabCount`

## _checkProfileCountFileSchema()
- 位置: L1855-1872
- 役割: プロファイル数ファイルの version と ID 一覧の型を検査し、違えば例外を投げる。
- 触るとき: プロファイル数ファイルの形式を変えるとき。
- 呼び出し先: `Array.isArray()`
- 参照: `fileData.profileTelemetryIds`, `fileData.version`

## reportProfileCount()
- 位置: async L1875-1960
- 役割: Windows で、同じインストールに属するプロファイル数をファイルで数え、1, 2, 3 から 10000 までの段階に丸めて報告する。読み書きに失敗した時は 0 を報告する。
- 触るとき: プロファイル数の指標を見直すとき。ファイルに入る ID の数は最大の段階で抑えている。
- 呼び出し先: `BrowserUsageTelemetry.Policy.getTelemetryClientId()`, `BrowserUsageTelemetry.Policy.getUpdateDirectory()`, `BrowserUsageTelemetry.Policy.readProfileCountFile()`, `BrowserUsageTelemetry._checkProfileCountFileSchema()`, `Glean.browserEngagement.profileCount.set()`, `JSON.parse()`, `Math.max()`, `fileData.profileTelemetryIds.includes()`, `profileCountFile.append()`
- 条件付き依存: `if (!(ex.name == "NotFoundError"))` → `console.error()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `fileData.profileTelemetryIds.push()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `BrowserUsageTelemetry.Policy.writeProfileCountFile()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `JSON.stringify()`
- 条件付き依存: `if ( !fileData.profileTelemetryIds.includes(currentTelemetryId) && fileData.profileTelemetryIds.length < Math.max(...buckets) )` → `console.error()`
- 参照: `ex.name`, `fileData.profileTelemetryIds.length`, `profileCountFile.path`, `updateDirectory.leafName`, `updateDirectory.parent.parent`

## collectInstallationTelemetry()
- 位置: async L1975-2105
- 役割: Windows で、初回に見たインストールの情報を集める。MSIX と従来のインストーラーで手順が分かれ、同じ情報は二度送らない。
- 触るとき: 初回インストールの指標の内容を変えるとき。タイムスタンプで重複送信を防いでいる。
- 呼び出し先: `Cc["@mozilla.org/windows-package-manager;1"].createInstance()`, `Services.prefs.getStringPref()`, `Services.sysinfo.getProperty()`
- 条件付き依存: `if (pfn)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (pfn)` → `wpm.getInstalledDate()`
- 条件付き依存: `if (pfn)` → `getInstallData()`
- 条件付き依存: `if (pfn)` → `install_data.msixInstalls.has(pfn).toString()`
- 条件付き依存: `if (pfn)` → `install_data.msixInstalls.has()`
- 条件付き依存: `if (pfn)` → `install_data.msixInstalls.delete()`
- 条件付き依存: `if (pfn)` → `(!!install_data.installPaths.size).toString()`
- 条件付き依存: `if (pfn)` → `(!!install_data.msixInstalls.size).toString()`
- 条件付き依存: `if (!dataPath)` → `Services.dirsvc.get()`
- 条件付き依存: `if (!dataPath)` → `dataPath.append()`
- 条件付き依存: `if (!(pfn))` → `IOUtils.read()`
- 条件付き依存: `if (!(pfn))` → `new TextDecoder("utf-16").decode()`
- 条件付き依存: `if (!(pfn))` → `JSON.parse()`
- 条件付き依存: `if (!(pfn))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(pfn))` → `getInstallData()`
- 条件付き依存: `if (!(pfn))` → `data.admin_user.toString()`
- 条件付き依存: `if (!(pfn))` → `data.install_existed.toString()`
- 条件付き依存: `if (!(pfn))` → `data.profdir_existed.toString()`
- 条件付き依存: `if (!(pfn))` → `(!!install_data.installPaths.size).toString()`
- 条件付き依存: `if (!(pfn))` → `(!!install_data.msixInstalls.size).toString()`
- 条件付き依存: `if (data.installer_type == "full")` → `data.silent.toString()`
- 条件付き依存: `if (data.installer_type == "full")` → `data.from_msi.toString()`
- 条件付き依存: `if (data.installer_type == "full")` → `data.default_path.toString()`
- 参照: `AppConstants.MOZ_APP_VERSION`, `AppConstants.MOZ_BUILDID`, `AppConstants.platform`, `Ci.nsIFile`, `Ci.nsIWindowsPackageManager`, `data.build_id`, `data.install_timestamp`, `data.installer_type`, `data.version`, `dataPath.path`, `ex.name`, `extra.admin_user`, `extra.build_id`, `extra.default_path`, `extra.from_msi`, `extra.install_existed`, `extra.other_inst`, `extra.other_msix_inst`, `extra.profdir_existed`, `extra.silent`, `extra.version`, `install_data.installPaths.size`, `install_data.msixInstalls.size`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / [`nsIWindowsPackageManager`](../../toolkit/system/windowsPackageManager/nsIWindowsPackageManager.idl.md) / `@mozilla.org/windows-package-manager;1` → `mozilla::toolkit::system::nsWindowsPackageManager` (toolkit/system/windowsPackageManager/components.conf) / `Services.dirsvc` / `Services.prefs` / `Services.sysinfo`

## getInstallData()
- 位置: L1995-2017
- 役割: 他のインストールの有無を、インストール先のパスと MSIX のパッケージから調べる。エラーは無視する。
- 触るとき: 他インストールの検出方法を変えるとき。
- 呼び出し先: `Services.dirsvc.get()`, `lazy.WindowsInstallsInfo.getInstallPaths()`, `msixInstalls.add()`, `wpm .findUserInstalledPackages()`, `wpm .findUserInstalledPackages(msixPackagePrefixes) .forEach()`
- 条件付き依存: `if (pfn)` → `msixInstalls.delete()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("GreBinD", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## reportInstallationTelemetry()
- 位置: async L2107-2166
- 役割: 初回インストールの情報を集め、installer_type に応じたイベントと各スカラーを記録する。進行中の呼び出しがあればその結果を再利用する。
- 触るとき: インストール指標の送り先や値の変換を変えるとき。dataPathOverride を渡した場合(テスト用)は再利用しない。
- 呼び出し先: `BrowserUsageTelemetry.collectInstallationTelemetry()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installation.firstSeenFull.record()`
- 条件付き依存: `if (installer_type == "stub")` → `Glean.installation.firstSeenStub.record()`
- 条件付き依存: `if (installer_type == "msix")` → `Glean.installation.firstSeenMsix.record()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.installerType.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.version.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.adminUser.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.installExisted.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.profdirExisted.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.otherInst.set()`
- 条件付き依存: `if (data?.installer_type)` → `Glean.installationFirstSeen.otherMsixInst.set()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installationFirstSeen.silent.set()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installationFirstSeen.fromMsi.set()`
- 条件付き依存: `if (installer_type == "full")` → `Glean.installationFirstSeen.defaultPath.set()`
- 参照: `data?.installer_type`, `extra.admin_user`, `extra.default_path`, `extra.from_msi`, `extra.install_existed`, `extra.other_inst`, `extra.other_msix_inst`, `extra.profdir_existed`, `extra.silent`, `extra.version`

## getUniqueDomainsVisitedInPast24Hours()
- 位置: L2170-2172
- 役割: nsIBrowserUsage 向けに、過去 24 時間のユニークドメイン数を返す。
- 触るとき: C++ 側から呼ばれるこの値の取得経路を変えるとき。
- 参照: `URICountListener.uniqueDomainsVisitedInPast24Hours`
