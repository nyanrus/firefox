# browser/base/content/aboutTabCrashed.js

source: browser/base/content/aboutTabCrashed.js
source-hash: 602f7fe79f0bcb9e34d975eb7f5347132c4969bc
lines: 263

## <module>
- 役割: (未記入)
- 呼び出し先: `AboutTabCrashed.init()`

## pageData()
- 位置: L31-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.replace()`, `decodeURIComponent()`, `queryString.match()`
- 参照: `document.documentURI`, `this.pageData`

## init()
- 位置: L47-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addEventListener()`
- 参照: `document.title`, `this.pageData.title`

## receiveMessage()
- 位置: L53-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onCrashReportSent()`, `this.onSetCrashReportAvailable()`, `this.setMultiple()`
- 参照: `message.data.count`, `message.name`

## handleEvent()
- 位置: L70-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onClick()`, `this.onDOMContentLoaded()`
- 参照: `event.type`

## onDOMContentLoaded()
- 位置: L83-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMAddMessageListener()`, `RPMSendAsyncMessage()`, `document.dispatchEvent()`, `document.getElementById()`, `el.addEventListener()`, `this.CLICK_TARGETS.forEach()`, `this.MESSAGES.forEach()`, `this.receiveMessage.bind()`

## onClick()
- 位置: L100-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendMessage()`, `this.showCrashReportUI()`
- 参照: `event.target.checked`, `event.target.id`

## onSetCrashReportAvailable()
- 位置: L148-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`
- 条件付き依存: `if (data.hasReport)` → `document.documentElement.classList.add()`
- 条件付き依存: `if (data.hasReport)` → `document.getElementById()`
- 条件付き依存: `if (data.hasReport)` → `this.showCrashReportUI()`
- 条件付き依存: `if (!(data.hasReport))` → `this.showCrashReportUI()`
- 条件付き依存: `if (data.requestAutoSubmit)` → `document.getElementById()`
- 参照: `data.hasReport`, `data.includeURL`, `data.requestAutoSubmit`, `data.sendReport`, `document.getElementById("includeURL").checked`, `document.getElementById("requestAutoSubmit").hidden`, `document.getElementById("sendReport").checked`, `message.data`, `this.hasReport`

## onCrashReportSent()
- 位置: L175-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.classList.add()`, `document.documentElement.classList.remove()`

## showCrashReportUI()
- 位置: L186-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `options.hidden`

## setMultiple()
- 位置: L199-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `main.setAttribute()`
- 条件付き依存: `if (hasMultiple)` → `restoreTab.classList.remove()`
- 条件付き依存: `if (!(hasMultiple))` → `restoreTab.classList.add()`

## sendMessage()
- 位置: L223-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `document.getElementById()`
- 条件付き依存: `if (this.hasReport)` → `document.getElementById()`
- 条件付き依存: `if (sendReport)` → `document.getElementById("comments").value.trim()`
- 条件付き依存: `if (sendReport)` → `document.getElementById()`
- 条件付き依存: `if (includeURL)` → `this.pageData.URL.trim()`
- 条件付き依存: `if (!(requestAutoSubmit.hidden))` → `document.getElementById()`
- 参照: `document.getElementById("autoSubmit").checked`, `document.getElementById("includeURL").checked`, `document.getElementById("sendReport").checked`, `requestAutoSubmit.hidden`, `this.hasReport`
