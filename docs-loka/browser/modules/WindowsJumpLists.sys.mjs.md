# browser/modules/WindowsJumpLists.sys.mjs

source: browser/modules/WindowsJumpLists.sys.mjs
source-hash: 5ddca6c37763b5261cceb156fded5f37035e218a
lines: 579

## <module>
- 役割: Windows のタスクバーのジャンプリスト(タスク、よく使うサイト、最近使ったサイト)を作成・更新し、設定や終了に応じて止める。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.prefs.getBoolPref()`, `Services.prefs.getBranch()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyServiceGetter()`, `console.createInstance()`

## _getString()
- 位置: L70-72
- 役割: taskbar.properties から名前を指定して文字列を読む。
- 触るとき: ジャンプリストの表示文言の取得先を変えるとき、文言が出ない問題を調べるとき。
- 呼び出し先: `lazy._stringBundle.GetStringFromName()`

## title()
- 位置: L90-92
- 役割: 新しいタブのタスクの表示名を taskbar.tasks.newTab.label から返す。
- 触るとき: 新しいタブのタスクの表示名を変えるとき。
- 呼び出し先: `_getString()`

## description()
- 位置: L93-95
- 役割: 新しいタブのタスクのツールチップを taskbar.tasks.newTab.description から返す。
- 触るとき: 新しいタブのタスクの説明文を変えるとき。
- 呼び出し先: `_getString()`

## title()
- 位置: L106-108
- 役割: 新しいウィンドウのタスクの表示名を taskbar.tasks.newWindow.label から返す。
- 触るとき: 新しいウィンドウのタスクの表示名を変えるとき。
- 呼び出し先: `_getString()`

## description()
- 位置: L109-111
- 役割: 新しいウィンドウのタスクのツールチップを taskbar.tasks.newWindow.description から返す。
- 触るとき: 新しいウィンドウのタスクの説明文を変えるとき。
- 呼び出し先: `_getString()`

## title()
- 位置: L122-124
- 役割: 新しいプライベートウィンドウのタスクの表示名を返す。
- 触るとき: プライベートウィンドウのタスクの表示名を変えるとき。
- 呼び出し先: `_getString()`

## description()
- 位置: L125-127
- 役割: 新しいプライベートウィンドウのタスクのツールチップを返す。
- 触るとき: プライベートウィンドウのタスクの説明文を変えるとき。
- 呼び出し先: `_getString()`

## constructor()
- 位置: L138-149
- 役割: ジャンプリストの作成器を受け取り、設定値の初期値を全て無効にして初期化する。
- 触るとき: 設定が読まれるまでの既定の状態を変えるとき。
- 参照: `this._builder`, `this._isBuilding`, `this._maxItemCount`, `this._showFrequent`, `this._showRecent`, `this._showTasks`, `this._shuttingDown`, `this._tasks`

## refreshPrefs()
- 位置: L151-156
- 役割: タスク・よく使うサイト・最近使ったサイトの表示有無と件数の値を保持する。
- 触るとき: ジャンプリストに表示する項目を決める設定の扱いを変えるとき。
- 参照: `this._maxItemCount`, `this._showFrequent`, `this._showRecent`, `this._showTasks`

## updateShutdownState()
- 位置: L158-160
- 役割: 終了処理中かどうかの状態を更新する。
- 触るとき: 終了中にジャンプリストを作り直さないための判定を変えるとき。
- 参照: `this._shuttingDown`

## delete()
- 位置: L162-164
- 役割: 作成器の参照を捨てる。
- 触るとき: 終了時に作成器を解放する処理を変えるとき。
- 参照: `this._builder`

## buildList()
- 位置: async L176-291
- 役割: タスクと履歴の項目を組み立て、履歴から削除された URL を消してから作成器に渡す。構築中または終了中なら何もしない。
- 触るとき: ジャンプリストの中身や、構築が止まる条件を変えるとき、項目が古いまま残る問題を調べるとき。
- 呼び出し先: `Services.dirsvc.get()`, `console.error()`, `this._builder.checkForRemovals()`
- 条件付き依存: `if (!(this._builder instanceof Ci.nsIJumpListBuilder))` → `console.error()`
- 条件付き依存: `if (!this._showRecent)` → `this._clearRecentsList()`
- 条件付き依存: `if (!this._showFrequent && !this._showTasks)` → `this._deleteActiveJumpList()`
- 条件付き依存: `if (removedURLs.length)` → `this._clearHistory()`
- 条件付き依存: `if (this._showTasks)` → `this._tasks.map()`
- 条件付き依存: `if (this._showFrequent)` → `lazy.PlacesUtils.promiseDBConnection()`
- 条件付き依存: `if (this._showFrequent)` → `conn.executeCached()`
- 条件付き依存: `if (this._showFrequent)` → `Services.io.newURI()`
- 条件付き依存: `if (this._showFrequent)` → `row.getResultByName()`
- 条件付き依存: `if (this._showFrequent)` → `this._builder.obtainAndCacheFaviconAsync()`
- 条件付き依存: `if (this._showFrequent)` → `lazy.logConsole.warn()`
- 条件付き依存: `if (this._showFrequent)` → `customDescriptions.push()`
- 条件付き依存: `if (this._showFrequent)` → `_getString()`
- 条件付き依存: `if (!this._shuttingDown)` → `this._builder.populateJumpList()`
- 参照: `Ci.nsIFile`, `Ci.nsIJumpListBuilder`, `Ci.nsINavHistoryService.TRANSITION_EMBED`, `Ci.nsINavHistoryService.TRANSITION_FRAMED_LINK`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).path`, `removedURLs.length`, `task.args`, `task.description`, `task.iconIndex`, `task.title`, `this._builder`, `this._isBuilding`, `this._maxItemCount`, `this._showFrequent`, `this._showRecent`, `this._showTasks`, `this._shuttingDown`, `uri.spec`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `nsIJumpListBuilder` / [`nsINavHistoryService`](../../toolkit/components/places/nsINavHistoryService.idl.md) / `Services.dirsvc` / `Services.io`

## _clearRecentsList()
- 位置: L293-295
- 役割: 作成器の最近使ったサイトの一覧を消す。
- 触るとき: 最近使ったサイトの表示を切ったときに一覧が残る問題を調べるとき。
- 呼び出し先: `this._builder.clearRecentsList()`

## _deleteActiveJumpList()
- 位置: L297-299
- 役割: 作成器のジャンプリストを消す。
- 触るとき: 項目を表示する設定がすべて無効になったときにリストを消す処理を変えるとき。
- 呼び出し先: `this._builder.clearJumpList()`

## _clearHistory()
- 位置: L317-326
- 役割: ジャンプリストから削除された URL を Places の履歴から消す。
- 触るとき: ジャンプリストの削除操作が履歴に反映されない問題を調べるとき。
- 呼び出し先: `Promise.resolve()`, `URL.parse()`, `uriSpecsToRemove .map()`, `uriSpecsToRemove .map(spec => URL.parse(spec)?.URI) .filter()`
- 条件付き依存: `if (URIsToRemove.length)` → `lazy.PlacesUtils.history.remove(URIsToRemove).catch()`
- 条件付き依存: `if (URIsToRemove.length)` → `lazy.PlacesUtils.history.remove()`
- 参照: `URIsToRemove.length`, `URL.parse(spec)?.URI`, `console.error`

## WTBJL_startup()
- 位置: async L344-372
- 役割: タスクバーが使えれば作成器を初期化し、プライベートブラウズが有効ならプライベートウィンドウのタスクを加え、設定、監視、更新タイマーを開始する。
- 触るとき: 起動時にジャンプリストが出ない問題や、起動時の初期化順を変えるとき。
- 呼び出し先: `this._initObs()`, `this._initTaskbar()`, `this._refreshPrefs()`, `this._updateTimer()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.enabled)` → `tasksCfg.push()`
- 条件付き依存: `if (this._blocked)` → `this._builder._deleteActiveJumpList()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `lazy._taskbarService.available`, `this._blocked`, `this._builder._tasks`, `this._pbBuilder._tasks`

## WTBJL_update()
- 位置: L374-393
- 役割: 有効でブロックされていなければ、通常のリストを構築し、プライベート用のリストは初回だけ構築する。
- 触るとき: ジャンプリストを更新する条件や、プライベート用リストを作る回数を変えるとき。
- 呼び出し先: `this._builder.buildList()`
- 条件付き依存: `if (!this._builtPb)` → `this._pbBuilder.buildList()`
- 参照: `this._blocked`, `this._builtPb`, `this._enabled`, `this._shuttingDown`

## WTBJL__shutdown()
- 位置: L395-400
- 役割: 両方の作成器を終了中の状態にしてから、監視・タイマー・作成器を解放する。
- 触るとき: 終了時の後始末を変えるとき。
- 呼び出し先: `this._builder.updateShutdownState()`, `this._free()`, `this._pbBuilder.updateShutdownState()`
- 参照: `this._shuttingDown`

## WTBJL__refreshPrefs()
- 位置: L406-419
- 役割: 有効設定と各種設定値を読み、通常の作成器に渡す。プライベート用には表示タスクだけを渡す。
- 触るとき: ジャンプリストの設定の読み方を変えるとき、プライベート用に表示される項目を変えるとき。
- 呼び出し先: `lazy._prefs.getBoolPref()`, `lazy._prefs.getIntPref()`, `this._builder.refreshPrefs()`, `this._pbBuilder.refreshPrefs()`
- 参照: `this._enabled`

## WTBJL__initTaskbar()
- 位置: async L425-446
- 役割: 通常用とプライベート用の作成器を作り、両方が使えるときだけ Builder を作って true を返す。
- 触るとき: タスクバー連携が使えない環境で何が起きるかを確認するとき。
- 呼び出し先: `Promise.all()`, `builder.isAvailable()`, `lazy._taskbarService.createJumpListBuilder()`, `pbBuilder.isAvailable()`
- 参照: `this._builder`, `this._pbBuilder`

## WTBJL__initObs()
- 位置: L448-462
- 役割: 終了、履歴の消去、設定変更を監視し、履歴の消去時には更新を依頼する。
- 触るとき: ジャンプリストを作り直すきっかけとなるイベントを増やす・減らすとき。
- 呼び出し先: `Services.obs.addObserver()`, `lazy.PlacesUtils.observers.addListener()`, `lazy._prefs.addObserver()`, `this.update.bind()`
- 参照: `this._placesObserver`
- XPCOM: `Services.obs`

## WTBJL__freeObs()
- 位置: L464-474
- 役割: WTBJL__initObs で登録した監視を全て外す。
- 触るとき: 終了処理で監視が残る問題を調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `lazy._prefs.removeObserver()`
- 条件付き依存: `if (this._placesObserver)` → `lazy.PlacesUtils.observers.removeListener()`
- 参照: `this._placesObserver`
- XPCOM: `Services.obs`

## WTBJL__updateTimer()
- 位置: L476-488
- 役割: 有効で終了中でなければ refreshInSeconds 間隔の繰り返しタイマーを作り、無効になればタイマーを止める。
- 触るとき: ジャンプリストの定期更新の間隔や条件を変えるとき。
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._timer)` → `Cc["@mozilla.org/timer;1"].createInstance()`
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._timer)` → `this._timer.initWithCallback()`
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._timer)` → `lazy._prefs.getIntPref()`
- 条件付き依存: `if ((!this._enabled || this._shuttingDown) && this._timer)` → `this._timer.cancel()`
- 参照: `Ci.nsITimer`, `this._enabled`, `this._shuttingDown`, `this._timer`, `this._timer.TYPE_REPEATING_SLACK`
- XPCOM: [`nsITimer`](../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## WTBJL__updateIdleObserver()
- 位置: L491-502
- 役割: 有効なら5分のアイドル監視を登録し、無効や終了時には外す。
- 触るとき: アイドル時に更新を止める仕組みを変えるとき。
- 条件付き依存: `if (this._enabled && !this._shuttingDown && !this._hasIdleObserver)` → `lazy._idle.addIdleObserver()`
- 条件付き依存: `if ( (!this._enabled || this._shuttingDown) && this._hasIdleObserver )` → `lazy._idle.removeIdleObserver()`
- 参照: `this._enabled`, `this._hasIdleObserver`, `this._shuttingDown`

## WTBJL__free()
- 位置: L504-510
- 役割: 監視、タイマー、アイドル監視を外し、作成器の参照を捨てる。
- 触るとき: 後始末の抜けで終了後も更新が続く問題を調べるとき。
- 呼び出し先: `this._builder.delete()`, `this._freeObs()`, `this._pbBuilder.delete()`, `this._updateIdleObserver()`, `this._updateTimer()`

## WTBJL_clearJumpList()
- 位置: async L520-530
- 役割: ジャンプリストの更新をブロックし、渡された Promise が終わるまで待ってから解除して更新を再開する。
- 触るとき: 事前案内モーダルの操作を待つ間はジャンプリストを更新しないようにする仕組みを変えるとき。
- 呼び出し先: `this._unblockJumpList()`
- 条件付き依存: `if (unblockPromise)` → `console.error()`
- 参照: `this._blocked`

## WTBJL_updateJumpList()
- 位置: L532-535
- 役割: ブロックを解除し、ジャンプリストを更新する。
- 触るとき: ブロック解除後にリストが更新されない問題を調べるとき。
- 呼び出し先: `this.update()`
- 参照: `this._blocked`

## WTBJL_notify()
- 位置: L537-543
- 役割: 更新タイマーの発火時に、アイドル監視を登録してから、アイドル時に更新を実行する。
- 触るとき: 定期更新のタイミングを変えるとき。
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `this._updateIdleObserver()`, `this.update()`
- XPCOM: `Services.tm`

## WTBJL_observe()
- 位置: L545-577
- 役割: 設定変更で有効が無効になったときは作成器のリストを消し、設定とタイマーを反映して更新する。終了時には _shutdown、履歴消去時には更新、アイドル時にはタイマーを止め、アクティブ時にはタイマーを再開する。
- 触るとき: 設定変更、終了、アイドルの各イベントで更新がどう変わるかを調べるとき。
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy._prefs.getBoolPref()`, `this._refreshPrefs()`, `this._shutdown()`, `this._updateIdleObserver()`, `this._updateTimer()`, `this.update()`
- 条件付き依存: `if (this._enabled && !lazy._prefs.getBoolPref(PREF_TASKBAR_ENABLED))` → `this._builder._deleteActiveJumpList()`
- 条件付き依存: `if (this._timer)` → `this._timer.cancel()`
- 参照: `this._enabled`, `this._timer`
- XPCOM: `Services.tm`
