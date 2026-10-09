# browser/modules/PopupAndRedirectBlockerObserver.sys.mjs

source: browser/modules/PopupAndRedirectBlockerObserver.sys.mjs
source-hash: b82d0cbd94a5d8e3055cbf25aaa5f9fa17f38bb0
lines: 416

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## handleEvent()
- 位置: L16-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onCommand()`, `this.onDOMUpdateBlockedPopupsAndRedirect()`, `this.onPopupHiding()`, `this.onPopupShowing()`
- 参照: `aEvent.type`

## onDOMUpdateBlockedPopupsAndRedirect()
- 位置: L42-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.getBlockedPopupCount()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.isRedirectBlocked()`, `gPermissionPanel.refreshPermissionIcons()`
- 条件付き依存: `if (!popupCount && !isRedirectBlocked)` → `this.hideNotification()`
- 条件付き依存: `if (Services.prefs.getBoolPref("privacy.popups.showBrowserMessage"))` → `this.ensureInitializedForWindow()`
- 条件付き依存: `if (Services.prefs.getBoolPref("privacy.popups.showBrowserMessage"))` → `this.showBrowserMessage()`
- 参照: `aEvent.originalTarget`, `aEvent.originalTarget.documentGlobal`, `gBrowser.selectedBrowser`
- XPCOM: `Services.prefs`

## hideNotification()
- 位置: L66-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.getNotificationBox()`, `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `notificationBox.removeNotification()`

## ensureInitializedForWindow()
- 位置: L75-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.getElementById()`, `popup.addEventListener()`, `popup.getAttribute()`, `popup.setAttribute()`

## showBrowserMessage()
- 位置: async L88-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `popupAndRedirectBlocker.eventCallback.bind()`, `popupAndRedirectBlocker.hasBeenDismissed()`
- 参照: `aBrowser.selectedBrowser`, `notification.label`, `notificationBox.PRIORITY_INFO_MEDIUM`, `selectedBrowser.popupAndRedirectBlocker`, `this.mNotificationPromise`, `this.maxReportedPopups`

## onPopupShowing()
- 位置: async L151-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `blockedPopupDontShowMessage.removeAttribute()`, `document.getElementById()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedPopups()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedPopups() .then()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedRedirect()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker .getBlockedRedirect() .then()`, `this.onPopupShowingBlockedPopups()`, `this.onPopupShowingBlockedRedirect()`
- 条件付き依存: `if (Services.prefs.prefIsLocked("dom.disable_open_during_load"))` → `blockedPopupAllowSite.setAttribute()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("dom.disable_open_during_load")))` → `blockedPopupAllowSite.removeAttribute()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("dom.disable_open_during_load")))` → `document.l10n.setAttributes()`
- 参照: `aEvent.originalTarget.documentGlobal`, `browser.contentPrincipal`, `browser.currentURI`, `browser.isContentPrincipal`, `gBrowser.selectedBrowser`, `uriOrPrincipal.asciiHost`, `uriOrPrincipal.displayHost`, `uriOrPrincipal.spec`
- XPCOM: `Services.prefs`

## onPopupShowingBlockedRedirect()
- 位置: L198-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blockedRedirectSeparator.after()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `menuitem.setAttribute()`, `nextElement?.hasAttribute()`
- 参照: `aBlockedRedirect.browsingContext`, `aBlockedRedirect.innerWindowId`, `aBlockedRedirect.redirectURISpec`, `blockedRedirectSeparator.hidden`, `blockedRedirectSeparator.nextElementSibling`, `gBrowser.selectedBrowser`, `menuitem.browser`, `menuitem.browsingContext`

## onPopupShowingBlockedPopups()
- 位置: L239-281
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blockedPopupsSeparator.after()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `menuitem.setAttribute()`, `nextElement?.hasAttribute()`
- 参照: `aBlockedPopups.length`, `blockedPopup.browsingContext`, `blockedPopup.innerWindowId`, `blockedPopup.popupWindowURISpec`, `blockedPopup.reportIndex`, `blockedPopupsSeparator.hidden`, `blockedPopupsSeparator.nextElementSibling`, `gBrowser.selectedBrowser`, `menuitem.browser`, `menuitem.browsingContext`

## onPopupHiding()
- 位置: L289-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `item.remove()`, `item?.hasAttribute()`
- 条件付き依存: `if (item?.hasAttribute("redirectInnerWindowId"))` → `item.remove()`
- 参照: `aEvent.originalTarget.documentGlobal`, `blockedPopupsSeparator.nextElementSibling`, `blockedRedirectSeparator.nextElementSibling`, `item.nextElementSibling`

## onCommand()
- 位置: L323-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.hasAttribute()`, `this.dontShowMessage()`, `this.editPopupSettings()`, `this.toggleAllowPopupsForSite()`
- 条件付き依存: `if (aEvent.target.hasAttribute("popupReportIndex"))` → `this.showBlockedPopup()`
- 条件付き依存: `if (aEvent.target.hasAttribute("redirectURISpec"))` → `this.navigateToBlockedRedirect()`
- 参照: `aEvent.target.id`

## showBlockedPopup()
- 位置: L347-357
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.getAttribute()`, `browser.popupAndRedirectBlocker.unblockPopup()`
- 参照: `aEvent.target`

## navigateToBlockedRedirect()
- 位置: L359-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.getAttribute()`, `browser.popupAndRedirectBlocker.unblockRedirect()`
- 参照: `aEvent.target`

## toggleAllowPopupsForSite()
- 位置: async L371-393
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.addFromPrincipal()`, `Services.prefs.prefIsLocked()`, `gBrowser.getNotificationBox()`, `gBrowser.getNotificationBox().removeCurrentNotification()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockAllPopups()`, `gBrowser.selectedBrowser.popupAndRedirectBlocker.unblockFirstRedirect()`
- 参照: `Services.perms.ALLOW_ACTION`, `aEvent.originalTarget.documentGlobal`, `gBrowser.contentPrincipal`
- XPCOM: `Services.perms` / `Services.prefs`

## editPopupSettings()
- 位置: L395-400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openPreferences()`
- 参照: `aEvent.originalTarget.documentGlobal`

## dontShowMessage()
- 位置: L402-408
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `gBrowser.getNotificationBox()`, `gBrowser.getNotificationBox().removeCurrentNotification()`
- 参照: `aEvent.originalTarget.documentGlobal`
- XPCOM: `Services.prefs`
