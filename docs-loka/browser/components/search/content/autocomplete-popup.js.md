# browser/components/search/content/autocomplete-popup.js

source: browser/components/search/content/autocomplete-popup.js
source-hash: 3ebd43a3fe78c28467fa69ba1bb10e2a20e7aba6
lines: 344

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## MozSearchAutocompleteRichlistboxPopup.constructor()
- 位置: L29-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this._oneOffButtons.addEventListener()`, `this._oneOffButtons.removeEventListener()`, `this.addEventListener()`, `this.searchbar.hasAttribute()`, `this.updateHeader()`, `this.updateHeader().catch()`
- 条件付き依存: `if (this.searchbar.hasAttribute("showonlysettings"))` → `this.searchbar.removeAttribute()`
- 条件付き依存: `if (this.searchbar.hasAttribute("showonlysettings"))` → `this.setAttribute()`
- 条件付き依存: `if (!(this.searchbar.hasAttribute("showonlysettings")))` → `this.removeAttribute()`
- 条件付き依存: `if (this.searchbar.value)` → `this.oneOffButtons.handleSearchCommand()`
- 条件付き依存: `if (event.shiftKey)` → `this.openSearchForm()`
- 参照: `button.parentNode.engine`, `console.error`, `event.button`, `event.originalTarget`, `event.shiftKey`, `this._bundle`, `this.matchCount`, `this.richlistbox.collapsed`, `this.searchbar.value`

## MozSearchAutocompleteRichlistboxPopup.inheritedAttributes()
- 位置: L92-97
- 役割: (未記入)
- 触るとき: (未記入)

## MozSearchAutocompleteRichlistboxPopup.getElementForAttrInheritance()
- 位置: L101-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozSearchAutocompleteRichlistboxPopup.initialize()
- 位置: L105-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `super.initialize()`, `this.initializeAttributeInheritance()`, `this.querySelector()`
- 参照: `lazy.SearchOneOffs`, `this._oneOffButtons`, `this._searchOneOffsContainer`, `this._searchbar`, `this._searchbarEngine`, `this._searchbarEngineName`

## MozSearchAutocompleteRichlistboxPopup.oneOffButtons()
- 位置: L118-123
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._oneOffButtons)` → `this.initialize()`
- 参照: `this._oneOffButtons`

## MozSearchAutocompleteRichlistboxPopup.markup()
- 位置: L125-136
- 役割: (未記入)
- 触るとき: (未記入)

## MozSearchAutocompleteRichlistboxPopup.searchOneOffsContainer()
- 位置: L138-143
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._searchOneOffsContainer)` → `this.initialize()`
- 参照: `this._searchOneOffsContainer`

## MozSearchAutocompleteRichlistboxPopup.searchbarEngine()
- 位置: L145-150
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._searchbarEngine)` → `this.initialize()`
- 参照: `this._searchbarEngine`

## MozSearchAutocompleteRichlistboxPopup.searchbarEngineName()
- 位置: L152-157
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._searchbarEngineName)` → `this.initialize()`
- 参照: `this._searchbarEngineName`

## MozSearchAutocompleteRichlistboxPopup.searchbar()
- 位置: L159-164
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._searchbar)` → `this.initialize()`
- 参照: `this._searchbar`

## MozSearchAutocompleteRichlistboxPopup.bundle()
- 位置: L166-172
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._bundle)` → `Services.strings.createBundle()`
- 参照: `this._bundle`
- XPCOM: `Services.strings`

## MozSearchAutocompleteRichlistboxPopup.openAutocompletePopup()
- 位置: L174-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openAutocompletePopup()`
- 参照: `aInput.popup.hidden`

## MozSearchAutocompleteRichlistboxPopup.onPopupClick()
- 位置: L183-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MouseEvent.isInstance()`, `lazy.BrowserSearchTelemetry.recordSearchSuggestionSelectionMethod()`, `lazy.BrowserUtils.whereToOpenLink()`, `this.input.controller.getValueAt()`, `this.searchbar.doSearch()`
- 条件付き依存: `if ( aEvent.button == 0 && !aEvent.shiftKey && !aEvent.ctrlKey && !aEvent.altKey && !aEvent.metaKey )` → `this.input.controller.handleEnter()`
- 条件付き依存: `if (!(where == "tab" && params.inBackground))` → `this.closePopup()`
- 条件付き依存: `if (!(where == "tab" && params.inBackground))` → `this.input.controller.handleEscape()`
- 条件付き依存: `if (where == "tab" && params.inBackground)` → `this.searchbar.focus()`
- 参照: `AppConstants.platform`, `aEvent.altKey`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `params.inBackground`, `this.searchbar.telemetrySelectedIndex`, `this.searchbar.value`, `this.selectedIndex`

## MozSearchAutocompleteRichlistboxPopup.updateHeader()
- 位置: async L254-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.getIconURL()`, `this.bundle.formatStringFromName()`, `this.searchbarEngineName.setAttribute()`
- 条件付き依存: `if (!engine)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `lazy.SearchService.getDefaultPrivate()`
- 条件付き依存: `if (!(PrivateBrowsingUtils.isWindowPrivate(window)))` → `lazy.SearchService.getDefault()`
- 条件付き依存: `if (uri)` → `this.setAttribute()`
- 条件付き依存: `if (!(uri))` → `this.removeAttribute()`
- 参照: `engine.name`, `this.#currentEngineName`, `this.searchbarEngine.engine`

## MozSearchAutocompleteRichlistboxPopup.handleOneOffSearch()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchbar.handleSearchCommandWhere()`

## MozSearchAutocompleteRichlistboxPopup.openSearchForm()
- 位置: L306-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.oneOffButtons._whereToOpen()`, `this.searchbar.openSearchFormWhere()`

## MozSearchAutocompleteRichlistboxPopup.handleEvent()
- 位置: L320-327
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## MozSearchAutocompleteRichlistboxPopup._on_SelectedOneOffButtonChanged()
- 位置: L328-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateHeader()`, `this.updateHeader(engine).catch()`
- 参照: `console.error`, `this.oneOffButtons.selectedButton`, `this.oneOffButtons.selectedButton.engine`
