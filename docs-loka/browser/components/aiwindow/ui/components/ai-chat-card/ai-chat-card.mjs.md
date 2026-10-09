# browser/components/aiwindow/ui/components/ai-chat-card/ai-chat-card.mjs

source: browser/components/aiwindow/ui/components/ai-chat-card/ai-chat-card.mjs
source-hash: cd4db10c925f701c6c89359c9549de5a2ab1401a
lines: 226

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AIChatCard.domain()
- 位置: L25-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `this.url`, `url?.hostname`

## AIChatCard.willUpdate()
- 位置: L30-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changed.has()`
- 参照: `this.thumbnailError`

## AIChatCard.renderImage()
- 位置: L36-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderFallback()`
- 条件付き依存: `if (this.thumbnailError)` → `this.renderFallback()`
- 条件付き依存: `if (this.thumbnail)` → `html()`
- 条件付き依存: `if (this.favicon)` → `html()`
- 参照: `e.target.src`, `this.favicon`, `this.thumbnail`, `this.thumbnailError`

## AIChatCard.renderFavicon()
- 位置: L75-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `e.target.src`, `this.favicon`

## AIChatCard.render()
- 位置: L86-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.renderFavicon()`, `this.renderImage()`
- 参照: `this.domain`, `this.timestamp`, `this.title`, `this.url`

## AIChatCard.renderFallback()
- 位置: L110-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
