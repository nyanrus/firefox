# browser/components/protections/content/vpn-card.mjs

source: browser/components/protections/content/vpn-card.mjs
source-hash: 80f4d5b925c7fd2dbdcd0ed90fb5c1414d38cbf1
lines: 104

## <module>
- 役割: (未記入)

## VPNCard.constructor()
- 位置: L6-8
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.doc`

## VPNCard.init()
- 位置: L10-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMGetStringPref()`, `androidVPNAppLink.addEventListener()`, `document.getElementById()`, `document.sendTelemetryEvent()`, `exitIcon.addEventListener()`, `iosVPNAppLink.addEventListener()`, `this.doc.getElementById()`, `this.doc.querySelector()`, `this.doc.sendTelemetryEvent()`, `this.showVPNCard()`, `vpnBanner.classList.add()`, `vpnBanner.querySelector()`, `vpnBannerLink.addEventListener()`, `vpnLink.addEventListener()`
- 参照: `androidVPNAppLink.href`, `iosVPNAppLink.href`, `vpnBannerLink.href`, `vpnLink.href`

## VPNCard.showVPNCard()
- 位置: async L57-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `RPMSendQuery("FetchShowVPNCard", {}).then()`, `RPMSendQuery("FetchVPNSubStatus", {}).then()`, `showVPNBanner()`, `this.doc.querySelector()`, `this.showVPNBanner.bind()`, `vpnCard.classList.remove()`
- 条件付き依存: `if (hasVPN)` → `vpnCard.classList.add()`
- 条件付き依存: `if (hasVPN)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (hasVPN)` → `vpnCard.querySelector()`
- 条件付き依存: `if (hasVPN)` → `RPMSetPref( "browser.contentblocking.report.hide_vpn_banner", true ).catch()`
- 条件付き依存: `if (hasVPN)` → `RPMSetPref()`

## VPNCard.showVPNBanner()
- 位置: L87-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMGetBoolPref()`, `RPMSetPref()`, `RPMSetPref("browser.contentblocking.report.hide_vpn_banner", true).catch()`, `this.doc.querySelector()`, `this.doc.sendTelemetryEvent()`, `vpnBanner.classList.remove()`
