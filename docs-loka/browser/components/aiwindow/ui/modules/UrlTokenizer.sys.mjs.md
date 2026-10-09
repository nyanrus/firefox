# browser/components/aiwindow/ui/modules/UrlTokenizer.sys.mjs

source: browser/components/aiwindow/ui/modules/UrlTokenizer.sys.mjs
source-hash: 09b1c3437aa6203470878283bb541be8c39e5ab1
lines: 227

## <module>
- 役割: (未記入)

## UrlTokenizer.constructor()
- 位置: L64-67
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tokenToUrl`, `this.urlToToken`

## UrlTokenizer.encodeToken()
- 位置: L81-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `this.#baseTokenCounts.get()`, `this.#baseTokenCounts.set()`, `this.tokenToUrl.set()`, `this.urlToToken.get()`, `this.urlToToken.set()`
- 条件付き依存: `if (parsedUrl.protocol !== "http:" && parsedUrl.protocol !== "https:")` → `parsedUrl.protocol.toUpperCase().replace()`
- 条件付き依存: `if (parsedUrl.protocol !== "http:" && parsedUrl.protocol !== "https:")` → `parsedUrl.protocol.toUpperCase()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace(/^www\./, "") .toUpperCase() .replace(/[.\-]/g, "_") .substring()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace(/^www\./, "") .toUpperCase() .replace()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace(/^www\./, "") .toUpperCase()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.pathname.split()`
- 条件付き依存: `if (parsedUrl)` → `part.toUpperCase().replace()`
- 条件付き依存: `if (parsedUrl)` → `part.toUpperCase()`
- 参照: `nextToken.length`, `parsedUrl.protocol`

## UrlTokenizer.formatToken()
- 位置: L147-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.encodeToken()`

## UrlTokenizer.tokenizeText()
- 位置: L159-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `match.indexOf()`, `match.replace()`, `match.slice()`, `text.replace()`, `this.formatToken()`, `url.split()`
- 参照: `url.length`, `url.split("(").length`, `url.split(")").length`

## UrlTokenizer.resolveExactToken()
- 位置: L194-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tokenToUrl.get()`, `value.trim()`, `value.trim().match()`

## expandUrlTokens()
- 位置: L211-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.replace()`, `tokenToUrl.get()`

## stripUnresolvedUrlTokens()
- 位置: L224-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.replace()`
