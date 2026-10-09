# browser/components/tabbrowser/AsyncTabSwitcher.sys.mjs

source: browser/components/tabbrowser/AsyncTabSwitcher.sys.mjs
source-hash: 294ee4fa7ca9575d18959bb006cf5ba7b9c97b2c
lines: 1499

## <module>
- 役割: 非同期タブ切り替えを行う AsyncTabSwitcher クラスを定義し、関連する pref を遅延取得で束ねるモジュール。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## AsyncTabSwitcher.constructor()
- 位置: L63-172
- 役割: 切り替え用の状態変数・タイマー・イベント監視を初期化し、現在のタブと印刷プレビューの状態を登録する。
- 触るとき: 切り替え器の初期状態や監視するイベントを変えるとき。
- 呼び出し先: `initialBrowser.preserveLayers()`, `this.log()`, `this.setTabState()`, `this.tabbrowser.getTabForBrowser()`, `this.window.addEventListener()`, `this.window.document.addEventListener()`
- 条件付き依存: `if (!this.windowHidden)` → `this.log()`
- 条件付き依存: `if (!this.windowHidden)` → `this.setTabState()`

## AsyncTabSwitcher.destroy()
- 位置: L174-193
- 役割: タイマーとイベントリスナーを解除し、tabbrowser から切り替え器への参照を外す。
- 触るとき: リスナーの付け外しやリークを調べるとき。
- 呼び出し先: `this.window.document.removeEventListener()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this.unloadTimer)` → `this.clearTimer()`
- 条件付き依存: `if (this.loadTimer)` → `this.clearTimer()`

## AsyncTabSwitcher.setTimer()
- 位置: L198-206
- 役割: nsITimer で一回限りのタイマーを作って返す。
- 触るとき: タイマーの実装や、setTimeout を使わない理由を確認するとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## AsyncTabSwitcher.clearTimer()
- 位置: L208-210
- 役割: 渡されたタイマーをキャンセルする。
- 触るとき: タイマーの取り消し方を調べるとき。
- 呼び出し先: `timer.cancel()`

## AsyncTabSwitcher.getTabState()
- 位置: L212-236
- 役割: タブの層(レイヤー)状態を返し、未登録なら browser の状態から求めて記録する。
- 触るとき: タブが LOADED かどうかの判定がおかしいとき。
- 呼び出し先: `this.tabState.get()`
- 条件付き依存: `if (state === undefined)` → `this.setTabStateNoAction()`

## AsyncTabSwitcher.setTabStateNoAction()
- 位置: L238-244
- 役割: 副作用なしで状態マップを更新する(UNLOADED は項目を削除)。
- 触るとき: 状態だけを書き換えたい処理を追うとき。
- 条件付き依存: `if (state == this.STATE_UNLOADED)` → `this.tabState.delete()`
- 条件付き依存: `if (!(state == this.STATE_UNLOADED))` → `this.tabState.set()`

## AsyncTabSwitcher.setTabState()
- 位置: L246-300
- 役割: タブの状態を変更し、遷移先に応じて docShell の有効化・無効化や renderLayers 設定を行う。
- 触るとき: タブの読み込み・解放の挙動や状態遷移を変えるとき。
- 呼び出し先: `this.getTabState()`, `this.setTabStateNoAction()`
- 条件付き依存: `if (state == this.STATE_LOADING)` → `this.assert()`
- 条件付き依存: `if (state == this.STATE_LOADING)` → `this.warmingTabs.has()`
- 条件付き依存: `if (browser.hasLayers)` → `this.onLayersReady()`
- 条件付き依存: `if (state == this.STATE_UNLOADING)` → `this.unwarmTab()`
- 条件付き依存: `if (!browser.hasLayers)` → `this.onLayersCleared()`
- 条件付き依存: `if (state == this.STATE_LOADED)` → `this.maybeActivateDocShell()`
- 条件付き依存: `if (!tab.linkedBrowser.isRemoteBrowser)` → `this.getTabState()`
- 条件付き依存: `if (!tab.linkedBrowser.isRemoteBrowser)` → `this.assert()`

## AsyncTabSwitcher.windowHidden()
- 位置: L302-304
- 役割: ウィンドウの document が非表示かどうかを返す getter。
- 触るとき: 最小化や隠れた状態の扱いを調べるとき。

## AsyncTabSwitcher.tabLayerCache()
- 位置: L306-308
- 役割: tabbrowser が持つタブのレイヤーキャッシュ配列を返す getter。
- 触るとき: キャッシュ配列の出どころを確認するとき。

## AsyncTabSwitcher.finish()
- 位置: L310-334
- 役割: 切り替え完了時に整合性を確認して destroy し、TabSwitchDone イベントを発火する。
- 触るとき: 切り替え器の終了条件や TabSwitchDone を調べるとき。
- 呼び出し先: `this.assert()`, `this.destroy()`, `this.getTabState()`, `this.log()`, `this.tabbrowser.dispatchEvent()`, `this.window.document.commandDispatcher.unlock()`

## AsyncTabSwitcher.updateDisplay()
- 位置: L338-479
- 役割: 表示するタブ、空白表示、スピナーを決め、パネルを切り替えてフォーカスを調整する。
- 触るとき: タブ切り替え時のスピナーや空白表示、フォーカスの挙動を変えるとき。
- 呼び出し先: `this.getTabState()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `this.requestedTab.hasAttribute()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `requestedBrowser.currentURI.schemeIs()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `this.logging()`
- 条件付き依存: `if (this.logging())` → `this.addLogFlag()`
- 条件付き依存: `if (requestedBrowser.isRemoteBrowser)` → `this.addLogFlag()`
- 条件付き依存: `if (!shouldBeBlank && this.blankTab)` → `this.blankTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (this.blankTab)` → `this.blankTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (shouldBeBlank && this.blankTab !== showTab)` → `this.blankTab.linkedBrowser.setAttribute()`
- 条件付き依存: `if (!needSpinner && this.spinnerTab)` → `this.noteSpinnerHidden()`
- 条件付き依存: `if (!needSpinner && this.spinnerTab)` → `this.tabbrowser.tabpanels.removeAttribute()`
- 条件付き依存: `if (!needSpinner && this.spinnerTab)` → `this.spinnerTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (this.spinnerTab)` → `this.spinnerTab.linkedBrowser.removeAttribute()`
- 条件付き依存: `if (!(this.spinnerTab))` → `this.noteSpinnerDisplayed()`
- 条件付き依存: `if (needSpinner && this.spinnerTab !== showTab)` → `this.tabbrowser.tabpanels.toggleAttribute()`
- 条件付き依存: `if (needSpinner && this.spinnerTab !== showTab)` → `this.spinnerTab.linkedBrowser.toggleAttribute()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `this.tabbrowser._adjustFocusBeforeTabSwitch()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `this.maybeVisibleTabs.add()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `this.tabbrowser.tabContainer.getRelatedElement()`
- 条件付き依存: `if (this.visibleTab !== showTab)` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if (index != -1)` → `this.log()`
- 条件付き依存: `if (index != -1)` → `this.tinfo()`
- 条件付き依存: `if (index != -1)` → `tabpanels.updateSelectedIndex()`
- 条件付き依存: `if (!(requestedTabState == this.STATE_LOADED))` → `this.noteMakingTabVisibleWithoutLayers()`
- 条件付き依存: `if (showTab === this.requestedTab)` → `this.tabbrowser._adjustFocusAfterTabSwitch()`
- 条件付き依存: `if (showTab === this.requestedTab)` → `this.window.gURLBar.afterTabSwitchFocusChange()`
- 条件付き依存: `if (showTab === this.requestedTab)` → `this.maybeActivateDocShell()`

## AsyncTabSwitcher.assert()
- 位置: L481-490
- 役割: 条件が偽ならスタックを出力し、DEBUG ビルドでは例外を投げる。
- 触るとき: 不変条件の検査失敗を調べるとき。
- 条件付き依存: `if (!cond)` → `dump()`
- 条件付き依存: `if (!cond)` → `Error()`

## AsyncTabSwitcher.maybeClearLoadTimer()
- 位置: L492-501
- 役割: 読み込み中のタブがあれば loadingTab を空にして読み込みタイマーを止める。
- 触るとき: 読み込みタイムアウトの解除理由(テレメトリ)を調べるとき。
- 条件付き依存: `if (this.loadTimer)` → `this.clearTimer()`

## AsyncTabSwitcher.loadRequestedTab()
- 位置: L504-518
- 役割: 要求されたタブを loadingTab にして読み込みタイマーを開始し、LOADING 状態にする。
- 触るとき: タブ読み込み開始の流れや切り替えのタイムアウト値を変えるとき。
- 呼び出し先: `this.assert()`, `this.handleEvent()`, `this.log()`, `this.setTabState()`, `this.setTimer()`, `this.tinfo()`

## AsyncTabSwitcher.maybeActivateDocShell()
- 位置: L520-545
- 役割: 要求タブが LOADED なのに docShell が非アクティブなら有効化する。
- 触るとき: 切り替え後に docShell が有効にならない問題を調べるとき。
- 呼び出し先: `this.getTabState()`
- 条件付き依存: `if ( tab == this.requestedTab && canCheckDocShellState && state == this.STATE_LOADED && !browser.docShellIsActive && !this.windowHidden )` → `this.logState()`
- 条件付き依存: `if ( tab == this.requestedTab && canCheckDocShellState && state == this.STATE_LOADED && !browser.docShellIsActive && !this.windowHidden )` → `browser.preserveLayers()`

## AsyncTabSwitcher.preActions()
- 位置: L549-585
- 役割: 各イベント処理の前に、閉じられたタブを各状態・キャッシュから取り除く。
- 触るとき: 閉じたタブへの参照が残る問題を調べるとき。
- 呼び出し先: `this.assert()`
- 条件付き依存: `if (!tab.linkedBrowser)` → `this.tabState.delete()`
- 条件付き依存: `if (!tab.linkedBrowser)` → `this.tabLayerCache.splice()`
- 条件付き依存: `if (!tab.linkedBrowser)` → `this.unwarmTab()`
- 条件付き依存: `if (this.spinnerTab && !this.spinnerTab.linkedBrowser)` → `this.noteSpinnerHidden()`
- 条件付き依存: `if (this.loadingTab && !this.loadingTab.linkedBrowser)` → `this.maybeClearLoadTimer()`

## AsyncTabSwitcher.postActions()
- 位置: L591-696
- 役割: イベント処理後に不変条件を確認し、要求タブの読み込み、表示更新、不要タブの解放、終了判定を行う。
- 触るとき: 切り替え状態機械の全体の流れや終了条件を変えるとき。
- 呼び出し先: `this.assert()`, `this.getTabState()`, `this.logState()`, `this.maybeFinishTabSwitch()`, `this.shouldDeactivateDocShell()`, `this.tabLayerCache.includes()`, `this.updateDisplay()`, `this.warmingTabs.has()`
- 条件付き依存: `if (!this.requestedTab.linkedBrowser.isRemoteBrowser)` → `this.maybeClearLoadTimer()`
- 条件付き依存: `if ( !this.loadTimer && !this.windowHidden && (stateOfRequestedTab == this.STATE_UNLOADED || stateOfRequestedTab == this.STATE_UNLOADING || this.warmingTabs.has(...)` → `this.assert()`
- 条件付き依存: `if ( !this.loadTimer && !this.windowHidden && (stateOfRequestedTab == this.STATE_UNLOADED || stateOfRequestedTab == this.STATE_UNLOADING || this.warmingTabs.has(...)` → `this.loadRequestedTab()`
- 条件付き依存: `if (numBackgroundCached > 0)` → `this.deactivateCachedBackgroundTabs()`
- 条件付き依存: `if (numWarming > lazy.gTabWarmingMax)` → `this.logState()`
- 条件付き依存: `if (this.unloadTimer)` → `this.clearTimer()`
- 条件付き依存: `if (numWarming > lazy.gTabWarmingMax)` → `this.unloadNonRequiredTabs()`
- 条件付き依存: `if (numPending == 0)` → `this.finish()`

## AsyncTabSwitcher.onUnloadTimeout()
- 位置: L699-702
- 役割: 解放タイマー満了時にタイマーを空にして不要タブの解放を行う。
- 触るとき: 解放の遅延動作を調べるとき。
- 呼び出し先: `this.unloadNonRequiredTabs()`

## AsyncTabSwitcher.deactivateCachedBackgroundTabs()
- 位置: L704-712
- 役割: レイヤーキャッシュ内の要求タブ以外について、レイヤーを保持したまま docShell を非アクティブにする。
- 触るとき: タブキャッシュの背景タブの扱いを変えるとき。
- 条件付き依存: `if (tab !== this.requestedTab)` → `browser.preserveLayers()`

## AsyncTabSwitcher.unloadNonRequiredTabs()
- 位置: L718-757
- 役割: 表示中・要求中・キャッシュ外の LOADED タブを UNLOADING にし、残りがあれば解放タイマーを再設定する。
- 触るとき: どのタブのレイヤーを解放するかの条件を変えるとき。
- 呼び出し先: `this.maybeVisibleTabs.has()`, `this.shouldDeactivateDocShell()`, `this.tabLayerCache.includes()`
- 条件付き依存: `if ( state == this.STATE_LOADED && !this.maybeVisibleTabs.has(tab) && tab !== this.lastVisibleTab && tab !== this.loadingTab && tab !== this.requestedTab && !isI...)` → `this.setTabState()`
- 条件付き依存: `if (numPending)` → `this.setTimer()`
- 条件付き依存: `if (numPending)` → `this.handleEvent()`

## AsyncTabSwitcher.onLoadTimeout()
- 位置: L760-762
- 役割: 読み込みタイムアウト時に読み込みタイマーを解除する。
- 触るとき: スピナー表示のきっかけとなるタイムアウトを調べるとき。
- 呼び出し先: `this.maybeClearLoadTimer()`

## AsyncTabSwitcher.onLayersReady()
- 位置: L765-785
- 役割: タブのレイヤー準備完了を受けて LOADED にし、読み込み中のタブならタイマーを解除する。
- 触るとき: MozLayerTreeReady 後の処理を調べるとき。
- 呼び出し先: `this.assert()`, `this.getTabState()`, `this.logState()`, `this.setTabState()`, `this.tabbrowser.getTabForBrowser()`, `this.unwarmTab()`
- 条件付き依存: `if (this.loadingTab === tab)` → `this.maybeClearLoadTimer()`

## AsyncTabSwitcher.onPaint()
- 位置: L790-798
- 役割: 描画完了で切り替えのテレメトリを記録し、表示候補タブの集合を空にする。
- 触るとき: MozAfterPaint 後の旧タブ解放の判断を調べるとき。
- 呼び出し先: `this.addLogFlag()`, `this.maybeVisibleTabs.clear()`, `this.notePaint()`

## AsyncTabSwitcher.onLayersCleared()
- 位置: L801-812
- 役割: レイヤー解放の完了を受けてタブを UNLOADED にする。
- 触るとき: MozLayerTreeCleared 後の処理を調べるとき。
- 呼び出し先: `this.assert()`, `this.getTabState()`, `this.logState()`, `this.setTabState()`, `this.tabbrowser.getTabForBrowser()`

## AsyncTabSwitcher.onRemotenessChange()
- 位置: L817-833
- 役割: リモート/非リモート切り替え時に、来ないレイヤー通知を代わりに処理し状態を整える。
- 触るとき: プロセス種別の変更中のタブ切り替え不具合を調べるとき。
- 呼び出し先: `this.logState()`
- 条件付き依存: `if (!tab.linkedBrowser.isRemoteBrowser)` → `this.getTabState()`
- 条件付き依存: `if (this.getTabState(tab) == this.STATE_LOADING)` → `this.onLayersReady()`
- 条件付き依存: `if (!(this.getTabState(tab) == this.STATE_LOADING))` → `this.getTabState()`
- 条件付き依存: `if (this.getTabState(tab) == this.STATE_UNLOADING)` → `this.onLayersCleared()`
- 条件付き依存: `if (!(!tab.linkedBrowser.isRemoteBrowser))` → `this.getTabState()`
- 条件付き依存: `if (this.getTabState(tab) == this.STATE_LOADED)` → `this.setTabState()`

## AsyncTabSwitcher.onTabRemoved()
- 位置: L835-839
- 役割: 最後に表示したタブが閉じられたとき tabRemoved イベントを処理に回す。
- 触るとき: タブを閉じた直後の切り替え動作を調べるとき。
- 条件付き依存: `if (this.lastVisibleTab == tab)` → `this.handleEvent()`

## AsyncTabSwitcher.onTabRemovedImpl()
- 位置: L843-845
- 役割: lastVisibleTab を空にする。
- 触るとき: 閉じたタブの表示状態の後始末を調べるとき。

## AsyncTabSwitcher.onTabDiscarded()
- 位置: L847-849
- 役割: タブ破棄を tabDiscarded イベントとして処理に回す。
- 触るとき: タブ破棄と切り替え器の連携を調べるとき。
- 呼び出し先: `this.handleEvent()`

## AsyncTabSwitcher.onTabDiscardedImpl()
- 位置: L854-868
- 役割: 破棄されたタブを読み込み中・キャッシュ・状態マップ・lastVisibleTab から外す。
- 触るとき: 破棄タブに状態が残る問題を調べるとき。
- 呼び出し先: `this.logState()`, `this.setTabStateNoAction()`, `this.tabLayerCache.indexOf()`, `this.unwarmTab()`
- 条件付き依存: `if (this.loadingTab === tab)` → `this.maybeClearLoadTimer()`
- 条件付き依存: `if (cacheIndex != -1)` → `this.tabLayerCache.splice()`

## AsyncTabSwitcher.onVisibilityChange()
- 位置: L870-887
- 役割: ウィンドウが隠れたら各タブを解放し、再表示されたら選択タブの docShell を有効化する。
- 触るとき: 最小化や遮蔽時のレイヤー解放を調べるとき。
- 条件付き依存: `if (this.windowHidden)` → `this.shouldDeactivateDocShell()`
- 条件付き依存: `if (state == this.STATE_LOADING || state == this.STATE_LOADED)` → `this.setTabState()`
- 条件付き依存: `if (this.windowHidden)` → `this.maybeClearLoadTimer()`
- 条件付き依存: `if (!(this.windowHidden))` → `this.maybeActivateDocShell()`

## AsyncTabSwitcher.onSwapDocShells()
- 位置: L889-911
- 役割: docShell 交換前に相手 browser の状態を swapMap に保存する。
- 触るとき: ウィンドウ間のタブ移動時の状態引き継ぎを調べるとき。
- 呼び出し先: `this.swapMap.set()`
- 条件付き依存: `if (otherTabbrowser && otherTabbrowser._switcher)` → `otherTabbrowser.getTabForBrowser()`
- 条件付き依存: `if (otherTabbrowser && otherTabbrowser._switcher)` → `otherSwitcher.getTabState()`

## AsyncTabSwitcher.onEndSwapDocShells()
- 位置: L913-933
- 役割: 交換後に読み込みタイマーを解除し、保存した相手の状態を自タブに設定する。
- 触るとき: タブ移動後の表示不具合を調べるとき。
- 呼び出し先: `this.maybeClearLoadTimer()`, `this.swapMap.delete()`, `this.swapMap.get()`, `this.tabbrowser.getTabForBrowser()`
- 条件付き依存: `if (ourTab)` → `this.setTabStateNoAction()`

## AsyncTabSwitcher.shouldDeactivateDocShell()
- 位置: L942-948
- 役割: 印刷プレビュー、分割ビュー、PiP 元の browser は無効化しないと判定する。
- 触るとき: 背景でも描画を続けるべき browser の条件を追加するとき。
- 呼び出し先: `lazy.PictureInPicture.isOriginatingBrowser()`, `this.tabbrowser._printPreviewBrowsers.has()`, `this.tabbrowser.splitViewBrowsers.includes()`

## AsyncTabSwitcher.shouldActivateDocShell()
- 位置: L950-954
- 役割: タブが LOADING か LOADED なら docShell を有効にすべきと返す。
- 触るとき: docShell を有効にする判定の呼び出し元を調べるとき。
- 呼び出し先: `this.getTabState()`, `this.tabbrowser.getTabForBrowser()`

## AsyncTabSwitcher.activateBrowserForPrintPreview()
- 位置: L956-965
- 役割: 印刷プレビューの browser が未ロードなら LOADING 状態にして有効化する。
- 触るとき: 印刷プレビュー表示時の描画問題を調べるとき。
- 呼び出し先: `this.getTabState()`, `this.tabbrowser.getTabForBrowser()`
- 条件付き依存: `if (state != this.STATE_LOADING && state != this.STATE_LOADED)` → `this.setTabState()`
- 条件付き依存: `if (state != this.STATE_LOADING && state != this.STATE_LOADED)` → `this.logState()`
- 条件付き依存: `if (state != this.STATE_LOADING && state != this.STATE_LOADED)` → `this.tinfo()`

## AsyncTabSwitcher.canWarmTab()
- 位置: L967-990
- 役割: ウォームアップ可能か(pref 有効、ウィンドウ表示中、リモートで生きているタブか)を判定する。
- 触るとき: タブウォームアップの対象条件を変えるとき。

## AsyncTabSwitcher.shouldWarmTab()
- 位置: L992-1003
- 役割: ウォームアップ可能で、かつ UNLOADED か UNLOADING のタブなら真を返す。
- 触るとき: ウォームアップを行うかの判断を調べるとき。
- 呼び出し先: `this.canWarmTab()`
- 条件付き依存: `if (this.canWarmTab(tab))` → `this.getTabState()`

## AsyncTabSwitcher.unwarmTab()
- 位置: L1005-1007
- 役割: タブをウォームアップ中の集合から外す。
- 触るとき: ウォームアップ状態の解除タイミングを調べるとき。
- 呼び出し先: `this.warmingTabs.delete()`

## AsyncTabSwitcher.warmupTab()
- 位置: L1009-1019
- 役割: タブをウォームアップ対象に加えて LOADING にし、解放を予約する。
- 触るとき: ホバー等によるタブの事前読み込みを調べるとき。
- 呼び出し先: `this.logState()`, `this.queueUnload()`, `this.setTabState()`, `this.shouldWarmTab()`, `this.tinfo()`, `this.warmingTabs.add()`

## AsyncTabSwitcher.cleanUpTabAfterEviction()
- 位置: L1021-1028
- 役割: キャッシュから追い出したタブのレイヤー保持を解除し UNLOADING にする。
- 触るとき: キャッシュ追い出し後の後始末を調べるとき。
- 呼び出し先: `this.assert()`, `this.setTabState()`
- 条件付き依存: `if (browser)` → `browser.preserveLayers()`

## AsyncTabSwitcher.evictOldestTabFromCache()
- 位置: L1030-1033
- 役割: レイヤーキャッシュの最古のタブを取り出して後始末する。
- 触るとき: キャッシュの追い出し順を変えるとき。
- 呼び出し先: `this.cleanUpTabAfterEviction()`, `this.tabLayerCache.shift()`

## AsyncTabSwitcher.maybePromoteTabInLayerCache()
- 位置: L1035-1053
- 役割: リモートタブをキャッシュの末尾へ移し、上限超過なら最古を追い出す。
- 触るとき: タブキャッシュ(tabCacheSize)の挙動を変えるとき。
- 条件付き依存: `if ( lazy.gTabCacheSize > 1 && tab.linkedBrowser.isRemoteBrowser && tab.linkedBrowser.currentURI.spec != "about:blank" )` → `this.tabLayerCache.indexOf()`
- 条件付き依存: `if (tabIndex != -1)` → `this.tabLayerCache.splice()`
- 条件付き依存: `if ( lazy.gTabCacheSize > 1 && tab.linkedBrowser.isRemoteBrowser && tab.linkedBrowser.currentURI.spec != "about:blank" )` → `this.tabLayerCache.push()`
- 条件付き依存: `if (this.tabLayerCache.length > lazy.gTabCacheSize)` → `this.evictOldestTabFromCache()`

## AsyncTabSwitcher.requestTab()
- 位置: L1056-1089
- 役割: ユーザーが選んだタブを要求タブにし、優先度と primary 属性を更新して解放を予約する。
- 触るとき: タブ切り替えの入口で何が起きるかを調べるとき。
- 呼び出し先: `oldBrowser.deprioritize()`, `tab.linkedBrowser.setAttribute()`, `this.getTabState()`, `this.logState()`, `this.queueUnload()`, `this.startTabSwitch()`, `this.tinfo()`
- 条件付き依存: `if (tabState == this.STATE_LOADED)` → `this.maybeVisibleTabs.clear()`
- 条件付き依存: `if (this.lastPrimaryTab && this.lastPrimaryTab != tab)` → `this.lastPrimaryTab.linkedBrowser.removeAttribute()`

## AsyncTabSwitcher.queueUnload()
- 位置: L1091-1093
- 役割: queueUnload イベントとして解放タイマー設定を処理に回す。
- 触るとき: 解放予約の呼び出し経路を調べるとき。
- 呼び出し先: `this.handleEvent()`

## AsyncTabSwitcher.onQueueUnload()
- 位置: L1095-1103
- 役割: 既存の解放タイマーを止めて、指定時間の新しいタイマーを設定する。
- 触るとき: 解放の遅延時間の扱いを調べるとき。
- 呼び出し先: `this.handleEvent()`, `this.setTimer()`
- 条件付き依存: `if (this.unloadTimer)` → `this.clearTimer()`

## AsyncTabSwitcher.handleEvent()
- 位置: L1105-1178
- 役割: 再入を避けつつ前処理、イベント種別ごとの処理、後処理の順で実行する。
- 触るとき: 切り替え器が受けるイベントを追加・調査するとき。
- 呼び出し先: `this.onEndSwapDocShells()`, `this.onLayersCleared()`, `this.onLayersReady()`, `this.onLoadTimeout()`, `this.onPaint()`, `this.onQueueUnload()`, `this.onRemotenessChange()`, `this.onSwapDocShells()`, `this.onTabDiscardedImpl()`, `this.onTabRemovedImpl()`, `this.onUnloadTimeout()`, `this.onVisibilityChange()`, `this.postActions()`, `this.preActions()`
- 条件付き依存: `if (this._processing)` → `this.setTimer()`
- 条件付き依存: `if (this._processing)` → `this.handleEvent()`

## AsyncTabSwitcher.startTabSwitch()
- 位置: L1185-1188
- 役割: 切り替え計測を開始し、switchInProgress を立てる。
- 触るとき: 切り替え計測の開始時点を調べるとき。
- 呼び出し先: `this.noteStartTabSwitch()`

## AsyncTabSwitcher.maybeFinishTabSwitch()
- 位置: L1196-1218
- 役割: 要求タブが LOADED か空白表示なら切り替え完了として計測を終え、TabSwitched を発火する。
- 触るとき: TabSwitched イベントや完了判定を調べるとき。
- 呼び出し先: `this.getTabState()`
- 条件付き依存: `if (this.requestedTab !== this.blankTab)` → `this.maybePromoteTabInLayerCache()`
- 条件付き依存: `if ( this.switchInProgress && this.requestedTab && (this.getTabState(this.requestedTab) == this.STATE_LOADED || this.requestedTab === this.blankTab) )` → `this.noteFinishTabSwitch()`
- 条件付き依存: `if ( this.switchInProgress && this.requestedTab && (this.getTabState(this.requestedTab) == this.STATE_LOADED || this.requestedTab === this.blankTab) )` → `this.tabbrowser.dispatchEvent()`

## AsyncTabSwitcher.logging()
- 位置: L1223-1237
- 役割: ログ出力が有効かを、pref を一度読んだ結果とともに返す。
- 触るとき: 切り替えログを有効にする方法を確認するとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## AsyncTabSwitcher.tinfo()
- 位置: L1239-1244
- 役割: タブの index と URL をログ用の文字列にする。
- 触るとき: ログ表示の書式を変えるとき。

## AsyncTabSwitcher.log()
- 位置: L1246-1255
- 役割: ログが有効なとき dump またはコンソールに文字列を出す。
- 触るとき: ログの出力先を確認するとき。
- 呼び出し先: `this.logging()`
- 条件付き依存: `if (this._useDumpForLogging)` → `dump()`
- 条件付き依存: `if (!(this._useDumpForLogging))` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## AsyncTabSwitcher.addLogFlag()
- 位置: L1257-1264
- 役割: ログ有効時に、サブフラグを 0/1 で添えたフラグを蓄積する。
- 触るとき: ログに付くフラグの意味を調べるとき。
- 呼び出し先: `this.logging()`
- 条件付き依存: `if (subFlags.length)` → `subFlags.map(f => (f ? 1 : 0)).join()`
- 条件付き依存: `if (subFlags.length)` → `subFlags.map()`
- 条件付き依存: `if (this.logging())` → `this._logFlags.push()`

## AsyncTabSwitcher.logState()
- 位置: L1266-1407
- 役割: 全タブの状態を圧縮した文字列にして、変化があればログに出す。
- 触るとき: ATS ログの読み方を調べるとき。
- 呼び出し先: `getTabString()`, `this.logging()`, `this.tabbrowser.tabs.map()`
- 条件付き依存: `if (lastMatch == i - 1)` → `unloadedTabsStrings.push()`
- 条件付き依存: `if (lastMatch == i - 1)` → `lastMatch.toString()`
- 条件付き依存: `if (!(lastMatch == i - 1))` → `unloadedTabsStrings.push()`
- 条件付き依存: `if (unloadedTabsStrings.length)` → `unloadedTabsStrings.join()`
- 条件付き依存: `if (this._logFlags.length)` → `this._logFlags.join()`
- 条件付き依存: `if (this._useDumpForLogging)` → `dump()`
- 条件付き依存: `if (!(this._useDumpForLogging))` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## getTabString()
- 位置: L1271-1344
- 役割: タブ一つの役割(V/L/R 等)と状態をログ用の文字列に変換する。
- 触るとき: ログ内の記号の意味を変える・調べるとき。
- 呼び出し先: `lazy.PictureInPicture.isOriginatingBrowser()`, `this.getTabState()`, `this.maybeVisibleTabs.has()`, `this.tabLayerCache.includes()`, `this.warmingTabs.has()`

## AsyncTabSwitcher.noteMakingTabVisibleWithoutLayers()
- 位置: L1409-1418
- 役割: レイヤー未準備のままタブを表示する場合に、合成時間の計測を取り消す。
- 触るとき: tabSwitchComposite 計測の欠落を調べるとき。
- 呼び出し先: `Glean.performanceInteraction.tabSwitchComposite.cancel()`

## AsyncTabSwitcher.notePaint()
- 位置: L1420-1434
- 役割: 切り替え後の描画が来たら合成時間の計測を止め、プロファイラ印を付ける。
- 触るとき: tabSwitchComposite の測定終点を調べるとき。
- 条件付き依存: `if (this._tabswitchCompositeTimerId)` → `Glean.performanceInteraction.tabSwitchComposite.stopAndAccumulate()`
- 条件付き依存: `if (this.switchPaintId != -1 && event.transactionId >= this.switchPaintId)` → `ChromeUtils.addProfilerMarker()`

## AsyncTabSwitcher.noteStartTabSwitch()
- 位置: L1436-1451
- 役割: 切り替え全体と合成時間のタイマーを開始し、プロファイラ印を付ける。
- 触るとき: タブ切り替えテレメトリの開始点を調べるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.browserTabswitch.total.start()`, `Glean.performanceInteraction.tabSwitchComposite.start()`
- 条件付き依存: `if (this._tabswitchTotalTimerId)` → `Glean.browserTabswitch.total.cancel()`
- 条件付き依存: `if (this._tabswitchCompositeTimerId)` → `Glean.performanceInteraction.tabSwitchComposite.cancel()`

## AsyncTabSwitcher.noteFinishTabSwitch()
- 位置: L1453-1464
- 役割: 切り替え全体のタイマーを止めて蓄積し、プロファイラ印を付ける。
- 触るとき: browser.tabswitch.total の終点を調べるとき。
- 条件付き依存: `if (this._tabswitchTotalTimerId)` → `Glean.browserTabswitch.total.stopAndAccumulate()`
- 条件付き依存: `if (this._tabswitchTotalTimerId)` → `ChromeUtils.addProfilerMarker()`

## AsyncTabSwitcher.noteSpinnerDisplayed()
- 位置: L1466-1482
- 役割: スピナー表示の計測を開始し、きっかけを記録して Nightly では通知する。
- 触るとき: スピナーのテレメトリを調べるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.browserTabswitch.spinnerVisible.start()`, `Glean.browserTabswitch.spinnerVisibleTrigger[this._loadTimerClearedBy].add()`, `this.assert()`
- 条件付き依存: `if (AppConstants.NIGHTLY_BUILD)` → `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## AsyncTabSwitcher.noteSpinnerHidden()
- 位置: L1484-1497
- 役割: スピナー表示の計測を止め、タイマー解除理由を初期化する。
- 触るとき: スピナー表示時間の測定終点を調べるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `Glean.browserTabswitch.spinnerVisible.stopAndAccumulate()`, `this.assert()`, `this.log()`
