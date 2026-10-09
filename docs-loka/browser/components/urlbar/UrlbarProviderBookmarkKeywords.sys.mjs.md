# browser/components/urlbar/UrlbarProviderBookmarkKeywords.sys.mjs

source: browser/components/urlbar/UrlbarProviderBookmarkKeywords.sys.mjs
source-hash: 60d60c4b35dc95140ae2faba093a4a3fd2ce187c
lines: 114

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderBookmarkKeywords.type()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderBookmarkKeywords.isActive()
- 位置: async L41-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.restrictInSearchMode()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `queryContext.restrictSource`, `queryContext.tokens.length`

## UrlbarProviderBookmarkKeywords.startQuery()
- 位置: async L58-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarUtils.substringAfter()`, `UrlbarUtils.substringAfter( queryContext.searchString, keyword ).trim()`, `addCallback()`, `bookmark.dateAdded.getTime()`, `lazy.KeywordUtils.getBindableKeyword()`, `lazy.PlacesUtils.bookmarks.fetch()`, `lazy.UrlbarShared.getIconForUrl()`
- 条件付き依存: `if (entry.url.host && searchString)` → `UrlbarUtils.strings.formatStringFromName()`
- 条件付き依存: `if (entry.url.host && searchString)` → `queryContext.tokens .slice(1) .map(t => t.value) .join()`
- 条件付き依存: `if (entry.url.host && searchString)` → `queryContext.tokens .slice(1) .map()`
- 条件付き依存: `if (entry.url.host && searchString)` → `queryContext.tokens .slice()`
- 条件付き依存: `if (!(entry.url.host && searchString))` → `lazy.UrlbarShared.prepareUrlForDisplay()`
- 参照: `entry.url`, `entry.url.host`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_TYPE.KEYWORD`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0]?.value`, `t.value`
