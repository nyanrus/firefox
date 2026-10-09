# browser/fxr/content/prefs.js

source: browser/fxr/content/prefs.js
source-hash: 769da79b6b5a3c81d740f9aa35d747c691bdbf50
lines: 118

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `initAboutInfo()`, `initClearAllData()`, `initParentDependencies()`, `initSubmitHealthReport()`, `window.addEventListener()`

## initAboutInfo()
- 位置: L24-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `Services.appinfo.version`, `document.getElementById("eFxVersion").textContent`, `document.getElementById("eFxrDate").textContent`, `document.getElementById("eFxrVersion").textContent`
- XPCOM: `Services.appinfo`

## initClearAllData()
- 位置: L32-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clearData.deleteData()`, `clearModalContainer()`, `document.body.appendChild()`, `document.getElementById()`, `document.getElementById("eClearConfirm").addEventListener()`, `eClearCancel.addEventListener()`, `eClearTry.addEventListener()`, `showModalContainer()`
- 条件付き依存: `if (aFailedFlags == 0)` → `document.body.appendChild()`
- 条件付き依存: `if (aFailedFlags == 0)` → `clearModalContainer()`
- 参照: `Ci.nsIClearDataService.CLEAR_ALL`, `eClearTry.disabled`, `eClearTry.textContent`
- XPCOM: [`nsIClearDataService`](../../../toolkit/components/cleardata/nsIClearDataService.idl.md) / `Services.clearData`

## initSubmitHealthReport()
- 位置: L67-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`, `document.getElementById()`
- 条件付き依存: `if (!( Services.prefs.prefIsLocked(PREF_UPLOAD_ENABLED) || !AppConstants.MOZ_TELEMETRY_REPORTING ))` → `checkbox.addEventListener()`
- 条件付き依存: `if (!( Services.prefs.prefIsLocked(PREF_UPLOAD_ENABLED) || !AppConstants.MOZ_TELEMETRY_REPORTING ))` → `Services.prefs.getBoolPref()`
- 参照: `AppConstants.MOZ_TELEMETRY_REPORTING`, `checkbox.checked`, `checkbox.disabled`
- XPCOM: `Services.prefs`

## updateSubmitHealthReport()
- 位置: L90-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `document.getElementById()`
- 参照: `checkbox.checked`
- XPCOM: `Services.prefs`

## initParentDependencies()
- 位置: L97-117
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (window.parent != window)` → `document.getElementById("eCloseSettings").addEventListener()`
- 条件付き依存: `if (window.parent != window)` → `document.getElementById()`
- 条件付き依存: `if (window.parent != window)` → `window.parent.closeSettings()`
- 条件付き依存: `if (window.parent != window)` → `document.getElementById("ePrivacyPolicy").addEventListener()`
- 条件付き依存: `if (window.parent != window)` → `window.parent.showPrivacyPolicy()`
- 条件付き依存: `if (window.parent != window)` → `document.getElementById("eLicenseInfo").addEventListener()`
- 条件付き依存: `if (window.parent != window)` → `window.parent.showLicenseInfo()`
- 条件付き依存: `if (window.parent != window)` → `document.getElementById("eReportIssue").addEventListener()`
- 条件付き依存: `if (window.parent != window)` → `window.parent.showReportIssue()`
- 参照: `window.parent`
