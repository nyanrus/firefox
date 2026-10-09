# browser/extensions/webcompat/experiment-apis/aboutConfigPrefs.js

source: browser/extensions/webcompat/experiment-apis/aboutConfigPrefs.js
source-hash: bc3c1167a3f82fa0be15fb3481108ed2a0a81d52
lines: 84

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## AboutConfigPrefsChildAPI.getAPI()
- 位置: L23-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.extension.id.split()`
- 参照: `ExtensionCommon.EventManager`

## getSafePref()
- 位置: L28-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AboutConfigPrefsChildAPI.ALLOWED_GLOBAL_PREFS.includes()`

## register()
- 位置: L40-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `getSafePref()`
- XPCOM: `Services.prefs`

## callback()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (changedPref == prefName)` → `fire.async(name).catch()`
- 条件付き依存: `if (changedPref == prefName)` → `fire.async()`

## AboutConfigPrefsChildAPI.getCheckableGlobalPrefs()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AboutConfigPrefsChildAPI.ALLOWED_GLOBAL_PREFS`

## AboutConfigPrefsChildAPI.getPref()
- 位置: L57-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prefs.getPrefType()`, `Services.prefs.getStringPref()`, `getSafePref()`
- 参照: `Ci.nsIPrefBranch.PREF_BOOL`, `Ci.nsIPrefBranch.PREF_INT`, `Ci.nsIPrefBranch.PREF_STRING`
- XPCOM: [`nsIPrefBranch`](../../../../netwerk/base/nsINetUtil.idl.md) / `Services.prefs`
