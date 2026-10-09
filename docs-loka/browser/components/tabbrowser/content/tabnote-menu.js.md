# browser/components/tabbrowser/content/tabnote-menu.js

source: browser/components/tabbrowser/content/tabnote-menu.js
source-hash: 3466f21a4e060ed9a43b62f64b3f9eb0cc5fd689
lines: 312

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## MozTabbrowserTabNoteMenu.connectedCallback()
- 位置: L100-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.#cancelButton.addEventListener()`, `this.#deleteButton.addEventListener()`, `this.#deleteNote()`, `this.#noteField.addEventListener()`, `this.#panel.addEventListener()`, `this.#panel.hidePopup()`, `this.#saveButton.addEventListener()`, `this.appendChild()`, `this.initializeAttributeInheritance()`, `this.querySelector()`, `this.saveNote()`

## MozTabbrowserTabNoteMenu.on_keypress()
- 位置: L137-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel.hidePopup()`
- 条件付き依存: `if (!event.shiftKey && event.target === this.#noteField)` → `this.saveNote()`

## MozTabbrowserTabNoteMenu.on_input()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePanel()`

## MozTabbrowserTabNoteMenu.on_popuphidden()
- 位置: L159-163
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabNoteMenu.createMode()
- 位置: L165-167
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabNoteMenu.createMode()
- 位置: L169-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabLocalization.formatValueSync()`, `this.#panel.setAttribute()`

## MozTabbrowserTabNoteMenu.#panelPosition()
- 位置: L189-196
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabNoteMenu.#updatePanel()
- 位置: L198-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getComputedStyle()`, `parseFloat()`, `this.#noteField.value.trim()`
- 条件付き依存: `if (overflow != OverflowState.NONE)` → `this.#panel.setAttribute()`
- 条件付き依存: `if (overflow != OverflowState.NONE)` → `gBrowser.tabLocalization.formatValueSync()`
- 条件付き依存: `if (!(overflow != OverflowState.NONE))` → `this.#panel.removeAttribute()`

## MozTabbrowserTabNoteMenu.openPanel()
- 位置: L248-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabNotes.get()`, `TabNotes.get(tab).then()`, `TabNotes.isEligible()`, `this.#noteField.focus()`, `this.#panel.addEventListener()`, `this.#panel.openPopup()`, `this.#updatePanel()`

## MozTabbrowserTabNoteMenu.saveNote()
- 位置: L284-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabNotes.isEligible()`, `note.trim()`, `this.#panel.hidePopup()`
- 条件付き依存: `if ( TabNotes.isEligible(this.#currentTab) && note.trim().length && note.length <= OVERFLOW_MAX_THRESHOLD )` → `TabNotes.set()`

## MozTabbrowserTabNoteMenu.#deleteNote()
- 位置: L300-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabNotes.isEligible()`, `this.#panel.hidePopup()`
- 条件付き依存: `if (TabNotes.isEligible(this.#currentTab))` → `TabNotes.delete()`
