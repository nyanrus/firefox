# browser/components/preferences/dialogs/dohExceptions.js

source: browser/components/preferences/dialogs/dohExceptions.js
source-hash: 84c1d58ef93d7f69030cff485c9e19f6cce8066a
lines: 322

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `document.addEventListener()`, `gDoHExceptionsManager.init()`

## init()
- 位置: L14-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `document .getElementById()`, `document .getElementById("siteCol") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.getElementById("exceptionDialog").getButton()`, `this._list.addEventListener()`, `this._loadExceptions()`, `this._urlField.addEventListener()`, `this._urlField.focus()`, `this.buildExceptionList()`, `this.onApplyChanges()`, `this.onExceptionInput()`, `this.onExceptionKeyPress()`, `this.onListBoxKeyPress()`, `this.onListBoxSelect()`
- 参照: `document.getElementById("exceptionDialog").getButton("accept").disabled`, `event.target`, `this._btnAddException`, `this._list`, `this._prefLocked`, `this._removeAllButton`, `this._removeButton`, `this._urlField`, `this._urlField.disabled`
- XPCOM: `Services.prefs`

## handleEvent()
- 位置: L56-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addException()`, `this.onAllExceptionsDelete()`, `this.onExceptionDelete()`, `window.close()`
- 参照: `event.target.id`

## _loadExceptions()
- 位置: L74-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `exception.trim()`, `exceptionsFromPref.trim()`, `exceptionsFromPref.trim().split()`, `exceptionsFromPref?.trim()`
- 条件付き依存: `if (trimmed)` → `this._exceptions.add()`
- XPCOM: `Services.prefs`

## addException()
- 位置: L92-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.prompt.alert()`, `document.getElementById()`, `document.l10n .formatValues()`, `document.l10n .formatValues([ { id: "permissions-invalid-uri-title" }, { id: "permissions-invalid-uri-label" }, ]) .then()`, `inputValue.startsWith()`, `textbox.focus()`, `textbox.value.trim()`, `this._exceptions.has()`, `this._setRemoveButtonState()`, `this.onExceptionInput()`
- 条件付き依存: `if (!this._exceptions.has(domain))` → `this._exceptions.add()`
- 条件付き依存: `if (!this._exceptions.has(domain))` → `this.buildExceptionList()`
- 参照: `textbox.value`, `this._prefLocked`, `uri.host`
- XPCOM: `Services.io` / `Services.prompt`

## onExceptionInput()
- 位置: L133-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._btnAddException.disabled`, `this._urlField.value`

## onExceptionKeyPress()
- 位置: L137-144
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_RETURN)` → `this._btnAddException.click()`
- 条件付き依存: `if (document.activeElement == this._urlField)` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `document.activeElement`, `event.keyCode`, `this._urlField`

## onListBoxKeyPress()
- 位置: L146-163
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && event.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `this.onExceptionDelete()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_DELETE || (AppConstants.platform == "macosx" && event.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `event.preventDefault()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `event.keyCode`, `this._list.selectedItem`, `this._prefLocked`

## onListBoxSelect()
- 位置: L165-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setRemoveButtonState()`

## _removeExceptionFromList()
- 位置: L169-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementsByAttribute()`, `this._exceptions.delete()`
- 条件付き依存: `if (exceptionlistitem)` → `exceptionlistitem.remove()`

## onExceptionDelete()
- 位置: L180-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `richlistitem.getAttribute()`, `this._removeExceptionFromList()`, `this._setRemoveButtonState()`
- 参照: `this._list.selectedItem`

## onAllExceptionsDelete()
- 位置: L189-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._exceptions.values()`, `this._removeExceptionFromList()`, `this._setRemoveButtonState()`

## _createExceptionListItem()
- 位置: L197-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `hbox.appendChild()`, `hbox.setAttribute()`, `richlistitem.appendChild()`, `richlistitem.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `website.setAttribute()`

## _sortExceptions()
- 位置: L216-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `c.removeAttribute()`, `cols.forEach()`, `column.setAttribute()`, `frag.appendChild()`, `frag.querySelectorAll()`, `items.forEach()`, `list.previousElementSibling.querySelectorAll()`
- 条件付き依存: `if (!column)` → `document.querySelector()`
- 条件付き依存: `if (!column)` → `column.getAttribute()`
- 条件付き依存: `if (!(!column))` → `column.getAttribute()`
- 条件付き依存: `if (sortDirection === "descending")` → `items.sort()`
- 条件付き依存: `if (sortDirection === "descending")` → `sortFunc()`
- 条件付き依存: `if (!(sortDirection === "descending"))` → `items.sort()`
- 参照: `Services.intl.Collator`
- XPCOM: `Services.intl`

## sortFunc()
- 位置: L229-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.getAttribute()`, `b.getAttribute()`, `comp.compare()`

## _setRemoveButtonState()
- 位置: L258-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._list.querySelectorAll()`
- 参照: `disabledItems.length`, `this._list`, `this._list.itemCount`, `this._list.selectedIndex`, `this._prefLocked`, `this._removeAllButton.disabled`, `this._removeButton.disabled`

## onApplyChanges()
- 位置: L280-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Services.prefs.setStringPref()`, `exceptions.join()`
- 条件付き依存: `if (this._exceptions.size == 0)` → `Services.prefs.setStringPref()`
- 参照: `this._exceptions`, `this._exceptions.size`
- XPCOM: `Services.prefs`

## buildExceptionList()
- 位置: L295-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `document.createDocumentFragment()`, `frag.appendChild()`, `item.remove()`, `this._createExceptionListItem()`, `this._exceptions.values()`, `this._list.appendChild()`, `this._list.querySelectorAll()`, `this._setRemoveButtonState()`, `this._sortExceptions()`
- 参照: `this._list`
