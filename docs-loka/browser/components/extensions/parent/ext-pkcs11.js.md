# browser/components/extensions/parent/ext-pkcs11.js

source: browser/components/extensions/parent/ext-pkcs11.js
source-hash: bde94fb3c31e21b718c29d8b6a65bb605cb99967
lines: 193

## <module>
- 役割: pkcs11 WebExtension API の実装。ネイティブマニフェストで指定された PKCS#11 モジュールの導入、削除、スロット一覧を扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## findModuleByPath()
- 位置: async L21-28
- 役割: nsIPKCS11ModuleDB に登録済みのモジュールから、libName がパスと一致するものを探して返す。
- 触るとき: インストール済み判定やアンインストールで対象モジュールを特定する処理を変えるとき。見つからなければ null を返す。
- 呼び出し先: `pkcs11db.listModules()`
- 参照: `module.libName`

## getAPI()
- 位置: L31-191
- 役割: マニフェスト取得をキャッシュする DefaultMap を作り、pkcs11 API の 4 メソッドを返す。
- 触るとき: 拡張から見える pkcs11 API を増やすときや、マニフェストの検証条件を変えるとき。
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
- 役割: マニフェストのパスで登録済みモジュールを探し、あれば true を返す。
- 触るとき: 拡張が導入状況を問い合わせた際に true/false が想定と違うとき。マニフェストが無ければ reject する。
- 呼び出し先: `findModuleByPath()`, `manifestCache.get()`
- 参照: `manifest.path`

## installModule()
- 位置: async L104-117
- 役割: マニフェストの description を使って nsIPKCS11ModuleDB.addModule でモジュールを登録する。
- 触るとき: モジュール導入が失敗するとき。description が空だと先に reject される。flags は既定 0 で呼び出し側から渡せる。
- 呼び出し先: `manifestCache.get()`, `pkcs11db.addModule()`
- 条件付き依存: `if (!manifest.description)` → `Promise.reject()`
- 参照: `manifest.description`, `manifest.path`

## uninstallModule()
- 位置: async L128-137
- 役割: マニフェストのパスで登録済みモジュールを探し、見つかれば deleteModule で削除する。
- 触るとき: アンインストールが効かないときや、削除対象の決め方を確認するとき。未登録なら reject する。
- 呼び出し先: `findModuleByPath()`, `manifestCache.get()`, `pkcs11db.deleteModule()`
- 条件付き依存: `if (!module)` → `Promise.reject()`
- 参照: `manifest.path`, `module.name`

## getModuleSlots()
- 位置: async L157-188
- 役割: 登録済みモジュールの各スロットを走査し、名前と (有効なスロットなら) トークン情報を配列で返す。
- 触るとき: 拡張に返すスロットやトークンの項目を増やすとき、またはスマートカードの状態表示が想定とずれるとき。無効または未装着のスロットは token が null になる。
- 呼び出し先: `findModuleByPath()`, `manifestCache.get()`, `rv.push()`
- 条件付き依存: `if (!module)` → `Promise.reject()`
- 条件付き依存: `if ( slot.status != Ci.nsIPKCS11Slot.SLOT_DISABLED && slot.status != Ci.nsIPKCS11Slot.SLOT_NOT_PRESENT )` → `slot.getToken()`
- 参照: `Ci.nsIPKCS11Slot.SLOT_DISABLED`, `Ci.nsIPKCS11Slot.SLOT_NOT_PRESENT`, `manifest.path`, `module.slots`, `slot.name`, `slot.status`, `slotobj.token`, `token.isLoggedIn`, `token.tokenFWVersion`, `token.tokenHWVersion`, `token.tokenManID`, `token.tokenName`, `token.tokenSerialNumber`
- XPCOM: `nsIPKCS11Slot`
