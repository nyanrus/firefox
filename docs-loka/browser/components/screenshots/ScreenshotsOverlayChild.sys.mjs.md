# browser/components/screenshots/ScreenshotsOverlayChild.sys.mjs

source: browser/components/screenshots/ScreenshotsOverlayChild.sys.mjs
source-hash: 203f1b831fc2dcb2ae6e5bfd39c08c90e73baf49
lines: 2177

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## ScreenshotsOverlay.mode()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#mode`

## ScreenshotsOverlay.mode()
- 位置: L91-101
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SELECTION_MODES.MINI_WINDOW`, `this.#mode`, `this.overlayTemplate`, `this.selectionRegion`, `this.selectionRegion.confineToViewport`

## ScreenshotsOverlay.markup()
- 位置: L111-233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ShortcutUtils.getModifierString()`, `lazy.overlayLocalization.formatMessagesSync()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `cancelAttributes.attributes`, `cancelAttributes.attributes[0].value`, `cancelAttributes.attributes[1].value`, `cancelLabel.value`, `copyAttributes.attributes`, `copyAttributes.attributes[0].value`, `copyAttributes.attributes[1].value`, `copyAttributes.value`, `downloadAttributes.attributes`, `downloadAttributes.attributes[0].value`, `downloadAttributes.attributes[1].value`, `downloadAttributes.value`, `instructions.value`, `miniWindowCancelAttributes.attributes`, `miniWindowCancelAttributes.attributes[0].value`, `miniWindowCancelAttributes.attributes[1].value`, `miniWindowCancelAttributes.value`, `miniWindowOverlayHeader.value`, `miniWindowOverlayInstructions.value`, `popAttributes.attributes`, `popAttributes.attributes[0].value`, `popAttributes.attributes[1].value`, `popAttributes.value`, `previewFaceAriaLabel.attributes`, `previewFaceAriaLabel.attributes[0].value`, `reselectAttributes.attributes`, `reselectAttributes.attributes[0].value`, `reselectAttributes.attributes[1].value`, `reselectAttributes.value`, `this.copyKey`, `this.downloadKey`, `this.mode`

## ScreenshotsOverlay.fragment()
- 位置: L235-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.overlayTemplate.content.cloneNode()`
- 条件付き依存: `if (!this.overlayTemplate)` → `parser.parseFromString()`
- 条件付き依存: `if (!this.overlayTemplate)` → `this.document.importNode()`
- 条件付き依存: `if (!this.overlayTemplate)` → `doc.querySelector()`
- 参照: `this.markup`, `this.overlayTemplate`

## ScreenshotsOverlay.initialized()
- 位置: L248-250
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#initialized`

## ScreenshotsOverlay.state()
- 位置: L252-254
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#state`

## ScreenshotsOverlay.methodsUsed()
- 位置: L256-258
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#methodsUsed`

## ScreenshotsOverlay.constructor()
- 位置: L260-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.overlayLocalization.formatMessagesSync()`, `this.resetMethodsUsed()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `SELECTION_MODES.SCREENSHOTS`, `contentDocument.documentGlobal`, `copyKey.value`, `downloadKey.value`, `this.copyKey`, `this.document`, `this.downloadKey`, `this.hoverElementRegion`, `this.mode`, `this.selectionRegion`, `this.selectionRegion.confineToViewport`, `this.window`, `this.windowDimensions`

## ScreenshotsOverlay.content()
- 位置: L281-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.isDeadWrapper()`
- 参照: `this.#content`

## ScreenshotsOverlay.getElementById()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.content.root.getElementById()`

## ScreenshotsOverlay.initialize()
- 位置: async L292-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#content.root.appendChild()`, `this.#setState()`, `this.document.insertAnonymousContent()`, `this.initializeElements()`, `this.ranges.push()`, `this.selection.getRangeAt()`, `this.updateWindowDimensions()`, `this.window.getSelection()`, `this.windowDimensions.reset()`
- 条件付き依存: `if (this.initialized && this.mode !== mode)` → `this.tearDown()`
- 参照: `SELECTION_MODES.SCREENSHOTS`, `STATES.CROSSHAIRS`, `Services.locale.isAppLocaleRTL`, `this.#content`, `this.#initialized`, `this.fragment`, `this.initialized`, `this.mode`, `this.ranges`, `this.screenshotsContainer.dir`, `this.selection`, `this.selection.rangeCount`
- XPCOM: `Services.locale`

## ScreenshotsOverlay.initializeElements()
- 位置: L328-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getElementById()`
- 参照: `this.bottomBackgroundEl`, `this.bottomLeftMover`, `this.bottomRightMover`, `this.buttonsContainer`, `this.cancelButton`, `this.copyButton`, `this.downloadButton`, `this.highlightEl`, `this.hoverElementContainer`, `this.leftBackgroundEl`, `this.leftEye`, `this.miniWindowCancelButton`, `this.popButton`, `this.previewCancelButton`, `this.previewContainer`, `this.previewFace`, `this.reselectButton`, `this.rightBackgroundEl`, `this.rightEye`, `this.screenshotsContainer`, `this.selectionContainer`, `this.selectionSize`, `this.topBackgroundEl`, `this.topLeftMover`, `this.topRightMover`

## ScreenshotsOverlay.tearDown()
- 位置: L366-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`
- 条件付き依存: `if (!(options.doNotResetMethods === true))` → `this.resetMethodsUsed()`
- 条件付き依存: `if (this.#content)` → `this.document.removeAnonymousContent()`
- 参照: `options.doNotResetMethods`, `this.#content`, `this.#initialized`

## ScreenshotsOverlay.resetMethodsUsed()
- 位置: L382-389
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#methodsUsed`

## ScreenshotsOverlay.focus()
- 位置: L391-397
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (direction === "backward")` → `this.previewCancelButton.focus()`
- 条件付き依存: `if (!(direction === "backward"))` → `this.previewFace.focus()`

## ScreenshotsOverlay.getCoordinatesFromEvent()
- 位置: L412-418
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.windowDimensions.scrollMinX`, `this.windowDimensions.scrollMinY`

## ScreenshotsOverlay.handleEvent()
- 位置: L420-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleClick()`, `this.handleKeyDown()`, `this.handleKeyUp()`, `this.handlePointerDown()`, `this.handlePointerMove()`, `this.handlePointerUp()`, `this.handleSelectionChange()`
- 参照: `event.type`

## ScreenshotsOverlay.preEventHandler()
- 位置: L456-470
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.button > 0 || event.buttons > 1)` → `this.#setState()`
- 参照: `STATES.CROSSHAIRS`, `STATES.DRAGGING`, `STATES.DRAGGING_READY`, `STATES.RESIZING`, `STATES.SELECTED`, `event.button`, `event.buttons`, `this.#state`

## ScreenshotsOverlay.handleClick()
- 位置: L472-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancelOverlay()`, `this.copySelectedRegion()`, `this.downloadSelectedRegion()`, `this.maybeCancelScreenshots()`, `this.popSelectedRegion()`, `this.preEventHandler()`, `this.reselectRegion()`
- 参照: `event.originalTarget.id`

## ScreenshotsOverlay.cancelOverlay()
- 位置: L501-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchEvent()`

## ScreenshotsOverlay.reselectRegion()
- 位置: L508-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`
- 参照: `STATES.CROSSHAIRS`

## ScreenshotsOverlay.maybeCancelScreenshots()
- 位置: L512-520
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#state === STATES.CROSSHAIRS)` → `this.#dispatchEvent()`
- 条件付き依存: `if (!(this.#state === STATES.CROSSHAIRS))` → `this.#setState()`
- 参照: `STATES.CROSSHAIRS`, `this.#state`

## ScreenshotsOverlay.handlePointerDown()
- 位置: L528-560
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.originalTarget.closest()`, `this.crosshairsDragStart()`, `this.getCoordinatesFromEvent()`, `this.preEventHandler()`, `this.selectedDragStart()`
- 条件付き依存: `if ( event.originalTarget.id === "screenshots-cancel-button" || event.originalTarget.closest("#buttons-container") === this.buttonsContainer )` → `event.stopPropagation()`
- 参照: `STATES.CROSSHAIRS`, `STATES.SELECTED`, `event.originalTarget.id`, `this.#state`, `this.buttonsContainer`

## ScreenshotsOverlay.handlePointerMove()
- 位置: L567-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.crosshairsMove()`, `this.draggingDrag()`, `this.draggingReadyDrag()`, `this.getCoordinatesFromEvent()`, `this.preEventHandler()`, `this.resizingDrag()`
- 参照: `STATES.CROSSHAIRS`, `STATES.DRAGGING`, `STATES.DRAGGING_READY`, `STATES.RESIZING`, `this.#state`

## ScreenshotsOverlay.handlePointerUp()
- 位置: L600-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.draggingDragEnd()`, `this.draggingReadyDragEnd()`, `this.getCoordinatesFromEvent()`, `this.resizingDragEnd()`
- 参照: `STATES.DRAGGING`, `STATES.DRAGGING_READY`, `STATES.RESIZING`, `event.originalTarget.id`, `this.#state`

## ScreenshotsOverlay.handleKeyDown()
- 位置: L625-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.crosshairsKeyDown()`, `this.draggingKeyDown()`, `this.resizingKeyDown()`, `this.selectedKeyDown()`
- 条件付き依存: `if (event.key === "Escape")` → `this.maybeCancelScreenshots()`
- 参照: `STATES.CROSSHAIRS`, `STATES.DRAGGING`, `STATES.RESIZING`, `STATES.SELECTED`, `event.key`, `this.#state`

## ScreenshotsOverlay.handleKeyUp()
- 位置: L653-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`
- 参照: `STATES.RESIZING`, `STATES.SELECTED`, `event.key`, `event.originalTarget.id`, `this.#state`

## ScreenshotsOverlay.getAccelKey()
- 位置: L683-688
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`, `event.ctrlKey`, `event.metaKey`

## ScreenshotsOverlay.crosshairsKeyDown()
- 位置: L690-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`, `this.crosshairsDragStart()`, `this.handleKeyDownOnButton()`, `this.maybeLockFocus()`, `this.window.windowUtils.getLastOverWindowPointerLocationInCSSPixels()`
- 条件付き依存: `if (this.hoverElementRegion.isRegionValid)` → `this.draggingReadyStart()`
- 条件付き依存: `if (this.hoverElementRegion.isRegionValid)` → `this.draggingReadyDragEnd()`
- 条件付き依存: `if (Services.focus.focusedElement === this.previewFace)` → `this.previewFace.getBoundingClientRect()`
- 条件付き依存: `if (Services.focus.focusedElement === this.previewFace)` → `this.hoverElementRegion.setDimensionsFromDOMRect()`
- 条件付き依存: `if (Services.focus.focusedElement === this.previewFace)` → `this.draggingReadyStart()`
- 条件付き依存: `if (Services.focus.focusedElement === this.previewFace)` → `this.draggingReadyDragEnd()`
- 条件付き依存: `if (Services.focus.focusedElement === this.previewFace)` → `this.bottomRightMover.focus()`
- 参照: `STATES.DRAGGING`, `Services.appinfo.isWayland`, `Services.focus.focusedElement`, `event.key`, `this.hoverElementRegion.isRegionValid`, `this.previewFace`, `this.windowDimensions.scrollX`, `this.windowDimensions.scrollY`, `x.value`, `y.value`
- XPCOM: `Services.appinfo` / `Services.focus`

## ScreenshotsOverlay.draggingKeyDown()
- 位置: L760-783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`, `this.drawSelectionContainer()`, `this.handleArrowDownKeyDown()`, `this.handleArrowLeftKeyDown()`, `this.handleArrowRightKeyDown()`, `this.handleArrowUpKeyDown()`
- 参照: `STATES.SELECTED`, `event.key`

## ScreenshotsOverlay.resizingKeyDown()
- 位置: L790-805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resizingArrowDownKeyDown()`, `this.resizingArrowLeftKeyDown()`, `this.resizingArrowRightKeyDown()`, `this.resizingArrowUpKeyDown()`
- 参照: `event.key`

## ScreenshotsOverlay.selectedKeyDown()
- 位置: L807-858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.originalTarget.closest()`, `this.copyKey.toLowerCase()`, `this.downloadKey.toLowerCase()`, `this.getAccelKey()`, `this.handleKeyDownOnButton()`, `this.maybeLockFocus()`
- 条件付き依存: `if (isSelectionElement)` → `this.resizingArrowLeftKeyDown()`
- 条件付き依存: `if (isSelectionElement)` → `this.resizingArrowUpKeyDown()`
- 条件付き依存: `if (isSelectionElement)` → `this.resizingArrowRightKeyDown()`
- 条件付き依存: `if (isSelectionElement)` → `this.resizingArrowDownKeyDown()`
- 条件付き依存: `if ( this.mode !== SELECTION_MODES.MINI_WINDOW && this.state === "selected" && this.getAccelKey(event) )` → `this.copySelectedRegion()`
- 条件付き依存: `if ( this.mode !== SELECTION_MODES.MINI_WINDOW && this.state === "selected" && this.getAccelKey(event) )` → `this.downloadSelectedRegion()`
- 参照: `SELECTION_MODES.MINI_WINDOW`, `event.key`, `this.mode`, `this.state`

## ScreenshotsOverlay.resizingArrowLeftKeyDown()
- 位置: L868-876
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.handleArrowLeftKeyDown()`
- 条件付き依存: `if (this.#state !== STATES.RESIZING)` → `this.#setState()`
- 参照: `STATES.RESIZING`, `this.#state`

## ScreenshotsOverlay.handleArrowLeftKeyDown()
- 位置: L886-937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAccelKey()`, `this.scrollIfByEdge()`
- 条件付き依存: `if (event.originalTarget.id === "mover-topRight")` → `this.topLeftMover.focus()`
- 条件付き依存: `if (event.originalTarget.id === "mover-bottomRight")` → `this.bottomLeftMover.focus()`
- 条件付き依存: `if (this.selectionRegion.x1 >= this.selectionRegion.x2)` → `this.selectionRegion.sortCoords()`
- 参照: `event.originalTarget.id`, `event.shiftKey`, `this.selectionRegion.left`, `this.selectionRegion.right`, `this.selectionRegion.width`, `this.selectionRegion.x1`, `this.selectionRegion.x2`, `this.windowDimensions.clientHeight`, `this.windowDimensions.scrollX`, `this.windowDimensions.scrollY`

## ScreenshotsOverlay.resizingArrowUpKeyDown()
- 位置: L947-955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.handleArrowUpKeyDown()`
- 条件付き依存: `if (this.#state !== STATES.RESIZING)` → `this.#setState()`
- 参照: `STATES.RESIZING`, `this.#state`

## ScreenshotsOverlay.handleArrowUpKeyDown()
- 位置: L965-1016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAccelKey()`, `this.scrollIfByEdge()`
- 条件付き依存: `if (event.originalTarget.id === "mover-bottomLeft")` → `this.topLeftMover.focus()`
- 条件付き依存: `if (event.originalTarget.id === "mover-bottomRight")` → `this.topRightMover.focus()`
- 条件付き依存: `if (this.selectionRegion.y1 >= this.selectionRegion.y2)` → `this.selectionRegion.sortCoords()`
- 参照: `event.originalTarget.id`, `event.shiftKey`, `this.selectionRegion.bottom`, `this.selectionRegion.height`, `this.selectionRegion.top`, `this.selectionRegion.y1`, `this.selectionRegion.y2`, `this.windowDimensions.clientWidth`, `this.windowDimensions.scrollX`, `this.windowDimensions.scrollY`

## ScreenshotsOverlay.resizingArrowRightKeyDown()
- 位置: L1026-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.handleArrowRightKeyDown()`
- 条件付き依存: `if (this.#state !== STATES.RESIZING)` → `this.#setState()`
- 参照: `STATES.RESIZING`, `this.#state`

## ScreenshotsOverlay.handleArrowRightKeyDown()
- 位置: L1044-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAccelKey()`, `this.scrollIfByEdge()`
- 条件付き依存: `if (event.originalTarget.id === "mover-topLeft")` → `this.topRightMover.focus()`
- 条件付き依存: `if (event.originalTarget.id === "mover-bottomLeft")` → `this.bottomRightMover.focus()`
- 条件付き依存: `if (this.selectionRegion.x1 >= this.selectionRegion.x2)` → `this.selectionRegion.sortCoords()`
- 参照: `event.originalTarget.id`, `event.shiftKey`, `this.selectionRegion.left`, `this.selectionRegion.right`, `this.selectionRegion.width`, `this.selectionRegion.x1`, `this.selectionRegion.x2`, `this.windowDimensions.clientHeight`, `this.windowDimensions.clientWidth`, `this.windowDimensions.dimensions`, `this.windowDimensions.scrollX`, `this.windowDimensions.scrollY`

## ScreenshotsOverlay.resizingArrowDownKeyDown()
- 位置: L1108-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.handleArrowDownKeyDown()`
- 条件付き依存: `if (this.#state !== STATES.RESIZING)` → `this.#setState()`
- 参照: `STATES.RESIZING`, `this.#state`

## ScreenshotsOverlay.handleArrowDownKeyDown()
- 位置: L1118-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAccelKey()`, `this.scrollIfByEdge()`
- 条件付き依存: `if (event.originalTarget.id === "mover-topLeft")` → `this.bottomLeftMover.focus()`
- 条件付き依存: `if (event.originalTarget.id === "mover-topRight")` → `this.bottomRightMover.focus()`
- 条件付き依存: `if (this.selectionRegion.y1 >= this.selectionRegion.y2)` → `this.selectionRegion.sortCoords()`
- 参照: `event.originalTarget.id`, `event.shiftKey`, `this.selectionRegion.bottom`, `this.selectionRegion.height`, `this.selectionRegion.top`, `this.selectionRegion.y1`, `this.selectionRegion.y2`, `this.windowDimensions.clientHeight`, `this.windowDimensions.clientWidth`, `this.windowDimensions.dimensions`, `this.windowDimensions.scrollX`, `this.windowDimensions.scrollY`

## ScreenshotsOverlay.maybeLockFocus()
- 位置: L1180-1228
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.shiftKey)` → `this.previewFace.focus()`
- 条件付き依存: `if (!(event.shiftKey))` → `this.#dispatchEvent()`
- 条件付き依存: `if (event.shiftKey)` → `this.#dispatchEvent()`
- 条件付き依存: `if (!(event.shiftKey))` → `this.previewCancelButton.focus()`
- 条件付き依存: `if (event.originalTarget.id === "highlight" && event.shiftKey)` → `lastActionButton.focus()`
- 条件付き依存: `if ( event.originalTarget === lastActionButton && !event.shiftKey )` → `this.highlightEl.focus()`
- 条件付き依存: `if (!( event.originalTarget === lastActionButton && !event.shiftKey ))` → `Services.focus.moveFocus()`
- 参照: `STATES.CROSSHAIRS`, `STATES.SELECTED`, `Services.focus.FLAG_BYKEY`, `Services.focus.MOVEFOCUS_BACKWARD`, `Services.focus.MOVEFOCUS_FORWARD`, `event.originalTarget`, `event.originalTarget.id`, `event.shiftKey`, `this.#state`, `this.downloadButton`, `this.popButton`, `this.previewCancelButton`, `this.previewFace`, `this.window`
- XPCOM: `Services.focus`

## ScreenshotsOverlay.setFocusToActionButton()
- 位置: L1234-1242
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.popButton)` → `this.popButton.focus()`
- 条件付き依存: `if (lazy.SCREENSHOTS_LAST_SAVED_METHOD === "copy")` → `this.copyButton.focus()`
- 条件付き依存: `if (!(lazy.SCREENSHOTS_LAST_SAVED_METHOD === "copy"))` → `this.downloadButton.focus()`
- 参照: `lazy.SCREENSHOTS_LAST_SAVED_METHOD`, `this.popButton`

## ScreenshotsOverlay.handleKeyDownOnButton()
- 位置: L1252-1277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancelOverlay()`, `this.copySelectedRegion()`, `this.downloadSelectedRegion()`, `this.maybeCancelScreenshots()`, `this.popSelectedRegion()`, `this.reselectRegion()`
- 参照: `event.originalTarget`, `this.cancelButton`, `this.copyButton`, `this.downloadButton`, `this.miniWindowCancelButton`, `this.popButton`, `this.previewCancelButton`, `this.reselectButton`

## ScreenshotsOverlay.handleSelectionChange()
- 位置: L1284-1290
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.ranges.length)` → `this.selection.addRange()`
- 参照: `this.ranges`, `this.ranges.length`

## ScreenshotsOverlay.#dispatchEvent()
- 位置: L1298-1306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.windowUtils.dispatchEventToChromeOnly()`
- 参照: `this.window`

## ScreenshotsOverlay.#setState()
- 位置: L1314-1359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.crosshairsStart()`, `this.draggingReadyStart()`, `this.draggingStart()`, `this.resizingStart()`, `this.selectedStart()`
- 条件付き依存: `if ( this.#state === STATES.SELECTED && newState === STATES.CROSSHAIRS && this.#mode == SELECTION_MODES.SCREENSHOTS )` → `this.#dispatchEvent()`
- 条件付き依存: `if (newState !== this.#state)` → `this.#dispatchEvent()`
- 条件付き依存: `if (newState !== this.#state)` → `[ STATES.DRAGGING_READY, STATES.DRAGGING, STATES.RESIZING, STATES.SELECTED, ].includes()`
- 参照: `SELECTION_MODES.SCREENSHOTS`, `STATES.CROSSHAIRS`, `STATES.DRAGGING`, `STATES.DRAGGING_READY`, `STATES.RESIZING`, `STATES.SELECTED`, `this.#mode`, `this.#state`

## ScreenshotsOverlay.copySelectedRegion()
- 位置: L1361-1365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchEvent()`
- 参照: `this.selectionRegion.dimensions`

## ScreenshotsOverlay.downloadSelectedRegion()
- 位置: L1367-1371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchEvent()`
- 参照: `this.selectionRegion.dimensions`

## ScreenshotsOverlay.popSelectedRegion()
- 位置: L1373-1379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchEvent()`
- 参照: `this.selectionRegion.dimensions`, `this.windowDimensions.clientHeight`, `this.windowDimensions.clientWidth`

## ScreenshotsOverlay.crosshairsStart()
- 位置: L1386-1395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchEvent()`, `this.hideButtonsContainer()`, `this.hideHoverElementContainer()`, `this.hideSelectionContainer()`, `this.hoverElementRegion.resetDimensions()`, `this.showPreviewContainer()`
- 参照: `this.#cachedEle`, `this.#previousDimensions`

## ScreenshotsOverlay.draggingReadyStart()
- 位置: L1400-1402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dispatchEvent()`

## ScreenshotsOverlay.draggingStart()
- 位置: L1408-1413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.hideButtonsContainer()`, `this.hideHoverElementContainer()`, `this.hidePreviewContainer()`

## ScreenshotsOverlay.selectedStart()
- 位置: L1422-1433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#ensureMiniWindowRegionSize()`, `this.drawButtonsContainer()`, `this.drawSelectionContainer()`, `this.hideHoverElementContainer()`, `this.hidePreviewContainer()`, `this.selectionRegion.sortCoords()`
- 条件付き依存: `if (!options.doNotMoveFocus)` → `this.setFocusToActionButton()`
- 参照: `options.doNotMoveFocus`

## ScreenshotsOverlay.#ensureMiniWindowRegionSize()
- 位置: L1438-1455
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SELECTION_MODES.MINI_WINDOW`, `region.bottom`, `region.height`, `region.left`, `region.right`, `region.top`, `region.width`, `this.mode`, `this.selectionRegion`

## ScreenshotsOverlay.resizingStart()
- 位置: L1463-1467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hideButtonsContainer()`
- 参照: `this.#previousDimensions`, `this.selectionRegion.dimensions`

## ScreenshotsOverlay.crosshairsDragStart()
- 位置: L1476-1485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`
- 参照: `STATES.DRAGGING_READY`, `this.selectionRegion.dimensions`

## ScreenshotsOverlay.selectedDragStart()
- 位置: L1495-1505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`
- 条件付き依存: `if (targetId === this.screenshotsContainer.id)` → `this.#setState()`
- 参照: `STATES.CROSSHAIRS`, `STATES.RESIZING`, `this.#lastPageX`, `this.#lastPageY`, `this.#moverId`, `this.screenshotsContainer.id`

## ScreenshotsOverlay.crosshairsMove()
- 位置: L1514-1518
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawPreviewEyes()`, `this.handleElementHover()`

## ScreenshotsOverlay.draggingReadyDrag()
- 位置: L1527-1536
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.selectionRegion.distance > 40)` → `this.#setState()`
- 参照: `STATES.DRAGGING`, `this.selectionRegion.dimensions`, `this.selectionRegion.distance`

## ScreenshotsOverlay.draggingDrag()
- 位置: L1545-1553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.scrollIfByEdge()`
- 参照: `this.selectionRegion.dimensions`

## ScreenshotsOverlay.resizingDrag()
- 位置: L1561-1676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.drawSelectionContainer()`, `this.scrollIfByEdge()`
- 参照: `this.#lastPageX`, `this.#lastPageY`, `this.#moverId`, `this.#previousDimensions.height`, `this.#previousDimensions.width`, `this.selectionRegion.dimensions`, `this.windowDimensions.dimensions`

## ScreenshotsOverlay.draggingReadyDragEnd()
- 位置: L1685-1696
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.hoverElementRegion.isRegionValid)` → `this.#setState()`
- 条件付き依存: `if (this.hoverElementRegion.isRegionValid)` → `this.#dispatchEvent()`
- 条件付き依存: `if (!(this.hoverElementRegion.isRegionValid))` → `this.#setState()`
- 参照: `STATES.CROSSHAIRS`, `STATES.SELECTED`, `this.#methodsUsed.element`, `this.hoverElementRegion.dimensions`, `this.hoverElementRegion.isRegionValid`, `this.selectionRegion.dimensions`

## ScreenshotsOverlay.draggingDragEnd()
- 位置: L1704-1712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`, `this.maybeRecordRegionSelected()`
- 参照: `STATES.SELECTED`, `this.#methodsUsed.region`, `this.selectionRegion.dimensions`

## ScreenshotsOverlay.resizingDragEnd()
- 位置: L1721-1730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setState()`, `this.maybeRecordRegionSelected()`, `this.resizingDrag()`
- 参照: `STATES.SELECTED`, `this.#methodsUsed.move`, `this.#methodsUsed.resize`, `this.#moverId`

## ScreenshotsOverlay.maybeRecordRegionSelected()
- 位置: L1732-1747
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if ( !this.#previousDimensions || (Math.abs(this.#previousDimensions.width - width) > REGION_CHANGE_THRESHOLD && Math.abs(this.#previousDimensions.height - heigh...)` → `this.#dispatchEvent()`
- 参照: `this.#previousDimensions`, `this.#previousDimensions.height`, `this.#previousDimensions.width`, `this.selectionRegion.dimensions`

## ScreenshotsOverlay.drawPreviewEyes()
- 位置: L1755-1766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`
- 参照: `this.leftEye`, `this.leftEye.style`, `this.rightEye.style`, `this.windowDimensions.dimensions`

## ScreenshotsOverlay.showPreviewContainer()
- 位置: L1768-1770
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.previewContainer.hidden`

## ScreenshotsOverlay.hidePreviewContainer()
- 位置: L1772-1774
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.previewContainer.hidden`

## ScreenshotsOverlay.updatePreviewContainer()
- 位置: L1776-1780
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.previewContainer.style.height`, `this.previewContainer.style.width`, `this.windowDimensions.dimensions`

## ScreenshotsOverlay.updateScreenshotsOverlayContainer()
- 位置: L1785-1789
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.screenshotsContainer.style`, `this.windowDimensions.dimensions`

## ScreenshotsOverlay.showScreenshotsOverlayContainer()
- 位置: L1791-1793
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.screenshotsContainer.hidden`

## ScreenshotsOverlay.hideScreenshotsOverlayContainer()
- 位置: L1795-1797
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.screenshotsContainer.hidden`

## ScreenshotsOverlay.drawHoverElementRegion()
- 位置: L1802-1808
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showHoverElementContainer()`
- 参照: `this.hoverElementContainer.style`, `this.hoverElementRegion.dimensions`

## ScreenshotsOverlay.showHoverElementContainer()
- 位置: L1810-1812
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.hoverElementContainer.hidden`

## ScreenshotsOverlay.hideHoverElementContainer()
- 位置: L1814-1816
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.hoverElementContainer.hidden`

## ScreenshotsOverlay.drawSelectionContainer()
- 位置: L1822-1836
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showSelectionContainer()`, `this.updateSelectionSizeText()`
- 参照: `this.bottomBackgroundEl.style`, `this.highlightEl.style`, `this.leftBackgroundEl.style`, `this.rightBackgroundEl.style`, `this.selectionRegion.dimensions`, `this.topBackgroundEl.style.height`

## ScreenshotsOverlay.updateSelectionSizeText()
- 位置: L1842-1857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.round()`, `lazy.overlayLocalization.formatMessagesSync()`
- 参照: `selectionSizeTranslation.value`, `this.selectionRegion.dimensions`, `this.selectionSize.textContent`, `this.window.browsingContext.fullZoom`

## ScreenshotsOverlay.showSelectionContainer()
- 位置: L1859-1861
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectionContainer.hidden`

## ScreenshotsOverlay.hideSelectionContainer()
- 位置: L1863-1865
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectionContainer.hidden`

## ScreenshotsOverlay.drawButtonsContainer()
- 位置: L1873-1933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.showButtonsContainer()`, `this.windowDimensions.isInViewport()`
- 条件付き依存: `if (!this.buttonsContainerRect)` → `this.buttonsContainer.getBoundingClientRect()`
- 条件付き依存: `if (isLTR)` → `Math.max()`
- 条件付き依存: `if (isLTR)` → `Math.min()`
- 条件付き依存: `if (isLTR)` → `Math.ceil()`
- 条件付き依存: `if (!(isLTR))` → `Math.min()`
- 条件付き依存: `if (!(isLTR))` → `Math.max()`
- 条件付き依存: `if (!(isLTR))` → `Math.ceil()`
- 参照: `Services.locale.isAppLocaleRTL`, `this.buttonsContainer.style.left`, `this.buttonsContainer.style.right`, `this.buttonsContainer.style.top`, `this.buttonsContainerRect`, `this.buttonsContainerRect.width`, `this.selectionRegion.dimensions`, `this.windowDimensions.dimensions`
- XPCOM: `Services.locale`

## ScreenshotsOverlay.showButtonsContainer()
- 位置: L1935-1937
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.buttonsContainer.hidden`

## ScreenshotsOverlay.hideButtonsContainer()
- 位置: L1939-1941
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.buttonsContainer.hidden`

## ScreenshotsOverlay.updateCursorRegion()
- 位置: L1943-1945
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.cursorRegion`

## ScreenshotsOverlay.setPointerEventsNone()
- 位置: L1951-1953
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.screenshotsContainer.style.pointerEvents`

## ScreenshotsOverlay.resetPointerEvents()
- 位置: L1955-1957
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.screenshotsContainer.style.pointerEvents`

## ScreenshotsOverlay.handleElementHover()
- 位置: async L1967-1995
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getElementFromPoint()`, `this.resetPointerEvents()`, `this.setPointerEventsNone()`, `this.window.HTMLIFrameElement.isInstance()`
- 条件付き依存: `if (!rect)` → `getBestRectForElement()`
- 条件付き依存: `if (rect)` → `this.hoverElementRegion.setDimensionsFromDOMRect()`
- 条件付き依存: `if (rect)` → `this.drawHoverElementRegion()`
- 条件付き依存: `if (!(rect))` → `this.hoverElementRegion.resetDimensions()`
- 条件付き依存: `if (!(rect))` → `this.hideHoverElementContainer()`
- 参照: `this.#cachedEle`, `this.document`

## ScreenshotsOverlay.scrollIfByEdge()
- 位置: L2003-2022
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pageY - scrollY < SCROLL_BY_EDGE)` → `this.scrollWindow()`
- 条件付き依存: `if (scrollY + clientHeight - pageY < SCROLL_BY_EDGE)` → `this.scrollWindow()`
- 条件付き依存: `if (pageX - scrollX <= SCROLL_BY_EDGE)` → `this.scrollWindow()`
- 条件付き依存: `if (scrollX + clientWidth - pageX <= SCROLL_BY_EDGE)` → `this.scrollWindow()`
- 参照: `this.windowDimensions.dimensions`

## ScreenshotsOverlay.scrollWindow()
- 位置: L2030-2033
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateScreenshotsOverlayDimensions()`, `this.window.scrollBy()`

## ScreenshotsOverlay.updateScreenshotsOverlayDimensions()
- 位置: async L2041-2061
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateWindowDimensions()`
- 条件付き依存: `if (eventType === "resize")` → `this.hideHoverElementContainer()`
- 条件付き依存: `if (this.#lastClientX && this.#lastClientY)` → `this.handleElementHover()`
- 条件付き依存: `if (this.#state === STATES.SELECTED)` → `this.selectionRegion.shift()`
- 条件付き依存: `if (this.#state === STATES.SELECTED)` → `this.drawSelectionContainer()`
- 条件付き依存: `if (this.#state === STATES.SELECTED)` → `this.drawButtonsContainer()`
- 条件付き依存: `if (this.#state === STATES.SELECTED)` → `this.updateSelectionSizeText()`
- 参照: `STATES.CROSSHAIRS`, `STATES.SELECTED`, `this.#cachedEle`, `this.#lastClientX`, `this.#lastClientY`, `this.#state`

## ScreenshotsOverlay.getDimensionsFromWindow()
- 位置: L2080-2124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `this.window.windowUtils.getScrollbarSize()`
- 参照: `docEl.scrollHeight`, `docEl.scrollWidth`, `scrollbarHeight.value`, `scrollbarWidth.value`, `this.window`, `this.window.document.documentElement`

## ScreenshotsOverlay.updateWindowDimensions()
- 位置: async L2134-2175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `setMaxDetectHeight()`, `setMaxDetectWidth()`, `this.getDimensionsFromWindow()`, `this.screenshotsContainer.toggleAttribute()`, `this.updatePreviewContainer()`, `this.updateScreenshotsOverlayContainer()`, `this.window.requestAnimationFrame()`
- 参照: `this.window.devicePixelRatio`, `this.windowDimensions.dimensions`
