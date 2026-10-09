# browser/components/aiwindow/ui/components/ai-sff-form-review/ai-sff-form-review.stories.mjs

source: browser/components/aiwindow/ui/components/ai-sff-form-review/ai-sff-form-review.stories.mjs
source-hash: 2e1683faed14f955790c235913a48b7af820ffc3
lines: 180

## <module>
- 役割: ai-sff-form-review の各状態(進行中、確認、完了、エラー)を Storybook で確認するためのストーリーと文言を定義する。
- 呼び出し先: `Array.from()`, `Object.values()`, `Template.bind()`

## Template()
- 位置: L116-128
- 役割: fields、state、errorType、filledFieldCount を渡して ai-sff-form-review を描画する共通テンプレート。
- 触るとき: 確認用ストーリーで別の状態や入力件数を試したいとき。
- 呼び出し先: `html()`
