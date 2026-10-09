# browser/components/webrtc/content/webrtc-preview/webrtc-preview.mjs

source: browser/components/webrtc/content/webrtc-preview/webrtc-preview.mjs
source-hash: d51f4c545ecd3659b3ffff9f2047288dbfa3c2cf
lines: 230

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `customElements.define()`, `window.MozXULElement?.insertFTLIfNeeded()`

## WebRTCPreview.constructor()
- 位置: L48-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._loading`, `this._previewActive`, `this.showPreviewControlButtons`

## WebRTCPreview.disconnectedCallback()
- 位置: L58-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.stopPreview()`

## WebRTCPreview.startPreview()
- 位置: async L75-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `navigator.mediaDevices.getUserMedia()`, `this.#dispatchTestEvent()`, `this.stopPreview()`
- 条件付き依存: `if (lazy.testGumDelayMs > 0)` → `setTimeout()`
- 条件付き依存: `if (signal.aborted)` → `this.#dispatchTestEvent()`
- 条件付き依存: `if ( error.name == "OverconstrainedError" && error.constraint == "deviceId" )` → `this.stopPreview()`
- 条件付き依存: `if ( error.name == "OverconstrainedError" && error.constraint == "deviceId" )` → `this.#dispatchTestEvent()`
- 条件付き依存: `if (signal.aborted)` → `stream.getTracks().forEach()`
- 条件付き依存: `if (signal.aborted)` → `stream.getTracks()`
- 条件付き依存: `if (signal.aborted)` → `t.stop()`
- 参照: `error.constraint`, `error.message`, `error.name`, `lazy.testGumDelayMs`, `signal.aborted`, `this.#abortController`, `this.#stream`, `this._loading`, `this._previewActive`, `this.deviceId`, `this.isConnected`, `this.mediaSource`, `this.showPreviewControlButtons`, `this.videoEl`, `this.videoEl.srcObject`

## WebRTCPreview.#dispatchTestEvent()
- 位置: L161-167
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.testGumDelayMs > 0)` → `this.dispatchEvent()`
- 参照: `lazy.testGumDelayMs`

## WebRTCPreview.stopPreview()
- 位置: L172-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `t.stop()`, `this.#abortController?.abort()`, `this.#stream?.getTracks()`, `this.#stream?.getTracks().forEach()`
- 参照: `this.#abortController`, `this.#stream`, `this._loading`, `this._previewActive`, `this.videoEl`, `this.videoEl.srcObject`

## WebRTCPreview.render()
- 位置: L189-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `this.startPreview()`, `this.stopPreview()`
- 参照: `this._loading`, `this._previewActive`, `this.deviceId`, `this.showPreviewControlButtons`
