# browser/components/pagedata/PageDataParent.sys.mjs

source: browser/components/pagedata/PageDataParent.sys.mjs
source-hash: 939dae368fd1ec3951f6076e46863c6f309d9ff4
lines: 58

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PageDataParent.collectPageData()
- 位置: L25-35
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#deferredCollection)` → `Promise.withResolvers()`
- 条件付き依存: `if (!this.#deferredCollection)` → `this.sendQuery("PageData:Collect").then()`
- 条件付き依存: `if (!this.#deferredCollection)` → `this.sendQuery()`
- 参照: `this.#deferredCollection`, `this.#deferredCollection.promise`, `this.#deferredCollection.reject`, `this.#deferredCollection.resolve`

## PageDataParent.didDestroy()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deferredCollection?.resolve()`

## PageDataParent.receiveMessage()
- 位置: L50-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PageDataService.pageLoaded()`
- 参照: `msg.data.url`, `msg.name`
