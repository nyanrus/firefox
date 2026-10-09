# browser/components/aiwindow/ui/modules/SmartFormFillReviewSession.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillReviewSession.sys.mjs
source-hash: ff1e214447c6f87d5a1b4a1112ced941067d009a
lines: 242

## <module>
- 役割: Smart Form Fill のレビューダイアログ 1 回分を管理し、生成結果の受け渡しと、利用者の操作 (埋める・止める・閉じる) の検証を担う。
- 呼び出し先: `Promise.withResolvers()`

## SmartFormFillReviewSession.constructor()
- 位置: L71-77
- 役割: 対象のブラウザ、親のウィンドウ、各種コールバックを受け取って保持する。
- 触るとき: レビューセッションに新しいコールバックや依存を足すとき。
- 参照: `this.#browser`, `this.#chromeWindow`, `this.#onCancelGeneration`, `this.#onClose`, `this.#onFill`

## SmartFormFillReviewSession.generationPending()
- 位置: L84-86
- 役割: 値の生成がまだ完了を待っているかを返す。
- 触るとき: 生成中の表示や、生成結果を受け付けてよいかの判断を調べるとき。
- 参照: `this.#generationPending`

## SmartFormFillReviewSession.open()
- 位置: async L94-123
- 役割: レビュー用のタブダイアログを開き、UI の初期化完了を待つ。既に閉じているか開いていれば false を返す。
- 触るとき: レビュー画面が開かない、または初期化で止まる問題を追うとき。
- 呼び出し先: `this.#chromeWindow.gBrowser .getTabDialogBox()`, `this.#chromeWindow.gBrowser .getTabDialogBox(this.#browser) .open()`, `this.#waitForClose()`
- 参照: `this.#browser`, `this.#closed`, `this.#dialog`, `this.#generationResult.promise`, `this.#ready.promise`

## onReady()
- 位置: L101-101
- 役割: ダイアログの UI が初期化できたことを知らせ、open() の待ちを true で完了させる。
- 触るとき: レビュー画面の起動完了の通知経路を変えるとき。
- 呼び出し先: `this.#ready.resolve()`

## onAction()
- 位置: L102-102
- 役割: ダイアログからの操作を #handleAction に渡す。
- 触るとき: レビュー画面の操作を受け付ける入口を変えるとき。
- 呼び出し先: `this.#handleAction()`

## SmartFormFillReviewSession.completeGeneration()
- 位置: L132-147
- 役割: 生成された候補か生成エラーをダイアログに渡し、生成済みの項目 ID を記録する。待機中でなければ何もしない。
- 触るとき: 生成結果がダイアログに届かない、または受け付けられた項目だけを埋める仕組みを調べるとき。
- 呼び出し先: `Array.isArray()`, `this.#generationResult.resolve()`
- 条件付き依存: `if (Array.isArray(result.fields))` → `this.#generatedFieldIds.add()`
- 参照: `result.fields`, `this.#closed`, `this.#generationPending`

## SmartFormFillReviewSession.abort()
- 位置: L154-162
- 役割: セッションを閉じた扱いにして、生成を中止し、ダイアログを中止する。
- 触るとき: レビューを途中で閉じた後に生成や画面が残る問題を追うとき。
- 呼び出し先: `this.#cancelGeneration()`, `this.#dialog?.abort()`
- 参照: `this.#closed`

## SmartFormFillReviewSession.#handleAction()
- 位置: async L171-199
- 役割: 停止の操作にはキャンセル結果を返す。埋める操作は、生成済みで文字列の値だけを #onFill に渡す。それ以外は失敗の結果を返す。
- 触るとき: ダイアログの操作の種類を増やす、または埋める値の検証条件を変えるとき。
- 呼び出し先: `Array.isArray()`, `action.fields.filter()`, `this.#generatedFieldIds.has()`, `this.#onFill()`
- 条件付き依存: `if (action.type === FORM_REVIEW_ACTIONS.STOP)` → `this.#cancelGeneration()`
- 参照: `FORM_REVIEW_ACTIONS.FILL_FORM`, `FORM_REVIEW_ACTIONS.STOP`, `action.fields`, `action.type`, `this.#closed`

## SmartFormFillReviewSession.#cancelGeneration()
- 位置: L206-216
- 役割: 生成待ちを一度だけ終わらせ、中止のコールバックを呼んで、結果の Promise を AbortError で拒否する。
- 触るとき: 生成のキャンセルが二重に起きる、または中止の通知が届かない問題を追うとき。
- 呼び出し先: `this.#generationResult.reject()`, `this.#onCancelGeneration()`
- 参照: `this.#generationPending`

## SmartFormFillReviewSession.#waitForClose()
- 位置: async L226-240
- 役割: ダイアログが閉じるのを待ち、閉じたら準備の Promise を false で完了させ、生成を中止して閉じた状態にし、onClose を呼ぶ。
- 触るとき: 閉じた後の後始末 (参照の解放や onClose の呼び出し) を変えるとき。
- 呼び出し先: `this.#cancelGeneration()`, `this.#onClose()`, `this.#ready.resolve()`
- 参照: `this.#closed`, `this.#dialog`
