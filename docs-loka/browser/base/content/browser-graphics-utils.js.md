# browser/base/content/browser-graphics-utils.js

source: browser/base/content/browser-graphics-utils.js
source-hash: 3d1289604a757dd1d20d916de27a5591c3c6bc87
lines: 87

## <module>
- 役割: (未記入)

## init()
- 位置: L13-17
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("gfx.webrender.debug.enable-capture"))` → `this.registerCaptureShortcuts()`
- XPCOM: `Services.prefs`

## registerCaptureShortcuts()
- 位置: L26-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createXULElement()`, `document.documentElement.appendChild()`, `keyElement.setAttribute()`, `keyset.appendChild()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `keyElement.setAttribute()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `keyElement.setAttribute()`
- 参照: `AppConstants.platform`, `keyElement.id`, `keyset.id`

## toggleWindowRecording()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.setCompositionRecording()`
- 参照: `this._isRecording`

## webrenderCapture()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.windowUtils.wrCapture()`

## toggleWebrenderCaptureSequence()
- 位置: L75-85
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._isCapturingFrames)` → `window.windowUtils.wrStartCaptureSequence()`
- 条件付き依存: `if (!(this._isCapturingFrames))` → `window.windowUtils.wrStopCaptureSequence()`
- 参照: `this._isCapturingFrames`, `this.captureSequenceFlags`, `this.captureSequencePath`
