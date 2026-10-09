# browser/themes/BuiltInThemes.sys.mjs

source: browser/themes/BuiltInThemes.sys.mjs
source-hash: 61343fb1f00a225d516a079a56fe3b4d085b2690
lines: 77

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _BuiltInThemes.previewForBuiltInThemeId()
- 位置: L27-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.builtInThemeMap.get()`
- 参照: `theme.path`

## _BuiltInThemes.maybeInstallActiveBuiltInTheme()
- 位置: L40-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `this.builtInThemeMap.get()`
- 条件付き依存: `if (activeBuiltInTheme)` → `lazy.AddonManager.maybeInstallBuiltinAddon()`
- 参照: `activeBuiltInTheme.path`, `activeBuiltInTheme.version`
- XPCOM: `Services.prefs`

## _BuiltInThemes.ensureBuiltInThemes()
- 位置: async L59-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `installPromises.push()`, `lazy.AddonManager.maybeInstallBuiltinAddon()`, `this.builtInThemeMap.entries()`
- 参照: `themeInfo.path`, `themeInfo.version`
