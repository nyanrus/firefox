# browser/components/extensions/ExtensionControlledPopup.sys.mjs

source: browser/components/extensions/ExtensionControlledPopup.sys.mjs
source-hash: 13f2bb2fb5019eba3305d168669bb581f63568ac
lines: 453

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs .getChildList()`, `Services.prefs .getChildList(PREF_BRANCH_INSTALLED_ADDON) .map()`, `Services.strings.createBundle()`, `id.replace()`

## ExtensionControlledPopup.constructor()
- 位置: L102-118
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `opts.beforeDisableAddon`, `opts.confirmedType`, `opts.descriptionId`, `opts.descriptionMessageId`, `opts.getLocalizedDescription`, `opts.learnMoreLink`, `opts.observerTopic`, `opts.onObserverAdded`, `opts.onObserverRemoved`, `opts.popupnotificationId`, `opts.preferencesEntrypoint`, `opts.preferencesLocation`, `opts.settingKey`, `opts.settingType`, `this.beforeDisableAddon`, `this.confirmedType`, `this.descriptionId`, `this.descriptionMessageId`, `this.getLocalizedDescription`, `this.learnMoreLink`, `this.observerRegistered`, `this.observerTopic`, `this.onObserverAdded`, `this.onObserverRemoved`, `this.popupnotificationId`, `this.preferencesEntrypoint`, `this.preferencesLocation`, `this.settingKey`, `this.settingType`

## ExtensionControlledPopup.topWindow()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- XPCOM: `Services.wm`

## ExtensionControlledPopup.userHasConfirmed()
- 位置: L124-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `lazy.ExtensionSettingsStore.getSetting()`, `lazy.distributionAddonsList.has()`
- 参照: `Services.policies`, `setting.value`, `this.confirmedType`, `this.preferencesLocation`
- XPCOM: `Services.policies`

## ExtensionControlledPopup.setConfirmation()
- 位置: async L145-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionSettingsStore.addSetting()`, `lazy.ExtensionSettingsStore.initialize()`
- 参照: `this.confirmedType`

## ExtensionControlledPopup.clearConfirmation()
- 位置: async L156-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionSettingsStore.initialize()`, `lazy.ExtensionSettingsStore.removeSetting()`
- 参照: `this.confirmedType`

## ExtensionControlledPopup.observe()
- 位置: L165-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.open()`, `this.removeObserver()`, `this.topWindow.requestIdleCallback()`
- 参照: `subject.document`

## ExtensionControlledPopup.removeObserver()
- 位置: L180-188
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.observerRegistered)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this.onObserverRemoved)` → `this.onObserverRemoved()`
- 参照: `this.observerRegistered`, `this.observerTopic`, `this.onObserverRemoved`
- XPCOM: `Services.obs`

## ExtensionControlledPopup.addObserver()
- 位置: async L190-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ExtensionSettingsStore.initialize()`, `this.userHasConfirmed()`
- 条件付き依存: `if (!this.observerRegistered && !this.userHasConfirmed(extensionId))` → `Services.obs.addObserver()`
- 条件付き依存: `if (this.onObserverAdded)` → `this.onObserverAdded()`
- 参照: `this.observerRegistered`, `this.observerTopic`, `this.onObserverAdded`
- XPCOM: `Services.obs`

## ExtensionControlledPopup.open()
- 位置: async L204-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionControlledPopup._getAndMaybeCreatePanel()`, `WebExtensionPolicy.getByID()`, `doc.getElementById()`, `lazy.AddonManager.getAddonByID()`, `lazy.CustomizableUI.getWidget()`, `lazy.ExtensionSettingsStore.initialize()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `makeWidgetId()`, `panel.addEventListener()`, `panel.openPopup()`, `panel.querySelectorAll()`, `panel.removeEventListener()`, `popupnotification.show()`, `this._ensureWindowReady()`, `this.populateDescription()`, `this.removeObserver()`, `this.userHasConfirmed()`
- 条件付き依存: `if (!extensionId)` → `lazy.ExtensionSettingsStore.getSetting()`
- 条件付き依存: `if (elementsToTranslate.length)` → `win.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (elementsToTranslate.length)` → `el.setAttribute()`
- 条件付き依存: `if (elementsToTranslate.length)` → `el.getAttribute()`
- 条件付き依存: `if (elementsToTranslate.length)` → `el.removeAttribute()`
- 条件付き依存: `if (elementsToTranslate.length)` → `win.document.l10n.translateFragment()`
- 条件付き依存: `if (action)` → `action .forWindow(win) .node.querySelector()`
- 条件付き依存: `if (action)` → `action .forWindow()`
- 条件付き依存: `if (this.learnMoreLink)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (this.learnMoreLink)` → `popupnotification.setAttribute()`
- 条件付き依存: `if (!(this.learnMoreLink))` → `popupnotification.removeAttribute()`
- 条件付き依存: `if (anchor?.id == "unified-extensions-button")` → `gUnifiedExtensions.recordButtonTelemetry()`
- 条件付き依存: `if (anchor?.id == "unified-extensions-button")` → `gUnifiedExtensions.ensureButtonShownBeforeAttachingPanel()`
- 参照: `WebExtensionPolicy.getByID(extensionId).privateBrowsingAllowed`, `action.areaType`, `anchor.documentGlobal`, `anchor?.id`, `elementsToTranslate.length`, `item.id`, `popupnotification.hidden`, `this.learnMoreLink`, `this.popupnotificationId`, `this.settingKey`, `this.settingType`, `this.topWindow`, `win.document`, `win.gURLBar.focused`
- XPCOM: `Services.urlFormatter`

## handleButtonCommand()
- 位置: async L270-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `panel.hidePopup()`, `this.setConfirmation()`
- 条件付き依存: `if (urlBarWasFocused)` → `win.gURLBar.focus()`

## handleSecondaryButtonCommand()
- 位置: async L285-306
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `panel.hidePopup()`
- 条件付き依存: `if (this.preferencesLocation)` → `win.openPreferences()`
- 条件付き依存: `if (this.beforeDisableAddon)` → `this.beforeDisableAddon()`
- 条件付き依存: `if (!(this.preferencesLocation))` → `addon.disable()`
- 条件付き依存: `if (urlBarWasFocused)` → `win.gURLBar.focus()`
- 参照: `this.Entrypoint`, `this.beforeDisableAddon`, `this.preferencesLocation`

## ExtensionControlledPopup.getAddonDetails()
- 位置: L361-373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addonDetails.appendChild()`, `doc.createDocumentFragment()`, `doc.createTextNode()`, `doc.createXULElement()`, `image.classList.add()`, `image.setAttribute()`
- 参照: `addon.iconURL`, `addon.name`

## ExtensionControlledPopup.populateDescription()
- 位置: L375-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`, `lazy.strBundle.GetStringFromName()`, `this.getAddonDetails()`
- 条件付き依存: `if (this.getLocalizedDescription)` → `description.appendChild()`
- 条件付き依存: `if (this.getLocalizedDescription)` → `this.getLocalizedDescription()`
- 条件付き依存: `if (!(this.getLocalizedDescription))` → `description.appendChild()`
- 条件付き依存: `if (!(this.getLocalizedDescription))` → `lazy.BrowserUIUtils.getLocalizedFragment()`
- 参照: `description.textContent`, `this.descriptionId`, `this.descriptionMessageId`, `this.getLocalizedDescription`

## ExtensionControlledPopup._ensureWindowReady()
- 位置: async L392-441
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (activeWindow != win)` → `promiseEvent()`
- 条件付き依存: `if (focusedWindow)` → `rootTreeItem.QueryInterface()`
- 条件付き依存: `if (focusedWindow != win)` → `promiseEvent()`
- 条件付き依存: `if (promises.length)` → `win.addEventListener()`
- 条件付き依存: `if (promises.length)` → `Promise.all()`
- 条件付き依存: `if (promises.length)` → `Promise.race()`
- 条件付き依存: `if (promises.length)` → `win.removeEventListener()`
- 参照: `Ci.nsIDocShell`, `Services.focus`, `focusedWindow.docShell`, `promises.length`, `rootTreeItem.docViewer.DOMDocument.defaultView`, `win.closed`
- XPCOM: [`nsIDocShell`](../../../docshell/base/nsIDocShell.idl.md) / `Services.focus`

## promiseEvent()
- 位置: L398-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listenersToRemove.push()`, `promises.push()`, `win.addEventListener()`

## listener()
- 位置: L401-404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resolve()`, `win.removeEventListener()`

## unloadListener()
- 位置: L426-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `reject()`, `win.removeEventListener()`

## ExtensionControlledPopup._getAndMaybeCreatePanel()
- 位置: L443-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.getElementById()`
- 条件付き依存: `if (template)` → `template.replaceWith()`
- 参照: `template.content`
