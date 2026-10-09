# browser/components/extensions/parent/ext-pkcs11.js

source: browser/components/extensions/parent/ext-pkcs11.js
source-hash: bde94fb3c31e21b718c29d8b6a65bb605cb99967
lines: 193

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## findModuleByPath()
- 位置: async L21-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pkcs11db.listModules()`
- 参照: `module.libName`

## getAPI()
- 位置: L31-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NativeManifests.lookupManifest()`, `Promise.reject()`
- 条件付き依存: `if (hostInfo)` → `PathUtils.isAbsolute()`
- 条件付き依存: `if (hostInfo)` → `PathUtils.joinRelative()`
- 条件付き依存: `if (hostInfo)` → `PathUtils.parent()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `PathUtils.normalize()`
- 条件付き依存: `if (hostInfo)` → `PathUtils.filename()`
- 条件付き依存: `if (AppConstants.platform !== "linux")` → `manifestLib.toLowerCase()`
- 条件付き依存: `if (hostInfo)` → `ctypes.libraryName()`
- 参照: `AppConstants.platform`, `hostInfo.manifest`, `hostInfo.manifest.path`, `hostInfo.path`

## isModuleInstalled()
- 位置: async L88-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findModuleByPath()`, `manifestCache.get()`
- 参照: `manifest.path`

## installModule()
- 位置: async L104-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manifestCache.get()`, `pkcs11db.addModule()`
- 条件付き依存: `if (!manifest.description)` → `Promise.reject()`
- 参照: `manifest.description`, `manifest.path`

## uninstallModule()
- 位置: async L128-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findModuleByPath()`, `manifestCache.get()`, `pkcs11db.deleteModule()`
- 条件付き依存: `if (!module)` → `Promise.reject()`
- 参照: `manifest.path`, `module.name`

## getModuleSlots()
- 位置: async L157-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findModuleByPath()`, `manifestCache.get()`, `rv.push()`
- 条件付き依存: `if (!module)` → `Promise.reject()`
- 条件付き依存: `if ( slot.status != Ci.nsIPKCS11Slot.SLOT_DISABLED && slot.status != Ci.nsIPKCS11Slot.SLOT_NOT_PRESENT )` → `slot.getToken()`
- 参照: `Ci.nsIPKCS11Slot.SLOT_DISABLED`, `Ci.nsIPKCS11Slot.SLOT_NOT_PRESENT`, `manifest.path`, `module.slots`, `slot.name`, `slot.status`, `slotobj.token`, `token.isLoggedIn`, `token.tokenFWVersion`, `token.tokenHWVersion`, `token.tokenManID`, `token.tokenName`, `token.tokenSerialNumber`
- XPCOM: `nsIPKCS11Slot`
