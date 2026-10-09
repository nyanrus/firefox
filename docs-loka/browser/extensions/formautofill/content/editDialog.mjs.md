# browser/extensions/formautofill/content/editDialog.mjs

source: browser/extensions/formautofill/content/editDialog.mjs
source-hash: b9f82e4937aaf327870f7efe7cb414fc6a820f18
lines: 320

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AutofillEditDialog.constructor()
- 位置: L21-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.formAutofillStorage.initialize()`, `this.localizeDocument()`, `window.addEventListener()`
- 参照: `this._elements`, `this._record`, `this._storageInitPromise`, `this._subStorageName`

## AutofillEditDialog.init()
- 位置: async L30-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.attachEventListeners()`, `this.updateSaveButtonState()`, `window.dispatchEvent()`

## AutofillEditDialog.getStorage()
- 位置: async L44-47
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.formAutofillStorage`, `this._storageInitPromise`, `this._subStorageName`

## AutofillEditDialog.saveRecord()
- 位置: async L55-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getStorage()`
- 条件付き依存: `if (guid)` → `storage.update()`
- 条件付き依存: `if (!(guid))` → `storage.add()`

## AutofillEditDialog.handleEvent()
- 位置: L69-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HTMLInputElement.isInstance()`, `HTMLTextAreaElement.isInstance()`, `this.handleClick()`, `this.handleInput()`, `this.handleKeyPress()`, `this.init()`
- 条件付き依存: `if ( !HTMLInputElement.isInstance(event.target) && !HTMLTextAreaElement.isInstance(event.target) )` → `event.preventDefault()`
- 参照: `event.target`, `event.type`

## AutofillEditDialog.handleClick()
- 位置: L104-111
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this._elements.cancel)` → `window.close()`
- 条件付き依存: `if (event.target == this._elements.save)` → `this.handleSubmit()`
- 参照: `event.target`, `this._elements.cancel`, `this._elements.save`

## AutofillEditDialog.handleInput()
- 位置: L116-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateSaveButtonState()`

## AutofillEditDialog.handleKeyPress()
- 位置: L125-129
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `window.close()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `event.keyCode`

## AutofillEditDialog.updateSaveButtonState()
- 位置: L131-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this._elements.fieldContainer.buildFormObject()`
- 参照: `Object.keys( this._elements.fieldContainer.buildFormObject() ).length`, `this._elements.save.disabled`

## AutofillEditDialog.attachEventListeners()
- 位置: L140-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `this._elements.cancel.addEventListener()`, `this._elements.save.addEventListener()`, `window.addEventListener()`

## AutofillEditDialog.localizeDocument()
- 位置: L149-149
- 役割: (未記入)
- 触るとき: (未記入)

## AutofillEditDialog.recordFormSubmit()
- 位置: L151-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AutofillTelemetry.recordManageEvent()`
- 参照: `this._record?.guid`, `this.dataType`

## EditAddressDialog.constructor()
- 位置: L160-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 条件付き依存: `if (record)` → `lazy.AutofillTelemetry.recordManageEvent()`
- 参照: `this.dataType`

## EditAddressDialog.handleEvent()
- 位置: L167-173
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "focusout")` → `this.handleFocusOut()`
- 条件付き依存: `if (!(event.type === "focusout"))` → `super.handleEvent()`
- 参照: `event.type`

## EditAddressDialog._validateField()
- 位置: L175-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `field.inputEl.checkValidity()`, `field.toggleAttribute()`
- 参照: `field.dataset.pattern`, `field.dataset.required`, `field.dataset.type`, `field.inputEl`, `field.inputEl.pattern`, `field.inputEl.required`, `field.inputEl.type`

## EditAddressDialog.handleInput()
- 位置: L191-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.handleInput()`, `this._validateField()`
- 参照: `event.target`

## EditAddressDialog.handleFocusOut()
- 位置: L196-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._validateField()`
- 参照: `event.target`

## EditAddressDialog.attachEventListeners()
- 位置: L200-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `super.attachEventListeners()`

## EditAddressDialog.localizeDocument()
- 位置: L205-212
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._record?.guid)` → `document.l10n.setAttributes()`
- 参照: `this._elements.title`, `this._record?.guid`

## EditAddressDialog.updateSaveButtonState()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canSubmitForm()`
- 参照: `this._elements.save.disabled`

## EditAddressDialog.handleSubmit()
- 位置: async L218-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCurrentFormData()`, `this.recordFormSubmit()`, `this.saveRecord()`, `validateAddressForm()`, `window.close()`
- 参照: `this._record`, `this._record.guid`

## EditCreditCardDialog.constructor()
- 位置: L235-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elements.fieldContainer._elements.ccNumber.addEventListener()`, `super()`, `this._onCCNumberFieldBlur.bind()`
- 条件付き依存: `if (record)` → `lazy.AutofillTelemetry.recordManageEvent()`
- 参照: `elements.fieldContainer._elements.billingAddress.disabled`, `this.dataType`

## EditCreditCardDialog._onCCNumberFieldBlur()
- 位置: L247-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elem.inputEl?.checkValidity()`, `elem.toggleAttribute()`, `this._elements.fieldContainer.updateCustomValidity()`
- 参照: `this._elements.fieldContainer._elements.ccNumber`

## EditCreditCardDialog.localizeDocument()
- 位置: L254-261
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._record?.guid)` → `document.l10n.setAttributes()`
- 参照: `this._elements.title`, `this._record?.guid`

## EditCreditCardDialog.handleSubmit()
- 位置: async L263-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._elements.fieldContainer.buildFormObject()`, `this._elements.fieldContainer.validateForm()`, `this.recordFormSubmit()`, `this.saveRecord()`, `window.close()`
- 参照: `this._record`, `this._record.guid`

## EditPassportDialog.constructor()
- 位置: L287-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 条件付き依存: `if (record)` → `lazy.AutofillTelemetry.recordManageEvent()`
- 参照: `this.dataType`

## EditPassportDialog.localizeDocument()
- 位置: L294-301
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._record?.guid)` → `document.l10n.setAttributes()`
- 参照: `this._elements.title`, `this._record?.guid`

## EditPassportDialog.handleSubmit()
- 位置: async L303-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._elements.fieldContainer.buildFormObject()`, `this._elements.fieldContainer.validateForm()`, `this.recordFormSubmit()`, `this.saveRecord()`, `window.close()`
- 参照: `this._record`, `this._record.guid`
