# browser/components/urlbar/UrlbarProviderRestrictKeywords.sys.mjs

source: browser/components/urlbar/UrlbarProviderRestrictKeywords.sys.mjs
source-hash: 0a2e587c82301ecfc73c1a3a1f95329d67262502
lines: 91

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderRestrictKeywords.constructor()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderRestrictKeywords.type()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderRestrictKeywords.getPriority()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderRestrictKeywords.isActive()
- 位置: async L42-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.getScotchBonnetPref()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.trimmedSearchString`

## UrlbarProviderRestrictKeywords.startQuery()
- 位置: async L60-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find()`, `lazy.UrlbarTokenizer.getL10nRestrictKeywords()`, `tokenToKeyword.entries()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find( mode => mode.restrict == token )?.icon`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `mode.restrict`, `this.queryInstance`
