# browser/tools/mozscreenshots/mozscreenshots/extension/configurations/ControlCenter.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/configurations/ControlCenter.sys.mjs
source-hash: bcd421abebda63ee025a2def8b2b89d354f68495
lines: 287

## <module>
- 役割: (未記入)

## init()
- 位置: L29-29
- 役割: (未記入)
- 触るとき: (未記入)

## applyConfig()
- 位置: async L34-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L43-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.browserLoaded()`, `BrowserTestUtils.startLoadingURIString()`, `NetUtil.newChannel()`, `Services.wm.getMostRecentWindow()`, `channel.QueryInterface()`, `openIdentityPopup()`
- 参照: `Ci.nsIFileChannel`, `browserWindow.gBrowser`, `channel.file.path`, `gBrowser.selectedBrowser`
- XPCOM: [`nsIFileChannel`](../../../../../../netwerk/protocol/file/nsIFileChannel.idl.md) / `Services.wm`

## applyConfig()
- 位置: async L63-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L71-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L79-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L87-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L95-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `SitePermissions.setForPrincipal()`, `loadPage()`, `openIdentityPopup()`
- 参照: `SitePermissions.ALLOW`
- XPCOM: `Services.scriptSecurityManager`

## applyConfig()
- 位置: async L113-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`, `SitePermissions.listPermissions()`, `SitePermissions.listPermissions().forEach()`, `SitePermissions.setForPrincipal()`, `loadPage()`, `openIdentityPopup()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.BLOCK`
- XPCOM: `Services.scriptSecurityManager`

## applyConfig()
- 位置: async L136-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L144-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L152-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L160-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L168-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L176-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L184-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L192-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loadPage()`, `openIdentityPopup()`

## applyConfig()
- 位置: async L200-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `loadPage()`, `openProtectionsPopup()`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L210-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `UrlClassifierTestUtils.addTestTrackers()`, `loadPage()`, `openProtectionsPopup()`
- XPCOM: `Services.prefs`

## applyConfig()
- 位置: async L221-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.browserLoaded()`, `Services.prefs.setBoolPref()`, `Services.wm.getMostRecentWindow()`, `UrlClassifierTestUtils.addTestTrackers()`, `gBrowser.documentGlobal.gProtectionsHandler.disableForCurrentPage()`, `loadPage()`, `openProtectionsPopup()`
- 参照: `browserWindow.gBrowser`, `gBrowser.selectedBrowser`
- XPCOM: `Services.prefs` / `Services.wm`

## loadPage()
- 位置: async L244-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserTestUtils.browserLoaded()`, `BrowserTestUtils.startLoadingURIString()`, `Services.wm.getMostRecentWindow()`
- 参照: `browserWindow.gBrowser`, `gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## openIdentityPopup()
- 位置: async L251-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `gIdentityHandler._identityIconBox.click()`, `gIdentityHandler._identityPopup.hidePopup()`, `gIdentityHandler._initializePopup()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `gIdentityHandler._identityPopup.classList.add()`
- 条件付き依存: `if (expand)` → `setTimeout()`
- 条件付き依存: `if (expand)` → `gIdentityHandler._identityPopup .querySelector("#identity-popup-security-button") .click()`
- 条件付き依存: `if (expand)` → `gIdentityHandler._identityPopup .querySelector()`
- 参照: `AppConstants.platform`, `browserWindow.gBrowser`, `gBrowser.documentGlobal`
- XPCOM: `Services.wm`

## openProtectionsPopup()
- 位置: async L272-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `gProtectionsHandler._initializePopup()`, `gProtectionsHandler._protectionsPopup.hidePopup()`, `gProtectionsHandler.showProtectionsPopup()`, `setTimeout()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `gProtectionsHandler._protectionsPopup.classList.add()`
- 参照: `AppConstants.platform`, `browserWindow.gBrowser`, `gBrowser.documentGlobal`
- XPCOM: `Services.wm`
