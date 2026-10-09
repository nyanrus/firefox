# browser/components/preferences/moreFromMozilla.js

source: browser/components/preferences/moreFromMozilla.js
source-hash: c9db86e4155d23e9f0989f201a2bd5afa383ad5e
lines: 297

## <module>
- 役割: (未記入)

## option()
- 位置: L16-25
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._option`

## option()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._option`

## getTemplateName()
- 位置: L31-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._option`

## getURL()
- 位置: L38-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `pageUrl.searchParams.append()`, `pageUrl.toString()`
- 条件付き依存: `if (option)` → `pageUrl.searchParams.set()`
- 条件付き依存: `if (option !== "default")` → `pageUrl.searchParams.set()`
- 参照: `experiment_params.entrypoint_experiment`

## renderProducts()
- 位置: L82-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.shouldShowPromo()`, `BrowserUtils.shouldShowVPNPromo()`, `Region.home.toLowerCase()`, `document.createDocumentFragment()`, `document.getElementById()`, `document.l10n.setAttributes()`, `frag.appendChild()`, `products.push()`, `template.querySelector()`, `this._productsContainer.appendChild()`, `this._template.content.cloneNode()`, `this.getTemplateName()`
- 条件付き依存: `if (BrowserUtils.shouldShowVPNPromo())` → `products.push()`
- 条件付き依存: `if (BrowserUtils.shouldShowPromo(BrowserUtils.PromoType.RELAY))` → `products.push()`
- 条件付き依存: `if (actionElement)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (isLink)` → `actionElement.setAttribute()`
- 条件付き依存: `if (isLink)` → `this.getURL()`
- 条件付き依存: `if (!(isLink))` → `actionElement.addEventListener()`
- 条件付き依存: `if (!(isLink))` → `mainWindow.openTrustedLinkIn()`
- 条件付き依存: `if (!(isLink))` → `gMoreFromMozillaPane.getURL()`
- 条件付き依存: `if (product.qrcode)` → `template.querySelector()`
- 条件付き依存: `if (product.qrcode)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (product.qrcode)` → `this.getTemplateName()`
- 条件付き依存: `if (product.qrcode)` → `BrowserUtils.sendToDeviceEmailsSupported()`
- 条件付き依存: `if (BrowserUtils.sendToDeviceEmailsSupported())` → `document.l10n.setAttributes()`
- 条件付き依存: `if (BrowserUtils.sendToDeviceEmailsSupported())` → `this.getURL()`
- 参照: `BrowserUtils.PromoType.RELAY`, `actionElement.hidden`, `actionElement.id`, `gMoreFromMozillaPane.option`, `img.src`, `product.button.actionURL`, `product.button.id`, `product.button.label_string_id`, `product.button.type`, `product.description_string_id`, `product.id`, `product.qrcode`, `product.qrcode.button.actionURL`, `product.qrcode.button.id`, `product.qrcode.button.label.string_id`, `product.qrcode.image_src_prefix`, `product.qrcode.title.string_id`, `product.region`, `product.title_string_id`, `qrc_link.hidden`, `qrc_link.href`, `qrc_link.id`, `qrcode.hidden`, `this._productsContainer`, `this._template`, `this.option`, `title.id`, `window.windowRoot.window`

## init()
- 位置: async L282-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("moreFromMozillaCategory") .removeAttribute()`, `document .getElementById("moreFromMozillaCategory-header") .removeAttribute()`, `this.renderProducts()`
- 参照: `this.initialized`
