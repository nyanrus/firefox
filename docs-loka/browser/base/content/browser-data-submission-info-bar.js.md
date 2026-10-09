# browser/base/content/browser-data-submission-info-bar.js

source: browser/base/content/browser-data-submission-info-bar.js
source-hash: 42f9a68ccdf81e33a37211dd9f2710f49a03d03c
lines: 124

## <module>
- 役割: データ送信ポリシーの通知を情報バーとして表示し、ユーザーが応答したことを datareporting へ知らせる gDataNotificationInfoBar を定義する。
- 呼び出し先: `ChromeUtils.generateQI()`

## _log()
- 位置: L16-25
- 役割: Toolkit.Telemetry 用のログ出力係を初回アクセス時に作ってキャッシュする。
- 触るとき: この情報バーのログ出力の接頭辞や出力先を変えるとき。
- 呼び出し先: `ChromeUtils.importESModule()`, `Log.repository.getLoggerWithMessagePrefix()`
- 参照: `this._log`

## init()
- 位置: L27-37
- 役割: datareporting のポリシー要求・クローズ通知を監視し、ウィンドウ unload 時に監視を外す。
- 触るとき: データ送信通知の監視トピックを変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `window.addEventListener()`
- 参照: `this._OBSERVERS`
- XPCOM: `Services.obs`

## _getDataReportingNotification()
- 位置: L39-41
- 役割: data-reporting という値の通知を通知ボックスから探して返す。
- 触るとき: データ送信通知の検索条件を変えるとき。
- 呼び出し先: `gNotificationBox.getNotificationWithValue()`
- 参照: `this._DATA_REPORTING_NOTIFICATION`

## _displayDataPolicyInfoBar()
- 位置: async L43-85
- 役割: 未表示なら情報バーとボタンを出し、表示できた時点で onUserNotifyComplete を呼ぶ。
- 触るとき: データ送信ポリシー通知の文言、ボタン、表示完了の扱いを変えるとき。
- 呼び出し先: `gNotificationBox.appendNotification()`, `request.onUserNotifyComplete()`, `this._getDataReportingNotification()`, `this._log.info()`
- 参照: `gNotificationBox.PRIORITY_INFO_HIGH`, `this._DATA_REPORTING_NOTIFICATION`, `this._actionTaken`

## callback()
- 位置: L54-57
- 役割: 通知のボタン押下でプライバシー設定の報告欄を開き、操作済みフラグを立てる。
- 触るとき: 通知ボタンから開く設定画面を変えるとき。
- 呼び出し先: `window.openPreferences()`
- 参照: `this._actionTaken`

## eventCallback()
- 位置: L69-76
- 役割: 通知が閉じられたとき datareporting:notify-data-policy:close を発行する。
- 触るとき: 通知を閉じた時に他へ伝える通知の仕組みを変えるとき。
- 条件付き依存: `if (event == "removed")` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## _clearPolicyNotification()
- 位置: L87-93
- 役割: 表示中のデータ送信通知があれば閉じる。
- 触るとき: 外部から応答済みになった時の通知の後始末を変えるとき。
- 呼び出し先: `this._getDataReportingNotification()`
- 条件付き依存: `if (notification)` → `this._log.debug()`
- 条件付き依存: `if (notification)` → `notification.close()`

## observe()
- 位置: L95-117
- 役割: ポリシー要求で通知を表示し、クローズ通知で操作済みにして通知を消す。
- 触るとき: データ送信ポリシーのトピック処理を変えるとき。
- 呼び出し先: `request.onUserNotifyFailed()`, `this._clearPolicyNotification()`, `this._displayDataPolicyInfoBar()`
- 参照: `subject.wrappedJSObject.object`, `this._actionTaken`
