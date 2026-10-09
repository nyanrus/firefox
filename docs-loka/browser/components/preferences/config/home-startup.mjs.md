# browser/components/preferences/config/home-startup.mjs

source: browser/components/preferences/config/home-startup.mjs
source-hash: 4c19e7d08db873c52c24815cd9ed6b29c1f6c93c
lines: 846

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Preferences.addAll()`, `SettingGroupManager.registerGroups()`, `setupCustomHomepageGroup()`, `setupHomepageGroup()`, `window.createDefaultBrowserConfig()`, `window.createStartupConfig()`

## getExtensionOptions()
- 位置: async L55-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`, `lazy.ExtensionSettingsStore.getAllSettings()`, `lazy.ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (policy)` → `options.push()`
- 参照: `policy.id`, `policy.name`

## getActiveExtensionForSetting()
- 位置: L74-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`, `console.error()`, `lazy.ExtensionSettingsStore.getSetting()`
- 参照: `setting.id`, `setting?.id`

## getHomepageActiveExtension()
- 位置: L85-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.prefs.getStringPref()`, `WebExtensionPolicy.getByURI()`, `getActiveExtensionForSetting()`
- XPCOM: `Services.io` / `Services.prefs`

## makeAddonListenerForRefresh()
- 位置: L102-109
- 役割: (未記入)
- 触るとき: (未記入)

## makeExtensionSettingChangedListener()
- 位置: L111-117
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (changedSetting.key === key && changedSetting.type === type)` → `refreshFn()`
- 参照: `changedSetting.key`, `changedSetting.type`

## forceSelectValue()
- 位置: L119-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prefWindow.document.getElementById()`, `prefWindow.requestAnimationFrame()`
- 参照: `control.controlEl.value`, `prefWindow.closed`

## setupHomepageGroup()
- 位置: L138-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.Management.asyncLoadSettingsModules()`, `lazy.Management.asyncLoadSettingsModules().catch()`, `panelPrefs.addSetting()`

## setup()
- 位置: L156-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `console.error()`, `lazy.AddonManager.addAddonListener()`, `lazy.AddonManager.removeAddonListener()`, `lazy.Management.off()`, `lazy.Management.on()`, `makeAddonListenerForRefresh()`, `makeExtensionSettingChangedListener()`, `refreshExtensions()`, `refreshExtensions().catch()`
- XPCOM: `Services.prefs`

## refreshExtensions()
- 位置: async L157-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getExtensionOptions()`
- 条件付き依存: `if (!prefWindow.closed)` → `onChange()`
- 条件付き依存: `if (!prefWindow.closed)` → `getHomepageActiveExtension()`
- 条件付き依存: `if (!prefWindow.closed)` → `forceSelectValue()`
- 参照: `ext?.id`, `prefWindow.closed`

## homepagePrefObserver()
- 位置: L176-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `forceSelectValue()`, `getHomepageActiveExtension()`, `onChange()`
- 参照: `ext?.id`

## get()
- 位置: L205-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getHomepageActiveExtension()`
- 参照: `ext.id`, `this.useCustomHomepage`

## set()
- 位置: L224-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["home", "blank", "custom"].includes()`, `console.error()`, `lazy.ExtensionPreferencesManager.selectSetting()`, `lazy.ExtensionPreferencesManager.selectSetting( inputVal, HOMEPAGE_OVERRIDE_KEY ).catch()`
- 条件付き依存: `if (wasCustomHomepage !== this.useCustomHomepage)` → `setting.onChange()`
- 条件付き依存: `if (["home", "blank", "custom"].includes(inputVal))` → `getActiveExtensionForSetting()`
- 条件付き依存: `if (currentAddon)` → `lazy.ExtensionSettingsStore.select()`
- 条件付き依存: `if (currentAddon)` → `console.error()`
- 参照: `setting.pref.value`, `this.useCustomHomepage`

## getControlConfig()
- 位置: L270-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `builtinValues.has()`, `config.options.filter()`, `extOptions.some()`, `getHomepageActiveExtension()`
- 条件付き依存: `if (ext && !extOptions.some(o => o.value === ext.id))` → `extOptions.push()`
- 参照: `ext.id`, `ext.name`, `o.value`

## visible()
- 位置: L317-319
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `homepageNewWindows.value`

## onUserClick()
- 位置: L320-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prefWindow.gotoPref()`

## getControlConfig()
- 位置: L324-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes()`, `homepageDisplayPref.value.trim()`
- 条件付き依存: `if (!([DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(prefVal)))` → `homepageDisplayPref.value .split("|") .map(uri => lazy.BrowserUtils.formatURIStringForDisplay(uri)) .filter()`
- 条件付き依存: `if (!([DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(prefVal)))` → `homepageDisplayPref.value .split("|") .map()`
- 条件付き依存: `if (!([DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(prefVal)))` → `homepageDisplayPref.value .split()`
- 条件付き依存: `if (!([DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(prefVal)))` → `lazy.BrowserUtils.formatURIStringForDisplay()`
- 参照: `config.controlAttrs`

## setup()
- 位置: L358-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `console.error()`, `lazy.AddonManager.addAddonListener()`, `lazy.AddonManager.removeAddonListener()`, `lazy.Management.off()`, `lazy.Management.on()`, `makeAddonListenerForRefresh()`, `makeExtensionSettingChangedListener()`, `refreshExtensions()`, `refreshExtensions().catch()`
- XPCOM: `Services.obs`

## refreshExtensions()
- 位置: async L359-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getExtensionOptions()`
- 条件付き依存: `if (!prefWindow.closed)` → `onChange()`
- 条件付き依存: `if (!prefWindow.closed)` → `getActiveExtensionForSetting()`
- 条件付き依存: `if (!prefWindow.closed)` → `forceSelectValue()`
- 参照: `getActiveExtensionForSetting( URL_OVERRIDES_TYPE, NEW_TAB_KEY )?.id`, `prefWindow.closed`

## newTabObserver()
- 位置: L386-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `refreshExtensions()`

## get()
- 位置: L398-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActiveExtensionForSetting()`
- 参照: `getActiveExtensionForSetting( URL_OVERRIDES_TYPE, NEW_TAB_KEY )?.id`

## set()
- 位置: L410-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.ExtensionSettingsStore.select()`
- 条件付き依存: `if (inputVal === "home" || inputVal === "blank")` → `getActiveExtensionForSetting()`
- 条件付き依存: `if (currentAddon)` → `lazy.ExtensionSettingsStore.select()`
- 条件付き依存: `if (currentAddon)` → `console.error()`

## getControlConfig()
- 位置: L443-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `builtinValues.has()`, `config.options.filter()`
- 参照: `o.value`

## disabled()
- 位置: L462-466
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `homepageNewTabs.value`, `homepageNewWindows.value`

## onUserClick()
- 位置: L467-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`
- 参照: `homepageNewTabs.value`, `homepageNewWindows.value`

## setupCustomHomepageGroup()
- 位置: L527-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelPrefs.addSetting()`

## get()
- 位置: L535-537
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._inputValue`

## set()
- 位置: L538-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setting.onChange()`, `val.trim()`
- 参照: `this._inputValue`

## disabled()
- 位置: L542-544
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `homepageDisplayPref.locked`

## onUserClick()
- 位置: L551-581
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes()`, `currentVal.startsWith()`, `e.target.focus()`, `homepageDisplayPref.value.trim()`
- 条件付き依存: `if (!( [DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(currentVal) || currentVal.startsWith("moz-extension://") ))` → `lazy.HomePage.parseCustomHomepageURLs()`
- 条件付き依存: `if (!( [DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(currentVal) || currentVal.startsWith("moz-extension://") ))` → `urls.push()`
- 条件付き依存: `if (!( [DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(currentVal) || currentVal.startsWith("moz-extension://") ))` → `urls.join()`
- 参照: `customHomepageAddUrlInput.value`, `homepageDisplayPref.value`

## disabled()
- 位置: L582-584
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `homepageDisplayPref.locked`

## setup()
- 位置: L592-623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `tabContainer.addEventListener()`, `tabContainer.removeEventListener()`
- 参照: `win.gBrowser`
- XPCOM: `Services.wm`

## onTabChange()
- 位置: L603-612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`, `event.target.linkedBrowser?.currentURI?.spec?.startsWith()`

## onUserClick()
- 位置: L624-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.HomePage.getTabsForCustomHomepage()`
- 条件付き依存: `if (tabs.length)` → `tabs .map(t => t.linkedBrowser.currentURI.spec) .join()`
- 条件付き依存: `if (tabs.length)` → `tabs .map()`
- 参照: `homepageDisplayPref.value`, `t.linkedBrowser.currentURI.spec`, `tabs.length`

## disabled()
- 位置: L633-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.HomePage.getTabsForCustomHomepage()`
- 参照: `disableCurrentPagesButton?.value`, `homepageDisplayPref.locked`, `lazy.HomePage.getTabsForCustomHomepage().length`

## onUserClick()
- 位置: L644-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prefWindow.gSubDialog.open()`

## closingCallback()
- 位置: L648-655
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (rv.urls)` → `rv.urls.join()`
- 参照: `event.detail.button`, `homepageDisplayPref.value`, `rv.urls`

## disabled()
- 位置: L666-668
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `disableBookmarkButton?.value`, `homepageDisplayPref.locked`

## setup()
- 位置: L674-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.addAddonListener()`, `lazy.AddonManager.removeAddonListener()`, `lazy.Management.off()`, `lazy.Management.on()`, `makeAddonListenerForRefresh()`, `makeExtensionSettingChangedListener()`

## getControlConfig()
- 位置: L694-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes()`, `homepageDisplayPref.value.trim()`, `lazy.HomePage.parseCustomHomepageURLs()`
- 条件付き依存: `if ( ![DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(currentPrefVal) )` → `urls.map()`
- 条件付き依存: `if ( ![DEFAULT_HOMEPAGE_URL, BLANK_HOMEPAGE_URL].includes(currentPrefVal) )` → `lazy.BrowserUtils.formatURIStringForDisplay()`
- 参照: `config.controlAttrs`, `homepageDisplayPref.locked`, `homepageDisplayPref.value`

## onUserReorder()
- 位置: L798-804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.reorderArrayFromEvent()`, `lazy.HomePage.parseCustomHomepageURLs()`, `urls.join()`
- 参照: `homepageDisplayPref.value`

## onUserClick()
- 位置: L805-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`, `lazy.HomePage.parseCustomHomepageURLs()`
- 条件付き依存: `if ( e.target.localName === "moz-button" && e.target.getAttribute("data-action") === "delete" )` → `Number()`
- 条件付き依存: `if ( e.target.localName === "moz-button" && e.target.getAttribute("data-action") === "delete" )` → `Number.isInteger()`
- 条件付き依存: `if (Number.isInteger(index) && index >= 0 && index < urls.length)` → `urls.splice()`
- 条件付き依存: `if (Number.isInteger(index) && index >= 0 && index < urls.length)` → `urls.join()`
- 参照: `e.target.dataset.index`, `e.target.localName`, `homepageDisplayPref.value`, `urls.length`
