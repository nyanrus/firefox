# browser/extensions/newtab/lib/HighlightsFeed.sys.mjs

source: browser/extensions/newtab/lib/HighlightsFeed.sys.mjs
source-hash: 5d28d2bf7cc83755a3739c6f112841d15495b65a
lines: 324

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## HighlightsFeed.constructor()
- 位置: L43-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PageThumbs.addExpirationFilter()`
- 参照: `lazy.DownloadsManager`, `lazy.LinksCache`, `lazy.NewTabUtils.activityStreamLinks`, `this._dedupeKey`, `this.dedupe`, `this.downloadsManager`, `this.linksCache`

## HighlightsFeed._dedupeKey()
- 位置: L54-60
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `site.type`, `site.url`

## HighlightsFeed.init()
- 位置: L62-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `lazy.SectionsManager.onceInitialized()`, `this.postInit.bind()`
- XPCOM: `Services.obs`

## HighlightsFeed.postInit()
- 位置: L69-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SectionsManager.enableSection()`, `this.downloadsManager.init()`, `this.fetchHighlights()`
- 参照: `this.store`

## HighlightsFeed.uninit()
- 位置: L75-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.PageThumbs.removeExpirationFilter()`, `lazy.SectionsManager.disableSection()`
- XPCOM: `Services.obs`

## HighlightsFeed.observe()
- 位置: L83-93
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (manyBookmarksChanged)` → `this.fetchHighlights()`

## HighlightsFeed.filterForThumbnailExpiration()
- 位置: L95-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `acc.push()`, `callback()`, `state.rows.reduce()`, `this.store .getState()`, `this.store .getState() .Sections.find()`
- 条件付き依存: `if (site.preview_image_url)` → `acc.push()`
- 参照: `section.id`, `site.preview_image_url`, `site.url`, `state.initialized`

## HighlightsFeed._orderHighlights()
- 位置: L122-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `splitHighlights.chronologicalCandidates .sort()`, `splitHighlights.chronologicalCandidates .sort((a, b) => b.date_added - a.date_added) .concat()`
- 条件付き依存: `if (page.type === "history")` → `splitHighlights.visited.push()`
- 条件付き依存: `if (!(page.type === "history"))` → `splitHighlights.chronologicalCandidates.push()`
- 参照: `a.date_added`, `b.date_added`, `page.type`, `splitHighlights.visited`

## HighlightsFeed.fetchHighlights()
- 位置: async L144-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `highlights.push()`, `hosts.add()`, `hosts.has()`, `lazy.FilterAdult.filter()`, `lazy.NewTabUtils.shortURL()`, `lazy.SectionsManager.updateSection()`, `this._orderHighlights()`, `this.dedupe.group()`, `this.linksCache.request()`, `this.store .getState()`, `this.store .getState() .Sections.find()`, `this.store.getState()`
- 条件付き依存: `if (options.broadcast)` → `this.linksCache.expire()`
- 条件付き依存: `if ( this.store.getState().Prefs.values["section.highlights.includeDownloads"] )` → `this.downloadsManager.getDownloads()`
- 条件付き依存: `if (results.length)` → `manyPages.push()`
- 条件付き依存: `if (!page.image && page.type !== "download")` → `this.fetchImage()`
- 参照: `highlights.length`, `options.broadcast`, `options.isStartup`, `page.__sharedCache`, `page.bookmarkGuid`, `page.image`, `page.type`, `results.length`, `section.id`, `this.store.getState().Prefs.values`, `this.store.getState().Sections.length`, `this.store.getState().TopSites.initialized`, `this.store.getState().TopSites.rows`

## HighlightsFeed.fetchImage()
- 位置: L270-287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Screenshots.maybeCacheScreenshot()`, `lazy.SectionsManager.updateSectionCard()`

## HighlightsFeed.onAction()
- 位置: L289-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.data.name.startsWith()`, `this.downloadsManager.onAction()`, `this.fetchHighlights()`, `this.init()`, `this.linksCache.expire()`, `this.uninit()`
- 条件付き依存: `if (action.data.name.startsWith("section.highlights.include"))` → `this.fetchHighlights()`
- 参照: `action.meta?.isStartup`, `action.type`, `at.DOWNLOAD_CHANGED`, `at.INIT`, `at.PLACES_HISTORY_CLEARED`, `at.PLACES_LINKS_CHANGED`, `at.PLACES_LINK_BLOCKED`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.TOP_SITES_UPDATED`, `at.UNINIT`
