# browser/components/pagedata/PageDataSchema.sys.mjs

source: browser/components/pagedata/PageDataSchema.sys.mjs
source-hash: 682e0148282cfff738b206e756a7c30d6ec672ce
lines: 255

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## loadSchema()
- 位置: async L53-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SCHEMAS.has()`, `SCHEMAS.set()`, `fetch()`, `response.json()`, `schemaName.toLocaleLowerCase()`
- 条件付き依存: `if (SCHEMAS.has(schemaName))` → `SCHEMAS.get()`
- 参照: `response.ok`, `response.statusText`

## validateData()
- 位置: async L77-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.JsonSchemaValidator.validate()`, `loadSchema()`, `schemaName.toLocaleLowerCase()`
- 参照: `result.error`, `result.valid`

## nameForType()
- 位置: L113-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 参照: `this.DATA_TYPE`

## validateData()
- 位置: async L132-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.nameForType()`, `validateData()`

## validatePageData()
- 位置: async L151-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `this.nameForType()`, `validateData()`

## coalescePageData()
- 位置: L191-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.entries()`
- 条件付き依存: `if (type in newMap)` → `Object.assign()`

## collectPageData()
- 位置: async L228-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Promise.all()`, `collector.collect()`, `lazy.DATA_COLLECTORS.map()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `pageDataList.reduce()`, `this.validatePageData()`
- 参照: `PageDataSchema.coalescePageData`, `document.documentURI`
