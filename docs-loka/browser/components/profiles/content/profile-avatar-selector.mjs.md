# browser/components/profiles/content/profile-avatar-selector.mjs

source: browser/components/profiles/content/profile-avatar-selector.mjs
source-hash: b561c39936b2f321497050f9c615cc1831edab52
lines: 1047

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ProfileAvatarSelector.constructor()
- 位置: L115-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.setView()`
- 参照: `STATES.SELECTED`, `VIEWS.ICON`, `this.avatarLabels`, `this.avatarRegion`, `this.state`, `this.viewDimensions`

## ProfileAvatarSelector.connectedCallback()
- 位置: async L126-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.connectedCallback()`, `this.loadAvatarLabels()`

## ProfileAvatarSelector.loadAvatarLabels()
- 位置: async L132-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AVATARS.map()`, `document.l10n.formatValues()`, `this.getAvatarL10nId()`, `this.requestUpdate()`
- 参照: `AVATARS.length`, `this.avatarLabels`

## ProfileAvatarSelector.setView()
- 位置: L145-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cropViewStart()`
- 条件付き依存: `if (this.view === VIEWS.CROP)` → `this.cropViewEnd()`
- 参照: `VIEWS.CROP`, `VIEWS.CUSTOM`, `VIEWS.ICON`, `this.view`

## ProfileAvatarSelector.toggleHidden()
- 位置: L164-179
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (force === true || (this.dialog.open && force !== false))` → `this.dialog.close()`
- 条件付き依存: `if (!(force === true || (this.dialog.open && force !== false)))` → `this.dialog.show()`
- 条件付き依存: `if (!this.dialog.open)` → `document.removeEventListener()`
- 条件付き依存: `if (!this.dialog.open)` → `window.removeEventListener()`
- 条件付き依存: `if (!(!this.dialog.open))` → `document.addEventListener()`
- 条件付き依存: `if (!(!this.dialog.open))` → `window.addEventListener()`
- 参照: `this.dialog.open`

## ProfileAvatarSelector.show()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleHidden()`

## ProfileAvatarSelector.hide()
- 位置: L185-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleHidden()`

## ProfileAvatarSelector.maybeHide()
- 位置: L189-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hide()`
- 条件付き依存: `if (this.view === VIEWS.CROP)` → `this.setView()`
- 参照: `VIEWS.CROP`, `VIEWS.CUSTOM`, `this.view`

## ProfileAvatarSelector.cropViewStart()
- 位置: L198-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.classList.add()`, `window.addEventListener()`

## ProfileAvatarSelector.cropViewEnd()
- 位置: L205-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.classList.remove()`, `window.removeEventListener()`

## ProfileAvatarSelector.getAvatarL10nId()
- 位置: L211-272
- 役割: (未記入)
- 触るとき: (未記入)

## ProfileAvatarSelector.handleAvatarChange()
- 位置: L274-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`
- 参照: `this.avatarPicker.value`

## ProfileAvatarSelector.handleTabChange()
- 位置: L284-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopImmediatePropagation()`
- 条件付き依存: `if (event.target.value === VIEWS.ICON)` → `this.setView()`
- 条件付き依存: `if (!(event.target.value === VIEWS.ICON))` → `this.setView()`
- 参照: `VIEWS.CUSTOM`, `VIEWS.ICON`, `event.target.value`

## ProfileAvatarSelector.iconTabContentTemplate()
- 位置: L293-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AVATARS.map()`, `html()`, `ifDefined()`
- 参照: `this.avatarLabels`, `this.handleAvatarChange`, `this.value`

## ProfileAvatarSelector.customTabUploadFileContentTemplate()
- 位置: L320-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleFileUpload`

## ProfileAvatarSelector.customTabViewImageTemplate()
- 位置: L344-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.blobURL`, `this.handleBackKeyDown`, `this.handleCancelClick`, `this.handleCancelKeyDown`, `this.handleSaveClick`, `this.handleSaveKeyDown`, `this.imageLoaded`

## ProfileAvatarSelector.handleCancelClick()
- 位置: L428-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopImmediatePropagation()`, `this.setView()`
- 条件付き依存: `if (this.blobURL)` → `URL.revokeObjectURL()`
- 参照: `VIEWS.CUSTOM`, `this.blobURL`, `this.file`

## ProfileAvatarSelector.handleBackKeyDown()
- 位置: L438-443
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `event.preventDefault()`
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `this.handleCancelClick()`
- 参照: `event.code`

## ProfileAvatarSelector.handleCancelKeyDown()
- 位置: L445-450
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `event.preventDefault()`
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `this.handleCancelClick()`
- 参照: `event.code`

## ProfileAvatarSelector.handleSaveKeyDown()
- 位置: L452-457
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `event.preventDefault()`
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `this.handleSaveClick()`
- 参照: `event.code`

## ProfileAvatarSelector.handleSaveClick()
- 位置: async L459-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `document.dispatchEvent()`, `event.stopImmediatePropagation()`, `img.decode()`, `squareCanvas.convertToBlob()`, `squareCanvas.getContext()`, `squareCtx.arc()`, `squareCtx.beginPath()`, `squareCtx.clip()`, `squareCtx.drawImage()`, `this.hide()`, `this.setView()`
- 条件付き依存: `if (this.blobURL)` → `URL.revokeObjectURL()`
- 参照: `Math.PI`, `VIEWS.CUSTOM`, `img.src`, `this.avatarRegion.dimensions`, `this.blobURL`, `this.customAvatarCropArea`, `this.customAvatarCropArea.clientHeight`, `this.customAvatarCropArea.clientWidth`, `this.file.name`, `this.viewDimensions.dimensions`

## ProfileAvatarSelector.updateViewDimensions()
- 位置: L525-539
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (width > height)` → `this.customAvatarImage.classList.add()`
- 条件付き依存: `if (!(width > height))` → `this.customAvatarImage.classList.add()`
- 参照: `this.customAvatarCropArea.clientHeight`, `this.customAvatarCropArea.clientWidth`, `this.customAvatarImage`, `this.viewDimensions.dimensions`, `window.devicePixelRatio`

## ProfileAvatarSelector.imageLoaded()
- 位置: L541-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.highlight.focus()`, `this.setInitialAvatarSelection()`, `this.updateViewDimensions()`

## ProfileAvatarSelector.setInitialAvatarSelection()
- 位置: L547-565
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.min()`, `this.avatarRegion.resizeToSquare()`, `this.drawSelectionContainer()`
- 参照: `this.viewDimensions.height`, `this.viewDimensions.width`

## ProfileAvatarSelector.drawSelectionContainer()
- 位置: L567-572
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.avatarRegion.dimensions`, `this.highlight.style`

## ProfileAvatarSelector.getCoordinatesFromEvent()
- 位置: L574-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarSelectionContainer.getBoundingClientRect()`
- 参照: `rect.x`, `rect.y`

## ProfileAvatarSelector.handleEvent()
- 位置: L581-617
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element?.getRootNode()`, `this.handleKeyDown()`, `this.handlePointerDown()`, `this.handlePointerMove()`, `this.handlePointerUp()`, `this.hide()`
- 参照: `VIEWS.CROP`, `element?.getRootNode()?.host`, `event.originalTarget`, `event.type`, `this.view`

## ProfileAvatarSelector.handlePointerDown()
- 位置: L619-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ "highlight", "mover-topLeft", "mover-topRight", "mover-bottomRight", "mover-bottomLeft", ].includes()`
- 参照: `STATES.RESIZING`, `event.originalTarget?.id`, `this.#moverId`, `this.state`

## ProfileAvatarSelector.handlePointerMove()
- 位置: L635-640
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.state === STATES.RESIZING)` → `this.getCoordinatesFromEvent()`
- 条件付き依存: `if (this.state === STATES.RESIZING)` → `this.handleResizingPointerMove()`
- 参照: `STATES.RESIZING`, `this.state`

## ProfileAvatarSelector.handleResizingPointerMove()
- 位置: L642-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarRegion.resizeToSquare()`, `this.drawSelectionContainer()`, `this.scrollIfByEdge()`
- 参照: `this.#moverId`, `this.avatarRegion.bottom`, `this.avatarRegion.left`, `this.avatarRegion.right`, `this.avatarRegion.top`

## ProfileAvatarSelector.handlePointerUp()
- 位置: L704-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarRegion.sortCoords()`
- 参照: `STATES.SELECTED`, `this.#moverId`, `this.state`

## ProfileAvatarSelector.handleKeyDown()
- 位置: L710-740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.drawSelectionContainer()`, `this.handleArrowDownKeyDown()`, `this.handleArrowLeftKeyDown()`, `this.handleArrowRightKeyDown()`, `this.handleArrowUpKeyDown()`
- 条件付き依存: `if (event.key === "Escape")` → `this.maybeHide()`
- 参照: `VIEWS.CROP`, `event.key`, `this.view`

## ProfileAvatarSelector.handleArrowLeftKeyDown()
- 位置: L742-795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarRegion.forceSquare()`, `this.scrollIfByEdge()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.avatarRegion.sortCoords()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.bottomLeftMover.focus()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.topLeftMover.focus()`
- 参照: `event.originalTarget.id`, `this.avatarRegion.bottom`, `this.avatarRegion.left`, `this.avatarRegion.right`, `this.avatarRegion.top`, `this.avatarRegion.x1`, `this.avatarRegion.x2`, `this.avatarRegion.y1`, `this.avatarRegion.y2`, `this.viewDimensions.height`

## ProfileAvatarSelector.handleArrowUpKeyDown()
- 位置: L797-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarRegion.forceSquare()`, `this.scrollIfByEdge()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.avatarRegion.sortCoords()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.topRightMover.focus()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.topLeftMover.focus()`
- 参照: `event.originalTarget.id`, `this.avatarRegion.bottom`, `this.avatarRegion.left`, `this.avatarRegion.right`, `this.avatarRegion.top`, `this.avatarRegion.x1`, `this.avatarRegion.x2`, `this.avatarRegion.y1`, `this.avatarRegion.y2`, `this.viewDimensions.width`

## ProfileAvatarSelector.handleArrowRightKeyDown()
- 位置: L852-905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarRegion.forceSquare()`, `this.scrollIfByEdge()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.avatarRegion.sortCoords()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.bottomRightMover.focus()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.topRightMover.focus()`
- 参照: `event.originalTarget.id`, `this.avatarRegion.bottom`, `this.avatarRegion.left`, `this.avatarRegion.right`, `this.avatarRegion.top`, `this.avatarRegion.x1`, `this.avatarRegion.x2`, `this.avatarRegion.y1`, `this.avatarRegion.y2`, `this.viewDimensions.height`

## ProfileAvatarSelector.handleArrowDownKeyDown()
- 位置: L907-960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.avatarRegion.forceSquare()`, `this.scrollIfByEdge()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.avatarRegion.sortCoords()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.bottomRightMover.focus()`
- 条件付き依存: `if ( this.avatarRegion.x1 >= this.avatarRegion.x2 || this.avatarRegion.y1 >= this.avatarRegion.y2 )` → `this.bottomLeftMover.focus()`
- 参照: `event.originalTarget.id`, `this.avatarRegion.bottom`, `this.avatarRegion.left`, `this.avatarRegion.right`, `this.avatarRegion.top`, `this.avatarRegion.x1`, `this.avatarRegion.x2`, `this.avatarRegion.y1`, `this.avatarRegion.y2`, `this.viewDimensions.width`

## ProfileAvatarSelector.scrollIfByEdge()
- 位置: L962-980
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (viewY <= SCROLL_BY_EDGE)` → `this.scrollView()`
- 条件付き依存: `if (height - viewY < SCROLL_BY_EDGE)` → `this.scrollView()`
- 条件付き依存: `if (viewX <= SCROLL_BY_EDGE)` → `this.scrollView()`
- 条件付き依存: `if (width - viewX <= SCROLL_BY_EDGE)` → `this.scrollView()`
- 参照: `this.viewDimensions.dimensions`

## ProfileAvatarSelector.scrollView()
- 位置: L982-984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.customAvatarCropArea.scrollBy()`

## ProfileAvatarSelector.handleFileUpload()
- 位置: L986-996
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.createObjectURL()`, `this.setView()`
- 条件付き依存: `if (this.blobURL)` → `URL.revokeObjectURL()`
- 参照: `VIEWS.CROP`, `event.target.files`, `this.blobURL`, `this.file`

## ProfileAvatarSelector.contentTemplate()
- 位置: L998-1011
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.customTabUploadFileContentTemplate()`, `this.customTabViewImageTemplate()`, `this.iconTabContentTemplate()`
- 参照: `VIEWS.CROP`, `VIEWS.CUSTOM`, `VIEWS.ICON`, `this.view`

## ProfileAvatarSelector.render()
- 位置: L1013-1043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.contentTemplate()`
- 参照: `VIEWS.CUSTOM`, `VIEWS.ICON`, `this.handleTabChange`, `this.view`
