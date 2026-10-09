# browser/components/extensions/parent/ext-topSites.js

source: browser/components/extensions/parent/ext-topSites.js
source-hash: 96d15c717efb85fa5a019ef30a4205d5993e8c44
lines: 118

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getAPI()
- 位置: L20-116
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: async L23-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutNewTab.getTopSites()`, `NewTabUtils.activityStreamLinks.getTopSites()`, `Promise.all()`, `Services.prefs.getBoolPref()`, `links.map()`, `makeDataURI()`
- 条件付き依存: `if (options.includeFavicon)` → `NewTabUtils.activityStreamProvider._faviconBytesToDataURI()`
- 条件付き依存: `if (options.includeFavicon)` → `NewTabUtils.activityStreamProvider._addFavicons()`
- 条件付き依存: `if (options.includePinned && !getNewtabSites)` → `pinnedLinks.forEach()`
- 条件付き依存: `if ( pinnedLink && (!pinnedLink.searchTopSite || options.includeSearchShortcuts) )` → `links.filter()`
- 条件付き依存: `if ( pinnedLink && (!pinnedLink.searchTopSite || options.includeSearchShortcuts) )` → `NewTabUtils.extractSite()`
- 条件付き依存: `if ( pinnedLink && (!pinnedLink.searchTopSite || options.includeSearchShortcuts) )` → `links.splice()`
- 条件付き依存: `if ( options.includeSearchShortcuts && Services.prefs.getBoolPref(SHORTCUTS_PREF, false) && !getNewtabSites )` → `links.map()`
- 条件付き依存: `if ( options.includeSearchShortcuts && Services.prefs.getBoolPref(SHORTCUTS_PREF, false) && !getNewtabSites )` → `getSearchProvider()`
- 条件付き依存: `if ( options.includeSearchShortcuts && Services.prefs.getBoolPref(SHORTCUTS_PREF, false) && !getNewtabSites )` → `NewTabUtils.shortURL()`
- 条件付き依存: `if (typeof options.limit == "number")` → `links.slice()`
- 参照: `NewTabUtils.pinnedLinks.links`, `link.favicon`, `link.hostname`, `link.label`, `link.searchTopSite`, `link.tippyTopIcon`, `link.title`, `link.url`, `options.includeBlocked`, `options.includeFavicon`, `options.includePinned`, `options.includeSearchShortcuts`, `options.limit`, `options.newtab`, `options.onePerDomain`, `pinnedLink.baseDomain`, `pinnedLink.searchTopSite`, `pinnedLink.url`, `searchProvider.keyword`, `searchProvider.url`
- XPCOM: `Services.prefs`

## makeDataURI()
- 位置: L93-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionUtils.makeDataURI()`
