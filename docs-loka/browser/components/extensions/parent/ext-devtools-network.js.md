# browser/components/extensions/parent/ext-devtools-network.js

source: browser/components/extensions/parent/ext-devtools-network.js
source-hash: 21bbd252147220d658c81b54d881b3cacf4a6502
lines: 81

## <module>
- 役割: (未記入)

## getAPI()
- 位置: L12-79
- 役割: (未記入)
- 触るとき: (未記入)

## register()
- 位置: L19-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.addOnNavigatedListener()`, `context.removeOnNavigatedListener()`, `promise.then()`

## listener()
- 位置: L20-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## getHAR()
- 位置: L33-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.devToolsToolbox.getHARFromNetMonitor()`

## register()
- 位置: L40-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolbox.addRequestFinishedListener()`, `toolbox.removeRequestFinishedListener()`
- 参照: `context.devToolsToolbox`

## listener()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`

## getContent()
- 位置: async L58-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.reportError()`, `context.devToolsToolbox .fetchResponseContent()`, `context.devToolsToolbox .fetchResponseContent(requestId) .then()`
- 参照: `content.mimeType`, `content.text`, `context.extension.policy.debugName`
