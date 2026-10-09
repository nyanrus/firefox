# browser/components/preferences/sync.js

source: browser/components/preferences/sync.js
source-hash: 71615fa88f593593b17f17f546db5fdf4009b42c
lines: 474

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## page()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("weavePrefsDeck").selectedIndex`

## page()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("weavePrefsDeck").selectedIndex`

## init()
- 位置: L39-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/weave/service;1"].getService()`, `Services.obs.addObserver()`, `document .getElementById()`, `document .getElementById("weavePrefsDeck") .removeAttribute()`, `this._setupEventListeners()`, `this._showLoadPage()`, `this.setupEnginesUI()`, `this.updateSyncUI()`, `window.addEventListener()`, `xps.ensureLoaded()`
- 条件付き依存: `if (xps.ready)` → `this._init()`
- 参照: `Cc["@mozilla.org/weave/service;1"].getService( Ci.nsISupports ).wrappedJSObject`, `Ci.nsISupports`, `xps.ready`
- XPCOM: [`nsISupports`](../../../netwerk/base/nsIEncodedChannel.idl.md) / `@mozilla.org/weave/service;1` → `WeaveService` (services/sync/components.conf) / `Services.obs`

## onUnload()
- 位置: L62-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `window.removeEventListener()`
- XPCOM: `Services.obs`

## onReady()
- 位置: L69-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `this._init()`, `window.removeEventListener()`
- XPCOM: `Services.obs`

## _showLoadPage()
- 位置: L81-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getCharPref()`, `Services.prefs.getStringPref()`
- 条件付き依存: `if (username)` → `document.getElementById()`
- 条件付き依存: `if (cachedComputerName)` → `this._populateComputerName()`
- 参照: `document.getElementById("fxaEmailAddress").textContent`, `this.page`
- XPCOM: `Services.prefs`

## _init()
- 位置: L100-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccounts.config .promiseConnectDeviceURI()`, `FxAccounts.config .promiseConnectDeviceURI("sync", SyncHelpers.getEntryPoint()) .then()`, `Services.obs.notifyObservers()`, `Services.prefs.getCharPref()`, `SyncHelpers.getEntryPoint()`, `SyncHelpers.maybeShowSyncAction()`, `Weave.Svc.Obs.add()`, `Weave.Svc.Obs.remove()`, `document .getElementById()`, `document .getElementById("connect-another-device") .setAttribute()`, `document.querySelectorAll()`, `elt.setAttribute()`, `initSettingGroup()`, `this.updateWeavePrefs()`, `window.addEventListener()`
- 参照: `UIState.ON_UPDATE`, `this.updateWeavePrefs`
- XPCOM: `Services.obs` / `Services.prefs`

## _toggleComputerNameControls()
- 位置: L137-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("fxaCancelChangeDeviceName").hidden`, `document.getElementById("fxaChangeDeviceName").hidden`, `document.getElementById("fxaSaveChangeDeviceName").hidden`, `textbox.disabled`

## _focusComputerNameTextbox()
- 位置: L145-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `textbox.focus()`, `textbox.setSelectionRange()`
- 参照: `textbox.value.length`

## _blurComputerNameTextbox()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("fxaSyncComputerName").blur()`

## _focusAfterComputerNameTextbox()
- 位置: L156-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.focus.moveFocus()`, `document.getElementById()`
- 参照: `Services.focus.MOVEFOCUS_FORWARD`
- XPCOM: `Services.focus`

## _updateComputerNameValue()
- 位置: L166-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._populateComputerName()`
- 条件付き依存: `if (save)` → `document.getElementById()`
- 参照: `Weave.Service.clientsEngine.localName`, `textbox.value`

## _setupEventListeners()
- 位置: L174-258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SyncHelpers._chooseWhatToSync()`, `SyncHelpers.getEntryPoint()`, `SyncHelpers.reSignIn()`, `SyncHelpers.setupSync()`, `SyncHelpers.signIn()`, `SyncHelpers.unlinkFirefoxAccount()`, `SyncHelpers.verifyFirefoxAccount()`, `UIState.get()`, `Weave.Service.sync()`, `document .getElementById()`, `document .getElementById("syncNow") .setAttribute()`, `document.getElementById()`, `document.getElementById("syncNow").getAttribute()`, `gSyncPane.openChangeProfileImage()`, `setEventListener()`, `this._blurComputerNameTextbox()`, `this._focusAfterComputerNameTextbox()`, `this._focusComputerNameTextbox()`, `this._toggleComputerNameControls()`, `this._updateComputerNameValue()`, `this._updateSyncNow()`, `window.browsingContext.topChromeWindow.gSync.formatLastSyncDate()`
- 条件付き依存: `if (e.keyCode == KeyEvent.DOM_VK_RETURN)` → `document.getElementById("fxaSaveChangeDeviceName").click()`
- 条件付き依存: `if (e.keyCode == KeyEvent.DOM_VK_RETURN)` → `document.getElementById()`
- 条件付き依存: `if (e.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `document.getElementById("fxaCancelChangeDeviceName").click()`
- 条件付き依存: `if (e.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `document.getElementById()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_RETURN`, `e.keyCode`, `state.lastSync`, `state.syncing`

## setEventListener()
- 位置: L175-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aCallback.bind()`, `document .getElementById()`, `document .getElementById(aId) .addEventListener()`

## updateSyncUI()
- 位置: L260-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (SyncHelpers.isSyncEnabled)` → `syncStatusTitle.setAttribute()`
- 条件付き依存: `if (!(SyncHelpers.isSyncEnabled))` → `syncStatusTitle.setAttribute()`
- 参照: `SyncHelpers.isSyncEnabled`, `syncConfiguredEl.hidden`, `syncConnectAnotherDeviceEl.hidden`, `syncNotConfiguredEl.hidden`, `syncNowButton.hidden`

## _updateSyncNow()
- 位置: L284-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.getAttributes()`
- 条件付き依存: `if (document.l10n.getAttributes(butSyncNow).id != fluentID)` → `butSyncNow.removeAttribute()`
- 条件付き依存: `if (document.l10n.getAttributes(butSyncNow).id != fluentID)` → `document.l10n.setAttributes()`
- 参照: `butSyncNow.disabled`, `document.l10n.getAttributes(butSyncNow).id`

## updateWeavePrefs()
- 位置: L297-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/weave/service;1"].getService()`, `FxAccounts.config .promiseManageURI()`, `FxAccounts.config .promiseManageURI(SyncHelpers.getEntryPoint()) .then()`, `SyncHelpers.getEntryPoint()`, `UIState.get()`, `document .getElementById()`, `document .getElementById("verifiedManage") .setAttribute()`, `document .querySelector()`, `document .querySelector("#fxaLoginVerified > .fxaProfileImage") .style.removeProperty()`, `document.getElementById()`, `document.l10n.getAttributes()`, `document.l10n.setAttributes()`, `document.querySelectorAll()`, `fxaEmailAddressLabels.forEach()`, `this._populateComputerName()`, `this._showLoadPage()`, `this._updateSyncNow()`, `this.updateSyncUI()`
- 条件付き依存: `if (state.displayName)` → `fxaLoginStatus.setAttribute()`
- 条件付き依存: `if (state.displayName)` → `document.getElementById()`
- 条件付き依存: `if (!(state.displayName))` → `fxaLoginStatus.removeAttribute()`
- 条件付き依存: `if (state.avatarURL && !state.avatarIsDefault)` → `document.querySelector()`
- 参照: `Cc["@mozilla.org/weave/service;1"].getService( Ci.nsISupports ).wrappedJSObject`, `Ci.nsISupports`, `UIState.STATUS_LOGIN_FAILED`, `UIState.STATUS_NOT_CONFIGURED`, `UIState.STATUS_NOT_VERIFIED`, `Weave.Service.clientsEngine.localName`, `displayNameLabel.hidden`, `document.getElementById("fxaDisplayNameHeading").textContent`, `document.getElementById("fxaEmailAddress").textContent`, `elt.disabled`, `eltSyncStatus.hidden`, `fxaLoginStatus.selectedIndex`, `img.onerror`, `img.src`, `l10nAttrs.id`, `profileImageElement.style.listStyleImage`, `state.avatarIsDefault`, `state.avatarURL`, `state.displayName`, `state.email`, `state.status`, `state.syncing`, `this.page`
- XPCOM: [`nsISupports`](../../../netwerk/base/nsIEncodedChannel.idl.md) / `@mozilla.org/weave/service;1` → `WeaveService` (services/sync/components.conf)

## img.onerror()
- 位置: L365-371
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (profileImageElement.style.listStyleImage === bgImage)` → `profileImageElement.style.removeProperty()`
- 参照: `profileImageElement.style.listStyleImage`

## openContentInBrowser()
- 位置: L390-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentWindow()`, `win.switchToTabHavingURI()`
- 条件付き依存: `if (!win)` → `openTrustedLinkIn()`
- XPCOM: `Services.wm`

## replaceTabWithUrl()
- 位置: L400-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createNullPrincipal()`, `browser.loadURI()`
- 参照: `window.docShell.chromeEventHandler`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## clickOrSpaceOrEnterPressed()
- 位置: L411-420
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `event.button`, `event.charCode`, `event.keyCode`, `event.type`

## openChangeProfileImage()
- 位置: L422-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.clickOrSpaceOrEnterPressed()`
- 条件付き依存: `if (this.clickOrSpaceOrEnterPressed(event))` → `FxAccounts.config .promiseChangeAvatarURI(SyncHelpers.getEntryPoint()) .then()`
- 条件付き依存: `if (this.clickOrSpaceOrEnterPressed(event))` → `FxAccounts.config .promiseChangeAvatarURI()`
- 条件付き依存: `if (this.clickOrSpaceOrEnterPressed(event))` → `SyncHelpers.getEntryPoint()`
- 条件付き依存: `if (this.clickOrSpaceOrEnterPressed(event))` → `this.openContentInBrowser()`
- 条件付き依存: `if (this.clickOrSpaceOrEnterPressed(event))` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this.clickOrSpaceOrEnterPressed(event))` → `event.preventDefault()`
- XPCOM: `Services.scriptSecurityManager`

## pairAnotherDevice()
- 位置: L438-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## _populateComputerName()
- 位置: L445-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `textbox.hasAttribute()`
- 条件付き依存: `if (!textbox.hasAttribute("placeholder"))` → `textbox.setAttribute()`
- 条件付き依存: `if (!textbox.hasAttribute("placeholder"))` → `fxAccounts.device.getDefaultLocalName()`
- 参照: `textbox.value`

## setupEnginesUI()
- 位置: L458-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `document.querySelectorAll()`, `elt.getAttribute()`, `obs()`, `observe.bind()`, `window.addEventListener()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L459-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `elt.hidden`
- XPCOM: `Services.prefs`
