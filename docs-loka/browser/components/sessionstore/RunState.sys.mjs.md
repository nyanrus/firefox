# browser/components/sessionstore/RunState.sys.mjs

source: browser/components/sessionstore/RunState.sys.mjs
source-hash: 94f9a86fcddce87697b65cda2c57f18eaa320315
lines: 93

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## isStopped()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)

## isRunning()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)

## isQuitting()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)

## isClosing()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)

## isClosed()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)

## setRunning()
- 位置: L60-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isStopped`

## setClosing()
- 位置: L69-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isQuitting`

## setClosed()
- 位置: L78-82
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isClosing`

## setQuitting()
- 位置: L87-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.isRunning`
