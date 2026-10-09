# browser/components/aiwindow/ui/actors/SmartFormFillReviewParent.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillReviewParent.sys.mjs
source-hash: c3a3c87a0d818520e38ffa74336899799a16432f
lines: 196

## <module>
- 役割: Smart Form Fill の確認ダイアログの親アクター。ダイアログ側への状態送信と、ダイアログからの操作の受け渡しを行う。

## SmartFormFillReviewParent.connect()
- 位置: L47-51
- 役割: プロセスの種類を検査したうえで、操作ハンドラと破棄ハンドラを登録する。
- 触るとき: 確認ダイアログの操作がハンドラに届かないとき、またはハンドラの登録方法を変えるときに見る。
- 呼び出し先: `this.#assertRemoteType()`
- 参照: `this.#actionHandler`, `this.#destroyHandler`

## SmartFormFillReviewParent.disconnect()
- 位置: L58-61
- 役割: 操作と破棄のハンドラを外す。
- 触るとき: ダイアログを閉じた後に古いハンドラが呼ばれる、または呼ばれるべき処理が呼ばれないときに見る。
- 参照: `this.#actionHandler`, `this.#destroyHandler`

## SmartFormFillReviewParent.initialize()
- 位置: L70-73
- 役割: ダイアログを進行中の状態にする Initialize を子へ問い合わせ、反映されたかを返す。
- 触るとき: 候補の生成中に確認画面が進行表示にならないときに見る。
- 呼び出し先: `this.#assertRemoteType()`, `this.sendQuery()`

## SmartFormFillReviewParent.showSuggestions()
- 位置: L83-86
- 役割: 生成された値の一覧を ShowSuggestions として子へ送り、表示されたかを返す。
- 触るとき: 生成結果が確認画面に出ないとき、または送る項目の形を変えるときに見る。
- 呼び出し先: `this.#assertRemoteType()`, `this.sendQuery()`

## SmartFormFillReviewParent.showGenerationError()
- 位置: L96-105
- 役割: 許可された生成エラー種別なら ShowGenerationError として子へ送る。不正な種別は送らず false を返す。
- 触るとき: 生成失敗の表示が出ないとき、または新しいエラー種別を足すときに見る。種別は SmartFormFillConstants.mjs の許可リストにも足す必要がある。
- 呼び出し先: `VALID_FORM_REVIEW_GENERATION_ERRORS.includes()`, `this.#assertRemoteType()`, `this.sendQuery()`
- 条件付き依存: `if (!VALID_FORM_REVIEW_GENERATION_ERRORS.includes(errorType))` → `Promise.resolve()`

## SmartFormFillReviewParent.receiveMessage()
- 位置: L125-146
- 役割: Ready なら準備完了を通知し、Action なら許可された操作種別だけを接続中のハンドラへ渡して結果を返す。それ以外は例外にする。
- 触るとき: 確認画面の操作に応答が返らないとき、または親で受け付ける操作を増やすときに見る。
- 呼び出し先: `VALID_FORM_REVIEW_ACTIONS.includes()`, `this.#actionHandler()`, `this.#assertRemoteType()`
- 条件付き依存: `if (name === FORM_REVIEW_READY_EVENT)` → `this.#notifyReady()`
- 参照: `data?.type`, `this.#actionHandler`

## SmartFormFillReviewParent.#notifyReady()
- 位置: L153-163
- 役割: 埋め込み元のブラウザ要素に、準備完了の CustomEvent を発火する。
- 触るとき: 確認画面の準備完了を待つ側(ダイアログ殻)が反応しないときに見る。
- 呼び出し先: `browser.dispatchEvent()`
- 参照: `browser?.documentGlobal`, `chromeWindow.CustomEvent`, `this.browsingContext.embedderElement`

## SmartFormFillReviewParent.didDestroy()
- 位置: L170-177
- 役割: 破棄ハンドラを取り出してから接続を外し、破棄ハンドラがあれば呼ぶ。
- 触るとき: ダイアログを閉じた後の後始末が走らない、または二重に走るときに見る。
- 呼び出し先: `this.disconnect()`
- 条件付き依存: `if (destroyHandler)` → `destroyHandler()`
- 参照: `this.#destroyHandler`

## SmartFormFillReviewParent.#assertRemoteType()
- 位置: L185-194
- 役割: 文書が同一プロセスか privilegedabout のプロセスでなければ例外を投げる。
- 触るとき: 確認ダイアログの別プロセス化や、プロセスの種類の扱いを変えるときに見る。想定外のプロセスからの要求を止める役割がある。
- 参照: `E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `this.manager.isInProcess`, `this.manager.remoteType`
