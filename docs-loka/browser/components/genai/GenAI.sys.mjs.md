# browser/components/genai/GenAI.sys.mjs

source: browser/components/genai/GenAI.sys.mjs
source-hash: a0df450f264c950610306bf24a637af8c6c0a9a0
lines: 1823

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `GenAI.init()`, `Object.setPrototypeOf()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`, `onChatEnabledChange()`, `onChatProviderChange()`, `onChatShortcutsChange()`

## currentChatProviderInfo()
- 位置: L269-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.chatProviders.get()`
- 参照: `lazy.chatProvider`

## canOfferChatbot()
- 位置: L284-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.sidebarTools.includes()`
- 参照: `lazy.chatEnabled`, `lazy.sidebarRevamp`

## canShowChatEntrypoint()
- 位置: L295-297
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.chatProvider`, `this.canOfferChatbot`

## canShowAIAction()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.chatShortcuts`, `this.canOfferChatbot`

## canShowSelectionMenu()
- 位置: L309-318
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.chatShortcuts`, `lazy.highlightToSearchEnabled`, `lazy.highlightToSearchFeatureGate`, `this.canShowAIAction`, `this.canShowChatEntrypoint`

## init()
- 位置: L323-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.badges.set()`, `Glean.genaiChatbot.enabled.set()`, `Glean.genaiChatbot.menu.set()`, `Glean.genaiChatbot.page.set()`, `Glean.genaiChatbot.provider.set()`, `Glean.genaiChatbot.shortcuts.set()`, `Glean.genaiChatbot.shortcutsCustom.set()`, `Glean.genaiChatbot.sidebar.set()`, `Object.entries()`, `Object.entries(feature.getVariable("prefs") ?? {}).forEach()`, `Services.prefs.getBoolPref()`, `Services.vc.compare()`, `feature.getEnrollmentMetadata()`, `feature.getVariable()`, `feature.onUpdate()`, `reorderChatProviders()`, `setPref()`, `this.getProviderId()`, `updateIgnoredInputs()`
- 条件付き依存: `if (feature.getVariable("badgeSidebar") && newEnroll)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(pref))` → `acc.push()`
- 参照: `AppConstants.MOZ_APP_VERSION_DISPLAY`, `enrollment.branch`, `enrollment.slug`, `lazy.NimbusFeatures.chatbot`, `lazy.chatEnabled`, `lazy.chatHideLocalhost`, `lazy.chatMenu`, `lazy.chatNimbus`, `lazy.chatPage`, `lazy.chatProvider`, `lazy.chatProviders`, `lazy.chatShortcuts`, `lazy.chatShortcutsCustom`, `lazy.chatShortcutsIgnoreFields`, `lazy.chatSidebar`, `this._initialized`
- XPCOM: `Services.prefs` / `Services.vc`

## setPref()
- 位置: L367-371
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (newEnroll || branch == "default")` → `lazy.PrefUtils.setPref()`

## getProviderId()
- 位置: L411-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.chatProviders.get()`
- 参照: `lazy.chatProvider`

## addAskChatItems()
- 位置: async L426-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.getContextualPrompts(context)).forEach()`, `cleanup()`, `item?.addEventListener()`, `itemAdder()`, `this.getContextualPrompts()`, `this.handleAskChat()`, `window?.gBrowser?.getTabForBrowser()`
- 参照: `browser.currentURI`, `browser.documentGlobal`, `lazy.chatProvider`, `tab.label`, `tab?.labelIsContentTitle`, `uri?.asciiHost`, `uri?.filePath`

## initializeSelectionShortcutPanel()
- 位置: L461-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiActionButton.addEventListener()`, `aiActionButton.setAttribute()`, `buildPopup()`, `chatShortcutsOptionsPanel.addEventListener()`, `document.getElementById()`, `document.l10n.setAttributes()`, `panel.querySelector()`
- 条件付き依存: `if (chatShortcutsOptionsPanel.state != "closed")` → `chatShortcutsOptionsPanel.hidePopup()`
- 参照: `aiActionButton.ariaExpanded`, `aiActionButton.ariaHasPopup`, `aiActionButton.iconSrc`, `chatShortcutsOptionsPanel.firstChild.id`, `chatShortcutsOptionsPanel.state`, `panel.hide`, `panel.initialized`, `panel.ownerDocument`, `panel.querySelector(id).iconSrc`, `panel.setSearchButtonLabel`

## truncateSelection()
- 位置: L489-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collapsed.substring()`, `collapsed[15].charCodeAt()`, `selection.replace()`, `selection.replace(/\s+/g, " ").trim()`
- 参照: `Services.locale.ellipsis`, `collapsed.length`
- XPCOM: `Services.locale`

## panel.setSearchButtonLabel()
- 位置: L503-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `truncateSelection()`
- 条件付き依存: `if (lazy.SearchService.hasSuccessfullyInitialized)` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `engine.name`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `searchActionButton.hidden`

## panel.hide()
- 位置: L533-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chatShortcutsOptionsPanel.hidePopup()`, `panel.hidePopup()`

## roundDownToNearestHundred()
- 位置: L550-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`

## createMessageBarWarning()
- 位置: L563-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `roundDownToNearestHundred()`, `this.createWarningEl()`, `this.estimateSelectionLimit()`
- 参照: `chatProvider?.maxLength`, `chatProvider?.name`, `panel.selectionData.selection.length`

## buildPopup()
- 位置: async L589-701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.shortcutsExpanded.record()`, `Glean.selectionMenu.actionClick.record()`, `addItem()`, `aiActionButton.setAttribute()`, `chatShortcutsOptionsPanel.openPopup()`, `chatShortcutsOptionsPanel.querySelector()`, `lazy.AIWindow.isAIWindowActive()`, `this.addAskChatItems()`, `this.chatProviders.get()`, `this.getProviderId()`, `this.isContextTooLong()`
- 条件付き依存: `if (showWarning)` → `vbox.appendChild()`
- 条件付き依存: `if (showWarning)` → `createMessageBarWarning()`
- 条件付き依存: `if (lazy.chatShortcutsCustom)` → `vbox.appendChild()`
- 条件付き依存: `if (lazy.chatShortcutsCustom)` → `document.createElement()`
- 条件付き依存: `if (lazy.chatShortcutsCustom)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (lazy.chatShortcutsCustom)` → `textAreaEl.addEventListener()`
- 条件付き依存: `if (lazy.chatShortcutsCustom)` → `textAreaEl.focus()`
- 条件付き依存: `if (event.key == "Enter" && !event.shiftKey)` → `this.handleAskChat()`
- 条件付き依存: `if (event.key == "Enter" && !event.shiftKey)` → `panel.hide()`
- 条件付き依存: `if (lazy.chatProvider)` → `lazy.ContentAnalysisUtils.setupContentAnalysisEventsForTextElement()`
- 条件付き依存: `if (lazy.chatProvider)` → `Services.io.newURI()`
- 条件付き依存: `if (lazy.chatShortcutsCustom)` → `chatShortcutsOptionsPanel.addEventListener()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `vbox.appendChild()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `document.createXULElement()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `addItem()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `hider.addEventListener()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!currentIsSmartWindow)` → `Glean.genaiChatbot.shortcutsHideClick.record()`
- 参照: `browser.browsingContext`, `button.textContent`, `chatProvider?.name`, `document.defaultView`, `document.documentGlobal.gBrowser.selectedBrowser`, `event.key`, `event.shiftKey`, `lazy.chatProvider`, `lazy.chatShortcutsCustom`, `panel.hide`, `panel.selectionData`, `panel.selectionData.selection`, `panel.selectionData.selection.length`, `promptObj.id`, `promptObj.label`, `textAreaEl.className`, `textAreaEl.value`, `vbox.innerHTML`
- XPCOM: `Services.io` / `Services.prefs`

## addItem()
- 位置: L605-612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.setAttribute()`, `document.createXULElement()`, `vbox.appendChild()`
- 参照: `button.className`

## resetHeight()
- 位置: L666-669
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `textAreaEl.scrollHeight`, `textAreaEl.style.height`

## hasMouseoverOnPopup()
- 位置: L704-719
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (chatShortcutsOptionsPanel.state == "closed")` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (chatShortcutsOptionsPanel.state == "closed")` → `buildPopup()`
- 参照: `chatShortcutsOptionsPanel.state`, `lazy.shortcutMouseoverCount`
- XPCOM: `Services.prefs`

## handleShortcutsMessage()
- 位置: L747-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.shortcutsDisplayed.record()`, `Glean.selectionMenu.displayed.record()`, `browser.getBoundingClientRect()`, `browser?.closest()`, `document.getElementById()`, `lazy.AIWindow.isAIWindowActive()`, `shortcutPanel.openPopup()`, `shortcutPanel.removeAttribute()`, `shortcutPanel.setSearchButtonLabel()`, `shortcutPanel.toggleAttribute()`, `this.ignoredInputs.has()`, `this.isSupportedContext()`
- 条件付き依存: `if (isSmartWindow)` → `this.initializeSelectionShortcutPanel()`
- 条件付き依存: `if (!(isSmartWindow))` → `this.initializeSelectionShortcutPanel()`
- 条件付き依存: `if (!imeHiding)` → `shortcutPanel.hide()`
- 参照: `Services.locale.isAppLocaleRTL`, `browser.documentGlobal`, `browser.getBoundingClientRect().width`, `browser.screenX`, `browser.screenY`, `data.delay`, `data.host`, `data.inputType`, `data.screenXDevPx`, `data.screenYDevPx`, `data.selection`, `data.selection.length`, `lazy.chatShortcutsSmartWindow`, `shortcutPanel.selectionData`, `this.canShowSelectionMenu`, `window.outerHeight`
- XPCOM: `Services.locale`

## isContextTooLong()
- 位置: L840-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.chatProviders.get()`, `this.estimateSelectionLimit()`
- 参照: `chatProvider?.maxLength`, `lazy.chatProvider`, `selection.length`

## createWarningEl()
- 位置: L856-870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `mozMessageBarEl.setAttribute()`
- 条件付き依存: `if (dismissable)` → `mozMessageBarEl.setAttribute()`
- 参照: `mozMessageBarEl.className`, `mozMessageBarEl.dataset.l10nAttrs`

## isSmartWindow()
- 位置: L878-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.browsingContext?.topChromeWindow`

## isSupportedContext()
- 位置: L893-904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `uri?.startsWith()`
- 参照: `browser.browsingContext?.currentURI.spec`, `browser.browsingContext?.isDocumentPiP`, `browser.documentGlobal.toolbar?.visible`

## canShowAskChat()
- 位置: L913-944
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.sidebarTools.includes()`, `this.isSmartWindow()`, `this.isSupportedContext()`
- 参照: `contextTabs?.length`, `lazy.chatMenu`, `lazy.chatPage`, `lazy.chatProvider`, `lazy.sidebarRevamp`, `selectionInfo?.text`, `this.canShowChatEntrypoint`

## buildAskChatContext()
- 位置: async L954-964
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.chatPage && !context.selection)` → `this.addPageContext()`
- 参照: `context.selection`, `lazy.chatPage`, `selectionInfo?.fullText`

## buildAskChatMenu()
- 位置: async L972-1096
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.contextmenuRemove.record()`, `addItem()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `item.hasAttribute()`, `item.setAttribute()`, `popup.appendChild()`, `removeItem.addEventListener()`, `showItem()`, `this.addAskChatItems()`, `this.buildAskChatContext()`, `this.canShowAskChat()`, `this.chatProviders.get()`, `this.getProviderId()`, `this.isSmartWindow()`
- 条件付き依存: `if (!this.canShowAskChat(browser, source, contextTabs, selectionInfo))` → `showItem()`
- 条件付き依存: `if (isSmartWindow)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (provider)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(provider))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (source !== "tool")` → `menu.menupopup?.remove()`
- 条件付き依存: `if (promptObj.badge && lazy.chatPageMenuBadge)` → `item.setAttribute()`
- 条件付き依存: `if (item.hasAttribute("badge"))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!isSmartWindow && context.contentType == "page")` → `addItem()`
- 条件付き依存: `if (!isSmartWindow && context.contentType == "page")` → `openItem.addEventListener()`
- 条件付き依存: `if (!isSmartWindow && context.contentType == "page")` → `window.SidebarController.show()`
- 条件付き依存: `if (!isSmartWindow && context.contentType == "page")` → `Glean.genaiChatbot.contextmenuChoose.record()`
- 条件付き依存: `if (!isSmartWindow && context.contentType == "page")` → `this.getProviderId()`
- 条件付き依存: `if (lazy.chatProvider)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (source === "tool")` → `lazy.SidebarManager.updateToolsPref()`
- 条件付き依存: `if (!(source === "tool"))` → `Services.prefs.setBoolPref()`
- 参照: `browser.documentGlobal`, `context.contentType`, `item.disabled`, `lazy.chatPageMenuBadge`, `lazy.chatProvider`, `menu.menupopup`, `menu.ownerDocument`, `promptObj.badge`, `promptObj.id`, `promptObj.label`, `this.chatProviders.get(lazy.chatProvider)?.name`, `this.showItem`
- XPCOM: `Services.prefs`

## addItem()
- 位置: L1012-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `menu.appendChild()`, `menu.appendItem()`

## buildTabMenu()
- 位置: async L1106-1124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buildAskChatMenu()`
- 参照: `contextTab?.linkedBrowser`

## showItem()
- 位置: L1113-1120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showItem()`
- 条件付き依存: `if (separator && separator.localName === "menuseparator")` → `this.showItem()`
- 参照: `item.nextElementSibling`, `separator.localName`

## buildTabSummarizeItem()
- 位置: async L1136-1192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.setAttribute()`, `this.addAskChatItems()`, `this.buildAskChatContext()`, `this.canShowAskChat()`, `this.showItem()`
- 条件付き依存: `if (!browser || !this.canShowAskChat(browser, "tab", contextTabs, null))` → `this.showItem()`
- 条件付き依存: `if (!summarize)` → `this.showItem()`
- 条件付き依存: `if (summarize.badge && lazy.chatPageMenuBadge)` → `item.setAttribute()`
- 条件付き依存: `if (!(summarize.badge && lazy.chatPageMenuBadge))` → `item.removeAttribute()`
- 条件付き依存: `if (!item.hasSummarizeHandler)` → `item.addEventListener()`
- 条件付き依存: `if (!item.hasSummarizeHandler)` → `this.handleAskChat()`
- 条件付き依存: `if (!item.hasSummarizeHandler)` → `item.hasAttribute()`
- 条件付き依存: `if (item.hasAttribute("badge"))` → `Services.prefs.setBoolPref()`
- 参照: `context.contentType`, `context.pageUrl`, `contextTab?.linkedBrowser`, `item.disabled`, `item.hasSummarizeHandler`, `item.summarizeContext`, `item.summarizePrompt`, `lazy.chatPageMenuBadge`, `promptObj.id`, `summarize.badge`, `summarize.label`
- XPCOM: `Services.prefs`

## showItem()
- 位置: L1200-1202
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `item.hidden`

## getContextualPrompts()
- 位置: async L1210-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await lazy.l10n.formatMessages(toFormat.map(obj => obj.l10nId))).forEach()`, `JSON.parse()`, `Object.assign()`, `Services.prefs.getChildList()`, `Services.prefs.getChildList("browser.ml.chat.prompts.").forEach()`, `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`, `console.error()`, `lazy.ASRouterTargeting.findMatchingMessage()`, `lazy.l10n.formatMessages()`, `messages.push()`, `msg?.attributes.forEach()`, `toFormat.map()`
- 条件付き依存: `if (promptObj.l10nId)` → `toFormat.push()`
- 条件付き依存: `if (promptObj.id == "summarize")` → `lazy.l10n.formatValues()`
- 参照: `attr.name`, `attr.value`, `context.contentType`, `obj.l10nId`, `promptObj.badge`, `promptObj.id`, `promptObj.l10nId`, `promptObj.label`, `promptObj.value`
- XPCOM: `Services.prefs`

## estimateSelectionLimit()
- 位置: L1276-1280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`
- 参照: `lazy.chatMaxLength`

## prepareChatPromptPrefix()
- 位置: async L1285-1316
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this.chatPromptPrefix || this.chatLastPrefix != lazy.chatPromptPrefix )` → `JSON.parse()`
- 条件付き依存: `if ( !this.chatPromptPrefix || this.chatLastPrefix != lazy.chatPromptPrefix )` → `lazy.l10n.formatMessages()`
- 条件付き依存: `if ( !this.chatPromptPrefix || this.chatLastPrefix != lazy.chatPromptPrefix )` → `this.estimateSelectionLimit()`
- 条件付き依存: `if ( !this.chatPromptPrefix || this.chatLastPrefix != lazy.chatPromptPrefix )` → `this.chatProviders.get()`
- 参照: `lazy.chatPromptPrefix`, `lazy.chatProvider`, `prefixObj.l10nId`, `this.chatLastPrefix`, `this.chatPromptPrefix`, `this.chatProviders.get(lazy.chatProvider)?.maxLength`

## buildChatPrompt()
- 位置: L1326-1383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/%pageUrl(?:\|[^%]+)?%/.test()`, `template.replace()`
- 条件付き依存: `if (value !== undefined)` → `document.createElement()`
- 条件付き依存: `if (value !== undefined)` → `lazy.parserUtils.parseFragment()`
- 条件付き依存: `if (value !== undefined)` → `Services.io.newURI()`
- 条件付き依存: `if (options)` → `sanitized.slice()`
- 条件付き依存: `if (options)` → `Number()`
- 条件付き依存: `if (value !== undefined)` → `sanitized .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace(/"/g, "&quot;") .replace()`
- 条件付き依存: `if (value !== undefined)` → `sanitized .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace()`
- 条件付き依存: `if (value !== undefined)` → `sanitized .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace()`
- 条件付き依存: `if (value !== undefined)` → `sanitized .replace(/&/g, "&amp;") .replace()`
- 条件付き依存: `if (value !== undefined)` → `sanitized .replace()`
- 参照: `Ci.nsIParserUtils.SanitizerDropForms`, `Ci.nsIParserUtils.SanitizerDropMedia`, `context.contentType`, `context.pageUrl`, `item.label`, `item.value`, `this.chatPromptPrefix`
- XPCOM: `nsIParserUtils` / `Services.io`

## getPageUrl()
- 位置: L1392-1406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ReaderMode.getOriginalUrl()`, `uri?.schemeIs()`
- 条件付き依存: `if (readerOriginalUrl)` → `Services.io.newURI()`
- 条件付き依存: `if (uri?.schemeIs("http") || uri?.schemeIs("https"))` → `Services.io.createExposableURI()`
- 参照: `Services.io.createExposableURI(uri).specIgnoringRef`, `browser?.currentURI`, `uri.spec`
- XPCOM: `Services.io`

## addPageContext()
- 位置: L1416-1420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPageUrl()`
- 参照: `context.contentType`, `context.pageUrl`

## summarizeCurrentPage()
- 位置: async L1428-1444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addAskChatItems()`, `this.addPageContext()`
- 条件付き依存: `if (promptObj.id === "summarize")` → `this.handleAskChat()`
- 参照: `context.pageUrl`, `promptObj.id`, `window.gBrowser.selectedBrowser`

## setupAutoSubmit()
- 位置: L1453-1529
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.chatSidebar)` → `ChromeUtils.generateQI()`
- 条件付き依存: `if (lazy.chatSidebar)` → `browser.webProgress?.addProgressListener()`
- 条件付き依存: `if (!(lazy.chatSidebar))` → `ChromeUtils.generateQI()`
- 条件付き依存: `if (!(lazy.chatSidebar))` → `gBrowser.addTabsProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_DOCUMENT`, `context.window.gBrowser`, `lazy.chatSidebar`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## sendAutoSubmit()
- 位置: L1454-1468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `console.error()`, `wgp?.getActor()`
- 参照: `br.browsingContext?.currentWindowGlobal`

## onStateChange()
- 位置: async L1472-1489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webProgress?.removeProgressListener()`, `sendAutoSubmit()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_DOCUMENT`, `Ci.nsIWebProgressListener.STATE_STOP`, `browser.browsingContext?.currentWindowGlobal`, `wgp.isInitialDocument`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: async L1506-1520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.removeTabsProgressListener()`, `sendAutoSubmit()`
- 参照: `location?.spec`

## handleAskChat()
- 位置: async L1537-1663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.promptClick.record()`, `Services.scriptSecurityManager.createNullPrincipal()`, `["page", "shortcuts"].includes()`, `browser.fixupAndLoadURIString()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.chatProvider?.includes()`, `this.buildChatPrompt()`, `this.chatProviders.get()`, `this.getProviderId()`, `this.prepareChatPromptPrefix()`
- 条件付き依存: `if (isPageSummarizeRequest)` → `Glean.genaiChatbot.summarizePage.record()`
- 条件付き依存: `if (isPageSummarizeRequest)` → `this.getProviderId()`
- 条件付き依存: `if (["page", "shortcuts"].includes(context.entry))` → `Glean.genaiChatbot[ context.entry == "page" ? "contextmenuPromptClick" : "shortcutsPromptClick" ].record()`
- 条件付き依存: `if (["page", "shortcuts"].includes(context.entry))` → `this.getProviderId()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActive(win))` → `lazy.AIWindowUI.isSidebarOpen()`
- 条件付き依存: `if (!lazy.AIWindowUI.isSidebarOpen(win))` → `lazy.AIWindow.getActiveConversation()`
- 条件付き依存: `if (!lazy.AIWindowUI.isSidebarOpen(win))` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActive(win))` → `lazy.AIWindowUI._getSidebarAiWindow()`
- 条件付き依存: `if (aiWindowEl)` → `aiWindowEl.submitChatMessage()`
- 条件付き依存: `if (!lazy.chatProvider)` → `SidebarController.show()`
- 条件付き依存: `if (header)` → `Cc[ "@mozilla.org/io/string-input-stream;1" ].createInstance()`
- 条件付き依存: `if (header)` → `options.headers.setByteStringData()`
- 条件付き依存: `if (header)` → `encodeURIComponent()`
- 条件付き依存: `if (!supportAutoSubmit)` → `url.searchParams.set()`
- 条件付き依存: `if (lazy.chatSidebar)` → `SidebarController.show()`
- 条件付き依存: `if (!browser)` → `console.error()`
- 条件付き依存: `if (!(lazy.chatSidebar))` → `context.window.gBrowser.addTab()`
- 条件付き依存: `if ( supportAutoSubmit || lazy.chatProvider?.includes("file_chat-autosubmit.html") )` → `this.setupAutoSubmit()`
- 参照: `Ci.nsIStringInputStream`, `Glean.genaiChatbot`, `SidebarController.browser.contentWindow.browserPromise`, `SidebarController.browser.contentWindow.onboardingPromise`, `context.contentType`, `context.entry`, `context.pageUrl`, `context.selection`, `context.selection?.length`, `context.window`, `context.window.document`, `context.window.gBrowser.addTab("", options).linkedBrowser`, `context.window?.browsingContext?.topChromeWindow`, `lazy.chatProvider`, `lazy.chatSidebar`, `options.headers`, `promptObj.id`, `promptObj.label`, `promptObj.value`
- XPCOM: [`nsIStringInputStream`](../../../xpcom/io/nsIStringStream.idl.md) / `@mozilla.org/io/string-input-stream;1` / `Services.scriptSecurityManager`

## id()
- 位置: L1665-1667
- 役割: (未記入)
- 触るとき: (未記入)

## hasDistinctEnabledState()
- 位置: L1669-1673
- 役割: (未記入)
- 触るとき: (未記入)

## isBlocked()
- 位置: L1675-1677
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.chatEnabled`

## isEnabled()
- 位置: L1679-1681
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.chatEnabled`, `lazy.chatProvider`

## isAllowed()
- 位置: L1683-1685
- 役割: (未記入)
- 触るとき: (未記入)

## canRunOnDevice()
- 位置: L1687-1690
- 役割: (未記入)
- 触るとき: (未記入)

## isManagedByPolicy()
- 位置: L1692-1698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## makeAvailable()
- 位置: async L1700-1707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## enable()
- 位置: async L1709-1714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## block()
- 位置: async L1716-1720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## onChatEnabledChange()
- 位置: L1730-1741
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!value)` → `lazy.EveryWindow.readyWindows.forEach()`
- 条件付き依存: `if ( SidebarController.isOpen && SidebarController.currentID == "viewGenaiChatSidebar" )` → `SidebarController.hide()`
- 参照: `SidebarController.currentID`, `SidebarController.isOpen`

## onChatProviderChange()
- 位置: L1748-1762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.readyWindows.forEach()`, `window.SidebarController.addOrUpdateExtension()`
- 条件付き依存: `if (value && lazy.chatEnabled && lazy.chatOpenSidebarOnProviderChange)` → `Services.wm .getMostRecentWindow("navigator:browser") ?.SidebarController.show()`
- 条件付き依存: `if (value && lazy.chatEnabled && lazy.chatOpenSidebarOnProviderChange)` → `Services.wm .getMostRecentWindow()`
- 参照: `GenAI.chatLastPrefix`, `lazy.chatEnabled`, `lazy.chatOpenSidebarOnProviderChange`
- XPCOM: `Services.wm`

## onChatShortcutsChange()
- 位置: L1769-1779
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!value)` → `lazy.EveryWindow.readyWindows.forEach()`
- 条件付き依存: `if (!value)` → `window.document.getElementById()`
- 条件付き依存: `if (!value)` → `selectionShortcutActionPanel.hidePopup()`

## reorderChatProviders()
- 位置: L1784-1809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GenAI.chatProviders.forEach()`, `GenAI.chatProviders.get()`, `GenAI.chatProviders.set()`, `[...GenAI.chatProviders].map()`, `idToKey.get()`, `lazy.chatProviders.split()`, `ordered.forEach()`, `toSet.forEach()`
- 条件付き依存: `if (!lazy.chatHideLocalhost)` → `ordered.push()`
- 条件付き依存: `if (val)` → `toSet.push()`
- 条件付き依存: `if (val)` → `GenAI.chatProviders.delete()`
- 参照: `GenAI.chatProviders`, `lazy.chatHideLocalhost`, `v.id`, `val.hidden`

## updateIgnoredInputs()
- 位置: L1814-1819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.chatShortcutsIgnoreFields.split()`, `lazy.chatShortcutsIgnoreFields.split(",").filter()`
- 参照: `GenAI.ignoredInputs`
