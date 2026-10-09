# browser/components/aiwindow/ui/actors/AIChatContentParent.sys.mjs

source: browser/components/aiwindow/ui/actors/AIChatContentParent.sys.mjs
source-hash: ef9b2cdc672976bdb291adb028da2a0c1ee6df5b
lines: 371

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AIChatContentParent.isTrustedInternalURI()
- 位置: L45-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `isSettingsURL()`, `isSmartPageURL()`, `isTasksURL()`
- 参照: `uri.spec`

## AIChatContentParent.dispatchMessageToChatContent()
- 位置: L51-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.sendAsyncMessage()`
- 参照: `message.pageUrl`

## AIChatContentParent.dispatchTruncateToChatContent()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.dispatchRemoveAppliedMemoryToChatContent()
- 位置: L67-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.dispatchSeenUrlsToChatContent()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.setGeneratingOnChatContent()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## AIChatContentParent.receiveMessage()
- 位置: L87-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `lazy.AIWindowTelemetry.recordHistoryGridEvent()`, `this.#getAIWindowElement()`, `this.#handleAccountSignIn()`, `this.#handleClientError()`, `this.#handleFollowUpFromChild()`, `this.#handleFooterActionFromChild()`, `this.#handleNewChat()`, `this.#handleOpenLink()`, `this.#handleRequestAssets()`, `this.#handleToolUIUpdate()`, `this.#notifyContentReady()`

## AIChatContentParent.#notifyContentReady()
- 位置: L141-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow?.onContentReady()`, `this.#getAIWindowElement()`
- 条件付き依存: `if (aiWindow?.mode)` → `this.sendAsyncMessage()`
- 参照: `aiWindow.mode`, `aiWindow?.mode`

## AIChatContentParent.#handleFooterActionFromChild()
- 位置: L152-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow.handleFooterAction()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#handleOpenLink()
- 位置: L161-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createNullPrincipal()`, `aiWindow?.onOpenLink()`, `console.warn()`, `lazy.BrowserUtils.whereToOpenLink()`, `lazy.SmartWindowTelemetry.recordUriLoad()`, `lazy.URILoadingHelper.openWebLinkIn()`, `this.#getAIWindowElement()`, `this.isTrustedInternalURI()`
- 条件付き依存: `if (url === currentPageURL)` → `lazy.AIWindowUI.handleSameLinkClick()`
- 条件付き依存: `if (this.isTrustedInternalURI(uri))` → `lazy.URILoadingHelper.switchToTabHavingURI()`
- 条件付き依存: `if (preferSwitchToTab)` → `lazy.URILoadingHelper.switchToTabHavingURI()`
- 条件付き依存: `if (preferSwitchToTab)` → `lazy.URILoadingHelper.openWebLinkIn()`
- 条件付き依存: `if (where === "current")` → `lazy.URILoadingHelper.switchToTabHavingURI()`
- 参照: `this.browsingContext.topChromeWindow`, `uri.scheme`, `window.gBrowser.selectedBrowser.browsingContext.originAttributes`, `window.gBrowser.selectedBrowser.currentURI.spec`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## AIChatContentParent.#handleAccountSignIn()
- 位置: async L246-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.launchSignInFlow()`
- 条件付き依存: `if (success)` → `this.#handleRetryAfterError()`
- 参照: `this.browsingContext.topChromeWindow.gBrowser`

## AIChatContentParent.#handleRetryAfterError()
- 位置: L254-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow.handleFooterAction()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#handleNewChat()
- 位置: L263-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow.onCreateNewChatClick()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#getAIWindowElement()
- 位置: L272-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser?.getRootNode()`, `browser?.ownerDocument?.querySelector()`
- 参照: `root.host`, `root?.host?.localName`, `this.browsingContext.embedderElement`

## AIChatContentParent.#handleFollowUpFromChild()
- 位置: L281-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow.onQuickPromptClicked()`, `console.warn()`, `this.#getAIWindowElement()`
- 参照: `data.text`

## AIChatContentParent.#handleToolUIUpdate()
- 位置: L290-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow.handleToolUIUpdate()`, `console.warn()`, `this.#getAIWindowElement()`

## AIChatContentParent.#handleRequestAssets()
- 位置: async L313-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `console.warn()`, `items.map()`, `lazy.captureThumbnail()`, `this.#getAIWindowElement()`, `this.#pageHasFavicon()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (aiWindowElement)` → `aiWindowElement.applyHistoryAssets()`

## AIChatContentParent.#pageHasFavicon()
- 位置: async L348-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`
- XPCOM: `Services.io`

## AIChatContentParent.#handleClientError()
- 位置: L359-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow?.getClientErrorContext()`, `console.warn()`, `lazy.SmartWindowTelemetry.recordClientErrorDetail()`, `this.#getAIWindowElement()`
