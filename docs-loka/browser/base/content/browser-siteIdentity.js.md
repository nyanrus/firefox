# browser/base/content/browser-siteIdentity.js

source: browser/base/content/browser-siteIdentity.js
source-hash: 16b222280f856e697f11fee76798cc2afe0bc239
lines: 1458

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _isBrokenConnection()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IS_BROKEN`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isSecureConnection()
- 位置: L87-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IS_SECURE`, `this._isURILoadedFromFile`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isEV()
- 位置: L98-107
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_EV_TOPLEVEL`, `this._isURILoadedFromFile`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isAssociatedIdentity()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_ASSOCIATED`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isMixedActiveContentLoaded()
- 位置: L113-117
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isMixedActiveContentBlocked()
- 位置: L119-123
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_MIXED_ACTIVE_CONTENT`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isMixedPassiveContentLoaded()
- 位置: L125-129
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_DISPLAY_CONTENT`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isContentHttpsOnlyModeUpgraded()
- 位置: L131-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isContentHttpsOnlyModeUpgradeFailed()
- 位置: L137-142
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADE_FAILED`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isContentHttpsFirstModeUpgraded()
- 位置: L144-149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED_FIRST`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isCertUserOverridden()
- 位置: L151-153
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_CERT_USER_OVERRIDDEN`, `this._state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _isCertErrorPage()
- 位置: L155-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isSecurelyConnectedAboutNetErrorPage()
- 位置: L168-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isAboutNetErrorPage()
- 位置: L180-183
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isAboutHttpsOnlyErrorPage()
- 位置: L185-190
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _isPotentiallyTrustworthy()
- 位置: L192-198
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.selectedBrowser.documentURI?.scheme`, `this._isBrokenConnection`, `this._isSecureContext`

## _isAboutBlockedPage()
- 位置: L200-203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## _initializePopup()
- 位置: L206-213
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._popupInitialized)` → `document.getElementById()`
- 条件付き依存: `if (!this._popupInitialized)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this._popupInitialized)` → `this._initializePopupListeners()`
- 参照: `this._popupInitialized`, `wrapper.content`

## _initializePopupListeners()
- 位置: L215-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `document.getElementById(id).addEventListener()`, `popup.addEventListener()`, `this.onPopupHidden()`, `this.onPopupShown()`
- 参照: `this._identityPopup`

## "identity-popup-security-button"()
- 位置: L225-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showSecuritySubView()`

## "identity-popup-security-httpsonlymode-menulist"()
- 位置: L228-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.changeHttpsOnlyPermission()`

## "identity-popup-clear-sitedata-button"()
- 位置: L231-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearSiteData()`

## "identity-popup-remove-cert-exception"()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeCertException()`

## "identity-popup-more-info"()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleMoreInfoClick()`

## hidePopup()
- 位置: L247-251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 参照: `this._identityPopup`, `this._popupInitialized`

## _identityPopup()
- 位置: L254-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopup`, `this._popupInitialized`

## _identityBox()
- 位置: L261-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityBox`

## _identityIconBox()
- 位置: L265-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityIconBox`

## _identityPopupMultiView()
- 位置: L270-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupMultiView`

## _identityPopupMainView()
- 位置: L276-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupMainView`

## _identityPopupMainViewHeaderLabel()
- 位置: L282-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupMainViewHeaderLabel`

## _identityPopupSecurityView()
- 位置: L288-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupSecurityView`

## _identityPopupHttpsOnlyMode()
- 位置: L294-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupHttpsOnlyMode`

## _identityPopupHttpsOnlyModeMenuList()
- 位置: L300-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupHttpsOnlyModeMenuList`

## _identityPopupHttpsOnlyModeMenuListOffItem()
- 位置: L306-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupHttpsOnlyModeMenuListOffItem`

## _identityPopupSecurityEVContentOwner()
- 位置: L311-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupSecurityEVContentOwner`

## _identityPopupContentOwner()
- 位置: L317-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupContentOwner`

## _identityPopupContentSupp()
- 位置: L323-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupContentSupp`

## _identityPopupContentVerif()
- 位置: L329-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupContentVerif`

## _identityPopupCustomRootLearnMore()
- 位置: L335-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityPopupCustomRootLearnMore`

## _identityPopupMixedContentLearnMore()
- 位置: L341-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelectorAll()`
- 参照: `this._identityPopupMixedContentLearnMore`

## _identityIconLabel()
- 位置: L348-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityIconLabel`

## _overrideService()
- 位置: L354-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/security/certoverride;1" ].getService()`
- 参照: `Ci.nsICertOverrideService`, `this._overrideService`
- XPCOM: `nsICertOverrideService` / `@mozilla.org/security/certoverride;1`

## _identityIcon()
- 位置: L360-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._identityIcon`

## _clearSiteDataFooter()
- 位置: L364-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._clearSiteDataFooter`

## _insecureConnectionTextEnabled()
- 位置: L370-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._insecureConnectionTextEnabled`

## _insecureConnectionTextPBModeEnabled()
- 位置: L379-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._insecureConnectionTextPBModeEnabled`

## _httpsOnlyModeEnabled()
- 位置: L388-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsOnlyModeEnabled`

## _httpsOnlyModeEnabledPBM()
- 位置: L397-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsOnlyModeEnabledPBM`

## _httpsFirstModeEnabled()
- 位置: L406-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsFirstModeEnabled`

## _httpsFirstModeEnabledPBM()
- 位置: L420-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._httpsFirstModeEnabledPBM`

## _schemelessHttpsFirstModeEnabled()
- 位置: L429-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this._schemelessHttpsFirstModeEnabled`

## _isHttpsOnlyModeActive()
- 位置: L439-444
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._httpsOnlyModeEnabled`, `this._httpsOnlyModeEnabledPBM`

## _isHttpsFirstModeActive()
- 位置: L445-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isHttpsOnlyModeActive()`
- 参照: `this._httpsFirstModeEnabled`, `this._httpsFirstModeEnabledPBM`

## _isSchemelessHttpsFirstModeActive()
- 位置: L452-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isHttpsFirstModeActive()`, `this._isHttpsOnlyModeActive()`
- 参照: `this._schemelessHttpsFirstModeEnabled`

## clearSiteData()
- 位置: async L463-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `SiteDataManager.getBaseDomainFromHost()`, `SiteDataManager.promptSiteDataRemoval()`, `event.stopPropagation()`, `this._identityPopup.addEventListener()`
- 条件付き依存: `if (SiteDataManager.promptSiteDataRemoval(window, [baseDomain]))` → `SiteDataManager.remove()`
- 参照: `this._identityPopup`, `this._uri.host`, `this._uriHasHost`

## handleMoreInfoClick()
- 位置: L490-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `displaySecurityInfo()`, `event.stopPropagation()`
- 参照: `this._identityPopup`

## showSecuritySubView()
- 位置: L496-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.clearFocus()`, `document.getElementById()`, `this._identityPopupMultiView.showSubView()`
- XPCOM: `Services.focus`

## removeCertException()
- 位置: L507-525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserCommands.reloadSkipCache()`, `this._overrideService.clearValidityOverride()`
- 条件付き依存: `if (!this._uriHasHost)` → `console.error()`
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 参照: `gBrowser.contentPrincipal.originAttributes`, `this._identityPopup`, `this._popupInitialized`, `this._uri.host`, `this._uri.port`, `this._uriHasHost`

## _getHttpsOnlyPermission()
- 位置: L532-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `SitePermissions.getForPrincipal()`, `uri.mutate()`, `uri.mutate().setScheme()`, `uri.mutate().setScheme("http").finalize()`, `uri.schemeIs()`
- 条件付き依存: `if (uri instanceof Ci.nsINestedURI)` → `uri.QueryInterface()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `uri.QueryInterface(Ci.nsINestedURI).innermostURI`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / `Services.scriptSecurityManager`

## changeHttpsOnlyPermission()
- 位置: L562-647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `newURI.mutate()`, `newURI.mutate().setScheme()`, `newURI.mutate().setScheme("http").finalize()`, `parseInt()`, `this._getHttpsOnlyPermission()`, `this.refreshIdentityPopup()`
- 条件付き依存: `if (oldValue < 0)` → `console.error()`
- 条件付き依存: `if (newURI instanceof Ci.nsINestedURI)` → `newURI.QueryInterface()`
- 条件付き依存: `if (newValue === 0)` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (newValue === 1)` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!(newValue === 1))` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (this._isAboutHttpsOnlyErrorPage)` → `gBrowser.loadURI()`
- 条件付き依存: `if (this._isAboutHttpsOnlyErrorPage)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this._popupInitialized)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `BrowserCommands.reloadSkipCache()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `gBrowser.selectedBrowser.focus()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_SESSION`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `newURI.QueryInterface(Ci.nsINestedURI).innermostURI`, `this._identityPopup`, `this._identityPopupHttpsOnlyModeMenuList.selectedItem.value`, `this._isAboutHttpsOnlyErrorPage`, `this._popupInitialized`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## getIdentityData()
- 位置: L653-678
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split(",").forEach()`
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split()`
- 条件付き依存: `if (cert.subjectName)` → `v.split()`
- 参照: `cert.issuerCommonName`, `cert.issuerOrganization`, `cert.organization`, `cert.subjectName`, `result.caOrg`, `result.cert`, `result.city`, `result.country`, `result.state`, `result.subjectNameFields`, `result.subjectNameFields.C`, `result.subjectNameFields.L`, `result.subjectNameFields.ST`, `result.subjectOrg`, `this._secInfo.serverCert`

## _getIsSecureContext()
- 位置: L680-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `console.error()`
- 参照: `gBrowser.contentPrincipal?.originNoSuffix`, `gBrowser.securityUI.isSecureContext`, `gBrowser.selectedBrowser.documentURI`, `principal.isOriginPotentiallyTrustworthy`
- XPCOM: `Services.scriptSecurityManager`

## updateIdentity()
- 位置: L718-744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getIsSecureContext()`, `this.refreshIdentityBlock()`, `this.setURI()`
- 条件付き依存: `if (locationChanged)` → `this.hidePopup()`
- 条件付き依存: `if (locationChanged)` → `gPermissionPanel.hidePopup()`
- 参照: `gBrowser.securityUI.secInfo`, `this._isSecureContext`, `this._qwac`, `this._qwacStatusPromise`, `this._secInfo`, `this._state`, `this._uri`, `this._uri.spec`, `uri.spec`

## getEffectiveHost()
- 位置: L751-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._IDNService.convertToDisplayIDN()`
- 条件付き依存: `if (!this._IDNService)` → `Cc["@mozilla.org/network/idn-service;1"].getService()`
- 参照: `Ci.nsIIDNService`, `this._IDNService`, `this._uri`, `uri.host`
- XPCOM: [`nsIIDNService`](../../../netwerk/dns/nsIIDNService.idl.md) / `@mozilla.org/network/idn-service;1`

## getHostForDisplay()
- 位置: L766-808
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ReaderMode.getOriginalUrlObjectForDisplay()`, `this.getEffectiveHost()`, `uri.schemeIs()`
- 参照: `readerStrippedURI.host`, `this._pageExtensionPolicy`, `this._pageExtensionPolicy.name`, `this._uri`, `uri.displaySpec`, `uri.filePath`, `uri.spec`, `uri.specIgnoringRef`

## pointerlockFsWarningClassName()
- 位置: L815-821
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isSecureConnection`, `this._uriHasHost`

## _hasCustomRoot()
- 位置: L829-836
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isCertUserOverridden`, `this._isSecureConnection`, `this._secInfo`, `this._secInfo.isBuiltCertChainRootBuiltInRoot`

## _hasInvalidPageProxyState()
- 位置: L843-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionUtils.isExtensionUrl()`, `isBlankPageURL()`
- 参照: `this._uri`, `this._uri.spec`, `this._uriHasHost`

## _refreshIdentityIcons()
- 位置: L855-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this._identityIcon.setAttribute()`, `this._identityIconLabel.setAttribute()`
- 条件付き依存: `if (this._isSecureInternalUI)` → `document.getElementById()`
- 条件付き依存: `if (this._isSecureInternalUI)` → `brandBundle.getString()`
- 条件付き依存: `if (this._pageExtensionPolicy)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (this._isMixedActiveContentBlocked)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (!this._isCertUserOverridden)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!this._isCertUserOverridden)` → `this.getIdentityData()`
- 条件付き依存: `if (this._isMixedActiveContentLoaded)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isMixedActiveContentLoaded)` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && warnTextOnInsecure )` → `gNavigatorBundle.getString()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && warnTextOnInsecure )` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isMixedPassiveContentLoaded)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (!(this._isMixedPassiveContentLoaded))` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isCertErrorPage)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!(this._isPotentiallyTrustworthy))` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (warnTextOnInsecure)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (warnTextOnInsecure)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isCertUserOverridden)` → `this._identityBox.classList.add()`
- 条件付き依存: `if (this._isCertUserOverridden)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (this._pageExtensionPolicy)` → `this._identityIcon.setAttribute()`
- 参照: `this._identityBox.className`, `this._identityIconLabel.collapsed`, `this._insecureConnectionTextEnabled`, `this._insecureConnectionTextPBModeEnabled`, `this._isAboutBlockedPage`, `this._isAboutHttpsOnlyErrorPage`, `this._isAboutNetErrorPage`, `this._isAssociatedIdentity`, `this._isBrokenConnection`, `this._isCertErrorPage`, `this._isCertUserOverridden`, `this._isMixedActiveContentBlocked`, `this._isMixedActiveContentLoaded`, `this._isMixedPassiveContentLoaded`, `this._isPotentiallyTrustworthy`, `this._isSecureConnection`, `this._isSecureInternalUI`, `this._pageExtensionPolicy`, `this._pageExtensionPolicy.name`, `this._uriHasHost`, `this.getIdentityData().caOrg`

## refreshIdentityBlock()
- 位置: L973-993
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gProtectionsHandler._trackingProtectionIconContainer.classList.toggle()`, `this._hasInvalidPageProxyState()`, `this._refreshIdentityIcons()`
- 条件付き依存: `if (this._hasInvalidPageProxyState())` → `gPermissionPanel.hidePermissionIcons()`
- 条件付き依存: `if (!(this._hasInvalidPageProxyState()))` → `gPermissionPanel.refreshPermissionIcons()`
- 参照: `this._identityBox`, `this._isSecureInternalUI`

## getConnectionSecurityInformation()
- 位置: L999-1030
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isAboutBlockedPage`, `this._isAboutHttpsOnlyErrorPage`, `this._isAboutNetErrorPage`, `this._isAssociatedIdentity`, `this._isCertErrorPage`, `this._isCertUserOverridden`, `this._isEV`, `this._isPotentiallyTrustworthy`, `this._isSecureConnection`, `this._isSecureInternalUI`, `this._isSecurelyConnectedAboutNetErrorPage`, `this._isURILoadedFromFile`, `this._pageExtensionPolicy`, `this._qwac`

## refreshIdentityPopup()
- 位置: L1037-1237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `document.getElementById()`, `document.l10n.setAttributes()`, `element.toggleAttribute()`, `gNavigatorBundle.getFormattedString()`, `identityPopupPanelView.removeAttribute()`, `mixedcontent.join()`, `this._hasCustomRoot()`, `this._isHttpsFirstModeActive()`, `this._isHttpsOnlyModeActive()`, `this._isSchemelessHttpsFirstModeActive()`, `this._updateAttribute()`, `this.getConnectionSecurityInformation()`, `this.getHostForDisplay()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && this._uriHasHost && !this._pageExtensionPolicy )` → `SiteDataManager.hasSiteData(this._uri.asciiHost).then()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && this._uriHasHost && !this._pageExtensionPolicy )` → `SiteDataManager.hasSiteData()`
- 条件付き依存: `if ( !PrivateBrowsingUtils.isWindowPrivate(window) && this._uriHasHost && !this._pageExtensionPolicy )` → `identityPopupPanelView.setAttribute()`
- 条件付き依存: `if (disableSecurityButton)` → `securityButtonNode.classList.remove()`
- 条件付き依存: `if (!(disableSecurityButton))` → `securityButtonNode.classList.add()`
- 条件付き依存: `if (this._isMixedPassiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this._isMixedActiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this._isMixedActiveContentBlocked)` → `mixedcontent.push()`
- 条件付き依存: `if ( isHttpsFirstModeActive || isHttpsOnlyModeActive || isSchemelessHttpsFirstModeActive )` → `this._getHttpsOnlyPermission()`
- 条件付き依存: `if (this._isEV || this._qwac)` → `this.getIdentityData()`
- 条件付き依存: `if (iData.state && iData.country)` → `gNavigatorBundle.getFormattedString()`
- 参照: `iData.city`, `iData.country`, `iData.state`, `iData.subjectOrg`, `securityButtonNode.disabled`, `this._clearSiteDataFooter.hidden`, `this._identityIconLabel.tooltipText`, `this._identityPopupContentOwner.textContent`, `this._identityPopupContentSupp.textContent`, `this._identityPopupContentVerif.textContent`, `this._identityPopupHttpsOnlyMode.hidden`, `this._identityPopupHttpsOnlyModeMenuList.value`, `this._identityPopupHttpsOnlyModeMenuListOffItem.hidden`, `this._identityPopupMainViewHeaderLabel`, `this._identityPopupSecurityEVContentOwner.textContent`, `this._identityPopupSecurityView`, `this._isAboutHttpsOnlyErrorPage`, `this._isBrokenConnection`, `this._isCertUserOverridden`, `this._isContentHttpsFirstModeUpgraded`, `this._isContentHttpsOnlyModeUpgradeFailed`, `this._isContentHttpsOnlyModeUpgraded`, `this._isEV`, `this._isMixedActiveContentBlocked`, `this._isMixedActiveContentLoaded`, `this._isMixedPassiveContentLoaded`, `this._isSecureConnection`, `this._pageExtensionPolicy`, `this._qwac`, `this._secInfo.serverCert`, `this._uri.asciiHost`, `this._uriHasHost`

## setURI()
- 位置: L1239-1269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByURI()`, `uri.QueryInterface()`, `uri.schemeIs()`
- 条件付き依存: `if (uri.schemeIs("about"))` → `E10SUtils.getAboutModule()`
- 条件付き依存: `if (module)` → `module.getURIFlags()`
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `Ci.nsINestedURI`, `this._isSecureInternalUI`, `this._isURILoadedFromFile`, `this._pageExtensionPolicy`, `this._uri`, `this._uri.host`, `this._uriHasHost`, `uri.QueryInterface(Ci.nsINestedURI).innerURI`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md)

## handleIdentityButtonEvent()
- 位置: L1274-1292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `gURLBar.getAttribute()`, `this._openPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## _openPopup()
- 位置: L1294-1329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `document.querySelectorAll()`, `this._initializePopup()`, `this.refreshIdentityPopup()`
- 条件付き依存: `if (this._isSecureContext && !this._qwacStatusPromise)` → `QWACs.determineQWACStatus( this._secInfo, this._uri, gBrowser.selectedBrowser.browsingContext ).then()`
- 条件付き依存: `if (this._isSecureContext && !this._qwacStatusPromise)` → `QWACs.determineQWACStatus()`
- 条件付き依存: `if (qwacStatusPromise == this._qwacStatusPromise && result)` → `this.refreshIdentityPopup()`
- 参照: `console.error`, `gBrowser.selectedBrowser.browsingContext`, `this._identityIconBox`, `this._identityPopup`, `this._isSecureContext`, `this._qwac`, `this._qwacStatusPromise`, `this._secInfo`, `this._uri`

## onPopupShown()
- 位置: L1331-1336
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this._identityPopup)` → `PopupNotifications.suppressWhileOpen()`
- 条件付き依存: `if (event.target == this._identityPopup)` → `window.addEventListener()`
- 参照: `event.target`, `this._identityPopup`

## onPopupHidden()
- 位置: L1338-1342
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this._identityPopup)` → `window.removeEventListener()`
- 参照: `event.target`, `this._identityPopup`

## handleEvent()
- 位置: L1344-1360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elem.compareDocumentPosition()`, `this._identityPopup.hasAttribute()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this._identityPopup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `this._identityPopup`

## observe()
- 位置: L1362-1377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.isSitePermission()`, `subject.QueryInterface()`
- 条件付き依存: `if (SitePermissions.isSitePermission(type))` → `this.refreshIdentityBlock()`
- 参照: `Ci.nsIPermission`
- XPCOM: [`nsIPermission`](../../../netwerk/base/nsIPermission.idl.md)

## onDragStart()
- 位置: L1379-1448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canvas.getContext()`, `ctx.drawImage()`, `ctx.fillRect()`, `ctx.fillText()`, `ctx.measureText()`, `document.createElementNS()`, `dt.setData()`, `dt.setDragImage()`, `gURLBar.getAttribute()`, `gURLBar.view.close()`, `parseInt()`
- 参照: `canvas.width`, `ctx.fillStyle`, `ctx.font`, `ctx.measureText(value).width`, `event.dataTransfer`, `gBrowser.contentTitle`, `gBrowser.currentURI.displaySpec`, `gBrowser.selectedTab.iconImage`, `image.src`, `image.width`, `tabIcon.src`, `window.devicePixelRatio`

## _updateAttribute()
- 位置: L1450-1456
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `elem.setAttribute()`
- 条件付き依存: `if (!(value))` → `elem.removeAttribute()`
