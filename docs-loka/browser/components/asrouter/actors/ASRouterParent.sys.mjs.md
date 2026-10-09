# browser/components/asrouter/actors/ASRouterParent.sys.mjs

source: browser/components/asrouter/actors/ASRouterParent.sys.mjs
source-hash: 779bb026caf98a56605def0a0893f2c8198aac1b
lines: 98

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## ASRouterTabs.constructor()
- 位置: L17-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterDefaultConfig()`, `asRouterNewTabHook .getInstance()`, `asRouterNewTabHook .getInstance() .then()`, `asRouterNewTabHook.createInstance()`, `initializer.connect()`
- 参照: `this.actors`, `this.destroy`, `this.loadingMessageHandler`

## this.destroy()
- 位置: L19-19
- 役割: (未記入)
- 触るとき: (未記入)

## clearChildMessages()
- 位置: L27-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messageAll()`

## clearChildProviders()
- 位置: L28-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messageAll()`

## updateAdminState()
- 位置: L29-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messageAll()`

## this.destroy()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `initializer.disconnect()`

## ASRouterTabs.size()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.actors.size`

## ASRouterTabs.messageAll()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `[...this.actors].map()`, `a.sendAsyncMessage()`
- 参照: `this.actors`

## ASRouterTabs.registerActor()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actors.add()`

## ASRouterTabs.unregisterActor()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.actors.delete()`

## defaultTabsFactory()
- 位置: L57-58
- 役割: (未記入)
- 触るとき: (未記入)

## ASRouterParent.constructor()
- 位置: L65-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.tabsFactory`

## ASRouterParent.actorCreated()
- 位置: L70-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterParent.tabs.registerActor()`, `this.tabsFactory()`
- 参照: `ASRouterParent.nextTabId`, `ASRouterParent.tabs`, `this.tabId`, `this.tabsFactory`

## ASRouterParent.didDestroy()
- 位置: L77-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterParent.tabs.unregisterActor()`
- 条件付き依存: `if (ASRouterParent.tabs.size < 1)` → `ASRouterParent.tabs.destroy()`
- 参照: `ASRouterParent.tabs`, `ASRouterParent.tabs.size`

## ASRouterParent.getTab()
- 位置: L85-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.browsingContext.embedderElement`, `this.tabId`

## ASRouterParent.receiveMessage()
- 位置: L92-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterParent.tabs.loadingMessageHandler.then()`, `handler.handleMessage()`, `this.getTab()`
