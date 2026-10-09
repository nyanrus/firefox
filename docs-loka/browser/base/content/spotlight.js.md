# browser/base/content/spotlight.js

source: browser/base/content/spotlight.js
source-hash: 3de411aa5fbaf87c21e02bcd61972ebedd1eb069
lines: 154

## <module>
- 役割: スポットライト(about:welcome 形式のダイアログ)のサブダイアログ側スクリプト。CONFIG に従って多段階メッセージを描画し、ウィンドウに AW 系の関数を公開する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `document.addEventListener()`, `renderMultistage()`

## addStylesheet()
- 位置: L14-18
- 役割: 文書の head に link 要素を追加して、指定の stylesheet を読み込む。
- 触るとき: スポットライトの見た目が about:welcome と揃わないときに、読み込む CSS を確かめるときに見る。
- 呼び出し先: `document.createElement()`, `document.head.appendChild()`
- 参照: `link.href`, `link.rel`

## disableEscClose()
- 位置: L20-27
- 役割: ウィンドウの keydown で Escape を検出し、既定動作と伝播を止める。
- 触るとき: CONFIG の disableEscClose で Esc が効かない、または効きすぎるときに見る。
- 呼び出し先: `addEventListener()`
- 条件付き依存: `if (event.key === "Escape")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape")` → `event.stopPropagation()`
- 参照: `event.key`

## renderMultistage()
- 位置: L32-142
- 役割: AboutWelcomeParent を作り、window に AW 関数群を公開し、ダイアログの見た目を整えてバンドルの script を読み込み、最後に ready を呼ぶ。
- 触るとき: スポットライトの表示内容や telemetry の page 名、ダイアログのサイズ指定を変えるとき、またはバンドルが描画されないときに見る。
- 呼び出し先: `addEventListener()`, `addStylesheet()`, `box.classList.add()`, `box.classList.remove()`, `box.closest()`, `box.removeAttribute()`, `box.setAttribute()`, `browser.closest()`, `dialog?.classList.add()`, `dialog?.classList.remove()`, `document.body.classList.add()`, `document.createElement()`, `document.head.appendChild()`, `ready()`, `receive()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `disableEscClose()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `browser.documentGlobal.addEventListener()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `addEventListener()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `browser.documentGlobal.removeEventListener()`
- 参照: `CONFIG?.disableEscClose`, `document.body.dataset.page`, `document.body.id`, `document.head.appendChild(document.createElement("script")).src`, `window.AWAddScreenImpression`, `window.AWEvaluateAttributeTargeting`, `window.AWEvaluateScreenTargeting`, `window.AWFinish`, `window.AWGetFeatureConfig`, `window.AWGetInstalledAddons`, `window.AWGetSelectedTheme`, `window.AWPredictRemoteType`, `window.AWSelectTheme`, `window.AWSendEventTelemetry`, `window.AWSendToDeviceEmailsSupported`, `window.AWSendToParent`, `window.AWWaitForMigrationClose`, `window.AWWaitForNimbus`

## receive()
- 位置: L34-35
- 役割: 名前から AWPage:<name> のメッセージを作り、AWParent.onContentMessage に渡す関数を返す。
- 触るとき: 新しい AW 用メッセージを追加するとき、またはどのメッセージ名が親に届くかを調べるときに見る。
- 呼び出し先: `AWParent.onContentMessage()`

## window.AWGetFeatureConfig()
- 位置: L38-38
- 役割: バンドル側が呼ぶ AWGetFeatureConfig を、CONFIG を返す関数として公開する。
- 触るとき: バンドルが設定を読めない、または CONFIG の参照先を変えたいときに見る。

## window.AWSelectTheme()
- 位置: L41-41
- 役割: テーマ名を大文字にして SELECT_THEME メッセージとして親へ送る。
- 触るとき: テーマ選択が保存されない、または大文字化の扱いを変えるときに見る。
- 呼び出し先: `data?.toUpperCase()`, `receive()`, `receive("SELECT_THEME")()`

## window.AWSendEventTelemetry()
- 位置: L44-72
- 役割: metrics が block なら送らず、microsurvey では feedbackData を付けてから TELEMETRY_EVENT を親へ送る。
- 触るとき: telemetry が出ない、または microsurvey のフィードバックが期待どおりに付かないときに見る。
- 呼び出し先: `telemetryMessageHandler()`
- 参照: `CONFIG.feedbackData`, `CONFIG?.feedbackData`, `CONFIG?.metrics`, `CONFIG?.write_in_microsurvey`, `data.event`, `data.event_context`, `data.event_context.contentToggleState`, `data.event_context.smart_window_user_feedback_data`, `data.event_context.source`, `data.event_context.write_in_microsurvey`, `feedbackDataToSend.chat`

## window.AWSendToParent()
- 位置: L77-77
- 役割: 任意の名前でメッセージを親へ送る。
- 触るとき: バンドルから親への新しいメッセージを処理させるときに見る。
- 呼び出し先: `receive()`, `receive(name)()`

## window.AWFinish()
- 位置: L78-80
- 役割: window.close() を呼び、スポットライトを閉じる。
- 触るとき: 完了ボタンを押しても閉じない、または閉じるタイミングを変えたいときに見る。
- 呼び出し先: `window.close()`

## window.AWPredictRemoteType()
- 位置: L85-87
- 役割: 渡された url に対して ChromeUtils.predictRemoteTypeForURI を呼び、その結果の remote type を返す。
- 触るとき: スポットライトで開く URL のプロセス割り当てを確かめるときに見る。
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`

## preventEscape()
- 位置: L116-124
- 役割: dialog またはボックス内にフォーカスがある Escape の keydown を、システムグループの段階で止める。
- 触るとき: ダイアログ枠にフォーカスがあるときに ESC で閉じてしまう問題を調べるとき、または伝播を止める対象を変えるときに見る。
- 呼び出し先: `box.contains()`, `dialog?.contains()`
- 条件付き依存: `if ( event.key === "Escape" && (dialog?.contains(event.target) || box.contains(event.target)) )` → `event.preventDefault()`
- 条件付き依存: `if ( event.key === "Escape" && (dialog?.contains(event.target) || box.contains(event.target)) )` → `event.stopPropagation()`
- 参照: `event.key`, `event.target`
