# browser/modules/ProcessHangMonitor.sys.mjs

source: browser/modules/ProcessHangMonitor.sys.mjs
source-hash: 2c9b2a18e7aa5a0819a3319acf934eef63f3b848
lines: 698

## <module>
- 役割: (未記入)

## elideMiddleOfString()
- 位置: L12-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchElisionPoint()`
- 条件付き依存: `if (elisionStart < elisionEnd)` → `str.slice()`
- 参照: `str.length`

## searchElisionPoint()
- 位置: L19-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `unsplittableCharacter()`

## unsplittableCharacter()
- 位置: L20-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/[\p{M}\uDC00-\uDFFF]/u.test()`

## WAIT_EXPIRATION_TIME()
- 位置: L52-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- XPCOM: `Services.prefs`

## init()
- 位置: L88-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.ww.registerNotification()`
- XPCOM: `Services.obs` / `Services.ww`

## terminateScript()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `report.terminateScript()`, `this.handleUserInput()`

## debugScript()
- 位置: L108-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/dom/slow-script-debug;1"].getService()`, `handler.handleSlowScriptDebug()`, `report.beginStartingDebugger()`, `this._recordTelemetryForReport()`, `this.handleUserInput()`
- 参照: `Ci.nsISlowScriptDebug`, `report.scriptBrowser`, `svc.remoteActivationHandler`
- XPCOM: [`nsISlowScriptDebug`](../../dom/base/nsISlowScriptDebug.idl.md) / `@mozilla.org/dom/slow-script-debug;1` → `SlowScriptDebug` (dom/base/components.conf)

## callback()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `report.endStartingDebugger()`

## stopIt()
- 位置: L129-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._recordTelemetryForReport()`, `this.findActiveReport()`, `this.terminateScript()`
- 参照: `win.gBrowser.selectedBrowser`

## stopHang()
- 位置: L143-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `report.terminateScript()`, `this._recordTelemetryForReport()`

## waitLonger()
- 位置: L152-194
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `this._activeReports.get()`, `this._pausedReports.set()`, `this.findActiveReport()`, `this.removeActiveReport()`, `this.updateWindows()`, `timer.initWithCallback()`
- 条件付き依存: `if (pausedInfo.timer === timer)` → `this.removePausedReport()`
- 条件付き依存: `if (pausedInfo.timer === timer)` → `this._activeReports.set()`
- 条件付き依存: `if (pausedInfo.timer === timer)` → `this.updateWindows()`
- 参照: `Ci.nsITimer`, `pausedInfo.timer`, `reportInfo.timer`, `reportInfo.waitCount`, `this.WAIT_EXPIRATION_TIME`, `this._pausedReports`, `timer.TYPE_ONE_SHOT`, `win.gBrowser.selectedBrowser`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## handleUserInput()
- 位置: L201-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `func()`, `this.findActiveReport()`, `this.removeActiveReport()`
- 参照: `win.gBrowser.selectedBrowser`

## observe()
- 位置: L211-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.ww.unregisterNotification()`, `subject.QueryInterface()`, `this.clearHang()`, `this.onQuitApplicationGranted()`, `this.onWindowClosed()`, `this.reportHang()`, `win.addEventListener()`
- 参照: `Ci.nsIHangReport`
- XPCOM: [`nsIHangReport`](../../dom/ipc/nsIHangReport.idl.md) / `Services.obs` / `Services.ww`

## listener()
- 位置: L241-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateWindows()`, `win.removeEventListener()`

## onQuitApplicationGranted()
- 位置: L263-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stopAllHangs()`, `this.updateWindows()`
- 参照: `this._shuttingDown`

## onWindowClosed()
- 位置: L269-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `maybeStopHang()`, `this.updateWindows()`
- 条件付き依存: `if (maybeStopHang(report))` → `this._activeReports.delete()`
- 条件付き依存: `if (maybeStopHang(pausedReport))` → `this.removePausedReport()`
- 参照: `this._activeReports`, `this._pausedReports`

## maybeStopHang()
- 位置: L270-285
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!hungBrowserWindow || hungBrowserWindow == win)` → `this.stopHang()`
- 参照: `report.scriptBrowser.documentGlobal`

## stopAllHangs()
- 位置: L304-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removePausedReport()`, `this.stopHang()`
- 参照: `this._activeReports`, `this._pausedReports`

## findActiveReport()
- 位置: L320-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `report.isReportForBrowserOrChildren()`, `this._activeReports.keys()`
- 参照: `browser.frameLoader`

## findPausedReport()
- 位置: L333-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `report.isReportForBrowserOrChildren()`
- 参照: `browser.frameLoader`, `this._pausedReports`

## _recordTelemetryForReport()
- 位置: L346-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.slowScriptWarning.shownContent.record()`, `console.error()`, `this._activeReports.get()`, `this._pausedReports.get()`
- 条件付き依存: `if (!(report.addonId))` → `report.scriptFileName?.startsWith()`
- 条件付き依存: `if (!(report.scriptFileName?.startsWith("debugger")))` → `report.scriptFileName?.startsWith()`
- 条件付き依存: `if (!( report.scriptFileName?.startsWith( "resource://pdf.js/build/pdf.scripting.mjs" ) ))` → `console.error()`
- 条件付き依存: `if (info.notificationTime)` → `ChromeUtils.now()`
- 参照: `info.deselectCount`, `info.lastReportFromChild`, `info.notificationTime`, `info.waitCount`, `report.addonId`, `report.hangDuration`, `report.scriptFileName`, `url.protocol`

## removeActiveReport()
- 位置: L411-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._activeReports.delete()`, `this.updateWindows()`

## removePausedReport()
- 位置: L420-424
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info?.timer?.cancel()`, `this._pausedReports.delete()`, `this._pausedReports.get()`

## updateWindows()
- 位置: L432-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `e.hasMoreElements()`, `this.updateWindow()`
- 条件付き依存: `if (!e.hasMoreElements())` → `this.stopAllHangs()`
- 条件付き依存: `if (this._activeReports.size)` → `this.trackWindow()`
- 条件付き依存: `if (!(this._activeReports.size))` → `this.untrackWindow()`
- 参照: `this._activeReports.size`
- XPCOM: `Services.wm`

## updateWindow()
- 位置: L458-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findActiveReport()`
- 条件付き依存: `if (report)` → `this._activeReports.get()`
- 条件付き依存: `if (info && !info.notificationTime)` → `ChromeUtils.now()`
- 条件付き依存: `if (report)` → `this.showNotification()`
- 条件付き依存: `if (!(report))` → `this.hideNotification()`
- 参照: `info.notificationTime`, `win.gBrowser.selectedBrowser`

## showNotification()
- 位置: async L475-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `bundle.getString()`, `console.warn()`, `doc .getElementById()`, `doc .getElementById("bundle_brand") .getString()`, `hangNotification.setAttribute()`, `notification?.getAttribute()`, `win.gNotificationBox.appendNotification()`, `win.gNotificationBox.getNotificationWithValue()`
- 条件付き依存: `if (report.addonId)` → `Cc["@mozilla.org/addons/policy-service;1"].getService()`
- 条件付き依存: `if (report.addonId)` → `aps.getExtensionName()`
- 条件付き依存: `if (report.addonId)` → `bundle.getFormattedString()`
- 条件付き依存: `if (report.addonId)` → `buttons.unshift()`
- 条件付き依存: `if (report.addonId)` → `bundle.getString()`
- 条件付き依存: `if (scriptBrowser == win.gBrowser?.selectedBrowser)` → `bundle.getFormattedString()`
- 条件付き依存: `if (!(scriptBrowser == win.gBrowser?.selectedBrowser))` → `scriptBrowser?.documentGlobal.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (!tab)` → `bundle.getFormattedString()`
- 条件付き依存: `if (!(!tab))` → `scriptBrowser.browserId.toString()`
- 条件付き依存: `if (!(!tab))` → `tab.getAttribute()`
- 条件付き依存: `if (!(!tab))` → `elideMiddleOfString()`
- 条件付き依存: `if (!(!tab))` → `bundle.getFormattedString()`
- 条件付き依存: `if (notification)` → `notification.setAttribute()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("devtools.policy.disabled", false) && (AppConstants.MOZ_DEV_EDITION || AppConstants.NIGHTLY_BUILD || report.scriptBrowser.browsi...)` → `buttons.push()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref("devtools.policy.disabled", false) && (AppConstants.MOZ_DEV_EDITION || AppConstants.NIGHTLY_BUILD || report.scriptBrowser.browsi...)` → `bundle.getString()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `AppConstants.NIGHTLY_BUILD`, `Ci.nsIAddonPolicyService`, `notification.label`, `report.addonId`, `report.scriptBrowser`, `report.scriptBrowser.browsingContext.watchedByDevTools`, `win.document`, `win.gBrowser?.selectedBrowser`, `win.gNavigatorBundle`, `win.gNotificationBox.PRIORITY_INFO_HIGH`
- XPCOM: `nsIAddonPolicyService` / `@mozilla.org/addons/policy-service;1` / `Services.prefs`

## callback()
- 位置: L482-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProcessHangMonitor.stopIt()`

## callback()
- 位置: L565-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ProcessHangMonitor.debugScript()`

## eventCallback()
- 位置: L580-584
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event == "dismissed")` → `ProcessHangMonitor.waitLonger()`

## hideNotification()
- 位置: L597-603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `win.gNotificationBox.removeNotification()`

## trackWindow()
- 位置: L609-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.tabContainer.addEventListener()`

## untrackWindow()
- 位置: L618-625
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gBrowser.tabContainer.removeEventListener()`

## handleEvent()
- 位置: L627-646
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type == "TabSelect" && event.detail.previousTab)` → `this.findActiveReport()`
- 条件付き依存: `if (event.type == "TabSelect" && event.detail.previousTab)` → `this.findPausedReport()`
- 条件付き依存: `if (r)` → `this._activeReports.get()`
- 条件付き依存: `if (r)` → `this._pausedReports.get()`
- 条件付き依存: `if (event.type == "TabSelect" || event.type == "TabRemotenessChange")` → `this.updateWindow()`
- 参照: `event.detail.previousTab`, `event.detail.previousTab.linkedBrowser`, `event.target.documentGlobal`, `event.type`, `info.deselectCount`

## reportHang()
- 位置: L652-688
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `Glean.dom.slowScriptNoticeCount.add()`, `this._activeReports.has()`, `this._activeReports.set()`, `this._pausedReports.has()`, `this.updateWindows()`
- 条件付き依存: `if (this._shuttingDown)` → `this.stopHang()`
- 条件付き依存: `if (this._activeReports.has(report))` → `this._activeReports.get()`
- 条件付き依存: `if (this._activeReports.has(report))` → `this.updateWindows()`
- 条件付き依存: `if (this._pausedReports.has(report))` → `this._pausedReports.get()`
- 参照: `this._activeReports.get(report).lastReportFromChild`, `this._pausedReports.get(report).lastReportFromChild`, `this._shuttingDown`

## clearHang()
- 位置: L690-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `report.userCanceled()`, `this._recordTelemetryForReport()`, `this.removeActiveReport()`, `this.removePausedReport()`
