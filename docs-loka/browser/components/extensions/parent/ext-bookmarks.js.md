# browser/components/extensions/parent/ext-bookmarks.js

source: browser/components/extensions/parent/ext-bookmarks.js
source-hash: 114d79fcedc212983dec812f507bfbfb8f6f35d7
lines: 512

## <module>
- 役割: bookmarks API の親プロセス側実装。Places の内部形式を拡張向けの形式へ変換し、ブックマークの取得・作成・移動・更新・削除と変更イベントを提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `theMap.set()`

## getUrl()
- 位置: L34-43
- 役割: ブックマーク種別に応じて url を返す。ブックマークはそのまま、区切りは data: の固定値、フォルダーは undefined を返す。
- 触るとき: 区切り線やフォルダーの url 表示が拡張側で違って見える問題を調べるとき。

## getTree()
- 位置: L45-85
- 役割: PlacesUtils.promiseBookmarksTree で木構造を取り、onlyChildren なら直下の子だけを、そうでなければ根を変換して 1 要素の配列で返す。
- 触るとき: getTree、getChildren、getSubTree の返す階層や parentId の付き方を変えるとき。
- 呼び出し先: `PlacesUtils.promiseBookmarksTree()`, `PlacesUtils.promiseBookmarksTree(rootGuid) .then()`, `Promise.reject()`, `convert()`
- 条件付き依存: `if (onlyChildren)` → `children.map()`
- 条件付き依存: `if (onlyChildren)` → `convert()`
- 参照: `e.message`, `root.children`, `root.parentGuid`, `treenode.parentId`

## convert()
- 位置: L46-71
- 役割: Places のノードを拡張の BookmarkTreeNode 形式へ変換し、フォルダーなら dateGroupModified と子ノードを再帰的に付ける。
- 触るとき: ツリーの各ノードに出すフィールドや子ノードの扱いを変えるとき。
- 呼び出し先: `BOOKMARKS_TYPES_TO_API_TYPES_MAP.get()`, `PlacesUtils.bookmarks.getLocalizedTitle()`, `getUrl()`
- 条件付き依存: `if (!onlyChildren)` → `node.children.map()`
- 条件付き依存: `if (!onlyChildren)` → `convert()`
- 参照: `PlacesUtils.bookmarks.rootGuid`, `node.children`, `node.dateAdded`, `node.guid`, `node.index`, `node.lastModified`, `node.typeCode`, `node.uri`, `parent.guid`, `treenode.children`, `treenode.dateGroupModified`, `treenode.parentId`

## convertBookmarks()
- 位置: L87-106
- 役割: Places の検索結果や取得結果 1 件を拡張の BookmarkTreeNode 形式へ変換する。根ノードには parentId を付けない。
- 触るとき: get、search、create などの戻り値の形式を揃えたいとき。
- 呼び出し先: `BOOKMARKS_TYPES_TO_API_TYPES_MAP.get()`, `PlacesUtils.bookmarks.getLocalizedTitle()`, `getUrl()`, `result.dateAdded.getTime()`
- 条件付き依存: `if (result.type == TYPE_FOLDER)` → `result.lastModified.getTime()`
- 参照: `PlacesUtils.bookmarks.rootGuid`, `node.dateGroupModified`, `node.parentId`, `result.guid`, `result.index`, `result.parentGuid`, `result.type`, `result.url`, `result.url.href`

## throwIfRootId()
- 位置: L108-112
- 役割: 指定 ID がブックマークの根なら、根は変更できないという ExtensionError を投げる。
- 触るとき: 根ノードに対する操作を新たに許可・禁止する判断を変えるとき。
- 参照: `PlacesUtils.bookmarks.rootGuid`

## constructor()
- 位置: L115-118
- 役割: EventEmitter を初期化し、handlePlacesEvents を this に束縛する。
- 触るとき: Places イベントの配送先を別の仕組みに替えるとき。
- 呼び出し先: `super()`, `this.handlePlacesEvents.bind()`
- 参照: `this.handlePlacesEvents`

## handlePlacesEvents()
- 位置: L120-196
- 役割: Places の bookmark-added、removed、moved、title-changed、url-changed を拡張向けの created、removed、moved、changed に変換して emit する。タグ付けや子孫の一括削除は無視する。
- 触るとき: 拡張の onCreated などに届く情報が欠ける、または多すぎる問題を調べるとき。
- 呼び出し先: `BOOKMARKS_TYPES_TO_API_TYPES_MAP.get()`, `getUrl()`, `this.emit()`
- 参照: `bookmark.dateAdded`, `bookmark.dateGroupModified`, `event.dateAdded`, `event.guid`, `event.index`, `event.isDescendantRemoval`, `event.isTagging`, `event.itemType`, `event.oldIndex`, `event.oldParentGuid`, `event.parentGuid`, `event.title`, `event.type`, `event.url`

## decrementListeners()
- 位置: L199-213
- 役割: リスナー数を 1 減らし、0 になったら Places の監視を外す。
- 触るとき: イベントリスナーを外したのに Places の監視が残る、または早く外れる問題を調べるとき。
- 条件付き依存: `if (!listenerCount)` → `PlacesUtils.observers.removeListener()`
- 参照: `observer.handlePlacesEvents`

## incrementListeners()
- 位置: L215-229
- 役割: リスナー数を 1 増やし、初めて 1 になったときだけ Places の監視を登録する。
- 触るとき: 複数のイベントが同じ監視を共有する仕組みを変えるとき。
- 条件付き依存: `if (listenerCount == 1)` → `PlacesUtils.observers.addListener()`
- 参照: `observer.handlePlacesEvents`

## onCreated()
- 位置: L233-249
- 役割: created を監視するリスナーを登録してリスナー数を増やし、解除時に外して数を減らす。fire は convert で差し替えられる。
- 触るとき: onCreated の登録と解除が正しく対になっているかを確かめるとき。
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L234-236
- 役割: created の内容を id と共に fire.sync で拡張へ送る。
- 触るとき: onCreated の引数が拡張に届く形を変えるとき。
- 呼び出し先: `fire.sync()`
- 参照: `bookmark.id`

## unregister()
- 位置: L241-244
- 役割: created のリスナーを外し、リスナー数を減らす。
- 触るとき: onCreated を購読解除した後も監視が続く問題を調べるとき。
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L245-247
- 役割: 永続イベントの復元時に、新しい fire を受け取って差し替える。
- 触るとき: バックグラウンドの再起動後にイベントが届かない問題を調べるとき。

## onRemoved()
- 位置: L251-267
- 役割: removed を監視するリスナーを登録し、解除時に外して数を減らす。
- 触るとき: onRemoved の登録と解除の対応を調べるとき。
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L252-254
- 役割: removed の guid と info を fire.sync で拡張へ送る。
- 触るとき: onRemoved の引数の中身を変えるとき。
- 呼び出し先: `fire.sync()`
- 参照: `data.guid`, `data.info`

## unregister()
- 位置: L259-262
- 役割: removed のリスナーを外し、リスナー数を減らす。
- 触るとき: onRemoved の購読解除が効かない問題を調べるとき。
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L263-265
- 役割: 永続イベントの復元時に、新しい fire を受け取って差し替える。
- 触るとき: onRemoved が再起動後に届かない問題を調べるとき。

## onChanged()
- 位置: L269-285
- 役割: changed を監視するリスナーを登録し、解除時に外して数を減らす。
- 触るとき: onChanged の登録と解除の対応を調べるとき。
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L270-272
- 役割: changed の guid と info を fire.sync で拡張へ送る。
- 触るとき: onChanged の引数の中身を変えるとき。
- 呼び出し先: `fire.sync()`
- 参照: `data.guid`, `data.info`

## unregister()
- 位置: L277-280
- 役割: changed のリスナーを外し、リスナー数を減らす。
- 触るとき: onChanged の購読解除が効かない問題を調べるとき。
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L281-283
- 役割: 永続イベントの復元時に、新しい fire を受け取って差し替える。
- 触るとき: onChanged が再起動後に届かない問題を調べるとき。

## onMoved()
- 位置: L287-303
- 役割: moved を監視するリスナーを登録し、解除時に外して数を減らす。
- 触るとき: onMoved の登録と解除の対応を調べるとき。
- 呼び出し先: `incrementListeners()`, `observer.on()`

## listener()
- 位置: L288-290
- 役割: moved の guid と info を fire.sync で拡張へ送る。
- 触るとき: onMoved の引数の中身を変えるとき。
- 呼び出し先: `fire.sync()`
- 参照: `data.guid`, `data.info`

## unregister()
- 位置: L295-298
- 役割: moved のリスナーを外し、リスナー数を減らす。
- 触るとき: onMoved の購読解除が効かない問題を調べるとき。
- 呼び出し先: `decrementListeners()`, `observer.off()`

## convert()
- 位置: L299-301
- 役割: 永続イベントの復元時に、新しい fire を受け取って差し替える。
- 触るとき: onMoved が再起動後に届かない問題を調べるとき。

## getAPI()
- 位置: L306-510
- 役割: bookmarks 名前空間の関数と 4 つのイベントを持つ API オブジェクトを返す。
- 触るとき: bookmarks API に関数やイベントを追加・削除するとき。
- 呼び出し先: `new EventManager({ context, module: "bookmarks", event: "onChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "bookmarks", event: "onCreated", extensionApi: this, }).api()`, `new EventManager({ context, module: "bookmarks", event: "onMoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "bookmarks", event: "onRemoved", extensionApi: this, }).api()`

## get()
- 位置: async L309-325
- 役割: ID 1 つまたは配列を受け取り、各 GUID を Places から取り出して変換する。1 件でも見つからなければ Bookmark not found で拒否する。
- 触るとき: bookmarks.get が存在しない ID で失敗する条件を変えるとき。
- 呼び出し先: `Array.isArray()`, `PlacesUtils.bookmarks.fetch()`, `Promise.reject()`, `bookmarks.push()`, `convertBookmarks()`
- 参照: `error.message`

## getChildren()
- 位置: L327-330
- 役割: 指定 ID の直下の子だけを getTree に渡して取得する。
- 触るとき: getChildren の戻り値の階層を調べるとき。
- 呼び出し先: `getTree()`

## getTree()
- 位置: L332-334
- 役割: 根 GUID を起点に、子孫を含むブックマーク木を取得する。
- 触るとき: 拡張に返す全体ツリーの範囲を変えるとき。
- 呼び出し先: `getTree()`
- 参照: `PlacesUtils.bookmarks.rootGuid`

## getSubTree()
- 位置: L336-338
- 役割: 指定 ID を根として、子孫を含む木を取得する。
- 触るとき: getSubTree の範囲や性能を調べるとき。
- 呼び出し先: `getTree()`

## search()
- 位置: L340-344
- 役割: Places の検索に query を渡し、結果を拡張の形式へ変換する。
- 触るとき: bookmarks.search の検索条件の扱いを変えるとき。
- 呼び出し先: `PlacesUtils.bookmarks .search()`, `PlacesUtils.bookmarks .search(query) .then()`, `result.map()`

## getRecent()
- 位置: L346-350
- 役割: Places から直近のブックマークを指定件数取り出し、拡張の形式へ変換する。
- 触るとき: getRecent の件数や並び順の問題を調べるとき。
- 呼び出し先: `PlacesUtils.bookmarks .getRecent()`, `PlacesUtils.bookmarks .getRecent(numberOfItems) .then()`, `result.map()`

## create()
- 位置: L352-392
- 役割: type を Places の種別へ対応づけ、未指定なら url の有無でブックマークかフォルダーかを決める。parentId は根を禁止し、未指定なら未分類フォルダーへ入れて insert する。
- 触るとき: create で種別や親の既定値の決め方を変えるとき。
- 呼び出し先: `API_TYPES_TO_BOOKMARKS_TYPES_MAP.get()`, `JSON.stringify()`, `PlacesUtils.bookmarks .insert()`, `PlacesUtils.bookmarks .insert(info) .then()`, `PlacesUtils.bookmarks .insert(info) .then(convertBookmarks) .catch()`, `Promise.reject()`
- 条件付き依存: `if (bookmark.parentId !== null)` → `throwIfRootId()`
- 参照: `PlacesUtils.bookmarks.unfiledGuid`, `bookmark.index`, `bookmark.parentId`, `bookmark.title`, `bookmark.type`, `bookmark.url`, `error.message`, `info.index`, `info.parentGuid`, `info.type`, `info.url`

## move()
- 位置: L394-419
- 役割: 根の移動を禁止し、parentId と index を整えて PlacesUtils.bookmarks.update で移動する。
- 触るとき: move の移動先指定や既定の index の扱いを変えるとき。
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .update()`, `PlacesUtils.bookmarks .update(info) .then()`, `PlacesUtils.bookmarks .update(info) .then(convertBookmarks) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 条件付き依存: `if (destination.parentId !== null)` → `throwIfRootId()`
- 参照: `PlacesUtils.bookmarks.DEFAULT_INDEX`, `destination.index`, `destination.parentId`, `error.message`, `info.index`, `info.parentGuid`

## update()
- 位置: L421-444
- 役割: 根の更新を禁止し、title と url のうち null でないものだけを Places の update に渡す。
- 触るとき: update で値を消す指定(null)の扱いを変えるとき。
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .update()`, `PlacesUtils.bookmarks .update(info) .then()`, `PlacesUtils.bookmarks .update(info) .then(convertBookmarks) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 参照: `changes.title`, `changes.url`, `error.message`, `info.title`, `info.url`

## remove()
- 位置: L446-462
- 役割: 根の削除を禁止し、空でないフォルダーの削除を防ぐ指定付きで Places の remove を呼ぶ。
- 触るとき: remove が非空フォルダーで失敗する条件を調べるとき。
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .remove()`, `PlacesUtils.bookmarks .remove(info, { preventRemovalOfNonEmptyFolders: true }) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 参照: `error.message`

## removeTree()
- 位置: L464-479
- 役割: 根の削除を禁止し、子孫ごと Places の remove を呼ぶ。
- 触るとき: removeTree の削除範囲を変えるとき。
- 呼び出し先: `JSON.stringify()`, `PlacesUtils.bookmarks .remove()`, `PlacesUtils.bookmarks .remove(info) .catch()`, `Promise.reject()`, `throwIfRootId()`
- 参照: `error.message`
