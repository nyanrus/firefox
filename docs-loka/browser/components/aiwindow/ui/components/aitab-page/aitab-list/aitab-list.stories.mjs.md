# browser/components/aiwindow/ui/components/aitab-page/aitab-list/aitab-list.stories.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-list/aitab-list.stories.mjs
source-hash: aaac2dd83fd9ce92c8465ddea46c899dac7766bc
lines: 145

## <module>
- 役割: aitab-list の Storybook 定義。グループ付きの例データを持つ
- 呼び出し先: `KANAZAWA_GROUPS.slice()`, `KANAZAWA_GROUPS.slice(0, 2).map()`, `Template.bind()`, `html()`, `story()`

## Template()
- 位置: L53-60
- 役割: title・description・groups・layout を aitab-list に渡して描画する
- 触るとき: Storybook の全例に共通する属性の渡し方を変えるとき。
- 呼び出し先: `html()`
