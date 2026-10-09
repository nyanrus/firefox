# browser/components/genai/content/model-optin.mjs

source: browser/components/genai/content/model-optin.mjs
source-hash: a44a7c788a221b976ecabf0ef37ff33a67c3da13
lines: 185

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ModelOptin.constructor()
- 位置: L42-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.cancelDownloadButtonL10nId`, `this.footerMessageL10nId`, `this.iconAtEnd`, `this.isHidden`, `this.isLoading`, `this.optinButtonL10nId`, `this.optoutButtonL10nId`

## ModelOptin.dispatch()
- 位置: L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## ModelOptin.handleConfirmClick()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatch()`
- 参照: `ModelOptin.events.confirm`

## ModelOptin.handleDenyClick()
- 位置: L63-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatch()`
- 参照: `ModelOptin.events.deny`, `this.isHidden`

## ModelOptin.handleCancelDownloadClick()
- 位置: L68-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatch()`
- 参照: `ModelOptin.events.cancelDownload`, `this.isLoading`, `this.progressStatus`

## ModelOptin.handleMessageLinkClick()
- 位置: L74-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatch()`
- 参照: `ModelOptin.events.messageLinkClick`, `e.target.id`

## ModelOptin.handleFooterLinkClick()
- 位置: L82-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatch()`
- 参照: `ModelOptin.events.footerLinkClick`, `e.target.id`

## ModelOptin.render()
- 位置: L90-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.cancelDownloadButtonL10nId`, `this.footerMessageL10nId`, `this.handleCancelDownloadClick`, `this.handleConfirmClick`, `this.handleDenyClick`, `this.handleFooterLinkClick`, `this.handleMessageLinkClick`, `this.headingIcon`, `this.headingL10nId`, `this.iconAtEnd`, `this.isHidden`, `this.isLoading`, `this.messageL10nId`, `this.optinButtonL10nId`, `this.optoutButtonL10nId`, `this.progressStatus`
