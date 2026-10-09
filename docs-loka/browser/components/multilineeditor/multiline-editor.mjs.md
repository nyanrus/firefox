# browser/components/multilineeditor/multiline-editor.mjs

source: browser/components/multilineeditor/multiline-editor.mjs
source-hash: d4d442dcaac3b7cd4ec61956b955f820f997468f
lines: 1186

## <module>
- 役割: (未記入)
- 呼び出し先: `basicSchema.spec.nodes.get()`, `crypto.randomUUID()`, `customElements.define()`

## generatePlaceholderKeyframeStyles()
- 位置: L27-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `css()`

## MultilineEditor.constructor()
- 位置: L160-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `historyPlugin()`, `keymap()`, `super()`, `this.#createPlaceholderPlugin()`
- 条件付き依存: `if (document.contentType === "application/xhtml+xml")` → `plugins.push()`
- 条件付き依存: `if (document.contentType === "application/xhtml+xml")` → `this.#createCleanupOrphanedBreaksPlugin()`
- 参照: `document.contentType`, `this.#placeholderPlugin`, `this.#plugins`, `this.maxLength`, `this.placeholder`, `this.placeholderHints`, `this.plugins`, `this.readOnly`, `this.showPlaceholderAnimation`

## Enter()
- 位置: L173-173
- 役割: (未記入)
- 触るとき: (未記入)

## "Shift-Enter"()
- 位置: L174-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#insertParagraph()`

## MultilineEditor.view()
- 位置: L196-198
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#view`

## MultilineEditor.composing()
- 位置: L205-207
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#view?.composing`

## MultilineEditor.value()
- 位置: L214-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.textBetween()`, `this.#markdownSerializer.serialize()`
- 参照: `doc.content.size`, `this.#markdownSerializer`, `this.#pendingValue`, `this.#valueCacheDoc`, `this.#valueCacheStr`, `this.#view`, `this.#view.state.doc`

## MultilineEditor.value()
- 位置: L234-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TextSelection.between()`, `state.tr.replaceWith()`, `this.#dispatchSilently()`, `this.#posFromTextOffset()`, `this.#textToDoc()`, `tr.doc.resolve()`, `tr.setSelection()`
- 参照: `doc.content`, `state.doc.content.size`, `state.schema`, `this.#pendingValue`, `this.#view`, `this.#view.state`, `this.value`, `tr.doc`, `val.length`

## MultilineEditor.setRangeText()
- 位置: L266-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TextSelection.between()`, `state.tr.insertText()`, `this.#dispatchSilently()`, `this.#posFromTextOffset()`, `tr.doc.resolve()`, `tr.mapping.map()`, `tr.setSelection()`
- 参照: `state.doc`, `state.selection.from`, `state.selection.to`, `this.#view`, `this.#view.state`, `this.selectionEnd`, `this.selectionStart`

## MultilineEditor.#dispatchSilently()
- 位置: L314-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#view.dispatch()`, `tr.setMeta()`
- 参照: `this.#suppressInputEvent`

## MultilineEditor.plainText()
- 位置: L331-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#view.state.doc.textBetween()`
- 参照: `this.#pendingValue`, `this.#view`, `this.#view.state.doc.content.size`

## MultilineEditor.posToTextOffset()
- 位置: L350-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#textOffsetFromPos()`
- 参照: `this.#view?.state.doc`

## MultilineEditor.textOffsetToPos()
- 位置: L361-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#posFromTextOffset()`

## MultilineEditor.selectionStart()
- 位置: L370-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#textOffsetFromPos()`
- 参照: `this.#view`, `this.#view.state.selection.from`

## MultilineEditor.selectionStart()
- 位置: L382-384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setSelectionRange()`
- 参照: `this.selectionEnd`

## MultilineEditor.selectionEnd()
- 位置: L391-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#textOffsetFromPos()`
- 参照: `this.#view`, `this.#view.state.selection.to`

## MultilineEditor.selectionEnd()
- 位置: L403-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setSelectionRange()`
- 参照: `this.selectionStart`

## MultilineEditor.setSelectionRange()
- 位置: L413-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `TextSelection.between()`, `TextSelection.near()`, `doc.resolve()`, `this.#posFromTextOffsets()`, `this.#view.dispatch()`, `this.#view.state.tr.setSelection()`, `this.#view.state.tr.setSelection(selection).scrollIntoView()`
- 参照: `doc.content.size`, `this.#view`, `this.#view.state.doc`, `this.#view.state.selection.from`, `this.#view.state.selection.to`

## MultilineEditor.select()
- 位置: L450-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focus()`, `this.setSelectionRange()`
- 参照: `this.value.length`

## MultilineEditor.focus()
- 位置: L458-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.focus()`, `this.#view?.focus()`

## MultilineEditor.paste()
- 位置: L477-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dataTransfer.getData()`, `this.#view.focus()`
- 条件付き依存: `if (htmlData)` → `this.#view.pasteHTML()`
- 条件付き依存: `if (!(htmlData))` → `this.#view.pasteText()`
- 参照: `this.#view`

## MultilineEditor.connectedCallback()
- 位置: L497-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.getAttribute()`, `this.setAttribute()`
- 参照: `this.#innerRole`

## MultilineEditor.disconnectedCallback()
- 位置: L513-518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.#cancelPlaceholderAnimations()`, `this.#destroyView()`
- 参照: `this.#pendingValue`

## MultilineEditor.firstUpdated()
- 位置: L523-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#createView()`, `this.#updatePlaceholderKeyframeStyles()`

## MultilineEditor.updated()
- 位置: L533-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProps.has()`, `this.#applyForwardedAria()`
- 条件付き依存: `if ( changedProps.has("placeholder") || changedProps.has("placeholderHints") || changedProps.has("plugins") || changedProps.has("readOnly") )` → `this.#refreshView()`
- 条件付き依存: `if (this.showPlaceholderAnimation)` → `this.#resetPlaceholderAnimation()`
- 条件付き依存: `if (!(this.showPlaceholderAnimation))` → `this.#cancelPlaceholderAnimations()`
- 参照: `this.showPlaceholderAnimation`

## MultilineEditor.#buildSchema()
- 位置: L553-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.keys()`, `baseSchemaSpec.marks.append()`, `baseSchemaSpec.nodes.append()`
- 参照: `MultilineEditor.schema`, `MultilineEditor.schema.spec`, `Object.keys(marks).length`, `Object.keys(nodes).length`, `plugin.schemaExtension?.marks`, `plugin.schemaExtension?.nodes`, `this.plugins`

## MultilineEditor.#createMarkdownClipboardPlugin()
- 位置: L573-637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.keys()`, `filterBySchema()`, `filterParserTokens()`
- 参照: `Object.keys(parsers).length`, `Object.keys(serializers).length`, `defaultMarkdownParser.tokenizer`, `defaultMarkdownParser.tokens`, `defaultMarkdownSerializer.marks`, `defaultMarkdownSerializer.nodes`, `plugin.parseMarkdown`, `plugin.toMarkdown`, `schema.marks`, `schema.nodes`, `this.#markdownSerializer`, `this.plugins`

## filterParserTokens()
- 位置: L590-603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.values()`, `Object.values(spec).every()`
- 参照: `schema.marks`, `schema.nodes`

## filterBySchema()
- 位置: L605-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`

## clipboardTextParser()
- 位置: L633-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parser.parse()`
- 参照: `parser.parse(text)?.content`

## clipboardTextSerializer()
- 位置: L634-634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `serializer.serialize()`
- 参照: `slice.content`

## MultilineEditor.#createView()
- 位置: L639-699
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EditorState.create()`, `Object.assign()`, `event.stopPropagation()`, `plugin.createPlugin()`, `this.#buildSchema()`, `this.#createMarkdownClipboardPlugin()`, `this.#view.dom.addEventListener()`, `this.#viewAttributes()`, `this.plugins .map()`, `this.plugins .map(plugin => plugin.createPlugin?.(this)) .filter()`, `this.plugins.map()`, `this.plugins.map(plugin => plugin.nodeViews).filter()`, `this.renderRoot.querySelector()`
- 参照: `plugin.nodeViews`, `this.#dispatchTransaction`, `this.#pendingValue`, `this.#plugins`, `this.#view`, `this.value`

## editable()
- 位置: L663-663
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.readOnly`

## contextmenu()
- 位置: L666-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `view.dom.getRootNode()`
- 条件付き依存: `if (host && host != view.dom)` → `host.dispatchEvent()`
- 参照: `this.readOnly`, `view.dom`, `view.dom.getRootNode().host`

## MultilineEditor.#destroyView()
- 位置: L701-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#view?.destroy()`
- 参照: `this.#view`

## MultilineEditor.#dispatchTransaction()
- 位置: L706-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#view.state.apply()`, `this.#view.updateState()`
- 条件付き依存: `if ( tr.docChanged && this.maxLength > 0 && tr.doc.content.size > this.maxLength )` → `tr.doc.textBetween()`
- 条件付き依存: `if ( tr.docChanged && this.maxLength > 0 && tr.doc.content.size > this.maxLength )` → `newText.slice()`
- 条件付き依存: `if (newText.length > this.maxLength && truncated !== this.value)` → `this.#textToDoc()`
- 条件付き依存: `if (newText.length > this.maxLength && truncated !== this.value)` → `this.#view.state.tr .replaceWith(0, this.#view.state.doc.content.size, doc.content) .scrollIntoView()`
- 条件付き依存: `if (newText.length > this.maxLength && truncated !== this.value)` → `this.#view.state.tr .replaceWith()`
- 条件付き依存: `if (selectionChanged)` → `this.#dispatchSelectionChange()`
- 条件付き依存: `if (willDispatchInput)` → `step.slice?.content?.textBetween()`
- 条件付き依存: `if (willDispatchInput)` → `this.dispatchEvent()`
- 参照: `doc.content`, `newText.length`, `nextState.selection.from`, `nextState.selection.to`, `nextText.length`, `prevSelection.from`, `prevSelection.to`, `prevText.length`, `step.slice.content.size`, `this.#suppressInputEvent`, `this.#view`, `this.#view.state.doc.content.size`, `this.#view.state.schema`, `this.#view.state.selection`, `this.maxLength`, `this.value`, `tr.doc.content.size`, `tr.docChanged`, `tr.selectionSet`, `tr.steps`

## MultilineEditor.#dispatchSelectionChange()
- 位置: L771-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## MultilineEditor.#insertParagraph()
- 位置: L777-790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatch()`, `tr.mapping.map()`, `tr.split()`, `tr.split(tr.mapping.map($from.pos)).scrollIntoView()`
- 条件付き依存: `if (!state.selection.empty)` → `tr.deleteSelection()`
- 参照: `$from.pos`, `state.schema.nodes.paragraph`, `state.selection`, `state.selection.empty`, `state.tr`

## MultilineEditor.#createPlaceholderHints()
- 位置: L792-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `hintItem.style.setProperty()`, `hints.appendChild()`, `hints.setAttribute()`, `hints.style.setProperty()`, `placeholder.style.setProperty()`, `this.placeholderHints.entries()`
- 参照: `hintItem.textContent`, `hints.className`, `hints.id`, `placeholder.textContent`, `this.#instanceId`, `this.#placeholderVersion`, `this.placeholder`, `this.placeholderHints.length`

## MultilineEditor.#createPlaceholderPlugin()
- 位置: L827-862
- 役割: (未記入)
- 触るとき: (未記入)

## decorations()
- 位置: L830-859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Decoration.node()`, `DecorationSet.create()`
- 条件付き依存: `if (this.placeholderHints.length)` → `DecorationSet.create()`
- 条件付き依存: `if (this.placeholderHints.length)` → `Decoration.widget()`
- 条件付き依存: `if (this.placeholderHints.length)` → `this.#createPlaceholderHints()`
- 参照: `doc.childCount`, `doc.firstChild.content.size`, `doc.firstChild.isTextblock`, `doc.firstChild.nodeSize`, `this.#instanceId`, `this.#placeholderVersion`, `this.placeholder`, `this.placeholderHints.length`

## MultilineEditor.#createCleanupOrphanedBreaksPlugin()
- 位置: L873-913
- 役割: (未記入)
- 触るとき: (未記入)

## MultilineEditor.appendTransaction()
- 位置: L875-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nextNode.child()`, `nextState.doc.descendants()`, `transactions.some()`
- 条件付き依存: `if (nextNode.child(i).type.name === "hard_break")` → `prevState.doc.nodeAt()`
- 条件付き依存: `if (prevNode?.type.name === "paragraph" && prevNode.textContent)` → `tr.replaceWith()`
- 参照: `nextNode.child(i).type.name`, `nextNode.childCount`, `nextNode.content.size`, `nextNode.textContent`, `nextNode.type.name`, `nextState.tr`, `prevNode.textContent`, `prevNode?.type.name`, `tr.docChanged`

## MultilineEditor.#applyForwardedAria()
- 位置: L915-929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProps.has()`
- 条件付き依存: `if (this[prop] == null)` → `this.#view.dom.removeAttribute()`
- 条件付き依存: `if (!(this[prop] == null))` → `this.#view.dom.setAttribute()`
- 参照: `MultilineEditor.FORWARDED_ARIA`, `this.#view`

## MultilineEditor.#refreshView()
- 位置: L931-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePlaceholderKeyframeStyles()`, `this.#view.dispatch()`, `this.#view.setProps()`, `this.#viewAttributes()`
- 参照: `this.#placeholderVersion`, `this.#view`, `this.#view.state.tr`

## editable()
- 位置: L940-940
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.readOnly`

## MultilineEditor.#resetPlaceholderAnimation()
- 位置: L951-962
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.all(animations.map(animation => animation.ready)) .then()`, `animations.map()`, `this.#getPlaceholderAnimations()`
- 参照: `animation.currentTime`, `animation.ready`

## MultilineEditor.#cancelPlaceholderAnimations()
- 位置: L964-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `animation.cancel()`, `this.#getPlaceholderAnimations()`

## MultilineEditor.#getPlaceholderAnimations()
- 位置: L971-980
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...placeholderHints.querySelectorAll("li")].flatMap()`, `placeholderHint.getAnimations()`, `placeholderHints.querySelectorAll()`, `this.renderRoot.querySelector()`

## MultilineEditor.#updatePlaceholderKeyframeStyles()
- 位置: L982-994
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `generatePlaceholderKeyframeStyles()`, `this.#placeholderKeyframeStyles.replaceSync()`
- 条件付き依存: `if (!this.#placeholderKeyframeStyles)` → `this.renderRoot.adoptedStyleSheets.push()`
- 参照: `keyframeStyles.cssText`, `this.#placeholderKeyframeStyles`, `this.placeholderHints.length`

## MultilineEditor.#textToDoc()
- 位置: L996-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `schema.node()`, `schema.text()`, `text.split()`, `text.split("\n").map()`

## MultilineEditor.#textOffsetFromPos()
- 位置: L1004-1014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.textBetween()`
- 参照: `doc.textBetween(0, pos, blockSeparator, leafText).length`, `this.#view?.state.doc`

## MultilineEditor.#posFromTextOffsets()
- 位置: L1035-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `doc.descendants()`, `new Array(targets.length).fill()`, `offsets.map()`, `results.map()`
- 条件付き依存: `if (!doc)` → `offsets.map()`
- 条件付き依存: `if (paragraphCount > 0)` → `resolveReached()`
- 条件付き依存: `if (node.isText)` → `resolveReached()`
- 条件付き依存: `if (node.isLeaf)` → `resolveReached()`
- 参照: `doc.content.size`, `node.isLeaf`, `node.isText`, `node.nodeSize`, `node.text.length`, `node.type.name`, `targets.length`, `this.#view?.state.doc`

## resolveReached()
- 位置: L1046-1055
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (results[i] == -1 && targets[i] <= limit)` → `posAt()`
- 参照: `targets.length`

## MultilineEditor.#posFromTextOffset()
- 位置: L1095-1139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `doc.descendants()`, `this.#textLength()`
- 参照: `doc.content.size`, `node.isText`, `node.text.length`, `node.type.name`, `this.#view?.state.doc`

## MultilineEditor.#textLength()
- 位置: L1141-1146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.textBetween()`
- 参照: `doc.content.size`, `doc.textBetween(0, doc.content.size, "\n", "\n").length`

## MultilineEditor.#viewAttributes()
- 位置: L1148-1168
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `attrs.role`, `this.#innerRole`, `this.#instanceId`, `this.#placeholderVersion`, `this.placeholder`, `this.placeholderHints.length`, `this.readOnly`

## MultilineEditor.render()
- 位置: L1170-1182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
