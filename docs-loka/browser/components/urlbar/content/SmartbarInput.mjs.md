# browser/components/urlbar/content/SmartbarInput.mjs

source: browser/components/urlbar/content/SmartbarInput.mjs
source-hash: 62b27dc8d0cce96ec4382194406edcedd55f7039
lines: 8002

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Promise.resolve()`, `XPCOMUtils.declareLazy()`, `customElements.define()`

## logger()
- 位置: L97-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getLogger()`

## getBoundsWithoutFlushing()
- 位置: L106-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.documentGlobal.windowUtils.getBoundsWithoutFlushing()`

## px()
- 位置: L108-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `number.toFixed()`

## SmartbarInput.#markup()
- 位置: L153-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`

## SmartbarInput.observedAttributes()
- 位置: L232-234
- 役割: (未記入)
- 触るとき: (未記入)

## SmartbarInput.fragment()
- 位置: L244-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.importNode()`
- 条件付き依存: `if (!this.#fragment)` → `window.MozXULElement.parseXULToFragment()`
- 参照: `this.#fragment`, `this.#markup`

## SmartbarInput.#popoverAnchor()
- 位置: L286-288
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.parentNode`

## SmartbarInput.constructor()
- 位置: L365-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.addObserver()`, `UrlbarPrefs.removeObserver()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `super()`, `window.addEventListener()`
- 条件付き依存: `if (!this.window.gBrowser)` → `logger().debug()`
- 条件付き依存: `if (!this.window.gBrowser)` → `logger()`
- 参照: `this.document`, `this.documentGlobal`, `this.isPrivate`, `this.window`, `this.window.document`, `this.window.gBrowser`, `window.browsingContext.topChromeWindow`

## SmartbarInput.#populateSlots()
- 位置: L393-420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `slot.getAttribute()`, `slot.parentNode.insertBefore()`, `slot.remove()`, `this._searchModeIndicator?.querySelector()`, `this.querySelector()`, `this.querySelectorAll()`
- 参照: `this._identityBox`, `this._revertButton`, `this._searchModeIndicator`, `this._searchModeIndicatorClose`, `this._searchModeIndicatorTitle`

## SmartbarInput.#initOnce()
- 位置: L425-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `this._setPlaceholder()`, `this.appendChild()`, `this.controller.addListener()`, `this.controller.maybeInitEngineStore()`, `this.dispatchEvent()`, `this.documentGlobal.requestAnimationFrame()`, `this.getAttribute()`, `this.querySelector()`
- 条件付き依存: `if (document.readyState === "loading")` → `document.addEventListener()`
- 条件付き依存: `if (document.readyState === "loading")` → `this.#populateSlots()`
- 条件付き依存: `if (!(document.readyState === "loading"))` → `this.#populateSlots()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#ensureSmartbarEditor()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.querySelector()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this._inputCta.addEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.addEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#findWebsiteContextChipsContainer()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#updateContextChips()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#updateCtaSearchEngineInfo()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#initEngineStoreAfterPaint().then()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#initEngineStoreAfterPaint()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#deferUpdatePlaceholder()`
- 参照: `SmartbarInput.fragment`, `document.readyState`, `smartbarGlow.referenceElement`, `this.#isAddressbar`, `this.#isSmartbarMode`, `this.#sapName`, `this._inputContainer`, `this._inputCta`, `this.controller`, `this.eventBufferer`, `this.inputField`, `this.panel`, `this.searchModeSwitcher`, `this.smartbarAction`, `this.view`

## SmartbarInput.get()
- 位置: L505-507
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.inputField`

## SmartbarInput.set()
- 位置: L508-510
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.inputField`

## SmartbarInput.attributeChangedCallback()
- 位置: L538-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePopover()`

## SmartbarInput.connectedCallback()
- 位置: L546-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#init()`, `this.getAttribute()`

## SmartbarInput.#init()
- 位置: L557-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `this.#initContextMenuItems()`, `this.#updatePopoverAnchor()`, `this._addObservers()`, `this._initCopyCutController()`, `this._inputContainer.addEventListener()`, `this.addEventListener()`, `this.closest()`, `this.inputField.addEventListener()`, `this.searchModeSwitcher.connect()`, `this.view.panel.addEventListener()`, `this.window.addEventListener()`, `this.window.document.documentElement.hasAttribute()`
- 条件付き依存: `if (!this.controller)` → `this.#initOnce()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `this.parentNode.setAttribute()`
- 条件付き依存: `if ( !this.window.toolbar.visible || this.window.document.documentElement.hasAttribute("taskbartab") || this.readOnly )` → `this.#releasePopoverAnchor()`
- 条件付き依存: `if (UrlbarContentUtils.getPlatform() == "win")` → `this.window.addEventListener()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.addGBrowserListeners()`
- 条件付き依存: `if (this.controller.engineStore.initialized)` → `this.searchModeSwitcher.updateSearchIcon()`
- 条件付き依存: `if (this.controller.engineStore.initialized)` → `this.updatePlaceholder()`
- 条件付き依存: `if (!(this.controller.engineStore.initialized))` → `this.#initPlaceholderFromPref()`
- 参照: `SmartbarInput.#inputFieldEvents`, `this.#canOpenPopover`, `this.controller`, `this.controller.engineStore.initialized`, `this.readOnly`, `this.sapName`, `this.window.gBrowser`, `this.window.toolbar.visible`

## SmartbarInput.disconnectedCallback()
- 位置: L635-644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#uninit()`, `this.getAttribute()`

## SmartbarInput.#uninit()
- 位置: L646-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `UrlbarPrefs.removeObserver()`, `this.#removeContextMenuItems()`, `this._inputContainer.removeEventListener()`, `this._removeObservers()`, `this.controller.removeListener()`, `this.inputField.removeEventListener()`, `this.removeEventListener()`, `this.searchModeSwitcher.disconnect()`, `this.view.panel.removeEventListener()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `this.parentNode.removeAttribute()`
- 条件付き依存: `if (this._copyCutController)` → `this.inputField.controllers.removeController()`
- 条件付き依存: `if (UrlbarContentUtils.getPlatform() == "win")` → `this.window.removeEventListener()`
- 条件付き依存: `if (this.#scrollAnimationId)` → `this.window.cancelAnimationFrame()`
- 条件付き依存: `if (this.#gBrowserListenersAdded)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this.#gBrowserListenersAdded)` → `this.window.gBrowser.removeTabsProgressListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this._inputCta.removeEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.removeEventListener()`
- 参照: `SmartbarInput.#inputFieldEvents`, `this.#gBrowserListenersAdded`, `this.#isSmartbarMode`, `this.#scrollAnimationId`, `this._copyCutController`, `this.document`, `this.sapName`, `this.window`

## SmartbarInput.#editContextMenu()
- 位置: L736-738
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.documentGlobal.EditContextMenu`

## SmartbarInput.#initContextMenuItems()
- 位置: L751-766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#initAddSearchEngines()`, `this._initPasteAndGo()`, `this._initStripOnShare()`
- 条件付き依存: `if (this.#isAddressbar || this.#isSmartbarMode)` → `this._initAutofillDismiss()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this._initPasteAndGo()`
- 参照: `this.#editContextMenu`, `this.#isAddressbar`, `this.#isSmartbarMode`

## SmartbarInput.#initAddSearchEngines()
- 位置: L772-786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L774-780
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fragment.appendChild()`, `this.addSearchEngineHelper.createContextSeparator()`, `this.ownerDocument.createDocumentFragment()`

## onShowing()
- 位置: L781-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `items.push()`, `this.addSearchEngineHelper.refreshContextMenu()`
- 参照: `items.length`

## SmartbarInput.#addContextMenuItems()
- 位置: L794-801
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contextMenuItemSets.push()`, `this.#editContextMenu.addItems()`

## matches()
- 位置: L798-798
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.inputField`

## SmartbarInput.#removeContextMenuItems()
- 位置: L807-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#editContextMenu.removeItems()`
- 参照: `this.#contextMenuItemSets`

## SmartbarInput.#initSmartbarContextMenu()
- 位置: L817-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.#editContextMenu.open()`, `this.#initSmartbarContextMenuPaste()`, `this.#maybeSelectAll()`, `this.inputField.addEventListener()`
- 参照: `event.button`, `this.#editContextMenu`, `this.inputField`

## SmartbarInput.#initSmartbarContextMenuPaste()
- 位置: L839-866
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.#ensureSmartbarEditor()`, `this.#readClipboardData()`, `this.ownerDocument .getElementById()`, `this.ownerDocument .getElementById("cmd_paste") .addEventListener()`
- 条件付き依存: `if (editor && dt)` → `editor.paste()`
- 参照: `this.#editContextMenu.input`, `this.#smartbarContextMenuPasteInitialized`, `this.#smartbarInputController?.input`, `this.inputField`

## SmartbarInput.#readClipboardData()
- 位置: L868-898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `data.value?.QueryInterface()`, `dt.setData()`, `xferable.addDataFlavor()`, `xferable.getTransferData()`, `xferable.init()`
- 条件付き依存: `if (windowContext)` → `Services.clipboard.getData()`
- 条件付き依存: `if (!(windowContext))` → `Services.clipboard.getData()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsISupportsString`, `Ci.nsITransferable`, `data.value?.QueryInterface(Ci.nsISupportsString).data`, `this.documentGlobal?.browsingContext?.currentWindowContext`
- XPCOM: `nsIClipboard` / [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## SmartbarInput.addGBrowserListeners()
- 位置: L900-920
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (this.#isAddressbar || this.#isSmartbarMode)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 参照: `this.#gBrowserListenersAdded`, `this.#isAddressbar`, `this.#isSmartbarMode`, `this.window.gBrowser`

## SmartbarInput.#initSmartbarEditor()
- 位置: L922-929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createEditor()`, `this.#initSmartbarContextMenu()`
- 参照: `adapter.editor`, `adapter.input`, `adapter.input.maxLength`, `lazy.SmartbarInputController`, `this.#smartbarEditor`, `this.#smartbarInputController`, `this.inputField`

## SmartbarInput.#ensureSmartbarEditor()
- 位置: L931-936
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#smartbarInputController)` → `this.#initSmartbarEditor()`
- 参照: `this.#smartbarEditor`, `this.#smartbarInputController`

## SmartbarInput.#setInputValue()
- 位置: L938-944
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.setValue()`
- 参照: `this.#smartbarInputController`, `this.inputField.value`

## SmartbarInput.#setInputRangeText()
- 位置: L946-957
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.setRangeText()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.setRangeText()`
- 参照: `this.#smartbarInputController`

## SmartbarInput.addSearchEngineHelper()
- 位置: L966-968
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#addSearchEngineHelper`

## SmartbarInput.#getValueFormatter()
- 位置: L970-972
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarValueFormatter`, `this.#valueFormatter`

## SmartbarInput.sapName()
- 位置: L974-976
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#sapName`

## SmartbarInput.isSearchbarSAP()
- 位置: L984-986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.isSearchbarSAP()`
- 参照: `this.#sapName`

## SmartbarInput.parentController()
- 位置: L988-990
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.controller.parentController`

## SmartbarInput.smartbarAction()
- 位置: L992-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`
- 参照: `this.#smartbarAction`

## SmartbarInput.detectedIntent()
- 位置: L1001-1003
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#detectedIntent`

## SmartbarInput.assistantIsGenerating()
- 位置: L1008-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarAssistantIsGenerating`

## SmartbarInput.assistantIsGenerating()
- 位置: L1012-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `this._inputCta.setAttribute()`
- 条件付き依存: `if (!(value))` → `this._inputCta.setAttribute()`
- 参照: `this.#smartbarAssistantIsGenerating`, `this.smartbarAction`

## SmartbarInput.sapLocation()
- 位置: L1029-1031
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isSidebarMode`

## SmartbarInput.windowMode()
- 位置: L1038-1041
- 役割: (未記入)
- 触るとき: (未記入)

## SmartbarInput.#aiWindow()
- 位置: L1046-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `root.host?.closest()`, `this.getRootNode()`

## SmartbarInput.conversationTelemetryInfo()
- 位置: L1056-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#aiWindow?.conversationId`, `this.#aiWindow?.conversationMessageCount`

## SmartbarInput.modelName()
- 位置: L1068-1070
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#aiWindow?.modelName`

## SmartbarInput.contextWebsitesCount()
- 位置: L1077-1079
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getResolvedContextWebsites()`
- 参照: `this.getResolvedContextWebsites().length`

## SmartbarInput.smartbarAction()
- 位置: L1086-1094
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#smartbarAction != action)` → `this.setAttribute()`
- 条件付き依存: `if (!this.#smartbarAssistantIsGenerating)` → `this._inputCta.setAttribute()`
- 参照: `this.#smartbarAction`, `this.#smartbarAssistantIsGenerating`

## SmartbarInput.blur()
- 位置: L1096-1102
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.blur()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.blur()`
- 参照: `this.#smartbarInputController`

## SmartbarInput.placeholder()
- 位置: L1107-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController?.placeholder`, `this.inputField?.placeholder`

## SmartbarInput.placeholder()
- 位置: L1113-1121
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.placeholder`, `this.inputField`, `this.inputField.placeholder`

## SmartbarInput.readOnly()
- 位置: L1126-1128
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController?.readOnly`, `this.inputField?.readOnly`

## SmartbarInput.readOnly()
- 位置: L1130-1138
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.readOnly`, `this.inputField`, `this.inputField.readOnly`

## SmartbarInput.selectionStart()
- 位置: L1143-1149
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController?.selectionStart`, `this.inputField?.selectionStart`

## SmartbarInput.selectionStart()
- 位置: L1151-1159
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.selectionStart`, `this.inputField`, `this.inputField.selectionStart`

## SmartbarInput.selectionEnd()
- 位置: L1164-1170
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController?.selectionEnd`, `this.inputField?.selectionEnd`

## SmartbarInput.selectionEnd()
- 位置: L1172-1180
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.selectionEnd`, `this.inputField`, `this.inputField.selectionEnd`

## SmartbarInput.onPrefChanged()
- 位置: L1188-1205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAttribute()`, `this.updatePlaceholder()`
- 条件付き依存: `if (this.getAttribute("sap-name") == "searchbar" && this.isConnected)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.search.widget.new"))` → `this.#init()`
- 条件付き依存: `if (!(UrlbarPrefs.get("browser.search.widget.new")))` → `this.#uninit()`
- 参照: `this.isConnected`

## SmartbarInput.formatValue()
- 位置: L1210-1215
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isAddressbar && this.editor)` → `this.#getValueFormatter().update()`
- 条件付き依存: `if (this.#isAddressbar && this.editor)` → `this.#getValueFormatter()`
- 参照: `this.#isAddressbar`, `this.editor`

## SmartbarInput.focus()
- 位置: L1217-1232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.inputField.dispatchEvent()`
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.focus()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.focus()`
- 参照: `beforeFocus.defaultPrevented`, `this.#smartbarInputController`

## SmartbarInput.select()
- 位置: L1234-1253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.inputField.dispatchEvent()`
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController?.select()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.select()`
- 参照: `beforeSelect.defaultPrevented`, `this.#smartbarInputController`, `this._suppressPrimaryAdjustment`

## SmartbarInput.setSelectionRange()
- 位置: L1255-1277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.inputField.dispatchEvent()`
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.setSelectionRange()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.setSelectionRange()`
- 参照: `beforeSelect.defaultPrevented`, `this.#smartbarInputController`, `this._suppressPrimaryAdjustment`

## SmartbarInput.saveSelectionStateForBrowser()
- 位置: L1279-1291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserState()`
- 参照: `Number.MAX_SAFE_INTEGER`, `state.selection`, `this._protocolIsTrimmed`, `this._wwwIsTrimmed`, `this.selectionEnd`, `this.selectionStart`, `this.value`

## SmartbarInput.restoreSelectionStateForBrowser()
- 位置: L1293-1307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focus()`, `this.getBrowserState()`
- 条件付き依存: `if (state.selection.shouldUntrim)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (state.selection)` → `this.setSelectionRange()`
- 条件付き依存: `if (state.selection)` → `Math.min()`
- 参照: `state.selection`, `state.selection.end`, `state.selection.shouldUntrim`, `state.selection.start`, `this.value.length`

## SmartbarInput.setURI()
- 位置: L1326-1508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`, `lazy.UrlbarSearchTermsPersistence.searchModeMatchesState()`, `this.#handlePersistedSearchTerms()`, `this.getBrowserState()`, `this.inputField.dispatchEvent()`, `this.setPageProxyState()`, `this.setValue()`, `this.toggleAttribute()`
- 条件付き依存: `if ( dueToTabSwitch && UrlbarPrefs.getScotchBonnetPref("scotchBonnet.persistSearchMode") )` → `this._updateSearchModeUI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `Services.io.createExposableURI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `this.window.isInitialPage()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if (!( this.window.isInitialPage(uri) && lazy.BrowserUIUtils.checkEmptyPageOrigin( this.window.gBrowser.selectedBrowser, uri ) ))` → `losslessDecodeURI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `this.window.isBlankPageURL()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `lazy.ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (!(value === null || (!value && dueToTabSwitch)))` → `this.window.isInitialPage()`
- 条件付き依存: `if (!(value === null || (!value && dueToTabSwitch)))` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if (this.focused && value != previousUntrimmedValue)` → `value.substring()`
- 条件付き依存: `if (this.focused && value != previousUntrimmedValue)` → `previousUntrimmedValue.substring()`
- 条件付き依存: `if ( previousSelectionStart != previousSelectionEnd && value.substring(previousSelectionStart, previousSelectionEnd) === previousUntrimmedValue.substring( previo...)` → `this.setSelectionRange()`
- 条件付き依存: `if ( previousSelectionEnd && (previousUntrimmedValue.length === previousSelectionEnd || value.length <= previousSelectionEnd) )` → `this.setSelectionRange()`
- 条件付き依存: `if (!( previousSelectionEnd && (previousUntrimmedValue.length === previousSelectionEnd || value.length <= previousSelectionEnd) ))` → `this.setSelectionRange()`
- 条件付き依存: `if (dueToTabSwitch && !valid)` → `this.restoreSearchModeState()`
- 参照: `"www.".length`, `UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.BrowserUIUtils.trimURLProtocol.length`, `previousUntrimmedValue.length`, `state.persist.isDefaultEngine`, `state.persist.originalEngineName`, `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.#isOpenedPageInBlankTargetLoading`, `this._protocolIsTrimmed`, `this._wwwIsTrimmed`, `this.focused`, `this.getBrowserState(this.window.gBrowser.selectedBrowser) .isUnifiedSearchButtonAvailable`, `this.searchMode`, `this.selectionEnd`, `this.selectionStart`, `this.untrimmedValue`, `this.userTypedValue`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser`, `this.window.gBrowser.selectedBrowser.currentAuthPromptURI`, `uri.spec`, `value.length`
- XPCOM: `Services.io`

## SmartbarInput.makeURIReadable()
- 位置: L1519-1534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.createExposableURI()`, `lazy.ReaderMode.getOriginalUrlObjectForDisplay()`
- 参照: `uri.displaySpec`
- XPCOM: `Services.io`

## SmartbarInput.onLocationChange()
- 位置: L1547-1573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.isBlankPageURL()`
- 条件付き依存: `if (browser == this.window.gBrowser.selectedBrowser)` → `this.#updateContextChips()`
- 条件付き依存: `if ( browser != this.window.gBrowser.selectedBrowser && !this.window.isBlankPageURL(locationURI.spec) )` → `this.getBrowserState()`
- 条件付き依存: `if (webProgress.loadType & Ci.nsIDocShell.LOAD_CMD_HISTORY)` → `lazy.handleBounceEventTrigger()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `locationURI.spec`, `this.#isSmartbarMode`, `this.getBrowserState(browser).isUnifiedSearchButtonAvailable`, `this.window.gBrowser.selectedBrowser`, `webProgress.isTopLevel`, `webProgress.loadType`
- XPCOM: [`nsIDocShell`](../../../../docshell/base/nsIDocShell.idl.md)

## SmartbarInput.handleEvent()
- 位置: L1580-1622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.type.startsWith()`
- 条件付き依存: `if (event.type === "shown")` → `Glean.smartWindow.intentChangePreview.record()`
- 条件付き依存: `if (event.type === "shown")` → `String()`
- 条件付き依存: `if (event.type.startsWith("aiwindow-input-cta:"))` → `this.#handleSmartbarCtaAction()`
- 条件付き依存: `if (event.type === "ai-website-chip:remove")` → `this.removeContextMention()`
- 条件付き依存: `if (event.type === "ai-website-chip:remove")` → `Glean.smartWindow.removeTab.record()`
- 条件付き依存: `if (event.type === "ai-website-chip:remove")` → `String()`
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 条件付き依存: `if (methodName in this)` → `console.error()`
- 参照: `(event).detail`, `event.type`, `this.#contextWebsites.length`, `this.conversationTelemetryInfo`, `this.sapLocation`, `this.smartbarAction`

## SmartbarInput.handleCommand()
- 位置: L1630-1655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MouseEvent.isInstance()`, `this.handleNavigation()`
- 条件付き依存: `if (selectedOneOff && (!isMouseEvent || event.target == selectedOneOff))` → `this.view.oneOffSearchButtons.handleSearchCommand()`
- 参照: `event.button`, `event.target`, `selectedOneOff.engine?.name`, `selectedOneOff.source`, `this.view.isOpen`, `this.view.oneOffSearchButtons?.selectedButton`

## SmartbarInput.#dispatchSmartbarCommitEvent()
- 位置: L1668-1691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`, `this.getContextPageUrl()`, `this.getResolvedContextWebsites()`
- 参照: `this.controller.engineStore.default?.name`, `this.detectedIntent`, `this.sapLocation`, `this.smartbarAction`

## SmartbarInput.submitChat()
- 位置: L1701-1709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchSmartbarCommitEvent()`
- 参照: `this.smartbarAction`

## SmartbarInput.#handleSuppressedNavigation()
- 位置: L1720-1735
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.submitChat()`
- 条件付き依存: `if (this.#smartbarActionLocked)` → `this.#submitLockedAction()`
- 条件付き依存: `if (this._resultForCurrentValue?.type == UrlbarShared.RESULT_TYPE.URL)` → `this.pickResult()`
- 参照: `UrlbarShared.RESULT_TYPE.URL`, `this.#smartbarActionLocked`, `this._lastSearchString`, `this._resultForCurrentValue`, `this._resultForCurrentValue?.type`, `this.untrimmedValue`, `this.value`

## SmartbarInput.#shouldHandleSuppressedNavigation()
- 位置: L1737-1743
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isAgentCommand`, `this._permanentlySuppressStartQuery`, `this.inputField.hasMention`

## SmartbarInput.#handleSmartbarCtaAction()
- 位置: L1761-1800
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleNavigation()`
- 条件付き依存: `if (event.type === "aiwindow-input-cta:on-stop")` → `this.dispatchEvent()`
- 条件付き依存: `if (isExplicitAction)` → `this.#updateGoGuardrail()`
- 条件付き依存: `if (isExplicitAction)` → `this.#updateCtaSearchEngineInfo()`
- 条件付き依存: `if (isExplicitAction)` → `this.focus()`
- 条件付き依存: `if (!this.focused)` → `this.controller.engagementEvent.start()`
- 参照: `event.detail.action`, `event.detail.engineName`, `event.type`, `this.#smartbarActionLocked`, `this.#smartbarSearchEngineName`, `this.focused`, `this.smartbarAction`, `this.value`

## SmartbarInput.#isSafeToPickResult()
- 位置: L1810-1819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getValueFromResult()`
- 参照: `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.TIP`, `result.heuristic`, `result.type`, `this.value`, `this.valueIsTyped`

## SmartbarInput.#shouldSubmitLockedAction()
- 位置: L1835-1848
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `oneOffParams?.engine`, `result.heuristic`, `this.#isSmartbarMode`, `this.#smartbarActionLocked`

## SmartbarInput.#submitLockedAction()
- 位置: L1857-1877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#submitNavigate()`, `this.#submitSearch()`, `this.submitChat()`, `value.trim()`
- 参照: `this.#goBlocked`, `this.smartbarAction`, `this.untrimmedValue`

## SmartbarInput.#submitSearch()
- 位置: L1886-1919
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchSmartbarCommitEvent()`, `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.controller.engineStore.getEngineByName()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.parentController.openSERP()`
- 参照: `engine.id`, `this.#selectedBrowserId`, `this.#smartbarSearchEngineName`, `this.controller.engineStore.default`, `this.sapLocation`, `this.windowMode`

## SmartbarInput.#submitNavigate()
- 位置: L1927-1952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `this.#dispatchSmartbarCommitEvent()`, `this.#loadURL()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `fixupInfo.preferredURI.spec`, `this.isPrivate`, `this.sapLocation`, `this.windowMode`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## SmartbarInput.#goBlocked()
- 位置: L1961-1968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.untrimmedValue.trim()`
- 参照: `this.#detectedIntent`, `this.#smartbarActionLocked`, `this.smartbarAction`

## SmartbarInput.#updateGoGuardrail()
- 位置: L1974-1976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._inputCta?.toggleAttribute()`
- 参照: `this.#goBlocked`

## SmartbarInput.#searchModeEngineForEnterKey()
- 位置: L1990-2008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.engineStore.getEngineByName()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `oneOffParams?.engine`, `result.heuristic`, `result.type`, `this.#isAddressbar`, `this.searchMode.engineName`, `this.searchMode?.engineName`

## SmartbarInput.#engineSearchStringForResult()
- 位置: L2017-2022
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.query`, `result.payload.suggestion`, `this._lastSearchString`

## SmartbarInput.#selectedBrowserId()
- 位置: L2029-2031
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.gBrowser?.selectedBrowser?.browserId`

## SmartbarInput.#openEngineSearch()
- 位置: L2052-2084
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.getSearchSource()`, `this.parentController.openSERP()`
- 参照: `engine.id`, `this.#selectedBrowserId`, `this._resultForCurrentValue`, `this.sapLocation`, `this.view.selectedResult`, `this.windowMode`

## SmartbarInput.#isAgentCommand()
- 位置: L2093-2095
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isAgentCommand()`
- 参照: `this.#isSmartbarMode`, `this.untrimmedValue`

## SmartbarInput.handleNavigation()
- 位置: L2112-2363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.canParse()`, `UrlbarPrefs.get()`, `this.#isSafeToPickResult()`, `this.#searchModeEngineForEnterKey()`, `this.#shouldSubmitLockedAction()`, `this._maybeCanonizeURL()`, `this.controller .resolveFallbackNavigation()`, `this.controller .resolveFallbackNavigation({ searchString: url, where, searchMode: this.searchMode, browserId, }) .then()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.value.startsWith()`, `this.view.getResultFromElement()`, `this.view.telemetryTypeFromElement()`, `url.trim()`
- 条件付き依存: `if (this.#isAgentCommand)` → `getAgentCommandId()`
- 条件付き依存: `if (commandId)` → `Glean.smartWindow.agentCommandSelect.record()`
- 条件付き依存: `if (commandId)` → `String()`
- 条件付き依存: `if (this.#isAgentCommand)` → `this.submitChat()`
- 条件付き依存: `if (this.#isSmartbarMode && this.#shouldHandleSuppressedNavigation)` → `this.#handleSuppressedNavigation()`
- 条件付き依存: `if ( this.#shouldSubmitLockedAction({ element, result, safeToPickResult, isComposing, oneOffParams, }) )` → `this.#submitLockedAction()`
- 条件付き依存: `if ( !isComposing && element && !searchModeEngine && (!oneOffParams?.engine || selectedPrivateEngineResult) && safeToPickResult )` → `this.pickElement()`
- 条件付き依存: `if ( UrlbarPrefs.get("experimental.hideHeuristic") && !element && !isComposing && !oneOffParams?.engine && !searchModeEngine && this._resultForCurrentValue?.heur...)` → `this.pickResult()`
- 条件付き依存: `if (!result && this.value.startsWith("@"))` → `this.view.getResultAtIndex()`
- 条件付き依存: `if (tokenAliasResult?.autofill && tokenAliasResult?.payload.keyword)` → `this.pickResult()`
- 条件付き依存: `if (oneOffParams?.engine)` → `this.#openEngineSearch()`
- 条件付き依存: `if (oneOffParams?.engine)` → `this.#engineSearchStringForResult()`
- 条件付き依存: `if (searchModeEngine)` → `this.#openEngineSearch()`
- 条件付き依存: `if (searchModeEngine)` → `this.controller.whereToOpen()`
- 条件付き依存: `if (URL.canParse(url))` → `this.#getSchemelessInput()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#dispatchSmartbarCommitEvent()`
- 条件付き依存: `if (URL.canParse(url))` → `this.#loadURL()`
- 条件付き依存: `if (!isComposing && this._resultForCurrentValue)` → `this.pickResult()`
- 条件付き依存: `if (heuristicResult)` → `this.pickResult()`
- 条件付き依存: `if (!fixup.keywordAsSent)` → `this.#getSchemelessInput()`
- 条件付き依存: `if (fixup)` → `this.#loadURL()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `console.error`, `fixup.keywordAsSent`, `fixup.postData`, `fixup.url`, `oneOffParams.engine`, `oneOffParams.openWhere`, `oneOffParams?.engine`, `oneOffParams?.openParams`, `oneOffParams?.openWhere`, `openParams.allowInheritPrincipal`, `openParams.inBackground`, `openParams.private`, `openParams.schemelessInput`, `result.payload.inPrivateWindow`, `result.payload.isPrivateEngine`, `result.type`, `this.#isAgentCommand`, `this.#isSmartbarMode`, `this.#selectedBrowserId`, `this.#shouldHandleSuppressedNavigation`, `this._lastSearchString`, `this._resultForCurrentValue`, `this._resultForCurrentValue?.heuristic`, `this.conversationTelemetryInfo`, `this.editor.composing`, `this.sapLocation`, `this.searchMode`, `this.searchMode.engineName`, `this.untrimmedValue`, `this.value`, `this.view.selectedElement`, `this.view.selectedResult`, `this.windowMode`, `tokenAliasResult?.autofill`, `tokenAliasResult?.payload.keyword`

## SmartbarInput.handleRevert()
- 位置: L2365-2381
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isAddressbar)` → `this.setURI()`
- 条件付き依存: `if (this.#isAddressbar && this.value && this.focused)` → `this.select()`
- 参照: `this.#isAddressbar`, `this.#isSmartbarMode`, `this.focused`, `this.searchMode`, `this.userTypedValue`, `this.value`

## SmartbarInput.maybeHandleRevertFromPopup()
- 位置: L2383-2392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorElement?.closest()`, `this.getBrowserState()`
- 条件付き依存: `if (anchorElement?.closest("#urlbar") && state.persist?.shouldPersist)` → `this.handleRevert()`
- 条件付き依存: `if (anchorElement?.closest("#urlbar") && state.persist?.shouldPersist)` → `Glean.urlbarPersistedsearchterms.revertByPopupCount.add()`
- 参照: `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.handoff()
- 位置: L2407-2418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("shouldHandOffToSearchMode") && searchEngine)` → `this.search()`
- 条件付き依存: `if (!(UrlbarPrefs.get("shouldHandOffToSearchMode") && searchEngine))` → `this.search()`
- 参照: `this._handoffSession`, `this._isHandoffSession`

## SmartbarInput.handlesOpenInCommands()
- 位置: L2426-2428
- 役割: (未記入)
- 触るとき: (未記入)

## SmartbarInput.pickElement()
- 位置: L2436-2445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `logger()`, `logger().debug()`, `this.pickResult()`, `this.view.getResultFromElement()`
- 参照: `event?.type`

## SmartbarInput.pickResult()
- 位置: L2460-2906
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.getLoadRequestFromResult()`, `UrlbarShared.looksLikeSingleWordHost()`, `element?.classList.contains()`, `lazy.ExtensionSearchHandler.handleInputEntered()`, `this.#loadURL()`, `this.#providesSearchMode()`, `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.controller.engineStore.getEngineByName()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.handleRevert()`, `this.hasAttribute()`, `this.maybeConfirmSearchModeFromResult()`, `this.parentController.switchToTab()`, `this.setValueFromResult()`, `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (element?.classList.contains("urlbarView-button-menu"))` → `this.view.openResultMenu()`
- 条件付き依存: `if (element?.dataset.command)` → `this.#pickMenuResult()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderGlobalActions" && this.#providesSearchMode(result) && !this.view.selectedElement?.dataset.immediateSearch )` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( (this.searchMode?.isPreview && result.providerName == "UrlbarProviderGlobalActions" && !this.view.selectedElement?.dataset.immediateSearch) || (result.heuri...)` → `this.confirmSearchMode()`
- 条件付き依存: `if ( (this.searchMode?.isPreview && result.providerName == "UrlbarProviderGlobalActions" && !this.view.selectedElement?.dataset.immediateSearch) || (result.heuri...)` → `this.search()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.getSearchSource()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.view.onQueryResultRemoved()`
- 条件付き依存: `if (!this.#providesSearchMode(result))` → `this.view.close()`
- 条件付き依存: `if (isCanonized)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (isCanonized)` → `this.getSearchSource()`
- 条件付き依存: `if (isCanonized)` → `this.#loadURL()`
- 条件付き依存: `if (result.heuristic)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (result.heuristic)` → `UrlbarShared.looksLikeSingleWordHost()`
- 条件付き依存: `if (result.heuristic)` → `this.#getSchemelessInput()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.getSearchSource()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( this.#isAddressbar && !this.searchMode && result.heuristic && // If we asked the DNS earlier, avoid the post-facto check. !UrlbarPrefs.get("browser.fixup.dn...)` → `this.parentController.checkKeywordURIFixup()`
- 条件付き依存: `if ( this.#isAddressbar && !this.searchMode && result.heuristic && // If we asked the DNS earlier, avoid the post-facto check. !UrlbarPrefs.get("browser.fixup.dn...)` → `originalUntrimmedValue.trim()`
- 条件付き依存: `if (!loadRequest)` → `this.handleRevert()`
- 条件付き依存: `if (!loadRequest)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (!loadRequest)` → `this.getSearchSource()`
- 条件付き依存: `if (!loadRequest)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (!loadRequest)` → `JSON.stringify()`
- 条件付き依存: `if (input !== undefined)` → `this.parentController.addToInputHistory()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.controller.engagementEvent .startTrackingBounceEvent()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.getSearchSource()`
- 条件付き依存: `if (this.window.gBrowser)` → `logger().error()`
- 条件付き依存: `if (this.window.gBrowser)` → `logger()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#dispatchSmartbarCommitEvent()`
- 参照: `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `element?.dataset.action`, `element?.dataset.command`, `element?.dataset.url`, `loadRequest.urlLoad`, `loadRequest.urlLoad.url`, `openParams.allowInheritPrincipal`, `openParams.private`, `openParams.schemelessInput`, `result.autofill.adaptiveHistoryInput`, `result.autofill?.type`, `result.heuristic`, `result.id`, `result.payload.content`, `result.payload.engine`, `result.payload.inPrivateWindow`, `result.payload.keyword`, `result.payload.providesSearchMode`, `result.payload.query`, `result.payload.suggestion`, `result.payload.tabGroup`, `result.payload.type`, `result.payload.url`, `result.payload.userContext?.id`, `result.payload?.engine`, `result.payload?.isSponsored`, `result.providerName`, `result.source`, `result.type`, `this.#isAddressbar`, `this.#isSmartbarMode`, `this.#sapName`, `this._lastSearchString`, `this._untrimmedValue`, `this.isPrivate`, `this.sapLocation`, `this.searchMode`, `this.searchMode?.isPreview`, `this.untrimmedValue`, `this.value`, `this.view.oneOffSearchButtons?.selectedButton`, `this.view.selectedElement?.dataset.immediateSearch`, `this.window.gBrowser`, `this.window.gBrowser.selectedBrowser.browserId`, `this.window.gBrowser.selectedTab.splitview`, `this.windowMode`

## SmartbarInput.clearSmartbarInput()
- 位置: L2908-2930
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`, `this.#updateCtaSearchEngineInfo()`, `this.#updateGoGuardrail()`, `this.dispatchEvent()`, `this.setSelectionRange()`, `this.view.close()`
- 参照: `this.#contextWebsites`, `this.#detectedIntent`, `this.#smartbarActionLocked`, `this.#smartbarSearchEngineName`, `this._autofillPlaceholder`, `this._lastSearchString`, `this._resultForCurrentValue`, `this.smartbarAction`, `this.userTypedValue`, `this.value`

## SmartbarInput.setValueFromResult()
- 位置: L2955-3061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#providesSearchMode()`, `this._maybeCanonizeURL()`, `this.setPageProxyState()`, `this.setResultForCurrentValue()`
- 条件付き依存: `if (!result)` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (canonizedUrl)` → `this.setValue()`
- 条件付き依存: `if (canonizedUrl)` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (result.autofill)` → `this._autofillValue()`
- 条件付き依存: `if (this.#providesSearchMode(result))` → `this.view.resultIsSelected()`
- 条件付き依存: `if (this.view.resultIsSelected(result))` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if (this.view.resultIsSelected(result))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!enteredSearchMode)` → `this.setValue()`
- 条件付き依存: `if (!enteredSearchMode)` → `this.#getValueFromResult()`
- 条件付き依存: `if (!enteredSearchMode)` → `this.#getActionTypeFromResult()`
- 条件付き依存: `if (this.#providesSearchMode(result))` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (!result.autofill)` → `this.#getValueFromResult()`
- 条件付き依存: `if (!result.autofill)` → `this.setValue()`
- 条件付き依存: `if (!result.autofill)` → `this.#getActionTypeFromResult()`
- 参照: `result.autofill`, `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._autofillPlaceholder.value`, `this._lastSearchString`, `this._valueOnLastSearch`, `this.searchMode`, `this.searchMode?.isPreview`, `this.value`, `this.value.length`, `this.view.oneOffSearchButtons?.selectedButton`, `this.view.visibleResults.length`

## SmartbarInput.setResultForCurrentValue()
- 位置: L3074-3076
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._resultForCurrentValue`

## SmartbarInput._autofillFirstResult()
- 位置: L3086-3117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._autofillPlaceholder.value .toLocaleLowerCase()`, `this._autofillPlaceholder.value .toLocaleLowerCase() .startsWith()`, `this._lastSearchString.toLocaleLowerCase()`, `this.setValueFromResult()`
- 参照: `result.autofill`, `this._autofillIgnoresSelection`, `this._autofillPlaceholder`, `this._autofillPlaceholder.value.length`, `this._lastSearchString.length`, `this.inputField.isHandlingMentions`, `this.selectionEnd`, `this.selectionStart`

## SmartbarInput.#clearAutofill()
- 位置: L3121-3135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setInputValue()`, `this.setSelectionRange()`, `this.value.substring()`
- 参照: `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionStart`, `this.selectionEnd`, `this.selectionStart`

## SmartbarInput.onFirstResult()
- 位置: L3143-3177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#providesSearchMode()`, `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( firstResult.heuristic && firstResult.payload.keyword && !this.#providesSearchMode(firstResult) && this.maybeConfirmSearchModeFromResult({ result: firstResul...)` → `this.controller.discardResults()`
- 条件付き依存: `if (firstResult.autofill)` → `this._autofillFirstResult()`
- 条件付き依存: `if (!(firstResult.autofill))` → `this.value.endsWith()`
- 条件付き依存: `if ( this._autofillPlaceholder && // Avoid clobbering added spaces (for token aliases, for example). !this.value.endsWith(" ") )` → `this.setValue()`
- 参照: `firstResult.autofill`, `firstResult.heuristic`, `firstResult.payload.keyword`, `queryContext.results`, `this._autofillPlaceholder`, `this.userTypedValue`

## SmartbarInput.onQueryStarted()
- 位置: L3184-3186
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarActionPending`

## SmartbarInput.onQueryResults()
- 位置: L3193-3203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateSmartbarCTAButton()`
- 参照: `queryContext.pendingHeuristicProviders.size`, `queryContext.results`, `this.#isSmartbarMode`, `this.#smartbarActionPending`

## SmartbarInput.onQueryFinished()
- 位置: L3205-3208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePanelScrollFade()`

## SmartbarInput.suppressStartQuery()
- 位置: L3216-3221
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._permanentlySuppressStartQuery`, `this._suppressStartQuery`

## SmartbarInput.unsuppressStartQuery()
- 位置: L3226-3229
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._permanentlySuppressStartQuery`, `this._suppressStartQuery`

## SmartbarInput.startQuery()
- 位置: L3255-3332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#makeQueryContext()`, `this.controller.startQuery()`
- 条件付き依存: `if ( (isHandlingMentions || isHandlingCommands || this.#isAgentCommand) && event )` → `this.view.close()`
- 条件付き依存: `if ( (isHandlingMentions || isHandlingCommands || this.#isAgentCommand) && event )` → `this.#updateSmartbarCTAButton()`
- 条件付き依存: `if (!searchString)` → `this.getAttribute()`
- 条件付き依存: `if (!(!searchString))` → `this.value.startsWith()`
- 条件付き依存: `if (event)` → `this.controller.engagementEvent.start()`
- 条件付き依存: `if (this._suppressStartQuery)` → `lazy.UrlbarProviderHeuristicFallback.matchUnknownUrl()`
- 条件付き依存: `if (this._suppressStartQuery)` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (this._suppressStartQuery)` → `this.#updateSmartbarCTAButton()`
- 条件付き依存: `if (resetSearchState)` → `this._resetSearchState()`
- 条件付き依存: `if (this.searchMode)` → `this.confirmSearchMode()`
- 参照: `this.#isAgentCommand`, `this._autofillIgnoresSelection`, `this._lastSearchString`, `this._suppressStartQuery`, `this._valueOnLastSearch`, `this.inputField.isHandlingCommands`, `this.inputField.isHandlingMentions`, `this.lastQueryContextPromise`, `this.searchMode`, `this.value`

## SmartbarInput.search()
- 位置: L3355-3437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setInputValue()`, `this.searchModeForToken()`, `trimmedValue.search()`, `trimmedValue.substring()`, `value.trim()`
- 条件付き依存: `if (options.focus ?? true)` → `this.focus()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.controller.engineStore .init() .catch(() => {}) .then()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.controller.engineStore .init() .catch()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.controller.engineStore .init()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.search()`
- 条件付き依存: `if (!searchMode && searchEngine)` → `searchEngine.aliases.includes()`
- 条件付き依存: `if (firstTokenIsRestriction)` → `value.replace()`
- 条件付き依存: `if (searchMode)` → `UrlbarShared.REGEXP_SPACES.test()`
- 条件付き依存: `if (UrlbarShared.REGEXP_SPACES.test(value[0]))` → `value.slice()`
- 条件付き依存: `if (!(searchMode))` → `( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes()`
- 条件付き依存: `if (!(searchMode))` → `Object.values()`
- 条件付き依存: `if ( /** @type {string[]} */ ( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes(firstToken) )` → `( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes()`
- 条件付き依存: `if ( /** @type {string[]} */ ( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes(firstToken) )` → `Object.values()`
- 条件付き依存: `if (startQuery)` → `this.inputField.dispatchEvent()`
- 参照: `UrlbarShared.REGEXP_SPACES`, `UrlbarShared.RESTRICT_TOKENS`, `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `options.focus`, `searchEngine.name`, `searchMode.entry`, `this._lastSearchString`, `this.controller.engineStore.failed`, `this.controller.engineStore.initialized`, `this.searchMode`, `this.selectionStart`, `this.window`

## SmartbarInput.searchModeForToken()
- 位置: L3448-3464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `m.restrict`, `this.#isAddressbar`, `this.controller.engineStore.default?.name`

## SmartbarInput.openSearchEnginePage()
- 位置: L3477-3530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.trim()`
- 条件付き依存: `if (!searchEngine || !event || !where)` → `console.warn()`
- 条件付き依存: `if (trimmedValue)` → `this._recordSearch()`
- 条件付き依存: `if (where == "current")` → `this.setSearchMode()`
- 条件付き依存: `if (trimmedValue)` → `this.parentController.openSERP()`
- 条件付き依存: `if (!(trimmedValue))` → `this.parentController.openSearchForm()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `searchEngine.id`, `searchEngine.name`, `this.#selectedBrowserId`, `this._lastSearchString`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.setHiddenFocus()
- 位置: L3536-3543
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.focused)` → `this.removeAttribute()`
- 条件付き依存: `if (!(this.focused))` → `this.focus()`
- 参照: `this._hideFocus`, `this.focused`

## SmartbarInput.removeHiddenFocus()
- 位置: L3552-3561
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.focused)` → `this.toggleAttribute()`
- 条件付き依存: `if (forceSuppressFocusBorder)` → `this.toggleAttribute()`
- 参照: `this._hideFocus`, `this.focused`

## SmartbarInput.getSearchMode()
- 位置: L3577-3588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSearchModesObject()`
- 参照: `modes.confirmed`, `modes.preview`

## SmartbarInput.setSearchMode()
- 位置: async L3601-3697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.SEARCH_MODE_ENTRY.has()`, `UrlbarShared.deepEqual()`, `lazy.UrlbarSearchTermsPersistence.onSearchModeChanged()`, `this.#getSearchModesObject()`, `this.dispatchEvent()`, `this.getSearchMode()`
- 条件付き依存: `if (!this.controller.engineStore.initialized)` → `this.controller.engineStore.init()`
- 条件付き依存: `if (searchMode?.engineName)` → `this.controller.engineStore.getEngineByName()`
- 条件付き依存: `if (source)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (!(sourceName))` → `console.error()`
- 条件付き依存: `if (browser == this.window.gBrowser.selectedBrowser)` → `this._updateSearchModeUI()`
- 条件付き依存: `if (!newSearchMode.isPreview && !areSearchModesSame)` → `this.parentController.recordSearchMode()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `engine.isGeneralPurposeEngine`, `modes.confirmed`, `modes.preview`, `newSearchMode.isGeneralPurposeEngine`, `newSearchMode.isPreview`, `newSearchMode.restrictType`, `newSearchMode.source`, `searchMode.engineName`, `searchMode?.engineName`, `this.#isSmartbarMode`, `this.controller.engineStore.initialized`, `this.untrimmedValue`, `this.userTypedValue`, `this.valueIsTyped`, `this.window`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.#getSearchModesObject()
- 位置: L3725-3735
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserState()`
- 参照: `state.searchModes`, `this.#isAddressbar`, `this.#searchbarSearchModes`

## SmartbarInput.restoreSearchModeState()
- 位置: L3740-3746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserState()`
- 参照: `state.searchModes?.confirmed`, `this.#isSmartbarMode`, `this.searchMode`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.searchModeShortcut()
- 位置: async L3751-3773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.search()`, `this.select()`
- 条件付き依存: `if (!this.controller.engineStore.initialized)` → `this.controller.engineStore.init()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `this.controller.engineStore.default.name`, `this.controller.engineStore.initialized`, `this.searchMode`, `this.value`

## SmartbarInput.confirmSearchMode()
- 位置: L3778-3789
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `searchMode.isPreview`, `searchMode?.isPreview`, `this.searchMode`, `this.view.oneOffSearchButtons`, `this.view.oneOffSearchButtons.selectedButton`

## SmartbarInput.editor()
- 位置: L3793-3798
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#ensureSmartbarEditor()`
- 参照: `this.#isSmartbarMode`, `this.inputField.editor`

## SmartbarInput.focused()
- 位置: L3800-3803
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `input.getRootNode()`
- 参照: `input.getRootNode().activeElement`, `this.#smartbarInputController?.input`, `this.inputField`

## SmartbarInput.goButton()
- 位置: L3805-3807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## SmartbarInput.smartbarButtonContainer()
- 位置: L3809-3811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## SmartbarInput.focusFirstActionButton()
- 位置: L3819-3825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( this.smartbarButtonContainer.querySelector( ":scope > :not([hidden]):not([disabled])" ) ).focus()`, `this.smartbarButtonContainer.querySelector()`

## SmartbarInput.focusLastActionButton()
- 位置: L3835-3859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(last).focus()`, `this.smartbarButtonContainer.querySelectorAll()`, `walk()`
- 参照: `buttons.length`

## walk()
- 位置: L3841-3856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.checkVisibility()`, `this.#isTabbable()`, `walk()`
- 条件付き依存: `if (node.shadowRoot)` → `walk()`
- 参照: `node.checkVisibility`, `node.children`, `node.shadowRoot`, `node.shadowRoot.children`

## SmartbarInput.#isTabbable()
- 位置: L3869-3871
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `el.disabled`, `el.localName`, `el.tabIndex`

## SmartbarInput.#isInsideContainer()
- 位置: L3882-3887
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `target.host`, `target.parentNode`

## SmartbarInput.#onActionButtonsKeyDown()
- 位置: L3897-3948
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttons.includes()`, `container.querySelectorAll()`, `this.#isTabbable()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE && this.view.isOpen)` → `this.view.close()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE && this.view.isOpen)` → `this.focus()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE && this.view.isOpen)` → `event.preventDefault()`
- 条件付き依存: `if (event.shiftKey && focused == buttons[0])` → `this.focus()`
- 条件付き依存: `if (event.shiftKey && focused == buttons[0])` → `this.view.selectBy()`
- 条件付き依存: `if (event.shiftKey && focused == buttons[0])` → `event.preventDefault()`
- 条件付き依存: `if (!event.shiftKey && focused == buttons[buttons.length - 1])` → `this.focus()`
- 条件付き依存: `if (!event.shiftKey && focused == buttons[buttons.length - 1])` → `this.view.selectBy()`
- 条件付き依存: `if (!event.shiftKey && focused == buttons[buttons.length - 1])` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_TAB`, `buttons.length`, `event.composedTarget`, `event.keyCode`, `event.shiftKey`, `focused.host`, `focused.parentNode`, `innerTarget?.nextElementSibling`, `innerTarget?.previousElementSibling`, `this.smartbarButtonContainer`, `this.view.isOpen`

## SmartbarInput.value()
- 位置: L3950-3952
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#smartbarInputController?.value`, `this.inputField.value`

## SmartbarInput.value()
- 位置: L3954-3956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setValue()`

## SmartbarInput.untrimmedValue()
- 位置: L3958-3960
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._untrimmedValue`

## SmartbarInput.userTypedValue()
- 位置: L3962-3966
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isAddressbar`, `this._userTypedValue`, `this.window.gBrowser.userTypedValue`

## SmartbarInput.userTypedValue()
- 位置: L3968-3974
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isAddressbar`, `this._userTypedValue`, `this.window.gBrowser.userTypedValue`

## SmartbarInput.lastSearchString()
- 位置: L3976-3978
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._lastSearchString`

## SmartbarInput.searchMode()
- 位置: L3990-3999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSearchMode()`
- 参照: `this.#isSmartbarMode`, `this.window.gBrowser`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.searchMode()
- 位置: L4001-4014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.engineStore .getEngineByName()`, `this.controller.engineStore .getEngineByName(this.searchMode?.engineName) ?.markAsUsed()`, `this.setSearchMode()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `Promise.resolve()`
- 参照: `this.#isSmartbarMode`, `this.#searchModeApplied`, `this.searchMode?.engineName`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.getBrowserState()
- 位置: L4016-4023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserStates.get()`
- 条件付き依存: `if (!state)` → `this.#browserStates.set()`

## SmartbarInput.#updatePopoverAnchor()
- 位置: async L4025-4042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#measurePopoverAnchor()`
- 条件付き依存: `if (this.document.fullscreenElement)` → `this.window.addEventListener()`
- 条件付き依存: `if (this.document.fullscreenElement)` → `this.#updatePopoverAnchor()`
- 参照: `this.#canOpenPopover`, `this.document.fullscreenElement`

## SmartbarInput.#openPopover()
- 位置: L4044-4065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`, `this.setAttribute()`
- 条件付き依存: `if (!this.hasAttribute("popover-animate"))` → `this.window.promiseDocumentFlushed()`
- 条件付き依存: `if (!this.hasAttribute("popover-animate"))` → `this.window.requestAnimationFrame()`
- 条件付き依存: `if (!this.hasAttribute("popover-animate"))` → `this.setAttribute()`
- 参照: `this.#canOpenPopover`, `this.view.isOpen`

## SmartbarInput.#closePopover()
- 位置: L4067-4076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`, `this.removeAttribute()`
- 参照: `this.view.isOpen`

## SmartbarInput.updatePopover()
- 位置: L4078-4084
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.view.isOpen)` → `this.#openPopover()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.#closePopover()`
- 参照: `this.view.isOpen`

## SmartbarInput.setPageProxyState()
- 位置: L4106-4134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._identityBox?.setAttribute()`, `this._inputContainer.setAttribute()`, `this.getAttribute()`, `this.setAttribute()`, `this.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if ( updatePopupNotifications && prevState != state && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 参照: `this.#isAddressbar`, `this._lastValidURLStr`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`

## SmartbarInput.afterTabSwitchFocusChange()
- 位置: L4141-4144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._afterTabSelectAndFocusChange()`
- 参照: `this._gotFocusChange`

## SmartbarInput.maybeConfirmSearchModeFromResult()
- 位置: L4165-4207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.payload.autofillKeyword?.trim()`, `result.payload.keyword?.trim()`, `result.payload.query?.trimStart()`, `this._searchModeForResult()`, `this.setValue()`, `this.value.trim()`
- 条件付き依存: `if (startQuery)` → `this.#searchModeApplied.then()`
- 条件付き依存: `if (startQuery)` → `this.startQuery()`
- 参照: `searchMode.isPreview`, `this._resultForCurrentValue`, `this.searchMode`, `this.untrimmedValue`, `this.userTypedValue`

## SmartbarInput.onSearchEngineUpdate()
- 位置: L4213-4229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateCtaSearchEngineInfo()`, `this.updatePlaceholder()`
- 参照: `engine.name`, `searchMode?.engineName`, `this.searchMode`

## SmartbarInput.getSearchSource()
- 位置: L4239-4271
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isAddressbar)` → `this.searchModeSwitcher?.eventTargetIsPanelItem()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.view.oneOffSearchButtons?.eventTargetIsAOneOff()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 参照: `state.persist?.searchTerms`, `this.#isAddressbar`, `this.#sapName`, `this._isHandoffSession`, `this.searchMode`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.#providesSearchMode()
- 位置: L4280-4291
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.providesSearchMode`, `result.providerName`, `this.view.selectedElement`, `this.view.selectedElement.dataset.providesSearchmode`

## SmartbarInput._addObservers()
- 位置: L4293-4298
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._observersAdded)` → `this.controller.engineStore.addObserver()`
- 参照: `this._observersAdded`, `this.onSearchEngineUpdate`

## SmartbarInput._removeObservers()
- 位置: L4300-4305
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._observersAdded)` → `this.controller.engineStore.removeObserver()`
- 参照: `this._observersAdded`, `this.onSearchEngineUpdate`

## SmartbarInput._afterTabSelectAndFocusChange()
- 位置: L4307-4343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._resetSearchState()`, `this.formatValue()`, `this.searchModeSwitcher.closePanel()`, `this.view.autoOpen()`, `this.view.close()`
- 条件付き依存: `if (this.focused)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (this.focused)` → `this.getSearchSource()`
- 参照: `this._gotFocusChange`, `this._gotTabSelect`, `this._lastSearchString`, `this.focused`, `this.sapLocation`, `this.windowMode`

## SmartbarInput.#releasePopoverAnchor()
- 位置: L4345-4352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hidePopover()`
- 参照: `this.#popoverAnchorUpdateKey`

## SmartbarInput.incrementPopoverBlockerCount()
- 位置: L4354-4359
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#popoverBlockerCount == 1)` → `this.#releasePopoverAnchor()`
- 参照: `this.#popoverBlockerCount`

## SmartbarInput.decrementPopoverBlockerCount()
- 位置: L4361-4368
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#popoverBlockerCount === 0)` → `this.#updatePopoverAnchor()`
- 参照: `this.#popoverBlockerCount`

## SmartbarInput.#measurePopoverAnchor()
- 位置: async L4370-4398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getBoundsWithoutFlushing()`, `px()`, `resolve()`, `this.#popoverAnchor.style.setProperty()`, `this.#releasePopoverAnchor()`, `this.showPopover()`, `this.window.promiseDocumentFlushed()`, `this.window.requestAnimationFrame()`
- 参照: `getBoundsWithoutFlushing(this.#popoverAnchor).height`, `this.#popoverAnchor`, `this.#popoverAnchorUpdateKey`, `this.#popoverBlockerCount`, `this.isConnected`

## SmartbarInput.setValue()
- 位置: L4412-4462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.initEvent()`, `lazy.ReaderMode.getOriginalUrlObjectForDisplay()`, `this.#setInputValue()`, `this.document.createEvent()`, `this.formatValue()`, `this.inputField.dispatchEvent()`
- 条件付き依存: `if (allowTrim)` → `this._trimValue()`
- 条件付き依存: `if (allowTrim)` → `lazy.BrowserUIUtils.getTrimmedURLPrefix()`
- 条件付き依存: `if (allowTrim)` → `val.startsWith()`
- 条件付き依存: `if (trimmedPrefix && !val.startsWith(trimmedPrefix))` → `trimmedPrefix.startsWith()`
- 条件付き依存: `if (trimmedPrefix && !val.startsWith(trimmedPrefix))` → `trimmedPrefix.endsWith()`
- 条件付き依存: `if (actionType !== undefined)` → `this.setAttribute()`
- 条件付き依存: `if (!(actionType !== undefined))` → `this.removeAttribute()`
- 参照: `lazy.BrowserUIUtils.trimURLProtocol`, `originalUrl.displaySpec`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.valueIsTyped`

## SmartbarInput.#getValueFromResult()
- 位置: L4490-4567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `UrlbarContentUtils.getFixupPrimitives()`, `UrlbarShared.stripPrefixAndTrim()`, `losslessDecodeURI()`, `result.payload.url.startsWith()`, `this.#getSchemelessInput()`
- 条件付き依存: `if (urlOverride !== null)` → `URL.parse()`
- 条件付き依存: `if (urlOverride !== null)` → `losslessDecodeURI()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeSchemeless`, `UrlbarContentUtils.getFixupPrimitives( trimmedUrl, this.isPrivate )?.keywordAsSent`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TIP`, `element?.dataset.input`, `element?.dataset.query`, `element?.dataset.url`, `parsedUrl.URI`, `result.heuristic`, `result.payload.autofillKeyword`, `result.payload.content`, `result.payload.input`, `result.payload.keyword`, `result.payload.query`, `result.payload.suggestion`, `result.payload.url`, `result.type`, `this.isPrivate`, `this.userTypedValue`, `url.URI`
- XPCOM: [`nsILoadInfo`](../../../../dom/base/nsIContentPolicy.idl.md)

## SmartbarInput.#getActionTypeFromResult()
- 位置: L4576-4585
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.type`

## SmartbarInput._resetSearchState()
- 位置: L4591-4594
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._autofillPlaceholder`, `this._lastSearchString`, `this.value`

## SmartbarInput._maybeAutofillPlaceholder()
- 位置: L4606-4674
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!allowAutofill)` → `this.#clearAutofill()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `this._autofillPlaceholder.value .toLocaleLowerCase() .startsWith()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `this._autofillPlaceholder.value .toLocaleLowerCase()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `value.toLocaleLowerCase()`
- 条件付き依存: `if (!( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" ))` → `UrlbarShared.canAutofillURL()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.selectionEnd == this.value.length && this._enableAutofillPlaceholder )` → `this._autofillPlaceholder.value.substring()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.selectionEnd == this.value.length && this._enableAutofillPlaceholder )` → `this._autofillValue()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `autofillValue.length`, `this._autofillPlaceholder`, `this._autofillPlaceholder.adaptiveHistoryInput`, `this._autofillPlaceholder.adaptiveHistoryInput.length`, `this._autofillPlaceholder.type`, `this._autofillPlaceholder.untrimmedValue`, `this._autofillPlaceholder.value`, `this._enableAutofillPlaceholder`, `this.inputField.isHandlingMentions`, `this.searchMode?.engineName`, `this.searchMode?.source`, `this.selectionEnd`, `this.selectionStart`, `this.value`, `this.value.length`, `value.length`

## SmartbarInput.updateTextOverflow()
- 位置: L4681-4725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.isTextDirectionRTL()`, `this.getAttribute()`, `this.window.promiseDocumentFlushed()`
- 条件付き依存: `if (!this._overflowing)` → `this.removeAttribute()`
- 条件付き依存: `if (input && this._overflowing)` → `this.window.requestAnimationFrame()`
- 条件付き依存: `if (this._overflowing)` → `this.setAttribute()`
- 参照: `input.scrollLeft`, `input.scrollLeftMax`, `input.scrollLeftMin`, `this._overflowing`, `this.inputField`, `this.value`

## SmartbarInput._updateUrlTooltip()
- 位置: L4727-4733
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.focused || !this._overflowing)` → `this.inputField.removeAttribute()`
- 条件付き依存: `if (!(this.focused || !this._overflowing))` → `this.inputField.setAttribute()`
- 参照: `this._overflowing`, `this.focused`, `this.untrimmedValue`

## SmartbarInput._getSelectedValueForClipboard()
- 位置: L4735-4834
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `lazy.BrowserUIUtils.getTrimmedURLPrefix()`, `selectedVal.includes()`, `selectedVal.startsWith()`, `this.getAttribute()`, `this.makeURIReadable()`, `uri.schemeIs()`
- 条件付き依存: `if (!selectedVal.includes("/"))` → `this.value.replace()`
- 条件付き依存: `if (!(this.getAttribute("pageproxystate") == "valid"))` → `URL.parse()`
- 条件付き依存: `if (!UrlbarPrefs.get("decodeURLsOnCopy") && !uri.schemeIs("data"))` → `URL.canParse()`
- 条件付き依存: `if (URL.canParse(selectedVal))` → `encodeURI()`
- 参照: `URL.parse(this._untrimmedValue)?.URI`, `result.payload.url`, `result?.autofill?.value`, `this.#isOpenedPageInBlankTargetLoading`, `this.#selectedText`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.editor.selection.rangeCount`, `this.selectionStart`, `this.value`, `this.valueIsTyped`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser.browsingContext .nonWebControlledLoadingURI`, `uri.displaySpec`

## SmartbarInput._toggleActionOverride()
- 位置: L4836-4856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 条件付き依存: `if (event.type == "keydown")` → `this.toggleAttribute()`
- 条件付き依存: `if (event.type == "keydown")` → `this.view.panel.toggleAttribute()`
- 条件付き依存: `if ( this._actionOverrideKeyCount && --this._actionOverrideKeyCount == 0 )` → `this._clearActionOverride()`
- 参照: `KeyEvent.DOM_VK_ALT`, `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_META`, `KeyEvent.DOM_VK_SHIFT`, `event.keyCode`, `event.type`, `this._actionOverrideKeyCount`

## SmartbarInput._clearActionOverride()
- 位置: L4858-4862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeAttribute()`, `this.view.panel.removeAttribute()`
- 参照: `this._actionOverrideKeyCount`

## SmartbarInput._recordSearch()
- 位置: L4894-4921
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSearchSource()`, `this.view.oneOffSearchButtons?.eventTargetIsAOneOff()`, `where.startsWith()`
- 条件付き依存: `if (where.startsWith("tab"))` → `this.parentController.recordSearchInOpenedTab()`
- 条件付き依存: `if (!(where.startsWith("tab")))` → `this.parentController.recordSearch()`
- 参照: `engine.id`, `this._handoffSession`

## SmartbarInput._trimValue()
- 位置: L4931-4944
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.isTextDirectionRTL()`, `UrlbarPrefs.get()`, `lazy.BrowserUIUtils.trimURL()`, `this.#getValueFormatter()`, `this.#getValueFormatter().willShowFormattedMixedContentProtocol()`
- 参照: `this.#isAddressbar`

## SmartbarInput._maybeCanonizeURL()
- 位置: L4957-4999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^\s*[^.:\/\s]+(?:\/.*|\s*)$/i.test()`, `Services.uriFixup.getFixupURIInfo()`, `console.error()`, `suffix.endsWith()`, `this.controller.isCanonizeKeyboardEvent()`, `value.indexOf()`, `value.trim()`
- 条件付き依存: `if (firstSlash >= 0)` → `value.substring()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAGS_MAKE_ALTERNATE_URI`, `Services.locale.urlFixupSuffix`, `info.fixedURI.spec`, `this.value`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.locale` / `Services.uriFixup`

## SmartbarInput._autofillValue()
- 位置: L5021-5061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value.substring()`
- 条件付き依存: `if (this.value === value.substring(0, selectionStart))` → `this.#setInputRangeText()`
- 条件付き依存: `if (this.value === value.substring(0, selectionStart))` → `value.substring()`
- 条件付き依存: `if (this.value === value.substring(0, selectionStart))` → `this.formatValue()`
- 条件付き依存: `if (!(this.value === value.substring(0, selectionStart)))` → `this.setValue()`
- 条件付き依存: `if (!(this.value === value.substring(0, selectionStart)))` → `this.setSelectionRange()`
- 参照: `this._applyingAutofill`, `this._autofillPlaceholder`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this.value`, `this.value.length`

## SmartbarInput.#pickMenuResult()
- 位置: L5070-5117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#loadURL()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.view.close()`
- 条件付き依存: `if (element.dataset.command == "manage")` → `this.window.openPreferences()`
- 参照: `element.dataset.command`, `element.dataset.url`, `result.payload.helpUrl`, `result.source`, `result.type`, `this._lastSearchString`, `this.isPrivate`, `this.sapLocation`, `this.windowMode`

## SmartbarInput.#loadURL()
- 位置: async L5148-5238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `KeyboardEvent.isInstance()`, `keyDownEnterDeferred?.resolve()`, `this.#notifyStartNavigation()`, `this.parentController.loadURL()`, `this.view.close()`
- 条件付き依存: `if (!(loadRequest.engineSearch))` → `losslessDecodeURI()`
- 条件付き依存: `if (where == "current")` → `loadRequest.urlLoad?.url.startsWith()`
- 条件付き依存: `if (!params.avoidBrowserFocus)` → `this.setSelectionRange()`
- 条件付き依存: `if (where != "current")` → `this.handleRevert()`
- 条件付き依存: `if (loadStatus.reverted)` → `this.handleRevert()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `event.keyCode`, `loadRequest.engineSearch`, `loadRequest.engineSearch.query`, `loadRequest.urlLoad`, `loadStatus.browserId`, `loadStatus.reverted`, `new URL(url).URI`, `params.allowPinnedTabHostChange`, `params.allowPopups`, `params.allowThirdPartyFixup`, `params.avoidBrowserFocus`, `params.indicateErrorPageLoad`, `params.private`, `this.#isAddressbar`, `this._keyDownEnterDeferred`, `this._keyDownEnterDeferred.loadedContent`, `this.isPrivate`, `this.value`

## SmartbarInput._initCopyCutController()
- 位置: L5240-5250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.inputField.controllers.insertControllerAt()`
- 参照: `this.#isSmartbarMode`, `this._copyCutController`

## SmartbarInput.#stripURI()
- 位置: L5259-5279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `console.warn()`, `lazy.QueryStringStripper.stripForCopyOrShare()`, `this._getSelectedValueForClipboard()`
- 条件付き依存: `if (strippedURI)` → `this.makeURIReadable()`
- 参照: `e.message`
- XPCOM: `Services.io`

## SmartbarInput.#isClipboardURIValid()
- 位置: L5286-5293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.canParse()`, `this._getSelectedValueForClipboard()`

## SmartbarInput.#canStrip()
- 位置: L5300-5313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `console.warn()`, `lazy.QueryStringStripper.canStripForShare()`, `this._getSelectedValueForClipboard()`
- XPCOM: `Services.io`

## SmartbarInput.#maybeUntrimUrl()
- 位置: L5325-5400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`, `this.setSelectionRange()`, `this.setValue()`
- 条件付き依存: `if (moveCursorToStart)` → `this.setValue()`
- 条件付き依存: `if (moveCursorToStart)` → `this.setSelectionRange()`
- 条件付き依存: `if (!(selectionStart != 0))` → `Services.io.newURI()`
- 条件付き依存: `if (!(selectionStart != 0))` → `[uri.userPass, uri.displayHost] .filter(Boolean) .join()`
- 条件付き依存: `if (!(selectionStart != 0))` → `[uri.userPass, uri.displayHost] .filter()`
- 条件付き依存: `if (!(selectionStart != 0))` → `logger().error()`
- 条件付き依存: `if (!(selectionStart != 0))` → `logger()`
- 条件付き依存: `if (!(selectionStart != 0))` → `this.#selectedText.startsWith()`
- 参照: `"www.".length`, `lazy.BrowserUIUtils.trimURLProtocol.length`, `this.#allTextSelected`, `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._protocolIsTrimmed`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.focused`, `this.selectionEnd`, `this.selectionStart`, `this.value.length`, `this.valueIsTyped`, `uri.displayHost`, `uri.userPass`
- XPCOM: `Services.io`

## SmartbarInput._initStripOnShare()
- 位置: L5404-5451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L5407-5424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createDocumentFragment()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `fragment.appendChild()`, `lazy.ClipboardHelper.copyString()`, `stripOnShare.addEventListener()`, `stripOnShare.setAttribute()`, `this.#stripURI()`
- 参照: `stripOnShare.id`, `strippedURI.displaySpec`, `this.ownerDocument`

## onShowing()
- 位置: L5426-5449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `controller.isCommandEnabled()`, `stripOnShare.removeAttribute()`, `this.#canStrip()`, `this.#isClipboardURIValid()`, `this.document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if ( !UrlbarPrefs.get("privacy.query_stripping.strip_on_share.enabled") )` → `stripOnShare.setAttribute()`
- 条件付き依存: `if ( !controller.isCommandEnabled("cmd_copy") || !this.#isClipboardURIValid() )` → `stripOnShare.setAttribute()`
- 条件付き依存: `if (!this.#canStrip())` → `stripOnShare.setAttribute()`

## SmartbarInput.#pasteAndGoEnabled()
- 位置: L5458-5468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.commandDispatcher .getControllerForCommand()`, `this.document.commandDispatcher .getControllerForCommand("cmd_paste") .isCommandEnabled()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `Services.clipboard.hasDataMatchingFlavors()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `this.#isSmartbarMode`
- XPCOM: `nsIClipboard` / `Services.clipboard`

## SmartbarInput.#pasteForPasteAndGo()
- 位置: L5473-5483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#readClipboardData()`, `this.#readClipboardData()?.getData()`
- 条件付き依存: `if (!this.#isSmartbarMode)` → `this.window.goDoCommand()`
- 参照: `this.#isSmartbarMode`, `this.value`

## SmartbarInput._initPasteAndGo()
- 位置: L5485-5545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L5488-5514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.strings .createBundle()`, `Services.strings .createBundle("chrome://browser/locale/browser.properties") .GetStringFromName()`, `doc.createDocumentFragment()`, `doc.createXULElement()`, `fragment.appendChild()`, `pasteAndGo.addEventListener()`, `pasteAndGo.setAttribute()`, `this.#pasteForPasteAndGo()`, `this.handleCommand()`, `this.parentController.clearLastQueryContextCache()`, `this.select()`, `this.setResultForCurrentValue()`, `this.suppressStartQuery()`
- 条件付き依存: `if (!this._permanentlySuppressStartQuery)` → `this.unsuppressStartQuery()`
- 参照: `pasteAndGo.id`, `this._permanentlySuppressStartQuery`, `this.ownerDocument`
- XPCOM: `Services.strings`

## onShowing()
- 位置: L5515-5543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popup.addEventListener()`, `popup.setAttribute()`, `this.#pasteAndGoEnabled()`, `this.view.close()`
- 条件付き依存: `if (popup.state == "closed")` → `popup.removeAttribute()`
- 条件付き依存: `if (this.#pasteAndGoEnabled())` → `pasteAndGo.removeAttribute()`
- 条件付き依存: `if (!(this.#pasteAndGoEnabled()))` → `pasteAndGo.setAttribute()`
- 参照: `popup.state`, `this.#editContextMenu.popup`

## SmartbarInput._initAutofillDismiss()
- 位置: L5549-5591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L5552-5582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dismiss.addEventListener()`, `dismiss.setAttribute()`, `doc.createDocumentFragment()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `forget.addEventListener()`, `forget.setAttribute()`, `fragment.append()`, `separator.setAttribute()`, `this.#dismissAdaptiveAutofillFromContextMenu()`
- 参照: `this.ownerDocument`

## onShowing()
- 位置: L5583-5589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#autofillDismissContextMenuVisibility()`
- 参照: `dismiss.hidden`, `forget.hidden`, `separator.hidden`

## SmartbarInput.#autofillDismissContextMenuVisibility()
- 位置: L5605-5631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isOriginUrl()`
- 参照: `result.autofill`, `result.autofill.type`, `result.payload.url`, `result?.heuristic`, `this._resultForCurrentValue`, `this.isPrivate`

## SmartbarInput.#dismissAdaptiveAutofillFromContextMenu()
- 位置: async L5640-5656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.parentController .dismissAutofill()`, `this.parentController .dismissAutofill(result.payload.url, action) .catch()`, `this.setValue()`, `this.startQuery()`
- 参照: `console.error`, `result.autofill`, `result.payload.url`, `result?.heuristic`, `this._lastSearchString`, `this._resultForCurrentValue`

## SmartbarInput.#notifyStartNavigation()
- 位置: L5668-5675
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#isAddressbar)` → `Services.obs.notifyObservers()`
- 参照: `this.#isAddressbar`
- XPCOM: `Services.obs`

## SmartbarInput._searchModeForResult()
- 位置: L5689-5737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchModeForToken()`
- 条件付き依存: `if (!(result.type == UrlbarShared.RESULT_TYPE.RESTRICT))` → `UrlbarShared.SEARCH_MODE_RESTRICT.has()`
- 参照: `UrlbarShared.RESULT_TYPE.RESTRICT`, `result.payload.dynamicType`, `result.payload.engine`, `result.payload.keyword`, `result.payload.originalEngine`, `result.providerName`, `result.type`, `searchMode.entry`, `searchMode.restrictType`

## SmartbarInput.#updateCtaSearchEngineInfo()
- 位置: async L5742-5777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `e.getIconURL()`, `engine.getIconURL()`, `this.controller.engineStore .getEngines()`, `this.controller.engineStore .getEngines() .filter()`, `this.controller.engineStore .getEngines() .filter(e => !e.hideOneOffButton) .map()`, `this.controller.engineStore.getEngineByName()`, `this.controller.engineStore.init()`
- 参照: `e.hideOneOffButton`, `e.name`, `engine.name`, `this.#isSmartbarMode`, `this.#smartbarSearchEngineName`, `this._inputCta.searchEngineInfo`, `this._inputCta.searchEngines`, `this.controller.engineStore.default`

## SmartbarInput._updateSearchModeUI()
- 位置: L5785-5850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarSearchTermsPersistence.onSearchModeChanged()`, `this.dispatchEvent()`, `this.getAttribute()`, `this.hasAttribute()`, `this.toggleAttribute()`
- 条件付き依存: `if (this._searchModeIndicatorTitle)` → `this._searchModeIndicatorTitle.removeAttribute()`
- 条件付き依存: `if (!engineName && !source)` → `this.removeAttribute()`
- 条件付き依存: `if (!engineName && !source)` → `this.updatePlaceholder()`
- 条件付き依存: `if (engineName)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (source)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (source)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (this.getAttribute("pageproxystate") == "valid")` → `this.setPageProxyState()`
- 参照: `this.#isAddressbar`, `this._autofillPlaceholder`, `this._searchModeIndicatorTitle`, `this._searchModeIndicatorTitle.textContent`, `this.inputField`, `this.userTypedValue`, `this.value`, `this.window`

## SmartbarInput.#handlePersistedSearchTerms()
- 位置: L5870-5940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarSearchTermsPersistence.shouldPersist()`, `lazy.UrlbarUtils.isPersistedSearchTermsEnabled()`, `state.persist.originalURI.equals()`, `this.toggleAttribute()`
- 条件付き依存: `if (state.persist)` → `this.removeAttribute()`
- 条件付き依存: `if (firstView || cachedUriDidChange)` → `lazy.UrlbarSearchTermsPersistence.setPersistenceState()`
- 条件付き依存: `if (state.persist.shouldPersist && !isSameDocument)` → `Glean.urlbarPersistedsearchterms.viewCount.add()`
- 参照: `state.persist`, `state.persist.searchTerms`, `state.persist.shouldPersist`, `state.persist?.originalURI`, `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.userTypedValue`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser.originalURI`

## SmartbarInput.#initPlaceholderFromPref()
- 位置: L5949-5960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (engineName)` → `this._setPlaceholder()`
- 参照: `this.#isAddressbar`, `this.controller.engineStore.failed`, `this.isPrivate`

## SmartbarInput.#initEngineStoreAfterPaint()
- 位置: async L5973-5982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.engineStore.init()`
- 条件付き依存: `if (document.readyState == "loading")` → `document.addEventListener()`
- 条件付き依存: `if (document.readyState == "loading")` → `this.window.requestIdleCallback()`
- 参照: `document.readyState`

## SmartbarInput.#deferUpdatePlaceholder()
- 位置: async L5994-6037
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.inputField.dataset.l10nId == "urlbar-placeholder-with-name")` → `this.updatePlaceholder()`
- 条件付き依存: `if (!this.value)` → `this.inputField.addEventListener()`
- 条件付き依存: `if (!this.value)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (!(!this.value))` → `this.updatePlaceholder()`
- 参照: `this.inputField.dataset.l10nId`, `this.sapName`, `this.value`

## updateListener()
- 位置: L6013-6027
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.searchModeSwitcher.updateSearchIcon().catch()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.searchModeSwitcher.updateSearchIcon()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.updatePlaceholder()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.inputField.removeEventListener()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 参照: `console.error`, `this.searchMode`, `this.value`

## SmartbarInput.setUnifiedSearchButtonAvailability()
- 位置: L6044-6058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserState()`, `this.querySelector()`, `this.toggleAttribute()`
- 条件付き依存: `if (available)` → `switcher.removeAttribute()`
- 条件付き依存: `if (!(available))` → `switcher.setAttribute()`
- 参照: `this.#isSmartbarMode`, `this.getBrowserState( this.window.gBrowser.selectedBrowser ).isUnifiedSearchButtonAvailable`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.updatePlaceholder()
- 位置: L6063-6078
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (defaultEngine?.isConfigEngine)` → `this._setPlaceholder()`
- 条件付き依存: `if (!(defaultEngine?.isConfigEngine))` → `this._setPlaceholder()`
- 参照: `defaultEngine.name`, `defaultEngine?.isConfigEngine`, `this.#isAddressbar`, `this.controller.engineStore.default`, `this.searchMode`

## SmartbarInput._setPlaceholder()
- 位置: L6087-6114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.document.l10n.setAttributes()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (!this.#isAddressbar)` → `this.document.l10n.setAttributes()`
- 参照: `this.#isAddressbar`, `this.#isSmartbarMode`, `this.inputField`

## SmartbarInput.#maybeSelectAll()
- 位置: L6120-6132
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this._preventClickSelectsAll && this.#compositionState != UrlbarShared.COMPOSITION.COMPOSING && this.focused && this.selectionStart == this.selectionEnd )` → `this.select()`
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionState`, `this.#isSmartbarMode`, `this._preventClickSelectsAll`, `this.focused`, `this.selectionEnd`, `this.selectionStart`

## SmartbarInput._on_command()
- 位置: L6136-6148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if ( !event.target.classList.contains("urlbarView-result-menuitem") && (!event.target.classList.contains("searchbar-engine-one-off-item") || this.searchMode?.ent...)` → `this.controller.engagementEvent.discard()`
- 参照: `this.searchMode?.entry`

## SmartbarInput._on_blur()
- 位置: L6150-6237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `UrlbarPrefs.get()`, `lazy.ExtensionSearchHandler.hasActiveInputSession()`, `logger()`, `logger().debug()`, `this.#isInsideContainer()`, `this._clearActionOverride()`, `this._resetSearchState()`, `this.controller.engagementEvent.record()`, `this.getAttribute()`, `this.getSearchSource()`, `this.removeAttribute()`, `this.view.resultMenu.hasAttribute()`
- 条件付き依存: `if (!( this.value == this._untrimmedValue && !this.userTypedValue && !this.focused ))` → `this.formatValue()`
- 条件付き依存: `if (lazy.ExtensionSearchHandler.hasActiveInputSession())` → `lazy.ExtensionSearchHandler.handleInputCancelled()`
- 条件付き依存: `if ( !UrlbarPrefs.get("ui.popup.disable_autohide") && !this.#isInsideContainer( event.relatedTarget, this.smartbarButtonContainer ) )` → `this.view.close()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") != "valid" && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 条件付き依存: `if (this._keyDownEnterDeferred)` → `this._keyDownEnterDeferred.resolve()`
- 参照: `event.relatedTarget`, `this._autofillPlaceholder`, `this._handoffSession`, `this._isHandoffSession`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._lastSearchString`, `this._untrimmedValue`, `this.focused`, `this.focusedViaMousedown`, `this.sapLocation`, `this.smartbarButtonContainer`, `this.userTypedValue`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`, `this.windowMode`
- XPCOM: `Services.obs`

## SmartbarInput._on_click()
- 位置: L6239-6270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeSelectAll()`, `this.#maybeUntrimUrl()`, `this.handleCommand()`, `this.handleRevert()`, `this.select()`
- 条件付き依存: `if (this.view.isOpen)` → `this.startQuery()`
- 参照: `event.button`, `event.target`, `this._inputContainer`, `this._revertButton`, `this._searchModeIndicatorClose`, `this.goButton`, `this.inputField`, `this.searchMode`, `this.view.isOpen`, `this.view.oneOffSearchButtons`, `this.view.oneOffSearchButtons.selectedButton`

## SmartbarInput._on_contextmenu()
- 位置: L6272-6279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeSelectAll()`
- 参照: `event.button`

## SmartbarInput._on_focus()
- 位置: L6281-6350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `logger()`, `logger().debug()`, `this._updateUrlTooltip()`, `this.formatValue()`, `this.getAttribute()`
- 条件付き依存: `if (!this._hideFocus)` → `this.toggleAttribute()`
- 条件付き依存: `if (!untrim)` → `UrlbarContentUtils.getFixupPrimitives()`
- 条件付き依存: `if (fixedDisplaySpec)` → `UrlbarContentUtils.getDisplaySpec()`
- 条件付き依存: `if (!(expectedDisplaySpec == null))` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (!(expectedDisplaySpec == null))` → `this._untrimmedValue.startsWith()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && this._untrimmedValue.startsWith("https://") )` → `fixedDisplaySpec.replace()`
- 条件付き依存: `if (untrim)` → `this.setValue()`
- 条件付き依存: `if (this.focusedViaMousedown && !this._permanentlySuppressStartQuery)` → `this.view.autoOpen()`
- 条件付き依存: `if (this._untrimOnFocusAfterKeydown)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (!(this.focusedViaMousedown && !this._permanentlySuppressStartQuery))` → `this.inputField.hasAttribute()`
- 条件付き依存: `if (this.inputField.hasAttribute("refocused-by-panel"))` → `this.#maybeSelectAll()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") != "valid" && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 参照: `UrlbarContentUtils.getFixupPrimitives( this.value, this.isPrivate )?.preferredURIDisplaySpec`, `this._hideFocus`, `this._permanentlySuppressStartQuery`, `this._protocolIsTrimmed`, `this._untrimOnFocusAfterKeydown`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.focusedViaMousedown`, `this.isPrivate`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`
- XPCOM: `Services.obs`

## SmartbarInput._on_mouseover()
- 位置: L6352-6354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateUrlTooltip()`

## SmartbarInput._on_draggableregionleftmousedown()
- 位置: L6356-6360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`

## SmartbarInput._on_mousedown()
- 位置: L6362-6445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `event.target.closest()`, `this.#isInsideContainer()`, `this.hasAttribute()`, `this.view.autoOpen()`
- 条件付き依存: `if ( !this.#isInsideContainer(event.composedTarget, this.inputField) && event.composedTarget != this._inputContainer )` → `this.#isInsideContainer()`
- 条件付き依存: `if ( this.#isInsideContainer( event.composedTarget, this.smartbarButtonContainer ) )` → `event.preventDefault()`
- 条件付き依存: `if (!this.#isInsideContainer(event.composedTarget, this.inputField))` → `this.focus()`
- 条件付き依存: `if (this.focusedViaMousedown && !this.#isSmartbarMode)` → `this.setSelectionRange()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.hasAttribute()`
- 条件付き依存: `if (this.view.isOpen && !this.hasAttribute("focused"))` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (this.view.isOpen && !this.hasAttribute("focused"))` → `this.getSearchSource()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`
- 参照: `event.button`, `event.composedTarget`, `event.currentTarget`, `this.#isSmartbarMode`, `this._inputContainer`, `this._lastSearchString`, `this._mousedownOnUrlbarDescendant`, `this._preventClickSelectsAll`, `this.focused`, `this.focusedViaMousedown`, `this.inputField`, `this.sapLocation`, `this.smartbarButtonContainer`, `this.view.isOpen`, `this.window`, `this.windowMode`

## SmartbarInput._on_input()
- 位置: L6447-6596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isPasteEvent()`, `event.inputType?.startsWith()`, `getAgentCommandId()`, `this._maybeAutofillPlaceholder()`, `this.getAttribute()`, `this.removeAttribute()`, `this.startQuery()`, `this.toggleAttribute()`, `this.view.removeAccessibleFocus()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.value === this.userTypedValue && (event.inputType === "deleteContentBackward" || event.inputType === "deleteContentForward") )` → `this.parentController.recordAutofillDeletion()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") == "valid" && this.value != this._lastValidURLStr )` → `this.setPageProxyState()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 条件付き依存: `if ( state.persist?.shouldPersist && this.value !== state.persist.searchTerms )` → `this.removeAttribute()`
- 条件付き依存: `if (previousCommandId && event.inputType && !this.#isAgentCommand)` → `Glean.smartWindow.agentCommandRemove.record()`
- 条件付き依存: `if (previousCommandId && event.inputType && !this.#isAgentCommand)` → `String()`
- 条件付き依存: `if (this.inputField.hasMention || this.#isAgentCommand)` → `this.suppressStartQuery()`
- 条件付き依存: `if (!this._permanentlySuppressStartQuery)` → `this.unsuppressStartQuery()`
- 条件付き依存: `if (!value)` → `this.#updateSmartbarCTAButton()`
- 条件付き依存: `if (this.view.isOpen)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("closeOtherPanelsOnOpen"))` → `this.window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow) .rollupAllPopups()`
- 条件付き依存: `if (UrlbarPrefs.get("closeOtherPanelsOnOpen"))` → `this.window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (UrlbarPrefs.get("closeOtherPanelsOnOpen"))` → `this.window.docShell.treeOwner .QueryInterface()`
- 条件付き依存: `if (!willShowResults)` → `this.view.clear()`
- 条件付き依存: `if (!this.searchMode || !this.view.oneOffSearchButtons?.hasView)` → `this.view.close()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.view.clear()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `UrlbarShared.COMPOSITION.CANCELED`, `UrlbarShared.COMPOSITION.COMPOSING`, `UrlbarShared.COMPOSITION.NONE`, `event.data`, `event.inputType`, `state.persist.searchTerms`, `state.persist.shouldPersist`, `state.persist?.shouldPersist`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this.#inputEpoch`, `this.#isAddressbar`, `this.#isAgentCommand`, `this.#isSmartbarMode`, `this._autofillPlaceholder`, `this._lastValidURLStr`, `this._permanentlySuppressStartQuery`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.controller.userSelectionBehavior`, `this.conversationTelemetryInfo`, `this.inputField.hasMention`, `this.sapLocation`, `this.searchMode`, `this.untrimmedValue`, `this.userTypedValue`, `this.value`, `this.valueIsTyped`, `this.view.isOpen`, `this.view.oneOffSearchButtons?.hasView`, `this.window.gBrowser.selectedBrowser`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../../netwerk/base/nsIChannel.idl.md)

## SmartbarInput._on_selectionchange()
- 位置: L6598-6612
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._applyingAutofill`, `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._autofillPlaceholder.value`, `this.selectionEnd`, `this.selectionStart`, `this.userTypedValue`, `this.value`

## SmartbarInput._on_select()
- 位置: L6614-6648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clipboard.isClipboardTypeSupported()`, `lazy.ClipboardHelper.copyStringToClipboard()`, `this._getSelectedValueForClipboard()`
- 参照: `Services.clipboard.kSelectionClipboard`, `this._suppressPrimaryAdjustment`, `this.window.windowUtils.isHandlingUserInput`
- XPCOM: `Services.clipboard`

## SmartbarInput._on_overflow()
- 位置: L6650-6653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateTextOverflow()`
- 参照: `this._overflowing`

## SmartbarInput._on_underflow()
- 位置: L6655-6659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateUrlTooltip()`, `this.updateTextOverflow()`
- 参照: `this._overflowing`

## SmartbarInput._on_paste()
- 位置: L6661-6712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getFixupPrimitives()`, `UrlbarShared.sanitizeTextFromClipboard()`, `event.clipboardData.getData()`, `oldStart.trim()`, `oldValue.substring()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `event.preventDefault()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `event.stopImmediatePropagation()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.setValue()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("pageproxystate") == "valid")` → `this.setPageProxyState()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.toggleAttribute()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.setSelectionRange()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.startQuery()`
- 参照: `oldStart.length`, `pasteData.length`, `this._untrimmedValue`, `this.isPrivate`, `this.selectionEnd`, `this.selectionStart`, `this.userTypedValue`, `this.value`

## SmartbarInput.#makeQueryContext()
- 位置: L6728-6783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isPasteEvent()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!(this.#isSmartbarMode))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (this.window.gBrowser)` → `parseInt()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.window.gBrowser.selectedBrowser?.getAttribute()`
- 条件付き依存: `if (this.searchMode)` → `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_SOURCE.ACTIONS`, `event.data?.length`, `lazy.UrlbarQueryContext`, `options.currentPage`, `options.searchMode`, `options.sources`, `options.tabGroup`, `options.userContextId`, `this.#isSmartbarMode`, `this.isPrivate`, `this.sapName`, `this.searchMode`, `this.searchMode.source`, `this.searchMode?.source`, `this.window.gBrowser`, `this.window.gBrowser.currentURI?.spec`, `this.window.gBrowser.selectedTab.group?.id`

## SmartbarInput._on_scroll()
- 位置: L6794-6802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.supports()`, `this.#updatePanelScrollFade()`
- 参照: `event.target`, `this.view.panel`

## SmartbarInput.#updatePanelScrollFade()
- 位置: L6804-6823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `progress.toFixed()`, `this.view.panel.style.setProperty()`, `this.view.panel.toggleAttribute()`, `this.window.requestAnimationFrame()`
- 参照: `this.#scrollAnimationId`, `this.view.panel`

## SmartbarInput._on_scrollend()
- 位置: L6825-6827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateTextOverflow()`

## SmartbarInput._on_TabSelect()
- 位置: L6829-6840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._afterTabSelectAndFocusChange()`
- 条件付き依存: `if (this.#isSidebarMode)` → `this.#updateContextChips()`
- 参照: `this.#isSidebarMode`, `this._gotTabSelect`, `this._untrimOnFocusAfterKeydown`

## SmartbarInput._on_TabAttrModified()
- 位置: L6842-6851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.detail.changed.includes()`
- 条件付き依存: `if ( this.#isSidebarMode && event.target == this.window.gBrowser.selectedTab && (event.detail.changed.includes("image") || event.detail.changed.includes("label")) )` → `this.#updateContextChips()`
- 参照: `event.target`, `this.#isSidebarMode`, `this.window.gBrowser.selectedTab`

## SmartbarInput._on_TabClose()
- 位置: L6853-6862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.handleBounceEventTrigger()`
- 条件付き依存: `if (this.view.isOpen)` → `this.startQuery()`
- 参照: `event.target.linkedBrowser`, `this.view.isOpen`

## SmartbarInput._on_beforeinput()
- 位置: L6864-6881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view?.shouldSpaceActivateSelectedElement()`
- 条件付き依存: `if (event.data && this._keyDownEnterDeferred)` → `event.preventDefault()`
- 条件付き依存: `if ( this.#isSmartbarMode && event.data == " " && this.view?.shouldSpaceActivateSelectedElement?.() )` → `event.preventDefault()`
- 参照: `event.data`, `this.#isSmartbarMode`, `this._keyDownEnterDeferred`

## SmartbarInput._on_keydown()
- 位置: L6883-6974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.handleKeyNavigation()`, `this.eventBufferer.maybeDeferEvent()`, `this.eventBufferer.shouldDeferEvent()`, `this.view.resultMenu.hasAttribute()`
- 条件付き依存: `if (event.currentTarget == this.window)` → `this.#isInsideContainer()`
- 条件付き依存: `if ( this.#isInsideContainer( event.composedTarget, this.smartbarButtonContainer ) )` → `this.#onActionButtonsKeyDown()`
- 条件付き依存: `if ( this.#isSmartbarMode && event.keyCode === KeyEvent.DOM_VK_RETURN && (event.shiftKey || this.#smartbarAssistantIsGenerating) )` → `event.preventDefault()`
- 条件付き依存: `if (this._keyDownEnterDeferred)` → `this._keyDownEnterDeferred.reject()`
- 条件付き依存: `if (event.keyCode === KeyEvent.DOM_VK_RETURN)` → `Promise.withResolvers()`
- 条件付き依存: `if (event.keyCode === KeyEvent.DOM_VK_RETURN)` → `UrlbarContentUtils.getPlatform()`
- 条件付き依存: `if (!event.repeat)` → `this._toggleActionOverride()`
- 条件付き依存: `if (this.eventBufferer.shouldDeferEvent(event))` → `this.controller.handleKeyNavigation()`
- 参照: `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_LEFT`, `KeyEvent.DOM_VK_META`, `KeyEvent.DOM_VK_RETURN`, `event._disableCanonization`, `event.composedTarget`, `event.ctrlKey`, `event.currentTarget`, `event.keyCode`, `event.metaKey`, `event.repeat`, `event.shiftKey`, `this.#allTextSelected`, `this.#allTextSelectedOnKeyDown`, `this.#inputEpoch`, `this.#isSmartbarMode`, `this.#smartbarAssistantIsGenerating`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._keyDownEnterDeferred.inputEpoch`, `this._untrimOnFocusAfterKeydown`, `this.controller`, `this.focused`, `this.smartbarButtonContainer`, `this.window`

## SmartbarInput._on_keyup()
- 位置: L6976-7009
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleActionOverride()`
- 条件付き依存: `if (this.#allTextSelectedOnKeyDown)` → `this.#isHomeKeyUpEvent()`
- 条件付き依存: `if (this.#allTextSelectedOnKeyDown)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (this._keyDownEnterDeferred && !this._finishingDeferredEnter)` → `this.#finishDeferredEnter()`
- 参照: `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_META`, `event.currentTarget`, `event.keyCode`, `this.#allTextSelectedOnKeyDown`, `this._finishingDeferredEnter`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._untrimOnFocusAfterKeydown`, `this.selectionEnd`, `this.selectionStart`, `this.window`

## SmartbarInput.#finishDeferredEnter()
- 位置: async L7015-7052
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (keyDownEnterDeferred.loadedContent)` → `this.parentController.focusBrowser()`
- 条件付き依存: `if (focused && keyDownEnterDeferred.inputEpoch === this.#inputEpoch)` → `this.setSelectionRange()`
- 条件付き依存: `if (!(keyDownEnterDeferred.loadedContent))` → `keyDownEnterDeferred.resolve()`
- 参照: `keyDownEnterDeferred.inputEpoch`, `keyDownEnterDeferred.loadedContent`, `keyDownEnterDeferred.promise`, `this.#inputEpoch`, `this._finishingDeferredEnter`, `this._keyDownEnterDeferred`

## SmartbarInput._on_compositionstart()
- 位置: L7054-7084
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (this.searchMode)` → `this.confirmSearchMode()`
- 条件付き依存: `if (this.view.isOpen)` → `this.view.close()`
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this.searchMode`, `this.userTypedValue`, `this.value`, `this.view.isOpen`

## SmartbarInput._on_compositionend()
- 位置: L7086-7119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("keepPanelOpenDuringImeComposition"))` → `this.view.clearSelection()`
- 条件付き依存: `if ( !event.data && !this.#compositionHadText && this.#compositionClosedPopup && !UrlbarPrefs.get("keepPanelOpenDuringImeComposition") )` → `this.startQuery()`
- 参照: `UrlbarShared.COMPOSITION.CANCELED`, `UrlbarShared.COMPOSITION.COMMIT`, `UrlbarShared.COMPOSITION.COMPOSING`, `UrlbarShared.COMPOSITION.NONE`, `event.data`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this._resultForCurrentValue`

## SmartbarInput._on_dragstart()
- 位置: L7121-7157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.escapeHtmlEntities()`, `event.dataTransfer.setData()`, `event.stopPropagation()`, `this.getAttribute()`, `this.inputField.compareDocumentPosition()`, `this.makeURIReadable()`, `this.view.close()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `event.dataTransfer.effectAllowed`, `event.originalTarget`, `event.target`, `this.#allTextSelected`, `this.inputField`, `this.window.gBrowser.contentTitle`, `this.window.gBrowser.currentURI`, `uri.displaySpec`

## SmartbarInput._on_dragover()
- 位置: L7164-7168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getDroppableData()`
- 参照: `event.dataTransfer.dropEffect`

## SmartbarInput._on_drop()
- 位置: L7175-7200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.isInstance()`, `getDroppableData()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `Services.droppedLinkHandler.getTriggeringPrincipal()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.setPageProxyState()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.focus()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.#makeQueryContext()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.parentController.setLastQueryContextCache()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.controller.engagementEvent.start()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.handleNavigation()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.setURI()`
- 参照: `droppedItem.href`, `this.#isAddressbar`, `this.userTypedValue`, `this.value`, `this.window.gBrowser.currentURI.spec`
- XPCOM: `Services.droppedLinkHandler`

## SmartbarInput._on_customizationstarting()
- 位置: L7202-7205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.blur()`, `this.incrementPopoverBlockerCount()`

## SmartbarInput._on_aftercustomization()
- 位置: L7207-7210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePopoverAnchor()`, `this.decrementPopoverBlockerCount()`

## SmartbarInput.uiDensityChanged()
- 位置: L7212-7217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePopoverAnchor()`
- 参照: `this.#popoverBlockerCount`

## SmartbarInput.#allTextSelected()
- 位置: L7220-7222
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectionEnd`, `this.selectionStart`, `this.value.length`

## SmartbarInput.#getSchemelessInput()
- 位置: L7233-7239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http://", "https://", "file://"].every()`, `value.trim()`, `value.trim().startsWith()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeSchemeful`, `Ci.nsILoadInfo.SchemelessInputTypeSchemeless`
- XPCOM: [`nsILoadInfo`](../../../../dom/base/nsIContentPolicy.idl.md)

## SmartbarInput.#isOpenedPageInBlankTargetLoading()
- 位置: L7241-7248
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.gBrowser.selectedBrowser.browsingContext .nonWebControlledLoadingURI`, `this.window.gBrowser.selectedBrowser.browsingContext.sessionHistory ?.count`

## SmartbarInput.#selectedText()
- 位置: L7270-7277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.editor.selection.toStringWithFormat()`
- 参照: `Ci.nsIDocumentEncoder.OutputPreformatted`, `Ci.nsIDocumentEncoder.OutputRaw`
- XPCOM: [`nsIDocumentEncoder`](../../../../dom/serializers/nsIDocumentEncoder.idl.md)

## SmartbarInput.#isHomeKeyUpEvent()
- 位置: L7285-7309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_HOME`, `KeyEvent.DOM_VK_META`, `KeyboardEvent.DOM_VK_A`, `KeyboardEvent.DOM_VK_LEFT`, `event.ctrlKey`, `event.keyCode`, `event.shiftKey`, `this._isKeyDownWithMetaAndLeft`

## SmartbarInput.#updateSmartbarCTAButton()
- 位置: L7317-7345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateGoGuardrail()`
- 参照: `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.URL`, `firstResult.heuristic`, `firstResult.type`, `this.#detectedIntent`, `this.#smartbarActionLocked`, `this.smartbarAction`, `this.value`

## SmartbarInput.getCurrentContextData()
- 位置: L7354-7359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getContextPageUrl()`, `this.getResolvedContextWebsites()`

## SmartbarInput.getContextPageUrl()
- 位置: L7367-7376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `lazy.getCurrentTabUrl()`
- 参照: `currentTabUrl?.spec`, `this.#isSidebarMode`, `this.#removedImplicitTabUrl`, `this.window`

## SmartbarInput.getResolvedContextWebsites()
- 位置: L7384-7411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidates .filter()`, `getContextMentionKey()`, `seen.add()`, `seen.has()`
- 条件付き依存: `if (url && url != this.#removedImplicitTabUrl)` → `candidates.unshift()`
- 条件付き依存: `if (url && url != this.#removedImplicitTabUrl)` → `this.#resolveTabIconSrc()`
- 参照: `tab.image`, `tab.label`, `tab?.linkedBrowser.currentURI?.spec`, `this.#contextWebsites`, `this.#isSidebarMode`, `this.#removedImplicitTabUrl`, `this.window.gBrowser?.selectedTab`

## SmartbarInput.#updateContextChips()
- 位置: L7416-7426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `finalWebsites.forEach()`, `this.#ensureWebsiteIcon()`, `this.#findWebsiteContextChipsContainer()`, `this.getResolvedContextWebsites()`
- 参照: `container.hidden`, `container.removable`, `container.websites`, `finalWebsites.length`

## SmartbarInput.updateContextChips()
- 位置: L7432-7434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`

## SmartbarInput.contextChips()
- 位置: L7442-7444
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contextWebsites`

## SmartbarInput.removedImplicitContextChip()
- 位置: L7452-7454
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#removedImplicitTabUrl`

## SmartbarInput.restoreContextChips()
- 位置: L7465-7473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`
- 参照: `this.#contextWebsites`, `this.#removedImplicitTabUrl`, `this.window.gBrowser?.selectedTab?.linkedBrowser?.currentURI?.spec`

## SmartbarInput.#resolveTabIconSrc()
- 位置: L7485-7489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getIconForUrl()`, `tabImage?.startsWith()`

## SmartbarInput.#ensureWebsiteIcon()
- 位置: L7496-7501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getIconForUrl()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `site.iconSrc`, `site.type`, `site.url`

## SmartbarInput.#findWebsiteContextChipsContainer()
- 位置: L7507-7517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`
- 参照: `this.#websiteContextChipsContainer`, `this.#websiteContextChipsContainer?.isConnected`

## SmartbarInput.isSidebarMode()
- 位置: L7519-7521
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isSidebarMode`

## SmartbarInput.isSidebarMode()
- 位置: L7526-7535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`, `this.querySelector()`
- 参照: `modelSelect.sidebarMode`, `this.#isSidebarMode`

## SmartbarInput.addContextMention()
- 位置: L7542-7563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getContextMentionKey()`, `this.#contextWebsites.some()`, `this.#updateContextChips()`, `this.dispatchEvent()`
- 参照: `mention.url`, `this.#contextWebsites`, `this.#removedImplicitTabUrl`

## SmartbarInput.removeContextMention()
- 位置: L7570-7594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contextWebsites.filter()`
- 条件付き依存: `if (this.#contextWebsites.length !== originalLength || isCurrentTab)` → `this.#updateContextChips()`
- 条件付き依存: `if (this.#contextWebsites.length !== originalLength || isCurrentTab)` → `this.dispatchEvent()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `site.groupId`, `site.type`, `site.url`, `this.#contextWebsites`, `this.#contextWebsites.length`, `this.#isSidebarMode`, `this.#removedImplicitTabUrl`, `this.window.gBrowser.selectedTab.linkedBrowser.currentURI?.spec`

## getDroppableData()
- 位置: L7606-7653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`, `event.dataTransfer.getData()`
- 条件付き依存: `if (links[0]?.url)` → `event.preventDefault()`
- 条件付き依存: `if (links[0]?.url)` → `UrlbarShared.stripUnsafeProtocolOnPaste()`
- 条件付き依存: `if (UrlbarShared.stripUnsafeProtocolOnPaste(href) != href)` → `event.stopImmediatePropagation()`
- 条件付き依存: `if (links[0]?.url)` → `URL.parse()`
- 条件付き依存: `if (url)` → `Services.droppedLinkHandler.getTriggeringPrincipal()`
- 条件付き依存: `if (url)` → `Services.scriptSecurityManager.checkLoadURIStrWithPrincipal()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_INHERIT_PRINCIPAL`, `links[0].url`, `links[0]?.url`, `url.href`
- XPCOM: `nsIScriptSecurityManager` / `Services.droppedLinkHandler` / `Services.scriptSecurityManager`

## losslessDecodeURI()
- 位置: L7664-7744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/%25(?:3B|2F|3F|3A|40|26|3D|2B|24|2C|23)/i.test()`, `value.replace()`
- 条件付き依存: `if (!/%25(?:3B|2F|3F|3A|40|26|3D|2B|24|2C|23)/i.test(value))` → `["https", "http", "file", "ftp"].includes()`
- 条件付き依存: `if (decodeASCIIOnly)` → `value.replace()`
- 条件付き依存: `if (!(decodeASCIIOnly))` → `decodeURI()`
- 参照: `aURI.displaySpec`, `aURI.scheme`

## CopyCutController.constructor()
- 位置: L7754-7756
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.urlbar`

## CopyCutController.doCommand()
- 位置: L7762-7787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClipboardHelper.copyString()`, `this.isCommandEnabled()`, `urlbar._getSelectedValueForClipboard()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.value.substring()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.setSelectionRange()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.dispatchEvent()`
- 参照: `this.urlbar`, `urlbar.inputField.value`, `urlbar.selectionEnd`, `urlbar.selectionStart`, `urlbar.window`

## CopyCutController.supportsCommand()
- 位置: L7795-7802
- 役割: (未記入)
- 触るとき: (未記入)

## CopyCutController.isCommandEnabled()
- 位置: L7810-7816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.supportsCommand()`
- 参照: `this.urlbar.readOnly`, `this.urlbar.selectionEnd`, `this.urlbar.selectionStart`

## CopyCutController.onEvent()
- 位置: L7818-7818
- 役割: (未記入)
- 触るとき: (未記入)

## AddSearchEngineHelper.constructor()
- 位置: L7843-7846
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `input.view.oneOffSearchButtons`, `this.input`, `this.shortcutButtons`

## AddSearchEngineHelper.maxInlineEngines()
- 位置: L7854-7856
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.shortcutButtons._maxInlineAddEngines`

## AddSearchEngineHelper.setEnginesFromBrowser()
- 位置: L7864-7872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engines.slice()`, `this._sameEngines()`
- 条件付き依存: `if (!this._sameEngines(this.engines, engines))` → `this.shortcutButtons?.updateWebEngines()`
- 参照: `browser.browsingContext`, `this.browsingContext`, `this.engines`

## AddSearchEngineHelper._sameEngines()
- 位置: L7874-7882
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.deepEqual()`, `engines1.map()`, `engines2.map()`
- 参照: `e.title`, `engines1?.length`, `engines2?.length`

## AddSearchEngineHelper._createMenuitem()
- 位置: L7884-7901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `doc.l10n.setAttributes()`, `elt.addEventListener()`, `elt.classList.add()`, `elt.setAttribute()`, `this._onCommand.bind()`
- 条件付き依存: `if (engine.icon)` → `elt.setAttribute()`
- 条件付き依存: `if (!(engine.icon))` → `elt.removeAttribute()`
- 参照: `engine.icon`, `engine.title`, `engine.uri`, `this.input.ownerDocument`

## AddSearchEngineHelper._createMenu()
- 位置: L7903-7916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `doc.l10n.setAttributes()`, `elt.appendChild()`, `elt.classList.add()`, `elt.setAttribute()`
- 条件付き依存: `if (engine.icon)` → `elt.setAttribute()`
- 条件付き依存: `if (engine.icon)` → `ChromeUtils.encodeURIForSrcset()`
- 参照: `engine.icon`, `this.input.ownerDocument`

## AddSearchEngineHelper.createContextSeparator()
- 位置: L7933-7940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextSeparator.classList.add()`, `this.contextSeparator.setAttribute()`, `this.input.ownerDocument.createXULElement()`
- 参照: `this.contextSeparator`, `this.contextSeparator.collapsed`

## AddSearchEngineHelper.refreshContextMenu()
- 位置: L7948-7985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elt.remove()`, `this._createMenuitem()`
- 条件付き依存: `if (engines.length > this.maxInlineEngines)` → `this._createMenu()`
- 条件付き依存: `if (engines.length > this.maxInlineEngines)` → `this.contextSeparator.insertAdjacentElement()`
- 条件付き依存: `if (engines.length > this.maxInlineEngines)` → `this.#contextItems.push()`
- 条件付き依存: `if (curElt.localName == "menupopup")` → `curElt.appendChild()`
- 条件付き依存: `if (!(curElt.localName == "menupopup"))` → `curElt.insertAdjacentElement()`
- 条件付き依存: `if (!(curElt.localName == "menupopup"))` → `this.#contextItems.push()`
- 参照: `curElt.localName`, `elt.lastElementChild`, `engines.length`, `this.#contextItems`, `this.contextSeparator`, `this.contextSeparator.collapsed`, `this.engines`, `this.maxInlineEngines`

## AddSearchEngineHelper._onCommand()
- 位置: async L7987-7998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `lazy.SearchUIUtils.addOpenSearchEngine()`
- 条件付き依存: `if (added)` → `this.refreshContextMenu()`
- 参照: `console.error`, `this.browsingContext`
