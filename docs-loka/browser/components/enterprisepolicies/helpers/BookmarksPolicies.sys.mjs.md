# browser/components/enterprisepolicies/helpers/BookmarksPolicies.sys.mjs

source: browser/components/enterprisepolicies/helpers/BookmarksPolicies.sys.mjs
source-hash: 3400c7cde4208273a77db217de47896ec27f7685
lines: 302

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `foldersMap.set()`, `lazy.PlacesUtils.bookmarks .fetch()`, `resolve()`

## reportFailure()
- 位置: L68-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PolicyFailures.report()`, `lazy.log.error()`

## processBookmarks()
- 位置: L86-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `calculateLists()`, `calculateLists(param).then()`

## addRemoveBookmarks()
- 位置: async L90-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `insertBookmark()`, `insertBookmark(bookmark).catch()`, `lazy.PlacesUtils.bookmarks .remove()`, `lazy.PlacesUtils.bookmarks .remove(bookmark) .catch()`, `lazy.gFoldersMapPromise.then()`, `map.clear()`, `reportFailure()`, `results.add.values()`, `results.emptyFolders.values()`, `results.remove.values()`
- 参照: `bookmark.Title`

## calculateLists()
- 位置: async L123-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `existingBookmarksMap.has()`, `existingBookmarksMap.keys()`, `existingBookmarksMap.set()`, `foldersSeen.add()`, `lazy.PlacesUtils.bookmarks.fetch()`, `lazy.log.debug()`, `specifiedBookmarksMap.keys()`, `specifiedBookmarksMap.set()`
- 条件付き依存: `if (existingBookmarksMap.has(url))` → `lazy.log.debug()`
- 条件付き依存: `if (existingBookmarksMap.has(url))` → `specifiedBookmarksMap.delete()`
- 条件付き依存: `if (existingBookmarksMap.has(url))` → `existingBookmarksMap.delete()`
- 条件付き依存: `if (existingBookmarksMap.size > 0)` → `lazy.PlacesUtils.bookmarks.fetch()`
- 条件付き依存: `if (existingBookmarksMap.size > 0)` → `foldersSeen.has()`
- 条件付き依存: `if (!foldersSeen.has(folder.title))` → `lazy.log.debug()`
- 条件付き依存: `if (!foldersSeen.has(folder.title))` → `foldersToRemove.add()`
- 参照: `BookmarksPolicies.BOOKMARK_GUID_PREFIX`, `BookmarksPolicies.FOLDER_GUID_PREFIX`, `bookmark.URL.href`, `bookmark.url.href`, `existingBookmarksMap.size`, `folder.title`, `item.Folder`

## insertBookmark()
- 位置: async L211-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getParentGuid()`, `lazy.PlacesUtils.bookmarks.insert()`, `lazy.PlacesUtils.generateGuidWithPrefix()`
- 条件付き依存: `if (bookmark.Favicon)` → `setFaviconForBookmark()`
- 参照: `BookmarksPolicies.BOOKMARK_GUID_PREFIX`, `bookmark.Favicon`, `bookmark.Folder`, `bookmark.Placement`, `bookmark.Title`, `bookmark.URL.URI`

## setFaviconForBookmark()
- 位置: L228-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons .setFaviconForPage()`, `reportFailure()`
- 条件付き依存: `if (bookmark.Favicon.protocol != "data:")` → `reportFailure()`
- 参照: `bookmark.Favicon.URI`, `bookmark.Favicon.URI.spec`, `bookmark.Favicon.protocol`, `bookmark.Title`, `bookmark.URL.URI`, `bookmark.URL.href`
- XPCOM: `Services.io`

## getParentGuid()
- 位置: async L269-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `foldersMap.has()`, `foldersMap.set()`, `lazy.PlacesUtils.bookmarks.insert()`, `lazy.PlacesUtils.generateGuidWithPrefix()`
- 条件付き依存: `if (foldersMap.has(folderName))` → `foldersMap.get()`
- 参照: `BookmarksPolicies.FOLDER_GUID_PREFIX`, `lazy.PlacesUtils.bookmarks.TYPE_FOLDER`, `lazy.PlacesUtils.bookmarks.menuGuid`, `lazy.PlacesUtils.bookmarks.toolbarGuid`, `lazy.gFoldersMapPromise`
