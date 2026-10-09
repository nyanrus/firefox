# browser/components/aiwindow/ui/actors/SmartFormFillChild.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillChild.sys.mjs
source-hash: 50552bdf9a1fd012a88d1ccc958594d8dff7aa8b
lines: 480

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/satchel/form-fill-controller;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## SmartFormFillChild.actorCreated()
- 位置: L90-94
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.document.readyState !== "loading")` → `this.#prepareDocument()`
- 参照: `this.document.readyState`

## SmartFormFillChild.handleEvent()
- 位置: async L102-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#prepareDocument()`
- 参照: `event.type`

## SmartFormFillChild.#prepareDocument()
- 位置: L115-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setUpDocument()`, `this.#setUpDocument() .catch()`, `this.#smartFormFillDocument?.destroy()`
- 条件付き依存: `if (this.#smartFormFillDocument || this.#destroyed)` → `Promise.resolve()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `this.#destroyed`, `this.#documentPreparationPromise`, `this.#smartFormFillDocument`

## SmartFormFillChild.#setUpDocument()
- 位置: async L151-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onFieldOutcomes.bind()`, `this.#onFieldsFilled.bind()`, `this.#onFormUpdate.bind()`, `this.#registerAutocompleteFields()`, `this.#smartFormFillDocument.initialize()`, `this.sendQuery()`, `this.sendQuery( "SmartFormFill:IsSmartWindow" ).catch()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `lazy.SmartFormFillDocument`, `this.#destroyed`, `this.#smartFormFillDocument`, `this.document`

## SmartFormFillChild.receiveMessage()
- 位置: async L186-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#refreshAutocomplete()`, `this.#showAutocompletePopup()`, `this.#smartFormFillDocument.fillForm()`, `this.#smartFormFillDocument.getFocusedForm()`, `this.#smartFormFillDocument.stopFilling()`
- 条件付き依存: `if ( !this.#smartFormFillDocument && this.document.readyState !== "loading" )` → `this.#prepareDocument()`
- 参照: `this.#smartFormFillDocument`, `this.document.readyState`

## SmartFormFillChild.didDestroy()
- 位置: L225-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#autocompletePopupFocusAbortController?.abort()`, `this.#smartFormFillDocument?.destroy()`
- 参照: `this.#autocompletePopupFocusAbortController`, `this.#destroyed`, `this.#documentPreparationPromise`, `this.#smartFormFillDocument`

## SmartFormFillChild.#onFormUpdate()
- 位置: L240-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registerAutocompleteFields()`, `this.sendAsyncMessage()`
- 参照: `this.#destroyed`

## SmartFormFillChild.#showAutocompletePopup()
- 位置: L252-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `this.#autocompletePopupFocusAbortController?.abort()`, `this.#tryShowAutocompletePopup()`, `this.document.addEventListener()`
- 条件付き依存: `if (this.#tryShowAutocompletePopup())` → `clearPendingAttempt()`
- 参照: `abortController.signal`, `abortController.signal.aborted`, `this.#autocompletePopupFocusAbortController`, `this.#destroyed`
- XPCOM: `Services.tm`

## clearPendingAttempt()
- 位置: L262-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `abortController.abort()`
- 参照: `this.#autocompletePopupFocusAbortController`

## retryAfterFocus()
- 位置: L269-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `clearPendingAttempt()`, `this.#tryShowAutocompletePopup()`
- 参照: `abortController.signal.aborted`, `this.#destroyed`
- XPCOM: `Services.tm`

## SmartFormFillChild.#tryShowAutocompletePopup()
- 位置: L302-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.formFillController.showPopup()`, `this.#smartFormFillDocument.isSupportedField()`, `this.manager.getActor()`
- 参照: `autocompleteActor.popupOpen`, `lazy.formFillController.controlledElement`, `this.#destroyed`, `this.#smartFormFillDocument`, `this.document.activeElement`

## SmartFormFillChild.#refreshAutocomplete()
- 位置: L335-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `autocompleteController.startSearch()`, `lazy.formFillController.QueryInterface()`, `this.#smartFormFillDocument?.isSupportedField()`, `this.manager.getActor()`
- 条件付き依存: `if (!autocompleteActor?.popupOpen)` → `autocompleteController.resetInternalState()`
- 参照: `Ci.nsIAutoCompleteInput`, `autocompleteActor?.popupOpen`, `autocompleteController.searchString`, `autocompleteInput.controller`, `lazy.formFillController.controlledElement`, `this.document.activeElement`
- XPCOM: [`nsIAutoCompleteInput`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteController.idl.md)

## SmartFormFillChild.#registerAutocompleteFields()
- 位置: L373-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `autocompleteActor.markAsAutoCompletableField()`, `this.#smartFormFillDocument.getSupportedFields()`, `this.manager.getActor()`

## SmartFormFillChild.shouldSearchForAutoComplete()
- 位置: L396-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartFormFillDocument?.shouldOfferFill()`

## SmartFormFillChild.getAutoCompleteSearchOption()
- 位置: L405-407
- 役割: (未記入)
- 触るとき: (未記入)

## SmartFormFillChild.searchResultToAutoCompleteResult()
- 位置: L425-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.externalEntries.push()`
- 参照: `input.name`, `lazy.FormHistoryAutoCompleteResult`, `records.entries`, `records?.entries?.length`

## SmartFormFillChild.actorName()
- 位置: L446-448
- 役割: (未記入)
- 触るとき: (未記入)

## SmartFormFillChild.#onFieldOutcomes()
- 位置: L456-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `this.#destroyed`

## SmartFormFillChild.#onFieldsFilled()
- 位置: L472-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `this.#destroyed`
