# browser/components/aiwindow/ui/content/firstrun.js

source: browser/components/aiwindow/ui/content/firstrun.js
source-hash: 5ee4e9ae1b01f4510a3507c980691f9e72e4888b
lines: 750

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`

## isEuropePromotionRegion()
- 位置: L133-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EEA_REGIONS.has()`
- 参照: `lazy.Region.current`, `lazy.Region.home`

## getPromotedChoiceId()
- 位置: L139-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getModelDisplayOrder()`, `getModelDisplayOrder().find()`, `isEuropePromotionRegion()`
- 参照: `(modelData[id] ?? {}).brandName`

## buildModelCards()
- 位置: L150-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getModelDisplayOrder()`, `getModelDisplayOrder().map()`
- 参照: `card.label.args`, `card.subtitle`, `cardContent.body`, `cardContent.icon`, `cardContent.label`

## getHiddenOnboardingScreenIds()
- 位置: L194-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `id.trim()`, `lazy.NimbusFeatures.smartWindow.getVariable()`, `value .split()`, `value .split(",") .map()`, `value .split(",") .map(id => id.trim()) .filter()`

## getScreens()
- 位置: L206-541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildModelCards()`

## filterOnboardingScreens()
- 位置: L553-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NON_REMOVABLE_SCREEN_IDS.has()`, `allScreens.at()`, `allScreens.filter()`, `hiddenScreenIds.has()`, `screens.at()`
- 条件付き依存: `if ( lastVisible && lastVisible !== allScreens.at(-1) && lastVisible.content.additional_button )` → `Array.isArray()`
- 条件付き依存: `if ( lastVisible && lastVisible !== allScreens.at(-1) && lastVisible.content.additional_button )` → `actions.some()`
- 条件付き依存: `if ( Array.isArray(actions) && !actions.some( action => action.data?.pref?.name === FIRST_RUN_COMPLETE_PREF ) )` → `actions.push()`
- 参照: `action.data?.pref?.name`, `button.action?.data?.actions`, `button.label`, `lastVisible.content.additional_button`, `screen.id`

## createAIWindowConfig()
- 位置: L585-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `filterOnboardingScreens()`, `getHiddenOnboardingScreenIds()`, `getPromotedChoiceId()`, `getScreens()`
- 条件付き依存: `if (promotedChoiceId)` → `Services.prefs.setStringPref()`
- 参照: `hiddenScreenIds.size`
- XPCOM: `Services.prefs`

## renderFirstRun()
- 位置: async L607-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AWParent.didDestroy()`, `createAIWindowConfig()`, `document.body.appendChild()`, `document.createElement()`, `getAllModelsData()`, `window.addEventListener()`
- 参照: `lazy.AboutWelcomeParent`, `script.src`, `window.AWEvaluateScreenTargeting`, `window.AWFinish`, `window.AWGetFeatureConfig`, `window.AWGetInstalledAddons`, `window.AWGetSelectedTheme`, `window.AWSendEventTelemetry`, `window.AWSendToParent`

## receive()
- 位置: L613-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AWParent.onContentMessage()`
- 参照: `topChromeWindow.gBrowser.selectedBrowser`

## window.AWGetFeatureConfig()
- 位置: L620-620
- 役割: (未記入)
- 触るとき: (未記入)

## window.AWEvaluateScreenTargeting()
- 位置: L621-621
- 役割: (未記入)
- 触るとき: (未記入)

## window.AWGetSelectedTheme()
- 位置: L622-622
- 役割: (未記入)
- 触るとき: (未記入)

## window.AWGetInstalledAddons()
- 位置: L623-623
- 役割: (未記入)
- 触るとき: (未記入)

## window.AWSendToParent()
- 位置: L624-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `receive()`, `receive(name)()`

## window.AWSendEventTelemetry()
- 位置: L626-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Glean.smartWindow.onboardingScreenImpression.record()`, `["model_1", "model_2", "model_3"].includes()`, `message_id.includes()`
- 条件付き依存: `if (["model_1", "model_2", "model_3"].includes(source))` → `Glean.smartWindow.onboardingModelSelected.record()`
- 条件付き依存: `if (["model_1", "model_2", "model_3"].includes(source))` → `source.split()`
- 条件付き依存: `if (!(["model_1", "model_2", "model_3"].includes(source)))` → `message_id.includes()`
- 条件付き依存: `if ( source === "primary_button" && message_id.includes("AI_WINDOW_CHOOSE_MODEL") )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if ( source === "primary_button" && message_id.includes("AI_WINDOW_CHOOSE_MODEL") )` → `Glean.smartWindow.onboardingModelNavigate.record()`
- 条件付き依存: `if (!( source === "primary_button" && message_id.includes("AI_WINDOW_CHOOSE_MODEL") ))` → `message_id.includes()`
- 条件付き依存: `if ( source === "primary_button" && (message_id.includes("AI_WINDOW_MEMORIES") || message_id.includes("AI_WINDOW_SET_DEFAULT")) )` → `Glean.smartWindow.onboardingBackNavigate.record()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) )` → `Glean.smartWindow.onboardingMemoriesSettings.record()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) )` → `source.join()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) )` → `Glean.smartWindow.onboardingMemoriesNavigate.record()`
- 条件付き依存: `if (!( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) ))` → `message_id.includes()`
- 条件付き依存: `if (!( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) ))` → `Array.isArray()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_SET_DEFAULT") && Array.isArray(source) )` → `Glean.smartWindow.onboardingSetdefaultSettings.record()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_SET_DEFAULT") && Array.isArray(source) )` → `source.join()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_SET_DEFAULT") && Array.isArray(source) )` → `Glean.smartWindow.onboardingSetdefaultNavigate.record()`
- XPCOM: `Services.prefs`

## window.AWFinish()
- 位置: L692-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.onboardingComplete.record()`, `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `memories.join()`, `window.AWSendToParent()`
- 条件付き依存: `if (Services.prefs.getBoolPref(MEMORIES_FROM_CONVERSATION_PREF, false))` → `memories.push()`
- 条件付き依存: `if (Services.prefs.getBoolPref(MEMORIES_FROM_HISTORY_PREF, false))` → `memories.push()`
- 参照: `lazy.AIWindow.newTabURL`, `window.location.href`
- XPCOM: `Services.prefs`
