# browser/components/sharing/SharePageAction.sys.mjs

source: browser/components/sharing/SharePageAction.sys.mjs
source-hash: 516f86462f1df362176779bd9686a0f5b628d71c
lines: 477

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `SharePageAction.updateGlobalButtonVisibility()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## shouldButtonBeVisible()
- 位置: L29-52
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## SharePageActionClass.init()
- 位置: L80-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.addEventListener()`, `this.updateButtonVisibility()`, `window.document.getElementById()`
- 参照: `window.toolbar.visible`

## SharePageActionClass.updateGlobalButtonVisibility()
- 位置: L97-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getEnumerator()`, `this.updateButtonVisibility()`
- XPCOM: `Services.wm`

## SharePageActionClass.updateButtonVisibility()
- 位置: L103-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.document.getElementById()`
- 参照: `button.hidden`, `lazy.SHARE_BUTTON_ENABLED`

## SharePageActionClass.handleEvent()
- 位置: L112-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordActions()`, `this.#setButtonExpanded()`, `this.handleCommand()`, `this.handleKeydown()`, `this.handlePopupShowing()`, `this.togglePanel()`
- 参照: `event.target`, `event.target.documentGlobal`, `event.type`, `this.#openedByKeyboard`

## SharePageActionClass.handleKeydown()
- 位置: L138-142
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `event.key`, `this.#openedByKeyboard`

## SharePageActionClass.handleCommand()
- 位置: L144-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `event.target.classList.contains()`, `event.target.documentGlobal.gSync.openSendTabHelp()`, `event.target.id.replace()`, `lazy.PanelMultiView.hidePopup()`, `lazy.SharingUtils.openPairingFlow()`, `lazy.SharingUtils.sendEmail()`, `this.#copyLink()`, `this.#handleOsShare()`, `this.#saveAction()`, `this.#showDeviceView()`, `this.#showQRCode()`
- 条件付き依存: `if (event.target.classList.contains("share-panel-device"))` → `this.#saveAction()`
- 条件付き依存: `if (event.target.classList.contains("share-panel-device"))` → `lazy.SharingUtils.sendToDevice()`
- 条件付き依存: `if (event.target.classList.contains("share-panel-device"))` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if (hintL10nId)` → `this.#showConfirmationHint()`
- 参照: `event.currentTarget`, `event.target.deviceId`, `event.target.documentGlobal`, `event.target.id`
- XPCOM: `Services.obs`

## SharePageActionClass.#copyLink()
- 位置: L219-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SharingUtils.copyLink()`, `lazy.SharingUtils.getLinkToShare()`
- 参照: `lazy.SharingUtils.getLinkToShare(panel).urlToShare`

## SharePageActionClass.#showQRCode()
- 位置: L234-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SharingUtils.getLinkToShare()`, `lazy.SharingUtils.showQRCodePanel()`, `panel.contextBrowserToShare?.get()`
- 参照: `panel.documentGlobal`

## SharePageActionClass.#handleOsShare()
- 位置: L246-250
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform === "win")` → `lazy.SharingUtils.shareOnWindows()`
- 参照: `AppConstants.platform`

## SharePageActionClass.#showConfirmationHint()
- 位置: L258-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.addEventListener()`, `window.ConfirmationHint.show()`, `window.document.getElementById()`
- 参照: `panel.documentGlobal`

## SharePageActionClass.handlePopupShowing()
- 位置: L270-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SharingUtils.getLinkToShare()`, `panel.querySelectorAll()`, `shouldButtonBeVisible()`, `this.#setButtonExpanded()`, `this.#startActions()`
- 条件付き依存: `if (this.#openedByKeyboard)` → `panel.querySelector()`
- 条件付き依存: `if (this.#openedByKeyboard)` → `lazy.PanelMultiView.forNode()`
- 参照: `button.hidden`, `button.id`, `event.target`, `lazy.PanelMultiView.forNode(mainView).focusWhenActive`, `lazy.SharingUtils.getLinkToShare(panel).urlToShare`, `panel.documentGlobal`, `this.#openedByKeyboard`

## SharePageActionClass.#setButtonExpanded()
- 位置: L290-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `button?.setAttribute()`, `panel.documentGlobal?.document.getElementById()`

## SharePageActionClass.togglePanel()
- 位置: L295-326
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.getWeakReference()`, `lazy.PanelMultiView.openPopup()`, `this.#ensurePanel()`, `this.#updateSendToDeviceButton()`, `window.document.getElementById()`
- 条件付き依存: `if (panel.state === "open" || panel.state === "showing")` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if (window.gSync.sendTabConfiguredAndLoading)` → `window.gSync.ensureFxaDevices().then()`
- 条件付き依存: `if (window.gSync.sendTabConfiguredAndLoading)` → `window.gSync.ensureFxaDevices()`
- 条件付き依存: `if (!window.closed)` → `this.#updateSendToDeviceButton()`
- 参照: `event.button`, `event.target.documentGlobal`, `panel.contextBrowserToShare`, `panel.state`, `window.closed`, `window.gBrowser.selectedBrowser`, `window.gSync.sendTabConfiguredAndLoading`

## SharePageActionClass.#updateSendToDeviceButton()
- 位置: L335-347
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.classList.toggle()`, `button.toggleAttribute()`, `window.document.getElementById()`, `window.document.l10n.setAttributes()`, `window.gSync.getSendTabTargets()`
- 参照: `window.gSync.getSendTabTargets().length`, `window.gSync.sendTabConfiguredAndLoading`

## SharePageActionClass.#showDeviceView()
- 位置: L359-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#populateDeviceView()`, `window.document .getElementById()`, `window.document .getElementById("share-panel-multiview") .showSubView()`, `window.gSync.getSendTabTargets()`
- 条件付き依存: `if (window.gSync.isSignedIn)` → `window.gSync.openConnectAnotherDevice()`
- 条件付き依存: `if (!(window.gSync.isSignedIn))` → `window.gSync.openSignInAgainPage()`
- 参照: `event.target`, `panel.documentGlobal`, `window.gSync.getSendTabTargets().length`, `window.gSync.isSignedIn`

## SharePageActionClass.#populateDeviceView()
- 位置: L382-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `body.replaceChildren()`, `button.classList.add()`, `button.setAttribute()`, `connectButton.classList.add()`, `document.createXULElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `helpButton.classList.add()`, `window.gSync.getSendTabTargets()`, `window.gSync.getSendTabTargets().map()`, `window.gSync.getTargetClientType()`
- 参照: `button.deviceId`, `connectButton.id`, `helpButton.id`, `panel.documentGlobal`, `panel.ownerDocument`, `target.id`, `target.name`

## SharePageActionClass.#ensurePanel()
- 位置: L432-445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.document.getElementById()`
- 条件付き依存: `if (!panel)` → `window.document.getElementById()`
- 条件付き依存: `if (!panel)` → `template.replaceWith()`
- 条件付き依存: `if (!panel)` → `panel.addEventListener()`
- 参照: `template.content`, `template.content.firstElementChild`

## SharePageActionClass.#startActions()
- 位置: L447-449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowToAction.set()`

## SharePageActionClass.#saveAction()
- 位置: L451-458
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#windowToAction.get()`
- 参照: `actionObject.action`

## SharePageActionClass.#recordActions()
- 位置: L460-473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.shareButton.impression.record()`, `this.#windowToAction.delete()`, `this.#windowToAction.get()`
