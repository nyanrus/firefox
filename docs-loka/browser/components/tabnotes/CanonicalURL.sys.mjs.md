# browser/components/tabnotes/CanonicalURL.sys.mjs

source: browser/components/tabnotes/CanonicalURL.sys.mjs
source-hash: 1dea36335c675592fcfab6d41b09dd5897959133
lines: 127

## <module>
- 役割: (未記入)

## findCandidates()
- 位置: L13-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getFallbackCanonicalUrl()`, `getJSONLDUrl()`, `getLinkRelCanonical()`, `getOpenGraphUrl()`

## pickCanonicalUrl()
- 位置: L29-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sources.fallback`, `sources.jsonLd`, `sources.link`, `sources.opengraph`

## getLinkRelCanonical()
- 位置: L44-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelector()`, `document .querySelector('link[rel="canonical"]') ?.getAttribute()`, `parseUrl()`

## getOpenGraphUrl()
- 位置: L58-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelector()`, `document .querySelector('meta[property="og:url"]') ?.getAttribute()`, `parseUrl()`

## getJSONLDUrl()
- 位置: L75-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from( document.querySelectorAll('script[type="application/ld+json"]') ) .map()`, `JSON.parse()`, `document.querySelectorAll()`, `parseUrl()`
- 参照: `firstMatch?.url`, `obj.url`, `script.textContent`

## getFallbackCanonicalUrl()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cleanNoncanonicalUrl()`
- 参照: `document.documentURI`

## cleanNoncanonicalUrl()
- 位置: L104-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 条件付き依存: `if (parsed)` → `[parsed.origin, parsed.pathname, parsed.search].join()`
- 参照: `parsed.origin`, `parsed.pathname`, `parsed.search`

## parseUrl()
- 位置: L117-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `URL.parse(urlString, document.documentURI)?.toString()`
- 参照: `document.documentURI`
