# browser/components/aiwindow/ui/modules/AIWindowUI.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowUI.sys.mjs
source-hash: d24f44e2668d56df7b9f83dff3eb186bda61bfce
lines: 829

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _getSidebarElements()
- 位置: L44-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeDoc.getElementById()`
- 参照: `this.BOX_ID`, `this.SPLITTER_ID`, `win.document`

## updateSidebarMaxWidth()
- 位置: L63-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `gSidebarWidthHandlers.has()`, `nodes.box.style.setProperty()`, `parseFloat()`, `this._getSidebarElements()`, `win .getComputedStyle()`, `win .getComputedStyle(win.document.documentElement) .getPropertyValue()`
- 条件付き依存: `if (!gSidebarWidthHandlers.has(win))` → `gSidebarWidthHandlers.set()`
- 条件付き依存: `if (!gSidebarWidthHandlers.has(win))` → `win.addEventListener()`
- 参照: `win.document.documentElement`, `win.innerWidth`

## sidebarResizeHandler()
- 位置: L79-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateSidebarMaxWidth()`

## _removeSidebarWidthHandler()
- 位置: L90-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSidebarWidthHandlers.get()`
- 条件付き依存: `if (handler)` → `win.removeEventListener()`
- 条件付き依存: `if (handler)` → `gSidebarWidthHandlers.delete()`

## _getConversationFromSidebar()
- 位置: L102-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.getActiveConversation()`
- 参照: `conversation?.id`, `conversation?.messageCount`

## ensureBrowserIsAppended()
- 位置: L117-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `box.querySelector()`, `browser.setAttribute()`, `chromeDoc.createXULElement()`, `chromeDoc.getElementById()`, `stack.appendChild()`
- 条件付き依存: `if (!stack.isConnected)` → `stack.setAttribute()`
- 条件付き依存: `if (!stack.isConnected)` → `box.appendChild()`
- 参照: `browser.id`, `stack.className`, `stack.isConnected`, `this.BROWSER_ID`, `this.STACK_CLASS`

## isSidebarOpen()
- 位置: L148-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSidebarElements()`
- 参照: `nodes.box._aiWindowOpen`, `nodes.box.collapsed`

## _setSidebarCollapsed()
- 位置: L176-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._animateSidebarToggle()`, `win.document .getElementById()`, `win.document .getElementById("tabbrowser-tabbox") .toggleAttribute()`, `win.matchMedia()`
- 条件付き依存: `if (!collapse)` → `this.updateSidebarMaxWidth()`
- 条件付き依存: `if (!(!collapse))` → `this._removeSidebarWidthHandler()`
- 条件付き依存: `if (!animate || reduceMotion)` → `this._cancelSidebarAnimation()`
- 条件付き依存: `if (!animate || reduceMotion)` → `this._commitSidebarCollapsed()`
- 参照: `box._aiWindowOpen`, `win.matchMedia( "(prefers-reduced-motion: reduce)" ).matches`

## _commitSidebarCollapsed()
- 位置: L202-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearSidebarAnimationStyles()`
- 参照: `box.collapsed`, `box.parentElement.collapsed`, `splitter.collapsed`

## _clearSidebarAnimationStyles()
- 位置: L211-220
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `box.parentElement.style.overflow`, `box.style.bottom`, `box.style.left`, `box.style.position`, `box.style.right`, `box.style.top`, `box.style.width`

## _cancelSidebarAnimation()
- 位置: L222-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSidebarAnimations.get()`
- 条件付き依存: `if (animations)` → `gSidebarAnimations.delete()`
- 条件付き依存: `if (animations)` → `animations.forEach()`
- 条件付き依存: `if (animations)` → `animation.cancel()`

## _animateSidebarToggle()
- 位置: L230-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `Promise.allSettled(animations.map(animation => animation.finished)).then()`, `animations.map()`, `box.animate()`, `box.getBoundingClientRect()`, `browserEl.getBoundingClientRect()`, `gSidebarAnimations.delete()`, `gSidebarAnimations.get()`, `gSidebarAnimations.set()`, `parseFloat()`, `tabbox.animate()`, `tabbox.getBoundingClientRect()`, `this._cancelSidebarAnimation()`, `this._clearSidebarAnimationStyles()`, `this._commitSidebarCollapsed()`, `win.document.getElementById()`, `win.getComputedStyle()`
- 条件付き依存: `if (boxRect.width <= 0 || clipAmount <= 0)` → `this._commitSidebarCollapsed()`
- 参照: `animation.finished`, `box.collapsed`, `box.parentElement`, `box.style`, `box.style.bottom`, `box.style.position`, `box.style.top`, `box.style.width`, `boxRect.bottom`, `boxRect.left`, `boxRect.right`, `boxRect.top`, `boxRect.width`, `browserEl.collapsed`, `browserEl.style.overflow`, `browserRect.bottom`, `browserRect.left`, `browserRect.right`, `browserRect.top`, `browserStyle.paddingLeft`, `browserStyle.paddingRight`, `splitter.collapsed`, `tabboxRect.left`, `tabboxRect.right`, `this.SIDEBAR_ANIMATION_MS`

## openInFullWindow()
- 位置: L315-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.setAttribute()`, `contentDocument.dispatchEvent()`, `this.closeSidebar()`
- 参照: `browser.contentWindow.CustomEvent`, `browser.documentGlobal`, `conversation.id`

## reopenConversationInTab()
- 位置: L336-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.getMostRecentPageVisited()`, `lazy.URILoadingHelper.openTrustedLinkIn()`
- 参照: `mostRecentPage?.href`, `win.BROWSER_NEW_TAB_URL`

## resolveOnContentBrowserCreated()
- 位置: async L340-347
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (url === win.BROWSER_NEW_TAB_URL)` → `this.openInFullWindow()`
- 条件付き依存: `if (!(url === win.BROWSER_NEW_TAB_URL))` → `AIWindow.restoreTabConversation()`
- 条件付き依存: `if (!(url === win.BROWSER_NEW_TAB_URL))` → `this.openSidebar()`
- 参照: `targetBrowser.documentGlobal`, `win.BROWSER_NEW_TAB_URL`

## openSidebar()
- 位置: async L361-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.sidebarOpen.record()`, `aiWindowElement.onCreateNewChatClick()`, `this._getSidebarElements()`, `this.ensureBrowserIsAppended()`, `this.getAiWindowElement()`, `this.isSidebarOpen()`, `win.dispatchEvent()`
- 条件付き依存: `if (!this.isSidebarOpen(win))` → `this._setSidebarCollapsed()`
- 条件付き依存: `if (!this.isSidebarOpen(win))` → `this._updateAskButtonChecked()`
- 条件付き依存: `if (conversation)` → `aiBrowser.setAttribute()`
- 条件付き依存: `if (!(conversation))` → `aiBrowser.removeAttribute()`
- 条件付き依存: `if (conversation)` → `aiWindowElement.openConversation()`
- 参照: `conversation.id`, `conversation?.id`, `conversation?.messageCount`, `win.CustomEvent`, `win.document`, `win.gBrowser.selectedTab`

## getAiWindowElement()
- 位置: async L425-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `aiBrowser.contentDocument?.querySelector()`, `win.setTimeout()`
- 参照: `AIWindowUI.AI_WINDOW_ELEMENT_TIMEOUT`

## focusSidebar()
- 位置: async L437-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiBrowser.focus()`, `aiWindowElement.focusSmartbar()`, `this.getAiWindowElement()`, `this.isSidebarOpen()`, `win.document.getElementById()`
- 参照: `this.BROWSER_ID`

## closeSidebar()
- 位置: L463-490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.sidebarClose.record()`, `this._getConversationFromSidebar()`, `this._getSidebarElements()`, `this._setSidebarCollapsed()`, `this._updateAskButtonChecked()`, `this.isSidebarOpen()`, `win.dispatchEvent()`
- 参照: `win.CustomEvent`, `win.gBrowser?.selectedTab`

## toggleGroupTabsPanel()
- 位置: L499-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AutoTabGrouping.toggleGroupTabsPanel()`

## toggleMonitorPanel()
- 位置: L508-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorPanel.toggleMonitorPanel()`

## showMonitorCreateForm()
- 位置: L517-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MonitorPanel.showCreateForm()`

## toggleSidebar()
- 位置: L527-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getSidebarElements()`, `this._setSidebarCollapsed()`, `this._updateAskButtonChecked()`, `this.ensureBrowserIsAppended()`, `this.focusSidebar()`, `this.isSidebarOpen()`, `win.dispatchEvent()`
- 条件付き依存: `if (this.isSidebarOpen(win))` → `this.closeSidebar()`
- 参照: `win.CustomEvent`, `win.gBrowser?.selectedTab`

## restoreMemoriesState()
- 位置: L565-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.linkedBrowser?.contentDocument?.querySelector()`, `this._getSidebarAiWindow()`
- 条件付き依存: `if (aiWindowEl)` → `aiWindowEl.syncSmartbarMemoriesStateFromConversation()`

## _updateAskButtonChecked()
- 位置: L580-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `askBtn.setAttribute()`, `win.document.querySelector()`

## moveFullPageToSidebar()
- 位置: async L595-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.isAIWindowContentPage()`, `fullPageBrowser.contentDocument?.querySelector()`, `nodes.chromeDoc.getElementById()`, `this._getSidebarElements()`, `this.focusSidebar()`, `this.openSidebar()`
- 条件付き依存: `if (conversationId)` → `AIWindow.chatStore.findConversationById()`
- 参照: `aiWindowEl?.conversationId`, `fullPageBrowser.currentURI`, `fullPageBrowser?.currentURI`, `tab.linkedBrowser`, `this.BROWSER_ID`

## updateSidebarInput()
- 位置: L638-649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindowEl.updateInput()`, `this._getSidebarAiWindow()`, `this.isSidebarOpen()`
- 参照: `aiWindowEl?.updateInput`

## updateSidebarModel()
- 位置: L658-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindowEl.restoreModelChoiceOverride()`, `this._getSidebarAiWindow()`, `this.isSidebarOpen()`
- 参照: `aiWindowEl?.restoreModelChoiceOverride`

## updateSidebarContextChips()
- 位置: L679-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindowEl.restoreContextChips()`, `this._getSidebarAiWindow()`, `this.isSidebarOpen()`
- 参照: `aiWindowEl?.restoreContextChips`

## updateStarterPrompts()
- 位置: L707-714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindow.loadStarterPrompts()`, `this._getActiveAiWindow()`
- 参照: `win.gBrowser.selectedTab`

## _getSidebarAiWindow()
- 位置: L723-730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aiWindowBrowser?.contentDocument?.querySelector()`, `this.isSidebarOpen()`, `win.document.getElementById()`
- 参照: `this.BROWSER_ID`

## _getActiveAiWindow()
- 位置: L743-755
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (mode === "sidebar")` → `this._getSidebarAiWindow()`
- 条件付き依存: `if (mode === "fullpage" && tab)` → `tab.linkedBrowser.contentDocument.querySelector()`

## _getFadeTarget()
- 位置: L757-760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win?.document?.getElementById()`
- 参照: `tabPanels?.selectedPanel`

## _prefersReducedMotion()
- 位置: L762-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win?.matchMedia()`
- 参照: `win?.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches`

## _fadeToOpacity()
- 位置: L766-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `el.addEventListener()`, `el.removeEventListener()`, `resolve()`, `win.setTimeout()`
- 参照: `el.style.opacity`, `el.style.transition`, `this.TAB_FADE_MS`, `this.TAB_FADE_TIMEOUT_MS`

## onEnd()
- 位置: L768-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `el.removeEventListener()`, `resolve()`, `win.clearTimeout()`
- 参照: `event.propertyName`

## _runTabPanelsFade()
- 位置: async L789-811
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.getBoundingClientRect()`, `this._fadeToOpacity()`, `this._getFadeTarget()`, `this._prefersReducedMotion()`
- 参照: `target.style.opacity`, `target.style.transition`

## handleSameLinkClick()
- 位置: L818-827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gFadingWindows.add()`, `gFadingWindows.delete()`, `gFadingWindows.has()`, `this._runTabPanelsFade()`, `this._runTabPanelsFade(win).finally()`
