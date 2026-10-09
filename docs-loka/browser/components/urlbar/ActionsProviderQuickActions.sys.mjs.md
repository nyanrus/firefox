# browser/components/urlbar/ActionsProviderQuickActions.sys.mjs

source: browser/components/urlbar/ActionsProviderQuickActions.sys.mjs
source-hash: ea83d2727b89037ac3ca4b9f055aa7655d761895
lines: 224

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ProviderQuickActions.name()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)

## ProviderQuickActions.isActive()
- 位置: L55-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`
- 参照: `queryContext.sapName`, `queryContext.trimmedSearchString.length`

## ProviderQuickActions.queryActions()
- 位置: async L66-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...results].map()`, `action.isInactive()`, `action.isUnsupported()`, `lazy.UrlbarPrefs.get()`, `results.forEach()`, `this.#actions.get()`, `this.getActions()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get(MATCH_IN_PHRASE_PREF))` → `input.includes()`
- 条件付き依存: `if (input.includes(keyword) && keys.length)` → `keys.forEach()`
- 条件付き依存: `if (input.includes(keyword) && keys.length)` → `results.add()`
- 条件付き依存: `if (action.isUnsupported?.() || action.isInactive?.())` → `results.delete()`
- 参照: `action.icon`, `action.label`, `keys.length`, `queryContext.trimmedLowerCaseSearchString`, `queryContext.trimmedSearchString.length`, `results.size`, `this.#keywords`, `this.name`

## ProviderQuickActions.getActions()
- 位置: async L105-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickActionsLoaderDefault.ensureLoaded()`, `this.#prefixes.get()`
- 条件付き依存: `if (includesExactMatch)` → `this.#keywords.get()`
- 条件付き依存: `if (includesExactMatch)` → `actions?.forEach()`
- 条件付き依存: `if (includesExactMatch)` → `results.add()`

## ProviderQuickActions.getAction()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#actions.get()`

## ProviderQuickActions.onPick()
- 位置: L122-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.pickAction()`
- 参照: `actionResult.dataset.inputLength`, `actionResult.key`

## ProviderQuickActions.pickAction()
- 位置: L131-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarQuickaction.picked[`${key}-${inputLength}`].add()`, `Math.min()`, `this.#actions.get()`, `this.#actions.get(key).onPick()`
- 条件付き依存: `if (options?.focusContent)` → `controller.browserWindow.gBrowser.selectedBrowser.focus()`
- 参照: `Glean.urlbarQuickaction.picked`, `options?.focusContent`

## ProviderQuickActions.addAction()
- 位置: L146-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `definition.commands.forEach()`, `keys.push()`, `this.#actions.set()`, `this.#keywords.get()`, `this.#keywords.set()`, `this.#loopOverPrefixes()`, `this.#prefixes.get()`, `this.#prefixes.set()`
- 条件付き依存: `if (result)` → `result.add()`
- 参照: `definition.commands`

## ProviderQuickActions.removeAction()
- 位置: L169-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `definition.commands.forEach()`, `keys.filter()`, `this.#actions.delete()`, `this.#actions.get()`, `this.#keywords.get()`, `this.#keywords.set()`, `this.#loopOverPrefixes()`, `this.#prefixes.get()`, `this.#prefixes.set()`
- 条件付き依存: `if (result)` → `result.delete()`
- 参照: `definition.commands`

## ProviderQuickActions.#loopOverPrefixes()
- 位置: L209-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `command.substring()`, `fun()`
- 参照: `command.length`
