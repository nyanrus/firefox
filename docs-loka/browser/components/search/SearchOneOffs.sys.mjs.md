# browser/components/search/SearchOneOffs.sys.mjs

source: browser/components/search/SearchOneOffs.sys.mjs
source-hash: 7f6f1f35b2a1107e3a84b267831359042ae8c863
lines: 1183

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SearchOneOffs.constructor()
- 位置: L44-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.obs.addObserver()`, `aEvent.stopPropagation()`, `this.addEventListener()`, `this.container.appendChild()`, `this.contextMenuPopup.addEventListener()`, `this.querySelector()`, `this.window.MozXULElement.parseXULToFragment()`
- 参照: `container.documentGlobal`, `container.ownerDocument`, `this.QueryInterface`, `this._engineInfo`, `this._popup`, `this._query`, `this._rebuilding`, `this._selectedButton`, `this._textbox`, `this._textboxWidth`, `this.buttons`, `this.container`, `this.contextMenuPopup`, `this.disableOneOffsHorizontalKeyNavigation`, `this.document`, `this.header`, `this.settingsButton`, `this.telemetryOrigin`, `this.window`
- XPCOM: `Services.obs`

## listener()
- 位置: L108-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.stopPropagation()`

## SearchOneOffs.addEventListener()
- 位置: L136-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.addEventListener()`

## SearchOneOffs.removeEventListener()
- 位置: L140-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.removeEventListener()`

## SearchOneOffs.dispatchEvent()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.dispatchEvent()`

## SearchOneOffs.getAttribute()
- 位置: L148-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.getAttribute()`

## SearchOneOffs.hasAttribute()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.hasAttribute()`

## SearchOneOffs.setAttribute()
- 位置: L156-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.setAttribute()`

## SearchOneOffs.querySelector()
- 位置: L160-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.container.querySelector()`

## SearchOneOffs.handleEvent()
- 位置: L164-171
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## SearchOneOffs.willHide()
- 位置: async L177-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getEngineInfo()`
- 参照: `engineInfo.default.name`, `engineInfo.engines`, `engineInfo.engines.length`, `engineInfo.engines[0].name`, `engineInfo.willHide`, `this._engineInfo.willHide`, `this._engineInfo?.willHide`

## SearchOneOffs.invalidateCache()
- 位置: L194-198
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._engineInfo`, `this._rebuilding`

## SearchOneOffs.buttonWidth()
- 位置: L206-208
- 役割: (未記入)
- 触るとき: (未記入)

## SearchOneOffs.popup()
- 位置: L216-233
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._popup)` → `this._popup.removeEventListener()`
- 条件付き依存: `if (val)` → `val.addEventListener()`
- 条件付き依存: `if (val && val.state != "closed")` → `this._rebuild()`
- 参照: `this._popup`, `val.state`

## SearchOneOffs.popup()
- 位置: L235-237
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._popup`

## SearchOneOffs.textbox()
- 位置: L248-256
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._textbox)` → `this._textbox.removeEventListener()`
- 条件付き依存: `if (val)` → `val.addEventListener()`
- 参照: `this._textbox`

## SearchOneOffs.style()
- 位置: L258-260
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.container.style`

## SearchOneOffs.textbox()
- 位置: L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._textbox`

## SearchOneOffs.query()
- 位置: L274-292
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isViewOpen)` → `this.selectedButton.classList.contains()`
- 条件付き依存: `if (this.isViewOpen)` → `this.hasAttribute()`
- 参照: `this._query`, `this.isViewOpen`, `this.selectedButton`, `this.settingsButton`

## SearchOneOffs.query()
- 位置: L294-296
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._query`

## SearchOneOffs.selectedButton()
- 位置: L305-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 条件付き依存: `if (previousButton)` → `previousButton.removeAttribute()`
- 条件付き依存: `if (val)` → `val.toggleAttribute()`
- 条件付き依存: `if (val)` → `this.textbox.setAttribute()`
- 条件付き依存: `if (!(val))` → `this.textbox.getAttribute()`
- 条件付き依存: `if (!(val))` → `active.includes()`
- 条件付き依存: `if (active && active.includes("-engine-one-off-item-"))` → `this.textbox.removeAttribute()`
- 参照: `this._selectedButton`, `this.textbox`, `val.id`

## SearchOneOffs.selectedButton()
- 位置: L329-331
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._selectedButton`

## SearchOneOffs.selectedButtonIndex()
- 位置: L340-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSelectableButtons()`
- 参照: `this.selectedButton`

## SearchOneOffs.selectedButtonIndex()
- 位置: L345-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSelectableButtons()`
- 参照: `buttons.length`, `this._selectedButton`

## SearchOneOffs.getEngineInfo()
- 位置: async L355-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await lazy.SearchService.getVisibleEngines()).filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SearchService.getVisibleEngines()`, `this.getAttribute()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(this.window))` → `lazy.SearchService.getDefaultPrivate()`
- 条件付き依存: `if (!(lazy.PrivateBrowsingUtils.isWindowPrivate(this.window)))` → `lazy.SearchService.getDefault()`
- 参照: `defaultEngine.name`, `e.hideOneOffButton`, `e.name`, `this._engineInfo`, `this.window`

## SearchOneOffs.observe()
- 位置: L390-409
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aTopic != "browser-search-service" || aData == "engines-reloaded")` → `this.invalidateCache()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `engine.getIconURL().then()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `engine.getIconURL()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `this.getSelectableButtons(false) .find(b => b.engine?.id == engine.id) ?.setAttribute()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `this.getSelectableButtons(false) .find()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `this.getSelectableButtons()`
- 参照: `aSubject.wrappedJSObject`, `b.engine?.id`, `engine.id`

## SearchOneOffs._maxInlineAddEngines()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)

## SearchOneOffs._rebuild()
- 位置: async L418-432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.__rebuild()`, `this.dispatchEvent()`
- 参照: `this._rebuilding`

## SearchOneOffs.__rebuild()
- 位置: async L437-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OpenSearchManager.getInstallableEngines()`, `this._rebuildEngineList()`, `this.buttons.firstElementChild.remove()`, `this.buttons.setAttribute()`, `this.getEngineInfo()`, `this.hasAttribute()`, `this.header.querySelector()`, `this.willHide()`
- 条件付き依存: `if (this.popup && this._textbox)` → `this.window.promiseDocumentFlushed()`
- 参照: `(await this.getEngineInfo()).engines`, `addEngines.length`, `headerText.id`, `this._addEngines`, `this._engineInfo.domWasUpdated`, `this._engineInfo?.domWasUpdated`, `this._textbox`, `this._textbox.clientWidth`, `this._textboxWidth`, `this.buttons.firstElementChild`, `this.container.hidden`, `this.popup`, `this.settingsButton.id`, `this.telemetryOrigin`, `this.window.gBrowser.selectedBrowser`

## SearchOneOffs._rebuildEngineList()
- 位置: async L515-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `button.classList.add()`, `button.setAttribute()`, `engine.getIconURL()`, `this._buttonIDForEngine()`, `this.buttons.appendChild()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`, `this.setTooltipForEngineButton()`
- 条件付き依存: `if (engine.icon)` → `button.setAttribute()`
- 参照: `addEngines.length`, `button.engine`, `button.id`, `engine.icon`, `engine.title`, `engine.uri`, `engines.length`, `this._maxInlineAddEngines`

## SearchOneOffs._buttonIDForEngine()
- 位置: L554-560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._engineInfo.engines.indexOf()`
- 参照: `this.telemetryOrigin`

## SearchOneOffs.getSelectableButtons()
- 位置: L562-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buttons.querySelectorAll()`
- 条件付き依存: `if (aIncludeNonEngineButtons)` → `buttons.push()`
- 参照: `this.settingsButton`

## SearchOneOffs._whereToOpen()
- 位置: L586-617
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aForceNewTab)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(aForceNewTab))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(aForceNewTab))` → `KeyboardEvent.isInstance()`
- 条件付き依存: `if (!(aForceNewTab))` → `MouseEvent.isInstance()`
- 条件付き依存: `if (!(aForceNewTab))` → `aEvent.getModifierState()`
- 参照: `aEvent.altKey`, `aEvent.button`, `this.window.gBrowser.selectedTab.isEmpty`
- XPCOM: `Services.prefs`

## SearchOneOffs.advanceSelection()
- 位置: L638-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSelectableButtons()`
- 条件付き依存: `if (this.selectedButton)` → `buttons.indexOf()`
- 参照: `buttons.length`, `this.selectedButton`

## SearchOneOffs.handleKeyDown()
- 位置: L688-703
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handleKeyDown()`
- 条件付き依存: `if (handled)` → `event.preventDefault()`
- 条件付き依存: `if (handled)` → `event.stopPropagation()`
- 参照: `this.hasView`

## SearchOneOffs._handleKeyDown()
- 位置: L705-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.getModifierState()`, `this.selectedButton.classList.contains()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_TAB && !event.getModifierState("Alt") && !event.getModifierState("AltGraph") && !event.getModifierState("Control") && !even...)` → `this.getAttribute()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_TAB && !event.getModifierState("Alt") && !event.getModifierState("AltGraph") && !event.getModifierState("Control") && !even...)` → `this.getSelectableButtons()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_TAB && !event.getModifierState("Alt") && !event.getModifierState("AltGraph") && !event.getModifierState("Control") && !even...)` → `this.advanceSelection()`
- 条件付き依存: `if (event.altKey)` → `this.advanceSelection()`
- 条件付き依存: `if (numListItems == 0)` → `this.advanceSelection()`
- 条件付き依存: `if (this.selectedViewIndex == 0)` → `this.advanceSelection()`
- 条件付き依存: `if (!this.selectedButton)` → `this.advanceSelection()`
- 条件付き依存: `if (event.keyCode == KeyboardEvent.DOM_VK_UP)` → `this.advanceSelection()`
- 条件付き依存: `if (this.selectedButton)` → `this.getSelectableButtons()`
- 条件付き依存: `if (this.selectedButton)` → `this.advanceSelection()`
- 条件付き依存: `if ( this.selectedButton && this.selectedButton.engine && !this.disableOneOffsHorizontalKeyNavigation )` → `this.advanceSelection()`
- 参照: `KeyEvent.DOM_VK_RIGHT`, `KeyEvent.DOM_VK_TAB`, `KeyboardEvent.DOM_VK_DOWN`, `KeyboardEvent.DOM_VK_LEFT`, `KeyboardEvent.DOM_VK_RIGHT`, `KeyboardEvent.DOM_VK_UP`, `buttons.length`, `event.altKey`, `event.keyCode`, `event.shiftKey`, `this.container.hidden`, `this.disableOneOffsHorizontalKeyNavigation`, `this.getSelectableButtons(true).length`, `this.selectedButton`, `this.selectedButton.engine`, `this.selectedButton.open`, `this.selectedButtonIndex`, `this.selectedViewIndex`, `this.textbox`, `this.textbox.value`

## SearchOneOffs.eventTargetIsAOneOff()
- 位置: L899-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Element.isInstance()`, `KeyboardEvent.isInstance()`, `MouseEvent.isInstance()`, `target.classList.contains()`, `this.window.XULCommandEvent.isInstance()`
- 参照: `event.originalTarget`, `this.selectedButton`

## SearchOneOffs.hasView()
- 位置: L932-934
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.popup`

## SearchOneOffs.isViewOpen()
- 位置: L939-942
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.popup`, `this.popup.popupOpen`

## SearchOneOffs.selectedViewIndex()
- 位置: L947-950
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.popup.selectedIndex`

## SearchOneOffs.selectedViewIndex()
- 位置: L958-961
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.popup.selectedIndex`

## SearchOneOffs.closeView()
- 位置: L966-968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.popup.hidePopup()`

## SearchOneOffs.handleSearchCommand()
- 位置: L981-985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._whereToOpen()`, `this.popup.handleOneOffSearch()`

## SearchOneOffs.setTooltipForEngineButton()
- 位置: L994-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.setAttribute()`
- 参照: `button.engine.name`

## SearchOneOffs._on_mousedown()
- 位置: L1000-1005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`

## SearchOneOffs._on_click()
- 位置: L1007-1030
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleSearchCommand()`
- 条件付き依存: `if (event.shiftKey)` → `this.popup.openSearchForm()`
- 参照: `button.engine`, `event.button`, `event.originalTarget`, `event.shiftKey`, `this.selectedButton`, `this.textbox.value`

## SearchOneOffs._on_command()
- 位置: async L1032-1118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.classList.contains()`
- 条件付き依存: `if (target == this.settingsButton)` → `this.window.openPreferences()`
- 条件付き依存: `if (target == this.settingsButton)` → `this.closeView()`
- 条件付き依存: `if (target.classList.contains("searchbar-engine-one-off-add-engine"))` → `lazy.SearchUIUtils.addOpenSearchEngine()`
- 条件付き依存: `if (target.classList.contains("searchbar-engine-one-off-add-engine"))` → `target.getAttribute()`
- 条件付き依存: `if (result)` → `this._rebuild()`
- 条件付き依存: `if (target.classList.contains("search-one-offs-context-open-in-new-tab"))` → `target.closest()`
- 条件付き依存: `if (this.textbox.value)` → `this.handleSearchCommand()`
- 条件付き依存: `if (!(this.textbox.value))` → `this.popup.openSearchForm()`
- 条件付き依存: `if ( target.classList.contains("search-one-offs-context-set-default") || isPrivateButton )` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( target.classList.contains("search-one-offs-context-set-default") || isPrivateButton )` → `target.closest()`
- 条件付き依存: `if ( target.classList.contains("search-one-offs-context-set-default") || isPrivateButton )` → `this.getAttribute()`
- 条件付き依存: `if ( !this.getAttribute("includecurrentengine") && isPrivateButton == isPrivateWin )` → `currentEngine.getIconURL()`
- 条件付き依存: `if ( !this.getAttribute("includecurrentengine") && isPrivateButton == isPrivateWin )` → `button.setAttribute()`
- 条件付き依存: `if (isPrivateButton)` → `lazy.SearchService.setDefaultPrivate()`
- 条件付き依存: `if (!(isPrivateButton))` → `lazy.SearchService.setDefault()`
- 参照: `button.engine`, `console.error`, `currentEngine.name`, `event.target`, `lazy.SearchService`, `lazy.SearchService.CHANGE_REASON.USER_SEARCHBAR_CONTEXT`, `target.closest("menupopup")._triggerButton`, `this.selectedButton`, `this.selectedButton.engine`, `this.settingsButton`, `this.textbox.value`, `this.window`, `this.window.gBrowser.selectedBrowser.browsingContext`

## SearchOneOffs._on_contextmenu()
- 位置: L1120-1165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `event.preventDefault()`, `target.classList.contains()`, `this.contextMenuPopup .querySelector()`, `this.contextMenuPopup .querySelector(".search-one-offs-context-set-default") .setAttribute()`, `this.contextMenuPopup.openPopupAtScreen()`, `this.contextMenuPopup.querySelector()`
- 条件付き依存: `if ( !target.classList.contains("searchbar-engine-one-off-item") || target.classList.contains("search-setting-button") )` → `event.preventDefault()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "browser.search.separatePrivateDefault.featureGate", false ) && Services.prefs.getBoolPref( "browser.search.separatePrivateDefau...)` → `privateDefaultItem.setAttribute()`
- 参照: `event.originalTarget`, `event.screenX`, `event.screenY`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `privateDefaultItem.hidden`, `target.engine`, `this.contextMenuPopup._triggerButton`
- XPCOM: `Services.prefs`

## SearchOneOffs._on_input()
- 位置: L1167-1173
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.target.oneOffSearchQuery`, `event.target.value`, `this.query`

## SearchOneOffs._on_popupshowing()
- 位置: L1175-1177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._rebuild()`

## SearchOneOffs._on_popuphidden()
- 位置: L1179-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectedButton`
