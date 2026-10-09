# browser/components/downloads/content/downloads.js

source: browser/components/downloads/content/downloads.js
source-hash: 311e0d736c78077b3e095156b35f558012e29883
lines: 1891

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Integration.downloads.defineESModuleGetter()`, `XPCOMUtils.defineConstant()`, `document.getElementById()`

## initialize()
- 位置: L79-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getData(window).addView()`, `DownloadsCommon.getSummary()`, `DownloadsCommon.getSummary(window, DownloadsView.kItemCountLimit).addView()`, `DownloadsCommon.initializeAllDataLinks()`, `DownloadsCommon.log()`, `DownloadsPanel._attachEventListeners()`, `DownloadsViewController.initialize()`, `document.getElementById()`, `downloadPanelCommands.addEventListener()`, `goUpdateCommand()`, `window.addEventListener()`
- 条件付き依存: `if (DownloadIntegration.downloadSpamProtection)` → `DownloadIntegration.downloadSpamProtection.register()`
- 条件付き依存: `if (this._initialized)` → `DownloadsCommon.log()`
- 参照: `DownloadIntegration.downloadSpamProtection`, `DownloadsView.kItemCountLimit`, `this._initialized`, `this.onWindowUnload`, `this.panel.hidden`

## terminate()
- 位置: L134-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getData(window).removeView()`, `DownloadsCommon.getSummary()`, `DownloadsCommon.getSummary( window, DownloadsView.kItemCountLimit ).removeView()`, `DownloadsCommon.log()`, `DownloadsViewController.terminate()`, `document .getElementById()`, `document .getElementById("downloadPanelCommands") .removeEventListener()`, `this._unattachEventListeners()`, `this.hidePanel()`, `window.removeEventListener()`
- 条件付き依存: `if (!this._initialized)` → `DownloadsCommon.log()`
- 条件付き依存: `if (DownloadIntegration.downloadSpamProtection)` → `DownloadIntegration.downloadSpamProtection.unregister()`
- 参照: `DownloadIntegration.downloadSpamProtection`, `DownloadsSummary.active`, `DownloadsView.kItemCountLimit`, `this._initialized`, `this.onWindowUnload`

## panel()
- 位置: L174-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.panel`

## showPanel()
- 位置: L185-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsButton.unhide()`, `DownloadsCommon.log()`, `Glean.downloads.panelShown.add()`, `setTimeout()`, `this._openPopupIfDataReady()`, `this.initialize()`
- 条件付き依存: `if (this.isPanelShowing)` → `DownloadsCommon.log()`
- 条件付き依存: `if (this.isPanelShowing)` → `this._focusPanel()`
- 参照: `this._openedManually`, `this._preventFocusRing`, `this._waitingDataForOpen`, `this.isPanelShowing`

## hidePanel()
- 位置: L217-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `PanelMultiView.hidePopup()`
- 条件付き依存: `if (!this.isPanelShowing)` → `DownloadsCommon.log()`
- 参照: `this.isPanelShowing`, `this.panel`

## isPanelShowing()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._waitingDataForOpen`, `this.panel.state`

## handleEvent()
- 位置: L238-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.showDownloadsHistory()`, `DownloadsView._onDownloadContextMenu()`, `DownloadsView._onDownloadDragStart()`, `DownloadsView._onDownloadMouseOut()`, `DownloadsView._onDownloadMouseOver()`, `DownloadsView.richListBox.hasAttribute()`, `goDoCommand()`, `this._onKeyDown()`, `this._onKeyPress()`, `this._onPopupHidden()`, `this._onPopupShown()`, `this._onSelect()`, `this.panel.contains()`
- 条件付き依存: `if (aEvent.currentTarget == DownloadsView.downloadsHistory)` → `DownloadsPanel.showDownloadsHistory()`
- 条件付き依存: `if ( aEvent.currentTarget == DownloadsBlockedSubview.elements.deleteButton )` → `DownloadsBlockedSubview.confirmBlock()`
- 条件付き依存: `if ( !DownloadsView.contextMenuOpen && !DownloadsView.subViewOpen && this.panel.contains(document.activeElement) )` → `document.activeElement.blur()`
- 条件付き依存: `if ( !DownloadsView.contextMenuOpen && !DownloadsView.subViewOpen && this.panel.contains(document.activeElement) )` → `DownloadsView.richListBox.removeAttribute()`
- 条件付き依存: `if ( !DownloadsView.contextMenuOpen && !DownloadsView.subViewOpen && this.panel.contains(document.activeElement) )` → `this._focusPanel()`
- 条件付き依存: `if (DownloadsView.richListBox.hasAttribute("disabled"))` → `this._handlePotentiallySpammyDownloadActivation()`
- 条件付き依存: `if (aEvent.currentTarget == DownloadsSummary._summaryNode)` → `DownloadsSummary._onKeyDown()`
- 参照: `DownloadsBlockedSubview.elements.deleteButton`, `DownloadsSummary._summaryNode`, `DownloadsView.contextMenuOpen`, `DownloadsView.downloadsHistory`, `DownloadsView.subViewOpen`, `aEvent.currentTarget`, `aEvent.target.id`, `aEvent.type`, `document.activeElement`, `this._preventFocusRing`

## onViewLoadCompleted()
- 位置: L321-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._openPopupIfDataReady()`

## onWindowUnload()
- 位置: L327-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.terminate()`

## _onPopupShown()
- 位置: L332-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.log()`, `this._focusPanel()`
- 参照: `DownloadsCommon.SUPPRESS_PANEL_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `DownloadsView.richListBox.itemCount`, `DownloadsView.richListBox.selectedIndex`, `aEvent.target`, `this.panel`

## _onPopupHidden()
- 位置: L352-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsButton.releaseAnchor()`, `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.log()`, `DownloadsView.richListBox.removeAttribute()`
- 条件付き依存: `if (this._delayTimeout)` → `DownloadsView.richListBox.removeAttribute()`
- 条件付き依存: `if (this._delayTimeout)` → `clearTimeout()`
- 条件付き依存: `if (this._delayTimeout)` → `this._stopWatchingForSpammyDownloadActivation()`
- 参照: `DownloadsCommon.SUPPRESS_PANEL_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `aEvent.target`, `this._delayTimeout`, `this.panel`

## showDownloadsHistory()
- 位置: L382-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserCommands.downloadsUI()`, `DownloadsCommon.log()`, `this.hidePanel()`

## _attachEventListeners()
- 位置: L398-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsBlockedSubview.elements.deleteButton.addEventListener()`, `DownloadsSummary._summaryNode.addEventListener()`, `DownloadsView.downloadsHistory.addEventListener()`, `DownloadsView.richListBox.addEventListener()`, `this.panel.addEventListener()`

## _unattachEventListeners()
- 位置: L429-449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsBlockedSubview.elements.deleteButton.removeEventListener()`, `DownloadsSummary._summaryNode.removeEventListener()`, `DownloadsView.downloadsHistory.removeEventListener()`, `DownloadsView.richListBox.removeEventListener()`, `this.panel.removeEventListener()`

## _onKeyPress()
- 位置: L451-461
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (document.activeElement === DownloadsView.richListBox)` → `DownloadsView.onDownloadKeyPress()`
- 参照: `DownloadsView.richListBox`, `aEvent.altKey`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `document.activeElement`

## _onKeyDown()
- 位置: L468-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `DownloadURL()`, `DownloadsCommon.log()`, `DownloadsView.richListBox.hasAttribute()`, `NetUtil.newURI()`, `Services.clipboard.getData()`, `aEvent.getModifierState()`, `data.value .QueryInterface()`, `data.value .QueryInterface(Ci.nsISupportsString) .data.split()`, `flavors.forEach()`, `trans.getAnyTransferData()`, `trans.init()`
- 条件付き依存: `if (DownloadsView.richListBox.hasAttribute("disabled"))` → `this._handlePotentiallySpammyDownloadActivation()`
- 条件付き依存: `if ( aEvent.keyCode == aEvent.DOM_VK_UP || aEvent.keyCode == aEvent.DOM_VK_DOWN )` → `richListBox.setAttribute()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_UP && richListBox.firstElementChild)` → `document .getElementById("downloadsFooter") .contains()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_UP && richListBox.firstElementChild)` → `document .getElementById()`
- 条件付き依存: `if ( document .getElementById("downloadsFooter") .contains(document.activeElement) )` → `richListBox.focus()`
- 条件付き依存: `if ( document .getElementById("downloadsFooter") .contains(document.activeElement) )` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_DOWN)` → `document .getElementById("downloadsFooter") .contains()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_DOWN)` → `document .getElementById()`
- 条件付き依存: `if ( DownloadsView.canChangeSelectedItem && (richListBox.selectedItem === richListBox.lastElementChild || document .getElementById("downloadsFooter") .contains(d...)` → `DownloadsFooter.focus()`
- 条件付き依存: `if ( DownloadsView.canChangeSelectedItem && (richListBox.selectedItem === richListBox.lastElementChild || document .getElementById("downloadsFooter") .contains(d...)` → `aEvent.preventDefault()`
- 参照: `Ci.nsISupportsString`, `Ci.nsITransferable`, `DownloadsView.canChangeSelectedItem`, `DownloadsView.richListBox`, `Services.clipboard.kGlobalClipboard`, `aEvent.DOM_VK_DOWN`, `aEvent.DOM_VK_UP`, `aEvent.DOM_VK_V`, `aEvent.keyCode`, `document.activeElement`, `richListBox.firstElementChild`, `richListBox.lastElementChild`, `richListBox.selectedIndex`, `richListBox.selectedItem`, `trans.addDataFlavor`, `uri.spec`
- XPCOM: [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## _onSelect()
- 位置: L553-563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `item.querySelector()`, `richlistbox.itemChildren.forEach()`
- 条件付き依存: `if (item.selected)` → `button.removeAttribute()`
- 条件付き依存: `if (!(item.selected))` → `button.setAttribute()`
- 参照: `DownloadsView.richListBox`, `item.selected`

## _focusPanel()
- 位置: L569-594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.contains()`, `this.panel.shadowRoot.contains()`
- 条件付き依存: `if (DownloadsView.richListBox.itemCount > 0)` → `DownloadsView.richListBox.focus()`
- 条件付き依存: `if (!(DownloadsView.richListBox.itemCount > 0))` → `DownloadsFooter.focus()`
- 参照: `DownloadsView.canChangeSelectedItem`, `DownloadsView.richListBox.itemCount`, `DownloadsView.richListBox.selectedIndex`, `document.activeElement`, `focusOptions.focusVisible`, `this._preventFocusRing`, `this.panel.state`

## _delayPopupItems()
- 位置: L596-601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsView.richListBox.setAttribute()`, `this._refreshDelayTimer()`, `this._startWatchingForSpammyDownloadActivation()`

## _refreshDelayTimer()
- 位置: L603-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsView.richListBox.removeAttribute()`, `Services.prefs.getIntPref()`, `setTimeout()`, `this._focusPanel()`, `this._stopWatchingForSpammyDownloadActivation()`
- 条件付き依存: `if (this._delayTimeout)` → `clearTimeout()`
- 参照: `this._delayTimeout`
- XPCOM: `Services.prefs`

## _startWatchingForSpammyDownloadActivation()
- 位置: L618-623
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.addEventListener()`

## _handlePotentiallySpammyDownloadActivation()
- 位置: L626-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.type.startsWith()`
- 条件付き依存: `if (isSpammyKey || isSpammyMouse)` → `Date.now()`
- 条件付き依存: `if (Date.now() - this._lastBeepTime > 1000)` → `Cc["@mozilla.org/sound;1"].getService(Ci.nsISound).beep()`
- 条件付き依存: `if (Date.now() - this._lastBeepTime > 1000)` → `Cc["@mozilla.org/sound;1"].getService()`
- 条件付き依存: `if (Date.now() - this._lastBeepTime > 1000)` → `Date.now()`
- 条件付き依存: `if (isSpammyKey || isSpammyMouse)` → `this._refreshDelayTimer()`
- 参照: `Ci.nsISound`, `aEvent.button`, `aEvent.key`, `this._lastBeepTime`
- XPCOM: `nsISound` / `@mozilla.org/sound;1`

## _stopWatchingForSpammyDownloadActivation()
- 位置: L643-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.removeEventListener()`

## _openPopupIfDataReady()
- 位置: L653-728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsButton.getAnchor()`, `DownloadsCommon.log()`, `DownloadsView._visibleViewItems.values()`, `PanelMultiView.openPopup()`, `PanelMultiView.openPopup( this.panel, anchor, "bottomright topright", 0, 0, false, null ).then()`, `PrivateBrowsingUtils.isContentWindowPrivate()`, `Services.prefs.getBoolPref()`, `anchor.closest()`, `setTimeout()`, `this.panel.classList.toggle()`, `viewItem.download.refresh()`, `viewItem.download.refresh().catch()`
- 条件付き依存: `if (!anchor)` → `DownloadsCommon.error()`
- 条件付き依存: `if (!this._openedManually)` → `this._delayPopupItems()`
- 条件付き依存: `if ( // If private, show message asking whether to delete files at end of session isPrivate && Services.prefs.getBoolPref( "browser.download.enableDeletePrivate"...)` → `PrivateDownloadsSubview.openWhenReady()`
- 参照: `DownloadsView.loading`, `console.error`, `this._openedManually`, `this._waitingDataForOpen`, `this.panel`, `window.STATE_MINIMIZED`, `window.windowState`
- XPCOM: `Services.prefs`

## _itemCountChanged()
- 位置: L776-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`
- 条件付き依存: `if (count > 0)` → `DownloadsCommon.log()`
- 条件付き依存: `if (count > 0)` → `DownloadsPanel.panel.setAttribute()`
- 条件付き依存: `if (!(count > 0))` → `DownloadsCommon.log()`
- 条件付き依存: `if (!(count > 0))` → `DownloadsPanel.panel.removeAttribute()`
- 参照: `DownloadsSummary.active`, `this._downloads.length`, `this.kItemCountLimit`

## richListBox()
- 位置: L804-807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.richListBox`

## downloadsHistory()
- 位置: L812-816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.downloadsHistory`

## onDownloadBatchStarting()
- 位置: L823-826
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`
- 参照: `this.loading`

## onDownloadBatchEnded()
- 位置: L831-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `DownloadsPanel.onViewLoadCompleted()`, `this._itemCountChanged()`
- 参照: `this.loading`

## onDownloadAdded()
- 位置: L852-870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `this._addViewItem()`, `this._downloads.unshift()`
- 条件付き依存: `if (this._downloads.length > this.kItemCountLimit)` → `this._removeViewItem()`
- 条件付き依存: `if (!this.loading)` → `this._itemCountChanged()`
- 参照: `this._downloads`, `this._downloads.length`, `this.kItemCountLimit`, `this.loading`

## onDownloadChanged()
- 位置: L872-877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._visibleViewItems.get()`
- 条件付き依存: `if (viewItem)` → `viewItem.onChanged()`

## onDownloadRemoved()
- 位置: L886-902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `this._downloads.indexOf()`, `this._downloads.splice()`, `this._itemCountChanged()`
- 条件付き依存: `if (itemIndex < this.kItemCountLimit)` → `this._removeViewItem()`
- 条件付き依存: `if (this._downloads.length >= this.kItemCountLimit)` → `this._addViewItem()`
- 参照: `this._downloads`, `this._downloads.length`, `this.kItemCountLimit`

## itemForElement()
- 位置: L910-912
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._itemsForElements.get()`

## _addViewItem()
- 位置: L918-940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `document.createXULElement()`, `element.setAttribute()`, `this._itemsForElements.set()`, `this._visibleViewItems.set()`, `viewItem.ensureActive()`
- 条件付き依存: `if (aNewest)` → `this.richListBox.insertBefore()`
- 条件付き依存: `if (!(aNewest))` → `this.richListBox.appendChild()`
- 参照: `this.richListBox.firstElementChild`

## _removeViewItem()
- 位置: L945-960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.log()`, `this._itemsForElements.delete()`, `this._visibleViewItems.delete()`, `this._visibleViewItems.get()`, `this.richListBox.removeChild()`
- 条件付き依存: `if (previousSelectedIndex != -1)` → `Math.min()`
- 参照: `this._visibleViewItems.get(download).element`, `this.richListBox.itemCount`, `this.richListBox.selectedIndex`

## onDownloadClick()
- 位置: L964-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.closest()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `aEvent.target.closest()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `target.closest("richlistbox").hasAttribute()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `target.closest()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `DownloadsView.itemForElement()`
- 条件付き依存: `if (aEvent.shiftKey || aEvent.ctrlKey || aEvent.metaKey)` → `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (aEvent.shiftKey || aEvent.ctrlKey || aEvent.metaKey)` → `["tab", "window", "tabshifted"].includes()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `command.startsWith()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `DownloadsCommon.log()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `goDoCommand()`
- 参照: `DownloadsView.itemForElement(target).download`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `download._launchedFromPanel`, `download.hasBlockedData`, `download.launchWhenSucceeded`, `download.stopped`, `download.succeeded`

## onDownloadButton()
- 位置: L998-1001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsView.itemForElement()`, `DownloadsView.itemForElement(target).onButton()`, `event.target.closest()`

## onDownloadKeyPress()
- 位置: L1006-1028
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `" ".charCodeAt()`, `aEvent.originalTarget.hasAttribute()`
- 条件付き依存: `if (aEvent.charCode == " ".charCodeAt(0))` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.charCode == " ".charCodeAt(0))` → `goDoCommand()`
- 条件付き依存: `if (readyToDownload)` → `goDoCommand()`
- 参照: `DownloadsView.richListBox.disabled`, `KeyEvent.DOM_VK_RETURN`, `aEvent.charCode`, `aEvent.keyCode`

## contextMenu()
- 位置: L1030-1037
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.contextMenu`

## contextMenuOpen()
- 位置: L1042-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.contextMenu.state`

## canChangeSelectedItem()
- 位置: L1049-1053
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.contextMenuOpen`, `this.subViewOpen`

## _onDownloadMouseOver()
- 位置: L1058-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.classList.contains()`, `aEvent.target.closest()`, `item.classList.toggle()`
- 条件付き依存: `if (aEvent.target.classList.contains("downloadButton"))` → `item.classList.add()`
- 参照: `item.localName`, `this.canChangeSelectedItem`, `this.richListBox.selectedItem`

## _onDownloadMouseOut()
- 位置: L1078-1093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.classList.contains()`, `aEvent.target.closest()`, `item.contains()`
- 条件付き依存: `if (aEvent.target.classList.contains("downloadButton"))` → `item.classList.remove()`
- 参照: `aEvent.relatedTarget`, `item.localName`, `this.canChangeSelectedItem`, `this.richListBox.selectedIndex`

## _onDownloadContextMenu()
- 位置: L1095-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewController.updateCommands()`, `DownloadsViewUI.updateContextMenuForElement()`, `aEvent.originalTarget.closest()`, `element._shell.isCommandEnabled()`, `this.contextMenu.querySelector()`
- 条件付き依存: `if (!element)` → `aEvent.preventDefault()`
- 参照: `this.contextMenu`, `this.contextMenu.querySelector(".downloadCopyLocationMenuItem").hidden`, `this.contextMenu.querySelector(".downloadLinksSeparator").hidden`, `this.contextMenu.querySelector(".downloadOpenReferrerMenuItem").hidden`, `this.richListBox.selectedItem`

## _onDownloadDragStart()
- 位置: L1118-1140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsView.itemForElement()`, `NetUtil.newURI()`, `aEvent.stopPropagation()`, `aEvent.target.closest()`, `dataTransfer.addElement()`, `dataTransfer.mozSetDataAt()`, `dataTransfer.setData()`, `file.exists()`
- 参照: `DownloadsView.itemForElement(element).download.target.path`, `FileUtils.File`, `NetUtil.newURI(file).spec`, `aEvent.dataTransfer`, `dataTransfer.effectAllowed`

## DownloadsViewItem.constructor()
- 位置: L1159-1170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.element.classList.add()`, `this.element.setAttribute()`
- 参照: `this.download`, `this.element`, `this.element._shell`, `this.isPanel`

## DownloadsViewItem.onChanged()
- 位置: L1172-1180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.stateOfDownload()`
- 条件付き依存: `if (this.downloadState !== newState)` → `this._updateState()`
- 条件付き依存: `if (!(this.downloadState !== newState))` → `this._updateStateInner()`
- 参照: `this.download`, `this.downloadState`

## DownloadsViewItem.isCommandEnabled()
- 位置: L1182-1224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.DownloadElementShell.prototype.isCommandEnabled.call()`, `file.exists()`, `partFile.exists()`
- 参照: `FileUtils.File`, `this.download.hasBlockedData`, `this.download.source.isDataURICleared`, `this.download.source?.url`, `this.download.succeeded`, `this.download.target.partFilePath`, `this.download.target.path`

## DownloadsViewItem.doCommand()
- 位置: L1226-1233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isCommandEnabled()`
- 条件付き依存: `if (this.isCommandEnabled(aCommand))` → `aCommand.split()`
- 条件付き依存: `if (this.isCommandEnabled(aCommand))` → `this[command]()`

## DownloadsViewItem.downloadsCmd_unblock()
- 位置: L1237-1240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.confirmUnblock()`

## DownloadsViewItem.downloadsCmd_chooseUnblock()
- 位置: L1242-1245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.confirmUnblock()`

## DownloadsViewItem.downloadsCmd_unblockAndOpen()
- 位置: L1247-1250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.unblockAndOpenDownload()`, `this.unblockAndOpenDownload().catch()`
- 参照: `console.error`

## DownloadsViewItem.downloadsCmd_unblockAndSave()
- 位置: L1251-1254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.unblockAndSave()`

## DownloadsViewItem.downloadsCmd_open()
- 位置: L1256-1265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_open()`

## DownloadsViewItem.downloadsCmd_openInSystemViewer()
- 位置: L1267-1273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_openInSystemViewer()`

## DownloadsViewItem.downloadsCmd_alwaysOpenInSystemViewer()
- 位置: L1275-1281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_alwaysOpenInSystemViewer()`

## DownloadsViewItem.downloadsCmd_alwaysOpenSimilarFiles()
- 位置: L1283-1289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_alwaysOpenSimilarFiles()`

## DownloadsViewItem.downloadsCmd_show()
- 位置: L1291-1301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.showDownloadedFile()`, `DownloadsPanel.hidePanel()`
- 参照: `FileUtils.File`, `this.download.target.path`

## DownloadsViewItem.downloadsCmd_deleteFile()
- 位置: async L1303-1317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsView._visibleViewItems.values()`, `super.downloadsCmd_deleteFile()`, `viewItem.download.refresh()`, `viewItem.download.refresh().catch()`
- 参照: `console.error`

## DownloadsViewItem.downloadsCmd_showBlockedInfo()
- 位置: L1319-1324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsBlockedSubview.toggle()`
- 参照: `this.element`, `this.rawBlockedTitleAndDetails`

## DownloadsViewItem.downloadsCmd_openReferrer()
- 位置: L1326-1328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openURL()`
- 参照: `this.download.source.referrerInfo.originalReferrer`

## DownloadsViewItem.downloadsCmd_copyLocation()
- 位置: L1330-1332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.copyDownloadLink()`
- 参照: `this.download`

## DownloadsViewItem.downloadsCmd_doDefault()
- 位置: L1334-1339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isCommandEnabled()`
- 条件付き依存: `if (defaultCommand && this.isCommandEnabled(defaultCommand))` → `this.doCommand()`
- 参照: `this.currentDefaultCommandName`

## initialize()
- 位置: L1352-1354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.controllers.insertControllerAt()`

## terminate()
- 位置: L1356-1358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.controllers.removeController()`

## supportsCommand()
- 位置: L1362-1399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.isCommandName()`, `aCommand.split()`
- 条件付き依存: `if (DownloadsView.subViewOpen)` → `blockedSubviewCmds.includes()`
- 参照: `DownloadsView.richListBox`, `DownloadsView.subViewOpen`, `DownloadsViewItem.prototype`, `document.commandDispatcher.focusedElement`, `element.parentNode`

## isCommandEnabled()
- 位置: L1401-1419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsView.itemForElement()`, `DownloadsView.itemForElement(element).isCommandEnabled()`
- 参照: `DownloadsCommon.getData(window).canRemoveFinished`, `DownloadsView.richListBox.selectedItem`

## doCommand()
- 位置: L1421-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aCommand in this)` → `this[aCommand]()`
- 条件付き依存: `if (element)` → `DownloadsView.itemForElement(element).doCommand()`
- 条件付き依存: `if (element)` → `DownloadsView.itemForElement()`
- 参照: `DownloadsView.richListBox.selectedItem`

## onEvent()
- 位置: L1436-1436
- 役割: (未記入)
- 触るとき: (未記入)

## updateCommands()
- 位置: L1440-1450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateCommandsForObject()`
- 参照: `DownloadsViewItem.prototype`

## updateCommandsForObject()
- 位置: L1441-1447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewUI.isCommandName()`
- 条件付き依存: `if (DownloadsViewUI.isCommandName(name))` → `goUpdateCommand()`

## downloadsCmd_clearList()
- 位置: L1454-1456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getData(window).removeFinished()`

## downloadsCmd_deletePrivate()
- 位置: L1458-1460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateDownloadsSubview.choose()`

## downloadsCmd_dismissDeletePrivate()
- 位置: L1462-1464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateDownloadsSubview.choose()`

## active()
- 位置: L1487-1501
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aActive)` → `DownloadsCommon.getSummary( window, DownloadsView.kItemCountLimit ).refreshView()`
- 条件付き依存: `if (aActive)` → `DownloadsCommon.getSummary()`
- 参照: `DownloadsFooter.showingSummary`, `DownloadsView.kItemCountLimit`, `this._active`, `this._summaryNode`

## active()
- 位置: L1506-1508
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._active`

## showingProgress()
- 位置: L1518-1526
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aShowingProgress)` → `this._summaryNode.setAttribute()`
- 条件付き依存: `if (!(aShowingProgress))` → `this._summaryNode.removeAttribute()`
- 参照: `DownloadsFooter.showingSummary`

## percentComplete()
- 位置: L1535-1539
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._progressNode)` → `this._progressNode.setAttribute()`
- 参照: `this._progressNode`

## description()
- 位置: L1548-1553
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._descriptionNode)` → `this._descriptionNode.setAttribute()`
- 参照: `this._descriptionNode`

## details()
- 位置: L1563-1568
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._detailsNode)` → `this._detailsNode.setAttribute()`
- 参照: `this._detailsNode`

## focus()
- 位置: L1573-1577
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._summaryNode)` → `this._summaryNode.focus()`
- 参照: `this._summaryNode`

## _onKeyDown()
- 位置: L1585-1592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `" ".charCodeAt()`
- 条件付き依存: `if ( aEvent.charCode == " ".charCodeAt(0) || aEvent.keyCode == KeyEvent.DOM_VK_RETURN )` → `DownloadsPanel.showDownloadsHistory()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.charCode`, `aEvent.keyCode`

## _summaryNode()
- 位置: L1597-1604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._summaryNode`

## _progressNode()
- 位置: L1609-1616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._progressNode`

## _descriptionNode()
- 位置: L1622-1629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._descriptionNode`

## _detailsNode()
- 位置: L1635-1642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._detailsNode`

## focus()
- 位置: L1659-1665
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._showingSummary)` → `DownloadsSummary.focus()`
- 条件付き依存: `if (!(this._showingSummary))` → `DownloadsView.downloadsHistory.focus()`
- 参照: `this._showingSummary`

## showingSummary()
- 位置: L1673-1682
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aValue)` → `this._footerNode.setAttribute()`
- 条件付き依存: `if (!(aValue))` → `this._footerNode.removeAttribute()`
- 参照: `this._footerNode`, `this._showingSummary`

## _footerNode()
- 位置: L1687-1694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._footerNode`

## elements()
- 位置: L1708-1722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `idSuffixes.reduce()`
- 参照: `this.elements`

## toggle()
- 位置: L1740-1791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.panel.addEventListener()`, `DownloadsView.itemForElement()`, `DownloadsViewController.updateCommands()`, `Services.prefs.getBoolPref()`, `document.l10n.setAttributes()`, `element.getAttribute()`, `this.mainView.addEventListener()`, `this.panelMultiView.showSubView()`, `this.subview.setAttribute()`, `window.getComputedStyle()`
- 参照: `DownloadsCommon.strings`, `DownloadsView.subViewOpen`, `details[0].l10n`, `details[0].l10n.args`, `details[0].l10n.id`, `download.error?.becauseBlockedByContentAnalysis`, `download.error?.reputationCheckVerdict`, `download.launchWhenSucceeded`, `e.deleteButton.hidden`, `e.deleteButton.label`, `e.details1`, `e.details1.textContent`, `e.details2.textContent`, `e.title`, `e.title.textContent`, `e.unblockButton.command`, `e.unblockButton.hidden`, `e.unblockButton.label`, `s.unblockButtonConfirmBlock`, `s.unblockButtonOpen`, `s.unblockButtonUnblock`, `this.elements`, `this.mainView.style.minWidth`, `this.subview`, `title.l10n`, `title.l10n.args`, `title.l10n.id`, `window.getComputedStyle(this.subview).width`
- XPCOM: `Services.prefs`

## handleEvent()
- 位置: L1793-1802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.panel.removeEventListener()`, `this.mainView.removeEventListener()`
- 条件付き依存: `if (event.type == "ViewShown")` → `DownloadsPanel.showPanel()`
- 参照: `DownloadsView.subViewOpen`, `event.type`

## confirmBlock()
- 位置: L1807-1810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.hidePanel()`, `goDoCommand()`

## openWhenReady()
- 位置: L1839-1845
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsViewController.updateCommands()`, `this.mainView.addEventListener()`, `this.mainView.toggleAttribute()`
- 参照: `DownloadsView.subViewOpen`

## handleEvent()
- 位置: L1847-1854
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "ViewShown")` → `this.panelMultiView.showSubView()`
- 参照: `event.type`, `this.subview`

## choose()
- 位置: L1863-1871
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.mainView.toggleAttribute()`, `this.panelMultiView.goBack()`
- 条件付き依存: `if (deletePrivate)` → `Services.prefs.setBoolPref()`
- 参照: `DownloadsView.subViewOpen`
- XPCOM: `Services.prefs`
