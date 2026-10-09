# browser/components/aiwindow/ui/components/aitab-table/aitab-table.stories.mjs

source: browser/components/aiwindow/ui/components/aitab-table/aitab-table.stories.mjs
source-hash: 627e682d037b8062e22fbf478f330862e66f648b
lines: 182

## <module>
- 役割: aitab-table の Storybook 用ストーリーを定義し、宿泊・見積もりなど代表的な列構成の例を並べるモジュール。
- 呼び出し先: `STAY_COLUMNS.slice()`, `STAY_ROWS.map()`, `Template.bind()`

## Template()
- 位置: L25-32
- 役割: heading・description・columns・rows を受け取り、aitab-table 要素に プロパティとして渡して描く。
- 触るとき: Storybook で表示する要素の属性の渡し方を変えるとき、または新しいプロパティを表に渡すストーリーを足すとき。
- 呼び出し先: `html()`
