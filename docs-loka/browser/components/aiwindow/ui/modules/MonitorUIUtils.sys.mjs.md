# browser/components/aiwindow/ui/modules/MonitorUIUtils.sys.mjs

source: browser/components/aiwindow/ui/modules/MonitorUIUtils.sys.mjs
source-hash: b48bd642b3a545ccabee6ca568a3020cdeff45f1
lines: 296

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## deleteMonitorWithConfirmation()
- 位置: async L62-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.deleteMonitor()`
- 条件付き依存: `if (!skipConfirmation)` → `localization.formatValues()`
- 条件付き依存: `if (!skipConfirmation)` → `Services.prompt.asyncConfirmEx()`
- 条件付き依存: `if (!skipConfirmation)` → `result.get()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_INTERNAL_WINDOW`, `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_POS_1_DEFAULT`, `Ci.nsIPromptService.BUTTON_TITLE_CANCEL`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `error.message`
- XPCOM: [`nsIPrompt`](../../../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIPromptService`](../../../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## buildMonitorStatus()
- 位置: L131-138
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `monitor.enabled`

## formatMonitorForDisplay()
- 位置: L146-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(monitor.history || []).slice()`, `(monitor.history || []).slice().reverse()`, `(monitor.schedule.hour ?? 0) .toString()`, `(monitor.schedule.hour ?? 0) .toString() .padStart()`, `(monitor.schedule.minute ?? 0) .toString()`, `(monitor.schedule.minute ?? 0) .toString() .padStart()`, `monitor.schedule.weekday?.toString()`, `this.buildMonitorStatus()`
- 参照: `monitor.enabled`, `monitor.history`, `monitor.id`, `monitor.monitorPrompt`, `monitor.schedule`, `monitor.schedule.hour`, `monitor.schedule.minute`, `monitor.schedule.type`, `monitor.title`, `monitor.watchUrls`

## getScheduleL10n()
- 位置: L182-203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `Number.isInteger()`, `schedule.time.split()`, `schedule.time.split(":").map()`, `time.getTime()`, `time.setHours()`
- 参照: `SCHEDULE_TYPES.WEEKLY`, `schedule.frequency`, `schedule.weekday`, `schedule?.time`

## openMonitorUrl()
- 位置: L212-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `console.error()`, `lazy.URILoadingHelper.switchToTabHavingURI()`
- 条件付き依存: `if ( !lazy.URILoadingHelper.switchToTabHavingURI( chromeWindow, url, false, {} ) )` → `lazy.URILoadingHelper.openWebLinkIn()`
- 条件付き依存: `if ( !lazy.URILoadingHelper.switchToTabHavingURI( chromeWindow, url, false, {} ) )` → `Services.scriptSecurityManager.createNullPrincipal()`
- 参照: `chromeWindow.gBrowser.selectedBrowser.browsingContext .originAttributes`, `error.message`, `uri.scheme`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## resolveWatchUrlTitles()
- 位置: async L261-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(urls ?? []).map()`, `Promise.all()`, `console.error()`, `lazy.PlacesUtils.history.fetch()`
- 参照: `info.title`, `info?.title`

## isMonitorRegionSupported()
- 位置: L286-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `lazy.Region.home?.toUpperCase()`, `lazy.monitorSupportedRegions .split()`, `lazy.monitorSupportedRegions .split(",") .map()`, `lazy.monitorSupportedRegions .split(",") .map(region => region.trim().toUpperCase()) .filter()`, `region.trim()`, `region.trim().toUpperCase()`, `supportedRegions.includes()`
