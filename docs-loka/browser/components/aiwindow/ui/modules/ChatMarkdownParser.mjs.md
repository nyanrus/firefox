# browser/components/aiwindow/ui/modules/ChatMarkdownParser.mjs

source: browser/components/aiwindow/ui/modules/ChatMarkdownParser.mjs
source-hash: c5f1cc2c48a56eab037921339fb9ba9da4bb433e
lines: 125

## <module>
- 役割: (未記入)
- 呼び出し先: `MarkdownIt()`, `Object.entries()`

## md.renderer.rules[`${element}_open`]()
- 位置: L26-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...dataAttributes] .map()`, `[...dataAttributes] .map(([key, value]) => `${key}="${md.utils.escapeHtml(value)}"`) .join()`, `md.utils.escapeHtml()`, `renderer.renderToken()`
- 条件付き依存: `if (map)` → `dataAttributes.set()`
- 条件付き依存: `if (map)` → `JSON.stringify()`

## md.renderer.rules[`${element}_close`]()
- 位置: L45-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `renderer.renderToken()`

## hasDestination()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `token?.attrGet()`, `token?.attrGet("href")?.trim()`

## md.renderer.rules.link_open()
- 位置: L62-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasDestination()`, `renderer.renderToken()`

## md.renderer.rules.link_close()
- 位置: L67-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasDestination()`, `renderer.renderToken()`
- 参照: `tokens[i].type`

## parseMarkdown()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `md.render()`

## parseMarkdownBlocks()
- 位置: L101-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blocks.push()`, `md.parse()`, `md.renderer.render()`, `tokens.slice()`
- 参照: `md.options`, `tokens.length`, `tokens[end].nesting`, `tokens[start].nesting`
