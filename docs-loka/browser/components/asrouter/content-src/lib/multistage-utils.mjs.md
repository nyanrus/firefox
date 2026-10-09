# browser/components/asrouter/content-src/lib/multistage-utils.mjs

source: browser/components/asrouter/content-src/lib/multistage-utils.mjs
source-hash: 42b9a7b9ec455b6eda37e7fec0de333c4a7732ed
lines: 130

## <module>
- 役割: about:welcome、Spotlight、Feature Callout などのマルチステージ画面で、親への送信・テレメトリ・スタイル検証を行う共通関数群。
- 呼び出し先: `document.querySelector()`

## handleUserAction()
- 位置: L14-16
- 役割: ボタン操作を SPECIAL_ACTION として親プロセスへ送る。
- 触るとき: 画面のボタン操作が親に届かないとき、または操作の種類を増やすとき。
- 呼び出し先: `window.AWSendToParent()`

## handleImpressionAction()
- 位置: L17-31
- 役割: 表示アクションを親へ送り、実行された場合だけ IMPRESSION_ACTION のアクションテレメトリを送る。
- 触るとき: 表示時のアクションが記録されない、または二重に記録されると調べるとき。
- 呼び出し先: `Promise.resolve()`, `Promise.resolve( window.AWSendImpressionAction?.({ action, message_id: messageId, screen_id: screenId, }) ).then()`, `window.AWSendImpressionAction()`
- 条件付き依存: `if (fired)` → `this.sendActionTelemetry()`
- 参照: `action.type`

## sendImpressionTelemetry()
- 位置: L32-41
- 役割: 表示の IMPRESSION テレメトリを、ページ種別を加えて送る。
- 触るとき: 表示イベントの event_context の項目を変えるとき。
- 呼び出し先: `window.AWSendEventTelemetry()`

## sendActionTelemetry()
- 位置: L42-58
- 役割: クリックなどの操作を、source と page を付けたテレメトリとして送る。既定イベントは CLICK_BUTTON。
- 触るとき: クリック系テレメトリの項目や既定イベント名を変えるとき。
- 呼び出し先: `window.AWSendEventTelemetry()`

## sendDismissTelemetry()
- 位置: L59-65
- 役割: 閉じる操作の DISMISS テレメトリを送る。ただし spotlight では既に独自に送るため送らない。
- 触るとき: Spotlight で閉じるイベントが二重に計測される、または欠けると調べるとき。
- 条件付き依存: `if (page !== "spotlight")` → `this.sendActionTelemetry()`

## fetchFlowParams()
- 位置: async L66-82
- 役割: metricsFlowUri から deviceId、flowId、flowBeginTime を取得する。失敗時は null を返す。
- 触るとき: 計測フローのパラメータ取得や失敗時の扱いを変えるとき。
- 呼び出し先: `fetch()`
- 条件付き依存: `if (response.status === 200)` → `response.json()`
- 条件付き依存: `if (!(response.status === 200))` → `console.error()`
- 参照: `response.status`

## sendEvent()
- 位置: L83-90
- 役割: AWPage:種別 という名前のカスタムイベントを、バブリングする形で document に発火する。
- 触るとき: ページ内のコンポーネントへ通知するイベント名を追加するとき。
- 呼び出し先: `document.dispatchEvent()`

## getLoadingStrategyFor()
- 位置: L91-93
- 役割: URL が http で始まる場合は lazy、それ以外は eager の読み込み方式を返す。
- 触るとき: 画像の読み込み方式の判定を変えるとき。
- 呼び出し先: `url?.startsWith()`

## handleCampaignAction()
- 位置: L94-105
- 役割: キャンペーンアクションを親へ送り、処理された場合だけ CAMPAIGN_ACTION のクリック計測を送る。
- 触るとき: キャンペーンのクリック計測が出ない、または多く出ると調べるとき。
- 呼び出し先: `window.AWSendToParent()`, `window.AWSendToParent("HANDLE_CAMPAIGN_ACTION", action).then()`
- 条件付き依存: `if (handled)` → `this.sendActionTelemetry()`

## getValidStyle()
- 位置: L106-118
- 役割: 許可されたスタイルのキーだけを残す。allowVars が真なら CSS 変数(--)も残す。
- 触るとき: 画面に許可するスタイルのプロパティを増やすとき、またはスタイルが消える原因を調べるとき。
- 呼び出し先: `Object.keys()`, `Object.keys(style) .filter()`, `Object.keys(style) .filter( key => validStyles.includes(key) || (allowVars && key.startsWith("--")) ) .reduce()`, `key.startsWith()`, `validStyles.includes()`

## getTileStyle()
- 位置: L119-128
- 役割: tile.style を優先し、なければ旧形式の tiles.style を使い、検証済みのスタイルを返す。
- 触るとき: タイルのスタイル指定の互換性を変えるとき。
- 呼び出し先: `this.getValidStyle()`
- 参照: `tile?.style`, `tile?.tiles?.style`
