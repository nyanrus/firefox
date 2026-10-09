# browser/actors/ClickHandlerParent.sys.mjs

source: browser/actors/ClickHandlerParent.sys.mjs
source-hash: c06993a8f543d7d4587f618b429c7dba59ff9987
lines: 161

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## fillInClickEvent()
- 位置: L19-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.WebNavigationFrames.getFrameId()`
- 参照: `actor.manager`, `data.frameID`, `data.isContentWindowPrivate`, `data.originAttributes`, `data.originPrincipal`, `data.originStoragePrincipal`, `data.triggeringPrincipal`, `wgp.browsingContext`, `wgp.browsingContext.usePrivateBrowsing`, `wgp.documentPrincipal`, `wgp.documentPrincipal?.originAttributes`, `wgp.documentStoragePrincipal`

## MiddleMousePasteHandlerParent.receiveMessage()
- 位置: L30-43
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (message.name == "MiddleClickPaste")` → `fillInClickEvent()`
- 条件付き依存: `if (message.name == "MiddleClickPaste")` → `browser.documentGlobal.middleMousePaste()`
- 参照: `message.data`, `message.name`, `this.manager.browsingContext.top.embedderElement`

## ClickHandlerParent.addContentClickListener()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gContentClickListeners.add()`

## ClickHandlerParent.removeContentClickListener()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gContentClickListeners.delete()`

## ClickHandlerParent.receiveMessage()
- 位置: L55-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fillInClickEvent()`, `this.contentAreaClick()`, `this.notifyClickListeners()`
- 参照: `message.data`, `message.name`

## ClickHandlerParent.contentAreaClick()
- 位置: L71-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.whereToOpenLink()`, `lazy.E10SUtils.deserializePolicyContainer()`, `lazy.E10SUtils.deserializeReferrerInfo()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `window.openLinkIn()`
- 条件付き依存: `if (!lazy.PrivateBrowsingUtils.isWindowPrivate(window))` → `lazy.PlacesUIUtils.markPageAsFollowedLink()`
- 条件付き依存: `if (!(data.globalHistoryOptions))` → `browser.getAttribute()`
- 参照: `browser.characterSet`, `browser.documentGlobal`, `data.frameID`, `data.globalHistoryOptions`, `data.href`, `data.isContentWindowPrivate`, `data.originAttributes.userContextId`, `data.originPrincipal`, `data.originStoragePrincipal`, `data.policyContainer`, `data.referrerInfo`, `data.triggeringPrincipal`, `params.allowInheritPrincipal`, `params.globalHistoryOptions`, `params.userContextId`, `this.manager.browsingContext.top.embedderElement`, `this.manager.domProcess?.remoteType`, `window.openLinkIn`

## ClickHandlerParent.notifyClickListeners()
- 位置: L149-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `listener.onContentClick()`
- 参照: `this.browsingContext.top.embedderElement`
