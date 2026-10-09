# browser/components/customizableui/ToolbarContextMenu.sys.mjs

source: browser/components/customizableui/ToolbarContextMenu.sys.mjs
source-hash: c87bd45858c9f10a64551cf5a5572c0ceb5507d0
lines: 621

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## updateDownloadsAutoHide()
- 位置: L47-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["downloads-button", "wrapper-downloads-button"].includes()`, `checkbox.toggleAttribute()`, `document.getElementById()`
- 参照: `DownloadsButton.autoHideDownloadsButton`, `checkbox.hidden`, `popup.documentGlobal`, `popup.triggerNode`, `popup.triggerNode.id`

## onDownloadsAutoHideChange()
- 位置: L72-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.target.hasAttribute()`
- XPCOM: `Services.prefs`

## updateDownloadsAlwaysOpenPanel()
- 位置: L88-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["downloads-button", "wrapper-downloads-button"].includes()`, `checkbox.toggleAttribute()`, `document.getElementById()`
- 参照: `checkbox.hidden`, `lazy.gAlwaysOpenPanel`, `popup.documentGlobal`, `popup.triggerNode`, `popup.triggerNode.id`, `separator.hidden`

## onDownloadsAlwaysOpenPanelChange()
- 位置: L113-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.target.hasAttribute()`
- XPCOM: `Services.prefs`

## onViewToolbarsPopupShowing()
- 位置: L131-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `Services.prefs.getBoolPref()`, `["tabbrowser-tabs", "sidebar-button"].includes()`, `deadItem.hasAttribute()`, `document .getElementById()`, `document .getElementById("toolbar-context-menu") .querySelectorAll()`, `document .getElementById("toolbar-context-menu") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`, `document.getElementById()`, `document.l10n.setAttributes()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `lazy.CustomizableUI.isSpecialWidget()`, `lazy.CustomizableUI.isWidgetRemovable()`, `moveToPanel.toggleAttribute()`, `popup.querySelector()`, `popup.querySelectorAll()`, `removeFromToolbar.toggleAttribute()`, `showFullScreenViewContextMenuItems()`, `toolbarItem?.classList.contains()`, `toolbarItem?.id.startsWith()`, `toolbarItem?.localName.includes()`
- 条件付き依存: `if (localName == "menupopup")` → `aEvent.preventDefault()`
- 条件付き依存: `if (localName == "menupopup")` → `aEvent.stopPropagation()`
- 条件付き依存: `if (parent)` → `parent.classList.contains()`
- 条件付き依存: `if (parent)` → `parent.getAttribute()`
- 条件付き依存: `if (deadItem.hasAttribute("toolbarId"))` → `popup.removeChild()`
- 条件付き依存: `if (!isVerticalTabStripMenu)` → `MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!isVerticalTabStripMenu)` → `gNavToolbox.querySelectorAll()`
- 条件付き依存: `if (!isVerticalTabStripMenu)` → `toolbar.hasAttribute()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.buildBookmarksToolbarSubmenu()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `popup.insertBefore()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `document.createXULElement()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `menuItem.setAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `toolbar.getAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `menuItem.toggleAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `toolbar.hasAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `popup.insertBefore()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `menuItem.addEventListener()`
- 条件付き依存: `if (showTabStripItems)` → `document.getElementById()`
- 条件付き依存: `if (showTabStripItems)` → `gBrowser.allTabsSelected()`
- 条件付き依存: `if (showTabStripItems)` → `lazy.SessionStore.getLastClosedTabCount()`
- 条件付き依存: `if (showTabStripItems)` → `document .getElementById("History:UndoCloseTab") .toggleAttribute()`
- 条件付き依存: `if (showTabStripItems)` → `document .getElementById()`
- 条件付き依存: `if (showTabStripItems)` → `document.l10n.setArgs()`
- 参照: `aEvent.target`, `aInsertPoint.hidden`, `document.getElementById("customizationMenuSeparator").hidden`, `document.getElementById("sidebarRevampSeparator").hidden`, `document.getElementById("toolbar-context-bookmarkSelectedTab").hidden`, `document.getElementById("toolbar-context-bookmarkSelectedTabs").hidden`, `document.getElementById("toolbar-context-customize").hidden`, `document.getElementById("toolbar-context-customize-sidebar").hidden`, `document.getElementById("toolbar-context-reloadSelectedTab").hidden`, `document.getElementById("toolbar-context-reloadSelectedTabs").hidden`, `document.getElementById("toolbar-context-selectAllTabs").disabled`, `document.getElementById("toolbarNavigatorItemsMenuSeparator").hidden`, `gBrowser.multiSelectedTabsCount`, `gBrowser.tabContainer?.verticalMode`, `menuSeparator.hidden`, `moveToPanel.hidden`, `node.hidden`, `parent.id`, `parent.localName`, `popup.children`, `popup.children.length`, `popup.documentGlobal`, `popup.firstElementChild`, `popup.triggerNode`, `removeFromToolbar.hidden`, `toggleVerticalTabsItem.hidden`, `toolbar.id`, `toolbarItem.firstElementChild`, `toolbarItem.id`, `toolbarItem.localName`, `toolbarItem.parentElement`, `toolbarItem.parentElement.id`, `toolbarItem?.id`, `toolbarItem?.localName`, `toolbarItem?.parentElement?.id`
- XPCOM: `Services.prefs`

## _getUnwrappedTriggerNode()
- 位置: L376-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gCustomizeMode.isWrappedToolbarItem()`
- 参照: `popup.documentGlobal`, `triggerNode.firstElementChild`

## _getExtensionId()
- 位置: L396-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.getAttribute()`, `this._getUnwrappedTriggerNode()`

## _getWidgetId()
- 位置: L413-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node?.closest()`, `this._getUnwrappedTriggerNode()`
- 参照: `node?.closest(".unified-extensions-item")?.id`

## updateExtensionsButtonContextMenu()
- 位置: L424-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popup.querySelector()`
- 条件付き依存: `if (isCustomizingExtsButton)` → `checkbox.toggleAttribute()`
- 条件付き依存: `if (isExtsButton && !gUnifiedExtensions.buttonAlwaysVisible)` → `checkbox.removeAttribute()`
- 条件付き依存: `if (isExtsButton)` → `popup.querySelector()`
- 条件付き依存: `if (gUnifiedExtensions.buttonAlwaysVisible)` → `removeFromToolbar.removeAttribute()`
- 参照: `checkbox.hidden`, `gUnifiedExtensions.buttonAlwaysVisible`, `popup.documentGlobal`, `popup.triggerNode?.id`, `removeFromToolbar.hidden`

## updateExtension()
- 位置: async L475-521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.getAddonByID()`, `popup.querySelector()`, `this._getExtensionId()`
- 条件付き依存: `if (addon)` → `popup.querySelector()`
- 条件付き依存: `if (pinToToolbar)` → `this._getWidgetId()`
- 条件付き依存: `if (widgetId)` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (widgetId)` → `pinToToolbar.toggleAttribute()`
- 条件付き依存: `if (popup.id === "toolbar-context-menu")` → `lazy.ExtensionsUI.originControlsMenu()`
- 参照: `addon.permissions`, `element.hidden`, `lazy.AddonManager.PERM_CAN_UNINSTALL`, `lazy.CustomizableUI.AREA_ADDONS`, `lazy.CustomizableUI.getPlacementOfWidget(widgetId).area`, `lazy.gAddonAbuseReportEnabled`, `pinToToolbar.hidden`, `popup.id`, `popup.querySelector(".customize-context-moveToPanel").hidden`, `popup.querySelector(".customize-context-removeFromToolbar").hidden`, `removeExtension.disabled`, `reportExtension.hidden`, `reportExtension.nextElementSibling`

## removeExtensionForContextAction()
- 位置: async L531-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.removeAddon()`, `this._getExtensionId()`
- 参照: `popup.documentGlobal`

## reportExtensionForContextAction()
- 位置: async L548-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.reportAddon()`, `this._getExtensionId()`
- 参照: `popup.documentGlobal`

## openAboutAddonsForContextAction()
- 位置: async L563-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.manageAddon()`, `this._getExtensionId()`
- 参照: `popup.documentGlobal`

## hideLeadingSeparatorIfNeeded()
- 位置: L579-593
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `firstVisibleElement.hidden`, `firstVisibleElement.localName`, `firstVisibleElement.nextElementSibling`, `popup.firstElementChild`

## updateCustomizationItemsVisibility()
- 位置: L606-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `moveToPanel.hasAttribute()`, `popup.querySelector()`, `removeFromToolbar?.hasAttribute()`
- 参照: `moveToPanel.hidden`, `removeFromToolbar.hidden`
