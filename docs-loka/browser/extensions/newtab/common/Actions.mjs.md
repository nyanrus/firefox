# browser/extensions/newtab/common/Actions.mjs

source: browser/extensions/newtab/common/Actions.mjs
source-hash: 12295912fcfe13de7e58c5cef5fbec3685696b9f
lines: 580

## <module>
- 役割: (未記入)

## _RouteMessage()
- 位置: L293-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["from", "to", "toTarget", "fromTarget", "skipMain", "skipLocal"].forEach()`
- 参照: `action.meta`, `options.from`, `options.to`

## AlsoToMain()
- 位置: L322-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_RouteMessage()`

## OnlyToMain()
- 位置: L338-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`

## BroadcastToContent()
- 位置: L349-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_RouteMessage()`

## AlsoToOneContent()
- 位置: L366-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_RouteMessage()`

## OnlyToOneContent()
- 位置: L388-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToOneContent()`

## AlsoToPreloaded()
- 位置: L398-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_RouteMessage()`

## UserEvent()
- 位置: L412-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.TELEMETRY_USER_EVENT`

## DiscoveryStreamUserEvent()
- 位置: L426-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.DISCOVERY_STREAM_USER_EVENT`

## ImpressionStats()
- 位置: L440-446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.TELEMETRY_IMPRESSION_STATS`

## DiscoveryStreamImpressionStats()
- 位置: L455-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.DISCOVERY_STREAM_IMPRESSION_STATS`

## DiscoveryStreamLoadedContent()
- 位置: L473-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.DISCOVERY_STREAM_LOADED_CONTENT`

## SetPref()
- 位置: L484-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.SET_PREF`

## SetMultiplePrefs()
- 位置: L493-499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `actionTypes.SET_MULTIPLE_PREFS`

## WebExtEvent()
- 位置: L501-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AlsoToMain()`
- 参照: `data.source`

## isSendToMain()
- 位置: L530-538
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.meta`, `action.meta.from`, `action.meta.to`

## isBroadcastToContent()
- 位置: L539-547
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.meta`, `action.meta.to`, `action.meta.toTarget`

## isSendToOneContent()
- 位置: L548-556
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.meta`, `action.meta.to`, `action.meta.toTarget`

## isSendToPreloaded()
- 位置: L557-565
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.meta`, `action.meta.from`, `action.meta.to`

## isFromMain()
- 位置: L566-574
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.meta`, `action.meta.from`, `action.meta.to`

## getPortIdOfSender()
- 位置: L575-577
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.meta`, `action.meta.fromTarget`
