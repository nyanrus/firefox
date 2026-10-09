# browser/extensions/webcompat/lib/about_compat_broker.js

source: browser/extensions/webcompat/lib/about_compat_broker.js
source-hash: 9ff3b5e6b4db6b5d1329da605d09d8326eb75270
lines: 125

## <module>
- 役割: (未記入)

## AboutCompatBroker.constructor()
- 位置: L10-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._interventions?.bindAboutCompatBroker()`, `this._shims?.bindAboutCompatBroker()`, `this.buildPorts()`
- 参照: `bindings.interventions`, `bindings.shims`, `this._interventions`, `this._shims`, `this.portsToAboutCompatTabs`

## AboutCompatBroker.buildPorts()
- 位置: L25-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.runtime.onConnect.addListener()`, `port.onDisconnect.addListener()`, `ports.add()`, `ports.delete()`

## broadcast()
- 位置: async L35-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `port.postMessage()`, `ports.delete()`

## AboutCompatBroker.filterInterventions()
- 位置: L48-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `interventions .filter()`, `interventions .filter(intervention => intervention.availableOnPlatform) .map()`
- 参照: `intervention.availableOnPlatform`, `intervention.label`

## AboutCompatBroker.getInterventionById()
- 位置: L59-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `this._interventions?.getAvailableInterventions()`, `this._shims?.getAvailableShims()`
- 参照: `what.id`

## AboutCompatBroker.bootup()
- 位置: L73-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `onMessageFromTab()`, `this._interventions?.getAvailableInterventions()`, `this._interventions?.isEnabled()`, `this._shims?.getAvailableShims()`, `this.filterInterventions()`, `this.getInterventionById()`, `this.portsToAboutCompatTabs .broadcast()`, `this.portsToAboutCompatTabs .broadcast({ toggling: id, active }) .then()`
- 条件付き依存: `if (!what)` → `Promise.reject()`
- 条件付き依存: `if (active)` → `this._interventions?.disableInterventions()`
- 条件付き依存: `if (!(active))` → `this._interventions?.enableInterventions()`
- 条件付き依存: `if (active)` → `this._shims?.disableShimForSession()`
- 条件付き依存: `if (!(active))` → `this._shims?.enableShimForSession()`
- 参照: `msg.command`, `msg.id`, `what.active`, `what.disabledReason`, `what.id`
