# browser/actors/ClickHandlerChild.sys.mjs

source: browser/actors/ClickHandlerChild.sys.mjs
source-hash: 3d8c409c7e08b399d47a46a62e0fffe415d8831d
lines: 193

## <module>
- 役割: リンククリックと中クリック貼り付けを子プロセスで受け、安全性を確かめてから親へ Content:Click として送るアクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## MiddleMousePasteHandlerChild.handleEvent()
- 位置: L29-43
- 役割: 中ボタンのクリックで、オートスクロールが無効なら ClickHandler の処理へ回す。
- 触るとき: 中クリック貼り付けとリンク中クリックの振り分けを変えるときに見る。
- 呼び出し先: `this.manager .getActor()`, `this.manager .getActor("ClickHandler") .handleClickEvent()`
- 参照: `clickEvent.button`, `clickEvent.defaultPrevented`, `lazy.autoscrollEnabled`

## MiddleMousePasteHandlerChild.onProcessedClick()
- 位置: L45-47
- 役割: 処理済みの中クリック情報を MiddleClickPaste として親へ送る。
- 触るとき: 中クリック貼り付けが親に届かない問題を調べるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## ClickHandlerChild.handleEvent()
- 位置: L51-53
- 役割: ラップされたイベントの元のイベントを取り出し、クリック処理へ渡す。
- 触るとき: クリックイベントの入口を変えるときに見る。
- 呼び出し先: `this.handleClickEvent()`
- 参照: `wrapperEvent.sourceEvent`

## ClickHandlerChild.handleClickEvent()
- 位置: L55-191
- 役割: 編集可能要素や右クリックを除外し、リンクの URL・参照元・ポリシーを集め、JavaScript リンクや無効な URL を弾いて Content:Click を送る。
- 触るとき: リンクのクリックがページ側で開かない、または誤って開くときに見る。信頼されていないイベントのユーザー操作判定もここで行う。
- 呼び出し先: `Cc["@mozilla.org/referrer-info;1"].createInstance()`, `ChromeUtils.getClassName()`, `lazy.BrowserUtils.hrefAndLinkNodeForClickEvent()`, `lazy.E10SUtils.serializeReferrerInfo()`
- 条件付き依存: `if (event.button == 0)` → `ownerDoc.documentURI.startsWith()`
- 条件付き依存: `if (policyContainer)` → `lazy.E10SUtils.serializePolicyContainer()`
- 条件付き依存: `if (node)` → `referrerInfo.initWithElement()`
- 条件付き依存: `if (!(node))` → `referrerInfo.initWithDocument()`
- 条件付き依存: `if (href && !isFromMiddleMousePasteHandler)` → `Services.io.extractScheme()`
- 条件付き依存: `if (href && !isFromMiddleMousePasteHandler)` → `Services.scriptSecurityManager.checkLoadURIStrWithPrincipal()`
- 条件付き依存: `if (href && !isFromMiddleMousePasteHandler)` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if ( !event.isTrusted && lazy.BrowserUtils.whereToOpenLink(event) != "current" )` → `ownerDoc.consumeTransientUserGestureActivation()`
- 条件付き依存: `if (node)` → `node.getAttribute()`
- 条件付き依存: `if (href && !isFromMiddleMousePasteHandler)` → `event.preventMultipleActions()`
- 条件付き依存: `if (href && !isFromMiddleMousePasteHandler)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!href && event.button == 1 && isFromMiddleMousePasteHandler)` → `this.manager.getActor("MiddleMousePasteHandler").onProcessedClick()`
- 条件付き依存: `if (!href && event.button == 1 && isFromMiddleMousePasteHandler)` → `this.manager.getActor()`
- 参照: `Ci.nsIReferrerInfo`, `composedTarget.isContentEditable`, `composedTarget.ownerDocument`, `composedTarget.ownerDocument.designMode`, `event.altKey`, `event.button`, `event.composedTarget`, `event.ctrlKey`, `event.defaultPrevented`, `event.isTrusted`, `event.metaKey`, `event.originalTarget`, `event.shiftKey`, `json.globalHistoryOptions`, `json.href`, `json.title`, `lazy.blockJavascript`, `node.dataset.isSponsoredLink`, `originalTarget.ownerDocument`, `ownerDoc.URL`, `ownerDoc.hasValidTransientUserGestureActivation`, `ownerDoc.policyContainer`
- XPCOM: [`nsIReferrerInfo`](../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/referrer-info;1` / `Services.io` / `Services.scriptSecurityManager`
