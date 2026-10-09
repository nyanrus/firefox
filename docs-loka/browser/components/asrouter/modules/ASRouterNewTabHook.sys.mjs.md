# browser/components/asrouter/modules/ASRouterNewTabHook.sys.mjs

source: browser/components/asrouter/modules/ASRouterNewTabHook.sys.mjs
source-hash: 53e825db9381be3175282677b6f0abb621d2f28d
lines: 117

## <module>
- 役割: (未記入)

## ASRouterNewTabHookInstance.constructor()
- 位置: L6-22
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._clearChildMessages`, `this._clearChildProviders`, `this._newTabMessageHandler`, `this._parentProcessMessageHandler`, `this._router`, `this._updateAdminState`

## this._clearChildMessages()
- 位置: L10-13
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `this._newTabMessageHandler.clearChildMessages()`
- 参照: `this._newTabMessageHandler`

## this._clearChildProviders()
- 位置: L14-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `this._newTabMessageHandler.clearChildProviders()`
- 参照: `this._newTabMessageHandler`

## this._updateAdminState()
- 位置: L18-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `this._newTabMessageHandler.updateAdminState()`
- 参照: `this._newTabMessageHandler`

## ASRouterNewTabHookInstance.initialize()
- 位置: async L36-50
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._router.initialized)` → `createStorage()`
- 条件付き依存: `if (!this._router.initialized)` → `this._router.init()`
- 参照: `this._clearChildMessages`, `this._clearChildProviders`, `this._parentProcessMessageHandler`, `this._parentProcessMessageHandler.handleCFRAction`, `this._parentProcessMessageHandler.handleTelemetry`, `this._router`, `this._router.initialized`, `this._updateAdminState`

## ASRouterNewTabHookInstance.destroy()
- 位置: L52-57
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._router?.initialized)` → `this.disconnect()`
- 条件付き依存: `if (this._router?.initialized)` → `this._router.uninit()`
- 参照: `this._router?.initialized`

## ASRouterNewTabHookInstance.connect()
- 位置: L70-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._newTabMessageHandler`, `this._parentProcessMessageHandler`

## ASRouterNewTabHookInstance.disconnect()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._newTabMessageHandler`

## AwaitSingleton.constructor()
- 位置: L84-94
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.getInstance`, `this.instance`, `this.setInstance`

## this.setInstance()
- 位置: L87-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`
- 参照: `this.instance`, `this.setInstance`

## this.setInstance()
- 位置: L88-88
- 役割: (未記入)
- 触るとき: (未記入)

## this.getInstance()
- 位置: L93-93
- 役割: (未記入)
- 触るとき: (未記入)

## createInstance()
- 位置: async L107-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `instance.initialize()`, `singleton.setInstance()`

## destroy()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `instance.destroy()`
