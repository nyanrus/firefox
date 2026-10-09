# browser/extensions/newtab/lib/SectionsLayoutFeed.sys.mjs

source: browser/extensions/newtab/lib/SectionsLayoutFeed.sys.mjs
source-hash: 5298fb7b3ed6e9dd3b3d308cfb01c968d5c58600
lines: 827

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isValidLayout()
- 位置: L662-670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `[1, 2, 3, 4].every()`, `columnCounts.has()`, `record.responsiveLayouts.map()`
- 参照: `layout.columnCount`, `record.name`, `record.responsiveLayouts`

## isValidOrdering()
- 位置: L674-680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 参照: `record.name`, `record.sectionLayouts`, `record.sectionLayouts.length`

## maskLayoutAds()
- 位置: L693-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowedRanks.has()`, `layout.responsiveLayouts.map()`, `responsiveLayout.tiles.map()`
- 参照: `tile.hasAd`

## SectionsLayoutFeed.constructor()
- 位置: L717-721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onSync.bind()`
- 参照: `this._layoutsClient`, `this._onSync`, `this._orderingClient`

## SectionsLayoutFeed.RemoteSettings()
- 位置: L723-725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteSettings()`

## SectionsLayoutFeed._connectClient()
- 位置: L729-733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.on()`, `this.RemoteSettings()`
- 参照: `this._onSync`

## SectionsLayoutFeed.init()
- 位置: async L735-760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpaceOverridden()`, `this.store.getState()`
- 条件付き依存: `if (shouldSyncLayouts)` → `this._connectClient()`
- 条件付き依存: `if (shouldSyncLayouts)` → `this._fetchLayouts()`
- 条件付き依存: `if (!(shouldSyncLayouts))` → `this.uninit()`
- 参照: `SPACE_IDS.STORIES`, `prefs.trainhopConfig?.sections?.ordering`, `this._layoutsClient`, `this._orderingClient`, `this.store.getState().Prefs.values`

## SectionsLayoutFeed.uninit()
- 位置: L762-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._layoutsClient?.off()`, `this._orderingClient?.off()`
- 参照: `this._layoutsClient`, `this._onSync`, `this._orderingClient`

## SectionsLayoutFeed._onSync()
- 位置: async L769-771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._fetchLayouts()`

## SectionsLayoutFeed._fetchLayouts()
- 位置: async L773-804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Promise.all()`, `ac.BroadcastToContent()`, `isValidLayout()`, `isValidOrdering()`, `this._layoutsClient.get()`, `this._orderingClient.get()`, `this.store.dispatch()`
- 参照: `Object.keys(configs).length`, `Object.keys(orderings).length`, `at.SECTIONS_LAYOUT_UPDATE`, `record.name`, `record.sectionLayouts`

## SectionsLayoutFeed.onAction()
- 位置: async L806-825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`, `this.uninit()`
- 条件付き依存: `if ( action.data.name === PREF_SECTIONS_ORDERING || action.data.name === PREF_TOPSTORIES_ENABLED || (action.data.name === "trainhopConfig" && action.data.value?....)` → `this.init()`
- 参照: `action.data.name`, `action.data.value?.sections?.ordering`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.UNINIT`
