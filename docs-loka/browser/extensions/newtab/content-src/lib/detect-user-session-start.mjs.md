# browser/extensions/newtab/content-src/lib/detect-user-session-start.mjs

source: browser/extensions/newtab/content-src/lib/detect-user-session-start.mjs
source-hash: e573c33c23f8ae0be49291d52f935549f158a350
lines: 87

## <module>
- 役割: (未記入)

## DetectUserSessionStart.constructor()
- 位置: L15-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onVisibilityChange.bind()`
- 参照: `globalThis.document`, `options.document`, `options.perfService`, `this._onVisibilityChange`, `this._perfService`, `this._store`, `this.document`

## DetectUserSessionStart.sendEventOrAddListener()
- 位置: L29-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.document.visibilityState === VISIBLE)` → `this._sendEvent()`
- 条件付き依存: `if (!(this.document.visibilityState === VISIBLE))` → `this.document.addEventListener()`
- 参照: `this._onVisibilityChange`, `this.document.visibilityState`

## DetectUserSessionStart._sendEvent()
- 位置: L48-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`, `this._perfService.getMostRecentAbsMarkStartByName()`, `this._perfService.mark()`, `this._store.dispatch()`
- 参照: `at.SAVE_SESSION_PERF_DATA`, `window.innerHeight`, `window.innerWidth`

## DetectUserSessionStart._onVisibilityChange()
- 位置: L77-85
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.document.visibilityState === VISIBLE)` → `this._sendEvent()`
- 条件付き依存: `if (this.document.visibilityState === VISIBLE)` → `this.document.removeEventListener()`
- 参照: `this._onVisibilityChange`, `this.document.visibilityState`
