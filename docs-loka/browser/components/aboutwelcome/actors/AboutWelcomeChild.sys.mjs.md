# browser/components/aboutwelcome/actors/AboutWelcomeChild.sys.mjs

source: browser/components/aboutwelcome/actors/AboutWelcomeChild.sys.mjs
source-hash: e787093bcdf019811ccc00911f2af227bd492a2a
lines: 437

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## AboutWelcomeChild.didDestroy()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._destroyed`

## AboutWelcomeChild.actorCreated()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.exportFunctions()`

## AboutWelcomeChild.sendToPage()
- 位置: L48-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `lazy.log.debug()`, `win.dispatchEvent()`
- 参照: `action.type`, `this.document.defaultView`, `win.CustomEvent`

## AboutWelcomeChild.exportFunctions()
- 位置: L60-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.exportFunction()`, `this.AWAddScreenImpression.bind()`, `this.AWEnsureAddonInstalled.bind()`, `this.AWEnsureLangPackInstalled.bind()`, `this.AWEvaluateAttributeTargeting.bind()`, `this.AWEvaluateScreenTargeting.bind()`, `this.AWFindBackupsInWellKnownLocations.bind()`, `this.AWFinish.bind()`, `this.AWGetFeatureConfig.bind()`, `this.AWGetFxAMetricsFlowURI.bind()`, `this.AWGetInstalledAddons.bind()`, `this.AWGetSelectedTheme.bind()`, `this.AWGetUnhandledCampaignAction.bind()`, `this.AWNegotiateLangPackForLanguageMismatch.bind()`, `this.AWNewScreen.bind()`, `this.AWSelectTheme.bind()`, `this.AWSendEventTelemetry.bind()`, `this.AWSendImpressionAction.bind()`, `this.AWSendToDeviceEmailsSupported.bind()`, `this.AWSendToParent.bind()`, `this.AWSetRequestedLocales.bind()`, `this.AWWaitForMigrationClose.bind()`, `this.AWWaitForNimbus.bind()`, `this.RPMGetFormatURLPref.bind()`
- 参照: `this.contentWindow`

## AboutWelcomeChild.wrapPromise()
- 位置: L165-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promise.then()`
- 参照: `this.contentWindow.Promise`

## AboutWelcomeChild.sendQueryAndCloneForContent()
- 位置: L174-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(async () => { return Cu.cloneInto( await this.sendQuery(...sendQueryArgs), this.contentWindow ); })()`, `Cu.cloneInto()`, `this.sendQuery()`, `this.wrapPromise()`
- 参照: `this.contentWindow`

## AboutWelcomeChild.AWSelectTheme()
- 位置: L185-189
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data.toUpperCase()`, `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWEvaluateScreenTargeting()
- 位置: L191-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWEvaluateAttributeTargeting()
- 位置: L198-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWAddScreenImpression()
- 位置: L204-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWSendImpressionAction()
- 位置: L210-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWFindBackupsInWellKnownLocations()
- 位置: L214-219
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.getAWContent()
- 位置: async L224-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `lazy.AboutWelcomeDefaults.getDefaults()`, `lazy.AboutWelcomeDefaults.prepareContentForReact()`, `lazy.log.debug()`, `this.sendQuery()`
- 条件付き依存: `if (featureConfig.languageMismatchEnabled)` → `this.sendQuery()`
- 参照: `defaults.backdrop`, `defaults.screens`, `experimentMetadata?.slug`, `featureConfig.appAndSystemLocaleInfo`, `featureConfig.backdrop`, `featureConfig.languageMismatchEnabled`, `featureConfig.needDefault`, `featureConfig.needPin`, `featureConfig.screens`, `this.contentWindow`

## AboutWelcomeChild.AWGetFeatureConfig()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAWContent()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetFxAMetricsFlowURI()
- 位置: L268-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetSelectedTheme()
- 位置: L272-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWSendEventTelemetry()
- 位置: L281-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.AWSendToParent()`
- 参照: `eventData.event_context`, `eventData.event_context.entrypoint`, `lazy.toolbarEntrypoint`

## AboutWelcomeChild.AWSendToParent()
- 位置: L300-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWWaitForMigrationClose()
- 位置: L304-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.setDidSeeFinalScreen()
- 位置: L308-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.AWSendToParent()`

## AboutWelcomeChild.focusUrlBar()
- 位置: L320-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.AWSendToParent()`

## AboutWelcomeChild.AWFinish()
- 位置: L326-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.focusUrlBar()`, `this.setDidSeeFinalScreen()`
- 参照: `this.contentWindow.location.href`

## AboutWelcomeChild.AWEnsureAddonInstalled()
- 位置: L333-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetInstalledAddons()
- 位置: L339-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`, `this.wrapPromise()`

## AboutWelcomeChild.AWEnsureLangPackInstalled()
- 位置: L345-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Promise.all()`, `Promise.all(formatting).then()`, `addMessageArgsAndUseLangPack()`, `this.sendQuery()`, `this.sendQuery( "AWPage:ENSURE_LANG_PACK_INSTALLED", negotiated.langPack ).then()`, `this.wrapPromise()`
- 参照: `content.languageSwitcher`, `negotiated.langPack`, `negotiated.requestSystemLocales`, `this.contentWindow`

## addMessageArgsAndUseLangPack()
- 位置: L362-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`
- 条件付き依存: `if (value.useLangPack)` → `formatting.push()`
- 条件付き依存: `if (value.useLangPack)` → `l10n.formatValue(value.string_id, value.args).then()`
- 条件付き依存: `if (value.useLangPack)` → `l10n.formatValue()`
- 参照: `negotiated.langPackDisplayName`, `value.args`, `value.raw`, `value.string_id`, `value.useLangPack`, `value?.string_id`

## AboutWelcomeChild.AWSetRequestedLocales()
- 位置: L391-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWNegotiateLangPackForLanguageMismatch()
- 位置: L398-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWSendToDeviceEmailsSupported()
- 位置: L405-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWNewScreen()
- 位置: L411-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetUnhandledCampaignAction()
- 位置: L415-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWWaitForNimbus()
- 位置: L421-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.RPMGetFormatURLPref()
- 位置: L425-427
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## AboutWelcomeChild.handleEvent()
- 位置: L433-435
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.debug()`
- 参照: `event.type`
