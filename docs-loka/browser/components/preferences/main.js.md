# browser/components/preferences/main.js

source: browser/components/preferences/main.js
source-hash: 6dcfd4bd0ee2b0665afed9dad88df67bed1a2818
lines: 2639

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Services.prefs.getBoolPref()`, `SettingGroupManager.registerGroups()`, `createDefaultBrowserConfig()`, `createStartupConfig()`, `importIntoWindow()`, `window.MozXULElement.parseXULToFragment()`

## importIntoWindow()
- 位置: L33-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`
- 参照: `window.closed`

## canShowAiFeature()
- 位置: L101-106
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `defaultSetting.value`, `featureSetting.value`

## get()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._getLaunchOnLoginApprovedCachedValue`

## setup()
- 位置: L161-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LaunchOnLogin.isAllowed()`, `LaunchOnLogin.isAllowed().then()`, `LaunchOnLogin.isSupported()`
- 参照: `this._getLaunchOnLoginApprovedCachedValue`

## startWithLastProfile()
- 位置: L183-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/toolkit/profile-service;1"].getService()`
- 参照: `Cc["@mozilla.org/toolkit/profile-service;1"].getService( Ci.nsIToolkitProfileService ).startWithLastProfile`, `Ci.nsIToolkitProfileService`
- XPCOM: [`nsIToolkitProfileService`](../../../toolkit/profile/nsIToolkitProfileService.idl.md) / `@mozilla.org/toolkit/profile-service;1`

## get()
- 位置: L188-190
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._getLaunchOnLoginEnabledValue`

## setup()
- 位置: L191-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LaunchOnLogin.isSupported()`
- 条件付き依存: `if (!this.startWithLastProfile)` → `maybeEmitChange()`
- 条件付き依存: `if (!(!this.startWithLastProfile))` → `LaunchOnLogin.isEnabled().then()`
- 条件付き依存: `if (!(!this.startWithLastProfile))` → `LaunchOnLogin.isEnabled()`
- 条件付き依存: `if (!(!this.startWithLastProfile))` → `maybeEmitChange()`
- 参照: `this.startWithLastProfile`

## maybeEmitChange()
- 位置: L198-205
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( getLaunchOnLoginEnabledValue !== this._getLaunchOnLoginEnabledValue )` → `emitChange()`
- 参照: `this._getLaunchOnLoginEnabledValue`

## visible()
- 位置: L217-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LaunchOnLogin.isSupported()`
- 条件付き依存: `if (isVisible)` → `NimbusFeatures.windowsLaunchOnLogin.recordExposureEvent()`
- 参照: `windowsLaunchOnLoginEnabled.value`

## disabled()
- 位置: L228-230
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `launchOnLoginApproved.value`, `this.startWithLastProfile`

## onUserChange()
- 位置: L231-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.launchOnLogin.userToggle.record()`
- 条件付き依存: `if (checked)` → `LaunchOnLogin.enable()`
- 条件付き依存: `if (!(checked))` → `LaunchOnLogin.disable()`

## visible()
- 位置: L253-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/toolkit/profile-service;1" ].getService()`, `LaunchOnLogin.isSupported()`
- 参照: `Cc[ "@mozilla.org/toolkit/profile-service;1" ].getService(Ci.nsIToolkitProfileService).startWithLastProfile`, `Ci.nsIToolkitProfileService`, `windowsLaunchOnLoginEnabled.value`
- XPCOM: [`nsIToolkitProfileService`](../../../toolkit/profile/nsIToolkitProfileService.idl.md) / `@mozilla.org/toolkit/profile-service;1`

## visible()
- 位置: L268-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/toolkit/profile-service;1" ].getService()`, `LaunchOnLogin.isSupported()`
- 参照: `Cc[ "@mozilla.org/toolkit/profile-service;1" ].getService(Ci.nsIToolkitProfileService).startWithLastProfile`, `Ci.nsIToolkitProfileService`, `launchOnLoginApproved.value`, `windowsLaunchOnLoginEnabled.value`
- XPCOM: [`nsIToolkitProfileService`](../../../toolkit/profile/nsIToolkitProfileService.idl.md) / `@mozilla.org/toolkit/profile-service;1`

## get()
- 位置: L299-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 参照: `gMainPane.STARTUP_PREF_RESTORE_SESSION`, `pbAutoStartPref.value`

## set()
- 位置: L309-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 条件付き依存: `if (startupPref.value === gMainPane.STARTUP_PREF_BLANK)` → `HomePage.safeSet()`
- 参照: `gMainPane.STARTUP_PREF_BLANK`, `gMainPane.STARTUP_PREF_HOMEPAGE`, `gMainPane.STARTUP_PREF_RESTORE_SESSION`, `startupPref.value`

## disabled()
- 位置: L325-327
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.privateBrowsingAutoStart.value`

## visible()
- 位置: L334-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## disabled()
- 位置: L339-339
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.browserRestoreSession.value`

## onUserClick()
- 位置: L344-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `gotoPref()`

## visible()
- 位置: L353-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `canShowAiFeature()`
- XPCOM: `Services.prefs`

## onUserClick()
- 位置: L360-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gMainPane.showConnections()`

## setup()
- 位置: L371-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DefaultBrowserHelper.pollForDefaultChanges()`
- 参照: `DefaultBrowserHelper.canCheck`

## visible()
- 位置: L381-381
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DefaultBrowserHelper.canCheck`

## disabled()
- 位置: L382-385
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `DefaultBrowserHelper.canCheck`, `DefaultBrowserHelper.isBrowserDefault`, `setting.locked`

## visible()
- 位置: L391-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `Services.prefs.prefIsLocked()`
- 参照: `DefaultBrowserHelper.canCheck`, `DefaultBrowserHelper.isBrowserDefault`
- XPCOM: `Services.policies` / `Services.prefs`

## visible()
- 位置: L401-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `Services.prefs.prefIsLocked()`
- 参照: `DefaultBrowserHelper.canCheck`, `DefaultBrowserHelper.isBrowserDefault`
- XPCOM: `Services.policies` / `Services.prefs`

## onUserClick()
- 位置: L406-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DefaultBrowserHelper.setDefaultBrowser()`, `DefaultBrowserHelper.setDefaultBrowser().finally()`
- 参照: `DefaultBrowserHelper.canCheck`, `alwaysCheckDefault.value`, `e.target`, `setDefaultButton.disabled`

## createDefaultBrowserConfig()
- 位置: L465-513
- 役割: (未記入)
- 触るとき: (未記入)

## createStartupConfig()
- 位置: L515-573
- 役割: (未記入)
- 触るとき: (未記入)

## initSettingGroup()
- 位置: L585-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SettingGroupManager.get()`, `document.querySelectorAll()`
- 条件付き依存: `if (group && config)` → `srdSectionEnabled()`
- 条件付き依存: `if (group && config)` → `group.hasAttribute()`
- 条件付き依存: `if ( (sectionEnabled && group.hasAttribute("data-srd-migrated")) || (config.inProgress && !sectionEnabled) )` → `group.remove()`
- 条件付き依存: `if (group && config)` → `document.querySelectorAll()`
- 条件付き依存: `if (sectionEnabled)` → `section.removeAttribute()`
- 条件付き依存: `if (sectionEnabled)` → `section.setAttribute()`
- 条件付き依存: `if (group && config)` → `Preferences.getSetting.bind()`
- 参照: `config.inProgress`, `group.config`, `group.getSetting`, `group.srdEnabled`, `section.hidden`, `srdSectionPrefs.all`

## getBundleForLocales()
- 位置: L629-643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`
- 参照: `Services.locale.lastFallbackLocale`, `Services.locale.requestedLocales`
- XPCOM: `Services.locale`

## init()
- 位置: L656-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `gMainPane.initTranslations()`, `gMainPane.showBrowserLanguagesSubDialog()`, `initSettingGroup()`, `setEventListener()`, `srdSectionEnabled()`, `this.displayUseSystemLocale()`, `this.setInitialized()`, `window.addEventListener()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.enabled"))` → `gMainPane.initPrimaryBrowserLanguageUI()`
- 条件付き依存: `if (!srdSectionEnabled("applications"))` → `AppFileHandler._init()`
- 参照: `gMainPane.showLanguages`
- XPCOM: `Services.obs` / `Services.prefs`

## setEventListener()
- 位置: L662-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback.bind()`, `document .getElementById()`, `document .getElementById(aId) .addEventListener()`

## preInit()
- 位置: L719-738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`, `resolve()`, `srdSectionEnabled()`, `window.addEventListener()`
- 条件付き依存: `if (!srdSectionEnabled("applications"))` → `AppFileHandler.preInit()`
- 条件付き依存: `if (!srdSectionEnabled("applications"))` → `Services.obs.notifyObservers()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## handleSubcategory()
- 位置: L740-754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- 条件付き依存: `if (subcategory == "migrate")` → `this.showMigrationWizardDialog()`
- 条件付き依存: `if (subcategory == "migrate-autoclose")` → `this.showMigrationWizardDialog()`
- 参照: `Services.policies`
- XPCOM: `Services.policies`

## onGetStarted()
- 位置: async L765-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.canConnectAccount()`, `FxAccounts.config.promiseConnectAccountURI()`, `Services.wm.getMostRecentWindow()`, `fxAccounts.getSignedInUser()`, `win.gBrowser.addWebTab()`
- 条件付き依存: `if (user)` → `win.openTrustedLinkIn()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `win.gBrowser.selectedTab`
- XPCOM: `Services.wm`

## updateButtons()
- 位置: L811-816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`
- 参照: `button.disabled`, `preference.value`

## initTranslations()
- 位置: async L821-1246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `TranslationsState.create()`, `TranslationsState.create().then()`, `TranslationsView.showError()`, `document.getElementById()`, `legacyTranslationsVisible.off()`, `legacyTranslationsVisible.on()`, `setTranslationsGroupVisbility()`, `window.addEventListener()`
- 参照: `this._translationsView`

## setTranslationsGroupVisbility()
- 位置: L832-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `translationsGroup.classList.toggle()`
- 参照: `legacyTranslationsVisible.visible`, `translationsGroup.hidden`

## TranslationsState.constructor()
- 位置: L859-863
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.downloadPhases`, `this.languageList`, `this.supportedLanguages`

## TranslationsState.create()
- 位置: async L868-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.getLanguageList()`, `TranslationsParent.getSupportedLanguages()`, `TranslationsState.createDownloadPhases()`
- 参照: `supportedLanguages.languagePairs.length`

## TranslationsState.createDownloadPhases()
- 位置: async L895-906
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.hasAllFilesForLanguage()`, `downloadPhases.set()`

## TranslationsView.constructor()
- 位置: L918-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.setup()`
- 参照: `this.elements`, `this.state`

## TranslationsView.setup()
- 位置: L936-953
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this.buildLanguageList()`, `this.elements.deleteAll.addEventListener()`, `this.elements.installAll.addEventListener()`, `this.elements.settingsButton.addEventListener()`
- 参照: `gMainPane.showTranslationsSettings`, `this.handleDeleteAll`, `this.handleInstallAll`
- XPCOM: `Services.obs`

## TranslationsView.destroy()
- 位置: L955-957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## TranslationsView.handleInstallAll()
- 位置: async L959-974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.downloadAllFiles()`, `TranslationsView.showError()`, `this.disableButtons()`, `this.hideError()`, `this.markAllDownloadPhases()`, `this.reloadDownloadPhases()`, `this.updateAllButtons()`

## TranslationsView.handleDeleteAll()
- 位置: async L976-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsUtils.deleteAllLanguageFiles()`, `TranslationsView.showError()`, `console.error()`, `this.disableButtons()`, `this.hideError()`, `this.markAllDownloadPhases()`, `this.reloadDownloadPhases()`

## TranslationsView.getDownloadButtonHandler()
- 位置: L995-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.downloadLanguageFiles()`, `TranslationsView.showError()`, `this.hideError()`, `this.updateDownloadPhase()`

## TranslationsView.getDeleteButtonHandler()
- 位置: L1016-1032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.deleteLanguageFiles()`, `TranslationsView.showError()`, `this.hideError()`, `this.reloadDownloadPhases()`, `this.updateDownloadPhase()`

## TranslationsView.buildLanguageList()
- 位置: L1034-1079
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deleteButton.addEventListener()`, `document.createDocumentFragment()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `downloadButton.addEventListener()`, `hboxRow.appendChild()`, `hboxRow.classList.add()`, `hboxRow.setAttribute()`, `listFragment.appendChild()`, `this.deleteButtons.set()`, `this.downloadButtons.set()`, `this.elements.installList.appendChild()`, `this.getDeleteButtonHandler()`, `this.getDownloadButtonHandler()`, `this.updateAllButtons()`
- 参照: `deleteButton.hidden`, `downloadButton.hidden`, `languageLabel.textContent`, `this.state.languageList`

## TranslationsView.updateDownloadPhase()
- 位置: L1087-1091
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.state.downloadPhases.set()`, `this.updateButton()`, `this.updateHeaderButtons()`

## TranslationsView.reloadDownloadPhases()
- 位置: async L1096-1100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsState.createDownloadPhases()`, `this.updateAllButtons()`
- 参照: `this.state.downloadPhases`, `this.state.languageList`

## TranslationsView.markAllDownloadPhases()
- 位置: L1107-1113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `downloadPhases.keys()`, `downloadPhases.set()`, `this.updateAllButtons()`
- 参照: `this.state`

## TranslationsView.updateHeaderButtons()
- 位置: L1119-1133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.state.downloadPhases.values()`
- 参照: `this.elements.deleteAll.hidden`, `this.elements.installAll.hidden`

## TranslationsView.updateAllButtons()
- 位置: L1138-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateButton()`, `this.updateHeaderButtons()`
- 参照: `this.state.downloadPhases`

## TranslationsView.updateButton()
- 位置: L1149-1169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `downloadButton.removeAttribute()`, `downloadButton.setAttribute()`, `this.deleteButtons.get()`, `this.downloadButtons.get()`
- 参照: `deleteButton.hidden`, `downloadButton.hidden`

## TranslationsView.disableButtons()
- 位置: L1174-1183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.deleteButtons.values()`, `this.downloadButtons.values()`
- 参照: `button.disabled`, `this.elements.deleteAll.disabled`, `this.elements.installAll.disabled`

## TranslationsView.showError()
- 位置: L1192-1199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `document.getElementById()`, `document.l10n.setAttributes()`
- 参照: `errorMessage.hidden`

## TranslationsView.hideError()
- 位置: L1201-1203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.elements.error.hidden`

## TranslationsView.observe()
- 位置: L1205-1209
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "intl:app-locales-changed")` → `this.refreshLanguageListDisplay()`

## TranslationsView.refreshLanguageListDisplay()
- 位置: L1211-1233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.createLanguageDisplayNames()`, `console.error()`, `row.getAttribute()`, `row.querySelector()`
- 条件付き依存: `if (label)` → `languageDisplayNames.of()`
- 参照: `label.textContent`, `this.elements.installList.children`

## initPrimaryBrowserLanguageUI()
- 位置: L1248-1256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `gMainPane.onPrimaryBrowserLanguageMenuChange()`, `gMainPane.updatePrimaryBrowserLanguageUI()`
- 参照: `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## updatePrimaryBrowserLanguageUI()
- 位置: async L1265-1302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LangPackMatcher.getAvailableLocales()`, `Services.intl.getLocaleDisplayNames()`, `Services.prefs.getBoolPref()`, `available.map()`, `document.createDocumentFragment()`, `document.createXULElement()`, `document.getElementById()`, `fragment.appendChild()`, `locales.sort()`, `menuitem.setAttribute()`, `menulist.querySelector()`, `menupopup.appendChild()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.downloadEnabled"))` → `document.createXULElement()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.downloadEnabled"))` → `menuitem.setAttribute()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.downloadEnabled"))` → `document.l10n.formatValue()`
- 条件付き依存: `if (Services.prefs.getBoolPref("intl.multilingual.downloadEnabled"))` → `fragment.appendChild()`
- 参照: `a.name`, `b.name`, `document.getElementById("browserLanguagesBox").hidden`, `menuitem.id`, `menulist.value`, `menupopup.textContent`
- XPCOM: `Services.intl` / `Services.prefs`

## showConfirmLanguageChangeMessageBar()
- 位置: async L1305-1355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Services.intl.getScriptDirection()`, `[newBundle, document.l10n].map()`, `bundle.formatValue()`, `button.addEventListener()`, `button.setAttribute()`, `document.createElement()`, `document.createXULElement()`, `document.getElementById()`, `getBundleForLocales()`, `locales.join()`, `messageBar.appendChild()`, `messageBar.setAttribute()`, `messageBarContainer.appendChild()`
- 条件付き依存: `if (messages[0] == messages[1] && buttonLabels[0] == buttonLabels[1])` → `messages.pop()`
- 条件付き依存: `if (messages[0] == messages[1] && buttonLabels[0] == buttonLabels[1])` → `buttonLabels.pop()`
- 条件付き依存: `if (i == 0 && Services.intl.getScriptDirection(locales[0]) === "rtl")` → `messageBar.setAttribute()`
- 参照: `document.l10n`, `gMainPane.confirmBrowserLanguageChange`, `gMainPane.selectedLocalesForRestart`, `messageBarContainer.hidden`, `messageBarContainer.textContent`, `messages.length`
- XPCOM: `Services.intl`

## hideConfirmLanguageChangeMessageBar()
- 位置: L1357-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `gMainPane.requestingLocales`, `messageBarContainer.hidden`, `messageBarContainer.textContent`

## confirmBrowserLanguageChange()
- 位置: L1365-1372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(event.target.getAttribute("locales") || "").trim()`, `Multilingual.applyAndRestart()`, `event.target.getAttribute()`, `localesString.split()`
- 参照: `localesString.length`

## onPrimaryBrowserLanguageMenuChange()
- 位置: L1375-1415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Multilingual.getTransitionType()`, `Multilingual.recordTelemetry()`, `gMainPane.hideConfirmLanguageChangeMessageBar()`, `gMainPane.showConfirmLanguageChangeMessageBar()`, `gMainPane.updatePrimaryBrowserLanguageUI()`, `new Set([locale, ...Services.locale.requestedLocales]).values()`
- 条件付き依存: `if (locale == "search")` → `gMainPane.showBrowserLanguagesSubDialog()`
- 条件付き依存: `if (locale == Services.locale.appLocaleAsBCP47)` → `this.hideConfirmLanguageChangeMessageBar()`
- 参照: `Multilingual.TransitionType.LiveReload`, `Multilingual.TransitionType.LocalesMatch`, `Multilingual.TransitionType.RestartRequired`, `Services.locale.appLocaleAsBCP47`, `Services.locale.requestedLocales`, `event.target.value`
- XPCOM: `Services.locale`

## manageProfiles()
- 位置: L1420-1428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.toOpenWindowByType()`
- 参照: `window.browsingContext.topChromeWindow`

## showLanguages()
- 位置: L1433-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## showBrowserLanguagesSubDialog()
- 位置: L1446-1465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Multilingual.recordTelemetry()`, `Services.telemetry.msSinceProcessStart()`, `gSubDialog.open()`, `parseInt()`, `parseInt( Services.telemetry.msSinceProcessStart(), 10 ).toString()`
- 参照: `gMainPane.selectedLocalesForRestart`, `this.browserLanguagesClosed`
- XPCOM: `Services.telemetry`

## browserLanguagesClosed()
- 位置: L1468-1517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Multilingual.getTransitionType()`, `Services.locale.requestedLocales.filter()`, `gMainPane.hideConfirmLanguageChangeMessageBar()`, `gMainPane.showConfirmLanguageChangeMessageBar()`, `gMainPane.updatePrimaryBrowserLanguageUI()`, `prevLocales.includes()`, `prevLocales.some()`, `selected.filter()`, `selected.indexOf()`, `this.gBrowserLanguagesDialog.recordTelemetry()`
- 条件付き依存: `if (prevLocales.some((lc, i) => newLocales[i] != lc))` → `this.gBrowserLanguagesDialog.recordTelemetry()`
- 参照: `Multilingual.TransitionType.LiveReload`, `Multilingual.TransitionType.LocalesMatch`, `Multilingual.TransitionType.RestartRequired`, `Services.locale.appLocaleAsBCP47`, `Services.locale.requestedLocales`, `this.gBrowserLanguagesDialog`
- XPCOM: `Services.locale`

## displayUseSystemLocale()
- 位置: L1519-1542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.intl.getLocaleDisplayNames()`, `appLocale.split()`, `systemLocale.split()`
- 条件付き依存: `if (appLocale.split("-u-")[0] != systemLocale.split("-u-")[0])` → `document.getElementById()`
- 条件付き依存: `if (appLocale.split("-u-")[0] != systemLocale.split("-u-")[0])` → `document.l10n.setAttributes()`
- 参照: `Services.locale.appLocaleAsBCP47`, `Services.locale.regionalPrefsLocales`, `checkbox.hidden`, `localeDisplayname.length`, `regionalPrefsLocales.length`
- XPCOM: `Services.intl` / `Services.locale`

## showTranslationsSettings()
- 位置: L1544-1548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## showConnections()
- 位置: L1554-1558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## showMigrationWizardDialog()
- 位置: async L1563-1606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `customElements.whenDefined()`, `document.getElementById()`, `migrationWizardDialog.addEventListener()`, `migrationWizardDialog.firstElementChild.requestState()`, `migrationWizardDialog.showModal()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `document.createElement()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `wizard.toggleAttribute()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `migrationWizardDialog.appendChild()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `migrationWizardDialog.addEventListener()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `e.currentTarget.close()`
- 条件付き依存: `if (closeTabWhenDone)` → `window.close()`
- 参照: `migrationWizardDialog.firstElementChild`, `migrationWizardDialog.open`
- XPCOM: `Services.obs`

## destroy()
- 位置: L1608-1616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.removeEventListener()`
- 条件付き依存: `if (this._translationsView)` → `this._translationsView.destroy()`
- 参照: `this._translationsView`

## observe()
- 位置: async L1624-1638
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic == "nsPref:changed")` → `srdSectionEnabled()`
- 条件付き依存: `if ( !srdSectionEnabled("applications") && !AppFileHandler._storingAction )` → `AppFileHandler._rebuildView()`
- 参照: `AppFileHandler._storingAction`

## handleEvent()
- 位置: L1642-1649
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.type == "unload")` → `this.destroy()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `onUnload()`
- 参照: `AppConstants.MOZ_UPDATER`, `aEvent.type`

## isValidHandlerApp()
- 位置: L1658-1660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppFileHandler.isValidHandlerApp()`

## _getIconURLForHandlerApp()
- 位置: L1667-1669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getIconURLForHandlerApp()`

## HandlerListItem.forNode()
- 位置: L1719-1721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNodeToObjectMap.get()`

## HandlerListItem.constructor()
- 位置: L1726-1728
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.handlerInfoWrapper`

## HandlerListItem.setOrRemoveAttributes()
- 位置: L1734-1743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.node.querySelector()`
- 条件付き依存: `if (value)` → `node.setAttribute()`
- 条件付き依存: `if (!(value))` → `node.removeAttribute()`
- 参照: `this.node`

## HandlerListItem.createNode()
- 位置: L1745-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.importNode()`, `gNodeToObjectMap.set()`, `list.appendChild()`
- 参照: `list.lastChild`, `this.node`

## HandlerListItem.setupNode()
- 位置: L1751-1768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AppFileHandler.onSelectAction()`, `localizeElement()`, `this.node .querySelector()`, `this.node .querySelector(".actionsMenu") .addEventListener()`, `this.node.querySelector()`, `this.setOrRemoveAttributes()`
- 参照: `event.originalTarget`, `this.handlerInfoWrapper.iconSrcSet`, `this.handlerInfoWrapper.type`, `this.handlerInfoWrapper.typeDescription`, `this.showActionsMenu`

## HandlerListItem.refreshAction()
- 位置: L1770-1800
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.getAttributes()`, `localizeElement()`, `this.node.querySelector()`, `this.setOrRemoveAttributes()`
- 条件付き依存: `if (!selectedItem)` → `console.error()`
- 参照: `this.handlerInfoWrapper`, `this.handlerInfoWrapper.actionIconSrcset`, `this.handlerInfoWrapper.type`

## HandlerListItem.showActionsMenu()
- 位置: L1802-1807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setOrRemoveAttributes()`

## localizeElement()
- 位置: L1820-1827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `l10n.hasOwnProperty()`
- 条件付き依存: `if (l10n.hasOwnProperty("raw"))` → `node.removeAttribute()`
- 条件付き依存: `if (!(l10n.hasOwnProperty("raw")))` → `document.l10n.setAttributes()`
- 参照: `l10n.args`, `l10n.id`, `l10n.raw`, `node.textContent`

## Handler._list()
- 位置: L1875-1877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## Handler._filter()
- 位置: L1879-1881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## Handler.preInit()
- 位置: async L1885-1893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._initListEventHandlers()`, `this._loadApplicationHandlers()`, `this._loadInternalHandlers()`, `this._rebuildView()`, `this._rebuildVisibleTypes()`, `this._sortListView()`

## Handler._init()
- 位置: L1895-1915
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("actionColumn").hasAttribute()`, `setEventListener()`, `this.filter()`, `this.sort()`
- 条件付き依存: `if ( document.getElementById("actionColumn").hasAttribute("sortDirection") )` → `document.getElementById()`
- 条件付き依存: `if ( document.getElementById("actionColumn").hasAttribute("sortDirection") )` → `document.getElementById("typeColumn").removeAttribute()`
- 条件付き依存: `if (!( document.getElementById("actionColumn").hasAttribute("sortDirection") ))` → `document.getElementById()`
- 参照: `this._sortColumn`

## Handler._rebuildVisibleTypes()
- 位置: async L1917-1951
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.tm.dispatchToMainThread()`, `this._visibleTypes.push()`, `visibleDescriptions.get()`
- 条件付き依存: `if (!otherHandlerInfo)` → `visibleDescriptions.set()`
- 参照: `handlerInfo.description`, `handlerInfo.disambiguateDescription`, `otherHandlerInfo.disambiguateDescription`, `this._handledTypes`, `this._visibleTypes`
- XPCOM: `Services.tm`

## Handler._loadApplicationHandlers()
- 位置: L1953-1955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HandlerServiceHelpers.loadApplicationHandlers()`
- 参照: `this._handledTypes`

## Handler._initListEventHandlers()
- 位置: L1957-1979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HandlerListItem.forNode()`, `this._list.addEventListener()`
- 条件付き依存: `if (handlerListItem)` → `this.rebuildActionsMenu()`
- 参照: `event.target`, `handlerListItem.showActionsMenu`, `this._list`, `this._list.selectedItem`, `this.selectedHandlerListItem`, `this.selectedHandlerListItem.showActionsMenu`

## Handler._loadInternalHandlers()
- 位置: L1981-1983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HandlerServiceHelpers.loadInternalHandlers()`
- 参照: `this._handledTypes`

## Handler._rebuildView()
- 位置: async L1985-2034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createDocumentFragment()`, `item.createNode()`, `item.refreshAction()`, `item.setupNode()`, `this.rebuildActionsMenu()`, `visibleTypes.map()`
- 条件付き依存: `if (this._filter.value)` → `document.l10n.translateFragment()`
- 条件付き依存: `if (this._filter.value)` → `this._filterView()`
- 条件付き依存: `if (this._filter.value)` → `document.l10n.pauseObserving()`
- 条件付き依存: `if (this._filter.value)` → `this._list.appendChild()`
- 条件付き依存: `if (this._filter.value)` → `document.l10n.resumeObserving()`
- 条件付き依存: `if (!(this._filter.value))` → `this._list.appendChild()`
- 参照: `item.handlerInfoWrapper`, `item.handlerInfoWrapper.type`, `item.node`, `lastSelectedItem.node`, `this._filter.value`, `this._list.selectedItem`, `this._list.textContent`, `this._visibleTypes`, `this.selectedHandlerListItem`, `this.selectedHandlerListItem.handlerInfoWrapper.type`

## Handler.sort()
- 位置: L2041-2063
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `column.getAttribute()`, `this._sortListView()`
- 条件付き依存: `if (this._sortColumn && this._sortColumn != column)` → `this._sortColumn.removeAttribute()`
- 条件付き依存: `if (column.getAttribute("sortDirection") == "ascending")` → `column.setAttribute()`
- 条件付き依存: `if (!(column.getAttribute("sortDirection") == "ascending"))` → `column.setAttribute()`
- 参照: `event.button`, `event.target`, `this._sortColumn`

## Handler._sortListView()
- 位置: async L2065-2092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `comp.compare()`, `document.l10n.translateFragment()`, `items.forEach()`, `items.sort()`, `textForNode()`, `this._list.appendChild()`, `this._sortColumn.getAttribute()`
- 参照: `Services.intl.Collator`, `this._list`, `this._list.children`, `this._sortColumn`
- XPCOM: `Services.intl`

## textForNode()
- 位置: L2078-2078
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.querySelector()`
- 参照: `n.querySelector(".typeDescription").textContent`

## textForNode()
- 位置: L2080-2081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.querySelector()`, `n.querySelector(".actionsMenu").getAttribute()`

## Handler._filterView()
- 位置: L2094-2106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionDescription.toLowerCase()`, `actionDescription.toLowerCase().includes()`, `elem .querySelector()`, `elem .querySelector(".actionDescription") .getAttribute()`, `elem.querySelector()`, `this._filter.value.toLowerCase()`, `typeDescription.toLowerCase()`, `typeDescription.toLowerCase().includes()`
- 参照: `elem.hidden`, `elem.querySelector(".typeDescription").textContent`, `frag.children`, `this._list`

## Handler._buildHeader()
- 位置: L2113-2129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `headerElement.appendChild()`, `this.actionColumn.setAttribute()`, `this.typeColumn.setAttribute()`
- 参照: `headerElement.slot`, `this.actionColumn`, `this.actionColumn.slot`, `this.typeColumn`

## Handler._sortItems()
- 位置: L2137-2146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `comp.compare()`, `textForNode()`, `unorderedItems.sort()`
- 参照: `Services.intl.Collator`
- XPCOM: `Services.intl`

## textForNode()
- 位置: L2141-2141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.getAttribute()`

## Handler.filter()
- 位置: L2148-2150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._rebuildView()`

## Handler.focusFilterBox()
- 位置: L2152-2155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._filter.focus()`, `this._filter.select()`

## Handler.onSelectAction()
- 位置: L2167-2175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._storeAction()`
- 参照: `this._storingAction`

## Handler._storeAction()
- 位置: L2177-2206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aActionItem.getAttribute()`, `handlerInfo.store()`, `parseInt()`, `this.selectedHandlerListItem.refreshAction()`
- 参照: `Ci.nsIHandlerInfo.alwaysAsk`, `Ci.nsIHandlerInfo.useHelperApp`, `aActionItem.handlerApp`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`, `this.selectedHandlerListItem.handlerInfoWrapper`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md)

## Handler.manageApp()
- 位置: L2208-2229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.stopPropagation()`, `gSubDialog.open()`
- 参照: `this.selectedHandlerListItem.handlerInfoWrapper`

## onComplete()
- 位置: L2215-2222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.rebuildActionsMenu()`, `this.selectedHandlerListItem.refreshAction()`

## Handler.chooseApp()
- 位置: async L2231-2330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.stopPropagation()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `document.l10n.formatValue()`
- 条件付き依存: `if ("id" in handlerInfo.description)` → `document.l10n.formatValue()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `gSubDialog.open()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `document.l10n.formatValue()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `Cc["@mozilla.org/filepicker;1"].createInstance()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `fp.init()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `fp.appendFilters()`
- 条件付き依存: `if (!(AppConstants.platform == "win"))` → `fp.open()`
- 参照: `AppConstants.platform`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.filterApps`, `Ci.nsIFilePicker.modeOpen`, `handlerInfo.description`, `handlerInfo.description.args`, `handlerInfo.description.id`, `handlerInfo.typeDescription.raw`, `handlerInfo.wrappedHandlerInfo`, `params.description`, `params.filename`, `params.handlerApp`, `params.mimeInfo`, `params.title`, `this.selectedHandlerListItem.handlerInfoWrapper`, `window.browsingContext`
- XPCOM: `nsIFilePicker` / `@mozilla.org/filepicker;1`

## chooseAppCallback()
- 位置: L2237-2260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.rebuildActionsMenu()`
- 条件付き依存: `if (aHandlerApp)` → `typeItem.querySelector()`
- 条件付き依存: `if (aHandlerApp)` → `menuItem.handlerApp.equals()`
- 条件付き依存: `if ( menuItem.handlerApp && menuItem.handlerApp.equals(aHandlerApp) )` → `this.onSelectAction()`
- 参照: `actionsMenu.menupopup.childNodes`, `actionsMenu.selectedIndex`, `menuItem.handlerApp`, `menuItems.length`, `this._list.selectedItem`

## onAppSelected()
- 位置: L2281-2290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chooseAppCallback()`, `this.isValidHandlerApp()`
- 条件付き依存: `if (this.isValidHandlerApp(params.handlerApp))` → `handlerInfo.addPossibleApplicationHandler()`
- 参照: `params.handlerApp`

## fpCallback()
- 位置: L2304-2322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._isValidHandlerExecutable()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `Cc[ "@mozilla.org/uriloader/local-handler-app;1" ].createInstance()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `getFileDisplayName()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `handler.addPossibleApplicationHandler()`
- 条件付き依存: `if ( aResult == Ci.nsIFilePicker.returnOK && fp.file && this._isValidHandlerExecutable(fp.file) )` → `chooseAppCallback()`
- 参照: `Ci.nsIFilePicker.returnOK`, `Ci.nsILocalHandlerApp`, `fp.file`, `handlerApp.executable`, `handlerApp.name`, `this.selectedHandlerListItem.handlerInfoWrapper`
- XPCOM: `nsIFilePicker` / [`nsILocalHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/local-handler-app;1`

## Handler.rebuildActionsMenu()
- 位置: L2336-2587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `askMenuItem.setAttribute()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `getIconURLForHandlerApp()`, `handlerInfo.possibleApplicationHandlers.enumerate()`, `menuItem.setAttribute()`, `menuPopup.appendChild()`, `menuPopup.hasChildNodes()`, `menuPopup.removeChild()`, `possibleAppMenuItems.push()`, `this.isValidHandlerApp()`, `typeItem.querySelector()`
- 条件付き依存: `if ( handlerInfo instanceof InternalHandlerInfoWrapper && !handlerInfo.preventInternalViewing )` → `document.createXULElement()`
- 条件付き依存: `if ( handlerInfo instanceof InternalHandlerInfoWrapper && !handlerInfo.preventInternalViewing )` → `internalMenuItem.setAttribute()`
- 条件付き依存: `if ( handlerInfo instanceof InternalHandlerInfoWrapper && !handlerInfo.preventInternalViewing )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( handlerInfo instanceof InternalHandlerInfoWrapper && !handlerInfo.preventInternalViewing )` → `menuPopup.appendChild()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `document.createXULElement()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `saveMenuItem.setAttribute()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `menuPopup.appendChild()`
- 条件付き依存: `if (handlerInfo.hasDefaultHandler)` → `document.createXULElement()`
- 条件付き依存: `if (handlerInfo.hasDefaultHandler)` → `defaultMenuItem.setAttribute()`
- 条件付き依存: `if (internalMenuItem)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (internalMenuItem)` → `defaultMenuItem.setAttribute()`
- 条件付き依存: `if (!(internalMenuItem))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (image)` → `defaultMenuItem.setAttribute()`
- 条件付き依存: `if (handlerInfo.hasDefaultHandler)` → `menuPopup.appendChild()`
- 条件付き依存: `if (possibleApp instanceof Ci.nsILocalHandlerApp)` → `getFileDisplayName()`
- 条件付き依存: `if (image)` → `menuItem.setAttribute()`
- 条件付き依存: `if (gGIOService)` → `gGIOService.getAppsForURIScheme()`
- 条件付き依存: `if (gGIOService)` → `gioApps.enumerate()`
- 条件付き依存: `if (gGIOService)` → `possibleHandlers.queryElementAt()`
- 条件付き依存: `if (gGIOService)` → `handler.equals()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `document.createXULElement()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `menuItem.setAttribute()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `getIconURLForHandlerApp()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `menuPopup.appendChild()`
- 条件付き依存: `if (!appAlreadyInHandlers)` → `possibleAppMenuItems.push()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Cc["@mozilla.org/mime;1"] .getService(Ci.nsIMIMEService) .getTypeFromExtension()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Cc["@mozilla.org/mime;1"] .getService()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `document.createXULElement()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `menuItem.addEventListener()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `AppFileHandler.chooseApp()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (canOpenWithOtherApp)` → `menuPopup.appendChild()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `document.createXULElement()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `menuPopup.appendChild()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `menuItem.addEventListener()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `AppFileHandler.manageApp()`
- 条件付き依存: `if (possibleAppMenuItems.length)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(internalMenuItem))` → `console.error()`
- 条件付き依存: `if (preferredApp)` → `possibleAppMenuItems.find()`
- 条件付き依存: `if (preferredApp)` → `v.handlerApp.equals()`
- 条件付き依存: `if (!(preferredItem))` → `possibleAppMenuItems .map(v => v.handlerApp && v.handlerApp.name) .join()`
- 条件付き依存: `if (!(preferredItem))` → `possibleAppMenuItems .map()`
- 条件付き依存: `if (!(preferredItem))` → `console.error()`
- 参照: `AppConstants.platform`, `Ci.nsIHandlerApp`, `Ci.nsIHandlerInfo.alwaysAsk`, `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIHandlerInfo.saveToDisk`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerInfo.useSystemDefault`, `Ci.nsILocalHandlerApp`, `Ci.nsIMIMEInfo`, `Ci.nsIMIMEService`, `askMenuItem.className`, `handler.name`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.defaultDescription`, `handlerInfo.hasDefaultHandler`, `handlerInfo.iconURLForSystemDefault`, `handlerInfo.possibleApplicationHandlers`, `handlerInfo.preferredAction`, `handlerInfo.preferredApplicationHandler`, `handlerInfo.preventInternalViewing`, `handlerInfo.type`, `handlerInfo.wrappedHandlerInfo`, `internalMenuItem.className`, `menu.menupopup`, `menu.selectedItem`, `menuItem.className`, `menuItem.handlerApp`, `menuPopup.lastChild`, `possibleApp.executable`, `possibleApp.name`, `possibleAppMenuItems.length`, `possibleHandlers.length`, `saveMenuItem.className`, `this._list.selectedItem`, `this.selectedHandlerListItem.handlerInfoWrapper`, `v.handlerApp`, `v.handlerApp.name`
- XPCOM: [`nsIHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsILocalHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMIMEInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMIMEService`](../../../netwerk/mime/nsIMIMEService.idl.md) / `@mozilla.org/mime;1`

## Handler.isValidHandlerApp()
- 位置: L2595-2616
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aHandlerApp instanceof Ci.nsILocalHandlerApp)` → `this._isValidHandlerExecutable()`
- 参照: `Ci.nsIGIOHandlerApp`, `Ci.nsIGIOMimeApp`, `Ci.nsILocalHandlerApp`, `Ci.nsIWebHandlerApp`, `aHandlerApp.command`, `aHandlerApp.executable`, `aHandlerApp.id`, `aHandlerApp.uriTemplate`
- XPCOM: [`nsIGIOHandlerApp`](../../../xpcom/system/nsIGIOService.idl.md) / [`nsIGIOMimeApp`](../../../xpcom/system/nsIGIOService.idl.md) / [`nsILocalHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md)

## Handler._isValidHandlerExecutable()
- 位置: L2618-2636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aExecutable.exists()`, `aExecutable.isExecutable()`
- 参照: `AppConstants.MOZ_APP_NAME`, `AppConstants.MOZ_MACBUNDLE_NAME`, `AppConstants.platform`, `aExecutable.leafName`
