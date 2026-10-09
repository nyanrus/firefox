# browser/components/search/content/searchbar.js

source: browser/components/search/content/searchbar.js
source-hash: bebd239f31ac9179d75514892091e9bc671dde77
lines: 1032

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## MozSearchbar.inheritedAttributes()
- 位置: L32-38
- 役割: (未記入)
- 触るとき: (未記入)

## MozSearchbar.markup()
- 位置: L40-53
- 役割: (未記入)
- 触るとき: (未記入)

## MozSearchbar.constructor()
- 位置: L55-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `MozXULElement.insertFTLIfNeeded()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `super()`, `this._setupEventListeners()`, `this.destroy()`, `window.addEventListener()`
- 参照: `this._engines`, `this._ignoreFocus`, `this.observer`, `this.telemetrySelectedIndex`
- XPCOM: `Services.prefs`

## MozSearchbar.observe()
- 位置: L62-80
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic == "browser-search-engine-modified")` → `searchbar._textbox.popup.updateHeader()`
- 条件付き依存: `if (aTopic == "browser-search-engine-modified")` → `searchbar.updateDisplay()`
- 条件付き依存: `if ( aData == "browser.search.widget.new" && searchbar.isConnected )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.search.widget.new"))` → `searchbar.disconnectedCallback()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.search.widget.new")))` → `searchbar.connectedCallback()`
- 参照: `searchbar._engines`, `searchbar.isConnected`
- XPCOM: `Services.prefs`

## MozSearchbar.connectedCallback()
- 位置: L99-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(window.delayedStartupPromise || Promise.resolve()).then()`, `OpenSearchManager.updateOpenSearchBadge()`, `Promise.resolve()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.xulStore.getValue()`, `console.error()`, `lazy.SearchService.init()`, `lazy.SearchService.init() .then()`, `this._initTextbox()`, `this._setupTextboxEventListeners()`, `this._textbox.popup.updateHeader()`, `this.appendChild()`, `this.closest()`, `this.handleSearchCommand()`, `this.initializeAttributeInheritance()`, `this.querySelector()`, `this.querySelector(".search-go-button").addEventListener()`, `this.textbox.popup.addEventListener()`, `this.updateDisplay()`, `window.requestIdleCallback()`
- 条件付き依存: `if (storedWidth)` → `this.parentNode.setAttribute()`
- 参照: `document.documentURI`, `oneOffButtons.popup`, `oneOffButtons.telemetryOrigin`, `oneOffButtons.textbox`, `this._initialized`, `this._menupopup`, `this._pasteAndSearchMenuItem`, `this._stringBundle`, `this._textbox`, `this.constructor.fragment`, `this.observer`, `this.parentNode.id`, `this.parentNode.parentNode.localName`, `this.parentNode.style.width`, `this.textbox`, `this.textbox.popup`, `this.textbox.popup.oneOffButtons`, `window.delayedStartupPromise`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.xulStore`

## MozSearchbar.getEngines()
- 位置: async L190-195
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._engines)` → `lazy.SearchService.getVisibleEngines()`
- 参照: `this._engines`

## MozSearchbar.currentEngine()
- 位置: L197-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `lazy.SearchService.setDefaultPrivate()`
- 条件付き依存: `if (!(PrivateBrowsingUtils.isWindowPrivate(window)))` → `lazy.SearchService.setDefault()`
- 参照: `lazy.SearchService.CHANGE_REASON.USER_SEARCHBAR`

## MozSearchbar.currentEngine()
- 位置: L211-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`

## MozSearchbar.textbox()
- 位置: L228-230
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._textbox`

## MozSearchbar.inputField()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.textbox`

## MozSearchbar.value()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._textbox.value`

## MozSearchbar.value()
- 位置: L243-245
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._textbox.value`

## MozSearchbar.destroy()
- 位置: L247-271
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._textbox`, `this._textbox.mController`, `this._textbox.mController.input`, `this._textbox.mController.input.wrappedJSObject`, `this.nsIAutocompleteInput`, `this.observer`
- XPCOM: `Services.obs`

## MozSearchbar.focus()
- 位置: L273-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._textbox.focus()`

## MozSearchbar.select()
- 位置: L277-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._textbox.select()`

## MozSearchbar.setIcon()
- 位置: L281-283
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.setAttribute()`

## MozSearchbar.updateDisplay()
- 位置: L285-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._stringBundle.getFormattedString()`
- 参照: `this._textbox.title`, `this.currentEngine.name`

## MozSearchbar.updateGoButtonVisibility()
- 位置: L291-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`
- 参照: `this._textbox.value`, `this.querySelector(".search-go-button").hidden`

## MozSearchbar.openSuggestionsPanel()
- 位置: L295-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `searchIcon.setAttribute()`, `this._textbox.showHistoryPopup()`
- 条件付き依存: `if (this._textbox.value)` → `this._textbox.mController.handleText()`
- 条件付き依存: `if (aShowOnlySettingsIfEmpty)` → `this.setAttribute()`
- 参照: `this._textbox.open`, `this._textbox.value`

## MozSearchbar.selectEngine()
- 位置: async L313-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.preventDefault()`, `aEvent.stopPropagation()`, `this.getEngines()`, `this.openSuggestionsPanel()`
- 参照: `engines.length`, `engines[i].name`, `this.currentEngine`, `this.currentEngine.name`

## MozSearchbar.handleSearchCommand()
- 位置: L342-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.originalTarget.classList.contains()`, `this._whereToOpen()`, `this.handleSearchCommandWhere()`
- 参照: `aEvent.button`

## MozSearchbar.handleSearchCommandWhere()
- 位置: L354-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchSuggestionSelectionMethod()`, `this.doSearch()`
- 条件付き依存: `if (selectedIndex == -1)` → `this.textbox.popup.oneOffButtons.eventTargetIsAOneOff()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.keyCode`, `aParams.avoidBrowserFocus`, `aParams.inBackground`, `textBox.value`, `this._needBrowserFocusAtEnterKeyUp`, `this._textbox`, `this.telemetrySelectedIndex`

## MozSearchbar.doSearch()
- 位置: L387-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.setStringPref()`, `engine.getSubmission()`, `new Date().toISOString()`, `openTrustedLinkIn()`
- 条件付き依存: `if ( aData && !PrivateBrowsingUtils.isWindowPrivate(window) && lazy.FormHistory.enabled && aData.length <= lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VAL...)` → `lazy.FormHistory.update()`
- 条件付き依存: `if ( aData && !PrivateBrowsingUtils.isWindowPrivate(window) && lazy.FormHistory.enabled && aData.length <= lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VAL...)` → `textBox.getAttribute()`
- 条件付き依存: `if ( aData && !PrivateBrowsingUtils.isWindowPrivate(window) && lazy.FormHistory.enabled && aData.length <= lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VAL...)` → `console.error()`
- 条件付き依存: `if (aWhere == "tab")` → `gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (aWhere == "tab")` → `lazy.BrowserSearchTelemetry.recordSearch()`
- 条件付き依存: `if (!(aWhere == "tab"))` → `lazy.BrowserSearchTelemetry.recordSearch()`
- 参照: `aData.length`, `engine.name`, `event.target.linkedBrowser`, `gBrowser.selectedBrowser`, `lazy.FormHistory.enabled`, `lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VALUE_LENGTH`, `submission.postData`, `submission.uri.spec`, `this._textbox`, `this.currentEngine`, `this.telemetrySelectedIndex`
- XPCOM: `Services.prefs`

## MozSearchbar._whereToOpen()
- 位置: L474-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `aEvent?.originalTarget.classList.contains()`
- 条件付き依存: `if (aEvent?.originalTarget.classList.contains("search-go-button"))` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (aEvent?.originalTarget.classList.contains("search-go-button"))` → `aEvent.getModifierState()`
- 条件付き依存: `if (aForceNewTab)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(aForceNewTab))` → `KeyboardEvent.isInstance()`
- 条件付き依存: `if (!(aForceNewTab))` → `aEvent.getModifierState()`
- 条件付き依存: `if (!(aForceNewTab))` → `MouseEvent.isInstance()`
- 参照: `aEvent.altKey`, `aEvent.button`, `gBrowser.selectedTab.isEmpty`
- XPCOM: `Services.prefs`

## MozSearchbar.openSearchFormWhere()
- 位置: L534-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchForm()`, `openTrustedLinkIn()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.keyCode`, `engine.searchForm`, `params.avoidBrowserFocus`, `params.inBackground`, `this._needBrowserFocusAtEnterKeyUp`, `this.currentEngine`

## MozSearchbar.disconnectedCallback()
- 位置: L554-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.destroy()`, `this.firstChild.remove()`
- 参照: `this.firstChild`

## MozSearchbar._maybeSelectAll()
- 位置: L565-573
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this._preventClickSelectsAll && document.activeElement == this._textbox && this._textbox.selectionStart == this._textbox.selectionEnd )` → `this.select()`
- 参照: `document.activeElement`, `this._preventClickSelectsAll`, `this._textbox`, `this._textbox.selectionEnd`, `this._textbox.selectionStart`

## MozSearchbar._setupEventListeners()
- 位置: L575-679
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.getLastFocusMethod()`, `event.getModifierState()`, `event.originalTarget.classList.contains()`, `this._maybeSelectAll()`, `this.addEventListener()`, `this.currentEngine.speculativeConnect()`, `this.openSuggestionsPanel()`, `this.updateGoButtonVisibility()`
- 条件付き依存: `if (event.getModifierState("Accel"))` → `this.selectEngine()`
- 条件付き依存: `if (isIconClick && this.textbox.popup.popupOpen)` → `this.textbox.popup.closePopup()`
- 条件付き依存: `if (isIconClick && this.textbox.popup.popupOpen)` → `document.querySelector()`
- 条件付き依存: `if (isIconClick && this.textbox.popup.popupOpen)` → `searchIcon.setAttribute()`
- 条件付き依存: `if (isIconClick || this._textbox.value)` → `this.openSuggestionsPanel()`
- 参照: `Services.focus.FLAG_BYMOUSE`, `document.activeElement`, `event.button`, `event.detail`, `event.originalTarget.localName`, `gBrowser.contentPrincipal.originAttributes`, `this._ignoreFocus`, `this._needBrowserFocusAtEnterKeyUp`, `this._preventClickSelectsAll`, `this._textbox`, `this._textbox.focused`, `this._textbox.value`, `this.textbox.popup.popupOpen`
- XPCOM: `Services.focus`

## MozSearchbar._setupTextboxEventListeners()
- 位置: L681-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.isCommandEnabled()`, `dataTransfer.getData()`, `document.commandDispatcher .getControllerForCommand()`, `document.commandDispatcher .getControllerForCommand("cmd_paste") .isCommandEnabled()`, `document.commandDispatcher.getControllerForCommand()`, `event.preventDefault()`, `item.getAttribute()`, `this._menupopup.openPopupAtScreen()`, `this._menupopup.querySelectorAll()`, `this._textbox.closePopup()`, `this.textbox.addEventListener()`, `this.textbox.popup.removeAttribute()`, `types.includes()`
- 条件付き依存: `if ( types.includes("text/plain") || types.includes("text/x-moz-text-internal") )` → `event.preventDefault()`
- 条件付き依存: `if (!data)` → `dataTransfer.getData()`
- 条件付き依存: `if (data)` → `event.preventDefault()`
- 条件付き依存: `if (data)` → `this.openSuggestionsPanel()`
- 条件付き依存: `if (!this._menupopup)` → `this._buildContextMenu()`
- 条件付き依存: `if (event.button)` → `this._maybeSelectAll()`
- 参照: `event.button`, `event.dataTransfer`, `event.dataTransfer.types`, `event.screenX`, `event.screenY`, `item.disabled`, `this._menupopup`, `this._pasteAndSearchMenuItem.disabled`, `this.textbox.value`

## MozSearchbar._initTextbox()
- 位置: L741-961
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `this.setAttribute()`
- 参照: `this.parentNode.parentNode.localName`, `this.textbox`, `this.textbox.handleEnter`, `this.textbox.onBeforeHandleKeyDown`, `this.textbox.onBeforeValueSet`, `this.textbox.onTextEntered`, `this.textbox.onbeforeinput`, `this.textbox.onkeyup`, `this.textbox.openPopup`, `this.textbox.openSearch`, `this.textbox.popup.id`

## MozSearchbar.get()
- 位置: L756-761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this.getAttribute()`

## MozSearchbar.set()
- 位置: L762-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setAttribute()`

## MozSearchbar.get()
- 位置: L768-770
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.popup.oneOffButtons.selectedButton`

## MozSearchbar.set()
- 位置: L771-773
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.popup.oneOffButtons.selectedButton`

## this.textbox.onBeforeValueSet()
- 位置: L778-783
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.textbox.popup._oneOffButtons`, `this.textbox.popup.oneOffButtons.query`

## this.textbox.onBeforeHandleKeyDown()
- 位置: L786-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.getModifierState()`, `document.querySelector()`, `searchIcon.setAttribute()`
- 条件付き依存: `if ( aEvent.keyCode == KeyEvent.DOM_VK_DOWN || aEvent.keyCode == KeyEvent.DOM_VK_UP )` → `this.selectEngine()`
- 条件付き依存: `if ( (AppConstants.platform == "macosx" && aEvent.keyCode == KeyEvent.DOM_VK_F4) || (aEvent.getModifierState("Alt") && (aEvent.keyCode == KeyEvent.DOM_VK_DOWN ||...)` → `this.textbox.openSearch()`
- 条件付き依存: `if (!this.textbox.openSearch())` → `aEvent.preventDefault()`
- 条件付き依存: `if (!this.textbox.openSearch())` → `aEvent.stopPropagation()`
- 条件付き依存: `if (popup.popupOpen)` → `popup.richlistbox.hasAttribute()`
- 条件付き依存: `if (popup.popupOpen)` → `popup.oneOffButtons.handleKeyDown()`
- 条件付き依存: `if (this.textbox.editor.canUndo)` → `this.textbox.editor.undoAll()`
- 条件付き依存: `if (!(this.textbox.editor.canUndo))` → `this.textbox.select()`
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `aEvent.preventDefault()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_F4`, `KeyEvent.DOM_VK_UP`, `aEvent.keyCode`, `popup.matchCount`, `popup.popupOpen`, `this.textbox.editor.canUndo`, `this.textbox.popup`

## this.textbox.openPopup()
- 位置: L835-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`, `document.querySelector()`
- 条件付き依存: `if (popup.id == "PopupSearchAutoComplete")` → `popup.setAttribute()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (popup.oneOffButtons)` → `Math.max()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `popup.style.setProperty()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `popup._invalidate()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `popup.openPopup()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `searchIcon.setAttribute()`
- 参照: `popup.hidden`, `popup.id`, `popup.mInput`, `popup.mPopupOpen`, `popup.oneOffButtons`, `popup.oneOffButtons.buttonWidth`, `popup.selectedIndex`, `this.textbox`, `this.textbox.popup`

## this.textbox.openSearch()
- 位置: L880-886
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.textbox.popupOpen)` → `this.openSuggestionsPanel()`
- 参照: `this.textbox.popupOpen`

## this.textbox.handleEnter()
- 位置: L888-922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.textbox.mController.handleEnter()`, `this.textbox.selectedButton.getAttribute()`, `this.textbox.selectedButton?.classList.contains()`, `this.textbox.selectedButton?.getAttribute()`
- 条件付き依存: `if (event.shiftKey)` → `this._whereToOpen()`
- 条件付き依存: `if (event.shiftKey)` → `this.openSearchFormWhere()`
- 参照: `event.shiftKey`, `this.textbox.selectedButton`, `this.textbox.selectedButton.open`, `this.textbox.selectedButton?.engine`, `this.textbox.value`

## this.textbox.onTextEntered()
- 位置: L925-942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleSearchCommand()`, `this.textbox.editor.clearUndoRedo()`
- 条件付き依存: `if (!oneOff.engine)` → `oneOff.doCommand()`
- 参照: `oneOff.engine`, `this.telemetrySelectedIndex`, `this.textbox.popupSelectedIndex`, `this.textbox.selectedButton`

## this.textbox.onbeforeinput()
- 位置: L944-949
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.data && this._needBrowserFocusAtEnterKeyUp)` → `event.preventDefault()`
- 参照: `event.data`, `this._needBrowserFocusAtEnterKeyUp`

## this.textbox.onkeyup()
- 位置: L951-960
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._needBrowserFocusAtEnterKeyUp)` → `gBrowser.selectedBrowser.focus()`
- 参照: `this._needBrowserFocusAtEnterKeyUp`

## MozSearchbar._buildContextMenu()
- 位置: L963-1027
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozXULElement.parseXULToFragment()`, `clearHistoryItem.setAttribute()`, `event.originalTarget.getAttribute()`, `frag.querySelector()`, `goDoCommand()`, `lazy.FormHistory.update()`, `this._menupopup.addEventListener()`, `this._menupopup.appendChild()`, `this._pasteAndSearchMenuItem.setAttribute()`, `this._stringBundle.getString()`, `this.handleSearchCommand()`, `this.querySelector()`, `this.select()`, `this.textbox.getAttribute()`
- 条件付き依存: `if (cmd)` → `document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if (cmd)` → `controller.doCommand()`
- 参照: `event.originalTarget`, `this._menupopup`, `this._pasteAndSearchMenuItem`, `this.textbox.value`
