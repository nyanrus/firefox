# browser/base/content/nsContextMenu.sys.mjs

source: browser/base/content/nsContextMenu.sys.mjs
source-hash: af4633e94e3753ef4fd07f72c7bd4958127c4676
lines: 3102

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`, `Promise.resolve()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## nsContextMenu.constructor()
- 位置: L153-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.getElementById()`, `this.initItems()`, `this.setContext()`
- 条件付き依存: `if (!aIsShift)` → `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!aIsShift)` → `Services.obs.notifyObservers()`
- 参照: `aXulMenu.documentGlobal`, `aXulMenu.ownerDocument`, `gBrowser.getTabForBrowser`, `subject.wrappedJSObject`, `this.browser`, `this.browser.currentURI.spec`, `this.contentData`, `this.contentData.docLocation`, `this.contentData.webExtContextData`, `this.document`, `this.frameID`, `this.inFrame`, `this.isContentSelected`, `this.isTextSelected`, `this.linkTextStr`, `this.linkURI`, `this.linkURL`, `this.onAudio`, `this.onCanvas`, `this.onEditable`, `this.onImage`, `this.onLink`, `this.onPassword`, `this.onPlainTextLink`, `this.onSpellcheckable`, `this.onTextInput`, `this.onVideo`, `this.originalMediaURL`, `this.passwordRevealed`, `this.selectionInfo.docSelectionIsCollapsed`, `this.selectionInfo.fullText`, `this.shouldDisplay`, `this.timeStamp`, `this.viewFrameSourceElement`, `this.webExtBrowserType`, `this.window`
- XPCOM: `Services.obs`

## nsContextMenu.setContext()
- 位置: L222-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.get()`, `Object.create()`, `gBrowser.getTabForBrowser()`, `lazy.E10SUtils.deserializePolicyContainer()`, `this.browser.getAttribute()`, `this.getLinkURI()`
- 条件付き依存: `if (!(this.contentData))` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!(this.contentData))` → `SelectionUtils.getSelectionDetails()`
- 条件付き依存: `if (!(this.contentData))` → `this.browser.browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (context.shouldInitInlineSpellCheckerUINoChildren)` → `InlineSpellCheckerUI.initFromRemote()`
- 条件付き依存: `if (context.shouldInitInlineSpellCheckerUIWithChildren)` → `InlineSpellCheckerUI.initFromRemote()`
- 条件付き依存: `if (context.shouldInitInlineSpellCheckerUIWithChildren)` → `this.showItem()`
- 参照: `InlineSpellCheckerUI.canSpellCheck`, `context.bgImageURL`, `context.canSpellCheck`, `context.frameBrowsingContextID`, `context.frameID`, `context.frameOuterWindowID`, `context.hasBGImage`, `context.hasMultipleBGImages`, `context.hasTextFragments`, `context.imageDescURL`, `context.imageInfo`, `context.inAboutDevtoolsToolbox`, `context.inFrame`, `context.inPDFViewer`, `context.inSrcdocFrame`, `context.inSyntheticDoc`, `context.inTabBrowser`, `context.inWebExtBrowser`, `context.isDesignMode`, `context.isSponsoredLink`, `context.link`, `context.linkDownload`, `context.linkProtocol`, `context.linkTextStr`, `context.linkURL`, `context.mediaURL`, `context.onAudio`, `context.onCanvas`, `context.onCompletedImage`, `context.onDRMMedia`, `context.onEditable`, `context.onImage`, `context.onLink`, `context.onLoadedImage`, `context.onMailtoLink`, `context.onMozExtLink`, `context.onNumeric`, `context.onPassword`, `context.onPiPVideo`, `context.onSaveableLink`, `context.onSearchField`, `context.onSpellcheckable`, `context.onTelLink`, `context.onTextInput`, `context.onVideo`, `context.originalMediaURL`, `context.passwordRevealed`, `context.policyContainer`, `context.principal`, `context.shouldDisplay`, `context.shouldInitInlineSpellCheckerUINoChildren`, `context.shouldInitInlineSpellCheckerUIWithChildren`, `context.storagePrincipal`, `context.target`, `context.targetIdentifier`, `context.timeStamp`, `context.webExtBrowserType`, `gBrowser.getTabForBrowser`, `nsContextMenu.contentData`, `this.actor`, `this.actor.manager`, `this.actor.manager.domProcess.remoteType`, `this.browser`, `this.browser.documentGlobal`, `this.canSpellCheck`, `this.contentData`, `this.contentData.actor`, `this.contentData.browser`, `this.contentData.context`, `this.contentData.selectionInfo`, `this.contentData.spellInfo`, `this.contentData.spellInfo.spellSuggestions`, `this.frameBrowsingContext`, `this.frameID`, `this.frameOuterWindowID`, `this.hasBGImage`, `this.hasMultipleBGImages`, `this.hasTextFragments`, `this.imageDescURL`, `this.imageInfo`, `this.inAboutDevtoolsToolbox`, `this.inFrame`, `this.inPDFViewer`, `this.inSrcdocFrame`, `this.inSyntheticDoc`, `this.inTabBrowser`, `this.inWebExtBrowser`, `this.isDesignMode`, `this.isSponsoredLink`, `this.isTextSelected`, `this.link`, `this.linkDownload`, `this.linkProtocol`, `this.linkTextStr`, `this.linkURI`, `this.linkURL`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onCompletedImage`, `this.onDRMMedia`, `this.onEditable`, `this.onImage`, `this.onLink`, `this.onLoadedImage`, `this.onMailtoLink`, `this.onMozExtLink`, `this.onNumeric`, `this.onPassword`, `this.onPiPVideo`, `this.onSaveableLink`, `this.onSearchField`, `this.onSpellcheckable`, `this.onTelLink`, `this.onTextInput`, `this.onVideo`, `this.originalMediaURL`, `this.ownerDoc`, `this.ownerDoc.defaultView.docShell.chromeEventHandler`, `this.passwordRevealed`, `this.pdfjsContextMenu`, `this.policyContainer`, `this.principal`, `this.remoteType`, `this.selectedText`, `this.selectedText.length`, `this.selectionInfo`, `this.selectionInfo.text`, `this.shouldDisplay`, `this.spellSuggestions`, `this.storagePrincipal`, `this.target`, `this.target.ownerDocument`, `this.targetIdentifier`, `this.textFragmentURL`, `this.timeStamp`, `this.webExtBrowserType`, `this.window`

## nsContextMenu.hiding()
- 位置: L367-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.isESModuleLoaded()`, `this.#passwordItemsAbortController?.abort()`, `this.window.InlineSpellCheckerUI.clearDictionaryListFromMenu()`, `this.window.InlineSpellCheckerUI.clearSuggestionsFromMenu()`, `this.window.InlineSpellCheckerUI.uninit()`
- 条件付き依存: `if (this.actor)` → `this.actor.hiding()`
- 条件付き依存: `if ( Cu.isESModuleLoaded( "resource://gre/modules/LoginManagerContextMenu.sys.mjs" ) )` → `lazy.LoginManagerContextMenu.clearLoginsFromMenu()`
- 条件付き依存: `if (this._onPopupHiding)` → `this._onPopupHiding()`
- 参照: `aXulMenu.showHideSeparators`, `this._onPopupHiding`, `this.actor`, `this.contentData`, `this.document`

## nsContextMenu.initItems()
- 位置: L393-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.initClipboardItems()`, `this.initImageItems()`, `this.initLeaveDOMFullScreenItems()`, `this.initMediaPlayerItems()`, `this.initMiscItems()`, `this.initNavigationItems()`, `this.initOpenItems()`, `this.initPasswordControlItems()`, `this.initPasswordManagerItems()`, `this.initSaveItems()`, `this.initScreenshotItem()`, `this.initSpellingItems()`, `this.initSyncItems()`, `this.initTextFragmentItems()`, `this.initViewItems()`, `this.initViewSourceItems()`, `this.pdfjsContextMenu.initItems()`, `this.showHideSeparators()`
- 参照: `aXulMenu.showHideSeparators`

## aXulMenu.showHideSeparators()
- 位置: L417-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showHideSeparators()`

## nsContextMenu.initTextFragmentItems()
- 位置: L423-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browser.currentURI.schemeIs()`, `this.setItemAttr()`, `this.showItem()`
- 参照: `lazy.STRIP_ON_SHARE_ENABLED`, `lazy.TEXT_FRAGMENTS_ENABLED`, `this.hasTextFragments`, `this.inFrame`, `this.inPDFViewer`, `this.isContentSelected`, `this.onEditable`

## nsContextMenu.getTextDirective()
- 位置: async L448-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.getTextDirective()`
- 条件付き依存: `if (this.textFragmentURL)` → `this.setItemAttr()`
- 条件付き依存: `if (this.textFragmentURL)` → `this.getLinkURI()`
- 条件付き依存: `if (this.textFragmentURL)` → `this.#canStripParams()`
- 参照: `lazy.TEXT_FRAGMENTS_ENABLED`, `this.textFragmentURL`

## nsContextMenu.removeAllTextFragments()
- 位置: async L467-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.removeAllTextFragments()`

## nsContextMenu.copyLinkToHighlight()
- 位置: L471-480
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (stripSiteTracking)` → `this.getLinkURI()`
- 条件付き依存: `if (stripSiteTracking)` → `this.copyStrippedLink()`
- 条件付き依存: `if (!(stripSiteTracking))` → `this.copyLink()`
- 参照: `this.textFragmentURL`

## nsContextMenu.initOpenItems()
- 位置: L482-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.AIWindow.isAIWindowEnabled()`, `lazy.ContextualIdentityService.getPublicIdentities()`, `lazy.LinkPreview.shouldShowContextMenu()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.showItem()`, `window.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (this.onMailtoLink)` → `Cc[ "@mozilla.org/uriloader/external-protocol-service;1" ] .getService()`
- 条件付き依存: `if ( this.isTextSelected && !this.onLink && this.selectionInfo && this.selectionInfo.linkURL )` → `this.getLinkURI()`
- 条件付き依存: `if (this.contentData.userContextId)` → `document.getElementById()`
- 条件付き依存: `if (this.contentData.userContextId)` → `item.setAttribute()`
- 条件付き依存: `if (this.contentData.userContextId)` → `lazy.ContextualIdentityService.getUserContextLabel()`
- 条件付き依存: `if (this.contentData.userContextId)` → `document.l10n.setAttributes()`
- 参照: `Ci.nsIExternalProtocolService`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIWebHandlerApp`, `lazy.ContextualIdentityService.getPublicIdentities().length`, `lazy.PrivateBrowsingUtils.enabled`, `mailtoHandler.alwaysAskBeforeHandling`, `mailtoHandler.preferredAction`, `mailtoHandler.preferredApplicationHandler`, `this.browser`, `this.contentData.userContextId`, `this.isTextSelected`, `this.linkTextStr`, `this.linkURI`, `this.linkURL`, `this.onLink`, `this.onMailtoLink`, `this.onPlainTextLink`, `this.onSaveableLink`, `this.selectionInfo`, `this.selectionInfo.linkText`, `this.selectionInfo.linkURL`, `window.gBrowser?.getTabForBrowser(this.browser)?.hidden`, `window.gBrowser?.getTabForBrowser(this.browser)?.pinned`, `window.gBrowser?.selectedTab?.splitview`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1` / `Services.prefs`

## nsContextMenu.initNavigationItems()
- 位置: L574-643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `initBackForwardMenuItemTooltip()`, `this.showItem()`, `this.window.XULBrowserWindow.stopCommand.getAttribute()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.showItem()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.showItem()`
- 参照: `AppConstants.platform`, `this.inTabBrowser`, `this.isContentSelected`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onTextInput`, `this.onVideo`, `this.window.browsingContext.isDocumentPiP`

## initBackForwardMenuItemTooltip()
- 位置: L613-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (shortcut)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 参照: `AppConstants.platform`

## nsContextMenu.initLeaveDOMFullScreenItems()
- 位置: L645-649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showItem()`
- 参照: `this.target.ownerDocument.fullscreen`

## nsContextMenu.initSaveItems()
- 位置: L651-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `this.mediaURL.startsWith()`, `this.setItemAttr()`, `this.showItem()`
- 条件付き依存: `if ( (this.onSaveableLink || this.onPlainTextLink) && Services.policies.status === Services.policies.ACTIVE )` → `this.setItemAttr()`
- 条件付き依存: `if ( (this.onSaveableLink || this.onPlainTextLink) && Services.policies.status === Services.policies.ACTIVE )` → `lazy.WebsiteFilter.isAllowed()`
- 条件付き依存: `if ( Services.policies.status === Services.policies.ACTIVE && !Services.policies.isAllowed("filepickers") )` → `this.setItemAttr()`
- 参照: `Services.policies.ACTIVE`, `Services.policies.status`, `this.isContentSelected`, `this.linkURL`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onPlainTextLink`, `this.onSaveableLink`, `this.onTextInput`, `this.onVideo`
- XPCOM: `Services.policies`

## nsContextMenu.initImageItems()
- 位置: L719-837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IMAGE_ONLY_PROTOCOLS.includes()`, `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`, `URL.parse()`, `this.setItemAttr()`, `this.showAndFormatVisualSearchContextItem()`, `this.showItem()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE)` → `this.setItemAttr()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE)` → `Services.policies.isAllowed()`
- 条件付き依存: `if ( AppConstants.HAVE_SHELL_SERVICE && Services.policies.isAllowed("setDesktopBackground") )` → `this.window.getShellService()`
- 条件付き依存: `if (canSetDesktopBackground)` → `this.document.getElementById()`
- 参照: `AppConstants.HAVE_SHELL_SERVICE`, `Services.appinfo.isTextRecognitionSupported`, `Services.policies.ACTIVE`, `Services.policies.status`, `lazy.TEXT_RECOGNITION_ENABLED`, `mediaURL.protocol`, `shell.canSetDesktopBackground`, `this.contentData.disableSetDesktopBackground`, `this.document.getElementById("context-setDesktopBackground").disabled`, `this.hasBGImage`, `this.hasMultipleBGImages`, `this.imageDescURL`, `this.inFrame`, `this.inPDFViewer`, `this.inSyntheticDoc`, `this.isContentSelected`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onCompletedImage`, `this.onImage`, `this.onLink`, `this.onLoadedImage`, `this.onTextInput`, `this.onVideo`, `this.webExtBrowserType`
- XPCOM: `Services.appinfo` / `Services.policies` / `Services.prefs`

## nsContextMenu.initViewItems()
- 位置: L839-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.DevToolsShim.isDevToolsUser()`, `this.setItemAttr()`, `this.showItem()`
- 参照: `lazy.gPrintEnabled`, `this.inAboutDevtoolsToolbox`, `this.inFrame`, `this.inSyntheticDoc`, `this.inTabBrowser`, `this.isContentSelected`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onTextInput`, `this.onVideo`, `this.selectionInfo.isDocumentLevelSelection`, `this.window.browsingContext.isDocumentPiP`
- XPCOM: `Services.prefs`

## nsContextMenu.initMiscItems()
- 位置: L896-978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http", "https"].includes()`, `document.getElementById()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `lazy.GenAI.buildAskChatMenu()`, `this.shouldShowAddEngine()`, `this.showAndFormatSearchContextItem()`, `this.showItem()`, `this.showItem.bind()`, `this.showTranslateSelectionItem()`
- 条件付き依存: `if (this.inFrame)` → `this.setItemAttr()`
- 条件付き依存: `if (this.inFrame)` → `lazy.BrowserUtils.mimeTypeIsTextBased()`
- 参照: `lazy.AITAB_ENABLED`, `lazy.gPrintEnabled`, `this.actor.manager.browsingContext.currentWindowGlobal.osPid`, `this.browser`, `this.browser.currentURI.scheme`, `this.inFrame`, `this.inSrcdocFrame`, `this.inWebExtBrowser`, `this.isContentSelected`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onMailtoLink`, `this.onMozExtLink`, `this.onNumeric`, `this.onPlainTextLink`, `this.onTelLink`, `this.onTextInput`, `this.onVideo`, `this.selectionInfo`, `this.target.ownerDocument.contentType`, `this.viewFrameSourceElement.hidden`, `this.window`, `this.window.browsingContext.isDocumentPiP`, `window.top.gBidiUI`

## nsContextMenu.initSpellingItems()
- 位置: L980-1028
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InlineSpellCheckerUI.canUndo()`, `document .getElementById()`, `document .getElementById("spell-check-enabled") .toggleAttribute()`, `this.showItem()`
- 条件付き依存: `if (onMisspelling)` → `document.getElementById()`
- 条件付き依存: `if (onMisspelling)` → `InlineSpellCheckerUI.addSuggestionsToMenu()`
- 条件付き依存: `if (onMisspelling)` → `this.showItem()`
- 条件付き依存: `if (!(onMisspelling))` → `this.showItem()`
- 条件付き依存: `if (canSpell)` → `document.getElementById()`
- 条件付き依存: `if (canSpell)` → `InlineSpellCheckerUI.addDictionaryListToMenu()`
- 条件付き依存: `if (canSpell)` → `this.showItem()`
- 条件付き依存: `if (this.onSpellcheckable)` → `this.showItem()`
- 条件付き依存: `if (!(this.onSpellcheckable))` → `this.showItem()`
- 参照: `InlineSpellCheckerUI.canSpellCheck`, `InlineSpellCheckerUI.enabled`, `InlineSpellCheckerUI.initialSpellCheckPending`, `InlineSpellCheckerUI.overMisspelling`, `suggestionsSeparator.parentNode`, `this.canSpellCheck`, `this.onSpellcheckable`, `this.spellSuggestions`, `this.window`

## nsContextMenu.initClipboardItems()
- 位置: L1030-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sendLinkSeparator.toggleAttribute()`, `this.#canStripParams()`, `this.document.getElementById()`, `this.isSecureAboutPage()`, `this.setItemAttr()`, `this.showItem()`, `this.window.goUpdateGlobalEditMenuItems()`
- 参照: `lazy.STRIP_ON_SHARE_ENABLED`, `this.inSyntheticDoc`, `this.isContentSelected`, `this.isDesignMode`, `this.mediaURL`, `this.onAudio`, `this.onImage`, `this.onLink`, `this.onMailtoLink`, `this.onMozExtLink`, `this.onPlainTextLink`, `this.onTelLink`, `this.onTextInput`, `this.onVideo`, `this.syncItemsShown`

## nsContextMenu.initMediaPlayerItems()
- 位置: L1098-1206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.showItem()`
- 条件付き依存: `if (onMedia)` → `this.setItemAttr()`
- 条件付き依存: `if (this.onVideo)` → `this.setItemAttr()`
- 参照: `Number.POSITIVE_INFINITY`, `this.inSyntheticDoc`, `this.onAudio`, `this.onDRMMedia`, `this.onPiPVideo`, `this.onVideo`, `this.target.HAVE_CURRENT_DATA`, `this.target.NETWORK_NO_SOURCE`, `this.target.controls`, `this.target.duration`, `this.target.ended`, `this.target.error`, `this.target.loop`, `this.target.muted`, `this.target.networkState`, `this.target.ownerDocument.fullscreen`, `this.target.paused`, `this.target.playbackRate`, `this.target.readyState`
- XPCOM: `Services.prefs`

## nsContextMenu.initPasswordManagerItems()
- 位置: L1208-1290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PASSWORD_FIELDNAME_HINTS.includes()`, `Services.logins.getLoginSavingEnabled()`, `document.getElementById()`, `document.l10n.setAttributes()`, `lazy.LoginHelper.getLoginOrigin()`, `this.isLoginForm()`, `this.setItemAttr()`, `this.showItem()`, `this.updatePasswordManagerSubMenuItems()`
- 参照: `Services.logins.isLoggedIn`, `documentURI?.spec`, `lazy.LoginHelper.generationAvailable`, `lazy.LoginHelper.generationEnabled`, `loginFillInfo.activeField.fieldNameHint`, `loginFillInfo?.activeField.disabled`, `loginFillInfo?.passwordField.disabled`, `this.#passwordItemsAbortController`, `this.#passwordItemsAbortController.signal`, `this.#passwordItemsReady`, `this.contentData?.context.showRelay`, `this.contentData?.documentURIObject`, `this.contentData?.loginFillInfo`
- XPCOM: `Services.logins`

## nsContextMenu.passwordItemsReady()
- 位置: L1299-1301
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#passwordItemsReady`

## nsContextMenu.updatePasswordManagerSubMenuItems()
- 位置: async L1311-1330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `lazy.LoginManagerContextMenu.addLoginsToMenu()`, `popup.appendChild()`, `this.setItemAttr()`, `this.showItem()`
- 参照: `signal.aborted`, `this.browser`, `this.targetIdentifier`

## nsContextMenu.initSyncItems()
- 位置: L1332-1334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.gSync.updateContentContextMenu()`
- 参照: `this.syncItemsShown`

## nsContextMenu.initViewSourceItems()
- 位置: L1336-1372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `showViewSourceItem()`, `this.browser.browsingContext.currentWindowGlobal?.documentURI?.schemeIs()`
- XPCOM: `Services.prefs`

## getString()
- 位置: L1337-1342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bundle.GetStringFromName()`, `this.window.gViewSourceUtils.getPageActor()`
- 参照: `this.browser`

## showViewSourceItem()
- 位置: L1343-1358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `check()`, `getString()`, `this.setItemAttr()`, `this.showItem()`
- 条件付き依存: `if (accesskey)` → `this.setItemAttr()`
- 条件付き依存: `if (accesskey)` → `getString()`

## nsContextMenu.showHideSeparators()
- 位置: L1377-1415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menuItem.hasAttribute()`
- 条件付き依存: `if (menuItem.localName == "menuseparator")` → `menuItem.hasAttribute()`
- 条件付き依存: `if (menuItem.localName == "menu" && menuItem.menupopup)` → `this.showHideSeparators()`
- 条件付き依存: `if (menuItem.localName == "menugroup")` → `this.showHideSeparators()`
- 参照: `aPopup.children`, `lastVisibleSeparator.hidden`, `menuItem.hidden`, `menuItem.localName`, `menuItem.menupopup`

## nsContextMenu.shouldShowTakeScreenshot()
- 位置: L1417-1429
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ScreenshotsUtils.screenshotsEnabled`, `this.inTabBrowser`, `this.onAudio`, `this.onEditable`, `this.onLink`, `this.onPassword`, `this.onPlainTextLink`, `this.onTextInput`

## nsContextMenu.initScreenshotItem()
- 位置: L1431-1442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.document.documentElement.hasAttribute()`, `this.shouldShowTakeScreenshot()`, `this.showItem()`
- XPCOM: `Services.prefs`

## nsContextMenu.initPasswordControlItems()
- 位置: L1444-1454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `this.showItem()`
- 条件付き依存: `if (shouldShow)` → `this.document.getElementById()`
- 条件付き依存: `if (shouldShow)` → `revealPassword.toggleAttribute()`
- 参照: `this.onPassword`, `this.passwordRevealed`
- XPCOM: `Services.policies`

## nsContextMenu.toggleRevealPassword()
- 位置: L1456-1458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.toggleRevealPassword()`
- 参照: `this.targetIdentifier`

## nsContextMenu.openPasswordManager()
- 位置: L1460-1464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.openPasswordManager()`
- 参照: `this.window`

## nsContextMenu.useRelayMask()
- 位置: L1466-1470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.getLoginOrigin()`, `this.actor.useRelayMask()`
- 参照: `documentURI?.spec`, `this.contentData?.documentURIObject`, `this.targetIdentifier`

## nsContextMenu.useGeneratedPassword()
- 位置: L1472-1474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginManagerContextMenu.useGeneratedPassword()`
- 参照: `this.targetIdentifier`

## nsContextMenu.isLoginForm()
- 位置: L1476-1488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `documentURI?.schemeIs()`
- 参照: `loginFillInfo?.activeField.fieldNameHint`, `loginFillInfo?.passwordField?.found`, `this.browser.contentPrincipal.spec`, `this.contentData?.documentURIObject`, `this.contentData?.loginFillInfo`

## nsContextMenu.inspectNode()
- 位置: L1490-1495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DevToolsShim.inspectNode()`
- 参照: `this.targetIdentifier`, `this.window.gBrowser.selectedTab`

## nsContextMenu.inspectA11Y()
- 位置: L1497-1502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DevToolsShim.inspectA11Y()`
- 参照: `this.targetIdentifier`, `this.window.gBrowser.selectedTab`

## nsContextMenu._openLinkInParameters()
- 位置: L1504-1539
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.ReferrerInfo`, `params.referrerInfo`, `params.userContextId`, `referrerInfo.originalReferrer`, `referrerInfo.referrerPolicy`, `this.contentData.charSet`, `this.contentData.frameID`, `this.contentData.linkReferrerInfo`, `this.contentData.referrerInfo`, `this.contentData.userContextId`, `this.onLink`, `this.onPlainTextLink`, `this.policyContainer`, `this.principal`, `this.remoteType`, `this.storagePrincipal`

## nsContextMenu._getGlobalHistoryOptions()
- 位置: L1541-1563
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(this.isSponsoredLink))` → `this.browser.hasAttribute()`
- 条件付き依存: `if (this.browser.hasAttribute("triggeringSponsoredURL"))` → `this.browser.getAttribute()`
- 参照: `this.isSponsoredLink`, `this.linkURL`

## nsContextMenu.openLink()
- 位置: L1566-1574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInPrivateWindow()
- 位置: L1577-1583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInSmartWindow()
- 位置: L1586-1593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInTab()
- 位置: L1596-1608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `parseInt()`, `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInSplitView()
- 位置: L1611-1631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `win.gBrowser.getTabForBrowser()`, `win.openLinkIn()`
- 参照: `currentTab.userContextId`, `this.browser`, `this.linkURL`, `this.window`

## resolveOnNewTabCreated()
- 位置: L1619-1627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (linkTab && currentTab)` → `win.gBrowser.addTabSplitView()`
- 参照: `win.gBrowser.selectedTab`

## nsContextMenu.openLinkInCurrent()
- 位置: L1634-1640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openFrameInTab()
- 位置: L1643-1650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.openLinkIn()`
- 参照: `this.browser.contentPrincipal`, `this.browser.policyContainer`, `this.contentData.charSet`, `this.contentData.docLocation`, `this.contentData.frameReferrerInfo`

## nsContextMenu.reloadFrame()
- 位置: L1653-1656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.reloadFrame()`
- 参照: `aEvent.shiftKey`, `this.targetIdentifier`

## nsContextMenu.openFrame()
- 位置: L1659-1666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.openLinkIn()`
- 参照: `this.browser.contentPrincipal`, `this.browser.policyContainer`, `this.contentData.charSet`, `this.contentData.docLocation`, `this.contentData.frameReferrerInfo`

## nsContextMenu.showOnlyThisFrame()
- 位置: L1669-1679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.openWebLinkIn()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.browser.contentPrincipal`, `this.contentData.docLocation`, `this.contentData.frameReferrerInfo`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.takeScreenshot()
- 位置: L1681-1687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `this.window`
- XPCOM: `Services.obs`

## nsContextMenu.useMiniWindow()
- 位置: L1689-1693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ScreenshotsUtils.toggle()`
- 参照: `lazy.SELECTION_MODES.MINI_WINDOW`, `this.browser`

## nsContextMenu.viewPartialSource()
- 位置: L1696-1733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.gViewSourceUtils.viewPartialSourceInBrowser()`
- 参照: `this.actor.browsingContext`

## openSelectionFn()
- 位置: async L1698-1727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `tabBrowser.addTab()`, `tabBrowser.getBrowserForTab()`
- 条件付き依存: `if (!tabBrowser || !tabBrowser.addTab || !this.window.toolbar.visible)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!tabBrowser || !tabBrowser.addTab || !this.window.toolbar.visible)` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (inNewWindow)` → `tabBrowser.hideTab()`
- 条件付き依存: `if (inNewWindow)` → `tabBrowser.replaceTabsWithWindow()`
- 参照: `browserWindow.gBrowser`, `tabBrowser.addTab`, `tabBrowser?.selectedBrowser`, `this.window.gBrowser`, `this.window.toolbar.visible`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## nsContextMenu.viewFrameSource()
- 位置: L1736-1742
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.BrowserCommands.viewSourceOfDocument()`
- 参照: `this.browser`, `this.contentData.docLocation`, `this.frameOuterWindowID`

## nsContextMenu.viewInfo()
- 位置: L1744-1752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.BrowserCommands.pageInfo()`
- 参照: `this.browser`, `this.contentData.docLocation`

## nsContextMenu.viewImageInfo()
- 位置: L1754-1762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.BrowserCommands.pageInfo()`
- 参照: `this.browser`, `this.contentData.docLocation`, `this.imageInfo`

## nsContextMenu.viewImageDesc()
- 位置: L1764-1776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.openUILink()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.contentData.referrerInfo`, `this.imageDescURL`, `this.policyContainer`, `this.principal`, `this.remoteType`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.viewFrameInfo()
- 位置: L1778-1786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.BrowserCommands.pageInfo()`
- 参照: `this.actor.browsingContext`, `this.browser`, `this.contentData.docLocation`

## nsContextMenu.reloadImage()
- 位置: L1788-1795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.reloadImage()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.mediaURL`, `this.principal`, `this.targetIdentifier`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.#canvasToBlobURL()
- 位置: async L1797-1805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.isBlobURLValid()`, `this.actor.canvasToBlobURL()`
- 参照: `this.principal`

## nsContextMenu.copyCanvasImage()
- 位置: L1807-1814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blob.arrayBuffer()`, `lazy.BrowserUtils.copyImageToClipboard()`, `this.actor .canvasToBlob()`, `this.actor .canvasToBlob(this.targetIdentifier) .then()`, `this.actor .canvasToBlob(this.targetIdentifier) .then(blob => blob.arrayBuffer()) .then()`
- 参照: `console.error`, `this.targetIdentifier`

## nsContextMenu.viewMedia()
- 位置: L1817-1850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL(this.targetIdentifier).then()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL()`
- 条件付き依存: `if (this.onCanvas)` → `this.window.openLinkIn()`
- 条件付き依存: `if (!(this.onCanvas))` → `ALLOWED_CHROME_IMAGE_URLS.has()`
- 条件付き依存: `if (!(this.onCanvas))` → `this.window.urlSecurityCheck()`
- 条件付き依存: `if (!(this.onCanvas))` → `this.window.openLinkIn()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `console.error`, `this.contentData.referrerInfo`, `this.mediaURL`, `this.onCanvas`, `this.policyContainer`, `this.principal`, `this.remoteType`, `this.targetIdentifier`
- XPCOM: `nsIScriptSecurityManager` / `Services.scriptSecurityManager`

## nsContextMenu.saveVideoFrameAsImage()
- 位置: L1852-1894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `this.actor.saveVideoFrameAsImage()`, `this.actor.saveVideoFrameAsImage(this.targetIdentifier).then()`, `this.window.internalSave()`
- 条件付き依存: `if (this.mediaURL)` → `this.window.makeURI()`
- 条件付き依存: `if (this.mediaURL)` → `uri.QueryInterface()`
- 条件付き依存: `if (url.fileBaseName)` → `decodeURI()`
- 参照: `Ci.nsIURL`, `this.browser`, `this.contentData.cookieJarSettings`, `this.contentData.referrerInfo`, `this.mediaURL`, `this.principal`, `this.targetIdentifier`, `url.fileBaseName`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md)

## nsContextMenu.leaveDOMFullScreen()
- 位置: L1896-1898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.exitFullscreen()`

## nsContextMenu.viewBGImage()
- 位置: L1901-1915
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.openUILink()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.bgImageURL`, `this.contentData.referrerInfo`, `this.policyContainer`, `this.principal`, `this.remoteType`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.setDesktopBackground()
- 位置: L1917-1968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `this.actor .setAsDesktopBackground()`, `this.actor .setAsDesktopBackground(this.targetIdentifier) .then()`, `this.document.createElementNS()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (dbWin)` → `dbWin.gSetBackground.init()`
- 条件付き依存: `if (dbWin)` → `dbWin.focus()`
- 条件付き依存: `if (!(dbWin))` → `this.window.openDialog()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.window.openDialog()`
- 参照: `AppConstants.platform`, `image.src`, `this.targetIdentifier`
- XPCOM: `Services.policies` / `Services.wm`

## nsContextMenu.saveFrame()
- 位置: L1971-1973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.saveBrowser()`
- 参照: `this.browser`, `this.frameBrowsingContext`

## nsContextMenu.saveHelper()
- 位置: L1977-2174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `Services.prefs.getIntPref()`, `channel.asyncOpen()`, `lazy.NetUtil.newChannel()`, `this.window.makeURI()`, `timer.initWithCallback()`
- 条件付き依存: `if (channel instanceof Ci.nsIPrivateBrowsingChannel)` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (channel instanceof Ci.nsIPrivateBrowsingChannel)` → `channel.setPrivate()`
- 参照: `Ci.nsICachingChannel`, `Ci.nsICachingChannel.LOAD_BYPASS_LOCAL_CACHE_IF_BUSY`, `Ci.nsIChannel.LOAD_CALL_CONTENT_SNIFFERS`, `Ci.nsIContentPolicy.TYPE_SAVEAS_DOWNLOAD`, `Ci.nsIHttpChannel`, `Ci.nsIHttpChannelInternal`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_INHERITS_SEC_CONTEXT`, `Ci.nsIPrivateBrowsingChannel`, `Ci.nsIRequest.LOAD_BYPASS_CACHE`, `Ci.nsITimer`, `callbacks.prototype`, `channel.contentDispositionFilename`, `channel.forceAllowThirdPartyCookie`, `channel.loadFlags`, `channel.loadInfo.cookieJarSettings`, `channel.notificationCallbacks`, `channel.referrerInfo`, `saveAsListener.prototype`, `this.browser`, `this.principal`, `this.window`, `timer.TYPE_ONE_SHOT`, `timerCallback.prototype`
- XPCOM: [`nsICachingChannel`](../../../netwerk/base/nsICachingChannel.idl.md) / [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / [`nsIHttpChannelInternal`](../../../netwerk/protocol/http/nsIHttpChannelInternal.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIPrivateBrowsingChannel`](../../../netwerk/base/nsIPrivateBrowsingChannel.idl.md) / [`nsIRequest`](../../../docshell/base/nsIDocShell.idl.md) / [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1` / `Services.prefs`

## saveAsListener()
- 位置: L1993-1996
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._triggeringPrincipal`, `this._window`

## saveLinkAs_onStartRequest()
- 位置: L2000-2055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/external-helper-app-service;1" ].getService()`, `Components.isSuccessCode()`, `aRequest.QueryInterface()`, `extHelperAppSvc.doContent()`, `this.extListener.onStartRequest()`, `timer.cancel()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `aRequest.QueryInterface()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `channel.QueryInterface()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `properties.getProperty()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `l10n.formatValueSync()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `WebExtensionPolicy.getByID()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `l10n.formatValueSync()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `Services.wm.getOuterWindowWithId()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `Services.prompt.alert()`
- 参照: `Ci.nsIChannel`, `Ci.nsIExternalHelperAppService`, `Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST`, `Ci.nsIPropertyBag`, `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`, `WebExtensionPolicy.getByID(id).name`, `aRequest.status`, `channel.contentType`, `channel.loadInfo.requestBlockingReason`, `this._window`, `this.extListener`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIExternalHelperAppService`](../../../uriloader/exthandler/nsIExternalHelperAppService.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIPropertyBag`](../../../toolkit/components/passwordmgr/nsILoginManager.idl.md) / `@mozilla.org/uriloader/external-helper-app-service;1` / `Services.prompt` / `Services.wm`

## saveLinkAs_onStopRequest()
- 位置: L2057-2078
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aStatusCode == Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT)` → `this._window.saveURL()`
- 条件付き依存: `if (this.extListener)` → `this.extListener.onStopRequest()`
- 参照: `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`, `this._triggeringPrincipal`, `this.extListener`

## saveLinkAs_onDataAvailable()
- 位置: L2080-2092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extListener.onDataAvailable()`

## callbacks()
- 位置: L2095-2095
- 役割: (未記入)
- 触るとき: (未記入)

## sLA_callbacks_getInterface()
- 位置: L2097-2108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.Exception()`, `aIID.equals()`
- 条件付き依存: `if (aIID.equals(Ci.nsIAuthPrompt) || aIID.equals(Ci.nsIAuthPrompt2))` → `timer.cancel()`
- 条件付き依存: `if (aIID.equals(Ci.nsIAuthPrompt) || aIID.equals(Ci.nsIAuthPrompt2))` → `channel.cancel()`
- 参照: `Ci.nsIAuthPrompt`, `Ci.nsIAuthPrompt2`, `Cr.NS_ERROR_NO_INTERFACE`, `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`
- XPCOM: [`nsIAuthPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIAuthPrompt2`](../../../netwerk/base/nsIAuthPrompt2.idl.md)

## timerCallback()
- 位置: L2114-2114
- 役割: (未記入)
- 触るとき: (未記入)

## sLA_timer_notify()
- 位置: L2116-2118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `channel.cancel()`
- 参照: `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`

## nsContextMenu.saveLink()
- 位置: L2177-2195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `this.saveHelper()`
- 参照: `this.browser`, `this.contentData.cookieJarSettings`, `this.contentData.linkReferrerInfo`, `this.contentData.referrerInfo`, `this.frameOuterWindowID`, `this.linkDownload`, `this.linkTextStr`, `this.linkURL`, `this.onLink`, `this.ownerDoc`

## nsContextMenu.saveImage()
- 位置: L2198-2202
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.onCanvas || this.onImage)` → `this.saveMedia()`
- 参照: `this.onCanvas`, `this.onImage`

## nsContextMenu.saveMedia()
- 位置: L2205-2281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL(this.targetIdentifier).then()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL()`
- 条件付き依存: `if (this.onCanvas)` → `this.window.internalSave()`
- 条件付き依存: `if (this.onImage)` → `ALLOWED_CHROME_IMAGE_URLS.has()`
- 条件付き依存: `if (this.onImage)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this.onImage)` → `this.window.urlSecurityCheck()`
- 条件付き依存: `if (this.onImage)` → `this.window.internalSave()`
- 条件付き依存: `if (this.onVideo || this.onAudio)` → `this.mediaURL.startsWith()`
- 条件付き依存: `if (this.mediaURL.startsWith("data"))` → `this.window.ContentAreaUtils.stringBundle.GetStringFromName()`
- 条件付き依存: `if (this.onVideo || this.onAudio)` → `this.saveHelper()`
- 参照: `console.error`, `this.browser`, `this.contentData.contentDisposition`, `this.contentData.contentType`, `this.contentData.cookieJarSettings`, `this.contentData.referrerInfo`, `this.document.nodePrincipal`, `this.frameOuterWindowID`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onVideo`, `this.ownerDoc`, `this.principal`, `this.targetIdentifier`
- XPCOM: `Services.scriptSecurityManager`

## nsContextMenu.sendImage()
- 位置: L2284-2288
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.onCanvas || this.onImage)` → `this.sendMedia()`
- 参照: `this.onCanvas`, `this.onImage`

## nsContextMenu.sendMedia()
- 位置: L2290-2292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.MailIntegration.sendMessage()`
- 参照: `this.mediaURL`

## nsContextMenu.copyEmail()
- 位置: L2295-2318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.textToSubURI.unEscapeURIForUI()`, `lazy.clipboard.copyString()`, `url.indexOf()`, `url.substr()`, `url.substring()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURL`
- XPCOM: `Services.textToSubURI`

## nsContextMenu.copyPhone()
- 位置: L2321-2338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.textToSubURI.unEscapeURIForUI()`, `lazy.clipboard.copyString()`, `url.substr()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURL`
- XPCOM: `Services.textToSubURI`

## nsContextMenu.copyLink()
- 位置: L2340-2347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clipboard.copyString()`, `url.replace()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURL`

## nsContextMenu.previewLink()
- 位置: L2349-2353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LinkPreview.handleContextMenuClick()`, `url.replace()`
- 参照: `this.linkURL`

## nsContextMenu.copyStrippedLink()
- 位置: L2360-2370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.createExposableURI()`, `this.getStrippedLink()`
- 条件付き依存: `if (strippedLinkURL)` → `lazy.clipboard.copyString()`
- 参照: `Services.io.createExposableURI(strippedLinkURI)?.displaySpec`, `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURI`
- XPCOM: `Services.io`

## nsContextMenu.addSearchFieldAsEngine()
- 位置: async L2372-2405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `formData.values()`, `this.actor.getSearchFieldEngineData()`, `this.window.gDialogBox.open()`
- 条件付き依存: `if (engineInfo)` → `lazy.SearchService.addUserEngine()`
- 条件付き依存: `if (engineInfo)` → `this.window.gURLBar.search()`
- 参照: `Services.io.newURI(url).host`, `engineInfo.alias`, `engineInfo.name`, `this.targetIdentifier`
- XPCOM: `Services.io`

## nsContextMenu.showItem()
- 位置: L2419-2427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.getElementById()`
- 参照: `aItemOrId.constructor`, `item.hidden`

## nsContextMenu.setItemAttr()
- 位置: L2432-2453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elem.setAttribute()`, `this.document.getElementById()`
- 条件付き依存: `if (aVal == null)` → `elem.removeAttribute()`
- 条件付き依存: `if (aVal)` → `elem.setAttribute()`
- 条件付き依存: `if (!(aVal))` → `elem.removeAttribute()`

## nsContextMenu.cloneNode()
- 位置: L2456-2469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `attrs.item()`, `node.setAttribute()`, `this.document.createElement()`
- 参照: `aItem.attributes`, `aItem.tagName`, `attr.nodeName`, `attr.nodeValue`, `attrs.length`

## nsContextMenu.getLinkURI()
- 位置: L2471-2479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.makeURI()`
- 参照: `this.linkURL`

## nsContextMenu.getStrippedLink()
- 位置: L2487-2502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `lazy.QueryStringStripper.stripForCopyOrShare()`
- 参照: `e.message`, `this.linkURI`

## nsContextMenu.#canStripParams()
- 位置: L2509-2519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `lazy.QueryStringStripper.canStripForShare()`
- 参照: `this.linkURI`

## nsContextMenu.isSecureAboutPage()
- 位置: L2526-2536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `currentURI?.schemeIs()`
- 条件付き依存: `if (currentURI?.schemeIs("about"))` → `lazy.E10SUtils.getAboutModule()`
- 条件付き依存: `if (module)` → `module.getURIFlags()`
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `this.browser`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md)

## nsContextMenu.linkText()
- 位置: L2539-2541
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.linkTextStr`

## nsContextMenu.shouldShowSeparator()
- 位置: L2546-2558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.getElementById()`
- 参照: `separator.previousSibling`, `sibling.hidden`, `sibling.localName`, `sibling.previousSibling`

## nsContextMenu.shouldShowAddEngine()
- 位置: L2560-2570
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `this.isLoginForm()`, `uri.schemeIs()`
- 参照: `this.browser.currentURI`, `this.onSearchField`, `this.onTextInput`
- XPCOM: `Services.policies`

## nsContextMenu.addDictionaries()
- 位置: L2572-2595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.urlFormatter.formatURLPref()`, `escape()`, `this.window.openTrustedLinkIn()`, `uri.replace()`, `uri.replace(/%LOCALE%/, escape(locale)).replace()`
- 参照: `Services.appinfo.version`, `Services.locale.acceptLanguages`
- XPCOM: `Services.appinfo` / `Services.locale` / `Services.prefs` / `Services.urlFormatter`

## nsContextMenu.bookmarkThisPage()
- 位置: L2597-2599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.top.PlacesCommandHook.bookmarkPage()`, `this.window.top.PlacesCommandHook.bookmarkPage().catch()`
- 参照: `console.error`

## nsContextMenu.bookmarkLink()
- 位置: L2601-2606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.top.PlacesCommandHook.bookmarkLink()`, `this.window.top.PlacesCommandHook.bookmarkLink( this.linkURL, this.linkTextStr ).catch()`
- 参照: `console.error`, `this.linkTextStr`, `this.linkURL`

## nsContextMenu.addBookmarkForFrame()
- 位置: L2608-2616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.getFrameTitle()`, `this.actor.getFrameTitle(this.targetIdentifier).then()`, `this.window.top.PlacesCommandHook.bookmarkLink()`, `this.window.top.PlacesCommandHook.bookmarkLink(uri.spec, title).catch()`
- 参照: `console.error`, `this.contentData.documentURIObject`, `this.targetIdentifier`, `uri.spec`

## nsContextMenu.savePageAs()
- 位置: L2618-2620
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.saveBrowser()`
- 参照: `this.browser`

## nsContextMenu.printFrame()
- 位置: L2622-2626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.PrintUtils.startPrintWindow()`
- 参照: `this.actor.browsingContext`

## nsContextMenu.printSelection()
- 位置: L2628-2632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.PrintUtils.startPrintWindow()`
- 参照: `this.actor.browsingContext`

## nsContextMenu.switchPageDirection()
- 位置: L2634-2641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.gBrowser.selectedBrowser.sendMessageToActor()`

## nsContextMenu.mediaCommand()
- 位置: L2643-2645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actor.mediaCommand()`
- 参照: `this.targetIdentifier`

## nsContextMenu.copyMediaLocation()
- 位置: L2647-2652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clipboard.copyString()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.originalMediaURL`

## nsContextMenu.getImageText()
- 位置: L2654-2669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.textRecognition.apiPerformance.start()`, `dialog.resizeVertically()`, `dialogBox.open()`, `this.actor.getImageText()`, `this.window.gBrowser.getTabDialogBox()`
- 参照: `Services.prompt.MODAL_TYPE_CONTENT`, `this.browser`, `this.targetIdentifier`, `this.window.openLinkIn`
- XPCOM: `Services.prompt`

## nsContextMenu.drmLearnMore()
- 位置: L2671-2682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.BrowserUtils.whereToOpenLink()`, `this.window.openTrustedLinkIn()`
- XPCOM: `Services.urlFormatter`

## nsContextMenu.createAITab()
- 位置: L2684-2686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.createAITab()`
- 参照: `this.browser.currentURI.spec`, `this.window`

## nsContextMenu.openSelectTranslationsPanel()
- 位置: L2693-2705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getTextToTranslate()`, `this.window.SelectTranslationsPanel.open()`
- 参照: `console.error`, `context.screenXDevPx`, `context.screenYDevPx`, `this.#translationsLangPairPromise`, `this.contentData.context`, `this.isTextSelected`, `this.window.devicePixelRatio`

## nsContextMenu.localizeTranslateSelectionItem()
- 位置: async L2716-2766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.l10n.setAttributes()`, `translateSelectionItem.removeAttribute()`
- 条件付き依存: `if (targetLanguage)` → `lazy.TranslationsUtils.langTagsMatch()`
- 条件付き依存: `if ( lazy.TranslationsUtils.langTagsMatch(sourceLanguage, targetLanguage) )` → `translateSelectionItem.removeAttribute()`
- 条件付き依存: `if ( lazy.TranslationsUtils.langTagsMatch(sourceLanguage, targetLanguage) )` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (targetLanguage)` → `lazy.TranslationsParent.createLanguageDisplayNames()`
- 条件付き依存: `if (targetLanguage)` → `languageDisplayNames.of()`
- 条件付き依存: `if (displayName)` → `translateSelectionItem.setAttribute()`
- 条件付き依存: `if (displayName)` → `this.document.l10n.setAttributes()`
- 参照: `this.#translationsLangPairPromise`, `this.isTextSelected`

## nsContextMenu.#getTextToTranslate()
- 位置: L2773-2792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.canParse()`, `this.linkTextStr.trim()`
- 条件付き依存: `if (this.isTextSelected)` → `this.selectionInfo.fullText.trim()`
- 参照: `this.isTextSelected`

## nsContextMenu.showTranslateSelectionItem()
- 位置: L2797-2824
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.TranslationsParent.getIsTranslationsEngineSupported()`, `this.#getTextToTranslate()`, `this.document.getElementById()`, `this.localizeTranslateSelectionItem()`, `this.window.SelectTranslationsPanel.getLangPairPromise()`
- 条件付き依存: `if (translateSelectionItem.hidden)` → `translateSelectionItem.removeAttribute()`
- 参照: `lazy.TranslationsParent.AIFeature.isEnabled`, `textToTranslate.length`, `this.#translationsLangPairPromise`, `translateSelectionItem.hidden`
- XPCOM: `Services.prefs`

## nsContextMenu.showAndFormatSearchContextItem()
- 位置: L2827-2915
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `frameSeparator.toggleAttribute()`, `this.#updateSearchMenuitem()`
- 条件付き依存: `if (selectedText.length > 15)` → `selectedText[15].charCodeAt()`
- 条件付き依存: `if (selectedText.length > 15)` → `selectedText.substr()`
- 条件付き依存: `if (!menuItem.hidden)` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (!menuItem.hidden)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!menuItem.hidden)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (otherEngine)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!(otherEngine))` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!menuItemPrivate.hidden)` → `gNavigatorBundle.getString()`
- 参照: `Services.locale.ellipsis`, `lazy.SearchService.defaultEngine.name`, `lazy.SearchService.defaultPrivateEngine.name`, `lazy.SearchUtils.URL_TYPE.SEARCH`, `menuItem.accessKey`, `menuItem.hidden`, `menuItem.label`, `menuItemPrivate.accessKey`, `menuItemPrivate.hidden`, `menuItemPrivate.label`, `selectedText.length`, `this.browser`, `this.inFrame`, `this.isTextSelected`, `this.linkTextStr`, `this.onImage`, `this.onLink`, `this.selectedText`, `this.window`
- XPCOM: `Services.locale`

## nsContextMenu.#updateSearchMenuitem()
- 位置: L2917-2975
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `engine?.supportsResponseType()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (!menuitem.hidden)` → `engine.getURLOfType()`
- 条件付き依存: `if (!menuitem.hidden)` → `url.acceptedContentTypes.includes()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `menuitem.engine`, `menuitem.hidden`, `menuitem.policyContainer`, `menuitem.principal`, `menuitem.searchTerms`, `menuitem.usePrivate`, `this.browser`, `this.contentData.contentType`, `this.contentData?.contentType`, `this.inAboutDevtoolsToolbox`, `this.policyContainer`, `this.principal`, `url?.acceptedContentTypes`
- XPCOM: `Services.prefs`

## nsContextMenu.showAndFormatVisualSearchContextItem()
- 位置: L2981-3028
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateSearchMenuitem()`, `this.contentData.contentDisposition?.startsWith()`, `this.imageInfo.currentSrc.startsWith()`, `this.window.document.getElementById()`
- 条件付き依存: `if (!menuitem.hidden)` → `lazy.NimbusFeatures.search.recordExposureEvent()`
- 条件付き依存: `if (!menuitem.hidden)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!menuitem.hidden)` → `menuitem.engine.getURLOfType()`
- 条件付き依存: `if (!menuitem.hidden)` → `this.window.document.l10n.setAttributes()`
- 条件付き依存: `if (!menuitem.hidden)` → `this.#setNewFeatureBadge()`
- 条件付き依存: `if (!menuitem.hidden)` → `visualSearchUrl.isNew()`
- 条件付き依存: `if (!menuitem.hidden)` → `lazy.BrowserSearchTelemetry.recordSapImpression()`
- 参照: `lazy.SearchUtils.URL_TYPE.VISUAL_SEARCH`, `menuitem.engine`, `menuitem.engine.name`, `menuitem.hidden`, `this.browser`, `this.imageInfo?.currentSrc`, `this.onImage`, `visualSearchUrl.displayName`
- XPCOM: `Services.prefs`

## nsContextMenu.loadSearch()
- 位置: L3043-3056
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchUIUtils.loadSearchFromContext()`
- 参照: `event.target`, `this.window`

## nsContextMenu.createContainerMenu()
- 位置: L3058-3065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.createUserContextMenu()`
- 参照: `this.contentData.userContextId`

## nsContextMenu.#setNewFeatureBadge()
- 位置: async L3080-3100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menuitem.classList.toggle()`, `this.window.document.l10n.formatValue()`
- 条件付き依存: `if (!shouldShow)` → `menuitem.removeAttribute()`
- 条件付き依存: `if (this.#newFeatureBadgeL10nString)` → `menuitem.setAttribute()`
- 条件付き依存: `if (value)` → `this.#setNewFeatureBadge()`
- 参照: `this.#newFeatureBadgeL10nString`
