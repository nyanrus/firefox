# browser/extensions/webcompat/lib/interventions.js

source: browser/extensions/webcompat/lib/interventions.js
source-hash: 593e7b5dc415d0a274466e43fad1718c0f45fb3b
lines: 1105

## <module>
- 役割: (未記入)
- 呼び出し先: `InterventionHelpers.getOS()`, `browser.appConstants.getAppVersion()`, `browser.appConstants.getAppVersion().match()`, `browser.appConstants.getEffectiveUpdateChannel()`, `parseFloat()`, `this.#maybeOverrideUAHeaders()`, `this.#requestBlocksListener.getMatchingInterventions()`

## getTLDForUrl()
- 位置: L11-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `browser.urlHelpers.getBaseDomainFromHost()`, `console.error()`, `url.replaceAll()`, `url.startsWith()`
- 参照: `URL.parse(url.replaceAll("*", "x")).hostname`

## InterventionsWebRequestListener.constructor()
- 位置: L34-38
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#eventName`, `this.#listener`, `this.#opts`

## InterventionsWebRequestListener.getMatchingInterventions()
- 位置: L40-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...interventions].filter()`, `getTLDForUrl()`, `pattern.matches()`, `this.#excludePatternsForInterventions.get()`, `this.#interventionsByTLD.get()`, `this.#matchPatternsForInterventions.get()`, `types.includes()`

## InterventionsWebRequestListener.restartListener()
- 位置: L66-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...this.#matchPatternsForInterventions.values()] .map()`, `[...this.#matchPatternsForInterventions.values()] .map(setOfMatchPatterns => [...setOfMatchPatterns]) .flat()`, `[...this.#matchPatternsForInterventions.values()] .map(setOfMatchPatterns => [...setOfMatchPatterns]) .flat() .map()`, `browser.webRequest[this.#eventName].removeListener()`, `this.#matchPatternsForInterventions.values()`
- 条件付き依存: `if (urls.length)` → `browser.webRequest[this.#eventName].addListener()`
- 参照: `browser.webRequest`, `config.pattern.patterns`, `this.#eventName`, `this.#listener`, `this.#opts`, `urls.length`

## InterventionsWebRequestListener.interventionHandlesMatchPattern()
- 位置: L82-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MatchPatternCache.get()`, `getTLDForUrl()`, `set.add()`, `this.#interventionsByTLD.get()`, `this.#matchPatternsForInterventions.get()`
- 条件付き依存: `if (!set)` → `this.#matchPatternsForInterventions.set()`
- 条件付き依存: `if (!set)` → `this.#interventionsByTLD.set()`
- 参照: `infoOrPatternString.types`, `infoOrPatternString.url`

## InterventionsWebRequestListener.interventionExcludesMatchPattern()
- 位置: L103-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MatchPatternCache.get()`, `set.add()`, `this.#excludePatternsForInterventions.get()`
- 条件付き依存: `if (!set)` → `this.#excludePatternsForInterventions.set()`
- 参照: `infoOrPatternString.types`, `infoOrPatternString.url`

## InterventionsWebRequestListener.interventionNoLongerHandlesMatchPattern()
- 位置: L116-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MatchPatternCache.get()`, `getTLDForUrl()`, `this.#interventionsByTLD.get()`, `this.#matchPatternsForInterventions.get()`
- 条件付き依存: `if (set)` → `set.delete()`
- 条件付き依存: `if (!set.size)` → `this.#matchPatternsForInterventions.delete()`
- 条件付き依存: `if (!set.size)` → `this.#interventionsByTLD.delete()`
- 参照: `infoOrPatternString.url`, `set.size`

## InterventionsWebRequestListener.interventionNoLongerExcludesMatchPattern()
- 位置: L138-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MatchPatternCache.get()`, `this.#excludePatternsForInterventions.get()`
- 条件付き依存: `if (set)` → `set.delete()`
- 条件付き依存: `if (!set.size)` → `this.#excludePatternsForInterventions.delete()`
- 参照: `infoOrPatternString.url`, `set.size`

## SpecialContentScriptMetadataServer.constructor()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#serve.bind()`
- 参照: `this.#listener`

## SpecialContentScriptMetadataServer.start()
- 位置: L167-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.runtime.onConnect.addListener()`
- 参照: `this.#listener`

## SpecialContentScriptMetadataServer.stopAndClear()
- 位置: L171-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.runtime.onConnect.removeListener()`
- 参照: `this.#listener`, `this.#metadata`

## SpecialContentScriptMetadataServer.addMetadata()
- 位置: L176-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#metadata.interventionExcludesMatchPattern()`, `this.#metadata.interventionHandlesMatchPattern()`

## SpecialContentScriptMetadataServer.clearMetadata()
- 位置: L188-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#metadata.interventionNoLongerExcludesMatchPattern()`, `this.#metadata.interventionNoLongerHandlesMatchPattern()`
- 参照: `info?.metadata`

## SpecialContentScriptMetadataServer.#serve()
- 位置: L207-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `Object.keys()`, `port.disconnect()`, `this.#metadata.getMatchingInterventions()`, `url.startsWith()`
- 条件付き依存: `if (!metadata)` → `port.disconnect()`
- 条件付き依存: `if (cssToInject)` → `browser.scripting .insertCSS({ css, origin: useUserStyles ? "USER" : "AUTHOR", target, }) .catch()`
- 条件付き依存: `if (cssToInject)` → `browser.scripting .insertCSS()`
- 条件付き依存: `if (cssToInject)` → `console.error()`
- 条件付き依存: `if (bugsByMatchPattern)` → `this.#getBugNumberForUrl()`
- 条件付き依存: `if (Object.keys(dataToSend).length)` → `port.postMessage()`
- 参照: `Object.keys(dataToSend).length`, `dataToSend.bugNumber`, `dataToSend.bugsByMatchPattern`, `dataToSend.cssToInject`, `port.sender`, `tab.id`, `target.allFrames`, `target.frameIds`

## SpecialContentScriptMetadataServer.#getBugNumberForUrl()
- 位置: L265-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pattern.matches()`

## Interventions.constructor()
- 位置: L330-341
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.appConstants.isInAutomation()`, `this.#onSourceJSONChanged()`
- 条件付き依存: `if (browser.appConstants.isInAutomation())` → `structuredClone()`
- 条件付き依存: `if (browser.appConstants.isInAutomation())` → `browser.aboutConfigPrefs.getPref()`
- 条件付き依存: `if (override)` → `JSON.parse()`
- 参照: `this.#customFunctions`, `this.#originalInterventions`

## Interventions.#onSourceJSONChanged()
- 位置: L343-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.entries(availableInterventions).map()`
- 参照: `obj.id`, `this.#availableInterventions`

## Interventions.#postStartupAtomicOperation()
- 位置: async L357-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `navigator.locks.request()`
- 参照: `this.#bootedUp`

## Interventions.allSettled()
- 位置: async L363-365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#postStartupAtomicOperation()`

## Interventions.replaceAllInterventions()
- 位置: async L367-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#disableInterventionsInternal()`, `this.#enableInterventionsInternal()`, `this.#onSourceJSONChanged()`, `this.#postStartupAtomicOperation()`, `this.#signalInterventionChangesToAboutCompat()`, `this.#specialContentScriptMetadataServer.start()`, `this.#specialContentScriptMetadataServer.stopAndClear()`, `this.#stopListenersForTogglingIndividualInterventions()`
- 参照: `this.#availableInterventions`

## Interventions.onRemoteSettingsUpdate()
- 位置: async L383-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.replaceAllInterventions()`

## Interventions.resetToDefaultInterventions()
- 位置: async L387-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredClone()`, `this.replaceAllInterventions()`
- 参照: `this.#originalInterventions`

## Interventions.bindAboutCompatBroker()
- 位置: L393-395
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#aboutCompatBroker`

## Interventions.bootup()
- 位置: L397-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.onPrefChange.addListener()`, `this.#checkInterventionPref()`, `this.#checkInterventionPref(true).then()`, `this.#postStartupAtomicOperation()`, `this.#signalInterventionChangesToAboutCompat()`
- 参照: `this.#availableInterventions`, `this.#doneBootingUp`, `this.#interventionsEnabledByPref`

## Interventions.updateInterventions()
- 位置: async L420-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_data.map()`, `structuredClone()`, `this.#availableInterventions.findIndex()`, `this.#disableInterventionsInternal()`, `this.#enableInterventionsInternal()`, `this.#postStartupAtomicOperation()`, `this.#signalInterventionChangesToAboutCompat()`, `this.#specialContentScriptMetadataServer.start()`, `this.#specialContentScriptMetadataServer.stopAndClear()`, `this.getInterventionsByIds()`
- 条件付き依存: `if (!(i > -1))` → `this.#availableInterventions.push()`
- 参照: `i.id`, `this.#availableInterventions`, `v.id`

## Interventions.#checkInterventionPref()
- 位置: L443-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.getPref()`, `this.#disableInterventionsInternal()`, `this.#specialContentScriptMetadataServer.stopAndClear()`
- 条件付き依存: `if (value)` → `this.#enableInterventionsInternal({ alsoClearObsoleteContentScripts, }).then()`
- 条件付き依存: `if (value)` → `this.#enableInterventionsInternal()`
- 条件付き依存: `if (value)` → `this.#specialContentScriptMetadataServer.start()`
- 参照: `this.#interventionsEnabledByPref`

## Interventions.getAvailableInterventions()
- 位置: L460-462
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#availableInterventions`

## Interventions.getAllOriginalInterventions()
- 位置: L464-466
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#originalInterventions`

## Interventions.getInterventionsByIds()
- 位置: L468-470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ids?.includes()`, `this.#availableInterventions.filter()`

## Interventions.isEnabled()
- 位置: L472-474
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#interventionsEnabledByPref`

## Interventions.enableInterventions()
- 位置: async L476-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#enableInterventionsInternal()`, `this.#postStartupAtomicOperation()`, `this.#signalInterventionChangesToAboutCompat()`, `this.getInterventionsByIds()`

## Interventions.disableInterventions()
- 位置: async L486-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#disableInterventionsInternal()`, `this.#postStartupAtomicOperation()`, `this.#signalInterventionChangesToAboutCompat()`, `this.getInterventionsByIds()`

## Interventions.getBlocksAndMatchesFor()
- 位置: L496-516
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(bugs) .map()`, `Object.values(bugs) .map(bug => bug.blocks) .flat()`, `Object.values(bugs) .map(bug => bug.blocks) .flat() .filter()`, `Object.values(bugs) .map(bug => bug.exclude_blocks) .flat()`, `Object.values(bugs) .map(bug => bug.exclude_blocks) .flat() .filter()`, `Object.values(bugs) .map(bug => bug.exclude_matches) .flat()`, `Object.values(bugs) .map(bug => bug.exclude_matches) .flat() .filter()`, `Object.values(bugs) .map(bug => bug.matches) .flat()`, `Object.values(bugs) .map(bug => bug.matches) .flat() .filter()`
- 参照: `bug.blocks`, `bug.exclude_blocks`, `bug.exclude_matches`, `bug.matches`

## Interventions.#disableInterventionsInternal()
- 位置: L518-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contentScriptsPerIntervention.get()`, `this.#disableContentScripts()`, `this.#enableOrDisableCustomFuncs()`, `this.getBlocksAndMatchesFor()`
- 条件付き依存: `if (contentScriptData)` → `this.#contentScriptsPerIntervention.delete()`
- 条件付き依存: `if (contentScriptData)` → `this.#specialContentScriptMetadataServer.clearMetadata()`
- 条件付き依存: `if (contentScriptData)` → `contentScriptsToUnregister.push()`
- 条件付き依存: `if ("ua_string" in intervention)` → `this.#uaOverridesListener.interventionNoLongerHandlesMatchPattern()`
- 条件付き依存: `if ("ua_string" in intervention)` → `this.#uaOverridesListener.interventionNoLongerExcludesMatchPattern()`
- 条件付き依存: `if (blocks.length)` → `this.#requestBlocksListener.interventionNoLongerHandlesMatchPattern()`
- 条件付き依存: `if (blocks.length)` → `this.#requestBlocksListener.interventionNoLongerExcludesMatchPattern()`
- 条件付き依存: `if (requestBlocksChanged)` → `this.#requestBlocksListener.restartListener()`
- 条件付き依存: `if (uaOverridesChanged)` → `this.#uaOverridesListener.restartListener()`
- 参照: `blocks.length`, `config.active`, `contentScriptData.excludeMatches`, `contentScriptData.matches`, `contentScriptData.metadata`, `contentScriptData.registrations`, `intervention.enabled`, `this.#availableInterventions`

## Interventions.#signalInterventionChangesToAboutCompat()
- 位置: async L599-607
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#aboutCompatBroker.portsToAboutCompatTabs.broadcast()`
- 条件付き依存: `if (interventionsChanged)` → `this.#aboutCompatBroker.filterInterventions()`

## Interventions.#onGlobalPrefCheckedByInterventionsChanged()
- 位置: L609-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cfg.interventions.find()`, `this.#availableInterventions.filter()`, `this.#cachedCheckedGlobalPrefValues.delete()`, `this.updateInterventions()`
- 参照: `i.pref_check`

## Interventions.#checkInterventionNeededBasedOnGlobalPrefs()
- 位置: L617-641
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Object.keys()`, `this.#cachedCheckedGlobalPrefValues.get()`, `this.#cachedCheckedGlobalPrefValues.has()`, `this.#listenersForCheckedGlobalPrefs.has()`
- 条件付き依存: `if (!this.#listenersForCheckedGlobalPrefs.has(pref))` → `this.#listenersForCheckedGlobalPrefs.set()`
- 条件付き依存: `if (!this.#listenersForCheckedGlobalPrefs.has(pref))` → `browser.aboutConfigPrefs.onPrefChange.addListener()`
- 条件付き依存: `if (!this.#cachedCheckedGlobalPrefValues.has(pref))` → `this.#cachedCheckedGlobalPrefValues.set()`
- 条件付き依存: `if (!this.#cachedCheckedGlobalPrefValues.has(pref))` → `browser.aboutConfigPrefs.getPref()`
- 参照: `intervention.pref_check`

## listener()
- 位置: L623-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onGlobalPrefCheckedByInterventionsChanged()`

## Interventions.#onIndividualInterventionDisablingPrefChanged()
- 位置: async L643-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.getPref()`, `this.#getInterventionDisablingPref()`, `this.#postStartupAtomicOperation()`, `this.#signalInterventionChangesToAboutCompat()`, `this.getInterventionsByIds()`
- 条件付き依存: `if (prefValue === true)` → `this.#disableInterventionsInternal()`
- 条件付き依存: `if (!(prefValue === true))` → `this.#enableInterventionsInternal()`
- 参照: `config.id`

## Interventions.#whichInterventionsShouldBeSkipped()
- 位置: L662-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InterventionHelpers.shouldSkip()`
- 条件付き依存: `if (reason)` → `reasons.set()`
- 参照: `config.interventions`, `this.#appVersion`, `this.#updateChannel`, `this.appVersionOverride`

## Interventions.#getInterventionDisablingPref()
- 位置: L683-685
- 役割: (未記入)
- 触るとき: (未記入)

## Interventions.#ensureListeningForIndividualInterventionTogglingPref()
- 位置: L687-700
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#individualDisablingPrefListeners.has()`
- 条件付き依存: `if (!this.#individualDisablingPrefListeners.has(interventionId))` → `this.#individualDisablingPrefListeners.set()`
- 条件付き依存: `if (!this.#individualDisablingPrefListeners.has(interventionId))` → `browser.aboutConfigPrefs.onPrefChange.addListener()`

## listener()
- 位置: L692-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onIndividualInterventionDisablingPrefChanged()`

## Interventions.#stopListenersForTogglingIndividualInterventions()
- 位置: L702-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.onPrefChange.removeListener()`, `this.#individualDisablingPrefListeners.values()`
- 参照: `this.#individualDisablingPrefListeners`

## Interventions.#enableInterventionsInternal()
- 位置: L709-951
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Promise.resolve()`, `Promise.resolve().then()`, `browser.aboutConfigPrefs.getPref()`, `console.error()`, `skipped.push()`, `this.#ensureListeningForIndividualInterventionTogglingPref()`, `this.#getInterventionDisablingPref()`, `this.#whichInterventionsShouldBeSkipped()`
- 条件付き依存: `if (config.isMissingFiles)` → `skipped.push()`
- 条件付き依存: `if (!force && disablingPrefValue === true)` → `skipped.push()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `this.getBlocksAndMatchesFor()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `whichInterventionsShouldBeSkipped.get()`
- 条件付き依存: `if (skippedReason)` → `skippedReasons.add()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `this.#checkInterventionNeededBasedOnGlobalPrefs()`
- 条件付き依存: `if (checkedPrefFailure)` → `skippedReasons.add()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `InterventionHelpers.isDisabledByDefault()`
- 条件付き依存: `if ( !force && InterventionHelpers.isDisabledByDefault(intervention) )` → `skippedReasons.add()`
- 条件付き依存: `if (force)` → `forceEnabling.push()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `this.#enableOrDisableCustomFuncs()`
- 条件付き依存: `if ("ua_string" in intervention)` → `this.#uaOverridesListener.interventionHandlesMatchPattern()`
- 条件付き依存: `if ("ua_string" in intervention)` → `this.#uaOverridesListener.interventionExcludesMatchPattern()`
- 条件付き依存: `if (blocks.length)` → `this.#requestBlocksListener.interventionHandlesMatchPattern()`
- 条件付き依存: `if (blocks.length)` → `this.#requestBlocksListener.interventionExcludesMatchPattern()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `contentScriptsToRegister.push()`
- 条件付き依存: `if (!(!force && disablingPrefValue === true))` → `this.buildContentScriptsRegistrationsForIntervention()`
- 条件付き依存: `if (uaOverridesEnabled)` → `enabledUAoverrides.push()`
- 条件付き依存: `if (requestBlocksEnabled)` → `enabledRequestBlocks.push()`
- 条件付き依存: `if (usesCustomFuncs)` → `enabledCustomFuncs.push()`
- 条件付き依存: `if (!somethingWasEnabled && skippedReasons.size)` → `skipped.push()`
- 条件付き依存: `if (!somethingWasEnabled && skippedReasons.size)` → `skippedReasons.values()`
- 条件付き依存: `if (enabledRequestBlocks.length)` → `this.#requestBlocksListener.restartListener()`
- 条件付き依存: `if (enabledUAoverrides.length)` → `this.#uaOverridesListener.restartListener()`
- 条件付き依存: `if (alsoClearObsoleteContentScripts)` → `InterventionHelpers.ensureOnlyTheseContentScripts()`
- 条件付き依存: `if (alsoClearObsoleteContentScripts)` → `browser.appConstants.isInAutomation()`
- 条件付き依存: `if (!(alsoClearObsoleteContentScripts))` → `InterventionHelpers.registerContentScripts()`
- 条件付き依存: `if (enabledUAoverrides.length)` → `debugLog()`
- 条件付き依存: `if (enabledUAoverrides.length)` → `enabledUAoverrides.sort()`
- 条件付き依存: `if (enabledRequestBlocks.length)` → `debugLog()`
- 条件付き依存: `if (enabledRequestBlocks.length)` → `enabledRequestBlocks.sort()`
- 条件付き依存: `if (enabledCustomFuncs.length)` → `debugLog()`
- 条件付き依存: `if (enabledCustomFuncs.length)` → `enabledCustomFuncs.sort()`
- 条件付き依存: `if (forceEnabling.length)` → `debugLog()`
- 条件付き依存: `if (forceEnabling.length)` → `forceEnabling.sort()`
- 条件付き依存: `if (skipped.length)` → `debugLog()`
- 条件付き依存: `if (skipped.length)` → `skipped.sort()`
- 参照: `blocks.length`, `config.active`, `config.availableOnPlatform`, `config.id`, `config.interventions`, `config.interventions.length`, `config.isMissingFiles`, `config.label`, `enabledCustomFuncs.length`, `enabledRequestBlocks.length`, `enabledUAoverrides.length`, `forceEnabling.length`, `intervention.enabled`, `skipped.length`, `skippedReasons.size`, `this.#availableInterventions`, `this.#customFunctions`, `this._lastEnabledInfo`, `whichInterventionsShouldBeSkipped.size`

## Interventions.buildContentScriptsRegistrationsForIntervention()
- 位置: L953-1012
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.interventions?.some()`, `regsBuilder.add()`, `regsBuilder.build()`, `specialContentScriptKeys.addRegs()`, `specialContentScriptKeys.areAnyUsedBy()`, `specialContentScriptKeys.filterFromContentScriptsSection()`, `specialContentScriptKeys.foldIn()`, `specialContentScriptKeys.getNeededMetadata()`, `this.#contentScriptsPerIntervention.set()`, `this.#specialContentScriptMetadataServer.addMetadata()`
- 参照: `config.interventions`, `config.label`, `i.content_scripts?.no_console_message`, `intervention.content_scripts`, `intervention.enabled`

## Interventions.#enableOrDisableCustomFuncs()
- 位置: L1014-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (customFuncName in intervention)` → `customFunc[action]()`
- 条件付き依存: `if (customFuncName in intervention)` → `console.trace()`
- 参照: `config.label`, `this.#customFunctions`

## Interventions.#maybeOverrideUAHeaders()
- 位置: L1036-1077
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InterventionHelpers.applyUAChanges()`, `header.name.toLowerCase()`, `header.value.includes()`, `this.#uaOverridesListener.getMatchingInterventions()`
- 参照: `details.type`, `details.url`, `header.value`, `interventions?.length`, `this.#currentPlatform`

## Interventions.#disableContentScripts()
- 位置: async L1079-1103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await browser.scripting.getRegisteredContentScripts({ ids: contentScripts.map(s => s.id), }) )?.map()`, `browser.scripting.getRegisteredContentScripts()`, `browser.scripting.unregisterContentScripts()`, `console.error()`, `contentScripts.map()`
- 参照: `contentScripts?.length`, `s.id`, `script.id`
