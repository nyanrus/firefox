# browser/components/ReinstallCheck.sys.mjs

source: browser/components/ReinstallCheck.sys.mjs
source-hash: eb97d70db4f73f75d65588debcc1c8e68714655e
lines: 58

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## readAndClearUninstalledValue()
- 位置: L14-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (updateChannel)` → `lazy.WindowsRegistry.readRegKey()`
- 条件付き依存: `if (updateChannel)` → `lazy.WindowsRegistry.removeRegKey()`
- 参照: `AppConstants.platform`, `ChromeUtils.importESModule( "resource://gre/modules/UpdateUtils.sys.mjs" ).UpdateUtils.UpdateChannel`, `Ci.nsIWindowsRegKey.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md) / `Services.prefs`

## wasReinstalled()
- 位置: L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._wasReinstalled === null)` → `readAndClearUninstalledValue()`
- 参照: `this._wasReinstalled`
