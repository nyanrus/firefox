# browser/components/preferences/privacy.js

source: browser/components/preferences/privacy.js
source-hash: 885d4e14e163597e0c2f12c20d70dc168435bda5
lines: 1959

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/parental-controls-service;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## setEventListener()
- 位置: L106-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback.bind()`, `document .getElementById()`, `document .getElementById(aId) .addEventListener()`

## setSyncFromPrefListener()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addSyncFromPrefListener()`, `document.getElementById()`

## setSyncToPrefListener()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addSyncToPrefListener()`, `document.getElementById()`

## setUpContentBlockingWarnings()
- 位置: L121-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`
- 参照: `Preferences.get("privacy.resistFingerprinting").value`, `Preferences.get("privacy.resistFingerprinting.pbmode").value`, `document.getElementById("fpiIncompatibilityWarning").hidden`, `document.getElementById("rfpIncompatibilityWarning").hidden`

## initTCPStandardSection()
- 位置: L130-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `cookieBehaviorPref.on()`, `updateTCPSectionVisibilityState()`

## updateTCPSectionVisibilityState()
- 位置: L132-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `cookieBehaviorPref.value`, `document.getElementById("etpStandardTCPBox").hidden`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## _updateTrackingProtectionUI()
- 位置: L154-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CONTENT_BLOCKING_PREFS.some()`, `PrivacySettingHelpers.shouldDisableETPCategoryControls()`, `Services.prefs.prefIsLocked()`, `TRACKING_PROTECTION_PREFS.some()`
- 条件付き依存: `if (PrivacySettingHelpers.shouldDisableETPCategoryControls())` → `setInputsDisabledState()`
- 条件付き依存: `if (tPPrefisLocked)` → `hideControllingExtension()`
- 条件付き依存: `if (tPPrefisLocked)` → `setInputsDisabledState()`
- 条件付き依存: `if (!(tPPrefisLocked))` → `handleControllingExtension( PREF_SETTING_TYPE, TRACKING_PROTECTION_KEY ).then()`
- 条件付き依存: `if (!(tPPrefisLocked))` → `handleControllingExtension()`
- XPCOM: `Services.prefs`

## setInputsDisabledState()
- 位置: L162-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `document .getElementById()`, `document .getElementById("contentBlockingOptionStandard") .classList.toggle()`, `document .getElementById("contentBlockingOptionStrict") .classList.toggle()`, `document.getElementById()`, `document.querySelectorAll()`
- 参照: `button.disabled`, `document.getElementById("standardRadio").disabled`, `document.getElementById("strictRadio").disabled`, `document.getElementById("trackingProtectionMenu").disabled`, `tpCheckbox.checked`, `tpCheckbox.disabled`
- XPCOM: `Services.obs`

## _initTrackingProtectionExtensionControl()
- 位置: L211-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `makeDisableControllingExtension()`, `setEventListener()`, `window.addEventListener()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L222-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPrivacyPane._updateTrackingProtectionUI()`

## _ensureTrackingProtectionExceptionListMigration()
- 位置: L242-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/url-classifier/exception-list-service;1" ].getService()`, `Services.prefs.getBoolPref()`, `exceptionListService.maybeMigrateCategoryPrefs()`
- 参照: `Ci.nsIUrlClassifierExceptionListService`
- XPCOM: [`nsIUrlClassifierExceptionListService`](../../../netwerk/url-classifier/nsIUrlClassifierExceptionListService.idl.md) / `@mozilla.org/url-classifier/exception-list-service;1` → `UrlClassifierExceptionListService` (netwerk/url-classifier/components.conf) / `Services.prefs`

## dnsOverHttpsResolvers()
- 位置: L261-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `providers.findIndex()`
- 条件付き依存: `if (defaultIndex == -1 && defaultURI)` → `providers.unshift()`
- 参照: `DoHConfigController.currentConfig.fallbackProviderURI`, `DoHConfigController.currentConfig.providerList`, `p.uri`

## updateDoHResolverList()
- 位置: L274-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`, `resolvers.findIndex()`
- 条件付き依存: `if (!currentURI)` → `Preferences.get()`
- 参照: `Preferences.get("network.trr.default_provider_uri").value`, `Preferences.get("network.trr.uri").value`, `customInput.hidden`, `menu.itemCount`, `menu.selectedIndex`, `menu.value`, `r.uri`, `this.dnsOverHttpsResolvers`

## populateDoHResolverList()
- 位置: L295-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityDohSettings.providerChoiceValue.record()`, `customInput.addEventListener()`, `document.getElementById()`, `document.l10n.setAttributes()`, `menu.addEventListener()`, `menu.appendItem()`, `menu.removeAllItems()`, `this.updateDoHResolverList()`, `updateURIPref()`
- 条件付き依存: `if (resolver.uri == defaultURI)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (menu.value == "custom")` → `updateURIPref()`
- 条件付き依存: `if (!(menu.value == "custom"))` → `Services.prefs.setStringPref()`
- 参照: `DoHConfigController.currentConfig.fallbackProviderURI`, `customInput.hidden`, `item.label`, `menu.value`, `otherInput.hidden`, `otherMenu.value`, `resolver.UIName`, `resolver.uri`, `this.dnsOverHttpsResolvers`
- XPCOM: `Services.prefs`

## updateURIPref()
- 位置: L327-338
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (customInput.value == "")` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(customInput.value == ""))` → `Services.prefs.setStringPref()`
- 参照: `customInput.value`
- XPCOM: `Services.prefs`

## updateDoHStatus()
- 位置: async L366-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `computeStatus()`, `document.getElementById()`, `document.l10n.setAttributes()`, `nameOrDomain()`, `setStatus()`
- 条件付き依存: `if (!hostname)` → `document.l10n.formatValue()`
- 条件付き依存: `if ( (mode == Ci.nsIDNSService.MODE_TRRFIRST || mode == Ci.nsIDNSService.MODE_TRRONLY) && lazy.gParentalControlsService?.parentalControlsEnabled )` → `Services.dns.getTRRSkipReasonName()`
- 条件付き依存: `if (confirmationStatus != Cr.NS_OK)` → `ChromeUtils.getXPCOMErrorName()`
- 条件付き依存: `if (!(confirmationStatus != Cr.NS_OK))` → `Services.dns.getTRRSkipReasonName()`
- 参照: `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRRONLY`, `Ci.nsITRRSkipReason.TRR_PARENTAL_CONTROL`, `Cr.NS_OK`, `Services.dns.currentTrrMode`, `Services.dns.currentTrrURI`, `Services.dns.lastConfirmationSkipReason`, `Services.dns.lastConfirmationStatus`, `URL.parse(trrURI)?.hostname`, `dohResolver.hidden`, `lazy.gParentalControlsService?.parentalControlsEnabled`, `statusLearnMore.hidden`, `steering.hidden`
- XPCOM: [`nsIDNSService`](../../../netwerk/dns/nsIDNSService.idl.md) / [`nsITRRSkipReason`](../../../netwerk/dns/nsITRRSkipReason.idl.md) / `Services.dns`

## setStatus()
- 位置: async L381-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValue()`, `document.l10n.setAttributes()`

## computeStatus()
- 位置: L392-413
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIDNSService.CONFIRM_DISABLED`, `Ci.nsIDNSService.CONFIRM_OK`, `Ci.nsIDNSService.CONFIRM_TRYING_OK`, `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRRONLY`, `Services.dns.currentTrrConfirmationState`, `Services.dns.currentTrrMode`, `lazy.gParentalControlsService?.parentalControlsEnabled`
- XPCOM: [`nsIDNSService`](../../../netwerk/dns/nsIDNSService.idl.md) / `Services.dns`

## nameOrDomain()
- 位置: L446-463
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DoHConfigController.currentConfig.providerList`, `DoHConfigController.currentConfig.providerSteering .providerList`, `resolver.UIName`, `resolver.uri`, `steering.hidden`

## highlightDoHCategoryAndUpdateStatus()
- 位置: L471-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `defaultOption.classList.add()`, `defaultOption.classList.remove()`, `document.getElementById()`, `enabledOption.classList.add()`, `enabledOption.classList.remove()`, `gPrivacyPane.updateDoHStatus()`, `offOption.classList.add()`, `offOption.classList.remove()`, `strictOption.classList.add()`, `strictOption.classList.remove()`
- 条件付き依存: `if (value == Ci.nsIDNSService.MODE_NATIVEONLY)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if ( value == Ci.nsIDNSService.MODE_TRRFIRST || value == Ci.nsIDNSService.MODE_TRRONLY )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (!Services.prefs.getStringPref("network.trr.uri"))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (value == Ci.nsIDNSService.MODE_TRROFF)` → `Services.prefs.clearUserPref()`
- 参照: `Ci.nsIDNSService.MODE_NATIVEONLY`, `Ci.nsIDNSService.MODE_TRRFIRST`, `Ci.nsIDNSService.MODE_TRROFF`, `Ci.nsIDNSService.MODE_TRRONLY`, `DoHConfigController.currentConfig.fallbackProviderURI`, `Preferences.get("network.trr.mode").value`, `document.getElementById("dohCategoryRadioGroup").selectedIndex`
- XPCOM: [`nsIDNSService`](../../../netwerk/dns/nsIDNSService.idl.md) / `Services.prefs`

## initDoH()
- 位置: L539-601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Preferences.get("network.trr.mode").on()`, `Preferences.get("network.trr.uri").on()`, `Services.obs.addObserver()`, `Services.prefs.getStringPref()`, `Services.prefs.prefIsLocked()`, `gPrivacyPane.updateDoHResolverList()`, `gPrivacyPane.updateDoHStatus()`, `setEventListener()`, `this.dnsOverHttpsResolvers.some()`, `this.highlightDoHCategoryAndUpdateStatus()`, `this.populateDoHResolverList()`, `window.addEventListener()`
- 条件付き依存: `if (uriPref && !this.dnsOverHttpsResolvers.some(e => e.uri == uriPref))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (uriPref && !this.dnsOverHttpsResolvers.some(e => e.uri == uriPref))` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (Services.prefs.prefIsLocked("network.trr.mode"))` → `document.getElementById()`
- 条件付き依存: `if (Services.prefs.prefIsLocked("network.trr.mode"))` → `Services.prefs.setStringPref()`
- 参照: `document.getElementById("dohCategoryRadioGroup").disabled`, `e.uri`, `gPrivacyPane.highlightDoHCategoryAndUpdateStatus`, `this.toggleExpansion`
- XPCOM: `Services.obs` / `Services.prefs`

## modeButtonPressed()
- 位置: L544-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityDohSettings.modeChangedButton.record()`, `Preferences.get()`, `parseInt()`
- 参照: `Preferences.get("network.trr.mode").value`, `e.target.id`, `e.target.value`

## unload()
- 位置: L580-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## initWebAuthn()
- 位置: L603-609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.getElementById()`
- 参照: `document.getElementById("openWindowsPasskeySettings").hidden`
- XPCOM: `Services.prefs`

## init()
- 位置: L615-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Preferences.get("browser.privatebrowsing.autostart").on()`, `Preferences.get("network.cookie.cookieBehavior").on()`, `Preferences.get("privacy.fingerprintingProtection").on()`, `Preferences.get("privacy.fingerprintingProtection.pbmode").on()`, `Preferences.get("privacy.firstparty.isolate").on()`, `Preferences.get("privacy.trackingprotection.enabled").on()`, `Preferences.get("privacy.trackingprotection.pbmode.enabled").on()`, `Services.obs.notifyObservers()`, `appendSearchKeywords()`, `document.getElementById()`, `gPrivacyPane.fingerprintingProtectionReadPrefs.bind()`, `gPrivacyPane.networkCookieBehaviorReadPrefs.bind()`, `gPrivacyPane.trackingProtectionReadPrefs.bind()`, `initSettingGroup()`, `setEventListener()`, `setSyncFromPrefListener()`, `setSyncToPrefListener()`, `signonBundle.getString()`, `this._ensureTrackingProtectionExceptionListMigration()`, `this._initMasterPasswordUI()`, `this._initOSAuthentication()`, `this._initPasswordGenerationUI()`, `this._initRelayIntegrationUI()`, `this._initTrackingProtectionExtensionControl()`, `this.fingerprintingProtectionReadPrefs()`, `this.initContentBlocking()`, `this.initDoH()`, `this.initListenersForExtensionControllingPasswordManager()`, `this.initPrivacySegmentation()`, `this.initWebAuthn()`, `this.networkCookieBehaviorReadPrefs()`, `this.readBlockCookies()`, `this.readBlockCookiesFrom()`, `this.readSavePasswords()`, `this.trackingProtectionReadPrefs()`, `this.writeBlockCookies()`, `this.writeBlockCookiesFrom()`
- 参照: `gPrivacyPane.changeMasterPassword`, `gPrivacyPane.maybeNotifyUserToReload`, `gPrivacyPane.onBaselineCheckboxChange`, `gPrivacyPane.showDoHExceptions`, `gPrivacyPane.showPasswordExceptions`, `gPrivacyPane.showPasswords`, `gPrivacyPane.showTrackingProtectionExceptions`, `gPrivacyPane.updateMasterPasswordButton`, `this._pane`
- XPCOM: `Services.obs`

## initContentBlocking()
- 位置: L780-917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.privacyUiFppClick.checkbox.record()`, `Glean.privacyUiFppClick.menu.record()`, `Preferences.get()`, `Preferences.get("browser.contentblocking.category").on()`, `Preferences.get("browser.contentblocking.features.strict").on()`, `Preferences.get("network.cookie.cookieBehavior").on()`, `Preferences.get("privacy.firstparty.isolate").on()`, `Preferences.get("privacy.resistFingerprinting").on()`, `Preferences.get("privacy.resistFingerprinting.pbmode").on()`, `Preferences.get("urlclassifier.trackingTable").on()`, `Preferences.get(pref).on()`, `Services.prefs.getBoolPref()`, `button.addEventListener()`, `document.getElementById()`, `document.querySelector()`, `document.querySelectorAll()`, `gPrivacyPane.readBlockCookies.bind()`, `initTCPStandardSection()`, `setEventListener()`, `setUpContentBlockingWarnings()`, `this.fingerprintingProtectionWritePrefs()`, `this.highlightCBCategory()`, `this.populateCategoryContents()`, `this.readBlockCookies()`, `updateTrackingAndIsolateOption()`
- 条件付き依存: `if (Services.prefs.getBoolPref(STP_COOKIES_PREF))` → `document.getElementById()`
- 条件付き依存: `if (Services.prefs.getBoolPref(STP_COOKIES_PREF))` → `document.l10n.setAttributes()`
- 参照: `cryptoMinersOption.hidden`, `e.target.checked`, `e.target.value`, `fingerprintersOption.hidden`, `gPrivacyPane.highlightCBCategory`, `gPrivacyPane.maybeNotifyUserToReload`, `gPrivacyPane.populateCategoryContents`, `gPrivacyPane.reloadAllOtherTabs`, `this._updateTrackingProtectionUI`, `this.populateCategoryContents`, `this.toggleExpansion`, `this.trackingProtectionWritePrefs`, `this.updateCryptominingLists`, `this.updateFingerprintingLists`
- XPCOM: `Services.prefs`

## updateTrackingAndIsolateOption()
- 位置: L873-875
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `trackingAndIsolateOption.hidden`

## populateCategoryContents()
- 位置: L919-1137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.querySelector()`, `rulesArray.includes()`
- 条件付き依存: `if (type == "strict")` → `Services.prefs .getStringPref("browser.contentblocking.features.strict") .split()`
- 条件付き依存: `if (type == "strict")` → `Services.prefs .getStringPref()`
- 条件付き依存: `if (gIsFirstPartyIsolated)` → `rulesArray.indexOf()`
- 条件付き依存: `if (!(type == "strict"))` → `Services.prefs.getDefaultBranch()`
- 条件付き依存: `if (!(type == "strict"))` → `defaults.getIntPref()`
- 条件付き依存: `if (!(type == "strict"))` → `rulesArray.push()`
- 条件付き依存: `if (!(type == "strict"))` → `defaults.getBoolPref()`
- 条件付き依存: `if (!(type == "strict"))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(STP_COOKIES_PREF))` → `document.querySelector()`
- 条件付き依存: `if (!rulesArray.includes("cookieBehavior5"))` → `document.querySelector()`
- 条件付き依存: `if (!document.querySelector(selector + " .trackers-option").hidden)` → `document.querySelector()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `document.querySelector( selector + " .all-third-party-cookies-option" ).hidden`, `document.querySelector( selector + " .all-third-party-cookies-private-windows-option" ).hidden`, `document.querySelector( selector + " .cross-site-cookies-option" ).hidden`, `document.querySelector( selector + " .fingerprinters-option" ).hidden`, `document.querySelector( selector + " .social-media-option" ).hidden`, `document.querySelector( selector + " .third-party-tracking-cookies-option" ).hidden`, `document.querySelector( selector + " .unvisited-cookies-option" ).hidden`, `document.querySelector(selector + " .all-cookies-option").hidden`, `document.querySelector(selector + " .cross-site-cookies-option").hidden`, `document.querySelector(selector + " .cryptominers-option").hidden`, `document.querySelector(selector + " .pb-trackers-option").hidden`, `document.querySelector(selector + " .social-media-option").hidden`, `document.querySelector(selector + " .trackers-option").hidden`, `document.querySelector(selector + " .unvisited-cookies-option").hidden`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / `Services.prefs`

## highlightCBCategory()
- 位置: L1139-1161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `customEl.classList.add()`, `customEl.classList.remove()`, `document.getElementById()`, `standardEl.classList.add()`, `standardEl.classList.remove()`, `strictEl.classList.add()`, `strictEl.classList.remove()`
- 参照: `Preferences.get("browser.contentblocking.category").value`

## updateCryptominingLists()
- 位置: L1163-1173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `listManager.forceUpdates()`, `listPrefs .map()`, `listPrefs .map(l => Services.prefs.getStringPref(l)) .join()`
- XPCOM: `Services.prefs`

## updateFingerprintingLists()
- 位置: L1175-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `listManager.forceUpdates()`, `listPrefs .map()`, `listPrefs .map(l => Services.prefs.getStringPref(l)) .join()`
- XPCOM: `Services.prefs`

## trackingProtectionReadPrefs()
- 位置: L1192-1213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`, `this._updateTrackingProtectionUI()`
- 参照: `enabledPref.value`, `pbmPref.value`, `tpCheckbox.checked`, `tpMenu.value`

## fingerprintingProtectionReadPrefs()
- 位置: L1219-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`
- 参照: `enabledPref.locked`, `enabledPref.value`, `fppCheckbox.checked`, `fppCheckbox.disabled`, `fppMenu.disabled`, `fppMenu.value`, `pbmPref.value`

## networkCookieBehaviorReadPrefs()
- 位置: L1245-1274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cookies.getCookieBehavior()`, `Services.prefs.prefIsLocked()`, `document.getElementById()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `blockCookiesMenu.disabled`, `blockCookiesMenu.value`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / `Services.cookies` / `Services.prefs`

## trackingProtectionWritePrefs()
- 位置: L1279-1342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`
- 参照: `emailTPPBMPref.value`, `emailTPPref.value`, `enabledPref.value`, `pbmPref.value`, `stpCookiePref.value`, `stpPref.value`, `tpCheckbox.checked`, `tpMenu.value`

## fingerprintingProtectionWritePrefs()
- 位置: L1344-1379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`
- 参照: `enabledPref.value`, `fppCheckbox.checked`, `fppMenu.disabled`, `fppMenu.value`, `pbmPref.value`

## toggleExpansion()
- 位置: L1381-1389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `carat.classList.toggle()`, `carat.closest()`, `carat.closest(".privacy-detailedoption").classList.toggle()`, `carat.getAttribute()`, `carat.setAttribute()`
- 参照: `e.target`

## showClearPrivateDataSettings()
- 位置: L1404-1416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## clearPrivateDataNow()
- 位置: L1422-1424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.clearPrivateDataNow()`

## _isCustomCleaningPrefPresent()
- 位置: L1426-1428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers._isCustomCleaningPrefPresent()`

## showTrackingProtectionExceptions()
- 位置: L1433-1445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## readBlockCookies()
- 位置: L1467-1472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cookies.getCookieBehavior()`, `document.getElementById()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `bcControl.disabled`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / `Services.cookies`

## writeBlockCookies()
- 位置: L1478-1488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (block.checked)` → `this.writeBlockCookiesFrom()`
- 参照: `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `block.checked`, `blockCookiesMenu.selectedIndex`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## readBlockCookiesFrom()
- 位置: L1490-1505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cookies.getCookieBehavior()`
- 参照: `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / `Services.cookies`

## writeBlockCookiesFrom()
- 位置: L1507-1523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `block.value`, `document.getElementById("blockCookiesMenu").selectedItem`
- XPCOM: [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md)

## reloadAllOtherTabs()
- 位置: L1530-1532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.reloadAllOtherTabs()`

## maybeNotifyUserToReload()
- 位置: L1538-1540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.maybeNotifyUserToReload()`

## showHttpsOnlyModeExceptions()
- 位置: L1545-1547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showHttpsOnlyModeExceptions()`

## showDoHExceptions()
- 位置: L1549-1551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showDoHExceptions()`

## showLocationExceptions()
- 位置: L1559-1561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showLocationExceptions()`

## showLoopbackNetworkExceptions()
- 位置: L1569-1571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showLoopbackNetworkExceptions()`

## showLocalNetworkExceptions()
- 位置: L1579-1581
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showLocalNetworkExceptions()`

## showXRExceptions()
- 位置: L1589-1591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showXRExceptions()`

## showCameraExceptions()
- 位置: L1599-1601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showCameraExceptions()`

## showMicrophoneExceptions()
- 位置: L1609-1611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showMicrophoneExceptions()`

## showSpeakerExceptions()
- 位置: L1619-1621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showSpeakerExceptions()`

## showNotificationExceptions()
- 位置: L1629-1631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showNotificationExceptions()`

## showAutoplayMediaExceptions()
- 位置: L1635-1637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showAutoplayMediaExceptions()`

## showPopupExceptions()
- 位置: L1645-1647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showPopupExceptions()`

## updateButtons()
- 位置: L1655-1660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`
- 参照: `button.disabled`, `preference.locked`, `preference.value`

## showPasswordExceptions()
- 位置: L1677-1679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.showPasswordExceptions()`

## _initMasterPasswordUI()
- 位置: L1687-1689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers._initMasterPasswordUI()`

## updateMasterPasswordButton()
- 位置: async L1696-1706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._initMasterPasswordUI()`
- 条件付き依存: `if (!checkbox.checked)` → `PasswordSettingHelpers._removeMasterPassword()`
- 条件付き依存: `if (!(!checkbox.checked))` → `PasswordSettingHelpers.changeMasterPassword()`
- 参照: `button.disabled`, `checkbox.checked`

## _removeMasterPassword()
- 位置: async L1708-1710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers._removeMasterPassword()`

## changeMasterPassword()
- 位置: async L1712-1714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.changeMasterPassword()`

## _initPasswordGenerationUI()
- 位置: L1720-1727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.getElementById()`
- 参照: `document.getElementById("generatePasswordsBox").hidden`
- XPCOM: `Services.prefs`

## toggleRelayIntegration()
- 位置: L1729-1738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (checkbox.checked)` → `FirefoxRelay.markAsAvailable()`
- 条件付き依存: `if (checkbox.checked)` → `Glean.relayIntegration.enabledPrefChange.record()`
- 条件付き依存: `if (!(checkbox.checked))` → `FirefoxRelay.markAsDisabled()`
- 条件付き依存: `if (!(checkbox.checked))` → `Glean.relayIntegration.disabledPrefChange.record()`
- 参照: `checkbox.checked`

## _updateRelayIntegrationUI()
- 位置: L1740-1745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `FirefoxRelay.isAvailable`, `FirefoxRelay.isDisabled`, `document.getElementById("relayIntegration").checked`, `document.getElementById("relayIntegrationBox").hidden`

## _initRelayIntegrationUI()
- 位置: L1747-1763
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Preferences.get("signon.firefoxRelay.feature").on()`, `document .getElementById()`, `document .getElementById("relayIntegrationLearnMoreLink") .setAttribute()`, `gPrivacyPane._updateRelayIntegrationUI.bind()`, `gPrivacyPane.toggleRelayIntegration.bind()`, `setEventListener()`, `this._updateRelayIntegrationUI()`
- 参照: `FirefoxRelay.learnMoreUrl`

## _toggleOSAuth()
- 位置: async L1765-1804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.pwmgr.promptShownOsReauth.record()`, `Glean.pwmgr.requireOsReauthToggle.record()`, `LoginHelper.setOSAuthEnabled()`, `OSKeyStore.ensureLoggedIn()`, `document.getElementById()`, `lazy.AboutLoginsL10n.formatValue()`
- 参照: `( await OSKeyStore.ensureLoggedIn(messageText, captionText, win, false) ).authenticated`, `osReauthCheckbox.checked`, `osReauthCheckbox.documentGlobal.docShell.chromeEventHandler .documentGlobal`

## _initOSAuthentication()
- 位置: L1806-1823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginHelper.getOSAuthEnabled()`, `OSKeyStore.canReauth()`, `Services.prefs.getBoolPref()`, `document.getElementById()`, `gPrivacyPane._toggleOSAuth.bind()`, `osReauthCheckbox.toggleAttribute()`, `setEventListener()`
- 参照: `osReauthCheckbox.hidden`
- XPCOM: `Services.prefs`

## showPasswords()
- 位置: L1829-1831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.showPasswords()`

## readSavePasswords()
- 位置: L1838-1847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Services.prefs.prefIsLocked()`, `document.getElementById()`
- 参照: `Preferences.get("signon.rememberSignons").value`, `document.getElementById("generatePasswords").disabled`, `document.getElementById("passwordAutofillCheckbox").disabled`, `document.getElementById("passwordExceptions").disabled`, `document.getElementById("relayIntegration").disabled`
- XPCOM: `Services.prefs`

## initListenersForExtensionControllingPasswordManager()
- 位置: L1854-1873
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `initListenersForPrefChange()`, `makeDisableControllingExtension()`, `this._disableExtensionButton.addEventListener()`
- 参照: `this._disableExtensionButton`, `this._passwordManagerCheckbox`

## showAddonExceptions()
- 位置: L1878-1880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showAddonExceptions()`

## showCertificates()
- 位置: L1885-1887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showCertificates()`

## showSecurityDevices()
- 位置: L1892-1894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.showSecurityDevices()`

## initPrivacySegmentation()
- 位置: L1896-1923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.prefs.removeObserver()`, `document.getElementById()`, `updatePrivacySegmentationSectionVisibilityState()`, `window.addEventListener()`
- 参照: `AppConstants.MOZ_DATA_REPORTING`
- XPCOM: `Services.prefs`

## updatePrivacySegmentationSectionVisibilityState()
- 位置: L1906-1908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `section.hidden`
- XPCOM: `Services.prefs`

## observe()
- 位置: L1925-1933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPrivacyPane.updateDoHStatus()`

## onBaselineCheckboxChange()
- 位置: async L1944-1946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.onBaselineCheckboxChange()`

## onBaselineAllowListSettingChange()
- 位置: async L1948-1953
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers.onBaselineAllowListSettingChange()`

## _confirmBaselineAllowListDisable()
- 位置: async L1955-1957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivacySettingHelpers._confirmBaselineAllowListDisable()`
