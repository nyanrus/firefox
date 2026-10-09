# browser/components/urlbar/UrlbarProviderRemoteTabs.sys.mjs

source: browser/components/urlbar/UrlbarProviderRemoteTabs.sys.mjs
source-hash: ec3635f3c0d4c34447548959db3e7f3bbf1888b5
lines: 245

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/weave/service;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## escapeRegExp()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `string.replace()`

## _cache.constructor()
- 位置: L62-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this.observe.bind()`
- XPCOM: `Services.obs`

## _cache.#buildItems()
- 位置: async L76-93
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.weaveXPCService.ready)` → `lazy.SyncedTabs.getTabClients()`
- 条件付き依存: `if (lazy.weaveXPCService.ready)` → `lazy.SyncedTabs.sortTabClientsByLastUsed()`
- 条件付き依存: `if (lazy.weaveXPCService.ready)` → `tabsData.push()`
- 参照: `client.tabs`, `lazy.weaveXPCService.ready`, `this.#tabsData`

## _cache.observe()
- 位置: L95-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#tabsData`

## _cache.get()
- 位置: async L121-128
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!_cache.#instance.#tabsData)` → `_cache.#instance.#buildItems()`
- 参照: `_cache.#instance`, `_cache.#instance.#tabsData`

## UrlbarProviderRemoteTabs.constructor()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`

## UrlbarProviderRemoteTabs.type()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.NETWORK`

## UrlbarProviderRemoteTabs.isActive()
- 位置: async L153-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.sources.includes()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.syncUsernamePref`, `lazy.weaveXPCService`, `lazy.weaveXPCService.enabled`, `lazy.weaveXPCService.ready`

## UrlbarProviderRemoteTabs.startQuery()
- 位置: async L171-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_cache.get()`, `addCallback()`, `escapeRegExp()`, `queryContext.tokens.map()`, `queryContext.tokens.map(t => t.value).join()`, `re.test()`, `staleTabs.shift()`
- 条件付き依存: `if ( !searchString || searchString == lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE || re.test(tab.url) || (tab.title && re.test(tab.title)) )` → `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if ( !searchString || searchString == lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE || re.test(tab.url) || (tab.title && re.test(tab.title)) )` → `Date.now()`
- 条件付き依存: `if ( tab.lastUsed <= (Date.now() - RECENT_REMOTE_TAB_THRESHOLD_MS) / 1000 )` → `staleTabs.push()`
- 条件付き依存: `if (!( tab.lastUsed <= (Date.now() - RECENT_REMOTE_TAB_THRESHOLD_MS) / 1000 ))` → `addCallback()`
- 参照: `client.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `lazy.showRemoteIconsPref`, `queryContext.maxResults`, `staleTabs.length`, `t.value`, `tab.lastUsed`, `tab.title`, `tab.url`, `this.queryInstance`
