# browser/extensions/newtab/lib/SmartShortcutsFeed.sys.mjs

source: browser/extensions/newtab/lib/SmartShortcutsFeed.sys.mjs
source-hash: fbbda608ee8ac5d3f6fd26776de2ea3748622209
lines: 143

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## smartshortcutsEnabled()
- 位置: L19-26
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `values.trainhopConfig?.smartShortcuts?.enabled`

## timeMSToSeconds()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`

## SmartShortcutsFeed.constructor()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.loaded`

## SmartShortcutsFeed.isEnabled()
- 位置: L43-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `smartshortcutsEnabled()`, `this.store.getState()`
- 参照: `this.store.getState().Prefs`, `values.trainhopConfig?.smartShortcuts?.force_log`

## SmartShortcutsFeed.init()
- 位置: async L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isEnabled()`
- 参照: `this.loaded`

## SmartShortcutsFeed.reset()
- 位置: async L56-58
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.loaded`

## SmartShortcutsFeed.recordShortcutsInteraction()
- 位置: async L60-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.execute()`, `lazy.PlacesUtils.withConnectionWrapper()`, `this.Date()`, `this.Date().now()`, `timeMSToSeconds()`
- 参照: `data.guid`, `data.isPinned`, `data.position`

## SmartShortcutsFeed.handleTopSitesOrganicImpressionStats()
- 位置: async L91-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.recordShortcutsInteraction()`
- 参照: `action.data`, `action.data?.type`

## SmartShortcutsFeed.onPrefChangedAction()
- 位置: async L104-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 参照: `action.data.name`

## SmartShortcutsFeed.onAction()
- 位置: async L113-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`, `this.isEnabled()`, `this.onPrefChangedAction()`, `this.reset()`
- 条件付き依存: `if (this.isEnabled())` → `this.handleTopSitesOrganicImpressionStats()`
- 条件付き依存: `if (action.data.name === "trainhopConfig")` → `this.init()`
- 参照: `action.data.name`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.TOP_SITES_ORGANIC_IMPRESSION_STATS`, `at.UNINIT`

## SmartShortcutsFeed.prototype.Date()
- 位置: L140-142
- 役割: (未記入)
- 触るとき: (未記入)
