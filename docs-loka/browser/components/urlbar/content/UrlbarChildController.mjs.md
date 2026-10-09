# browser/components/urlbar/content/UrlbarChildController.mjs

source: browser/components/urlbar/content/UrlbarChildController.mjs
source-hash: a04f963921743cf011a84c7c298cdbe02ece57a3
lines: 889

## <module>
- 役割: (未記入)

## UrlbarChildController.logger()
- 位置: L53-60
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!UrlbarChildController.#logger)` → `UrlbarShared.getLogger()`
- 参照: `UrlbarChildController.#logger`

## UrlbarChildController.constructor()
- 位置: L105-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.usesMessagePath()`, `options.input.window.windowGlobalChild.getActor()`, `this.#parentController.setChild()`
- 参照: `lazy.UrlbarParentController`, `options.input`, `options.input.isPrivate`, `options.input.sapName`, `this.#input`, `this.#parentController`, `this.engineStore`

## UrlbarChildController.input()
- 位置: L123-125
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#input`

## UrlbarChildController.window()
- 位置: L131-133
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#input.window`

## UrlbarChildController.view()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#view`

## UrlbarChildController.parentController()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#parentController`

## UrlbarChildController.engagementEvent()
- 位置: L156-160
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#childTelemetry`, `this.#parentController`, `this.#parentController.engagementEvent`

## UrlbarChildController.userSelectionBehavior()
- 位置: L169-171
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#userSelectionBehavior`

## UrlbarChildController.userSelectionBehavior()
- 位置: L173-180
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#userSelectionBehavior`

## UrlbarChildController.setView()
- 位置: L182-184
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#view`

## UrlbarChildController.resolveFallbackNavigation()
- 位置: async L186-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#engineStoreReady()`, `this.#parentController.resolveFallbackNavigation()`

## UrlbarChildController.addListener()
- 位置: L193-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.add()`

## UrlbarChildController.removeListener()
- 位置: L200-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.delete()`

## UrlbarChildController.notifyFromWire()
- 位置: L213-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarQueryContext.fromWire()`, `params.map()`, `this.notify()`
- 参照: `param.serializedQueryContext`, `param?.serializedQueryContext`

## UrlbarChildController.notify()
- 位置: L234-271
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( notification === UrlbarShared.NOTIFICATIONS.QUERY_RESULTS && params[0].firstResultChanged )` → `this.#parentController.speculativeConnect()`
- 条件付き依存: `if (typeof listener[notification] != "undefined")` → `listener[notification]()`
- 条件付き依存: `if (typeof listener[notification] != "undefined")` → `console.error()`
- 参照: `UrlbarShared.NOTIFICATIONS.QUERY_FINISHED`, `UrlbarShared.NOTIFICATIONS.QUERY_FIRST_RESULT`, `UrlbarShared.NOTIFICATIONS.QUERY_RESULTS`, `params[0].firstResultChanged`, `params[0].id`, `params[0].results`, `this.#listeners`, `this.#queryId`

## UrlbarChildController.startQuery()
- 位置: L289-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchQuery()`, `this.#engineStoreReady()`, `this.#engineStoreReady().then()`, `this.#input.eventBufferer.queryStarting()`
- 条件付き依存: `if (this.engineStore.initialized || this.engineStore.failed)` → `this.#dispatchQuery()`
- 参照: `queryContext.id`, `this.#queryCancelled`, `this.#queryId`, `this.engineStore.failed`, `this.engineStore.initialized`

## UrlbarChildController.#dispatchQuery()
- 位置: L316-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#input.eventBufferer.queryStarting()`, `this.#parentController.startQuery()`

## UrlbarChildController.#engineStoreReady()
- 位置: async L336-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engineStore.init()`
- 参照: `this.engineStore.failed`, `this.engineStore.initialized`

## UrlbarChildController.cancelQuery()
- 位置: L347-351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#parentController.cancelQuery()`
- 参照: `this.#queryCancelled`

## UrlbarChildController.discardResults()
- 位置: L364-367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.notify()`
- 参照: `UrlbarShared.NOTIFICATIONS.QUERY_CANCELLED`, `this.#queryId`

## UrlbarChildController.handleKeyNavigation()
- 位置: L382-675
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `UrlbarPrefs.get()`, `event.preventDefault()`, `this.input.getAttribute()`, `this.input.maybeConfirmSearchModeFromResult()`, `this.logger.debug()`, `this.view.isResultMenuOpen()`, `this.view.removeAccessibleFocus()`, `this.view.shouldSpaceActivateSelectedElement()`
- 条件付き依存: `if (executeAction)` → `this.view.selectBy()`
- 条件付き依存: `if ( isMac && this.view.isOpen && event.ctrlKey && (event.key == "n" || event.key == "p") )` → `event.preventDefault()`
- 条件付き依存: `if (executeAction)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `this.input.searchModeSwitcher.handleKeyDown()`
- 条件付き依存: `if ( this.view.isOpen && this.#parentController._lastQueryContextWrapper )` → `this.view.oneOffSearchButtons?.handleKeyDown()`
- 条件付き依存: `if (this.view.isOpen)` → `this.view.close()`
- 条件付き依存: `if (!(this.view.isOpen))` → `UrlbarPrefs.get()`
- 条件付き依存: `if ( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...)` → `this.input.blur()`
- 条件付き依存: `if (!( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...))` → `this.input.getAttribute()`
- 条件付き依存: `if (!( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...))` → `this.window.isBlankPageURL()`
- 条件付き依存: `if ( // A chrome urlbar moves focus into the content document instead. this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.search...)` → `this.window.gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (!( // A chrome urlbar moves focus into the content document instead. this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.search...))` → `this.input.handleRevert()`
- 条件付き依存: `if (executeAction)` → `this.input.handleCommand()`
- 条件付き依存: `if ( this.input.sapName == "smartbar" && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getLastSelectableElement()`
- 条件付き依存: `if ( this.input.sapName == "smartbar" && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getFirstSelectableElement()`
- 条件付き依存: `if (atEnd)` → `smartbar.focusFirstActionButton()`
- 条件付き依存: `if (!(atEnd))` → `smartbar.focusLastActionButton()`
- 条件付き依存: `if (atEnd || atStart)` → `event.preventDefault()`
- 条件付き依存: `if ( UrlbarPrefs.get("scotchBonnet.enableOverride") && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getFirstSelectableElement()`
- 条件付き依存: `if ( UrlbarPrefs.get("scotchBonnet.enableOverride") && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getLastSelectableElement()`
- 条件付き依存: `if ( (event.shiftKey && this.view.selectedElement == this.view.getFirstSelectableElement()) || (!event.shiftKey && this.view.selectedElement == this.view.getLast...)` → `event.preventDefault()`
- 条件付き依存: `if ( (event.shiftKey && this.view.selectedElement == this.view.getFirstSelectableElement()) || (!event.shiftKey && this.view.selectedElement == this.view.getLast...)` → `this.focusOnUnifiedSearchButton()`
- 条件付き依存: `if (event.shiftKey)` → `this.focusOnUnifiedSearchButton()`
- 条件付き依存: `if (!(event.shiftKey))` → `this.view.selectBy()`
- 条件付き依存: `if ( !this.view.selectedElement && this.input.focusedViaMousedown )` → `event.preventDefault()`
- 条件付き依存: `if ( // Even if the view is closed, we may be waiting results, and in // such a case we don't want to tab out of the urlbar. (this.view.isOpen || !executeAction)...)` → `event.preventDefault()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.keyEventMovesCaret()`
- 条件付き依存: `if (executeAction)` → `this.input.startQuery()`
- 条件付き依存: `if ( this.input.searchMode && this.input.selectionStart == 0 && this.input.selectionEnd == 0 && !event.shiftKey )` → `this.input.startQuery()`
- 条件付き依存: `if (event.shiftKey)` → `this.#dismissSelectedResult()`
- 条件付き依存: `if (!executeAction || this.#dismissSelectedResult(event))` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_END`, `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_HOME`, `KeyEvent.DOM_VK_LEFT`, `KeyEvent.DOM_VK_PAGE_DOWN`, `KeyEvent.DOM_VK_PAGE_UP`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_RIGHT`, `KeyEvent.DOM_VK_SPACE`, `KeyEvent.DOM_VK_TAB`, `KeyEvent.DOM_VK_UP`, `UrlbarShared.PAGE_UP_DOWN_DELTA`, `UrlbarShared.RESULT_SOURCE.ACTIONS`, `event.altKey`, `event.ctrlKey`, `event.key`, `event.keyCode`, `event.shiftKey`, `queryContext.searchString`, `this.#parentController._lastQueryContextWrapper`, `this.input`, `this.input.focusedViaMousedown`, `this.input.sapName`, `this.input.searchMode`, `this.input.searchMode?.isPreview`, `this.input.searchMode?.source`, `this.input.selectionEnd`, `this.input.selectionStart`, `this.input.value`, `this.input.view.oneOffSearchButtons`, `this.input.view.oneOffSearchButtons.selectedButton`, `this.userSelectionBehavior`, `this.view.allowEmptySelection`, `this.view.isOpen`, `this.view.selectedElement`, `this.view.selectedRowIndex`, `this.view.visibleRowCount`, `this.window.gBrowser`, `this.window.gBrowser.currentURI.spec`

## UrlbarChildController.#dismissSelectedResult()
- 位置: L689-719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectedElement?.classList.contains()`, `this.engagementEvent.record()`, `this.input.getSearchSource()`
- 条件付き依存: `if (!this.#parentController._lastQueryContextWrapper)` → `console.error()`
- 参照: `queryContext.searchString`, `result.autofill`, `result.heuristic`, `this.#parentController._lastQueryContextWrapper`, `this.input.view`, `this.input.view.selectedResult`

## UrlbarChildController.keyEventMovesCaret()
- 位置: L734-759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_UP`, `event.keyCode`, `this.input.selectionEnd`, `this.input.selectionStart`, `this.input.value.length`, `this.view.isOpen`

## UrlbarChildController.isCanonizeKeyboardEvent()
- 位置: L769-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `UrlbarPrefs.get()`, `UrlbarShared.isInstance()`
- 参照: `(event)._disableCanonization`, `KeyEvent.DOM_VK_RETURN`, `keyEvent.ctrlKey`, `keyEvent.keyCode`, `keyEvent.metaKey`, `this.#input.sapName`

## UrlbarChildController.whereToOpen()
- 位置: L797-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isInstance()`, `event.getModifierState()`
- 条件付き依存: `if (!( isKeyboardEvent && (event.altKey || event.getModifierState("AltGraph")) ))` → `this.isCanonizeKeyboardEvent()`
- 条件付き依存: `if (!(this.isCanonizeKeyboardEvent(event)))` → `UrlbarContentUtils.whereToOpenLink()`
- 参照: `event.altKey`, `event.shiftKey`, `this.#input.sapName`, `this.window.gBrowser?.selectedTab.isEmpty`

## UrlbarChildController.focusOnUnifiedSearchButton()
- 位置: L840-872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `switcher.addEventListener()`, `switcher.focus()`, `this.input.contains()`, `this.input.hasAttribute()`, `this.input.inputField.addEventListener()`, `this.input.inputField.removeEventListener()`, `this.input.querySelector()`, `this.input.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if ( this.input.hasAttribute("focused") && !this.input.contains(relatedTarget) )` → `this.input.inputField.dispatchEvent()`
- 参照: `e.relatedTarget`, `this.input`

## UrlbarChildController.maybeInitEngineStore()
- 位置: L874-880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#parentController.maybeInitEngineStore()`
- 参照: `this.#parentController`

## UrlbarChildController.updateEngineStore()
- 位置: L885-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engineStore.receive()`
