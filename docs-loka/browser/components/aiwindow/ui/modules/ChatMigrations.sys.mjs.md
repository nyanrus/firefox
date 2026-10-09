# browser/components/aiwindow/ui/modules/ChatMigrations.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatMigrations.sys.mjs
source-hash: e988d2acf016fb11a48cc71222ca61dda667024b
lines: 252

## <module>
- 役割: (未記入)

## applyV2()
- 位置: async L25-29
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (version < 2)` → `conn.execute()`

## getColumns()
- 位置: async L42-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.map()`, `conn.execute()`
- 参照: `c.name`

## applyV3()
- 位置: async L48-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV4()
- 位置: async L73-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV5()
- 位置: async L89-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV6()
- 位置: async L105-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV7()
- 位置: async L121-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV8()
- 位置: async L161-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV9()
- 位置: async L175-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.execute()`

## applyV10()
- 位置: async L184-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `columns.has()`, `conn.execute()`, `getColumns()`

## applyV11()
- 位置: async L201-218
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.execute()`

## applyV12()
- 位置: async L223-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.execute()`
