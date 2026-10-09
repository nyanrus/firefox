# browser/components/sessionstore/SessionWindowUI.sys.mjs

source: browser/components/sessionstore/SessionWindowUI.sys.mjs
source-hash: 2f5ca2664eadc8fd3a0dd28ad7934f67087f0c94
lines: 312

## <module>
- 役割: 閉じたタブ・ウィンドウ・セッションの復元操作と、復元用のメニュー状態やインフォバーを扱うウィンドウ UI 層。
- 呼び出し先: `ChromeUtils.generateQI()`, `XPCOMUtils.declareLazy()`

## restoreLastClosedTabOrWindowOrSession()
- 位置: L26-56
- 役割: 直前に閉じた操作（タブかウィンドウ）を取り消し、なければ最後のセッションを復元する。
- 触るとき: Ctrl+Shift+T の挙動が閉じたタブ・ウィンドウ・セッションのどれに着地するかを変えるとき。
- 呼び出し先: `lazy.SessionStore.popLastClosedAction()`
- 条件付き依存: `if (lastActionTaken)` → `lazy.SessionStore.getWindowForTabClosedId()`
- 条件付き依存: `if (lastActionTaken)` → `this.undoCloseTab()`
- 条件付き依存: `if (lastActionTaken)` → `lazy.SessionStore.getWindowId()`
- 条件付き依存: `if (lastActionTaken)` → `this.undoCloseWindow()`
- 条件付き依存: `if (!(lastActionTaken))` → `lazy.SessionStore.getLastClosedTabCount()`
- 条件付き依存: `if (lazy.SessionStore.canRestoreLastSession)` → `lazy.SessionStore.restoreLastSession()`
- 条件付き依存: `if (closedTabCount)` → `this.undoCloseTab()`
- 参照: `lastActionTaken.closedId`, `lastActionTaken.type`, `lazy.SessionStore.LAST_ACTION_CLOSED_TAB`, `lazy.SessionStore.LAST_ACTION_CLOSED_WINDOW`, `lazy.SessionStore.canRestoreLastSession`

## undoCloseTab()
- 位置: L72-147
- 役割: 閉じたタブを対象ウィンドウに戻す。閉じたタブグループがあればグループごと開き、空の初期タブは取り除く。
- 触るとき: 閉じたタブの復元先が元のウィンドウにならない、または空タブが残る不具合を調べるとき。
- 呼び出し先: `lazy.SessionStore.getLastClosedTabGroupId()`
- 条件付き依存: `if (sourceWindowSSId)` → `lazy.SessionStore.getWindowById()`
- 条件付き依存: `if (aIndex === undefined && lastClosedTabGroupId)` → `lazy.SessionStore.getSavedTabGroup()`
- 条件付き依存: `if (lazy.SessionStore.getSavedTabGroup(lastClosedTabGroupId))` → `lazy.SessionStore.openSavedTabGroup()`
- 条件付き依存: `if (!(lazy.SessionStore.getSavedTabGroup(lastClosedTabGroupId)))` → `lazy.SessionStore.undoCloseTabGroup()`
- 条件付き依存: `if (aIndex === undefined && lastClosedTabGroupId)` → `group.tabs.at()`
- 条件付き依存: `if (!(aIndex === undefined && lastClosedTabGroupId))` → `lazy.SessionStore.getLastClosedTabCount()`
- 条件付き依存: `if (!(aIndex === undefined && lastClosedTabGroupId))` → `new Array(lastClosedTabCount).fill()`
- 条件付き依存: `if (!(aIndex === undefined && lastClosedTabGroupId))` → `lazy.SessionStore.getClosedTabCountForWindow()`
- 条件付き依存: `if ( lazy.SessionStore.getClosedTabCountForWindow(sourceWindow) > index )` → `lazy.SessionStore.undoCloseTab()`
- 条件付き依存: `if (tabsRemoved && blankTabToRemove)` → `targetWindow.gBrowser.removeTab()`
- 参照: `lazy.TabMetrics.METRIC_SOURCE.RECENT_TABS`, `targetWindow.gBrowser.selectedTab`, `targetWindow.gBrowser.selectedTab.isEmpty`, `targetWindow.gBrowser.visibleTabs.length`

## undoCloseWindow()
- 位置: L156-163
- 役割: 閉じたウィンドウを SessionStore から復元し、復元されたウィンドウを返す。
- 触るとき: 閉じたウィンドウの取り消し件数やインデックスの扱いを変えるとき。
- 呼び出し先: `lazy.SessionStore.getClosedWindowCount()`
- 条件付き依存: `if (lazy.SessionStore.getClosedWindowCount() > (aIndex || 0))` → `lazy.SessionStore.undoCloseWindow()`

## maybeShowRestoreSessionInfoBar()
- 位置: async L168-240
- 役割: 再起動 2 回目までの間に、復元可能なセッションがあれば「セッションを復元」の通知バーを出す。
- 触るとき: 通知バーが出る条件（回数、プライベートウィンドウ、復元可否）を調整するとき。
- 呼び出し先: `Date.now()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `icon.setAttribute()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `message.appendChild()`, `messageFragment.appendChild()`, `notifyBox.appendNotification()`, `win.document.createDocumentFragment()`, `win.document.createElement()`, `win.document.l10n.setAttributes()`, `win.gBrowser.getNotificationBox()`
- 条件付き依存: `if (count == 0)` → `Services.prefs.setIntPref()`
- 参照: `icon.className`, `icon.src`, `lazy.SessionStore.canRestoreLastSession`, `notification.timeout`, `notifyBox.PRIORITY_INFO_MEDIUM`
- XPCOM: `Services.prefs`

## callback()
- 位置: L220-225
- 役割: 通知バーのボタン押下時に、アプリメニューの履歴から「セッションを復元」を選択状態にする。
- 触るとき: 通知バーのボタンから開くメニュー項目を変えるとき。
- 呼び出し先: `win.PanelUI.selectAndMarkItem()`

## RestoreLastSessionObserver.constructor()
- 位置: L244-248
- 役割: ウィンドウの unload を監視対象に登録し、オブザーバー登録フラグを初期化する。
- 触るとき: ウィンドウごとの復元コマンドの後始末を追うとき。
- 呼び出し先: `this._window.addEventListener()`
- 参照: `this._observersAdded`, `this._window`

## RestoreLastSessionObserver.init()
- 位置: L250-268
- 役割: 復元可能かつ非プライベートなら復元コマンドを有効化してオブザーバーを張る。自動復元のみの場合はメニュー項目を隠す。
- 触るとき: 「前回のセッションを復元」メニューが有効にならない、または隠れる原因を調べるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( lazy.SessionStore.canRestoreLastSession && !lazy.PrivateBrowsingUtils.isWindowPrivate(this._window) )` → `Services.obs.addObserver()`
- 条件付き依存: `if ( lazy.SessionStore.canRestoreLastSession && !lazy.PrivateBrowsingUtils.isWindowPrivate(this._window) )` → `this._window.goSetCommandEnabled()`
- 条件付き依存: `if (lazy.SessionStore.willAutoRestore)` → `this._window.document.getElementById()`
- 参照: `lazy.SessionStore.canRestoreLastSession`, `lazy.SessionStore.willAutoRestore`, `this._observersAdded`, `this._window`, `this._window.document.getElementById( "Browser:RestoreLastSession" ).hidden`
- XPCOM: `Services.obs`

## RestoreLastSessionObserver.uninit()
- 位置: L270-284
- 役割: 張っていたオブザーバーを外し、ウィンドウの参照と unload の監視を解除する。
- 触るとき: ウィンドウを閉じた後にオブザーバーが残るリークを確かめるとき。
- 条件付き依存: `if (this._observersAdded)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._window)` → `this._window.removeEventListener()`
- 参照: `this._observersAdded`, `this._window`
- XPCOM: `Services.obs`

## RestoreLastSessionObserver.handleEvent()
- 位置: L286-290
- 役割: unload イベントを受けて uninit を呼ぶ。
- 触るとき: ウィンドウ破棄時の解除経路を変えるとき。
- 条件付き依存: `if (event.type === "unload")` → `this.uninit()`
- 参照: `event.type`

## RestoreLastSessionObserver.observe()
- 位置: L292-305
- 役割: 最後のセッションのクリアと再有効化の通知を受け、復元コマンドの有効・無効を切り替える。
- 触るとき: セッションの削除・再有効化後にメニューの状態がずれるとき。
- 呼び出し先: `this._window.goSetCommandEnabled()`
- 参照: `this._window`
