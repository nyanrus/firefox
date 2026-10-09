# browser/components/aiwindow/services/MemoryStoreConstants.sys.mjs

source: browser/components/aiwindow/services/MemoryStoreConstants.sys.mjs
source-hash: be58ddab9d9c57ef048c3149181511e95ec0a0c1
lines: 125

## <module>
- 役割: (未記入)

## field()
- 位置: L57-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AGGREGATE_FIELD_REGEX.test()`, `MEMORY_FILTER_NUMBER_FIELDS.includes()`

## value()
- 位置: L61-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`

## field()
- 位置: L66-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MEMORY_FILTER_ARRAY_FIELDS.includes()`

## value()
- 位置: L67-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`

## field()
- 位置: L73-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MEMORY_FILTER_ARRAY_FIELDS.includes()`

## value()
- 位置: L74-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object()`

## field()
- 位置: L77-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MEMORY_FILTER_SCALAR_FIELDS.includes()`

## value()
- 位置: L78-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`

## field()
- 位置: L85-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AGGREGATE_FIELD_REGEX.test()`, `MEMORY_FILTER_SCALAR_FIELDS.includes()`

## value()
- 位置: L89-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object()`

## field()
- 位置: L94-94
- 役割: (未記入)
- 触るとき: (未記入)

## value()
- 位置: L95-95
- 役割: (未記入)
- 触るとき: (未記入)

## [MEMORY_FILTER_COMPARATOR.INCLUDES]()
- 位置: L101-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `field.includes()`

## [MEMORY_FILTER_COMPARATOR.IN]()
- 位置: L103-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.includes()`

## [MEMORY_FILTER_COMPARATOR.GREATER_THAN]()
- 位置: L104-104
- 役割: (未記入)
- 触るとき: (未記入)

## [MEMORY_FILTER_COMPARATOR.LESS_THAN]()
- 位置: L105-105
- 役割: (未記入)
- 触るとき: (未記入)

## [MEMORY_FILTER_COMPARATOR.GREATER_THAN_OR_EQUAL_TO]()
- 位置: L106-107
- 役割: (未記入)
- 触るとき: (未記入)

## [MEMORY_FILTER_COMPARATOR.LESS_THAN_OR_EQUAL_TO]()
- 位置: L108-109
- 役割: (未記入)
- 触るとき: (未記入)

## [MEMORY_FILTER_COMPARATOR.EQUAL_TO]()
- 位置: L110-110
- 役割: (未記入)
- 触るとき: (未記入)

## [MEMORY_FILTER_COMPARATOR.SOME]()
- 位置: L111-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `field.includes()`, `value.some()`

## [MEMORY_FILTER_COMPARATOR.ALL]()
- 位置: L113-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `[...valueSet].every()`, `fieldSet.has()`
- 参照: `fieldSet.size`, `valueSet.size`
