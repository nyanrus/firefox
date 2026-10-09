# browser/extensions/newtab/common/PageLayoutVariants.mjs

source: browser/extensions/newtab/common/PageLayoutVariants.mjs
source-hash: 332fec35d4a3358d8bef7622289145f6b3a29028
lines: 823

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.keys()`

## resolvePageLayoutVariant()
- 位置: L85-91
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `prefs?.trainhopConfig?.pageLayouts?.variant`

## isAutoMinimizeWidgetsAssigned()
- 位置: L100-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePageLayoutVariant()`
- 参照: `PAGE_LAYOUT_VARIANTS.AUTO_MINIMIZE_WIDGETS`

## resolveAutoMinimizeDelayMs()
- 位置: L114-123
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `prefs?.trainhopConfig?.pageLayouts?.autoMinimizeDelayMs`

## sideBySideBandClasses()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePageLayoutVariant()`

## isSideBySideAssigned()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SIDE_BY_SIDE_PAGE_LAYOUTS.includes()`, `resolvePageLayoutVariant()`

## resolveFeatureSpacesOrder()
- 位置: L190-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.values()`, `[...new Set(raw)].filter()`, `ids.includes()`
- 条件付き依存: `if (typeof pref === "string")` → `pref.split(",").map()`
- 条件付き依存: `if (typeof pref === "string")` → `pref.split()`
- 条件付き依存: `if (typeof pref === "string")` → `id.trim()`
- 参照: `order.length`, `prefs?.trainhopConfig?.pageLayouts?.spacesOrder`

## resolveThematicSpaceIcon()
- 位置: L219-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.startsWith()`

## resolveThematicIconFamily()
- 位置: L232-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url.startsWith()`

## asStringArray()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `value.filter()`

## rejectSpacesConfig()
- 位置: L251-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`

## normalizeSpacesConfig()
- 位置: L271-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `asStringArray()`, `kept.includes()`, `order.filter()`, `resolveThematicIconFamily()`, `resolveThematicSpaceIcon()`
- 条件付き依存: `if (!order.length || !rawSpaces || typeof rawSpaces !== "object")` → `rejectSpacesConfig()`
- 条件付き依存: `if (!kept.length)` → `rejectSpacesConfig()`
- 参照: `kept.length`, `order.length`, `raw.default`, `raw?.order`, `raw?.spaces`, `space.icon`, `space.label`, `space.sections`, `space.widgets`

## spacesBandClasses()
- 位置: L339-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePageLayoutVariant()`

## isSpacesAssigned()
- 位置: L349-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SPACES_PAGE_LAYOUTS.includes()`, `resolvePageLayoutVariant()`

## isSpacesThematicAssigned()
- 位置: L361-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePageLayoutVariant()`
- 参照: `PAGE_LAYOUT_VARIANTS.SPACES_THEMATIC_V1`

## isSpacesArrowsAssigned()
- 位置: L373-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePageLayoutVariant()`
- 参照: `PAGE_LAYOUT_VARIANTS.SPACES_FLOATING_ARROWS`

## isSpaceOverridden()
- 位置: L394-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `isSpacesAssigned()`
- 参照: `prefs?.trainhopConfig`, `prefs?.trainhopConfig?.[trainhopKey]?.enabled`

## hasSideBySidePair()
- 位置: L411-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `hasContentAreaWidgets()`, `isSpaceOverridden()`, `isWidgetsContainerVisible()`
- 参照: `SPACE_IDS.STORIES`, `SPACE_IDS.WIDGETS`

## isSideBySideActive()
- 位置: L440-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `SIDE_BY_SIDE_PAGE_LAYOUTS.includes()`, `hasSideBySidePair()`, `resolvePageLayoutVariant()`

## isSpaceEnabled()
- 位置: L447-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `isSpaceOverridden()`
- 参照: `SPACE_CONFIG[id].userPref`

## resolveThematicDefaultSpace()
- 位置: L462-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `populatedSpaces.includes()`
- 参照: `config.default`, `config?.default`

## resolveSpacesConfigFrom()
- 位置: L478-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `normalizeSpacesConfig()`, `rejectSpacesConfig()`
- 条件付き依存: `if (trainhopConfig?.spaces)` → `normalizeSpacesConfig()`
- 参照: `trainhopConfig.spaces`, `trainhopConfig?.spaces`

## resolveThematicSpacesConfig()
- 位置: L504-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveSpacesConfigFrom()`
- 参照: `lastResolved.pref`, `lastResolved.trainhop`, `lastResolved.value`, `prefs?.trainhopConfig`, `prefs?.trainhopConfig?.spaces`

## resolveThematicSpaceSections()
- 位置: L528-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(config?.spaces ?? {}) .filter()`, `Object.entries(config?.spaces ?? {}) .filter(([id]) => id !== spaceId && id !== config?.default) .flatMap()`, `assigned.has()`, `claimedElsewhere.has()`, `sectionKeys.filter()`
- 参照: `config?.default`, `config?.spaces`, `config?.spaces?.[spaceId]?.sections`, `space.sections`

## resolveFeedSectionKeys()
- 位置: L555-560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(discoveryStream?.feeds?.data ?? {}).find()`, `sections?.map()`, `sections?.map(section => section.sectionKey).filter()`
- 参照: `Object.values(discoveryStream?.feeds?.data ?? {}).find( feed => feed?.data?.sections?.length )?.data?.sections`, `discoveryStream?.feeds?.data`, `feed?.data?.sections?.length`, `section.sectionKey`

## resolveThematicSpaceWidgets()
- 位置: L576-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(config?.spaces ?? {}).flatMap()`, `WIDGET_REGISTRY.filter()`, `assigned.has()`, `claimed.has()`, `isSpaceOverridden()`, `isWidgetEnabled()`
- 参照: `SPACE_IDS.WIDGETS`, `config?.default`, `config?.spaces`, `config?.spaces?.[spaceId]?.widgets`, `space.widgets`, `w.id`

## resolvePopulatedThematicSpaces()
- 位置: L603-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.order.filter()`, `hasSideBySidePair()`, `resolveThematicSpaceSections()`, `resolveThematicSpacesConfig()`
- 参照: `resolveThematicSpaceSections(config, id, sectionKeys).length`

## resolvePopulatedFeatureSpaces()
- 位置: L623-640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpaceEnabled()`, `resolveFeatureSpacesOrder()`, `resolveFeatureSpacesOrder(prefs).filter()`
- 条件付き依存: `if (id === SPACE_IDS.STORIES)` → `Boolean()`
- 条件付き依存: `if (id === SPACE_IDS.WIDGETS)` → `hasContentAreaWidgets()`
- 参照: `SPACE_IDS.STORIES`, `SPACE_IDS.WIDGETS`

## resolveThematicWidgetsBySpace()
- 位置: L652-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `resolveThematicSpaceWidgets()`, `spaceIds.map()`

## resolvePopulatedSpaces()
- 位置: L668-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpacesThematicAssigned()`, `resolvePopulatedFeatureSpaces()`, `resolvePopulatedThematicSpaces()`

## resolveThematicSpaces()
- 位置: L684-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.fromEntries()`, `isSpacesThematicAssigned()`, `order.map()`, `resolveFeedSectionKeys()`, `resolvePopulatedSpaces()`, `resolveThematicDefaultSpace()`, `resolveThematicSpaceSections()`, `resolveThematicSpaceWidgets()`, `resolveThematicSpacesConfig()`
- 参照: `config.spaces`, `order.length`

## isSpacesActive()
- 位置: L724-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpacesAssigned()`, `isSpacesThematicAssigned()`, `resolveFeedSectionKeys()`, `resolvePopulatedSpaces()`
- 参照: `resolvePopulatedSpaces(prefs, sectionKeys).length`

## isWidgetsAdActive()
- 位置: L755-765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `hasContentAreaWidgets()`, `isWidgetsContainerVisible()`, `resolvePageLayoutVariant()`
- 参照: `PAGE_LAYOUT_VARIANTS.WIDGETS_AD_LARGE`, `prefs.showSponsored`

## selectWidgetsRowAd()
- 位置: L779-790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WIDGETS_AD_EXCLUDED_FORMATS.includes()`, `blocked.includes()`, `isWidgetsAdActive()`, `spocs?.data?.newtab_spocs?.items?.find()`
- 参照: `first.url`, `item.format`, `spocs?.blocked`

## selectFirstSlotWidget()
- 位置: L804-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WIDGET_REGISTRY.find()`, `isWidgetEnabled()`, `resolvePageLayoutVariant()`
- 参照: `PAGE_LAYOUT_VARIANTS.WIDGET_FIRST_CONTENT_SLOT`, `prefs.trainhopConfig?.pageLayouts?.widgetFirstContentSlot?.widget`, `w.id`
