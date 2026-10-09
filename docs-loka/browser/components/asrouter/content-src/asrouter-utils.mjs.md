# browser/components/asrouter/content-src/asrouter-utils.mjs

source: browser/components/asrouter/content-src/asrouter-utils.mjs
source-hash: f728f6abf5cda7866afe39d16d6a3d32ec9f27c2
lines: 108

## <module>
- 役割: (未記入)

## addListener()
- 位置: L8-12
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (globalThis.ASRouterAddParentListener)` → `globalThis.ASRouterAddParentListener()`
- 参照: `globalThis.ASRouterAddParentListener`

## removeListener()
- 位置: L13-17
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (globalThis.ASRouterRemoveParentListener)` → `globalThis.ASRouterRemoveParentListener()`
- 参照: `globalThis.ASRouterRemoveParentListener`

## sendMessage()
- 位置: L18-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`
- 条件付き依存: `if (globalThis.ASRouterMessage)` → `globalThis.ASRouterMessage()`
- 参照: `globalThis.ASRouterMessage`

## blockById()
- 位置: L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.BLOCK_MESSAGE_BY_ID`

## modifyMessageJson()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.MODIFY_MESSAGE_JSON`

## executeAction()
- 位置: L36-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.USER_ACTION`

## unblockById()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.UNBLOCK_MESSAGE_BY_ID`

## unblockAll()
- 位置: L48-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.UNBLOCK_ALL`

## resetGroupImpressions()
- 位置: L53-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.RESET_GROUPS_STATE`

## resetMessageImpressions()
- 位置: L58-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.RESET_MESSAGE_STATE`

## resetScreenImpressions()
- 位置: L63-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.RESET_SCREEN_IMPRESSIONS`

## blockBundle()
- 位置: L68-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.BLOCK_BUNDLE`

## unblockBundle()
- 位置: L74-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.UNBLOCK_BUNDLE`

## overrideMessage()
- 位置: L80-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.OVERRIDE_MESSAGE`

## editState()
- 位置: L86-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.EDIT_STATE`

## openPBWindow()
- 位置: L92-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`

## sendTelemetry()
- 位置: L98-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.AS_ROUTER_TELEMETRY_USER_EVENT`

## getPreviewEndpoint()
- 位置: L104-106
- 役割: (未記入)
- 触るとき: (未記入)
