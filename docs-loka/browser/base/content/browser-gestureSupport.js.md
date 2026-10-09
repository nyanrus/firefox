# browser/base/content/browser-gestureSupport.js

source: browser/base/content/browser-gestureSupport.js
source-hash: 89aef994819370b0577923f488690558f010cdec
lines: 1062

## <module>
- 役割: (未記入)
- 呼び出し先: `aArray.reduce()`

## init()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleListeners()`

## uninit()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleListeners()`

## _toggleListeners()
- 位置: L44-68
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aAddListener)` → `gBrowser.tabbox.addEventListener()`
- 条件付き依存: `if (!(aAddListener))` → `gBrowser.tabbox.removeEventListener()`

## GS_handleEvent()
- 位置: L78-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `aEvent.preventDefault()`, `def()`, `this._doAction()`, `this._doEnd()`, `this._doUpdate()`, `this._setupGesture()`, `this._setupSwipeGesture()`, `this._shouldDoSwipeGesture()`, `this.onSwipe()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref( "dom.debug.propagate_gesture_events_through_content" ) )` → `aEvent.stopPropagation()`
- 条件付き依存: `if (this._shouldDoSwipeGesture(aEvent))` → `aEvent.preventDefault()`
- 参照: `aEvent.type`
- XPCOM: `Services.prefs`

## def()
- 位置: L88-91
- 役割: (未記入)
- 触るとき: (未記入)

## GS__setupGesture()
- 位置: L156-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `this._doUpdate()`, `this._getPref()`
- 参照: `aEvent.delta`, `this._doUpdate`

## GS__doUpdate()
- 位置: L174-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if (!aPref.latched || isLatched ^ sameDir)` → `this._doAction()`
- 参照: `aPref.latched`, `aPref.threshold`, `updateEvent.delta`

## GS__swipeNavigatesHistory()
- 位置: L210-220
- 役割: (未記入)
- 触るとき: (未記入)

## GS__shouldDoSwipeGesture()
- 位置: L231-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.hasAttribute()`, `gHistorySwipeAnimation.canGoBack()`, `gHistorySwipeAnimation.canGoForward()`, `this._getCommand()`, `this._swipeNavigatesHistory()`
- 参照: `aEvent.DIRECTION_DOWN`, `aEvent.DIRECTION_LEFT`, `aEvent.DIRECTION_RIGHT`, `aEvent.DIRECTION_UP`, `aEvent.allowedDirections`, `aEvent.direction`, `gHistorySwipeAnimation.isLTR`, `window.content.pageYOffset`, `window.content.scrollMaxY`

## GS__setupSwipeGesture()
- 位置: L302-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHistorySwipeAnimation.startAnimation()`
- 参照: `this._doEnd`, `this._doUpdate`

## GS__doUpdate()
- 位置: L305-310
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHistorySwipeAnimation.updateAnimation()`
- 参照: `aEvent.delta`

## GS__doEnd()
- 位置: L312-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHistorySwipeAnimation.swipeEndEventReceived()`
- 参照: `this._doEnd`, `this._doUpdate`

## this._doUpdate()
- 位置: L315-315
- 役割: (未記入)
- 触るとき: (未記入)

## this._doEnd()
- 位置: L316-316
- 役割: (未記入)
- 触るとき: (未記入)

## GS__doAction()
- 位置: L353-356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._doCommand()`, `this._getCommand()`

## GS__getCommand()
- 位置: L367-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aGesture.concat()`, `aGesture.concat(subCombo).join()`, `this._getPref()`, `this._power()`
- 条件付き依存: `if (aEvent[key + "Key"])` → `keyCombos.push()`

## GS__doCommand()
- 位置: L403-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (node)` → `node.getAttribute()`
- 条件付き依存: `if (node.getAttribute("disabled") != "true")` → `document.createEvent()`
- 条件付き依存: `if (node.getAttribute("disabled") != "true")` → `cmdEvent.initCommandEvent()`
- 条件付き依存: `if (node.getAttribute("disabled") != "true")` → `node.dispatchEvent()`
- 条件付き依存: `if (!(node))` → `goDoCommand()`
- 参照: `aEvent.altKey`, `aEvent.ctrlKey`, `aEvent.inputSource`, `aEvent.metaKey`, `aEvent.shiftKey`

## _doUpdate()
- 位置: L436-436
- 役割: (未記入)
- 触るとき: (未記入)

## _doEnd()
- 位置: L444-444
- 役割: (未記入)
- 触るとき: (未記入)

## GS_onSwipe()
- 位置: L452-460
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aEvent.direction == aEvent["DIRECTION_" + dir])` → `this._coordinateSwipeEventWithAnimation()`
- 参照: `aEvent.direction`

## GS_processSwipeEvent()
- 位置: L470-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aDir.toLowerCase()`, `this._doAction()`
- 参照: `gHistorySwipeAnimation.isLTR`

## GS__coordinateSwipeEventWithAnimation()
- 位置: L503-506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHistorySwipeAnimation.stopAnimation()`, `this.processSwipeEvent()`

## GS__getPref()
- 位置: L516-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs["get" + getFunc + "Pref"]()`
- 参照: `Services.prefs`
- XPCOM: `Services.prefs`

## rotate()
- 位置: L541-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ImageDocument.isInstance()`, `Math.round()`, `contentElement.classList.contains()`
- 条件付き依存: `if (contentElement.classList.contains("completeRotation"))` → `this._clearCompleteRotation()`
- 参照: `aEvent.delta`, `contentElement.style.transform`, `this._lastRotateDelta`, `this.rotation`, `window.content.document`, `window.content.document.body.firstElementChild`

## rotateEnd()
- 位置: L563-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ImageDocument.isInstance()`
- 条件付き依存: `if (transitionRotation != this.rotation)` → `contentElement.classList.add()`
- 条件付き依存: `if (transitionRotation != this.rotation)` → `contentElement.addEventListener()`
- 参照: `contentElement.style.transform`, `this._clearCompleteRotation`, `this._lastRotateDelta`, `this._rotateMomentumThreshold`, `this.rotation`, `window.content.document`, `window.content.document.body.firstElementChild`

## rotation()
- 位置: L620-622
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._currentRotation`

## rotation()
- 位置: L631-636
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._currentRotation`

## restoreRotationState()
- 位置: L642-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ImageDocument.isInstance()`, `Math.atan2()`, `Math.round()`, `transformValue.split()`, `transformValue.split("(")[1].split()`, `transformValue.split("(")[1].split(")")[0].split()`, `window.content.window.getComputedStyle()`
- 参照: `Math.PI`, `this.rotation`, `window.content.document`, `window.content.document.body.firstElementChild`, `window.content.window.getComputedStyle(contentElement).transform`

## _clearCompleteRotation()
- 位置: L672-686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ImageDocument.isInstance()`, `contentElement.classList.remove()`, `contentElement.removeEventListener()`
- 参照: `this._clearCompleteRotation`, `window.content.document`, `window.content.document.body`, `window.content.document.body.firstElementChild`

## HSA_init()
- 位置: L698-719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.documentElement.matches()`, `document.getElementById()`, `this._addPrefObserver()`, `this._initPrefValues()`, `this._isSupported()`
- 参照: `this._icon`, `this._isStoppingAnimation`, `this.active`, `this.isLTR`
- XPCOM: `Services.prefs`

## HSA_uninit()
- 位置: L724-730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._removeBoxes()`, `this._removePrefObserver()`
- 参照: `this._icon`, `this.active`, `this.isLTR`

## HSA_startAnimation()
- 位置: L738-750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._removeBoxes()`, `this.canGoBack()`, `this.canGoForward()`, `this.updateAnimation()`
- 条件付き依存: `if (this.active)` → `this._addBoxes()`
- 参照: `this._canGoBack`, `this._canGoForward`, `this._isStoppingAnimation`, `this.active`

## HSA_stopAnimation()
- 位置: L755-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isAnimationRunning()`
- 条件付き依存: `if (box != null)` → `box.addEventListener()`
- 条件付き依存: `if (box != null)` → `window.getComputedStyle()`
- 条件付き依存: `if (!(box != null))` → `this._removeBoxes()`
- 参照: `box.collapsed`, `box.style.opacity`, `box.style.transition`, `box.style.translate`, `this._isStoppingAnimation`, `this._lastVisibleBox`, `this._lastVisibleTranslate`, `this._nextBox`, `this._nextBox.collapsed`, `this._prevBox`, `this._prevBox.collapsed`, `window.getComputedStyle(box).opacity`

## HSA_swipeCommand()
- 位置: L786-795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gGestureSupport._getCommand()`
- 参照: `aSwipeUpdate.delta`, `aSwipeUpdate.event`, `this.isLTR`

## HSA_willGoBack()
- 位置: L797-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._swipeCommand()`
- 参照: `this._canGoBack`

## HSA_willGoForward()
- 位置: L801-805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._swipeCommand()`
- 参照: `this._canGoForward`

## HSA_updateAnimation()
- 位置: L817-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`, `Math.min()`, `this._willGoBack()`, `this.isAnimationRunning()`
- 条件付き依存: `if (radius >= 0)` → `this._prevBox .querySelectorAll("circle")[1] .setAttribute()`
- 条件付き依存: `if (radius >= 0)` → `this._prevBox .querySelectorAll()`
- 条件付き依存: `if (this._willGoBack(aSwipeUpdate))` → `Math.abs()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._prevBox.querySelector("svg").classList.add()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._prevBox.querySelector()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._prevBox.querySelector("svg").classList.remove()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._prevBox.querySelector()`
- 条件付き依存: `if (!(this._willGoBack(aSwipeUpdate)))` → `this._willGoForward()`
- 条件付き依存: `if (radius >= 0)` → `this._nextBox .querySelectorAll("circle")[1] .setAttribute()`
- 条件付き依存: `if (radius >= 0)` → `this._nextBox .querySelectorAll()`
- 条件付き依存: `if (this._willGoForward(aSwipeUpdate))` → `Math.abs()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._nextBox.querySelector("svg").classList.add()`
- 条件付き依存: `if (Math.abs(aSwipeUpdate.delta) >= 0.25)` → `this._nextBox.querySelector()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._nextBox.querySelector("svg").classList.remove()`
- 条件付き依存: `if (!(Math.abs(aSwipeUpdate.delta) >= 0.25))` → `this._nextBox.querySelector()`
- 参照: `aSwipeUpdate.delta`, `this._isStoppingAnimation`, `this._lastVisibleBox`, `this._lastVisibleTranslate`, `this._nextBox`, `this._nextBox.collapsed`, `this._nextBox.style.translate`, `this._prevBox`, `this._prevBox.collapsed`, `this._prevBox.style.translate`, `this.isLTR`, `this.maxRadius`, `this.minRadius`, `this.translateEndPosition`, `this.translateStartPosition`

## HSA_isAnimationRunning()
- 位置: L894-896
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._container`

## HSA_canGoBack()
- 位置: L903-905
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.webNavigation.canGoBack`

## HSA_canGoForward()
- 位置: L912-914
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `gBrowser.webNavigation.canGoForward`

## HSA_swipeEndEventReceived()
- 位置: L921-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stopAnimation()`

## HSA__isSupported()
- 位置: L931-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.matchMedia()`
- 参照: `window.matchMedia("(-moz-swipe-animation-enabled)").matches`

## HSA_handleEvent()
- 位置: L935-941
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._completeFadeOut()`
- 参照: `aEvent.type`

## HSA__completeFadeOut()
- 位置: L943-951
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gHistorySwipeAnimation._removeBoxes()`
- 参照: `this._isStoppingAnimation`

## HSA__addBoxes()
- 位置: L956-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserStack.appendChild()`, `gBrowser.getPanel()`, `gBrowser.getPanel().querySelector()`, `icon.classList.add()`, `this._container.appendChild()`, `this._createElement()`, `this._icon.cloneNode()`, `this._nextBox.appendChild()`, `this._prevBox.appendChild()`
- 参照: `this._container`, `this._nextBox`, `this._nextBox.collapsed`, `this._prevBox`, `this._prevBox.collapsed`

## HSA__removeBoxes()
- 位置: L988-997
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._container)` → `this._container.remove()`
- 参照: `this._container`, `this._lastVisibleBox`, `this._lastVisibleTranslate`, `this._nextBox`, `this._prevBox`

## HSA__createElement()
- 位置: L1008-1012
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`
- 参照: `element.id`

## observe()
- 位置: L1014-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._initPrefValues()`

## HSA__initPrefValues()
- 位置: L1021-1038
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `this.maxRadius`, `this.minRadius`, `this.translateEndPosition`, `this.translateStartPosition`
- XPCOM: `Services.prefs`

## HSA__addPrefObserver()
- 位置: L1040-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`
- XPCOM: `Services.prefs`

## HSA__removePrefObserver()
- 位置: L1051-1060
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`
