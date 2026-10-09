# browser/components/preferences/config/appearance.mjs

source: browser/components/preferences/config/appearance.mjs
source-hash: 7675fab2253d0e962b3a2d5b9e7e4028d8dcf8fc
lines: 434

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-ui-utils;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`, `isAutoTouchModeAvailable()`, `matchMedia()`

## getUIDensity()
- 位置: L32-35
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext.topChromeWindow.gUIDensity`

## isAutoTouchModeAvailable()
- 位置: L41-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_WIDGET_GTK`, `lazy.WindowsUIUtils.isTabletCapable`

## isBrowserIconAvailable()
- 位置: L50-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.sysinfo.getProperty()`
- XPCOM: `Services.prefs` / `Services.sysinfo`

## setup()
- 位置: L66-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FORCED_COLORS_QUERY.addEventListener()`, `FORCED_COLORS_QUERY.removeEventListener()`

## visible()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `FORCED_COLORS_QUERY.matches`

## setup()
- 位置: L80-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## get()
- 位置: L85-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `setting.pref.defaultValue`, `this.themeNames`

## set()
- 位置: L92-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.themeNames.indexOf()`

## getControlConfig()
- 位置: L95-106
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.appinfo .contentThemeDerivedColorSchemeIsDark`, `config.options`, `config.options[0].controlAttrs`, `config.options[systemThemeIndex].controlAttrs.imagesrc`
- XPCOM: `Services.appinfo`

## onUserClick()
- 位置: L112-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.browsingContext.topChromeWindow.BrowserAddonUI.openAddonsMgr()`

## onUserClick()
- 位置: L123-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## onUserClick()
- 位置: L131-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## onUserClick()
- 位置: L139-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## setup()
- 位置: L153-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## observer()
- 位置: L154-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`

## visible()
- 位置: L168-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isAutoTouchModeAvailable()`
- 参照: `uiDensity.value`

## visible()
- 位置: L175-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## get()
- 位置: L183-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getUIDensity()`
- 参照: `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_TOUCH`, `uiDensityPref.pref.hasUserValue`, `uiDensityPref.value`

## set()
- 位置: L197-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.setIntPref()`, `getUIDensity()`
- 参照: `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_NORMAL`, `gUIDensity.MODE_TOUCH`, `uiDensityPref.pref`
- XPCOM: `Services.prefs`

## onUserClick()
- 位置: L219-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## visible()
- 位置: L227-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isBrowserIconAvailable()`

## setup()
- 位置: L236-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `COLOR_SCHEME_QUERY.addEventListener()`, `COLOR_SCHEME_QUERY.removeEventListener()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## observer()
- 位置: L237-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`

## getControlConfig()
- 位置: L245-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `isBrowserIconAvailable()`, `lazy.resolvePreview()`
- 参照: `COLOR_SCHEME_QUERY.matches`, `entry.l10nId`, `lazy.ICON_CATALOG`, `lazy.ICON_CATALOG.default`
- XPCOM: `Services.prefs`
