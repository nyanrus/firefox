# browser/components/urlbar/private/SuggestFeature.sys.mjs

source: browser/components/urlbar/private/SuggestFeature.sys.mjs
source-hash: 7b58b2bb0065a7ae202076ee2be774d2cc0daa90
lines: 472

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SuggestFeature.enablingPreferences()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestFeature.primaryUserControlledPreferences()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestFeature.shouldEnable()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.enablingPreferences.every()`

## SuggestFeature.enable()
- 位置: L86-86
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestFeature.logger()
- 位置: L94-101
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._logger)` → `lazy.UrlbarShared.getLogger()`
- 参照: `this._logger`, `this.name`

## SuggestFeature.isEnabled()
- 位置: L108-110
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isEnabled`

## SuggestFeature.name()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.constructor.name`

## SuggestFeature.update()
- 位置: L125-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (enable != this.isEnabled)` → `this.logger.info()`
- 条件付き依存: `if (enable != this.isEnabled)` → `this.enable()`
- 参照: `this.#isEnabled`, `this.isEnabled`, `this.shouldEnable`

## SuggestProvider.merinoProvider()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.rustSuggestionType()
- 位置: L174-176
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.dynamicRustSuggestionTypes()
- 位置: L185-187
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.rustProviderConstraints()
- 位置: L197-204
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dynamicRustSuggestionTypes`, `this.dynamicRustSuggestionTypes?.length`

## SuggestProvider.mlIntent()
- 位置: L212-214
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.isMlIntentEnabled()
- 位置: L222-224
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.getSuggestionTelemetryType()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.merinoProvider`

## SuggestProvider.getResultCommands()
- 位置: L254-256
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.canShowLessFrequently()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.incrementShowLessFrequentlyCount()
- 位置: L272-272
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.isSuggestionSponsored()
- 位置: L284-286
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.filterSuggestions()
- 位置: async L305-307
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.makeResult()
- 位置: async L325-327
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.onImpression()
- 位置: L346-346
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.onEngagement()
- 位置: L364-364
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestProvider.isUrlEquivalentToResultUrl()
- 位置: L382-384
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.url`

## SuggestProvider.handleShowLessFrequently()
- 位置: L399-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.view.acknowledgeFeedback()`, `this.incrementShowLessFrequentlyCount()`
- 条件付き依存: `if (!this.canShowLessFrequently)` → `controller.view.updateResultMenuCommands()`
- 条件付き依存: `if (!this.canShowLessFrequently)` → `this.getResultCommands()`
- 参照: `result.id`, `this.canShowLessFrequently`

## SuggestProvider.update()
- 位置: L414-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.rustBackend?.ingestEnabledSuggestions()`, `super.update()`

## SuggestBackend.query()
- 位置: async L449-451
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestBackend.cancelQuery()
- 位置: L457-457
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestBackend.onSearchSessionEnd()
- 位置: L470-470
- 役割: (未記入)
- 触るとき: (未記入)
