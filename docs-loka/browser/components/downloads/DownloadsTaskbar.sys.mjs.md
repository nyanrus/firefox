# browser/components/downloads/DownloadsTaskbar.sys.mjs

source: browser/components/downloads/DownloadsTaskbar.sys.mjs
source-hash: dabc7df9b7d9bd9bdaac6d985d5ccd7499c275a8
lines: 342

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/macdocksupport;1"].getService()`, `Cc["@mozilla.org/widget/taskbarprogress/gtk;1"].getService()`, `Cc["@mozilla.org/windows-taskbar;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `defineResettableGetter()`

## defineResettableGetter()
- 位置: L14-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`

## get()
- 位置: L18-24
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof result == "undefined")` → `callback()`

## set()
- 位置: L25-31
- 役割: (未記入)
- 触るとき: (未記入)

## DownloadsTaskbarInstance.constructor()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#filter`

## DownloadsTaskbarInstance.registerIndicator()
- 位置: async L125-173
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aForcedBackend == "windows" || (!aForcedBackend && gInterfaces.winTaskbar) )` → `this.#windowsAttachIndicator()`
- 条件付き依存: `if ( aForcedBackend == "mac" || (!aForcedBackend && gInterfaces.macTaskbarProgress) )` → `this.#taskbarProgresses.add()`
- 条件付き依存: `if ( aForcedBackend == "mac" || (!aForcedBackend && gInterfaces.macTaskbarProgress) )` → `Services.obs.addObserver()`
- 条件付き依存: `if ( aForcedBackend == "mac" || (!aForcedBackend && gInterfaces.macTaskbarProgress) )` → `this.#taskbarProgresses.clear()`
- 条件付き依存: `if ( aForcedBackend == "linux" || (!aForcedBackend && gInterfaces.gtkTaskbarProgress) )` → `this.#taskbarProgresses.add()`
- 条件付き依存: `if ( aForcedBackend == "linux" || (!aForcedBackend && gInterfaces.gtkTaskbarProgress) )` → `this.#attachGtkTaskbarProgress()`
- 条件付き依存: `if (!this.#summary)` → `lazy.Downloads.getSummary()`
- 条件付き依存: `if (!this.#summary)` → `this.#summary.addView()`
- 条件付き依存: `if (!this.#summary)` → `console.error()`
- 参照: `gInterfaces.gtkTaskbarProgress`, `gInterfaces.macTaskbarProgress`, `gInterfaces.winTaskbar`, `this.#filter`, `this.#summary`, `this.#taskbarProgresses.size`
- XPCOM: `Services.obs`

## DownloadsTaskbarInstance.#windowsAttachIndicator()
- 位置: L178-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.addEventListener()`, `gInterfaces.winTaskbar.getTaskbarProgress()`, `this.#taskbarProgresses.add()`, `this.#taskbarProgresses.delete()`
- 条件付き依存: `if (this.#summary)` → `this.onSummaryChanged()`
- 参照: `aWindow.browsingContext.topChromeWindow`, `this.#summary`

## DownloadsTaskbarInstance.#attachGtkTaskbarProgress()
- 位置: L201-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.addEventListener()`, `taskbarProgress.setPrimaryWindow()`, `this.#determineProgressRepresentative()`, `this.#taskbarProgresses.values()`, `this.#taskbarProgresses.values().next()`
- 条件付き依存: `if (this.#summary)` → `this.onSummaryChanged()`
- 条件付き依存: `if (browserWindow)` → `this.#attachGtkTaskbarProgress()`
- 条件付き依存: `if (!(browserWindow))` → `this.#taskbarProgresses.clear()`
- 参照: `this.#summary`, `this.#taskbarProgresses.values().next().value`

## DownloadsTaskbarInstance.#determineProgressRepresentative()
- 位置: L232-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (this.#filter == lazy.Downloads.ALL)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 参照: `lazy.Downloads.ALL`, `lazy.Downloads.PRIVATE`, `this.#filter`

## DownloadsTaskbarInstance.reset()
- 位置: L242-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#taskbarProgresses.clear()`
- 条件付き依存: `if (this.#summary)` → `this.#summary.removeView()`
- 参照: `this.#summary`

## DownloadsTaskbarInstance.updateProgress()
- 位置: L257-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `progress.setProgressState()`
- 参照: `this.#taskbarProgresses`

## DownloadsTaskbarInstance.onSummaryChanged()
- 位置: L265-289
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#summary.allHaveStopped || this.#summary.progressTotalBytes == 0)` → `this.updateProgress()`
- 条件付き依存: `if (this.#summary.allUnknownSize)` → `this.updateProgress()`
- 条件付き依存: `if (!(this.#summary.allUnknownSize))` → `Math.min()`
- 条件付き依存: `if (!(this.#summary.allUnknownSize))` → `this.updateProgress()`
- 参照: `Ci.nsITaskbarProgress.STATE_INDETERMINATE`, `Ci.nsITaskbarProgress.STATE_NORMAL`, `Ci.nsITaskbarProgress.STATE_NO_PROGRESS`, `this.#summary.allHaveStopped`, `this.#summary.allUnknownSize`, `this.#summary.progressCurrentBytes`, `this.#summary.progressTotalBytes`, `this.#taskbarProgresses.size`
- XPCOM: `nsITaskbarProgress`

## registerIndicator()
- 位置: async L295-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gDownloadsTaskbarInstances[filter].registerIndicator()`, `this._selectFilterForWindow()`

## _selectFilterForWindow()
- 位置: L307-329
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( aForcedBackend == "windows" || (!aForcedBackend && gInterfaces.winTaskbar) )` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `gInterfaces.winTaskbar`, `lazy.Downloads.ALL`, `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`

## resetBetweenTests()
- 位置: L331-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `gDownloadsTaskbarInstances[key].reset()`
- 参照: `gInterfaces.gtkTaskbarProgress`, `gInterfaces.macTaskbarProgress`, `gInterfaces.winTaskbar`
