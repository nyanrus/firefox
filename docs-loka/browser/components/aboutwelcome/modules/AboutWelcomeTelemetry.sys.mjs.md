# browser/components/aboutwelcome/modules/AboutWelcomeTelemetry.sys.mjs

source: browser/components/aboutwelcome/modules/AboutWelcomeTelemetry.sys.mjs
source-hash: f19a2e977151aa4064c39e7b3ef06ee38df62b03
lines: 324

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getCharPref()`, `lazy.ClientID.getClientID()`, `lazy.TelemetrySession.getMetadata()`

## AboutWelcomeTelemetry.constructor()
- 位置: L46-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## AboutWelcomeTelemetry._maybeAttachAttribution()
- 位置: L67-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `lazy.AttributionCode.getCachedAttributionData()`
- 参照: `Object.keys(attribution).length`, `ping.attribution`

## AboutWelcomeTelemetry._createPing()
- 位置: async L75-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._maybeAttachAttribution()`
- 参照: `Services.appinfo.appBuildID`, `Services.locale.appLocaleAsBCP47`, `lazy.browserSessionId`, `lazy.telemetryClientId`
- XPCOM: `Services.appinfo` / `Services.locale`

## AboutWelcomeTelemetry.sendTelemetry()
- 位置: async L101-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._createPing()`, `this.parseAndSubmitPing()`
- 参照: `this.telemetryEnabled`

## AboutWelcomeTelemetry.parseAndSubmitPing()
- 位置: L110-170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean[pingKey].gleanPingForPingFailures.add()`, `this.submitGleanPingForPing()`
- 条件付き依存: `if (typeof ping.event_context === "string")` → `JSON.parse()`
- 条件付き依存: `if (eventContextStr.length)` → `eventContextStr.includes()`
- 条件付き依存: `if (eventContextStr.includes("{"))` → `Glean[pingKey].eventContextParseError.add()`
- 参照: `eventContextStr.length`, `lazy.impressionId`, `ping.browser_session_id`, `ping.client_id`, `ping.event_context`, `ping.event_context.write_in_microsurvey`, `ping.impression_id`, `ping.write_in_microsurvey`

## AboutWelcomeTelemetry.submitGleanPingForPing()
- 位置: L187-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings[pingKey].submit()`, `Glean[pingKey].unknownKeyCount.add()`, `Glean[pingKey].unknownKeys[camelKey].add()`, `JSON.stringify()`, `Number.isInteger()`, `Object.entries()`, `handledKeys.includes()`, `lazy.log.debug()`, `this._snakeToCamelCase()`
- 条件付き依存: `if (event_context?.reason)` → `Glean[pingKey].eventReason.set()`
- 条件付き依存: `if (event_context?.page)` → `Glean[pingKey].eventPage.set()`
- 条件付き依存: `if (event_context?.source)` → `Glean[pingKey].eventSource.set()`
- 条件付き依存: `if (event_context?.screen_family)` → `Glean[pingKey].eventScreenFamily.set()`
- 条件付き依存: `if (event_context?.value && writeInMicrosurvey)` → `Glean.microsurvey.eventInputValue.set()`
- 条件付き依存: `if (event_context?.smart_window_user_feedback_data && writeInMicrosurvey)` → `Glean.microsurveySmartWindow.userFeedbackData.set()`
- 条件付き依存: `if (event_context?.smart_window_user_feedback_data && writeInMicrosurvey)` → `lazy.normalizeChatLog()`
- 条件付き依存: `if (normalizedChat)` → `Glean.microsurveySmartWindow.chat.set()`
- 条件付き依存: `if (Number.isInteger(event_context?.screen_index))` → `Glean[pingKey].eventScreenIndex.set()`
- 条件付き依存: `if (event_context?.screen_id)` → `Glean[pingKey].eventScreenId.set()`
- 条件付き依存: `if (event_context?.screen_initials)` → `Glean[pingKey].eventScreenInitials.set()`
- 条件付き依存: `if (event_context)` → `JSON.stringify()`
- 条件付き依存: `if (event_context)` → `Glean[pingKey].eventContext.set()`
- 条件付き依存: `if ("attribution" in ping)` → `Object.entries()`
- 条件付き依存: `if ("attribution" in ping)` → `this._snakeToCamelCase()`
- 条件付き依存: `if ("attribution" in ping)` → `Glean[attributionKey][camelKey].set()`
- 条件付き依存: `if ("attribution" in ping)` → `Glean[attributionKey].unknownKeys[camelKey].add()`
- 条件付き依存: `if (typeof value === "object")` → `Glean[pingKey].invalidNestedData[camelKey].add()`
- 条件付き依存: `if (!(typeof value === "object"))` → `Glean[pingKey][camelKey].set()`
- 条件付き依存: `if (writeInMicrosurvey)` → `Glean.microsurvey.os.set()`
- 条件付き依存: `if (writeInMicrosurvey)` → `Glean.microsurvey.osVersion.set()`
- 条件付き依存: `if (os.isWindows)` → `Glean.microsurvey.windowsBuildNumber.set()`
- 条件付き依存: `if (writeInMicrosurvey)` → `Glean.microsurvey.appDisplayVersion.set()`
- 条件付き依存: `if (writeInMicrosurvey)` → `Glean.microsurvey.appChannel.set()`
- 条件付き依存: `if (writeInMicrosurvey)` → `Glean.microsurvey.appBuildId.set()`
- 参照: `Glean[attributionKey].unknownKeys`, `Glean[pingKey].invalidNestedData`, `Glean[pingKey].unknownKeys`, `Services.appinfo.OS`, `Services.appinfo.appBuildID`, `event_context.page`, `event_context.reason`, `event_context.screen_family`, `event_context.screen_id`, `event_context.screen_index`, `event_context.screen_initials`, `event_context.smart_window_user_feedback_data`, `event_context.source`, `event_context.value`, `event_context?.page`, `event_context?.reason`, `event_context?.screen_family`, `event_context?.screen_id`, `event_context?.screen_index`, `event_context?.screen_initials`, `event_context?.smart_window_user_feedback_data`, `event_context?.source`, `event_context?.value`, `lazy.ClientEnvironmentBase`, `os.isWindows`, `os.version`, `os.windowsBuildNumber`, `ping.attribution`, `ping.write_in_microsurvey`
- XPCOM: `Services.appinfo`

## AboutWelcomeTelemetry._snakeToCamelCase()
- 位置: L318-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.toUpperCase()`, `s.toString()`, `s.toString().replace()`
