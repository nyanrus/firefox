# browser/actors/EncryptedMediaChild.sys.mjs

source: browser/actors/EncryptedMediaChild.sys.mjs
source-hash: b8bff619e963c2b02404986a25f32f1e73248eb5
lines: 125

## <module>
- 役割: (未記入)

## GlobalCaptureListener.constructor()
- 位置: L12-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.cpmm.sharedData.addEventListener()`
- 参照: `this._isAnyWindowCaptured`, `this._isScreenCaptured`
- XPCOM: `Services.cpmm`

## GlobalCaptureListener.requestUpdateAndNotify()
- 位置: L25-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateCaptureState()`

## GlobalCaptureListener.handleEvent()
- 位置: L36-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.changedKeys.includes()`
- 条件付き依存: `if ( event.changedKeys.includes("webrtcUI:isSharingScreen") || event.changedKeys.includes("webrtcUI:sharedTopInnerWindowIds") )` → `this._updateCaptureState()`

## GlobalCaptureListener._updateCaptureState()
- 位置: L54-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `Services.cpmm.sharedData.get()`
- 条件付き依存: `if (forceNotify || captureStateChanged)` → `this._notifyCaptureState()`
- 参照: `capturedTopInnerWindowIds.size`, `this._isAnyWindowCaptured`, `this._isScreenCaptured`
- XPCOM: `Services.cpmm`

## GlobalCaptureListener._notifyCaptureState()
- 位置: L86-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `this._isAnyWindowCaptured`, `this._isScreenCaptured`
- XPCOM: `Services.obs`

## EncryptedMediaChild.observe()
- 位置: L107-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `console.error()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (status == "is-capture-possible")` → `gGlobalCaptureListener.requestUpdateAndNotify()`
