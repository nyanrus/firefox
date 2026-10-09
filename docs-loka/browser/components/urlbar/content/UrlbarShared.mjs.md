# browser/components/urlbar/content/UrlbarShared.mjs

source: browser/components/urlbar/content/UrlbarShared.mjs
source-hash: f135f613f6ae34df77a040e61ecdf7d8261532c5
lines: 1933

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`, `element.documentGlobal.windowUtils.getBoundsWithoutFlushing()`, `element.getBoundingClientRect()`

## isInstance()
- 位置: L117-122
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof ChromeUtils != "undefined")` → `iface.isInstance()`

## LOCAL_SEARCH_MODES()
- 位置: L448-484
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.RESTRICT_TOKENS.ACTION`, `this.RESTRICT_TOKENS.BOOKMARK`, `this.RESTRICT_TOKENS.HISTORY`, `this.RESTRICT_TOKENS.OPENPAGE`, `this.RESULT_SOURCE.ACTIONS`, `this.RESULT_SOURCE.BOOKMARKS`, `this.RESULT_SOURCE.HISTORY`, `this.RESULT_SOURCE.TABS`

## SEARCH_MODE_RESTRICT()
- 位置: L489-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `keys.push()`
- 参照: `this.RESTRICT_TOKENS.ACTION`, `this.RESTRICT_TOKENS.BOOKMARK`, `this.RESTRICT_TOKENS.HISTORY`, `this.RESTRICT_TOKENS.OPENPAGE`, `this.RESTRICT_TOKENS.SEARCH`

## getUserContextIdForOpenPagesTable()
- 位置: L513-515
- 役割: (未記入)
- 触るとき: (未記入)

## normalizedUserContextId()
- 位置: L527-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getUserContextIdForOpenPagesTable()`

## isNonPrivateUserContextId()
- 位置: L542-544
- 役割: (未記入)
- 触るとき: (未記入)

## isContainerUserContextId()
- 位置: L552-554
- 役割: (未記入)
- 触るとき: (未記入)

## getLogger()
- 位置: L571-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loggers.get()`, `loggers.set()`
- 条件付き依存: `if (console.createInstance)` → `createLoggerChrome()`
- 条件付き依存: `if (!(console.createInstance))` → `createLoggerContent()`
- 参照: `console.createInstance`

## getLoadRequestFromResult()
- 位置: L601-626
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.SEARCH`, `element?.dataset.query`, `result.payload.engine`, `result.payload.postData`, `result.payload.query`, `result.payload.suggestion`, `result.payload.url`, `result.type`

## deepEqual()
- 位置: L638-653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.hasOwn()`, `Object.keys()`, `UrlbarShared.deepEqual()`, `aKeys.every()`
- 参照: `aKeys.length`, `bKeys.length`

## looksLikeSingleWordHost()
- 位置: L667-670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.REGEXP_SINGLE_WORD.test()`, `value.trim()`

## isOriginUrl()
- 位置: L682-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `parsed.hash`, `parsed.pathname`, `parsed.search`

## isSearchbarSAP()
- 位置: L704-706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.SEARCHBAR_SAPS.includes()`

## keywordEnabled()
- 位置: L718-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.isSearchbarSAP()`

## navigationEnabled()
- 位置: L731-733
- 役割: (未記入)
- 触るとき: (未記入)

## navigationInSearchModeEnabled()
- 位置: L745-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.isSearchbarSAP()`, `this.navigationEnabled()`

## getIconForUrl()
- 位置: L760-773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.PROTOCOLS_WITH_ICONS.includes()`, `this.isInstance()`
- 条件付き依存: `if (typeof url == "string")` → `this.PROTOCOLS_WITH_ICONS.some()`
- 条件付き依存: `if (typeof url == "string")` → `url.startsWith()`
- 参照: `this.ICON.DEFAULT`, `url.href`, `url.protocol`

## getResultSourceName()
- 位置: L784-794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._resultSourceNamesBySource.get()`
- 条件付き依存: `if (!this._resultSourceNamesBySource)` → `Object.entries()`
- 条件付き依存: `if (!this._resultSourceNamesBySource)` → `this._resultSourceNamesBySource.set()`
- 条件付き依存: `if (!this._resultSourceNamesBySource)` → `sourceName.toLowerCase()`
- 参照: `UrlbarShared.RESULT_SOURCE`, `this._resultSourceNamesBySource`

## stripPrefixAndTrim()
- 位置: L822-853
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `spec.endsWith()`, `spec.startsWith()`
- 条件付き依存: `if (options.stripHttp && spec.startsWith("http://"))` → `spec.slice()`
- 条件付き依存: `if (!(options.stripHttp && spec.startsWith("http://")))` → `spec.startsWith()`
- 条件付き依存: `if (options.stripHttps && spec.startsWith("https://"))` → `spec.slice()`
- 条件付き依存: `if (options.stripWww && spec.startsWith("www."))` → `spec.slice()`
- 条件付き依存: `if (options.trimEmptyHash && spec.endsWith("#"))` → `spec.slice()`
- 条件付き依存: `if (options.trimEmptyQuery && spec.endsWith("?"))` → `spec.slice()`
- 条件付き依存: `if (options.trimSlash && spec.endsWith("/"))` → `spec.slice()`
- 条件付き依存: `if (options.trimTrailingDot && spec.endsWith("."))` → `spec.slice()`
- 参照: `options.stripHttp`, `options.stripHttps`, `options.stripWww`, `options.trimEmptyHash`, `options.trimEmptyQuery`, `options.trimSlash`, `options.trimTrailingDot`

## unEscapeURIForUI()
- 位置: L863-867
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.unEscapeURIForUI()`
- 参照: `this.MAX_TEXT_LENGTH`, `uri.length`

## prepareUrlForDisplay()
- 位置: L880-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getDisplaySpec()`, `this.unEscapeURIForUI()`
- 条件付き依存: `if (schemeless)` → `this.stripPrefixAndTrim()`
- 条件付き依存: `if (!(schemeless))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (trimURL && UrlbarPrefs.get("trimURLs"))` → `displayString.replace()`
- 条件付き依存: `if (trimURL && UrlbarPrefs.get("trimURLs"))` → `displayString.startsWith()`
- 条件付き依存: `if (displayString.startsWith("https://"))` → `displayString.substring()`
- 条件付き依存: `if (displayString.startsWith("https://"))` → `displayString.startsWith()`
- 条件付き依存: `if (displayString.startsWith("www."))` → `displayString.substring()`
- 参照: `url.href`

## canAutofillURL()
- 位置: L925-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `candidate.href.endsWith()`, `candidateString.toLocaleLowerCase()`, `this.REGEXP_PREFIX.test()`, `url.hash.startsWith()`, `urlString .toLocaleLowerCase()`, `urlString .toLocaleLowerCase() .startsWith()`
- 条件付き依存: `if (checkFragmentOnly)` → `url.hash.startsWith()`
- 条件付き依存: `if (!candidate.href.endsWith("/"))` → `url.pathname.indexOf()`
- 参照: `candidate.hash`, `candidate.pathname.length`, `candidateString.length`, `url.hash`, `url.pathname.length`, `urlString.length`

## isPasteEvent()
- 位置: L985-991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.inputType.startsWith()`
- 参照: `event.inputType`

## sanitizeTextFromClipboard()
- 位置: L1006-1031
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `this.stripUnsafeProtocolOnPaste()`
- 条件付き依存: `if (clipboardData.length < 500)` → `clipboardData.replace()`
- 条件付き依存: `if (!(fixupInfo?.keywordAsSent))` → `url.href.match()`
- 条件付き依存: `if ( url?.protocol == "data:" && !url.href.match(/^data:.+;base64,/) )` → `clipboardData.replace()`
- 条件付き依存: `if (!( url?.protocol == "data:" && !url.href.match(/^data:.+;base64,/) ))` → `clipboardData.replace()`
- 参照: `clipboardData.length`, `fixupInfo?.keywordAsSent`, `url?.protocol`

## stripUnsafeProtocolOnPaste()
- 位置: L1040-1045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `pasteData.indexOf()`, `pasteData.substring()`
- 参照: `URL.parse(pasteData)?.protocol`

## getSpanForResult()
- 位置: L1061-1075
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `result.isHiddenExposure`, `result.resultSpan`, `result.type`

## getResultGroup()
- 位置: L1085-1177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (result.heuristic)` → `result.providerName.startsWith()`
- 条件付き依存: `if (result.heuristic)` → `console.error()`
- 参照: `UrlbarShared.PROVIDER_TYPE.EXTENSION`, `UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `UrlbarShared.RESULT_GROUP.AI`, `UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `UrlbarShared.RESULT_GROUP.GENERAL`, `UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `UrlbarShared.RESULT_GROUP.HEURISTIC_AI_CHAT`, `UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `UrlbarShared.RESULT_GROUP.HEURISTIC_BOOKMARK_KEYWORD`, `UrlbarShared.RESULT_GROUP.HEURISTIC_ENGINE_ALIAS`, `UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `UrlbarShared.RESULT_GROUP.HEURISTIC_HISTORY_URL`, `UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `UrlbarShared.RESULT_GROUP.HEURISTIC_RESTRICT_KEYWORD_AUTOFILL`, `UrlbarShared.RESULT_GROUP.HEURISTIC_SEARCH_TIP`, `UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `UrlbarShared.RESULT_GROUP.HEURISTIC_TOKEN_ALIAS_ENGINE`, `UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `UrlbarShared.RESULT_GROUP.OMNIBOX`, `UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `UrlbarShared.RESULT_GROUP.RESTRICT_SEARCH_KEYWORD`, `UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `UrlbarShared.RESULT_GROUP.SUGGESTED_INDEX`, `UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `result.group`, `result.hasSuggestedIndex`, `result.heuristic`, `result.isRichSuggestion`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.suggestion`, `result.payload.tail`, `result.providerName`, `result.providerType`, `result.source`, `result.type`

## searchEngagementTelemetryGroup()
- 位置: L1185-1249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getResultGroup()`
- 参照: `UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `UrlbarShared.RESULT_GROUP.AI`, `UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `UrlbarShared.RESULT_GROUP.GENERAL`, `UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `UrlbarShared.RESULT_GROUP.OMNIBOX`, `UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `UrlbarShared.RESULT_GROUP.RESTRICT_SEARCH_KEYWORD`, `UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `UrlbarShared.RESULT_GROUP.SUGGESTED_INDEX`, `UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `result.heuristic`, `result.isBestMatch`, `result.isRichSuggestion`, `result.payload.trending`, `result.providerName`

## searchEngagementTelemetryAction()
- 位置: L1258-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `result.payload.actionsResults.map()`, `result.payload.actionsResults.map(({ key }) => key).join()`
- 参照: `result.payload.action?.key`, `result.providerName`

## searchEngagementTelemetryType()
- 位置: L1275-1430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkForSubType()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderQuickSuggest")` → `this._getQuickSuggestTelemetryType()`
- 条件付き依存: `if (result.source === UrlbarShared.RESULT_SOURCE.BOOKMARKS)` → `checkForSubType()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`, `UrlbarShared.PROVIDER_TYPE.EXTENSION`, `UrlbarShared.RESTRICT_TOKENS.ACTION`, `UrlbarShared.RESTRICT_TOKENS.BOOKMARK`, `UrlbarShared.RESTRICT_TOKENS.HISTORY`, `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`, `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `UrlbarShared.SEARCH_TIP_TYPE.ONBOARD`, `UrlbarShared.SEARCH_TIP_TYPE.REDIRECT`, `result.autofill`, `result.autofill.type`, `result.heuristic`, `result.isRichSuggestion`, `result.payload.isAutofillFallback`, `result.payload.keyword`, `result.payload.suggestion`, `result.payload.trending`, `result.payload.type`, `result.providerName`, `result.providerType`, `result.source`, `result.type`

## checkForSubType()
- 位置: L1294-1311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ UrlbarShared.RESULT_SOURCE.BOOKMARKS, UrlbarShared.RESULT_SOURCE.HISTORY, UrlbarShared.RESULT_SOURCE.TABS, ].includes()`
- 参照: `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_SOURCE.TABS`, `res.isSERP`, `res.providerName`, `res.source`

## _getQuickSuggestTelemetryType()
- 位置: L1432-1439
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `result.payload.source`, `result.payload.telemetryType`

## getTokenMatches()
- 位置: L1465-1579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hits.fill()`, `hits.indexOf()`, `new Array(str.length).fill()`, `ranges.push()`, `str.indexOf()`, `str.substring()`, `str.substring(0, UrlbarShared.MAX_TEXT_LENGTH).toLocaleLowerCase()`
- 条件付き依存: `if (highlightType == UrlbarShared.HIGHLIGHT.SUGGESTED)` → `str.lastIndexOf()`
- 条件付き依存: `if (!found)` → `str.substr()`
- 条件付き依存: `if (!found)` → `compareIgnoringDiacritics()`
- 条件付き依存: `if (compareIgnoringDiacritics(needle, hay) === 0)` → `hits.fill()`
- 参照: `Intl.Collator`, `UrlbarShared.HIGHLIGHT.ALL`, `UrlbarShared.HIGHLIGHT.SUGGESTED`, `UrlbarShared.MAX_TEXT_LENGTH`, `hits.length`, `needle.length`, `new Intl.Collator("en", { sensitivity: "base", }).compare`, `str.length`, `this._compareIgnoringDiacritics`, `tokens.length`, `tokens?.length`

## addTextContentWithHighlights()
- 位置: L1593-1619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(highlights || []).concat()`
- 条件付き依存: `if (highlightIndex - index > 0)` → `parentNode.appendChild()`
- 条件付き依存: `if (highlightIndex - index > 0)` → `parentNode.ownerDocument.createTextNode()`
- 条件付き依存: `if (highlightIndex - index > 0)` → `textContent.substring()`
- 条件付き依存: `if (highlightLength > 0)` → `parentNode.ownerDocument.createElement()`
- 条件付き依存: `if (highlightLength > 0)` → `textContent.substring()`
- 条件付き依存: `if (highlightLength > 0)` → `parentNode.appendChild()`
- 参照: `parentNode.textContent`, `strong.textContent`, `textContent.length`

## formatDate()
- 位置: L1663-1753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.parseDate()`
- 条件付き依存: `if (!forceAbsoluteDate)` → `Math.abs()`
- 条件付き依存: `if (Math.abs(daysAgo) <= 1)` → `new Intl.RelativeTimeFormat(undefined, { numeric: "auto", }).format()`
- 条件付き依存: `if (0 < daysAgo && daysAgo <= 6)` → `new Intl.RelativeTimeFormat(undefined, { numeric: "always", }).format()`
- 条件付き依存: `if (0 < weeksAgo && (weeksAgo <= 4 || monthsAgo == 0))` → `new Intl.RelativeTimeFormat(undefined, { numeric: "always", }).format()`
- 条件付き依存: `if (0 < monthsAgo && monthsAgo <= 11)` → `new Intl.RelativeTimeFormat(undefined, { numeric: "always", }).format()`
- 条件付き依存: `if (capitalizeRelativeDate && formattedDate)` → `formattedDate[0].toLocaleUpperCase()`
- 条件付き依存: `if (capitalizeRelativeDate && formattedDate)` → `formattedDate.substring()`
- 条件付き依存: `if (!formattedDate)` → `new Intl.DateTimeFormat(undefined, opts).format()`
- 参照: `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, `opts.day`, `opts.month`, `opts.weekday`, `opts.year`, `this.DATE_FORMAT_TYPE.ABSOLUTE`, `this.DATE_FORMAT_TYPE.DAYS_WEEKS_MONTHS_AGO`, `this.DATE_FORMAT_TYPE.YESTERDAY_TODAY_TOMORROW`, `zonedDate.year`, `zonedNow.timeZoneId`, `zonedNow.year`

## parseDate()
- 位置: L1796-1832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Temporal.ZonedDateTime.compare()`, `date.toTemporalInstant()`, `date.toTemporalInstant().toZonedDateTimeISO()`, `dateDay.subtract()`, `dateDay.with()`, `this._firstDayOfWeek()`, `this._zonedDateTimeISO()`, `thisMonth.since()`, `thisMonth.since(dateMonth).round()`, `thisWeek.since()`, `thisWeek.since(dateWeek).round()`, `today.since()`, `today.since(dateDay).round()`, `today.subtract()`, `today.with()`, `zonedDate.startOfDay()`, `zonedNow.startOfDay()`
- 参照: `dateDay.dayOfWeek`, `thisMonth.since(dateMonth).round({ smallestUnit: "months", relativeTo: thisMonth, }).months`, `thisWeek.since(dateWeek).round({ smallestUnit: "weeks", relativeTo: thisWeek, }).weeks`, `today.dayOfWeek`, `today.since(dateDay).round("days").days`

## _zonedDateTimeISO()
- 位置: L1836-1838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Temporal.Now.zonedDateTimeISO()`

## _firstDayOfWeek()
- 位置: L1842-1856
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.__firstDayOfWeek === undefined)` → `new Intl.Locale( Intl.DateTimeFormat().resolvedOptions().locale ).getWeekInfo()`
- 条件付き依存: `if (this.__firstDayOfWeek === undefined)` → `Intl.DateTimeFormat().resolvedOptions()`
- 条件付き依存: `if (this.__firstDayOfWeek === undefined)` → `Intl.DateTimeFormat()`
- 参照: `Intl.DateTimeFormat().resolvedOptions().locale`, `Intl.Locale`, `new Intl.Locale( Intl.DateTimeFormat().resolvedOptions().locale ).getWeekInfo().firstDay`, `this.__firstDayOfWeek`

## escapeHtmlEntities()
- 位置: L1864-1871
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(s || "") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace(/"/g, "&quot;") .replace()`

## createLoggerChrome()
- 位置: L1881-1886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.createInstance()`

## createLoggerContent()
- 位置: L1895-1929
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `maxLogLevelPref.replace()`

## shouldLog()
- 位置: L1912-1917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarPrefs.get(levelPref).toLowerCase()`
- 参照: `LEVEL_NUMBERS.warn`

## get()
- 位置: L1920-1927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LEVELS.includes()`, `value.bind()`
- 条件付き依存: `if (typeof prop == "string" && LEVELS.includes(prop))` → `shouldLog()`
- 条件付き依存: `if (typeof prop == "string" && LEVELS.includes(prop))` → `target[prop]()`
