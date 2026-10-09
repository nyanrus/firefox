# browser/components/urlbar/UrlbarProviderAliasEngines.sys.mjs

source: browser/components/urlbar/UrlbarProviderAliasEngines.sys.mjs
source-hash: e7ebfcac125066fb15997c7993c292dfffe5c139
lines: 93

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderAliasEngines.type()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderAliasEngines.isActive()
- 位置: async L42-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.restrictInSearchMode()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.restrictSource`, `queryContext.tokens.length`

## UrlbarProviderAliasEngines.startQuery()
- 位置: async L60-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `UrlbarUtils.substringAfter()`, `UrlbarUtils.substringAfter( queryContext.searchString, alias ).trimStart()`, `addCallback()`, `lazy.UrlbarSearchUtils.engineForAlias()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0]?.value`, `this.queryInstance`
