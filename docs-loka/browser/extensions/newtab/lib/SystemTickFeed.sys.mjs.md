# browser/extensions/newtab/lib/SystemTickFeed.sys.mjs

source: browser/extensions/newtab/lib/SystemTickFeed.sys.mjs
source-hash: c7bb05c87feb297738e9617bb6060a4a95294190
lines: 76

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SystemTickFeed.init()
- 位置: L23-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/useridleservice;1"].getService()`, `this.setTimer()`
- 参照: `Ci.nsIUserIdleService`, `this._hasObserver`, `this._idleService`
- XPCOM: `nsIUserIdleService` / `@mozilla.org/widget/useridleservice;1`

## SystemTickFeed.setTimer()
- 位置: L31-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.setInterval()`, `this.dispatchTick()`
- 条件付き依存: `if (this._idleService.idleTime > SYSTEM_TICK_INTERVAL)` → `this.cancelTimer()`
- 条件付き依存: `if (this._idleService.idleTime > SYSTEM_TICK_INTERVAL)` → `Services.obs.addObserver()`
- 参照: `this._hasObserver`, `this._idleService.idleTime`, `this.intervalId`
- XPCOM: `Services.obs`

## SystemTickFeed.cancelTimer()
- 位置: L43-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clearInterval()`
- 参照: `this.intervalId`

## SystemTickFeed.observe()
- 位置: L48-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this.dispatchTick()`, `this.setTimer()`
- 参照: `this._hasObserver`
- XPCOM: `Services.obs`

## SystemTickFeed.dispatchTick()
- 位置: L55-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`, `this.store.dispatch()`
- 参照: `at.SYSTEM_TICK`

## SystemTickFeed.onAction()
- 位置: L61-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancelTimer()`, `this.init()`
- 条件付き依存: `if (this._hasObserver)` → `Services.obs.removeObserver()`
- 参照: `action.type`, `at.INIT`, `at.UNINIT`, `this._hasObserver`
- XPCOM: `Services.obs`
