# browser/extensions/formautofill/content/manageDialog.mjs

source: browser/extensions/formautofill/content/manageDialog.mjs
source-hash: 68b06662c2fbfbbc0326510c9bcf691ac0a01509
lines: 463

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `FormAutofill.defineLogGetter()`

## ManageRecords.constructor()
- 位置: L36-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.formAutofillStorage.initialize()`, `window.addEventListener()`
- 参照: `this._elements`, `this._isLoadingRecords`, `this._newRequest`, `this._storageInitPromise`, `this._subStorageName`, `this.prefWin`, `window.opener`

## ManageRecords.init()
- 位置: async L46-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.attachEventListeners()`, `this.loadRecords()`, `window.dispatchEvent()`

## ManageRecords.uninit()
- 位置: L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.detachEventListeners()`
- 参照: `this._elements`

## ManageRecords._selectedOptions()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`
- 参照: `this._elements.records.selectedOptions`

## ManageRecords.getStorage()
- 位置: async L73-76
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.formAutofillStorage`, `this._storageInitPromise`, `this._subStorageName`

## ManageRecords.loadRecords()
- 位置: async L82-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._elements.records.dispatchEvent()`, `this._loadRecords()`
- 参照: `this._isLoadingRecords`, `this._newRequest`

## ManageRecords._loadRecords()
- 位置: async L106-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `records.sort()`, `storage.getAll()`, `this.getStorage()`, `this.renderRecordElements()`, `this.updateButtonsStates()`
- 参照: `a.timeLastModified`, `a.timeLastUsed`, `b.timeLastModified`, `b.timeLastUsed`, `this._selectedOptions.length`

## ManageRecords.renderRecordElements()
- 位置: async L125-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectedGuids.includes()`, `this._elements.records.appendChild()`, `this._selectedOptions.map()`, `this.clearRecordElements()`, `this.getLabelInfo()`
- 条件付き依存: `if (id)` → `document.l10n.setAttributes()`
- 参照: `option.record`, `option.value`, `record.guid`

## ManageRecords.clearRecordElements()
- 位置: L148-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parentElement.removeChild()`
- 参照: `parentElement.lastChild`, `this._elements.records`

## ManageRecords.removeRecords()
- 位置: async L160-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutofillTelemetry.recordManageEvent()`, `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `option.remove()`, `storage.remove()`, `this._elements.records.dispatchEvent()`, `this.getStorage()`, `this.updateButtonsStates()`
- 参照: `option.value`, `options.length`, `this._selectedOptions`, `this.dataType`
- XPCOM: `Services.obs`

## ManageRecords.updateButtonsStates()
- 位置: L188-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.log.debug()`
- 条件付き依存: `if (selectedCount == 0)` → `this._elements.edit.setAttribute()`
- 条件付き依存: `if (selectedCount == 0)` → `this._elements.remove.setAttribute()`
- 条件付き依存: `if (selectedCount == 1)` → `this._elements.edit.removeAttribute()`
- 条件付き依存: `if (selectedCount == 1)` → `this._elements.remove.removeAttribute()`
- 条件付き依存: `if (selectedCount > 1)` → `this._elements.edit.setAttribute()`
- 条件付き依存: `if (selectedCount > 1)` → `this._elements.remove.removeAttribute()`
- 参照: `this._elements.add.disabled`, `this._subStorageName`
- XPCOM: `Services.prefs`

## ManageRecords.handleEvent()
- 位置: L210-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.handleClick()`, `this.handleKeyPress()`, `this.init()`, `this.uninit()`, `this.updateButtonsStates()`
- 参照: `event.type`, `this._selectedOptions.length`

## ManageRecords.handleClick()
- 位置: L244-255
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this._elements.remove)` → `this.removeRecords()`
- 条件付き依存: `if (event.target == this._elements.add)` → `this.openEditDialog()`
- 条件付き依存: `if ( event.target == this._elements.edit || (event.target.parentNode == this._elements.records && event.detail > 1) )` → `this.openEditDialog()`
- 参照: `event.detail`, `event.target`, `event.target.parentNode`, `this._elements.add`, `this._elements.edit`, `this._elements.records`, `this._elements.remove`, `this._selectedOptions`, `this._selectedOptions[0].record`

## ManageRecords.handleKeyPress()
- 位置: L262-269
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `window.close()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_DELETE)` → `this.removeRecords()`
- 参照: `KeyEvent.DOM_VK_DELETE`, `KeyEvent.DOM_VK_ESCAPE`, `event.keyCode`, `this._selectedOptions`

## ManageRecords.observe()
- 位置: L271-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.loadRecords()`

## ManageRecords.attachEventListeners()
- 位置: L282-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this._elements.controlsContainer.addEventListener()`, `this._elements.records.addEventListener()`, `window.addEventListener()`
- XPCOM: `Services.obs`

## ManageRecords.detachEventListeners()
- 位置: L295-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this._elements.controlsContainer.removeEventListener()`, `this._elements.records.removeEventListener()`, `window.removeEventListener()`
- XPCOM: `Services.obs`

## ManageAddresses.constructor()
- 位置: L308-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutofillTelemetry.recordManageEvent()`, `elements.add.setAttribute()`, `lazy.FormAutofillUtils.EDIT_ADDRESS_L10N_IDS.join()`, `super()`
- 参照: `this.dataType`

## ManageAddresses.getAddressL10nStrings()
- 位置: L317-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `l10nIds.reduce()`, `lazy.l10n.formatValueSync()`
- 参照: `lazy.FormAutofillUtils.EDIT_ADDRESS_L10N_IDS`, `lazy.FormAutofillUtils.MANAGE_ADDRESSES_L10N_IDS`

## ManageAddresses.openEditDialog()
- 位置: L337-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillPreferences.openEditAddressDialog()`
- 参照: `this.prefWin`

## ManageAddresses.getLabelInfo()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillUtils.getAddressLabel()`

## ManageCreditCards.constructor()
- 位置: L352-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutofillTelemetry.recordManageEvent()`, `elements.add.setAttribute()`, `lazy.FormAutofillUtils.EDIT_CREDITCARD_L10N_IDS.join()`, `super()`
- 参照: `this._isDecrypted`, `this.dataType`

## ManageCreditCards.openEditDialog()
- 位置: async L368-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillPreferences.openEditCreditCardDialog()`
- 参照: `this.prefWin`

## ManageCreditCards.getLabelInfo()
- 位置: async L382-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValue()`, `lazy.CreditCard.getLabelInfo()`, `lazy.CreditCard.getNetworkL10nId()`, `this.#withSecurityCodeLabel()`
- 参照: `FormAutofill.isAutofillCreditCardCVVEnabled`

## ManageCreditCards.#withSecurityCodeLabel()
- 位置: async L420-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatMessages()`, `message?.attributes?.find()`
- 参照: `attribute.name`, `message?.attributes?.find( attribute => attribute.name == "aria-label" )?.value`, `message?.value`

## ManageCreditCards.renderRecordElements()
- 位置: async L434-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.renderRecordElements()`, `this._elements.records.classList.toggle()`
- 条件付き依存: `if (record && record["cc-type"])` → `option.setAttribute()`
- 条件付き依存: `if (!(record && record["cc-type"]))` → `option.removeAttribute()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `option.record`, `this._elements.records.options`, `this._isDecrypted`

## ManageCreditCards.updateButtonsStates()
- 位置: L455-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updateButtonsStates()`

## ManageCreditCards.handleClick()
- 位置: L459-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.handleClick()`
