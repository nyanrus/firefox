# browser/base/content/browser-siteProtections.js

source: browser/base/content/browser-siteProtections.js
source-hash: db1d8e05d21269aaa84cb3e431d5998560595929
lines: 2948

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## ProtectionCategory.constructor()
- 位置: L49-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `MozXULElement.insertFTLIfNeeded()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getPrefType()`, `document.getElementById()`
- 条件付き依存: `if ( Services.prefs.getPrefType(this.prefEnabled) == Services.prefs.PREF_BOOL )` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if ( Services.prefs.getPrefType(this.prefEnabled) == Services.prefs.PREF_BOOL )` → `this.updateCategoryItem.bind()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `Services.prefs.PREF_BOOL`, `this._flags`, `this._id`, `this.prefEnabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md) / `Services.prefs`

## ProtectionCategory.init()
- 位置: L103-103
- 役割: (未記入)
- 触るとき: (未記入)

## ProtectionCategory.uninit()
- 位置: L104-104
- 役割: (未記入)
- 触るとき: (未記入)

## ProtectionCategory.enabled()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._enabled`

## ProtectionCategory.categoryItem()
- 位置: L118-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._categoryItem`, `this._id`

## ProtectionCategory.blockingEnabled()
- 位置: L134-136
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.enabled`

## ProtectionCategory.subViewTitleL10nId()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.l10nKeys.title`

## ProtectionCategory.updateCategoryItem()
- 位置: L156-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.categoryItem.classList.toggle()`
- 参照: `gProtectionsHandler._protectionsPopup`, `this.enabled`

## ProtectionCategory.updateSubView()
- 位置: async L173-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._generateSubViewListItems()`, `this.subViewList.append()`
- 条件付き依存: `if (l10nId)` → `document.l10n.setAttributes()`
- 参照: `gProtectionsHandler.hasException`, `this._id`, `this.blockingEnabled`, `this.subView`, `this.subViewList.textContent`, `this.subViewShimAllowHint.hidden`

## ProtectionCategory._generateSubViewListItems()
- 位置: async L213-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `document.createDocumentFragment()`, `fragment.appendChild()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `this._createListItem()`

## ProtectionCategory.getBlockerCount()
- 位置: async L239-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._generateSubViewListItems()`
- 参照: `items?.childElementCount`

## ProtectionCategory._createListItem()
- 位置: L256-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.some()`, `document.createElementNS()`, `document.createXULElement()`, `label.setAttribute()`, `listItem.append()`, `listItem.classList.toggle()`, `this.isAllowing()`, `this.isBlocking()`, `this.isShimming()`
- 条件付き依存: `if (shimAllowed)` → `listItem.append()`
- 条件付き依存: `if (shimAllowed)` → `this._getShimAllowIndicator()`
- 参照: `label.className`, `label.tooltipText`, `label.value`, `listItem.className`, `this._flags.allow`

## ProtectionCategory._getShimAllowIndicator()
- 位置: L301-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowIndicator.classList.add()`, `document.createXULElement()`, `document.l10n.setAttributes()`

## ProtectionCategory.isBlocking()
- 位置: L317-319
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._flags.block`

## ProtectionCategory.isAllowing()
- 位置: L325-327
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._flags.load`

## ProtectionCategory.isDetected()
- 位置: L334-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAllowing()`, `this.isBlocking()`

## ProtectionCategory.isShimming()
- 位置: L343-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAllowing()`
- 参照: `this._flags.shim`

## FingerprintingProtection.constructor()
- 位置: L361-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_FINGERPRINTING_CONTENT`, `Ci.nsIWebProgressListener.STATE_BLOCKED_FINGERPRINTING_CONTENT`, `Ci.nsIWebProgressListener.STATE_LOADED_FINGERPRINTING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_FINGERPRINTING_CONTENT`, `this.enabledFPB`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## FingerprintingProtection.init()
- 位置: L384-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateEnabled()`
- 条件付き依存: `if (!this.#isInitialized)` → `Services.prefs.addObserver()`
- 参照: `this.#isInitialized`, `this.prefEnabled`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## FingerprintingProtection.uninit()
- 位置: L395-405
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isInitialized)` → `Services.prefs.removeObserver()`
- 参照: `this.#isInitialized`, `this.prefEnabled`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## FingerprintingProtection.updateEnabled()
- 位置: L407-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.enabledFPB`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.prefEnabled`, `this.prefFPPEnabled`, `this.prefFPPEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## FingerprintingProtection.observe()
- 位置: L415-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateCategoryItem()`, `this.updateEnabled()`

## FingerprintingProtection.enabled()
- 位置: L420-426
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.enabledFPB`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.isWindowPrivate`

## FingerprintingProtection.isBlocking()
- 位置: L428-442
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_SUSPICIOUS_FINGERPRINTING`, `this._flags.block`, `this.enabledFPPGlobally`, `this.enabledFPPInPrivateWindows`, `this.isWindowPrivate`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.constructor()
- 位置: L482-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_EMAILTRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_BLOCKED_TRACKING_CONTENT`, `this.emailTrackingProtectionEnabledGlobally`, `this.emailTrackingProtectionEnabledInPrivateWindows`, `this.enabledGlobally`, `this.enabledInPrivateWindows`, `this.prefAnnotationsLevel2Enabled`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabledInPrivateWindows`, `this.prefTrackingAnnotationTable`, `this.prefTrackingTable`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.init()
- 位置: L534-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateEnabled()`
- 条件付き依存: `if (!this.#isInitialized)` → `Services.prefs.addObserver()`
- 参照: `this.#isInitialized`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabled`, `this.prefEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## TrackingProtection.uninit()
- 位置: L552-566
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isInitialized)` → `Services.prefs.removeObserver()`
- 参照: `this.#isInitialized`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabled`, `this.prefEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## TrackingProtection.observe()
- 位置: L568-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateCategoryItem()`, `this.updateEnabled()`

## TrackingProtection.trackingProtectionLevel2Enabled()
- 位置: L573-576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.trackingTable.includes()`

## TrackingProtection.enabled()
- 位置: L578-586
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.emailTrackingProtectionEnabledGlobally`, `this.emailTrackingProtectionEnabledInPrivateWindows`, `this.enabledGlobally`, `this.enabledInPrivateWindows`, `this.isWindowPrivate`

## TrackingProtection.updateEnabled()
- 位置: L588-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.emailTrackingProtectionEnabledGlobally`, `this.emailTrackingProtectionEnabledInPrivateWindows`, `this.enabledGlobally`, `this.enabledInPrivateWindows`, `this.prefEmailTrackingProtectionEnabled`, `this.prefEmailTrackingProtectionEnabledInPrivateWindows`, `this.prefEnabled`, `this.prefEnabledInPrivateWindows`
- XPCOM: `Services.prefs`

## TrackingProtection.isAllowingLevel1()
- 位置: L602-608
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_LEVEL_1_TRACKING_CONTENT`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.isAllowingLevel2()
- 位置: L610-616
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_LEVEL_2_TRACKING_CONTENT`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrackingProtection.isAllowing()
- 位置: L618-620
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAllowingLevel1()`, `this.isAllowingLevel2()`

## TrackingProtection.updateSubView()
- 位置: async L622-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._generateSubViewListItems()`
- 条件付き依存: `if (!items.childNodes.length)` → `document.createXULElement()`
- 条件付き依存: `if (!items.childNodes.length)` → `emptyImage.classList.add()`
- 条件付き依存: `if (!items.childNodes.length)` → `emptyLabel.classList.add()`
- 条件付き依存: `if (!items.childNodes.length)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!items.childNodes.length)` → `items.appendChild()`
- 条件付き依存: `if (!items.childNodes.length)` → `this.subViewList.classList.add()`
- 条件付き依存: `if (!(!items.childNodes.length))` → `this.subViewList.classList.remove()`
- 条件付き依存: `if ( previousURI == gBrowser.currentURI.spec && previousWindow == gBrowser.selectedBrowser.innerWindowID )` → `this.subViewList.append()`
- 条件付き依存: `if ( previousURI == gBrowser.currentURI.spec && previousWindow == gBrowser.selectedBrowser.innerWindowID )` → `document.l10n.setAttributes()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.innerWindowID`, `gProtectionsHandler.hasException`, `items.childNodes.length`, `this.enabled`, `this.subView`, `this.subViewList.textContent`, `this.subViewShimAllowHint.hidden`

## TrackingProtection._createListItem()
- 位置: async L671-722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.some()`, `document.createElementNS()`, `document.createXULElement()`, `label.setAttribute()`, `listItem.append()`, `listItem.classList.toggle()`, `this.isAllowing()`, `this.isBlocking()`, `this.isShimming()`
- 条件付き依存: `if (shimAllowed)` → `listItem.append()`
- 条件付き依存: `if (shimAllowed)` → `this._getShimAllowIndicator()`
- 参照: `Ci.nsIWebProgressListener .STATE_LOADED_LEVEL_2_TRACKING_CONTENT`, `label.className`, `label.tooltipText`, `label.value`, `listItem.className`, `this._flags.allow`, `this.annotationsLevel2Enabled`, `this.trackingProtectionLevel2Enabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## ThirdPartyCookies.constructor()
- 位置: L737-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `document.getElementById()`, `super()`, `this.updateCategoryItem.bind()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.prefEnabled`, `this.prefEnabledValues`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.isBlocking()
- 位置: L777-793
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_ALL`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_BY_PERMISSION`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_FOREIGN`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_SOCIALTRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_TRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_PARTITIONED_TRACKER`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## ThirdPartyCookies.isDetected()
- 位置: L795-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isBlocking()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED`, `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED_SOCIALTRACKER`, `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED_TRACKER`, `SocialTracking.enabled`, `this.behaviorPref`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## ThirdPartyCookies.updateCategoryItem()
- 位置: L822-855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `super.updateCategoryItem()`
- 条件付き依存: `if (!(!this.enabled))` → `console.error()`
- 条件付き依存: `if (!(!this.enabled))` → `this.categoryLabel.removeAttribute()`
- 参照: `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.behaviorPref`, `this.categoryLabel`, `this.categoryLabel.textContent`, `this.enabled`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.enabled()
- 位置: L857-859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.prefEnabledValues.includes()`
- 参照: `this.behaviorPref`

## ThirdPartyCookies._generateSubViewListItems()
- 位置: L861-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `categoryNames.push()`, `document.createDocumentFragment()`, `fragment.appendChild()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `this._createListItem()`, `this._processContentBlockingLog()`
- 参照: `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `itemsToShow.length`, `this.behaviorPref`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.updateSubView()
- 位置: L889-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `box.appendChild()`, `categoryNames.push()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `this._createListItem()`, `this._processContentBlockingLog()`, `this.subViewList.appendChild()`, `this.subViewTitleL10nId()`
- 条件付き依存: `if (l10nId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!this.enabled)` → `document.l10n.setAttributes()`
- 参照: `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `box.className`, `gProtectionsHandler.hasException`, `itemsToShow.length`, `label.className`, `this.behaviorPref`, `this.enabled`, `this.subView`, `this.subViewHeading.hidden`, `this.subViewHeading.nextSibling.hidden`, `this.subViewHeading.nextSibling.nodeName`, `this.subViewList.textContent`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies.subViewTitleL10nId()
- 位置: L987-1011
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `this.behaviorPref`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## ThirdPartyCookies._getExceptionState()
- 位置: L1013-1028
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`, `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 参照: `Services.perms.UNKNOWN_ACTION`, `gBrowser.contentPrincipal`
- XPCOM: `Services.perms` / `Services.scriptSecurityManager`

## ThirdPartyCookies._clearException()
- 位置: L1030-1052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `Services.perms.getAllForPrincipal()`
- 条件付き依存: `if (perm.type == "3rdPartyStorage^" + origin)` → `Services.perms.removePermission()`
- 条件付き依存: `if ( perm.type == "cookie" && Services.eTLD.hasRootDomain(host, perm.principal.host) )` → `Services.perms.removePermission()`
- 参照: `Services.io.newURI(origin).host`, `Services.perms.all`, `gBrowser.contentPrincipal`, `perm.principal.host`, `perm.type`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.perms`

## ThirdPartyCookies._processContentBlockingLog()
- 位置: L1056-1136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `TrackingProtection.isAllowing()`, `origin.startsWith()`, `this._getExceptionState()`, `this.isBlocking()`, `this.isDetected()`
- 条件付き依存: `if (isFirstParty)` → `newLog.firstParty.push()`
- 条件付き依存: `if (isTracker)` → `newLog.trackers.push()`
- 条件付き依存: `if (!(isTracker))` → `newLog.thirdParty.push()`
- 参照: `Cr.NS_ERROR_HOST_IS_IP_ADDRESS`, `Cr.NS_ERROR_INSUFFICIENT_DOMAIN_LEVELS`, `e.result`, `gBrowser.currentURI`, `info.isAllowed`
- XPCOM: `Services.eTLD` / `Services.io`

## ThirdPartyCookies._createListItem()
- 位置: L1138-1193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElementNS()`, `document.createXULElement()`, `label.setAttribute()`, `listItem.append()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `listItem.classList.add()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `document.createXULElement()`
- 条件付き依存: `if (isAllowed)` → `listItem.classList.toggle()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `removeException.appendChild()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `removeException.addEventListener()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `this._clearException()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `removeException.remove()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `listItem.classList.toggle()`
- 条件付き依存: `if ( (isAllowed && exceptionState == Services.perms.ALLOW_ACTION) || (!isAllowed && exceptionState == Services.perms.DENY_ACTION) )` → `listItem.append()`
- 参照: `Services.perms.ALLOW_ACTION`, `Services.perms.DENY_ACTION`, `label.className`, `label.value`, `listItem.className`, `listItem.tooltipText`, `removeException.className`, `stateLabel.className`
- XPCOM: `Services.perms`

## SocialTrackingProtection.constructor()
- 位置: L1208-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `[ Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER, Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN, ].includes()`, `super()`, `this.updateCategoryItem.bind()`
- 参照: `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `Ci.nsIWebProgressListener.STATE_BLOCKED_SOCIALTRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_LOADED_SOCIALTRACKING_CONTENT`, `this.prefCookieBehavior`, `this.prefEnabled`, `this.prefSTPCookieEnabled`, `this.prefStpTpEnabled`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## SocialTrackingProtection.blockingEnabled()
- 位置: L1246-1251
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.enabled`, `this.rejectTrackingCookies`, `this.socialTrackingProtectionEnabled`

## SocialTrackingProtection.isBlockingCookies()
- 位置: L1253-1259
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_COOKIES_BLOCKED_SOCIALTRACKER`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## SocialTrackingProtection.isBlocking()
- 位置: L1261-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.isBlocking()`, `this.isBlockingCookies()`

## SocialTrackingProtection.isAllowing()
- 位置: L1265-1275
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.socialTrackingProtectionEnabled)` → `super.isAllowing()`
- 参照: `Ci.nsIWebProgressListener.STATE_COOKIES_LOADED_SOCIALTRACKER`, `this.socialTrackingProtectionEnabled`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## SocialTrackingProtection.updateCategoryItem()
- 位置: L1277-1291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.categoryItem.classList.toggle()`
- 条件付き依存: `if (this.enabled)` → `this.categoryItem.removeAttribute()`
- 条件付き依存: `if (!(this.enabled))` → `this.categoryItem.setAttribute()`
- 参照: `gProtectionsHandler._protectionsPopup`, `this.blockingEnabled`, `this.enabled`

## _initializePopup()
- 位置: L1347-1387
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._protectionsPopup)` → `document.getElementById()`
- 条件付き依存: `if (!this._protectionsPopup)` → `this._protectionsPopup.addEventListener()`
- 条件付き依存: `if (!this._protectionsPopup)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this._protectionsPopup)` → `this.maybeSetMilestoneCounterText()`
- 条件付き依存: `if (!this._protectionsPopup)` → `Object.values()`
- 条件付き依存: `if (!this._protectionsPopup)` → `blocker.updateCategoryItem()`
- 条件付き依存: `if (!this._protectionsPopup)` → `notBlockingWhy.addEventListener()`
- 条件付き依存: `if (!this._protectionsPopup)` → `document .getElementById( "protections-popup-trackers-blocked-counter-description" ) .addEventListener()`
- 条件付き依存: `if (!this._protectionsPopup)` → `document .getElementById()`
- 条件付き依存: `if (!this._protectionsPopup)` → `gProtectionsHandler.openProtections()`
- 参照: `this._protectionsPopup`, `this.blockers`, `wrapper.content`, `wrapper.content.firstElementChild`

## openTooltip()
- 位置: L1365-1367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(event.target.tooltip).openPopup()`
- 参照: `event.target`, `event.target.tooltip`

## closeTooltip()
- 位置: L1368-1370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(event.target.tooltip).hidePopup()`
- 参照: `event.target.tooltip`

## _hidePopup()
- 位置: L1389-1393
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._protectionsPopup)` → `PanelMultiView.hidePopup()`
- 参照: `this._protectionsPopup`

## iconBox()
- 位置: L1396-1401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.iconBox`

## _protectionsPopupMultiView()
- 位置: L1402-1407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMultiView`

## _protectionsPopupMainView()
- 位置: L1408-1413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMainView`

## _protectionsPopupMainViewHeaderLabel()
- 位置: L1414-1419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMainViewHeaderLabel`

## _protectionsPopupTPSwitch()
- 位置: L1420-1425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupTPSwitch`

## _protectionsPopupCategoryList()
- 位置: L1426-1431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupCategoryList`

## _protectionsPopupBlockingHeader()
- 位置: L1432-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupBlockingHeader`

## _protectionsPopupNotBlockingHeader()
- 位置: L1438-1443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupNotBlockingHeader`

## _protectionsPopupNotFoundHeader()
- 位置: L1444-1449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupNotFoundHeader`

## _protectionsPopupSmartblockContainer()
- 位置: L1450-1455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSmartblockContainer`

## _protectionsPopupSmartblockDescription()
- 位置: L1456-1460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSmartblockDescription`

## _protectionsPopupSmartblockToggleContainer()
- 位置: L1461-1465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSmartblockToggleContainer`

## _protectionsPopupSettingsButton()
- 位置: L1466-1471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupSettingsButton`

## _protectionsPopupFooter()
- 位置: L1472-1477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupFooter`

## _protectionsPopupTrackersCounterBox()
- 位置: L1478-1483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupTrackersCounterBox`

## _protectionsPopupTrackersCounterDescription()
- 位置: L1484-1490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupTrackersCounterDescription`

## _protectionsPopupFooterProtectionTypeLabel()
- 位置: L1491-1497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupFooterProtectionTypeLabel`

## _trackingProtectionIconTooltipLabel()
- 位置: L1498-1503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._trackingProtectionIconTooltipLabel`

## _trackingProtectionIconContainer()
- 位置: L1504-1509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._trackingProtectionIconContainer`

## noTrackersDetectedDescription()
- 位置: L1511-1516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.noTrackersDetectedDescription`

## _protectionsPopupMilestonesText()
- 位置: L1518-1523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._protectionsPopupMilestonesText`

## _notBlockingWhyLink()
- 位置: L1525-1530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._notBlockingWhyLink`

## init()
- 位置: L1551-1636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.values()`, `Services.obs.addObserver()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `parseInt()`, `this._resetToggleSecDelay.bind()`, `this.maybeSetMilestoneCounterText()`
- 条件付き依存: `if (blocker.init)` → `blocker.init()`
- 参照: `blocker.init`, `this._resetToggleSecDelay`, `this.blockers`
- XPCOM: `Services.obs`

## uninit()
- 位置: L1638-1647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (blocker.uninit)` → `blocker.uninit()`
- 参照: `blocker.uninit`, `this.blockers`
- XPCOM: `Services.obs`

## getTrackingProtectionLabel()
- 位置: L1649-1662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- 参照: `this.PREF_CB_CATEGORY`
- XPCOM: `Services.prefs`

## openPreferences()
- 位置: L1664-1666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openPreferences()`

## openProtections()
- 位置: L1668-1679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `switchToTabHavingURI()`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## showTrackersSubview()
- 位置: async L1681-1686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TrackingProtection.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showSocialblockerSubview()
- 位置: async L1688-1693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SocialTracking.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showCookiesSubview()
- 位置: async L1695-1700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ThirdPartyCookies.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showFingerprintersSubview()
- 位置: async L1702-1707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Fingerprinting.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## showCryptominersSubview()
- 位置: async L1709-1714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cryptomining.updateSubView()`, `this._protectionsPopupMultiView.showSubView()`

## shieldHistogramAdd()
- 位置: L1716-1723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.contentblocking.trackingProtectionShield.accumulateSingleSample()`, `PrivateBrowsingUtils.isWindowPrivate()`

## cryptominersHistogramAdd()
- 位置: L1725-1727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.contentblocking.cryptominersBlockedCount[value].add()`
- 参照: `Glean.contentblocking.cryptominersBlockedCount`

## fingerprintersHistogramAdd()
- 位置: L1729-1731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.contentblocking.fingerprintersBlockedCount[value].add()`
- 参照: `Glean.contentblocking.fingerprintersBlockedCount`

## handleProtectionsButtonEvent()
- 位置: L1733-1745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.showProtectionsPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## onPopupShown()
- 位置: L1747-1785
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `PopupNotifications.suppressWhileOpen()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `window.addEventListener()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._protectionsPopupTPSwitch.addEventListener()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._insertProtectionsPanelInfoMessage()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `event.target.hasAttribute()`
- 条件付き依存: `if (!event.target.hasAttribute("toast"))` → `Glean.securityUiProtectionspopup.openProtectionsPopup.record()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._trackingProtectionIconContainer.setAttribute()`
- 条件付き依存: `if (this._protectionsPopupOpeningReason == "embedPlaceholderButton")` → `this._disablePopupToggles()`
- 条件付き依存: `if (this._protectionsPopupOpeningReason == "embedPlaceholderButton")` → `setTimeout()`
- 条件付き依存: `if (this._protectionsPopupOpeningReason == "embedPlaceholderButton")` → `this._enablePopupToggles()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `ReportBrokenSite.updateParentMenu()`
- 参照: `event.target`, `this._protectionsPopup`, `this._protectionsPopupButtonDelay`, `this._protectionsPopupOpeningReason`, `this._protectionsPopupSmartblockContainer.hidden`, `this._protectionsPopupToggleDelayTimer`

## onPopupHidden()
- 位置: L1787-1800
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `window.removeEventListener()`
- 条件付き依存: `if (event.target == this._protectionsPopup)` → `this._protectionsPopupTPSwitch.removeEventListener()`
- 条件付き依存: `if (this._protectionsPopupToggleDelayTimer)` → `clearTimeout()`
- 条件付き依存: `if (this._protectionsPopupToggleDelayTimer)` → `this._enablePopupToggles()`
- 参照: `event.target`, `this._protectionsPopup`, `this._protectionsPopupOpeningReason`, `this._protectionsPopupToggleDelayTimer`

## onTrackingProtectionIconHoveredOrFocused()
- 位置: async L1802-1827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TrackingDBService.sumAllEvents()`, `document.l10n.setAttributes()`, `this._initializePopup()`, `this.getTrackingProtectionLabel()`, `this.maybeUpdateEarliestRecordedDateTooltip()`, `this.setTrackersBlockedCounter()`
- 参照: `this._protectionsPopupFooterProtectionTypeLabel`, `this._updatingFooter`

## onLocationChange()
- 位置: L1830-1872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`, `this.cryptominersHistogramAdd()`, `this.fingerprintersHistogramAdd()`, `this.iconBox.toggleAttribute()`, `this.shieldHistogramAdd()`
- 条件付き依存: `if ( this._previousURI == gBrowser.currentURI.spec && this._previousOuterWindowID == gBrowser.selectedBrowser.outerWindowID )` → `this.showProtectionsPopup()`
- 条件付き依存: `if (this._protectionsPopup)` → `this._protectionsPopup.toggleAttribute()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser`, `gBrowser.selectedBrowser.outerWindowID`, `this._previousOuterWindowID`, `this._previousURI`, `this._protectionsPopup`, `this._showToastAfterRefresh`, `this._trackingProtectionIconContainer.hidden`, `this.hadShieldState`, `this.hasException`

## notifyContentBlockingEvent()
- 位置: L1874-1896
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.currentURI`, `gBrowser.selectedBrowser`, `this._isStoppedState`, `this.anyDetected`, `uri.asciiHost`, `uri.host`, `uri.spec`
- XPCOM: `Services.obs`

## onStateChange()
- 位置: L1898-1909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.selectedBrowser.getContentBlockingEvents()`, `this.notifyContentBlockingEvent()`
- 参照: `Ci.nsIWebProgressListener.STATE_STOP`, `aWebProgress.isTopLevel`, `this._isStoppedState`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## updatePanelForBlockingEvent()
- 位置: L1915-1942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `blocker.categoryItem.classList.toggle()`, `blocker.categoryItem.hasAttribute()`, `blocker.isDetected()`, `this._protectionsPopup.toggleAttribute()`
- 条件付き依存: `if (this.anyDetected)` → `this.reorderCategoryItems()`
- 参照: `this.anyBlocking`, `this.anyDetected`, `this.blockers`, `this.hasException`, `this.noTrackersDetectedDescription.hidden`

## reportBlockingEventTelemetry()
- 位置: L1944-1983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cryptomining.isAllowing()`, `Cryptomining.isBlocking()`, `Fingerprinting.isAllowing()`, `Fingerprinting.isBlocking()`
- 条件付き依存: `if (this.hasException && !this.hadShieldState)` → `this.shieldHistogramAdd()`
- 条件付き依存: `if ( !this.hasException && this.anyBlocking && !this.hadShieldState )` → `this.shieldHistogramAdd()`
- 条件付き依存: `if (fingerprintingBlocking)` → `this.fingerprintersHistogramAdd()`
- 条件付き依存: `if (fingerprintingAllowing)` → `this.fingerprintersHistogramAdd()`
- 条件付き依存: `if (cryptominingBlocking)` → `this.cryptominersHistogramAdd()`
- 条件付き依存: `if (cryptominingAllowing)` → `this.cryptominersHistogramAdd()`
- 参照: `this.anyBlocking`, `this.hadShieldState`, `this.hasException`

## onContentBlockingEvent()
- 位置: L1985-2057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`, `Object.values()`, `["showing", "open"].includes()`, `blocker.categoryItem?.hasAttribute()`, `blocker.isBlocking()`, `blocker.isDetected()`, `this.iconBox.toggleAttribute()`, `this.reportBlockingEventTelemetry()`
- 条件付き依存: `if (!ContentBlockingAllowList.canHandle(gBrowser.selectedBrowser))` → `this.iconBox.removeAttribute()`
- 条件付き依存: `if (this.hasException)` → `this.showDisabledTooltipForTPIcon()`
- 条件付き依存: `if (this.anyBlocking)` → `this.showActiveTooltipForTPIcon()`
- 条件付き依存: `if (!(this.anyBlocking))` → `this.showNoTrackerTooltipForTPIcon()`
- 条件付き依存: `if (isPanelOpen)` → `this.updatePanelForBlockingEvent()`
- 条件付き依存: `if (!isSimulated)` → `this.notifyContentBlockingEvent()`
- 参照: `blocker.activated`, `gBrowser.selectedBrowser`, `this._categoryItemOrderInvalidated`, `this._lastEvent`, `this._protectionsPopup?.state`, `this.anyBlocking`, `this.anyDetected`, `this.blockers`, `this.hasException`

## onCommand()
- 位置: L2059-2135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityUiProtectionspopup.clickCookies.record()`, `Glean.securityUiProtectionspopup.clickCryptominers.record()`, `Glean.securityUiProtectionspopup.clickFingerprinters.record()`, `Glean.securityUiProtectionspopup.clickFullReport.record()`, `Glean.securityUiProtectionspopup.clickMilestoneMessage.record()`, `Glean.securityUiProtectionspopup.clickSettings.record()`, `Glean.securityUiProtectionspopup.clickSocial.record()`, `Glean.securityUiProtectionspopup.clickSubviewSettings.record()`, `Glean.securityUiProtectionspopup.clickTrackers.record()`, `PanelMultiView.hidePopup()`, `gProtectionsHandler.openPreferences()`, `gProtectionsHandler.openProtections()`, `gProtectionsHandler.showCookiesSubview()`, `gProtectionsHandler.showCryptominersSubview()`, `gProtectionsHandler.showFingerprintersSubview()`, `gProtectionsHandler.showSocialblockerSubview()`, `gProtectionsHandler.showTrackersSubview()`, `this.showProtectionsPopup()`
- 参照: `event.target.id`, `this._protectionsPopup`

## handleEvent()
- 位置: L2138-2173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elem.compareDocumentPosition()`, `this._protectionsPopup.hasAttribute()`, `this.onCommand()`, `this.onPopupHidden()`, `this.onPopupShown()`, `this.onTPSwitchCommand()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this._protectionsPopup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `event.type`, `this._protectionsPopup`

## observe()
- 位置: L2175-2201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hidePopup()`, `this.maybeUpdateEarliestRecordedDateTooltip()`, `this.showProtectionsPopup()`
- 参照: `gBrowser.selectedBrowser.browserId`, `subject.browserId`, `this._earliestRecordedDate`, `this.smartblockEmbedsEnabledPref`

## refreshProtectionsPopup()
- 位置: L2207-2243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `document.l10n.setAttributes()`, `gIdentityHandler.getHostForDisplay()`, `this._notBlockingWhyLink.setAttribute()`, `this._protectionsPopup.toggleAttribute()`, `this.maybeUpdateEarliestRecordedDateTooltip()`, `this.updateProtectionsToggle()`
- 条件付き依存: `if (this._milestoneTextSet && !expired)` → `this._protectionsPopup.setAttribute()`
- 条件付き依存: `if (this._milestoneTextSet && !expired)` → `NimbusFeatures.privacySecurityMessaging.recordExposureEvent()`
- 条件付き依存: `if (!(this._milestoneTextSet && !expired))` → `this._protectionsPopup.removeAttribute()`
- 参照: `this._milestoneTextSet`, `this._protectionsPopupMainViewHeaderLabel`, `this.anyBlocking`, `this.anyDetected`, `this.hasException`, `this.milestonePref`, `this.milestoneTimestampPref`

## updateProtectionsToggle()
- 位置: L2251-2263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `gIdentityHandler.getHostForDisplay()`, `toggle.toggleAttribute()`
- 参照: `this._TPSwitchCommanding`, `this._protectionsPopupTPSwitch`

## reorderCategoryItems()
- 位置: L2270-2334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `categoryItem.classList.contains()`, `categoryItem.hasAttribute()`, `categoryItem.parentNode.insertBefore()`, `categoryItem.removeAttribute()`, `this._addSmartblockEmbedToggles()`
- 条件付き依存: `if ( categoryItem.classList.contains("notFound") || categoryItem.hasAttribute("uidisabled") )` → `this._protectionsPopupCategoryList.insertAdjacentElement()`
- 条件付き依存: `if ( categoryItem.classList.contains("notFound") || categoryItem.hasAttribute("uidisabled") )` → `categoryItem.setAttribute()`
- 条件付き依存: `if (categoryItem.classList.contains("blocked") && !this.hasException)` → `categoryItem.parentNode.insertBefore()`
- 参照: `this._categoryItemOrderInvalidated`, `this._protectionsPopupBlockingHeader.hidden`, `this._protectionsPopupNotBlockingHeader.hidden`, `this._protectionsPopupNotFoundHeader`, `this._protectionsPopupNotFoundHeader.hidden`, `this._protectionsPopupSmartblockContainer`, `this._protectionsPopupSmartblockContainer.hidden`, `this.blockers`, `this.hasException`

## _addSmartblockEmbedToggles()
- 位置: L2342-2451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `actions.some()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.getContentBlockingEvents()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `matchPatternSet.matches()`, `shimId.toLowerCase()`, `this._protectionsPopupSmartblockToggleContainer.insertAdjacentElement()`, `this._protectionsPopupSmartblockToggleContainer.lastChild.remove()`, `this.smartblockEmbedInfo.find()`, `toggle.addEventListener()`, `toggle.setAttribute()`, `toggle.toggleAttribute()`
- 条件付き依存: `if (shimAllowed)` → `existingToggle.setAttribute()`
- 条件付き依存: `if (newToggleState)` → `this._sendUnblockMessageToSmartblock()`
- 条件付き依存: `if (!(newToggleState))` → `this._sendReblockMessageToSmartblock()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `element.matchPatterns`, `event.target.pressed`, `this._protectionsPopupSmartblockToggleContainer.lastChild`, `this.smartblockEmbedsEnabledPref`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## disableForCurrentPage()
- 位置: L2453-2459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.add()`
- 条件付き依存: `if (shouldReload)` → `this._hidePopup()`
- 条件付き依存: `if (shouldReload)` → `BrowserCommands.reload()`
- 参照: `gBrowser.selectedBrowser`

## enableForCurrentPage()
- 位置: L2461-2467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.remove()`
- 条件付き依存: `if (shouldReload)` → `this._hidePopup()`
- 条件付き依存: `if (shouldReload)` → `BrowserCommands.reload()`
- 参照: `gBrowser.selectedBrowser`

## onTPSwitchCommand()
- 位置: async L2469-2528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `Promise.race()`, `gBrowser.reloadTab()`, `gBrowser.tabContainer.addEventListener()`, `gBrowser.tabContainer.removeEventListener()`, `setTimeout()`, `this._protectionsPopup.toggleAttribute()`, `this.iconBox.toggleAttribute()`, `this.updateProtectionsToggle()`
- 条件付き依存: `if (newExceptionState)` → `this.showDisabledTooltipForTPIcon()`
- 条件付き依存: `if (!(newExceptionState))` → `this.showNoTrackerTooltipForTPIcon()`
- 条件付き依存: `if (newExceptionState)` → `this.disableForCurrentPage()`
- 条件付き依存: `if (newExceptionState)` → `Glean.securityUiProtectionspopup.clickEtpToggleOff.record()`
- 条件付き依存: `if (!(newExceptionState))` → `this.enableForCurrentPage()`
- 条件付き依存: `if (!(newExceptionState))` → `Glean.securityUiProtectionspopup.clickEtpToggleOn.record()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.outerWindowID`, `gBrowser.selectedTab`, `this._TPSwitchCommanding`, `this._previousOuterWindowID`, `this._previousURI`, `this._protectionsPopup`, `this._showToastAfterRefresh`

## onTabSelectHandler()
- 位置: L2517-2517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## setTrackersBlockedCounter()
- 位置: L2530-2553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._protectionsPopupTrackersCounterBox.toggleAttribute()`
- 条件付き依存: `if (this._earliestRecordedDate)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._earliestRecordedDate))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this._earliestRecordedDate))` → `this._protectionsPopupTrackersCounterDescription.removeAttribute()`
- 参照: `this._earliestRecordedDate`, `this._protectionsPopupTrackersCounterDescription`

## maybeSetMilestoneCounterText()
- 位置: async L2562-2583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TrackingDBService.getEarliestRecordedDate()`, `document.l10n.setAttributes()`, `this.milestoneListPref.includes()`
- 参照: `this._milestoneTextSet`, `this._protectionsPopup`, `this._protectionsPopupMilestonesText`, `this.milestonePref`, `this.milestonesEnabledPref`

## showDisabledTooltipForTPIcon()
- 位置: L2585-2594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this._trackingProtectionIconContainer`, `this._trackingProtectionIconTooltipLabel`

## showActiveTooltipForTPIcon()
- 位置: L2596-2605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this._trackingProtectionIconContainer`, `this._trackingProtectionIconTooltipLabel`

## showNoTrackerTooltipForTPIcon()
- 位置: L2607-2616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`
- 参照: `this._trackingProtectionIconContainer`, `this._trackingProtectionIconTooltipLabel`

## showProtectionsPopup()
- 位置: L2633-2691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `PanelMultiView.hidePopup()`, `PanelMultiView.openPopup()`, `document.querySelectorAll()`, `this._initializePopup()`, `this._protectionsPopup.toggleAttribute()`, `this.hasOwnProperty()`
- 条件付き依存: `if (this.hasOwnProperty("_lastEvent"))` → `this.updatePanelForBlockingEvent()`
- 条件付き依存: `if (this._toastPanelTimer)` → `clearTimeout()`
- 条件付き依存: `if (!toast)` → `this.refreshProtectionsPopup()`
- 条件付き依存: `if (toast)` → `this._protectionsPopup.addEventListener()`
- 条件付き依存: `if (toast)` → `setTimeout()`
- 条件付き依存: `if (toast)` → `PanelMultiView.hidePopup()`
- 参照: `console.error`, `this._lastEvent`, `this._protectionsPopup`, `this._protectionsPopupOpeningReason`, `this._protectionsPopupToastTimeout`, `this._toastPanelTimer`, `this._trackingProtectionIconContainer`, `this.trustPanelEnabledPref`

## maybeUpdateEarliestRecordedDateTooltip()
- 位置: async L2693-2715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TrackingDBService.getEarliestRecordedDate()`
- 条件付き依存: `if (typeof trackerCount !== "number")` → `TrackingDBService.sumAllEvents()`
- 条件付き依存: `if (date)` → `document.l10n.setAttributes()`
- 参照: `this._earliestRecordedDate`, `this._protectionsPopup`, `this._protectionsPopupTrackersCounterDescription`

## _sendUnblockMessageToSmartblock()
- 位置: L2722-2728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## _sendReblockMessageToSmartblock()
- 位置: L2735-2741
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## _dispatchUserAction()
- 位置: L2746-2773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.urlFormatter.formatURL()`, `SpecialMessageActions.handleAction()`, `console.error()`
- 条件付き依存: `if (!PrivateBrowsingUtils.isWindowPrivate(window))` → `Glean.securityUiProtectionspopup.clickProtectionspopupCfr.record()`
- 参照: `message.content.cta_type`, `message.content.cta_url`, `message.content.cta_where`, `message.id`, `window.gBrowser.selectedBrowser`
- XPCOM: `Services.urlFormatter`

## _attachCommandListener()
- 位置: L2778-2790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.addEventListener()`, `this._dispatchUserAction()`
- 条件付き依存: `if (e.key === "Enter" || e.key === " ")` → `this._dispatchUserAction()`
- 参照: `e.key`

## _insertProtectionsPanelInfoMessage()
- 位置: L2797-2875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `container.hasAttribute()`, `doc.getElementById()`, `panelContainer.addEventListener()`
- 条件付き依存: `if (!container.childElementCount)` → `this._createHeroElement()`
- 条件付き依存: `if (!container.childElementCount)` → `container.appendChild()`
- 条件付き依存: `if (!container.childElementCount)` → `infoButton.addEventListener()`
- 条件付き依存: `if ( !this.protectionsPanelMessageSeen && container.hasAttribute("disabled") )` → `toggleMessage()`
- 条件付き依存: `if (!this.protectionsPanelMessageSeen)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( this.protectionsPanelMessageSeen && !container.hasAttribute("disabled") )` → `toggleMessage()`
- 参照: `container.childElementCount`, `event.target.ownerDocument`, `this.protectionsPanelMessageSeen`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## toggleMessage()
- 位置: L2817-2838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `doc.querySelector()`, `panelContainer.hasAttribute()`
- 条件付き依存: `if (learnMoreLink)` → `container.toggleAttribute()`
- 条件付き依存: `if (learnMoreLink)` → `infoButton.toggleAttribute()`
- 条件付き依存: `if (learnMoreLink)` → `panelContainer.toggleAttribute()`
- 条件付き依存: `if ( panelContainer.hasAttribute("infoMessageShowing") && !PrivateBrowsingUtils.isWindowPrivate(window) )` → `Glean.securityUiProtectionspopup.openProtectionspopupCfr.record()`
- 参照: `learnMoreLink.disabled`, `message.id`

## _createElement()
- 位置: L2877-2886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createElementNS()`
- 条件付き依存: `if (options.classList)` → `node.classList.add()`
- 条件付き依存: `if (options.content)` → `doc.l10n.setAttributes()`
- 参照: `options.classList`, `options.content`, `options.content.string_id`

## _createHeroElement()
- 位置: L2888-2921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messageEl.appendChild()`, `messageEl.classList.add()`, `messageEl.setAttribute()`, `this._createElement()`, `wrapperEl.appendChild()`, `wrapperEl.classList.add()`
- 条件付き依存: `if (message.content.link_text)` → `this._createElement()`
- 条件付き依存: `if (message.content.link_text)` → `wrapperEl.appendChild()`
- 条件付き依存: `if (message.content.link_text)` → `this._attachCommandListener()`
- 条件付き依存: `if (!(message.content.link_text))` → `this._attachCommandListener()`
- 参照: `linkEl.disabled`, `message.content.body`, `message.content.link_text`, `message.content.title`

## _resetToggleSecDelay()
- 位置: L2923-2930
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `setTimeout()`, `this._enablePopupToggles()`
- 参照: `this._protectionsPopupButtonDelay`, `this._protectionsPopupToggleDelayTimer`

## _disablePopupToggles()
- 位置: L2932-2938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._protectionsPopup.querySelectorAll()`, `this._protectionsPopup.querySelectorAll("moz-toggle").forEach()`, `toggle.addEventListener()`, `toggle.setAttribute()`
- 参照: `this._resetToggleSecDelay`

## _enablePopupToggles()
- 位置: L2940-2946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._protectionsPopup.querySelectorAll()`, `this._protectionsPopup.querySelectorAll("moz-toggle").forEach()`, `toggle.removeAttribute()`, `toggle.removeEventListener()`
- 参照: `this._resetToggleSecDelay`
