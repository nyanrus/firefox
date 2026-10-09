# browser/actors/RefreshBlockerChild.sys.mjs

source: browser/actors/RefreshBlockerChild.sys.mjs
source-hash: a610fce48d65519334128d22b77241f593b11bf0
lines: 236

## <module>
- 役割: 自動再読み込み(リフレッシュ)を文書ごとに阻止し、阻止した事実を親へ伝える子側アクターと、そのプロセス側の監視役。
- 呼び出し先: `ChromeUtils.generateQI()`

## onStateChange()
- 位置: L53-60
- 役割: 窓の読み込みが完了したら、その窓の阻止情報を記録から消す。
- 触るとき: 阻止情報を保持する期間を変えるとき。
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && aStateFlags & Ci.nsIWebProgressListener.STATE_STOP )` → `this.blockedWindows.delete()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_STOP`, `aWebProgress.DOMWindow`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: L67-79
- 役割: 場所が変わった時、阻止情報が既にあれば通知を送り、無ければ記録して後の通知に備える。
- 触るとき: 通知のタイミングの扱いを変えるとき。
- 呼び出し先: `this.blockedWindows.has()`
- 条件付き依存: `if (this.blockedWindows.has(win))` → `this.blockedWindows.get()`
- 条件付き依存: `if (data)` → `this.send()`
- 条件付き依存: `if (!(this.blockedWindows.has(win)))` → `this.blockedWindows.set()`
- 参照: `aWebProgress.DOMWindow`

## onRefreshAttempted()
- 位置: L86-107
- 役割: 阻止した更新の内容を作り、場所変更が済んでいれば即座に、まだなら記録して後で送る。常に false を返して更新を止める。
- 触るとき: 阻止した更新の情報の中身を変えるとき。
- 呼び出し先: `this.blockedWindows.has()`
- 条件付き依存: `if (this.blockedWindows.has(win))` → `this.send()`
- 条件付き依存: `if (!(this.blockedWindows.has(win)))` → `this.blockedWindows.set()`
- 参照: `aURI.spec`, `aWebProgress.DOMWindow`, `win.browsingContext`

## send()
- 位置: L109-125
- 役割: タイマーで 0 ms 遅らせてから、窓の RefreshBlocker アクターに通知を送る。例外は無視する。
- 触るとき: 通知の送信タイミングを変えるとき。
- 呼び出し先: `setTimeout()`, `win.windowGlobalChild.getActor()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`

## RefreshBlockerChild.didDestroy()
- 位置: L135-142
- 役割: 阻止の設定が無効になっていれば、この文書の阻止を解除する。
- 触るとき: アクター破棄時の後始末を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `this.disable()`
- 参照: `this.docShell`
- XPCOM: `Services.prefs`

## RefreshBlockerChild.enable()
- 位置: L144-148
- 役割: プロセス側の RefreshBlockerObserver に、この文書の阻止を有効にさせる。
- 触るとき: 阻止の有効化の経路を追うとき。
- 呼び出し先: `ChromeUtils.domProcessChild .getActor()`, `ChromeUtils.domProcessChild .getActor("RefreshBlockerObserver") .enable()`
- 参照: `this.docShell`

## RefreshBlockerChild.disable()
- 位置: L150-154
- 役割: プロセス側の RefreshBlockerObserver に、この文書の阻止を解除させる。
- 触るとき: 阻止の解除の経路を追うとき。
- 呼び出し先: `ChromeUtils.domProcessChild .getActor()`, `ChromeUtils.domProcessChild .getActor("RefreshBlockerObserver") .disable()`
- 参照: `this.docShell`

## RefreshBlockerChild.receiveMessage()
- 位置: L156-175
- 役割: RefreshBlocker:Refresh で阻止していた更新を実行し、PreferenceChanged で阻止の有効・無効を切り替える。
- 触るとき: 手動の更新の実行や設定の反映を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `docShell.QueryInterface()`, `refreshURI.forceRefreshURI()`
- 条件付き依存: `if (data.isEnabled)` → `this.enable()`
- 条件付き依存: `if (!(data.isEnabled))` → `this.disable()`
- 参照: `Ci.nsIRefreshURI`, `data.URI`, `data.browsingContext.docShell`, `data.delay`, `data.isEnabled`, `message.data`, `message.name`, `this.docShell`
- XPCOM: [`nsIRefreshURI`](../../docshell/base/nsIRefreshURI.idl.md) / `Services.io`

## RefreshBlockerObserverChild.constructor()
- 位置: L179-182
- 役割: 文書ごとのフィルターを保持する対応表を作る。
- 触るとき: フィルターの管理方法を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.filtersMap`

## RefreshBlockerObserverChild.observe()
- 位置: L184-200
- 役割: 文書の作成と破棄の通知を受け、阻止の設定が有効なら有効化・解除する。
- 触るとき: 新しい文書で阻止が効かない不具合を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `this.enable()`
- 条件付き依存: `if (Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `subject.QueryInterface()`
- 条件付き依存: `if (Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `this.disable()`
- 参照: `Ci.nsIDocShell`
- XPCOM: [`nsIDocShell`](../../docshell/base/nsIDocShell.idl.md) / `Services.prefs`

## RefreshBlockerObserverChild.enable()
- 位置: L202-219
- 役割: 文書ごとにフィルターを作って進捗リスナーを付け、文書の進捗に接続する。既にあれば何もしない。
- 触るとき: 阻止の対象範囲を変えるとき。
- 呼び出し先: `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`, `docShell .QueryInterface()`, `docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `filter.addProgressListener()`, `this.filtersMap.has()`, `this.filtersMap.set()`, `webProgress.addProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_ALL`
- XPCOM: [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1`

## RefreshBlockerObserverChild.disable()
- 位置: L221-234
- 役割: 文書の進捗からフィルターを外し、対応表からも消す。
- 触るとき: 阻止解除の後始末を変えるとき。
- 呼び出し先: `docShell .QueryInterface()`, `docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `filter.removeProgressListener()`, `this.filtersMap.delete()`, `this.filtersMap.get()`, `webProgress.removeProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`
- XPCOM: [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)
