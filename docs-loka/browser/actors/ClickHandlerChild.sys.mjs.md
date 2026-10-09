# browser/actors/ClickHandlerChild.sys.mjs

source: browser/actors/ClickHandlerChild.sys.mjs
source-hash: 3d8c409c7e08b399d47a46a62e0fffe415d8831d
lines: 193

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## MiddleMousePasteHandlerChild.handleEvent()
- 位置: L29-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.manager .getActor()`, `this.manager .getActor("ClickHandler") .handleClickEvent()`
- 参照: `clickEvent.button`, `clickEvent.defaultPrevented`, `lazy.autoscrollEnabled`

## MiddleMousePasteHandlerChild.onProcessedClick()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## ClickHandlerChild.handleEvent()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleClickEvent()`
- 参照: `wrapperEvent.sourceEvent`

## ClickHandlerChild.handleClickEvent()
- 位置: L55-191
- 役割: (未記入)
- 触るとき: (未記入)
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
