# browser/themes/ThemesList.sys.mjs

source: browser/themes/ThemesList.sys.mjs
source-hash: bf2b430244d6f880712c97f4b78d31c520bad4ea
lines: 471

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `FIREFOX_THEMES_LIST.map()`

## themeColorVariantAsImage()
- 位置: L285-287
- 役割: (未記入)
- 触るとき: (未記入)

## ThemesList.constructor()
- 位置: L300-302
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#installSource`

## ThemesList.getThemesInfo()
- 位置: L311-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `FIREFOX_THEMES_MAP.values()`, `themes.map()`
- 条件付き依存: `if (showInCompactLayout)` → `themes.filter()`
- 参照: `theme.showInCompactLayout`

## ThemesList.hasThemeId()
- 位置: L326-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FIREFOX_THEMES_MAP.has()`

## ThemesList.isBuiltIn()
- 位置: L335-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FIREFOX_THEMES_MAP.get()`
- 参照: `FIREFOX_THEMES_MAP.get(themeId)?.isBuiltIn`

## ThemesList.getThemePreviewLinkParameters()
- 位置: L346-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FIREFOX_THEMES_MAP.get()`, `Object.entries()`, `Object.entries(params) .map()`, `Object.entries(params) .map(([name, value]) => `param(${name}, ${value})`) .join()`, `lightDark()`, `themeColorVariantAsImage()`
- 参照: `theme?.themePreviewColors`, `themePickerColors.dark`, `themePickerColors.light`

## lightDark()
- 位置: L352-353
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `themePreviewColors.dark`, `themePreviewColors.light`

## ThemesList.updateThemeState()
- 位置: async L383-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.themePicker.change.record()`, `console.error()`, `install.install()`, `lazy.AddonManager.getAddonByID()`, `lazy.AddonManager.getInstallForURL()`, `lazy.AddonRepository.getAddonsByIDs()`, `theme.enable()`, `this.hasThemeId()`
- 条件付き依存: `if (!this.hasThemeId(themeId))` → `console.error()`
- 条件付き依存: `if (!enabled)` → `addon?.disable()`
- 条件付き依存: `if (!layout)` → `console.error()`
- 条件付き依存: `if (addon)` → `addon.enable()`
- 条件付き依存: `if (addon)` → `Glean.themePicker.change.record()`
- 条件付き依存: `if (!repoAddon?.sourceURI)` → `console.error()`
- 条件付き依存: `if (installListener)` → `install.addListener()`
- 条件付き依存: `if (installListener)` → `install?.removeListener()`
- 参照: `repoAddon.name`, `repoAddon.sourceURI.spec`, `repoAddon?.sourceURI`, `this.#installSource`

## getThemesList()
- 位置: async L465-470
- 役割: (未記入)
- 触るとき: (未記入)
