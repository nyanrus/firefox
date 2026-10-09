# browser/extensions/webcompat/lib/custom_functions.js

source: browser/extensions/webcompat/lib/custom_functions.js
source-hash: cb3b5993195f5c0910420e60aa6c6a8a830f0c75
lines: 194

## <module>
- 役割: (未記入)
- 呼び出し先: `makeHeaderAlterer()`

## replaceStringInRequest()
- 位置: L9-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webRequest.filterResponseData()`
- 参照: `filter.ondata`, `filter.onstop`, `inString.length`

## filter.ondata()
- 位置: L22-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( carryover + decoder.decode(event.data, { stream: true }) ).replace()`, `decoder.decode()`, `encoder.encode()`, `filter.write()`, `replaced.slice()`
- 参照: `event.data`

## filter.onstop()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filter.close()`
- 条件付き依存: `if (carryover.length)` → `filter.write()`
- 条件付き依存: `if (carryover.length)` → `encoder.encode()`
- 参照: `carryover.length`

## rememberListener()
- 位置: L40-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `interventionListeners.get()`, `interventionListeners.has()`, `map.has()`, `map.set()`
- 条件付き依存: `if (!interventionListeners.has(intervention))` → `interventionListeners.set()`

## forgetListener()
- 位置: L51-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `interventionListeners.get()`, `map.delete()`, `map.get()`

## makeHeaderAlterer()
- 位置: L61-124
- 役割: (未記入)
- 触るとき: (未記入)

## getKey()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`

## enable()
- 位置: L68-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webRequest[webRequestAPI].addListener()`, `rememberListener()`, `this.getKey()`
- 条件付き依存: `if (!urls)` → `Object.values(intervention.bugs) .map(bug => bug.matches) .flat() .filter()`
- 条件付き依存: `if (!urls)` → `Object.values(intervention.bugs) .map(bug => bug.matches) .flat()`
- 条件付き依存: `if (!urls)` → `Object.values(intervention.bugs) .map()`
- 条件付き依存: `if (!urls)` → `Object.values()`
- 参照: `browser.webRequest`, `bug.matches`, `intervention.bugs`

## listener()
- 位置: L78-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `header.name.toLowerCase()`, `headers.includes()`
- 条件付き依存: `if ( regex !== null && replacement !== null && replacement !== undefined )` → `header.value.replaceAll()`
- 条件付き依存: `if ( regex !== null && replacement !== null && replacement !== undefined )` → `finalHeaders.push()`
- 条件付き依存: `if (replacement !== null)` → `finalHeaders.push()`
- 条件付き依存: `if (!(headers.includes(header.name.toLowerCase())))` → `finalHeaders.push()`
- 条件付き依存: `if (value !== null)` → `finalHeaders.push()`
- 参照: `header.name`

## disable()
- 位置: L117-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `forgetListener()`, `this.getKey()`
- 条件付き依存: `if (listener)` → `browser.webRequest[webRequestAPI].removeListener()`
- 参照: `browser.webRequest`

## enable()
- 位置: L132-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webRequest.onBeforeRequest.addListener()`
- 参照: `details.listener`

## details.listener()
- 位置: L134-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `replaceStringInRequest()`

## disable()
- 位置: L144-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webRequest.onBeforeRequest.removeListener()`
- 参照: `details.listener`

## enable()
- 位置: L153-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webRequest.onBeforeRequest.addListener()`
- 参照: `details.listener`

## details.listener()
- 位置: L158-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `browser.tabs .executeScript()`, `browser.tabs .executeScript(tabId, { file: script, frameId, runAt: "document_start", }) .then()`, `browser.tabs.executeScript()`, `console.error()`

## disable()
- 位置: L187-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.webRequest.onBeforeRequest.removeListener()`
- 参照: `details.listener`
