# browser/extensions/search-detection/extension/background.js

source: browser/extensions/search-detection/extension/background.js
source-hash: 323391eb60d7d5f6fe3026f569fd5cef1583c73b
lines: 152

## <module>
- 役割: (未記入)
- 呼び出し先: `browser.addonsSearchDetection.onSearchEngineModified.addListener()`, `exp.monitor()`

## AddonsSearchDetection.constructor()
- 位置: L14-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onRedirectedListener.bind()`
- 参照: `this.engines`, `this.onRedirectedListener`

## AddonsSearchDetection.getEngines()
- 位置: async L21-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addonsSearchDetection.getEngines()`, `console.error()`
- 参照: `this.engines`

## AddonsSearchDetection.monitor()
- 位置: async L35-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addonsSearchDetection.onRedirected.addListener()`, `browser.addonsSearchDetection.onRedirected.hasListener()`, `engines.map()`, `this.getEngines()`
- 条件付き依存: `if ( browser.addonsSearchDetection.onRedirected.hasListener( this.onRedirectedListener ) )` → `browser.addonsSearchDetection.onRedirected.removeListener()`
- 参照: `e.baseUrl`, `patterns.size`, `this.onRedirectedListener`

## AddonsSearchDetection.onRedirectedListener()
- 位置: async L66-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addonsSearchDetection.getAddonVersion()`, `browser.addonsSearchDetection.getPublicSuffix()`, `this.getEnginesForUrl()`
- 条件付き依存: `if (maybeServerSideRedirect)` → `engines.filter(e => e.addonId).map()`
- 条件付き依存: `if (maybeServerSideRedirect)` → `engines.filter()`
- 条件付き依存: `if (sameSite)` → `engines.filter()`
- 条件付き依存: `if (sameSite)` → `firstParams.get()`
- 条件付き依存: `if (sameSite)` → `lastParams.get()`
- 条件付き依存: `if (sameSite)` → `browser.addonsSearchDetection.reportSameSiteRedirect()`
- 条件付き依存: `if (maybeServerSideRedirect)` → `browser.addonsSearchDetection.reportETLDChangeOther()`
- 条件付き依存: `if (!(maybeServerSideRedirect))` → `browser.addonsSearchDetection.reportETLDChangeWebrequest()`
- 参照: `addonIds.length`, `e.addonId`, `e.paramName`, `new URL(firstUrl).search`, `new URL(lastUrl).search`

## AddonsSearchDetection.getEnginesForUrl()
- 位置: L141-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engines.filter()`, `url.startsWith()`
- 参照: `e.baseUrl`
