# browser/components/sessionstore/SessionWindowUI.sys.mjs

source: browser/components/sessionstore/SessionWindowUI.sys.mjs
source-hash: 2f5ca2664eadc8fd3a0dd28ad7934f67087f0c94
lines: 312

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `XPCOMUtils.declareLazy()`

## restoreLastClosedTabOrWindowOrSession()
- 位置: L26-56
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getClosedWindowCount()`
- 条件付き依存: `if (lazy.SessionStore.getClosedWindowCount() > (aIndex || 0))` → `lazy.SessionStore.undoCloseWindow()`

## maybeShowRestoreSessionInfoBar()
- 位置: async L168-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `icon.setAttribute()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `message.appendChild()`, `messageFragment.appendChild()`, `notifyBox.appendNotification()`, `win.document.createDocumentFragment()`, `win.document.createElement()`, `win.document.l10n.setAttributes()`, `win.gBrowser.getNotificationBox()`
- 条件付き依存: `if (count == 0)` → `Services.prefs.setIntPref()`
- 参照: `icon.className`, `icon.src`, `lazy.SessionStore.canRestoreLastSession`, `notification.timeout`, `notifyBox.PRIORITY_INFO_MEDIUM`
- XPCOM: `Services.prefs`

## callback()
- 位置: L220-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.PanelUI.selectAndMarkItem()`

## RestoreLastSessionObserver.constructor()
- 位置: L244-248
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._window.addEventListener()`
- 参照: `this._observersAdded`, `this._window`

## RestoreLastSessionObserver.init()
- 位置: L250-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( lazy.SessionStore.canRestoreLastSession && !lazy.PrivateBrowsingUtils.isWindowPrivate(this._window) )` → `Services.obs.addObserver()`
- 条件付き依存: `if ( lazy.SessionStore.canRestoreLastSession && !lazy.PrivateBrowsingUtils.isWindowPrivate(this._window) )` → `this._window.goSetCommandEnabled()`
- 条件付き依存: `if (lazy.SessionStore.willAutoRestore)` → `this._window.document.getElementById()`
- 参照: `lazy.SessionStore.canRestoreLastSession`, `lazy.SessionStore.willAutoRestore`, `this._observersAdded`, `this._window`, `this._window.document.getElementById( "Browser:RestoreLastSession" ).hidden`
- XPCOM: `Services.obs`

## RestoreLastSessionObserver.uninit()
- 位置: L270-284
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._observersAdded)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._window)` → `this._window.removeEventListener()`
- 参照: `this._observersAdded`, `this._window`
- XPCOM: `Services.obs`

## RestoreLastSessionObserver.handleEvent()
- 位置: L286-290
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "unload")` → `this.uninit()`
- 参照: `event.type`

## RestoreLastSessionObserver.observe()
- 位置: L292-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._window.goSetCommandEnabled()`
- 参照: `this._window`
