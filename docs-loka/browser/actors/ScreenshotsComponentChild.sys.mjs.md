# browser/actors/ScreenshotsComponentChild.sys.mjs

source: browser/actors/ScreenshotsComponentChild.sys.mjs
source-hash: 26416f14fc98d5bf560b7b26980d7ccc11724558
lines: 443

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ScreenshotsComponentChild.overlay()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#overlay`

## ScreenshotsComponentChild.receiveMessage()
- 位置: L60-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.clearFocus()`, `this.addEventListeners()`, `this.endScreenshotsOverlay()`, `this.focusOverlay()`, `this.getDocumentTitle()`, `this.getFullPageBounds()`, `this.getMethodsUsed()`, `this.getVisibleBounds()`, `this.removeEventListeners()`, `this.startScreenshotsOverlay()`
- 参照: `message.data`, `message.data?.mode`, `message.name`, `this.contentWindow`, `this.overlay?.initialized`
- XPCOM: `Services.focus`

## ScreenshotsComponentChild.handleEvent()
- 位置: L89-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.screenshots[eventName].record()`, `this.#resizeTask.arm()`, `this.#scrollTask.arm()`, `this.endScreenshotsOverlay()`, `this.requestCancelScreenshot()`, `this.requestCopyScreenshot()`, `this.requestDownloadScreenshot()`, `this.sendAsyncMessage()`, `this.sendOverlaySelection()`
- 条件付き依存: `if ( [ ...ScreenshotsComponentChild.OVERLAY_EVENTS, ...ScreenshotsComponentChild.PREVENTABLE_EVENTS, "selectionchange", ].includes(event.type) )` → `["contextmenu", "pointerdown"].includes()`
- 条件付き依存: `if (!["contextmenu", "pointerdown"].includes(event.type))` → `event.preventDefault()`
- 条件付き依存: `if ( [ ...ScreenshotsComponentChild.OVERLAY_EVENTS, ...ScreenshotsComponentChild.PREVENTABLE_EVENTS, "selectionchange", ].includes(event.type) )` → `event.stopImmediatePropagation()`
- 条件付き依存: `if ( [ ...ScreenshotsComponentChild.OVERLAY_EVENTS, ...ScreenshotsComponentChild.PREVENTABLE_EVENTS, "selectionchange", ].includes(event.type) )` → `this.overlay.handleEvent()`
- 条件付き依存: `if (!this.#resizeTask && this.overlay?.initialized)` → `this.overlay.updateScreenshotsOverlayDimensions()`
- 条件付き依存: `if (!this.#scrollTask && this.overlay?.initialized)` → `this.overlay.updateScreenshotsOverlayDimensions()`
- 参照: `Glean.screenshots`, `ScreenshotsComponentChild.OVERLAY_EVENTS`, `ScreenshotsComponentChild.PREVENTABLE_EVENTS`, `event.detail`, `event.detail.reason`, `event.detail.region`, `event.detail.viewportHeight`, `event.detail.viewportWidth`, `event.isTrusted`, `event.type`, `lazy.DeferredTask`, `this.#resizeTask`, `this.#scrollTask`, `this.overlay?.initialized`

## ScreenshotsComponentChild.requestCancelScreenshot()
- 位置: L181-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.endScreenshotsOverlay()`, `this.sendAsyncMessage()`

## ScreenshotsComponentChild.requestCopyScreenshot()
- 位置: L194-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.endScreenshotsOverlay()`, `this.sendAsyncMessage()`
- 参照: `region.devicePixelRatio`, `this.contentWindow.devicePixelRatio`

## ScreenshotsComponentChild.requestDownloadScreenshot()
- 位置: L205-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.endScreenshotsOverlay()`, `this.getDocumentTitle()`, `this.sendAsyncMessage()`
- 参照: `region.devicePixelRatio`, `this.contentWindow.devicePixelRatio`

## ScreenshotsComponentChild.getDocumentTitle()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.document.title`

## ScreenshotsComponentChild.sendOverlaySelection()
- 位置: L218-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## ScreenshotsComponentChild.getMethodsUsed()
- 位置: L222-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#overlay.resetMethodsUsed()`
- 参照: `this.#overlay.methodsUsed`

## ScreenshotsComponentChild.focusOverlay()
- 位置: L228-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#overlay.focus()`, `this.contentWindow.focus()`

## ScreenshotsComponentChild.documentIsReady()
- 位置: L239-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `readyEnough()`, `this.contentWindow.addEventListener()`
- 条件付き依存: `if (readyEnough())` → `Promise.resolve()`
- 参照: `this.document`

## readyEnough()
- 位置: L243-247
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.documentElement`, `document.readyState`

## onChange()
- 位置: L253-263
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "pagehide")` → `document.removeEventListener()`
- 条件付き依存: `if (event.type === "pagehide")` → `this.contentWindow.removeEventListener()`
- 条件付き依存: `if (event.type === "pagehide")` → `reject()`
- 条件付き依存: `if (!(event.type === "pagehide"))` → `readyEnough()`
- 条件付き依存: `if (readyEnough())` → `document.removeEventListener()`
- 条件付き依存: `if (readyEnough())` → `this.contentWindow.removeEventListener()`
- 条件付き依存: `if (readyEnough())` → `resolve()`
- 参照: `event.type`

## ScreenshotsComponentChild.addEventListeners()
- 位置: L269-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addOverlayEventListeners()`, `this.contentWindow.addEventListener()`

## ScreenshotsComponentChild.addOverlayEventListeners()
- 位置: L276-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `chromeEventHandler.addEventListener()`, `this.document.addEventListener()`
- 条件付き依存: `if (Services.prefs.getBoolPref(SCREENSHOTS_PREVENT_CONTENT_EVENTS_PREF))` → `chromeEventHandler.addEventListener()`
- 参照: `ScreenshotsComponentChild.OVERLAY_EVENTS`, `ScreenshotsComponentChild.PREVENTABLE_EVENTS`, `this.#preventableEventsAdded`, `this.docShell.chromeEventHandler`
- XPCOM: `Services.prefs`

## ScreenshotsComponentChild.startScreenshotsOverlay()
- 位置: async L300-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `overlay.initialize()`, `this.addEventListeners()`, `this.documentIsReady()`
- 参照: `SELECTION_MODES.SCREENSHOTS`, `ex.message`, `lazy.ScreenshotsOverlay`, `this.#overlay`, `this.document`, `this.overlay`

## ScreenshotsComponentChild.removeEventListeners()
- 位置: L318-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.removeEventListener()`, `this.removeOverlayEventListeners()`

## ScreenshotsComponentChild.removeOverlayEventListeners()
- 位置: L325-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeEventHandler.removeEventListener()`, `this.document.removeEventListener()`
- 条件付き依存: `if (this.#preventableEventsAdded)` → `chromeEventHandler.removeEventListener()`
- 参照: `ScreenshotsComponentChild.OVERLAY_EVENTS`, `ScreenshotsComponentChild.PREVENTABLE_EVENTS`, `this.#preventableEventsAdded`, `this.docShell.chromeEventHandler`

## ScreenshotsComponentChild.endScreenshotsOverlay()
- 位置: L345-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resizeTask?.disarm()`, `this.#scrollTask?.disarm()`, `this.overlay?.tearDown()`, `this.removeEventListeners()`

## ScreenshotsComponentChild.didDestroy()
- 位置: L353-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resizeTask?.disarm()`, `this.#scrollTask?.disarm()`

## ScreenshotsComponentChild.getFullPageBounds()
- 位置: L380-398
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#overlay.windowDimensions.dimensions`

## ScreenshotsComponentChild.getVisibleBounds()
- 位置: L423-441
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#overlay.windowDimensions.dimensions`
