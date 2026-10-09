# browser/components/extensions/parent/ext-tabs.js

source: browser/components/extensions/parent/ext-tabs.js
source-hash: cb2c4b387df5620b770d418506dfe55cb2feeeb4
lines: 1849

## <module>
- 役割: 拡張機能の tabs API を実装する親側モジュール。タブのイベント、作成、移動、更新、キャプチャ、グループ化、非表示などを扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`, `this.tabEventRegistrar()`

## getLocalizedDescription()
- 位置: L38-50
- 役割: タブ非表示の拡張通知に使う説明文を作る。全タブボタンのアイコンを、タブストリップ上にあれば通常の、無ければ汎用の見た目で付ける。
- 触るとき: タブ非表示の通知の見た目や文言を変えるとき。
- 呼び出し先: `BrowserUIUtils.getLocalizedFragment()`, `doc.createXULElement()`, `doc.getElementById()`, `doc.getElementById("alltabs-button")?.closest()`, `image.classList.add()`
- 条件付き依存: `if (!doc.getElementById("alltabs-button")?.closest("#TabsToolbar"))` → `image.classList.add()`

## showHiddenTabs()
- 位置: L55-71
- 役割: 開いている全ブラウザーウィンドウを見て、その拡張が隠したタブ(hiddenBy の値が一致するもの)を表示に戻す。
- 触るとき: 拡張の無効化や更新で隠されたままのタブが残る問題を調べるとき。
- 呼び出し先: `Services.wm.getEnumerator()`, `SessionStore.getCustomTabValue()`
- 条件付き依存: `if ( tab.hidden && tab.documentGlobal && SessionStore.getCustomTabValue(tab, "hiddenBy") === id )` → `win.gBrowser.showTab()`
- 参照: `tab.documentGlobal`, `tab.hidden`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`
- XPCOM: `Services.wm`

## onUpdate()
- 位置: L103-107
- 役割: 新しいマニフェストに tabHide 権限が無ければ、その拡張が隠したタブを表示に戻す。
- 触るとき: アップデートで tabHide 権限を外した拡張のタブが隠れたままになる問題を調べるとき。
- 呼び出し先: `manifest.permissions.includes()`
- 条件付き依存: `if (!manifest.permissions || !manifest.permissions.includes("tabHide"))` → `showHiddenTabs()`
- 参照: `manifest.permissions`

## onDisable()
- 位置: L109-112
- 役割: 拡張の無効化時に隠したタブを表示に戻し、その拡張向けの通知確認を消す。
- 触るとき: 無効化時のタブ表示や通知の後始末を変えるとき。
- 呼び出し先: `showHiddenTabs()`, `tabHidePopup.clearConfirmation()`

## onUninstall()
- 位置: L114-116
- 役割: アンインストール時に、その拡張向けのタブ非表示通知の確認状態を消す。
- 触るとき: アンインストール時の通知の後始末を変えるとき。
- 呼び出し先: `tabHidePopup.clearConfirmation()`

## tabEventRegistrar()
- 位置: L118-140
- 役割: タブイベントについて、拡張がアクセスできるタブだけを通すリスナーを tabTracker に登録する。
- 触るとき: 新しいタブイベントを追加するとき、タブのアクセス権によるイベントの絞り込みを調べるとき。
- 呼び出し先: `tabTracker.on()`

## listener2()
- 位置: L122-128
- 役割: アクセスできるタブのイベントだけ、元のリスナーへ fire と一緒に渡す。
- 触るとき: タブ単位のイベント絞り込みを変えるとき。
- 呼び出し先: `listener()`, `tabManager.canAccessTab()`
- 参照: `eventData.nativeTab`

## unregister()
- 位置: L132-134
- 役割: tabTracker からその絞り込み付きリスナーを外す。
- 触るとき: タブイベントの購読解除後も通知が届く問題を調べるとき。
- 呼び出し先: `tabTracker.off()`

## convert()
- 位置: L135-137
- 役割: 永続イベントの復元時に、登録済みの fire を新しいものへ差し替える。
- 触るとき: 再起動後にタブイベントが古い fire へ送られる問題を調べるとき。

## listener()
- 位置: L145-152
- 役割: tab-activated の情報から、前のタブが私有ウィンドウのもので拡張が私有を許可されていなければ previousTabId を消して onActivated へ送る。
- 触るとき: onActivated の値や私有タブの扱いを変えるとき。
- 呼び出し先: `fire.async()`
- 参照: `extension.privateBrowsingAllowed`

## listener()
- 位置: L156-161
- 役割: tab-attached の情報から、タブ ID と新しいウィンドウ ID、位置を onAttached へ送る。
- 触るとき: onAttached の引数を変えるとき。
- 呼び出し先: `fire.async()`
- 参照: `event.newPosition`, `event.newWindowId`, `event.tabId`

## listener()
- 位置: L165-168
- 役割: tab-created のタブを変換して onCreated へ送る。
- 触るとき: onCreated に渡すタブ情報の内容を変えるとき。
- 呼び出し先: `fire.async()`, `tabManager.convert()`
- 参照: `event.currentTabSize`, `event.nativeTab`, `this.extension`

## listener()
- 位置: L172-177
- 役割: tab-detached の情報から、タブ ID と元のウィンドウ ID、位置を onDetached へ送る。
- 触るとき: onDetached の引数を変えるとき。
- 呼び出し先: `fire.async()`
- 参照: `event.oldPosition`, `event.oldWindowId`, `event.tabId`

## listener()
- 位置: L181-186
- 役割: tab-removed の情報から、タブ ID と閉じたウィンドウ ID、ウィンドウが閉じているかを onRemoved へ送る。
- 触るとき: onRemoved の引数を変えるとき。
- 呼び出し先: `fire.async()`
- 参照: `event.isWindowClosing`, `event.tabId`, `event.windowId`

## onMoved()
- 位置: L188-218
- 役割: TabMove のうち位置が実際に変わったものだけを、タブ ID、ウィンドウ ID、移動前後の位置として onMoved へ送る。
- 触るとき: onMoved の発火条件を変えるとき、グループの変更だけで通知が出ていないかを確認するとき。
- 呼び出し先: `windowTracker.addListener()`
- 参照: `this.extension`

## moveListener()
- 位置: L193-207
- 役割: TabMove の前後の tabIndex を比べ、違っていてアクセスできるタブなら fire する。
- 触るとき: タブ移動の通知判定を変えるとき。
- 呼び出し先: `tabManager.canAccessTab()`
- 条件付き依存: `if (fromIndex !== toIndex && tabManager.canAccessTab(nativeTab))` → `fire.async()`
- 条件付き依存: `if (fromIndex !== toIndex && tabManager.canAccessTab(nativeTab))` → `tabTracker.getId()`
- 条件付き依存: `if (fromIndex !== toIndex && tabManager.canAccessTab(nativeTab))` → `windowTracker.getId()`
- 参照: `currentTabState.tabIndex`, `event.detail`, `event.originalTarget`, `nativeTab.documentGlobal`, `previousTabState.tabIndex`

## unregister()
- 位置: L211-213
- 役割: TabMove のリスナーを windowTracker から外す。
- 触るとき: onMoved の購読解除を調べるとき。
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L214-216
- 役割: 登録済みの fire を新しいものへ差し替える。
- 触るとき: onMoved の永続イベントの復元を変えるとき。

## onHighlighted()
- 位置: L220-249
- 役割: タブの選択状態が変わったとき、アクセスできるウィンドウの強調中タブ ID 一覧を onHighlighted へ送る。
- 触るとき: onHighlighted の値や発火の条件を変えるとき。
- 呼び出し先: `tabTracker.on()`
- 参照: `this.extension`

## highlightListener()
- 位置: L222-237
- 役割: tabs-highlighted の対象ウィンドウを取り、その強調中タブの ID を集めて fire する。
- 触るとき: 強調中タブの情報の取り方を変えるとき、ウィンドウが無い場合に通知が落ちる問題を調べるとき。
- 呼び出し先: `Array.from()`, `fire.async()`, `windowManager.getWrapper()`, `windowTracker.getWindow()`, `windowWrapper.getHighlightedTabs()`
- 参照: `event.windowId`, `tab.id`

## unregister()
- 位置: L241-243
- 役割: tabs-highlighted のリスナーを外す。
- 触るとき: onHighlighted の購読解除を調べるとき。
- 呼び出し先: `tabTracker.off()`

## convert()
- 位置: L244-247
- 役割: 登録済みの fire と context を新しいものへ差し替える。
- 触るとき: onHighlighted の永続イベントの復元を変えるとき。

## onUpdated()
- 位置: L251-545
- 役割: フィルターに合うタブの変化を集め、必要なプロパティだけを changeInfo にして onUpdated へ送る。status、url、attention、音量、ミュート、ラベル、ピン留め、グループ、分割表示、非表示などを扱う。
- 触るとき: onUpdated の発火条件や changeInfo の中身を変えるとき、特定のプロパティの変化が届かない問題を調べるとき。
- 呼び出し先: `filter.properties.has()`, `windowTracker.addListener()`
- 条件付き依存: `if (filter.properties)` → `filter.properties.some()`
- 条件付き依存: `if (filter.properties)` → `allAttrs.has()`
- 条件付き依存: `if (filter.properties.has("status") || filter.properties.has("url"))` → `listeners.set()`
- 条件付き依存: `if (needsModified)` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("pinned"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("discarded"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("groupId"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("splitViewId"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("hidden"))` → `listeners.set()`
- 条件付き依存: `if (filter.properties.has("isArticle"))` → `tabTracker.on()`
- 条件付き依存: `if (filter.properties.has("openerTabId"))` → `tabTracker.on()`
- 参照: `filter.properties`, `filter.urls`

## sanitize()
- 位置: L270-285
- 役割: 変化のうち制限付きのプロパティ(url、favIconUrl、title)は、タブにホスト権限が無ければ除外して返す。
- 触るとき: タブ情報の公開範囲を変えるとき、権限が無いのに url や title が渡る問題を調べるとき。
- 呼び出し先: `restricted.has()`
- 参照: `tab.hasTabPermission`

## getWindowID()
- 位置: L287-296
- 役割: WINDOW_ID_CURRENT を、現在のコンテキストの最上位ウィンドウの ID に置き換える。
- 触るとき: フィルターの windowId の扱いを変えるとき。
- 条件付き依存: `if (windowId === Window.WINDOW_ID_CURRENT)` → `windowTracker.getTopWindow()`
- 条件付き依存: `if (windowId === Window.WINDOW_ID_CURRENT)` → `windowTracker.getId()`
- 参照: `Window.WINDOW_ID_CURRENT`

## matchFilters()
- 位置: L298-321
- 役割: tabId、windowId、cookieStoreId、urls のフィルター条件に、タブが合うかを判定する。
- 触るとき: onUpdated のフィルターの条件を増やすとき、フィルターが効かない問題を調べるとき。
- 呼び出し先: `getWindowID()`
- 条件付き依存: `if (filter.urls)` → `filter.urls.matches()`
- 参照: `filter.cookieStoreId`, `filter.tabId`, `filter.urls`, `filter.windowId`, `tab._uri`, `tab.cookieStoreId`, `tab.hasTabPermission`, `tab.id`, `tab.windowId`

## fireForTab()
- 位置: L323-339
- 役割: フィルターに合うタブで変化があれば、タブが開き終わるのを待ってから onUpdated を送る。
- 触るとき: onUpdated の送信タイミングや、タブ破棄後の送信抑止を変えるとき。
- 呼び出し先: `matchFilters()`, `sanitize()`
- 条件付き依存: `if (changeInfo)` → `tabTracker.maybeWaitForTabOpen(nativeTab).then()`
- 条件付き依存: `if (changeInfo)` → `tabTracker.maybeWaitForTabOpen()`
- 条件付き依存: `if (changeInfo)` → `fire.async()`
- 条件付き依存: `if (changeInfo)` → `tab.convert()`
- 参照: `nativeTab.parentNode`, `tab.id`

## listener()
- 位置: L341-450
- 役割: TabAttrModified、TabPinned、TabBrowserInserted、TabGrouped、TabMove などのイベントを、変化したプロパティの名前に対応づけて fireForTab へ渡す。採用中のタブや分割表示の移動は無視する。
- 触るとき: onUpdated で新しいタブイベントを扱うとき、グループや分割表示の変更で通知が重複する問題を調べるとき。
- 呼び出し先: `extension.canAccessWindow()`, `fireForTab()`, `tabManager.getWrapper()`, `updatedTab.documentGlobal.gBrowserInit?.isAdoptingTab()`
- 条件付き依存: `if (event.type == "TabAttrModified")` → `changed.includes()`
- 条件付き依存: `if (event.type == "TabAttrModified")` → `filter.properties.has()`
- 条件付き依存: `if ( changed.includes("image") && filter.properties.has("favIconUrl") )` → `needed.push()`
- 条件付き依存: `if (changed.includes("muted") && filter.properties.has("mutedInfo"))` → `needed.push()`
- 条件付き依存: `if ( changed.includes("soundplaying") && filter.properties.has("audible") )` → `needed.push()`
- 条件付き依存: `if ( changed.includes("undiscardable") && filter.properties.has("autoDiscardable") )` → `needed.push()`
- 条件付き依存: `if (changed.includes("label") && filter.properties.has("title"))` → `needed.push()`
- 条件付き依存: `if ( changed.includes("sharing") && filter.properties.has("sharingState") )` → `needed.push()`
- 条件付き依存: `if ( changed.includes("attention") && filter.properties.has("attention") )` → `needed.push()`
- 条件付き依存: `if (event.type == "TabPinned")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabUnpinned")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabBrowserInserted")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabBrowserDiscarded")` → `needed.push()`
- 条件付き依存: `if (event.type === "TabGrouped")` → `needed.push()`
- 条件付き依存: `if (event.type === "TabUngrouped")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabMove")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabShow")` → `needed.push()`
- 条件付き依存: `if (event.type == "TabHide")` → `needed.push()`
- 参照: `currentTabState.splitViewId`, `event.detail`, `event.detail.adoptingSplitView`, `event.detail.changed`, `event.detail.insertedOnTabCreation`, `event.originalTarget`, `event.originalTarget.documentGlobal`, `event.type`, `previousTabState.splitViewId`, `updatedTab.group`, `updatedTab.initializing`

## statusListener()
- 位置: L452-470
- 役割: 読み込み状態(status)と URL の変化を、アクセスできるタブについて onUpdated の changeInfo に入れて送る。
- 触るとき: 読み込み中の status や url の通知を変えるとき。
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (tabElem)` → `extension.canAccessWindow()`
- 条件付き依存: `if (tabElem)` → `filter.properties.has()`
- 条件付き依存: `if (tabElem)` → `fireForTab()`
- 条件付き依存: `if (tabElem)` → `tabManager.wrapTab()`
- 参照: `browser.documentGlobal`, `changed.status`, `changed.url`, `tabElem.documentGlobal`

## isArticleChangeListener()
- 位置: L472-480
- 役割: タブが記事か判定された結果(isArticle)を、そのタブの onUpdated として送る。
- 触るとき: isArticle の通知の経路を変えるとき。
- 呼び出し先: `extension.canAccessWindow()`, `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (nativeTab && extension.canAccessWindow(nativeTab.documentGlobal))` → `tabManager.getWrapper()`
- 条件付き依存: `if (nativeTab && extension.canAccessWindow(nativeTab.documentGlobal))` → `fireForTab()`
- 参照: `message.data.isArticle`, `message.target`, `message.target.documentGlobal`, `nativeTab.documentGlobal`

## openerTabIdChangeListener()
- 位置: L482-485
- 役割: タブの openerTabId が変わったとき、その値を onUpdated として送る。
- 触るとき: openerTabId の変化の通知を変えるとき。
- 呼び出し先: `fireForTab()`, `tabManager.getWrapper()`

## unregister()
- 位置: L527-539
- 役割: onUpdated で登録した各リスナーと、isArticle、openerTabId のリスナーを外す。
- 触るとき: onUpdated の購読解除後にリスナーが残る問題を調べるとき。
- 呼び出し先: `filter.properties.has()`, `windowTracker.removeListener()`
- 条件付き依存: `if (filter.properties.has("isArticle"))` → `tabTracker.off()`
- 条件付き依存: `if (filter.properties.has("openerTabId"))` → `tabTracker.off()`

## convert()
- 位置: L540-543
- 役割: 登録済みの fire と context を新しいものへ差し替える。
- 触るとき: onUpdated の永続イベントの復元を変えるとき。

## getAPI()
- 位置: L548-1847
- 役割: tabs 名前空間の全イベントと関数を組み立てて返す。各関数で使う補助関数もここで定義する。
- 触るとき: tabs API に関数やイベントを追加するとき、どの関数がどの補助関数を使うかを調べるとき。
- 呼び出し先: `new EventManager({ context, module, event: "onActivated", extensionApi, }).api()`, `new EventManager({ context, module, event: "onAttached", extensionApi, }).api()`, `new EventManager({ context, module, event: "onCreated", extensionApi, }).api()`, `new EventManager({ context, module, event: "onDetached", extensionApi, }).api()`, `new EventManager({ context, module, event: "onHighlighted", extensionApi, }).api()`, `new EventManager({ context, module, event: "onMoved", extensionApi, }).api()`, `new EventManager({ context, module, event: "onRemoved", extensionApi, }).api()`, `new EventManager({ context, module, event: "onUpdated", extensionApi, }).api()`, `new EventManager({ context, name: "tabs.onReplaced", register: () => { return () => {}; }, }).api()`

## getTabOrActive()
- 位置: L554-565
- 役割: タブ ID が null なら現在のアクティブタブを、それ以外は指定のタブを取り、アクセスできなければ例外にする。
- 触るとき: タブを指定する API の既定値や、拒否時のエラー文言を変えるとき。
- 呼び出し先: `tabManager.canAccessTab()`, `tabTracker.getTab()`
- 参照: `tabTracker.activeTab`

## getNativeTabsFromIDArray()
- 位置: L567-578
- 役割: タブ ID か配列を受け取り、各タブをネイティブのタブへ変換する。アクセスできないタブがあれば例外にする。
- 触るとき: 複数タブを対象にする API の入力の扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `tabIds.map()`, `tabManager.canAccessTab()`, `tabTracker.getTab()`

## getNativeTabsOrSplitViews()
- 位置: L580-582
- 役割: タブ一覧を、分割表示があればその単位にまとめて重複を除く。
- 触るとき: 分割表示を含むタブ操作の対象を変えるとき。
- 呼び出し先: `Array.from()`, `nativeTabs.map()`
- 参照: `t.splitview`

## updateNativeTabAfterAdopt()
- 位置: L584-590
- 役割: タブがウィンドウ間で移された後、対象の一覧の古いタブを新しいタブに置き換える。
- 触るとき: ウィンドウ間の移動で対象一覧が古いタブを指す問題を調べるとき。
- 参照: `nativeTabs.length`

## promiseTabWhenReady()
- 位置: async L592-608
- 役割: タブ(省略時はアクティブタブ)を取り、読み込みの準備ができてから解決する。
- 触るとき: スクリプト実行や CSS 挿入など、読み込み後のタブに対する API を変えるとき。
- 呼び出し先: `tabTracker.awaitTabReady()`
- 条件付き依存: `if (tabId !== null)` → `tabManager.get()`
- 条件付き依存: `if (!(tabId !== null))` → `tabManager.getWrapper()`
- 参照: `tab.nativeTab`, `tabTracker.activeTab`

## setContentTriggeringPrincipal()
- 位置: L610-625
- 役割: 指定 URL 用の content principal を作って options.triggeringPrincipal にする。私有タブなら privateBrowsingId を 1 にする。
- 触るとき: 拡張の権限では直接開けない newtab や about、moz-extension の URL を開くときの権限を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `options.triggeringPrincipal`, `options.userContextId`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## register()
- 位置: L674-676
- 役割: tabs.onReplaced 用の登録関数。何もせず、空の解除関数を返す。
- 触るとき: onReplaced を実装するとき、このイベントが実際には発火しないことを確認するとき。

## create()
- 位置: L693-831
- 役割: 指定のウィンドウ(省略時は通常の最上位ウィンドウ)の起動完了後に、URL、位置、ピン留め、破棄状態での作成を整えてタブを作り、変換して返す。
- 触るとき: tabs.create の引数の検証、アクティブ化、破棄状態のタブの扱いを変えるとき、作成時の URL 判定を調べるとき。
- 呼び出し先: `ExtensionUtils.isExtensionUrl()`, `context.canAccessWindow()`, `tabManager.convert()`, `tabTracker.addTabReadyBlocker()`, `url.startsWith()`, `window.gBrowser.addTab()`, `windowTracker.getTopNormalWindow()`, `windowTracker.getWindow()`
- 条件付き依存: `if (!gBrowserInit || !gBrowserInit.delayedStartupFinished)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(!gBrowserInit || !gBrowserInit.delayedStartupFinished))` → `resolve()`
- 条件付き依存: `if (createProperties.cookieStoreId)` → `getUserContextIdForCookieStoreId()`
- 条件付き依存: `if (createProperties.cookieStoreId)` → `PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (createProperties.url !== null)` → `context.uri.resolve()`
- 条件付き依存: `if (createProperties.url !== null)` → `ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (createProperties.url !== null)` → `context.checkLoadURL()`
- 条件付き依存: `if ( !ExtensionUtils.isExtensionUrl(url) && !context.checkLoadURL(url, { dontReportErrors: true }) )` → `Promise.reject()`
- 条件付き依存: `if (createProperties.openInReaderMode)` → `encodeURIComponent()`
- 条件付き依存: `if (!discardable || ExtensionUtils.isExtensionUrl(url))` → `setContentTriggeringPrincipal()`
- 条件付き依存: `if (createProperties.openerTabId !== null)` → `tabTracker.getTab()`
- 条件付き依存: `if (options.ownerTab.documentGlobal !== window)` → `Promise.reject()`
- 条件付き依存: `if (active)` → `Promise.reject()`
- 条件付き依存: `if (createProperties.pinned)` → `Promise.reject()`
- 条件付き依存: `if (!discardable)` → `Promise.reject()`
- 条件付き依存: `if (createProperties.title)` → `Promise.reject()`
- 条件付き依存: `if (!createProperties.url)` → `window.gURLBar.select()`
- 条件付き依存: `if (createProperties.muted)` → `nativeTab.toggleMuteAudio()`
- 参照: `context.principal`, `createProperties.active`, `createProperties.cookieStoreId`, `createProperties.discarded`, `createProperties.index`, `createProperties.muted`, `createProperties.openInReaderMode`, `createProperties.openerTabId`, `createProperties.pinned`, `createProperties.title`, `createProperties.url`, `createProperties.windowId`, `currentTab.linkedBrowser`, `extension.id`, `frameLoader.lazyHeight`, `frameLoader.lazyWidth`, `gBrowserInit.delayedStartupFinished`, `options.createLazyBrowser`, `options.lazyTabTitle`, `options.openerBrowser`, `options.ownerTab`, `options.ownerTab.documentGlobal`, `options.ownerTab.linkedBrowser`, `options.pinned`, `options.tabIndex`, `options.userContextId`, `window.BROWSER_NEW_TAB_URL`, `window.gBrowser`, `window.gBrowser.selectedTab`
- XPCOM: `Services.obs`

## obs()
- 位置: L706-715
- 役割: ウィンドウの起動完了通知を一度だけ受けて、そのウィンドウで解決するオブザーバー。
- 触るとき: 起動直後のウィンドウにタブを作る際の待ち方を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `resolve()`
- XPCOM: `Services.obs`

## remove()
- 位置: async L833-858
- 役割: タブ一つならそのまま閉じ、複数なら各ウィンドウごとに一度の removeTabs で閉じる。アニメーションと確認ダイアログは出さない。
- 触るとき: tabs.remove の閉じ方や、閉じた数の数え方(最近閉じたタブ)を変えるとき。
- 呼び出し先: `eachWindow.gBrowser.removeTabs()`, `getNativeTabsFromIDArray()`, `windowTabMap.entries()`, `windowTabMap.get()`, `windowTabMap.get(nativeTab.documentGlobal).push()`
- 条件付き依存: `if (nativeTabs.length === 1)` → `nativeTabs[0].documentGlobal.gBrowser.removeTab()`
- 参照: `nativeTab.documentGlobal`, `nativeTabs.length`

## discard()
- 位置: async L860-870
- 役割: 対象タブの破棄の準備を待ってから、それぞれのブラウザーを破棄する。
- 触るとき: tabs.discard の挙動を変えるとき、破棄されないタブがある問題を調べるとき。
- 呼び出し先: `Promise.all()`, `getNativeTabsFromIDArray()`, `nativeTab.documentGlobal.gBrowser.discardBrowser()`, `nativeTab.documentGlobal.gBrowser.prepareDiscardBrowser()`, `nativeTabs.map()`

## update()
- 位置: async L872-968
- 役割: URL の読み込み、アクティブ化、自動破棄の可否、強調表示、ミュート、ピン留め、opener、successor を順に適用して、更新後のタブを返す。
- 触るとき: tabs.update の項目を増やすとき、個々のプロパティが反映されない問題を調べるとき。
- 呼び出し先: `getTabOrActive()`, `tabManager.convert()`
- 条件付き依存: `if (updateProperties.url !== null)` → `context.uri.resolve()`
- 条件付き依存: `if (updateProperties.url !== null)` → `context.checkLoadURL()`
- 条件付き依存: `if (!context.checkLoadURL(url, { dontReportErrors: true }))` → `ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (ExtensionUtils.isExtensionUrl(url))` → `setContentTriggeringPrincipal()`
- 条件付き依存: `if (!(ExtensionUtils.isExtensionUrl(url)))` → `Promise.reject()`
- 条件付き依存: `if (nativeTab.linkedPanel)` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if (!(nativeTab.linkedPanel))` → `nativeTab.addEventListener()`
- 条件付き依存: `if (!(nativeTab.linkedPanel))` → `browser.fixupAndLoadURIString()`
- 条件付き依存: `if (!(nativeTab.linkedPanel))` → `tabbrowser.insertBrowser()`
- 条件付き依存: `if (!nativeTab.selected && !nativeTab.multiselected)` → `tabbrowser.addToMultiSelectedTabs()`
- 条件付き依存: `if (updateProperties.active !== false)` → `tabbrowser.lockClearMultiSelectionOnce()`
- 条件付き依存: `if (!(updateProperties.highlighted))` → `tabbrowser.removeFromMultiSelectedTabs()`
- 条件付き依存: `if (nativeTab.muted != updateProperties.muted)` → `nativeTab.toggleMuteAudio()`
- 条件付き依存: `if (updateProperties.pinned)` → `tabbrowser.pinTab()`
- 条件付き依存: `if (!(updateProperties.pinned))` → `tabbrowser.unpinTab()`
- 条件付き依存: `if (updateProperties.openerTabId !== null)` → `tabTracker.setOpener()`
- 条件付き依存: `if (updateProperties.successorTabId !== TAB_ID_NONE)` → `tabTracker.getTab()`
- 条件付き依存: `if (updateProperties.successorTabId !== null)` → `tabbrowser.setSuccessor()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `context.principal`, `extension.id`, `nativeTab.documentGlobal.gBrowser`, `nativeTab.linkedBrowser`, `nativeTab.linkedPanel`, `nativeTab.multiselected`, `nativeTab.muted`, `nativeTab.ownerDocument`, `nativeTab.selected`, `nativeTab.undiscardable`, `successor.ownerDocument`, `tabbrowser.selectedTab`, `updateProperties.active`, `updateProperties.autoDiscardable`, `updateProperties.highlighted`, `updateProperties.loadReplace`, `updateProperties.muted`, `updateProperties.openerTabId`, `updateProperties.pinned`, `updateProperties.successorTabId`, `updateProperties.url`
- XPCOM: [`nsIWebNavigation`](../../../../docshell/base/nsIWebNavigation.idl.md)

## reload()
- 位置: async L970-978
- 役割: 対象タブを再読み込みする。bypassCache が真ならキャッシュを使わずに読み込む。
- 触るとき: tabs.reload の再読み込み方法を変えるとき。
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.reloadWithFlags()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_BYPASS_CACHE`, `Ci.nsIWebNavigation.LOAD_FLAGS_NONE`, `reloadProperties.bypassCache`
- XPCOM: [`nsIWebNavigation`](../../../../docshell/base/nsIWebNavigation.idl.md)

## warmup()
- 位置: async L980-987
- 役割: 対象タブをウォームアップ(先読みして読み込み準備)する。
- 触るとき: tabs.warmup の対象や条件を変えるとき。
- 呼び出し先: `tabManager.canAccessTab()`, `tabTracker.getTab()`, `tabbrowser.warmupTab()`
- 参照: `nativeTab.documentGlobal.gBrowser`

## get()
- 位置: async L989-991
- 役割: タブ ID のタブを拡張向けの形に変換して返す。
- 触るとき: tabs.get の戻り値の形を変えるとき。
- 呼び出し先: `tabManager.get()`, `tabManager.get(tabId).convert()`

## getCurrent()
- 位置: L993-999
- 役割: 拡張のコンテキストに紐付くタブがあれば、その情報を返す。無ければ undefined。
- 触るとき: tabs.getCurrent が返す対象の決め方を変えるとき。
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (context.tabId)` → `tabManager.get(context.tabId).convert()`
- 条件付き依存: `if (context.tabId)` → `tabManager.get()`
- 参照: `context.tabId`

## query()
- 位置: async L1001-1005
- 役割: queryInfo の条件でタブを絞り、拡張向けの形に変換して返す。
- 触るとき: tabs.query の条件の扱いを変えるとき。
- 呼び出し先: `Array.from()`, `tab.convert()`, `tabManager.query()`

## captureTab()
- 位置: async L1007-1017
- 役割: 対象タブの読み込み完了を待ち、ズームを考慮してキャプチャする。
- 触るとき: tabs.captureTab の画像の生成を変えるとき。
- 呼び出し先: `getTabOrActive()`, `tab.capture()`, `tabManager.wrapTab()`, `tabTracker.awaitTabReady()`, `window.ZoomManager.getZoomForBrowser()`
- 参照: `browser.documentGlobal`, `nativeTab.linkedBrowser`

## captureVisibleTab()
- 位置: async L1019-1038
- 役割: 指定ウィンドウ(省略時は最上位)の選択中タブを、activeTab かすべての URL の権限がある場合だけキャプチャする。
- 触るとき: tabs.captureVisibleTab の権限チェックを変えるとき、activeTab 権限が無い拡張の挙動を調べるとき。
- 呼び出し先: `extension.hasPermission()`, `tab.capture()`, `tabManager.getWrapper()`, `tabTracker.awaitTabReady()`, `window.ZoomManager.getZoomForBrowser()`, `windowTracker.getTopWindow()`, `windowTracker.getWindow()`
- 参照: `tab.hasActiveTabPermission`, `tab.nativeTab`, `tab.nativeTab.linkedBrowser`, `window.gBrowser.selectedTab`

## detectLanguage()
- 位置: async L1040-1044
- 役割: 読み込み後のタブのコンテンツに言語判定を依頼し、最初の結果を返す。
- 触るとき: tabs.detectLanguage の判定経路を変えるとき。
- 呼び出し先: `promiseTabWhenReady()`, `tab.queryContent()`

## executeScript()
- 位置: async L1046-1049
- 役割: 読み込み後のタブでスクリプトを実行する。
- 触るとき: tabs.executeScript の実行経路を変えるとき。
- 呼び出し先: `promiseTabWhenReady()`, `tab.executeScript()`

## insertCSS()
- 位置: async L1051-1054
- 役割: 読み込み後のタブに CSS を挿入する。
- 触るとき: tabs.insertCSS の挿入経路を変えるとき。
- 呼び出し先: `promiseTabWhenReady()`, `tab.insertCSS()`

## removeCSS()
- 位置: async L1056-1059
- 役割: 読み込み後のタブから CSS を取り除く。
- 触るとき: tabs.removeCSS の取り除き方を変えるとき。
- 呼び出し先: `promiseTabWhenReady()`, `tab.removeCSS()`

## move()
- 位置: async L1061-1230
- 役割: タブを指定のウィンドウと位置へ移す。同じウィンドウなら並べ替え、別ウィンドウなら adopt する。分割表示は一つの単位として扱い、ピン留めの境界を越える位置は無視する。
- 触るとき: tabs.move の位置の計算、ピン留めや分割表示の扱い、別ウィンドウへの移動を変えるとき。
- 呼び出し先: `Array.isArray()`, `PrivateBrowsingUtils.isBrowserPrivate()`, `getNativeTabsFromIDArray()`, `lastInsertionMap.get()`, `lastInsertionMap.set()`, `splitviewTabs.at()`, `tabManager.convert()`, `tabsMoved.map()`, `tabsToMove.shift()`
- 条件付き依存: `if (moveProperties.windowId !== null)` → `windowTracker.getWindow()`
- 条件付き依存: `if (!destinationWindow)` → `Promise.reject()`
- 条件付き依存: `if (isSameWindow && gBrowser.tabs.length === 1)` → `lastInsertionMap.set()`
- 条件付き依存: `if (!(insertionPoint == -1))` → `Math.min()`
- 条件付き依存: `if (splitview)` → `splitviewTabs.find()`
- 条件付き依存: `if (!(otherTabInSplit === tabsToMove[0]))` → `tabsToMove.includes()`
- 条件付き依存: `if (tabsToMove.includes(otherTabInSplit))` → `splitview.unsplitTabs()`
- 条件付き依存: `if (wantReversedSplit)` → `splitview.reverseTabs()`
- 条件付き依存: `if (isSameWindow)` → `gBrowser.moveTabTo()`
- 条件付き依存: `if (splitview)` → `splitviewTabs.indexOf()`
- 条件付き依存: `if (splitview)` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (splitview)` → `Iterator.zip()`
- 条件付き依存: `if (splitview)` → `updateNativeTabAfterAdopt()`
- 条件付き依存: `if (!(splitview))` → `gBrowser.adoptTab()`
- 条件付き依存: `if (!(splitview))` → `updateNativeTabAfterAdopt()`
- 条件付き依存: `if (splitview)` → `tabsToMove.indexOf()`
- 条件付き依存: `if (splitview)` → `tabsToMove.splice()`
- 条件付き依存: `if (tabIsInTabsToMove)` → `tabsMoved.push()`
- 条件付き依存: `if (!(splitview))` → `tabsMoved.push()`
- 参照: `gBrowser.pinnedTabCount`, `gBrowser.tabs.length`, `moveProperties.index`, `moveProperties.windowId`, `nativeTab.documentGlobal`, `nativeTab.documentGlobal.gBrowser`, `nativeTab.index`, `nativeTab.pinned`, `nativeTab.splitview`, `otherTabInSplit.index`, `splitview.tabs`, `splitview?.tabs`, `splitviewTabs.at(-1).index`, `tabsToMove.length`, `window.gBrowser`

## duplicate()
- 位置: L1232-1257
- 役割: 対象タブを複製し、SSTabRestoring の時点で解決して変換したタブを返す。active が偽なら背景で開く。
- 触るとき: tabs.duplicate の位置や前面化の扱いを変えるとき。
- 呼び出し先: `gBrowser.duplicateTab()`, `getTabOrActive()`, `newTab.addEventListener()`, `resolve()`, `tabManager.convert()`, `tabTracker.addTabReadyBlocker()`
- 参照: `nativeTab.documentGlobal.gBrowser`

## getZoom()
- 位置: L1259-1266
- 役割: 対象タブのブラウザーに対するズーム率を返す。
- 触るとき: tabs.getZoom の値の取り方を変えるとき。
- 呼び出し先: `Promise.resolve()`, `ZoomManager.getZoomForBrowser()`, `getTabOrActive()`
- 参照: `nativeTab.documentGlobal`, `nativeTab.linkedBrowser`

## setZoom()
- 位置: L1268-1285
- 役割: ズーム率を設定する。0 なら既定値に戻し、範囲外なら拒否する。
- 触るとき: ズームの範囲の検査や既定値の扱いを変えるとき。
- 呼び出し先: `Promise.resolve()`, `getTabOrActive()`
- 条件付き依存: `if (zoom === 0)` → `FullZoom.reset()`
- 条件付き依存: `if (zoom >= ZoomManager.MIN && zoom <= ZoomManager.MAX)` → `FullZoom.setZoom()`
- 条件付き依存: `if (!(zoom >= ZoomManager.MIN && zoom <= ZoomManager.MAX))` → `Promise.reject()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `nativeTab.documentGlobal`, `nativeTab.linkedBrowser`

## getZoomSettings()
- 位置: async L1287-1297
- 役割: ズームの設定を、モードは automatic、範囲はサイトごとかタブごと、既定値付きで返す。
- 触るとき: tabs.getZoomSettings が返す項目を変えるとき。
- 呼び出し先: `ZoomUI.getGlobalValue()`, `getTabOrActive()`
- 参照: `FullZoom.siteSpecific`, `nativeTab.documentGlobal`

## setZoomSettings()
- 位置: async L1299-1315
- 役割: ズームの設定を変えようとするが、現在の設定と違う値は未対応として例外にする。
- 触るとき: ズーム設定の変更を対応させるとき。
- 呼び出し先: `Object.keys()`, `Object.keys(settings).every()`, `getTabOrActive()`, `tabTracker.getId()`, `this.getZoomSettings()`
- 条件付き依存: `if ( !Object.keys(settings).every( key => settings[key] === currentSettings[key] ) )` → `JSON.stringify()`

## register()
- 位置: L1320-1397
- 役割: タブ作成時の控えと、FullZoomChange と TextZoomChange の変化を監視し、ズーム率が変わったタブについて onZoomChange を送る。
- 触るとき: onZoomChange の発火条件や控えた値の扱いを変えるとき、同じ値で通知が出る問題を調べるとき。
- 呼び出し先: `context.canAccessWindow()`, `getZoomLevel()`, `tabTracker.off()`, `tabTracker.on()`, `windowTracker.addListener()`, `windowTracker.browserWindows()`, `windowTracker.removeListener()`, `zoomLevels.set()`
- 参照: `nativeTab.linkedBrowser`, `window.gBrowser.tabs`

## getZoomLevel()
- 位置: L1321-1325
- 役割: ブラウザーの現在のズーム率を ZoomManager から取る。
- 触るとき: ズーム率の取得元を変えるとき。
- 呼び出し先: `ZoomManager.getZoomForBrowser()`
- 参照: `browser.documentGlobal`

## tabCreated()
- 位置: L1342-1347
- 役割: タブが作られた、または別ウィンドウから移された時点で、そのブラウザーのズーム率を控える。私有タブは私有を許可された拡張の場合だけ控える。
- 触るとき: 新しいタブのズーム率を控える条件を変えるとき。
- 条件付き依存: `if (!event.isPrivate || context.privateBrowsingAllowed)` → `zoomLevels.set()`
- 条件付き依存: `if (!event.isPrivate || context.privateBrowsingAllowed)` → `getZoomLevel()`
- 参照: `context.privateBrowsingAllowed`, `event.isPrivate`, `event.nativeTab.linkedBrowser`

## zoomListener()
- 位置: async L1349-1383
- 役割: ズーム変化のイベントを受けて、トップレベルのタブについて前回と違う率なら控え直し、onZoomChange を送る。
- 触るとき: onZoomChange に渡す値(旧率、新率、ズーム設定)を変えるとき、ズーム変化が通知されない問題を調べるとき。
- 呼び出し先: `context.canAccessWindow()`, `gBrowser.getTabForBrowser()`, `getZoomLevel()`, `zoomLevels.get()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `zoomLevels.set()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `tabTracker.getId()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `fire.async()`
- 条件付き依存: `if (oldZoomFactor != newZoomFactor)` → `tabsApi.tabs.getZoomSettings()`
- 参照: `browser.DOCUMENT_NODE`, `browser.docShell.chromeEventHandler`, `browser.documentGlobal`, `browser.nodeType`, `event.originalTarget`

## print()
- 位置: L1400-1404
- 役割: アクティブタブの印刷ダイアログを開く。
- 触るとき: tabs.print の挙動を変えるとき。
- 呼び出し先: `PrintUtils.startPrintWindow()`, `getTabOrActive()`
- 参照: `activeTab.documentGlobal`, `activeTab.linkedBrowser.browsingContext`

## printPreview()
- 位置: L1407-1409
- 役割: 旧 API。print を呼んで、その結果を Promise で返す。
- 触るとき: 旧 API の互換性を保つ処理を変えるとき。
- 呼び出し先: `Promise.resolve()`, `this.print()`

## saveAsPDF()
- 位置: L1411-1564
- 役割: 保存先を選ぶダイアログを出し、印刷設定を組み立ててアクティブタブを PDF として保存する。結果は saved、replaced、not_saved などの文字列で返す。
- 触るとき: tabs.saveAsPDF の保存先の決め方、印刷設定の対応範囲、結果の文字列を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `DownloadPaths.sanitize()`, `getTabOrActive()`, `picker.appendFilter()`, `picker.init()`, `picker.open()`, `strBundle.GetStringFromName()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `decodeURIComponent()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `path.replace()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `path.split("/").pop()`
- 条件付き依存: `if (!(activeTab.linkedBrowser.contentTitle != ""))` → `path.split()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `Cc[ "@mozilla.org/network/file-output-stream;1" ].createInstance()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `fstream.init()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `fstream.close()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `resolve()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `Cc[ "@mozilla.org/gfx/printsettings-service;1" ].getService()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `psService.createNewPrintSettings()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `activeTab.linkedBrowser.browsingContext .print(printSettings) .then()`
- 条件付き依存: `if (retval == 0 || retval == 2)` → `activeTab.linkedBrowser.browsingContext .print()`
- 条件付き依存: `if (!(retval == 0 || retval == 2))` → `resolve()`
- 参照: `Ci.nsIFileOutputStream`, `Ci.nsIFilePicker`, `Ci.nsIFilePicker.modeSave`, `Ci.nsIPrintSettings.kOutputDestinationFile`, `Ci.nsIPrintSettings.kOutputFormatPDF`, `Ci.nsIPrintSettingsService`, `activeTab.documentGlobal.browsingContext`, `activeTab.linkedBrowser.contentTitle`, `activeTab.linkedBrowser.currentURI.spec`, `pageSettings.edgeBottom`, `pageSettings.edgeLeft`, `pageSettings.edgeRight`, `pageSettings.edgeTop`, `pageSettings.footerCenter`, `pageSettings.footerLeft`, `pageSettings.footerRight`, `pageSettings.headerCenter`, `pageSettings.headerLeft`, `pageSettings.headerRight`, `pageSettings.marginBottom`, `pageSettings.marginLeft`, `pageSettings.marginRight`, `pageSettings.marginTop`, `pageSettings.orientation`, `pageSettings.paperHeight`, `pageSettings.paperSizeUnit`, `pageSettings.paperWidth`, `pageSettings.scaling`, `pageSettings.showBackgroundColors`, `pageSettings.showBackgroundImages`, `pageSettings.shrinkToFit`, `pageSettings.toFileName`, `picker.defaultExtension`, `picker.defaultString`, `picker.file`, `picker.file.path`, `printSettings.edgeBottom`, `printSettings.edgeLeft`, `printSettings.edgeRight`, `printSettings.edgeTop`, `printSettings.footerStrCenter`, `printSettings.footerStrLeft`, `printSettings.footerStrRight`, `printSettings.headerStrCenter`, `printSettings.headerStrLeft`, `printSettings.headerStrRight`, `printSettings.isInitializedFromPrefs`, `printSettings.isInitializedFromPrinter`, `printSettings.marginBottom`, `printSettings.marginLeft`, `printSettings.marginRight`, `printSettings.marginTop`, `printSettings.orientation`, `printSettings.outputDestination`, `printSettings.outputFormat`, `printSettings.paperHeight`, `printSettings.paperSizeUnit`, `printSettings.paperWidth`, `printSettings.printBGColors`, `printSettings.printBGImages`, `printSettings.printSilent`, `printSettings.printerName`, `printSettings.scaling`, `printSettings.shrinkToFit`, `printSettings.toFileName`, `url.hostname`, `url.pathname`
- XPCOM: [`nsIFileOutputStream`](../../../../netwerk/base/nsIFileStreams.idl.md) / `nsIFilePicker` / [`nsIPrintSettings`](../../../../docshell/base/nsIDocumentViewer.idl.md) / `nsIPrintSettingsService` / `@mozilla.org/filepicker;1` / `@mozilla.org/gfx/printsettings-service;1` / `@mozilla.org/network/file-output-stream;1`

## toggleReaderMode()
- 位置: async L1566-1580
- 役割: 対象タブが記事か、既にリーダー表示なら、リーダー表示の切り替えを AboutReader に送る。そうでなければ例外にする。
- 触るとき: tabs.toggleReaderMode の条件やメッセージ送信を変えるとき。
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.sendMessageToActor()`, `promiseTabWhenReady()`
- 参照: `tab.isArticle`, `tab.isInReaderMode`

## moveInSuccession()
- 位置: L1582-1651
- 役割: タブ群を後継(successor)の鎖として並べ直す。append と insert の指定で、基準タブの前後や後継の位置を決める。
- 触るとき: 後継タブの順序を変えるとき、ID の重複や基準タブの扱いで例外が出る問題を調べるとき。
- 呼び出し先: `context.canAccessWindow()`, `referenceWindow.gBrowser.getSuccessor()`, `referenceWindow.gBrowser.replaceInSuccession()`, `tabIdSet.has()`, `tabManager.canAccessTab()`, `tabTracker.getTab()`
- 条件付き依存: `if (append)` → `referenceWindow.gBrowser.getSuccessor()`
- 条件付き依存: `if (append && tab === lastSuccessor)` → `referenceWindow.gBrowser.getSuccessor()`
- 条件付き依存: `if (previousTab)` → `referenceWindow.gBrowser.setSuccessor()`
- 条件付き依存: `if (!append && insert && lastSuccessor !== null)` → `referenceWindow.gBrowser.replaceInSuccession()`
- 参照: `referenceTab.documentGlobal`, `tab.documentGlobal`, `tabIdSet.size`, `tabIds.length`

## show()
- 位置: L1653-1659
- 役割: 指定タブを表示状態に戻す。
- 触るとき: tabs.show の対象の扱いを変えるとき。
- 呼び出し先: `getNativeTabsFromIDArray()`
- 条件付き依存: `if (tab.documentGlobal)` → `tab.documentGlobal.gBrowser.showTab()`
- 参照: `tab.documentGlobal`

## hide()
- 位置: L1661-1687
- 役割: 指定タブを隠し、隠せたタブ ID の一覧を返す。一つでも隠れたら、全タブボタンを見える場所へ移してタブ非表示の通知を出す。
- 触るとき: tabs.hide の戻り値や、非表示の通知の出し方を変えるとき。
- 呼び出し先: `getNativeTabsFromIDArray()`
- 条件付き依存: `if (tab.documentGlobal && !tab.hidden)` → `tab.documentGlobal.gBrowser.hideTab()`
- 条件付き依存: `if (tab.hidden)` → `hidden.push()`
- 条件付き依存: `if (tab.hidden)` → `tabTracker.getId()`
- 条件付き依存: `if (hidden.length)` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (hidden.length)` → `CustomizableUI.widgetIsLikelyVisible()`
- 条件付き依存: `if (!CustomizableUI.widgetIsLikelyVisible("alltabs-button", win))` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (hidden.length)` → `tabHidePopup.open()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `extension.id`, `hidden.length`, `tab.documentGlobal`, `tab.hidden`
- XPCOM: `Services.wm`

## highlight()
- 位置: L1689-1712
- 役割: 指定ウィンドウで、指定インデックスのタブを選択状態にして、そのウィンドウの情報を返す。タブが空なら例外にする。
- 触るとき: tabs.highlight の選択方法や例外の条件を変えるとき。
- 呼び出し先: `Array.isArray()`, `context.canAccessWindow()`, `tabManager.canAccessTab()`, `tabs.map()`, `windowManager.convert()`, `windowTracker.getWindow()`
- 参照: `Window.WINDOW_ID_CURRENT`, `tabs.length`, `window.gBrowser.selectedTabs`, `window.gBrowser.tabs`

## goForward()
- 位置: L1714-1717
- 役割: 対象タブを一つ先へ進める。
- 触るとき: tabs.goForward の挙動を変えるとき。
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.goForward()`

## goBack()
- 位置: L1719-1722
- 役割: 対象タブを一つ前へ戻る。
- 触るとき: tabs.goBack の挙動を変えるとき。
- 呼び出し先: `getTabOrActive()`, `nativeTab.linkedBrowser.goBack()`

## group()
- 位置: L1724-1814
- 役割: タブを新しいタブグループへ入れるか、既存のグループへ入れる。私有と非私有の混在は拒否し、ピン留めは外してからまとめる。
- 触るとき: tabs.group の配置位置や、私有ウィンドウとの混在の判定を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `getExtTabGroupIdForInternalTabGroupId()`, `getNativeTabsFromIDArray()`, `windowTracker.getWindow()`
- 条件付き依存: `if (options.groupId == null)` → `nativeTabs.find()`
- 条件付き依存: `if (options.groupId == null)` → `unpinTabsBeforeGrouping()`
- 条件付き依存: `if (options.groupId == null)` → `window.gBrowser.addTabGroup()`
- 条件付き依存: `if (options.groupId == null)` → `getNativeTabsOrSplitViews()`
- 条件付き依存: `if (!(options.groupId == null))` → `window.gBrowser.getTabGroupById()`
- 条件付き依存: `if (!(options.groupId == null))` → `getInternalTabGroupIdForExtTabGroupId()`
- 条件付き依存: `if (!(options.groupId == null))` → `unpinTabsBeforeGrouping()`
- 条件付き依存: `if ( nativeTab.documentGlobal === window && nativeTab.index < firstTabInGroup.index )` → `tabsBefore.push()`
- 条件付き依存: `if (!( nativeTab.documentGlobal === window && nativeTab.index < firstTabInGroup.index ))` → `tabsAfter.push()`
- 条件付き依存: `if (tabsBefore.length)` → `window.gBrowser.moveTabsBefore()`
- 条件付き依存: `if (tabsBefore.length)` → `getNativeTabsOrSplitViews()`
- 条件付き依存: `if (tabsAfter.length)` → `group.addTabs()`
- 条件付き依存: `if (tabsAfter.length)` → `getNativeTabsOrSplitViews()`
- 参照: `Window.WINDOW_ID_CURRENT`, `firstTabInGroup.index`, `firstTabInGroup.splitview`, `group.id`, `group.tabs`, `insertBefore.group.nextElementSibling`, `insertBefore?.splitview`, `nativeTab.documentGlobal`, `nativeTab.index`, `options.createProperties?.windowId`, `options.groupId`, `options.tabIds`, `t.documentGlobal`, `tabInWin.group`, `tabInWin.group.tabs`, `tabInWin.splitview?.tabs`, `tabInWin?.group`, `tabsAfter.length`, `tabsBefore.length`

## unpinTabsBeforeGrouping()
- 位置: L1746-1750
- 役割: グループに入れる前に、対象タブのピン留めを外す。
- 触るとき: グループ化とピン留めの関係を変えるとき。
- 呼び出し先: `nativeTab.documentGlobal.gBrowser.unpinTab()`

## ungroup()
- 位置: L1816-1843
- 役割: 対象タブをグループから外す。元の並び順をできるだけ保つように、グループの前か後ろへ移す。
- 触るとき: tabs.ungroup の並び順の保ち方を変えるとき、部分的な解除で順序が崩れる問題を調べるとき。
- 呼び出し先: `Tabbrowser.isSplitViewWrapper()`, `getNativeTabsFromIDArray()`, `getNativeTabsOrSplitViews()`, `tabs.sort()`
- 条件付き依存: `if (nativeTab.group)` → `ungroupOrder.get(nativeTab.group).push()`
- 条件付き依存: `if (nativeTab.group)` → `ungroupOrder.get()`
- 条件付き依存: `if (firstTab === group.tabs[0])` → `group.documentGlobal.gBrowser.moveTabsBefore()`
- 条件付き依存: `if (!(firstTab === group.tabs[0]))` → `group.documentGlobal.gBrowser.moveTabsAfter()`
- 参照: `a.index`, `b.index`, `firstTab.tabs`, `group.tabs`, `nativeTab.group`
