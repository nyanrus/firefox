# browser/components/aiwindow/ui/content/smartformfill-form-review.mjs

source: browser/components/aiwindow/ui/content/smartformfill-form-review.mjs
source-hash: dc218c9b7980343b03c98cb296a3e98d7fe9b9aa
lines: 230

## <module>
- 役割: スマートフォーム入力の確認ダイアログの殻を作り、隔離された確認ページの表示と操作の受け渡しを行う
- 呼び出し先: `addEventListener()`, `closeDialog()`, `console.error()`, `dialogBox.classList.add()`, `dialogBox.classList.remove()`, `dialogBox.removeAttribute()`, `dialogBox.setAttribute()`, `dialogBrowser.closest()`, `document.querySelector()`, `initialize()`, `initialize().catch()`, `removeEventListener()`

## closeDialog()
- 位置: L63-70
- 役割: 一度だけ window.close() を呼んでダイアログを閉じる
- 触るとき: 閉じる経路が二重に動く問題や、閉じ方を変えるとき
- 呼び出し先: `window.close()`

## handleAction()
- 位置: async L79-99
- 役割: 確認ページからの操作を種類別に処理する(入力は onAction へ転送、停止は転送後に閉じ、取消と閉じるは即閉じる)
- 触るとき: 確認画面のボタンごとの挙動を変えるとき、新しい操作種別を足すとき
- 呼び出し先: `closeDialog()`, `dialogArguments.onAction()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `FORM_REVIEW_ACTIONS.CLOSE`, `FORM_REVIEW_ACTIONS.FILL_FORM`, `FORM_REVIEW_ACTIONS.STOP`, `action.type`

## showGenerationResult()
- 位置: async L106-119
- 役割: 生成結果の候補、または生成エラーを確認ページに表示し、表示できなければダイアログを閉じる
- 触るとき: 生成失敗時の表示や、候補が表示されずに閉じてしまう問題を調べるとき
- 呼び出し先: `Array.isArray()`, `reviewActor.showGenerationError()`, `reviewActor.showSuggestions()`
- 条件付き依存: `if (!displayed)` → `closeDialog()`
- 参照: `dialogArguments.generationResult`, `result.fields`, `result?.errorType`, `result?.fields`

## handleKeydown()
- 位置: L128-134
- 役割: Escape で入力せずにダイアログを閉じる
- 触るとき: キー操作での閉じ方や伝播の扱いを変えるとき
- 条件付き依存: `if (event.key === "Escape")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape")` → `event.stopPropagation()`
- 条件付き依存: `if (event.key === "Escape")` → `closeDialog()`
- 参照: `event.key`

## createReviewBrowser()
- 位置: L141-154
- 役割: about:smartformfillreview を privilegedabout の隔離ブラウザ要素として作る
- 触るとき: 生成された値をページ内容から隔離する設定(プロセスの種類など)を変えるとき
- 呼び出し先: `browser.setAttribute()`, `document.createXULElement()`
- 参照: `browser.id`

## initialize()
- 位置: async L161-203
- 役割: 隔離ブラウザを読み込み、ready 通知を待って actor を接続し、初期化できたら onReady と結果表示を行う
- 触るとき: 確認画面の起動手順や、初期化失敗時の扱いを追うとき
- 呼び出し先: `container.append()`, `createReviewBrowser()`, `dialogArguments.onReady()`, `reviewActor.connect()`, `reviewActor.initialize()`, `reviewBrowser.addEventListener()`, `reviewBrowser.browsingContext.currentWindowGlobal.getActor()`, `showGenerationResult()`, `showGenerationResult().catch()`
- 条件付き依存: `if (reviewBrowser.currentURI.spec !== REVIEW_URL)` → `closeDialog()`
- 条件付き依存: `if (!initialized)` → `closeDialog()`
- 条件付き依存: `if (!closing)` → `console.error()`
- 条件付き依存: `if (!closing)` → `closeDialog()`
- 参照: `document.subDialogSetDefaultFocus`, `reviewBrowser.currentURI.spec`

## document.subDialogSetDefaultFocus()
- 位置: L177-177
- 役割: ダイアログの既定フォーカスを隔離ブラウザへ移す
- 触るとき: ダイアログを開いた直後のフォーカス位置を変えるとき
- 呼び出し先: `reviewBrowser.focus()`
