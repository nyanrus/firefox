# browser/components/customizableui/CustomizeMode.sys.mjs

source: browser/components/customizableui/CustomizeMode.sys.mjs
source-hash: 0226177206cf5a7940a756ba33c3de2e374545fd
lines: 4017

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyServiceGetter()`

## closeGlobalTab()
- 位置: L62-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.removeTab()`
- 条件付き依存: `if (win.gBrowser.browsers.length == 1)` → `win.BrowserCommands.openTab()`
- 参照: `gTab.documentGlobal`, `win.gBrowser.browsers.length`

## onLocationChange()
- 位置: L72-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `unregisterGlobalTab()`
- 参照: `aLocation.spec`, `gTab.linkedBrowser`

## unregisterGlobalTab()
- 位置: L88-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTab.removeAttribute()`, `gTab.removeEventListener()`, `win.gBrowser.removeTabsProgressListener()`, `win.removeEventListener()`
- 参照: `gTab.documentGlobal`

## CustomizeMode.constructor()
- 位置: L104-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `this.#attachEventListeners()`, `this.#canDrawInTitlebar()`, `this.#ensureCustomizationPanels()`, `this.#onTranslations()`, `this.#window.addEventListener()`, `this.$()`
- 条件付き依存: `if (!content)` → `this.#window.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!content)` → `this.$()`
- 条件付き依存: `if (!content)` → `container.replaceChild()`
- 条件付き依存: `if (!content)` → `this.#window.MozXULElement.parseXULToFragment()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `this.#updateTitlebarCheckbox()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `Services.prefs.addObserver()`
- 条件付き依存: `if (!(this.#canDrawInTitlebar()))` → `this.$()`
- 参照: `aWindow.MutationObserver`, `aWindow.document`, `aWindow.gBrowser`, `container.firstChild.data`, `container.lastChild`, `this.#browser`, `this.#document`, `this.#translationObserver`, `this.#window`, `this.$("customization-titlebar-visibility-checkbox").hidden`, `this.areas`, `this.pongArena`, `this.visiblePalette`
- XPCOM: `Services.prefs`

## CustomizeMode.#handler()
- 位置: L301-303
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#window.CustomizationHandler`

## CustomizeMode.#uninit()
- 位置: L309-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `this.#canDrawInTitlebar()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## CustomizeMode.$()
- 位置: L323-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#document.getElementById()`

## CustomizeMode.setTab()
- 位置: L342-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTab.addEventListener()`, `gTab.setAttribute()`, `win.addEventListener()`, `win.gBrowser.addTabsProgressListener()`, `win.gBrowser.setIcon()`, `win.gBrowser.setTabTitle()`
- 条件付き依存: `if (gTab)` → `closeGlobalTab()`
- 条件付き依存: `if (gTab.linkedPanel)` → `gTab.linkedBrowser.stop()`
- 条件付き依存: `if (gTab.selected)` → `win.gCustomizeMode.enter()`
- 参照: `gTab.documentGlobal`, `gTab.linkedPanel`, `gTab.selected`

## CustomizeMode.enter()
- 位置: L388-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `CustomizableUI.dispatchToolboxEvent()`, `CustomizableUI.notifyStartCustomizing()`, `Services.prefs.getBoolPref()`, `Services.prefs.getPrefType()`, `document.addEventListener()`, `document.getElementById()`, `document.getElementById("mainPopupSet").appendChild()`, `document.querySelectorAll()`, `gTab.documentGlobal.focus()`, `lazy.log.error()`, `panelHolder.appendChild()`, `resetButton.setAttribute()`, `this.#document.documentElement.toggleAttribute()`, `this.#populatePalette()`, `this.#setupDownloadAutoHideToggle()`, `this.#setupPaletteDragging()`, `this.#updateDensityMenu()`, `this.#updateEmptyPaletteNotice()`, `this.#updateOverflowPanelArrowOffset()`, `this.#updateResetButton()`, `this.#updateTouchBarButton()`, `this.#updateUndoResetButton()`, `this.#window.document.documentElement.hasAttribute()`, `this.#wrapAllAreaItems()`, `this.#wrapAreaItemsSync()`, `this.$()`, `this.exit()`, `this.visiblePalette.setAttribute()`, `toolbar.toggleAttribute()`, `window.PanelUI.hide()`, `window.PanelUI.overflowFixedList.toggleAttribute()`, `window.gNavToolbox.addEventListener()`, `window.setTimeout()`
- 条件付き依存: `if ( !this.#window.toolbar.visible || this.#window.document.documentElement.hasAttribute("taskbartab") || this.#window.document.documentElement.hasAttribute("min...)` → `lazy.URILoadingHelper.getTargetWindow()`
- 条件付き依存: `if (w)` → `w.gCustomizeMode.enter()`
- 条件付き依存: `if ( !this.#window.toolbar.visible || this.#window.document.documentElement.hasAttribute("taskbartab") || this.#window.document.documentElement.hasAttribute("min...)` → `Services.obs.addObserver()`
- 条件付き依存: `if ( !this.#window.toolbar.visible || this.#window.document.documentElement.hasAttribute("taskbartab") || this.#window.document.documentElement.hasAttribute("min...)` → `this.#window.openTrustedLinkIn()`
- 条件付き依存: `if (this.#handler.isExitingCustomizeMode)` → `lazy.log.debug()`
- 条件付き依存: `if (!gTab)` → `this.setTab()`
- 条件付き依存: `if (!gTab)` → `this.#browser.addTab()`
- 条件付き依存: `if (!gTab)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (!this.#window.gBrowserInit.delayedStartupFinished)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._wantToBeInCustomizeMode)` → `this.exit()`
- 参照: `Ci.nsIPrefBranch.PREF_BOOL`, `CustomizableUI.AREA_TABSTRIP`, `browser.hidden`, `customizer.hidden`, `document.getElementById("nav-bar-overflow-button").disabled`, `gTab.documentGlobal.gBrowser.selectedTab`, `gTab.ownerDocument`, `gTab.selected`, `panelContextMenu.parentNode`, `this.#customizing`, `this.#document`, `this.#handler.isEnteringCustomizeMode`, `this.#handler.isExitingCustomizeMode`, `this.#skipSourceNodeCheck`, `this.#transitioning`, `this.#window`, `this.#window.gBrowserInit.delayedStartupFinished`, `this.#window.toolbar.visible`, `this._previousPanelContextMenuParent`, `this._wantToBeInCustomizeMode`, `this.visiblePalette.clientTop`, `this.visiblePalette.hidden`, `window.PanelUI.menuButton.disabled`, `window.PanelUI.overflowFixedList`
- XPCOM: [`nsIPrefBranch`](../../../netwerk/base/nsINetUtil.idl.md) / `Services.obs` / `Services.prefs` / `Services.scriptSecurityManager`

## obs()
- 位置: L402-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.URILoadingHelper.getTargetWindow()`, `w.gCustomizeMode.enter()`
- 参照: `this.#window`
- XPCOM: `Services.obs`

## delayedStartupObserver()
- 位置: L466-474
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aSubject == this.#window)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aSubject == this.#window)` → `resolve()`
- 参照: `this.#window`
- XPCOM: `Services.obs`

## CustomizeMode.exit()
- 位置: L584-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.dispatchToolboxEvent()`, `CustomizableUI.notifyEndCustomizing()`, `CustomizableUI.removeListener()`, `document.documentElement.removeAttribute()`, `document.getElementById()`, `document.querySelectorAll()`, `document.removeEventListener()`, `lazy.log.error()`, `overflowContainer.appendChild()`, `this.#depopulatePalette()`, `this.#maybeMoveDownloadsButtonToNavBar()`, `this.#teardownDownloadAutoHideToggle()`, `this.#teardownPaletteDragging()`, `this.#togglePong()`, `this.#translationObserver.disconnect()`, `this.#unwrapAllAreaItems()`, `this.$()`, `this._previousPanelContextMenuParent.appendChild()`, `this.areas.clear()`, `toolbar.removeAttribute()`, `window.gNavToolbox.removeEventListener()`
- 条件付き依存: `if (this.#handler.isEnteringCustomizeMode)` → `lazy.log.debug()`
- 条件付き依存: `if (this.resetting)` → `lazy.log.debug()`
- 条件付き依存: `if (this.#browser.selectedTab == gTab)` → `closeGlobalTab()`
- 条件付き依存: `if (this._wantToBeInCustomizeMode)` → `this.enter()`
- 参照: `browser.hidden`, `customizer.hidden`, `document.getElementById( "widget-overflow-mainView" ).firstElementChild`, `document.getElementById("nav-bar-overflow-button").disabled`, `resetButton.disabled`, `this.#browser.selectedTab`, `this.#customizing`, `this.#document`, `this.#handler.isEnteringCustomizeMode`, `this.#handler.isExitingCustomizeMode`, `this.#transitioning`, `this.#window`, `this._lastLightweightTheme`, `this._wantToBeInCustomizeMode`, `this.resetting`, `undoResetButton.hidden`, `window.PanelUI.menuButton.disabled`, `window.PanelUI.overflowFixedList`

## CustomizeMode.#updateOverflowPanelArrowOffset()
- 位置: async L706-730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `overflowButton.getBoundingClientRect()`, `this.#document.documentElement.getAttribute()`, `this.#window.promiseDocumentFlushed()`, `this.$()`, `this.$("customization-panelWrapper").style.setProperty()`
- 参照: `buttonRect.left`, `buttonRect.right`, `buttonRect.width`, `this.#document`, `this.#window.RTL_UI`, `this.#window.innerWidth`

## CustomizeMode.#getCustomizableChildForNode()
- 位置: L742-772
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `aNode.ownerDocument.getElementById()`, `areaNode.getAttribute()`, `areas.includes()`, `areas.push()`
- 条件付き依存: `if (customizationTarget && customizationTarget != areaNode)` → `areas.push()`
- 条件付き依存: `if (overflowTarget)` → `areas.push()`
- 参照: `CustomizableUI.areas`, `aNode.parentNode`, `areas.length`, `customizationTarget.id`, `parent.id`

## CustomizeMode.#promiseWidgetAnimationOut()
- 位置: L791-849
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.getAttribute()`, `aNode.parentNode.id.startsWith()`, `animationNode.addEventListener()`, `animationNode.classList.add()`, `animationNode.documentGlobal.gNavToolbox.addEventListener()`, `this.#window.requestAnimationFrame()`
- 参照: `aNode.hidden`, `aNode.id`, `aNode.parentNode`, `aNode.tagName`, `this.#window.gReduceMotion`

## cleanupCustomizationExit()
- 位置: L808-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveAnimationPromise()`

## cleanupWidgetAnimationEnd()
- 位置: L812-819
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( e.animationName == "widget-animate-out" && e.target.id == animationNode.id )` → `resolveAnimationPromise()`
- 参照: `animationNode.id`, `e.animationName`, `e.target.id`

## resolveAnimationPromise()
- 位置: L821-831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `animationNode.removeEventListener()`, `resolve()`

## CustomizeMode.addToToolbar()
- 位置: async L864-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addWidgetToArea()`, `CustomizableUI.isSpecialWidget()`, `aNode.closest()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `this.#getCustomizableChildForNode()`, `this.#promiseWidgetAnimationOut()`
- 条件付き依存: `if ( CustomizableUI.isSpecialWidget(widgetToAdd) && aNode.closest("#customization-palette") )` → `widgetToAdd.match()`
- 条件付き依存: `if (!this.#customizing)` → `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (aNode.id == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.#customizing)` → `this.#showDownloadsAutoHidePanel()`
- 条件付き依存: `if (animationNode)` → `animationNode.classList.remove()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `aNode.firstElementChild`, `aNode.id`, `aNode.localName`, `this.#customizing`
- XPCOM: `Services.prefs`

## CustomizeMode.addToPanel()
- 位置: async L934-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addWidgetToArea()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `this.#getCustomizableChildForNode()`, `this.#promiseWidgetAnimationOut()`
- 条件付き依存: `if (!this.#customizing)` → `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (aNode.id == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.#customizing)` → `this.#showDownloadsAutoHidePanel()`
- 条件付き依存: `if (animationNode)` → `animationNode.classList.remove()`
- 条件付き依存: `if (!this.#window.gReduceMotion)` → `this.$()`
- 条件付き依存: `if (!this.#window.gReduceMotion)` → `overflowButton.setAttribute()`
- 条件付き依存: `if (!this.#window.gReduceMotion)` → `overflowButton.addEventListener()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `aNode.firstElementChild`, `aNode.id`, `aNode.localName`, `this.#customizing`, `this.#window.gReduceMotion`
- XPCOM: `Services.prefs`

## onAnimationEnd()
- 位置: L968-973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.animationName.startsWith()`
- 条件付き依存: `if (event.animationName.startsWith("overflow-animation"))` → `this.removeEventListener()`
- 条件付き依存: `if (event.animationName.startsWith("overflow-animation"))` → `this.removeAttribute()`

## CustomizeMode.removeFromArea()
- 位置: async L1006-1033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeWidgetFromArea()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `this.#getCustomizableChildForNode()`, `this.#promiseWidgetAnimationOut()`
- 条件付き依存: `if (!this.#customizing)` → `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (aNode.id == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.#customizing)` → `this.#showDownloadsAutoHidePanel()`
- 条件付き依存: `if (animationNode)` → `animationNode.classList.remove()`
- 参照: `aNode.firstElementChild`, `aNode.id`, `aNode.localName`, `this.#customizing`
- XPCOM: `Services.prefs`

## CustomizeMode.#populatePalette()
- 位置: L1041-1072
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.createSpecialWidget()`, `CustomizableUI.getUnusedWidgets()`, `fragment.appendChild()`, `lazy.log.error()`, `this.#document.createDocumentFragment()`, `this.#makePaletteItem()`, `this.#updateCommandsDisabledState()`, `this.visiblePalette.appendChild()`, `this.wrapToolbarItem()`
- 参照: `this.#document`, `this.#stowedPalette`, `this.#window.gNavToolbox.palette`, `this.visiblePalette`

## CustomizeMode.#makePaletteItem()
- 位置: L1082-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWidget.forWindow()`, `this.createOrUpdateWrapper()`, `wrapper.appendChild()`
- 条件付き依存: `if (!widgetNode)` → `lazy.log.error()`
- 参照: `aWidget.forWindow(this.#window).node`, `aWidget.id`, `this.#window`, `widgetNode.hidden`

## CustomizeMode.#depopulatePalette()
- 位置: L1106-1132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isSpecialWidget()`, `this.#updateCommandsDisabledState()`
- 条件付き依存: `if (CustomizableUI.isSpecialWidget(itemId))` → `this.visiblePalette.removeChild()`
- 条件付き依存: `if (!(CustomizableUI.isSpecialWidget(itemId)))` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (!(CustomizableUI.isSpecialWidget(itemId)))` → `this.#stowedPalette.appendChild()`
- 参照: `paletteChild.firstElementChild.id`, `paletteChild.nextElementSibling`, `this.#stowedPalette`, `this.#window.gNavToolbox.palette`, `this.visiblePalette.firstElementChild`, `this.visiblePalette.hidden`

## CustomizeMode.#updateCommandsDisabledState()
- 位置: L1148-1164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#document.querySelectorAll()`, `this.#enabledCommands.has()`
- 条件付き依存: `if (shouldBeDisabled)` → `command.hasAttribute()`
- 条件付き依存: `if (!command.hasAttribute("disabled"))` → `command.setAttribute()`
- 条件付き依存: `if (!(!command.hasAttribute("disabled")))` → `command.setAttribute()`
- 条件付き依存: `if (!(shouldBeDisabled))` → `command.getAttribute()`
- 条件付き依存: `if (command.getAttribute("wasdisabled") != "true")` → `command.removeAttribute()`
- 条件付き依存: `if (!(command.getAttribute("wasdisabled") != "true"))` → `command.removeAttribute()`
- 参照: `command.id`

## CustomizeMode.#isCustomizableItem()
- 位置: L1176-1184
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aNode.localName`

## CustomizeMode.isWrappedToolbarItem()
- 位置: L1195-1197
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aNode.localName`

## CustomizeMode.#deferredWrapToolbarItem()
- 位置: L1213-1220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `resolve()`, `this.wrapToolbarItem()`
- XPCOM: `Services.tm`

## CustomizeMode.wrapToolbarItem()
- 位置: L1236-1252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isCustomizableItem()`, `this.createOrUpdateWrapper()`, `wrapper.appendChild()`
- 条件付き依存: `if (aNode.parentNode)` → `aNode.parentNode.replaceChild()`
- 参照: `aNode.parentNode`

## CustomizeMode.#updateWrapperLabel()
- 位置: L1270-1283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("label"))` → `aWrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("label"))` → `aNode.getAttribute()`
- 条件付き依存: `if (!(aNode.hasAttribute("label")))` → `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("title"))` → `aWrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("title"))` → `aNode.getAttribute()`
- 条件付き依存: `if (!(aNode.hasAttribute("title")))` → `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("data-l10n-id") && !aIsUpdate)` → `this.#translationObserver.observe()`
- 参照: `aNode.parentElement`

## CustomizeMode.#onTranslations()
- 位置: L1292-1302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mut.target.hasAttribute()`, `target.hasAttribute()`
- 条件付き依存: `if ( target.parentElement?.localName == "toolbarpaletteitem" && (target.hasAttribute("label") || mut.target.hasAttribute("title")) )` → `this.#updateWrapperLabel()`
- 参照: `target.parentElement?.localName`

## CustomizeMode.createOrUpdateWrapper()
- 位置: L1321-1414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isSpecialWidget()`, `CustomizableUI.isWidgetRemovable()`, `aNode.getAttribute()`, `aNode.hasAttribute()`, `this.#updateWrapperLabel()`, `wrapper.setAttribute()`
- 条件付き依存: `if ( aIsUpdate && aNode.parentNode && aNode.parentNode.localName == "toolbarpaletteitem" )` → `wrapper.getAttribute()`
- 条件付き依存: `if (!( aIsUpdate && aNode.parentNode && aNode.parentNode.localName == "toolbarpaletteitem" ))` → `this.#document.createXULElement()`
- 条件付き依存: `if (!( aIsUpdate && aNode.parentNode && aNode.parentNode.localName == "toolbarpaletteitem" ))` → `wrapper.setAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("command") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `wrapper.setAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("command") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.getAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("command") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.removeAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("observes") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `wrapper.setAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("observes") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.getAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("observes") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.removeAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("checked"))` → `wrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("checked"))` → `aNode.removeAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("id"))` → `wrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("id"))` → `aNode.getAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("flex"))` → `wrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("flex"))` → `aNode.getAttribute()`
- 条件付き依存: `if (!(aNode.getAttribute("context")))` → `aNode.getAttribute()`
- 条件付き依存: `if (aPlace != "toolbar")` → `wrapper.setAttribute()`
- 条件付き依存: `if (currentContextMenu && currentContextMenu != contextMenuForPlace)` → `aNode.setAttribute()`
- 条件付き依存: `if (currentContextMenu && currentContextMenu != contextMenuForPlace)` → `aNode.removeAttribute()`
- 条件付き依存: `if (currentContextMenu == contextMenuForPlace)` → `aNode.removeAttribute()`
- 条件付き依存: `if (!aIsUpdate)` → `wrapper.addEventListener()`
- 条件付き依存: `if (CustomizableUI.isSpecialWidget(aNode.id))` → `wrapper.setAttribute()`
- 条件付き依存: `if (CustomizableUI.isSpecialWidget(aNode.id))` → `lazy.gWidgetsBundle.GetStringFromName()`
- 参照: `aNode.id`, `aNode.nodeName`, `aNode.parentNode`, `aNode.parentNode.localName`

## CustomizeMode.#deferredUnwrapToolbarItem()
- 位置: L1426-1438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `console.error()`, `resolve()`, `this.unwrapToolbarItem()`
- XPCOM: `Services.tm`

## CustomizeMode.unwrapToolbarItem()
- 位置: L1451-1505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWrapper.getAttribute()`, `aWrapper.hasAttribute()`, `aWrapper.removeEventListener()`, `toolbarItem.getAttribute()`
- 条件付き依存: `if (!toolbarItem)` → `lazy.log.error()`
- 条件付き依存: `if (!toolbarItem)` → `aWrapper.remove()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemobserves"))` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemobserves"))` → `aWrapper.getAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `aWrapper.getAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `this.$()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `toolbarItem.toggleAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `command?.hasAttribute()`
- 条件付き依存: `if (wrappedContext)` → `toolbarItem.getAttribute()`
- 条件付き依存: `if (wrappedContext)` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (wrappedContext)` → `toolbarItem.removeAttribute()`
- 条件付き依存: `if (place == "panel")` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (aWrapper.parentNode)` → `aWrapper.parentNode.replaceChild()`
- 参照: `aWrapper.firstElementChild`, `aWrapper.id`, `aWrapper.nodeName`, `aWrapper.parentNode`, `aWrapper.tagName`, `toolbarItem.checked`

## CustomizeMode.#wrapAreaItems()
- 位置: async L1521-1541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getCustomizeTargetForArea()`, `this.#addCustomizeTargetDragAndDropHandlers()`, `this.#isCustomizableItem()`, `this.areas.add()`, `this.areas.has()`, `this.isWrappedToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `this.#deferredWrapToolbarItem( child, CustomizableUI.getPlaceForItem(child) ).catch()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `this.#deferredWrapToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `CustomizableUI.getPlaceForItem()`
- 参照: `lazy.log.error`, `target.children`, `this.#window`

## CustomizeMode.#wrapAreaItemsSync()
- 位置: L1555-1577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getCustomizeTargetForArea()`, `lazy.log.error()`, `this.#addCustomizeTargetDragAndDropHandlers()`, `this.#isCustomizableItem()`, `this.areas.add()`, `this.areas.has()`, `this.isWrappedToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `this.wrapToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `CustomizableUI.getPlaceForItem()`
- 参照: `ex.stack`, `target.children`, `this.#window`

## CustomizeMode.#wrapAllAreaItems()
- 位置: async L1587-1591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#wrapAreaItems()`
- 参照: `CustomizableUI.areas`

## CustomizeMode.#addCustomizeTargetDragAndDropHandlers()
- 位置: L1601-1611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTarget.addEventListener()`
- 条件付き依存: `if (aTarget.id == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `this.$()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `aTarget.id`

## CustomizeMode.#wrapItemsInArea()
- 位置: L1620-1626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isCustomizableItem()`
- 条件付き依存: `if (this.#isCustomizableItem(child))` → `this.wrapToolbarItem()`
- 条件付き依存: `if (this.#isCustomizableItem(child))` → `CustomizableUI.getPlaceForItem()`
- 参照: `target.children`

## CustomizeMode.#removeCustomizeTargetDragAndDropHandlers()
- 位置: L1635-1646
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTarget.removeEventListener()`
- 条件付き依存: `if (aTarget.id == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `this.$()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `aTarget.id`

## CustomizeMode.#unwrapItemsInArea()
- 位置: L1656-1662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isWrappedToolbarItem()`
- 条件付き依存: `if (this.isWrappedToolbarItem(toolbarItem))` → `this.unwrapToolbarItem()`
- 参照: `target.children`

## CustomizeMode.#unwrapAllAreaItems()
- 位置: L1673-1685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeCustomizeTargetDragAndDropHandlers()`, `this.areas.clear()`, `this.isWrappedToolbarItem()`
- 条件付き依存: `if (this.isWrappedToolbarItem(toolbarItem))` → `this.#deferredUnwrapToolbarItem()`
- 参照: `lazy.log.error`, `target.children`, `this.areas`

## CustomizeMode.reset()
- 位置: L1694-1717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.reset()`, `this.#depopulatePalette()`, `this.#populatePalette()`, `this.#unwrapAllAreaItems()`, `this.#updateEmptyPaletteNotice()`, `this.#updateResetButton()`, `this.#updateUndoResetButton()`, `this.#wrapAllAreaItems()`, `this.$()`
- 条件付き依存: `if (!this._wantToBeInCustomizeMode)` → `this.exit()`
- 参照: `btn.disabled`, `lazy.log.error`, `this.#moveDownloadsButtonToNavBar`, `this._wantToBeInCustomizeMode`, `this.resetting`

## CustomizeMode.undoReset()
- 位置: L1725-1743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.undoReset()`, `this.#depopulatePalette()`, `this.#populatePalette()`, `this.#unwrapAllAreaItems()`, `this.#updateEmptyPaletteNotice()`, `this.#updateResetButton()`, `this.#updateUndoResetButton()`, `this.#wrapAllAreaItems()`
- 参照: `lazy.log.error`, `this.#moveDownloadsButtonToNavBar`, `this.resetting`

## CustomizeMode.#onToolbarVisibilityChange()
- 位置: L1752-1759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onUIChange()`, `toolbar.getAttribute()`, `toolbar.toggleAttribute()`
- 参照: `aEvent.detail.visible`, `aEvent.target`

## CustomizeMode.onWidgetMoved()
- 位置: L1764-1766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onUIChange()`

## CustomizeMode.onWidgetAdded()
- 位置: L1771-1773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onUIChange()`

## CustomizeMode.onWidgetRemoved()
- 位置: L1779-1781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onUIChange()`

## CustomizeMode.onWidgetBeforeDOMChange()
- 位置: L1795-1807
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNodeToChange.parentNode)` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (aSecondaryNode)` → `this.unwrapToolbarItem()`
- 参照: `aContainer.documentGlobal`, `aNodeToChange.parentNode`, `aSecondaryNode.parentNode`, `this.#window`, `this.resetting`

## CustomizeMode.onWidgetAfterDOMChange()
- 位置: L1821-1846
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aNodeToChange.parentNode)` → `CustomizableUI.getPlaceForItem()`
- 条件付き依存: `if (aNodeToChange.parentNode)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (aSecondaryNode)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (!(aNodeToChange.parentNode))` → `CustomizableUI.getWidget()`
- 条件付き依存: `if (widget.provider == CustomizableUI.PROVIDER_API)` → `this.#makePaletteItem()`
- 条件付き依存: `if (widget.provider == CustomizableUI.PROVIDER_API)` → `this.visiblePalette.appendChild()`
- 参照: `CustomizableUI.PROVIDER_API`, `aContainer.documentGlobal`, `aNodeToChange.id`, `aNodeToChange.parentNode`, `this.#window`, `this.resetting`, `widget.provider`

## CustomizeMode.onWidgetDestroyed()
- 位置: L1855-1860
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.$()`
- 条件付き依存: `if (wrapper)` → `wrapper.remove()`

## CustomizeMode.onWidgetAfterCreation()
- 位置: L1875-1887
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!aArea)` → `this.$()`
- 条件付き依存: `if (widgetNode)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (!(widgetNode))` → `CustomizableUI.getWidget()`
- 条件付き依存: `if (!(widgetNode))` → `this.visiblePalette.appendChild()`
- 条件付き依存: `if (!(widgetNode))` → `this.#makePaletteItem()`

## CustomizeMode.onAreaNodeRegistered()
- 位置: L1898-1904
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aContainer.ownerDocument == this.#document)` → `this.#wrapItemsInArea()`
- 条件付き依存: `if (aContainer.ownerDocument == this.#document)` → `this.#addCustomizeTargetDragAndDropHandlers()`
- 条件付き依存: `if (aContainer.ownerDocument == this.#document)` → `this.areas.add()`
- 参照: `aContainer.ownerDocument`, `this.#document`

## CustomizeMode.onAreaNodeUnregistered()
- 位置: L1918-1927
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aContainer.ownerDocument == this.#document && aReason == CustomizableUI.REASON_AREA_UNREGISTERED )` → `this.#unwrapItemsInArea()`
- 条件付き依存: `if ( aContainer.ownerDocument == this.#document && aReason == CustomizableUI.REASON_AREA_UNREGISTERED )` → `this.#removeCustomizeTargetDragAndDropHandlers()`
- 条件付き依存: `if ( aContainer.ownerDocument == this.#document && aReason == CustomizableUI.REASON_AREA_UNREGISTERED )` → `this.areas.delete()`
- 参照: `CustomizableUI.REASON_AREA_UNREGISTERED`, `aContainer.ownerDocument`, `this.#document`

## CustomizeMode.#openUIDensityPreferences()
- 位置: L1932-1934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.openPreferences()`

## CustomizeMode.#updateDensityMenu()
- 位置: L1942-1966
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `button.querySelector()`, `gUIDensity.getCurrentDensity()`, `this.#document.getElementById()`
- 条件付き依存: `if (gUIDensity.getCurrentDensity().mode == gUIDensity.MODE_COMPACT)` → `Services.prefs.setBoolPref()`
- 参照: `button.hidden`, `gUIDensity.MODE_COMPACT`, `gUIDensity.getCurrentDensity().mode`, `link.hidden`, `this.#window.gUIDensity`, `this.#window.gUIDensity.novaEnabled`
- XPCOM: `Services.prefs`

## CustomizeMode.#openAddonsManagerThemes()
- 位置: L1971-1973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.BrowserAddonUI.openAddonsMgr()`

## CustomizeMode.#previewUIDensity()
- 位置: L1985-1988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateOverflowPanelArrowOffset()`, `this.#window.gUIDensity.update()`

## CustomizeMode.#resetUIDensity()
- 位置: L1994-1997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateOverflowPanelArrowOffset()`, `this.#window.gUIDensity.update()`

## CustomizeMode.setUIDensity()
- 位置: L2006-2016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`, `panel.hidePopup()`, `this.#onUIChange()`, `this.#updateOverflowPanelArrowOffset()`, `win.document.getElementById()`
- 参照: `gUIDensity.uiDensityPref`, `this.#window`, `win.gUIDensity`
- XPCOM: `Services.prefs`

## CustomizeMode.#onUIDensityMenuShowing()
- 位置: L2022-2098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `doc.getElementById()`, `gUIDensity.getCurrentDensity()`
- 条件付き依存: `if (Services.prefs.getBoolPref(kCompactModeShowPref))` → `items.push()`
- 条件付き依存: `if (touchItem)` → `items.push()`
- 条件付き依存: `if (item.mode == currentDensity.mode)` → `item.setAttribute()`
- 条件付き依存: `if (!(item.mode == currentDensity.mode))` → `item.removeAttribute()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `doc.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `spacer.removeAttribute()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `checkbox.removeAttribute()`
- 条件付き依存: `if (currentDensity.overridden)` → `Services.strings.createBundle()`
- 条件付き依存: `if (currentDensity.overridden)` → `touchItem.setAttribute()`
- 条件付き依存: `if (currentDensity.overridden)` → `sb.GetStringFromName()`
- 条件付き依存: `if (!(currentDensity.overridden))` → `touchItem.removeAttribute()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (autoTouchMode)` → `checkbox.setAttribute()`
- 条件付き依存: `if (!(autoTouchMode))` → `checkbox.removeAttribute()`
- 参照: `AppConstants.platform`, `compactItem.hidden`, `compactItem.mode`, `currentDensity.mode`, `currentDensity.overridden`, `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_NORMAL`, `gUIDensity.MODE_TOUCH`, `item.mode`, `normalItem.mode`, `this.#window`, `touchItem.mode`, `win.document`, `win.gUIDensity`, `win.gUIDensity.autoTouchModePref`
- XPCOM: `Services.prefs` / `Services.strings`

## CustomizeMode.#updateAutoTouchMode()
- 位置: L2108-2114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.#onUIChange()`, `this.#onUIDensityMenuShowing()`
- XPCOM: `Services.prefs`

## CustomizeMode.#onUIChange()
- 位置: L2120-2127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (!this.resetting)` → `this.#updateResetButton()`
- 条件付き依存: `if (!this.resetting)` → `this.#updateUndoResetButton()`
- 条件付き依存: `if (!this.resetting)` → `this.#updateEmptyPaletteNotice()`
- 参照: `this.resetting`

## CustomizeMode.#updateEmptyPaletteNotice()
- 位置: L2134-2148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `paletteItems[0].id.includes()`, `this.$()`, `this.visiblePalette.getElementsByTagName()`
- 条件付き依存: `if (!( paletteItems.length == 1 && paletteItems[0].id.includes("wrapper-customizableui-special-spring") ))` → `this.#togglePong()`
- 参照: `paletteItems.length`, `whimsyButton.hidden`

## CustomizeMode.#updateResetButton()
- 位置: L2154-2157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.$()`
- 参照: `CustomizableUI.inDefaultState`, `btn.disabled`

## CustomizeMode.#updateUndoResetButton()
- 位置: L2163-2166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.$()`
- 参照: `CustomizableUI.canUndoReset`, `undoResetButton.hidden`

## CustomizeMode.#updateTouchBarButton()
- 位置: L2172-2182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gTouchBarUpdater.isTouchBarInitialized()`, `this.$()`
- 参照: `AppConstants.platform`, `touchBarButton.hidden`, `touchBarSpacer.hidden`

## CustomizeMode.handleEvent()
- 位置: L2192-2227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onDragDrop()`, `this.#onDragEnd()`, `this.#onDragLeave()`, `this.#onDragOver()`, `this.#onDragStart()`, `this.#onMouseDown()`, `this.#onMouseUp()`, `this.#onToolbarVisibilityChange()`, `this.#uninit()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_ESCAPE)` → `this.exit()`
- 参照: `aEvent.DOM_VK_ESCAPE`, `aEvent.keyCode`, `aEvent.type`

## CustomizeMode.#setupPaletteDragging()
- 位置: L2234-2260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentContainer.addEventListener()`, `this.#addCustomizeTargetDragAndDropHandlers()`, `this.$()`
- 参照: `this.paletteDragHandler`, `this.visiblePalette`

## this.paletteDragHandler()
- 位置: L2237-2252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isUnwantedDragDrop()`, `this.$()`, `this.$("customization-panelHolder").contains()`, `this.visiblePalette.contains()`
- 条件付き依存: `if (aEvent.type == "dragover")` → `this.#onDragOver()`
- 条件付き依存: `if (!(aEvent.type == "dragover"))` → `this.#onDragDrop()`
- 参照: `aEvent.originalTarget`, `aEvent.type`, `this.visiblePalette`

## CustomizeMode.#teardownPaletteDragging()
- 位置: L2266-2278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentContainer.removeEventListener()`, `lazy.DragPositionManager.stop()`, `this.#removeCustomizeTargetDragAndDropHandlers()`, `this.$()`
- 参照: `this.paletteDragHandler`, `this.visiblePalette`

## CustomizeMode.observe()
- 位置: L2289-2299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#canDrawInTitlebar()`, `this.#updateResetButton()`, `this.#updateUndoResetButton()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `this.#updateTitlebarCheckbox()`

## CustomizeMode.#canDrawInTitlebar()
- 位置: L2307-2309
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#window.CustomTitlebar.systemSupported`

## CustomizeMode.#ensureCustomizationPanels()
- 位置: L2317-2323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `template.replaceWith()`, `this.$()`, `wrapper.replaceWith()`
- 参照: `template.content`, `wrapper.content`

## CustomizeMode.#attachEventListeners()
- 位置: L2329-2453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `autohidePanel.addEventListener()`, `container.addEventListener()`, `densityMenu.addEventListener()`, `event.target.hidePopup()`, `this.#customizeTouchBar()`, `this.#document.getElementById()`, `this.#onDownloadsAutoHideChange()`, `this.#onPaletteContextMenuShowing()`, `this.#onUIDensityMenuShowing()`, `this.#openAddonsManagerThemes()`, `this.#openUIDensityPreferences()`, `this.#togglePong()`, `this.#toggleTitlebar()`, `this.#updateAutoTouchMode()`, `this.#window.ToolbarContextMenu.onViewToolbarsPopupShowing()`, `this.#window.clearTimeout()`, `this.#window.setTimeout()`, `this.$()`, `this.$("customization-lwtheme-link").addEventListener()`, `this.$("customization-uidensity-link").addEventListener()`, `this.$(kDownloadAutohideCheckboxId).addEventListener()`, `this.$(kPaletteItemContextMenu).addEventListener()`, `this.addToPanel()`, `this.addToToolbar()`, `this.exit()`, `this.reset()`, `this.setUIDensity()`, `this.undoReset()`
- 参照: `event.target.checked`, `event.target.id`, `event.target.mode`, `event.target.parentNode.triggerNode`, `this._downloadPanelAutoHideTimeout`

## updateDensity()
- 位置: L2376-2383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#previewUIDensity()`
- 参照: `event.target.id`, `event.target.mode`

## resetDensity()
- 位置: L2390-2397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resetUIDensity()`
- 参照: `event.target.id`

## CustomizeMode.#updateTitlebarCheckbox()
- 位置: L2460-2471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.$()`
- 条件付き依存: `if (drawInTitlebar)` → `checkbox.removeAttribute()`
- 条件付き依存: `if (!(drawInTitlebar))` → `checkbox.setAttribute()`
- 参照: `Services.appinfo.drawInTitlebar`
- XPCOM: `Services.appinfo`

## CustomizeMode.#toggleTitlebar()
- 位置: L2480-2483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## CustomizeMode.#getBoundsWithoutFlushing()
- 位置: L2494-2496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.windowUtils.getBoundsWithoutFlushing()`

## CustomizeMode.#onDragStart()
- 位置: L2505-2584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlaceForItem()`, `__dumpDragData()`, `draggedItem.closest()`, `dt.mozSetDataAt()`, `this.#getBoundsWithoutFlushing()`, `this.#window.setTimeout()`
- 条件付き依存: `if (toolbarParent)` → `this.#getBoundsWithoutFlushing()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.dataTransfer`, `aEvent.target`, `aEvent.target.ownerDocument.documentElement.id`, `draggedItem.id`, `dt.effectAllowed`, `item.firstElementChild`, `item.id`, `item.localName`, `item.parentNode`, `itemCenter.x`, `itemCenter.y`, `itemRect.height`, `itemRect.left`, `itemRect.top`, `itemRect.width`, `this._dragInitializeTimeout`, `this._dragOffset`, `this._initializeDragAfterMove`, `toolbarParent.style.minHeight`, `toolbarRect.height`

## this._initializeDragAfterMove()
- 位置: L2548-2579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.clearTimeout()`
- 条件付き依存: `if (this.#customizing && !this.#transitioning)` → `lazy.DragPositionManager.start()`
- 条件付き依存: `if (item.nextElementSibling)` → `this.#setDragActive()`
- 条件付き依存: `if (canUsePrevSibling && item.previousElementSibling)` → `this.#setDragActive()`
- 条件付き依存: `if (this.#customizing && !this.#transitioning)` → `this.#getCustomizableParent()`
- 条件付き依存: `if (this.#customizing && !this.#transitioning)` → `currentArea.setAttribute()`
- 参照: `draggedItem.id`, `item.hidden`, `item.nextElementSibling`, `item.previousElementSibling`, `this.#customizing`, `this.#dragOverItem`, `this.#transitioning`, `this.#window`, `this._dragInitializeTimeout`, `this._initializeDragAfterMove`

## CustomizeMode.#onDragOver()
- 位置: L2595-2731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.canWidgetMoveToArea()`, `CustomizableUI.getCustomizationTarget()`, `CustomizableUI.getPlaceForItem()`, `CustomizableUI.isWidgetRemovable()`, `__dumpDragData()`, `aEvent.dataTransfer.mozGetDataAt()`, `aEvent.dataTransfer.mozTypesAt()`, `aEvent.preventDefault()`, `aEvent.stopPropagation()`, `document.getElementById()`, `dragOverItem.getAttribute()`, `this.#getCustomizableParent()`, `this.#getDragOverNode()`, `this.#isUnwantedDragDrop()`
- 条件付き依存: `if (this._initializeDragAfterMove)` → `this._initializeDragAfterMove()`
- 条件付き依存: `if (targetNode == CustomizableUI.getCustomizationTarget(targetArea))` → `this.#findVisiblePreviousSiblingNode()`
- 条件付き依存: `if (!(targetNode == CustomizableUI.getCustomizationTarget(targetArea)))` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if (position == -1)` → `this.#findVisiblePreviousSiblingNode()`
- 条件付き依存: `if (targetAreaType == "toolbar")` → `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (targetAreaType == "toolbar")` → `dragOverItem.getAttribute()`
- 条件付き依存: `if (existingDir == "before")` → `parseInt()`
- 条件付き依存: `if (!(existingDir == "before"))` → `parseInt()`
- 条件付き依存: `if (targetAreaType == "panel")` → `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (targetAreaType == "panel")` → `dragOverItem.getAttribute()`
- 条件付き依存: `if (this.#dragOverItem && dragOverItem != this.#dragOverItem)` → `this.#cancelDragActive()`
- 条件付き依存: `if ( dragOverItem != this.#dragOverItem || dragValue != dragOverItem.getAttribute("dragover") )` → `CustomizableUI.getCustomizationTarget()`
- 条件付き依存: `if (dragOverItem != CustomizableUI.getCustomizationTarget(targetArea))` → `this.#setDragActive()`
- 条件付き依存: `if ( dragOverItem != this.#dragOverItem || dragValue != dragOverItem.getAttribute("dragover") )` → `targetArea.setAttribute()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.currentTarget`, `aEvent.dataTransfer.mozTypesAt(0).length`, `aEvent.target.ownerDocument`, `document.documentElement.id`, `dragOverItem.style.borderBlockEndWidth`, `dragOverItem.style.borderBlockStartWidth`, `dragOverItem.style.borderInlineEndWidth`, `dragOverItem.style.borderInlineStartWidth`, `itemRect.height`, `itemRect.left`, `itemRect.top`, `itemRect.width`, `targetArea.id`, `targetNode.lastElementChild`, `targetNode.parentNode`, `targetParent.children`, `this.#dragOverItem`, `this.#window.RTL_UI`, `this._initializeDragAfterMove`

## CustomizeMode.#onDragDrop()
- 位置: L2742-2802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `__dumpDragData()`, `aEvent.dataTransfer.mozGetDataAt()`, `document.getElementById()`, `lazy.log.error()`, `targetNode.getAttribute()`, `this.#applyDrop()`, `this.#cancelDragActive()`, `this.#getCustomizableParent()`, `this.#isUnwantedDragDrop()`, `this.#window.clearTimeout()`
- 条件付き依存: `if (draggedItemId == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (draggedItemId == "downloads-button")` → `this.#showDownloadsAutoHidePanel()`
- 参照: `aEvent.currentTarget`, `aEvent.target.ownerDocument`, `document.documentElement.id`, `ex.stack`, `targetNode.firstElementChild`, `targetNode.nextElementSibling`, `targetNode.tagName`, `this.#dragOverItem`, `this.#dragSizeMap`, `this._dragInitializeTimeout`, `this._initializeDragAfterMove`
- XPCOM: `Services.prefs`

## CustomizeMode.#applyDrop()
- 位置: L2819-2982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.canWidgetMoveToArea()`, `CustomizableUI.getCustomizationTarget()`, `CustomizableUI.isSpecialWidget()`, `document.getElementById()`, `draggedItem.closest()`, `draggedItem.getAttribute()`, `draggedItem.removeAttribute()`, `itemForPlacement.getAttribute()`, `this.#onDragEnd()`
- 条件付き依存: `if (toolbarParent)` → `toolbarParent.style.removeProperty()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `CustomizableUI.isWidgetRemovable()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `CustomizableUI.removeWidgetFromArea()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if (aTargetNode == this.visiblePalette)` → `this.visiblePalette.appendChild()`
- 条件付き依存: `if (!(aTargetNode == this.visiblePalette))` → `this.visiblePalette.insertBefore()`
- 条件付き依存: `if (aTargetArea.id == kPaletteId)` → `this.#onDragEnd()`
- 条件付き依存: `if (draggedItem.getAttribute("skipintoolbarset") == "true")` → `draggedItem.parentNode.getAttribute()`
- 条件付き依存: `if (draggedItem.getAttribute("skipintoolbarset") == "true")` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `areaCustomizationTarget.appendChild()`
- 条件付き依存: `if (!(aTargetNode == areaCustomizationTarget))` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (!(aTargetNode == areaCustomizationTarget))` → `areaCustomizationTarget.insertBefore()`
- 条件付き依存: `if (!(aTargetNode == areaCustomizationTarget))` → `this.wrapToolbarItem()`
- 条件付き依存: `if (draggedItem.getAttribute("skipintoolbarset") == "true")` → `this.wrapToolbarItem()`
- 条件付き依存: `if ( CustomizableUI.isSpecialWidget(aDroppedItemId) && aOriginArea.id == kPaletteId )` → `aDroppedItemId.match()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `this.#onDragEnd()`
- 条件付き依存: `if (itemForPlacement)` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!placement)` → `lazy.log.debug()`
- 条件付き依存: `if (aTargetArea == aOriginArea)` → `CustomizableUI.moveWidgetWithinArea()`
- 条件付き依存: `if (aTargetArea == aOriginArea)` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (!(aTargetArea == aOriginArea))` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (!(aTargetArea == aOriginArea))` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (aTargetNode != itemForPlacement)` → `container.insertBefore()`
- 参照: `aEvent.target.ownerDocument`, `aOriginArea.id`, `aTargetArea.id`, `aTargetNode.className`, `aTargetNode.id`, `aTargetNode.nodeName`, `aTargetNode.parentNode`, `draggedItem.hidden`, `draggedItem.parentNode`, `draggedWrapper.parentNode`, `itemForPlacement.firstElementChild`, `itemForPlacement.firstElementChild.id`, `itemForPlacement.id`, `itemForPlacement.nodeName`, `itemForPlacement.parentNode`, `itemForPlacement.parentNode.nextElementSibling`, `itemForPlacement.parentNode.nodeName`, `placement.position`, `this.visiblePalette`

## CustomizeMode.#onDragLeave()
- 位置: L2990-3006
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `__dumpDragData()`, `this.#isUnwantedDragDrop()`
- 条件付き依存: `if (this.#dragOverItem && aEvent.target == aEvent.currentTarget)` → `this.#cancelDragActive()`
- 参照: `aEvent.currentTarget`, `aEvent.target`, `this.#dragOverItem`

## CustomizeMode.#onDragEnd()
- 位置: L3014-3057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `__dumpDragData()`, `aEvent.dataTransfer.mozGetDataAt()`, `aEvent.dataTransfer.mozTypesAt()`, `document.getElementById()`, `lazy.DragPositionManager.stop()`, `this.#isUnwantedDragDrop()`, `this.#window.clearTimeout()`
- 条件付き依存: `if (draggedWrapper)` → `draggedWrapper.removeAttribute()`
- 条件付き依存: `if (draggedWrapper)` → `draggedWrapper.closest()`
- 条件付き依存: `if (toolbarParent)` → `toolbarParent.style.removeProperty()`
- 条件付き依存: `if (this.#dragOverItem)` → `this.#cancelDragActive()`
- 参照: `aEvent.target.ownerDocument`, `document.documentElement.id`, `draggedWrapper.hidden`, `this.#dragOverItem`, `this._dragInitializeTimeout`, `this._initializeDragAfterMove`

## CustomizeMode.#isUnwantedDragDrop()
- 位置: L3069-3086
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aEvent.dataTransfer.mozSourceNode`, `mozSourceNode.documentGlobal`, `this.#skipSourceNodeCheck`, `this.#window`

## CustomizeMode.#setDragActive()
- 位置: L3107-3156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDraggedOverItem.getAttribute()`
- 条件付き依存: `if (aDraggedOverItem.getAttribute("dragover") != aValue)` → `aDraggedOverItem.setAttribute()`
- 条件付き依存: `if (aDraggedOverItem.getAttribute("dragover") != aValue)` → `window.document.getElementById()`
- 条件付き依存: `if (aPlace == "palette")` → `this.#setGridDragActive()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `this.#getCustomizableParent()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `gDraggingInToolbars.has()`
- 条件付き依存: `if (!gDraggingInToolbars.has(targetArea.id))` → `gDraggingInToolbars.add()`
- 条件付き依存: `if (!gDraggingInToolbars.has(targetArea.id))` → `this.$()`
- 条件付き依存: `if (!gDraggingInToolbars.has(targetArea.id))` → `this.#getCustomizableParent()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `this.#getDragItemSize()`
- 条件付き依存: `if (aValue == "before")` → `layoutSide.toLowerCase()`
- 条件付き依存: `if (!(aValue == "before"))` → `layoutSide.toLowerCase()`
- 条件付き依存: `if (makeSpaceImmediately)` → `aDraggedOverItem.setAttribute()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `aDraggedOverItem.style.removeProperty()`
- 条件付き依存: `if (makeSpaceImmediately)` → `aDraggedOverItem.getBoundingClientRect()`
- 条件付き依存: `if (makeSpaceImmediately)` → `aDraggedOverItem.removeAttribute()`
- 参照: `aDraggedOverItem.documentGlobal`, `aDraggedOverItem.style`, `targetArea.id`

## CustomizeMode.#cancelDragActive()
- 位置: L3171-3212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getAreaType()`, `this.#getCustomizableParent()`
- 条件付き依存: `if (currentArea != nextArea)` → `currentArea.removeAttribute()`
- 条件付き依存: `if (aNoTransition)` → `aDraggedOverItem.setAttribute()`
- 条件付き依存: `if (areaType)` → `aDraggedOverItem.removeAttribute()`
- 条件付き依存: `if (areaType)` → `aDraggedOverItem.style.removeProperty()`
- 条件付き依存: `if (aNoTransition)` → `aDraggedOverItem.getBoundingClientRect()`
- 条件付き依存: `if (aNoTransition)` → `aDraggedOverItem.removeAttribute()`
- 条件付き依存: `if (!(areaType))` → `aDraggedOverItem.removeAttribute()`
- 条件付き依存: `if (!(areaType))` → `lazy.DragPositionManager.getManagerForArea()`
- 条件付き依存: `if (!(areaType))` → `positionManager.clearPlaceholders()`
- 参照: `currentArea.id`

## CustomizeMode.#setGridDragActive()
- 位置: L3223-3236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.DragPositionManager.getManagerForArea()`, `positionManager.insertPlaceholder()`, `this.#getCustomizableParent()`, `this.#getDragItemSize()`, `this.$()`
- 参照: `aDraggedItem.id`

## CustomizeMode.#getDragItemSize()
- 位置: L3249-3313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDraggedItem.parentNode.getBoundingClientRect()`, `itemMap.get()`, `itemMap.set()`, `this.#dragSizeMap.get()`, `this.#dragSizeMap.has()`, `this.#getCustomizableParent()`
- 条件付き依存: `if (!this.#dragSizeMap.has(aDraggedItem))` → `this.#dragSizeMap.set()`
- 条件付き依存: `if (targetArea != currentArea)` → `aDragOverNode.parentNode.insertBefore()`
- 条件付き依存: `if (targetArea != currentArea)` → `CustomizableUI.getAreaType()`
- 条件付き依存: `if (targetArea != currentArea)` → `aDraggedItem.hasAttribute()`
- 条件付き依存: `if (targetArea != currentArea)` → `aDraggedItem.getAttribute()`
- 条件付き依存: `if (areaType)` → `aDraggedItem.setAttribute()`
- 条件付き依存: `if (targetArea != currentArea)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (targetArea != currentArea)` → `CustomizableUI.onWidgetDrag()`
- 条件付き依存: `if (targetArea != currentArea)` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (targetArea != currentArea)` → `currentParent.insertBefore()`
- 条件付き依存: `if (currentType === false)` → `aDraggedItem.removeAttribute()`
- 条件付き依存: `if (!(currentType === false))` → `aDraggedItem.setAttribute()`
- 条件付き依存: `if (targetArea != currentArea)` → `this.createOrUpdateWrapper()`
- 参照: `aDraggedItem.id`, `aDraggedItem.nextElementSibling`, `aDraggedItem.parentNode`, `aDraggedItem.parentNode.hidden`, `rect.height`, `rect.width`, `targetArea.id`, `this.#dragSizeMap`

## CustomizeMode.#getCustomizableParent()
- 位置: L3325-3341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.escape()`, `aElement.closest()`, `areas.map()`, `areas.map(a => "#" + CSS.escape(a)).join()`, `areas.push()`
- 条件付き依存: `if (aElement)` → `aElement.closest()`
- 条件付き依存: `if (containingPanelHolder)` → `containingPanelHolder.querySelector()`
- 参照: `CustomizableUI.areas`

## CustomizeMode.#getDragOverNode()
- 位置: L3365-3398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `Math.max()`, `Math.min()`, `expectedParent.contains()`, `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (aPlace == "toolbar" || aPlace == "panel")` → `aAreaElement.ownerDocument.elementFromPoint()`
- 条件付き依存: `if (!(aPlace == "toolbar" || aPlace == "panel"))` → `lazy.DragPositionManager.getManagerForArea()`
- 条件付き依存: `if (!(aPlace == "toolbar" || aPlace == "panel"))` → `positionManager.find()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.target`, `bounds.bottom`, `bounds.left`, `bounds.right`, `bounds.top`, `targetNode.parentNode`, `this._dragOffset.x`, `this._dragOffset.y`

## CustomizeMode.#onMouseDown()
- 位置: L3408-3417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.#getWrapper()`
- 条件付き依存: `if (item)` → `item.toggleAttribute()`
- 参照: `aEvent.button`, `aEvent.target`

## CustomizeMode.#onMouseUp()
- 位置: L3427-3436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`, `this.#getWrapper()`
- 条件付き依存: `if (item)` → `item.removeAttribute()`
- 参照: `aEvent.button`, `aEvent.target`

## CustomizeMode.#getWrapper()
- 位置: L3449-3457
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aElement.localName`, `aElement.parentNode`

## CustomizeMode.#findVisiblePreviousSiblingNode()
- 位置: L3474-3483
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aReferenceNode.firstElementChild.hidden`, `aReferenceNode.localName`, `aReferenceNode.previousElementSibling`

## CustomizeMode.#onPaletteContextMenuShowing()
- 位置: L3492-3498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.querySelector()`, `event.target.triggerNode.id.includes()`
- 参照: `event.target.querySelector(".customize-context-addToPanel").disabled`

## CustomizeMode.onPanelContextMenuShowing()
- 位置: L3508-3525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.documentGlobal.MozXULElement.insertFTLIfNeeded()`, `doc.getElementById()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `event.target.querySelectorAll()`, `event.target.querySelectorAll("[data-lazy-l10n-id]").forEach()`, `event.target.triggerNode.closest()`
- 参照: `doc.getElementById("customizationPanelItemContextMenuPin").hidden`, `doc.getElementById("customizationPanelItemContextMenuUnpin").hidden`, `event.target.ownerDocument`

## CustomizeMode.#checkForDownloadsClick()
- 位置: L3535-3542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if ( event.target.closest("#wrapper-downloads-button") && event.button == 0 )` → `event.view.gCustomizeMode.#showDownloadsAutoHidePanel()`
- 参照: `event.button`

## CustomizeMode.#setupDownloadAutoHideToggle()
- 位置: L3550-3552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.addEventListener()`
- 参照: `this.#checkForDownloadsClick`

## CustomizeMode.#teardownDownloadAutoHideToggle()
- 位置: L3558-3565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#window.removeEventListener()`, `this.$()`, `this.$(kDownloadAutohidePanelId).hidePopup()`
- 参照: `this.#checkForDownloadsClick`

## CustomizeMode.#maybeMoveDownloadsButtonToNavBar()
- 位置: L3572-3604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `navbarPlacements.indexOf()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `widget.includes()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 参照: `navbarPlacements.length`, `this.#moveDownloadsButtonToNavBar`, `this.#window.DownloadsButton.autoHideDownloadsButton`

## CustomizeMode.#showDownloadsAutoHidePanel()
- 位置: async L3614-3672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.closest()`, `doc.getElementById()`, `panel.hidePopup()`, `panel.openPopup()`
- 条件付き依存: `if (toolbarContainer && toolbarContainer.id == "nav-bar")` → `CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (toolbarContainer && toolbarContainer.id == "nav-bar")` → `navbarWidgets.indexOf()`
- 条件付き依存: `if (!(toolbarContainer && toolbarContainer.id == "nav-bar"))` → `this.#window.promiseDocumentFlushed()`
- 条件付き依存: `if (!(toolbarContainer && toolbarContainer.id == "nav-bar"))` → `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (this.#window.DownloadsButton.autoHideDownloadsButton)` → `checkbox.setAttribute()`
- 条件付き依存: `if (!(this.#window.DownloadsButton.autoHideDownloadsButton))` → `checkbox.removeAttribute()`
- 参照: `buttonBounds.left`, `buttonBounds.width`, `doc.documentElement`, `this.#customizing`, `this.#document`, `this.#window.DownloadsButton.autoHideDownloadsButton`, `this._wantToBeInCustomizeMode`, `toolbarContainer.id`, `windowBounds.width`

## CustomizeMode.#onDownloadsAutoHideChange()
- 位置: L3680-3687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.target.ownerDocument.getElementById()`
- 参照: `checkbox.checked`, `event.view.gCustomizeMode.#moveDownloadsButtonToNavBar`
- XPCOM: `Services.prefs`

## CustomizeMode.#customizeTouchBar()
- 位置: L3692-3697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/touchbarupdater;1"].getService()`, `updater.enterCustomizeMode()`
- 参照: `Ci.nsITouchBarUpdater`
- XPCOM: `nsITouchBarUpdater` / `@mozilla.org/widget/touchbarupdater;1`

## CustomizeMode.#togglePong()
- 位置: L3705-3726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.$()`
- 条件付き依存: `if (enabled)` → `this.visiblePalette.setAttribute()`
- 条件付き依存: `if (!this.uninitWhimsy)` → `this.#whimsypong()`
- 条件付き依存: `if (!(enabled))` → `this.visiblePalette.removeAttribute()`
- 条件付き依存: `if (this.uninitWhimsy)` → `this.uninitWhimsy()`
- 参照: `this.pongArena.hidden`, `this.uninitWhimsy`, `whimsyButton.checked`

## CustomizeMode.#whimsypong()
- 位置: L3735-3973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `document.createXULElement()`, `document.getElementById()`, `elements.arena.appendChild()`, `elements.arena.querySelector()`, `this.visiblePalette.querySelector()`, `window.requestAnimationFrame()`
- 参照: `el.id`, `elements.arena.querySelector(player).style.background`, `spacer.id`, `this.#document`, `this.#window`, `this.uninitWhimsy`

## update()
- 位置: L3736-3739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateBall()`, `updatePlayers()`

## updateBall()
- 位置: L3741-3776
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] < p1 || ball[0] > p1 + paddleWidth)) || (ball[1] >= gameSide && (ball[0] < p2 || ball[0] > p2 + paddleWidth)) )` → `updateScore()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.random()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.max()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.min()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.abs()`
- 条件付き依存: `if (Math.abs(ballDxDy[0]) == 6)` → `Math.sign()`
- 条件付き依存: `if (Math.abs(ballDxDy[0]) == 6)` → `Math.random()`

## updatePlayers()
- 位置: L3778-3809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `Math.sign()`
- 参照: `window.RTL_UI`

## updateScore()
- 位置: L3811-3820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ballDef.slice()`, `ballDxDyDef.slice()`

## draw()
- 位置: L3822-3855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elements["wp-lives"].setAttribute()`
- 条件付き依存: `if (arena.style.backgroundImage)` → `arena.style.backgroundImage.split()`
- 参照: `arena.style.backgroundImage`, `arena.style.backgroundImage.split(",").length`, `arena.style.backgroundPosition`, `arena.style.backgroundRepeat`, `arena.style.backgroundSize`, `elements.arena`, `elements["wp-ball"].style.transform`, `elements["wp-player1"].style.transform`, `elements["wp-player2"].style.transform`, `elements["wp-score"].textContent`, `window.RTL_UI`

## onkeydown()
- 位置: L3857-3880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keys.push()`
- 条件付き依存: `if (keys.length > 10)` → `keys.shift()`
- 条件付き依存: `if (codeEntered)` → `elements.arena.setAttribute()`
- 条件付き依存: `if (codeEntered)` → `document.querySelector()`
- 条件付き依存: `if (codeEntered)` → `spacer.setAttribute()`
- 参照: `event.which`, `keys.length`

## onkeyup()
- 位置: L3882-3887
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.which`

## uninit()
- 位置: L3889-3913
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `arena.firstChild.remove()`, `arena.removeAttribute()`, `arena.style.removeProperty()`, `document.querySelector()`, `document.removeEventListener()`, `spacer.removeAttribute()`
- 条件付き依存: `if (rAFHandle)` → `window.cancelAnimationFrame()`
- 参照: `arena.firstChild`, `elements.arena`

## animate()
- 位置: L3958-3970
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `draw()`, `update()`
- 条件付き依存: `if (quit)` → `elements["wp-lives"].setAttribute()`
- 条件付き依存: `if (quit)` → `elements.arena.setAttribute()`
- 条件付き依存: `if (!(quit))` → `window.requestAnimationFrame()`
- 参照: `elements["wp-score"].textContent`

## __dumpDragData()
- 位置: L3985-4016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 参照: `aEvent.dataTransfer`, `aEvent.type`, `aEvent[el].id`, `aEvent[el].localName`
