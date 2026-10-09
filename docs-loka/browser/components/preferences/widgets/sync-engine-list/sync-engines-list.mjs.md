# browser/components/preferences/widgets/sync-engine-list/sync-engines-list.mjs

source: browser/components/preferences/widgets/sync-engine-list/sync-engines-list.mjs
source-hash: 40649616b2ba61ba6f610e1e520531ac9d8c8f8e
lines: 140

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`, `window.MozXULElement.insertFTLIfNeeded()`

## SyncEnginesList.constructor()
- 位置: L67-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.engines`

## SyncEnginesList.engineTemplate()
- 位置: L77-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `metadata.iconSrc`, `metadata.l10nId`

## SyncEnginesList.syncedEnginesTemplate()
- 位置: L91-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `html()`, `this.engineTemplate()`, `this.engines.map()`
- XPCOM: `Services.prefs`

## SyncEnginesList.emptyStateTemplate()
- 位置: L112-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `SyncHelpers._chooseWhatToSync()`, `html()`
- XPCOM: `Services.prefs`

## SyncEnginesList.render()
- 位置: L127-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.emptyStateTemplate()`, `this.syncedEnginesTemplate()`
- 参照: `this.engines.length`
