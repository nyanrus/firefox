# browser/components/aiwindow/ui/components/aitab-highlights/aitab-highlights.mjs

source: browser/components/aiwindow/ui/components/aitab-highlights/aitab-highlights.mjs
source-hash: b7a1304d60b77b7d62104b30d5a8a440e0536615
lines: 122

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITabHighlights.constructor()
- 位置: L36-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.items`, `this.title`

## AITabHighlights.#renderSource()
- 位置: L42-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `source.favicon`, `source.title`, `url.hostname`, `url.href`

## AITabHighlights.#renderSources()
- 位置: L53-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(sources?.items ?? []) .map()`, `(sources?.items ?? []) .map(source => ({ source, url: httpUrl(source?.href) })) .filter()`, `html()`, `httpUrl()`, `links.map()`, `this.#renderSource()`
- 参照: `link.url`, `links.length`, `source?.href`, `sources?.items`

## AITabHighlights.#renderItem()
- 位置: L65-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderSources()`
- 参照: `item.body`, `item.eyebrow`, `item.sources`, `item.title`

## AITabHighlights.#renderList()
- 位置: L86-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.items ?? []).filter()`, `html()`, `items.map()`, `this.#renderItem()`
- 参照: `items.length`, `this.items`, `this.title`

## AITabHighlights.render()
- 位置: L99-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderList()`
- 参照: `this.title`
