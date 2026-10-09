# browser/components/aiwindow/ui/components/ai-grouped-chip-container/ai-grouped-chip-container.stories.mjs

source: browser/components/aiwindow/ui/components/ai-grouped-chip-container/ai-grouped-chip-container.stories.mjs
source-hash: 8077ac8b808647146d5d4bb1211f21b1858af99c
lines: 57

## <module>
- 役割: ai-grouped-chip-container を Storybook で確認するためのストーリー(Default、WithTabGroup)を定義する。

## Default()
- 位置: L35-37
- 役割: URL の異なるチップ2件と重複する1件の計3件を渡して、通常の複数チップ表示を描画する。
- 触るとき: 複数チップの表示やパネルの見た目を確認したいとき。
- 呼び出し先: `html()`

## WithTabGroup()
- 位置: L40-56
- 役割: タブグループ1件と先頭2件を渡し、タブグループ用の色付きアイコンが出る表示を描画する。tab.tokens.css も読み込む。
- 触るとき: タブグループのアイコンの色や描画が崩れたときに、その見た目を確かめるとき。
- 呼び出し先: `chips.slice()`, `html()`
