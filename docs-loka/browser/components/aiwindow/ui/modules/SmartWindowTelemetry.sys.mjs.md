# browser/components/aiwindow/ui/modules/SmartWindowTelemetry.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartWindowTelemetry.sys.mjs
source-hash: 768d54783b683ca4b41e0561b15b843039660add
lines: 224

## <module>
- 役割: AI Window のテレメトリのうち、状態を共有する必要がある計測を扱う。設定値の変化の反映、クライアント側のエラーの記録、URL 読込の記録を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `SmartWindowTelemetry.updateEnabledMetric()`, `SmartWindowTelemetry.updateMemoriesFromConversationMetric()`, `SmartWindowTelemetry.updateMemoriesFromHistoryMetric()`, `SmartWindowTelemetry.updateModelMetric()`, `SmartWindowTelemetry.updateSetDefaultOptinMetric()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## init()
- 位置: L81-92
- 役割: 一度だけ、モデル・記憶・既定ウィンドウ・有効状態の各計測値を Glean に反映する。
- 触るとき: 起動時に送られる計測値の一覧を変えるとき。
- 呼び出し先: `this.updateEnabledMetric()`, `this.updateMemoriesFromConversationMetric()`, `this.updateMemoriesFromHistoryMetric()`, `this.updateModelMetric()`, `this.updateModelMetric().catch()`, `this.updateSetDefaultOptinMetric()`
- 参照: `console.error`, `this._initialized`

## updateMemoriesFromConversationMetric()
- 位置: L94-99
- 役割: 会話からの記憶生成の設定値を Glean の計測に書き込む。
- 触るとき: 会話からの記憶生成のオプトイン計測がずれて見えるとき。
- 呼び出し先: `Glean.smartWindow.memoriesOptin.generate_from_conversation.set()`
- 参照: `lazy.memoriesFromConversation`

## updateMemoriesFromHistoryMetric()
- 位置: L101-106
- 役割: 履歴からの記憶生成の設定値を Glean の計測に書き込む。
- 触るとき: 履歴からの記憶生成のオプトイン計測がずれて見えるとき。
- 呼び出し先: `Glean.smartWindow.memoriesOptin.generate_from_history.set()`
- 参照: `lazy.memoriesFromHistory`

## updateSetDefaultOptinMetric()
- 位置: L108-110
- 役割: 既定ウィンドウとして使う設定値を Glean の計測に書き込む。
- 触るとき: 既定ウィンドウのオプトイン計測を確かめるとき。
- 呼び出し先: `Glean.smartWindow.setDefaultOptin.set()`
- 参照: `lazy.isDefaultWindow`

## updateEnabledMetric()
- 位置: L112-114
- 役割: AI Window の有効状態を Glean の計測に書き込む。
- 触るとき: 有効状態の計測が設定と食い違うとき。
- 呼び出し先: `Glean.smartWindow.enabled.set()`
- 参照: `lazy.smartWindowEnabled`

## updateModelMetric()
- 位置: async L116-119
- 役割: 選択されたモデル設定からモデル情報を解決し、名前を Glean に書き込む。解決できなければ unset にする。
- 触るとき: モデルの計測値が unset になるとき、またはモデルの選び方を変えるとき。
- 呼び出し先: `Glean.smartWindow.model.set()`, `lazy.getModelForChoice()`
- 参照: `lazy.modelChoice`, `modelInfo?.model`

## recordClientError()
- 位置: L142-147
- 役割: 捕捉された任意の値から名前や発生箇所などを抜き出して、エラー計測の詳細の形で記録する。
- 触るとき: クライアント側の例外を新たに計測に入れるとき。呼び出し側で値を整える必要はない。
- 呼び出し先: `extractClientErrorFields()`, `this.recordClientErrorDetail()`

## recordClientErrorDetail()
- 位置: L160-199
- 役割: 別プロセスから届いたエラーの詳細を検証し、未知の発生元は uncaught に分類する。同じ組み合わせは 20 回まで記録し、その後は捨てる。
- 触るとき: エラー計測の重複抑止の上限や、発生元の分類を変えるとき。大量に記録される不具合の抑え方を見るときにも使う。
- 呼び出し先: `CLIENT_ERROR_SOURCES.has()`, `Glean.smartWindow.clientError.record()`, `Number.isFinite()`, `asString()`, `clientErrorEmitCounts.get()`, `clientErrorEmitCounts.set()`, `normalizeClientErrorMessage()`
- 条件付き依存: `if (!CLIENT_ERROR_SOURCES.has(source))` → `console.warn()`
- 条件付き依存: `if (!CLIENT_ERROR_SOURCES.has(source))` → `JSON.stringify()`
- 参照: `context.chat_id`, `context.location`, `context.message_seq`, `context.model`, `detail.lineno`, `detail?.filename`, `detail?.lineno`, `detail?.message`, `detail?.messageKey`, `detail?.name`, `detail?.source`

## _resetClientErrorDedupForTests()
- 位置: L201-203
- 役割: テスト用に、エラー計測の重複数の記録を空にする。
- 触るとき: エラー計測の上限のテストが前のテストの影響を受けるとき。
- 呼び出し先: `clientErrorEmitCounts.clear()`

## recordUriLoad()
- 位置: async L205-222
- 役割: 1 時間に 1 回だけ、モデル名を添えた URI 読込の計測を記録する。記録したら true を返す。
- 触るとき: URI 読込の計測の頻度を変えるとき、またはその計測が増えすぎないかを確かめるとき。
- 呼び出し先: `Date.now()`, `Glean.smartWindow.uriLoad.record()`, `lazy.getModelForChoice()`
- 参照: `lazy.modelChoice`, `modelInfo?.model`, `this.lastUriLoadTimestamp`
