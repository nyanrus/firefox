# browser/components/urlbar/private/FlightStatusSuggestions.sys.mjs

source: browser/components/urlbar/private/FlightStatusSuggestions.sys.mjs
source-hash: 5369522add36f8d9687096024bf49d5ad4db6f86
lines: 299

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## FlightStatusSuggestions.realtimeType()
- 位置: L19-21
- 役割: (未記入)
- 触るとき: (未記入)

## FlightStatusSuggestions.isSponsored()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)

## FlightStatusSuggestions.merinoProvider()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)

## FlightStatusSuggestions.baseTelemetryType()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)

## FlightStatusSuggestions.getViewTemplateForDescriptionTop()
- 位置: L35-62
- 役割: (未記入)
- 触るとき: (未記入)

## FlightStatusSuggestions.getViewTemplateForDescriptionBottom()
- 位置: L64-99
- 役割: (未記入)
- 触るとき: (未記入)

## FlightStatusSuggestions.getViewUpdateForPayloadItem()
- 位置: L101-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat(undefined, { hour: "numeric", minute: "numeric", timeZone: arrivalTimeZone, }).format()`, `new Intl.DateTimeFormat(undefined, { hour: "numeric", minute: "numeric", timeZone: departureTimeZone, }).format()`
- 条件付き依存: `if (status == "delayed" || !item.delayed)` → `getTimeZone()`
- 条件付き依存: `if (!(status == "delayed" || !item.delayed))` → `getTimeZone()`
- 条件付き依存: `if (status == "delayed")` → `getTimeZone()`
- 条件付き依存: `if (item.airline.icon)` → `UrlbarUtils.getRemoteImageUrl()`
- 条件付き依存: `if (status == "inflight")` → `Math.floor()`
- 条件付き依存: `if (typeof item.time_left_minutes == "number")` → `Math.floor()`
- 条件付き依存: `if (typeof item.time_left_minutes == "number")` → `new Intl.DurationFormat(undefined, { style: "short", }).format()`
- 参照: `Intl.DateTimeFormat`, `Intl.DurationFormat`, `item.airline.color`, `item.airline.icon`, `item.airline.name`, `item.arrival.estimated_time`, `item.arrival.scheduled_time`, `item.delayed`, `item.departure.estimated_time`, `item.departure.scheduled_time`, `item.destination.city`, `item.destination.code`, `item.flight_number`, `item.origin.city`, `item.origin.code`, `item.progress_percent`, `item.status`, `item.time_left_minutes`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`

## getTimeZone()
- 位置: L290-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isoTimeString.match()`
