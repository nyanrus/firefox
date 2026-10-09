# browser/components/backup/content/password-rules-tooltip.mjs

source: browser/components/backup/content/password-rules-tooltip.mjs
source-hash: 302eaec4d1c7c180e2517d974de9235643b86571
lines: 127

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## PasswordRulesTooltip.queries()
- 位置: L19-23
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordRulesTooltip.constructor()
- 位置: L25-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._onResize`, `this.hasEmail`, `this.tooShort`

## PasswordRulesTooltip._debounce()
- 位置: L32-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `fn()`, `setTimeout()`

## PasswordRulesTooltip._handleResize()
- 位置: L40-44
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.open)` → `this.positionPopover()`
- 参照: `this.open`

## PasswordRulesTooltip.connectedCallback()
- 位置: L46-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this._debounce()`, `this._handleResize()`, `window.addEventListener()`
- 参照: `this._onResize`

## PasswordRulesTooltip.disconnectedCallback()
- 位置: L52-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this._onResize)` → `window.removeEventListener()`
- 参照: `this._onResize`

## PasswordRulesTooltip.show()
- 位置: L59-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.passwordRulesEl.showPopover()`, `this.positionPopover()`

## PasswordRulesTooltip.hide()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.passwordRulesEl.hidePopover()`

## PasswordRulesTooltip.positionPopover()
- 位置: L68-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBoundingClientRect()`
- 参照: `anchorRect.bottom`, `anchorRect.height`, `anchorRect.top`, `document.dir`, `popover.style.left`, `popover.style.right`, `popover.style.top`, `this.passwordRulesEl`, `window.innerWidth`

## PasswordRulesTooltip._onBeforeToggle()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `e.newState`, `this.open`

## PasswordRulesTooltip.render()
- 位置: L88-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this._onBeforeToggle`, `this.hasEmail`, `this.tooShort`
