# browser/components/tabbrowser/content/browser-ctrlTab.js

source: browser/components/tabbrowser/content/browser-ctrlTab.js
source-hash: 3878a29a91aef0911f0260082847ed416ddf16d4
lines: 859

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Math.max()`, `Math.min()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## aspectRatio()
- 位置: L9-16
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `PageThumbUtils.getThumbnailSize()`

## tabPreviews_loadImage()
- 位置: async L27-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PageThumbs.getThumbnailURL()`, `finish()`, `img.addEventListener()`, `setTimeout()`

## finish()
- 位置: L36-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `controller.abort()`, `resolve()`

## tabPreviews_get()
- 位置: async L70-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.hasAttribute()`, `this.capture()`
- 条件付き依存: `if (!browser.browsingContext)` → `this.loadImage()`

## tabPreviews_capture()
- 位置: async L110-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PageThumbs.captureToCanvas()`, `PageThumbs.createCanvas()`, `PageThumbs.shouldStoreThumbnail()`, `console.error()`
- 条件付き依存: `if (doStore && aShouldCache)` → `PageThumbs.captureAndStore()`
- 条件付き依存: `if (doStore && aShouldCache)` → `this.loadImage()`
- 条件付き依存: `if (img)` → `canvas.getContext("2d").drawImage()`
- 条件付き依存: `if (img)` → `canvas.getContext()`

## opening()
- 位置: L148-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `host.panel.addEventListener()`, `this._generateHandler()`

## _generateHandler()
- 位置: L157-165
- 役割: (未記入)
- 触るとき: (未記入)

## listener()
- 位置: L159-164
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == host.panel)` → `host.panel.removeEventListener()`
- 条件付き依存: `if (event.target == host.panel)` → `self["_" + event.type]()`

## _popupshown()
- 位置: L166-170
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("setupGUI" in host)` → `host.setupGUI()`

## _popuphiding()
- 位置: L171-195
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("suspendGUI" in host)` → `host.suspendGUI()`
- 条件付き依存: `if (host._prevFocus)` → `Services.focus.setFocus()`
- 条件付き依存: `if (!(host._prevFocus))` → `gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (host.tabToSelect)` → `gBrowser.setSelectedTab()`
- 条件付き依存: `if (host.tabToSelect)` → `gBrowser.TabMetrics.userTriggeredContext()`
- XPCOM: [`nsIFocusManager`](../../../../dom/interfaces/base/nsIFocusManager.idl.md) / `Services.focus`

## panel()
- 位置: L203-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## previewsContainer()
- 位置: L207-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## showAllButton()
- 位置: L212-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("ctrlTab-showAll-container") .appendChild()`, `document.createXULElement()`, `this.showAllButton.addEventListener()`

## previews()
- 位置: L224-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._buildPreviews()`

## keys()
- 位置: L229-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["close", "find", "selectAll"].forEach()`, `document .getElementById()`, `document .getElementById("key_" + key) .getAttribute()`, `document .getElementById("key_" + key) .getAttribute("key") .toLocaleLowerCase()`, `document .getElementById("key_" + key) .getAttribute("key") .toLocaleLowerCase() .charCodeAt()`

## selected()
- 位置: L242-246
- 役割: (未記入)
- 触るとき: (未記入)

## isOpen()
- 位置: L247-251
- 役割: (未記入)
- 触るとき: (未記入)

## tabCount()
- 位置: L252-254
- 役割: (未記入)
- 触るとき: (未記入)

## tabPreviewCount()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`

## previewColumnCount()
- 位置: L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`

## tabList()
- 位置: L266-268
- 役割: (未記入)
- 触るとき: (未記入)

## ctrlTab_init()
- 位置: L270-275
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._recentlyUsedTabs)` → `this._initRecentlyUsedTabs()`
- 条件付き依存: `if (!this._recentlyUsedTabs)` → `this._init()`

## ctrlTab_uninit()
- 位置: L277-282
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._recentlyUsedTabs)` → `this._init()`

## ctrlTab_observePref()
- 位置: L286-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `this.readPref()`
- XPCOM: `Services.prefs`

## ctrlTab_stopObservingPref()
- 位置: L291-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`, `this.uninit()`
- XPCOM: `Services.prefs`

## ctrlTab_readPref()
- 位置: L296-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enable)` → `this.init()`
- 条件付き依存: `if (!(enable))` → `this.uninit()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L310-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.readPref()`

## _buildPreviews()
- 位置: L314-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._makePreview()`, `this.previews.push()`, `this.previewsContainer.appendChild()`, `this.previewsContainer.replaceChildren()`

## _makePreview()
- 位置: L325-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `faviconContainer.appendChild()`, `label.setAttribute()`, `preview.addEventListener()`, `preview.appendChild()`, `preview.setAttribute()`, `previewInner.appendChild()`

## ctrlTab_updatePreviews()
- 位置: L357-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `this.previewsContainer.style.setProperty()`, `this.updatePreview()`

## ctrlTab_updatePreview()
- 位置: L375-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPreview._canvas.replaceChildren()`, `aPreview._label.setAttribute()`, `aPreview.setAttribute()`, `console.error()`, `tabPreviews .get()`, `tabPreviews .get(aTab) .then()`
- 条件付き依存: `if (!aTab)` → `aPreview._canvas.replaceChildren()`
- 条件付き依存: `if (!aTab)` → `aPreview._label.removeAttribute()`
- 条件付き依存: `if (!aTab)` → `aPreview.removeAttribute()`
- 条件付き依存: `if (!aTab)` → `aPreview._favicon.removeAttribute()`
- 条件付き依存: `if (tabChanged)` → `aPreview._canvas.replaceChildren()`
- 条件付き依存: `if (tabChanged)` → `this._makePlaceholder()`
- 条件付き依存: `if (aTab.image)` → `aPreview._favicon.setAttribute()`
- 条件付き依存: `if (!(aTab.image))` → `aPreview._favicon.removeAttribute()`

## _makePlaceholder()
- 位置: L421-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `placeholder.setAttribute()`

## ctrlTab_advanceFocus()
- 位置: L430-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.previews.indexOf()`
- 条件付き依存: `if (this._selectedIndex == -1)` → `this.previews[selectedIndex].focus()`
- 条件付き依存: `if (this.previews[selectedIndex]._tab)` → `gBrowser.warmupTab()`
- 条件付き依存: `if (this._timer)` → `clearTimeout()`
- 条件付き依存: `if (this._timer)` → `this._openPanel()`

## ctrlTab_pick()
- 位置: L459-471
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (select == this.showAllButton)` → `this.showAllTabs()`
- 条件付き依存: `if (!(select == this.showAllButton))` → `this.close()`

## ctrlTab_showAllTabs()
- 位置: L473-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gTabsPanel.showAllTabsPanel()`, `this.close()`

## ctrlTab_remove()
- 位置: L478-482
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aPreview._tab)` → `gBrowser.removeTab()`

## ctrlTab_attachTab()
- 位置: L484-502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.detachTab()`
- 条件付き依存: `if (aPos == 0)` → `this._recentlyUsedTabs.unshift()`
- 条件付き依存: `if (aPos)` → `this._recentlyUsedTabs.splice()`
- 条件付き依存: `if (!(aPos))` → `this._recentlyUsedTabs.push()`

## ctrlTab_detachTab()
- 位置: L504-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recentlyUsedTabs.indexOf()`
- 条件付き依存: `if (i >= 0)` → `this._recentlyUsedTabs.splice()`

## ctrlTab_open()
- 位置: L511-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.round()`, `gBrowser.warmupTab()`, `setTimeout()`, `this._openPanel()`, `this.updatePreviews()`
- 条件付き依存: `if (this.previews.length != this.maxTabPreviews + 1)` → `this._buildPreviews()`

## ctrlTab_openPanel()
- 位置: L535-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Math.min()`, `tabPreviewPanelHelper.opening()`, `this.panel.openPopupAtScreen()`

## ctrlTab_close()
- 位置: L552-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panel.hidePopup()`
- 条件付き依存: `if (this._timer)` → `clearTimeout()`
- 条件付き依存: `if (this._timer)` → `this.suspendGUI()`
- 条件付き依存: `if (aTabToSelect)` → `gBrowser.setSelectedTab()`
- 条件付き依存: `if (aTabToSelect)` → `gBrowser.TabMetrics.userTriggeredContext()`

## ctrlTab_setupGUI()
- 位置: L576-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.selected.focus()`

## ctrlTab_suspendGUI()
- 位置: L581-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePreview()`

## onKeyDown()
- 位置: L587-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShortcutUtils.getSystemActionForEvent()`, `document.addEventListener()`, `event.preventDefault()`, `event.stopPropagation()`, `this.KeyboardLockUtils.mustWaitForKeyboardLockRequestedReply()`
- 条件付き依存: `if (this.isOpen)` → `this.advanceFocus()`
- 条件付き依存: `if (event.shiftKey)` → `this.showAllTabs()`
- 条件付き依存: `if (tabs.length > 2)` → `this.open()`
- 条件付き依存: `if (tabs.length == 2)` → `gBrowser.setSelectedTab()`
- 条件付き依存: `if (tabs.length == 2)` → `gBrowser.TabMetrics.userTriggeredContext()`

## onKeyPress()
- 位置: L630-654
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`, `this.remove()`, `this.showAllTabs()`
- 条件付き依存: `if (event.keyCode == event.DOM_VK_DELETE)` → `this.remove()`

## ctrlTab_removeClosingTabFromUI()
- 位置: L656-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updatePreviews()`
- 条件付き依存: `if (this.tabCount == 2)` → `this.close()`
- 条件付き依存: `if (this.selected.hidden)` → `this.advanceFocus()`
- 条件付き依存: `if (this.selected == this.showAllButton)` → `this.advanceFocus()`
- 条件付き依存: `if (aTab.selected && this.panel.state == "open")` → `setTimeout()`
- 条件付き依存: `if (aTab.selected && this.panel.state == "open")` → `selected.focus()`

## ctrlTab_handleEvent()
- 位置: L683-778
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["label", "busy", "image"].includes()`, `event.detail.changed.some()`, `event.preventDefault()`, `event.stopPropagation()`, `this._initRecentlyUsedTabs()`, `this._sortRecentlyUsedTabs()`, `this.attachTab()`, `this.detachTab()`, `this.onKeyDown()`, `this.onKeyPress()`, `this.pick()`
- 条件付き依存: `if ( this.previews[i]._tab && this.previews[i]._tab == event.target )` → `this.updatePreview()`
- 条件付き依存: `if (previousTab.hidden)` → `this.detachTab()`
- 条件付き依存: `if (this.isOpen)` → `this.removeClosingTabFromUI()`
- 条件付き依存: `if (event.keyCode === event.DOM_VK_CONTROL)` → `document.removeEventListener()`
- 条件付き依存: `if (this.isOpen)` → `this.pick()`
- 条件付き依存: `if (event.target.id == "menu_viewPopup")` → `document.getElementById()`
- 条件付き依存: `if (event.relatedTarget)` → `event.currentTarget.focus()`
- 条件付き依存: `if (event.button == 1)` → `this.remove()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && event.button == 2)` → `this.pick()`

## filterForThumbnailExpiration()
- 位置: L780-795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `aCallback()`, `urls.push()`

## _sortRecentlyUsedTabs()
- 位置: L796-800
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recentlyUsedTabs.sort()`

## _initRecentlyUsedTabs()
- 位置: L801-807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.prototype.filter.call()`, `this._sortRecentlyUsedTabs()`

## ctrlTab__init()
- 位置: L809-844
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("menu_viewPopup") [toggleEventListener]()`, `document.getElementById()`, `document[toggleEventListener]()`, `tabContainer[toggleEventListener]()`, `window[toggleEventListener]()`
- 条件付き依存: `if (enable)` → `document.addEventListener()`
- 条件付き依存: `if (!(enable))` → `document.removeEventListener()`
- 条件付き依存: `if (enable)` → `PageThumbs.addExpirationFilter()`
- 条件付き依存: `if (!(enable))` → `PageThumbs.removeExpirationFilter()`
