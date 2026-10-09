# browser/components/sessionstore/SessionSaver.sys.mjs

source: browser/components/sessionstore/SessionSaver.sys.mjs
source-hash: 1b99e507311668ed2d0a8dd3a34554db513e596e
lines: 444

## <module>
- 役割: セッションの状態を収集し、遅延・即時・アイドル時に保存をスケジュールしてセッションファイルへ書き込む。
- 呼び出し先: `Cc["@mozilla.org/widget/useridleservice;1"].getService()`, `Object.freeze()`, `SessionSaverInternal.cancel()`, `SessionSaverInternal.runDelayed()`, `XPCOMUtils.declareLazy()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `idleService.addIdleObserver()`

## notify()
- 位置: L48-50
- 役割: オブザーバー通知を発行する小さな関数。
- 触るとき: 状態書き込み完了の通知名を変えるとき、その通知を受け取る側を探すとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## run()
- 位置: L59-64
- 役割: 現在の状態をすぐに保存する公開 API。実行中でないときはデバッグログを出してから保存する。
- 触るとき: 終了処理の途中で即時保存が呼ばれたときの動きを調べるとき。
- 呼び出し先: `SessionSaverInternal.run()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`

## runDelayed()
- 位置: L71-73
- 役割: 遅延保存を予約する公開 API。内部の runDelayed に委譲する。
- 触るとき: 保存の頻度や予約の扱いを外から変えるとき、呼び出し元を追うとき。
- 呼び出し先: `SessionSaverInternal.runDelayed()`

## lastSaveTime()
- 位置: L78-80
- 役割: 直近の保存試行時刻を返す getter。
- 触るとき: 保存の間隔計算に使う前回時刻が正しく更新されているかを確認するとき。
- 参照: `SessionSaverInternal._lastSaveTime`

## updateLastSaveTime()
- 位置: L86-88
- 役割: 保存時刻を現在時刻にする公開 API。次の遅延保存は、この時刻から設定の間隔を空ける。
- 触るとき: 保存のたびに間隔の基準がずれないかを調べるとき。
- 呼び出し先: `SessionSaverInternal.updateLastSaveTime()`

## cancel()
- 位置: L93-95
- 役割: 保留中の遅延保存と idle コールバックをすべて取り消す公開 API。
- 触るとき: 保存を一時的に止めたい処理や、予約を組み直す処理を追加するとき。
- 呼び出し先: `SessionSaverInternal.cancel()`

## run()
- 位置: L154-156
- 役割: すべてのウィンドウを強制的に再収集して保存する。
- 触るとき: キャッシュを使わずに状態を保存する即時保存の動作を変えるとき。
- 呼び出し先: `this._saveState()`

## runDelayed()
- 位置: L167-199
- 役割: 保存間隔を守って遅延保存を予約する。既に予約があれば何もしない。既定の遅延は 2000 ミリ秒。
- 触るとき: 保存が遅れる、または早まる挙動を変えるとき。アイドル時は browser.sessionstore.interval.idle、そうでなければ browser.sessionstore.interval の間隔を使い、前回保存からの経過時間を差し引く。
- 呼び出し先: `Date.now()`, `Math.max()`, `requestIdleCallback()`, `setTimeout()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`, `this._idleCallbackID`, `this._intervalWhileActive`, `this._intervalWhileIdle`, `this._isIdle`, `this._lastSaveTime`, `this._timeoutID`, `this._wasIdle`

## saveStateAsyncWhenIdle()
- 位置: L188-195
- 役割: 予約の満了後、ブラウザがアイドル時間になったところで非同期保存を呼ぶ。
- 触るとき: 保存をユーザー操作の邪魔にならない時間へ寄せる仕組みを変えるとき。
- 呼び出し先: `this._saveStateAsync()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`

## updateLastSaveTime()
- 位置: L205-207
- 役割: 内部の保存時刻を現在時刻にする。
- 触るとき: _writeState の前後で時刻を更新する意図(連続した書き込みを避けるため)を確認するとき。
- 呼び出し先: `Date.now()`
- 参照: `this._lastSaveTime`

## cancel()
- 位置: L212-217
- 役割: タイマーと idle コールバックを解除し、ID を null に戻す。
- 触るとき: 保留中の保存の取り消しに漏れがないかを確認するとき。
- 呼び出し先: `cancelIdleCallback()`, `clearTimeout()`
- 参照: `this._idleCallbackID`, `this._timeoutID`

## observe()
- 位置: L222-240
- 役割: アイドルと復帰の通知を受けて _isIdle を更新する。復帰時にアイドル中の予約があれば取り消して、通常の遅延保存で組み直す。
- 触るとき: アイドル時の保存間隔の扱いを変えるとき、または復帰直後の保存が遅れる問題を調べるとき。想定外の通知は例外にする。
- 条件付き依存: `if (this._timeoutID && this._wasIdle)` → `clearTimeout()`
- 条件付き依存: `if (this._timeoutID && this._wasIdle)` → `this.runDelayed()`
- 参照: `this._isIdle`, `this._timeoutID`, `this._wasIdle`

## _saveState()
- 位置: L249-309
- 役割: 予約を止めて状態を収集し、フィルタや保存対象外タブの除去、閉じたウィンドウの復元を行ってから書き込む中心の保存処理。
- 触るとき: 保存されるウィンドウやタブの範囲を変えるとき。恒久的なプライベートブラウジングでは何も保存しない。macOS では閉じたウィンドウの復元(_shouldRestore)を行わない点に注意する。
- 呼び出し先: `Glean.sessionRestore.collectData.start()`, `Glean.sessionRestore.collectData.stopAndAccumulate()`, `lazy.PrivacyFilter.filterPrivateWindowsAndTabs()`, `lazy.SessionStore.getCurrentState()`, `lazy.SessionStore.keepOnlyWorthSavingTabs()`, `this._maybeClearCookiesAndStorage()`, `this._writeState()`, `this.cancel()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `this.updateLastSaveTime()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `Promise.resolve()`
- 条件付き依存: `if (lazy.sessionStoreLogger.debugEnabled)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `state.windows.unshift()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `state._closedWindows.pop()`
- 参照: `AppConstants.platform`, `closedWin._shouldRestore`, `closedWin.closedAt`, `closedWin.closedId`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.sessionStoreLogger.debugEnabled`, `state._closedWindows`, `state._closedWindows.length`, `state._closedWindows[i]._shouldRestore`, `state.deferredInitialState`, `state.deferredInitialState.windows`, `state.windows`

## _maybeClearCookiesAndStorage()
- 位置: L315-342
- 役割: 終了時で、再開設定が無く、終了時の Cookie 削除が有効なら、状態から Cookie と DOM ストレージを取り除く。
- 触るとき: 終了時に Cookie やサイトストレージを残さない設定の動きを確認するとき。privacy.sanitize.sanitizeOnShutdown と privacy.clearOnShutdown.cookies の両方が真のときだけ消す。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.RunState.isClosing`, `state.cookies`, `state.windows`, `tab.storage`, `window.tabs`
- XPCOM: `Services.prefs`

## _saveStateAsync()
- 位置: L349-355
- 役割: アイドル時のコールバックから呼ばれ、予約を解除してから _saveState で保存する。
- 触るとき: 遅延保存の実行経路を変えるとき。
- 呼び出し先: `this._saveState()`
- 参照: `this._timeoutID`

## _writeState()
- 位置: L360-392
- 役割: 保存時刻を更新してから SessionFile.write で書き込み、成功時に時刻を更新して完了通知を出す。失敗はエラーログに残すだけ。
- 触るとき: 書き込み失敗時の挙動や、完了通知を受ける側の動きを変えるとき。
- 呼び出し先: `lazy.SessionFile.write()`, `lazy.SessionFile.write(state).then()`, `lazy.sessionStoreLogger.error()`, `notify()`, `this.updateLastSaveTime()`
- 条件付き依存: `if (!lazy.RunState.isRunning)` → `lazy.sessionStoreLogger.debug()`
- 参照: `lazy.RunState.isRunning`
