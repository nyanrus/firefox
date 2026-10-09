# browser/extensions/newtab/lib/PersistentCache.sys.mjs

source: browser/extensions/newtab/lib/PersistentCache.sys.mjs
source-hash: c7cf5e115f01669e7a726f15fe685aeee8b0d8e8
lines: 91

## <module>
- 役割: (未記入)

## PersistentCache.constructor()
- 位置: L15-21
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (preload)` → `this._load()`
- 参照: `this._filename`, `this.name`

## PersistentCache.set()
- 位置: async L29-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._load()`, `this._persist()`

## PersistentCache.get()
- 位置: async L41-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._load()`

## PersistentCache._load()
- 位置: L49-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.readJSON()`, `PathUtils.join()`, `reject()`, `resolve()`
- 条件付き依存: `if ( // isInstance() is not available in node unit test. It should be safe to use instanceof as it's directly from IOUtils. // eslint-disable-next-line mozilla/u...)` → `console.error()`
- 参照: `PathUtils.localProfileDir`, `error.message`, `error.name`, `this._cache`, `this._filename`

## PersistentCache._persist()
- 位置: async L84-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.writeJSON()`, `PathUtils.join()`
- 参照: `PathUtils.localProfileDir`, `this._filename`
