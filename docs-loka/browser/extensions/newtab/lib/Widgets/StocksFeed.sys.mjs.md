# browser/extensions/newtab/lib/Widgets/StocksFeed.sys.mjs

source: browser/extensions/newtab/lib/Widgets/StocksFeed.sys.mjs
source-hash: d6e14cc16e0457d0931d02f40c2c06413f05389f
lines: 593

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## StocksFeed.constructor()
- 位置: L45-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.cache`, `this.cacheWriteChain`, `this.error`, `this.fetchGeneration`, `this.fetchIntervalMs`, `this.fetchTimer`, `this.lastUpdated`, `this.loaded`, `this.merino`, `this.pendingFullRefresh`, `this.retryTimer`, `this.tickers`, `this.watchlistDesiredSaved`, `this.watchlistExpiring`, `this.watchlistGeneration`, `this.watchlistLastFullRefresh`, `this.watchlistProcessedVersion`, `this.watchlistRequestedVersion`, `this.watchlistSymbols`, `this.watchlistTickers`, `this.watchlistWorker`

## StocksFeed.isEnabled()
- 位置: L70-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs`, `values.trainhopConfig?.widgets?.stocksEnabled`

## StocksFeed.init()
- 位置: async L79-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`, `this.loadStocks()`, `this.loadWatchlist()`
- 参照: `this.fetchGeneration`

## StocksFeed.stopFetching()
- 位置: L88-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearTimeout()`
- 参照: `this.error`, `this.fetchGeneration`, `this.fetchTimer`, `this.lastUpdated`, `this.merino`, `this.pendingFullRefresh`, `this.retryTimer`, `this.tickers`, `this.watchlistGeneration`, `this.watchlistLastFullRefresh`, `this.watchlistSymbols`, `this.watchlistTickers`

## StocksFeed.restartFetchTimer()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearTimeout()`, `this.fetch()`, `this.setTimeout()`
- 参照: `this.fetchIntervalMs`, `this.fetchTimer`

## StocksFeed.loadStocks()
- 位置: async L121-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`, `this.cache.get()`
- 条件付き依存: `if ( !stocks?.lastUpdated || this.Date().now() - stocks.lastUpdated >= STOCKS_UPDATE_TIME )` → `this.fetch()`
- 条件付き依存: `if (!this.lastUpdated)` → `this.update()`
- 条件付き依存: `if (!this.lastUpdated)` → `this.Date().now()`
- 条件付き依存: `if (!this.lastUpdated)` → `this.Date()`
- 条件付き依存: `if (!this.lastUpdated)` → `this.restartFetchTimer()`
- 条件付き依存: `if (!this.lastUpdated)` → `Math.max()`
- 参照: `stocks.lastUpdated`, `stocks.tickers`, `stocks?.lastUpdated`, `this.fetchGeneration`, `this.lastUpdated`, `this.loaded`, `this.tickers`

## StocksFeed.ensureMerinoClient()
- 位置: L147-157
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.merino)` → `this.MerinoClient()`
- 参照: `this.fetchGeneration`, `this.merino`

## StocksFeed.search()
- 位置: async L162-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.fetch()`, `client.resetSession()`, `console.error()`, `query.trim()`, `query.trim().replace()`, `query.trim().replace(/^\$+/, "").trim()`, `reply()`, `this.MerinoClient()`, `this.isEnabled()`
- 条件付き依存: `if (!this.isEnabled() || typeof query !== "string")` → `reply()`
- 条件付き依存: `if (!normalized)` → `reply()`
- 条件付き依存: `if ( status === "timeout" || status === "network_error" || status === "http_error" )` → `reply()`
- 条件付き依存: `if (!( status === "timeout" || status === "network_error" || status === "http_error" ))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(matches) && matches.length)` → `reply()`
- 条件付き依存: `if (!(Array.isArray(matches) && matches.length))` → `reply()`
- 参照: `client.lastFetchStatus`, `matches.length`, `result?.[0]?.custom_details?.polygon?.matches`

## reply()
- 位置: L166-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToOneContent()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_STOCKS_SEARCH_RESPONSE`

## StocksFeed.fetch()
- 位置: async L220-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._fetchHelper()`, `this.ensureMerinoClient()`, `this.restartFetchTimer()`, `this.update()`
- 条件付き依存: `if (tickers.length)` → `this.Date().now()`
- 条件付き依存: `if (tickers.length)` → `this.Date()`
- 条件付き依存: `if (tickers.length)` → `this.clearTimeout()`
- 条件付き依存: `if (tickers.length)` → `this._cacheSet()`
- 条件付き依存: `if (!tickers.length && retryCount < MAX_RETRIES)` → `this.clearTimeout()`
- 条件付き依存: `if (!tickers.length && retryCount < MAX_RETRIES)` → `this.setTimeout()`
- 条件付き依存: `if (!tickers.length && retryCount < MAX_RETRIES)` → `this.fetch()`
- 参照: `this.error`, `this.fetchGeneration`, `this.lastUpdated`, `this.retryTimer`, `this.tickers`, `tickers.length`

## StocksFeed._fetchHelper()
- 位置: async L275-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `console.error()`, `this.merino.fetch()`
- 参照: `result?.[0]?.custom_details?.polygon?.values`, `this.merino`, `values.length`

## StocksFeed._fetchWatchlistSymbol()
- 位置: async L296-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalize()`, `this._fetchHelper()`, `values.find()`
- 参照: `v.ticker`

## StocksFeed.getSavedWatchlistSymbols()
- 位置: L301-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseWatchlist()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs.values`

## StocksFeed.watchlistFetchSet()
- 位置: L309-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defaults.has()`, `normalize()`, `saved.filter()`, `this.tickers.map()`
- 参照: `t.ticker`

## StocksFeed.reconcileWatchlist()
- 位置: L314-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._startWatchlistWorker()`, `this.getSavedWatchlistSymbols()`
- 条件付き依存: `if (this.watchlistExpiring)` → `Promise.resolve()`
- 参照: `this.pendingFullRefresh`, `this.watchlistDesiredSaved`, `this.watchlistExpiring`, `this.watchlistRequestedVersion`, `this.watchlistWorker`

## StocksFeed._startWatchlistWorker()
- 位置: L325-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._runWatchlistWorker()`, `this._runWatchlistWorker( this.watchlistGeneration ).finally()`, `this.isEnabled()`
- 条件付き依存: `if ( this.watchlistProcessedVersion !== this.watchlistRequestedVersion && this.isEnabled() )` → `this._startWatchlistWorker()`
- 参照: `this.watchlistGeneration`, `this.watchlistProcessedVersion`, `this.watchlistRequestedVersion`, `this.watchlistWorker`

## StocksFeed._runWatchlistWorker()
- 位置: async L345-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...merged.entries()] .filter()`, `[...merged.entries()] .filter(([sym]) => keep.has(sym)) .map()`, `console.error()`, `have.has()`, `keep.has()`, `merged.entries()`, `normalize()`, `this._fetchWatchlistSymbols()`, `this._writeWatchlistCache()`, `this.broadcastWatchlist()`, `this.ensureMerinoClient()`, `this.watchlistFetchSet()`, `this.watchlistTickers.map()`, `toFetch.filter()`
- 条件付き依存: `if (summary)` → `merged.set()`
- 条件付き依存: `if (full)` → `this.Date().now()`
- 条件付き依存: `if (full)` → `this.Date()`
- 参照: `t.ticker`, `this.pendingFullRefresh`, `this.watchlistDesiredSaved`, `this.watchlistGeneration`, `this.watchlistLastFullRefresh`, `this.watchlistProcessedVersion`, `this.watchlistRequestedVersion`, `this.watchlistSymbols`, `this.watchlistTickers`

## StocksFeed._fetchWatchlistSymbols()
- 位置: async L407-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `results.set()`, `this._fetchWatchlistSymbol()`
- 参照: `this.watchlistGeneration`, `this.watchlistRequestedVersion`

## StocksFeed.broadcastWatchlist()
- 位置: L421-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_STOCKS_WATCHLIST_UPDATE`, `this.watchlistSymbols`, `this.watchlistTickers`

## StocksFeed._cacheSet()
- 位置: L437-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.cacheWriteChain || Promise.resolve()).then()`, `Promise.resolve()`, `op.catch()`, `this.cache.set()`
- 参照: `this.cacheWriteChain`

## StocksFeed._writeWatchlistCache()
- 位置: async L445-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cacheSet()`
- 参照: `this.watchlistLastFullRefresh`, `this.watchlistSymbols`, `this.watchlistTickers`

## StocksFeed.loadWatchlist()
- 位置: async L453-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._watchlistIsStale()`, `this.cache.get()`, `this.reconcileWatchlist()`
- 条件付き依存: `if (wl?.watchlistTickers?.length)` → `this.broadcastWatchlist()`
- 参照: `cached.stocksWatchlist`, `this.watchlistGeneration`, `this.watchlistLastFullRefresh`, `this.watchlistSymbols`, `this.watchlistTickers`, `wl.lastFullRefresh`, `wl.watchlistSymbols`, `wl.watchlistTickers`, `wl?.watchlistTickers?.length`

## StocksFeed._watchlistIsStale()
- 位置: L472-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`
- 参照: `this.watchlistLastFullRefresh`

## StocksFeed.refreshWatchlistIfStale()
- 位置: async L480-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._watchlistIsStale()`
- 条件付き依存: `if (this._watchlistIsStale())` → `this.reconcileWatchlist()`

## StocksFeed.update()
- 位置: L486-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_STOCKS_UPDATE`, `this.error`, `this.lastUpdated`, `this.tickers`

## StocksFeed.onPrefChangedAction()
- 位置: async L499-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`
- 条件付き依存: `if (enabled && !this.loaded)` → `this.init()`
- 条件付き依存: `if (!enabled)` → `this.stopFetching()`
- 条件付き依存: `if (this.isEnabled())` → `this.reconcileWatchlist()`
- 参照: `action.data.name`, `this.loaded`

## StocksFeed.onAction()
- 位置: async L522-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cacheSet()`, `this.isEnabled()`, `this.onPrefChangedAction()`, `this.search()`, `this.stopFetching()`
- 条件付き依存: `if (this.isEnabled() && !this.loaded)` → `this.init()`
- 条件付き依存: `if (this.isEnabled())` → `this.loadStocks()`
- 条件付き依存: `if (this.isEnabled())` → `this.refreshWatchlistIfStale()`
- 条件付き依存: `if (this.isEnabled())` → `this.fetch()`
- 条件付き依存: `if (this.isEnabled())` → `this.reconcileWatchlist()`
- 参照: `action.data?.query`, `action.data?.requestId`, `action.meta?.fromTarget`, `action.type`, `at.DISCOVERY_STREAM_DEV_EXPIRE_CACHE`, `at.INIT`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.UNINIT`, `at.WIDGETS_STOCKS_SEARCH_REQUEST`, `this.cacheWriteChain`, `this.fetchGeneration`, `this.lastUpdated`, `this.loaded`, `this.pendingFullRefresh`, `this.tickers`, `this.watchlistExpiring`, `this.watchlistGeneration`, `this.watchlistLastFullRefresh`, `this.watchlistProcessedVersion`, `this.watchlistRequestedVersion`, `this.watchlistSymbols`, `this.watchlistTickers`, `this.watchlistWorker`

## StocksFeed.prototype.MerinoClient()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MerinoClient`

## StocksFeed.prototype.PersistentCache()
- 位置: L581-583
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## StocksFeed.prototype.Date()
- 位置: L584-586
- 役割: (未記入)
- 触るとき: (未記入)

## StocksFeed.prototype.setTimeout()
- 位置: L587-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setTimeout()`

## StocksFeed.prototype.clearTimeout()
- 位置: L590-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clearTimeout()`
