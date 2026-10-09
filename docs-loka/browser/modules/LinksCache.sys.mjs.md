# browser/modules/LinksCache.sys.mjs

source: browser/modules/LinksCache.sys.mjs
source-hash: b6ab328b930857b24ffc5a1cff7e6f91c9bab2bf
lines: 134

## <module>
- 役割: (未記入)

## LinksCache.constructor()
- 位置: L28-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clear()`
- 参照: `this.linkGetter`, `this.migrateProperties`, `this.shouldRefresh`

## this.linkGetter()
- 位置: L37-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ret.call()`

## LinksCache.clear()
- 位置: L50-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `this.expire()`
- 参照: `this.cache`, `this.lastOptions`

## LinksCache.expire()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.lastUpdate`

## LinksCache.request()
- 位置: async L69-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await this.cache).map()`, `Date.now()`, `Object.assign()`, `this.shouldRefresh()`
- 条件付き依存: `if (oldLink)` → `toMigrate.set()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `resolve()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `(await this.linkGetter(options)).map()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `this.linkGetter()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `Object.assign()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `toMigrate.get()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `reject()`
- 参照: `newLink.__sharedCache`, `newLink.__sharedCache.updateLink`, `newLink.url`, `oldLink.url`, `this.cache`, `this.lastOptions`, `this.lastUpdate`, `this.migrateProperties`

## newLink.__sharedCache.updateLink()
- 位置: L117-119
- 役割: (未記入)
- 触るとき: (未記入)
