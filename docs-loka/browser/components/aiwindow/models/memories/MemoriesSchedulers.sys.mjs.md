# browser/components/aiwindow/models/memories/MemoriesSchedulers.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesSchedulers.sys.mjs
source-hash: 0e0da81216a5e8b5f11cb485023ae7d7a2e8ab4e
lines: 469

## <module>
- 役割: 記憶の生成と保守を定期的に走らせるスケジューラーを定義する。2分ごとの1つのタイマーで、生成の条件(クールダウンと閲覧・チャットの契機)と保守の周期を別々に判定する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getIntPref()`, `console.createInstance()`

## MemoriesSchedulers.maybeRunAndSchedule()
- 位置: L104-115
- 役割: 生成か保守の対象となるソースが一つでも有効なら、唯一のインスタンスを作って返す。無ければnullを返す。
- 触るとき: AIウィンドウが起動してスケジューラーが始まらない原因を調べるとき。呼び出し元はAIWindowの_startSchedulers。
- 呼び出し先: `MemoriesSchedulers.#anySourceEnabled()`
- 条件付き依存: `if (!MemoriesSchedulers.#anySourceEnabled())` → `lazy.console.debug()`
- 参照: `this.#instance`

## MemoriesSchedulers.stop()
- 位置: L120-122
- 役割: 唯一のインスタンスがあれば破棄する。
- 触るとき: テストの後始末や、AIウィンドウを閉じたときの停止処理を調べるとき。
- 呼び出し先: `this.#instance?.destroy()`

## MemoriesSchedulers.#anySourceEnabled()
- 位置: L124-129
- 役割: 履歴と会話のどちらかの記憶生成が有効かを、MemoriesManagerの判定で確かめる。
- 触るとき: 記憶生成の有効条件が増えたり減ったりしたときに、スケジューラーを動かす条件を見直すとき。
- 呼び出し先: `lazy.MemoriesManager.shouldEnableMemoriesFromSchedulers()`
- 参照: `lazy.CONVERSATION`, `lazy.HISTORY`

## MemoriesSchedulers.constructor()
- 位置: L137-144
- 役割: ページ訪問の通知を購読し、初期化処理を開始する。
- 触るとき: ページ訪問の通知の購読の仕方を変えるとき、インスタンス作成直後の動きを追うとき。
- 呼び出し先: `lazy.PlacesUtils.observers.addListener()`, `lazy.console.debug()`, `this.#init()`
- 参照: `this.#initPromise`, `this.#onPageVisited`

## MemoriesSchedulers.#init()
- 位置: async L146-167
- 役割: 最終の処理済み時刻が無ければ初回として即座に1回実行し、あれば最終生成時刻を読んで間隔タイマーを開始する。
- 触るとき: 起動直後に生成が走る、または走らないときに見るとき。初回判定の条件を変えるとき。
- 呼び出し先: `MemoriesSchedulers.#anySourceEnabled()`, `lazy.MemoriesManager.getLastGenerationRunTimestamp()`, `lazy.MemoriesManager.getLastSessionMemoryTimestamp()`
- 条件付き依存: `if (isFirstRun)` → `lazy.console.debug()`
- 条件付き依存: `if (isFirstRun)` → `this.#onInterval()`
- 条件付き依存: `if (!this.#running && !this.#intervalHandle)` → `this.#startInterval()`
- 参照: `this.#intervalHandle`, `this.#lastGenerationMs`, `this.#running`

## MemoriesSchedulers.#startInterval()
- 位置: L169-179
- 役割: 2分間隔のタイマーを開始する。既に動いていればエラーを投げる。
- 触るとき: タイマーの二重起動の例外が出るとき、間隔を変えるとき。
- 呼び出し先: `lazy.setInterval()`
- 参照: `this.#intervalHandle`, `this.#onInterval`

## MemoriesSchedulers.#stopInterval()
- 位置: L181-186
- 役割: タイマーがあれば止めて、ハンドルを0に戻す。
- 触るとき: 実行中にタイマーを止める箇所の挙動を追うとき。
- 条件付き依存: `if (this.#intervalHandle)` → `lazy.clearInterval()`
- 参照: `this.#intervalHandle`

## MemoriesSchedulers.#onPageVisited()
- 位置: L192-194
- 役割: ページ訪問の通知が来るたびに、訪問件数を1増やす。
- 触るとき: 閲覧の契機が効かないとき、訪問件数の数え方を変えるとき。
- 参照: `this.#pagesVisited`

## MemoriesSchedulers.#shouldRunGeneration()
- 位置: async L205-250
- 役割: 初回は直近60日の訪問が10件以上あれば契機成立とし、2回目以降は新しい訪問があれば成立とする。チャットは処理済み時刻以降の発話が1件でもあれば成立とする。
- 触るとき: 生成が始まる契機を変えるとき、初回の閾値や対象期間を見直すとき。
- 条件付き依存: `if (isFirstRun)` → `lazy.MemoriesManager.countRecentVisits()`
- 条件付き依存: `if (recentVisitCount >= MIN_RECENT_VISITS)` → `lazy.console.debug()`
- 条件付き依存: `if (this.#pagesVisited > 0)` → `lazy.console.debug()`
- 条件付き依存: `if (conversationEnabled)` → `lazy.getRecentChats()`
- 条件付き依存: `if (conversationEnabled)` → `lazy.MemoriesManager.getSessionMemoryDeltaStartMs()`
- 条件付き依存: `if (chatMessagesSinceLastMemory.length)` → `lazy.console.debug()`
- 参照: `chatMessagesSinceLastMemory.length`, `this.#pagesVisited`

## MemoriesSchedulers.#onInterval()
- 位置: async L252-403
- 役割: 毎回有効条件を確かめ、保守を設定値の周期(既定は4時間)ごとに実行したうえで、クールダウンの判定と契機の判定を通った時だけ記憶生成と統合を行う。429は長い待機、一時エラーは短い待機にして再試行を遅らせる。
- 触るとき: 記憶生成や統合が動かない、または繰り返し失敗するとき。待機時間や実行順を変えるとき。
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
- 役割: タイマーを止め、ページ訪問の購読を外し、以後の実行を無効にして唯一のインスタンスを空にする。
- 触るとき: スケジューラーが止まらない、または二重に動くと調べるとき。
- 呼び出し先: `lazy.PlacesUtils.observers.removeListener()`, `lazy.console.debug()`, `this.#stopInterval()`
- 参照: `MemoriesSchedulers.#instance`, `this.#destroyed`, `this.#onPageVisited`

## MemoriesSchedulers.setPagesVisitedForTesting()
- 位置: L426-428
- 役割: テスト用に訪問件数を設定する。
- 触るとき: 閲覧の契機を再現する単体テストを書くとき。
- 参照: `this.#pagesVisited`

## MemoriesSchedulers.setBackoffUntilMsForTesting()
- 位置: L436-438
- 役割: テスト用に再試行までの待機の期限を設定する。0で解除する。
- 触るとき: 待機中の挙動を確かめるテストを書くとき。
- 参照: `this.#backoffUntilMs`

## MemoriesSchedulers.setLastMaintenanceMsForTesting()
- 位置: L446-448
- 役割: テスト用に最終保守の時刻を設定する。0で次の回に保守を走らせる。
- 触るとき: 保守の実行を強制するテストを書くとき。
- 参照: `this.#lastMaintenanceMs`

## MemoriesSchedulers.setLastGenerationMsForTesting()
- 位置: L456-458
- 役割: テスト用に最終生成の時刻を設定する。0でクールダウンを解除する。
- 触るとき: クールダウンの挙動を確かめるテストを書くとき。
- 参照: `this.#lastGenerationMs`

## MemoriesSchedulers.runNowForTesting()
- 位置: async L464-467
- 役割: テスト用に、初期化の完了を待ってから間隔の処理を1回だけ実行する。
- 触るとき: スケジューラーの1回分の処理をテストから直接動かすとき。
- 呼び出し先: `this.#onInterval()`
- 参照: `this.#initPromise`
