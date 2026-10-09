# browser/components/BrowserGlue.sys.mjs

source: browser/components/BrowserGlue.sys.mjs
source-hash: 4a292baaec92880c7a17709b207117edec1920c4
lines: 1720

## <module>
- 役割: アプリ起動から終了までの全体制御を担う BrowserGlue を定義する。起動時の通知購読、初回ウィンドウ後の処理、遅延タスク、終了時の確認とプロファイル移行を行う。
- 呼び出し先: `Cc["@mozilla.org/weave/service;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyServiceGetters()`

## BrowserGlue()
- 位置: L163-172
- 役割: BrowserGlue のコンストラクター。アイドルサービスを遅延取得し、_init で通知を購読する。
- 触るとき: 起動直後の初期化順や、BrowserGlue の生成箇所を変えるときに見る。
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`, `this._init()`
- 参照: `Ci.nsIUserIdleService`
- XPCOM: `nsIUserIdleService`

## BG__setPrefToSaveSession()
- 位置: L179-195
- 役割: セッション保存が必要なとき、once 再開の pref を立ててから prefs をディスクに書く。
- 触るとき: 終了後にセッションが復元されない、または Mac で pref が保存されないときに見る。
- 呼び出し先: `Services.prefs.savePrefFile()`
- 条件付き依存: `if (!lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._saveSession`
- XPCOM: `Services.prefs`

## BG_observe()
- 位置: async L198-339
- 役割: 通知トピックごとに処理を振り分ける。初回ウィンドウ、セッション復元、終了要求、キーワード検索、署名失効、PDF.js 初期化、app-startup の OS 起動判定などを扱う。
- 触るとき: 新しい通知を購読させるとき、または起動や終了の通知の順序に問題が出たときに見る。
- 呼び出し先: `JSON.parse()`, `Services.console.logStringMessage()`, `Services.console.reset()`, `Services.obs.removeObserver()`, `addons.some()`, `console.error()`, `lazy.AddonManager.getAddonsByIDs()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.DownloadsViewableInternally.register()`, `lazy.LaunchOnLogin.isSupported()`, `lazy.PdfJs.init()`, `lazy.PlacesBrowserStartup.backendInitComplete()`, `lazy.SearchService.getEngineById()`, `subject.QueryInterface()`, `subject.findFlag()`, `subject.handleFlag()`, `this._beforeUIStartup()`, `this._dispose()`, `this._earlyBlankFirstPaint()`, `this._onFirstWindowLoaded()`, `this._onQuitApplicationGranted()`, `this._onQuitRequest()`, `this._onSafeModeRestart()`, `this._onWindowsRestored()`, `this._openPreferences()`, `this._setPrefToSaveSession()`
- 条件付き依存: `if (OBSERVE_LASTWINDOW_CLOSE_TOPICS)` → `this._onQuitRequest()`
- 条件付き依存: `if (OBSERVE_LASTWINDOW_CLOSE_TOPICS)` → `this._setPrefToSaveSession()`
- 条件付き依存: `if (data == "places-browser-init-complete")` → `lazy.PlacesBrowserStartup.notifyIfInitializationComplete()`
- 条件付き依存: `if (data == "add-breaches-sync-handler")` → `this._addBreachesSyncHandler()`
- 条件付き依存: `if (!linkHandled.data)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!linkHandled.data)` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (win)` → `JSON.parse()`
- 条件付き依存: `if (win)` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (win)` → `win.openTrustedLinkIn()`
- 条件付き依存: `if (addons.some(addon => addon))` → `this._notifyUnsignedAddonsDisabled()`
- 条件付き依存: `if (lazy.LaunchOnLogin.isSupported())` → `lazy.StartupOSIntegration.checkForLaunchOnLogin()`
- 参照: `BrowserInitState.isLaunchOnLogin`, `BrowserInitState.isTaskbarTab`, `Ci.nsISupportsPRBool`, `Ci.nsISupportsString`, `JSON.parse(data).disabled`, `data.href`, `linkHandled.data`, `subject.QueryInterface(Ci.nsISupportsString).data`, `subject.data`, `this._isNewProfile`, `win.gBrowser.selectedBrowser`
- XPCOM: [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `Services.console` / `Services.obs`

## BG__init()
- 位置: L342-367
- 役割: 起動時に必要な通知を Services.obs に登録し、DesktopActorRegistry を初期化する。
- 触るとき: 新しい通知を BrowserGlue で受けたいとき、または登録漏れで処理が走らないときに見る。
- 呼び出し先: `lazy.DesktopActorRegistry.init()`, `os.addObserver()`
- 条件付き依存: `if (OBSERVE_LASTWINDOW_CLOSE_TOPICS)` → `os.addObserver()`
- 参照: `Services.obs`
- XPCOM: `Services.obs`

## BG__dispose()
- 位置: L370-389
- 役割: プロファイル変更前に、ホーム画面キャッシュ、アイドル監視、GMP インストールマネージャー、コンテンツブロッキング設定を後始末する。
- 触るとき: 終了時に後始末が漏れる、またはエラーが出るときに見る。
- 呼び出し先: `lazy.AboutHomeStartupCache.uninit()`, `lazy.ContentBlockingPrefs.uninit()`
- 条件付き依存: `if (this._lateTasksIdleObserver)` → `this._userIdleService.removeIdleObserver()`
- 条件付き依存: `if (this._gmpInstallManager)` → `this._gmpInstallManager.uninit()`
- 参照: `this._gmpInstallManager`, `this._lateTasksIdleObserver`

## BG__beforeUIStartup()
- 位置: L393-427
- 役割: UI 表示前の処理。SessionStartup の初期化、セーフモードの画面、配布カスタマイズ、UI 移行、PDF.js の既定判定を行う。
- 触るとき: 起動時の UI 前処理の順序を変えるとき、またはセーフモードや移行が効かないときに見る。
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.prefHasUserValue()`, `lazy.BrowserUtils.callModulesFromCategory()`, `lazy.DistributionManagement.applyCustomizations()`, `lazy.SessionStartup.init()`, `this._migrateUI()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `Services.ww.openWindow()`
- 条件付き依存: `if (!Services.prefs.prefHasUserValue(PREF_PDFJS_ISDEFAULT_CACHE_STATE))` → `lazy.PdfJs.checkIsDefault()`
- 条件付き依存: `if (!AppConstants.NIGHTLY_BUILD && this._isNewProfile)` → `lazy.FormAutofillUtils.setOSAuthEnabled()`
- 条件付き依存: `if (!AppConstants.NIGHTLY_BUILD && this._isNewProfile)` → `lazy.LoginHelper.setOSAuthEnabled()`
- 参照: `AppConstants.NIGHTLY_BUILD`, `Services.appinfo.inSafeMode`, `this._isNewProfile`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.prefs` / `Services.ww`

## _checkForOldBuildUpdates()
- 位置: L429-461
- 役割: ビルド日時が checkInstallTime の日数より古ければ、バックグラウンド更新の確認を開始する。
- 触るとき: 古いビルドで更新確認が走らない、または頻繁に走るときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( AppConstants.MOZ_UPDATER && Services.prefs.getBoolPref("app.update.checkInstallTime") )` → `new Date().getTime()`
- 条件付き依存: `if ( AppConstants.MOZ_UPDATER && Services.prefs.getBoolPref("app.update.checkInstallTime") )` → `buildID.slice()`
- 条件付き依存: `if ( AppConstants.MOZ_UPDATER && Services.prefs.getBoolPref("app.update.checkInstallTime") )` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (buildDate + acceptableAge < today)` → `Cc["@mozilla.org/updates/update-service;1"] .getService(Ci.nsIApplicationUpdateService) .checkForBackgroundUpdates()`
- 条件付き依存: `if (buildDate + acceptableAge < today)` → `Cc["@mozilla.org/updates/update-service;1"] .getService()`
- 参照: `AppConstants.MOZ_UPDATER`, `Ci.nsIApplicationUpdateService`, `Services.appinfo.appBuildID`
- XPCOM: [`nsIApplicationUpdateService`](../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-service;1` → `UpdateService` (toolkit/mozapps/update/components.conf) / `Services.appinfo` / `Services.prefs`

## _onSafeModeRestart()
- 位置: async L463-510
- 役割: セーフモード再起動の確認ダイアログを出し、承認されて終了が拒否されなければ安全モードで再起動する。
- 触るとき: セーフモードへの再起動が始まらない、または確認なしで再起動するときに見る。
- 呼び出し先: `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`, `Services.obs.notifyObservers()`, `Services.prompt.asyncConfirmEx()`, `lazy.gBrandBundle.GetStringFromName()`, `rv.get()`, `strings.GetStringFromName()`, `strings.formatStringFromName()`
- 条件付き依存: `if (!cancelQuit.data)` → `Services.startup.restartInSafeMode()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIPrompt.MODAL_TYPE_INTERNAL_WINDOW`, `Ci.nsISupportsPRBool`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `cancelQuit.data`, `lazy.gBrowserBundle`, `window.browsingContext`
- XPCOM: [`nsIAppStartup`](../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsIPrompt`](../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs` / `Services.prompt` / `Services.startup`

## _notifyUnsignedAddonsDisabled()
- 位置: L512-547
- 役割: 署名のない拡張が無効化されたことを、最上位ウィンドウの通知バーで知らせる。
- 触るとき: 未署名アドオンの無効化通知が出ないときに見る。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.gNavigatorBundle.getString()`, `win.gNotificationBox.appendNotification()`
- 参照: `win.gNotificationBox.PRIORITY_WARNING_MEDIUM`

## callback()
- 位置: L531-535
- 役割: 通知の「詳細を見る」ボタンから、署名なし拡張の一覧を開く。
- 触るとき: 通知のリンク先が正しく開かないときに見る。
- 呼び出し先: `win.BrowserAddonUI.openAddonsMgr()`

## _earlyBlankFirstPaint()
- 位置: L549-708
- 役割: 起動の早い段階で空白のウィンドウを表示するかを決め、表示する場合はサイズと位置を xulstore から復元して先に描く。
- 触るとき: 起動直後の空白ウィンドウが出ない、または大きさがずれるときに見る。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.importESModule()`, `ChromeUtils.now()`, `Glean.browserTimings.startupTimeline.blankWindowShown.set()`, `Services.telemetry.msSinceProcessStart()`, `Services.ww.openWindow()`, `TelemetryTimestamps.add()`, `appWin.showInitialViewer()`, `cmdLine.findFlag()`, `docElt.setAttribute()`, `getValue()`, `lazy.StartupOSIntegration.isPrivateBrowsingAllowedInRegistry()`, `shouldCreateWindow()`, `win.docShell.treeOwner .QueryInterface()`, `win.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (hiddenTitlebar)` → `win.windowUtils.setCustomTitlebar()`
- 条件付き依存: `if (sizemode == "maximized")` → `docElt.setAttribute()`
- 条件付き依存: `if (!(sizemode == "maximized"))` → `win.resizeTo()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `Services.appinfo.drawInTitlebar`, `appWin.outerToInnerHeightDifferenceInCSSPixels`, `appWin.outerToInnerWidthDifferenceInCSSPixels`, `win.document.documentElement`, `win.openTime`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../netwerk/base/nsIChannel.idl.md) / `Services.appinfo` / `Services.telemetry` / `Services.ww`

## shouldCreateWindow()
- 位置: L552-622
- 役割: 空白ウィンドウを出してよいかを判定する。OS やサイレント起動、サイズ指定の CLI 引数、非既定テーマ、FPP などで除外する。
- 触るとき: 空白ウィンドウが出る条件を増やす、または減らすとき、または特定の起動で出ない理由を確かめるときに見る。
- 呼び出し先: `ChromeUtils.shouldResistFingerprinting()`, `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `cmdLine.findFlag()`, `getValue()`
- 参照: `AppConstants.platform`, `Services.startup.showedPreXULSkeletonUI`, `Services.startup.wasSilentlyStarted`
- XPCOM: `Services.prefs` / `Services.startup`

## getValue()
- 位置: L701-707
- 役割: xulstore から main-window の指定属性を読む。
- 触るとき: 空白ウィンドウの位置やサイズが保存値と違うときに見る。
- 呼び出し先: `Services.xulStore.getValue()`
- 参照: `AppConstants.BROWSER_CHROME_URL`
- XPCOM: `Services.xulStore`

## _firstWindowTelemetry()
- 位置: L710-713
- 役割: 最初のウィンドウの devicePixelRatio を百分率で gfx の計測値に記録する。
- 触るとき: 画面の拡大率の計測値が想定と違うときに見る。
- 呼び出し先: `Glean.gfxDisplay.scaling.accumulateSingleSample()`
- 参照: `aWindow.devicePixelRatio`

## BG__onFirstWindowLoaded()
- 位置: L716-754
- 役割: 最初のウィンドウ読み込み後に、リモート診断の WebChannel、古いビルドの更新確認、Sync 初期化、browser-first-window-ready のモジュール呼び出し、計測を行う。
- 触るとき: 最初のウィンドウで起動すべき処理が走らない、またはリモート診断の応答が変わったときに見る。
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `channel.listen()`, `lazy.BrowserUtils.callModulesFromCategory()`, `this._checkForOldBuildUpdates()`, `this._firstWindowTelemetry()`
- 条件付き依存: `if (data.command == "request")` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (data.command == "request")` → `Troubleshoot.snapshot().then()`
- 条件付き依存: `if (data.command == "request")` → `Troubleshoot.snapshot()`
- 条件付き依存: `if (data.command == "request")` → `channel.send()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue("services.sync.username"))` → `lazy.WeaveService.init()`
- 参照: `data.command`, `lazy.WebChannel`, `snapshotData.crashes`, `snapshotData.modifiedPreferences`, `snapshotData.printingPreferences`
- XPCOM: `Services.prefs`

## _onQuitApplicationGranted()
- 位置: L763-805
- 役割: 終了確定時に、カテゴリーの終了処理、セッション保存の pref、起動クラッシュ終了の記録、FOG の初期化を順に行う。
- 触るとき: 終了時に保存されるべき情報が残らない、または終了処理のエラーを確かめるときに見る。
- 呼び出し先: `Services.startup.trackStartupCrashEnd()`, `console.error()`, `failureHandler()`, `lazy.BrowserUtils.callModulesFromCategory()`, `task()`, `this._setPrefToSaveSession()`
- 参照: `Services.fog`
- XPCOM: `Services.fog` / `Services.startup`

## failureHandler()
- 位置: L764-774
- 役割: 自動テスト中の終了処理で例外が出たら、デバッグ用の abort でプロセスを止める。
- 触るとき: テストの終了時に異常終了する原因を調べるときに見る。
- 条件付き依存: `if (Cu.isInAutomation)` → `Cc["@mozilla.org/xpcom/debug;1"] .getService(Ci.nsIDebug2) .abort()`
- 条件付き依存: `if (Cu.isInAutomation)` → `Cc["@mozilla.org/xpcom/debug;1"] .getService()`
- 参照: `Ci.nsIDebug2`, `Cu.isInAutomation`, `ex.fileName`, `ex.filename`, `ex.lineNumber`
- XPCOM: [`nsIDebug2`](../../xpcom/base/nsIDebug2.idl.md) / `@mozilla.org/xpcom/debug;1`

## _monitorWebcompatReporterPref()
- 位置: L807-822
- 役割: Web 互換性レポーターの pref が変わるたびに、そのアドオンを有効化または無効化する。
- 触るとき: 互換性レポーターの有効・無効が pref に追従しないときに見る。
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (enabled && !addon.isActive)` → `addon.enable()`
- 条件付き依存: `if (!enabled && addon.isActive)` → `addon.disable()`
- 参照: `addon.isActive`
- XPCOM: `Services.prefs`

## BG__onWindowsRestored()
- 位置: L825-905
- 役割: 最初のウィンドウ群の復元後に一度だけ、テレメトリ、検索、拡張 UI、署名の確認、クラッシュ報告、Sanitizer などを初期化し、遅延タスクの予約をする。
- 触るとき: 起動後の初期化が一部走らない、または復元後に出る処理の順序を変えるときに見る。
- 呼び出し先: `lazy.BrowserUsageTelemetry.init()`, `lazy.ExtensionsUI.init()`, `lazy.Interactions.init()`, `lazy.PageDataService.init()`, `lazy.PreonboardingSplash.maybeShowStartupSplash()`, `lazy.Sanitizer.onStartup()`, `lazy.SearchSERPTelemetry.init()`, `lazy.SessionWindowUI.maybeShowRestoreSessionInfoBar()`, `this._monitorWebcompatReporterPref()`, `this._scheduleStartupIdleTasks()`, `this._userIdleService.addIdleObserver()`
- 条件付き依存: `if (!(AppConstants.MOZ_REQUIRE_SIGNING))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (signingRequired)` → `lazy.AddonManager.getStartupChanges()`
- 条件付き依存: `if (signingRequired)` → `lazy.AddonManager.getAddonsByIDs(disabledAddons).then()`
- 条件付き依存: `if (signingRequired)` → `lazy.AddonManager.getAddonsByIDs()`
- 条件付き依存: `if (addon.signedState <= lazy.AddonManager.SIGNEDSTATE_MISSING)` → `this._notifyUnsignedAddonsDisabled()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.CrashFileCleaner.init()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.CrashFileCleaner.scheduleCleanup()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.UnsubmittedCrashHandler.init()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.UnsubmittedCrashHandler.scheduleCheckForUnsubmittedCrashReports()`
- 条件付き依存: `if (AppConstants.ASAN_REPORTER)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (AppConstants.ASAN_REPORTER)` → `AsanReporter.init()`
- 条件付き依存: `if (AppConstants.ENABLE_WEBDRIVER)` → `lazy.RemoteControlBanner.init()`
- 参照: `AppConstants.ASAN_REPORTER`, `AppConstants.ENABLE_WEBDRIVER`, `AppConstants.MOZ_CRASHREPORTER`, `AppConstants.MOZ_REQUIRE_SIGNING`, `addon.signedState`, `lazy.AddonManager.SIGNEDSTATE_MISSING`, `lazy.AddonManager.STARTUP_CHANGE_DISABLED`, `lazy.MigrationUtils`, `this._lateTasksIdleObserver`, `this._windowsWereRestored`
- XPCOM: `Services.prefs`

## this._lateTasksIdleObserver()
- 位置: L883-892
- 役割: 一定時間アイドルになったら、遅延タスク用のアイドル監視を解除してベストエフォートの処理を予約する。
- 触るとき: ユーザーがアイドルになっても遅延タスクが走らないときに見る。
- 条件付き依存: `if (topic == "idle")` → `idleService.removeIdleObserver()`
- 条件付き依存: `if (topic == "idle")` → `this._scheduleBestEffortUserIdleTasks()`
- 参照: `this._lateTasksIdleObserver`

## _scheduleStartupIdleTasks()
- 位置: L928-1227
- 役割: 起動後のアイドル時に実行するタスク群を予約する。SafeBrowsing の初期化、カテゴリーのモジュール、プッシュやログイン、既定ブラウザ、Sync などを順に扱う。
- 触るとき: 起動後のタスクを追加・削除するとき、またはタスクが走らない理由を確かめるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.BrowserUtils.callModulesFromCategory()`, `runIdleTasks()`
- 参照: `AppConstants.MOZ_TELEMETRY_REPORTING`, `AppConstants.MOZ_UPDATER`, `AppConstants.MOZ_UPDATE_AGENT`, `AppConstants.platform`
- XPCOM: `Services.prefs`

## runIdleTasks()
- 位置: L929-955
- 役割: タスク配列を一つずつ ChromeUtils.idleDispatch に渡す。condition が偽のタスクは飛ばし、終了中は走らせない。
- 触るとき: アイドルタスクの条件判定やタイムアウトの扱いを変えるときに見る。
- 呼び出し先: `ChromeUtils.idleDispatch()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.now()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task.task()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `console.error()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.addProfilerMarker()`
- 参照: `Services.startup.shuttingDown`, `task.condition`, `task.name`, `task.timeout`
- XPCOM: `Services.startup`

## task()
- 位置: L966-968
- 役割: SafeBrowsing を初期化する。タイムアウトは 5 秒。
- 触るとき: SafeBrowsing が起動直後に効かないときに見る。
- 呼び出し先: `lazy.SafeBrowsing.init()`

## task()
- 位置: L985-995
- 役割: プッシュサービスの準備を始める。NS_ERROR_NOT_AVAILABLE は無視する。
- 触るとき: プッシュ通知が受信できないときに見る。
- 呼び出し先: `lazy.PushService.wrappedJSObject.ensureReady()`
- 参照: `Cr.NS_ERROR_NOT_AVAILABLE`, `ex.result`

## task()
- 位置: L1004-1010
- 役割: Services.logins にアクセスして、ログイン情報を別スレッドで読み込ませる。
- 触るとき: パスワード欄のある復元ページで遅くなるときに見る。
- 呼び出し先: `console.error()`
- 参照: `Services.logins`
- XPCOM: `Services.logins`

## task()
- 位置: L1017-1019
- 役割: 侵害アラートの pref 監視を登録する。
- 触るとき: 侵害アラートの切り替えが効かないときに見る。
- 呼び出し先: `this._addBreachAlertsPrefObserver()`

## task()
- 位置: L1024-1026
- 役割: 既定ブラウザの確認を行うかを判定する(_maybeShowDefaultBrowserPrompt)。
- 触るとき: 既定ブラウザの確認や上書きダイアログの表示順を調べるときに見る。
- 呼び出し先: `this._maybeShowDefaultBrowserPrompt()`

## task()
- 位置: L1031-1033
- 役割: スクリーンショットの pref を監視する。
- 触るとき: スクリーンショット機能の有効化が追従しないときに見る。
- 呼び出し先: `lazy.ScreenshotsUtils.monitorScreenshotsPref()`

## task()
- 位置: L1038-1044
- 役割: STARTUP_CRASHES_END_DELAY_MS のあとに、起動クラッシュの追跡を終了する。
- 触るとき: 起動クラッシュの判定が早すぎる、または遅すぎるときに見る。
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy.setTimeout()`
- 参照: `Services.startup.trackStartupCrashEnd`
- XPCOM: `Services.startup` / `Services.tm`

## task()
- 位置: L1049-1054
- 役割: ハンドラーサービスの asyncInit を呼ぶ。
- 触るとき: ファイルの関連付けの読み込みが遅いときに見る。
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/handler-service;1" ].getService()`, `handlerService.asyncInit()`
- 参照: `Ci.nsIHandlerService`
- XPCOM: [`nsIHandlerService`](../../uriloader/exthandler/nsIHandlerService.idl.md) / `@mozilla.org/uriloader/handler-service;1`

## task()
- 位置: L1059-1061
- 役割: Web プロトコルハンドラーの登録を初期化する。
- 触るとき: Web プロトコルの登録が有効にならないときに見る。
- 呼び出し先: `lazy.WebProtocolHandlerRegistrar.prototype.init()`

## task()
- 位置: L1067-1090
- 役割: DoH の TRR 測定を、有効化されたときに一度だけ実行する。
- 触るとき: TRR 測定が二重に走る、または走らないときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `new lazy.TRRRacer().run()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref(enabledPref, false)))` → `Services.prefs.addObserver()`
- 参照: `lazy.TRRRacer`
- XPCOM: `Services.prefs`

## observer()
- 位置: L1078-1088
- 役割: trrRace の有効化を監視し、有効になったら一度だけ TRR 測定を実行する。
- 触るとき: 有効化の後に測定が始まらないときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.removeObserver()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `new lazy.TRRRacer().run()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(completePref, false))` → `Services.prefs.setBoolPref()`
- 参照: `lazy.TRRRacer`
- XPCOM: `Services.prefs`

## task()
- 位置: async L1096-1106
- 役割: AW ツールバーボタンの設定ボタンを、自動化以外で必要なら追加する。
- 触るとき: 初回のセットアップボタンが出ない、またはテストで出てしまうときに見る。
- 条件付き依存: `if ( // Not in automation: the button changes CUI state, // breaking tests. Check this first, so that the module // doesn't load if it doesn't have to. !Cu.isInA...)` → `lazy.AWToolbarButton.maybeAddSetupButton()`
- 参照: `Cu.isInAutomation`, `lazy.AWToolbarButton.hasToolbarButtonEnabled`

## task()
- 位置: L1111-1113
- 役割: ASRouter の新規タブフックを既定設定で生成する。
- 触るとき: 新規タブのメッセージが出ないときに見る。
- 呼び出し先: `lazy.ASRouterDefaultConfig()`, `lazy.ASRouterNewTabHook.createInstance()`

## task()
- 位置: async L1119-1138
- 役割: バックグラウンド更新のスナップショットとタスクの予約を、更新が無効でない場合に行う。
- 触るとき: バックグラウンド更新のタスクが登録されないときに見る。
- 呼び出し先: `Cc[ "@mozilla.org/updates/update-service-stub;1" ].getService()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `BackgroundUpdate.scheduleFirefoxMessagingSystemTargetingSnapshotting()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `console.error()`
- 条件付き依存: `if (!updateServiceStub.updateDisabledForTesting)` → `BackgroundUpdate.maybeScheduleBackgroundUpdateTask()`
- 参照: `Ci.nsIApplicationUpdateServiceStub`, `updateServiceStub.updateDisabledForTesting`
- XPCOM: [`nsIApplicationUpdateServiceStub`](../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-service-stub;1` → `UpdateServiceStub` (toolkit/mozapps/update/components.conf)

## task()
- 位置: L1144-1149
- 役割: ログイン検出サービス(Fission で高価値サイトを判定)を初期化する。
- 触るとき: 高価値サイトの判定が効かないときに見る。
- 呼び出し先: `Cc[ "@mozilla.org/login-detection-service;1" ].getService()`, `loginDetection.init()`
- 参照: `Ci.nsILoginDetectionService`
- XPCOM: [`nsILoginDetectionService`](../../dom/ipc/nsILoginDetectionService.idl.md) / `@mozilla.org/login-detection-service;1`

## task()
- 位置: async L1155-1160
- 役割: Sync が有効なら、読み込み後に自動接続を予約する。
- 触るとき: Sync が起動後に同期されないときに見る。
- 条件付き依存: `if (lazy.WeaveService.enabled)` → `lazy.WeaveService.whenLoaded()`
- 条件付き依存: `if (lazy.WeaveService.enabled)` → `lazy.WeaveService.Weave.Service.scheduler.autoConnect()`
- 参照: `lazy.WeaveService.enabled`

## task()
- 位置: L1166-1171
- 役割: Windows で、信頼されていないモジュールのスレッドを解除する通知を出す。
- 触るとき: Windows の起動時に信頼されていないモジュールの処理が止まるときに見る。
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## task()
- 位置: async L1177-1181
- 役割: テレメトリ報告が有効なら、DAP の送信と訪問カウンターを起動する。
- 触るとき: DAP の計測が送られないときに見る。
- 呼び出し先: `lazy.DAPIncrementality.startup()`, `lazy.DAPTelemetrySender.startup()`, `lazy.DAPVisitCounter.startup()`

## task()
- 位置: L1187-1189
- 役割: ORB の JavaScript 検証用の JSOracle プロセスを起動する。
- 触るとき: ORB の検証が効かないときに見る。
- 呼び出し先: `ChromeUtils.ensureJSOracleStarted()`

## task()
- 位置: L1195-1197
- 役割: バックアップ機能が有効なら BackupService を初期化する。
- 触るとき: バックアップ機能が起動時に動かないときに見る。
- 呼び出し先: `lazy.BackupService.init()`

## task()
- 位置: L1206-1206
- 役割: Windows で SystemInfo の diskInfo を取得し、SSD 判定を用意する。
- 触るとき: ページ読み込みの計測の SSD 情報が欠けるときに見る。
- 参照: `Services.sysinfo.diskInfo`
- XPCOM: `Services.sysinfo`

## task()
- 位置: L1211-1221
- 役割: 全てのアイドルタスクの後に browser-startup-idle-tasks-finished を通知し、BrowserInitState の完了を解決する。
- 触るとき: 起動完了の通知が遅れる、または届かないときに見る。
- 呼び出し先: `BrowserInitState._resolveStartupIdleTask()`, `ChromeUtils.idleDispatch()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## _scheduleBestEffortUserIdleTasks()
- 位置: L1242-1288
- 役割: 一度もアイドルにならないと走らない遅延タスク(GMP のインストール確認、Remote Settings、侵害 Sync、検索のバックグラウンド確認)を予約する。
- 触るとき: アイドル後に走るべき処理を追加する、または更新の確認が走らないときに見る。
- 呼び出し先: `ChromeUtils.idleDispatch()`, `function RemoteSettingsInit() { lazy.RemoteSettings.init(); this._addBreachesSyncHandler(); }.bind()`, `lazy.BrowserUtils.callModulesFromCategory()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.now()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `console.error()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.addProfilerMarker()`
- 参照: `Services.startup.shuttingDown`, `task.name`
- XPCOM: `Services.startup`

## GMPInstallManagerSimpleCheckAndInstall()
- 位置: L1244-1252
- 役割: GMP のインストールマネージャーを作り、簡易の確認とインストールを実行する。結果は無視する。
- 触るとき: GMP プラグインの更新が入らないときに見る。
- 呼び出し先: `ChromeUtils.importESModule()`, `this._gmpInstallManager.simpleCheckAndInstall()`, `this._gmpInstallManager.simpleCheckAndInstall().catch()`
- 参照: `this._gmpInstallManager`

## RemoteSettingsInit()
- 位置: L1254-1257
- 役割: Remote Settings を初期化し、侵害の Sync ハンドラーを登録する。
- 触るとき: Remote Settings が取得されない、または侵害の同期が始まらないときに見る。
- 呼び出し先: `lazy.RemoteSettings.init()`, `this._addBreachesSyncHandler()`

## searchBackgroundChecks()
- 位置: L1259-1261
- 役割: 検索サービスのバックグラウンド確認を実行する。
- 触るとき: 検索エンジンの一覧の更新が起動後に行われないときに見る。
- 呼び出し先: `lazy.SearchService.runBackgroundChecks()`

## _addBreachesSyncHandler()
- 位置: L1290-1299
- 役割: 侵害アラートが有効なら、侵害の更新を購読する。
- 触るとき: 侵害アラートの更新が届かないときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "signon.management.page.breach-alerts.enabled", false ) )` → `lazy.LoginBreaches.subscribeToBreachUpdates()`
- XPCOM: `Services.prefs`

## _addBreachAlertsPrefObserver()
- 位置: L1301-1313
- 役割: 侵害アラートの pref を監視し、無効化された時に脆弱なパスワードの記録を消す。
- 触るとき: 侵害アラートを切ったあとも脆弱なパスワードの表示が残るときに見る。
- 呼び出し先: `Services.prefs.addObserver()`, `clearVulnerablePasswordsIfBreachAlertsDisabled()`
- XPCOM: `Services.prefs`

## clearVulnerablePasswordsIfBreachAlertsDisabled()
- 位置: async L1303-1307
- 役割: 侵害アラートが無効なら、脆弱なパスワードの記録を全て消す。最初に一度実行し、pref の変化でも呼ばれる。
- 触るとき: 侵害アラートを切ったときに記録が消えないときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(BREACH_ALERTS_PREF))` → `lazy.LoginBreaches.clearAllPotentiallyVulnerablePasswords()`
- XPCOM: `Services.prefs`

## _registerQuitSource()
- 位置: L1316-1318
- 役割: 終了の起点(ショートカットなど)を _quitSource に記録する。
- 触るとき: 終了時の警告がショートカットでの終了に対して出ないときに見る。
- 参照: `this._quitSource`

## BG__onQuitRequest()
- 位置: L1320-1507
- 役割: 終了要求時に、タブやウィンドウが残っていれば「閉じる前に確認」ダイアログを出し、承認か取り消しかを aCancelQuit に入れる。
- 触るとき: 終了時の確認が出ない、または出すぎるときに、その条件を確かめるときに見る。(要確認: 1468 行目は評価されるだけで効果のない式になっている。)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prompt.confirmEx()`, `lazy.BrowserWindowTracker.getTopWindow()`, `win.gBrowser.tabLocalization.formatMessagesSync()`, `win.gDialogBox.replaceDialogIfOpen()`
- 条件付き依存: `if (shouldWarnForShortcut)` → `win.document.getElementById()`
- 条件付き依存: `if (shouldWarnForShortcut)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (showCloseCurrentTabOption)` → `win.gBrowser.tabLocalization.formatMessagesSync()`
- 条件付き依存: `if (shouldWarnForShortcut)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(shouldWarnForShortcut))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (buttonPressed === 2)` → `win.gBrowser.removeTab()`
- 参照: `Ci.nsISupportsPRBool`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_POS_1_IS_SECONDARY`, `Services.prompt.BUTTON_POS_2`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `aCancelQuit.data`, `checkboxLabel.value`, `closeTabButtonLabel.value`, `lazy.BrowserWindowTracker.orderedWindows`, `quitButtonLabel.value`, `tabbrowser.pinnedTabCount`, `tabbrowser.visibleTabs.length`, `this._quitSource`, `title.value`, `warnOnClose.value`, `win.closed`, `win.gBrowser`, `win.gBrowser.selectedTab`, `win.gBrowser.visibleTabs.length`
- XPCOM: [`nsISupportsPRBool`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / `Services.prefs` / `Services.prompt`

## _migrateUI()
- 位置: L1509-1525
- 役割: プロファイルの移行バージョン(APP_DATA_VERSION = 183)を見て、新規ならバージョンを記録し、古ければ ProfileDataUpgrader.upgrade を呼ぶ。
- 触るとき: プロファイル移行の対象バージョンを上げるとき、または移行が走らないときに見る。
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (this._isNewProfile)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (profileDataVersion < APP_DATA_VERSION)` → `lazy.ProfileDataUpgrader.upgrade()`
- 参照: `this._isNewProfile`
- XPCOM: `Services.prefs`

## _showUpgradeDialog()
- 位置: async L1527-1564
- 役割: about:home の新規タブを開き、読み込み後にアップグレード用のスポットライトを表示する。
- 触るとき: アップグレード後の案内が出ない、または出る時期を変えるときに見る。
- 呼び出し先: `gBrowser.addTabsProgressListener()`, `gBrowser.addTrustedTab()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.OnboardingMessageProvider.getUpgradeMessage()`
- 参照: `gBrowser.selectedTab`

## onLocationChange()
- 位置: L1537-1552
- 役割: アップグレード用のタブの読み込みが進んだら、少し遅らせてスポットライトを表示し、リスナーを外す。
- 触るとき: アップグレードの案内が早すぎる、または表示されないときに見る。
- 条件付き依存: `if (aBrowser === tab.linkedBrowser)` → `lazy.setTimeout()`
- 条件付き依存: `if (aBrowser === tab.linkedBrowser)` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if (aBrowser === tab.linkedBrowser)` → `gBrowser.removeTabsProgressListener()`
- 参照: `tab.linkedBrowser`

## _showSetToDefaultSpotlight()
- 位置: async L1566-1598
- 役割: 既定ブラウザの案内をスポットライトで表示し、結果を Glean の既定設定の計測に記録する。
- 触るとき: 既定ブラウザの実験用スポットライトの表示や計測を調べるときに見る。
- 呼び出し先: `Date.now()`, `Glean.browser.setDefaultResult.accumulateSingleSample()`, `Math.floor()`, `Math.floor(Date.now() / 1000).toString()`, `Services.prefs.setCharPref()`, `console.error()`, `lazy.Spotlight.showSpotlightDialog()`, `shellService.isDefaultBrowserAsync()`, `win.getShellService()`
- 参照: `browser.documentGlobal`, `shellService.shouldCheckDefaultBrowser`
- XPCOM: `Services.prefs`

## _maybeShowDefaultBrowserPrompt()
- 位置: async L1600-1696
- 役割: アップグレードダイアログを出せるかを判定し、出せなければ既定ブラウザの確認やスポットライトを表示する。最後に ASRouter の defaultBrowserCheck トリガーを送る。
- 触るとき: 既定ブラウザの確認やアップグレードダイアログの出る順序や条件を変えるときに見る。
- 呼び出し先: `Glean.upgradeDialog.triggerReason.record()`, `Services.policies.isAllowed()`, `Services.prefs.getDefaultBranch()`, `Services.prefs.getIntPref()`, `await()`, `defaultPrefs.getBoolPref()`, `lazy.ASRouter.sendTriggerMessage()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.DefaultBrowserCheck.willCheckDefaultBrowser()`, `lazy.NimbusFeatures.upgradeDialog.getVariable()`, `lazy.TelemetryReportingPolicy.ensureUserIsNotified()`
- 条件付き依存: `if (!dialogReason)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!dialogReason)` → `this._showUpgradeDialog()`
- 条件付き依存: `if (willPrompt)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (willPrompt)` → `setToDefaultFeature.ready()`
- 条件付き依存: `if (willPrompt)` → `setToDefaultFeature.recordExposureEvent()`
- 条件付き依存: `if (willPrompt)` → `setToDefaultFeature.getAllVariables()`
- 条件付き依存: `if (showSpotlightPrompt && message)` → `this._showSetToDefaultSpotlight()`
- 条件付き依存: `if (willPrompt)` → `lazy.DefaultBrowserCheck.prompt()`
- 参照: `lazy.ASRouter.waitForInitialized`, `lazy.BrowserHandler.majorUpgrade`, `lazy.BrowserWindowTracker.getTopWindow({ allowFromInactiveWorkspace: true, })?.gBrowser.selectedBrowser`, `lazy.NimbusFeatures.setToDefaultPrompt`, `win.gBrowser.selectedBrowser`
- XPCOM: `Services.policies` / `Services.prefs`

## _openPreferences()
- 位置: L1701-1713
- 役割: 最上位のウィンドウで設定画面を開く。無ければ macOS では hiddenDOMWindow で開く。
- 触るとき: ウィンドウが無い状態で設定が開かないときに見る。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (chromeWindow)` → `chromeWindow.openPreferences()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Services.appShell.hiddenDOMWindow.openPreferences()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.appShell`
