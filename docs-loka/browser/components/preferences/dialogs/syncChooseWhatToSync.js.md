# browser/components/preferences/dialogs/syncChooseWhatToSync.js

source: browser/components/preferences/dialogs/syncChooseWhatToSync.js
source-hash: 68780e5ebd91eb8b0a6ca5841c95cd1245964441
lines: 127

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ChromeUtils.importESModule( "resource://gre/modules/FxAccounts.sys.mjs" ).getFxAccountsSingleton()`, `Preferences.addAll()`, `Services.prefs.getBoolPref()`, `gSyncChooseWhatToSync.init()`, `window.addEventListener()`

## init()
- 位置: L36-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._adjustForPrefs()`, `this._setupEventListeners()`
- 条件付き依存: `if (options.disconnectFun)` → `document.addEventListener()`
- 条件付き依存: `if (options.disconnectFun)` → `options.disconnectFun().then()`
- 条件付き依存: `if (options.disconnectFun)` → `options.disconnectFun()`
- 条件付き依存: `if (disconnected)` → `window.close()`
- 条件付き依存: `if (!(options.disconnectFun))` → `document.getElementById("syncChooseOptions").getButton()`
- 条件付き依存: `if (!(options.disconnectFun))` → `document.getElementById()`
- 参照: `document.getElementById("syncChooseOptions").getButton("extra2").hidden`, `options.disconnectFun`, `window.arguments`

## _adjustForPrefs()
- 位置: L58-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(enabledPref, false))` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!Services.prefs.getBoolPref(availablePref))` → `document.querySelector()`
- 参照: `elt.hidden`
- XPCOM: `Services.prefs`

## _setupEventListeners()
- 位置: L78-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `document.addEventListener()`, `lazy.fxAccounts.telemetry.recordSaveSyncSettings()`, `lazy.fxAccounts.telemetry.recordSaveSyncSettings(settings).catch()`, `this._getSyncEngineEnablementChanges()`

## _getSyncEngineEnablementChanges()
- 位置: L87-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `document.getElementById()`, `engine.slice()`, `engine[0].toUpperCase()`
- 条件付き依存: `if (checkboxValue === true)` → `settings.enabledEngines.push()`
- 条件付き依存: `if (checkboxValue === false)` → `settings.disabledEngines.push()`
- 参照: `document.getElementById(checkboxId).checked`
- XPCOM: `Services.prefs`
