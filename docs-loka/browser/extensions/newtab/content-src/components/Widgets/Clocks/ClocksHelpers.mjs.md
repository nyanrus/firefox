# browser/extensions/newtab/content-src/components/Widgets/Clocks/ClocksHelpers.mjs

source: browser/extensions/newtab/content-src/components/Widgets/Clocks/ClocksHelpers.mjs
source-hash: e3451975e5c7c6010050467855cb870eaafaa4b4
lines: 822

## <module>
- 役割: (未記入)
- 呼び出し先: `LABEL_PALETTE.filter()`

## isValidPaletteName()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LABEL_PALETTE.includes()`

## getRandomLabelColor()
- 位置: L38-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`
- 参照: `RANDOM_LABEL_PALETTE.length`

## is12HourLocale()
- 位置: L52-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat(locale, { hour: "numeric", }).resolvedOptions()`
- 参照: `Intl.DateTimeFormat`, `opts.hour12`, `opts.hourCycle`

## shouldUse12HourTimeFormat()
- 位置: L70-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `is12HourLocale()`

## getDefaultTimeZones()
- 位置: L83-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat().resolvedOptions()`, `seen.has()`
- 条件付き依存: `if (localTz)` → `result.push()`
- 条件付き依存: `if (localTz)` → `seen.add()`
- 条件付き依存: `if (!seen.has(tz))` → `result.push()`
- 条件付き依存: `if (!seen.has(tz))` → `seen.add()`
- 参照: `Intl.DateTimeFormat`, `new Intl.DateTimeFormat().resolvedOptions().timeZone`, `result.length`

## decorateDefaultZones()
- 位置: L108-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `timeZones.map()`

## buildDefaultZones()
- 位置: L119-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decorateDefaultZones()`, `getDefaultTimeZones()`

## isValidTimeZone()
- 位置: L123-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat(undefined, { timeZone }).format()`
- 参照: `Intl.DateTimeFormat`

## getSupportedTimeZones()
- 位置: L135-147
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof Intl.supportedValuesOf === "function")` → `Intl.supportedValuesOf()`
- 参照: `Intl.supportedValuesOf`, `timeZones.length`

## getLocalizedTimeZoneName()
- 位置: L152-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat(locale, { timeZone, timeZoneName: "longGeneric", }).formatToParts()`, `parts.find()`
- 参照: `Intl.DateTimeFormat`, `p.type`, `part?.value`

## buildLocalizedTimeZoneMap()
- 位置: L165-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLocalizedTimeZoneName()`, `map.set()`

## normalizeClockZone()
- 位置: L173-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CLOCK_CITY_BY_ID.has()`, `isValidPaletteName()`, `isValidTimeZone()`, `normalizedClock.city.trim()`, `normalizedClock.cityId.trim()`, `normalizedClock.label.trim()`
- 参照: `normalizedClock.city`, `normalizedClock.cityId`, `normalizedClock.label`, `normalizedClock.labelColor`, `normalizedClock.timeZone`

## parseClockZonesPref()
- 位置: L206-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `parsed .map()`, `parsed .map(normalizeClockZone) .filter()`, `parsed .map(normalizeClockZone) .filter(Boolean) .slice()`
- 参照: `clocks.length`

## getCityFromTimeZone()
- 位置: L230-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `last.replace()`, `tz.split()`
- 参照: `segments.length`

## buildClockZone()
- 位置: L246-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCityFromTimeZone()`

## backfillClockLabelColors()
- 位置: L258-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clockZones.map()`, `getRandomLabelColor()`
- 参照: `clock.label`, `clock.labelColor`

## canonicalTimeZone()
- 位置: L271-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canonicalZoneCache.get()`, `canonicalZoneCache.has()`
- 条件付き依存: `if (!canonicalZoneCache.has(timeZone))` → `new Intl.DateTimeFormat(undefined, { timeZone, }).resolvedOptions()`
- 条件付き依存: `if (!canonicalZoneCache.has(timeZone))` → `canonicalZoneCache.set()`
- 参照: `Intl.DateTimeFormat`, `new Intl.DateTimeFormat(undefined, { timeZone, }).resolvedOptions().timeZone`

## normalizeCityQuery()
- 位置: L301-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(value ?? "") .normalize()`, `(value ?? "") .normalize("NFKD") .replace()`, `(value ?? "") .normalize("NFKD") .replace(/[\u0300-\u036f]/g, "") .toLowerCase()`, `PREFIX_EXPANSIONS.reduce()`, `text.replace()`

## maxTypos()
- 位置: L329-337
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `query.length`

## isWithinEditDistance()
- 位置: L343-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Math.abs()`, `Math.min()`
- 条件付き依存: `if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1])` → `Math.min()`
- 参照: `a.length`, `b.length`

## matchScore()
- 位置: L374-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `key.startsWith()`, `maxTypos()`
- 条件付き依存: `if (key.startsWith(query))` → `Math.min()`
- 条件付き依存: `if (!(key.startsWith(query)))` → `key.includes()`
- 条件付き依存: `if (allowSubstring && key.includes(query))` → `Math.min()`
- 条件付き依存: `if (best === MATCH_NONE && allowFuzzy && budget)` → `isWithinEditDistance()`

## buildNextClockZones()
- 位置: L397-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clockZones.map()`

## removeClockZoneAtIndex()
- 位置: L404-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clockZones.filter()`

## getCityAbbreviation()
- 位置: L413-429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CLOCK_CITY_BY_ID.get()`, `CLOCK_CITY_BY_NAME.get()`, `cityName.replace()`, `cityName.replace(/\s/g, "").slice()`, `cityName.replace(/\s/g, "").slice(0, 3).toUpperCase()`
- 参照: `byId.iataCode`, `byName.iataCode`

## getClockCityDisplay()
- 位置: L434-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CLOCK_CITY_BY_ID.get()`, `getCityFromTimeZone()`
- 参照: `CLOCK_CITY_BY_ID.get(clock.cityId)?.fallbackName`, `clock.city`, `clock.cityId`, `clock.timeZone`

## getTimeZoneAbbreviation()
- 位置: L448-459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat(locale, { timeZone: tz, timeZoneName: "short", }).formatToParts()`, `parts.find()`
- 参照: `Intl.DateTimeFormat`, `p.type`, `part?.value`

## getTimeZoneOffsetLabel()
- 位置: L465-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `new Intl.DateTimeFormat("en-US", { timeZone, timeZoneName: "longOffset", }).formatToParts()`, `parseInt()`, `parts.find()`, `raw.match()`
- 参照: `Intl.DateTimeFormat`, `p.type`, `parts.find(p => p.type === "timeZoneName")?.value`

## formatCustomZoneLabel()
- 位置: L485-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCityFromTimeZone()`, `getTimeZoneOffsetLabel()`

## offsetSearchKeys()
- 位置: L490-507
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hours.padStart()`, `offsetLabel.match()`

## dedupeKeys()
- 位置: L509-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `keys.filter()`

## buildRegionNameLookup()
- 位置: L512-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `displayNames.of()`
- 参照: `Intl.DisplayNames`

## getCuratedKeysByZone()
- 位置: L531-544
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!curatedKeysByZone)` → `canonicalTimeZone()`
- 条件付き依存: `if (!curatedKeysByZone)` → `curatedKeysByZone.set()`
- 条件付き依存: `if (!curatedKeysByZone)` → `curatedKeysByZone.get()`
- 条件付き依存: `if (!curatedKeysByZone)` → `normalizeCityQuery()`
- 条件付き依存: `if (!curatedKeysByZone)` → `(entry.aliases ?? []).map()`
- 参照: `entry.aliases`, `entry.fallbackName`, `entry.timeZone`

## buildZoneEntries()
- 位置: L546-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canonicalTimeZone()`, `curatedKeys.get()`, `dedupeKeys()`, `getCityFromTimeZone()`, `getCuratedKeysByZone()`, `getLocalizedTimeZoneName()`, `getTimeZoneAbbreviation()`, `getTimeZoneOffsetLabel()`, `localizedTimeZoneMap?.get()`, `normalizeCityQuery()`, `offsetSearchKeys()`, `offsetSearchKeys(offsetLabel).map()`, `supportedTimeZones.map()`

## buildClockSearchIndex()
- 位置: L587-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(entry.aliases ?? []).map()`, `buildRegionNameLookup()`, `buildZoneEntries()`, `canonicalTimeZone()`, `curatedCities.map()`, `dedupeKeys()`, `entry.id.slice()`, `entry.id.slice(0, 2).toUpperCase()`, `getLocalizedTimeZoneName()`, `normalizeCityQuery()`, `regionNameOf()`, `zoneEntries.map()`, `zoneNameByZone.get()`
- 参照: `entry.aliases`, `entry.fallbackName`, `entry.id`, `entry.timeZone`, `entry.zone`, `entry.zoneName`

## filterClockSearchIndex()
- 位置: L638-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `citiesMatchedZones.has()`, `index.filter()`, `kinds.includes()`, `normalizeCityQuery()`, `rank()`, `scored .filter()`, `scored .filter( ({ entry }) => entry.kind !== "zone" || !citiesMatchedZones.has(entry.zone) ) .sort()`, `scored .filter(({ entry }) => entry.kind === "city") .map()`
- 条件付き依存: `if (!scored.length)` → `rank()`
- 参照: `a.score`, `b.score`, `entry.kind`, `entry.zone`, `normalized.length`, `scored.length`

## rank()
- 位置: L651-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `matchScore()`, `pool .map()`
- 参照: `entry.searchKeys`

## filterCustomZoneResults()
- 位置: L688-700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filterClockSearchIndex()`, `filterClockSearchIndex(index, query, { limit, kinds: ["zone"] }).map()`

## getClockFormDerivedState()
- 位置: L702-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filterClockSearchIndex()`, `isValidTimeZone()`, `matches.map()`, `matches.some()`, `normalizeCityQuery()`
- 条件付き依存: `if (clockSelectedTimeZone && isValidTimeZone(clockSelectedTimeZone))` → `getCityFromTimeZone()`
- 条件付き依存: `if (query)` → `searchIndex.filter()`
- 条件付き依存: `if (query)` → `filteredResults.find()`
- 条件付き依存: `if (query)` → `normalizeCityQuery()`
- 条件付き依存: `if (query)` → `zoneEntries.find()`
- 条件付き依存: `if (!(exactId))` → `zoneEntries.filter()`
- 条件付き依存: `if (!(exactId))` → `normalizeCityQuery()`
- 参照: `entry.city`, `entry.cityId`, `entry.kind`, `entry.timeZone`, `entry.zoneName`, `exactCity.city`, `exactCity.cityId`, `exactCity.timeZone`, `exactId.city`, `exactId.timeZone`, `localizedMatches.length`, `only.city`, `only.timeZone`, `result.city`

## formatDateTimeAttr()
- 位置: L774-790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `date.toISOString()`, `get()`
- 参照: `Intl.DateTimeFormat`

## get()
- 位置: L785-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parts.find()`
- 参照: `p.type`, `parts.find(p => p.type === type)?.value`

## formatTime()
- 位置: L795-809
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Intl.DateTimeFormat(locale, opts).format()`
- 参照: `Intl.DateTimeFormat`, `opts.hour12`

## buildClocksRowAriaLabel()
- 位置: L815-821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parts.join()`
- 条件付き依存: `if (timeDisplay)` → `parts.push()`
