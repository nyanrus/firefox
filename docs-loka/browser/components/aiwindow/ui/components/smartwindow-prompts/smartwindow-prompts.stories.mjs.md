# browser/components/aiwindow/ui/components/smartwindow-prompts/smartwindow-prompts.stories.mjs

source: browser/components/aiwindow/ui/components/smartwindow-prompts/smartwindow-prompts.stories.mjs
source-hash: 1e60e68262c7bc3b4a328a9c95d8352adad6d49a
lines: 100

## <module>
- 役割: smartwindow-prompts の Storybook 用ストーリーを定義し、サイドバーとフルページ、アイコン付き、多数の項目の例を並べるモジュール。
- 呼び出し先: `Template.bind()`, `window.MozXULElement.insertFTLIfNeeded()`

## Template()
- 位置: L62-72
- 役割: mode・prompts・幅を smartwindow-prompts に渡して描き、選ばれたスターターを alert で表示する。
- 触るとき: スターターの例を増やすとき、または選択時の通知の確かめ方を変えるとき。
- 呼び出し先: `alert()`, `html()`
- 参照: `e.detail.text`, `e.detail.type`
