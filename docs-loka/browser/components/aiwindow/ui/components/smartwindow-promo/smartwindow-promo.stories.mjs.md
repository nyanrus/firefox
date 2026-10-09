# browser/components/aiwindow/ui/components/smartwindow-promo/smartwindow-promo.stories.mjs

source: browser/components/aiwindow/ui/components/smartwindow-promo/smartwindow-promo.stories.mjs
source-hash: 2cfd840be828de2322e63cdbbafceed8c271363d
lines: 131

## <module>
- 役割: smartwindow-promo の Storybook 用ストーリーを定義し、画像・ボタン・閉じ方の組み合わせを並べるモジュール。
- 呼び出し先: `Template.bind()`

## Template()
- 位置: L43-83
- 役割: 設定値を message オブジェクトにまとめて smartwindow-promo に渡し、発火したイベントを console に出す。
- 触るとき: promo に渡す項目を増やすとき、またはストーリーで発火するイベントを確かめたいとき。
- 呼び出し先: `console.log()`, `html()`
