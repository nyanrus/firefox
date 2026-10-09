# browser/extensions/newtab/lib/cache.worker.js

source: browser/extensions/newtab/lib/cache.worker.js
source-hash: 990533e4ca9ee2a1457eb2a6c341daa11255d13c
lines: 207

## <module>
- 役割: (未記入)
- 呼び出し先: `importScripts()`, `require()`, `self.addEventListener()`, `worker.handleMessage()`

## window.requestAnimationFrame()
- 位置: L15-15
- 役割: (未記入)
- 触るとき: (未記入)

## window.cancelAnimationFrame()
- 位置: L16-16
- 役割: (未記入)
- 触るとき: (未記入)

## window.matchMedia()
- 位置: L17-21
- 役割: (未記入)
- 触るとき: (未記入)

## addEventListener()
- 位置: L19-19
- 役割: (未記入)
- 触るとき: (未記入)

## removeEventListener()
- 位置: L20-20
- 役割: (未記入)
- 触るとき: (未記入)

## getOrCreateTemplates()
- 位置: L67-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `xhr.open()`, `xhr.send()`
- 参照: `this._templates`, `xhr.responseText`, `xhr.responseType`

## construct()
- 位置: L109-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._construct()`

## _construct()
- 位置: L146-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `NewtabRenderUtils.NewTab()`, `Object.keys()`, `ReactDOMServer.renderToString()`, `new Date().toUTCString()`, `pageTemplate .replace()`, `pageTemplate .replace("{{ MARKUP }}", markup) .replace()`, `scriptTemplate.replace()`, `this.getOrCreateTemplates()`
- 参照: `self.document`, `state.App.isForStartupCache`

## getState()
- 位置: L162-164
- 役割: (未記入)
- 触るとき: (未記入)

## dispatch()
- 位置: L165-165
- 役割: (未記入)
- 触るとき: (未記入)

## worker.dispatch()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Agent[method]()`

## worker.postMessage()
- 位置: L196-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.postMessage()`

## worker.close()
- 位置: L199-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `self.close()`
