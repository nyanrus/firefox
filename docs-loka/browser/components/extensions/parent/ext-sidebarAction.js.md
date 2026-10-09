# browser/components/extensions/parent/ext-sidebarAction.js

source: browser/components/extensions/parent/ext-sidebarAction.js
source-hash: ec0676688769674c9caab7e34f621c2dede5e7d8
lines: 485

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## for()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarActionMap.get()`

## onManifestEntry()
- 位置: L31-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getClassName()`, `IconDetails.normalize()`, `Object.create()`, `extension.once()`, `makeWidgetId()`, `sidebarActionMap.set()`, `this.onReady.bind()`, `this.tabContext.get()`, `windowTracker.addOpenListener()`
- 参照: `extension.id`, `extension.manifest.sidebar_action`, `extension.name`, `options.browser_style`, `options.default_icon`, `options.default_panel`, `options.default_title`, `target.documentGlobal`, `this.browserStyle`, `this.defaults`, `this.globals`, `this.id`, `this.menuId`, `this.tabContext`, `this.windowOpenListener`

## this.windowOpenListener()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createMenuItem()`
- 参照: `this.globals`

## onReady()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.build()`

## onShutdown()
- 位置: L83-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SidebarController.removeExtension()`, `sidebarActionMap.delete()`, `this.tabContext.shutdown()`, `windowTracker.browserWindows()`, `windowTracker.removeOpenListener()`
- 参照: `this.extension`, `this.id`, `this.windowOpenListener`

## onUninstall()
- 位置: L105-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getStringPref()`, `Services.prefs .getStringPref("sidebar.installed.extensions", "") .split()`, `installedExtensions.indexOf()`, `makeWidgetId()`, `windowTracker.browserWindows()`
- 条件付き依存: `if (index != -1)` → `SidebarManager.cleanupPrefs()`
- 参照: `SidebarController.lastOpenedId`
- XPCOM: `Services.prefs`

## build()
- 位置: L124-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabContext.on()`, `this.updateWindow()`, `windowTracker.browserWindows()`
- 条件付き依存: `if ( (install || SidebarController.lastOpenedId == this.id) && this.extension.manifest.sidebar_action.open_at_install )` → `SidebarController.show()`
- 参照: `SidebarController.lastOpenedId`, `tab.documentGlobal`, `this.extension.manifest.sidebar_action.open_at_install`, `this.extension.startupReason`, `this.id`

## createMenuItem()
- 位置: L143-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SidebarController.registerExtension()`, `this.extension.canAccessWindow()`, `this.getMenuIcon()`
- 参照: `details.panel`, `details.title`, `this.extension.id`, `this.id`, `this.menuId`, `this.panel`

## onload()
- 位置: L154-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SidebarController.browser.contentWindow.loadPanel()`
- 参照: `this.browserStyle`, `this.extension.id`, `this.panel`

## getMenuIcon()
- 位置: L173-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IconDetails.escapeUrl()`, `IconDetails.getPreferredIcon()`
- 参照: `IconDetails.getPreferredIcon(icon, this.extension, 16 * scale).icon`, `this.extension`

## updateButton()
- 位置: L187-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SidebarController.setExtensionAttributes()`, `document.getElementById()`, `this.getMenuIcon()`
- 条件付き依存: `if (!document.getElementById(this.menuId))` → `this.createMenuItem()`
- 参照: `tabData.panel`, `tabData.title`, `this.extension.name`, `this.id`, `this.menuId`, `this.panel`

## updateWindow()
- 位置: L216-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.canAccessWindow()`, `this.tabContext.get()`, `this.updateButton()`
- 参照: `window.gBrowser.selectedTab`

## updateOnChange()
- 位置: L233-245
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target)` → `ChromeUtils.getClassName()`
- 条件付き依存: `if (ChromeUtils.getClassName(target) == "Window")` → `this.updateWindow()`
- 条件付き依存: `if (target.selected)` → `this.updateWindow()`
- 条件付き依存: `if (!(target))` → `windowTracker.browserWindows()`
- 条件付き依存: `if (!(target))` → `this.updateWindow()`
- 参照: `target.documentGlobal`, `target.selected`

## getTargetFromDetails()
- 位置: L263-282
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tabId != null)` → `tabTracker.getTab()`
- 条件付き依存: `if (tabId != null)` → `this.extension.canAccessWindow()`
- 条件付き依存: `if (windowId != null)` → `windowTracker.getWindow()`
- 条件付き依存: `if (windowId != null)` → `this.extension.canAccessWindow()`
- 参照: `target.documentGlobal`

## getContextData()
- 位置: L292-297
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target)` → `this.tabContext.get()`
- 参照: `this.globals`

## setProperty()
- 位置: L309-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getContextData()`, `this.updateOnChange()`

## getProperty()
- 位置: L330-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getContextData()`

## setPropertyFromDetails()
- 位置: L334-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getTargetFromDetails()`, `this.setProperty()`

## getPropertyFromDetails()
- 位置: L338-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getProperty()`, `this.getTargetFromDetails()`

## triggerAction()
- 位置: L348-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.canAccessWindow()`
- 条件付き依存: `if (SidebarController && this.extension.canAccessWindow(window))` → `SidebarController.toggle()`
- 参照: `this.id`

## open()
- 位置: L360-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.canAccessWindow()`
- 条件付き依存: `if (SidebarController && this.extension.canAccessWindow(window))` → `SidebarController.show()`
- 参照: `this.id`

## close()
- 位置: L372-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isOpen()`
- 条件付き依存: `if (this.isOpen(window))` → `window.SidebarController.hide()`

## toggle()
- 位置: L383-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.canAccessWindow()`, `this.isOpen()`
- 条件付き依存: `if (!this.isOpen(window))` → `SidebarController.show()`
- 条件付き依存: `if (!(!this.isOpen(window)))` → `SidebarController.hide()`
- 参照: `this.id`

## isOpen()
- 位置: L402-405
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SidebarController.currentID`, `SidebarController.isOpen`, `this.id`

## getAPI()
- 位置: L407-481
- 役割: (未記入)
- 触るとき: (未記入)

## setTitle()
- 位置: async L413-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarAction.setPropertyFromDetails()`
- 参照: `details.title`

## getTitle()
- 位置: L417-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarAction.getPropertyFromDetails()`

## setIcon()
- 位置: async L421-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IconDetails.normalize()`, `Object.keys()`, `sidebarAction.setPropertyFromDetails()`
- 参照: `Object.keys(icon).length`

## setPanel()
- 位置: async L429-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarAction.setPropertyFromDetails()`
- 条件付き依存: `if (!(!details.panel))` → `context.uri.resolve()`
- 条件付き依存: `if (!(!details.panel))` → `context.checkLoadURL()`
- 条件付き依存: `if (!context.checkLoadURL(url))` → `Promise.reject()`
- 参照: `details.panel`

## getPanel()
- 位置: L446-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarAction.getPropertyFromDetails()`

## open()
- 位置: L450-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`
- 条件付き依存: `if (context.canAccessWindow(window))` → `sidebarAction.open()`
- 参照: `windowTracker.topWindow`

## close()
- 位置: L457-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`
- 条件付き依存: `if (context.canAccessWindow(window))` → `sidebarAction.close()`
- 参照: `windowTracker.topWindow`

## toggle()
- 位置: L464-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.canAccessWindow()`
- 条件付き依存: `if (context.canAccessWindow(window))` → `sidebarAction.toggle()`
- 参照: `windowTracker.topWindow`

## isOpen()
- 位置: L471-478
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarAction.isOpen()`, `windowTracker.getWindow()`
- 参照: `Window.WINDOW_ID_CURRENT`
