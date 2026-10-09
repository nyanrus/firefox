# browser/base/content/browser-data-submission-info-bar.js

source: browser/base/content/browser-data-submission-info-bar.js
source-hash: 42f9a68ccdf81e33a37211dd9f2710f49a03d03c
lines: 124

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## _log()
- 位置: L16-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Log.repository.getLoggerWithMessagePrefix()`
- 参照: `this._log`

## init()
- 位置: L27-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `window.addEventListener()`
- 参照: `this._OBSERVERS`
- XPCOM: `Services.obs`

## _getDataReportingNotification()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNotificationBox.getNotificationWithValue()`
- 参照: `this._DATA_REPORTING_NOTIFICATION`

## _displayDataPolicyInfoBar()
- 位置: async L43-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gNotificationBox.appendNotification()`, `request.onUserNotifyComplete()`, `this._getDataReportingNotification()`, `this._log.info()`
- 参照: `gNotificationBox.PRIORITY_INFO_HIGH`, `this._DATA_REPORTING_NOTIFICATION`, `this._actionTaken`

## callback()
- 位置: L54-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.openPreferences()`
- 参照: `this._actionTaken`

## eventCallback()
- 位置: L69-76
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event == "removed")` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## _clearPolicyNotification()
- 位置: L87-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getDataReportingNotification()`
- 条件付き依存: `if (notification)` → `this._log.debug()`
- 条件付き依存: `if (notification)` → `notification.close()`

## observe()
- 位置: L95-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `request.onUserNotifyFailed()`, `this._clearPolicyNotification()`, `this._displayDataPolicyInfoBar()`
- 参照: `subject.wrappedJSObject.object`, `this._actionTaken`
