# browser/actors/AboutReaderParent.sys.mjs

source: browser/actors/AboutReaderParent.sys.mjs
source-hash: 4a7bac56a273dbb6efcab7e9763768d63879da11
lines: 261

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutReaderParent.didDestroy()
- 位置: L27-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gAllActors.delete()`, `this.isReaderMode()`
- 条件付き依存: `if (this.isReaderMode())` → `decodeURIComponent()`
- 条件付き依存: `if (this.isReaderMode())` → `url.substr()`
- 条件付き依存: `if (this.isReaderMode())` → `gCachedArticles.delete()`
- 参照: `"about:reader?url=".length`, `this.manager.documentURI.spec`

## AboutReaderParent.isReaderMode()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.manager.documentURI.spec.startsWith()`

## AboutReaderParent.addMessageListener()
- 位置: L41-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gListeners.has()`
- 条件付き依存: `if (!gListeners.has(name))` → `gListeners.set()`
- 条件付き依存: `if (!(!gListeners.has(name)))` → `gListeners.get(name).add()`
- 条件付き依存: `if (!(!gListeners.has(name)))` → `gListeners.get()`

## AboutReaderParent.removeMessageListener()
- 位置: L49-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gListeners.get()`, `gListeners.get(name).delete()`, `gListeners.has()`

## AboutReaderParent.broadcastAsyncMessage()
- 位置: L57-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`

## AboutReaderParent.callListeners()
- 位置: L66-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `gListeners.get()`, `listener.receiveMessage()`, `listeners.values()`
- 参照: `message.name`, `message.target`, `this.browsingContext.embedderElement`

## AboutReaderParent.receiveMessage()
- 位置: async L82-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `console.error()`, `gCachedArticles.delete()`, `gCachedArticles.get()`, `gCachedArticles.set()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`, `this.callListeners()`, `this.enterReaderMode()`, `this.leaveReaderMode()`, `this.updateReaderButton()`
- 参照: `browser.isArticle`, `message.data`, `message.data.article`, `message.data.isArticle`, `message.data.newURL`, `message.data.preferredWidth`, `message.data.url`, `message.name`, `result.uri.spec`, `this.browsingContext.embedderElement`, `uri.spec`
- XPCOM: `Services.io`

## AboutReaderParent.onLocationChange()
- 位置: L149-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutReaderParent.updateReaderButton()`
- 参照: `webProgress.browsingContext.embedderElement`

## AboutReaderParent.updateReaderButton()
- 位置: L157-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.updateReaderButton()`, `windowGlobal.getActor()`
- 参照: `browser.browsingContext.currentWindowGlobal`

## AboutReaderParent.updateReaderButton()
- 位置: L163-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `doc.getElementById()`, `this.isReaderMode()`
- 条件付き依存: `if (this.isReaderMode())` → `gAllActors.add()`
- 条件付き依存: `if (this.isReaderMode())` → `button.setAttribute()`
- 条件付き依存: `if (this.isReaderMode())` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (this.isReaderMode())` → `key.removeAttribute()`
- 条件付き依存: `if (this.isReaderMode())` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(this.isReaderMode()))` → `button.removeAttribute()`
- 条件付き依存: `if (!(this.isReaderMode()))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(this.isReaderMode()))` → `key.toggleAttribute()`
- 条件付き依存: `if (browser.isArticle)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!button.hidden)` → `lazy.PageActions.sendPlacedInUrlbarTrigger()`
- 参照: `browser.documentGlobal.document`, `browser.isArticle`, `button.hidden`, `menuitem.hidden`, `tabBrowser.selectedBrowser`
- XPCOM: `Services.obs`

## AboutReaderParent.forceShowReaderIcon()
- 位置: L206-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutReaderParent.updateReaderButton()`
- 参照: `browser.isArticle`

## AboutReaderParent.toggleReaderMode()
- 位置: L211-225
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win.gBrowser)` → `windowGlobal.getActor()`
- 条件付き依存: `if (actor)` → `actor.isReaderMode()`
- 条件付き依存: `if (actor.isReaderMode())` → `gAllActors.delete()`
- 条件付き依存: `if (actor)` → `actor.sendAsyncMessage()`
- 参照: `browser.browsingContext.currentWindowGlobal`, `event.target.documentGlobal`, `win.gBrowser`, `win.gBrowser.selectedBrowser`

## AboutReaderParent.hasReaderModeEntryAtOffset()
- 位置: L227-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browsingContext.childSessionHistory.canGo()`
- 条件付き依存: `if (browsingContext.childSessionHistory.canGo(offset))` → `shistory.getEntryAtIndex()`
- 参照: `browsingContext.sessionHistory`, `nextEntry.URI.spec`, `shistory.index`, `this.browsingContext`

## AboutReaderParent.enterReaderMode()
- 位置: L238-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encodeURIComponent()`, `this.hasReaderModeEntryAtOffset()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (this.hasReaderModeEntryAtOffset(readerURL, +1))` → `browsingContext.childSessionHistory.go()`
- 参照: `this.browsingContext`

## AboutReaderParent.leaveReaderMode()
- 位置: L249-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ReaderMode.getOriginalUrl()`, `this.hasReaderModeEntryAtOffset()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (this.hasReaderModeEntryAtOffset(originalURL, -1))` → `browsingContext.childSessionHistory.go()`
- 参照: `browsingContext.currentWindowGlobal.documentURI.spec`, `this.browsingContext`
