# browser/base/content/aboutDialog-appUpdater.js

source: browser/base/content/aboutDialog-appUpdater.js
source-hash: 879b827299c0231c08f1a4fd41750ad14712563c
lines: 323

## <module>
- 役割: about:dialog と設定画面の「バージョン情報」で使う更新 UI の制御。AppUpdater の状態を受けて、更新パネルの切り替えと再起動処理を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetter()`

## onUnload()
- 位置: L31-36
- 役割: ページを閉じるとき、更新 UI の AppUpdater を破棄して参照を外す。
- 触るとき: ダイアログを閉じた後に更新チェックが動き続けるときに見る。
- 条件付き依存: `if (gAppUpdater)` → `gAppUpdater.destroy()`

## appUpdater()
- 位置: L38-76
- 役割: AppUpdater を作って状態リスナーを登録し、手動更新リンクを設定してから更新チェックを始める。
- 触るとき: 更新 UI の初期化の流れや、オプションの受け取り方を変えるとき。
- 呼び出し先: `Services.strings.createBundle()`, `document.getElementById()`, `this._appUpdater.addListener()`, `this._appUpdater.check()`
- 条件付き依存: `if (this.updateDeck)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (this.updateDeck)` → `document.querySelectorAll()`
- 条件付き依存: `if (this.updateDeck)` → `document.l10n.setArgs()`
- 条件付き依存: `if (this.updateDeck)` → `manualLink.closest()`
- 条件付き依存: `if (this.updateDeck)` → `document.getElementById()`
- 条件付き依存: `if (this.updateDeck)` → `console.error()`
- 参照: `document.getElementById("failedLink").href`, `manualLink.href`, `manualURL.href`, `manualURL.origin`, `manualURL.pathname`, `this._appUpdateListener`, `this._appUpdater`, `this.bundle`, `this.options`, `this.updateDeck`, `this.updatingMinDisplayTimerId`
- XPCOM: `Services.strings` / `Services.urlFormatter`

## this._appUpdateListener()
- 位置: L41-43
- 役割: AppUpdater の状態通知を _onAppUpdateStatus へ転送する。
- 触るとき: 状態通知の受け口を変えるとき。
- 呼び出し先: `this._onAppUpdateStatus()`

## destroy()
- 位置: L79-84
- 役割: 進行中のチェックを止め、最小表示時間のタイマーを解除する。
- 触るとき: 更新 UI を破棄した後にタイマーが残る問題を調べるとき。
- 呼び出し先: `this.stopCurrentCheck()`
- 条件付き依存: `if (this.updatingMinDisplayTimerId)` → `clearTimeout()`
- 参照: `this.updatingMinDisplayTimerId`

## stopCurrentCheck()
- 位置: L86-89
- 役割: リスナーを外して AppUpdater の確認を止める。
- 触るとき: 更新チェックを途中で止める経路を調べるとき。
- 呼び出し先: `this._appUpdater.removeListener()`, `this._appUpdater.stop()`
- 参照: `this._appUpdateListener`

## update()
- 位置: L91-93
- 役割: AppUpdater が保持している現在の更新情報を返す。
- 触るとき: 更新パネルで表示するバージョン等を参照するとき。
- 参照: `this._appUpdater.update`

## selectedPanel()
- 位置: L95-97
- 役割: 更新デッキで今選ばれているパネルを返す。
- 触るとき: どの更新状態のパネルが表示中かを確認するとき。
- 参照: `this.updateDeck?.selectedPanel`

## _onAppUpdateStatus()
- 位置: L99-199
- 役割: AppUpdater の各ステータスを、表示すべき更新パネルに対応づける。ダウンロード進捗も表示に反映する。
- 触るとき: 更新状態ごとの表示を追加・変更するとき。
- 呼び出し先: `Services.policies.isAllowed()`, `document.getElementById()`, `setTimeout()`, `this.checkingForUpdatesDelayPromise.then()`, `this.selectPanel()`
- 条件付き依存: `if (!args.length)` → `DownloadUtils.getTransferTotal()`
- 条件付き依存: `if (downloadStatus)` → `document.l10n.setArgs()`
- 条件付き依存: `if (!args.length)` → `this.selectPanel()`
- 条件付き依存: `if (!(!args.length))` → `DownloadUtils.getTransferTotal()`
- 条件付き依存: `if (!(downloadStatus))` → `this.selectPanel()`
- 条件付き依存: `if (Services.policies.isAllowed("appUpdate"))` → `this.selectPanel()`
- 条件付き依存: `if (!(Services.policies.isAllowed("appUpdate")))` → `this.selectPanel()`
- 条件付き依存: `if (this.updateDeck)` → `document.getElementById()`
- 条件付き依存: `if (this.update.detailsURL)` → `this.selectPanel()`
- 条件付き依存: `if (!(this.update.detailsURL))` → `this.selectPanel()`
- 参照: `AppUpdater.STATUS.CHECKING`, `AppUpdater.STATUS.CHECKING_FAILED`, `AppUpdater.STATUS.DOWNLOADING`, `AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `AppUpdater.STATUS.DOWNLOAD_FAILED`, `AppUpdater.STATUS.INTERNAL_ERROR`, `AppUpdater.STATUS.MANUAL_UPDATE`, `AppUpdater.STATUS.NEVER_CHECKED`, `AppUpdater.STATUS.NO_UPDATER`, `AppUpdater.STATUS.NO_UPDATES_FOUND`, `AppUpdater.STATUS.OTHER_INSTANCE_HANDLING_UPDATES`, `AppUpdater.STATUS.READY_FOR_RESTART`, `AppUpdater.STATUS.STAGING`, `AppUpdater.STATUS.UNSUPPORTED_SYSTEM`, `AppUpdater.STATUS.UPDATE_DISABLED_BY_POLICY`, `args.length`, `this.checkingForUpdatesDelayPromise`, `this.update.detailsURL`, `this.update.selectedPatch`, `this.update.selectedPatch.size`, `this.updateDeck`, `this.updatingMinDisplayTimerId`, `unsupportedLink.href`
- XPCOM: `Services.policies`

## selectPanel()
- 位置: L207-264
- 役割: 指定パネルを表示し、アイコンとボタンの文言を更新する。ダウンロード時はバージョンと nightly のビルド日を付ける。カスタムの selectPanel があればそちらへ渡す。
- 触るとき: 更新パネルの表示やボタンのラベル、自動フォーカスを変えるとき。
- 呼び出し先: `document.getElementById()`, `panel.querySelector()`
- 条件付き依存: `if (aChildID == "downloadAndInstall")` → `/a\d+$/.test()`
- 条件付き依存: `if (/a\d+$/.test(updateVersion))` → `buildID.slice()`
- 条件付き依存: `if (typeof this.options.selectPanel === "function")` → `this.options.selectPanel()`
- 条件付き依存: `if (aChildID == "downloadAndInstall")` → `this.bundle.formatStringFromName()`
- 条件付き依存: `if (aChildID == "downloadAndInstall")` → `this.bundle.GetStringFromName()`
- 条件付き依存: `if (this.options.buttonAutoFocus)` → `Promise.resolve()`
- 条件付き依存: `if (document.readyState != "complete")` → `window.addEventListener()`
- 条件付き依存: `if (this.options.buttonAutoFocus)` → `promise.then()`
- 条件付き依存: `if ( !document.commandDispatcher.focusedElement || // don't steal the focus // except from the other buttons document.commandDispatcher.focusedElement.localName ...)` → `button.focus()`
- 参照: `button.accessKey`, `button.label`, `document.commandDispatcher.focusedElement`, `document.commandDispatcher.focusedElement.localName`, `document.readyState`, `gAppUpdater.update.buildID`, `gAppUpdater.update.displayVersion`, `icon.className`, `this.options.buttonAutoFocus`, `this.options.selectPanel`, `this.updateDeck.selectedPanel`

## checkForUpdates()
- 位置: L269-271
- 役割: AppUpdater に更新チェックを依頼する。
- 触るとき: 手動の再チェック操作の経路を調べるとき。
- 呼び出し先: `this._appUpdater.check()`

## buttonRestartAfterDownload()
- 位置: L277-314
- 役割: 更新適用の再起動ボタンの処理。終了要求を各ウィンドウに通知し、中断されたら適用パネルに戻し、無ければ再起動する。セーフモードでは再起動もセーフモードで行う。
- 触るとき: 更新後の再起動の挙動や中断時の扱いを変えるとき。
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.startup.quit()`, `gAppUpdater.selectPanel()`
- 条件付き依存: `if (cancelQuit.data)` → `gAppUpdater.selectPanel()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.startup.restartInSafeMode()`
- 条件付き依存: `if ( !Services.startup.quit( Ci.nsIAppStartup.eAttemptQuit | Ci.nsIAppStartup.eRestart ) )` → `gAppUpdater.selectPanel()`
- 参照: `AUS.currentState`, `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `Ci.nsIApplicationUpdateService.STATE_PENDING`, `Ci.nsISupportsPRBool`, `Services.appinfo.inSafeMode`, `cancelQuit.data`
- XPCOM: [`nsIAppStartup`](../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsIApplicationUpdateService`](../../../toolkit/mozapps/update/nsIUpdateService.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.appinfo` / `Services.obs` / `Services.startup`

## startDownload()
- 位置: L319-321
- 役割: AppUpdater に更新のダウンロードを許可する。
- 触るとき: ダウンロード開始ボタンの経路を調べるとき。
- 呼び出し先: `this._appUpdater.allowUpdateDownload()`
