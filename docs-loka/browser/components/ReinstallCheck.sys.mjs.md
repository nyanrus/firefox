# browser/components/ReinstallCheck.sys.mjs

source: browser/components/ReinstallCheck.sys.mjs
source-hash: eb97d70db4f73f75d65588debcc1c8e68714655e
lines: 58

## <module>
- 役割: Windows アンインストーラーが残す再インストールの印を読み、Firefox が再インストールされたかを判定するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## readAndClearUninstalledValue()
- 位置: L14-43
- 役割: Windows でのみ動く。HKCU の Software\Mozilla\Firefox にある Uninstalled-<チャンネル> 値を読んで削除し、値が True で削除に成功したときに true を返す。browser.disableResetPrompt が true か、チャンネル取得に失敗した場合は false。
- 触るとき: 再インストール後のリセット案内が出ない、または余計に出るときに見る。レジストリ値の名前や削除条件を変えるときも見る。
- 呼び出し先: `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (updateChannel)` → `lazy.WindowsRegistry.readRegKey()`
- 条件付き依存: `if (updateChannel)` → `lazy.WindowsRegistry.removeRegKey()`
- 参照: `AppConstants.platform`, `ChromeUtils.importESModule( "resource://gre/modules/UpdateUtils.sys.mjs" ).UpdateUtils.UpdateChannel`, `Ci.nsIWindowsRegKey.ROOT_KEY_CURRENT_USER`
- XPCOM: [`nsIWindowsRegKey`](../../xpcom/ds/nsIWindowsRegKey.idl.md) / `Services.prefs`

## wasReinstalled()
- 位置: L51-56
- 役割: readAndClearUninstalledValue() の結果を初回アクセス時だけ読んで _wasReinstalled に保持し、以後はそれを返す getter。
- 触るとき: 起動中に再インストール判定が何度も読まれても同じ値を返すかを確認するとき、またはキャッシュの扱いを変えるときに見る。
- 条件付き依存: `if (this._wasReinstalled === null)` → `readAndClearUninstalledValue()`
- 参照: `this._wasReinstalled`
