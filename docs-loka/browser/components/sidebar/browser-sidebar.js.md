# browser/components/sidebar/browser-sidebar.js

source: browser/components/sidebar/browser-sidebar.js
source-hash: 3a9925d2a3fa0c3338163ce47bce33f36f20c1c7
lines: 3051

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Promise.withResolvers()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## makeSidebar()
- 位置: L29-54
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (toolID)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (toolID)` → `this.handleToolBadges()`
- 参照: `sidebar.attention`

## sourceL10nEl()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## title()
- 位置: L34-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `element?.getAttribute()`

## registerPrefSidebar()
- 位置: L56-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `sidebar._updateMenus()`, `this._sidebars.set()`, `this.makeSidebar()`, `this.promiseInitialized.then()`
- 参照: `sidebar._updateMenus`

## sidebar._updateMenus()
- 位置: L61-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `window.dispatchEvent()`
- 条件付き依存: `if (!visible && this._state.command == commandID)` → `this.hide()`
- 条件付き依存: `if (visible && !menuItem)` → `this.createMenuItem()`
- 条件付き依存: `if (visible && !menuItem)` → `switcherMenuitem.setAttribute()`
- 条件付き依存: `if (visible && !menuItem)` → `switcherMenuitem.removeAttribute()`
- 条件付き依存: `if (visible && !menuItem)` → `this._switcherPanel.querySelector()`
- 条件付き依存: `if (visible && !menuItem)` → `separator.parentNode.insertBefore()`
- 条件付き依存: `if (!(visible && !menuItem))` → `switcherMenuitem?.remove()`
- 参照: `config.elementId`, `sidebar.menuId`, `this._state.command`, `this.lastOpenedId`, `viewItem.hidden`

## get()
- 位置: L102-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAIWindow()`
- 参照: `config.hideInAIWindow`, `sidebar._prefVisible`

## isAIWindow()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.AIWindow.isAIWindowActive()`

## sidebars()
- 位置: L113-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.generateSidebarsMap()`
- 参照: `this._sidebars`

## generateSidebarsMap()
- 位置: L121-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.makeSidebar()`, `this.registerPrefSidebar()`
- 条件付き依存: `if (this.sidebarRevampEnabled)` → `this.registerPrefSidebar()`
- 条件付き依存: `if (this.sidebarRevampEnabled)` → `this._sidebars.set()`
- 参照: `Glean.bookmarks.sidebarToggle`, `Glean.contextualManager.sidebarToggle`, `Glean.history.sidebarToggle`, `Glean.sidebar.bookmarksIconClick`, `Glean.sidebar.chatbotIconClick`, `Glean.sidebar.historyIconClick`, `Glean.sidebar.openTabsIconClick`, `Glean.sidebar.passwordsIconClick`, `Glean.sidebar.syncedTabsIconClick`, `Glean.sidebarCustomize.panelToggle`, `this._sidebars`, `this.sidebarRevampEnabled`, `this.updatedBookmarksPanelEnabled`

## toolsAndExtensions()
- 位置: L288-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toolsAndExtensions.set()`, `this.getExtensions()`, `this.getExtensions().forEach()`, `this.getTools()`, `this.getTools().forEach()`
- 参照: `extension.commandID`, `this._toolsAndExtensions`, `tool.commandID`

## browser()
- 位置: L305-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._browser`

## _pinnedTabsContainer()
- 位置: L331-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._pinnedTabsContainerNode`

## _pinnedTabsItemsWrapper()
- 位置: L343-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._pinnedTabsContainer.shadowRoot.querySelector()`
- 参照: `this._pinnedTabsItemsWrapperNode`

## _pinnedTabsSplitter()
- 位置: L356-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._pinnedTabsSplitterNode`

## _title()
- 位置: L365-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.__title`

## markSessionRestoreStateReceived()
- 位置: L407-409
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._sessionRestoreStateReceived`

## promiseInitialized()
- 位置: L412-414
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._initDeferred.promise`

## initialized()
- 位置: L416-418
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._inited`

## uninitializing()
- 位置: L420-422
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._uninitializing`

## inSingleTabWindow()
- 位置: L424-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.document.documentElement.hasAttribute()`
- 参照: `window.toolbar.visible`

## sidebarContainer()
- 位置: L432-438
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._sidebarContainer)` → `document.getElementById()`
- 参照: `this._sidebarContainer`

## sidebarMain()
- 位置: L440-445
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._sidebarMain)` → `document.querySelector()`
- 参照: `this._sidebarMain`

## contentArea()
- 位置: L447-452
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._contentArea)` → `document.getElementById()`
- 参照: `this._contentArea`

## toolbarButton()
- 位置: L454-459
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._toolbarButton)` → `document.getElementById()`
- 参照: `this._toolbarButton`

## isLauncherDragging()
- 位置: L461-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._launcherSplitter.getAttribute()`

## isPinnedTabsDragging()
- 位置: L465-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._pinnedTabsSplitter.getAttribute()`

## sidebarTools()
- 位置: L469-471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sidebarRevampTools.split()`
- 参照: `this.sidebarRevampTools`

## sidebarExtensions()
- 位置: L473-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.installedExtensions.split()`
- 参照: `this.installedExtensions`

## launcherSplitter()
- 位置: L477-479
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._launcherSplitter`

## init()
- 位置: L481-647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Object.hasOwn()`, `Services.prefs.getBoolPref()`, `currentMenuItems.has()`, `document.documentElement.hasAttribute()`, `document.getElementById()`, `this._fullscreenObserver.observe()`, `this._handleLauncherResize()`, `this.setPosition()`, `this.sidebars.entries()`
- 条件付き依存: `if (!this._splitterAriaUpdateTask)` → `this._updateSplitterAriaAttributes()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "browser.tabs.allow_transparent_browser", false ) )` → `this.browser.setAttribute()`
- 条件付き依存: `if ( !Object.hasOwn(sidebar, "extensionId") && commandID !== "viewCustomizeSidebar" && !currentMenuItems.has(sidebar.menuId) )` → `this.createMenuItem()`
- 条件付き依存: `if ( !Object.hasOwn(sidebar, "extensionId") && commandID !== "viewCustomizeSidebar" && !currentMenuItems.has(sidebar.menuId) )` → `menubar.appendChild()`
- 条件付き依存: `if (this._mainResizeObserver)` → `this._mainResizeObserver.disconnect()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `customElements.get()`
- 条件付き依存: `if (!customElements.get("sidebar-main"))` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `window.addEventListener()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `this._state.initializeState()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `document.getElementById()`
- 条件付き依存: `if (!this._mainResizeObserverAdded)` → `this._mainResizeObserver.observe()`
- 条件付き依存: `if (!this._browserResizeObserver)` → `this._splitter.addEventListener()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `this._enablePinnedTabsSplitterDragging()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `this.recordVisibilitySetting()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `this.recordPositionSetting()`
- 条件付き依存: `if (this.sidebarRevampEnabled && !BrowserHandler.kiosk)` → `this.recordTabsLayoutSetting()`
- 条件付き依存: `if (!(this.sidebarRevampEnabled && !BrowserHandler.kiosk))` → `document.getElementById()`
- 条件付き依存: `if (!this._switcherListenersAdded)` → `this._switcherCloseButton.addEventListener()`
- 条件付き依存: `if (!this._switcherListenersAdded)` → `this.hide()`
- 条件付き依存: `if (!this._switcherListenersAdded)` → `this._switcherTarget.addEventListener()`
- 条件付き依存: `if (!this._switcherListenersAdded)` → `this.toggleSwitcherPanel()`
- 条件付き依存: `if (!this._switcherListenersAdded)` → `this.handleKeydown()`
- 条件付き依存: `if (!(this.sidebarRevampEnabled && !BrowserHandler.kiosk))` → `this._disableLauncherDragging()`
- 条件付き依存: `if (!(this.sidebarRevampEnabled && !BrowserHandler.kiosk))` → `this._disablePinnedTabsDragging()`
- 条件付き依存: `if (CustomizableUI.verticalTabsEnabled)` → `this.toggleTabstrip()`
- 条件付き依存: `if (!this._localesObserverAdded)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._tabstripOrientationObserverAdded)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._aiWindowObserverAdded)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._windowRestoredObserverAdded)` → `Services.obs.addObserver()`
- 参照: `BrowserHandler.kiosk`, `CustomizableUI.verticalTabsEnabled`, `document.documentElement`, `document.getElementById("sidebar-header").hidden`, `item.id`, `menubar.childNodes`, `sidebar.menuId`, `this.SidebarManager`, `this.SidebarState`, `this._aiWindowObserverAdded`, `this._box`, `this._browserResizeObserver`, `this._escapedWhileHovered`, `this._fullscreenObserver`, `this._inited`, `this._launcherSplitter`, `this._localesObserverAdded`, `this._mainResizeObserver`, `this._mainResizeObserverAdded`, `this._mouseLeftSinceEscape`, `this._openPopups`, `this._reversePositionButton`, `this._sidebarMainKeydownHandler`, `this._splitter`, `this._splitterAriaUpdateTask`, `this._state`, `this._state.navToolboxCollapsed`, `this._switcherArrow`, `this._switcherCloseButton`, `this._switcherListenersAdded`, `this._switcherPanel`, `this._switcherTarget`, `this._tabstripOrientationObserverAdded`, `this._windowRestoredObserverAdded`, `this.revampComponentsLoaded`, `this.sidebarContainer`, `this.sidebarRevampEnabled`
- XPCOM: `Services.obs` / `Services.prefs`

## this._sidebarMainKeydownHandler()
- 位置: L565-569
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.key === "Escape")` → `this.collapseOnEscape()`
- 参照: `e.key`

## this._browserResizeObserver()
- 位置: L583-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.resize.record()`, `Math.round()`, `this._recordBrowserSize()`, `this.browser.getBoundingClientRect()`
- 参照: `this._browserWidth`, `this.browser.getBoundingClientRect().width`, `window.innerWidth`

## uninit()
- 位置: L649-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `Services.obs.removeObserver()`, `Services.wm.getEnumerator()`, `enumerator.hasMoreElements()`, `this._disableLauncherDragging()`, `this._disablePinnedTabsDragging()`, `this._splitter.removeEventListener()`, `this._splitterAriaUpdateTask.finalize()`
- 条件付き依存: `if (this._fullscreenObserver)` → `this._fullscreenObserver.disconnect()`
- 条件付き依存: `if (!enumerator.hasMoreElements())` → `xulStore.persist()`
- 条件付き依存: `if (!enumerator.hasMoreElements())` → `this.getUIState()`
- 条件付き依存: `if (!enumerator.hasMoreElements())` → `this.SidebarManager.setBackupState()`
- 条件付き依存: `if (this._sidebarMainKeydownHandler)` → `window.removeEventListener()`
- 条件付き依存: `if (this._observer)` → `this._observer.disconnect()`
- 条件付き依存: `if (this._mainResizeObserver)` → `this._mainResizeObserver.disconnect()`
- 条件付き依存: `if (this._maxWidthUpdateTask)` → `this._maxWidthUpdateTask.finalize()`
- 条件付き依存: `if (this.revampComponentsLoaded)` → `this.sidebarMain.remove()`
- 参照: `Services.xulStore`, `this._aiWindowObserverAdded`, `this._browserResizeObserver`, `this._fullscreenObserver`, `this._mainResizeObserver`, `this._maxWidthUpdateTask`, `this._observer`, `this._sidebarMainKeydownHandler`, `this._splitterAriaUpdateTask`, `this._tabstripOrientationObserverAdded`, `this._title`, `this._uninitializing`, `this._windowRestoredObserverAdded`, `this.revampComponentsLoaded`
- XPCOM: `Services.obs` / `Services.wm` / `Services.xulStore`

## _handleLauncherResize()
- 位置: L715-723
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._launcherCollapsedWidthStale)` → `this.refreshLauncherCollapsedWidth()`
- 参照: `entry.borderBoxSize`, `entry.borderBoxSize[0].inlineSize`, `this._launcherCollapsedWidthStale`, `this._state.launcherDragActive`, `this._state.launcherWidth`, `this.isLauncherDragging`

## requestMaxWidthUpdate()
- 位置: L725-733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maxWidthUpdateTask.arm()`
- 条件付き依存: `if (!this._maxWidthUpdateTask)` → `this._updateLauncherAndPanelMaxWidths()`
- 参照: `this._maxWidthUpdateTask`

## _updateLauncherAndPanelMaxWidths()
- 位置: async L739-762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`, `getComputedStyle()`, `launcherEl.getBoundingClientRect()`, `parseFloat()`, `window.promiseDocumentFlushed()`
- 条件付き依存: `if ( expandOnHoverEnabled || !this._state.launcherExpanded || !this._state.panelOpen )` → `launcherEl.style.removeProperty()`
- 条件付き依存: `if ( expandOnHoverEnabled || !this._state.launcherExpanded || !this._state.panelOpen )` → `panelEl.style.removeProperty()`
- 参照: `getComputedStyle(panelEl).minWidth`, `launcherEl.getBoundingClientRect().width`, `launcherEl.style.maxWidth`, `panelEl.style.maxWidth`, `this._box`, `this._state.launcherExpanded`, `this._state.panelOpen`, `this.sidebarContainer`

## getUIState()
- 位置: L764-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._state.getProperties()`
- 参照: `this.inSingleTabWindow`

## updateUIState()
- 位置: async L777-802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._state.loadCurrentState()`, `this.sidebars.has()`, `this.updateToolbarButton()`, `this.waitUntilStable()`
- 条件付き依存: `if (this.sidebarRevampVisibility === "expand-on-hover")` → `this.toggleExpandOnHover()`
- 参照: `state.command`, `state.hidden`, `state.panelOpen`, `this._initialUIStateUpdated`, `this._launcherStateAtOpen`, `this.currentID`, `this.sidebarRevampVisibility`

## toggleVerticalTabs()
- 位置: L807-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- 参照: `this.sidebarVerticalTabsEnabled`
- XPCOM: `Services.prefs`

## observe()
- 位置: L817-855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.promiseInitialized.then()`, `this.toggleTabstrip()`
- 条件付き依存: `if (this.isOpen)` → `this.hide()`
- 条件付き依存: `if (this.isOpen)` → `this.showInitially()`
- 条件付き依存: `if (this.revampComponentsLoaded)` → `this.sidebarMain.requestUpdate()`
- 条件付き依存: `if (subject == window)` → `this._initDeferred.resolve()`
- 条件付き依存: `if (subject == window)` → `this.sidebars.values()`
- 条件付き依存: `if (subject == window)` → `sidebar._updateMenus()`
- 参照: `this.isOpen`, `this.lastOpenedId`, `this.revampComponentsLoaded`

## observeTitleChanges()
- 位置: L863-881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `observer.disconnect()`, `observer.observe()`
- 条件付き依存: `if (!observer)` → `this.sidebars.get()`
- 参照: `this._observer`, `this.lastOpenedId`, `this.sidebars.get(this.lastOpenedId)?.title`, `this.title`

## toggleSwitcherPanel()
- 位置: L886-895
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this._switcherPanel.state == "open" || this._switcherPanel.state == "showing" )` → `this.hideSwitcherPanel()`
- 条件付き依存: `if (this._switcherPanel.state == "closed")` → `this.showSwitcherPanel()`
- 参照: `this._switcherPanel.state`

## getRevampSwitcherItems()
- 位置: async L906-927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.push()`, `resolveLabel()`, `this.getExtensions()`, `this.getTools()`, `this.getTools().filter()`, `this.sidebars.get()`
- 条件付き依存: `if (customize)` → `items.push()`
- 条件付き依存: `if (customize)` → `resolveLabel()`
- 参照: `customize.revampL10nId`, `ext.tooltiptext`, `ext.view`, `t.hidden`, `tool.l10nId`, `tool.view`

## resolveLabel()
- 位置: async L907-910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatMessages()`, `message?.attributes?.find()`
- 参照: `a.name`, `message?.attributes?.find(a => a.name === "label")?.value`

## handleKeydown()
- 位置: L934-950
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`, `this.hideSwitcherPanel()`, `this.toggleSwitcherPanel()`
- 参照: `event.key`

## hideSwitcherPanel()
- 位置: L952-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._switcherPanel.hidePopup()`

## showSwitcherPanel()
- 位置: L956-979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNavigatorBundle.getString()`, `this._reversePositionButton.setAttribute()`, `this._switcherPanel.addEventListener()`, `this._switcherPanel.openPopup()`, `this._switcherTarget.classList.add()`, `this._switcherTarget.classList.remove()`, `this._switcherTarget.setAttribute()`
- 参照: `this._positionStart`, `this._switcherPanel.hidden`, `this._switcherTarget`

## updateShortcut()
- 位置: L981-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menuitem.removeAttribute()`, `this._switcherPanel?.querySelector()`

## reversePosition()
- 位置: L994-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- 参照: `this.POSITION_START_PREF`, `this._positionStart`
- XPCOM: `Services.prefs`

## setPosition()
- 位置: L1002-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...browser.children].forEach()`, `contentArea.toggleAttribute()`, `document.getElementById()`, `document.querySelector()`, `sidebarContainer.toggleAttribute()`, `sidebarMain.requestUpdate()`, `sidebarMain.toggleAttribute()`, `this._box.toggleAttribute()`, `this.hideSwitcherPanel()`, `this.toolbarButton.toggleAttribute()`
- 条件付き依存: `if (content && content.updatePosition)` → `content.updatePosition()`
- 参照: `SidebarController.browser.contentWindow`, `browser.children`, `children.length`, `content.updatePosition`, `node.style.order`, `this._positionStart`, `this.toolbarButton`

## toggleRevampSidebar()
- 位置: async L1039-1080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebar.hasOwnProperty()`, `this._sidebars.get()`, `this.generateSidebarsMap()`, `this.init()`, `this.sidebars.entries()`, `this.sidebars.set()`, `this.updateToolbarButton()`
- 条件付き依存: `if (wasOpen)` → `this.hide()`
- 条件付き依存: `if (sidebar.hasOwnProperty("extensionId"))` → `extensionsArr.push()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `document.querySelector()`
- 条件付き依存: `if (wasOpen)` → `this.toggle()`
- 参照: `cpmMenuItem.hidden`, `document.getElementById("sidebar-header").hidden`, `extension.commandID`, `extension.sidebar`, `this.DEFAULT_SIDEBAR_ID`, `this._inited`, `this._state.launcherVisible`, `this.isOpen`, `this.lastOpenedId`, `this.promiseInitialized`, `this.sidebarRevampEnabled`, `this.sidebars`

## getAdoptedStateFromWindow()
- 位置: L1089-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sourceController._state?.getProperties()`
- 参照: `sourceController._box`, `sourceController.inPopup`, `sourceWindow.SidebarController`

## windowPrivacyMatches()
- 位置: L1108-1113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`

## startDelayedLoad()
- 位置: async L1118-1189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.SidebarManager.getBackupState()`, `this._box.getAttribute()`, `this._initDeferred.resolve()`, `this.updateUIState()`
- 条件付き依存: `if (this.inSingleTabWindow)` → `this._initDeferred.resolve()`
- 条件付き依存: `if (sourceWindow)` → `this.windowPrivacyMatches()`
- 条件付き依存: `if ( sourceWindow.closed || sourceWindow.location.protocol != "chrome:" || (!this.sidebarRevampEnabled && !this.windowPrivacyMatches(sourceWindow, window)) )` → `this._initDeferred.resolve()`
- 条件付き依存: `if (sourceWindow)` → `this.getAdoptedStateFromWindow()`
- 条件付き依存: `if (stateToApply)` → `this.updateUIState()`
- 条件付き依存: `if (stateToApply)` → `this._initDeferred.resolve()`
- 条件付き依存: `if (this._initialUIStateUpdated)` → `this._initDeferred.resolve()`
- 条件付き依存: `if (wasOpen)` → `this.sidebars.has()`
- 条件付き依存: `if (wasOpen && commandID && this.sidebars.has(commandID))` → `this.showInitially()`
- 条件付き依存: `if (!(wasOpen && commandID && this.sidebars.has(commandID)))` → `this._box.removeAttribute()`
- 参照: `sourceWindow.closed`, `sourceWindow.location.protocol`, `this._initialUIStateUpdated`, `this._sessionRestoreStateReceived`, `this._state.command`, `this._state.launcherVisible`, `this.inSingleTabWindow`, `this.lastOpenedId`, `this.sidebarRevampEnabled`, `window.opener`

## _fireShowEvent()
- 位置: L1195-1198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._switcherTarget.dispatchEvent()`

## _recordBrowserSize()
- 位置: L1203-1207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.width.set()`, `this._splitterAriaUpdateTask.arm()`, `this.browser.getBoundingClientRect()`
- 参照: `this._browserWidth`, `this.browser.getBoundingClientRect().width`

## _updateSplitterAriaAttributes()
- 位置: L1213-1231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `parseFloat()`, `splitter.setAttribute()`, `window.getComputedStyle()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!this._state.panelOpen)` → `splitter.removeAttribute()`
- 参照: `style.maxWidth`, `style.minWidth`, `this._box`, `this._splitter`, `this._state.panelOpen`, `this._state.panelWidth`, `window.windowUtils.getBoundsWithoutFlushing(this._box).width`

## _fireFocusedEvent()
- 位置: L1239-1242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browser.contentWindow.dispatchEvent()`

## isOpen()
- 位置: L1247-1249
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._box`, `this._box.hidden`

## currentID()
- 位置: L1254-1256
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state.command`, `this.isOpen`

## currentContextMenu()
- 位置: L1261-1267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.sidebars.get()`
- 参照: `sidebar.contextMenuId`, `this.currentID`

## launcherVisible()
- 位置: L1269-1271
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state?.launcherVisible`

## launcherEverVisible()
- 位置: L1273-1275
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state?.launcherEverVisible`

## title()
- 位置: L1277-1279
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._title.value`

## title()
- 位置: L1281-1283
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._title.value`

## toggle()
- 位置: L1295-1342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `this.show()`, `this.sidebars.has()`
- 条件付き依存: `if ( CustomizationHandler.isCustomizing() || CustomizationHandler.isExitingCustomizeMode )` → `Promise.resolve()`
- 条件付き依存: `if (this.sidebarRevampEnabled && this.sidebars.size)` → `this.sidebars.keys().next()`
- 条件付き依存: `if (this.sidebarRevampEnabled && this.sidebars.size)` → `this.sidebars.keys()`
- 条件付き依存: `if (this.isOpen && commandID == this.currentID)` → `this.hide()`
- 条件付き依存: `if (this.isOpen && commandID == this.currentID)` → `this.updateToolbarButton()`
- 条件付き依存: `if (this.isOpen && commandID == this.currentID)` → `Promise.resolve()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `document.querySelector()`
- 参照: `CustomizationHandler.isExitingCustomizeMode`, `cpmMenuItem.hidden`, `this.DEFAULT_SIDEBAR_ID`, `this._state.command`, `this._state.launcherHiddenWithPanel`, `this.currentID`, `this.isOpen`, `this.lastOpenedId`, `this.sidebarRevampEnabled`, `this.sidebars.keys().next().value`, `this.sidebars.size`

## _getRects()
- 位置: L1344-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `animatingElements.map()`, `e.getBoundingClientRect()`, `e.getBoundingClientRect().toJSON()`
- 参照: `e.hidden`

## waitUntilStable()
- 位置: async L1356-1368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`
- 条件付き依存: `if (this._ongoingAnimations?.length)` → `tasks.push()`
- 条件付き依存: `if (this._ongoingAnimations?.length)` → `this._ongoingAnimations.map()`
- 参照: `animation.finished`, `this._ongoingAnimations?.length`, `this.sidebarMain.updateComplete`, `this.sidebarRevampEnabled`

## _animateSidebarContainer()
- 位置: async L1370-1538
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `animations.map()`, `animations.push()`, `document.documentElement.hasAttribute()`, `document.getElementById()`, `el.animate()`, `queueMicrotask()`, `resolve()`, `tabbox.toggleAttribute()`, `this._box.toggleAttribute()`, `this._getRects()`, `this.sidebarContainer.toggleAttribute()`, `this.sidebarMain.toggleAttribute()`
- 条件付き依存: `if (this._ongoingAnimations.length)` → `this._ongoingAnimations.forEach()`
- 条件付き依存: `if (this._ongoingAnimations.length)` → `a.cancel()`
- 条件付き依存: `if (this._ongoingAnimations.length)` → `resetElements()`
- 条件付き依存: `if (!this._state.launcherExpanded)` → `animations.push()`
- 条件付き依存: `if (!this._state.launcherExpanded)` → `this.sidebarMain.animate()`
- 条件付き依存: `if (!(!this._state.launcherExpanded))` → `animations.push()`
- 条件付き依存: `if (!(!this._state.launcherExpanded))` → `this.sidebarMain.animate()`
- 条件付き依存: `if (this._ongoingAnimations === animations)` → `resetElements()`
- 条件付き依存: `if (expandOnHoverEnabled)` → `this._reconcileHoverState()`
- 参照: `a.finished`, `animatingElements.length`, `el.style`, `el.style.display`, `el.style.marginLeft`, `el.style.marginRight`, `el.style.maxWidth`, `el.style.minWidth`, `from.left`, `from.right`, `from.width`, `this._animationDurationMs`, `this._animationExpandOnHoverDurationMs`, `this._box`, `this._ongoingAnimations`, `this._ongoingAnimations.length`, `this._positionStart`, `this._splitter`, `this._state.launcherExpanded`, `this._state.launcherHiddenWithPanel`, `this.sidebarContainer`, `this.sidebarMain.updateComplete`, `to.left`, `to.right`, `to.width`

## resetElements()
- 位置: L1386-1402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabbox.toggleAttribute()`, `this._box.toggleAttribute()`, `this.sidebarContainer.toggleAttribute()`, `this.sidebarMain.toggleAttribute()`
- 参照: `el.style.display`, `el.style.marginLeft`, `el.style.marginRight`, `el.style.maxWidth`, `el.style.minWidth`

## handleToolbarButtonClick()
- 位置: async L1543-1602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["always-show", "expand-on-hover"].includes()`, `this._state.updateVisibility()`, `this.updateToolbarButton()`
- 条件付き依存: `if (this.sidebarRevampVisibility === "expand-on-hover")` → `this.toggleExpandOnHover()`
- 条件付き依存: `if (this._animationEnabled && !window.gReduceMotion)` → `this._animateSidebarContainer()`
- 条件付き依存: `if (expandOnToggle)` → `this._state.updateVisibility()`
- 条件付き依存: `if (expandOnToggle)` → `this.updateToolbarButton()`
- 条件付き依存: `if (this.isOpen)` → `this.hide()`
- 条件付き依存: `if (!(this.isOpen))` → `this.sidebars.has()`
- 条件付き依存: `if (!commandID || !this.sidebars.has(commandID))` → `this.sidebars.keys().next()`
- 条件付き依存: `if (!commandID || !this.sidebars.has(commandID))` → `this.sidebars.keys()`
- 条件付き依存: `if (!(this.isOpen))` → `this.show()`
- 条件付き依存: `if (this._state.launcherHiddenWithPanel)` → `this.updateToolbarButton()`
- 条件付き依存: `if (shouldShowLauncher && this._state.command)` → `this.show()`
- 条件付き依存: `if (!shouldShowLauncher)` → `this.hide()`
- 参照: `this._animationEnabled`, `this._state.command`, `this._state.launcherExpanded`, `this._state.launcherHiddenWithPanel`, `this._state.launcherVisible`, `this.inSingleTabWindow`, `this.isOpen`, `this.lastOpenedId`, `this.sidebarRevampVisibility`, `this.sidebarVerticalTabsEnabled`, `this.sidebars.keys().next().value`, `this.uninitializing`, `window.gReduceMotion`

## updateToolbarButton()
- 位置: L1607-1670
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(!this.sidebarRevampEnabled))` → `document.getElementById()`
- 条件付き依存: `if (!(!this.sidebarRevampEnabled))` → `ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (!(!this.sidebarRevampEnabled))` → `JSON.stringify()`
- 条件付き依存: `if (!(!this.sidebarRevampEnabled))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (isVerticalTabs)` → `toolbarButton.toggleAttribute()`
- 条件付き依存: `if (!(isVerticalTabs))` → `toolbarButton.toggleAttribute()`
- 条件付き依存: `if (!(!this.sidebarRevampEnabled))` → `this.handleToolBadges()`
- 参照: `this.inSingleTabWindow`, `this.isOpen`, `this.sidebarContainer.hidden`, `this.sidebarMain.expanded`, `this.sidebarRevampEnabled`, `this.sidebarRevampVisibility`, `this.toolbarButton`, `toolbarButton.checked`, `toolbarButton.dataset.l10nArgs`, `toolbarButton.dataset.l10nId`
- XPCOM: `Services.prefs`

## handleToolBadges()
- 位置: L1679-1723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `[...this.toolsAndExtensions.keys()].find()`, `this.SidebarManager.getBadgeTools()`, `this.toolsAndExtensions.get()`, `this.toolsAndExtensions.keys()`, `window.dispatchEvent()`
- 条件付き依存: `if (badgePref && isCurrentView && this.isOpen)` → `this.dismissSidebarBadge()`
- 条件付き依存: `if ( this.sidebarRevampEnabled && badgePref && !tool.disabled && !tool.hidden && isSidebarClosed )` → `this._showToolbarButtonBadge()`
- 条件付き依存: `if (!( this.sidebarRevampEnabled && badgePref && !tool.disabled && !tool.hidden && isSidebarClosed ))` → `this._clearToolbarButtonBadge()`
- 参照: `this._state?.command`, `this._state?.launcherVisible`, `this.isOpen`, `this.sidebarRevampEnabled`, `tool.disabled`, `tool.hidden`
- XPCOM: `Services.prefs`

## _isMenuPopupOpen()
- 位置: L1725-1732
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (popup.state !== "open" && popup.state !== "showing")` → `this._openPopups.delete()`
- 参照: `popup.state`, `this._openPopups`, `this._openPopups.size`

## _reconcileHoverState()
- 位置: L1739-1749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._checkIsHoveredOverLauncher()`, `this._isMenuPopupOpen()`
- 条件付き依存: `if (isHovered && !this._state.launcherExpanded)` → `this.onMouseEnter()`
- 条件付き依存: `if (!isHovered && this._state.launcherExpanded)` → `this._collapseLauncher()`
- 参照: `this._ongoingAnimations.length`, `this._state.launcherExpanded`

## _showToolbarButtonBadge()
- 位置: L1751-1754
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `badgeEl?.classList.add()`, `this.toolbarButton?.querySelector()`

## _clearToolbarButtonBadge()
- 位置: L1756-1759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `badgeEl?.classList.remove()`, `this.toolbarButton?.querySelector()`

## dismissSidebarBadge()
- 位置: L1766-1771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(prefName, false))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _enableLauncherDragging()
- 位置: L1776-1797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._launcherSplitter.addEventListener()`, `this._panelResizeObserver.observe()`
- 参照: `entry.borderBoxSize`, `entry.borderBoxSize[0].inlineSize`, `this._box`, `this._launcherDropHandler`, `this._panelResizeObserver`, `this._state.panelWidth`

## this._launcherDropHandler()
- 位置: L1789-1792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePinnedTabsHeightOnResize()`
- 参照: `this._state.launcherDragActive`

## _enablePinnedTabsSplitterDragging()
- 位置: L1802-1842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `requestAnimationFrame()`, `this._itemsWrapperResizeObserver.observe()`, `this._pinnedTabsContainer.hasAttribute()`, `this._pinnedTabsResizeObserver.observe()`, `this._pinnedTabsSplitter.addEventListener()`, `this.updatePinnedTabsHeightOnResize()`, `window.promiseDocumentFlushed()`
- 参照: `entry.contentBoxSize`, `entry.contentBoxSize[0].inlineSize`, `this._itemsWrapperResizeObserver`, `this._pinnedTabsContainer`, `this._pinnedTabsDropHandler`, `this._pinnedTabsItemsWrapper`, `this._pinnedTabsItemsWrapperWidth`, `this._pinnedTabsResizeObserver`, `this._pinnedTabsSplitter.hidden`, `this._state.pinnedTabsDragActive`, `this.isPinnedTabsDragging`

## this._pinnedTabsDropHandler()
- 位置: L1834-1835
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state.pinnedTabsDragActive`

## _disableLauncherDragging()
- 位置: L1847-1856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._launcherSplitter.removeEventListener()`
- 条件付き依存: `if (this._panelResizeObserver)` → `this._panelResizeObserver.disconnect()`
- 参照: `this._launcherDropHandler`, `this._panelResizeObserver`

## _disablePinnedTabsDragging()
- 位置: L1861-1871
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._pinnedTabsResizeObserver)` → `this._pinnedTabsResizeObserver.disconnect()`
- 条件付き依存: `if (this._itemsWrapperResizeObserver)` → `this._itemsWrapperResizeObserver.disconnect()`
- 参照: `this._itemsWrapperResizeObserver`, `this._pinnedTabsResizeObserver`, `this._pinnedTabsSplitter`, `this._pinnedTabsSplitter.hidden`

## _loadSidebarExtension()
- 位置: L1873-1878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sidebars.get()`
- 条件付き依存: `if (typeof sidebar?.onload === "function")` → `sidebar.onload()`
- 参照: `sidebar?.onload`

## updatePinnedTabsHeightOnResize()
- 位置: L1880-1891
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._state.updatePinnedTabsHeight()`
- 参照: `this._pinnedTabsContainer.childElementCount`, `this.isLauncherDragging`, `this.isPinnedTabsDragging`

## updatePinnedTabsHeightAfterReflow()
- 位置: async L1893-1901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.promiseDocumentFlushed()`
- 条件付き依存: `if (!this.uninitializing)` → `this.updatePinnedTabsHeightOnResize()`
- 参照: `this._pinnedTabsContainer`, `this.sidebarVerticalTabsEnabled`, `this.uninitializing`

## refreshTools()
- 位置: L1906-1919
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sidebarRevampTools.split()`, `this.toolsAndExtensions.forEach()`, `tools.has()`
- 条件付き依存: `if (changed)` → `window.dispatchEvent()`
- 参照: `tool.disabled`, `tool.name`

## toggleTool()
- 位置: L1926-1943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.SidebarManager.updateToolsPref()`, `this.toolsAndExtensions.get()`, `window.dispatchEvent()`
- 条件付き依存: `if (!toggledTool.disabled)` → `this.toolsAndExtensions.delete()`
- 条件付き依存: `if (!toggledTool.disabled)` → `this.toolsAndExtensions.set()`
- 条件付き依存: `if (toggledTool.disabled)` → `this.dismissSidebarBadge()`
- 参照: `toggledTool.disabled`, `toggledTool.name`

## addOrUpdateExtension()
- 位置: L1945-1968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toolsAndExtensions.has()`
- 条件付き依存: `if (this.toolsAndExtensions.has(commandID))` → `this.toolsAndExtensions.get()`
- 条件付き依存: `if (this.toolsAndExtensions.has(commandID))` → `window.dispatchEvent()`
- 条件付き依存: `if (!(this.toolsAndExtensions.has(commandID)))` → `this.toolsAndExtensions.set()`
- 条件付き依存: `if (!(this.toolsAndExtensions.has(commandID)))` → `this.sidebarTools.includes()`
- 条件付き依存: `if (!(this.toolsAndExtensions.has(commandID)))` → `window.dispatchEvent()`
- 参照: `extension.extensionId`, `extension.iconUrl`, `extension.label`, `extensionToUpdate.iconUrl`, `extensionToUpdate.tooltiptext`, `this.inSingleTabWindow`

## registerExtension()
- 位置: L1977-2030
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("viewSidebarMenu").appendChild()`, `installedExtensions.includes()`, `sidebarTools.includes()`, `this._setExtensionAttributes()`, `this.addOrUpdateExtension()`, `this.createMenuItem()`, `this.sidebars.set()`
- 条件付き依存: `if (!installedExtensions.includes(name) && !sidebarTools.includes(name))` → `sidebarTools.push()`
- 条件付き依存: `if (!installedExtensions.includes(name) && !sidebarTools.includes(name))` → `installedExtensions.push()`
- 条件付き依存: `if (!installedExtensions.includes(name) && !sidebarTools.includes(name))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!installedExtensions.includes(name) && !sidebarTools.includes(name))` → `sidebarTools.join()`
- 条件付き依存: `if (!installedExtensions.includes(name) && !sidebarTools.includes(name))` → `installedExtensions.join()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `this.createMenuItem()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `switcherMenuitem.setAttribute()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `switcherMenuitem.removeAttribute()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `document.getElementById()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `separator.parentNode.insertBefore()`
- 参照: `props.extensionId`, `props.iconUrl`, `props.menuId`, `props.onload`, `props.title`, `sidebar.switcherMenuId`, `this.INSTALLED_EXTENSIONS`, `this.TOOLS_PREF`, `this.sidebarExtensions`, `this.sidebarRevampEnabled`, `this.sidebarTools`
- XPCOM: `Services.prefs`

## createMenuItem()
- 位置: L2039-2060
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `menuitem.addEventListener()`, `menuitem.hasAttribute()`, `menuitem.setAttribute()`, `this[menuitem.hasAttribute("type") ? "toggle" : "show"]()`
- 条件付き依存: `if (sidebar.classAttribute)` → `menuitem.setAttribute()`
- 条件付き依存: `if (sidebar.keyId)` → `menuitem.setAttribute()`
- 条件付き依存: `if (this.inSingleTabWindow)` → `menuitem.setAttribute()`
- 参照: `menuitem.dataset.l10nId`, `sidebar.classAttribute`, `sidebar.keyId`, `sidebar.menuId`, `sidebar.menuL10nId`, `this.inSingleTabWindow`

## setExtensionAttributes()
- 位置: L2071-2075
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setExtensionAttributes()`, `this.addOrUpdateExtension()`, `this.sidebars.get()`

## _setExtensionAttributes()
- 位置: L2077-2109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `updateAttributes()`
- 条件付き依存: `if (switcherMenu)` → `updateAttributes()`
- 条件付き依存: `if (this.isOpen && needsRefresh)` → `this.show()`
- 参照: `sidebar.iconUrl`, `sidebar.label`, `sidebar.menuId`, `sidebar.switcherMenuId`, `this.currentID`, `this.initialized`, `this.isOpen`, `this.title`

## updateAttributes()
- 位置: L2086-2095
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.setAttribute()`, `el.style.setProperty()`, `el.toggleAttribute()`
- 参照: `sidebar.iconUrl`, `sidebar.label`

## getExtensions()
- 位置: L2116-2135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `this.sidebars.entries()`
- 条件付き依存: `if (Object.hasOwn(sidebar, "extensionId"))` → `this.sidebarTools.includes()`
- 条件付き依存: `if (Object.hasOwn(sidebar, "extensionId"))` → `extensions.push()`
- 参照: `sidebar.extensionId`, `sidebar.iconUrl`, `sidebar.label`, `sidebar.name`

## getTools()
- 位置: L2142-2165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(toolsNameMap) .filter()`, `Object.keys(toolsNameMap) .filter(commandID => this.sidebars.get(commandID)) .map()`, `this.sidebarTools.includes()`, `this.sidebars.get()`
- 参照: `sidebar.iconUrl`, `sidebar.name`, `sidebar.revampL10nId`, `sidebar.toolContextMenuId`

## hidden()
- 位置: L2156-2158
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sidebar.visible`

## attention()
- 位置: L2159-2161
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sidebar.attention`

## removeExtension()
- 位置: L2172-2191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById(sidebar.menuId)?.remove()`, `document.getElementById(sidebar.switcherMenuId)?.remove()`, `this.sidebars.delete()`, `this.sidebars.get()`, `this.toolsAndExtensions.delete()`, `window.dispatchEvent()`
- 条件付き依存: `if (this.currentID === commandID)` → `this.hide()`
- 参照: `sidebar.menuId`, `sidebar.switcherMenuId`, `this.currentID`, `this.inSingleTabWindow`

## _canShow()
- 位置: L2199-2204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sidebars.get()`
- 参照: `sidebar.visible`

## show()
- 位置: async L2216-2247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._canShow()`, `this._fireFocusedEvent()`, `this._loadSidebarExtension()`, `this._recordPanelToggle()`, `this._show()`, `this._show(commandID).then()`, `this.dismissSidebarBadge()`, `this.updateToolbarButton()`
- 条件付き依存: `if (this.currentID && commandID !== this.currentID)` → `this._recordPanelToggle()`
- 条件付き依存: `if (triggerNode)` → `updateToggleControlLabel()`
- 参照: `this._launcherStateAtOpen`, `this._state.launcherVisible`, `this.currentID`, `this.inSingleTabWindow`

## showInitially()
- 位置: async L2257-2270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._canShow()`, `this._loadSidebarExtension()`, `this._recordPanelToggle()`, `this._show()`, `this._show(commandID).then()`
- 参照: `this.inSingleTabWindow`

## _show()
- 位置: L2279-2372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._box.setAttribute()`, `this.browser.contentWindow?.dispatchEvent()`, `this.browser.setAttribute()`, `this.selectMenuItem()`, `this.sidebars.get()`
- 条件付き依存: `if (this.sidebarRevampEnabled)` → `this._box.dispatchEvent()`
- 条件付き依存: `if (!(this.sidebarRevampEnabled))` → `this.hideSwitcherPanel()`
- 条件付き依存: `if (iconUrl)` → `this._switcherTarget.style.setProperty()`
- 条件付き依存: `if (!(iconUrl))` → `this._switcherTarget.style.removeProperty()`
- 条件付き依存: `if (contextMenuId)` → `this._box.setAttribute()`
- 条件付き依存: `if (!(contextMenuId))` → `this._box.removeAttribute()`
- 条件付き依存: `if (!this.sidebarRevampEnabled)` → `this.observeTitleChanges()`
- 条件付き依存: `if (this.browser.contentDocument.location.href != url)` → `this.browser.addEventListener()`
- 条件付き依存: `if (this.browser.loadingTimerID)` → `clearTimeout()`
- 条件付き依存: `if (this.browser.loadingTimerID)` → `resolve()`
- 条件付き依存: `if (this.browser.contentDocument.location.href != url)` → `setTimeout()`
- 条件付き依存: `if (this.browser.contentDocument.location.href != url)` → `resolve()`
- 条件付き依存: `if (this.browser.contentDocument.location.href != url)` → `this._fireShowEvent()`
- 条件付き依存: `if (this.browser.contentDocument.location.href != url)` → `this._recordBrowserSize()`
- 条件付き依存: `if (this.browser.contentDocument.location.href != url)` → `this.sidebars.get()`
- 条件付き依存: `if (sidebar?.permissions)` → `this._permissions.init()`
- 条件付き依存: `if (!(this.browser.contentDocument.location.href != url))` → `resolve()`
- 条件付き依存: `if (!(this.browser.contentDocument.location.href != url))` → `this._fireShowEvent()`
- 条件付き依存: `if (!(this.browser.contentDocument.location.href != url))` → `this._recordBrowserSize()`
- 参照: `sidebar?.permissions`, `this.SidebarPermissions`, `this._box.hidden`, `this._permissions`, `this._splitter.hidden`, `this._state.command`, `this._state.panelOpen`, `this.browser`, `this.browser.contentDocument.location.href`, `this.browser.loadingTimerID`, `this.lastOpenedId`, `this.sidebarRevampEnabled`, `this.title`

## hide()
- 位置: L2382-2443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selBrowser.focus()`, `this._box.removeAttribute()`, `this._recordPanelToggle()`, `this._splitterAriaUpdateTask.arm()`, `this.browser.contentWindow?.dispatchEvent()`, `this.browser.docShell?.createAboutBlankDocumentViewer()`, `this.browser.setAttribute()`, `this.hideSwitcherPanel()`, `this.selectMenuItem()`, `this.updateToolbarButton()`
- 条件付き依存: `if (this._launcherStateAtOpen !== undefined)` → `["hide-sidebar", "hide-on-close"].includes()`
- 条件付き依存: `if (this.sidebarRevampEnabled)` → `this._box.dispatchEvent()`
- 条件付き依存: `if (triggerNode)` → `updateToggleControlLabel()`
- 参照: `gBrowser.selectedBrowser`, `this._box.hidden`, `this._launcherStateAtOpen`, `this._splitter.hidden`, `this._state.command`, `this._state.launcherVisible`, `this._state.panelOpen`, `this.currentID`, `this.isOpen`, `this.lastOpenedId`, `this.sidebarRevampEnabled`, `this.sidebarRevampVisibility`, `willHideEvent.defaultPrevented`

## _recordPanelToggle()
- 位置: L2451-2472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `this.sidebars.get()`
- 条件付き依存: `if (isExtension)` → `WebExtensionPolicy.getByID()`
- 条件付き依存: `if (isExtension)` → `Glean.extension.sidebarToggle.record()`
- 条件付き依存: `if (isExtension)` → `AMTelemetry.getTrimmedString()`
- 条件付き依存: `if (sidebar.gleanEvent && sidebar.recordSidebarVersion)` → `sidebar.gleanEvent.record()`
- 条件付き依存: `if (sidebar.gleanEvent)` → `sidebar.gleanEvent.record()`
- 参照: `WebExtensionPolicy.getByID(addonId)?.name`, `sidebar.extensionId`, `sidebar.gleanEvent`, `sidebar.recordSidebarVersion`, `this.sidebarRevampEnabled`

## _checkIsHoveredOverLauncher()
- 位置: L2477-2486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MousePosTracker._callListener()`

## onMouseEnter()
- 位置: L2481-2481
- 役割: (未記入)
- 触るとき: (未記入)

## onMouseLeave()
- 位置: L2482-2482
- 役割: (未記入)
- 触るとき: (未記入)

## getMouseTargetRect()
- 位置: L2483-2483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getMouseTargetRect()`

## recordIconClick()
- 位置: L2494-2508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `this.sidebars.get()`
- 条件付き依存: `if (isExtension)` → `Glean.sidebar.addonIconClick.record()`
- 条件付き依存: `if (isExtension)` → `AMTelemetry.getTrimmedString()`
- 条件付き依存: `if (sidebar.gleanClickEvent)` → `sidebar.gleanClickEvent.record()`
- 参照: `sidebar.extensionId`, `sidebar.gleanClickEvent`

## selectMenuItem()
- 位置: L2514-2536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (id == commandID)` → `menu.setAttribute()`
- 条件付き依存: `if (triggerbutton)` → `triggerbutton.setAttribute()`
- 条件付き依存: `if (triggerbutton)` → `updateToggleControlLabel()`
- 条件付き依存: `if (!(id == commandID))` → `menu.removeAttribute()`
- 条件付き依存: `if (triggerbutton)` → `triggerbutton.removeAttribute()`
- 参照: `this.sidebars`

## toggleTabstrip()
- 位置: L2538-2575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `arrowScrollbox.getAttribute()`, `document.getElementById()`, `this.sidebarMain.requestUpdate()`, `verticalToolbar.toggleAttribute()`
- 条件付き依存: `if (toVerticalTabs)` → `arrowScrollbox.setAttribute()`
- 条件付き依存: `if (toVerticalTabs)` → `tabStrip.setAttribute()`
- 条件付き依存: `if (toVerticalTabs)` → `this._clearToolbarButtonBadge()`
- 条件付き依存: `if (!(toVerticalTabs))` → `arrowScrollbox.setAttribute()`
- 条件付き依存: `if (!(toVerticalTabs))` → `tabStrip.removeAttribute()`
- 条件付き依存: `if (!(toVerticalTabs))` → `tabStrip.setAttribute()`
- 参照: `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `gBrowser.tabContainer`, `tabStrip.arrowScrollbox`, `this._state.launcherExpanded`

## debouncedMouseEnter()
- 位置: L2577-2587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentArea.toggleAttribute()`, `document.getElementById()`, `this._box.toggleAttribute()`, `this._mouseEnterDeferred.resolve()`
- 条件付き依存: `if (this._animationEnabled && !window.gReduceMotion)` → `this._animateSidebarContainer()`
- 参照: `this._animationEnabled`, `this._state.launcherExpanded`, `this._state.launcherHoverActive`, `window.gReduceMotion`

## _collapseLauncher()
- 位置: L2589-2600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentArea.toggleAttribute()`, `document.getElementById()`, `this._box.toggleAttribute()`, `this._mouseEnterDeferred?.resolve()`, `this.mouseEnterTask?.disarm()`
- 条件付き依存: `if (this._animationEnabled && !window.gReduceMotion)` → `this._animateSidebarContainer()`
- 参照: `this._animationEnabled`, `this._state.launcherExpanded`, `this._state.launcherHoverActive`, `window.gReduceMotion`

## collapseOnEscape()
- 位置: L2602-2612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._collapseLauncher()`
- 参照: `this._escapedWhileHovered`, `this._mouseLeftSinceEscape`, `this._state.launcherExpanded`, `this.sidebarRevampVisibility`

## onMouseLeave()
- 位置: L2614-2628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._collapseLauncher()`, `this._isMenuPopupOpen()`
- 参照: `this._escapedWhileHovered`, `this._mouseLeftSinceEscape`, `this._ongoingAnimations.length`, `this._state.launcherExpanded`

## onMouseEnter()
- 位置: L2630-2658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `this._checkIsHoveredOverLauncher()`, `this._isMenuPopupOpen()`, `this.mouseEnterTask?.arm()`
- 条件付き依存: `if (isHovered)` → `this.debouncedMouseEnter()`
- 参照: `this._animationExpandOnHoverDelayDurationMs`, `this._escapedWhileHovered`, `this._mouseEnterDeferred`, `this._mouseLeftSinceEscape`, `this._ongoingAnimations.length`, `this._state.launcherExpanded`, `this.mouseEnterTask`

## expandOnHoverComplete()
- 位置: L2660-2662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 参照: `this._mouseEnterDeferred?.promise`

## refreshLauncherCollapsedWidth()
- 位置: L2664-2678
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`, `this.getUIState()`, `this.setLauncherCollapsedWidth()`
- 参照: `this._launcherCollapsedWidthStale`, `this._state`, `this.getUIState()?.launcherExpanded`

## setLauncherCollapsedWidth()
- 位置: async L2691-2716
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserEl.style.setProperty()`, `document.getElementById()`, `this._getRects()`, `this.getUIState()`, `this.waitUntilStable()`, `window.promiseDocumentFlushed()`
- 参照: `this._collapsedWidthMeasurementID`, `this._getRects([this.sidebarContainer])[0][1].width`, `this._state.launcherExpanded`, `this.getUIState().launcherExpanded`, `this.sidebarContainer`

## getMouseTargetRect()
- 位置: L2718-2732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `SidebarController.sidebarMain`, `launcherRect.bottom`, `launcherRect.left`, `launcherRect.right`, `launcherRect.top`, `this._positionStart`

## handleEvent()
- 位置: L2734-2753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.refreshLauncherCollapsedWidth()`
- 条件付き依存: `if (e.composedTarget.tagName !== "tooltip")` → `this._openPopups.add()`
- 条件付き依存: `if (e.composedTarget.tagName !== "tooltip")` → `this._openPopups.delete()`
- 条件付き依存: `if (e.composedTarget.tagName !== "tooltip")` → `this._reconcileHoverState()`
- 参照: `e.composedTarget`, `e.composedTarget.tagName`, `e.type`

## toggleExpandOnHover()
- 位置: async L2755-2804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.toggleAttribute()`
- 条件付き依存: `if (isEnabled)` → `this.waitUntilStable()`
- 条件付き依存: `if (isEnabled)` → `MousePosTracker.addListener()`
- 条件付き依存: `if (!isDragEnded)` → `this.setLauncherCollapsedWidth()`
- 条件付き依存: `if (isEnabled)` → `document.addEventListener()`
- 条件付き依存: `if (isEnabled)` → `window.addEventListener()`
- 条件付き依存: `if (!(isEnabled))` → `this._openPopups.clear()`
- 条件付き依存: `if (!(isEnabled))` → `MousePosTracker.removeListener()`
- 条件付き依存: `if (!this.mouseOverTask?.isFinalized)` → `this.mouseOverTask?.finalize()`
- 条件付き依存: `if (!(isEnabled))` → `document.removeEventListener()`
- 条件付き依存: `if (!(isEnabled))` → `window.removeEventListener()`
- 条件付き依存: `if (!(isEnabled))` → `this._state.updateToolsHeight()`
- 参照: `this.SidebarState`, `this._expandOnHoverToggleID`, `this._launcherCollapsedWidthStale`, `this._state`, `this._state .launcherExpanded`, `this.mouseOverTask?.isFinalized`, `this.sidebarMain.buttonsWrapper.style.height`

## recordVisibilitySetting()
- 位置: L2811-2819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.displaySettings.set()`
- 参照: `this.sidebarRevampVisibility`

## recordPositionSetting()
- 位置: L2826-2828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.positionSettings.set()`
- 参照: `this._positionStart`

## recordTabsLayoutSetting()
- 位置: L2835-2837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebar.tabsLayout.set()`
- 参照: `this.sidebarVerticalTabsEnabled`
