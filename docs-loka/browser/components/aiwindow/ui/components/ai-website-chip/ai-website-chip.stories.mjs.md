# browser/components/aiwindow/ui/components/ai-website-chip/ai-website-chip.stories.mjs

source: browser/components/aiwindow/ui/components/ai-website-chip/ai-website-chip.stories.mjs
source-hash: 0f6b85e3088416259f4c7fd0a4cf1f5af02b4928
lines: 198

## <module>
- 役割: ai-website-chip を Storybook で確認するためのストーリー、引数の選択肢と文言を定義する。
- 呼び出し先: `Template.bind()`, `html()`

## Template()
- 位置: L66-87
- 役割: type、size、label、アイコン、href、タブグループ関連の値を渡して ai-website-chip を描画する共通テンプレート。タブグループ時は色のトークン CSS も読み込む。
- 触るとき: チップの新しい組み合わせを確認用に足すとき。
- 呼び出し先: `html()`

## InLineCollection()
- 位置: L103-112
- 役割: 文字ありと空の in-line チップを並べて表示する。
- 触るとき: 入力欄チップの並びや間隔を確かめたいとき。
- 呼び出し先: `html()`

## MixedCollection()
- 位置: L131-154
- 役割: in-line と context-chip(削除可・小サイズ含む)を混ぜて並べる。
- 触るとき: 種類が混ざったときの見た目を確かめたいとき。
- 呼び出し先: `html()`

## TabGroupColors()
- 位置: L173-197
- 役割: 全 9 色のタブグループのチップを並べ、色ごとの見た目を確認できるようにする。
- 触るとき: タブグループの色トークンを変えたとき、または色の見え方を確かめたいとき。
- 呼び出し先: `[ "blue", "cyan", "gray", "green", "orange", "pink", "purple", "red", "yellow", ].map()`, `html()`
