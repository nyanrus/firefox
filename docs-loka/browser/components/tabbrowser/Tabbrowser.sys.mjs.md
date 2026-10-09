# browser/components/tabbrowser/Tabbrowser.sys.mjs

source: browser/components/tabbrowser/Tabbrowser.sys.mjs
source-hash: 430e1137a15f0aa8c5f39fd76127f825b2751c69
lines: 11180

## <module>
- 役割: 遅延ロードのモジュール群と定数を宣言し、各ウィンドウの gBrowser となる Tabbrowser クラスと、補助の TabProgressListener、URILoadingWrapper を定義する。
- 呼び出し先: `ChromeUtils.generateQI()`, `XPCOMUtils.declareLazy()`

## tabLocalization()
- 位置: L66-74
- 役割: tabbrowser.ftl などを読み込む Localization を遅延生成するファクトリ。
- 触るとき: タブ周りの文言 (FTL) の読み込み元を変えるとき。

## getTotalMemoryUsage()
- 位置: async L118-125
- 役割: 親プロセスと全子プロセスのメモリ使用量を合計して非同期で返す。
- 触るとき: タブの明示アンロード時のメモリ計測を調べるとき。直前のコメントは本文と合っていない。
- 呼び出し先: `ChromeUtils.requestProcInfo()`
- 参照: `child.memory`, `procInfo.children`, `procInfo.memory`

## handleDroppedLink()
- 位置: async L132-200
- 役割: ドロップされたリンクを数の警告で確認し、URL を解決して対象タブに loadTabs で読み込む。
- 触るとき: コンテンツ領域へのリンクのドロップ動作を変えるとき。
- 呼び出し先: `Array.isArray()`, `Services.prefs.getIntPref()`, `browser.getAttribute()`, `lazy.UrlbarUtils.getShortcutOrURIAndPostData()`, `postDatas.push()`, `urls.push()`
- 条件付き依存: `if (event)` → `event.preventDefault()`
- 条件付き依存: `if (event)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( links.length >= Services.prefs.getIntPref("browser.tabs.maxOpenBeforeWarn") )` → `lazy.OpenInTabsUtils.promiseConfirmOpenInTabs()`
- 条件付き依存: `if (lastLocationChange == browser.lastLocationChange)` → `tabbrowser.loadTabs()`
- 条件付き依存: `if (lastLocationChange == browser.lastLocationChange)` → `tabbrowser.getTabForBrowser()`
- 参照: `browser.lastLocationChange`, `data.postData`, `data.url`, `event.shiftKey`, `link.url`, `links.length`, `tabbrowser.documentGlobal`
- XPCOM: `Services.prefs`

## Tabbrowser.create()
- 位置: L227-230
- 役割: Tabbrowser を作って window.gBrowser に設定し、init を呼ぶ静的メソッド。
- 触るとき: ウィンドウ起動時の gBrowser 初期化の入口を調べるとき。
- 呼び出し先: `window.gBrowser.init()`
- 参照: `window.gBrowser`

## Tabbrowser.destroy()
- 位置: L232-234
- 役割: window.gBrowser の destroy を呼ぶ静的メソッド。
- 触るとき: ウィンドウ終了時の後始末の入口を調べるとき。
- 呼び出し先: `window.gBrowser.destroy()`

## Tabbrowser.init()
- 位置: L236-302
- 役割: 必要な DOM 要素の取得、オブザーバとイベントリスナの登録、最初のブラウザとタブの構築を行う。
- 触るとき: gBrowser の起動時初期化や、登録されるイベントを変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.getIntPref()`, `this.#setFindbarData()`, `this.#setupEventListeners()`, `this.#setupInitialBrowserAndTab()`, `this.document.addEventListener()`, `this.document.getElementById()`, `this.document.querySelector()`, `this.document.querySelector("title").removeAttribute()`, `this.documentGlobal .matchMedia()`, `this.documentGlobal .matchMedia("(prefers-color-scheme: dark)") .addEventListener()`, `this.documentGlobal.addEventListener()`, `this.tabContainer.init()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.display.document_color_use") == 2)` → `Services.prefs.getCharPref()`
- 参照: `this.#defaultDropLinkHandler`, `this._initialized`, `this.pinnedTabsContainer`, `this.splitViewCommandSet`, `this.tabContainer`, `this.tabGroupMenu`, `this.tabNoteMenu`, `this.tabbox`, `this.tabpanels`, `this.tabpanels.style.backgroundColor`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#defaultDropLinkHandler()
- 位置: L282-284
- 役割: ドロップ先の browser を this として handleDroppedLink を呼ぶ関数 (init 内で代入される)。
- 触るとき: browser 要素の droppedLinkHandler の中身を追うとき。
- 呼び出し先: `handleDroppedLink()`, `this.getTabBrowser()`

## Tabbrowser.ownerDocument()
- 位置: L310-312
- 役割: this.document を返すだけのゲッター。モジュール外の利用者向けに残してある。
- 触るとき: gBrowser.ownerDocument を使う外部コードを調べるとき。
- 参照: `this.document`

## Tabbrowser.TabMetrics()
- 位置: L316-318
- 役割: 遅延ロードした TabMetrics モジュールを返すゲッター。
- 触るとき: gBrowser.TabMetrics を参照する外部コードを調べるとき。
- 参照: `lazy.TabMetrics`

## Tabbrowser.tabLocalization()
- 位置: L320-322
- 役割: 遅延生成した tabLocalization を返すゲッター。
- 触るとき: gBrowser.tabLocalization を参照する外部コードを調べるとき。
- 参照: `lazy.tabLocalization`

## Tabbrowser.constructor()
- 位置: L324-327
- 役割: ウィンドウとその document をプロパティに保持する。
- 触るとき: Tabbrowser が持つ window への参照の出どころを調べるとき。
- 参照: `this.document`, `this.documentGlobal`, `window.document`

## has()
- 位置: L499-504
- 役割: browsers プロキシの has トラップで、数値の添字が tabs に存在するかを返す。
- 触るとき: gBrowser.browsers の添字アクセスの挙動を調べるとき。
- 呼び出し先: `Number.isInteger()`, `parseInt()`
- 参照: `this.tabs`

## get()
- 位置: L505-516
- 役割: browsers プロキシの get トラップで、length は tabs の長さ、数値の添字は対応するタブの linkedBrowser を返す。
- 触るとき: gBrowser.browsers の添字アクセスや長さの扱いを調べるとき。
- 呼び出し先: `Number.isInteger()`, `parseInt()`
- 参照: `this.tabs`, `this.tabs.length`, `this.tabs[name].linkedBrowser`

## Tabbrowser.activeSplitView()
- 位置: L528-530
- 役割: 現在アクティブな分割ビューを返すゲッター。
- 触るとき: 分割ビューの有効状態の参照元を調べるとき。
- 参照: `this.#activeSplitView`

## Tabbrowser.splitViewBrowsers()
- 位置: L537-545
- 役割: アクティブな分割ビューに含まれるタブの browser を配列で返す。
- 触るとき: 分割ビューで同時に表示される browser の扱いを調べるとき。
- 条件付き依存: `if (this.#activeSplitView)` → `browsers.push()`
- 参照: `tab.linkedBrowser`, `this.#activeSplitView`, `this.#activeSplitView.tabs`

## Tabbrowser.tabs()
- 位置: L554-556
- 役割: tabContainer の allTabs を返すゲッター。
- 触るとき: gBrowser.tabs が返すタブの範囲を調べるとき。
- 参照: `this.tabContainer.allTabs`

## Tabbrowser.tabGroups()
- 位置: L558-560
- 役割: tabContainer の allGroups を返すゲッター。
- 触るとき: ウィンドウ内のタブグループの取得元を調べるとき。
- 参照: `this.tabContainer.allGroups`

## Tabbrowser.splitViews()
- 位置: L562-564
- 役割: tabContainer の allSplitViews を返すゲッター。
- 触るとき: ウィンドウ内の分割ビューの取得元を調べるとき。
- 参照: `this.tabContainer.allSplitViews`

## Tabbrowser.tabsInCollapsedTabGroups()
- 位置: L566-571
- 役割: 折りたたまれたグループ内で、非表示でも閉じ中でもないタブを返す。
- 触るとき: 折りたたみグループのタブを選択候補に含める処理を調べるとき。
- 呼び出し先: `this.tabGroups .filter()`, `this.tabGroups .filter(tabGroup => tabGroup.collapsed) .flatMap()`, `this.tabGroups .filter(tabGroup => tabGroup.collapsed) .flatMap(tabGroup => tabGroup.tabs) .filter()`
- 参照: `tab.closing`, `tab.hidden`, `tabGroup.collapsed`, `tabGroup.tabs`

## Tabbrowser.addEventListener()
- 位置: L573-575
- 役割: リスナー登録を tabpanels 要素に委譲する。
- 触るとき: gBrowser へのイベント登録がどの要素に付くかを調べるとき。
- 呼び出し先: `this.tabpanels.addEventListener()`

## Tabbrowser.removeEventListener()
- 位置: L577-579
- 役割: リスナー解除を tabpanels 要素に委譲する。
- 触るとき: gBrowser のイベント解除がどの要素に効くかを調べるとき。
- 呼び出し先: `this.tabpanels.removeEventListener()`

## Tabbrowser.dispatchEvent()
- 位置: L581-583
- 役割: イベントの送出を tabpanels 要素に委譲する。
- 触るとき: gBrowser から送出されるイベントの宛先を調べるとき。
- 呼び出し先: `this.tabpanels.dispatchEvent()`

## Tabbrowser.recordTabMetrics()
- 位置: L593-612
- 役割: ユーザー操作で分解されていない文脈のときだけ、タブ操作を Glean に記録する。
- 触るとき: タブ操作のテレメトリの記録条件や項目を変えるとき。
- 呼び出し先: `Glean.tab.actions[action].add()`, `Glean.tab.interaction.record()`, `Glean.tab.tabCount[action].add()`
- 参照: `Glean.tab.actions`, `Glean.tab.tabCount`, `metricsContext.isDecomposed`, `metricsContext.telemetrySource`, `metricsContext?.isUserTriggered`, `this.selectedTabs.length`, `this.tabContainer.verticalMode`

## Tabbrowser.openTabs()
- 位置: L618-620
- 役割: tabContainer の openTabs を返す。非表示や折りたたみ内を含み、閉じ中と Firefox View は除く。
- 触るとき: 閉じ中のタブを除いた一覧が必要なとき。
- 参照: `this.tabContainer.openTabs`

## Tabbrowser.nonHiddenTabs()
- 位置: L625-627
- 役割: tabContainer の nonHiddenTabs を返す。openTabs から非表示を除いたもの。
- 触るとき: 非表示タブを除いた一覧が必要なとき。
- 参照: `this.tabContainer.nonHiddenTabs`

## Tabbrowser.visibleTabs()
- 位置: L632-634
- 役割: tabContainer の visibleTabs を返す。非表示と折りたたみグループ内を除いたもの。
- 触るとき: 画面上に見えているタブの一覧が必要なとき。
- 参照: `this.tabContainer.visibleTabs`

## Tabbrowser.pinnedTabCount()
- 位置: L636-643
- 役割: 先頭から続くピン留めタブの数 (最初の非ピンタブの添字) を返す。
- 触るとき: ピン留めタブと通常タブの境界の計算を調べるとき。
- 参照: `this.tabs`, `this.tabs.length`, `this.tabs[i].pinned`

## Tabbrowser.setSelectedTab()
- 位置: L645-664
- 役割: 共有警告やモーダル表示中などは何もせず、それ以外は tabbox の選択タブを切り替えて ACTIVATE を記録する。
- 触るとき: タブ選択が無視される条件や、選択時のテレメトリを変えるとき。
- 呼び出し先: `this.document.documentElement.hasAttribute()`, `this.documentGlobal.gSharedTabWarning.willShowSharedTabWarning()`, `this.recordTabMetrics()`
- 参照: `this.TabMetrics.METRIC_ACTION.ACTIVATE`, `this.documentGlobal.gNavToolbox.collapsed`, `this.selectedTab`, `this.tabbox.selectedTab`

## Tabbrowser.selectedTab()
- 位置: L670-672
- 役割: setSelectedTab を呼ぶセッター。
- 触るとき: gBrowser.selectedTab への代入の経路を調べるとき。
- 呼び出し先: `this.setSelectedTab()`

## Tabbrowser.selectedTab()
- 位置: L674-676
- 役割: 選択中のタブを返すゲッター。
- 触るとき: 現在のタブの保持場所を調べるとき。
- 参照: `this.#selectedTab`

## Tabbrowser.selectedBrowser()
- 位置: L678-680
- 役割: 選択中の browser を返すゲッター。
- 触るとき: 現在の browser の保持場所を調べるとき。
- 参照: `this.#selectedBrowser`

## Tabbrowser.selectedBrowsers()
- 位置: L682-687
- 役割: 分割ビュー表示中はその browser 群、それ以外は選択中の browser 1 つを配列で返す。
- 触るとき: 画面に表示中の browser 全てを扱う処理を書くとき。
- 参照: `splitViewBrowsers.length`, `this.#selectedBrowser`, `this.splitViewBrowsers`

## Tabbrowser.#setupInitialBrowserAndTab()
- 位置: L689-875
- 役割: window.arguments や採用タブから remoteType を決め、最初の browser を作って既存の先頭タブに結び付け、進捗リスナーを接続する。
- 触るとき: 新規ウィンドウ最初のタブのプロセス選択や、タブの採用時の初期化を調べるとき。
- 呼び出し先: `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`, `Tabbrowser.#generateUniquePanelID()`, `Tabbrowser.#tabFilters.set()`, `Tabbrowser.#tabListeners.set()`, `URILoadingWrapper.fixupAndLoadURIString.bind()`, `URILoadingWrapper.loadURI.bind()`, `browser.setAttribute()`, `browser.webProgress.addProgressListener()`, `extraOptions?.hasKey()`, `filter.addProgressListener()`, `lazy.AIWindow.isAIWindowActive()`, `tabArgument.hasAttribute()`, `this.#tabForBrowser.set()`, `this.#updateUserContextUIIndicator()`, `this.appendStatusPanel()`, `this.createBrowser()`, `this.documentGlobal.docShell.treeOwner .QueryInterface()`, `this.documentGlobal.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `this.documentGlobal.gBrowserInit.getTabToAdopt()`, `this.getPanel()`, `this.shouldActivateDocShell()`, `this.tabpanels.appendChild()`
- 条件付き依存: `if (extraOptions?.hasKey("triggeringRemoteType"))` → `extraOptions.getPropertyAsACString()`
- 条件付き依存: `if (tabArgument && tabArgument.hasAttribute("usercontextid"))` → `parseInt()`
- 条件付き依存: `if (tabArgument && tabArgument.hasAttribute("usercontextid"))` → `tabArgument.getAttribute()`
- 条件付き依存: `if (openWindowInfo.isRemote)` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (!(openWindowInfo))` → `Array.isArray()`
- 条件付き依存: `if (uriToLoad && typeof uriToLoad == "string")` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (Cu.isInAutomation)` → `ChromeUtils.releaseAssert()`
- 条件付き依存: `if (this.documentGlobal.gBrowserAllowScriptsToCloseInitialTabs)` → `browser.setAttribute()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActive(this.documentGlobal))` → `Array.isArray()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `browser.toggleAttribute()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `lazy.AIWindow.isAIWindowContentPage()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `Services.io.newURI()`
- 条件付き依存: `if (userContextId)` → `tab.setAttribute()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.setTabStyle()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `Ci.nsIPropertyBag2`, `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_ALL`, `Cu.isInAutomation`, `browser.docShellIsActive`, `browser.droppedLinkHandler`, `browser.fixupAndLoadURIString`, `browser.loadURI`, `lazy.E10SUtils.NOT_REMOTE`, `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `lazy.allowTransparentBrowser`, `openWindowInfo.isRemote`, `openWindowInfo.originAttributes.userContextId`, `panel.id`, `remoteTypeOptions.preferredRemoteType`, `tab._index`, `tab.initializing`, `tab.linkedBrowser`, `tab.linkedPanel`, `tabArgument.linkedBrowser`, `tabArgument.linkedBrowser.browsingContext?.group.id`, `tabArgument.linkedBrowser.remoteType`, `this.#defaultDropLinkHandler`, `this.#selectedBrowser`, `this.#selectedTab`, `this.documentGlobal`, `this.documentGlobal.arguments`, `this.documentGlobal.gBrowserAllowScriptsToCloseInitialTabs`, `this.documentGlobal.gBrowserInit.uriToLoadPromise`, `this.tabs`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1` / `Services.io`

## Tabbrowser.#updateUserContextUIIndicator()
- 位置: L877-931
- 役割: 選択中 browser のコンテナ (userContext) に合わせて、コンテナの表示アイコンとラベルを更新または隠す。
- 触るとき: コンテナ表示の更新タイミングや見た目を変えるとき。
- 呼び出し先: `hbox.setAttribute()`, `lazy.ContextualIdentityService.getPublicIdentityFromId()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `replaceContainerClass()`, `this.document.getElementById()`, `this.selectedBrowser.getAttribute()`
- 条件付き依存: `if (!userContextId)` → `this.document.getElementById()`
- 条件付き依存: `if (!userContextId)` → `replaceContainerClass()`
- 条件付き依存: `if (!identity)` → `replaceContainerClass()`
- 参照: `creationPanel.state`, `hbox.hidden`, `identity.color`, `identity.icon`, `this.document.getElementById("userContext-label").textContent`

## replaceContainerClass()
- 位置: L878-891
- 役割: identity-種別- で始まるクラスを外し、指定値のクラスを付け直すローカル関数。
- 触るとき: コンテナ表示の色やアイコンのクラス名の扱いを調べるとき。
- 呼び出し先: `className.startsWith()`, `element.classList.contains()`
- 条件付き依存: `if (className.startsWith(prefix))` → `element.classList.remove()`
- 条件付き依存: `if (value)` → `element.classList.add()`
- 参照: `element.classList`

## Tabbrowser.canGoBack()
- 位置: L939-941
- 役割: 選択タブが戻れるかを返す、browser への転送。
- 触るとき: 戻るの可否の判定元を調べるとき。
- 参照: `this.selectedBrowser.canGoBack`

## Tabbrowser.canGoBackIgnoringUserInteraction()
- 位置: L947-949
- 役割: ユーザー操作の有無を無視した戻れるかの判定を、選択 browser から返す。
- 触るとき: 戻る履歴の判定でユーザー操作の扱いを調べるとき。
- 参照: `this.selectedBrowser.canGoBackIgnoringUserInteraction`

## Tabbrowser.canGoForward()
- 位置: L954-956
- 役割: 選択タブが進めるかを返す、browser への転送。
- 触るとき: 進むの可否の判定元を調べるとき。
- 参照: `this.selectedBrowser.canGoForward`

## Tabbrowser.goBack()
- 位置: L965-967
- 役割: 選択 browser の goBack を呼ぶ転送。
- 触るとき: 戻る操作の経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.goBack()`

## Tabbrowser.goForward()
- 位置: L976-978
- 役割: 選択 browser の goForward を呼ぶ転送。
- 触るとき: 進む操作の経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.goForward()`

## Tabbrowser.reload()
- 位置: L984-986
- 役割: 選択 browser だけを reload する転送。複数選択は無視する。
- 触るとき: 単一タブのリロード経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.reload()`

## Tabbrowser.reloadWithFlags()
- 位置: L988-1073
- 役割: 選択中の各タブについて、リモート性が変わるなら URL を再読み込みし、変わらなければ一時権限をリセットしてフラグ付きでリロードする。
- 触るとき: 強制リロードや複数選択のリロード、リロード時の権限リセットを変えるとき。
- 呼び出し先: `lazy.ReducedProtectionNotification.markUserReload()`, `lazy.SitePermissions.clearTemporaryBlockPermissions()`, `reloadBrowser()`, `this.documentGlobal.gIdentityHandler.hidePopup()`, `this.documentGlobal.gPermissionPanel.hidePopup()`, `this.updateBrowserRemotenessByURL()`
- 条件付き依存: `if (tab.linkedPanel)` → `loadBrowserURI()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tab.addEventListener()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `loadBrowserURI()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `this.#insertBrowser()`
- 条件付き依存: `if (!(this.updateBrowserRemotenessByURL(browser, urlSpec)))` → `unchangedRemoteness.push()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_USER_ACTIVATION`, `browser.currentURI`, `tab.linkedBrowser`, `tab.linkedBrowser.authPromptAbuseCounter`, `tab.linkedBrowser.contentPrincipal`, `tab.linkedPanel`, `this.document.hasValidTransientUserGestureActivation`, `this.selectedTabs`, `unchangedRemoteness.length`, `url.spec`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md)

## reloadBrowser()
- 位置: L1044-1065
- 役割: セッション履歴または browsingContext でリロードし、未ロードのタブは browser を挿入して復元後に実行するローカル関数。
- 触るとき: 未ロードタブのリロードの遅延実行を調べるとき。
- 条件付き依存: `if (sessionHistory)` → `sessionHistory.reload()`
- 条件付き依存: `if (!(sessionHistory))` → `browsingContext.reload()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tab.addEventListener()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tab.linkedBrowser.browsingContext.reload()`
- 条件付き依存: `if (!(tab.linkedPanel))` → `tabbrowser.#insertBrowser()`
- 参照: `tab.linkedBrowser`, `tab.linkedPanel`

## loadBrowserURI()
- 位置: L1067-1072
- 役割: 指定の URL を、保存した principal とリロードフラグで browser に読み込むローカル関数。
- 触るとき: リモート性が変わった後の再読み込みを調べるとき。
- 呼び出し先: `browser.loadURI()`

## Tabbrowser.stop()
- 位置: L1078-1080
- 役割: 選択 browser の stop を呼ぶ転送。
- 触るとき: 読み込み停止の経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.stop()`

## Tabbrowser.loadURI()
- 位置: L1088-1090
- 役割: 選択 browser の loadURI を呼ぶ転送。
- 触るとき: 選択タブへの nsIURI 読み込みの経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.loadURI()`

## Tabbrowser.fixupAndLoadURIString()
- 位置: L1097-1099
- 役割: 選択 browser の fixupAndLoadURIString を呼ぶ転送。
- 触るとき: 選択タブへの文字列 URL 読み込みの経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.fixupAndLoadURIString()`

## Tabbrowser.gotoIndex()
- 位置: L1107-1109
- 役割: 選択 browser のセッション履歴の指定位置へ移動する転送。
- 触るとき: 履歴の特定エントリへ移る経路を調べるとき。
- 呼び出し先: `this.selectedBrowser.gotoIndex()`

## Tabbrowser.currentURI()
- 位置: L1114-1116
- 役割: 選択 browser の currentURI を返す転送。
- 触るとき: 現在のページの URI の取得元を調べるとき。
- 参照: `this.selectedBrowser.currentURI`

## Tabbrowser.finder()
- 位置: L1121-1123
- 役割: 選択 browser の finder を返す転送。
- 触るとき: ページ内検索の実行体の取得元を調べるとき。
- 参照: `this.selectedBrowser.finder`

## Tabbrowser.docShell()
- 位置: L1129-1131
- 役割: 選択 browser の docShell を返す転送。
- 触るとき: 選択タブの docShell への参照を調べるとき。
- 参照: `this.selectedBrowser.docShell`

## Tabbrowser.webNavigation()
- 位置: L1136-1138
- 役割: 選択 browser の webNavigation を返す転送。
- 触るとき: 選択タブのナビゲーション API の取得元を調べるとき。
- 参照: `this.selectedBrowser.webNavigation`

## Tabbrowser.webProgress()
- 位置: L1143-1145
- 役割: 選択 browser の webProgress を返す転送。
- 触るとき: 選択タブの進捗オブジェクトの取得元を調べるとき。
- 参照: `this.selectedBrowser.webProgress`

## Tabbrowser.contentWindow()
- 位置: L1151-1153
- 役割: 選択 browser の contentWindow を返す転送。
- 触るとき: 選択タブのコンテンツ window の取得元を調べるとき。
- 参照: `this.selectedBrowser.contentWindow`

## Tabbrowser.sessionHistory()
- 位置: L1158-1160
- 役割: 選択 browser の sessionHistory を返す転送。
- 触るとき: 選択タブの履歴オブジェクトの取得元を調べるとき。
- 参照: `this.selectedBrowser.sessionHistory`

## Tabbrowser.contentDocument()
- 位置: L1166-1168
- 役割: 選択 browser の contentDocument を返す転送。
- 触るとき: 選択タブのコンテンツ document の取得元を調べるとき。
- 参照: `this.selectedBrowser.contentDocument`

## Tabbrowser.contentTitle()
- 位置: L1173-1175
- 役割: 選択 browser の contentTitle を返す転送。
- 触るとき: 選択タブのページタイトルの取得元を調べるとき。
- 参照: `this.selectedBrowser.contentTitle`

## Tabbrowser.contentPrincipal()
- 位置: L1180-1182
- 役割: 選択 browser の contentPrincipal を返す転送。
- 触るとき: 選択タブのページの principal の取得元を調べるとき。
- 参照: `this.selectedBrowser.contentPrincipal`

## Tabbrowser.securityUI()
- 位置: L1187-1189
- 役割: 選択 browser の securityUI を返す転送。
- 触るとき: 選択タブのセキュリティ状態の取得元を調べるとき。
- 参照: `this.selectedBrowser.securityUI`

## Tabbrowser.fullZoom()
- 位置: L1194-1196
- 役割: 選択 browser の fullZoom を設定する転送。
- 触るとき: 選択タブのズーム率の設定経路を調べるとき。
- 参照: `this.selectedBrowser.fullZoom`

## Tabbrowser.fullZoom()
- 位置: L1198-1200
- 役割: 選択 browser の fullZoom を返す転送。
- 触るとき: 選択タブのズーム率の取得元を調べるとき。
- 参照: `this.selectedBrowser.fullZoom`

## Tabbrowser.textZoom()
- 位置: L1205-1207
- 役割: 選択 browser の textZoom を設定する転送。
- 触るとき: 選択タブの文字サイズ倍率の設定経路を調べるとき。
- 参照: `this.selectedBrowser.textZoom`

## Tabbrowser.textZoom()
- 位置: L1209-1211
- 役割: 選択 browser の textZoom を返す転送。
- 触るとき: 選択タブの文字サイズ倍率の取得元を調べるとき。
- 参照: `this.selectedBrowser.textZoom`

## Tabbrowser.isSyntheticDocument()
- 位置: L1217-1219
- 役割: 選択 browser の isSyntheticDocument を返す転送。
- 触るとき: 画像やメディア単体の表示ページかの判定元を調べるとき。
- 参照: `this.selectedBrowser.isSyntheticDocument`

## Tabbrowser.userTypedValue()
- 位置: L1226-1228
- 役割: 選択 browser の userTypedValue を設定する転送。
- 触るとき: アドレスバーの入力途中の値の設定経路を調べるとき。
- 参照: `this.selectedBrowser.userTypedValue`

## Tabbrowser.userTypedValue()
- 位置: L1230-1232
- 役割: 選択 browser の userTypedValue を返す転送。
- 触るとき: アドレスバーの入力途中の値の取得元を調べるとき。
- 参照: `this.selectedBrowser.userTypedValue`

## Tabbrowser.#setFindbarData()
- 位置: L1234-1253
- 役割: 検索バーのショートカットキーを、未設定なら Services.ppmm の sharedData に登録する。
- 触るとき: コンテンツ側が知る検索ショートカットの決まり方を変えるとき。
- 呼び出し先: `sharedData.has()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `this.document.getElementById()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `keyEl .getAttribute("modifiers") .replace()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `keyEl .getAttribute()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `sharedData.set()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `keyEl.getAttribute()`
- 条件付き依存: `if (!sharedData.has("Findbar:Shortcut"))` → `mods.includes()`
- 参照: `AppConstants.platform`, `Services.ppmm`
- XPCOM: `Services.ppmm`

## Tabbrowser.isFindBarInitialized()
- 位置: L1263-1265
- 役割: そのタブの検索バーがすでに作られているかを、作成せずに返す。
- 触るとき: 検索バーを不用意に生成せず存在確認したいとき。
- 呼び出し先: `Tabbrowser.#findBars.has()`
- 参照: `this.selectedTab`

## Tabbrowser.getCachedFindBar()
- 位置: L1274-1276
- 役割: 作成済みなら検索バーを同期的に返し、未作成なら undefined を返す。
- 触るとき: 検索バーを生成せずに参照したいとき。
- 呼び出し先: `Tabbrowser.#findBars.get()`
- 参照: `this.selectedTab`

## Tabbrowser.clearLastFindValue()
- 位置: L1281-1283
- 役割: 新規検索バーに初期入力する直近の検索語を消す。
- 触るとき: 検索語の引き継ぎをリセットする処理を調べるとき。
- 参照: `this.#lastFindValue`

## Tabbrowser.getFindBar()
- 位置: async L1292-1305
- 役割: タブの検索バーを返し、未作成なら作成する。作成中の Promise を共有して再入を防ぐ。
- 触るとき: 検索バーの遅延生成や、重複作成の防止を調べるとき。
- 呼び出し先: `Tabbrowser.#pendingFindBars.get()`, `this.getCachedFindBar()`
- 条件付き依存: `if (!pendingFindBar)` → `this.#createFindBar()`
- 条件付き依存: `if (!pendingFindBar)` → `Tabbrowser.#pendingFindBars.set()`
- 参照: `this.selectedTab`

## Tabbrowser.#createFindBar()
- 位置: async L1313-1335
- 役割: findbar 要素を browser の直後に挿入し、次フレーム後に browser と直近の検索語を設定して TabFindInitialized を送る。
- 触るとき: 検索バーの生成手順や初期状態を変えるとき。
- 呼び出し先: `Tabbrowser.#findBars.set()`, `Tabbrowser.#pendingFindBars.delete()`, `aTab.dispatchEvent()`, `browser.parentNode.insertAdjacentElement()`, `event.initEvent()`, `this.document.createEvent()`, `this.document.createXULElement()`, `this.documentGlobal.requestAnimationFrame()`, `this.getBrowserForTab()`
- 参照: `aTab.closing`, `findBar._findField.value`, `findBar.browser`, `this.#lastFindValue`, `this.documentGlobal.closed`

## Tabbrowser.appendStatusPanel()
- 位置: L1337-1342
- 役割: ステータスパネルを指定 browser (既定は選択中) の直後に移す。
- 触るとき: ステータスパネルの配置位置を調べるとき。
- 呼び出し先: `browser.insertAdjacentElement()`
- 参照: `this.documentGlobal.StatusPanel.panel`, `this.selectedBrowser`

## Tabbrowser.#updateTabBarForPinnedTabs()
- 位置: L1344-1348
- 役割: ピン留めの増減後に、タブ幅のロック解除、選択の再処理、閉じるボタンの更新を行う。
- 触るとき: ピン留め後のタブバーの再計算を調べるとき。
- 呼び出し先: `this.tabContainer._handleTabSelect()`, `this.tabContainer._unlockTabSizing()`, `this.tabContainer._updateCloseButtons()`

## Tabbrowser.#notifyPinnedStatus()
- 位置: L1350-1376
- 役割: browsingContext の isAppTab を更新し、PIN/UNPIN を記録して TabPinned/TabUnpinned を送る。
- 触るとき: ピン留め状態の通知やテレメトリを変えるとき。
- 呼び出し先: `aTab.dispatchEvent()`, `this.recordTabMetrics()`
- 参照: `aTab.linkedBrowser.browsingContext`, `aTab.linkedBrowser.browsingContext.isAppTab`, `aTab.pinned`, `this.TabMetrics.METRIC_ACTION.PIN`, `this.TabMetrics.METRIC_ACTION.UNPIN`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this.documentGlobal.CustomEvent`

## Tabbrowser.pinTab()
- 位置: L1388-1405
- 役割: タブを表示して pinned コンテナへ移し、ピン属性の設定、タブバー更新、通知を行う。
- 触るとき: ピン留めの処理や、ピン留め不可の条件を変えるとき。
- 呼び出し先: `aTab.setAttribute()`, `this.#handleTabMove()`, `this.#notifyPinnedStatus()`, `this.#updateTabBarForPinnedTabs()`, `this.document.getElementById()`, `this.pinnedTabsContainer.insertBefore()`, `this.showTab()`
- 参照: `aTab.pinned`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this.documentGlobal.FirefoxViewHandler.tab`

## Tabbrowser.unpinTab()
- 位置: L1417-1433
- 役割: タブのピン属性を外して通常のタブ列の先頭へ移し、タブバー更新と通知を行う。
- 触るとき: ピン解除時の配置や処理を変えるとき。
- 呼び出し先: `aTab.removeAttribute()`, `this.#handleTabMove()`, `this.#notifyPinnedStatus()`, `this.#updateTabBarForPinnedTabs()`, `this.tabContainer.arrowScrollbox.prepend()`
- 参照: `aTab.pinned`, `aTab.style.marginInlineStart`, `this.TabMetrics.UNKNOWN_CONTEXT`

## Tabbrowser.previewTab()
- 位置: L1435-1446
- 役割: プレビューモードで一時的にタブを選択してコールバックを実行し、元のタブに戻す。
- 触るとき: タブを実際には切り替えずに一時選択する処理を調べるとき。
- 呼び出し先: `aCallback()`
- 参照: `this.#previewMode`, `this.selectedTab`

## Tabbrowser.getBrowserAtIndex()
- 位置: L1448-1450
- 役割: browsers の指定位置の browser を返す。
- 触るとき: 添字から browser を引く経路を調べるとき。
- 参照: `this.browsers`

## Tabbrowser.getBrowserForOuterWindowID()
- 位置: L1452-1460
- 役割: outerWindowID が一致する browser を全 browser から探して返し、無ければ null を返す。
- 触るとき: ウィンドウ ID から対応するタブの browser を引く処理を調べるとき。
- 参照: `b.outerWindowID`, `this.browsers`

## Tabbrowser.getTabForBrowser()
- 位置: L1462-1464
- 役割: browser から対応するタブを引く。
- 触るとき: browser とタブの対応づけの取得元を調べるとき。
- 呼び出し先: `this.#tabForBrowser.get()`

## Tabbrowser.getPanel()
- 位置: L1466-1468
- 役割: browser を含むタブパネル要素を返す。
- 触るとき: browser の外側の DOM 構造を調べるとき。
- 呼び出し先: `this.getBrowserContainer()`
- 参照: `this.getBrowserContainer(aBrowser).parentNode`

## Tabbrowser.getBrowserContainer()
- 位置: L1470-1472
- 役割: browser の 2 階層上の browserContainer 要素を返す。引数省略時は選択中の browser。
- 触るとき: browser を包む容器要素の取得を調べるとき。
- 参照: `(aBrowser || this.selectedBrowser).parentNode.parentNode`, `this.selectedBrowser`

## Tabbrowser.getTabNotificationDeck()
- 位置: L1475-1486
- 役割: タブ通知用の deck 要素を、テンプレートから初回のみ展開して返す。
- 触るとき: 通知ボックスの置き場の遅延生成を調べるとき。
- 条件付き依存: `if (!this.#tabNotificationDeck)` → `this.document.getElementById()`
- 条件付き依存: `if (!this.#tabNotificationDeck)` → `template.replaceWith()`
- 参照: `template.content`, `this.#tabNotificationDeck`

## Tabbrowser.getNotificationBox()
- 位置: L1489-1503
- 役割: browser ごとの NotificationBox を遅延作成して返し、作成時に挿入先を決める。
- 触るとき: タブ単位の通知バーの生成を変えるとき。
- 条件付き依存: `if (!browser._notificationBox)` → `element.setAttribute()`
- 条件付き依存: `if (!browser._notificationBox)` → `this.#insertNotificationBox()`
- 参照: `browser._notificationBox`, `lazy.notificationEnableDelay`, `this.#nextNotificationBoxId`, `this.documentGlobal.MozElements.NotificationBox`, `this.selectedBrowser`

## Tabbrowser.#insertNotificationBox()
- 位置: L1517-1533
- 役割: 分割ビュー内なら該当パネルの先頭に、そうでなければ共有の通知 deck に通知ボックスを入れる。
- 触るとき: 分割ビュー時の通知バーの置き場を調べるとき。
- 呼び出し先: `this.#isBrowserInActiveSplitView()`, `this.getTabNotificationDeck()`, `this.getTabNotificationDeck().append()`
- 条件付き依存: `if (this.#isBrowserInActiveSplitView(browser))` → `this.getBrowserContainer()`
- 条件付き依存: `if (this.#isBrowserInActiveSplitView(browser))` → `browserContainer.prepend()`
- 条件付き依存: `if (browser == this.selectedBrowser)` → `this.#updateVisibleNotificationBox()`
- 参照: `box.parentNode`, `this.selectedBrowser`

## Tabbrowser.#isBrowserInActiveSplitView()
- 位置: L1535-1538
- 役割: browser がアクティブな分割ビューに属するかを返す。
- 触るとき: 分割ビュー所属の判定を調べるとき。
- 呼び出し先: `this.getTabForBrowser()`
- 参照: `tab?.splitview`, `this.#activeSplitView`

## Tabbrowser.readNotificationBox()
- 位置: L1540-1543
- 役割: 作成済みの通知ボックスを返す。未作成なら作らず null を返す。
- 触るとき: 通知ボックスを生成せずに参照したいとき。
- 参照: `browser._notificationBox`, `this.selectedBrowser`

## Tabbrowser.#updateVisibleNotificationBox()
- 位置: L1545-1561
- 役割: 通知 deck の表示対象を、指定 browser の通知ボックスに切り替える。
- 触るとき: タブ切り替え時に表示される通知バーの選択を調べるとき。
- 呼び出し先: `notificationBox.stack.getAttribute()`, `this.getTabNotificationDeck()`, `this.readNotificationBox()`
- 参照: `notificationBox._stack.parentNode`, `notificationBox?._stack`, `this.#tabNotificationDeck`, `this.getTabNotificationDeck().selectedViewName`

## Tabbrowser.getTabDialogBox()
- 位置: L1563-1573
- 役割: browser の TabDialogBox を遅延作成して返す。引数が無いと例外。
- 触るとき: タブ単位のダイアログ管理の生成を調べるとき。
- 参照: `aBrowser.documentGlobal.TabDialogBox`, `aBrowser.tabDialogBox`

## Tabbrowser.getTabFromAudioEvent()
- 位置: L1575-1583
- 役割: 信頼されたイベントの originalTarget の browser からタブを返し、非信頼なら null を返す。
- 触るとき: 音声関連イベントからタブを特定する処理を調べるとき。
- 呼び出し先: `this.getTabForBrowser()`
- 参照: `aEvent.isTrusted`, `aEvent.originalTarget`

## Tabbrowser._callProgressListeners()
- 位置: L1585-1622
- 役割: 選択 browser なら全体用、常にタブ全体用の進捗リスナーへ、メソッドを例外を握りつぶしつつ呼び分ける。
- 触るとき: 進捗通知がどのリスナーへどの順で届くかを調べるとき。
- 条件付き依存: `if (aCallGlobalListeners && aBrowser == this.selectedBrowser)` → `callListeners()`
- 条件付き依存: `if (aCallTabsListeners)` → `aArguments.unshift()`
- 条件付き依存: `if (aCallTabsListeners)` → `callListeners()`
- 参照: `this.#progressListeners`, `this.#tabsProgressListeners`, `this.selectedBrowser`

## callListeners()
- 位置: L1594-1607
- 役割: リスナー配列に対し指定メソッドを呼び、falsy の戻りを集約するローカル関数。
- 触るとき: リスナーの例外や戻り値の扱いを調べるとき。
- 条件付き依存: `if (aMethod in p)` → `p[aMethod].apply()`
- 条件付き依存: `if (aMethod in p)` → `console.error()`

## Tabbrowser.setDefaultIcon()
- 位置: L1630-1634
- 役割: URI が FAVICON_DEFAULTS にあれば、そのアイコンをタブに設定する。
- 触るとき: 内部ページの既定ファビコンを足すとき。
- 条件付き依存: `if (aURI && aURI.spec in FAVICON_DEFAULTS)` → `this.setIcon()`
- 参照: `aURI.spec`

## Tabbrowser.setIcon()
- 位置: L1636-1686
- 役割: ローカルスキームのアイコン URL のみ受け付け、browser とタブの image 属性を更新して onLinkIconAvailable を通知する。
- 触るとき: タブのアイコン設定の検証や更新を変えるとき。
- 呼び出し先: `LOCAL_PROTOCOLS.some()`, `aIconURL.startsWith()`, `aTab.getAttribute()`, `makeString()`, `this._callProgressListeners()`, `this.getBrowserForTab()`
- 条件付き依存: `if ( aIconURL && !LOCAL_PROTOCOLS.some(protocol => aIconURL.startsWith(protocol)) )` → `console.error()`
- 条件付き依存: `if (aClearImageFirst)` → `aTab.removeAttribute()`
- 条件付き依存: `if (aIconURL)` → `url.startsWith()`
- 条件付き依存: `if ( lazy.remoteSVGIconDecoding && url.startsWith(lazy.FaviconUtils.SVG_DATA_URI_PREFIX) )` → `this.#getMozRemoteImageURLForSvg()`
- 条件付き依存: `if (aIconURL)` → `aTab.setAttribute()`
- 条件付き依存: `if (!(aIconURL))` → `aTab.removeAttribute()`
- 条件付き依存: `if (aIconURL != aTab.getAttribute("image"))` → `this._tabAttrModified()`
- 参照: `browser.mIconURL`, `lazy.FaviconUtils.SVG_DATA_URI_PREFIX`, `lazy.remoteSVGIconDecoding`

## makeString()
- 位置: L1642-1642
- 役割: nsIURI なら spec を、それ以外はそのまま返すローカル関数。
- 触るとき: アイコン URL の型の扱いを調べるとき。
- 参照: `Ci.nsIURI`, `url.spec`
- XPCOM: [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md)

## Tabbrowser.#maybeRefreshIcons()
- 位置: L1689-1709
- 役割: リモート SVG デコード有効時、配色変更に合わせて SVG データ URI のタブアイコンを作り直す。
- 触るとき: ダーク/ライト切替時のファビコン更新を調べるとき。
- 呼び出し先: `iconURL.startsWith()`, `tab.setAttribute()`, `this.#getMozRemoteImageURLForSvg()`, `this.getBrowserForTab()`
- 参照: `browser.mIconURL`, `lazy.FaviconUtils.SVG_DATA_URI_PREFIX`, `lazy.remoteSVGIconDecoding`, `this.tabs`

## Tabbrowser.#getMozRemoteImageURLForSvg()
- 位置: L1711-1730
- 役割: SVG アイコンを指定サイズと配色、可能なら content process 指定で描画する moz-remote-image の URL を作る。
- 触るとき: SVG ファビコンのリモート描画の指定を変えるとき。
- 呼び出し先: `Math.floor()`, `lazy.FaviconUtils.getMozRemoteImageURL()`, `this.documentGlobal.matchMedia()`
- 参照: `browser.browsingContext?.currentWindowGlobal?.contentParentId`, `options.contentParentId`, `this.documentGlobal.devicePixelRatio`, `this.documentGlobal.matchMedia( "(prefers-color-scheme: dark)" ).matches`

## Tabbrowser.getIcon()
- 位置: L1732-1735
- 役割: 指定タブ (省略時は選択中) の browser に保存されたアイコン URL を返す。
- 触るとき: タブのアイコン URL の取得元を調べるとき。
- 呼び出し先: `this.getBrowserForTab()`
- 参照: `browser.mIconURL`, `this.selectedBrowser`

## Tabbrowser.setPageInfo()
- 位置: L1737-1749
- 役割: URL があれば Places の履歴に説明とプレビュー画像を更新し、タブの description を設定する。
- 触るとき: ページ情報の履歴への保存を調べるとき。
- 条件付き依存: `if (aURL)` → `lazy.PlacesUtils.history.update(pageInfo).catch()`
- 条件付き依存: `if (aURL)` → `lazy.PlacesUtils.history.update()`
- 参照: `console.error`, `tab.description`

## Tabbrowser.#populateTitleCache()
- 位置: L1752-1762
- 役割: ウィンドウタイトル用の文言 3 種を DOM から読み取りキャッシュする。
- 触るとき: ウィンドウタイトルの文言の取得元を調べるとき。
- 呼び出し先: `this.document.getElementById()`
- 参照: `this.#cachedTitleInfo`, `this.document.getElementById(id)?.textContent`

## Tabbrowser.#determineTaskbarTabTitle()
- 位置: L1802-1852
- 役割: タスクバータブ名、コンテナ名、プロファイル名からタイトルの一部を作り、不要なら null を返す。
- 触るとき: タスクバータブのウィンドウタイトルの組み立てを変えるとき。
- 呼び出し先: `lazy.ContextualIdentityService.getUserContextLabel()`, `lazy.TaskbarTabsUtils.getTaskbarTabIdFromWindow()`, `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (!this.#taskbarTab)` → `lazy.TaskbarTabs.getTaskbarTab(id) .then(tt => { this.#taskbarTab = tt; this.updateTitlebar(); }) .catch()`
- 条件付き依存: `if (!this.#taskbarTab)` → `lazy.TaskbarTabs.getTaskbarTab(id) .then()`
- 条件付き依存: `if (!this.#taskbarTab)` → `lazy.TaskbarTabs.getTaskbarTab()`
- 条件付き依存: `if (!this.#taskbarTab)` → `this.updateTitlebar()`
- 参照: `lazy.shouldExposeContentTitle`, `this.#taskbarTab`, `this.#taskbarTab.name`, `this.#taskbarTab.userContextId`, `this.#taskbarTabTitle`, `this.#taskbarTabTitleLastProfile`, `this.documentGlobal`

## Tabbrowser.#determineContentTitle()
- 位置: L1854-1904
- 役割: 設定に応じて、ポップアップ系ウィンドウの接頭辞や titlepreface とタブのコンテンツタイトルを連結して返す。
- 触るとき: ウィンドウタイトルへのコンテンツタイトルの露出条件を変えるとき。
- 呼び出し先: `docElement.hasAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getTabForBrowser()`
- 条件付き依存: `if ( docElement.hasAttribute("web-extension-popup-window") || docElement.hasAttribute("chromeless-window") )` → `Services.io.createExposableURI()`
- 条件付き依存: `if (uri.scheme == "moz-extension")` → `WebExtensionPolicy.getByHostname()`
- 条件付き依存: `if (ext && ext.name)` → `this.document.getElementById()`
- 条件付き依存: `if (docElement.hasAttribute("titlepreface"))` → `docElement.getAttribute()`
- 条件付き依存: `if (tab.labelIsContentTitle)` → `tab.getAttribute("label").replace()`
- 条件付き依存: `if (tab.labelIsContentTitle)` → `tab.getAttribute()`
- 参照: `browser.currentURI`, `ext.name`, `extensionLabel.value`, `lazy.shouldExposeContentTitle`, `lazy.shouldExposeContentTitlePbm`, `tab.labelIsContentTitle`, `this.document.documentElement`, `this.documentGlobal`, `uri.host`, `uri.prePath`, `uri.scheme`, `uri.spec`
- XPCOM: `Services.io`

## Tabbrowser.getWindowTitleForBrowser()
- 位置: L1906-1950
- 役割: コンテンツ名、タスクバー/プロファイル名、ブランド名などを組み合わせたウィンドウタイトルを返す。
- 触るとき: ウィンドウタイトルの構成をプラットフォーム別に変えるとき。
- 呼び出し先: `docElement.getAttribute()`, `lazy.SelectableProfileService.currentProfile?.name.replace()`, `lazy.SelectableProfileService.getCachedProfileCount()`, `parts.filter()`, `parts.filter(p => !!p).join()`, `this.#determineContentTitle()`, `this.#determineTaskbarTabTitle()`
- 条件付き依存: `if (!this.#cachedTitleInfo)` → `this.#populateTitleCache()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" && contentTitle && isTemporaryPrivateWindow )` → `parts.push()`
- 条件付き依存: `if ( !taskbarTabTitle && (!contentTitle || AppConstants.platform != "macosx") )` → `parts.push()`
- 参照: `AppConstants.platform`, `lazy.SelectableProfileService?.isEnabled`, `this.#cachedTitleInfo`, `this.#cachedTitleInfo.privateWindowSuffixForContent`, `this.document.documentElement`

## Tabbrowser.updateTitlebar()
- 位置: L1952-1954
- 役割: 選択 browser 用のタイトルを document.title に設定する。
- 触るとき: タイトルバーの更新タイミングを調べるとき。
- 呼び出し先: `this.getWindowTitleForBrowser()`
- 参照: `this.document.title`, `this.selectedBrowser`

## Tabbrowser.updateCurrentBrowser()
- 位置: L1956-2210
- 役割: 選択タブが切り替わったときに、browser の入れ替え、進捗リスナーへの状態再通知、TabSelect の送出、フォーカス調整などをまとめて行う。
- 触るとき: タブ切り替え時に起きる処理全般の追跡や、切り替えの不具合調査をするとき。
- 呼び出し先: `Tabbrowser.#tabListeners.get()`, `newBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `newBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `newTab.hasAttribute()`, `newTab.setAttribute()`, `oldBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `oldBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `oldTab.removeAttribute()`, `this.#lastRelatedTabMap.get()`, `this.#updateUserContextUIIndicator()`, `this.#updateVisibleNotificationBox()`, `this._callProgressListeners()`, `this.appendStatusPanel()`, `this.documentGlobal.gPermissionPanel.updateSharingIndicator()`, `this.documentGlobal.gURLBar?.saveSelectionStateForBrowser()`, `this.getBrowserAtIndex()`, `this.getTabForBrowser()`, `this.showTab()`
- 条件付き依存: `if (!aForceUpdate)` → `Glean.browserTabswitch.update.start()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher().requestTab()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher()`
- 条件付き依存: `if (!aForceUpdate)` → `this.document.commandDispatcher.lock()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `oldBrowser.removeAttribute()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `newBrowser.setAttribute()`
- 条件付き依存: `if (oldBrowserPopupsBlocked != newBrowserPopupsBlocked)` → `newBrowser.popupAndRedirectBlocker.sendObserverUpdateBlockedPopupsEvent()`
- 条件付き依存: `if (oldBrowserRedirectBlocked != newBrowserRedirectBlocked)` → `newBrowser.popupAndRedirectBlocker.sendObserverUpdateBlockedRedirectEvent()`
- 条件付き依存: `if (securityUI)` → `this._callProgressListeners()`
- 条件付き依存: `if (securityUI)` → `newBrowser.getContentBlockingEvents()`
- 条件付き依存: `if (listener && listener._stateFlags)` → `this._callProgressListeners()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.recordTimeFromUnloadToReload()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.updateLastAccessed()`
- 条件付き依存: `if (!this.#previewMode)` → `oldTab.updateLastAccessed()`
- 条件付き依存: `if (!this.#previewMode)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (this.documentGlobal == lazy.BrowserWindowTracker.getTopWindow())` → `newTab.updateLastSeenActive()`
- 条件付き依存: `if (this.documentGlobal == lazy.BrowserWindowTracker.getTopWindow())` → `oldTab.updateLastSeenActive()`
- 条件付き依存: `if (!this.#previewMode)` → `Tabbrowser.#findBars.get()`
- 条件付き依存: `if (!this.#previewMode)` → `this.updateTitlebar()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.removeAttribute()`
- 条件付き依存: `if (!this.#previewMode)` → `newBrowser.unselectedTabHover()`
- 条件付き依存: `if (newTab.hasAttribute("busy") && !this._isBusy)` → `this._callProgressListeners()`
- 条件付き依存: `if (!newTab.hasAttribute("busy") && this._isBusy)` → `this._callProgressListeners()`
- 条件付き依存: `if (!this.#previewMode)` → `Tabbrowser.#tabsLeavingAdoptedSplitView.has()`
- 条件付き依存: `if (!this.#previewMode)` → `newTab.dispatchEvent()`
- 条件付き依存: `if (!this.#previewMode)` → `this.#checkIfShouldTriggerTabSelectMessage()`
- 条件付き依存: `if (!this.#previewMode)` → `this._tabAttrModified()`
- 条件付き依存: `if (!this.#previewMode)` → `this.#startMultiSelectChange()`
- 条件付き依存: `if (!this.#previewMode)` → `this.clearMultiSelectedTabs()`
- 条件付き依存: `if (this.#multiSelectChangeAdditions.size)` → `this.addToMultiSelectedTabs()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this._adjustFocusBeforeTabSwitch()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this._adjustFocusAfterTabSwitch()`
- 条件付き依存: `if (aForceUpdate || !this.documentGlobal.gMultiProcessBrowser)` → `this.documentGlobal.gURLBar.afterTabSwitchFocusChange()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this.document.commandDispatcher.unlock()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this.dispatchEvent()`
- 条件付き依存: `if (!aForceUpdate)` → `Glean.browserTabswitch.update.stopAndAccumulate()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_START`, `Ci.nsIWebProgressListener.STATE_STOP`, `lastRelatedTab.owner`, `lastRelatedTab.selected`, `listener._message`, `listener._stateFlags`, `listener._status`, `listener._totalProgress`, `newBrowser.currentURI`, `newBrowser.docShellIsActive`, `newBrowser.securityUI`, `newBrowser.webProgress`, `newTab.attention`, `oldBrowser.docShellIsActive`, `oldFindBar.FIND_NORMAL`, `oldFindBar._findField.value`, `oldFindBar.findMode`, `oldFindBar.hidden`, `oldTab.owner`, `oldTab.selected`, `securityUI.state`, `this.#asyncTabSwitching`, `this.#lastFindValue`, `this.#lastRelatedTabMap`, `this.#multiSelectChangeAdditions.size`, `this.#multiSelectChangeSelected`, `this.#previewMode`, `this.#selectedBrowser`, `this.#selectedTab`, `this._isBusy`, `this.document.hidden`, `this.documentGlobal`, `this.documentGlobal.CustomEvent`, `this.documentGlobal.gMultiProcessBrowser`, `this.selectedBrowser`, `this.selectedTab`, `this.tabContainer.selectedIndex`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## Tabbrowser.#checkIfShouldTriggerTabSelectMessage()
- 位置: async L2219-2269
- 役割: 1 分以内に同じ 2 タブ間を 3 回切り替えたら ASRouter に tabSwitch トリガーを送る。
- 触るとき: タブ切り替えの反復を検知するメッセージ条件を変えるとき。
- 呼び出し先: `Date.now()`, `[oldTab, newTab].some()`, `[oldTabSpec, newTabSpec].sort()`, `this.#tabSelectTimestamps.filter()`, `this.#tabSelectTimestamps.find()`
- 条件付き依存: `if (existingEntry.count === LIMIT_FOR_TRIGGER)` → `lazy.ASRouter.sendTriggerMessage()`
- 条件付き依存: `if (existingEntry.count === LIMIT_FOR_TRIGGER)` → `this.#tabSelectTimestamps.filter()`
- 条件付き依存: `if (!(existingEntry))` → `this.#tabSelectTimestamps.push()`
- 参照: `entry.timestamp`, `entry.uris`, `existingEntry.count`, `existingEntry.timestamp`, `lazy.ASRouter.waitForInitialized`, `newTab.linkedBrowser`, `newTab.linkedBrowser.currentURI.spec`, `oldTab.linkedBrowser.currentURI.spec`, `tab.linkedBrowser.currentURI.scheme`, `this.#tabSelectTimestamps`, `this.visibleTabs.length`

## Tabbrowser._adjustFocusBeforeTabSwitch()
- 位置: L2271-2314
- 役割: 切り替え前に、アドレスバーや検索バーのフォーカス状態を旧タブ側に保存し、フォーカスを新タブへ移す。
- 触るとき: タブ切り替え前のフォーカスの保存処理を調べるとき。
- 呼び出し先: `this.documentGlobal.gURLBar.getBrowserState()`, `this.isFindBarInitialized()`
- 条件付き依存: `if (this.isFindBarInitialized(oldTab))` → `this.getCachedFindBar()`
- 条件付き依存: `if (this.isFindBarInitialized(oldTab))` → `findBar._findField.getAttribute()`
- 条件付き依存: `if (activeEl == oldTab)` → `newTab.focus()`
- 条件付き依存: `if ( this.documentGlobal.gMultiProcessBrowser && activeEl != newBrowser && activeEl != newTab )` → `this.documentGlobal.gURLBar.getBrowserState()`
- 条件付き依存: `if (!keepFocusOnUrlBar)` → `this.document.activeElement.blur()`
- 参照: `findBar.hidden`, `newBrowser._userTypedValueAtBeforeTabSwitch`, `newBrowser.userTypedValue`, `newTab.linkedBrowser`, `oldTab._findBarFocused`, `oldTab.linkedBrowser`, `this.#asyncTabSwitching`, `this.#previewMode`, `this.document.activeElement`, `this.documentGlobal.gMultiProcessBrowser`, `this.documentGlobal.gURLBar.focused`, `this.documentGlobal.gURLBar.getBrowserState(newBrowser).urlbarFocused`, `this.documentGlobal.gURLBar.getBrowserState(oldBrowser).urlbarFocused`

## Tabbrowser._adjustFocusAfterTabSwitch()
- 位置: L2316-2447
- 役割: 切り替え後に、保存状態に従ってアドレスバー、検索バー、タブダイアログ、コンテンツのいずれかへフォーカスを戻す。
- 触るとき: タブ切り替え後のフォーカス先を変えるとき。
- 呼び出し先: `fm.setFocus()`, `newBrowser.hasAttribute()`, `this.documentGlobal.gURLBar.getBrowserState()`, `this.getBrowserForTab()`
- 条件付き依存: `if (newBrowser.hasAttribute("tabDialogShowing"))` → `newBrowser.tabDialogBox.focus()`
- 条件付き依存: `if (this.documentGlobal.gURLBar.getBrowserState(newBrowser).urlbarFocused)` → `this.document.documentElement.hasAttribute()`
- 条件付き依存: `if (this.document.documentElement.hasAttribute("inDOMFullscreen"))` → `this.documentGlobal.addEventListener()`
- 条件付き依存: `if (!this.documentGlobal.fullScreen || newTab.isEmpty)` → `selectURL()`
- 条件付き依存: `if ( this.documentGlobal.gFindBarInitialized && !this.documentGlobal.gFindBar.hidden && this.selectedTab._findBarFocused )` → `this.documentGlobal.gFindBar._findField.focus()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `fm.getFocusedElementForWindow()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `HTMLAnchorElement.isInstance()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `newFocusedElement.getAttributeNS()`
- 参照: `Services.focus`, `fm.FLAG_NOSCROLL`, `fm.FLAG_SHOWRING`, `newTab.isEmpty`, `this.document.activeElement`, `this.document.body`, `this.documentGlobal.content`, `this.documentGlobal.fullScreen`, `this.documentGlobal.gFindBar.hidden`, `this.documentGlobal.gFindBarInitialized`, `this.documentGlobal.gMultiProcessBrowser`, `this.documentGlobal.gURLBar.getBrowserState(newBrowser).urlbarFocused`, `this.selectedTab._findBarFocused`
- XPCOM: `Services.focus`

## selectURL()
- 位置: L2332-2378
- 役割: アドレスバーの選択状態を復元するローカル関数。非同期切り替え中は SetURI の後に行う。
- 触るとき: タブ切り替え時のアドレスバー選択の復元を調べるとき。
- 条件付き依存: `if (this.#asyncTabSwitching)` → `this.documentGlobal.gURLBar.inputField.addEventListener()`
- 条件付き依存: `if (this.#asyncTabSwitching)` → `this.documentGlobal.gURLBar.restoreSelectionStateForBrowser()`
- 条件付き依存: `if (!(this.#asyncTabSwitching))` → `this.documentGlobal.gURLBar.restoreSelectionStateForBrowser()`
- 参照: `newBrowser._awaitingSetURI`, `newBrowser._userTypedValueAtBeforeTabSwitch`, `newBrowser.userTypedValue`, `this.#asyncTabSwitching`, `this.document.activeElement`

## Tabbrowser._tabAttrModified()
- 位置: L2449-2462
- 役割: 閉じ中でないタブに、変更属性名つきの TabAttrModified を送る。
- 触るとき: タブ属性変更の通知経路を調べるとき。
- 呼び出し先: `aTab.dispatchEvent()`
- 参照: `aTab.closing`, `this.documentGlobal.CustomEvent`

## Tabbrowser.resetBrowserSharing()
- 位置: L2464-2478
- 役割: browser の共有状態を初期化 (WebRTC は猶予追跡用に枠を残す) し、sharing 属性を外して通知する。
- 触るとき: 画面/カメラ共有状態のリセットを調べるとき。
- 呼び出し先: `tab.removeAttribute()`, `this._tabAttrModified()`, `this.getTabForBrowser()`
- 条件付き依存: `if (aBrowser == this.selectedBrowser)` → `this.documentGlobal.gPermissionPanel.updateSharingIndicator()`
- 参照: `aBrowser._sharingState`, `aBrowser._sharingState?.webRTC`, `this.selectedBrowser`

## Tabbrowser.updateBrowserSharing()
- 位置: L2480-2507
- 役割: 共有状態を browser に反映し、WebRTC 状況に合わせてタブの sharing 属性を更新して通知する。
- 触るとき: 共有中のタブ表示の更新を変えるとき。
- 呼び出し先: `Object.assign()`, `this.getTabForBrowser()`
- 条件付き依存: `if (aBrowser._sharingState.webRTC.paused)` → `tab.removeAttribute()`
- 条件付き依存: `if (!(aBrowser._sharingState.webRTC.paused))` → `tab.setAttribute()`
- 条件付き依存: `if (!(aBrowser._sharingState.webRTC?.sharing))` → `tab.removeAttribute()`
- 条件付き依存: `if ("webRTC" in aState)` → `this._tabAttrModified()`
- 条件付き依存: `if (aBrowser == this.selectedBrowser)` → `this.documentGlobal.gPermissionPanel.updateSharingIndicator()`
- 参照: `aBrowser._sharingState`, `aBrowser._sharingState.webRTC.paused`, `aBrowser._sharingState.webRTC?.sharing`, `aState.webRTC.sharing`, `this.selectedBrowser`

## Tabbrowser.getTabSharingState()
- 位置: L2509-2521
- 役割: タブの WebRTC 共有状態を camera/microphone/screen の形に整えて返す静的メソッド。
- 触るとき: 拡張機能などが参照する共有状態の形を調べるとき。
- 呼び出し先: `Object.assign()`, `state.screen.replace()`
- 参照: `aTab.linkedBrowser`, `browser._sharingState`, `browser._sharingState.webRTC`, `state.camera`, `state.microphone`, `state.screen`

## Tabbrowser.setInitialTabTitle()
- 位置: L2543-2564
- 役割: 読み込み前の暫定ラベルを設定する。空白ページの URL は空タブ用タイトルに置換する。
- 触るとき: セッション復元や新規タブの初期ラベルの付け方を変えるとき。
- 呼び出し先: `this.documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (aTitle)` → `aTab.getAttribute()`
- 条件付き依存: `if (!aTab.getAttribute("label"))` → `Tabbrowser.#tabsWithInitialTitle.add()`
- 条件付き依存: `if (aTitle)` → `this.#setTabLabel()`
- 参照: `this.tabContainer.emptyTabTitle`

## Tabbrowser.setTabTitle()
- 位置: L2586-2650
- 役割: コンテンツのタイトルを整え、無ければ URI や空タブ用タイトルで代替し、#setTabLabel で反映する。
- 触るとき: タブのタイトルの決め方や代替表示を変えるとき。
- 呼び出し先: `Tabbrowser.#nonPrintingRegEx.test()`, `Tabbrowser.#tabsWithInitialTitle.has()`, `aTab.hasAttribute()`, `this.#setTabLabel()`, `this.getBrowserForTab()`, `title.trim()`
- 条件付き依存: `if (aTab.hasAttribute("customizemode"))` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (Tabbrowser.#tabsWithInitialTitle.has(aTab))` → `Tabbrowser.#tabsWithInitialTitle.delete()`
- 条件付き依存: `if (browser.currentURI.displaySpec)` → `Services.io.createExposableURI()`
- 条件付き依存: `if (!title)` → `this.documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (title && !this.documentGlobal.isBlankPageURL(title))` → `Tabbrowser.#dataURLRegEx.test()`
- 条件付き依存: `if (title.length <= 500 || !Tabbrowser.#dataURLRegEx.test(title))` → `Services.textToSubURI.unEscapeNonAsciiURI()`
- 参照: `Services.io.createExposableURI( browser.currentURI ).displaySpec`, `browser.characterSet`, `browser.contentTitle`, `browser.currentURI`, `browser.currentURI.displaySpec`, `this.tabContainer.emptyTabTitle`, `title.length`
- XPCOM: `Services.io` / `Services.textToSubURI`

## Tabbrowser.setTabLabelForAuthPrompts()
- 位置: L2656-2658
- 役割: 認証プロンプト用に、タブのラベルを指定値で設定する。
- 触るとき: 認証ダイアログ中のタブ表示の偽装対策を調べるとき。
- 呼び出し先: `this.#setTabLabel()`

## Tabbrowser.#setTabLabel()
- 位置: L2680-2736
- 役割: ラベルを短縮と長さ制限して label 属性に設定し、文字方向を更新、必要なら通知とタイトルバー更新を行う。
- 触るとき: タブのラベル表示の加工や長さ制限を変えるとき。
- 呼び出し先: `/^about:reader\?url=/.test()`, `Tabbrowser.#dataURLRegEx.test()`, `Tabbrowser.#fullLabels.set()`, `aTab.getAttribute()`, `aTab.setAttribute()`, `aTab.toggleAttribute()`, `dwu.getDirectionFromText()`
- 条件付き依存: `if (isURL && aLabel.length > 500 && Tabbrowser.#dataURLRegEx.test(aLabel))` → `aLabel.substring()`
- 条件付き依存: `if (!isContentTitle)` → `aLabel.replace()`
- 条件付き依存: `if (aLabel.length > TAB_LABEL_MAX_LENGTH)` → `aLabel.substring()`
- 条件付き依存: `if (!beforeTabOpen)` → `this._tabAttrModified()`
- 条件付き依存: `if (aTab.selected)` → `this.updateTitlebar()`
- 参照: `Ci.nsIDOMWindowUtils.DIRECTION_RTL`, `Tabbrowser.#shortenURLRegEx`, `aLabel.length`, `aTab.labelIsContentTitle`, `aTab.selected`, `this.document.dir`, `this.documentGlobal.windowUtils`
- XPCOM: [`nsIDOMWindowUtils`](../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md)

## Tabbrowser.loadTabs()
- 位置: L2780-2929
- 役割: 複数 URL を新規タブまたは既存タブで読み込み、開いたタブを URL の順に返す。
- 触るとき: 複数 URL を一括で開く挙動や、置き換え読み込みの条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `tabs.push()`, `this.addTab()`
- 条件付き依存: `if (typeof elementIndex == "number")` → `this.#elementIndexToTabIndex()`
- 条件付き依存: `if (replace)` → `Tabbrowser.isTabGroupLabel()`
- 条件付き依存: `if (targetTab)` → `this.getBrowserForTab()`
- 条件付き依存: `if (replace)` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if (replace)` → `tabs.push()`
- 条件付き依存: `if (!(replace))` → `this.addTab()`
- 条件付き依存: `if (!(replace))` → `tabs.push()`
- 参照: `aURIs.length`, `browser.initiatedFromNonWebControlled`, `firstTabAdded.index`, `params.tabIndex`, `targetTab.index`, `this.selectedBrowser`, `this.selectedTab`, `this.selectedTab.index`, `this.tabContainer.selectedIndex`
- XPCOM: `Services.prefs`

## Tabbrowser.updateBrowserRemoteness()
- 位置: L2945-3088
- 役割: browser の frameloader を別の remoteType に差し替え、進捗リスナーを付け替えて TabRemotenessChange を送る。
- 触るとき: プロセスの切り替え (リモート性の変更) 時の処理を調べるとき。
- 呼び出し先: `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Tabbrowser.#tabListeners.set()`, `aBrowser.changeRemoteness()`, `aBrowser.construct()`, `aBrowser.destroy()`, `aBrowser.didStartLoadSinceLastUserTyping()`, `aBrowser.getContentBlockingEvents()`, `aBrowser.hasAttribute()`, `aBrowser.webProgress.addProgressListener()`, `evt.initEvent()`, `filter.addProgressListener()`, `listener?.destroy()`, `tab.dispatchEvent()`, `this.#insertBrowser()`, `this._callProgressListeners()`, `this.document.createEvent()`, `this.getTabForBrowser()`, `this.isFindBarInitialized()`
- 条件付き依存: `if (filter)` → `aBrowser.webProgress.removeProgressListener()`
- 条件付き依存: `if (filter)` → `filter.removeProgressListener()`
- 条件付き依存: `if (shouldBeRemote)` → `aBrowser.setAttribute()`
- 条件付き依存: `if (!(shouldBeRemote))` → `aBrowser.removeAttribute()`
- 条件付き依存: `if (hadStartedLoad)` → `aBrowser.urlbarChangeTracker.startedLoad()`
- 条件付き依存: `if (!filter)` → `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`
- 条件付き依存: `if (!filter)` → `Tabbrowser.#tabFilters.set()`
- 条件付き依存: `if (shouldBeRemote)` → `tab.removeAttribute()`
- 条件付き依存: `if (this.isFindBarInitialized(tab))` → `this.getCachedFindBar()`
- 参照: `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_ALL`, `Ci.nsIWebProgressListener.STATE_IS_INSECURE`, `aBrowser.remoteType`, `aBrowser.securityUI`, `aBrowser.userTypedValue`, `aBrowser.webProgress`, `lazy.E10SUtils.NOT_REMOTE`, `securityUI.state`, `this.documentGlobal.gMultiProcessBrowser`, `this.getCachedFindBar(tab).browser`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1`

## Tabbrowser.updateBrowserRemotenessByURL()
- 位置: L3107-3129
- 役割: URL から予測した remoteType に browser が合わなければ updateBrowserRemoteness で切り替える。
- 触るとき: URL に応じたプロセス切り替えの判定を調べるとき。
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `this.getTabForBrowser()`
- 条件付き依存: `if (!this.documentGlobal.gMultiProcessBrowser)` → `this.updateBrowserRemoteness()`
- 条件付き依存: `if (oldRemoteType != options.remoteType || options.newFrameloader)` → `this.updateBrowserRemoteness()`
- 参照: `aBrowser.remoteType`, `lazy.E10SUtils.NOT_REMOTE`, `options.newFrameloader`, `options.remoteType`, `this.documentGlobal`, `this.documentGlobal.gMultiProcessBrowser`, `this.getTabForBrowser(aBrowser).userContextId`

## Tabbrowser.createBrowser()
- 位置: L3156-3270
- 役割: browser 要素に既定属性と remoteType などを設定して作成し、stack と容器要素に収める。
- 触るとき: browser 要素の生成時の属性や構造を変えるとき。
- 呼び出し先: `Cu.getGlobalForObject()`, `Services.obs.notifyObservers()`, `b.setAttribute()`, `browserContainer.appendChild()`, `browserSidebarContainer.appendChild()`, `lazy.AIWindow.isAIWindowActive()`, `stack.appendChild()`, `this.document.createXULElement()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser || remoteType)` → `b.setAttribute()`
- 条件付き依存: `if (userContextId)` → `b.setAttribute()`
- 条件付き依存: `if (remoteType)` → `b.setAttribute()`
- 条件付き依存: `if (!isPreloadBrowser)` → `b.setAttribute()`
- 条件付き依存: `if (isPreloadBrowser)` → `b.setAttribute()`
- 条件付き依存: `if (initialBrowsingContextGroupId)` → `b.setAttribute()`
- 条件付き依存: `if (name)` → `b.setAttribute()`
- 条件付き依存: `if ( lazy.AIWindow.isAIWindowActive(this.documentGlobal) || lazy.allowTransparentBrowser )` → `b.setAttribute()`
- 条件付き依存: `if (!uriIsAboutBlank || skipLoad)` → `b.setAttribute()`
- 参照: `Cu.getGlobalForObject(Services).Object`, `b.openWindowInfo`, `b.permanentKey`, `browserContainer.className`, `browserSidebarContainer.className`, `lazy.allowTransparentBrowser`, `stack.className`, `this.documentGlobal`, `this.documentGlobal.gMultiProcessBrowser`
- XPCOM: `Services.obs`

## Tabbrowser.#createLazyBrowser()
- 位置: L3272-3372
- 役割: 未挿入の browser に、一部プロパティは SessionStore などから返し、他は触れた時点で挿入する代替プロパティを定義する。
- 触るとき: 遅延 (lazy) ブラウザの振る舞いや、意図しない挿入の調査をするとき。
- 呼び出し先: `Object.defineProperty()`
- 参照: `Tabbrowser.#browserBindingProperties`, `aTab.linkedBrowser`, `names.length`

## getter()
- 位置: L3283-3283
- 役割: audioMuted を、タブの muted 属性から返す。
- 触るとき: 遅延ブラウザのミュート状態の返し方を調べるとき。
- 呼び出し先: `aTab.hasAttribute()`

## getter()
- 位置: L3286-3286
- 役割: contentTitle を、SessionStore の保存値から返す。
- 触るとき: 遅延ブラウザのタイトルの返し方を調べるとき。
- 呼び出し先: `lazy.SessionStore.getLazyTabValue()`

## getter()
- 位置: L3289-3297
- 役割: currentURI を、SessionStore の URL から作った nsIURI で返し、結果をキャッシュする。
- 触るとき: 遅延ブラウザの URI の返し方を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `lazy.SessionStore.getLazyTabValue()`
- 参照: `browser._cachedCurrentURI`
- XPCOM: `Services.io`

## getter()
- 位置: L3300-3300
- 役割: didStartLoadSinceLastUserTyping を、常に false を返す関数として返す。
- 触るとき: 遅延ブラウザでの入力後ロード判定を調べるとき。

## getter()
- 位置: L3304-3304
- 役割: fullZoom/textZoom を常に 1 として返す。
- 触るとき: 遅延ブラウザのズーム値の扱いを調べるとき。

## getter()
- 位置: L3307-3307
- 役割: tabHasCustomZoom を常に false として返す。
- 触るとき: 遅延ブラウザのズーム状態の扱いを調べるとき。

## getter()
- 位置: L3310-3310
- 役割: getTabBrowser を、this を返す関数として返す。
- 触るとき: 遅延ブラウザからの tabbrowser 取得を調べるとき。

## getter()
- 位置: L3313-3313
- 役割: isRemoteBrowser を、remote 属性の有無から返す。
- 触るとき: 遅延ブラウザのリモート判定を調べるとき。
- 呼び出し先: `browser.hasAttribute()`

## getter()
- 位置: L3316-3316
- 役割: permitUnload を、常に許可を返す関数として返す。
- 触るとき: 遅延ブラウザの unload 確認の扱いを調べるとき。

## getter()
- 位置: L3320-3331
- 役割: reload/reloadWithFlags を、SSTabRestoring 後に実行するよう予約し browser を挿入する関数として返す。
- 触るとき: 遅延ブラウザでリロードされたときの挙動を調べるとき。
- 呼び出し先: `aTab.addEventListener()`, `browser[name]()`, `this.#insertBrowser()`

## getter()
- 位置: L3334-3341
- 役割: remoteType を、SessionStore の URL から予測して返す。
- 触るとき: 遅延ブラウザの remoteType の決め方を調べるとき。
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `aTab.getAttribute()`, `lazy.SessionStore.getLazyTabValue()`
- 参照: `this.documentGlobal`

## getter()
- 位置: L3345-3345
- 役割: userTypedValue/userTypedClear を SessionStore の保存値から返す。
- 触るとき: 遅延ブラウザの入力途中の値の扱いを調べるとき。
- 呼び出し先: `lazy.SessionStore.getLazyTabValue()`

## getter()
- 位置: L3348-3355
- 役割: その他のプロパティの参照時に browser を挿入し、実際の値を返す (Nightly ではログを出す)。
- 触るとき: 遅延ブラウザが意図せず挿入される原因を調べるとき。
- 呼び出し先: `this.#insertBrowser()`
- 条件付き依存: `if (AppConstants.NIGHTLY_BUILD)` → `Services.console.logStringMessage()`
- 参照: `AppConstants.NIGHTLY_BUILD`, `new Error().stack`
- XPCOM: `Services.console`

## setter()
- 位置: L3356-3363
- 役割: その他のプロパティへの代入時に browser を挿入し、実際の browser に値を設定する。
- 触るとき: 遅延ブラウザが代入で挿入される原因を調べるとき。
- 呼び出し先: `this.#insertBrowser()`
- 条件付き依存: `if (AppConstants.NIGHTLY_BUILD)` → `Services.console.logStringMessage()`
- 参照: `AppConstants.NIGHTLY_BUILD`, `new Error().stack`
- XPCOM: `Services.console`

## Tabbrowser.insertBrowser()
- 位置: L3381-3383
- 役割: #insertBrowser を呼ぶ公開ラッパー。遅延タブに実際の browser を与える。
- 触るとき: 外部から遅延タブを読み込み可能にする経路を調べるとき。
- 呼び出し先: `this.#insertBrowser()`

## Tabbrowser.#insertBrowser()
- 位置: L3385-3493
- 役割: 遅延タブのパネルを DOM に挿入し、進捗リスナーとロード用の関数を設定して TabBrowserInserted を送る。
- 触るとき: 遅延タブがいつ実体化されるか、その初期化を調べるとき。
- 呼び出し先: `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`, `Tabbrowser.#browserParams.delete()`, `Tabbrowser.#browserParams.get()`, `Tabbrowser.#generateUniquePanelID()`, `Tabbrowser.#tabFilters.set()`, `Tabbrowser.#tabListeners.set()`, `URILoadingWrapper.fixupAndLoadURIString.bind()`, `URILoadingWrapper.loadURI.bind()`, `browser.webProgress.addProgressListener()`, `filter.addProgressListener()`, `this.getPanel()`
- 条件付き依存: `if (!panel.parentNode)` → `this.tabpanels.appendChild()`
- 条件付き依存: `if (aTab.userContextId)` → `browser.setAttribute()`
- 条件付き依存: `if (aTab.selected)` → `this.#updateUserContextUIIndicator()`
- 条件付き依存: `if (aTab.isConnected)` → `aTab.dispatchEvent()`
- 参照: `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_ALL`, `Tabbrowser.#browserBindingProperties`, `aTab.isConnected`, `aTab.linkedBrowser`, `aTab.linkedBrowser.browsingContext.hasSiblings`, `aTab.linkedPanel`, `aTab.pinned`, `aTab.selected`, `aTab.userContextId`, `browser._cachedCurrentURI`, `browser.browsingContext.isAppTab`, `browser.docShellIsActive`, `browser.droppedLinkHandler`, `browser.fixupAndLoadURIString`, `browser.loadURI`, `panel.id`, `panel.parentNode`, `this.#defaultDropLinkHandler`, `this.documentGlobal.CustomEvent`, `this.documentGlobal.closed`, `this.tabs`, `this.tabs.length`, `this.tabs[0].linkedBrowser.browsingContext.hasSiblings`, `this.tabs[1].linkedBrowser.browsingContext.hasSiblings`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1`

## Tabbrowser.#mayDiscardBrowser()
- 位置: L3495-3521
- 役割: 選択中や閉じ中、非リモート、unload 拒否のタブは破棄不可とし、強制でなければダイアログ表示中も不可とする。
- 触るとき: タブの破棄 (アンロード) ができる条件を変えるとき。
- 呼び出し先: `browser.permitUnload()`, `this.getTabDialogBox()`
- 参照: `aTab.closing`, `aTab.linkedBrowser`, `aTab.selected`, `browser.isConnected`, `browser.isRemoteBrowser`, `browser.permitUnload(action).permitUnload`, `this.#windowIsClosing`, `this.getTabDialogBox(browser)._tabDialogManager._dialogs.length`

## Tabbrowser.prepareDiscardBrowser()
- 位置: async L3523-3535
- 役割: 破棄の対象になりうるタブの状態を TabStateFlusher で書き出す。閉じ中やウィンドウ終了中は何もしない。
- 触るとき: アンロード前のセッション状態の保存を調べるとき。
- 呼び出し先: `lazy.TabStateFlusher.flush()`
- 参照: `aTab.closing`, `aTab.linkedBrowser`, `browser.isRemoteBrowser`, `this.#windowIsClosing`

## Tabbrowser.discardBrowser()
- 位置: L3537-3619
- 役割: タブの browser を破棄して遅延状態に戻し、リスナーや検索バーを片付けて TabBrowserDiscarded を送る。
- 触るとき: メモリ解放のためのタブ破棄の処理や後始末を変えるとき。
- 呼び出し先: `Tabbrowser.#browserParams.set()`, `Tabbrowser.#findBars.get()`, `Tabbrowser.#tabFilters.delete()`, `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.delete()`, `Tabbrowser.#tabListeners.get()`, `aTab.dispatchEvent()`, `aTab.hasAttribute()`, `aTab.removeAttribute()`, `browser.destroy()`, `browser.webProgress.removeProgressListener()`, `filter.removeProgressListener()`, `lazy.SessionStore.resetBrowserToLazyState()`, `lazy.webrtcUI.forgetStreamsFromBrowserContext()`, `listener.destroy()`, `tabDialogBox.abortAllDialogs()`, `this.#createLazyBrowser()`, `this.#mayDiscardBrowser()`, `this._switcher?.onTabDiscarded()`, `this.getPanel()`, `this.getPanel(browser).remove()`, `this.getTabDialogBox()`, `this.resetBrowserSharing()`
- 条件付き依存: `if (aForceDiscard)` → `aTab.toggleAttribute()`
- 条件付き依存: `if (findBar)` → `findBar.close()`
- 条件付き依存: `if (findBar)` → `findBar.remove()`
- 条件付き依存: `if (findBar)` → `Tabbrowser.#findBars.delete()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `removedAttributes.push()`
- 条件付き依存: `if (aTab.hasAttribute(attr))` → `aTab.removeAttribute()`
- 条件付き依存: `if (removedAttributes.length)` → `this._tabAttrModified()`
- 参照: `aTab.linkedBrowser`, `browser.browsingContext`, `browser.currentURI.spec`, `browser.remoteType`, `removedAttributes.length`, `this.documentGlobal.CustomEvent`

## Tabbrowser.addWebTab()
- 位置: L3628-3641
- 役割: triggeringPrincipal が無ければ null principal を設定して addTab を呼ぶ。system principal は拒否する。
- 触るとき: Web コンテンツ由来のタブを開く経路や principal の扱いを調べるとき。
- 呼び出し先: `this.addTab()`
- 条件付き依存: `if (!params.triggeringPrincipal)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 参照: `params.triggeringPrincipal`, `params.triggeringPrincipal.isSystemPrincipal`, `params.userContextId`
- XPCOM: `Services.scriptSecurityManager`

## Tabbrowser.addAdjacentNewTab()
- 位置: L3649-3667
- 役割: 指定タブの直後に新規タブ URL のタブを開いて選択し、browser-open-newtab-start を通知する。
- 触るとき: タブの右に新規タブを開く操作を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `resolve()`, `this.addTrustedTab()`
- 参照: `tab.group`, `tab.index`, `tab.userContextId`, `this.documentGlobal.BROWSER_NEW_TAB_URL`, `this.selectedBrowser`, `this.selectedTab`
- XPCOM: `Services.obs`

## Tabbrowser.addAdjacentTab()
- 位置: L3677-3690
- 役割: 指定タブの直後 (グループ外指定時はグループの後) の位置を計算して addTab を呼ぶ。
- 触るとき: 隣に新しいタブを開く位置の決め方を調べるとき。
- 呼び出し先: `adjacentTab.group.tabs.at()`, `this.addTab()`
- 参照: `adjacentTab.group`, `adjacentTab.group.tabs.at(-1).index`, `adjacentTab.index`, `options.tabGroup`

## Tabbrowser.addTrustedTab()
- 位置: L3701-3705
- 役割: triggeringPrincipal を system principal にして addTab を呼ぶ。
- 触るとき: chrome 由来のタブを開く経路を調べるとき。
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `this.addTab()`
- 参照: `options.triggeringPrincipal`
- XPCOM: `Services.scriptSecurityManager`

## Tabbrowser.addTab()
- 位置: L3824-4105
- 役割: タブと browser を作って位置を決めて挿入し、TabOpen の送出、読み込み開始、アニメーションと選択までを行う。
- 触るとき: 新しいタブを開く処理全般や、そのオプション、位置、読み込みの不具合を調べるとき。
- 呼び出し先: `UserInteraction.running()`, `console.error()`, `t?.remove()`, `this.#createBrowserForTab()`, `this.#createTab()`, `this.#determineURIToLoad()`, `this.documentGlobal.gSharedTabWarning.tabAdded()`, `this.getTabForBrowser()`, `this.tabContainer.markTabOpening()`
- 条件付き依存: `if (!UserInteraction.running("browser.tabs.opening", this.documentGlobal))` → `UserInteraction.start()`
- 条件付き依存: `if (insertTab)` → `this.#insertTabAtIndex()`
- 条件付き依存: `if (focusUrlBar)` → `this.documentGlobal.gURLBar.getBrowserState()`
- 条件付き依存: `if (createLazyBrowser)` → `this.#createLazyBrowser()`
- 条件付き依存: `if (lazyBrowserURI)` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`
- 条件付き依存: `if (lazyBrowserURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (insertTab)` → `lazy.SessionStore.setTabState()`
- 条件付き依存: `if (insertTab)` → `lazy.E10SUtils.serializePrincipal()`
- 条件付き依存: `if (!(createLazyBrowser))` → `this.#insertBrowser()`
- 条件付き依存: `if (t?.linkedBrowser)` → `Tabbrowser.#tabFilters.delete()`
- 条件付き依存: `if (t?.linkedBrowser)` → `Tabbrowser.#tabListeners.delete()`
- 条件付き依存: `if (t?.linkedBrowser)` → `this.getPanel(t.linkedBrowser).remove()`
- 条件付き依存: `if (t?.linkedBrowser)` → `this.getPanel()`
- 条件付き依存: `if (insertTab)` → `this.#fireTabOpen()`
- 条件付き依存: `if (insertTab)` → `this.#kickOffBrowserLoad()`
- 条件付き依存: `if (usingPreloadedContent)` → `this.documentGlobal.requestAnimationFrame()`
- 条件付き依存: `if (usingPreloadedContent)` → `t.setAttribute()`
- 条件付き依存: `if (!(usingPreloadedContent))` → `this.documentGlobal.requestAnimationFrame()`
- 条件付き依存: `if (!(usingPreloadedContent))` → `t.setAttribute()`
- 条件付き依存: `if (pinned)` → `this.#notifyPinnedStatus()`
- 参照: `b.browsingContext.crossGroupOpener`, `b.registeredOpenURI`, `lazyBrowserURI.spec`, `lazyBrowserURI?.spec`, `openWindowInfo?.hasValidUserGestureActivation`, `openWindowInfo?.textDirectiveUserActivation`, `openerBrowser.browsingContext`, `openerBrowser?.browsingContext`, `openerTab?.group`, `referrerInfo.originalReferrer`, `t.linkedBrowser`, `t.userContextId`, `t?.linkedBrowser`, `tabGroup?.id`, `this.documentGlobal`, `this.documentGlobal.gReduceMotion`, `this.documentGlobal.gURLBar.getBrowserState(b).urlbarFocused`, `this.selectedTab`, `this.selectedTab.owner`, `this.tabContainer.overflowing`, `this.tabContainer.verticalMode`

## Tabbrowser.#elementIndexToTabIndex()
- 位置: L4107-4122
- 役割: ドラッグ&ドロップ要素の添字を、tabs 配列の添字に変換する。
- 触るとき: グループ/分割ビューを含む位置指定から実タブの位置を出す処理を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `Tabbrowser.isTabGroupLabel()`
- 参照: `element.group.tabs`, `element.index`, `element.tabs`, `this.tabContainer.dragAndDropElements`, `this.tabContainer.dragAndDropElements.length`, `this.tabs.length`

## Tabbrowser.#createTabSplitView()
- 位置: L4128-4140
- 役割: 分割ビューのラッパー要素を作り、指定または採番した ID を設定する。
- 触るとき: 分割ビュー要素の生成と ID 付与を調べるとき。
- 呼び出し先: `this.document.createXULElement()`
- 条件付き依存: `if (!id)` → `lazy.SessionStore.getNextSplitViewId()`
- 参照: `splitview.splitViewId`

## Tabbrowser.addTabSplitView()
- 位置: L4160-4223
- 役割: 指定タブを含む分割ビューを作って挿入し、空なら破棄、作成時に Glean を記録して SplitViewCreated を送る。
- 触るとき: 分割ビューの作成処理やテレメトリを変えるとき。
- 呼び出し先: `splitview.addTabs()`, `this.#createTabSplitView()`, `this.tabContainer.dispatchEvent()`, `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!splitview.tabs.length)` → `splitview.remove()`
- 条件付き依存: `if (trigger && tabGroupInfo)` → `Glean.splitview.start.record()`
- 参照: `insertBefore?.splitview`, `splitview.tabs.length`, `tabs.length`, `tabs?.length`, `tabs[0]?.group`, `tabs[1]?.group`, `this.documentGlobal.CustomEvent`, `this.tabContainer.verticalMode`

## Tabbrowser.showSplitViewPanels()
- 位置: L4230-4243
- 役割: 分割ビューの各タブの browser を挿入し、フッターを付けて docShell を有効にし、パネルを表示対象に設定する。
- 触るとき: 分割ビュー表示時のパネルの有効化を調べるとき。
- 呼び出し先: `panelEl?.classList.toggle()`, `this.#insertBrowser()`, `this.#insertSplitViewFooter()`, `this.document.getElementById()`
- 条件付き依存: `if (tab.linkedBrowser)` → `panels.push()`
- 参照: `tab.linkedBrowser`, `tab.linkedBrowser.docShellIsActive`, `tab.linkedPanel`, `this.tabpanels.splitViewPanels`

## Tabbrowser.#insertSplitViewFooter()
- 位置: L4250-4260
- 役割: タブのパネルに分割ビュー用フッターが無ければ追加する。
- 触るとき: 分割ビューのフッター表示を調べるとき。
- 呼び出し先: `panelEl?.querySelector()`, `this.document.getElementById()`
- 条件付き依存: `if (panelEl)` → `this.document.createXULElement()`
- 条件付き依存: `if (panelEl)` → `footer.setTab()`
- 条件付き依存: `if (panelEl)` → `panelEl.querySelector(".browserStack").appendChild()`
- 条件付き依存: `if (panelEl)` → `panelEl.querySelector()`
- 参照: `tab.linkedPanel`

## Tabbrowser.openSplitViewMenu()
- 位置: L4262-4269
- 役割: 起点要素に応じてトリガー元を設定し、分割ビューのメニューを開く。
- 触るとき: 分割ビューのメニュー表示とトリガー記録を調べるとき。
- 呼び出し先: `menu.openPopup()`, `menu.setAttribute()`, `this.document.getElementById()`
- 参照: `anchorElement?.localName`, `anchorElement?.parentElement?.localName`

## Tabbrowser.#createTabGroup()
- 位置: L4279-4289
- 役割: ID、色、折りたたみ、ラベルを設定した tab-group 要素を作る。
- 触るとき: タブグループ要素の生成内容を調べるとき。
- 呼び出し先: `this.document.createXULElement()`
- 参照: `group.collapsed`, `group.color`, `group.id`, `group.label`, `group.wasCreatedByAdoption`

## Tabbrowser.addTabGroup()
- 位置: L4316-4380
- 役割: タブまたは分割ビューを含むグループを作って挿入し、ユーザー操作なら TabGroupCreateByUser を送り、タブ状態を書き出す。
- 触るとき: タブグループの作成処理や、空グループの扱いを調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `Tabbrowser.isTab()`, `group.addTabs()`, `group.tabs.forEach()`, `lazy.TabStateFlusher.flush()`, `tabsAndSplitViews.some()`, `this.#createTabGroup()`, `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!id)` → `Date.now()`
- 条件付き依存: `if (!id)` → `Math.round()`
- 条件付き依存: `if (!id)` → `Math.random()`
- 条件付き依存: `if (!group.tabs.length)` → `group.remove()`
- 条件付き依存: `if (metricsContext.isUserTriggered)` → `group.dispatchEvent()`
- 参照: `group.tabs.length`, `insertBefore?.group`, `metricsContext.isUserTriggered`, `tab.linkedBrowser`, `tabsAndSplitViews?.length`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this.documentGlobal.CustomEvent`, `this.tabGroupMenu.nextUnusedColor`

## Tabbrowser.removeTabGroup()
- 位置: async L4391-4445
- 役割: unload 確認後、グループ削除の通知を送り、属するタブを removeTabs で閉じる。
- 触るとき: タブグループの削除と保存済みグループの扱いを調べるとき。
- 呼び出し先: `group.dispatchEvent()`, `this.removeTabs()`
- 条件付き依存: `if (this.tabGroupMenu.panel.state != "closed")` → `this.tabGroupMenu.panel.hidePopup()`
- 条件付き依存: `if (!options.skipPermitUnload)` → `this.runBeforeUnloadForTabs()`
- 条件付き依存: `if (cancel)` → `lazy.SessionStore.getSavedTabGroup()`
- 条件付き依存: `if (lazy.SessionStore.getSavedTabGroup(group.id))` → `lazy.SessionStore.forgetSavedTabGroup()`
- 参照: `group.id`, `group.saveOnWindowClose`, `group.tabs`, `group.tabs.length`, `options.animate`, `options.closeWindowWithLastTab`, `options.metricsContext`, `options.skipGroupCheck`, `options.skipPermitUnload`, `options.skipSessionStore`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this.documentGlobal.CustomEvent`, `this.tabGroupMenu.panel.state`, `this.tabs.length`

## Tabbrowser.ungroupTab()
- 位置: L4453-4461
- 役割: グループ内のタブをグループの直後に移して、グループから外す。
- 触るとき: グループ解除の処理を調べるとき。
- 呼び出し先: `this.#handleTabMove()`, `this.tabContainer.insertBefore()`
- 参照: `tab.group`, `tab.group.nextElementSibling`

## Tabbrowser.ungroupSplitView()
- 位置: L4463-4474
- 役割: グループ内の分割ビューをグループの直後に移して、グループから外す。
- 触るとき: 分割ビューのグループ解除を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `this.#handleTabMove()`, `this.tabContainer.insertBefore()`
- 参照: `splitView.tabs`, `splitView.tabs[0].group.nextElementSibling`

## Tabbrowser.adoptTabGroup()
- 位置: L4484-4544
- 役割: 別ウィンドウのグループの各タブ/分割ビューを採用し、同じ ID、ラベル、色のグループを作り直す。
- 触るとき: ウィンドウ間でのタブグループの移動を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `group.documentGlobal.gBrowser.nonHiddenTabs.every()`, `this.addTabGroup()`
- 条件付き依存: `if (noOtherTabsInWindow)` → `group.dispatchEvent()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(element))` → `this.adoptSplitView()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(element))` → `newTabs.push()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(element)))` → `this.adoptTab()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(element)))` → `newTabs.push()`
- 参照: `adoptedTab.index`, `group.color`, `group.documentGlobal.gBrowser.selectedTab`, `group.id`, `group.label`, `group.ownerDocument`, `group.removedByAdoption`, `group.saveOnWindowClose`, `group.tabs`, `group.tabsAndSplitViews`, `splitview.tabs`, `splitview.tabs.length`, `splitview.tabs[0].index`, `t.group`, `this.document`, `this.documentGlobal.CustomEvent`

## Tabbrowser.adoptSplitView()
- 位置: L4554-4593
- 役割: 別ウィンドウの分割ビューの各タブを採用し、同じ ID の分割ビューを作り直す。
- 触るとき: ウィンドウ間での分割ビューの移動と、TabMove の抑制フラグを調べるとき。
- 呼び出し先: `Tabbrowser.#tabsJoiningAdoptedSplitView.add()`, `Tabbrowser.#tabsJoiningAdoptedSplitView.delete()`, `Tabbrowser.#tabsLeavingAdoptedSplitView.add()`, `newTabs.push()`, `this.addTabSplitView()`, `this.adoptTab()`
- 参照: `adoptedTab.index`, `container.documentGlobal.gBrowser.selectedTab`, `container.ownerDocument`, `container.splitViewId`, `container.tabs`, `this.document`

## Tabbrowser.getAllTabGroups()
- 位置: L4603-4616
- 役割: 同じプライベート種別の全ウィンドウからタブグループを集め、必要なら最近見た順に並べる。
- 触るとき: 全ウィンドウ横断でグループを列挙する処理を調べるとき。
- 呼び出し先: `acc.concat()`, `lazy.BrowserWindowTracker.getOrderedWindows()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (sortByLastSeenActive)` → `groups.sort()`
- 参照: `group1.lastSeenActive`, `group2.lastSeenActive`, `this.documentGlobal`, `thisWindow.gBrowser.tabGroups`

## Tabbrowser.getTabGroupById()
- 位置: L4618-4629
- 役割: 同じプライベート種別の全ウィンドウから ID が一致するグループを探して返す。
- 触るとき: ID からタブグループを引く処理を調べるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getOrderedWindows()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `group.id`, `this.documentGlobal`, `win.gBrowser.tabGroups`

## Tabbrowser.#determineURIToLoad()
- 位置: L4631-4652
- 役割: URL 文字列を nsIURI にし、遅延ブラウザなら実 URI を退避して about:blank に差し替えた情報を返す。
- 触るとき: タブ作成時に読み込む URI の決め方を調べるとき。
- 呼び出し先: `Services.io.newURI()`
- XPCOM: `Services.io`

## Tabbrowser.#createTab()
- 位置: L4674-4749
- 役割: tab 要素を作り、opener、コンテナ、ピン、初期ラベルなどを設定し、アニメ無しなら新タブ処理を予約する。
- 触るとき: タブ要素の初期属性や初期ラベルの付け方を調べるとき。
- 呼び出し先: `t.classList.add()`, `this.document.createXULElement()`, `this.tabContainer._unlockTabSizing()`
- 条件付き依存: `if (!noInitialLabel)` → `this.documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (this.documentGlobal.isBlankPageURL(uriString))` → `t.setAttribute()`
- 条件付き依存: `if (!(this.documentGlobal.isBlankPageURL(uriString)))` → `this.setInitialTabTitle()`
- 条件付き依存: `if (userContextId)` → `t.setAttribute()`
- 条件付き依存: `if (userContextId)` → `lazy.ContextualIdentityService.setTabStyle()`
- 条件付き依存: `if (skipBackgroundNotify)` → `t.setAttribute()`
- 条件付き依存: `if (pinned)` → `t.setAttribute()`
- 条件付き依存: `if (!animate)` → `UserInteraction.update()`
- 条件付き依存: `if (!animate)` → `t.setAttribute()`
- 条件付き依存: `if (!animate)` → `this.documentGlobal.setTimeout()`
- 条件付き依存: `if (!animate)` → `tabContainer._handleNewTab()`
- 条件付き依存: `if (!(!animate))` → `UserInteraction.update()`
- 参照: `openerTab.userContextId`, `t.openerTab`, `this.documentGlobal`, `this.tabContainer`, `this.tabContainer.emptyTabTitle`

## Tabbrowser.#createBrowserForTab()
- 位置: L4785-4880
- 役割: remoteType を決め、プリロード済み browser があれば使い、無ければ作成してタブに結び付ける。
- 触るとき: 新規タブのプロセス選択やプリロード利用を調べるとき。
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`, `Tabbrowser.#browserParams.set()`, `this.#tabForBrowser.set()`, `this.setDefaultIcon()`
- 条件付き依存: `if ( uriIsAboutBlank && !preferredRemoteType && referrerInfo && referrerInfo.originalReferrer )` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if ( uriString == this.documentGlobal.BROWSER_NEW_TAB_URL && !userContextId )` → `lazy.NewTabPagePreloading.getPreloadedBrowser()`
- 条件付き依存: `if (!b)` → `this.createBrowser()`
- 参照: `lazy.E10SUtils.NOT_REMOTE`, `openerBrowser.remoteType`, `referrerInfo.originalReferrer`, `tab.linkedBrowser`, `this.documentGlobal`, `this.documentGlobal.BROWSER_NEW_TAB_URL`

## Tabbrowser.#kickOffBrowserLoad()
- 位置: L4937-5047
- 役割: 継承する principal の about:blank を用意し、ロードフラグを組み立てて browser に URL を読み込ませる。
- 触るとき: 新規タブの初回読み込みのフラグや principal の扱いを変えるとき。
- 条件付き依存: `if ( !usingPreloadedContent && originPrincipal && originStoragePrincipal && uriString )` → `this.documentGlobal.doGetProtocolFlags()`
- 条件付き依存: `if (shouldInheritSecurityContext)` → `browser.createAboutBlankDocumentViewer()`
- 条件付き依存: `if ( !usingPreloadedContent && (!uriIsAboutBlank || !allowInheritPrincipal) && !skipLoad )` → `this.documentGlobal.gInitialPages.includes()`
- 条件付き依存: `if ( !usingPreloadedContent && (!uriIsAboutBlank || !allowInheritPrincipal) && !skipLoad )` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if ( !usingPreloadedContent && (!uriIsAboutBlank || !allowInheritPrincipal) && !skipLoad )` → `console.error()`
- 参照: `Ci.nsIProtocolHandler`, `browser.userTypedValue`, `triggeringPrincipal.isSystemPrincipal`
- XPCOM: [`nsIProtocolHandler`](../../../netwerk/base/nsIIOService.idl.md)

## Tabbrowser.createTabsForSessionRestore()
- 位置: L5082-5316
- 役割: 復元データから、タブ、グループ、分割ビューを fragment 上で作ってまとめて挿入し、TabOpen などを送る。
- 触るとき: セッション復元時のタブ生成や挿入の順序を調べるとき。
- 呼び出し先: `event.initEvent()`, `lazy.SessionStore.isTabRestoring()`, `splitViewWorkingData.get()`, `splitViewWorkingData.set()`, `splitViewWorkingData.values()`, `tab.dispatchEvent()`, `tab.initialize()`, `tabGroupWorkingData.set()`, `tabGroupWorkingData.values()`, `tabs.push()`, `this.document.createDocumentFragment()`, `this.document.createEvent()`, `this.tabContainer._invalidateCachedTabs()`, `this.tabContainer.appendChild()`
- 条件付き依存: `if (!tabData.pinned)` → `this.unpinTab()`
- 条件付き依存: `if (!(!tabData.pinned))` → `this.pinTab()`
- 条件付き依存: `if (tabData.entries?.length)` → `Math.min()`
- 条件付き依存: `if (tabData.entries?.length)` → `Math.max()`
- 条件付き依存: `if (!tab)` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (!tab)` → `this.addTrustedTab()`
- 条件付き依存: `if (splitView)` → `splitView.tabs.push()`
- 条件付き依存: `if (splitView.tabs.length == splitView.numberOfTabs)` → `this.#createTabSplitView()`
- 条件付き依存: `if (tabData.pinned)` → `this.pinTab()`
- 条件付き依存: `if (tabData.pinned)` → `this.#fireTabOpen()`
- 条件付き依存: `if (tabData.groupId)` → `tabGroupWorkingData.get()`
- 条件付き依存: `if (!splitView)` → `tabGroup.containingTabsFragment.appendChild()`
- 条件付き依存: `if (splitView?.node)` → `tabGroup.containingTabsFragment.appendChild()`
- 条件付き依存: `if (!tabGroup.node)` → `this.#createTabGroup()`
- 条件付き依存: `if (!tabGroup.node)` → `tabsFragment.appendChild()`
- 条件付き依存: `if (tab.hidden)` → `hiddenTabs.set()`
- 条件付き依存: `if (!splitView)` → `tabsFragment.appendChild()`
- 条件付き依存: `if (splitView?.node)` → `splitView.tabs.some()`
- 条件付き依存: `if (splitView.tabs.some(t => t.hidden))` → `splitView.node.toggleAttribute()`
- 条件付き依存: `if (splitView?.node)` → `tabsFragment.appendChild()`
- 条件付き依存: `if (tabWasReused)` → `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (tabGroup.node)` → `tabGroup.node.appendChild()`
- 条件付き依存: `if (splitView.node)` → `splitView.node.addTabs()`
- 条件付き依存: `if (hiddenBy)` → `lazy.SessionStore.setCustomTabValue()`
- 条件付き依存: `if (tabToSelect)` → `this.removeTab()`
- 条件付き依存: `if (tabs.length > 1 || !tabs[0].selected)` → `this.#updateTabsAfterInsert()`
- 条件付き依存: `if (tabs.length > 1 || !tabs[0].selected)` → `this.documentGlobal.TabBarVisibility.update()`
- 条件付き依存: `if (!tab.pinned)` → `this.#fireTabOpen()`
- 条件付き依存: `if (tab.linkedPanel)` → `tab.dispatchEvent()`
- 参照: `splitView.node`, `splitView.numberOfTabs`, `splitView.tabs`, `splitView.tabs.length`, `splitView?.node`, `splitViewData.id`, `splitViewData.numberOfTabs`, `t.hidden`, `tab.hidden`, `tab.linkedPanel`, `tab.pinned`, `tab.selected`, `tabData.entries`, `tabData.entries.length`, `tabData.entries?.length`, `tabData.entries[activeIndex].url`, `tabData.extData`, `tabData.extData.hiddenBy`, `tabData.groupId`, `tabData.index`, `tabData.pinned`, `tabData.splitViewId`, `tabData.userContextId`, `tabDataList.length`, `tabGroup.containingTabsFragment`, `tabGroup.node`, `tabGroup.stateData.collapsed`, `tabGroup.stateData.color`, `tabGroup.stateData.id`, `tabGroup.stateData.name`, `tabGroupData.id`, `tabs.length`, `tabs[0].selected`, `this.documentGlobal`, `this.documentGlobal.CustomEvent`, `this.selectedTab`, `this.selectedTab.userContextId`, `this.tabContainer.verticalMode`

## Tabbrowser.moveTabsToStart()
- 位置: L5328-5339
- 役割: コンテキストタブまたは選択中の全タブを、順序を保って先頭に移す。
- 触るとき: 先頭へ移動のコンテキストメニュー操作を調べるとき。
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.moveTabToStart()`, `this.recordTabMetrics()`
- 参照: `contextTab.multiselected`, `tabs.length`, `this.TabMetrics.METRIC_ACTION.MOVE`, `this.selectedTabs`

## Tabbrowser.moveTabsToEnd()
- 位置: L5351-5361
- 役割: コンテキストタブまたは選択中の全タブを末尾に移す。
- 触るとき: 末尾へ移動のコンテキストメニュー操作を調べるとき。
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.moveTabToEnd()`, `this.recordTabMetrics()`
- 参照: `contextTab.multiselected`, `tabs.length`, `this.TabMetrics.METRIC_ACTION.MOVE`, `this.selectedTabs`

## Tabbrowser.warnAboutClosingTabs()
- 位置: L5363-5479
- 役割: 閉じる種類と数、設定に応じて確認ダイアログを出し、続行してよいかを返す。
- 触るとき: 複数タブを閉じるときの警告条件や文言を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `ps.confirmEx()`, `this.documentGlobal.focus()`, `this.documentGlobal.gDialogBox.replaceDialogIfOpen()`, `this.tabLocalization.formatValuesSync()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `this.documentGlobal.focus()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `this.tabLocalization.formatValuesSync()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL_DUPLICATES && !Services.prefs.getBoolPref(shownDupeDialogPref, false) )` → `ps.confirmEx()`
- 条件付き依存: `if ( aCloseTabs == Tabbrowser.closingTabsEnum.ALL && reallyClose && !warnOnClose.value )` → `Services.prefs.setBoolPref()`
- 参照: `Services.prompt`, `Tabbrowser.closingTabsEnum.ALL`, `Tabbrowser.closingTabsEnum.ALL_DUPLICATES`, `ps.BUTTON_POS_0`, `ps.BUTTON_POS_0_DEFAULT`, `ps.BUTTON_POS_1`, `ps.BUTTON_TITLE_CANCEL`, `ps.BUTTON_TITLE_IS_STRING`, `this.documentGlobal`, `warnOnClose.value`
- XPCOM: `Services.prefs` / `Services.prompt`

## Tabbrowser.#insertTabAtIndex()
- 位置: L5502-5657
- 役割: 設定と指定位置からタブの挿入位置を決め、ピン、グループ、分割ビューの境界を考慮して DOM に挿入する。
- 触るとき: 新規タブをどこに挿入するかの規則を変えるとき。
- 呼び出し先: `allItems.at()`, `tab.initialize()`, `this.#updateTabsAfterInsert()`, `this.documentGlobal.TabBarVisibility.update()`, `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (typeof elementIndex != "number" && typeof tabIndex != "number")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !bulkOrderedOpen && ((openerTab && insertRelatedAfterCurrent) || Services.prefs.getBoolPref("browser.tabs.insertAfterCurrent")) )` → `this.#lastRelatedTabMap.get()`
- 条件付き依存: `if ( !bulkOrderedOpen && ((openerTab && insertRelatedAfterCurrent) || Services.prefs.getBoolPref("browser.tabs.insertAfterCurrent")) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (previousTab.visible && previousTab.splitview)` → `this.tabContainer.dragAndDropElements.indexOf()`
- 条件付き依存: `if (openerTab)` → `this.#lastRelatedTabMap.set()`
- 条件付き依存: `if (tab.pinned)` → `Math.max()`
- 条件付き依存: `if (tab.pinned)` → `Math.min()`
- 条件付き依存: `if (!(tab.pinned))` → `Math.max()`
- 条件付き依存: `if (!(tab.pinned))` → `Math.min()`
- 条件付き依存: `if (tabGroup)` → `Tabbrowser.isTab()`
- 条件付き依存: `if (tabGroup)` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if ( (Tabbrowser.isTab(itemAfter) && itemAfter.group == tabGroup) || Tabbrowser.isSplitViewWrapper(itemAfter) )` → `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!( (Tabbrowser.isTab(itemAfter) && itemAfter.group == tabGroup) || Tabbrowser.isSplitViewWrapper(itemAfter) ))` → `tabGroup.appendChild()`
- 条件付き依存: `if (!(tabGroup))` → `Tabbrowser.isTab()`
- 条件付き依存: `if (!(tabGroup))` → `Tabbrowser.isTabGroupLabel()`
- 条件付き依存: `if ( (Tabbrowser.isTab(itemAfter) && itemAfter.group?.tabs[0] == itemAfter) || Tabbrowser.isTabGroupLabel(itemAfter) )` → `this.tabContainer.insertBefore()`
- 条件付き依存: `if (!( (Tabbrowser.isTab(itemAfter) && itemAfter.group?.tabs[0] == itemAfter) || Tabbrowser.isTabGroupLabel(itemAfter) ))` → `tabContainer.insertBefore()`
- 条件付き依存: `if (pinned)` → `this.#updateTabBarForPinnedTabs()`
- 参照: `allItems.length`, `itemAfter.group`, `itemAfter.group?.tabs`, `itemAfter.splitview`, `itemAfter?.pinned`, `itemAfter?.splitview`, `lastRelatedTab.owner`, `previousTab.elementIndex`, `previousTab.group`, `previousTab.pinned`, `previousTab.splitview`, `previousTab.visible`, `splitview.nextElementSibling`, `splitview.tabs`, `tab.group.collapsed`, `tab.group?.collapsed`, `tab.owner`, `tab.pinned`, `this.documentGlobal.FirefoxViewHandler.tab`, `this.pinnedTabCount`, `this.selectedTab`, `this.tabContainer`, `this.tabContainer.dragAndDropElements`, `this.tabContainer.pinnedTabsContainer`, `this.tabs`
- XPCOM: `Services.prefs`

## Tabbrowser.#fireTabOpen()
- 位置: L5668-5675
- 役割: initializing を解除し、detail 付きで TabOpen を送る。
- 触るとき: TabOpen の送出タイミングを調べるとき。
- 呼び出し先: `tab.dispatchEvent()`
- 参照: `tab.initializing`, `this.documentGlobal.CustomEvent`

## Tabbrowser._getTabsToTheStartFrom()
- 位置: L5681-5703
- 役割: 指定タブより前の、ピン留めと非表示を除くタブを集める。複数選択中は選択済みも除く。
- 触るとき: 左側のタブを閉じる対象の決め方を調べるとき。
- 呼び出し先: `tabsToStart.push()`
- 参照: `aTab.multiselected`, `aTab.visible`, `tabs.length`, `tabs[i].hidden`, `tabs[i].multiselected`, `tabs[i].pinned`, `this.openTabs`

## Tabbrowser._getTabsToTheEndFrom()
- 位置: L5709-5731
- 役割: 指定タブより後の、ピン留めと非表示を除くタブを集める。複数選択中は選択済みも除く。
- 触るとき: 右側のタブを閉じる対象の決め方を調べるとき。
- 呼び出し先: `tabsToEnd.push()`
- 参照: `aTab.multiselected`, `aTab.visible`, `tabs.length`, `tabs[i].hidden`, `tabs[i].multiselected`, `tabs[i].pinned`, `this.openTabs`

## Tabbrowser.#uriForDuplicateCheck()
- 位置: L5740-5749
- 役割: 重複判定に使う URI を返す。復元中の about:blank は判定不能として null を返す。
- 触るとき: 重複タブ判定で復元中タブをどう扱うかを調べるとき。
- 呼び出し先: `lazy.SessionStore.isTabRestoring()`
- 参照: `tab.linkedBrowser?.currentURI`, `uri.spec`

## Tabbrowser.getDuplicateTabsToClose()
- 位置: L5751-5807
- 役割: 指定タブ (複数選択なら全て) と URI、コンテナ、会話 ID が一致する、ピン留めでない他のタブを返す。
- 触るとき: 重複タブを閉じる対象の判定を変えるとき。
- 呼び出し先: `keyEquals()`, `keyForTab()`, `keys.some()`
- 条件付き依存: `if (aTab.multiselected)` → `keyForTab()`
- 条件付き依存: `if (key)` → `keys.push()`
- 条件付き依存: `if (!(aTab.multiselected))` → `keyForTab()`
- 条件付き依存: `if (key && keys.some(k => keyEquals(k, key)))` → `duplicateTabs.push()`
- 参照: `aTab.multiselected`, `keys.length`, `tab.multiselected`, `tab.pinned`, `this.selectedTabs`, `this.tabs`

## keyForTab()
- 位置: L5756-5766
- 役割: タブから URI、コンテナ ID、会話 ID の組を作るローカル関数。
- 触るとき: 重複判定のキーの中身を調べるとき。
- 呼び出し先: `Tabbrowser.#uriForDuplicateCheck()`, `lazy.AIWindow.getChatTabConversationId()`
- 参照: `tab.userContextId`

## keyEquals()
- 位置: L5767-5773
- 役割: 2 つのキーのコンテナ ID、会話 ID、URI が一致するかを返すローカル関数。
- 触るとき: 重複判定の一致条件を調べるとき。
- 呼び出し先: `a.uri.equals()`
- 参照: `a.conversationId`, `a.userContextId`, `b.conversationId`, `b.uri`, `b.userContextId`

## Tabbrowser.getAllDuplicateTabsToClose()
- 位置: L5809-5837
- 役割: 最近見た順に走査し、同じ URI とコンテナで 2 つ目以降のピン留めでないタブを重複として返す。
- 触るとき: すべての重複タブを閉じる機能の対象判定を変えるとき。
- 呼び出し先: `Tabbrowser.#uriForDuplicateCheck()`, `lazy.AIWindow.getChatTabConversationId()`, `this.tabs.toSorted()`, `userContextIds.add()`, `userContextIds.has()`, `userContextIdsPerUri.getOrInsertComputed()`
- 条件付き依存: `if (!tab.pinned && userContextIds.has(userContextId))` → `duplicateTabs.push()`
- 参照: `a.lastSeenActive`, `b.lastSeenActive`, `tab.pinned`, `tab.userContextId`, `uri.spec`

## Tabbrowser.removeDuplicateTabs()
- 位置: L5839-5846
- 役割: 指定タブの重複タブを集めて #removeDuplicateTabs で閉じる。
- 触るとき: コンテキストメニューの重複タブを閉じる操作を調べるとき。
- 呼び出し先: `this.#removeDuplicateTabs()`, `this.getDuplicateTabsToClose()`
- 参照: `Tabbrowser.closingTabsEnum.DUPLICATES`

## Tabbrowser.#removeDuplicateTabs()
- 位置: L5848-5863
- 役割: 対象があれば警告を確認して removeTabs で閉じ、閉じた数の確認ヒントを出す。
- 触るとき: 重複タブを閉じた後の確認ヒント表示を調べるとき。
- 呼び出し先: `this.documentGlobal.ConfirmationHint.show()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`
- 参照: `tabs.length`

## Tabbrowser.removeAllDuplicateTabs()
- 位置: L5873-5881
- 役割: ウィンドウ全体の重複タブを閉じる。ヒントの表示位置は既定で All Tabs ボタン。
- 触るとき: 全重複タブを閉じる操作と、ヒントの出し先を調べるとき。
- 呼び出し先: `this.#removeDuplicateTabs()`, `this.document.getElementById()`, `this.getAllDuplicateTabsToClose()`
- 参照: `Tabbrowser.closingTabsEnum.ALL_DUPLICATES`

## Tabbrowser.removeTabsToTheStartFrom()
- 位置: L5891-5903
- 役割: 指定タブより前のタブを、警告確認後に閉じる。
- 触るとき: 左側のタブを閉じる操作を調べるとき。
- 呼び出し先: `this._getTabsToTheStartFrom()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`
- 参照: `Tabbrowser.closingTabsEnum.TO_START`, `tabs.length`

## Tabbrowser.removeTabsToTheEndFrom()
- 位置: L5913-5922
- 役割: 指定タブより後のタブを、警告確認後に閉じる。
- 触るとき: 右側のタブを閉じる操作を調べるとき。
- 呼び出し先: `this._getTabsToTheEndFrom()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`
- 参照: `Tabbrowser.closingTabsEnum.TO_END`, `tabs.length`

## Tabbrowser.removeAllTabsBut()
- 位置: L5940-5977
- 役割: 指定タブ以外を閉じる。既定ではピン留めと選択済みは除き、警告確認も行う。
- 触るとき: 他のタブを閉じる操作の対象条件を変えるとき。
- 呼び出し先: `this.openTabs.filter()`, `this.removeTabs()`, `this.warnAboutClosingTabs()`
- 参照: `Tabbrowser.closingTabsEnum.OTHER`, `aTab?.multiselected`, `tabsToRemove.length`

## filterFn()
- 位置: L5954-5954
- 役割: 複数選択中に、未選択でピン留め/非表示でないタブを対象にするフィルタ。
- 触るとき: 他のタブを閉じる際の複数選択時の対象を調べるとき。
- 参照: `tab.hidden`, `tab.multiselected`, `tab.pinned`

## filterFn()
- 位置: L5956-5956
- 役割: 指定タブ以外で、ピン留め/非表示でないタブを対象にするフィルタ。
- 触るとき: 他のタブを閉じる際の通常時の対象を調べるとき。
- 参照: `tab.hidden`, `tab.pinned`

## filterFn()
- 位置: L5960-5960
- 役割: 指定タブ以外を全て対象にするフィルタ。
- 触るとき: ピン留めも含めて閉じる場合の対象を調べるとき。

## Tabbrowser.removeMultiSelectedTabs()
- 位置: L5989-6014
- 役割: 選択中のタブを警告確認後に閉じる。ピン留めを除く指定時はその後に選択を整える。
- 触るとき: 複数選択したタブを閉じる操作を調べるとき。
- 呼び出し先: `this.warnAboutClosingTabs()`
- 条件付き依存: `if (excludePinnedTabs)` → `this.selectedTabs.filter()`
- 条件付き依存: `if (excludePinnedTabs)` → `this.removeTabs()`
- 条件付き依存: `if (excludePinnedTabs)` → `this.clearMultiSelectedTabs()`
- 条件付き依存: `if (!(excludePinnedTabs))` → `this.removeTabs()`
- 参照: `Tabbrowser.closingTabsEnum.MULTI_SELECTED`, `selectedTabs.length`, `tab.pinned`, `this.pinnedTabCount`, `this.selectedTab.pinned`, `this.selectedTabs`, `this.tabContainer.selectedIndex`, `this.visibleTabs.length`

## Tabbrowser.#startRemoveTabs()
- 位置: L6050-6148
- 役割: 各タブの beforeunload を並列に確認し、確認不要なものは先に閉じ、プロンプト要のタブと最後に閉じるタブを返す。
- 触るとき: 複数タブを閉じるときの beforeunload の処理順序を変えるとき。
- 呼び出し先: `Promise.all()`
- 条件付き依存: `if (!skipRemoves && tab.selected)` → `this._findTabToBlurTo()`
- 条件付き依存: `if (toBlurTo)` → `this._getSwitcher().warmupTab()`
- 条件付き依存: `if (toBlurTo)` → `this._getSwitcher()`
- 条件付き依存: `if (!(!skipRemoves && tab.selected))` → `Tabbrowser.#hasBeforeUnload()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Glean.browserTabclose.permitUnloadTime.start()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Tabbrowser.#tabsPendingPermitUnload.add()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `beforeUnloadPromises.push()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `tab.linkedBrowser.asyncPermitUnload("dontUnload").then()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `tab.linkedBrowser.asyncPermitUnload()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Tabbrowser.#tabsPendingPermitUnload.delete()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `Glean.browserTabclose.permitUnloadTime.stopAndAccumulate()`
- 条件付き依存: `if (!skipRemoves)` → `this.removeTab()`
- 条件付き依存: `if (!(permitUnload))` → `tabsWithBeforeUnloadPrompt.push()`
- 条件付き依存: `if (!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab))` → `console.error()`
- 条件付き依存: `if (!(!skipPermitUnload && Tabbrowser.#hasBeforeUnload(tab)))` → `tabsWithoutBeforeUnload.push()`
- 参照: `tab.closing`, `tab.selected`

## Tabbrowser.runBeforeUnloadForTabs()
- 位置: async L6168-6193
- 役割: 閉じる前に beforeunload を実行し、ユーザーが中止したかを返す。実際には閉じない。
- 触るとき: タブを閉じる前に確認だけを先に行いたいとき。
- 呼び出し先: `Tabbrowser.#tabsPendingPermitUnload.add()`, `Tabbrowser.#tabsPendingPermitUnload.delete()`, `console.error()`, `this.#startRemoveTabs()`, `this.getBrowserForTab()`, `this.getBrowserForTab(tab).permitUnload()`

## Tabbrowser.#separateWholeGroups()
- 位置: L6204-6233
- 役割: 閉じるタブ群を、全タブが含まれるグループとそれ以外のタブに分けて返す。
- 触るとき: グループ全体を閉じる場合の判定を調べるとき。
- 呼び出し先: `tabGroupSurvivingTabs.entries()`
- 条件付き依存: `if (tab.group)` → `tabGroupSurvivingTabs.has()`
- 条件付き依存: `if (!tabGroupSurvivingTabs.has(tab.group))` → `tabGroupSurvivingTabs.set()`
- 条件付き依存: `if (tab.group)` → `tabGroupSurvivingTabs.get(tab.group).delete()`
- 条件付き依存: `if (tab.group)` → `tabGroupSurvivingTabs.get()`
- 条件付き依存: `if (!survivingTabs.size)` → `wholeGroups.push()`
- 条件付き依存: `if (!survivingTabs.size)` → `tabs.filter()`
- 条件付き依存: `if (!survivingTabs.size)` → `tabGroup.tabs.includes()`
- 参照: `survivingTabs.size`, `tab.group`, `tab.group.tabs`

## Tabbrowser.removeTabs()
- 位置: L6260-6401
- 役割: 複数タブを閉じる。全タブならウィンドウを閉じ、グループは保存して削除し、確認後に残りを閉じて記録する。
- 触るとき: 複数タブを閉じる処理全般や、ウィンドウを閉じる条件を調べるとき。
- 呼び出し先: `Promise.all()`, `Promise.all([...groupRemovalPromises, beforeUnloadComplete]).then()`, `Services.prefs.getBoolPref()`, `Services.tm.spinEventLoopUntilOrQuit()`, `console.error()`, `this.#avoidSingleSelectedTab()`, `this.#startRemoveTabs()`, `this.TabMetrics.decomposedContext()`, `this.removeTab()`
- 条件付き依存: `if ( this.tabs.length == tabs.length && (closeWindowWithLastTab ?? Services.prefs.getBoolPref("browser.tabs.closeWindowWithLastTab")) )` → `this.documentGlobal.closeWindow()`
- 条件付き依存: `if (!skipSessionStore)` → `lazy.SessionStore.resetLastClosedTabCount()`
- 条件付き依存: `if (!skipGroupCheck)` → `Tabbrowser.#separateWholeGroups()`
- 条件付き依存: `if (!skipGroupCheck)` → `groups.map()`
- 条件付き依存: `if (!skipGroupCheck)` → `groupTabsToClose.push()`
- 条件付き依存: `if (!skipSessionStore)` → `group.save()`
- 条件付き依存: `if (!skipGroupCheck)` → `this.removeTabGroup()`
- 条件付き依存: `if (!skipGroupCheck)` → `this.TabMetrics.decomposedContext()`
- 条件付き依存: `if (lastToClose)` → `this.removeTab()`
- 条件付き依存: `if (closedTabCount > 0)` → `this.recordTabMetrics()`
- 参照: `group.tabs`, `lastToClose.closing`, `tab.closing`, `tabs.length`, `this.#clearMultiSelectionLocked`, `this.TabMetrics.METRIC_ACTION.CLOSE`, `this.documentGlobal`, `this.documentGlobal.closed`, `this.documentGlobal.warnAboutClosingWindow`, `this.tabs.length`
- XPCOM: `Services.prefs` / `Services.tm`

## Tabbrowser.removeCurrentTab()
- 位置: L6409-6411
- 役割: 選択中のタブを removeTab で閉じる。
- 触るとき: 現在のタブを閉じる操作の経路を調べるとき。
- 呼び出し先: `this.removeTab()`
- 参照: `this.selectedTab`

## Tabbrowser.maybeCloseTabForRetargetedLoad()
- 位置: L6421-6433
- 役割: 読み込みが他へ移された空のタブ (ピン留めでも最後でもない) を閉じる。
- 触るとき: 別タブへ移った読み込みで残った空タブの後始末を調べるとき。
- 呼び出し先: `this.getTabForBrowser()`, `this.removeTab()`
- 参照: `tab.isEmptyIgnoringLoad`, `tab.pinned`, `this.tabs.length`

## Tabbrowser.removeTab()
- 位置: L6465-6611
- 役割: タブを閉じる。beforeunload の確認、選択の移し替え、アニメーションの要否判断を行い、最後に _endRemoveTab を呼ぶ。
- 触るとき: タブを閉じる挙動やアニメーション、閉じる際の不具合を調べるとき。
- 呼び出し先: `(triggeringEvent.target).closest()`, `Glean.browserTabclose.timeNoAnim.cancel()`, `Services.prefs.getBoolPref()`, `Tabbrowser.#closeTimeAnimTimerIds.get()`, `Tabbrowser.#closeTimeNoAnimTimerIds.delete()`, `Tabbrowser.#closeTimeNoAnimTimerIds.get()`, `UserInteraction.running()`, `aTab.hasAttribute()`, `aTab.removeAttribute()`, `lazy.MiniWindowManager.maybeMoveOldestMiniWindow()`, `tabbrowser.documentGlobal.getComputedStyle()`, `this.#beginRemoveTab()`, `this.#isLastTabInWindow()`, `this.documentGlobal.setTimeout()`, `this.documentGlobal.windowUtils.getBoundsWithoutFlushing()`, `this.tabContainer.openAnimationFinished()`
- 条件付き依存: `if (UserInteraction.running("browser.tabs.opening", this.documentGlobal))` → `UserInteraction.finish()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Tabbrowser.#closeTimeAnimTimerIds.set()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Glean.browserTabclose.timeAnim.start()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Tabbrowser.#closeTimeNoAnimTimerIds.set()`
- 条件付き依存: `if ( !Tabbrowser.#closeTimeAnimTimerIds.get(aTab) && !Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab) )` → `Glean.browserTabclose.timeNoAnim.start()`
- 条件付き依存: `if (!animate && aTab.closing)` → `this._endRemoveTab()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Glean.browserTabclose.timeAnim.cancel()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeAnimTimerIds.get()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeAnimTimerIds.delete()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Glean.browserTabclose.timeNoAnim.cancel()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeNoAnimTimerIds.get()`
- 条件付き依存: `if ( !this.#beginRemoveTab(aTab, { closeWindowFastpath: true, skipPermitUnload, closeWindowWithLastTab, prewarmed, skipSessionStore, inMultiselection, metricsCon...)` → `Tabbrowser.#closeTimeNoAnimTimerIds.delete()`
- 条件付き依存: `if (lockTabSizing)` → `this.tabContainer._lockTabSizing()`
- 条件付き依存: `if (!(lockTabSizing))` → `this.tabContainer._unlockTabSizing()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `Glean.browserTabclose.timeAnim.cancel()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `Tabbrowser.#closeTimeAnimTimerIds.get()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `Tabbrowser.#closeTimeAnimTimerIds.delete()`
- 条件付き依存: `if ( !animate /* the caller didn't opt in */ || this.documentGlobal.gReduceMotion || isLastTab || aTab.pinned || !isVisibleTab || this.tabContainer.verticalMode ...)` → `this._endRemoveTab()`
- 条件付き依存: `if ( tab.container && tabbrowser.documentGlobal.getComputedStyle(tab).maxWidth == "0.1px" )` → `console.assert()`
- 条件付き依存: `if ( tab.container && tabbrowser.documentGlobal.getComputedStyle(tab).maxWidth == "0.1px" )` → `tabbrowser._endRemoveTab()`
- 参照: `MouseEvent.MOZ_SOURCE_MOUSE`, `aTab.closing`, `aTab.pinned`, `aTab.style.maxWidth`, `aTab.visible`, `tab.container`, `tabbrowser.documentGlobal.getComputedStyle(tab).maxWidth`, `this._removingTabs.size`, `this.documentGlobal`, `this.documentGlobal.gReduceMotion`, `this.documentGlobal.windowUtils.getBoundsWithoutFlushing(aTab).width`, `this.tabContainer.verticalMode`, `triggeringEvent.target`, `triggeringEvent?.inputSource`
- XPCOM: `Services.prefs`

## Tabbrowser.#shouldCloseWindowWithLastTab()
- 位置: L6619-6624
- 役割: ツールバー非表示か設定により、最後のタブでウィンドウを閉じるかを返す。
- 触るとき: 最後のタブを閉じたときの挙動を決める条件を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.documentGlobal.toolbar.visible`
- XPCOM: `Services.prefs`

## Tabbrowser.#isLastTabInWindow()
- 位置: L6636-6643
- 役割: 非表示を除いて、指定タブがウィンドウ内の最後の開いているタブかを返す。
- 触るとき: 最後のタブか否かの判定規則を調べるとき。
- 参照: `otherTab.hidden`, `otherTab.isOpen`, `this.tabs`

## Tabbrowser.#hasBeforeUnload()
- 位置: L6645-6651
- 役割: リモート browser で beforeunload ハンドラを持つかを返す。
- 触るとき: 閉じる際の確認要否の判定を調べるとき。
- 参照: `aTab.linkedBrowser`, `browser.frameLoader`, `browser.hasBeforeUnload`, `browser.isRemoteBrowser`

## Tabbrowser.#beginRemoveTab()
- 位置: L6686-6911
- 役割: 確認とリスナー解除、イベント送出など、アニメーション前の閉じる準備を行い、続行してよいかを返す。
- 触るとき: タブを閉じる前半の処理や、ウィンドウごと閉じる分岐を調べるとき。
- 呼び出し先: `Tabbrowser.#endRemoveArgs.set()`, `Tabbrowser.#hasBeforeUnload()`, `Tabbrowser.#tabsPendingPermitUnload.has()`, `aTab._mouseleave()`, `aTab.dispatchEvent()`, `aTab.hasAttribute()`, `browser.removeAttribute()`, `notificationBox?._stack?.remove()`, `this.#isLastTabInWindow()`, `this._removingTabs.add()`, `this._tabLayerCache.indexOf()`, `this.getBrowserForTab()`, `this.getSuccessor()`, `this.readNotificationBox()`, `this.recordTabMetrics()`, `this.replaceInSuccession()`, `this.setSuccessor()`, `this.tabContainer._invalidateCachedTabs()`, `this.tabContainer._invalidateCachedVisibleTabs()`, `this.tabContainer.cancelTabOpening()`, `this.tabContainer.matches()`
- 条件付き依存: `if (!prewarmed)` → `this._findTabToBlurTo()`
- 条件付き依存: `if (blurTab)` → `this.warmupTab()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Glean.browserTabclose.permitUnloadTime.start()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Tabbrowser.#tabsPendingPermitUnload.add()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `browser.permitUnload()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Tabbrowser.#tabsPendingPermitUnload.delete()`
- 条件付き依存: `if ( !skipPermitUnload && !adoptedByTab && aTab.linkedPanel && !Tabbrowser.#tabsPendingPermitUnload.has(aTab) && (!browser.isRemoteBrowser || Tabbrowser.#hasBefo...)` → `Glean.browserTabclose.permitUnloadTime.stopAndAccumulate()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this._tabLayerCache.splice()`
- 条件付き依存: `if (!screenShareInActiveTab)` → `this.#blurTab()`
- 条件付き依存: `if (closeWindow && closeWindowFastpath && !this._removingTabs.size)` → `this.documentGlobal.closeWindow()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabFilters.get()`
- 条件付き依存: `if (aTab.linkedPanel)` → `browser.webProgress.removeProgressListener()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabListeners.get()`
- 条件付き依存: `if (aTab.linkedPanel)` → `filter.removeProgressListener()`
- 条件付き依存: `if (aTab.linkedPanel)` → `listener.destroy()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabListeners.delete()`
- 条件付き依存: `if (aTab.linkedPanel)` → `Tabbrowser.#tabFilters.delete()`
- 条件付き依存: `if (!adoptedByTab && aTab.hasAttribute("soundplaying"))` → `aTab.linkedBrowser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (handOverHover)` → `this.#tabTakingPlaceOf(aTab)?._mouseenter()`
- 条件付き依存: `if (handOverHover)` → `this.#tabTakingPlaceOf()`
- 条件付き依存: `if (newTab)` → `this.addTrustedTab()`
- 条件付き依存: `if (!(newTab))` → `this.documentGlobal.TabBarVisibility.update()`
- 条件付き依存: `if (!adoptedByTab && !this.documentGlobal.gMultiProcessBrowser)` → `browser.contentWindow.windowUtils.disableDialogs()`
- 条件付き依存: `if (browser.registeredOpenURI && !adoptedByTab)` → `browser.getAttribute()`
- 条件付き依存: `if (browser.registeredOpenURI && !adoptedByTab)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (browser.registeredOpenURI && !adoptedByTab)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `aTab._hover`, `aTab.closing`, `aTab.group?.id`, `aTab.linkedPanel`, `bc.hasSiblings`, `browser._sharingState?.webRTC?.screen`, `browser.isRemoteBrowser`, `browser.registeredOpenURI`, `browser.registeredOpenURI.spec`, `tab.linkedBrowser.browsingContext`, `this.#shouldCloseWindowWithLastTab`, `this.#windowIsClosing`, `this.TabMetrics.METRIC_ACTION.CLOSE`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this._removingTabs.size`, `this.documentGlobal`, `this.documentGlobal.BROWSER_NEW_TAB_URL`, `this.documentGlobal.CustomEvent`, `this.documentGlobal.gMultiProcessBrowser`, `this.documentGlobal.skipNextCanClose`, `this.documentGlobal.warnAboutClosingWindow`, `this.selectedTab`, `this.tabs`, `this.tabs.length`

## Tabbrowser.#tabTakingPlaceOf()
- 位置: L6919-6928
- 役割: 閉じるタブの後ろに続く、最初のフォーカス可能なタブを返す。タブでなければ null。
- 触るとき: タブを閉じた際のホバー引き継ぎ先を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`, `closingTab.compareDocumentPosition()`, `this.tabContainer.ariaFocusableItems.find()`
- 参照: `Node.DOCUMENT_POSITION_FOLLOWING`

## Tabbrowser._endRemoveTab()
- 位置: L6930-7058
- 役割: 閉じるタブを DOM から取り除き、browser とパネルを破棄し、必要ならウィンドウを閉じる。
- 触るとき: タブ削除の後半 (DOM 除去と破棄) や後始末を調べるとき。
- 呼び出し先: `Tabbrowser.#closeTimeAnimTimerIds.get()`, `Tabbrowser.#closeTimeNoAnimTimerIds.get()`, `Tabbrowser.#endRemoveArgs.delete()`, `Tabbrowser.#endRemoveArgs.get()`, `Tabbrowser.#tabFilters.delete()`, `Tabbrowser.#tabListeners.delete()`, `aTab.remove()`, `browser.remove()`, `panel.remove()`, `this.#blurTab()`, `this.#tabForBrowser.delete()`, `this._removingTabs.delete()`, `this.getBrowserForTab()`, `this.getPanel()`, `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (aCloseWindow)` → `this._endRemoveTab()`
- 条件付き依存: `if (aNewTab)` → `this.documentGlobal.gURLBar.select()`
- 条件付き依存: `if (aTab.linkedPanel)` → `browser.destroy()`
- 条件付き依存: `if (!this.#windowIsClosing)` → `this.tabContainer._updateCloseButtons()`
- 条件付き依存: `if (!this.#windowIsClosing)` → `this.documentGlobal.setTimeout()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.onTabRemoved()`
- 条件付き依存: `if (Tabbrowser.#closeTimeAnimTimerIds.get(aTab))` → `Glean.browserTabclose.timeAnim.stopAndAccumulate()`
- 条件付き依存: `if (Tabbrowser.#closeTimeAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeAnimTimerIds.get()`
- 条件付き依存: `if (Tabbrowser.#closeTimeAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeAnimTimerIds.delete()`
- 条件付き依存: `if (Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab))` → `Glean.browserTabclose.timeNoAnim.stopAndAccumulate()`
- 条件付き依存: `if (Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeNoAnimTimerIds.get()`
- 条件付き依存: `if (Tabbrowser.#closeTimeNoAnimTimerIds.get(aTab))` → `Tabbrowser.#closeTimeNoAnimTimerIds.delete()`
- 条件付き依存: `if (aCloseWindow)` → `this.documentGlobal.closeWindow()`
- 参照: `aTab.collapsed`, `aTab.index`, `aTab.linkedBrowser`, `aTab.linkedPanel`, `tabs._lastTabClosedByMouse`, `this.#lastRelatedTabMap`, `this.#windowIsClosing`, `this._removingTabs`, `this._switcher`, `this.documentGlobal.warnAboutClosingWindow`, `this.selectedTab._selected`, `this.tabContainer`, `this.tabs`, `this.tabs.length`, `this.tabs[i]._index`

## Tabbrowser.closeTabsByURI()
- 位置: async L7068-7109
- 役割: URI が一致するタブを beforeunload 確認の上で閉じ、閉じた数を返す。確認が出るタブは閉じない。
- 触るとき: URI を指定した一括クローズ機能を調べるとき。
- 呼び出し先: `uriToClose.equals()`, `urisToClose.findIndex()`
- 条件付き依存: `if (matchedIndex > -1)` → `tabsToRemove.push()`
- 条件付き依存: `if (tabsToRemove.length)` → `this.#startRemoveTabs()`
- 条件付き依存: `if (lastToClose)` → `this.removeTab()`
- 参照: `tab.linkedBrowser.currentURI`, `tabsToRemove.length`, `this.tabs`

## Tabbrowser.explicitUnloadTabs()
- 位置: async L7111-7180
- 役割: 確認後、選択中なら別タブへ移ってから対象タブを破棄し、メモリと所要時間を Glean に記録する。
- 触るとき: タブの明示的なアンロード機能とそのテレメトリを調べるとき。
- 呼び出し先: `Glean.browserEngagement.tabExplicitUnload.record()`, `Math.floor()`, `Promise.all()`, `getTotalMemoryUsage()`, `tabs.map()`, `tabs.some()`, `this.discardBrowser()`, `this.documentGlobal.performance.now()`, `this.prepareDiscardBrowser()`, `this.runBeforeUnloadForTabs()`
- 条件付き依存: `if (tabs.some(tab => tab.selected || tab.splitview?.hasActiveTab))` → `tabs.concat()`
- 条件付き依存: `if (tabs.some(tab => tab.selected || tab.splitview?.hasActiveTab))` → `this.tabContainer.allTabs.filter()`
- 条件付き依存: `if (tab.splitview)` → `tabsToExclude.push()`
- 条件付き依存: `if (tab.splitview)` → `tab.splitview.tabs.filter()`
- 条件付き依存: `if (tabs.some(tab => tab.selected || tab.splitview?.hasActiveTab))` → `this._findTabToBlurTo()`
- 条件付き依存: `if (!(newTab))` → `this.documentGlobal.FirefoxViewHandler.button?.checkVisibility()`
- 条件付き依存: `if (firefoxViewAvailable)` → `this.documentGlobal.FirefoxViewHandler.openTab()`
- 条件付き依存: `if (!(firefoxViewAvailable))` → `this.addTrustedTab()`
- 参照: `tab.linkedPanel`, `tab.selected`, `tab.splitview`, `tab.splitview?.hasActiveTab`, `this.documentGlobal.BROWSER_NEW_TAB_URL`, `this.documentGlobal.FirefoxViewHandler.tab`, `this.selectedTab`

## Tabbrowser.handleNewTabMiddleClick()
- 位置: L7190-7206
- 役割: disabled でなければ、中クリックで新規タブを開き、イベントの伝播を止める。
- 触るとき: 新規タブボタンの中クリック動作を変えるとき。
- 呼び出し先: `node.hasAttribute()`
- 条件付き依存: `if (event.button == 1)` → `this.documentGlobal.BrowserCommands.openTab()`
- 条件付き依存: `if (event.button == 1)` → `event.stopPropagation()`
- 条件付き依存: `if (event.button == 1)` → `event.preventDefault()`
- 参照: `event.button`

## Tabbrowser._findTabToBlurTo()
- 位置: L7217-7305
- 役割: タブを閉じる/隠すときに次に選ぶタブを、successor、owner、MRU、近傍の順などで決める。
- 触るとき: タブを閉じた後にどのタブが選ばれるかの規則を変えるとき。
- 呼び出し先: `Array.prototype.filter.call()`, `Services.prefs.getBoolPref()`, `excludeTabs.has()`, `new Set(this.tabsInCollapsedTabGroups).difference()`, `tab.hasAttribute()`, `this.getSuccessor()`, `this.tabContainer.findNextTab()`
- 条件付き依存: `if (this.documentGlobal.FirefoxViewHandler.tab)` → `aExcludeTabs.push()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.selectMRUOnClose", false))` → `remainingTabs .filter(t => t !== aTab) .reduce()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.tabs.selectMRUOnClose", false))` → `remainingTabs .filter()`
- 条件付き依存: `if (!tab)` → `this.tabContainer.findNextTab()`
- 参照: `aTab.owner`, `aTab.owner?.visible`, `aTab.selected`, `best.lastAccessed`, `nonDiscardedTabs.length`, `t.lastAccessed`, `this.documentGlobal.FirefoxViewHandler.tab`, `this.tabsInCollapsedTabGroups`, `this.visibleTabs`
- XPCOM: `Services.prefs`

## filter()
- 位置: L7272-7272
- 役割: 残っているタブに含まれるものだけを通すフィルタ。
- 触るとき: 次に選ぶタブの探索範囲を調べるとき。
- 呼び出し先: `remainingTabs.includes()`

## filter()
- 位置: L7278-7278
- 役割: 残っているタブに含まれるものだけを通すフィルタ (逆方向の探索用)。
- 触るとき: 次に選ぶタブの探索範囲を調べるとき。
- 呼び出し先: `remainingTabs.includes()`

## filter()
- 位置: L7294-7294
- 役割: 折りたたみグループ内の候補に含まれるものだけを通すフィルタ。
- 触るとき: 折りたたみグループ内のタブを選択候補にする処理を調べるとき。
- 呼び出し先: `eligibleTabs.has()`

## filter()
- 位置: L7300-7300
- 役割: 折りたたみグループ内の候補に含まれるものだけを通すフィルタ (逆方向の探索用)。
- 触るとき: 折りたたみグループ内のタブを選択候補にする処理を調べるとき。
- 呼び出し先: `eligibleTabs.has()`

## Tabbrowser.#blurTab()
- 位置: L7307-7309
- 役割: 移り先のタブを _findTabToBlurTo で決め、選択する。
- 触るとき: タブを外す際の選択移動の入口を調べるとき。
- 呼び出し先: `this._findTabToBlurTo()`
- 参照: `this.selectedTab`

## Tabbrowser.swapBrowsersAndCloseOther()
- 位置: L7321-7549
- 役割: 別タブの browser を自分のタブと入れ替え、状態を引き継いで元のタブ (別ウィンドウ可) を閉じる。入れ替え不可なら false を返す。
- 触るとき: ウィンドウ間のタブ移動 (採用) の中核処理や、引き継ぐ属性を変えるとき。
- 呼び出し先: `Tabbrowser.#endRemoveArgs.get()`, `Tabbrowser.#findBars.get()`, `Tabbrowser.#originalRegisteredOpenURIs.set()`, `Tabbrowser.#tabListeners.get()`, `aOtherTab.hasAttribute()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SitePermissions.copyTemporaryPermissions()`, `otherBrowser.hasAttribute()`, `remoteBrowser.#beginRemoveTab()`, `this.getBrowserForTab()`, `this.setTabTitle()`
- 条件付き依存: `if (otherBrowser.hasAttribute("usercontextid"))` → `ourBrowser.setAttribute()`
- 条件付き依存: `if (otherBrowser.hasAttribute("usercontextid"))` → `otherBrowser.getAttribute()`
- 条件付き依存: `if (aOtherTab._soundPlayingAttrRemovalTimer)` → `aOtherTab.documentGlobal.clearTimeout()`
- 条件付き依存: `if (aOtherTab._soundPlayingAttrRemovalTimer)` → `aOtherTab.removeAttribute()`
- 条件付き依存: `if (aOtherTab._soundPlayingAttrRemovalTimer)` → `remoteBrowser._tabAttrModified()`
- 条件付き依存: `if (closeWindow)` → `win.windowUtils.suppressAnimation()`
- 条件付き依存: `if (closeWindow)` → `win.docShell.treeOwner.QueryInterface()`
- 条件付き依存: `if (aOtherTab.hasAttribute("muted"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOurTab.linkedPanel)` → `ourBrowser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("muted"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("discarded"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("discarded"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("undiscardable"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("undiscardable"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("soundplaying"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("soundplaying"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("usercontextid"))` → `aOurTab.setUserContextId()`
- 条件付き依存: `if (aOtherTab.hasAttribute("usercontextid"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `aOurTab.setAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `aOtherTab.getAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("sharing"))` → `lazy.webrtcUI.swapBrowserForNotification()`
- 条件付き依存: `if (aOtherTab.hasAttribute("pictureinpicture"))` → `aOurTab.toggleAttribute()`
- 条件付き依存: `if (aOtherTab.hasAttribute("pictureinpicture"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aOtherTab.hasAttribute("pictureinpicture"))` → `aOtherTab.dispatchEvent()`
- 条件付き依存: `if (isPending)` → `lazy.SessionStore.setTabState()`
- 条件付き依存: `if (isPending)` → `lazy.SessionStore.getTabState()`
- 条件付き依存: `if (isPending)` → `Tabbrowser.#swapRegisteredOpenURIs()`
- 条件付き依存: `if (!ourBrowser.mIconURL && otherBrowser.mIconURL)` → `this.setIcon()`
- 条件付き依存: `if (!(isPending))` → `aOtherTab.hasAttribute()`
- 条件付き依存: `if (isBusy)` → `aOurTab.setAttribute()`
- 条件付き依存: `if (isBusy)` → `modifiedAttrs.push()`
- 条件付き依存: `if (!(isPending))` → `this.#swapBrowserDocShells()`
- 条件付き依存: `if (otherBrowser.registeredOpenURI)` → `otherBrowser.getAttribute()`
- 条件付き依存: `if (otherBrowser.registeredOpenURI)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (otherBrowser.registeredOpenURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (otherFindBar && otherFindBar.findMode == otherFindBar.FIND_NORMAL)` → `this.getFindBar()`
- 条件付き依存: `if (otherFindBar && otherFindBar.findMode == otherFindBar.FIND_NORMAL)` → `ourFindBarPromise.then()`
- 条件付き依存: `if (!wasHidden)` → `ourFindBar.onFindCommand()`
- 条件付き依存: `if (closeWindow)` → `aOtherTab.documentGlobal.close()`
- 条件付き依存: `if (!(closeWindow))` → `remoteBrowser._endRemoveTab()`
- 条件付き依存: `if (aOurTab.selected)` → `this.updateCurrentBrowser()`
- 条件付き依存: `if (modifiedAttrs.length)` → `this._tabAttrModified()`
- 参照: `Ci.nsIBaseWindow`, `aOtherTab._soundPlayingAttrRemovalTimer`, `aOtherTab.canonicalUrl`, `aOtherTab.documentGlobal`, `aOtherTab.documentGlobal.gBrowser`, `aOtherTab.documentGlobal.gFissionBrowser`, `aOtherTab.group?.id`, `aOtherTab.hasTabNote`, `aOtherTab.linkedBrowser`, `aOtherTab.muteReason`, `aOtherTab.userContextId`, `aOurTab.canonicalUrl`, `aOurTab.hasTabNote`, `aOurTab.initializing`, `aOurTab.linkedPanel`, `aOurTab.muteReason`, `aOurTab.selected`, `baseWin.visibility`, `modifiedAttrs.length`, `otherBrowser._sharingState`, `otherBrowser.browserId`, `otherBrowser.isRemoteBrowser`, `otherBrowser.mIconURL`, `otherBrowser.registeredOpenURI`, `otherBrowser.registeredOpenURI.spec`, `otherFindBar.FIND_NORMAL`, `otherFindBar._findField.value`, `otherFindBar.findMode`, `otherFindBar.hidden`, `otherTabListener._stateFlags`, `ourBrowser._cachedCurrentURI`, `ourBrowser._sharingState`, `ourBrowser.isRemoteBrowser`, `ourBrowser.mIconURL`, `ourFindBar._findField.value`, `this._isBusy`, `this.documentGlobal`, `this.documentGlobal.CustomEvent`, `this.documentGlobal.gFissionBrowser`
- XPCOM: `nsIBaseWindow`

## Tabbrowser.swapBrowsers()
- 位置: L7551-7575
- 役割: もう一方のタブを閉じずに docShell を入れ替え、そのタブの進捗リスナーを付け直す。
- 触るとき: タブを閉じない形での browser の入れ替えを調べるとき。
- 呼び出し先: `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Tabbrowser.#tabListeners.set()`, `filter.addProgressListener()`, `filter.removeProgressListener()`, `otherBrowser.webProgress.addProgressListener()`, `otherBrowser.webProgress.removeProgressListener()`, `this.#swapBrowserDocShells()`
- 参照: `Ci.nsIWebProgress.NOTIFY_ALL`, `aOtherTab.linkedBrowser`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## Tabbrowser.#swapBrowserDocShells()
- 位置: L7577-7636
- 役割: docShell と permanentKey を入れ替え、進捗リスナーと開いている URI の登録を付け替える。
- 触るとき: docShell 入れ替え時のリスナーや登録の扱いを調べるとき。
- 呼び出し先: `Tabbrowser.#swapRegisteredOpenURIs()`, `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Tabbrowser.#tabListeners.set()`, `aOtherBrowser.ownerDocument.getElementById()`, `aOurTab.registerAudibleChangeHandler()`, `filter.addProgressListener()`, `filter.removeProgressListener()`, `ourBrowser.ownerDocument.getElementById()`, `ourBrowser.swapDocShells()`, `ourBrowser.webProgress.addProgressListener()`, `ourBrowser.webProgress.removeProgressListener()`, `this.#insertBrowser()`, `this.getBrowserForTab()`
- 条件付き依存: `if (!this._switcher)` → `this.shouldActivateDocShell()`
- 参照: `Ci.nsIWebProgress.NOTIFY_ALL`, `aOtherBrowser.docShellIsActive`, `aOtherBrowser.permanentKey`, `otherBrowserContainer.hidden`, `ourBrowser.permanentKey`, `ourBrowserContainer.hidden`, `this._switcher`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## Tabbrowser.#swapRegisteredOpenURIs()
- 位置: L7638-7649
- 役割: 2 つの browser の registeredOpenURI を入れ替える。
- 触るとき: 入れ替え時の switch-to-tab 用の登録の扱いを調べるとき。
- 参照: `aOtherBrowser.registeredOpenURI`, `aOurBrowser.registeredOpenURI`

## Tabbrowser.reloadMultiSelectedTabs()
- 位置: L7651-7653
- 役割: 選択中のタブをまとめて reloadTabs で再読み込みする。
- 触るとき: 複数選択タブのリロード経路を調べるとき。
- 呼び出し先: `this.reloadTabs()`
- 参照: `this.selectedTabs`

## Tabbrowser.reloadTabs()
- 位置: L7655-7663
- 役割: 指定タブを順に reload し、失敗は無視して残りを続ける。
- 触るとき: 複数タブのリロードの失敗時の扱いを調べるとき。
- 呼び出し先: `this.getBrowserForTab()`, `this.getBrowserForTab(tab).reload()`

## Tabbrowser.reloadTab()
- 位置: L7665-7675
- 役割: 一時的なブロック権限と認証プロンプトの抑止をリセットし、ポップアップを閉じて reload する。
- 触るとき: ユーザーのリロード時に権限をリセットする処理を調べるとき。
- 呼び出し先: `browser.reload()`, `lazy.SitePermissions.clearTemporaryBlockPermissions()`, `this.documentGlobal.gIdentityHandler.hidePopup()`, `this.documentGlobal.gPermissionPanel.hidePopup()`, `this.getBrowserForTab()`
- 参照: `browser.authPromptAbuseCounter`

## Tabbrowser.addProgressListener()
- 位置: L7688-7700
- 役割: 選択 browser 用の進捗リスナーを登録する。引数が 2 つ以上だとエラーを記録する。
- 触るとき: 選択タブの進捗通知を購読する拡張点を調べるとき。
- 呼び出し先: `this.#progressListeners.push()`
- 条件付き依存: `if (arguments.length != 1)` → `console.error()`
- 参照: `arguments.length`, `new Error().stack`

## Tabbrowser.removeProgressListener()
- 位置: L7708-7712
- 役割: 登録済みの進捗リスナーを外す。
- 触るとき: 選択タブの進捗の購読解除を調べるとき。
- 呼び出し先: `this.#progressListeners.filter()`
- 参照: `this.#progressListeners`

## Tabbrowser.addTabsProgressListener()
- 位置: L7723-7725
- 役割: 全タブの進捗を受けるリスナーを登録する。
- 触るとき: 全タブの進捗通知を購読する拡張点を調べるとき。
- 呼び出し先: `this.#tabsProgressListeners.push()`

## Tabbrowser.removeTabsProgressListener()
- 位置: L7733-7737
- 役割: 全タブ用の進捗リスナーを外す。
- 触るとき: 全タブの進捗の購読解除を調べるとき。
- 呼び出し先: `this.#tabsProgressListeners.filter()`
- 参照: `this.#tabsProgressListeners`

## Tabbrowser.getBrowserForTab()
- 位置: L7739-7741
- 役割: タブの linkedBrowser を返す。
- 触るとき: タブから browser を引く経路を調べるとき。
- 参照: `aTab.linkedBrowser`

## Tabbrowser.showTab()
- 位置: L7743-7771
- 役割: 非表示のタブを再表示し、TabShow を送って hiddenBy を消す。分割ビューは全体を表示する。
- 触るとき: タブの再表示や分割ビューとの連動を調べるとき。
- 呼び出し先: `aTab.dispatchEvent()`, `aTab.removeAttribute()`, `event.initEvent()`, `lazy.SessionStore.deleteCustomTabValue()`, `this.document.createEvent()`, `this.tabContainer._invalidateCachedVisibleTabs()`, `this.tabContainer._updateCloseButtons()`
- 条件付き依存: `if (aTab.multiselected)` → `this.#updateMultiselectedTabCloseButtonTooltip()`
- 条件付き依存: `if (sibling != aTab)` → `this.showTab()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.toggleAttribute()`
- 参照: `aTab.hidden`, `aTab.multiselected`, `aTab.splitview`, `aTab.splitview.tabs`, `this.documentGlobal.FirefoxViewHandler.tab`

## Tabbrowser.hideTab()
- 位置: L7773-7820
- 役割: ピン留め、選択中、共有中などでなければタブを隠して TabHide を送り、分割ビューは全体を隠す。
- 触るとき: タブを隠せる条件や、隠した際の後処理を調べるとき。
- 呼び出し先: `aTab.dispatchEvent()`, `aTab.setAttribute()`, `event.initEvent()`, `this.document.createEvent()`, `this.getSuccessor()`, `this.replaceInSuccession()`, `this.setSuccessor()`, `this.tabContainer._invalidateCachedVisibleTabs()`, `this.tabContainer._updateCloseButtons()`
- 条件付き依存: `if (aTab.multiselected)` → `this.#updateMultiselectedTabCloseButtonTooltip()`
- 条件付き依存: `if (aSource)` → `lazy.SessionStore.setCustomTabValue()`
- 条件付き依存: `if (sibling != aTab)` → `this.hideTab()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.toggleAttribute()`
- 参照: `aTab.closing`, `aTab.hidden`, `aTab.linkedBrowser._sharingState?.webRTC?.sharing`, `aTab.multiselected`, `aTab.pinned`, `aTab.selected`, `aTab.splitview`, `aTab.splitview.tabs`

## Tabbrowser.selectTabAtIndex()
- 位置: L7834-7855
- 役割: 表示中タブの添字 (負なら末尾から、範囲外は端に丸める) で選択し、イベントがあれば消費する。
- 触るとき: 番号キーなどによるタブ選択の規則を調べるとき。
- 呼び出し先: `this.setSelectedTab()`
- 条件付き依存: `if (event)` → `event.preventDefault()`
- 条件付き依存: `if (event)` → `event.stopPropagation()`
- 参照: `tabs.length`, `this.visibleTabs`

## Tabbrowser.replaceTabWithWindow()
- 位置: L7867-7896
- 役割: タブ、グループ、分割ビューを新しいウィンドウに引き渡して開く。唯一のタブなら何もしない。
- 触るとき: タブを新しいウィンドウに切り出す処理を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Object.entries()`, `Object.entries(features) .map()`, `Object.entries(features) .map(([key, value]) => `${key}=${value}`) .join()`, `Tabbrowser.isTab()`, `args.appendElement()`, `lazy.BrowserWindowTracker.openWindow()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (this.tabs.length == 1)` → `this.addTrustedTab()`
- 条件付き依存: `if (!this.documentGlobal.gReduceMotion && Tabbrowser.isTab(aTab))` → `aTab.removeAttribute()`
- 参照: `Ci.nsIMutableArray`, `aTab.splitview`, `aTab.style.maxWidth`, `this.documentGlobal`, `this.documentGlobal.BROWSER_NEW_TAB_URL`, `this.documentGlobal.gReduceMotion`, `this.tabs.length`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1`

## Tabbrowser.replaceTabsWithWindow()
- 位置: L7908-7992
- 役割: コンテキストタブまたは複数選択のタブ群を新ウィンドウに移し、採用後に選択状態を復元する。
- 触るとき: 複数タブを新ウィンドウに移す処理や選択の復元を調べるとき。
- 呼び出し先: `Tabbrowser.isTabGroupLabel()`, `elements.includes()`, `this.recordTabMetrics()`, `this.replaceTabWithWindow()`, `win.addEventListener()`, `win.gBrowser.addRangeToMultiSelectedTabs()`, `win.gBrowser.lockClearMultiSelectionOnce()`
- 条件付き依存: `if (Tabbrowser.isTabGroupLabel(contextTab))` → `this.replaceTabWithWindow()`
- 条件付き依存: `if (elements.length == 1)` → `this.replaceTabWithWindow()`
- 条件付き依存: `if (!this.documentGlobal.gReduceMotion)` → `element.removeAttribute()`
- 条件付き依存: `if ( !elements.includes(selectedTab) && !elements.includes(selectedTab.splitview) )` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (element !== selectedTab && element !== selectedTab.splitview)` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (element !== selectedTab && element !== selectedTab.splitview)` → `win.gBrowser.adoptSplitView()`
- 条件付き依存: `if (element !== selectedTab && element !== selectedTab.splitview)` → `win.gBrowser.adoptTab()`
- 条件付き依存: `if (!newTab)` → `element.setAttribute()`
- 参照: `contextTab.multiselected`, `contextTab.splitview`, `element.style.maxWidth`, `elements.length`, `elements[0].tabs`, `options.metricsContext`, `selectedTab.splitview`, `this.TabMetrics.METRIC_ACTION.DETACH`, `this.documentGlobal.gReduceMotion`, `this.selectedElements`, `this.tabs.length`, `win.gBrowser.visibleTabs`, `winVisibleTabs.length`

## Tabbrowser.replaceGroupWithWindow()
- 位置: L8003-8010
- 役割: DETACH を記録して、グループを新しいウィンドウに移す。
- 触るとき: グループを新ウィンドウに移す操作を調べるとき。
- 呼び出し先: `this.recordTabMetrics()`, `this.replaceTabWithWindow()`
- 参照: `group.tabs.length`, `this.TabMetrics.METRIC_ACTION.DETACH`

## Tabbrowser.isTab()
- 位置: L8018-8020
- 役割: 要素が tab かを返す静的メソッド。
- 触るとき: 要素の種類の判定を調べるとき。
- 参照: `element?.tagName`

## Tabbrowser.isTabGroup()
- 位置: L8028-8030
- 役割: 要素が tab-group かを返す静的メソッド。
- 触るとき: 要素の種類の判定を調べるとき。
- 参照: `element?.tagName`

## Tabbrowser.isTabGroupLabel()
- 位置: L8038-8040
- 役割: 要素がタブグループのラベルかを返す静的メソッド。
- 触るとき: 要素の種類の判定を調べるとき。
- 呼び出し先: `element?.classList?.contains()`

## Tabbrowser.isSplitViewWrapper()
- 位置: L8048-8050
- 役割: 要素が分割ビューのラッパーかを返す静的メソッド。
- 触るとき: 要素の種類の判定を調べるとき。
- 参照: `element?.tagName`

## Tabbrowser.#updateTabsAfterInsert()
- 位置: L8052-8074
- 役割: 各タブの _index を振り直し、選択を解除してから選択中のタブだけ選択状態に戻す。
- 触るとき: タブの挿入や移動後に位置情報と選択状態を整える処理を調べるとき。
- 参照: `this.selectedTab._selected`, `this.tabs`, `this.tabs.length`, `this.tabs[i]._index`, `this.tabs[i]._selected`

## Tabbrowser.moveTabTo()
- 位置: L8094-8171
- 役割: 要素 (タブ、グループ、分割ビュー) を指定位置へ移す。ピンと通常タブの混在を防ぎ、グループ指定の扱いを調整する。
- 触るとき: タブの位置指定による移動の規則を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`, `Tabbrowser.isTabGroup()`, `Tabbrowser.isTabGroupLabel()`, `this.#handleTabMove()`
- 条件付き依存: `if (typeof elementIndex == "number")` → `this.#elementIndexToTabIndex()`
- 条件付き依存: `if (Tabbrowser.isTab(element) && element.pinned)` → `Math.min()`
- 条件付き依存: `if (!(Tabbrowser.isTab(element) && element.pinned))` → `Math.max()`
- 条件付き依存: `if (movingForwards)` → `Math.min()`
- 条件付き依存: `if (movingForwards && neighbor)` → `neighbor.after()`
- 条件付き依存: `if (!(movingForwards && neighbor))` → `this.tabContainer.insertBefore()`
- 参照: `element.group`, `element.index`, `element.pinned`, `element.splitview`, `element.tabs`, `neighbor.group`, `neighbor.splitview`, `neighbor?.group`, `neighbor?.splitview`, `tabsInElement.length`, `tabsInElement[0].index`, `this.pinnedTabCount`, `this.tabs`, `this.tabs.length`

## Tabbrowser.moveTabBefore()
- 位置: L8181-8183
- 役割: 要素を対象要素の前へ移す (#moveTabNextTo への委譲)。
- 触るとき: 相対位置によるタブ移動の入口を調べるとき。
- 呼び出し先: `this.#moveTabNextTo()`

## Tabbrowser.moveTabsBefore()
- 位置: L8192-8194
- 役割: 複数の要素を対象要素の前へ移す。
- 触るとき: 複数タブの相対位置移動の入口を調べるとき。
- 呼び出し先: `this.#moveTabsNextTo()`

## Tabbrowser.moveTabAfter()
- 位置: L8204-8206
- 役割: 要素を対象要素の後ろへ移す (#moveTabNextTo への委譲)。
- 触るとき: 相対位置によるタブ移動の入口を調べるとき。
- 呼び出し先: `this.#moveTabNextTo()`

## Tabbrowser.moveTabsAfter()
- 位置: L8215-8217
- 役割: 複数の要素を対象要素の後ろへ移す。
- 触るとき: 複数タブの相対位置移動の入口を調べるとき。
- 呼び出し先: `this.#moveTabsNextTo()`

## Tabbrowser.#moveTabNextTo()
- 位置: L8230-8298
- 役割: 対象の隣へ要素を移す。グループラベルの扱い、ピンと通常の境界、分割ビューを調整して移動する。
- 触るとき: タブ移動時のグループ・ピン・分割ビューの境界処理を調べるとき。
- 呼び出し先: `Tabbrowser.isTabGroupLabel()`, `this.#handleTabMove()`
- 条件付き依存: `if (moveBefore)` → `getContainer().insertBefore()`
- 条件付き依存: `if (moveBefore)` → `getContainer()`
- 条件付き依存: `if (targetElement)` → `targetElement.after()`
- 条件付き依存: `if (!(targetElement))` → `getContainer().appendChild()`
- 条件付き依存: `if (!(targetElement))` → `getContainer()`
- 参照: `element.group`, `element.pinned`, `element.splitview`, `targetElement.collapsed`, `targetElement.group`, `targetElement.pinned`, `targetElement.splitview`, `targetElement.tabs`, `targetElement?.group`, `targetElement?.pinned`, `targetElement?.splitview`, `this.pinnedTabCount`, `this.tabs`

## getContainer()
- 位置: L8280-8283
- 役割: 要素がピン留めならピン用、そうでなければ通常のタブコンテナを返すローカル関数。
- 触るとき: 移動先のコンテナの選択を調べるとき。
- 参照: `element.pinned`, `this.tabContainer`, `this.tabContainer.pinnedTabsContainer`

## Tabbrowser.#moveTabsNextTo()
- 位置: L8308-8326
- 役割: 複数要素の移動をまとめて MOVE として記録し、先頭を対象の隣に、残りを直前の要素の後ろに移す。
- 触るとき: 複数タブ移動の記録と順序を調べるとき。
- 呼び出し先: `this.#moveTabNextTo()`, `this.TabMetrics.decomposedContext()`, `this.recordTabMetrics()`
- 参照: `elements.length`, `this.TabMetrics.METRIC_ACTION.MOVE`

## Tabbrowser.moveTabToSplitView()
- 位置: L8334-8358
- 役割: ピン留めでないタブを分割ビューに移し、複数選択から外す。
- 触るとき: タブを既存の分割ビューに加える処理を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`, `aSplitViewWrapper.appendChild()`, `aSplitViewWrapper.insertBefore()`, `this.#handleTabMove()`, `this.removeFromMultiSelectedTabs()`, `this.tabContainer._notifyBackgroundTab()`
- 参照: `aSplitViewWrapper.splitViewId`, `aSplitViewWrapper.tabs`, `aTab.pinned`, `aTab.splitview`, `aTab.splitview.splitViewId`

## Tabbrowser.moveTabToExistingGroup()
- 位置: L8368-8396
- 役割: ピン留めでないタブ (分割ビュー所属なら分割ビューごと) を既存グループに追加し、複数選択から外す。
- 触るとき: タブを既存グループへ入れる処理を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`
- 条件付き依存: `if (aTab.splitview)` → `this.#handleTabMove()`
- 条件付き依存: `if (aTab.splitview)` → `aGroup.appendChild()`
- 条件付き依存: `if (aTab.splitview)` → `this.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (aTab.splitview)` → `this.tabContainer._notifyBackgroundTab()`
- 条件付き依存: `if (!(aTab.splitview))` → `this.#handleTabMove()`
- 条件付き依存: `if (!(aTab.splitview))` → `aGroup.appendChild()`
- 条件付き依存: `if (!(aTab.splitview))` → `this.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (!(aTab.splitview))` → `this.tabContainer._notifyBackgroundTab()`
- 参照: `aGroup.id`, `aTab.group`, `aTab.group.id`, `aTab.pinned`, `aTab.splitview`, `aTab.splitview.tabs`

## Tabbrowser.moveSplitViewToExistingGroup()
- 位置: L8406-8426
- 役割: 分割ビューを既存グループの末尾に移し、含まれるタブを複数選択から外す。
- 触るとき: 分割ビューを既存グループへ入れる処理を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `aGroup.appendChild()`, `this.#handleTabMove()`, `this.removeFromMultiSelectedTabs()`, `this.tabContainer._notifyBackgroundTab()`
- 参照: `aGroup.id`, `aSplitView.group`, `aSplitView.group.id`, `aSplitView.tabs`

## Tabbrowser.#getTabMoveState()
- 位置: L8445-8463
- 役割: タブの位置、グループ ID、分割ビュー ID を TabMove 通知用の状態として返す。
- 触るとき: TabMove の通知に含まれる状態を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`
- 参照: `state.elementIndex`, `state.splitViewId`, `state.tabGroupId`, `tab.elementIndex`, `tab.group`, `tab.group.id`, `tab.index`, `tab.splitview`, `tab.splitview.splitViewId`, `tab.visible`

## Tabbrowser.#notifyOnTabMove()
- 位置: L8473-8510
- 役割: 位置、グループ、分割ビューのいずれかが変わっていれば TabMove を送り、移動を記録する。
- 触るとき: TabMove の送出条件や detail を変えるとき。
- 呼び出し先: `Tabbrowser.isTab()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `tab.dispatchEvent()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `Tabbrowser.#tabsLeavingAdoptedSplitView.has()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `Tabbrowser.#tabsJoiningAdoptedSplitView.has()`
- 条件付き依存: `if (changedPosition || changedTabGroup || changedSplitView)` → `this.recordTabMetrics()`
- 参照: `currentTabState.splitViewId`, `currentTabState.tabGroupId`, `currentTabState.tabIndex`, `previousTabState.splitViewId`, `previousTabState.tabGroupId`, `previousTabState.tabIndex`, `this.TabMetrics.METRIC_ACTION.MOVE`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this.documentGlobal.CustomEvent`

## Tabbrowser.handleTabMove()
- 位置: L8519-8521
- 役割: #handleTabMove を呼ぶ公開ラッパー。
- 触るとき: 外部から移動処理を包んで通知させる経路を調べるとき。
- 呼び出し先: `this.#handleTabMove()`

## Tabbrowser.#handleTabMove()
- 位置: L8530-8597
- 役割: 移動前後のタブ状態を記録して移動用コールバックを実行し、キャッシュ無効化と選択の整え、TabMove、TabGroupMoved の送出を行う。
- 触るとき: タブ移動の共通処理や通知の順序を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`, `Tabbrowser.isTabGroup()`, `moveActionCallback()`, `tabs.map()`, `this.#getTabMoveState()`, `this.#notifyOnTabMove()`, `this.#updateTabsAfterInsert()`, `this.tabContainer._invalidateCachedTabs()`
- 条件付き依存: `if (!( Tabbrowser.isTab(element) && element.splitview?.shouldMoveAllTabsAtOnce ))` → `Tabbrowser.isTab()`
- 条件付き依存: `if (!(Tabbrowser.isTab(element)))` → `Tabbrowser.isTabGroup()`
- 条件付き依存: `if (!(Tabbrowser.isTab(element)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (wasFocused)` → `this.selectedTab.focus()`
- 条件付き依存: `if (tab.selected)` → `this.tabContainer._handleTabSelect()`
- 条件付き依存: `if ( Tabbrowser.isTabGroup(element) && previousTabStates[0].tabIndex != currentFirst.tabIndex )` → `element.dispatchEvent()`
- 参照: `currentFirst.tabIndex`, `element.splitview.tabs`, `element.splitview?.shouldMoveAllTabsAtOnce`, `element.tabs`, `previousTabStates[0].tabIndex`, `tab.selected`, `tabs.length`, `tabs[0].index`, `this.#lastRelatedTabMap`, `this.document.activeElement`, `this.documentGlobal.CustomEvent`, `this.selectedTab`

## Tabbrowser.adoptTab()
- 位置: L8615-8676
- 役割: 別ウィンドウのタブを、新タブを作って browser を入れ替え、元のタブを閉じることで取り込む。失敗時は null を返す。
- 触るとき: ウィンドウ間のタブのドラッグ移動を調べるとき。
- 呼び出し先: `Tabbrowser.isTab()`, `aTab.container.tabDragAndDrop.finishAnimateTabMove()`, `aTab.hasAttribute()`, `this.addWebTab()`, `this.swapBrowsersAndCloseOther()`
- 条件付き依存: `if (typeof elementIndex == "number")` → `this.tabContainer.dragAndDropElements.at()`
- 条件付き依存: `if (!(typeof elementIndex == "number"))` → `this.tabs.at()`
- 条件付き依存: `if (aTab.hasAttribute("usercontextid"))` → `aTab.getAttribute()`
- 条件付き依存: `if (!this.swapBrowsersAndCloseOther(newTab, aTab))` → `this.removeTab()`
- 条件付き依存: `if (tabInGroup)` → `Glean.tabgroup.tabInteractions.remove_other_window.add()`
- 参照: `aTab.group`, `aTab.linkedBrowser`, `aTab.linkedPanel`, `aTab.pinned`, `linkedBrowser.browsingContext?.group.id`, `linkedBrowser.remoteType`, `nextElement.group`, `params.pinned`, `params.skipLoad`, `params.userContextId`, `this.pinnedTabCount`, `this.selectedTab`

## Tabbrowser.moveTabForward()
- 位置: L8687-8727
- 役割: 選択中のタブ (または分割ビュー) を 1 つ後ろへ動かす。折りたたみグループは飛び越え、展開グループには入る。
- 触るとき: キーボードによるタブの前後移動の規則を変えるとき。
- 呼び出し先: `this.tabContainer.findNextTab()`
- 条件付き依存: `if (nextTab)` → `this.#handleTabMove()`
- 条件付き依存: `if (nextTabOrSplitview.group.collapsed)` → `nextTabOrSplitview.group.after()`
- 条件付き依存: `if (!(nextTabOrSplitview.group.collapsed))` → `nextTabOrSplitview.group.insertBefore()`
- 条件付き依存: `if (selectedTab.group != nextTab.group)` → `selectedTab.group.after()`
- 条件付き依存: `if (!(selectedTab.group != nextTab.group))` → `nextTabOrSplitview.after()`
- 条件付き依存: `if (selectedTab.group)` → `selectedTab.group.after()`
- 参照: `nextTab.group`, `nextTab?.splitview`, `nextTabOrSplitview.group.collapsed`, `selectedTab.group`, `selectedTab.splitview`, `selectedTab.splitview?.lastElementChild`

## filter()
- 位置: L8694-8694
- 役割: 非表示でなく、選択タブとピン状態が同じタブだけを通すフィルタ。
- 触るとき: 前進移動の対象タブの絞り込みを調べるとき。
- 参照: `selectedTab.pinned`, `tab.hidden`, `tab.pinned`

## Tabbrowser.moveTabBackward()
- 位置: L8738-8775
- 役割: 選択中のタブ (または分割ビュー) を 1 つ前へ動かす。折りたたみグループは飛び越え、展開グループには入る。
- 触るとき: キーボードによるタブの前後移動の規則を変えるとき。
- 呼び出し先: `this.tabContainer.findNextTab()`
- 条件付き依存: `if (previousTab)` → `this.#handleTabMove()`
- 条件付き依存: `if (previousTab.group.collapsed)` → `previousTab.group.before()`
- 条件付き依存: `if (!(previousTab.group.collapsed))` → `previousTab.group.append()`
- 条件付き依存: `if (selectedTab.group != previousTab.group)` → `selectedTab.group.before()`
- 条件付き依存: `if (!(selectedTab.group != previousTab.group))` → `previousTabOrSplitview.before()`
- 条件付き依存: `if (selectedTab.group)` → `selectedTab.group.before()`
- 参照: `previousTab.group`, `previousTab.group.collapsed`, `previousTab?.splitview`, `selectedTab.group`, `selectedTab.splitview`, `selectedTab.splitview?.firstElementChild`

## filter()
- 位置: L8745-8745
- 役割: 非表示でなく、選択タブとピン状態が同じタブだけを通すフィルタ。
- 触るとき: 後退移動の対象タブの絞り込みを調べるとき。
- 参照: `selectedTab.pinned`, `tab.hidden`, `tab.pinned`

## Tabbrowser.moveTabToStart()
- 位置: L8787-8793
- 役割: タブを (グループ外の) 先頭位置へ移す。
- 触るとき: 先頭へ移動の挙動を調べるとき。
- 呼び出し先: `this.moveTabTo()`
- 参照: `this.selectedTab`

## Tabbrowser.moveTabToEnd()
- 位置: L8805-8811
- 役割: タブを (グループ外の) 末尾位置へ移す。
- 触るとき: 末尾へ移動の挙動を調べるとき。
- 呼び出し先: `this.moveTabTo()`
- 参照: `this.selectedTab`, `this.tabs.length`

## Tabbrowser.duplicateTab()
- 位置: L8823-8835
- 役割: SessionStore.duplicateTab でタブを複製し、グループ内なら記録する。
- 触るとき: タブの複製の経路を調べるとき。
- 呼び出し先: `lazy.SessionStore.duplicateTab()`
- 条件付き依存: `if (aTab.group)` → `Glean.tabgroup.tabInteractions.duplicate.add()`
- 参照: `aTab.group`, `this.documentGlobal`

## Tabbrowser.#updateMultiselectedTabCloseButtonTooltip()
- 位置: L8846-8862
- 役割: 複数選択タブの閉じるボタンに選択数を渡し、選択から外れたタブは 1 に戻す。
- 触るとき: 複数選択時の閉じるボタンの読み上げ/文言を調べるとき。
- 呼び出し先: `aTabsRemovedFromMultiselection?.forEach()`, `selectedTab.querySelector()`, `selectedTabs.forEach()`, `this.document.l10n.setArgs()`, `unselectedTab.querySelector()`
- 参照: `args.tabCount`, `selectedTabs.length`

## Tabbrowser.addToMultiSelectedTabs()
- 位置: L8872-8896
- 役割: タブを複数選択に加え属性を設定する。分割ビューは構成タブすべてを対象にし、変更は後でまとめて処理する。
- 触るとき: 複数選択への追加処理を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `aTab.setAttribute()`, `this.#multiSelectChangeRemovals.delete()`, `this.#multiSelectedTabsSet.add()`, `this.#startMultiSelectChange()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(aTab))` → `this.addToMultiSelectedTabs()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.setAttribute()`
- 条件付き依存: `if (!this.#multiSelectChangeRemovals.delete(aTab))` → `this.#multiSelectChangeAdditions.add()`
- 参照: `aTab.multiselected`, `aTab.splitview`, `aTab.tabs`

## Tabbrowser.addRangeToMultiSelectedTabs()
- 位置: L8904-8921
- 役割: 表示中タブの中で 2 つのタブの間をすべて複数選択に加える。
- 触るとき: Shift 選択などの範囲選択の処理を調べるとき。
- 呼び出し先: `Math.max()`, `tabs.indexOf()`, `this.addToMultiSelectedTabs()`
- 参照: `this.visibleTabs`

## Tabbrowser.removeFromMultiSelectedTabs()
- 位置: L8931-8948
- 役割: タブを複数選択から外して属性を消し、変更を記録する。
- 触るとき: 複数選択からの除外処理を調べるとき。
- 呼び出し先: `aTab.removeAttribute()`, `this.#multiSelectChangeAdditions.delete()`, `this.#multiSelectedTabsSet.delete()`, `this.#startMultiSelectChange()`
- 条件付き依存: `if (aTab.splitview)` → `aTab.splitview.removeAttribute()`
- 条件付き依存: `if (!this.#multiSelectChangeAdditions.delete(aTab))` → `this.#multiSelectChangeRemovals.add()`
- 参照: `aTab.multiselected`, `aTab.splitview`

## Tabbrowser.clearMultiSelectedTabs()
- 位置: L8950-8967
- 役割: ロック中でなければ、複数選択を全て解除する。
- 触るとき: 複数選択の解除と、そのロックの扱いを調べるとき。
- 呼び出し先: `this.removeFromMultiSelectedTabs()`
- 参照: `this.#clearMultiSelectionLocked`, `this.#clearMultiSelectionLockedOnce`, `this.#lastMultiSelectedTabRef`, `this.multiSelectedTabsCount`, `this.selectedTabs`

## Tabbrowser.selectAllTabs()
- 位置: L8969-8975
- 役割: 表示中の全タブを複数選択にする。
- 触るとき: すべてのタブを選択する操作を調べるとき。
- 呼び出し先: `this.addRangeToMultiSelectedTabs()`
- 参照: `this.visibleTabs`, `visibleTabs.length`

## Tabbrowser.allTabsSelected()
- 位置: L8977-8982
- 役割: 表示中タブが 1 つ、または全て複数選択済みかを返す。
- 触るとき: 全選択済みの判定を調べるとき。
- 呼び出し先: `this.visibleTabs.every()`
- 参照: `t.multiselected`, `this.visibleTabs.length`

## Tabbrowser.lockClearMultiSelectionOnce()
- 位置: L8984-8987
- 役割: 次の 1 回だけ複数選択の解除を抑止するロックを掛ける。
- 触るとき: ウィンドウ間移動直後などで選択を保つ処理を調べるとき。
- 参照: `this.#clearMultiSelectionLocked`, `this.#clearMultiSelectionLockedOnce`

## Tabbrowser.unlockClearMultiSelection()
- 位置: L8989-8992
- 役割: 複数選択解除のロックを解除する。
- 触るとき: 複数選択解除のロックの解除経路を調べるとき。
- 参照: `this.#clearMultiSelectionLocked`, `this.#clearMultiSelectionLockedOnce`

## Tabbrowser.#avoidSingleSelectedTab()
- 位置: L9020-9024
- 役割: 複数選択が 1 つだけ残った場合に選択を解除する。
- 触るとき: 複数選択が 1 つになったときの扱いを調べるとき。
- 条件付き依存: `if (this.multiSelectedTabsCount == 1)` → `this.clearMultiSelectedTabs()`
- 参照: `this.multiSelectedTabsCount`

## Tabbrowser.#switchToNextMultiSelectedTab()
- 位置: L9026-9045
- 役割: 選択解除の影響を避けつつ、最後に選んだタブか複数選択の最後のタブへ切り替える。
- 触るとき: 選択中タブが複数選択から外れたときの切り替えを調べるとき。
- 呼び出し先: `console.error()`
- 条件付き依存: `if (!(!lastMultiSelectedTab.selected))` → `ChromeUtils.nondeterministicGetWeakSetKeys( this.#multiSelectedTabsSet ).filter()`
- 条件付き依存: `if (!(!lastMultiSelectedTab.selected))` → `ChromeUtils.nondeterministicGetWeakSetKeys()`
- 条件付き依存: `if (!(!lastMultiSelectedTab.selected))` → `selectedTabs.at()`
- 参照: `Tabbrowser.#mayTabBeMultiselected`, `lastMultiSelectedTab.selected`, `this.#clearMultiSelectionLocked`, `this.#multiSelectedTabsSet`, `this.lastMultiSelectedTab`, `this.selectedTab`

## Tabbrowser.selectedTabs()
- 位置: L9047-9055
- 役割: 複数選択をクリアし、先頭を選択タブにして、2 つ以上なら全て複数選択に加えるセッター。
- 触るとき: gBrowser.selectedTabs への代入の挙動を調べるとき。
- 呼び出し先: `this.clearMultiSelectedTabs()`
- 条件付き依存: `if (tabs.length > 1)` → `this.addToMultiSelectedTabs()`
- 参照: `tabs.length`, `this.selectedTab`

## Tabbrowser.selectedTabs()
- 位置: L9057-9070
- 役割: 複数選択中のタブ、無ければ選択タブを、位置順に並べて返すゲッター。
- 触るとき: 選択中のタブ群の取得元を調べるとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `ChromeUtils.nondeterministicGetWeakSetKeys( this.#multiSelectedTabsSet ).filter()`, `Tabbrowser.#mayTabBeMultiselected()`, `tabs.sort()`, `this.#multiSelectedTabsSet.has()`
- 条件付き依存: `if ( (!this.#multiSelectedTabsSet.has(selectedTab) && Tabbrowser.#mayTabBeMultiselected(selectedTab)) || !tabs.length )` → `tabs.push()`
- 参照: `Tabbrowser.#mayTabBeMultiselected`, `a.index`, `b.index`, `tabs.length`, `this.#multiSelectedTabsSet`

## Tabbrowser.selectedElements()
- 位置: L9080-9086
- 役割: 選択中のタブを、分割ビューに属するものは分割ビューにまとめた要素の配列で返す。
- 触るとき: ドラッグ対象となる要素単位の選択を扱うとき。
- 呼び出し先: `Array.from()`, `selectedElements.add()`, `selectedElements.values()`
- 参照: `selectedTab.splitview`, `this.selectedTabs`

## Tabbrowser.multiSelectedTabsCount()
- 位置: L9088-9092
- 役割: 複数選択されている表示中タブの数を返す。
- 触るとき: 複数選択の件数の取得元を調べるとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakSetKeys()`, `ChromeUtils.nondeterministicGetWeakSetKeys( this.#multiSelectedTabsSet ).filter()`
- 参照: `Tabbrowser.#mayTabBeMultiselected`, `this.#multiSelectedTabsSet`

## Tabbrowser.lastMultiSelectedTab()
- 位置: L9094-9104
- 役割: 最後に複数選択に加えたタブを返す。無効なら選択中のタブに置き換える。
- 触るとき: 範囲選択の起点となるタブの取得を調べるとき。
- 呼び出し先: `this.#lastMultiSelectedTabRef.get()`, `this.#multiSelectedTabsSet.has()`
- 参照: `tab.isConnected`, `this.#lastMultiSelectedTabRef`, `this.lastMultiSelectedTab`, `this.selectedTab`

## Tabbrowser.lastMultiSelectedTab()
- 位置: L9106-9108
- 役割: 最後に複数選択したタブを弱参照で保持するセッター。
- 触るとき: 範囲選択の起点の保持方法を調べるとき。
- 呼び出し先: `Cu.getWeakReference()`
- 参照: `this.#lastMultiSelectedTabRef`

## Tabbrowser.#mayTabBeMultiselected()
- 位置: L9110-9112
- 役割: タブが表示中なら複数選択の対象になりうると返す。
- 触るとき: 複数選択できるタブの条件を調べるとき。
- 参照: `aTab.visible`

## Tabbrowser.#startMultiSelectChange()
- 位置: L9114-9119
- 役割: 複数選択の変更をマイクロタスクでまとめて処理するよう予約する。
- 触るとき: 複数選択の変更を一括処理する仕組みを調べるとき。
- 条件付き依存: `if (!this.#multiSelectChangeStarted)` → `Promise.resolve().then()`
- 条件付き依存: `if (!this.#multiSelectChangeStarted)` → `Promise.resolve()`
- 条件付き依存: `if (!this.#multiSelectChangeStarted)` → `this.#endMultiSelectChange()`
- 参照: `this.#multiSelectChangeStarted`

## Tabbrowser.#endMultiSelectChange()
- 位置: L9121-9153
- 役割: 予約済みの追加と除外を確定し、閉じるボタンの文言を更新して TabMultiSelect を送る。
- 触るとき: 複数選択の変更確定後の処理や通知を変えるとき。
- 条件付き依存: `if (!selectedTab.multiselected)` → `this.addToMultiSelectedTabs()`
- 条件付き依存: `if (this.#multiSelectChangeRemovals.size)` → `this.#multiSelectChangeRemovals.has()`
- 条件付き依存: `if (this.#multiSelectChangeRemovals.has(selectedTab))` → `this.#switchToNextMultiSelectedTab()`
- 条件付き依存: `if (this.#multiSelectChangeRemovals.size)` → `this.#avoidSingleSelectedTab()`
- 条件付き依存: `if (noticeable)` → `this.#updateMultiselectedTabCloseButtonTooltip()`
- 条件付き依存: `if (noticeable || this.#multiSelectChangeSelected)` → `this.#multiSelectChangeAdditions.clear()`
- 条件付き依存: `if (noticeable || this.#multiSelectChangeSelected)` → `this.#multiSelectChangeRemovals.clear()`
- 条件付き依存: `if (noticeable || this.#multiSelectChangeSelected)` → `this.tabContainer.dispatchEvent()`
- 参照: `selectedTab.multiselected`, `this.#multiSelectChangeAdditions.size`, `this.#multiSelectChangeRemovals`, `this.#multiSelectChangeRemovals.size`, `this.#multiSelectChangeSelected`, `this.#multiSelectChangeStarted`, `this.documentGlobal.CustomEvent`

## Tabbrowser.toggleMuteAudioOnMultiSelectedTabs()
- 位置: L9155-9163
- 役割: 選択中のうち、指定タブと同じミュート状態のタブすべてのミュートを切り替える。
- 触るとき: 複数選択でのミュート切り替えを調べるとき。
- 呼び出し先: `tab.toggleMuteAudio()`, `this.selectedTabs.filter()`
- 参照: `aTab.linkedBrowser.audioMuted`, `tab.linkedBrowser.audioMuted`

## Tabbrowser.resumeDelayedMediaOnMultiSelectedTabs()
- 位置: L9165-9169
- 役割: 選択中の各タブで、保留中のメディア再生を再開する。
- 触るとき: 複数選択での再生再開の経路を調べるとき。
- 呼び出し先: `tab.resumeDelayedMedia()`
- 参照: `this.selectedTabs`

## Tabbrowser.pinMultiSelectedTabs()
- 位置: L9179-9191
- 役割: 選択中のタブをまとめてピン留めし、PIN を記録する。
- 触るとき: 複数選択のピン留め操作を調べるとき。
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.pinTab()`, `this.recordTabMetrics()`
- 参照: `tabs.length`, `this.TabMetrics.METRIC_ACTION.PIN`, `this.TabMetrics.UNKNOWN_CONTEXT`, `this.selectedTabs`

## Tabbrowser.unpinMultiSelectedTabs()
- 位置: L9200-9213
- 役割: 選択中のタブを、表示順を保つよう逆順にピン解除し、UNPIN を記録する。
- 触るとき: 複数選択のピン解除と順序の保持を調べるとき。
- 呼び出し先: `this.TabMetrics.decomposedContext()`, `this.recordTabMetrics()`, `this.unpinTab()`
- 参照: `selectedTabs.length`, `this.TabMetrics.METRIC_ACTION.UNPIN`, `this.selectedTabs`

## Tabbrowser.activateBrowserForPrintPreview()
- 位置: L9215-9221
- 役割: 印刷プレビュー用に browser を登録し、docShell を有効にする。
- 触るとき: 印刷プレビュー中の browser の有効化を調べるとき。
- 呼び出し先: `this._printPreviewBrowsers.add()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.activateBrowserForPrintPreview()`
- 参照: `aBrowser.docShellIsActive`, `this._switcher`

## Tabbrowser.deactivatePrintPreviewBrowsers()
- 位置: L9223-9229
- 役割: 印刷プレビュー用の登録を解除し、docShell の有効状態を再計算する。
- 触るとき: 印刷プレビュー終了時の後始末を調べるとき。
- 呼び出し先: `this.shouldActivateDocShell()`
- 参照: `browser.docShellIsActive`, `this._printPreviewBrowsers`

## Tabbrowser.shouldActivateDocShell()
- 位置: L9236-9246
- 役割: browser の docShell を有効にすべきかを、スイッチャーまたは選択、印刷、PiP、分割ビューから判定する。
- 触るとき: どの browser の docShell を有効にするかの規則を変えるとき。
- 呼び出し先: `lazy.PictureInPicture.isOriginatingBrowser()`, `this._printPreviewBrowsers.has()`, `this.splitViewBrowsers.includes()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.shouldActivateDocShell()`
- 参照: `this._switcher`, `this.document.hidden`, `this.selectedBrowser`

## Tabbrowser._getSwitcher()
- 位置: L9248-9253
- 役割: AsyncTabSwitcher を遅延作成して返す。
- 触るとき: 非同期タブ切り替えの生成箇所を調べるとき。
- 参照: `lazy.AsyncTabSwitcher`, `this._switcher`

## Tabbrowser.warmupTab()
- 位置: L9255-9259
- 役割: マルチプロセス時のみ、スイッチャーでタブをウォームアップする。
- 触るとき: タブ切り替えの先読み (ウォームアップ) を調べるとき。
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher().warmupTab()`
- 条件付き依存: `if (this.documentGlobal.gMultiProcessBrowser)` → `this._getSwitcher()`
- 参照: `this.documentGlobal.gMultiProcessBrowser`

## Tabbrowser.#maybeRequestReplyFromRemoteContent()
- 位置: L9269-9287
- 役割: リモートコンテンツの返答待ちが必要なら requestReplyFromRemoteContent を呼び、待つべきかを返す。
- 触るとき: キー操作でコンテンツ側の処理を待つ条件を調べるとき。
- 条件付き依存: `if ( !aEvent.isReplyEventFromRemoteContent && /** @type {MozBrowser} */ (aEvent.target)?.isRemoteBrowser === true )` → `aEvent.requestReplyFromRemoteContent()`
- 参照: `(aEvent.target)?.isRemoteBrowser`, `aEvent.defaultPrevented`, `aEvent.isReplyEventFromRemoteContent`, `aEvent.isWaitingReplyFromRemoteContent`, `aEvent.target`

## Tabbrowser.on_keydown()
- 位置: L9289-9353
- 役割: 信頼された keydown で、タブの前後移動と閉じるのショートカットを処理する。
- 触るとき: キーボードショートカットによるタブ操作を変えるとき。
- 呼び出し先: `Tabbrowser.#maybeRequestReplyFromRemoteContent()`, `aEvent.preventDefault()`, `lazy.KeyboardLockUtils.mustWaitForKeyboardLockRequestedReply()`, `lazy.ShortcutUtils.getSystemActionForEvent()`, `this.TabMetrics.userTriggeredContext()`, `this.moveTabBackward()`, `this.moveTabForward()`
- 条件付き依存: `if (this.multiSelectedTabsCount)` → `this.removeMultiSelectedTabs()`
- 条件付き依存: `if (this.multiSelectedTabsCount)` → `this.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!this.selectedTab.pinned)` → `this.removeCurrentTab()`
- 条件付き依存: `if (!this.selectedTab.pinned)` → `this.TabMetrics.userTriggeredContext()`
- 参照: `aEvent.defaultCancelled`, `aEvent.defaultPrevented`, `aEvent.isTrusted`, `lazy.ShortcutUtils.CLOSE_TAB`, `lazy.ShortcutUtils.MOVE_TAB_BACKWARD`, `lazy.ShortcutUtils.MOVE_TAB_FORWARD`, `lazy.ShortcutUtils.TOGGLE_CARET_BROWSING`, `this.TabMetrics.METRIC_SOURCE.KEYBOARD`, `this.multiSelectedTabsCount`, `this.selectedTab.pinned`

## Tabbrowser.#toggleCaretBrowsing()
- 位置: L9355-9420
- 役割: 設定を確認し、必要なら確認ダイアログを出して、キャレットブラウジングの設定を切り替える。
- 触るとき: キャレットブラウジングのショートカットの挙動を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`
- 条件付き依存: `if (warn && !browseWithCaretOn)` → `this.tabLocalization.formatValuesSync()`
- 条件付き依存: `if (warn && !browseWithCaretOn)` → `promptService.confirmEx()`
- 条件付き依存: `if (checkValue.value)` → `Services.prefs.setBoolPref()`
- 参照: `Services.prompt`, `checkValue.value`, `promptService.BUTTON_POS_1_DEFAULT`, `promptService.STD_YES_NO_BUTTONS`, `this.#awaitingToggleCaretBrowsingPrompt`, `this.documentGlobal`
- XPCOM: `Services.prefs` / `Services.prompt`

## Tabbrowser.on_keypress()
- 位置: L9422-9470
- 役割: keypress で、キャレットブラウジングの切り替えと、macOS の次/前のタブ移動を処理する。
- 触るとき: keypress 由来のタブ・キャレット操作を調べるとき。
- 呼び出し先: `Tabbrowser.#maybeRequestReplyFromRemoteContent()`, `lazy.ShortcutUtils.getSystemActionForEvent()`, `this.#toggleCaretBrowsing()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.tabContainer.advanceSelectedTab()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `aEvent.preventDefault()`
- 参照: `AppConstants.platform`, `aEvent.defaultCancelled`, `aEvent.defaultPrevented`, `aEvent.defaultPreventedByChrome`, `aEvent.isTrusted`, `lazy.ShortcutUtils.NEXT_TAB`, `lazy.ShortcutUtils.PREVIOUS_TAB`, `lazy.ShortcutUtils.TOGGLE_CARET_BROWSING`, `this.documentGlobal.RTL_UI`

## Tabbrowser.on_framefocusrequested()
- 位置: L9472-9482
- 役割: 別のタブの browser からフォーカス要求があれば、そのタブを選択してウィンドウにフォーカスする。
- 触るとき: 背景タブからのフォーカス要求の扱いを調べるとき。
- 呼び出し先: `aEvent.preventDefault()`, `this.documentGlobal.focus()`, `this.getTabForBrowser()`
- 参照: `aEvent.target`, `this.selectedTab`

## Tabbrowser.on_visibilitychange()
- 位置: L9484-9492
- 役割: スイッチャーが無いとき、ウィンドウの可視状態に応じて表示中 browser の layers と docShell の有効状態を切り替える。
- 触るとき: ウィンドウ非表示時の browser の有効化を調べるとき。
- 条件付き依存: `if (!this._switcher)` → `browser.preserveLayers()`
- 参照: `browser.docShellIsActive`, `this._switcher`, `this.document.hidden`, `this.selectedBrowsers`

## Tabbrowser.on_TabGroupCollapse()
- 位置: L9494-9498
- 役割: 折りたたまれたグループ内のタブを複数選択から外す。
- 触るとき: グループ折りたたみ時の選択解除を調べるとき。
- 呼び出し先: `aEvent.target.tabs.forEach()`, `this.removeFromMultiSelectedTabs()`

## Tabbrowser.on_TabGroupCreateByUser()
- 位置: L9500-9502
- 役割: ユーザー作成のグループに対し、作成モーダルを開く。
- 触るとき: グループ作成直後の名前入力 UI を調べるとき。
- 呼び出し先: `this.tabGroupMenu.openCreateModal()`
- 参照: `aEvent.target`

## Tabbrowser.on_TabGrouped()
- 位置: L9504-9523
- 役割: グループ化されたタブの開いている URI の登録を、新しいグループ ID で登録し直す。
- 触るとき: グループ変更時の switch-to-tab 用登録の更新を調べるとき。
- 呼び出し先: `Tabbrowser.#originalRegisteredOpenURIs.get()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (uri)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`
- 参照: `aEvent.detail`, `tab.group?.id`, `tab.linkedBrowser?.registeredOpenURI`, `tab.userContextId`, `this.documentGlobal`, `uri.spec`

## Tabbrowser.on_TabUngrouped()
- 位置: L9525-9547
- 役割: グループ解除されたタブの開いている URI の登録を、元のグループ分から外して登録し直す。
- 触るとき: グループ解除時の switch-to-tab 用登録の更新を調べるとき。
- 呼び出し先: `Tabbrowser.#originalRegisteredOpenURIs.get()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (uri)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (uri)` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`
- 参照: `aEvent.detail`, `aEvent.target`, `originalGroup.id`, `tab.linkedBrowser?.registeredOpenURI`, `tab.userContextId`, `this.documentGlobal`, `uri.spec`

## Tabbrowser.on_TabSplitViewActivate()
- 位置: L9549-9552
- 役割: アクティブな分割ビューを記録し、通知ボックスを分割ビュー側に移す。
- 触るとき: 分割ビューが有効になったときの処理を調べるとき。
- 呼び出し先: `this.#moveSplitViewNotificationBoxes()`
- 参照: `aEvent.detail.splitview`, `aEvent.detail.tabs`, `this.#activeSplitView`

## Tabbrowser.on_TabSplitViewDeactivate()
- 位置: L9554-9559
- 役割: 該当の分割ビューならアクティブ記録を外し、通知ボックスを移し戻す。
- 触るとき: 分割ビューが無効になったときの処理を調べるとき。
- 呼び出し先: `this.#moveSplitViewNotificationBoxes()`
- 参照: `aEvent.detail.splitview`, `aEvent.detail.tabs`, `this.#activeSplitView`

## Tabbrowser.#moveSplitViewNotificationBoxes()
- 位置: L9567-9574
- 役割: 指定タブの既存の通知ボックスを、挿入先の規則に従って入れ直す。
- 触るとき: 分割ビューの切り替え時の通知バーの移動を調べるとき。
- 呼び出し先: `this.readNotificationBox()`
- 条件付き依存: `if (notificationBox?._stack)` → `this.#insertNotificationBox()`
- 参照: `notificationBox._stack`, `notificationBox?._stack`, `tab.linkedBrowser`

## Tabbrowser.on_activate()
- 位置: L9576-9578
- 役割: ウィンドウがアクティブになったとき、選択タブの最終アクティブ時刻を更新する。
- 触るとき: 最後に見た時刻の更新契機を調べるとき。
- 呼び出し先: `this.selectedTab.updateLastSeenActive()`

## Tabbrowser.on_deactivate()
- 位置: L9580-9582
- 役割: ウィンドウが非アクティブになったとき、選択タブの最終アクティブ時刻を更新する。
- 触るとき: 最後に見た時刻の更新契機を調べるとき。
- 呼び出し先: `this.selectedTab.updateLastSeenActive()`

## Tabbrowser.on_change()
- 位置: L9584-9587
- 役割: 配色 (ダーク/ライト) の変更時にアイコンの更新を行う。
- 触るとき: 配色変更時のタブアイコンの再描画を調べるとき。
- 呼び出し先: `this.#maybeRefreshIcons()`

## Tabbrowser.#isFirstOrLastInTabGroup()
- 位置: L9593-9601
- 役割: タブがグループの先頭または末尾にあるかを返す静的メソッド。
- 触るとき: ツールチップにグループ名を出す条件を調べるとき。
- 条件付き依存: `if (tab.group)` → `groupTabs.at()`
- 参照: `tab.group`, `tab.group.tabs`

## Tabbrowser.getTabPids()
- 位置: L9603-9615
- 役割: タブの content プロセスとサブフレームのプロセスの PID を並べて返す。
- 触るとき: デバッグ用ツールチップのプロセス ID 表示を調べるとき。
- 呼び出し先: `framePids.sort()`, `lazy.E10SUtils.getBrowserPids()`, `pids.concat()`
- 参照: `tab.linkedBrowser`, `tab?.linkedBrowser`, `this.documentGlobal.gFissionBrowser`

## Tabbrowser.getTabTooltip()
- 位置: L9626-9698
- 役割: タブのラベル、デバッグ情報、コンテナ名、グループ名、音声再生中の説明を行ごとに連結して返す。
- 触るとき: タブのツールチップの内容を変えるとき。
- 呼び出し先: `Tabbrowser.#isFirstOrLastInTabGroup()`, `labelArray.join()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (includeLabel)` → `labelArray.push()`
- 条件付き依存: `if (includeLabel)` → `Tabbrowser.#fullLabels.get()`
- 条件付き依存: `if (includeLabel)` → `tab.getAttribute()`
- 条件付き依存: `if (Tabbrowser.prefs.showPidAndActiveness)` → `this.getTabPids()`
- 条件付き依存: `if (pids.length)` → `debugStringArray.push()`
- 条件付き依存: `if (pids.length)` → `pids.join()`
- 条件付き依存: `if (tab.linkedBrowser.docShellIsActive)` → `debugStringArray.push()`
- 条件付き依存: `if (Tabbrowser.prefs.showPidAndActiveness)` → `lazy.SponsorProtection.isProtectedBrowser()`
- 条件付き依存: `if (lazy.SponsorProtection.isProtectedBrowser(tab.linkedBrowser))` → `debugStringArray.push()`
- 条件付き依存: `if (debugStringArray.length)` → `labelArray.push()`
- 条件付き依存: `if (debugStringArray.length)` → `debugStringArray.join()`
- 条件付き依存: `if (containerName && tabGroupName)` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (tabGroupName)` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (!(tabGroupName))` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (containerName || tabGroupName)` → `labelArray.push()`
- 条件付き依存: `if (tab.soundPlaying)` → `this.tabLocalization.formatValueSync()`
- 条件付き依存: `if (tab.soundPlaying)` → `labelArray.push()`
- 参照: `Tabbrowser.prefs.showPidAndActiveness`, `debugStringArray.length`, `pids.length`, `tab.group.name`, `tab.linkedBrowser`, `tab.linkedBrowser.docShellIsActive`, `tab.soundPlaying`, `tab.userContextId`

## Tabbrowser.createTooltip()
- 位置: L9700-9747
- 役割: ツールチップ表示時に対象タブを特定し、音声ボタン上なら専用文言、それ以外ではタブの説明を設定する。
- 触るとき: タブのツールチップの出し分けや抑止条件を変えるとき。
- 呼び出し先: `event.stopPropagation()`, `event.target.triggerNode?.closest()`, `this.selectedTabs.includes()`, `tooltip.removeAttribute()`
- 条件付き依存: `if (!tab)` → `event.target.triggerNode?.getRootNode()?.host?.closest()`
- 条件付き依存: `if (!tab)` → `event.target.triggerNode?.getRootNode()`
- 条件付き依存: `if (event.target.triggerNode?.getRootNode()?.host?.closest("tab"))` → `event.target.triggerNode?.getRootNode().host.closest()`
- 条件付き依存: `if (event.target.triggerNode?.getRootNode()?.host?.closest("tab"))` → `event.target.triggerNode?.getRootNode()`
- 条件付き依存: `if (!(event.target.triggerNode?.getRootNode()?.host?.closest("tab")))` → `event.preventDefault()`
- 条件付き依存: `if (tab.selected)` → `this.document.getElementById()`
- 条件付き依存: `if (tab.selected)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (!(tab.selected))` → `tab.hasAttribute()`
- 条件付き依存: `if (tab._overPlayingIcon || tab._overAudioButton)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (lazy.showTabCardPreview)` → `event.preventDefault()`
- 条件付き依存: `if (!(tab._overPlayingIcon || tab._overAudioButton))` → `this.getTabTooltip()`
- 参照: `event.target`, `l10nArgs.shortcut`, `lazy.showTabCardPreview`, `tab._overAudioButton`, `tab._overPlayingIcon`, `tab.linkedBrowser.audioMuted`, `tab.selected`, `this.selectedTabs.length`, `tooltip.label`

## Tabbrowser.handleEvent()
- 位置: L9749-9756
- 役割: イベント種別に応じた on_<type> メソッドへ振り分け、無ければ例外を投げる。
- 触るとき: gBrowser が受けるイベントの処理先を調べるとき。
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `aEvent.type`

## Tabbrowser.observe()
- 位置: L9758-9775
- 役割: コンテナ更新ではタブの見た目を更新し、言語変更ではタイトルのキャッシュとタイトルバーを更新する。
- 触るとき: オブザーバ通知への反応を調べるとき。
- 呼び出し先: `tab.getAttribute()`, `this.#populateTitleCache()`, `this.updateTitlebar()`
- 条件付き依存: `if (tab.getAttribute("usercontextid") == identity.userContextId)` → `lazy.ContextualIdentityService.setTabStyle()`
- 参照: `aSubject.wrappedJSObject`, `identity.userContextId`, `this.tabs`

## Tabbrowser.refreshBlocked()
- 位置: L9777-9816
- 役割: ブロックされたリフレッシュ/リダイレクトの通知バーを、無ければ追加し、あれば文言を更新する。
- 触るとき: 自動リフレッシュのブロック通知を変えるとき。
- 呼び出し先: `notificationBox.getNotificationWithValue()`, `this.getNotificationBox()`
- 条件付き依存: `if (!(notification))` → `notificationBox.appendNotification()`
- 参照: `data.sameURI`, `notification.label`, `notificationBox.PRIORITY_INFO_MEDIUM`

## Tabbrowser.callback()
- 位置: L9800-9802
- 役割: RefreshBlocker:Refresh メッセージを送って、ブロックしたリフレッシュを許可するボタンのコールバック。
- 触るとき: リフレッシュ許可ボタンの動作を調べるとき。
- 呼び出し先: `actor.sendAsyncMessage()`

## Tabbrowser.#generateUniquePanelID()
- 位置: L9819-9823
- 役割: プロセス全体で単調増加する連番から tabpanel- 形式の一意な ID を返す静的メソッド。
- 触るとき: タブパネルの ID の付け方を調べるとき。
- 参照: `Tabbrowser.#uniquePanelIDCounter`

## Tabbrowser.destroy()
- 位置: L9825-9876
- 役割: コンテナの破棄、オブザーバとイベントリスナの解除、各タブのリスナーと登録の解除、スイッチャーの破棄を行う。
- 触るとき: ウィンドウ終了時の後始末や、リスナーの解除漏れを調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `Tabbrowser.#tabFilters.get()`, `this.document.removeEventListener()`, `this.documentGlobal.removeEventListener()`, `this.tabContainer.destroy()`
- 条件付き依存: `if (browser.registeredOpenURI)` → `browser.getAttribute()`
- 条件付き依存: `if (browser.registeredOpenURI)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (browser.registeredOpenURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (filter)` → `browser.webProgress.removeProgressListener()`
- 条件付き依存: `if (filter)` → `Tabbrowser.#tabListeners.get()`
- 条件付き依存: `if (listener)` → `filter.removeProgressListener()`
- 条件付き依存: `if (listener)` → `listener.destroy()`
- 条件付き依存: `if (filter)` → `Tabbrowser.#tabFilters.delete()`
- 条件付き依存: `if (filter)` → `Tabbrowser.#tabListeners.delete()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.document.removeEventListener()`
- 条件付き依存: `if (this._switcher)` → `this._switcher.destroy()`
- 参照: `AppConstants.platform`, `browser.registeredOpenURI`, `browser.registeredOpenURI.spec`, `tab.group?.id`, `tab.linkedBrowser`, `this._switcher`, `this.documentGlobal`, `this.documentGlobal.gMultiProcessBrowser`, `this.tabs`
- XPCOM: `Services.obs`

## Tabbrowser.#setupEventListeners()
- 位置: L9878-10310
- 役割: 選択切り替え、ウィンドウを閉じる要求、ページタイトル変更、モーダル、クラッシュ、音声などのイベントリスナを登録する。
- 触るとき: gBrowser が購読するイベントの追加や変更をするとき。
- 呼び出し先: `Tabbrowser.#tabFilters.get()`, `Tabbrowser.#tabListeners.get()`, `Window.isInstance()`, `browser.addEventListener()`, `browser.didStartLoadSinceLastUserTyping()`, `browser.webProgress.removeProgressListener()`, `event.target.registerAudibleChangeHandler()`, `event.target.unregisterAudibleChangeHandler()`, `evt.initEvent()`, `filter.removeProgressListener()`, `lazy.SitePermissions.setForPrincipal()`, `oldListener.destroy()`, `tab.dispatchEvent()`, `tab.hasAttribute()`, `tab.registerAudibleChangeHandler()`, `tab.unregisterAudibleChangeHandler()`, `this.#activeSplitView.close()`, `this.#activeSplitView.reverseTabs()`, `this.#activeSplitView.unsplitTabs()`, `this.addEventListener()`, `this.document .getElementById()`, `this.document .getElementById("split-view-menu") ?.getAttribute()`, `this.document.createEvent()`, `this.documentGlobal.addEventListener()`, `this.getTabForBrowser()`, `this.getTabFromAudioEvent()`, `this.maybeCloseTabForRetargetedLoad()`, `this.setPageInfo()`, `this.setTabTitle()`, `this.splitViewCommandSet.addEventListener()`, `this.tabContainer.addEventListener()`, `this.tabpanels.addEventListener()`
- 条件付き依存: `if (event.target == this.tabpanels)` → `this.updateCurrentBrowser()`
- 条件付き依存: `if (this.tabs.length == 1 && this.#shouldCloseWindowWithLastTab)` → `this.documentGlobal.close()`
- 条件付き依存: `if (tab)` → `this.removeTab()`
- 条件付き依存: `if (tab)` → `event.preventDefault()`
- 条件付き依存: `if (titleChanged && !tab.selected && !tab.hasAttribute("busy"))` → `tab.setAttribute()`
- 条件付き依存: `if ( event.detail && event.detail.tabPrompt && event.detail.inPermitUnload && Services.focus.activeWindow )` → `this.documentGlobal.focus()`
- 条件付き依存: `if (promptPrincipal.URI && !promptPrincipal.isSystemPrincipal)` → `Services.perms.testPermissionFromPrincipal()`
- 条件付き依存: `if (permission != Services.perms.ALLOW_ACTION)` → `this.getTabDialogBox()`
- 条件付き依存: `if (permission != Services.perms.ALLOW_ACTION)` → `tabPrompt.onNextPromptShowAllowFocusCheckboxFor()`
- 条件付き依存: `if (event.target == this.selectedBrowser)` → `this.documentGlobal.gURLBar.setURI()`
- 条件付き依存: `if (!tab.hasAttribute("activemedia-blocked"))` → `tab.setAttribute()`
- 条件付き依存: `if (!tab.hasAttribute("activemedia-blocked"))` → `this._tabAttrModified()`
- 条件付き依存: `if (tab.hasAttribute("activemedia-blocked"))` → `tab.removeAttribute()`
- 条件付き依存: `if (tab.hasAttribute("activemedia-blocked"))` → `this._tabAttrModified()`
- 参照: `Services.focus.activeWindow`, `Services.perms.ALLOW_ACTION`, `browser.contentPrincipal`, `browser.contentPrincipal.isSystemPrincipal`, `browser.contentTitle`, `browser.isRemoteBrowser`, `browser.userTypedValue`, `event.detail`, `event.detail.areLeaving`, `event.detail.inPermitUnload`, `event.detail.promptPrincipal`, `event.detail.tabPrompt`, `event.detail?.promptType`, `event.isTrusted`, `event.originalTarget`, `event.target`, `event.target.docShell.chromeEventHandler`, `event.target.document.nodePrincipal`, `event.target.id`, `event.target.nodeName`, `event.target.userTypedValue`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_GLOBAL`, `oldListener._requestCount`, `oldListener._stateFlags`, `promptPrincipal.URI`, `promptPrincipal.isNullPrincipal`, `promptPrincipal.isSystemPrincipal`, `tab.selected`, `tabForEvent.attention`, `tabForEvent.linkedBrowser`, `tabForEvent.linkedBrowser.contentPrincipal`, `tabForEvent.selected`, `this.#shouldCloseWindowWithLastTab`, `this.documentGlobal.skipNextCanClose`, `this.selectedBrowser`, `this.selectedTab`, `this.tabpanels`, `this.tabs`, `this.tabs.length`
- XPCOM: `Services.focus` / `Services.perms`

## onTabCrashed()
- 位置: L10054-10092
- 役割: タブのクラッシュ時に、状況に応じたクラッシュ処理を呼び、音声表示を消してアイコンを再設定する。
- 触るとき: タブのクラッシュ時の UI 処理を調べるとき。
- 呼び出し先: `tab.removeAttribute()`, `this.getTabForBrowser()`, `this.setIcon()`
- 条件付き依存: `if (!event.isTopFrame)` → `lazy.TabCrashHandler.onSubFrameCrash()`
- 条件付き依存: `if (browser === this.preloadedBrowser)` → `lazy.NewTabPagePreloading.removePreloadedBrowser()`
- 条件付き依存: `if (this.selectedBrowser == browser)` → `lazy.TabCrashHandler.onSelectedBrowserCrash()`
- 条件付き依存: `if (!(this.selectedBrowser == browser))` → `lazy.TabCrashHandler.onBackgroundBrowserCrash()`
- 参照: `browser.mIconURL`, `event.childID`, `event.isTopFrame`, `event.isTrusted`, `event.originalTarget`, `event.type`, `this.documentGlobal`, `this.preloadedBrowser`, `this.selectedBrowser`

## tabContextFTLInserter()
- 位置: L10175-10188
- 役割: 初回の操作時にタブのコンテキストメニューの翻訳を挿入し、自身の登録を解除する。
- 触るとき: コンテキストメニューの文言の遅延挿入を調べるとき。
- 呼び出し先: `this.tabContainer.removeEventListener()`, `this.translateTabContextMenu()`

## didChange()
- 位置: L10227-10278
- 役割: リモート性の変更後に、入力値、進捗リスナー、検索バーを復元して TabRemotenessChange を送る。
- 触るとき: Gecko 側が決めたプロセス切り替えの後処理を調べるとき。
- 呼び出し先: `Tabbrowser.#tabListeners.set()`, `browser.getContentBlockingEvents()`, `browser.webProgress.addProgressListener()`, `evt.initEvent()`, `filter.addProgressListener()`, `tab.dispatchEvent()`, `this._callProgressListeners()`, `this.document.createEvent()`, `this.isFindBarInitialized()`
- 条件付き依存: `if (hadStartedLoad)` → `browser.urlbarChangeTracker.startedLoad()`
- 条件付き依存: `if (browser.isRemoteBrowser)` → `tab.removeAttribute()`
- 条件付き依存: `if (this.isFindBarInitialized(tab))` → `this.getCachedFindBar()`
- 参照: `Ci.nsIWebProgress.NOTIFY_ALL`, `browser.isRemoteBrowser`, `browser.userTypedValue`, `browser.webProgress`, `this.getCachedFindBar(tab).browser`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## Tabbrowser.translateTabContextMenu()
- 位置: L10313-10329
- 役割: タブのコンテキストメニューの FTL を挿入し、遅延 l10n ID を有効にする (1 回のみ)。
- 触るとき: コンテキストメニュー文言の遅延ロードを調べるとき。
- 呼び出し先: `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `this.document .getElementById()`, `this.document .getElementById("tabContextMenu") .querySelectorAll()`, `this.document .getElementById("tabContextMenu") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`, `this.documentGlobal.MozXULElement.insertFTLIfNeeded()`
- 参照: `this.#tabContextMenuTranslated`

## Tabbrowser.setSuccessor()
- 位置: L10331-10356
- 役割: タブの後継タブを設定または解除し、逆引きの集合も更新する。別ウィンドウのタブは拒否する。
- 触るとき: タブを閉じた後の選択先 (successor) の管理を調べるとき。
- 呼び出し先: `Tabbrowser.#predecessors.get()`, `Tabbrowser.#successors.get()`, `Tabbrowser.#successors.set()`, `predecessors.add()`
- 条件付き依存: `if (oldSuccessor)` → `Tabbrowser.#predecessors.get(oldSuccessor).delete()`
- 条件付き依存: `if (oldSuccessor)` → `Tabbrowser.#predecessors.get()`
- 条件付き依存: `if (!successorTab)` → `Tabbrowser.#successors.delete()`
- 条件付き依存: `if (!predecessors)` → `Tabbrowser.#predecessors.set()`
- 参照: `aTab.documentGlobal`, `successorTab.documentGlobal`, `this.documentGlobal`

## Tabbrowser.getSuccessor()
- 位置: L10364-10366
- 役割: タブが閉じられる/隠れるときに選ぶ後継タブを返す。無ければ null。
- 触るとき: 後継タブの取得元を調べるとき。
- 呼び出し先: `Tabbrowser.#successors.get()`

## Tabbrowser.replaceInSuccession()
- 位置: L10375-10382
- 役割: 指定タブを後継にしている全タブの後継を、別のタブに付け替える。
- 触るとき: タブを閉じる/隠す際の後継の付け替えを調べるとき。
- 呼び出し先: `Tabbrowser.#predecessors.get()`
- 条件付き依存: `if (predecessors)` → `Array.from()`
- 条件付き依存: `if (predecessors)` → `this.setSuccessor()`

## Tabbrowser.clearRelatedTabs()
- 位置: L10384-10386
- 役割: 直近の関連タブの対応表をリセットする。
- 触るとき: 次に開くタブの関連付けを断ち切る契機を調べるとき。
- 参照: `this.#lastRelatedTabMap`

## TabProgressListener.constructor()
- 位置: L10393-10425
- 役割: タブと browser を保持し、状態フラグ、進捗、リクエスト数を初期化する。
- 触るとき: 進捗リスナーの初期状態 (プリロード時含む) を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_IS_REQUEST`, `Ci.nsIWebProgressListener.STATE_STOP`, `this._blank`, `this._browser`, `this._message`, `this._requestCount`, `this._stateFlags`, `this._status`, `this._tab`, `this._totalProgress`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.#documentGlobal()
- 位置: L10427-10429
- 役割: タブの属する window を返す。
- 触るとき: リスナーが使う window の取得元を調べるとき。
- 参照: `this._tab.documentGlobal`

## TabProgressListener.#tabbrowser()
- 位置: L10431-10433
- 役割: タブの属する window の gBrowser を返す。
- 触るとき: リスナーが使う gBrowser の取得元を調べるとき。
- 参照: `this._tab.documentGlobal.gBrowser`

## TabProgressListener.destroy()
- 位置: L10435-10438
- 役割: タブと browser への参照を削除する。
- 触るとき: リスナー破棄時の参照解放を調べるとき。
- 参照: `this._browser`, `this._tab`

## TabProgressListener._callProgressListeners()
- 位置: L10440-10443
- 役割: 自身の browser を先頭に付けて tabbrowser の _callProgressListeners を呼ぶ。
- 触るとき: リスナーから全体の進捗通知への中継を調べるとき。
- 呼び出し先: `args.unshift()`, `this.#tabbrowser._callProgressListeners()`
- 参照: `this._browser`

## TabProgressListener._shouldShowProgress()
- 位置: L10445-10460
- 役割: 初期の空白ページや about: のローカルページでは進捗を出さないと判定する。
- 触るとき: 進捗表示を出す条件を変えるとき。
- 呼び出し先: `aRequest.originalURI.schemeIs()`
- 参照: `Ci.nsIChannel`, `this._blank`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md)

## TabProgressListener._isForInitialAboutBlank()
- 位置: L10462-10479
- 役割: 状態変化が最初の about:blank に関するものかを判定する。
- 触るとき: 初期 about:blank の通知を無視する条件を調べるとき。
- 参照: `Ci.nsIWebProgressListener.STATE_STOP`, `aLocation.spec`, `aWebProgress.isTopLevel`, `this._blank`, `this._requestCount`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.onProgressChange()
- 位置: L10481-10510
- 役割: 進捗率を更新し、busy なら progress 属性を付けて、進捗リスナーへ通知する。
- 触るとき: タブの読み込み進捗表示を調べるとき。
- 呼び出し先: `this._callProgressListeners()`, `this._shouldShowProgress()`, `this._tab.hasAttribute()`
- 条件付き依存: `if (this._totalProgress && this._tab.hasAttribute("busy"))` → `this._tab.setAttribute()`
- 条件付き依存: `if (this._totalProgress && this._tab.hasAttribute("busy"))` → `this.#tabbrowser._tabAttrModified()`
- 参照: `this._tab`, `this._totalProgress`

## TabProgressListener.onProgressChange64()
- 位置: L10512-10528
- 役割: onProgressChange にそのまま委譲する。
- 触るとき: 64bit 版の進捗通知の経路を調べるとき。
- 呼び出し先: `this.onProgressChange()`

## TabProgressListener.onStateChange()
- 位置: L10531-10776
- 役割: 読み込みの開始と終了に応じて busy などの属性、アイコン、URL バー状態、進捗リスナーへの通知を更新する。
- 触るとき: 読み込み開始/終了時のタブの見た目や状態の更新を調べるとき。
- 呼び出し先: `aRequest.QueryInterface()`, `this._callProgressListeners()`, `this._isForInitialAboutBlank()`
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `this.#documentGlobal.gInitialPages.includes()`
- 条件付き依存: `if ( !( originalLocation && this.#documentGlobal.gInitialPages.includes( originalLocation.spec ) && originalLocation != "about:blank" && this._browser.initialPag...)` → `this._browser.urlbarChangeTracker.startedLoad()`
- 条件付き依存: `if ( !( originalLocation && this.#documentGlobal.gInitialPages.includes( originalLocation.spec ) && originalLocation != "about:blank" && this._browser.initialPag...)` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if ( this._browser.browsingContext.sessionHistory?.count === 0 && (this._browser.initiatedFromNonWebControlled || lazy.BrowserUIUtils.checkEmptyPageOrigin( this....)` → `this.#tabbrowser.setInitialTabTitle()`
- 条件付き依存: `if (this._tab.selected && !this.#tabbrowser.userTypedValue)` → `this.#documentGlobal.gURLBar.setURI()`
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `this._tab.removeAttribute()`
- 条件付き依存: `if (aStateFlags & STATE_START && aStateFlags & STATE_IS_NETWORK)` → `this._shouldShowProgress()`
- 条件付き依存: `if ( !(aStateFlags & Ci.nsIWebProgressListener.STATE_RESTORING) && aWebProgress && aWebProgress.isTopLevel )` → `this._tab.setAttribute()`
- 条件付き依存: `if ( !(aStateFlags & Ci.nsIWebProgressListener.STATE_RESTORING) && aWebProgress && aWebProgress.isTopLevel )` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (aStateFlags & STATE_STOP && aStateFlags & STATE_IS_NETWORK)` → `this._tab.hasAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("busy"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("busy"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (this._tab.hasAttribute("busy"))` → `Components.isSuccessCode()`
- 条件付き依存: `if (this._tab._notselectedsinceload)` → `this._tab.setAttribute()`
- 条件付き依存: `if (!(this._tab._notselectedsinceload))` → `this._tab.removeAttribute()`
- 条件付き依存: `if ( aWebProgress.isTopLevel && !aWebProgress.isLoadingDocument && Components.isSuccessCode(aStatus) && !this.#tabbrowser.tabContainer.tabAnimationsInProgress &&...)` → `this._tab.setAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("progress"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("progress"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (aWebProgress.isTopLevel)` → `Components.isSuccessCode()`
- 条件付き依存: `if ( this._tab.selected && aStatus != Cr.NS_BINDING_CANCELLED_OLD_LOAD && !isNavigating )` → `this.#documentGlobal.gURLBar.setURI()`
- 条件付き依存: `if (isSuccessful)` → `this._browser.urlbarChangeTracker.finishedLoad()`
- 条件付き依存: `if (shouldRemoveFavicon && this._tab.hasAttribute("image"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (shouldRemoveFavicon && this._tab.hasAttribute("image"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (!shouldRemoveFavicon)` → `this.#tabbrowser.setDefaultIcon()`
- 条件付き依存: `if (modifiedAttrs.length)` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (ignoreBlank)` → `this._callProgressListeners()`
- 条件付き依存: `if (!(ignoreBlank))` → `this._callProgressListeners()`
- 参照: `Ci.nsIChannel`, `Ci.nsIWebProgressListener`, `Ci.nsIWebProgressListener.STATE_RESTORING`, `Cr.NS_BINDING_CANCELLED_OLD_LOAD`, `aRequest.URI`, `aRequest.originalURI`, `aWebProgress.isLoadingDocument`, `aWebProgress.isTopLevel`, `location.scheme`, `modifiedAttrs.length`, `originalLocation.spec`, `this.#documentGlobal.gReduceMotion`, `this.#tabbrowser._isBusy`, `this.#tabbrowser.tabContainer.tabAnimationsInProgress`, `this.#tabbrowser.userTypedValue`, `this._blank`, `this._browser`, `this._browser.browsingContext.nonWebControlledLoadingURI`, `this._browser.browsingContext.sessionHistory?.count`, `this._browser.currentURI`, `this._browser.currentURI.spec`, `this._browser.documentURI`, `this._browser.initialPageLoadedFromUserAction`, `this._browser.initiatedFromNonWebControlled`, `this._browser.isNavigating`, `this._browser.mIconURL`, `this._browser.userTypedValue`, `this._message`, `this._requestCount`, `this._stateFlags`, `this._status`, `this._tab`, `this._tab._notselectedsinceload`, `this._tab.isEmpty`, `this._tab.selected`, `this._totalProgress`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.onLocationChange()
- 位置: L10779-10965
- 役割: URL 変更時に入力値、音声、検索バー、タイトル、アイコン、開いている URI の登録を更新し、リスナーへ通知する。
- 触るとき: ページ遷移時のタブの状態更新や URL バーとの連動を調べるとき。
- 条件付き依存: `if (topLevel)` → `this._browser.didStartLoadSinceLastUserTyping()`
- 条件付き依存: `if (topLevel)` → `this._tab.hasAttribute()`
- 条件付き依存: `if (isErrorPage && this._tab.hasAttribute("busy"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (isErrorPage && this._tab.hasAttribute("busy"))` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (!isSameDocument)` → `this._tab.hasAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("soundplaying"))` → `this.#documentGlobal.clearTimeout()`
- 条件付き依存: `if (this._tab.hasAttribute("soundplaying"))` → `this._tab.removeAttribute()`
- 条件付き依存: `if (this._tab.hasAttribute("soundplaying"))` → `this.#tabbrowser._tabAttrModified()`
- 条件付き依存: `if (this._tab.hasAttribute("muted"))` → `this._tab.linkedBrowser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (!isSameDocument)` → `this.#tabbrowser.isFindBarInitialized()`
- 条件付き依存: `if (this.#tabbrowser.isFindBarInitialized(this._tab))` → `this.#tabbrowser.getCachedFindBar()`
- 条件付き依存: `if (findBar.findMode != findBar.FIND_NORMAL)` → `findBar.close()`
- 条件付き依存: `if (!isReload)` → `this.#tabbrowser.setTabTitle()`
- 条件付き依存: `if (!isReload && aWebProgress.isLoadingDocument)` → `TabProgressListener.#getTriggeringPrincipalFromHistory()`
- 条件付き依存: `if (triggerer && triggerer.isSystemPrincipal)` → `this.#tabbrowser.clearRelatedTabs()`
- 条件付き依存: `if (!isSameDocument)` → `this.#documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `this._browser.toggleAttribute()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `lazy.AIWindow.isAIWindowActive()`
- 条件付き依存: `if (!lazy.allowTransparentBrowser)` → `lazy.AIWindow.isAIWindowContentPage()`
- 条件付き依存: `if (topLevel)` → `this._browser.getAttribute()`
- 条件付き依存: `if (this._browser.registeredOpenURI)` → `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`
- 条件付き依存: `if (this._browser.registeredOpenURI)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (topLevel)` → `this.#documentGlobal.isBlankPageURL()`
- 条件付き依存: `if (!this.#documentGlobal.isBlankPageURL(aLocation.spec))` → `lazy.UrlbarProviderOpenTabs.registerOpenTab()`
- 条件付き依存: `if (!this.#documentGlobal.isBlankPageURL(aLocation.spec))` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (this._tab.splitview && aLocation.spec !== "about:opentabs")` → `this._tab.splitview.tabs.indexOf()`
- 条件付き依存: `if (this._tab.splitview && aLocation.spec !== "about:opentabs")` → `String()`
- 条件付き依存: `if (this._tab.splitview && aLocation.spec !== "about:opentabs")` → `Glean.splitview.uriCount[label].add()`
- 条件付き依存: `if (this._tab != this.#tabbrowser.selectedTab)` → `this.#tabbrowser._tabLayerCache.indexOf()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this.#tabbrowser._tabLayerCache.splice()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this.#tabbrowser._getSwitcher().cleanUpTabAfterEviction()`
- 条件付き依存: `if (tabCacheIndex != -1)` → `this.#tabbrowser._getSwitcher()`
- 条件付き依存: `if (!this._blank || this._browser.hasContentOpener)` → `this._callProgressListeners()`
- 条件付き依存: `if (topLevel && !isSameDocument)` → `this._callProgressListeners()`
- 条件付き依存: `if (topLevel)` → `Date.now()`
- 参照: `Ci.nsIChannel`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_ERROR_PAGE`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `Glean.splitview.uriCount`, `aLocation.spec`, `aRequest.originalURI`, `aRequest.originalURI.spec`, `aWebProgress.isLoadingDocument`, `aWebProgress.isTopLevel`, `findBar.FIND_NORMAL`, `findBar.findMode`, `lazy.allowTransparentBrowser`, `this.#documentGlobal`, `this.#tabbrowser.selectedTab`, `this._blank`, `this._browser`, `this._browser.hasContentOpener`, `this._browser.isNavigating`, `this._browser.lastLocationChange`, `this._browser.lastURI`, `this._browser.mIconURL`, `this._browser.originalURI`, `this._browser.registeredOpenURI`, `this._browser.userTypedValue`, `this._tab`, `this._tab._soundPlayingAttrRemovalTimer`, `this._tab.group?.id`, `this._tab.splitview`, `triggerer.isSystemPrincipal`, `uri.spec`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TabProgressListener.onStatusChange()
- 位置: L10967-10980
- 役割: 空白でなければステータス文言を進捗リスナーへ通知して保持する。
- 触るとき: ステータスバーの文言の流れを調べるとき。
- 呼び出し先: `this._callProgressListeners()`
- 参照: `this._blank`, `this._message`

## TabProgressListener.onSecurityChange()
- 位置: L10982-10988
- 役割: セキュリティ状態の変化を進捗リスナーへ中継する。
- 触るとき: セキュリティ表示の更新経路を調べるとき。
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.onContentBlockingEvent()
- 位置: L10990-10996
- 役割: コンテンツブロッキングのイベントを進捗リスナーへ中継する。
- 触るとき: トラッキング保護表示の更新経路を調べるとき。
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.onRefreshAttempted()
- 位置: L10998-11005
- 役割: リフレッシュ試行を進捗リスナーへ中継し、その結果を返す。
- 触るとき: 自動リフレッシュの可否判断の経路を調べるとき。
- 呼び出し先: `this._callProgressListeners()`

## TabProgressListener.#getTriggeringPrincipalFromHistory()
- 位置: L11012-11020
- 役割: セッション履歴の現在エントリから triggering principal を取り出して返す静的メソッド。
- 触るとき: 直近の遷移の発生元を判定する処理を調べるとき。
- 呼び出し先: `sessionHistory.getEntryAtIndex()`
- 参照: `aBrowser?.browsingContext?.sessionHistory`, `currentEntry?.triggeringPrincipal`, `sessionHistory.count`, `sessionHistory.index`

## _normalizeLoadURIOptions()
- 位置: L11029-11045
- 役割: 読み込みオプションを検証し、triggeringPrincipal 必須、コンテナ ID 一致の確認と、フラグ、ユーザー操作の既定値を整える。
- 触るとき: loadURI 系のオプションの検証を変えるとき。
- 呼び出し先: `browser.getAttribute()`
- 参照: `browser.ownerDocument.hasValidTransientUserGestureActivation`, `loadURIOptions.flags`, `loadURIOptions.hasValidUserGestureActivation`, `loadURIOptions.loadFlags`, `loadURIOptions.triggeringPrincipal`, `loadURIOptions.userContextId`

## _loadFlagsToFixupFlags()
- 位置: L11047-11060
- 役割: 読み込みフラグとプライベート状態から URI 補正のフラグを作る。
- 触るとき: URL 補正のフラグの決め方を調べるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_NONE`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md)

## _fixupURIString()
- 位置: L11062-11081
- 役割: URL 文字列を補正した優先 URI を返す。失敗時は null を返す。
- 触るとき: アドレスバー入力の補正結果の取得を調べるとき。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `this._loadFlagsToFixupFlags()`
- 参照: `fixupInfo.preferredURI`, `loadURIOptions.loadFlags`
- XPCOM: `Services.uriFixup`

## _updateTriggerMetadataForLoad()
- 位置: L11083-11123
- 役割: 読み込みの履歴オプションに応じ、スポンサーや検索エンジン由来の情報を browser の属性に設定または削除する。
- 触るとき: 読み込み元の情報 (スポンサー、検索エンジン) の記録を調べるとき。
- 条件付き依存: `if (globalHistoryOptions.triggeringSource == "newtab")` → `lazy.SponsorProtection.addProtectedBrowser()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `Services.uriFixup.getFixupURIInfo()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `this._loadFlagsToFixupFlags()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `browser.setAttribute()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSponsoredURL)` → `Date.now()`
- 条件付き依存: `if (!(globalHistoryOptions?.triggeringSponsoredURL))` → `lazy.SponsorProtection.removeProtectedBrowser()`
- 条件付き依存: `if (globalHistoryOptions?.triggeringSearchEngine)` → `browser.setAttribute()`
- 条件付き依存: `if (!(globalHistoryOptions?.triggeringSearchEngine))` → `browser.removeAttribute()`
- 参照: `globalHistoryOptions.triggeringSearchEngine`, `globalHistoryOptions.triggeringSource`, `globalHistoryOptions.triggeringSponsoredURL`, `globalHistoryOptions.triggeringSponsoredURLVisitTimeMS`, `globalHistoryOptions?.triggeringSearchEngine`, `globalHistoryOptions?.triggeringSponsoredURL`
- XPCOM: `Services.uriFixup`

## fixupAndLoadURIString()
- 位置: L11126-11128
- 役割: 文字列 URL を共通の読み込み処理へ渡す。browser 要素の関数を置き換える。
- 触るとき: 文字列 URL の読み込みの入口を調べるとき。
- 呼び出し先: `this._internalMaybeFixupLoadURI()`

## loadURI()
- 位置: L11129-11131
- 役割: nsIURI を共通の読み込み処理へ渡す。browser 要素の関数を置き換える。
- 触るとき: nsIURI の読み込みの入口を調べるとき。
- 呼び出し先: `this._internalMaybeFixupLoadURI()`

## _internalMaybeFixupLoadURI()
- 位置: L11135-11178
- 役割: オプションを検証し、補正と履歴メタデータの更新を行って、webNavigation に URI または文字列を読み込ませる。
- 触るとき: browser への URL 読み込みの共通処理を変えるとき。
- 呼び出し先: `this._normalizeLoadURIOptions()`, `this._updateTriggerMetadataForLoad()`
- 条件付き依存: `if (!uriString && !uri)` → `Services.io.newURI()`
- 条件付き依存: `if (!uri)` → `this._fixupURIString()`
- 条件付き依存: `if (startedWithURI)` → `browser.webNavigation.loadURI()`
- 条件付き依存: `if (!(startedWithURI))` → `browser.webNavigation.fixupAndLoadURIString()`
- 参照: `browser.browsingContext.isCaptivePortalTab`, `browser.isNavigating`, `loadURIOptions.isCaptivePortalTab`, `uri.spec`
- XPCOM: `Services.io`
