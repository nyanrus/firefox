# browser/components/aiwindow/ui/modules/ClientErrorTelemetry.mjs

source: browser/components/aiwindow/ui/modules/ClientErrorTelemetry.mjs
source-hash: 2a2a3bee94b6ada13d29f9cfbeaf86d495d94268
lines: 244

## <module>
- 役割: (未記入)

## asString()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)

## extractClientErrorFields()
- 位置: L83-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `asString()`
- 参照: `error.fileName`, `error.lineNumber`, `error.message`, `error.name`

## normalizeClientErrorMessage()
- 位置: L112-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `asString()`, `asString(message).toLowerCase()`, `text.includes()`
- 条件付き依存: `if (key)` → `CLIENT_ERROR_MESSAGES.has()`
- 条件付き依存: `if (key)` → `console.warn()`
- 条件付き依存: `if (key)` → `JSON.stringify()`

## classifyClientErrorSource()
- 位置: L152-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `error.stack.includes()`
- 参照: `error.stack`

## installClientErrorListeners()
- 位置: L171-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.addEventListener()`, `target.removeEventListener()`

## reportSafely()
- 位置: L172-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classifyClientErrorSource()`, `console.warn()`, `report()`

## onError()
- 位置: L180-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reportSafely()`
- 参照: `event.error`, `event.filename`, `event.lineno`, `event.message`

## onUnhandledRejection()
- 位置: L193-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reportSafely()`
- 参照: `event.reason`

## serializeClientErrorDetail()
- 位置: L216-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `extractClientErrorFields()`

## dispatchClientError()
- 位置: L229-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `serializeClientErrorDetail()`, `target.dispatchEvent()`
- 条件付き依存: `if (error && typeof error === "object")` → `reportedErrors.has()`
- 条件付き依存: `if (error && typeof error === "object")` → `reportedErrors.add()`
