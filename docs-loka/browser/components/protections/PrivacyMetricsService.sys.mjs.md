# browser/components/protections/PrivacyMetricsService.sys.mjs

source: browser/components/protections/PrivacyMetricsService.sys.mjs
source-hash: 555dfce30644031d995c32e3b58edcf1f6461a64
lines: 113

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`

## getWeeklyStats()
- 位置: async L46-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.TrackingDBService.getEventsByDateRange()`, `this._aggregateStats()`

## getTodayStats()
- 位置: async L69-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `lazy.TrackingDBService.getEventsByDateRange()`, `this._aggregateStats()`

## _aggregateStats()
- 位置: L87-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Math.sumPrecise()`, `Object.values()`, `Object.values(privacyMetricsStatsCategories).forEach()`, `row.getResultByName()`
