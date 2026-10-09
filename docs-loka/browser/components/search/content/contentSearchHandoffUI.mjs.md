# browser/components/search/content/contentSearchHandoffUI.mjs

source: browser/components/search/content/contentSearchHandoffUI.mjs
source-hash: e1d2a59ce886dc624b9c037bcd75a7fbdd1518ac
lines: 1347

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ContentSearchHandoffUIController.constructor()
- 位置: L17-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`, `window.addEventListener()`
- 参照: `this.#shadowRoot`, `this.#ui`, `this._engineIcon`, `this._isPrivateEngine`, `ui.shadowRoot`

## ContentSearchHandoffUIController.handleEvent()
- 位置: L28-33
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.detail.data`, `event.detail.type`

## ContentSearchHandoffUIController.defaultEngine()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._defaultEngine`

## ContentSearchHandoffUIController.doSearchHandoff()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`

## ContentSearchHandoffUIController._isAboutPrivateBrowsing()
- 位置: L44-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentSearchHandoffUIController.privateBrowsingRegex.test()`
- 参照: `document.location.href`

## ContentSearchHandoffUIController._onMsgEngine()
- 位置: L50-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateEngine()`
- 参照: `this._isPrivateEngine`

## ContentSearchHandoffUIController._onMsgCurrentEngine()
- 位置: L55-59
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._isPrivateEngine)` → `this._updateEngine()`
- 参照: `this._isPrivateEngine`

## ContentSearchHandoffUIController._onMsgCurrentPrivateEngine()
- 位置: L61-65
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._isPrivateEngine)` → `this._updateEngine()`
- 参照: `this._isPrivateEngine`

## ContentSearchHandoffUIController._onMsgHandoffSearchModePrefs()
- 位置: L67-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updatel10nIds()`
- 参照: `this._shouldHandOffToSearchMode`

## ContentSearchHandoffUIController._onMsgDisableSearch()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#ui.disabled`

## ContentSearchHandoffUIController._onMsgShowSearch()
- 位置: L76-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#ui.disabled`, `this.#ui.fakeFocus`

## ContentSearchHandoffUIController._updateEngine()
- 位置: L81-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.body.style.setProperty()`, `this._updatel10nIds()`
- 条件付き依存: `if (this._engineIcon)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (engine.iconData)` → `this._getFaviconURIFromIconData()`
- 参照: `engine.iconData`, `engine.isConfigEngine`, `this._defaultEngine`, `this._engineIcon`

## ContentSearchHandoffUIController._updatel10nIds()
- 位置: L104-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#shadowRoot.querySelector()`
- 条件付き依存: `if (!engine || this._shouldHandOffToSearchMode)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!engine.isConfigEngine)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(!engine.isConfigEngine))` → `document.l10n.setAttributes()`
- 参照: `engine.isConfigEngine`, `engine.name`, `this._defaultEngine`, `this._isAboutPrivateBrowsing`, `this._shouldHandOffToSearchMode`

## ContentSearchHandoffUIController._getFaviconURIFromIconData()
- 位置: L168-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.createObjectURL()`
- 参照: `data.icon`, `data.mimeType`

## ContentSearchHandoffUIController._sendMsg()
- 位置: L178-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchEvent()`

## ContentSearchUIController()
- 位置: L222-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tableParent.appendChild()`, `this._getSearchEngines()`, `this._getStrings()`, `this._hideSuggestions()`, `this._makeTable()`, `this.input.addEventListener()`, `this.input.setAttribute()`, `window.addEventListener()`
- 参照: `this._healthReportKey`, `this._idPrefix`, `this._isPrivateEngine`, `this._stickyInputValue`, `this._tableParent`, `this.input`, `this.input.autocomplete`

## defaultEngine()
- 位置: L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._defaultEngine`

## defaultEngine()
- 位置: L266-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateDefaultEngineHeader()`, `this._updateDefaultEngineIcon()`
- 条件付き依存: `if (this._defaultEngine && this._defaultEngine.icon)` → `URL.revokeObjectURL()`
- 条件付き依存: `if (engine.iconData)` → `this._getFaviconURIFromIconData()`
- 条件付き依存: `if (engine && document.activeElement == this.input)` → `this._speculativeConnect()`
- 参照: `document.activeElement`, `engine.iconData`, `engine.isConfigEngine`, `engine.name`, `this._defaultEngine`, `this._defaultEngine.icon`, `this.input`

## engines()
- 位置: L289-291
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._engines`

## engines()
- 位置: L293-296
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._engines`, `this._pendingOneOffRefresh`

## selectedIndex()
- 位置: L301-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elt.classList.contains()`, `this._tableParent.querySelector()`
- 参照: `allElts.length`, `this._oneOffButtons`, `this._suggestionsList.children`

## selectedIndex()
- 位置: L316-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._table.removeAttribute()`, `this._tableParent.querySelector()`, `this.input.removeAttribute()`
- 条件付き依存: `if (i == idx)` → `elt.classList.add()`
- 条件付き依存: `if (i == idx)` → `ariaSelectedElt.setAttribute()`
- 条件付き依存: `if (i == idx)` → `this.input.setAttribute()`
- 条件付き依存: `if (i != excludeIndex)` → `elt.classList.remove()`
- 条件付き依存: `if (i != excludeIndex)` → `ariaSelectedElt.setAttribute()`
- 参照: `allElts.length`, `ariaSelectedElt.id`, `elt.firstChild`, `this._oneOffButtons`, `this._suggestionsList.children`, `this.numSuggestions`, `this.selectedButtonIndex`

## selectedButtonIndex()
- 位置: L345-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elts[i].classList.contains()`, `this._tableParent.querySelector()`
- 参照: `elts.length`, `this._oneOffButtons`

## selectedButtonIndex()
- 位置: L358-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tableParent.querySelector()`
- 条件付き依存: `if (i == idx)` → `elt.classList.add()`
- 条件付き依存: `if (i == idx)` → `elt.setAttribute()`
- 条件付き依存: `if (!(i == idx))` → `elt.classList.remove()`
- 条件付き依存: `if (!(i == idx))` → `elt.setAttribute()`
- 参照: `elts.length`, `this._oneOffButtons`

## selectedEngineName()
- 位置: L375-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._oneOffsTable.querySelector()`
- 参照: `selectedElt.engineName`, `this.defaultEngine.name`

## numSuggestions()
- 位置: L383-385
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._suggestionsList.children.length`

## selectAndUpdateInput()
- 位置: L387-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateSearchWithHeader()`, `this.suggestionAtIndex()`
- 参照: `this._stickyInputValue`, `this.input.value`, `this.selectedIndex`

## suggestionAtIndex()
- 位置: L398-401
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `row.textContent`, `this._suggestionsList.children`

## deleteSuggestionAtIndex()
- 位置: L403-411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isFormHistorySuggestionAtIndex()`
- 条件付き依存: `if (this.isFormHistorySuggestionAtIndex(idx))` → `this.suggestionAtIndex()`
- 条件付き依存: `if (this.isFormHistorySuggestionAtIndex(idx))` → `this._sendMsg()`
- 条件付き依存: `if (this.isFormHistorySuggestionAtIndex(idx))` → `this._suggestionsList.children[idx].remove()`
- 条件付き依存: `if (this.isFormHistorySuggestionAtIndex(idx))` → `this.selectAndUpdateInput()`
- 参照: `this._suggestionsList.children`

## isFormHistorySuggestionAtIndex()
- 位置: L413-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `row.classList.contains()`
- 参照: `this._suggestionsList.children`

## addInputValueToFormHistory()
- 位置: L418-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`
- 参照: `this.input.value`, `this.selectedEngineName`

## handleEvent()
- 位置: L427-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.type.substr()`, `event.type[0].toUpperCase()`, `this["_on" + event.type[0].toUpperCase() + event.type.substr(1)]()`
- 参照: `event.type`, `this.input.isConnected`

## _onCommand()
- 位置: L436-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.search()`
- 条件付き依存: `if (this.selectedButtonIndex == this._oneOffButtons.length)` → `this._sendMsg()`
- 条件付き依存: `if (aEvent)` → `aEvent.preventDefault()`
- 参照: `this._oneOffButtons.length`, `this.selectedButtonIndex`

## search()
- 位置: L450-499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`, `this.addInputValueToFormHistory()`, `this.suggestionAtIndex()`
- 条件付き依存: `if (!( this._table.hidden || (aEvent.originalTarget && aEvent.originalTarget.id == "contentSearchDefaultEngineHeader") || aEvent instanceof KeyboardEvent ))` → `this.suggestionAtIndex()`
- 参照: `aEvent.altKey`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.originalTarget`, `aEvent.originalTarget.id`, `aEvent.shiftKey`, `eventData.originalEvent.button`, `eventData.selection`, `eventData.selection.kind`, `searchText.value`, `this._healthReportKey`, `this._table.hidden`, `this.defaultEngine`, `this.input`, `this.selectedEngineName`, `this.selectedIndex`

## _onInput()
- 位置: L501-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateSearchWithHeader()`
- 条件付き依存: `if (!this.input.value)` → `this._hideSuggestions()`
- 条件付き依存: `if (this.input.value != this._stickyInputValue)` → `this._getSuggestions()`
- 条件付き依存: `if (this.input.value != this._stickyInputValue)` → `this.selectAndUpdateInput()`
- 参照: `this._stickyInputValue`, `this.input.value`

## _onKeydown()
- 位置: L513-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.getModifierState()`, `event.preventDefault()`, `this._hideSuggestions()`, `this._onCommand()`
- 条件付き依存: `if (event.getModifierState("Accel"))` → `this._cycleCurrentEngine()`
- 条件付き依存: `if (this._table.hidden)` → `this._getSuggestions()`
- 条件付き依存: `if ( this.numSuggestions && this.selectedIndex >= 0 && this.selectedIndex < this.numSuggestions )` → `this.suggestionAtIndex()`
- 条件付き依存: `if ( this.numSuggestions && this.selectedIndex >= 0 && this.selectedIndex < this.numSuggestions )` → `this.input.setAttribute()`
- 条件付き依存: `if (!( this.numSuggestions && this.selectedIndex >= 0 && this.selectedIndex < this.numSuggestions ))` → `this.input.removeAttribute()`
- 条件付き依存: `if (this.selectedIndex >= 0)` → `this.deleteSuggestionAtIndex()`
- 条件付き依存: `if (!this._table.hidden)` → `this._hideSuggestions()`
- 条件付き依存: `if (selectedIndexDelta)` → `this.selectAndUpdateInput()`
- 条件付き依存: `if (selectedSuggestionDelta)` → `this.selectAndUpdateInput()`
- 参照: `event.DOM_VK_DELETE`, `event.DOM_VK_DOWN`, `event.DOM_VK_ESCAPE`, `event.DOM_VK_RETURN`, `event.DOM_VK_RIGHT`, `event.DOM_VK_TAB`, `event.DOM_VK_UP`, `event.altKey`, `event.keyCode`, `event.shiftKey`, `this._oneOffButtons.length`, `this._stickyInputValue`, `this._table.hidden`, `this.input.selectionEnd`, `this.input.selectionStart`, `this.input.value`, `this.input.value.length`, `this.numSuggestions`, `this.selectedButtonIndex`, `this.selectedIndex`

## _cycleCurrentEngine()
- 位置: L667-677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`
- 参照: `this._currentEngineIndex`, `this._engines`, `this._engines.length`, `this._engines[this._currentEngineIndex].name`

## _onFocus()
- 位置: L679-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._speculativeConnect()`, `this.input.setAttribute()`
- 参照: `this._mousedown`

## _onBlur()
- 位置: L692-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideSuggestions()`, `this.input.removeAttribute()`
- 条件付き依存: `if (this._mousedown)` → `setTimeout()`
- 条件付き依存: `if (this._mousedown)` → `this.input.focus()`
- 参照: `this._mousedown`

## _onMousemove()
- 位置: L704-713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._indexOfTableItem()`
- 参照: `event.target`, `this.numSuggestions`, `this.selectedButtonIndex`, `this.selectedIndex`

## _onMouseup()
- 位置: L715-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onCommand()`
- 参照: `event.button`

## _onMouseout()
- 位置: L722-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._indexOfTableItem()`
- 参照: `event.originalTarget`, `this.numSuggestions`, `this.selectedButtonIndex`

## _onClick()
- 位置: L731-733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onMouseup()`

## _onContentSearchService()
- 位置: L735-740
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.detail.data`, `event.detail.type`

## _onMsgFocusInput()
- 位置: L742-744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.focus()`

## _onMsgBlur()
- 位置: L746-749
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._hideSuggestions()`, `this.input.blur()`

## _onMsgSuggestions()
- 位置: L751-803
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suggestions.searchString.trim()`, `suggestions.searchString.trim().toLowerCase()`, `suggestions.searchString.trim().toLowerCase().split()`, `this._clearSuggestionRows()`, `this._makeTableRow()`, `this._suggestionsList.appendChild()`, `this.input.getBoundingClientRect()`
- 条件付き依存: `if (this._pendingOneOffRefresh)` → `this._setUpOneOffButtons()`
- 条件付き依存: `if (this._table.hidden)` → `this._engines.findIndex()`
- 条件付き依存: `if (this._table.hidden)` → `this.input.setAttribute()`
- 参照: `aEngine.name`, `suggestions.engineName`, `suggestions.formHistory.length`, `suggestions.remote.length`, `suggestions.searchString`, `this._currentEngineIndex`, `this._pendingOneOffRefresh`, `this._stickyInputValue`, `this._table.hidden`, `this._table.style.maxWidth`, `this._table.style.minWidth`, `this._table.style.top`, `this.defaultEngine.name`, `this.input.offsetHeight`, `this.input.offsetWidth`, `this.selectedIndex`, `window.innerWidth`

## _onMsgSuggestionsCancelled()
- 位置: L805-809
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._table.hidden)` → `this._hideSuggestions()`
- 参照: `this._table.hidden`

## _onMsgState()
- 位置: L811-833
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `currentEngine.icon`, `currentEngine.name`, `state.currentEngine`, `state.currentPrivateEngine`, `state.engines`, `state.isPrivateEngine`, `this._isPrivateEngine`, `this.defaultEngine`, `this.defaultEngine.icon`, `this.defaultEngine.name`, `this.engines`

## _onMsgCurrentState()
- 位置: L835-837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onMsgState()`

## _onMsgCurrentEngine()
- 位置: L839-845
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isPrivateEngine`, `this._pendingOneOffRefresh`, `this.defaultEngine`

## _onMsgCurrentPrivateEngine()
- 位置: L847-853
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._isPrivateEngine`, `this._pendingOneOffRefresh`, `this.defaultEngine`

## _onMsgStrings()
- 位置: L855-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._tableParent.querySelector()`, `this._updateDefaultEngineHeader()`, `this._updateSearchWithHeader()`
- 参照: `this._strings`, `this._strings.searchSettings`, `this._tableParent.querySelector( "#contentSearchSettingsButton" ).textContent`

## _updateDefaultEngineIcon()
- 位置: L864-875
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.body.style.setProperty()`
- 参照: `this.defaultEngine.icon`, `this.defaultEngine.isConfigEngine`

## _updateDefaultEngineHeader()
- 位置: L877-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createTextNode()`, `header.appendChild()`, `header.firstChild.nextSibling.remove()`, `header.firstChild.setAttribute()`, `this._strings.searchHeader.replace()`, `this._tableParent.querySelector()`
- 参照: `header.firstChild.nextSibling`, `this._strings`, `this.defaultEngine.icon`, `this.defaultEngine.name`

## _updateSearchWithHeader()
- 位置: L895-915
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchWithHeader.querySelectorAll()`, `this._tableParent.querySelector()`
- 条件付き依存: `if (this.input.value)` → `header.replace("%1$S", "%S").split()`
- 条件付き依存: `if (this.input.value)` → `header.replace()`
- 参照: `labels[0].textContent`, `labels[1].textContent`, `labels[2].textContent`, `this._strings`, `this._strings.searchForSomethingWith2`, `this._strings.searchWithHeader`, `this.input.value`

## _speculativeConnect()
- 位置: L917-921
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.defaultEngine)` → `this._sendMsg()`
- 参照: `this.defaultEngine`, `this.defaultEngine.name`

## _makeTableRow()
- 位置: L923-957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElementNS()`, `entry.appendChild()`, `entry.classList.add()`, `entry.setAttribute()`, `img.setAttribute()`, `row.addEventListener()`, `row.appendChild()`, `row.classList.add()`, `row.setAttribute()`, `searchWords.has()`, `suggestionStr.trim()`, `suggestionStr.trim().toLowerCase()`, `suggestionStr.trim().toLowerCase().split()`
- 条件付き依存: `if (searchWords.has(word))` → `wordSpan.classList.add()`
- 条件付き依存: `if (i < suggestionWords.length - 1)` → `entry.appendChild()`
- 条件付き依存: `if (i < suggestionWords.length - 1)` → `document.createTextNode()`
- 参照: `entry.id`, `row.dir`, `suggestionWords.length`, `this._idPrefix`, `wordSpan.textContent`

## _getFaviconURIFromIconData()
- 位置: L968-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.createObjectURL()`
- 参照: `data.icon`, `data.mimeType`

## _getImageURIForCurrentResolution()
- 位置: L979-984
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (window.devicePixelRatio > 1)` → `uri.replace()`
- 参照: `window.devicePixelRatio`

## _getSearchEngines()
- 位置: L986-988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`

## _getStrings()
- 位置: L990-992
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMsg()`

## _getSuggestions()
- 位置: L994-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.defaultEngine)` → `this._sendMsg()`
- 参照: `this._stickyInputValue`, `this.defaultEngine`, `this.defaultEngine.name`, `this.input.value`

## _clearSuggestionRows()
- 位置: L1004-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._suggestionsList.firstElementChild.remove()`
- 参照: `this._suggestionsList.firstElementChild`

## _hideSuggestions()
- 位置: L1010-1016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.input.setAttribute()`
- 参照: `this._currentEngineIndex`, `this._table.hidden`, `this.selectedButtonIndex`, `this.selectedIndex`

## _indexOfTableItem()
- 位置: L1018-1032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elt.classList.contains()`
- 条件付き依存: `if (elt.classList.contains("contentSearchOneOffItem"))` → `this._oneOffButtons.indexOf()`
- 参照: `elt.localName`, `elt.parentNode`, `elt.rowIndex`, `this._oneOffButtons.length`, `this.numSuggestions`

## _makeTable()
- 位置: L1034-1113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.addEventListener()`, `button.classList.add()`, `button.setAttribute()`, `cell.appendChild()`, `cell.setAttribute()`, `document.addEventListener()`, `document.createElement()`, `document.createElementNS()`, `header.appendChild()`, `header.setAttribute()`, `headerRow.addEventListener()`, `headerRow.appendChild()`, `headerRow.setAttribute()`, `inputLabel.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `this._oneOffsTable.appendChild()`, `this._oneOffsTable.classList.add()`, `this._oneOffsTable.setAttribute()`, `this._suggestionsList.setAttribute()`, `this._table.addEventListener()`, `this._table.appendChild()`, `this._table.classList.add()`, `this._table.setAttribute()`
- 参照: `button.id`, `header.id`, `this._mousedown`, `this._oneOffsTable`, `this._suggestionsList`, `this._table`, `this._table.hidden`, `this._table.id`

## _setUpOneOffButtons()
- 位置: L1115-1199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `URL.revokeObjectURL()`, `button.addEventListener()`, `button.appendChild()`, `button.setAttribute()`, `cell.appendChild()`, `cell.setAttribute()`, `document.createElementNS()`, `img.addEventListener()`, `img.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `this._engines .filter()`, `this._engines .filter(aEngine => aEngine.name != this.defaultEngine.name) .filter()`, `this._oneOffButtons.push()`, `this._oneOffsTable.appendChild()`, `this._oneOffsTable.firstChild.nextSibling.remove()`
- 条件付き依存: `if (i > 0 && i % enginesPerRow == 0)` → `row.appendChild()`
- 条件付き依存: `if (i > 0 && i % enginesPerRow == 0)` → `this._oneOffsTable.appendChild()`
- 条件付き依存: `if (i > 0 && i % enginesPerRow == 0)` → `document.createElementNS()`
- 条件付き依存: `if (i > 0 && i % enginesPerRow == 0)` → `row.setAttribute()`
- 条件付き依存: `if (i > 0 && i % enginesPerRow == 0)` → `cell.setAttribute()`
- 条件付き依存: `if (engine.iconData)` → `this._getFaviconURIFromIconData()`
- 条件付き依存: `if (!(engine.iconData))` → `this._getImageURIForCurrentResolution()`
- 条件付き依存: `if (engines.length - i <= enginesPerRow - (i % enginesPerRow))` → `button.classList.add()`
- 条件付き依存: `if ((i + 1) % enginesPerRow == 0)` → `button.classList.add()`
- 参照: `aEngine.hidden`, `aEngine.name`, `button.engineName`, `button.id`, `button.style.width`, `engine.iconData`, `engine.name`, `engines.length`, `this._engines`, `this._oneOffButtons`, `this._oneOffsTable.firstChild.nextSibling`, `this._oneOffsTable.hidden`, `this.defaultEngine.name`, `this.input.offsetWidth`

## _sendMsg()
- 位置: L1201-1210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchEvent()`

## ContentSearchHandoffUI.constructor()
- 位置: L1235-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.disabled`, `this.fakeFocus`, `this.nonHandoff`

## ContentSearchHandoffUI.nonHandoffMode()
- 位置: L1242-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.nonHandoff`

## ContentSearchHandoffUI.#doSearchHandoff()
- 位置: L1246-1249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.doSearchHandoff()`
- 参照: `this.fakeFocus`

## ContentSearchHandoffUI.#onSearchHandoffClick()
- 位置: L1251-1258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.#doSearchHandoff()`

## ContentSearchHandoffUI.#onSearchHandoffPaste()
- 位置: L1260-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.clipboardData.getData()`, `event.preventDefault()`, `this.#doSearchHandoff()`

## ContentSearchHandoffUI.#onSearchHandoffDrop()
- 位置: L1265-1271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.dataTransfer.getData()`, `event.preventDefault()`
- 条件付き依存: `if (text)` → `this.#doSearchHandoff()`

## ContentSearchHandoffUI.firstUpdated()
- 位置: L1273-1289
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `globalThis.document`, `globalThis.document.documentURI`, `this.#controller`, `this.nonHandoffMode`, `this.nonHandoffSearchInput`, `this.nonHandoffSearchInput.parentElement`, `window.ContentSearchHandoffUIController`, `window.ContentSearchUIController`

## ContentSearchHandoffUI.render()
- 位置: L1291-1301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handoffTemplate()`, `this.#nonHandoffTemplate()`
- 参照: `this.nonHandoffMode`

## ContentSearchHandoffUI.#onNonHandoffSearchClick()
- 位置: L1303-1305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.search()`

## ContentSearchHandoffUI.#nonHandoffTemplate()
- 位置: L1307-1324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#onNonHandoffSearchClick`

## ContentSearchHandoffUI.#handoffTemplate()
- 位置: L1326-1343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#onSearchHandoffClick`, `this.#onSearchHandoffDrop`, `this.#onSearchHandoffPaste`
