# browser/base/content/safeMode.js

source: browser/base/content/safeMode.js
source-hash: 48d4ddb299c96dad7314d1a4fd13357b0854b06a
lines: 75

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `document.addEventListener()`, `document.getElementById()`, `window.addEventListener()`

## showResetDialog()
- 位置: L13-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ResetProfile.doReset()`, `window.openDialog()`
- 参照: `retVals.reset`

## onDefaultButton()
- 位置: L31-40
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (defaultToReset)` → `event.preventDefault()`
- 条件付き依存: `if (defaultToReset)` → `ResetProfile.doReset()`

## onCancel()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `appStartup.quit()`
- 参照: `appStartup.eForceQuit`

## onExtra1()
- 位置: L46-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `showResetDialog()`
- 条件付き依存: `if (defaultToReset)` → `window.close()`
