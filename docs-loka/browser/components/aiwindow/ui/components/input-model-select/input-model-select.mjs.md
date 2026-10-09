# browser/components/aiwindow/ui/components/input-model-select/input-model-select.mjs

source: browser/components/aiwindow/ui/components/input-model-select/input-model-select.mjs
source-hash: ea4ef034174b1f96298998928abab3c6f9568d57
lines: 293

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## getModelDisplayOrder()
- 位置: L26-26
- 役割: (未記入)
- 触るとき: (未記入)

## InputModelSelect.constructor()
- 位置: L76-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `crypto.randomUUID()`, `super()`, `this.requestUpdate()`
- 参照: `this._menuId`, `this.availableModels`, `this.defaultModelChoiceId`, `this.mistralRelease`, `this.panelOpen`, `this.selectedModelId`, `this.sidebarMode`

## InputModelSelect.#caretIcon()
- 位置: L99-103
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.panelOpen`

## InputModelSelect.#onPanelShown()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.panelOpen`

## InputModelSelect.#onPanelHidden()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.panelOpen`

## InputModelSelect.#modelsList()
- 位置: L113-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(this.availableModels) .map()`, `Object.entries(this.availableModels) .map(([index, availableModel]) => ({ ...availableModel, index, })) .sort()`, `getModelDisplayOrder()`, `rank()`
- 参照: `a.index`, `b.index`, `this.availableModels`

## rank()
- 位置: L118-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `order.indexOf()`
- 参照: `order.length`

## InputModelSelect.#selectedModel()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#modelsList.find()`
- 参照: `m.model`, `this.selectedModelId`

## InputModelSelect.#setModelId()
- 位置: L139-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#modelsList.find()`
- 条件付き依存: `if (!selectedModel)` → `console.error()`
- 条件付き依存: `if (modelId !== this.selectedModelId)` → `this.dispatchEvent()`
- 参照: `m.model`, `selectedModel.index`, `this.selectedModelId`

## InputModelSelect.#openSmartwindowSettings()
- 位置: L158-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## InputModelSelect.#getButtonLabelL10nId()
- 位置: L167-169
- 役割: (未記入)
- 触るとき: (未記入)

## InputModelSelect.#getDescriptionL10nId()
- 位置: L171-179
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.mistralRelease`

## InputModelSelect.#iconSrc()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.mistralRelease`

## InputModelSelect.render()
- 位置: L185-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#getButtonLabelL10nId()`, `this.#getDescriptionL10nId()`, `this.#iconSrc()`, `this.#setModelId()`
- 条件付き依存: `if (!this.#modelsList.length || !this.#selectedModel)` → `html()`
- 参照: `item.index`, `item.model`, `item.ownerName`, `item.shortName`, `this.#caretIcon`, `this.#modelsList`, `this.#modelsList.length`, `this.#onPanelHidden`, `this.#onPanelShown`, `this.#openSmartwindowSettings`, `this.#selectedModel`, `this.#selectedModel.brandName`, `this.#selectedModel.index`, `this._menuId`, `this.defaultModelChoiceId`, `this.mistralRelease`, `this.selectedModelId`
