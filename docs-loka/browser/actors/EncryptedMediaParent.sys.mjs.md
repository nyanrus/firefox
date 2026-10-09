# browser/actors/EncryptedMediaParent.sys.mjs

source: browser/actors/EncryptedMediaParent.sys.mjs
source-hash: 8bdeba9b8803354e23a3881147fee6a6af94a63b
lines: 316

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## EncryptedMediaParent.isUiEnabled()
- 位置: L24-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## EncryptedMediaParent.ensureEMEEnabled()
- 位置: L28-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getPrefType()`, `Services.prefs.setBoolPref()`, `aBrowser.reload()`
- 条件付き依存: `if ( aKeySystem && aKeySystem == "com.widevine.alpha" && Services.prefs.getPrefType("media.gmp-widevinecdm.enabled") && !Services.prefs.getBoolPref("media.gmp-wi...)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## EncryptedMediaParent.isKeySystemVisible()
- 位置: L41-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getPrefType()`
- 条件付き依存: `if ( aKeySystem == "com.widevine.alpha" && Services.prefs.getPrefType("media.gmp-widevinecdm.visible") )` → `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## EncryptedMediaParent.getMessageWithBrandName()
- 位置: L54-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gBrandBundle.GetStringFromName()`, `lazy.gNavigatorBundle.formatStringFromName()`

## EncryptedMediaParent.receiveMessage()
- 位置: async L61-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `console.error()`, `lazy.gNavigatorBundle.GetStringFromName()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.getMessageWithBrandName()`, `this.handledMessages.add()`, `this.handledMessages.delete()`, `this.handledMessages.has()`, `this.isKeySystemVisible()`, `this.isUiEnabled()`, `this.reportEMEDecryptionProbe()`
- 条件付き依存: `if (status == "cdm-not-installed")` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (keySystem != "org.w3.clearkey")` → `this.showPopupNotificationForSuccess()`
- 条件付き依存: `if (notificationBox.getNotificationWithValue(notificationId))` → `this.handledMessages.delete()`
- 条件付き依存: `if (supportPage)` → `buttons.push()`
- 条件付き依存: `if (buttonCallback)` → `buttons.push()`
- 条件付き依存: `if (buttonCallback)` → `lazy.gNavigatorBundle.GetStringFromName()`
- 参照: `aMessage.data`, `notificationBox.PRIORITY_INFO_HIGH`, `this.browsingContext.top.embedderElement`, `this.handledMessages`
- XPCOM: `Services.obs`

## buttonCallback()
- 位置: L119-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ensureEMEEnabled()`

## EncryptedMediaParent.showPopupNotificationForSuccess()
- 位置: async L186-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getPrefType()`, `Services.urlFormatter.formatURLPref()`, `["drmContentDisabled", "drmContentCDMInstalling"].forEach()`, `aBrowser.documentGlobal.PopupNotifications.getNotification()`, `aBrowser.documentGlobal.PopupNotifications.show()`, `aBrowser.getTabBrowser()`, `aBrowser.getTabBrowser().getNotificationBox()`, `lazy.gFluentStrings.formatValues()`, `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `notificationBox.removeNotification()`
- 条件付き依存: `if ( !Services.prefs.getPrefType(firstPlayPref) || !Services.prefs.getBoolPref(firstPlayPref) )` → `document.getElementById(anchorId).setAttribute()`
- 条件付き依存: `if ( !Services.prefs.getPrefType(firstPlayPref) || !Services.prefs.getBoolPref(firstPlayPref) )` → `document.getElementById()`
- 条件付き依存: `if ( !Services.prefs.getPrefType(firstPlayPref) || !Services.prefs.getBoolPref(firstPlayPref) )` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!( !Services.prefs.getPrefType(firstPlayPref) || !Services.prefs.getBoolPref(firstPlayPref) ))` → `document.getElementById(anchorId).removeAttribute()`
- 条件付き依存: `if (!( !Services.prefs.getPrefType(firstPlayPref) || !Services.prefs.getBoolPref(firstPlayPref) ))` → `document.getElementById()`
- 参照: `aBrowser.ownerDocument`
- XPCOM: `Services.prefs` / `Services.urlFormatter`

## EncryptedMediaParent.callback()
- 位置: L244-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aBrowser.documentGlobal.openPreferences()`

## callback()
- 位置: L254-254
- 役割: (未記入)
- 触るとき: (未記入)

## eventCallback()
- 位置: L261-261
- 役割: (未記入)
- 触るとき: (未記入)

## EncryptedMediaParent.reportEMEDecryptionProbe()
- 位置: async L278-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.getGMPContentDecryptionModuleInformation()`, `Glean.mediadrm.decryption.has_hardware_clearlead.set()`, `Glean.mediadrm.decryption.has_hardware_decryption.set()`, `Glean.mediadrm.decryption.has_software_clearlead.set()`, `Glean.mediadrm.decryption.has_wmf.set()`, `infos.push()`
- 条件付き依存: `if (ChromeUtils.getWMFContentDecryptionModuleInformation !== undefined)` → `ChromeUtils.getWMFContentDecryptionModuleInformation()`
- 条件付き依存: `if (ChromeUtils.getWMFContentDecryptionModuleInformation !== undefined)` → `infos.push()`
- 参照: `ChromeUtils.getWMFContentDecryptionModuleInformation`, `info.clearlead`, `info.isHardwareDecryption`
