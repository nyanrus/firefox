# browser/components/urlbar/unitconverters/UnitConverterTimezone.sys.mjs

source: browser/components/urlbar/unitconverters/UnitConverterTimezone.sys.mjs
source-hash: 4051b6ac2415edc1c54d4cede9a98f5746a6fa2e
lines: 149

## <module>
- 役割: タイムゾーン略語の固定オフセット表を使い、時刻を別のタイムゾーンへ換算するモジュール。

## UnitConverterTimezone.convert()
- 位置: L76-143
- 役割: 「時刻 タイムゾーン in タイムゾーン」を解析し、UTC 差で時刻を換算して返す。
- 触るとき: 入力書式、'now' や 'here' の扱い、AM/PM の表示を変えるとき。未知の略語は null を返す。'now' は現在のローカル時刻を基にしてオフセットで補正する。
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
- 役割: 数値を2桁のゼロ埋め文字列にする。here 出力の分の部分で使う。
- 触るとき: here 出力の UTC±時:分 表記を直すとき。呼び出し側が (オフセットの分 % 60) * 60 を渡しており、30分単位の時差で表示が崩れる可能性がある(要確認)。
- 呼び出し先: `minutes.toString()`, `minutes.toString().padStart()`
