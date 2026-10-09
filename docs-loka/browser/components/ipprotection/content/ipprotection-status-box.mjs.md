# browser/components/ipprotection/content/ipprotection-status-box.mjs

source: browser/components/ipprotection/content/ipprotection-status-box.mjs
source-hash: 0569d782f86956bef053e2ee30f3ab5bdab744ff
lines: 127

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## IPProtectionStatusBox.constructor()
- 位置: L30-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#keyListener.bind()`
- 参照: `this.keyListener`

## IPProtectionStatusBox.connectedCallback()
- 位置: L36-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`
- 参照: `this.keyListener`

## IPProtectionStatusBox.disconnectedCallback()
- 位置: L41-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this.keyListener`

## IPProtectionStatusBox.focus()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.connectionButtonEl?.focus()`

## IPProtectionStatusBox.#keyListener()
- 位置: L51-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.moveFocus()`, `event.preventDefault()`, `event.stopPropagation()`
- 参照: `Services.focus.FLAG_BYKEY`, `Services.focus.MOVEFOCUS_BACKWARD`, `Services.focus.MOVEFOCUS_FORWARD`, `event.code`
- XPCOM: `Services.focus`

## IPProtectionStatusBox.render()
- 位置: L75-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.descriptionL10nArgs`, `this.descriptionL10nId`, `this.descriptionSupportSlug`, `this.headerL10nId`, `this.type`
