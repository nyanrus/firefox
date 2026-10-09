# browser/components/StartupRecorder.sys.mjs

source: browser/components/StartupRecorder.sys.mjs
source-hash: 2f0f1dff85cc85a7806ca449e4904a27c22e4a73
lines: 250

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Cm.QueryInterface()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## afterPaintListener()
- 位置: L36-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `canvas.getContext()`, `ctx.drawWindow()`, `ctx.getImageData()`, `paints.push()`
- 参照: `canvas.height`, `canvas.width`, `ctx.DRAWWINDOW_ASYNC_DECODE_IMAGES`, `ctx.DRAWWINDOW_DO_NOT_FLUSH`, `ctx.DRAWWINDOW_DRAW_VIEW`, `ctx.DRAWWINDOW_USE_WIDGET_LAYERS`, `ctx.getImageData(0, 0, width, height).data`, `win.innerHeight`, `win.innerWidth`

## StartupRecorder()
- 位置: L79-92
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._resolve`, `this.data`, `this.done`, `this.wrappedJSObject`

## record()
- 位置: L97-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Cm.isServiceInstantiatedByContractID()`, `Object.keys()`, `Object.keys(Cc).filter()`
- 参照: `Ci.nsISupports`, `Cu.loadedESModules`, `this.data.code`
- XPCOM: [`nsISupports`](../../netwerk/base/nsIEncodedChannel.idl.md)

## observe()
- 位置: L115-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (!lazy.BROWSER_STARTUP_RECORD && !lazy.BROWSER_STARTUP_RECORD_IMAGES)` → `this._resolve()`
- 条件付き依存: `if (topic == "app-startup" || topic == "content-process-ready-for-script")` → `Services.obs.addObserver()`
- 条件付き依存: `if (subject instanceof Ci.nsIAppWindow)` → `subject .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (subject instanceof Ci.nsIAppWindow)` → `subject .QueryInterface()`
- 条件付き依存: `if (topic == firstPaintNotification)` → `doc.documentElement.getAttribute()`
- 条件付き依存: `if (topic == "image-drawing" || topic == "image-loading")` → `this.data.images[topic].add()`
- 条件付き依存: `if (topic == firstPaintNotification)` → `win.document.createElementNS()`
- 条件付き依存: `if (topic == firstPaintNotification)` → `afterPaintListener()`
- 条件付き依存: `if (topic == firstPaintNotification)` → `win.addEventListener()`
- 条件付き依存: `if (topic == "sessionstore-windows-restored")` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (topic == "sessionstore-windows-restored")` → `this.record.bind()`
- 条件付き依存: `if (lazy.BROWSER_STARTUP_RECORD_IMAGES)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (lazy.BROWSER_STARTUP_RECORD_IMAGES)` → `this._resolve()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `this.record()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `win.removeEventListener()`
- 条件付き依存: `if (AppConstants.DEBUG)` → `Services.prefs.readStats()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `Services.env.exists()`
- 条件付き依存: `if (!Services.env.exists("MOZ_PROFILER_STARTUP_PERFORMANCE_TEST"))` → `this._resolve()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `Services.profiler.getProfileDataAsync().then()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `Services.profiler.getProfileDataAsync()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `Services.profiler.StopProfiler()`
- 条件付き依存: `if (topic == "browser-startup-idle-tasks-finished")` → `this._resolve()`
- 条件付き依存: `if (!(topic == "browser-startup-idle-tasks-finished"))` → `this.record()`
- 参照: `AppConstants.DEBUG`, `Ci.nsIAppWindow`, `Ci.nsIDOMWindow`, `Ci.nsIInterfaceRequestor`, `Services.appinfo.ID`, `canvas.mozOpaque`, `lazy.BROWSER_STARTUP_RECORD`, `lazy.BROWSER_STARTUP_RECORD_IMAGES`, `subject.defaultView`, `subject.document`, `this._resolve`, `this.data.frames`, `this.data.images`, `this.data.prefStats`, `this.data.profile`
- XPCOM: `nsIAppWindow` / [`nsIDOMWindow`](../../dom/base/nsISlowScriptDebug.idl.md) / [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / `Services.appinfo` / `Services.env` / `Services.obs` / `Services.prefs` / `Services.profiler` / `Services.tm`
