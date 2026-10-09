# browser/components/ipprotection/content/bandwidth-usage.mjs

source: browser/components/ipprotection/content/bandwidth-usage.mjs
source-hash: b2e1690f383a29023c2105a371869044b39bd0f8
lines: 186

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## BandwidthUsageCustomElement.bandwidthPercent()
- 位置: L30-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`
- 参照: `this.bandwidthUsed`, `this.max`

## BandwidthUsageCustomElement.remainingMB()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANDWIDTH.BYTES_IN_MB`, `this.remaining`

## BandwidthUsageCustomElement.remainingGB()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANDWIDTH.BYTES_IN_GB`, `this.remaining`

## BandwidthUsageCustomElement.maxGB()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANDWIDTH.BYTES_IN_GB`, `this.max`

## BandwidthUsageCustomElement.bandwidthUsed()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.max`, `this.remaining`

## BandwidthUsageCustomElement.bandwidthUsedGB()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANDWIDTH.BYTES_IN_GB`, `this.max`, `this.remaining`

## BandwidthUsageCustomElement.remainingRounded()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatRemainingBandwidth()`
- 参照: `formatRemainingBandwidth(this.remaining).value`, `this.remaining`

## BandwidthUsageCustomElement.bandwidthLeftDataL10nId()
- 位置: L64-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatRemainingBandwidth()`
- 参照: `formatRemainingBandwidth(this.remaining).useGB`, `this.remaining`

## BandwidthUsageCustomElement.bandwidthLeftThisMonthDataL10nId()
- 位置: L70-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formatRemainingBandwidth()`
- 参照: `formatRemainingBandwidth(this.remaining).useGB`, `this.remaining`

## BandwidthUsageCustomElement.constructor()
- 位置: L76-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.numeric`

## BandwidthUsageCustomElement.progressBarTemplate()
- 位置: L81-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `parseFloat()`, `this.bandwidthUsedGB.toFixed()`
- 条件付き依存: `if (this.remaining > 0)` → `html()`
- 条件付き依存: `if (this.remaining > 0)` → `JSON.stringify()`
- 条件付き依存: `if (!(this.remaining > 0))` → `html()`
- 条件付き依存: `if (!(this.remaining > 0))` → `JSON.stringify()`
- 参照: `LINKS.SUPPORT_SLUG`, `this.bandwidthLeftDataL10nId`, `this.bandwidthPercent`, `this.maxGB`, `this.numeric`, `this.remaining`, `this.remainingRounded`

## BandwidthUsageCustomElement.numericTemplate()
- 位置: L145-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 条件付き依存: `if (this.remaining > 0)` → `html()`
- 条件付き依存: `if (this.remaining > 0)` → `JSON.stringify()`
- 参照: `this.bandwidthLeftThisMonthDataL10nId`, `this.maxGB`, `this.numeric`, `this.remaining`, `this.remainingRounded`

## BandwidthUsageCustomElement.render()
- 位置: L170-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (this.numeric)` → `this.numericTemplate()`
- 条件付き依存: `if (!(this.numeric))` → `this.progressBarTemplate()`
- 参照: `this.numeric`
