# browser/components/sessionstore/SessionStore.sys.mjs

source: browser/components/sessionstore/SessionStore.sys.mjs
source-hash: 9fa4c8e8ccd31587442cec02e0563099dc65cd51
lines: 9611

## <module>
- 役割: ウィンドウ・タブ・タブグループの状態を追跡し、セッションをまたいで復元する SessionStore 本体。
- 呼び出し先: `ChromeUtils.generateQI()`, `Date.now()`, `Promise.withResolvers()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.declareLazy()`

## blankURI()
- 位置: L365-365
- 役割: about:blank の nsIURI を生成して返す。
- 触るとき: 復元や新規タブで空白ページの URI を作る箇所の挙動を変えるとき。
- 呼び出し先: `Services.io.newURI()`
- XPCOM: `Services.io`

## _SessionStore.resetNextClosedId()
- 位置: L402-404
- 役割: 閉じたタブ・ウィンドウに振る ID のカウンタを 0 に戻す(テスト専用)。
- 触るとき: テストで閉じたアイテムの ID を毎回同じ値から始めたいとき。本番コードからは使わない。
- 参照: `this.#nextClosedId`

## _SessionStore.getNextSplitViewId()
- 位置: L512-518
- 役割: 分割表示(split view)用の一意な整数 ID を払い出し、上限到達時は例外を投げる。
- 触るとき: 分割表示の ID 採番や、ID の再利用・移行処理を変えるとき。
- 参照: `Number.MAX_SAFE_INTEGER`, `this.#maxSplitViewId`

## _SessionStore.savedGroups()
- 位置: L530-532
- 役割: 保存済みおよび閉じたタブグループの状態配列 #savedGroups を返す getter。
- 触るとき: 保存済みタブグループの一覧を呼び出し側が参照する経路を調べるとき。
- 参照: `this.#savedGroups`

## _SessionStore.shouldRestoreLastSession()
- 位置: L556-558
- 役割: 次に通常ウィンドウが開いたときに前回セッションを復元すべきかを示すフラグを返す。
- 触るとき: タスクバータブが残ったままウィンドウを閉じた後に前回セッションを戻すか判定する処理を調べるとき。
- 参照: `this.#shouldRestoreLastSession`

## _SessionStore.#removeClosedAction()
- 位置: L586-594
- 役割: #lastClosedActions から、種別と closedId が一致する最初の要素を 1 件削除する。
- 触るとき: 閉じたタブやウィンドウを復元や忘却で取り除いたときに、直前に閉じた操作の記録を整合させる箇所を変えるとき。
- 呼び出し先: `this.#lastClosedActions.findIndex()`
- 条件付き依存: `if (closedActionIndex > -1)` → `this.#lastClosedActions.splice()`
- 参照: `obj.closedId`, `obj.type`

## _SessionStore.#addClosedAction()
- 位置: L604-614
- 役割: 閉じた操作を #lastClosedActions の末尾に追加し、上限(タブ数×ウィンドウ数)を超えた分を先頭から切り捨てる。
- 触るとき: 最近閉じた操作の履歴上限を変えたり、閉じた操作の記録タイミングを調べるとき。
- 呼び出し先: `this.#lastClosedActions.push()`
- 条件付き依存: `if (this.#lastClosedActions.length > maxLength)` → `this.#lastClosedActions.slice()`
- 参照: `this.#lastClosedActions`, `this.#lastClosedActions.length`, `this.#max_tabs_undo`, `this.#max_windows_undo`

## _SessionStore.lastClosedActions()
- 位置: L621-623
- 役割: 最近閉じた操作の配列のコピーを古い順で返す getter。
- 触るとき: 「閉じたタブを開き直す」の対象を決めるために履歴の並びを確認するとき。
- 参照: `this.#lastClosedActions`

## _SessionStore.popLastClosedAction()
- 位置: L633-635
- 役割: 最も新しい閉じた操作を配列から取り出して返す。
- 触るとき: 直前に閉じたタブやウィンドウを開き直す処理(restoreLastClosedTabOrWindowOrSession 相当)の動きを変えるとき。
- 呼び出し先: `this.#lastClosedActions.pop()`

## _SessionStore.resetLastClosedActions()
- 位置: L640-642
- 役割: 閉じた操作の履歴を空にする(テスト専用)。
- 触るとき: テストの前提状態として閉じた操作の履歴を消したいとき。
- 参照: `this.#lastClosedActions`

## _SessionStore.logger()
- 位置: L655-657
- 役割: SessionStoreLogger を返す getter。初期化前は null を返す。
- 触るとき: ログ出力先や初期化順序を確認するとき、初期化前にロガーを参照していないかを調べるとき。
- 参照: `this.#log`

## _SessionStore.promiseAllWindowsRestored()
- 位置: L684-686
- 役割: 全ウィンドウの復元完了を表す Promise を返す getter。
- 触るとき: 起動後の処理を全ウィンドウ復元の後に行わせたい呼び出し元の待ち合わせを追うとき。
- 参照: `this.#deferredAllWindowsRestored.promise`

## _SessionStore.promiseInitialized()
- 位置: L698-700
- 役割: SessionStore の初期化完了を表す Promise を返す getter。
- 触るとき: 初期化前に SessionStore を参照してしまう呼び出し元がないか確認するとき。
- 参照: `this.#deferredInitialized.promise`

## _SessionStore.canRestoreLastSession()
- 位置: L708-710
- 役割: 前回セッションが復元可能かを LastSession.canRestore から返す。
- 触るとき: 「前回のセッションを復元」を有効にするかどうかの判定元を調べるとき。
- 参照: `LastSession.canRestore`

## _SessionStore.canRestoreLastSession()
- 位置: L712-716
- 役割: false を代入すると LastSession を消去して前回セッションを破棄する。true の代入は何もしない。
- 触るとき: 前回セッションを明示的に捨てる呼び出し元を追うとき。
- 条件付き依存: `if (!val)` → `LastSession.clear()`

## _SessionStore.lastClosedObjectType()
- 位置: L723-743
- 役割: 閉じたウィンドウのほうが閉じたタブより新しければ "window"、そうでなければ "tab" を返す。
- 触るとき: sessions.restore WebExtensions API が返す直近に閉じた項目の種別を変えるとき、または判定の時刻比較を確認するとき。
- 条件付き依存: `if (this.#closedWindows.length)` → `Services.wm.getEnumerator()`
- 条件付き依存: `if (this.#closedWindows.length)` → `this.#windowIds.get()`
- 条件付き依存: `if (windowState && windowState._closedTabs[0])` → `tabTimestamps.push()`
- 条件付き依存: `if (this.#closedWindows.length)` → `tabTimestamps.sort()`
- 参照: `tabTimestamps.length`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[0].closedAt`, `this.#windows`, `this.LAST_ACTION_CLOSED_TAB`, `this.LAST_ACTION_CLOSED_WINDOW`, `windowState._closedTabs`, `windowState._closedTabs[0].closedAt`
- XPCOM: `Services.wm`

## _SessionStore.willAutoRestore()
- 位置: L749-756
- 役割: 次回起動時に前回セッションが自動復元されるかを、非永続プライベートブラウズで resume_session_once が立つか startup.page が RESUME_SESSION の場合に判定する。
- 触るとき: 次回起動時の自動復元条件を変えるとき、または起動ページ設定と resume_session_once の関係を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`
- 参照: `PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.prefs`

## _SessionStore.init()
- 位置: L761-779
- 役割: 起動時に一度だけ呼ばれ、必要な topic の Observer を登録し、設定を読み込む。二度目の呼び出しは例外になる。
- 触るとき: SessionStore の起動順序を変えるとき、または init より前に通知を受けてしまう経路を調べるとき。
- 呼び出し先: `Glean.sessionRestore.startupTimeline.sessionRestoreInitialized.set()`, `Services.obs.addObserver()`, `Services.telemetry.msSinceProcessStart()`, `this.#initPrefs()`, `this.#log.debug()`, `this.promiseAllWindowsRestored.finally()`
- 参照: `this.#initialized`
- XPCOM: `Services.obs` / `Services.telemetry`

## _SessionStore.#initSession()
- 位置: L784-965
- 役割: SessionStartup の状態から復元対象を決める。遅延復元ではピン留めタブと保存済みグループだけを残し、クラッシュ後は about:sessionrestore か about:welcomeback に差し替え、通常復元では明示的に閉じたタブを除いて復元用の state を返す。
- 触るとき: 起動時の復元方式(通常・遅延・クラッシュ後の確認画面)を変えるとき、または起動時の判定結果が decision として記録される経路を追うとき。
- 呼び出し先: `Glean.sessionRestore.startupInitSession.start()`, `Glean.sessionRestore.startupInitSession.stopAndAccumulate()`, `ss.willRestore()`, `this.#log.debug()`, `this.#prefBranch.getBoolPref()`, `this.#recordSessionDecision()`
- 条件付き依存: `if (state)` → `this.#initSplitViewIds()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `this.#prepDataForDeferredRestore()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `iniState.windows.some()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `this.#log.debug()`
- 条件付き依存: `if (remainingState.windows.length)` → `LastSession.setState()`
- 条件付き依存: `if (ss.sessionType == ss.DEFER_SESSION)` → `Glean.browserEngagement.sessionrestoreInterstitial.deferred_restore.add()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `LastSession.setState()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `ss.willRestoreAsCrashed()`
- 条件付き依存: `if (restoreAsCrashed)` → `this.#log.debug()`
- 条件付き依存: `if (restoreAsCrashed)` → `this.#needsRestorePage()`
- 条件付き依存: `if (decision.interstitialReason)` → `Glean.browserEngagement.sessionrestoreInterstitial[ `shown_${decision.interstitialReason}` ].add()`
- 条件付き依存: `if (decision.interstitialReason)` → `this.#log.debug()`
- 条件付き依存: `if (!(decision.interstitialReason))` → `this.#hasSingleTabWithURL()`
- 条件付き依存: `if ( this.#hasSingleTabWithURL(state.windows, "about:welcomeback") )` → `this.#log.debug()`
- 条件付き依存: `if ( this.#hasSingleTabWithURL(state.windows, "about:welcomeback") )` → `Glean.browserEngagement.sessionrestoreInterstitial.shown_only_about_welcomeback.add()`
- 条件付き依存: `if (!restoreAsCrashed)` → `Glean.browserEngagement.sessionrestoreInterstitial.autorestore.add()`
- 条件付き依存: `if (!restoreAsCrashed)` → `this.#log.debug()`
- 条件付き依存: `if (!restoreAsCrashed)` → `this.#removeExplicitlyClosedTabs()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `this.#updateSessionStartTime()`
- 条件付き依存: `if (!(ss.sessionType == ss.DEFER_SESSION))` → `state.windows.forEach()`
- 条件付き依存: `if (state)` → `state?.windows?.forEach()`
- 条件付き依存: `if (state)` → `state?._closedWindows?.forEach()`
- 条件付き依存: `if (state)` → `this.#log.error()`
- 条件付き依存: `if ( !lazy.RunState.isQuitting && this.#prefBranch.getBoolPref("sessionstore.resume_session_once") )` → `this.#prefBranch.setBoolPref()`
- 参照: `Glean.browserEngagement.sessionrestoreInterstitial`, `aWindow.__lastSessionWindowID`, `decision.action`, `decision.initError`, `decision.interstitialReason`, `ex.name`, `iniState.savedGroups`, `iniState.savedGroups.length`, `iniState.windows.length`, `lazy.E10SUtils.SERIALIZED_SYSTEMPRINCIPAL`, `lazy.RunState.isQuitting`, `lazy.SessionStartup`, `remainingState.windows.length`, `ss.DEFER_SESSION`, `ss.RESUME_SESSION`, `ss.previousSessionCrashed`, `ss.sessionType`, `ss.state`, `state.lastSessionState`, `state.savedGroups`, `state.session`, `state.session.recentCrashes`, `state.windows`, `state.windows.length`, `state.windows[0].sizemode`, `state.windows[0].tabs`, `state.windows[0].tabs[0].entries`, `state.windows[0].tabs[0].entries[0].triggeringPrincipal_base64`, `state.windows[0].tabs[0].entries[0].url`, `state?.savedGroups`, `this.#isUserConfiguredRestore`, `this.#recentCrashes`, `this.#savedGroups`, `win._maybeDontRestoreTabs`, `win.tabs.length`

## _SessionStore.#recordSessionDecision()
- 位置: L980-1019
- 役割: セッション種別(no_session・recover・resume・defer)と選んだ動作、クラッシュ有無などを Glean の startupSessionDecision に記録する。
- 触るとき: 起動時のセッション判定テレメトリの項目や値を追加・変更するとき。
- 呼び出し先: `Glean.sessionRestore.startupSessionDecision.record()`, `this.#log.debug()`
- 参照: `PrivateBrowsingUtils.permanentPrivateBrowsing`, `Services.appinfo.restartedByOS`, `decision.action`, `decision.initError`, `decision.interstitialReason`, `extra.init_error`, `extra.interstitial_reason`, `extra.previous_session_crashed`, `extra.resume_reason`, `ss.DEFER_SESSION`, `ss.NO_SESSION`, `ss.RECOVER_SESSION`, `ss.RESUME_SESSION`, `ss.previousSessionCrashed`, `ss.sessionType`
- XPCOM: `Services.appinfo`

## _SessionStore.#removeExplicitlyClosedTabs()
- 位置: L1030-1080
- 役割: _maybeDontRestoreTabs が付いたウィンドウを復元対象から外す。唯一のウィンドウであればそのタブを閉じたタブ扱いにして _closedTabs へ移す。
- 触るとき: ユーザーが閉じたはずのタブが起動時に復元されてしまう不具合(bug 490136 の系統)を調べるとき。
- 条件付き依存: `if (state.windows.length == 1)` → `winData.tabs.pop()`
- 条件付き依存: `if (state.windows.length == 1)` → `this.historyIndex()`
- 条件付き依存: `if (state.windows.length == 1)` → `Math.min()`
- 条件付き依存: `if (state.windows.length == 1)` → `Math.max()`
- 条件付き依存: `if (state.windows.length == 1)` → `Date.now()`
- 条件付き依存: `if (state.windows.length == 1)` → `this.#shouldSaveTabState()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.#saveClosedTabData()`
- 条件付き依存: `if (!(state.windows.length == 1))` → `winData.tabs.some()`
- 条件付き依存: `if (winData.tabs.some(this.#shouldSaveTabState))` → `Date.now()`
- 条件付き依存: `if (winData.tabs.some(this.#shouldSaveTabState))` → `state._closedWindows.unshift()`
- 条件付き依存: `if (!(state.windows.length == 1))` → `state.windows.splice()`
- 参照: `state.windows`, `state.windows.length`, `tabState.entries`, `tabState.entries.length`, `tabState.entries[activeIndex].title`, `tabState.entries[activeIndex].url`, `tabState.image`, `this.#shouldSaveTabState`, `winData._closedTabs`, `winData._lastClosedTabGroupCount`, `winData._maybeDontRestoreTabs`, `winData.closedAt`, `winData.tabs.length`

## _SessionStore.#initPrefs()
- 位置: L1091-1139
- 役割: browser.sessionstore.* の設定値を読み込んでフィールドに保持し、変更通知を購読する。debug 切り替えも同時に設定する。
- 触るとき: 新しい sessionstore 設定を追加するとき、または設定変更が即座に反映されない原因を調べるとき。
- 呼び出し先: `Glean.sessionRestore.newTabOnRestoreEnabled.set()`, `Services.prefs.addObserver()`, `Services.prefs.getBranch()`, `this.#prefBranch.addObserver()`, `this.#prefBranch.getBoolPref()`, `this.#prefBranch.getIntPref()`
- 参照: `lazy.sessionStoreLogger`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedTabsFromClosedWindowsEnabled`, `this.#log`, `this.#max_tabs_undo`, `this.#max_windows_undo`, `this.#prefBranch`, `this.#restore_on_demand`
- XPCOM: `Services.prefs`

## _SessionStore.#uninit()
- 位置: L1145-1163
- 役割: 終了時に RunState を closing にし、初期化済みなら最後の状態を保存し、TabRestoreQueue をリセットして保留中の保存をキャンセルする。
- 触るとき: 終了時にセッションファイルが最後の状態で書き出されるかを確認するとき、または終了処理の順序を変えるとき。
- 呼び出し先: `TabRestoreQueue.reset()`, `lazy.RunState.setClosing()`, `lazy.SessionSaver.cancel()`
- 条件付き依存: `if (this.#sessionInitialized)` → `lazy.SessionSaver.run()`
- 参照: `this.#initialized`, `this.#sessionInitialized`

## _SessionStore.observe()
- 位置: L1175-1263
- 役割: Observer 通知(新規・閉じたウィンドウ、終了、履歴消去、設定変更、idle-daily、SHistory リスナー関連など)を topic ごとに対応するハンドラへ振り分ける。
- 触るとき: 新しい通知を購読させるとき、または特定の通知でどの処理が走るかを追うとき。
- 呼び出し先: `JSON.parse()`, `this.#notifyOfClosedObjectsChange()`, `this.#onBeforeBrowserWindowShown()`, `this.#onClose()`, `this.#onClose(/** @type {ChromeWindow} */ (aSubject)).then()`, `this.#onFinalTabStateUpdateComplete()`, `this.#onIdleDaily()`, `this.#onLastWindowCloseGranted()`, `this.#onPrefChange()`, `this.#onPurgeDomainData()`, `this.#onPurgeSessionHistory()`, `this.#onQuitApplication()`, `this.#onQuitApplicationGranted()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (userContextId)` → `this.#forgetTabsWithUserContextId()`
- 条件付き依存: `if (permanentKey)` → `this.#maybeRecreateSHistoryListener()`
- 条件付き依存: `if (permanentKey)` → `this.#browserSHistoryListener.get(permanentKey)?.unregister()`
- 条件付き依存: `if (permanentKey)` → `this.#browserSHistoryListener.get()`
- 参照: `( browsingContext.embedderElement )?.permanentKey`, `( browsingContext?.embedderElement )?.permanentKey`, `JSON.parse(aData).userContextId`, `browsingContext.embedderElement`, `browsingContext.isContent`, `browsingContext.top`, `browsingContext?.embedderElement`
- XPCOM: `Services.obs`

## _SessionStore.#getOrCreateSHistoryListener()
- 位置: L1265-1276
- 役割: トップの browsing context に対応する session history リスナーを返す。無ければ作成し、トップでなければ null を返す。
- 触るとき: タブのセッション履歴の変化を SessionStore が取りこぼさず追跡しているかを調べるとき。
- 呼び出し先: `this.#browserSHistoryListener.get()`, `this.#createSHistoryListener()`
- 参照: `browsingContext.top`

## _SessionStore.#maybeRecreateSHistoryListener()
- 位置: L1282-1288
- 役割: 既存リスナーの _browserId が現在の browsingContext と違う場合にリスナーを解除し、作り直す。
- 触るとき: browser が別の browsing context に付け替えられた後も履歴が追跡されるかを確認するとき。
- 呼び出し先: `this.#browserSHistoryListener.get()`
- 条件付き依存: `if (!listener || listener._browserId != browsingContext.browserId)` → `listener?.unregister()`
- 条件付き依存: `if (!listener || listener._browserId != browsingContext.browserId)` → `this.#createSHistoryListener()`
- 参照: `browsingContext.browserId`, `listener._browserId`

## _SessionStore.#createSHistoryListener()
- 位置: L1290-1417
- 役割: browsing context の sessionHistory に SHistoryListener を登録して permanentKey ごとに保持し、必要なら直ちに履歴を収集してキャッシュに書く。
- 触るとき: タブごとの履歴リスナーの生成条件や、about:blank を初回収集から外す判定を変えるとき。
- 呼び出し先: `sessionHistory.addSHistoryListener()`, `this.#browserSHistoryListener.set()`
- 条件付き依存: `if (collectImmediately && (!isAboutBlank || sessionHistory.count !== 0))` → `listener.collect()`
- 参照: `browsingContext.currentURI?.spec`, `browsingContext.sessionHistory`, `sessionHistory.count`

## SHistoryListener.constructor()
- 位置: L1296-1304
- 役割: nsISHistoryListener を実装するリスナーを作り、browserId と収集開始位置(kNoIndex)を初期化する。
- 触るとき: リスナーが保持する状態の初期値を変えるとき。
- 呼び出し先: `ChromeUtils.generateQI()`
- 参照: `browsingContext.browserId`, `this.QueryInterface`, `this._browserId`, `this._fromIndex`

## SHistoryListener.unregister()
- 位置: L1306-1312
- 役割: 現在のトップ browsing context の sessionHistory からリスナーを外し、permanentKey の登録も削除する。
- 触るとき: タブが閉じられたり付け替えられた後に履歴リスナーが残り続けないかを確認するとき。
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`, `SessionStore.#browserSHistoryListener.delete()`, `bc?.sessionHistory?.removeSHistoryListener()`
- 参照: `this._browserId`

## SHistoryListener.collect()
- 位置: L1314-1349
- 役割: 履歴の差分(全体または _fromIndex 以降)を SessionHistory.collectFromParent で取り出し、writeToCache 指定時はタブ状態の更新として渡す。変更が無ければ null を返す。
- 触るとき: セッション履歴の差分がどの範囲で収集されるか、またはキャッシュ書き込みの条件を変えるとき。
- 呼び出し先: `Glean.sessionRestore.collectSessionHistory.start()`, `Glean.sessionRestore.collectSessionHistory.stopAndAccumulate()`, `lazy.SessionHistory.collectFromParent()`
- 条件付き依存: `if (writeToCache)` → `SessionStore.#onTabStateUpdate()`
- 参照: `browsingContext.currentURI?.spec`, `browsingContext.currentWindowGlobal?.browsingContext?.window`, `browsingContext.embedderElement?.documentGlobal`, `browsingContext.sessionHistory`, `this._fromIndex`

## SHistoryListener.collectFrom()
- 位置: L1351-1374
- 役割: 既に記録した開始位置より後ろなら何もせず、そうでなければ index を収集開始位置として保存し、フレームローダーに履歴更新を要求する。
- 触るとき: 履歴の変化が遅延収集のタイマー経由でどのように集められるかを追うとき。
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`
- 条件付き依存: `if (bc?.embedderElement?.frameLoader)` → `bc.embedderElement.frameLoader.requestSHistoryUpdate()`
- 参照: `bc?.embedderElement?.frameLoader`, `this._browserId`, `this._fromIndex`

## SHistoryListener.OnHistoryNewEntry()
- 位置: L1376-1381
- 役割: 新しい履歴エントリが追加されたとき、oldIndex - 1 から collectFrom で収集を要求する(oldIndex が -1 ならそのまま)。
- 触るとき: 新規ナビゲーション時に現在のエントリの変更も拾えているかを確認するとき。
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryGotoIndex()
- 位置: L1382-1384
- 役割: 履歴内を移動したとき、kLastIndex から collectFrom で収集を要求する。
- 触るとき: 戻る・進むで履歴位置が移動した際の保存範囲を変えるとき。
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryPurge()
- 位置: L1385-1387
- 役割: 履歴が消去されたとき、-1 から全体を収集対象にする。
- 触るとき: 履歴消去後に保存内容が古いまま残らないかを確認するとき。
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryReload()
- 位置: L1388-1391
- 役割: リロードされたとき、-1 から全体を収集対象にして true を返す。
- 触るとき: リロード時の履歴保存の扱いを変えるとき。
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryReplaceEntry()
- 位置: L1392-1394
- 役割: エントリが置き換えられたとき、-1 から全体を収集対象にする。
- 触るとき: location.replace 相当の置換で履歴が保存されない問題を調べるとき。
- 呼び出し先: `this.collectFrom()`

## SHistoryListener.OnHistoryTruncate()
- 位置: L1395-1395
- 役割: 何もしない。履歴の切り詰め通知を無視する。
- 触るとき: 履歴の切り詰めを保存に反映する必要が出た場合にここへ処理を足すかを検討するとき。

## SHistoryListener.OnDocumentViewerEvicted()
- 位置: L1396-1396
- 役割: 何もしない。ドキュメントビューアが退避された通知を無視する。
- 触るとき: ビューア退避時にも保存が必要になったかを検討するとき。

## SHistoryListener.OnHistoryCommit()
- 位置: L1397-1397
- 役割: 何もしない。履歴のコミット通知を無視する。
- 触るとき: コミット時に収集が必要になったかを検討するとき。

## SHistoryListener.OnEntryUpdated()
- 位置: L1398-1398
- 役割: 何もしない。エントリ更新の通知を無視する。
- 触るとき: エントリ更新を保存に反映する必要があるかを検討するとき。

## _SessionStore.#onTabStateUpdate()
- 位置: L1419-1438
- 役割: クラッシュ中でないブラウザのタブ状態を TabState に反映し、保存を遅延予約する。閉じたタブの最終更新なら閉じたタブの状態もキャッシュからコピーする。
- 触るとき: タブ状態の更新がどこで保存に入るか、閉じたタブの後追い更新を扱う経路を調べるとき。
- 呼び出し先: `lazy.TabState.update()`, `this.#closingTabMap.get()`, `this.#crashedBrowsers.has()`, `this.#saveStateDelayed()`
- 条件付き依存: `if (closedTab)` → `lazy.TabState.copyFromCache()`
- 参照: `closedTab.tabData.state`

## _SessionStore.#onFinalTabStateUpdateComplete()
- 位置: L1443-1491
- 役割: タブ閉鎖時の最終更新が届いた後、保存すべきかを判定して閉じたタブ一覧に追加または削除し、孤立したグループを掃除する。さらにフラッシュ要求を解決してリスナーを解除し、shutdown-flush 通知を出す。
- 触るとき: 閉じたタブが閉じたタブ一覧に残るべきか判定する経路、またはシャットダウン時のフラッシュ順序を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.TabStateFlusher.resolveAll()`, `this.#browserSHistoryListener.get()`, `this.#browserSHistoryListener.get(permanentKey)?.unregister()`, `this.#closingTabMap.has()`, `this.#crashedBrowsers.has()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(permanentKey)?.unregister()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#closingTabMap.get()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#closingTabMap.delete()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#shouldSaveTabState()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `closedTabs.indexOf()`
- 条件付き依存: `if (shouldSave && index == -1)` → `this.#saveClosedTabData()`
- 条件付き依存: `if (!shouldSave && index > -1)` → `this.#removeClosedTabData()`
- 条件付き依存: `if ( this.#closingTabMap.has(permanentKey) && !this.#crashedBrowsers.has(permanentKey) )` → `this.#cleanupOrphanedClosedGroups()`
- 参照: `browser.permanentKey`, `tabData.permanentKey`, `tabData.state`
- XPCOM: `Services.obs`

## _SessionStore.updateSessionStoreFromChild()
- 位置: L1509-1558
- 役割: 子プロセスから届いたタブ状態の更新を、現在のエポックのものに限って受け付ける。必要なら履歴の差分を収集して update に入れ、#onTabStateUpdate に渡す。
- 触るとき: 子プロセスからのタブ状態更新の受け付け条件や、保存時(forStorage)の履歴収集を変えるとき。
- 呼び出し先: `this.#getOrCreateSHistoryListener()`, `this.#isCurrentEpoch()`, `this.#onTabStateUpdate()`
- 条件付き依存: `if (listener)` → `lazy.SessionHistory.collectNonWebControlledLoadingSession()`
- 条件付き依存: `if (listener)` → `listener.collect()`
- 参照: `browser?.documentGlobal`, `browser?.permanentKey`, `browsingContext.currentWindowGlobal?.browsingContext?.window`, `browsingContext.isReplaced`, `update.data.historychange`, `update.epoch`, `update.sHistoryNeeded`

## _SessionStore.handleEvent()
- 位置: L1568-1670
- 役割: タブ・タブグループ・分割表示・クラッシュ・XUL フレームローダーなどの DOM イベントを種類ごとに対応処理へ振り分け、最後に復元中ウィンドウの状態をクリアする。未知のイベントは例外にする。
- 触るとき: 保存を走らせるイベントを追加・削除するとき、またはタブを閉じたときに閉じたタブとして記録されない理由を追うとき。
- 呼び出し先: `this.#clearRestoringWindows()`, `this.#maybeRestoreTabContent()`, `this.#notifyOfClosedObjectsChange()`, `this.#onTabAdd()`, `this.#onTabBrowserInserted()`, `this.#onTabHide()`, `this.#onTabRemove()`, `this.#onTabSelect()`, `this.#onTabShow()`, `this.#saveStateDelayed()`
- 条件付き依存: `if (detail.adoptedTab)` → `this.#moveCustomTabValue()`
- 条件付き依存: `if (detail.adoptedBy)` → `this.#moveCustomTabValue()`
- 条件付き依存: `if (detail.adoptedBy)` → `this.#onMoveToNewWindow()`
- 条件付き依存: `if (!detail.skipSessionStore)` → `this.#onTabClose()`
- 条件付き依存: `if (!(/** @type {CustomEvent} */ (aEvent).detail?.skipSessionStore))` → `this.#onTabGroupRemoveRequested()`
- 条件付き依存: `if (!(/** @type {CustomEvent} */ (aEvent).detail?.skipSessionStore))` → `this.#notifyOfClosedObjectsChange()`
- 条件付き依存: `if (/** @type {FrameCrashedEvent} */ (aEvent).isTopFrame)` → `this.#onBrowserCrashed()`
- 条件付き依存: `if ( browser.namespaceURI == XUL_NS && browser.localName == "browser" && browser.frameLoader && browser.permanentKey )` → `this.#resetEpoch()`
- 参照: `(aEvent).detail.tabs`, `(aEvent).detail?.skipSessionStore`, `(aEvent).isTopFrame`, `(aEvent.currentTarget).documentGlobal`, `aEvent.currentTarget`, `aEvent.originalTarget`, `aEvent.type`, `browser.frameLoader`, `browser.localName`, `browser.namespaceURI`, `browser.permanentKey`, `detail.adoptedBy`, `detail.adoptedBy.linkedBrowser`, `detail.adoptedTab`, `detail.inMultiselection`, `detail.skipSessionStore`, `tab.linkedBrowser`

## _SessionStore.#generateWindowID()
- 位置: L1678-1680
- 役割: "window" に連番を付けた内部ウィンドウ ID の文字列を返す。
- 触るとき: ウィンドウ ID の形式を変えるとき、またはセッション内で ID が一意に払い出されるかを確認するとき。
- 参照: `this.#nextWindowID`

## _SessionStore.ensureInitialized()
- 位置: L1688-1697
- 役割: セッションが初期化済みで、対象ウィンドウがまだ ID を持たない場合だけ #onLoad を呼んで追跡を始める。
- 触るとき: 初期化より後に開いたウィンドウが追跡されない問題や、同じウィンドウへの二重登録を調べるとき。
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#sessionInitialized && !this.#windowIds.has(window))` → `this.#onLoad()`
- 参照: `this.#sessionInitialized`

## _SessionStore.#onLoad()
- 位置: L1705-1791
- 役割: 未登録のウィンドウに ID を振り、タブ・グループ・閉じたタブなどを持つ状態オブジェクトを作る。プライベート、ポップアップ、taskbartab、AI ウィンドウ、chromeless などのフラグを立て、既存タブとタブ関連イベントの購読を始める。終了中に開かれたウィンドウは登録しない。
- 触るとき: ウィンドウ状態に新しいフラグを追加するとき、またはウィンドウがいつ追跡され始めるかを調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `aWindow.docShell.treeOwner .QueryInterface()`, `aWindow.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`, `aWindow.document.documentElement.hasAttribute()`, `aWindow.gBrowser.addEventListener()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `tabbrowser.tabContainer.addEventListener()`, `this.#generateWindowID()`, `this.#isWindowLoaded()`, `this.#onTabBrowserInserted()`, `this.#windowIds.get()`, `this.#windowIds.set()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!aWindow.toolbar.visible)` → `this.#windowIds.get()`
- 条件付き依存: `if (aWindow.document.documentElement.hasAttribute("taskbartab"))` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActiveAndEnabled(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (aWindow.document.documentElement.hasAttribute(ARG_CHROMELESS_WINDOW))` → `this.#windowIds.get()`
- 条件付き依存: `if ( aWindow.document.documentElement.hasAttribute( ARG_WEB_EXTENSION_POPUP_WINDOW ) )` → `this.#windowIds.get()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `aWindow.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow).chromeFlags`, `aWindow.gBrowser`, `aWindow.toolbar.visible`, `lazy.RunState.isQuitting`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._restoring`, `this.#windows[this.#windowIds.get(aWindow)].args`, `this.#windows[this.#windowIds.get(aWindow)].isAIWindow`, `this.#windows[this.#windowIds.get(aWindow)].isPopup`, `this.#windows[this.#windowIds.get(aWindow)].isPrivate`, `this.#windows[this.#windowIds.get(aWindow)].isTaskbarTab`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md)

## _SessionStore.#initializeWindow()
- 位置: L1805-2007
- 役割: 初回ウィンドウなら起動時の初期状態を流し込み、遅れて開いた通常ウィンドウには延期していた状態、閉じたウィンドウ、taskbar tab 向けの前回セッションのいずれかを復元する。
- 触るとき: 起動時の復元が最初のウィンドウ・通常ウィンドウ・taskbar tab のどれに入るかの条件を変えるとき、または last-closed-window の復元で閉じたウィンドウがどう分割されるかを調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isStopped)` → `lazy.RunState.setRunning()`
- 条件付き依存: `if (aInitialState)` → `lazy.SessionSaver.updateLastSaveTime()`
- 条件付き依存: `if (isPrivateWindow || isTaskbarTab)` → `this.#log.debug()`
- 条件付き依存: `if (isPrivateWindow || isTaskbarTab)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (isPrivateWindow || isTaskbarTab)` → `this.#deferredAllWindowsRestored.resolve()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `Glean.sessionRestore.startupTimeline.sessionRestoreRestoring.set()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `Services.telemetry.msSinceProcessStart()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `this.#globalState.setFromState()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `lazy.SessionCookies.restore()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `this.#isCmdLineEmpty()`
- 条件付き依存: `if (!(isPrivateWindow || isTaskbarTab))` → `this.#restoreWindows()`
- 条件付き依存: `if (!(aInitialState))` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(aInitialState))` → `this.#deferredAllWindowsRestored.resolve()`
- 条件付き依存: `if (!(lazy.RunState.isStopped))` → `this.#isWindowLoaded()`
- 条件付き依存: `if (this.#deferredInitialState && isRegularWindow)` → `lazy.SessionStartup.willRestore()`
- 条件付き依存: `if (lazy.SessionStartup.willRestore())` → `this.#globalState.setFromState()`
- 条件付き依存: `if (lazy.SessionStartup.willRestore())` → `this.#restoreWindows()`
- 条件付き依存: `if (closedWindowState)` → `lazy.SessionStartup.willRestore()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" || !lazy.SessionStartup.willRestore() )` → `this.#prepDataForDeferredRestore()`
- 条件付き依存: `if (!normalTabsState.windows.length)` → `this.#removeClosedWindow()`
- 条件付き依存: `if (!( AppConstants.platform == "macosx" || !lazy.SessionStartup.willRestore() ))` → `this.#removeClosedWindow()`
- 条件付き依存: `if (newWindowState)` → `this.#isCmdLineEmpty()`
- 条件付き依存: `if (newWindowState)` → `this.#restoreWindow()`
- 条件付き依存: `if (newWindowState)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if ( this.#restoreLastWindow && aWindow.toolbar.visible && this.#closedWindows.length && !isPrivateWindow )` → `this.#prefBranch.setBoolPref()`
- 条件付き依存: `if (!( this.#restoreLastWindow && aWindow.toolbar.visible && this.#closedWindows.length && !isPrivateWindow ))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `LastSession.getState()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `this.#globalState.setFromState()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `lazy.SessionCookies.restore()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && this.#shouldRestoreLastSession && isRegularWindow )` → `this.#restoreWindows()`
- 参照: `AppConstants.platform`, `aInitialState.cookies`, `aInitialState.windows`, `aInitialState.windows.length`, `aWindow.toolbar.visible`, `appTabsState.windows`, `appTabsState.windows.length`, `lastSessionState.cookies`, `lazy.RunState.isStopped`, `lazy.SessionStartup.state`, `newWindowState.__lastSessionWindowID`, `normalTabsState.windows`, `normalTabsState.windows.length`, `normalTabsState.windows[0].__lastSessionWindowID`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[i].isPopup`, `this.#cmdLineHadURLOnStartup`, `this.#deferredInitialState`, `this.#deferredInitialState.windows`, `this.#deferredInitialState.windows.length`, `this.#isUserConfiguredRestore`, `this.#restoreCount`, `this.#restoreLastWindow`, `this.#shouldRestoreLastSession`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].isTaskbarTab`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.telemetry`

## _SessionStore.#onBeforeBrowserWindowShown()
- 位置: L2015-2113
- 役割: ウィンドウが表示される直前に、DocumentPiP・mini-window・ASWebAuthenticationSession を除いて登録し、待機中の Promise を解決する。初期化済みならそのまま初期化し、未初期化なら最初のウィンドウの遅延起動完了と SessionStartup の初期化完了を待ってからセッションを読み込む。
- 触るとき: 起動直後に開くウィンドウの扱いや、追跡対象外にするウィンドウ種別を増やすとき。
- 呼び出し先: `WINDOW_SHOWING_PROMISES.get()`, `aWindow.document.documentElement.hasAttribute()`, `this.#log.error()`, `this.#onLoad()`, `this.#promiseReadyForInitialization .then()`
- 条件付き依存: `if (deferred)` → `deferred.resolve()`
- 条件付き依存: `if (deferred)` → `WINDOW_SHOWING_PROMISES.delete()`
- 条件付き依存: `if (this.#sessionInitialized)` → `this.#log.debug()`
- 条件付き依存: `if (this.#sessionInitialized)` → `this.#initializeWindow()`
- 条件付き依存: `if (!this.#promiseReadyForInitialization)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this.#promiseReadyForInitialization)` → `Promise.all()`
- 条件付き依存: `if (aWindow.closed)` → `this.#log.debug()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `this.#initSession()`
- 条件付き依存: `if (initialState)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `Glean.sessionRestore.startupOnloadInitialWindow.start()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `this.#initializeWindow()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `Glean.sessionRestore.startupOnloadInitialWindow.stopAndAccumulate()`
- 条件付き依存: `if (!(this.#sessionInitialized))` → `this.#deferredInitialized.resolve()`
- 参照: `aWindow.browsingContext.isDocumentPiP`, `aWindow.closed`, `lazy.SessionStartup.onceInitialized`, `this.#promiseReadyForInitialization`, `this.#sessionInitialized`
- XPCOM: `Services.obs`

## obs()
- 位置: L2057-2062
- 役割: browser-delayed-startup-finished 通知を待ち、対象ウィンドウが届いたら自分自身を登録解除して Promise を解決する匿名 Observer。
- 触るとき: 初回ウィンドウの遅延起動が終わるのを待つ仕組みを変えたり、起動時の待ち合わせが止まる原因を追うとき。
- 条件付き依存: `if (aWindow == subject)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aWindow == subject)` → `resolve()`
- XPCOM: `Services.obs`

## _SessionStore.#onClose()
- 位置: L2125-2323
- 役割: ウィンドウ終了時に SSWindowClosing を発火し、タブのイベント購読を外す。実行中なら状態を閉じた時刻付きで退避し、タスクバータブ併用時の再起動復元を予約し、タブのフラッシュ完了後に閉じたウィンドウとして保存判定して状態を保存する。
- 触るとき: ウィンドウを閉じたときに閉じたウィンドウ一覧へ入る条件や、タスクバータブが残るときの次回復元の予約を変えるとき。
- 呼び出し先: `Array.from()`, `Promise.resolve()`, `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `aWindow.gBrowser.removeEventListener()`, `event.initEvent()`, `tabbrowser.tabContainer.removeEventListener()`, `this.#isWindowLoaded()`, `this.#onTabRemove()`, `this.#windowIds.get()`
- 条件付き依存: `if (!isFullyLoaded)` → `this.#windowIds.has()`
- 条件付き依存: `if (!this.#windowIds.has(aWindow))` → `this.#windowIds.set()`
- 条件付き依存: `if (!this.#windowIds.has(aWindow))` → `this.#generateWindowID()`
- 条件付き依存: `if (!isFullyLoaded)` → `WINDOW_RESTORE_IDS.get()`
- 条件付き依存: `if (!isFullyLoaded)` → `this.#windowIds.get()`
- 条件付き依存: `if (!isFullyLoaded)` → `WINDOW_RESTORE_IDS.delete()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#collectWindowData()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#tabClosingByWindowMap.set()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Date.now()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#isLastRestorableWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Object.values(this.#windows).filter()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Object.values()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#log.debug()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Object.values(this.#windows).some()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(this.willAutoRestore))` → `Services.obs.notifyObservers()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && isLastRegularWindow && !winData.isTaskbarTab && !winData.isPrivate && taskbarTabsRemains )` → `this.getCurrentState()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && isLastRegularWindow && !winData.isTaskbarTab && !winData.isPrivate && taskbarTabsRemains )` → `lazy.PrivacyFilter.filterPrivateWindowsAndTabs()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.taskbarTabs.enabled", false) && isLastRegularWindow && !winData.isTaskbarTab && !winData.isPrivate && taskbarTabsRemains )` → `LastSession.setState()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#saveableClosedWindowData.add()`
- 条件付き依存: `if (!winData.isPrivate && !winData.isTaskbarTab)` → `this.#maybeSaveClosedWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.TabStateFlusher.flushWindow(aWindow).then()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.TabStateFlusher.flushWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `WINDOW_FLUSHING_PROMISES.delete()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#tabClosingByWindowMap.has()`
- 条件付き依存: `if (this.#tabClosingByWindowMap.has(browser.permanentKey))` → `this.#tabClosingByWindowMap.get()`
- 条件付き依存: `if (this.#tabClosingByWindowMap.has(browser.permanentKey))` → `lazy.TabState.copyFromCache()`
- 条件付き依存: `if (this.#tabClosingByWindowMap.has(browser.permanentKey))` → `this.#tabClosingByWindowMap.delete()`
- 条件付き依存: `if (!isLastWindow && winData.closedId > -1)` → `this.#addClosedAction()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#cleanUpWindow()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#saveStateDelayed()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `WINDOW_FLUSHING_PROMISES.set()`
- 条件付き依存: `if (!(lazy.RunState.isRunning))` → `this.#cleanUpWindow()`
- 参照: `AppConstants.platform`, `Object.values(this.#windows).filter( wData => !wData.isPrivate && !wData.isTaskbarTab ).length`, `aWindow.gBrowser`, `browser.permanentKey`, `lazy.RunState.isRunning`, `tab.linkedBrowser.permanentKey`, `tabbrowser.browsers`, `tabbrowser.selectedBrowser.contentTitle`, `tabbrowser.selectedTab.label`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `this.#restoreWithoutRestart`, `this.#shouldRestoreLastSession`, `this.#statesToRestore`, `this.#statesToRestore[restoreID].windows`, `this.#windowToFocus`, `this.#windows`, `this.LAST_ACTION_CLOSED_WINDOW`, `this.willAutoRestore`, `wData.isPrivate`, `wData.isTaskbarTab`, `winData._shouldRestore`, `winData.busy`, `winData.closedAt`, `winData.closedId`, `winData.isPrivate`, `winData.isTaskbarTab`, `winData.title`
- XPCOM: `Services.obs` / `Services.prefs`

## _SessionStore.#cleanUpWindow()
- 位置: L2340-2352
- 役割: 残っているタブのフラッシュ Promise を解決し、ウィンドウの状態を DyingWindowCache に移して、ウィンドウ ID と保存対象の対応を削除する。
- 触るとき: 閉じたウィンドウのデータが参照されなくなるタイミングや、ウィンドウ ID の後始末を変えるとき。
- 呼び出し先: `DyingWindowCache.set()`, `lazy.TabStateFlusher.resolveAll()`, `this.#saveableClosedWindowData.delete()`, `this.#windowIds.delete()`

## _SessionStore.#maybeSaveClosedWindow()
- 位置: L2371-2447
- 役割: 保存可能なタブがあるか、最後のウィンドウであれば閉じたウィンドウ一覧に入れ、閉じた時刻の新しい順に挿入して ID を振る。条件を満たさなければ一覧から外す。macOS で初回に閉じたときは履歴メニューに popupshowing を送る。
- 触るとき: 閉じたウィンドウ一覧に残す条件(保存可能なタブの判定)や、最後のウィンドウの扱いを変えるとき。
- 呼び出し先: `this.#saveableClosedWindowData.has()`
- 条件付き依存: `if ( lazy.RunState.isRunning && this.#saveableClosedWindowData.has(winData) )` → `winData.tabs.some()`
- 条件付き依存: `if ( lazy.RunState.isRunning && this.#saveableClosedWindowData.has(winData) )` → `this.#closedWindows.indexOf()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#closedWindows.findIndex()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#closedWindows.splice()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#capClosedWindows()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#saveOpenTabGroupsOnClose()`
- 条件付き依存: `if (shouldStore && !alreadyStored)` → `this.#log.debug()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" && this.#closedWindows.length == 1 )` → `window.document.getElementById()`
- 条件付き依存: `if ( AppConstants.platform == "macosx" && this.#closedWindows.length == 1 )` → `historyMenu.menupopup.dispatchEvent()`
- 条件付き依存: `if (alreadyStored)` → `this.#removeClosedWindow()`
- 条件付き依存: `if (!shouldStore)` → `this.#log.warn()`
- 参照: `AppConstants.platform`, `Services.appShell.hiddenDOMWindow`, `lazy.RunState.isRunning`, `this.#closedObjectsChanged`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedWindows.length`, `this.#nextClosedId`, `this.#shouldSaveTabState`, `win.closedAt`, `winData._closedTabs.length`, `winData.closedAt`, `winData.closedId`, `winData.tabs.length`, `window.CustomEvent`
- XPCOM: `Services.appShell`

## _SessionStore.#saveOpenTabGroupsOnClose()
- 位置: L2464-2503
- 役割: 閉じるウィンドウ内のタブグループのうち saveOnWindowClose のものを保存済みグループに変換し、そのグループに属するタブを整形して追加した上で状態を記録する。
- 触るとき: ウィンドウを閉じたときにタブグループが失われず保存済みに残るかを確認するとき、またはグループ保存の条件を変えるとき。
- 呼び出し先: `closedWinData.groups.map()`, `lazy.TabGroupState.savedInClosedWindow()`, `newlySavedTabGroups.has()`, `newlySavedTabGroups.set()`, `newlySavedTabGroups.values()`, `this.#recordSavedTabGroupState()`, `this.#shouldSaveTabState()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.formatTabStateForSavedGroup()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `newlySavedTabGroups.get(tabState.groupId).tabs.push()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `newlySavedTabGroups.get()`
- 参照: `closedWinData.closedId`, `closedWinData.groups`, `closedWinData.tabs`, `closedWinData.tabs.length`, `tabGroupState.id`, `tabGroupState.saveOnWindowClose`, `tabState.groupId`

## _SessionStore.formatTabStateForSavedGroup()
- 位置: L2516-2533
- 役割: タブの現在の履歴インデックス(範囲内に丸める)のエントリからタイトルを決め、保存済みグループ用のタブ情報(state、title、image、closedAt、closedId)を作る。表示できる履歴が無ければ null を返す。
- 触るとき: 保存済みタブグループに入るタブの表示名や画像の扱いを変えるとき、または移行時の縮小 state をどう扱うかを確認するとき。
- 呼び出し先: `Date.now()`, `Math.max()`, `Math.min()`
- 参照: `tabState.entries`, `tabState.entries.length`, `tabState.entries[activeIndex].title`, `tabState.entries[activeIndex].url`, `tabState.image`, `tabState.index`, `this.#nextClosedId`

## _SessionStore.#onQuitApplicationGranted()
- 位置: L2543-2666
- 役割: 終了が許可されたとき、全ウィンドウの状態を収集して z 順を付け、RunState を quitting にする。非同期終了では全ウィンドウのフラッシュを待つ(10 秒制限、クラッシュ通知、content-shutdown 通知で打ち切り)。同期終了ではキャッシュ済みの内容だけを保存する。
- 触るとき: 終了時にセッションが最後の状態まで保存されるか、またはフラッシュの待ち時間や打ち切り条件を変えるとき。
- 呼び出し先: `Date.now()`, `lazy.RunState.setQuitting()`, `this.#collectWindowData()`, `this.#log.debug()`, `this.#windowIds.get()`
- 条件付き依存: `if (!syncShutdown)` → `Glean.sessionRestore.shutdownType.async.add()`
- 条件付き依存: `if (!syncShutdown)` → `this.#flushAllWindowsAsync()`
- 条件付き依存: `if (!syncShutdown)` → `Math.max()`
- 条件付き依存: `if (!syncShutdown)` → `this.#looseTimer()`
- 条件付き依存: `if (!syncShutdown)` → `observeTopic()`
- 条件付き依存: `if (!syncShutdown)` → `promises.push()`
- 条件付き依存: `if (!syncShutdown)` → `defers.map()`
- 条件付き依存: `if (!syncShutdown)` → `Promise.race(promises) .then()`
- 条件付き依存: `if (!syncShutdown)` → `Promise.race()`
- 条件付き依存: `if (!syncShutdown)` → `defers.forEach()`
- 条件付き依存: `if (!syncShutdown)` → `deferred.reject()`
- 条件付き依存: `if (!syncShutdown)` → `Services.tm.spinEventLoopUntil()`
- 条件付き依存: `if (!(!syncShutdown))` → `Glean.sessionRestore.shutdownType.sync.add()`
- 参照: `deferred.promise`, `lazy.AsyncShutdown.DELAY_CRASH_MS`, `lazy.SessionSaver.lastSaveTime`, `this.#orderedBrowserWindows`, `this.#windows`, `this.#windows[this.#windowIds.get(window)].zIndex`
- XPCOM: `Services.tm`

## observeTopic()
- 位置: L2591-2627
- 役割: 指定した通知 topic の Observer を登録し、対象の通知が届いたら中断用の Deferred を解決する。登録解除は後で行えるように返す。
- 触るとき: 終了時の待機を打ち切る通知を追加したり、通知購読の後片付けを確認するとき。
- 呼び出し先: `Promise.withResolvers()`, `Services.obs.addObserver()`, `deferred.promise.then()`
- XPCOM: `Services.obs`

## observer()
- 位置: L2593-2616
- 役割: ipc:content-shutdown の abnormal 通知と oop-frameloader-crashed 通知を受けて、該当する場合だけ Deferred を解決し、対応する結果カウンタを記録する。
- 触るとき: クラッシュ時に終了時フラッシュを打ち切る条件を変えるとき。
- 呼び出し先: `Glean.sessionRestore.shutdownFlushAllOutcomes.oop_frameloader_crashed.add()`, `deferred.resolve()`, `subject.QueryInterface()`, `subject.get()`, `this.#log.debug()`
- 条件付き依存: `if (subject.get("abnormal"))` → `this.#log.debug()`
- 条件付き依存: `if (subject.get("abnormal"))` → `Glean.sessionRestore.shutdownFlushAllOutcomes.abnormal_content_shutdown.add()`
- 条件付き依存: `if (subject.get("abnormal"))` → `deferred.resolve()`
- 参照: `Ci.nsIPropertyBag2`
- XPCOM: [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## cleanup()
- 位置: L2617-2623
- 役割: observer の登録を外す。解除に失敗した場合はエラーをログに出す。
- 触るとき: 終了時に登録した Observer が確実に外れるかを確認するとき。
- 呼び出し先: `Services.obs.removeObserver()`, `this.#log.error()`
- XPCOM: `Services.obs`

## _SessionStore.#flushAllWindowsAsync()
- 位置: async L2686-2728
- 役割: 保存中の Flush Promise を集め、全ブラウザウィンドウをフラッシュ開始と同時に見えなくする。各 Promise を順に待ちながら状態を収集し、最後に最前面ウィンドウを記録して DirtyWindows をクリアする。
- 触るとき: 終了時のフラッシュの待ち方や進捗表示を変えるとき、または終了直前のウィンドウ状態がどこで確定するかを追うとき。
- 呼び出し先: `DirtyWindows.clear()`, `Glean.sessionRestore.shutdownFlushAllOutcomes.complete.add()`, `WINDOW_FLUSHING_PROMISES.clear()`, `lazy.TabStateFlusher.flushWindow()`, `this.#getTopWindow()`, `this.#windowIds.get()`, `window.docShell.treeOwner.QueryInterface()`, `windowPromises.set()`
- 条件付き依存: `if (this.#windowIds.get(win) && this.#windows[this.#windowIds.get(win)])` → `this.#collectWindowData()`
- 条件付き依存: `if (activeWindow)` → `this.#windowIds.get()`
- 参照: `Ci.nsIBaseWindow`, `baseWin.visibility`, `progress.current`, `progress.total`, `this.#activeWindowSSiCache`, `this.#browserWindows`, `this.#windows`, `windowPromises.size`
- XPCOM: `nsIBaseWindow`

## _SessionStore.#onLastWindowCloseGranted()
- 位置: L2733-2739
- 役割: 最後のブラウザウィンドウが閉じられることが許可されたとき、次に別のブラウザウィンドウが開いた時点で最後のウィンドウを復元するように #restoreLastWindow を立てる。
- 触るとき: 最後のウィンドウを閉じた後に新しいウィンドウを開いたときの復元挙動を変えるとき。
- 参照: `this.#restoreLastWindow`

## _SessionStore.#onQuitApplication()
- 位置: L2747-2777
- 役割: quit-application 時に、restart または os-restart なら resume_session_once を立てる(OS 再起動時は resuming_after_os_restart も立てる)。restart 以外は前回セッションを破棄し、最後に #uninit で終了処理を行う。
- 触るとき: 再起動・OS 再起動後にセッションを戻すかどうかの判定や、終了種別ごとの前回セッションの扱いを変えるとき。
- 呼び出し先: `this.#uninit()`
- 条件付き依存: `if (!PrivateBrowsingUtils.permanentPrivateBrowsing)` → `this.#prefBranch.getBoolPref()`
- 条件付き依存: `if ( aData == "os-restart" && !this.#prefBranch.getBoolPref("sessionstore.resume_session_once") )` → `this.#prefBranch.setBoolPref()`
- 条件付き依存: `if (!PrivateBrowsingUtils.permanentPrivateBrowsing)` → `this.#prefBranch.setBoolPref()`
- 条件付き依存: `if (aData == "restart" || aData == "os-restart")` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aData != "restart")` → `LastSession.clear()`
- 参照: `PrivateBrowsingUtils.permanentPrivateBrowsing`
- XPCOM: `Services.obs`

## _SessionStore.purgeDataForPrivateWindow()
- 位置: L2784-2821
- 役割: 指定したプライベートウィンドウの閉じたタブと閉じたタブグループのデータを削除し、関連する一覧を初期化する。終了中は何もしない。
- 触るとき: プライベートウィンドウを閉じた後に閉じたタブの履歴が残らないかを確認するとき。
- 呼び出し先: `this.#windowIds.get()`
- 条件付き依存: `if (windowData._closedTabs.length)` → `this.#removeClosedTabData()`
- 条件付き依存: `if (windowData.closedGroups.length)` → `this.#removeClosedTabData()`
- 参照: `closedGroup.tabs`, `closedGroup.tabs.length`, `lazy.RunState.isQuitting`, `this.#closedObjectsChanged`, `this.#windows`, `windowData._closedTabs`, `windowData._closedTabs.length`, `windowData._lastClosedTabGroupCount`, `windowData.closedGroups`, `windowData.closedGroups.length`, `windowData.lastClosedTabGroupId`

## _SessionStore.#onPurgeSessionHistory()
- 位置: L2826-2873
- 役割: セッションファイルを消去し、終了中でなければ前回セッションを破棄する。開いているウィンドウの閉じたタブ・閉じたグループ、閉じたウィンドウ一覧、閉じた操作履歴を消し、閉じたウィンドウの一覧にない古い状態を捨てて保存を走らせる。
- 触るとき: 履歴消去(sanitize)で閉じたタブやウィンドウのデータがどこまで消えるかを変えるとき。
- 呼び出し先: `LastSession.clear()`, `lazy.SessionFile.wipe()`, `this.#clearRestoringWindows()`, `this.#getTopWindow()`, `this.#windowIds.get()`
- 条件付き依存: `if (win)` → `win.setTimeout()`
- 条件付き依存: `if (win)` → `lazy.SessionSaver.run()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.SessionSaver.run()`
- 参照: `lazy.RunState.isQuitting`, `lazy.RunState.isRunning`, `this.#browserWindows`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#lastClosedActions`, `this.#saveableClosedWindowData`, `this.#windows`, `this.#windows[ix]._closedTabs`, `this.#windows[ix]._closedTabs.length`, `this.#windows[ix].closedGroups`, `this.#windows[ix].closedGroups.length`

## _SessionStore.#onPurgeDomainData()
- 位置: L2881-2955
- 役割: 指定ドメインを含む閉じたタブ・グループを、ウィンドウ別と閉じたウィンドウ別に削除する。閉じたウィンドウ内の開いたタブも消し、残りがなければそのウィンドウを削除し、一部だけ消えた場合はタイトルと選択位置を直す。
- 触るとき: サイト単位の履歴消去で閉じたタブやウィンドウのデータが正しく消えるかを確認するとき。
- 呼び出し先: `closedTabs[i].state.entries.some()`, `openTabs[j].entries.some()`, `this.#clearRestoringWindows()`, `this.#closedWindows[ix].closedGroups.map()`, `this.#windows[ix].closedGroups.map()`
- 条件付き依存: `if (closedTabs[i].state.entries.some(containsDomain, this))` → `closedTabs.splice()`
- 条件付き依存: `if (openTabs[j].entries.some(containsDomain, this))` → `openTabs.splice()`
- 条件付き依存: `if (!openTabs.length)` → `this.#closedWindows.splice()`
- 条件付き依存: `if (openTabs.length != openTabCount)` → `this.historyIndex()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `lazy.SessionSaver.run()`
- 参照: `closedTabs.length`, `g.tabs`, `lazy.RunState.isRunning`, `openTabs.length`, `selectedTab.entries`, `selectedTab.entries.length`, `selectedTab.entries[activeIndex].title`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[ix]._closedTabs`, `this.#closedWindows[ix].selected`, `this.#closedWindows[ix].tabs`, `this.#closedWindows[ix].title`, `this.#windows`, `this.#windows[ix]._closedTabs`

## containsDomain()
- 位置: L2883-2894
- 役割: 履歴エントリの URL のホストが指定ドメインに属するかを判定し、子エントリにも再帰的に調べる。URL にホストが無い場合は子エントリだけを調べる。
- 触るとき: ドメイン単位の消去で一致判定の範囲(子エントリを含むか、サブドメインを含むか)を変えるとき。
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `aEntry.children.some()`
- 参照: `Services.io.newURI(aEntry.url).host`, `aEntry.children`, `aEntry.url`
- XPCOM: `Services.eTLD` / `Services.io`

## _SessionStore.#onPrefChange()
- 位置: L2963-3010
- 役割: sessionstore の設定変更を受け、上限値(max_tabs_undo、max_windows_undo)の変更時は超過分を切り詰め、その他の設定値はフィールドに反映して Glean の値も更新する。
- 触るとき: sessionstore の設定を新しく追加したり、設定変更時の即時反映のしかたを変えるとき。
- 呼び出し先: `Glean.sessionRestore.newTabOnRestoreEnabled.set()`, `this.#capClosedWindows()`, `this.#prefBranch.getBoolPref()`, `this.#prefBranch.getIntPref()`
- 条件付き依存: `if (this.#windows[ix]._closedTabs.length > this.#max_tabs_undo)` → `this.#windows[ix]._closedTabs.splice()`
- 参照: `this.#closedObjectsChanged`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedTabsFromClosedWindowsEnabled`, `this.#max_tabs_undo`, `this.#max_windows_undo`, `this.#restore_on_demand`, `this.#windows`, `this.#windows[ix]._closedTabs.length`

## _SessionStore.#onTabAdd()
- 位置: L3018-3020
- 役割: タブが追加されたとき、そのウィンドウの状態保存を遅延予約する。
- 触るとき: 新規タブ追加時に保存のタイミングが適切かを確認するとき。
- 呼び出し先: `this.#saveStateDelayed()`

## _SessionStore.#onTabBrowserInserted()
- 位置: L3030-3048
- 役割: タブの browser に SwapDocShells と oop-browser-crashed などのイベント購読を付け、遅延読み込みのタブが保存済みの状態を持っていれば #restoreTab で復元してから遅延状態を消す。
- 触るとき: 新しいタブの browser が挿入されたときのイベント購読や、遅延タブの復元条件を変えるとき。
- 呼び出し先: `TAB_LAZY_STATES.delete()`, `TAB_LAZY_STATES.has()`, `TAB_STATE_FOR_BROWSER.has()`, `browser.addEventListener()`, `lazy.TabStateCache.get()`
- 条件付き依存: `if ( TAB_LAZY_STATES.has(aTab) && !TAB_STATE_FOR_BROWSER.has(browser) && lazy.TabStateCache.get(browser.permanentKey) )` → `lazy.TabState.clone()`
- 条件付き依存: `if ( TAB_LAZY_STATES.has(aTab) && !TAB_STATE_FOR_BROWSER.has(browser) && lazy.TabStateCache.get(browser.permanentKey) )` → `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if ( TAB_LAZY_STATES.has(aTab) && !TAB_STATE_FOR_BROWSER.has(browser) && lazy.TabStateCache.get(browser.permanentKey) )` → `this.#restoreTab()`
- 参照: `aTab.linkedBrowser`, `browser.permanentKey`

## _SessionStore.#onTabRemove()
- 位置: L3060-3066
- 役割: タブの browser に関する内部状態を後始末し、通知を伴う場合は状態の保存を遅延予約する。
- 触るとき: タブを閉じた後に内部状態が残らないか、または保存が必要かを確認するとき。
- 呼び出し先: `this.#cleanUpRemovedBrowser()`
- 条件付き依存: `if (!aNoNotification)` → `this.#saveStateDelayed()`

## _SessionStore.#onTabClose()
- 位置: L3078-3089
- 役割: max_tabs_undo が 0 でなければ、タブの最新状態を収集して #maybeSaveClosedTab に渡し、閉じたタブとして保存する。
- 触るとき: 閉じたタブの記録が取られる条件や、一括で閉じたタブ(multiselection)の扱いを変えるとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `lazy.TabState.collect()`, `this.#maybeSaveClosedTab()`
- 参照: `this.#max_tabs_undo`

## _SessionStore.#onTabGroupRemoveRequested()
- 位置: L3095-3127
- 役割: タブグループが閉じられるとき、保存済みのグループなら何もせず、そうでなければグループの状態と属するタブ・分割表示のデータを閉じたグループとして先頭に追加し、直前のグループ閉鎖数を更新する。max_tabs_undo が 0 なら何もしない。
- 触るとき: タブグループを閉じたときに閉じたグループ一覧へ入る条件や、保存済みグループの「保存して閉じる」扱いを変えるとき。
- 呼び出し先: `closedGroups.unshift()`, `lazy.TabGroupState.closed()`, `this.#collectClosedTabsForTabGroup()`, `this.#collectSplitViewDataForTabGroup()`, `this.#windowIds.get()`, `this.getSavedTabGroup()`
- 参照: `tabGroup.id`, `tabGroup.tabs`, `tabGroupState.splitViews`, `tabGroupState.tabs`, `tabGroupState.tabs.length`, `this.#closedObjectsChanged`, `this.#max_tabs_undo`, `this.#windows`, `this.#windows[this.#windowIds.get(win)]._lastClosedTabGroupCount`, `this.#windows[this.#windowIds.get(win)].closedGroups`

## _SessionStore.#collectClosedTabsForTabGroup()
- 位置: L3149-3162
- 役割: グループ内の各タブの状態を収集し、必要なら groupId を付け替えて、閉じたタブ用の配列へ #maybeSaveClosedTab 経由で集める。
- 触るとき: 閉じたタブグループに入るタブのデータ形式や groupId の付け替えを変えるとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `lazy.TabState.collect()`, `tabs.forEach()`, `this.#maybeSaveClosedTab()`
- 参照: `tabState.groupId`

## _SessionStore.#collectSplitViewDataForTabGroup()
- 位置: L3168-3178
- 役割: グループ内のタブから分割表示 ID ごとに最初に見つかった状態だけを取り出して配列にする。
- 触るとき: 閉じたグループや保存済みグループに分割表示の情報をどう残すかを変えるとき。
- 呼び出し先: `Array.from()`, `splitViewData.values()`, `tabs.forEach()`
- 条件付き依存: `if (tab.splitview)` → `splitViewData.get()`
- 条件付き依存: `if (!splitViewData.get(tab.splitview.splitViewId))` → `splitViewData.set()`
- 参照: `tab.splitview`, `tab.splitview.splitViewId`, `tab.splitview.state`

## _SessionStore.#onMoveToNewWindow()
- 位置: L3188-3198
- 役割: 移動元 browser をフラッシュしてからタブ状態をキャッシュし、移動先 browser の permanentKey に複製する。移動元の状態が無ければ例外を投げる。
- 触るとき: タブを新しいウィンドウへ移したときに状態が引き継がれるかを確認するとき。
- 呼び出し先: `lazy.TabStateCache.get()`, `lazy.TabStateCache.update()`, `lazy.TabStateFlusher.flush()`, `lazy.TabStateFlusher.flush(aFromBrowser).then()`
- 参照: `aFromBrowser.permanentKey`, `aToBrowser.permanentKey`

## _SessionStore.#maybeSaveClosedTab()
- 位置: L3219-3270
- 役割: プライベートタブや FirefoxView のタブは除外し、保存対象ならタブの情報を閉じたタブ用の配列へ保存する。どの場合も closingTabMap に登録して、閉じた後に届く最後の更新を扱えるようにする。
- 触るとき: 閉じたタブが記録される条件(プライベートや FirefoxView の除外)を変えるとき。
- 呼び出し先: `Date.now()`, `PrivateBrowsingUtils.isWindowPrivate()`, `aWindow.gBrowser.getIcon()`, `this.#closingTabMap.set()`, `this.#shouldSaveTabState()`, `this.#windowIds.get()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.#saveClosedTabData()`
- 参照: `aTab.index`, `aTab.label`, `aTab.linkedBrowser.permanentKey`, `aWindow.FirefoxViewHandler.tab`, `tabState.groupId`, `tabState.isPrivate`, `this.#windows`, `winData._closedTabs`

## _SessionStore.resetBrowserToLazyState()
- 位置: L3279-3335
- 役割: 接続中の browser をタブ閉鎖時と同様に後始末し、pending と crashed の属性を立て直し、入力中の URL をキャッシュに補ってから遅延状態(TAB_LAZY_STATES)に戻す。
- 触るとき: タブを破棄して遅延状態に戻す(discard)処理の結果、次に開いたとき正しい URL で復元されるかを調べるとき。
- 呼び出し先: `TAB_LAZY_STATES.set()`, `aTab.removeAttribute()`, `aTab.setAttribute()`, `browser.didStartLoadSinceLastUserTyping()`, `lazy.TabStateCache.get()`, `this.#cleanUpRemovedBrowser()`, `this.#crashedBrowsers.delete()`
- 条件付き依存: `if (shouldUpdateCacheState)` → `lazy.TabStateCache.update()`
- 参照: `aTab.label`, `aTab.linkedBrowser`, `browser.currentURI.spec`, `browser.isConnected`, `browser.permanentKey`, `cacheState.userTypedValue`

## _SessionStore.maybeExitCrashedState()
- 位置: L3345-3350
- 役割: browser の文書が about:tabcrashed なら、クラッシュ中の集合から外して更新メッセージを再び受け付けるようにする。
- 触るとき: クラッシュしたタブが別ページへ移動して復活した後に状態保存が再開されるかを確認するとき。
- 呼び出し先: `uri?.spec?.startsWith()`
- 条件付き依存: `if (uri?.spec?.startsWith("about:tabcrashed"))` → `this.#crashedBrowsers.delete()`
- 参照: `aBrowser.documentURI`, `aBrowser.permanentKey`

## _SessionStore.isBrowserInCrashedSet()
- 位置: L3358-3365
- 役割: デバッグモード時だけ、browser がクラッシュ中の集合に入っているかを返す。デバッグモード以外では例外を投げる。
- 触るとき: テストでクラッシュ状態の遷移を検証する箇所を書くとき。
- 条件付き依存: `if (gDebuggingEnabled)` → `this.#crashedBrowsers.has()`
- 参照: `aBrowser.permanentKey`

## _SessionStore.#cleanUpRemovedBrowser()
- 位置: L3373-3390
- 役割: browser の SwapDocShells と oop-browser-crashed などの購読を外し、復元中・復元待ちの状態を戻す。復元中だったタブなら次のタブの復元を始める。
- 触るとき: タブを閉じたり遅延状態に戻したときに復元キューが止まらないかを確認するとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `browser.removeEventListener()`
- 条件付き依存: `if (previousState)` → `this.#resetTabRestoringState()`
- 条件付き依存: `if (previousState == TAB_STATE_RESTORING)` → `this.#restoreNextTab()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.#saveClosedTabData()
- 位置: L3406-3455
- 役割: 閉じたタブを closedAt の新しい順に挿入して ID を振り、グループ外のタブは max_tabs_undo を超えた分を切り詰める。グループ内の閉鎖数と closedAt を更新し、必要なら閉じた操作の履歴にも追加する。
- 触るとき: 閉じたタブの並び順や上限の扱い、タブグループ内の閉鎖数の数え方を変えるとき。
- 呼び出し先: `closedTabs.findIndex()`, `closedTabs.splice()`
- 条件付き依存: `if (saveAction)` → `this.#addClosedAction()`
- 条件付き依存: `if ( !tabData.closedInTabGroupId && closedTabs.length > this.#max_tabs_undo )` → `closedTabs.splice()`
- 参照: `closedTabs.length`, `tab.closedAt`, `tabData.closedAt`, `tabData.closedId`, `tabData.closedInGroup`, `tabData.closedInTabGroupId`, `this.#closedObjectsChanged`, `this.#max_tabs_undo`, `this.#nextClosedId`, `this.LAST_ACTION_CLOSED_TAB`, `winData._lastClosedTabGroupCount`, `winData.lastClosedTabGroupId`

## _SessionStore.#removeClosedTabData()
- 位置: L3470-3494
- 役割: 閉じたタブ一覧から指定位置のタブを取り除き、最終更新待ちの closingTabMap などの登録も外して、閉じた操作の履歴からも削除する。
- 触るとき: 閉じたタブを開き直す、または忘れるときに、最終更新が後から戻ってきて再登録されないかを確認するとき。
- 呼び出し先: `closedTabs.splice()`, `this.#removeClosedAction()`
- 条件付き依存: `if (closedTab.permanentKey)` → `this.#closingTabMap.delete()`
- 条件付き依存: `if (closedTab.permanentKey)` → `this.#tabClosingByWindowMap.delete()`
- 参照: `closedTab.closedId`, `closedTab.permanentKey`, `this.#closedObjectsChanged`, `this.LAST_ACTION_CLOSED_TAB`, `winData._lastClosedTabGroupCount`

## _SessionStore.#onTabSelect()
- 位置: L3502-3510
- 役割: 稼働中ならウィンドウの選択タブ位置を更新し、選ばれたタブの内容が未復元なら復元を始める。
- 触るとき: タブを切り替えたときに遅延タブの内容が読み込まれるタイミングを変えるとき。
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#maybeRestoreTabContent()`
- 参照: `aWindow.gBrowser.selectedTab`, `aWindow.gBrowser.tabContainer.selectedIndex`, `lazy.RunState.isRunning`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].selected`

## _SessionStore.#maybeRestoreTabContent()
- 位置: L3515-3534
- 役割: タブが未復元(NEEDS_RESTORE)の場合、クラッシュ画面を表示すべきならクラッシュ状態に入り、そうでなければ #restoreTabContent で中身を復元する。
- 触るとき: 遅延タブを表示した時点でクラッシュ画面と通常復元のどちらを出すかを変えるとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.get(browser) == TAB_STATE_NEEDS_RESTORE)` → `lazy.TabCrashHandler.willShowCrashedTab()`
- 条件付き依存: `if (lazy.TabCrashHandler.willShowCrashedTab(browser))` → `this.#enterCrashedState()`
- 条件付き依存: `if (!(lazy.TabCrashHandler.willShowCrashedTab(browser)))` → `this.#restoreTabContent()`
- 参照: `tab.linkedBrowser`

## _SessionStore.#onTabShow()
- 位置: L3540-3556
- 役割: 未復元のタブが表示されたら TabRestoreQueue の隠れ→表示の区分を移し、復元キューを進める。その後、状態の保存を遅延予約する。
- 触るとき: 非表示タブの復元(restore_hidden_tabs)の順番や、表示切り替え時の保存タイミングを変えるとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `this.#saveStateDelayed()`
- 条件付き依存: `if ( TAB_STATE_FOR_BROWSER.get(aTab.linkedBrowser) == TAB_STATE_NEEDS_RESTORE )` → `TabRestoreQueue.hiddenToVisible()`
- 条件付き依存: `if ( TAB_STATE_FOR_BROWSER.get(aTab.linkedBrowser) == TAB_STATE_NEEDS_RESTORE )` → `this.#restoreNextTab()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.#onTabHide()
- 位置: L3562-3574
- 役割: 未復元のタブが隠されたら TabRestoreQueue の表示→隠れ区分を移し、状態の保存を遅延予約する。
- 触るとき: タブを非表示にしたときに復元キュー上の位置がどう変わるかを確認するとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `this.#saveStateDelayed()`
- 条件付き依存: `if ( TAB_STATE_FOR_BROWSER.get(aTab.linkedBrowser) == TAB_STATE_NEEDS_RESTORE )` → `TabRestoreQueue.visibleToHidden()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.#onBrowserCrashed()
- 位置: L3582-3587
- 役割: browser のクラッシュを #enterCrashedState に渡し、返ってこないフラッシュ要求を解決する。
- 触るとき: タブのクラッシュ時にフラッシュ待ちが止まらないかを確認するとき。
- 呼び出し先: `lazy.TabStateFlusher.resolveAll()`, `this.#enterCrashedState()`

## _SessionStore.#enterCrashedState()
- 位置: L3597-3612
- 役割: browser をクラッシュ中の集合に加え、未復元または復元途中だった場合はタブの復元状態を戻して、後で復活させたときに再度復元できるようにする。
- 触るとき: クラッシュしたタブを復活させた後に内容がもう一度復元されるかを調べるとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`, `this.#crashedBrowsers.add()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.has(browser))` → `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (tab)` → `this.#resetLocalTabRestoringState()`
- 参照: `browser.documentGlobal`, `browser.permanentKey`

## _SessionStore.#onIdleDaily()
- 位置: L3617-3642
- 役割: アイドル時の日次処理で、閉じたウィンドウ・その閉じたタブ・閉じたグループ、開いているウィンドウの閉じたタブ・閉じたグループについて古いものを削除する。保存は再予約しない。
- 触るとき: 閉じた項目の保持期間を変えるとき、または日次の掃除が閉じた項目の一覧にどう効くかを調べるとき。
- 呼び出し先: `Object.keys()`, `Object.keys(this.#windows).map()`, `this.#cleanupOldData()`, `this.#closedWindows.map()`, `this.#notifyOfClosedObjectsChange()`
- 参照: `this.#closedWindows`, `this.#windows`, `this.#windows[key]._closedTabs`, `this.#windows[key].closedGroups`, `winData._closedTabs`, `winData.closedGroups`

## _SessionStore.#cleanupOldData()
- 位置: L3645-3664
- 役割: sessionstore.cleanup.forget_closed_after を保持期間として、渡された各配列を後ろから見て期間を過ぎた項目を削除する。closedAt が無い項目には今の時刻を入れる。
- 触るとき: 閉じた項目を何日残すかの判定や、closedAt が無い古いデータの扱いを変えるとき。
- 呼び出し先: `Date.now()`, `this.#prefBranch.getIntPref()`
- 条件付き依存: `if (now - data.closedAt > TIME_TO_LIVE)` → `array.splice()`
- 参照: `array.length`, `data.closedAt`, `this.#closedObjectsChanged`

## _SessionStore.getBrowserState()
- 位置: L3673-3683
- 役割: 現在の状態を JSON 文字列にして返す。前回セッションの状態と遅延初期状態は含めない。
- 触るとき: nsISessionStore の getBrowserState の戻り値の形を変えるとき、またはテストで状態を取得する経路を追うとき。
- 呼び出し先: `JSON.stringify()`, `this.getCurrentState()`
- 参照: `state.deferredInitialState`, `state.lastSessionState`

## _SessionStore.setBrowserState()
- 位置: L3699-3765
- 役割: テストや自動化用に、JSON の状態を受け取って他のブラウザウィンドウを閉じ、閉じたウィンドウ一覧を空にしてから全ウィンドウを復元する。state が無効なら例外を投げる。
- 触るとき: テストで状態を丸ごと差し替える手順や、setBrowserState 時に閉じたデータがどう消えるかを変えるとき。
- 呼び出し先: `JSON.parse()`, `lazy.SessionCookies.restore()`, `this.#getTopWindow()`, `this.#globalState.setFromState()`, `this.#handleClosedWindows()`, `this.#initSplitViewIds()`, `this.#notifyOfClosedObjectsChange()`, `this.#resetRestoringState()`, `this.#restoreWindows()`
- 条件付き依存: `if (!state)` → `Components.Exception()`
- 条件付き依存: `if (!state.windows)` → `Components.Exception()`
- 条件付き依存: `if (!window)` → `this.#openWindowWithState()`
- 条件付き依存: `if (otherWin != window)` → `otherWin.close()`
- 条件付き依存: `if (otherWin != window)` → `this.#onClose()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `state.cookies`, `state.windows`, `state.windows.length`, `this.#browserSetState`, `this.#browserWindows`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#maxSplitViewId`, `this.#restoreCount`

## _SessionStore.getWindowState()
- 位置: L3772-3786
- 役割: 追跡中のウィンドウならその状態を、終了直前のキャッシュにあればその状態を、どちらも無ければ例外を返す。
- 触るとき: ウィンドウ単位の状態取得で、閉じかけのウィンドウの扱いを確認するとき。
- 呼び出し先: `Components.Exception()`, `DyingWindowCache.has()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `Cu.cloneInto()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#getWindowState()`
- 条件付き依存: `if (DyingWindowCache.has(aWindow))` → `DyingWindowCache.get()`
- 条件付き依存: `if (DyingWindowCache.has(aWindow))` → `Cu.cloneInto()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`

## _SessionStore.setWindowState()
- 位置: L3799-3814
- 役割: 追跡中のウィンドウに対して、渡された状態を復元する。上書きの指定を渡せる。
- 触るとき: 既存ウィンドウへの状態の流し込みの挙動を変えるとき。
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#restoreWindows()`, `this.#windowIds.get()`
- 条件付き依存: `if (!this.#windowIds.get(aWindow))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`

## _SessionStore.getTabState()
- 位置: L3826-3840
- 役割: タブが追跡中のウィンドウに属していれば、そのタブの状態を収集して JSON 文字列で返す。無効なタブや未追跡なら例外を投げる。
- 触るとき: タブ単位の状態取得の形式や、追跡されていないタブの扱いを変えるとき。
- 呼び出し先: `JSON.stringify()`, `TAB_CUSTOM_VALUES.get()`, `lazy.TabState.collect()`, `this.#windowIds.get()`
- 条件付き依存: `if (!aTab || !aTab.documentGlobal)` → `Components.Exception()`
- 条件付き依存: `if (!this.#windowIds.get(aTab.documentGlobal))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTab.documentGlobal`

## _SessionStore.setTabState()
- 位置: L3853-3899
- 役割: JSON または object のタブ状態を検証し(entries が必要)、追跡中のウィンドウのタブへ復元する。復元中ならリセットしてから #restoreTab を呼ぶ。
- 触るとき: タブ状態の入力検証の条件や、復元中のタブを差し替える経路を変えるとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`, `this.#ensureNoNullsInTabDataList()`, `this.#notifyOfClosedObjectsChange()`, `this.#restoreTab()`, `this.#windowIds.get()`, `this.#windowIds.has()`
- 条件付き依存: `if (typeof tabState == "string")` → `JSON.parse()`
- 条件付き依存: `if (!tabState)` → `Components.Exception()`
- 条件付き依存: `if (typeof tabState != "object")` → `Components.Exception()`
- 条件付き依存: `if (!("entries" in tabState))` → `Components.Exception()`
- 条件付き依存: `if (!window || !this.#windowIds.has(window))` → `Components.Exception()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.has(aTab.linkedBrowser))` → `this.#resetTabRestoringState()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTab.documentGlobal`, `aTab.index`, `aTab.linkedBrowser`, `this.#windows`, `this.#windows[this.#windowIds.get(window)].tabs`, `window.gBrowser.tabs`

## _SessionStore.isTabRestoring()
- 位置: L3907-3909
- 役割: タブの browser が復元状態(TAB_STATE_FOR_BROWSER)を持つかを返す。
- 触るとき: タブが復元中かどうかの判定を呼び出し側で使う箇所を調べるとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`
- 参照: `aTab.linkedBrowser`

## _SessionStore.getInternalObjectState()
- 位置: L3918-3926
- 役割: ウィンドウ ID があればそのウィンドウの内部データを、なければ loadURI を持つ browser なら復元状態、それ以外はタブのカスタム値を返す。
- 触るとき: テストや内部確認で、ウィンドウ・browser・タブごとの内部状態をどこから読むかを調べるとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `TAB_STATE_FOR_BROWSER.get()`, `this.#windowIds.get()`
- 参照: `this.#windows`

## _SessionStore.getObjectTypeForClosedId()
- 位置: L3933-3939
- 役割: 指定の closedId が閉じたウィンドウに一致すれば "window"、そうでなければ "tab" を返す。
- 触るとき: 閉じた項目の ID から種別を引く呼び出し元(sessions.restore など)の挙動を変えるとき。
- 呼び出し先: `this.#getClosedWindowDataByClosedId()`
- 参照: `this.LAST_ACTION_CLOSED_TAB`, `this.LAST_ACTION_CLOSED_WINDOW`

## _SessionStore.#getClosedWindowDataByClosedId()
- 位置: L3945-3949
- 役割: 閉じたウィンドウ一覧から closedId が一致する最初のデータを返す。無ければ undefined。
- 触るとき: 閉じたウィンドウを ID で探す箇所の挙動を変えるとき。
- 呼び出し先: `this.#closedWindows.find()`
- 参照: `closedData.closedId`

## _SessionStore.getWindowId()
- 位置: L3964-3966
- 役割: ウィンドウに振られた SessionStore の ID を返す。未登録なら null を返す。
- 触るとき: ウィンドウ ID を外部に渡す箇所や、再開時に ID が変わる条件を確認するとき。
- 呼び出し先: `this.#windowIds.get()`

## _SessionStore.getWindowById()
- 位置: L3973-3982
- 役割: 開いているブラウザウィンドウの中から SessionStore の ID が一致するものを返す。無ければ undefined。
- 触るとき: ID からウィンドウを逆引きする呼び出し元の挙動を確認するとき。
- 呼び出し先: `this.#windowIds.get()`
- 参照: `this.#browserWindows`

## _SessionStore.duplicateTab()
- 位置: L4007-4100
- 役割: ウィンドウに新しいタブを作り、元タブの状態をフラッシュ後にキャッシュから取り込んで、履歴位置を aDelta だけずらし固定化を解いたうえで復元する。背景指定ならフォーカスを移さない。
- 触るとき: タブの複製で履歴位置の初期値や背景での開き方を変えるとき、またはフラッシュ前の状態が複製に入る経路を調べるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `TAB_CUSTOM_VALUES.get()`, `aTab.getAttribute()`, `aWindow.gBrowser.addTrustedTab()`, `aWindow.gBrowser.setDefaultIcon()`, `lazy.TabState.collect()`, `lazy.TabState.copyFromCache()`, `lazy.TabStateFlusher.flush()`, `lazy.TabStateFlusher.flush(browser).then()`, `this.#restoreTab()`, `this.#windowIds.get()`, `uriObj.schemeIs()`
- 条件付き依存: `if (!aTab || !aTab.documentGlobal)` → `Components.Exception()`
- 条件付き依存: `if (!this.#windowIds.get(aTab.documentGlobal))` → `Components.Exception()`
- 条件付き依存: `if (!aWindow.gBrowser)` → `Components.Exception()`
- 条件付き依存: `if (!uriObj || (uriObj && !uriObj.schemeIs("about")))` → `newTab.setAttribute()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTab.documentGlobal`, `aTab.group`, `aTab.linkedBrowser`, `aTab.linkedBrowser.currentURI`, `aTab.linkedBrowser.remoteType`, `aWindow.gBrowser`, `aWindow.gBrowser.selectedTab`, `browser.permanentKey`, `newTab.closing`, `newTab.documentGlobal`, `newTab.linkedBrowser`, `tabState.entries.length`, `tabState.index`, `tabState.pinned`, `window.closed`

## _SessionStore.getWindows()
- 位置: L4110-4125
- 役割: 指定ウィンドウ(省略時は最前面)と同じプライベート状態のブラウザウィンドウ一覧を返す。
- 触るとき: プライベート・非プライベートで対象を絞る呼び出し元の挙動を確認するとき。
- 呼び出し先: `Array.from()`, `Array.from(this.#browserWindows).filter()`, `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!aWindowOrOptions)` → `this.#getTopWindow()`
- 条件付き依存: `if (aWindowOrOptions instanceof Ci.nsIDOMWindow)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!(aWindowOrOptions instanceof Ci.nsIDOMWindow))` → `Boolean()`
- 参照: `Ci.nsIDOMWindow`, `aWindowOrOptions.private`, `this.#browserWindows`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md)

## _SessionStore.getWindowForTabClosedId()
- 位置: L4133-4151
- 役割: 非プライベートのウィンドウを先に、aIncludePrivate が真ならプライベートも順に調べ、その closedId の閉じたタブを持つウィンドウを返す。無ければ undefined。
- 触るとき: 閉じたタブの ID から持ち主のウィンドウを探す検索順序を変えるとき。
- 呼び出し先: `closedTabs.find()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#windowIds.get()`, `this.getWindows()`
- 参照: `closedTabs.length`, `tab.closedId`, `this.#windows`

## _SessionStore.getLastClosedTabCount()
- 位置: L4163-4175
- 役割: 直近に一緒に閉じたタブ数を、グループ閉鎖数の下限 1 と閉じたタブ数の上限で挟んで返す。未追跡のウィンドウなら例外を投げる。
- 触るとき: 複数タブを一括で閉じた後の「閉じたタブを開き直す」の件数表示を変えるとき。
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `Math.min()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `Math.max()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.getClosedTabCountForWindow()`
- 参照: `Components.returnCode`, `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._lastClosedTabGroupCount`

## _SessionStore.resetLastClosedTabCount()
- 位置: L4184-4191
- 役割: 追跡中のウィンドウについて、直近の一括閉鎖数を -1、直近のグループ ID を null に戻す。未追跡なら例外。
- 触るとき: 一括閉鎖の記録をどの操作でリセットするかを確認するとき。
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 参照: `Components.returnCode`, `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._lastClosedTabGroupCount`, `this.#windows[this.#windowIds.get(aWindow)].lastClosedTabGroupId`

## _SessionStore.getClosedTabCountForWindow()
- 位置: L4198-4215
- 役割: 追跡中のウィンドウ、または終了直前のキャッシュにあるウィンドウについて、閉じたタブとグループ内のタブの合計数を返す。どちらにも無ければ例外。
- 触るとき: ウィンドウ単位の閉じたタブ数の数え方を変えるとき。
- 呼び出し先: `DyingWindowCache.get()`, `DyingWindowCache.has()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!DyingWindowCache.has(aWindow))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#getStateForClosedTabsAndClosedGroupTabs( DyingWindowCache.get(aWindow) ).length`, `this.#getStateForClosedTabsAndClosedGroupTabs( this.#windows[this.#windowIds.get(aWindow)] ).length`, `this.#windows`

## _SessionStore.#prepareClosedTabOptions()
- 位置: L4222-4248
- 役割: オプションに既定値(全ウィンドウ対象、閉じたウィンドウ対象の設定値)を補い、元ウィンドウが無ければ最前面を使い、プライベート指定を決める。
- 触るとき: 閉じたタブの取得 API に渡すオプションの既定値を変えるとき。
- 呼び出し先: `Object.assign()`, `sourceOptions.hasOwnProperty()`
- 条件付き依存: `if (!sourceOptions.sourceWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if (!sourceOptions.hasOwnProperty("private"))` → `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `sourceOptions.private`, `sourceOptions.sourceWindow`, `this.#closedTabsFromAllWindowsEnabled`, `this.#closedTabsFromClosedWindowsEnabled`

## _SessionStore.getClosedTabCount()
- 位置: L4256-4272
- 役割: オプションに従って、対象ウィンドウ(全ウィンドウか元ウィンドウだけか)の閉じたタブ数と、閉じたウィンドウ由来の数を合計する。
- 触るとき: 閉じたタブ数の表示や判定に使われる件数の範囲を変えるとき。
- 呼び出し先: `this.#prepareClosedTabOptions()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows({ private: sourceOptions.private }) .map(win => this.getClosedTabCountForWindow(win)) .reduce()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows({ private: sourceOptions.private }) .map()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getClosedTabCountForWindow()`
- 条件付き依存: `if (!(sourceOptions.closedTabsFromAllWindows))` → `this.getClosedTabCountForWindow()`
- 条件付き依存: `if (!sourceOptions.private && sourceOptions.closedTabsFromClosedWindows)` → `this.getClosedTabCountFromClosedWindows()`
- 参照: `sourceOptions.closedTabsFromAllWindows`, `sourceOptions.closedTabsFromClosedWindows`, `sourceOptions.private`, `sourceOptions.sourceWindow`

## _SessionStore.getClosedTabCountFromClosedWindows()
- 位置: L4280-4287
- 役割: 閉じたウィンドウ一覧の各ウィンドウについて、閉じたタブとグループ内タブの数を合計して返す。
- 触るとき: 閉じたウィンドウから復元できるタブ数の計算を調べるとき。
- 呼び出し先: `this.#closedWindows .map()`, `this.#closedWindows .map( winData => this.#getStateForClosedTabsAndClosedGroupTabs(winData).length ) .reduce()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 参照: `this.#getStateForClosedTabsAndClosedGroupTabs(winData).length`

## _SessionStore.getClosedTabDataForWindow()
- 位置: L4297-4302
- 役割: 指定ウィンドウの閉じたタブとグループ内タブのデータを、複製して配列で返す。
- 触るとき: 閉じたタブの一覧を呼び出し元に渡す形式を変えるとき。
- 呼び出し先: `this.#getClonedDataForWindow()`
- 参照: `this.#getStateForClosedTabsAndClosedGroupTabs`

## _SessionStore.getClosedTabData()
- 位置: L4310-4323
- 役割: オプションに従い、全ウィンドウまたは元ウィンドウの閉じたタブデータを連結して返す。
- 触るとき: 閉じたタブの一覧の取得範囲を変えるとき。
- 呼び出し先: `this.#prepareClosedTabOptions()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `closedTabData.push()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getClosedTabDataForWindow()`
- 条件付き依存: `if (!(sourceOptions.closedTabsFromAllWindows))` → `closedTabData.push()`
- 条件付き依存: `if (!(sourceOptions.closedTabsFromAllWindows))` → `this.getClosedTabDataForWindow()`
- 参照: `sourceOptions.closedTabsFromAllWindows`, `sourceOptions.private`, `sourceOptions.sourceWindow`

## _SessionStore.getClosedTabDataFromClosedWindows()
- 位置: L4331-4347
- 役割: 閉じたウィンドウ一覧の各ウィンドウの閉じたタブを複製し、元の閉じたウィンドウ ID(sourceClosedId)を付けて連結する。並び替えは行わない。
- 触るとき: 閉じたウィンドウ由来のタブ一覧に元ウィンドウを示す情報を足すとき、または並び順の責務を確認するとき。
- 呼び出し先: `Cu.cloneInto()`, `closedTabData.push()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 参照: `tabData.sourceClosedId`, `this.#closedWindows`, `winData.closedId`

## _SessionStore.getClosedTabGroups()
- 位置: L4356-4389
- 役割: オプションに従い、対象ウィンドウの閉じたタブグループを複製して返す。閉じたウィンドウ由来のグループには元ウィンドウの closedId を各タブに付ける。
- 触るとき: 閉じたタブグループの一覧に含める範囲や、元ウィンドウ情報の付け方を変えるとき。
- 呼び出し先: `this.#prepareClosedTabOptions()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.getWindows()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `closedTabGroups.push()`
- 条件付き依存: `if (sourceOptions.closedTabsFromAllWindows)` → `this.#getClonedDataForWindow()`
- 条件付き依存: `if (sourceOptions.sourceWindow.closedGroups)` → `closedTabGroups.push()`
- 条件付き依存: `if (sourceOptions.sourceWindow.closedGroups)` → `this.#getClonedDataForWindow()`
- 条件付き依存: `if (sourceOptions.closedTabsFromClosedWindows)` → `this.getClosedWindowData()`
- 条件付き依存: `if (sourceOptions.closedTabsFromClosedWindows)` → `closedTabGroups.push()`
- 参照: `groupData.tabs`, `sourceOptions.closedTabsFromAllWindows`, `sourceOptions.closedTabsFromClosedWindows`, `sourceOptions.private`, `sourceOptions.sourceWindow`, `sourceOptions.sourceWindow.closedGroups`, `tabData.sourceClosedId`, `w.closedGroups`, `winData.closedGroups`, `winData.closedId`

## _SessionStore.getLastClosedTabGroupId()
- 位置: L4396-4402
- 役割: 追跡中のウィンドウについて、直近に閉じたタブグループの ID を返す。未追跡なら例外。
- 触るとき: 直近に閉じたグループを「開き直す」対象として特定する処理を調べるとき。
- 呼び出し先: `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 参照: `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].lastClosedTabGroupId`

## _SessionStore.#getClonedDataForWindow()
- 位置: L4414-4436
- 役割: 追跡中のウィンドウ、無ければ終了直前のキャッシュから状態を取り、selector で選んだ部分を FormData を含めて複製して返す。どちらにも無ければ例外。
- 触るとき: ウィンドウ状態の一部を外部に渡す際の複製方法や、閉じかけウィンドウの扱いを変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `DyingWindowCache.get()`, `DyingWindowCache.has()`, `selector()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (!winData && !DyingWindowCache.has(aWindow))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`

## _SessionStore.#getStateForClosedTabsAndClosedGroupTabs()
- 位置: L4449-4485
- 役割: _closedTabs とグループ内タブを closedAt の降順に並べた 1 本の配列にまとめ、各要素に元の位置(_originalStateIndex、グループなら _originalGroupStateIndex)を記録する。
- 触るとき: 閉じたタブの統一インデックス(closedId 以外の並び)の作り方を変えるとき、または閉じたタブ操作の番号がずれる原因を調べるとき。
- 条件付き依存: `if ( groupIdx < closedGroups.length && (tabIdx >= closedTabs.length || group?.closedAt > tab?.closedAt) )` → `group.tabs.forEach()`
- 条件付き依存: `if ( groupIdx < closedGroups.length && (tabIdx >= closedTabs.length || group?.closedAt > tab?.closedAt) )` → `result.push()`
- 条件付き依存: `if (!( groupIdx < closedGroups.length && (tabIdx >= closedTabs.length || group?.closedAt > tab?.closedAt) ))` → `result.push()`
- 参照: `closedGroups.length`, `closedTabs.length`, `group?.closedAt`, `groupTab._originalGroupStateIndex`, `groupTab._originalStateIndex`, `tab._originalStateIndex`, `tab?.closedAt`, `winData._closedTabs`, `winData.closedGroups`

## _SessionStore.#getClosedTabStateFromUnifiedIndex()
- 位置: L4500-4511
- 役割: 統一インデックスの要素から、元の閉じたタブ配列(グループ内なら該当グループの tabs)と、その中の位置を取り出す。
- 触るとき: 統一インデックスで指した閉じたタブを実際にどの配列から取り除くかを確認するとき。
- 参照: `sourceWinData._closedTabs`, `sourceWinData.closedGroups`, `sourceWinData.closedGroups[tabState._originalGroupStateIndex].tabs`, `tabState._originalGroupStateIndex`, `tabState._originalStateIndex`

## _SessionStore.undoCloseTab()
- 位置: L4524-4600
- 役割: 指定した閉じたタブを統一インデックスで取り出して閉じた一覧から外し、ユーザーコンテキストやグループを引き継いだ新しいタブを対象ウィンドウに作って状態を復元する。プライバシーが違う場合は例外。
- 触るとき: 「閉じたタブを開き直す」の挙動、対象ウィンドウの選び方、プライベートの扱いを変えるとき。
- 呼び出し先: `Boolean()`, `PrivateBrowsingUtils.isWindowPrivate()`, `tabbrowser.addTrustedTab()`, `tabbrowser.tabGroups.find()`, `this.#cleanupOrphanedClosedGroups()`, `this.#getClosedTabStateFromUnifiedIndex()`, `this.#getPreferredRemoteType()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedTabData()`, `this.#resolveClosedDataSource()`, `this.#restoreTab()`, `this.#windowIds.get()`
- 条件付き依存: `if (aTargetWindow && !this.#windowIds.get(aTargetWindow))` → `Components.Exception()`
- 条件付き依存: `if (!aTargetWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if ( isPrivateSource !== PrivateBrowsingUtils.isWindowPrivate(aTargetWindow) )` → `Components.Exception()`
- 条件付き依存: `if (!closedTabState)` → `Components.Exception()`
- 条件付き依存: `if (state.entries?.length)` → `this.historyIndex()`
- 条件付き依存: `if (state.entries?.length)` → `Math.min()`
- 条件付き依存: `if (state.entries?.length)` → `Math.max()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `aTargetWindow.gBrowser`, `g.id`, `sourceWinData.isPrivate`, `state.entries`, `state.entries.length`, `state.entries?.length`, `state.entries[activeIndex].url`, `state.groupId`, `state.pinned`, `state.userContextId`, `tabbrowser.selectedTab`

## _SessionStore.undoClosedTabFromClosedWindow()
- 位置: L4613-4627
- 役割: 閉じたウィンドウ内で closedId が一致する項目を探し、その統一インデックスで undoCloseTab に渡す。見つからなければ例外。
- 触るとき: 閉じたウィンドウ由来のタブを closedId で開き直す経路を変えるとき。
- 呼び出し先: `Components.Exception()`, `closedTabs.findIndex()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`, `this.#resolveClosedDataSource()`
- 条件付き依存: `if (closedIndex >= 0)` → `this.undoCloseTab()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `tabData.closedId`

## _SessionStore.#getPreferredRemoteType()
- 位置: L4629-4634
- 役割: URL とユーザーコンテキストから、そのタブが使うべきリモートタイプを ChromeUtils で予測して返す。
- 触るとき: タブを開き直すときにプロセス切り替えが起きないよう、リモートタイプの予測条件を変えるとき。
- 呼び出し先: `ChromeUtils.predictRemoteTypeForURI()`

## _SessionStore.#resolveClosedDataSource()
- 位置: L4640-4664
- 役割: ウィンドウ、sourceWindow、sourceClosedId、sourceWindowId のいずれかから、対応するウィンドウの状態データを取り出す。どれにも当たらなければ例外。
- 触るとき: 閉じたタブ API に渡される呼び出し元の指定方法(ウィンドウ、閉じた ID、ウィンドウ ID)を追加・変更するとき。
- 条件付き依存: `if (aSource instanceof Ci.nsIDOMWindow)` → `this.#getWindowStateData()`
- 条件付き依存: `if (aSource.sourceWindow instanceof Ci.nsIDOMWindow)` → `this.#getWindowStateData()`
- 条件付き依存: `if (typeof aSource.sourceClosedId == "number")` → `this.#getClosedWindowDataByClosedId()`
- 条件付き依存: `if (!winData)` → `Components.Exception()`
- 条件付き依存: `if (typeof aSource.sourceWindowId == "string")` → `this.getWindowById()`
- 条件付き依存: `if (typeof aSource.sourceWindowId == "string")` → `this.#getWindowStateData()`
- 条件付き依存: `if (!(typeof aSource.sourceWindowId == "string"))` → `Components.Exception()`
- 参照: `Ci.nsIDOMWindow`, `Cr.NS_ERROR_INVALID_ARG`, `aSource.sourceClosedId`, `aSource.sourceWindow`, `aSource.sourceWindowId`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md)

## _SessionStore.forgetClosedTab()
- 位置: L4677-4693
- 役割: 指定した位置の閉じたタブを、そのウィンドウの閉じたタブ一覧から削除する。範囲外なら例外を投げる。
- 触るとき: 閉じたタブを一覧から消す操作で、開き直せなくなる範囲を確認するとき。
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedTabData()`, `this.#resolveClosedDataSource()`
- 条件付き依存: `if (!(aIndex in winData._closedTabs))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `winData._closedTabs`

## _SessionStore.forgetClosedTabGroup()
- 位置: L4707-4728
- 役割: 指定 ID の閉じたタブグループを探し、そのタブを閉じた一覧から全部外してからグループ自体を削除する。見つからなければ例外。
- 触るとき: 閉じたタブグループを一覧から消したとき、中のタブも開き直せなくなるかを確認するとき。
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedTabData()`, `this.#resolveClosedDataSource()`, `winData.closedGroups.findIndex()`, `winData.closedGroups.splice()`
- 条件付き依存: `if (closedGroupIndex < 0)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `closedGroup.tabs`, `closedGroup.tabs.length`, `closedTabGroup.id`, `winData.closedGroups`

## _SessionStore.forgetSavedTabGroup()
- 位置: L4736-4766
- 役割: 保存済みタブグループを ID で探して削除し、そのタブを閉じた一覧からも外す。各ウィンドウの直近グループ参照は、一致すれば解除する。見つからなければ例外。
- 触るとき: 保存済みタブグループを忘れる操作で残る参照や通知の範囲を変えるとき。
- 呼び出し先: `Object.values()`, `this.#notifyOfClosedObjectsChange()`, `this.#notifyOfSavedTabGroupsChange()`, `this.#removeClosedTabData()`, `this.#savedGroups.findIndex()`, `this.#savedGroups.splice()`
- 条件付き依存: `if (savedGroupIndex < 0)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `savedGroup.tabs`, `savedGroup.tabs.length`, `savedTabGroup.id`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#savedGroups`, `this.#windows`, `winData._lastClosedTabGroupCount`, `winData.lastClosedTabGroupId`

## _SessionStore.forgetClosedWindowById()
- 位置: L4777-4789
- 役割: 閉じたウィンドウ一覧から closedId が一致する位置を探し、forgetClosedWindow に委ねる。見つからなければ例外。
- 触るとき: 閉じたウィンドウを ID で忘れる経路を追うとき。
- 呼び出し先: `this.#closedWindows.findIndex()`, `this.forgetClosedWindow()`
- 条件付き依存: `if (closedIndex < 0)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `windowState.closedId`

## _SessionStore.forgetClosedTabById()
- 位置: L4804-4853
- 役割: 渡された呼び出し元があればそのウィンドウだけ、なければ開いているウィンドウ(includePrivate が偽ならプライベートを除く)を順に調べ、closedId が一致する閉じたタブを削除する。どこにも無ければ例外。
- 触るとき: 閉じたタブを ID で忘れるときの検索範囲(プライベートを含むかどうか)を変えるとき。
- 呼び出し先: `Components.Exception()`, `closedTabs.find()`, `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 条件付き依存: `if ( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions )` → `this.#resolveClosedDataSource()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `Array.from()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `sourceWindowsData.push()`
- 条件付き依存: `if (!( aSourceOptions instanceof Ci.nsIDOMWindow || "sourceWindowId" in aSourceOptions || "sourceClosedId" in aSourceOptions ))` → `this.#windowIds.get()`
- 条件付き依存: `if (closedTabState)` → `this.#getClosedTabStateFromUnifiedIndex()`
- 条件付き依存: `if (closedTabState)` → `this.#removeClosedTabData()`
- 条件付き依存: `if (closedTabState)` → `this.#notifyOfClosedObjectsChange()`
- 参照: `(aSourceOptions) .includePrivate`, `Ci.nsIDOMWindow`, `Cr.NS_ERROR_INVALID_ARG`, `tabData.closedId`, `this.#browserWindows`, `this.#windows`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md)

## _SessionStore.getClosedWindowCount()
- 位置: L4859-4861
- 役割: 閉じたウィンドウ一覧の件数を返す。
- 触るとき: 開き直せる閉じたウィンドウがあるかの判定を見るとき。
- 参照: `this.#closedWindows.length`

## _SessionStore.getClosedWindowData()
- 位置: L4866-4872
- 役割: 閉じたウィンドウ一覧を複製し、各ウィンドウのグループを概要情報だけに切り詰めて返す。
- 触るとき: 外部に渡す閉じたウィンドウの情報の範囲を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `this.#trimSavedTabGroupMetadataInClosedWindow()`
- 参照: `this.#closedWindows`

## _SessionStore.#trimSavedTabGroupMetadataInClosedWindow()
- 位置: L4884-4889
- 役割: 閉じたウィンドウの groups を、TabGroupState の abbreviated 形式(タブの本体を除いた要約)に置き換える。
- 触るとき: 閉じたウィンドウの情報に含めるグループの項目を増減するとき。
- 呼び出し先: `Cu.cloneInto()`, `closedWinData.groups?.map()`, `lazy.TabGroupState.abbreviated()`
- 参照: `closedWinData.groups`

## _SessionStore.maybeDontRestoreTabs()
- 位置: L4898-4901
- 役割: 指定ウィンドウに _maybeDontRestoreTabs を立て、次回の起動時に前回セッションのタブを復元しないようにする。
- 触るとき: ユーザーが閉じたウィンドウのタブが次回起動時に戻らないようにする経路を追うとき。
- 呼び出し先: `this.#windowIds.get()`
- 参照: `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._maybeDontRestoreTabs`

## _SessionStore.#isLastRestorableWindow()
- 位置: L4903-4909
- 役割: 非プライベートの開いているウィンドウがちょうど 1 つで、閉じたウィンドウに復元対象(_shouldRestore)が無いときに真を返す。
- 触るとき: 最後のウィンドウを閉じたときに閉じたウィンドウとして保存するかを判定する条件を変えるとき。
- 呼び出し先: `Object.values()`, `Object.values(this.#windows).filter()`, `this.#closedWindows.some()`
- 参照: `Object.values(this.#windows).filter(winData => !winData.isPrivate) .length`, `this.#windows`, `win._shouldRestore`, `winData.isPrivate`

## _SessionStore.undoCloseWindow()
- 位置: L4922-4957
- 役割: 閉じたウィンドウを一覧から外して開き直し、中の保存済みタブグループを開いたグループに変換して保存済みから消す。ウィンドウ表示後に undo_close として状態を復元する。
- 触るとき: 閉じたウィンドウを開き直す挙動や、保存済みタブグループが戻る際の移動の扱いを変えるとき。
- 呼び出し先: `WINDOW_SHOWING_PROMISES.get()`, `WINDOW_SHOWING_PROMISES.get(window).promise.then()`, `this.#notifyOfClosedObjectsChange()`, `this.#openWindowWithState()`, `this.#removeClosedWindow()`, `this.#restoreWindows()`, `this.#trimSavedTabGroupMetadataInClosedWindow()`, `this.getSavedTabGroup()`
- 条件付き依存: `if (!(aIndex in this.#closedWindows))` → `Components.Exception()`
- 条件付き依存: `if (this.getSavedTabGroup(tabGroup.id))` → `this.forgetSavedTabGroup()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `state.windows`, `state.windows[0].closedAt`, `state.windows[0].groups`, `tabGroup.id`, `this.#closedWindows`, `this.#windowToFocus`

## _SessionStore.forgetClosedWindow()
- 位置: L4967-4984
- 役割: 指定位置(省略時は最新)の閉じたウィンドウを一覧から削除し、保存対象からも外す。範囲外なら例外。
- 触るとき: 閉じたウィンドウを一覧から消す操作の副作用を確認するとき。
- 呼び出し先: `this.#notifyOfClosedObjectsChange()`, `this.#removeClosedWindow()`, `this.#saveableClosedWindowData.delete()`
- 条件付き依存: `if (!(aIndex in this.#closedWindows))` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#closedWindows`

## _SessionStore.getCustomWindowValue()
- 位置: L4995-5010
- 役割: 追跡中のウィンドウ、または終了直前のキャッシュにあるウィンドウの extData から指定キーの値を返す。無ければ空文字列。どちらにも無ければ例外。
- 触るとき: 拡張機能などがウィンドウに保存した値を読む経路で、キーの不一致や空文字の扱いを確認するとき。
- 呼び出し先: `Components.Exception()`, `DyingWindowCache.has()`, `this.#windowIds.has()`
- 条件付き依存: `if (this.#windowIds.has(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (DyingWindowCache.has(aWindow))` → `DyingWindowCache.get()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `DyingWindowCache.get(aWindow).extData`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].extData`

## _SessionStore.setCustomWindowValue()
- 位置: L5024-5040
- 役割: 文字列の値だけを受け付け、追跡中のウィンドウの extData に保存して状態の保存を遅延予約する。型が違えば TypeError、未追跡なら例外。
- 触るとき: ウィンドウ単位のカスタム値の保存条件や、保存タイミングを変えるとき。
- 呼び出し先: `this.#saveStateDelayed()`, `this.#windowIds.get()`, `this.#windowIds.has()`
- 条件付き依存: `if (!this.#windowIds.has(aWindow))` → `Components.Exception()`
- 条件付き依存: `if (!this.#windows[this.#windowIds.get(aWindow)].extData)` → `this.#windowIds.get()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].extData`

## _SessionStore.deleteCustomWindowValue()
- 位置: L5050-5059
- 役割: ウィンドウの extData から指定キーを消し、値の有無に関わらず状態の保存を遅延予約する。
- 触るとき: ウィンドウ単位のカスタム値を削除したときに保存が走るかを確認するとき。
- 呼び出し先: `this.#saveStateDelayed()`, `this.#windowIds.get()`
- 条件付き依存: `if ( this.#windowIds.get(aWindow) && this.#windows[this.#windowIds.get(aWindow)].extData && this.#windows[this.#windowIds.get(aWindow)].extData[aKey] )` → `this.#windowIds.get()`
- 参照: `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].extData`

## _SessionStore.getCustomTabValue()
- 位置: L5069-5071
- 役割: タブのカスタム値から指定キーの値を返す。無ければ空文字列。
- 触るとき: タブ単位のカスタム値の読み出し方を確認するとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`

## _SessionStore.setCustomTabValue()
- 位置: L5084-5097
- 役割: 文字列の値だけを受け付け、タブのカスタム値の辞書を作ってから値を書き込み、タブのあるウィンドウの保存を遅延予約する。型が違えば TypeError。
- 触るとき: タブ単位のカスタム値が未復元タブでも失われないかを確認するとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `TAB_CUSTOM_VALUES.has()`, `this.#saveStateDelayed()`
- 条件付き依存: `if (!TAB_CUSTOM_VALUES.has(aTab))` → `TAB_CUSTOM_VALUES.set()`
- 参照: `aTab.documentGlobal`

## _SessionStore.deleteCustomTabValue()
- 位置: L5107-5113
- 役割: タブのカスタム値に指定キーがあれば削除し、保存を遅延予約する。
- 触るとき: タブ単位のカスタム値の削除で保存が走る条件を変えるとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (state && aKey in state)` → `this.#saveStateDelayed()`
- 参照: `aTab.documentGlobal`

## _SessionStore.#moveCustomTabValue()
- 位置: L5119-5128
- 役割: 移動元タブのカスタム値の辞書を移動先タブへ付け替え、移動元の登録を外す。保存の予約は呼び出し元が行う。
- 触るとき: タブをウィンドウ間で移動したときにカスタム値が引き継がれるかを確認するとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (state)` → `TAB_CUSTOM_VALUES.set()`
- 条件付き依存: `if (state)` → `TAB_CUSTOM_VALUES.delete()`

## _SessionStore.getLazyTabValue()
- 位置: L5139-5141
- 役割: 遅延タブ(まだ browser が作られていないタブ)の遅延状態から指定キーの値を返す。遅延状態が無ければ undefined。
- 触るとき: 遅延タブの URL やタイトルを読み取る経路を変えるとき。
- 呼び出し先: `TAB_LAZY_STATES.get()`

## _SessionStore.getCustomGlobalValue()
- 位置: L5149-5151
- 役割: セッション全体のグローバル状態から指定キーの値を返す。
- 触るとき: セッション全体で保存する値の読み出しを確認するとき。
- 呼び出し先: `this.#globalState.get()`

## _SessionStore.setCustomGlobalValue()
- 位置: L5162-5169
- 役割: 文字列の値だけを受け付け、グローバル状態に保存して状態の保存を遅延予約する。型が違えば TypeError。
- 触るとき: セッション全体の値の保存条件を変えるとき。
- 呼び出し先: `this.#globalState.set()`, `this.#saveStateDelayed()`

## _SessionStore.deleteCustomGlobalValue()
- 位置: L5177-5180
- 役割: グローバル状態から指定キーを削除し、状態の保存を遅延予約する。
- 触るとき: グローバル値の削除後に保存が反映されるかを確認するとき。
- 呼び出し先: `this.#globalState.delete()`, `this.#saveStateDelayed()`

## _SessionStore.undoCloseById()
- 位置: L5197-5228
- 役割: closedId が閉じたウィンドウに一致すればそのウィンドウを開き直し、そうでなければ開いているウィンドウの閉じたタブ一覧から探して開き直す。どちらにも無ければ undefined を返す。
- 触るとき: closedId 一つで閉じたタブかウィンドウを開き直す共通の入口の挙動を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.wm.getEnumerator()`, `this.#windowIds.get()`
- 条件付き依存: `if (this.#closedWindows[i].closedId == aClosedId)` → `this.undoCloseWindow()`
- 条件付き依存: `if (windowState)` → `this.#getStateForClosedTabsAndClosedGroupTabs()`
- 条件付き依存: `if (closedTabs[j].closedId == aClosedId)` → `this.undoCloseTab()`
- 参照: `closedTabs.length`, `closedTabs[j].closedId`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[i].closedId`, `this.#windows`
- XPCOM: `Services.wm`

## _SessionStore.#updateTabLabelAndIcon()
- 位置: L5240-5285
- 役割: カスタマイズモード中は何もしない。現在の履歴エントリのタイトルとアイコンをタブに設定し、読み込んだアイコンは一度だけ使ってキャッシュから消す。about:blank の最初の読み込みではアイコンを変えない。
- 触るとき: 復元直後のタブのタイトルやアイコンがちらつく問題、または about:blank の扱いを調べるとき。
- 呼び出し先: `tab.hasAttribute()`
- 条件付き依存: `if (!tabData)` → `lazy.TabState.collect()`
- 条件付き依存: `if (!tabData)` → `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (activePageData.title && activePageData.title != activePageData.url)` → `win.gBrowser.setInitialTabTitle()`
- 条件付き依存: `if (!(activePageData.title && activePageData.title != activePageData.url))` → `win.gBrowser.setInitialTabTitle()`
- 条件付き依存: `if ( !activePageData || (activePageData && activePageData.url != "about:blank") )` → `win.gBrowser.setIcon()`
- 条件付き依存: `if ("image" in tabData)` → `lazy.TabStateCache.update()`
- 参照: `activePageData.title`, `activePageData.url`, `browser.documentGlobal`, `browser.permanentKey`, `tab.linkedBrowser`, `tabData.entries`, `tabData.image`, `tabData.index`

## _SessionStore.#forgetTabsWithUserContextId()
- 位置: L5288-5331
- 役割: 指定のユーザーコンテキスト ID を持つ閉じたタブを、開いているウィンドウと閉じたウィンドウの両方から削除する。閉じたウィンドウは残りのタブが無くなったら一覧から外す。
- 触るとき: コンテナ(ユーザーコンテキスト)を削除したときに閉じたタブが残らないかを確認するとき。
- 呼び出し先: `Services.wm.getEnumerator()`, `clearClosedTabs()`, `this.#notifyOfClosedObjectsChange()`, `this.#windowIds.get()`, `windowState.tabs.filter()`
- 条件付き依存: `if (windowState)` → `clearClosedTabs()`
- 条件付き依存: `if (!windowState.tabs.length)` → `this.#removeClosedWindow()`
- 条件付き依存: `if (!windowState.tabs.length)` → `this.#saveableClosedWindowData.delete()`
- 参照: `tab.userContextId`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#windows`, `windowState.tabs`, `windowState.tabs.length`
- XPCOM: `Services.wm`

## clearClosedTabs()
- 位置: L5289-5303
- 役割: 指定ウィンドウの閉じたタブのうち、ユーザーコンテキスト ID が一致するものを後ろから順に削除する。
- 触るとき: ユーザーコンテキスト単位で閉じたタブを消す範囲を変えるとき。
- 呼び出し先: `indexes.reverse()`, `this.#removeClosedTabData()`, `windowState._closedTabs.forEach()`
- 条件付き依存: `if (closedTab.state.userContextId == userContextId)` → `indexes.push()`
- 参照: `closedTab.state.userContextId`, `windowState._closedTabs`

## _SessionStore.restoreLastSession()
- 位置: L5340-5517
- 役割: 前回セッション(LastSession)を現在のセッションへ統合する。既存ウィンドウに入れられるものは再利用し、残りは新規に開いて逆 z 順で復元し、閉じたウィンドウや保存済みグループ、クラッシュ回数も引き継ぐ。
- 触るとき: 「前回のセッションを復元」の動作、既存ウィンドウの再利用条件、または復元後に閉じたタブ一覧がどう統合されるかを変えるとき。
- 呼び出し先: `LastSession.clear()`, `LastSession.getState()`, `Services.obs.notifyObservers()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.AIWindow.isAIWindowEnabled()`, `lazy.DevToolsShim.restoreDevToolsSession()`, `lazy.SessionCookies.restore()`, `openWindows.concat()`, `this.#canRestoreIntoExistingWindow()`, `this.#getTopWindow()`, `this.#globalState.setFromState()`, `this.#lastSessionWindowIds.get()`, `this.#notifyOfClosedObjectsChange()`, `this.#openWindows()`, `this.#openWindows({ windows: windowsToOpen }).then()`, `this.#restoreWindowsInReversedZOrder()`, `this.#savedGroups.filter()`, `this.#updateSessionStartTime()`, `this.forgetSavedTabGroup()`
- 条件付き依存: `if (!this.canRestoreLastSession)` → `Components.Exception()`
- 条件付き依存: `if (this.#lastSessionWindowIds.get(window))` → `this.#lastSessionWindowIds.get()`
- 条件付き依存: `if (!lastSessionState.windows.length)` → `Components.Exception()`
- 条件付き依存: `if (this.#restoreWithoutRestart)` → `this.#closedWindows.findIndex()`
- 条件付き依存: `if (restoreIndex > -1)` → `this.#closedWindows.splice()`
- 条件付き依存: `if (winState._closedTabs && winState._closedTabs.length)` → `this.#windowIds.get()`
- 条件付き依存: `if (winState._closedTabs && winState._closedTabs.length)` → `curWinState._closedTabs.concat()`
- 条件付き依存: `if (winState._closedTabs && winState._closedTabs.length)` → `curWinState._closedTabs.splice()`
- 条件付き依存: `if (windowToUse)` → `this.#getRemovableHomePages()`
- 条件付き依存: `if (!(windowToUse.gBrowser.tabs.length == removableTabs.length))` → `windowToUse.gBrowser.removeTab()`
- 条件付き依存: `if (!(windowToUse.gBrowser.tabs.length == removableTabs.length))` → `removableTabs.pop()`
- 条件付き依存: `if (windowToUse)` → `this.#updateWindowRestoreState()`
- 条件付き依存: `if (windowToUse)` → `openWindows.push()`
- 条件付き依存: `if (!(windowToUse))` → `windowsToOpen.push()`
- 条件付き依存: `if (this.#restoreWithoutRestart)` → `this.#removeDuplicateClosedWindows()`
- 条件付き依存: `if (closedWindow._closedTabs?.length)` → `this.#resetClosedTabIds()`
- 条件付き依存: `if (lastSessionState._closedWindows)` → `this.#closedWindows.concat()`
- 条件付き依存: `if (lastSessionState._closedWindows)` → `this.#capClosedWindows()`
- 参照: `Cr.NS_ERROR_UNEXPECTED`, `closedWindow._closedTabs`, `closedWindow._closedTabs?.length`, `closedWindow.closedId`, `curWinState._closedTabs`, `curWinState._closedTabs.length`, `group.id`, `group.removeAfterRestore`, `lastSessionState._closedWindows`, `lastSessionState.cookies`, `lastSessionState.session`, `lastSessionState.session.recentCrashes`, `lastSessionState.windows`, `lastSessionState.windows.length`, `removableTabs.length`, `this.#browserSetState`, `this.#browserWindows`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#max_tabs_undo`, `this.#nextClosedId`, `this.#recentCrashes`, `this.#restoreCount`, `this.#restoreWithoutRestart`, `this.#windows`, `this.canRestoreLastSession`, `win.closedId`, `winState.__lastSessionWindowID`, `winState._closedTabs`, `winState._closedTabs.length`, `winState.closedId`, `winState.isAIWindow`, `windowToUse.gBrowser.tabs.length`
- XPCOM: `Services.obs`

## _SessionStore.#removeDuplicateClosedWindows()
- 位置: L5527-5537
- 役割: 前回セッションの _closedWindows から、現在の閉じたウィンドウと closedId が重なるものを除く。何度も復元した場合の重複を防ぐ。
- 触るとき: 復元を繰り返したときに閉じたウィンドウが二重に並ぶ問題を調べるとき。
- 呼び出し先: `currentClosedIds.has()`, `lastSessionState._closedWindows.filter()`, `this.#closedWindows.map()`
- 参照: `lastSessionState._closedWindows`, `win.closedId`, `window.closedId`

## _SessionStore.reviveCrashedTab()
- 位置: L5547-5585
- 役割: クラッシュ中として記録された browser の属性を外し、一度 about:blank を読み込んでから、タブの状態を強制的に遅延復元する。クラッシュ中でなければ何もしない。残っていれば例外。
- 触るとき: クラッシュしたタブを復活させるときの読み込み先や遅延復元の扱いを変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `TAB_CUSTOM_VALUES.get()`, `aTab.removeAttribute()`, `browser.loadURI()`, `lazy.TabState.collect()`, `this.#crashedBrowsers.has()`, `this.#restoreTab()`
- 参照: `aTab.linkedBrowser`, `aTab.userContextId`, `browser.isRemoteBrowser`, `browser.permanentKey`, `lazy.E10SUtils.NOT_REMOTE`, `lazy.blankURI`
- XPCOM: `Services.scriptSecurityManager`

## _SessionStore.reviveAllCrashedTabs()
- 位置: L5590-5596
- 役割: 開いている全ウィンドウの全タブについて reviveCrashedTab を呼ぶ。
- 触るとき: クラッシュしたタブを一括で復活させる挙動を確認するとき。
- 呼び出し先: `Services.wm.getEnumerator()`, `this.reviveCrashedTab()`
- 参照: `window.gBrowser.tabs`
- XPCOM: `Services.wm`

## _SessionStore.getSessionHistory()
- 位置: L5612-5628
- 役割: タブの現在の状態から履歴エントリと現在のインデックス(0 始まり)を返す。updatedCallback があれば、フラッシュ後の最新の履歴でも呼び出す。タブが閉じていれば null。
- 触るとき: 履歴一覧の取得元や、フラッシュ後に更新されるタイミングを確認するとき。
- 条件付き依存: `if (updatedCallback)` → `lazy.TabStateFlusher.flush(tab.linkedBrowser).then()`
- 条件付き依存: `if (updatedCallback)` → `lazy.TabStateFlusher.flush()`
- 条件付き依存: `if (updatedCallback)` → `this.getSessionHistory()`
- 条件付き依存: `if (sessionHistory)` → `updatedCallback()`
- 条件付き依存: `if (tab.linkedBrowser)` → `lazy.TabState.collect()`
- 条件付き依存: `if (tab.linkedBrowser)` → `TAB_CUSTOM_VALUES.get()`
- 参照: `tab.linkedBrowser`, `tabState.entries`, `tabState.index`

## _SessionStore.#canRestoreIntoExistingWindow()
- 位置: L5642-5673
- 役割: 既存ウィンドウと前回のウィンドウ状態について、ポップアップ、プライベート、taskbar tab の性質と引数(args)が一致するかを判定する。一致しなければ既存ウィンドウへの復元を許さない。
- 触るとき: 前回セッションのウィンドウを既存ウィンドウに入れてよい条件を変えるとき。
- 呼び出し先: `Boolean()`, `Object.entries()`, `Object.entries(existingArgs).every()`, `Object.keys()`, `this.#getWindowStateData()`
- 参照: `Object.keys(existingArgs).length`, `Object.keys(previousArgs).length`, `aPreviousState.args`, `aPreviousState.isPopup`, `aPreviousState.isPrivate`, `aPreviousState.isTaskbarTab`, `existingState.args`, `existingState.isPopup`, `existingState.isPrivate`, `existingState.isTaskbarTab`

## _SessionStore.#getImmutableWindowFeatures()
- 位置: L5684-5707
- 役割: ウィンドウ状態から、作成時にしか決められない特性(private、popup、taskbartab、chromeless、拡張ポップアップ)の名前を集めた Set を返す。
- 触るとき: ウィンドウ復元時に新しい特性を作成時オプションとして渡す判定を追加するとき。
- 条件付き依存: `if (winState.isPrivate)` → `features.add()`
- 条件付き依存: `if (winState.isPopup)` → `features.add()`
- 条件付き依存: `if (winState.isTaskbarTab)` → `features.add()`
- 条件付き依存: `if (winState.args?.[ARG_CHROMELESS_WINDOW])` → `features.add()`
- 条件付き依存: `if (winState.args?.[ARG_WEB_EXTENSION_POPUP_WINDOW])` → `features.add()`
- 参照: `winState.args`, `winState.isPopup`, `winState.isPrivate`, `winState.isTaskbarTab`

## _SessionStore.#getRemovableHomePages()
- 位置: L5720-5754
- 役割: 既存ウィンドウの非固定タブのうち about:blank やホームページ(startup.page が 1 のとき)、AI ウィンドウの初期 URL に一致するものを集める。全可視タブが対象なら 1 つ残す。
- 触るとき: 状態を既存ウィンドウに流し込む前に、どのホームページタブを閉じるか判定を変えるとき。
- 呼び出し先: `homePages.includes()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `this.#prefBranch.getIntPref()`
- 条件付き依存: `if (startupPref == 1)` → `homePages.concat()`
- 条件付き依存: `if (startupPref == 1)` → `lazy.HomePage.get(aWindow).split()`
- 条件付き依存: `if (startupPref == 1)` → `lazy.HomePage.get()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActiveAndEnabled(aWindow))` → `homePages.push()`
- 条件付き依存: `if (homePages.includes(tab.linkedBrowser.currentURI.spec))` → `removableTabs.push()`
- 条件付き依存: `if ( tabbrowser.tabs.length > tabbrowser.visibleTabs.length && tabbrowser.visibleTabs.length === removableTabs.length )` → `removableTabs.shift()`
- 参照: `aWindow.gBrowser`, `lazy.AIWindow.initialStartupURL`, `removableTabs.length`, `tab.linkedBrowser.currentURI.spec`, `tabbrowser.pinnedTabCount`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `tabbrowser.visibleTabs.length`

## _SessionStore.#updateWindowFeatures()
- 位置: L5764-5786
- 役割: ウィンドウの寸法・表示状態、最小化前の表示モード、サイドバーの UI 状態、ワークスペース ID、AI ウィンドウ判定を状態に書き込む。
- 触るとき: 保存されるウィンドウの見た目の情報(位置、サイズ、サイドバー、ワークスペース)を増やすとき。
- 呼び出し先: `aWindow.SidebarController.getUIState()`, `aWindow.getWorkspaceID()`, `lazy.AIWindow.isAIWindowActive()`, `this.#getWindowDimension()`, `this.#windowIds.get()`
- 条件付き依存: `if (sidebarUIState)` → `structuredClone()`
- 参照: `this.#windows`, `winData.isAIWindow`, `winData.sidebar`, `winData.sizemode`, `winData.sizemodeBeforeMinimized`, `winData.workspaceID`

## _SessionStore.getCurrentState()
- 位置: L5796-5922
- 役割: 実行中なら必要なウィンドウだけタブ状態を収集し、それ以外は見た目の情報だけ更新してから、全ウィンドウ・復元待ちのウィンドウ・閉じたウィンドウ・Cookie・グローバル状態などを含むセッション全体の状態を組み立てて返す。macOS 以外で最後の通常ウィンドウが無くなり終了中なら、閉じたウィンドウを先頭に加える。
- 触るとき: セッションファイルに書かれる内容や、終了時にどの閉じたウィンドウが含まれるかを変えるとき。
- 呼び出し先: `Date.now()`, `Glean.sessionRestore.collectAllWindowsData.start()`, `Glean.sessionRestore.collectAllWindowsData.stopAndAccumulate()`, `ids.indexOf()`, `ids.push()`, `lazy.DevToolsShim.saveDevToolsSession()`, `lazy.SessionCookies.collect()`, `this.#closedWindows.slice()`, `this.#getTopWindow()`, `this.#globalState.getState()`, `this.#handleClosedWindows()`, `this.#handleClosedWindows().then()`, `this.#notifyOfClosedObjectsChange()`, `total.push()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#isWindowLoaded()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `DirtyWindows.has()`
- 条件付き依存: `if (aUpdateAll || DirtyWindows.has(window) || window == activeWindow)` → `this.#collectWindowData()`
- 条件付き依存: `if (!(aUpdateAll || DirtyWindows.has(window) || window == activeWindow))` → `this.#updateWindowFeatures()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#windowIds.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `DirtyWindows.clear()`
- 条件付き依存: `if ( nonPopupCount == 0 && !!lastClosedWindowsCopy.length && lazy.RunState.isQuitting )` → `total.unshift()`
- 条件付き依存: `if ( nonPopupCount == 0 && !!lastClosedWindowsCopy.length && lazy.RunState.isQuitting )` → `lastClosedWindowsCopy.shift()`
- 条件付き依存: `if (activeWindow)` → `this.#windowIds.get()`
- 条件付き依存: `if (LastSession.canRestore)` → `LastSession.getState()`
- 参照: `AppConstants.platform`, `LastSession.canRestore`, `lastClosedWindowsCopy.length`, `lazy.RunState.isQuitting`, `lazy.RunState.isRunning`, `state.cookies`, `state.deferredInitialState`, `state.lastSessionState`, `this.#activeWindowSSiCache`, `this.#deferredInitialState`, `this.#maxSplitViewId`, `this.#orderedBrowserWindows`, `this.#recentCrashes`, `this.#savedGroups`, `this.#sessionStartTime`, `this.#statesToRestore`, `this.#statesToRestore[ix].windows`, `this.#windows`, `this.#windows[ix]._restoring`, `this.#windows[ix].isPopup`, `this.#windows[ix].isTaskbarTab`, `this.#windows[this.#windowIds.get(window)].zIndex`, `total[0].isPopup`, `total[ix].sizemode`, `winData.isPopup`

## _SessionStore.#getWindowState()
- 位置: L5931-5941
- 役割: 読み込み済みのウィンドウならそのタブ状態を収集して返し、未読み込みなら復元待ちの状態を返す。
- 触るとき: getWindowState の内部で、読み込み途中のウィンドウをどう扱うかを確認するとき。
- 呼び出し先: `this.#isWindowLoaded()`, `this.#windowIds.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.get()`
- 条件付き依存: `if (lazy.RunState.isRunning)` → `this.#collectWindowData()`
- 参照: `lazy.RunState.isRunning`, `this.#statesToRestore`, `this.#windows`

## _SessionStore.#getWindowStateData()
- 位置: L5950-5962
- 役割: 追跡中のウィンドウの内部状態オブジェクトを返す。未追跡なら例外。
- 触るとき: ウィンドウ内部データを直接読む箇所を追加・変更するとき。
- 呼び出し先: `this.#windowIds.get()`
- 条件付き依存: `if ( !this.#windowIds.get(aWindow) || !(this.#windowIds.get(aWindow) in this.#windows) )` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `this.#windows`

## _SessionStore.#collectWindowData()
- 位置: L5974-6029
- 役割: 読み込み済みのウィンドウについて、タブごとの状態(Firefox View タブは除く)、タブグループ、分割表示を集めて内部状態を更新し、タブ状態のマップを返す。未読み込みなら何もしない。
- 触るとき: 保存されるタブ・タブグループ・分割表示のデータを増やす、または収集対象を絞るとき。
- 呼び出し先: `DirtyWindows.remove()`, `TAB_CUSTOM_VALUES.get()`, `lazy.TabGroupState.collect()`, `lazy.TabState.collect()`, `tabMap.set()`, `tabsData.push()`, `this.#isWindowLoaded()`, `this.#lastSessionWindowIds.get()`, `this.#updateWindowFeatures()`, `this.#windowIds.get()`, `winData.groups.push()`, `winData.splitViews.push()`
- 条件付き依存: `if (this.#lastSessionWindowIds.get(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#lastSessionWindowIds.get(aWindow))` → `this.#lastSessionWindowIds.get()`
- 参照: `aWindow.FirefoxViewHandler.tab`, `aWindow.FirefoxViewHandler.tab?.selected`, `aWindow.gBrowser`, `aWindow.gBrowser.splitViews`, `aWindow.gBrowser.tabGroups`, `splitView.state`, `tabbrowser.tabbox.selectedIndex`, `tabbrowser.tabs`, `tabbrowser.tabs[0].label`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].__lastSessionWindowID`, `winData.groups`, `winData.selected`, `winData.splitViews`, `winData.tabs`, `winData.title`

## _SessionStore.#openWindows()
- 位置: L6041-6057
- 役割: 状態を持つウィンドウを 1 つずつ #openWindowWithState で開き、全部が表示されるまで待つ。タブが無いウィンドウは飛ばして復元数を減らす。
- 触るとき: 復元時に新規ウィンドウを開く数や、タブの無いウィンドウを扱う判定を変えるとき。
- 呼び出し先: `Promise.all()`, `WINDOW_SHOWING_PROMISES.get()`, `this.#openWindowWithState()`, `windowOpenedPromises.push()`, `windowsOpened.push()`
- 条件付き依存: `if (!winData || !winData.tabs || !winData.tabs[0])` → `this.#log.debug()`
- 参照: `deferred.promise`, `root.windows`, `this.#restoreCount`, `winData.tabs`

## _SessionStore.#resetClosedTabIds()
- 位置: L6069-6075
- 役割: 渡された閉じたタブごとに新しい closedId を振り、sourceWindowId を指定のウィンドウ ID にする。
- 触るとき: 前回セッションの閉じたタブの ID が現在のセッションと重ならないようにする処理を変えるとき。
- 参照: `entry.closedId`, `entry.sourceWindowId`, `this.#nextClosedId`

## _SessionStore.#initSplitViewIds()
- 位置: L6077-6099
- 役割: 分割表示 ID の採番カウンタを、遅延状態・前回セッション状態・現在の状態の順に読み、必要なら各状態を移行したうえで最大値に揃える。カウンタが既に 0 より大きい場合はエラーログを出す。
- 触るとき: 分割表示 ID の移行や、セッション起動時の採番カウンタの初期化を変えるとき。
- 呼び出し先: `Math.max()`, `this.#migrateSplitViewIds()`
- 条件付き依存: `if (this.#maxSplitViewId > 0)` → `this.#log.error()`
- 参照: `session.maxSplitViewId`, `state.deferredInitialState`, `state.lastSessionState`, `this.#maxSplitViewId`

## _SessionStore.#migrateSplitViewIds()
- 位置: L6108-6161
- 役割: maxSplitViewId が数値なら何もしない。それ以外は、文字列の分割表示 ID を新しい整数 ID に振り直し(同じ分割表示のタブは同じ新 ID になる)、グループの分割表示データの ID も合わせる。
- 触るとき: 古い形式の分割表示 ID を持つセッションファイルを読み込む際の変換規則を変えるとき。
- 呼び出し先: `oldToNewMap.get()`, `oldToNewMap.has()`
- 条件付き依存: `if (state._closedWindows?.length)` → `windowsData.push.apply()`
- 条件付き依存: `if (idType === "number")` → `Math.max()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `oldToNewMap.set()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `SessionStore.getNextSplitViewId()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `this.#log.debug()`
- 条件付き依存: `if (!oldToNewMap.has(tabData.splitViewId))` → `oldToNewMap.get()`
- 条件付き依存: `if (winData.splitViews)` → `oldToNewMap.has()`
- 条件付き依存: `if (oldToNewMap.has(splitViewData.id))` → `oldToNewMap.get()`
- 参照: `splitViewData.id`, `state._closedWindows`, `state._closedWindows?.length`, `state.maxSplitViewId`, `state.windows`, `tabData.splitViewId`, `this.#maxSplitViewId`, `winData.splitViews`, `winData.tabs`, `winData.tabs?.length`

## _SessionStore.#restoreWindow()
- 位置: L6173-6376
- 役割: ウィンドウに保存されたサイドバー、ワークスペース、閉じたタブ一覧、閉じたタブグループ、拡張データを適用し、タブを作って復元する。上書き指定なら既存タブを閉じ、最初のウィンドウでは元からあったタブを末尾へ移す。
- 触るとき: ウィンドウ単位の復元で何がどの順で適用されるか、または既存タブと復元タブの並びを変えるとき。
- 呼び出し先: `Glean.sessionRestore.restoreWindow.start()`, `Glean.sessionRestore.restoreWindow.stopAndAccumulate()`, `lazy.SessionCookies.restore()`, `newClosedTabGroupsData.forEach()`, `this.#isWindowLoaded()`, `this.#lastSessionWindowIds.delete()`, `this.#log.debug()`, `this.#prefBranch.getBoolPref()`, `this.#resetClosedTabIds()`, `this.#restoreSidebar()`, `this.#sendWindowRestoringNotification()`, `this.#setWindowStateBusy()`, `this.#windowIds.get()`
- 条件付き依存: `if ( aWindow && (!this.#windowIds.get(aWindow) || !this.#windows[this.#windowIds.get(aWindow)]) )` → `this.#onLoad()`
- 条件付き依存: `if (winData.workspaceID && lazy.gRestoreWindowsToVirtualDesktop)` → `this.#log.debug()`
- 条件付き依存: `if (winData.workspaceID && lazy.gRestoreWindowsToVirtualDesktop)` → `aWindow.moveToWorkspace()`
- 条件付き依存: `if (overwriteTabs)` → `Math.max()`
- 条件付き依存: `if (overwriteTabs)` → `Math.min()`
- 条件付き依存: `if (!overwriteTabs && firstWindow)` → `Array.from()`
- 条件付き依存: `if (!tabbrowser.tabs[i].selected)` → `tabbrowser.removeTab()`
- 条件付き依存: `if (winData.tabs.length)` → `tabbrowser.createTabsForSessionRestore()`
- 条件付き依存: `if (winData.tabs.length)` → `this.#log.debug()`
- 条件付き依存: `if (winData.tabs.length)` → `tabbrowser.tabGroups.map()`
- 条件付き依存: `if (winData.tabs.length)` → `this.#savedGroups.filter()`
- 条件付き依存: `if (winData.tabs.length)` → `openTabGroupIdsInWindow.has()`
- 条件付き依存: `if (initialTabs)` → `tabbrowser.unpinTab()`
- 条件付き依存: `if (initialTabs)` → `tabbrowser.moveTabTo()`
- 条件付き依存: `if (winData.__lastSessionWindowID)` → `this.#lastSessionWindowIds.set()`
- 条件付き依存: `if (overwriteTabs)` → `this.#windowIds.get()`
- 条件付き依存: `if (winData.extData)` → `this.#windowIds.get()`
- 条件付き依存: `if (!this.#windows[this.#windowIds.get(aWindow)].extData)` → `this.#windowIds.get()`
- 条件付き依存: `if (winData._closedTabs)` → `this.#resetClosedTabIds()`
- 条件付き依存: `if (winData._closedTabs)` → `this.#windowIds.get()`
- 条件付き依存: `if (overwriteTabs || firstWindow)` → `this.#windowIds.get()`
- 条件付き依存: `if (PERSIST_SESSIONS)` → `this.#windows[ this.#windowIds.get(aWindow) ]._closedTabs.filter()`
- 条件付き依存: `if (PERSIST_SESSIONS)` → `this.#windowIds.get()`
- 条件付き依存: `if (!(PERSIST_SESSIONS))` → `newClosedTabsData.concat()`
- 条件付き依存: `if (!(PERSIST_SESSIONS))` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#max_tabs_undo > 0)` → `this.#windowIds.get()`
- 条件付き依存: `if (this.#max_tabs_undo > 0)` → `newClosedTabsData.slice()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.delete()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `this.#windowIds.get()`
- 条件付き依存: `if (winData.tabs.length)` → `this.#restoreTabs()`
- 参照: `aOptions.firstWindow`, `aOptions.overwriteTabs`, `aWindow.gBrowser`, `arrowScrollbox.smoothScroll`, `group.id`, `group.tabs`, `initialTabs.length`, `lazy.gRestoreWindowsToVirtualDesktop`, `savedTabGroup.id`, `tab.removeAfterRestore`, `tabbrowser.browsers.length`, `tabbrowser.tabContainer.arrowScrollbox`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `tabbrowser.tabs[i].selected`, `tabs.length`, `this.#max_tabs_undo`, `this.#restore_on_demand`, `this.#savedGroups`, `this.#statesToRestore`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)]._closedTabs`, `this.#windows[this.#windowIds.get(aWindow)]._lastClosedTabGroupCount`, `this.#windows[this.#windowIds.get(aWindow)]._restoring`, `this.#windows[this.#windowIds.get(aWindow)].closedGroups`, `this.#windows[this.#windowIds.get(aWindow)].extData`, `this.#windows[this.#windowIds.get(aWindow)].lastClosedTabGroupId`, `winData.__lastSessionWindowID`, `winData._closedTabs`, `winData._lastClosedTabGroupCount`, `winData.closedGroups`, `winData.cookies`, `winData.extData`, `winData.groups`, `winData.groups?.length`, `winData.isPopup`, `winData.lastClosedTabGroupId`, `winData.selected`, `winData.sidebar`, `winData.splitViews`, `winData.splitViews?.length`, `winData.tabs`, `winData.tabs.length`, `winData.tabs[0].entries`, `winData.tabs[0].entries.length`, `winData.workspaceID`

## _SessionStore.#prepareConnectionToHost()
- 位置: L6388-6414
- 役割: about: 以外の URL について null プリンシパルで投機的接続を開く。成功なら true、例外や about: の URL なら false を返す。
- 触るとき: タブの復元前に接続先へ先行接続する挙動を変えるとき、またはその接続先の条件を調べるとき。
- 呼び出し先: `url.startsWith()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `ChromeUtils.generateQI()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `Services.io.newURI()`
- 条件付き依存: `if (url && !url.startsWith("about:"))` → `Services.io.speculativeConnect()`
- 参照: `tab.linkedBrowser.browsingContext`, `tab.userContextId`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## _SessionStore.getInterface()
- 位置: L6396-6402
- 役割: nsILoadContext を要求されたときだけ対象タブの browsingContext を返し、それ以外は NS_ERROR_NO_INTERFACE を投げる。
- 触るとき: 投機的接続で渡すコールバックが要求するインターフェースを増やすとき。
- 呼び出し先: `Components.Exception()`, `iid.equals()`
- 参照: `Ci.nsILoadContext`, `Cr.NS_ERROR_NO_INTERFACE`
- XPCOM: [`nsILoadContext`](../../../docshell/base/nsILoadContext.idl.md)

## _SessionStore.speculativeConnectOnTabHover()
- 位置: L6424-6440
- 役割: まだ接続していない遅延タブについて、マウスオーバー時に保存済みの URL へ先行接続し、一度試したことを記録して二重に接続しないようにする。
- 触るとき: タブにマウスを乗せたときの先行接続の条件や、テスト用の接続フラグを変えるとき。
- 呼び出し先: `TAB_LAZY_STATES.get()`
- 条件付き依存: `if (tabState && !tabState.connectionPrepared)` → `this.getLazyTabValue()`
- 条件付き依存: `if (tabState && !tabState.connectionPrepared)` → `this.#prepareConnectionToHost()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Object.assign()`
- 参照: `tabState.connectionPrepared`

## _SessionStore.#restoreWindowsFeaturesAndTabs()
- 位置: L6448-6484
- 役割: まず全ウィンドウの見た目(サイズや位置)を復元してからタブ内容を復元し、サイズ変更の完了後に SSWindowStateReady、復元完了の通知を出す。
- 触るとき: 複数ウィンドウ復元で、見た目とタブ内容のどちらを先に適用し、どの通知をいつ出すかを変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `WINDOW_RESTORE_IDS.get()`, `WINDOW_RESTORE_ZINDICES.delete()`, `resizePromise.then()`, `resizePromises.push()`, `this.#restoreWindow()`, `this.#restoreWindowFeatures()`, `this.#sendRestoreCompletedNotifications()`, `this.#sendWindowRestoredNotification()`, `this.#setWindowStateReady()`
- 参照: `state.options`, `state.windows`, `this.#statesToRestore`
- XPCOM: `Services.obs`

## _SessionStore.#restoreWindowsInReversedZOrder()
- 位置: L6493-6502
- 役割: 保存されている z 順の逆に並べ替え、先頭のウィンドウを復元後のフォーカス対象にして、全ウィンドウの features と tabs を復元する。
- 触るとき: 最後に使ったウィンドウを最初に表示させる順序や、復元後にフォーカスされるウィンドウを変えるとき。
- 呼び出し先: `WINDOW_RESTORE_ZINDICES.get()`, `this.#restoreWindowsFeaturesAndTabs()`, `windows.sort()`
- 参照: `this.#windowToFocus`

## _SessionStore.#restoreWindows()
- 位置: L6515-6608
- 役割: 状態を JSON から読み、閉じたウィンドウを再採番して一覧に置き、先頭のウィンドウを既存のウィンドウに入れられるか判定する(不一致なら記録)。残りのウィンドウは開いてから逆 z 順で復元する。ウィンドウが無ければ完了通知だけ送る。
- 触るとき: setBrowserState や setWindowState など、複数ウィンドウの状態をまとめて流し込む経路の順序を変えるとき。
- 呼び出し先: `JSON.parse()`, `lazy.DevToolsShim.restoreDevToolsSession()`, `root.windows.splice()`, `this.#canRestoreIntoExistingWindow()`, `this.#log.debug()`, `this.#log.error()`, `this.#openWindows()`, `this.#openWindows(root).then()`, `this.#restoreWindowsInReversedZOrder()`, `this.#sendRestoreCompletedNotifications()`, `this.#updateWindowRestoreState()`, `this.#windowIds.get()`, `windows.unshift()`
- 条件付き依存: `if ( aWindow && (!this.#windowIds.get(aWindow) || !this.#windows[this.#windowIds.get(aWindow)]) )` → `this.#onLoad()`
- 条件付き依存: `if (closedWindow._closedTabs?.length)` → `this.#resetClosedTabIds()`
- 条件付き依存: `if (root._closedWindows)` → `this.#log.debug()`
- 条件付き依存: `if (!root.windows || !root.windows.length)` → `this.#sendRestoreCompletedNotifications()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `this.#getWindowStateData()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `this.#getImmutableWindowFeatures()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `this.#log.warn()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Glean.sessionRestore.windowFeaturesMismatchIgnored.record()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Array.from(existingFeatures).join()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Array.from()`
- 条件付き依存: `if (!this.#canRestoreIntoExistingWindow(aWindow, firstWindowState))` → `Array.from(requestedFeatures).join()`
- 参照: `aOptions.restoreSource`, `closedWindow._closedTabs`, `closedWindow._closedTabs?.length`, `closedWindow.closedId`, `ex.message`, `root._closedWindows`, `root.windows`, `root.windows.length`, `root.windows?.length`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#nextClosedId`, `this.#windows`

## _SessionStore.#restoreTabs()
- 位置: L6624-6670
- 役割: 既存のタブデータを、タブ数の差に応じて削り、タブ要素と同じ数に揃えてから選択タブを先頭にして全タブを復元する。選択位置が有効なら、ウィンドウの selected を更新する。
- 触るとき: タブごとのデータを既存のタブ要素と突き合わせる際のずれや、選択タブを先に復元する順序を変えるとき。
- 呼び出し先: `aTabs.indexOf()`, `this.#ensureNoNullsInTabDataList()`, `this.#windowIds.get()`
- 条件付き依存: `if (!(numTabsInWindow == numTabsToRestore))` → `tabsDataArray.splice()`
- 条件付き依存: `if (aSelectTab > 0 && aSelectTab <= aTabs.length)` → `this.#windowIds.get()`
- 条件付き依存: `if (selectedIndex > -1)` → `this.#restoreTab()`
- 条件付き依存: `if (t != selectedIndex)` → `this.#restoreTab()`
- 参照: `aTabs.length`, `aWindow.gBrowser`, `tabbrowser.selectedTab`, `tabbrowser.tabs`, `tabbrowser.tabs.length`, `tabsDataArray.length`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].selected`, `this.#windows[this.#windowIds.get(aWindow)].tabs`

## _SessionStore.#ensureNoNullsInTabDataList()
- 位置: L6675-6698
- 役割: タブデータ配列を、既存タブ要素の数と changedTabPos までの長さに揃え、空の entries と lastAccessed を入れて null の穴を埋める。
- 触るとき: タブデータが未収集のタブでずれたり null になる不具合を調べるとき、またはタブ要素とデータの対応を変えるとき。
- 呼び出し先: `tabDataList.push()`
- 参照: `existingTabEl.lastAccessed`, `tabDataList.length`

## _SessionStore.#restoreTab()
- 位置: L6701-6906
- 役割: タブの状態をウィンドウのタブデータに反映し、アクティブな履歴位置を範囲内に丸め、キャッシュを更新する。接続済みのブラウザなら新しいエポックで履歴を送り、選択中か即時指定なら内容も読み込み、それ以外は復元キューへ入れる。未接続(遅延)なら TAB_LAZY_STATES に URL とタイトルだけを持たせる。最後にピン・非表示・ミュート・ラベルとアイコンを反映する。
- 触るとき: タブ復元の順序(即時、キュー、遅延)や、復元時に保存される項目を変えるとき。
- 呼び出し先: `DirtyWindows.add()`, `Math.max()`, `Math.min()`, `TAB_STATE_FOR_BROWSER.has()`, `lazy.TabStateCache.update()`, `tab.hasAttribute()`, `tab.setAttribute()`, `this.#crashedBrowsers.delete()`, `this.#setWindowStateBusy()`, `this.#setWindowStateReady()`, `this.#updateTabLabelAndIcon()`, `this.#windowIds.get()`, `this.historyIndex()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.has(browser))` → `this.#log.warn()`
- 条件付き依存: `if (tabData.lastAccessed)` → `tab.updateLastAccessed()`
- 条件付き依存: `if (tabData.extData)` → `TAB_CUSTOM_VALUES.set()`
- 条件付き依存: `if (tabData.extData)` → `Cu.cloneInto()`
- 条件付き依存: `if (!(tabData.extData))` → `TAB_CUSTOM_VALUES.delete()`
- 条件付き依存: `if ("attributes" in tabData)` → `lazy.TabAttributes.set()`
- 条件付き依存: `if (isBrowserInserted)` → `this.#startNextEpoch()`
- 条件付き依存: `if (isBrowserInserted)` → `TAB_STATE_FOR_BROWSER.set()`
- 条件付き依存: `if (isBrowserInserted)` → `this.#sendRestoreHistory()`
- 条件付き依存: `if (willRestoreImmediately)` → `this.#restoreTabContent()`
- 条件付き依存: `if (!forceOnDemand)` → `TabRestoreQueue.add()`
- 条件付き依存: `if (!forceOnDemand)` → `TabRestoreQueue.willRestoreSoon()`
- 条件付き依存: `if (activeIndex in tabData.entries)` → `this.#prepareConnectionToHost()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Object.assign()`
- 条件付き依存: `if (!forceOnDemand)` → `this.#restoreNextTab()`
- 条件付き依存: `if (!(isBrowserInserted))` → `TAB_LAZY_STATES.set()`
- 条件付き依存: `if (tabData.pinned)` → `tabbrowser.pinTab()`
- 条件付き依存: `if (!(tabData.pinned))` → `tabbrowser.unpinTab()`
- 条件付き依存: `if (tabData.hidden)` → `tabbrowser.hideTab()`
- 条件付き依存: `if (!(tabData.hidden))` → `tabbrowser.showTab()`
- 条件付き依存: `if (!!tabData.muted != browser.audioMuted)` → `tab.toggleMuteAudio()`
- 条件付き依存: `if (tab.hasAttribute("customizemode"))` → `window.gCustomizeMode.setTab()`
- 参照: `RESTORE_TAB_CONTENT_REASON.NAVIGATE_AND_RESTORE`, `browser.audioMuted`, `browser.isConnected`, `browser.permanentKey`, `options.forceOnDemand`, `options.loadArguments`, `options.restoreContentReason`, `options.restoreImmediately`, `tab.canonicalUrl`, `tab.documentGlobal`, `tab.index`, `tab.linkedBrowser`, `tab.splitview`, `tabData.attributes`, `tabData.canonicalUrl`, `tabData.closedAt`, `tabData.disallow`, `tabData.entries`, `tabData.entries.length`, `tabData.entries[activeIndex].title`, `tabData.entries[activeIndex].url`, `tabData.extData`, `tabData.formdata`, `tabData.hidden`, `tabData.image`, `tabData.index`, `tabData.lastAccessed`, `tabData.muteReason`, `tabData.muted`, `tabData.pinned`, `tabData.scroll`, `tabData.searchMode`, `tabData.storage`, `tabData.userContextId`, `tabData.userTypedClear`, `tabData.userTypedValue`, `tabbrowser.selectedBrowser`, `tabbrowser.selectedTab.splitview`, `this.#windows`, `this.#windows[this.#windowIds.get(window)].tabs`, `window.gBrowser`

## _SessionStore.#restoreTabContent()
- 位置: L6916-6941
- 役割: カスタマイズモード中は読み込みせず、現在の履歴エントリの URL を取り、復元中の印を付けてから復元要求を送る。選択中で空白ページでなければフォーカスを内容領域へ移す。
- 触るとき: タブの内容読み込みの要求が出る条件や、読み込み後のフォーカス移動を変えるとき。
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `aTab.hasAttribute()`, `lazy.TabState.clone()`, `this.#markTabAsRestoring()`, `this.#sendRestoreTabContent()`, `window.isBlankPageURL()`
- 条件付き依存: `if (aTab.selected && !window.isBlankPageURL(uri))` → `browser.focus()`
- 参照: `RESTORE_TAB_CONTENT_REASON.SET_STATE`, `aOptions.loadArguments`, `aOptions.restoreContentReason`, `aTab.documentGlobal`, `aTab.linkedBrowser`, `aTab.selected`, `activePageData.url`, `tabData.entries`, `tabData.index`

## _SessionStore.#markTabAsRestoring()
- 位置: L6949-6965
- 役割: タブが NEEDS_RESTORE であることを確かめてから、復元キューから外し、復元中の件数を増やし、状態を RESTORING にして pending と discarded の属性を外す。違えば例外。
- 触るとき: 復元中の件数や状態遷移を変えるとき、または復元が二重に始まる原因を調べるとき。
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `TAB_STATE_FOR_BROWSER.set()`, `TabRestoreQueue.remove()`, `aTab.removeAttribute()`
- 参照: `aTab.linkedBrowser`, `this.#tabsRestoringCount`

## _SessionStore.#restoreNextTab()
- 位置: L6975-6990
- 役割: 終了中でなく、同時復元中のタブ数が MAX_CONCURRENT_TAB_RESTORES 未満なら、復元キューの先頭タブの内容読み込みを始める。
- 触るとき: 復元キューの処理順や同時に読み込むタブ数の上限を変えるとき。
- 呼び出し先: `TabRestoreQueue.shift()`
- 条件付き依存: `if (tab)` → `this.#restoreTabContent()`
- 参照: `lazy.RunState.isQuitting`, `this.#tabsRestoringCount`

## _SessionStore.#restoreWindowFeatures()
- 位置: L7002-7053
- 役割: 保存時の AI ウィンドウ種別を戻す(既定の新規起動ウィンドウだけ Smart にする)。次のタスクで寸法を反映するが、その前に最小化されていれば寸法は適用しない。
- 触るとき: AI ウィンドウ種別の判定や、寸法を適用するタイミングを変えるとき。
- 呼び出し先: `Promise.withResolvers()`, `aWindow.setTimeout()`, `lazy.AIWindow.isAIWindowActive()`, `lazy.AIWindow.isAIWindowEnabled()`, `lazy.AIWindow.shouldOpenAsSmartWindow()`, `lazy.SessionStartup.willRestore()`, `promiseParts.resolve()`, `this.#restoreDimensions()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowActive(aWindow) !== shouldBeAIWindow)` → `lazy.AIWindow.toggleAIWindow()`
- 条件付き依存: `if (shouldBeAIWindow)` → `lazy.AIWindow.recordOpenWindowTelemetry()`
- 条件付き依存: `if (minimizedWhilePending)` → `promiseParts.resolve()`
- 参照: `aOptions.firstWindow`, `aOptions.trigger`, `aWinData.height`, `aWinData.isAIWindow`, `aWinData.screenX`, `aWinData.screenY`, `aWinData.sizemode`, `aWinData.sizemodeBeforeMinimized`, `aWinData.width`, `aWindow.STATE_MINIMIZED`, `aWindow.windowState`, `promiseParts.promise`

## _SessionStore.#restoreSidebar()
- 位置: L7064-7070
- 役割: ポップアップでなくサイドバーの保存状態があれば、復元を受け取ったことを SidebarController に伝えてから UI 状態を更新する。
- 触るとき: サイドバーの表示状態が起動時や復元時に戻らない問題を調べるとき。
- 呼び出し先: `aWindow.SidebarController.markSessionRestoreStateReceived()`, `aWindow.SidebarController.updateUIState()`

## _SessionStore.#restoreDimensions()
- 位置: L7090-7244
- 役割: 保存された位置とサイズを、現在の画面の利用可能領域に収まるように補正してから適用し、最大化・最小化・通常の状態も戻す。サイズを丸める fingerprinting 抵抗が有効ならサイズは変えない。
- 触るとき: ウィンドウが画面外に出る不具合、マルチディスプレイでの位置補正、サイズモードの復元を変えるとき。
- 呼び出し先: `ChromeUtils.shouldResistFingerprinting()`, `dwu.suppressAnimation()`, `isNaN()`, `lazy.gScreenManager.screenForRect()`, `this.#windowIds.get()`, `win_()`
- 条件付き依存: `if (screen)` → `screen.GetAvailRectDisplayPix()`
- 条件付き依存: `if (screen)` → `Math.max()`
- 条件付き依存: `if (aLeft > screenLeft)` → `Math.max()`
- 条件付き依存: `if (aTop > screenTop)` → `Math.max()`
- 条件付き依存: `if ( !isNaN(aLeft) && !isNaN(aTop) && (aLeft != win_("screenX") || aTop != win_("screenY")) )` → `getBaseWindow(aWindow).setPositionDesktopPix()`
- 条件付き依存: `if ( !isNaN(aLeft) && !isNaN(aTop) && (aLeft != win_("screenX") || aTop != win_("screenY")) )` → `getBaseWindow()`
- 条件付き依存: `if ( !isNaN(aLeft) && !isNaN(aTop) && (aLeft != win_("screenX") || aTop != win_("screenY")) )` → `Math.round()`
- 条件付き依存: `if ( aWidth && aHeight && (aWidth != win_("width") || aHeight != win_("height")) && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `win_()`
- 条件付き依存: `if (aSizeMode != "maximized" || win_("sizemode") != "maximized")` → `aWindow.resizeTo()`
- 条件付き依存: `if ( aSizeMode && win_("sizemode") != aSizeMode && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `aWindow.maximize()`
- 条件付き依存: `if (aSizeModeBeforeMinimized == "maximized")` → `aWindow.maximize()`
- 条件付き依存: `if ( aSizeMode && win_("sizemode") != aSizeMode && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `aWindow.minimize()`
- 条件付き依存: `if ( aSizeMode && win_("sizemode") != aSizeMode && !ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null) )` → `aWindow.restore()`
- 条件付き依存: `if (this.#windowToFocus)` → `this.#windowToFocus.focus()`
- 参照: `height.value`, `left.value`, `screen.contentsScaleFactor`, `screen.defaultCSSScaleFactor`, `this.#windowToFocus`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].sizemodeBeforeMinimized`, `top.value`, `width.value`, `win.screenEdgeSlopX`, `win.screenEdgeSlopY`, `win.windowUtils`

## win_()
- 位置: L7100-7100
- 役割: 対象ウィンドウの現在の寸法や状態(screenX、width、sizemode など)を #getWindowDimension で取り出す補助関数。
- 触るとき: #restoreDimensions で比較する値を増やすとき。
- 呼び出し先: `this.#getWindowDimension()`

## _SessionStore.#saveStateDelayed()
- 位置: L7255-7261
- 役割: 指定ウィンドウがあれば DirtyWindows に入れ、SessionSaver の遅延保存を予約する。
- 触るとき: 状態変化から実際にディスクへ書かれるまでの遅延や、再収集の対象を変えるとき。
- 呼び出し先: `lazy.SessionSaver.runDelayed()`
- 条件付き依存: `if (aWindow)` → `DirtyWindows.add()`

## _SessionStore.#removeClosedWindow()
- 位置: L7274-7287
- 役割: 閉じたウィンドウ一覧の指定位置を外し、その中の閉じたタブと閉じたウィンドウの閉じた操作の履歴も消して、変更通知を立てる。取り除いた要素を返す。
- 触るとき: 閉じたウィンドウを開き直す・忘れる・上限で切るときに、閉じた操作の履歴と一覧がずれないかを確認するとき。
- 呼び出し先: `this.#closedWindows.splice()`, `this.#removeClosedAction()`
- 参照: `closedTab.closedId`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows[index]._closedTabs`, `this.#closedWindows[index].closedId`, `this.LAST_ACTION_CLOSED_TAB`, `this.LAST_ACTION_CLOSED_WINDOW`

## _SessionStore.#notifyOfClosedObjectsChange()
- 位置: L7293-7301
- 役割: 閉じた項目の一覧が変わっていれば変更フラグを戻し、次のタスクで NOTIFY_CLOSED_OBJECTS_CHANGED を通知する。
- 触るとき: 閉じた項目の変更通知が必要な操作を追加するとき、または通知が重複・欠落しないかを調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.setTimeout()`
- 参照: `this.#closedObjectsChanged`
- XPCOM: `Services.obs`

## _SessionStore.#notifyOfSavedTabGroupsChange()
- 位置: L7307-7311
- 役割: 次のタスクで NOTIFY_SAVED_TAB_GROUPS_CHANGED を通知する。フラグは見ずに毎回通知する。
- 触るとき: 保存済みタブグループの変更通知を受ける側が更新されないとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.setTimeout()`
- XPCOM: `Services.obs`

## _SessionStore.#updateSessionStartTime()
- 位置: L7320-7325
- 役割: 状態に session.startTime があれば、セッション開始時刻として保持する。
- 触るとき: セッション開始時刻の引き継ぎ方や、セッション日数の計算元を変えるとき。
- 参照: `state.session`, `state.session.startTime`, `this.#sessionStartTime`

## _SessionStore.[Symbol.iterator]()
- 位置: L7334-7340
- 役割: ウィンドウ ID を持ち閉じていない browser ウィンドウを、BrowserWindowTracker の順(フォーカス順)で列挙する。
- 触るとき: 全ウィンドウを対象にする処理の順序や、対象外になるウィンドウの条件を変えるとき。
- 呼び出し先: `SessionStore.getWindowId()`
- 参照: `Symbol.iterator`, `lazy.BrowserWindowTracker.orderedWindows`, `window.closed`

## _SessionStore.[Symbol.iterator]()
- 位置: L7349-7371
- 役割: 同じく閉じていないウィンドウを列挙するが、最小化されたウィンドウを最後に回す。
- 触るとき: 状態収集や保存時に、最小化ウィンドウをどの順で処理するかを変えるとき。
- 呼び出し先: `SessionStore.getWindowId()`, `windows.sort()`
- 参照: `Symbol.iterator`, `a.STATE_MINIMIZED`, `a.windowState`, `b.STATE_MINIMIZED`, `b.windowState`, `lazy.BrowserWindowTracker.orderedWindows`, `window.closed`

## _SessionStore.#getTopWindow()
- 位置: L7382-7390
- 役割: BrowserWindowTracker から最前面のウィンドウを取得する。isPrivate を指定すると、そのプライベート状態のものに限り、ポップアップも含める。
- 触るとき: 「最前面のウィンドウ」を基準にする処理(閉じたタブの復元先など)の対象を変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 参照: `options.private`

## _SessionStore.#handleClosedWindows()
- 位置: L7397-7405
- 役割: まだ破棄されていないが閉じているウィンドウについて #onClose を呼び、その完了を待つ Promise を返す。
- 触るとき: getBrowserState や setBrowserState の前に、閉じかけのウィンドウを開いたウィンドウとして扱わないようにしたいとき。
- 呼び出し先: `Promise.all()`, `Services.wm.getEnumerator()`
- 条件付き依存: `if (window.closed)` → `promises.push()`
- 条件付き依存: `if (window.closed)` → `this.#onClose()`
- 参照: `window.closed`
- XPCOM: `Services.wm`

## _SessionStore.#updateWindowRestoreState()
- 位置: L7417-7427
- 役割: ウィンドウの z 順(あれば)を記録し、ランダムな ID を振って、そのウィンドウの復元状態を #statesToRestore に保存する。
- 触るとき: 複数ウィンドウの復元を後から z 順で実行する仕組みや、復元待ちの状態の保存先を変えるとき。
- 呼び出し先: `Math.random()`, `WINDOW_RESTORE_IDS.set()`
- 条件付き依存: `if ("zIndex" in state.windows[0])` → `WINDOW_RESTORE_ZINDICES.set()`
- 参照: `state.windows`, `state.windows[0].zIndex`, `this.#statesToRestore`

## _SessionStore.#openWindowWithState()
- 位置: L7437-7538
- 役割: 保存された chromeFlags(無ければ既定の features)、位置・サイズ、private や AI ウィンドウの指定から features を組み立て、ブラウザウィンドウを開く。復元状態を #updateWindowRestoreState に登録し、表示完了を待つ Promise を作る。
- 触るとき: 新しいウィンドウを状態から開くときの features の組み立て、またはプライベートや AI ウィンドウの開き方を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`, `JSON.stringify()`, `Promise.withResolvers()`, `Services.ww.openWindow()`, `WINDOW_ATTRIBUTES.forEach()`, `WINDOW_SHOWING_PROMISES.set()`, `args.appendElement()`, `args.queryElementAt()`, `features.join()`, `isNaN()`, `this.#log.debug()`, `this.#serializePropertyBag()`, `this.#updateWindowRestoreState()`
- 条件付き依存: `if (hasAll)` → `features.push()`
- 条件付き依存: `if (value)` → `features.push()`
- 条件付き依存: `if (!(winState.chromeFlags))` → `features.push()`
- 条件付き依存: `if (winState.isPopup)` → `features.push()`
- 条件付き依存: `if (!(winState.isPopup))` → `features.push()`
- 条件付き依存: `if (aFeature in winState && !isNaN(winState[aFeature]))` → `features.push()`
- 条件付き依存: `if (winState.isPrivate)` → `features.push()`
- 条件付き依存: `if (tab.entries.length)` → `this.historyIndex()`
- 条件付き依存: `if (winState.isAIWindow)` → `lazy.AIWindow.handleAIWindowOptions()`
- 条件付き依存: `if (!args.length)` → `args.appendElement()`
- 条件付き依存: `if (winState.args?.[ARG_WEB_EXTENSION_POPUP_WINDOW])` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (winState.args?.[ARG_CHROMELESS_WINDOW])` → `extraOptions.setPropertyAsBool()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `Ci.nsIMutableArray`, `Ci.nsIWebBrowserChrome.CHROME_ALL`, `Ci.nsIWritablePropertyBag2`, `aState.windows`, `args.length`, `tab.entries`, `tab.entries.length`, `tab.entries[activeIndex].url`, `winState.args`, `winState.chromeFlags`, `winState.closedId`, `winState.isAIWindow`, `winState.isPopup`, `winState.isPrivate`, `winState.selected`, `winState.tabs`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIWebBrowserChrome`](../../../dom/interfaces/base/nsIBrowserChild.idl.md) / [`nsIWritablePropertyBag2`](../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `Services.ww`

## _SessionStore.#serializePropertyBag()
- 位置: L7547-7553
- 役割: プロパティバッグの各名前と値を、プレーンなオブジェクトにまとめる。デバッグ出力用。
- 触るとき: ウィンドウを開くときのデバッグログの内容を変えるとき。
- 参照: `bag.enumerator`

## _SessionStore.#isCmdLineEmpty()
- 位置: L7567-7587
- 役割: 状態のタブがすべてピン留めなら、コマンドライン引数の先頭が既定の引数でなければ「ある」と判定する。結果は、起動時にタブを上書きしてよいかの判断に使われる。
- 触るとき: 起動引数によって保存済みのタブを上書きするかの判定条件を変えるとき。
- 呼び出し先: `aState.windows.every()`, `win.tabs.every()`
- 条件付き依存: `if (!pinnedOnly)` → `Cc["@mozilla.org/browser/clh;1"].getService()`
- 参照: `Cc["@mozilla.org/browser/clh;1"].getService( Ci.nsIBrowserHandler ).defaultArgs`, `Ci.nsIBrowserHandler`, `aState.windows`, `aWindow.arguments`, `tab.pinned`
- XPCOM: [`nsIBrowserHandler`](../nsIBrowserHandler.idl.md) / `@mozilla.org/browser/clh;1`

## _SessionStore.#getWindowDimension()
- 位置: L7602-7666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `baseWin.getPosition()`, `getBaseWindow()`
- 条件付き依存: `if (aWindow.windowState != aWindow.STATE_NORMAL)` → `parseInt()`
- 条件付き依存: `if (aWindow.windowState != aWindow.STATE_NORMAL)` → `docElem.getAttribute()`
- 条件付き依存: `if (attr)` → `aWindow.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (attr)` → `aWindow.docShell.treeOwner .QueryInterface()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `aWindow.STATE_FULLSCREEN`, `aWindow.STATE_MAXIMIZED`, `aWindow.STATE_MINIMIZED`, `aWindow.STATE_NORMAL`, `aWindow.document.documentElement`, `aWindow.outerHeight`, `aWindow.outerWidth`, `aWindow.windowState`, `appWin.outerToInnerHeightDifferenceInCSSPixels`, `appWin.outerToInnerWidthDifferenceInCSSPixels`, `baseWin.devicePixelsPerDesktopPixel`, `x.value`, `y.value`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md)

## _SessionStore.#needsRestorePage()
- 位置: L7678-7722
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.#hasSingleTabWithURL()`, `this.#prefBranch.getIntPref()`
- 参照: `Services.appinfo.inSafeMode`, `aState.session`, `aState.session.lastUpdate`, `aState.windows`, `winData.length`
- XPCOM: `Services.appinfo`

## _SessionStore.#hasSingleTabWithURL()
- 位置: L7732-7744
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aWinData.length`, `aWinData[0].tabs`, `aWinData[0].tabs.length`, `aWinData[0].tabs[0].entries`, `aWinData[0].tabs[0].entries.length`, `aWinData[0].tabs[0].entries[0].url`

## _SessionStore.#shouldSaveTabState()
- 位置: L7755-7771
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aTabState.entries`, `aTabState.entries.length`, `aTabState.entries[0]?.url`, `aTabState.splitViewId`, `aTabState.userTypedValue`

## _SessionStore.shouldSaveTabsToGroup()
- 位置: L7784-7795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.TabState.collect()`, `this.#shouldSaveTabState()`

## _SessionStore.#shouldSaveTab()
- 位置: L7808-7818
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aTabState.attributes`, `aTabState.attributes.customizemode`, `aTabState.entries`, `aTabState.entries.length`, `aTabState.entries[0].url`, `aTabState.userTypedValue`

## _SessionStore.keepOnlyWorthSavingTabs()
- 位置: L7827-7857
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aState._closedWindows.some()`, `this.#shouldSaveTab()`
- 条件付き依存: `if (!this.#shouldSaveTab(tab))` → `win.tabs.splice()`
- 条件付き依存: `if ( !win.tabs.length && (aState.windows.length > 1 || closedWindowShouldRestore || (closedWindowShouldRestore == null && (closedWindowShouldRestore = aState._cl...)` → `aState.windows.splice()`
- 参照: `aState.selectedWindow`, `aState.windows`, `aState.windows.length`, `w._shouldRestore`, `win.selected`, `win.tabs`, `win.tabs.length`

## _SessionStore.#prepDataForDeferredRestore()
- 位置: L7880-8067
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `defaultState.savedGroups.find()`, `groupsToSave.forEach()`
- 条件付き依存: `if (PERSIST_SESSIONS)` → `Cu.cloneInto()`
- 条件付き依存: `if (window.tabs[tIndex].pinned)` → `newWindowState.tabs.concat()`
- 条件付き依存: `if (window.tabs[tIndex].pinned)` → `window.tabs.splice()`
- 条件付き依存: `if (window.tabs[tIndex].groupId)` → `window.groups.find()`
- 条件付き依存: `if (window.tabs[tIndex].groupId)` → `groupsToSave.get()`
- 条件付き依存: `if (!groupToSave)` → `lazy.TabGroupState.savedInClosedWindow()`
- 条件付き依存: `if (!groupToSave)` → `groupsToSave.set()`
- 条件付き依存: `if (window.tabs[tIndex].groupId)` → `this.formatTabStateForSavedGroup()`
- 条件付き依存: `if (tabData)` → `groupToSave.tabs.push()`
- 条件付き依存: `if (!window.tabs[tIndex].hidden && PERSIST_SESSIONS)` → `Math.min()`
- 条件付き依存: `if (!window.tabs[tIndex].hidden && PERSIST_SESSIONS)` → `Math.max()`
- 条件付き依存: `if (activeIndex in tabState.entries)` → `Date.now()`
- 条件付き依存: `if (activeIndex in tabState.entries)` → `this.#shouldSaveTabState()`
- 条件付き依存: `if (this.#shouldSaveTabState(tabState))` → `this.#saveClosedTabData()`
- 条件付き依存: `if (!(alreadySavedGroup))` → `defaultState.savedGroups.push()`
- 条件付き依存: `if (newWindowState.tabs.length)` → `WINDOW_ATTRIBUTES.forEach()`
- 条件付き依存: `if (newWindowState.tabs.length)` → `Date.now()`
- 条件付き依存: `if (newWindowState.tabs.length)` → `Math.random()`
- 条件付き依存: `if ( newWindowState.tabs.length || (PERSIST_SESSIONS && (newWindowState._closedTabs.length || newWindowState.closedGroups.length)) )` → `defaultState.windows.push()`
- 条件付き依存: `if (!window.tabs.length)` → `state.windows.splice()`
- 参照: `alreadySavedGroup.removeAfterRestore`, `defaultState.cookies`, `defaultState.savedGroups`, `defaultState.selectedIndex`, `defaultState.windows.length`, `existingGroup.id`, `group.removeAfterRestore`, `groupState.id`, `groupStateToSave.id`, `groupToSave.removeAfterRestore`, `newWindowState.__lastSessionWindowID`, `newWindowState._closedTabs`, `newWindowState._closedTabs.length`, `newWindowState.closedGroups`, `newWindowState.closedGroups.length`, `newWindowState.selected`, `newWindowState.sidebar`, `newWindowState.tabs`, `newWindowState.tabs.length`, `state.cookies`, `state.savedGroups`, `state.selectedWindow`, `state.windows`, `state.windows.length`, `tabState.entries`, `tabState.entries.length`, `tabState.entries[activeIndex].title`, `tabState.entries[activeIndex].url`, `tabState.image`, `tabState.index`, `window.__lastSessionWindowID`, `window._closedTabs`, `window.closedGroups`, `window.selected`, `window.sidebar`, `window.tabs`, `window.tabs.length`, `window.tabs[tIndex].groupId`, `window.tabs[tIndex].hidden`, `window.tabs[tIndex].pinned`

## _SessionStore.#sendRestoreCompletedNotifications()
- 位置: L8069-8109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserWindows [Symbol.iterator]()`, `this.#browserWindows [Symbol.iterator]() .some()`
- 条件付き依存: `if (this.#restoreCount > 1)` → `this.#log.warn()`
- 条件付き依存: `if (!this.#browserSetState)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!this.#browserSetState)` → `this.#log.debug()`
- 条件付き依存: `if (!this.#browserSetState)` → `this.#maybeOpenNewTabAfterRestore()`
- 条件付き依存: `if (!this.#browserSetState)` → `this.#deferredAllWindowsRestored.resolve()`
- 条件付き依存: `if (!(!this.#browserSetState))` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (!anyWindowNotCloaked)` → `lazy.BrowserWindowTracker.openWindow()`
- 参照: `Symbol.iterator`, `this.#browserSetState`, `this.#browserWindows`, `this.#restoreCount`, `window.isCloaked`
- XPCOM: `Services.obs`

## _SessionStore.#isNewTabURL()
- 位置: L8111-8113
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AboutNewTab.newTabURL`

## _SessionStore.#getActiveURLFromTabData()
- 位置: L8115-8123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `this.historyIndex()`
- 参照: `tabData.entries`, `tabData.entries.length`, `tabData.entries[activeIndex]?.url`, `tabData?.entries?.length`

## _SessionStore.#maybeOpenNewTabAfterRestore()
- 位置: L8125-8213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.sessionRestore.startupSessionAutoRestored.record()`, `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.NimbusFeatures.sessionRestoreNewTab.recordExposureEvent()`, `this.#log.debug()`, `this.#windowIds.get()`, `win.gBrowser.addTrustedTab()`
- 条件付き依存: `if (!this.#isUserConfiguredRestore)` → `this.#log.debug()`
- 条件付き依存: `if (!newTabOnRestore || !showSetting)` → `this.#log.debug()`
- 条件付き依存: `if (!newTabOnRestore || !showSetting)` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (this.#cmdLineHadURLOnStartup)` → `this.#log.debug()`
- 条件付き依存: `if (this.#cmdLineHadURLOnStartup)` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (windowState?.tabs?.length)` → `this.#getActiveURLFromTabData()`
- 条件付き依存: `if (windowState?.tabs?.length)` → `this.#isNewTabURL()`
- 条件付き依存: `if (this.#isNewTabURL(selectedURL))` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (this.#isNewTabURL(selectedURL))` → `this.#log.debug()`
- 条件付き依存: `if (windowState?.tabs?.length)` → `windowState.tabs.at()`
- 条件付き依存: `if (this.#isNewTabURL(lastTabURL))` → `win.gBrowser.visibleTabs.at()`
- 条件付き依存: `if (this.#isNewTabURL(lastTabURL))` → `Glean.sessionRestore.startupSessionAutoRestored.record()`
- 条件付き依存: `if (this.#isNewTabURL(lastTabURL))` → `this.#log.debug()`
- 参照: `lazy.AboutNewTab.newTabURL`, `this.#cmdLineHadURLOnStartup`, `this.#isUserConfiguredRestore`, `this.#windows`, `win.gBrowser.selectedTab`, `windowState.selected`, `windowState.tabs`, `windowState?.tabs?.length`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## _SessionStore.#setWindowStateBusyValue()
- 位置: L8223-8233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isWindowLoaded()`, `this.#windowIds.get()`
- 条件付き依存: `if (!this.#isWindowLoaded(aWindow))` → `WINDOW_RESTORE_IDS.get()`
- 参照: `stateToRestore.busy`, `this.#statesToRestore`, `this.#statesToRestore[WINDOW_RESTORE_IDS.get(aWindow)].windows`, `this.#windows`, `this.#windows[this.#windowIds.get(aWindow)].busy`

## _SessionStore.#setWindowStateReady()
- 位置: L8241-8252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowBusyStates.get()`, `this.#windowBusyStates.set()`
- 条件付き依存: `if (newCount == 0)` → `this.#setWindowStateBusyValue()`
- 条件付き依存: `if (newCount == 0)` → `this.#sendWindowStateReadyEvent()`

## _SessionStore.#setWindowStateBusy()
- 位置: L8260-8268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowBusyStates.get()`, `this.#windowBusyStates.set()`
- 条件付き依存: `if (newCount == 1)` → `this.#setWindowStateBusyValue()`
- 条件付き依存: `if (newCount == 1)` → `this.#sendWindowStateBusyEvent()`

## _SessionStore.#sendWindowStateReadyEvent()
- 位置: L8276-8280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendWindowStateBusyEvent()
- 位置: L8288-8292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendWindowRestoringNotification()
- 位置: L8300-8304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendWindowRestoredNotification()
- 位置: L8312-8316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.dispatchEvent()`, `aWindow.document.createEvent()`, `event.initEvent()`

## _SessionStore.#sendTabRestoredNotification()
- 位置: L8324-8328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aTab.dispatchEvent()`, `aTab.ownerDocument.createEvent()`, `event.initEvent()`

## _SessionStore.#isWindowLoaded()
- 位置: L8337-8339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WINDOW_RESTORE_IDS.has()`

## _SessionStore.#capClosedWindows()
- 位置: L8346-8368
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (spliceTo < this.#closedWindows.length)` → `this.#closedWindows.splice()`
- 参照: `AppConstants.platform`, `this.#closedObjectsChanged`, `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[normalWindowIndex].isPopup`, `this.#max_windows_undo`

## _SessionStore.#clearRestoringWindows()
- 位置: L8379-8383
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#closedWindows`, `this.#closedWindows.length`, `this.#closedWindows[i]._shouldRestore`

## _SessionStore.#resetRestoringState()
- 位置: L8388-8391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabRestoreQueue.reset()`
- 参照: `this.#tabsRestoringCount`

## _SessionStore.#resetLocalTabRestoringState()
- 位置: L8400-8430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.delete()`, `TAB_STATE_FOR_BROWSER.get()`, `aTab.removeAttribute()`, `browser.browsingContext.clearRestoreState()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`
- 条件付き依存: `if (!previousState)` → `console.error()`
- 条件付き依存: `if (previousState == TAB_STATE_NEEDS_RESTORE)` → `TabRestoreQueue.remove()`
- 参照: `aTab.linkedBrowser`, `browser.permanentKey`, `this.#tabsRestoringCount`

## _SessionStore.#resetTabRestoringState()
- 位置: L8432-8441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.has()`, `this.#resetLocalTabRestoringState()`
- 条件付き依存: `if (!TAB_STATE_FOR_BROWSER.has(browser))` → `console.error()`
- 参照: `tab.linkedBrowser`

## _SessionStore.#startNextEpoch()
- 位置: L8452-8456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserEpochs.set()`, `this.#getCurrentEpoch()`

## _SessionStore.#getCurrentEpoch()
- 位置: L8465-8467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserEpochs.get()`

## _SessionStore.#isCurrentEpoch()
- 位置: L8481-8483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getCurrentEpoch()`

## _SessionStore.#resetEpoch()
- 位置: L8495-8500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserEpochs.delete()`
- 条件付き依存: `if (frameLoader)` → `frameLoader.requestEpochUpdate()`

## _SessionStore.#looseTimer()
- 位置: L8511-8535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `Math.ceil()`, `Promise.withResolvers()`, `deferred.promise.then()`, `timer.cancel()`, `timer.initWithCallback()`
- 条件付き依存: `if (beats <= 0)` → `this.#log.debug()`
- 条件付き依存: `if (beats <= 0)` → `Glean.sessionRestore.shutdownFlushAllOutcomes.timed_out.add()`
- 条件付き依存: `if (beats <= 0)` → `deferred.resolve()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_REPEATING_PRECISE_CAN_SKIP`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## _SessionStore.#waitForStateStop()
- 位置: L8537-8588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.withResolvers()`, `browser.addProgressListener()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`, `this.#restoreListeners.set()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`, `deferred.promise`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.unregister()
- 位置: L8541-8554
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.#restoreListeners.delete()`, `browser.removeProgressListener()`
- 条件付き依存: `if (reject)` → `deferred.reject()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.onStateChange()
- 位置: L8556-8571
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( webProgress.isTopLevel && stateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && stateFlags & Ci.nsIWebProgressListener.STATE_STOP )` → `request.QueryInterface()`
- 条件付き依存: `if (url !== "about:blank" || aboutBlankOK)` → `this.unregister()`
- 条件付き依存: `if (url !== "about:blank" || aboutBlankOK)` → `deferred.resolve()`
- 参照: `Ci.nsIChannel`, `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_STOP`, `request.QueryInterface(Ci.nsIChannel).originalURI.spec`, `webProgress.isTopLevel`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _SessionStore.#listenForNavigations()
- 位置: L8590-8643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `browser.addProgressListener()`, `browser.browsingContext?.sessionHistory?.addSHistoryListener()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`, `this.#restoreListeners.set()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.unregister()
- 位置: L8592-8603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.#restoreListeners.delete()`, `browser.browsingContext?.sessionHistory?.removeSHistoryListener()`, `browser.removeProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `browser.permanentKey`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## _SessionStore.OnHistoryReload()
- 位置: L8605-8608
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callbacks.onHistoryReload()`, `this.unregister()`

## _SessionStore.OnHistoryNewEntry()
- 位置: L8611-8611
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.OnHistoryGotoIndex()
- 位置: L8612-8612
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.OnHistoryPurge()
- 位置: L8613-8613
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.OnHistoryReplaceEntry()
- 位置: L8614-8614
- 役割: (未記入)
- 触るとき: (未記入)

## _SessionStore.onStateChange()
- 位置: L8616-8625
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( webProgress.isTopLevel && stateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && stateFlags & Ci.nsIWebProgressListener.STATE_START )` → `this.unregister()`
- 条件付き依存: `if ( webProgress.isTopLevel && stateFlags & Ci.nsIWebProgressListener.STATE_IS_WINDOW && stateFlags & Ci.nsIWebProgressListener.STATE_START )` → `callbacks.onStartRequest()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_WINDOW`, `Ci.nsIWebProgressListener.STATE_START`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _SessionStore.#restoreHistory()
- 位置: L8653-8701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStoreUtils.restoreDocShellState()`, `browser.stop()`, `lazy.SessionHistory.restoreFromParent()`, `promise.then()`, `promise.then(onResolve).catch()`, `this.#tabStateRestorePromises.set()`, `this.#tabStateToRestore.set()`
- 参照: `browser.browsingContext`, `browser.browsingContext.sessionHistory`, `browser.permanentKey`, `data.tabData`, `data.tabData.index`, `data.tabData?.disallow`, `data.tabData?.entries`, `data.tabData?.entries[data.tabData.index - 1]?.url`

## onResolve()
- 位置: L8675-8698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `this.#restoreHistoryComplete()`, `this.#tabStateRestorePromises.delete()`
- 条件付き依存: `if (TAB_STATE_FOR_BROWSER.get(browser) !== TAB_STATE_RESTORING)` → `this.#listenForNavigations()`
- 参照: `browser.permanentKey`

## onHistoryReload()
- 位置: L8680-8683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreTabContentForBrowser()`

## onStartRequest()
- 位置: L8688-8691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreTabContentForBrowser()`, `this.#tabStateToRestore.delete()`
- 参照: `browser.permanentKey`

## _SessionStore.#restoreTabEntry()
- 位置: L8712-8746
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `browser.browsingContext.fixupAndLoadURIString()`, `this.#waitForStateStop()`
- 条件付き依存: `if (!haveUserTypedValue && tabData.entries.length)` → `SessionStoreUtils.initializeRestore()`
- 条件付き依存: `if (!haveUserTypedValue && tabData.entries.length)` → `lazy.SessionStoreHelper.buildRestoreData()`
- 条件付き依存: `if (!haveUserTypedValue)` → `this.#waitForStateStop()`
- 条件付き依存: `if (!haveUserTypedValue)` → `browser.browsingContext.loadURI()`
- 参照: `Ci.nsIWebNavigation.LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP`, `Ci.nsIWebNavigation.LOAD_FLAGS_BYPASS_HISTORY`, `browser.browsingContext`, `lazy.blankURI`, `tabData.entries.length`, `tabData.formdata`, `tabData.scroll`, `tabData.userTypedClear`, `tabData.userTypedValue`
- XPCOM: [`nsIWebNavigation`](../../../docshell/base/nsIWebNavigation.idl.md) / `Services.scriptSecurityManager`

## _SessionStore.#restoreTabContentForBrowser()
- 位置: L8757-8779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `Promise.allSettled(promises).then()`, `this.#restoreListeners.get()`, `this.#restoreListeners.get(browser.permanentKey)?.unregister()`, `this.#restoreTabContentComplete()`, `this.#restoreTabContentStarted()`, `this.#tabStateRestorePromises.get()`, `this.#tabStateToRestore.delete()`, `this.#tabStateToRestore.get()`
- 条件付き依存: `if (state)` → `promises.push()`
- 条件付き依存: `if (state)` → `this.#restoreTabEntry()`
- 条件付き依存: `if (!(state))` → `promises.push()`
- 条件付き依存: `if (!(state))` → `this.#waitForStateStop()`
- 参照: `browser.permanentKey`, `state.tabData`

## _SessionStore.#sendRestoreTabContent()
- 位置: L8781-8783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreTabContentForBrowser()`

## _SessionStore.#restoreHistoryComplete()
- 位置: L8785-8801
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_CUSTOM_VALUES.get()`, `event.initEvent()`, `lazy.TabState.collect()`, `tab.dispatchEvent()`, `this.#updateTabLabelAndIcon()`, `win.document.createEvent()`, `win?.gBrowser.getTabForBrowser()`
- 参照: `browser.documentGlobal`

## _SessionStore.#restoreTabContentStarted()
- 位置: L8803-8870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_STATE_FOR_BROWSER.get()`, `lazy.TabStateCache.get()`, `win?.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!initiatedBySessionStore || isNavigateAndRestore)` → `lazy.TabStateCache.update()`
- 条件付き依存: `if (!initiatedBySessionStore)` → `this.#markTabAsRestoring()`
- 条件付き依存: `if (!isNavigateAndRestore)` → `lazy.TabState.collect()`
- 条件付き依存: `if (!isNavigateAndRestore)` → `TAB_CUSTOM_VALUES.get()`
- 条件付き依存: `if (tab.selected)` → `win.gURLBar.setURI()`
- 条件付き依存: `if (!isNavigateAndRestore)` → `lazy.TabStateCache.update()`
- 参照: `RESTORE_TAB_CONTENT_REASON.NAVIGATE_AND_RESTORE`, `browser.documentGlobal`, `browser.permanentKey`, `browser.userTypedValue`, `cacheState.searchMode`, `data.reason`, `tab.selected`, `tabData.userTypedClear`, `tabData.userTypedValue`

## _SessionStore.#restoreTabContentComplete()
- 位置: L8872-8905
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `SessionStore.#resetLocalTabRestoringState()`, `SessionStore.#restoreNextTab()`, `lazy.TabStateCache.get()`, `this.#sendTabRestoredNotification()`, `win?.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (cacheState.searchMode)` → `win.gURLBar.setSearchMode()`
- 条件付き依存: `if (tab.selected)` → `win.gURLBar.setURI()`
- 条件付き依存: `if (cacheState.searchMode)` → `lazy.TabStateCache.update()`
- 条件付き依存: `if (gDebuggingEnabled)` → `Services.obs.notifyObservers()`
- 参照: `browser.documentGlobal`, `browser.permanentKey`, `browser.userTypedValue`, `cacheState.searchMode`, `cacheState.userTypedValue`, `tab.selected`
- XPCOM: `Services.obs`

## _SessionStore.#sendRestoreHistory()
- 位置: L8919-8933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#restoreHistory()`
- 条件付き依存: `if (options.tabData.storage)` → `SessionStoreUtils.restoreSessionStorageFromParent()`
- 条件付き依存: `if (browser && browser.frameLoader)` → `browser.frameLoader.requestEpochUpdate()`
- 参照: `browser.browsingContext`, `browser.frameLoader`, `options.epoch`, `options.tabData.storage`

## _SessionStore.addSavedTabGroup()
- 位置: L8940-8957
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `lazy.TabGroupState.savedInOpenWindow()`, `this.#collectClosedTabsForTabGroup()`, `this.#collectSplitViewDataForTabGroup()`, `this.#recordSavedTabGroupState()`, `this.#windowIds.get()`
- 参照: `tabGroup.documentGlobal`, `tabGroup.tabs`, `tabGroupState.splitViews`, `tabGroupState.tabs`

## _SessionStore.addTabsToSavedGroup()
- 位置: L8968-9007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.addTab.record()`, `PrivateBrowsingUtils.isWindowPrivate()`, `tabGroupState.splitViews.push()`, `tabGroupState.tabs.push()`, `tabs.every()`, `this.#collectClosedTabsForTabGroup()`, `this.#collectSplitViewDataForTabGroup()`, `this.#notifyOfSavedTabGroupsChange()`, `this.getSavedTabGroup()`
- 参照: `TabMetrics.METRIC_GROUP_TYPE.SAVED`, `TabMetrics.METRIC_SOURCE.UNKNOWN`, `TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `metricsContext?.telemetrySource`, `tab.documentGlobal`, `tabGroupState.splitViews`, `tabs.length`, `tabs[0].documentGlobal`, `win.gBrowser.tabContainer.verticalMode`

## _SessionStore.#recordSavedTabGroupState()
- 位置: L9013-9022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#notifyOfSavedTabGroupsChange()`, `this.#savedGroups.push()`, `this.getSavedTabGroup()`
- 参照: `savedTabGroupState.id`, `savedTabGroupState.tabs.length`

## _SessionStore.getSavedTabGroup()
- 位置: L9030-9034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#savedGroups.find()`
- 参照: `savedTabGroup.id`

## _SessionStore.getSavedTabGroups()
- 位置: L9041-9043
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`
- 参照: `this.#savedGroups`

## _SessionStore.#getClosedTabGroup()
- 位置: L9050-9055
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resolveClosedDataSource()`, `winData?.closedGroups.find()`
- 参照: `closedGroup.id`

## _SessionStore.undoCloseTabGroup()
- 位置: L9068-9117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `Glean.tabgroup.groupInteractions.open_recent.add()`, `Glean.tabgroup.reopen.record()`, `PrivateBrowsingUtils.isWindowPrivate()`, `group.select()`, `this.#createTabsForSavedOrClosedTabGroup()`, `this.#getClosedTabGroup()`, `this.#resolveClosedDataSource()`, `this.#windowIds.get()`, `this.forgetClosedTabGroup()`
- 条件付き依存: `if (targetWindow && !this.#windowIds.get(targetWindow))` → `Components.Exception()`
- 条件付き依存: `if (!targetWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if ( isPrivateSource !== PrivateBrowsingUtils.isWindowPrivate(targetWindow) )` → `Components.Exception()`
- 条件付き依存: `if (!tabGroupData)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `TabMetrics.METRIC_REOPEN_TYPE.DELETED`, `TabMetrics.METRIC_SOURCE.RECENT_TABS`, `TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `sourceWinData.isPrivate`, `sourceWinData.lastClosedTabGroupId`, `targetWindow.gBrowser.tabContainer.verticalMode`

## _SessionStore.openSavedTabGroup()
- 位置: L9134-9205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.reopen.record()`, `PrivateBrowsingUtils.isWindowPrivate()`, `group.select()`, `this.#createTabsForSavedOrClosedTabGroup()`, `this.#windowIds.get()`, `this.forgetSavedTabGroup()`, `this.getSavedTabGroup()`
- 条件付き依存: `if (!targetWindow)` → `this.#getTopWindow()`
- 条件付き依存: `if (!this.#windowIds.get(targetWindow))` → `Components.Exception()`
- 条件付き依存: `if (source == TabMetrics.METRIC_SOURCE.SUGGEST)` → `Glean.tabgroup.groupInteractions.open_suggest.add()`
- 条件付き依存: `if (source == TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU)` → `Glean.tabgroup.groupInteractions.open_tabmenu.add()`
- 条件付き依存: `if (source == TabMetrics.METRIC_SOURCE.RECENT_TABS)` → `Glean.tabgroup.groupInteractions.open_recent.add()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(targetWindow))` → `Components.Exception()`
- 条件付き依存: `if (!tabGroupData)` → `Components.Exception()`
- 条件付き依存: `if (tabGroupData.windowClosedId)` → `this.#getClosedWindowDataByClosedId()`
- 条件付き依存: `if (closedWinData)` → `this.#removeSavedTabGroupFromClosedWindow()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `TabMetrics.METRIC_REOPEN_TYPE.SAVED`, `TabMetrics.METRIC_SOURCE.RECENT_TABS`, `TabMetrics.METRIC_SOURCE.SUGGEST`, `TabMetrics.METRIC_SOURCE.TAB_OVERFLOW_MENU`, `TabMetrics.METRIC_SOURCE.UNKNOWN`, `TabMetrics.METRIC_TABS_LAYOUT.HORIZONTAL`, `TabMetrics.METRIC_TABS_LAYOUT.VERTICAL`, `tabGroupData.id`, `tabGroupData.windowClosedId`, `targetWindow.gBrowser.tabContainer.verticalMode`

## _SessionStore.#createTabsForSavedOrClosedTabGroup()
- 位置: L9212-9224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabGroupData.tabs.map()`, `targetWindow.gBrowser.createTabsForSessionRestore()`, `this.#restoreTabs()`
- 参照: `tab.state`, `tabGroupData.splitViews`, `tabs[0].group`

## _SessionStore.#cleanupOrphanedClosedGroups()
- 位置: L9241-9251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (winData.closedGroups[index].tabs.length === 0)` → `winData.closedGroups.splice()`
- 参照: `this.#closedObjectsChanged`, `winData.closedGroups`, `winData.closedGroups.length`, `winData.closedGroups[index].tabs.length`

## _SessionStore.#removeSavedTabGroupFromClosedWindow()
- 位置: L9258-9262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `removeWhere()`
- 参照: `closedWinData.groups`, `closedWinData.tabs`, `tab.groupId`, `tabGroup.id`, `this.#closedObjectsChanged`

## _SessionStore.isFormatVersionCompatible()
- 位置: L9271-9288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Number.isNaN()`, `Number.parseFloat()`

## _SessionStore.validateState()
- 位置: async L9298-9323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `fetch()`, `fetch( "moz-src:///browser/components/sessionstore/session.schema.json" ).then()`, `lazy.JsonSchema.validate()`, `rsp.json()`
- 条件付き依存: `if (!state)` → `this.getCurrentState()`
- 条件付き依存: `if (!result.valid)` → `console.warn()`
- 参照: `ex.message`, `result.errors`, `result.valid`, `state.deferredInitialState`, `state.lastSessionState`

## _SessionStore.historyIndex()
- 位置: L9333-9335
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabData.entries.length`, `tabData.index`

## restoreOnDemand()
- 位置: L9354-9365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateValue()`
- XPCOM: `Services.prefs`

## updateValue()
- 位置: L9355-9360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## restorePinnedTabsOnDemand()
- 位置: L9368-9379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateValue()`
- XPCOM: `Services.prefs`

## updateValue()
- 位置: L9369-9374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## restoreHiddenTabs()
- 位置: L9382-9393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `updateValue()`
- XPCOM: `Services.prefs`

## updateValue()
- 位置: L9383-9388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## reset()
- 位置: L9397-9399
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tabs`

## add()
- 位置: L9402-9412
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tab.pinned)` → `priority.push()`
- 条件付き依存: `if (tab.hidden)` → `hidden.push()`
- 条件付き依存: `if (!(tab.hidden))` → `visible.push()`
- 参照: `tab.hidden`, `tab.pinned`, `this.tabs`

## remove()
- 位置: L9415-9431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `set.indexOf()`
- 条件付き依存: `if (index == -1)` → `set.indexOf()`
- 条件付き依存: `if (index > -1)` → `set.splice()`
- 参照: `tab.hidden`, `this.tabs`

## shift()
- 位置: L9434-9451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `set.shift()`
- 参照: `hidden.length`, `priority.length`, `this.prefs`, `this.prefs.restoreHiddenTabs`, `this.tabs`, `visible.length`

## hiddenToVisible()
- 位置: L9454-9462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hidden.indexOf()`
- 条件付き依存: `if (index > -1)` → `hidden.splice()`
- 条件付き依存: `if (index > -1)` → `visible.push()`
- 参照: `this.tabs`

## visibleToHidden()
- 位置: L9465-9473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `visible.indexOf()`
- 条件付き依存: `if (index > -1)` → `visible.splice()`
- 条件付き依存: `if (index > -1)` → `hidden.push()`
- 参照: `this.tabs`

## willRestoreSoon()
- 位置: L9484-9506
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidateSet.indexOf()`
- 条件付き依存: `if (restorePinned && priority.length)` → `candidateSet.push()`
- 条件付き依存: `if (visible.length)` → `candidateSet.push()`
- 条件付き依存: `if (restoreHiddenTabs && hidden.length)` → `candidateSet.push()`
- 参照: `hidden.length`, `priority.length`, `this.prefs`, `this.tabs`, `visible.length`

## has()
- 位置: L9515-9517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.has()`

## get()
- 位置: L9519-9521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.get()`

## set()
- 位置: L9523-9525
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.set()`

## remove()
- 位置: L9527-9529
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.delete()`

## has()
- 位置: L9537-9539
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.has()`

## add()
- 位置: L9541-9543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.set()`

## remove()
- 位置: L9545-9547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._data.delete()`

## clear()
- 位置: L9549-9551
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._data`

## canRestore()
- 位置: L9561-9563
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## getState()
- 位置: L9565-9567
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## setState()
- 位置: L9569-9571
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._state`

## clear()
- 位置: L9573-9580
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!silent)` → `Services.obs.notifyObservers()`
- 参照: `this._state`
- XPCOM: `Services.obs`

## getBaseWindow()
- 位置: L9592-9594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.docShell.treeOwner.QueryInterface()`
- 参照: `Ci.nsIBaseWindow`
- XPCOM: `nsIBaseWindow`

## removeWhere()
- 位置: L9601-9607
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `predicate()`
- 条件付き依存: `if (predicate(array[i]))` → `array.splice()`
- 参照: `array.length`
