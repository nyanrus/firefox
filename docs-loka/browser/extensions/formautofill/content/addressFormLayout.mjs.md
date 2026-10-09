# browser/extensions/formautofill/content/addressFormLayout.mjs

source: browser/extensions/formautofill/content/addressFormLayout.mjs
source-hash: a43973714899210041919581eed17e297b69e3e9
lines: 238

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## commonAttributes()
- 位置: L13-19
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `item.fieldId`, `item.value`

## "moz-input-text"()
- 位置: L20-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.commonAttributes()`

## "moz-textarea"()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.commonAttributes()`

## "moz-select"()
- 位置: L32-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.options.map()`, `this.commonAttributes()`

## createElement()
- 位置: L54-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `createElement()`, `document.createElement()`, `element.appendChild()`
- 条件付き依存: `if (!(attributeName in element))` → `element.setAttribute()`

## convertLayoutToUI()
- 位置: L79-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.appendChild()`, `createElement()`, `field.setAttribute()`, `fieldTemplates[fieldTag]()`
- 参照: `field.dataset.pattern`, `field.dataset.required`, `field.dataset.type`, `item.fieldId`, `item.l10nId`, `item.multiline`, `item.newLine`, `item.options`, `item.pattern`, `item.required`, `item.type`

## getCurrentFormData()
- 位置: L119-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 参照: `document.querySelector("form").elements`, `element.name`, `element.value`

## canSubmitForm()
- 位置: L133-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(formData).filter()`, `getCurrentFormData()`
- 参照: `validValues.length`

## validateAddressForm()
- 位置: L144-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `field.inputEl.checkValidity()`, `field.toggleAttribute()`
- 条件付き依存: `if (firstInvalidField)` → `firstInvalidField.inputEl.reportValidity()`
- 参照: `field.dataset.pattern`, `field.dataset.required`, `field.dataset.type`, `field.inputEl`, `field.inputEl.pattern`, `field.inputEl.required`, `field.inputEl.type`, `form.elements`

## createFormLayoutFromRecord()
- 位置: L180-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `convertLayoutToUI()`, `createFormLayoutFromRecord()`, `document.querySelector()`, `document.querySelector("#country").addEventListener()`, `fields.findIndex()`, `formElement.appendChild()`, `formElement.querySelectorAll()`, `getCurrentFormData()`, `lazy.FormAutofillUtils.getFormLayout()`, `setTimeout()`, `window.dispatchEvent()`
- 条件付き依存: `if (countryIdx > -1)` → `Math.max()`
- 条件付き依存: `if (countryIdx > -1)` → `fields.findIndex()`
- 条件付き依存: `if (anchorIdx > -1 && countryIdx > anchorIdx + 1)` → `fields.splice()`
- 参照: `ev.target.value`, `f.fieldId`, `formElement.innerHTML`, `lazy.FormAutofill.DEFAULT_REGION`, `record.country`, `select.value`
