# browser/base/content/browser-sync.js

source: browser/base/content/browser-sync.js
source-hash: 8631d88912fb55054ac9484b7ef283621e9c1ba5
lines: 4342

## <module>
- 役割: Firefox アカウント(FxA)と Sync の UI(アプリメニュー、アカウントボタン、同期済みタブの一覧、タブ送信)を組み立て、表示状態と操作を制御するファイル。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`

## SyncedTabsPanelList.constructor()
- 位置: L72-85
- 役割: 同期タブの一覧パネルを作り、TOPIC_TABS_CHANGED を監視してから createSyncedTabs で初期表示を行う。
- 触るとき: 同期タブ一覧を開いた時の初期状態や、更新通知の登録を変えるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.resolve()`, `Services.obs.addObserver()`, `this.createSyncedTabs()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this.QueryInterface`, `this._showSyncedTabsPromise`, `this.deck`, `this.separator`, `this.tabsList`
- XPCOM: `Services.obs`

## SyncedTabsPanelList.observe()
- 位置: L87-91
- 役割: 同期タブが変わったという通知を受けて、_showSyncedTabs で一覧を描き直す。
- 触るとき: 同期タブの更新が一覧に反映されないと感じたとき。
- 条件付き依存: `if (topic == SyncedTabs.TOPIC_TABS_CHANGED)` → `this._showSyncedTabs()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`

## SyncedTabsPanelList.createSyncedTabs()
- 位置: L93-122
- 役割: 同期設定の有無と同期済みかどうかで deck の表示を決め、同期済みなら SyncedTabs.syncTabs() を呼んで一覧を出す。未同期なら取得中の表示、無効なら無効表示にして区切り線を隠す。
- 触るとき: パネルを開いた直後に出る「取得中」「一覧」「無効」の表示条件を変えるとき。
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs().catch()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `console.error()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `this.deck.toggleAttribute()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `this._showSyncedTabs()`
- 条件付き依存: `if (!(SyncedTabs.isConfiguredToSyncTabs))` → `this.deck.toggleAttribute()`
- 参照: `SyncedTabs.hasSyncedThisSession`, `SyncedTabs.isConfiguredToSyncTabs`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_FETCHING`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_TABS`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_TABSDISABLED`, `this.deck.selectedIndex`, `this.separator`, `this.separator.hidden`

## SyncedTabsPanelList._showSyncedTabs()
- 位置: L125-134
- 役割: 直前の描画 Promise の後ろに __showSyncedTabs をつなぎ、描画が重ならないよう直列化する。
- 触るとき: 一覧の描画が競合する、または続きの読み込み(ページング)を呼び出すとき。
- 呼び出し先: `console.error()`, `this.__showSyncedTabs()`, `this._showSyncedTabsPromise.then()`
- 参照: `this._showSyncedTabsPromise`

## SyncedTabsPanelList.__showSyncedTabs()
- 位置: L137-210
- 役割: SyncedTabs.getTabClients() でクライアント一覧を取り、クライアントごとにラベル付きのコンテナを作って _appendSyncClient で中身を入れる。0 件なら状態に応じて deck を切り替え、最後にテスト用の通知を出す。
- 触るとき: 同期タブ一覧の構成や、クライアントが無いときの表示を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `SyncedTabs.getTabClients()`, `SyncedTabs.getTabClients() .then()`, `SyncedTabs.sortTabClientsByLastUsed()`, `UIState.get()`, `console.error()`, `container.classList.add()`, `container.setAttribute()`, `document.createDocumentFragment()`, `document.createXULElement()`, `fragment.appendChild()`, `this._appendSyncClient()`, `this._clearSyncedTabList()`, `this.deck.toggleAttribute()`, `this.tabsList.appendChild()`
- 条件付き依存: `if (fragment.lastElementChild)` → `document.createXULElement()`
- 条件付き依存: `if (fragment.lastElementChild)` → `fragment.appendChild()`
- 参照: `SyncedTabs.hasSyncedThisSession`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_NOCLIENTS`, `SyncedTabsPanelList.sRemoteTabsDeckIndices.DECKINDEX_TABS`, `UIState.get().syncEnabled`, `client.id`, `clients.length`, `fragment.lastElementChild`, `paginationInfo.clientId`, `this.deck.selectedIndex`, `this.separator`, `this.separator.hidden`, `this.tabsList`
- XPCOM: `Services.obs`

## SyncedTabsPanelList._clearSyncedTabList()
- 位置: L212-217
- 役割: tabsList の子要素をすべて取り除く。
- 触るとき: 一覧を描き直す前の掃除に問題があるとき。
- 呼び出し先: `list.lastChild.remove()`
- 参照: `list.lastChild`, `this.tabsList`

## SyncedTabsPanelList._createNoSyncedTabsElement()
- 位置: L219-231
- 役割: 属性で指定された Fluent 文言を持つ label を作り、tabsList か指定の親に追加する。
- 触るとき: 「タブがありません」などの案内文を出す箇所を増やすとき。
- 呼び出し先: `appendTo.appendChild()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `this.tabsList.getAttribute()`
- 参照: `this.tabsList`

## SyncedTabsPanelList._appendSyncClient()
- 位置: L233-304
- 役割: クライアント名の見出しを作り、タブが無ければ案内文を、あれば FxA デバイスを解決して非アクティブでないタブを maxTabs 件まで並べる。必要に応じて非アクティブ表示と「もっと見る」ボタンを付ける。
- 触るとき: 1 台分の同期タブの件数(25 件、最低 5 件の差)や、閉じる操作の可否を変えるとき。
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
- 役割: 「もっと見る」ボタンを作り、クリックすると maxTabs を無制限にして一覧を描き直す。
- 触るとき: 同期タブの続きの読み込み方を変えるとき。
- 呼び出し先: `document.createXULElement()`, `document.l10n.setAttributes()`, `e.preventDefault()`, `e.stopPropagation()`, `showMoreItem.addEventListener()`, `showMoreItem.classList.add()`, `showMoreItem.setAttribute()`, `this._showSyncedTabs()`
- 参照: `paginationInfo.maxTabs`

## SyncedTabsPanelList._createShowInactiveTabsElement()
- 位置: L322-357
- 役割: 「非アクティブなタブを表示」ボタンを作る。クリックで該当端末の非アクティブなタブだけをサブビューに並べて表示する。
- 触るとき: 非アクティブなタブの見せ方を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `client.tabs .filter()`, `client.tabs .filter(t => t.inactive) .map()`, `container.replaceChildren()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `fxAccounts.commands.closeTab.isDeviceCompatible()`, `node.querySelector()`, `showItem.addEventListener()`, `showItem.classList.add()`, `showItem.setAttribute()`, `this._createSyncedTabElement()`
- 参照: `client.name`, `label.textContent`, `t.inactive`

## SyncedTabsPanelList._createSyncedTabElement()
- 位置: L359-416
- 役割: タブ 1 行分の toolbaritem を作る。クリックで openUILink によりタブを開き、テレメトリを記録する。端末が閉じる操作に対応していれば閉じる・元に戻すボタンも付ける。
- 触るとき: 同期タブをクリックしたときの開き方やテレメトリを変えるとき。
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
- 役割: リモートのタブを閉じるボタンを作る。クリックで他の行の閉じる操作の残りを片付け、このボタンを隠して元に戻すボタンを出し、タブを無効化して閉じ要求を SyncedTabsManagement のキューに積む。
- 触るとき: リモートタブを閉じる操作の見た目や、閉じ要求を送るタイミングを変えるとき。
- 呼び出し先: `SyncedTabsManagement.enqueueTabToClose()`, `closeBtn.addEventListener()`, `closeBtn.classList.add()`, `closeBtn.setAttribute()`, `document.createXULElement()`, `e.stopPropagation()`, `gSync.fluentStrings.formatValueSync()`, `tabContainer.querySelector()`, `tabList.querySelector()`
- 条件付き依存: `if (prevClose)` → `prevCloseContainer.classList.add()`
- 条件付き依存: `if (prevClose)` → `prevCloseContainer.addEventListener()`
- 条件付き依存: `if (prevClose)` → `prevCloseContainer.remove()`
- 参照: `closeBtn.hidden`, `closeBtn.parentNode`, `closeBtn.tab`, `closeBtn.tab.disabled`, `device.id`, `device.name`, `prevClose.parentNode`, `tabContainer.parentNode`, `undoBtn.hidden`

## SyncedTabsPanelList._createUndoCloseTabElement()
- 位置: L465-486
- 役割: 閉じるの取り消しボタンを作る。クリックで閉じるボタンを戻し、タブの無効化を解き、保留中の閉じ要求から外す。
- 触るとき: 閉じる操作の取り消しが効かない問題を調べるとき。
- 呼び出し先: `SyncedTabsManagement.removePendingTabToClose()`, `document.createXULElement()`, `e.stopPropagation()`, `undoBtn.addEventListener()`, `undoBtn.classList.add()`, `undoBtn.parentNode.querySelector()`, `undoBtn.setAttribute()`
- 参照: `closeBtn.hidden`, `device.id`, `undoBtn.hidden`, `undoBtn.tab`, `undoBtn.tab.disabled`

## SyncedTabsPanelList.destroy()
- 位置: L488-493
- 役割: TOPIC_TABS_CHANGED の購読を外し、tabsList・deck・separator への参照を null にする。
- 触るとき: パネルを閉じた後に古い参照へ更新が走らないか確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this.deck`, `this.separator`, `this.tabsList`
- XPCOM: `Services.obs`

## FxAMenuDeviceList.constructor()
- 位置: L503-520
- 役割: devicesList を受け取って TOPIC_TABS_CHANGED を購読し、_initDeviceList で一覧を作ってから gSync.refreshFxaDevices で FxA の端末一覧を更新する。
- 触るとき: FxA メニューを開いたときの端末一覧の初期化順序を変えるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.resolve()`, `Services.obs.addObserver()`, `gSync.refreshFxaDevices()`, `this._initDeviceList()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this.QueryInterface`, `this._removalTimers`, `this._updateDevicesPromise`, `this.devicesList`
- XPCOM: `Services.obs`

## FxAMenuDeviceList.observe()
- 位置: L522-526
- 役割: 同期タブの変化を受けて _updateDeviceList を呼ぶ。
- 触るとき: 同期タブの変化がメニューの端末一覧に反映されない問題を調べるとき。
- 条件付き依存: `if (topic == SyncedTabs.TOPIC_TABS_CHANGED)` → `this._updateDeviceList()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`

## FxAMenuDeviceList._initDeviceList()
- 位置: L528-535
- 役割: 同期タブ設定が有効なら SyncedTabs.syncTabs() を起動し、そのあと _updateDeviceList を呼ぶ。
- 触るとき: メニューを開いたときに強制同期を行うかどうかを変えるとき。
- 呼び出し先: `this._updateDeviceList()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs().catch()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `SyncedTabs.syncTabs()`
- 条件付き依存: `if (SyncedTabs.isConfiguredToSyncTabs)` → `console.error()`
- 参照: `SyncedTabs.isConfiguredToSyncTabs`

## FxAMenuDeviceList._updateDeviceList()
- 位置: L537-542
- 役割: _doUpdateDeviceList を前回の処理の後に直列で実行する。
- 触るとき: 端末一覧の更新が競合して古い表示が残る問題を調べるとき。
- 呼び出し先: `console.error()`, `this._doUpdateDeviceList()`, `this._updateDevicesPromise.then()`
- 参照: `this._updateDevicesPromise`

## FxAMenuDeviceList._doUpdateDeviceList()
- 位置: async L544-606
- 役割: 統合済みの端末一覧を取り、同期が無効か 0 件なら一覧を隠す。アプリメニューでは端末ごとにセクションを並べ、アカウントメニューでは先頭 MAX_DEVICES 件を並べ、残りは「すべてのデバイス」ボタンへ回す。
- 触るとき: メニューに出す端末の数や並び、アプリメニューとアカウントメニューの違いを変えるとき。
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
- 役割: Sync クライアント ID を FxA デバイス ID に変換して、FxA の recentDeviceList から該当の端末を探す。変換できなければクライアント ID をそのまま使う。
- 触るとき: 同期クライアントと FxA 端末の対応付けがずれる問題を調べるとき。
- 呼び出し先: `Weave.Service.clientsEngine.getClientFxaDeviceId()`, `devices.find()`
- 参照: `client.id`, `d.id`, `fxAccounts.device.recentDeviceList`

## FxAMenuDeviceList._getMergedDeviceList()
- 位置: async L637-683
- 役割: Sync クライアントと FxA の recentDeviceList を突き合わせる。タブ送信ができるだけの端末には空タブの代用クライアントを作って加え、対応の無いクライアントは末尾に残す。現在の端末は除く。
- 触るとき: メニューに出る端末の条件を変えるとき、古い端末一覧で端末が欠けて見えるときに確かめる。
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
- 役割: 「すべてのデバイス」ボタンを作り、クリックで _showAllDevices を呼ぶ。
- 触るとき: 端末が多いときの導線を変えるとき。
- 呼び出し先: `btn.addEventListener()`, `btn.classList.add()`, `btn.setAttribute()`, `document.createXULElement()`, `this._showAllDevices()`
- 参照: `btn.id`

## FxAMenuDeviceList._showAllDevices()
- 位置: L697-708
- 役割: 「すべてのデバイス」サブビューの一覧を作り直し、全端末の項目を並べてサブビューを表示する。
- 触るとき: 全端末一覧の中身や表示方法を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `list.appendChild()`, `list.replaceChildren()`, `this._createDeviceEntry()`, `this._getDeviceForClient()`

## FxAMenuDeviceList._getDeviceClientType()
- 位置: L710-721
- 役割: 端末の種別から clientType の値(phone、tablet、desktop)を返す。端末情報が無ければ desktop を返す。
- 触るとき: 端末アイコンの種類の判定を変えるとき。
- 参照: `device.type`

## FxAMenuDeviceList._getTelemetryDeviceType()
- 位置: L723-728
- 役割: 端末がモバイルかタブレットなら mobile、それ以外は desktop を返す。テレメトリ用の値になる。
- 触るとき: 端末種別のテレメトリの値を変えるとき。
- 参照: `device?.type`

## FxAMenuDeviceList._createDeviceEntry()
- 位置: L730-763
- 役割: 端末 1 件のボタンを作る。クリック時に端末情報を解決し直して synced_device_submenu を記録し、その端末の最近のタブを表示する。
- 触るとき: 端末をクリックしたときの動作や計測を変えるとき。
- 呼び出し先: `String()`, `btn.addEventListener()`, `btn.classList.add()`, `btn.setAttribute()`, `document.createXULElement()`, `gSync.emitFxaToolbarTelemetry()`, `gSync.fluentStrings.formatValueSync()`, `gSync.formatLastSyncDate()`, `gSync.getSendTabTargets()`, `this._getDeviceClientType()`, `this._getDeviceForClient()`, `this._getTelemetryDeviceType()`, `this._showDeviceRecentTabs()`
- 参照: `client.lastModified`, `client.name`, `gSync.getSendTabTargets().length`

## FxAMenuDeviceList._getRecentTabs()
- 位置: L765-769
- 役割: 非アクティブでないタブを先頭から MAX_RECENT_TABS 件まで返す。
- 触るとき: メニューに出す最近のタブの件数や条件を変えるとき。
- 呼び出し先: `client.tabs .filter()`, `client.tabs .filter(t => !t.inactive) .slice()`
- 参照: `FxAMenuDeviceList.MAX_RECENT_TABS`, `t.inactive`

## FxAMenuDeviceList._populateRecentTabs()
- 位置: L775-795
- 役割: 最近のタブごとに行を作って tabsList に追加する。閉じる・元に戻すボタンは端末が閉じ操作に対応しているときだけ付け、行の描画を強制する。
- 触るとき: 最近のタブの行の構成や、閉じ操作の出し分けを変えるとき。
- 呼び出し先: `fxAccounts.commands.closeTab.isDeviceCompatible()`, `item.render()`, `recentTabs.entries()`, `tabContainer.querySelector()`, `tabsList.appendChild()`, `this._createSyncedTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `this._createCloseTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `this._createUndoCloseTabElement()`
- 条件付き依存: `if (canCloseTabs)` → `tabContainer.append()`
- 参照: `closeBtn.tab`, `tab.url`, `undoBtn.tab`

## FxAMenuDeviceList._configureViewAllTabsButton()
- 位置: L797-813
- 役割: 「すべての同期タブを表示」ボタンのラベルをタブ数入りで設定し、クリックで同期タブのサイドバーを開く。
- 触るとき: 全件表示ボタンの文言や挙動を変えるとき。
- 呼び出し先: `gSync.fluentStrings.formatMessagesSync()`, `viewAllBtn.setAttribute()`, `viewAllMessage.attributes?.find()`
- 参照: `attr.name`, `viewAllBtn.onclick`, `viewAllMessage.attributes?.find(attr => attr.name === "label")?.value`

## viewAllBtn.onclick()
- 位置: L808-812
- 役割: 全件表示ボタンのクリック時に、パネルを閉じ、viewTabsSidebar を表示して view_all_synced_tabs を記録する。
- 触るとき: 全件表示ボタンを押した後の遷移やテレメトリを変えるとき。
- 呼び出し先: `CustomizableUI.hidePanelForNode()`, `SidebarController.show()`, `gSync.emitFxaToolbarTelemetry()`

## FxAMenuDeviceList._canSendTabToDevice()
- 位置: L815-821
- 役割: 端末がタブ送信に対応し、現在のブラウザの URI が共有可能な URL なら真を返す。
- 触るとき: 「このページを端末へ送る」ボタンを出す条件を変えるとき。
- 呼び出し先: `BrowserUtils.getShareableURL()`, `fxAccounts.commands.sendTab.isDeviceCompatible()`
- 参照: `gBrowser.selectedBrowser.currentURI`

## FxAMenuDeviceList._configureSendPageButton()
- 位置: L829-861
- 役割: 送信先の数を添えて send_tab_opened と send_tab_exposed を記録し、ボタンに onclick を設定する。
- 触るとき: 端末へのページ送信ボタンの露出計測を変えるとき。
- 呼び出し先: `String()`, `gSync.emitFxaToolbarTelemetry()`, `gSync.getSendTabTargets()`
- 参照: `sendPageBtn.onclick`, `targets.length`

## sendPageBtn.onclick()
- 位置: L837-860
- 役割: send_tab を記録し、パネルを閉じたうえで、複数タブ選択中ならその全タブを、そうでなければ現在のページを sendTabsAndConfirm で端末に送る。
- 触るとき: ページ送信の対象(選択タブか現在のページか)を変えるとき。
- 呼び出し先: `BrowserUtils.getShareableURL()`, `CustomizableUI.hidePanelForNode()`, `PrivateBrowsingUtils.isBrowserPrivate()`, `String()`, `gBrowser.selectedTabs.map()`, `gSync.emitFxaToolbarTelemetry()`, `gSync.sendTabsAndConfirm()`
- 参照: `BrowserUtils.getShareableURL( gBrowser.selectedBrowser.currentURI ).spec`, `gBrowser.selectedBrowser.contentTitle`, `gBrowser.selectedBrowser.currentURI`, `gBrowser.selectedTab.multiselected`, `t.linkedBrowser.contentTitle`, `t.linkedBrowser.currentURI.spec`, `targets.length`

## FxAMenuDeviceList._showDeviceRecentTabs()
- 位置: L863-919
- 役割: 端末ごとの最近のタブのパネルを作り直す。タブ一覧、「タブがありません」、全件表示、送信ボタンの表示を状況に応じて切り替え、閉じた件数に応じて表示を戻す処理を登録してサブビューを開く。
- 触るとき: 端末の最近のタブパネルの表示や、タブを閉じた後の表示の戻り方を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelUI.showSubView()`, `panelNode.querySelector()`, `tabsList.replaceChildren()`, `this._canSendTabToDevice()`, `this._configureViewAllTabsButton()`, `this._getRecentTabs()`, `this._populateRecentTabs()`, `this._trackTabCount()`
- 条件付き依存: `if (remaining)` → `this._configureViewAllTabsButton()`
- 条件付き依存: `if (canSendTab)` → `this._configureSendPageButton()`
- 参照: `client.tabs.length`, `footerSeparator.hidden`, `noTabsLabel.hidden`, `recentTabs.length`, `sendPageBtn.hidden`, `tabsList.hidden`, `viewAllBtn.hidden`

## FxAMenuDeviceList._appendDeviceSection()
- 位置: L926-988
- 役割: アプリメニュー用に、端末名の見出し、最近のタブ(無ければ案内)、全件表示ボタン、送信ボタンを 1 つのセクションとして追加する。
- 触るとき: アプリメニュー内の端末セクションの並びや項目を変えるとき。
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
- 役割: classes を付けた toolbarbutton を作り、closemenu 指定があれば none を設定して、onClick を click に登録する。
- 触るとき: 同期タブ行のボタンに共通の属性やイベントを足すとき。
- 呼び出し先: `btn.addEventListener()`, `btn.classList.add()`, `document.createXULElement()`
- 条件付き依存: `if (closemenu)` → `btn.setAttribute()`

## FxAMenuDeviceList._createSyncedTabElement()
- 位置: L1011-1051
- 役割: 最近のタブ 1 行(toolbaritem と toolbarbutton)を作り、ラベル、画像、ツールチップを設定する。クリックで URL を開き、現在のタブで開いたときだけパネルを閉じる。
- 触るとき: メニューの最近のタブを開くときの挙動を変えるとき。
- 呼び出し先: `BrowserUtils.whereToOpenLink()`, `Services.scriptSecurityManager.createNullPrincipal()`, `SyncedTabs.recordSyncedTabsTelemetry()`, `document.createXULElement()`, `document.defaultView.openUILink()`, `index.toString()`, `item.setAttribute()`, `tabContainer.appendChild()`, `tabContainer.setAttribute()`, `this._createTabToolbarButton()`, `window.gSync._getEntryPointForElement()`
- 条件付き依存: `if (BrowserUtils.whereToOpenLink(e) != "current")` → `e.preventDefault()`
- 条件付き依存: `if (BrowserUtils.whereToOpenLink(e) != "current")` → `e.stopPropagation()`
- 条件付き依存: `if (!(BrowserUtils.whereToOpenLink(e) != "current"))` → `CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (tabInfo.icon)` → `item.setAttribute()`
- 参照: `e.currentTarget`, `tabInfo.icon`, `tabInfo.title`, `tabInfo.url`
- XPCOM: `Services.scriptSecurityManager`

## FxAMenuDeviceList._createCloseTabElement()
- 位置: L1053-1082
- 役割: 閉じるボタンを作る。クリックでこのボタンを隠して元に戻すボタンを出し、タブを無効化して閉じ要求を積み、行を一定時間後に消す予約を入れる。
- 触るとき: 閉じた後に行が消えるまでの流れを変えるとき。
- 呼び出し先: `SyncedTabsManagement.enqueueTabToClose()`, `closeBtn.setAttribute()`, `e.stopPropagation()`, `gSync.fluentStrings.formatValueSync()`, `tabContainer.querySelector()`, `this._createTabToolbarButton()`, `this._scheduleTabRowRemoval()`
- 参照: `closeBtn.hidden`, `closeBtn.parentNode`, `closeBtn.tab`, `closeBtn.tab.disabled`, `device.id`, `device.name`, `undoBtn.hidden`

## FxAMenuDeviceList._createUndoCloseTabElement()
- 位置: L1084-1107
- 役割: 元に戻すボタンを作る。クリックで行の削除予約を取り消し、閉じるボタンを戻し、タブの無効化を解いて保留中の閉じ要求から外す。
- 触るとき: 閉じる操作の取り消しの流れを変えるとき。
- 呼び出し先: `SyncedTabsManagement.removePendingTabToClose()`, `e.stopPropagation()`, `tabContainer.querySelector()`, `this._cancelTabRowRemoval()`, `this._createTabToolbarButton()`, `undoBtn.setAttribute()`
- 参照: `closeBtn.hidden`, `device.id`, `undoBtn.hidden`, `undoBtn.parentNode`, `undoBtn.tab`, `undoBtn.tab.disabled`

## FxAMenuDeviceList._trackTabCount()
- 位置: L1115-1118
- 役割: 一覧に残りのタブ数と、数が変わったときに呼ぶ関数を覚えさせる。
- 触るとき: 行を消した後に見出しや全件表示ボタンを更新する仕組みを追うとき。
- 参照: `tabsList.applyTabCount`, `tabsList.tabCount`

## FxAMenuDeviceList._scheduleTabRowRemoval()
- 位置: L1125-1148
- 役割: TAB_REMOVAL_DELAY_MS(5 秒)後に行をフェードさせ、transitionend で行を消して残りのタブ数を減らし、表示を更新する。タイマーは行と一覧の両方に記録する。
- 触るとき: 閉じたタブの行が消えるまでの猶予時間や残数表示の更新を変えるとき。
- 呼び出し先: `setTimeout()`, `tabContainer.addEventListener()`, `tabContainer.classList.add()`, `tabContainer.remove()`, `this._removalTimers.add()`, `this._removalTimers.delete()`
- 条件付き依存: `if (tabsList.applyTabCount)` → `Math.max()`
- 条件付き依存: `if (tabsList.applyTabCount)` → `tabsList.applyTabCount()`
- 参照: `FxAMenuDeviceList.TAB_REMOVAL_DELAY_MS`, `tabContainer.parentNode`, `tabContainer.removalTimer`, `tabsList.applyTabCount`, `tabsList.tabCount`

## FxAMenuDeviceList._cancelTabRowRemoval()
- 位置: L1150-1154
- 役割: 行に記録された削除タイマーを解除し、一覧の管理からも外す。
- 触るとき: 元に戻す操作で行の削除を止められない問題を調べるとき。
- 呼び出し先: `clearTimeout()`, `this._removalTimers.delete()`
- 参照: `tabContainer.removalTimer`

## FxAMenuDeviceList.destroy()
- 位置: L1156-1163
- 役割: 保留中の行削除タイマーをすべて止め、TOPIC_TABS_CHANGED の購読を外し、devicesList を null にする。
- 触るとき: メニューを閉じた後にタイマーが残らないか確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `clearTimeout()`, `this._removalTimers.clear()`
- 参照: `SyncedTabs.TOPIC_TABS_CHANGED`, `this._removalTimers`, `this.devicesList`
- XPCOM: `Services.obs`

## log()
- 位置: L1211-1221
- 役割: Sync.Browser のロガーを初回だけ取得し、services.sync.log.logger.browser の pref でレベルを管理させて保持する。
- 触るとき: browser-sync のログ出力の設定を変えるとき。
- 条件付き依存: `if (!this._log)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!this._log)` → `Log.repository.getLogger()`
- 条件付き依存: `if (!this._log)` → `syncLog.manageLevelFromPref()`
- 参照: `this._log`

## fluentStrings()
- 位置: L1223-1238
- 役割: 初回アクセス時に必要な Fluent ファイル群を読み込んで Localization を作り、以後その値を使い回す。
- 触るとき: この画面で使う文言ファイルを追加するとき。
- 参照: `this.fluentStrings`

## sendTabConfiguredAndLoading()
- 位置: L1242-1249
- 役割: サインイン済みかつ同期有効で、端末一覧がまだ読み込まれていないときに真を返す。
- 触るとき: 送信先の読み込み中表示を出す条件を変えるとき。
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`, `fxAccounts.device.recentDeviceList`, `state.status`, `state.syncEnabled`

## isSignedIn()
- 位置: L1251-1253
- 役割: UIState の状態がサインイン済みかどうかを返す。
- 触るとき: サインインの有無で分岐を追加するとき。
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`, `UIState.get().status`

## isUnverified()
- 位置: L1255-1257
- 役割: UIState の状態がメール未確認かどうかを返す。
- 触るとき: 未確認アカウントの分岐を確かめるとき。
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_NOT_VERIFIED`, `UIState.get().status`

## isSignedInWithSyncDisabled()
- 位置: L1259-1262
- 役割: サインイン済みだが同期が無効なときに真を返す。
- 触るとき: 同期オフ時の表示の出し分けを変えるとき。
- 呼び出し先: `UIState.get()`
- 参照: `UIState.STATUS_SIGNED_IN`, `state.status`, `state.syncEnabled`

## hasNoSendTabTargets()
- 位置: L1264-1266
- 役割: 送信先の候補が 0 件かどうかを返す。
- 触るとき: 送信先が無いときの案内表示を変えるとき。
- 呼び出し先: `this.getSendTabTargets()`
- 参照: `this.getSendTabTargets().length`

## getSyncPromoState()
- 位置: L1271-1302
- 役割: FxA が無効なら null を返す。未登録と未確認なら signin、同期が無効または必要なエンジンが無効なら turnonsync、他の端末が無ければ connectdevice、それ以外は null を返す。
- 触るとき: 同期の案内を状態ごとにどれにするかを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `UIState.get()`, `devices?.some()`, `requiredEngines.some()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`, `d.isCurrentDevice`, `fxAccounts.device.recentDeviceList`, `state.status`, `state.syncEnabled`, `this.FXA_ENABLED`
- XPCOM: `Services.prefs`

## handleSyncPromoAction()
- 位置: L1307-1319
- 役割: getSyncPromoState の結果に応じて、サインイン画面、同期設定、端末追加のいずれかを開く。
- 触るとき: 同期の案内ボタンの遷移先を変えるとき。
- 呼び出し先: `this.openConnectAnotherDevice()`, `this.openFxAEmailFirstPage()`, `this.openSyncSetupForEntryPoint()`

## shouldHideSendContextMenuItems()
- 位置: L1321-1323
- 役割: 引数が無効、または FxA が無効なら真を返し、送信メニュー項目を隠す判定に使う。
- 触るとき: 右クリックメニューの送信項目の出し分けを変えるとき。
- 参照: `this.FXA_ENABLED`

## getSendTabTargets()
- 位置: L1325-1345
- 役割: サインイン済みで同期が有効で端末一覧があるときだけ、現在の端末以外でタブ送信に対応する端末を、最後の利用が新しい順に返す。
- 触るとき: 送信先の候補を増減させたり並び順を変えたりするとき。
- 呼び出し先: `UIState.get()`, `fxAccounts.commands.sendTab.isDeviceCompatible()`, `targets.sort()`
- 条件付き依存: `if (fxAccounts.commands.sendTab.isDeviceCompatible(d))` → `targets.push()`
- 参照: `UIState.STATUS_SIGNED_IN`, `a.lastAccessTime`, `b.lastAccessTime`, `d.isCurrentDevice`, `fxAccounts.device.recentDeviceList`, `state.status`, `state.syncEnabled`

## getTargetClientType()
- 位置: L1349-1355
- 役割: 送信先が Sync クライアントを持てばその種別を返す。無ければ FxA の mobile を Sync の phone に読み替えた値を返す。
- 触るとき: 送信先のアイコン種別の判定を変えるとき。
- 条件付き依存: `if (target.clientRecord)` → `Weave.Service.clientsEngine.getClientType()`
- 参照: `target.clientRecord`, `target.clientRecord.id`, `target.type`

## hasOnlyMobileSendTabTargets()
- 位置: L1357-1365
- 役割: 送信先が無いか、すべてモバイルかタブレットなら真を返す。
- 触るとき: デスクトップ向けの送信案内を出し分けるとき。
- 呼び出し先: `targets.every()`, `this.getSendTabTargets()`
- 参照: `target.type`, `targets.length`

## _definePrefGetters()
- 位置: L1367-1385
- 役割: FXA_ENABLED、FXA_CTA_MENU_ENABLED、APP_MENU_SIGN_IN_PROMO_DISMISSED を pref から遅延して読む値として定義し、dismiss の変更時にアプリメニューのサインイン案内を更新する。
- 触るとき: 新しい pref をこの画面の表示判定に加えるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `this.updateAppMenuSignInPromo()`

## maybeUpdateUIState()
- 位置: L1387-1401
- 役割: UIState の準備ができていれば、未設定の初期状態ではないか、サインアウト済みの場合に updateAllUI を呼ぶ。
- 触るとき: 起動時の再描画を省く条件を変えるとき。
- 呼び出し先: `UIState.isReady()`
- 条件付き依存: `if (UIState.isReady())` → `UIState.get()`
- 条件付き依存: `if ( state.status != UIState.STATUS_NOT_CONFIGURED || this._hasSignedOutOfSync )` → `this.updateAllUI()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `state.status`, `this._hasSignedOutOfSync`

## init()
- 位置: L1403-1588
- 役割: 一度だけ実行する。FxA が無効なら onFxaDisabled で終える。有効なら FTL を読み込み、メニューの要素を取り、初期表示を整え、クリックと表示のイベントを登録し、Nimbus の CTA 変数とアイコンの variant を適用する。
- 触るとき: メニューの初期化で登録するイベントや Nimbus 変数を増やすとき、要素が無いウィンドウで早期に抜ける条件を確かめるとき。
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
- 役割: UIState、終了、同期の各オブザーバーを外し、初期化フラグを戻す。
- 触るとき: ウィンドウを閉じるときの後始末に抜けが無いか確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._obs`
- XPCOM: `Services.obs`

## handleEvent()
- 位置: L1602-1624
- 役割: mouseover でツールチップを更新し、command と click は onCommand へ、ViewShowing と ViewHiding はメインメニューか FxA パネルかに応じた処理へ振り分ける。
- 触るとき: FxA メニューに新しいイベントの種類を追加するとき。
- 呼び出し先: `this.onCommand()`, `this.onFxAPanelViewHiding()`, `this.refreshSyncButtonsTooltip()`
- 条件付き依存: `if (event.target == PanelUI.mainView)` → `this.onAppMenuShowing()`
- 条件付き依存: `if (!(event.target == PanelUI.mainView))` → `this.onFxAPanelViewShowing()`
- 参照: `PanelUI.mainView`, `event.target`, `event.type`

## onAppMenuShowing()
- 位置: L1626-1643
- 役割: アプリメニューの表示時に、ヘッダ文言を Nimbus の CTA 文言(無ければ既定)にし、CTA の variant があれば露出を記録する。
- 触るとき: アプリメニューのヘッダ文言や露出計測を変えるとき。
- 呼び出し先: `NimbusFeatures.fxaAppMenuItem.getVariable()`, `PanelMultiView.getViewNode()`, `document.l10n.setAttributes()`, `this.getMenuCtaCopy()`
- 条件付き依存: `if (NimbusFeatures.fxaAppMenuItem.getVariable("ctaCopyVariant"))` → `NimbusFeatures.fxaAppMenuItem.recordExposureEvent()`
- 参照: `NimbusFeatures.fxaAppMenuItem`

## updateAppMenuSignInPromo()
- 位置: L1651-1656
- 役割: dismiss 状態を documentElement の fxa-sign-in-promo-dismissed 属性に反映する。CSS がこの属性でサインイン案内の表示を切り替える。
- 触るとき: サインイン案内の出し分けを CSS 側と合わせて変えるとき。
- 呼び出し先: `document.documentElement.toggleAttribute()`
- 参照: `this.APP_MENU_SIGN_IN_PROMO_DISMISSED`

## dismissAppMenuSignInPromo()
- 位置: L1658-1660
- 役割: APP_MENU_SIGN_IN_PROMO_DISMISSED の pref を true にして、以後サインイン案内を出さないようにする。
- 触るとき: サインイン案内の閉じ方や保存先を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## onFxAPanelViewShowing()
- 位置: L1662-1721
- 役割: 表示時にメニューメッセージの表示を記録し、同期オフの印を消す。サインアウトボタンと端末一覧の位置を、アプリメニューかアカウントメニューかに合わせて動かし、FxAMenuDeviceList を作る。avatar の CTA 露出も記録する。
- 触るとき: FxA パネルを開いたときの要素の並びや初期化を変えるとき。
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
- 役割: メニューメッセージを隠し、FxAMenuDeviceList の destroy を呼んで参照を消す。
- 触るとき: パネルを閉じた後の後始末を変えるとき。
- 呼び出し先: `MenuMessage.hidePxiMenuMessage()`, `panelview.syncedTabsPanelList.destroy()`
- 参照: `gBrowser.selectedBrowser`, `panelview.syncedTabsPanelList`

## _showSecureSyncSubpanel()
- 位置: L1729-1732
- 役割: 「今すぐ同期」のラベルを更新してから、セキュア同期のサブビューを表示する。
- 触るとき: セキュア同期のサブビューの開き方を変えるとき。
- 呼び出し先: `PanelUI.showSubView()`, `this._updateSecureSyncNowLabel()`

## _updateAppMenuSignedOutRow()
- 位置: L1734-1751
- 役割: アプリメニューのサインアウト行に、メールアドレスがあればそれを、無ければサインアウトの文言を設定し、メッセージも設定する。
- 触るとき: サインアウト行の文言を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (email)` → `titleEl.removeAttribute()`
- 条件付き依存: `if (!(email))` → `document.l10n.setAttributes()`
- 参照: `titleEl.textContent`

## _updateSecureSyncNowLabel()
- 位置: L1757-1779
- 役割: 同期中なら「同期中」、そうでなければ端末名入りの「今すぐ同期」ラベルを設定する。
- 触るとき: 「今すぐ同期」ボタンの文言を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`
- 条件付き依存: `if (this._isCurrentlySyncing)` → `labelEl.setAttribute()`
- 条件付き依存: `if (this._isCurrentlySyncing)` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(this._isCurrentlySyncing))` → `fxAccounts.device.getLocalName()`
- 条件付き依存: `if (!(this._isCurrentlySyncing))` → `labelEl.setAttribute()`
- 条件付き依存: `if (!(this._isCurrentlySyncing))` → `this.fluentStrings.formatValueSync()`
- 参照: `this._isCurrentlySyncing`

## _hasSignedOutOfSync()
- 位置: L1788-1790
- 役割: services.sync.lastversion にユーザー値があるかで、サインアウト済みか未サインインかを判定する。
- 触るとき: 未サインインとサインアウト済みの表示を分けるとき、bug 1784055 周辺の挙動を調べるとき。
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## _updateSyncStatusButton()
- 位置: L1804-1919
- 役割: 状態(同期オン、同期オフ、未サインイン、要再認証)に応じて、同期状態ボタンと同期オフカードのタイトル、説明、アクセシブルな名前を設定し、モバイル向けボタンの位置を決める。
- 触るとき: 同期状態ボタンの表示内容や、押したときの遷移先を変えるとき。
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
- 役割: 同期オンならセキュア同期のサブビュー、同期オフならサインイン済みは同期設定、未サインインは FxA のサインイン画面を開き、メニューを閉じる。
- 触るとき: 同期状態ボタンのクリック先を変えるとき。
- 呼び出し先: `UIState.get()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN && state.syncEnabled)` → `this._showSecureSyncSubpanel()`
- 条件付き依存: `if (state.status == UIState.STATUS_SIGNED_IN)` → `this.openPrefsFromFxaMenu()`
- 条件付き依存: `if (!(state.status == UIState.STATUS_SIGNED_IN))` → `this.emitFxaToolbarTelemetry()`
- 条件付き依存: `if (!(state.status == UIState.STATUS_SIGNED_IN))` → `this.openFxAEmailFirstPageFromFxaMenu()`
- 条件付き依存: `if (!(state.status == UIState.STATUS_SIGNED_IN && state.syncEnabled))` → `CustomizableUI.hidePanelForNode()`
- 参照: `UIState.STATUS_SIGNED_IN`, `state.status`, `state.syncEnabled`

## onCommand()
- 位置: L1938-2014
- 役割: ボタンの id で分岐し、モバイル案内、端末追加、端末管理、今すぐ同期、設定、サインイン、サインアウト、各リンク、同期の有効化、アカウント確認などの処理を呼ぶ。
- 触るとき: FxA メニューにボタンを追加して処理をつなぐとき。
- 呼び出し先: `PanelUI.hide()`, `this._getEntryPointForElement()`, `this.clickFxAMenuHeaderButton()`, `this.clickOpenConnectAnotherDevice()`, `this.disconnect()`, `this.dismissAppMenuSignInPromo()`, `this.doSyncFromFxaMenu()`, `this.emitFxaToolbarTelemetry()`, `this.enableSync()`, `this.openDeviceMissingHelp()`, `this.openDevicesManagementPage()`, `this.openFxAEmailFirstPageFromFxaMenu()`, `this.openGetFirefoxMobile()`, `this.openMonitorLink()`, `this.openPairDevice()`, `this.openPrefsFromFxaMenu()`, `this.openRelayLink()`, `this.openSendTabHelp()`, `this.openShareFirefoxLink()`, `this.openVPNLink()`, `this.signInToSync()`, `this.verifyAccount()`
- 参照: `button.id`

## observe()
- 位置: L2016-2040
- 役割: 初期化前の呼び出しはエラーを出して抜ける。UIState の更新では全体を更新し、終了時はアニメーションのタイマーを止め、clients の同期が終わると端末一覧と FxA パネルを更新する。
- 触るとき: 同期の状態変化を UI に伝える経路を変えるとき。
- 呼び出し先: `UIState.get()`, `clearTimeout()`, `this.onClientsSynced()`, `this.updateAllUI()`, `this.updateFxAPanel()`
- 条件付き依存: `if (!this._initialized)` → `console.error()`
- 参照: `UIState.ON_UPDATE`, `this._initialized`, `this._syncAnimationTimer`

## updateAllUI()
- 位置: L2042-2050
- 役割: パネル、状態、ツールチップ、同期ステータス、FxA パネル、端末一覧、接続中の OAuth クライアント一覧を順に更新する。
- 触るとき: UI 全体の再描画で何を更新するかを変えるとき。
- 呼び出し先: `this.ensureFxaDevices()`, `this.fetchListOfOAuthClients()`, `this.updateFxAPanel()`, `this.updatePanelPopup()`, `this.updateState()`, `this.updateSyncButtonsTooltip()`, `this.updateSyncStatus()`

## ensureFxaDevices()
- 位置: async L2058-2072
- 役割: サインイン済みで recentDeviceList が無ければ refreshFxaDevices を呼ぶ。それでも無ければ警告を出す。
- 触るとき: 端末一覧が null のまま UI が崩れる問題を調べるとき。
- 呼び出し先: `UIState.get()`
- 条件付き依存: `if (UIState.get().status != UIState.STATUS_SIGNED_IN)` → `console.info()`
- 条件付き依存: `if (!fxAccounts.device.recentDeviceList)` → `this.refreshFxaDevices()`
- 条件付き依存: `if (!fxAccounts.device.recentDeviceList)` → `console.warn()`
- 参照: `UIState.STATUS_SIGNED_IN`, `UIState.get().status`, `fxAccounts.device.recentDeviceList`

## refreshFxaDevices()
- 位置: async L2080-2093
- 役割: サインイン済みなら FxA の refreshDeviceList を ignoreCached 付きで呼ぶ。成功なら true、失敗はログを出して false を返す。
- 触るとき: 端末一覧の強制更新の頻度やキャッシュの扱いを変えるとき。
- 呼び出し先: `UIState.get()`, `fxAccounts.device.refreshDeviceList()`, `this.log.error()`
- 条件付き依存: `if (UIState.get().status != UIState.STATUS_SIGNED_IN)` → `console.info()`
- 参照: `UIState.STATUS_SIGNED_IN`, `UIState.get().status`

## fetchListOfOAuthClients()
- 位置: async L2100-2112
- 役割: サインイン済みなら FxA から接続中の OAuth クライアント一覧を取得して _attachedClients に保存する。
- 触るとき: 接続中のサービス一覧を扱う機能を変えるとき。
- 呼び出し先: `fxAccounts.listAttachedOAuthClients()`, `this.log.error()`
- 条件付き依存: `if (!this.isSignedIn)` → `console.info()`
- 参照: `this._attachedClients`, `this.isSignedIn`

## toggleAccountPanel()
- 位置: async L2114-2193
- 役割: カスタマイズ中は何もしない。入力の種類を確かめたうえで、未サインインなら FxA パネルを、サインイン済みなら同期パネルを開閉し、ASRouter に menuOpened を送る。
- 触るとき: アカウントパネルを開閉する入口の条件を変えるとき。
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
- 役割: 同期パネルを開いたという pref が未設定なら true にして、同期オフの印を次回以降出さないようにする。
- 触るとき: 同期オフの印の出し方を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(SYNC_PANEL_ACCESSED_PREF, false))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## updateFxAPanel()
- 位置: L2204-2411
- 役割: 状態ごとに FxA パネルの見出し、説明、アバター、サインアウトカード、サインインのプロモ、管理ボタンの表示を切り替え、同期状態ボタンも更新する。
- 触るとき: FxA パネルの状態別の表示内容を変えるとき。
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
- 役割: プロファイルとセキュア同期の要素を引数の要素の直後へ移し、同期状態ボタンをセキュア同期の見出しの後ろに置く。
- 触るとき: パネル内の並び順を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `anchorEl.after()`, `profileButtonsContainer.remove()`, `profilesHeaderLabel.remove()`, `profilesSeparator.remove()`, `secureSyncHeader.after()`, `secureSyncHeader.remove()`
- 参照: `secureSyncHeader.hidden`

## _showFxASignedOutCard()
- 位置: L2456-2489
- 役割: 未設定ならサインアウト済みの文言を、それ以外は登録メールと、未確認またはログイン失敗の文言を設定してカードを表示する。
- 触るとき: サインアウトやログイン失敗時のカードの文言を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`
- 条件付き依存: `if (state.status === UIState.STATUS_NOT_CONFIGURED)` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (state.status === UIState.STATUS_NOT_CONFIGURED)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(state.status === UIState.STATUS_NOT_CONFIGURED))` → `document.l10n.setAttributes()`
- 参照: `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `cardEl.hidden`, `emailEl.value`, `separatorEl.hidden`, `state.email`, `state.status`

## updateAvatarURL()
- 位置: L2491-2505
- 役割: avatarURL があり既定の画像でなければ画像を読み込み、成功時に --avatar-image-url を設定する。それ以外は変数を削除する。
- 触るとき: アバター画像を表示する条件を変えるとき。
- 条件付き依存: `if (!(avatarURL && !avatarIsDefault))` → `mainWindowEl.style.removeProperty()`
- 参照: `img.onerror`, `img.onload`, `img.src`

## img.onload()
- 位置: L2495-2497
- 役割: avatar の画像読み込みが成功したとき、CSS 変数 --avatar-image-url にその画像を設定する。
- 触るとき: アバター画像の反映方法を変えるとき。
- 呼び出し先: `mainWindowEl.style.setProperty()`

## img.onerror()
- 位置: L2498-2500
- 役割: avatar の画像読み込みが失敗したとき、CSS 変数 --avatar-image-url を削除して既定の表示に戻す。
- 触るとき: 画像の読み込み失敗時の表示を変えるとき。
- 呼び出し先: `mainWindowEl.style.removeProperty()`

## emitFxaToolbarTelemetry()
- 位置: L2519-2568
- 役割: UIState の準備後に入口(avatar メニューか app メニュー)を判定し、avatar 限定の種類は app メニューからなら捨てる。Glean のイベント名を組み立てて、状態や同期の有無などの extra と共に記録する。
- 触るとき: FxA メニューのテレメトリを追加・変更するとき、イベントが記録されない問題を調べるとき。
- 呼び出し先: `AVATAR_MENU_ONLY_PROFILES_COUNT_EVENT_TYPES.has()`, `AVATAR_MENU_ONLY_PROFILES_EVENT_TYPES.has()`, `Glean[category][methodName]?.record()`, `UIState.get()`, `UIState.isReady()`, `gSync.NONPREFIXED_EVENT_TYPES.has()`, `parts.map()`, `parts.map(cap).join()`, `parts.slice()`, `parts.slice(1).map()`, `parts.slice(1).map(cap).join()`, `this._getEntryPointForElement()`, `type.split()`
- 条件付き依存: `if (AVATAR_MENU_ONLY_PROFILES_COUNT_EVENT_TYPES.has(type))` → `SelectableProfileService?.getCachedProfileCount()`
- 参照: `extraOptions.profile_count`, `state.avatarIsDefault`, `state.avatarURL`, `state.status`, `state.syncEnabled`

## cap()
- 位置: L2561-2561
- 役割: 単語の先頭文字を大文字にする補助関数。
- 触るとき: Glean のメソッド名の組み立て方を変えるとき。
- 呼び出し先: `w.slice()`, `w[0].toUpperCase()`

## updatePanelPopup()
- 位置: L2570-2690
- 役割: アプリメニューの FxA 表示(ラベル、ステータス、見出し、サインアウト行)を状態ごとに設定する。サインアウト済みはサインアウト行を表示する。
- 触るとき: アプリメニューのアカウント表示を状態別に変えるとき。
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
- 役割: 状態に応じて、設定、同期オフ、再認証、未確認、同期オンの各メニュー項目と対応するボックスの表示を切り替える。
- 触るとき: 同期の状態ごとにどのメニュー項目を出すかを変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `document.getElementById()`
- 参照: `PanelMultiView.getViewNode( document, boxId ).hidden`, `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`, `document.getElementById(menuId).hidden`, `state.status`, `state.syncEnabled`

## updateSyncStatus()
- 位置: L2727-2738
- 役割: 同期ボタンのアニメーション状態と UIState の syncing を比べ、違えば同期開始または停止の処理を呼ぶ。
- 触るとき: 同期中の表示が始まらない、または止まらない問題を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("appMenu-viewCache") .content.querySelector()`, `document.querySelector()`, `syncNow.getAttribute()`
- 条件付き依存: `if (state.syncing != syncingUI)` → `this.onActivityStart()`
- 条件付き依存: `if (state.syncing != syncingUI)` → `this.onActivityStop()`
- 参照: `state.syncing`

## openSignInAgainPage()
- 位置: async L2740-2752
- 役割: 接続可能なら再サインイン用の URL を作り、既存のタブで開く。
- 触るとき: 再サインインのページの開き方を変えるとき。
- 呼び出し先: `FxAccounts.canConnectAccount()`, `FxAccounts.config.promiseConnectAccountURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `switchToTabHavingURI()`
- XPCOM: `Services.scriptSecurityManager`

## openDevicesManagementPage()
- 位置: async L2754-2760
- 役割: 端末管理ページの URL を作り、既存のタブで開く。
- 触るとき: 端末管理ページへの導線を変えるとき。
- 呼び出し先: `FxAccounts.config.promiseManageDevicesURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `switchToTabHavingURI()`
- XPCOM: `Services.scriptSecurityManager`

## openConnectAnotherDevice()
- 位置: async L2762-2768
- 役割: 端末接続用の URL を作り、新しいタブで開く。
- 触るとき: 端末追加の導線を変えるとき。
- 呼び出し先: `FxAccounts.config.promiseConnectDeviceURI()`, `openTrustedLinkIn()`

## clickOpenConnectAnotherDevice()
- 位置: async L2770-2774
- 役割: 端末追加の計測 cad を記録し、入口を判定してから openConnectAnotherDevice を呼ぶ。
- 触るとき: 端末追加ボタンの計測を変えるとき。
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openConnectAnotherDevice()`

## openSendToDevicePromo()
- 位置: L2776-2781
- 役割: タブ送信の案内ページ(identity.sendtabpromo.url)を既存のタブで開く。
- 触るとき: タブ送信の案内 URL を変えるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `switchToTabHavingURI()`
- XPCOM: `Services.urlFormatter`

## clickFxAMenuHeaderButton()
- 位置: async L2783-2802
- 役割: 状態に応じて遷移先を決める。未設定ならサインイン、ログイン失敗なら同期設定、未確認なら確認画面、サインイン済みなら管理ページを開く。
- 触るとき: FxA メニューのヘッダを押したときの遷移先を変えるとき。
- 呼び出し先: `UIState.get()`, `this._openFxAManagePageFromElement()`, `this.openFxAEmailFirstPage()`, `this.openFxAEmailFirstPageFromFxaMenu()`, `this.openPrefsFromFxaMenu()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `UIState.STATUS_SIGNED_IN`

## _getEntryPointForElement()
- 位置: L2811-2839
- 役割: 要素が app メニュー内なら fxa_app_menu、アカウントボタンまたは PanelUI-fxa-menu 系の子ビューなら fxa_avatar_menu、それ以外は fxa_discoverability_native を返す。テレメトリの入口名になる。
- 触るとき: 新しい FxA メニューの要素を追加し、その計測の入口名が正しく付くかを確かめるとき。
- 呼び出し先: `appMenuPanel.contains()`, `document.getElementById()`, `sourceElement.closest()`
- 参照: `sourceElement.id`

## openFxAEmailFirstPage()
- 位置: async L2841-2851
- 役割: アカウントに接続できるなら、入口と追加パラメータ付きのサインイン URL を作り、既存タブで開く。
- 触るとき: サインイン画面の入口や付与するパラメータを変えるとき。
- 呼び出し先: `FxAccounts.canConnectAccount()`, `FxAccounts.config.promiseConnectAccountURI()`, `switchToTabHavingURI()`

## openFxAEmailFirstPageFromFxaMenu()
- 位置: async L2853-2859
- 役割: login の計測を記録してから、要素から入口を求めて openFxAEmailFirstPage を呼ぶ。
- 触るとき: FxA メニューからサインインしたときの計測や入口を変えるとき。
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openFxAEmailFirstPage()`

## openFxAManagePage()
- 位置: async L2861-2864
- 役割: アカウント管理の URL を入口付きで作り、既存タブで開く。
- 触るとき: アカウント管理ページへの導線を変えるとき。
- 呼び出し先: `FxAccounts.config.promiseManageURI()`, `switchToTabHavingURI()`

## _openFxAManagePageFromElement()
- 位置: async L2866-2869
- 役割: account_settings の計測を記録し、要素から入口を求めて openFxAManagePage を呼ぶ。
- 触るとき: アカウント管理ページを FxA メニューから開くときの計測を変えるとき。
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openFxAManagePage()`

## sendTabToDevice()
- 位置: async L2872-2922
- 役割: タブ送信に対応した端末だけを選び、マスターパスワードの解除を確かめてから FxA の sendTab コマンドで送る。失敗した端末を数えて、全部失敗でなければ true を返す。
- 触るとき: タブ送信の対象端末の条件や失敗時の扱い、マスターパスワードの確認を変えるとき。
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
- 役割: 各タブを sendTabToDevice で送り、一つでも成功したら確認ヒントを FxA ボタン(無ければアプリメニューボタン)に出す。ログを書き出して結果を返す。
- 触るとき: タブ送信後の確認ヒントの表示先や条件を変えるとき。
- 呼び出し先: `Promise.all()`, `fxAccounts.flushLogFile()`, `results.includes()`, `tabsToSend.map()`, `this.sendTabToDevice()`
- 条件付き依存: `if (results.includes(true))` → `document.documentElement.getAttribute()`
- 条件付き依存: `if (results.includes(true))` → `document.getElementById()`
- 条件付き依存: `if (results.includes(true))` → `ConfirmationHint.show()`
- 参照: `document.getElementById("fxa-toolbar-menu-button")?.parentNode?.id`

## populateSendTabToDevicesMenu()
- 位置: L2956-3042
- 役割: 共有可能な URL を確かめ、古い送信項目を消してから、状態(同期無効、サインイン済み、未確認・失敗、未サインイン)に応じた項目を作って popup に追加する。最後に端末一覧を更新する。
- 触るとき: コンテキストメニューやツールバーの「端末に送る」項目の中身を状態ごとに変えるとき。
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
- 役割: 送信先の端末ごとに項目を作り、2 台以上なら「すべての端末に送る」と「端末の管理」を追加する。複数選択中なら選択タブ全部を送る。
- 触るとき: 送信先の一覧の並びや、全端末への送信の扱いを変えるとき。
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
- 役割: 渡された端末群に対して sendTabsAndConfirm で tabsToSend を送る。
- 触るとき: 送信メニューの各項目から送る対象を変えるとき。
- 呼び出し先: `this.sendTabsAndConfirm()`

## onSendAllCommand()
- 位置: L3066-3076
- 役割: 「すべての端末に送る」項目が選ばれたとき、全送信先に送り、コンテキストメニューからなら click_send_tab を all_devices として記録する。
- 触るとき: 全端末への送信の計測や対象を変えるとき。
- 呼び出し先: `send()`
- 条件付き依存: `if (contextMenuType)` → `this._recordSendTabTelemetry()`
- 参照: `targets.length`

## onTargetDeviceCommand()
- 位置: L3077-3089
- 役割: 個別の端末項目が選ばれたとき、clientId から該当の端末を探してその端末だけに送り、device として記録する。
- 触るとき: 個別端末への送信の計測や対象の探し方を変えるとき。
- 呼び出し先: `event.target.getAttribute()`, `send()`, `targets.find()`
- 条件付き依存: `if (contextMenuType)` → `this._recordSendTabTelemetry()`
- 参照: `t.id`, `targets.length`

## addTargetDevice()
- 位置: L3091-3108
- 役割: createDeviceNodeFn で項目を作り、clientId の有無で個別かすべてかの command ハンドラを付け、属性を設定して fragment に追加する。
- 触るとき: 送信メニューの項目の属性や種類を変えるとき。
- 呼び出し先: `createDeviceNodeFn()`, `fragment.appendChild()`, `targetDevice.addEventListener()`, `targetDevice.classList.add()`, `targetDevice.setAttribute()`

## _resetSendTabExposureTracking()
- 位置: L3169-3171
- 役割: 送信の露出を記録済みとして覚えていた集合を空にする。
- 触るとき: 露出の計測を新しいメニューの開き方ごとにやり直すとき。
- 呼び出し先: `this._sendTabExposureRecorded.clear()`

## _recordSendTabTelemetry()
- 位置: L3173-3217
- 役割: コンテキスト種別を Glean のカテゴリ、イベント種別をメソッド名に対応させ、device_count と action(必要時)を付けて記録する。対応がなければエラーを出して止める。
- 触るとき: タブ送信の Glean 計測の項目を追加・変更するとき。
- 呼び出し先: `Glean[category][method].record()`, `String()`
- 条件付き依存: `if ( !category || !method || (category == "sendTabToolbar" && method == "sendTabExposed") )` → `this.log.error()`
- 参照: `extraParams.action`, `extraParams.context_type`

## _appendSignedInSyncDisabled()
- 位置: L3219-3244
- 役割: 同期が無効なサインイン済みユーザー向けに、コンテキスト種別に応じた「同期を有効にする」項目を追加し、選ぶと enableSync を呼ぶ。
- 触るとき: 同期オフ時の送信メニューの案内文言や動きを変えるとき。
- 呼び出し先: `createDeviceNodeFn()`, `enableSyncMenuItem.addEventListener()`, `enableSyncMenuItem.classList.add()`, `enableSyncMenuItem.setAttribute()`, `fragment.appendChild()`, `this.enableSync()`
- 条件付き依存: `if (contextMenuType == "link")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (contextMenuType == "page")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(contextMenuType == "page"))` → `this.fluentStrings.formatValueSync()`

## _appendSendTabSingleDevice()
- 位置: L3246-3311
- 役割: 送信先が無い時の案内項目を作る。「携帯端末を接続」(ペアリング URL を開く)と「端末が見つからない」(ヘルプを開く)の 2 件を追加する。
- 触るとき: 送信先が無いときに出す導線や文言を変えるとき。
- 呼び出し先: `FxAccounts.config.promisePairingURI()`, `connectPhoneMenuItem.addEventListener()`, `connectPhoneMenuItem.classList.add()`, `connectPhoneMenuItem.setAttribute()`, `createDeviceNodeFn()`, `deviceMissingMenuItem.addEventListener()`, `deviceMissingMenuItem.classList.add()`, `deviceMissingMenuItem.setAttribute()`, `fragment.appendChild()`, `separator.classList.add()`, `switchToTabHavingURI()`, `this.openSendTabHelp()`
- 条件付き依存: `if (contextMenuType == "link")` → `this.fluentStrings.formatValuesSync()`
- 条件付き依存: `if (contextMenuType == "page")` → `this.fluentStrings.formatValuesSync()`
- 条件付き依存: `if (!(contextMenuType == "page"))` → `this.fluentStrings.formatValuesSync()`

## _appendSendTabVerify()
- 位置: L3313-3327
- 役割: 未確認またはログイン失敗のとき、状態の表示と「アカウントを確認」の項目を作って、_appendSendTabInfoItems に渡す。
- 触るとき: 未確認アカウント時の送信メニューの文言を変えるとき。
- 呼び出し先: `this._appendSendTabInfoItems()`, `this.fluentStrings.formatValuesSync()`

## command()
- 位置: L3319-3319
- 役割: 「アカウントを確認」項目が選ばれたときに、sendtab 用の設定画面を開く無名関数。
- 触るとき: 未確認時の確認項目の遷移先を変えるとき。
- 呼び出し先: `this.openPrefs()`

## _appendSendTabInfoItems()
- 位置: L3329-3347
- 役割: 無効化された状態表示の項目、区切り線、各アクション項目を fragment に順に追加する。
- 触るとき: 送信メニューの案内項目の並びや見た目を変えるとき。
- 呼び出し先: `actionItem.addEventListener()`, `actionItem.classList.add()`, `actionItem.setAttribute()`, `createDeviceNodeFn()`, `fragment.appendChild()`, `separator.classList.add()`, `status.classList.add()`, `status.setAttribute()`

## _appendSendTabSignedOut()
- 位置: L3349-3381
- 役割: 未サインイン時に、コンテキスト種別に応じた「サインイン」項目を作り、選ぶと openSignInAgainPage を呼ぶ。
- 触るとき: 未サインイン時の送信メニューの文言や遷移を変えるとき。
- 呼び出し先: `createDeviceNodeFn()`, `fragment.appendChild()`, `signInMenuItem.addEventListener()`, `signInMenuItem.classList.add()`, `signInMenuItem.setAttribute()`, `this.openSignInAgainPage()`
- 条件付き依存: `if (contextMenuType == "link")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (contextMenuType == "page")` → `this.fluentStrings.formatValueSync()`
- 条件付き依存: `if (!(contextMenuType == "page"))` → `this.fluentStrings.formatValueSync()`

## updateTabContextMenu()
- 位置: L3384-3449
- 役割: タブの右クリックの「端末に送る」項目を、FxA の有効状態、共有可能な URL の有無、送信先の種類に応じて表示・無効化し、露出を一度だけ記録する。
- 触るとき: タブの右クリックメニューの送信項目の出し分けや表示文言を変えるとき。
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
- 役割: ページ・リンクの右クリックの「端末に送る」「リンクを端末に送る」項目を、選択内容から種類を決め、有効性と送信先の種類に応じて表示・無効化する。露出を一度だけ記録する。
- 触るとき: ページやリンクの右クリックの送信項目の出し分けを変えるとき。
- 呼び出し先: `BrowserUtils.getShareableURL()`, `contextMenu.getLinkURI()`, `contextMenu.setItemAttr()`, `contextMenu.showItem()`, `document.getElementById()`, `sendLinkToDevice.setAttribute()`, `sendPageToDevice.setAttribute()`, `this.hasOnlyMobileSendTabTargets()`, `this.shouldHideSendContextMenuItems()`
- 条件付き依存: `if (!hideItems && enabled)` → `this.getSendTabTargets()`
- 条件付き依存: `if (!hideItems && enabled)` → `this._sendTabExposureRecorded.has()`
- 条件付き依存: `if (targets.length && !this._sendTabExposureRecorded.has(exposureKey))` → `this._recordSendTabTelemetry()`
- 条件付き依存: `if (targets.length && !this._sendTabExposureRecorded.has(exposureKey))` → `this._sendTabExposureRecorded.add()`
- 参照: `contextMenu.browser.currentURI`, `contextMenu.isContentSelected`, `contextMenu.onAudio`, `contextMenu.onCanvas`, `contextMenu.onImage`, `contextMenu.onLink`, `contextMenu.onPlainTextLink`, `contextMenu.onSaveableLink`, `contextMenu.onTextInput`, `contextMenu.onVideo`, `targets.length`, `this.FXA_ENABLED`, `this.sendTabConfiguredAndLoading`

## onActivityStart()
- 位置: L3537-3559
- 役割: 同期中フラグを立て、同期ボタンの「同期中」表示と syncstatus=active を全ての「今すぐ同期」ボタン(通常とキャッシュ分)に付けて、ラベルを更新する。
- 触るとき: 同期中の表示が始まる時の挙動を変えるとき。
- 呼び出し先: `Date.now()`, `clearTimeout()`, `document .getElementById()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll(".syncNowBtn") .forEach()`, `document.l10n.setAttributes()`, `document.querySelectorAll()`, `document.querySelectorAll(".syncNowBtn").forEach()`, `document.querySelectorAll(".syncnow-label").forEach()`, `el.getAttribute()`, `el.setAttribute()`, `this._updateSecureSyncNowLabel()`
- 参照: `this._isCurrentlySyncing`, `this._syncAnimationTimer`, `this._syncStartTime`

## _onActivityStop()
- 位置: L3561-3586
- 役割: 同期中フラグを下ろし、ラベルと syncstatus 属性を元に戻し、ラベルを更新して test:browser-sync:activity-stop を通知する。
- 触るとき: 同期終了時の表示の戻し方を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `document .getElementById()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll()`, `document .getElementById("appMenu-viewCache") .content.querySelectorAll(".syncNowBtn") .forEach()`, `document.l10n.setAttributes()`, `document.querySelectorAll()`, `document.querySelectorAll(".syncNowBtn").forEach()`, `document.querySelectorAll(".syncnow-label").forEach()`, `el.getAttribute()`, `el.removeAttribute()`, `this._updateSecureSyncNowLabel()`
- 参照: `this._isCurrentlySyncing`
- XPCOM: `Services.obs`

## onActivityStop()
- 位置: L3588-3602
- 役割: 同期開始からの経過時間が MIN_STATUS_ANIMATION_DURATION(1.6 秒)に満たなければ、残り時間だけ待ってから _onActivityStop を呼ぶ。
- 触るとき: 同期アニメーションを最低限見せる時間を変えるとき。
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (syncDuration < MIN_STATUS_ANIMATION_DURATION)` → `clearTimeout()`
- 条件付き依存: `if (syncDuration < MIN_STATUS_ANIMATION_DURATION)` → `setTimeout()`
- 条件付き依存: `if (syncDuration < MIN_STATUS_ANIMATION_DURATION)` → `this._onActivityStop()`
- 条件付き依存: `if (!(syncDuration < MIN_STATUS_ANIMATION_DURATION))` → `this._onActivityStop()`
- 参照: `this._syncAnimationTimer`, `this._syncStartTime`

## disconnect()
- 位置: async L3607-3624
- 役割: アカウントの切断なら確認の後 FxA と Sync を切断する。Sync だけなら確認の後 _disconnectSync を呼ぶ。確認で拒否されたら false を返す。
- 触るとき: サインアウトや Sync 切断の流れを変えるとき。
- 呼び出し先: `this._confirmSyncDisconnect()`, `this._disconnectSync()`
- 条件付き依存: `if (confirm)` → `this._confirmFxaAndSyncDisconnect()`
- 条件付き依存: `if (disconnectAccount)` → `this._disconnectFxaAndSync()`
- 参照: `options.deleteLocalData`, `options.userConfirmedDisconnect`

## _confirmFxaAndSyncDisconnect()
- 位置: async L3628-3670
- 役割: サインアウトの確認ダイアログを出し、ボタンの押下結果と「ローカルデータを削除」のチェック状態を返す。同期が無効ならチェックボックスを出さない。
- 触るとき: サインアウトの確認文言やローカルデータ削除の選択肢を変えるとき。
- 呼び出し先: `AIWindow.hasActiveAIWindows()`, `Services.prompt.asyncConfirmEx()`, `UIState.get()`, `document.l10n.formatValues()`, `propBag.get()`, `result.QueryInterface()`
- 参照: `Ci.nsIPropertyBag2`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_INTERNAL_WINDOW`, `UIState.get().syncEnabled`, `options.deleteLocalData`, `options.userConfirmedDisconnect`, `window.browsingContext`
- XPCOM: [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.prompt`

## _disconnectFxaAndSync()
- 位置: async L3672-3687
- 役割: 切断を Glean に記録し、SyncDisconnect.disconnect で切断して接続中クライアントの一覧を消す。true を返す。
- 触るとき: アカウント切断の処理や計測を変えるとき。
- 呼び出し先: `ChromeUtils.importESModule()`, `SyncDisconnect.disconnect()`, `SyncDisconnect.disconnect(deleteLocalData).catch()`, `console.error()`, `fxAccounts.telemetry.recordDisconnection()`
- 参照: `this._attachedClients`

## _confirmSyncDisconnect()
- 位置: async L3691-3715
- 役割: Sync 切断の確認ダイアログを出し、切断ボタンが押されたら true を返す。ローカルのデータは消さない。
- 触るとき: Sync 切断の確認文言を変えるとき。
- 呼び出し先: `Services.prompt.confirmEx()`, `document.l10n.formatValues()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`
- XPCOM: `Services.prompt`

## _disconnectSync()
- 位置: async L3717-3724
- 役割: 切断を記録し、Weave サービスの初期化を待ってから startOver で Sync の状態を初期化する。
- 触るとき: Sync のみの切断処理を変えるとき。
- 呼び出し先: `Weave.Service.startOver()`, `fxAccounts.telemetry.recordDisconnection()`
- 参照: `Weave.Service.promiseInitialized`

## doSync()
- 位置: L3728-3747
- 役割: サインイン済みなら同期中の表示にし、メインスレッドで保留中の FxA コマンドを取り直してから Weave.Service.sync を呼ぶ。
- 触るとき: 手動同期の処理順序や対象を変えるとき。
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
- 役割: doSync を呼び、sync_now を計測する。
- 触るとき: FxA メニューからの手動同期の計測を変えるとき。
- 呼び出し先: `this.doSync()`, `this.emitFxaToolbarTelemetry()`

## openPrefs()
- 位置: L3754-3759
- 役割: 同期の設定画面(paneSync-sync)を入口付きで開く。
- 触るとき: 同期の設定画面へ遷移する経路を変えるとき。
- 呼び出し先: `window.openPreferences()`

## openPrefsFromFxaMenu()
- 位置: L3761-3765
- 役割: 計測を記録し、要素から入口を求めて openPrefs を呼ぶ。
- 触るとき: FxA メニューから設定画面を開くときの計測を変えるとき。
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openPrefs()`

## openChooseWhatToSync()
- 位置: L3767-3771
- 役割: 計測を記録し、「同期する項目を選ぶ」の画面を開く。
- 触るとき: 同期項目の選択画面への導線を変えるとき。
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openPrefs()`

## openSyncSetup()
- 位置: L3773-3777
- 役割: 計測を記録し、入口を求めて openSyncSetupForEntryPoint を呼ぶ。
- 触るとき: 同期のセットアップ導線の入口の計測を変えるとき。
- 呼び出し先: `this._getEntryPointForElement()`, `this.emitFxaToolbarTelemetry()`, `this.openSyncSetupForEntryPoint()`

## openSyncSetupForEntryPoint()
- 位置: async L3785-3805
- 役割: 同期の鍵があれば同期項目の選択へ、無ければ FxA のパスワード設定 URL を既存タブで開く。失敗したら設定画面を開く。
- 触るとき: 同期を有効にする流れの分岐条件を変えるとき。
- 呼び出し先: `fxAccounts.keys.hasKeysForScope()`, `this.log.error()`, `this.openPrefs()`
- 条件付き依存: `if (hasKeys)` → `this.openPrefs()`
- 条件付き依存: `if (!(hasKeys))` → `FxAccounts.canConnectAccount()`
- 条件付き依存: `if (!(hasKeys))` → `FxAccounts.config.promiseSetPasswordURI()`
- 条件付き依存: `if (!(hasKeys))` → `switchToTabHavingURI()`

## signInToSync()
- 位置: async L3807-3818
- 役割: 入口がアプリメニューなら send-tab-app-menu、それ以外は send-tab-account-menu として接続 URL を作り、既存タブで開く。
- 触るとき: タブ送信の案内からのサインインの入口を変えるとき。
- 呼び出し先: `FxAccounts.config.promiseConnectAccountURI()`, `switchToTabHavingURI()`, `this._getEntryPointForElement()`

## enableSync()
- 位置: L3820-3822
- 役割: about:preferences の同期設定を新しいタブで開く。
- 触るとき: 同期を有効にする導線の遷移先を変えるとき。
- 呼び出し先: `openTrustedLinkIn()`

## openPairDevice()
- 位置: async L3824-3835
- 役割: 入口(指定が無ければ要素から判定)を使って端末ペアリングの URL を作り、既存タブで開く。
- 触るとき: 携帯端末のペアリング導線を変えるとき。
- 呼び出し先: `FxAccounts.config.promisePairingURI()`, `switchToTabHavingURI()`
- 条件付き依存: `if (!entryPoint)` → `this._getEntryPointForElement()`

## verifyAccount()
- 位置: async L3837-3839
- 役割: about:preferences#sync を新しいタブで開き、アカウントの確認に誘導する。
- 触るとき: アカウント確認の導線を変えるとき。
- 呼び出し先: `openTrustedLinkIn()`

## openSendTabHelp()
- 位置: L3841-3846
- 役割: タブ送信の不具合ヘルプの URL(identity.sendtab.deviceissues.url)を既存タブで開く。
- 触るとき: タブ送信のヘルプのリンク先を変えるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `switchToTabHavingURI()`
- XPCOM: `Services.urlFormatter`

## openDeviceMissingHelp()
- 位置: L3848-3854
- 役割: 端末管理に関するサポートページを既存タブで開く。
- 触るとき: 端末が見つからない時のヘルプのリンク先を変えるとき。
- 呼び出し先: `switchToTabHavingURI()`

## openGetFirefoxMobile()
- 位置: L3856-3864
- 役割: モバイル版 Firefox の案内ページを、計測用のパラメータ付きで既存タブで開く。
- 触るとき: モバイル版への誘導 URL やそのパラメータを変えるとき。
- 呼び出し先: `switchToTabHavingURI()`

## openSyncedTabsPanel()
- 位置: L3866-3886
- 役割: sync-button の配置を調べ、オーバーフローにあればナビバーを開いてから、なければ可視のボタンかアプリメニューボタンを基点にして同期タブのサブビューを表示する。
- 触るとき: 同期タブのパネルを開く経路(ツールバー、オーバーフロー、アプリメニュー)を変えるとき。
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
- 役割: 現在の UIState を取り、同期ボタンのツールチップを更新する。
- 触るとき: マウスオーバー時のツールチップの更新元を変えるとき。
- 呼び出し先: `UIState.get()`, `this.updateSyncButtonsTooltip()`

## updateSyncButtonsTooltip()
- 位置: L3898-3934
- 役割: 状態が要確認なら確認、要再認証なら再認証、未設定なら表示しない、それ以外は最終同期の時刻をツールチップにして、PanelUI-remotetabs-syncnow に設定する。
- 触るとき: 同期ボタンのツールチップの文言を状態ごとに変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `this.fluentStrings.formatValueSync()`, `this.formatLastSyncDate()`
- 条件付き依存: `if (tooltiptext)` → `el.setAttribute()`
- 条件付き依存: `if (!(tooltiptext))` → `el.removeAttribute()`
- 参照: `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `state.email`, `state.lastSync`, `state.status`

## relativeTimeFormat()
- 位置: L3936-3942
- 役割: 長い形式の相対時刻フォーマッタを初回だけ作り、以後その値を使う。
- 触るとき: 最終同期時刻の表記を変えるとき。
- 参照: `Services.intl.RelativeTimeFormat`, `this.relativeTimeFormat`
- XPCOM: `Services.intl`

## formatLastSyncDate()
- 位置: L3944-3961
- 役割: 日付が無ければ null、あれば現在から 1 秒前までの範囲で相対時刻の文字列にする。例外時はログを出して null を返す。
- 触るとき: 最終同期時刻の表示形式やエラー時の扱いを変えるとき。
- 呼び出し先: `Date.now()`, `this.log.warn()`, `this.relativeTimeFormat.formatBestUnit()`

## onClientsSynced()
- 位置: L3963-3976
- 役割: クライアントの同期が終わると、端末数が 1 を超えるかで PanelUI-remotetabs-main の devices-status を multi か single に設定する。
- 触るとき: 複数端末があるときの表示の出し分けを変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`
- 条件付き依存: `if (Weave.Service.clientsEngine.stats.numClients > 1)` → `element.setAttribute()`
- 条件付き依存: `if (!(Weave.Service.clientsEngine.stats.numClients > 1))` → `element.setAttribute()`
- 参照: `Weave.Service.clientsEngine.stats.numClients`

## onFxaDisabled()
- 位置: L3978-3989
- 役割: fxadisabled と fxastatus=not_configured を設定し、sync-ui-item の要素をすべて隠す。
- 触るとき: FxA が無効なときに同期関連の UI を隠す範囲を変えるとき。
- 呼び出し先: `document.documentElement.setAttribute()`, `document.querySelectorAll()`
- 参照: `item.hidden`

## hasClientForId()
- 位置: L4000-4002
- 役割: 接続中の OAuth クライアント一覧に、指定の ID を持つものがあるか判定する。
- 触るとき: 製品の CTA で、既に接続中かどうかを判定する条件を変えるとき。
- 呼び出し先: `this._attachedClients?.some()`
- 参照: `c.id`

## updateCTAPanel()
- 位置: L4004-4101
- 役割: FxA 関連 CTA の実験が有効で、アプリメニューからでなければ CTA パネルを表示し、Monitor、Relay、VPN、Share Firefox の各ボタンの表示と文言を、pref と接続状態から決める。
- 触るとき: アカウントメニューの製品 CTA の表示条件や順序を変えるとき。
- 呼び出し先: `BrowserUtils.shouldShowPromo()`, `PanelMultiView.getViewNode()`, `Services.prefs.getBoolPref()`, `this.hasClientForId()`, `this.updateCTAButtonStrings()`
- 参照: `BrowserUtils.PromoType.RELAY`, `BrowserUtils.PromoType.VPN`, `VpnPanelEl.hidden`, `anchor.id`, `mainPanelEl.hidden`, `monitorPanelEl.hidden`, `privacyToolsSeparatorEl.hidden`, `relayPanelEl.hidden`, `shareFirefoxPanelEl.hidden`, `this.FXA_CTA_MENU_ENABLED`, `this.isSignedIn`
- XPCOM: `Services.prefs`

## updateCTAButtonStrings()
- 位置: L4121-4132
- 役割: CTA ボタンのタイトルを、接続中なら接続中用、そうでなければ宣伝用に切り替え、接続中は説明を隠す。
- 触るとき: 製品 CTA の文言の出し分けを変えるとき。
- 呼び出し先: `buttonEl.querySelector()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (!inUse)` → `document.l10n.setAttributes()`
- 参照: `descriptionEl.hidden`

## openMonitorLink()
- 位置: L4134-4141
- 役割: Monitor の計測を記録し、接続状態に応じた URL で openCtaLink を呼ぶ。
- 触るとき: Monitor の CTA の遷移先や計測を変えるとき。
- 呼び出し先: `this._ctaURL()`, `this.emitFxaToolbarTelemetry()`, `this.openCtaLink()`

## openRelayLink()
- 位置: L4143-4150
- 役割: Relay の計測を記録し、接続状態に応じた URL で openCtaLink を呼ぶ。
- 触るとき: Relay の CTA の遷移先や計測を変えるとき。
- 呼び出し先: `this._ctaURL()`, `this.emitFxaToolbarTelemetry()`, `this.openCtaLink()`

## openVPNLink()
- 位置: L4152-4159
- 役割: VPN の計測を記録し、接続状態に応じた URL で openCtaLink を呼ぶ。
- 触るとき: VPN の CTA の遷移先や計測を変えるとき。
- 呼び出し先: `this._ctaURL()`, `this.emitFxaToolbarTelemetry()`, `this.openCtaLink()`

## openShareFirefoxLink()
- 位置: L4161-4164
- 役割: accounts_menu として紹介画面を開き、パネルを閉じる。
- 触るとき: Firefox の紹介の導線を変えるとき。
- 呼び出し先: `PanelUI.hide()`, `Referrals.openReferralsTab()`

## _ctaURL()
- 位置: L4175-4182
- 役割: 基の URL に共通の UTM パラメータを付け、utm_content を指定して URL を返す。
- 触るとき: 製品 CTA の計測用パラメータを変えるとき。
- 呼び出し先: `Object.entries()`, `url.searchParams.set()`

## openCtaLink()
- 位置: L4194-4202
- 役割: 製品が接続済みなら接続済み用の URL、そうでなければ既定の URL を openLink で開き、パネルを閉じる。
- 触るとき: 製品 CTA で接続済みの人にどの URL を見せるかを変えるとき。
- 呼び出し先: `PanelUI.hide()`, `this.hasClientForId()`, `this.openLink()`
- 参照: `this.isSignedIn`

## getMenuCtaCopy()
- 位置: L4236-4287
- 役割: Nimbus の ctaCopyVariant に応じて、アプリメニューなら折りたたみ用の文言 ID、アバターメニューならヘッダ用のタイトル ID と説明を返す。実験が無ければ null。
- 触るとき: CTA 実験の文言の出し分けを増やしたり変えたりするとき。
- 呼び出し先: `feature.getVariable()`, `this.fluentStrings.formatValueSync()`
- 参照: `NimbusFeatures.fxaAppMenuItem`

## applyAvatarIconVariant()
- 位置: L4297-4305
- 役割: 許可された variant(control、human-circle、fox-circle)なら fxa-avatar-icon-variant 属性を付ける。
- 触るとき: アバターアイコンの実験の種類を追加するとき。
- 呼び出し先: `ICON_VARIANTS.includes()`, `document.documentElement.setAttribute()`

## openLink()
- 位置: L4307-4309
- 役割: URL を既存タブで開く(クエリ文字列は置き換え)。
- 触るとき: FxA 関連のリンクを開く共通の方法を変えるとき。
- 呼び出し先: `switchToTabHavingURI()`

## sendTabToolbarButtonShouldBeEnabled()
- 位置: L4311-4326
- 役割: 初期化してから、FxA が無効、または送信先の読み込み中なら false を、共有可能な URL があるかを返す。
- 触るとき: ツールバーの送信ボタンを有効にする条件を変えるとき。
- 呼び出し先: `BrowserUtils.getShareableURL()`, `this.init()`
- 参照: `this.FXA_ENABLED`, `this.sendTabConfiguredAndLoading`

## populateSendTabToolbarButton()
- 位置: async L4328-4335
- 役割: 現在のページのタイトルと URL で populateSendTabToDevicesMenu を呼び、種類 toolbar として送信メニューを作る。
- 触るとき: ツールバーの送信ボタンのメニュー内容を変えるとき。
- 呼び出し先: `this.populateSendTabToDevicesMenu()`
- 参照: `menuPopup.documentGlobal.gBrowser.contentTitle`, `menuPopup.documentGlobal.gBrowser.currentURI`
