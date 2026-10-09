# browser/components/asrouter/modules/PinnableSitesProvider.sys.mjs

source: browser/components/asrouter/modules/PinnableSitesProvider.sys.mjs
source-hash: d52b8db85b19160962dce13855859482394d3df3
lines: 271

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## normalizeHost()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `host.replace()`, `host.replace(/^www\./i, "").toLowerCase()`

## getExcludedHosts()
- 位置: async L44-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addHost()`, `console.error()`, `lazy.HomePage.get()`, `lazy.HomePage.get().split()`, `lazy.SearchService.getVisibleEngines()`
- 条件付き依存: `if (engine.searchUrlDomain)` → `excluded.add()`
- 条件付き依存: `if (engine.searchUrlDomain)` → `normalizeHost()`
- 参照: `engine.searchUrlDomain`, `lazy.AboutNewTab.newTabURL`

## addHost()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 条件付き依存: `if (host)` → `excluded.add()`
- 条件付き依存: `if (host)` → `normalizeHost()`
- 参照: `URL.parse(url)?.hostname`

## isAlreadyPinned()
- 位置: async L77-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.TaskbarTabs.findTaskbarTab()`, `normalizeHost()`, `uri .mutate()`, `uri .mutate() .setHost()`, `uri .mutate() .setHost(variant) .finalize()`, `uri .mutate() .setHost(variant) .finalize() .QueryInterface()`
- 参照: `Ci.nsIURL`, `uri.host`
- XPCOM: [`nsIURL`](../../../../netwerk/base/nsIURL.idl.md) / `Services.io`

## hasIcon()
- 位置: async L100-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`
- XPCOM: `Services.io`

## getPersonalizedSites()
- 位置: async L111-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `byHost.get()`, `candidates.sort()`, `excludedHosts.has()`, `getExcludedHosts()`, `hasIcon()`, `isAlreadyPinned()`, `lazy.FilterAdult.filter()`, `lazy.NewTabUtils.activityStreamProvider.getTopFrecentSites()`, `lazy.PlacesUtils.history.pageFrecencyThreshold()`, `lazy.generateName()`, `normalizeHost()`, `sites.map()`
- 条件付き依存: `if (!entry)` → `byHost.set()`
- 条件付き依存: `if (!excludedHosts.has(host))` → `candidates.push()`
- 条件付き依存: `if ( !(await isAlreadyPinned(entry.origin)) && (await hasIcon(entry.origin)) )` → `sites.push()`
- 参照: `a.score`, `b.score`, `entry.origin`, `entry.score`, `page.frecency`, `page.url`, `sites.length`, `uri.host`, `uri.prePath`, `uri.scheme`
- XPCOM: `Services.eTLD` / `Services.io`

## personalizedTiles()
- 位置: L191-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `content?.screens`, `screen?.content?.tiles`, `tile.source`, `tile?.type`

## populateTile()
- 位置: async L214-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `console.error()`, `getPersonalizedSites()`
- 条件付き依存: `if (tile.backfill !== false && sites.length < slots)` → `sites.map()`
- 条件付き依存: `if (tile.backfill !== false && sites.length < slots)` → `URL.parse()`
- 条件付き依存: `if (tile.backfill !== false && sites.length < slots)` → `taken.has()`
- 条件付き依存: `if (tile.backfill !== false && sites.length < slots)` → `isAlreadyPinned()`
- 条件付き依存: `if (tile.backfill !== false && sites.length < slots)` → `taken.add()`
- 条件付き依存: `if (tile.backfill !== false && sites.length < slots)` → `sites.push()`
- 参照: `URL.parse(item.url)?.origin`, `item.url`, `site.url`, `sites.length`, `tile.backfill`, `tile.data`, `tile.minPersonalized`, `tile.slots`

## hasPersonalizedTile()
- 位置: L253-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `personalizedTiles()`, `personalizedTiles(content).next()`
- 参照: `personalizedTiles(content).next().done`

## populate()
- 位置: async L262-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `personalizedTiles()`, `populateTile()`
