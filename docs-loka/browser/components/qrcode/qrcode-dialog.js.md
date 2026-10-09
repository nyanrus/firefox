# browser/components/qrcode/qrcode-dialog.js

source: browser/components/qrcode/qrcode-dialog.js
source-hash: 42764d484a66db55899c8b121c04de3c7c7d00dd
lines: 194

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `QRCodeDialog.init()`, `XPCOMUtils.defineLazyServiceGetter()`, `window.addEventListener()`

## init()
- 位置: L29-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `copyButton.addEventListener()`, `document .getElementById()`, `document .getElementById("close-button") .addEventListener()`, `document .getElementById("save-button") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `event.target.closest()`, `this.copyImage()`, `this.saveImage()`, `this.setupDialog()`, `window.close()`
- 条件付き依存: `if ( event.key === "Enter" && !event.defaultPrevented && !event.target.closest("moz-button") )` → `event.preventDefault()`
- 条件付き依存: `if ( event.key === "Enter" && !event.defaultPrevented && !event.target.closest("moz-button") )` → `this.copyImage()`
- 参照: `document.mozSubdialogReady`, `document.subDialogSetDefaultFocus`, `event.defaultPrevented`, `event.key`, `params.qrCodeDataURI`, `params.url`, `this._qrCodeDataURI`, `this._url`, `window.arguments`

## document.subDialogSetDefaultFocus()
- 位置: L40-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `copyButton.focus()`

## setupDialog()
- 位置: async L66-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (!this._qrCodeDataURI)` → `this.showFeedback()`
- 参照: `imageElement.src`, `successContainer.hidden`, `this._qrCodeDataURI`, `this._url`, `urlElement.textContent`, `urlElement.title`

## showFeedback()
- 位置: async L90-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `window.resizeDialog()`
- 条件付き依存: `if (!bar)` → `document.createElement()`
- 条件付き依存: `if (!bar)` → `bar.setAttribute()`
- 条件付き依存: `if (!bar)` → `bar.addEventListener()`
- 条件付き依存: `if (!bar)` → `requestAnimationFrame()`
- 条件付き依存: `if (!bar)` → `window.resizeDialog()`
- 条件付き依存: `if (!bar)` → `document.getElementById()`
- 条件付き依存: `if (!bar)` → `content.appendChild()`
- 参照: `bar.id`, `bar.type`, `bar.updateComplete`

## decodeDataURI()
- 位置: L117-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Uint8Array.fromBase64()`, `this._qrCodeDataURI.slice()`, `this._qrCodeDataURI?.startsWith()`
- 参照: `dataPrefix.length`

## copyImage()
- 位置: async L127-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `navigator.clipboard.write()`, `this.decodeDataURI()`, `this.showFeedback()`

## saveImage()
- 位置: async L142-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getSchemelessSite()`, `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `chromeWindow.internalSave()`, `document.l10n.formatValues()`, `lazy.IDNService.domainToDisplay()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `this._qrCodeDataURI`, `this._url`, `uri.host`, `window.browsingContext.topChromeWindow`
- XPCOM: `Services.eTLD` / `Services.io` / `Services.scriptSecurityManager`
