# browser/extensions/webcompat/lib/remote_settings_update_check.js

source: browser/extensions/webcompat/lib/remote_settings_update_check.js
source-hash: 39233a6db5d00706ca3baee4f40ea1ccb3fdd4e0
lines: 87

## <module>
- 役割: (未記入)
- 呼び出し先: `browser.runtime.getManifest()`

## isUpdateWanted()
- 位置: L9-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isNewerVersion()`
- 条件付き依存: `if (!update?.version || (!update?.interventions && !update.shims))` → `console.error()`
- 条件付き依存: `if (!this.isNewerVersion(update.version, currentVersion))` → `console.error()`
- 参照: `update.shims`, `update.version`, `update?.interventions`, `update?.version`

## isNewerVersion()
- 位置: L35-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a_raw.split()`, `b_raw.split()`, `num()`

## num()
- 位置: L36-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNaN()`, `parseInt()`

## listenForRemoteSettingsUpdates()
- 位置: L55-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.remoteSettings.onRemoteSettingsUpdate.addListener()`, `console.info()`, `isUpdateWanted()`
- 条件付き依存: `if (!isUpdateWanted(update))` → `console.info()`
- 条件付き依存: `if (update.interventions)` → `interventions.onRemoteSettingsUpdate()`
- 条件付き依存: `if (update.shims)` → `shims.onRemoteSettingsUpdate()`
- 参照: `update.interventions`, `update.shims`, `update.version`, `window._downgradeForTesting`, `window.latestReceivedUpdate`, `window.latestUpdate`

## window._downgradeForTesting()
- 位置: async L81-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.runtime.getManifest()`, `interventions.resetToDefaultInterventions()`, `shims._resetToDefaultShims()`
- 参照: `browser.runtime.getManifest().version`
