# browser/components/sessionstore/TabState.sys.mjs

source: browser/components/sessionstore/TabState.sys.mjs
source-hash: dd70542d768543591f9b78f5109fde7b5d5e1f5a
lines: 353

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## _TabState.update()
- 位置: L123-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabStateCache.update()`

## _TabState.collect()
- 位置: L139-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectBaseTabData()`

## _TabState.clone()
- 位置: L156-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#collectBaseTabData()`

## _TabState.#collectBaseTabData()
- 位置: L171-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabAttributes.get()`, `tab.documentGlobal.gURLBar.getSearchMode()`, `this.copyFromCache()`
- 条件付き依存: `if (!options.includePrivateData)` → `lazy.PrivacyFilter.filterCanonicalUrl()`
- 条件付き依存: `if (!("image" in tabData))` → `tabbrowser.getIcon()`
- 条件付き依存: `if (!("userTypedValue" in tabData) && browser.userTypedValue)` → `browser.didStartLoadSinceLastUserTyping()`
- 参照: `browser.permanentKey`, `browser.userTypedValue`, `options.extData`, `options.includePrivateData`, `tab.canonicalUrl`, `tab.documentGlobal.gBrowser`, `tab.group`, `tab.group.id`, `tab.hidden`, `tab.lastAccessed`, `tab.linkedBrowser`, `tab.muteReason`, `tab.muted`, `tab.pinned`, `tab.splitview`, `tab.splitview.splitViewId`, `tab.userContextId`, `tabData.attributes`, `tabData.canonicalUrl`, `tabData.extData`, `tabData.groupId`, `tabData.hidden`, `tabData.image`, `tabData.muteReason`, `tabData.muted`, `tabData.pinned`, `tabData.searchMode`, `tabData.splitViewId`, `tabData.userContextId`, `tabData.userTypedClear`, `tabData.userTypedValue`

## _TabState.processAboutRestartrequiredEnties()
- 位置: L256-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEntries.some()`, `e.url.startsWith()`, `newEntries.forEach()`, `structuredClone()`
- 条件付き依存: `if (item.url === "about:restartrequired")` → `object.splice()`
- 条件付き依存: `if (!(item.url === "about:restartrequired"))` → `item.url.startsWith()`
- 条件付き依存: `if (item.url.startsWith("about:restartrequired"))` → `parsedURL.searchParams.has()`
- 条件付き依存: `if (parsedURL && parsedURL.searchParams.has("u"))` → `parsedURL.searchParams.get()`
- 条件付き依存: `if (item.url.startsWith("about:restartrequired"))` → `lazy.sessionStoreLogger.error()`
- 参照: `e.url`, `item.url`, `object[index].url`

## _TabState.copyFromCache()
- 位置: L300-349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `lazy.TabStateCache.get()`
- 条件付き依存: `if (key === "storage")` → `lazy.PrivacyFilter.filterSessionStorageData()`
- 条件付き依存: `if (key === "formdata")` → `lazy.PrivacyFilter.filterFormData()`
- 条件付き依存: `if (key === "history")` → `value.hasOwnProperty()`
- 条件付き依存: `if (key === "history")` → `this.processAboutRestartrequiredEnties()`
- 参照: `options.includePrivateData`, `tabData.entries`, `tabData.index`, `tabData.requestedIndex`, `value.entries`, `value.index`, `value.requestedIndex`
