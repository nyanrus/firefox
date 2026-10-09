# browser/modules/BackgroundTask_install.sys.mjs

source: browser/modules/BackgroundTask_install.sys.mjs
source-hash: 4f1d43cbbfa3deafd8d27f6806bd418c4684c8a0
lines: 29

## <module>
- 役割: インストール時に実行されるバックグラウンドタスクの本体。

## runBackgroundTask()
- 位置: async L17-28
- 役割: 更新マネージャーの doInstallCleanup を呼んで、更新ファイルの後始末をする。例外はログに出して続行する。
- 触るとき: インストール時に後始末する対象や順序を変えるとき。タイムアウトは backgroundTaskTimeoutSec(30 秒)で決まる。
- 呼び出し先: `Cc["@mozilla.org/updates/update-manager;1"] .getService()`, `Cc["@mozilla.org/updates/update-manager;1"] .getService(Ci.nsIUpdateManager) .doInstallCleanup()`, `console.error()`, `console.log()`
- 参照: `Ci.nsIUpdateManager`
- XPCOM: [`nsIUpdateManager`](../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-manager;1` → `UpdateManager` (toolkit/mozapps/update/components.conf)
