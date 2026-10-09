# browser/components/places/InteractionsChild.sys.mjs

source: browser/components/places/InteractionsChild.sys.mjs
source-hash: edf0d7e4c573017eaeb94097c12f5bdc41c31d9e
lines: 139

## <module>
- 役割: content プロセス側でトップレベルのページ遷移を検出し、親へ PageLoaded と PageHide を送る子アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## InteractionsChild.actorCreated()
- 位置: L19-47
- 役割: プライベートウィンドウでなければ docShell の進行状況リスナーを登録する。
- 触るとき: アクター生成時にリスナーが付かない、またはプライベートブラウジングで記録が始まる不具合を調べるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`, `this.docShell .QueryInterface()`, `this.docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `webProgress.addProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`, `Ci.nsIWebProgress.NOTIFY_LOCATION`, `Ci.nsIWebProgress.NOTIFY_STATE_DOCUMENT`, `this.#progressListener`, `this.contentWindow`, `this.isContentWindowPrivate`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## onLocationChange()
- 位置: L28-30
- 役割: 登録したリスナーの位置変更コールバックを、同名のメソッドへそのまま転送する。
- 触るとき: 位置変更の引数を増やすとき、リスナー経由の呼び出し経路を追うとき。
- 呼び出し先: `this.onLocationChange()`

## InteractionsChild.didDestroy()
- 位置: L49-59
- 役割: 登録済みの進行状況リスナーを docShell から外す。docShell が無ければ何もしない。
- 触るとき: タブを閉じた後にリスナーが残る、または破棄時に例外が出る問題を調べるとき。
- 呼び出し先: `this.docShell .QueryInterface()`, `this.docShell .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `webProgress.removeProgressListener()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIWebProgress`, `this.#progressListener`, `this.docShell`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## InteractionsChild.onLocationChange()
- 位置: L61-74
- 役割: トップレベルかつ同一ドキュメント内の遷移(pushState など)だけを #recordNewPage へ渡す。
- 触るとき: SPA の履歴遷移が記録されない、または同じページ内の遷移を新規ページとして扱ってしまうときに見る。
- 呼び出し先: `this.#recordNewPage()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## InteractionsChild.#recordNewPage()
- 位置: L76-107
- 役割: ドキュメントチャネルが無ければ PageHide を送り、同じ URL や失敗した HTTP 応答は無視して、それ以外は referrer 付きで PageLoaded を送る。
- 触るとき: 同じ URL が二重に記録される、または失敗したリクエストが記録に残る問題を調べるとき、referrer の扱いを変えるとき。
- 呼び出し先: `Services.io.newURI()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!this.docShell.currentDocumentChannel)` → `this.sendAsyncMessage()`
- 参照: `Ci.nsIHttpChannel`, `Services.io.newURI(doc.referrer).specIgnoringRef`, `doc.documentURIObject.specIgnoringRef`, `doc.referrer`, `this.#currentURL`, `this.docShell.currentDocumentChannel`, `this.docShell.currentDocumentChannel.requestSucceeded`, `this.document`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `Services.io`

## InteractionsChild.handleEvent()
- 位置: async L109-137
- 役割: DOMContentLoaded で #recordNewPage を呼び、pagehide では成功した HTTP 応答の場合にだけ PageHide を送る。
- 触るとき: ページの読み込み開始や離脱を検出するタイミングを変えるとき、pagehide で離脱が送られないケースを調べるとき。
- 呼び出し先: `this.#recordNewPage()`, `this.sendAsyncMessage()`
- 参照: `currentDocumentChannel.requestSucceeded`, `event.type`, `this.docShell.currentDocumentChannel`, `this.isContentWindowPrivate`
