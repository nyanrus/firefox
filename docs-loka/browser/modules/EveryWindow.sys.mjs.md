# browser/modules/EveryWindow.sys.mjs

source: browser/modules/EveryWindow.sys.mjs
source-hash: 64e7cbaa31be611c2d2d8ffb40f77359dbb5156f
lines: 115

## <module>
- 役割: (未記入)

## callForEveryWindow()
- 位置: L30-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `callback()`, `win.delayedStartupPromise.then()`
- XPCOM: `Services.wm`

## readyWindows()
- 位置: L43-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(Services.wm.getEnumerator("navigator:browser")).filter()`, `Services.wm.getEnumerator()`
- 参照: `win.gBrowserInit?.delayedStartupFinished`
- XPCOM: `Services.wm`

## EW_registerCallback()
- 位置: L60-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callForEveryWindow()`, `callbacks.has()`, `callbacks.set()`
- 条件付き依存: `if (!initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!initialized)` → `callbacks.values()`
- 条件付き依存: `if (!initialized)` → `c.init()`
- 条件付き依存: `if (!initialized)` → `addUnloadListener()`
- 条件付き依存: `if (!initialized)` → `callForEveryWindow()`
- XPCOM: `Services.obs`

## addUnloadListener()
- 位置: L66-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ww.registerNotification()`
- XPCOM: `Services.ww`

## observer()
- 位置: L67-74
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "domwindowclosed" && subject === win)` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (topic == "domwindowclosed" && subject === win)` → `callbacks.values()`
- 条件付き依存: `if (topic == "domwindowclosed" && subject === win)` → `c.uninit()`
- XPCOM: `Services.ww`

## EW_unregisterCallback()
- 位置: L103-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callbacks.delete()`, `callbacks.has()`
- 条件付き依存: `if (callUninit)` → `callForEveryWindow()`
- 条件付き依存: `if (callUninit)` → `callbacks.get()`
- 参照: `callbacks.get(id).uninit`
