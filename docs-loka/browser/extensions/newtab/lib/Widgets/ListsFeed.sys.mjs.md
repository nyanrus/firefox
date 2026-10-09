# browser/extensions/newtab/lib/Widgets/ListsFeed.sys.mjs

source: browser/extensions/newtab/lib/Widgets/ListsFeed.sys.mjs
source-hash: 250a38020655d9aac8f3cce9174053157895398e
lines: 167

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ListsFeed.constructor()
- 位置: L30-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PersistentCache()`
- 参照: `this.cache`, `this.initialized`

## ListsFeed.enabled()
- 位置: L35-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 参照: `prefs.trainhopConfig?.widgets?.listsEnabled`, `prefs.widgetsConfig?.listsEnabled`, `this.store.getState()?.Prefs.values`

## ListsFeed.init()
- 位置: async L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.syncLists()`
- 参照: `this.initialized`

## ListsFeed.isOverMaximumListCount()
- 位置: L54-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this.store.getState()`
- 参照: `Object.keys(lists).length`, `this.store.getState()?.Prefs.values`

## ListsFeed.syncLists()
- 位置: async L61-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.get()`
- 条件付き依存: `if (lists[listId])` → `Array.isArray()`
- 条件付き依存: `if (task.completed === true)` → `completedTasks.push()`
- 条件付き依存: `if (!(task.completed === true))` → `activeTasks.push()`
- 条件付き依存: `if (lists[listId])` → `list.completed.concat()`
- 条件付き依存: `if (lists)` → `this.isOverMaximumListCount()`
- 条件付き依存: `if (lists)` → `this.update()`
- 条件付き依存: `if (selected)` → `this.updateSelected()`
- 参照: `list.completed`, `list.tasks`, `task.completed`

## ListsFeed.update()
- 位置: L103-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_LISTS_SET`, `data.lists`

## ListsFeed.updateSelected()
- 位置: L113-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_LISTS_SET_SELECTED`

## ListsFeed.onPrefChangedAction()
- 位置: async L128-140
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.enabled && !this.initialized)` → `this.init()`
- 参照: `action.data.name`, `this.enabled`, `this.initialized`

## ListsFeed.onAction()
- 位置: async L142-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cache.set()`, `this.onPrefChangedAction()`, `this.update()`, `this.updateSelected()`
- 条件付き依存: `if (this.enabled)` → `this.init()`
- 参照: `action.data`, `action.data.lists`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.WIDGETS_LISTS_CHANGE_SELECTED`, `at.WIDGETS_LISTS_UPDATE`, `this.enabled`

## ListsFeed.prototype.PersistentCache()
- 位置: L164-166
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PersistentCache`
