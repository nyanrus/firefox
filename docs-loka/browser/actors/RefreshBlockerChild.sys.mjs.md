# browser/actors/RefreshBlockerChild.sys.mjs

source: browser/actors/RefreshBlockerChild.sys.mjs
source-hash: a610fce48d65519334128d22b77241f593b11bf0
lines: 236

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## onStateChange()
- 位置: L53-60
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && aStateFlags & Ci.nsIWebProgressListener.STATE_STOP )` → `this.blockedWindows.delete()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_STOP`, `aWebProgress.DOMWindow`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: L67-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.blockedWindows.has()`
- 条件付き依存: `if (this.blockedWindows.has(win))` → `this.blockedWindows.get()`
- 条件付き依存: `if (data)` → `this.send()`
- 条件付き依存: `if (!(this.blockedWindows.has(win)))` → `this.blockedWindows.set()`
- 参照: `aWebProgress.DOMWindow`

## onRefreshAttempted()
- 位置: L86-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.blockedWindows.has()`
- 条件付き依存: `if (this.blockedWindows.has(win))` → `this.send()`
- 条件付き依存: `if (!(this.blockedWindows.has(win)))` → `this.blockedWindows.set()`
- 参照: `aURI.spec`, `aWebProgress.DOMWindow`, `win.browsingContext`

## send()
- 位置: L109-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `win.windowGlobalChild.getActor()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`

## RefreshBlockerChild.didDestroy()
- 位置: L135-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `this.disable()`
- 参照: `this.docShell`
- XPCOM: `Services.prefs`

## RefreshBlockerChild.enable()
- 位置: L144-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.domProcessChild .getActor()`, `ChromeUtils.domProcessChild .getActor("RefreshBlockerObserver") .enable()`
- 参照: `this.docShell`

## RefreshBlockerChild.disable()
- 位置: L150-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.domProcessChild .getActor()`, `ChromeUtils.domProcessChild .getActor("RefreshBlockerObserver") .disable()`
- 参照: `this.docShell`

## RefreshBlockerChild.receiveMessage()
- 位置: L156-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `docShell.QueryInterface()`, `refreshURI.forceRefreshURI()`
- 条件付き依存: `if (data.isEnabled)` → `this.enable()`
- 条件付き依存: `if (!(data.isEnabled))` → `this.disable()`
- 参照: `Ci.nsIRefreshURI`, `data.URI`, `data.browsingContext.docShell`, `data.delay`, `data.isEnabled`, `message.data`, `message.name`, `this.docShell`
- XPCOM: [`nsIRefreshURI`](../../docshell/base/nsIRefreshURI.idl.md) / `Services.io`

## RefreshBlockerObserverChild.constructor()
- 位置: L179-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.filtersMap`

## RefreshBlockerObserverChild.observe()
- 位置: L184-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `this.enable()`
- 条件付き依存: `if (Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `subject.QueryInterface()`
- 条件付き依存: `if (Services.prefs.getBoolPref(REFRESHBLOCKING_PREF))` → `this.disable()`
- 参照: `Ci.nsIDocShell`
- XPCOM: [`nsIDocShell`](../../docshell/base/nsIDocShell.idl.md) / `Services.prefs`

## RefreshBlockerObserverChild.enable()
- 位置: L202-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/appshell/component/browser-status-filter;1" ].createInstance()`, `docShell .QueryInterface()`, `docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `filter.addProgressListener()`, `this.filtersMap.has()`, `this.filtersMap.set()`, `webProgress.addProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_ALL`
- XPCOM: [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md) / `@mozilla.org/appshell/component/browser-status-filter;1`

## RefreshBlockerObserverChild.disable()
- 位置: L221-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `docShell .QueryInterface()`, `docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `filter.removeProgressListener()`, `this.filtersMap.delete()`, `this.filtersMap.get()`, `webProgress.removeProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`
- XPCOM: [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)
