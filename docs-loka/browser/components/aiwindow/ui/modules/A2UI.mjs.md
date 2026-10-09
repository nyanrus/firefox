# browser/components/aiwindow/ui/modules/A2UI.mjs

source: browser/components/aiwindow/ui/modules/A2UI.mjs
source-hash: 0ff61547777aea0d302bd5cb8ca6a0c4e7eeccae
lines: 308

## <module>
- 役割: 生成 AI が返す A2UI 形式の JSON を、描画用の構造に変換する A2UI クラスを定義する

## A2UI.constructor()
- 位置: L17-28
- 役割: 入力 JSON を複製して保持し、コンポーネント種別ごとの変換関数を登録する
- 触るとき: 対応するコンポーネント種別を増やすとき、変換の登録漏れを調べるとき
- 呼び出し先: `structuredClone()`, `this.#hydrateCards.bind()`, `this.#hydrateHighlights.bind()`, `this.#hydrateList.bind()`, `this.#hydrateRankedTable.bind()`, `this.#hydrateSourceLinks.bind()`, `this.#hydrateTextBlock.bind()`, `this.#hydrateTimeline.bind()`, `this.#hydrators.set()`
- 参照: `this.#hydrators`, `this.#surface`

## A2UI.toUI()
- 位置: L33-58
- 役割: root コンポーネントを起点に、ヘッダーと子を変換して描画用のページ構造を返す(root が無ければ空のページ)
- 触るとき: 生成結果の描画全体の流れを追うとき、ページ構造の入口を変えるとき
- 呼び出し先: `structuredClone()`, `surface.components.forEach()`, `this.#components.get()`, `this.#components.set()`, `this.#getChildren()`, `this.#getHeader()`
- 参照: `component.id`, `root.component`, `surface.dataModel`, `this.#components`, `this.#dataModel`, `this.#surface`

## A2UI.#hydrateList()
- 位置: L60-76
- 役割: List の title、description、groups をデータモデルから解決する
- 触るとき: リスト表示の値の解決方法を変えるとき
- 呼び出し先: `this.#resolveArray()`
- 条件付き依存: `if (component.title)` → `this.#resolveValue()`
- 条件付き依存: `if (component.description)` → `this.#resolveValue()`
- 参照: `component.description`, `component.groups`, `component.title`

## A2UI.#hydrateTimeline()
- 位置: L78-94
- 役割: Timeline の title、description、items を解決する
- 触るとき: タイムライン表示の値の解決方法を変えるとき
- 呼び出し先: `this.#resolveArray()`
- 条件付き依存: `if (component.title)` → `this.#resolveValue()`
- 条件付き依存: `if (component.description)` → `this.#resolveValue()`
- 参照: `component.description`, `component.items`, `component.title`

## A2UI.#hydrateCards()
- 位置: L96-104
- 役割: Cards の title と items を解決する
- 触るとき: カード表示の値の解決方法を変えるとき
- 呼び出し先: `this.#resolveArray()`
- 条件付き依存: `if (component.title)` → `this.#resolveValue()`
- 参照: `component.items`, `component.title`

## A2UI.#hydrateRankedTable()
- 位置: L106-122
- 役割: RankedTable の title、description、rows を解決する
- 触るとき: ランキング表の値の解決方法を変えるとき
- 呼び出し先: `this.#resolveArray()`
- 条件付き依存: `if (component.title)` → `this.#resolveValue()`
- 条件付き依存: `if (component.description)` → `this.#resolveValue()`
- 参照: `component.description`, `component.rows`, `component.title`

## A2UI.#hydrateTextBlock()
- 位置: L124-138
- 役割: TextBlock の lead と paragraphs を解決する
- 触るとき: 本文ブロックの値の解決方法を変えるとき
- 条件付き依存: `if (component.lead)` → `this.#resolveValue()`
- 条件付き依存: `if (component.paragraphs)` → `this.#resolveArray()`
- 参照: `component.lead`, `component.paragraphs`

## A2UI.#hydrateHighlights()
- 位置: L140-153
- 役割: Highlights の title を解決し、各項目を #hydrateHighlightItem で変換する
- 触るとき: ハイライト表示の項目の扱いを変えるとき
- 呼び出し先: `this.#hydrateHighlightItem()`, `this.#resolveArray()`, `this.#resolveValue()`
- 参照: `component.items`, `component.title`

## A2UI.#getHeader()
- 位置: L155-179
- 役割: root の header を解決して、ヘッダーをページの先頭に積む
- 触るとき: ページ先頭の見出し(eyebrow、title、subhead、参照)の扱いを変えるとき
- 呼び出し先: `page.children.push()`, `this.#components.get()`, `this.#components.has()`
- 条件付き依存: `if (header.eyebrow)` → `this.#resolveValue()`
- 条件付き依存: `if (header.title)` → `this.#resolveValue()`
- 条件付き依存: `if (header.subhead)` → `this.#resolveValue()`
- 条件付き依存: `if (header.references)` → `this.#hydrateSourceLinks()`
- 参照: `header.eyebrow`, `header.references`, `header.subhead`, `header.title`, `root.header`

## A2UI.#hydrateSourceLinks()
- 位置: L181-191
- 役割: 参照リンクの title と items を解決する
- 触るとき: 出典リンクの表示内容を変えるとき
- 条件付き依存: `if (sourceLinks.title)` → `this.#resolveValue()`
- 条件付き依存: `if (sourceLinks.items)` → `this.#resolveArray()`
- 参照: `sourceLinks.items`, `sourceLinks.title`

## A2UI.#getChildren()
- 位置: L193-230
- 役割: children が配列なら各子を、データパス指定なら配列の要素ごとに複製して変換し、ページに積む
- 触るとき: 子要素の並びや、データから繰り返し生成する仕組みを変えるとき
- 呼び出し先: `Array.isArray()`, `page.children.push()`, `structuredClone()`, `this.#components.get()`, `this.#components.has()`, `this.#hydrateComponent()`, `this.#resolvePath()`
- 条件付き依存: `if (Array.isArray(root.children))` → `this.#components.has()`
- 条件付き依存: `if (Array.isArray(root.children))` → `this.#components.get()`
- 条件付き依存: `if (Array.isArray(root.children))` → `page.children.push()`
- 条件付き依存: `if (Array.isArray(root.children))` → `this.#hydrateComponent()`
- 参照: `root.children`

## A2UI.#hydrateComponent()
- 位置: L232-239
- 役割: コンポーネント種別に登録された変換関数があればそれを通し、無ければそのまま返す
- 触るとき: 種別ごとの変換の振り分けを追うとき
- 呼び出し先: `this.#hydrators.get()`
- 条件付き依存: `if (typeof hydrator === "function")` → `hydrator()`
- 参照: `component.component`

## A2UI.#resolveValue()
- 位置: L241-255
- 役割: {path} 指定ならデータモデルから値を取り、それ以外は値をそのまま返す
- 触るとき: JSON 内の値参照の書式や既定値の扱いを変えるとき
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if ( typeof target === "object" && !Array.isArray(target) && typeof target.path === "string" )` → `this.#resolvePath()`
- 参照: `target.path`

## A2UI.#resolveArray()
- 位置: L257-269
- 役割: 値を解決して配列でなければ既定値を返し、必要なら項目ごとに変換する
- 触るとき: 配列項目の変換を追加するとき、配列でない値の扱いを調べるとき
- 呼び出し先: `Array.isArray()`, `this.#resolveValue()`, `value.map()`

## A2UI.#hydrateHighlightItem()
- 位置: L271-280
- 役割: ハイライト項目の sources を参照リンクとして解決する
- 触るとき: ハイライト項目の出典の扱いを変えるとき
- 条件付き依存: `if (highlightItem.sources)` → `this.#hydrateSourceLinks()`
- 参照: `highlightItem.sources`

## A2UI.#resolvePath()
- 位置: L282-306
- 役割: スラッシュ区切りのパスを辿ってデータを取り、~1 と ~0 のエスケープを戻す(/ で始まれば全体、それ以外は現在の項目)
- 触るとき: データパスの書式や解決範囲(絶対パスと相対パス)を変えるとき、値が取れない問題を調べるとき
- 呼び出し先: `fieldPath.shift()`, `key.replace()`, `key.replace(/~1/g, "/").replace()`, `path.split()`, `path.startsWith()`
- 条件付き依存: `if (absolutePath)` → `fieldPath.shift()`
- 参照: `fieldPath.length`, `this.#dataModel`
