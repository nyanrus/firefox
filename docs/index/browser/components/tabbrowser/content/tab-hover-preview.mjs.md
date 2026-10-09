# browser/components/tabbrowser/content/tab-hover-preview.mjs

source: browser/components/tabbrowser/content/tab-hover-preview.mjs
source-hash: da8702a6d9b763f337edfa7ab9a981876545ca97
lines: 1337

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`

## TabHoverPanelSet.constructor()
- 位置: L51-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `event.target.closest()`, `lazy.Tabbrowser.isTab()`, `lazy.Tabbrowser.isTabGroupLabel()`, `this.#setExternalPopupListeners()`, `this.#win.document.getElementById()`, `this.#win.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if ( target && (lazy.Tabbrowser.isTab(target) || lazy.Tabbrowser.isTabGroupLabel(target)) )` → `this.deactivate()`

## TabHoverPanelSet.activate()
- 位置: L110-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Tabbrowser.isTab()`, `this.shouldActivate()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup))` → `this.#setActivePanel()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup))` → `this.tabPanel.activate()`
- 条件付き依存: `if (!(lazy.Tabbrowser.isTab(tabOrGroup)))` → `lazy.Tabbrowser.isTabGroup()`
- 条件付き依存: `if (lazy.Tabbrowser.isTabGroup(tabOrGroup))` → `this.#setActivePanel()`
- 条件付き依存: `if (lazy.Tabbrowser.isTabGroup(tabOrGroup))` → `this.tabGroupPanel.activate()`

## TabHoverPanelSet.deactivate()
- 位置: L147-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Tabbrowser.isTab()`, `lazy.Tabbrowser.isTabGroup()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup) || !tabOrGroup)` → `this.tabPanel.deactivate()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup) || !tabOrGroup)` → `this.tabNotePanel.deactivate()`
- 条件付き依存: `if (lazy.Tabbrowser.isTabGroup(tabOrGroup) || !tabOrGroup)` → `this.tabGroupPanel.deactivate()`

## TabHoverPanelSet.activateNotePanel()
- 位置: L162-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setActivePanel()`, `this.shouldActivate()`, `this.tabNotePanel.activate()`

## TabHoverPanelSet.deactivateNotePanel()
- 位置: L170-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabNotePanel.deactivate()`

## TabHoverPanelSet.#setActivePanel()
- 位置: L177-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearDeactivateTimer()`
- 条件付き依存: `if (this.#activePanel && this.#activePanel != panel)` → `this.requestDeactivate()`

## TabHoverPanelSet.requestDeactivate()
- 位置: L186-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.hoverTargets?.some()`, `t.matches()`, `this.#clearDeactivateTimer()`, `this.#deactivateTimers.delete()`, `this.#deactivateTimers.set()`, `this.#doDeactivate()`, `this.#win.setTimeout()`
- 条件付き依存: `if (force)` → `this.#doDeactivate()`

## TabHoverPanelSet.#clearDeactivateTimer()
- 位置: L203-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deactivateTimers.get()`
- 条件付き依存: `if (timer)` → `this.#win.clearTimeout()`
- 条件付き依存: `if (timer)` → `this.#deactivateTimers.delete()`

## TabHoverPanelSet.#doDeactivate()
- 位置: L211-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.onBeforeHide()`, `panel.panelElement.hidePopup()`, `this.panelOpener.clear()`, `this.panelOpener.setZeroDelay()`
- 条件付き依存: `if (panel.panelElement.state == "showing")` → `panel.panelElement.addEventListener()`
- 条件付き依存: `if (this.#activePanel != panel)` → `this.#doDeactivate()`

## TabHoverPanelSet.forceReset()
- 位置: L241-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.onBeforeHide()`, `panel.panelElement.hidePopup()`, `this.#clearDeactivateTimer()`, `this.panelOpener.reset()`

## TabHoverPanelSet.isHoverPanel()
- 位置: L260-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[this.tabPanel, this.tabGroupPanel, this.tabNotePanel].some()`

## TabHoverPanelSet.shouldActivate()
- 位置: L266-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#win.gBrowser.tabContainer.hasAttribute()`
- XPCOM: `Services.focus`

## TabHoverPanelSet.#setExternalPopupListeners()
- 位置: L283-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleExternalPopupEvent()`, `this.#win.document.querySelectorAll()`

## handleExternalPopupEvent()
- 位置: L295-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#win.addEventListener()`
- 条件付き依存: `if ( target !== this.tabPanel.panelElement && target !== this.tabGroupPanel.panelElement && target !== this.tabNotePanel.panelElement && (target.nodeName == "pan...)` → `this.#openPopups[setMethod]()`

## HoverPanel.constructor()
- 位置: L318-322
- 役割: (未記入)
- 触るとき: (未記入)

## HoverPanel.isActive()
- 位置: L324-326
- 役割: (未記入)
- 触るとき: (未記入)

## HoverPanel.deactivate()
- 位置: L328-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelSet.requestDeactivate()`

## HoverPanel.hoverTargets()
- 位置: L332-334
- 役割: (未記入)
- 触るとき: (未記入)

## HoverPanel.onBeforeHide()
- 位置: L336-336
- 役割: (未記入)
- 触るとき: (未記入)

## TabPanel.constructor()
- 位置: L352-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`, `this.#addNoteButton.addEventListener()`, `this.#openTabNotePanel()`, `this.panelElement.querySelector()`, `this.win.document.getElementById()`, `this.win.document.importNode()`

## TabPanel.handleEvent()
- 位置: async L399-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePreview()`, `this.deactivate()`, `this.mouseoutTarget.contains()`, `this.mouseoutTarget?.addEventListener()`
- 条件付き依存: `if ( this.mouseoutTarget && !this.mouseoutTarget.contains(e.relatedTarget) )` → `this.deactivate()`

## TabPanel.activate()
- 位置: L424-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalTab?.removeEventListener()`, `this.#maybeRequestThumbnail()`, `this.#movePanel()`, `this.#tab.addEventListener()`
- 条件付き依存: `if ( this.panelElement.state == "open" || this.panelElement.state == "showing" )` → `this.panelElement.removeEventListener()`
- 条件付き依存: `if ( this.panelElement.state == "open" || this.panelElement.state == "showing" )` → `this.#updatePreview()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.panelOpener.execute()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.shouldActivate()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.openPopup()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.win.addEventListener()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.addEventListener()`

## TabPanel.deactivate()
- 位置: L471-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.deactivate()`
- 条件付き依存: `if (leavingTab)` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (this.#tab == leavingTab)` → `this.deactivate()`

## TabPanel.onBeforeHide()
- 位置: L489-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tab?.removeEventListener()`, `this.mouseoutTarget?.removeEventListener()`, `this.panelElement.removeEventListener()`, `this.win.removeEventListener()`

## TabPanel.hoverTargets()
- 位置: L498-507
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#interactiveArea.childNodes.length)` → `targets.push()`
- 条件付き依存: `if (this.#tab)` → `targets.push()`

## TabPanel.mouseoutTarget()
- 位置: L514-518
- 役割: (未記入)
- 触るとき: (未記入)

## TabPanel.getPrettyURI()
- 位置: L520-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `url.hostname.replace()`
- 条件付き依存: `if (url.protocol == "about:" && url.pathname == "reader")` → `URL.parse()`
- 条件付き依存: `if (url.protocol == "about:" && url.pathname == "reader")` → `url.searchParams.get()`

## TabPanel.#hasValidWireframeState()
- 位置: L536-544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PageWireframes.getWireframeState()`

## TabPanel.#hasValidThumbnailState()
- 位置: L546-554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.getAttribute()`

## TabPanel.#maybeRequestThumbnail()
- 位置: L556-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.#hasValidThumbnailState()`, `this.win.PageThumbs.captureTabPreviewThumbnail()`, `this.win.PageThumbs.captureTabPreviewThumbnail( tab.linkedBrowser, thumbnailCanvas ) .then()`, `this.win.document.createElement()`
- 条件付き依存: `if (!this.#hasValidThumbnailState(tab))` → `lazy.PageWireframes.getWireframeElementForTab()`
- 条件付き依存: `if (wireframeElement)` → `this.#updatePreview()`
- 条件付き依存: `if (captured && this.#tab == tab && this.#hasValidThumbnailState(tab))` → `this.#updatePreview()`

## TabPanel.#displayTitle()
- 位置: L588-593
- 役割: (未記入)
- 触るとき: (未記入)

## TabPanel.#displayURI()
- 位置: L595-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPrettyURI()`

## TabPanel.#displayPids()
- 位置: L602-610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pids.join()`, `this.win.gBrowser.getTabPids()`

## TabPanel.#displayActiveness()
- 位置: L612-614
- 役割: (未記入)
- 触るとき: (未記入)

## TabPanel.#displaySponsorProtection()
- 位置: L616-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SponsorProtection.isProtectedBrowser()`

## TabPanel.#updateContainerIndicator()
- 位置: L623-655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `className.startsWith()`, `indicator.querySelector()`, `lazy.ContextualIdentityService.getPublicIdentityFromId()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `this.panelElement.querySelector()`
- 条件付き依存: `if ( className.startsWith("identity-color-") || className.startsWith("identity-icon-") )` → `indicator.classList.remove()`
- 条件付き依存: `if (identity.color)` → `indicator.classList.add()`
- 条件付き依存: `if (identity.icon)` → `indicator.classList.add()`

## TabPanel.#openTabNotePanel()
- 位置: L662-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.deactivate()`, `this.win.gBrowser.tabNoteMenu.openPanel()`
- XPCOM: `Services.prefs`

## TabPanel.#updatePreview()
- 位置: async L670-740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabNotes.isEligible()`, `this.#hasValidThumbnailState()`, `this.#hasValidWireframeState()`, `this.#movePanel()`, `this.#updateContainerIndicator()`, `this.panelElement.dispatchEvent()`, `this.panelElement.querySelector()`, `thumbnailContainer.classList.toggle()`
- 条件付き依存: `if (lazy.Tabbrowser.prefs.showPidAndActiveness)` → `this.panelElement.querySelector()`
- 条件付き依存: `if (!(lazy.Tabbrowser.prefs.showPidAndActiveness))` → `this.panelElement.querySelector()`
- 条件付き依存: `if (this._prefUseTabNotes && lazy.TabNotes.isEligible(this.#tab))` → `lazy.TabNotes.get()`
- 条件付き依存: `if (note)` → `this.#addNoteButton.remove()`
- 条件付き依存: `if (!(note))` → `this.#interactiveArea.append()`
- 条件付き依存: `if (!(note))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(note))` → `this.#addNoteButton .querySelector("moz-badge") .toggleAttribute()`
- 条件付き依存: `if (!(note))` → `this.#addNoteButton .querySelector()`
- 条件付き依存: `if (!(this._prefUseTabNotes && lazy.TabNotes.isEligible(this.#tab)))` → `this.#addNoteButton.remove()`
- 条件付き依存: `if (thumbnailContainer.firstChild != this.#thumbnailElement)` → `thumbnailContainer.replaceChildren()`
- 条件付き依存: `if (this.#thumbnailElement)` → `thumbnailContainer.appendChild()`
- 条件付き依存: `if (thumbnailContainer.firstChild != this.#thumbnailElement)` → `this.panelElement.dispatchEvent()`
- XPCOM: `Services.prefs`

## TabPanel.#movePanel()
- 位置: L742-751
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#tab)` → `this.panelElement.moveToAnchor()`

## TabPanel.popupOptions()
- 位置: L753-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabContainer.isContainerVerticalPinnedGrid()`

## TabGroupPanel.constructor()
- 位置: L801-806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.querySelector()`, `super()`

## TabGroupPanel.activate()
- 位置: L808-828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.groupInteractions.hover_preview.add()`, `this.#movePanel()`, `this.#updatePanelContent()`
- 条件付き依存: `if (this.#group && this.#group != group)` → `this.#removeGroupListeners()`
- 条件付き依存: `if (this.panelElement.state == "closed")` → `this.panelSet.panelOpener.execute()`
- 条件付き依存: `if (this.panelElement.state == "closed")` → `this.panelSet.shouldActivate()`
- 条件付き依存: `if (this.panelElement.state == "closed")` → `this.#doOpenPanel()`
- 条件付き依存: `if (!(this.panelElement.state == "closed"))` → `this.#addGroupListeners()`

## TabGroupPanel.focusPanel()
- 位置: L835-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelContent.children[childIndex].focus()`

## TabGroupPanel.#doOpenPanel()
- 位置: L840-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addGroupListeners()`, `this.panelElement.addEventListener()`, `this.panelElement.openPopup()`

## TabGroupPanel.#updatePanelContent()
- 位置: L849-880
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fragment.appendChild()`, `tabbutton.classList.add()`, `tabbutton.setAttribute()`, `this.panelContent.replaceChildren()`, `this.panelElement.dispatchEvent()`, `this.win.document.createDocumentFragment()`, `this.win.document.createXULElement()`
- 条件付き依存: `if (tab.linkedBrowser)` → `tabbutton.setAttribute()`
- 条件付き依存: `if (tab == this.win.gBrowser.selectedTab)` → `tabbutton.classList.add()`

## TabGroupPanel.handleEvent()
- 位置: L882-921
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.win.gBrowser.selectedTab == event.target.tab)` → `this.deactivate()`
- 条件付き依存: `if (event.type == "command")` → `switchingTabs.every()`
- 条件付き依存: `if (switchingTabs.every(tab => tab.group == this.#group))` → `this.win.addEventListener()`
- 条件付き依存: `if (switchingTabs.every(tab => tab.group == this.#group))` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (event.type == "command")` → `this.deactivate()`
- 条件付き依存: `if (!(event.type == "command"))` → `this.hoverTargets.every()`
- 条件付き依存: `if (!(event.type == "command"))` → `target.contains()`
- 条件付き依存: `if ( event.type == "mouseout" && this.hoverTargets.every(target => !target.contains(event.relatedTarget)) )` → `this.deactivate()`
- 条件付き依存: `if (!( event.type == "mouseout" && this.hoverTargets.every(target => !target.contains(event.relatedTarget)) ))` → `TabGroupPanel.PANEL_UPDATE_EVENTS.includes()`
- 条件付き依存: `if (TabGroupPanel.PANEL_UPDATE_EVENTS.includes(event.type))` → `this.#updatePanelContent()`

## TabGroupPanel.onBeforeHide()
- 位置: L923-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#removeGroupListeners()`, `this.panelElement.removeEventListener()`

## TabGroupPanel.hoverTargets()
- 位置: L930-936
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#popupTarget)` → `targets.push()`

## TabGroupPanel.popupOptions()
- 位置: L938-963
- 役割: (未記入)
- 触るとき: (未記入)

## TabGroupPanel.#popupTarget()
- 位置: L965-967
- 役割: (未記入)
- 触るとき: (未記入)

## TabGroupPanel.#addGroupListeners()
- 位置: L969-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#group.addEventListener()`

## TabGroupPanel.#removeGroupListeners()
- 位置: L979-987
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#group.removeEventListener()`

## TabGroupPanel.#movePanel()
- 位置: L989-999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelElement.moveToAnchor()`

## TabNotePanel.constructor()
- 位置: L1009-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionsContainer.appendChild()`, `editIcon.addEventListener()`, `editIcon.setAttribute()`, `super()`, `this.#openTabNotePanel()`, `this.panelElement .querySelector()`, `this.panelElement .querySelector(".tab-note-preview-expand") .addEventListener()`, `this.panelElement .querySelector(".tab-note-preview-text") .addEventListener()`, `this.panelElement.querySelector()`, `this.win.document.createElement()`

## TabNotePanel.handleEvent()
- 位置: L1037-1055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePanelContent()`, `this.deactivate()`, `this.panelElement.addEventListener()`, `this.panelElement.contains()`
- 条件付き依存: `if (!this.panelElement.contains(e.relatedTarget))` → `this.deactivate()`

## TabNotePanel.activate()
- 位置: L1057-1086
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalTab?.removeEventListener()`, `this.#movePanel()`, `this.#tab.addEventListener()`
- 条件付き依存: `if ( this.panelElement.state == "open" || this.panelElement.state == "showing" )` → `this.#updatePanelContent()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.panelOpener.execute()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.shouldActivate()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.openPopup()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.win.addEventListener()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.addEventListener()`

## TabNotePanel.deactivate()
- 位置: L1093-1106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.deactivate()`
- 条件付き依存: `if (leavingTab)` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (this.#tab == leavingTab)` → `this.deactivate()`

## TabNotePanel.onBeforeHide()
- 位置: L1108-1116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tab?.removeEventListener()`, `this.panelElement.removeEventListener()`, `this.panelSet.panelOpener.setZeroDelay()`, `this.win.removeEventListener()`

## TabNotePanel.#updatePanelContent()
- 位置: async L1118-1155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabNotes.get()`, `noteTextContainer.style.setProperty()`, `this.#movePanel()`, `this.panelElement.dispatchEvent()`, `this.panelElement.querySelector()`

## TabNotePanel.#movePanel()
- 位置: L1157-1166
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#anchorElement)` → `this.panelElement.moveToAnchor()`

## TabNotePanel.#noteExpanded()
- 位置: L1168-1175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelElement.toggleAttribute()`
- 条件付き依存: `if (val && this.#tab)` → `this.#tab.dispatchEvent()`

## TabNotePanel.#noteOverflow()
- 位置: L1177-1179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelElement.toggleAttribute()`

## TabNotePanel.#openTabNotePanel()
- 位置: L1181-1186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.deactivate()`, `this.win.gBrowser.tabNoteMenu.openPanel()`

## TabNotePanel.popupOptions()
- 位置: L1188-1194
- 役割: (未記入)
- 触るとき: (未記入)

## TabPreviewPanelTimedFunction.constructor()
- 位置: L1220-1235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## TabPreviewPanelTimedFunction.execute()
- 位置: L1260-1278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#target()`, `this.#win.setTimeout()`

## TabPreviewPanelTimedFunction.clear()
- 位置: L1292-1298
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (from == this.#from && this.#timer)` → `this.#win.clearTimeout()`

## TabPreviewPanelTimedFunction.setZeroDelay()
- 位置: L1306-1314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#win.setTimeout()`
- 条件付き依存: `if (this.#useZeroDelay)` → `this.#win.clearTimeout()`

## TabPreviewPanelTimedFunction.delayActive()
- 位置: L1316-1318
- 役割: (未記入)
- 触るとき: (未記入)

## TabPreviewPanelTimedFunction.zeroDelayActive()
- 位置: L1320-1322
- 役割: (未記入)
- 触るとき: (未記入)

## TabPreviewPanelTimedFunction.reset()
- 位置: L1324-1335
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#timer)` → `this.#win.clearTimeout()`
- 条件付き依存: `if (this.#useZeroDelay)` → `this.#win.clearTimeout()`
