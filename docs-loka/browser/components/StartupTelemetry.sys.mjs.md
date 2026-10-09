# browser/components/StartupTelemetry.sys.mjs

source: browser/components/StartupTelemetry.sys.mjs
source-hash: 3ff41474da5020938e27779c750578029cc1dcd3
lines: 550

## <module>
- 役割: 起動時に収集する各種テレメトリ(Glean 指標)をまとめる。アイドル時に実行するタスクの登録と、個々の項目の計測を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _willUseExpensiveTelemetry()
- 位置: L35-43
- 役割: テレメトリ送信機能がビルドで有効で、かつ healthreport のアップロードが有効なときだけ true を返す。ディスク I/O を伴う計測を、送信される場合に限って実行するための判定。
- 触るとき: 重い計測を走らせる条件を変えるとき、または送信しないビルドで計測がどう動くかを確かめるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `AppConstants.MOZ_TELEMETRY_REPORTING`
- XPCOM: `Services.prefs`

## _runIdleTasks()
- 位置: L45-64
- 役割: 各タスクを idleDispatch で登録し、シャットダウン中でなければ実行する。所要時間を指定のプロファイラマーカーに記録し、例外はコンソールに出す。
- 触るとき: アイドルタスクの実行タイミングや例外処理を変えるとき。
- 呼び出し先: `ChromeUtils.idleDispatch()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.now()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `console.error()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!Services.startup.shuttingDown)` → `task.toSource()`
- 参照: `Services.startup.shuttingDown`
- XPCOM: `Services.startup`

## browserIdleStartup()
- 位置: L66-95
- 役割: 起動後のアイドル時に実行するタスク列を組み立てる。共通項目(FOG 初期化、コンテンツブロック、終了時消去、PiP、SSL キーログ、OS 認証、起動状態、HTTPS-only、GPC、AI 制御、ログイン時起動)に加え、送信時のみ PlacesDB の計測、Windows ではピン留めと既定ハンドラ、macOS では Dock の状態を登録する。
- 触るとき: 起動時に一度送る指標を追加するとき、またはプラットフォーム別の計測の振り分けを変えるとき。
- 呼び出し先: `this._runIdleTasks()`, `this.aiControlBlocking()`, `this.contentBlocking()`, `this.dataSanitization()`, `this.globalPrivacyControl()`, `this.httpsOnlyState()`, `this.initFOG()`, `this.launchOnLoginState()`, `this.osAuthEnabled()`, `this.pipEnabled()`, `this.sslKeylogFile()`, `this.startupConditions()`
- 条件付き依存: `if (this._willUseExpensiveTelemetry)` → `tasks.push()`
- 条件付き依存: `if (this._willUseExpensiveTelemetry)` → `lazy.PlacesDBUtils.telemetry()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `tasks.push()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.pinningStatus()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.isDefaultHandler()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `tasks.push()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.macDockStatus()`
- 参照: `AppConstants.platform`, `this._willUseExpensiveTelemetry`

## bestEffortIdleStartup()
- 位置: L106-118
- 役割: 取りこぼしても良い計測のタスク列を作る。主パスワードの有無と許可されたアプリ送信元を記録し、Windows かつ送信時のみプロファイル数とインストール情報を追加する。
- 触るとき: 一度きりで十分だが実行されなくても良い計測を足すとき。
- 呼び出し先: `lazy.OsEnvironment.reportAllowedAppSources()`, `this._runIdleTasks()`, `this.primaryPasswordEnabled()`
- 条件付き依存: `if (AppConstants.platform == "win" && this._willUseExpensiveTelemetry)` → `tasks.push()`
- 条件付き依存: `if (AppConstants.platform == "win" && this._willUseExpensiveTelemetry)` → `lazy.BrowserUsageTelemetry.reportProfileCount()`
- 条件付き依存: `if (AppConstants.platform == "win" && this._willUseExpensiveTelemetry)` → `lazy.BrowserUsageTelemetry.reportInstallationTelemetry()`
- 参照: `AppConstants.platform`, `this._willUseExpensiveTelemetry`

## initFOG()
- 位置: async L126-166
- 役割: 利用プロファイル ID を初期化し、ポリシー通知を待ってから FOG を初期化する。続けて fxAccountsClientInfo ping を有効にし、gleanInternalSdk と glean の Nimbus 変更を監視して Glean の設定を適用する。
- 触るとき: Glean の初期化順序や Nimbus からのメトリクス設定の適用を変えるとき。順序の依存に注意する。
- 呼び出し先: `GleanPings.fxAccountsClientInfo.setEnabled()`, `JSON.stringify()`, `Services.fog.applyServerKnobsConfig()`, `Services.fog.initializeFOG()`, `lazy.NimbusFeatures.glean.getAllEnrollments()`, `lazy.NimbusFeatures.glean.onUpdate()`, `lazy.NimbusFeatures.gleanInternalSdk.getVariable()`, `lazy.NimbusFeatures.gleanInternalSdk.onUpdate()`, `lazy.TelemetryReportingPolicy.ensureUserIsNotified()`, `lazy.UsageReporting.ensureInitialized()`
- 条件付き依存: `if (typeof cfg === "object" && cfg !== null)` → `Services.fog.applyServerKnobsConfig()`
- 条件付き依存: `if (typeof cfg === "object" && cfg !== null)` → `JSON.stringify()`
- 参照: `enrollment.value.gleanMetricConfiguration`
- XPCOM: `Services.fog`

## startupConditions()
- 位置: L168-195
- 役割: 前回の確認時刻の pref を読み、今回の時刻で上書きする。OS 再起動からの経過秒数と比べて、コールドスタートかを isCold に、経過秒数を secondsSinceLastOsRestart に記録する。例外は NOT_IMPLEMENTED 以外をコンソールに出す。
- 触るとき: コールドスタートの判定を変えるとき。既定値が現在時刻のため、pref が無い初回は isCold が false になり、ソースのコメントとずれる(要確認)。
- 呼び出し先: `Date.now()`, `Glean.startup.isCold.set()`, `Glean.startup.secondsSinceLastOsRestart.set()`, `Math.round()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- 条件付き依存: `if (ex.name !== "NS_ERROR_NOT_IMPLEMENTED")` → `console.error()`
- 参照: `Services.startup.secondsSinceLastOSRestart`, `ex.name`
- XPCOM: `Services.prefs` / `Services.startup`

## contentBlocking()
- 位置: L197-245
- 役割: トラッキング防止の通常・private 窓の有効状態、Cookie の扱い、フィンガープリント防止とマイニング防止の有効状態を Glean に送る。コンテンツブロックのカテゴリは standard・strict・custom を 0・1・2 に、それ以外を 3 に変換する。
- 触るとき: コンテンツブロックの指標を追加するとき、またはカテゴリの番号付けを変えるとき。
- 呼び出し先: `Glean.contentblocking.category.set()`, `Glean.contentblocking.cookieBehavior.accumulateSingleSample()`, `Glean.contentblocking.cryptominingBlockingEnabled.set()`, `Glean.contentblocking.fingerprintingBlockingEnabled.set()`, `Glean.contentblocking.trackingProtectionEnabled[ tpEnabled ? "true" : "false" ].add()`, `Glean.contentblocking.trackingProtectionPbmDisabled[ !tpPBEnabled ? "true" : "false" ].add()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prefs.getStringPref()`
- 参照: `Glean.contentblocking.trackingProtectionEnabled`, `Glean.contentblocking.trackingProtectionPbmDisabled`
- XPCOM: `Services.prefs`

## dataSanitization()
- 位置: L247-293
- 役割: 終了時消去の各項目の pref を Glean に送り、セッション限定の Cookie 例外を http・https・file について数えて送る。
- 触るとき: 終了時消去の指標を増やすとき、または例外の数え方を変えるとき。
- 呼び出し先: `Glean.datasanitization.privacyClearOnShutdownCache.set()`, `Glean.datasanitization.privacyClearOnShutdownCookies.set()`, `Glean.datasanitization.privacyClearOnShutdownDownloads.set()`, `Glean.datasanitization.privacyClearOnShutdownFormdata.set()`, `Glean.datasanitization.privacyClearOnShutdownHistory.set()`, `Glean.datasanitization.privacyClearOnShutdownOfflineApps.set()`, `Glean.datasanitization.privacyClearOnShutdownOpenWindows.set()`, `Glean.datasanitization.privacyClearOnShutdownSessions.set()`, `Glean.datasanitization.privacyClearOnShutdownSiteSettings.set()`, `Glean.datasanitization.privacySanitizeSanitizeOnShutdown.set()`, `Glean.datasanitization.sessionPermissionExceptions.set()`, `Services.prefs.getBoolPref()`, `["http", "https", "file"].some()`, `permission.principal.schemeIs()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`, `Services.perms.all`, `permission.capability`, `permission.type`
- XPCOM: [`nsICookiePermission`](../../netwerk/cookie/nsICookiePermission.idl.md) / `Services.perms` / `Services.prefs`

## httpsOnlyState()
- 位置: L295-336
- 役割: HTTPS-only モードの通常窓と private 窓について、監視関数を登録し、現在の状態を記録する。
- 触るとき: HTTPS-only の指標の登録や監視対象の pref を変えるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `_checkHTTPSOnlyPBMPref()`, `_checkHTTPSOnlyPref()`
- XPCOM: `Services.prefs`

## _checkHTTPSOnlyPref()
- 位置: async L298-309
- 役割: 通常窓の HTTPS-only が有効なら 1 を記録し、「一度でも有効にしたこと」の pref を立てる。無効でも過去に有効だったなら 2、それ以外は 0 を記録する。
- 触るとき: HTTPS-only の状態の値の意味を変えるとき。
- 呼び出し先: `Glean.security.httpsOnlyModeEnabled.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabled)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _checkHTTPSOnlyPBMPref()
- 位置: async L318-332
- 役割: private 窓の HTTPS-only について、通常窓と同じ 0・1・2 の判定を行い Glean に記録する。
- 触るとき: private 窓の HTTPS-only の指標を変えるとき。
- 呼び出し先: `Glean.security.httpsOnlyModeEnabledPbm.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabledPBM)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## globalPrivacyControl()
- 位置: L338-359
- 役割: GPC の機能 pref を監視対象に登録し、登録直後に一度判定を実行する。
- 触るとき: GPC の監視対象 pref を変えるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `_checkGPCPref()`
- XPCOM: `Services.prefs`

## _checkGPCPref()
- 位置: async L341-355
- 役割: GPC が有効なら 1 を記録し、「一度でも有効にしたこと」の pref を立てる。無効でも過去に有効だったなら 2、それ以外は 0 を記録する。
- 触るとき: GPC の指標の値の意味を変えるとき。
- 呼び出し先: `Glean.security.globalPrivacyControlEnabled.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (feature_enabled)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## aiControlBlocking()
- 位置: L361-397
- 役割: AI 機能の全体の制御 pref と各機能の制御 pref を監視対象に登録し、登録解除用の関数を返す。
- 触るとき: AI 機能の制御指標に機能を加えるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `_checkAiControlPrefs()`
- XPCOM: `Services.prefs`

## _checkAiControlPrefs()
- 位置: async L372-384
- 役割: 全体の制御が blocked かを記録し、各機能について blocked なら、または default で全体が blocked なら blocked として記録する。
- 触るとき: AI 制御の判定規則を変えるとき。
- 呼び出し先: `Glean.browser.aiControlIsBlocking[key].set()`, `Glean.browser.globalAiControlIsBlocking.set()`, `Object.entries()`, `Services.prefs.getStringPref()`
- 参照: `Glean.browser.aiControlIsBlocking`
- XPCOM: `Services.prefs`

## isUsingLauncher()
- 位置: L400-406
- 役割: 環境変数 FIREFOX_LAUNCHED_BY_DESKTOP_LAUNCHER が TRUE なら true を返し、それ以外は false を返す。
- 触るとき: 起動経路の判定(DesktopLauncher)の条件を変えるとき。
- 呼び出し先: `Services.env.get()`
- XPCOM: `Services.env`

## pinningStatus()
- 位置: async L408-465
- 役割: Windows のタスクバーのピン留め状態(通常窓と、MSIX 以外での private 窓)を記録する。起動ショートカットを分類し、自動起動・その他のショートカット・ランチャー・その他のいずれかを launchMethod に記録する。タスクバータブなら TaskbarTab で上書きする。
- 触るとき: Windows の起動経路の分類を変えるとき。MSIX では private 側の判定を行わない点に注意する。
- 呼び出し先: `Cc["@mozilla.org/browser/shell-service;1"].getService()`, `Cc["@mozilla.org/windows-taskbar;1"].getService()`, `Glean.osEnvironment.isTaskbarPinned.set()`, `Glean.osEnvironment.launchMethod.set()`, `Services.sysinfo.getProperty()`, `console.error()`, `shellService.classifyShortcut()`, `shellService.isCurrentAppPinnedToTaskbar()`
- 条件付き依存: `if ( AppConstants.platform === "win" && !Services.sysinfo.getProperty("hasWinPackageId") )` → `Glean.osEnvironment.isTaskbarPinnedPrivate.set()`
- 条件付き依存: `if ( AppConstants.platform === "win" && !Services.sysinfo.getProperty("hasWinPackageId") )` → `shellService.isCurrentAppPinnedToTaskbar()`
- 条件付き依存: `if (!(shortcut))` → `this.isUsingLauncher()`
- 参照: `AppConstants.platform`, `Ci.nsIWinTaskbar`, `Ci.nsIWindowsShellService`, `Services.appinfo.processStartupShortcut`, `lazy.BrowserInitState.isLaunchOnLogin`, `lazy.BrowserInitState.isTaskbarTab`, `winTaskbar.defaultGroupId`, `winTaskbar.defaultPrivateGroupId`
- XPCOM: `nsIWinTaskbar` / [`nsIWindowsShellService`](shell/nsIWindowsShellService.idl.md) / `@mozilla.org/browser/shell-service;1` / `@mozilla.org/windows-taskbar;1` / `Services.appinfo` / `Services.sysinfo`

## isDefaultHandler()
- 位置: L467-476
- 役割: .pdf と mailto について、Firefox が既定のアプリかどうかを Glean に記録する。
- 触るとき: 既定アプリの計測対象の種類を増やすとき。
- 呼び出し先: `Glean.osEnvironment.isDefaultHandler[x].set()`, `[".pdf", "mailto"].every()`, `lazy.ShellService.isDefaultHandlerFor()`
- 参照: `Glean.osEnvironment.isDefaultHandler`

## launchOnLoginState()
- 位置: async L478-500
- 役割: ログイン時起動の状態を、未対応・有効・設定で無効・ポリシーで無効・無効・エラーのいずれかに判定して Glean に記録する。
- 触るとき: ログイン時起動の状態の区分を増やすとき、またはポリシーによる無効の判定を変えるとき。
- 呼び出し先: `Glean.osEnvironment.launchOnLoginState.set()`, `lazy.LaunchOnLogin.isSupported()`
- 条件付き依存: `if (!(!lazy.LaunchOnLogin.isSupported()))` → `lazy.LaunchOnLogin.enablementDetails()`
- 条件付き依存: `if (!(!lazy.LaunchOnLogin.isSupported()))` → `console.error()`
- 参照: `enablementDetails.isAllowedByPolicy`, `enablementDetails.isEnabled`, `enablementDetails.isSupported`

## macDockStatus()
- 位置: L502-509
- 役割: macOS の Dock にアプリが登録されているかを Glean に記録する。
- 触るとき: macOS の Dock 関連の指標を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/macdocksupport;1"].getService()`, `Glean.osEnvironment.isKeptInDock.set()`
- 参照: `Cc["@mozilla.org/widget/macdocksupport;1"].getService( Ci.nsIMacDockSupport ).isAppInDock`, `Ci.nsIMacDockSupport`
- XPCOM: `nsIMacDockSupport` / `@mozilla.org/widget/macdocksupport;1`

## sslKeylogFile()
- 位置: L511-513
- 役割: SSLKEYLOGFILE 環境変数が設定されているかを Glean に記録する。
- 触るとき: SSL キーログの指標の取得方法を変えるとき。
- 呼び出し先: `Glean.sslkeylogging.enabled.set()`, `Services.env.exists()`
- XPCOM: `Services.env`

## osAuthEnabled()
- 位置: L515-521
- 役割: フォーム自動入力とパスワードそれぞれの OS 認証の有効状態を Glean に記録する。
- 触るとき: OS 認証の指標の取得元を変えるとき。
- 呼び出し先: `Glean.formautofill.osAuthEnabled.set()`, `Glean.pwmgr.osAuthEnabled.set()`, `lazy.FormAutofillUtils.getOSAuthEnabled()`, `lazy.LoginHelper.getOSAuthEnabled()`

## primaryPasswordEnabled()
- 位置: L523-528
- 役割: 内部トークンに主パスワードが設定されているかを Glean に記録する。
- 触るとき: 主パスワードの指標の取得方法を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/security/internalkeytoken;1"].createInstance()`, `Glean.primaryPassword.enabled.set()`
- 参照: `Ci.nsIPKCS11Token`, `token.hasPassword`
- XPCOM: `nsIPKCS11Token` / `@mozilla.org/security/internalkeytoken;1`

## pipEnabled()
- 位置: L530-548
- 役割: PiP の動画トグル pref の現在値を Glean に記録し、pref が変わって有効になったときは設定の有効化イベントを記録する。
- 触るとき: PiP の設定指標を追加するとき。
- 呼び出し先: `Services.prefs.addObserver()`, `observe()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L534-544
- 役割: PiP の動画トグル pref を読み、toggleEnabled に記録する。pref の変更時で有効なら enableSettings を記録する。
- 触るとき: PiP の変更イベントの扱いを変えるとき。
- 呼び出し先: `Glean.pictureinpicture.toggleEnabled.set()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enabled)` → `Glean.pictureinpictureSettings.enableSettings.record()`
- XPCOM: `Services.prefs`
