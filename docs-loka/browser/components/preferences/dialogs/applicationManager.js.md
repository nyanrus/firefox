# browser/components/preferences/dialogs/applicationManager.js

source: browser/components/preferences/dialogs/applicationManager.js
source-hash: 530532284096ede4b6cad0a5f958eee073b74791
lines: 137

## <module>
- 役割: (未記入)
- 呼び出し先: `gAppManagerDialog.onLoad()`, `window.addEventListener()`

## onLoad()
- 位置: L10-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 参照: `document.mozSubdialogReady`

## init()
- 位置: async L14-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("cmd_remove") .addEventListener()`, `document.addEventListener()`, `document.createDocumentFragment()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.translateElements()`, `gAppManagerDialog.onOK()`, `gMainPane._getIconURLForHandlerApp()`, `gMainPane.isValidHandlerApp()`, `image.setAttribute()`, `item.appendChild()`, `label.setAttribute()`, `list.addEventListener()`, `list.append()`, `listFragment.append()`, `this.handlerInfo.possibleApplicationHandlers.enumerate()`, `this.onSelect()`, `this.remove()`
- 条件付き依存: `if (typeDescription.id)` → `MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (typeDescription.id)` → `document.l10n.formatValue()`
- 条件付き依存: `if (this.handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this.handlerInfo.wrappedHandlerInfo instanceof Ci.nsIMIMEInfo))` → `document.l10n.setAttributes()`
- 参照: `Ci.nsIMIMEInfo`, `app.name`, `item.app`, `list.selectedIndex`, `this.handlerInfo`, `this.handlerInfo.typeDescription.raw`, `this.handlerInfo.wrappedHandlerInfo`, `typeDescription.args`, `typeDescription.id`, `typeDescription.raw`, `window.arguments`, `window.parent.gMainPane`
- XPCOM: [`nsIMIMEInfo`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)

## appManager_onOK()
- 位置: L82-90
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._removed.length)` → `this.handlerInfo.removePossibleApplicationHandler()`
- 条件付き依存: `if (this._removed.length)` → `this.handlerInfo.store()`
- 参照: `this._removed`, `this._removed.length`

## appManager_remove()
- 位置: L92-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `element.remove()`, `list.removeItemFromSelection()`, `this._removed.push()`
- 条件付き依存: `if (list.itemCount == 0)` → `document.getElementById()`
- 参照: `document.getElementById("appDetails").hidden`, `list.itemCount`, `list.selectedIndex`, `list.selectedItem`, `list.selectedItem.app`

## appManager_onSelect()
- 位置: L112-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (!list.selectedItem)` → `document.getElementById()`
- 参照: `Ci.nsILocalHandlerApp`, `Ci.nsIWebHandlerApp`, `app.executable.path`, `app.uriTemplate`, `document.getElementById("appLocation").value`, `document.getElementById("remove").disabled`, `list.selectedItem`, `list.selectedItem.app`
- XPCOM: [`nsILocalHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../../netwerk/mime/nsIMIMEInfo.idl.md)
