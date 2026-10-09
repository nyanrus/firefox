# browser/components/urlbar/UrlbarTokenizer.sys.mjs

source: browser/components/urlbar/UrlbarTokenizer.sys.mjs
source-hash: d63efa5fda95b5855484e8975a03fd3425cfe399
lines: 306

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.entries()`, `Object.entries(UrlbarShared.RESTRICT_TOKENS).map()`, `UrlbarShared.getLogger()`

## loadL10nRestrictKeywords()
- 位置: async L52-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.map()`, `UrlbarShared.getResultSourceName()`, `englishKeywords.shift()`, `englishSearchStrings.formatValues()`, `l10nKeywords.shift()`, `lazy.gFluentStrings.formatValues()`, `tokenToKeywords.set()`
- 参照: `UrlbarShared.LOCAL_SEARCH_MODES`, `mode.source`

## getL10nRestrictKeywords()
- 位置: async L84-90
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tokenToKeywords.size === 0)` → `this.loadL10nRestrictKeywords()`
- 参照: `tokenToKeywords.size`

## tokenize()
- 位置: L102-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filterTokens()`, `lazy.logger.debug()`, `splitString()`
- 参照: `context.searchString`, `context.trimmedSearchString`

## isRestrictionToken()
- 位置: L120-126
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY`, `UrlbarShared.TOKEN_TYPE.RESTRICT_URL`, `token.type`

## splitString()
- 位置: L145-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CHAR_TO_TYPE_MAP.has()`, `Object.values()`, `Object.values(UrlbarShared.RESTRICT_TOKENS).includes()`, `lazy.PlacesUtils.keywords.isKeywordFromCache()`, `lazy.UrlUtils.REGEXP_PERCENT_ENCODED_START.test()`, `searchString.trim()`, `tokens.some()`, `trimmed.startsWith()`
- 条件付き依存: `if (trimmed.length < 500)` → `trimmed.split()`
- 条件付き依存: `if (!(trimmed.length < 500))` → `trimmed.substring(0, 500).split()`
- 条件付き依存: `if (!(trimmed.length < 500))` → `trimmed.substring()`
- 条件付き依存: `if ( CHAR_TO_TYPE_MAP.has(firstToken[0]) && !lazy.UrlUtils.REGEXP_PERCENT_ENCODED_START.test(firstToken) && !searchMode )` → `firstToken.substring()`
- 条件付き依存: `if ( CHAR_TO_TYPE_MAP.has(firstToken[0]) && !lazy.UrlUtils.REGEXP_PERCENT_ENCODED_START.test(firstToken) && !searchMode )` → `tokens.splice()`
- 参照: `UrlbarShared.RESTRICT_TOKENS`, `lazy.UrlUtils.REGEXP_SPACES`, `tokens.length`, `trimmed.length`

## filterTokens()
- 位置: L212-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CHAR_TO_TYPE_MAP.get()`, `Object.values()`, `Object.values(UrlbarShared.RESTRICT_TOKENS).includes()`, `filtered.push()`, `lazy.PlacesUtils.keywords.isKeywordFromCache()`, `lazy.logger.info()`, `token.toLocaleLowerCase()`
- 条件付き依存: `if (tokens.length > 1 && token.length > 500)` → `filtered.push()`
- 条件付き依存: `if (isFirstTokenAKeyword)` → `filtered.push()`
- 条件付き依存: `if (restrictionType)` → `restrictions.push()`
- 条件付き依存: `if (!(restrictionType))` → `lazy.UrlUtils.looksLikeOrigin()`
- 条件付き依存: `if (!(restrictionType))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(looksLikeOrigin != lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE))` → `lazy.UrlUtils.looksLikeUrl()`
- 条件付き依存: `if (restrictions.length)` → `assignRestriction()`
- 条件付き依存: `if (restrictions.length)` → `restrictions.find()`
- 条件付き依存: `if (found)` → `assignRestriction()`
- 条件付き依存: `if (found)` → `restrictions.find()`
- 参照: `UrlbarShared.RESTRICT_TOKENS`, `UrlbarShared.TOKEN_TYPE.POSSIBLE_ORIGIN`, `UrlbarShared.TOKEN_TYPE.POSSIBLE_ORIGIN_BUT_SEARCH_ALLOWED`, `UrlbarShared.TOKEN_TYPE.POSSIBLE_URL`, `UrlbarShared.TOKEN_TYPE.TEXT`, `lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE`, `lazy.UrlUtils.LOOKS_LIKE_ORIGIN.OTHER`, `r.index`, `restrictions.length`, `token.length`, `tokenObj.type`, `tokens.length`

## assignRestriction()
- 位置: L266-286
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (r && !(matchingRestrictionFound && typeRestrictionFound))` → `[ UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE, UrlbarShared.TOKEN_TYPE.RESTRICT_URL, ].includes()`
- 参照: `UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `UrlbarShared.TOKEN_TYPE.RESTRICT_URL`, `filtered[r.index].type`, `r.index`, `r.type`
