# browser/components/urlbar/unitconverters/UnitConverterTimezone.sys.mjs

source: browser/components/urlbar/unitconverters/UnitConverterTimezone.sys.mjs
source-hash: 4051b6ac2415edc1c54d4cede9a98f5746a6fa2e
lines: 149

## <module>
- 役割: (未記入)

## UnitConverterTimezone.convert()
- 位置: L76-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QUERY_REGEX.exec()`, `inputDate.getTime()`, `inputDate.getTimezoneOffset()`, `new Intl.DateTimeFormat("en-US", { timeStyle: "short", hour12: isMeridiemNeeded, timeZone: "UTC", }).format()`, `outputDate.getUTCMinutes()`, `outputDate.setUTCMinutes()`, `regexResult[1].toUpperCase()`, `regexResult[6]?.toUpperCase()`, `regexResult[7].toUpperCase()`
- 条件付き依存: `if (inputTime === KEYWORD_NOW)` → `inputDate.setUTCHours()`
- 条件付き依存: `if (inputTime === KEYWORD_NOW)` → `inputDate.getHours()`
- 条件付き依存: `if (inputTime === KEYWORD_NOW)` → `inputDate.setUTCMinutes()`
- 条件付き依存: `if (inputTime === KEYWORD_NOW)` → `inputDate.getMinutes()`
- 条件付き依存: `if (!(inputTime === KEYWORD_NOW))` → `regexResult[5]?.toLowerCase()`
- 条件付き依存: `if (!(inputTime === KEYWORD_NOW))` → `Number()`
- 条件付き依存: `if (!(inputTime === KEYWORD_NOW))` → `inputDate.setUTCHours()`
- 条件付き依存: `if (!(inputTime === KEYWORD_NOW))` → `inputDate.setUTCMinutes()`
- 条件付き依存: `if (outputTimezone === KEYWORD_HERE)` → `inputDate.getTimezoneOffset()`
- 条件付き依存: `if (outputTimezone === KEYWORD_HERE)` → `Math.floor()`
- 条件付き依存: `if (outputTimezone === KEYWORD_HERE)` → `Math.abs()`
- 条件付き依存: `if (outputTimezone === KEYWORD_HERE)` → `formatMinutes()`
- 参照: `Intl.DateTimeFormat`

## formatMinutes()
- 位置: L146-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `minutes.toString()`, `minutes.toString().padStart()`
