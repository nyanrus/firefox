# browser/components/preferences/dialogs/connection.js

source: browser/components/preferences/dialogs/connection.js
source-hash: c39d0684dbeed5dd6909a7411fa59425ca631c4d
lines: 432

## <module>
- 役割: (未記入)
- 呼び出し先: `Preferences.addAll()`, `Preferences.close()`, `Preferences.get()`, `Preferences.get("network.proxy.socks_version").on()`, `Preferences.get("network.proxy.type").on()`, `document .getElementById()`, `document .getElementById("ConnectionsDialog") .addEventListener()`, `document .getElementById("autoReload") .addEventListener()`, `document .getElementById("disableProxyExtension") .addEventListener()`, `document .getElementById("key_close") .addEventListener()`, `document .getElementById("networkProxyAutoconfigURL") .addEventListener()`, `gConnectionsDialog.beforeAccept()`, `gConnectionsDialog.checkForSystemProxy()`, `gConnectionsDialog.proxyTypeChanged.bind()`, `gConnectionsDialog.registerSyncPrefListeners()`, `gConnectionsDialog.reloadPAC()`, `gConnectionsDialog.updateDNSPref.bind()`, `gConnectionsDialog.updateProxySettingsUI()`, `gConnectionsDialog.updateReloadButton()`, `initializeProxyUI()`, `makeDisableControllingExtension()`, `makeDisableControllingExtension(PREF_SETTING_TYPE, PROXY_KEY).bind()`, `window.addEventListener()`

## beforeAccept()
- 位置: L88-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.networkProxySettings.proxyTypePreference.record()`, `PROXY_TYPES_MAP_REVERSE.get()`, `Preferences.get()`, `this.sanitizeNoProxiesPref()`
- 条件付き依存: `if (proxyTypePref.value == 2)` → `this.doAutoconfigURLFixup()`
- 条件付き依存: `if (proxyPortPref.value == 0)` → `document .getElementById("networkProxy" + prefName.toUpperCase() + "_Port") .focus()`
- 条件付き依存: `if (proxyPortPref.value == 0)` → `document .getElementById()`
- 条件付き依存: `if (proxyPortPref.value == 0)` → `prefName.toUpperCase()`
- 条件付き依存: `if (proxyPortPref.value == 0)` → `event.preventDefault()`
- 条件付き依存: `if (!(proxyPortPref.value == 0))` → `Services.io.isValidHostname()`
- 条件付き依存: `if (!Services.io.isValidHostname(proxyPref.value))` → `document .getElementById("networkProxy" + prefName.toUpperCase()) .focus()`
- 条件付き依存: `if (!Services.io.isValidHostname(proxyPref.value))` → `document .getElementById()`
- 条件付き依存: `if (!Services.io.isValidHostname(proxyPref.value))` → `prefName.toUpperCase()`
- 条件付き依存: `if (!Services.io.isValidHostname(proxyPref.value))` → `event.preventDefault()`
- 条件付き依存: `if (shareProxiesPref.value)` → `Preferences.get()`
- 参照: `backupPortPref.value`, `backupServerURLPref.value`, `httpProxyPortPref.value`, `httpProxyURLPref.value`, `proxyPortPref.value`, `proxyPref.value`, `proxyServerURLPref.value`, `proxyTypePref.value`, `shareProxiesPref.value`
- XPCOM: `Services.io`

## checkForSystemProxy()
- 位置: L157-169
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("@mozilla.org/system-proxy-settings;1" in Cc)` → `document.getElementById("systemPref").removeAttribute()`
- 条件付き依存: `if ("@mozilla.org/system-proxy-settings;1" in Cc)` → `document.getElementById()`
- 条件付き依存: `if ("@mozilla.org/system-proxy-settings;1" in Cc)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (systemWpadAllowed && AppConstants.platform == "win")` → `document.getElementById("systemWpad").removeAttribute()`
- 条件付き依存: `if (systemWpadAllowed && AppConstants.platform == "win")` → `document.getElementById()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.prefs`

## proxyTypeChanged()
- 位置: L171-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Services.prefs.getBoolPref()`, `autoconfigURLPref.updateControlDisabledState()`, `autologinProxyPref.updateControlDisabledState()`, `document.getElementById()`, `httpProxyPortPref.updateControlDisabledState()`, `httpProxyURLPref.updateControlDisabledState()`, `noProxiesPref.updateControlDisabledState()`, `shareProxiesPref.updateControlDisabledState()`, `systemWpadPref.updateControlDisabledState()`, `this.updateProtocolPrefs()`, `this.updateReloadButton()`
- 参照: `document.getElementById("networkProxyNoneLocalhost").hidden`, `proxyTypePref.value`
- XPCOM: `Services.prefs`

## updateDNSPref()
- 位置: L206-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `socks4DNSPref.updateControlDisabledState()`, `socks5DNSPref.updateControlDisabledState()`
- 参照: `proxyTypePref.value`, `socksVersionPref.value`

## updateReloadButton()
- 位置: L224-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Services.prefs.getCharPref()`, `Services.prefs.getIntPref()`, `disableReloadPref.updateControlDisabledState()`, `document.getElementById()`
- 参照: `Preferences.get("network.proxy.type").value`, `document.getElementById("networkProxyAutoconfigURL").value`
- XPCOM: `Services.prefs`

## readProxyType()
- 位置: L244-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.proxyTypeChanged()`

## updateProtocolPrefs()
- 位置: L249-295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `proxyPortPref.updateControlDisabledState()`, `proxyPortPref.updateElements()`, `proxyServerURLPref.updateControlDisabledState()`, `proxyServerURLPref.updateElements()`, `socksVersionPref.updateControlDisabledState()`, `this.updateDNSPref()`
- 条件付き依存: `if (proxyPrefs[i] != "socks" && !shareProxiesPref.value)` → `Preferences.get()`
- 条件付き依存: `if (backupServerURLPref.hasUserValue)` → `backupServerURLPref.reset()`
- 条件付き依存: `if (backupPortPref.hasUserValue)` → `backupPortPref.reset()`
- 参照: `backupPortPref.hasUserValue`, `backupPortPref.value`, `backupServerURLPref.hasUserValue`, `backupServerURLPref.value`, `proxyPortPref.value`, `proxyPrefs.length`, `proxyServerURLPref.value`, `proxyTypePref.value`, `shareProxiesPref.value`

## readProxyProtocolPref()
- 位置: L297-315
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (aProtocol != "socks")` → `Preferences.get()`
- 条件付き依存: `if (shareProxiesPref.value)` → `Preferences.get()`
- 参照: `backupPref.hasUserValue`, `backupPref.value`, `pref.value`, `shareProxiesPref.value`

## reloadPAC()
- 位置: L317-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/network/protocol-proxy-service;1"] .getService()`, `Cc["@mozilla.org/network/protocol-proxy-service;1"] .getService() .reloadPAC()`
- XPCOM: `@mozilla.org/network/protocol-proxy-service;1`

## doAutoconfigURLFixup()
- 位置: L323-331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `Services.uriFixup.getFixupURIInfo()`, `document.getElementById()`
- 参照: `Services.uriFixup.getFixupURIInfo( autoURL.value ).preferredURI.spec`, `autoURL.value`, `autoURLPref.value`
- XPCOM: `Services.uriFixup`

## sanitizeNoProxiesPref()
- 位置: L333-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `noProxiesPref.value.replace()`
- 参照: `noProxiesPref.value`

## readHTTPProxyServer()
- 位置: L345-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 条件付き依存: `if (shareProxiesPref.value)` → `this.updateProtocolPrefs()`
- 参照: `shareProxiesPref.value`

## readHTTPProxyPort()
- 位置: L355-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 条件付き依存: `if (shareProxiesPref.value)` → `this.updateProtocolPrefs()`
- 参照: `shareProxiesPref.value`

## getProxyControls()
- 位置: L365-375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controlGroup.querySelectorAll()`, `document.getElementById()`, `document.querySelectorAll()`

## updateProxySettingsUI()
- 位置: async L379-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `API_PROXY_PREFS.some()`, `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (isLocked)` → `hideControllingExtension()`
- 条件付き依存: `if (!(isLocked))` → `handleControllingExtension(PREF_SETTING_TYPE, PROXY_KEY).then()`
- 条件付き依存: `if (!(isLocked))` → `handleControllingExtension()`
- XPCOM: `Services.prefs`

## setInputsDisabledState()
- 位置: L384-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gConnectionsDialog.getProxyControls()`, `gConnectionsDialog.proxyTypeChanged()`
- 参照: `element.disabled`

## registerSyncPrefListeners()
- 位置: L401-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setSyncFromPrefListener()`, `this.readHTTPProxyPort()`, `this.readHTTPProxyServer()`, `this.readProxyProtocolPref()`, `this.readProxyType()`, `this.updateProtocolPrefs()`

## setSyncFromPrefListener()
- 位置: L402-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addSyncFromPrefListener()`, `document.getElementById()`
