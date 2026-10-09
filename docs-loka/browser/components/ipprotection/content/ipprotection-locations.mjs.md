# browser/components/ipprotection/content/ipprotection-locations.mjs

source: browser/components/ipprotection/content/ipprotection-locations.mjs
source-hash: bd557c0cb4eab15c43cc3a3dbb7e6e511ce0e3ab
lines: 81

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## IPProtectionLocationsElement.constructor()
- 位置: L23-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.state`

## IPProtectionLocationsElement.createRenderRoot()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)

## IPProtectionLocationsElement.connectedCallback()
- 位置: L32-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.dispatchEvent()`

## IPProtectionLocationsElement.handlePromoButtonClick()
- 位置: L37-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.ipprotection.locationUpgradePromoClicked.record()`, `event.target.documentGlobal.openWebLinkIn()`
- 参照: `LINKS.LOCATION_PROMO_URL`

## IPProtectionLocationsElement.promoTemplate()
- 位置: L42-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handlePromoButtonClick`, `this.state?.hasUpgraded`, `this.state?.upgradeNotAvailable`

## IPProtectionLocationsElement.render()
- 位置: L63-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.promoTemplate()`
- 参照: `this.state.isPremium`, `this.state.location`, `this.state.locationsList`
