# browser/components/sidebar/sidebar-customize.mjs

source: browser/components/sidebar/sidebar-customize.mjs
source-hash: ceec6854260e967ebd2ad20ea54889c9e2315f35
lines: 418

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## SidebarCustomize.constructor()
- 位置: L34-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`
- 参照: `this.#prefValues`, `this.#prefValues.expandOnHoverEnabled`, `this.#prefValues.hoverPreviewEnabled`, `this.#prefValues.isPositionStart`, `this.#prefValues.verticalTabsEnabled`, `this.#prefValues.visibility`, `this.boundObserve`, `this.expandOnHoverEnabled`, `this.hoverPreviewEnabled`, `this.isPositionStart`, `this.verticalTabsEnabled`, `this.visibility`

## this.boundObserve()
- 位置: L86-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observe()`

## SidebarCustomize.connectedCallback()
- 位置: L111-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.getWindow()`, `this.getWindow().addEventListener()`

## SidebarCustomize.disconnectedCallback()
- 位置: L118-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.getWindow()`, `this.getWindow().removeEventListener()`

## SidebarCustomize.fluentStrings()
- 位置: L125-130
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._fluentStrings`

## SidebarCustomize.getWindow()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window.browsingContext.embedderWindowGlobal.browsingContext.window`

## SidebarCustomize.handleEvent()
- 位置: L136-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 参照: `e.type`

## SidebarCustomize.onToggleToolInput()
- 位置: async L146-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.contextualManager.passwordsEnabled.record()`, `Glean.sidebarCustomize.bookmarksEnabled.record()`, `Glean.sidebarCustomize.chatbotEnabled.record()`, `Glean.sidebarCustomize.historyEnabled.record()`, `Glean.sidebarCustomize.syncedTabsEnabled.record()`, `e.preventDefault()`, `this.getWindow()`, `this.getWindow().SidebarController.toggleTool()`
- 参照: `e.target.checked`

## SidebarCustomize.getInputL10nId()
- 位置: L178-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `l10nMap.get()`

## SidebarCustomize.openFirefoxSettings()
- 位置: L182-188
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `e.preventDefault()`
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `this.getWindow().openPreferences()`
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `this.getWindow()`
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `Glean.sidebarCustomize.firefoxSettingsClicked.record()`
- 参照: `e.code`, `e.type`

## SidebarCustomize.toolInputTemplate()
- 位置: L190-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.getInputL10nId()`, `this.onToggleToolInput()`, `when()`
- 参照: `this.#toggleHoverPreview`, `this.hoverPreviewEnabled`, `tool.commandID`, `tool.disabled`, `tool.hidden`, `tool.iconUrl`, `tool.name`, `tool.tooltiptext`, `tool.view`

## SidebarCustomize.manageAddons()
- 位置: L225-231
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `e.preventDefault()`
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `this.getWindow().BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `this.getWindow()`
- 条件付き依存: `if (e.type == "click" || (e.type == "keydown" && e.code == "Enter"))` → `Glean.sidebarCustomize.extensionsClicked.record()`
- 参照: `e.code`, `e.type`

## SidebarCustomize.reversePosition()
- 位置: L233-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebarCustomize.sidebarPosition.record()`, `SidebarController.reversePosition()`, `this.getWindow()`
- 参照: `this.getWindow().RTL_UI`, `this.isPositionStart`

## SidebarCustomize.render()
- 位置: L242-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extensions.map()`, `html()`, `this.getWindow()`, `this.getWindow() .SidebarController.getTools()`, `this.getWindow() .SidebarController.getTools() .map()`, `this.getWindow().SidebarController.getExtensions()`, `this.stylesheet()`, `this.toolInputTemplate()`, `when()`
- 参照: `document.dir`, `extensions.length`, `this.#handleOpenToolsFromSidebarChange`, `this.#handleTabDirectionChange`, `this.#handleVisibilityChange`, `this.#toggleExpandOnHover`, `this.expandOnHoverEnabled`, `this.getWindow().SidebarController._state .revampVisibility`, `this.isPositionStart`, `this.manageAddons`, `this.openFirefoxSettings`, `this.reversePosition`, `this.verticalTabsEnabled`, `this.visibility`

## SidebarCustomize.#handleVisibilityChange()
- 位置: L368-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebarCustomize.sidebarDisplay.record()`, `Services.prefs.setStringPref()`, `e.stopPropagation()`
- 参照: `e.target.checked`, `this.visibility`
- XPCOM: `Services.prefs`

## SidebarCustomize.#handleOpenToolsFromSidebarChange()
- 位置: L380-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebarCustomize.sidebarDisplay.record()`, `Services.prefs.setStringPref()`, `e.stopPropagation()`
- 参照: `e.target.checked`, `this.visibility`
- XPCOM: `Services.prefs`

## SidebarCustomize.#toggleExpandOnHover()
- 位置: L391-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.stopPropagation()`
- 条件付き依存: `if (e.target.checked)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (e.target.checked)` → `Glean.sidebarCustomize.expandOnHoverEnabled.record()`
- 条件付き依存: `if (!(e.target.checked))` → `Services.prefs.setStringPref()`
- 参照: `e.target.checked`
- XPCOM: `Services.prefs`

## SidebarCustomize.#toggleHoverPreview()
- 位置: L403-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `e.stopPropagation()`
- 参照: `e.target.checked`
- XPCOM: `Services.prefs`

## SidebarCustomize.#handleTabDirectionChange()
- 位置: L408-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sidebarCustomize.tabsLayout.record()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`
