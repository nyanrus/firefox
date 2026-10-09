# browser/components/urlbar/UrlbarProviderTabToSearch.sys.mjs

source: browser/components/urlbar/UrlbarProviderTabToSearch.sys.mjs
source-hash: 68d96a8de2703d91b1e23cdd2c4184b552f307fc
lines: 383

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderTabToSearch.constructor()
- 位置: L99-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderTabToSearch.type()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderTabToSearch.isActive()
- 位置: async L117-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ActionsProviderContextualSearch.isActive()`, `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`, `this.queryInstance .getProvider()`, `this.queryInstance .getProvider(lazy.UrlbarProviderGlobalActions.name) ?.isActive()`
- 参照: `lazy.UrlbarProviderGlobalActions.name`, `queryContext.searchString`, `queryContext.tokens.length`

## UrlbarProviderTabToSearch.getPriority()
- 位置: L137-139
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderTabToSearch.getViewTemplate()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderTabToSearch.getViewUpdate()
- 位置: L151-182
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.engine`, `result.payload.icon`, `result.payload.isGeneralPurposeEngine`

## UrlbarProviderTabToSearch.onSelection()
- 位置: L193-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if ( result.payload.dynamicType && (!UrlbarProviderTabToSearch.onboardingInteractionAtTime || UrlbarProviderTabToSearch.onboardingInteractionAtTime < Date.now() ...)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (interactionsLeft > 0)` → `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if ( result.payload.dynamicType && (!UrlbarProviderTabToSearch.onboardingInteractionAtTime || UrlbarProviderTabToSearch.onboardingInteractionAtTime < Date.now() ...)` → `Date.now()`
- 参照: `UrlbarProviderTabToSearch.onboardingInteractionAtTime`, `result.payload.dynamicType`

## UrlbarProviderTabToSearch.deferUserSelection()
- 位置: L228-230
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderTabToSearch.startQuery()
- 位置: async L239-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `baseDomain.startsWith()`, `host.includes()`, `host.startsWith()`, `lazy.UrlUtils.looksLikeOrigin()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarSearchUtils.enginesForDomainPrefix()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `searchStr.includes()`, `searchStr.toLocaleLowerCase()`
- 条件付き依存: `if (searchStr.includes("."))` → `UrlbarUtils.stripPublicSuffixFromHost()`
- 条件付き依存: `if (onboardingInteractionsLeft > 0)` → `addCallback()`
- 条件付き依存: `if (onboardingInteractionsLeft > 0)` → `makeOnboardingResult()`
- 条件付き依存: `if (!(onboardingInteractionsLeft > 0))` → `addCallback()`
- 条件付き依存: `if (!(onboardingInteractionsLeft > 0))` → `makeResult()`
- 条件付き依存: `if (host.includes("." + searchStr.toLocaleLowerCase()))` → `partialMatchEnginesByHost.set()`
- 条件付き依存: `if (baseDomain.startsWith(searchStr))` → `partialMatchEnginesByHost.set()`
- 条件付き依存: `if (partialMatchEnginesByHost.size)` → `lazy.UrlbarProviderAutofill.getTopHostOverThreshold()`
- 条件付き依存: `if (partialMatchEnginesByHost.size)` → `Array.from()`
- 条件付き依存: `if (partialMatchEnginesByHost.size)` → `partialMatchEnginesByHost.keys()`
- 条件付き依存: `if (host)` → `partialMatchEnginesByHost.get()`
- 参照: `engine.searchUrlDomain`, `engines.length`, `partialMatchEnginesByHost.size`, `queryContext.searchString`
- XPCOM: `Services.eTLD`

## makeOnboardingResult()
- 位置: L343-358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchUrlDomainWithoutSuffix()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.ICON.SEARCH_GLASS`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`

## makeResult()
- 位置: L360-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchUrlDomainWithoutSuffix()`
- 参照: `engine.isGeneralPurposeEngine`, `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.ICON.SEARCH_GLASS`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`

## searchUrlDomainWithoutSuffix()
- 位置: L377-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`, `value.substr()`
- 参照: `engine.searchUrlDomain`, `engine.searchUrlPublicSuffix.length`, `value.length`
