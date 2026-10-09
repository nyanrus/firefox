# browser/extensions/newtab/common/WidgetsRegistry.mjs

source: browser/extensions/newtab/common/WidgetsRegistry.mjs
source-hash: 9b68ab80d6a86a558952f0ed1a6df142b72bc743
lines: 838

## <module>
- 役割: (未記入)

## getWidgetOrder()
- 位置: L395-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WIDGET_REGISTRY.map()`, `orderPref .split()`, `orderPref .split(",") .filter()`, `registryIds.filter()`, `registryIds.includes()`, `seen.add()`, `seen.has()`
- 参照: `w.id`

## resolveWidgetOrder()
- 位置: L415-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getWidgetOrder()`
- 条件付き依存: `if (userOrder)` → `getWidgetOrder()`
- 条件付き依存: `if (trainhopOrder)` → `getWidgetOrder()`
- 参照: `prefs.trainhopConfig?.widgets?.order`

## isWidgetDataUnavailable()
- 位置: L443-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `prefs.recordsHistory`, `prefs.supportsWidgetSearchSap`, `widget.requiresHistory`, `widget.requiresWidgetSearchSap`

## isWidgetAddable()
- 位置: L464-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `isWidgetDataUnavailable()`
- 参照: `prefs.trainhopConfig`, `prefs.trainhopConfig?.[widget.trainhopNamespace]?.visible`, `prefs.trainhopConfig?.widgets`, `prefs.trainhopConfig?.widgetsSettings`, `widget.retired`, `widget.systemEnabledPref`, `widget.trainhopEnabledKey`, `widget.trainhopNamespace`, `widget.widgetsSettingsVisibleKey`

## isWidgetToggleVisible()
- 位置: L492-500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `isWidgetAddable()`, `isWidgetDataUnavailable()`
- 参照: `prefs.widgetsConfig`, `widget.retired`, `widget.trainhopEnabledKey`

## isWeatherAvailable()
- 位置: L512-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `prefs.trainhopConfig?.weather?.enabled`, `prefs.trainhopConfig?.widgetsSettings?.weatherVisible`

## isWidgetsContainerVisible()
- 位置: L529-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `prefs.trainhopConfig?.widgets?.enabled`, `prefs.trainhopConfig?.widgetsSettings?.enabled`, `prefs.widgetsConfig?.enabled`

## isWidgetEnabled()
- 位置: L547-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `isWidgetAddable()`
- 参照: `widget.enabledPref`

## resolveWidgetSize()
- 位置: L567-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectFirstSlotWidget()`
- 参照: `prefs.trainhopConfig`, `prefs.trainhopConfig?.[widget.trainhopNamespace]?.size`, `prefs.trainhopConfig?.widgets`, `widget.defaultSize`, `widget.id`, `widget.sizePref`, `widget.trainhopNamespace`, `widget.trainhopSizeKey`

## resolveWidgetHasSidebar()
- 位置: L595-603
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `prefs.trainhopConfig?.widgets`, `widget.hasSidebar`, `widget.trainhopSidebarKey`

## hasContentAreaWidgets()
- 位置: L618-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WIDGET_REGISTRY.find()`, `WIDGET_REGISTRY.some()`, `isWidgetEnabled()`, `resolveWidgetHasSidebar()`, `resolveWidgetSize()`
- 参照: `w.id`

## resolveCrosswordEndpoint()
- 位置: L644-650
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `prefs.trainhopConfig?.widgetCrossword?.endpoint`, `prefs.trainhopConfig?.widgets?.crosswordEndpoint`

## resolvePrivacyTrainhopValue()
- 位置: L666-679
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (dedicated !== undefined)` → `console.warn()`
- 条件付き依存: `if (dedicated !== undefined)` → `JSON.stringify()`
- 参照: `prefs.trainhopConfig?.widgetPrivacy`, `prefs.trainhopConfig?.widgets`

## resolvePrivacyMaxCount()
- 位置: L691-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePrivacyTrainhopValue()`

## resolvePrivacyDisplayCount()
- 位置: L713-724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePrivacyTrainhopValue()`

## resolvePrivacyBlankChance()
- 位置: L736-768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isNaN()`, `parseFloat()`, `resolvePrivacyTrainhopValue()`
- 条件付き依存: `if (rawPref !== undefined && rawPref !== "")` → `console.warn()`
- 条件付き依存: `if (rawPref !== undefined && rawPref !== "")` → `JSON.stringify()`
- 条件付き依存: `if (raw < 0 || raw > 1)` → `console.warn()`

## resolvePrivacyShowVpnMessages()
- 位置: L780-791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolvePrivacyTrainhopValue()`

## resolvePrivacyCelebrationThreshold()
- 位置: L800-817
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `resolvePrivacyTrainhopValue()`

## getHideAllTargets()
- 位置: L829-837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WIDGET_REGISTRY.filter()`, `WIDGET_REGISTRY.filter( w => !resolveWidgetHasSidebar(w, prefs) || widgetEnabledMap[w.id] ).map()`, `resolveWidgetHasSidebar()`
- 参照: `w.enabledPref`, `w.id`, `w.telemetryName`
