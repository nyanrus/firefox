# browser/components/urlbar/unitconverters/UnitConverterTemperature.sys.mjs

source: browser/components/urlbar/unitconverters/UnitConverterTemperature.sys.mjs
source-hash: eef2f525517a3234c0cb3b2e2a744c7fb5937780
lines: 131

## <module>
- 役割: (未記入)

## UnitConverterTemperature.convert()
- 位置: L32-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `QUERY_REGEX.exec()`, `UrlbarUtils.formatUnitConversionResult()`, `findUnits()`, `formatter.formatToParts()`, `inputUnit.charAt()`, `outputUnit.charAt()`, `parseFloat()`, `parts.find()`
- 条件付き依存: `if (!(inputChar === outputChar))` → `this[`${inputChar}2${outputChar}`]()`
- 参照: `Intl.NumberFormat`, `part.type`, `parts.find(part => part.type == "unit").value`

## UnitConverterTemperature.c2k()
- 位置: L75-77
- 役割: (未記入)
- 触るとき: (未記入)

## UnitConverterTemperature.c2f()
- 位置: L79-81
- 役割: (未記入)
- 触るとき: (未記入)

## UnitConverterTemperature.k2c()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)

## UnitConverterTemperature.k2f()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.c2f()`, `this.k2c()`

## UnitConverterTemperature.f2c()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)

## UnitConverterTemperature.f2k()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.c2k()`, `this.f2c()`

## findUnits()
- 位置: L110-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UNITS.includes()`, `inputUnit.toLowerCase()`, `outputUnit.toLowerCase()`, `toAbsoluteUnit()`

## toAbsoluteUnit()
- 位置: L124-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ABSOLUTE.find()`, `a.startsWith()`, `unit.slice()`
- 参照: `unit.length`
