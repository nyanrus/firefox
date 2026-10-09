# browser/components/backup/content/password-validation-inputs.mjs

source: browser/components/backup/content/password-validation-inputs.mjs
source-hash: dfa6e7753d74e007424711232d24f06d1e226959
lines: 264

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## PasswordValidationInputs.queries()
- 位置: L33-41
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordValidationInputs.constructor()
- 位置: L43-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._hasEmail`, `this._passwordsMatch`, `this._passwordsValid`, `this._tooShort`

## PasswordValidationInputs.connectedCallback()
- 位置: L51-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `super.connectedCallback()`
- 参照: `this._onKeydown`

## this._onKeydown()
- 位置: L53-59
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.key === "Escape" && this.passwordRulesEl.open)` → `this.passwordRulesEl.hide()`
- 条件付き依存: `if (e.key === "Escape" && this.passwordRulesEl.open)` → `e.stopPropagation()`
- 条件付き依存: `if (e.key === "Escape" && this.passwordRulesEl.open)` → `e.preventDefault()`
- 参照: `e.key`, `this.passwordRulesEl.open`

## PasswordValidationInputs.disconnectedCallback()
- 位置: L62-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.removeEventListener()`, `super.disconnectedCallback()`
- 参照: `this._onKeydown`

## PasswordValidationInputs.setInputValidity()
- 位置: L67-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `input.setAttribute()`
- 条件付き依存: `if (describedById)` → `input.setAttribute()`
- 条件付き依存: `if (!(describedById))` → `input.removeAttribute()`

## PasswordValidationInputs.reset()
- 位置: L76-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.formEl?.reset()`, `this.passwordRulesEl.hide()`
- 条件付き依存: `if (this.inputNewPasswordEl)` → `this.setInputValidity()`
- 条件付き依存: `if (this.inputRepeatPasswordEl)` → `this.setInputValidity()`
- 参照: `this._hasEmail`, `this._passwordsMatch`, `this._passwordsValid`, `this._tooShort`, `this.inputNewPasswordEl`, `this.inputNewPasswordEl.revealPassword`, `this.inputRepeatPasswordEl`, `this.inputRepeatPasswordEl.revealPassword`

## PasswordValidationInputs.handleFocusNewPassword()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.passwordRulesEl.show()`

## PasswordValidationInputs.handleBlurNewPassword()
- 位置: L97-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.checkValidity()`
- 条件付き依存: `if (event.target.checkValidity())` → `this.passwordRulesEl.hide()`

## PasswordValidationInputs.handleChangeNewPassword()
- 位置: L103-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePasswordValidity()`

## PasswordValidationInputs.handleChangeRepeatPassword()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePasswordValidity()`

## PasswordValidationInputs.updatePasswordValidity()
- 位置: L111-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emailRegex.test()`, `this.setInputValidity()`
- 条件付き依存: `if (this._hasEmail)` → `l10n.formatValueSync()`
- 条件付き依存: `if (this._hasEmail)` → `this.inputNewPasswordEl.setCustomValidity()`
- 条件付き依存: `if (!(this._hasEmail))` → `this.inputNewPasswordEl.setCustomValidity()`
- 条件付き依存: `if (!this._passwordsMatch)` → `this.inputRepeatPasswordEl.setCustomValidity()`
- 条件付き依存: `if (!this._passwordsMatch)` → `l10n.formatValueSync()`
- 条件付き依存: `if (!this._passwordsMatch)` → `this.setInputValidity()`
- 条件付き依存: `if (!this._passwordsMatch)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(!this._passwordsMatch))` → `this.inputRepeatPasswordEl.setCustomValidity()`
- 条件付き依存: `if (!(!this._passwordsMatch))` → `this.setInputValidity()`
- 参照: `newPassValidity?.tooShort`, `newPassValidity?.valid`, `newPassValidity?.valueMissing`, `repeatPassValidity?.valid`, `this._hasEmail`, `this._passwordsMatch`, `this._passwordsValid`, `this._tooShort`, `this.inputNewPasswordEl`, `this.inputNewPasswordEl.validity`, `this.inputNewPasswordEl.value`, `this.inputRepeatPasswordEl`, `this.inputRepeatPasswordEl.validity`, `this.inputRepeatPasswordEl.value`, `this.repeatPasswordErrorEl`

## PasswordValidationInputs.updated()
- 位置: L171-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`
- 条件付き依存: `if (this._passwordsValid)` → `this.dispatchEvent()`
- 条件付き依存: `if (!(this._passwordsValid))` → `this.dispatchEvent()`
- 参照: `this._passwordsValid`, `this.inputNewPasswordEl.value`

## PasswordValidationInputs.contentTemplate()
- 位置: L196-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this._hasEmail`, `this._tooShort`, `this.createPasswordLabelL10nId`, `this.embeddedFxBackupOptIn`, `this.handleBlurNewPassword`, `this.handleChangeNewPassword`, `this.handleChangeRepeatPassword`, `this.handleFocusNewPassword`

## PasswordValidationInputs.render()
- 位置: L252-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.contentTemplate()`
