# browser/extensions/newtab/lib/SponsoredTopSitesScoreProvider/SponsoredTopSitesScoreProvider.mjs

source: browser/extensions/newtab/lib/SponsoredTopSitesScoreProvider/SponsoredTopSitesScoreProvider.mjs
source-hash: 45b8a554ea4cbe2bfa801f2ebeefa0e5a88d9d9f
lines: 219

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SponsoredTopSitesScoreProvider.constructor()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._getFlags`, `this._refreshTimer`, `this._rs`, `this._scores`

## SponsoredTopSitesScoreProvider.init()
- 位置: async L43-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._refreshScores()`
- 条件付き依存: `if (!this._rs)` → `lazy.RemoteSettings()`
- 条件付き依存: `if (!this._refreshTimer)` → `lazy.setInterval()`
- 条件付き依存: `if (!this._refreshTimer)` → `this._refreshScores()`
- 参照: `this._refreshTimer`, `this._rs`

## SponsoredTopSitesScoreProvider.uninit()
- 位置: L60-67
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._refreshTimer)` → `lazy.clearInterval()`
- 参照: `this._refreshTimer`, `this._rs`, `this._scores`

## SponsoredTopSitesScoreProvider._refreshScores()
- 位置: async L75-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._loadConfig()`
- 参照: `this._scores`

## SponsoredTopSitesScoreProvider._loadConfig()
- 位置: async L91-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `records?.find()`, `this._getRecordId()`, `this._rs?.get()`
- 参照: `r.id`

## SponsoredTopSitesScoreProvider._getRecordId()
- 位置: L109-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(flags).filter()`, `flag.startsWith()`, `this._getFlags()`
- 参照: `enabled.length`

## SponsoredTopSitesScoreProvider.getScores()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._scores`

## SponsoredTopSitesScoreProvider._getDomainDayCounts()
- 位置: async L133-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `days.get()`, `days.set()`, `domainDayCounts.get()`, `domainDayCounts.set()`, `lazy.NewTabUtils.activityStreamProvider.executePlacesQuery()`, `this._findConfiguredDomain()`, `this._revHostPrefixMap()`
- 参照: `config.lookback_days`, `lazy.PlacesUtils.history.TRANSITIONS.BOOKMARK`, `lazy.PlacesUtils.history.TRANSITIONS.LINK`, `lazy.PlacesUtils.history.TRANSITIONS.TYPED`, `prefixMap.size`, `row.day`, `row.rev_host`, `row.visits`

## SponsoredTopSitesScoreProvider._revHostPrefixMap()
- 位置: L185-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `domain.toLowerCase()`, `lazy.PlacesUtils.getReversedHost()`, `prefixMap.set()`
- 参照: `config.targets`

## SponsoredTopSitesScoreProvider._findConfiguredDomain()
- 位置: L207-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prefixMap.get()`, `revHost?.split()`, `revHost?.split(".").slice()`
