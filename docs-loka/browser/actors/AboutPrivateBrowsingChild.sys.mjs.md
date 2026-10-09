# browser/actors/AboutPrivateBrowsingChild.sys.mjs

source: browser/actors/AboutPrivateBrowsingChild.sys.mjs
source-hash: 7645cbb1ca12d5f067b72c1b941e063b03d58781
lines: 92

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutPrivateBrowsingChild.actorCreated()
- 位置: L15-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.exportFunction()`, `super.actorCreated()`, `this.PrivateBrowsingIsEnrolledInExperiment.bind()`, `this.PrivateBrowsingPromoExposureTelemetry.bind()`, `this.PrivateBrowsingRecordIntroAnimation.bind()`, `this.PrivateBrowsingRecordRedesignClick.bind()`, `this.PrivateBrowsingRedesignEnabled.bind()`, `this.PrivateBrowsingRedesignExposure.bind()`, `this.PrivateBrowsingShouldHideDefault.bind()`
- 参照: `this.contentWindow`

## AboutPrivateBrowsingChild.PrivateBrowsingIsEnrolledInExperiment()
- 位置: L54-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pbNewtab.getEnrollmentMetadata()`
- 参照: `lazy.EnrollmentType.EXPERIMENT`

## AboutPrivateBrowsingChild.PrivateBrowsingShouldHideDefault()
- 位置: L60-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pbNewtab.getAllVariables()`
- 参照: `config?.content?.hideDefault`

## AboutPrivateBrowsingChild.PrivateBrowsingPromoExposureTelemetry()
- 位置: L65-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.pbNewtab.recordExposureEvent()`

## AboutPrivateBrowsingChild.PrivateBrowsingRecordRedesignClick()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.aboutprivatebrowsing["click" + source].record()`
- 参照: `Glean.aboutprivatebrowsing`

## AboutPrivateBrowsingChild.PrivateBrowsingRecordIntroAnimation()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.aboutprivatebrowsing.introAnimationPlayed.record()`

## AboutPrivateBrowsingChild.PrivateBrowsingRedesignExposure()
- 位置: L79-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NimbusFeatures.privateWindowRedesign.recordExposureEvent()`

## AboutPrivateBrowsingChild.PrivateBrowsingRedesignEnabled()
- 位置: L85-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`
