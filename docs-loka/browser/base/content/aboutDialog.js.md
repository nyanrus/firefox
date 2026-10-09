# browser/base/content/aboutDialog.js

source: browser/base/content/aboutDialog.js
source-hash: 9ce7aa058ce2156bcb213984416282da05d7e69b
lines: 204

## <module>
- 役割: about:dialog(バージョン情報)のスクリプト。更新 UI の読み込みも行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `init()`

## init()
- 位置: L27-201
- 役割: バージョン表示、配布元情報、リリースノートのリンク、チャンネル表示、寄付説明の切り替え、更新ボタンの配線を初期化する。
- 触るとき: バージョン情報ダイアログの表示項目を変える、または更新ボタンの動作を変えるとき。
- 呼び出し先: `/a\d+$/.test()`, `Services.prefs.getBoolPref()`, `Services.prefs.getDefaultBranch()`, `Services.prefs.getPrefType()`, `Services.sysinfo.get()`, `["x86", "x86-64"].includes()`, `[...new Set(describedBy)].join()`, `defaults.getCharPref()`, `defaults.getStringPref()`, `document .getElementById()`, `document .getElementById("aboutDialogEscapeKey") .addEventListener()`, `document.documentElement .getAttribute()`, `document.documentElement .getAttribute("aria-describedby") .split()`, `document.documentElement .getAttribute("aria-describedby") .split(" ") .map()`, `document.documentElement.setAttribute()`, `document.getElementById()`, `document.l10n.setAttributes()`, `versionIdMap.get()`, `window.close()`
- 条件付き依存: `if (distroId && distroAbout)` → `document.getElementById()`
- 条件付き依存: `if (distroId && distroAbout)` → `defaults.getCharPref()`
- 条件付き依存: `if (/a\d+$/.test(version))` → `buildID.slice()`
- 条件付き依存: `if (/a\d+$/.test(version))` → `document.getElementById()`
- 条件付き依存: `if (relNotesPrefType != Services.prefs.PREF_INVALID)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document.l10n.getAttributes()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `/^release($|\-)/.test()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `Services.sysinfo.getProperty()`
- 条件付き依存: `if (referralsEnabled)` → `contributeDescReferrals.addEventListener()`
- 条件付き依存: `if (referralsEnabled)` → `event.target.closest()`
- 条件付き依存: `if ( event.target.closest('[data-l10n-name="helpus-shareFirefoxLink"]') )` → `event.preventDefault()`
- 条件付き依存: `if ( event.target.closest('[data-l10n-name="helpus-shareFirefoxLink"]') )` → `lazy.Referrals.openReferralsTab()`
- 条件付き依存: `if (AppConstants.IS_ESR)` → `document.getElementById()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document .getElementById("aboutDialogHelpLink") .addEventListener()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document .getElementById()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `openHelpLink()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document .getElementById("submit-feedback") .addEventListener()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document .getElementById("checkForUpdatesButton") .addEventListener()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `gAppUpdater.checkForUpdates()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document .getElementById("downloadAndInstallButton") .addEventListener()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `gAppUpdater.startDownload()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `document.getElementById("updateButton").addEventListener()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `gAppUpdater.buttonRestartAfterDownload()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `window.addEventListener()`
- 条件付き依存: `if (AppConstants.MOZ_UPDATER)` → `onUnload()`
- 参照: `AppConstants.IS_ESR`, `AppConstants.MOZ_APP_VERSION_DISPLAY`, `AppConstants.MOZ_UPDATER`, `Services.appinfo.appBuildID`, `Services.appinfo.is64Bit`, `Services.appinfo.version`, `Services.prefs.PREF_INVALID`, `UpdateUtils.UpdateChannel`, `channelAttrs.id`, `channelLabel.hidden`, `contributeDescReferrals.hidden`, `distroField.style.display`, `distroField.value`, `distroIdField.style.display`, `distroIdField.value`, `document.getElementById("communityDesc").hidden`, `document.getElementById("contributeDesc").hidden`, `document.getElementById("experimental").hidden`, `document.getElementById("release").hidden`, `relNotesLink.hidden`, `relNotesLink.href`, `versionAttributes.arch`, `versionAttributes.bits`, `versionAttributes.isodate`
- XPCOM: `Services.appinfo` / `Services.prefs` / `Services.sysinfo` / `Services.urlFormatter`
