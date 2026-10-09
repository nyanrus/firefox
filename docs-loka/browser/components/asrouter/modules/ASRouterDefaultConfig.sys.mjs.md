# browser/components/asrouter/modules/ASRouterDefaultConfig.sys.mjs

source: browser/components/asrouter/modules/ASRouterDefaultConfig.sys.mjs
source-hash: 1f83fb3b4106b270465edbfe2f7458640a94e814
lines: 74

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## createStorage()
- 位置: async L29-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.reject()`, `dbStore.flush()`, `dbStore.getDbTable()`, `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`
- 参照: `dbStore.db`

## handleUndesiredEvent()
- 位置: L39-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `telemetryFeed.SendASRouterUndesiredEvent()`

## fetchState()
- 位置: L53-53
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `dbStore.pendingWriteCount`

## ASRouterDefaultConfig()
- 位置: L58-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createStorage.bind()`, `telemetry.onAction.bind()`
