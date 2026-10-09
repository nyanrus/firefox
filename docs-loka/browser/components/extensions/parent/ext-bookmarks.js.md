# browser/components/extensions/parent/ext-bookmarks.js

source: browser/components/extensions/parent/ext-bookmarks.js
source-hash: 114d79fcedc212983dec812f507bfbfb8f6f35d7
lines: 512

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `theMap.set()`

## getUrl()
- 位置: L34-43
- 役割: (未記入)
- 触るとき: (未記入)

## getTree()
- 位置: L45-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.promiseBookmarksTree()`, `PlacesUtils.promiseBookmarksTree(rootGuid) .then()`, `Promise.reject()`, `convert()`
- 条件付き依存: `if (onlyChildren)` → `children.map()`
- 条件付き依存: `if (onlyChildren)` → `convert()`
- 参照: `e.message`, `root.children`, `root.parentGuid`, `treenode.parentId`

## convert()
- 位置: L46-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BOOKMARKS_TYPES_TO_API_TYPES_MAP.get()`, `PlacesUtils.bookmarks.getLocalizedTitle()`, `getUrl()`
- 条件付き依存: `if (!onlyChildren)` → `node.children.map()`
- 条件付き依存: `if (!onlyChildren)` → `convert()`
- 参照: `PlacesUtils.bookmarks.rootGuid`, `node.children`, `node.dateAdded`, `node.guid`, `node.index`, `node.lastModified`, `node.typeCode`, `node.uri`, `parent.guid`, `treenode.children`, `treenode.dateGroupModified`, `treenode.parentId`

## convertBookmarks()
- 位置: L87-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BOOKMARKS_TYPES_TO_API_TYPES_MAP.get()`, `PlacesUtils.bookmarks.getLocalizedTitle()`, `getUrl()`, `result.dateAdded.getTime()`
- 条件付き依存: `if (result.type == TYPE_FOLDER)` → `result.lastModified.getTime()`
- 参照: `PlacesUtils.bookmarks.rootGuid`, `node.dateGroupModified`, `node.parentId`, `result.guid`, `result.index`, `result.parentGuid`, `result.type`, `result.url`, `result.url.href`

## throwIfRootId()
- 位置: L108-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PlacesUtils.bookmarks.rootGuid`

## constructor()
- 位置: L115-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.handlePlacesEvents.bind()`
- 参照: `this.handlePlacesEvents`

## handlePlacesEvents()
- 位置: L120-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BOOKMARKS_TYPES_TO_API_TYPES_MAP.get()`, `getUrl()`, `this.emit()`
- 参照: `bookmark.dateAdded`, `bookmark.dateGroupModified`, `event.dateAdded`, `event.guid`, `event.index`, `event.isDescendantRemoval`, `event.isTagging`, `event.itemType`, `event.oldIndex`, `event.oldParentGuid`, `event.parentGuid`, `event.title`, `event.type`, `event.url`

## decrementListeners()
- 位置: L199-213
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!listenerCount)` → `PlacesUtils.observers.removeListener()`
- 参照: `observer.handlePlacesEvents`

## incrementListeners()
- 位置: L215-229
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (listenerCount == 1)` → `PlacesUtils.observers.addListener()`
- 参照: `observer.handlePlacesEvents`

## onCreated()
- 位置: L233-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L234-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 参照: `bookmark.id`

## unregister()
- 位置: L241-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L245-247
- 役割: (未記入)
- 触るとき: (未記入)

## onRemoved()
- 位置: L251-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L252-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 参照: `data.guid`, `data.info`

## unregister()
- 位置: L259-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L263-265
- 役割: (未記入)
- 触るとき: (未記入)

## onChanged()
- 位置: L269-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L270-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 参照: `data.guid`, `data.info`

## unregister()
- 位置: L277-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L281-283
- 役割: (未記入)
- 触るとき: (未記入)

## onMoved()
- 位置: L287-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L288-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`
- 参照: `data.guid`, `data.info`

## unregister()
- 位置: L295-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L306-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new EventManager({ context, module: "bookmarks", event: "onChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "bookmarks", event: "onCreated", extensionApi: this, }).api()`, `new EventManager({ context, module: "bookmarks", event: "onMoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "bookmarks", event: "onRemoved", extensionApi: this, }).api()`

## get()
- 位置: async L309-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `PlacesUtils.bookmarks.fetch()`, `Promise.reject()`, `bookmarks.push()`, `convertBookmarks()`
- 参照: `error.message`

## getChildren()
- 位置: L327-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTree()`

## getTree()
- 位置: L332-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTree()`
- 参照: `PlacesUtils.bookmarks.rootGuid`

## getSubTree()
- 位置: L336-338
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTree()`

## search()
- 位置: L340-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.bookmarks .search()`, `PlacesUtils.bookmarks .search(query) .then()`, `result.map()`

## getRecent()
- 位置: L346-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PlacesUtils.bookmarks .getRecent()`, `PlacesUtils.bookmarks .getRecent(numberOfItems) .then()`, `result.map()`

## create()
- 位置: L352-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `API_TYPES_TO_BOOKMARKS_TYPES_MAP.get()`, `JSON.stringify()`, `PlacesUtils.bookmarks .insert()`, `PlacesUtils.bookmarks .insert(info) .then()`, `PlacesUtils.bookmarks .insert(info) .then(convertBookmarks) .catch()`, `Promise.reject()`
- 条件付き依存: `if (bookmark.parentId !== null)` → `throwIfRootId()`
- 参照: `PlacesUtils.bookmarks.unfiledGuid`, `bookmark.index`, `bookmark.parentId`, `bookmark.title`, `bookmark.type`, `bookmark.url`, `error.message`, `info.index`, `info.parentGuid`, `info.type`, `info.url`

## move()
- 位置: L394-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .update()`, `PlacesUtils.bookmarks .update(info) .then()`, `PlacesUtils.bookmarks .update(info) .then(convertBookmarks) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 条件付き依存: `if (destination.parentId !== null)` → `throwIfRootId()`
- 参照: `PlacesUtils.bookmarks.DEFAULT_INDEX`, `destination.index`, `destination.parentId`, `error.message`, `info.index`, `info.parentGuid`

## update()
- 位置: L421-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .update()`, `PlacesUtils.bookmarks .update(info) .then()`, `PlacesUtils.bookmarks .update(info) .then(convertBookmarks) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 参照: `changes.title`, `changes.url`, `error.message`, `info.title`, `info.url`

## remove()
- 位置: L446-462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .remove()`, `PlacesUtils.bookmarks .remove(info, { preventRemovalOfNonEmptyFolders: true }) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 参照: `error.message`

## removeTree()
- 位置: L464-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .remove()`, `PlacesUtils.bookmarks .remove(info) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 参照: `error.message`
