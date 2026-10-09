# browser/components/urlbar/UrlbarProviderSearchTips.sys.mjs

source: browser/components/urlbar/UrlbarProviderSearchTips.sys.mjs
source-hash: 162beebeda8195e3d80d1369323065c967997548
lines: 535

## <module>
- 役割: 新しいタブや既定の検索エンジンのトップページを開いたときに、検索ヒントを一度だけ出す UrlbarProviderSearchTips を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.SearchStaticData.getAlternateDomains()`, `lazy.SearchStaticData.getAlternateDomains("www.google.com") .map()`, `str.slice()`, `str.slice("www.google.".length).replaceAll()`

## UrlbarProviderSearchTips.constructor()
- 位置: L100-122
- 役割: インスタンスが一つだけであることを確かめ、まだ表示上限に達していないヒントが一つでもあれば、セッション内でヒントを有効にする。
- 触るとき: ヒントが出ない原因が表示上限の判定にあるかを調べるとき、この初期化の条件を見る。二つ目のインスタンスが作られると例外になる点にも注意する。
- 呼び出し先: `Object.values()`, `lazy.UrlbarPrefs.get()`, `super()`
- 参照: `UrlbarProviderSearchTips.#instance`, `UrlbarShared.SEARCH_TIP_TYPE`, `this._seenWindows`, `this.disableTipsForCurrentSession`

## UrlbarProviderSearchTips.PRIORITY()
- 位置: L124-127
- 役割: 優先度をトップサイトの優先度に 1 を足した値とし、Places やトップサイトより先に出るようにする。
- 触るとき: ヒント結果と他の候補の前後関係を変えるとき、この値を見直す。
- 参照: `lazy.UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderSearchTips.type()
- 位置: L132-134
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: ヒント結果を他の結果種別とどう並べるかを変えるとき見る。
- 参照: `UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderSearchTips.isActive()
- 位置: async L141-143
- 役割: 表示すべきヒントが決まっており、cfr の機能設定が有効なときだけ有効にする。
- 触るとき: ヒントが出ない問題を調べるとき、currentTip が設定されているかと cfr 設定のどちらで弾かれているかを確かめる。
- 参照: `lazy.cfrFeaturesUserPref`, `this.currentTip`

## UrlbarProviderSearchTips.getPriority()
- 位置: L150-152
- 役割: 静的な PRIORITY の値を返す。
- 触るとき: 優先度を動的に変える必要が出たとき、ここを書き換える。
- 参照: `UrlbarProviderSearchTips.PRIORITY`

## UrlbarProviderSearchTips.startQuery()
- 位置: async L162-204
- 役割: 保持中の currentTip を表示済みとして記録し、既定の検索エンジンのアイコンと名前を使って ONBOARD は heuristic、REDIRECT は通常の TIP 結果を一件追加する。
- 触るとき: ヒントの文言や、ONBOARD と REDIRECT の出し分けを変えるとき見る。
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `addCallback()`, `lazy.SearchService.getDefault()`, `this.#makeResult()`
- 参照: `UrlbarShared.SEARCH_TIP_TYPE.NONE`, `UrlbarShared.SEARCH_TIP_TYPE.ONBOARD`, `UrlbarShared.SEARCH_TIP_TYPE.REDIRECT`, `defaultEngine.name`, `this.currentTip`, `this.queryInstance`, `this.showedTipTypeInCurrentEngagement`

## UrlbarProviderSearchTips.#pickResult()
- 位置: L214-228
- 役割: urlbar の値を空にしてフォーカスを移し、そのヒントの表示回数を上限まで引き上げて、以後のセッションで再表示しないようにする。
- 触るとき: ヒントの「OK」操作や、クリック後に再表示される問題を調べるとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.set()`, `window.gURLBar.focus()`, `window.gURLBar.removeAttribute()`, `window.gURLBar.setPageProxyState()`
- 参照: `result.payload.type`, `window.gURLBar.value`

## UrlbarProviderSearchTips.onEngagement()
- 位置: L235-237
- 役割: 選ばれた結果がヒントなら #pickResult で確認済みとして扱う。
- 触るとき: ヒント結果を選んだ後の挙動を変えるとき見る。
- 呼び出し先: `this.#pickResult()`
- 参照: `controller.browserWindow`, `details.result`

## UrlbarProviderSearchTips.onSearchSessionEnd()
- 位置: L239-241
- 役割: 検索セッションが終わったとき、このエンゲージメントで表示したヒントの記録を NONE に戻す。
- 触るとき: 検索セッションごとの表示記録が残って次の検索を妨げる問題を調べるとき見る。
- 参照: `UrlbarShared.SEARCH_TIP_TYPE.NONE`, `this.showedTipTypeInCurrentEngagement`

## UrlbarProviderSearchTips.onLocationChange()
- 位置: async L255-264
- 役割: インスタンスが存在すれば、ウィンドウの場所変更をそのインスタンスの onLocationChange に渡す静的な窓口である。
- 触るとき: browser.js からの場所変更通知の受け口を変えるとき見る。
- 条件付き依存: `if (UrlbarProviderSearchTips.#instance)` → `UrlbarProviderSearchTips.#instance.onLocationChange()`
- 参照: `UrlbarProviderSearchTips.#instance`

## UrlbarProviderSearchTips.onLocationChange()
- 位置: async L278-335
- 役割: ウィンドウ初回は描画後 500ms 待ってからページ遷移を処理し、同一ドキュメントの変更やサブフレームは無視する。表示中のビューを閉じ、条件を満たせば _maybeShowTipForUrl を呼ぶ。
- 触るとき: ヒントを出すタイミングや、起動直後の描画負荷への配慮を変えるとき見る。ts_paint に影響させないための待機もここで行われる。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._maybeShowTipForUrl()`, `this._maybeShowTipForUrl(uri.spec, window).catch()`, `this._seenWindows.has()`, `this.logger.error()`
- 条件付き依存: `if (!this._seenWindows.has(window))` → `this._seenWindows.add()`
- 条件付き依存: `if (!this._seenWindows.has(window))` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 条件付き依存: `if (!this._seenWindows.has(window))` → `timer.initWithCallback()`
- 条件付き依存: `if ( this.showedTipTypeInCurrentEngagement != UrlbarShared.SEARCH_TIP_TYPE.NONE )` → `window.gURLBar.view.close()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `UrlbarShared.SEARCH_TIP_TYPE.NONE`, `lazy.cfrFeaturesUserPref`, `this._onLocationChangeInstance`, `this.disableTipsForCurrentSession`, `this.showedTipTypeInCurrentEngagement`, `uri.spec`, `webProgress.isTopLevel`, `window.gBrowserInit.firstContentWindowPaintPromise`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `@mozilla.org/timer;1`

## UrlbarProviderSearchTips._maybeShowTipForUrl()
- 位置: async L346-423
- 役割: about:newtab か既定エンジンのホームページかで種別を決め、表示上限、直近の更新(24 時間以内)、他の通知の有無を確かめたうえで、200ms 後に空文字で検索を開始してヒントを表示する。
- 触るとき: ヒントが出る条件(上限回数、更新からの経過時間、他の通知との競合)を変えたいとき、またはヒントが出ない原因を追うとき見る。
- 呼び出し先: `Math.min()`, `["about:newtab", "about:home"].includes()`, `isBrowserShowingNotification()`, `isDefaultEngineHomepage()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`, `lazy.setTimeout()`, `window.gURLBar.getAttribute()`, `window.gURLBar.search()`
- 参照: `UrlbarShared.SEARCH_TIP_TYPE.ONBOARD`, `UrlbarShared.SEARCH_TIP_TYPE.REDIRECT`, `lazy.LaterRun.hoursSinceInstall`, `lazy.LaterRun.hoursSinceUpdate`, `this._maybeShowTipForUrlInstance`, `this.currentTip`, `this.disableTipsForCurrentSession`, `window.gURLBar.value`

## UrlbarProviderSearchTips.#makeResult()
- 位置: L425-437
- 役割: TIP 型の結果を作り、確認ボタンと、表示種別・アイコン・タイトルの payload を設定する。
- 触るとき: ヒント結果のボタンや表示内容を変えるとき見る。
- 参照: `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.TIP`, `lazy.UrlbarResult`

## isBrowserShowingNotification()
- 位置: async L440-499
- 役割: urlbar のビュー、通知バー、アプリメニュー、ポップアップ、ページアクション、ツールバーのパネル、ダイアログ、既定ブラウザの確認が開いていれば true を返す。
- 触るとき: ヒントを出すべきでない他の表示物を増やしたいとき、またはヒントと他の表示が重なる問題を調べるときに見る。
- 呼び出し先: `lazy.DefaultBrowserCheck.willCheckDefaultBrowser()`, `navbar.querySelectorAll()`, `node.getAttribute()`, `window.document.getElementById()`, `window.gBrowser.getNotificationBox()`
- 条件付き依存: `if (pageActions)` → `child.getAttribute()`
- 参照: `lazy.AppMenuNotifications.activeNotification`, `lazy.AppMenuNotifications.activeNotification.dismissed`, `lazy.AppMenuNotifications.activeNotification.options.badgeOnly`, `pageActions.childNodes`, `window.PopupNotifications.isPanelOpen`, `window.gBrowser.getNotificationBox().currentNotification`, `window.gDialogBox.isOpen`, `window.gNotificationBox.currentNotification`, `window.gURLBar.view.isOpen`

## isDefaultEngineHomepage()
- 位置: async L510-534
- 役割: 既定エンジンの名前が SUPPORTED_ENGINES にあり、URL のホストとパスが対応する正規表現に一致するかを判定する。禁止された検索パラメーターがあれば false を返す。
- 触るとき: 対応する検索エンジンを増やしたいときや、ホームページ判定が外れる原因を調べるとき見る。(要確認: SUPPORTED_ENGINES の Google の正規表現は、テンプレート文字列内のエスケープにより「.」がエスケープされていない可能性がある。)
- 呼び出し先: `URL.parse()`, `homepageMatches.domainPath.test()`, `lazy.SUPPORTED_ENGINES.get()`, `lazy.SearchService.getDefault()`, `url.hostname.concat()`, `url.searchParams.has()`
- 参照: `defaultEngine.name`, `homepageMatches.prohibitedSearchParams`, `url.pathname`
