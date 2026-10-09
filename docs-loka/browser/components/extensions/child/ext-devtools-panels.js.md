# browser/components/extensions/child/ext-devtools-panels.js

source: browser/components/extensions/child/ext-devtools-panels.js
source-hash: 4b38bd50517794fcd20bdc433ae4978967d43b6e
lines: 325

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyGlobalGetters()`

## ChildDevToolsPanel.constructor()
- 位置: L30-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.openConduit()`, `super()`, `this.context.callOnClose()`
- 参照: `this._panelContext`, `this.conduit`, `this.context`, `this.id`

## ChildDevToolsPanel.panelContext()
- 位置: L44-67
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( view.viewType === "devtools_panel" && view.devtoolsToolboxInfo.toolboxPanelId === this.id )` → `view.callOnClose()`
- 参照: `this._panelContext`, `this.context.extension.devtoolsViews`, `this.id`, `view.devtoolsToolboxInfo.toolboxPanelId`, `view.viewType`

## close()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._panelContext`

## ChildDevToolsPanel.recvPanelShown()
- 位置: L69-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promiseDocumentLoaded()`, `promiseDocumentLoaded(document).then()`, `this.emit()`
- 参照: `this.panelContext`, `this.panelContext.contentWindow`

## ChildDevToolsPanel.recvPanelHidden()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## ChildDevToolsPanel.api()
- 位置: L87-119
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.context`

## register()
- 位置: L92-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.asyncWithoutClone()`

## register()
- 位置: L106-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L107-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## ChildDevToolsPanel.close()
- 位置: L121-124
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._panelContext`, `this.context`

## ChildDevToolsInspectorSidebar.constructor()
- 位置: L137-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.openConduit()`, `super()`, `this.context.callOnClose()`
- 参照: `this.conduit`, `this.context`, `this.id`

## ChildDevToolsInspectorSidebar.close()
- 位置: L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.context`

## ChildDevToolsInspectorSidebar.recvInspectorSidebarShown()
- 位置: L154-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## ChildDevToolsInspectorSidebar.recvInspectorSidebarHidden()
- 位置: L159-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`

## ChildDevToolsInspectorSidebar.api()
- 位置: L163-242
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `context.uri.spec`

## resolveExtensionURL()
- 位置: L171-184
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `context.cloneScope.Error`, `context.uri.spec`, `extensionURL.host`, `extensionURL.protocol`, `sidebarPageURL.host`, `sidebarPageURL.href`, `sidebarPageURL.protocol`

## register()
- 位置: L190-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L191-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.asyncWithoutClone()`

## register()
- 位置: L204-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`, `this.on()`

## listener()
- 位置: L205-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## ChildDevToolsInspectorSidebar.setPage()
- 位置: L215-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `resolveExtensionURL()`

## ChildDevToolsInspectorSidebar.setObject()
- 位置: L224-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`

## ChildDevToolsInspectorSidebar.setExpression()
- 位置: L233-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`

## getAPI()
- 位置: L246-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionChildDevToolsUtils.getThemeChangeObserver()`

## createSidebarPane()
- 位置: L254-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`, `sidebar.api()`
- 参照: `context.cloneScope`

## create()
- 位置: L280-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `context.childManager.callParentAsyncFunction()`, `context.cloneScope.Promise.resolve()`, `context.cloneScope.Promise.resolve().then()`, `devtoolsPanel.api()`
- 参照: `context.cloneScope`

## themeName()
- 位置: L304-306
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `themeChangeObserver.themeName`

## register()
- 位置: L310-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `themeChangeObserver.off()`, `themeChangeObserver.on()`

## listener()
- 位置: L311-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`
