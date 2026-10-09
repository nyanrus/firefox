# browser/components/aiwindow/ui/components/ai-sff-form-review/ai-sff-form-review.mjs

source: browser/components/aiwindow/ui/components/ai-sff-form-review/ai-sff-form-review.mjs
source-hash: 6c83d3cefe5e0f92c07de93fb32bdebd1c1dd8f7
lines: 676

## <module>
- 役割: Smart Form Fill で生成された入力値を確認・編集し、フォームへの入力を依頼する画面 ai-sff-form-review を定義する。
- 呼び出し先: `customElements.define()`

## AiSffFormReview.constructor()
- 位置: L81-98
- 役割: 状態を PROGRESS、入力値を空配列、errorType と filledFieldCount を null、filling を false にする。
- 触るとき: 初期表示を進行中以外にしたいとき、または新しい状態フィールドを足すとき。
- 呼び出し先: `super()`
- 参照: `FORM_REVIEW_STATES.PROGRESS`, `this.errorType`, `this.fields`, `this.filledFieldCount`, `this.filling`, `this.state`

## AiSffFormReview.firstUpdated()
- 位置: async L105-112
- 役割: 現在の状態へフォーカスを移してから FORM_REVIEW_READY_EVENT を発火し、値の生成を始めさせる。
- 触るとき: 生成が始まらず進行表示のまま止まるとき、または準備完了の合図を変えるとき。
- 呼び出し先: `this.#focusCurrentState()`, `this.dispatchEvent()`

## AiSffFormReview.updated()
- 位置: L121-149
- 役割: 状態が変わった時や再入力の完了時にフォーカスを移す。PROGRESS に戻ったときだけ再試行済みと全件確認のフラグを戻し、状態変化時はスクロールとレビュー監視を張り直す。
- 触るとき: 状態遷移のあとにフォーカスが飛ぶ、または再試行や確認フラグが残って次の確認が省かれるとき。
- 呼び出し先: `changedProperties.get()`, `changedProperties.has()`, `super.updated()`, `this.#observeReviewFields()`, `this.#updateScrollListeners()`
- 条件付き依存: `if (changedProperties.get("state") !== undefined || retryCompleted)` → `this.#focusCurrentState()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `FORM_REVIEW_STATES.PROGRESS`, `this.#retryUsed`, `this.#reviewedAllFields`, `this.filling`, `this.state`

## AiSffFormReview.#observeReviewFields()
- 位置: L151-171
- 役割: REVIEW 状態で全件確認がまだなら、入力一覧の scroll と ResizeObserver を監視し、末尾到達を判定できるようにする。
- 触るとき: 末尾まで読んでも入力ボタンが有効にならない、または REVIEW 以外で監視が動くとき。
- 呼び出し先: `this.#reviewFieldsElement.addEventListener()`, `this.#reviewFieldsObserver.observe()`, `this.#stopObservingReviewFields()`
- 参照: `FORM_REVIEW_STATES.REVIEW`, `this.#reviewFieldsElement`, `this.#reviewFieldsObserver`, `this.#reviewedAllFields`, `this.#updateReviewCompletion`, `this.reviewFields`, `this.state`

## AiSffFormReview.#stopObservingReviewFields()
- 位置: L173-181
- 役割: 入力一覧の ResizeObserver を切断し、scroll リスナーを外して参照を消す。
- 触るとき: 画面を離れたあとも一覧の監視が残る不具合を調べるとき。
- 呼び出し先: `this.#reviewFieldsElement?.removeEventListener()`, `this.#reviewFieldsObserver?.disconnect()`
- 参照: `this.#reviewFieldsElement`, `this.#reviewFieldsObserver`, `this.#updateReviewCompletion`

## AiSffFormReview.#updateReviewCompletion()
- 位置: L183-196
- 役割: 一覧の残りのスクロール量が 1px 以下になったら全件確認済みにし、監視を止めて再描画を要求する。
- 触るとき: 確認完了の条件を変えるとき、または入力ボタンが有効にならない原因を調べるとき。
- 呼び出し先: `this.#stopObservingReviewFields()`, `this.requestUpdate()`
- 参照: `this.#reviewFieldsElement`, `this.#reviewedAllFields`

## AiSffFormReview.disconnectedCallback()
- 位置: L198-202
- 役割: 親の切断処理のあとに、入力一覧の監視とスクロール関連のリスナーを外す。
- 触るとき: 要素を取り外した後に監視やリスナーが残る問題を調べるとき。
- 呼び出し先: `super.disconnectedCallback()`, `this.#stopObservingReviewFields()`, `this.#teardownScrollListeners()`

## AiSffFormReview.#focusCurrentState()
- 位置: async L209-225
- 役割: 状態の区画を l10n で翻訳してから、状態が変わっていなければその区画にフォーカスを当てる。
- 触るとき: 状態が変わったあとのフォーカス位置や読み上げ内容を確かめるとき。
- 呼び出し先: `this.ownerDocument.l10n?.translateFragment()`
- 条件付き依存: `if ( section.isConnected && this.state === state && this.stateSection === section )` → `section.focus()`
- 参照: `section.isConnected`, `this.state`, `this.stateSection`

## AiSffFormReview.#updateScrollListeners()
- 位置: L233-272
- 役割: REVIEW 状態で一覧と末尾ボタンがあるときだけ、スクロール、ボタンのクリック、サイズ変化のリスナーを張る。
- 触るとき: 末尾ボタンが反応しない、または状態を戻しても監視が残るときに見る。
- 呼び出し先: `fields.addEventListener()`, `jumpButton.addEventListener()`, `this.#overflowObserver.observe()`, `this.#teardownScrollListeners()`, `this.#updateJumpButtonState()`
- 参照: `FORM_REVIEW_STATES.REVIEW`, `this.#jumpClickHandler`, `this.#overflowObserver`, `this.#scrollHandler`, `this.jumpButton`, `this.reviewFields`, `this.state`

## this.#scrollHandler()
- 位置: L246-255
- 役割: 一覧のスクロールを requestAnimationFrame で1フレームに1回にまとめ、末尾ボタンの表示判定を呼ぶ。
- 触るとき: 末尾ボタンの表示が遅れる、またはスクロール中に負荷が出るときに見る。
- 呼び出し先: `requestAnimationFrame()`, `this.#updateJumpButtonState()`
- 参照: `this.#scrollRafId`

## this.#jumpClickHandler()
- 位置: L257-259
- 役割: 末尾ボタンが押されたら、一覧の scrollTop を scrollHeight に合わせて末尾へ移動する。
- 触るとき: 末尾ボタンの移動先を変えたいとき、または移動しないとき。
- 参照: `fields.scrollHeight`, `fields.scrollTop`

## AiSffFormReview.#updateJumpButtonState()
- 位置: L280-295
- 役割: 末尾から 1px を超えて離れているときだけ末尾ボタンを visible かつ有効にし、それ以外は隠して無効にする。
- 触るとき: 末尾ボタンを出す条件を変えるとき、または表示が実際の位置とずれるとき。
- 呼び出し先: `jumpButton.hasAttribute()`
- 条件付き依存: `if (jumpButton.hasAttribute("visible") !== show)` → `jumpButton.toggleAttribute()`
- 参照: `fields.clientHeight`, `fields.scrollHeight`, `fields.scrollTop`, `this.jumpButton`, `this.reviewFields`

## AiSffFormReview.#teardownScrollListeners()
- 位置: L302-320
- 役割: 保留中の rAF を取り消し、一覧のスクロールとボタンのクリックのリスナー、サイズ監視を外す。
- 触るとき: 状態を切り替えた後も古いリスナーが動き続ける問題を調べるとき。
- 呼び出し先: `this.#overflowObserver?.disconnect()`
- 条件付き依存: `if (this.#scrollRafId)` → `cancelAnimationFrame()`
- 条件付き依存: `if (this.#scrollHandler)` → `this.reviewFields?.removeEventListener()`
- 条件付き依存: `if (this.#jumpClickHandler)` → `this.jumpButton?.removeEventListener()`
- 参照: `this.#jumpClickHandler`, `this.#overflowObserver`, `this.#scrollHandler`, `this.#scrollRafId`

## AiSffFormReview.#dispatchAction()
- 位置: L331-339
- 役割: 指定された種類と detail を持つ CustomEvent を、bubbles と composed を付けて発火する。
- 触るとき: 親ダイアログにアクションが届かないとき、またはイベントの形式を変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## AiSffFormReview.#handleInput()
- 位置: L350-363
- 役割: 生成中でなければ、編集された欄の値で fields の同じ id の要素の value を差し替える。
- 触るとき: 編集した値が保存されない、または別の欄に反映される不具合を調べるとき。
- 呼び出し先: `this.fields.map()`
- 参照: `event.currentTarget.value`, `field.id`, `this.fields`, `this.filling`

## AiSffFormReview.#handleFill()
- 位置: L370-379
- 役割: 生成中でなく全件確認済みなら filling を true にし、id と value の組を FILL_FORM として送る。
- 触るとき: フォームに送る値の形式を変えるとき、または入力が始まらない原因を調べるとき。
- 呼び出し先: `this.#dispatchAction()`, `this.fields.map()`
- 参照: `FORM_REVIEW_ACTIONS.FILL_FORM`, `this.#reviewedAllFields`, `this.filling`

## AiSffFormReview.#handleRetry()
- 位置: L387-394
- 役割: 生成中でなく再試行が未使用なら使用済みにして #handleFill を呼ぶ。再確認は挟まない。
- 触るとき: 失敗後の再試行が二度押せる、または再試行が効かないときに見る。
- 呼び出し先: `this.#handleFill()`
- 参照: `this.#retryUsed`, `this.filling`

## AiSffFormReview.#handleCancel()
- 位置: L401-407
- 役割: 生成中でなければ CANCEL アクションを発火し、値を入力せずに閉じる要求を出す。
- 触るとき: キャンセルで意図せず入力が走る、または閉じない不具合を調べるとき。
- 呼び出し先: `this.#dispatchAction()`
- 参照: `FORM_REVIEW_ACTIONS.CANCEL`, `this.filling`

## AiSffFormReview.#handleStop()
- 位置: L414-416
- 役割: STOP アクションを発火して、候補の生成を止めるよう要求する。
- 触るとき: 探索中の停止ボタンが効かないとき、または停止の扱いを変えるとき。
- 呼び出し先: `this.#dispatchAction()`
- 参照: `FORM_REVIEW_ACTIONS.STOP`

## AiSffFormReview.#handleClose()
- 位置: L423-425
- 役割: CLOSE アクションを発火して、完了画面のダイアログを閉じるよう要求する。
- 触るとき: 閉じた後の処理をダイアログ側で追うとき。
- 呼び出し先: `this.#dispatchAction()`
- 参照: `FORM_REVIEW_ACTIONS.CLOSE`

## AiSffFormReview.#renderReviewField()
- 位置: L434-449
- 役割: 1件の値を編集可能な入力欄として描画する。ラベルは label、placeholder、name の順に選び、無ければ汎用ラベルを使う。
- 触るとき: 入力欄のラベルの決め方や、生成中に無効化する条件を変えるとき。
- 呼び出し先: `html()`, `ifDefined()`, `this.#handleInput()`
- 参照: `field.id`, `field.label`, `field.name`, `field.placeholder`, `field.value`, `this.filling`

## AiSffFormReview.#renderReview()
- 位置: L457-512
- 役割: 見出し、説明、入力欄の一覧、末尾ボタン、キャンセルと入力のボタンを描画する。入力ボタンは全件確認まで無効。
- 触るとき: 確認画面の文言やボタン配置、入力ボタンの有効条件を変えるとき。
- 呼び出し先: `JSON.stringify()`, `html()`, `repeat()`, `this.#renderReviewField()`
- 参照: `field.id`, `this.#handleCancel`, `this.#handleFill`, `this.#reviewedAllFields`, `this.fields`, `this.fields.length`, `this.filling`

## AiSffFormReview.#renderProgress()
- 位置: L519-547
- 役割: 候補を探している間の読み込みアイコン、説明、停止ボタンを描画する。
- 触るとき: 探索中の表示文言や停止ボタンの見た目を変えるとき。
- 呼び出し先: `html()`
- 参照: `this.#handleStop`

## AiSffFormReview.#renderFinal()
- 位置: L554-641
- 役割: エラー種別と入力件数から結果の見出し、説明、アイコンを選び、閉じるボタンと、失敗時のみ再試行ボタンを描画する。
- 触るとき: 完了や失敗の表示文言、または再試行ボタンを出す条件を変えるとき。
- 呼び出し先: `html()`
- 参照: `FORM_REVIEW_ERRORS.FILL_FAILED`, `FORM_REVIEW_ERRORS.NO_SUGGESTIONS`, `this.#handleClose`, `this.#handleRetry`, `this.#retryUsed`, `this.errorType`, `this.filledFieldCount`, `this.filling`

## AiSffFormReview.render()
- 位置: L648-672
- 役割: 現在の状態に応じて進行中、確認、完了のどれかを描画し、スタイルシートと一緒に返す。
- 触るとき: 状態ごとの画面切り替えを変えるとき、または未知の状態が来た時の表示を調べるとき。
- 呼び出し先: `html()`, `this.#renderFinal()`, `this.#renderProgress()`, `this.#renderReview()`
- 参照: `FORM_REVIEW_STATES.FINAL`, `FORM_REVIEW_STATES.PROGRESS`, `FORM_REVIEW_STATES.REVIEW`, `this.state`
