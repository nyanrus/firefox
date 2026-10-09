# browser/components/sessionstore/StartupPerformance.sys.mjs

source: browser/components/sessionstore/StartupPerformance.sys.mjs
source-hash: ce5a7af623592758c59937388f750f944e790685
lines: 240

## <module>
- 役割: 起動時のセッション復元が完了するまでの時間を計測し、Glean テレメトリに送るモジュール。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## init()
- 位置: L51-55
- 役割: sessionstore の起動・手動復元の通知を監視し始める。
- 触るとき: 復元計測がいつ開始されるか、監視対象の topic を変えるときに見る。
- 呼び出し先: `Services.obs.addObserver()`
- XPCOM: `Services.obs`

## latestRestoredTimeStamp()
- 位置: L63-65
- 役割: 直近にタブ復元が完了した時刻を返す getter。
- 触るとき: 復元完了時刻を外部から参照するコードを追うとき。
- 参照: `this._latestRestoredTimeStamp`

## isRestored()
- 位置: L70-72
- 役割: 起動時のタブ復元が完了したかを返す getter。
- 触るとき: 復元完了の判定を別の箇所で使うとき。
- 参照: `this._isRestored`

## _onRestorationStarts()
- 位置: L77-133
- 役割: 復元開始時に時刻と統計を初期化し、全タブ復元の Promise を作って完了時に Glean へ時間と件数を送る。
- 触るとき: 復元時間のテレメトリの値がおかしい、または自動復元と手動復元の区別を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Date.now()`, `Glean.sessionRestore.numberOfEagerTabsRestored.accumulateSingleSample()`, `Glean.sessionRestore.numberOfTabsRestored.accumulateSingleSample()`, `Glean.sessionRestore.numberOfWindowsRestored.accumulateSingleSample()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.obs.removeObserver()`, `console.error()`, `this._promiseFinished.then()`
- 条件付き依存: `if (isAutoRestore)` → `Glean.sessionRestore.autoRestoreDurationUntilEagerTabsRestored.accumulateSingleSample()`
- 条件付き依存: `if (!(isAutoRestore))` → `Glean.sessionRestore.manualRestoreDurationUntilEagerTabsRestored.accumulateSingleSample()`
- 参照: `this.RESTORED_TOPIC`, `this._isRestored`, `this._latestRestoredTimeStamp`, `this._promiseFinished`, `this._resolveFinished`, `this._startTimeStamp`, `this._totalNumberOfEagerTabs`, `this._totalNumberOfTabs`, `this._totalNumberOfWindows`
- XPCOM: `Services.obs`

## _startTimer()
- 位置: L135-158
- 役割: COLLECT_RESULTS_AFTER_MS（10秒）の期限タイマーを張り直し、切れたら完了 Promise を解決する。
- 触るとき: ウィンドウが増えるたびに計測の締め切りがどう延びるかを確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `console.error()`, `lazy.setTimeout()`, `this._resolveFinished()`
- 条件付き依存: `if (this._deadlineTimer)` → `lazy.clearTimeout()`
- 参照: `this._deadlineTimer`, `this._hasFired`, `this._resolveFinished`
- XPCOM: `Services.obs`

## observe()
- 位置: L160-238
- 役割: 復元開始・手動復元・ウィンドウ復元の各通知を受け、タイマー更新と SSTabRestored の監視登録を行う。
- 触るとき: 新しい sessionstore の通知を計測に加えるとき、またはウィンドウごとの復元件数がずれるとき。
- 呼び出し先: `console.error()`, `this._onRestorationStarts()`, `this._promiseFinished.then()`, `this._startTimer()`, `win.gBrowser.tabContainer.addEventListener()`, `win.gBrowser.tabContainer.removeEventListener()`
- 参照: `ex.stack`, `this._totalNumberOfTabs`, `this._totalNumberOfWindows`, `win.gBrowser.tabContainer`, `win.gBrowser.tabContainer.itemCount`

## observer()
- 位置: L207-211
- 役割: SSTabRestored イベントごとに最新復元時刻を更新し、復元済みタブ数を増やす。
- 触るとき: タブ復元の完了時刻が早すぎる、または遅すぎる値になる原因を調べるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Date.now()`
- 参照: `this._latestRestoredTimeStamp`, `this._totalNumberOfEagerTabs`
