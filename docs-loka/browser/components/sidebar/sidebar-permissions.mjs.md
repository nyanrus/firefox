# browser/components/sidebar/sidebar-permissions.mjs

source: browser/components/sidebar/sidebar-permissions.mjs
source-hash: 34edfb026102437eaa6774adfbf91caf7cc56938
lines: 734

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## getTabNotificationCount()
- 位置: L18-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.PopupNotifications.getNotificationsForBrowser()`
- 参照: `notifications.length`, `win.PopupNotifications`, `win.gBrowser?.selectedBrowser`

## cancelAllTabNotifications()
- 位置: L34-40
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tabBrowser && win.PopupNotifications)` → `removeNotificationsForBrowser()`
- 参照: `win.PopupNotifications`, `win.gBrowser?.selectedBrowser`

## removeNotificationsForBrowser()
- 位置: L48-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popupNotifications.getNotificationsForBrowser()`
- 条件付き依存: `if (notifications?.length)` → `popupNotifications.remove()`
- 参照: `notifications?.length`

## SidebarPermissions.constructor()
- 位置: L81-83
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#window`

## SidebarPermissions.contentBrowser()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contentBrowser`

## SidebarPermissions.init()
- 位置: L96-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browser.contentDocument.querySelector()`, `this.#browser.contentWindow?.addEventListener()`, `this.#setupPermissionStateListener()`, `this.#setupSidebarPopupNotificationWrapper()`, `this.#sidebarPermissionUI.build()`, `this.#sidebarPermissionUI.setContentBrowser()`
- 条件付き依存: `if (!this.#browser?.contentDocument)` → `console.warn()`
- 条件付き依存: `if (!this.#initialized)` → `this.#bindObservers()`
- 条件付き依存: `if (!this.#initialized)` → `this.onContentBrowserChanged.bind()`
- 条件付き依存: `if (!this.#initialized)` → `win.addEventListener()`
- 条件付き依存: `if (!this.#initialized)` → `this.#uninit()`
- 条件付き依存: `if (!win.SidebarPopupNotifications)` → `this.#setupSidebarPopupNotifications()`
- 条件付き依存: `if (this.#contentBrowser && this.#onPermissionStateChanged)` → `this.#contentBrowser.removeEventListener()`
- 参照: `this.#browser`, `this.#browser?.contentDocument`, `this.#contentBrowser`, `this.#initialized`, `this.#onPermissionStateChanged`, `this.#onSidebarBrowserChanged`, `this.#onSidebarHideEvent`, `this.#sidebarPermissionUI`, `this.#window`, `win.SidebarPopupNotifications`

## this.#onSidebarHideEvent()
- 位置: L135-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onSidebarHidden()`

## SidebarPermissions.onSidebarHidden()
- 位置: L159-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browser?.contentWindow?.removeEventListener()`, `this.#cancelSidebarNotifications()`, `this.#sidebarPermissionUI?.destroy()`, `win.document?.getElementById()`
- 条件付き依存: `if (this.#observerBound)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#popupshowingHandler)` → `panel?.removeEventListener()`
- 条件付き依存: `if (this.#panelOpenHandler)` → `panel?.removeEventListener()`
- 条件付き依存: `if (this.#popuphiddenHandler)` → `panel?.removeEventListener()`
- 条件付き依存: `if (this.#onSidebarBrowserChanged)` → `win.removeEventListener()`
- 条件付き依存: `if (this.#contentBrowser && this.#securityChangeListener)` → `this.#contentBrowser.removeProgressListener()`
- 条件付き依存: `if (this.#contentBrowser && this.#onPermissionStateChanged)` → `this.#contentBrowser.removeEventListener()`
- 参照: `this.#browser`, `this.#contentBrowser`, `this.#contentBrowser._sharingState`, `this.#contentBrowser?._sharingState`, `this.#currentPopupNotificationBrowser`, `this.#observerBound`, `this.#onPermissionStateChanged`, `this.#onSidebarBrowserChanged`, `this.#onSidebarHideEvent`, `this.#panelOpenHandler`, `this.#popuphiddenHandler`, `this.#popupshowingHandler`, `this.#securityChangeListener`, `this.#sidebarPermissionUI`, `this.#window`, `win.SidebarPopupNotifications`, `win.SidebarPopupNotifications._currentAnchorElement`, `win.SidebarPopupNotifications._originalShow`, `win.SidebarPopupNotifications._wrappedBySidebarPermissions`, `win.SidebarPopupNotifications.show`
- XPCOM: `Services.obs`

## SidebarPermissions.#uninit()
- 位置: L248-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sidebarPermissionUI?.destroy()`, `this.onSidebarHidden()`, `win.document?.getElementById()`
- 条件付き依存: `if (this.#contentBrowser && this.#securityChangeListener)` → `this.#contentBrowser.removeProgressListener()`
- 条件付き依存: `if (this.#contentBrowser && this.#securityChangeListener)` → `console.warn()`
- 条件付き依存: `if (this.#contentBrowser && this.#onPermissionStateChanged)` → `this.#contentBrowser.removeEventListener()`
- 条件付き依存: `if (this.#browser?.contentWindow && this.#onSidebarHideEvent)` → `this.#browser.contentWindow.removeEventListener()`
- 条件付き依存: `if (this.#popupshowingHandler)` → `panel?.removeEventListener()`
- 条件付き依存: `if (this.#panelOpenHandler)` → `panel?.removeEventListener()`
- 条件付き依存: `if (this.#popuphiddenHandler)` → `panel?.removeEventListener()`
- 条件付き依存: `if (this.#observerBound)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#onSidebarBrowserChanged)` → `this.#window.removeEventListener()`
- 条件付き依存: `if (win.gPermissionPanel)` → `win.gPermissionPanel.clearBrowserOverride()`
- 参照: `e.message`, `this.#browser`, `this.#browser?.contentWindow`, `this.#contentBrowser`, `this.#currentPopupNotificationBrowser`, `this.#observerBound`, `this.#onPermissionStateChanged`, `this.#onSidebarBrowserChanged`, `this.#onSidebarHideEvent`, `this.#panelOpenHandler`, `this.#popuphiddenHandler`, `this.#popupshowingHandler`, `this.#securityChangeListener`, `this.#sidebarPermissionUI`, `this.#window`, `win.SidebarPopupNotifications`, `win.gPermissionPanel`
- XPCOM: `Services.obs`

## SidebarPermissions.#setupSidebarPopupNotifications()
- 位置: L341-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `chromeDoc.getElementById()`, `panel.addEventListener()`, `this.#wrapSidebarShow()`
- 参照: `lazy.PopupNotifications`, `this.#browser`, `this.#currentPopupNotificationBrowser`, `this.#panelOpenHandler`, `this.#popuphiddenHandler`, `this.#popupshowingHandler`, `this.#window`, `win.SidebarPopupNotifications`, `win.document`

## SidebarPermissions.getVisibleAnchorElement()
- 位置: L353-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorElement?.checkVisibility()`, `micAnchor?.checkVisibility()`, `sidebarDocument?.getElementById()`
- 参照: `lazy.PopupNotifications.CHECK_VISIBILITY_OPTIONS`, `win.SidebarController?.browser?.contentDocument`

## this.#popupshowingHandler()
- 位置: L387-396
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (isSidebarNotification)` → `this.#sidebarPermissionUI.showMicRequestUI()`
- 参照: `firstChild?.notification?.browser`, `panel.firstElementChild`, `this.#contentBrowser`, `this.#currentPopupNotificationBrowser`

## this.#panelOpenHandler()
- 位置: L398-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handlePopupChange()`

## this.#popuphiddenHandler()
- 位置: L402-411
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#currentPopupNotificationBrowser === this.#contentBrowser)` → `this.#onSidebarPopupNotificationHidden()`
- 参照: `this.#contentBrowser`, `this.#currentPopupNotificationBrowser`, `win.SidebarPopupNotifications?._isShowing`

## SidebarPermissions.#handlePopupChange()
- 位置: L421-435
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!isSidebarNotification)` → `this.#cancelSidebarNotifications()`
- 参照: `firstChild?.notification?.browser`, `panel.firstElementChild`, `panel.state`, `this.#contentBrowser`, `this.#currentPopupNotificationBrowser`

## SidebarPermissions.#setupSidebarPopupNotificationWrapper()
- 位置: L441-448
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (win.SidebarPopupNotifications)` → `this.#wrapSidebarShow()`
- 参照: `this.#window`, `win.SidebarPopupNotifications`

## SidebarPermissions.#onSidebarPopupNotificationHidden()
- 位置: L453-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cancelSidebarNotifications()`, `this.updatePermissionIcons()`

## SidebarPermissions.#cancelSidebarNotifications()
- 位置: L461-470
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#contentBrowser && win.SidebarPopupNotifications)` → `removeNotificationsForBrowser()`
- 参照: `this.#contentBrowser`, `this.#window`, `win.SidebarPopupNotifications`

## SidebarPermissions.#wrapSidebarShow()
- 位置: L478-534
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `sidebarInstance._isShowing`, `sidebarInstance._originalShow`, `sidebarInstance._wrappedBySidebarPermissions`, `sidebarInstance.show`, `this.#window`

## sidebarInstance.show()
- 位置: L489-530
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabNotificationCount()`, `originalShow.call()`, `win.document.getElementById()`
- 条件付き依存: `if (tabNotificationCount >= 1)` → `cancelAllTabNotifications()`
- 条件付き依存: `if (tabNotificationCount > 1 && panel)` → `showAfterHidden()`
- 参照: `sidebarInstance._isShowing`

## showAfterHidden()
- 位置: async L505-522
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalShow.call()`
- 条件付き依存: `if (panel && panel.state === "closed")` → `panel.addEventListener()`
- 条件付き依存: `if (!(panel && panel.state === "closed"))` → `resolve()`
- 参照: `panel.state`, `sidebarInstance._isShowing`

## SidebarPermissions.#bindObservers()
- 位置: L536-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.#observerBound`
- XPCOM: `Services.obs`

## SidebarPermissions.observe()
- 位置: L545-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onPermissionChanged()`

## SidebarPermissions.onContentBrowserChanged()
- 位置: L553-620
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browser?.contentDocument?.querySelector()`, `this.#cancelSidebarNotifications()`, `this.#sidebarPermissionUI.setContentBrowser()`, `this.#sidebarPermissionUI?.clearUI()`
- 条件付き依存: `if (this.#contentBrowser && this.#onPermissionStateChanged)` → `this.#contentBrowser.removeEventListener()`
- 条件付き依存: `if (this.#contentBrowser && this.#securityChangeListener)` → `this.#contentBrowser.removeProgressListener()`
- 条件付き依存: `if (this.#contentBrowser && this.#securityChangeListener)` → `console.warn()`
- 条件付き依存: `if (this.#contentBrowser)` → `ChromeUtils.generateQI()`
- 条件付き依存: `if (this.#contentBrowser)` → `this.#contentBrowser.addProgressListener()`
- 条件付き依存: `if (this.#contentBrowser)` → `this.#setupPermissionStateListener()`
- 条件付き依存: `if (win.gPermissionPanel)` → `win.gPermissionPanel.clearBrowserOverride()`
- 参照: `Ci.nsIWebProgress.NOTIFY_SECURITY`, `e.message`, `this.#contentBrowser`, `this.#onPermissionStateChanged`, `this.#securityChangeListener`, `this.#window`, `win.gPermissionPanel`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## SidebarPermissions.onSecurityChange()
- 位置: L592-601
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_self.updatePermissionIcons()`
- 参照: `_self.#contentBrowser?.contentPrincipal?.origin`, `this._previousOrigin`

## SidebarPermissions.#onPermissionChanged()
- 位置: L622-645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subject.QueryInterface()`, `this.#sidebarPermissionUI.isIdentityBoxOpen()`, `this.#sidebarPermissionUI?.isReady()`, `this.updatePermissionIcons()`
- 参照: `Ci.nsIPermission`, `permission.principal?.origin`, `permission.type`, `sidebarPrincipal?.origin`, `this.#contentBrowser?.contentPrincipal`
- XPCOM: [`nsIPermission`](../../../netwerk/base/nsIPermission.idl.md)

## SidebarPermissions.#setupPermissionStateListener()
- 位置: L647-667
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contentBrowser.addEventListener()`
- 参照: `this.#contentBrowser`, `this.#onPermissionStateChanged`

## this.#onPermissionStateChanged()
- 位置: L652-659
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currentBrowser === this.#contentBrowser)` → `this.updatePermissionIcons()`
- 参照: `event.target`, `this.#contentBrowser`

## SidebarPermissions.updatePermissionIcons()
- 位置: L673-710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SitePermissions.getAllForBrowser()`, `matchingMicPermissions.some()`, `p.id.startsWith()`, `permissions.filter()`, `this.#sidebarPermissionUI.clearUI()`
- 条件付き依存: `if (!permissions.length)` → `this.#sidebarPermissionUI.clearUI()`
- 条件付き依存: `if ( matchingMicPermissions.some(p => p.state === lazy.SitePermissions.BLOCK) )` → `this.#sidebarPermissionUI.showBlockedUI()`
- 条件付き依存: `if ( matchingMicPermissions.some(p => p.state === lazy.SitePermissions.ALLOW) )` → `this.#sidebarPermissionUI.showGrantedUI()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `p.id`, `p.state`, `permissions.length`, `this.#contentBrowser`

## SidebarPermissions.showMicRequestUI()
- 位置: L712-714
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sidebarPermissionUI.showMicRequestUI()`

## SidebarPermissions.showGrantedUI()
- 位置: L721-723
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sidebarPermissionUI.showGrantedUI()`

## SidebarPermissions.updateFromBrowserState()
- 位置: L730-732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sidebarPermissionUI?.updateFromBrowserState()`
