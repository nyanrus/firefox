# browser/base/content/browser-init.js

source: browser/base/content/browser-init.js
source-hash: d1e5aa51451a6999b80cf44fd1c1a7a114a91a4a
lines: 1166

## <module>
- 役割: ブラウザウィンドウの起動・読み込み・終了の各段階を担う gBrowserInit を定義し、window のイベントに接続する
- 呼び出し先: `Promise.withResolvers()`

## observe()
- 位置: L24-59
- 役割: Translations の有効状態変化を受け、翻訳メニュー項目の更新と既存タブの Translations アクター再生成を行う。
- 触るとき: 翻訳機能の無効化・再有効化時の UI 更新を変えるとき。
- 呼び出し先: `XULBrowserWindow._updateElementsForContentType()`
- 条件付き依存: `if (topic !== "translations:enabled-state-changed")` → `console.warn()`
- 条件付き依存: `if (data === "enabled")` → `windowGlobal.getActor()`
- 参照: `gBrowser.tabs`, `tab.linkedBrowser?.browsingContext?.currentWindowGlobal`, `windowGlobal.isClosed`, `windowGlobal.isCurrentGlobal`

## _setupFirstContentWindowPaintPromise()
- 位置: L62-81
- 役割: 最初のコンテンツ描画(MozAfterPaint)を待つ Promise を用意し、タブ採用中は待機する。
- 触るとき: 初回描画の判定やフォーカス移動のタイミングを調べるとき。
- 呼び出し先: `addEventListener()`
- 参照: `window.windowUtils.lastTransactionId`

## layerTreeListener()
- 位置: L64-79
- 役割: MozLayerTreeReady 後にタブ採用が終わっていれば、次の MozAfterPaint の監視を始める。
- 触るとき: 初回描画待ちの開始条件を変えるとき。
- 呼び出し先: `addEventListener()`, `removeEventListener()`, `this.getTabToAdopt()`

## listener()
- 位置: L72-77
- 役割: transactionId が開始時より進んだ MozAfterPaint を見つけ、初回描画 Promise を解決する。
- 触るとき: 初回描画の判定条件を変えるとき。
- 条件付き依存: `if (e.transactionId > lastTransactionId)` → `window.removeEventListener()`
- 条件付き依存: `if (e.transactionId > lastTransactionId)` → `this._firstContentWindowPaintDeferred.resolve()`
- 参照: `e.transactionId`

## getTabToAdopt()
- 位置: L83-100
- 役割: window.arguments[0] が XUL タブなら採用対象として保持し、引数側の参照を消す。
- 触るとき: 別ウィンドウからタブを移す起動経路を調べるとき。
- 呼び出し先: `window.XULElement.isInstance()`
- 参照: `this._tabToAdopt`, `window.arguments`

## _clearTabToAdopt()
- 位置: L102-104
- 役割: 採用対象のタブ参照を null にして、採用処理の完了を記録する。
- 触るとき: タブ採用の後始末を変えるとき。
- 参照: `this._tabToAdopt`

## isAdoptingTab()
- 位置: L108-110
- 役割: 起動時に既存タブを採用中かどうかを返す。
- 触るとき: 採用中かどうかで分岐する処理を追加・変更するとき。
- 呼び出し先: `this.getTabToAdopt()`

## onBeforeInitialXULLayout()
- 位置: L112-235
- 役割: XUL レイアウト前にウィンドウサイズ・メニューバー・タスクバータブ等の属性を設定し、before-layout モジュールを呼ぶ。
- 触るとき: 起動直後のウィンドウ属性やサイズ決定を変えるとき。
- 呼び出し先: `BrowserUtils.callModulesFromCategory()`, `ChromeUtils.shouldResistFingerprinting()`, `Services.prefs.getBoolPref()`, `document.getElementById()`, `tabToAdopt?.hasAttribute()`, `this._setupFirstContentWindowPaintPromise()`, `this.getTabToAdopt()`, `updateBookmarkToolbarVisibility()`, `window.TabBarVisibility.update()`
- 条件付き依存: `if (!window.toolbar.visible)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!(ChromeUtils.shouldResistFingerprinting("RoundWindowSize", null)))` → `document.documentElement.hasAttribute()`
- 条件付き依存: `if (!document.documentElement.hasAttribute("width"))` → `Math.min()`
- 条件付き依存: `if (!document.documentElement.hasAttribute("width"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (width < TARGET_WIDTH && height < TARGET_HEIGHT)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (nativeMenubar)` → `toolbarMenubar.removeAttribute()`
- 条件付き依存: `if (!(nativeMenubar))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(nativeMenubar))` → `toolbarMenubar.setAttribute()`
- 条件付き依存: `if (window.arguments?.[1] instanceof Ci.nsIPropertyBag2)` → `extraOptions.hasKey()`
- 条件付き依存: `if (extraOptions.hasKey("taskbartab"))` → `extraOptions.getPropertyAsAString()`
- 条件付き依存: `if (extraOptions.hasKey("taskbartab"))` → `extraOptions.get()`
- 条件付き依存: `if (taskbarTabClass)` → `window.document.documentElement.setAttribute()`
- 条件付き依存: `if (extraOptions.hasKey("taskbartab"))` → `window.document.documentElement.setAttribute()`
- 条件付き依存: `if (extraOptions.hasKey("ai-window"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (extraOptions.hasKey("aiwindow-immersive-view"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (extraOptions.hasKey("chromeless-window"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (extraOptions.hasKey("web-extension-popup-window"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (extraOptions.hasKey("aswebauth"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (tabToAdopt?.hasAttribute?.("mini-window"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (tabToAdopt?.hasAttribute?.("mini-window"))` → `tabToAdopt.hasAttribute()`
- 条件付き依存: `if (tabToAdopt.hasAttribute("cropped-mini-window"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "toolkit.legacyUserProfileCustomizations.windowIcon", false ) )` → `document.documentElement.setAttribute()`
- 参照: `Ci.nsIPropertyBag2`, `Services.appinfo.nativeMenubar`, `screen.availHeight`, `screen.availWidth`, `toolbarMenubar.collapsed`, `window.arguments`, `window.document.documentElement.id`, `window.toolbar.visible`
- XPCOM: [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.appinfo` / `Services.prefs`

## onDOMContentLoaded()
- 位置: L237-290
- 役割: DOMContentLoaded 時に tabbrowser 用モジュールを呼び、gURLBar 等の接続と初期フォーカスを行う。
- 触るとき: DOM 読み込み後の初期化順を変えるとき。
- 呼び出し先: `BrowserUtils.callModulesFromCategory()`, `Services.prefs.getBoolPref()`, `URL.parse()`, `gURLBar.addGBrowserListeners()`, `this._callWithURIToLoad()`, `this._setInitialFocus()`, `updateFxaToolbarMenu()`, `updatePrintCommands()`, `window.docShell.treeOwner .QueryInterface()`, `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.search.widget.new", false))` → `document.getElementById("searchbar-new")?.addGBrowserListeners()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.search.widget.new", false))` → `document.getElementById()`
- 条件付き依存: `if (nonQuery in gPageIcons)` → `gBrowser.setIcon()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `gBrowser.selectedTab`, `this.domContentLoaded`, `url.URI.prePath`, `url.pathname`, `window.XULBrowserWindow`, `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow).XULBrowserWindow`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / `Services.prefs`

## onLoad()
- 位置: L292-451
- 役割: load 時に進行リスナー・翻訳・AppCommand 等を接続し、採用タブの差し替えと遅延起動の予約を行う。
- 触るとき: ウィンドウ読み込み完了時の接続処理を追加・変更するとき。
- 呼び出し先: `BrowserUtils.callModulesFromCategory()`, `FullPageTranslationsPanel.onLocationChange()`, `PopupAndRedirectBlockerObserver.handleEvent()`, `Services.obs.notifyObservers()`, `gBrowser.addEventListener()`, `gBrowser.addProgressListener()`, `gBrowser.addTabsProgressListener()`, `gBrowser.tabContainer.addEventListener()`, `gRemoteControl.updateVisualCue()`, `this._delayedStartup.bind()`, `this.getTabToAdopt()`, `window.addEventListener()`, `window.document.documentElement.hasAttribute()`
- 条件付き依存: `if (!gMultiProcessBrowser)` → `gBrowser.tabpanels.addEventListener()`
- 条件付き依存: `if (tabToAdopt)` → `gBrowser.tabpanels.dispatchEvent()`
- 条件付き依存: `if (tabToAdopt)` → `gBrowser.stop()`
- 条件付き依存: `if (tabToAdopt)` → `gURLBar.removeAttribute()`
- 条件付き依存: `if (tabToAdopt)` → `Tabbrowser.isTab()`
- 条件付き依存: `if ( Tabbrowser.isTab(tabToAdopt) && !tabToAdopt.linkedBrowser.isRemoteBrowser )` → `swapBrowsers()`
- 条件付き依存: `if (!( Tabbrowser.isTab(tabToAdopt) && !tabToAdopt.linkedBrowser.isRemoteBrowser ))` → `addEventListener()`
- 条件付き依存: `if (!PrivateBrowsingUtils.enabled)` → `document.getElementById()`
- 条件付き依存: `if (!PrivateBrowsingUtils.enabled)` → `document.getElementById("key_privatebrowsing").remove()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById("key_quitApplication").remove()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById("menu_FileQuitItem").removeAttribute()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `PanelMultiView.getViewNode( document, "appMenu-quit-button2" )?.removeAttribute()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `PanelMultiView.getViewNode()`
- 条件付き依存: `if (window.browsingContext.isDocumentPiP)` → `document.getElementById(cmd).setAttribute()`
- 条件付き依存: `if (window.browsingContext.isDocumentPiP)` → `document.getElementById()`
- 参照: `BrowserUIUtils.quitShortcutDisabled`, `PrivateBrowsingUtils.enabled`, `document.getElementById("Tools:PrivateBrowsing").hidden`, `document.getElementById("menu_newPrivateWindow").hidden`, `gBrowser.selectedBrowser`, `gURLBar.readOnly`, `tabToAdopt.linkedBrowser.isRemoteBrowser`, `this._boundDelayedStartup`, `this._loadHandled`, `window.TabsProgressListener`, `window.XULBrowserWindow`, `window.browsingContext.isDocumentPiP`, `window.toolbar.visible`
- XPCOM: `Services.obs`

## swapBrowsers()
- 位置: L374-408
- 役割: 採用されるタブ・タブグループ・分割ビューの種類ごとに、仮のタブと入れ替えて現ウィンドウへ移す。
- 触るとき: 別ウィンドウからのタブ・グループ移動の挙動を変えるとき。
- 呼び出し先: `Tabbrowser.isTabGroupLabel()`, `this._clearTabToAdopt()`
- 条件付き依存: `if (Tabbrowser.isTabGroupLabel(tabToAdopt))` → `gBrowser.adoptTabGroup()`
- 条件付き依存: `if (Tabbrowser.isTabGroupLabel(tabToAdopt))` → `gBrowser.removeTab()`
- 条件付き依存: `if (!(Tabbrowser.isTabGroupLabel(tabToAdopt)))` → `Tabbrowser.isTabGroup()`
- 条件付き依存: `if (Tabbrowser.isTabGroup(tabToAdopt))` → `gBrowser.adoptTabGroup()`
- 条件付き依存: `if (Tabbrowser.isTabGroup(tabToAdopt))` → `gBrowser.removeTab()`
- 条件付き依存: `if (Tabbrowser.isTabGroup(tabToAdopt))` → `Glean.tabgroup.groupInteractions.move_window.add()`
- 条件付き依存: `if (!(Tabbrowser.isTabGroup(tabToAdopt)))` → `Tabbrowser.isSplitViewWrapper()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabToAdopt))` → `gBrowser.adoptSplitView()`
- 条件付き依存: `if (gBrowser.selectedTabs.length > 1)` → `gBrowser.addRangeToMultiSelectedTabs()`
- 条件付き依存: `if (Tabbrowser.isSplitViewWrapper(tabToAdopt))` → `gBrowser.removeTab()`
- 条件付き依存: `if (tabToAdopt.group)` → `Glean.tabgroup.tabInteractions.remove_new_window.add()`
- 条件付き依存: `if (!(Tabbrowser.isSplitViewWrapper(tabToAdopt)))` → `gBrowser.swapBrowsersAndCloseOther()`
- 参照: `gBrowser.selectedTab`, `gBrowser.selectedTabs.length`, `splitview.tabs`, `splitview.tabs.length`, `tabToAdopt.group`

## _cancelDelayedStartup()
- 位置: L453-456
- 役割: MozAfterPaint に登録した遅延起動のリスナーを外す。
- 触るとき: 遅延起動の中止経路を調べるとき。
- 呼び出し先: `window.removeEventListener()`
- 参照: `this._boundDelayedStartup`

## _delayedStartup()
- 位置: L458-754
- 役割: 初回描画後に、各種オブザーバー登録・ポリシー適用・セッション復元後の処理などの重い初期化を行う。
- 触るとき: 遅延起動で行う初期化を追加・並べ替えするとき。
- 呼び出し先: `BrowserUtils.callModulesFromCategory()`, `Glean.browserTimings.startupTimeline.delayedStartupFinished.set()`, `Glean.browserTimings.startupTimeline.delayedStartupStarted.set()`, `Referrals.maybeLockPref()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `Services.telemetry.msSinceProcessStart()`, `SessionStore.promiseAllWindowsRestored.then()`, `SessionStore.promiseInitialized.then()`, `TranslationsParent.ensurePrefObservers()`, `UpdateUrlbarSearchSplitterState()`, `_resolveDelayedStartup()`, `browser?.getTabBrowser()`, `document.documentElement.setAttribute()`, `document.getElementById()`, `gBrowser.addEventListener()`, `gIdentityHandler.refreshIdentityBlock()`, `gNavToolbox.addEventListener()`, `gPermissionPanel.updateSharingIndicator()`, `htmlTooltip.addEventListener()`, `htmlTooltip.toggleAttribute()`, `initBackForwardButtonTooltip()`, `isBidiEnabled()`, `this._cancelDelayedStartup()`, `this._handleURIToLoad()`, `this._schedulePerWindowIdleTasks()`, `window.addEventListener()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `safeMode.setAttribute()`
- 条件付き依存: `if (gBidiUI)` → `document.getElementById()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("ui.click_hold_context_menus", false))` → `SetClickAndHoldHandlers()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `updateEditUIVisibility()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `placesContext.addEventListener()`
- 条件付き依存: `if (wasMinimized != isMinimized)` → `UpdatePopupNotificationsVisibility()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE)` → `Services.policies.isAllowed()`
- 条件付き依存: `if (!Services.policies.isAllowed("hideShowMenuBar"))` → `document .getElementById("toolbar-menubar") .removeAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("hideShowMenuBar"))` → `document .getElementById()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `document.getElementById()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `savePageCommand.setAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `openFileCommand.setAttribute()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `document.addEventListener()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `browser .getTabBrowser() ?.getNotificationBox()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `browser .getTabBrowser()`
- 条件付き依存: `if (!Services.policies.isAllowed("filepickers"))` → `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if ( notificationBox && !notificationBox.getNotificationWithValue("filepicker-blocked") )` → `notificationBox.appendNotification()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE)` → `Services.policies.getActivePolicies()`
- 条件付き依存: `if ("ManagedBookmarks" in policies)` → `managedBookmarks.filter()`
- 条件付き依存: `if (children.length)` → `document.createXULElement()`
- 条件付き依存: `if (children.length)` → `managedBookmarksButton.setAttribute()`
- 条件付き依存: `if (children.length)` → `managedBookmarks.find()`
- 条件付き依存: `if (toplevel)` → `managedBookmarksButton.setAttribute()`
- 条件付き依存: `if (!(toplevel))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (children.length)` → `managedBookmarksPopup.setAttribute()`
- 条件付き依存: `if (children.length)` → `managedBookmarksPopup.addEventListener()`
- 条件付き依存: `if (children.length)` → `PlacesToolbarHelper.openManagedBookmark()`
- 条件付き依存: `if (children.length)` → `PlacesToolbarHelper.onDragStartManaged()`
- 条件付き依存: `if (children.length)` → `PlacesToolbarHelper.populateManagedBookmarks()`
- 条件付き依存: `if (children.length)` → `managedBookmarksPopup.toggleAttribute()`
- 条件付き依存: `if (children.length)` → `managedBookmarksPopup.classList.add()`
- 条件付き依存: `if (children.length)` → `managedBookmarksButton.appendChild()`
- 条件付き依存: `if (children.length)` → `gNavToolbox.palette.appendChild()`
- 条件付き依存: `if (children.length)` → `CustomizableUI.ensureWidgetPlacedInWindow()`
- 条件付き依存: `if (children.length)` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!CustomizableUI.getPlacementOfWidget("managed-bookmarks"))` → `CustomizableUI.addWidgetToArea()`
- 参照: `AppConstants.platform`, `BrowserHandler.kiosk`, `CustomizableUI.AREA_BOOKMARKS`, `Services.appinfo.inSafeMode`, `Services.policies.ACTIVE`, `Services.policies.status`, `children.length`, `document.getElementById("documentDirection-separator").hidden`, `document.getElementById("documentDirection-swap").hidden`, `document.getElementById("textfieldDirection-separator").hidden`, `document.getElementById("textfieldDirection-swap").hidden`, `event.currentTarget`, `event.dataTransfer.effectAllowed`, `event.target`, `gURLBar.readOnly`, `htmlTooltip.triggerNode?.documentGlobal.browsingContext.top .embedderElement`, `notificationBox.PRIORITY_INFO_LOW`, `policies.ManagedBookmarks`, `this._translationsEnabledStateObserver`, `this.delayedStartupFinished`, `toplevel.toplevel_name`, `window.STATE_MINIMIZED`, `window.closed`, `window.fullScreen`, `window.windowState`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.policies` / `Services.prefs` / `Services.telemetry`

## initBackForwardButtonTooltip()
- 位置: L552-558
- 役割: 戻る・進むボタンのツールチップに、設定されたショートカット表記を入れる。
- 触るとき: 戻る・進むボタンのツールチップ文言を変えるとき。
- 呼び出し先: `ShortcutUtils.prettifyShortcut()`, `document.getElementById()`, `document.l10n.setAttributes()`

## firstContentWindowPaintPromise()
- 位置: L760-762
- 役割: 初回コンテンツ描画の Promise を返す getter。
- 触るとき: 初回描画を待つ呼び出し元を追加するとき。
- 参照: `this._firstContentWindowPaintDeferred.promise`

## _setInitialFocus()
- 位置: L764-815
- 役割: 起動 URI に応じて URL バーかコンテンツへ初期フォーカスを移し、不要なら focused 属性を外す。
- 触るとき: 起動直後のフォーカス先を変えるとき。
- 呼び出し先: `Promise.resolve()`, `isBlankPageURL()`, `promise.then()`, `this._callWithURIToLoad()`, `this.getTabToAdopt()`
- 条件付き依存: `if ( isBlankPageURL(uriToLoad) || uriToLoad == "about:privatebrowsing" || this.getTabToAdopt()?.isEmpty )` → `gURLBar.select()`
- 条件付き依存: `if ( document.commandDispatcher.focusedElement == initiallyFocusedElement )` → `gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (shouldRemoveFocusedAttribute)` → `window.requestAnimationFrame()`
- 条件付き依存: `if (shouldRemoveFocusedAttribute)` → `gURLBar.removeAttribute()`
- 参照: `document.commandDispatcher.focusedElement`, `gBrowser.selectedBrowser.isRemoteBrowser`, `this.firstContentWindowPaintPromise`, `this.getTabToAdopt()?.isEmpty`

## _handleURIToLoad()
- 位置: L817-958
- 役割: window.arguments の URI やオプションを読み、起動時の URL 群をタブとして開く。
- 触るとき: 起動引数から開く URL の扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `this._callWithURIToLoad()`
- 条件付き依存: `if (Array.isArray(uriToLoad))` → `gBrowser.loadTabs()`
- 条件付き依存: `if (Array.isArray(uriToLoad))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (window.arguments[1])` → `extraOptions.hasKey()`
- 条件付き依存: `if (extraOptions.hasKey("hasValidUserGestureActivation"))` → `extraOptions.getPropertyAsBool()`
- 条件付き依存: `if (extraOptions.hasKey("textDirectiveUserActivation"))` → `extraOptions.getPropertyAsBool()`
- 条件付き依存: `if (extraOptions.hasKey("fromExternal"))` → `extraOptions.getPropertyAsBool()`
- 条件付き依存: `if (extraOptions.hasKey("triggeringSponsoredURL"))` → `extraOptions.getPropertyAsACString()`
- 条件付き依存: `if (extraOptions.hasKey("triggeringSponsoredURL"))` → `extraOptions.hasKey()`
- 条件付き依存: `if (extraOptions.hasKey("triggeringSponsoredURLVisitTimeMS"))` → `extraOptions.getPropertyAsUint64()`
- 条件付き依存: `if (extraOptions.hasKey("triggeringSource"))` → `extraOptions.getPropertyAsACString()`
- 条件付き依存: `if (extraOptions.hasKey("triggeringRemoteType"))` → `extraOptions.getPropertyAsACString()`
- 条件付き依存: `if (extraOptions.hasKey("forceAllowDataURI"))` → `extraOptions.getPropertyAsBool()`
- 条件付き依存: `if (extraOptions.hasKey("schemelessInput"))` → `extraOptions.getPropertyAsUint32()`
- 条件付き依存: `if (window.arguments.length >= 3)` → `openLinkIn()`
- 条件付き依存: `if (window.arguments.length >= 3)` → `console.error()`
- 条件付き依存: `if (window.arguments.length >= 3)` → `window.focus()`
- 条件付き依存: `if (!(window.arguments.length >= 3))` → `loadOneOrMoreURIs()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeUnset`, `Ci.nsIPropertyBag2`, `Ci.nsIScriptSecurityManager.DEFAULT_USER_CONTEXT_ID`, `globalHistoryOptions.triggeringSource`, `globalHistoryOptions.triggeringSponsoredURLVisitTimeMS`, `window.arguments`, `window.arguments.length`
- XPCOM: [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIPropertyBag2`](../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `nsIScriptSecurityManager` / `Services.scriptSecurityManager`

## _schedulePerWindowIdleTasks()
- 位置: L970-1001
- 役割: セッション復元後にウィンドウ単位のアイドルタスクを登録し、完了通知を最後に出す。
- 触るとき: ウィンドウごとのアイドル処理を追加するとき。
- 呼び出し先: `BrowserUtils.callModulesFromCategory()`, `ChromeUtils.idleDispatch()`, `Services.obs.notifyObservers()`, `this.idleTasksFinished.resolve()`
- 参照: `window.closed`
- XPCOM: `Services.obs`

## uriToLoadPromise()
- 位置: L1005-1047
- 役割: 起動時に読み込む URI を決める。ホームページのときは、セッション復元で上書きされるかを確認する。
- 触るとき: 起動時のページ選択ルールを変えるとき。
- 呼び出し先: `willOverride.then()`, `window.XULElement.isInstance()`
- 条件付き依存: `if (uri != defaultArgs)` → `AboutNewTab.noteNonDefaultStartup()`
- 条件付き依存: `if (uri instanceof Ci.nsIArray)` → `Array.from()`
- 条件付き依存: `if (uri instanceof Ci.nsIArray)` → `uri.enumerate()`
- 参照: `BrowserHandler.defaultArgs`, `Ci.nsIArray`, `Ci.nsISupportsString`, `SessionStartup.willOverrideHomepage`, `supportStr.data`, `this.uriToLoadPromise`, `uri.data`, `window.arguments`
- XPCOM: [`nsIArray`](../../../dom/events/nsIEventListenerService.idl.md) / [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md)

## _callWithURIToLoad()
- 位置: L1051-1058
- 役割: 起動 URI が即時に決まれば同期で、Promise なら解決後にコールバックを呼ぶ。
- 触るとき: 起動 URI に依存する処理を書くとき。
- 条件付き依存: `if (uriToLoad && uriToLoad.then)` → `uriToLoad.then()`
- 条件付き依存: `if (!(uriToLoad && uriToLoad.then))` → `callback()`
- 参照: `this.uriToLoadPromise`, `uriToLoad.then`

## onUnload()
- 位置: L1060-1164
- 役割: unload 時に進行リスナーの解除、遅延起動の取消または各種オブザーバーの解除を行い、終了用モジュールを呼ぶ。
- 触るとき: ウィンドウ終了時の後始末を追加・変更するとき。
- 呼び出し先: `BrowserUtils.callModulesFromCategory()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "moz-src:///browser/components/genai/LinkPreview.sys.mjs" ).LinkPreview.teardown()`, `gBrowser.removeProgressListener()`, `gBrowser.removeTabsProgressListener()`, `window.docShell.treeOwner .QueryInterface()`, `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (this._boundDelayedStartup)` → `this._cancelDelayedStartup()`
- 条件付き依存: `if (!(this._boundDelayedStartup))` → `BrowserUtils.callModulesFromCategory()`
- 条件付き依存: `if (!(this._boundDelayedStartup))` → `Services.obs.removeObserver()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `this._boundDelayedStartup`, `this._loadHandled`, `this._translationsEnabledStateObserver`, `window.TabsProgressListener`, `window.XULBrowserWindow`, `window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow).XULBrowserWindow`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../netwerk/base/nsIChannel.idl.md) / `Services.obs`
