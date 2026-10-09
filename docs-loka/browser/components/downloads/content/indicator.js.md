# browser/components/downloads/content/indicator.js

source: browser/components/downloads/content/indicator.js
source-hash: 3d7d4aece537362831f16c3258e160f28f23b390
lines: 689

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.defineProperty()`

## _placeholder()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`

## initializeIndicator()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsIndicatorView.ensureInitialized()`

## _getAnchorInternal()
- 位置: L66-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `isElementVisible()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `DownloadsIndicatorView.indicator`, `DownloadsIndicatorView.indicatorAnchor`, `indicator.open`, `indicator.parentNode`, `this._anchorRequested`, `widget.areaType`

## getAnchor()
- 位置: L100-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getAnchorInternal()`
- 参照: `this._anchorRequested`, `this._customizing`

## releaseAnchor()
- 位置: L113-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getAnchorInternal()`
- 参照: `this._anchorRequested`

## unhide()
- 位置: L130-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.hasAttribute()`
- 条件付き依存: `if (!button && includePalette)` → `gNavToolbox.palette.querySelector()`
- 条件付き依存: `if (button && button.hasAttribute("hidden"))` → `button.removeAttribute()`
- 条件付き依存: `if (button && button.hasAttribute("hidden"))` → `this._navBar.contains()`
- 条件付き依存: `if (this._navBar.contains(button))` → `this._navBar.setAttribute()`
- 参照: `this._placeholder`

## hide()
- 位置: L146-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.closest()`
- 条件付き依存: `if (this.autoHideDownloadsButton && button && button.closest("toolbar"))` → `DownloadsPanel.hidePanel()`
- 条件付き依存: `if (this.autoHideDownloadsButton && button && button.closest("toolbar"))` → `this._navBar.removeAttribute()`
- 参照: `button.hidden`, `this._placeholder`, `this.autoHideDownloadsButton`

## startAutoHide()
- 位置: L155-161
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (DownloadsIndicatorView.hasDownloads)` → `this.unhide()`
- 条件付き依存: `if (!(DownloadsIndicatorView.hasDownloads))` → `this.hide()`
- 参照: `DownloadsIndicatorView.hasDownloads`

## checkForAutoHide()
- 位置: L163-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.closest()`
- 条件付き依存: `if ( !this._customizing && this.autoHideDownloadsButton && button && button.closest("toolbar") )` → `this.startAutoHide()`
- 条件付き依存: `if (!( !this._customizing && this.autoHideDownloadsButton && button && button.closest("toolbar") ))` → `this.unhide()`
- 参照: `this._customizing`, `this._placeholder`, `this.autoHideDownloadsButton`

## onWidgetAfterDOMChange()
- 位置: L180-184
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node == this._placeholder)` → `this.checkForAutoHide()`
- 参照: `this._placeholder`

## onCustomizeStart()
- 位置: L194-202
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win == window)` → `this.unhide()`
- 参照: `this._anchorRequested`, `this._customizing`

## onCustomizeEnd()
- 位置: L204-210
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win == window)` → `this.checkForAutoHide()`
- 条件付き依存: `if (win == window)` → `DownloadsIndicatorView.afterCustomize()`
- 参照: `this._customizing`

## init()
- 位置: L212-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `this.checkForAutoHide()`, `this.checkForAutoHide.bind()`

## uninit()
- 位置: L225-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`

## _tabsToolbar()
- 位置: L229-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._tabsToolbar`

## _navBar()
- 位置: L234-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this._navBar`

## ensureInitialized()
- 位置: L269-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.getIndicatorData(window).addView()`, `window.addEventListener()`
- 参照: `this._initialized`

## ensureTerminated()
- 位置: L283-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.getIndicatorData(window).removeView()`, `window.removeEventListener()`
- 参照: `DownloadsCommon.ATTENTION_NONE`, `this._initialized`, `this.attention`, `this.percentComplete`

## _ensureOperational()
- 位置: L303-321
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._initialized)` → `DownloadsCommon.getIndicatorData(window).refreshView()`
- 条件付き依存: `if (this._initialized)` → `DownloadsCommon.getIndicatorData()`
- 参照: `DownloadsButton._placeholder`, `this._initialized`, `this._operational`

## _isAncestorPanelOpen()
- 位置: L342-347
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aNode.localName`, `aNode.parentNode`, `aNode.state`

## showEventNotification()
- 位置: L355-369
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(this._currentNotificationType))` → `this._showNotification()`
- 参照: `this._currentNotificationType`, `this._initialized`, `this._nextNotificationType`

## _showNotification()
- 位置: L378-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchor.addEventListener()`, `anchor.documentGlobal.matchMedia()`, `anchor.documentGlobal.setTimeout()`, `anchor.setAttribute()`, `anchor.toggleAttribute()`, `isElementVisible()`
- 参照: `DownloadsButton._placeholder`, `anchor.documentGlobal.matchMedia("(prefers-reduced-motion)").matches`, `anchor.parentNode`, `this._currentNotificationType`, `this._wasHidden`

## finalize()
- 位置: L402-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchor.documentGlobal.clearTimeout()`, `anchor.removeAttribute()`, `anchor.removeEventListener()`, `isElementVisible()`, `requestAnimationFrame()`
- 条件付き依存: `if (nextType && isElementVisible(anchor.parentNode))` → `this._showNotification()`
- 参照: `anchor.parentNode`, `this._currentNotificationType`, `this._nextNotificationType`

## onNotificationAnimEnd()
- 位置: L425-433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `finalize()`
- 参照: `event.animationName`

## hasDownloads()
- 位置: L451-464
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aValue)` → `DownloadsButton.unhide()`
- 条件付き依存: `if (aValue)` → `this._ensureOperational()`
- 条件付き依存: `if (!(aValue))` → `DownloadsButton.checkForAutoHide()`
- 参照: `this._hasDownloads`, `this._operational`, `this._wasHidden`

## hasDownloads()
- 位置: L465-467
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._hasDownloads`

## percentComplete()
- 位置: L474-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`
- 条件付き依存: `if (this._percentComplete < 0 && aValue >= 0)` → `this.showEventNotification()`
- 条件付き依存: `if (this._percentComplete !== aValue)` → `this._refreshAttention()`
- 条件付き依存: `if (this._percentComplete !== aValue)` → `this._maybeScheduleProgressUpdate()`
- 参照: `this._operational`, `this._percentComplete`

## _maybeScheduleProgressUpdate()
- 位置: L491-519
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( this.indicator && !this._progressRaf && document.visibilityState == "visible" )` → `requestAnimationFrame()`
- 条件付き依存: `if (this._percentComplete >= 0)` → `this.indicator.hasAttribute()`
- 条件付き依存: `if (!this.indicator.hasAttribute("progress"))` → `this.indicator.setAttribute()`
- 条件付き依存: `if (this._percentComplete >= 0)` → `this._progressIcon.style.setProperty()`
- 条件付き依存: `if (this._percentComplete >= 0)` → `Math.max()`
- 条件付き依存: `if (!(this._percentComplete >= 0))` → `this.indicator.removeAttribute()`
- 条件付き依存: `if (!(this._percentComplete >= 0))` → `this._progressIcon.style.setProperty()`
- 参照: `document.visibilityState`, `this._percentComplete`, `this._progressRaf`, `this.indicator`

## attention()
- 位置: L525-533
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._attention != aValue)` → `this._refreshAttention()`
- 参照: `this._attention`, `this._operational`

## _refreshAttention()
- 位置: L535-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`
- 条件付き依存: `if ( suppressAttention || this._attention == DownloadsCommon.ATTENTION_NONE )` → `this.indicator.removeAttribute()`
- 条件付き依存: `if (!( suppressAttention || this._attention == DownloadsCommon.ATTENTION_NONE ))` → `this.indicator.setAttribute()`
- 参照: `CustomizableUI.TYPE_PANEL`, `DownloadsCommon.ATTENTION_NONE`, `DownloadsCommon.ATTENTION_SUCCESS`, `this._attention`, `this._percentComplete`, `widgetGroup.areaType`

## handleEvent()
- 位置: L560-570
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeScheduleProgressUpdate()`, `this.ensureTerminated()`
- 参照: `aEvent.type`

## onCommand()
- 位置: L572-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DownloadsPanel.showPanel()`, `aEvent.stopPropagation()`, `aEvent.type.startsWith()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.key`, `aEvent.type`

## onDragOver()
- 位置: L591-593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ToolbarDropHandler.onDragOver()`

## onDrop()
- 位置: L595-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`, `dt.mozGetDataAt()`, `link.url.startsWith()`, `saveURL()`
- 条件付き依存: `if (handled)` → `aEvent.preventDefault()`
- 参照: `aEvent.dataTransfer`, `dt.mozSourceNode`, `dt.mozSourceNode.ownerDocument`, `link.name`, `link.url`, `links.length`
- XPCOM: `Services.droppedLinkHandler`

## indicator()
- 位置: L640-646
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._indicator)` → `document.getElementById()`
- 参照: `this._indicator`

## indicatorAnchor()
- 位置: L648-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`
- 条件付き依存: `if (widgetGroup.areaType == CustomizableUI.TYPE_PANEL)` → `widgetGroup.forWindow()`
- 参照: `CustomizableUI.TYPE_PANEL`, `overflowIcon.icon`, `this.indicator.badgeStack`, `widgetGroup.areaType`, `widgetGroup.forWindow(window).anchor`

## _progressIcon()
- 位置: L658-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `this.__progressIcon`

## _onCustomizedAway()
- 位置: L667-670
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.__progressIcon`, `this._indicator`

## afterCustomize()
- 位置: L672-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (this._indicator != document.getElementById("downloads-button"))` → `this._onCustomizedAway()`
- 条件付き依存: `if (this._indicator != document.getElementById("downloads-button"))` → `this.ensureTerminated()`
- 条件付き依存: `if (this._indicator != document.getElementById("downloads-button"))` → `this.ensureInitialized()`
- 参照: `this._indicator`, `this._operational`
