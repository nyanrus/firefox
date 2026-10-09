# browser/base/content/browser-addons.js

source: browser/base/content/browser-addons.js
source-hash: d380089ca59a0728e9378503934b4c6c0432b8af
lines: 3406

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `customElements.define()`, `customElements.get()`

## MozAddonNotificationBlocklistURL.connectedCallback()
- 位置: L108-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addEventListener()`

## MozAddonNotificationBlocklistURL.disconnectedCallback()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.removeEventListener()`

## MozAddonNotificationBlocklistURL.handleEvent()
- 位置: L116-125
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.type == "click")` → `e.preventDefault()`
- 条件付き依存: `if (e.type == "click")` → `window.openTrustedLinkIn()`
- 参照: `e.type`, `this.href`

## MozAddonPermissionsNotification.show()
- 位置: L135-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.show()`, `this.querySelector()`, `this.render()`
- 参照: `this.introEl`, `this.notification`, `this.notification.options?.customElementOptions`, `this.permsListDataCollectionEl`, `this.permsListEl`, `this.permsListOptionalEl`, `this.permsTitleDataCollectionEl`, `this.permsTitleEl`, `this.permsTitleOptionalEl`, `this.textEl`

## MozAddonPermissionsNotification.hasNoPermissions()
- 位置: L170-183
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `strings.msgs.length`, `this.#dataCollectionPermissions?.msg`, `this.notification.options.customElementOptions`

## MozAddonPermissionsNotification.domainsSet()
- 位置: L185-191
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `strings.fullDomainsList?.domainsSet`, `this.notification.options.customElementOptions`, `this.notification?.options?.customElementOptions`

## MozAddonPermissionsNotification.hasFullDomainsList()
- 位置: L193-195
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.domainsSet?.size`

## MozAddonPermissionsNotification.#isFullDomainsListEntryIndex()
- 位置: L197-203
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `strings.fullDomainsList.msgIdIndex`, `this.hasFullDomainsList`, `this.notification.options.customElementOptions`

## MozAddonPermissionsNotification.#dataCollectionPermissions()
- 位置: L209-215
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `strings.dataCollectionPermissions`, `this.notification.options.customElementOptions`, `this.notification?.options?.customElementOptions`

## MozAddonPermissionsNotification.render()
- 位置: L217-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#clearChildElements()`, `this.#setAllowButtonEnabled()`
- 条件付き依存: `if (strings.text)` → `strings.text.includes()`
- 条件付き依存: `if (strings.text.includes("\n\n"))` → `textEl.classList.add()`
- 条件付き依存: `if (isUserScriptsRequest)` → `this.#createUserScriptsPermissionItems()`
- 条件付き依存: `if (isUserScriptsRequest)` → `this.#setAllowButtonEnabled()`
- 条件付き依存: `if (isUserScriptsRequest)` → `doc.createElementNS()`
- 条件付き依存: `if (isUserScriptsRequest)` → `item.append()`
- 条件付き依存: `if (isUserScriptsRequest)` → `item.classList.add()`
- 条件付き依存: `if (isUserScriptsRequest)` → `permsListEl.append()`
- 条件付き依存: `if (strings.msgs.length)` → `strings.msgs.entries()`
- 条件付き依存: `if (strings.msgs.length)` → `doc.createElementNS()`
- 条件付き依存: `if (strings.msgs.length)` → `item.classList.add()`
- 条件付き依存: `if (strings.msgs.length)` → `this.#isFullDomainsListEntryIndex()`
- 条件付き依存: `if ( this.hasFullDomainsList && this.#isFullDomainsListEntryIndex(idx) )` → `item.append()`
- 条件付き依存: `if ( this.hasFullDomainsList && this.#isFullDomainsListEntryIndex(idx) )` → `this.#createFullDomainsListFragment()`
- 条件付き依存: `if (strings.msgs.length)` → `permsListEl.appendChild()`
- 条件付き依存: `if (this.#dataCollectionPermissions?.msg)` → `doc.createElementNS()`
- 条件付き依存: `if (this.#dataCollectionPermissions?.msg)` → `item.classList.add()`
- 条件付き依存: `if (this.#dataCollectionPermissions?.msg)` → `permsListDataCollectionEl.appendChild()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `doc.createElementNS()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `item.classList.add()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `item.appendChild()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `this.#createTechnicalAndInteractionDataCheckbox()`
- 条件付き依存: `if (showTechnicalAndInteractionCheckbox)` → `permsListOptionalEl.appendChild()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `doc.createElementNS()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `item.classList.add()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `item.appendChild()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `this.#createPrivateBrowsingCheckbox()`
- 条件付き依存: `if (showIncognitoCheckbox)` → `permsListOptionalEl.appendChild()`
- 参照: `introEl.hidden`, `introEl.textContent`, `item.textContent`, `permsListDataCollectionEl.hidden`, `permsListEl.hidden`, `permsListOptionalEl.hidden`, `permsTitleDataCollectionEl.hidden`, `permsTitleDataCollectionEl.textContent`, `permsTitleEl.hidden`, `permsTitleEl.textContent`, `permsTitleOptionalEl.hidden`, `permsTitleOptionalEl.textContent`, `strings.listIntro`, `strings.msgs`, `strings.msgs.length`, `strings.sectionHeaders`, `strings.text`, `textEl.hidden`, `textEl.textContent`, `this.#dataCollectionPermissions.msg`, `this.#dataCollectionPermissions?.msg`, `this.hasFullDomainsList`, `this.hasNoPermissions`, `this.notification.options.customElementOptions`, `this.ownerDocument`

## MozAddonPermissionsNotification.#createFullDomainsListFragment()
- 位置: L356-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createElementNS()`, `doc.createXULElement()`, `domainsList.appendChild()`, `domainsList.classList.add()`, `fragment.append()`
- 条件付き依存: `if (this.domainsSet.size > 5)` → `domainsList.classList.add()`
- 参照: `domainItem.textContent`, `label.value`, `this.documentGlobal`, `this.domainsSet`, `this.domainsSet.size`, `this.ownerDocument`

## MozAddonPermissionsNotification.#clearChildElements()
- 位置: L382-419
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `textEl.classList.remove()`
- 参照: `introEl.hidden`, `introEl.textContent`, `list.hidden`, `list.textContent`, `textEl.hidden`, `textEl.textContent`, `title.hidden`

## MozAddonPermissionsNotification.#createUserScriptsPermissionItems()
- 位置: L421-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkboxEl.addEventListener()`, `lazy.PERMISSION_L10N.formatValueSync()`, `this.#setAllowButtonEnabled()`, `this.ownerDocument.createElement()`, `warningEl.setAttribute()`
- 参照: `checkboxEl.checked`, `checkboxEl.label`

## MozAddonPermissionsNotification.#setAllowButtonEnabled()
- 位置: L442-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleAttribute()`

## MozAddonPermissionsNotification.#createPrivateBrowsingCheckbox()
- 位置: L462-482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkboxEl.addEventListener()`, `onPrivateBrowsingAllowedChanged()`, `this.ownerDocument.createElement()`, `this.ownerDocument.l10n.setAttributes()`
- 参照: `checkboxEl.checked`, `this.notification.options.customElementOptions`

## MozAddonPermissionsNotification.#createTechnicalAndInteractionDataCheckbox()
- 位置: L484-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkboxEl.addEventListener()`, `onTechnicalAndInteractionDataChanged()`, `this.ownerDocument.createElement()`, `this.ownerDocument.l10n.setAttributes()`
- 参照: `checkboxEl.checked`, `this.notification.options.customElementOptions`

## MozAddonProgressNotification.show()
- 位置: L515-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aInstall.addListener()`, `document.getElementById()`, `setTimeout()`, `super.show()`, `this.notification.options.installs.forEach()`, `this.setProgress()`, `this.updateProgress.bind()`
- 参照: `this._updateProgressTimeout`, `this.notification`, `this.progressmeter`, `this.progresstext`

## MozAddonProgressNotification.disconnectedCallback()
- 位置: L545-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.destroy()`

## MozAddonProgressNotification.destroy()
- 位置: L549-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aInstall.removeListener()`, `clearTimeout()`, `this.notification.options.installs.forEach()`
- 参照: `this._updateProgressTimeout`, `this.notification`

## MozAddonProgressNotification.setProgress()
- 位置: L560-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `DownloadUtils.getDownloadStatus()`, `Math.max()`, `this.progresstext.setAttribute()`
- 条件付き依存: `if (aMaxProgress == -1)` → `this.progressmeter.removeAttribute()`
- 条件付き依存: `if (!(aMaxProgress == -1))` → `this.progressmeter.setAttribute()`
- 参照: `this.notification.last`, `this.notification.lastProgress`, `this.notification.lastUpdate`, `this.notification.speed`

## MozAddonProgressNotification.cancel()
- 位置: L608-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PopupNotifications.remove()`, `aInstall.cancel()`, `installs.forEach()`
- 参照: `this.notification`, `this.notification.options.installs`

## MozAddonProgressNotification.updateProgress()
- 位置: L621-652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.notification.options.installs.forEach()`
- 条件付き依存: `if (downloadingCount == 0)` → `this.destroy()`
- 条件付き依存: `if (downloadingCount == 0)` → `this.progressmeter.removeAttribute()`
- 条件付き依存: `if (downloadingCount == 0)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (downloadingCount == 0)` → `this.progresstext.setAttribute()`
- 条件付き依存: `if (!(downloadingCount == 0))` → `this.setProgress()`
- 参照: `AddonManager.STATE_DOWNLOADED`, `aInstall.maxProgress`, `aInstall.progress`, `aInstall.state`, `this.notification`

## MozAddonProgressNotification.onDownloadProgress()
- 位置: L654-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateProgress()`

## MozAddonProgressNotification.onDownloadFailed()
- 位置: L658-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateProgress()`

## MozAddonProgressNotification.onDownloadCancelled()
- 位置: L662-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateProgress()`

## MozAddonProgressNotification.onDownloadEnded()
- 位置: L666-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateProgress()`

## extensionPolicy()
- 位置: L678-680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`
- 参照: `this.extensionId`

## extensionName()
- 位置: L682-684
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.extensionPolicy?.name`

## isSoftBlocked()
- 位置: L686-688
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.extensionPolicy?.extension?.isSoftBlocked`

## connectedCallback()
- 位置: L690-695
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `this.append()`, `this.messagebar.classList.add()`, `this.refresh()`
- 参照: `this.messagebar`

## disconnectedCallback()
- 位置: L697-699
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.messagebar?.remove()`

## refresh()
- 位置: async L701-738
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customElements.get()`, `messagebar.requestUpdate()`
- 条件付き依存: `if (!customElements.get("moz-message-bar"))` → `document.createElement()`
- 条件付き依存: `if (!customElements.get("moz-message-bar"))` → `customElements.whenDefined()`
- 条件付き依存: `if (this.isSoftBlocked)` → `messagebar.removeAttribute()`
- 条件付き依存: `if (this.isSoftBlocked)` → `messagebar.setAttribute()`
- 条件付き依存: `if (!(this.isSoftBlocked))` → `messagebar.hasAttribute()`
- 条件付き依存: `if (!(this.isSoftBlocked))` → `messagebar.setAttribute()`
- 参照: `messagebar.messageL10nArgs`, `messagebar.messageL10nArgs?.extensionName`, `messagebar.messageL10nId`, `this.extensionName`, `this.isSoftBlocked`, `this.messagebar`

## BrowserActionWidgetObserver.constructor()
- 位置: L750-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionCommon.makeWidgetId()`
- 参照: `this.addonId`, `this.onButtonAreaChanged`, `this.widgetId`

## BrowserActionWidgetObserver.startObserving()
- 位置: L758-765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addListener()`, `window.addEventListener()`
- 参照: `this.#connected`

## BrowserActionWidgetObserver.stopObserving()
- 位置: L767-774
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.removeListener()`, `window.removeEventListener()`
- 参照: `this.#connected`

## BrowserActionWidgetObserver.hasBrowserActionUI()
- 位置: L776-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`, `gUnifiedExtensions.browserActionFor()`, `policy?.canAccessWindow()`
- 参照: `this.addonId`

## BrowserActionWidgetObserver.onWidgetCreated()
- 位置: L790-797
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId === this.widgetId)` → `this.onButtonAreaChanged()`
- 参照: `this.widgetId`

## BrowserActionWidgetObserver.onWidgetAdded()
- 位置: L799-803
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId === this.widgetId)` → `this.onButtonAreaChanged()`
- 参照: `this.widgetId`

## BrowserActionWidgetObserver.onWidgetMoved()
- 位置: L805-809
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aWidgetId === this.widgetId)` → `this.onButtonAreaChanged()`
- 参照: `this.widgetId`

## BrowserActionWidgetObserver.handleEvent()
- 位置: L811-815
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.type === "unload")` → `this.stopObserving()`
- 参照: `event.type`

## MozAddonInstalledNotification.connectedCallback()
- 位置: L824-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserActionWidgetObserver?.startObserving()`, `this.addEventListener()`, `this.pinExtensionEl.addEventListener()`, `this.querySelector()`
- 参照: `this.descriptionEl`, `this.pinExtensionEl`

## MozAddonInstalledNotification.disconnectedCallback()
- 位置: L835-839
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#browserActionWidgetObserver?.stopObserving()`, `this.pinExtensionEl.removeEventListener()`, `this.removeEventListener()`

## MozAddonInstalledNotification.#settingsLinkId()
- 位置: L841-843
- 役割: (未記入)
- 触るとき: (未記入)

## MozAddonInstalledNotification.handleEvent()
- 位置: L845-871
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (target.id === this.#settingsLinkId)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (target.id === this.#settingsLinkId)` → `encodeURIComponent()`
- 条件付き依存: `if (target.id === this.#settingsLinkId)` → `event.preventDefault()`
- 条件付き依存: `if (target == this.pinExtensionEl)` → `this.#handlePinnedCheckboxStateChange()`
- 参照: `event.type`, `target.id`, `this.#settingsLinkId`, `this.notification.options.customElementOptions`, `this.pinExtensionEl`

## MozAddonInstalledNotification.show()
- 位置: L873-896
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.show()`, `this.#browserActionWidgetObserver?.stopObserving()`, `this.#renderPinToolbarButtonCheckbox()`, `this.render()`
- 条件付き依存: `if (this.isConnected)` → `this.#browserActionWidgetObserver.startObserving()`
- 参照: `this.#browserActionWidgetObserver`, `this.isConnected`, `this.notification`, `this.notification.options.customElementOptions.addonId`, `this.notification.options?.customElementOptions`

## MozAddonInstalledNotification.render()
- 位置: L898-918
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderPinToolbarButtonCheckbox()`, `this.ownerDocument.l10n.setAttributes()`, `this.querySelector()`, `this.querySelector(`#${this.#settingsLinkId}`)?.remove()`
- 条件付き依存: `if (this.#dataCollectionPermissionsEnabled)` → `document.createElementNS()`
- 条件付き依存: `if (this.#dataCollectionPermissionsEnabled)` → `link.setAttribute()`
- 条件付き依存: `if (this.#dataCollectionPermissionsEnabled)` → `this.descriptionEl.append()`
- 参照: `link.href`, `this.#dataCollectionPermissionsEnabled`, `this.#settingsLinkId`, `this.descriptionEl`

## MozAddonInstalledNotification.#dataCollectionPermissionsEnabled()
- 位置: L920-925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## MozAddonInstalledNotification.#renderPinToolbarButtonCheckbox()
- 位置: L927-952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `this.#browserActionWidgetObserver.hasBrowserActionUI()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.getPlacementOfWidget(widgetId)?.area`, `this.#browserActionWidgetObserver.widgetId`, `this.pinExtensionEl.checked`, `this.pinExtensionEl.hidden`

## MozAddonInstalledNotification.#handlePinnedCheckboxStateChange()
- 位置: L954-967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gUnifiedExtensions.pinToToolbar()`, `this.#browserActionWidgetObserver.hasBrowserActionUI()`
- 条件付き依存: `if (shouldPinToToolbar)` → `gUnifiedExtensions._maybeMoveWidgetNodeBack()`
- 参照: `this.#browserActionWidgetObserver.widgetId`, `this.notification.options.customElementOptions`, `this.pinExtensionEl.checked`

## removeNotificationOnEnd()
- 位置: L974-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `install.addListener()`
- 参照: `installs.length`

## maybeRemove()
- 位置: L977-990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `install.removeListener()`
- 条件付き依存: `if (--count == 0)` → `PopupNotifications.getNotification()`
- 条件付き依存: `if (current === notification)` → `notification.remove()`
- 参照: `notification.browser`, `notification.id`

## buildNotificationAction()
- 位置: L1002-1020
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `action.disableSecurityDelay`, `msg.attributes`, `options.disableSecurityDelay`

## showInstallConfirmation()
- 位置: L1025-1208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityUi.events.accumulateSingleSample()`, `PopupNotifications.getNotification()`, `PopupNotifications.show()`, `Services.urlFormatter.formatURLPref()`, `buildNotificationAction()`, `document.getElementById()`, `gBrowser.getTabForBrowser()`, `gUnifiedExtensions.getPopupAnchorID()`, `installInfo.installs.every()`, `installInfo.installs.filter()`, `lazy.l10n.formatMessagesSync()`, `lazy.l10n.formatValueSync()`, `removeNotificationOnEnd()`
- 条件付き依存: `if ( PopupNotifications.getNotification("addon-install-confirmation", browser) )` → `this.pendingInstalls.get()`
- 条件付き依存: `if (pending)` → `pending.push()`
- 条件付き依存: `if (!(pending))` → `this.pendingInstalls.set()`
- 条件付き依存: `if ( installInfo.installs.every(i => i.state != AddonManager.STATE_DOWNLOADED) )` → `showNextConfirmation()`
- 条件付き依存: `if (unsigned.length == installInfo.installs.length)` → `notification.setAttribute()`
- 条件付き依存: `if (!unsigned.length)` → `notification.removeAttribute()`
- 条件付き依存: `if (!(!unsigned.length))` → `notification.setAttribute()`
- 参照: `AddonManager.SIGNEDSTATE_MISSING`, `AddonManager.STATE_DOWNLOADED`, `Ci.nsISecurityUITelemetry.WARNING_CONFIRM_ADDON_INSTALL`, `gBrowser.selectedTab`, `i.addon.signedState`, `i.state`, `installInfo.installs`, `installInfo.installs.length`, `installInfo.originatingURI`, `notification.style.minHeight`, `options.eventCallback`, `options.learnMoreURL`, `unsigned.length`
- XPCOM: `nsISecurityUITelemetry` / `Services.urlFormatter`

## showNextConfirmation()
- 位置: L1040-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.browsers.includes()`, `this.pendingInstalls.get()`
- 条件付き依存: `if (pending && pending.length)` → `this.showInstallConfirmation()`
- 条件付き依存: `if (pending && pending.length)` → `pending.shift()`
- 参照: `pending.length`

## acceptInstallation()
- 位置: L1071-1080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.securityUi.events.accumulateSingleSample()`, `install.install()`
- 参照: `Ci.nsISecurityUITelemetry.WARNING_CONFIRM_ADDON_INSTALL_CLICK_THROUGH`, `installInfo.installs`
- XPCOM: `nsISecurityUITelemetry`

## cancelInstallation()
- 位置: L1082-1095
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showNextConfirmation()`
- 条件付き依存: `if (install.state != AddonManager.STATE_CANCELLED)` → `install.cancel()`
- 参照: `AddonManager.STATE_CANCELLED`, `install.state`, `installInfo.installs`

## options.eventCallback()
- 位置: L1103-1145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addonList.appendChild()`, `addonList.firstChild.remove()`, `cancelInstallation()`, `container.appendChild()`, `document.createXULElement()`, `document.getElementById()`, `name.setAttribute()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `document.createXULElement()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `unsignedLabel.setAttribute()`
- 条件付き依存: `if ( someUnsigned && install.addon.signedState <= AddonManager.SIGNEDSTATE_MISSING )` → `container.appendChild()`
- 参照: `AddonManager.SIGNEDSTATE_MISSING`, `addonList.firstChild`, `install.addon.name`, `install.addon.signedState`, `installInfo.installs`

## removeAllNotifications()
- 位置: L1233-1241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PopupNotifications.getNotification()`, `PopupNotifications.remove()`, `this.NOTIFICATION_IDS.map()`, `this.NOTIFICATION_IDS.map(id => PopupNotifications.getNotification(id, browser) ).filter()`
- 参照: `notifications.length`

## logWarningFullScreenInstallBlocked()
- 位置: L1243-1261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/scripterror;1"].createInstance()`, `Services.console.logMessage()`, `consoleMsg.initWithWindowID()`, `lazy.l10n.formatValueSync()`
- 参照: `Ci.nsIScriptError`, `Ci.nsIScriptError.warningFlag`, `gBrowser.currentURI.spec`, `gBrowser.selectedBrowser.innerWindowID`
- XPCOM: [`nsIScriptError`](../../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## observe()
- 位置: async L1264-1751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Glean.securityUi.events.accumulateSingleSample()`, `PopupNotifications.getNotification()`, `PopupNotifications.show()`, `Services.policies.mayInstallAddon()`, `Services.prefs.prefIsLocked()`, `[ AddonManager.ERROR_BLOCKLISTED, AddonManager.ERROR_SOFT_BLOCKED, ].includes()`, `buildNotificationAction()`, `gBrowser.browsers.includes()`, `gUnifiedExtensions.getPopupAnchorID()`, `installInfo.install()`, `installInfo.installs.every()`, `lazy.l10n.formatMessages()`, `lazy.l10n.formatMessagesSync()`, `lazy.l10n.formatValue()`, `lazy.l10n.formatValueSync()`, `lazy.l10n.formatValues()`, `removeNotificationOnEnd()`, `showNotification()`, `this._removeProgressNotification()`, `this.logWarningFullScreenInstallBlocked()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("xpinstall.enabled")))` → `lazy.l10n.formatMessages()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("xpinstall.enabled")))` → `buildNotificationAction()`
- 条件付き依存: `if (!(Services.prefs.prefIsLocked("xpinstall.enabled")))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (Services.policies)` → `Services.policies.getExtensionSettings()`
- 条件付き依存: `if (progressNotification)` → `progressNotification.remove()`
- 条件付き依存: `if (isSitePermissionAddon)` → `lazy.getSitePermsInstallPromptStringIds()`
- 条件付き依存: `if (!(stringIds?.header && stringIds?.message))` → `console.error()`
- 条件付き依存: `if (!(stringIds?.header && stringIds?.message))` → `cancelInstallation()`
- 条件付き依存: `if (isSitePermissionAddon)` → `declineActions.push()`
- 条件付き依存: `if (isSitePermissionAddon)` → `buildNotificationAction()`
- 条件付き依存: `if (isSitePermissionAddon)` → `AMTelemetry.recordSuspiciousSiteEvent()`
- 条件付き依存: `if (isSitePermissionAddon)` → `neverAllowCallback()`
- 条件付き依存: `if (install.state != AddonManager.STATE_CANCELLED)` → `install.cancel()`
- 条件付き依存: `if ( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...)` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if ( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...)` → `Services.policies.getExtensionSettings()`
- 条件付き依存: `if (!( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...))` → `ERROR_L10N_IDS.get()`
- 条件付き依存: `if (!( install.addon && !Services.policies.mayInstallAddon({ id: install.addon.id, type: install.addon.type, permissions: install.addon.userPermissions?.permission...))` → `lazy.l10n.formatValueSync()`
- 条件付き依存: `if (install.error == AddonManager.ERROR_SIGNEDSTATE_REQUIRED)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (isBlocklistError)` → `install.addon?.getBlocklistURL()`
- 条件付き依存: `if (progressNotification)` → `Date.now()`
- 条件付き依存: `if (progressNotification)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (securityDelay > 0)` → `setTimeout()`
- 条件付き依存: `if (securityDelay > 0)` → `PopupNotifications.getNotification()`
- 条件付き依存: `if ( PopupNotifications.getNotification("addon-progress", browser) )` → `showNotification()`
- 参照: `AddonManager.ERROR_BLOCKLISTED`, `AddonManager.ERROR_SIGNEDSTATE_REQUIRED`, `AddonManager.ERROR_SOFT_BLOCKED`, `AddonManager.STATE_CANCELLED`, `AddonManager.STATE_DOWNLOADED`, `Ci.nsISecurityUITelemetry .WARNING_ADDON_ASKING_PREVENTED_CLICK_THROUGH`, `Ci.nsISecurityUITelemetry.WARNING_ADDON_ASKING_PREVENTED`, `Ci.nsIStandardURL`, `Services.appinfo.version`, `Services.policies`, `aInstall.state`, `aSubject.wrappedJSObject`, `action.disabled`, `addon?.type`, `browser.contentWindow`, `browser.currentURI`, `extensionSettings.blocked_install_message`, `fluentIds?.length`, `install.addon`, `install.addon.id`, `install.addon.type`, `install.addon.userPermissions?.permissions`, `install.error`, `install.name`, `install.sourceURI`, `install.sourceURI.host`, `install.state`, `installInfo.browser`, `installInfo.installs`, `installInfo.installs.length`, `installInfo.installs[0].addon.sitePermissions`, `installInfo.originatingURI`, `lazy.SITEPERMS_ADDON_TYPE`, `notification._startTime`, `options.contentWindow`, `options.displayURI`, `options.displayURI.displayHost`, `options.displayURI.host`, `options.eventCallback`, `options.installs`, `options.learnMoreURL`, `options.name`, `options.persistent`, `options.removeOnDismissal`, `options.sourceURI`, `progressNotification._startTime`, `stringIds.header`, `stringIds.message`, `stringIds?.header`, `stringIds?.message`
- XPCOM: `nsISecurityUITelemetry` / [`nsIStandardURL`](../../../netwerk/base/nsIStandardURL.idl.md) / `Services.appinfo` / `Services.policies` / `Services.prefs` / `Services.urlFormatter`

## cancelInstallation()
- 位置: L1273-1282
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (install.state != AddonManager.STATE_CANCELLED)` → `install.cancel()`
- 条件付き依存: `if (installInfo.cancel)` → `installInfo.cancel()`
- 参照: `AddonManager.STATE_CANCELLED`, `install.state`, `installInfo.cancel`, `installInfo.installs`

## options.eventCallback()
- 位置: L1427-1456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `learnMore.setAttribute()`, `message.firstChild.remove()`
- 条件付き依存: `if (!(!hasHost))` → `doc.createElementNS()`
- 条件付き依存: `if (!(!hasHost))` → `BrowserUIUtils.getLocalizedFragment()`
- 条件付き依存: `if (!(!hasHost))` → `message.appendChild()`
- 参照: `b.textContent`, `browser.ownerDocument`, `message.firstChild`, `message.textContent`, `options.name`

## neverAllowCallback()
- 位置: L1481-1488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SitePermissions.setForPrincipal()`, `cancelInstallation()`
- 参照: `SitePermissions.BLOCK`, `browser.contentPrincipal`

## options.eventCallback()
- 位置: L1549-1556
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `options.contentWindow`, `options.sourceURI`

## options.eventCallback()
- 位置: L1679-1692
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (blocklistURL)` → `blocklistURLEl.setAttribute()`
- 条件付き依存: `if (!(blocklistURL))` → `blocklistURLEl.removeAttribute()`
- 参照: `browser.ownerDocument`

## showNotification()
- 位置: L1712-1724
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._removeProgressNotification()`, `this.showInstallConfirmation()`
- 条件付き依存: `if (PopupNotifications.isPanelOpen)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (PopupNotifications.isPanelOpen)` → `document.getElementById()`
- 参照: `PopupNotifications.isPanelOpen`, `rect.height`

## _removeProgressNotification()
- 位置: L1752-1760
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PopupNotifications.getNotification()`
- 条件付き依存: `if (notification)` → `notification.remove()`

## init()
- 位置: L1765-1770
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionsUI.on()`, `this.updateAlerts()`, `this.updateAlerts.bind()`
- 参照: `this.boundUpdate`, `this.initialized`

## uninit()
- 位置: L1772-1779
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionsUI.off()`
- 参照: `this.boundUpdate`, `this.initialized`

## _createAddonButton()
- 位置: L1781-1797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelUI.addonNotificationContainer.appendChild()`, `button.addEventListener()`, `button.setAttribute()`, `document.createXULElement()`, `lazy.l10n.formatValueSync()`
- 参照: `addon.name`, `addon?.iconURL`, `button.className`

## updateAlerts()
- 位置: L1799-1842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionsUI.showSideloaded()`, `ExtensionsUI.showUpdate()`, `PanelUI.hide()`, `container.firstChild.remove()`, `this._createAddonButton()`
- 条件付き依存: `if (lazy.AMBrowserExtensionsImport.canCompleteOrCancelInstalls)` → `this._createAddonButton()`
- 条件付き依存: `if (lazy.AMBrowserExtensionsImport.canCompleteOrCancelInstalls)` → `lazy.AMBrowserExtensionsImport.completeInstalls()`
- 参照: `ExtensionsUI.sideloaded`, `ExtensionsUI.updates`, `PanelUI.addonNotificationContainer`, `container.firstChild`, `lazy.AMBrowserExtensionsImport.canCompleteOrCancelInstalls`, `update.addon`

## promptRemoveExtension()
- 位置: async L1846-1895
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["extension", "theme"].includes()`, `confirmEx()`, `lazy.l10n.formatValues()`
- 条件付き依存: `if ( gAddonAbuseReportEnabled && ["extension", "theme"].includes(addon.type) )` → `lazy.l10n.formatValue()`
- 条件付き依存: `if (addon.type === "mlmodel")` → `lazy.l10n.formatValue()`
- 参照: `Services.prompt`, `addon.type`, `checkboxState.value`
- XPCOM: `Services.prompt`

## reportAddon()
- 位置: async L1897-1909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `lazy.AbuseReporter.getAMOFormURL()`, `window.openTrustedLinkIn()`

## removeAddon()
- 位置: async L1911-1928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `this.promptRemoveExtension()`
- 条件付き依存: `if (remove)` → `addon.uninstall()`
- 条件付き依存: `if (report)` → `this.reportAddon()`
- 参照: `AddonManager.PERM_CAN_UNINSTALL`, `addon.id`, `addon.permissions`

## manageAddon()
- 位置: async L1930-1937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `encodeURIComponent()`, `this.openAddonsMgr()`
- 参照: `addon.id`

## openAddonsMgr()
- 位置: L1960-2016
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (aView && !selectTabByViewId)` → `emWindow.loadView()`
- 条件付き依存: `if (emWindow)` → `browserWindow.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (emWindow)` → `emWindow.focus()`
- 条件付き依存: `if (emWindow)` → `resolve()`
- 条件付き依存: `if (selectTabByViewId)` → `isBlankPageURL()`
- 条件付き依存: `if (selectTabByViewId)` → `openTrustedLinkIn()`
- 条件付き依存: `if (!(selectTabByViewId))` → `switchToTabHavingURI()`
- 参照: `browserWindow.gBrowser.selectedTab`, `emWindow.docShell.chromeEventHandler`, `gBrowser.currentURI.spec`
- XPCOM: `Services.obs`

## receivePong()
- 位置: L1965-1978
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aSubject.browsingContext.topChromeWindow`, `aSubject.gViewController.currentViewId`

## observer()
- 位置: L2007-2014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `aSubject.focus()`, `resolve()`
- 条件付き依存: `if (aView)` → `aSubject.loadView()`
- XPCOM: `Services.obs`

## init()
- 位置: L2044-2075
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.addManagerListener()`, `CustomizableUI.addListener()`, `Glean.extensionsButton.prefersHiddenButton.set()`, `PanelUI.mainView.addEventListener()`, `document.getElementById()`, `gBrowser.addTabsProgressListener()`, `gNavToolbox.addEventListener()`, `lazy.ExtensionPermissions.addListener()`, `this._button.addEventListener()`, `this._buttonAttrObs.observe()`, `this._updateButtonBarListeners()`, `this.onAppMenuShowing.bind()`, `this.onButtonOpenChange()`, `this.updateAttention()`, `this.updateButtonVisibility()`, `window.addEventListener()`
- 参照: `this._button`, `this._buttonAttrObs`, `this._initialized`, `this._navbar`, `this.buttonAlwaysVisible`, `this.onAppMenuShowing`, `this.permListener`

## this.permListener()
- 位置: L2062-2062
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateAttention()`

## uninit()
- 位置: L2077-2095
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.removeManagerListener()`, `CustomizableUI.removeListener()`, `PanelUI.mainView.removeEventListener()`, `gNavToolbox.removeEventListener()`, `lazy.ExtensionPermissions.removeListener()`, `this._button.removeEventListener()`, `this._buttonAttrObs.disconnect()`, `window.removeEventListener()`
- 参照: `this._initialized`, `this.onAppMenuShowing`, `this.permListener`

## _updateButtonBarListeners()
- 位置: L2097-2117
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.buttonAlwaysVisible)` → `this._navbar.removeEventListener()`
- 条件付き依存: `if (!(this.buttonAlwaysVisible))` → `this._navbar.addEventListener()`
- 参照: `this._buttonBarHasMouse`, `this.buttonAlwaysVisible`

## onBlocklistAttentionUpdated()
- 位置: L2119-2121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateAttention()`

## onAppMenuShowing()
- 位置: L2123-2128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("appMenu-extensions-themes-button").hidden`, `document.getElementById("appMenu-unified-extensions-button").hidden`, `this.buttonAlwaysVisible`

## onLocationChange()
- 位置: L2130-2139
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( webProgress.isTopLevel && browser === gBrowser.selectedBrowser && !(flags & Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT) )` → `this.updateAttention()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `gBrowser.selectedBrowser`, `webProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## updateButtonVisibility()
- 位置: L2141-2167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `this.button.hasAttribute()`
- 条件付き依存: `if (shouldShowButton)` → `this._navbar.setAttribute()`
- 条件付き依存: `if (!(shouldShowButton))` → `this._navbar.removeAttribute()`
- 参照: `this._button.hidden`, `this._button.open`, `this._buttonBarHasMouse`, `this._buttonShownBeforeButtonOpen`, `this.button.hidden`, `this.buttonAlwaysVisible`, `this.buttonIgnoresAttention`

## ensureButtonShownBeforeAttachingPanel()
- 位置: L2169-2178
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.buttonAlwaysVisible && !this._button.open)` → `this.updateButtonVisibility()`
- 参照: `this._button.open`, `this._buttonShownBeforeButtonOpen`, `this.buttonAlwaysVisible`

## onButtonOpenChange()
- 位置: L2180-2187
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.buttonAlwaysVisible && !this._button.open)` → `this.updateButtonVisibility()`
- 参照: `this._button.open`, `this._buttonShownBeforeButtonOpen`, `this.buttonAlwaysVisible`

## updateAttention()
- 位置: L2190-2243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.shouldShowBlocklistAttention()`, `this.button.ownerDocument.l10n.setAttributes()`, `this.button.toggleAttribute()`
- 条件付き依存: `if (!blocklistAttention)` → `this.getActivePolicies()`
- 条件付き依存: `if (!blocklistAttention)` → `this.browserActionFor()`
- 条件付き依存: `if (!widget || widget.areaType !== CustomizableUI.TYPE_TOOLBAR)` → `lazy.OriginControls.getAttentionState()`
- 条件付き依存: `if (!blocklistAttention)` → `this._shouldShowQuarantinedNotification()`
- 条件付き依存: `if (blocklistAttention)` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (permissionsAttention || quarantinedAttention)` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!this.buttonAlwaysVisible && !this.buttonIgnoresAttention)` → `this.updateButtonVisibility()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `lazy.OriginControls.getAttentionState(policy, window).attention`, `this.browserActionFor(policy)?.widget`, `this.button`, `this.buttonAlwaysVisible`, `this.buttonIgnoresAttention`, `widget.areaType`

## getPopupAnchorID()
- 位置: L2249-2265
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!aBrowser[attr])` → `aWindow.document.getElementById()`

## button()
- 位置: L2267-2269
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._button`

## getActivePolicies()
- 位置: L2281-2307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getActiveExtensions()`, `policies.filter()`, `policy.canAccessWindow()`
- 参照: `extension.isHidden`, `extension?.type`

## hasExtensionsInPanel()
- 位置: L2319-2328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `policies.some()`, `this.browserActionFor()`, `this.getActivePolicies()`, `widget.forWindow()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `this.browserActionFor(policy)?.widget`, `widget.areaType`, `widget.forWindow(window).overflowed`

## isPrivateWindowMissingExtensionsWithoutPBMAccess()
- 位置: L2330-2336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `policies.some()`, `this.getActivePolicies()`
- 参照: `p.privateBrowsingAllowed`

## isAtLeastOneExtensionWithPBMOptIn()
- 位置: async L2348-2366
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonsByTypes()`, `WebExtensionPolicy.getByID()`, `addons.some()`
- 参照: `addon.hidden`, `addon.id`, `addon.permissions`, `lazy.AddonManager.PERM_CAN_CHANGE_PRIVATEBROWSING_ACCESS`, `policy.privateBrowsingAllowed`

## getDisabledExtensionsInfo()
- 位置: async L2368-2376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonsByTypes()`, `addons.filter()`, `addons.some()`
- 参照: `a.hidden`, `a.isActive`, `a.permissions`, `addons.length`, `lazy.AddonManager.PERM_CAN_ENABLE`

## handleEvent()
- 位置: L2378-2433
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `popupnotification?.getAttribute()`, `this._navbar.contains()`, `this.ensureButtonShownBeforeAttachingPanel()`, `this.onPanelViewHiding()`, `this.onPanelViewShowing()`, `this.onToolbarVisibilityChange()`, `this.panel.hidePopup()`, `this.recordButtonTelemetry()`, `this.updateButtonVisibility()`
- 条件付き依存: `if (popupid === "addon-webext-permissions")` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!(popupid === "addon-webext-permissions"))` → `gXPInstallObserver.NOTIFICATION_IDS.includes()`
- 条件付き依存: `if (gXPInstallObserver.NOTIFICATION_IDS.includes(popupid))` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!(gXPInstallObserver.NOTIFICATION_IDS.includes(popupid)))` → `console.error()`
- 条件付き依存: `if ( this._buttonBarHasMouse && !this._navbar.contains(event.relatedTarget) )` → `this.updateButtonVisibility()`
- 参照: `PopupNotifications.panel`, `PopupNotifications.panel.firstElementChild`, `event.detail.visible`, `event.relatedTarget`, `event.target`, `event.target.id`, `event.type`, `this._buttonBarHasMouse`

## onPanelViewShowing()
- 位置: L2435-2579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.name.localeCompare()`, `document.createElement()`, `item.setExtension()`, `list.appendChild()`, `panelview.querySelector()`, `policies.filter()`, `policiesForList.sort()`, `this._shouldShowQuarantinedNotification()`, `this.getActivePolicies()`, `this.hasExtensionsInPanel()`
- 条件付き依存: `if (this.hasExtensionsInPanel(policies))` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!(this.hasExtensionsInPanel(policies)))` → `this.isPrivateWindowMissingExtensionsWithoutPBMAccess()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `this.isAtLeastOneExtensionWithPBMOptIn().then()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `this.isAtLeastOneExtensionWithPBMOptIn()`
- 条件付き依存: `if (this.isPrivateWindowMissingExtensionsWithoutPBMAccess())` → `isStillShowing()`
- 条件付き依存: `if (!result && isStillShowing())` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `this.getDisabledExtensionsInfo().then()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `this.getDisabledExtensionsInfo()`
- 条件付き依存: `if (!(this.isPrivateWindowMissingExtensionsWithoutPBMAccess()))` → `isStillShowing()`
- 条件付き依存: `if (disabledExtensionsInfo.isAnyDisabled)` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!policies.length)` → `this._updateEmptyStateBox()`
- 条件付き依存: `if (!policies.length)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!policies.length)` → `this._createDiscoverButton()`
- 条件付き依存: `if (!policies.length)` → `panelview.querySelector()`
- 条件付き依存: `if (!policies.length)` → `manageExtensionsButton.previousElementSibling.before()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `this._makeMessageBar()`
- 条件付き依存: `if (Services.appinfo.inSafeMode)` → `container.prepend()`
- 条件付き依存: `if (this.blocklistAttentionInfo?.shouldShow)` → `this._createBlocklistMessageBar()`
- 条件付き依存: `if (!(this.blocklistAttentionInfo?.shouldShow))` → `this._messageBarBlocklist?.remove()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this._makeMessageBar()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this._messageBarQuarantinedDomain .querySelector("a") .addEventListener()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this._messageBarQuarantinedDomain .querySelector()`
- 条件付き依存: `if (!this._messageBarQuarantinedDomain)` → `this.togglePanel()`
- 条件付き依存: `if (shouldShowQuarantinedNotification)` → `container.appendChild()`
- 条件付き依存: `if (!(shouldShowQuarantinedNotification))` → `container.contains()`
- 条件付き依存: `if ( !shouldShowQuarantinedNotification && this._messageBarQuarantinedDomain && container.contains(this._messageBarQuarantinedDomain) )` → `container.removeChild()`
- 参照: `Services.appinfo.inSafeMode`, `b.name`, `disabledExtensionsInfo.isAnyDisabled`, `disabledExtensionsInfo.isAnyEnableable`, `p.extension.hasBrowserActionUI`, `policies.length`, `policy.extension`, `this._messageBarBlocklist`, `this._messageBarQuarantinedDomain`, `this._messageBarSafemode`, `this._panelShownCount`, `this.blocklistAttentionInfo?.shouldShow`
- XPCOM: `Services.appinfo` / `Services.prefs`

## isStillShowing()
- 位置: L2437-2437
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._panelShownCount`

## onPanelViewHiding()
- 位置: L2581-2596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `list.lastChild.remove()`, `panelview .querySelector()`, `panelview .querySelector("#unified-extensions-discover-extensions") ?.remove()`, `panelview.querySelector()`, `requestAnimationFrame()`, `this.updateAttention()`
- 参照: `list.lastChild`, `this._panelShownCount`, `window.closed`

## onToolbarVisibilityChange()
- 位置: L2598-2645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidgetIdsInArea()`, `CustomizableUI.getWidgetIdsInArea(toolbarId).filter()`, `this.panel.querySelector()`
- 条件付き依存: `if (isVisible)` → `this._maybeMoveWidgetNodeBack()`
- 条件付き依存: `if (!(isVisible))` → `widget.forWindow()`
- 条件付き依存: `if (!(isVisible))` → `node.setAttribute()`
- 条件付き依存: `if (!(isVisible))` → `overflowedExtensionsList.appendChild()`
- 条件付き依存: `if (!(isVisible))` → `this._updateWidgetClassName()`
- 参照: `CustomizableUI.isWebExtensionWidget`, `widget.id`

## _maybeMoveWidgetNodeBack()
- 位置: L2647-2701
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `CustomizableUI.getPlacementOfWidget()`, `CustomizableUI.getWidget()`, `child.getAttribute()`, `document.getElementById()`, `node.hasAttribute()`, `widget.forWindow()`
- 条件付き依存: `if (currentPosition === position)` → `child.before()`
- 条件付き依存: `if (child === container.lastChild)` → `child.after()`
- 条件付き依存: `if (moved)` → `node.removeAttribute()`
- 条件付き依存: `if (moved)` → `this._updateWidgetClassName()`
- 参照: `container.childNodes`, `container.lastChild`

## panel()
- 位置: L2704-2739
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._panel)` → `document.getElementById()`
- 条件付き依存: `if (!this._panel)` → `template.replaceWith()`
- 条件付き依存: `if (!this._panel)` → `this._panel.querySelector()`
- 条件付き依存: `if (!this._panel)` → `CustomizableUI.registerPanelNode()`
- 条件付き依存: `if (!this._panel)` → `CustomizableUI.addPanelCloseListeners()`
- 条件付き依存: `if (!this._panel)` → `this._panel .querySelector("#unified-extensions-manage-extensions") .addEventListener()`
- 条件付き依存: `if (!this._panel)` → `this._panel .querySelector()`
- 条件付き依存: `if (!this._panel)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (!this._panel)` → `document .getElementById("unified-extensions-context-menu") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`
- 条件付き依存: `if (!this._panel)` → `document .getElementById("unified-extensions-context-menu") .querySelectorAll()`
- 条件付き依存: `if (!this._panel)` → `document .getElementById()`
- 条件付き依存: `if (!this._panel)` → `el.setAttribute()`
- 条件付き依存: `if (!this._panel)` → `el.getAttribute()`
- 条件付き依存: `if (!this._panel)` → `el.removeAttribute()`
- 参照: `CustomizableUI.AREA_ADDONS`, `template.content`, `this._panel`

## togglePanel()
- 位置: async L2743-2813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `window.dispatchEvent()`
- 条件付き依存: `if (aEvent)` → `this.getActivePolicies()`
- 条件付き依存: `if (aEvent)` → `this.hasExtensionsInPanel()`
- 条件付き依存: `if (aEvent)` → `this.isPrivateWindowMissingExtensionsWithoutPBMAccess()`
- 条件付き依存: `if (aEvent)` → `this.getDisabledExtensionsInfo()`
- 条件付き依存: `if ( policies.length && !this.hasExtensionsInPanel(policies) && !this.isPrivateWindowMissingExtensionsWithoutPBMAccess() && !(await this.getDisabledExtensionsInf...)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (!CustomizationHandler.isCustomizing())` → `AddonManager.getBlocklistAttentionInfo()`
- 条件付き依存: `if (!this._listView)` → `PanelMultiView.getViewNode()`
- 条件付き依存: `if (!this._listView)` → `this._listView.addEventListener()`
- 条件付き依存: `if (this._button.open)` → `PanelMultiView.hidePopup()`
- 条件付き依存: `if (!(this._button.open))` → `CustomizableUI.getCollapsedToolbarIds()`
- 条件付き依存: `if (!(this._button.open))` → `this.onToolbarVisibilityChange()`
- 条件付き依存: `if (!(this._button.open))` → `this.recordButtonTelemetry()`
- 条件付き依存: `if (!(this._button.open))` → `this.ensureButtonShownBeforeAttachingPanel()`
- 条件付き依存: `if (!(this._button.open))` → `PanelMultiView.openPopup()`
- 参照: `(await this.getDisabledExtensionsInfo()).isAnyDisabled`, `AppConstants.platform`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `aEvent.button`, `aEvent.charCode`, `aEvent.ctrlKey`, `aEvent.keyCode`, `aEvent.type`, `panel.hidden`, `policies.length`, `this._button`, `this._button.open`, `this._listView`, `this.blocklistAttentionInfo`, `this.panel`

## openPanel()
- 位置: async L2815-2831
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `this.togglePanel()`
- 条件付き依存: `if (event?.sourceEvent?.target.id === "appMenu-unified-extensions-button")` → `Glean.extensionsButton.openViaAppMenu.record()`
- 条件付き依存: `if (event?.sourceEvent?.target.id === "appMenu-unified-extensions-button")` → `this.hasExtensionsInPanel()`
- 参照: `event?.sourceEvent?.target.id`, `this._button.hidden`, `this._button.open`

## isPanelOpen()
- 位置: L2837-2839
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._button?.open`

## updateContextMenu()
- 位置: L2841-2920
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `AddonManager.getAddonByID(id).then()`, `ExtensionsUI.originControlsMenu()`, `WebExtensionPolicy.getByID()`, `menu.querySelector()`, `this._getExtensionId()`, `this._getWidgetId()`, `this.browserActionFor()`
- 条件付き依存: `if (forBrowserAction)` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (forBrowserAction)` → `pinButton.toggleAttribute()`
- 条件付き依存: `if (forBrowserAction)` → `document.querySelector()`
- 条件付き依存: `if (browserAction)` → `browserAction.updateContextMenu()`
- 参照: `AddonManager.PERM_CAN_UNINSTALL`, `CustomizableUI.AREA_ADDONS`, `CustomizableUI.getPlacementOfWidget(widgetId).area`, `addon.permissions`, `document.querySelector("#unified-extensions-area > :first-child") ?.id`, `document.querySelector("#unified-extensions-area > :last-child")?.id`, `element.hidden`, `event.target.id`, `moveDown.hidden`, `moveUp.hidden`, `placement?.area`, `removeButton.disabled`, `reportButton.hidden`

## onContextMenuCommand()
- 位置: L2923-2935
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classList.contains()`, `this.togglePanel()`
- 参照: `event.target`

## browserActionFor()
- 位置: L2937-2943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `method()`
- 参照: `lazy.ExtensionParent.apiManager.global.browserActionFor`, `policy?.extension`

## manageExtension()
- 位置: async L2945-2949
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.manageAddon()`, `this._getExtensionId()`

## removeExtension()
- 位置: async L2951-2955
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.removeAddon()`, `this._getExtensionId()`

## reportExtension()
- 位置: async L2957-2961
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.reportAddon()`, `this._getExtensionId()`

## _getExtensionId()
- 位置: L2963-2968
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `triggerNode .closest()`, `triggerNode .closest(".unified-extensions-item") ?.querySelector()`
- 参照: `triggerNode .closest(".unified-extensions-item") ?.querySelector("toolbarbutton")?.dataset.extensionid`

## _getWidgetId()
- 位置: L2970-2973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `triggerNode.closest()`
- 参照: `triggerNode.closest(".unified-extensions-item")?.id`

## onPinToToolbarChange()
- 位置: async L2975-3001
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.hasAttribute()`, `event.target.toggleAttribute()`, `this._getWidgetId()`, `this.pinToToolbar()`
- 条件付き依存: `if (shouldPinToToolbar)` → `this._maybeMoveWidgetNodeBack()`

## pinToToolbar()
- 位置: L3003-3012
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_NAVBAR`

## moveWidget()
- 位置: async L3014-3045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`, `menu.triggerNode.closest()`
- 条件付き依存: `if (placement)` → `CustomizableUI.moveWidgetWithinArea()`
- 参照: `element?.id`, `node.id`, `node.nextElementSibling`, `node.previousElementSibling`, `placement.position`

## onWidgetAdded()
- 位置: L3047-3064
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getAreaType()`, `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(aWidgetId)?.forWindow()`, `CustomizableUI.isWebExtensionWidget()`, `this._updateWidgetClassName()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `this.updateAttention()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.getWidget(aWidgetId)?.forWindow(window)?.overflowed`

## onWidgetMoved()
- 位置: L3066-3070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `this.updateAttention()`

## onWidgetOverflow()
- 位置: L3072-3080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.getAttribute()`, `this._updateWidgetClassName()`
- 参照: `aNode.documentGlobal`

## onWidgetUnderflow()
- 位置: L3082-3090
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNode.getAttribute()`, `this._updateWidgetClassName()`
- 参照: `aNode.documentGlobal`

## onAreaNodeRegistered()
- 位置: L3092-3105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getAreaType()`, `CustomizableUI.getWidgetIdsInArea()`, `this._updateWidgetClassName()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aContainer.documentGlobal`

## _updateWidgetClassName()
- 位置: L3112-3134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizableUI.getWidget()`, `CustomizableUI.getWidget(aWidgetId)?.forWindow()`, `CustomizableUI.isWebExtensionWidget()`, `node?.querySelector()`
- 条件付き依存: `if (actionButton)` → `actionButton.classList.toggle()`
- 条件付き依存: `if (menuButton)` → `menuButton.classList.toggle()`
- 参照: `CustomizableUI.getWidget(aWidgetId)?.forWindow(window)?.node`

## _createBlocklistMessageBar()
- 位置: L3136-3195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.contains()`, `messageBarBlocklist.addEventListener()`, `this._makeMessageBar()`, `this.blocklistAttentionInfo?.dismiss()`
- 条件付き依存: `if ( this._messageBarBlocklist && container.contains(this._messageBarBlocklist) )` → `container.replaceChild()`
- 条件付き依存: `if (!( this._messageBarBlocklist && container.contains(this._messageBarBlocklist) ))` → `container.contains()`
- 条件付き依存: `if (container.contains(this._messageBarQuarantinedDomain))` → `container.insertBefore()`
- 条件付き依存: `if (!(container.contains(this._messageBarQuarantinedDomain)))` → `container.appendChild()`
- 参照: `addons[0].name`, `this._messageBarBlocklist`, `this._messageBarQuarantinedDomain`, `this.blocklistAttentionInfo`

## _makeMessageBar()
- 位置: L3197-3253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.l10n.setAttributes()`, `messageBar.classList.add()`, `messageBar.setAttribute()`
- 条件付き依存: `if (dismissible)` → `messageBar.setAttribute()`
- 条件付き依存: `if (linkToAboutAddons)` → `document.createElement()`
- 条件付き依存: `if (linkToAboutAddons)` → `linkToAboutAddonsEl.setAttribute()`
- 条件付き依存: `if (linkToAboutAddons)` → `linkToAboutAddonsEl.addEventListener()`
- 条件付き依存: `if (linkToAboutAddons)` → `BrowserAddonUI.openAddonsMgr()`
- 条件付き依存: `if (linkToAboutAddons)` → `this.togglePanel()`
- 条件付き依存: `if (linkToAboutAddons)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (linkToAboutAddons)` → `messageBar.append()`
- 条件付き依存: `if (supportPage)` → `document.createElement()`
- 条件付き依存: `if (supportPage)` → `supportUrl.setAttribute()`
- 条件付き依存: `if (supportPageFluentId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (supportPage)` → `messageBar.append()`

## _updateEmptyStateBox()
- 位置: L3255-3287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelview.querySelector()`
- 条件付き依存: `if (!hidden)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!hidden)` → `emptyStateBox.querySelector()`
- 条件付き依存: `if (!hidden)` → `img.classList.toggle()`
- 参照: `emptyStateBox.hidden`, `this.EMPTY_STATE_ILLUSTRATION_CLASS`, `this.EMPTY_STATE_ILLUSTRATION_ONBOARDING_CLASS`

## _createDiscoverButton()
- 位置: L3289-3306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserAddonUI.openAddonsMgr()`, `discoverButton.addEventListener()`, `document.createElement()`, `document.l10n.setAttributes()`
- 参照: `discoverButton.className`, `discoverButton.id`, `discoverButton.type`

## _shouldShowQuarantinedNotification()
- 位置: L3308-3321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.isQuarantinedURI()`, `lazy.OriginControls.getState()`, `this.getActivePolicies()`, `this.getActivePolicies().some()`, `this.hasExtensionsInPanel()`
- 参照: `lazy.OriginControls.getState(policy, selectedTab).quarantined`, `window.gBrowser`

## recordButtonTelemetry()
- 位置: L3331-3335
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.buttonAlwaysVisible && this._button.hidden)` → `Glean.extensionsButton.temporarilyUnhidden[reason].add()`
- 参照: `Glean.extensionsButton.temporarilyUnhidden`, `this._button.hidden`, `this.buttonAlwaysVisible`

## hideExtensionsButtonFromToolbar()
- 位置: L3337-3356
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ConfirmationHint.show()`, `CustomizationHandler.isCustomizing()`, `Glean.extensionsButton.toggleVisibility.record()`, `Services.prefs.setBoolPref()`, `document.getElementById()`, `this.hasExtensionsInPanel()`
- 参照: `this._button.hidden`
- XPCOM: `Services.prefs`

## showExtensionsButtonInToolbar()
- 位置: L3358-3371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `Glean.extensionsButton.toggleVisibility.record()`, `Services.prefs.setBoolPref()`, `this.hasExtensionsInPanel()`
- 参照: `this._button.hidden`, `this.buttonAlwaysVisible`
- XPCOM: `Services.prefs`
