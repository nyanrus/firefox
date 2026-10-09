# browser/components/aiwindow/models/agents/Monitor.sys.mjs

source: browser/components/aiwindow/models/agents/Monitor.sys.mjs
source-hash: 87657b2c7ccda9329bdcc854bdf176d4e49877ab
lines: 1188

## <module>
- 役割: 監視エージェント(Monitor)1 件の状態と実行を担うモジュール。定期実行、ページ取得と LLM 判定、履歴、自動失効、エラー分類と telemetry を扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `String()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## [MONITOR_EXPIRY_REASONS.NO_MATCH]()
- 位置: L89-89
- 役割: 条件一致しないまま続いた期間の上限として、pref browser.smartwindow.agent.expiry.noMatchDays の日数を返す。
- 触るとき: 一致なしによる自動停止の期間を変える pref を扱うとき。
- 参照: `lazy.expiryNoMatchDays`

## [MONITOR_EXPIRY_REASONS.MAX_AGE]()
- 位置: L90-90
- 役割: 監視の最長稼働期間として、pref browser.smartwindow.agent.expiry.maxAgeDays の日数を返す。
- 触るとき: 最長稼働による自動停止の期間を変える pref を扱うとき。
- 参照: `lazy.expiryMaxAgeDays`

## MonitorRunError.constructor()
- 位置: L105-109
- 役割: 失敗カテゴリ(code)を持つ実行エラーを作る。元のエラーは cause として残す。
- 触るとき: 新しい失敗カテゴリを実行中に投げるとき、またはエラーの code が history の errorCode になる経路を追うとき。
- 呼び出し先: `super()`
- 参照: `this.code`, `this.name`

## MonitorLimitError.constructor()
- 位置: L121-126
- 役割: 有効な監視が上限(TOTAL_NUM_MONITORS)に達したときのエラーを作る。code は active_limit_reached 固定。
- 触るとき: 監視の作成や再開の上限チェックを変えるとき、または UI が上限エラーを判定する方法を確認するとき。
- 呼び出し先: `super()`
- 参照: `MONITOR_ERROR_CODES.ACTIVE_LIMIT`, `this.code`, `this.limit`, `this.name`

## Monitor.constructor()
- 位置: L207-260
- 役割: 監視の各フィールドを既定値付きで設定する。スケジュールが無効、ID やプロンプト、URL が空なら例外を投げ、次回実行時刻も未指定なら計算する。
- 触るとき: 監視の新規作成や復元で必須項目を追加・変更するとき、または不正な監視が作られる原因を調べるとき。
- 呼び出し先: `Array.isArray()`, `String()`, `String(monitorPrompt ?? "").trim()`, `String(title ?? "").trim()`, `crypto.randomUUID()`, `new Date().toISOString()`, `schedule.getNextRunTime()`, `schedule.getNextRunTime(lastRunTime).toISOString()`, `trimAndFilterWatchUrls()`
- 参照: `schedule?.getNextRunTime`, `this.activeSince`, `this.createdAt`, `this.enabled`, `this.expiry`, `this.history`, `this.id`, `this.initialSnapshot`, `this.lastMatchAt`, `this.lastRunTime`, `this.monitorPrompt`, `this.nextRunTime`, `this.notificationsMuted`, `this.runCount`, `this.schedule`, `this.title`, `this.updatedAt`, `this.watchUrls`, `this.watchUrls.length`

## Monitor.fromJSON()
- 位置: L266-292
- 役割: 保存済みの JSON から監視を復元する。履歴は running を error に直し、lastMatchAt が無い古い保存データは履歴から補う。
- 触るとき: 保存形式の互換性を保ったままフィールドを増やすとき、または再起動後に監視の状態が変わる原因を調べるとき。
- 呼び出し先: `Schedule.fromJSON()`, `latestMatchTime()`, `normalizeLoadedHistory()`
- 参照: `savedMonitor.activeSince`, `savedMonitor.createdAt`, `savedMonitor.enabled`, `savedMonitor.expiry`, `savedMonitor.history`, `savedMonitor.id`, `savedMonitor.initialSnapshot`, `savedMonitor.lastMatchAt`, `savedMonitor.lastRunTime`, `savedMonitor.monitorPrompt`, `savedMonitor.nextRunTime`, `savedMonitor.notificationsMuted`, `savedMonitor.runCount`, `savedMonitor.schedule`, `savedMonitor.title`, `savedMonitor.updatedAt`, `savedMonitor.watchUrls`, `savedMonitor?.id`

## Monitor.run()
- 位置: async L302-427
- 役割: 監視の 1 回分の実行本体。実行中でなければ履歴に running を追加し、条件判定を行い、タイムアウト付きで結果を記録し、最後に保存と telemetry を行う。
- 触るとき: 実行の順序、タイムアウト、失効での停止、次回スケジュールの決め方を変えるとき。手動と定期の違いもここで分かれる。
- 呼び出し先: `ChromeUtils.now()`, `Math.round()`, `String()`, `abortController.abort()`, `checkedAt.toISOString()`, `crypto.randomUUID()`, `getCancelCode()`, `getRunReason()`, `lazy.MonitorAgent._saveAndNotify()`, `monitorErrorCode()`, `new Date().toISOString()`, `recordRunEnd()`, `recordRunRequest()`, `scheduledRunDelayMs()`, `this.#finishRun()`, `this.addHistoryEntry()`, `this.runMonitorCheck()`, `this.schedule .getNextRunTime()`, `this.schedule .getNextRunTime(this.lastRunTime) .toISOString()`, `withTimeout()`
- 条件付き依存: `if (!this.enabled || new Date(this.nextRunTime) > checkedAt)` → `this.scheduleNextRun()`
- 条件付き依存: `if (!manual)` → `this.getExpiryReason()`
- 条件付き依存: `if (expiryReason)` → `lazy.MonitorAgent._expireMonitor()`
- 条件付き依存: `if (timedOut && checkPromise)` → `checkPromise.catch()`
- 参照: `abortController.signal`, `abortController.signal.reason`, `error.message`, `historyEntry.checkedAt`, `historyEntry.conditionMet`, `historyEntry.errorCode`, `historyEntry.resultExplanation`, `historyEntry.status`, `result.conditionMet`, `result.explanation`, `this.#abortController`, `this.#disposed`, `this.#running`, `this.enabled`, `this.id`, `this.lastMatchAt`, `this.lastRunTime`, `this.nextRunTime`, `this.runCount`, `this.updatedAt`

## Monitor.runMonitorCheck()
- 位置: async L441-567
- 役割: 会話を組み立て、必要ならベースラインを取り、監視対象ページを読み、JSON スキーマ付きで LLM に判定させる。結果は parseMonitorResult で解釈する。
- 触るとき: LLM に渡すプロンプトや応答スキーマを変えるとき、またはページ読み取りや推論の失敗がどのエラー分類になるかを追うとき。
- 呼び出し先: `ChromeUtils.now()`, `Promise.all()`, `String()`, `categorizeError()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `extractMonitorPageContent()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `makeJSONSchemaBlob()`, `now.toISOString()`, `openAIEngine.getFxAccountToken()`, `renderPrompt()`, `this.parseMonitorResult()`, `this.watchUrls.join()`, `throwIfAborted()`, `withAbortSignal()`
- 条件付き依存: `if (!initialSnapshot)` → `this.ensureInitialSnapshot()`
- 条件付き依存: `if (!initialSnapshot)` → `throwIfAborted()`
- 条件付き依存: `if (!initialSnapshot)` → `lazy.log.warn()`
- 条件付き依存: `if (runStats)` → `recordRunStart()`
- 条件付き依存: `if (runStats)` → `Math.round()`
- 条件付き依存: `if (runStats)` → `ChromeUtils.now()`
- 参照: `MODEL_FEATURES.AGENT_MONITOR`, `MONITOR_ERROR_CODES.MODEL`, `MONITOR_ERROR_CODES.PROMPT_LOAD`, `MONITOR_ERROR_CODES.UNKNOWN`, `conversation.engine?.model`, `error.message`, `initialSnapshot?.capturedAt`, `initialSnapshot?.pageContent`, `runStats.model`, `runStats.modelLatencyMs`, `this.initialSnapshot`, `this.monitorPrompt`, `this.watchUrls`

## Monitor.captureInitialSnapshot()
- 位置: async L582-618
- 役割: 監視対象ページの現在の内容を initialSnapshot として保存する。取得中に監視 URL が変わっていれば保存を拒否する。
- 触るとき: 変化検知の基準となるスナップショットの取り方や保存条件を変えるとき。
- 呼び出し先: `AbortSignal.any()`, `extractMonitorPageContent()`, `lazy.buildConversation()`, `new Date().toISOString()`, `throwIfAborted()`, `urlListsEqual()`
- 参照: `MODEL_FEATURES.AGENT_MONITOR`, `abortController.signal`, `this.#snapshotAbortController`, `this.id`, `this.initialSnapshot`, `this.watchUrls`

## Monitor.cancelSnapshotCapture()
- 位置: L625-630
- 役割: 進行中のスナップショット取得を中断し、待機中の参照も捨てる。
- 触るとき: 監視の定義を編集したときに、古い定義のスナップショットが新しい定義の基準にならないようにする処理を変えるとき。
- 呼び出し先: `this.#snapshotAbortController?.abort()`
- 参照: `this.#snapshotCapture`

## Monitor.ensureInitialSnapshot()
- 位置: async L641-658
- 役割: スナップショットがあれば返し、無ければ取得する。同時に来た呼び出しは同じ取得を待つ。
- 触るとき: スナップショットの取得が重複する問題や、取得待ちの扱いを調べるとき。
- 条件付き依存: `if (!this.#snapshotCapture)` → `this.captureInitialSnapshot({ conversation, signal, }).finally()`
- 条件付き依存: `if (!this.#snapshotCapture)` → `this.captureInitialSnapshot()`
- 参照: `this.#snapshotCapture`, `this.initialSnapshot`

## Monitor.scheduleNextRun()
- 位置: L664-690
- 役割: 既存のタイマーを解除し、次回実行時刻(最低 1 秒後)に run を予約する。無効または破棄済みなら何もしない。
- 触るとき: 定期実行の予約方法や無効化の条件を変えるとき。
- 呼び出し先: `Date.now()`, `Math.max()`, `Number.isNaN()`, `lazy.log.error()`, `nextRun.getTime()`, `this.clearTimer()`, `this.run()`
- 条件付き依存: `if (!nextRun || Number.isNaN(nextRun.getTime()))` → `this.schedule .getNextRunTime(this.lastRunTime) .toISOString()`
- 条件付き依存: `if (!nextRun || Number.isNaN(nextRun.getTime()))` → `this.schedule .getNextRunTime()`
- 参照: `lazy.ScheduledTask`, `this.#disposed`, `this.#timer`, `this.enabled`, `this.lastRunTime`, `this.nextRunTime`

## Monitor.getExpiryReason()
- 位置: L701-717
- 役割: 最長稼働期間を activeSince から、一致なし期間を activeSince と lastMatchAt の遅い方から測り、どの失効ルールに当たるかを返す。当たらなければ null。
- 触るとき: 自動停止の判定基準や起点の時刻を変えるとき。pref が 0 以下のルールは無効になる。
- 呼び出し先: `Date.parse()`, `Math.max()`, `Number.isFinite()`, `expiryRuleElapsed()`
- 参照: `MONITOR_EXPIRY_REASONS.MAX_AGE`, `MONITOR_EXPIRY_REASONS.NO_MATCH`, `this.activeSince`, `this.lastMatchAt`

## Monitor.parseMonitorResult()
- 位置: L726-756
- 役割: 応答から ```json の囲みを外して explanation と conditionMet を読む。形式が不正なら conditionMet を false にし、生テキストを説明文に使う。
- 触るとき: LLM の判定応答の形式を変えるとき、または条件が一致しないのに説明だけ出る原因を調べるとき。
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `fenced[1].trim()`, `parsed.explanation.trim()`, `raw.match()`, `response?.finalOutput?.trim()`
- 参照: `parsed.conditionMet`, `parsed.explanation`

## Monitor.toSerializable()
- 位置: L763-785
- 役割: 監視の状態を、呼び出し元や通知に渡せるよう値をコピーした平らなオブジェクトにする。
- 触るとき: 保存や通知の形式に新しいフィールドを足すとき。
- 呼び出し先: `this.history.map()`, `this.watchUrls.slice()`
- 参照: `this.activeSince`, `this.createdAt`, `this.enabled`, `this.expiry`, `this.id`, `this.initialSnapshot`, `this.lastMatchAt`, `this.lastRunTime`, `this.monitorPrompt`, `this.nextRunTime`, `this.notificationsMuted`, `this.runCount`, `this.schedule`, `this.title`, `this.updatedAt`

## Monitor.clearTimer()
- 位置: L787-792
- 役割: 予約済みの定期実行タイマーがあれば解除する。
- 触るとき: タイマー解除の漏れを調べるとき、または予約の取り消し処理を足すとき。
- 条件付き依存: `if (this.#timer)` → `this.#timer.disarm()`
- 参照: `this.#timer`

## Monitor.dispose()
- 位置: L799-813
- 役割: 監視を破棄状態にし、進行中の実行とスナップショット取得を中断してタイマーを解除する。errorCode で canceled か interrupted を決める。
- 触るとき: 監視の削除、一時停止、終了時の中断動作を変えるとき。
- 呼び出し先: `this.#abortController?.abort()`, `this.#snapshotAbortController?.abort()`, `this.clearTimer()`
- 参照: `MONITOR_ERROR_CODES.CANCELED`, `MONITOR_ERROR_CODES.INTERRUPTED`, `this.#disposed`

## Monitor.restore()
- 位置: L815-817
- 役割: 破棄状態を解除し、再び実行できるようにする。
- 触るとき: 破棄後に同じ監視を再開する経路を変えるとき。
- 参照: `this.#disposed`

## Monitor.addHistoryEntry()
- 位置: L819-824
- 役割: 履歴に 1 件追加し、上限(MAX_HISTORY_ENTRIES)を超えたら最も古い件を捨てる。
- 触るとき: 履歴の保持件数を変えるとき、または古い履歴が消える理由を調べるとき。
- 呼び出し先: `this.history.push()`
- 条件付き依存: `if (this.history.length > MAX_HISTORY_ENTRIES)` → `this.history.shift()`
- 参照: `this.history.length`

## Monitor.#finishRun()
- 位置: L826-834
- 役割: 実行中の状態を解除し、まだ有効で破棄されていなければ次回の予約をし直す。
- 触るとき: 実行の後始末や、実行後に次回予約が入らない問題を調べるとき。
- 条件付き依存: `if (!this.#disposed && this.enabled)` → `this.scheduleNextRun()`
- 参照: `this.#abortController`, `this.#disposed`, `this.#running`, `this.enabled`

## throwIfAborted()
- 位置: L839-847
- 役割: 中断シグナルが立っていれば、その理由を例外として投げる。
- 触るとき: 実行中の中断チェックを増やすとき、または中断理由が呼び出し元に届かない問題を調べるとき。
- 参照: `signal.reason`, `signal?.aborted`

## withAbortSignal()
- 位置: async L849-873
- 役割: promise と中断シグナルのうち先に決まった方で待つ。中断時は理由を例外として投げる。
- 触るとき: 中断に対応していない非同期呼び出しを、中断可能な形で待たせたいとき。
- 呼び出し先: `Promise.race()`, `signal.addEventListener()`, `signal.removeEventListener()`, `throwIfAborted()`

## onAbort()
- 位置: L858-864
- 役割: 中断が来たとき、理由の例外で待ちを reject する。
- 触るとき: 中断時に投げるエラーの内容を変えるとき。
- 呼び出し先: `reject()`
- 参照: `signal.reason`

## withTimeout()
- 位置: async L875-898
- 役割: promise と時限のどちらか先の方で待つ。時限が来たら TimeoutError を作って onTimeout を呼び、reject する。
- 触るとき: 監視の実行時間の上限を変えるとき、またはタイムアウトの扱いを追うとき。
- 呼び出し先: `Number.isFinite()`, `Promise.race()`, `lazy.setTimeout()`, `onTimeout()`, `reject()`
- 条件付き依存: `if (timeoutId)` → `lazy.clearTimeout()`
- 参照: `error.name`

## latestMatchTime()
- 位置: L900-902
- 役割: 履歴のうち条件一致した最新の checkedAt を返す。無ければ null。
- 触るとき: lastMatchAt が無い古い保存データの補完の仕方を変えるとき。
- 呼び出し先: `history.findLast()`
- 参照: `entry?.conditionMet`, `history.findLast(entry => entry?.conditionMet)?.checkedAt`

## expiryRuleDays()
- 位置: L911-918
- 役割: 失効ルールの日数を pref から返す。未知の理由ならログを出して 0 を返し、ルールは無効になる。
- 触るとき: 失効ルールの日数の決め方を変えるとき。
- 呼び出し先: `days()`
- 条件付き依存: `if (!days)` → `lazy.log.error()`

## expiryRuleElapsed()
- 位置: L920-923
- 役割: 失効ルールが有効で、起点から日数分の時間が過ぎたかを判定する。
- 触るとき: 失効の比較条件(以上か超えか)を変えるとき。
- 呼び出し先: `expiryRuleDays()`, `now.getTime()`

## normalizeLoadedHistory()
- 位置: L927-943
- 役割: 読み込んだ履歴のうち running のまま残っている件を、中断による error に直す。
- 触るとき: クラッシュや終了後に残った履歴の扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `history.map()`
- 参照: `MONITOR_ERROR_CODES.INTERRUPTED`, `entry?.status`

## monitorErrorCode()
- 位置: L956-967
- 役割: 失敗した実行のエラー分類を決める。タイムアウト、MonitorRunError の code、中断、それ以外の順に判定し、残りは categorizeError に任せる。
- 触るとき: history の errorCode や telemetry の error_code がなぜそう記録されたかを追うとき。
- 呼び出し先: `/abort/i.test()`, `categorizeError()`
- 参照: `MONITOR_ERROR_CODES.INTERRUPTED`, `MONITOR_ERROR_CODES.TIMEOUT`, `error.code`, `error?.message`, `error?.name`

## extractMonitorPageContent()
- 位置: async L969-997
- 役割: 監視対象 URL の本文を GetPageContent で読み、区切り線で連結する。1 件も読めなければ content_extraction_error で失敗させる。
- 触るとき: ページ本文の連結形式を変えるとき、または全ページ読めない場合の扱いを変えるとき。
- 呼び出し先: `lazy.GetPageContent.getPageContent()`, `results .map()`, `results .map(result => result.content) .join()`, `results.some()`, `throwIfAborted()`, `withAbortSignal()`
- 参照: `MONITOR_ERROR_CODES.CONTENT_EXTRACTION`, `result.content`, `result.ok`

## urlListsEqual()
- 位置: L999-1001
- 役割: 2 つの URL 配列が同じ長さで同じ順序かを比べる。
- 触るとき: 監視の URL 変更検知の条件を変えるとき。
- 呼び出し先: `a.every()`
- 参照: `a.length`, `b.length`

## trimAndFilterWatchUrls()
- 位置: L1003-1013
- 役割: URL 前後の空白を除き、http と https のみ残す。件数が上限を超えたら例外を投げる。
- 触るとき: 監視できる URL の上限や許可するプロトコルを変えるとき。
- 呼び出し先: `Array.isArray()`, `String()`, `String(url ?? "").trim()`, `urls.map()`, `urls.map(url => String(url ?? "").trim()).filter()`
- 参照: `urls.length`

## isAllowedWatchUrl()
- 位置: L1015-1018
- 役割: URL が解析でき、http または https なら true を返す。
- 触るとき: 監視に登録できる URL の条件を変えるとき。
- 呼び出し先: `URL.parse()`, `["http:", "https:"].includes()`
- 参照: `url.protocol`

## scheduledRunDelayMs()
- 位置: L1020-1029
- 役割: 手動実行なら null、定期実行なら予定時刻から実際の開始時刻までの遅れをミリ秒で返す。
- 触るとき: 遅延実行の判定や telemetry の delay の値を追うとき。
- 呼び出し先: `Date.parse()`, `Math.max()`, `Number.isFinite()`, `checkedAt.getTime()`

## getRunReason()
- 位置: L1031-1038
- 役割: 手動なら manual、遅れが閾値(5 分)以上なら delayed、それ以外は trigger_time を返す。
- 触るとき: 実行理由の分類を変えるとき、または遅延の閾値を調整するとき。
- 参照: `RUN_REASONS.DELAYED`, `RUN_REASONS.MANUAL`, `RUN_REASONS.TRIGGER_TIME`

## getCancelCode()
- 位置: L1044-1057
- 役割: 中断理由が、履歴に記録したエラーと同じ canceled または interrupted のときだけそのコードを返す。完了後の破棄では null。
- 触るとき: キャンセル扱いと完了扱いの境界を変えるとき。
- 呼び出し先: `[ MONITOR_ERROR_CODES.CANCELED, MONITOR_ERROR_CODES.INTERRUPTED, ].includes()`
- 参照: `MONITOR_ERROR_CODES.CANCELED`, `MONITOR_ERROR_CODES.INTERRUPTED`, `abortReason.code`

## buildRunTelemetryExtra()
- 位置: L1059-1065
- 役割: 監視の共通情報に reason と execution_seq を足した telemetry の extra を作る。
- 触るとき: 実行系 telemetry に共通で載せる項目を増やすとき。
- 呼び出し先: `lazy.MonitorAgent._telemetryExtra()`

## recordRunRequest()
- 位置: L1067-1073
- 役割: 実行要求の telemetry を記録する。遅延があれば delay も付ける。
- 触るとき: 要求時点の telemetry 項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionExecuteRequest.record()`, `buildRunTelemetryExtra()`
- 参照: `extra.delay`, `runStats.delayMs`

## recordRunStart()
- 位置: L1075-1081
- 役割: 推論を始めたときの telemetry を記録する。モデル名が分かれば付ける。
- 触るとき: 開始時の telemetry 項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionExecuteStart.record()`, `buildRunTelemetryExtra()`
- 参照: `extra.model`, `runStats.model`

## recordRunEnd()
- 位置: L1083-1125
- 役割: 実行の終わりを telemetry に記録する。キャンセルなら cancel、それ以外は complete とし、成否、結果、遅延、遅延時間を付ける。
- 触るとき: 終了時の telemetry の種類や項目を変えるとき、または成功と失敗の集計がずれる原因を調べるとき。
- 呼び出し先: `Glean.smartWindow.agenticActionExecuteComplete.record()`, `buildRunTelemetryExtra()`
- 条件付き依存: `if (cancelCode)` → `Glean.smartWindow.agenticActionExecuteCancel.record()`
- 参照: `completeExtra.delay`, `completeExtra.error_code`, `completeExtra.latency`, `completeExtra.outcome`, `extra.duration`, `extra.model`

## monitorAgeMs()
- 位置: L1133-1136
- 役割: 監視の作成時刻(または指定時刻)からの経過ミリ秒を返す。解析できなければ 0。
- 触るとき: 監視の経過時間を表示や判定に使うとき。
- 呼び出し先: `Date.now()`, `Date.parse()`, `Math.max()`, `Number.isFinite()`
- 参照: `monitor.createdAt`

## categorizeError()
- 位置: L1147-1187
- 役割: エラーを HTTP ステータス、次にメッセージの語句で安全なエラーコードに分類する。生のメッセージは返さない。
- 触るとき: 新しいエラー種別を telemetry に載せるとき、または分類されずに unknown_error になる例外を調べるとき。
- 呼び出し先: `(error?.message ?? String(error)).toLowerCase()`, `Number()`, `String()`, `message.includes()`, `message.match()`, `patterns.some()`
- 参照: `MONITOR_ERROR_CODES.AUTH`, `MONITOR_ERROR_CODES.MODEL`, `MONITOR_ERROR_CODES.RATE_LIMIT`, `MONITOR_ERROR_CODES.TIMEOUT`, `error.status`, `error?.message`, `error?.status`
