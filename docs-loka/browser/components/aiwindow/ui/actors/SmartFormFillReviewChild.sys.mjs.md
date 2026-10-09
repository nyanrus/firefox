# browser/components/aiwindow/ui/actors/SmartFormFillReviewChild.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillReviewChild.sys.mjs
source-hash: 4209ce623c7906a4ae3e0af003d102c8eaf3e67a
lines: 260

## <module>
- 役割: Smart Form Fill の確認ダイアログ(ai-sff-form-review)側の子アクター。親からの状態更新を反映し、ユーザー操作を親へ送る。

## SmartFormFillReviewChild.actorCreated()
- 位置: L36-38
- 役割: コンテンツウィンドウに keydown のリスナーを付け、Escape を捕まえられるようにする。
- 触るとき: 確認ダイアログで Escape が効かないときに見る。
- 呼び出し先: `this.contentWindow.addEventListener()`

## SmartFormFillReviewChild.didDestroy()
- 位置: L45-47
- 役割: 破棄済みフラグを立て、以後の操作と結果表示を止める。
- 触るとき: ダイアログを閉じた後に古い結果が表示される、または送信が続くときに見る。
- 参照: `this.#destroyed`

## SmartFormFillReviewChild.receiveMessage()
- 位置: async L71-113
- 役割: 親からの Initialize、ShowSuggestions、ShowGenerationError を受けて ai-sff-form-review の状態(進行中、確認、最終)を切り替える。不正な値は false を返し、未知の名前は例外にする。
- 触るとき: 確認画面の表示が親の状態と合わないとき、または親から新しい状態を追加するときに見る。
- 呼び出し先: `Array.isArray()`, `Cu.cloneInto()`, `VALID_FORM_REVIEW_GENERATION_ERRORS.includes()`, `this.#getReview()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `FORM_REVIEW_STATES.PROGRESS`, `FORM_REVIEW_STATES.REVIEW`, `data.errorType`, `data.fields`, `data?.errorType`, `data?.fields`, `review.errorType`, `review.fields`, `review.filledFieldCount`, `review.filling`, `review.state`, `review.updateComplete`, `this.contentWindow`

## SmartFormFillReviewChild.handleEvent()
- 位置: L122-163
- 役割: Escape はキャンセルとして扱い、準備完了イベントは親へ送る。ユーザー操作は許可された種類だけ親へ送り、FILL_FORM では id と value が文字列の欄だけを残す。
- 触るとき: 確認画面の操作が親に届かない、または入力欄が落ちて埋められないときに見る。
- 呼び出し先: `VALID_FORM_REVIEW_ACTIONS.includes()`, `this.#sendAction()`
- 条件付き依存: `if (event.key === "Escape")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape")` → `event.stopPropagation()`
- 条件付き依存: `if (!this.#fillPending)` → `this.#sendAction()`
- 条件付き依存: `if (event.type === FORM_REVIEW_READY_EVENT)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type === FORM_REVIEW_ACTIONS.FILL_FORM)` → `Array.isArray()`
- 条件付き依存: `if (event.type === FORM_REVIEW_ACTIONS.FILL_FORM)` → `event.detail.fields .filter( field => typeof field.id === "string" && typeof field.value === "string" ) .map()`
- 条件付き依存: `if (event.type === FORM_REVIEW_ACTIONS.FILL_FORM)` → `event.detail.fields .filter()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `FORM_REVIEW_ACTIONS.FILL_FORM`, `action.fields`, `event.detail`, `event.detail.fields`, `event.key`, `event.type`, `field.id`, `field.value`, `this.#fillPending`

## SmartFormFillReviewChild.#sendAction()
- 位置: L171-182
- 役割: フィルの途中なら何もしない。フィル以外の操作は親へそのまま送り、フィルは #sendFillAction に回す。
- 触るとき: 操作を二重に送ってしまうとき、またはフィル以外の操作の扱いを変えるときに見る。
- 呼び出し先: `this.#sendFillAction()`
- 条件付き依存: `if (action.type !== FORM_REVIEW_ACTIONS.FILL_FORM)` → `this.sendAsyncMessage()`
- 参照: `FORM_REVIEW_ACTIONS.FILL_FORM`, `action.type`, `this.#fillPending`

## SmartFormFillReviewChild.#sendFillAction()
- 位置: async L191-221
- 役割: フィル中の印を立てて親に問い合わせる。失敗なら FILL_FAILED を表示し、キャンセルされた場合はキャンセル操作として扱う。成功なら結果の件数を表示する。
- 触るとき: フィルの結果表示が失敗扱いになる、またはキャンセル時に画面が戻らないときに見る。
- 呼び出し先: `this.#showResult()`, `this.sendQuery()`
- 条件付き依存: `if (!this.#destroyed)` → `this.#showResult()`
- 条件付き依存: `if (result?.cancelled)` → `this.#sendAction()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `FORM_REVIEW_ERRORS.FILL_FAILED`, `result.hasErrors`, `result?.cancelled`, `result?.filledFieldCount`, `this.#destroyed`, `this.#fillPending`

## SmartFormFillReviewChild.#showResult()
- 位置: L232-247
- 役割: フィル中の印を解除し、エラー種別と埋めたフィールド数を反映して最終状態にする。
- 触るとき: フィル完了後の結果表示(件数や失敗表示)がずれるときに見る。
- 呼び出し先: `this.#getReview()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `review.errorType`, `review.filledFieldCount`, `review.filling`, `review.state`, `this.#destroyed`, `this.#fillPending`

## SmartFormFillReviewChild.#getReview()
- 位置: L255-258
- 役割: 文書から ai-sff-form-review を探し、Xray を外して返す。無ければ null を返す。
- 触るとき: ダイアログの要素が見つからず処理が黙って止まるとき、またはコンポーネント名を変えるときに見る。
- 呼び出し先: `Cu.waiveXrays()`, `this.document.querySelector()`
