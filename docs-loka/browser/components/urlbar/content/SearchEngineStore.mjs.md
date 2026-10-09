# browser/components/urlbar/content/SearchEngineStore.mjs

source: browser/components/urlbar/content/SearchEngineStore.mjs
source-hash: 6d9c262c83945b27d7c2e44ff8f5d26ab960a4ed
lines: 346

## <module>
- 役割: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `UrlbarShared.getLogger()`

## PartialSearchEngine.constructor()
- 位置: L43-53
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `engineInfo.aliases`, `engineInfo.hideOneOffButton`, `engineInfo.id`, `engineInfo.isAppProvided`, `engineInfo.isConfigEngine`, `engineInfo.isGeneralPurposeEngine`, `engineInfo.isNewUntil`, `engineInfo.name`, `this.#controller`, `this.aliases`, `this.hideOneOffButton`, `this.id`, `this.isAppProvided`, `this.isConfigEngine`, `this.isGeneralPurposeEngine`, `this.isNewUntil`, `this.name`

## PartialSearchEngine.getIconURL()
- 位置: async L69-76
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#icon === undefined)` → `this.#controller.parentController.getEngineIconURL()`
- 参照: `this.#icon`, `this.id`

## PartialSearchEngine.isNew()
- 位置: L83-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date().toISOString()`, `new Date().toISOString().slice()`
- 参照: `this.isNewUntil`

## PartialSearchEngine.invalidateIcon()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#icon`

## PartialSearchEngine.markAsUsed()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.parentController.markEngineAsUsed()`
- 参照: `this.id`

## SearchEngineStore.constructor()
- 位置: L129-132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `controller.input.isPrivate`, `this.#controller`, `this.isPrivate`

## SearchEngineStore.init()
- 位置: L141-147
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized && !this.failed)` → `this.#controller.parentController.initEngineStore()`
- 参照: `this.#initPromiseWithResolvers.promise`, `this.failed`, `this.initialized`

## SearchEngineStore.default()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#defaultEngine`

## SearchEngineStore.getEngine()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store.find()`
- 参照: `e.id`

## SearchEngineStore.getEngines()
- 位置: L172-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#store`, `this.initialized`

## SearchEngineStore.getEngineByName()
- 位置: L184-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#store.find()`
- 参照: `e.name`

## SearchEngineStore.addObserver()
- 位置: L191-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observers.includes()`
- 条件付き依存: `if (!this.#observers.includes(observer))` → `this.#observers.push()`

## SearchEngineStore.removeObserver()
- 位置: L200-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observers.findIndex()`
- 条件付き依存: `if (index != -1)` → `this.#observers.splice()`

## SearchEngineStore.receive()
- 位置: L213-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleError()`, `this.#handleInit()`, `this.#handleUpdate()`

## SearchEngineStore.#handleInit()
- 位置: L239-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#initPromiseWithResolvers.resolve()`, `this.#store.push()`
- 参照: `this.#controller`, `this.#defaultEngine`, `this.#store`, `this.initialized`

## SearchEngineStore.#handleError()
- 位置: L257-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#initPromiseWithResolvers.reject()`
- 参照: `this.failed`, `this.initialized`

## SearchEngineStore.#handleUpdate()
- 位置: L279-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `engine.invalidateIcon()`, `this.#notifyObservers()`, `this.#store.findIndex()`
- 条件付き依存: `if (currentIndex != -1)` → `this.#store.splice()`
- 条件付き依存: `if (currentIndex != -1)` → `this.#notifyObservers()`
- 条件付き依存: `if (newIndex == -1)` → `this.#store.push()`
- 条件付き依存: `if (!(newIndex == -1))` → `this.#store.splice()`
- 条件付き依存: `if (currentIndex == -1)` → `this.#notifyObservers()`
- 条件付き依存: `if (newIndex != currentIndex)` → `this.#store.splice()`
- 条件付き依存: `if (currentIndex == -1)` → `logger.warn()`
- 参照: `e.id`, `engineInfo.id`, `this.#controller`, `this.#defaultEngine`, `this.#store`, `this.initialized`

## SearchEngineStore.#notifyObservers()
- 位置: L340-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `observer()`
- 参照: `this.#observers`
