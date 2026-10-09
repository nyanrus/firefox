# browser/components/sidebar/sidebar-main.mjs

source: browser/components/sidebar/sidebar-main.mjs
source-hash: 315082705fcf30a62dabe9bf639d1a95f61b0bc7
lines: 974

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SidebarMain.fluentStrings()
- 位置: L55-63
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._fluentStrings`

## SidebarMain.constructor()
- 位置: L71-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.bottomActions`, `this.clickCounts`, `this.contextMenuTarget`, `this.expanded`, `this.open`, `this.overflowMenuOpen`, `this.selectedView`, `this.shouldShowOverflowButton`, `window.SidebarController.currentID`, `window.SidebarController.isOpen`

## SidebarMain.connectedCallback()
- 位置: L106-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.querySelector()`, `super.connectedCallback()`, `this._contextMenu.addEventListener()`, `this._contextMenu.querySelector()`, `this._sidebarBox.addEventListener()`, `this._sidebarContainer.addEventListener()`, `this._toolsOverflowMenu.addEventListener()`, `this._toolsOverflowMenu.querySelector()`, `this.createSplitter()`, `this.createToolsObservers()`, `this.setCustomize()`, `window.addEventListener()`
- 参照: `this._contextMenu`, `this._customizeSidebarMenuItem`, `this._enableVerticalTabsMenuItem`, `this._hideSidebarMenuItem`, `this._manageExtensionMenuItem`, `this._menuseparator`, `this._openTabsPreview`, `this._removeExtensionMenuItem`, `this._reportExtensionMenuItem`, `this._sidebarBox`, `this._sidebarContainer`, `this._toolsOverflowButtonGroup`, `this._toolsOverflowMenu`, `this._unpinExtensionMenuItem`

## SidebarMain.disconnectedCallback()
- 位置: L155-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this._contextMenu.removeEventListener()`, `this._sidebarBox.removeEventListener()`, `this._sidebarContainer.removeEventListener()`, `this._toolsIntersectionObserver?.disconnect()`, `this._toolsOverflowMenu.removeEventListener()`, `this._toolsResizeObserver?.disconnect()`, `this.ownerDocument .getElementById()`, `this.ownerDocument .getElementById("drag-to-pin-promo-card") ?.disconnectedCallback()`, `window.removeEventListener()`

## SidebarMain.isToolsDragging()
- 位置: L176-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toolsSplitter.getAttribute()`

## SidebarMain.createToolsObservers()
- 位置: L180-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `entries.some()`, `entry.target.getAttribute()`, `panelButtonGroup.querySelector()`, `this.toolsSplitter.addEventListener()`
- 条件付き依存: `if (!entry.isIntersecting && !buttonAlreadyAddedToOverflow)` → `this.createCopyButton()`
- 条件付き依存: `if (!entry.isIntersecting && !buttonAlreadyAddedToOverflow)` → `panelButtonGroup.querySelector()`
- 条件付き依存: `if (customizeCopy && view !== "viewCustomizeSidebar")` → `panelButtonGroup.insertBefore()`
- 条件付き依存: `if (!(customizeCopy && view !== "viewCustomizeSidebar"))` → `panelButtonGroup.appendChild()`
- 条件付き依存: `if (entry.target === this.buttonGroup.activeChild)` → `window.getComputedStyle()`
- 条件付き依存: `if (entry.isIntersecting && buttonAlreadyAddedToOverflow)` → `copyButton.remove()`
- 参照: `entry.isIntersecting`, `entry.target`, `entry.target.style.visibility`, `style.display`, `style.visibility`, `this._toolsDropHandler`, `this._toolsIntersectionObserver`, `this._toolsResizeObserver`, `this.buttonGroup`, `this.buttonGroup.activeChild`, `this.buttonGroup.children`, `this.isToolsDragging`, `this.shouldShowOverflowButton`, `window.SidebarController._state.toolsDragActive`, `window.SidebarController.sidebarVerticalTabsEnabled`

## this._toolsDropHandler()
- 位置: L254-255
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.SidebarController._state.toolsDragActive`

## SidebarMain.createSplitter()
- 位置: L259-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `toolsSplitter.setAttribute()`
- 参照: `this.toolsSplitter`

## SidebarMain.createCopyButton()
- 位置: L268-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `this.getEntrypointValues()`
- 条件付き依存: `if (!(view === "viewCustomizeSidebar"))` → `this.getToolsAndExtensions().get()`
- 条件付き依存: `if (!(view === "viewCustomizeSidebar"))` → `this.getToolsAndExtensions()`
- 条件付き依存: `if (newButtonValues)` → `newButton.classList.add()`
- 条件付き依存: `if (newButtonValues)` → `newButton.setAttribute()`
- 条件付き依存: `if (newButtonValues)` → `newButton.addEventListener()`
- 条件付き依存: `if (newButtonValues)` → `this.showView()`
- 条件付き依存: `if (newButtonValues)` → `this.resetPanelButtonValues()`
- 条件付き依存: `if (newButtonValues)` → `this._toolsOverflowMenu.hidePopup()`
- 条件付き依存: `if (newButtonValues)` → `newButtonValues.action.view?.includes()`
- 条件付き依存: `if (newButtonValues.action.view?.includes("-sidebar-action"))` → `newButton.setAttribute()`
- 条件付き依存: `if (newButtonValues.action.extensionId)` → `newButton.setAttribute()`
- 参照: `newButton.iconSrc`, `newButton.textContent`, `newButtonValues.action.extensionId`, `newButtonValues.action.iconUrl`, `newButtonValues.action.view`, `newButtonValues.actionLabel`, `newButtonValues.isActiveView`, `newButtonValues.tooltip`, `this.bottomActions`, `this.open`, `this.selectedView`

## SidebarMain.resetPanelButtonValues()
- 位置: L318-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `document.getElementById()`, `panelButton.getAttribute()`, `panelButton.setAttribute()`
- 参照: `panelButtonGroup.children`, `this.open`, `this.selectedView`

## SidebarMain.onSidebarPopupShowing()
- 位置: async L329-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["moz-button", "sidebar-main"].includes()`, `event.explicitOriginalTarget.getRootNode()`, `event.preventDefault()`, `this.contextMenuTarget?.className.includes()`, `this.contextMenuTarget?.getAttribute()`, `this.contextMenuTarget?.hasAttribute()`
- 条件付き依存: `if (!(["moz-button", "sidebar-main"].includes(targetHost?.localName)))` → `document .getElementById("vertical-tabs") .contains()`
- 条件付き依存: `if (!(["moz-button", "sidebar-main"].includes(targetHost?.localName)))` → `document .getElementById()`
- 条件付き依存: `if ( this.contextMenuTarget?.localName === "sidebar-main" && !window.SidebarController.sidebarVerticalTabsEnabled )` → `this.updateSidebarContextMenuItems()`
- 条件付き依存: `if ( this.contextMenuTarget?.getAttribute("extensionId") || this.contextMenuTarget?.className.includes("tab") || isToolbarTarget )` → `this.updateExtensionContextMenuItems()`
- 条件付き依存: `if (this.contextMenuTarget?.hasAttribute("contextMenu"))` → `this.hideExistingMenuItem()`
- 条件付き依存: `if (this.contextMenuTarget?.hasAttribute("contextMenu"))` → `this.contextMenuTarget.getAttribute()`
- 条件付き依存: `if (this.contextMenuTarget?.hasAttribute("contextMenu"))` → `this.buildToolContextMenuItems()`
- 条件付き依存: `if (this.contextMenuTarget?.hasAttribute("contextMenu"))` → `this._contextMenu.querySelectorAll()`
- 条件付き依存: `if (items?.length)` → `this._contextMenu.openPopupAtScreen()`
- 参照: `event.explicitOriginalTarget.flattenedTreeParentNode .flattenedTreeParentNode`, `event.explicitOriginalTarget.getRootNode().host`, `event.screenX`, `event.screenY`, `items?.length`, `targetHost?.localName`, `this.contextMenuTarget`, `this.contextMenuTarget?.localName`, `window.SidebarController.sidebarVerticalTabsEnabled`

## SidebarMain.buildToolContextMenuItems()
- 位置: async L383-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menu .querySelectorAll()`, `menu .querySelectorAll("[customized-tool='true']") .forEach()`, `node.remove()`
- 条件付き依存: `if (typeof builder === "function")` → `menu.appendChild.bind()`
- 条件付き依存: `if (typeof builder === "function")` → `builder()`
- 参照: `menu.appendChild`, `this._contextMenu`

## aichat()
- 位置: async L391-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.ml.chat.page"))` → `lazy.GenAI.buildAskChatMenu()`
- 参照: `this._contextMenu`, `window.gBrowser.selectedBrowser`
- XPCOM: `Services.prefs`

## menu.appendChild()
- 位置: L406-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.setAttribute()`, `originalAppendChild()`

## SidebarMain.hideToolMenuItems()
- 位置: L418-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customMenuItems.forEach()`, `this._contextMenu.querySelectorAll()`
- 参照: `item.hidden`

## SidebarMain.hideExistingMenuItem()
- 位置: L425-435
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._customizeSidebarMenuItem.hidden`, `this._enableVerticalTabsMenuItem.hidden`, `this._hideSidebarMenuItem.hidden`, `this._manageExtensionMenuItem.hidden`, `this._menuseparator.hidden`, `this._removeExtensionMenuItem.hidden`, `this._reportExtensionMenuItem.hidden`, `this._unpinExtensionMenuItem.hidden`

## SidebarMain.updateSidebarContextMenuItems()
- 位置: L437-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideToolMenuItems()`
- 参照: `this._customizeSidebarMenuItem.hidden`, `this._enableVerticalTabsMenuItem.hidden`, `this._hideSidebarMenuItem.hidden`, `this._manageExtensionMenuItem.hidden`, `this._menuseparator.hidden`, `this._removeExtensionMenuItem.hidden`, `this._reportExtensionMenuItem.hidden`, `this._unpinExtensionMenuItem.hidden`

## SidebarMain.updateExtensionContextMenuItems()
- 位置: async L449-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextMenuTarget.getAttribute()`, `this.hideToolMenuItems()`, `window.AddonManager?.getAddonByID()`
- 参照: `AddonManager.PERM_CAN_UNINSTALL`, `addon.permissions`, `this._customizeSidebarMenuItem.hidden`, `this._enableVerticalTabsMenuItem.hidden`, `this._hideSidebarMenuItem.hidden`, `this._manageExtensionMenuItem.disabled`, `this._manageExtensionMenuItem.hidden`, `this._menuseparator.hidden`, `this._removeExtensionMenuItem.disabled`, `this._removeExtensionMenuItem.hidden`, `this._reportExtensionMenuItem.disabled`, `this._reportExtensionMenuItem.hidden`, `this._unpinExtensionMenuItem.hidden`, `window.gAddonAbuseReportEnabled`

## SidebarMain.manageExtension()
- 位置: async L479-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextMenuTarget.getAttribute()`, `window.BrowserAddonUI.manageAddon()`

## SidebarMain.removeExtension()
- 位置: async L486-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextMenuTarget.getAttribute()`, `window.BrowserAddonUI.removeAddon()`

## SidebarMain.reportExtension()
- 位置: async L493-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextMenuTarget.getAttribute()`, `window.BrowserAddonUI.reportAddon()`

## SidebarMain.unpinExtension()
- 位置: L500-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextMenuTarget.getAttribute()`, `window.SidebarController.toggleTool()`

## SidebarMain.getImageUrl()
- 位置: L506-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.startsWith()`
- 条件付き依存: `if (!icon)` → `targetURI?.startsWith()`
- 参照: `window.IS_STORYBOOK`

## SidebarMain.getToolsAndExtensions()
- 位置: L526-528
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.SidebarController.toolsAndExtensions`

## SidebarMain.getLauncherActions()
- 位置: L530-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actions.splice()`, `this.getToolsAndExtensions()`, `this.getToolsAndExtensions().values()`
- 参照: `actions.length`, `this.bottomActions`, `this.expanded`, `window.SidebarController._positionStart`, `window.SidebarController.sidebarVerticalTabsEnabled`

## SidebarMain.setCustomize()
- 位置: L545-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.SidebarController.sidebars.get()`
- 参照: `customizeSidebar.iconUrl`, `customizeSidebar.revampL10nId`, `this.bottomActions`

## SidebarMain.handleEvent()
- 位置: async L557-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["tabs-newtab-button", "vertical-tabs-newtab-button"].includes()`, `this.manageExtension()`, `this.removeExtension()`, `this.reportExtension()`, `this.requestUpdate()`, `this.unpinExtension()`, `window.SidebarController._state.updateVisibility()`, `window.SidebarController.hide()`, `window.SidebarController.show()`, `window.SidebarController.toggleVerticalTabs()`, `window.SidebarController.updateToolbarButton()`
- 条件付き依存: `if ( window.SidebarController._animationEnabled && !window.gReduceMotion )` → `window.SidebarController._animateSidebarContainer()`
- 条件付き依存: `if ( !["tabs-newtab-button", "vertical-tabs-newtab-button"].includes( e.target.id ) )` → `this.onSidebarPopupShowing(e).then()`
- 条件付き依存: `if ( !["tabs-newtab-button", "vertical-tabs-newtab-button"].includes( e.target.id ) )` → `this.onSidebarPopupShowing()`
- 条件付き依存: `if ( !["tabs-newtab-button", "vertical-tabs-newtab-button"].includes( e.target.id ) )` → `this.dispatchEvent()`
- 条件付き依存: `if (e.target === this._toolsOverflowMenu)` → `window.removeEventListener()`
- 条件付き依存: `if (e.target === this._toolsOverflowMenu)` → `window.addEventListener()`
- 参照: `e.detail.viewId`, `e.target`, `e.target.id`, `e.type`, `this.#shouldUpdateActiveButton`, `this._contextMenu`, `this._toolsOverflowMenu`, `this.contextMenuTarget`, `this.handleOverflowKeypress`, `this.isOverflowMenuOpen`, `this.open`, `this.selectedView`, `window.SidebarController._animationEnabled`, `window.gReduceMotion`

## SidebarMain.handleOverflowKeypress()
- 位置: L634-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toolsOverflowButtonGroup.matches()`
- 条件付き依存: `if (e.key == "ArrowUp")` → `this._toolsOverflowButtonGroup.walker.lastChild()`
- 条件付き依存: `if ( (e.key == "ArrowDown" || e.key == "ArrowUp") && !this._toolsOverflowButtonGroup.matches(":focus-within") )` → `this._toolsOverflowButtonGroup.activeChild.focus()`
- 参照: `e.key`, `this._toolsOverflowButtonGroup.activeChild`

## SidebarMain.checkShouldShowCalloutSurveys()
- 位置: async L647-663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`
- 参照: `lazy.ASRouter.waitForInitialized`, `this.clickCounts`, `this.clickCounts.genai`, `this.clickCounts.totalToolsMinusGenai`, `window.gBrowser.selectedBrowser`

## SidebarMain.showView()
- 位置: async L665-679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openTabsPreview?.hide()`, `toolsAndExtensions.has()`, `window.SidebarController.recordIconClick()`, `window.SidebarController.toggle()`
- 条件付き依存: `if (view === "viewCustomizeSidebar")` → `Glean.sidebarCustomize.iconClick.record()`
- 条件付き依存: `if (isToolOpening)` → `this.checkShouldShowCalloutSurveys()`
- 参照: `this.expanded`, `window.SidebarController`

## SidebarMain.enabledToolsAndExtensionsCount()
- 位置: L681-689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.SidebarController.toolsAndExtensions.values()`
- 参照: `tool.disabled`

## SidebarMain.isToolsOverflowing()
- 位置: L691-693
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.expanded`, `window.SidebarController.sidebarVerticalTabsEnabled`

## SidebarMain.willUpdate()
- 位置: L695-698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toolsIntersectionObserver?.disconnect()`, `this._toolsResizeObserver?.disconnect()`

## SidebarMain.updated()
- 位置: L700-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toolsIntersectionObserver.disconnect()`, `this._toolsResizeObserver.disconnect()`
- 条件付き依存: `if (this.#shouldUpdateActiveButton)` → `[...this.allButtons].find()`
- 条件付き依存: `if (this.#shouldUpdateActiveButton)` → `button.getAttribute()`
- 条件付き依存: `if ( !isExpandOnHover && window.SidebarController.sidebarVerticalTabsEnabled )` → `buttonEl.hasAttribute()`
- 条件付き依存: `if (buttonEl.hasAttribute("view"))` → `this._toolsIntersectionObserver.observe()`
- 条件付き依存: `if ( !isExpandOnHover && window.SidebarController.sidebarVerticalTabsEnabled )` → `this._toolsResizeObserver.observe()`
- 条件付き依存: `if (!isExpandOnHover)` → `document.getElementById("tools-overflow-list").replaceChildren()`
- 条件付き依存: `if (!isExpandOnHover)` → `document.getElementById()`
- 参照: `buttonEl.style.visibility`, `this.#shouldUpdateActiveButton`, `this.allButtons`, `this.buttonGroup`, `this.buttonGroup.activeChild`, `this.expanded`, `this.selectedView`, `this.shouldShowOverflowButton`, `window.SidebarController.sidebarRevampVisibility`, `window.SidebarController.sidebarVerticalTabsEnabled`

## SidebarMain.getEntrypointValues()
- 位置: L747-800
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isToolsOverflowing()`
- 条件付き依存: `if (action.l10nId)` → `this.fluentStrings.formatMessagesSync()`
- 条件付き依存: `if (action.l10nId)` → `attributes?.find()`
- 条件付き依存: `if (shortcutId)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (shortcutId)` → `document.getElementById()`
- 条件付き依存: `if (tooltipInfo)` → `this.fluentStrings.formatValueSync()`
- 参照: `action.disabled`, `action.hidden`, `action.iconUrl`, `action.l10nId`, `action.tooltiptext`, `action.view`, `attr.name`, `attributes?.find(attr => attr.name === "label")?.value`, `lazy.GenAI.currentChatProviderInfo`, `messages?.[0]?.attributes`, `providerInfo.iconUrl`, `providerInfo.name`, `providerInfo?.name`, `this.open`, `this.selectedView`, `this.tooltips`, `tooltipData.provider`, `tooltipData.shortcut`, `tooltipInfo.closeProviderl10nId`, `tooltipInfo.openProviderl10nId`

## SidebarMain.onEntrypointHover()
- 位置: L802-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.currentTarget.contains()`, `this._openTabsPreview?.activate()`
- 参照: `e.currentTarget`, `e.relatedTarget`

## SidebarMain.onEntrypointHoverEnd()
- 位置: L812-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.currentTarget.contains()`, `this._openTabsPreview?.deactivate()`
- 参照: `e.relatedTarget`

## SidebarMain.entrypointTemplate()
- 位置: L822-851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttonValues.action.view?.includes()`, `classMap()`, `html()`, `ifDefined()`, `this.getEntrypointValues()`, `this.onEntrypointHover()`, `this.onEntrypointHoverEnd()`, `this.showView()`, `when()`
- 参照: `action?.attention`, `action?.contextMenu`, `buttonValues.action.extensionId`, `buttonValues.action.iconUrl`, `buttonValues.action.view`, `buttonValues.actionLabel`, `buttonValues.isActiveView`, `buttonValues.toolsOverflowing`, `buttonValues.tooltip`

## SidebarMain.showOverflowMenu()
- 位置: L853-885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `panel.addEventListener()`, `panel.openPopup()`, `panel.querySelector()`, `this.moreToolsButton.shadowRoot.querySelector()`, `this.resetPanelButtonValues()`
- 条件付き依存: `if (isKeyboardEvent)` → `group.activeChild.focus()`
- 条件付き依存: `if (isKeyboardEvent)` → `panel.addEventListener()`
- 条件付き依存: `if (isKeyboardEvent)` → `this.moreToolsButton.focus()`
- 参照: `e.detail`, `group.activeChild`, `group.firstElementChild`, `window.SidebarController._positionStart`

## SidebarMain.shouldUpdate()
- 位置: L887-890
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `container.hidden`, `window.SidebarController.sidebarContainer`

## SidebarMain.render()
- 位置: L892-970
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `attributes?.find()`, `html()`, `ifDefined()`, `repeat()`, `this.enabledToolsAndExtensionsCount()`, `this.entrypointTemplate()`, `this.fluentStrings.formatMessagesSync()`, `this.getLauncherActions()`, `this.isToolsOverflowing()`, `when()`
- 参照: `action.view`, `attr.name`, `attributes?.find( attr => attr.name === "label" )?.value`, `messages?.[0]?.attributes`, `this.bottomActions`, `this.expanded`, `this.isOverflowMenuOpen`, `this.shouldShowOverflowButton`, `this.showOverflowMenu`, `this.toolsSplitter`, `window.SidebarController.sidebarRevampVisibility`, `window.SidebarController.sidebarVerticalTabsEnabled`
