# browser/components/extensions/parent/ext-tabGroups.js

source: browser/components/extensions/parent/ext-tabGroups.js
source-hash: b901973f1fec795ba3056d0a0c78625188928e10
lines: 301

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## spellColour()
- 位置: L12-12
- 役割: (未記入)
- 触るとき: (未記入)

## validateTabIndexForMove()
- 位置: L21-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `window.gBrowser.tabs.at()`
- 参照: `group.documentGlobal`, `group.tabs`, `group_tabs.length`, `group_tabs[0].index`, `nextTab.group`, `nextTab?.group`, `nextTab?.pinned`, `prevTab.group`, `window.gBrowser.tabs.length`

## queryGroups()
- 位置: L48-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `glob.matches()`, `spellColour()`, `this.extension.canAccessWindow()`, `windowTracker .browserWindows()`, `windowTracker .browserWindows() .filter()`, `windowTracker.getWindow()`
- 参照: `group.collapsed`, `group.color`, `group.name`, `win.gBrowser.tabGroups`

## get()
- 位置: L69-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getInternalTabGroupIdForExtTabGroupId()`, `this.queryGroups()`
- 参照: `group.id`

## convert()
- 位置: L82-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getExtTabGroupIdForInternalTabGroupId()`, `windowTracker.getId()`
- 参照: `group.collapsed`, `group.color`, `group.documentGlobal`, `group.id`, `group.name`

## onCreated()
- 位置: L94-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## onCreate()
- 位置: L95-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.detail.adopting`, `event.originalTarget`, `event.originalTarget.documentGlobal`

## unregister()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)

## onMoved()
- 位置: L117-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## onMove()
- 位置: L118-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.originalTarget`, `event.originalTarget.documentGlobal`

## onCreate()
- 位置: L126-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.detail.adopting`, `event.originalTarget`, `event.originalTarget.documentGlobal`

## unregister()
- 位置: L141-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)

## onRemoved()
- 位置: L150-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## onRemove()
- 位置: L151-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.detail.adopting`, `event.originalTarget`, `event.originalTarget.documentGlobal`

## onClosed()
- 位置: L165-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `window.gBrowser.tabGroups`

## unregister()
- 位置: L176-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L180-182
- 役割: (未記入)
- 触るとき: (未記入)

## onUpdated()
- 位置: L185-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.addListener()`

## onUpdate()
- 位置: L186-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.originalTarget`, `event.originalTarget.documentGlobal`

## unregister()
- 位置: L198-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L203-205
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L210-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "tabGroups", event: "onCreated", extensionApi: this, }).api()`, `new EventManager({ context, module: "tabGroups", event: "onMoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "tabGroups", event: "onRemoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "tabGroups", event: "onUpdated", extensionApi: this, }).api()`
- 参照: `this.extension`

## get()
- 位置: L214-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.convert()`, `this.get()`

## move()
- 位置: L218-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `this.convert()`, `this.get()`, `validateTabIndexForMove()`
- 条件付き依存: `if (windowId != null)` → `windowTracker.getWindow()`
- 条件付き依存: `if (windowId != null)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (windowId != null)` → `windowManager.getWrapper()`
- 条件付き依存: `if (win !== group.documentGlobal)` → `win.gBrowser.adoptTabGroup()`
- 条件付き依存: `if (!(win !== group.documentGlobal))` → `win.gBrowser.moveTabTo()`
- 参照: `group.documentGlobal`, `win.gBrowser.tabs.length`, `windowManager.getWrapper(win).type`

## query()
- 位置: L250-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `this.convert()`, `this.queryGroups()`

## update()
- 位置: L256-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.convert()`, `this.get()`
- 条件付き依存: `if (color != null)` → `spellColour()`
- 参照: `group.collapsed`, `group.color`, `group.name`
