# browser/components/aiwindow/ui/components/tab-group-icon/tab-group-icon.stories.mjs

source: browser/components/aiwindow/ui/components/tab-group-icon/tab-group-icon.stories.mjs
source-hash: c6d0a79a0862dd5abaee9feeb0597d6d8b06079c
lines: 80

## <module>
- 役割: tab-group-icon の Storybook ストーリー(既定・全色・サイズ指定)を定義する
- 呼び出し先: `Template.bind()`, `html()`

## Template()
- 位置: L39-42
- 役割: label と color を渡して tab-group-icon を 1 つ描く
- 触るとき: ストーリーの既定の引数や描画方法を変えるとき
- 呼び出し先: `html()`

## AllColors()
- 位置: L50-68
- 役割: 全色の tab-group-icon を並べて描く
- 触るとき: 色トークンを追加・変更した後に全色を目視確認するとき
- 呼び出し先: `[ "blue", "cyan", "gray", "green", "orange", "pink", "purple", "red", "yellow", ].map()`, `html()`

## Sized()
- 位置: L72-79
- 役割: --tab-group-icon-size と --tab-group-icon-font-size を上書きした大きいアイコンを描く
- 触るとき: サイズ用の CSS 変数の使い方を確認するとき
- 呼び出し先: `html()`
