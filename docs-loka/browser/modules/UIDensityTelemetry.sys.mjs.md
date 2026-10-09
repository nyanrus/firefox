# browser/modules/UIDensityTelemetry.sys.mjs

source: browser/modules/UIDensityTelemetry.sys.mjs
source-hash: 64e42398c45e6841fc9145a5cf2c1475b2ac09fa
lines: 237

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-ui-utils;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## currentSetting()
- 位置: L31-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`
- 参照: `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_NORMAL`, `gUIDensity.MODE_TOUCH`
- XPCOM: `Services.prefs`

## effectiveDensity()
- 位置: L59-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gUIDensity.getCurrentDensity()`
- 参照: `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_TOUCH`, `gUIDensity.getCurrentDensity().mode`

## touchCapable()
- 位置: L74-84
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `lazy.WindowsUIUtils.isTabletCapable`

## init()
- 位置: async L121-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `effectiveDensity()`, `lazy.BrowserWindowTracker.getTopWindow()`, `this._lastEffective.set()`, `this._record()`
- 参照: `lazy.SessionStore.promiseAllWindowsRestored`, `this._initialized`, `win.toolbar.visible`
- XPCOM: `Services.prefs`

## uninit()
- 位置: L152-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- 参照: `this._autoAdjustments`, `this._current`, `this._initialized`, `this._lastEffective`
- XPCOM: `Services.prefs`

## observe()
- 位置: L164-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (win)` → `this._record()`

## onDensityChanged()
- 位置: L179-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `this._record()`
- 参照: `this._initialized`

## _record()
- 位置: L194-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.uiDensity.mode.record()`, `String()`, `currentSetting()`, `effectiveDensity()`, `this._lastEffective.get()`, `this._lastEffective.set()`, `touchCapable()`
- 参照: `extra.previous`, `this._autoAdjustments`, `this._current`, `win.devicePixelRatio`, `win.outerHeight`, `win.outerWidth`
