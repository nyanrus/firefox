# browser/components/urlbar/unitconverters/UnitConverterSimple.sys.mjs

source: browser/components/urlbar/unitconverters/UnitConverterSimple.sys.mjs
source-hash: dc249e5b04f63e998ef5d73f1fdffbc0b5a11224
lines: 291

## <module>
- 役割: (未記入)

## UnitConverterSimple.convert()
- 位置: L222-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `QUERY_REGEX.exec()`, `UrlbarUtils.formatUnitConversionResult()`, `findUnitGroup()`, `formatter.formatToParts()`, `parts.find()`, `regexResult[2].trim()`, `regexResult[3].trim()`
- 参照: `Intl.NumberFormat`, `part.type`, `parts.find(part => part.type == "unit").value`

## findUnitGroup()
- 位置: L263-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UNITS_GROUPS.find()`, `toSuitableUnit()`

## toSuitableUnit()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CASE_SENSITIVE_UNITS.includes()`, `unit.toLowerCase()`
