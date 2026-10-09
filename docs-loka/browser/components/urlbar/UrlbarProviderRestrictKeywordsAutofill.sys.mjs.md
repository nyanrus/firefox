# browser/components/urlbar/UrlbarProviderRestrictKeywordsAutofill.sys.mjs

source: browser/components/urlbar/UrlbarProviderRestrictKeywordsAutofill.sys.mjs
source-hash: 8558c84fda435d2abf23a760e15331ab54327879
lines: 216

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderRestrictKeywordsAutofill.constructor()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderRestrictKeywordsAutofill.type()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderRestrictKeywordsAutofill.getPriority()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProviderRestrictKeywordsAutofill.#getLowerCaseTokenToKeywords()
- 位置: async L46-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...tokenToKeywords].map()`, `keyword.toLowerCase()`, `keywords.map()`, `lazy.UrlbarTokenizer.getL10nRestrictKeywords()`
- 参照: `this.#lowerCaseTokenToKeywords`

## UrlbarProviderRestrictKeywordsAutofill.#getKeywordAliases()
- 位置: async L59-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(await this.#lowerCaseTokenToKeywords.values()) .flat()`, `Array.from(await this.#lowerCaseTokenToKeywords.values()) .flat() .map()`, `this.#lowerCaseTokenToKeywords.values()`

## UrlbarProviderRestrictKeywordsAutofill.isActive()
- 位置: async L65-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keyword.startsWith()`, `keywordAliases.some()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`, `queryContext.restrictInSearchMode()`, `queryContext.searchString.startsWith()`, `this.#getKeywordAliases()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("autoFill") && queryContext.allowAutofill)` → `this.#getAutofillResult()`
- 参照: `queryContext.allowAutofill`, `queryContext.restrictSource`, `queryContext.searchString.length`, `queryContext.tokens.length`, `queryContext.trimmedLowerCaseSearchString`, `this.#autofillData`, `this.queryInstance`

## UrlbarProviderRestrictKeywordsAutofill.startQuery()
- 位置: async L114-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keywords.includes()`, `queryContext.trimmedLowerCaseSearchString.substring()`, `this.#getLowerCaseTokenToKeywords()`
- 条件付き依存: `if ( this.#autofillData && this.#autofillData.instance == this.queryInstance )` → `addCallback()`
- 条件付き依存: `if (restrictSymbol && typedKeyword == aliasKeyword)` → `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `queryContext.lowerCaseSearchString`, `this.#autofillData`, `this.#autofillData.instance`, `this.#autofillData.result`, `this.queryInstance`

## UrlbarProviderRestrictKeywordsAutofill.cancelQuery()
- 位置: L161-165
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#autofillData`, `this.#autofillData?.instance`, `this.queryInstance`

## UrlbarProviderRestrictKeywordsAutofill.#getAutofillResult()
- 位置: async L167-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...l10nRestrictKeywords].map()`, `keyword.startsWith()`, `keywords.find()`, `this.#getLowerCaseTokenToKeywords()`, `tokenToKeywords.entries()`
- 条件付き依存: `if (autofillKeyword)` → `autofillKeyword.substr()`
- 条件付き依存: `if (autofillKeyword)` → `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find( mode => mode.restrict == token )?.icon`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `mode.restrict`, `queryContext.searchString`, `queryContext.searchString.length`, `value.length`
