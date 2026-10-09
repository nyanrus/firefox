# browser/extensions/webcompat/lib/shims.js

source: browser/extensions/webcompat/lib/shims.js
source-hash: 736e2694ddb9a00b5e5607179446d87a7313eb8c
lines: 1435

## <module>
- 役割: (未記入)
- 呼び出し先: `browser.appConstants.getEffectiveUpdateChannel()`, `browser.appConstants.getPlatform()`

## Shim.constructor()
- 位置: L21-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.getPref()`, `browser.aboutConfigPrefs.onPrefChange.addListener()`, `supportedBranchAndPlatform.split()`, `this._onEnabledStateChanged()`, `this._preprocessOptions()`
- 条件付き依存: `if (!match.types)` → `this.matches.push()`
- 条件付き依存: `if (!(!match.types))` → `this.matches.push()`
- 参照: `match.target`, `match.types`, `matches?.length`, `opts.branches`, `opts.bug`, `opts.custom`, `opts.disabled`, `opts.file`, `opts.hiddenInAboutCompat`, `opts.hosts`, `opts.id`, `opts.isMissingFiles`, `opts.isSmartblockEmbedShim`, `opts.logos`, `opts.name`, `opts.needsShimHelpers`, `opts.notHosts`, `opts.onlyIfBlockedByETP`, `opts.onlyIfDFPIActive`, `opts.onlyIfPrivateBrowsing`, `opts.options`, `opts.platform`, `opts.requestStorageAccessForRedirect`, `opts.runFirst`, `opts.webExposedShimHelpers`, `script.css`, `script.js`, `this._activeOnTabs`, `this._contentScriptRegistrations`, `this._disabledByConfig`, `this._disabledByPlatform`, `this._disabledByReleaseBranch`, `this._disabledBySmartblockEmbedPref`, `this._disabledForSession`, `this._disabledGlobally`, `this._disabledPrefValue`, `this._hostOptIns`, `this._options`, `this._pBModeHostOptIns`, `this._showedOptInOnTabs`, `this.branches`, `this.bug`, `this.contentScripts`, `this.file`, `this.hiddenInAboutCompat`, `this.hosts`, `this.id`, `this.isGoogleTrendsDFPIFix`, `this.isMissingFiles`, `this.isSmartblockEmbedShim`, `this.logos`, `this.manager`, `this.matches`, `this.name`, `this.needsShimHelpers`, `this.notHosts`, `this.onlyIfBlockedByETP`, `this.onlyIfDFPIActive`, `this.onlyIfPrivateBrowsing`, `this.platform`, `this.ready`, `this.redirectsRequests`, `this.requestStorageAccessForRedirect`, `this.runFirst`, `this.unblocksOnOptIn`, `this.webExposedShimHelpers`

## Shim._preprocessOptions()
- 位置: L121-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (v?.value)` → `v.branches.includes()`
- 参照: `this._options`, `this.options`, `v.branches`, `v.platform`, `v.value`, `v?.value`

## Shim.enabled()
- 位置: L139-161
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disabledByConfig`, `this._disabledByPlatform`, `this._disabledByReleaseBranch`, `this._disabledBySmartblockEmbedPref`, `this._disabledForSession`, `this._disabledGlobally`, `this._disabledPrefValue`, `this.isMissingFiles`, `this.isSmartblockEmbedShim`

## Shim.disabledReason()
- 位置: L163-200
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disabledByConfig`, `this._disabledByPlatform`, `this._disabledByReleaseBranch`, `this._disabledBySmartblockEmbedPref`, `this._disabledForSession`, `this._disabledGlobally`, `this._disabledPrefValue`, `this.isMissingFiles`, `this.isSmartblockEmbedShim`

## Shim.disabledBySmartblockEmbedPref()
- 位置: L202-204
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disabledBySmartblockEmbedPref`

## Shim.disabledBySmartblockEmbedPref()
- 位置: L206-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._onEnabledStateChanged()`
- 参照: `this._disabledBySmartblockEmbedPref`

## Shim.onAllShimsEnabled()
- 位置: L211-217
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!wasEnabled)` → `this._onEnabledStateChanged()`
- 参照: `this._disabledGlobally`, `this.enabled`

## Shim.onAllShimsDisabled()
- 位置: L219-225
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (wasEnabled)` → `this._onEnabledStateChanged()`
- 参照: `this._disabledGlobally`, `this.enabled`

## Shim.enableForSession()
- 位置: L227-233
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!wasEnabled)` → `this._onEnabledStateChanged()`
- 参照: `this._disabledForSession`, `this.enabled`

## Shim.disableForSession()
- 位置: L235-241
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (wasEnabled)` → `this._onEnabledStateChanged()`
- 参照: `this._disabledForSession`, `this.enabled`

## Shim._onEnabledStateChanged()
- 位置: async L243-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._allowRequestsInETP()`, `this.manager?.onShimStateChanged()`
- 条件付き依存: `if (alsoToggleContentScripts)` → `this.manager._unregisterContentScriptsForShims()`
- 条件付き依存: `if (!this.enabled)` → `this._revokeRequestsInETP()`
- 条件付き依存: `if (alsoToggleContentScripts)` → `this.manager._registerContentScriptsForShims()`
- 参照: `this.enabled`, `this.id`

## Shim._allowRequestsInETP()
- 位置: async L260-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.matches.map()`
- 条件付き依存: `if (matchEntries.length)` → `browser.trackingProtection.shim()`
- 条件付き依存: `if (this._hostOptIns.size)` → `this.getApplicableOptIns()`
- 条件付き依存: `if (optIns.length)` → `browser.trackingProtection.allow()`
- 条件付き依存: `if (optIns.length)` → `Array.from()`
- 条件付き依存: `if (this._pBModeHostOptIns.size)` → `this.getApplicableOptIns()`
- 条件付き依存: `if (this._haveCheckedEnabledPrefs && alsoClearResourceCache && modified)` → `this.clearResourceCache()`
- 参照: `matchEntries.length`, `optIns.length`, `this._haveCheckedEnabledPrefs`, `this._hostOptIns`, `this._hostOptIns.size`, `this._optInPatterns`, `this._pBModeHostOptIns`, `this._pBModeHostOptIns.size`, `this.id`

## Shim._revokeRequestsInETP()
- 位置: async L303-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.trackingProtection.revoke()`
- 条件付き依存: `if (this._haveCheckedEnabledPrefs && alsoClearResourceCache)` → `this.clearResourceCache()`
- 参照: `this._haveCheckedEnabledPrefs`, `this.id`

## Shim.setActiveOnTab()
- 位置: L310-317
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (active)` → `this._activeOnTabs.add()`
- 条件付き依存: `if (!(active))` → `this._activeOnTabs.delete()`
- 条件付き依存: `if (!(active))` → `this._showedOptInOnTabs.delete()`

## Shim.isActiveOnTab()
- 位置: L319-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._activeOnTabs.has()`

## Shim.meantForHost()
- 位置: L323-334
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (hosts || notHosts)` → `notHosts.includes()`
- 条件付き依存: `if (hosts || notHosts)` → `hosts.includes()`

## Shim.unblocksURLOnOptIn()
- 位置: async L336-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._optInMatcher.matches()`
- 条件付き依存: `if (!this._optInPatterns)` → `this.getApplicableOptIns()`
- 条件付き依存: `if (!this._optInMatcher)` → `browser.matchPatterns.getMatcher()`
- 条件付き依存: `if (!this._optInMatcher)` → `Array.from()`
- 参照: `this._optInMatcher`, `this._optInPatterns`

## Shim.isTriggeredByURLAndType()
- 位置: L350-366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entry.matcher.matches()`, `entry.types.includes()`
- 条件付き依存: `if (!entry.matcher)` → `browser.matchPatterns.getMatcher()`
- 条件付き依存: `if (!entry.matcher)` → `Array.from()`
- 参照: `entry.matcher`, `entry.patterns`, `this.matches`

## Shim.getApplicableOptIns()
- 位置: async L368-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `branches.includes()`, `optins.push.apply()`, `platforms.includes()`
- 条件付き依存: `if (typeof unblock === "string")` → `optins.push()`
- 参照: `branches?.length`, `platforms?.length`, `this._applicableOptIns`, `this.unblocksOnOptIn`

## Shim.onUserOptIn()
- 位置: async L395-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getApplicableOptIns()`
- 条件付き依存: `if (optins.length)` → `activeHostOptIns.add()`
- 条件付き依存: `if (optins.length)` → `browser.trackingProtection.allow()`
- 条件付き依存: `if (optins.length)` → `Array.from()`
- 条件付き依存: `if (optins.length)` → `this.clearResourceCache()`
- 参照: `optins.length`, `this._hostOptIns`, `this._pBModeHostOptIns`, `this.id`

## Shim.hasUserOptedInAlready()
- 位置: L412-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `activeHostOptIns.has()`
- 参照: `this._hostOptIns`, `this._pBModeHostOptIns`

## Shim.showOptInWarningOnce()
- 位置: L419-433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `browser.tabs .executeScript()`, `this._showedOptInOnTabs.add()`, `this._showedOptInOnTabs.has()`
- 条件付き依存: `if (this._showedOptInOnTabs.has(tabId))` → `Promise.resolve()`

## Shim.onUserOptOut()
- 位置: async L435-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getApplicableOptIns()`
- 条件付き依存: `if (optIns.length)` → `activeHostOptIns.delete()`
- 条件付き依存: `if (optIns.length)` → `browser.trackingProtection.allow()`
- 条件付き依存: `if (optIns.length)` → `Array.from()`
- 条件付き依存: `if (optIns.length)` → `this.clearResourceCache()`
- 参照: `optIns.length`, `this._hostOptIns`, `this._pBModeHostOptIns`, `this.id`

## Shim.clearUserOptIns()
- 位置: async L452-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `activeHostOptIns.clear()`, `browser.trackingProtection.allow()`, `this.clearResourceCache()`, `this.getApplicableOptIns()`
- 参照: `activeHostOptIns.length`, `optIns.length`, `this._hostOptIns`, `this._pBModeHostOptIns`, `this.id`

## Shim.clearResourceCache()
- 位置: L478-480
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.trackingProtection.clearResourceCache()`

## Shims.constructor()
- 位置: L484-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.appConstants.isInAutomation()`, `this.#initialize()`
- 条件付き依存: `if (!browser.trackingProtection)` → `console.error()`
- 条件付き依存: `if (browser.appConstants.isInAutomation())` → `browser.aboutConfigPrefs.getPref()`
- 条件付き依存: `if (override)` → `JSON.parse()`
- 参照: `browser.trackingProtection`, `this._originalShims`

## Shims.#initialize()
- 位置: async L503-576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `browser.aboutConfigPrefs.onPrefChange.addListener()`, `browser.tabs.get()`, `browser.tabs.reload()`, `browser.tabs.sendMessage()`, `browser.trackingProtection.onPrivateSessionEnd.addListener()`, `browser.trackingProtection.onSmartBlockEmbedReblock.addListener()`, `browser.trackingProtection.onSmartBlockEmbedUnblock.addListener()`, `onMessageFromTab()`, `shim.clearUserOptIns()`, `shim.onUserOptIn()`, `shim.onUserOptOut()`, `this._checkEnabledPref()`, `this._checkSmartblockEmbedsEnabledPref()`, `this._haveCheckedEnabledPrefsPromise.then()`, `this._onMessageFromShim.bind()`, `this._registerShims()`, `this.shims.get()`, `this.shims.values()`
- 条件付き依存: `if (!shim)` → `console.warn()`
- 参照: `(await browser.tabs.get(tabId)).incognito`, `this.ENABLED_PREF`, `this.SMARTBLOCK_EMBEDS_ENABLED_PREF`, `this._haveCheckedEnabledPrefs`, `this._haveCheckedEnabledPrefsPromise`, `this._readyPromise`, `this._resolveReady`

## Shims.ready()
- 位置: L578-580
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._readyPromise`

## Shims.bindAboutCompatBroker()
- 位置: L582-584
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._aboutCompatBroker`

## Shims.getShimInfoForAboutCompat()
- 位置: L586-590
- 役割: (未記入)
- 触るとき: (未記入)

## Shims.disableShimForSession()
- 位置: L592-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shim?.disableForSession()`, `this.shims.get()`

## Shims.enableShimForSession()
- 位置: L597-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shim?.enableForSession()`, `this.shims.get()`

## Shims.onShimStateChanged()
- 位置: L602-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._aboutCompatBroker.portsToAboutCompatTabs.broadcast()`, `this.getShimInfoForAboutCompat()`, `this.shims.get()`
- 参照: `this._aboutCompatBroker`

## Shims.getAvailableShims()
- 位置: L616-622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.shims.values()).map()`, `a.name.localeCompare()`, `shims.sort()`, `this.shims.values()`
- 参照: `b.name`, `this.getShimInfoForAboutCompat`

## Shims.onRemoteSettingsUpdate()
- 位置: async L624-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateShims()`
- 参照: `this._readyPromise`, `this._resolveReady`

## Shims._updateShims()
- 位置: async L631-636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._checkEnabledPref()`, `this._registerShims()`, `this._unregisterShims()`, `this.ready()`

## Shims._resetToDefaultShims()
- 位置: async L638-640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateShims()`
- 参照: `this._originalShims`

## Shims._registerShims()
- 位置: async L642-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(shims.values()) .filter()`, `Array.from(shims.values()) .filter( shim => !shim.isMissingFiles && shim.requestStorageAccessForRedirect ) .flatMap()`, `allLogos.push()`, `allMatchTypePatterns.entries()`, `debugLog()`, `registerShimListener()`, `shims.values()`, `this._ensureShimForRequestOnTab.bind()`, `this._registerContentScriptsForShims()`, `this.shims.has()`, `this.shims.values()`
- 条件付き依存: `if (!this.shims.has(id))` → `this.shims.set()`
- 条件付き依存: `if (redirectTargetUrls.length)` → `debugLog()`
- 条件付き依存: `if (redirectTargetUrls.length)` → `registerShimListener()`
- 条件付き依存: `if (redirectTargetUrls.length)` → `this._onRequestStorageAccessRedirect.bind()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `addTypePatterns()`
- 条件付き依存: `if (target || shim.file || shim.runFirst)` → `addTypePatterns()`
- 条件付き依存: `if (allLogos.length)` → `Array.from(new Set(allLogos)).map()`
- 条件付き依存: `if (allLogos.length)` → `Array.from()`
- 条件付き依存: `if (allLogos.length)` → `debugLog()`
- 条件付き依存: `if (allLogos.length)` → `registerShimListener()`
- 条件付き依存: `if (changeInfo.discarded || changeInfo.url)` → `unmarkShimsActive()`
- 条件付き依存: `if (allLogos.length)` → `this._redirectLogos.bind()`
- 条件付き依存: `if (allHeaderChangingMatchTypePatterns)` → `allHeaderChangingMatchTypePatterns.entries()`
- 条件付き依存: `if (allHeaderChangingMatchTypePatterns)` → `Array.from()`
- 条件付き依存: `if (allHeaderChangingMatchTypePatterns)` → `debugLog()`
- 条件付き依存: `if (allHeaderChangingMatchTypePatterns)` → `registerShimListener()`
- 条件付き依存: `if (allHeaderChangingMatchTypePatterns)` → `this._onBeforeSendHeaders.bind()`
- 条件付き依存: `if (allHeaderChangingMatchTypePatterns)` → `this._onHeadersReceived.bind()`
- 条件付き依存: `if (!allMatchTypePatterns.size)` → `debugLog()`
- 参照: `allLogos.length`, `allMatchTypePatterns.size`, `browser.tabs.onRemoved`, `browser.tabs.onUpdated`, `browser.webRequest.onBeforeRequest`, `browser.webRequest.onBeforeSendHeaders`, `browser.webRequest.onHeadersReceived`, `changeInfo.discarded`, `changeInfo.url`, `redirectTargetUrls.length`, `shim.file`, `shim.isGoogleTrendsDFPIFix`, `shim.isMissingFiles`, `shim.requestStorageAccessForRedirect`, `shim.runFirst`, `shimOpts.id`, `this._registeredShimListeners`, `this.shims`

## registerShimListener()
- 位置: L648-651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `api.addListener()`, `this._registeredShimListeners.push()`

## addTypePatterns()
- 位置: L691-699
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allSet.add()`, `set.get()`, `set.has()`
- 条件付き依存: `if (!set.has(type))` → `set.set()`
- 参照: `set.get(type).patterns`

## unmarkShimsActive()
- 位置: L727-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shim.setActiveOnTab()`, `this.shims.values()`

## Shims._unregisterShims()
- 位置: L786-795
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._registeredShimListeners)` → `api.removeListener()`
- 参照: `this._registeredShimListeners`, `this.enabled`, `this.shims`

## Shims._checkEnabledPref()
- 位置: async L797-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.getPref()`
- 参照: `this.ENABLED_PREF`, `this.enabled`

## Shims.enabled()
- 位置: L801-803
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._enabled`

## Shims.enabled()
- 位置: L805-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolveReady()`, `this.shims.values()`
- 条件付き依存: `if (enabled)` → `shim.onAllShimsEnabled()`
- 条件付き依存: `if (!(enabled))` → `shim.onAllShimsDisabled()`
- 参照: `this._enabled`, `this._resolveReady`

## Shims._checkSmartblockEmbedsEnabledPref()
- 位置: async L824-829
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPrefs.getPref()`
- 参照: `this.SMARTBLOCK_EMBEDS_ENABLED_PREF`, `this.smartblockEmbedsEnabled`

## Shims.smartblockEmbedsEnabled()
- 位置: L831-833
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._smartblockEmbedsEnabled`

## Shims.smartblockEmbedsEnabled()
- 位置: L835-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shims.values()`
- 参照: `shim.disabledBySmartblockEmbedPref`, `shim.isSmartblockEmbedShim`, `this._smartblockEmbedsEnabled`

## Shims._onRequestStorageAccessRedirect()
- 位置: async L849-945
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(bugNumbers) .map()`, `Array.from(bugNumbers) .map(bugNo => `https://bugzilla.mozilla.org/show_bug.cgi?id=${bugNo}`) .join()`, `Array.from(this.shims.values()).filter()`, `Promise.all()`, `browser.matchPatterns.getMatcher()`, `browser.matchPatterns.getMatcher([dstPattern]).matches()`, `browser.matchPatterns.getMatcher([srcPattern]).matches()`, `browser.tabs.executeScript()`, `browser.tabs.get()`, `browser.tabs.sendMessage()`, `bugNumbers.add()`, `console.error()`, `debugLog()`, `matchingShims.map()`, `requestStorageAccessForRedirect.some()`, `this.shims.values()`
- 条件付き依存: `if ( currentTabUrlOrigin && dstOrigin && currentTabUrlOrigin == dstOrigin )` → `debugLog()`
- 条件付き依存: `if (isDFPIActive === null)` → `browser.tabs.get()`
- 条件付き依存: `if (isDFPIActive === null)` → `browser.trackingProtection.isDFPIActive()`
- 参照: `(await browser.tabs.get(tabId)).incognito`, `bugNumbers.size`, `new URL(dstUrl).origin`, `new URL(tab.url).origin`, `shim.bug`, `shim.onlyIfDFPIActive`, `tab.url`

## Shims._onMessageFromShim()
- 位置: async L947-1030
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `shim?.needsShimHelpers?.includes()`, `this.shims.get()`
- 条件付き依存: `if (message === "getOptions")` → `Object.assign()`
- 条件付き依存: `if (message === "optIn")` → `shim.onUserOptIn()`
- 条件付き依存: `if (message === "optIn")` → `debugLog()`
- 条件付き依存: `if (message === "optIn")` → `shim.showOptInWarningOnce()`
- 条件付き依存: `if (message === "optIn")` → `console.error()`
- 条件付き依存: `if (message === "embedClicked")` → `browser.trackingProtection.openProtectionsPanel()`
- 条件付き依存: `if (message === "smartblockGetFluentString")` → `browser.trackingProtection.getSmartBlockEmbedFluentString()`
- 条件付き依存: `if (message === "checkFacebookLoginStatus")` → `browser.cookies.get()`
- 参照: `browser.runtime.id`, `new URL(tab.url).origin`, `new URL(url).hostname`, `sender.id`, `shim.name`, `shim.options`, `tab.incognito`, `tab.url`

## Shims._redirectLogos()
- 位置: async L1032-1066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URL(url).pathname.slice()`, `shim.isActiveOnTab()`, `shim.logos.includes()`, `this.shims.values()`
- 条件付き依存: `if (shim.onlyIfDFPIActive)` → `browser.tabs.get()`
- 条件付き依存: `if (shim.onlyIfDFPIActive)` → `browser.trackingProtection.isDFPIActive()`
- 条件付き依存: `if (shim.isActiveOnTab(tabId))` → `browser.runtime.getURL()`
- 参照: `(await browser.tabs.get(details.tabId)).incognito`, `details.tabId`, `shim.enabled`, `shim.onlyIfDFPIActive`, `shim.ready`, `this._haveCheckedEnabledPrefsPromise`, `this.enabled`

## Shims._onHeadersReceived()
- 位置: async L1068-1100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shims.values()`
- 条件付き依存: `if (shim.onlyIfDFPIActive)` → `browser.tabs.get()`
- 条件付き依存: `if (shim.onlyIfDFPIActive)` → `browser.trackingProtection.isDFPIActive()`
- 参照: `(await browser.tabs.get(details.tabId)).incognito`, `details.responseHeaders`, `details.tabId`, `details.url`, `header.name`, `header.value`, `shim.GoogleNidCookieToUse`, `shim.enabled`, `shim.isGoogleTrendsDFPIFix`, `shim.onlyIfDFPIActive`, `shim.ready`, `this._haveCheckedEnabledPrefsPromise`

## Shims._onBeforeSendHeaders()
- 位置: async L1102-1156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.shims.values()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `header.name.toLowerCase()`
- 条件付き依存: `if (!found)` → `requestHeaders.push()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `browser.tabs .get(tabId) .then()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `browser.tabs .get()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `debugLog()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `browser.tabs .executeScript()`
- 条件付き依存: `if (shim.isGoogleTrendsDFPIFix)` → `JSON.stringify()`
- 参照: `header.value`, `shim.GoogleNidCookieToUse`, `shim.bug`, `shim.enabled`, `shim.isGoogleTrendsDFPIFix`, `shim.ready`, `this._haveCheckedEnabledPrefsPromise`, `this.enabled`

## Shims._ensureShimForRequestOnTab()
- 位置: async L1159-1351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.tabs.get()`, `browser.trackingProtection.wasRequestUnblocked()`, `shim.isTriggeredByURLAndType()`, `shim.meantForHost()`, `this.shims.values()`
- 条件付き依存: `if (shim.onlyIfDFPIActive || shim.onlyIfPrivateBrowsing)` → `browser.trackingProtection.isDFPIActive()`
- 条件付き依存: `if (match)` → `shim.hasUserOptedInAlready()`
- 条件付き依存: `if (shim.hasUserOptedInAlready(topHost, isPB))` → `console.warn()`
- 条件付き依存: `if (shim.hasUserOptedInAlready(topHost, isPB))` → `shim.showOptInWarningOnce()`
- 条件付き依存: `if (shimToApply)` → `console.warn()`
- 条件付き依存: `if (shimToApply.isSmartblockEmbedShim)` → `browser.tabs.executeScript()`
- 条件付き依存: `if (runFirst)` → `browser.tabs.executeScript()`
- 条件付き依存: `if (runFirst)` → `shimToApply.setActiveOnTab()`
- 条件付き依存: `if (type === "script" && needsShimHelpers?.length)` → `browser.tabs.executeScript()`
- 条件付き依存: `if (type === "script" && needsShimHelpers?.length)` → `browser.tabs.sendMessage()`
- 条件付き依存: `if (type === "script" && needsShimHelpers?.length)` → `shimToApply.setActiveOnTab()`
- 条件付き依存: `if (needConsoleMessage)` → `browser.tabs.executeScript()`
- 条件付き依存: `if (needConsoleMessage)` → `JSON.stringify()`
- 条件付き依存: `if (shimToApply)` → `redirect.indexOf()`
- 条件付き依存: `if (shimToApply)` → `browser.runtime.getURL()`
- 条件付き依存: `if (unblocked)` → `console.error()`
- 条件付き依存: `if (!runFirst)` → `debugLog()`
- 参照: `(await browser.tabs.get(details.tabId)).incognito`, `(await browser.tabs.get(tabId)).url`, `details.parentFrameId`, `details.tabId`, `match.onlyIfBlockedByETP`, `needsShimHelpers?.length`, `new URL((await browser.tabs.get(tabId)).url).hostname`, `new URL(originUrl).origin`, `shim.enabled`, `shim.onlyIfBlockedByETP`, `shim.onlyIfDFPIActive`, `shim.onlyIfPrivateBrowsing`, `shim.ready`, `shim.redirectsRequests`, `shim.runFirst`, `shimToApply.isSmartblockEmbedShim`, `shimToApply.needsShimHelpers`, `shimToApply.runFirst`, `shimToApply.webExposedShimHelpers`, `this._haveCheckedEnabledPrefsPromise`, `this.enabled`

## Shims._registerContentScriptsForShims()
- 位置: async L1353-1410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.assign()`, `contentScriptsToRegister.push()`, `shim._contentScriptRegistrations.push()`
- 条件付き依存: `if (alsoClearObsoleteContentScripts)` → `InterventionHelpers.ensureOnlyTheseContentScripts()`
- 条件付き依存: `if (alsoClearObsoleteContentScripts)` → `browser.appConstants.isInAutomation()`
- 条件付き依存: `if (!(alsoClearObsoleteContentScripts))` → `InterventionHelpers.registerContentScripts()`
- 参照: `shim._contentScriptRegistrations`, `shim._contentScriptRegistrations.length`, `shim.contentScripts`, `shim.contentScripts.length`, `shim.disabledReason`, `shim.id`, `this._lastEnabledInfo`

## Shims._unregisterContentScriptsForShims()
- 位置: async L1412-1429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.scripting.unregisterContentScripts()`, `console.error()`, `ids.push()`, `this.shims.values()`
- 参照: `shim._contentScriptRegistrations`
