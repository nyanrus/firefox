# browser/actors/EncryptedMediaParent.sys.mjs

source: browser/actors/EncryptedMediaParent.sys.mjs
source-hash: 8bdeba9b8803354e23a3881147fee6a6af94a63b
lines: 316

## <module>
- 役割: EME(暗号化メディア拡張)で DRM コンテンツを再生できない時などに、利用者への案内と DRM の利用状況の記録を行う親側アクター。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## EncryptedMediaParent.isUiEnabled()
- 位置: L24-26
- 役割: EME の UI を表示する設定を読む。
- 触るとき: DRM 案内を出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## EncryptedMediaParent.ensureEMEEnabled()
- 位置: L28-39
- 役割: EME を有効にし、キーシステムが Widevine なら CDM も有効にして、ページを再読み込みする。
- 触るとき: DRM を有効化する操作の内容を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getPrefType()`, `Services.prefs.setBoolPref()`, `aBrowser.reload()`
- 条件付き依存: `if ( aKeySystem && aKeySystem == "com.widevine.alpha" && Services.prefs.getPrefType("media.gmp-widevinecdm.enabled") && !Services.prefs.getBoolPref("media.gmp-wi...)` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## EncryptedMediaParent.isKeySystemVisible()
- 位置: L41-52
- 役割: キーシステムを案内の対象にするかを返す。Widevine は表示設定の pref に従い、それ以外は対象とする。
- 触るとき: 案内の対象となるキーシステムを変えるとき。
- 呼び出し先: `Services.prefs.getPrefType()`
- 条件付き依存: `if ( aKeySystem == "com.widevine.alpha" && Services.prefs.getPrefType("media.gmp-widevinecdm.visible") )` → `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## EncryptedMediaParent.getMessageWithBrandName()
- 位置: L54-59
- 役割: 通知の文言 ID を作り、ブランド名を入れた文字列を返す。
- 触るとき: 通知文言の組み立て方を変えるとき。
- 呼び出し先: `lazy.gBrandBundle.GetStringFromName()`, `lazy.gNavigatorBundle.formatStringFromName()`

## EncryptedMediaParent.receiveMessage()
- 位置: async L61-184
- 役割: ページからの CDM の状態を読み、再生成功時の案内の更新、DRM 無効や CDM 未インストールの通知を出す。同じ通知は重ねない。
- 触るとき: DRM 関連の通知の表示条件や内容を変えるとき。
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
- 役割: 「管理」ボタンから EME を有効化する。
- 触るとき: DRM 無効の通知のボタンの動作を変えるとき。
- 呼び出し先: `this.ensureEMEEnabled()`

## EncryptedMediaParent.showPopupNotificationForSuccess()
- 位置: async L186-276
- 役割: DRM 失敗の通知を消し、DRM 再生中の案内を出す。初回は firstplay 属性と設定を立てる。
- 触るとき: 再生中の案内の表示を変えるとき。
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
- 役割: 再生中案内の「管理」ボタンで、一般設定の DRM の項目を開く。
- 触るとき: 設定画面への導線を変えるとき。
- 呼び出し先: `aBrowser.documentGlobal.openPreferences()`

## callback()
- 位置: L254-254
- 役割: 「閉じる」ボタンの処理で、何もせずに閉じる。
- 触るとき: 閉じるボタンの動作を変えるとき。

## eventCallback()
- 位置: L261-261
- 役割: パネルのイベントのうち、タブの入れ替えの時だけ真を返す。
- 触るとき: タブ移動時の案内の扱いを変えるとき。

## EncryptedMediaParent.reportEMEDecryptionProbe()
- 位置: async L278-314
- 役割: GMP と WMF の CDM の情報を集め、ハードウェア復号やクリアリードの有無を Glean に記録する。
- 触るとき: DRM 対応状況のテレメトリを変えるとき。
- 呼び出し先: `ChromeUtils.getGMPContentDecryptionModuleInformation()`, `Glean.mediadrm.decryption.has_hardware_clearlead.set()`, `Glean.mediadrm.decryption.has_hardware_decryption.set()`, `Glean.mediadrm.decryption.has_software_clearlead.set()`, `Glean.mediadrm.decryption.has_wmf.set()`, `infos.push()`
- 条件付き依存: `if (ChromeUtils.getWMFContentDecryptionModuleInformation !== undefined)` → `ChromeUtils.getWMFContentDecryptionModuleInformation()`
- 条件付き依存: `if (ChromeUtils.getWMFContentDecryptionModuleInformation !== undefined)` → `infos.push()`
- 参照: `ChromeUtils.getWMFContentDecryptionModuleInformation`, `info.clearlead`, `info.isHardwareDecryption`
