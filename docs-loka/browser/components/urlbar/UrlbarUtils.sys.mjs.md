# browser/components/urlbar/UrlbarUtils.sys.mjs

source: browser/components/urlbar/UrlbarUtils.sys.mjs
source-hash: 8757427707dcf6cf26d83d1b52055ddf3e0cea2b
lines: 2563

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Promise.resolve()`, `Services.strings.createBundle()`, `XPCOMUtils.declareLazy()`

## parseOriginParts()
- 位置: L73-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `parsed.host`, `parsed.protocol`

## getPayloadSchema()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.RESULT_PAYLOAD_SCHEMA`

## addToUrlbarHistory()
- 位置: L99-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/[\x00-\x1F]/.test()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `url.includes()`
- 条件付き依存: `if ( !lazy.PrivateBrowsingUtils.isWindowPrivate(window) && url && !url.includes(" ") && // eslint-disable-next-line no-control-regex !/[\x00-\x1F]/.test(url) )` → `lazy.PlacesUIUtils.markPageAsTyped()`

## getShortcutOrURIAndPostData()
- 位置: async L122-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.KeywordUtils.parseUrlAndPostData()`, `lazy.PlacesUtils.keywords.fetch()`, `lazy.SearchService.getEngineByAlias()`, `url.trim()`, `url.trim().split()`
- 条件付き依存: `if (engine)` → `engine.getSubmission()`
- 条件付き依存: `if (postData)` → `this.getPostDataStream()`
- 参照: `entry.postData`, `entry.url`, `entry.url.href`, `submission.postData`, `submission.uri.spec`

## getPostDataStream()
- 位置: L183-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/network/mime-input-stream;1" ].createInstance()`, `Cc["@mozilla.org/io/string-input-stream;1"].createInstance()`, `dataStream.setByteStringData()`, `mimeStream.QueryInterface()`, `mimeStream.addHeader()`, `mimeStream.setData()`
- 参照: `Ci.nsIInputStream`, `Ci.nsIMIMEInputStream`, `Ci.nsIStringInputStream`
- XPCOM: [`nsIInputStream`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIMIMEInputStream`](../../../netwerk/base/nsIMIMEInputStream.idl.md) / [`nsIStringInputStream`](../../../xpcom/io/nsIStringStream.idl.md) / `@mozilla.org/io/string-input-stream;1` / `@mozilla.org/network/mime-input-stream;1`

## getPostDataString()
- 位置: L210-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `postData .QueryInterface()`, `postData .QueryInterface(Ci.nsIMIMEInputStream) .data.QueryInterface()`
- 参照: `Ci.nsIMIMEInputStream`, `Ci.nsISupportsCString`, `postData .QueryInterface(Ci.nsIMIMEInputStream) .data.QueryInterface(Ci.nsISupportsCString).data`
- XPCOM: [`nsIMIMEInputStream`](../../../netwerk/base/nsIMIMEInputStream.idl.md) / [`nsISupportsCString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md)

## getUrlFromResult()
- 位置: L231-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getLoadRequestFromResult()`, `this.loadRequestToUrl()`

## loadRequestToUrl()
- 位置: L250-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPostDataStream()`
- 条件付き依存: `if (loadRequest.engineSearch)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (loadRequest.engineSearch)` → `this.getSearchQueryUrl()`
- 参照: `loadRequest.engineSearch`, `loadRequest.urlLoad.postData`, `loadRequest.urlLoad.url`

## getSearchQueryUrl()
- 位置: L280-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.getSubmission()`
- 参照: `submission.postData`, `submission.uri.spec`

## getPrefixRank()
- 位置: L293-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http://www.", "http://", "https://www.", "https://"].indexOf()`

## getRemoteImageUrl()
- 位置: L322-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `lazy.FaviconUtils.TRUSTED_FAVICON_SCHEMES.includes()`, `parsedUrl.protocol.slice()`
- 条件付き依存: `if ( !controller?.rendersInContentProcess && !lazy.FaviconUtils.TRUSTED_FAVICON_SCHEMES.includes(scheme) )` → `controller?.browserWindow?.matchMedia()`
- 条件付き依存: `if (size)` → `Math.floor()`
- 条件付き依存: `if ( !controller?.rendersInContentProcess && !lazy.FaviconUtils.TRUSTED_FAVICON_SCHEMES.includes(scheme) )` → `lazy.FaviconUtils.getMozRemoteImageURL()`
- 参照: `controller?.browserWindow?.devicePixelRatio`, `controller?.browserWindow?.matchMedia?.( "(prefers-color-scheme: dark)" ).matches`, `controller?.rendersInContentProcess`, `opts.size`

## getEngineIconUrl()
- 位置: async L365-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^(?:blob|moz-extension):/.test()`, `engine.getIconURL()`, `gEngineIconDataUrls.get()`
- 条件付き依存: `if (!dataUrl)` → `fetch()`
- 条件付き依存: `if (!dataUrl)` → `lazy.blobAsDataURL()`
- 条件付き依存: `if (!dataUrl)` → `response.blob()`
- 条件付き依存: `if (!dataUrl)` → `console.error()`
- 条件付き依存: `if (!dataUrl)` → `gEngineIconDataUrls.delete()`
- 条件付き依存: `if (!dataUrl)` → `gEngineIconDataUrls.set()`
- 参照: `controller?.rendersInContentProcess`, `engine.id`

## setupSpeculativeConnection()
- 位置: L403-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.io.speculativeConnect()`, `URL.isInstance()`, `lazy.UrlbarPrefs.get()`, `window.docShell.QueryInterface()`
- 条件付き依存: `if (urlOrEngine instanceof lazy.SearchEngine)` → `urlOrEngine.speculativeConnect()`
- 参照: `Ci.nsIInterfaceRequestor`, `Ci.nsIURI`, `lazy.SearchEngine`, `urlOrEngine.href`, `window.gBrowser.contentPrincipal`, `window.gBrowser.contentPrincipal.originAttributes`
- XPCOM: [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / [`nsIURI`](../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## extractRefFromUrl()
- 位置: L449-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `URL.parse(url)?.URI`, `uri.ref`, `uri.specIgnoringRef`

## stripPublicSuffixFromHost()
- 位置: L467-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getKnownPublicSuffixFromHost()`, `host.substring()`
- 参照: `Cr.NS_ERROR_HOST_IS_IP_ADDRESS`, `Services.eTLD.getKnownPublicSuffixFromHost(host).length`, `ex.result`, `host.length`
- XPCOM: `Services.eTLD`

## getURIFixupInfo()
- 位置: L491-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `console.error()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## getFixupPrimitives()
- 位置: L521-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getURIFixupInfo()`
- 参照: `info.keywordAsSent`, `info.preferredURI?.displaySpec`

## addToInputHistory()
- 位置: async L541-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `input.toLowerCase()`, `lazy.PlacesUtils.withConnectionWrapper()`
- 参照: `lazy.historyEnabled`, `rows.length`

## addToInputHistoryWhenReady()
- 位置: async L578-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesObservers.addListener()`, `PlacesObservers.removeListener()`, `Promise.withResolvers()`, `lazy.clearTimeout()`, `lazy.setTimeout()`, `this.addToInputHistory()`, `visitedResolve()`
- 条件付き依存: `if (await this.addToInputHistory(url, input))` → `PlacesObservers.removeListener()`
- 条件付き依存: `if (await this.addToInputHistory(url, input))` → `lazy.clearTimeout()`
- 条件付き依存: `if (visited)` → `this.addToInputHistory()`
- 参照: `lazy.historyEnabled`

## listener()
- 位置: L586-594
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "page-visited" && event.url == url)` → `PlacesObservers.removeListener()`
- 条件付き依存: `if (event.type == "page-visited" && event.url == url)` → `visitedResolve()`
- 参照: `event.type`, `event.url`

## removeInputHistory()
- 位置: async L627-639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `input.toLowerCase()`, `lazy.PlacesUtils.withConnectionWrapper()`

## blockAutofill()
- 位置: async L651-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isOriginUrl()`
- 条件付き依存: `if (UrlbarShared.isOriginUrl(url))` → `this.blockOriginAutofill()`
- 条件付き依存: `if (!(UrlbarShared.isOriginUrl(url)))` → `this.blockOriginPageAutofill()`

## blockOriginAutofill()
- 位置: async L673-692
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`

## blockOriginPageAutofill()
- 位置: async L707-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`

## clearOriginAutofillBlock()
- 位置: async L747-772
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`
- 参照: `rows.length`

## clearOriginPageAutofillBlock()
- 位置: async L788-813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`, `origin.host.replace()`, `parseOriginParts()`
- 参照: `rows.length`

## _backspaceBlockKey()
- 位置: L875-885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isOriginUrl()`, `origin.host.replace()`, `parseOriginParts()`

## recordAutofillBackspace()
- 位置: L903-907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._doRecordAutofillBackspace()`
- 参照: `this._lastRecordAutofillBackspacePromise`

## _doRecordAutofillBackspace()
- 位置: async L909-946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._backspaceBlockKey()`, `this._backspaceBlocks.delete()`, `this._backspaceBlocks.get()`, `this._backspaceBlocks.set()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `Date.now()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `this.blockAutofill( url, Date.now() + lazy.UrlbarPrefs.get("autoFill.backspaceBlockDurationMs") ).catch()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `this.blockAutofill()`
- 条件付き依存: `if (newCount >= lazy.UrlbarPrefs.get("autoFill.backspaceThreshold"))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (this._backspaceBlocks.size > this._BACKSPACE_BLOCKS_MAX)` → `this._backspaceBlocks.keys().next()`
- 条件付き依存: `if (this._backspaceBlocks.size > this._BACKSPACE_BLOCKS_MAX)` → `this._backspaceBlocks.keys()`
- 条件付き依存: `if (this._backspaceBlocks.size > this._BACKSPACE_BLOCKS_MAX)` → `this._backspaceBlocks.delete()`
- 参照: `console.error`, `entry.blockedAt`, `entry.count`, `this._BACKSPACE_BLOCKS_MAX`, `this._backspaceBlocks.keys().next().value`, `this._backspaceBlocks.size`

## getBackspaceBlock()
- 位置: L962-982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._backspaceBlockKey()`, `this._backspaceBlocks.delete()`, `this._backspaceBlocks.get()`
- 参照: `entry.blockedAt`, `entry?.blockedAt`, `this._BACKSPACE_BLOCK_MAX_AGE_HOURS`

## clearAutofillBackspaceEntryForUrl()
- 位置: L990-995
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._backspaceBlockKey()`
- 条件付き依存: `if (key)` → `this._backspaceBlocks.delete()`

## dismissAutofill()
- 位置: async L1011-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clearAutofillBackspaceEntryForUrl()`
- 条件付き依存: `if (removeFromHistory)` → `lazy.PlacesUtils.history.remove(url).catch()`
- 条件付き依存: `if (removeFromHistory)` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (!(removeFromHistory))` → `this.blockAutofill( url, Date.now() + lazy.UrlbarPrefs.get("autoFill.dismissalBlockDurationMs") ).catch()`
- 条件付き依存: `if (!(removeFromHistory))` → `this.blockAutofill()`
- 条件付き依存: `if (!(removeFromHistory))` → `Date.now()`
- 条件付き依存: `if (!(removeFromHistory))` → `lazy.UrlbarPrefs.get()`
- 参照: `console.error`

## reintegrateAutofill()
- 位置: async L1036-1051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isOriginUrl()`, `this.clearAutofillBackspaceEntryForUrl()`, `this.clearOriginAutofillBlock()`, `this.clearOriginPageAutofillBlock()`, `this.getBackspaceBlock()`

## isPersistedSearchTermsEnabled()
- 位置: L1058-1064
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`

## substringAt()
- 位置: L1077-1080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sourceStr.indexOf()`, `sourceStr.substr()`

## substringAfter()
- 位置: L1093-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sourceStr.indexOf()`, `sourceStr.substr()`
- 参照: `targetStr.length`

## stripURLPrefix()
- 位置: L1109-1129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.PROTOCOLS_WITHOUT_AUTHORITY.includes()`, `lazy.UrlUtils.REGEXP_PREFIX.exec()`, `prefix.endsWith()`, `prefix.toLowerCase()`, `str.substring()`
- 参照: `prefix.length`, `str.length`

## addToFormHistory()
- 位置: async L1142-1162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormHistory.update()`
- 参照: `lazy.DEFAULT_FORM_HISTORY_PARAM`, `lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VALUE_LENGTH`, `value.length`

## clearFormHistory()
- 位置: L1169-1174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormHistory.update()`
- 参照: `lazy.DEFAULT_FORM_HISTORY_PARAM`

## tupleString()
- 位置: L1184-1186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tokens.filter()`, `tokens.filter(t => t).join()`

## copySnakeKeysToCamel()
- 位置: L1201-1225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `key.match()`, `key.replace()`, `obj.hasOwnProperty()`, `p1.toUpperCase()`
- 条件付き依存: `if (match)` → `key.substring()`
- 条件付き依存: `if (value && typeof value == "object")` → `this.copySnakeKeysToCamel()`
- 参照: `match[0].length`

## createTabSwitchSecondaryAction()
- 位置: L1234-1257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getPublicIdentityFromId()`
- 条件付き依存: `if (identity)` → `lazy.ContextualIdentityService.getUserContextLabel( userContextId ).toLowerCase()`
- 条件付き依存: `if (identity)` → `lazy.ContextualIdentityService.getUserContextLabel()`
- 参照: `action.classList`, `action.l10nArgs`, `action.l10nId`, `identity.color`

## getUserContextData()
- 位置: L1270-1288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextualIdentityService.getContainerIconURL()`, `lazy.ContextualIdentityService.getPublicIdentityFromId()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `lazy.ContextualIdentityService.getUserContextLabel( userContextId ).trim()`
- 参照: `identity.color`, `identity.icon`

## getURLBarForFocus()
- 位置: L1300-1314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `lazy.AIWindow.shouldUseImmersiveView()`
- 条件付き依存: `if ( lazy.AIWindow.isAIWindowActive(window) && lazy.AIWindow.shouldUseImmersiveView(window.gBrowser.currentURI) )` → `lazy.AIWindow.getSmartbarForWindow()`
- 参照: `window.gBrowser.currentURI`, `window.gURLBar`

## formatUnitConversionResult()
- 位置: L1322-1358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if (!( Math.abs(result) >= FULL_NUMBER_MAX_THRESHOLD || (Math.abs(result) <= FULL_NUMBER_MIN_THRESHOLD && result !== 0) ))` → `Math.abs()`
- 参照: `Intl.NumberFormat`, `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## UrlbarMuxer.name()
- 位置: L1897-1899
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarMuxer.sort()
- 位置: L1909-1911
- 役割: (未記入)
- 触るとき: (未記入)

## logger()
- 位置: L1920-1920
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getLogger()`
- 参照: `this.name`

## UrlbarProvider.logger()
- 位置: L1923-1925
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#lazy.logger`

## UrlbarProvider.name()
- 位置: L1933-1935
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.constructor.name`

## UrlbarProvider.type()
- 位置: L1943-1945
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.tryMethod()
- 位置: L1974-1981
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this[methodName]()`

## UrlbarProvider.isActive()
- 位置: async L1996-1998
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.getPriority()
- 位置: L2010-2013
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.startQuery()
- 位置: L2030-2032
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.cancelQuery()
- 位置: L2041-2043
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.onBeforeSelection()
- 位置: L2168-2168
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.onSelection()
- 位置: L2181-2181
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.getViewTemplate()
- 位置: L2259-2261
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.getViewUpdate()
- 位置: L2332-2334
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.getResultCommands()
- 位置: L2348-2350
- 役割: (未記入)
- 触るとき: (未記入)

## UrlbarProvider.deferUserSelection()
- 位置: L2362-2364
- 役割: (未記入)
- 触るとき: (未記入)

## SkippableTimer.constructor()
- 位置: L2396-2442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `Promise.race()`, `Promise.race([timerPromise, firePromise]).then()`, `resolve()`, `this._log()`, `this._timer.initWithCallback()`
- 条件付き依存: `if (callback && !this._canceled)` → `callback()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `this._canceled`, `this._timer`, `this.done`, `this.fire`, `this.logger`, `this.name`, `this.promise`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## this.fire()
- 位置: async L2422-2433
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._canceled)` → `this._log()`
- 条件付き依存: `if (this._timer)` → `this._timer.cancel()`
- 条件付き依存: `if (this._timer)` → `resolve()`
- 参照: `this._canceled`, `this._timer`, `this.done`, `this.promise`

## SkippableTimer.cancel()
- 位置: async L2449-2455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fire()`
- 条件付き依存: `if (this._timer)` → `this._log()`
- 参照: `this._canceled`, `this._timer`

## SkippableTimer._log()
- 位置: L2457-2465
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.logger)` → `this.logger.debug()`
- 条件付き依存: `if (isError)` → `console.error()`
- 参照: `this.logger`, `this.name`

## TaskQueue.emptyPromise()
- 位置: L2479-2481
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#emptyPromise`

## TaskQueue.queue()
- 位置: L2496-2505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#queue.push()`
- 条件付き依存: `if (this.#queue.length == 1)` → `Promise.withResolvers()`
- 条件付き依存: `if (this.#queue.length == 1)` → `this.#doNextTask()`
- 参照: `this.#emptyDeferred`, `this.#emptyDeferred.promise`, `this.#emptyPromise`, `this.#queue.length`

## TaskQueue.queueIdleCallback()
- 位置: L2517-2531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`, `callback()`, `console.error()`, `reject()`, `resolve()`, `this.queue()`

## TaskQueue.#doNextTask()
- 位置: async L2537-2557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `console.error()`, `reject()`, `resolve()`, `this.#doNextTask()`, `this.#queue.shift()`
- 条件付き依存: `if (!this.#queue.length)` → `this.#emptyDeferred.resolve()`
- 参照: `this.#emptyDeferred`, `this.#queue`, `this.#queue.length`
