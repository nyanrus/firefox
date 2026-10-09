# browser/components/urlbar/private/ImpressionCaps.sys.mjs

source: browser/components/urlbar/private/ImpressionCaps.sys.mjs
source-hash: 9bddf7752e1e0299df61db0f83f442822e2c79d7
lines: 459

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ImpressionCaps.constructor()
- 位置: L23-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.addObserver()`, `super()`

## ImpressionCaps.enablingPreferences()
- 位置: L28-33
- 役割: (未記入)
- 触るとき: (未記入)

## ImpressionCaps.enable()
- 位置: L35-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (enabled)` → `this.#init()`
- 条件付き依存: `if (!(enabled))` → `this.#uninit()`

## ImpressionCaps.updateStats()
- 位置: L51-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`, `this.logger.debug()`
- 条件付き依存: `if ( (isSponsored && !lazy.UrlbarPrefs.get("quickSuggestImpressionCapsSponsoredEnabled")) || (!isSponsored && !lazy.UrlbarPrefs.get("quickSuggestImpressionCapsNo...)` → `this.logger.debug()`
- 条件付き依存: `if (!stats)` → `this.logger.debug()`
- 条件付き依存: `if (stat.count == stat.maxCount)` → `this.logger.debug()`
- 参照: `lazy.QuickSuggest.config.impression_caps`, `stat.count`, `stat.impressionDateMs`, `stat.maxCount`, `this.#stats`, `this.#updatingStats`

## ImpressionCaps.getHitStats()
- 位置: L118-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resetElapsedCounters()`
- 条件付き依存: `if (stats)` → `stats.filter()`
- 参照: `hitStats.length`, `s.count`, `s.maxCount`, `this.#stats`

## ImpressionCaps.onPrefChanged()
- 位置: L136-147
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#updatingStats)` → `this.logger.debug()`
- 条件付き依存: `if (!this.#updatingStats)` → `this.#loadStats()`
- 参照: `this.#updatingStats`

## ImpressionCaps.#init()
- 位置: L149-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AsyncShutdown.profileChangeTeardown.addBlocker()`, `this.#loadStats()`, `this.#setCountersResetInterval()`
- 参照: `this._onConfigSet`, `this._shutdownBlocker`

## this._onConfigSet()
- 位置: L153-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#validateStats()`

## this._shutdownBlocker()
- 位置: L162-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resetElapsedCounters()`

## ImpressionCaps.#uninit()
- 位置: L169-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AsyncShutdown.profileChangeTeardown.removeBlocker()`, `lazy.clearInterval()`
- 参照: `this._impressionCountersResetInterval`, `this._onConfigSet`, `this._shutdownBlocker`

## ImpressionCaps.#loadStats()
- 位置: L187-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#validateStats()`
- 条件付き依存: `if (!(!json))` → `JSON.parse()`
- 参照: `this.#stats`

## ImpressionCaps.#validateStats()
- 位置: L213-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(cap.custom || []).reduce()`, `Array.isArray()`, `Object.entries()`, `map.set()`, `maxCapCounts.entries()`, `stats.find()`, `stats.some()`, `stats.sort()`, `this.logger.debug()`
- 条件付き依存: `if (typeof cap.lifetime == "number")` → `maxCapCounts.set()`
- 条件付き依存: `if ( typeof stat.intervalSeconds != "number" || typeof stat.startDateMs != "number" || typeof stat.count != "number" || typeof stat.maxCount != "number" || typeo...)` → `stats.splice()`
- 条件付き依存: `if (!( typeof stat.intervalSeconds != "number" || typeof stat.startDateMs != "number" || typeof stat.count != "number" || typeof stat.maxCount != "number" || typeo...))` → `Math.max()`
- 条件付き依存: `if (!( typeof stat.intervalSeconds != "number" || typeof stat.startDateMs != "number" || typeof stat.count != "number" || typeof stat.maxCount != "number" || typeo...))` → `maxCapCounts.get()`
- 条件付き依存: `if (maxCount === undefined)` → `stats.splice()`
- 条件付き依存: `if (maxCount === undefined)` → `orphanStats.push()`
- 条件付き依存: `if (!stats.some(s => s.intervalSeconds == intervalSeconds))` → `stats.push()`
- 条件付き依存: `if (!stats.some(s => s.intervalSeconds == intervalSeconds))` → `Date.now()`
- 条件付き依存: `if (orphan.intervalSeconds <= stat.intervalSeconds)` → `Math.max()`
- 条件付き依存: `if (orphan.intervalSeconds <= stat.intervalSeconds)` → `Math.min()`
- 参照: `a.intervalSeconds`, `b.intervalSeconds`, `cap.custom`, `cap.lifetime`, `lazy.QuickSuggest.config`, `lifetimeStat.count`, `orphan.count`, `orphan.impressionDateMs`, `orphan.intervalSeconds`, `orphan.startDateMs`, `s.intervalSeconds`, `stat.count`, `stat.impressionDateMs`, `stat.intervalSeconds`, `stat.maxCount`, `stat.startDateMs`, `stats.length`, `this.#stats`

## ImpressionCaps.#resetElapsedCounters()
- 位置: L329-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.floor()`, `Object.entries()`, `this.logger.debug()`
- 条件付き依存: `if (elapsedIntervalCount)` → `this.logger.debug()`
- 参照: `lazy.QuickSuggest.config.impression_caps`, `stat.count`, `stat.intervalSeconds`, `stat.startDateMs`, `this.#stats`

## ImpressionCaps.#setCountersResetInterval()
- 位置: L375-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setInterval()`, `this.#resetElapsedCounters()`
- 条件付き依存: `if (this._impressionCountersResetInterval)` → `lazy.clearInterval()`
- 参照: `this._impressionCountersResetInterval`

## ImpressionCaps._getStartupDateMs()
- 位置: L393-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.startup.getStartupInfo()`, `Services.startup.getStartupInfo().process.getTime()`
- XPCOM: `Services.startup`

## ImpressionCaps._test_stats()
- 位置: L397-399
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#stats`

## ImpressionCaps._test_reloadStats()
- 位置: L401-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#loadStats()`
- 参照: `this.#stats`

## ImpressionCaps._test_resetElapsedCounters()
- 位置: L406-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resetElapsedCounters()`

## ImpressionCaps._test_setCountersResetInterval()
- 位置: L410-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setCountersResetInterval()`
