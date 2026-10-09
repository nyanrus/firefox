# browser/components/urlbar/UrlbarSearchUtils.sys.mjs

source: browser/components/urlbar/UrlbarSearchUtils.sys.mjs
source-hash: 6dff789de49de7446db5dd1191b2dd39e5803f6e
lines: 490

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## SearchUtils.constructor()
- 位置: L44-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.resolve()`
- 参照: `this.QueryInterface`, `this._refreshEnginesByAliasPromise`

## SearchUtils.init()
- 位置: async L55-60
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initPromise)` → `this._initInternal()`
- 参照: `this._initPromise`

## SearchUtils.enginesForDomainPrefix()
- 位置: async L76-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `domain.startsWith()`, `engineSet.has()`, `lazy.SearchService.getVisibleEngines()`, `prefix.toLowerCase()`, `this.init()`
- 条件付き依存: `if (domain.startsWith(prefix) || domain.startsWith("www." + prefix))` → `perfectMatchEngines.push()`
- 条件付き依存: `if (domain.startsWith(prefix) || domain.startsWith("www." + prefix))` → `perfectMatchEngineSet.add()`
- 条件付き依存: `if (matchAllDomainLevels)` → `prefix.includes()`
- 条件付き依存: `if (prefix.includes("."))` → `matchPrefix()`
- 条件付き依存: `if (matchAllDomainLevels)` → `matchPrefix()`
- 条件付き依存: `if (matchAllDomainLevels)` → `domain.substr()`
- 条件付き依存: `if (!engineSet.has(engine))` → `engineSet.add()`
- 条件付き依存: `if (!engineSet.has(engine))` → `engines.push()`
- 参照: `domain.length`, `engine.hideOneOffButton`, `engine.searchUrlDomain`, `engine.searchUrlPublicSuffix.length`

## matchPrefix()
- 位置: L86-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engineHost.split()`, `parts.slice()`, `parts.slice(i).join()`, `parts.slice(i).join(".").startsWith()`
- 条件付き依存: `if (parts.slice(i).join(".").startsWith(prefix))` → `partialMatchEngines.push()`
- 参照: `parts.length`

## SearchUtils.engineForAlias()
- 位置: async L151-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `alias.toLocaleLowerCase()`, `this._enginesByAlias.get()`, `this.init()`
- 条件付き依存: `if (engine && searchString)` → `lazy.UrlbarUtils.substringAfter()`
- 条件付き依存: `if (engine && searchString)` → `lazy.UrlUtils.REGEXP_SPACES_START.test()`
- 参照: `this._refreshEnginesByAliasPromise`

## SearchUtils.tokenAliasEngines()
- 位置: async L174-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.startsWith()`, `lazy.SearchService.getVisibleEngines()`, `this.#orderEnginesForAliases()`, `this._aliasesForEngine()`, `this._aliasesForEngine(engine).filter()`, `this.init()`
- 条件付き依存: `if (tokenAliases.length)` → `tokenAliasEngines.push()`
- 参照: `tokenAliases.length`

## SearchUtils.getRootDomainFromEngine()
- 位置: L204-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `domain.split()`, `domain.substr()`, `domainParts.pop()`
- 条件付き依存: `if (!suffix)` → `domain.endsWith()`
- 参照: `domain.length`, `engine.searchUrlDomain`, `engine.searchUrlPublicSuffix`, `suffix.length`

## SearchUtils.getDefaultEngine()
- 位置: L229-239
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `lazy.separatePrivateDefault`, `lazy.separatePrivateDefaultUIEnabled`

## SearchUtils.separatePrivateDefaultUIEnabled()
- 位置: L245-247
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.separatePrivateDefaultUIEnabled`

## SearchUtils.separatePrivateDefault()
- 位置: L253-255
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.separatePrivateDefault`

## SearchUtils.getSearchModeScalarKey()
- 位置: L267-292
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (searchMode.engineName)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (!(!(engine instanceof lazy.ConfigSearchEngine)))` → `resultDomain.includes()`
- 条件付き依存: `if (!(resultDomain.includes("amazon.")))` → `resultDomain.endsWith()`
- 条件付き依存: `if (searchMode.source)` → `lazy.UrlbarShared.getResultSourceName()`
- 参照: `engine.searchUrlDomain`, `lazy.ConfigSearchEngine`, `searchMode.engineName`, `searchMode.restrictType`, `searchMode.source`

## SearchUtils.resultIsSERP()
- 位置: L305-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowedSources?.includes()`, `lazy.SearchService.parseSubmissionURL()`
- 参照: `lazy.SearchService.parseSubmissionURL(result.payload.url) ?.engine`, `result.payload.url`, `result.source`

## SearchUtils.resetInitPromiseForTests()
- 位置: L323-325
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._initPromise`

## SearchUtils._initInternal()
- 位置: async L327-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.SearchService.init()`, `this._refreshEnginesByAlias()`
- XPCOM: `Services.obs`

## SearchUtils.#orderEnginesForAliases()
- 位置: L349-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `orderedEngines.add()`, `orderedEngines.values()`
- 条件付き依存: `if (engine instanceof lazy.AppProvidedConfigEngine)` → `orderedEngines.add()`
- 参照: `lazy.AppProvidedConfigEngine`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`

## SearchUtils._refreshEnginesByAlias()
- 位置: async L374-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getVisibleEngines()`, `this.#addAliasesForEngine()`, `this.#orderEnginesForAliases()`
- 参照: `this._enginesByAlias`

## SearchUtils.#addAliasesForEngine()
- 位置: L393-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._aliasesForEngine()`, `this._enginesByAlias.getOrInsert()`

## SearchUtils.serpsAreEquivalent()
- 位置: L421-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(historyParams.entries()).every()`, `generatedParams.get()`, `historyParams.entries()`, `ignoreParams.includes()`
- 参照: `new URL(generatedSerp).searchParams`, `new URL(historySerp).searchParams`

## SearchUtils._aliasesForEngine()
- 位置: L449-459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alias.startsWith()`, `aliasWithCase.toLocaleLowerCase()`, `aliases.push()`, `engine.aliases.reduce()`
- 条件付き依存: `if (!alias.startsWith("@"))` → `aliases.push()`

## SearchUtils.getEngineByName()
- 位置: L468-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByName()`
- 参照: `lazy.SearchService.hasSuccessfullyInitialized`

## SearchUtils.observe()
- 位置: L476-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._refreshEnginesByAlias()`
- 参照: `this._refreshEnginesByAliasPromise`
