# browser/components/urlbar/UrlbarValueFormatter.sys.mjs

source: browser/components/urlbar/UrlbarValueFormatter.sys.mjs
source-hash: 7ac2e345ea619d60c90bdde4c274786c9ade8e89
lines: 709

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## UrlbarValueFormatter.constructor()
- 位置: L24-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.addEventListener()`
- 参照: `this.#urlbarInput`

## UrlbarValueFormatter.update()
- 位置: async L30-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#formatSearchAlias()`, `this.#formatURL()`, `this.#removeSearchAliasFormat()`, `this.#removeURLFormat()`, `this.#urlbarInput.removeAttribute()`, `this.#window.requestAnimationFrame()`
- 条件付き依存: `if (!lazy.SearchService.isInitialized)` → `lazy.SearchService.init()`
- 参照: `lazy.SearchService.isInitialized`, `this.#formattingApplied`, `this.#scheme.value`, `this.#updateInstance`, `this.#urlbarInput.value`, `this.#window.delayedStartupPromise`, `this.#window.docShell`, `this.#window.gBrowserInit.delayedStartupFinished`

## UrlbarValueFormatter.#document()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#urlbarInput.document`

## UrlbarValueFormatter.#inputField()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#urlbarInput.inputField`

## UrlbarValueFormatter.#window()
- 位置: L99-101
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#urlbarInput.window`

## UrlbarValueFormatter.#scheme()
- 位置: L103-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#urlbarInput.querySelector()`

## UrlbarValueFormatter.#scrollHostIntoView()
- 位置: L109-126
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#hostRange)` → `this.#hostRange.getBoundingClientRect()`
- 条件付き依存: `if (this.#hostRange)` → `this.#inputField.getBoundingClientRect()`
- 条件付き依存: `if (this.#hostRange)` → `Math.min()`
- 条件付き依存: `if (this.#hostRange)` → `Math.max()`
- 参照: `hostRect.left`, `hostRect.right`, `this.#hostRange`, `this.#inputField.scrollLeft`, `this.#inputField.scrollLeftMax`, `urlbarRect.left`, `urlbarRect.right`

## UrlbarValueFormatter.#ensureFormattedHostVisible()
- 位置: L128-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getUrlMetaData()`, `this.#urlbarInput.updateTextOverflow()`, `this.#window.windowUtils.getDirectionFromText()`
- 条件付き依存: `if (!urlMetaData)` → `this.#urlbarInput.removeAttribute()`
- 条件付き依存: `if ( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" )` → `this.#urlbarInput.setAttribute()`
- 条件付き依存: `if ( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" )` → `this.#scrollHostIntoView()`
- 条件付き依存: `if (!( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" ))` → `this.#urlbarInput.setAttribute()`
- 条件付き依存: `if (!( directionality == this.#window.windowUtils.DIRECTION_RTL && url[preDomain.length + domain.length] != "\u200E" ))` → `this.#scrollHostIntoView()`
- 参照: `domain.length`, `preDomain.length`, `this.#window.windowUtils.DIRECTION_RTL`

## UrlbarValueFormatter.#getUrlMetaData()
- 位置: L156-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `inputValue.startsWith()`, `this.#urlbarInput.getBrowserState()`, `untrimmedValue.startsWith()`, `url.match()`
- 条件付き依存: `if ( untrimmedValue.startsWith("http://") || untrimmedValue.startsWith("https://") )` → `Services.io.newURI()`
- 条件付き依存: `if (!uri)` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!uri)` → `Services.uriFixup.getFixupURIInfo()`
- 条件付き依存: `if (!uri)` → `["http", "https"].includes()`
- 条件付き依存: `if (replaceUrl)` → `this.#urlbarInput.setURI()`
- 条件付き依存: `if (replaceUrl)` → `this.#getUrlMetaData()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeSchemeless`, `Services.io.newURI("http://" + domain).displayHost`, `Services.uriFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Services.uriFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Services.uriFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `browserState.urlMetaData`, `browserState.urlMetaData.data`, `browserState.urlMetaData.inputValue`, `browserState.urlMetaData.untrimmedValue`, `lazy.BrowserUIUtils.trimURLProtocol`, `scheme.length`, `this.#inGetUrlMetaData`, `this.#urlbarInput.focused`, `this.#urlbarInput.untrimmedValue`, `this.#urlbarInput.value`, `this.#window`, `this.#window.gBrowser.selectedBrowser`, `this.#window.gBrowser.userTypedValue`, `trimmedProtocol.length`, `uri.displayHost`, `uri.host`, `uri.scheme`, `uriInfo.fixedURI`, `uriInfo.fixedURI.scheme`, `uriInfo.keywordProviderId`, `uriInfo?.schemelessInput`
- XPCOM: [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / `Services.io` / `Services.uriFixup`

## UrlbarValueFormatter.#removeURLFormat()
- 位置: L296-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.getSelection()`, `selection.removeAllRanges()`, `strikeOut.removeAllRanges()`, `this.#formatScheme()`, `this.#inputField.style.setProperty()`
- 参照: `controller.SELECTION_URLSECONDARY`, `controller.SELECTION_URLSTRIKEOUT`, `this.#formattingApplied`, `this.#hostRange`, `this.#urlbarInput.editor.selectionController`

## UrlbarValueFormatter.formattingEnabled()
- 位置: L316-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`

## UrlbarValueFormatter.willShowFormattedMixedContentProtocol()
- 位置: L329-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `val.startsWith()`
- 参照: `this.#showingMixedContentLoadedPageUrl`, `this.#urlbarInput.value`, `this.formattingEnabled`

## UrlbarValueFormatter.#showingMixedContentLoadedPageUrl()
- 位置: L387-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#urlbarInput.getAttribute()`
- 参照: `Ci.nsIWebProgressListener.STATE_LOADED_MIXED_ACTIVE_CONTENT`, `this.#window.gBrowser.securityUI.state`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## UrlbarValueFormatter.#formatURL()
- 位置: L406-517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `controller.getSelection()`, `domain.endsWith()`, `lazy.UrlbarPrefs.get()`, `this.#ensureFormattedHostVisible()`, `this.#formatScheme()`, `this.#getUrlMetaData()`, `this.#urlbarInput.getBrowserState()`, `this.#urlbarInput.value.startsWith()`, `this.willShowFormattedMixedContentProtocol()`
- 条件付き依存: `if ( !lazy.UrlbarPrefs.get("security.insecure_connection_text.enabled") && !isUnformattedMixedContent && this.#urlbarInput.value.startsWith(schemeWSlashes) )` → `this.#inputField.style.setProperty()`
- 条件付き依存: `if (hostStart < hostEnd)` → `this.#document.createRange()`
- 条件付き依存: `if (hostStart < hostEnd)` → `this.#hostRange.setStart()`
- 条件付き依存: `if (hostStart < hostEnd)` → `this.#hostRange.setEnd()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `this.#document.createRange()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `range.setStart()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `range.setEnd()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `controller.getSelection()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `strikeOut.addRange()`
- 条件付き依存: `if (this.willShowFormattedMixedContentProtocol(this.#urlbarInput.value))` → `this.#formatScheme()`
- 条件付き依存: `if (!domain.endsWith(baseDomain))` → `Cc["@mozilla.org/network/idn-service;1"].getService()`
- 条件付き依存: `if (!domain.endsWith(baseDomain))` → `IDNService.domainToDisplay()`
- 条件付き依存: `if (baseDomain != domain)` → `domain.slice()`
- 条件付き依存: `if (rangeLength)` → `this.#document.createRange()`
- 条件付き依存: `if (rangeLength)` → `range.setStart()`
- 条件付き依存: `if (rangeLength)` → `range.setEnd()`
- 条件付き依存: `if (rangeLength)` → `selection.addRange()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `this.#document.createRange()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `range.setStart()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `range.setEnd()`
- 条件付き依存: `if (startRest < url.length - trimmedLength)` → `selection.addRange()`
- 参照: `Ci.nsIIDNService`, `baseDomain.length`, `controller.SELECTION_URLSECONDARY`, `controller.SELECTION_URLSTRIKEOUT`, `domain.length`, `editor.rootElement.firstChild`, `editor.selectionController`, `preDomain.length`, `schemeWSlashes.length`, `state.searchTerms`, `subDomain.length`, `this.#hostRange`, `this.#scheme.value`, `this.#showingMixedContentLoadedPageUrl`, `this.#urlbarInput.editor`, `this.#urlbarInput.value`, `this.#window.gBrowser.selectedBrowser`, `this.formattingEnabled`, `url.length`
- XPCOM: [`nsIIDNService`](../../../netwerk/dns/nsIIDNService.idl.md) / `@mozilla.org/network/idn-service;1` / `Services.eTLD`

## UrlbarValueFormatter.#formatScheme()
- 位置: L519-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.getSelection()`
- 条件付き依存: `if (clear)` → `selection.removeAllRanges()`
- 条件付き依存: `if (!(clear))` → `this.#document.createRange()`
- 条件付き依存: `if (!(clear))` → `r.setStart()`
- 条件付き依存: `if (!(clear))` → `r.setEnd()`
- 条件付き依存: `if (!(clear))` → `selection.addRange()`
- 参照: `editor.rootElement.firstChild`, `editor.selectionController`, `textNode.textContent.length`, `this.#scheme.editor`

## UrlbarValueFormatter.#removeSearchAliasFormat()
- 位置: L534-542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selection.removeAllRanges()`, `this.#urlbarInput.editor.selectionController.getSelection()`
- 参照: `Ci.nsISelectionController.SELECTION_FIND`, `this.#formattingApplied`
- XPCOM: [`nsISelectionController`](../../../dom/base/nsISelectionController.idl.md)

## UrlbarValueFormatter.#formatSearchAlias()
- 位置: L550-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editor.selectionController.getSelection()`, `range.setEnd()`, `range.setStart()`, `selection.addRange()`, `this.#document.createRange()`, `this.#document.documentElement.hasAttribute()`, `this.#findEngineAliasOrRestrictKeyword()`, `this.#window.matchMedia()`, `trimmedValue.startsWith()`, `value.indexOf()`, `value.trim()`
- 条件付き依存: `if ( this.#document.documentElement.hasAttribute("lwtheme") || this.#window.matchMedia("(prefers-contrast)").matches )` → `selection.setColors()`
- 条件付き依存: `if (!( this.#document.documentElement.hasAttribute("lwtheme") || this.#window.matchMedia("(prefers-contrast)").matches ))` → `selection.setColors()`
- 参照: `Ci.nsISelectionController.SELECTION_FIND`, `alias.length`, `editor.rootElement.firstChild`, `textNode.textContent`, `this.#urlbarInput.editor`, `this.#urlbarInput.view.oneOffSearchButtons.selectedButton`, `this.#window.matchMedia("(prefers-contrast)").matches`, `this.formattingEnabled`
- XPCOM: [`nsISelectionController`](../../../dom/base/nsISelectionController.idl.md)

## UrlbarValueFormatter.#findEngineAliasOrRestrictKeyword()
- 位置: L634-662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#urlbarInput.view.getResultAtIndex()`
- 参照: `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `payload.autofillKeyword`, `payload.keyword`, `this.#selectedResult`, `this.#urlbarInput.view.selectedResult`

## UrlbarValueFormatter.handleEvent()
- 位置: L670-677
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## UrlbarValueFormatter._on_resize()
- 位置: L679-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.requestAnimationFrame()`, `this.#window.setTimeout()`
- 条件付き依存: `if (this.#resizeThrottleTimeout)` → `this.#window.clearTimeout()`
- 条件付き依存: `if ( this.#hostRange && !this.#hostRange.commonAncestorContainer.isConnected )` → `this.#removeURLFormat()`
- 条件付き依存: `if ( this.#hostRange && !this.#hostRange.commonAncestorContainer.isConnected )` → `this.#formatURL()`
- 条件付き依存: `if (!( this.#hostRange && !this.#hostRange.commonAncestorContainer.isConnected ))` → `this.#ensureFormattedHostVisible()`
- 参照: `event.target`, `this.#hostRange`, `this.#hostRange.commonAncestorContainer.isConnected`, `this.#resizeInstance`, `this.#resizeThrottleTimeout`, `this.#window`
