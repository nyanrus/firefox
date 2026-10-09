# browser/components/aiwindow/ui/modules/ClientErrorTelemetry.mjs

source: browser/components/aiwindow/ui/modules/ClientErrorTelemetry.mjs
source-hash: 2a2a3bee94b6ada13d29f9cfbeaf86d495d94268
lines: 244

## <module>
- 役割: スマートウィンドウ UI のエラーを client_error イベントとして記録するための共通の語彙と補助関数。chrome 側と about:aichatcontent 側の両方で使う。

## asString()
- 位置: L69-71
- 役割: 値が文字列ならそのまま返し、それ以外は空文字を返す。
- 触るとき: エラーの項目を読むとき、文字列でない値が来ても例外にしたくないとき。

## extractClientErrorFields()
- 位置: L83-96
- 役割: 投げられた任意の値から name・message・ファイル名・行番号を取り出す。文字列や非オブジェクトも扱う。
- 触るとき: エラーイベントの項目名を変えるとき、またはプロセス間で項目が欠ける問題を調べるとき。
- 呼び出し先: `Number.isFinite()`, `asString()`
- 参照: `error.fileName`, `error.lineNumber`, `error.message`, `error.name`

## normalizeClientErrorMessage()
- 位置: L112-143
- 役割: 失敗を定められたメッセージ key のどれかに対応づける。生の例外文は返さない。
- 触るとき: 新しいエラーの分類を増やすとき、または多くの失敗が runtime_error に落ちる問題を調べるとき。
- 呼び出し先: `asString()`, `asString(message).toLowerCase()`, `text.includes()`
- 条件付き依存: `if (key)` → `CLIENT_ERROR_MESSAGES.has()`
- 条件付き依存: `if (key)` → `console.warn()`
- 条件付き依存: `if (key)` → `JSON.stringify()`

## classifyClientErrorSource()
- 位置: L152-158
- 役割: スタックに lit.all.mjs を含むエラーを lit-render、それ以外を uncaught に分類する。
- 触るとき: Lit の描画エラーが汎用のエラーに混ざる問題を調べるとき。
- 呼び出し先: `error.stack.includes()`
- 参照: `error.stack`

## installClientErrorListeners()
- 位置: L171-202
- 役割: ウィンドウの error と unhandledrejection を購読し、報告関数へ渡す。解除関数を返す。
- 触るとき: エラー報告の購読先やタイミングを変えるとき。
- 呼び出し先: `target.addEventListener()`, `target.removeEventListener()`

## reportSafely()
- 位置: L172-179
- 役割: 報告処理の中の例外が別の失敗を生まないよう握りつぶし、警告を出す。
- 触るとき: 報告処理そのものが失敗したときに何が見えるかを変えるとき。
- 呼び出し先: `classifyClientErrorSource()`, `console.warn()`, `report()`

## onError()
- 位置: L180-192
- 役割: error イベントを報告する。error が null なら、イベントの項目から組み立てて報告する。
- 触るとき: error イベントの値が空で報告が欠ける問題を調べるとき。
- 呼び出し先: `reportSafely()`
- 参照: `event.error`, `event.filename`, `event.lineno`, `event.message`

## onUnhandledRejection()
- 位置: L193-193
- 役割: 未処理の Promise 拒否の理由を報告する。
- 触るとき: 未処理の拒否が記録されない問題を調べるとき。
- 呼び出し先: `reportSafely()`
- 参照: `event.reason`

## serializeClientErrorDetail()
- 位置: L216-218
- 役割: source と messageKey に、エラーの項目を合わせた詳細オブジェクトを作る。
- 触るとき: 親プロセスへ送る項目を増やすとき。
- 呼び出し先: `extractClientErrorFields()`

## dispatchClientError()
- 位置: L229-243
- 役割: 同じエラーは一度だけ、bubbles と composed を付けた client-error イベントとして発火する。
- 触るとき: コンテンツ文書から親プロセスへエラーを送る経路を変えるとき。
- 呼び出し先: `serializeClientErrorDetail()`, `target.dispatchEvent()`
- 条件付き依存: `if (error && typeof error === "object")` → `reportedErrors.has()`
- 条件付き依存: `if (error && typeof error === "object")` → `reportedErrors.add()`
