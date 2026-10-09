# browser/modules/FirefoxBridgeExtensionUtils.sys.mjs

source: browser/modules/FirefoxBridgeExtensionUtils.sys.mjs
source-hash: e1222db6e0b3b16186f2970e7beb68422eb37aad
lines: 268

## <module>
- 役割: Firefox Bridge 拡張向けの Windows レジストリ登録と NMH マニフェストを管理する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.getApplicationPath()
- 位置: L17-19
- 役割: 現在の実行ファイル(XREExeF)のパスを返す。
- 触るとき: レジストリの登録値と比較するパス文字列の生成元を確かめるとき。
- 呼び出し先: `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.openRegistryRoot()
- 位置: L21-29
- 役割: HKCU の Software\Classes キーを全権限で開いて返す。
- 触るとき: プロトコル登録の削除対象になるレジストリのルートを変えるとき。
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `wrk.open()`
- 参照: `Ci.nsIWindowsRegKey`, `wrk.ACCESS_ALL`, `wrk.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.deleteChildren()
- 位置: L31-43
- 役割: 子キーを末尾から再帰的に削除する。
- 触るとき: レジストリ木を削除する手順を変えるとき。逆順にすることで削除中の添字ずれを防いでいる。
- 呼び出し先: `child.close()`, `start.getChildName()`, `start.openChild()`, `start.removeChild()`, `this.deleteChildren()`
- 参照: `start.ACCESS_ALL`, `start.childCount`

## DeleteBridgeProtocolRegistryEntryHelperImplementation.deleteRegistryTree()
- 位置: L45-51
- 役割: 指定したプロトコルキーの子を全て消してから、キー自体を削除する。
- 触るとき: 古い firefox-bridge 系プロトコルの登録を消す処理の後始末を確かめるとき。
- 呼び出し先: `root.openChild()`, `root.removeChild()`, `start.close()`, `this.deleteChildren()`
- 参照: `root.ACCESS_ALL`

## maybeDeleteBridgeProtocolRegistryEntries()
- 位置: L79-135
- 役割: このインストールが作った firefox-bridge 系の登録だけを条件付きで削除する。
- 触るとき: アンインストールや起動時のクリーンアップで、他のアプリの登録を消してしまう疑いを調べるとき。open コマンド文字列が完全一致した場合のみ削除する。エラーはコンソールに出す。
- 呼び出し先: `console.error()`, `deleteBridgeProtocolRegistryEntryHelper.getApplicationPath()`, `deleteBridgeProtocolRegistryEntryHelper.openRegistryRoot()`, `maybeDeleteRegistryKey()`, `wrk.close()`
- 参照: `this.PRIVATE_PROTOCOL`, `this.PUBLIC_PROTOCOL`

## maybeDeleteRegistryKey()
- 位置: L88-123
- 役割: shell\open\command の既定値が期待文字列と一致するプロトコルキーを削除対象にする。
- 触るとき: 削除判定の条件(値の型、値の数、文字列の一致)を変えるとき。既定値が文字列でないか、値の数が1つでなければ削除しない。
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
- 役割: ビルド種別に応じた NMH のホスト ID を返す。
- 触るとき: ナイトリー、dev、ESR で別の NMH 名を使う理由や、マニフェストのファイル名を確かめるとき。
- 参照: `AppConstants.IS_ESR`, `AppConstants.MOZ_DEV_EDITION`, `AppConstants.NIGHTLY_BUILD`

## getExtensionOrigins()
- 位置: L149-153
- 役割: browser.firefoxbridge.extensionOrigins をカンマで分割した配列を返す。
- 触るとき: NMH マニフェストに許可する拡張のオリジン一覧の出どころを確かめるとき。
- 呼び出し先: `Services.prefs .getStringPref()`, `Services.prefs .getStringPref("browser.firefoxbridge.extensionOrigins", "") .split()`
- XPCOM: `Services.prefs`

## maybeWriteManifestFiles()
- 位置: async L155-199
- 役割: nmhproxy のパスと許可オリジンを含む NMH マニフェスト JSON を、内容が違う時だけ書き出す。
- 触るとき: マニフェストの中身(name, path, allowed_origins)を変えるとき、または NMH が見つからない報告を調べるとき。Windows と macOS 以外は例外になり、ログに残る。
- 呼び出し先: `IOUtils.getFile()`, `IOUtils.readJSON()`, `Services.dirsvc.get()`, `console.error()`, `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `binFile.append()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `binFile.append()`
- 条件付き依存: `if (!correctFileExists)` → `IOUtils.writeJSON()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).parent`, `binFile.path`, `nmhManifestFile.path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## ensureRegistered()
- 位置: async L201-229
- 役割: OS ごとのマニフェスト置き場を決め、マニフェストを書き、Windows なら登録キーも書く。
- 触るとき: Bridge の NMH 登録の入口を変えるとき、または Windows と macOS で登録先が違う理由を確かめるとき。Windows 以外の platform では例外を投げる。
- 呼び出し先: `this.getExtensionOrigins()`, `this.getNativeMessagingHostId()`, `this.maybeWriteManifestFiles()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `PathUtils.join()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.dirsvc.get()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.maybeWriteNativeMessagingRegKeys()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `this.getNativeMessagingHostId()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `Services.dirsvc.get("AppData", Ci.nsIFile).path`
- XPCOM: [`nsIFile`](../components/shell/nsIShellService.idl.md) / `Services.dirsvc`

## maybeWriteNativeMessagingRegKeys()
- 位置: L231-266
- 役割: HKCU の Chrome 向け NativeMessagingHosts キーの既定値に、マニフェストのパスを書き込む。
- 触るとき: Windows で Chrome 系ブラウザが NMH を見つけられない報告を調べるとき。値が既に正しければ何もせず、失敗は無視する。
- 呼び出し先: `Cc["@mozilla.org/windows-registry-key;1"].createInstance()`, `PathUtils.join()`, `wrk.close()`, `wrk.create()`, `wrk.readStringValue()`, `wrk.writeStringValue()`
- 参照: `Ci.nsIWindowsRegKey`, `wrk.ACCESS_ALL`, `wrk.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md) / `@mozilla.org/windows-registry-key;1`
