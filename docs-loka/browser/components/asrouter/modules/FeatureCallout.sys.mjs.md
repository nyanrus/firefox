# browser/components/asrouter/modules/FeatureCallout.sys.mjs

source: browser/components/asrouter/modules/FeatureCallout.sys.mjs
source-hash: bb0eba92ef596e1c30176f563863a04f81286f33
lines: 2629

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## FeatureCallout.constructor()
- 位置: L58-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._handlePrefChange.bind()`, `this._initTheme()`, `this.setupFeatureTourProgress()`, `this.win.addEventListener()`
- 条件付き依存: `if (this.context !== "chrome")` → `this.win.addEventListener()`
- 参照: `pref?.name`, `this.AWSetup`, `this._featureTourProgress`, `this._handlePrefChange`, `this._panelConflictListenersRegistered`, `this._positionListenersRegistered`, `this.browser`, `this.config`, `this.context`, `this.currentScreen`, `this.doc`, `this.listener`, `this.loadingConfig`, `this.location`, `this.message`, `this.pref`, `this.ready`, `this.renderObserver`, `this.savedFocus`, `this.win`, `this.win.docShell.chromeEventHandler`, `win.document`

## FeatureCallout.setupFeatureTourProgress()
- 位置: L103-111
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.pref?.name)` → `this._handlePrefChange()`
- 条件付き依存: `if (this.pref?.name)` → `Services.prefs.addObserver()`
- 参照: `this._handlePrefChange`, `this.featureTourProgress`, `this.pref.name`, `this.pref?.name`
- XPCOM: `Services.prefs`

## FeatureCallout.teardownFeatureTourProgress()
- 位置: L113-118
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.pref?.name)` → `Services.prefs.removeObserver()`
- 参照: `this._featureTourProgress`, `this._handlePrefChange`, `this.pref.name`, `this.pref?.name`
- XPCOM: `Services.prefs`

## FeatureCallout.featureTourProgress()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._featureTourProgress`

## FeatureCallout._loadPageEventManager()
- 位置: L130-135
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PageEventManager`, `this._pageEventManager`, `this.win`

## FeatureCallout._addPositionListeners()
- 位置: L137-142
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._positionListenersRegistered)` → `this.win.addEventListener()`
- 参照: `this._positionListenersRegistered`

## FeatureCallout._removePositionListeners()
- 位置: L144-149
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._positionListenersRegistered)` → `this.win.removeEventListener()`
- 参照: `this._positionListenersRegistered`

## FeatureCallout._addPanelConflictListeners()
- 位置: L151-157
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._panelConflictListenersRegistered)` → `this.win.addEventListener()`
- 条件付き依存: `if (!this._panelConflictListenersRegistered)` → `this.win.gURLBar.controller.addListener()`
- 参照: `this._panelConflictListenersRegistered`

## FeatureCallout._removePanelConflictListeners()
- 位置: L159-165
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._panelConflictListenersRegistered)` → `this.win.removeEventListener()`
- 条件付き依存: `if (this._panelConflictListenersRegistered)` → `this.win.gURLBar.controller.removeListener()`
- 参照: `this._panelConflictListenersRegistered`

## FeatureCallout.onViewOpen()
- 位置: L171-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.endTour()`

## FeatureCallout._handlePrefChange()
- 位置: L175-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`
- 条件付き依存: `if (topic === "nsPref:changed")` → `this._advanceOnTourPrefChange()`
- 参照: `this._featureTourProgress`, `this.pref.defaultValue`, `this.pref.name`, `this.pref?.name`
- XPCOM: `Services.prefs`

## FeatureCallout._advanceScreens()
- 位置: L213-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `this._container?.classList.toggle()`, `this._pageEventManager?.emit()`, `this.config.screens.findIndex()`
- 条件付き依存: `if (!this.currentScreen)` → `lazy.log.error()`
- 条件付き依存: `if ((!direction || !Number.isInteger(direction)) && !id)` → `lazy.log.debug()`
- 条件付き依存: `if (id === "%end%")` → `this.endTour()`
- 条件付き依存: `if (id)` → `this.config.screens.findIndex()`
- 条件付き依存: `if (nextIndex === -1)` → `lazy.log.debug()`
- 条件付き依存: `if (nextIndex === currentIndex)` → `lazy.log.debug()`
- 条件付き依存: `if (!(id))` → `Math.max()`
- 条件付き依存: `if (nextIndex < 0)` → `lazy.log.debug()`
- 条件付き依存: `if (nextIndex >= this.config.screens.length)` → `this.endTour()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.removeEventListener()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.addEventListener()`
- 条件付き依存: `if (event.target === this._container)` → `controller.abort()`
- 条件付き依存: `if (event.target === this._container)` → `onFadeOut()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.hidePopup()`
- 条件付き依存: `if (!(this._container?.localName === "panel"))` → `this.win.setTimeout()`
- 参照: `controller.signal`, `event.target`, `screen.id`, `this._container`, `this._container?.localName`, `this.config.screens.length`, `this.currentScreen`, `this.currentScreen.id`, `this.location`, `this.ready`

## onFadeOut()
- 位置: async L276-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._container?.remove()`, `this._removePanelConflictListeners()`, `this._removePositionListeners()`, `this._renderCallout()`, `this._updateConfig()`, `this.doc.querySelector()`, `this.doc.querySelector(`[src="${BUNDLE_SRC}"]`)?.remove()`, `this.renderObserver?.disconnect()`
- 条件付き依存: `if (this.message)` → `lazy.ASRouter.isUnblockedMessage()`
- 条件付き依存: `if (!isMessageUnblocked)` → `this.endTour()`
- 条件付き依存: `if (!updated && !this.currentScreen)` → `this.endTour()`
- 条件付き依存: `if (!rendering)` → `this.endTour()`
- 参照: `this.currentScreen`, `this.message`

## FeatureCallout._advanceOnTourPrefChange()
- 位置: L320-422
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this.config?.screens.length === 1 || this.currentScreen === "spotlight" )` → `this.showFeatureCallout()`
- 条件付き依存: `if (prefVal.complete)` → `this.endTour()`
- 条件付き依存: `if (prefVal.screen !== this.currentScreen?.id)` → `this._container?.classList.toggle()`
- 条件付き依存: `if (prefVal.screen !== this.currentScreen?.id)` → `this._pageEventManager?.emit()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.removeEventListener()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.addEventListener()`
- 条件付き依存: `if (event.target === this._container)` → `controller.abort()`
- 条件付き依存: `if (event.target === this._container)` → `onFadeOut()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.hidePopup()`
- 条件付き依存: `if (!(this._container?.localName === "panel"))` → `this.win.setTimeout()`
- 参照: `controller.signal`, `event.target`, `prefVal.complete`, `prefVal.screen`, `this._container`, `this._container?.localName`, `this.config?.screens.length`, `this.context`, `this.currentScreen`, `this.currentScreen?.id`, `this.doc.visibilityState`, `this.featureTourProgress`, `this.ready`

## onFadeOut()
- 位置: async L360-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouterTargeting.getMessageTriggers()`, `lazy.ASRouterTargeting.getMessageTriggers(this.message).some()`, `this._container?.remove()`, `this._removePanelConflictListeners()`, `this._removePositionListeners()`, `this._renderCallout()`, `this._updateConfig()`, `this.doc.querySelector()`, `this.doc.querySelector(`[src="${BUNDLE_SRC}"]`)?.remove()`, `this.renderObserver?.disconnect()`
- 条件付き依存: `if ( this.context === "chrome" && !lazy.ASRouterTargeting.getMessageTriggers(this.message).some( t => t.id === "featureCalloutCheck" ) )` → `this.config?.screens.some()`
- 条件付き依存: `if ( this.context === "chrome" && !lazy.ASRouterTargeting.getMessageTriggers(this.message).some( t => t.id === "featureCalloutCheck" ) )` → `this.config.screens.some()`
- 条件付き依存: `if (nextMessage)` → `lazy.ASRouter.isUnblockedMessage()`
- 条件付き依存: `if (!isMessageUnblocked)` → `this.endTour()`
- 条件付き依存: `if (!updated && !this.currentScreen)` → `this.endTour()`
- 条件付き依存: `if (!rendering)` → `this.endTour()`
- 参照: `prefVal.screen`, `s.id`, `t.id`, `this.context`, `this.currentScreen`, `this.currentScreen?.id`, `this.message`

## FeatureCallout.handleEvent()
- 位置: L424-511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Node.isInstance()`, `event.preventDefault()`, `event.target.hasAttribute()`, `this._advanceOnTourPrefChange()`, `this._container.contains()`, `this._dismiss()`, `this._positionCallout()`, `this.config?.id.toUpperCase()`, `this.endTour()`, `this.win.AWSendEventTelemetry()`, `this.win.requestAnimationFrame()`
- 条件付き依存: `if (this.doc.activeElement)` → `element.matches()`
- 条件付き依存: `if ( event.target.documentGlobal === this.win && event.target !== this._container && event.target.localName === "panel" && event.target.id !== "ctrlTab-panel" &&...)` → `this.endTour()`
- 条件付き依存: `if (event.target === this._container)` → `this.endTour()`
- 参照: `event.key`, `event.target`, `event.target.documentGlobal`, `event.target.id`, `event.target.localName`, `event.type`, `this._container`, `this.doc.activeElement`, `this.location`, `this.savedFocus`, `this.win`

## FeatureCallout._addCalloutLinkElements()
- 位置: async L513-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addStylesheet()`, `this.win.MozXULElement.insertFTLIfNeeded()`

## addChromeSheet()
- 位置: L525-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.win.windowUtils.loadSheetUsingURIString()`
- 参照: `Ci.nsIDOMWindowUtils.AUTHOR_SHEET`
- XPCOM: [`nsIDOMWindowUtils`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md)

## addStylesheet()
- 位置: L537-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doc.createElement()`, `this.doc.head.appendChild()`, `this.doc.querySelector()`
- 条件付き依存: `if (this.win.isChromeWindow)` → `addChromeSheet()`
- 参照: `link.href`, `link.rel`, `this.win.isChromeWindow`

## FeatureCallout._getAnchor()
- 位置: L712-805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `scope.matches()`, `scope.querySelector()`, `selector.includes()`, `this._HTMLArrowPositions.includes()`, `this._isElementVisible()`, `this._resolveSelectorAndScope()`
- 条件付き依存: `if (!anchor || typeof anchor !== "object")` → `lazy.log.debug()`
- 条件付き依存: `if (panel_position)` → `this._getPanelPositionString()`
- 条件付き依存: `if (!panel_position_string && !arrow_position)` → `lazy.log.debug()`
- 条件付き依存: `if (!panel_position_string && !arrow_position)` → `JSON.stringify()`
- 条件付き依存: `if ( arrow_position && !this._HTMLArrowPositions.includes(arrow_position) )` → `lazy.log.debug()`
- 条件付き依存: `if ( arrow_position && !this._HTMLArrowPositions.includes(arrow_position) )` → `JSON.stringify()`
- 条件付き依存: `if ( this.context === "chrome" && element.id && selector.includes(`#${element.id}`) )` → `lazy.CustomizableUI.getWidget()`
- 条件付き依存: `if ( this.context === "chrome" && element.id && selector.includes(`#${element.id}`) )` → `this.win.CustomizationHandler.isCustomizing()`
- 条件付き依存: `if ( this.context === "chrome" && element.id && selector.includes(`#${element.id}`) )` → `widget.areaType?.includes()`
- 参照: `element.id`, `panel_position.panel_position_string`, `this._HTMLArrowPositions`, `this.context`, `this.currentScreen.anchors`, `this.currentScreen?.anchors`, `this.location`

## FeatureCallout._isElementVisible()
- 位置: L807-818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.win.getComputedStyle()`, `this.win.isElementVisible()`
- 参照: `style?.display`, `style?.visibility`, `this.context`, `this.win.isElementVisible`

## FeatureCallout._resolveSelectorAndScope()
- 位置: L835-955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalizedSelector.includes()`, `scope.matches()`, `scope.querySelector()`, `this._isElementVisible()`
- 条件付き依存: `if (this.browser && normalizedSelector.includes("%triggerTab%"))` → `this.browser.documentGlobal.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (!triggerTab)` → `lazy.log.debug()`
- 条件付き依存: `if (this.browser && normalizedSelector.includes("%triggerTab%"))` → `normalizedSelector.replace()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `this.doc.getElementById()`
- 条件付き依存: `if (!toolbar || toolbar.collapsed || !scrollbox || (!url && !label))` → `lazy.log.debug()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `normalizedSelector.split()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `preTokenSelector.trim()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `this.doc.querySelector()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `rootScope.querySelectorAll()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `bookmarkItems.find()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `[this.browser.contentTitle, url].includes()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `el.getAttribute()`
- 条件付き依存: `if (!match)` → `lazy.log.debug()`
- 条件付き依存: `if (normalizedSelector.includes("%triggeredTabBookmark%"))` → `this._isElementVisible()`
- 条件付き依存: `if (!this._isElementVisible(match))` → `lazy.log.debug()`
- 条件付き依存: `if ( normalizedSelector.includes("::%shadow%") || normalizedSelector.includes("::%document%") )` → `normalizedSelector.split()`
- 条件付き依存: `if ( normalizedSelector.includes("::%shadow%") || normalizedSelector.includes("::%document%") )` → `parts[i].trim()`
- 条件付き依存: `if ( normalizedSelector.includes("::%shadow%") || normalizedSelector.includes("::%document%") )` → `scope.querySelector()`
- 条件付き依存: `if (!element || !this._isElementVisible(element))` → `lazy.log.debug()`
- 参照: `el._placesNode`, `el._placesNode?.title`, `el._placesNode?.uri`, `el.contentDocument`, `el.shadowRoot`, `parts.length`, `tab?.label`, `this._cachedHistoryTitle?.title`, `this.browser`, `this.browser.contentTitle`, `this.browser?.currentURI?.spec`, `this.browser?.documentGlobal?.gBrowser`, `this.doc`, `this.doc.documentElement`, `this.location`, `toolbar.collapsed`

## FeatureCallout._convertPopupAttachmentPoint()
- 位置: L958-988
- 役割: (未記入)
- 触るとき: (未記入)

## FeatureCallout._getPanelPositionString()
- 位置: L999-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._convertPopupAttachmentPoint()`

## FeatureCallout._setPanelMethods()
- 位置: L1016-1077
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `panel.setArrowPosition`

## setArrowPosition()
- 位置: L1019-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alignmentPosition?.match()`, `popupAlignment?.includes()`, `this.documentGlobal.getComputedStyle()`, `this.getAttribute()`, `this.hasAttribute()`, `this.setAttribute()`
- 条件付き依存: `if (alignmentOffset)` → `this.setAttribute()`
- 条件付き依存: `if (!(alignmentOffset))` → `this.removeAttribute()`
- 参照: `this.documentGlobal.getComputedStyle(this).direction`

## FeatureCallout._createContainer()
- 位置: L1079-1200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["none", "both", "slide"].includes()`, `this._getAnchor()`
- 条件付き依存: `if (needsPanel ^ (this._container?.localName === "panel"))` → `this._container.remove()`
- 条件付き依存: `if (needsPanel)` → `this.win.MozXULElement.parseXULToFragment()`
- 条件付き依存: `if (needsPanel)` → `this._setPanelMethods()`
- 条件付き依存: `if (!(needsPanel))` → `this.doc.createElement()`
- 条件付き依存: `if (!(needsPanel))` → `this._container?.classList.add()`
- 条件付き依存: `if (!this._container?.parentElement)` → `this._container.classList.add()`
- 条件付き依存: `if (hide_arrow)` → `this._container.setAttribute()`
- 条件付き依存: `if (!(hide_arrow))` → `this._container.removeAttribute()`
- 条件付き依存: `if (!this._container?.parentElement)` → `this._container.toggleAttribute()`
- 条件付き依存: `if (!this._container?.parentElement)` → `this._container.setAttribute()`
- 条件付き依存: `if (arrow_width)` → `this._container.style.setProperty()`
- 条件付き依存: `if (!(arrow_width))` → `this._container.style.removeProperty()`
- 条件付き依存: `if (arrow_corner_distance)` → `this._container.style.setProperty()`
- 条件付き依存: `if (!(arrow_corner_distance))` → `this._container.style.removeProperty()`
- 条件付き依存: `if (padding)` → `CSS.supports()`
- 条件付き依存: `if (CSS.supports("padding", padding))` → `this._container.style.setProperty()`
- 条件付き依存: `if (!(CSS.supports("padding", padding)))` → `CSS.supports()`
- 条件付き依存: `if (CSS.supports("padding", cssValue))` → `this._container.style.setProperty()`
- 条件付き依存: `if (!(CSS.supports("padding", cssValue)))` → `this._container.style.removeProperty()`
- 条件付き依存: `if (!(padding))` → `this._container.style.removeProperty()`
- 条件付き依存: `if (!this._container?.parentElement)` → `this.doc.createElement()`
- 条件付き依存: `if (!this._container?.parentElement)` → `contentBox.classList.add()`
- 条件付き依存: `if (!this._container?.parentElement)` → `this._applyTheme()`
- 条件付き依存: `if (needsPanel && this.win.isChromeWindow)` → `this.doc.getElementById("mainPopupSet").appendChild()`
- 条件付き依存: `if (needsPanel && this.win.isChromeWindow)` → `this.doc.getElementById()`
- 条件付き依存: `if (!(needsPanel && this.win.isChromeWindow))` → `this.doc.body.prepend()`
- 条件付き依存: `if (!this._container?.parentElement)` → `this._container.appendChild()`
- 条件付き依存: `if (!this._container?.parentElement)` → `makeArrow()`
- 参照: `contentBox.dataset.page`, `contentBox.id`, `fragment.firstElementChild`, `panel_position?.flip`, `panel_position?.panel_position_string`, `this._container`, `this._container.id`, `this._container?.localName`, `this._container?.parentElement`, `this.currentScreen.content`, `this.location`, `this.win`, `this.win.isChromeWindow`

## makeArrow()
- 位置: L1187-1194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `arrow.classList.add()`, `arrowRotationBox.appendChild()`, `arrowRotationBox.classList.add()`, `this.doc.createElement()`

## FeatureCallout._positionCallout()
- 位置: L1217-1652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `choosePosition()`, `clearPosition()`, `container.classList.remove()`, `container.getBoundingClientRect()`, `this._getAnchor()`
- 条件付き依存: `if (!container || !anchor)` → `this.endTour()`
- 条件付き依存: `if (customPosition)` → `overridePosition()`
- 条件付き依存: `if (finalPosition)` → `positioners[finalPosition].position()`
- 条件付き依存: `if (finalPosition)` → `setArrowPosition()`
- 参照: `anchor.absolute_position`, `anchor.arrow_position`, `anchor.arrow_width`, `anchor.element`, `container.getBoundingClientRect().height`, `container.getBoundingClientRect().width`, `this._container`, `this.doc.dir`

## getOffset()
- 位置: L1235-1243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.getBoundingClientRect()`
- 参照: `rect.bottom`, `rect.left`, `rect.right`, `rect.top`, `this.win.scrollX`, `this.win.scrollY`

## centerVertically()
- 位置: L1245-1251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.getBoundingClientRect()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `container.getBoundingClientRect().height`, `container.style.top`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## alignHorizontally()
- 位置: L1269-1318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `container.getBoundingClientRect()`, `getOffset()`, `parentEl.getBoundingClientRect()`, `position.endsWith()`
- 参照: `container.getBoundingClientRect().width`, `container.style`, `container.style.left`, `doc.documentElement.clientWidth`, `getOffset(parentEl).left`, `getOffset(parentEl).right`, `parentEl.getBoundingClientRect().left`, `parentEl.getBoundingClientRect().width`, `parentRect.left`, `parentRect.width`

## FeatureCallout.availableSpace()
- 位置: L1330-1336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `doc.documentElement.clientHeight`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.position()
- 位置: L1338-1346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `alignHorizontally()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `container.style.top`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.availableSpace()
- 位置: L1349-1351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`
- 参照: `getOffset(parentEl).top`

## FeatureCallout.position()
- 位置: L1353-1361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `alignHorizontally()`, `container.getBoundingClientRect()`, `getOffset()`
- 参照: `container.getBoundingClientRect().height`, `container.style.top`, `getOffset(parentEl).top`

## FeatureCallout.availableSpace()
- 位置: L1364-1366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`
- 参照: `getOffset(parentEl).left`

## FeatureCallout.position()
- 位置: L1368-1383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `container.getBoundingClientRect()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 条件付き依存: `if ( container.getBoundingClientRect().height <= parentEl.getBoundingClientRect().height )` → `getOffset()`
- 条件付き依存: `if (!( container.getBoundingClientRect().height <= parentEl.getBoundingClientRect().height ))` → `centerVertically()`
- 参照: `container.getBoundingClientRect().height`, `container.getBoundingClientRect().width`, `container.style.left`, `container.style.top`, `getOffset(parentEl).left`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.availableSpace()
- 位置: L1386-1388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`
- 参照: `doc.documentElement.clientWidth`, `getOffset(parentEl).right`

## FeatureCallout.position()
- 位置: L1390-1405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `container.getBoundingClientRect()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 条件付き依存: `if ( container.getBoundingClientRect().height <= parentEl.getBoundingClientRect().height )` → `getOffset()`
- 条件付き依存: `if (!( container.getBoundingClientRect().height <= parentEl.getBoundingClientRect().height ))` → `centerVertically()`
- 参照: `container.getBoundingClientRect().height`, `container.style.left`, `container.style.top`, `getOffset(parentEl).left`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`, `parentEl.getBoundingClientRect().width`

## FeatureCallout.availableSpace()
- 位置: L1408-1414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `doc.documentElement.clientHeight`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.position()
- 位置: L1416-1424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `alignHorizontally()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `container.style.top`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.availableSpace()
- 位置: L1427-1433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `doc.documentElement.clientHeight`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.position()
- 位置: L1435-1443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `alignHorizontally()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `container.style.top`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.availableSpace()
- 位置: L1446-1452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `doc.documentElement.clientHeight`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.position()
- 位置: L1454-1462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `alignHorizontally()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `container.style.top`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.availableSpace()
- 位置: L1465-1471
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `doc.documentElement.clientHeight`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## FeatureCallout.position()
- 位置: L1473-1481
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `alignHorizontally()`, `getOffset()`, `parentEl.getBoundingClientRect()`
- 参照: `container.style.top`, `getOffset(parentEl).top`, `parentEl.getBoundingClientRect().height`

## clearPosition()
- 位置: L1485-1490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(positioners).forEach()`, `container.removeAttribute()`
- 参照: `container.style`

## setArrowPosition()
- 位置: L1492-1519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.setAttribute()`

## addValueToPixelValue()
- 位置: L1521-1523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`

## subtractPixelValueFromValue()
- 位置: L1525-1527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseFloat()`

## overridePosition()
- 位置: L1529-1591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.prototype.hasOwnProperty.call()`
- 参照: `positioners[position].position`

## positioners[position].position()
- 位置: L1547-1589
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (customPosition.top)` → `addValueToPixelValue()`
- 条件付き依存: `if (customPosition.top)` → `parentEl.getBoundingClientRect()`
- 条件付き依存: `if (customPosition.left)` → `addValueToPixelValue()`
- 条件付き依存: `if (customPosition.left)` → `parentEl.getBoundingClientRect()`
- 条件付き依存: `if (customPosition.right)` → `subtractPixelValueFromValue()`
- 条件付き依存: `if (customPosition.right)` → `parentEl.getBoundingClientRect()`
- 条件付き依存: `if (customPosition.right)` → `container.getBoundingClientRect()`
- 条件付き依存: `if (customPosition.bottom)` → `subtractPixelValueFromValue()`
- 条件付き依存: `if (customPosition.bottom)` → `parentEl.getBoundingClientRect()`
- 条件付き依存: `if (customPosition.bottom)` → `container.getBoundingClientRect()`
- 参照: `container.getBoundingClientRect().height`, `container.getBoundingClientRect().width`, `container.style.left`, `container.style.right`, `container.style.top`, `customPosition.bottom`, `customPosition.left`, `customPosition.right`, `customPosition.top`, `parentEl.getBoundingClientRect().bottom`, `parentEl.getBoundingClientRect().left`, `parentEl.getBoundingClientRect().right`, `parentEl.getBoundingClientRect().top`

## calloutFits()
- 位置: L1593-1604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `position.split()`, `positioners[edgePosition].availableSpace()`
- 参照: `positioners[edgePosition].neededSpace`

## choosePosition()
- 位置: L1606-1637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["start", "end"].includes()`, `["top", "bottom", "left", "right"] .filter()`, `["top", "bottom", "left", "right"] .filter(p => p !== position) .filter()`, `["top", "bottom", "left", "right"] .filter(p => p !== position) .filter(calloutFits) .sort()`, `calloutFits()`, `positioners[a].availableSpace()`, `positioners[b].availableSpace()`, `this._HTMLArrowPositions.includes()`
- 参照: `positioners[a].neededSpace`, `positioners[b].neededSpace`

## FeatureCallout._setupWindowFunctions()
- 位置: L1655-1700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `getActionHandler()`, `lazy.AboutWelcomeParent.prototype.onContentMessage.bind()`
- 参照: `this.AWSetup`, `this._windowFuncs`, `this.win`

## getActionHandler()
- 位置: L1662-1663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleActorMessage()`
- 参照: `this.browser`

## AWSendEventTelemetry()
- 位置: L1665-1676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `telemetryMessageHandler()`
- 参照: `data.event_context`, `data.event_context.write_in_microsurvey`, `this.config?.metrics`, `this.config?.write_in_microsurvey`

## AWGetFeatureConfig()
- 位置: L1678-1678
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.config`

## AWSendToParent()
- 位置: L1687-1687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActionHandler()`, `getActionHandler(name)()`

## AWFinish()
- 位置: L1688-1688
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.endTour()`

## AWAdvanceScreens()
- 位置: L1689-1689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._advanceScreens()`

## FeatureCallout._clearWindowFunctions()
- 位置: L1703-1711
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.AWSetup)` → `Object.keys()`
- 参照: `this.AWSetup`, `this._windowFuncs`, `this.win`

## FeatureCallout._emitEvent()
- 位置: L1719-1721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.listener()`
- 参照: `this.win`

## FeatureCallout.endTour()
- 位置: L1723-1785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearWindowFunctions()`, `this._container?.classList.toggle()`, `this._container?.removeEventListener()`, `this._pageEventManager?.clear()`, `this._pageEventManager?.emit()`, `this.teardownFeatureTourProgress()`, `this.win.removeEventListener()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.addEventListener()`
- 条件付き依存: `if (event.target === this._container)` → `controller.abort()`
- 条件付き依存: `if (event.target === this._container)` → `onFadeOut()`
- 条件付き依存: `if (this._container?.localName === "panel")` → `this._container.hidePopup()`
- 条件付き依存: `if (this._container)` → `this.win.setTimeout()`
- 条件付き依存: `if (!(this._container))` → `onFadeOut()`
- 参照: `controller.signal`, `event.target`, `this._container`, `this._container?.localName`, `this.content`, `this.currentScreen`, `this.message`, `this.pref`, `this.ready`

## onFadeOut()
- 位置: L1751-1766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._container?.remove()`, `this._emitEvent()`, `this._removePanelConflictListeners()`, `this._removePositionListeners()`, `this.doc.querySelector()`, `this.doc.querySelector(`[src="${BUNDLE_SRC}"]`)?.remove()`, `this.renderObserver?.disconnect()`
- 条件付き依存: `if (this.savedFocus)` → `this.savedFocus.element.focus()`
- 参照: `this.savedFocus`, `this.savedFocus.focusVisible`

## FeatureCallout._dismiss()
- 位置: L1787-1798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.endTour()`
- 条件付き依存: `if (action?.type)` → `this.win.AWSendToParent()`
- 参照: `action.dismiss`, `action?.type`, `this.currentScreen?.content.dismiss_action`, `this.currentScreen?.content.dismiss_button?.action`

## FeatureCallout._addScriptsAndRender()
- 位置: async L1800-1833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doc.createElement()`, `this.doc.head.appendChild()`, `this.doc.querySelector()`, `this.doc.querySelector(`[src="${BUNDLE_SRC}"]`)?.remove()`
- 条件付き依存: `if (!this.doc.querySelector(`[src="${reactSrc}"]`))` → `getReactReady()`
- 条件付き依存: `if (!this.doc.querySelector(`[src="${domSrc}"]`))` → `getDomReady()`
- 参照: `bundleScript.src`

## getReactReady()
- 位置: L1804-1811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reactScript.addEventListener()`, `this.doc.createElement()`, `this.doc.head.appendChild()`
- 参照: `reactScript.src`

## getDomReady()
- 位置: L1813-1820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `domScript.addEventListener()`, `this.doc.createElement()`, `this.doc.head.appendChild()`
- 参照: `domScript.src`

## FeatureCallout._observeRender()
- 位置: L1835-1837
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderObserver?.observe()`

## FeatureCallout._updateConfig()
- 位置: async L1849-1914
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`, `structuredClone()`, `this._loadConfig()`
- 条件付き依存: `if (!this.config.screens)` → `lazy.log.error()`
- 条件付き依存: `if (!this.config.screens)` → `JSON.stringify()`
- 条件付き依存: `if ( !overrideScreen && this.config?.tour_pref_name && this.config.tour_pref_name === this.pref?.name && this.featureTourProgress )` → `this.config.screens.findIndex()`
- 参照: `newScreen?.id`, `screen.id`, `this.config`, `this.config.screens`, `this.config.startScreen`, `this.config.tour_pref_name`, `this.config?.screens`, `this.config?.startScreen`, `this.config?.tour_pref_name`, `this.currentScreen`, `this.currentScreen?.id`, `this.featureTourProgress`, `this.featureTourProgress.screen`, `this.loadingConfig`, `this.location`, `this.message`, `this.message.content`, `this.message.template`, `this.pref?.name`

## FeatureCallout._loadConfig()
- 位置: async L1922-1933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ASRouter.sendTriggerMessage()`
- 参照: `lazy.ASRouter.waitForInitialized`, `result.message`, `this.browser`, `this.loadingConfig`, `this.location`

## FeatureCallout._renderCallout()
- 位置: async L1940-1954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._addCalloutLinkElements()`, `this._createContainer()`, `this._setupWindowFunctions()`
- 条件付き依存: `if (container)` → `this._addScriptsAndRender()`
- 条件付き依存: `if (container)` → `this._observeRender()`
- 条件付き依存: `if (container)` → `container.querySelector()`
- 条件付き依存: `if (container.localName === "div")` → `this._addPositionListeners()`
- 参照: `container.localName`

## FeatureCallout._attachPageEventListeners()
- 位置: L1991-2003
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listeners?.forEach()`, `this._handlePageEventAction()`, `this._loadPageEventManager[params.options?.once ? "once" : "on"]()`
- 条件付き依存: `if (params.options?.preventDefault)` → `event.preventDefault()`
- 参照: `params.options?.once`, `params.options?.preventDefault`, `this._loadPageEventManager`

## FeatureCallout._handlePageEventAction()
- 位置: async L2011-2070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shouldDoBehavior()`, `this._getUniqueElementIdentifier()`, `this.config?.id.toUpperCase()`
- 条件付き依存: `if (action.type)` → `this.win.AWSendEventTelemetry()`
- 条件付き依存: `if (action.type)` → `event.type?.toUpperCase()`
- 条件付き依存: `if (action.type)` → `this.win.AWSendToParent()`
- 条件付き依存: `if (action.advance_screens)` → `shouldDoBehavior()`
- 条件付き依存: `if (shouldDoBehavior(action.advance_screens.behavior ?? true))` → `this._advanceScreens()`
- 条件付き依存: `if (shouldDoBehavior(action.dismiss))` → `this.win.AWSendEventTelemetry()`
- 条件付き依存: `if (shouldDoBehavior(action.dismiss))` → `this._dismiss()`
- 条件付き依存: `if (shouldDoBehavior(action.reposition))` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (shouldDoBehavior(action.reposition))` → `this._positionCallout()`
- 参照: `action.advance_screens`, `action.advance_screens.behavior`, `action.dismiss`, `action.needsAwait`, `action.reposition`, `action.type`, `event.target`, `this.location`

## shouldDoBehavior()
- 位置: L2039-2052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `lazy.log.warn()`
- 参照: `action.needsAwait`, `this.location`

## FeatureCallout._getUniqueElementIdentifier()
- 位置: L2078-2111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Element.isInstance()`
- 条件付き依存: `if (target.className)` → `[...target.classList].join()`
- 条件付き依存: `if (target.attributes.length)` → `[...target.attributes] .filter(attr => ["is", "role", "open"].includes(attr.name)) .map()`
- 条件付き依存: `if (target.attributes.length)` → `[...target.attributes] .filter()`
- 条件付き依存: `if (target.attributes.length)` → `["is", "role", "open"].includes()`
- 条件付き依存: `if (Element.isInstance(target))` → `doc.querySelectorAll()`
- 条件付き依存: `if (doc.querySelectorAll(source).length > 1)` → `target.closest()`
- 条件付き依存: `if (uniqueAncestor)` → `this._getUniqueElementIdentifier()`
- 条件付き依存: `if (doc !== this.doc)` → `[ ...Services.wm.getEnumerator("navigator:browser"), ].indexOf()`
- 条件付き依存: `if (doc !== this.doc)` → `Services.wm.getEnumerator()`
- 参照: `attr.name`, `attr.value`, `doc.querySelectorAll(source).length`, `target.attributes`, `target.attributes.length`, `target.classList`, `target.className`, `target.documentGlobal`, `target.id`, `target.localName`, `target.ownerDocument`, `this.doc`
- XPCOM: `Services.wm`

## FeatureCallout.getAutoFocusElement()
- 位置: L2124-2152
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (selector)` → `this._container.querySelector()`
- 条件付き依存: `if (use_defaults)` → `this._container.querySelector()`
- 参照: `this._container`

## FeatureCallout.showFeatureCallout()
- 位置: async L2161-2246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._container?.remove()`, `this._pageEventManager?.clear()`, `this._renderCallout()`, `this._updateConfig()`, `this.renderObserver?.disconnect()`
- 条件付き依存: `if (!this.renderObserver)` → `this._container.querySelector()`
- 条件付き依存: `if (!this.ready && this._container.querySelector(".screen"))` → `this._getAnchor()`
- 条件付き依存: `if ( this._container.localName === "div" && this.doc.activeElement && !this.savedFocus )` → `element.matches()`
- 条件付き依存: `if (this._container.localName === "div")` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (!anchor?.panel_position)` → `this.endTour()`
- 条件付き依存: `if (this._container.localName === "panel")` → `this._container.addEventListener()`
- 条件付き依存: `if (this._container.localName === "panel")` → `this._addPanelConflictListeners()`
- 条件付き依存: `if (this._container.localName === "panel")` → `this._container.openPopup()`
- 条件付き依存: `if (!rendering)` → `this.endTour()`
- 条件付き依存: `if (this.message.template)` → `lazy.ASRouter.addImpression()`
- 参照: `anchor.element`, `anchor.panel_position`, `anchor?.panel_position`, `this._container.localName`, `this.config?.screens?.length`, `this.currentScreen`, `this.doc.activeElement`, `this.message`, `this.message.template`, `this.ready`, `this.renderObserver`, `this.savedFocus`, `this.win.MutationObserver`

## onRender()
- 位置: L2173-2192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._attachPageEventListeners()`, `this._pageEventManager?.clear()`, `this.win.addEventListener()`
- 条件付き依存: `if (anchor?.autofocus)` → `this.getAutoFocusElement(anchor.autofocus)?.focus()`
- 条件付き依存: `if (anchor?.autofocus)` → `this.getAutoFocusElement()`
- 条件付き依存: `if (this._container.localName === "div")` → `this.win.addEventListener()`
- 条件付き依存: `if (this._container.localName === "div")` → `this._positionCallout()`
- 条件付き依存: `if (!(this._container.localName === "div"))` → `this._container.classList.remove()`
- 参照: `anchor.autofocus`, `anchor?.autofocus`, `this._container.localName`, `this.currentScreen?.content?.page_event_listeners`, `this.ready`

## FeatureCallout._initTheme()
- 位置: L2278-2285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `FeatureCallout.themePresets`, `theme.preset`, `this.theme`

## FeatureCallout._applyTheme()
- 位置: L2293-2322
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._container)` → `this._container.classList.toggle()`
- 条件付き依存: `if (this._container)` → `this._setThemeVariable()`
- 参照: `FeatureCallout.themePropNames`, `this._container`, `this.theme`, `this.theme.all`, `this.theme.lwtNewtab`, `this.theme.preset`, `this.theme.simulateContent`

## FeatureCallout._setThemeVariable()
- 位置: L2330-2336
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value)` → `this._container.style.setProperty()`
- 条件付き依存: `if (!(value))` → `this._container.style.removeProperty()`
