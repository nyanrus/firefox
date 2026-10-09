# browser/components/aiwindow/ui/components/aitab-page/aitab-text-block/aitab-text-block.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-text-block/aitab-text-block.mjs
source-hash: 18e175dff115e41f5781906b792566728ec0348e
lines: 79

## <module>
- 役割: AI Tab ページの本文ブロック aitab-text-block を定義する
- 呼び出し先: `customElements.define()`

## AITextBlock.constructor()
- 位置: L25-30
- 役割: heading を空、paragraphs と references を空配列にする
- 触るとき: 文章ブロックの既定値を変えるとき、値が無い時の表示を見直すとき。
- 呼び出し先: `super()`
- 参照: `this.heading`, `this.paragraphs`, `this.references`

## AITextBlock.#renderReferences()
- 位置: L32-51
- 役割: 参照元を ai-website-chip として段落の後に並べる
- 触るとき: 参照元チップの表示名（title が無ければ href）やアイコンの扱いを変えるとき。
- 呼び出し先: `html()`, `this.references.map()`
- 参照: `chip.favicon`, `chip.href`, `chip.title`, `this.references.length`

## AITextBlock.render()
- 位置: L53-75
- 役割: 見出しと段落を並べ、参照元があれば chip 列を添える
- 触るとき: 段落の描画方法や見出しの位置を変えるとき。
- 呼び出し先: `html()`, `this.#renderReferences()`, `this.paragraphs.map()`
- 参照: `this.heading`
