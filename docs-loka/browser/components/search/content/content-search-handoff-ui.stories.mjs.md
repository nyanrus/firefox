# browser/components/search/content/content-search-handoff-ui.stories.mjs

source: browser/components/search/content/content-search-handoff-ui.stories.mjs
source-hash: f0913e5e432de7843802a59676980bcab2640890
lines: 90

## <module>
- 役割: content-search-handoff-ui の Storybook ストーリー定義。Focused / Unfocused / Disabled の3状態を表示する。
- 呼び出し先: `Template.bind()`, `addEventListener()`, `e.target.dispatchEvent()`, `setTimeout()`, `window.MozXULElement.insertFTLIfNeeded()`

## Template()
- 位置: L51-72
- 役割: fakeFocus と disabled を受け取り、content-search-handoff-ui を幅720pxの検索バーに載せる lit テンプレート。
- 触るとき: ハンドオフ検索バーの見た目や属性を変えたとき、または Storybook で新しい状態を増やしたいとき。
- 呼び出し先: `html()`
