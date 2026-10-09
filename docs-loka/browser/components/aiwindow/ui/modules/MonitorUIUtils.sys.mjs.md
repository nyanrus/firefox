# browser/components/aiwindow/ui/modules/MonitorUIUtils.sys.mjs

source: browser/components/aiwindow/ui/modules/MonitorUIUtils.sys.mjs
source-hash: b48bd642b3a545ccabee6ca568a3020cdeff45f1
lines: 296

## <module>
- 役割: 監視（Monitor）の UI で共通に使う処理をまとめる。削除の確認、表示用の整形、スケジュールの文言、ページを開く処理、地域の判定を含む。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## deleteMonitorWithConfirmation()
- 位置: async L62-129
- 役割: 削除の確認を出し、確定されたときだけ監視を削除する。成功、削除、取り消しの結果を返す。
- 触るとき: 削除の確認文や取り消し時の扱いを変えるとき。テストでは確認を省ける。
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.deleteMonitor()`
- 条件付き依存: `if (!skipConfirmation)` → `localization.formatValues()`
- 条件付き依存: `if (!skipConfirmation)` → `Services.prompt.asyncConfirmEx()`
- 条件付き依存: `if (!skipConfirmation)` → `result.get()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_INTERNAL_WINDOW`, `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_POS_1_DEFAULT`, `Ci.nsIPromptService.BUTTON_TITLE_CANCEL`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `error.message`
- XPCOM: [`nsIPrompt`](../../../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIPromptService`](../../../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## buildMonitorStatus()
- 位置: L131-138
- 役割: 監視が有効か停止中かを、表示用の kind（watching か paused）で返す。
- 触るとき: 一覧に出す状態の種類を増やすとき。
- 参照: `monitor.enabled`

## formatMonitorForDisplay()
- 位置: L146-171
- 役割: DB から来た監視を、名前・URL・条件・スケジュール・履歴などの表示用の形に変換する。
- 触るとき: パネルやカードに出す項目を変えるとき。
- 呼び出し先: `(monitor.history || []).slice()`, `(monitor.history || []).slice().reverse()`, `(monitor.schedule.hour ?? 0) .toString()`, `(monitor.schedule.hour ?? 0) .toString() .padStart()`, `(monitor.schedule.minute ?? 0) .toString()`, `(monitor.schedule.minute ?? 0) .toString() .padStart()`, `monitor.schedule.weekday?.toString()`, `this.buildMonitorStatus()`
- 参照: `monitor.enabled`, `monitor.history`, `monitor.id`, `monitor.monitorPrompt`, `monitor.schedule`, `monitor.schedule.hour`, `monitor.schedule.minute`, `monitor.schedule.type`, `monitor.title`, `monitor.watchUrls`

## getScheduleL10n()
- 位置: L182-203
- 役割: スケジュールを Fluent の文字列 id と時刻の引数に変える。毎日か毎週かで id を選ぶ。
- 触るとき: スケジュールの文言の選び方や表示する時刻の形を変えるとき。
- 呼び出し先: `Number()`, `Number.isInteger()`, `schedule.time.split()`, `schedule.time.split(":").map()`, `time.getTime()`, `time.setHours()`
- 参照: `SCHEDULE_TYPES.WEEKLY`, `schedule.frequency`, `schedule.weekday`, `schedule?.time`

## openMonitorUrl()
- 位置: L212-252
- 役割: 監視のページを、開いていればそのタブへ、無ければ新しいタブで開く。http と https 以外は拒否する。
- 触るとき: 監視のページを開く条件や、開く場所（タブ、コンテナ）を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `console.error()`, `lazy.URILoadingHelper.switchToTabHavingURI()`
- 条件付き依存: `if ( !lazy.URILoadingHelper.switchToTabHavingURI( chromeWindow, url, false, {} ) )` → `lazy.URILoadingHelper.openWebLinkIn()`
- 条件付き依存: `if ( !lazy.URILoadingHelper.switchToTabHavingURI( chromeWindow, url, false, {} ) )` → `Services.scriptSecurityManager.createNullPrincipal()`
- 参照: `chromeWindow.gBrowser.selectedBrowser.browsingContext .originAttributes`, `error.message`, `uri.scheme`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## resolveWatchUrlTitles()
- 位置: async L261-276
- 役割: 監視の URL ごとに、Places に保存されたページタイトルを取得する。
- 触るとき: 監視のカードでページ名が出ない問題を調べるとき。
- 呼び出し先: `(urls ?? []).map()`, `Promise.all()`, `console.error()`, `lazy.PlacesUtils.history.fetch()`
- 参照: `info.title`, `info?.title`

## isMonitorRegionSupported()
- 位置: L286-294
- 役割: ホームの地域が、設定で指定された対象地域の一覧に入っているかを返す。
- 触るとき: 監視機能を提供する地域を変えるとき。
- 呼び出し先: `Boolean()`, `lazy.Region.home?.toUpperCase()`, `lazy.monitorSupportedRegions .split()`, `lazy.monitorSupportedRegions .split(",") .map()`, `lazy.monitorSupportedRegions .split(",") .map(region => region.trim().toUpperCase()) .filter()`, `region.trim()`, `region.trim().toUpperCase()`, `supportedRegions.includes()`
