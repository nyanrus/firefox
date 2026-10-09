# browser/actors/EncryptedMediaChild.sys.mjs

source: browser/actors/EncryptedMediaChild.sys.mjs
source-hash: b8bff619e963c2b02404986a25f32f1e73248eb5
lines: 125

## <module>
- 役割: EME（暗号化メディア）のコンテンツ側アクター。画面や窓の共有状況から、キャプチャ可能性を判定して EME の要求を親へ渡す。

## GlobalCaptureListener.constructor()
- 位置: L12-19
- 役割: 共有データの変化を購読し、判定の初期値を安全側（キャプチャ中）にしておく。
- 触るとき: プロセス内の画面キャプチャ判定の初期状態を変えるときに見る。
- 呼び出し先: `Services.cpmm.sharedData.addEventListener()`
- 参照: `this._isAnyWindowCaptured`, `this._isScreenCaptured`
- XPCOM: `Services.cpmm`

## GlobalCaptureListener.requestUpdateAndNotify()
- 位置: L25-27
- 役割: キャプチャ状態を再計算し、変化の有無にかかわらず observer へ通知する。
- 触るとき: EME が「キャプチャ可能か」を問い合わせたときの応答を調べるときに見る。
- 呼び出し先: `this._updateCaptureState()`

## GlobalCaptureListener.handleEvent()
- 位置: L36-43
- 役割: 画面共有フラグや共有ウィンドウ ID が変わったときだけ、キャプチャ状態を更新する。
- 触るとき: 共有の開始・終了が EME 側へ反映されないときに見る。
- 呼び出し先: `event.changedKeys.includes()`
- 条件付き依存: `if ( event.changedKeys.includes("webrtcUI:isSharingScreen") || event.changedKeys.includes("webrtcUI:sharedTopInnerWindowIds") )` → `this._updateCaptureState()`

## GlobalCaptureListener._updateCaptureState()
- 位置: L54-78
- 役割: 画面共有と共有ウィンドウの有無からキャプチャ状態を求め、変化したか強制時に通知する。
- 触るとき: キャプチャ判定の条件（画面か窓か）を変えるときに見る。
- 呼び出し先: `Boolean()`, `Services.cpmm.sharedData.get()`
- 条件付き依存: `if (forceNotify || captureStateChanged)` → `this._notifyCaptureState()`
- 参照: `capturedTopInnerWindowIds.size`, `this._isAnyWindowCaptured`, `this._isScreenCaptured`
- XPCOM: `Services.cpmm`

## GlobalCaptureListener._notifyCaptureState()
- 位置: L86-97
- 役割: キャプチャ可能かに応じて capture-possible か capture-not-possible を mediakeys-response として通知する。
- 触るとき: EME 側が受け取る応答の値や通知の形式を変えるときに見る。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `this._isAnyWindowCaptured`, `this._isScreenCaptured`
- XPCOM: `Services.obs`

## EncryptedMediaChild.observe()
- 位置: L107-123
- 役割: mediakeys-request の JSON を解析し、キャプチャ可能性の問い合わせはプロセス内で応答し、それ以外は親へ送る。
- 触るとき: EME の要求の振り分け（プロセス内か親か）を変えるときに見る。
- 呼び出し先: `JSON.parse()`, `console.error()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (status == "is-capture-possible")` → `gGlobalCaptureListener.requestUpdateAndNotify()`
