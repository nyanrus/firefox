# browser/actors/ThemePickerParent.sys.mjs

source: browser/actors/ThemePickerParent.sys.mjs
source-hash: 897977804305b82afee8033856936ac785b27a6e
lines: 161

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ThemePickerParent.getThemesManager()
- 位置: async L24-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.themesManagers.get()`
- 条件付き依存: `if (!managerPromise)` → `lazy.getThemesList({ installSource }).catch()`
- 条件付き依存: `if (!managerPromise)` → `lazy.getThemesList()`
- 条件付き依存: `if (!managerPromise)` → `this.themesManagers.delete()`
- 条件付き依存: `if (!managerPromise)` → `this.themesManagers.set()`

## ThemePickerParent.receiveMessage()
- 位置: async L37-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getActiveThemeId()`, `this.getAppearance()`, `this.getInitialState()`, `this.getNativeTheme()`, `this.updateAppearance()`, `this.updateNativeTheme()`, `this.updateTheme()`
- 参照: `message.data`, `message.name`

## ThemePickerParent.getInitialState()
- 位置: async L64-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `themesManager.getThemesInfo()`, `this.getActiveThemeId()`, `this.getAppearanceFromPref()`, `this.getNativeTheme()`, `this.getThemesManager()`
- 参照: `AppConstants.platform`, `Services.appinfo .contentThemeDerivedColorSchemeIsDark`
- XPCOM: `Services.appinfo`

## ThemePickerParent.updateTheme()
- 位置: async L86-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `themesManager.updateThemeState()`, `this.getActiveThemeId()`, `this.getThemesManager()`

## ThemePickerParent.updateAppearance()
- 位置: async L92-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.themePicker.change.record()`, `this.getAppearance()`
- 条件付き依存: `if (appearance === "device")` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(appearance === "device"))` → `Services.prefs.setIntPref()`
- 参照: `result.appearance`
- XPCOM: `Services.prefs`

## ThemePickerParent.updateNativeTheme()
- 位置: async L113-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.themePicker.change.record()`, `Services.prefs.setBoolPref()`, `this.getNativeTheme()`
- 参照: `result.nativeTheme`
- XPCOM: `Services.prefs`

## ThemePickerParent.getActiveThemeId()
- 位置: L127-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## ThemePickerParent.getAppearance()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAppearanceFromPref()`

## ThemePickerParent.getAppearanceFromPref()
- 位置: L140-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## ThemePickerParent.getNativeTheme()
- 位置: L155-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`
