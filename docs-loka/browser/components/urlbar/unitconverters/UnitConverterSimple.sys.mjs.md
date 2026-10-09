# browser/components/urlbar/unitconverters/UnitConverterSimple.sys.mjs

source: browser/components/urlbar/unitconverters/UnitConverterSimple.sys.mjs
source-hash: dc249e5b04f63e998ef5d73f1fdffbc0b5a11224
lines: 291

## <module>
- 役割: 角度・力・長さ・質量・速さの単位を換算表から変換するモジュール。

## UnitConverterSimple.convert()
- 位置: L222-251
- 役割: 単位表の同じグループ内の比で値を換算し、表示文字列を返す。
- 触るとき: 換算式や結果の桁・表記を変えるとき。単位が別グループだったり解析できない入力は null を返すので、その判定を見直すときにも読む。
- 呼び出し先: `Number()`, `QUERY_REGEX.exec()`, `UrlbarUtils.formatUnitConversionResult()`, `findUnitGroup()`, `formatter.formatToParts()`, `parts.find()`, `regexResult[2].trim()`, `regexResult[3].trim()`
- 参照: `Intl.NumberFormat`, `part.type`, `parts.find(part => part.type == "unit").value`

## findUnitGroup()
- 位置: L263-281
- 役割: 入出力の単位を両方含む最初のグループを探し、別名を正規の単位名に直して返す。
- 触るとき: 単位の別名を追加したとき、別グループの単位と誤って一致しないか確かめるとき。どちらかが見つからないと null を返す。
- 呼び出し先: `UNITS_GROUPS.find()`, `toSuitableUnit()`

## toSuitableUnit()
- 位置: L288-290
- 役割: 大文字小文字を区別する単位(PN, MN など)以外は小文字に揃える。
- 触るとき: 大文字と小文字で別の単位になる記号を追加するとき。判定は CASE_SENSITIVE_UNITS の一覧に依存するので、そちらと合わせて見る。
- 呼び出し先: `CASE_SENSITIVE_UNITS.includes()`, `unit.toLowerCase()`
