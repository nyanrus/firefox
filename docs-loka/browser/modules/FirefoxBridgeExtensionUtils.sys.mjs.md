# browser/modules/FirefoxBridgeExtensionUtils.sys.mjs

source: browser/modules/FirefoxBridgeExtensionUtils.sys.mjs
source-hash: e1222db6e0b3b16186f2970e7beb68422eb37aad
lines: 268

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.getApplicationPath()
- 位置: L17-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.openRegistryRoot()
- 位置: L21-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `wrk.open()`
- 参照: `Ci.nsIWindowsRegKey`, `wrk.ACCESS_ALL`, `wrk.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.deleteChildren()
- 位置: L31-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `child.close()`, `start.getChildName()`, `start.openChild()`, `start.removeChild()`, `this.deleteChildren()`
- 参照: `start.ACCESS_ALL`, `start.childCount`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.deleteRegistryTree()
- 位置: L45-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `root.openChild()`, `root.removeChild()`, `start.close()`, `this.deleteChildren()`
- 参照: `root.ACCESS_ALL`

## maybeDeleteBridgeProtocolRegistryEntries()
- 位置: L79-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `deleteBridgeProtocolRegistryEntryHelper.getApplicationPath()`, `deleteBridgeProtocolRegistryEntryHelper.openRegistryRoot()`, `maybeDeleteRegistryKey()`, `wrk.close()`
- 参照: `this.PRIVATE_PROTOCOL`, `this.PUBLIC_PROTOCOL`

## maybeDeleteRegistryKey()
- 位置: L88-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `wrk.hasChild()`
- 条件付き依存: `if (wrk.hasChild(openCommandPath))` → `wrk.openChild()`
- 条件付き依存: `if (openCommandKey.valueCount == 1)` → `openCommandKey.getValueName()`
- 条件付き依存: `if (openCommandKey.getValueName(0) == defaultKeyName)` → `openCommandKey.getValueType()`
- 条件付き依存: `if ( openCommandKey.getValueType(defaultKeyName) == Ci.nsIWindowsRegKey.TYPE_STRING )` → `openCommandKey.readStringValue()`
- 条件付き依存: `if (wrk.hasChild(openCommandPath))` → `openCommandKey.close()`
- 条件付き依存: `if (deleteProtocolEntry)` → `deleteBridgeProtocolRegistryEntryHelper.deleteRegistryTree()`
- 参照: `Ci.nsIWindowsRegKey.TYPE_STRING`, `openCommandKey.valueCount`, `wrk.ACCESS_READ`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md)

## getNativeMessagingHostId()
- 位置: L137-147
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AppConstants.IS_ESR`, `AppConstants.MOZ_DEV_EDITION`, `AppConstants.NIGHTLY_BUILD`

## getExtensionOrigins()
- 位置: L149-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getStringPref()`, `Services.prefs .getStringPref("browser.firefoxbridge.extensionOrigins", "") .split()`
- XPCOM: `Services.prefs`

## maybeWriteManifestFiles()
- 位置: async L155-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getFile()`, `IOUtils.readJSON()`, `Services.dirsvc.get()`, `console.error()`, `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `binFile.append()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `binFile.append()`
- 条件付き依存: `if (!correctFileExists)` → `IOUtils.writeJSON()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).parent`, `binFile.path`, `nmhManifestFile.path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## ensureRegistered()
- 位置: async L201-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getExtensionOrigins()`, `this.getNativeMessagingHostId()`, `this.maybeWriteManifestFiles()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `PathUtils.join()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.dirsvc.get()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.maybeWriteNativeMessagingRegKeys()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.getNativeMessagingHostId()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `Services.dirsvc.get("AppData", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## maybeWriteNativeMessagingRegKeys()
- 位置: L231-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `PathUtils.join()`, `wrk.close()`, `wrk.create()`, `wrk.readStringValue()`, `wrk.writeStringValue()`
- 参照: `Ci.nsIWindowsRegKey`, `wrk.ACCESS_ALL`, `wrk.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`
