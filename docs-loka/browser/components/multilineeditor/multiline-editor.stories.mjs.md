# browser/components/multilineeditor/multiline-editor.stories.mjs

source: browser/components/multilineeditor/multiline-editor.stories.mjs
source-hash: 10fa12bf023330409d58855596b55b9c3d56e9ea
lines: 159

## <module>
- 役割: (未記入)
- 呼び出し先: `MentionsTemplate.bind()`, `Template.bind()`, `createMentionsPlugin()`, `customElements.define()`

## Template()
- 位置: L25-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## toDOM()
- 位置: L54-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toDOM()`
- 参照: `node.attrs.label`

## onEnter()
- 位置: L55-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelList.show()`, `this.#createVirtualAnchor()`, `this.shadowRoot.querySelector()`
- 参照: `this.range`

## onChange()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.range`

## onExit()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector("panel-list").hide()`

## MultilineEditorWithMentions.constructor()
- 位置: L68-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.placeholder`

## MultilineEditorWithMentions.#createVirtualAnchor()
- 位置: L74-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `view.coordsAtPos()`
- 参照: `range.from`, `range.to`

## getBoundingClientRect()
- 位置: L78-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `coordsFrom.left`, `coordsFrom.top`, `coordsTo.bottom`, `coordsTo.right`

## setAttribute()
- 位置: L88-88
- 役割: (未記入)
- 触るとき: (未記入)

## getAttribute()
- 位置: L89-89
- 役割: (未記入)
- 触るとき: (未記入)

## hasAttribute()
- 位置: L90-90
- 役割: (未記入)
- 触るとき: (未記入)

## MultilineEditorWithMentions.handlePanelClick()
- 位置: L94-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.closest()`, `this.mentionsPlugin.mentions.insert()`
- 参照: `panelItem.dataset.id`, `panelItem.textContent`, `this.range.from`, `this.range.to`

## MultilineEditorWithMentions.render()
- 位置: L107-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.suggestions.map()`
- 参照: `item.id`, `item.label`, `this.handlePanelClick`, `this.mentionsPlugin`, `this.placeholder`

## MentionsTemplate()
- 位置: L130-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## toDOM()
- 位置: L145-151
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `node.attrs.label`
