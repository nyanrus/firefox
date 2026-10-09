# browser/components/preferences/config/passwords-autofill.mjs

source: browser/components/preferences/config/passwords-autofill.mjs
source-hash: 86cfeb6efddf0a95ed96d60eb900b84740f6b71e
lines: 1064

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `MANAGE_ADDRESSES_L10N_IDS.concat()`, `MANAGE_ADDRESSES_L10N_IDS.concat( EDIT_ADDRESS_L10N_IDS ).join()`, `MANAGE_CREDITCARDS_L10N_IDS.concat()`, `MANAGE_CREDITCARDS_L10N_IDS.concat( EDIT_CREDITCARD_L10N_IDS ).join()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Services.obs.notifyObservers()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`, `personalInfoEnabledPrefs()`, `personalInfoEnabledPrefs().map()`

## PasswordSettingHelpers.showPasswordExceptions()
- 位置: L44-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSubDialog.open()`

## PasswordSettingHelpers.showPasswords()
- 位置: L64-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `loginManager.sendAsyncMessage()`, `window.windowGlobalChild.getActor()`

## PasswordSettingHelpers.changeMasterPassword()
- 位置: async L74-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginHelper.getOSAuthEnabled()`, `LoginHelper.isPrimaryPasswordSet()`, `gSubDialog.open()`
- 条件付き依存: `if (!LoginHelper.isPrimaryPasswordSet() && LoginHelper.getOSAuthEnabled())` → `document.l10n.formatMessages()`
- 条件付き依存: `if (!LoginHelper.isPrimaryPasswordSet() && LoginHelper.getOSAuthEnabled())` → `Services.wm.getMostRecentBrowserWindow()`
- 条件付き依存: `if (!LoginHelper.isPrimaryPasswordSet() && LoginHelper.getOSAuthEnabled())` → `lazy.OSKeyStore.ensureLoggedIn()`
- 条件付き依存: `if (!LoginHelper.isPrimaryPasswordSet() && LoginHelper.getOSAuthEnabled())` → `Glean.pwmgr.promptShownOsReauth.record()`
- 参照: `captionText.value`, `lazy.AppConstants.platform`, `loggedIn.authenticated`, `messageText.value`
- XPCOM: `Services.wm`

## closingCallback()
- 位置: L108-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers._initMasterPasswordUI()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## PasswordSettingHelpers._removeMasterPassword()
- 位置: async L120-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/security/fipsutils;1"].getService()`
- 条件付き依存: `if (fipsUtils.isFIPSEnabled)` → `document.getElementById()`
- 条件付き依存: `if (fipsUtils.isFIPSEnabled)` → `Services.prompt.alert()`
- 条件付き依存: `if (fipsUtils.isFIPSEnabled)` → `PasswordSettingHelpers._initMasterPasswordUI()`
- 条件付き依存: `if (!(fipsUtils.isFIPSEnabled))` → `gSubDialog.open()`
- 参照: `Ci.nsIFIPSUtils`, `document.getElementById("fips-desc").textContent`, `document.getElementById("fips-title").textContent`, `fipsUtils.isFIPSEnabled`
- XPCOM: `nsIFIPSUtils` / `@mozilla.org/security/fipsutils;1` / `Services.prompt`

## closingCallback()
- 位置: L131-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers._initMasterPasswordUI()`, `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## PasswordSettingHelpers._initMasterPasswordUI()
- 位置: L145-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginHelper.isPrimaryPasswordSet()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (checkbox)` → `Services.policies.isAllowed()`
- 参照: `button.disabled`, `checkbox.checked`, `checkbox.disabled`
- XPCOM: `Services.policies` / `Services.prefs`

## visible()
- 位置: L300-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`
- 参照: `lazy.AutofillDataTypes.ADDRESS`

## visible()
- 位置: L306-307
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`
- 参照: `lazy.AutofillDataTypes.ADDRESS`

## onUserClick()
- 位置: L308-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `e.preventDefault()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.settings-redesign.enabled"))` → `window.gotoPref()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.settings-redesign.enabled")))` → `window.gSubDialog.open()`
- XPCOM: `Services.prefs`

## personalInfoTypes()
- 位置: L321-323
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.AutofillDataTypes.PASSPORT`

## isPersonalInfoCategoryAvailable()
- 位置: L327-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`, `personalInfoTypes()`, `personalInfoTypes().some()`

## personalInfoEnabledPrefs()
- 位置: L336-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AutofillDataTypes.get()`, `personalInfoTypes()`, `personalInfoTypes().map()`
- 参照: `lazy.AutofillDataTypes.get(typeId).enabledPref`

## get()
- 位置: L355-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(deps).some()`
- 参照: `dep.value`

## set()
- 位置: L356-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`
- 参照: `dep.value`

## onUserClick()
- 位置: L366-369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## visible()
- 位置: L375-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`
- 参照: `lazy.AutofillDataTypes.CREDIT_CARD`

## visible()
- 位置: L381-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`
- 参照: `lazy.AutofillDataTypes.CREDIT_CARD`

## onUserClick()
- 位置: L383-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `e.preventDefault()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.settings-redesign.enabled"))` → `window.gotoPref()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.settings-redesign.enabled")))` → `window.gSubDialog.open()`
- XPCOM: `Services.prefs`

## visible()
- 位置: L395-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OSKeyStore.canReauth()`

## get()
- 位置: L396-396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofillUtils.getOSAuthEnabled()`

## set()
- 位置: async L397-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `lazy.FormAutofillPreferences.trySetOSAuthEnabled()`
- XPCOM: `Services.obs`

## setup()
- 位置: L403-406
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## visible()
- 位置: L411-411
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `FormAutofill.isAutofillCreditCardCVVSupported`

## onUserClick()
- 位置: async L416-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`
- 条件付き依存: `if (action === "remove")` → `document.l10n.formatValues()`
- 条件付き依存: `if (action === "remove")` → `lazy.FormAutofillPreferences.prototype.openRemovePaymentDialog()`
- 条件付き依存: `if (action === "edit")` → `lazy.FormAutofillPreferences.prototype.openEditCreditCardDialog()`
- 参照: `window.browsingContext.topChromeWindow.browsingContext`

## setup()
- 位置: L446-460
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## updateDepsAndChange()
- 位置: L447-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `setting._deps`

## onUserClick()
- 位置: L461-465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`

## disabled()
- 位置: L466-466
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `saveAndFillPayments?.value`

## beforeRefresh()
- 位置: L484-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPaymentMethods()`
- 参照: `this.paymentMethods`

## getPaymentMethods()
- 位置: async L488-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillPreferences.prototype.initializePaymentsStorage()`, `lazy.FormAutofillPreferences.prototype.makePaymentsListItems()`

## getControlConfig()
- 位置: async L493-497
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.paymentMethods`

## visible()
- 位置: async L499-501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `(await this.paymentMethods).length`, `this.paymentMethods`

## setup()
- 位置: L503-510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## onUserClick()
- 位置: L517-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`
- 条件付き依存: `if (action === "remove")` → `lazy.FormAutofillPreferences.prototype.openRemoveAddressDialog()`
- 条件付き依存: `if (action === "edit")` → `lazy.FormAutofillPreferences.prototype.openEditAddressDialog()`
- 参照: `this._removeAddressDialogStrings`, `window.browsingContext.topChromeWindow.browsingContext`

## setup()
- 位置: L536-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n .formatValues()`
- 参照: `this._removeAddressDialogStrings`

## disabled()
- 位置: L546-548
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._removeAddressDialogStrings.length`

## setup()
- 位置: L554-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## updateDepsAndChange()
- 位置: L555-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `setting._deps`

## onUserClick()
- 位置: L569-574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillPreferences.prototype.openEditAddressDialog()`

## disabled()
- 位置: L575-575
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `saveAndFillAddresses?.value`

## beforeRefresh()
- 位置: L593-595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getAddresses()`
- 参照: `this.addresses`

## getAddresses()
- 位置: async L597-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillPreferences.prototype.initializeAddressesStorage()`, `lazy.FormAutofillPreferences.prototype.makeAddressesListItems()`

## getControlConfig()
- 位置: async L602-606
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.addresses`

## visible()
- 位置: async L608-610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `(await this.addresses).length`, `this.addresses`

## setup()
- 位置: L612-619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## onUserClick()
- 位置: L627-646
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`
- 条件付き依存: `if (action === "remove")` → `lazy.FormAutofillPreferences.prototype.openRemovePassportDialog()`
- 条件付き依存: `if (action === "edit")` → `lazy.FormAutofillPreferences.prototype.openEditPassportDialog()`
- 参照: `this._removePassportDialogStrings`, `window.browsingContext.topChromeWindow.browsingContext`

## setup()
- 位置: L647-656
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n .formatValues()`
- 参照: `this._removePassportDialogStrings`

## disabled()
- 位置: L657-659
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._removePassportDialogStrings.length`

## visible()
- 位置: L665-666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`
- 参照: `lazy.AutofillDataTypes.PASSPORT`

## onUserClick()
- 位置: L667-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillPreferences.prototype.openEditPassportDialog()`

## disabled()
- 位置: L673-673
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `saveAndFillPersonalInfo?.value`

## beforeRefresh()
- 位置: L691-693
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPassports()`
- 参照: `this.passports`

## getPassports()
- 位置: async L695-703
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`, `lazy.FormAutofillPreferences.prototype.initializePassportsStorage()`, `lazy.FormAutofillPreferences.prototype.makePassportsListItems()`
- 参照: `lazy.AutofillDataTypes.PASSPORT`

## getControlConfig()
- 位置: async L705-709
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.passports`

## visible()
- 位置: L714-718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`
- 参照: `lazy.AutofillDataTypes.PASSPORT`

## setup()
- 位置: L720-727
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## disabled()
- 位置: L742-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## onUserClick()
- 位置: L746-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.showPasswordExceptions()`

## visible()
- 位置: L759-759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## visible()
- 位置: L764-764
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.OSKeyStore.canReauth()`

## get()
- 位置: L765-765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.getOSAuthEnabled()`

## set()
- 位置: async L766-781
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Services.obs.notifyObservers()`, `lazy.AboutLoginsL10n.formatValue()`, `lazy.LoginHelper.trySetOSAuthEnabled()`
- XPCOM: `Services.obs`

## setup()
- 位置: L782-786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## visible()
- 位置: L792-792
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.platform`

## onUserClick()
- 位置: L797-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.showPasswords()`

## visible()
- 位置: L800-806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`, `Services.prefs.prefIsLocked()`
- 参照: `policy?.PasswordManagerEnabled`
- XPCOM: `Services.policies` / `Services.prefs`

## setup()
- 位置: L815-819
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## visible()
- 位置: L820-822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.isPrimaryPasswordSet()`

## onUserClick()
- 位置: L833-835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.changeMasterPassword()`

## disabled()
- 位置: L836-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- XPCOM: `Services.policies`

## setup()
- 位置: L843-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## visible()
- 位置: L848-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LoginHelper.isPrimaryPasswordSet()`

## onUserClick()
- 位置: L856-860
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.target.localName == "moz-button")` → `PasswordSettingHelpers._removeMasterPassword()`
- 参照: `e.target.localName`

## getControlConfig()
- 位置: L861-869
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`, `config.options?.find()`
- 参照: `button.controlAttrs`, `o.key`
- XPCOM: `Services.policies`

## onUserClick()
- 位置: L875-877
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PasswordSettingHelpers.changeMasterPassword()`
