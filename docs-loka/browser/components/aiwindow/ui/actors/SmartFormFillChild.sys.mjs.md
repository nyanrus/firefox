# browser/components/aiwindow/ui/actors/SmartFormFillChild.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillChild.sys.mjs
source-hash: 50552bdf9a1fd012a88d1ccc958594d8dff7aa8b
lines: 480

## <module>
- 役割: Smart Form Fill の子アクター。ページ文書の準備、親からの要求の振り分け、補完ポップアップの制御、フォーム更新と入力結果の通知を行う。
- 呼び出し先: `Cc["@mozilla.org/satchel/form-fill-controller;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## SmartFormFillChild.actorCreated()
- 位置: L90-94
- 役割: 文書が読み込み中でなければ準備を始める。読み込み中なら DOMContentLoaded を待つ。
- 触るとき: ページを開いた直後に入力支援が効かないとき、または準備が二重に走っていないか確かめるときに見る。
- 条件付き依存: `if (this.document.readyState !== "loading")` → `this.#prepareDocument()`
- 参照: `this.document.readyState`

## SmartFormFillChild.handleEvent()
- 位置: async L102-108
- 役割: DOMContentLoaded を受けたときだけ文書の準備を行い、他のイベントは無視する。
- 触るとき: 読み込み完了後に準備されないとき、または準備のきっかけとなるイベントを増やすときに見る。
- 呼び出し先: `this.#prepareDocument()`
- 参照: `event.type`

## SmartFormFillChild.#prepareDocument()
- 位置: L115-144
- 役割: 準備を一度だけ実行し、進行中の Promise を共有する。失敗したら文書を破棄し、破棄済みでなければエラーを記録する。
- 触るとき: 準備の失敗で入力支援が止まるとき、または準備の再実行の条件を変えるときに見る。
- 呼び出し先: `this.#setUpDocument()`, `this.#setUpDocument() .catch()`, `this.#smartFormFillDocument?.destroy()`
- 条件付き依存: `if (this.#smartFormFillDocument || this.#destroyed)` → `Promise.resolve()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `this.#destroyed`, `this.#documentPreparationPromise`, `this.#smartFormFillDocument`

## SmartFormFillChild.#setUpDocument()
- 位置: async L151-177
- 役割: 親に IsSmartWindow を問い合わせ、Smart Window でなければ何もしない。そうなら SmartFormFillDocument を作って初期化し、対象フィールドを補完に登録する。
- 触るとき: Smart Window 以外で動いてしまうとき、または対象フィールドが補完候補に出ないときに見る。
- 呼び出し先: `this.#onFieldOutcomes.bind()`, `this.#onFieldsFilled.bind()`, `this.#onFormUpdate.bind()`, `this.#registerAutocompleteFields()`, `this.#smartFormFillDocument.initialize()`, `this.sendQuery()`, `this.sendQuery( "SmartFormFill:IsSmartWindow" ).catch()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `lazy.SmartFormFillDocument`, `this.#destroyed`, `this.#smartFormFillDocument`, `this.document`

## SmartFormFillChild.receiveMessage()
- 位置: async L186-220
- 役割: 文書がまだ準備されていなければ準備してから、FillForm、StopFilling、GetFocusedForm、RefreshAutocomplete、ShowAutocompletePopup を文書マネージャーへ振り分ける。未知の名前は null を返す。
- 触るとき: 親から新しい要求を足すとき、または親の要求に応答が返らないときに見る。
- 呼び出し先: `this.#refreshAutocomplete()`, `this.#showAutocompletePopup()`, `this.#smartFormFillDocument.fillForm()`, `this.#smartFormFillDocument.getFocusedForm()`, `this.#smartFormFillDocument.stopFilling()`
- 条件付き依存: `if ( !this.#smartFormFillDocument && this.document.readyState !== "loading" )` → `this.#prepareDocument()`
- 参照: `this.#smartFormFillDocument`, `this.document.readyState`

## SmartFormFillChild.didDestroy()
- 位置: L225-232
- 役割: フォーカス待ちを中止し、文書の状態を破棄して破棄済みフラグを立てる。
- 触るとき: ページ遷移の後に古い文書へ処理が届く、または待ちが残るときに見る。
- 呼び出し先: `this.#autocompletePopupFocusAbortController?.abort()`, `this.#smartFormFillDocument?.destroy()`
- 参照: `this.#autocompletePopupFocusAbortController`, `this.#destroyed`, `this.#documentPreparationPromise`, `this.#smartFormFillDocument`

## SmartFormFillChild.#onFormUpdate()
- 位置: L240-247
- 役割: フォームが変わったら対象フィールドを再登録し、FormUpdate を親へ送る。
- 触るとき: 動的に増えた欄が補完対象にならないとき、またはフォームの変化が親に届かないときに見る。
- 呼び出し先: `this.#registerAutocompleteFields()`, `this.sendAsyncMessage()`
- 参照: `this.#destroyed`

## SmartFormFillChild.#showAutocompletePopup()
- 位置: L252-295
- 役割: 今すぐ開けなければ、次の focusin と遅延実行の両方で開き直すよう待ち状態を作る。開けた時点で待ち状態を解除する。
- 触るとき: ダイアログを閉じた後に補完ポップアップが開かないときに見る。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `this.#autocompletePopupFocusAbortController?.abort()`, `this.#tryShowAutocompletePopup()`, `this.document.addEventListener()`
- 条件付き依存: `if (this.#tryShowAutocompletePopup())` → `clearPendingAttempt()`
- 参照: `abortController.signal`, `abortController.signal.aborted`, `this.#autocompletePopupFocusAbortController`, `this.#destroyed`
- XPCOM: `Services.tm`

## clearPendingAttempt()
- 位置: L262-267
- 役割: 待ち状態を中止し、現在の待ち状態として保持していれば参照を消す。
- 触るとき: ポップアップの再試行が残り続けるとき、または古い待ち状態が次の表示に影響するときに見る。
- 呼び出し先: `abortController.abort()`
- 参照: `this.#autocompletePopupFocusAbortController`

## retryAfterFocus()
- 位置: L269-278
- 役割: focusin の後に次のタスクで待ち状態を解除し、ポップアップを開き直す。中止済みか破棄済みなら何もしない。
- 触るとき: フォーカスが戻った後にポップアップが二重に開く、または開かないときに見る。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `clearPendingAttempt()`, `this.#tryShowAutocompletePopup()`
- 参照: `abortController.signal.aborted`, `this.#destroyed`
- XPCOM: `Services.tm`

## SmartFormFillChild.#tryShowAutocompletePopup()
- 位置: L302-328
- 役割: 補完アクターのポップアップが閉じていて、フォーカス中の要素が対象欄かつ補完コントローラがその欄を制御している場合にだけ showPopup を呼ぶ。開けたら true を返す。
- 触るとき: 候補を出すべき欄でポップアップが出ない、または別の欄で出てしまうときに見る。
- 呼び出し先: `lazy.formFillController.showPopup()`, `this.#smartFormFillDocument.isSupportedField()`, `this.manager.getActor()`
- 参照: `autocompleteActor.popupOpen`, `lazy.formFillController.controlledElement`, `this.#destroyed`, `this.#smartFormFillDocument`, `this.document.activeElement`

## SmartFormFillChild.#refreshAutocomplete()
- 位置: L335-357
- 役割: フォーカス中の対象欄なら、ポップアップが開いていれば検索をやり直し、閉じていれば内部状態を初期化する。
- 触るとき: フォーム入力の後に候補が古いまま残るとき、または更新後に候補が出ないときに見る。
- 呼び出し先: `autocompleteController.startSearch()`, `lazy.formFillController.QueryInterface()`, `this.#smartFormFillDocument?.isSupportedField()`, `this.manager.getActor()`
- 条件付き依存: `if (!autocompleteActor?.popupOpen)` → `autocompleteController.resetInternalState()`
- 参照: `Ci.nsIAutoCompleteInput`, `autocompleteActor?.popupOpen`, `autocompleteController.searchString`, `autocompleteInput.controller`, `lazy.formFillController.controlledElement`, `this.document.activeElement`
- XPCOM: [`nsIAutoCompleteInput`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteController.idl.md)

## SmartFormFillChild.#registerAutocompleteFields()
- 位置: L373-382
- 役割: 対象フィールドのそれぞれを、この actor を候補元として AutoComplete アクターに登録する。
- 触るとき: 新しい欄が補完の候補元に含まれないときに見る。
- 呼び出し先: `autocompleteActor.markAsAutoCompletableField()`, `this.#smartFormFillDocument.getSupportedFields()`, `this.manager.getActor()`

## SmartFormFillChild.shouldSearchForAutoComplete()
- 位置: L396-398
- 役割: 入力欄に対して Smart Form Fill の候補があるかを文書に問い合わせ、無ければ false を返す。
- 触るとき: 候補の無い欄で親への検索が走る、または候補があるのに検索されないときに見る。
- 呼び出し先: `this.#smartFormFillDocument?.shouldOfferFill()`

## SmartFormFillChild.getAutoCompleteSearchOption()
- 位置: L405-407
- 役割: プロバイダ契約のための空のオプションを返す。
- 触るとき: 補完プロバイダの契約を変えるときだけ見る。

## SmartFormFillChild.searchResultToAutoCompleteResult()
- 位置: L425-438
- 役割: 親から届いた entries を外部候補として FormHistoryAutoCompleteResult に詰め直す。entries が無ければ null を返す。
- 触るとき: 候補の表示内容や並びが親の結果と合わないときに見る。
- 呼び出し先: `result.externalEntries.push()`
- 参照: `input.name`, `lazy.FormHistoryAutoCompleteResult`, `records.entries`, `records?.entries?.length`

## SmartFormFillChild.actorName()
- 位置: L446-448
- 役割: AutoComplete が検索を振り分ける先として "SmartFormFill" を返す。
- 触るとき: 補完の検索が別のアクターへ行ってしまうときに見る。

## SmartFormFillChild.#onFieldOutcomes()
- 位置: L456-462
- 役割: フィールドごとの入力結果を SmartFormFill:FieldOutcomes として親へ送る。
- 触るとき: モデルの入力結果が親の記録に残らないときに見る。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `this.#destroyed`

## SmartFormFillChild.#onFieldsFilled()
- 位置: L472-478
- 役割: 書き込んだフィールドの id と fieldIds を SmartFormFill:FieldsFilled として親へ送る。
- 触るとき: どの欄に書いたかの記録が親とずれるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `this.#destroyed`
