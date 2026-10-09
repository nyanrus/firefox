# browser/components/places/Interactions.sys.mjs

source: browser/components/places/Interactions.sys.mjs
source-hash: cf647ed30ec2c40aa10f3e372e4d603d3f251896
lines: 845

## <module>
- 役割: ページ滞在と操作(入力・スクロール)を集計して moz_places_metadata へ保存する、インタラクション記録の本体。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.now()`, `Promise.resolve()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `console.createInstance()`

## monotonicNow()
- 位置: L71-77
- 役割: 直前と同じミリ秒にならない単調増加の時刻を返す。
- 触るとき: interaction の created_at が衝突して保存の一意キーに影響する問題を調べるとき。
- 呼び出し先: `Date.now()`

## _Interactions.init()
- 位置: L185-218
- 役割: pref browser.places.interactions.enabled が真なら、ウィンドウアクターを登録し、既存ウィンドウの監視とアイドル監視を始める。
- 触るとき: 機能の有効化条件や起動時の登録順を変えるとき、既存ウィンドウで記録が始まらない問題を調べるとき。
- 呼び出し先: `ChromeUtils.registerWindowActor()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.wm.getMostRecentBrowserWindow()`, `lazy.idleService.addIdleObserver()`
- 条件付き依存: `if (!win.closed)` → `this.#registerWindow()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `lazy.pageViewIdleTime`, `this.#activeWindow`, `this.#initialized`, `win.closed`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.wm`

## _Interactions.uninit()
- 位置: L223-227
- 役割: 初期化済みならアイドル監視だけを外す。
- 触るとき: 終了時にアイドル監視が残る問題を調べるとき。
- 条件付き依存: `if (this.#initialized)` → `lazy.idleService.removeIdleObserver()`
- 参照: `lazy.pageViewIdleTime`, `this.#initialized`

## _Interactions.reset()
- 位置: async L233-241
- 役割: テスト用に記録中の状態を初期化し、保留中の更新を待ってから store を消去する。
- 触るとき: テストの前後で前回の記録が残る問題を調べるとき。
- 呼び出し先: `ChromeUtils.consumeInteractionData()`, `ChromeUtils.now()`, `lazy.logConsole.debug()`, `this.store.reset()`
- 参照: `_Interactions.interactionUpdatePromise`, `this.#interactions`, `this.#userIsIdle`, `this._pageViewStartTime`

## _Interactions.store()
- 位置: L250-255
- 役割: InteractionsStore を初回アクセス時に生成して返す。テスト用の参照口。
- 触るとき: 保存内容をテストから確認する箇所を変えるとき、本番コードから store を直接触っていないかを見るとき。
- 参照: `this.#store`

## _Interactions.registerNewInteraction()
- 位置: L265-313
- 役割: 履歴が有効で global history を使うブラウザーについて、ブロックリストに載らない URL の新しい interaction を作り、記録中と直近の一覧に加える。
- 触るとき: ページ遷移の開始時にどの interaction を閉じるかを変えるとき、除外すべき URL が記録される、または記録されない問題を調べるとき。
- 呼び出し先: `lazy.InteractionsBlocklist.isUrlBlocklisted()`, `lazy.logConsole.debug()`, `monotonicNow()`, `this.#interactions.get()`, `this.#interactions.set()`, `this.#pruneOldRecentInteractions()`, `this.#recentInteractions.get()`, `this.#recentInteractions.set()`
- 条件付き依存: `if (interaction && interaction.url != docInfo.url)` → `this.registerEndOfInteraction()`
- 条件付き依存: `if (lazy.InteractionsBlocklist.isUrlBlocklisted(docInfo.url))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (docInfo.isActive && browser.documentGlobal == this.#activeWindow)` → `ChromeUtils.now()`
- 参照: `browser.browsingContext.useGlobalHistory`, `browser.documentGlobal`, `docInfo.isActive`, `docInfo.referrer`, `docInfo.url`, `interaction.url`, `lazy.isHistoryEnabled`, `this.#activeWindow`, `this._pageViewStartTime`

## _Interactions.registerEndOfInteraction()
- 位置: L323-340
- 役割: 履歴が有効なとき #updateInteraction で最終値を保存し、そのブラウザーの記録中 interaction を消す。
- 触るとき: ページを離れたときに値が保存されない、または離脱後も記録が残る問題を調べるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `this.#interactions.delete()`, `this.#updateInteraction()`
- 参照: `browser.browsingContext.useGlobalHistory`, `lazy.isHistoryEnabled`

## _Interactions.#updateInteraction()
- 位置: L350-359
- 役割: 現在のアクティブウィンドウや状態を添えて #updateInteraction_async を起動する。
- 触るとき: 滞在時間の集計を呼ぶ箇所を増やすとき、ウィンドウ切替やアイドル時に保存されるタイミングを調べるとき。
- 呼び出し先: `_Interactions.#updateInteraction_async()`
- 参照: `this.#activeWindow`, `this.#interactions`, `this.#userIsIdle`, `this._pageViewStartTime`, `this.store`

## _Interactions.getRecentInteractionsForBrowser()
- 位置: async L367-373
- 役割: 滞在時間を先に更新して保存完了を待ち、そのブラウザーの直近 interaction の一覧を返す。
- 触るとき: 直近の滞在情報を読む呼び出し側を変えるとき、返る値が古く見える問題を調べるとき。
- 呼び出し先: `this.#recentInteractions.get()`, `this.#updateInteraction()`
- 参照: `_Interactions.interactionUpdatePromise`

## _Interactions.#pruneOldRecentInteractions()
- 位置: L382-401
- 役割: updated_at が 60 秒より前の直近 interaction を取り除き、残りが無ければブラウザーの登録も消す。
- 触るとき: 直近一覧の保持期間を変えるとき、古い interaction がいつ消えるかを調べるとき。
- 呼び出し先: `Date.now()`, `interactions.filter()`, `this.#recentInteractions.get()`
- 条件付き依存: `if (interactionstoTrack.length)` → `this.#recentInteractions.set()`
- 条件付き依存: `if (!(interactionstoTrack.length))` → `this.#recentInteractions.delete()`
- 参照: `interaction.updated_at`, `interactionstoTrack.length`

## _Interactions.interactionUpdatePromise()
- 位置: L414-416
- 役割: 保存更新の保留中 Promise を返す。テストが保存完了を待つための口。
- 触るとき: テストで非同期の保存を待つ箇所を書くとき、保存更新の連鎖を追うとき。
- 参照: `_Interactions.interactionUpdatePromise`

## _Interactions.#updateInteraction_async()
- 位置: async L434-497
- 役割: アクティブウィンドウ内の対象ブラウザーについて、滞在時間とキー入力を積算し、スクロール集計の完了後に store へ追加する。アイドル中や対象外のウィンドウでは何もしない。
- 触るとき: 滞在時間・キー入力・スクロール量の計算を変えるとき、アイドル中や非アクティブ時に集計されない理由を調べるとき。
- 呼び出し先: `ChromeUtils.collectScrollingData()`, `ChromeUtils.consumeInteractionData()`, `ChromeUtils.now()`, `_Interactions.interactionUpdatePromise .then()`, `_Interactions.interactionUpdatePromise .then(async () => ChromeUtils.collectScrollingData()) .then()`, `console.error()`, `interactions.get()`, `lazy.logConsole.debug()`, `monotonicNow()`, `store.add()`
- 条件付き依存: `if (!activeWindow || (browser && browser.documentGlobal != activeWindow))` → `lazy.logConsole.debug()`
- 条件付き依存: `if (userIsIdle)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!interaction)` → `lazy.logConsole.debug()`
- 参照: `Interactions._pageViewStartTime`, `_Interactions.interactionUpdatePromise`, `activeWindow.gBrowser.selectedTab.linkedBrowser`, `browser.documentGlobal`, `interaction.keypresses`, `interaction.scrollingDistance`, `interaction.scrollingTime`, `interaction.totalViewTime`, `interaction.typingTime`, `interaction.updated_at`, `interactionData.Typing`, `result.interactionTimeInMilliseconds`, `result.scrollingDistanceInPixels`, `typing.interactionCount`, `typing.interactionTimeInMilliseconds`

## _Interactions.#onActivateWindow()
- 位置: L505-514
- 役割: プライベートでなければアクティブウィンドウを記録し、滞在時間の起点を現在にする。
- 触るとき: ウィンドウを切り替えた直後の滞在時間が二重に数えられる問題を調べるとき。
- 呼び出し先: `ChromeUtils.now()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.logConsole.debug()`
- 参照: `this.#activeWindow`, `this._pageViewStartTime`

## _Interactions.#onDeactivateWindow()
- 位置: L519-524
- 役割: 現在の interaction を保存してから、アクティブウィンドウの記録を外す。
- 触るとき: 別のアプリへフォーカスが移ったときに保存が漏れる問題を調べるとき。
- 呼び出し先: `lazy.logConsole.debug()`, `this.#updateInteraction()`
- 参照: `this.#activeWindow`

## _Interactions.#onTabSelect()
- 位置: L538-559
- 役割: 前のタブの滞在時間を保存し、選んだタブの最終更新から breakupIfNoUpdatesForSeconds(既定 3600 秒)以上経っていれば interaction を終えて新しく始める。
- 触るとき: タブ切替で interaction を分けるしきい値を変えるとき、長く開いたままのタブの記録が一つにまとまる理由を調べるとき。
- 呼び出し先: `ChromeUtils.now()`, `lazy.logConsole.debug()`, `this.#interactions.has()`, `this.#updateInteraction()`
- 条件付き依存: `if (browser && this.#interactions.has(browser))` → `this.#interactions.get()`
- 条件付き依存: `if (browser && this.#interactions.has(browser))` → `Date.now()`
- 条件付き依存: `if (timePassedSinceUpdateSeconds >= lazy.breakupIfNoUpdatesForSeconds)` → `this.registerEndOfInteraction()`
- 条件付き依存: `if (timePassedSinceUpdateSeconds >= lazy.breakupIfNoUpdatesForSeconds)` → `this.registerNewInteraction()`
- 参照: `browser.currentURI.spec`, `interaction.updated_at`, `lazy.breakupIfNoUpdatesForSeconds`, `this.#activeWindow?.gBrowser.selectedBrowser`, `this._pageViewStartTime`

## _Interactions.handleEvent()
- 位置: L567-582
- 役割: TabSelect、activate、deactivate、unload をそれぞれの処理へ振り分ける。
- 触るとき: 記録の対象にするウィンドウイベントを増やすとき。
- 呼び出し先: `this.#onActivateWindow()`, `this.#onDeactivateWindow()`, `this.#onTabSelect()`, `this.#unregisterWindow()`
- 参照: `event.detail.previousTab.linkedBrowser`, `event.target`, `event.type`

## _Interactions.observe()
- 位置: L592-610
- 役割: 新規ウィンドウ、idle、active の通知を処理する。idle では滞在時間を保存して、以後の集計を止める。
- 触るとき: アイドル判定の扱いを変えるとき、スリープ復帰後に滞在時間が再開しない問題を調べるとき。
- 呼び出し先: `ChromeUtils.now()`, `lazy.logConsole.debug()`, `this.#onWindowOpen()`, `this.#updateInteraction()`
- 参照: `this.#userIsIdle`, `this._pageViewStartTime`

## _Interactions.#registerWindow()
- 位置: L618-626
- 役割: プライベートでなければ TabSelect、activate、deactivate をキャプチャ段階で監視する。
- 触るとき: 記録対象のウィンドウイベントを増減するとき、どのウィンドウが監視されているかを確認するとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.addEventListener()`

## _Interactions.#unregisterWindow()
- 位置: L634-638
- 役割: #registerWindow で付けた3つのイベントリスナーを外す。
- 触るとき: ウィンドウを閉じた後にリスナーが残る問題を調べるとき。
- 呼び出し先: `win.removeEventListener()`

## _Interactions.#onWindowOpen()
- 位置: L647-661
- 役割: 開かれたウィンドウの load を待ち、windowtype が navigator:browser のものだけ登録する。
- 触るとき: 新しく開いたブラウザーウィンドウで記録が始まらない問題を調べるとき。
- 呼び出し先: `this.#registerWindow()`, `win.addEventListener()`, `win.document.documentElement.getAttribute()`

## InteractionsStore.constructor()
- 位置: L698-709
- 役割: 終了時に flush を待つシャットダウンブロッカーを登録し、保留書き込みの Promise を初期化する。
- 触るとき: 終了時に最後の書き込みが失われる問題を調べるとき、シャットダウンの順序を変えるとき。
- 呼び出し先: `Promise.resolve()`, `lazy.PlacesUtils.history.shutdownClient.jsclient.addBlocker()`, `this.flush()`
- 参照: `this.pendingPromise`, `this.progress`

## fetchState()
- 位置: L704-704
- 役割: シャットダウンブロッカーの進行状況として progress オブジェクトを返す。
- 触るとき: 終了時に保存の待ち状態を確認するとき。
- 参照: `this.progress`

## InteractionsStore.flush()
- 位置: async L716-722
- 役割: 動いている保存タイマーを止め、保留分を直ちにデータベースへ書き込む。
- 触るとき: 終了前や、テストで保存を確実に完了させたいときに使う。
- 条件付き依存: `if (this.#timer)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this.#timer)` → `this.#timerResolve()`
- 条件付き依存: `if (this.#timer)` → `this.#updateDatabase()`
- 参照: `this.#timer`

## InteractionsStore.reset()
- 位置: async L728-741
- 役割: moz_places_metadata を全削除し、保留中のバッファとタイマーを破棄する。
- 触るとき: テストで滞在データを消すとき、リセット後に古い書き込みが残る問題を調べるとき。
- 呼び出し先: `db.executeCached()`, `lazy.PlacesUtils.withConnectionWrapper()`
- 条件付き依存: `if (this.#timer)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this.#timer)` → `this.#timerResolve()`
- 条件付き依存: `if (this.#timer)` → `this.#interactions.clear()`
- 参照: `this.#timer`

## InteractionsStore.add()
- 位置: L751-770
- 役割: URL と created_at をキーに保留バッファへ積み、タイマーが無ければ saveInterval(既定 10000 ms)後の書き込みを予約する。
- 触るとき: 保存の頻度や同じ interaction の重複排除を変えるとき、保存が遅れて見える問題を調べるとき。
- 呼び出し先: `interactionsForUrl.set()`, `lazy.logConsole.debug()`, `this.#interactions.get()`
- 条件付き依存: `if (!interactionsForUrl)` → `this.#interactions.set()`
- 条件付き依存: `if (!this.#timer)` → `lazy.setTimeout()`
- 条件付き依存: `if (!this.#timer)` → `this.#updateDatabase().catch(console.error).then()`
- 条件付き依存: `if (!this.#timer)` → `this.#updateDatabase().catch()`
- 条件付き依存: `if (!this.#timer)` → `this.#updateDatabase()`
- 条件付き依存: `if (!this.#timer)` → `this.pendingPromise.then()`
- 参照: `console.error`, `interaction.created_at`, `interaction.url`, `lazy.saveInterval`, `this.#timer`, `this.#timerResolve`, `this.pendingPromise`

## InteractionsStore.#updateDatabase()
- 位置: async L772-843
- 役割: 保留分を一つの INSERT OR REPLACE にまとめて moz_places_metadata へ書き、places-metadata-updated を通知する。place_id が無い行は挿入しない。
- 触るとき: 保存する列や参照先(referrer の place)を変えるとき、ページ削除後の行がどう扱われるかを確認するとき。
- 呼び出し先: `Math.round()`, `SQLInsertFragments.join()`, `SQLInsertFragments.push()`, `Services.obs.notifyObservers()`, `db.executeCached()`, `interactions.values()`, `interactionsForUrl.values()`, `lazy.PlacesUtils.withConnectionWrapper()`, `lazy.logConsole.debug()`
- 参照: `Interactions.DOCUMENT_TYPE.GENERIC`, `interaction.created_at`, `interaction.documentType`, `interaction.keypresses`, `interaction.referrer`, `interaction.scrollingDistance`, `interaction.scrollingTime`, `interaction.totalViewTime`, `interaction.typingTime`, `interaction.updated_at`, `interaction.url`, `interactions.size`, `this.#interactions`, `this.#timer`, `this.progress.pendingUpdates`
- XPCOM: `Services.obs`
