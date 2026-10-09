# browser/components/places/InteractionsChild.sys.mjs

source: browser/components/places/InteractionsChild.sys.mjs
source-hash: edf0d7e4c573017eaeb94097c12f5bdc41c31d9e
lines: 139

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## InteractionsChild.actorCreated()
- 位置: L19-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`, `this.docShell .QueryInterface()`, `this.docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `webProgress.addProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_LOCATION`, `Ci.nsIWebProgress.NOTIFY_STATE_DOCUMENT`, `this.#progressListener`, `this.contentWindow`, `this.isContentWindowPrivate`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## onLocationChange()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onLocationChange()`

## InteractionsChild.didDestroy()
- 位置: L49-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.docShell .QueryInterface()`, `this.docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `webProgress.removeProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`, `this.#progressListener`, `this.docShell`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## InteractionsChild.onLocationChange()
- 位置: L61-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordNewPage()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## InteractionsChild.#recordNewPage()
- 位置: L76-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!this.docShell.currentDocumentChannel)` → `this.sendAsyncMessage()`
- 参照: `Ci.nsIHttpChannel`, `Services.io.newURI(doc.referrer).specIgnoringRef`, `doc.documentURIObject.specIgnoringRef`, `doc.referrer`, `this.#currentURL`, `this.docShell.currentDocumentChannel`, `this.docShell.currentDocumentChannel.requestSucceeded`, `this.document`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `Services.io`

## InteractionsChild.handleEvent()
- 位置: async L109-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordNewPage()`, `this.sendAsyncMessage()`
- 参照: `currentDocumentChannel.requestSucceeded`, `event.type`, `this.docShell.currentDocumentChannel`, `this.isContentWindowPrivate`
