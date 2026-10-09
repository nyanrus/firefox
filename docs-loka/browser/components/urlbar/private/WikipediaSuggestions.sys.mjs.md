# browser/components/urlbar/private/WikipediaSuggestions.sys.mjs

source: browser/components/urlbar/private/WikipediaSuggestions.sys.mjs
source-hash: a2ccdce00c10b64e88f1bc25172b373aee65b1bf
lines: 110

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WikipediaSuggestions.enablingPreferences()
- 位置: L20-26
- 役割: (未記入)
- 触るとき: (未記入)

## WikipediaSuggestions.primaryUserControlledPreferences()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)

## WikipediaSuggestions.merinoProvider()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)

## WikipediaSuggestions.rustSuggestionType()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)

## WikipediaSuggestions.isSuggestionSponsored()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)

## WikipediaSuggestions.getSuggestionTelemetryType()
- 位置: L44-48
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `suggestion.source`

## WikipediaSuggestions.makeResult()
- 位置: L50-66
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `suggestion.fullKeyword`, `suggestion.full_keyword`, `suggestion.title`, `suggestion.url`

## WikipediaSuggestions.getResultCommands()
- 位置: L74-90
- 役割: (未記入)
- 触るとき: (未記入)

## WikipediaSuggestions.onEngagement()
- 位置: L98-108
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.QuickSuggest.dismissResult()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `details.selType`
