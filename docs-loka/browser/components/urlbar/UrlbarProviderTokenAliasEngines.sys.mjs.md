# browser/components/urlbar/UrlbarProviderTokenAliasEngines.sys.mjs

source: browser/components/urlbar/UrlbarProviderTokenAliasEngines.sys.mjs
source-hash: 2f2b35301b26fa4fdcc88fc369c9377ea76314a8
lines: 232

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderTokenAliasEngines.constructor()
- 位置: L29-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._engines`

## UrlbarProviderTokenAliasEngines.type()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderTokenAliasEngines.PRIORITY()
- 位置: L41-44
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderTokenAliasEngines.isActive()
- 位置: async L54-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarSearchUtils.tokenAliasEngines()`, `queryContext.restrictInSearchMode()`, `queryContext.searchString.startsWith()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("autoFill") && queryContext.allowAutofill)` → `this._getAutofillResult()`
- 参照: `queryContext.allowAutofill`, `queryContext.tokens.length`, `queryContext.trimmedSearchString`, `this._autofillData`, `this._engines`, `this._engines.length`, `this.queryInstance`

## UrlbarProviderTokenAliasEngines.startQuery()
- 位置: async L110-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tokenAliases[0].startsWith()`
- 条件付き依存: `if ( this._autofillData && this._autofillData.instance == this.queryInstance )` → `addCallback()`
- 条件付き依存: `if ( tokenAliases[0].startsWith(queryContext.trimmedSearchString) && engine.name != this._autofillData?.result.payload.engine )` → `tokenAliases.join()`
- 条件付き依存: `if ( tokenAliases[0].startsWith(queryContext.trimmedSearchString) && engine.name != this._autofillData?.result.payload.engine )` → `UrlbarUtils.getEngineIconUrl()`
- 条件付き依存: `if ( tokenAliases[0].startsWith(queryContext.trimmedSearchString) && engine.name != this._autofillData?.result.payload.engine )` → `addCallback()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.trimmedSearchString`, `this._autofillData`, `this._autofillData.instance`, `this._autofillData.result`, `this._autofillData?.result.payload.engine`, `this._engines`, `this._engines.length`, `this.queryInstance`

## UrlbarProviderTokenAliasEngines.getPriority()
- 位置: L160-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarProviderTokenAliasEngines.PRIORITY`

## UrlbarProviderTokenAliasEngines.cancelQuery()
- 位置: L167-171
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._autofillData`, `this._autofillData?.instance`, `this.queryInstance`

## UrlbarProviderTokenAliasEngines._getAutofillResult()
- 位置: async L173-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alias.startsWith()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `lowerCaseSearchString.startsWith()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `lazy.UrlUtils.REGEXP_SPACES_START.test()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `lowerCaseSearchString.substring()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `alias.substr()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `tokenAliases.join()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `UrlbarUtils.getEngineIconUrl()`
- 参照: `alias.length`, `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.searchString`, `queryContext.searchString.length`, `this._engines`, `value.length`
