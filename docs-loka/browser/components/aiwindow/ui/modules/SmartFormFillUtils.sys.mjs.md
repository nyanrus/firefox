# browser/components/aiwindow/ui/modules/SmartFormFillUtils.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillUtils.sys.mjs
source-hash: a2af5c8ddf9338bc889622d6a766e204d5307895
lines: 169

## <module>
- 役割: (未記入)

## SmartFormFillUtils.iterateNodes()
- 位置: L38-70
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!next)` → `this.shouldStopIterating()`
- 条件付き依存: `if (filter)` → `filter()`
- 条件付き依存: `if (!(!next))` → `this.shouldStopIterating()`
- 参照: `Node.ELEMENT_NODE`, `child.firstChild`, `child.lastChild`, `child.nodeType`, `element.nextSibling`, `element.parentNode`, `element.previousSibling`

## SmartFormFillUtils.shouldStopIterating()
- 位置: L80-95
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `element.localName`

## SmartFormFillUtils.clearCache()
- 位置: L100-103
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#mappedTextForward`, `this.#mappedTextReverse`

## SmartFormFillUtils.findNearbyText()
- 位置: L114-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cache.has()`, `cache.set()`, `this.iterateNodes()`, `txt.replace()`, `txt.replace(/\s{2,}/g, " ").trim()`
- 条件付き依存: `if (cache.has(element))` → `cache.get()`
- 参照: `current.nodeValue`, `this.#mappedTextForward`, `this.#mappedTextReverse`

## returnTextNode()
- 位置: L135-148
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Node.ELEMENT_NODE`, `Node.TEXT_NODE`, `node.localName`, `node.nodeType`, `txt.length`
