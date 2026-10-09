# browser/components/urlbar/private/AddonSuggestions.sys.mjs

source: browser/components/urlbar/private/AddonSuggestions.sys.mjs
source-hash: f40a1a58bb3e7b53254aeaa77d6739c5a197f166
lines: 215

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AddonSuggestions.enablingPreferences()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)

## AddonSuggestions.primaryUserControlledPreferences()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## AddonSuggestions.merinoProvider()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)

## AddonSuggestions.rustSuggestionType()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)

## AddonSuggestions.makeResult()
- 位置: async L49-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `lazy.AddonManager.getAddonByID()`, `url.searchParams.has()`
- 条件付き依存: `if (!url.searchParams.has(key))` → `url.searchParams.set()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `searchString.length`, `suggestion.custom_details.amo`, `suggestion.description`, `suggestion.icon`, `suggestion.iconUrl`, `suggestion.source`, `suggestion.title`, `suggestion.url`, `this.#minKeywordLength`, `this.isEnabled`, `this.showLessFrequentlyCount`, `url.href`

## AddonSuggestions.getResultCommands()
- 位置: L111-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## AddonSuggestions.onEngagement()
- 位置: L155-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `searchString.length`

## AddonSuggestions.incrementShowLessFrequentlyCount()
- 位置: L188-195
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## AddonSuggestions.showLessFrequentlyCount()
- 位置: L197-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## AddonSuggestions.canShowLessFrequently()
- 位置: L202-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## AddonSuggestions.#minKeywordLength()
- 位置: L210-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`
