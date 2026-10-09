# browser/modules/BackgroundTask_uninstall.sys.mjs

source: browser/modules/BackgroundTask_uninstall.sys.mjs
source-hash: 5fc445fab95b5a86f4275e1b0b9a42c7493c6cf6
lines: 58

## <module>
- 役割: (未記入)

## runBackgroundTask()
- 位置: async L14-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/updates/update-manager;1"] .getService()`, `Cc["@mozilla.org/updates/update-manager;1"] .getService(Ci.nsIUpdateManager) .doUninstallCleanup()`, `console.error()`, `console.log()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `removeNotifications()`
- 条件付き依存: `if (AppConstants.platform === "win")` → `console.error()`
- 条件付き依存: `if (!(AppConstants.platform === "win"))` → `console.log()`
- 参照: `AppConstants.platform`, `Ci.nsIUpdateManager`
- XPCOM: [`nsIUpdateManager`](../../toolkit/mozapps/update/nsIUpdateService.idl.md) / `@mozilla.org/updates/update-manager;1` → `UpdateManager` (toolkit/mozapps/update/components.conf)

## removeNotifications()
- 位置: L37-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/system-alerts-service;1"] .getService()`, `Cc["@mozilla.org/system-alerts-service;1"] .getService(Ci.nsIAlertsService) .QueryInterface()`, `alertsService.removeAllNotificationsForInstall()`, `console.error()`, `console.log()`
- 条件付き依存: `if (!("nsIWindowsAlertsService" in Ci))` → `console.log()`
- 参照: `Ci.nsIAlertsService`, `Ci.nsIWindowsAlertsService`, `e.message`
- XPCOM: [`nsIAlertsService`](../../toolkit/components/alerts/nsIAlertsService.idl.md) / [`nsIWindowsAlertsService`](../../toolkit/components/alerts/nsIWindowsAlertsService.idl.md) / `@mozilla.org/system-alerts-service;1` → `nsIAlertsService` (toolkit/system/gnome/components.conf)
