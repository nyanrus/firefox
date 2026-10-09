# browser/actors/DecoderDoctorParent.sys.mjs

source: browser/actors/DecoderDoctorParent.sys.mjs
source-hash: ae99347cd227e2fccb79b0e03e552b0dbe3909f4
lines: 271

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## LOG_DD()
- 位置: L23-27
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.DEBUG_LOG)` → `dump()`
- 参照: `lazy.DEBUG_LOG`

## DecoderDoctorParent.getLabelForNotificationBox()
- 位置: L30-66
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (decoderDoctorReportId == "MediaWMFNeeded")` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (decoderDoctorReportId == "MediaPlatformDecoderNotFound")` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (type == "cannot-initialize-pulseaudio")` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (type == "unsupported-libavcodec" && AppConstants.platform == "linux")` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (type == "decode-error")` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (type == "decode-warning")` → `lazy.gNavigatorBundle.GetStringFromName()`
- 参照: `AppConstants.platform`

## DecoderDoctorParent.getSumoForLearnHowButton()
- 位置: L68-79
- 役割: (未記入)
- 触るとき: (未記入)

## DecoderDoctorParent.getEndpointForReportIssueButton()
- 位置: L81-89
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (type == "decode-error" || type == "decode-warning")` → `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## DecoderDoctorParent.receiveMessage()
- 位置: L91-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^\w+$/im.test()`, `JSON.parse()`, `LOG_DD()`, `Services.prefs.getCharPref()`, `box.getNotificationWithValue()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `console.error()`, `this.getLabelForNotificationBox()`, `type.toLowerCase()`
- 条件付き依存: `if (!formatsInPref)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (!(!formatsInPref))` → `formatsInPref.split(",").map()`
- 条件付き依存: `if (!(!formatsInPref))` → `formatsInPref.split()`
- 条件付き依存: `if (!(!formatsInPref))` → `x.trim()`
- 条件付き依存: `if (!(!formatsInPref))` → `formats .split(",") .map(x => x.trim()) .filter()`
- 条件付き依存: `if (!(!formatsInPref))` → `formats .split(",") .map()`
- 条件付き依存: `if (!(!formatsInPref))` → `formats .split()`
- 条件付き依存: `if (!(!formatsInPref))` → `existing.includes()`
- 条件付き依存: `if (newbies.length)` → `Services.prefs.setCharPref()`
- 条件付き依存: `if (newbies.length)` → `existing.concat(newbies).join()`
- 条件付き依存: `if (newbies.length)` → `existing.concat()`
- 条件付き依存: `if (!decodeIssue)` → `console.error()`
- 条件付き依存: `if (!isSolved)` → `this.getSumoForLearnHowButton()`
- 条件付き依存: `if (sumo)` → `LOG_DD()`
- 条件付き依存: `if (sumo)` → `buttons.push()`
- 条件付き依存: `if (sumo)` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (!isSolved)` → `this.getEndpointForReportIssueButton()`
- 条件付き依存: `if (endpoint)` → `LOG_DD()`
- 条件付き依存: `if (endpoint)` → `buttons.push()`
- 条件付き依存: `if (endpoint)` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (!isSolved)` → `box.appendNotification()`
- 条件付き依存: `if (formatsInPref)` → `Services.prefs.clearUserPref()`
- 参照: `aMessage.data`, `box.PRIORITY_INFO_LOW`, `browser?.documentGlobal`, `newbies.length`, `this.browsingContext.top.embedderElement`
- XPCOM: `Services.prefs`

## DecoderDoctorParent.callback()
- 位置: L207-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!clickedInPref)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## DecoderDoctorParent.callback()
- 位置: L228-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.getBoolPref()`, `params.append()`, `params.toString()`, `window.openTrustedLinkIn()`
- 条件付き依存: `if (!clickedInPref)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`
