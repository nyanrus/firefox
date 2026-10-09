# browser/modules/ExtensionsUI.sys.mjs

source: browser/modules/ExtensionsUI.sys.mjs
source-hash: 73ef024602cb4554a024de4ddef83f492adc33ef
lines: 890

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `EventEmitter.decorate()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## getTabBrowser()
- 位置: L48-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getAttribute()`
- 参照: `Ci.nsIDocShell.typeChrome`, `browser.documentGlobal`, `browser.documentGlobal.docShell.chromeEventHandler`, `browser.documentGlobal.docShell.itemType`, `window.browsingContext.topChromeWindow`, `window.gBrowser.selectedBrowser`
- XPCOM: [`nsIDocShell`](../../docshell/base/nsIDocShell.idl.md)

## init()
- 位置: async L72-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.wm.getMostRecentWindow()`, `this._checkForSideloaded()`
- 参照: `Services.wm.getMostRecentWindow("navigator:browser") .delayedStartupPromise`
- XPCOM: `Services.obs` / `Services.wm`

## _checkForSideloaded()
- 位置: async L88-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.id.localeCompare()`, `lazy.AddonManagerPrivate.getNewSideloads()`, `sideloaded.sort()`, `this._updateNotifications()`, `this.sideloaded.add()`
- 条件付き依存: `if (!this.sideloadListener)` → `lazy.AddonManager.addAddonListener()`
- 参照: `b.id`, `sideloaded.length`, `this.sideloadListener`

## onEnabled()
- 位置: L102-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateNotifications()`, `this.sideloaded.delete()`, `this.sideloaded.has()`
- 条件付き依存: `if (this.sideloaded.size == 0)` → `lazy.AddonManager.removeAddonListener()`
- 参照: `this.sideloadListener`, `this.sideloaded.size`

## _updateNotifications()
- 位置: L125-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`
- 条件付き依存: `if (importedAddonIDs.length + sideloaded.size + updates.size == 0)` → `lazy.AppMenuNotifications.removeNotification()`
- 条件付き依存: `if (!(importedAddonIDs.length + sideloaded.size + updates.size == 0))` → `lazy.AppMenuNotifications.showBadgeOnlyNotification()`
- 参照: `importedAddonIDs.length`, `lazy.AMBrowserExtensionsImport`, `sideloaded.size`, `updates.size`

## showAddonsManager()
- 位置: L137-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `global.BrowserAddonUI.openAddonsMgr()`, `global.BrowserAddonUI.openAddonsMgr("addons://list/extension").then()`, `this.showPermissionsPrompt()`
- 参照: `aomWin.docShell.chromeEventHandler`, `tabbrowser.selectedBrowser.documentGlobal`

## showSideloaded()
- 位置: L160-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addon.markAsSeen()`, `lazy.AMTelemetry.recordManageEvent()`, `this._buildStrings()`, `this._updateNotifications()`, `this.emit()`, `this.showAddonsManager()`, `this.sideloaded.delete()`
- 条件付き依存: `if (answer)` → `addon.enable()`
- 条件付き依存: `if (answer)` → `this._updateNotifications()`
- 参照: `addon.iconURL`, `addon.installPermissions`, `lazy.dataCollectionPermissionsEnabled`, `strings.msgs.length`

## showUpdate()
- 位置: L190-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AMTelemetry.recordInstallEvent()`, `this._updateNotifications()`, `this.showAddonsManager()`, `this.showAddonsManager(browser, info.strings, info.addon.iconURL).then()`, `this.updates.delete()`
- 条件付き依存: `if (answer)` → `info.resolve()`
- 条件付き依存: `if (!(answer))` → `info.reject()`
- 参照: `info.addon.iconURL`, `info.install`, `info.strings`, `info.strings.msgs.length`

## observe()
- 位置: L211-404
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `getTabBrowser()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `window.PopupNotifications.getNotification()`
- 条件付き依存: `if (progressNotification)` → `progressNotification.remove()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( info.unsigned && (Cu.isInAutomation || !AppConstants.MOZILLA_OFFICIAL) && Services.prefs.getBoolPref( "extensions.ui.disableUnsignedWarnings", false ) )` → `lazy.logConsole.warn()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `this._buildStrings()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `console.error()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `info.reject()`
- 条件付き依存: `if ( info.type == "update" && !strings.msgs.length && !strings.dataCollectionPermissions?.msg )` → `info.resolve()`
- 条件付き依存: `if (info.type == "sideload")` → `lazy.AMTelemetry.recordManageEvent()`
- 条件付き依存: `if (!(info.type == "sideload"))` → `lazy.AMTelemetry.recordInstallEvent()`
- 条件付き依存: `if (topic == "webextension-permission-prompt")` → `this.showPermissionsPrompt()`
- 条件付き依存: `if (answer)` → `info.resolve()`
- 条件付き依存: `if (!(answer))` → `info.reject()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `this._buildStrings()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `console.error()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `info.reject()`
- 条件付き依存: `if (!strings.msgs.length && !strings.dataCollectionPermissions?.msg)` → `info.resolve()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `this.updates.add()`
- 条件付き依存: `if (topic == "webextension-update-permission-prompt")` → `this._updateNotifications()`
- 条件付き依存: `if (topic == "webextension-install-notify")` → `this.showInstallNotification(target, addon).then()`
- 条件付き依存: `if (topic == "webextension-install-notify")` → `this.showInstallNotification()`
- 条件付き依存: `if (callback)` → `callback()`
- 条件付き依存: `if (topic == "webextension-optional-permission-prompt")` → `this._buildStrings()`
- 条件付き依存: `if (!strings.msgs.length && !strings.dataCollectionPermissions?.msg)` → `resolve()`
- 条件付き依存: `if (topic == "webextension-optional-permission-prompt")` → `resolve()`
- 条件付き依存: `if (topic == "webextension-optional-permission-prompt")` → `this.showPermissionsPrompt()`
- 条件付き依存: `if (topic == "webextension-defaultsearch-prompt")` → `lazy.l10n.formatMessagesSync()`
- 条件付き依存: `if (topic == "webextension-defaultsearch-prompt")` → `this.showDefaultSearchPrompt(browser, strings, icon).then()`
- 条件付き依存: `if (topic == "webextension-defaultsearch-prompt")` → `this.showDefaultSearchPrompt()`
- 条件付き依存: `if ( [ "webextension-imported-addons-cancelled", "webextension-imported-addons-complete", "webextension-imported-addons-pending", ].includes(topic) )` → `this._updateNotifications()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `Cu.isInAutomation`, `attr.name`, `attr.value`, `info.addon`, `info.addon.id`, `info.addon.signedState`, `info.icon`, `info.install`, `info.permissions`, `info.reject`, `info.resolve`, `info.type`, `info.unsigned`, `lazy.AddonManager.SIGNEDSTATE_MISSING`, `lazy.dataCollectionPermissionsEnabled`, `permissions.permissions`, `permissions.permissions.length`, `searchDesc.value`, `searchNo.attributes`, `searchYes.attributes`, `strings.acceptKey`, `strings.acceptText`, `strings.cancelKey`, `strings.cancelText`, `strings.dataCollectionPermissions?.msg`, `strings.msgs.length`, `subject.wrappedJSObject`
- XPCOM: `Services.prefs`

## _buildStrings()
- 位置: L407-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionData.formatPermissionStrings()`
- 参照: `info.addon.name`, `strings.addonName`

## showPermissionsPrompt()
- 位置: async L420-630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.all(promises).then()`, `Services.urlFormatter.formatURLPref()`, `browser.documentGlobal.gUnifiedExtensions.getPopupAnchorID()`, `getTabBrowser()`, `lazy.AddonManager.getAddonByID()`, `lazy.ExtensionPermissions.remove()`, `lazy.ExtensionPermissions.remove(addon.id, perms).catch()`, `lazy.logConsole.warn()`, `permsToUpdate.map()`, `promise.finally()`, `promise.then()`, `strings.header.includes()`, `this.pendingNotifications.delete()`, `this.pendingNotifications.get()`, `this.pendingNotifications.set()`, `window.PopupNotifications.show()`
- 条件付き依存: `if ( showIncognitoCheckbox && // Usually false, unless the user tries to install a XPI file whose ID // matches an already-installed add-on. (await lazy.AddonMan...)` → `lazy.ExtensionPermissions.get()`
- 条件付き依存: `if ( showIncognitoCheckbox && // Usually false, unless the user tries to install a XPI file whose ID // matches an already-installed add-on. (await lazy.AddonMan...)` → `permissions.includes()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `permsToUpdate.push()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `permsToUpdate.push()`
- 条件付き依存: `if (value)` → `lazy.ExtensionPermissions.add(addon.id, perms).catch()`
- 条件付き依存: `if (value)` → `lazy.ExtensionPermissions.add()`
- 条件付き依存: `if (value)` → `lazy.logConsole.warn()`
- 参照: `addon.id`, `addon.permissions`, `lazy.AddonManager.PERM_CAN_CHANGE_PRIVATEBROWSING_ACCESS`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `options.name`, `strings.acceptKey`, `strings.acceptText`, `strings.addonName`, `strings.cancelKey`, `strings.cancelText`, `strings.dataCollectionPermissions?.collectsTechnicalAndInteractionData`, `strings.dataCollectionPermissions?.msg`, `strings.header`, `strings.msgs.length`
- XPCOM: `Services.urlFormatter`

## eventCallback()
- 位置: L471-481
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "removed")` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (topic == "removed")` → `resolve()`
- XPCOM: `Services.tm`

## onPrivateBrowsingAllowedChanged()
- 位置: L519-521
- 役割: (未記入)
- 触るとき: (未記入)

## onTechnicalAndInteractionDataChanged()
- 位置: L524-526
- 役割: (未記入)
- 触るとき: (未記入)

## callback()
- 位置: L548-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## callback()
- 位置: L556-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## showDefaultSearchPrompt()
- 位置: L632-676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabBrowser()`, `window.PopupNotifications.show()`
- 参照: `strings.acceptKey`, `strings.acceptText`, `strings.addonName`, `strings.cancelKey`, `strings.cancelText`, `strings.text`

## eventCallback()
- 位置: L639-643
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == "removed")` → `resolve()`

## callback()
- 位置: L650-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## callback()
- 位置: L658-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`

## showInstallNotification()
- 位置: async L678-760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getTabBrowser()`, `lazy.AddonManager.getPreferredIconURL()`, `lazy.l10n.formatValue()`
- 条件付き依存: `if (addon.type == "theme")` → `lazy.AppMenuNotifications.showNotification()`
- 条件付き依存: `if (!(addon.type == "theme"))` → `lazy.AppMenuNotifications.showNotification()`
- 参照: `addon.id`, `addon.isWebExtension`, `addon.name`, `addon.type`

## themeActionUndo()
- 位置: async L694-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addon.uninstall()`, `lazy.AddonManager.getAddonByID()`, `resolve()`
- 条件付き依存: `if (theme)` → `theme.enable()`

## onDismissed()
- 位置: L724-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AppMenuNotifications.removeNotification()`, `resolve()`

## onDismissed()
- 位置: L744-747
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AppMenuNotifications.removeNotification()`, `resolve()`

## showQuarantineConfirmation()
- 位置: async L762-792
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionsUI.showPermissionsPrompt()`, `attr()`, `lazy.l10n.formatMessages()`, `policy.extension?.getPreferredIcon()`
- 条件付き依存: `if (await ExtensionsUI.showPermissionsPrompt(browser, strings, icon))` → `lazy.QuarantinedDomains.setUserAllowedAddonIdPref()`
- 参照: `line1.value`, `line2.value`, `policy.id`, `policy.name`, `title.value`

## attr()
- 位置: L774-774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `msg.attributes.find()`
- 参照: `a.name`, `msg.attributes.find(a => a.name === name)?.value`

## originControlsMenu()
- 位置: L795-886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`, `doc.createXULElement()`, `headerItem.setAttribute()`, `items.forEach()`, `items.push()`, `lazy.OriginControls.getState()`, `popup.addEventListener()`, `popup.insertBefore()`, `popup.querySelector()`
- 条件付き依存: `if (state.noAccess)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (!(state.noAccess))` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.quarantined)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.quarantined)` → `doc.createXULElement()`
- 条件付き依存: `if (state.quarantined)` → `allowQuarantined.addEventListener()`
- 条件付き依存: `if (state.quarantined)` → `this.showQuarantineConfirmation()`
- 条件付き依存: `if (state.quarantined)` → `items.push()`
- 条件付き依存: `if (state.allDomains)` → `doc.createXULElement()`
- 条件付き依存: `if (state.allDomains)` → `allDomains.setAttribute()`
- 条件付き依存: `if (state.allDomains)` → `allDomains.toggleAttribute()`
- 条件付き依存: `if (state.allDomains)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.allDomains)` → `items.push()`
- 条件付き依存: `if (state.whenClicked)` → `doc.createXULElement()`
- 条件付き依存: `if (state.whenClicked)` → `whenClicked.setAttribute()`
- 条件付き依存: `if (state.whenClicked)` → `whenClicked.toggleAttribute()`
- 条件付き依存: `if (state.whenClicked)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.whenClicked)` → `whenClicked.addEventListener()`
- 条件付き依存: `if (state.whenClicked)` → `lazy.OriginControls.setWhenClicked()`
- 条件付き依存: `if (state.whenClicked)` → `win.gUnifiedExtensions.updateAttention()`
- 条件付き依存: `if (state.whenClicked)` → `items.push()`
- 条件付き依存: `if (state.alwaysOn)` → `doc.createXULElement()`
- 条件付き依存: `if (state.alwaysOn)` → `alwaysOn.setAttribute()`
- 条件付き依存: `if (state.alwaysOn)` → `alwaysOn.toggleAttribute()`
- 条件付き依存: `if (state.alwaysOn)` → `doc.l10n.setAttributes()`
- 条件付き依存: `if (state.alwaysOn)` → `alwaysOn.addEventListener()`
- 条件付き依存: `if (state.alwaysOn)` → `lazy.OriginControls.setAlwaysOn()`
- 条件付き依存: `if (state.alwaysOn)` → `win.gUnifiedExtensions.updateAttention()`
- 条件付き依存: `if (state.alwaysOn)` → `items.push()`
- 参照: `policy?.extension.originControls`, `popup.documentGlobal`, `popup.ownerDocument`, `state.allDomains`, `state.alwaysOn`, `state.hasAccess`, `state.noAccess`, `state.quarantined`, `state.whenClicked`, `tab.linkedBrowser`, `tab.linkedBrowser?.currentURI`, `uri.host`, `win.gBrowser.selectedTab`

## cleanup()
- 位置: L879-884
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.target === popup)` → `items.forEach()`
- 条件付き依存: `if (e.target === popup)` → `item?.remove()`
- 条件付き依存: `if (e.target === popup)` → `popup.removeEventListener()`
- 参照: `e.target`
