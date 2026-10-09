# browser/extensions/newtab/lib/ExternalComponentsFeed.sys.mjs

source: browser/extensions/newtab/lib/ExternalComponentsFeed.sys.mjs
source-hash: 4e7c06c96291a2634505644add793e9bc0c6a693
lines: 201

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## logConsole()
- 位置: L17-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `console.createInstance()`
- XPCOM: `Services.prefs`

## ExternalComponentsFeed.constructor()
- 位置: L114-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#registry.on()`, `this.refreshComponents()`
- 参照: `lazy.AboutNewTabComponentRegistry`, `lazy.AboutNewTabComponentRegistry.UPDATED_EVENT`, `this.#registry`

## ExternalComponentsFeed.refreshComponents()
- 位置: L133-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 条件付き依存: `if (configuration.actors)` → `Object.keys()`
- 条件付き依存: `if (configuration.actors)` → `ChromeUtils.unregisterWindowActor()`
- 条件付き依存: `if (configuration.actors)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (configuration.actors)` → `ChromeUtils.registerWindowActor()`
- 条件付き依存: `if (configuration.actors)` → `lazy.logConsole.error()`
- 参照: `action.meta`, `at.REFRESH_EXTERNAL_COMPONENTS`, `configuration.actors`, `configuration.type`, `options.isStartup`, `this.#registry.values`

## ExternalComponentsFeed.onAction()
- 位置: L193-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.refreshComponents()`
- 参照: `action.type`, `at.INIT`
