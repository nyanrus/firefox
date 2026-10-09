# browser/fxr/content/fxrui.js

source: browser/fxr/content/fxrui.js
source-hash: 443c4afc2901073c69c3801df3110872ed26f2ec
lines: 291

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `XPCOMUtils.defineLazyScriptGetter()`, `document.getElementById()`, `setupBrowser()`, `setupNavButtons()`, `setupUrlBar()`, `window.addEventListener()`

## setupBrowser()
- 位置: L76-146
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.createXULElement)` → `document.createXULElement()`
- 条件付き依存: `if (document.createXULElement)` → `browser.setAttribute()`
- 条件付き依存: `if (document.createXULElement)` → `browser.classList.add()`
- 条件付き依存: `if (document.createXULElement)` → `document.getElementById("eBrowserContainer").appendChild()`
- 条件付き依存: `if (document.createXULElement)` → `document.getElementById()`
- 条件付き依存: `if (document.createXULElement)` → `browser.loadUrlWithSystemPrincipal()`
- 条件付き依存: `if (document.createXULElement)` → `browser.addProgressListener()`
- 条件付き依存: `if (document.createXULElement)` → `ChromeUtils.generateQI()`
- 条件付き依存: `if (document.createXULElement)` → `FullScreen.init()`
- 条件付き依存: `if (document.createXULElement)` → `Services.obs.notifyObservers()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `Ci.nsIWebProgress.NOTIFY_SECURITY`, `Ci.nsIWebProgress.NOTIFY_STATE_REQUEST`, `browser.fxrPermissionPrompt`, `browser.loadUrlWithSystemPrincipal`, `document.createXULElement`, `urlInput.value`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md) / `Services.obs`

## browser.loadUrlWithSystemPrincipal()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadURI()`

## onLocationChange()
- 位置: L103-110
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `backButton.disabled`, `browser.canGoBack`, `browser.canGoForward`, `browser.currentURI.spec`, `forwardButton.disabled`, `urlInput.value`

## onStateChange()
- 位置: L111-123
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_STOP`, `refreshButton.disabled`, `stopButton.disabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onSecurityChange()
- 位置: L124-132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IS_SECURE`, `secureIcon.style.visibility`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## setupNavButtons()
- 位置: L148-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `elem.addEventListener()`

## navButtonHandler()
- 位置: L158-186
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.disabled)` → `browser.goBack()`
- 条件付き依存: `if (!this.disabled)` → `browser.goForward()`
- 条件付き依存: `if (!this.disabled)` → `browser.reload()`
- 条件付き依存: `if (!this.disabled)` → `browser.stop()`
- 条件付き依存: `if (!this.disabled)` → `browser.loadUrlWithSystemPrincipal()`
- 条件付き依存: `if (!this.disabled)` → `openSettings()`
- 参照: `this.disabled`, `this.id`

## setupUrlBar()
- 位置: L194-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `urlInput.addEventListener()`, `urlInput.select()`
- 条件付き依存: `if (e.key == "Enter")` → `SearchService.init()`
- 条件付き依存: `if (e.key == "Enter")` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (e.key == "Enter")` → `Services.uriFixup.getFixupURIInfo()`
- 条件付き依存: `if (e.key == "Enter")` → `browser.loadUrlWithSystemPrincipal()`
- 条件付き依存: `if (e.key == "Enter")` → `browser.focus()`
- 参照: `Services.uriFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Services.uriFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Services.uriFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `e.key`, `preferredURI.spec`, `urlInput.value`
- XPCOM: `Services.uriFixup`

## openSettings()
- 位置: L229-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserSettingsUI.classList.add()`, `browserSettingsUI.loadURI()`, `browserSettingsUI.setAttribute()`, `document.createXULElement()`, `showModalContainer()`

## closeSettings()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearModalContainer()`

## showPrivacyPolicy()
- 位置: L245-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.loadUrlWithSystemPrincipal()`, `closeSettings()`

## showLicenseInfo()
- 位置: L250-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.loadUrlWithSystemPrincipal()`, `closeSettings()`

## showReportIssue()
- 位置: L255-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.loadUrlWithSystemPrincipal()`, `closeSettings()`

## permissionPrompt()
- 位置: L264-280
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currentPermissionRequest)` → `pendingPermissionRequests.push()`
- 条件付き依存: `if (!(currentPermissionRequest))` → `currentPermissionRequest.showPrompt()`
- 参照: `Ci.nsIContentPermissionRequest`
- XPCOM: [`nsIContentPermissionRequest`](../../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md)

## finishPrompt()
- 位置: L282-290
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pendingPermissionRequests.length)` → `pendingPermissionRequests.shift()`
- 条件付き依存: `if (pendingPermissionRequests.length)` → `currentPermissionRequest.showPrompt()`
- 参照: `pendingPermissionRequests.length`
