# browser/extensions/newtab/lib/NewTabAttributionFeed.sys.mjs

source: browser/extensions/newtab/lib/NewTabAttributionFeed.sys.mjs
source-hash: 95458c6bf36193afd94866e99020199dde93e537
lines: 173

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## NewTabAttributionFeed.constructor()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.loaded`

## NewTabAttributionFeed.isEnabled()
- 位置: L42-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `this.store.getState().Prefs`, `values.trainhopConfig?.attribution?.enabled`

## NewTabAttributionFeed.init()
- 位置: async L74-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabActorRegistry.registerAttributionActor()`
- 参照: `this.loaded`

## NewTabAttributionFeed.uninit()
- 位置: L79-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NewTabActorRegistry.unregisterAttributionActor()`
- 参照: `this.loaded`

## NewTabAttributionFeed.onPlacesHistoryCleared()
- 位置: async L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.newTabAttributionService.onAttributionReset()`

## NewTabAttributionFeed.onPrefChangedAction()
- 位置: async L88-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`
- 条件付き依存: `if (enabled && !this.loaded)` → `this.init()`
- 条件付き依存: `if (!enabled && this.loaded)` → `this.onPlacesHistoryCleared()`
- 条件付き依存: `if (!enabled && this.loaded)` → `this.uninit()`
- 参照: `action.data.name`, `this.loaded`

## NewTabAttributionFeed.onAction()
- 位置: async L114-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`, `this.onPlacesHistoryCleared()`, `this.onPrefChangedAction()`, `this.uninit()`
- 条件付き依存: `if (this.isEnabled() && !this.loaded)` → `this.init()`
- 条件付き依存: `if (item.type === "impression")` → `lazy.newTabAttributionService.onAttributionEvent()`
- 条件付き依存: `if (item.type === "click")` → `lazy.newTabAttributionService.onAttributionEvent()`
- 条件付き依存: `if (item.attribution)` → `lazy.newTabAttributionService.onAttributionEvent()`
- 参照: `action.type`, `action?.data`, `action?.data?.tiles`, `action?.data?.value`, `at.DISCOVERY_STREAM_IMPRESSION_STATS`, `at.DISCOVERY_STREAM_USER_EVENT`, `at.INIT`, `at.PLACES_HISTORY_CLEARED`, `at.PREF_CHANGED`, `at.TOP_SITES_SPONSORED_IMPRESSION_STATS`, `at.UNINIT`, `item.attribution`, `item.type`, `this.loaded`
