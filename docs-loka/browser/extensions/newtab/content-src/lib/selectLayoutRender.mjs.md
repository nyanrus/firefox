# browser/extensions/newtab/content-src/lib/selectLayoutRender.mjs

source: browser/extensions/newtab/content-src/lib/selectLayoutRender.mjs
source-hash: dc24b99b90da7380fd1a0052d8b5ffa9f4f2cf5e
lines: 446

## <module>
- 役割: (未記入)

## keepOnlySections()
- 位置: L21-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(row.components ?? []).reduce()`, `keep.has()`, `layoutRender.reduce()`, `sections.filter()`
- 条件付き依存: `if (!sections)` → `kept.push()`
- 条件付き依存: `if (filtered.length)` → `kept.push()`
- 条件付き依存: `if (components.length)` → `rows.push()`
- 参照: `component.data`, `component?.data?.sections`, `components.length`, `filtered.length`, `row.components`, `section.sectionKey`

## selectLayoutRender()
- 位置: L46-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isSpaceOverridden()`, `renderLayout()`
- 条件付き依存: `if (!prefs["feeds.topsites"])` → `filterArray.push()`
- 条件付き依存: `if ( !nimbusWidgetsTrainhopEnabled && !nimbusWidgetsEnabled && !widgetsEnabled )` → `filterArray.push()`
- 条件付き依存: `if (!pocketEnabled)` → `filterArray.push()`
- 条件付き依存: `if (!pocketEnabled)` → `DS_COMPONENTS.filter()`
- 参照: `SPACE_IDS.STORIES`, `prefs.showSponsored`, `prefs.trainhopConfig?.widgets?.enabled`, `prefs.widgetsConfig?.enabled`

## fillSpocPositionsForPlacement()
- 位置: L56-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `spocs.blocked.includes()`
- 条件付き依存: `if (!spocs.blocked.includes(spoc.url))` → `results.splice()`
- 参照: `position.index`, `spoc.url`

## getMaxTiles()
- 位置: L136-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `responsiveLayouts .flatMap()`, `responsiveLayouts .flatMap(responsiveLayout => responsiveLayout) .reduce()`
- 参照: `t.tiles.length`

## placeholderComponent()
- 位置: L142-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data.recommendations.push()`
- 条件付き依存: `if (sectionsEnabled)` → `data.sections[0].data.push()`
- 参照: `component.feed`, `component.properties`, `component.properties.items`, `data.sections`

## handleSpocs()
- 位置: L188-228
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `selectWidgetsRowAd()`
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `spocsData?.items?.filter()`
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `excludedSpocs.includes()`
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `fillSpocPositionsForPlacement()`
- 参照: `item.format`, `placement.name`, `spocs.data`, `spocs.loaded`, `spocsData?.items?.length`, `spocsPositions?.length`

## handleSections()
- 位置: L230-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `acc[section].push()`, `recommendations.reduce()`, `result.forEach()`, `sections.sort()`
- 参照: `a.receivedRank`, `b.receivedRank`, `section.data`

## handleComponent()
- 位置: L248-273
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `spocsData.items .filter(spoc => spoc && !spocs.blocked.includes(spoc.url)) .map()`
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `spocsData.items .filter()`
- 条件付き依存: `if (spocs.loaded && spocsData?.items?.length)` → `spocs.blocked.includes()`
- 参照: `component.placement`, `component?.spocs?.positions?.length`, `placement.name`, `spoc.url`, `spocs.data`, `spocs.loaded`, `spocsData?.items?.length`

## handleComponentWithFeed()
- 位置: L275-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleSections()`, `handleSections(data.sections, data.recommendations).map()`, `handleSpocs()`, `selectFirstSlotWidget()`, `smallestBreakpointLayout.tiles.find()`, `smallestBreakpointLayout.tiles.forEach()`
- 条件付き依存: `if (component && component.properties && component.properties.offset)` → `data.recommendations.slice()`
- 条件付き依存: `if (tile.hasAd && section.allowAds !== false)` → `sectionsSpocsPositions.push()`
- 条件付き依存: `if (component.properties && component.properties.items)` → `Math.min()`
- 条件付き依存: `if (sectionsEnabled)` → `data.sections.forEach()`
- 条件付き依存: `if (sectionsEnabled)` → `getMaxTiles()`
- 参照: `carouselTile.position`, `component.feed.url`, `component.properties`, `component.properties.items`, `component.properties.offset`, `component.type`, `component?.placement`, `component?.spocs?.positions`, `data.recommendations`, `data.recommendations.length`, `data.sections`, `feed.data`, `feed.data.recommendations`, `feed.data.sections`, `feed?.data`, `feeds.data`, `item.columnCount`, `prefs.trainhopConfig?.carousel?.slideCount`, `section.allowAds`, `section.data`, `section?.layout?.responsiveLayouts`, `tile.carousel`, `tile.hasAd`, `tile.position`

## renderLayout()
- 位置: L406-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filterArray.includes()`, `layout.filter()`, `r.components.filter()`, `renderedLayoutArray.push()`, `row.components.filter()`
- 条件付き依存: `if ( (component.feed && !feeds.data[component.feed.url]) || (spocsConfig && spocsConfig.positions && spocsConfig.positions.length && !spocs.loaded) )` → `components.push()`
- 条件付き依存: `if ( (component.feed && !feeds.data[component.feed.url]) || (spocsConfig && spocsConfig.positions && spocsConfig.positions.length && !spocs.loaded) )` → `placeholderComponent()`
- 条件付き依存: `if (component.feed)` → `components.push()`
- 条件付き依存: `if (component.feed)` → `handleComponentWithFeed()`
- 条件付き依存: `if (!(component.feed))` → `components.push()`
- 条件付き依存: `if (!(component.feed))` → `handleComponent()`
- 条件付き依存: `if (!(spocsConfig || component.feed))` → `components.push()`
- 参照: `c.type`, `component.feed`, `component.feed.url`, `component.spocs`, `feeds.data`, `r.components.filter(c => !filterArray.includes(c.type)).length`, `spocs.loaded`, `spocsConfig.positions`, `spocsConfig.positions.length`
