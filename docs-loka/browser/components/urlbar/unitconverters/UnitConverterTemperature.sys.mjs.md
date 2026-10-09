# browser/components/urlbar/unitconverters/UnitConverterTemperature.sys.mjs

source: browser/components/urlbar/unitconverters/UnitConverterTemperature.sys.mjs
source-hash: eef2f525517a3234c0cb3b2e2a744c7fb5937780
lines: 131

## <module>
- 役割: 摂氏・華氏・ケルビンの温度換算を、検索文字列から行うモジュール。

## UnitConverterTemperature.convert()
- 位置: L32-73
- 役割: 「数値 単位 in 単位」形式を解析し、温度を換算して表示文字列を返す。
- 触るとき: 入力の書式(in/to/=)や結果の単位記号の付け方を変えるとき。解析できない入力や未知の単位は null を返すので、その判定を見直すときにも読む。
- 呼び出し先: `Number()`, `QUERY_REGEX.exec()`, `UrlbarUtils.formatUnitConversionResult()`, `findUnits()`, `formatter.formatToParts()`, `inputUnit.charAt()`, `outputUnit.charAt()`, `parseFloat()`, `parts.find()`
- 条件付き依存: `if (!(inputChar === outputChar))` → `this[`${inputChar}2${outputChar}`]()`
- 参照: `Intl.NumberFormat`, `part.type`, `parts.find(part => part.type == "unit").value`

## UnitConverterTemperature.c2k()
- 位置: L75-77
- 役割: 摂氏をケルビンに変換する(+273.15)。
- 触るとき: 基準温度の換算式を直すとき。f2k など経由で使われるので、そちらの結果も確かめる。

## UnitConverterTemperature.c2f()
- 位置: L79-81
- 役割: 摂氏を華氏に変換する(×1.8+32)。
- 触るとき: 華氏への換算式を直すとき。k2f からも呼ばれるので、そこへの影響を見る。

## UnitConverterTemperature.k2c()
- 位置: L83-85
- 役割: ケルビンを摂氏に変換する(-273.15)。
- 触るとき: ケルビン入力の扱いを変えるとき。k2f の前段として使われるので併せて確認する。

## UnitConverterTemperature.k2f()
- 位置: L87-89
- 役割: ケルビンを華氏に変換する。k2c の結果を c2f に渡す。
- 触るとき: ケルビンから華氏への経路を変えるとき。計算は k2c と c2f に任せているので、その二つを確認すれば足りる。
- 呼び出し先: `this.c2f()`, `this.k2c()`

## UnitConverterTemperature.f2c()
- 位置: L91-93
- 役割: 華氏を摂氏に変換する((F-32)/1.8)。
- 触るとき: 華氏入力の換算式を直すとき、c2f の逆関数になっているか確かめたいとき。

## UnitConverterTemperature.f2k()
- 位置: L95-97
- 役割: 華氏をケルビンに変換する。f2c の結果を c2k に渡す。
- 触るとき: 華氏からケルビンへの換算経路を変えるとき。
- 呼び出し先: `this.c2k()`, `this.f2c()`

## findUnits()
- 位置: L110-122
- 役割: 入出力の単位を小文字にし、温度単位として有効か確かめて絶対単位名に直す。
- 触るとき: 受け付ける単位の別名を増やすとき、大文字小文字の扱いを変えるときに見る。無効な単位があると null を返す。
- 呼び出し先: `UNITS.includes()`, `inputUnit.toLowerCase()`, `outputUnit.toLowerCase()`, `toAbsoluteUnit()`

## toAbsoluteUnit()
- 位置: L124-130
- 役割: 2文字以下の略記(c, k, f, °c など)を絶対単位名(celsius など)に直す。3文字以上はそのまま返す。
- 触るとき: 新しい略記を追加するとき。略記は末尾1文字で ABSOLUTE から探すので、先頭文字が重なる単位に注意する。
- 呼び出し先: `ABSOLUTE.find()`, `a.startsWith()`, `unit.slice()`
- 参照: `unit.length`
