# browser/components/preferences/DefaultBrowserHelper.mjs

source: browser/components/preferences/DefaultBrowserHelper.mjs
source-hash: b8a600cb5d888cdfa37ad53fd6c6b8678b8c52e2
lines: 196

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## shellSvc()
- 位置: L66-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.getShellService()`
- 参照: `AppConstants.HAVE_SHELL_SERVICE`

## pollForDefaultChanges()
- 位置: L85-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._changeListeners.add()`, `this._changeListeners.delete()`
- 条件付き依存: `if (!this._pollingTimer)` → `window.setTimeout()`
- 条件付き依存: `if (!this._pollingTimer)` → `window.requestIdleCallback()`
- 条件付き依存: `if (!this._changeListeners.size)` → `this.clearPollingForDefaultChanges()`
- 参照: `this._backoffIndex`, `this._changeListeners.size`, `this._lastPolledIsDefault`, `this._pollingTimer`, `this.isBrowserDefault`

## pollForDefaultBrowser()
- 位置: L97-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.requestIdleCallback()`, `window.setTimeout()`
- 条件付き依存: `if (isBrowserDefault !== this._lastPolledIsDefault)` → `listener()`
- 参照: `backoffTimes.length`, `document.visibilityState`, `location.hash`, `this._backoffIndex`, `this._changeListeners`, `this._lastPolledIsDefault`, `this._pollingTimer`

## clearPollingForDefaultChanges()
- 位置: L147-152
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._pollingTimer)` → `clearTimeout()`
- 参照: `this._pollingTimer`

## isBrowserDefault()
- 位置: L157-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shellSvc?.isDefaultBrowser()`
- 参照: `this.canCheck`

## setDefaultBrowser()
- 位置: async L170-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.shellSvc?.setDefaultBrowser()`
- 参照: `this._backoffIndex`

## canCheck()
- 位置: L186-194
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.gGIOService?.isRunningUnderFlatpak`, `this.shellSvc`
