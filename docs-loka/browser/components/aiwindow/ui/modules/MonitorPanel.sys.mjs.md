# browser/components/aiwindow/ui/modules/MonitorPanel.sys.mjs

source: browser/components/aiwindow/ui/modules/MonitorPanel.sys.mjs
source-hash: 8794ae8ba62364f658ecb57cab2c7a263804e8d4
lines: 435

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## toggleMonitorPanel()
- 位置: L54-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `this.showMonitorPanel()`
- 条件付き依存: `if (existing)` → `existing.hidePopup()`
- 参照: `win?.document`

## showCreateForm()
- 位置: L74-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `this.showMonitorPanel()`
- 条件付き依存: `if (existing)` → `this._openCreateView()`
- 参照: `win?.document`

## showMonitorPanel()
- 位置: L94-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `button.setAttribute()`, `doc.getElementById()`, `lazy.AIWindow.takeMonitorAttentionIds()`, `lazy.CustomizableUI.getWidget()`, `lazy.CustomizableUI.getWidget(BUTTON_ID)?.forWindow()`, `panel.addEventListener()`, `panel.openPopup()`, `panel.remove()`, `popupSet.appendChild()`, `this._createPanel()`, `this._syncContents()`
- 条件付き依存: `if (create)` → `this._openCreateView()`
- 参照: `lazy.CustomizableUI.getWidget(BUTTON_ID)?.forWindow(win)?.anchor`, `lazy.MONITOR_AGENTS_CHANGED_TOPIC`, `panel._contents.attentionIds`, `win.document`
- XPCOM: `Services.obs`

## onMonitorsChanged()
- 位置: L114-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._syncContents()`

## _createPanel()
- 位置: L152-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contents.addEventListener()`, `doc.createElement()`, `doc.createXULElement()`, `header.appendChild()`, `heading.appendChild()`, `panel.append()`, `panel.hidePopup()`, `panel.setAttribute()`, `this._onCreateSubmit()`, `this._onOpenTask()`, `this._openCreateView()`, `this._setView()`, `win.switchToTabHavingURI()`
- 参照: `contents.draft`, `contents.maxMonitors`, `event.detail`, `event.detail.draft`, `event.detail.id`, `header.className`, `heading.id`, `lazy.TOTAL_NUM_MONITORS`, `panel._contents`, `panel._header`, `panel._title`, `panel.id`, `win.document`

## _onOpenTask()
- 位置: L221-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(monitor?.watchUrls ?? []).filter()`, `panel._contents.monitors?.find()`, `panel.hidePopup()`, `this._existingTaskGroup()`, `this._groupTaskTabs()`, `this._openTaskTabs()`
- 参照: `existingGroup.collapsed`, `existingGroup.tabs`, `lazy.isAllowedWatchUrl`, `m.id`, `monitor.monitorName`, `monitor?.watchUrls`, `urls.length`, `win.gBrowser.selectedTab`

## _existingTaskGroup()
- 位置: L248-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._taskTabGroupIds.get()`, `this._taskTabGroupIds.get(win)?.get()`, `win.gBrowser.tabGroups.find()`
- 参照: `group.id`

## _openTaskTabs()
- 位置: L267-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `urls.map()`, `win.gBrowser.addTab()`
- XPCOM: `Services.scriptSecurityManager`

## _groupTaskTabs()
- 位置: L293-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `groupIds.set()`, `this._taskTabGroupIds.get()`, `this._taskTabGroupIds.set()`, `win.gBrowser.addTabGroup()`
- 参照: `group.id`, `lazy.TabMetrics.METRIC_SOURCE.SMART_WINDOW_TASKS`

## _watchableUrl()
- 位置: L314-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.isAllowedWatchUrl()`
- 参照: `win.gBrowser?.currentURI?.spec`

## _openCreateView()
- 位置: L321-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._setView()`, `this._watchableUrl()`
- 参照: `panel._contents.agent`

## _setView()
- 位置: L334-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `backButton.addEventListener()`, `backButton.setAttribute()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `lazy.gBundle.GetStringFromName()`, `panel._header.prepend()`, `panel._header.querySelector()`, `this._setView()`
- 条件付き依存: `if (view === "list")` → `existing?.remove()`
- 参照: `backButton.className`, `panel._contents.view`, `panel._title`, `panel.ownerDocument`

## _syncContents()
- 位置: async L366-385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.listMonitors()`, `lazy.MonitorUIUtils.formatMonitorForDisplay()`, `monitors .sort()`, `monitors .sort((a, b) => new Date(b.lastRunTime) - new Date(a.lastRunTime)) .map()`
- 参照: `a.lastRunTime`, `b.lastRunTime`, `panel._contents.monitors`, `panel.isConnected`

## _onCreateSubmit()
- 位置: async L391-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.MonitorAgent.createMonitor()`, `this._setView()`, `this._toAgentSchedule()`
- 参照: `panel._contents.draft`, `panel._contents.justCreatedId`, `panel.isConnected`

## _toAgentSchedule()
- 位置: L422-433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`, `schedule.time.split()`, `schedule.time.split(":").map()`
- 参照: `schedule.frequency`, `schedule.weekday`
