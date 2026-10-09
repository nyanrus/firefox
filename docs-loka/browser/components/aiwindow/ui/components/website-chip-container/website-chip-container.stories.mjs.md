# browser/components/aiwindow/ui/components/website-chip-container/website-chip-container.stories.mjs

source: browser/components/aiwindow/ui/components/website-chip-container/website-chip-container.stories.mjs
source-hash: e1d2ab09acc1057be19977247c949ba9d4370501
lines: 89

## <module>
- 役割: website-chip-container の Storybook 用ストーリー(既定、自動はみ出し、グループ化など)を定義する
- 呼び出し先: `html()`, `story()`

## makeWebsites()
- 位置: L39-44
- 役割: 指定件数のダミーサイト(URL、ラベル、アイコン)を作る
- 触るとき: ストーリーの件数や見た目のサンプルを変えるとき
- 呼び出し先: `Array.from()`

## Default()
- 位置: L46-52
- 役割: 3 件の削除可能なチップを描く
- 触るとき: 既定の表示を確認するストーリーの内容を変えるとき
- 呼び出し先: `html()`, `makeWebsites()`

## AutoWidthOverflow()
- 位置: L54-72
- 役割: 幅を 500px で可変にした枠の中に 6 件を自動はみ出しで描く
- 触るとき: 幅に応じたはみ出し表示を確認するとき
- 呼び出し先: `html()`, `makeWebsites()`

## NoOverflow()
- 位置: L76-81
- 役割: 2 件だけを自動はみ出しで描き、はみ出しが出ない場合を確認する
- 触るとき: はみ出しボタンが出ない条件を確認するとき
- 呼び出し先: `html()`, `makeWebsites()`

## CountBasedGrouping()
- 位置: L83-88
- 役割: 6 件をグループ化を有効にして描き、件数によるグループ表示を確認する
- 触るとき: グループ表示の閾値や見た目を確認するとき
- 呼び出し先: `html()`, `makeWebsites()`
