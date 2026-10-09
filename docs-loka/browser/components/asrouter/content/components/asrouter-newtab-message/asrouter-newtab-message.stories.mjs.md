# browser/components/asrouter/content/components/asrouter-newtab-message/asrouter-newtab-message.stories.mjs

source: browser/components/asrouter/content/components/asrouter-newtab-message/asrouter-newtab-message.stories.mjs
source-hash: 847ab9df10ee27b8bc71a85507a7469e5fc75521
lines: 157

## <module>
- 役割: asrouter-newtab-message 要素の Storybook 定義。各バリエーションの messageData を用意する。
- 呼び出し先: `Template.bind()`, `window.MozXULElement.insertFTLIfNeeded()`

## Template()
- 位置: L18-48
- 役割: messageData を受けて asrouter-newtab-message を描画し、各ハンドラを console.warn に置き換えたテンプレート。
- 触るとき: ストーリーの枠組みや、ハンドラの扱いを変えるとき。
- 呼び出し先: `console.warn()`, `html()`
