# browser/components/urlbar/UrlbarProviderPlaces.sys.mjs

source: browser/components/urlbar/UrlbarProviderPlaces.sys.mjs
source-hash: d4f7db9d7debb99f3e6727d785a6bf94227e323b
lines: 1662

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `Object.values()`, `Object.values(MATCH_TYPE).reduce()`, `XPCOMUtils.declareLazy()`

## defaultQuery()
- 位置: L42-73
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PAGES_FRECENCY_FIELD`

## PAGES_FRECENCY_FIELD()
- 位置: L114-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.PlacesUtils.history.isAlternativeFrecencyEnabled`

## typeToBehaviorMap()
- 位置: L120-132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_BOOKMARK`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_OPENPAGE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_URL`

## sourceToBehaviorMap()
- 位置: L133-142
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`

## setTimeout()
- 位置: L145-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `timer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## makeMapKeyForResult()
- 位置: L163-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.tupleString()`, `lazy.PlacesUtils.parseActionUrl()`, `lazy.UrlbarShared.isNonPrivateUserContextId()`
- 参照: `action?.type`, `match.userContextId`, `match.value`

## makeKeyForMatch()
- 位置: L185-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( action.params.searchSuggestion || action.params.searchQuery ).toLocaleLowerCase()`, `lazy.PlacesUtils.parseActionUrl()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `makeMapKeyForResult()`
- 条件付き依存: `if (!action)` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if (!action)` → `makeMapKeyForResult()`
- 参照: `action.params.engineName`, `action.params.searchQuery`, `action.params.searchSuggestion`, `action.params.url`, `action.type`, `match.value`

## makeActionUrl()
- 位置: L239-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `encodeURIComponent()`

## convertLegacyMatches()
- 位置: L263-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeMapKeyForResult()`, `makeUrlbarResult()`, `results.push()`, `urls.add()`, `urls.has()`
- 参照: `match.bookmarkDateMs`, `match.comment`, `match.finalCompleteValue`, `match.frecency`, `match.icon`, `match.lastVisit`, `match.style`, `match.tabGroup`, `match.userContextId`, `match.value`

## makeUrlbarResult()
- 位置: L315-437
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info.style.includes()`, `lazy.PlacesUtils.parseActionUrl()`
- 条件付き依存: `if (action)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (action)` → `action.params.searchSuggestion.toLocaleLowerCase()`
- 条件付き依存: `if (action)` → `UrlbarUtils.getUserContextData()`
- 条件付き依存: `if (action)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (action)` → `UrlbarUtils.createTabSwitchSecondaryAction()`
- 条件付き依存: `if (action)` → `console.error()`
- 条件付き依存: `if (!(info.style.includes("bookmark")))` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (info.style.includes("tag"))` → `info.title.split()`
- 条件付き依存: `if (info.style.includes("tag"))` → `titleTags.split(",").filter()`
- 条件付き依存: `if (info.style.includes("tag"))` → `titleTags.split()`
- 条件付き依存: `if (info.style.includes("tag"))` → `tag.toLocaleLowerCase()`
- 条件付き依存: `if (info.style.includes("tag"))` → `queryContext.tokens.some()`
- 条件付き依存: `if (info.style.includes("tag"))` → `lowerCaseTag.includes()`
- 参照: `action.params.engineName`, `action.params.searchSuggestion`, `action.params.url`, `action.type`, `info.bookmarkDateMs`, `info.frecency`, `info.icon`, `info.lastVisit`, `info.tabGroup`, `info.title`, `info.url`, `info.userContextId`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `lazy.UrlbarShared.TITLE_TAGS_SEPARATOR`, `token.lowerCaseValue`
- XPCOM: `Services.urlFormatter`

## Search.constructor()
- 位置: L459-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.unEscapeURIForUI()`, `lazy.UrlbarTokenizer.tokenize()`, `lazy.sourceToBehaviorMap.has()`, `queryContext.restrictInSearchMode()`, `this.filterTokens()`, `unescapedSearchString.startsWith()`, `unescapedSearchString.trim()`
- 条件付き依存: `if (!(unescapedSearchString.startsWith("about:")))` → `UrlbarUtils.stripURLPrefix()`
- 条件付き依存: `if (this.#searchModeEngine && queryContext.restrictInSearchMode())` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (tokens.length)` → `lazy.UrlbarTokenizer.isRestrictionToken()`
- 条件付き依存: `if ( prefix && prefix != "about:" && tokens[0].value.length > prefix.length )` → `tokens[0].value.substring()`
- 条件付き依存: `if ( queryContext && queryContext.restrictSource && lazy.sourceToBehaviorMap.has(queryContext.restrictSource) )` → `this.setBehavior()`
- 条件付き依存: `if ( queryContext && queryContext.restrictSource && lazy.sourceToBehaviorMap.has(queryContext.restrictSource) )` → `lazy.sourceToBehaviorMap.get()`
- 条件付き依存: `if (!( queryContext && queryContext.restrictSource && lazy.sourceToBehaviorMap.has(queryContext.restrictSource) ))` → `this.#trimmedOriginalSearchString.startsWith()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("filter.javascript"))` → `this.setBehavior()`
- 参照: `engine.searchUrlDomain`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `prefix.length`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.maxResults`, `queryContext.restrictSource`, `queryContext.restrictToken`, `queryContext.searchMode?.engineName`, `queryContext.searchString`, `queryContext.trimmedSearchString`, `queryContext.userContextId`, `this.#behavior`, `this.#currentPage`, `this.#emptySearchDefaultBehavior`, `this.#filterOnHost`, `this.#heuristicToken`, `this.#inPrivateWindow`, `this.#leadingRestrictionToken`, `this.#listener`, `this.#maxResults`, `this.#originalSearchString`, `this.#provider`, `this.#queryContext`, `this.#searchModeEngine`, `this.#searchString`, `this.#searchTokens`, `this.#searchTokens.length`, `this.#searchTokens[0].value`, `this.#trimmedOriginalSearchString`, `this.#userContextId`, `tokens.length`, `tokens[0].type`, `tokens[0].value`, `tokens[0].value.length`

## Search.setBehavior()
- 位置: L582-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `type.toUpperCase()`
- 参照: `Ci.mozIPlacesAutoComplete`, `this.#behavior`

## Search.hasBehavior()
- 位置: L594-597
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `type.toUpperCase()`
- 参照: `Ci.mozIPlacesAutoComplete`, `this.#behavior`

## Search.filterTokens()
- 位置: L607-636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarTokenizer.isRestrictionToken()`, `lazy.typeToBehaviorMap.get()`, `this.setBehavior()`
- 条件付き依存: `if (!lazy.UrlbarTokenizer.isRestrictionToken(token))` → `filtered.push()`
- 条件付き依存: `if (!foundToken)` → `this.setBehavior()`
- 条件付き依存: `if (behavior == "tag")` → `this.setBehavior()`
- 参照: `this.#behavior`, `token.type`

## Search.stop()
- 位置: L643-656
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#notifyTimer)` → `this.#notifyTimer.cancel()`
- 条件付き依存: `if (typeof this.#interrupt == "function")` → `this.#interrupt()`
- 参照: `this.#interrupt`, `this.#notifyDelaysCount`, `this.#notifyTimer`, `this.pending`

## Search.execute()
- 位置: async L669-761
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conn.executeCached()`, `lazy.UrlbarSearchUtils.tokenAliasEngines()`, `queries.push()`, `this.#checkIfFirstTokenIsKeyword()`, `this.#onResultRow.bind()`, `this.hasBehavior()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString == "@" && tokenAliasEngines.length)` → `this.#provider.finishSearch()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString)` → `/\s*\S?$/.test()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString)` → `this.#trimmedOriginalSearchString.startsWith()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString)` → `this.hasBehavior()`
- 条件付き依存: `if ( emptySearchRestriction || (tokenAliasEngines.length && this.#trimmedOriginalSearchString.startsWith("@")) || (this.hasBehavior("search") && this.hasBehavior...)` → `this.#provider.finishSearch()`
- 条件付き依存: `if (this.hasBehavior("openpage"))` → `queries.push()`
- 条件付き依存: `if (count < this.#maxResults)` → `this.hasBehavior()`
- 条件付き依存: `if (this.hasBehavior("openpage"))` → `queries.unshift()`
- 条件付き依存: `if (count < this.#maxResults)` → `conn.executeCached()`
- 条件付き依存: `if (count < this.#maxResults)` → `this.#onResultRow.bind()`
- 参照: `Ci.mozIPlacesAutoComplete.MATCH_ANYWHERE`, `MATCH_TYPE.GENERAL`, `lazy.UrlbarProviderOpenTabs.promiseDBPopulated`, `lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH`, `this.#counts`, `this.#firstTokenIsKeyword`, `this.#interrupt`, `this.#leadingRestrictionToken`, `this.#matchBehavior`, `this.#maxResults`, `this.#searchQuery`, `this.#switchToTabQuery`, `this.#trimmedOriginalSearchString`, `this.#trimmedOriginalSearchString.length`, `this.pending`, `tokenAliasEngines.length`

## this.#interrupt()
- 位置: L676-681
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!lazy.ProvidersManager.interruptLevel)` → `conn.interrupt()`
- 参照: `lazy.ProvidersManager.interruptLevel`

## Search.#checkIfFirstTokenIsKeyword()
- 位置: async L818-842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.KeywordUtils.getBindableKeyword()`, `lazy.UrlbarSearchUtils.engineForAlias()`
- 参照: `entry.url.host`, `this.#filterOnHost`, `this.#heuristicToken`, `this.#originalSearchString`

## Search.#onResultRow()
- 位置: L844-853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addFilteredQueryMatch()`
- 条件付き依存: `if (!this.pending || count >= this.#maxResults)` → `cancel()`
- 参照: `MATCH_TYPE.GENERAL`, `this.#counts`, `this.#maxResults`, `this.pending`

## Search.#maybeRestyleSearchMatch()
- 位置: L876-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.getSearchQueryUrl()`, `lazy.SearchService.parseSubmissionURL()`, `lazy.UrlbarSearchUtils.serpsAreEquivalent()`, `makeActionUrl()`, `parseResult.terms.toLowerCase()`, `terms.includes()`, `this.#searchTokens.every()`, `this.#searchTokens.map()`, `this.#searchTokens.map(t => t.value).join()`
- 参照: `match.comment`, `match.icon`, `match.iconUrl`, `match.style`, `match.value`, `parseResult.engine`, `parseResult.engine.name`, `parseResult.terms`, `parseResult.termsParameterName`, `parseResult?.engine`, `t.value`, `this.#searchTokens.length`, `token.value`

## Search.#addMatch()
- 位置: L927-974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#getInsertIndexForMatch()`, `this.#matches.splice()`, `this.notifyResult()`
- 条件付き依存: `if ( match.style == "favicon" && (lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine) )` → `this.#maybeRestyleSearchMatch()`
- 条件付き依存: `if ( match.style == "favicon" && (lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine) )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (replace)` → `this.#matches.splice()`
- 参照: `MATCH_TYPE.GENERAL`, `match.finalCompleteValue`, `match.frecency`, `match.icon`, `match.style`, `match.type`, `this.#counts`, `this.#searchModeEngine`, `this.pending`

## Search.#getInsertIndexForMatch()
- 位置: L997-1127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `makeKeyForMatch()`, `makeMapKeyForResult()`, `this.#usedPlaceIds.has()`, `this.#usedURLs.some()`
- 条件付き依存: `if ( (match.placeId && this.#usedPlaceIds.has(makeMapKeyForResult(match.placeId, match))) || this.#usedURLs.some(e => lazy.ObjectUtils.deepEqual(e.key, urlMapKey)) )` → `["switchtab", "remotetab"].includes()`
- 条件付き依存: `if (action && ["switchtab", "remotetab"].includes(action.type))` → `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (!(action && ["switchtab", "remotetab"].includes(action.type)))` → `UrlbarUtils.getPrefixRank()`
- 条件付き依存: `if (!(action && ["switchtab", "remotetab"].includes(action.type)))` → `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (lazy.ObjectUtils.deepEqual(existingKey, urlMapKey))` → `prefix.endsWith()`
- 条件付き依存: `if (lazy.ObjectUtils.deepEqual(existingKey, urlMapKey))` → `existingPrefix.endsWith()`
- 条件付き依存: `if (match.placeId)` → `this.#usedPlaceIds.add()`
- 条件付き依存: `if (match.placeId)` → `makeMapKeyForResult()`
- 条件付き依存: `if (!this.#groups)` → `this.#makeGroups()`
- 条件付き依存: `if (!this.#groups)` → `lazy.UrlbarPrefs.getResultGroups()`
- 参照: `action.type`, `e.key`, `group.available`, `group.count`, `group.insertIndex`, `group.type`, `match.comment`, `match.placeId`, `match.type`, `this.#groups`, `this.#maxResults`, `this.#queryContext`, `this.#usedURLs`, `this.#usedURLs.length`

## Search.#makeGroups()
- 位置: L1129-1186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `this.#makeGroups()`
- 条件付き依存: `if (!resultGroup.children)` → `this.#groups.push()`
- 参照: `MATCH_TYPE.EXTENSION`, `MATCH_TYPE.GENERAL`, `MATCH_TYPE.HEURISTIC`, `MATCH_TYPE.SUGGESTION`, `last.type`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_SEARCH_TIP`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TOKEN_ALIAS_ENGINE`, `lazy.UrlbarShared.RESULT_GROUP.OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `lazy.UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `resultGroup.availableSpan`, `resultGroup.children`, `resultGroup.group`, `resultGroup.maxResultCount`, `this.#groups`, `this.#groups.length`, `this.#maxResults`

## Search.#addFilteredQueryMatch()
- 位置: L1188-1250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.toDate()`, `lazy.PlacesUtils.toDate(bookmarkDatePRTime).getTime()`, `lazy.PlacesUtils.toDate(lastVisitPRTime).getTime()`, `lazy.UrlbarShared.getIconForUrl()`, `row.getResultByName()`, `this.#addMatch()`, `this.hasBehavior()`
- 条件付き依存: `if (openPageCount > 0 && this.hasBehavior("openpage"))` → `makeActionUrl()`
- 条件付き依存: `if (!(openPageCount > 0 && this.hasBehavior("openpage")))` → `this.hasBehavior()`
- 条件付き依存: `if (tags)` → `this.hasBehavior()`
- 参照: `lazy.UrlbarShared.TITLE_TAGS_SEPARATOR`, `match.comment`, `match.style`, `match.userContextId`, `match.value`, `this.#currentPage`, `this.#userContextId`

## Search.#suggestionPrefQuery()
- 位置: L1257-1327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conditions.join()`, `defaultQuery()`, `this.hasBehavior()`
- 条件付き依存: `if (this.#filterOnHost)` → `conditions.push()`
- 条件付き依存: `if (this.#filterOnHost)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine)` → `conditions.push()`
- 条件付き依存: `if (!(lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine))` → `conditions.push()`
- 条件付き依存: `if ( this.hasBehavior("restrict") || (!this.hasBehavior("openpage") && (!this.hasBehavior("history") || !this.hasBehavior("bookmark"))) )` → `this.hasBehavior()`
- 条件付き依存: `if (this.hasBehavior("history"))` → `conditions.push()`
- 条件付き依存: `if (this.hasBehavior("bookmark"))` → `conditions.push()`
- 条件付き依存: `if (this.hasBehavior("tag"))` → `conditions.push()`
- 参照: `this.#filterOnHost`, `this.#searchModeEngine`

## Search.#emptySearchDefaultBehavior()
- 位置: L1329-1343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(lazy.UrlbarPrefs.get("suggest.history")))` → `lazy.UrlbarPrefs.get()`
- 参照: `Ci.mozIPlacesAutoComplete.BEHAVIOR_BOOKMARK`, `Ci.mozIPlacesAutoComplete.BEHAVIOR_HISTORY`, `Ci.mozIPlacesAutoComplete.BEHAVIOR_OPENPAGE`, `Ci.mozIPlacesAutoComplete.BEHAVIOR_RESTRICT`

## Search.#keywordFilteredSearchString()
- 位置: L1351-1357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#searchTokens.map()`, `tokens.join()`
- 条件付き依存: `if (this.#firstTokenIsKeyword)` → `tokens.slice()`
- 参照: `t.value`, `this.#firstTokenIsKeyword`

## Search.#searchQuery()
- 位置: L1367-1389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `this.hasBehavior()`
- 参照: `lazy.PlacesUtils.tagsFolderId`, `params.host`, `params.userContextId`, `this.#behavior`, `this.#filterOnHost`, `this.#inPrivateWindow`, `this.#keywordFilteredSearchString`, `this.#matchBehavior`, `this.#maxResults`, `this.#suggestionPrefQuery`

## Search.#switchToTabQuery()
- 位置: L1398-1414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`
- 参照: `this.#behavior`, `this.#inPrivateWindow`, `this.#keywordFilteredSearchString`, `this.#matchBehavior`, `this.#maxResults`

## Search.notifyResult()
- 位置: L1432-1458
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#notifyTimer)` → `this.#notifyTimer.cancel()`
- 条件付き依存: `if (this.#notifyDelaysCount > 3)` → `notify()`
- 条件付き依存: `if (!(this.#notifyDelaysCount > 3))` → `setTimeout()`
- 参照: `this.#notifyDelaysCount`, `this.#notifyTimer`

## notify()
- 位置: L1433-1445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listener()`
- 条件付き依存: `if (!searchOngoing)` → `this.stop()`
- 参照: `this.#listener`, `this.#matches`, `this.#notifyDelaysCount`, `this.#provider`, `this.pending`

## UrlbarProviderPlaces.type()
- 位置: L1481-1483
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderPlaces.getDatabaseHandle()
- 位置: L1492-1512
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!_promiseDatabase)` → `lazy.PlacesUtils.promiseLargeCacheDBConnection()`
- 条件付き依存: `if (!_promiseDatabase)` → `lazy.Sqlite.shutdown.addBlocker()`
- 条件付き依存: `if (!_promiseDatabase)` → `dump()`
- 条件付き依存: `if (!_promiseDatabase)` → `this.logger.error()`
- 参照: `this.#currentSearch`

## UrlbarProviderPlaces.isActive()
- 位置: async L1521-1529
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `queryContext.searchMode?.engineName`, `queryContext.trimmedSearchString`

## UrlbarProviderPlaces.startQuery()
- 位置: L1538-1551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addCallback()`, `convertLegacyMatches()`, `this.#startLegacyQuery()`
- 参照: `this.#deferred.promise`, `this.queryInstance`

## UrlbarProviderPlaces.cancelQuery()
- 位置: L1556-1566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.finishSearch()`
- 条件付き依存: `if (this.#currentSearch)` → `this.#currentSearch.stop()`
- 条件付き依存: `if (this.#deferred)` → `this.#deferred.resolve()`
- 参照: `this.#currentSearch`, `this.#deferred`

## UrlbarProviderPlaces.finishSearch()
- 位置: L1575-1596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `search.notifyResult()`
- 参照: `search.pending`, `this.#currentSearch`

## UrlbarProviderPlaces.onEngagement()
- 位置: L1603-1624
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (details.selType == "dismiss")` → `UrlbarUtils.getUrlFromResult()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove(url).catch()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history .remove(result.payload.url) .catch()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history .remove()`
- 参照: `console.error`, `details.selType`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `result.payload.url`, `result.type`

## UrlbarProviderPlaces.#startLegacyQuery()
- 位置: L1626-1636
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `this.#startSearch()`
- 参照: `queryContext.searchString`, `this.#deferred`

## listener()
- 位置: L1628-1633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`
- 条件付き依存: `if (!searchOngoing)` → `deferred.resolve()`

## UrlbarProviderPlaces.#startSearch()
- 位置: L1638-1660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dump()`, `search.execute()`, `this.getDatabaseHandle()`, `this.getDatabaseHandle() .then()`, `this.getDatabaseHandle() .then(conn => search.execute(conn)) .catch()`, `this.logger.error()`
- 条件付き依存: `if (this.#currentSearch)` → `this.cancelQuery()`
- 条件付き依存: `if (search == this.#currentSearch)` → `this.finishSearch()`
- 参照: `this.#currentSearch`
