# browser/components/urlbar/UrlbarTokenizer.sys.mjs

source: browser/components/urlbar/UrlbarTokenizer.sys.mjs
source-hash: d63efa5fda95b5855484e8975a03fd3425cfe399
lines: 306

## <module>
- 役割: urlbar の検索文字列を、空白区切りのトークンに分け、制限トークン(@ や * など)を種類付きのトークンに変換する関数群を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.entries()`, `Object.entries(UrlbarShared.RESTRICT_TOKENS).map()`, `UrlbarShared.getLogger()`

## loadL10nRestrictKeywords()
- 位置: async L52-78
- 役割: 各検索モードについて、ローカライズ済みのキーワードと英語のキーワードを集め、重複を除いて制限記号ごとに保存する。
- 触るとき: 制限キーワードの翻訳や追加のキーワードの扱いを変えるとき見る。保存先は tokenToKeywords の Map である。
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.map()`, `UrlbarShared.getResultSourceName()`, `englishKeywords.shift()`, `englishSearchStrings.formatValues()`, `l10nKeywords.shift()`, `lazy.gFluentStrings.formatValues()`, `tokenToKeywords.set()`
- 参照: `UrlbarShared.LOCAL_SEARCH_MODES`, `mode.source`

## getL10nRestrictKeywords()
- 位置: async L84-90
- 役割: キーワードの Map が空なら読み込みを行い、キャッシュ済みの Map を返す。
- 触るとき: 制限キーワードが候補に出ない原因が読み込み前の状態にあるかを調べるとき見る。
- 条件付き依存: `if (tokenToKeywords.size === 0)` → `this.loadL10nRestrictKeywords()`
- 参照: `tokenToKeywords.size`

## tokenize()
- 位置: L102-111
- 役割: 空でない検索文字列を splitString で分割し、その後 filterTokens で種類を付けた配列を返す。
- 触るとき: トークン化の全体の流れを変えるとき、または入力がどう分割されるかを調べるとき見る。
- 呼び出し先: `filterTokens()`, `lazy.logger.debug()`, `splitString()`
- 参照: `context.searchString`, `context.trimmedSearchString`

## isRestrictionToken()
- 位置: L120-126
- 役割: トークンの種類が RESTRICT_HISTORY から RESTRICT_URL の範囲にあれば true を返す。
- 触るとき: 制限トークンかどうかを判定する箇所の範囲を変えるとき見る。新しい制限の種類を足すときは種類の並びに注意する。
- 参照: `UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY`, `UrlbarShared.TOKEN_TYPE.RESTRICT_URL`, `token.type`

## splitString()
- 位置: L145-198
- 役割: 空白で分割する。長さ 500 以上は先頭 500 字だけ分割し残りを最後のトークンに付ける。data: で始まるものは分割せず、先頭や末尾の制限記号は必要なら独立したトークンとして切り出す。
- 触るとき: 入力を空白でどう区切るか、長い入力や data: URL をどう扱うかを変えるとき見る。制限記号が隣接する場合の切り出しもここで行われる。
- 呼び出し先: `CHAR_TO_TYPE_MAP.has()`, `Object.values()`, `Object.values(UrlbarShared.RESTRICT_TOKENS).includes()`, `lazy.PlacesUtils.keywords.isKeywordFromCache()`, `lazy.UrlUtils.REGEXP_PERCENT_ENCODED_START.test()`, `searchString.trim()`, `tokens.some()`, `trimmed.startsWith()`
- 条件付き依存: `if (trimmed.length < 500)` → `trimmed.split()`
- 条件付き依存: `if (!(trimmed.length < 500))` → `trimmed.substring(0, 500).split()`
- 条件付き依存: `if (!(trimmed.length < 500))` → `trimmed.substring()`
- 条件付き依存: `if ( CHAR_TO_TYPE_MAP.has(firstToken[0]) && !lazy.UrlUtils.REGEXP_PERCENT_ENCODED_START.test(firstToken) && !searchMode )` → `firstToken.substring()`
- 条件付き依存: `if ( CHAR_TO_TYPE_MAP.has(firstToken[0]) && !lazy.UrlUtils.REGEXP_PERCENT_ENCODED_START.test(firstToken) && !searchMode )` → `tokens.splice()`
- 参照: `UrlbarShared.RESTRICT_TOKENS`, `lazy.UrlUtils.REGEXP_SPACES`, `tokens.length`, `trimmed.length`

## filterTokens()
- 位置: L212-305
- 役割: 各トークンに種類を付ける。制限記号は先頭と末尾だけ有効とし、URL や origin らしいトークンは対応する種類にする。最後に assignRestriction で制限を割り当てる。
- 触るとき: トークンの種類判定(origin、URL の候補、制限記号)を変えるとき見る。長さ 500 超のトークンを検索語として扱う理由もここにある。
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
- 役割: 制限の種類を一つずつ割り当て、一致の制限(title、url)と種類の制限をそれぞれ一つまでとする。割り当てたら true を返す。
- 触るとき: 同じ種類の制限が二つ付いたときの扱いを変えるとき見る。
- 条件付き依存: `if (r && !(matchingRestrictionFound && typeRestrictionFound))` → `[ UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE, UrlbarShared.TOKEN_TYPE.RESTRICT_URL, ].includes()`
- 参照: `UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `UrlbarShared.TOKEN_TYPE.RESTRICT_URL`, `filtered[r.index].type`, `r.index`, `r.type`
