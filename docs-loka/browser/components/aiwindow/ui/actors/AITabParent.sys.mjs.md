# browser/components/aiwindow/ui/actors/AITabParent.sys.mjs

source: browser/components/aiwindow/ui/actors/AITabParent.sys.mjs
source-hash: 004540ea8ab2e28872785d6eaf99ef5cd71eb7f2
lines: 237

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## formatCreatedAt()
- 位置: L39-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.round()`, `Number.isNaN()`, `created.getTime()`, `created.toDateString()`, `created.valueOf()`, `lazy.fluentStrings.formatValueSync()`, `new Date(now).toDateString()`
- 条件付き依存: `if (created.toDateString() == new Date(now).toDateString())` → `lazy.fluentStrings.formatValueSync()`

## AITabParent.receiveMessage()
- 位置: async L61-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `this.#handleDeletePage()`, `this.#handleGetPage()`, `this.#handleOpenLink()`

## AITabParent.#pageName()
- 位置: L84-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `getSmartPageName()`
- 参照: `this.browsingContext?.currentURI?.spec`

## AITabParent.#handleGetPage()
- 位置: async L93-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITabStore.getBySlug()`, `a2ui.toUI()`, `console.error()`, `formatCreatedAt()`
- 参照: `pageData.createdAt`, `pageData?.components?.surface`, `this.#pageName`

## AITabParent.#handleDeletePage()
- 位置: async L135-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITabStore.getBySlug()`, `Services.tm.dispatchToMainThread()`, `console.error()`, `this.#returnToSmartWindowHome()`
- 条件付き依存: `if (page)` → `AITabStore.deleteBySlug()`
- 条件付き依存: `if (page.toolConvId)` → `ConversationStore.deleteConversationById()`
- 条件付き依存: `if (page.toolConvId)` → `console.error()`
- 参照: `page.slug`, `page.toolConvId`, `this.#pageName`
- XPCOM: `Services.tm`

## AITabParent.#handleOpenLink()
- 位置: L189-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `URL.parse()`, `lazy.URILoadingHelper.openWebLinkIn()`, `lazy.URILoadingHelper.switchToTabHavingURI()`
- 参照: `this.browsingContext?.topChromeWindow`, `uri?.protocol`, `window.gBrowser.selectedBrowser.browsingContext.originAttributes`
- XPCOM: `Services.scriptSecurityManager`

## AITabParent.#returnToSmartWindowHome()
- 位置: L228-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `this.browsingContext?.loadURI()`
- 参照: `lazy.AIWINDOW_URL`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`
