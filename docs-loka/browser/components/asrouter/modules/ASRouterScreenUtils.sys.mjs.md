# browser/components/asrouter/modules/ASRouterScreenUtils.sys.mjs

source: browser/components/asrouter/modules/ASRouterScreenUtils.sys.mjs
source-hash: 922a4fe314ad44127c54998ccf14683f2c18a764
lines: 243

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## removeScreens()
- 位置: async L23-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`
- 条件付き依存: `if (await callback(screens[i], i))` → `screens.splice()`
- 参照: `screens?.length`

## evaluateScreenTargeting()
- 位置: async L38-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.evaluateExpression()`
- 参照: `lazy.ASRouterTargeting.Environment`, `result.evaluationStatus.result`, `result?.evaluationStatus?.success`

## getUnhandledCampaignAction()
- 位置: async L55-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.evaluateExpression()`
- 参照: `lazy.ASRouterTargeting.Environment`, `result?.evaluationStatus?.result`

## evaluateTargetingAndRemoveScreens()
- 位置: async L76-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.filterTileTargeting()`, `this.removeScreens()`
- 条件付き依存: `if (screen.targeting !== undefined)` → `this.evaluateScreenTargeting()`
- 参照: `screen.targeting`

## prepareContentForFirstPaint()
- 位置: async L107-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PinnableSitesProvider.hasPersonalizedTile()`, `lazy.PinnableSitesProvider.populate()`, `structuredClone()`

## filterTileTargeting()
- 位置: async L124-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `TARGETABLE_TILE_TYPES.includes()`, `evaluatedItems.some()`, `this.evaluateScreenTargeting()`
- 条件付き依存: `if ( item?.targeting === undefined || (await this.evaluateScreenTargeting(item.targeting)) )` → `evaluatedItems.push()`
- 条件付き依存: `if (Array.isArray(tiles))` → `tiles.filter()`
- 条件付き依存: `if (Array.isArray(tiles))` → `isEmptyTile()`
- 条件付き依存: `if (!(Array.isArray(tiles)))` → `isEmptyTile()`
- 参照: `item.id`, `item.targeting`, `item?.targeting`, `screen.content.tiles`, `screen?.content?.tiles`, `tile.data`, `tile.selected`, `tile.type`

## isEmptyTile()
- 位置: L162-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TARGETABLE_TILE_TYPES.includes()`
- 参照: `tile.data.length`, `tile?.type`

## addScreenImpression()
- 位置: async L171-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.addScreenImpression()`

## hasSeenScreen()
- 位置: async L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `lazy.ASRouter.state.screenImpressions`

## isAllowedImpressionAction()
- 位置: L193-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_IMPRESSION_ACTIONS.includes()`
- 条件付き依存: `if (action.type === "MULTI_ACTION")` → `Array.isArray()`
- 条件付き依存: `if (action.type === "MULTI_ACTION")` → `actions.every()`
- 条件付き依存: `if (action.type === "MULTI_ACTION")` → `ALLOWED_IMPRESSION_ACTIONS.includes()`
- 参照: `action.data?.actions`, `action.type`, `actions.length`, `nestedAction?.type`

## handleImpressionAction()
- 位置: async L228-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SpecialMessageActions.handleAction()`, `this.hasSeenScreen()`, `this.isAllowedImpressionAction()`
- 参照: `action.data`, `action.once`, `action.type`
