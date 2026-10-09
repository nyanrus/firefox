# browser/components/urlbar/content/UrlbarQueryContext.mjs

source: browser/components/urlbar/content/UrlbarQueryContext.mjs
source-hash: 1cb514a3074bc37972753505c1ad5a7eadf489c7
lines: 516

## <module>
- 役割: (未記入)

## UrlbarQueryContext.constructor()
- 位置: L69-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `UrlbarShared.normalizedUserContextId()`, `isNaN()`, `structuredClone()`, `this._checkRequiredOptions()`, `this.searchString.toLowerCase()`, `this.searchString.trim()`, `this.trimmedSearchString.toLowerCase()`
- 条件付き依存: `if (prop in options)` → `checkFn()`
- 参照: `options.maxResults`, `options.tabGroup`, `options.userContextId`, `this.deferUserSelectionProviders`, `this.firstTimerId`, `this.id`, `this.isPrivate`, `this.lastResultCount`, `this.lowerCaseSearchString`, `this.pendingHeuristicProviders`, `this.sixthTimerId`, `this.tabGroup`, `this.trimmedLowerCaseSearchString`, `this.trimmedSearchString`, `this.userContextId`, `v.length`

## UrlbarQueryContext.isSearchbarSAP()
- 位置: L265-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isSearchbarSAP()`
- 参照: `this.sapName`

## UrlbarQueryContext.keywordEnabled()
- 位置: L276-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.keywordEnabled()`
- 参照: `this.sapName`

## UrlbarQueryContext.navigationEnabled()
- 位置: L287-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.navigationEnabled()`
- 参照: `this.sapName`

## UrlbarQueryContext.navigationInSearchModeEnabled()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.navigationInSearchModeEnabled()`
- 参照: `this.sapName`

## UrlbarQueryContext.restrictInSearchMode()
- 位置: L318-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `this.searchMode`, `this.searchMode.engineName`

## UrlbarQueryContext._checkRequiredOptions()
- 位置: L351-360
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarQueryContext.fixupInfo()
- 位置: L370-396
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._fixupError && !this._fixupInfo && this.trimmedSearchString)` → `Services.uriFixup.getFixupURIInfo()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_FORCE_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `ex.result`, `info.fixedURI.scheme`, `info.fixedURI.spec`, `info.keywordAsSent`, `this._fixupError`, `this._fixupInfo`, `this.isPrivate`, `this.isSearchbarSAP`, `this.searchString`, `this.trimmedSearchString`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## UrlbarQueryContext.fixupError()
- 位置: L405-411
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._fixupError`, `this.fixupInfo`

## UrlbarQueryContext.allowRemoteResults()
- 位置: L426-468
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.TOKEN_TYPE.POSSIBLE_ORIGIN`, `UrlbarShared.TOKEN_TYPE.POSSIBLE_ORIGIN_BUT_SEARCH_ALLOWED`, `searchString.length`, `this.fixupInfo?.href`, `this.fixupInfo?.isSearch`, `this.navigationEnabled`, `this.prohibitRemoteResults`, `this.searchString`, `this.tokens`, `this.tokens.length`, `this.tokens[0].type`

## UrlbarQueryContext.toWire()
- 位置: L478-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.toWire()`, `this.heuristicResult?.toWire()`, `this.results?.map()`

## UrlbarQueryContext.fromWire()
- 位置: L496-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.setPrototypeOf()`, `UrlbarResult.fromWire()`, `wire.results?.map()`
- 条件付き依存: `if (wire.heuristicResult)` → `UrlbarResult.fromWire()`
- 参照: `UrlbarQueryContext.prototype`, `wire.heuristicResult`, `wire.results`
