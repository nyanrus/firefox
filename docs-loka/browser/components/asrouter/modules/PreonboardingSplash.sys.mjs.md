# browser/components/asrouter/modules/PreonboardingSplash.sys.mjs

source: browser/components/asrouter/modules/PreonboardingSplash.sys.mjs
source-hash: ed0afa1ca7822c5ccacb0429d78450e8597b62b2
lines: 226

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetters()`

## getTopWindow()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`

## showSpotlight()
- 位置: L59-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SpecialMessageActions.handleAction()`

## isFirstRunProfile()
- 位置: L61-61
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.BrowserHandler.firstRunProfile`

## maybeShowStartupSplash()
- 位置: L68-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._getSplashScreens()`, `this._shouldShow()`, `this._show()`, `this._show(screens).catch()`
- 参照: `screens.length`

## _shouldShow()
- 位置: L86-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.TelemetryReportingPolicy.hasUserResolvedTermsOfUse()`, `lazy.TelemetryReportingPolicy.willShowTOUModal()`, `this._willShowAboutWelcome()`
- 参照: `lazy.ASRouterTargeting.Environment.experimentsLoaded`, `lazy.ExperimentAPI.enabled`
- XPCOM: `Services.prefs`

## _willShowAboutWelcome()
- 位置: L140-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.urlFormatter .formatURLPref()`, `Services.urlFormatter .formatURLPref(WELCOME_URL_PREF) .split()`, `Services.urlFormatter .formatURLPref(WELCOME_URL_PREF) .split("|") .includes()`, `this.Policy.isFirstRunProfile()`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## _getSplashScreens()
- 位置: L162-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `lazy.NimbusFeatures.preonboarding.getAllVariables()`, `lazy.OnboardingMessageProvider.getPreonboardingVariablesWithDefaults()`, `screens.filter()`, `splashScreens.map()`
- 参照: `screen.id`, `splashScreens.length`, `variables.enabled`, `variables.screens`, `variables?.screens`

## _show()
- 位置: async L201-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.Policy.getTopWindow()`, `this.Policy.showSpotlight()`
- 参照: `win.gBrowser.selectedBrowser`
- XPCOM: `Services.prefs`
