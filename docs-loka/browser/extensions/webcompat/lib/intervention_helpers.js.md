# browser/extensions/webcompat/lib/intervention_helpers.js

source: browser/extensions/webcompat/lib/intervention_helpers.js
source-hash: b3f4fe6dd5ae2fb71856ab2b34313cc950166665
lines: 1086

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## MatchPatternCache.get()
- 位置: L214-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MatchPatternCache.#cache.get()`
- 条件付き依存: `if (!instance)` → `browser.matchPatterns.getMatcher()`
- 条件付き依存: `if (!instance)` → `MatchPatternCache.#cache.set()`

## ContentScriptRegistrationsBuilder.add()
- 位置: L233-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `filePaths.add()`, `path.includes()`, `paths.forEach()`, `this.#regs.get()`, `this.#regs.get(key).get()`, `this.#regs.get(key).has()`, `this.#regs.has()`
- 条件付き依存: `if (!this.#regs.has(key))` → `this.#regs.set()`
- 条件付き依存: `if (!this.#regs.get(key).has(fileType))` → `this.#regs.get(key).set()`
- 条件付き依存: `if (!this.#regs.get(key).has(fileType))` → `this.#regs.get()`
- 参照: `paths?.length`

## ContentScriptRegistrationsBuilder.build()
- 位置: L275-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `JSON.stringify()`, `regs.push()`
- 参照: `excludeMatches?.length`, `matches?.length`, `reg.allFrames`, `reg.cssOrigin`, `reg.excludeMatches`, `reg.id`, `reg.matchOriginAsFallback`, `reg.matches`, `reg.persistAcrossSessions`, `reg.runAt`, `reg.world`, `this.#regs`

## AbstractSpecialContentScriptKey.constructor()
- 位置: L336-340
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.must_match_origin_as_fallback`, `this.needed_on_all_frames`, `this.values`

## AbstractSpecialContentScriptKey.filterSelfFromJS()
- 位置: L342-349
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (contentScriptDefinition?.content_scripts?.js)` → `contentScriptDefinition.content_scripts.js.filter()`
- 条件付き依存: `if (contentScriptDefinition?.content_scripts?.js)` → `s.includes()`
- 参照: `contentScriptDefinition.content_scripts.js`, `contentScriptDefinition?.content_scripts?.js`, `this.constructor.scriptFilename`

## AbstractSpecialContentScriptKey.isUsedBy()
- 位置: L351-353
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.constructor.jsonKey`

## AbstractSpecialContentScriptKey.foldIn()
- 位置: L355-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.values.push()`
- 参照: `specialKeyData.all_frames`, `specialKeyData.match_origin_as_fallback`, `specialKeyData.user_styles`, `this.constructor.jsonKey`, `this.constructor.valuesKey`, `this.must_match_origin_as_fallback`, `this.needed_on_all_frames`, `this.user_styles`

## AbstractSpecialContentScriptKey.needed()
- 位置: L375-377
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.values.length`

## AbstractSpecialContentScriptKey.addRegs()
- 位置: L379-379
- 役割: (未記入)
- 触るとき: (未記入)

## AbstractSpecialContentScriptKey.addToMetadata()
- 位置: L381-385
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `this.values.flat()`
- 参照: `this.constructor.metadataKey`, `this.needed`

## HideAlertsKey.addRegs()
- 位置: L398-414
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `regsBuilder.add()`
- 参照: `this.constructor.scriptFilename`, `this.must_match_origin_as_fallback`, `this.needed`, `this.needed_on_all_frames`

## HideMessagesKey.addRegs()
- 位置: L427-437
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `regsBuilder.add()`
- 参照: `this.constructor.scriptFilename`, `this.must_match_origin_as_fallback`, `this.needed`, `this.needed_on_all_frames`

## ModifyMetaViewportKey.addRegs()
- 位置: L450-460
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `regsBuilder.add()`
- 参照: `this.constructor.scriptFilename`, `this.must_match_origin_as_fallback`, `this.needed`, `this.needed_on_all_frames`

## ModifyMetaViewportKey.addToMetadata()
- 位置: L462-469
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `Object.assign()`
- 参照: `this.constructor.metadataKey`, `this.needed`, `this.values`

## ConsoleLoggingScript.needed()
- 位置: L484-486
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#foundScriptsRequiringUs`

## ConsoleLoggingScript.isUsedBy()
- 位置: L488-491
- 役割: (未記入)
- 触るとき: (未記入)

## ConsoleLoggingScript.foldIn()
- 位置: L493-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content_scripts?.js?.filter()`, `path.includes()`, `path.startsWith()`
- 参照: `content_scripts?.js?.filter( path => !path.startsWith("bug") && !path.includes("/bug") ).length`, `this.#foundScriptsRequiringUs`, `this.must_match_origin_as_fallback`, `this.needed_on_all_frames`

## ConsoleLoggingScript.addRegs()
- 位置: L511-521
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `regsBuilder.add()`
- 参照: `this.constructor.scriptFilename`, `this.must_match_origin_as_fallback`, `this.needed`, `this.needed_on_all_frames`

## ConsoleLoggingScript.addToMetadata()
- 位置: L523-533
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `Object.entries()`
- 条件付き依存: `if (this.needed)` → `bugsByMatchPattern.push()`
- 条件付き依存: `if (this.needed)` → `MatchPatternCache.get()`
- 参照: `info.matches`, `interventionConfig.bugs`, `this.constructor.metadataKey`, `this.needed`

## InjectCSSKey.addRegs()
- 位置: L542-552
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `regsBuilder.add()`
- 参照: `this.constructor.scriptFilename`, `this.must_match_origin_as_fallback`, `this.needed`, `this.needed_on_all_frames`

## InjectCSSKey.addToMetadata()
- 位置: L554-564
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.needed)` → `this.values.flat()`
- 条件付き依存: `if (this.needed)` → `whichSheets.map(name => sheets[name] ?? "").join()`
- 条件付き依存: `if (this.needed)` → `whichSheets.map()`
- 参照: `interventionConfig.css`, `this.all_frames`, `this.constructor.metadataKey`, `this.needed`, `this.user_styles`

## SpecialContentScriptKeys.metadataKeys()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SpecialContentScriptKeys.#classes.map()`
- 参照: `c.metadataKey`

## SpecialContentScriptKeys.constructor()
- 位置: L584-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SpecialContentScriptKeys.#classes.map()`
- 参照: `this.#keys`

## SpecialContentScriptKeys.areAnyUsedBy()
- 位置: L588-590
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `key.isUsedBy()`, `this.#keys.some()`

## SpecialContentScriptKeys.filterFromContentScriptsSection()
- 位置: L592-596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `specialKey.filterSelfFromJS()`
- 参照: `this.#keys`

## SpecialContentScriptKeys.foldIn()
- 位置: L598-602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `specialKey.foldIn()`
- 参照: `this.#keys`

## SpecialContentScriptKeys.addRegs()
- 位置: L604-608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `specialKey.addRegs()`
- 参照: `this.#keys`

## SpecialContentScriptKeys.getNeededMetadata()
- 位置: L610-620
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `specialKey.addToMetadata()`, `this.#keys.some()`
- 参照: `key.needed`, `this.#keys`

## InstallTrigger_defined()
- 位置: L625-627
- 役割: (未記入)
- 触るとき: (未記入)

## InstallTrigger_undefined()
- 位置: L628-630
- 役割: (未記入)
- 触るとき: (未記入)

## relaxed_name_validation_rules()
- 位置: L631-639
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `n.setAttribute()`

## add_Chrome()
- 位置: L643-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.addChrome()`
- 参照: `config.version`

## add_Firefox_as_Gecko()
- 位置: L646-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.addGecko()`
- 参照: `config.version`

## add_Samsung_for_Samsung_devices()
- 位置: L649-651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.addSamsungForSamsungDevices()`

## add_Version_segment()
- 位置: L652-654
- 役割: (未記入)
- 触るとき: (未記入)

## cap_Version_to_99()
- 位置: L655-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.capVersionTo99()`

## change_Firefox_to_FireFox()
- 位置: L658-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.changeFirefoxToFireFox()`

## change_Gecko_to_like_Gecko()
- 位置: L661-663
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ua.replace()`

## change_OS_to_MacOSX()
- 位置: L664-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.getMacOSXUA()`
- 参照: `config.arch`, `config.version`

## change_OS_to_Windows()
- 位置: L667-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.windows()`

## Chrome()
- 位置: L670-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.getDeviceAppropriateChromeUA()`
- 参照: `config.noFxQuantum`, `config.ua`

## Chrome_with_FxQuantum()
- 位置: L675-678
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.getDeviceAppropriateChromeUA()`
- 参照: `config.ua`

## desktop_not_mobile()
- 位置: L679-681
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.desktopUA()`

## mimic_Android_Hotspot2_device()
- 位置: L682-684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.androidHotspot2Device()`

## replace_colon_in_rv_with_space()
- 位置: L685-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ua.replace()`

## browser_version()
- 位置: L688-690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.changeBrowserVersion()`

## add_Safari()
- 位置: L691-694
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.safari()`
- 参照: `config.withFirefox`

## Safari()
- 位置: L695-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.safari()`

## Safari_with_FxQuantum()
- 位置: L698-701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.safari()`
- 参照: `config.withFxQuantum`

## shouldSkip()
- 位置: L715-801
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InterventionHelpers.checkPlatformMatches()`, `InterventionHelpers.isDisabledByDefault()`, `InterventionHelpers.isMissingCustomFunctions()`
- 条件付き依存: `if (ua_string)` → `Array.isArray()`
- 条件付き依存: `if (firefoxChannel)` → `only_channels.includes()`
- 条件付き依存: `if (firefoxChannel)` → `not_channels?.includes()`
- 条件付き依存: `if (max_version)` → `String(max_version).includes()`
- 条件付き依存: `if (max_version)` → `String()`
- 条件付き依存: `if (!(String(max_version).includes(".")))` → `Math.floor()`
- 条件付き依存: `if (skip_if)` → `this.skip_if_functions[skip_if]()`
- 条件付き依存: `if (skip_if)` → `console.trace()`
- 参照: `InterventionHelpers.ua_change_functions`, `this.skip_if_functions`, `ua.change`

## isMissingCustomFunctions()
- 位置: L823-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InterventionHelpers.nonCustomInterventionKeys.has()`, `Object.keys()`, `customFunctionNames.has()`

## getOS()
- 位置: L835-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.getPref()`, `browser.appConstants.getPlatform()`

## getPlatformMatches()
- 位置: L842-858
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!InterventionHelpers._platformMatches)` → `this.getOS()`
- 条件付き依存: `if (os == "android")` → `browser.appConstants.getAndroidPackageName()`
- 条件付き依存: `if (os == "android")` → `packageName.includes()`
- 条件付き依存: `if (packageName.includes("fenix") || packageName.includes("firefox"))` → `InterventionHelpers._platformMatches.push()`
- 参照: `InterventionHelpers._platformMatches`

## checkPlatformMatches()
- 位置: L860-890
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `InterventionHelpers.getPlatformMatches()`, `actual.filter()`, `desired.includes()`
- 条件付き依存: `if (undesired)` → `Array.isArray()`
- 条件付き依存: `if (undesired)` → `undesired.includes()`
- 条件付き依存: `if (undesired)` → `actual.filter()`
- 参照: `actual.filter(x => desired.includes(x)).length`, `actual.filter(x => undesired.includes(x)).length`, `intervention.not_platforms`, `intervention.platforms`

## isDisabledByDefault()
- 位置: L892-898
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `intervention.not_platforms`, `intervention.platforms`, `intervention.platforms.length`

## applyUAChanges()
- 位置: L900-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `InterventionHelpers.ua_change_functions[change]()`, `console.trace()`
- 参照: `InterventionHelpers.ua_change_functions`, `config.bug`, `config.change`

## matchPatternsForTLDs()
- 位置: L935-937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tlds.map()`

## matchPatternsForGoogle()
- 位置: L943-945
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `InterventionHelpers.matchPatternsForTLDs()`

## registerContentScripts()
- 位置: async L947-990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `alreadyRegged.map()`, `alreadyReggedIds.includes()`, `browser.scripting.getRegisteredContentScripts()`, `browser.scripting.registerContentScripts()`, `console.error()`, `debugLog()`, `scriptsToReg.filter()`, `scriptsToReg.map()`
- 参照: `ids.length`, `s.id`, `script.id`

## ensureOnlyTheseContentScripts()
- 位置: async L992-1084
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activeContentScripts.filter()`, `browser.scripting.getRegisteredContentScripts()`, `contentScriptsToRegister.filter()`, `contentScriptsToRegister.map()`, `desiredContentScriptIds.has()`, `interventionContentScriptIds.has()`, `interventionContentScripts.filter()`, `interventionContentScripts.map()`, `s.id.includes()`
- 条件付き依存: `if (oldContentScriptsToUnregister.length)` → `debugLog()`
- 条件付き依存: `if (oldContentScriptsToUnregister.length)` → `browser.scripting.unregisterContentScripts()`
- 条件付き依存: `if (oldContentScriptsToUnregister.length)` → `oldContentScriptsToUnregister.map()`
- 条件付き依存: `if (oldContentScriptsToUnregister.length)` → `console.error()`
- 条件付き依存: `if (newContentScriptsToRegister.length)` → `debugLog()`
- 条件付き依存: `if (newContentScriptsToRegister.length)` → `browser.scripting.registerContentScripts()`
- 条件付き依存: `if (e.name != "InvalidStateError")` → `browser.scripting.registerContentScripts()`
- 条件付き依存: `if (e2.name != "InvalidStateError")` → `console.error()`
- 条件付き依存: `if (alreadyRegisteredContentScripts.length)` → `debugLog()`
- 参照: `alreadyRegisteredContentScripts.length`, `e.name`, `e2.name`, `newContentScriptsToRegister.length`, `oldContentScriptsToUnregister.length`, `s.id`, `script.id`
