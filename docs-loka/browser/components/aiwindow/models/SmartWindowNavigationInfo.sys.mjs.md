# browser/components/aiwindow/models/SmartWindowNavigationInfo.sys.mjs

source: browser/components/aiwindow/models/SmartWindowNavigationInfo.sys.mjs
source-hash: daf62297b220a1f8d4c92b6b16c6e6655aae231a
lines: 103

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## buildNavEntries()
- 位置: L31-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(lazy.PREFERENCES_NAV_MAP).map()`, `[info.breadcrumb, info.description] .filter()`, `[info.breadcrumb, info.description] .filter(Boolean) .join()`, `[info.breadcrumb, info.description] .filter(Boolean) .join(". ") .toLowerCase()`
- 参照: `info.breadcrumb`, `info.description`, `info.label`, `lazy.PREFERENCES_NAV_MAP`

## NavigationInfoImpl.getRelevantNavigation()
- 位置: async L62-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.cosSim()`, `query.toLowerCase()`, `this.#embeddingsGenerator.embed()`, `this.#navEmbeddings .map()`
- 条件付き依存: `if (!this.#navEntries)` → `buildNavEntries()`
- 条件付き依存: `if (!this.#embeddingsGenerator)` → `lazy.embeddingsGeneratorFactory.forGeneral()`
- 条件付き依存: `if (!this.#navEmbeddings)` → `this.#embeddingsGenerator.embedMany()`
- 条件付き依存: `if (!this.#navEmbeddings)` → `this.#navEntries.map()`
- 参照: `a.similarity`, `b.similarity`, `e.embeddingText`, `e.similarity`, `queryEmbedding.length`, `queryResult.output`, `result.output`, `this.#embeddingsGenerator`, `this.#navEmbeddings`, `this.#navEntries`
