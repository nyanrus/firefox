# browser/components/preferences/config/accessibility.mjs

source: browser/components/preferences/config/accessibility.mjs
source-hash: 1b9b856055cfa0c3bdc7aec40765d52500f4b2a1
lines: 650

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Services.prefs.getBoolPref()`, `SettingGroupManager.registerGroups()`, `String()`, `[ 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 40, 44, 48, 56, 64, 72, ].map()`

## visible()
- 位置: L44-44
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## visible()
- 位置: L52-52
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## get()
- 位置: L65-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._storedFullKeyboardNavigation`

## set()
- 位置: L74-82
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._storedFullKeyboardNavigation`

## visible()
- 位置: L96-99
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_WIDGET_GTK`, `AppConstants.platform`

## visible()
- 位置: L112-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.MOZ_WIDGET_GTK`

## onUserClick()
- 位置: L119-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## FullZoom()
- 位置: L131-133
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.FullZoom`

## ZoomManager()
- 位置: L134-136
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.win.ZoomManager`

## setDefaultZoom()
- 位置: async L144-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`, `Cu.createLoadContext()`, `Promise.withResolvers()`, `cps2.setGlobal()`
- 参照: `Ci.nsIContentPrefService2`, `resolvers.promise`, `resolvers.reject`, `resolvers.resolve`, `this.FullZoom.name`
- XPCOM: [`nsIContentPrefService2`](../../../../dom/interfaces/base/nsIContentPrefService2.idl.md) / `@mozilla.org/content-pref/service;1` → `ContentPrefService2` (toolkit/components/contentprefs/components.conf)

## getDefaultZoom()
- 位置: async L162-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomUI.getGlobalValue()`
- 参照: `this.win.ZoomUI`

## zoomValues()
- 位置: L174-176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.ZoomManager.zoomValues`

## toggleFullZoom()
- 位置: L178-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ZoomManager.toggleZoom()`

## set()
- 位置: async L192-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(parseInt(val, 10) / 100).toFixed()`, `ZoomHelpers.setDefaultZoom()`, `parseFloat()`, `parseInt()`

## get()
- 位置: async L197-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `String()`, `ZoomHelpers.getDefaultZoom()`

## getControlConfig()
- 位置: async L200-215
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.optionsConfig)` → `ZoomHelpers.zoomValues.map()`
- 条件付き依存: `if (!this.optionsConfig)` → `String()`
- 条件付き依存: `if (!this.optionsConfig)` → `Math.round()`
- 参照: `this.optionsConfig`

## get()
- 位置: L227-227
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `zoomTextPref.value`

## set()
- 位置: L228-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ZoomHelpers.toggleFullZoom()`

## disabled()
- 位置: L229-229
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `zoomTextPref.locked`

## visible()
- 位置: L234-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `zoomText.value`

## fetchLocalizedDefaultLabel()
- 位置: async L245-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatMessages()`, `msg?.attributes?.find()`, `this.enumerator.getDefaultFont()`
- 条件付き依存: `if (!defaultFont)` → `this.enumerator.getDefaultFont()`
- 条件付き依存: `if (labelAttr)` → `this._localizedDefaultLabels.set()`
- 参照: `a.name`, `labelAttr.value`

## enumerator()
- 位置: L264-271
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._enumerator)` → `Cc["@mozilla.org/gfx/fontenumerator;1"].createInstance()`
- 参照: `Ci.nsIFontEnumerator`, `this._enumerator`
- XPCOM: `nsIFontEnumerator` / `@mozilla.org/gfx/fontenumerator;1` → `nsThebesFontEnumerator` (gfx/src/components.conf)

## ensurePref()
- 位置: L273-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 条件付き依存: `if (!pref)` → `Preferences.add()`

## langGroup()
- 位置: L281-283
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.locale.fontLanguageGroup`
- XPCOM: `Services.locale`

## getFontTypePrefId()
- 位置: L285-287
- 役割: (未記入)
- 触るとき: (未記入)

## getFontType()
- 位置: L289-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `this.getFontTypePrefId()`
- XPCOM: `Services.prefs`

## getFontPrefId()
- 位置: L294-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getFontType()`

## getSizePrefId()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)

## buildFontOptions()
- 位置: L303-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.enumerator.EnumerateFonts()`
- 条件付き依存: `if (fonts.length)` → `this.enumerator.getDefaultFont()`
- 条件付き依存: `if (!(fonts.length))` → `this.enumerator.EnumerateFonts()`
- 条件付き依存: `if (!this._allFonts)` → `this.enumerator.EnumerateAllFonts()`
- 条件付き依存: `if (fonts.length)` → `this._localizedDefaultLabels.get()`
- 条件付き依存: `if (defaultFont)` → `options.push()`
- 条件付き依存: `if (!(defaultFont))` → `options.push()`
- 条件付き依存: `if (fonts.length)` → `options.push()`
- 条件付き依存: `if (this._allFonts.length > fonts.length)` → `fontSet.has()`
- 条件付き依存: `if (!fontSet.has(font))` → `options.push()`
- 参照: `fonts.length`, `this._allFonts`, `this._allFonts.length`

## setup()
- 位置: L379-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deps.fontLanguageGroup.off()`, `deps.fontLanguageGroup.on()`, `handleChange()`

## handleChange()
- 位置: L380-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FontHelpers.ensurePref()`, `FontHelpers.getFontTypePrefId()`, `emitChange()`
- 参照: `FontHelpers.langGroup`, `setting.pref`

## setup()
- 位置: L398-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deps.fontType.off()`, `deps.fontType.on()`, `handleChange()`

## handleChange()
- 位置: L399-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FontHelpers.ensurePref()`, `FontHelpers.fetchLocalizedDefaultLabel()`, `FontHelpers.fetchLocalizedDefaultLabel(langGroup, fontType) .then()`, `FontHelpers.getFontPrefId()`, `FontHelpers.getFontType()`, `emitChange()`
- 参照: `FontHelpers.langGroup`, `console.error`, `setting.pref`, `this.optionsConfig`

## getControlConfig()
- 位置: L420-431
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.optionsConfig)` → `FontHelpers.buildFontOptions()`
- 条件付き依存: `if (!this.optionsConfig)` → `FontHelpers.getFontType()`
- 参照: `FontHelpers.langGroup`, `this.optionsConfig`

## setup()
- 位置: L437-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `deps.fontLanguageGroup.off()`, `deps.fontLanguageGroup.on()`, `handleLangChange()`

## handleLangChange()
- 位置: L438-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FontHelpers.ensurePref()`, `FontHelpers.getSizePrefId()`, `emitChange()`
- 参照: `FontHelpers.langGroup`, `setting.pref`

## getControlConfig()
- 位置: L449-451
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `FontHelpers.fontSizeOptions`

## onUserClick()
- 位置: L456-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`

## onUserClick()
- 位置: L469-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`
