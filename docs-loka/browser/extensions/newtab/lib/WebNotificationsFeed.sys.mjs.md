# browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs

source: browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs
source-hash: f9d0902c624083ec71f37e7ad00a3ee4223dc299
lines: 511

## <module>
- 役割: (未記入)

## readNotificationStore()
- 位置: async L104-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DOMException.isInstance()`, `IOUtils.readUTF8()`, `JSON.parse()`, `PathUtils.join()`
- 参照: `PathUtils.profileDir`, `e.name`, `text.length`

## normalizeDiskEntry()
- 位置: L127-135
- 役割: (未記入)
- 触るとき: (未記入)

## WebNotificationsFeed.constructor()
- 位置: L166-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`
- 参照: `this._byOrigin`, `this._notifications`, `this._observing`

## WebNotificationsFeed._broadcast()
- 位置: L174-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`

## WebNotificationsFeed._byOriginSnapshot()
- 位置: L179-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.create()`
- 参照: `this._byOrigin`

## WebNotificationsFeed._add()
- 位置: L188-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ids.add()`, `this._byOrigin.get()`
- 条件付き依存: `if (!ids)` → `this._byOrigin.set()`
- 参照: `this._notifications`

## WebNotificationsFeed._remove()
- 位置: L204-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._byOrigin.get()`
- 条件付き依存: `if (ids)` → `ids.delete()`
- 条件付き依存: `if (!ids.size)` → `this._byOrigin.delete()`
- 参照: `ids.size`, `this._notifications`

## WebNotificationsFeed._seedFromDisk()
- 位置: async L219-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Object.keys()`, `String()`, `normalizeDiskEntry()`, `readNotificationStore()`, `this._add()`, `this._broadcast()`, `this._byOriginSnapshot()`
- 参照: `at.WEB_NOTIFICATIONS_ERROR`, `at.WEB_NOTIFICATIONS_UPDATED`, `this._notifications`

## WebNotificationsFeed._answer()
- 位置: L249-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `ac.AlsoToOneContent()`, `this._byOriginSnapshot()`, `this.store.dispatch()`
- 参照: `at.WEB_NOTIFICATIONS_UPDATED`, `this._notifications`

## WebNotificationsFeed.observe()
- 位置: L267-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subject?.QueryInterface()`
- 条件付き依存: `if (topic === TOPIC_SHOWN)` → `this._add()`
- 条件付き依存: `if (topic === TOPIC_SHOWN)` → `this._normalizeAlert()`
- 条件付き依存: `if (topic === TOPIC_SHOWN)` → `this._broadcast()`
- 条件付き依存: `if (topic === TOPIC_CLOSED)` → `this._shouldReleaseOnClose()`
- 条件付き依存: `if (topic === TOPIC_CLOSED)` → `this._remove()`
- 条件付き依存: `if ( existing && this._shouldReleaseOnClose(existing) && this._remove(origin, alert.id) )` → `this._broadcast()`
- 参照: `Ci.nsIAlertNotification`, `alert.id`, `alert.principal?.origin`, `at.WEB_NOTIFICATIONS_ADDED`, `at.WEB_NOTIFICATIONS_REMOVED`, `this._notifications`
- XPCOM: [`nsIAlertNotification`](../../../../toolkit/components/alerts/nsIAlertsService.idl.md)

## WebNotificationsFeed._shouldReleaseOnClose()
- 位置: L316-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `STICKY_ORIGINS.has()`
- 参照: `notification.origin`

## WebNotificationsFeed._normalizeAlert()
- 位置: L325-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 参照: `alert.dir`, `alert.id`, `alert.imageURL`, `alert.requireInteraction`, `alert.text`, `alert.title`

## WebNotificationsFeed._principalFor()
- 位置: L338-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- XPCOM: `Services.scriptSecurityManager`

## WebNotificationsFeed._click()
- 位置: L354-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._principalFor()`, `this._remove()`
- 条件付き依存: `if (principal)` → `Cc[NOTIFICATION_HANDLER].getService(Ci.nsINotificationHandler) .respondOnClick()`
- 条件付き依存: `if (principal)` → `Cc[NOTIFICATION_HANDLER].getService()`
- 条件付き依存: `if (this._remove(origin, id))` → `this._broadcast()`
- 参照: `Ci.nsINotificationHandler`, `at.WEB_NOTIFICATIONS_REMOVED`
- XPCOM: [`nsINotificationHandler`](../../../../dom/notification/nsINotificationHandler.idl.md)

## WebNotificationsFeed._dismiss()
- 位置: L378-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ALERTS_SERVICE].getService()`, `Cc[ALERTS_SERVICE].getService(Ci.nsIAlertsService).closeAlert()`, `Cc[NOTIFICATION_STORAGE].getService()`, `Cc[NOTIFICATION_STORAGE].getService(Ci.nsINotificationStorage).delete()`, `this._remove()`
- 条件付き依存: `if (this._remove(origin, id))` → `this._broadcast()`
- 参照: `Ci.nsIAlertsService`, `Ci.nsINotificationStorage`, `at.WEB_NOTIFICATIONS_REMOVED`, `this._notifications`
- XPCOM: [`nsIAlertsService`](../../../../toolkit/components/alerts/nsIAlertsService.idl.md) / [`nsINotificationStorage`](../../../../dom/interfaces/notification/nsINotificationStorage.idl.md)

## WebNotificationsFeed._dismissAll()
- 位置: L404-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this._dismiss()`
- 条件付き依存: `if (!origin || entry.origin === origin)` → `targets.push()`
- 参照: `entry.origin`, `this._notifications`

## WebNotificationsFeed._enabled()
- 位置: L422-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `this.store.getState()`
- 参照: `prefs.trainhopConfig?.webNotifications?.enabled`, `this.store.getState().Prefs.values`

## WebNotificationsFeed._startObserving()
- 位置: L429-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this._observing`
- XPCOM: `Services.obs`

## WebNotificationsFeed._stopObserving()
- 位置: L438-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this._observing`
- XPCOM: `Services.obs`

## WebNotificationsFeed._clear()
- 位置: L448-459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Object.create()`, `this._broadcast()`, `this._byOrigin.clear()`
- 参照: `at.WEB_NOTIFICATIONS_UPDATED`, `this._notifications`

## WebNotificationsFeed._updateEnabled()
- 位置: L467-477
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._observing)` → `this._startObserving()`
- 条件付き依存: `if (!this._observing)` → `this._seedFromDisk()`
- 条件付き依存: `if (this._observing)` → `this._stopObserving()`
- 条件付き依存: `if (this._observing)` → `this._clear()`
- 参照: `this._enabled`, `this._observing`

## WebNotificationsFeed.onAction()
- 位置: L479-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._answer()`, `this._click()`, `this._dismiss()`, `this._dismissAll()`, `this._stopObserving()`, `this._updateEnabled()`
- 条件付き依存: `if ( action.data.name === PREF_SYSTEM || action.data.name === PREF_USER || action.data.name === "trainhopConfig" )` → `this._updateEnabled()`
- 参照: `action.data`, `action.data.name`, `action.meta?.fromTarget`, `action.type`, `at.INIT`, `at.PREF_CHANGED`, `at.UNINIT`, `at.WEB_NOTIFICATIONS_CLICK`, `at.WEB_NOTIFICATIONS_DISMISS`, `at.WEB_NOTIFICATIONS_DISMISS_ALL`, `at.WEB_NOTIFICATIONS_REQUEST`
