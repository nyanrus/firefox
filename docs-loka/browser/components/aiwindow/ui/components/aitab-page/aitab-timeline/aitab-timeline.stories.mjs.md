# browser/components/aiwindow/ui/components/aitab-page/aitab-timeline/aitab-timeline.stories.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-timeline/aitab-timeline.stories.mjs
source-hash: cfded886617658741b0df4ab4fc07eb341f069a1
lines: 99

## <module>
- 役割: aitab-timeline の Storybook 定義。日付つきの例データを持つ
- 呼び出し先: `KANAZAWA_ITEMS.slice()`, `Template.bind()`, `html()`, `story()`

## Template()
- 位置: L56-62
- 役割: title・description・items を aitab-timeline に渡して描画する
- 触るとき: Storybook の全例に共通する渡し方を変えるとき。
- 呼び出し先: `html()`
