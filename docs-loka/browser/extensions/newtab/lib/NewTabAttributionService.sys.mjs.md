# browser/extensions/newtab/lib/NewTabAttributionService.sys.mjs

source: browser/extensions/newtab/lib/NewTabAttributionService.sys.mjs
source-hash: fc32ff967e504ae8b2d0c6d9894e4c31886b6b75
lines: 494

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## NewTabAttributionService.constructor()
- 位置: L66-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#dapSenderInternal`, `this.#dateProvider`, `this.#testDapOptions`, `this.budgetStoreName`, `this.dbName`, `this.dbVersion`, `this.impressionStoreName`, `this.models`, `this.storeNames`

## NewTabAttributionService.#dapSender()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.DAPSender`, `this.#dapSenderInternal`

## NewTabAttributionService.#now()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dateProvider.now()`

## NewTabAttributionService.#getTrainhopConfig()
- 位置: L91-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.activityStream?.store.getState()`
- 参照: `lazy.AboutNewTab.activityStream?.store.getState().Prefs.values .trainhopConfig`

## NewTabAttributionService.onAttributionEvent()
- 位置: async L105-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#getImpression()`, `this.#getModelProp()`, `this.#now()`, `this.#updateImpression()`
- 参照: `impression.lastImpression`, `params.index`, `params.partner_id`

## NewTabAttributionService.onAttributionReset()
- 位置: async L138-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `budgetStore.get()`, `budgetStore.getAllKeys()`, `budgetStore.put()`, `console.error()`, `impressionStore.clear()`, `this.#getBudgetStore()`, `this.#getImpressionStore()`, `this.#now()`

## NewTabAttributionService.onAttributionConversion()
- 位置: async L179-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `console.error()`, `this.#dapSender.sendDAPMeasurement()`, `this.#findImpression()`, `this.#getBudget()`, `this.#getTaskConfig()`, `this.#getTrainhopConfig()`, `this.#now()`, `this.#updateBudget()`
- 条件付き依存: `if (dapHpke)` → `lazy.HPKEConfigManager.decodeKey()`
- 参照: `attributionConfig.maxConversions`, `attributionConfig.maxLookbackDays`, `budget.conversions`, `impression.conversion.index`, `options.ohttp_hpke`, `options.ohttp_relay`, `receivedTaskConfig.default_measurement`, `receivedTaskConfig.length`, `receivedTaskConfig.task_id`, `trainhopConfig.attribution`
- XPCOM: `Services.prefs`

## NewTabAttributionService.#findImpression()
- 位置: async L269-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `impressions // Filter by lookback days .filter()`, `this.#getImpressionStore()`, `this.#getModelProp()`, `this.#getPartnerImpressions()`

## NewTabAttributionService.#getImpression()
- 位置: async L304-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `impressions.find()`, `this.#compareImpression()`, `this.#getImpressionStore()`, `this.#getPartnerImpressions()`

## NewTabAttributionService.#getTaskConfig()
- 位置: async L317-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `console.error()`, `encodeURIComponent()`, `lazy.ObliviousHTTP.getOHTTPConfig()`, `lazy.ObliviousHTTP.ohttpRequest()`, `response.json()`
- 条件付き依存: `if (!config)` → `console.error()`
- 参照: `error.message`
- XPCOM: `Services.prefs`

## NewTabAttributionService.#updateImpression()
- 位置: async L369-386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `impressionStore.put()`, `impressions.findIndex()`, `this.#compareImpression()`, `this.#getImpressionStore()`, `this.#getPartnerImpressions()`
- 条件付き依存: `if (i < 0)` → `impressions.push()`

## NewTabAttributionService.#compareImpression()
- 位置: L393-395
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `cur.conversion.index`, `impression.conversion.index`

## NewTabAttributionService.#getBudget()
- 位置: async L404-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `budgetStore.get()`, `this.#getBudgetStore()`
- 参照: `budget.nextReset`

## NewTabAttributionService.#updateBudget()
- 位置: async L425-429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `budgetStore.put()`, `this.#getBudgetStore()`
- 参照: `budget.conversions`

## NewTabAttributionService.#getPartnerImpressions()
- 位置: async L436-439
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `impressionStore.get()`

## NewTabAttributionService.#getImpressionStore()
- 位置: async L441-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getStore()`
- 参照: `this.impressionStoreName`

## NewTabAttributionService.#getBudgetStore()
- 位置: async L445-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getStore()`
- 参照: `this.budgetStoreName`

## NewTabAttributionService.#getStore()
- 位置: async L449-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.#db).objectStore()`
- 参照: `this.#db`

## NewTabAttributionService.#db()
- 位置: L453-455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#createOrOpenDb()`
- 参照: `this._db`

## NewTabAttributionService.#createOrOpenDb()
- 位置: async L457-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IndexedDB.deleteDatabase()`, `this.#openDatabase()`
- 参照: `this.dbName`

## NewTabAttributionService.#openDatabase()
- 位置: async L466-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.objectStoreNames.contains()`, `lazy.IndexedDB.open()`, `this.storeNames.forEach()`
- 条件付き依存: `if (!db.objectStoreNames.contains(store))` → `db.createObjectStore()`
- 参照: `this.dbName`, `this.dbVersion`

## NewTabAttributionService.#getModelProp()
- 位置: L483-485
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.models`, `this.models.default`
