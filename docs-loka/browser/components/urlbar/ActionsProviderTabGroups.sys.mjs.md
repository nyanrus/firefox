# browser/components/urlbar/ActionsProviderTabGroups.sys.mjs

source: browser/components/urlbar/ActionsProviderTabGroups.sys.mjs
source-hash: 38c872f4aa81093ef46af423965e3204f7b51dbc
lines: 160

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ProviderTabGroups.name()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)

## ProviderTabGroups.isActive()
- 位置: L31-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.UrlbarPrefs.get()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `queryContext.restrictSource`, `queryContext.sapName`, `queryContext.trimmedSearchString.length`
- XPCOM: `Services.prefs`

## ProviderTabGroups.queryActions()
- 位置: async L44-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.SessionStore.getSavedTabGroups()`, `results.push()`, `this.#makeResult()`, `this.#matches()`, `window.gBrowser.getAllTabGroups()`
- 条件付き依存: `if (!Cu.isInAutomation)` → `console.error()`
- 参照: `Cu.isInAutomation`, `group.color`, `group.documentGlobal`, `group.id`, `group.label`, `queryContext.isPrivate`, `savedGroup.color`, `savedGroup.id`, `savedGroup.name`, `window.gBrowser.selectedTab.group`

## ProviderTabGroups.onPick()
- 位置: L107-127
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (action.dataset.savedGroupId)` → `lazy.SessionStore.openSavedTabGroup()`
- 条件付き依存: `if (!(action.dataset.savedGroupId))` → `controller.browserWindow.gBrowser.getTabGroupById()`
- 条件付き依存: `if (group)` → `group.select()`
- 条件付き依存: `if (group)` → `group.documentGlobal.focus()`
- 参照: `action.dataset.groupId`, `action.dataset.savedGroupId`, `controller.browserWindow`, `lazy.TabMetrics.METRIC_SOURCE.SUGGEST`

## ProviderTabGroups.#matches()
- 位置: L129-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `groupName.includes()`, `groupName.toLowerCase()`, `queryContext.tokens.every()`
- 条件付き依存: `if (queryContext.trimmedLowerCaseSearchString.length == 1)` → `groupName.startsWith()`
- 参照: `queryContext.trimmedLowerCaseSearchString`, `queryContext.trimmedLowerCaseSearchString.length`, `token.lowerCaseValue`

## ProviderTabGroups.#makeResult()
- 位置: L139-156
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.name`
