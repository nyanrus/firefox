# browser/modules/BrowserWindowTracker.sys.mjs

source: browser/modules/BrowserWindowTracker.sys.mjs
source-hash: d90f63e373a7cdc7caee4ff5b9d94a5a57febece
lines: 534

## <module>
- 役割: 開いているブラウザウィンドウを追跡し、前面の窓の選択中タブの browserId をネットワーク側へ通知するモジュール。窓の生成と列挙も担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`

## debug()
- 位置: L44-48
- 役割: DEBUG が true の時だけ、標準出力に追跡の状態を書く。
- 触るとき: 追跡の挙動を調べるため DEBUG を一時的に有効にするとき。
- 条件付き依存: `if (DEBUG)` → `dump()`

## _updateCurrentBrowserId()
- 位置: L50-79
- 役割: 前面の非最小化窓の選択中ブラウザが変わった時だけ、その browserId を net:current-browser-id で通知する。
- 触るとき: ネットワーク側に現在のタブを伝える条件を変えるとき。最小化された窓を前面として扱わない理由は bug 2007691 にある。
- 呼び出し先: `Cc["@mozilla.org/supports-PRUint64;1"].createInstance()`, `Services.obs.notifyObservers()`, `_trackedWindows.find()`
- 条件付き依存: `if (DEBUG)` → `debug()`
- 参照: `Ci.nsISupportsPRUint64`, `browser.browserId`, `browser.currentURI?.spec`, `browser.documentGlobal`, `idWrapper.data`, `w.STATE_MINIMIZED`, `w.closed`, `w.windowState`
- XPCOM: [`nsISupportsPRUint64`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRUint64;1` / `Services.obs`

## _handleEvent()
- 位置: L81-101
- 役割: タブの挿入・選択と窓の activate・unload を、それぞれの処理に振り分ける。
- 触るとき: 追跡の対象にするイベントを増やすとき。
- 呼び出し先: `WindowHelper.onActivate()`, `WindowHelper.removeWindow()`, `_updateCurrentBrowserId()`
- 条件付き依存: `if ( event.target.documentGlobal.gBrowser.selectedBrowser === event.target.linkedBrowser )` → `_updateCurrentBrowserId()`
- 参照: `event.currentTarget`, `event.target`, `event.target.documentGlobal.gBrowser.selectedBrowser`, `event.target.linkedBrowser`, `event.type`

## _trackWindowOrder()
- 位置: L108-110
- 役割: 窓を追跡リストの先頭に加える。
- 触るとき: 前後の並びの扱いを変えるとき。最小化状態はここでは見ず、読み出し側で扱う。
- 呼び出し先: `_trackedWindows.unshift()`

## _untrackWindowOrder()
- 位置: L112-117
- 役割: 窓を追跡リストから取り除く。
- 触るとき: 窓を閉じた後に参照が残らないかを確かめるとき。
- 呼び出し先: `_trackedWindows.indexOf()`
- 条件付き依存: `if (idx >= 0)` → `_trackedWindows.splice()`

## topicObserved()
- 位置: L119-137
- 役割: 指定の通知を 1 回だけ待ち、checkFn が真を返した時に解決する Promise を返す。
- 触るとき: 特定の通知を待つ処理を追加するとき。
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## observer()
- 位置: L121-134
- 役割: 通知が checkFn を通ったら監視を外して解決し、例外が出たら監視を外して拒否する。
- 触るとき: 通知待ちをどの時点で解除するかを変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `checkFn()`, `reject()`, `resolve()`
- XPCOM: `Services.obs`

## addWindow()
- 位置: L141-154
- 役割: 窓のタブイベントと窓イベントを登録し、追跡リストに加えて、選択中ブラウザを通知する。
- 触るとき: 窓が追跡され始める時の処理を増やすとき。
- 呼び出し先: `TAB_EVENTS.forEach()`, `WINDOW_EVENTS.forEach()`, `_trackWindowOrder()`, `_updateCurrentBrowserId()`, `window.addEventListener()`, `window.gBrowser.tabContainer.addEventListener()`
- 参照: `window.gBrowser.selectedBrowser`

## removeWindow()
- 位置: L156-166
- 役割: 窓を追跡リストから外し、登録したイベントを解除する。
- 触るとき: 窓を閉じた時の後始末を増やすとき。
- 呼び出し先: `TAB_EVENTS.forEach()`, `WINDOW_EVENTS.forEach()`, `_untrackWindowOrder()`, `window.gBrowser.tabContainer.removeEventListener()`, `window.removeEventListener()`

## onActivate()
- 位置: L168-178
- 役割: 活性化された窓が先頭でなければ先頭へ移し、選択中ブラウザを通知する。
- 触るとき: 前面の窓の判定を変えるとき。
- 呼び出し先: `_trackWindowOrder()`, `_untrackWindowOrder()`, `_updateCurrentBrowserId()`
- 参照: `window.gBrowser.selectedBrowser`

## getTopWindow()
- 位置: L207-247
- 役割: 条件(私用、ポップアップ、タスクバータブ、仮想デスクトップ)に合う最も前面の窓を返す。最小化は後回しにし、無ければ最小化の窓、それも無ければ別デスクトップの窓を返す。
- 触るとき: 新しいタブや通知を出す窓の選び方を変えるとき。Windows の仮想デスクトップを跨がない既定の意味を保つこと。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.document.documentElement.hasAttribute()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.gPreferWindowsOnCurrentVirtualDesktop`, `options.allowFromInactiveWorkspace`, `options.allowPopups`, `options.allowTaskbarTabs`, `options.private`, `win.STATE_MINIMIZED`, `win.closed`, `win.isCloaked`, `win.toolbar.visible`, `win.windowState`

## getPendingWindow()
- 位置: L263-274
- 役割: 開きかけの窓の完了を待つ Promise を、私用の条件に合うものから返す。無ければ null。
- 触るとき: 起動中の窓を待つ処理を変えるとき。
- 呼び出し先: `this.pendingWindows.values()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `options.private`, `pending.deferred.promise`, `pending.isPrivate`

## registerOpeningWindow()
- 位置: L286-308
- 役割: 開きかけの窓を登録し、窓の browsingContext が破棄された時に登録を消して待ちを解決する。
- 触るとき: 窓が閉じられずに残る登録(リーク)の防ぎ方や待ち方を変えるとき。
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `this.pendingWindows.set()`
- XPCOM: `Services.obs`

## observer()
- 位置: L297-306
- 役割: 破棄された browsingContext が対象の窓のものなら、保留中の登録を消して Promise を解決し、監視を外す。
- 触るとき: 窓の破棄時の後始末を変えるとき。
- 条件付き依存: `if (window.browsingContext == aSubject)` → `this.pendingWindows.get()`
- 条件付き依存: `if (pending)` → `this.pendingWindows.delete()`
- 条件付き依存: `if (pending)` → `pending.deferred.resolve()`
- 条件付き依存: `if (window.browsingContext == aSubject)` → `Services.obs.removeObserver()`
- 参照: `window.browsingContext`
- XPCOM: `Services.obs`

## openWindow()
- 位置: L337-421
- 役割: オプションからウィンドウ機能を組み立てて新しい窓を開き、保留中として登録する。最初の描画でホームページ開始の通知を出す。
- 触るとき: 新しい窓の作り方(私用、AI 窓、リモート、Fission、アニメーションの抑止)を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.ww.openWindow()`, `lazy.AIWindow.handleAIWindowOptions()`, `lazy.HomePage.get()`, `this.registerOpeningWindow()`, `win.addEventListener()`
- 条件付き依存: `if (!args)` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if ( Services.prefs.getIntPref("browser.startup.page") == 1 && loadURIString == lazy.HomePage.get() )` → `Services.obs.notifyObservers()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsISupportsString`, `args.data`, `lazy.BrowserHandler.defaultArgs`, `lazy.PrivateBrowsingUtils.enabled`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `openerWindow?.STATE_MAXIMIZED`, `openerWindow?.windowState`
- XPCOM: [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1` / `Services.obs` / `Services.prefs` / `Services.ww`

## promiseOpenWindow()
- 位置: async L432-439
- 役割: openWindow で窓を開き、遅延起動が終わるまで待ってから返す。
- 触るとき: 窓を開いてすぐ操作する処理を書くとき。
- 呼び出し先: `this.openWindow()`, `topicObserved()`

## windowCount()
- 位置: L444-446
- 役割: 追跡中の窓の数を返す。
- 触るとき: 窓数に依存する判定を読むとき。
- 参照: `_trackedWindows.length`

## orderedWindows()
- 位置: L448-450
- 役割: getOrderedWindows() の結果を返す。
- 触るとき: 前面順の窓一覧を外部から読むとき。
- 呼び出し先: `this.getOrderedWindows()`

## getOrderedWindows()
- 位置: L462-488
- 役割: 非最小化の窓を前に、最小化の窓を後ろにした一覧を返す。private 指定があればそれで絞る。
- 触るとき: 前面順の定義や私用窓の絞り込みを変えるとき。毎回新しい配列を返す。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `nonMinimized.concat()`, `windows.filter()`
- 条件付き依存: `if (w.windowState == w.STATE_MINIMIZED)` → `minimized.push()`
- 条件付き依存: `if (!(w.windowState == w.STATE_MINIMIZED))` → `nonMinimized.push()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `w.STATE_MINIMIZED`, `w.windowState`

## getAllVisibleTabs()
- 位置: L490-502
- 役割: 全窓の表示中タブのうち読み込み済みのものについて、タイトルと browserId を集める。
- 触るとき: タブ一覧を外部へ渡す処理を変えるとき。破棄や未復元のタブは含めない。
- 条件付き依存: `if (tab.linkedPanel)` → `tabs.push()`
- 参照: `BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser`, `tab.linkedPanel`, `win.gBrowser.visibleTabs`

## track()
- 位置: L504-514
- 役割: 保留中の窓なら遅延起動の完了後に解決し、窓を追跡リストに加える。
- 触るとき: 新しい窓を追跡対象に入れる経路を変えるとき。
- 呼び出し先: `WindowHelper.addWindow()`, `this.pendingWindows.get()`
- 条件付き依存: `if (pending)` → `this.pendingWindows.delete()`
- 条件付き依存: `if (pending)` → `window.delayedStartupPromise.then()`
- 条件付き依存: `if (pending)` → `pending.deferred.resolve()`

## getBrowserById()
- 位置: L516-525
- 役割: browserId が一致する表示中タブのブラウザを返す。無ければ null。
- 触るとき: browserId からブラウザを引く処理を変えるとき。
- 参照: `BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser`, `tab.linkedBrowser.browserId`, `tab.linkedPanel`, `win.gBrowser.visibleTabs`

## untrackForTestsOnly()
- 位置: L530-532
- 役割: テスト用に窓を追跡リストから外す。
- 触るとき: テストで窓を一時的に外す必要があるとき。テスト後に track で戻すこと。
- 呼び出し先: `WindowHelper.removeWindow()`
