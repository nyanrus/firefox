# browser/components/asrouter/modules/ToolbarBadgeHub.sys.mjs

source: browser/components/asrouter/modules/ToolbarBadgeHub.sys.mjs
source-hash: 5289efadec6589b58d0d4b55ae447373f22aeefe
lines: 272

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _ToolbarBadgeHub.constructor()
- 位置: L18-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendPing.bind()`, `this.addToolbarNotification.bind()`, `this.registerBadgeToAllWindows.bind()`, `this.removeAllNotifications.bind()`, `this.removeToolbarNotification.bind()`, `this.sendUserEventTelemetry.bind()`
- 参照: `this._addImpression`, `this._blockMessageById`, `this._handleMessageRequest`, `this._initialized`, `this._sendPing`, `this._sendTelemetry`, `this.addToolbarNotification`, `this.id`, `this.registerBadgeToAllWindows`, `this.removeAllNotifications`, `this.removeToolbarNotification`, `this.sendUserEventTelemetry`, `this.state`

## _ToolbarBadgeHub.init()
- 位置: async L35-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messageRequest()`
- 参照: `this._addImpression`, `this._blockMessageById`, `this._handleMessageRequest`, `this._initialized`, `this._sendTelemetry`, `this._unblockMessageById`

## _ToolbarBadgeHub.maybeInsertFTL()
- 位置: L63-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.MozXULElement.insertFTLIfNeeded()`

## _ToolbarBadgeHub._clearBadgeTimeout()
- 位置: L67-71
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.state.showBadgeTimeoutId)` → `lazy.clearTimeout()`
- 参照: `this.state.showBadgeTimeoutId`

## _ToolbarBadgeHub.removeAllNotifications()
- 位置: L73-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.unregisterCallback()`, `this._clearBadgeTimeout()`
- 条件付き依存: `if (event)` → `event.target.removeEventListener()`
- 条件付き依存: `if (this.state.notification)` → `this.sendUserEventTelemetry()`
- 条件付き依存: `if (this.state.notification)` → `this._blockMessageById()`
- 参照: `event.button`, `event.key`, `event.type`, `this.id`, `this.removeAllNotifications`, `this.state`, `this.state.notification`, `this.state.notification.id`

## _ToolbarBadgeHub.removeToolbarNotification()
- 位置: L111-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolbarButton .querySelector()`, `toolbarButton .querySelector(".toolbarbutton-badge") .classList.remove()`, `toolbarButton.querySelector()`, `toolbarButton.removeAttribute()`
- 条件付き依存: `if (notificationDescription)` → `notificationDescription.remove()`
- 条件付き依存: `if (notificationDescription)` → `toolbarButton.removeAttribute()`

## _ToolbarBadgeHub.addToolbarNotification()
- 位置: L129-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (toolbarbutton)` → `toolbarbutton.querySelector()`
- 条件付き依存: `if (toolbarbutton)` → `badge.classList.add()`
- 条件付き依存: `if (toolbarbutton)` → `toolbarbutton.setAttribute()`
- 条件付き依存: `if (message.content.badgeDescription)` → `this.maybeInsertFTL()`
- 条件付き依存: `if (message.content.badgeDescription)` → `toolbarbutton.setAttribute()`
- 条件付き依存: `if (message.content.badgeDescription)` → `document.createElement()`
- 条件付き依存: `if (message.content.badgeDescription)` → `descriptionEl.setAttribute()`
- 条件付き依存: `if (message.content.badgeDescription)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (message.content.badgeDescription)` → `toolbarbutton.appendChild()`
- 条件付き依存: `if (toolbarbutton)` → `toolbarbutton.addEventListener()`
- 条件付き依存: `if (toolbarbutton)` → `this._addImpression()`
- 条件付き依存: `if (toolbarbutton)` → `this.sendUserEventTelemetry()`
- 参照: `descriptionEl.hidden`, `message.content.badgeDescription`, `message.content.badgeDescription.string_id`, `message.content.target`, `message.id`, `this.removeAllNotifications`, `this.state`, `win.browser.ownerDocument`

## _ToolbarBadgeHub.registerBadgeToAllWindows()
- 位置: L186-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `notificationsByWindow.delete()`, `notificationsByWindow.get()`, `notificationsByWindow.has()`, `notificationsByWindow.set()`, `this.addToolbarNotification()`
- 条件付き依存: `if (el)` → `this.removeToolbarNotification()`
- 参照: `this.id`

## _ToolbarBadgeHub.registerBadgeNotificationListener()
- 位置: L207-224
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options.force)` → `this.removeAllNotifications()`
- 条件付き依存: `if (options.force)` → `this.registerBadgeToAllWindows()`
- 条件付き依存: `if (message.content.delay)` → `lazy.setTimeout()`
- 条件付き依存: `if (message.content.delay)` → `lazy.requestIdleCallback()`
- 条件付き依存: `if (message.content.delay)` → `this.registerBadgeToAllWindows()`
- 条件付き依存: `if (!(message.content.delay))` → `this.registerBadgeToAllWindows()`
- 参照: `message.content.delay`, `options.force`, `this.state.showBadgeTimeoutId`

## _ToolbarBadgeHub.messageRequest()
- 位置: async L226-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.messagingSystem.messageRequestTime.start()`, `Glean.messagingSystem.messageRequestTime.stopAndAccumulate()`, `this._handleMessageRequest()`
- 条件付き依存: `if (message)` → `this.registerBadgeNotificationListener()`

## _ToolbarBadgeHub._sendPing()
- 位置: L238-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendTelemetry()`

## _ToolbarBadgeHub.sendUserEventTelemetry()
- 位置: L245-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if ( win && !lazy.PrivateBrowsingUtils.isBrowserPrivate(win.gBrowser.selectedBrowser) )` → `this._sendPing()`
- 参照: `message.id`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.wm`

## _ToolbarBadgeHub.uninit()
- 位置: L259-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._clearBadgeTimeout()`
- 参照: `this._initialized`, `this.state`
