# browser/components/extensions/ExtensionPopups.sys.mjs

source: browser/components/extensions/ExtensionPopups.sys.mjs
source-hash: 71bbfb4be0bf9cf0dd7895dba779f30e72cf688a
lines: 793

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## promisePopupShown()
- 位置: L25-39
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (popup.state == "open")` → `resolve()`
- 条件付き依存: `if (!(popup.state == "open"))` → `popup.addEventListener()`
- 条件付き依存: `if (!(popup.state == "open"))` → `resolve()`
- 参照: `popup.state`

## addPanelHidingHandler()
- 位置: L41-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.addEventListener()`, `window.addEventListener()`, `window.removeEventListener()`, `window.setTimeout()`
- 参照: `lazy.delayBeforeEnablingButtons`, `panel.documentGlobal`

## handleClick()
- 位置: L42-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if ( event.target.closest( "panel:not(#unified-extensions-panel),#notifications-toolbar" ) )` → `event.preventDefault()`
- 条件付き依存: `if ( event.target.closest( "panel:not(#unified-extensions-panel),#notifications-toolbar" ) )` → `event.stopImmediatePropagation()`
- 条件付き依存: `if ( event.target.closest( "panel:not(#unified-extensions-panel),#notifications-toolbar" ) )` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## BasePopup.constructor()
- 位置: L71-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BasePopup.instances.get()`, `BasePopup.instances.get(this.window).set()`, `extension.callOnClose()`, `this.createBrowser()`, `this.panel.addEventListener()`, `this.viewNode.addEventListener()`, `this.window.addEventListener()`
- 参照: `this.DESTROY_EVENT`, `this._resolveContentReady`, `this.blockParser`, `this.browser`, `this.browserLoaded`, `this.browserLoadedDeferred`, `this.browserReady`, `this.browserStyle`, `this.contentReady`, `this.destroyed`, `this.extension`, `this.fixedWidth`, `this.popupURL`, `this.viewNode`, `this.window`, `viewNode.documentGlobal`

## BasePopup.for()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BasePopup.instances.get()`, `BasePopup.instances.get(window).get()`

## BasePopup.close()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closePopup()`

## BasePopup.destroy()
- 位置: L118-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BasePopup.instances.get()`, `BasePopup.instances.get(this.window).delete()`, `this._resolveContentReady()`, `this.browserLoaded.catch()`, `this.browserLoadedDeferred.reject()`, `this.browserReady.then()`, `this.extension.forgetOnClose()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this.browser)` → `this.destroyBrowser()`
- 条件付き依存: `if (this.browser)` → `this.browser.parentNode.remove()`
- 条件付き依存: `if (this.stack)` → `this.stack.remove()`
- 条件付き依存: `if (this.viewNode)` → `this.viewNode.removeEventListener()`
- 条件付き依存: `if (panel)` → `panel.removeEventListener()`
- 条件付き依存: `if (panel && panel.id !== REMOTE_PANEL_ID)` → `panel.style.removeProperty()`
- 条件付き依存: `if (panel && panel.id !== REMOTE_PANEL_ID)` → `panel.removeAttribute()`
- 参照: `panel.id`, `this.DESTROY_EVENT`, `this.browser`, `this.destroyed`, `this.extension`, `this.stack`, `this.viewNode`, `this.viewNode.customRectGetter`, `this.window`

## BasePopup.destroyBrowser()
- 位置: L164-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.removeEventListener()`
- 条件付き依存: `if (mm)` → `mm.removeMessageListener()`
- 参照: `browser.messageManager`, `this.receiveMessage`

## this.receiveMessage()
- 位置: L174-174
- 役割: (未記入)
- 触るとき: (未記入)

## BasePopup.DESTROY_EVENT()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)

## BasePopup.STYLESHEETS()
- 位置: L188-199
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.browserStyle)` → `sheets.push()`
- 条件付き依存: `if (!this.fixedWidth)` → `sheets.push()`
- 参照: `this.browserStyle`, `this.fixedWidth`

## BasePopup.panel()
- 位置: L201-207
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `panel.localName`, `panel.parentNode`, `this.viewNode`

## BasePopup.receiveMessage()
- 位置: L209-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._resolveContentReady()`, `this.browserLoadedDeferred.resolve()`, `this.setBackground()`
- 条件付き依存: `if (!(this.ignoreResizes))` → `this.resizeBrowser()`
- 参照: `data.background`, `this.dimensions`, `this.ignoreResizes`

## BasePopup.handleEvent()
- 位置: L230-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closePopup()`, `this.viewNode.setAttribute()`
- 条件付き依存: `if (!this.destroyed)` → `this.destroy()`
- 条件付き依存: `if (!this.destroyed)` → `this.browserLoaded .then()`
- 条件付き依存: `if (!this.destroyed)` → `this.browser.documentGlobal.promiseDocumentFlushed()`
- 条件付き依存: `if (!this.destroyed)` → `this.browser.messageManager.sendAsyncMessage()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `browser.documentGlobal`, `browser.fullZoom`, `event.target`, `event.type`, `this.DESTROY_EVENT`, `this.browser.contentTitle`, `this.browser.fullZoom`, `this.destroyed`

## BasePopup.createBrowser()
- 位置: L301-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addEventListener()`, `browser.fixupAndLoadURIString()`, `browser.setAttribute()`, `document.createXULElement()`, `initBrowser()`, `readyPromise.then()`, `stack.appendChild()`, `stack.setAttribute()`, `viewNode.appendChild()`
- 条件付き依存: `if (this.extension.remote)` → `browser.setAttribute()`
- 条件付き依存: `if (this.extension.remote)` → `promiseEvent()`
- 条件付き依存: `if (!(this.extension.remote))` → `promiseEvent()`
- 条件付き依存: `if (this.extension.remote)` → `readyPromise.then()`
- 条件付き依存: `if (this.extension.remote)` → `setupBrowser()`
- 条件付き依存: `if (!popupURL)` → `setupBrowser()`
- 参照: `browser.contentWindow`, `this.browser`, `this.extension.policy.browsingContextGroupId`, `this.extension.principal`, `this.extension.remote`, `this.extension.remoteType`, `this.stack`, `viewNode.ownerDocument`

## setupBrowser()
- 位置: L362-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addEventListener()`, `lazy.ExtensionParent.apiManager.emit()`, `mm.addMessageListener()`
- 参照: `browser.messageManager`

## initBrowser()
- 位置: L379-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mm.loadFrameScript()`, `mm.sendAsyncMessage()`, `setupBrowser()`
- 参照: `browser.messageManager`, `this.STYLESHEETS`, `this.blockParser`, `this.fixedWidth`

## BasePopup.unblockParser()
- 位置: L419-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browser.messageManager.sendAsyncMessage()`, `this.browserReady.then()`
- 参照: `this.blockParser`, `this.destroyed`

## BasePopup.resizeBrowser()
- 位置: L434-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browser.dispatchEvent()`
- 条件付き依存: `if (this.fixedWidth)` → `this.panel.getAttribute()`
- 条件付き依存: `if (this.fixedWidth)` → `Math.min()`
- 条件付き依存: `if (this.fixedWidth)` → `Math.max()`
- 参照: `this.browser.style.height`, `this.browser.style.minHeight`, `this.browser.style.minWidth`, `this.browser.style.width`, `this.extraHeight`, `this.fixedWidth`, `this.lastCalculatedInViewHeight`, `this.viewHeight`, `this.window.CustomEvent`

## BasePopup.setBackground()
- 位置: L458-478
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.panel.id != "widget-overflow")` → `this.panel.style.setProperty()`
- 条件付き依存: `if (background == "#fff")` → `this.panel.style.setProperty()`
- 参照: `this.background`, `this.panel.id`

## PanelPopup.constructor()
- 位置: L489-517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addPanelHidingHandler()`, `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mainPopupSet").appendChild()`, `makeWidgetId()`, `panel.addEventListener()`, `panel.setAttribute()`, `super()`, `this.browser.dispatchEvent()`
- 条件付き依存: `if (extension.remote)` → `panel.setAttribute()`
- 参照: `extension.id`, `extension.remote`, `this.window.CustomEvent`

## PanelPopup.DESTROY_EVENT()
- 位置: L519-521
- 役割: (未記入)
- 触るとき: (未記入)

## PanelPopup.destroy()
- 位置: L523-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.destroy()`, `this.viewNode.remove()`
- 参照: `this.viewNode`

## PanelPopup.closePopup()
- 位置: L529-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promisePopupShown()`, `promisePopupShown(this.viewNode).then()`
- 条件付き依存: `if (this.viewNode.state == "closed")` → `this.destroy()`
- 条件付き依存: `if (this.viewNode && this.viewNode.hidePopup)` → `this.viewNode.hidePopup()`
- 参照: `this.viewNode`, `this.viewNode.hidePopup`, `this.viewNode.state`

## ViewPopup.constructor()
- 位置: L547-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.browser.classList.add()`
- 条件付き依存: `if (extension.remote)` → `document.getElementById()`
- 条件付き依存: `if (!panel)` → `createPanel()`
- 条件付き依存: `if (!(extension.remote))` → `createPanel()`
- 参照: `extension.remote`, `panel.id`, `this.attached`, `this.browser`, `this.ignoreResizes`, `this.shown`, `this.tempBrowser`, `this.tempPanel`, `window.document`

## createPanel()
- 位置: L557-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mainPopupSet").appendChild()`, `panel.setAttribute()`
- 条件付き依存: `if (remote)` → `panel.setAttribute()`

## ViewPopup.attach()
- 位置: async L612-732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Promise.all()`, `Promise.race()`, `addPanelHidingHandler()`, `lazy.setTimeout()`, `panel.getBoundingClientRect()`, `this.browser.dispatchEvent()`, `this.browser.swapDocShells()`, `this.browserLoaded.catch()`, `this.createBrowser()`, `this.destroyBrowser()`, `this.panel.addEventListener()`, `this.panel.removeEventListener()`, `this.removeTempPanel()`, `this.setBackground()`, `this.viewNode.addEventListener()`, `this.viewNode.removeEventListener()`, `this.viewNode.setAttribute()`, `this.window.promiseDocumentFlushed()`, `viewNode.getBoundingClientRect()`
- 条件付き依存: `if (this.extension.remote)` → `this.panel.setAttribute()`
- 条件付き依存: `if (!this.destroyed && !panel)` → `this.destroy()`
- 条件付き依存: `if (this.destroyed)` → `lazy.CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (this.destroyed)` → `this.closePopup()`
- 条件付き依存: `if (this.destroyed)` → `this.destroy()`
- 条件付き依存: `if (this.dimensions)` → `this.resizeBrowser()`
- 参照: `popupRect.bottom`, `popupRect.top`, `this.DESTROY_EVENT`, `this.attached`, `this.background`, `this.browser`, `this.browserReady`, `this.destroyed`, `this.dimensions`, `this.dimensions.width`, `this.extension`, `this.extension.remote`, `this.extraHeight`, `this.fixedWidth`, `this.ignoreResizes`, `this.panel`, `this.shown`, `this.viewHeight`, `this.viewNode`, `this.viewNode.customRectGetter`, `this.window`, `this.window.CustomEvent`, `viewNode.getBoundingClientRect().height`, `win.mozInnerScreenY`, `win.screen.availHeight`, `win.screen.availTop`

## this.viewNode.customRectGetter()
- 位置: L711-713
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.lastCalculatedInViewHeight`, `this.viewHeight`

## ViewPopup.removeTempPanel()
- 位置: L734-745
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.tempPanel.id !== REMOTE_PANEL_ID)` → `this.tempPanel.remove()`
- 条件付き依存: `if (this.tempBrowser)` → `this.tempBrowser.parentNode.remove()`
- 参照: `this.tempBrowser`, `this.tempPanel`, `this.tempPanel.id`

## ViewPopup.destroy()
- 位置: L747-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.destroy()`, `super.destroy().then()`, `this.removeTempPanel()`

## ViewPopup.DESTROY_EVENT()
- 位置: L753-755
- 役割: (未記入)
- 触るとき: (未記入)

## ViewPopup.closePopup()
- 位置: L757-765
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.shown)` → `lazy.CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (!(this.attached))` → `this.destroy()`
- 参照: `this.attached`, `this.destroyed`, `this.shown`, `this.viewNode`

## isGloballyBlockingOpenPopup()
- 位置: L770-792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.document.querySelectorAll()`
- 条件付き依存: `if (elem.state !== "closed" && elem.state !== "hiding")` → `previewPanel?.isHoverPanel()`
- 参照: `elem.state`, `window.gBrowser.tabContainer.previewPanel`
