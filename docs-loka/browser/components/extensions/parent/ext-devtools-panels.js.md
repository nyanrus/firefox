# browser/components/extensions/parent/ext-devtools-panels.js

source: browser/components/extensions/parent/ext-devtools-panels.js
source-hash: a4d13753d30e52c4da62c9f3ee43226628c1d44c
lines: 739

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## BaseDevToolsPanel.constructor()
- 位置: L20-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!toolbox)` → `Error()`
- 参照: `context.devToolsToolbox`, `context.extension`, `panelOptions.id`, `this.browser`, `this.browserContainerWindow`, `this.context`, `this.extension`, `this.id`, `this.panelOptions`, `this.toolbox`, `this.unwatchExtensionProxyContextLoad`, `this.viewType`

## BaseDevToolsPanel.createBrowserElement()
- 位置: async L43-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTargetTabIdForToolbox()`, `this.browser.fixupAndLoadURIString()`, `this.syncToolboxZoom()`, `this.toolbox.win.browsingContext.embedderElement.addEventListener()`, `watchExtensionProxyContextLoad()`, `window.getBrowser()`
- 条件付き依存: `if (this._resolveTopLevelContext)` → `this._resolveTopLevelContext()`
- 参照: `context.devToolsToolbox`, `this._resolveTopLevelContext`, `this.browser`, `this.context`, `this.context.principal`, `this.id`, `this.panelOptions`, `this.unwatchExtensionProxyContextLoad`

## BaseDevToolsPanel.handleEvent()
- 位置: L93-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.syncToolboxZoom()`
- 参照: `event.type`

## BaseDevToolsPanel.syncToolboxZoom()
- 位置: L113-119
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.browser`, `this.browser.fullZoom`, `this.toolbox.win.browsingContext.fullZoom`

## BaseDevToolsPanel.destroyBrowserElement()
- 位置: L121-139
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (unwatchExtensionProxyContextLoad)` → `unwatchExtensionProxyContextLoad()`
- 条件付き依存: `if (this.toolbox)` → `this.toolbox.win.browsingContext.embedderElement.removeEventListener()`
- 条件付き依存: `if (browser)` → `browser.remove()`
- 参照: `this.browser`, `this.toolbox`, `this.unwatchExtensionProxyContextLoad`

## ParentDevToolsPanel.constructor()
- 位置: L159-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.addPanel()`, `this.context.callOnClose()`, `this.onToolboxHostChanged.bind()`, `this.onToolboxHostWillChange.bind()`, `this.onToolboxPanelSelect.bind()`
- 参照: `this._resolveTopLevelContext`, `this.conduit`, `this.destroyed`, `this.id`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`, `this.onToolboxPanelSelect`, `this.panelAdded`, `this.visible`, `this.waitTopLevelContext`

## ParentDevToolsPanel.addPanel()
- 位置: L184-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toolbox.addAdditionalTool()`
- 参照: `this.context.extension.id`, `this.context.extension.name`, `this.id`, `this.panelAdded`, `this.panelOptions`

## isToolSupported()
- 位置: L197-197
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `toolbox.commands.descriptorFront.isLocalTab`

## build()
- 位置: L198-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buildPanel()`
- 参照: `this.toolbox`

## ParentDevToolsPanel.buildPanel()
- 位置: L214-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createBrowserElement()`, `this.destroyBrowserElement()`, `toolbox.off()`, `toolbox.on()`
- 参照: `this.browserContainerWindow`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`, `this.onToolboxPanelSelect`

## ParentDevToolsPanel.onToolboxHostWillChange()
- 位置: L242-258
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.visible)` → `this.conduit.sendPanelHidden()`
- 条件付き依存: `if (this.browser)` → `this.destroyBrowserElement()`
- 参照: `this.browser`, `this.id`, `this.visible`

## ParentDevToolsPanel.onToolboxHostChanged()
- 位置: async L260-272
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.browserContainerWindow)` → `this.createBrowserElement()`
- 条件付き依存: `if (this.visible)` → `this.conduit.sendPanelShown()`
- 参照: `this.browserContainerWindow`, `this.id`, `this.visible`, `this.waitTopLevelContext`

## ParentDevToolsPanel.onToolboxPanelSelect()
- 位置: async L274-289
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.visible && id === this.id)` → `this.conduit.sendPanelShown()`
- 条件付き依存: `if (this.visible && id !== this.id)` → `this.conduit.sendPanelHidden()`
- 参照: `this.id`, `this.panelAdded`, `this.visible`, `this.waitTopLevelContext`

## ParentDevToolsPanel.close()
- 位置: L291-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.conduit.close()`, `toolbox.isToolRegistered()`
- 条件付き依存: `if (this.panelAdded && toolbox.isToolRegistered(this.id))` → `this.destroyBrowserElement()`
- 条件付き依存: `if (this.panelAdded && toolbox.isToolRegistered(this.id))` → `toolbox.removeAdditionalTool()`
- 参照: `this._resolveTopLevelContext`, `this.browser`, `this.browserContainerWindow`, `this.context`, `this.id`, `this.panelAdded`, `this.toolbox`, `this.waitTopLevelContext`

## ParentDevToolsPanel.destroyBrowserElement()
- 位置: L315-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.destroyBrowserElement()`
- 参照: `this._resolveTopLevelContext`, `this.waitTopLevelContext`

## DevToolsSelectionObserver.constructor()
- 位置: L328-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.callOnClose()`, `super()`, `this.onSelected.bind()`
- 条件付き依存: `if (!context.devToolsToolbox)` → `Error()`
- 参照: `context.devToolsToolbox`, `this.initialized`, `this.onSelected`, `this.toolbox`

## DevToolsSelectionObserver.on()
- 位置: L343-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.on.apply()`, `this.lazyInit()`

## DevToolsSelectionObserver.once()
- 位置: L348-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.once.apply()`, `this.lazyInit()`

## DevToolsSelectionObserver.lazyInit()
- 位置: async L353-358
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized)` → `this.toolbox.on()`
- 参照: `this.initialized`, `this.onSelected`

## DevToolsSelectionObserver.close()
- 位置: L360-371
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.initialized)` → `this.toolbox.off()`
- 参照: `this.destroyed`, `this.initialized`, `this.onSelected`, `this.toolbox`

## DevToolsSelectionObserver.onSelected()
- 位置: L373-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## ParentDevToolsInspectorSidebar.constructor()
- 位置: L391-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.context.callOnClose()`, `this.onExtensionPageMount.bind()`, `this.onExtensionPageUnmount.bind()`, `this.onSidebarCreated.bind()`, `this.onSidebarSelect.bind()`, `this.onToolboxHostChanged.bind()`, `this.onToolboxHostWillChange.bind()`, `this.toolbox.on()`, `this.toolbox.once()`, `this.toolbox.registerInspectorExtensionSidebar()`
- 参照: `panelOptions.title`, `this._initializeSidebar`, `this._lastExpressionResult`, `this.conduit`, `this.destroyed`, `this.id`, `this.onExtensionPageMount`, `this.onExtensionPageUnmount`, `this.onSidebarCreated`, `this.onSidebarSelect`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`, `this.visible`

## ParentDevToolsInspectorSidebar.close()
- 位置: L432-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.conduit.close()`, `this.toolbox.off()`, `this.toolbox.unregisterInspectorExtensionSidebar()`
- 条件付き依存: `if (this.extensionSidebar)` → `this.extensionSidebar.off()`
- 条件付き依存: `if (this.browser)` → `this.destroyBrowserElement()`
- 参照: `this._lazySidebarInit`, `this.browser`, `this.containerEl`, `this.destroyed`, `this.extensionSidebar`, `this.id`, `this.onExtensionPageMount`, `this.onExtensionPageUnmount`, `this.onSidebarCreated`, `this.onSidebarSelect`, `this.onToolboxHostChanged`, `this.onToolboxHostWillChange`

## ParentDevToolsInspectorSidebar.onToolboxHostWillChange()
- 位置: L471-475
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.browser)` → `this.destroyBrowserElement()`
- 参照: `this.browser`

## ParentDevToolsInspectorSidebar.onToolboxHostChanged()
- 位置: L477-481
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.containerEl && this.panelOptions.url)` → `this.createBrowserElement()`
- 参照: `this.containerEl`, `this.containerEl.contentWindow`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar.onExtensionPageMount()
- 位置: L483-499
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (doc.readyState == "complete" && doc.location.href != "about:blank")` → `onLoaded()`
- 条件付き依存: `if (!(doc.readyState == "complete" && doc.location.href != "about:blank"))` → `containerEl.addEventListener()`
- 参照: `containerEl.contentDocument`, `doc.location.href`, `doc.readyState`, `this.containerEl`

## onLoaded()
- 位置: L488-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createBrowserElement()`
- 参照: `containerEl.contentWindow`

## ParentDevToolsInspectorSidebar.onExtensionPageUnmount()
- 位置: L501-504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.destroyBrowserElement()`
- 参照: `this.containerEl`

## ParentDevToolsInspectorSidebar.onSidebarCreated()
- 位置: L506-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebar.on()`
- 条件付き依存: `if (typeof _lazySidebarInit === "function")` → `_lazySidebarInit()`
- 参照: `this._lazySidebarInit`, `this.extensionSidebar`, `this.onExtensionPageMount`, `this.onExtensionPageUnmount`

## ParentDevToolsInspectorSidebar.onSidebarSelect()
- 位置: L520-532
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.visible && id === this.id)` → `this.conduit.sendInspectorSidebarShown()`
- 条件付き依存: `if (this.visible && id !== this.id)` → `this.conduit.sendInspectorSidebarHidden()`
- 参照: `this.extensionSidebar`, `this.id`, `this.visible`

## ParentDevToolsInspectorSidebar.setPage()
- 位置: L534-556
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.browser)` → `this.browser.fixupAndLoadURIString()`
- 条件付き依存: `if (!(this.browser))` → `this.extensionSidebar.setExtensionPage()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this._setLazySidebarInit()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this.extensionSidebar.setExtensionPage()`
- 参照: `this.browser`, `this.context.extension.principal`, `this.extensionSidebar`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar.setObject()
- 位置: L558-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateLastExpressionResult()`
- 条件付き依存: `if (this.extensionSidebar)` → `this.extensionSidebar.setObject()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this._setLazySidebarInit()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this.extensionSidebar.setObject()`
- 参照: `this.extensionSidebar`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar._setLazySidebarInit()
- 位置: L576-578
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lazySidebarInit`

## ParentDevToolsInspectorSidebar.setExpressionResult()
- 位置: L580-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateLastExpressionResult()`
- 条件付き依存: `if (this.extensionSidebar)` → `this.extensionSidebar.setExpressionResult()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this._setLazySidebarInit()`
- 条件付き依存: `if (!(this.extensionSidebar))` → `this.extensionSidebar.setExpressionResult()`
- 参照: `this.extensionSidebar`, `this.panelOptions.url`

## ParentDevToolsInspectorSidebar._updateLastExpressionResult()
- 位置: L595-611
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( oldActor && oldActor !== newActor && typeof _lastExpressionResult.release === "function" )` → `_lastExpressionResult.release()`
- 参照: `_lastExpressionResult.actorID`, `_lastExpressionResult.release`, `newExpressionResult.actorID`, `this._lastExpressionResult`

## getAPI()
- 位置: L617-737
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `context.extension.baseURI.spec`, `context.extension.id`

## newBasePanelId()
- 位置: L631-633
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `context.contextId`, `context.extension.id`

## register()
- 位置: L642-650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolboxSelectionObserver.off()`, `toolboxSelectionObserver.on()`

## listener()
- 位置: L643-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## createSidebarPane()
- 位置: L652-673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `context.callOnClose()`, `makeWidgetId()`, `newBasePanelId()`, `sidebarsById.set()`

## close()
- 位置: L664-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebarsById.delete()`

## setPage()
- 位置: L678-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebar.setPage()`, `sidebarsById.get()`

## setObject()
- 位置: L682-685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sidebar.setObject()`, `sidebarsById.get()`

## setExpression()
- 位置: async L686-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `commands.inspectedWindowCommand.eval()`, `context.getDevToolsCommands()`, `getToolboxEvalOptions()`, `sidebar.setExpressionResult()`, `sidebarsById.get()`, `target.getFront()`
- 条件付き依存: `if (evalResult.exceptionInfo)` → `sidebar.setObject()`
- 参照: `commands.targetCommand.targetFront`, `evalResult.exceptionInfo`, `toolboxEvalOptions.consoleFront`

## create()
- 位置: L714-733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `context.extension.baseURI.resolve()`, `makeWidgetId()`, `newBasePanelId()`
- 条件付き依存: `if (icon === "")` → `context.extension.getPreferredIcon()`
