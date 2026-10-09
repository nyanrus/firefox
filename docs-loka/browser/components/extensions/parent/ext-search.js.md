# browser/components/extensions/parent/ext-search.js

source: browser/components/extensions/parent/ext-search.js
source-hash: 61f88ed4f74b458bb7cbbc53cf5303017d186c63
lines: 124

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getAPI()
- 位置: L21-122
- 役割: (未記入)
- 触るとき: (未記入)

## getTarget()
- 位置: L22-35
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tabId)` → `tabTracker.getTab()`

## get()
- 位置: async L39-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionUtils.isExtensionUrl()`, `Promise.all()`, `SearchService.getDefault()`, `SearchService.getVisibleEngines()`, `engine.getIconURL()`, `favIconUrl.startsWith()`, `visibleEngines.map()`
- 条件付き依存: `if ( favIconUrl && (favIconUrl.startsWith("blob:") || (ExtensionUtils.isExtensionUrl(favIconUrl) && !favIconUrl.startsWith(context.extension.baseURL))) )` → `ExtensionUtils.makeDataURI()`
- 参照: `SearchService.promiseInitialized`, `context.extension.baseURL`, `defaultEngine.name`, `engine.alias`, `engine.name`

## search()
- 位置: async L72-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SearchUIUtils.loadSearch()`, `getTarget()`
- 条件付き依存: `if (searchProperties.engine)` → `SearchService.getEngineByName()`
- 参照: `SearchService.promiseInitialized`, `context.principal`, `searchProperties.disposition`, `searchProperties.engine`, `searchProperties.query`, `searchProperties.tabId`, `windowTracker.topWindow`

## query()
- 位置: async L102-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SearchUIUtils.loadSearch()`, `getTarget()`
- 参照: `SearchService.promiseInitialized`, `context.principal`, `queryProperties.disposition`, `queryProperties.tabId`, `queryProperties.text`, `windowTracker.topWindow`
