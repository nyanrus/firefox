# nsITrackingDBService (toolkit/components/antitracking/nsITrackingDBService.idl)

source: toolkit/components/antitracking/nsITrackingDBService.idl
source-hash: 32f283aee9e9b1a240bbd8a12edead94eb0e1a05

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/AboutProtectionsParent.sys.mjs`](../../../browser/actors/AboutProtectionsParent.sys.mjs.md), [`browser/base/content/browser-siteProtections.js`](../../../browser/base/content/browser-siteProtections.js.md), [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/preferences/config/privacy.mjs`](../../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/protections/PrivacyMetricsService.sys.mjs`](../../../browser/components/protections/PrivacyMetricsService.sys.mjs.md), [`browser/extensions/newtab/lib/Widgets/PrivacyFeed.sys.mjs`](../../../browser/extensions/newtab/lib/Widgets/PrivacyFeed.sys.mjs.md)

## メソッド / 属性
- `void recordContentBlockingLog(ACString data)`: Record entries from a content blocking log in the tracking database.
- `Promise saveEvents(AString data)`: Save new events in the content blocking database
- `Promise clearAll()`: Clear all content blocking database entries.
- `Promise clearSince(int64_t since)`: Clear all content blocking database entries added since the specified time.
- `Promise getEventsByDateRange(int64_t dateFrom, int64_t dateTo)`: Fetch events from the content blocking database
- `Promise sumAllEvents()`: Return a count of all tracking events.
- `Promise getEarliestRecordedDate()`: Return the earliest recorded date.
- `const unsigned long OTHER_COOKIES_BLOCKED_ID`: (未記入)
- `const unsigned long TRACKERS_ID`: (未記入)
- `const unsigned long TRACKING_COOKIES_ID`: (未記入)
- `const unsigned long CRYPTOMINERS_ID`: (未記入)
- `const unsigned long FINGERPRINTERS_ID`: (未記入)
- `const unsigned long SOCIAL_ID`: (未記入)
- `const unsigned long SUSPICIOUS_FINGERPRINTERS_ID`: (未記入)
- `const unsigned long BOUNCETRACKERS_ID`: (未記入)
