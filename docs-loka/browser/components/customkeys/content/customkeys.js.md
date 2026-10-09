# browser/components/customkeys/content/customkeys.js

source: browser/components/customkeys/content/customkeys.js
source-hash: 0dff9a75e2ffdcdb7e3e074195ea6707e770b492
lines: 400

## <module>
- 役割: (未記入)
- 呼び出し先: `Glean.browserCustomkeys.opened.add()`, `RPMAddMessageListener()`, `buildTable()`, `customElements.whenDefined()`, `customElements.whenDefined("customkeys-sidebar").then()`, `document.getElementById()`, `document.getElementById("resetAll").addEventListener()`, `document.getElementById("search").addEventListener()`, `document.querySelector()`, `table.addEventListener()`

## notifyUpdate()
- 位置: L7-9
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.dispatchEvent()`

## buildTable()
- 位置: async L11-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `boxGroup.append()`, `buttonChange.setAttribute()`, `buttonClear.setAttribute()`, `buttonReset.setAttribute()`, `category.startsWith()`, `categoryCard.append()`, `document.createElement()`, `document.l10n.formatValue()`, `inputNewKey.setAttribute()`, `key.title.startsWith()`, `keyActions.append()`, `keyContent.append()`, `keyLabelContainer.append()`, `notifyUpdate()`, `row.append()`, `table.append()`, `table.querySelector()`, `updateKey()`
- 条件付き依存: `if (category.startsWith("customkeys-"))` → `categoryCard.setAttribute()`
- 条件付き依存: `if (key.title.startsWith("customkeys-"))` → `document.l10n.formatValue()`
- 条件付き依存: `if (key.internal)` → `row.classList.add()`
- 条件付き依存: `if (key.internal)` → `keyDescription.setAttribute()`
- 条件付き依存: `if (!key.shortcut)` → `inputCurrentKey.setAttribute()`
- 参照: `buttonChange.className`, `buttonChange.iconSrc`, `buttonChange.type`, `buttonClear.className`, `buttonClear.iconSrc`, `buttonClear.type`, `buttonReset.className`, `buttonReset.iconSrc`, `buttonReset.type`, `categoryCard.className`, `categoryCard.heading`, `categoryCard.headingLevel`, `categoryCard.type`, `inputCurrentKey.ariaLabel`, `inputCurrentKey.className`, `inputCurrentKey.readonly`, `inputCurrentKey.value`, `inputNewKey.className`, `key.internal`, `key.shortcut`, `key.title`, `keyActions.className`, `keyContent.className`, `keyDescription.className`, `keyLabel.className`, `keyLabel.textContent`, `keyLabelContainer.className`, `row.ariaLabelledByElements`, `row.className`, `row.dataset.id`, `row.dataset.label`, `row.role`, `table.querySelector("moz-card").expanded`

## updateKey()
- 位置: L139-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.classList.toggle()`, `row.querySelector()`
- 条件付き依存: `if (!input.value)` → `input.setAttribute()`
- 条件付き依存: `if (!(!input.value))` → `input.removeAttribute()`
- 参照: `data.isCustomized`, `data.shortcut`, `input.value`

## maybeHandleConflict()
- 位置: async L153-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendQuery()`, `document.l10n.formatValues()`, `row.classList.contains()`, `row.querySelector()`, `table.querySelectorAll()`, `updateKey()`
- 条件付き依存: `if (row.classList.contains("internal"))` → `document.l10n.formatValues()`
- 条件付き依存: `if (row.classList.contains("internal"))` → `RPMSendQuery()`
- 参照: `data.id`, `data.shortcut`, `row.dataset.id`, `row.dataset.label`, `row.querySelector(".currentShortcut").value`

## onAction()
- 位置: async L207-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if (event.target.className == "reset")` → `Glean.browserCustomkeys.actions.reset.add()`
- 条件付き依存: `if (event.target.className == "reset")` → `RPMSendQuery()`
- 条件付き依存: `if (event.target.className == "reset")` → `maybeHandleConflict()`
- 条件付き依存: `if (!data.shortcut || (await maybeHandleConflict(data)))` → `RPMSendQuery()`
- 条件付き依存: `if (!data.shortcut || (await maybeHandleConflict(data)))` → `updateKey()`
- 条件付き依存: `if (newData.shortcut)` → `row.querySelector(".clear").focus()`
- 条件付き依存: `if (newData.shortcut)` → `row.querySelector()`
- 条件付き依存: `if (!(newData.shortcut))` → `row.querySelector(".change").focus()`
- 条件付き依存: `if (!(newData.shortcut))` → `row.querySelector()`
- 条件付き依存: `if (!data.shortcut || (await maybeHandleConflict(data)))` → `notifyUpdate()`
- 条件付き依存: `if (event.target.className == "change")` → `Glean.browserCustomkeys.actions.change.add()`
- 条件付き依存: `if (event.target.className == "change")` → `row.classList.add()`
- 条件付き依存: `if (event.target.className == "change")` → `RPMSendAsyncMessage()`
- 条件付き依存: `if (event.target.className == "change")` → `row.querySelector(".newKey").focus()`
- 条件付き依存: `if (event.target.className == "change")` → `row.querySelector()`
- 条件付き依存: `if (event.target.className == "clear")` → `Glean.browserCustomkeys.actions.clear.add()`
- 条件付き依存: `if (event.target.className == "clear")` → `RPMSendQuery()`
- 条件付き依存: `if (event.target.className == "clear")` → `updateKey()`
- 条件付き依存: `if (event.target.className == "clear")` → `row.querySelector(".reset").focus()`
- 条件付き依存: `if (event.target.className == "clear")` → `row.querySelector()`
- 条件付き依存: `if (event.target.className == "clear")` → `notifyUpdate()`
- 参照: `data.shortcut`, `event.target.className`, `newData.shortcut`, `row.dataset.id`

## onKey()
- 位置: async L247-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `input.closest()`, `maybeHandleConflict()`, `notifyUpdate()`, `row.classList.remove()`, `row.querySelector()`, `row.querySelector(".change").focus()`
- 条件付き依存: `if (data.isModifier)` → `input.select()`
- 条件付き依存: `if (!data.isValid)` → `document.l10n.formatValue()`
- 条件付き依存: `if (!data.isValid)` → `input.select()`
- 条件付き依存: `if (await maybeHandleConflict(data))` → `RPMSendQuery()`
- 条件付き依存: `if (await maybeHandleConflict(data))` → `updateKey()`
- 参照: `data.id`, `data.isModifier`, `data.isValid`, `data.modifierString`, `document.activeElement`, `input.updateComplete`, `input.value`, `row.dataset.id`

## onFocusLost()
- 位置: L276-285
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target.className == "newKey")` → `RPMSendAsyncMessage()`
- 条件付き依存: `if (event.target.className == "newKey")` → `event.target.closest()`
- 条件付き依存: `if (event.target.className == "newKey")` → `row.classList.remove()`
- 参照: `event.target.className`, `event.target.value`

## clearSearchHighlights()
- 位置: L287-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `labelEl.querySelector()`, `row.querySelector()`
- 参照: `labelEl.textContent`, `row.dataset.label`

## applySearchHighlights()
- 位置: L294-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createDocumentFragment()`, `document.createElement()`, `frag.append()`, `labelEl.replaceChildren()`, `lower.indexOf()`, `row.querySelector()`, `text.slice()`, `text.toLowerCase()`
- 条件付き依存: `if (i > lastIndex)` → `frag.append()`
- 条件付き依存: `if (i > lastIndex)` → `text.slice()`
- 条件付き依存: `if (lastIndex < text.length)` → `frag.append()`
- 条件付き依存: `if (lastIndex < text.length)` → `text.slice()`
- 参照: `mark.className`, `mark.textContent`, `query.length`, `row.dataset.label`, `text.length`

## onSearchInput()
- 位置: L320-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `card.querySelector()`, `cards.entries()`, `event.target.value.toLowerCase()`, `notifyUpdate()`, `row.classList.toggle()`, `row.dataset.label.toLowerCase()`, `row.dataset.label.toLowerCase().includes()`, `table.querySelectorAll()`
- 条件付き依存: `if (query)` → `applySearchHighlights()`
- 条件付き依存: `if (!(query))` → `clearSearchHighlights()`
- 条件付き依存: `if (hasMatches)` → `card.classList.remove()`
- 条件付き依存: `if (!(hasMatches))` → `card.classList.add()`
- 参照: `card.expanded`, `card.hidden`, `row.hidden`

## onResetAll()
- 位置: async L353-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserCustomkeys.actions.reset_all.add()`, `RPMSendQuery()`, `document.l10n.formatValues()`, `notifyUpdate()`, `table.querySelectorAll()`
- 条件付き依存: `if (data)` → `updateKey()`
- 参照: `row.dataset.id`
