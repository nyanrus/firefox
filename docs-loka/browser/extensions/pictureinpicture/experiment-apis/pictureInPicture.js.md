# browser/extensions/pictureinpicture/experiment-apis/pictureInPicture.js

source: browser/extensions/pictureinpicture/experiment-apis/pictureInPicture.js
source-hash: 274c3ad75657c55e128a4eec24c0c1103acf8c72
lines: 88

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getAPI()
- 位置: L29-46
- 役割: (未記入)
- 触るとき: (未記入)

## setOverrides()
- 位置: L32-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.ppmm.sharedData.set()`
- 参照: `AppConstants.platform`
- XPCOM: `Services.ppmm`

## getAPI()
- 位置: L63-86
- 役割: (未記入)
- 触るとき: (未記入)

## getKeyboardControls()
- 位置: L66-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`
- 条件付き依存: `if (AppConstants.platform == "android")` → `Cu.cloneInto()`
- 参照: `AppConstants.platform`, `context.cloneScope`

## getPolicies()
- 位置: L75-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`
- 条件付き依存: `if (AppConstants.platform == "android")` → `Cu.cloneInto()`
- 参照: `AppConstants.platform`, `context.cloneScope`
