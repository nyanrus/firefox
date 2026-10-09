# browser/base/content/spotlight.js

source: browser/base/content/spotlight.js
source-hash: 3de411aa5fbaf87c21e02bcd61972ebedd1eb069
lines: 154

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `document.addEventListener()`, `renderMultistage()`

## addStylesheet()
- 位置: L14-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.head.appendChild()`
- 参照: `link.href`, `link.rel`

## disableEscClose()
- 位置: L20-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener()`
- 条件付き依存: `if (event.key === "Escape")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Escape")` → `event.stopPropagation()`
- 参照: `event.key`

## renderMultistage()
- 位置: L32-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener()`, `addStylesheet()`, `box.classList.add()`, `box.classList.remove()`, `box.closest()`, `box.removeAttribute()`, `box.setAttribute()`, `browser.closest()`, `dialog?.classList.add()`, `dialog?.classList.remove()`, `document.body.classList.add()`, `document.createElement()`, `document.head.appendChild()`, `ready()`, `receive()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `disableEscClose()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `browser.documentGlobal.addEventListener()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `addEventListener()`
- 条件付き依存: `if (CONFIG?.disableEscClose)` → `browser.documentGlobal.removeEventListener()`
- 参照: `CONFIG?.disableEscClose`, `document.body.dataset.page`, `document.body.id`, `document.head.appendChild(document.createElement("script")).src`, `window.AWAddScreenImpression`, `window.AWEvaluateAttributeTargeting`, `window.AWEvaluateScreenTargeting`, `window.AWFinish`, `window.AWGetFeatureConfig`, `window.AWGetInstalledAddons`, `window.AWGetSelectedTheme`, `window.AWPredictRemoteType`, `window.AWSelectTheme`, `window.AWSendEventTelemetry`, `window.AWSendToDeviceEmailsSupported`, `window.AWSendToParent`, `window.AWWaitForMigrationClose`, `window.AWWaitForNimbus`

## receive()
- 位置: L34-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AWParent.onContentMessage()`

## window.AWGetFeatureConfig()
- 位置: L38-38
- 役割: (未記入)
- 触るとき: (未記入)

## window.AWSelectTheme()
- 位置: L41-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data?.toUpperCase()`, `receive()`, `receive("SELECT_THEME")()`

## window.AWSendEventTelemetry()
- 位置: L44-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `telemetryMessageHandler()`
- 参照: `CONFIG.feedbackData`, `CONFIG?.feedbackData`, `CONFIG?.metrics`, `CONFIG?.write_in_microsurvey`, `data.event`, `data.event_context`, `data.event_context.contentToggleState`, `data.event_context.smart_window_user_feedback_data`, `data.event_context.source`, `data.event_context.write_in_microsurvey`, `feedbackDataToSend.chat`

## window.AWSendToParent()
- 位置: L77-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `receive()`, `receive(name)()`

## window.AWFinish()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.close()`

## window.AWPredictRemoteType()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`

## preventEscape()
- 位置: L116-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `box.contains()`, `dialog?.contains()`
- 条件付き依存: `if ( event.key === "Escape" && (dialog?.contains(event.target) || box.contains(event.target)) )` → `event.preventDefault()`
- 条件付き依存: `if ( event.key === "Escape" && (dialog?.contains(event.target) || box.contains(event.target)) )` → `event.stopPropagation()`
- 参照: `event.key`, `event.target`
