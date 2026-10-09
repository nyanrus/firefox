# browser/components/extensions/parent/ext-devtools.js

source: browser/components/extensions/parent/ext-devtools.js
source-hash: 650f58b7a5026d57a4f35a5e101d6fc3acfd66bb
lines: 513

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## getDevToolsPrefBranchName()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)

## global.getTargetTabIdForToolbox()
- 位置: L36-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parentWindow.gBrowser.getTabForBrowser()`, `tabTracker.getId()`
- 参照: `descriptorFront.isLocalTab`, `descriptorFront.localTab.linkedBrowser`, `descriptorFront.localTab.linkedBrowser.documentGlobal`, `toolbox.commands`

## global.getToolboxEvalOptions()
- 位置: async L55-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolbox.target.getFront()`
- 参照: `consoleFront.actor`, `context.devToolsToolbox`, `options.toolboxConsoleActorID`, `options.toolboxSelectedNodeActorID`, `selectedNode.nodeFront`, `selectedNode.nodeFront.actorID`, `toolbox.selection`

## DevToolsPage.constructor()
- 位置: L93-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.baseURI.resolve()`, `super()`
- 参照: `options.devToolsPageDefinition`, `options.toolbox`, `options.url`, `this.devToolsPageDefinition`, `this.resolveTopLevelContext`, `this.toolbox`, `this.unwatchExtensionProxyContextLoad`, `this.url`, `this.waitForTopLevelContext`

## DevToolsPage.build()
- 位置: async L107-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DevToolsShim.getTheme()`, `extensions.emit()`, `getTargetTabIdForToolbox()`, `this.browser.fixupAndLoadURIString()`, `this.createBrowserElement()`, `watchExtensionProxyContextLoad()`
- 条件付き依存: `if (!this.topLevelContext)` → `this.topLevelContext.callOnClose()`
- 条件付き依存: `if (!this.topLevelContext)` → `this.resolveTopLevelContext()`
- 参照: `context.devToolsToolbox`, `this.browser`, `this.extension.principal`, `this.toolbox`, `this.topLevelContext`, `this.unwatchExtensionProxyContextLoad`, `this.url`, `this.waitForTopLevelContext`

## DevToolsPage.close()
- 位置: L144-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.shutdown()`, `this.devToolsPageDefinition.forgetForToolbox()`
- 条件付き依存: `if (this.topLevelContext)` → `this.topLevelContext.forgetOnClose()`
- 条件付き依存: `if (this.unwatchExtensionProxyContextLoad)` → `this.unwatchExtensionProxyContextLoad()`
- 参照: `this.closed`, `this.toolbox`, `this.topLevelContext`, `this.unwatchExtensionProxyContextLoad`

## DevToolsPageDefinition.constructor()
- 位置: L188-194
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.devtoolsPageForToolbox`, `this.extension`, `this.url`

## DevToolsPageDefinition.onThemeChanged()
- 位置: L196-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.broadcastAsyncMessage()`
- XPCOM: `Services.ppmm`

## DevToolsPageDefinition.buildForToolbox()
- 位置: L202-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `devtoolsPage.build()`, `this.devtoolsPageForToolbox.has()`, `this.devtoolsPageForToolbox.set()`, `this.extension.canAccessWindow()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `Promise.reject()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.size === 0)` → `DevToolsShim.on()`
- 参照: `this.devtoolsPageForToolbox.size`, `this.extension`, `this.onThemeChanged`, `this.url`, `toolbox.commands.descriptorFront.localTab.documentGlobal`

## DevToolsPageDefinition.shutdownForToolbox()
- 位置: L234-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.devtoolsPageForToolbox.has()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `this.devtoolsPageForToolbox.get()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `devtoolsPage.close()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `this.devtoolsPageForToolbox.has()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.size === 0)` → `DevToolsShim.off()`
- 条件付き依存: `if (this.devtoolsPageForToolbox.has(toolbox))` → `this.extension.emit()`
- 参照: `this.devtoolsPageForToolbox.size`, `this.extension.policy.debugName`, `this.onThemeChanged`, `toolbox.commands.descriptorFront.url`

## DevToolsPageDefinition.forgetForToolbox()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.devtoolsPageForToolbox.delete()`

## DevToolsPageDefinition.build()
- 位置: L263-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DevToolsShim.getToolboxes()`, `getDevToolsPrefBranchName()`, `this.buildForToolbox()`, `this.extension.canAccessWindow()`, `toolbox.isDestroying()`, `toolbox.registerWebExtension()`
- 参照: `this.extension.id`, `this.extension.name`, `this.extension.uuid`, `toolbox.commands.descriptorFront.isLocalTab`, `toolbox.commands.descriptorFront.localTab.documentGlobal`

## DevToolsPageDefinition.shutdown()
- 位置: L295-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.devtoolsPageForToolbox.keys()`, `this.shutdownForToolbox()`
- 参照: `this.devtoolsPageForToolbox.size`

## constructor()
- 位置: L309-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extension.on()`, `permissions.permissions.includes()`, `super()`, `this.onToolboxDestroy.bind()`, `this.onToolboxReady.bind()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `getDevToolsPrefBranchName()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `this._initialize()`
- 条件付き依存: `if (permissions.permissions.includes("devtools"))` → `this._uninitialize()`
- 参照: `extension.id`, `this._initialized`, `this.onToolboxDestroy`, `this.onToolboxReady`, `this.pageDefinition`
- XPCOM: `Services.prefs`

## onManifestEntry()
- 位置: L344-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._initialize()`

## onUninstall()
- 位置: L348-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBranch()`, `getDevToolsPrefBranchName()`, `prefBranch.deleteBranch()`
- XPCOM: `Services.prefs`

## _initialize()
- 位置: L357-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DevToolsShim.on()`, `extension.hasPermission()`, `this.initDevToolsPref()`, `this.isDevToolsPageDisabled()`
- 条件付き依存: `if (!this.isDevToolsPageDisabled())` → `this.pageDefinition.build()`
- 参照: `extension.manifest.devtools_page`, `this._initialized`, `this.onToolboxDestroy`, `this.onToolboxReady`, `this.pageDefinition`

## _uninitialize()
- 位置: L383-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DevToolsShim.getToolboxes()`, `DevToolsShim.off()`, `this.pageDefinition.shutdown()`, `this.uninitDevToolsPref()`, `toolbox.unregisterWebExtension()`
- 参照: `this._initialized`, `this.extension.uuid`, `this.onToolboxDestroy`, `this.onToolboxReady`, `this.pageDefinition`

## onShutdown()
- 位置: L407-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._uninitialize()`

## getAPI()
- 位置: L411-415
- 役割: (未記入)
- 触るとき: (未記入)

## onToolboxReady()
- 位置: L417-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getDevToolsPrefBranchName()`, `this.extension.canAccessWindow()`, `toolbox.isWebExtensionEnabled()`, `toolbox.registerWebExtension()`
- 条件付き依存: `if (toolbox.isWebExtensionEnabled(this.extension.uuid))` → `this.pageDefinition.buildForToolbox()`
- 参照: `this.extension.id`, `this.extension.name`, `this.extension.uuid`, `toolbox.commands.descriptorFront.isLocalTab`, `toolbox.commands.descriptorFront.localTab.documentGlobal`

## onToolboxDestroy()
- 位置: L443-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pageDefinition.shutdownForToolbox()`
- 参照: `toolbox.commands.descriptorFront.isLocalTab`

## initDevToolsPref()
- 位置: L457-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBranch()`, `getDevToolsPrefBranchName()`, `prefBranch.getPrefType()`, `this.devtoolsPrefBranch.addObserver()`
- 条件付き依存: `if (prefBranch.getPrefType("enabled") === prefBranch.PREF_INVALID)` → `prefBranch.setBoolPref()`
- 参照: `prefBranch.PREF_INVALID`, `this.devtoolsPrefBranch`, `this.extension.id`
- XPCOM: `Services.prefs`

## uninitDevToolsPref()
- 位置: L474-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.devtoolsPrefBranch.removeObserver()`
- 参照: `this.devtoolsPrefBranch`

## isDevToolsPageDisabled()
- 位置: L486-488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.devtoolsPrefBranch.getBoolPref()`

## observe()
- 位置: L498-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isDevToolsPageDisabled()`
- 条件付き依存: `if (this.isDevToolsPageDisabled())` → `this.pageDefinition.shutdown()`
- 条件付き依存: `if (!(this.isDevToolsPageDisabled()))` → `this.pageDefinition.build()`
- 参照: `this.devtoolsPrefBranch`
