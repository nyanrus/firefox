# browser/components/aiwindow/ui/components/smartwindow-resume-card/smartwindow-resume-card.stories.mjs

source: browser/components/aiwindow/ui/components/smartwindow-resume-card/smartwindow-resume-card.stories.mjs
source-hash: d85bb0fb91c631392fe61924278449a2148ff358
lines: 84

## <module>
- 役割: smartwindow-resume-card の Storybook 用ストーリーを定義し、タブが多い場合や無い場合などの例を並べるモジュール。
- 呼び出し先: `Template.bind()`, `window.MozXULElement.insertFTLIfNeeded()`

## Template()
- 位置: L15-31
- 役割: content と journeyId を渡し、各イベントを alert で表示する幅340pxの枠の中に描く。
- 触るとき: 表示例の組み合わせを変えるとき、またはイベントの受け取り方を確かめたいとき。
- 呼び出し先: `alert()`, `html()`
- 参照: `e.detail.itemId`, `e.detail.journeyId`
