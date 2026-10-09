# browser/components/multilineeditor/plugins/MentionsPlugin.mjs

source: browser/components/multilineeditor/plugins/MentionsPlugin.mjs
source-hash: f39c254a3b651a6c8756c9b8aad5e3847f19e4e5
lines: 289

## <module>
- 役割: (未記入)

## Mentions.constructor()
- 位置: L33-38
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#editor`

## Mentions.insert()
- 位置: L51-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#buildInsertNodeTransaction()`, `tr.insertText()`, `view.dispatch()`, `view.focus()`
- 参照: `this.#editor.view`

## Mentions.insertNode()
- 位置: L71-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#buildInsertNodeTransaction()`, `view.dispatch()`
- 参照: `this.#editor.view`

## Mentions.#buildInsertNodeTransaction()
- 位置: L81-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `state.schema.nodes.mention.create()`, `state.tr.replaceRangeWith()`
- 参照: `mention.color`, `mention.id`, `mention.label`, `mention.type`, `this.#editor.view`

## Mentions.hasMention()
- 位置: L97-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.nodesBetween()`
- 参照: `doc.content.size`, `node.type`, `schema.nodes.mention`, `this.#editor.view`, `this.#hasMentionCacheDoc`, `this.#hasMentionCacheValue`

## Mentions.getAll()
- 位置: L123-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.descendants()`
- 条件付き依存: `if (node.type === schema.nodes.mention)` → `mentions.push()`
- 参照: `node.attrs.color`, `node.attrs.id`, `node.attrs.label`, `node.attrs.type`, `node.type`, `schema.nodes.mention`, `this.#editor.view`

## createMentionNodeSpec()
- 位置: L154-191
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `mentionNodeSpec.attrs`

## toDOM()
- 位置: L163-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toDOM()`
- 参照: `node.attrs.color`, `node.attrs.id`, `node.attrs.label`, `node.attrs.type`

## getAttrs()
- 位置: L182-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dom.getAttribute()`

## markdownSerializer()
- 位置: L198-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `state.esc()`, `state.write()`
- 条件付き依存: `if (node.attrs.type)` → `params.set()`
- 条件付き依存: `if (node.attrs.color)` → `params.set()`
- 参照: `node.attrs.color`, `node.attrs.id`, `node.attrs.label`, `node.attrs.type`

## createMentionsPlugin()
- 位置: L234-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createMentionNodeSpec()`, `markdownSerializer()`
- 参照: `node.attrs.label`

## mention()
- 位置: L256-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `document.createElement()`, `dom.classList.add()`, `nodeView()`

## update()
- 位置: L264-264
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `newNode.type.name`

## selectNode()
- 位置: L265-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dom.setAttribute()`

## deselectNode()
- 位置: L266-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dom.removeAttribute()`

## createPlugin()
- 位置: L274-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestionsPlugin()`, `triggerCharacter()`

## mentions()
- 位置: L284-286
- 役割: (未記入)
- 触るとき: (未記入)
