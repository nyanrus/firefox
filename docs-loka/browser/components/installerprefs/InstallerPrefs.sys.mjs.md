# browser/components/installerprefs/InstallerPrefs.sys.mjs

source: browser/components/installerprefs/InstallerPrefs.sys.mjs
source-hash: dd76d44f354b23efd523728d1ddb594cf1cce82c
lines: 141

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Components.ID()`

## InstallerPrefs()
- 位置: L39-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/xre/directory-provider;1" ].getService()`, `ChromeUtils.defineLazyGetter()`, `xreDirProvider.getInstallHash()`
- 参照: `AppConstants.MOZ_APP_NAME`, `Ci.nsIXREDirProvider`, `Services.appinfo.vendor`, `this.prefsList`
- XPCOM: [`nsIXREDirProvider`](../../../toolkit/xre/nsIXREDirProvider.idl.md) / `@mozilla.org/xre/directory-provider;1` / `Services.appinfo`

## observe()
- 位置: L62-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `regKey.close()`, `this._openRegKey()`, `this._reflectPrefsToRegistry()`, `this._registerPrefListeners()`, `this.prefsList.includes()`
- 条件付き依存: `if (this.prefsList.includes(data))` → `this._reflectOnePrefToRegistry()`
- 参照: `AppConstants.platform`, `this.prefsList`, `this.prefsList.length`

## _registerPrefListeners()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`
- XPCOM: `Services.prefs`

## _cleanRegistryKey()
- 位置: L94-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `name.startsWith()`, `regKey.getValueName()`
- 条件付き依存: `if (name.startsWith(INSTALLER_PREFS_BRANCH))` → `regKey.removeValue()`
- 参照: `regKey.valueCount`

## _reflectPrefsToRegistry()
- 位置: L103-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cleanRegistryKey()`, `this._reflectOnePrefToRegistry()`, `this.prefsList.forEach()`

## _reflectOnePrefToRegistry()
- 位置: L110-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `pref.startsWith()`
- 条件付き依存: `if (value)` → `regKey.writeIntValue()`
- 条件付き依存: `if (!(value))` → `regKey.removeValue()`
- XPCOM: `Services.prefs`

## _openRegKey()
- 位置: L129-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `key.create()`
- 参照: `Ci.nsIWindowsRegKey`, `key.ACCESS_READ`, `key.ACCESS_WRITE`, `key.ROOT_KEY_CURRENT_USER`, `key.WOW64_64`, `this._registryKeyPath`
- XPCOM: [`nsIWindowsRegKey`](../../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`
