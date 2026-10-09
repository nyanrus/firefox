# browser/modules/AboutNewTab.sys.mjs

source: browser/modules/AboutNewTab.sys.mjs
source-hash: fde4f9eb767211f65ef72e3635775a38f5810aa2
lines: 366

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`

## init()
- 位置: L54-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `Services.prefs.getPrefType()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.AboutNewTabResourceMapping.init()`, `this.notifyChange()`, `this.toggleActivityStream()`
- 条件付き依存: `if (!AppConstants.RELEASE_OR_BETA)` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (!AppConstants.RELEASE_OR_BETA)` → `this.notifyChange()`
- 条件付き依存: `if ( Services.prefs.getPrefType(AStelemetryPref) === Services.prefs.PREF_INVALID )` → `Services.prefs .getDefaultBranch("") .setBoolPref()`
- 条件付き依存: `if ( Services.prefs.getPrefType(AStelemetryPref) === Services.prefs.PREF_INVALID )` → `Services.prefs .getDefaultBranch()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `AppConstants.RELEASE_OR_BETA`, `Services.prefs.PREF_INVALID`, `lazy.TelemetryReportingPolicy.TELEMETRY_TOU_ACCEPTED_OR_INELIGIBLE`, `this._activityStreamResolver`, `this.activityStreamPromise`, `this.initialized`
- XPCOM: `Services.obs` / `Services.prefs`

## toggleActivityStream()
- 位置: L125-142
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._activityStreamEnabled`, `this._newTabURL`, `this._newTabURLOverridden`

## newTabURL()
- 位置: L144-146
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._newTabURL`

## newTabURL()
- 位置: L148-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNewTabURL.trim()`, `this.notifyChange()`, `this.toggleActivityStream()`
- 条件付き依存: `if (newTabURL === ABOUT_URL)` → `this.resetNewTabURL()`
- 参照: `this._newTabURL`, `this._newTabURLOverridden`

## newTabURLOverridden()
- 位置: L164-166
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._newTabURLOverridden`

## activityStreamEnabled()
- 位置: L168-170
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._activityStreamEnabled`

## resetNewTabURL()
- 位置: L172-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.notifyChange()`, `this.toggleActivityStream()`
- 参照: `this._newTabURL`, `this._newTabURLOverridden`

## notifyChange()
- 位置: L179-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `this._newTabURL`
- XPCOM: `Services.obs`

## onBrowserReady()
- 位置: async L186-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/network/protocol/about;1?what=newtab" ].getService()`, `Glean.newtab.activityStreamCtorSuccess.set()`, `Promise.all()`, `Temporal.Instant.fromEpochMilliseconds()`, `console.error()`, `lazy .ProfileAge()`, `lazy .ProfileAge() .then()`, `lazy.AboutNewTabResourceMapping.scheduleUpdateTrainhopAddonState()`, `nimbusFeature.ready()`, `this._activityStreamResolver()`, `this._subscribeToActivityStream()`, `this.activityStream.init()`
- 参照: `Cc[ "@mozilla.org/network/protocol/about;1?what=newtab" ].getService(Ci.nsIAboutModule).wrappedJSObject`, `Ci.nsIAboutModule`, `accessor.created`, `lazy.ActivityStream`, `lazy.NimbusFeatures`, `redirector.promiseBuiltInAddonInitialized`, `this.activityStream`, `this.activityStream.initialized`
- XPCOM: [`nsIAboutModule`](../../netwerk/protocol/about/nsIAboutModule.idl.md) / `@mozilla.org/network/protocol/about;1?what=newtab`

## _subscribeToActivityStream()
- 位置: L250-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `store.getState()`, `store.getState().TopSites.rows.map()`, `store.subscribe()`
- 条件付き依存: `if (!lazy.ObjectUtils.deepEqual(topSites, this._cachedTopSites))` → `Services.obs.notifyObservers()`
- 参照: `site.screenshot`, `this._cachedTopSites`, `this._unsubscribeFromActivityStream`, `this.activityStream.store`
- XPCOM: `Services.obs`

## this._unsubscribeFromActivityStream()
- 位置: L268-274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `unsubscribe()`

## uninit()
- 位置: L280-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (this.activityStream)` → `this._unsubscribeFromActivityStream()`
- 条件付き依存: `if (this.activityStream)` → `this.activityStream.uninit()`
- 参照: `lazy.TelemetryReportingPolicy.TELEMETRY_TOU_ACCEPTED_OR_INELIGIBLE`, `this.activityStream`, `this.initialized`
- XPCOM: `Services.obs`

## getTopSites()
- 位置: L300-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.activityStream.store.getState()`
- 参照: `this.activityStream`, `this.activityStream.store.getState().TopSites.rows`

## getVisitId()
- 位置: L316-323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTabParent.loadedTabs.get()`, `telemetryFeed?.sessions.get()`, `this.activityStream?.store.feeds.get()`
- 参照: `lazy.AboutNewTabParent.loadedTabs.get(browser)?.portID`, `telemetryFeed?.sessions.get(portID)?.session_id`

## noteNonDefaultStartup()
- 位置: L328-330
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._nonDefaultStartup`

## maybeRecordTopsitesPainted()
- 位置: L332-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.timestamps.aboutHomeTopsitesFirstPaint.set()`, `Math.round()`, `Services.startup.getStartupInfo()`, `startupInfo.process.getTime()`
- 参照: `this._alreadyRecordedTopsitesPainted`, `this._nonDefaultStartup`
- XPCOM: `Services.startup`

## observe()
- 位置: L347-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.tm.dispatchToMainThread()`, `this.onBrowserReady()`, `this.uninit()`
- 参照: `lazy.TelemetryReportingPolicy.TELEMETRY_TOU_ACCEPTED_OR_INELIGIBLE`
- XPCOM: `Services.obs` / `Services.tm`
