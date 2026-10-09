# browser/components/urlbar/private/SuggestBackendMl.sys.mjs

source: browser/components/urlbar/private/SuggestBackendMl.sys.mjs
source-hash: dec7f4157cfbe9d096ab4142aea30c7dd51ef7e8
lines: 112

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SuggestBackendMl.enablingPreferences()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestBackendMl.enable()
- 位置: L26-32
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (enabled)` → `this.#init()`
- 条件付き依存: `if (!(enabled))` → `this.#uninit()`

## SuggestBackendMl.query()
- 位置: async L47-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MLSuggest.makeSuggestions()`, `lazy.QuickSuggest.mlFeatures .values()`, `lazy.QuickSuggest.mlFeatures .values() .every()`, `this.logger.debug()`
- 条件付き依存: `if ( lazy.QuickSuggest.mlFeatures .values() .every(f => !f.isEnabled || !f.isMlIntentEnabled) )` → `this.logger.debug()`
- 条件付き依存: `if (suggestion?.intent)` → `lazy.QuickSuggest.getFeatureByMlIntent()`
- 条件付き依存: `if (!feature?.isEnabled || !feature?.isMlIntentEnabled)` → `this.logger.debug()`
- 参照: `f.isEnabled`, `f.isMlIntentEnabled`, `feature?.isEnabled`, `feature?.isMlIntentEnabled`, `queryContext.trimmedLowerCaseSearchString`, `suggestion.intent`, `suggestion.provider`, `suggestion.source`, `suggestion?.intent`

## SuggestBackendMl.#init()
- 位置: L84-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.SkippableTimer`, `this.#initTimer`, `this.logger`, `this.name`

## callback()
- 位置: async L97-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MLSuggest.initialize()`, `this.logger.info()`

## SuggestBackendMl.#uninit()
- 位置: async L104-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MLSuggest.shutdown()`, `this.#initTimer?.cancel()`
- 参照: `this.#initTimer`
