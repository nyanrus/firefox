# browser/components/ipprotection/content/ipprotection-utils.mjs

source: browser/components/ipprotection/content/ipprotection-utils.mjs
source-hash: 26fabd12548eb8d05a418eb0e5fa97f9d9f824ad
lines: 78

## <module>
- 役割: (未記入)

## countryName()
- 位置: L17-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `countryDisplayNames.of()`

## formatRemainingBandwidth()
- 位置: L35-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.NumberFormat(locale, { maximumFractionDigits: 1, }).format()`
- 条件付き依存: `if (remainingGB < 1)` → `Math.floor()`
- 参照: `BANDWIDTH.BYTES_IN_GB`, `BANDWIDTH.BYTES_IN_MB`, `Intl.NumberFormat`

## getSitePrincipal()
- 位置: L66-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `gBrowser.selectedBrowser?.browsingContext?.originAttributes`, `gBrowser?.currentURI`
- XPCOM: `Services.scriptSecurityManager`
