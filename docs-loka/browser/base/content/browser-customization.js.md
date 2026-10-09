# browser/base/content/browser-customization.js

source: browser/base/content/browser-customization.js
source-hash: 11f9486794c1a6d0ba2e0d2bf923effa67788c81
lines: 182

## <module>
- 役割: (未記入)

## handleEvent()
- 位置: L11-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._afterCustomization()`, `this._customizationStarting()`
- 参照: `aEvent.type`

## isCustomizing()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`

## _customizationStarting()
- 位置: L26-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesToolbarHelper.customizeStart()`, `Services.policies.isAllowed()`, `UpdateUrlbarSearchSplitterState()`, `childNode.setAttribute()`, `document.getElementById()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document.documentElement.setAttribute()`
- 参照: `menubar.children`
- XPCOM: `Services.policies`

## _afterCustomization()
- 位置: L42-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesToolbarHelper.customizeDone()`, `UpdateUrlbarSearchSplitterState()`, `XULBrowserWindow.asyncUpdateUI()`, `childNode.removeAttribute()`, `document.getElementById()`, `gBrowser.selectedBrowser.focus()`, `gURLBar.setURI()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `updateEditUIVisibility()`
- 参照: `AppConstants.platform`, `menubar.children`

## _node()
- 位置: L66-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._node`

## active()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.contextMenu`

## init()
- 位置: L78-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutoHideMenubar._node.addEventListener()`, `AutoHideMenubar._node.getAttribute()`, `document.getElementById()`, `event.target.closest()`, `this.contextMenu.addEventListener()`
- 参照: `this.contextMenu`

## handleEvent()
- 位置: L90-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutoHideMenubar._node.removeEventListener()`, `AutoHideMenubar._setInactiveAsync()`, `this.contextMenu.removeEventListener()`
- 参照: `event.type`, `this.contextMenu`

## init()
- 位置: L107-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._node.addEventListener()`, `this._node.hasAttribute()`
- 条件付き依存: `if (this._node.hasAttribute("autohide"))` → `this._enable()`

## _updateState()
- 位置: L114-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._node.hasAttribute()`
- 条件付き依存: `if (this._node.hasAttribute("autohide"))` → `this._enable()`
- 条件付き依存: `if (!(this._node.hasAttribute("autohide")))` → `this._disable()`

## _enable()
- 位置: L128-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._node.addEventListener()`, `this._node.setAttribute()`
- 参照: `this._events`

## _disable()
- 位置: L135-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._node.removeEventListener()`, `this._setActive()`
- 参照: `this._events`

## handleEvent()
- 位置: L142-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setActive()`, `this._updateState()`
- 条件付き依存: `if (event.button == 2)` → `this._contextMenuListener.init()`
- 条件付き依存: `if (!this._contextMenuListener.active)` → `this._setInactiveAsync()`
- 参照: `event.button`, `event.type`, `this._contextMenuListener.active`

## _setInactiveAsync()
- 位置: L165-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `this._node.hasAttribute()`
- 条件付き依存: `if (this._node.hasAttribute("autohide"))` → `this._node.setAttribute()`
- 参照: `this._inactiveTimeout`

## _setActive()
- 位置: L174-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._node.removeAttribute()`
- 条件付き依存: `if (this._inactiveTimeout)` → `clearTimeout()`
- 参照: `this._inactiveTimeout`
