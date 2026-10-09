# browser/base/content/browser-toolbarKeyNav.js

source: browser/base/content/browser-toolbarKeyNav.js
source-hash: fb43a8aef29c087a9d7e0e0390fa0d932319321e
lines: 463

## <module>
- 役割: (未記入)

## _isButton()
- 位置: L38-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElem.getAttribute()`
- 参照: `aElem.localName`, `aElem.namespaceURI`

## _getWalker()
- 位置: L54-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createTreeWalker()`
- 参照: `NodeFilter.SHOW_ELEMENT`, `aRoot._toolbarKeyNavWalker`

## filter()
- 位置: L59-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.checkVisibility()`, `document.getElementById()`, `document.getElementById("urlbar").getAttribute()`, `this._isButton()`, `window.windowUtils.getBoundsWithoutFlushing()`
- 参照: `NodeFilter.FILTER_ACCEPT`, `NodeFilter.FILTER_REJECT`, `NodeFilter.FILTER_SKIP`, `aNode.disabled`, `aNode.id`, `aNode.tagName`, `bounds.width`

## _initTabStops()
- 位置: L107-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aRoot.getElementsByTagName()`, `stop.addEventListener()`, `stop.setAttribute()`

## init()
- 位置: L117-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `document.getElementById()`, `this._initTabStops()`, `toolbar.addEventListener()`, `toolbar.setAttribute()`
- 参照: `this._initialized`, `this.kToolbars`

## uninit()
- 位置: L135-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `document.getElementById()`, `stop.removeEventListener()`, `toolbar.getElementsByTagName()`, `toolbar.removeAttribute()`, `toolbar.removeEventListener()`
- 参照: `this._initialized`, `this.kToolbars`

## onWidgetAdded()
- 位置: L153-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._initTabStops()`, `this.kToolbars.includes()`

## _focusButton()
- 位置: L164-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aButton.addEventListener()`, `aButton.focus()`, `aButton.hasAttribute()`, `aButton.setAttribute()`
- 条件付き依存: `if (aButton.hasAttribute("tabindex"))` → `aButton.focus()`

## _onButtonBlur()
- 位置: L184-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.getAttribute()`, `aEvent.target.removeAttribute()`, `aEvent.target.removeEventListener()`
- 参照: `aEvent.target`, `document.activeElement`

## _onTabStopFocus()
- 位置: L199-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.closest()`, `button?.getAttribute()`, `this._focusButton()`, `this._getWalker()`, `this._isButton()`, `walker.nextNode()`
- 条件付き依存: `if (oldFocus)` → `oldFocus.compareDocumentPosition()`
- 条件付き依存: `if (oldFocus)` → `this._isButton()`
- 条件付き依存: `if (this._isFocusMovingBackward && oldFocus && this._isButton(oldFocus))` → `document.commandDispatcher.rewindFocus()`
- 条件付き依存: `if (!button || !this._isButton(button))` → `gNavToolbox.contains()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `Array.from()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `gNavToolbox.querySelectorAll()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `allStops.indexOf()`
- 条件付き依存: `if ( this._isFocusMovingBackward && (!oldFocus || !gNavToolbox.contains(oldFocus)) )` → `allStops[earlierVisibleStopIndex].closest()`
- 条件付き依存: `if (this._isFocusMovingBackward)` → `document.commandDispatcher.rewindFocus()`
- 条件付き依存: `if (!(this._isFocusMovingBackward))` → `document.commandDispatcher.advanceFocus()`
- 参照: `Node.DOCUMENT_POSITION_PRECEDING`, `aEvent.relatedTarget`, `aEvent.target`, `stopToolbar.collapsed`, `this._isFocusMovingBackward`, `walker.currentNode`

## navigateButtons()
- 位置: L265-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._focusButton()`, `this._getWalker()`
- 条件付き依存: `if (aPrevious)` → `walker.previousNode()`
- 条件付き依存: `if (!(aPrevious))` → `walker.nextNode()`
- 参照: `document.activeElement`, `newFocus.tagName`, `walker.currentNode`

## _onKeyDown()
- 位置: L283-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.preventDefault()`, `focus.closest()`, `this._clearSearch()`, `this._isButton()`, `this.navigateButtons()`
- 条件付き依存: `if ( aEvent.key != " " && aEvent.key.length == 1 && this._isButton(focus) && // Don't handle characters if the user is focused in a panel anchored // to the tool...)` → `this._onSearchChar()`
- 参照: `aEvent.altKey`, `aEvent.controlKey`, `aEvent.currentTarget`, `aEvent.key`, `aEvent.key.length`, `aEvent.metaKey`, `aEvent.shiftKey`, `document.activeElement`, `window.RTL_UI`

## _clearSearch()
- 位置: L324-330
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._clearSearchTimeout)` → `clearTimeout()`
- 参照: `this._clearSearchTimeout`, `this._searchText`

## _onSearchChar()
- 位置: L332-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aChar.toLowerCase()`, `setTimeout()`, `this._clearSearch.bind()`, `this._doesSearchMatch()`, `this._getWalker()`, `walker.firstChild()`, `walker.nextNode()`
- 条件付き依存: `if (this._clearSearchTimeout)` → `clearTimeout()`
- 条件付き依存: `if (this._doesSearchMatch(newFocus))` → `this._focusButton()`
- 参照: `document.activeElement`, `this._clearSearchTimeout`, `this._searchText`, `this.kSearchClearTimeout`, `walker.currentNode`, `walker.root`

## _doesSearchMatch()
- 位置: L382-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aElem.getAttribute()`, `label.startsWith()`, `label.toLowerCase()`, `this._isButton()`
- 参照: `this._searchText`

## _onKeyPress()
- 位置: L401-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `focus.dispatchEvent()`, `focus.getAttribute()`, `focus.hasAttribute()`, `this._isButton()`
- 参照: `aEvent.altKey`, `aEvent.ctrlKey`, `aEvent.key`, `aEvent.metaKey`, `aEvent.shiftKey`, `document.activeElement`, `focus.localName`, `focus.open`, `focus.tagName`

## handleEvent()
- 位置: L446-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onButtonBlur()`, `this._onKeyDown()`, `this._onKeyPress()`, `this._onTabStopFocus()`
- 参照: `aEvent.type`
