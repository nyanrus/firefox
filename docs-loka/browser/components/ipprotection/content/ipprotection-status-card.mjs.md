# browser/components/ipprotection/content/ipprotection-status-card.mjs

source: browser/components/ipprotection/content/ipprotection-status-card.mjs
source-hash: 793e39eb14190d8a33fabefbcc38a623f6065672
lines: 242

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## IPProtectionStatusCard.handleButtonClick()
- 位置: L51-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.#actionButtonFocused`, `this.TOGGLE_OFF_EVENT`, `this.TOGGLE_ON_EVENT`, `this.protectionEnabled`

## IPProtectionStatusCard.handleLocationButtonClick()
- 位置: L64-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `e.detail`, `this.locationButtonEl`

## IPProtectionStatusCard.updated()
- 位置: L77-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `super.updated()`, `this.actionButtonEl.updateComplete.then()`, `this.focus()`
- 参照: `this.#actionButtonFocused`, `this.isActivating`

## IPProtectionStatusCard.focus()
- 位置: L95-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`
- 条件付き依存: `if (!button?.disabled)` → `button?.focus()`
- 参照: `button?.disabled`

## IPProtectionStatusCard.bandwidthUsageTemplate()
- 位置: L102-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.bandwidthUsage`, `this.bandwidthUsage.max`, `this.bandwidthUsage.remaining`

## IPProtectionStatusCard.locationSelectionButtonTemplate()
- 位置: L113-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `countryName()`, `html()`
- 条件付き依存: `if (this.location)` → `lazy.IPProtectionServerlist.getLocation()`
- 参照: `countryObject?.country.locked`, `this.handleLocationButtonClick`, `this.isActivating`, `this.isPremium`, `this.location`, `this.showLocationButtonBadge`

## IPProtectionStatusCard.statusTemplate()
- 位置: L158-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.bandwidthUsageTemplate()`, `this.locationSelectionButtonTemplate()`
- 参照: `this.handleButtonClick`, `this.location`

## IPProtectionStatusCard.render()
- 位置: L202-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.statusTemplate()`
- 参照: `this.hasExclusion`, `this.isActivating`, `this.protectionEnabled`
