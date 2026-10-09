# browser/components/genai/content/link-preview-card.mjs

source: browser/components/genai/content/link-preview-card.mjs
source-hash: 0469e94e30ea9cfcba7c21347f16e44012583805
lines: 593

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `customElements.define()`, `window.MozXULElement.insertFTLIfNeeded()`

## LinkPreviewCard.constructor()
- 位置: L63-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createRef()`, `super()`
- 参照: `this.canShowKeyPoints`, `this.collapsed`, `this.firstTimeModalRef`, `this.generationError`, `this.isMissingDataErrorState`, `this.keyPoints`, `this.optin`, `this.optinRef`, `this.progress`

## LinkPreviewCard.handleSettingsClick()
- 位置: L84-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`, `win.openPreferences()`
- 参照: `this.documentGlobal`

## LinkPreviewCard.addKeyPoint()
- 位置: L94-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.keyPoints.push()`, `this.requestUpdate()`

## LinkPreviewCard.handleLink()
- 位置: L104-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `event.preventDefault()`, `event.target.closest()`, `lazy.BrowserUtils.whereToOpenLink()`, `this.dispatchEvent()`, `win.openLinkIn()`
- 参照: `anchor.href`, `event.target.dataset.source`, `this.documentGlobal`
- XPCOM: `Services.scriptSecurityManager`

## LinkPreviewCard.handleRetry()
- 位置: L134-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.dispatchEvent()`

## LinkPreviewCard.toggleKeyPoints()
- 位置: L145-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!this.collapsed)` → `this.dispatchEvent()`
- 参照: `this.collapsed`, `this.progress`
- XPCOM: `Services.prefs`

## LinkPreviewCard.updated()
- 位置: L162-177
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `LinkPreviewCard.AI_ICON`, `this.firstTimeModalRef.value`, `this.firstTimeModalRef.value.footerMessageL10nId`, `this.firstTimeModalRef.value.headingIcon`, `this.firstTimeModalRef.value.iconAtEnd`, `this.firstTimeModalRef.value.isLoading`, `this.firstTimeModalRef.value.progressStatus`, `this.optinRef.value`, `this.optinRef.value.headingIcon`, `this.progress`

## LinkPreviewCard.errorMessageL10nId()
- 位置: L184-191
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.generationError`, `this.isMissingDataErrorState`

## LinkPreviewCard.renderErrorGenerationCard()
- 位置: L198-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.errorMessageL10nId`, `this.generationError`, `this.generationError.name`, `this.handleRetry`

## LinkPreviewCard.renderOptInPlaceholderCard()
- 位置: L233-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `Array(LinkPreviewCard.PLACEHOLDER_COUNT) .fill()`, `Array(LinkPreviewCard.PLACEHOLDER_COUNT) .fill() .map()`, `html()`, `this.renderModelOptIn()`
- 参照: `LinkPreviewCard.PLACEHOLDER_COUNT`, `this._handleOptinDeny`, `this.collapsed`

## LinkPreviewCard.renderNormalGenerationCard()
- 位置: L280-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `Array( Math.max( 0, LinkPreviewCard.PLACEHOLDER_COUNT - this.keyPoints.length ) ) .fill()`, `Array( Math.max( 0, LinkPreviewCard.PLACEHOLDER_COUNT - this.keyPoints.length ) ) .fill() .map()`, `Math.max()`, `html()`, `this.keyPoints.map()`, `this.renderModalFirstTime()`
- 参照: `LinkPreviewCard.PLACEHOLDER_COUNT`, `this.collapsed`, `this.generating`, `this.handleLink`, `this.keyPoints.length`, `this.progress`, `this.toggleKeyPoints`

## LinkPreviewCard.renderModelOptIn()
- 位置: L369-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ref()`
- 参照: `LinkPreviewCard.AI_ICON`, `this._handleOptinConfirm`, `this._handleOptinDeny`, `this.optinRef`

## LinkPreviewCard.renderModalFirstTime()
- 位置: L390-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ref()`
- 参照: `this._handleCancelDownload`, `this.firstTimeModalRef`, `this.progress`

## LinkPreviewCard._handleOptinConfirm()
- 位置: L412-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.dispatchEvent()`
- XPCOM: `Services.prefs`

## LinkPreviewCard._handleCancelDownload()
- 位置: L421-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## LinkPreviewCard._handleOptinDeny()
- 位置: L430-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.cardAiConsent.record()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## LinkPreviewCard.renderKeyPointsSection()
- 位置: L443-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderNormalGenerationCard()`
- 条件付き依存: `if (!this.optin && !this.collapsed)` → `this.renderOptInPlaceholderCard()`
- 条件付き依存: `if (isGenerationError)` → `this.renderErrorGenerationCard()`
- 参照: `this.canShowKeyPoints`, `this.collapsed`, `this.generationError`, `this.isMissingDataErrorState`, `this.optin`

## LinkPreviewCard.render()
- 位置: L470-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`, `imageUrl.startsWith()`, `lazy.FaviconUtils.getMozRemoteImageURL()`, `lazy.numberFormat.format()`, `lazy.numberFormat.formatRange()`, `lazy.pluralRules.select()`, `lazy.pluralRules.selectRange()`, `this.renderKeyPointsSection()`, `window.matchMedia()`
- 参照: `articleData.readingTimeMinsFast`, `articleData.readingTimeMinsSlow`, `articleData.siteName`, `articleData.textContent`, `this.handleLink`, `this.handleSettingsClick`, `this.pageData.meta`, `this.pageData?.article`, `this.pageData?.url`, `this.pageData?.urlComponents?.domain`, `this.pageData?.urlComponents?.filename`, `window.matchMedia( "(prefers-color-scheme: dark)" ).matches`
