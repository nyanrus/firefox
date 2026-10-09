# browser/components/sessionstore/SessionStartup.sys.mjs

source: browser/components/sessionstore/SessionStartup.sys.mjs
source-hash: 85c725f7eb8d0f88f8f9fea31be3e1e0736852a8
lines: 507

## <module>
- 役割: 起動時にセッションファイルを読み、復元するかどうかと、その種類(なし、クラッシュ復旧、再開、保留)を決める。
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.withResolvers()`, `XPCOMUtils.declareLazy()`

## init()
- 位置: L87-138
- 役割: 起動時の初期化。復元前の設定を控え、セッションファイルを非同期に読み込んで _onSessionFileRead へ渡す。恒久的なプライベートブラウジングでは何もしない。
- 触るとき: 起動直後に復元がどの段階で始まるか、または OS 再起動後の再開設定をどう消すかを変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `lazy.SessionFile.read()`, `lazy.SessionFile.read().then()`, `lazy.sessionStoreLogger.debug()`, `lazy.sessionStoreLogger.error()`, `this._onSessionFileRead()`
- 条件付き依存: `if (!AppConstants.DEBUG)` → `lazy.StartupPerformance.init()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.permanentPrivateBrowsing)` → `gOnceInitializedDeferred.resolve()`
- 条件付き依存: `if (this._resumingAfterOsRestart)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (!Services.appinfo.restartedByOS)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this._resumingAfterOsRestart)` → `Services.prefs.setBoolPref()`
- 参照: `AppConstants.DEBUG`, `Services.appinfo.restartedByOS`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `result.origin`, `this._initialized`, `this._resumeSessionOnce`, `this._resumingAfterOsRestart`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.prefs`

## _createSupportsString()
- 位置: L141-147
- 役割: 文字列を nsISupportsString で包んで返す。
- 触るとき: sessionstore-state-read の通知にアドオンが渡す値の形式を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 参照: `Ci.nsISupportsString`, `string.data`
- XPCOM: [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`

## _recordSessionAvailability()
- 位置: L160-185
- 役割: 読み込んだ元ファイル、形式、各候補の状態、関連する設定を Glean に記録する。
- 触るとき: 起動時のセッション読み込みの計測項目を追加・変更するとき、または読み込みの失敗原因を統計で追うとき。
- 呼び出し先: `Glean.sessionRestore.startupSessionAvailability.record()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `lazy.sessionStoreLogger.debug()`
- 参照: `Services.appinfo.restartedByOS`, `fileStates.clean`, `fileStates.cleanBackup`, `fileStates.recovery`, `fileStates.recoveryBackup`, `fileStates.upgradeBackup`, `this._resumeSessionOnce`, `this._resumingAfterOsRestart`
- XPCOM: `Services.appinfo` / `Services.prefs`

## _onSessionFileRead()
- 位置: L193-349
- 役割: 読み込み結果を受け取り、アドオンによる書き換えを反映し、クラッシュの有無と復元の種類を確定させる。
- 触るとき: 起動時に復元されるか、クラッシュ扱いになるかの判定を変えるとき。判定は CrashMonitor の終了時チェックポイントを優先し、無ければ session.state の値で判断する。
- 呼び出し先: `Glean.sessionRestore.shutdownOk[ this._previousSessionCrashed ? "false" : "true" ].add()`, `Glean.sessionRestore.shutdownSuccessSessionStartup.record()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.tm.idleDispatchToMainThread()`, `gOnceInitializedDeferred.resolve()`, `initialState.windows.reduce()`, `lazy.BrowserUsageTelemetry.updateMaxTabPinnedCount()`, `lazy.CrashMonitor.previousCheckpoints.then()`, `lazy.sessionStoreLogger.debug()`, `this._createSupportsString()`, `this._previousSessionCrashed.toString()`, `this._recordSessionAvailability()`, `this.isAutomaticRestoreEnabled()`, `win.tabs.reduce()`
- 条件付き依存: `if (stateString != source)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (stateString != source)` → `JSON.parse()`
- 条件付き依存: `if (stateString != source)` → `lazy.sessionStoreLogger.error()`
- 条件付き依存: `if (this._initialState == null)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (this._initialState == null)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (this._initialState == null)` → `gOnceInitializedDeferred.resolve()`
- 条件付き依存: `if (!isAutomaticRestoreEnabled && this._initialState)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (this.sessionType == this.NO_SESSION)` → `lazy.sessionStoreLogger.debug()`
- 条件付き依存: `if (!(this.sessionType == this.NO_SESSION))` → `Services.obs.addObserver()`
- 参照: `Glean.sessionRestore.shutdownOk`, `crashReasons.FINAL_STATE_WRITING_INCOMPLETE`, `crashReasons.SESSION_STATE_FLAG_MISSING`, `initialState.savedGroups.length`, `supportsStateString.data`, `tab.pinned`, `this.NO_SESSION`, `this._initialState`, `this._initialState.lastSessionState`, `this._initialState.session`, `this._initialState.session.state`, `this._initialized`, `this._previousSessionCrashed`, `this._sessionType`, `this.sessionType`
- XPCOM: `Services.obs` / `Services.tm`

## observe()
- 位置: L354-369
- 役割: ウィンドウ復元完了で初期状態を解放して復元済みにし、履歴の消去通知で種類を NO_SESSION に戻す。
- 触るとき: 復元後にメモリの初期状態を残していないか、履歴の消去が起動時の種類をどう変えるかを確認するとき。
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.sessionStoreLogger.debug()`
- 参照: `this.NO_SESSION`, `this._didRestore`, `this._initialState`, `this._sessionType`
- XPCOM: `Services.obs`

## onceInitialized()
- 位置: L373-375
- 役割: 初期化の完了を表す Promise を返す。
- 触るとき: 初期化完了を待つ処理を追加するとき、または待ちの順序を調べるとき。
- 参照: `gOnceInitializedDeferred.promise`

## state()
- 位置: L380-382
- 役割: 起動時に復元する状態(初期状態)を返す。
- 触るとき: 起動時の状態を使う処理がどの時点で値を受け取るかを調べるとき。
- 参照: `this._initialState`

## isAutomaticRestoreEnabled()
- 位置: L392-404
- 役割: 今回の起動で自動的に復元するかを返す。クラッシュ時の復元は含まない。値は初回の呼び出しで決めて保持する。
- 触るとき: 再開の設定(resume_session_once や browser.startup.page が 3)の解釈を変えるとき。結果は初回に固定される点に注意する。
- 条件付き依存: `if (this._resumeSessionEnabled === null)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this._resumeSessionEnabled === null)` → `Services.prefs.getIntPref()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._resumeSessionEnabled`
- XPCOM: `Services.prefs`

## willRestore()
- 位置: L411-416
- 役割: 種類がクラッシュ復旧か再開のとき、復元が予定されているかを真で返す。
- 触るとき: 起動直後に復元の予定がある前提で動く処理を書くとき。
- 参照: `this.RECOVER_SESSION`, `this.RESUME_SESSION`, `this.sessionType`

## willRestoreAsCrashed()
- 位置: L424-426
- 役割: 復元がクラッシュ復旧として予定されているかを返す。
- 触るとき: クラッシュ後の復旧だけ違う表示や処理を出したいとき。
- 参照: `this.RECOVER_SESSION`, `this.sessionType`

## willOverrideHomepage()
- 位置: L436-465
- 役割: セッションの復元がホームページを置き換えるかを Promise で返す。復元の予定が無ければ即座に偽を返す。
- 触るとき: 起動時にホームページの読み込みを省くかどうかを変えるとき。ピン留めのタブだけのウィンドウは置き換えに数えない。
- 呼び出し先: `resolve()`, `this._initialState.windows.filter()`, `this.isAutomaticRestoreEnabled()`, `this.onceInitialized.then()`, `this.willRestore()`, `this.willRestoreAsCrashed()`, `w.tabs.some()`
- 参照: `t.pinned`, `this._didRestore`, `this._initialState`, `this._initialState.windows`, `w._maybeDontRestoreTabs`

## sessionType()
- 位置: L470-488
- 役割: 起動時のセッションの種類を一度だけ決めて返す。順に、再開、クラッシュ復旧、保留、なしの判定を行う。
- 触るとき: 起動時にどの種類の復元になるかの優先順位を変えるとき。
- 条件付き依存: `if (this._sessionType === null)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this._sessionType === null)` → `this.isAutomaticRestoreEnabled()`
- 参照: `this.DEFER_SESSION`, `this.NO_SESSION`, `this.RECOVER_SESSION`, `this.RESUME_SESSION`, `this._initialState`, `this._previousSessionCrashed`, `this._sessionType`
- XPCOM: `Services.prefs`

## previousSessionCrashed()
- 位置: L493-495
- 役割: 前回のセッションがクラッシュ扱いだったかを返す。
- 触るとき: クラッシュ後の通知や、クラッシュ復旧の判定結果を別の処理で使うとき。
- 参照: `this._previousSessionCrashed`

## resetForTest()
- 位置: L497-500
- 役割: 再開の有無と種類のキャッシュを消す。テスト専用。
- 触るとき: テストごとに起動時の判定をやり直したいとき。
- 参照: `this._resumeSessionEnabled`, `this._sessionType`
