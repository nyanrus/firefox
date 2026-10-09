# browser/components/translations/content/TranslationsPanelShared.sys.mjs

source: browser/components/translations/content/TranslationsPanelShared.sys.mjs
source-hash: 0bfec642950e9ececafd10ba5e3fa6a5468565fc
lines: 230

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## TranslationsPanelShared.clearLanguageListsCache()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `TranslationsPanelShared.#langListsInitState`

## TranslationsPanelShared.defineLazyElements()
- 位置: L87-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Object.entries()`

## get()
- 位置: L91-105
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (discriminator[0] === ".")` → `document.querySelector()`
- 条件付き依存: `if (!(discriminator[0] === "."))` → `document.getElementById()`

## TranslationsPanelShared.simulateLangListError()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#simulateLangListError`

## TranslationsPanelShared.getLangListsInitState()
- 位置: L128-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsPanelShared.#langListsInitState.get()`

## TranslationsPanelShared.ensureLangListsBuilt()
- 位置: async L141-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsPanelShared.#langListsInitState.get()`, `TranslationsPanelShared.#langListsInitState.set()`, `document.createXULElement()`, `fromMenuItem.setAttribute()`, `lazy.TranslationsParent.getSupportedLanguages()`, `panelElement.querySelectorAll()`, `popup.appendChild()`, `popup.lastChild.remove()`, `toMenuItem.setAttribute()`
- 条件付き依存: `if (!TranslationsPanelShared.#observersInitialized)` → `Services.obs.addObserver()`
- 参照: `TranslationsPanelShared.#langListsInitState`, `TranslationsPanelShared.#observersInitialized`, `TranslationsPanelShared.clearLanguageListsCache`, `languagePairs.length`, `panel.elements`, `popup.lastChild?.value`, `this.#simulateLangListError`
- XPCOM: `Services.obs`
