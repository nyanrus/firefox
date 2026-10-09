# browser/components/ipprotection/content/ipprotection-unauthenticated.mjs

source: browser/components/ipprotection/content/ipprotection-unauthenticated.mjs
source-hash: ca11faa54b1830119465081e5fe7dcee0b745d5f
lines: 140

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## IPProtectionUnauthenticatedContentElement.constructor()
- 位置: L18-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## IPProtectionUnauthenticatedContentElement.isSiteInclusionsFeatureEnabled()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## IPProtectionUnauthenticatedContentElement.handleOptIn()
- 位置: L33-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## IPProtectionUnauthenticatedContentElement.handleTosClick()
- 位置: L39-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`
- 条件付き依存: `if ( event.target.id === "vpn-terms-of-service" || event.target.id === "vpn-privacy-notice" )` → `win.openWebLinkIn()`
- 条件付き依存: `if ( event.target.id === "vpn-terms-of-service" || event.target.id === "vpn-privacy-notice" )` → `this.dispatchEvent()`
- 参照: `event.target.documentGlobal`, `event.target.href`, `event.target.id`

## IPProtectionUnauthenticatedContentElement.handleLearnMoreClick()
- 位置: L53-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("learn-more-vpn"))` → `win.openWebLinkIn()`
- 条件付き依存: `if (event.target.classList.contains("learn-more-vpn"))` → `this.dispatchEvent()`
- 参照: `event.target.documentGlobal`, `event.target.href`

## IPProtectionUnauthenticatedContentElement.render()
- 位置: L64-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `html()`
- 参照: `LINKS.PRIVACY_NOTICE_URL`, `LINKS.SUPPORT_SLUG`, `LINKS.TERMS_OF_SERVICE_URL`, `this.handleLearnMoreClick`, `this.handleOptIn`, `this.handleTosClick`, `this.isSiteInclusionsFeatureEnabled`
- XPCOM: `Services.urlFormatter`
