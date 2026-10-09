# browser/components/sharing/content/content-sharing-modal.mjs

source: browser/components/sharing/content/content-sharing-modal.mjs
source-hash: f39acda58f681125b82a12969a5e95a7ecd0b028
lines: 380

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `customElements.define()`

## ContentSharingModal.getUpdateComplete()
- 位置: async L73-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.getUpdateComplete()`
- 参照: `this.previewCard?.updateComplete`

## ContentSharingModal.connectedCallback()
- 位置: async L78-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`
- 参照: `(await loadingPromise).shareResult`, `this.loading`, `this.shareResult`, `this.size`, `window.arguments`

## ContentSharingModal.close()
- 位置: L96-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.close()`, `window.top.document.documentElement.removeAttribute()`

## ContentSharingModal.linkTemplate()
- 位置: L104-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (link.type === "bookmarks")` → `html()`
- 参照: `link.title`, `link.type`, `link.url`

## ContentSharingModal.linksInfoTemplate()
- 位置: L118-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 条件付き依存: `if (this.shareResult.warning === WARNINGS.TOO_MANY_LINKS)` → `html()`
- 条件付き依存: `if (this.shareResult.warning === WARNINGS.TOO_MANY_LINKS)` → `JSON.stringify()`
- 参照: `WARNINGS.TOO_MANY_LINKS`, `this.shareResult.share.links.length`, `this.shareResult.warning`

## ContentSharingModal.linksTemplate()
- 位置: L140-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.linkTemplate()`, `this.shareResult.share.links.map()`
- 条件付き依存: `if (this.shareResult.share.links.length > MAX_PREVIEW_LINKS)` → `html()`
- 条件付き依存: `if (this.shareResult.share.links.length > MAX_PREVIEW_LINKS)` → `this.shareResult.share.links .slice(0, 3) .map()`
- 条件付き依存: `if (this.shareResult.share.links.length > MAX_PREVIEW_LINKS)` → `this.shareResult.share.links .slice()`
- 条件付き依存: `if (this.shareResult.share.links.length > MAX_PREVIEW_LINKS)` → `this.linkTemplate()`
- 条件付き依存: `if (this.shareResult.share.links.length > MAX_PREVIEW_LINKS)` → `this.linksInfoTemplate()`
- 参照: `this.shareResult.share.links.length`, `this.shareResult.share?.links`

## ContentSharingModal.handleViewPageClick()
- 位置: L155-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.collectionShare.ctaClicked.record()`, `this.close()`, `this.documentGlobal.frameElement.documentGlobal.openWebLinkIn()`
- 参照: `this.shareResult.url`

## ContentSharingModal.handleCopyClick()
- 位置: L167-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.collectionShare.ctaClicked.record()`, `new Promise(r => setTimeout(r, 1000)).then()`, `setTimeout()`, `this.copyButton.setAttribute()`, `window.navigator.clipboard.writeText()`
- 参照: `this.shareResult.url`

## ContentSharingModal.handleSignInClick()
- 位置: L183-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.collectionShare.ctaClicked.record()`, `this.close()`, `this.documentGlobal.frameElement.documentGlobal.openWebLinkIn()`
- 参照: `lazy.CONTENT_SHARING_DEBUG`, `lazy.CONTENT_SHARING_SERVER_URL`

## ContentSharingModal.acceptableUseClick()
- 位置: L199-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HTMLAnchorElement.isInstance()`, `event.preventDefault()`, `this.close()`, `this.documentGlobal.frameElement.documentGlobal.openWebLinkIn()`
- 参照: `event.target`, `event.target.href`

## ContentSharingModal.loadingTemplate()
- 位置: L212-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## ContentSharingModal.descriptionActionTemplate()
- 位置: L224-261
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.loading)` → `this.loadingTemplate()`
- 条件付き依存: `if ( this.shareResult.url || !this.shareResult.error || (!this.shareResult.isSignedIn && this.shareResult.error === ERRORS.UNAUTHORIZED) )` → `html()`
- 条件付き依存: `if ( this.shareResult.url || !this.shareResult.error || (!this.shareResult.isSignedIn && this.shareResult.error === ERRORS.UNAUTHORIZED) )` → `this.buttonsTemplate()`
- 条件付き依存: `if (this.shareResult.error === ERRORS.INVALID_SCHEMA)` → `html()`
- 条件付き依存: `if (this.shareResult.error)` → `html()`
- 参照: `ERRORS.INVALID_SCHEMA`, `ERRORS.UNAUTHORIZED`, `this.loading`, `this.shareResult.error`, `this.shareResult.isSignedIn`, `this.shareResult.url`

## ContentSharingModal.buttonsTemplate()
- 位置: L263-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (this.shareResult.isSignedIn)` → `html()`
- 参照: `this.handleCopyClick`, `this.handleSignInClick`, `this.handleViewPageClick`, `this.shareResult.isSignedIn`

## ContentSharingModal.policyTemplate()
- 位置: L290-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.acceptableUseClick`, `this.shareResult.isSignedIn`

## ContentSharingModal.previewTitleTemplate()
- 位置: L306-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (this.shareResult.share.type === "tabs")` → `html()`
- 参照: `this.shareResult.share.links.length`, `this.shareResult.share.title`, `this.shareResult.share.type`

## ContentSharingModal.render()
- 位置: L327-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.descriptionActionTemplate()`, `this.linksTemplate()`, `this.policyTemplate()`, `this.previewTitleTemplate()`
- 参照: `this.close`, `this.shareResult.isSignedIn`, `this.shareResult.share`
