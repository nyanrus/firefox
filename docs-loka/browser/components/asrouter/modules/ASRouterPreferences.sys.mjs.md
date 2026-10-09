# browser/components/asrouter/modules/ASRouterPreferences.sys.mjs

source: browser/components/asrouter/modules/ASRouterPreferences.sys.mjs
source-hash: 6795175a68ed6ddc0e7e589d2d9e1a2080615dd4
lines: 332

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Services.prefs.clearUserPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.SelectableProfileService.flushSharedPrefToDatabase()`

## _ASRouterPreferences.constructor()
- 位置: L86-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Object.assign()`
- 参照: `this._callbacks`

## _ASRouterPreferences._transformPersonalizedCfrScores()
- 位置: L104-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `console.error()`

## _ASRouterPreferences._getProviderConfig()
- 位置: L114-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.getChildList()`, `Services.prefs.getStringPref()`, `console.error()`, `prefList.reduce()`
- 条件付き依存: `if (value)` → `filtered.push()`
- 参照: `this._providerPrefBranch`
- XPCOM: `Services.prefs`

## _ASRouterPreferences.providers()
- 位置: L132-143
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized || this._providers === null)` → `this._getProviderConfig()`
- 条件付き依存: `if (!this._initialized || this._providers === null)` → `config.map()`
- 条件付き依存: `if (!this._initialized || this._providers === null)` → `Object.freeze()`
- 条件付き依存: `if (this.devtoolsEnabled)` → `providers.unshift()`
- 参照: `this._initialized`, `this._providers`, `this.devtoolsEnabled`

## _ASRouterPreferences.enableOrDisableProvider()
- 位置: L145-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `providers.find()`, `this._getProviderConfig()`
- 条件付き依存: `if (!config)` → `console.error()`
- 参照: `p.id`, `this._providerPrefBranch`
- XPCOM: `Services.prefs`

## _ASRouterPreferences.resetProviderPref()
- 位置: L161-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Services.prefs.clearUserPref()`, `Services.prefs.getChildList()`
- 参照: `this._providerPrefBranch`
- XPCOM: `Services.prefs`

## _ASRouterPreferences._migrateProviderPrefs()
- 位置: L176-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Services.prefs.clearUserPref()`, `Services.prefs.getChildList()`, `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (value && "bucket" in value && !("collection" in value))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (value && "bucket" in value && !("collection" in value))` → `JSON.stringify()`
- 参照: `this._providerPrefBranch`
- XPCOM: `Services.prefs`

## _ASRouterPreferences._maybeSetMessagingProfileID()
- 位置: async L200-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.SelectableProfileService.currentProfile?.id?.toString()`, `lazy.SelectableProfileService.init()`
- 条件付き依存: `if (!lazy.messagingProfileId && currentProfileID)` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!lazy.messagingProfileId && currentProfileID)` → `lazy.SelectableProfileService.trackPref()`
- 条件付き依存: `if ( lazy.messagingProfileId && lazy.SelectableProfileService.initialized )` → `lazy.SelectableProfileService.getProfile()`
- 条件付き依存: `if ( lazy.messagingProfileId && lazy.SelectableProfileService.initialized )` → `parseInt()`
- 条件付き依存: `if (!messagingProfile)` → `Services.prefs.setStringPref()`
- 参照: `lazy.SelectableProfileService.initialized`, `lazy.disableSingleProfileMessaging`, `lazy.messagingProfileId`
- XPCOM: `Services.prefs`

## _ASRouterPreferences.devtoolsEnabled()
- 位置: L242-250
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._initialized || this._devtoolsEnabled === null)` → `Services.prefs.getBoolPref()`
- 参照: `this._devtoolsEnabled`, `this._devtoolsPref`, `this._initialized`
- XPCOM: `Services.prefs`

## _ASRouterPreferences.observe()
- 位置: L252-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aPrefName.startsWith()`, `cb()`, `this._callbacks.forEach()`
- 参照: `this._devtoolsEnabled`, `this._devtoolsPref`, `this._providerPrefBranch`, `this._providers`

## _ASRouterPreferences.getUserPreference()
- 位置: L262-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## _ASRouterPreferences.getAllUserPreferences()
- 位置: L267-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `this.getUserPreference()`

## _ASRouterPreferences.setUserPreference()
- 位置: L275-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _ASRouterPreferences.addListener()
- 位置: L282-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callbacks.add()`

## _ASRouterPreferences.removeListener()
- 位置: L286-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._callbacks.delete()`

## _ASRouterPreferences.init()
- 位置: L290-309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `this._maybeSetMessagingProfileID()`, `this._migrateProviderPrefs()`
- 参照: `this._devtoolsPref`, `this._initialized`, `this._maybeSetMessagingProfileID`, `this._providerPrefBranch`
- XPCOM: `Services.obs` / `Services.prefs`

## _ASRouterPreferences.uninit()
- 位置: L311-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `this._callbacks.clear()`
- 条件付き依存: `if (this._initialized)` → `Services.prefs.removeObserver()`
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._initialized)` → `Object.keys()`
- 参照: `this._devtoolsPref`, `this._initialized`, `this._maybeSetMessagingProfileID`, `this._providerPrefBranch`
- XPCOM: `Services.obs` / `Services.prefs`
