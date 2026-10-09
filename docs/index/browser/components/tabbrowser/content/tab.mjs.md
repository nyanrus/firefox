# browser/components/tabbrowser/content/tab.mjs

source: browser/components/tabbrowser/content/tab.mjs
source-hash: 81c6e5dd4047fc7d57b5938e797a014c71d07cf9
lines: 1107

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`, `customElements.define()`

## MozTabbrowserTab.constructor()
- 位置: L39-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.addEventListener()`

## MozTabbrowserTab.inheritedAttributes()
- 位置: L107-132
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.connectedCallback()
- 位置: L135-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateOnTabGrouped()`, `this.#updateOnTabSplit()`, `this.initialize()`

## MozTabbrowserTab.disconnectedCallback()
- 位置: L143-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateOnTabUngrouped()`, `this.#updateOnTabUnsplit()`

## MozTabbrowserTab.initialize()
- 位置: L148-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `labelContainer.addEventListener()`, `this.appendChild()`, `this.initializeAttributeInheritance()`, `this.querySelector()`, `this.setAttribute()`
- 条件付き依存: `if (!("_lastAccessed" in this))` → `this.updateLastAccessed()`

## MozTabbrowserTab.index()
- 位置: L179-181
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.elementIndex()
- 位置: L184-191
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.elementIndex()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.owner()
- 位置: L198-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#owner?.deref()`

## MozTabbrowserTab.owner()
- 位置: L206-208
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.container()
- 位置: L210-212
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.attention()
- 位置: L214-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser._tabAttrModified()`, `this.hasAttribute()`, `this.toggleAttribute()`

## MozTabbrowserTab._visuallySelected()
- 位置: L223-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser._tabAttrModified()`, `this.hasAttribute()`, `this.toggleAttribute()`

## MozTabbrowserTab._selected()
- 位置: L232-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTab.pinned()
- 位置: L245-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.isOpen()
- 位置: L249-251
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.visible()
- 位置: L253-259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.group.isTabVisibleInGroup()`

## MozTabbrowserTab.hidden()
- 位置: L261-264
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.muted()
- 位置: L266-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.multiselected()
- 位置: L270-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.userContextId()
- 位置: L274-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseInt()`, `this.getAttribute()`, `this.hasAttribute()`

## MozTabbrowserTab.permanentKey()
- 位置: L286-288
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.soundPlaying()
- 位置: L290-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.pictureinpicture()
- 位置: L294-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.activeMediaBlocked()
- 位置: L298-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.undiscardable()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.undiscardable()
- 位置: L306-313
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser._tabAttrModified()`, `this.hasAttribute()`, `this.toggleAttribute()`

## MozTabbrowserTab.animationsEnabled()
- 位置: L315-317
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.animationsEnabled()
- 位置: L319-321
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.isEmpty()
- 位置: L323-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.isEmptyIgnoringLoad()
- 位置: L335-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUIUtils.checkEmptyPageOrigin()`, `isBlankPageURL()`, `this.hasAttribute()`

## MozTabbrowserTab.lastAccessed()
- 位置: L356-358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## MozTabbrowserTab.lastSeenActive()
- 位置: L368-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (isForegroundWindow && this.selected)` → `Date.now()`

## MozTabbrowserTab._overPlayingIcon()
- 位置: L393-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.overlayIcon?.matches()`

## MozTabbrowserTab._overAudioButton()
- 位置: L397-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.audioButton?.matches()`

## MozTabbrowserTab.overlayIcon()
- 位置: L401-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.audioButton()
- 位置: L405-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.throbber()
- 位置: L409-411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.iconImage()
- 位置: L413-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.sharingIcon()
- 位置: L417-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.textLabel()
- 位置: L421-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.closeButton()
- 位置: L425-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.noteIcon()
- 位置: L429-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.noteIconOverlay()
- 位置: L433-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`

## MozTabbrowserTab.group()
- 位置: L438-442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.closest()`

## MozTabbrowserTab.splitview()
- 位置: L445-450
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTab.hasTabNote()
- 位置: L455-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MozTabbrowserTab.hasTabNote()
- 位置: L462-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozTabbrowserTab.updateLastAccessed()
- 位置: L466-468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## MozTabbrowserTab.updateLastSeenActive()
- 位置: L470-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`

## MozTabbrowserTab.updateLastUnloadedByTabUnloader()
- 位置: L474-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.browserEngagement.tabUnloadCount.add()`

## MozTabbrowserTab.recordTimeFromUnloadToReload()
- 位置: L479-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.browserEngagement.tabReloadCount.add()`, `Glean.browserEngagement.tabUnloadToReload.accumulateSingleSample()`

## MozTabbrowserTab.on_mouseover()
- 位置: L492-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`, `gBrowser._findTabToBlurTo()`, `gBrowser.warmupTab()`, `this.contains()`
- 条件付き依存: `if (this.hasTabNote)` → `noteIcon.contains()`
- 条件付き依存: `if (this.hasTabNote)` → `noteIconOverlay.contains()`
- 条件付き依存: `if (isOverNoteIcon && !this._noteIconHover)` → `this.dispatchEvent()`
- 条件付き依存: `if (isOverNoteIcon && !this._noteIconHover)` → `noteIcon?.contains()`
- 条件付き依存: `if (!this.contains(event.relatedTarget))` → `this._mouseenter()`

## MozTabbrowserTab.on_mouseout()
- 位置: L530-553
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contains()`
- 条件付き依存: `if (this._noteIconHover)` → `noteIcon.contains()`
- 条件付き依存: `if (this._noteIconHover)` → `noteIconOverlay.contains()`
- 条件付き依存: `if (!stillOverNoteIcon)` → `this.dispatchEvent()`
- 条件付き依存: `if (!stillOverNoteIcon)` → `this.contains()`
- 条件付き依存: `if (!this.contains(event.relatedTarget))` → `this._mouseleave()`

## MozTabbrowserTab.on_dragstart()
- 位置: L555-569
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(event.eventPhase == Event.CAPTURING_PHASE))` → `event.target.classList?.contains()`
- 条件付き依存: `if (!(event.eventPhase == Event.CAPTURING_PHASE))` → `gSharedTabWarning.willShowSharedTabWarning()`
- 条件付き依存: `if ( event.target.classList?.contains("tab-close-button") || gSharedTabWarning.willShowSharedTabWarning(this) )` → `event.stopPropagation()`

## MozTabbrowserTab.on_mousedown()
- 位置: L571-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSharedTabWarning.willShowSharedTabWarning()`
- 条件付き依存: `if (!(this.selected))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.button == 1)` → `gBrowser.warmupTab()`
- 条件付き依存: `if (event.button == 1)` → `gBrowser._findTabToBlurTo()`
- 条件付き依存: `if (event.button == 0)` → `event.getModifierState()`
- 条件付き依存: `if (!accelKey)` → `gBrowser.clearMultiSelectedTabs()`
- 条件付き依存: `if (shiftKey)` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (this != gBrowser.selectedTab)` → `gBrowser.addToMultiSelectedTabs()`
- 条件付き依存: `if (!(accelKey))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!this.selected && this.multiselected)` → `gBrowser.lockClearMultiSelectionOnce()`
- 条件付き依存: `if (eventMaySelectTab)` → `super.on_mousedown()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.recordTabMetrics()`
- 条件付き依存: `if (gBrowser.selectedTab !== prevTab)` → `gBrowser.TabMetrics.userTriggeredContext()`
- XPCOM: `Services.prefs`

## MozTabbrowserTab.on_mouseup()
- 位置: L650-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.unlockClearMultiSelection()`

## MozTabbrowserTab.on_click()
- 位置: L658-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.getModifierState()`, `event.target.classList.contains()`
- 条件付き依存: `if (event.altKey)` → `event.target.classList.contains()`
- 条件付き依存: `if (event.altKey)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !event.target.classList.contains("tab-close-button") && !event.target.classList.contains("tab-icon-overlay") && !event.target.classList.contains("tab-audio-...)` → `gBrowser.addTabSplitView()`
- 条件付き依存: `if ( gBrowser.multiSelectedTabsCount > 0 && !event.target.classList.contains("tab-close-button") && !event.target.classList.contains("tab-icon-overlay") && !even...)` → `gBrowser.clearMultiSelectedTabs()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.resumeDelayedMediaOnMultiSelectedTabs()`
- 条件付き依存: `if (!(this.multiselected))` → `this.resumeDelayedMedia()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.toggleMuteAudioOnMultiSelectedTabs()`
- 条件付き依存: `if (!(this.multiselected))` → `this.toggleMuteAudio()`
- 条件付き依存: `if (this.multiselected)` → `gBrowser.removeMultiSelectedTabs()`
- 条件付き依存: `if (this.multiselected)` → `lazy.TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (!(this.multiselected))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(this.multiselected))` → `lazy.TabMetrics.userTriggeredContext()`
- XPCOM: `Services.prefs`

## MozTabbrowserTab.on_dblclick()
- 位置: L741-766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("tab-close-button"))` → `event.stopPropagation()`
- 条件付き依存: `if ( tabContainer._closeTabByDblclick && this._selectedOnFirstMouseDown && this.selected && !event.target.classList.contains("tab-icon-overlay") )` → `gBrowser.removeTab()`
- 条件付き依存: `if ( tabContainer._closeTabByDblclick && this._selectedOnFirstMouseDown && this.selected && !event.target.classList.contains("tab-icon-overlay") )` → `lazy.TabMetrics.userTriggeredContext()`

## MozTabbrowserTab.on_animationstart()
- 位置: L768-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.animationName.startsWith()`, `event.target.getAnimations()`

## MozTabbrowserTab.on_animationend()
- 位置: L783-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("tab-loading-burst"))` → `this.removeAttribute()`

## MozTabbrowserTab._mouseenter()
- 位置: L806-823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.speculativeConnectOnTabHover()`, `this.dispatchEvent()`
- 条件付き依存: `if (this.selected)` → `this.container._handleTabSelect()`
- 条件付き依存: `if (this.linkedPanel)` → `this.linkedBrowser.unselectedTabHover()`
- 条件付き依存: `if (withoutPointerEvent)` → `this.#endHoverUnlessPointerArrives()`

## MozTabbrowserTab.#endHoverUnlessPointerArrives()
- 位置: L825-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopWaitingForPointer()`, `window.addEventListener()`

## onMouseEvent()
- 位置: L827-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopWaitingForPointer()`, `this.matches()`
- 条件付き依存: `if (!this.matches(":hover"))` → `this._mouseleave()`

## this.#stopWaitingForPointer()
- 位置: L834-839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.removeEventListener()`

## MozTabbrowserTab._mouseleave()
- 位置: L845-855
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopWaitingForPointer()`, `this.dispatchEvent()`
- 条件付き依存: `if (this.linkedPanel && !this.selected)` → `this.linkedBrowser.unselectedTabHover()`

## MozTabbrowserTab.resumeDelayedMedia()
- 位置: L857-863
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.activeMediaBlocked)` → `this.removeAttribute()`
- 条件付き依存: `if (this.activeMediaBlocked)` → `this.linkedBrowser.resumeMedia()`
- 条件付き依存: `if (this.activeMediaBlocked)` → `gBrowser._tabAttrModified()`

## MozTabbrowserTab.toggleMuteAudio()
- 位置: L865-883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser._tabAttrModified()`
- 条件付き依存: `if (this.linkedPanel)` → `browser.browsingContext?.mediaController?.unmute()`
- 条件付き依存: `if (browser.audioMuted)` → `this.removeAttribute()`
- 条件付き依存: `if (this.linkedPanel)` → `browser.browsingContext?.mediaController?.mute()`
- 条件付き依存: `if (!(browser.audioMuted))` → `this.toggleAttribute()`

## MozTabbrowserTab.registerAudibleChangeHandler()
- 位置: L896-961
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mediaController.addEventListener()`, `this.unregisterAudibleChangeHandler()`

## this.#audibleChangeHandler()
- 位置: L902-955
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (mediaController.isAudible)` → `clearTimeout()`
- 条件付き依存: `if (mediaController.isAudible)` → `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying-scheduledremoval"))` → `this.removeAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying-scheduledremoval"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (!this.hasAttribute("soundplaying"))` → `this.toggleAttribute()`
- 条件付き依存: `if (!this.hasAttribute("soundplaying"))` → `modifiedAttrs.push()`
- 条件付き依存: `if (modifiedAttrs.length)` → `getComputedStyle()`
- 条件付き依存: `if (mediaController.isAudible)` → `gBrowser._tabAttrModified()`
- 条件付き依存: `if (!(mediaController.isAudible))` → `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `Math.max()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `this.toggleAttribute()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `gBrowser._tabAttrModified()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `setTimeout()`
- 条件付き依存: `if (this.hasAttribute("soundplaying"))` → `this.removeAttribute()`
- XPCOM: `Services.prefs`

## MozTabbrowserTab.unregisterAudibleChangeHandler()
- 位置: L963-970
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#audibleChangeController?.removeEventListener()`

## MozTabbrowserTab.setUserContextId()
- 位置: L972-986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContextualIdentityService.setTabStyle()`
- 条件付き依存: `if (this.linkedBrowser)` → `this.linkedBrowser.setAttribute()`
- 条件付き依存: `if (aUserContextId)` → `this.setAttribute()`
- 条件付き依存: `if (this.linkedBrowser)` → `this.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (!(aUserContextId))` → `this.removeAttribute()`

## MozTabbrowserTab.updateA11yDescription()
- 位置: L988-999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `gBrowser.getTabTooltip()`, `gBrowser.tabContainer.querySelector()`, `this.setAttribute()`
- 条件付き依存: `if (prevDescTab)` → `prevDescTab.removeAttribute()`

## MozTabbrowserTab.on_focus()
- 位置: L1001-1003
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateA11yDescription()`

## MozTabbrowserTab.on_AriaFocus()
- 位置: L1005-1007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateA11yDescription()`

## MozTabbrowserTab.on_overflow()
- 位置: L1009-1011
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.currentTarget.toggleAttribute()`

## MozTabbrowserTab.on_underflow()
- 位置: L1013-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.currentTarget.removeAttribute()`

## MozTabbrowserTab.#updateOnTabGrouped()
- 位置: L1017-1031
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.group && this.#lastGroup != this.group)` → `this.group.dispatchEvent()`
- 条件付き依存: `if (this.group && this.#lastGroup != this.group)` → `this.setAttribute()`

## MozTabbrowserTab.#updateOnTabUngrouped()
- 位置: L1033-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#lastGroup && this.#lastGroup != this.group)` → `this.#lastGroup.dispatchEvent()`
- 条件付き依存: `if (this.#lastGroup && this.#lastGroup != this.group)` → `this.setAttribute()`
- 条件付き依存: `if (this.#lastGroup && this.#lastGroup != this.group)` → `this.removeAttribute()`

## MozTabbrowserTab.#updateOnTabSplit()
- 位置: L1056-1060
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.splitview)` → `this.setAttribute()`

## MozTabbrowserTab.#updateOnTabUnsplit()
- 位置: L1062-1072
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.splitview)` → `this.setAttribute()`
- 条件付き依存: `if (!this.splitview)` → `this.removeAttribute()`

## MozTabbrowserTab.updateSplitViewAriaLabel()
- 位置: L1081-1101
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (l10nId)` → `gBrowser.tabLocalization.formatValueSync()`
- 条件付き依存: `if (l10nId)` → `this.getAttribute()`
- 条件付き依存: `if (l10nId)` → `this.setAttribute()`
