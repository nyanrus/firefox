# browser/base/content/browser-sync.js

source: browser/base/content/browser-sync.js
source-hash: 8631d88912fb55054ac9484b7ef283621e9c1ba5
lines: 4342

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`

## SyncedTabsPanelList.constructor()
- 位置: L72-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.resolve()`, `Services.obs.addObserver()`, `this.createSyncedTabs()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this.QueryInterface`, `this._showSyncedTabsPromise`, `this.deck`, `this.separator`, `this.tabsList`
- XPCOM: `Services.obs`

## SyncedTabsPanelList.observe()
- 位置: L87-91
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == SyncedTabs.TOPIC_TABS_CHANGED)` → `this._showSyncedTabs()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`

## SyncedTabsPanelList.createSyncedTabs()
- 位置: L93-122
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs().catch()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `console.error()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `this.deck.toggleAttribute()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `this._showSyncedTabs()`
- 条件付き依存: `if (!(SyncedTabs.isConfiguredToSyncTabs))` → `this.deck.toggleAttribute()`
- 参照: `SyncedTabs.hasSyncedThisSession`, `SyncedTabs.isConfiguredToSyncTabs`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_FETCHING`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_TABS`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_TABSDISABLED`, `this.deck.selectedIndex`, `this.separator`, `this.separator.hidden`

## SyncedTabsPanelList._showSyncedTabs()
- 位置: L125-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.__showSyncedTabs()`, `this._showSyncedTabsPromise.then()`
- 参照: `this._showSyncedTabsPromise`

## SyncedTabsPanelList.__showSyncedTabs()
- 位置: L137-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `SyncedTabs.getTabClients()`, `SyncedTabs.getTabClients() .then()`, `SyncedTabs.sortTabClientsByLastUsed()`, `UIState.get()`, `console.error()`, `container.classList.add()`, `container.setAttribute()`, `document.createDocumentFragment()`, `document.createXULElement()`, `fragment.appendChild()`, `this._appendSyncClient()`, `this._clearSyncedTabList()`, `this.deck.toggleAttribute()`, `this.tabsList.appendChild()`
- 条件付き依存: `if (fragment.lastElementChild)` → `document.createXULElement()`
- 条件付き依存: `if (fragment.lastElementChild)` → `fragment.appendChild()`
- 参照: `SyncedTabs.hasSyncedThisSession`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_NOCLIENTS`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_TABS`, `UIState.get().syncEnabled`, `client.id`, `clients.length`, `fragment.lastElementChild`, `paginationInfo.clientId`, `this.deck.selectedIndex`, `this.separator`, `this.separator.hidden`, `this.tabsList`
- XPCOM: `Services.obs`

## SyncedTabsPanelList._clearSyncedTabList()
- 位置: L212-217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.lastChild.remove()`
- 参照: `list.lastChild`, `this.tabsList`

## SyncedTabsPanelList._createNoSyncedTabsElement()
- 位置: L219-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appendTo.appendChild()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `this.tabsList.getAttribute()`
- 参照: `this.tabsList`

## SyncedTabsPanelList._appendSyncClient()
- 位置: L233-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clientItem.setAttribute()`, `container.appendChild()`, `document.createXULElement()`, `gSync.fluentStrings.formatValueSync()`, `gSync.formatLastSyncDate()`
- 条件付き依存: `if (!client.tabs.length)` → `this._createNoSyncedTabsElement()`
- 条件付き依存: `if (!client.tabs.length)` → `label.setAttribute()`
- 条件付き依存: `if (!(!client.tabs.length))` → `fxAccounts.device.recentDeviceList.find()`
- 条件付き依存: `if (!(!client.tabs.length))` → `Weave.Service.clientsEngine.getClientFxaDeviceId()`
- 条件付き依存: `if (!(!client.tabs.length))` → `fxAccounts.commands.closeTab.isDeviceCompatible()`
- 条件付き依存: `if (!(!client.tabs.length))` → `client.tabs.filter()`
- 条件付き依存: `if (hasInactive)` → `container.append()`
- 条件付き依存: `if (hasInactive)` → `this._createShowInactiveTabsElement()`
- 条件付き依存: `if (nextPageIsLastPage)` → `Math.min()`
- 条件付き依存: `if (hasNextPage)` → `tabs.slice()`
- 条件付き依存: `if (!(!client.tabs.length))` → `tabs.entries()`
- 条件付き依存: `if (!(!client.tabs.length))` → `this._createSyncedTabElement()`
- 条件付き依存: `if (!(!client.tabs.length))` → `container.appendChild()`
- 条件付き依存: `if (hasNextPage)` → `this._createShowMoreSyncedTabsElement()`
- 条件付き依存: `if (hasNextPage)` → `container.appendChild()`
- 参照: `SyncedTabsPanelList.sRemoteTabsNextPageMinTabs`, `SyncedTabsPanelList.sRemoteTabsPerPage`, `client.id`, `client.lastModified`, `client.name`, `client.tabs.length`, `clientItem.className`, `clientItem.textContent`, `d.id`, `fxAccounts.device.recentDeviceList`, `t.inactive`, `tabs.length`

## SyncedTabsPanelList._createShowMoreSyncedTabsElement()
- 位置: L306-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `e.preventDefault()`, `e.stopPropagation()`, `showMoreItem.addEventListener()`, `showMoreItem.classList.add()`, `showMoreItem.setAttribute()`, `this._showSyncedTabs()`
- 参照: `paginationInfo.maxTabs`

## SyncedTabsPanelList._createShowInactiveTabsElement()
- 位置: L322-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `client.tabs .filter()`, `client.tabs .filter(t => t.inactive) .map()`, `container.replaceChildren()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `fxAccounts.commands.closeTab.isDeviceCompatible()`, `node.querySelector()`, `showItem.addEventListener()`, `showItem.classList.add()`, `showItem.setAttribute()`, `this._createSyncedTabElement()`
- 参照: `client.name`, `label.textContent`, `t.inactive`

## SyncedTabsPanelList._createSyncedTabElement()
- 位置: L359-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `Services.scriptSecurityManager.createNullPrincipal()`, `SyncedTabs.recordSyncedTabsTelemetry()`, `document.createXULElement()`, `document.defaultView.openUILink()`, `index.toString()`, `item.addEventListener()`, `item.classList.add()`, `item.setAttribute()`, `tabContainer.appendChild()`, `tabContainer.setAttribute()`, `window.gSync._getEntryPointForElement()`
- 条件付き依存: `if (tabInfo.icon)` → `item.setAttribute()`
- 条件付き依存: `if (BrowserUtils.whereToOpenLink(e) != "current")` → `e.preventDefault()`
- 条件付き依存: `if (BrowserUtils.whereToOpenLink(e) != "current")` → `e.stopPropagation()`
- 条件付き依存: `if (!(BrowserUtils.whereToOpenLink(e) != "current"))` → `CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (canCloseTabs)` → `this._createCloseTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `tabContainer.appendChild()`
- 条件付き依存: `if (canCloseTabs)` → `this._createUndoCloseTabElement()`
- 参照: `closeBtn.tab`, `e.currentTarget`, `tabInfo.icon`, `tabInfo.title`, `tabInfo.url`, `undoBtn.tab`
- XPCOM: `Services.scriptSecurityManager`

## SyncedTabsPanelList._createCloseTabElement()
- 位置: L418-463
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncedTabsManagement.enqueueTabToClose()`, `closeBtn.addEventListener()`, `closeBtn.classList.add()`, `closeBtn.setAttribute()`, `document.createXULElement()`, `e.stopPropagation()`, `gSync.fluentStrings.formatValueSync()`, `tabContainer.querySelector()`, `tabList.querySelector()`
- 条件付き依存: `if (prevClose)` → `prevCloseContainer.classList.add()`
- 条件付き依存: `if (prevClose)` → `prevCloseContainer.addEventListener()`
- 条件付き依存: `if (prevClose)` → `prevCloseContainer.remove()`
- 参照: `closeBtn.hidden`, `closeBtn.parentNode`, `closeBtn.tab`, `closeBtn.tab.disabled`, `device.id`, `device.name`, `prevClose.parentNode`, `tabContainer.parentNode`, `undoBtn.hidden`

## SyncedTabsPanelList._createUndoCloseTabElement()
- 位置: L465-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncedTabsManagement.removePendingTabToClose()`, `document.createXULElement()`, `e.stopPropagation()`, `undoBtn.addEventListener()`, `undoBtn.classList.add()`, `undoBtn.parentNode.querySelector()`, `undoBtn.setAttribute()`
- 参照: `closeBtn.hidden`, `device.id`, `undoBtn.hidden`, `undoBtn.tab`, `undoBtn.tab.disabled`

## SyncedTabsPanelList.destroy()
- 位置: L488-493
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this.deck`, `this.separator`, `this.tabsList`
- XPCOM: `Services.obs`

## FxAMenuDeviceList.constructor()
- 位置: L503-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.resolve()`, `Services.obs.addObserver()`, `gSync.refreshFxaDevices()`, `this._initDeviceList()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this.QueryInterface`, `this._removalTimers`, `this._updateDevicesPromise`, `this.devicesList`
- XPCOM: `Services.obs`

## FxAMenuDeviceList.observe()
- 位置: L522-526
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == SyncedTabs.TOPIC_TABS_CHANGED)` → `this._updateDeviceList()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`

## FxAMenuDeviceList._initDeviceList()
- 位置: L528-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateDeviceList()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs().catch()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `console.error()`
- 参照: `SyncedTabs.isConfiguredToSyncTabs`

## FxAMenuDeviceList._updateDeviceList()
- 位置: L537-542
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this._doUpdateDeviceList()`, `this._updateDevicesPromise.then()`
- 参照: `this._updateDevicesPromise`

## FxAMenuDeviceList._doUpdateDeviceList()
- 位置: async L544-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `SyncedTabs.sortTabClientsByLastUsed()`, `UIState.get()`, `console.error()`, `document .getElementById()`, `document .getElementById("appMenu-popup") ?.contains()`, `this._getMergedDeviceList()`, `this.devicesList.lastChild.remove()`
- 条件付き依存: `if (!UIState.get().syncEnabled || !clients.length)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (inAppMenu)` → `this._getDeviceForClient()`
- 条件付き依存: `if (inAppMenu)` → `this.devicesList.appendChild()`
- 条件付き依存: `if (inAppMenu)` → `document.createXULElement()`
- 条件付き依存: `if (inAppMenu)` → `this._appendDeviceSection()`
- 条件付き依存: `if (!(inAppMenu))` → `clients.slice()`
- 条件付き依存: `if (!(inAppMenu))` → `this._getDeviceForClient()`
- 条件付き依存: `if (!(inAppMenu))` → `this.devicesList.appendChild()`
- 条件付き依存: `if (!(inAppMenu))` → `this._createDeviceEntry()`
- 条件付き依存: `if (clients.length > FxAMenuDeviceList.MAX_DEVICES)` → `this.devicesList.appendChild()`
- 条件付き依存: `if (clients.length > FxAMenuDeviceList.MAX_DEVICES)` → `this._createAllDevicesButton()`
- 参照: `FxAMenuDeviceList.MAX_DEVICES`, `UIState.get().syncEnabled`, `clients.length`, `this.devicesList`, `this.devicesList.hidden`, `this.devicesList.lastChild`
- XPCOM: `Services.obs`

## FxAMenuDeviceList._getDeviceForClient()
- 位置: L608-620
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Weave.Service.clientsEngine.getClientFxaDeviceId()`, `devices.find()`
- 参照: `client.id`, `d.id`, `fxAccounts.device.recentDeviceList`

## FxAMenuDeviceList._getMergedDeviceList()
- 位置: async L637-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncedTabs.getTabClients()`, `Weave.Service.clientsEngine.getClientFxaDeviceId()`, `clientByFxaId.get()`, `matchedClients.has()`
- 条件付き依存: `if (fxaDeviceId)` → `clientByFxaId.set()`
- 条件付き依存: `if (client)` → `matchedClients.add()`
- 条件付き依存: `if (client)` → `merged.push()`
- 条件付き依存: `if (!(client))` → `fxAccounts.commands.sendTab.isDeviceCompatible()`
- 条件付き依存: `if (fxAccounts.commands.sendTab.isDeviceCompatible(device))` → `merged.push()`
- 条件付き依存: `if (!matchedClients.has(client))` → `merged.push()`
- 参照: `client.id`, `device.id`, `device.isCurrentDevice`, `device.lastAccessTime`, `device.name`, `fxAccounts.device.recentDeviceList`

## FxAMenuDeviceList._createAllDevicesButton()
- 位置: L685-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `btn.addEventListener()`, `btn.classList.add()`, `btn.setAttribute()`, `document.createXULElement()`, `this._showAllDevices()`
- 参照: `btn.id`

## FxAMenuDeviceList._showAllDevices()
- 位置: L697-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `list.appendChild()`, `list.replaceChildren()`, `this._createDeviceEntry()`, `this._getDeviceForClient()`

## FxAMenuDeviceList._getDeviceClientType()
- 位置: L710-721
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `device.type`

## FxAMenuDeviceList._getTelemetryDeviceType()
- 位置: L723-728
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `device?.type`

## FxAMenuDeviceList._createDeviceEntry()
- 位置: L730-763
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `btn.addEventListener()`, `btn.classList.add()`, `btn.setAttribute()`, `document.createXULElement()`, `gSync.emitFxaToolbarTelemetry()`, `gSync.fluentStrings.formatValueSync()`, `gSync.formatLastSyncDate()`, `gSync.getSendTabTargets()`, `this._getDeviceClientType()`, `this._getDeviceForClient()`, `this._getTelemetryDeviceType()`, `this._showDeviceRecentTabs()`
- 参照: `client.lastModified`, `client.name`, `gSync.getSendTabTargets().length`

## FxAMenuDeviceList._getRecentTabs()
- 位置: L765-769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `client.tabs .filter()`, `client.tabs .filter(t => !t.inactive) .slice()`
- 参照: `FxAMenuDeviceList.MAX_RECENT_TABS`, `t.inactive`

## FxAMenuDeviceList._populateRecentTabs()
- 位置: L775-795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fxAccounts.commands.closeTab.isDeviceCompatible()`, `item.render()`, `recentTabs.entries()`, `tabContainer.querySelector()`, `tabsList.appendChild()`, `this._createSyncedTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `this._createCloseTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `this._createUndoCloseTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `tabContainer.append()`
- 参照: `closeBtn.tab`, `tab.url`, `undoBtn.tab`

## FxAMenuDeviceList._configureViewAllTabsButton()
- 位置: L797-813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSync.fluentStrings.formatMessagesSync()`, `viewAllBtn.setAttribute()`, `viewAllMessage.attributes?.find()`
- 参照: `attr.name`, `viewAllBtn.onclick`, `viewAllMessage.attributes?.find(attr => attr.name === "label")?.value`

## viewAllBtn.onclick()
- 位置: L808-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.hidePanelForNode()`, `SidebarController.show()`, `gSync.emitFxaToolbarTelemetry()`

## FxAMenuDeviceList._canSendTabToDevice()
- 位置: L815-821
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `fxAccounts.commands.sendTab.isDeviceCompatible()`
- 参照: `gBrowser.selectedBrowser.currentURI`

## FxAMenuDeviceList._configureSendPageButton()
- 位置: L829-861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `gSync.emitFxaToolbarTelemetry()`, `gSync.getSendTabTargets()`
- 参照: `sendPageBtn.onclick`, `targets.length`

## sendPageBtn.onclick()
- 位置: L837-860
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `CustomizableUI.hidePanelForNode()`, `PrivateBrowsingUtils.isBrowserPrivate()`, `String()`, `gBrowser.selectedTabs.map()`, `gSync.emitFxaToolbarTelemetry()`, `gSync.sendTabsAndConfirm()`
- 参照: `BrowserUtils.getShareableURL( gBrowser.selectedBrowser.currentURI ).spec`, `gBrowser.selectedBrowser.contentTitle`, `gBrowser.selectedBrowser.currentURI`, `gBrowser.selectedTab.multiselected`, `t.linkedBrowser.contentTitle`, `t.linkedBrowser.currentURI.spec`, `targets.length`

## FxAMenuDeviceList._showDeviceRecentTabs()
- 位置: L863-919
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `panelNode.querySelector()`, `tabsList.replaceChildren()`, `this._canSendTabToDevice()`, `this._configureViewAllTabsButton()`, `this._getRecentTabs()`, `this._populateRecentTabs()`, `this._trackTabCount()`
- 条件付き依存: `if (remaining)` → `this._configureViewAllTabsButton()`
- 条件付き依存: `if (canSendTab)` → `this._configureSendPageButton()`
- 参照: `client.tabs.length`, `footerSeparator.hidden`, `noTabsLabel.hidden`, `recentTabs.length`, `sendPageBtn.hidden`, `tabsList.hidden`, `viewAllBtn.hidden`

## FxAMenuDeviceList._appendDeviceSection()
- 位置: L926-988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `gSync.fluentStrings.formatValueSync()`, `gSync.formatLastSyncDate()`, `header.classList.add()`, `header.setAttribute()`, `list.appendChild()`, `noTabsLabel.classList.add()`, `noTabsLabel.setAttribute()`, `this._canSendTabToDevice()`, `this._getRecentTabs()`
- 条件付き依存: `if (recentTabs.length)` → `document.createXULElement()`
- 条件付き依存: `if (recentTabs.length)` → `tabsList.classList.add()`
- 条件付き依存: `if (recentTabs.length)` → `this._populateRecentTabs()`
- 条件付き依存: `if (recentTabs.length)` → `list.append()`
- 条件付き依存: `if (recentTabs.length)` → `viewAllBtn.classList.add()`
- 条件付き依存: `if (recentTabs.length)` → `viewAllBtn.setAttribute()`
- 条件付き依存: `if (recentTabs.length)` → `this._configureViewAllTabsButton()`
- 条件付き依存: `if (recentTabs.length)` → `list.appendChild()`
- 条件付き依存: `if (recentTabs.length)` → `this._trackTabCount()`
- 条件付き依存: `if (remaining)` → `this._configureViewAllTabsButton()`
- 条件付き依存: `if (!(recentTabs.length))` → `list.appendChild()`
- 条件付き依存: `if (this._canSendTabToDevice(device))` → `document.createXULElement()`
- 条件付き依存: `if (this._canSendTabToDevice(device))` → `sendPageBtn.classList.add()`
- 条件付き依存: `if (this._canSendTabToDevice(device))` → `sendPageBtn.setAttribute()`
- 条件付き依存: `if (this._canSendTabToDevice(device))` → `list.appendChild()`
- 条件付き依存: `if (this._canSendTabToDevice(device))` → `this._configureSendPageButton()`
- 参照: `client.lastModified`, `client.name`, `client.tabs.length`, `header.textContent`, `noTabsLabel.hidden`, `recentTabs.length`, `tabsList.hidden`, `this.devicesList`, `viewAllBtn.hidden`

## FxAMenuDeviceList._createTabToolbarButton()
- 位置: L1001-1009
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `btn.addEventListener()`, `btn.classList.add()`, `document.createXULElement()`
- 条件付き依存: `if (closemenu)` → `btn.setAttribute()`

## FxAMenuDeviceList._createSyncedTabElement()
- 位置: L1011-1051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `Services.scriptSecurityManager.createNullPrincipal()`, `SyncedTabs.recordSyncedTabsTelemetry()`, `document.createXULElement()`, `document.defaultView.openUILink()`, `index.toString()`, `item.setAttribute()`, `tabContainer.appendChild()`, `tabContainer.setAttribute()`, `this._createTabToolbarButton()`, `window.gSync._getEntryPointForElement()`
- 条件付き依存: `if (BrowserUtils.whereToOpenLink(e) != "current")` → `e.preventDefault()`
- 条件付き依存: `if (BrowserUtils.whereToOpenLink(e) != "current")` → `e.stopPropagation()`
- 条件付き依存: `if (!(BrowserUtils.whereToOpenLink(e) != "current"))` → `CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (tabInfo.icon)` → `item.setAttribute()`
- 参照: `e.currentTarget`, `tabInfo.icon`, `tabInfo.title`, `tabInfo.url`
- XPCOM: `Services.scriptSecurityManager`

## FxAMenuDeviceList._createCloseTabElement()
- 位置: L1053-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncedTabsManagement.enqueueTabToClose()`, `closeBtn.setAttribute()`, `e.stopPropagation()`, `gSync.fluentStrings.formatValueSync()`, `tabContainer.querySelector()`, `this._createTabToolbarButton()`, `this._scheduleTabRowRemoval()`
- 参照: `closeBtn.hidden`, `closeBtn.parentNode`, `closeBtn.tab`, `closeBtn.tab.disabled`, `device.id`, `device.name`, `undoBtn.hidden`

## FxAMenuDeviceList._createUndoCloseTabElement()
- 位置: L1084-1107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncedTabsManagement.removePendingTabToClose()`, `e.stopPropagation()`, `tabContainer.querySelector()`, `this._cancelTabRowRemoval()`, `this._createTabToolbarButton()`, `undoBtn.setAttribute()`
- 参照: `closeBtn.hidden`, `device.id`, `undoBtn.hidden`, `undoBtn.parentNode`, `undoBtn.tab`, `undoBtn.tab.disabled`

## FxAMenuDeviceList._trackTabCount()
- 位置: L1115-1118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tabsList.applyTabCount`, `tabsList.tabCount`

## FxAMenuDeviceList._scheduleTabRowRemoval()
- 位置: L1125-1148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `tabContainer.addEventListener()`, `tabContainer.classList.add()`, `tabContainer.remove()`, `this._removalTimers.add()`, `this._removalTimers.delete()`
- 条件付き依存: `if (tabsList.applyTabCount)` → `Math.max()`
- 条件付き依存: `if (tabsList.applyTabCount)` → `tabsList.applyTabCount()`
- 参照: `FxAMenuDeviceList.TAB_REMOVAL_DELAY_MS`, `tabContainer.parentNode`, `tabContainer.removalTimer`, `tabsList.applyTabCount`, `tabsList.tabCount`

## FxAMenuDeviceList._cancelTabRowRemoval()
- 位置: L1150-1154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearTimeout()`, `this._removalTimers.delete()`
- 参照: `tabContainer.removalTimer`

## FxAMenuDeviceList.destroy()
- 位置: L1156-1163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `clearTimeout()`, `this._removalTimers.clear()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this._removalTimers`, `this.devicesList`
- XPCOM: `Services.obs`

## log()
- 位置: L1211-1221
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._log)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!this._log)` → `Log.repository.getLogger()`
- 条件付き依存: `if (!this._log)` → `syncLog.manageLevelFromPref()`
- 参照: `this._log`

## fluentStrings()
- 位置: L1223-1238
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.fluentStrings`

## sendTabConfiguredAndLoading()
- 位置: L1242-1249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`, `fxAccounts.device.recentDeviceList`, `state.status`, `state.syncEnabled`

## isSignedIn()
- 位置: L1251-1253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`, `UIState.get().status`

## isUnverified()
- 位置: L1255-1257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_NOT_VERIFIED`, `UIState.get().status`

## isSignedInWithSyncDisabled()
- 位置: L1259-1262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`, `state.status`, `state.syncEnabled`

## hasNoSendTabTargets()
- 位置: L1264-1266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSendTabTargets()`
- 参照: `this.getSendTabTargets().length`

## getSyncPromoState()
- 位置: L1271-1302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `UIState.get()`, `devices?.some()`, `requiredEngines.some()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`, `d.isCurrentDevice`, `fxAccounts.device.recentDeviceList`, `state.status`, `state.syncEnabled`, `this.FXA_ENABLED`
- XPCOM: `Services.prefs`

## handleSyncPromoAction()
- 位置: L1307-1319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openConnectAnotherDevice()`, `this.openFxAEmailFirstPage()`, `this.openSyncSetupForEntryPoint()`

## shouldHideSendContextMenuItems()
- 位置: L1321-1323
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.FXA_ENABLED`

## getSendTabTargets()
- 位置: L1325-1345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `fxAccounts.commands.sendTab.isDeviceCompatible()`, `targets.sort()`
- 条件付き依存: `if (fxAccounts.commands.sendTab.isDeviceCompatible(d))` → `targets.push()`
- 参照: `UIState.STATUS_SIGNED_IN`, `a.lastAccessTime`, `b.lastAccessTime`, `d.isCurrentDevice`, `fxAccounts.device.recentDeviceList`, `state.status`, `state.syncEnabled`

## getTargetClientType()
- 位置: L1349-1355
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target.clientRecord)` → `Weave.Service.clientsEngine.getClientType()`
- 参照: `target.clientRecord`, `target.clientRecord.id`, `target.type`

## hasOnlyMobileSendTabTargets()
- 位置: L1357-1365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `targets.every()`, `this.getSendTabTargets()`
- 参照: `target.type`, `targets.length`

## _definePrefGetters()
- 位置: L1367-1385
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `this.updateAppMenuSignInPromo()`

## maybeUpdateUIState()
- 位置: L1387-1401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.isReady()`
- 条件付き依存: `if (UIState.isReady())` → `UIState.get()`
- 条件付き依存: `if ( state.status != UIState.STATUS_NOT_CONFIGURED || this._hasSignedOutOfSync )` → `this.updateAllUI()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `state.status`, `this._hasSignedOutOfSync`

## init()
- 位置: L1403-1588
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.hidePanelForNode()`, `EnsureFxAccountsWebChannel()`, `MozXULElement.insertFTLIfNeeded()`, `NimbusFeatures.fxaButtonVisibility.getVariable()`, `PanelMultiView.getViewNode()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-all-devices" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-secure-sync-subpanel" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sendtab-connect-phone-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sendtab-enable-sync-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sendtab-no-phone-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sendtab-sign-in-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sendtab-verify-account-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sign-in-promo-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-signed-out-sign-in-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sync-status-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-sync-status-off-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "appMenu-fxa-sign-in-promo-dismiss-button" ).addEventListener()`, `PanelMultiView.getViewNode( document, "appMenu-fxa-sign-in-promo-link" ).addEventListener()`, `PanelMultiView.getViewNode( document, "appMenu-fxa-signed-out-sign-in-button" ).addEventListener()`, `PanelUI.mainView.addEventListener()`, `Services.obs.addObserver()`, `document.getElementById()`, `document.l10n.setAttributes()`, `fxaPanelView.addEventListener()`, `this._definePrefGetters()`, `this._onSyncStatusButtonClick()`, `this.fluentStrings.formatValuesSync()`, `this.maybeUpdateUIState()`, `this.openPrefsFromFxaMenu()`, `this.updateAppMenuSignInPromo()`
- 条件付き依存: `if (!this.FXA_ENABLED)` → `this.onFxaDisabled()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `this.updateFxAPanel()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `UIState.get()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `this.updateCTAPanel()`
- 条件付き依存: `if (avatarIconVariant)` → `this.applyAvatarIconVariant()`
- 参照: `PanelMultiView.getViewNode( document, "PanelUI-remotetabs-setupsync" ).hidden`, `appMenuHeaderDescription.value`, `appMenuHeaderText.textContent`, `appMenuHeaderTitle.hidden`, `document.getElementById("sync-setup").hidden`, `e.currentTarget`, `novaFxaLabel.label`, `this.FXA_CTA_MENU_ENABLED`, `this.FXA_ENABLED`, `this._initialized`, `this._obs`
- XPCOM: `Services.obs`

## uninit()
- 位置: L1590-1600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._obs`
- XPCOM: `Services.obs`

## handleEvent()
- 位置: L1602-1624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onCommand()`, `this.onFxAPanelViewHiding()`, `this.refreshSyncButtonsTooltip()`
- 条件付き依存: `if (event.target == PanelUI.mainView)` → `this.onAppMenuShowing()`
- 条件付き依存: `if (!(event.target == PanelUI.mainView))` → `this.onFxAPanelViewShowing()`
- 参照: `PanelUI.mainView`, `event.target`, `event.type`

## onAppMenuShowing()
- 位置: L1626-1643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NimbusFeatures.fxaAppMenuItem.getVariable()`, `PanelMultiView.getViewNode()`, `document.l10n.setAttributes()`, `this.getMenuCtaCopy()`
- 条件付き依存: `if (NimbusFeatures.fxaAppMenuItem.getVariable("ctaCopyVariant"))` → `NimbusFeatures.fxaAppMenuItem.recordExposureEvent()`
- 参照: `NimbusFeatures.fxaAppMenuItem`

## updateAppMenuSignInPromo()
- 位置: L1651-1656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.toggleAttribute()`
- 参照: `this.APP_MENU_SIGN_IN_PROMO_DISMISSED`

## dismissAppMenuSignInPromo()
- 位置: L1658-1660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## onFxAPanelViewShowing()
- 位置: L1662-1721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NimbusFeatures.fxaAvatarMenuItem.getVariable()`, `PanelMultiView.getViewNode()`, `UIState.get()`, `document .getElementById()`, `document .getElementById("appMenu-popup") ?.contains()`, `panelview.getAttribute()`
- 条件付き依存: `if (messageId)` → `MenuMessage.recordMenuMessageTelemetry()`
- 条件付き依存: `if (messageId)` → `ASRouter.getMessageById()`
- 条件付き依存: `if (messageId)` → `ASRouter.addImpression()`
- 条件付き依存: `if (!syncEnabled)` → `this._disableSyncOffIndicator()`
- 条件付き依存: `if (inAppMenu)` → `signOutButtonEl.after()`
- 条件付き依存: `if (!(inAppMenu))` → `signOutSeparatorEl.before()`
- 条件付き依存: `if (ctaCopyVariant)` → `NimbusFeatures.fxaAvatarMenuItem.recordExposureEvent()`
- 参照: `MenuMessage.SHOWING_FXA_MENU_MESSAGE_ATTR`, `MenuMessage.SOURCES.PXI_MENU`, `UIState.get().syncEnabled`, `panelview.syncedTabsPanelList`, `signOutButtonEl.hidden`, `this.isSignedIn`

## onFxAPanelViewHiding()
- 位置: L1723-1727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MenuMessage.hidePxiMenuMessage()`, `panelview.syncedTabsPanelList.destroy()`
- 参照: `gBrowser.selectedBrowser`, `panelview.syncedTabsPanelList`

## _showSecureSyncSubpanel()
- 位置: L1729-1732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelUI.showSubView()`, `this._updateSecureSyncNowLabel()`

## _updateAppMenuSignedOutRow()
- 位置: L1734-1751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (email)` → `titleEl.removeAttribute()`
- 条件付き依存: `if (!(email))` → `document.l10n.setAttributes()`
- 参照: `titleEl.textContent`

## _updateSecureSyncNowLabel()
- 位置: L1757-1779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`
- 条件付き依存: `if (this._isCurrentlySyncing)` → `labelEl.setAttribute()`
- 条件付き依存: `if (this._isCurrentlySyncing)` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(this._isCurrentlySyncing))` → `fxAccounts.device.getLocalName()`
- 条件付き依存: `if (!(this._isCurrentlySyncing))` → `labelEl.setAttribute()`
- 条件付き依存: `if (!(this._isCurrentlySyncing))` → `this.fluentStrings.formatValueSync()`
- 参照: `this._isCurrentlySyncing`

## _hasSignedOutOfSync()
- 位置: L1788-1790
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## _updateSyncStatusButton()
- 位置: L1804-1919
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `btn.after()`, `btn.classList.toggle()`, `descEl.hasAttribute()`, `this.fluentStrings.formatValueSync()`, `titleEl.setAttribute()`
- 条件付き依存: `if (syncOffCard)` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (syncOffCard)` → `offTitleEl.setAttribute()`
- 条件付き依存: `if (syncOffCard)` → `offDescEl.setAttribute()`
- 条件付き依存: `if (syncOffCard)` → `onButtonEl.setAttribute()`
- 条件付き依存: `if (syncOffCard)` → `[offTitle, offDesc, onText].join()`
- 条件付き依存: `if (syncOffCard)` → `offCard.after()`
- 条件付き依存: `if (syncOn)` → `descEl.classList.remove()`
- 条件付き依存: `if (syncOn)` → `this.formatLastSyncDate()`
- 条件付き依存: `if (lastSyncDate)` → `descEl.setAttribute()`
- 条件付き依存: `if (lastSyncDate)` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(lastSyncDate))` → `descEl.removeAttribute()`
- 条件付き依存: `if (neverSignedIn)` → `descEl.classList.remove()`
- 条件付き依存: `if (neverSignedIn)` → `descEl.removeAttribute()`
- 条件付き依存: `if (!(neverSignedIn))` → `descEl.classList.add()`
- 条件付き依存: `if (!(neverSignedIn))` → `descEl.setAttribute()`
- 条件付き依存: `if (!(neverSignedIn))` → `this.fluentStrings.formatValueSync()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_SIGNED_IN`, `btn.hidden`, `descEl.hidden`, `mobileBtn.hidden`, `offCard.hidden`, `state.lastSync`, `state.status`, `state.syncEnabled`, `this._hasSignedOutOfSync`

## _onSyncStatusButtonClick()
- 位置: L1921-1936
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN && state.syncEnabled)` → `this._showSecureSyncSubpanel()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `this.openPrefsFromFxaMenu()`
- 条件付き依存: `if (!(state.status == UIState.STATUS_SIGNED_IN))` → `this.emitFxaToolbarTelemetry()`
- 条件付き依存: `if (!(state.status == UIState.STATUS_SIGNED_IN))` → `this.openFxAEmailFirstPageFromFxaMenu()`
- 条件付き依存: `if (!(state.status == UIState.STATUS_SIGNED_IN && state.syncEnabled))` → `CustomizableUI.hidePanelForNode()`
- 参照: `UIState.STATUS_SIGNED_IN`, `state.status`, `state.syncEnabled`

## onCommand()
- 位置: L1938-2014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelUI.hide()`, `this._getEntryPointForElement()`, `this.clickFxAMenuHeaderButton()`, `this.clickOpenConnectAnotherDevice()`, `this.disconnect()`, `this.dismissAppMenuSignInPromo()`, `this.doSyncFromFxaMenu()`, `this.emitFxaToolbarTelemetry()`, `this.enableSync()`, `this.openDeviceMissingHelp()`, `this.openDevicesManagementPage()`, `this.openFxAEmailFirstPageFromFxaMenu()`, `this.openGetFirefoxMobile()`, `this.openMonitorLink()`, `this.openPairDevice()`, `this.openPrefsFromFxaMenu()`, `this.openRelayLink()`, `this.openSendTabHelp()`, `this.openShareFirefoxLink()`, `this.openVPNLink()`, `this.signInToSync()`, `this.verifyAccount()`
- 参照: `button.id`

## observe()
- 位置: L2016-2040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `clearTimeout()`, `this.onClientsSynced()`, `this.updateAllUI()`, `this.updateFxAPanel()`
- 条件付き依存: `if (!this._initialized)` → `console.error()`
- 参照: `UIState.ON_UPDATE`, `this._initialized`, `this._syncAnimationTimer`

## updateAllUI()
- 位置: L2042-2050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureFxaDevices()`, `this.fetchListOfOAuthClients()`, `this.updateFxAPanel()`, `this.updatePanelPopup()`, `this.updateState()`, `this.updateSyncButtonsTooltip()`, `this.updateSyncStatus()`

## ensureFxaDevices()
- 位置: async L2058-2072
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`
- 条件付き依存: `if (UIState.get().status != UIState.STATUS_SIGNED_IN)` → `console.info()`
- 条件付き依存: `if (!fxAccounts.device.recentDeviceList)` → `this.refreshFxaDevices()`
- 条件付き依存: `if (!fxAccounts.device.recentDeviceList)` → `console.warn()`
- 参照: `UIState.STATUS_SIGNED_IN`, `UIState.get().status`, `fxAccounts.device.recentDeviceList`

## refreshFxaDevices()
- 位置: async L2080-2093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `fxAccounts.device.refreshDeviceList()`, `this.log.error()`
- 条件付き依存: `if (UIState.get().status != UIState.STATUS_SIGNED_IN)` → `console.info()`
- 参照: `UIState.STATUS_SIGNED_IN`, `UIState.get().status`

## fetchListOfOAuthClients()
- 位置: async L2100-2112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fxAccounts.listAttachedOAuthClients()`, `this.log.error()`
- 条件付き依存: `if (!this.isSignedIn)` → `console.info()`
- 参照: `this._attachedClients`, `this.isSignedIn`

## toggleAccountPanel()
- 位置: async L2114-2193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchor.getAttribute()`, `document.documentElement.getAttribute()`, `document.documentElement.hasAttribute()`, `document.getElementById()`
- 条件付き依存: `if (ASRouter.initialized)` → `ASRouter.sendTriggerMessage()`
- 条件付き依存: `if ( anchor.id == "appMenu-fxa-label2" || anchor.id == "appMenu-nova-fxa-label" )` → `this.openFxAEmailFirstPageFromFxaMenu()`
- 条件付き依存: `if ( anchor.id == "appMenu-fxa-label2" || anchor.id == "appMenu-nova-fxa-label" )` → `PanelUI.hide()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `this.updateFxAPanel()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `UIState.get()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `this.updateCTAPanel()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `PanelUI.showSubView()`
- 条件付き依存: `if (!(this.FXA_CTA_MENU_ENABLED))` → `this.updateFxAPanel()`
- 条件付き依存: `if (!(this.FXA_CTA_MENU_ENABLED))` → `UIState.get()`
- 条件付き依存: `if (!(this.FXA_CTA_MENU_ENABLED))` → `PanelUI.showSubView()`
- 条件付き依存: `if (!gFxaToolbarAccessed)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (anchor.getAttribute("open") == "true")` → `PanelUI.hide()`
- 条件付き依存: `if (!(anchor.getAttribute("open") == "true"))` → `this.emitFxaToolbarTelemetry()`
- 条件付き依存: `if (!(anchor.getAttribute("open") == "true"))` → `PanelUI.showSubView()`
- 参照: `ASRouter.initialized`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `MenuMessage.SOURCES.PXI_MENU`, `aEvent.button`, `aEvent.charCode`, `aEvent.keyCode`, `aEvent.type`, `anchor.id`, `gBrowser.selectedBrowser`, `this.FXA_CTA_MENU_ENABLED`
- XPCOM: `Services.prefs`

## _disableSyncOffIndicator()
- 位置: L2195-2202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(SYNC_PANEL_ACCESSED_PREF, false))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## updateFxAPanel()
- 位置: L2204-2411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NimbusFeatures.expandSignInButton.getVariable()`, `PanelMultiView.getViewNode()`, `document.getElementById()`, `mainWindowEl.setAttribute()`, `mainWindowEl.style.removeProperty()`, `manageAccountButtonEl.after()`, `manageAccountSeparator.remove()`, `menuHeaderDescriptionEl.removeAttribute()`, `menuHeaderTitleEl.removeAttribute()`, `signedInContainer.prepend()`, `this._positionSecureSyncSection()`, `this._showFxASignedOutCard()`, `this._updateSyncStatusButton()`, `this.fluentStrings.formatValueSync()`, `this.updateAvatarURL()`
- 条件付き依存: `if ( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy )` → `fxaAvatarLabelEl.setAttribute()`
- 条件付き依存: `if ( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy )` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if ( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy )` → `fxaAvatarLabelEl.removeAttribute()`
- 条件付き依存: `if ( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy )` → `fxaToolbarMenuButton.setAttribute()`
- 条件付き依存: `if ( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy )` → `fxaToolbarMenuButton.classList.add()`
- 条件付き依存: `if (!( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy ))` → `fxaToolbarMenuButton.setAttribute()`
- 条件付き依存: `if (!( state.status === UIState.STATUS_NOT_CONFIGURED && expandedSignInCopy ))` → `fxaToolbarMenuButton.classList.remove()`
- 条件付き依存: `if (this._hasSignedOutOfSync)` → `this._showFxASignedOutCard()`
- 条件付き依存: `if (this.FXA_CTA_MENU_ENABLED)` → `this.getMenuCtaCopy()`
- 参照: `NimbusFeatures.fxaAvatarMenuItem`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-manage-account-email" ).value`, `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`, `ctaCopy.headerDescription`, `ctaCopy.headerTitleL10nId`, `document.documentElement`, `fxaAvatarLabelEl.hidden`, `manageAccountButtonEl.hidden`, `manageAccountSeparator.hidden`, `menuHeaderDescriptionEl.hidden`, `menuHeaderDescriptionEl.value`, `menuHeaderTitleEl.value`, `signInPromoEl.hidden`, `signOutSeparator.hidden`, `signedInContainer.hidden`, `signedOutCardEl.hidden`, `signedOutSeparatorEl.hidden`, `state.avatarIsDefault`, `state.avatarURL`, `state.displayName`, `state.email`, `state.status`, `syncStatusBtn.hidden`, `this.FXA_CTA_MENU_ENABLED`, `this._hasSignedOutOfSync`

## _positionSecureSyncSection()
- 位置: L2416-2451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `anchorEl.after()`, `profileButtonsContainer.remove()`, `profilesHeaderLabel.remove()`, `profilesSeparator.remove()`, `secureSyncHeader.after()`, `secureSyncHeader.remove()`
- 参照: `secureSyncHeader.hidden`

## _showFxASignedOutCard()
- 位置: L2456-2489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`
- 条件付き依存: `if (state.status === UIState.STATUS_NOT_CONFIGURED)` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (state.status === UIState.STATUS_NOT_CONFIGURED)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(state.status === UIState.STATUS_NOT_CONFIGURED))` → `document.l10n.setAttributes()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `cardEl.hidden`, `emailEl.value`, `separatorEl.hidden`, `state.email`, `state.status`

## updateAvatarURL()
- 位置: L2491-2505
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(avatarURL && !avatarIsDefault))` → `mainWindowEl.style.removeProperty()`
- 参照: `img.onerror`, `img.onload`, `img.src`

## img.onload()
- 位置: L2495-2497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mainWindowEl.style.setProperty()`

## img.onerror()
- 位置: L2498-2500
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mainWindowEl.style.removeProperty()`

## emitFxaToolbarTelemetry()
- 位置: L2519-2568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AVATAR_MENU_ONLY_PROFILES_COUNT_EVENT_TYPES.has()`, `AVATAR_MENU_ONLY_PROFILES_EVENT_TYPES.has()`, `Glean[category][methodName]?.record()`, `UIState.get()`, `UIState.isReady()`, `gSync.NONPREFIXED_EVENT_TYPES.has()`, `parts.map()`, `parts.map(cap).join()`, `parts.slice()`, `parts.slice(1).map()`, `parts.slice(1).map(cap).join()`, `this._getEntryPointForElement()`, `type.split()`
- 条件付き依存: `if (AVATAR_MENU_ONLY_PROFILES_COUNT_EVENT_TYPES.has(type))` → `SelectableProfileService?.getCachedProfileCount()`
- 参照: `extraOptions.profile_count`, `state.avatarIsDefault`, `state.avatarURL`, `state.status`, `state.syncEnabled`

## cap()
- 位置: L2561-2561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `w.slice()`, `w[0].toUpperCase()`

## updatePanelPopup()
- 位置: L2570-2690
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `appMenuLabel.classList.add()`, `appMenuLabel.classList.remove()`, `appMenuLabel.removeAttribute()`, `appMenuLabel.setAttribute()`, `appMenuStatus.classList.remove()`, `appMenuStatus.removeAttribute()`, `appMenuStatus.setAttribute()`, `document.documentElement.toggleAttribute()`, `fxaPanelView.setAttribute()`, `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (status == UIState.STATUS_NOT_CONFIGURED)` → `appMenuStatus.classList.add()`
- 条件付き依存: `if (status == UIState.STATUS_NOT_CONFIGURED)` → `appMenuLabel.classList.remove()`
- 条件付き依存: `if (signedOut)` → `this._updateAppMenuSignedOutRow()`
- 条件付き依存: `if (signedOut)` → `appMenuStatus.setAttribute()`
- 条件付き依存: `if (status == UIState.STATUS_LOGIN_FAILED)` → `this.fluentStrings.formatValuesSync()`
- 条件付き依存: `if (status == UIState.STATUS_LOGIN_FAILED)` → `appMenuStatus.setAttribute()`
- 条件付き依存: `if (status == UIState.STATUS_LOGIN_FAILED)` → `appMenuLabel.classList.add()`
- 条件付き依存: `if (status == UIState.STATUS_LOGIN_FAILED)` → `appMenuLabel.removeAttribute()`
- 条件付き依存: `if (status == UIState.STATUS_LOGIN_FAILED)` → `appMenuLabel.setAttribute()`
- 条件付き依存: `if (status == UIState.STATUS_NOT_VERIFIED)` → `appMenuStatus.setAttribute()`
- 条件付き依存: `if (status == UIState.STATUS_NOT_VERIFIED)` → `this._updateAppMenuSignedOutRow()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `appMenuHeaderDescription.id`, `appMenuHeaderDescription.value`, `appMenuHeaderText.hidden`, `appMenuHeaderTitle.hidden`, `appMenuHeaderTitle.id`, `appMenuHeaderTitle.value`, `appMenuLabel.hidden`, `appMenuSignedOutRow.hidden`, `this._hasSignedOutOfSync`

## updateState()
- 位置: L2692-2725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.getElementById()`
- 参照: `PanelMultiView.getViewNode( document, boxId ).hidden`, `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`, `document.getElementById(menuId).hidden`, `state.status`, `state.syncEnabled`

## updateSyncStatus()
- 位置: L2727-2738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .getElementById()`, `document .getElementById("appMenu-viewCache") .content.querySelector()`, `document.querySelector()`, `syncNow.getAttribute()`
- 条件付き依存: `if (state.syncing != syncingUI)` → `this.onActivityStart()`
- 条件付き依存: `if (state.syncing != syncingUI)` → `this.onActivityStop()`
- 参照: `state.syncing`

## openSignInAgainPage()
- 位置: async L2740-2752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.canConnectAccount()`, `FxAccounts.config.promiseConnectAccountURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `switchToTabHavingURI()`
- XPCOM: `Services.scriptSecurityManager`

## openDevicesManagementPage()
- 位置: async L2754-2760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config.promiseManageDevicesURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `switchToTabHavingURI()`
- XPCOM: `Services.scriptSecurityManager`

## openConnectAnotherDevice()
- 位置: async L2762-2768
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config.promiseConnectDeviceURI()`, `openTrustedLinkIn()`

## clickOpenConnectAnotherDevice()
- 位置: async L2770-2774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openConnectAnotherDevice()`

## openSendToDevicePromo()
- 位置: L2776-2781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `switchToTabHavingURI()`
- XPCOM: `Services.urlFormatter`

## clickFxAMenuHeaderButton()
- 位置: async L2783-2802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `this._openFxAManagePageFromElement()`, `this.openFxAEmailFirstPage()`, `this.openFxAEmailFirstPageFromFxaMenu()`, `this.openPrefsFromFxaMenu()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`

## _getEntryPointForElement()
- 位置: L2811-2839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appMenuPanel.contains()`, `document.getElementById()`, `sourceElement.closest()`
- 参照: `sourceElement.id`

## openFxAEmailFirstPage()
- 位置: async L2841-2851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.canConnectAccount()`, `FxAccounts.config.promiseConnectAccountURI()`, `switchToTabHavingURI()`

## openFxAEmailFirstPageFromFxaMenu()
- 位置: async L2853-2859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openFxAEmailFirstPage()`

## openFxAManagePage()
- 位置: async L2861-2864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config.promiseManageURI()`, `switchToTabHavingURI()`

## _openFxAManagePageFromElement()
- 位置: async L2866-2869
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openFxAManagePage()`

## sendTabToDevice()
- 位置: async L2872-2922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/login-manager/crypto/SDR;1"].getService()`, `fxAccounts.commands.sendTab.isDeviceCompatible()`
- 条件付き依存: `if (fxAccounts.commands.sendTab.isDeviceCompatible(target))` → `fxaCommandsDevices.push()`
- 条件付き依存: `if (!(fxAccounts.commands.sendTab.isDeviceCompatible(target)))` → `this.log.error()`
- 条件付き依存: `if (cryptoSDR.uiBusy)` → `this.log.info()`
- 条件付き依存: `if (!cryptoSDR.isLoggedIn)` → `cryptoSDR.encrypt()`
- 条件付き依存: `if (!cryptoSDR.isLoggedIn)` → `this.log.info()`
- 条件付き依存: `if (fxaCommandsDevices.length)` → `this.log.info()`
- 条件付き依存: `if (fxaCommandsDevices.length)` → `fxaCommandsDevices .map(d => d.id) .join()`
- 条件付き依存: `if (fxaCommandsDevices.length)` → `fxaCommandsDevices .map()`
- 条件付き依存: `if (fxaCommandsDevices.length)` → `fxAccounts.commands.sendTab.send()`
- 条件付き依存: `if (fxaCommandsDevices.length)` → `this.log.error()`
- 参照: `Ci.nsILoginManagerCrypto`, `cryptoSDR.isLoggedIn`, `cryptoSDR.uiBusy`, `d.id`, `device.id`, `fxaCommandsDevices.length`, `report.failed`, `target.id`, `targets.length`
- XPCOM: [`nsILoginManagerCrypto`](../../../toolkit/components/passwordmgr/nsILoginManagerCrypto.idl.md) / `@mozilla.org/login-manager/crypto/SDR;1` → `LoginManagerCrypto_SDR` (toolkit/components/passwordmgr/components.conf)

## sendTabsAndConfirm()
- 位置: async L2933-2954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `fxAccounts.flushLogFile()`, `results.includes()`, `tabsToSend.map()`, `this.sendTabToDevice()`
- 条件付き依存: `if (results.includes(true))` → `document.documentElement.getAttribute()`
- 条件付き依存: `if (results.includes(true))` → `document.getElementById()`
- 条件付き依存: `if (results.includes(true))` → `ConfirmationHint.show()`
- 参照: `document.getElementById("fxa-toolbar-menu-button")?.parentNode?.id`

## populateSendTabToDevicesMenu()
- 位置: L2956-3042
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `UIState.get()`, `child.classList.contains()`, `devicesPopup.appendChild()`, `document.createDocumentFragment()`, `document.createXULElement()`, `this.refreshFxaDevices()`
- 条件付き依存: `if (!uri)` → `this.log.error()`
- 条件付き依存: `if (child.classList.contains("sync-menuitem"))` → `child.remove()`
- 条件付き依存: `if (this.isSignedInWithSyncDisabled)` → `this._appendSignedInSyncDisabled()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `this.getSendTabTargets()`
- 条件付き依存: `if (targets.length)` → `this._appendSendTabDeviceList()`
- 条件付き依存: `if (contextMenuType)` → `this._recordSendTabTelemetry()`
- 条件付き依存: `if (!(targets.length))` → `this._appendSendTabSingleDevice()`
- 条件付き依存: `if ( state.status == UIState.STATUS_NOT_VERIFIED || state.status == UIState.STATUS_LOGIN_FAILED )` → `this._appendSendTabVerify()`
- 条件付き依存: `if (!( state.status == UIState.STATUS_NOT_VERIFIED || state.status == UIState.STATUS_LOGIN_FAILED ))` → `this._appendSendTabSignedOut()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`, `devicesPopup.children`, `devicesPopup.children.length`, `gSync.sendTabConfiguredAndLoading`, `state.status`, `targets.length`, `this.isSignedInWithSyncDisabled`, `uri.spec`

## _appendSendTabDeviceList()
- 位置: L3044-3167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isBrowserPrivate()`, `addTargetDevice()`, `gBrowser.selectedTabs.map()`, `this.getTargetClientType()`
- 条件付き依存: `if (targets.length > 1)` → `createDeviceNodeFn()`
- 条件付き依存: `if (targets.length > 1)` → `separator.classList.add()`
- 条件付き依存: `if (targets.length > 1)` → `fragment.appendChild()`
- 条件付き依存: `if (targets.length > 1)` → `this.fluentStrings.formatValuesSync()`
- 条件付き依存: `if (targets.length > 1)` → `addTargetDevice()`
- 条件付き依存: `if (targets.length > 1)` → `targetDevice.addEventListener()`
- 条件付き依存: `if (targets.length > 1)` → `gSync.openDevicesManagementPage()`
- 条件付き依存: `if (contextMenuType)` → `this._recordSendTabTelemetry()`
- 条件付き依存: `if (targets.length > 1)` → `targetDevice.classList.add()`
- 条件付き依存: `if (targets.length > 1)` → `targetDevice.setAttribute()`
- 参照: `t.linkedBrowser.contentTitle`, `t.linkedBrowser.currentURI.spec`, `target.clientRecord`, `target.clientRecord.serverLastModified`, `target.id`, `target.lastAccessTime`, `target.name`, `targets.length`

## send()
- 位置: L3065-3065
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendTabsAndConfirm()`

## onSendAllCommand()
- 位置: L3066-3076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `send()`
- 条件付き依存: `if (contextMenuType)` → `this._recordSendTabTelemetry()`
- 参照: `targets.length`

## onTargetDeviceCommand()
- 位置: L3077-3089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `send()`, `targets.find()`
- 条件付き依存: `if (contextMenuType)` → `this._recordSendTabTelemetry()`
- 参照: `t.id`, `targets.length`

## addTargetDevice()
- 位置: L3091-3108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createDeviceNodeFn()`, `fragment.appendChild()`, `targetDevice.addEventListener()`, `targetDevice.classList.add()`, `targetDevice.setAttribute()`

## _resetSendTabExposureTracking()
- 位置: L3169-3171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendTabExposureRecorded.clear()`

## _recordSendTabTelemetry()
- 位置: L3173-3217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean[category][method].record()`, `String()`
- 条件付き依存: `if ( !category || !method || (category == "sendTabToolbar" && method == "sendTabExposed") )` → `this.log.error()`
- 参照: `extraParams.action`, `extraParams.context_type`

## _appendSignedInSyncDisabled()
- 位置: L3219-3244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createDeviceNodeFn()`, `enableSyncMenuItem.addEventListener()`, `enableSyncMenuItem.classList.add()`, `enableSyncMenuItem.setAttribute()`, `fragment.appendChild()`, `this.enableSync()`
- 条件付き依存: `if (contextMenuType == "link")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (contextMenuType == "page")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(contextMenuType == "page"))` → `this.fluentStrings.formatValueSync()`

## _appendSendTabSingleDevice()
- 位置: L3246-3311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config.promisePairingURI()`, `connectPhoneMenuItem.addEventListener()`, `connectPhoneMenuItem.classList.add()`, `connectPhoneMenuItem.setAttribute()`, `createDeviceNodeFn()`, `deviceMissingMenuItem.addEventListener()`, `deviceMissingMenuItem.classList.add()`, `deviceMissingMenuItem.setAttribute()`, `fragment.appendChild()`, `separator.classList.add()`, `switchToTabHavingURI()`, `this.openSendTabHelp()`
- 条件付き依存: `if (contextMenuType == "link")` → `this.fluentStrings.formatValuesSync()`
- 条件付き依存: `if (contextMenuType == "page")` → `this.fluentStrings.formatValuesSync()`
- 条件付き依存: `if (!(contextMenuType == "page"))` → `this.fluentStrings.formatValuesSync()`

## _appendSendTabVerify()
- 位置: L3313-3327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._appendSendTabInfoItems()`, `this.fluentStrings.formatValuesSync()`

## command()
- 位置: L3319-3319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openPrefs()`

## _appendSendTabInfoItems()
- 位置: L3329-3347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionItem.addEventListener()`, `actionItem.classList.add()`, `actionItem.setAttribute()`, `createDeviceNodeFn()`, `fragment.appendChild()`, `separator.classList.add()`, `status.classList.add()`, `status.setAttribute()`

## _appendSendTabSignedOut()
- 位置: L3349-3381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createDeviceNodeFn()`, `fragment.appendChild()`, `signInMenuItem.addEventListener()`, `signInMenuItem.classList.add()`, `signInMenuItem.setAttribute()`, `this.openSignInAgainPage()`
- 条件付き依存: `if (contextMenuType == "link")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (contextMenuType == "page")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(contextMenuType == "page"))` → `this.fluentStrings.formatValueSync()`

## updateTabContextMenu()
- 位置: L3384-3449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `document.getElementById()`, `this.init()`, `this.shouldHideSendContextMenuItems()`
- 条件付き依存: `if (!(hideItems || !hasASendableURI))` → `this.hasOnlyMobileSendTabTargets()`
- 条件付き依存: `if (this.hasOnlyMobileSendTabTargets())` → `sendTabsToDevice.setAttribute()`
- 条件付き依存: `if (!(this.hasOnlyMobileSendTabTargets()))` → `sendTabsToDevice.setAttribute()`
- 条件付き依存: `if (!(hideItems || !hasASendableURI))` → `sendTabsToDevice.setAttribute()`
- 条件付き依存: `if (!(hideItems || !hasASendableURI))` → `JSON.stringify()`
- 条件付き依存: `if (enabled)` → `this.getSendTabTargets()`
- 条件付き依存: `if (enabled)` → `this._sendTabExposureRecorded.has()`
- 条件付き依存: `if (targets.length && !this._sendTabExposureRecorded.has(exposureKey))` → `this._recordSendTabTelemetry()`
- 条件付き依存: `if (targets.length && !this._sendTabExposureRecorded.has(exposureKey))` → `this._sendTabExposureRecorded.add()`
- 参照: `aTargetTab.multiselected`, `gBrowser.multiSelectedTabsCount`, `gBrowser.selectedTabs`, `sendTabToDeviceSeparator.hidden`, `sendTabsToDevice.disabled`, `sendTabsToDevice.hidden`, `tab.linkedBrowser.currentURI`, `targets.length`, `this.FXA_ENABLED`, `this.sendTabConfiguredAndLoading`

## updateContentContextMenu()
- 位置: L3452-3534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `contextMenu.getLinkURI()`, `contextMenu.setItemAttr()`, `contextMenu.showItem()`, `document.getElementById()`, `sendLinkToDevice.setAttribute()`, `sendPageToDevice.setAttribute()`, `this.hasOnlyMobileSendTabTargets()`, `this.shouldHideSendContextMenuItems()`
- 条件付き依存: `if (!hideItems && enabled)` → `this.getSendTabTargets()`
- 条件付き依存: `if (!hideItems && enabled)` → `this._sendTabExposureRecorded.has()`
- 条件付き依存: `if (targets.length && !this._sendTabExposureRecorded.has(exposureKey))` → `this._recordSendTabTelemetry()`
- 条件付き依存: `if (targets.length && !this._sendTabExposureRecorded.has(exposureKey))` → `this._sendTabExposureRecorded.add()`
- 参照: `contextMenu.browser.currentURI`, `contextMenu.isContentSelected`, `contextMenu.onAudio`, `contextMenu.onCanvas`, `contextMenu.onImage`, `contextMenu.onLink`, `contextMenu.onPlainTextLink`, `contextMenu.onSaveableLink`, `contextMenu.onTextInput`, `contextMenu.onVideo`, `targets.length`, `this.FXA_ENABLED`, `this.sendTabConfiguredAndLoading`

## onActivityStart()
- 位置: L3537-3559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `clearTimeout()`, `document .getElementById()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll(".syncNowBtn") .forEach()`, `document.l10n.setAttributes()`, `document.querySelectorAll()`, `document.querySelectorAll(".syncNowBtn").forEach()`, `document.querySelectorAll(".syncnow-label").forEach()`, `el.getAttribute()`, `el.setAttribute()`, `this._updateSecureSyncNowLabel()`
- 参照: `this._isCurrentlySyncing`, `this._syncAnimationTimer`, `this._syncStartTime`

## _onActivityStop()
- 位置: L3561-3586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `document .getElementById()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll(".syncNowBtn") .forEach()`, `document.l10n.setAttributes()`, `document.querySelectorAll()`, `document.querySelectorAll(".syncNowBtn").forEach()`, `document.querySelectorAll(".syncnow-label").forEach()`, `el.getAttribute()`, `el.removeAttribute()`, `this._updateSecureSyncNowLabel()`
- 参照: `this._isCurrentlySyncing`
- XPCOM: `Services.obs`

## onActivityStop()
- 位置: L3588-3602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (syncDuration < MIN_STATUS_ANIMATION_DURATION)` → `clearTimeout()`
- 条件付き依存: `if (syncDuration < MIN_STATUS_ANIMATION_DURATION)` → `setTimeout()`
- 条件付き依存: `if (syncDuration < MIN_STATUS_ANIMATION_DURATION)` → `this._onActivityStop()`
- 条件付き依存: `if (!(syncDuration < MIN_STATUS_ANIMATION_DURATION))` → `this._onActivityStop()`
- 参照: `this._syncAnimationTimer`, `this._syncStartTime`

## disconnect()
- 位置: async L3607-3624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._confirmSyncDisconnect()`, `this._disconnectSync()`
- 条件付き依存: `if (confirm)` → `this._confirmFxaAndSyncDisconnect()`
- 条件付き依存: `if (disconnectAccount)` → `this._disconnectFxaAndSync()`
- 参照: `options.deleteLocalData`, `options.userConfirmedDisconnect`

## _confirmFxaAndSyncDisconnect()
- 位置: async L3628-3670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AIWindow.hasActiveAIWindows()`, `Services.prompt.asyncConfirmEx()`, `UIState.get()`, `document.l10n.formatValues()`, `propBag.get()`, `result.QueryInterface()`
- 参照: `Ci.nsIPropertyBag2`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_INTERNAL_WINDOW`, `UIState.get().syncEnabled`, `options.deleteLocalData`, `options.userConfirmedDisconnect`, `window.browsingContext`
- XPCOM: [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.prompt`

## _disconnectFxaAndSync()
- 位置: async L3672-3687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `SyncDisconnect.disconnect()`, `SyncDisconnect.disconnect(deleteLocalData).catch()`, `console.error()`, `fxAccounts.telemetry.recordDisconnection()`
- 参照: `this._attachedClients`

## _confirmSyncDisconnect()
- 位置: async L3691-3715
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmEx()`, `document.l10n.formatValues()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`
- XPCOM: `Services.prompt`

## _disconnectSync()
- 位置: async L3717-3724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Weave.Service.startOver()`, `fxAccounts.telemetry.recordDisconnection()`
- 参照: `Weave.Service.promiseInitialized`

## doSync()
- 位置: L3728-3747
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `UIState.isReady()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `this.updateSyncStatus()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `fxAccounts.commands.pollDeviceCommands().catch()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `fxAccounts.commands.pollDeviceCommands()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `this.log.error()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `Weave.Service.sync()`
- 参照: `UIState.STATUS_SIGNED_IN`, `state.status`
- XPCOM: `Services.tm`

## doSyncFromFxaMenu()
- 位置: L3749-3752
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.doSync()`, `this.emitFxaToolbarTelemetry()`

## openPrefs()
- 位置: L3754-3759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.openPreferences()`

## openPrefsFromFxaMenu()
- 位置: L3761-3765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openPrefs()`

## openChooseWhatToSync()
- 位置: L3767-3771
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openPrefs()`

## openSyncSetup()
- 位置: L3773-3777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openSyncSetupForEntryPoint()`

## openSyncSetupForEntryPoint()
- 位置: async L3785-3805
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fxAccounts.keys.hasKeysForScope()`, `this.log.error()`, `this.openPrefs()`
- 条件付き依存: `if (hasKeys)` → `this.openPrefs()`
- 条件付き依存: `if (!(hasKeys))` → `FxAccounts.canConnectAccount()`
- 条件付き依存: `if (!(hasKeys))` → `FxAccounts.config.promiseSetPasswordURI()`
- 条件付き依存: `if (!(hasKeys))` → `switchToTabHavingURI()`

## signInToSync()
- 位置: async L3807-3818
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config.promiseConnectAccountURI()`, `switchToTabHavingURI()`, `this._getEntryPointForElement()`

## enableSync()
- 位置: L3820-3822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openTrustedLinkIn()`

## openPairDevice()
- 位置: async L3824-3835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config.promisePairingURI()`, `switchToTabHavingURI()`
- 条件付き依存: `if (!entryPoint)` → `this._getEntryPointForElement()`

## verifyAccount()
- 位置: async L3837-3839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openTrustedLinkIn()`

## openSendTabHelp()
- 位置: L3841-3846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `switchToTabHavingURI()`
- XPCOM: `Services.urlFormatter`

## openDeviceMissingHelp()
- 位置: L3848-3854
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `switchToTabHavingURI()`

## openGetFirefoxMobile()
- 位置: L3856-3864
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `switchToTabHavingURI()`

## openSyncedTabsPanel()
- 位置: L3866-3886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `document.getElementById()`
- 条件付き依存: `if (area == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `document.getElementById()`
- 条件付き依存: `if (area == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `navbar.overflowable.show().then()`
- 条件付き依存: `if (area == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `navbar.overflowable.show()`
- 条件付き依存: `if (area == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `PanelUI.showSubView()`
- 条件付き依存: `if (!(area == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL))` → `anchor?.checkVisibility()`
- 条件付き依存: `if ( !anchor?.checkVisibility({ checkVisibilityCSS: true, flush: false }) )` → `document.getElementById()`
- 条件付き依存: `if (!(area == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL))` → `PanelUI.showSubView()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.AREA_NAVBAR`, `console.error`, `placement?.area`

## refreshSyncButtonsTooltip()
- 位置: L3888-3891
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UIState.get()`, `this.updateSyncButtonsTooltip()`

## updateSyncButtonsTooltip()
- 位置: L3898-3934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`, `this.fluentStrings.formatValueSync()`, `this.formatLastSyncDate()`
- 条件付き依存: `if (tooltiptext)` → `el.setAttribute()`
- 条件付き依存: `if (!(tooltiptext))` → `el.removeAttribute()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `state.email`, `state.lastSync`, `state.status`

## relativeTimeFormat()
- 位置: L3936-3942
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.intl.RelativeTimeFormat`, `this.relativeTimeFormat`
- XPCOM: `Services.intl`

## formatLastSyncDate()
- 位置: L3944-3961
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.log.warn()`, `this.relativeTimeFormat.formatBestUnit()`

## onClientsSynced()
- 位置: L3963-3976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelMultiView.getViewNode()`
- 条件付き依存: `if (Weave.Service.clientsEngine.stats.numClients > 1)` → `element.setAttribute()`
- 条件付き依存: `if (!(Weave.Service.clientsEngine.stats.numClients > 1))` → `element.setAttribute()`
- 参照: `Weave.Service.clientsEngine.stats.numClients`

## onFxaDisabled()
- 位置: L3978-3989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.setAttribute()`, `document.querySelectorAll()`
- 参照: `item.hidden`

## hasClientForId()
- 位置: L4000-4002
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._attachedClients?.some()`
- 参照: `c.id`

## updateCTAPanel()
- 位置: L4004-4101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.shouldShowPromo()`, `PanelMultiView.getViewNode()`, `Services.prefs.getBoolPref()`, `this.hasClientForId()`, `this.updateCTAButtonStrings()`
- 参照: `BrowserUtils.PromoType.RELAY`, `BrowserUtils.PromoType.VPN`, `VpnPanelEl.hidden`, `anchor.id`, `mainPanelEl.hidden`, `monitorPanelEl.hidden`, `privacyToolsSeparatorEl.hidden`, `relayPanelEl.hidden`, `shareFirefoxPanelEl.hidden`, `this.FXA_CTA_MENU_ENABLED`, `this.isSignedIn`
- XPCOM: `Services.prefs`

## updateCTAButtonStrings()
- 位置: L4121-4132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttonEl.querySelector()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (!inUse)` → `document.l10n.setAttributes()`
- 参照: `descriptionEl.hidden`

## openMonitorLink()
- 位置: L4134-4141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ctaURL()`, `this.emitFxaToolbarTelemetry()`, `this.openCtaLink()`

## openRelayLink()
- 位置: L4143-4150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ctaURL()`, `this.emitFxaToolbarTelemetry()`, `this.openCtaLink()`

## openVPNLink()
- 位置: L4152-4159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._ctaURL()`, `this.emitFxaToolbarTelemetry()`, `this.openCtaLink()`

## openShareFirefoxLink()
- 位置: L4161-4164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelUI.hide()`, `Referrals.openReferralsTab()`

## _ctaURL()
- 位置: L4175-4182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `url.searchParams.set()`

## openCtaLink()
- 位置: L4194-4202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelUI.hide()`, `this.hasClientForId()`, `this.openLink()`
- 参照: `this.isSignedIn`

## getMenuCtaCopy()
- 位置: L4236-4287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feature.getVariable()`, `this.fluentStrings.formatValueSync()`
- 参照: `NimbusFeatures.fxaAppMenuItem`

## applyAvatarIconVariant()
- 位置: L4297-4305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ICON_VARIANTS.includes()`, `document.documentElement.setAttribute()`

## openLink()
- 位置: L4307-4309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `switchToTabHavingURI()`

## sendTabToolbarButtonShouldBeEnabled()
- 位置: L4311-4326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`, `this.init()`
- 参照: `this.FXA_ENABLED`, `this.sendTabConfiguredAndLoading`

## populateSendTabToolbarButton()
- 位置: async L4328-4335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.populateSendTabToDevicesMenu()`
- 参照: `menuPopup.documentGlobal.gBrowser.contentTitle`, `menuPopup.documentGlobal.gBrowser.currentURI`
