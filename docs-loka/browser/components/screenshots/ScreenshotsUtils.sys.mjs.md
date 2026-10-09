# browser/components/screenshots/ScreenshotsUtils.sys.mjs

source: browser/components/screenshots/ScreenshotsUtils.sys.mjs
source-hash: 8ce90418e7a3db111011734c5d9e0a426b75d68f
lines: 1652

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`, `ScreenshotsUtils.monitorScreenshotsPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`

## clampDimensionsIfNeeded()
- 位置: L89-106
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (width * height > MAX_CAPTURE_AREA)` → `Math.floor()`

## ScreenshotsComponentParent.receiveMessage()
- 位置: async L109-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ScreenshotsUtils.browserToScreenshotsState.has()`, `ScreenshotsUtils.cancel()`, `ScreenshotsUtils.closePanel()`, `ScreenshotsUtils.copyScreenshotFromRegion()`, `ScreenshotsUtils.downloadScreenshotFromRegion()`, `ScreenshotsUtils.exit()`, `ScreenshotsUtils.focusPanel()`, `ScreenshotsUtils.getUIPhase()`, `ScreenshotsUtils.miniWindowEntryPoint()`, `ScreenshotsUtils.miniWindowFromRegion()`, `ScreenshotsUtils.openPanel()`, `ScreenshotsUtils.setPerBrowserState()`
- 参照: `UIPhases.CLOSED`, `message.data`, `message.data.hasSelection`, `message.data.overlayState`, `message.name`, `message.target.browsingContext.topFrameElement`

## ScreenshotsComponentParent.didDestroy()
- 位置: L179-185
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (browser)` → `ScreenshotsUtils.exit()`
- 参照: `this.browsingContext.topFrameElement`

## ScreenshotsHelperParent.receiveMessage()
- 位置: L189-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ScreenshotsUtils.getUIPhase()`, `bc.currentWindowGlobal .getActor()`, `bc.currentWindowGlobal .getActor("ScreenshotsHelper") .sendQuery()`
- 条件付き依存: `if ( bc.isDiscarded || bc.parentWindowContext !== this.manager || !bc.isActive )` → `console.error()`
- 参照: `UIPhases.INITIAL`, `bc.isActive`, `bc.isDiscarded`, `bc.parentWindowContext`, `message.data`, `message.data.bc`, `message.name`, `this.browsingContext.topFrameElement`, `this.manager`

## getUIPhase()
- 位置: L237-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`, `this.panelForBrowser()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `UIPhases.CLOSED`, `UIPhases.INITIAL`, `UIPhases.OVERLAYSELECTION`, `UIPhases.PREVIEW`, `buttonsPanel.hidden`, `perBrowserState?.hasOverlaySelection`, `perBrowserState?.mode`, `perBrowserState?.overlayShowing`, `perBrowserState?.previewDialog`

## resetMethodsUsed()
- 位置: L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.methodsUsed`

## monitorScreenshotsPref()
- 位置: L266-274
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.SCREENSHOTS_ENABLED)` → `this.initialize()`
- 条件付き依存: `if (!(lazy.SCREENSHOTS_ENABLED))` → `this.uninitialize()`
- 参照: `lazy.SCREENSHOTS_ENABLED`, `this.screenshotsEnabled`

## initialize()
- 位置: L276-289
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized)` → `ScreenshotsCustomizableWidget.init()`
- 条件付き依存: `if (!this.initialized)` → `this.resetMethodsUsed()`
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (Cu.isInAutomation)` → `Services.obs.notifyObservers()`
- 参照: `Cu.isInAutomation`, `lazy.SCREENSHOTS_ENABLED`, `this.initialized`
- XPCOM: `Services.obs`

## uninitialize()
- 位置: L291-308
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.initialized)` → `ScreenshotsCustomizableWidget.uninit()`
- 条件付き依存: `if (this.initialized)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.initialized)` → `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 条件付き依存: `if (this.initialized)` → `this.exit()`
- 条件付き依存: `if (Cu.isInAutomation)` → `Services.obs.notifyObservers()`
- 参照: `Cu.isInAutomation`, `this.browserToScreenshotsState`, `this.initialized`
- XPCOM: `Services.obs`

## handleEvent()
- 位置: L310-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleDocShellSwapEvent()`, `this.handleEndDocShellSwapEvent()`, `this.handleKeyDownEvent()`, `this.handleTabSelect()`
- 参照: `event.type`

## handleKeyDownEvent()
- 位置: L327-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleArrowKeyDown()`, `this.maybeLockFocus()`, `this.panelForBrowser()`
- 条件付き依存: `if (event.target.parentElement === this.panelForBrowser(browser))` → `this.cancel()`
- 参照: `event.key`, `event.target.parentElement`, `event.view.browsingContext.topChromeWindow.gBrowser.selectedBrowser`

## handleDocShellSwapEvent()
- 位置: L362-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.delete()`, `this.browserToScreenshotsState.get()`, `this.getUIPhase()`
- 条件付き依存: `if (currentUIPhase === UIPhases.OVERLAYSELECTION)` → `newBrowser.addEventListener()`
- 条件付き依存: `if (currentUIPhase === UIPhases.OVERLAYSELECTION)` → `oldBrowser.removeEventListener()`
- 条件付き依存: `if (currentUIPhase === UIPhases.OVERLAYSELECTION)` → `this.browserToScreenshotsState.set()`
- 条件付き依存: `if (currentUIPhase === UIPhases.OVERLAYSELECTION)` → `this.getActor(oldBrowser).sendAsyncMessage()`
- 条件付き依存: `if (currentUIPhase === UIPhases.OVERLAYSELECTION)` → `this.getActor()`
- 条件付き依存: `if (!(currentUIPhase === UIPhases.OVERLAYSELECTION))` → `this.cancel()`
- 参照: `UIPhases.OVERLAYSELECTION`, `event.detail`, `event.target`, `previousState.exitOnPreviewClose`, `previousState.hasOverlaySelection`, `previousState.overlayState`

## handleEndDocShellSwapEvent()
- 位置: L406-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.removeEventListener()`, `this.getActor()`, `this.getActor(browser).sendAsyncMessage()`
- 参照: `event.target`

## handleTabSelect()
- 位置: L418-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getUIPhase()`
- 条件付き依存: `if (this.getUIPhase(previousTab.linkedBrowser) === UIPhases.INITIAL)` → `this.cancel()`
- 参照: `UIPhases.INITIAL`, `event.detail.previousTab`, `previousTab.linkedBrowser`

## handleArrowKeyDown()
- 位置: L433-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.clearFocus()`, `Services.focus.setFocus()`, `["crosshairs", "dragging"].includes()`, `this.browserToScreenshotsState.get()`, `this.clearContentFocus()`, `this.moveCursor()`, `win.windowUtils.getLastOverWindowPointerLocationInCSSPixels()`
- 参照: `Services.appinfo.isWayland`, `browser.documentGlobal`, `event.key`, `event.shiftKey`, `win.devicePixelRatio`, `x.value`, `y.value`
- XPCOM: `Services.appinfo` / `Services.focus`

## moveCursor()
- 位置: L491-524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `Math.round()`, `win.windowUtils.sendNativeMouseEvent()`
- 参照: `browser.clientHeight`, `browser.documentGlobal`, `win.devicePixelRatio`, `win.document.documentElement`, `win.innerHeight`, `win.innerWidth`, `win.mozInnerScreenX`, `win.mozInnerScreenY`, `win.windowUtils.NATIVE_MOUSE_MESSAGE_MOVE`

## observe()
- 位置: L526-529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggle()`
- 参照: `gBrowser.selectedBrowser`

## toggle()
- 位置: L541-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`, `this.getUIPhase()`, `this.start()`
- 条件付き依存: `if ( this.getUIPhase(browser) !== UIPhases.CLOSED && this.browserToScreenshotsState.get(browser)?.mode === mode )` → `this.cancel()`
- 参照: `SELECTION_MODES.SCREENSHOTS`, `UIPhases.CLOSED`, `this.browserToScreenshotsState.get(browser)?.mode`

## notify()
- 位置: L561-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `window.event.currentTarget.documentGlobal`
- XPCOM: `Services.obs`

## getActor()
- 位置: L575-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.browsingContext.currentWindowGlobal.getActor()`

## start()
- 位置: L590-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.addEventListener()`, `browser.getTabBrowser()`, `this.browserToScreenshotsState.get()`, `this.captureFocusedElement()`, `this.closeDialogBox()`, `this.getUIPhase()`, `this.setPerBrowserState()`, `this.showPanelAndOverlay()`, `this.tabContainerToScreenshotsCount.get()`, `this.tabContainerToScreenshotsCount.set()`
- 条件付き依存: `if (!count)` → `gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (!count)` → `browser.ownerDocument.addEventListener()`
- 条件付き依存: `if (previousMode && previousMode !== mode)` → `this.switchMode()`
- 参照: `SELECTION_MODES.SCREENSHOTS`, `UIPhases.CLOSED`, `UIPhases.INITIAL`, `UIPhases.OVERLAYSELECTION`, `UIPhases.PREVIEW`, `gBrowser.tabContainer`, `this.browserToScreenshotsState.get(browser)?.mode`

## switchMode()
- 位置: L637-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closePanel()`, `this.setPerBrowserState()`, `this.showPanelAndOverlay()`

## exit()
- 位置: L649-682
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `browser.removeEventListener()`, `this.browserToScreenshotsState.delete()`, `this.browserToScreenshotsState.has()`, `this.captureFocusedElement()`, `this.closeDialogBox()`, `this.closeOverlay()`, `this.closePanel()`, `this.resetMethodsUsed()`, `this.revokeBlobURL()`
- 条件付き依存: `if (gBrowser.selectedBrowser == browser)` → `this.attemptToRestoreFocus()`
- 条件付き依存: `if (this.browserToScreenshotsState.has(browser))` → `this.tabContainerToScreenshotsCount.get()`
- 条件付き依存: `if (count > 0)` → `this.tabContainerToScreenshotsCount.set()`
- 条件付き依存: `if (!count)` → `gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (!count)` → `browser.ownerDocument.removeEventListener()`
- 条件付き依存: `if (Cu.isInAutomation)` → `Services.obs.notifyObservers()`
- 参照: `Cu.isInAutomation`, `gBrowser.selectedBrowser`, `gBrowser.tabContainer`
- XPCOM: `Services.obs`

## cancel()
- 位置: L689-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`, `this.exit()`
- 条件付き依存: `if ( this.browserToScreenshotsState.get(browser)?.mode !== SELECTION_MODES.MINI_WINDOW )` → `this.recordTelemetryEvent()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `this.browserToScreenshotsState.get(browser)?.mode`

## setPerBrowserState()
- 位置: L705-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this.browserToScreenshotsState.get()`, `this.browserToScreenshotsState.has()`
- 条件付き依存: `if (!this.browserToScreenshotsState.has(browser))` → `this.browserToScreenshotsState.set()`

## maybeLockFocus()
- 位置: L713-737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.closest()`
- 条件付き依存: `if (!Services.focus.focusedElement)` → `event.preventDefault()`
- 条件付き依存: `if (!Services.focus.focusedElement)` → `this.focusPanel()`
- 条件付き依存: `if (isElementFirst && event.shiftKey)` → `event.preventDefault()`
- 条件付き依存: `if (isElementFirst && event.shiftKey)` → `this.moveFocusToContent()`
- 条件付き依存: `if (!isElementFirst && !event.shiftKey)` → `event.preventDefault()`
- 条件付き依存: `if (!isElementFirst && !event.shiftKey)` → `this.moveFocusToContent()`
- 参照: `Services.focus.focusedElement`, `event.explicitOriginalTarget`, `event.shiftKey`, `event.view.gBrowser.selectedBrowser`, `target.nextElementSibling`
- XPCOM: `Services.focus`

## focusPanel()
- 位置: L739-750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelForBrowser()`
- 条件付き依存: `if (direction)` → `buttonsPanel .querySelector("screenshots-buttons") .focusButton()`
- 条件付き依存: `if (direction)` → `buttonsPanel .querySelector()`
- 条件付き依存: `if (!(direction))` → `buttonsPanel .querySelector("screenshots-buttons") .focusButton()`
- 条件付き依存: `if (!(direction))` → `buttonsPanel .querySelector()`
- 参照: `lazy.SCREENSHOTS_LAST_SCREENSHOT_METHOD`

## moveFocusToContent()
- 位置: L752-757
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getActor()`, `this.getActor(browser).sendAsyncMessage()`

## clearContentFocus()
- 位置: L759-761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getActor()`, `this.getActor(browser).sendAsyncMessage()`

## attemptToRestoreFocus()
- 位置: L768-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `perBrowserState.currentFocusRef?.get()`, `perBrowserState.previousFocusRef?.get()`, `this.browserToScreenshotsState.get()`, `this.getDialog()`, `this.panelForBrowser()`
- 条件付き依存: `if (!currentFocus)` → `doFocus()`
- 条件付き依存: `if ( (dialog && currentFocus == dialog) || (panel && currentFocus == panel) || currentFocus == browser )` → `doFocus()`
- 条件付き依存: `if (prevFocus)` → `doFocus()`
- 参照: `browser.documentGlobal`, `browser.ownerDocument`, `currentFocus.DOCUMENT_FRAGMENT_NODE`, `currentFocus.host`, `currentFocus.nodeType`, `currentFocus.parentNode`, `document.activeElement`, `document.commandDispatcher.focusedElement`, `document.commandDispatcher.focusedWindow`, `perBrowserState.currentFocusRef`

## doFocus()
- 位置: L772-791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fm.setFocus()`, `prevFocus.focus()`, `prevFocus.removeAttribute()`, `prevFocus.setAttribute()`
- 参照: `Services.focus`, `document.activeElement`, `document.commandDispatcher.focusedElement`, `fm.FLAG_NOSCROLL`
- XPCOM: `Services.focus`

## scheduleRetry()
- 位置: L855-867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `perBrowserState?.closedPromise.then()`, `this.browserToScreenshotsState.get()`, `this.setPerBrowserState()`, `this.start()`
- 条件付き依存: `if (!perBrowserState?.closedPromise)` → `console.warn()`
- 参照: `perBrowserState?.closedPromise`

## openPreviewDialog()
- 位置: async L874-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.documentGlobal.gBrowser.getTabDialogBox()`, `closedPromise.finally()`, `dialogBox.open()`, `this.onDialogClose()`, `this.setPerBrowserState()`
- 参照: `browser.browsingContext.id`

## captureFocusedElement()
- 位置: L903-917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `this.setPerBrowserState()`
- 参照: `browser.ownerDocument`, `document.activeElement`, `document.commandDispatcher.focusedElement`

## panelForBrowser()
- 位置: L926-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `perBrowserState.buttonsPanel.get()`, `this.browserToScreenshotsState.get()`
- 参照: `perBrowserState?.buttonsPanel`

## createPanel()
- 位置: L935-941
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `containerElem.appendChild()`, `doc.getElementById()`, `doc.importNode()`
- 参照: `browser.ownerDocument`, `fragmentClone.firstElementChild`, `template.content`

## openPanel()
- 位置: L948-1002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `browser.documentGlobal.requestAnimationFrame()`, `buttonsPanel .querySelector()`, `buttonsPanel .querySelector("screenshots-buttons") .focusButton()`, `buttonsPanel .querySelector("screenshots-buttons") ?.setAttribute()`, `gBrowser.getPanel()`, `gBrowser.getTabForBrowser()`, `resolve()`, `this.browserToScreenshotsState.get()`, `this.panelForBrowser()`, `this.setPerBrowserState()`
- 条件付き依存: `if (!buttonsPanel)` → `gBrowser.tabpanels.querySelector()`
- 条件付き依存: `if (!buttonsPanel)` → `this.createPanel()`
- 条件付き依存: `if (buttonsPanel.parentElement !== browserWrapper)` → `browserWrapper.appendChild()`
- 条件付き依存: `if (tab?.splitview)` → `this.getUIPhase()`
- 条件付き依存: `if ( siblingTab !== tab && this.getUIPhase(siblingTab.linkedBrowser) === UIPhases.INITIAL )` → `this.cancel()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `SELECTION_MODES.SCREENSHOTS`, `UIPhases.INITIAL`, `browser.documentGlobal`, `buttonsPanel.hidden`, `buttonsPanel.parentElement`, `lazy.SCREENSHOTS_LAST_SCREENSHOT_METHOD`, `siblingTab.linkedBrowser`, `tab.splitview.tabs`, `tab?.splitview`, `this.browserToScreenshotsState.get(browser)?.mode`

## closePanel()
- 位置: L1009-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelForBrowser()`
- 参照: `buttonsPanel.hidden`

## showPanelAndOverlay()
- 位置: L1024-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `this.browserToScreenshotsState.get()`, `this.getActor()`, `this.openPanel()`, `this.setPerBrowserState()`
- 条件付き依存: `if (mode !== SELECTION_MODES.MINI_WINDOW)` → `this.recordTelemetryEvent()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `SELECTION_MODES.SCREENSHOTS`, `this.browserToScreenshotsState.get(browser)?.mode`

## closeOverlay()
- 位置: L1043-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor?.sendAsyncMessage()`, `this.browserToScreenshotsState.has()`, `this.getActor()`
- 条件付き依存: `if (this.browserToScreenshotsState.has(browser))` → `this.setPerBrowserState()`

## getDialog()
- 位置: L1066-1086
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currTabDialogBox)` → `currTabDialogBox.getTabDialogManager()`
- 条件付き依存: `if (dialogs.length)` → `dialog._openedURL.endsWith()`
- 条件付き依存: `if (dialogs.length)` → `dialog._openedURL.includes()`
- 参照: `browser.browsingContext.id`, `browser.tabDialogBox`, `dialogs.length`, `manager.dialogs`, `manager.hasDialogs`

## closeDialogBox()
- 位置: L1093-1100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`
- 条件付き依存: `if (perBrowserState?.previewDialog)` → `perBrowserState.previewDialog.close()`
- 参照: `perBrowserState?.previewDialog`

## onDialogClose()
- 位置: L1108-1117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`
- 条件付き依存: `if (perBrowserState?.exitOnPreviewClose)` → `this.exit()`
- 参照: `perBrowserState.previewDialog`, `perBrowserState?.exitOnPreviewClose`

## getWidgetAnchor()
- 位置: L1127-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `widgetGroup?.forWindow()`, `window.CustomizableUI.getWidget()`, `window.isElementVisible()`
- 条件付き依存: `if ( !anchor || !anchor.isConnected || !window.isElementVisible(anchor.parentNode) )` → `browser.ownerDocument.getElementById()`
- 参照: `anchor.isConnected`, `anchor.parentNode`, `browser.documentGlobal`, `widget?.anchor`

## showCopiedConfirmationHint()
- 位置: L1150-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.documentGlobal.ConfirmationHint.show()`, `this.getWidgetAnchor()`

## fetchFullPageBounds()
- 位置: L1166-1169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendQuery()`, `this.getActor()`

## fetchVisibleBounds()
- 位置: L1178-1181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendQuery()`, `this.getActor()`

## showAlertMessage()
- 位置: L1183-1187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AlertsService.showAlert()`

## revokeBlobURL()
- 位置: L1194-1199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`
- 条件付き依存: `if (browserState?.blobURL)` → `URL.revokeObjectURL()`
- 参照: `browserState.blobURL`, `browserState?.blobURL`

## setBlobURL()
- 位置: L1207-1213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.revokeBlobURL()`, `this.setPerBrowserState()`

## cropScreenshotRectIfNeeded()
- 位置: L1224-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `clampDimensionsIfNeeded()`
- 条件付き依存: `if (result.cropped)` → `lazy.screenshotsLocalization.formatMessagesSync()`
- 条件付き依存: `if (result.cropped)` → `this.showAlertMessage()`
- 条件付き依存: `if (result.cropped)` → `this.recordTelemetryEvent()`
- 参照: `errorMessage.value`, `errorTitle.value`, `rect.bottom`, `rect.devicePixelRatio`, `rect.height`, `rect.left`, `rect.right`, `rect.top`, `rect.width`, `result.cropped`, `result.height`, `result.width`

## takeScreenshot()
- 位置: async L1253-1297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.setFocus()`, `Services.prefs.setStringPref()`, `URL.createObjectURL()`, `canvas.convertToBlob()`, `dialog._frame.contentDocument.querySelector()`, `screenshotsPreviewEl.focusButton()`, `this.closeOverlay()`, `this.closePanel()`, `this.createCanvas()`, `this.openPreviewDialog()`, `this.recordTelemetryEvent()`, `this.setBlobURL()`
- 条件付き依存: `if (type === "FullPage")` → `this.fetchFullPageBounds()`
- 条件付き依存: `if (!(type === "FullPage"))` → `this.fetchVisibleBounds()`
- 条件付き依存: `if (Cu.isInAutomation)` → `Services.obs.notifyObservers()`
- 参照: `Cu.isInAutomation`, `dialog._dialogReady`, `lazy.SCREENSHOTS_LAST_SAVED_METHOD`, `screenshotsPreviewEl.previewImg.src`, `this.methodsUsed`
- XPCOM: `Services.focus` / `Services.obs` / `Services.prefs`

## createCanvas()
- 位置: async L1306-1381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowsingContext.get()`, `Math.floor()`, `Math.round()`, `browsingContext.currentWindowGlobal.drawSnapshot()`, `canvas.getContext()`, `context.drawImage()`, `context.fillRect()`, `snapshot.close()`, `this.cropScreenshotRectIfNeeded()`
- 参照: `browser.browsingContext.id`, `canvas.height`, `canvas.width`, `context.fillStyle`, `region.bottom`, `region.height`, `region.left`, `region.right`, `region.top`, `region.width`

## copyScreenshotFromRegion()
- 位置: async L1389-1394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `canvas.convertToBlob()`, `this.copyScreenshot()`, `this.createCanvas()`

## copyScreenshotFromBlobURL()
- 位置: async L1396-1399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`, `fetch(blobURL).then()`, `r.blob()`, `this.copyScreenshot()`

## copyScreenshot()
- 位置: async L1409-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `blob.arrayBuffer()`, `lazy.BrowserUtils.copyImageToClipboard()`, `this.getActor()`, `this.getActor(browser).sendQuery()`, `this.recordTelemetryEvent()`, `this.resetMethodsUsed()`, `this.showCopiedConfirmationHint()`
- 参照: `this.methodsUsed`
- XPCOM: `Services.prefs`

## downloadScreenshotFromRegion()
- 位置: async L1439-1446
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.createObjectURL()`, `canvas.convertToBlob()`, `this.createCanvas()`, `this.downloadScreenshot()`, `this.setBlobURL()`

## miniWindowEntryPoint()
- 位置: L1455-1458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserToScreenshotsState.get()`

## miniWindowFullTab()
- 位置: async L1465-1472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getTabBrowser()`, `browser.getTabBrowser()?.getTabForBrowser()`, `this.exit()`, `this.miniWindowEntryPoint()`
- 条件付き依存: `if (tab)` → `lazy.MiniWindowManager.popTab()`

## miniWindowFromRegion()
- 位置: async L1486-1511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `browser.getTabBrowser()`, `browser.getTabBrowser()?.getTabForBrowser()`, `lazy.MiniWindowManager.popRegion()`
- 参照: `browser.clientHeight`, `browser.clientWidth`, `browser.fullZoom`, `region.bottom`, `region.height`, `region.left`, `region.right`, `region.top`, `region.width`
- XPCOM: `Services.prefs`

## downloadScreenshot()
- 位置: async L1523-1576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `console.error()`, `download.start()`, `getFilename()`, `lazy.Downloads.createDownload()`, `lazy.Downloads.getList()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `list.add()`, `this.getActor()`, `this.getActor(browser).sendQuery()`, `this.recordTelemetryEvent()`, `this.resetMethodsUsed()`
- 参照: `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`, `lazy.FileUtils.File`, `new Blob([filename]).size`, `this.methodsUsed`
- XPCOM: `Services.prefs`

## recordTelemetryEvent()
- 位置: L1578-1580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.screenshots[name].record()`
- 参照: `Glean.screenshots`

## init()
- 位置: L1584-1646
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.createWidget()`, `lazy.NimbusFeatures.screenshots.getEnrollmentMetadata()`, `lazy.NimbusFeatures.screenshots.onUpdate()`, `maybePlaceToolbarButton()`

## onCommand()
- 位置: L1591-1597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `aEvent.currentTarget.documentGlobal`
- XPCOM: `Services.obs`

## maybePlaceToolbarButton()
- 位置: L1599-1634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.CustomizableUI.getPlacementOfWidget()`, `lazy.NimbusFeatures.screenshots.getVariable()`
- 条件付き依存: `if ( !buttonPlacedByNimbus && !lazy.CustomizableUI.getPlacementOfWidget(widgetId)?.area && lazy.NimbusFeatures.screenshots.getVariable("buttonOnToolbarByDefault") )` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (urlbarPlacement?.area == AREA_NAVBAR)` → `lazy.CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (urlbarPlacement?.area == AREA_NAVBAR)` → `widgetIds[buttonPosition].includes()`
- 条件付き依存: `if ( !buttonPlacedByNimbus && !lazy.CustomizableUI.getPlacementOfWidget(widgetId)?.area && lazy.NimbusFeatures.screenshots.getVariable("buttonOnToolbarByDefault") )` → `lazy.CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if ( !buttonPlacedByNimbus && !lazy.CustomizableUI.getPlacementOfWidget(widgetId)?.area && lazy.NimbusFeatures.screenshots.getVariable("buttonOnToolbarByDefault") )` → `Services.prefs.setBoolPref()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.CustomizableUI.getPlacementOfWidget(widgetId)?.area`, `urlbarPlacement.position`, `urlbarPlacement?.area`
- XPCOM: `Services.prefs`

## uninit()
- 位置: L1648-1650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`
