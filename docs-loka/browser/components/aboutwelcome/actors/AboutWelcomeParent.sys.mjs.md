# browser/components/aboutwelcome/actors/AboutWelcomeParent.sys.mjs

source: browser/components/aboutwelcome/actors/AboutWelcomeParent.sys.mjs
source-hash: 529018430287862b22a783bc5f4f9e7a7a693702
lines: 453

## <module>
- 役割: about:welcome の親プロセス側アクター。ページからのメッセージを受け、設定の変更、Nimbus の待機、ツールバー選択の管理、終了理由の記録を行う
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## shouldGateNimbusForAboutWelcome()
- 位置: L72-88
- 役割: 実験ゲートの pref が有効で、Nimbus が有効、かつ about:welcome をまだ見ていないときに true を返す
- 触るとき: about:welcome の表示前に Nimbus を待つかどうかの条件を変えるとき
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.ExperimentAPI.enabled`
- XPCOM: `Services.prefs`

## waitForNimbusForAboutWelcome()
- 位置: async L96-147
- 役割: ゲート条件を満たすときだけ、ExperimentAPI の初期化と RS の更新完了を maxDisplayMs まで待つ。待ちの Promise は共有する
- 触るとき: 初回表示が実験の反映前に描画される、または表示が遅れる問題を調べるとき
- 呼び出し先: `Promise.race()`, `Services.prefs.getIntPref()`, `lazy.ExperimentAPI._rsLoader.finishedUpdating()`, `lazy.ExperimentAPI.init()`, `lazy.log.debug()`, `lazy.log.error()`, `lazy.setTimeout()`, `resolve()`, `shouldGateNimbusForAboutWelcome()`
- 条件付き依存: `if (!shouldGateNimbusForAboutWelcome())` → `lazy.log.debug()`
- 条件付き依存: `if (nimbusReadyPromise)` → `lazy.log.debug()`
- 条件付き依存: `if (timeoutId)` → `lazy.clearTimeout()`
- XPCOM: `Services.prefs`

## AboutWelcomeObserver.constructor()
- 位置: L150-170
- 役割: quit-application を監視し、アクティブウィンドウの TabClose と unload を監視して終了理由を準備する
- 触るとき: about:welcome を閉じた理由の記録を変えるとき
- 呼び出し先: `Services.obs.addObserver()`, `this.win.addEventListener()`
- 参照: `AWTerminate.ADDRESS_BAR_NAVIGATED`, `Services.focus.activeWindow`, `this.onTabClose`, `this.onWindowClose`, `this.terminateReason`, `this.win`
- XPCOM: `Services.focus` / `Services.obs`

## this.onWindowClose()
- 位置: L160-162
- 役割: 終了理由をウィンドウを閉じたものとして記録する
- 触るとき: ウィンドウ閉鎖の理由の扱いを調べるとき
- 参照: `AWTerminate.WINDOW_CLOSED`, `this.terminateReason`

## this.onTabClose()
- 位置: L164-166
- 役割: 終了理由をタブを閉じたものとして記録する
- 触るとき: タブ閉鎖の理由の扱いを調べるとき
- 参照: `AWTerminate.TAB_CLOSED`, `this.terminateReason`

## AboutWelcomeObserver.observe()
- 位置: L172-178
- 役割: アプリ終了時の通知で、終了理由を app-shut-down に変える
- 触るとき: 終了理由の優先順位を変えるとき
- 参照: `AWTerminate.APP_SHUT_DOWN`, `this.terminateReason`

## AboutWelcomeObserver.AWTerminate()
- 位置: L181-183
- 役割: 終了理由の定数表を返す(テスト用)
- 触るとき: テストで終了理由の値を参照するとき

## AboutWelcomeObserver.stop()
- 位置: L185-196
- 役割: 終了理由をログに出し、エントリポイントの pref を消し、監視を外す
- 触るとき: ツールバー経由で開いた後の entrypoint の後片付けを調べるとき
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.clearUserPref()`, `lazy.log.debug()`, `this.win.removeEventListener()`
- 参照: `this.onTabClose`, `this.onWindowClose`, `this.terminateReason`, `this.win`
- XPCOM: `Services.obs` / `Services.prefs`

## AboutWelcomeParent.constructor()
- 位置: L200-209
- 役割: 終了監視を開始し、MessagingSystemAllowlists の初期化を待たずに始める
- 触るとき: アクター生成時の初期化順序を変えるとき
- 呼び出し先: `lazy.MessagingSystemAllowlists.ensureInit()`, `super()`, `this.startAboutWelcomeObserver()`

## AboutWelcomeParent.startAboutWelcomeObserver()
- 位置: L211-213
- 役割: AboutWelcomeObserver を生成して保持する
- 触るとき: 終了監視の生成タイミングを変えるとき
- 参照: `this.AboutWelcomeObserver`

## AboutWelcomeParent.doesAppNeedPin()
- 位置: async L217-222
- 役割: タスクバーのピン留めとスタートメニューのピン留めのどちらかが必要かを ShellService で判定する
- 触るとき: ピン留めを促す画面を出すかどうかの判定を変えるとき
- 呼び出し先: `lazy.ShellService.doesAppNeedPin()`, `lazy.ShellService.doesAppNeedStartMenuPin()`

## AboutWelcomeParent.isDefaultBrowser()
- 位置: L224-226
- 役割: ShellService で既定ブラウザかを返す
- 触るとき: 既定ブラウザ設定の画面の出し分けを変えるとき
- 呼び出し先: `lazy.ShellService.isDefaultBrowser()`

## AboutWelcomeParent.didDestroy()
- 位置: L228-242
- 役割: 監視を止め、SESSION_END のテレメトリに終了理由を載せて送る
- 触るとき: about:welcome の終了テレメトリを変えるとき。observer が無い状態では例外になる点に注意
- 呼び出し先: `lazy.Telemetry.sendTelemetry()`, `this.RegionHomeObserver?.stop()`
- 条件付き依存: `if (this.AboutWelcomeObserver)` → `this.AboutWelcomeObserver.stop()`
- 参照: `this.AWMessageId`, `this.AboutWelcomeObserver`, `this.AboutWelcomeObserver.terminateReason`

## AboutWelcomeParent.onContentMessage()
- 位置: async L251-430
- 役割: ページからの AWPage: メッセージ種別ごとに、pref の設定、特殊アクション、テレメトリ、アドオン導入、テーマ、ピン留め、移行待ち、言語パック、ターゲティング、バックアップ探索などを振り分けて実行する
- 触るとき: ページが親へ要求する処理を追加・変更するとき。新しい種別はここに case を足す
- 呼び出し先: `AboutWelcomeParent.doesAppNeedPin()`, `AboutWelcomeParent.isDefaultBrowser()`, `Object.keys()`, `Object.keys(LIGHT_WEIGHT_THEMES).find()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `addon.enable()`, `bs.findBackupsInWellKnownLocations()`, `lazy.ASRouterScreenUtils.addScreenImpression()`, `lazy.ASRouterScreenUtils.evaluateScreenTargeting()`, `lazy.ASRouterScreenUtils.evaluateTargetingAndRemoveScreens()`, `lazy.ASRouterScreenUtils.handleImpressionAction()`, `lazy.AboutWelcomeDefaults.getAddonFromRepository()`, `lazy.AboutWelcomeDefaults.getAttributionContent()`, `lazy.AddonManager.addInstallListener()`, `lazy.AddonManager.getActiveAddons()`, `lazy.AddonManager.getActiveAddons().then()`, `lazy.AddonManager.getAddonByID()`, `lazy.AddonManager.getAddonByID(LIGHT_WEIGHT_THEMES[data]).then()`, `lazy.AddonManager.getAddonsByTypes()`, `lazy.BackupService.get()`, `lazy.BackupService.init()`, `lazy.BrowserUtils.sendToDeviceEmailsSupported()`, `lazy.BuiltInThemes.ensureBuiltInThemes()`, `lazy.FxAccounts.config.promiseMetricsFlowURI()`, `lazy.LangPackMatcher.ensureLangPackInstalled()`, `lazy.LangPackMatcher.getAppAndSystemLocaleInfo()`, `lazy.LangPackMatcher.negotiateLangPackForLanguageMismatch()`, `lazy.LangPackMatcher.setRequestedAppLocales()`, `lazy.NimbusFeatures.aboutwelcome.getAllVariables()`, `lazy.NimbusFeatures.aboutwelcome.getEnrollmentMetadata()`, `lazy.SpecialMessageActions.handleAction()`, `lazy.Telemetry.sendTelemetry()`, `lazy.log.debug()`, `response.addons.map()`, `themeShortName?.toLowerCase()`, `themes.find()`, `topics.forEach()`, `waitForNimbusForAboutWelcome()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref(DID_HANDLE_CAMAPAIGN_ACTION_PREF, false) )` → `lazy.ASRouterScreenUtils.getUnhandledCampaignAction()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref(DID_HANDLE_CAMAPAIGN_ACTION_PREF, false) )` → `SET_DEFAULT_CAMPAIGN_ACTIONS.includes()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref(DID_HANDLE_CAMAPAIGN_ACTION_PREF, false) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref(DID_HANDLE_CAMAPAIGN_ACTION_PREF, false) )` → `lazy.SpecialMessageActions.handleAction()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref(DID_HANDLE_CAMAPAIGN_ACTION_PREF, false) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( !Services.prefs.getBoolPref(DID_HANDLE_CAMAPAIGN_ACTION_PREF, false) )` → `lazy.log.debug()`
- 参照: `LIGHT_WEIGHT_THEMES.AUTOMATIC`, `activeTheme.id`, `activeTheme?.id`, `addon.id`, `addon.isActive`, `addonDetails.iconURL`, `addonDetails.id`, `addonDetails.name`, `addonDetails.screenshots`, `addonDetails.type`, `addonDetails.url`, `lazy.EnrollmentType.EXPERIMENT`, `this.AWMessageId`
- XPCOM: `Services.obs` / `Services.prefs`

## AboutWelcomeParent.onInstallEnded()
- 位置: L277-282
- 役割: 指定 ID のアドオンの導入完了で、完了を返しリスナーを外す
- 触るとき: アドオン導入の完了判定を変えるとき
- 条件付き依存: `if (addon.id === data)` → `lazy.AddonManager.removeInstallListener()`
- 条件付き依存: `if (addon.id === data)` → `resolve()`
- 参照: `addon.id`

## AboutWelcomeParent.onInstallCancelled()
- 位置: L283-286
- 役割: 導入キャンセルで、キャンセル扱いの結果を返しリスナーを外す
- 触るとき: 導入キャンセル時の結果文言を変えるとき
- 呼び出し先: `lazy.AddonManager.removeInstallListener()`, `resolve()`

## AboutWelcomeParent.onDownloadCancelled()
- 位置: L287-290
- 役割: ダウンロード取消を導入キャンセルと同じ結果で返しリスナーを外す
- 触るとき: ダウンロード取消時の扱いを調べるとき
- 呼び出し先: `lazy.AddonManager.removeInstallListener()`, `resolve()`

## AboutWelcomeParent.onInstallFailed()
- 位置: L291-294
- 役割: 導入失敗の結果を返しリスナーを外す
- 触るとき: 導入失敗時の文言や後続処理を変えるとき
- 呼び出し先: `lazy.AddonManager.removeInstallListener()`, `resolve()`

## observer()
- 位置: L350-353
- 役割: 移行ウィザードの閉鎖または破棄の通知を受けて、両方の監視を外し Promise を解決する
- 触るとき: 移行完了の待ち方を変えるとき
- 呼び出し先: `Services.obs.removeObserver()`, `resolve()`, `topics.forEach()`
- XPCOM: `Services.obs`

## AboutWelcomeParent.receiveMessage()
- 位置: L436-447
- 役割: ブラウザ要素があるときだけ onContentMessage に渡し、無ければ警告を出して null を返す
- 触るとき: ページが閉じかけているときのメッセージ扱いを調べるとき
- 呼び出し先: `lazy.log.warn()`
- 条件付き依存: `if (this.manager.rootFrameLoader)` → `this.onContentMessage()`
- 参照: `this.manager.rootFrameLoader`, `this.manager.rootFrameLoader.ownerElement`

## resetNimbusReadyPromiseForTesting()
- 位置: L450-452
- 役割: Nimbus 待ちの共有 Promise をリセットする(テスト専用)
- 触るとき: about:welcome の Nimbus 待ちのテストを書くとき
