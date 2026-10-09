# browser/extensions/pictureinpicture/experiment-apis/aboutConfigPipPrefs.js

source: browser/extensions/pictureinpicture/experiment-apis/aboutConfigPipPrefs.js
source-hash: 4660affd8f20286c806e1cc67a92634b52bc93c2
lines: 69

## <module>
- 役割: (未記入)

## getAPI()
- 位置: L19-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.extension.id.split()`
- 参照: `ExtensionCommon.EventManager`

## register()
- 位置: L29-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## callback()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.async()`, `fire.async(name).catch()`

## getPref()
- 位置: async L46-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## setPref()
- 位置: async L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`
