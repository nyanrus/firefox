# browser/extensions/newtab/lib/NewTabContentPing.sys.mjs

source: browser/extensions/newtab/lib/NewTabContentPing.sys.mjs
source-hash: db009e5b59208ac3969700a4fc15a85ec93ab14f
lines: 440

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## NewTabContentPing.constructor()
- 位置: L41-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.#maxDailyClickEvents`, `this.#maxDailyEvents`, `this.#maxWeeklyClickEvents`, `this.cache`

## NewTabContentPing.setMaxEventsPerDay()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#maxDailyEvents`

## NewTabContentPing.setMaxClickEventsPerDay()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#maxDailyClickEvents`

## NewTabContentPing.setMaxClickEventsPerWeek()
- 位置: L71-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#maxWeeklyClickEvents`

## NewTabContentPing.recordEvent()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#eventBuffer.push()`, `this.sanitizeEventData()`

## NewTabContentPing.scheduleSubmission()
- 位置: L96-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtabContent[metric].set()`, `Object.keys()`, `console.error()`
- 条件付き依存: `if (!this.#deferredTask)` → `this.#generateRandomSubmissionDelayMs()`
- 条件付き依存: `if (!this.#deferredTask)` → `this.#flushEventsAndSubmit()`
- 条件付き依存: `if (!this.#deferredTask)` → `this.#deferredTask.arm()`
- 参照: `Glean.newtabContent`, `lazy.DeferredTask`, `this.#deferredTask`, `this.#lastDelaySelection`

## NewTabContentPing.uninit()
- 位置: L118-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deferredTask?.disarm()`
- 参照: `this.#eventBuffer`

## NewTabContentPing.resetDailyStats()
- 位置: async L126-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`, `this.cache.set()`

## NewTabContentPing.resetWeeklyStats()
- 位置: async L137-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.Date()`, `this.Date().now()`, `this.cache.set()`

## NewTabContentPing.test_only_resetAllStats()
- 位置: async L150-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetDailyStats()`, `this.resetWeeklyStats()`

## NewTabContentPing.shuffleArray()
- 位置: L161-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`
- 参照: `array.length`

## NewTabContentPing.#flushEventsAndSubmit()
- 位置: async L174-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.newtabContent[eventName].record()`, `GleanPings.newtabContent.submit()`, `NewTabContentPing.shuffleArray()`, `console.error()`, `events.filter()`, `isOrganicClickEvent()`, `this.Date()`, `this.Date().now()`, `this.cache.get()`, `this.cache.set()`
- 条件付き依存: `if ( !eventStats?.lastUpdatedDaily || !( this.Date().now() - eventStats.lastUpdatedDaily < EVENT_STATS_DAILY_PERIOD_MS ) )` → `this.resetDailyStats()`
- 条件付き依存: `if ( !eventStats?.lastUpdatedWeekly || !( this.Date().now() - eventStats.lastUpdatedWeekly < EVENT_STATS_WEEKLY_PERIOD_MS ) )` → `this.resetWeeklyStats()`
- 条件付き依存: `if (this.#maxDailyClickEvents > 0)` → `clickEvents.slice()`
- 条件付き依存: `if (this.#maxDailyClickEvents > 0)` → `Math.max()`
- 条件付き依存: `if (this.#maxWeeklyClickEvents > 0)` → `clickEvents.slice()`
- 条件付き依存: `if (this.#maxWeeklyClickEvents > 0)` → `Math.max()`
- 条件付き依存: `if ( numOriginalClickEvents > 0 && (this.#maxDailyClickEvents > 0 || this.#maxWeeklyClickEvents > 0) )` → `events .filter(([eventName, data]) => !isOrganicClickEvent(eventName, data)) .concat()`
- 条件付き依存: `if ( numOriginalClickEvents > 0 && (this.#maxDailyClickEvents > 0 || this.#maxWeeklyClickEvents > 0) )` → `events .filter()`
- 条件付き依存: `if ( numOriginalClickEvents > 0 && (this.#maxDailyClickEvents > 0 || this.#maxWeeklyClickEvents > 0) )` → `isOrganicClickEvent()`
- 参照: `Glean.newtabContent`, `clickEvents.length`, `eventStats.dailyClickCount`, `eventStats.dailyCount`, `eventStats.lastUpdatedDaily`, `eventStats.lastUpdatedWeekly`, `eventStats.weeklyClickCount`, `eventStats?.dailyClickCount`, `eventStats?.dailyCount`, `eventStats?.lastUpdatedDaily`, `eventStats?.lastUpdatedWeekly`, `eventStats?.weeklyClickCount`, `events.length`, `this.#curInstanceEventsSent`, `this.#deferredTask`, `this.#eventBuffer`, `this.#maxDailyClickEvents`, `this.#maxDailyEvents`, `this.#maxWeeklyClickEvents`

## isOrganicClickEvent()
- 位置: L175-177
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `data.is_sponsored`

## NewTabContentPing.testOnlyCurInstanceEventCount()
- 位置: L258-260
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#curInstanceEventsSent`

## NewTabContentPing.sanitizeEventData()
- 位置: L275-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.vc.compare()`
- 参照: `AppConstants.MOZ_APP_VERSION`, `result.layout_name`, `result.section_position`, `result.source_section_id`, `result.variant_id`
- XPCOM: `Services.vc`

## NewTabContentPing.#generateRandomSubmissionDelayMs()
- 位置: L336-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NewTabContentPing.secureRandIntInRange()`
- 条件付き依存: `if (lazy.MAX_SUBMISSION_DELAY_PREF_VALUE <= MIN_SUBMISSION_DELAY)` → `console.error()`
- 参照: `lazy.MAX_SUBMISSION_DELAY_PREF_VALUE`

## NewTabContentPing.secureRandIntInRange()
- 位置: L363-379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `crypto.getRandomValues()`

## NewTabContentPing.decideWithProbability()
- 位置: L388-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.getRandomValues()`

## NewTabContentPing.testOnlyForceFlush()
- 位置: async L414-426
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#deferredTask)` → `this.#deferredTask.disarm()`
- 条件付き依存: `if (this.#deferredTask)` → `this.#flushEventsAndSubmit()`
- 参照: `Cu.isInAutomation`, `this.#deferredTask`, `this.#lastDelaySelection`

## NewTabContentPing.prototype.PersistentCache()
- 位置: L433-435
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`

## NewTabContentPing.prototype.Date()
- 位置: L437-439
- 役割: (未記入)
- 触るとき: (未記入)
