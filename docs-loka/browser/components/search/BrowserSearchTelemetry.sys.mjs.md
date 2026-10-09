# browser/components/search/BrowserSearchTelemetry.sys.mjs

source: browser/components/search/BrowserSearchTelemetry.sys.mjs
source-hash: f9af3f2bd8c27a5caa30de05bd1c432907d5c754
lines: 419

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## BrowserSearchTelemetryHandler.shouldRecordSearchCount()
- 位置: L87-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `browser.documentGlobal`
- XPCOM: `Services.prefs`

## BrowserSearchTelemetryHandler.recordSearchSuggestionSelectionMethod()
- 位置: L103-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getClassName()`, `Glean.searchbar.selectedResultMethod[category].add()`
- 参照: `Glean.searchbar.selectedResultMethod`, `event.type`

## BrowserSearchTelemetryHandler.recordSearchMode()
- 位置: L135-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.urlbarSearchmode[name]?.[label].add()`, `lazy.UrlbarSearchUtils.getSearchModeScalarKey()`, `p.toUpperCase()`, `searchMode.entry.replace()`
- 参照: `Glean.urlbarSearchmode`, `searchMode.isPreview`

## BrowserSearchTelemetryHandler.recordSearch()
- 位置: L179-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sap.counts.record()`, `[ "about_home", "about_newtab", "newtab_searchbar", "urlbar_handoff", ].includes()`, `console.error()`, `engine.getURLOfType()`, `isOverridden.toString()`, `source.startsWith()`, `this.#recordSearch()`, `this._handleSearchAndUrlbar()`, `this.shouldRecordSearchCount()`
- 条件付き依存: `if (typeof engine == "string")` → `lazy.SearchService.getEngineById()`
- 条件付き依存: `if (engine.clickUrl)` → `this.#reportSearchInGlean()`
- 条件付き依存: `if (!(source in this.KNOWN_SEARCH_SOURCES))` → `console.error()`
- 条件付き依存: `if (source.startsWith("urlbar"))` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (source.startsWith("urlbar"))` → `Math.round()`
- 条件付き依存: `if (source.startsWith("urlbar"))` → `Date.now()`
- 条件付き依存: `if (source != "contextmenu_visual")` → `engine.aliases.includes()`
- 条件付き依存: `if ( details.alias && engine instanceof lazy.ConfigSearchEngine && engine.aliases.includes(details.alias) )` → `Glean.sap.deprecatedCounts[countIdPrefix + "alias"].add()`
- 条件付き依存: `if (!( details.alias && engine instanceof lazy.ConfigSearchEngine && engine.aliases.includes(details.alias) ))` → `Glean.sap.deprecatedCounts[countIdSource].add()`
- 条件付き依存: `if ( [ "about_home", "about_newtab", "newtab_searchbar", "urlbar_handoff", ].includes(source) )` → `Glean.newtabSearch.issued.record()`
- 条件付き依存: `if ( [ "about_home", "about_newtab", "newtab_searchbar", "urlbar_handoff", ].includes(source) )` → `lazy.SearchSERPTelemetry.recordBrowserNewtabSession()`
- 参照: `Glean.sap.deprecatedCounts`, `details.alias`, `details.newtabSessionId`, `details.searchUrlType`, `details.submission`, `details.submission.partnerCode`, `details.submission?.telemetryId`, `engine.clickUrl`, `engine.getURLOfType(searchUrlType)?.excludePartnerCodeFromTelemetry`, `engine.id`, `engine.name`, `engine.overriddenById`, `engine.partnerCode`, `engine.telemetryId`, `lazy.ConfigSearchEngine`, `lazy.SearchUtils.URL_TYPE.SEARCH`, `this.KNOWN_SEARCH_SOURCES`
- XPCOM: `Services.prefs`

## BrowserSearchTelemetryHandler.recordSearchForm()
- 位置: L310-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sap.searchFormCounts.record()`
- 参照: `engine.id`, `lazy.ConfigSearchEngine`

## BrowserSearchTelemetryHandler.recordSapImpression()
- 位置: L331-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sapImpressionCounts[name][label].add()`, `p.toUpperCase()`, `source.replace()`, `this.shouldRecordSearchCount()`
- 条件付き依存: `if (!(source in this.KNOWN_SEARCH_SOURCES))` → `console.error()`
- 参照: `Glean.sapImpressionCounts`, `engine.id`, `lazy.ConfigSearchEngine`, `this.KNOWN_SEARCH_SOURCES`

## BrowserSearchTelemetryHandler._handleSearchAndUrlbar()
- 位置: L358-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordSearch()`
- 参照: `details.alias`, `details.isFormHistory`, `details.isOneOff`, `details.isSuggestion`

## BrowserSearchTelemetryHandler.#recordSearch()
- 位置: L382-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browserEngagementNavigation[name][label].add()`, `lazy.SearchSERPTelemetry.recordBrowserSource()`, `p.toUpperCase()`, `source.replace()`
- 参照: `Glean.browserEngagementNavigation`

## BrowserSearchTelemetryHandler.#reportSearchInGlean()
- 位置: async L396-415
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ContextId.request()`, `sendGleanPing()`

## sendGleanPing()
- 位置: L401-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GleanPings.searchWith.submit()`, `Object.entries()`
- 条件付き依存: `if (value !== undefined && value !== "")` → `glean.set()`
- 参照: `Glean.searchWith`
