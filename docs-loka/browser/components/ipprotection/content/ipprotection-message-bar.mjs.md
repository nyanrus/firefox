# browser/components/ipprotection/content/ipprotection-message-bar.mjs

source: browser/components/ipprotection/content/ipprotection-message-bar.mjs
source-hash: c5f1b090c65921e417b0666ad04708fece742771
lines: 134

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`, `this.infoMessageTemplate()`, `this.warningMessageTemplate()`

## IPProtectionMessageBarElement.constructor()
- 位置: L40-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.handleClickSettingsLink.bind()`, `this.handleDismiss.bind()`
- 参照: `this.handleClickSettingsLink`, `this.handleDismiss`

## IPProtectionMessageBarElement.connectedCallback()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`

## IPProtectionMessageBarElement.disconnectedCallback()
- 位置: L51-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.mozMessageBarEl)` → `this.mozMessageBarEl.removeEventListener()`
- 参照: `this.handleDismiss`, `this.mozMessageBarEl`

## IPProtectionMessageBarElement.handleDismiss()
- 位置: L62-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.DISMISS_EVENT`

## IPProtectionMessageBarElement.infoMessageTemplate()
- 位置: L70-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.handleClickSettingsLink`, `this.messageId`, `this.messageLink`, `this.messageLinkl10nId`

## IPProtectionMessageBarElement.warningMessageTemplate()
- 位置: L87-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.messageId`, `this.messageLinkL10nArgs`

## IPProtectionMessageBarElement.firstUpdated()
- 位置: L99-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.mozMessageBarEl.addEventListener()`
- 参照: `this.handleDismiss`

## IPProtectionMessageBarElement.handleClickSettingsLink()
- 位置: L109-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.hasAttribute()`
- 条件付き依存: `if (event.target.hasAttribute("href"))` → `event.preventDefault()`
- 条件付き依存: `if (event.target.hasAttribute("href"))` → `lazy.URILoadingHelper.openTrustedLinkIn()`
- 条件付き依存: `if (event.target.hasAttribute("href"))` → `this.dispatchEvent()`
- 参照: `this.messageLink`

## IPProtectionMessageBarElement.render()
- 位置: L120-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `templateFn()`, `this.#MESSAGE_TYPE_MAP.get()`
- 参照: `this.type`
