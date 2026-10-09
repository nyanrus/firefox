# browser/components/aiwindow/services/MemoryStoreConstants.sys.mjs

source: browser/components/aiwindow/services/MemoryStoreConstants.sys.mjs
source-hash: be58ddab9d9c57ef048c3149181511e95ec0a0c1
lines: 125

## <module>
- 役割: 記憶の取り出し条件(getMemories)で使う比較の種類、項目ごとの許可、比較と照合の関数を定義する。

## field()
- 位置: L57-60
- 役割: 数値の比較で使える項目か判定する。数値の項目名か、recent_accessed_countsの日指定の形かを見る。
- 触るとき: 数値比較の対象に項目を足すとき、日指定の書式を変えるとき。
- 呼び出し先: `AGGREGATE_FIELD_REGEX.test()`, `MEMORY_FILTER_NUMBER_FIELDS.includes()`

## value()
- 位置: L61-61
- 役割: 数値の比較の値が有限な数値かを判定する。
- 触るとき: 数値比較の値の制約を変えるとき。
- 呼び出し先: `Number.isFinite()`

## field()
- 位置: L66-66
- 役割: 配列の比較で使える項目か判定する。
- 触るとき: 配列項目を検索対象に足すとき。
- 呼び出し先: `MEMORY_FILTER_ARRAY_FIELDS.includes()`

## value()
- 位置: L67-67
- 役割: 配列の比較の値が配列かを判定する。
- 触るとき: SOMEやALLに渡す値の形を変えるとき。
- 呼び出し先: `Array.isArray()`

## field()
- 位置: L73-73
- 役割: INCLUDESで使える配列項目か判定する。
- 触るとき: INCLUDESの対象項目を変えるとき。
- 呼び出し先: `MEMORY_FILTER_ARRAY_FIELDS.includes()`

## value()
- 位置: L74-74
- 役割: INCLUDESの値が配列や辞書などのオブジェクトでないかを判定する。
- 触るとき: INCLUDESに渡せる値の種類を変えるとき。
- 呼び出し先: `Object()`

## field()
- 位置: L77-77
- 役割: INで使える単純な項目(文字列と数値)か判定する。
- 触るとき: IN検索の対象項目を変えるとき。
- 呼び出し先: `MEMORY_FILTER_SCALAR_FIELDS.includes()`

## value()
- 位置: L78-78
- 役割: INの値が配列かを判定する。
- 触るとき: IN検索に渡す値の形を変えるとき。
- 呼び出し先: `Array.isArray()`

## field()
- 位置: L85-88
- 役割: EQUAL_TOで使える単純な項目か、日指定の集計項目かを判定する。
- 触るとき: EQUAL_TOの対象項目を変えるとき。
- 呼び出し先: `AGGREGATE_FIELD_REGEX.test()`, `MEMORY_FILTER_SCALAR_FIELDS.includes()`

## value()
- 位置: L89-89
- 役割: EQUAL_TOの値がオブジェクトでないかを判定する。
- 触るとき: EQUAL_TOに渡せる値の種類を変えるとき。
- 呼び出し先: `Object()`

## field()
- 位置: L94-94
- 役割: LIKEはmemory_summaryにだけ使えるかを判定する。
- 触るとき: 意味検索の対象項目を増やすとき。

## value()
- 位置: L95-95
- 役割: LIKEの値が文字列かを判定する。
- 触るとき: 意味検索に渡す値の制約を変えるとき。

## [MEMORY_FILTER_COMPARATOR.INCLUDES]()
- 位置: L101-102
- 役割: 項目が配列で、その中に値を含むときに真を返す。
- 触るとき: INCLUDESの一致判定を変えるとき。
- 呼び出し先: `Array.isArray()`, `field.includes()`

## [MEMORY_FILTER_COMPARATOR.IN]()
- 位置: L103-103
- 役割: 項目の値が、与えられた配列に含まれるときに真を返す。
- 触るとき: IN検索の一致判定を変えるとき。
- 呼び出し先: `value.includes()`

## [MEMORY_FILTER_COMPARATOR.GREATER_THAN]()
- 位置: L104-104
- 役割: 項目が値より大きいかを返す。
- 触るとき: 数値の大小の比較を調べるとき。

## [MEMORY_FILTER_COMPARATOR.LESS_THAN]()
- 位置: L105-105
- 役割: 項目が値より小さいかを返す。
- 触るとき: 数値の大小の比較を調べるとき。

## [MEMORY_FILTER_COMPARATOR.GREATER_THAN_OR_EQUAL_TO]()
- 位置: L106-107
- 役割: 項目が値以上かを返す。
- 触るとき: 以上の条件の境界の扱いを確かめるとき。

## [MEMORY_FILTER_COMPARATOR.LESS_THAN_OR_EQUAL_TO]()
- 位置: L108-109
- 役割: 項目が値以下かを返す。
- 触るとき: 以下の条件の境界の扱いを確かめるとき。

## [MEMORY_FILTER_COMPARATOR.EQUAL_TO]()
- 位置: L110-110
- 役割: 項目と値が厳密に等しいかを返す。
- 触るとき: 一致条件の判定を変えるとき。

## [MEMORY_FILTER_COMPARATOR.SOME]()
- 位置: L111-112
- 役割: 項目の配列と値の配列に、共通の要素が一つでもあれば真を返す。
- 触るとき: SOMEの一致判定を変えるとき。
- 呼び出し先: `Array.isArray()`, `field.includes()`, `value.some()`

## [MEMORY_FILTER_COMPARATOR.ALL]()
- 位置: L113-123
- 役割: 項目の配列と値の配列を集合として比べ、要素数が同じで全部一致すれば真を返す。
- 触るとき: ALLの一致判定を変えるとき。重複の扱いを確かめるとき。
- 呼び出し先: `Array.isArray()`, `[...valueSet].every()`, `fieldSet.has()`
- 参照: `fieldSet.size`, `valueSet.size`
