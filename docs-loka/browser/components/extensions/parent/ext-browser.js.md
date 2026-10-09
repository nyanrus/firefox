# browser/components/extensions/parent/ext-browser.js

source: browser/components/extensions/parent/ext-browser.js
source-hash: 6dec79782f28d055afed35514819ca02b0a51ce5
lines: 1357

## <module>
- 役割: tabs と windows の API 実装が共有するタブ・ウィンドウ追跡の基盤。TabTracker、WindowTracker、Tab、Window、TabManager、WindowManager をグローバルに置く。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Object.assign()`, `defineLazyGetter()`, `extensions.on()`

## isPrivateTab()
- 位置: L27-29
- 役割: タブのブラウザがプライベートブラウジングかどうかを返す。
- 触るとき: 拡張に返すタブの incognito 情報や、プライベートタブのイベント判定を調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`
- 参照: `nativeTab.linkedBrowser`

## global.openOptionsPage()
- 位置: L69-96
- 役割: 拡張のオプションページを、open_in_tab なら新しいタブで、そうでなければ about:addons の詳細画面で開く。ウィンドウがない・オプションがない場合は拒否する。
- 触るとき: runtime.openOptionsPage が開く先や失敗条件を変えるとき。
- 呼び出し先: `encodeURIComponent()`, `window.BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (!window)` → `Promise.reject()`
- 条件付き依存: `if (!optionsPageProperties)` → `Promise.reject()`
- 条件付き依存: `if (optionsPageProperties.open_in_tab)` → `window.switchToTabHavingURI()`
- 条件付き依存: `if (optionsPageProperties.open_in_tab)` → `Promise.resolve()`
- 参照: `extension.id`, `extension.principal`, `optionsPageProperties.open_in_tab`, `optionsPageProperties.page`, `windowTracker.topWindow`

## global.makeWidgetId()
- 位置: L98-102
- 役割: 拡張 ID を小文字にし、英数字、アンダースコア、ハイフン以外を _ に置き換えてウィジェット ID を作る。
- 触るとき: ツールバーボタンの ID の形式を変えるとき。コメントにもあるとおり衝突が起こり得る。
- 呼び出し先: `id.replace()`, `id.toLowerCase()`

## global.clickModifiersFromEvent()
- 位置: L104-120
- 役割: マウスイベントの修飾キーを Shift、Alt、Command、Ctrl の名前の配列にする。macOS で Ctrl を押したときは MacCtrl も加える。
- 触るとき: クリックの修飾キーが拡張の onClicked に正しく渡らないときに調べる。
- 呼び出し先: `Object.keys()`, `Object.keys(map) .filter()`, `Object.keys(map) .filter(key => event[key]) .map()`
- 条件付き依存: `if (event.ctrlKey && AppConstants.platform === "macosx")` → `modifiers.push()`
- 参照: `AppConstants.platform`, `event.ctrlKey`

## global.waitForTabLoaded()
- 位置: L122-137
- 役割: 進捗リスナーを付け、指定タブでトップレベルの位置が変わったとき（URL が指定されていればそれに一致したとき）に解決する Promise を返す。
- 触るとき: 拡張がタブの読み込み完了を待つ処理の判定条件を変えるとき。
- 呼び出し先: `windowTracker.addListener()`

## onLocationChange()
- 位置: L125-134
- 役割: トップレベルの場所変更で対象タブかつ（指定があれば）URL が一致したら、リスナーを外して待機を解決する。
- 触るとき: タブの読み込み待ちが終わらない、または早く終わる問題を調べるとき。
- 呼び出し先: `browser.documentGlobal.gBrowser.getTabForBrowser()`
- 条件付き依存: `if ( webProgress.isTopLevel && browser.documentGlobal.gBrowser.getTabForBrowser(browser) == tab && (!url || locationURI.spec == url) )` → `windowTracker.removeListener()`
- 条件付き依存: `if ( webProgress.isTopLevel && browser.documentGlobal.gBrowser.getTabForBrowser(browser) == tab && (!url || locationURI.spec == url) )` → `resolve()`
- 参照: `locationURI.spec`, `webProgress.isTopLevel`

## global.replaceUrlInTab()
- 位置: L139-146
- 役割: タブの履歴を置き換える形で URL を読み込み、読み込み完了を waitForTabLoaded で待つ Promise を返す。
- 触るとき: tabs.update で URL を変えたときの履歴の扱いや完了待ちを調べるとき。
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `gBrowser.loadURI()`, `waitForTabLoaded()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_REPLACE_HISTORY`, `uri.spec`
- XPCOM: [`nsIWebNavigation`](../../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## global.getExtTabGroupIdForInternalTabGroupId()
- 位置: L161-176
- 役割: 内部のタブグループ ID 文字列を整数に変換する。形式に合えば数字を連結し、合わなければ内部のマップで連番を振る。
- 触るとき: 拡張に返す groupId の値が毎回変わる、または重ならない問題を調べるとき。
- 呼び出し先: `/^(\d{13})-(\d{1,3})$/.exec()`, `fallbackTabGroupIdMap.get()`
- 条件付き依存: `if (parsedTabId)` → `parseInt()`
- 条件付き依存: `if (parsedTabId)` → `Number.isSafeInteger()`
- 条件付き依存: `if (!fallbackGroupId)` → `fallbackTabGroupIdMap.set()`

## global.getInternalTabGroupIdForExtTabGroupId()
- 位置: L177-189
- 役割: 拡張の整数の groupId を内部の文字列 ID に戻す。16 桁の整数なら分解し、そうでなければフォールバック用のマップを探す。見つからなければ null を返す。
- 触るとき: tabs API に渡された groupId から内部のグループを引けないときに調べる。
- 呼び出し先: `Number.isSafeInteger()`
- 条件付き依存: `if (Number.isSafeInteger(groupId) && groupId >= 1e15)` → `Math.floor()`

## constructor()
- 位置: L202-214
- 役割: タブとウィンドウごとの拡張データを WeakMap で保持し、進捗と TabSelect の監視、tab-adopted の購読を始める。
- 触るとき: タブごとの拡張データの保持方法や監視の始め方を変えるとき。
- 呼び出し先: `super()`, `tabTracker.on()`, `this.tabAdopted.bind()`, `windowTracker.addListener()`
- 参照: `this.getDefaultPrototype`, `this.tabAdopted`, `this.tabData`

## get()
- 位置: L223-230
- 役割: キーのオブジェクトに対応する拡張データを返す。無ければ既定のプロトタイプから作って保存する。
- 触るとき: タブやウィンドウに紐づく拡張データが既定値で作られる仕組みを追うとき。
- 呼び出し先: `this.tabData.get()`, `this.tabData.has()`
- 条件付き依存: `if (!this.tabData.has(keyObject))` → `Object.create()`
- 条件付き依存: `if (!this.tabData.has(keyObject))` → `this.getDefaultPrototype()`
- 条件付き依存: `if (!this.tabData.has(keyObject))` → `this.tabData.set()`

## clear()
- 位置: L238-240
- 役割: キーに対応する拡張データを削除する。
- 触るとき: タブが閉じた後に古いデータが残らないことを確かめるとき。
- 呼び出し先: `this.tabData.delete()`

## handleEvent()
- 位置: L242-248
- 役割: TabSelect を受けて、tab-select と location-change のイベントを発行する。
- 触るとき: タブ切り替え時に拡張側の状態が更新されない問題を調べるとき。
- 条件付き依存: `if (event.type == "TabSelect")` → `this.emit()`
- 参照: `event.target`, `event.type`

## onLocationChange()
- 位置: L250-264
- 役割: トップレベルの場所変更だけを受け、同じ文書内の変更でなければ fromBrowse を true にして location-change を発行する。
- 触るとき: pageAction や browserAction の表示を更新するタイミングを変えるとき。
- 呼び出し先: `gBrowser.getTabForBrowser()`, `this.emit()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `browser.documentGlobal.gBrowser`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## tabAdopted()
- 位置: L276-286
- 役割: タブが別ウィンドウへ移されたとき、旧タブの拡張データを新タブの拡張データへ移す。
- 触るとき: タブを別ウィンドウへ移したあとに拡張データが失われる問題を調べるとき。
- 呼び出し先: `Object.assign()`, `this.get()`, `this.tabData.delete()`, `this.tabData.get()`, `this.tabData.has()`

## shutdown()
- 位置: L291-295
- 役割: 進捗、TabSelect の監視と tab-adopted の購読を外す。
- 触るとき: TabContext を破棄する経路で監視が残る問題を調べるとき。
- 呼び出し先: `tabTracker.off()`, `windowTracker.removeListener()`
- 参照: `this.tabAdopted`

## WindowTracker.addProgressListener()
- 位置: L299-301
- 役割: ウィンドウのタブ群に進捗リスナーを追加する。
- 触るとき: 進捗イベントが拡張に届かない問題を調べるとき。
- 呼び出し先: `window.gBrowser.addTabsProgressListener()`

## WindowTracker.removeProgressListener()
- 位置: L303-305
- 役割: ウィンドウのタブ群から進捗リスナーを外す。
- 触るとき: リスナーの解除漏れを調べるとき。
- 呼び出し先: `window.gBrowser.removeTabsProgressListener()`

## WindowTracker.getTopNormalWindow()
- 位置: L315-324
- 役割: 拡張の権限とプライベートブラウジングの可否に応じて、最前面の通常ウィンドウを返す。ポップアップは除外し、別ワークスペースのウィンドウも対象にする。
- 触るとき: tabs.query など既定ウィンドウの選び方を変えるとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`
- 参照: `context.privateBrowsingAllowed`, `options.allowFromInactiveWorkspace`, `options.private`

## TabTracker.constructor()
- 位置: L328-337
- 役割: タブから内部 ID への WeakMap、ID から タブへの Map、次に振る ID などを初期化する。
- 触るとき: タブ ID の採番や保持の仕組みを変えるとき。
- 呼び出し先: `super()`, `this._handleTabDestroyed.bind()`
- 参照: `this._deferredTabOpenEvents`, `this._handleTabDestroyed`, `this._nextId`, `this._tabIds`, `this._tabs`

## TabTracker.init()
- 位置: L339-363
- 役割: 初回だけ、タブとウィンドウの開閉、選択、Reader の状態を監視し始める。tab-detached と tab-removed で ID を解放する。
- 触るとき: タブ関連のイベントが拡張に届き始める条件を調べるとき。
- 呼び出し先: `AboutReaderParent.addMessageListener()`, `this._handleWindowClose.bind()`, `this._handleWindowOpen.bind()`, `this.on()`, `windowTracker.addCloseListener()`, `windowTracker.addListener()`, `windowTracker.addOpenListener()`
- 参照: `this._handleTabDestroyed`, `this._handleWindowClose`, `this._handleWindowOpen`, `this.adoptedTabs`, `this.initialized`

## TabTracker.getId()
- 位置: L365-376
- 役割: タブに ID が無ければ初期化して新しい ID を振り、その ID を返す。
- 触るとき: 拡張に返すタブ ID が安定しない、または重複する問題を調べるとき。
- 呼び出し先: `this._tabs.get()`, `this.init()`, `this.setId()`
- 参照: `this._nextId`

## TabTracker.getTabForBrowser()
- 位置: L378-390
- 役割: ブラウザ要素からタブ要素を引く。about:addons の埋め込みオプションでは一段上の chromeEventHandler から引く。
- 触るとき: about:addons 内のブラウザがタブとして扱われない問題を調べるとき。
- 呼び出し先: `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (browser.id === "addon-inline-options")` → `browser.documentGlobal.gBrowser.getTabForBrowser()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.docShell.chromeEventHandler`, `browser.id`

## TabTracker.setId()
- 位置: L392-402
- 役割: 破棄済みや閉じたウィンドウのタブには ID を付けず、そうでなければタブと ID の双方向のマップに登録する。
- 触るとき: タブ ID の登録条件を変えるとき。
- 呼び出し先: `this._tabIds.set()`, `this._tabs.set()`
- 参照: `nativeTab.documentGlobal.closed`, `nativeTab.parentNode`

## TabTracker.adopt()
- 位置: L414-447
- 役割: 別ウィンドウへ移されたタブの ID を新しいタブへ引き継ぎ、tab-adopted と、必要なら tab-detached と tab-attached を発行する。
- 触るとき: タブのウィンドウ移動で ID が変わる、またはイベントが二重に出る問題を調べるとき。
- 呼び出し先: `this.adoptedTabs.add()`, `this.adoptedTabs.has()`, `this.emit()`, `this.getId()`, `this.has()`, `this.setId()`
- 条件付き依存: `if (this.has("tab-detached"))` → `windowTracker.getId()`
- 条件付き依存: `if (this.has("tab-detached"))` → `this.emit()`
- 条件付き依存: `if (this.has("tab-attached"))` → `windowTracker.getId()`
- 条件付き依存: `if (this.has("tab-attached"))` → `this.emit()`
- 参照: `nativeTab.documentGlobal`, `nativeTab.index`

## TabTracker._handleTabDestroyed()
- 位置: L449-457
- 役割: 破棄されるタブを ID のマップ両方から削除する。
- 触るとき: 閉じたタブの ID が残って tabs.get が古いタブを返す問題を調べるとき。
- 呼び出し先: `this._tabs.get()`
- 条件付き依存: `if (id)` → `this._tabs.delete()`
- 条件付き依存: `if (id)` → `this._tabIds.get()`
- 条件付き依存: `if (this._tabIds.get(id) === nativeTab)` → `this._tabIds.delete()`

## TabTracker.getTab()
- 位置: L471-480
- 役割: ID から タブ要素を返す。無ければ既定値を返し、既定値も無ければ Invalid tab ID の ExtensionError を投げる。
- 触るとき: tabs API で不正な tabId が渡されたときの振る舞いを調べるとき。
- 呼び出し先: `this._tabIds.get()`

## TabTracker.setOpener()
- 位置: L490-506
- 役割: 開いた元のタブ ID から opener のタブ要素を設定する。ID が -1 なら解除し、別ウィンドウのタブなら例外を投げる。
- 触るとき: tabs.update の openerTabId の挙動を変えるとき。
- 条件付き依存: `if (openerTabId > -1)` → `tabTracker.getTab()`
- 条件付き依存: `if (nativeTab.openerTab !== nativeOpenerTab)` → `this.emit()`
- 参照: `nativeOpenerTab.ownerDocument`, `nativeTab.openerTab`, `nativeTab.ownerDocument`

## TabTracker.deferredForTabOpen()
- 位置: L508-518
- 役割: タブ作成ごとに待機用の Promise を作り、解決後に Map から外す。
- 触るとき: onCreated より前に onActivated が届く順序の問題を調べるとき。
- 呼び出し先: `this._deferredTabOpenEvents.get()`
- 条件付き依存: `if (!deferred)` → `Promise.withResolvers()`
- 条件付き依存: `if (!deferred)` → `this._deferredTabOpenEvents.set()`
- 条件付き依存: `if (!deferred)` → `deferred.promise.then()`
- 条件付き依存: `if (!deferred)` → `this._deferredTabOpenEvents.delete()`

## TabTracker.maybeWaitForTabOpen()
- 位置: async L520-523
- 役割: そのタブの作成処理が未完了なら、その Promise を返す。
- 触るとき: タブ作成の後に来るイベントを待たせる仕組みを変えるとき。
- 呼び出し先: `this._deferredTabOpenEvents.get()`
- 参照: `deferred.promise`

## TabTracker.handleEvent()
- 位置: L530-604
- 役割: TabOpen、TabClose、TabSelect、TabMultiSelect を受け、採用、作成、削除、選択、複数選択の各イベントを発行する。作成は次のティックまで遅らせる。
- 触るとき: タブの作成、削除、選択のイベントが拡張に届く順序や条件を変えるとき。
- 呼び出し先: `this.adoptedTabs.has()`, `this.emitActivated()`, `this.has()`, `this.maybeWaitForTabOpen()`, `this.maybeWaitForTabOpen(nativeTab).then()`
- 条件付き依存: `if (adoptedTab)` → `this.adopt()`
- 条件付き依存: `if (!(adoptedTab))` → `this.deferredForTabOpen()`
- 条件付き依存: `if (!(adoptedTab))` → `Promise.resolve().then()`
- 条件付き依存: `if (!(adoptedTab))` → `Promise.resolve()`
- 条件付き依存: `if (!(adoptedTab))` → `deferred.resolve()`
- 条件付き依存: `if (!(adoptedTab))` → `this.emitCreated()`
- 条件付き依存: `if (adoptedBy)` → `this.adopt()`
- 条件付き依存: `if (!(adoptedBy))` → `this.emitRemoved()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `Promise.resolve().then()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `Promise.resolve()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `this.emitHighlighted()`
- 参照: `currentTab.linkedBrowser`, `event.detail`, `event.detail.previousTab`, `event.originalTarget`, `event.originalTarget.parentNode`, `event.target`, `event.target.documentGlobal`, `event.type`, `frameLoader.lazyHeight`, `frameLoader.lazyWidth`, `nativeTab.documentGlobal.gBrowser.selectedTab`, `nativeTab.parentNode`

## TabTracker.receiveMessage()
- 位置: L611-619
- 役割: Reader:UpdateReaderButton を受け、isArticle が定義されていれば tab-isarticle を発行する。
- 触るとき: タブの isArticle の値が更新されない問題を調べるとき。
- 条件付き依存: `if (message.data && message.data.isArticle !== undefined)` → `this.emit()`
- 参照: `message.data`, `message.data.isArticle`, `message.name`

## TabTracker._handleWindowOpen()
- 位置: L629-652
- 役割: 開かれたウィンドウが採用するタブがあれば採用を処理する。無ければ全タブの作成と最初のタブの有効化を発行し、必要なら複数選択も発行する。
- 触るとき: 新しいウィンドウを開いたときに拡張へ届くタブ関連イベントを調べるとき。
- 呼び出し先: `window.gBrowserInit.getTabToAdopt()`
- 条件付き依存: `if (tabToAdopt)` → `Tabbrowser.isTab()`
- 条件付き依存: `if (Tabbrowser.isTab(tabToAdopt))` → `this.adopt()`
- 条件付き依存: `if (!(tabToAdopt))` → `this.emitCreated()`
- 条件付き依存: `if (!(tabToAdopt))` → `this.emitActivated()`
- 条件付き依存: `if (!(tabToAdopt))` → `this.has()`
- 条件付き依存: `if (this.has("tabs-highlighted"))` → `this.emitHighlighted()`
- 参照: `window.gBrowser.tabs`

## TabTracker._handleWindowClose()
- 位置: L662-668
- 役割: 閉じるウィンドウの各タブについて、採用されていなければ削除イベントを発行する。
- 触るとき: ウィンドウを閉じたときに tabs.onRemoved が届く条件を調べるとき。
- 呼び出し先: `this.adoptedTabs.has()`
- 条件付き依存: `if (!this.adoptedTabs.has(nativeTab))` → `this.emitRemoved()`
- 参照: `window.gBrowser.tabs`

## TabTracker.emitActivated()
- 位置: L679-692
- 役割: タブが有効化されたことを、タブ ID、前のタブ ID、前のタブがプライベートか、ウィンドウ ID と共に発行する。
- 触るとき: tabs.onActivated の引数を変えるとき。
- 呼び出し先: `this.emit()`, `this.getId()`, `windowTracker.getId()`
- 条件付き依存: `if (previousTab && !previousTab.closing)` → `this.getId()`
- 条件付き依存: `if (previousTab && !previousTab.closing)` → `isPrivateTab()`
- 参照: `nativeTab.documentGlobal`, `previousTab.closing`

## TabTracker.emitHighlighted()
- 位置: L701-708
- 役割: 選択中のタブ ID の配列とウィンドウ ID を tabs-highlighted として発行する。
- 触るとき: tabs.onHighlighted の内容を変えるとき。
- 呼び出し先: `this.emit()`, `this.getId()`, `window.gBrowser.selectedTabs.map()`, `windowTracker.getId()`

## TabTracker.emitCreated()
- 位置: L719-724
- 役割: 新しいタブを、現在のタブのサイズと共に tab-created として発行する。
- 触るとき: tabs.onCreated の引数を変えるとき。
- 呼び出し先: `this.emit()`

## TabTracker.emitRemoved()
- 位置: L736-746
- 役割: 削除されるタブを、ウィンドウ ID、タブ ID、ウィンドウを閉じるかどうかと共に tab-removed として発行する。
- 触るとき: tabs.onRemoved の引数を変えるとき。
- 呼び出し先: `this.emit()`, `this.getId()`, `windowTracker.getId()`
- 参照: `nativeTab.documentGlobal`

## TabTracker.getBrowserData()
- 位置: L748-774
- 役割: ブラウザ要素から tabId と windowId を求める。タブが無ければ tabId は -1 とし、ブラウザウィンドウでなければ両方 -1 を返す。
- 触るとき: 拡張のポップアップやサイドバーの tabId や windowId が -1 になる問題を調べるとき。
- 呼び出し先: `this.getId()`, `this.getTabForBrowser()`, `windowTracker.getId()`
- 条件付き依存: `if (!(nativeTab))` → `windowTracker.isBrowserWindow()`
- 参照: `browser.documentGlobal`, `nativeTab.documentGlobal`, `window.browsingContext.topChromeWindow`

## TabTracker.activeTab()
- 位置: L776-782
- 役割: 最前面ウィンドウの選択中のタブを返す。無ければ null を返す。
- 触るとき: activeTab の既定値を調べるとき。
- 参照: `window.gBrowser`, `window.gBrowser.selectedTab`, `windowTracker.topWindow`

## Tab._favIconUrl()
- 位置: L791-793
- 役割: タブのファビコンの URL を gBrowser から取得する。
- 触るとき: favIconUrl が空になる問題を調べるとき。
- 呼び出し先: `this.window.gBrowser.getIcon()`
- 参照: `this.nativeTab`

## Tab.attention()
- 位置: L795-797
- 役割: タブに attention 属性があるかを返す。
- 触るとき: tab.attention の判定を変えるとき。
- 呼び出し先: `this.nativeTab.hasAttribute()`

## Tab.audible()
- 位置: L799-801
- 役割: タブで音が鳴っているかを返す。
- 触るとき: tab.audible の値が実際の再生と合わないときに調べる。
- 参照: `this.nativeTab.soundPlaying`

## Tab.autoDiscardable()
- 位置: L803-805
- 役割: タブが自動破棄の対象かを、undiscardable の反転で返す。
- 触るとき: tab.autoDiscardable が想定と逆に見えるときに調べる。
- 参照: `this.nativeTab.undiscardable`

## Tab.browser()
- 位置: L807-809
- 役割: タブの linkedBrowser を返す。
- 触るとき: 拡張内部でタブからブラウザ要素を取り出す箇所を追うとき。
- 参照: `this.nativeTab.linkedBrowser`

## Tab.discarded()
- 位置: L811-813
- 役割: タブが破棄済みか（linkedPanel が無いか）を返す。
- 触るとき: 破棄されたタブの扱いを調べるとき。
- 参照: `this.nativeTab.linkedPanel`

## Tab.frameLoader()
- 位置: L815-819
- 役割: タブの frameLoader を返し、無ければ幅と高さが 0 のダミーを返す。
- 触るとき: width や height が取れないタブで例外が出ないことを確かめるとき。
- 参照: `super.frameLoader`

## Tab.hidden()
- 位置: L821-823
- 役割: タブの hidden 属性を返す。
- 触るとき: tab.hidden の値を調べるとき。
- 参照: `this.nativeTab.hidden`

## Tab.sharingState()
- 位置: L825-827
- 役割: Tabbrowser からタブの画面共有状態を取得する。
- 触るとき: 共有中のタブの表示が拡張に正しく届かない問題を調べるとき。
- 呼び出し先: `Tabbrowser.getTabSharingState()`
- 参照: `this.nativeTab`

## Tab.cookieStoreId()
- 位置: L829-831
- 役割: タブのコンテナに対応する cookieStoreId を返す。
- 触るとき: コンテナタブの cookieStoreId の対応を変えるとき。
- 呼び出し先: `getCookieStoreIdForTab()`
- 参照: `this.nativeTab`

## Tab.openerTabId()
- 位置: L833-843
- 役割: 開いた元のタブが同じウィンドウにあれば、その ID を返す。無ければ null を返す。
- 触るとき: openerTabId が null になる、または別ウィンドウで値が出る問題を調べるとき。
- 条件付き依存: `if ( opener && opener.parentNode && opener.ownerDocument == this.nativeTab.ownerDocument )` → `tabTracker.getId()`
- 参照: `opener.ownerDocument`, `opener.parentNode`, `this.nativeTab.openerTab`, `this.nativeTab.ownerDocument`

## Tab.height()
- 位置: L845-847
- 役割: タブの frameLoader の lazyHeight を返す。
- 触るとき: tab の高さの値が古い、または 0 になる問題を調べるとき。
- 参照: `this.frameLoader.lazyHeight`

## Tab.index()
- 位置: L849-851
- 役割: タブのウィンドウ内での位置を返す。
- 触るとき: tab.index とタブ並びの対応を調べるとき。
- 参照: `this.nativeTab.index`

## Tab.mutedInfo()
- 位置: L853-865
- 役割: ミュート状態を、ユーザー操作か拡張による変更かの理由と拡張 ID を付けて返す。
- 触るとき: tab.mutedInfo の理由表示を変えるとき。
- 参照: `mutedInfo.extensionId`, `mutedInfo.reason`, `nativeTab.muteReason`, `nativeTab.muted`

## Tab.lastAccessed()
- 位置: L867-869
- 役割: タブが最後に開かれた時刻を返す。
- 触るとき: tab.lastAccessed の値を調べるとき。
- 参照: `this.nativeTab.lastAccessed`

## Tab.pinned()
- 位置: L871-873
- 役割: タブがピン留めされているかを返す。
- 触るとき: tab.pinned の判定を調べるとき。
- 参照: `this.nativeTab.pinned`

## Tab.active()
- 位置: L875-877
- 役割: タブが選択中かを返す。
- 触るとき: tab.active と選択中タブの対応を調べるとき。
- 参照: `this.nativeTab.selected`

## Tab.highlighted()
- 位置: L879-882
- 役割: タブが選択中か複数選択中かを返す。
- 触るとき: tab.highlighted の判定を変えるとき。
- 参照: `this.nativeTab`

## Tab.status()
- 位置: L884-889
- 役割: タブが busy 属性なら loading、そうでなければ complete を返す。
- 触るとき: tab.status が読み込み中に切り替わらない問題を調べるとき。
- 呼び出し先: `this.nativeTab.getAttribute()`

## Tab.width()
- 位置: L891-893
- 役割: タブの frameLoader の lazyWidth を返す。
- 触るとき: tab の幅の値が古い、または 0 になる問題を調べるとき。
- 参照: `this.frameLoader.lazyWidth`

## Tab.window()
- 位置: L895-897
- 役割: タブが属するブラウザウィンドウを返す。
- 触るとき: タブからウィンドウを引く箇所を追うとき。
- 参照: `this.nativeTab.documentGlobal`

## Tab.windowId()
- 位置: L899-901
- 役割: タブが属するウィンドウの ID を返す。
- 触るとき: tab.windowId が正しくない問題を調べるとき。
- 呼び出し先: `windowTracker.getId()`
- 参照: `this.window`

## Tab.isArticle()
- 位置: L903-905
- 役割: linkedBrowser の isArticle を返す。
- 触るとき: リーダー表示できる記事かどうかの判定を調べるとき。
- 参照: `this.nativeTab.linkedBrowser.isArticle`

## Tab.isInReaderMode()
- 位置: L907-909
- 役割: URL が about:reader で始まるかを返す。
- 触るとき: リーダーモードの判定を変えるとき。
- 呼び出し先: `this.url.startsWith()`
- 参照: `this.url`

## Tab.successorTabId()
- 位置: L911-914
- 役割: 閉じたときに選ばれる後続タブの ID を返す。無ければ -1 を返す。
- 触るとき: successorTabId の計算を変えるとき。
- 呼び出し先: `tabTracker.getId()`, `this.window.gBrowser.getSuccessor()`
- 参照: `this.nativeTab`

## Tab.groupId()
- 位置: L916-919
- 役割: タブのグループを拡張の整数 ID にして返す。グループが無ければ -1 を返す。
- 触るとき: タブグループの ID が拡張へ正しく渡らない問題を調べるとき。
- 呼び出し先: `getExtTabGroupIdForInternalTabGroupId()`
- 参照: `group.id`, `this.nativeTab`

## Tab.splitViewId()
- 位置: L921-924
- 役割: 分割表示の ID を返す。分割表示が無ければ -1 を返す。
- 触るとき: 分割表示の ID の扱いを変えるとき。
- 参照: `splitview.splitViewId`, `this.nativeTab`

## Tab.convertFromSessionStoreClosedData()
- 位置: L942-983
- 役割: 閉じたタブのセッションデータを拡張の Tab の形式に変換する。URL、タイトル、ファビコンは tabs 権限かホスト権限があるときだけ入れる。
- 触るとき: sessions API で閉じたタブの情報が返る形や、権限による隠し方を変えるとき。
- 呼び出し先: `Boolean()`, `String()`, `windowTracker.getId()`
- 条件付き依存: `if (entries.length)` → `extension.hasPermission()`
- 条件付き依存: `if (entries.length)` → `extension.allowedOrigins.matches()`
- 参照: `entries.length`, `entry.title`, `entry.url`, `result.favIconUrl`, `result.title`, `result.url`, `tabData.closedId`, `tabData.entries`, `tabData.hidden`, `tabData.image`, `tabData.index`, `tabData.lastAccessed`, `tabData.pos`, `tabData.state`, `tabData.state.entries`, `tabData.state.hidden`, `tabData.state.index`, `tabData.state.isPrivate`, `tabData.state.lastAccessed`

## Window.updateGeometry()
- 位置: L1003-1018
- 役割: left と top が指定されていれば moveTo、width と height が指定されていれば resizeTo で、指定されていない値は現在値を使って位置とサイズを変える。
- 触るとき: windows.update で位置や大きさが意図どおり変わらないときに調べる。
- 条件付き依存: `if (options.left !== null || options.top !== null)` → `window.moveTo()`
- 条件付き依存: `if (options.width !== null || options.height !== null)` → `window.resizeTo()`
- 参照: `options.height`, `options.left`, `options.top`, `options.width`, `window.outerHeight`, `window.outerWidth`, `window.screenX`, `window.screenY`

## Window._title()
- 位置: L1020-1022
- 役割: ウィンドウの document の title を返す。
- 触るとき: ウィンドウの表示タイトルを取得する箇所を調べるとき。
- 参照: `this.window.document.title`

## Window.setTitlePreface()
- 位置: L1024-1029
- 役割: documentElement の titlepreface 属性に値を設定し、タイトルの前置きを変える。
- 触るとき: 拡張がウィンドウタイトルに前置きを付ける仕組みを変えるとき。
- 呼び出し先: `this.window.document.documentElement.setAttribute()`

## Window.focused()
- 位置: L1031-1033
- 役割: ウィンドウの document がフォーカスを持つかを返す。
- 触るとき: windows.getCurrent などの focused の値を調べるとき。
- 呼び出し先: `this.window.document.hasFocus()`

## Window.top()
- 位置: L1035-1037
- 役割: ウィンドウの画面上の上端 (screenY) を返す。
- 触るとき: windows の top の値を調べるとき。
- 参照: `this.window.screenY`

## Window.left()
- 位置: L1039-1041
- 役割: ウィンドウの画面上の左端 (screenX) を返す。
- 触るとき: windows の left の値を調べるとき。
- 参照: `this.window.screenX`

## Window.width()
- 位置: L1043-1045
- 役割: ウィンドウの外側の幅 (outerWidth) を返す。
- 触るとき: windows の width の値を調べるとき。
- 参照: `this.window.outerWidth`

## Window.height()
- 位置: L1047-1049
- 役割: ウィンドウの外側の高さ (outerHeight) を返す。
- 触るとき: windows の height の値を調べるとき。
- 参照: `this.window.outerHeight`

## Window.incognito()
- 位置: L1051-1053
- 役割: ウィンドウがプライベートブラウジングかを返す。
- 触るとき: windows の incognito の判定を調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `this.window`

## Window.alwaysOnTop()
- 位置: L1055-1058
- 役割: 常に false を返す。ブラウザウィンドウは常に最前面にはならないため。
- 触るとき: alwaysOnTop を対応させる要望を検討するとき。

## Window.isLastFocused()
- 位置: L1060-1062
- 役割: このウィンドウが最前面のウィンドウかを返す。
- 触るとき: windows.getLastFocused の判定を調べるとき。
- 参照: `this.window`, `windowTracker.topWindow`

## Window.getState()
- 位置: L1064-1072
- 役割: window.windowState の数値を maximized、minimized、fullscreen、normal の文字列に変換する。
- 触るとき: windows の state の表記を変えるとき。
- 参照: `window.STATE_FULLSCREEN`, `window.STATE_MAXIMIZED`, `window.STATE_MINIMIZED`, `window.STATE_NORMAL`, `window.windowState`

## Window.state()
- 位置: L1074-1076
- 役割: 現在の状態を文字列にして返す。
- 触るとき: windows の state の値を調べるとき。
- 呼び出し先: `Window.getState()`
- 参照: `this.window`

## Window.setState()
- 位置: async L1078-1191
- 役割: 指定の状態へ変え、サイズモードとサイズの変化を待つ。変化が来なければ 2 秒で打ち切る。docked は minimized と同じ扱い。不正な状態なら例外を投げる。
- 触るとき: windows.update の state 変更が完了しない、または遅いときに調べる。
- 呼び出し先: `window.maximize()`, `window.minimize()`, `window.removeEventListener()`, `window.restore()`
- 条件付き依存: `if (resizeExpected)` → `window.addEventListener()`
- 条件付き依存: `if (window.windowState !== window.STATE_NORMAL)` → `window.restore()`
- 条件付き依存: `if (window.windowState != expectedState)` → `window.addEventListener()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `Promise.any()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `Promise.all()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `setTimeout()`
- 条件付き依存: `if (promiseExpectedSizeMode || promiseResize)` → `window.removeEventListener()`
- 参照: `window.STATE_FULLSCREEN`, `window.STATE_MAXIMIZED`, `window.STATE_MINIMIZED`, `window.STATE_NORMAL`, `window.fullScreen`, `window.windowState`

## onSizeModeChange()
- 位置: L1171-1175
- 役割: サイズモードが期待の状態になったら、待機の Promise を解決する。
- 触るとき: 状態変更の完了待ちが終わらないときに調べる。
- 条件付き依存: `if (window.windowState == expectedState)` → `resolve()`
- 参照: `window.windowState`

## Window.getTabs()
- 位置: L1193-1209
- 役割: ウィンドウのタブを 1 つずつラッパーにして返す。タブの採用中は何も返さない。
- 触るとき: windows.get の populate で返すタブ一覧を変えるとき。
- 呼び出し先: `tabManager.getWrapper()`, `this.window.gBrowserInit.isAdoptingTab()`
- 参照: `this.extension`, `this.window.gBrowser.tabs`

## Window.getHighlightedTabs()
- 位置: L1211-1219
- 役割: 選択中のタブ（複数選択を含む）をラッパーにして返す。
- 触るとき: highlighted の対象範囲を調べるとき。
- 呼び出し先: `tabManager.getWrapper()`
- 参照: `this.extension`, `this.window.gBrowser.selectedTabs`

## Window.activeTab()
- 位置: L1221-1232
- 役割: 選択中のタブのラッパーを返す。採用中のウィンドウでは null を返す。
- 触るとき: windows の active tab の取得を調べるとき。
- 呼び出し先: `tabManager.getWrapper()`, `this.window.gBrowserInit.isAdoptingTab()`
- 参照: `this.extension`, `this.window.gBrowser.selectedTab`

## Window.getTabAtIndex()
- 位置: L1234-1239
- 役割: 指定位置のタブのラッパーを返す。タブが無ければ undefined を返す。
- 触るとき: タブ位置の指定が範囲外のときの動作を調べるとき。
- 条件付き依存: `if (nativeTab)` → `this.extension.tabManager.getWrapper()`
- 参照: `this.window.gBrowser.tabs`

## Window.convertFromSessionStoreClosedData()
- 位置: L1254-1273
- 役割: 閉じたウィンドウのセッションデータを拡張の Window の形式に変換する。タブがあれば各タブを変換する。
- 触るとき: sessions API で閉じたウィンドウの情報の形を変えるとき。
- 呼び出し先: `String()`
- 条件付き依存: `if (windowData.tabs.length)` → `windowData.tabs.map()`
- 条件付き依存: `if (windowData.tabs.length)` → `Tab.convertFromSessionStoreClosedData()`
- 参照: `result.tabs`, `windowData.closedId`, `windowData.tabs.length`

## TabManager.get()
- 位置: L1279-1289
- 役割: タブ ID から native タブを引き、アクセスできなければ Invalid tab ID を投げ、できればラッパーを返す。
- 触るとき: ユーザーの隔離やプライベートの制限で tabs API が失敗する条件を調べるとき。
- 呼び出し先: `tabTracker.getTab()`
- 条件付き依存: `if (nativeTab)` → `this.canAccessTab()`
- 条件付き依存: `if (nativeTab)` → `this.getWrapper()`

## TabManager.addActiveTabPermission()
- 位置: L1291-1293
- 役割: 既定では最前面のタブに activeTab の権限を付ける。
- 触るとき: activeTab 権限の付与対象を変えるとき。
- 呼び出し先: `super.addActiveTabPermission()`
- 参照: `tabTracker.activeTab`

## TabManager.revokeActiveTabPermission()
- 位置: L1295-1297
- 役割: 既定では最前面のタブから activeTab の権限を外す。
- 触るとき: activeTab 権限の解除対象を変えるとき。
- 呼び出し先: `super.revokeActiveTabPermission()`
- 参照: `tabTracker.activeTab`

## TabManager.canAccessTab()
- 位置: L1299-1311
- 役割: ウィンドウへのアクセスと、ユーザーコンテキストの隔離に基づいて、タブにアクセスできるかを判定する。
- 触るとき: プライベートやコンテナのタブが拡張から見えるかを変えるとき。
- 呼び出し先: `this.extension.canAccessContainer()`, `this.extension.canAccessWindow()`
- 参照: `nativeTab.documentGlobal`, `nativeTab.userContextId`, `this.extension.userContextIsolation`

## TabManager.wrapTab()
- 位置: L1313-1315
- 役割: native タブから Tab のラッパーを新しく作る。
- 触るとき: タブのラッパーが作られる経路を追うとき。
- 呼び出し先: `tabTracker.getId()`
- 参照: `this.extension`

## TabManager.getWrapper()
- 位置: L1317-1321
- 役割: 採用中のタブ以外について、基底のラッパーを返す。採用中なら undefined を返す。
- 触るとき: 採用中のタブが拡張に見えない理由を調べるとき。
- 呼び出し先: `nativeTab.documentGlobal.gBrowserInit.isAdoptingTab()`
- 条件付き依存: `if (!nativeTab.documentGlobal.gBrowserInit.isAdoptingTab())` → `super.getWrapper()`

## WindowManager.get()
- 位置: L1325-1329
- 役割: ウィンドウ ID からウィンドウを引き、ラッパーにして返す。
- 触るとき: windows.get の戻りや不存在時の扱いを調べるとき。
- 呼び出し先: `this.getWrapper()`, `windowTracker.getWindow()`

## WindowManager.getAll()
- 位置: L1331-1341
- 役割: アクセスできるブラウザウィンドウを 1 つずつラッパーにして返す。
- 触るとき: windows.getAll の対象範囲を変えるとき。
- 呼び出し先: `this.canAccessWindow()`, `this.getWrapper()`, `windowTracker.browserWindows()`

## WindowManager.wrapWindow()
- 位置: L1343-1345
- 役割: native ウィンドウから Window のラッパーを新しく作る。
- 触るとき: ウィンドウのラッパーが作られる経路を追うとき。
- 呼び出し先: `windowTracker.getId()`
- 参照: `this.extension`
