# browser/components/asrouter/modules/ASRouterTriggerListeners.sys.mjs

source: browser/components/asrouter/modules/ASRouterTriggerListeners.sys.mjs
source-hash: c49400864be76220249f465da1a0e66044c298d7
lines: 2297

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`

## log()
- 位置: L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## isPrivateWindow()
- 位置: L59-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `Ci.nsIDOMWindow`, `win.closed`
- XPCOM: [`nsIDOMWindow`](../../../../dom/base/nsISlowScriptDebug.idl.md)

## checkURLMatch()
- 位置: L74-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aRequest.QueryInterface()`, `hosts.has()`
- 条件付き依存: `if (matchPatternSet)` → `matchPatternSet.matches()`
- 条件付き依存: `if (regexPatterns)` → `regex.test()`
- 条件付き依存: `if (originalLocation.spec !== aLocationURI.spec)` → `hosts.has()`
- 参照: `Ci.nsIChannel`, `aLocationURI.host`, `aLocationURI.spec`, `aRequest.QueryInterface(Ci.nsIChannel).originalURI`, `match.host`, `match.url`, `originalLocation.host`, `originalLocation.spec`
- XPCOM: [`nsIChannel`](../../../../docshell/base/nsIDocShell.idl.md)

## isDirectNavigationUrlbarResult()
- 位置: L156-170
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `result.source`, `result.type`

## createMatchPatternSet()
- 位置: L172-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`

## init()
- 位置: L205-216
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._initialized)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!this._initialized)` → `this._lastValues.set()`
- 参照: `this._initialized`, `this._lastValues`, `this._trackedPrefs`, `this._triggerHandler`
- XPCOM: `Services.obs` / `Services.prefs`

## observe()
- 位置: L218-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.wm.getMostRecentBrowserWindow()`, `this._lastValues.get()`
- 条件付き依存: `if (current !== previous)` → `this._lastValues.set()`
- 条件付き依存: `if (browser)` → `this._triggerHandler()`
- 参照: `Services.wm.getMostRecentBrowserWindow()?.gBrowser?.selectedBrowser`, `this._trackedPrefs`, `this.id`
- XPCOM: `Services.prefs` / `Services.wm`

## uninit()
- 位置: L250-257
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._lastValues`, `this._triggerHandler`
- XPCOM: `Services.obs`

## init()
- 位置: L276-299
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.receiveMessage.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.AboutReaderParent.addMessageListener()`
- 条件付き依存: `if (patterns)` → `createMatchPatternSet()`
- 条件付き依存: `if (hosts)` → `hosts.forEach()`
- 条件付き依存: `if (hosts)` → `this._hosts.add()`
- 条件付き依存: `if (regexPatterns)` → `regexPatterns.map()`
- 参照: `this._initialized`, `this._matchPatternSet`, `this._matchPatternSet.patterns`, `this._regexPatterns`, `this._triggerHandler`, `this.readerModeEvent`, `this.receiveMessage`

## receiveMessage()
- 位置: L301-312
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (data && data.isArticle)` → `checkURLMatch()`
- 条件付き依存: `if (match)` → `this._triggerHandler()`
- 参照: `data.isArticle`, `target.currentURI`, `this._hosts`, `this._matchPatternSet`, `this._regexPatterns`, `this.id`

## uninit()
- 位置: L314-326
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.AboutReaderParent.removeMessageListener()`
- 参照: `this._hosts`, `this._initialized`, `this._matchPatternSet`, `this._regexPatterns`, `this._triggerHandler`, `this.readerModeEvent`

## init()
- 位置: L338-344
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.bookmarkEvent`
- XPCOM: `Services.obs`

## observe()
- 位置: L346-355
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === this.bookmarkEvent && data === "starred")` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if (browser)` → `this._triggerHandler()`
- 参照: `browser.gBrowser.selectedBrowser`, `this.bookmarkEvent`, `this.id`
- XPCOM: `Services.wm`

## uninit()
- 位置: L357-364
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._hosts`, `this._initialized`, `this._triggerHandler`, `this.bookmarkEvent`
- XPCOM: `Services.obs`

## init()
- 位置: L384-403
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.PlacesUtils.observers.addListener()`
- 参照: `lazy.PlacesUtils.bookmarks.SOURCES .SYNC_REPARENT_REMOVED_FOLDER_CHILDREN`, `lazy.PlacesUtils.bookmarks.SOURCES.IMPORT`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE_ON_STARTUP`, `lazy.PlacesUtils.bookmarks.SOURCES.SYNC`, `this._initialized`, `this._sourcesToIgnore`, `this._triggerHandler`, `this.handlePlacesEvents`

## uninit()
- 位置: L405-414
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.PlacesUtils.observers.removeListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.handlePlacesEvents`

## handlePlacesEvents()
- 位置: L416-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `isPrivateWindow()`, `this._sourcesToIgnore.includes()`
- 条件付き依存: `if ( ev.itemType === lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK && !ev.isTagging && !this._sourcesToIgnore.includes(ev.source) )` → `this._triggerHandler()`
- 参照: `ev.isTagging`, `ev.itemType`, `ev.source`, `lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK`, `this.id`, `window.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## init()
- 位置: L451-470
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.onLocationChange.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `isPrivateWindow()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.removeTabsProgressListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`, `this.onLocationChange`

## uninit()
- 位置: L472-478
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## onLocationChange()
- 位置: async L480-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if (isBookmarked && this._triggerHandler)` → `this._triggerHandler()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`, `this._triggerHandler`, `this.id`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## init()
- 位置: L521-561
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.onTabSwitch.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `isPrivateWindow()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.addEventListener()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.removeEventListener()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.removeTabsProgressListener()`
- 条件付き依存: `if (patterns)` → `createMatchPatternSet()`
- 条件付き依存: `if (this._hosts)` → `hosts.forEach()`
- 条件付き依存: `if (this._hosts)` → `this._hosts.add()`
- 条件付き依存: `if (regexPatterns)` → `regexPatterns.map()`
- 参照: `this._hosts`, `this._initialized`, `this._matchPatternSet`, `this._matchPatternSet.patterns`, `this._regexPatterns`, `this._triggerHandler`, `this._visits`, `this.id`, `this.onTabSwitch`

## _updateVisits()
- 位置: L570-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._visits.get()`
- 条件付き依存: `if (visits && Date.now() - visits[0] > FEW_MINUTES)` → `this._visits.set()`
- 条件付き依存: `if (visits && Date.now() - visits[0] > FEW_MINUTES)` → `Date.now()`
- 条件付き依存: `if (!visits)` → `this._visits.set()`
- 条件付き依存: `if (!visits)` → `Date.now()`

## onTabSwitch()
- 位置: L585-599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkURLMatch()`
- 条件付き依存: `if (match)` → `this.triggerHandler()`
- 参照: `event.target.documentGlobal`, `event.target.documentGlobal.gBrowser`, `gBrowser.currentURI`, `gBrowser.selectedBrowser`, `this._hosts`, `this._matchPatternSet`, `this._regexPatterns`

## triggerHandler()
- 位置: L601-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._triggerHandler()`, `this._updateVisits()`, `this._visits .get()`, `this._visits .get(match.host) .map()`
- 参照: `match.host`, `this.id`

## onLocationChange()
- 位置: L623-644
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWebProgress.isTopLevel && !isSameDocument)` → `checkURLMatch()`
- 条件付き依存: `if (match)` → `this.triggerHandler()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`, `this._hosts`, `this._matchPatternSet`, `this._regexPatterns`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## uninit()
- 位置: L646-657
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._hosts`, `this._initialized`, `this._matchPatternSet`, `this._regexPatterns`, `this._triggerHandler`, `this._visits`, `this.id`

## init()
- 位置: L693-735
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.onLocationChange.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `isPrivateWindow()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.removeTabsProgressListener()`
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (patterns)` → `createMatchPatternSet()`
- 条件付き依存: `if (this._hosts)` → `hosts.forEach()`
- 条件付き依存: `if (this._hosts)` → `this._hosts.add()`
- 条件付き依存: `if (regexPatterns)` → `regexPatterns.map()`
- 参照: `this._hosts`, `this._initialized`, `this._matchPatternSet`, `this._matchPatternSet.patterns`, `this._recentUrlbarNavigations`, `this._regexPatterns`, `this._totalVisits`, `this._triggerHandler`, `this._visits`, `this.id`, `this.onLocationChange`
- XPCOM: `Services.obs`

## uninit()
- 位置: L737-751
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._hosts`, `this._initialized`, `this._matchPatternSet`, `this._recentUrlbarNavigations`, `this._regexPatterns`, `this._totalVisits`, `this._triggerHandler`, `this._visits`, `this.id`
- XPCOM: `Services.obs`

## observe()
- 位置: L753-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isDirectNavigationUrlbarResult()`, `isPrivateWindow()`, `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (browser)` → `this._recentUrlbarNavigations.set()`
- 条件付き依存: `if (browser)` → `Date.now()`
- 参照: `subject.wrappedJSObject.result`, `window.gBrowser?.selectedBrowser`

## _isAddressBarUrlNavigation()
- 位置: L776-783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this._recentUrlbarNavigations.delete()`, `this._recentUrlbarNavigations.get()`

## onLocationChange()
- 位置: L785-821
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWebProgress.isTopLevel && !isSameDocument)` → `this._isAddressBarUrlNavigation()`
- 条件付き依存: `if (aWebProgress.isTopLevel && !isSameDocument)` → `checkURLMatch()`
- 条件付き依存: `if (match)` → `this._visits.get()`
- 条件付き依存: `if (match)` → `this._visits.set()`
- 条件付き依存: `if (match)` → `this._triggerHandler()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`, `match.host`, `match.url`, `this._hosts`, `this._matchPatternSet`, `this._regexPatterns`, `this._totalVisits`, `this.id`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## init()
- 位置: L841-851
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.handlePlacesEvents.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.PlacesUtils.observers.addListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.handlePlacesEvents`

## uninit()
- 位置: L853-862
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.PlacesUtils.observers.removeListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.handlePlacesEvents`

## handlePlacesEvents()
- 位置: L864-907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `builtInFolders.includes()`, `isPrivateWindow()`, `sourcesToIgnore.includes()`
- 条件付き依存: `if ( ev.itemType === lazy.PlacesUtils.bookmarks.TYPE_FOLDER || (ev.itemType === lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK && !builtInFolders.includes(ev.parentGui...)` → `this._triggerHandler()`
- 参照: `ev.isTagging`, `ev.itemType`, `ev.parentGuid`, `ev.source`, `lazy.PlacesUtils.bookmarks.SOURCES .SYNC_REPARENT_REMOVED_FOLDER_CHILDREN`, `lazy.PlacesUtils.bookmarks.SOURCES.IMPORT`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE_ON_STARTUP`, `lazy.PlacesUtils.bookmarks.SOURCES.SYNC`, `lazy.PlacesUtils.bookmarks.TYPE_BOOKMARK`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `lazy.PlacesUtils.bookmarks.menuGuid`, `lazy.PlacesUtils.bookmarks.mobileGuid`, `lazy.PlacesUtils.bookmarks.rootGuid`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `lazy.PlacesUtils.bookmarks.unfiledGuid`, `window.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## init()
- 位置: L925-932
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 参照: `this._initialized`, `this._triggerHandler`
- XPCOM: `Services.obs`

## uninit()
- 位置: L934-942
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._triggerHandler`
- XPCOM: `Services.obs`

## observe()
- 位置: L944-971
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._triggerHandler()`
- 参照: `aSubject.currentURI.asciiHost`

## init()
- 位置: L985-991
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 参照: `this._initialized`, `this._topic`, `this._triggerHandler`
- XPCOM: `Services.obs`

## uninit()
- 位置: L993-999
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._topic`, `this._triggerHandler`
- XPCOM: `Services.obs`

## observe()
- 位置: L1001-1047
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `this._collections.includes()`, `this._events.includes()`
- 条件付き依存: `if (this._events.includes(data))` → `lazy.setTimeout()`
- 条件付き依存: `if (this._events.includes(data))` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if ( this._initialized && // Make sure the browser still exists and is still selected. browser.isConnectedAndReady && browser === Services.wm.getMostRecentBrowse...)` → `this._triggerHandler()`
- 参照: `Services.wm.getMostRecentBrowserWindow()?.gBrowser .selectedBrowser`, `Services.wm.getMostRecentBrowserWindow()?.gBrowser.selectedBrowser`, `browser.contentWindow?.gSubDialog?.dialogs.length`, `browser.isConnectedAndReady`, `subject.wrappedJSObject`, `this._initialized`, `this._topic`, `this._triggerDelay`, `this.id`
- XPCOM: `Services.wm`

## init()
- 位置: L1060-1087
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `params.forEach()`, `this._events.push()`
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._initialized)` → `this._onLocationChange.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `isPrivateWindow()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (!isPrivateWindow(win))` → `win.gBrowser.removeTabsProgressListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`, `this.onLocationChange`
- XPCOM: `Services.obs`

## uninit()
- 位置: L1089-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._events`, `this._initialized`, `this._sessionPageLoad`, `this._triggerHandler`, `this.id`, `this.onLocationChange`
- XPCOM: `Services.obs`

## observe()
- 位置: L1108-1144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._events.filter()`, `this._events.includes()`
- 条件付き依存: `if (this._events.filter(e => (e & event) === e).length)` → `this._triggerHandler()`
- 条件付き依存: `if (this._events.includes(aSubject.wrappedJSObject.event))` → `this._triggerHandler()`
- 条件付き依存: `if (this._events.includes(aSubject.wrappedJSObject.event))` → `Services.wm.getMostRecentBrowserWindow()`
- 参照: `Services.wm.getMostRecentBrowserWindow().gBrowser .selectedBrowser`, `aSubject.wrappedJSObject`, `aSubject.wrappedJSObject.event`, `this._events.filter(e => (e & event) === e).length`, `this._sessionPageLoad`
- XPCOM: `Services.wm`

## _onLocationChange()
- 位置: L1146-1166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http", "https"].includes()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aLocationURI.scheme`, `aWebProgress.isTopLevel`, `this._sessionPageLoad`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _shouldShowCaptivePortalVPNPromo()
- 位置: L1177-1179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUtils.shouldShowVPNPromo()`

## init()
- 位置: L1181-1187
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `Services.obs.addObserver()`
- 参照: `this._initialized`, `this._triggerHandler`
- XPCOM: `Services.obs`

## observe()
- 位置: L1189-1206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `this._shouldShowCaptivePortalVPNPromo()`
- 条件付き依存: `if (browser && this._shouldShowCaptivePortalVPNPromo())` → `this._triggerHandler()`
- 参照: `browser.gBrowser.selectedBrowser`, `this.id`
- XPCOM: `Services.wm`

## uninit()
- 位置: L1208-1214
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._triggerHandler`
- XPCOM: `Services.obs`

## init()
- 位置: L1226-1235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `prefs.forEach()`, `this._observedPrefs.push()`
- 参照: `this._initialized`, `this._triggerHandler`
- XPCOM: `Services.prefs`

## observe()
- 位置: L1237-1252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `this._observedPrefs.includes()`
- 条件付き依存: `if (browser && this._observedPrefs.includes(aData))` → `this._triggerHandler()`
- 参照: `browser.gBrowser.selectedBrowser`, `this.id`
- XPCOM: `Services.wm`

## uninit()
- 位置: L1254-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._observedPrefs.forEach()`
- 条件付き依存: `if (this._initialized)` → `Services.prefs.removeObserver()`
- 参照: `this._initialized`, `this._observedPrefs`, `this._triggerHandler`
- XPCOM: `Services.prefs`

## init()
- 位置: L1275-1289
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## handleEvent()
- 位置: L1290-1314
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._triggerHandler()`
- 参照: `event.target`, `event.target.documentGlobal`, `event.target.documentGlobal.gBrowser`, `gBrowser.selectedBrowser`, `gBrowser.tabs.length`, `tab.smartWindowActionSource`, `this._closedTabs`, `this._initialized`, `this.id`

## uninit()
- 位置: L1315-1322
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._closedTabs`, `this._initialized`, `this._triggerHandler`, `this.id`

## init()
- 位置: L1334-1348
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## handleEvent()
- 位置: L1349-1364
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._triggerHandler()`
- 参照: `event.target.documentGlobal`, `event.target.documentGlobal.gBrowser`, `gBrowser.selectedBrowser`, `gBrowser.tabs.length`, `this._initialized`, `this._openTabs`, `this.id`

## uninit()
- 位置: L1365-1372
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._initialized`, `this._openTabs`, `this._triggerHandler`, `this.id`

## init()
- 位置: L1384-1398
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## handleEvent()
- 位置: L1399-1413
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._triggerHandler()`
- 参照: `event.target.documentGlobal`, `event.target.documentGlobal.gBrowser`, `gBrowser.selectedBrowser`, `this._initialized`, `this._tabGroupsCreated`, `this.id`

## uninit()
- 位置: L1414-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._initialized`, `this._tabGroupsCreated`, `this._triggerHandler`, `this.id`

## init()
- 位置: L1433-1447
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## handleEvent()
- 位置: L1448-1462
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._triggerHandler()`
- 参照: `event.target.documentGlobal`, `event.target.documentGlobal.gBrowser`, `gBrowser.selectedBrowser`, `this._initialized`, `this._tabGroupsSaved`, `this.id`

## uninit()
- 位置: L1463-1470
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._initialized`, `this._tabGroupsSaved`, `this._triggerHandler`, `this.id`

## init()
- 位置: L1482-1496
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## handleEvent()
- 位置: L1497-1511
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._triggerHandler()`
- 参照: `event.target.documentGlobal`, `event.target.documentGlobal.gBrowser`, `gBrowser.selectedBrowser`, `this._initialized`, `this._tabGroupsCollapsed`, `this.id`

## uninit()
- 位置: L1512-1519
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._initialized`, `this._tabGroupsCollapsed`, `this._triggerHandler`, `this.id`

## _isVisible()
- 位置: L1560-1564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `[...Services.wm.getEnumerator("navigator:browser")].some()`
- 参照: `win.closed`, `win.document?.hidden`
- XPCOM: `Services.wm`

## _soundPlaying()
- 位置: L1565-1569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `[...Services.wm.getEnumerator("navigator:browser")].some()`, `win.gBrowser?.tabs.some()`
- 参照: `tab.closing`, `tab.soundPlaying`
- XPCOM: `Services.wm`

## init()
- 位置: L1570-1610
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._idleService)` → `Cc[ "@mozilla.org/widget/useridleservice;1" ].getService()`
- 条件付き依存: `if ( !this._initialized && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `this._idleService.addIdleObserver()`
- 条件付き依存: `if ( !this._initialized && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `Services.obs.addObserver()`
- 条件付き依存: `if ( !this._initialized && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if ( !this._initialized && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `win.addEventListener()`
- 条件付き依存: `if ( !this._initialized && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `win.removeEventListener()`
- 条件付き依存: `if (!this._soundPlaying)` → `Date.now()`
- 条件付き依存: `if ( !this._initialized && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `this.log()`
- 参照: `Ci.nsIUserIdleService`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._idleService`, `this._idleService.idleTime`, `this._idleThreshold`, `this._initialized`, `this._listenedEvents`, `this._observedTopics`, `this._quietSince`, `this._soundPlaying`, `this._triggerHandler`, `this.id`
- XPCOM: `nsIUserIdleService` / `@mozilla.org/widget/useridleservice;1` / `Services.obs`

## observe()
- 位置: L1611-1667
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this.log()`
- 条件付き依存: `if (this._initialized)` → `Date.now()`
- 条件付き依存: `if (this._initialized)` → `parseInt()`
- 条件付き依存: `if (this._initialized)` → `isNaN()`
- 条件付き依存: `if (this._isVisible)` → `this._onActive()`
- 参照: `this._awaitingVisibilityChange`, `this._idleService.idleTime`, `this._idleSince`, `this._initialized`, `this._isVisible`, `this._lastWakeTime`, `this._quietSince`, `this._wakeDelay`

## handleEvent()
- 位置: L1668-1700
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._awaitingVisibilityChange && this._isVisible)` → `this._onActive()`
- 条件付き依存: `if (this._initialized)` → `event.detail?.changed?.includes()`
- 条件付き依存: `if (this._initialized)` → `this.log()`
- 条件付き依存: `if (!this._quietSince)` → `Date.now()`
- 参照: `event.type`, `this._awaitingVisibilityChange`, `this._idleService.idleTime`, `this._idleSince`, `this._initialized`, `this._isVisible`, `this._lastWakeTime`, `this._quietSince`, `this._soundPlaying`

## _onActive()
- 位置: L1701-1724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.log()`
- 条件付き依存: `if (this._idleSince && this._quietSince)` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if (this._idleSince && this._quietSince)` → `isPrivateWindow()`
- 条件付き依存: `if (win && !isPrivateWindow(win) && !this._triggerTimeout)` → `Date.now()`
- 条件付き依存: `if (win && !isPrivateWindow(win) && !this._triggerTimeout)` → `Math.max()`
- 条件付き依存: `if (win && !isPrivateWindow(win) && !this._triggerTimeout)` → `lazy.setTimeout()`
- 条件付き依存: `if (win && !isPrivateWindow(win) && !this._triggerTimeout)` → `this._triggerHandler()`
- 参照: `this._idleService.idleTime`, `this._idleSince`, `this._lastWakeTime`, `this._quietSince`, `this._triggerDelay`, `this._triggerTimeout`, `this.id`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## uninit()
- 位置: L1725-1742
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `this._idleService.removeIdleObserver()`
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 条件付き依存: `if (this._initialized)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this._initialized)` → `this.log()`
- 参照: `this._awaitingVisibilityChange`, `this._idleSince`, `this._idleThreshold`, `this._initialized`, `this._lastWakeTime`, `this._observedTopics`, `this._quietSince`, `this._triggerHandler`, `this._triggerTimeout`, `this.id`
- XPCOM: `Services.obs`

## log()
- 位置: L1743-1745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`

## init()
- 位置: L1761-1784
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.onLocationChange.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `this.onBrowserWindow()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.gBrowser.removeTabsProgressListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`, `this.onLocationChange`, `this.onStateChange`

## uninit()
- 位置: L1786-1802
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 条件付き依存: `if (this._initialized)` → `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 条件付き依存: `if (this._initialized)` → `this._callouts.get()`
- 条件付き依存: `if (item)` → `item.callout.endTour()`
- 条件付き依存: `if (item)` → `item.cleanup()`
- 条件付き依存: `if (item)` → `this._callouts.delete()`
- 参照: `this._callouts`, `this._initialized`, `this._triggerHandler`, `this.id`

## showFeatureCalloutTour()
- 位置: async L1804-1833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterTargeting.getMessageTriggers()`, `this._triggerHandler()`
- 条件付き依存: `if (lazy.ASRouterTargeting.getMessageTriggers(result.message).length)` → `lazy.FeatureCalloutBroker.showCustomFeatureCallout()`
- 条件付き依存: `if (callout)` → `this._callouts.set()`
- 参照: `callout.panelId`, `lazy.ASRouterTargeting.getMessageTriggers(result.message).length`, `result.message`, `result.message.content?.tour_pref_default_value`, `result.message.content?.tour_pref_name`

## cleanup()
- 位置: L1822-1824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callouts.delete()`

## onLocationChange()
- 位置: L1835-1857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `this._callouts.get()`, `this._callouts.has()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isPDFJS) )` → `existingCallout.callout.endTour()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isPDFJS) )` → `existingCallout.cleanup()`
- 条件付き依存: `if (!this._callouts.has(win) && isPDFJS)` → `this.showFeatureCalloutTour()`
- 参照: `browser.contentPrincipal.originNoSuffix`, `existingCallout.panelId`, `tab.linkedPanel`, `tabbrowser.documentGlobal`, `tabbrowser.selectedBrowser`, `tabbrowser.selectedTab`

## handleEvent()
- 位置: L1859-1903
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.getBrowserForTab()`, `this._callouts.get()`, `this._callouts.has()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isPDFJS) )` → `existingCallout.callout.endTour()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isPDFJS) )` → `existingCallout.cleanup()`
- 条件付き依存: `if (!this._callouts.has(win) && isPDFJS)` → `this.showFeatureCalloutTour()`
- 条件付き依存: `if ( existingCallout && existingCallout.panelId === tab.linkedPanel )` → `existingCallout.callout.endTour()`
- 条件付き依存: `if ( existingCallout && existingCallout.panelId === tab.linkedPanel )` → `existingCallout.cleanup()`
- 参照: `browser.contentPrincipal.originNoSuffix`, `event.target`, `event.type`, `existingCallout.panelId`, `gBrowser.selectedTab`, `tab.documentGlobal`, `tab.linkedPanel`

## onBrowserWindow()
- 位置: L1905-1907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onLocationChange()`
- 参照: `win.gBrowser.selectedBrowser`

## init()
- 位置: L1918-1941
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `this.onLocationChange.bind()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `this.onBrowserWindow()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.gBrowser.removeTabsProgressListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`, `this.onLocationChange`, `this.onStateChange`

## uninit()
- 位置: L1943-1959
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 条件付き依存: `if (this._initialized)` → `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 条件付き依存: `if (this._initialized)` → `this._callouts.get()`
- 条件付き依存: `if (item)` → `item.callout.endTour()`
- 条件付き依存: `if (item)` → `item.cleanup()`
- 条件付き依存: `if (item)` → `this._callouts.delete()`
- 参照: `this._callouts`, `this._initialized`, `this._triggerHandler`, `this.id`

## showFeatureCalloutTour()
- 位置: async L1961-1990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterTargeting.getMessageTriggers()`, `this._triggerHandler()`
- 条件付き依存: `if (lazy.ASRouterTargeting.getMessageTriggers(result.message).length)` → `lazy.FeatureCalloutBroker.showCustomFeatureCallout()`
- 条件付き依存: `if (callout)` → `this._callouts.set()`
- 参照: `callout.panelId`, `lazy.ASRouterTargeting.getMessageTriggers(result.message).length`, `result.message`, `result.message.content?.tour_pref_default_value`, `result.message.content?.tour_pref_name`

## cleanup()
- 位置: L1979-1981
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callouts.delete()`

## onLocationChange()
- 位置: L1992-2016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.currentURI.spec.startsWith()`, `browser.getTabBrowser()`, `this._callouts.get()`, `this._callouts.has()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isNewtabOrHome) )` → `existingCallout.callout.endTour()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isNewtabOrHome) )` → `existingCallout.cleanup()`
- 条件付き依存: `if (!this._callouts.has(win) && isNewtabOrHome && tab.linkedPanel)` → `this.showFeatureCalloutTour()`
- 参照: `existingCallout.panelId`, `lazy.newtabPageEnabled`, `tab.linkedPanel`, `tabbrowser.documentGlobal`, `tabbrowser.selectedBrowser`, `tabbrowser.selectedTab`

## handleEvent()
- 位置: L2018-2064
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.currentURI.spec.startsWith()`, `gBrowser.getBrowserForTab()`, `this._callouts.get()`, `this._callouts.has()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isNewtabOrHome) )` → `existingCallout.callout.endTour()`
- 条件付き依存: `if ( existingCallout && (existingCallout.panelId !== tab.linkedPanel || !isNewtabOrHome) )` → `existingCallout.cleanup()`
- 条件付き依存: `if (!this._callouts.has(win) && isNewtabOrHome)` → `this.showFeatureCalloutTour()`
- 条件付き依存: `if ( existingCallout && existingCallout.panelId === tab.linkedPanel )` → `existingCallout.callout.endTour()`
- 条件付き依存: `if ( existingCallout && existingCallout.panelId === tab.linkedPanel )` → `existingCallout.cleanup()`
- 参照: `event.target`, `event.type`, `existingCallout.panelId`, `gBrowser.selectedTab`, `lazy.newtabPageEnabled`, `tab.documentGlobal`, `tab.linkedPanel`

## onBrowserWindow()
- 位置: L2066-2068
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onLocationChange()`
- 参照: `win.gBrowser.selectedBrowser`

## init()
- 位置: L2079-2101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elementIds.forEach()`, `this._elementIds.push()`
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `eventTypes.forEach()`
- 条件付き依存: `if (!this._initialized)` → `win.document.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.document.removeEventListener()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## handleEvent()
- 位置: L2103-2139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._elementIds.includes()`
- 条件付き依存: `if ( clickedElement?.id && this._elementIds.includes(clickedElement.id) )` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if (isCurrentWindow)` → `this._triggerHandler()`
- 参照: `clickedElement.id`, `clickedElement?.id`, `event.button`, `event.key`, `event.target`, `event.target.documentGlobal`, `event.type`, `this.id`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## uninit()
- 位置: L2141-2148
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._elementIds`, `this._initialized`, `this._triggerHandler`, `this.id`

## init()
- 位置: L2159-2178
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized)` → `lazy.EveryWindow.registerCallback()`
- 条件付き依存: `if (!this._initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this._initialized)` → `win.removeEventListener()`
- 条件付き依存: `if (!this._initialized)` → `this._clearVisit()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`

## uninit()
- 位置: L2180-2192
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `lazy.EveryWindow.unregisterCallback()`
- 条件付き依存: `if (this._initialized)` → `this._visits.values()`
- 条件付き依存: `if (visit.timerId !== undefined)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this._initialized)` → `this._visits.clear()`
- 参照: `this._initialized`, `this._triggerHandler`, `this.id`, `visit.timerId`

## _clearVisit()
- 位置: L2194-2200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._visits.delete()`, `this._visits.get()`
- 条件付き依存: `if (visit?.timerId !== undefined)` → `lazy.clearTimeout()`
- 参照: `visit.timerId`, `visit?.timerId`

## handleEvent()
- 位置: L2202-2253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isPrivateWindow()`
- 条件付き依存: `if (event.type === "SplitViewCreated")` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (event.type === "TabSplitViewActivate")` → `this._visits.get()`
- 条件付き依存: `if (event.type === "TabSplitViewActivate")` → `lazy.setTimeout()`
- 条件付き依存: `if (event.type === "TabSplitViewActivate")` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (event.type === "TabSplitViewActivate")` → `this._triggerHandler()`
- 条件付き依存: `if (event.type === "TabSplitViewActivate")` → `this._visits.set()`
- 条件付き依存: `if (event.type === "TabSplitViewDeactivate")` → `this._clearVisit()`
- 参照: `event.target.documentGlobal`, `event.type`, `existing?.fired`, `existing?.timerId`, `lazy.splitViewCreateCount`, `lazy.splitViewTriggerDelay`, `this._triggerHandler`, `this.id`, `visit.fired`, `visit.timerId`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.prefs`

## init()
- 位置: L2268-2270
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.initialized`

## uninit()
- 位置: L2271-2273
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.initialized`

## init()
- 位置: L2288-2290
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.initialized`

## uninit()
- 位置: L2291-2293
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.initialized`
