# browser/components/asrouter/modules/OnboardingMessageProvider.sys.mjs

source: browser/components/asrouter/modules/OnboardingMessageProvider.sys.mjs
source-hash: 65c52e35723928e8da1727d953d7fba57c7a8b4c
lines: 3776

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Services.sysinfo.getProperty()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## BASE_MESSAGES()
- 位置: L67-3312
- 役割: (未記入)
- 触るとき: (未記入)

## PREONBOARDING_MESSAGES()
- 位置: L3314-3520
- 役割: (未記入)
- 触るとき: (未記入)

## ONBOARDING_MESSAGES()
- 位置: L3523-3524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BASE_MESSAGES()`, `BASE_MESSAGES().concat()`, `FeatureCalloutMessages.getMessages()`

## getExtraAttributes()
- 位置: async L3527-3533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `L10N.formatMessages()`
- 参照: `button_label.value`, `header.value`

## getMessages()
- 位置: async L3535-3539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ONBOARDING_MESSAGES()`, `OnboardingMessageProvider.getRestoredFromBackupMessage()`, `this.translateMessages()`

## getPreonboardingMessages()
- 位置: L3541-3543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PREONBOARDING_MESSAGES()`

## getPreonboardingVariablesWithDefaults()
- 位置: L3556-3576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.entries()`, `Object.entries(variables).filter()`, `Object.fromEntries()`, `this.getPreonboardingMessages()`, `this.getPreonboardingMessages().find()`
- 参照: `m.id`, `value.length`, `variables.enabled`, `variables.screens?.length`

## getRestoredFromBackupMessage()
- 位置: L3579-3593
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (backupRestorationTimestamp)` → `msg.id.startsWith()`
- 参照: `msg.content.id`, `msg.id`
- XPCOM: `Services.prefs`

## getUntranslatedMessages()
- 位置: async L3595-3599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ONBOARDING_MESSAGES()`

## translateMessages()
- 位置: async L3601-3629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `translatedMessages.push()`
- 条件付き依存: `if (!translatedMessage.content)` → `translatedMessages.push()`
- 条件付き依存: `if (msg.content.secondary_button)` → `L10N.formatMessages()`
- 条件付き依存: `if (msg.content.header)` → `L10N.formatMessages()`
- 参照: `header_string.value`, `msg.content.header`, `msg.content.header.string_id`, `msg.content.secondary_button`, `msg.content.secondary_button.label.string_id`, `secondary_button_string.value`, `translatedMessage.content`, `translatedMessage.content.header`, `translatedMessage.content.secondary_button.label`

## _doesAppNeedPin()
- 位置: async L3631-3634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ShellService.doesAppNeedPin()`

## _doesAppNeedDefault()
- 位置: async L3636-3643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.ShellService.isDefaultBrowser()`
- XPCOM: `Services.prefs`

## _shouldShowPrivacySegmentationScreen()
- 位置: L3645-3649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## _doesHomepageNeedReset()
- 位置: L3651-3656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## getUpgradeMessage()
- 位置: async L3658-3774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(await OnboardingMessageProvider.getMessages()).find()`, `OnboardingMessageProvider.getMessages()`, `content.screens?.find()`, `this._doesAppNeedDefault()`, `this._doesAppNeedPin()`, `this._shouldShowPrivacySegmentationScreen()`
- 条件付き依存: `if (!needDefault)` → `removeScreens()`
- 条件付き依存: `if (!needDefault)` → `screen.id?.startsWith()`
- 条件付き依存: `if (!needPrivatePin || needPin)` → `removeScreens()`
- 条件付き依存: `if (!needPrivatePin || needPin)` → `screen.id?.startsWith()`
- 条件付き依存: `if (!showSegmentation)` → `removeScreens()`
- 条件付き依存: `if (!showSegmentation)` → `screen.id?.startsWith()`
- 条件付き依存: `if (!needPrivatePin)` → `content.screens?.find()`
- 条件付き依存: `if (removeDefault)` → `removeScreens()`
- 条件付き依存: `if (removeDefault)` → `screen.id?.startsWith()`
- 条件付き依存: `if (lazy.usesFirefoxSync && lazy.mobileDevices > 0)` → `removeScreens()`
- 条件付き依存: `if (!(lazy.usesFirefoxSync && lazy.mobileDevices > 0))` → `prepareMobileDownload()`
- 参照: `content.screens?.find( screen => screen.id === "UPGRADE_PIN_FIREFOX" )?.content?.checkbox`, `lazy.hidePrivatePin`, `lazy.mobileDevices`, `lazy.usesFirefoxSync`, `pinScreen.content.checkbox`, `pinScreen.content.primary_button`, `pinScreen.content.subtitle`, `pinScreen.id`, `primary.action.type`, `primary.label`, `primary.label.string_id`, `screen.id`

## removeScreens()
- 位置: L3665-3672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `check()`
- 条件付き依存: `if (check(screens[i]))` → `screens.splice()`
- 参照: `screens?.length`

## prepareMobileDownload()
- 位置: L3675-3691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.screens.find()`, `lazy.BrowserUtils.sendToDeviceEmailsSupported()`
- 参照: `content.screens.find( screen => screen.id === "UPGRADE_MOBILE_DOWNLOAD" )?.content`, `mobileContent.cta_paragraph.action`, `mobileContent.cta_paragraph.text`, `screen.id`
