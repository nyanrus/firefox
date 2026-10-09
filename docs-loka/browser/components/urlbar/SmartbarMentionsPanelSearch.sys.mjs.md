# browser/components/urlbar/SmartbarMentionsPanelSearch.sys.mjs

source: browser/components/urlbar/SmartbarMentionsPanelSearch.sys.mjs
source-hash: b8b9a1deb627502a16735575815e88d565cd56bf
lines: 218

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isExcludedMentionUrl()
- 位置: L37-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ADDITIONAL_EXCLUDED_MENTION_URLS.has()`, `Services.io.newURI()`, `browserWindow.isInitialPage()`
- XPCOM: `Services.io`

## SmartbarMentionsPanelSearch.constructor()
- 位置: L78-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getOpenAndClosedTabs()`
- 参照: `this.#browserWindow`, `this.#tabs`

## SmartbarMentionsPanelSearch.startQuery()
- 位置: L89-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#filterTabs()`, `this.#filterTabs(searchString).sort()`
- 参照: `a.timestamp`, `b.timestamp`

## SmartbarMentionsPanelSearch.getTabGroups()
- 位置: L102-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.tabManagementService.getTabGroups()`
- 参照: `this.#browserWindow`

## SmartbarMentionsPanelSearch.#filterTabs()
- 位置: L108-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: ``${tab.title} ${normalizedUrl}` .substring()`, ``${tab.title} ${normalizedUrl}` .substring(0, lazy.UrlbarShared.MAX_TEXT_LENGTH) .toLowerCase()`, `lazy.UrlbarTokenizer.tokenize()`, `searchString.substring()`, `searchText.includes()`, `this.#normalizeUrl()`, `this.#tabs.filter()`, `token.value.toLowerCase()`, `tokens.every()`, `truncatedSearch.trim()`
- 参照: `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `tab.title`, `tab.url`, `this.#tabs`, `tokens.length`

## SmartbarMentionsPanelSearch.#getOpenAndClosedTabs()
- 位置: L143-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `isExcludedMentionUrl()`, `lazy.SessionStore.getClosedTabDataForWindow()`, `lazy.UrlbarShared.getIconForUrl()`, `results.push()`, `tab.image.startsWith()`
- 参照: `MENTION_TYPE.TAB_OPEN`, `MENTION_TYPE.TAB_RECENTLY_CLOSED`, `browserWindow.gBrowser.tabs`, `closedTab.closedAt`, `closedTab.state`, `entry.title`, `entry.url`, `state.entries`, `state.entries.length`, `state.index`, `tab.image`, `tab.label`, `tab.lastAccessed`, `tab.linkedBrowser?.currentURI?.spec`

## SmartbarMentionsPanelSearch.#normalizeUrl()
- 位置: L203-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`
