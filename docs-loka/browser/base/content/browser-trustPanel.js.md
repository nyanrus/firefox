# browser/base/content/browser-trustPanel.js

source: browser/base/content/browser-trustPanel.js
source-hash: 544866fac7ea28417b911a5a790893fa0d5db437
lines: 2139

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `this.#resetToggleSecDelay.bind()`

## TrustPanel.init()
- 位置: L198-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Services.obs.addObserver()`, `customElements.whenDefined()`, `customElements.whenDefined("breach-alert-panel").then()`, `document.getElementById()`
- 条件付き依存: `if (blocker.init)` → `blocker.init()`
- 条件付き依存: `if (breachAlertElement)` → `breachAlertElement.addEventListener()`
- 条件付き依存: `if (breachAlertElement)` → `this.dismissBreachAlert.bind()`
- 参照: `blocker.init`, `this.#blockers`
- XPCOM: `Services.obs`

## TrustPanel.uninit()
- 位置: L224-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (blocker.uninit)` → `blocker.uninit()`
- 参照: `blocker.uninit`, `this.#blockers`
- XPCOM: `Services.obs`

## TrustPanel.#popup()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## TrustPanel.#enabled()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`

## TrustPanel.#trackerCountEnabled()
- 位置: L243-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`

## TrustPanel.handleProtectionsButtonEvent()
- 位置: L250-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.showPopup()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## TrustPanel.onContentBlockingEvent()
- 位置: async L264-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`, `Object.values()`, `blocker.isBlocking()`, `blocker.isDetected()`, `this.#updateToolbarTrackerCount()`
- 条件付き依存: `if (this.#popup)` → `this.#updatePopup()`
- 参照: `blocker.activated`, `this.#blockers`, `this.#enabled`, `this.#lastEvent`, `this.#popup`, `this.#uri`, `this.anyDetected`, `this.hasException`, `window.gBrowser.selectedBrowser`

## TrustPanel.#initializePopup()
- 位置: L303-349
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#popup)` → `document.getElementById()`
- 条件付き依存: `if (!this.#popup)` → `wrapper.replaceWith()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-popup-connection") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById()`
- 条件付き依存: `if (!this.#popup)` → `this.#openSecurityInformationSubview()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-blocker-see-all") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#openBlockerSubview()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-privacy-link") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#hidePopup()`
- 条件付き依存: `if (!this.#popup)` → `window.openTrustedLinkIn()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-clear-cookies-button") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#showClearCookiesSubview()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-siteinformation-morelink") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#showSecurityPopup()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-clear-cookie-cancel") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-clear-cookie-clear") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#clearSiteData()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-toggle") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#toggleTrackingProtection()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("identity-popup-remove-cert-exception") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#removeCertException()`
- 条件付き依存: `if (!this.#popup)` → `document .getElementById("trustpanel-popup-security-httpsonlymode-menulist") .addEventListener()`
- 条件付き依存: `if (!this.#popup)` → `this.#changeHttpsOnlyPermission()`
- 条件付き依存: `if (!this.#popup)` → `this.#popup.addEventListener()`
- 参照: `this.#popup`, `wrapper.content`

## TrustPanel.showPopup()
- 位置: async L351-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.trustpanel.opened.record()`, `PanelMultiView.openPopup()`, `Promise.all()`, `anchor?.setAttribute()`, `getBreachedStatus()`, `this.#anchor()`, `this.#computeTrackerCount()`, `this.#getApplicableBreaches()`, `this.#hasMonitorAccountOrStoredPasswords()`, `this.#initializePopup()`, `this.#updatePopup()`
- 条件付き依存: `if (this.#isSecureContext && !this.#qwacStatusPromise)` → `QWACs.determineQWACStatus( this.#secInfo, this.#uri, gBrowser.selectedBrowser.browsingContext ).then()`
- 条件付き依存: `if (this.#isSecureContext && !this.#qwacStatusPromise)` → `QWACs.determineQWACStatus()`
- 条件付き依存: `if (qwacStatusPromise == this.#qwacStatusPromise && result)` → `this.#updateSecurityInformationSubview()`
- 参照: `gBrowser.selectedBrowser.browsingContext`, `opts.event`, `opts.reason`, `this.#asciiHost`, `this.#isSecureContext`, `this.#openingReason`, `this.#popup`, `this.#qwac`, `this.#qwacStatusPromise`, `this.#secInfo`, `this.#uri`

## TrustPanel.#hidePopup()
- 位置: async L402-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `this.#popup.addEventListener()`
- 参照: `this.#popup`

## TrustPanel.#isWebPage()
- 位置: L417-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#uri.schemeIs()`
- 参照: `this.#uri`

## TrustPanel.#isSameSite()
- 位置: L432-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`
- XPCOM: `Services.eTLD`

## TrustPanel.resetIconForNavigation()
- 位置: L449-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `icon.classList.add()`, `icon.classList.remove()`, `this.#isSameSite()`
- 参照: `icon.classList`, `this.#blockersChecked`, `this.#enabled`, `this.#sameSiteNavigation`, `this.#trackerCountEnabled`, `this.#uri`

## TrustPanel.onNavigationComplete()
- 位置: L486-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateToolbarTrackerCount()`
- 条件付き依存: `if (!this.#blockersChecked)` → `this.#updateUrlbarIcon()`
- 参照: `this.#blockersChecked`, `this.#enabled`, `this.#trackerCountEnabled`, `this.#uri`

## TrustPanel.updateIdentity()
- 位置: L500-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByURI()`, `this.#checkForBreaches()`, `this.#isSameSite()`, `this.#updateToolbarTrackerCount()`, `this.#updateUrlbarIcon()`
- 条件付き依存: `if (this.#uri?.spec != uri.spec && this.#popup?.state == "open")` → `PanelMultiView.hidePopup()`
- 参照: `gBrowser.securityUI.secInfo`, `gBrowser.selectedBrowser`, `this.#blockersChecked`, `this.#breachedStatus`, `this.#enabled`, `this.#lastBrowser`, `this.#pageExtensionPolicy`, `this.#popup`, `this.#popup?.state`, `this.#qwac`, `this.#qwacStatusPromise`, `this.#sameSiteNavigation`, `this.#sameTabNavigation`, `this.#secInfo`, `this.#state`, `this.#uri`, `this.#uri?.spec`, `this.#uriHasHost`, `uri.host`, `uri.spec`

## TrustPanel.#checkForBreaches()
- 位置: async L557-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `getBreachedStatus()`, `this.#getApplicableBreaches()`, `this.#hasMonitorAccountOrStoredPasswords()`
- 条件付き依存: `if (breachedStatus !== "disabled" && breachedStatus !== "not-breached")` → `this.#updateUrlbarIcon()`
- 参照: `this.#asciiHost`, `this.#breachedStatus`, `this.#uri`

## TrustPanel.#anchor()
- 位置: L585-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchors.find()`, `document.getElementById()`, `element.checkVisibility()`
- 参照: `PopupNotifications.CHECK_VISIBILITY_OPTIONS`

## TrustPanel.#updateUrlbarIcon()
- 位置: L595-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `icon.classList.add()`, `icon.classList.toggle()`, `icon.setAttribute()`, `targetClasses.add()`, `targetClasses.has()`, `this.#computeTrackerCount()`, `this.#isSecurePage()`, `this.#isWebPage()`, `this.#tooltipText()`
- 条件付き依存: `if (this.#isSecurePage() && this.#breachedStatus === "breached")` → `targetClasses.add()`
- 条件付き依存: `if (!this.#trackingProtectionEnabled)` → `targetClasses.add()`
- 条件付き依存: `if (this.#isAboutNetErrorPage || this.#isCertUserOverridden)` → `targetClasses.add()`
- 条件付き依存: `if (this.#sameTabNavigation && !this.#sameSiteNavigation)` → `targetClasses.add()`
- 条件付き依存: `if (this.#trackerCountEnabled && this.#computeTrackerCount() > 0)` → `targetClasses.add()`
- 条件付き依存: `if (browser.lastAnimatedBreachURI !== this.#uri?.spec)` → `targetClasses.add()`
- 条件付き依存: `if (browser.lastAnimatedBreachURI !== this.#uri?.spec)` → `Glean.trustpanel.breachAlertShieldAnimated.record()`
- 条件付き依存: `if (!(browser.lastAnimatedBreachURI !== this.#uri?.spec))` → `icon.classList.contains()`
- 条件付き依存: `if (icon.classList.contains("breach-animating"))` → `targetClasses.add()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `this.#isFirstVisit(this.#uri.host).then()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `this.#isFirstVisit()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `Glean.trustpanel.trackerCountShown.record()`
- 条件付き依存: `if ( targetClasses.has("has-blocked-trackers") && browser.lastTrackerCountShownURI !== this.#uri?.spec )` → `targetClasses.has()`
- 条件付き依存: `if (!targetClasses.has(cls))` → `icon.classList.remove()`
- 参照: `browser.lastAnimatedBreachURI`, `browser.lastTrackerCountShownURI`, `gBrowser.selectedBrowser`, `icon.classList`, `this.#blockersChecked`, `this.#breachedStatus`, `this.#isAboutNetErrorPage`, `this.#isCertUserOverridden`, `this.#isInternalSecurePage`, `this.#sameSiteNavigation`, `this.#sameTabNavigation`, `this.#trackerCountEnabled`, `this.#trackingProtectionEnabled`, `this.#uri.host`, `this.#uri?.spec`

## TrustPanel.#updatePopup()
- 位置: async L683-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#connectionState()`, `this.#hasCustomRoot()`, `this.#popup.setAttribute()`, `this.#popup.toggleAttribute()`, `this.#tlsKeyLoggingEnabled()`, `this.#trackingProtectionStatus()`, `this.#updateMainView()`

## TrustPanel.#updateMainView()
- 位置: async L695-807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `PrivateBrowsingUtils.isWindowPrivate()`, `document.getElementById()`, `document.l10n.setAttributes()`, `getBreachedStatus()`, `hostElement.setAttribute()`, `this.#connectionLabel()`, `this.#getApplicableBreaches()`, `this.#hasMonitorAccountOrStoredPasswords()`, `this.#updateAttribute()`, `this.#updateBlockerView()`, `this.#updateToolbarTrackerCount()`, `toggle.toggleAttribute()`
- 条件付き依存: `if (breachedStatus !== "disabled" && breachedStatus !== "not-breached")` → `applicableBreaches.map()`
- 条件付き依存: `if (this.#uri)` → `PlacesUtils.favicons.getFaviconForPage()`
- 条件付き依存: `if (this.#uri)` → `document.getElementById()`
- 条件付き依存: `if (!isPrivate)` → `SiteDataManager.getBaseDomainFromHost()`
- 条件付き依存: `if (!isPrivate)` → `SiteDataManager.hasSiteData(baseDomain).then()`
- 条件付き依存: `if (!isPrivate)` → `SiteDataManager.hasSiteData()`
- 条件付き依存: `if (!isPrivate)` → `this.#updateAttribute()`
- 条件付き依存: `if (!isPrivate)` → `document.getElementById()`
- 参照: `assets.description`, `assets.header`, `assets.innerDescription`, `assets.label`, `breach.Name`, `breachAlertGraphicSection.breachNames`, `breachAlertGraphicSection.breachStatus`, `breachAlertGraphicSection.hidden`, `document.getElementById("trustpanel-popup-icon").src`, `favicon?.uri.spec`, `graphicSection.hidden`, `this.#asciiHost`, `this.#displayHost`, `this.#trackingProtectionEnabled`, `this.#uri`, `this.#uri.host`, `window.gBrowser.selectedBrowser`

## TrustPanel.#computeTrackerCount()
- 位置: L809-818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.values()`, `Object.values(log).filter()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `identifyType()`
- 参照: `logEntriesToCount.length`

## TrustPanel.#updateToolbarTrackerCount()
- 位置: L820-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `document.getElementById()`, `document.l10n.setArgs()`, `this.#computeTrackerCount()`, `this.#updateUrlbarIcon()`
- 条件付き依存: `if (count > 0 && !UrlbarPrefs.get("trackerCountShown"))` → `UrlbarPrefs.set()`
- 条件付き依存: `if (trackerCountLongform)` → `document.l10n.setArgs()`
- 参照: `this.#blockersChecked`, `this.#trackerCountEnabled`, `trackerCountShortform.textContent`

## TrustPanel.#updateBlockerView()
- 位置: L852-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `blocker.isBlocking()`, `document .getElementById()`, `document .getElementById("trustpanel-smartblock-section") .toggleAttribute()`, `document.getElementById()`, `document.l10n.setArgs()`, `this.#addButtons()`, `this.#addSmartblockEmbedToggles()`, `this.#computeTrackerCount()`, `this.#updateAttribute()`
- 条件付き依存: `if (blocker.isBlocking(this.#lastEvent))` → `blocked.push()`
- 条件付き依存: `if (!(blocker.isBlocking(this.#lastEvent)))` → `blocker.isDetected()`
- 条件付き依存: `if (blocker.isDetected(this.#lastEvent))` → `detected.push()`
- 参照: `this.#blockers`, `this.#lastEvent`

## TrustPanel.#showSecurityPopup()
- 位置: async L889-892
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hidePopup()`, `window.BrowserCommands.pageInfo()`

## TrustPanel.#removeCertException()
- 位置: L894-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserCommands.reloadSkipCache()`, `Cc["@mozilla.org/security/certoverride;1"].getService()`, `PanelMultiView.hidePopup()`, `overrideService.clearValidityOverride()`
- 参照: `Ci.nsICertOverrideService`, `gBrowser.contentPrincipal.originAttributes`, `this.#popup`, `this.#uri.host`, `this.#uri.port`
- XPCOM: `nsICertOverrideService` / `@mozilla.org/security/certoverride;1`

## TrustPanel.#trackingProtectionStatus()
- 位置: L907-912
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isSecurePage()`
- 参照: `this.#trackingProtectionEnabled`

## TrustPanel.#updateSecurityInformationSubview()
- 位置: L914-949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `element.toggleAttribute()`, `this.#ciphersState()`, `this.#connectionState()`, `this.#hasCustomRoot()`, `this.#httpsOnlyState()`, `this.#mixedContentState()`, `this.#supplementalText()`, `this.#tlsKeyLoggingEnabled()`, `this.#updateAttribute()`
- 参照: `document.getElementById("identity-popup-content-owner").textContent`, `document.getElementById("identity-popup-content-supplemental").textContent`, `document.getElementById("identity-popup-content-verifier").textContent`, `this.#displayHost`, `this.#isBrokenConnection`

## TrustPanel.#openSecurityInformationSubview()
- 位置: L951-956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `this.#updateSecurityInformationSubview()`
- 参照: `event.target`

## TrustPanel.#openBlockerSubview()
- 位置: L958-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `document.getElementById()`, `document.l10n.setAttributes()`, `this.#updateBlockerView()`
- 参照: `event.target`, `this.#displayHost`

## TrustPanel.#openBlockerDetailsSubview()
- 位置: async L970-1011
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blocker._generateSubViewListItems()`, `blocker.getBlockerCount()`, `blocker.subViewTitleL10nId()`, `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `document.getElementById()`, `document.getElementById("trustpanel-blocker-items").replaceChildren()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (titleL10nId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (titleL10nId)` → `document.getElementById()`
- 参照: `blocker.l10nKeys.content`, `blocker.l10nKeys.general`, `event.target`

## TrustPanel.#showClearCookiesSubview()
- 位置: async L1013-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("trustpanel-popup-multiView") .showSubView()`, `document.getElementById()`, `document.l10n.setAttributes()`
- 参照: `event.target`, `this.#displayHost`

## TrustPanel.#addButtons()
- 位置: async L1024-1052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `blocker.getBlockerCount()`, `blockers.map()`, `button.addEventListener()`, `button.classList.add()`, `button.setAttribute()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `sectionElement .querySelector()`, `sectionElement .querySelector(".trustpanel-blocker-buttons") .replaceChildren()`, `this.#openBlockerDetailsSubview()`
- 参照: `blocker.iconSrc`, `blocker.l10nKeys.general`, `blockers.length`, `sectionElement.hidden`

## TrustPanel.#trackingProtectionEnabled()
- 位置: L1054-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `ContentBlockingAllowList.includes()`
- 参照: `window.gBrowser.selectedBrowser`

## TrustPanel.#hasMonitorAccount()
- 位置: async L1061-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `attachedClients.some()`, `console.warn()`, `fxAccounts.listAttachedOAuthClients()`
- 参照: `UIState.STATUS_SIGNED_IN`, `client.id`, `state.status`, `this.#clearFxaOauthClientCache`

## TrustPanel.#hasStoredPasswords()
- 位置: async L1084-1092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.countLoginsAsync()`, `console.warn()`
- XPCOM: `Services.logins`

## TrustPanel.#hasMonitorAccountOrStoredPasswords()
- 位置: async L1094-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hasMonitorAccount()`, `this.#hasStoredPasswords()`

## TrustPanel.#isFirstVisit()
- 位置: async L1100-1114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.promiseDBConnection()`, `conn.executeCached()`, `host.split()`, `host.split("").reverse()`, `host.split("").reverse().join()`
- 参照: `rows.length`

## TrustPanel.#isSecurePage()
- 位置: L1116-1133
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isBrokenConnection`, `this.#isCertErrorPage`, `this.#isCertUserOverridden`, `this.#isInternalSecurePage`, `this.#isPotentiallyTrustworthy`, `this.#isSecureConnection`

## TrustPanel.#isInternalSecurePage()
- 位置: L1135-1146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#uri?.schemeIs()`
- 条件付き依存: `if (this.#uri?.schemeIs("about"))` → `E10SUtils.getAboutModule()`
- 条件付き依存: `if (module)` → `module.getURIFlags()`
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `this.#uri`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md)

## TrustPanel.#clearSiteData()
- 位置: L1148-1152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SiteDataManager.getBaseDomainFromHost()`, `SiteDataManager.remove()`, `this.#hidePopup()`
- 参照: `this.#uri.host`

## TrustPanel.#toggleTrackingProtection()
- 位置: L1154-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `window.BrowserCommands.reload()`
- 条件付き依存: `if (this.#trackingProtectionEnabled)` → `ContentBlockingAllowList.add()`
- 条件付き依存: `if (!(this.#trackingProtectionEnabled))` → `ContentBlockingAllowList.remove()`
- 参照: `this.#popup`, `this.#trackingProtectionEnabled`, `window.gBrowser.selectedBrowser`

## TrustPanel.#isHttpsOnlyModeActive()
- 位置: L1165-1167
- 役割: (未記入)
- 触るとき: (未記入)

## TrustPanel.#isHttpsFirstModeActive()
- 位置: L1169-1174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isHttpsOnlyModeActive()`

## TrustPanel.#isSchemelessHttpsFirstModeActive()
- 位置: L1175-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isHttpsFirstModeActive()`, `this.#isHttpsOnlyModeActive()`

## TrustPanel.#getIdentityData()
- 位置: L1186-1211
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split(",").forEach()`
- 条件付き依存: `if (cert.subjectName)` → `cert.subjectName.split()`
- 条件付き依存: `if (cert.subjectName)` → `v.split()`
- 参照: `cert.issuerCommonName`, `cert.issuerOrganization`, `cert.organization`, `cert.subjectName`, `result.caOrg`, `result.cert`, `result.city`, `result.country`, `result.state`, `result.subjectNameFields`, `result.subjectNameFields.C`, `result.subjectNameFields.L`, `result.subjectNameFields.ST`, `result.subjectOrg`, `this.#secInfo.serverCert`

## TrustPanel.#isSecureContext()
- 位置: L1213-1237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `console.error()`
- 参照: `gBrowser.contentPrincipal?.originNoSuffix`, `gBrowser.securityUI.isSecureContext`, `gBrowser.selectedBrowser.documentURI`, `principal.isOriginPotentiallyTrustworthy`
- XPCOM: `Services.scriptSecurityManager`

## TrustPanel.#hasCustomRoot()
- 位置: L1245-1252
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isCertUserOverridden`, `this.#isSecureConnection`, `this.#secInfo`, `this.#secInfo.isBuiltCertChainRootBuiltInRoot`

## TrustPanel.#tlsKeyLoggingEnabled()
- 位置: L1260-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.exists()`
- 参照: `this.#isCertUserOverridden`, `this.#isSecureConnection`
- XPCOM: `Services.env`

## TrustPanel.#isBrokenConnection()
- 位置: L1273-1275
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IS_BROKEN`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isSecureConnection()
- 位置: L1284-1293
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IS_SECURE`, `this.#isURILoadedFromFile`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#displayHost()
- 位置: L1298-1305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.formatURIForDisplay()`
- 参照: `this.#uri`

## TrustPanel.#asciiHost()
- 位置: L1310-1319
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#uri`, `this.#uri.asciiHost`

## TrustPanel.#isEV()
- 位置: L1321-1330
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_EV_TOPLEVEL`, `this.#isURILoadedFromFile`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isAssociatedIdentity()
- 位置: L1332-1334
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_IDENTITY_ASSOCIATED`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isMixedActiveContentLoaded()
- 位置: L1336-1340
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isMixedActiveContentBlocked()
- 位置: L1342-1346
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_MIXED_ACTIVE_CONTENT`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isMixedPassiveContentLoaded()
- 位置: L1348-1352
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_DISPLAY_CONTENT`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isContentHttpsOnlyModeUpgraded()
- 位置: L1354-1358
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isContentHttpsOnlyModeUpgradeFailed()
- 位置: L1360-1365
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADE_FAILED`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isContentHttpsFirstModeUpgraded()
- 位置: L1367-1372
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_HTTPS_ONLY_MODE_UPGRADED_FIRST`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isCertUserOverridden()
- 位置: L1374-1376
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIWebProgressListener.STATE_CERT_USER_OVERRIDDEN`, `this.#state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#isCertErrorPage()
- 位置: L1378-1389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isSecurelyConnectedAboutNetErrorPage()
- 位置: L1391-1401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URLSearchParams(documentURI.query).get()`
- 参照: `documentURI.filePath`, `documentURI.query`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isAboutNetErrorPage()
- 位置: L1403-1406
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isAboutHttpsOnlyErrorPage()
- 位置: L1408-1413
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isPotentiallyTrustworthy()
- 位置: L1415-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.selectedBrowser.documentURI?.scheme`, `this.#isBrokenConnection`, `this.#isSecureContext`

## TrustPanel.#isAboutBlockedPage()
- 位置: L1423-1426
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `documentURI.filePath`, `documentURI?.scheme`, `gBrowser.selectedBrowser`

## TrustPanel.#isURILoadedFromFile()
- 位置: L1428-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#uri.schemeIs()`

## TrustPanel.qwacStatusPromise()
- 位置: L1436-1438
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#qwacStatusPromise`

## TrustPanel.#supplementalText()
- 位置: L1440-1477
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isSecureConnection)` → `this.#getIdentityData()`
- 条件付き依存: `if (this.#isEV || this.#qwac)` → `this.#getIdentityData()`
- 条件付き依存: `if (identityData.state && identityData.country)` → `gNavigatorBundle.getFormattedString()`
- 参照: `identityData.caOrg`, `identityData.city`, `identityData.country`, `identityData.state`, `identityData.subjectOrg`, `this.#getIdentityData().caOrg`, `this.#isEV`, `this.#isSecureConnection`, `this.#qwac`, `this.#secInfo.serverCert`

## TrustPanel.#tooltipText()
- 位置: L1479-1515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!this.#isCertUserOverridden)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!this.#isCertUserOverridden)` → `this.#getIdentityData()`
- 条件付き依存: `if (this.#isMixedActiveContentLoaded)` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && warnTextOnInsecure )` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!this.#isPotentiallyTrustworthy)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (this.#isCertUserOverridden)` → `gNavigatorBundle.getString()`
- 参照: `this.#getIdentityData().caOrg`, `this.#isBrokenConnection`, `this.#isCertUserOverridden`, `this.#isMixedActiveContentLoaded`, `this.#isPotentiallyTrustworthy`, `this.#isSecureConnection`, `this.#uriHasHost`

## TrustPanel.#connectionState()
- 位置: L1517-1550
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isAboutBlockedPage`, `this.#isAboutHttpsOnlyErrorPage`, `this.#isAboutNetErrorPage`, `this.#isAssociatedIdentity`, `this.#isCertErrorPage`, `this.#isCertUserOverridden`, `this.#isEV`, `this.#isInternalSecurePage`, `this.#isPotentiallyTrustworthy`, `this.#isSecureConnection`, `this.#isSecurelyConnectedAboutNetErrorPage`, `this.#isURILoadedFromFile`, `this.#pageExtensionPolicy`, `this.#qwac`

## TrustPanel.#connectionLabel()
- 位置: L1552-1560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isSecurePage()`
- 参照: `this.#isAboutNetErrorPage`

## TrustPanel.#mixedContentState()
- 位置: L1562-1573
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isMixedPassiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this.#isMixedActiveContentLoaded)` → `mixedcontent.push()`
- 条件付き依存: `if (this.#isMixedActiveContentBlocked)` → `mixedcontent.push()`
- 参照: `this.#isMixedActiveContentBlocked`, `this.#isMixedActiveContentLoaded`, `this.#isMixedPassiveContentLoaded`

## TrustPanel.#ciphersState()
- 位置: L1575-1587
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isBrokenConnection`, `this.#isMixedActiveContentLoaded`, `this.#isMixedPassiveContentLoaded`

## TrustPanel.#httpsOnlyState()
- 位置: L1589-1642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this.#isHttpsFirstModeActive()`, `this.#isHttpsOnlyModeActive()`, `this.#isSchemelessHttpsFirstModeActive()`
- 条件付き依存: `if ( isHttpsFirstModeActive || isHttpsOnlyModeActive || isSchemelessHttpsFirstModeActive )` → `this.#getHttpsOnlyPermission()`
- 条件付き依存: `if ( isHttpsFirstModeActive || isHttpsOnlyModeActive || isSchemelessHttpsFirstModeActive )` → `document.getElementById()`
- 参照: `document.getElementById( "trustpanel-popup-security-httpsonlymode" ).hidden`, `document.getElementById( "trustpanel-popup-security-httpsonlymode-menulist" ).value`, `document.getElementById( "trustpanel-popup-security-menulist-off-item" ).hidden`, `this.#isAboutHttpsOnlyErrorPage`, `this.#isContentHttpsFirstModeUpgraded`, `this.#isContentHttpsOnlyModeUpgradeFailed`, `this.#isContentHttpsOnlyModeUpgraded`

## TrustPanel.#getHttpsOnlyPermission()
- 位置: L1649-1674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `SitePermissions.getForPrincipal()`, `uri.mutate()`, `uri.mutate().setScheme()`, `uri.mutate().setScheme("http").finalize()`, `uri.schemeIs()`
- 条件付き依存: `if (uri instanceof Ci.nsINestedURI)` → `uri.QueryInterface()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `uri.QueryInterface(Ci.nsINestedURI).innermostURI`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / `Services.scriptSecurityManager`

## TrustPanel.#changeHttpsOnlyPermission()
- 位置: L1679-1757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`, `document.getElementById()`, `newURI.mutate()`, `newURI.mutate().setScheme()`, `newURI.mutate().setScheme("http").finalize()`, `parseInt()`, `this.#getHttpsOnlyPermission()`
- 条件付き依存: `if (oldValue < 0)` → `console.error()`
- 条件付き依存: `if (newURI instanceof Ci.nsINestedURI)` → `newURI.QueryInterface()`
- 条件付き依存: `if (newValue === 0)` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (newValue === 1)` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!(newValue === 1))` → `SitePermissions.setForPrincipal()`
- 条件付き依存: `if (this.#isAboutHttpsOnlyErrorPage)` → `gBrowser.loadURI()`
- 条件付き依存: `if (this.#isAboutHttpsOnlyErrorPage)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this.#isAboutHttpsOnlyErrorPage)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `BrowserCommands.reloadSkipCache()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (newValue + oldValue !== 3)` → `gBrowser.selectedBrowser.focus()`
- 参照: `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW`, `Ci.nsIHttpsOnlyModePermission.LOAD_INSECURE_ALLOW_SESSION`, `Ci.nsINestedURI`, `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `SitePermissions.SCOPE_PERSISTENT`, `SitePermissions.SCOPE_SESSION`, `gBrowser.contentPrincipal.originAttributes`, `gBrowser.currentURI`, `menulist.selectedItem.value`, `newURI.QueryInterface(Ci.nsINestedURI).innermostURI`, `this.#isAboutHttpsOnlyErrorPage`, `this.#popup`
- XPCOM: [`nsIHttpsOnlyModePermission`](../../../dom/security/nsIHttpsOnlyModePermission.idl.md) / [`nsINestedURI`](../../../netwerk/base/nsINestedURI.idl.md) / [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## TrustPanel.#addSmartblockEmbedToggles()
- 位置: L1765-1847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.hidePopup()`, `container.insertAdjacentElement()`, `container.replaceChildren()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `gBrowser.selectedBrowser.getContentBlockingEvents()`, `shimId.toLowerCase()`, `this.#fetchSmartBlocked()`, `toggle.addEventListener()`, `toggle.setAttribute()`, `toggle.toggleAttribute()`
- 条件付き依存: `if (shimAllowed)` → `existingToggle.setAttribute()`
- 条件付き依存: `if (event.target.pressed)` → `this.#sendUnblockMessageToSmartblock()`
- 条件付き依存: `if (!(event.target.pressed))` → `this.#sendReblockMessageToSmartblock()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `blocked.length`, `event.target.pressed`, `this.#popup`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.#fetchSmartBlocked()
- 位置: L1849-1884
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `SMARTBLOCK_EMBED_INFO.find()`, `actions.some()`, `blocked.push()`, `gBrowser.selectedBrowser.getContentBlockingLog()`, `matchPatternSet.matches()`
- 参照: `Ci.nsIWebProgressListener.STATE_ALLOWED_TRACKING_CONTENT`, `Ci.nsIWebProgressListener.STATE_REPLACED_TRACKING_CONTENT`, `element.matchPatterns`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## TrustPanel.observe()
- 位置: async L1886-1919
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `multiview.getAttribute()`, `multiview.setAttribute()`, `this.#initializePopup()`, `this.#popup.addEventListener()`, `this.showPopup()`
- 参照: `gBrowser.selectedBrowser.browserId`, `subject.browserId`, `this.#clearFxaOauthClientCache`, `this.#enabled`

## TrustPanel.handleEvent()
- 位置: L1922-1949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elem.compareDocumentPosition()`, `this.#popup.hasAttribute()`, `this.onPopupHidden()`, `this.onPopupShown()`
- 条件付き依存: `if ( !( position & (Node.DOCUMENT_POSITION_CONTAINS | Node.DOCUMENT_POSITION_CONTAINED_BY) ) && !this.#popup.hasAttribute("noautohide") )` → `PanelMultiView.hidePopup()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `Node.DOCUMENT_POSITION_CONTAINS`, `document.activeElement`, `event.type`, `this.#popup`

## TrustPanel.onPopupShown()
- 位置: L1951-1962
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PopupNotifications.suppressWhileOpen()`, `window.addEventListener()`
- 条件付き依存: `if (this.#openingReason == "embedPlaceholderButton")` → `this.#disablePopupToggles()`
- 条件付き依存: `if (this.#openingReason == "embedPlaceholderButton")` → `setTimeout()`
- 条件付き依存: `if (this.#openingReason == "embedPlaceholderButton")` → `this.#enablePopupToggles()`
- 参照: `this.#openingReason`, `this.#popup`, `this.#popupToggleDelayTimer`

## TrustPanel.onPopupHidden()
- 位置: L1964-1969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(id)?.removeAttribute()`, `window.removeEventListener()`

## TrustPanel.#sendUnblockMessageToSmartblock()
- 位置: L1976-1982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## TrustPanel.#sendReblockMessageToSmartblock()
- 位置: L1989-1995
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `gBrowser.selectedTab`
- XPCOM: `Services.obs`

## TrustPanel.#resetToggleSecDelay()
- 位置: L1997-2002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `setTimeout()`, `this.#enablePopupToggles()`
- 参照: `this.#popupToggleDelayTimer`

## TrustPanel.#disablePopupToggles()
- 位置: L2004-2010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#popup.querySelectorAll()`, `this.#popup.querySelectorAll("moz-toggle").forEach()`, `toggle.addEventListener()`, `toggle.setAttribute()`
- 参照: `this.#resetToggleReference`

## TrustPanel.#enablePopupToggles()
- 位置: L2013-2024
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentBlockingAllowList.canHandle()`, `this.#popup.querySelectorAll()`, `this.#popup.querySelectorAll("moz-toggle").forEach()`, `toggle.removeEventListener()`
- 条件付き依存: `if ( toggle.id != "trustpanel-toggle" || ContentBlockingAllowList.canHandle(window.gBrowser.selectedBrowser) )` → `toggle.removeAttribute()`
- 参照: `this.#resetToggleReference`, `toggle.id`, `window.gBrowser.selectedBrowser`

## TrustPanel.#updateAttribute()
- 位置: L2026-2032
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `elem.setAttribute()`
- 条件付き依存: `if (!(value))` → `elem.removeAttribute()`

## TrustPanel.#getBreachAlertStorage()
- 位置: async L2034-2044
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#breachAlertStoragePromise === null)` → `initializeStorage()`
- 参照: `this.#breachAlertStoragePromise`

## initializeStorage()
- 位置: async L2036-2040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `storage.initialize()`

## TrustPanel.#getApplicableBreaches()
- 位置: async L2046-2074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await breachAlertStorage.getBreachAlertDismissals( recentBreaches.map(breach => breach.Name) ) ).map()`, `Services.eTLD.hasRootDomain()`, `breachAlertStorage.getBreachAlertDismissals()`, `breaches.filter()`, `breachesForSite.filter()`, `dismissedBreachNames.includes()`, `recentBreaches.filter()`, `recentBreaches.map()`, `this.#breachAlertsData.getAllBreaches()`, `this.#getBreachAlertStorage()`
- 参照: `breach.Domain`, `breach.Name`, `breachDismissal.breachName`, `breaches.length`, `recentBreach.Name`
- XPCOM: `Services.eTLD`

## TrustPanel.dismissBreachAlert()
- 位置: async L2076-2096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `breachAlertStorage.setBreachAlertDismissals()`, `breachNames.map()`, `console.error()`, `this.#getBreachAlertStorage()`, `this.#updateMainView()`, `this.#updateUrlbarIcon()`
- 参照: `event.detail.breachNames`, `this.#breachedStatus`

## isRecentBreach()
- 位置: L2103-2112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Temporal.Now.plainDateISO()`, `Temporal.PlainDate.compare()`, `Temporal.PlainDate.from()`, `currentDate.subtract()`
- 参照: `breach.BreachDate`

## getBreachedStatus()
- 位置: L2114-2136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `breaches.length`
