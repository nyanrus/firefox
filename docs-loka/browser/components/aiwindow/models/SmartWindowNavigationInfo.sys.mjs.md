# browser/components/aiwindow/models/SmartWindowNavigationInfo.sys.mjs

source: browser/components/aiwindow/models/SmartWindowNavigationInfo.sys.mjs
source-hash: daf62297b220a1f8d4c92b6b16c6e6655aae231a
lines: 103

## <module>
- 役割: 設定画面のナビゲーション対応表を埋め込みベクトルで検索し、「どこで設定できるか」の質問に近い設定ページを返す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## buildNavEntries()
- 位置: L31-42
- 役割: PREFERENCES_NAV_MAP を配列にし、パンくずと説明文を連結した小文字の埋め込み用テキストを各項目に付ける。
- 触るとき: 設定ページを検索する文章(埋め込み対象)を増やすとき、または検索ヒットの語句が合わないとき。
- 呼び出し先: `Object.entries()`, `Object.entries(lazy.PREFERENCES_NAV_MAP).map()`, `[info.breadcrumb, info.description] .filter()`, `[info.breadcrumb, info.description] .filter(Boolean) .join()`, `[info.breadcrumb, info.description] .filter(Boolean) .join(". ") .toLowerCase()`
- 参照: `info.breadcrumb`, `info.description`, `info.label`, `lazy.PREFERENCES_NAV_MAP`

## NavigationInfoImpl.getRelevantNavigation()
- 位置: async L62-99
- 役割: 初回だけ項目と埋め込みを作り、クエリを埋め込んで cosSim を計算し、閾値以上を上位 topK 件返す。
- 触るとき: ナビ検索の件数や閾値を変えるとき、または該当なしになる原因を調べるとき。
- 呼び出し先: `Array.isArray()`, `lazy.cosSim()`, `query.toLowerCase()`, `this.#embeddingsGenerator.embed()`, `this.#navEmbeddings .map()`
- 条件付き依存: `if (!this.#navEntries)` → `buildNavEntries()`
- 条件付き依存: `if (!this.#embeddingsGenerator)` → `lazy.embeddingsGeneratorFactory.forGeneral()`
- 条件付き依存: `if (!this.#navEmbeddings)` → `this.#embeddingsGenerator.embedMany()`
- 条件付き依存: `if (!this.#navEmbeddings)` → `this.#navEntries.map()`
- 参照: `a.similarity`, `b.similarity`, `e.embeddingText`, `e.similarity`, `queryEmbedding.length`, `queryResult.output`, `result.output`, `this.#embeddingsGenerator`, `this.#navEmbeddings`, `this.#navEntries`
