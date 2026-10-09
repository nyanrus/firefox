# browser/components/search/SearchUIUtils.sys.mjs

source: browser/components/search/SearchUIUtils.sys.mjs
source-hash: d2a1a93992f6a9565299c68a92ccdfa64e6480fa
lines: 623

## <module>
- 役割: 検索 UI の共通処理(通知バー、OpenSearch 追加、検索の実行、新規タブへの検索バー登録)をまとめた SearchUIUtils を定義する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## SearchUIUtilsL10n()
- 位置: L37-39
- 役割: browser/search.ftl と branding/brand.ftl を読む Localization を遅延生成する。
- 触るとき: 検索 UI の新しい文言を Fluent で出すとき、読み込む ftl ファイルに追加が必要か確かめるとき。

## init()
- 位置: L45-54
- 役割: 一度だけ browser-search-engine-modified を監視し、通常とプライベートの urlbar placeholder を初期化する。
- 触るとき: 起動時の検索エンジン関連の初期化の順序を変えるとき、または placeholder が起動直後に出ないときの原因を調べるとき。
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.initialized)` → `this.updatePlaceholderNamePreference()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L61-70
- 役割: engine-default と engine-default-private の変更を受け、対応する placeholder 設定を更新する。
- 触るとき: 既定エンジンの変更通知の種類を増やすとき、または既定を変えたのに placeholder が古いままのとき。
- 呼び出し先: `this.updatePlaceholderNamePreference()`

## showSearchServiceNotification()
- 位置: L84-97
- 役割: SearchService から届く通知種別 search-engine-removal と search-settings-reset に応じて、対応する通知バーを出す。
- 触るとき: SearchService 側で新しい通知種別を足して、ブラウザ側で表示させたいとき。
- 呼び出し先: `this.removalOfSearchEngineNotificationBox()`, `this.searchSettingsResetNotificationBox()`

## removalOfSearchEngineNotificationBox()
- 位置: async L108-147
- 役割: 最前面のウィンドウに、エンジン削除を知らせる通知バーを出し、全ウィンドウの urlbar placeholder を更新する。
- 触るとき: エンジン削除時の通知文やボタンを変えるとき、または削除後に placeholder が古いままのとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `openWin.gURLBar?.updatePlaceholder()`
- 条件付き依存: `if (win)` → `win.gNotificationBox.appendNotification()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `win.gNotificationBox.PRIORITY_SYSTEM`

## callback()
- 位置: L118-124
- 役割: 削除通知の「削除」ボタンを押したときに、search-engine-removal の通知を閉じる。
- 触るとき: 削除通知のボタン動作を変えるとき。
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`, `win.gNotificationBox.removeNotification()`

## searchSettingsResetNotificationBox()
- 位置: async L156-188
- 役割: 検索設定がリセットされたことと新しい既定エンジン名を、最前面のウィンドウの通知バーで知らせる。
- 触るとき: 設定リセット時の通知文や通知の値 search-settings-reset を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.gNotificationBox.appendNotification()`
- 参照: `win.gNotificationBox.PRIORITY_SYSTEM`

## callback()
- 位置: L165-170
- 役割: リセット通知の「リセット」ボタンを押したときに、search-settings-reset の通知を閉じる。
- 触るとき: リセット通知のボタン動作を変えるとき。
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`, `win.gNotificationBox.removeNotification()`

## addOpenSearchEngine()
- 位置: async L204-253
- 役割: SearchService で OpenSearch エンジンを追加し、失敗時は種類に応じたエラーダイアログを出して false を返す。
- 触るとき: OpenSearch の追加失敗時に出るエラー文言や、追加の成否の扱いを変えるとき。
- 呼び出し先: `Services.prompt.alertBC()`, `lazy.SearchService.addOpenSearchEngine()`, `lazy.SearchUIUtilsL10n.formatValues()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_CONTENT`, `browsingContext?.embedderElement?.contentPrincipal?.originAttributes`, `ex.type`, `lazy.SearchEngineInstallError`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt`

## searchEnginesURL()
- 位置: L260-264
- 役割: browser.search.searchEnginesURL の pref から、検索エンジンを探す案内 URL を整形して返す。
- 触るとき: 検索エンジンを追加するための案内ページの URL を変えるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## updatePlaceholderNamePreference()
- 位置: async L271-290
- 役割: 既定エンジンが ConfigSearchEngine なら名前を placeholderName の pref に保存し、それ以外や失敗時は pref を消す。
- 触るとき: urlbar の placeholder に出すエンジン名の決まり方を変えるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `lazy.SearchService.init()`
- 条件付き依存: `if (engine instanceof lazy.ConfigSearchEngine)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(engine instanceof lazy.ConfigSearchEngine))` → `Services.prefs.clearUserPref()`
- 参照: `engine.name`, `lazy.ConfigSearchEngine`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`
- XPCOM: `Services.prefs`

## webSearch()
- 位置: L300-382
- 役割: 通常のブラウザウィンドウで検索バーにフォーカスする。無ければ既存のウィンドウに委ね、無ければ新しいウィンドウを開いて後からフォーカスする。
- 触るとき: 検索ショートカットで検索バーに入る経路を変えるとき、または検索バーがツールバーのオーバーフローに入っているときの動きを調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `focusUrlBarIfSearchFieldIsNotActive()`, `lazy.CustomizableUI.getPlacementOfWidget()`, `searchBar.parentElement.getAttribute()`, `window.document.getElementById()`
- 条件付き依存: `if ( window.location.href != AppConstants.BROWSER_CHROME_URL || window.gURLBar.readOnly )` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (topWindow && !topWindow.gURLBar.readOnly)` → `topWindow.focus()`
- 条件付き依存: `if (topWindow && !topWindow.gURLBar.readOnly)` → `SearchUIUtils.webSearch()`
- 条件付き依存: `if (!(topWindow && !topWindow.gURLBar.readOnly))` → `window.openDialog()`
- 条件付き依存: `if (!(topWindow && !topWindow.gURLBar.readOnly))` → `Services.obs.addObserver()`
- 条件付き依存: `if ( placement && searchBar && ((searchBar.parentElement.getAttribute("overflowedItem") == "true" && placement.area == lazy.CustomizableUI.AREA_NAVBAR) || placem...)` → `window.document.getElementById()`
- 条件付き依存: `if ( placement && searchBar && ((searchBar.parentElement.getAttribute("overflowedItem") == "true" && placement.area == lazy.CustomizableUI.AREA_NAVBAR) || placem...)` → `navBar.overflowable.show().then()`
- 条件付き依存: `if ( placement && searchBar && ((searchBar.parentElement.getAttribute("overflowedItem") == "true" && placement.area == lazy.CustomizableUI.AREA_NAVBAR) || placem...)` → `navBar.overflowable.show()`
- 条件付き依存: `if (window.fullScreen)` → `window.FullScreen.showNavToolbox()`
- 条件付き依存: `if (searchBar)` → `searchBar.select()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `lazy.CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `lazy.CustomizableUI.AREA_NAVBAR`, `placement.area`, `topWindow.gURLBar.readOnly`, `window.fullScreen`, `window.gURLBar.readOnly`, `window.location.href`
- XPCOM: `Services.obs` / `Services.prefs`

## observer()
- 位置: L319-327
- 役割: 新しいウィンドウの browser-delayed-startup-finished を待ち、そのウィンドウで webSearch を呼んでから監視を外す。
- 触るとき: 起動直後の新規ウィンドウで検索を開始する際のタイミングを調べるとき。
- 条件付き依存: `if (subject == newWindow)` → `SearchUIUtils.webSearch()`
- 条件付き依存: `if (subject == newWindow)` → `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## focusUrlBarIfSearchFieldIsNotActive()
- 位置: L334-339
- 役割: 検索欄が無い、またはフォーカスされていなければ urlbar を検索モードにする。
- 触るとき: 検索欄にフォーカスが無いときに urlbar で検索モードに切り替える条件を変えるとき。
- 条件付き依存: `if (!searchBar || window.document.activeElement != searchBar.inputField)` → `window.gURLBar.searchModeShortcut()`
- 参照: `searchBar.inputField`, `window.document.activeElement`

## focusSearchBar()
- 位置: L350-360
- 役割: webSearch の中で、検索欄を取り直して選択し、検索モード判定を行う。オーバーフローメニューから開く経路で使われる。
- 触るとき: 検索欄がツールバーのオーバーフローに入っているときに検索欄へフォーカスが移らないとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `focusUrlBarIfSearchFieldIsNotActive()`, `searchBar.select()`, `window.document.getElementById()`
- XPCOM: `Services.prefs`

## loadSearch()
- 位置: async L423-479
- 役割: triggeringPrincipal を必須にし、既定または指定エンジンで検索 URL を作って openLinkIn で開き、BrowserSearchTelemetry に記録する。
- 触るとき: 検索結果を開く場所(タブ、ウィンドウ)やテレメトリの記録内容を変えるとき、または検索 URL が作れずに例外が出るとき。
- 呼び出し先: `engine.getSubmission()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `window.openLinkIn()`
- 条件付き依存: `if (!engine)` → `lazy.SearchService.getDefaultPrivate()`
- 条件付き依存: `if (!engine)` → `lazy.SearchService.getDefault()`
- 参照: `engine.name`, `submission.postData`, `submission.uri.spec`, `tab?.linkedBrowser`, `window.gBrowser.selectedBrowser`

## loadSearchFromContext()
- 位置: async L507-553
- 役割: 右クリックメニューの検索を開く。開き先は current を tab に変え、プライベート指定なら window にし、中クリックや Ctrl で背景タブの向きを反転させる。
- 触るとき: 右クリックからの検索の開き方や背景読み込みの扱いを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.createNullPrincipal()`, `lazy.BrowserUtils.getRootEvent()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.loadSearch()`
- 参照: `event.button`, `event.ctrlKey`, `lazy.SearchUtils.URL_TYPE.VISUAL_SEARCH`, `triggeringPrincipal.originAttributes`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## SearchNewTabComponentsRegistrant.constructor()
- 位置: L565-579
- 役割: handoffToAwesomebar の pref を遅延取得し、変更時に更新するよう設定し、UrlbarPrefs の監視を登録する。
- 触るとき: 新規タブの検索バーの登録条件に使う pref を足すとき。
- 呼び出し先: `XPCOMUtils.declareLazy()`, `lazy.UrlbarPrefs.addObserver()`, `super()`
- 参照: `this.lazy`

## onUpdate()
- 位置: L573-575
- 役割: handoffToAwesomebar の pref が変わったら updated を呼んで、新規タブのコンポーネント登録を更新する。
- 触るとき: handoffToAwesomebar の変更が新規タブに反映されないとき。
- 呼び出し先: `this.updated()`

## SearchNewTabComponentsRegistrant.destroy()
- 位置: L581-583
- 役割: UrlbarPrefs の監視を外す。
- 触るとき: レジストラントの破棄時に監視が残ってリークしないか確かめるとき。
- 呼び出し先: `lazy.UrlbarPrefs.removeObserver()`

## SearchNewTabComponentsRegistrant.onNimbusChanged()
- 位置: L585-589
- 役割: Nimbus の newtabFeatureGate が変わったら updated を呼んで登録を更新する。
- 触るとき: Nimbus の実験で新規タブの検索バーの出し分けを変えるとき。
- 条件付き依存: `if (variable == "newtabFeatureGate")` → `this.updated()`

## SearchNewTabComponentsRegistrant.onPrefChanged()
- 位置: L591-595
- 役割: browser.nova.enabled が変わったら updated を呼んで登録を更新する。
- 触るとき: nova の有効化に応じて新規タブの検索バーの登録が変わるかを確かめるとき。
- 条件付き依存: `if (pref == "browser.nova.enabled")` → `this.updated()`

## SearchNewTabComponentsRegistrant.getComponents()
- 位置: L597-621
- 役割: newtabFeatureGate が有効なら空を返し、無ければ content-search-handoff-ui の登録情報(キャレットの点滅設定、nonhandoff 属性)を返す。
- 触るとき: 新規タブに出す検索バーの構成やキャレット変数を変えるとき、または Nimbus gate の分岐を直すとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `AboutNewTabComponentRegistry.TYPES.SEARCH`, `Services.appinfo`, `this.lazy.prefHandoffToAwesomebar`
- XPCOM: `Services.appinfo`
