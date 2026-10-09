# browser/components/ipprotection/content/ipprotection-content.mjs

source: browser/components/ipprotection/content/ipprotection-content.mjs
source-hash: eada3ca7cab019b8651ae963f9cec4c1d2dfa69c
lines: 621

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## IPProtectionContentElement.constructor()
- 位置: L57-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.#messageBarListener.bind()`, `this.#statusCardListener.bind()`
- 参照: `this._messageDismissed`, `this._showMessageBar`, `this.messageBarListener`, `this.state`, `this.statusCardListener`

## IPProtectionContentElement.connectedCallback()
- 位置: L68-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.addEventListener()`, `this.dispatchEvent()`
- 参照: `this.#messageBarListener`, `this.#statusCardListener`

## IPProtectionContentElement.disconnectedCallback()
- 位置: L85-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.removeEventListener()`
- 参照: `this.#messageBarListener`, `this.#statusCardListener`

## IPProtectionContentElement.canEnableConnection()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.state`, `this.state.error`, `this.state.isProtectionEnabled`

## IPProtectionContentElement.hasSiteExclusion()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.state?.siteData?.isExclusion`

## IPProtectionContentElement.hasSiteInclusion()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.state?.siteData?.isInclusion`

## IPProtectionContentElement.hasSiteRule()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.state?.siteData?.hasSiteRule`

## IPProtectionContentElement.#hasErrors()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.state`, `this.state.error`

## IPProtectionContentElement.handleClickSupportLink()
- 位置: L122-132
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target === this.supportLinkEl)` → `event.preventDefault()`
- 条件付き依存: `if (event.target === this.supportLinkEl)` → `win.openWebLinkIn()`
- 条件付き依存: `if (event.target === this.supportLinkEl)` → `this.dispatchEvent()`
- 参照: `LINKS.PRODUCT_URL`, `event.target`, `event.target.documentGlobal`, `this.supportLinkEl`

## IPProtectionContentElement.handleUpgrade()
- 位置: L134-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.ipprotection.clickUpgradeButton.record()`, `this.dispatchEvent()`, `win.openWebLinkIn()`
- 参照: `LINKS.PRODUCT_URL`, `event.target.documentGlobal`

## IPProtectionContentElement.focus()
- 位置: L145-151
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.state.unauthenticated)` → `this.unauthenticatedEl?.focus()`
- 条件付き依存: `if (!(this.state.unauthenticated))` → `this.statusCardEl?.focus()`
- 参照: `this.state.unauthenticated`

## IPProtectionContentElement.#statusCardListener()
- 位置: L153-163
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "ipprotection-status-card:user-toggled-on")` → `this.dispatchEvent()`
- 条件付き依存: `if (event.type === "ipprotection-status-card:user-toggled-off")` → `this.dispatchEvent()`
- 参照: `event.type`

## IPProtectionContentElement.#messageBarListener()
- 位置: L165-185
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.state.bandwidthWarning)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this.state.bandwidthWarning)` → `this.dispatchEvent()`
- 参照: `event.type`, `this._messageDismissed`, `this._showMessageBar`, `this.state.bandwidthWarning`, `this.state.error`
- XPCOM: `Services.prefs`

## IPProtectionContentElement.handleToggleUseVPN()
- 位置: L187-204
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isEnabled)` → `this.dispatchEvent()`
- 条件付き依存: `if (!(isEnabled))` → `this.dispatchEvent()`
- 参照: `event.target.pressed`

## IPProtectionContentElement.handleClickSiteRulesLink()
- 位置: L206-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.dispatchEvent()`, `win.openPreferences()`
- 参照: `event.target.documentGlobal`

## IPProtectionContentElement.handleClickSettingsButton()
- 位置: L215-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.dispatchEvent()`, `win.openPreferences()`
- 参照: `event.target.documentGlobal`

## IPProtectionContentElement.updated()
- 位置: L224-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.updated()`
- 参照: `this.#prevBandwidthWarning`, `this._messageDismissed`, `this.state.bandwidthWarning`, `this.state.error`

## IPProtectionContentElement.messageBarTemplate()
- 位置: L243-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 条件付き依存: `if (this.state.bandwidthWarning && this.state.bandwidthUsage)` → `formatRemainingBandwidth()`
- 条件付き依存: `if (this.state.bandwidthWarning && this.state.bandwidthUsage)` → `JSON.stringify()`
- 参照: `BANDWIDTH.BYTES_IN_GB`, `this.state.bandwidthUsage`, `this.state.bandwidthUsage.max`, `this.state.bandwidthUsage.remaining`, `this.state.bandwidthWarning`, `this.state.onboardingMessage`

## IPProtectionContentElement.statusCardTemplate()
- 位置: L296-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `this.canEnableConnection`, `this.hasSiteExclusion`, `this.state.bandwidthUsage`, `this.state.hasUpgraded`, `this.state.isActivating`, `this.state.isPremium`, `this.state.location`, `this.state.showLocationButtonBadge`

## IPProtectionContentElement.upgradeTemplate()
- 位置: L313-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleUpgrade`, `this.state.hasUpgraded`, `this.state.upgradeNotAvailable`

## IPProtectionContentElement.errorTemplate()
- 位置: L345-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 参照: `ERRORS.CATASTROPHIC`, `ERRORS.GENERIC`, `ERRORS.NETWORK`, `ERRORS.VPN_UNAVAILABLE`, `LINKS.NO_ACCESS_SUPPORT_SLUG`, `this.state.error`

## IPProtectionContentElement.pausedTemplate()
- 位置: L400-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `this.upgradeTemplate()`
- 参照: `BANDWIDTH.BYTES_IN_GB`, `this.state.bandwidthUsage.max`

## IPProtectionContentElement.siteRulesStatusTemplate()
- 位置: L421-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#hasErrors`, `this.hasSiteExclusion`, `this.hasSiteInclusion`, `this.hasSiteRule`, `this.state.isProtectionEnabled`, `this.state.isSiteInclusionsEnabled`, `this.state.siteData`

## IPProtectionContentElement.siteRulesSettingsLinkTemplate()
- 位置: L469-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#hasErrors`, `this.handleClickSiteRulesLink`, `this.state.isSiteInclusionsEnabled`, `this.state.siteData`

## IPProtectionContentElement.exclusionToggleTemplate()
- 位置: L488-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#hasErrors`, `this.handleToggleUseVPN`, `this.hasSiteExclusion`, `this.state.isProtectionEnabled`, `this.state.isSiteExceptionsEnabled`, `this.state.isSiteInclusionsEnabled`, `this.state.siteData`

## IPProtectionContentElement.footerTemplate()
- 位置: L523-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleClickSettingsButton`

## IPProtectionContentElement.enrollingTemplate()
- 位置: L537-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## IPProtectionContentElement.mainContentTemplate()
- 位置: L553-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.exclusionToggleTemplate()`, `this.footerTemplate()`, `this.statusCardTemplate()`
- 条件付き依存: `if (this.state.isEnrolling)` → `html()`
- 条件付き依存: `if (this.state.isEnrolling)` → `this.enrollingTemplate()`
- 条件付き依存: `if (this.state.isEnrolling)` → `this.footerTemplate()`
- 条件付き依存: `if (this.state.unauthenticated)` → `html()`
- 条件付き依存: `if (this.#hasErrors)` → `html()`
- 条件付き依存: `if (this.#hasErrors)` → `this.errorTemplate()`
- 条件付き依存: `if (this.#hasErrors)` → `this.footerTemplate()`
- 条件付き依存: `if (this.state.paused)` → `html()`
- 条件付き依存: `if (this.state.paused)` → `this.pausedTemplate()`
- 条件付き依存: `if (this.state.paused)` → `this.footerTemplate()`
- 条件付き依存: `if (this.state.isSiteInclusionsEnabled)` → `html()`
- 条件付き依存: `if (this.state.isSiteInclusionsEnabled)` → `this.statusCardTemplate()`
- 条件付き依存: `if (this.state.isSiteInclusionsEnabled)` → `this.siteRulesStatusTemplate()`
- 条件付き依存: `if (this.state.isSiteInclusionsEnabled)` → `this.siteRulesSettingsLinkTemplate()`
- 条件付き依存: `if (this.state.isSiteInclusionsEnabled)` → `this.footerTemplate()`
- 参照: `this.#hasErrors`, `this.state.isEnrolling`, `this.state.isSiteInclusionsEnabled`, `this.state.paused`, `this.state.unauthenticated`

## IPProtectionContentElement.render()
- 位置: L588-617
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.mainContentTemplate()`, `this.messageBarTemplate()`
- 参照: `this._messageDismissed`, `this._showMessageBar`, `this.state.bandwidthWarning`, `this.state.onboardingMessage`, `this.state.paused`, `this.state.unauthenticated`
