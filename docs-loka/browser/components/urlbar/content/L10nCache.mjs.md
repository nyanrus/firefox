# browser/components/urlbar/content/L10nCache.mjs

source: browser/components/urlbar/content/L10nCache.mjs
source-hash: 964d2058502dfdba8c2567107a513de6ee818ca8
lines: 431

## <module>
- 役割: (未記入)

## L10nCache.constructor()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.l10n`, `this.l10n`

## L10nCache.get()
- 位置: L105-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#argsKey()`, `this.#messagesByArgsById.get()`, `this.#messagesByArgsById.get(id)?.get()`

## L10nCache.add()
- 位置: async L120-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#update()`, `this.l10n.formatMessages()`
- 条件付き依存: `if (!messages?.[0])` → `console.error()`
- 条件付き依存: `if (messages[0].attributes)` → `messages[0].attributes.reduce()`
- 参照: `a.name`, `a.value`, `message.attributes`, `messages[0].attributes`, `messages[0].value`

## L10nCache.ensure()
- 位置: async L157-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.get()`
- 条件付き依存: `if (message)` → `this.#update()`
- 条件付き依存: `if (!(message))` → `this.add()`

## L10nCache.ensureAll()
- 位置: async L172-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `promises.push()`, `this.ensure()`

## L10nCache.delete()
- 位置: L191-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messagesByArgsById.get()`
- 条件付き依存: `if (messagesByArgs)` → `messagesByArgs.delete()`
- 条件付き依存: `if (messagesByArgs)` → `this.#argsKey()`
- 条件付き依存: `if (!messagesByArgs.size)` → `this.#messagesByArgsById.delete()`
- 参照: `messagesByArgs.size`

## L10nCache.clear()
- 位置: L204-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messagesByArgsById.clear()`

## L10nCache.size()
- 位置: L211-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#messagesByArgsById .values()`, `this.#messagesByArgsById .values() .reduce()`
- 参照: `messagesByArg.size`

## L10nCache.setElementL10n()
- 位置: L259-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.ownerDocument.l10n.setAttributes()`, `this.ensure()`, `this.get()`
- 条件付き依存: `if (message.attributes)` → `Object.entries()`
- 条件付き依存: `if (message.attributes)` → `element.setAttribute()`
- 条件付き依存: `if (!(!parseMarkup))` → `element.setHTML()`
- 条件付き依存: `if (!message && !attribute && argsHighlights)` → `element.ownerDocument.createElement()`
- 条件付き依存: `if (!message && !attribute && argsHighlights)` → `UrlbarShared.addTextContentWithHighlights()`
- 条件付き依存: `if (attribute)` → `element.setAttribute()`
- 条件付き依存: `if (!(attribute))` → `element.removeAttribute()`
- 参照: `element.textContent`, `message.attributes`, `message.value`, `span.innerHTML`

## L10nCache.removeElementL10n()
- 位置: L342-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.removeAttribute()`
- 条件付き依存: `if (attribute)` → `element.removeAttribute()`
- 参照: `element.textContent`

## L10nCache.#update()
- 位置: L384-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `messagesByArgs.delete()`, `messagesByArgs.set()`, `this.#argsKey()`, `this.#messagesByArgsById.get()`
- 条件付き依存: `if (!messagesByArgs)` → `this.#messagesByArgsById.set()`
- 条件付き依存: `if (messagesByArgs.size == this.#maxEntriesPerId)` → `messagesByArgs.delete()`
- 条件付き依存: `if (messagesByArgs.size == this.#maxEntriesPerId)` → `messagesByArgs.keys().next()`
- 条件付き依存: `if (messagesByArgs.size == this.#maxEntriesPerId)` → `messagesByArgs.keys()`
- 参照: `messagesByArgs.keys().next().value`, `messagesByArgs.size`, `this.#maxEntriesPerId`

## L10nCache.#argsKey()
- 位置: L420-429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.entries()`, `Object.entries(args ?? []) .sort()`, `Object.entries(args ?? []) .sort(([key1], [key2]) => key1.localeCompare(key2)) .map()`, `key1.localeCompare()`
