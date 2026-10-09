# browser/components/urlbar/private/MDNSuggestions.sys.mjs

source: browser/components/urlbar/private/MDNSuggestions.sys.mjs
source-hash: 36946f67baaa02cc3dd409d015c85808a9407965
lines: 195

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MDNSuggestions.enablingPreferences()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)

## MDNSuggestions.primaryUserControlledPreferences()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)

## MDNSuggestions.merinoProvider()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)

## MDNSuggestions.rustSuggestionType()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)

## MDNSuggestions.makeResult()
- 位置: async L43-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.searchParams.set()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_NETWORK`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `searchString.length`, `suggestion.description`, `suggestion.title`, `suggestion.url`, `this.#minKeywordLength`, `this.isEnabled`, `this.showLessFrequentlyCount`, `url.href`

## MDNSuggestions.getResultCommands()
- 位置: L94-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## MDNSuggestions.onEngagement()
- 位置: L138-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `searchString.length`

## MDNSuggestions.incrementShowLessFrequentlyCount()
- 位置: L168-175
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## MDNSuggestions.showLessFrequentlyCount()
- 位置: L177-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## MDNSuggestions.canShowLessFrequently()
- 位置: L182-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## MDNSuggestions.#minKeywordLength()
- 位置: L190-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`
