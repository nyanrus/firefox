# browser/base/content/webext-panels.js

source: browser/base/content/webext-panels.js
source-hash: 2b0b40a636f352bcb131e0030d0aef53f2784744
lines: 212

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## getBrowser()
- 位置: L19-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addEventListener()`, `browser.setAttribute()`, `document.createXULElement()`, `document.getElementById()`, `event.stopPropagation()`, `readyPromise.then()`, `stack.appendChild()`
- 条件付き依存: `if (browser)` → `Promise.resolve()`
- 条件付き依存: `if (panel.viewType === "sidebar" && gSidebarRevampEnabled)` → `customElements.get()`
- 条件付き依存: `if (!customElements.get("sidebar-panel-header"))` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (panel.viewType === "sidebar" && gSidebarRevampEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!stack)` → `document.createXULElement()`
- 条件付き依存: `if (!stack)` → `stack.setAttribute()`
- 条件付き依存: `if (!stack)` → `document.documentElement.appendChild()`
- 条件付き依存: `if (gAllowTransparentBrowser)` → `browser.setAttribute()`
- 条件付き依存: `if (panel.extension.remote)` → `browser.setAttribute()`
- 条件付き依存: `if (panel.extension.remote)` → `ChromeUtils.predictRemoteTypeForURI()`
- 条件付き依存: `if (panel.extension.remote)` → `promiseEvent()`
- 条件付き依存: `if (!(panel.extension.remote))` → `Promise.resolve()`
- 条件付き依存: `if (panel.viewType == "sidebar")` → `windowRoot.window.SidebarController.hide()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `browser.documentGlobal`, `browser.fullZoom`, `document.getElementById("sidebar-panel-header").heading`, `panel.extension.manifest.sidebar_action.default_title`, `panel.extension.name`, `panel.extension.policy.browsingContextGroupId`, `panel.extension.remote`, `panel.uri`, `panel.viewType`

## initBrowser()
- 位置: L122-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionParent.apiManager.emit()`, `browser.messageManager.loadFrameScript()`, `browser.messageManager.sendAsyncMessage()`
- 参照: `options.stylesheets`, `panel.browserInsertedData`, `panel.browserStyle`

## selectedBrowser()
- 位置: L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## getTabForBrowser()
- 位置: L154-156
- 役割: (未記入)
- 触るとき: (未記入)

## updatePosition()
- 位置: L159-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `requestAnimationFrame()`, `setTimeout()`
- 条件付き依存: `if (browser && browser.isRemoteBrowser)` → `browser.frameLoader.requestUpdatePosition()`
- 参照: `browser.isRemoteBrowser`

## loadPanel()
- 位置: L172-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`, `WebExtensionPolicy.getByID()`, `browser.fixupAndLoadURIString()`, `document.getElementById()`, `getBrowser()`, `getBrowser(sidebar).then()`, `policy.getURL()`
- 条件付き依存: `if (browserEl)` → `browserEl.parentNode.remove()`
- 参照: `browserEl.currentURI.spec`, `policy.extension`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`
