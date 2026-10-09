# browser/components/aiwindow/models/memories/MemoriesSchedulers.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesSchedulers.sys.mjs
source-hash: 0e0da81216a5e8b5f11cb485023ae7d7a2e8ab4e
lines: 469

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getIntPref()`, `console.createInstance()`

## MemoriesSchedulers.maybeRunAndSchedule()
- 位置: L104-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoriesSchedulers.#anySourceEnabled()`
- 条件付き依存: `if (!MemoriesSchedulers.#anySourceEnabled())` → `lazy.console.debug()`
- 参照: `this.#instance`

## MemoriesSchedulers.stop()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#instance?.destroy()`

## MemoriesSchedulers.#anySourceEnabled()
- 位置: L124-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MemoriesManager.shouldEnableMemoriesFromSchedulers()`
- 参照: `lazy.CONVERSATION`, `lazy.HISTORY`

## MemoriesSchedulers.constructor()
- 位置: L137-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.observers.addListener()`, `lazy.console.debug()`, `this.#init()`
- 参照: `this.#initPromise`, `this.#onPageVisited`

## MemoriesSchedulers.#init()
- 位置: async L146-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MemoriesSchedulers.#anySourceEnabled()`, `lazy.MemoriesManager.getLastGenerationRunTimestamp()`, `lazy.MemoriesManager.getLastSessionMemoryTimestamp()`
- 条件付き依存: `if (isFirstRun)` → `lazy.console.debug()`
- 条件付き依存: `if (isFirstRun)` → `this.#onInterval()`
- 条件付き依存: `if (!this.#running && !this.#intervalHandle)` → `this.#startInterval()`
- 参照: `this.#intervalHandle`, `this.#lastGenerationMs`, `this.#running`

## MemoriesSchedulers.#startInterval()
- 位置: L169-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setInterval()`
- 参照: `this.#intervalHandle`, `this.#onInterval`

## MemoriesSchedulers.#stopInterval()
- 位置: L181-186
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#intervalHandle)` → `lazy.clearInterval()`
- 参照: `this.#intervalHandle`

## MemoriesSchedulers.#onPageVisited()
- 位置: L192-194
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pagesVisited`

## MemoriesSchedulers.#shouldRunGeneration()
- 位置: async L205-250
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isFirstRun)` → `lazy.MemoriesManager.countRecentVisits()`
- 条件付き依存: `if (recentVisitCount >= MIN_RECENT_VISITS)` → `lazy.console.debug()`
- 条件付き依存: `if (this.#pagesVisited > 0)` → `lazy.console.debug()`
- 条件付き依存: `if (conversationEnabled)` → `lazy.getRecentChats()`
- 条件付き依存: `if (conversationEnabled)` → `lazy.MemoriesManager.getSessionMemoryDeltaStartMs()`
- 条件付き依存: `if (chatMessagesSinceLastMemory.length)` → `lazy.console.debug()`
- 参照: `chatMessagesSinceLastMemory.length`, `this.#pagesVisited`

## MemoriesSchedulers.#onInterval()
- 位置: async L252-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `MemoriesSchedulers.#anySourceEnabled()`, `lazy.MemoriesManager.generateMemoriesFromSessions()`, `lazy.MemoriesManager.getLastSessionMemoryTimestamp()`, `lazy.MemoriesManager.setLastGenerationRunTimestamp()`, `lazy.MemoriesManager.shouldEnableMemoriesFromSchedulers()`, `lazy.console.debug()`, `lazy.openAIEngine.is429Error()`, `this.#shouldRunGeneration()`, `this.#stopInterval()`
- 条件付き依存: `if (this.#destroyed)` → `lazy.console.warn()`
- 条件付き依存: `if (!historyEnabled && !conversationEnabled)` → `lazy.console.debug()`
- 条件付き依存: `if (!historyEnabled && !conversationEnabled)` → `this.destroy()`
- 条件付き依存: `if (this.#running)` → `lazy.console.debug()`
- 条件付き依存: `if (this.#backoffUntilMs && Date.now() < this.#backoffUntilMs)` → `Math.ceil()`
- 条件付き依存: `if (this.#backoffUntilMs && Date.now() < this.#backoffUntilMs)` → `Date.now()`
- 条件付き依存: `if (this.#backoffUntilMs && Date.now() < this.#backoffUntilMs)` → `lazy.console.debug()`
- 条件付き依存: `if (now - this.#lastMaintenanceMs >= MEMORIES_MAINTENANCE_INTERVAL_MS)` → `lazy.console.debug()`
- 条件付き依存: `if (now - this.#lastMaintenanceMs >= MEMORIES_MAINTENANCE_INTERVAL_MS)` → `lazy.MemoriesManager.runMemoryMaintenance()`
- 条件付き依存: `if (now - this.#lastMaintenanceMs >= MEMORIES_MAINTENANCE_INTERVAL_MS)` → `lazy.console.error()`
- 条件付き依存: `if (!(now - this.#lastMaintenanceMs >= MEMORIES_MAINTENANCE_INTERVAL_MS))` → `lazy.console.debug()`
- 条件付き依存: `if (!(now - this.#lastMaintenanceMs >= MEMORIES_MAINTENANCE_INTERVAL_MS))` → `( (now - this.#lastMaintenanceMs) / (60 * 1000) ).toFixed()`
- 条件付き依存: `if (!(now - this.#lastMaintenanceMs >= MEMORIES_MAINTENANCE_INTERVAL_MS))` → `Math.floor()`
- 条件付き依存: `if ( this.#lastGenerationMs && now - this.#lastGenerationMs < MEMORIES_SCHEDULER_COOLDOWN_MS )` → `lazy.console.debug()`
- 条件付き依存: `if ( this.#lastGenerationMs && now - this.#lastGenerationMs < MEMORIES_SCHEDULER_COOLDOWN_MS )` → `Math.floor()`
- 条件付き依存: `if (!shouldRunGeneration)` → `lazy.console.debug()`
- 条件付き依存: `if (!shouldRunGeneration)` → `Date.now()`
- 条件付き依存: `if (!shouldRunGeneration)` → `lazy.MemoriesManager.setLastGenerationRunTimestamp()`
- 条件付き依存: `if (persistedMemories.length)` → `lazy.console.debug()`
- 条件付き依存: `if (persistedMemories.length)` → `lazy.MemoriesManager.mergeMemories()`
- 条件付き依存: `if (!(persistedMemories.length))` → `lazy.console.debug()`
- 条件付き依存: `if (lazy.openAIEngine.is429Error(error))` → `Date.now()`
- 条件付き依存: `if (lazy.openAIEngine.is429Error(error))` → `lazy.console.warn()`
- 条件付き依存: `if (lazy.openAIEngine.is429Error(error))` → `Math.floor()`
- 条件付き依存: `if (!(lazy.openAIEngine.is429Error(error)))` → `lazy.openAIEngine.isRetryableError()`
- 条件付き依存: `if (lazy.openAIEngine.isRetryableError(error))` → `Date.now()`
- 条件付き依存: `if (lazy.openAIEngine.isRetryableError(error))` → `lazy.console.warn()`
- 条件付き依存: `if (lazy.openAIEngine.isRetryableError(error))` → `Math.floor()`
- 条件付き依存: `if (!(lazy.openAIEngine.isRetryableError(error)))` → `lazy.console.error()`
- 条件付き依存: `if (!this.#destroyed && MemoriesSchedulers.#anySourceEnabled())` → `this.#startInterval()`
- 参照: `lazy.CONVERSATION`, `lazy.HISTORY`, `persistedMemories.length`, `this.#backoffUntilMs`, `this.#destroyed`, `this.#lastGenerationMs`, `this.#lastMaintenanceMs`, `this.#pagesVisited`, `this.#running`

## MemoriesSchedulers.destroy()
- 位置: L410-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.observers.removeListener()`, `lazy.console.debug()`, `this.#stopInterval()`
- 参照: `MemoriesSchedulers.#instance`, `this.#destroyed`, `this.#onPageVisited`

## MemoriesSchedulers.setPagesVisitedForTesting()
- 位置: L426-428
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#pagesVisited`

## MemoriesSchedulers.setBackoffUntilMsForTesting()
- 位置: L436-438
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#backoffUntilMs`

## MemoriesSchedulers.setLastMaintenanceMsForTesting()
- 位置: L446-448
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastMaintenanceMs`

## MemoriesSchedulers.setLastGenerationMsForTesting()
- 位置: L456-458
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lastGenerationMs`

## MemoriesSchedulers.runNowForTesting()
- 位置: async L464-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onInterval()`
- 参照: `this.#initPromise`
