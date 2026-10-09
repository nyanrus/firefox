# browser/components/aiwindow/models/TelemetryManager.sys.mjs

source: browser/components/aiwindow/models/TelemetryManager.sys.mjs
source-hash: 07e3544b9a80946fbbbf053ca9bf90f32455e02b
lines: 230

## <module>
- 役割: 会話終了時の LLM テレメトリを定期的に実行するスケジューラー TelemetryScheduler を定義する。最後の実行から 24 時間経過したときだけ、会話ごとに評価ジョブを走らせる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## TelemetryScheduler.maybeInit()
- 位置: L49-55
- 役割: シングルトンの TelemetryScheduler を作って返す。すでにあれば既存のものを返す。
- 触るとき: テレメトリの起動箇所を変えるとき、またはスケジューラーが二重に動くか確認するとき。
- 参照: `this.#instance`

## TelemetryScheduler.constructor()
- 位置: L63-67
- 役割: 初期化処理(#init)を非同期に起動し、初期化済みをデバッグログに出す。
- 触るとき: 起動時の初期化の流れを追うとき。
- 呼び出し先: `lazy.console.debug()`, `this.#init()`

## TelemetryScheduler.#init()
- 位置: async L77-87
- 役割: 最終実行時刻の pref が 0 なら初回として即時に #onInterval を待ち、そうでなければ #startInterval で周期実行を始める。
- 触るとき: 初回実行の条件(初めて起動した直後に走らせるか)を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (isFirstRun)` → `lazy.console.debug()`
- 条件付き依存: `if (isFirstRun)` → `this.#onInterval()`
- 条件付き依存: `if (!(isFirstRun))` → `this.#startInterval()`
- XPCOM: `Services.prefs`

## TelemetryScheduler.#startInterval()
- 位置: L96-106
- 役割: 2 分ごとに #onInterval を呼ぶタイマーを設定する。既にタイマーがあれば例外を投げる。
- 触るとき: ポーリング間隔を変えるとき、または「interval already existed」の例外が出る経路を調べるとき。
- 呼び出し先: `lazy.setInterval()`
- 参照: `this.#intervalHandle`, `this.#onInterval`

## TelemetryScheduler.#stopInterval()
- 位置: L111-116
- 役割: タイマーがあれば解除してハンドルを 0 に戻す。
- 触るとき: 実行中の多重起動を防ぐ処理を見直すとき。
- 条件付き依存: `if (this.#intervalHandle)` → `lazy.clearInterval()`
- 参照: `this.#intervalHandle`

## TelemetryScheduler.#onInterval()
- 位置: async L123-221
- 役割: 最終実行から 24 時間未満なら何もせず、そうでなければ未処理の会話を順に読み、ジョブを実行して結果を送信し、処理済みを記録する。終わりに最終実行時刻を保存して周期を再開する。
- 触るとき: テレメトリの対象会話の選び方、送信間隔の待ち時間、失敗時の続行方針を変えるとき。実行中フラグとクールダウンの判定が絡むので注意。
- 呼び出し先: `( await telemetryEngine.runTelemetryByName( telemetryNames, conversation ) ).map()`, `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Date.now()`, `Math.floor()`, `Math.max()`, `Math.random()`, `Object.keys()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `conversation.currentTurnIndex()`, `lazy.ChatStore.findConversationById()`, `lazy.ChatStore.getConversationsForTelemetry()`, `lazy.ChatStore.markLLMTelemetryProcessed()`, `lazy.console.debug()`, `lazy.console.error()`, `lazy.setTimeout()`, `lazy.submitTelemetryResult()`, `telemetryEngine.runTelemetryByName()`, `this.#stopInterval()`
- 条件付き依存: `if (this.#destroyed)` → `lazy.console.warn()`
- 条件付き依存: `if (this.#running)` → `lazy.console.debug()`
- 条件付き依存: `if (!this.#destroyed)` → `this.#startInterval()`
- 参照: `conversationObj.convId`, `conversationObj.modelId`, `conversationObj.telemetryJobs`, `conversationObj.telemetryProbs`, `conversationObj.uniformSamplingProbability`, `conversationsToRun.length`, `lazy.TelemetryEngine`, `r.telemetry_name`, `this.#destroyed`, `this.#running`
- XPCOM: `Services.prefs`

## TelemetryScheduler.destroy()
- 位置: L223-228
- 役割: タイマーを止め、破棄フラグを立てて、シングルトンの参照を消す。
- 触るとき: シャットダウンや機能の無効化時にテレメトリを確実に止めたいとき。
- 呼び出し先: `lazy.console.debug()`, `this.#stopInterval()`
- 参照: `TelemetryScheduler.#instance`, `this.#destroyed`
