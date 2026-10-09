# browser/base/content/browser-graphics-utils.js

source: browser/base/content/browser-graphics-utils.js
source-hash: 3d1289604a757dd1d20d916de27a5591c3c6bc87
lines: 87

## <module>
- 役割: WebRender のデバッグ用キャプチャ(ショートカット登録、記録・単発/連続キャプチャ)を提供する gGfxUtils 定義

## init()
- 位置: L13-17
- 役割: gfx.webrender.debug.enable-capture が有効なときだけキャプチャ用ショートカットを登録する。
- 触るとき: キャプチャ機能を有効化する条件や起動時の初期化順を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("gfx.webrender.debug.enable-capture"))` → `this.registerCaptureShortcuts()`
- XPCOM: `Services.prefs`

## registerCaptureShortcuts()
- 位置: L26-50
- 役割: WebRender キャプチャ用の key 要素を含む keyset を作り、ウィンドウに追加してショートカットを有効にする。
- 触るとき: キャプチャのキーバインドを変える、または macOS と他OSの差分を直すとき。
- 呼び出し先: `document.createXULElement()`, `document.documentElement.appendChild()`, `keyElement.setAttribute()`, `keyset.appendChild()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `keyElement.setAttribute()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `keyElement.setAttribute()`
- 参照: `AppConstants.platform`, `keyElement.id`, `keyset.id`

## toggleWindowRecording()
- 位置: L55-58
- 役割: 現在のウィンドウの composition 記録を開始・停止し、記録状態のフラグを反転させる。
- 触るとき: コンポジション記録の挙動や状態管理を調べるとき。
- 呼び出し先: `window.windowUtils.setCompositionRecording()`
- 参照: `this._isRecording`

## webrenderCapture()
- 位置: L62-64
- 役割: 現在の状態を WebRender の単発キャプチャとしてローカルフォルダへ書き出す。
- 触るとき: 単発キャプチャの呼び出し経路を調べるとき。
- 呼び出し先: `window.windowUtils.wrCapture()`

## toggleWebrenderCaptureSequence()
- 位置: L75-85
- 役割: フレーム連続キャプチャの開始と停止を切り替え、開始時は保存先とフラグを渡す。
- 触るとき: 連続キャプチャの保存先やフラグを変えるとき。
- 条件付き依存: `if (this._isCapturingFrames)` → `window.windowUtils.wrStartCaptureSequence()`
- 条件付き依存: `if (!(this._isCapturingFrames))` → `window.windowUtils.wrStopCaptureSequence()`
- 参照: `this._isCapturingFrames`, `this.captureSequenceFlags`, `this.captureSequencePath`
