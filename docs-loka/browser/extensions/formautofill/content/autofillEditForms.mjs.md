# browser/extensions/formautofill/content/autofillEditForms.mjs

source: browser/extensions/formautofill/content/autofillEditForms.mjs
source-hash: f4cc1e50aa6dc81984590b1b7d1104415d294b4e
lines: 557

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## EditAutofillForm.constructor()
- 位置: L14-16
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._elements`

## EditAutofillForm.loadRecord()
- 位置: L23-37
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!record.guid)` → `this._elements.form.reset()`
- 条件付き依存: `if (!(!record.guid))` → `this.updateCustomValidity()`
- 参照: `field.id`, `field.value`, `record.guid`, `this._elements.form.elements`

## EditAutofillForm.buildFormObject()
- 位置: L44-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this._elements.form.elements).reduce()`
- 参照: `input.disabled`, `input.id`, `input.value`, `this._elements.form.elements`, `this.hasMailingAddressFields`

## EditAutofillForm.handleEvent()
- 位置: L71-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleChange()`, `this.handleInput()`
- 参照: `event.type`

## EditAutofillForm.handleChange()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.removeAttribute()`

## EditAutofillForm.handleInput()
- 位置: L89-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.removeAttribute()`

## EditAutofillForm.attachEventListeners()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._elements.form.addEventListener()`

## EditAutofillForm.updateCustomValidity()
- 位置: L105-105
- 役割: (未記入)
- 触るとき: (未記入)

## EditCreditCard.constructor()
- 位置: L114-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `super()`, `this.#setupSecurityCodeField()`, `this._elements.form.querySelector()`, `this.attachEventListeners()`, `this.loadRecord()`
- 参照: `this._addresses`, `this._elements`

## EditCreditCard.#setupSecurityCodeField()
- 位置: L142-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `securityCode.updateComplete.then()`, `this._elements.form.classList.add()`
- 条件付き依存: `if (!lazy.FormAutofill.isAutofillCreditCardCVVEnabled)` → `securityCode.remove()`
- 参照: `lazy.FormAutofill.isAutofillCreditCardCVVEnabled`, `securityCode.inputEl.maxLength`, `securityCode.inputEl.pattern`, `this._elements.securityCode`, `this._elements.securityCodeContainer.hidden`

## EditCreditCard.loadRecord()
- 位置: L161-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.generateBillingAddressOptions()`
- 条件付き依存: `if (!preserveFieldValues)` → `this.generateMonths()`
- 条件付き依存: `if (!preserveFieldValues)` → `this.generateYears()`
- 条件付き依存: `if (!preserveFieldValues)` → `super.loadRecord()`
- 条件付き依存: `if (!preserveFieldValues)` → `this.#applySelectValues()`
- 参照: `this._addresses`, `this._record`

## EditCreditCard.#applySelectValues()
- 位置: async L180-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `selects.map()`, `value.toString()`
- 参照: `select.id`, `select.updateComplete`, `select.value`, `this._elements.billingAddress`, `this._elements.month`, `this._elements.year`

## EditCreditCard.generateMonths()
- 位置: L193-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(i + 1).toString()`, `dateFormat()`, `document.createElement()`, `emptyOption.setAttribute()`, `monthNumber.padStart()`, `option.setAttribute()`, `this._elements.month.appendChild()`
- 参照: `Intl.DateTimeFormat`, `navigator.language`, `new Intl.DateTimeFormat(navigator.language, { month: "long", }).format`, `this._elements.month.textContent`

## EditCreditCard.generateYears()
- 位置: L223-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `document.createElement()`, `emptyOption.setAttribute()`, `new Date().getFullYear()`, `option.setAttribute()`, `this._elements.year.appendChild()`
- 条件付き依存: `if (ccExpYear && ccExpYear < currentYear)` → `document.createElement()`
- 条件付き依存: `if (ccExpYear && ccExpYear < currentYear)` → `option.setAttribute()`
- 条件付き依存: `if (ccExpYear && ccExpYear < currentYear)` → `String()`
- 条件付き依存: `if (ccExpYear && ccExpYear < currentYear)` → `this._elements.year.appendChild()`
- 条件付き依存: `if (ccExpYear && ccExpYear > currentYear + count)` → `document.createElement()`
- 条件付き依存: `if (ccExpYear && ccExpYear > currentYear + count)` → `option.setAttribute()`
- 条件付き依存: `if (ccExpYear && ccExpYear > currentYear + count)` → `String()`
- 条件付き依存: `if (ccExpYear && ccExpYear > currentYear + count)` → `this._elements.year.appendChild()`
- 参照: `this._elements.year.textContent`, `this._record`

## EditCreditCard.generateBillingAddressOptions()
- 位置: L260-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `document.createElement()`, `emptyOption.setAttribute()`, `lazy.FormAutofillUtils.getAddressLabel()`, `option.setAttribute()`, `this._elements.billingAddress.appendChild()`
- 参照: `this._addresses`, `this._elements.billingAddress.textContent`, `this._elements.billingAddress.value`, `this._elements.billingAddressRow.hidden`, `this._record`, `this._record.billingAddressGUID`

## EditCreditCard.attachEventListeners()
- 位置: L294-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.attachEventListeners()`, `this._elements.form.addEventListener()`

## EditCreditCard.handleInput()
- 位置: L299-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillUtils.isCCNumber()`, `super.handleInput()`
- 条件付き依存: `if (inputEl)` → `inputEl.setCustomValidity()`
- 参照: `event.target`, `this._elements.ccNumber`, `this._elements.ccNumber.inputEl`, `this._elements.ccNumber.value`

## EditCreditCard.setupValidation()
- 位置: L317-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._elements.form.querySelector()`
- 参照: `ccEl.inputEl.minLength`, `ccEl.inputEl.pattern`, `ccEl.inputEl.required`, `ccEl?.inputEl`, `el.inputEl.required`, `el?.inputEl`, `this._elements.ccNumber`, `this._validationSetup`

## EditCreditCard.validateForm()
- 位置: L343-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setupValidation()`
- 条件付き依存: `if (field.inputEl)` → `field.inputEl.checkValidity()`
- 条件付き依存: `if (field.inputEl)` → `field.toggleAttribute()`
- 条件付き依存: `if (firstInvalidField)` → `firstInvalidField.inputEl.reportValidity()`
- 参照: `field.inputEl`, `this._elements.form.elements`

## EditCreditCard.updateCustomValidity()
- 位置: L362-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillUtils.isCCNumber()`, `super.updateCustomValidity()`
- 条件付き依存: `if (inputEl)` → `inputEl.setCustomValidity()`
- 参照: `field.inputEl`, `field.value`, `this._elements.ccNumber`, `this._elements.invalidCardNumberStringElement.textContent`

## EditPassport.constructor()
- 位置: L385-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `super()`, `this._elements.form.querySelector()`, `this.attachEventListeners()`, `this.loadRecord()`
- 参照: `this._elements`

## EditPassport.loadRecord()
- 位置: L408-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.loadRecord()`, `this.#applySelectValues()`, `this.generateDays()`, `this.generateMonths()`, `this.generateYears()`
- 参照: `this._elements.expiryDay`, `this._elements.expiryMonth`, `this._elements.expiryYear`, `this._elements.issueDay`, `this._elements.issueMonth`, `this._elements.issueYear`, `this._record`

## EditPassport.#applySelectValues()
- 位置: async L430-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `selects.map()`, `value.toString()`
- 参照: `select.id`, `select.updateComplete`, `select.value`, `this._elements.country`, `this._elements.expiryDay`, `this._elements.expiryMonth`, `this._elements.expiryYear`, `this._elements.issueDay`, `this._elements.issueMonth`, `this._elements.issueYear`

## EditPassport.#createOption()
- 位置: L447-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `option.setAttribute()`

## EditPassport.generateMonths()
- 位置: L454-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `i.toString()`, `i.toString().padStart()`, `select.appendChild()`, `this.#createOption()`
- 参照: `select.textContent`

## EditPassport.generateDays()
- 位置: L468-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `i.toString()`, `i.toString().padStart()`, `select.appendChild()`, `this.#createOption()`
- 参照: `select.textContent`

## EditPassport.generateYears()
- 位置: L482-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date().getFullYear()`, `select.appendChild()`, `this.#createOption()`, `year.toString()`
- 条件付き依存: `if (storedYear && storedYear < currentYear - count)` → `select.appendChild()`
- 条件付き依存: `if (storedYear && storedYear < currentYear - count)` → `this.#createOption()`
- 条件付き依存: `if (storedYear && storedYear < currentYear - count)` → `storedYear.toString()`
- 条件付き依存: `if (storedYear && storedYear > currentYear + count)` → `select.appendChild()`
- 条件付き依存: `if (storedYear && storedYear > currentYear + count)` → `this.#createOption()`
- 条件付き依存: `if (storedYear && storedYear > currentYear + count)` → `storedYear.toString()`
- 参照: `select.textContent`

## EditPassport.attachEventListeners()
- 位置: L512-515
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.attachEventListeners()`, `this._elements.form.addEventListener()`

## EditPassport.setupValidation()
- 位置: L521-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._elements.form.querySelector()`
- 参照: `numberEl.inputEl.required`, `numberEl?.inputEl`, `this._validationSetup`

## EditPassport.validateForm()
- 位置: L538-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setupValidation()`
- 条件付き依存: `if (field.inputEl)` → `field.inputEl.checkValidity()`
- 条件付き依存: `if (field.inputEl)` → `field.toggleAttribute()`
- 条件付き依存: `if (firstInvalidField)` → `firstInvalidField.inputEl.reportValidity()`
- 参照: `field.inputEl`, `this._elements.form.elements`
