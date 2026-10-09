# browser/components/sharing/SharingUtils.sys.mjs

source: browser/components/sharing/SharingUtils.sys.mjs
source-hash: a29e48e53f73fed67c0614ddc9b9b6553a1a245f
lines: 590

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `Object.defineProperty()`, `XPCOMUtils.defineLazyServiceGetters()`

## get()
- 位置: L23-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/macsharingservice;1"].getService()`
- 参照: `Ci.nsIMacSharingService`
- XPCOM: `nsIMacSharingService` / `@mozilla.org/widget/macsharingservice;1`

## get()
- 位置: L32-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/uriloader/external-protocol-service;1"].getService()`
- 参照: `Ci.nsIExternalProtocolService`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1`

## makeMacShareCustomItem()
- 位置: L41-48
- 役割: (未記入)
- 触るとき: (未記入)

## SharingUtilsCls.ensureShareMenu()
- 位置: L64-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `Cu.getWeakReference()`, `Services.prefs.getBoolPref()`, `browsers.some()`, `browsers?.map()`, `oldElement?.matches()`
- 条件付き依存: `if (!(oldElement?.matches(".share-tab-url-item")))` → `this.#createShareMenu()`
- 参照: `AppConstants.platform`, `b.currentURI`, `contextBrowser.currentURI`, `insertAfterEl.nextElementSibling`, `shareMenu.browsersToShare`, `shareMenu.contextBrowserToShare`, `shareMenu.hidden`
- XPCOM: `Services.prefs`

## SharingUtilsCls.#createShareMenu()
- 位置: L101-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `menu.appendChild()`, `menu.classList.add()`, `menuPopup.addEventListener()`, `menuPopup.setAttribute()`, `parentMenu.insertBefore()`
- 参照: `insertAfterEl.nextSibling`, `insertAfterEl.ownerDocument`, `insertAfterEl.parentNode`, `parentMenu.id`

## SharingUtilsCls.#createCopyLinkMenuItem()
- 位置: L130-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `item.classList.add()`

## SharingUtilsCls.showQRCode()
- 位置: L146-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.contextBrowserToShare?.get()`, `this.getLinkToShare()`
- 条件付き依存: `if (urlToShare && browser)` → `this.showQRCodePanel()`
- 参照: `node.documentGlobal`

## SharingUtilsCls.showQRCodePanel()
- 位置: async L154-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.qrcode.opened.add()`, `console.error()`, `lazy.QRCodeGenerator.generateQRCode()`, `win.gBrowser .getTabDialogBox()`, `win.gBrowser .getTabDialogBox(browser) .open()`, `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!tab.linkedPanel)` → `this.#waitForTabRestored()`
- 条件付き依存: `if (!(win.gBrowser.selectedTab === tab))` → `wait.cancel()`
- 参照: `tab.closing`, `tab.linkedBrowser`, `tab.linkedPanel`, `wait.promise`, `win.gBrowser.selectedTab`

## SharingUtilsCls.#waitForTabRestored()
- 位置: L198-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `tab.addEventListener()`

## cleanup()
- 位置: L200-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `tab.removeEventListener()`

## SharingUtilsCls.getLinkToShare()
- 位置: L216-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.contextBrowserToShare?.get()`
- 条件付き依存: `if (browser)` → `BrowserUtils.getShareableURL()`
- 条件付き依存: `if (maybeToShare)` → `gURLBar.makeURIReadable()`
- 参照: `browser.contentTitle`, `browser.currentURI`, `gURLBar.makeURIReadable(maybeToShare).displaySpec`, `node.documentGlobal`

## SharingUtilsCls.getLinksToShare()
- 位置: L238-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `weakRef.get()`
- 条件付き依存: `if (maybeToShare)` → `links.push()`
- 条件付き依存: `if (maybeToShare)` → `gURLBar.makeURIReadable()`
- 参照: `browser.contentTitle`, `browser.currentURI`, `gURLBar.makeURIReadable(maybeToShare).displaySpec`, `node.browsersToShare`, `node.contextBrowserToShare`, `node.documentGlobal`

## SharingUtilsCls.#initSharePopup()
- 位置: L258-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menuPopup.parentNode .closest()`, `menuPopup.parentNode .closest("menupopup") .addEventListener()`, `this.populateSharePopup()`

## SharingUtilsCls.populateSharePopup()
- 位置: L271-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `menuPopup.addEventListener()`, `menuPopup.appendChild()`, `menuPopup.firstChild.remove()`, `this.#createCopyLinkMenuItem()`, `this.getLinkToShare()`
- 条件付き依存: `if (isMultiTab)` → `this.getLinksToShare()`
- 条件付き依存: `if (!copyLinkEnabled)` → `copyItem.setAttribute()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.shareqrcode.enabled", false))` → `document.createXULElement()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.shareqrcode.enabled", false))` → `qrCodeItem.classList.add()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.shareqrcode.enabled", false))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!shouldEnable || isMultiTab)` → `qrCodeItem.setAttribute()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.shareqrcode.enabled", false))` → `menuPopup.appendChild()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `menuPopup.appendChild()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `document.createXULElement()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `winShareItem.classList.add()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!shouldEnable || isMultiTab)` → `winShareItem.setAttribute()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `menuPopup.appendChild()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.createXULElement()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `macPickerItem.classList.add()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!shouldEnable)` → `macPickerItem.setAttribute()`
- 参照: `AppConstants.platform`, `menuPopup.firstChild`, `menuPopup.ownerDocument`, `menuPopup.parentNode`, `node.browsersToShare`, `this.getLinksToShare(node).length`
- XPCOM: `Services.prefs`

## SharingUtilsCls.#onCommand()
- 位置: L342-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.classList.contains()`, `target.closest()`
- 条件付き依存: `if (target.classList.contains("share-qrcode-item"))` → `this.showQRCode()`
- 条件付き依存: `if (!(target.classList.contains("share-qrcode-item")))` → `target.classList.contains()`
- 条件付き依存: `if (target.classList.contains("share-copy-link"))` → `this.copyLink()`
- 条件付き依存: `if (!(target.classList.contains("share-copy-link")))` → `target.classList.contains()`
- 条件付き依存: `if (target.classList.contains("share-windows-item"))` → `this.shareOnWindows()`
- 条件付き依存: `if (!(target.classList.contains("share-windows-item")))` → `target.classList.contains()`
- 条件付き依存: `if (target.classList.contains("share-mac-picker-item"))` → `this.shareOnMacPicker()`
- 参照: `event.currentTarget.parentNode`, `event.target`

## SharingUtilsCls.onPopupHiding()
- 位置: L357-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.parentNode.closest()`, `event.target.querySelector()`, `event.target.removeEventListener()`, `menupopup?.removeEventListener()`
- 参照: `event.target.querySelector( ".share-tab-url-item" )?.menupopup`

## SharingUtilsCls.onPopupShowing()
- 位置: L370-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#initSharePopup()`
- 参照: `event.target`

## SharingUtilsCls.handleEvent()
- 位置: L374-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onCommand()`, `this.onPopupHiding()`, `this.onPopupShowing()`
- 参照: `aEvent.type`

## SharingUtilsCls.copyLink()
- 位置: L388-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getLinksToShare()`
- 条件付き依存: `if (links.length)` → `BrowserUtils.copyLinks()`
- 参照: `links.length`

## SharingUtilsCls.openPairingFlow()
- 位置: L395-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSync.openPairDevice()`

## SharingUtilsCls.sendToDevice()
- 位置: L399-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `panel.contextBrowserToShare?.get()`, `window.gSync .getSendTabTargets()`, `window.gSync .getSendTabTargets() .find()`, `window.gSync.sendTabsAndConfirm()`
- 参照: `browser.contentTitle`, `browser.currentURI`, `device.id`, `panel.documentGlobal`, `uri.spec`

## SharingUtilsCls.shareOnWindows()
- 位置: L426-433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.WindowsUIUtils.shareUrl()`, `this.getLinkToShare()`

## SharingUtilsCls.sendEmail()
- 位置: L435-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `encodeURIComponent()`, `lazy.ExternalProtocolService.loadURI()`, `this.getLinkToShare()`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## SharingUtilsCls.shareOnMacPicker()
- 位置: async L461-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MacSharingService.shareUrlWithPicker()`, `links.map()`, `makeMacShareCustomItem()`, `this.#formatLabel()`, `this.#resolvePickerAnchor()`
- 条件付き依存: `if (isMultiTab)` → `this.getLinksToShare()`
- 条件付き依存: `if (!(isMultiTab))` → `this.getLinkToShare()`
- 条件付き依存: `if (!(isMultiTab))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( injectQR && links.length && Services.prefs.getBoolPref("browser.shareqrcode.enabled", false) )` → `customItems.push()`
- 条件付き依存: `if ( injectQR && links.length && Services.prefs.getBoolPref("browser.shareqrcode.enabled", false) )` → `this.#makeQRCodeCustomItem()`
- 参照: `l.title`, `l.url`, `links.length`, `links[0].url`, `node.browsersToShare`
- XPCOM: `Services.prefs`

## handler()
- 位置: L503-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.copyLinks()`

## SharingUtilsCls.#formatLabel()
- 位置: async L516-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `msg?.attributes?.find()`, `node.ownerDocument.l10n.formatMessages()`
- 参照: `a.name`, `msg?.attributes?.find(a => a.name === "label")?.value`

## SharingUtilsCls.#makeQRCodeCustomItem()
- 位置: async L523-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeMacShareCustomItem()`, `node.contextBrowserToShare?.get()`, `this.#formatLabel()`
- 参照: `node.documentGlobal`

## handler()
- 位置: L530-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showQRCodePanel()`

## SharingUtilsCls.#resolvePickerAnchor()
- 位置: L534-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.classList.contains()`, `node.closest()`
- 条件付き依存: `if (node.closest("#tabContextMenu"))` → `node.contextBrowserToShare?.get()`
- 条件付き依存: `if (node.closest("#tabContextMenu"))` → `win.gBrowser?.getTabForBrowser()`
- 参照: `node.documentGlobal`, `win.gURLBar?.inputField`

## SharingUtilsCls.testOnlyMockUIUtils()
- 位置: L553-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`
- 参照: `Cu.isInAutomation`

## SharingUtilsCls.get()
- 位置: L559-566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-ui-utils;1"].getService()`
- 参照: `Ci.nsIWindowsUIUtils`
- XPCOM: `nsIWindowsUIUtils` / `@mozilla.org/windows-ui-utils;1`

## SharingUtilsCls.testOnlyMockExternalProtocolService()
- 位置: L570-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`
- 参照: `Cu.isInAutomation`

## SharingUtilsCls.get()
- 位置: L577-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/external-protocol-service;1" ].getService()`
- 参照: `Ci.nsIExternalProtocolService`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1`
