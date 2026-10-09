# browser/components/aiwindow/ui/modules/SmartFormFillAutocomplete.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillAutocomplete.sys.mjs
source-hash: 151454d4331af5e61882ee9a9d1ade4922816ca9
lines: 274

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## SmartFormFillAutocompleteItem.constructor()
- 位置: L82-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`
- 参照: `comment.secondaryAction`, `this.comment`, `this.image`, `this.label`

## autocompleteItemsAsync()
- 位置: async L149-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SUPPORTED_INPUT_TYPES.includes()`, `browsingContext.currentWindowGlobal.getActor()`, `lazy.AIWindow.isAIWindowActive()`, `sffActor.searchAutoCompleteEntries()`
- 参照: `browsingContext?.topChromeWindow`, `lazy.SFF_ENABLED`, `result?.entries`

## createItemsAsync()
- 位置: async L198-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ label, loading ? loadingLabel : (emptySourcesLabel ?? sourcesPillsLabel), ].join()`, `lazy.l10n.formatValue()`, `lazy.l10n.formatValues()`, `sffActor.areRelevantTabsReady()`, `sffActor.getSelectedTabSources()`
- 参照: `sffActor.getSelectedTabSources(formId).length`, `sffActor.hasSourceTabs`

## updatePopupSources()
- 位置: L263-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.autoCompletePopup.querySelector()`, `item?.querySelector()`
- 参照: `row.sources`
