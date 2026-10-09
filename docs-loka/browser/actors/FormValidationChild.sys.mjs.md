# browser/actors/FormValidationChild.sys.mjs

source: browser/actors/FormValidationChild.sys.mjs
source-hash: 428962d87b73a10440da8f86158bc975f9a50575
lines: 198

## <module>
- 役割: (未記入)

## FormValidationChild.constructor()
- 位置: L11-15
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._element`, `this._validationMessage`

## FormValidationChild.handleEvent()
- 位置: L21-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.preventDefault()`, `this._isRootDocumentEvent()`, `this._onBlur()`, `this._onInput()`, `this.notifyInvalidSubmit()`
- 条件付き依存: `if (this._isRootDocumentEvent(aEvent))` → `this._hidePopup()`
- 参照: `aEvent.detail`, `aEvent.type`

## FormValidationChild.notifyInvalidSubmit()
- 位置: L46-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getClassName()`, `Services.focus.elementIsFocusable()`, `element.addEventListener()`, `element.focus()`, `this._showPopup()`
- 条件付き依存: `if (this._element == element)` → `this._showPopup()`
- 参照: `element.documentGlobal`, `element.internals.validationAnchor`, `element.internals.validationMessage`, `element.isFormAssociatedCustomElement`, `element.validationMessage`, `this._element`, `this._validationMessage`, `this.contentWindow`
- XPCOM: `Services.focus`

## FormValidationChild._onInput()
- 位置: L118-133
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (element.validity.valid)` → `this._hidePopup()`
- 条件付き依存: `if (this._validationMessage != element.validationMessage)` → `this._showPopup()`
- 参照: `aEvent.originalTarget`, `element.validationMessage`, `element.validity.valid`, `this._validationMessage`

## FormValidationChild._onBlur()
- 位置: L139-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hidePopup()`
- 条件付き依存: `if (this._element)` → `this._element.removeEventListener()`
- 参照: `this._element`

## FormValidationChild._showPopup()
- 位置: L153-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`, `win.addEventListener()`, `win.windowUtils.getElementBoundingScreenRect()`
- 参照: `aElement.documentGlobal`, `aElement.tagName`, `aElement.type`, `panelData.message`, `panelData.position`, `panelData.screenRect`, `this._validationMessage`

## FormValidationChild._hidePopup()
- 位置: L180-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._element.documentGlobal.removeEventListener()`, `this.sendAsyncMessage()`

## FormValidationChild._isRootDocumentEvent()
- 位置: L187-196
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aEvent.originalTarget`, `target.ownerDocument`, `this.contentWindow`, `this.document`
