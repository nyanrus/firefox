# browser/components/aiwindow/ui/modules/AITabStore.sys.mjs

source: browser/components/aiwindow/ui/modules/AITabStore.sys.mjs
source-hash: bc786a20a5892d44bd4ded1fbf7ff4887c497e90
lines: 387

## <module>
- 役割: (未記入)

## AITabStore.logPrefix()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.logLevelPref()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.shutdownBlockerName()
- 位置: L49-51
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.CURRENT_SCHEMA_VERSION()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.databaseFileName()
- 位置: L57-59
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.prefBranch()
- 位置: L61-63
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.createEntityStatements()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.migrations()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)

## AITabStore.create()
- 位置: async L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#insertNextVersion()`

## AITabStore.edit()
- 位置: async L99-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#insertNextVersion()`

## AITabStore.getBySlug()
- 位置: async L110-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureConnection()`, `this.#parseRow()`, `this.connection.executeCached()`
- 参照: `rows.length`

## AITabStore.getBySlugAndVersion()
- 位置: async L127-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureConnection()`, `this.#parseRow()`, `this.connection.executeCached()`
- 参照: `rows.length`

## AITabStore.getVersionsBySlug()
- 位置: async L146-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.getResultByName()`, `rows.map()`, `this.#ensureConnection()`, `this.connection.executeCached()`

## AITabStore.getAITabPagesByConvId()
- 位置: async L164-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rows.map()`, `this.#ensureConnection()`, `this.#parseRow()`, `this.connection.executeCached()`

## AITabStore.deleteVersionsBefore()
- 位置: async L185-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureConnection()`, `this.connection.execute()`

## AITabStore.deleteBySlug()
- 位置: async L210-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureConnection()`, `this.connection.execute()`

## AITabStore.#parseRow()
- 位置: L222-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseJSONOrNull()`, `row.getResultByName()`

## AITabStore.#insertNextVersion()
- 位置: async L264-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `crypto.randomUUID()`, `this.#ensureConnection()`, `this.connection .executeTransaction()`, `this.connection.executeCached()`, `this.log.error()`, `toJSONOrNull()`
- 条件付き依存: `if (expectNew)` → `this.#mintSlug()`
- 条件付き依存: `if (!(expectNew))` → `this.connection.execute()`
- 条件付き依存: `if (!(expectNew))` → `rows[0].getResultByName()`
- 参照: `e.message`, `e.stack`

## AITabStore.#mintSlug()
- 位置: async L357-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.randomUUID()`, `crypto.randomUUID().slice()`, `rows[0].getResultByName()`, `this.connection.execute()`

## AITabStore.#ensureConnection()
- 位置: async L373-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureDatabase()`, `this.ensureDatabase().catch()`, `this.log.error()`
- 参照: `e.message`, `e.stack`
