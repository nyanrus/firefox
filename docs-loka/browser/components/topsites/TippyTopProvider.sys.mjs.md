# browser/components/topsites/TippyTopProvider.sys.mjs

source: browser/components/topsites/TippyTopProvider.sys.mjs
source-hash: 553d034e68e2ca72dcea608b04c076364b81f93b
lines: 69

## <module>
- 役割: (未記入)

## getDomain()
- 位置: L12-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 条件付き依存: `if (strip === "*")` → `Services.eTLD.getBaseDomainFromHost()`
- 条件付き依存: `if (!(strip === "*"))` → `domain.startsWith()`
- 条件付き依存: `if (domain.startsWith(strip))` → `domain.slice()`
- 参照: `URL.parse(url)?.hostname`, `strip.length`
- XPCOM: `Services.eTLD`

## TippyTopProvider.constructor()
- 位置: L28-31
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._sitesByDomain`, `this.initialized`

## TippyTopProvider.init()
- 位置: async L33-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `await()`, `await ( await this.fetch(TIPPYTOP_JSON_PATH, { credentials: "omit", }) ).json()`, `console.error()`, `this._sitesByDomain.set()`, `this.fetch()`
- 参照: `site.domains`, `this.initialized`

## TippyTopProvider.processSite()
- 位置: L51-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getDomain()`, `this._sitesByDomain.get()`
- 参照: `site.backgroundColor`, `site.smallFavicon`, `site.tippyTopIcon`, `site.url`, `tippyTop.background_color`, `tippyTop.favicon_url`, `tippyTop.image_url`

## TippyTopProvider.fetch()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`
