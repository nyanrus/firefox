# browser/components/urlbar/UrlbarProviderOmnibox.sys.mjs

source: browser/components/urlbar/UrlbarProviderOmnibox.sys.mjs
source-hash: 03bef140a3a6f171d0a03381ccb7b396c66c96a7
lines: 183

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderOmnibox.constructor()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderOmnibox.type()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderOmnibox.isActive()
- 位置: async L52-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.substringAfter()`, `lazy.ExtensionSearchHandler.hasActiveInputSession()`, `lazy.ExtensionSearchHandler.isKeywordRegistered()`, `queryContext.restrictInSearchMode()`
- 条件付き依存: `if (lazy.ExtensionSearchHandler.hasActiveInputSession())` → `lazy.ExtensionSearchHandler.handleInputCancelled()`
- 参照: `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0].value`, `queryContext.tokens[0].value.length`

## UrlbarProviderOmnibox.getPriority()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderOmnibox.startQuery()
- 位置: async L96-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `Promise.race([timeoutPromise, resultsPromise]).catch()`, `addCallback()`, `lazy.ExtensionSearchHandler.getDescription()`, `lazy.ExtensionSearchHandler.handleSearch()`, `lazy.UrlbarPrefs.get()`, `this.logger.error()`
- 参照: `heuristicResult.payload.content`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.ICON.EXTENSION`, `lazy.UrlbarShared.RESULT_SOURCE.ADDON`, `lazy.UrlbarShared.RESULT_TYPE.OMNIBOX`, `queryContext.isPrivate`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0].value`, `suggestion.content`, `suggestion.deletable`, `suggestion.description`, `this.logger`, `this.queryInstance`

## UrlbarProviderOmnibox.onEngagement()
- 位置: L175-181
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `lazy.ExtensionSearchHandler.handleInputDeleted()`
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `controller.removeResult()`
- 参照: `details.selType`, `result.payload.isBlockable`, `result.payload.title`
