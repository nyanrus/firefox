# browser/components/extensions/child/ext-devtools-network.js

source: browser/components/extensions/child/ext-devtools-network.js
source-hash: e4981aaa47c51c1dbff723facadfa22b00aa78b2
lines: 69

## <module>
- 役割: (未記入)

## ChildNetworkResponseLoader.constructor()
- 位置: L15-18
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.context`, `this.requestId`

## ChildNetworkResponseLoader.api()
- 位置: L20-31
- 役割: (未記入)
- 触るとき: (未記入)

## ChildNetworkResponseLoader.getContent()
- 位置: L23-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentAsyncFunction()`

## getAPI()
- 位置: L35-67
- 役割: (未記入)
- 触るとき: (未記入)

## register()
- 位置: L42-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.getParentEvent()`, `parent.addListener()`, `parent.removeListener()`

## onFinished()
- 位置: L43-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `fire.asyncWithoutClone()`, `loader.api()`
- 参照: `context.cloneScope`, `data.harEntry`, `data.requestId`
