# browser/components/places/content/bookmarkProperties.js

source: browser/components/places/content/bookmarkProperties.js
source-hash: c16b1d8239147c220376beabc4e16eff10fc8638
lines: 519

## <module>
- 役割: (未記入)
- 呼び出し先: `BookmarkPropertiesPanel.onDialogLoad()`, `BookmarkPropertiesPanel.onDialogLoad() .catch()`, `BookmarkPropertiesPanel.onDialogLoad() .catch(ex => console.error(`Failed to initialize dialog: ${ex}`)) .then()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyScriptGetter()`, `console.error()`, `document.addEventListener()`, `window.sizeToContent()`

## _strings()
- 位置: L82-87
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__strings)` → `document.getElementById()`
- 参照: `this.__strings`

## BPP__getAcceptLabel()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._strings.getString()`

## BPP__getDialogTitle()
- 位置: L115-139
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._strings.getString()`
- 条件付き依存: `if (this._URIs.length)` → `this._strings.getString()`
- 条件付き依存: `if (this._action == ACTION_ADD)` → `this._strings.getString()`
- 条件付き依存: `if (this._itemType === BOOKMARK_ITEM)` → `this._strings.getString()`
- 条件付き依存: `if (this._action == ACTION_EDIT)` → `this._strings.getString()`
- 参照: `this._URIs.length`, `this._action`, `this._itemType`

## _determineItemInfo()
- 位置: async L144-219
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof this._title != "string")` → `PlacesUtils.history.fetch()`
- 条件付き依存: `if (!("uri" in dialogInfo))` → `Services.io.newURI()`
- 条件付き依存: `if (!("uri" in dialogInfo))` → `this._strings.getString()`
- 条件付き依存: `if ("URIList" in dialogInfo)` → `this._strings.getString()`
- 条件付き依存: `if (!("URIList" in dialogInfo))` → `this._strings.getString()`
- 条件付き依存: `if (!(this._action == ACTION_ADD))` → `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsFolderOrShortcut(this._node)))` → `PlacesUtils.nodeIsURI()`
- 参照: `Ci.nsIURI`, `PlacesUIUtils.defaultParentGuid`, `dialogInfo.URIList`, `dialogInfo.action`, `dialogInfo.charSet`, `dialogInfo.defaultInsertionPoint`, `dialogInfo.hiddenRows`, `dialogInfo.keyword`, `dialogInfo.node`, `dialogInfo.postData`, `dialogInfo.title`, `dialogInfo.type`, `dialogInfo.uri`, `this._URIs`, `this._action`, `this._charSet`, `this._defaultInsertionPoint`, `this._dummyItem`, `this._hiddenRows`, `this._isAddKeywordDialog`, `this._itemType`, `this._keyword`, `this._node`, `this._node.title`, `this._postData`, `this._title`, `this._uri`, `this._uri.spec`, `window.arguments`
- XPCOM: [`nsIURI`](../../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## onDialogLoad()
- 位置: async L225-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `document .getElementById()`, `document .getElementById("bookmarkpropertiesdialog") .getButton()`, `document.addEventListener()`, `document.documentElement.setAttribute()`, `this._determineItemInfo()`, `this._getDialogTitle()`, `this._getIconUrl()`, `this._initDialog()`, `this.onDialogAccept()`, `this.onDialogCancel()`, `this.onDialogUnload()`, `window.addEventListener()`
- 条件付き依存: `if (iconUrl)` → `document.documentElement.style.setProperty()`
- 参照: `acceptButton.disabled`, `document.title`

## _getIconUrl()
- 位置: L253-261
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._action`, `this._itemType`, `window.arguments`, `window.arguments[0]?.node?.icon`

## _initDialog()
- 位置: async L267-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("bookmarkpropertiesdialog") .getButton()`, `gEditItemOverlay.initPanel()`, `target.classList.contains()`, `target.hasAttribute()`, `this._element()`, `this._getAcceptLabel()`, `this._mutationObserver.observe()`, `this._promiseNewItem()`
- 条件付き依存: `if (hidden)` → `this._mutationObserver._heightsById.get()`
- 条件付き依存: `if (hidden)` → `window.resizeBy()`
- 条件付き依存: `if (!(hidden))` → `target.getBoundingClientRect()`
- 条件付き依存: `if (!(hidden))` → `this._mutationObserver._heightsById.set()`
- 条件付き依存: `if (!(hidden))` → `window.resizeBy()`
- 条件付き依存: `if (target.classList.contains("hideable") && hidden != wasHidden)` → `window.sizeToContent()`
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._inputIsValid()`
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._element("locationField").addEventListener()`
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._element()`
- 条件付き依存: `if (this._isAddKeywordDialog)` → `this._element("keywordField").addEventListener()`
- 条件付き依存: `if (this._isAddKeywordDialog)` → `this._element()`
- 参照: `acceptButton.disabled`, `acceptButton.label`, `gEditItemOverlay.readOnly`, `locationField.value`, `target.getBoundingClientRect().height`, `target.id`, `this._action`, `this._hiddenRows`, `this._isAddKeywordDialog`, `this._itemType`, `this._mutationObserver`, `this._mutationObserver._heightsById`, `this._node`, `this._node.children?.length`, `this._postData`

## BPP_handleEvent()
- 位置: L356-371
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( target.id == "editBMPanel_locationField" || target.id == "editBMPanel_keywordField" )` → `document .getElementById("bookmarkpropertiesdialog") .getButton()`
- 条件付き依存: `if ( target.id == "editBMPanel_locationField" || target.id == "editBMPanel_keywordField" )` → `document .getElementById()`
- 条件付き依存: `if ( target.id == "editBMPanel_locationField" || target.id == "editBMPanel_keywordField" )` → `this._inputIsValid()`
- 参照: `aEvent.target`, `aEvent.type`, `document .getElementById("bookmarkpropertiesdialog") .getButton("accept").disabled`, `target.id`

## BPP__element()
- 位置: L376-378
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## onDialogUnload()
- 位置: L380-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._element()`, `this._element("keywordField").removeEventListener()`, `this._element("locationField").removeEventListener()`, `this._mutationObserver.disconnect()`
- 参照: `this._mutationObserver`

## onDialogAccept()
- 位置: L391-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.commandDispatcher.focusedElement?.blur()`, `gEditItemOverlay.uninitPanel()`
- 参照: `gEditItemOverlay._bookmarkState`, `this._node.bookmarkGuid`, `window.arguments`, `window.arguments[0].bookmarkGuid`, `window.arguments[0].bookmarkState`

## onDialogCancel()
- 位置: L405-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gEditItemOverlay.uninitPanel()`

## BPP__inputIsValid()
- 位置: L416-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._containsValidURI()`, `this._element()`
- 参照: `this._element("keywordField").value.length`, `this._isAddKeywordDialog`, `this._itemType`

## BPP__containsValidURI()
- 位置: L442-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._element()`
- 条件付き依存: `if (value)` → `Services.uriFixup.getFixupURIInfo()`
- 参照: `this._element(aTextboxID).value`
- XPCOM: `Services.uriFixup`

## _getInsertionPointDetails()
- 位置: async L461-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._defaultInsertionPoint.getIndex()`
- 参照: `this._defaultInsertionPoint.guid`

## _promiseNewItem()
- 位置: async L468-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.freeze()`, `this._getInsertionPointDetails()`
- 条件付き依存: `if (this._charSet)` → `PlacesUIUtils.setCharsetForPage(this._uri, this._charSet, window).catch()`
- 条件付き依存: `if (this._charSet)` → `PlacesUIUtils.setCharsetForPage()`
- 条件付き依存: `if (this._itemType == BOOKMARK_FOLDER)` → `this._URIs.map()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `PlacesUtils.bookmarks.unsavedGuid`, `console.error`, `info.children`, `info.keyword`, `info.postData`, `info.url`, `item.title`, `item.uri`, `this._charSet`, `this._itemType`, `this._keyword`, `this._postData`, `this._title`, `this._uri`, `this._uri.spec`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)
