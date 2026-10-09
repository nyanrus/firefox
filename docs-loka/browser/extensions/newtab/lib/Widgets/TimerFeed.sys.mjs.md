# browser/extensions/newtab/lib/Widgets/TimerFeed.sys.mjs

source: browser/extensions/newtab/lib/Widgets/TimerFeed.sys.mjs
source-hash: 1f3800b5657c535e9d98794d90ca583e04bbb07a
lines: 192

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`

## TimerFeed.constructor()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.cache`, `this.initialized`, `this.notifiedThisCycle`

## TimerFeed.resetNotificationFlag()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.notifiedThisCycle`

## TimerFeed.showSystemNotification()
- 位置: async L52-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/alerts-service;1"].getService()`, `alertsService.showAlert()`, `console.error()`, `this.store.getState()`
- 参照: `Ci.nsIAlertsService`, `this.store.getState()?.Prefs.values`
- XPCOM: [`nsIAlertsService`](../../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / `@mozilla.org/alerts-service;1`

## TimerFeed.enabled()
- 位置: L75-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `prefs.trainhopConfig?.widgets?.timerEnabled`, `prefs.widgetsConfig?.timerEnabled`, `this.store.getState()?.Prefs.values`

## TimerFeed.init()
- 位置: async L89-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.syncTimer()`
- 参照: `this.initialized`

## TimerFeed.syncTimer()
- 位置: async L94-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`
- 条件付き依存: `if (timer)` → `this.update()`

## TimerFeed.update()
- 位置: L102-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_TIMER_SET`

## TimerFeed.onPrefChangedAction()
- 位置: async L117-129
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.enabled && !this.initialized)` → `this.init()`
- 参照: `action.data.name`, `this.enabled`, `this.initialized`

## TimerFeed.onAction()
- 位置: async L131-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gNewTabStrings.formatMessages()`, `this.cache.set()`, `this.onPrefChangedAction()`, `this.resetNotificationFlag()`, `this.store.getState()`, `this.update()`
- 条件付き依存: `if (this.enabled)` → `this.init()`
- 条件付き依存: `if (!this.notifiedThisCycle)` → `this.showSystemNotification()`
- 参照: `action.data`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.WIDGETS_TIMER_END`, `at.WIDGETS_TIMER_PAUSE`, `at.WIDGETS_TIMER_PLAY`, `at.WIDGETS_TIMER_RESET`, `at.WIDGETS_TIMER_SET_DURATION`, `at.WIDGETS_TIMER_SET_TYPE`, `bodyMessage?.value`, `this.enabled`, `this.notifiedThisCycle`, `this.store.getState().TimerWidget`, `titleMessage?.value`

## TimerFeed.prototype.PersistentCache()
- 位置: L189-191
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`
