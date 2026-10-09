# browser/extensions/newtab/content-src/lib/web-notification-match.mjs

source: browser/extensions/newtab/content-src/lib/web-notification-match.mjs
source-hash: 7124f0fcef8d8088d27c6f2aa6f38ab092ac4aa8
lines: 83

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## originFromUrl()
- 位置: L26-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `parsed.origin`, `parsed.protocol`

## notificationKeyForUrl()
- 位置: L46-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ORIGIN_ALIASES.get()`, `originFromUrl()`

## getNotificationIdsForUrl()
- 位置: L61-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationKeyForUrl()`
- 参照: `state.WebNotifications.byOrigin`

## isWebNotificationsEnabled()
- 位置: L76-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `prefs.showWebNotifications`, `prefs.trainhopConfig?.webNotifications?.enabled`, `state.Prefs.values`
