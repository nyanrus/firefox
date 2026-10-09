# browser/components/aboutwelcome/actors/AboutWelcomeParent.sys.mjs

source: browser/components/aboutwelcome/actors/AboutWelcomeParent.sys.mjs
source-hash: 529018430287862b22a783bc5f4f9e7a7a693702
lines: 453

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## shouldGateNimbusForAboutWelcome()
- 位置: L72-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.ExperimentAPI.enabled`
- XPCOM: `Services.prefs`

## waitForNimbusForAboutWelcome()
- 位置: async L96-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `Services.prefs.getIntPref()`, `lazy.ExperimentAPI._rsLoader.finishedUpdating()`, `lazy.ExperimentAPI.init()`, `lazy.log.debug()`, `lazy.log.error()`, `lazy.setTimeout()`, `resolve()`, `shouldGateNimbusForAboutWelcome()`
- 条件付き依存: `if (!shouldGateNimbusForAboutWelcome())` → `lazy.log.debug()`
- 条件付き依存: `if (nimbusReadyPromise)` → `lazy.log.debug()`
- 条件付き依存: `if (timeoutId)` → `lazy.clearTimeout()`
- XPCOM: `Services.prefs`

## AboutWelcomeObserver.constructor()
- 位置: L150-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this.win.addEventListener()`
- 参照: `AWTerminate.ADDRESS_BAR_NAVIGATED`, `Services.focus.activeWindow`, `this.onTabClose`, `this.onWindowClose`, `this.terminateReason`, `this.win`
- XPCOM: `Services.focus` / `Services.obs`

## this.onWindowClose()
- 位置: L160-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AWTerminate.WINDOW_CLOSED`, `this.terminateReason`

## this.onTabClose()
- 位置: L164-166
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AWTerminate.TAB_CLOSED`, `this.terminateReason`

## AboutWelcomeObserver.observe()
- 位置: L172-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AWTerminate.APP_SHUT_DOWN`, `this.terminateReason`

## AboutWelcomeObserver.AWTerminate()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)

## AboutWelcomeObserver.stop()
- 位置: L185-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.clearUserPref()`, `lazy.log.debug()`, `this.win.removeEventListener()`
- 参照: `this.onTabClose`, `this.onWindowClose`, `this.terminateReason`, `this.win`
- XPCOM: `Services.obs` / `Services.prefs`

## AboutWelcomeParent.constructor()
- 位置: L200-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MessagingSystemAllowlists.ensureInit()`, `super()`, `this.startAboutWelcomeObserver()`

## AboutWelcomeParent.startAboutWelcomeObserver()
- 位置: L211-213
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.AboutWelcomeObserver`

## AboutWelcomeParent.doesAppNeedPin()
- 位置: async L217-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ShellService.doesAppNeedPin()`, `lazy.ShellService.doesAppNeedStartMenuPin()`

## AboutWelcomeParent.isDefaultBrowser()
- 位置: L224-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ShellService.isDefaultBrowser()`

## AboutWelcomeParent.didDestroy()
- 位置: L228-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Telemetry.sendTelemetry()`, `this.RegionHomeObserver?.stop()`
- 条件付き依存: `if (this.AboutWelcomeObserver)` → `this.AboutWelcomeObserver.stop()`
- 参照: `this.AWMessageId`, `this.AboutWelcomeObserver`, `this.AboutWelcomeObserver.terminateReason`

## AboutWelcomeParent.onContentMessage()
- 位置: async L251-430
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (addon.id === data)` → `lazy.AddonManager.removeInstallListener()`
- 条件付き依存: `if (addon.id === data)` → `resolve()`
- 参照: `addon.id`

## AboutWelcomeParent.onInstallCancelled()
- 位置: L283-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.removeInstallListener()`, `resolve()`

## AboutWelcomeParent.onDownloadCancelled()
- 位置: L287-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.removeInstallListener()`, `resolve()`

## AboutWelcomeParent.onInstallFailed()
- 位置: L291-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AddonManager.removeInstallListener()`, `resolve()`

## observer()
- 位置: L350-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `resolve()`, `topics.forEach()`
- XPCOM: `Services.obs`

## AboutWelcomeParent.receiveMessage()
- 位置: L436-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.warn()`
- 条件付き依存: `if (this.manager.rootFrameLoader)` → `this.onContentMessage()`
- 参照: `this.manager.rootFrameLoader`, `this.manager.rootFrameLoader.ownerElement`

## resetNimbusReadyPromiseForTesting()
- 位置: L450-452
- 役割: (未記入)
- 触るとき: (未記入)
