# browser/components/urlbar/UrlbarPrefs.sys.mjs

source: browser/components/urlbar/UrlbarPrefs.sys.mjs
source-hash: e044c8a6dfceb9028a0ac7b309df1d2f583cb8e1
lines: 1703

## <module>
- 役割: (未記入)
- 呼び出し先: `(1000 * 60 * 60 * 24 * 3).toString()`, `XPCOMUtils.declareLazy()`

## makeDefaultResultGroups()
- 位置: L897-1038
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rootGroup.children.push()`
- 条件付き依存: `if (!showSearchSuggestionsFirst)` → `mainGroup.children.reverse()`
- 参照: `lazy.UrlbarShared.RESULT_GROUP .HEURISTIC_RESTRICT_KEYWORD_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_BOOKMARK_KEYWORD`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_ENGINE_ALIAS`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_HISTORY_URL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_SEARCH_TIP`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TOKEN_ALIAS_ENGINE`, `lazy.UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_GROUP.RESTRICT_SEARCH_KEYWORD`, `lazy.UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `mainGroup.children`, `mainGroup.children[0].flex`, `mainGroup.children[1].flex`

## makeSmartBarGroups()
- 位置: L1048-1165
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!showSearchSuggestionsFirst)` → `mainGroup.children.reverse()`
- 参照: `generalBranch.flex`, `lazy.UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `lazy.UrlbarShared.RESULT_GROUP.AI`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL`, `lazy.UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AI_CHAT`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_HISTORY_URL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `lazy.UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `lazy.UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `mainGroup.children`, `searchBranch.flex`

## Preferences.constructor()
- 位置: L1174-1197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `PREF_OTHER_DEFAULTS_MAP.keys()`, `Services.prefs.addObserver()`, `lazy.NimbusFeatures.urlbar.onUpdate()`, `this._onNimbusUpdate()`, `this.addObserver()`
- 参照: `this.QueryInterface`, `this._map`, `this._observerWeakRefs`, `this.shouldHandOffToSearchModePrefs`
- XPCOM: `Services.prefs`

## Preferences.get()
- 位置: L1209-1216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._map.get()`
- 条件付き依存: `if (value === undefined)` → `this._getPrefValue()`
- 条件付き依存: `if (value === undefined)` → `this._map.set()`

## Preferences.set()
- 位置: L1228-1234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `set()`, `this._getPrefDescriptor()`

## Preferences.toggleResultMenuKeyboardAccessible()
- 位置: L1239-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.get()`, `this.set()`

## Preferences.add()
- 位置: L1255-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...maybeSet].join()`, `maybeSet.add()`, `this._getPrefValue()`, `this.set()`

## Preferences.clear()
- 位置: L1274-1277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clear()`, `this._getPrefDescriptor()`

## Preferences.hasUserValue()
- 位置: L1287-1290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasUserValue()`, `this._getPrefDescriptor()`

## Preferences.getScotchBonnetPref()
- 位置: L1301-1303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.get()`

## Preferences.#getShowSearchSuggestionsFirst()
- 位置: L1305-1318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.get()`
- 条件付き依存: `if (!inSearchEngineMode && showSearchSuggestionsFirst)` → `this.get()`
- 参照: `context.searchMode?.engineName`, `context.searchString`

## Preferences.getResultGroups()
- 位置: L1320-1368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeDefaultResultGroups()`, `makeSmartBarGroups()`, `this.#getOrCacheResultGroups()`, `this.#getShowSearchSuggestionsFirst()`, `this.get()`
- 参照: `context.sapName`

## Preferences.addObserver()
- 位置: L1382-1384
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `this._observerWeakRefs.push()`

## Preferences.removeObserver()
- 位置: L1392-1400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._observerWeakRefs[i].get()`
- 条件付き依存: `if (obs && obs == observer)` → `this._observerWeakRefs.splice()`
- 参照: `this._observerWeakRefs`, `this._observerWeakRefs.length`

## Preferences.observe()
- 位置: L1412-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PREF_OTHER_DEFAULTS_MAP.has()`, `PREF_URLBAR_DEFAULTS_MAP.has()`, `data.replace()`, `this.#notifyObservers()`

## Preferences.onPrefChanged()
- 位置: L1430-1457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pref.startsWith()`, `this.#cachedResultGroups.clear()`, `this._map.delete()`, `this.shouldHandOffToSearchModePrefs.includes()`
- 条件付き依存: `if (pref.startsWith("suggest."))` → `this._map.delete()`
- 条件付き依存: `if (this.shouldHandOffToSearchModePrefs.includes(pref))` → `this._map.delete()`

## Preferences._onNimbusUpdate()
- 位置: L1462-1479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `newNimbus.hasOwnProperty()`, `oldNimbus.hasOwnProperty()`, `this._clearNimbusCache()`, `variableNames.add()`
- 条件付き依存: `if ( oldNimbus.hasOwnProperty(name) != newNimbus.hasOwnProperty(name) || oldNimbus[name] !== newNimbus[name] )` → `this.#notifyObservers()`
- 参照: `this._nimbus`

## Preferences._clearNimbusCache()
- 位置: L1489-1498
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (nimbus)` → `Object.keys()`
- 条件付き依存: `if (nimbus)` → `this._map.delete()`
- 参照: `this.__nimbus`

## Preferences._nimbus()
- 位置: L1500-1507
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.__nimbus)` → `lazy.NimbusFeatures.urlbar.getAllVariables()`
- 参照: `this.__nimbus`

## Preferences._readPref()
- 位置: L1516-1519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `get()`, `this._getPrefDescriptor()`

## Preferences._getPrefValue()
- 位置: L1534-1582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `SUGGEST_PREF_TO_BEHAVIOR[ type ].toUpperCase()`, `parseFloat()`, `s.trim()`, `this._readPref()`, `this._readPref(pref) .split()`, `this._readPref(pref) .split(",") .map()`, `this._readPref(pref) .split(",") .map(s => s.trim()) .filter()`, `this.get()`, `this.shouldHandOffToSearchModePrefs.some()`
- 参照: `Ci.mozIPlacesAutoComplete`, `this._nimbus.autoFillAdaptiveHistoryUseCountThreshold`

## Preferences._getPrefDescriptor()
- 位置: L1591-1627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `PREF_URLBAR_DEFAULTS_MAP.get()`, `Services.prefs.getBranch()`
- 条件付き依存: `if (defaultValue === undefined)` → `PREF_OTHER_DEFAULTS_MAP.get()`
- 条件付き依存: `if (defaultValue === undefined)` → `this._getNimbusDescriptor()`
- 条件付き依存: `if (!Array.isArray(defaultValue))` → `PREF_TYPES.get()`
- 条件付き依存: `if (!(!Array.isArray(defaultValue)))` → `PREF_TYPES.get()`
- 参照: `Services.prefs`, `branch.clearUserPref`, `branch.prefHasUserValue`, `defaultValue.length`
- XPCOM: `Services.prefs`

## Preferences._getNimbusDescriptor()
- 位置: L1641-1660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._nimbus.hasOwnProperty()`
- 参照: `this._nimbus`

## get()
- 位置: L1647-1647
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._nimbus`

## Preferences.set()
- 位置: L1648-1650
- 役割: (未記入)
- 触るとき: (未記入)

## Preferences.clear()
- 位置: L1651-1653
- 役割: (未記入)
- 触るとき: (未記入)

## Preferences.hasUserValue()
- 位置: L1654-1658
- 役割: (未記入)
- 触るとき: (未記入)

## Preferences.#getOrCacheResultGroups()
- 位置: L1667-1674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cachedResultGroups.get()`
- 条件付き依存: `if (!groups)` → `builder()`
- 条件付き依存: `if (!groups)` → `this.#cachedResultGroups.set()`

## Preferences.#notifyObservers()
- 位置: L1676-1699
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._observerWeakRefs[i].get()`
- 条件付き依存: `if (!observer)` → `this._observerWeakRefs.splice()`
- 条件付き依存: `if (!inParent)` → `Cu.waiveXrays()`
- 条件付き依存: `if (method in observer)` → `observer[method]()`
- 条件付き依存: `if (method in observer)` → `console.error()`
- 参照: `this._observerWeakRefs`, `this._observerWeakRefs.length`
