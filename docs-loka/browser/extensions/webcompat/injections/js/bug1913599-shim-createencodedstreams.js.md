# browser/extensions/webcompat/injections/js/bug1913599-shim-createencodedstreams.js

source: browser/extensions/webcompat/injections/js/bug1913599-shim-createencodedstreams.js
source-hash: f86a0f7d9a7240ebd069c953f965f7b15547311f
lines: 83

## <module>
- 役割: (未記入)

## createEncodedStreams()
- 位置: L31-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `haveData .then()`, `haveData .then(({ readable }) => readable.pipeTo(readableNow.writable)) .catch()`, `haveData .then(({ writable }) => writableNow.readable.pipeTo(writable)) .catch()`, `readable.pipeTo()`, `readableNow.writable.abort()`, `work.toString()`, `writableNow.readable.cancel()`, `writableNow.readable.pipeTo()`
- 参照: `readableNow.readable`, `readableNow.writable`, `this._dummy`, `this._worker`, `this._worker.onmessage`, `this.transform`, `window.RTCRtpScriptTransform`, `writableNow.writable`

## work()
- 位置: L33-60
- 役割: (未記入)
- 触るとき: (未記入)

## onrtctransform()
- 位置: async L35-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `readable .pipeThrough()`, `readable .pipeThrough({ writable: diverter.writable, readable: reinserter.readable, }) .pipeTo()`, `self.postMessage()`
- 参照: `diverter.readable`, `diverter.writable`, `reinserter.readable`, `reinserter.writable`

## transform()
- 位置: L37-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.enqueue()`, `originals.push()`

## transform()
- 位置: L43-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.enqueue()`, `originals.shift()`
- 参照: `frame.data`, `original.data`

## this._worker.onmessage()
- 位置: L69-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `r()`
- 参照: `e.data`
