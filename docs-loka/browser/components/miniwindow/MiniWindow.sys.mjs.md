# browser/components/miniwindow/MiniWindow.sys.mjs

source: browser/components/miniwindow/MiniWindow.sys.mjs
source-hash: 5671b07ac9e5f6a02edfd1b01fdf7e0390056c1c
lines: 1067

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.now()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## MiniWindow.constructor()
- 位置: L196-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originWin.gBrowser.tabs.indexOf()`
- 条件付き依存: `if (!(cropInfo))` → `lazy.MiniWindowUtils.fullTabSize()`
- 参照: `MiniWindowState.OPENING`, `browser.clientHeight`, `browser.clientWidth`, `browser.fullZoom`, `sourceTab.linkedBrowser`, `this.#cropped`, `this.#originTabIndex`, `this.#sourceTab`, `this._crop`, `this._cropInfo`, `this._pageHeight`, `this._pageWidth`, `this._state`, `this.manager`, `this.miniWin`, `this.originWin`

## MiniWindow.state()
- 位置: L231-233
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## MiniWindow.isCropped()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#cropped`

## MiniWindow.browser()
- 位置: L250-252
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.miniWin?.gBrowser.selectedBrowser`

## MiniWindow.tab()
- 位置: L260-262
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.miniWin?.gBrowser?.selectedTab`

## MiniWindow.open()
- 位置: async L273-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.replaceTabWithWindow()`, `lazy.BrowserUtils.promiseObserved()`, `lazy.MiniWindowUtils.computeWindowRect()`, `lazy.logConsole.debug()`, `this.#attachHistoryListener()`, `this.#avoidOtherWindows()`, `this.#restrictShortcuts()`, `this.#sourceTab.setAttribute()`, `this.#wireNavBarButtons()`, `this.#wireToolbarReveal()`, `this.miniWin.addEventListener()`
- 条件付き依存: `if (this.#cropped)` → `this.#sourceTab.setAttribute()`
- 条件付き依存: `if (!this.miniWin)` → `lazy.logConsole.error()`
- 条件付き依存: `if (!this.miniWin)` → `this.#sourceTab.removeAttribute()`
- 条件付き依存: `if (this.#cropped)` → `this.#frame()`
- 参照: `MiniWindowState.ACTIVE`, `MiniWindowState.CLOSED`, `MiniWindowState.FRAMED`, `rect.height`, `rect.left`, `rect.top`, `rect.width`, `this.#abortController`, `this.#cropped`, `this.#sourceTab`, `this._cropInfo`, `this._state`, `this.miniWin`, `this.originWin`, `this.originWin.gBrowser`

## MiniWindow.#avoidOtherWindows()
- 位置: L346-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MiniWindowUtils.repositionToAvoid()`, `this.manager.windowsToAvoid()`
- 条件付き依存: `if (pos)` → `this.miniWin.moveTo()`
- 参照: `pos.left`, `pos.top`, `this.miniWin`, `this.miniWin.closed`

## MiniWindow.#attachHistoryListener()
- 位置: L363-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `sessionHistory.addSHistoryListener()`
- 参照: `this.#cropped`, `this.#historyListener`, `this.#historyListenerSH`, `this.#tabURI`, `this.browser.currentURI`, `this.browser?.browsingContext?.sessionHistory`

## OnHistoryNewEntry()
- 位置: L373-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `aNewURI?.equalsExceptRef()`, `this.returnToOriginWin()`
- 参照: `MiniWindowState.ACTIVE`, `this.#tabURI`, `this._state`
- XPCOM: `Services.tm`

## OnHistoryReload()
- 位置: L386-386
- 役割: (未記入)
- 触るとき: (未記入)

## OnHistoryGotoIndex()
- 位置: L387-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `this.returnToOriginWin()`
- 参照: `MiniWindowState.ACTIVE`, `this._state`
- XPCOM: `Services.tm`

## MiniWindow.OnHistoryPurge()
- 位置: L395-395
- 役割: (未記入)
- 触るとき: (未記入)

## MiniWindow.OnHistoryTruncate()
- 位置: L396-396
- 役割: (未記入)
- 触るとき: (未記入)

## MiniWindow.OnHistoryReplaceEntry()
- 位置: L397-397
- 役割: (未記入)
- 触るとき: (未記入)

## MiniWindow.OnHistoryCommit()
- 位置: L398-398
- 役割: (未記入)
- 触るとき: (未記入)

## MiniWindow.#detachHistoryListener()
- 位置: L408-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.error()`, `this.#historyListenerSH?.removeSHistoryListener()`
- 参照: `this.#historyListener`, `this.#historyListenerSH`, `this.#tabURI`

## MiniWindow.#restrictShortcuts()
- 位置: L426-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_KEYS.has()`, `Object.entries()`, `this.miniWin.document.getElementById()`, `this.miniWin.document.getElementById(id)?.addEventListener()`
- 条件付き依存: `if (!this.#cropped)` → `ALLOWED_KEYS.add()`
- 条件付き依存: `if (key.localName === "key" && !ALLOWED_KEYS.has(key.id))` → `key.setAttribute()`
- 参照: `key.id`, `key.localName`, `keyset.children`, `this.#abortController`, `this.#closeMethod`, `this.#cropped`

## MiniWindow.#wireNavBarButtons()
- 位置: L470-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `closeButton?.addEventListener()`, `closeButton?.removeAttribute()`, `doc.getElementById()`, `restoreButton?.addEventListener()`, `restoreButton?.removeAttribute()`, `this.#wireAudioButton()`, `this.close()`, `this.returnToOriginWin()`
- 参照: `this.#abortController`, `this.miniWin.document`

## MiniWindow.#wireAudioButton()
- 位置: L492-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `audioButton.addEventListener()`, `sync()`, `tab.addEventListener()`, `tab.toggleMuteAudio()`, `this.miniWin.document.getElementById()`
- 参照: `this.#abortController`, `this.tab`

## sync()
- 位置: L502-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `audioButton.setAttribute()`, `audioButton.toggleAttribute()`, `tab.hasAttribute()`

## MiniWindow.#wireToolbarReveal()
- 位置: L530-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enableScrollReveal()`, `this.#revealForFirstOpen()`, `this.#trackToolbarHeight()`, `this.miniWin.gBrowser.addTabsProgressListener()`, `this.revealToolbar()`, `toolbox.addEventListener()`, `win.MousePosTracker.addListener()`
- 参照: `this.#abortController`, `this.#edgeListener`, `this.#progressListener`, `this.miniWin`, `this.miniWin.gNavToolbox`

## MiniWindow.getMouseTargetRect()
- 位置: L536-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.windowUtils.getBoundsWithoutFlushing()`
- 参照: `lazy.prefs.edgeZonePx`, `win.document.documentElement`

## onMouseEnter()
- 位置: L548-555
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#scheduleHoverReveal()`
- 参照: `this.#edgeSuppressed`

## onMouseLeave()
- 位置: L556-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cancelHoverReveal()`, `toolbox.classList.contains()`
- 条件付き依存: `if (toolbox.classList.contains("mini-window-revealed"))` → `this.#startHideCountdown()`
- 参照: `this.#edgeSuppressed`

## onToolbarLeave()
- 位置: L569-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolbox.contains()`
- 条件付き依存: `if (!toolbox.contains(event.relatedTarget))` → `this.revealToolbar()`
- 参照: `event.relatedTarget`

## onLocationChange()
- 位置: L581-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enableScrollReveal()`, `this.revealToolbar()`

## MiniWindow.#revealForFirstOpen()
- 位置: L602-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `root.removeAttribute()`, `root.setAttribute()`, `this.miniWin.requestAnimationFrame()`, `this.miniWin?.requestAnimationFrame()`, `this.revealToolbar()`
- 参照: `this.miniWin.document.documentElement`

## MiniWindow.#trackToolbarHeight()
- 位置: L621-642
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries.at()`, `setHeight()`, `this.#toolbarHeightObserver.observe()`, `this.miniWin.windowUtils.getBoundsWithoutFlushing()`
- 参照: `entries.at(-1)?.borderBoxSize`, `entries.at(-1)?.borderBoxSize?.[0]?.blockSize`, `this.#toolbarHeightObserver`, `this.miniWin.ResizeObserver`, `this.miniWin.windowUtils.getBoundsWithoutFlushing(toolbox).height`

## setHeight()
- 位置: L622-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.miniWin?.document.documentElement.style.setProperty()`

## MiniWindow.hideToolbarOnScrollDown()
- 位置: L647-650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#hideToolbar()`
- 参照: `this.#edgeSuppressed`

## MiniWindow.#toolbarHeld()
- 位置: L659-671
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc .getElementById()`, `doc .getElementById("notifications-toolbar") ?.querySelector()`, `doc.getElementById()`
- 参照: `doc.getElementById("notification-popup")?.state`, `this.miniWin?.document`

## MiniWindow.#enableScrollReveal()
- 位置: L674-676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getActor()`, `this.#getActor()?.sendAsyncMessage()`

## MiniWindow.revealToolbar()
- 位置: L683-686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#keepToolbarShown()`, `this.#startHideCountdown()`
- 参照: `lazy.prefs.hideDelayMs`

## MiniWindow.#startHideCountdown()
- 位置: L693-704
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearHideTimer()`, `this.#hideToolbar()`, `this.#toolbarHeld()`, `this.miniWin.setTimeout()`
- 条件付き依存: `if (this.#toolbarHeld())` → `this.#startHideCountdown()`
- 参照: `lazy.prefs.hideDelayMs`, `this.#hideToolbarTimer`

## MiniWindow.#keepToolbarShown()
- 位置: L707-710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearHideTimer()`, `this.miniWin?.gNavToolbox?.classList.add()`

## MiniWindow.#hideToolbar()
- 位置: L713-717
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cancelHoverReveal()`, `this.#clearHideTimer()`, `this.miniWin?.gNavToolbox?.classList.remove()`

## MiniWindow.#clearHideTimer()
- 位置: L719-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.miniWin.clearTimeout()`
- 参照: `this.#hideToolbarTimer`

## MiniWindow.#scheduleHoverReveal()
- 位置: L732-743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.miniWin?.gNavToolbox?.classList.contains()`
- 条件付き依存: `if (this.miniWin?.gNavToolbox?.classList.contains("mini-window-revealed"))` → `this.#keepToolbarShown()`
- 条件付き依存: `if (this.#hoverRevealTimer === null)` → `this.miniWin.setTimeout()`
- 条件付き依存: `if (this.#hoverRevealTimer === null)` → `this.#keepToolbarShown()`
- 参照: `lazy.prefs.hoverRevealDelayMs`, `this.#hoverRevealTimer`

## MiniWindow.#cancelHoverReveal()
- 位置: L745-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.miniWin.clearTimeout()`
- 参照: `this.#hoverRevealTimer`

## MiniWindow.#unwireToolbarReveal()
- 位置: L755-774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cancelHoverReveal()`, `this.#clearHideTimer()`, `this.#frameResizeObserver?.disconnect()`, `this.#toolbarHeightObserver?.disconnect()`
- 条件付き依存: `if (this.#progressListener)` → `this.miniWin?.gBrowser?.removeTabsProgressListener()`
- 条件付き依存: `if (this.#edgeListener)` → `this.miniWin?.MousePosTracker.removeListener()`
- 参照: `this.#edgeListener`, `this.#frameResizeObserver`, `this.#progressListener`, `this.#toolbarHeightObserver`

## MiniWindow.handleEvent()
- 位置: L779-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onUnload()`
- 条件付き依存: `if (this._state === MiniWindowState.ACTIVE)` → `this.miniWin.setTimeout()`
- 条件付き依存: `if (this._state === MiniWindowState.ACTIVE)` → `this.revealToolbar()`
- 参照: `MiniWindowState.ACTIVE`, `event.type`, `lazy.prefs.hoverRevealDelayMs`, `this._state`

## MiniWindow.#frame()
- 位置: async L806-846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor?.sendAsyncMessage()`, `actor?.sendQuery()`, `actor?.sendQuery("GetSize").catch()`, `browser.closest()`, `lazy.MiniWindowUtils.computeFrameBox()`, `lazy.logConsole.debug()`, `this.#applyTransform()`, `this.#getActor()`, `this.#trackWindowResize()`
- 条件付き依存: `if (!actor)` → `lazy.logConsole.warn()`
- 参照: `box.boxHeight`, `box.boxWidth`, `box.pageHeight`, `box.pageWidth`, `browser.parentNode`, `browser.style.height`, `browser.style.minHeight`, `browser.style.minWidth`, `browser.style.transformOrigin`, `browser.style.width`, `container.style.overflow`, `cropInfo.fullZoom`, `cropInfo.height`, `cropInfo.left`, `cropInfo.top`, `cropInfo.width`, `this._crop`, `this._pageHeight`, `this._pageWidth`

## MiniWindow.#getActor()
- 位置: L852-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browser?.browsingContext?.currentWindowGlobal?.getActor()`

## MiniWindow.#applyTransform()
- 位置: L865-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MiniWindowUtils.computeTransform()`, `this.miniWin.windowUtils.getBoundsWithoutFlushing()`
- 参照: `this._crop`, `this._cropInfo.fullZoom`, `this.browser.style.transform`, `this.miniWin.document.documentElement`, `this.miniWin.windowUtils.getBoundsWithoutFlushing( this.miniWin.document.documentElement ).width`

## MiniWindow.#trackWindowResize()
- 位置: L884-893
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entries.at()`, `this.#frameResizeObserver.observe()`
- 条件付き依存: `if (width)` → `this.#applyTransform()`
- 参照: `entries.at(-1)?.contentBoxSize`, `entries.at(-1)?.contentBoxSize?.[0]?.inlineSize`, `this.#frameResizeObserver`, `this.miniWin.ResizeObserver`, `this.miniWin.document.documentElement`

## MiniWindow.#onUnload()
- 位置: L902-911
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this._state !== MiniWindowState.RESTORING && this._state !== MiniWindowState.CLOSING && this._state !== MiniWindowState.CLOSED )` → `lazy.logConsole.debug()`
- 条件付き依存: `if ( this._state !== MiniWindowState.RESTORING && this._state !== MiniWindowState.CLOSING && this._state !== MiniWindowState.CLOSED )` → `this.returnToOriginWin()`
- 参照: `MiniWindowState.CLOSED`, `MiniWindowState.CLOSING`, `MiniWindowState.RESTORING`, `this._state`

## MiniWindow.close()
- 位置: L927-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `flushed .then()`, `lazy.TabStateFlusher.flush()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#abortController?.abort()`, `this.#detachHistoryListener()`, `this.#returnTabToOrigin()`, `this.#unwireToolbarReveal()`, `this.uninit()`
- 条件付き依存: `if (adopted && win && !win.closed)` → `win.gBrowser.removeTab()`
- 参照: `MiniWindowState.CLOSED`, `MiniWindowState.CLOSING`, `this.#closeMethod`, `this._state`, `this.tab`, `this.tab.linkedBrowser`, `win.closed`

## MiniWindow.returnToOriginWin()
- 位置: L962-987
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `this.#returnTabToOrigin()`, `this.uninit()`
- 条件付き依存: `if (focus && adopted && targetWin && !targetWin.closed)` → `targetWin.focus()`
- 条件付き依存: `if (focus && adopted && targetWin && !targetWin.closed)` → `targetWin.getAttention()`
- 参照: `MiniWindowState.ACTIVE`, `MiniWindowState.FRAMED`, `MiniWindowState.OPENING`, `MiniWindowState.RESTORING`, `targetWin.closed`, `this.#closeMethod`, `this._state`

## MiniWindow.#returnTabToOrigin()
- 位置: L996-1014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `target.gBrowser.adoptTab()`
- 条件付き依存: `if (!target && selectTab)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 参照: `originWin.closed`, `target.gBrowser.tabs.length`, `this.#originTabIndex`, `this.tab`

## MiniWindow.uninit()
- 位置: L1020-1065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.miniWindow.closed.record()`, `Glean.miniWindow.openDuration[flavour].accumulateSingleSample()`, `Math.round()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `this.#abortController?.abort()`, `this.#detachHistoryListener()`, `this.#unwireToolbarReveal()`, `this.manager._unregister()`, `this.miniWin?.removeEventListener()`
- 条件付き依存: `if (this._state === MiniWindowState.CLOSED)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (this.miniWin && !this.miniWin.closed)` → `this.miniWin.close()`
- 参照: `Glean.miniWindow.openDuration`, `MiniWindowState.CLOSED`, `this.#closeMethod`, `this.#createdAt`, `this.#cropped`, `this._state`, `this.miniWin`, `this.miniWin.closed`
