# browser/components/preferences/fxaPairDevice.js

source: browser/components/preferences/fxaPairDevice.js
source-hash: e22ef3aa272366d8c94d493adaf9086c23f06fb9
lines: 143

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `gFxaPairDeviceDialog.init()`, `window.addEventListener()`

## init()
- 位置: L33-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `document .getElementById()`, `document .getElementById("qrError") .addEventListener()`, `this._resetBackgroundQR()`, `this.startPairingFlow()`, `this.uninit()`, `window.addEventListener()`
- XPCOM: `Services.tm`

## uninit()
- 位置: L44-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `browser.loadURI()`, `this._emitter.emit()`, `this.teardownListeners()`
- 参照: `window.docShell.chromeEventHandler`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## startPairingFlow()
- 位置: async L56-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FxAccountsPairingFlow.start()`, `Promise.all()`, `QR.encodeToDataURI()`, `Weave.Utils.ensureMPUnlocked()`, `document .getElementById()`, `document .getElementById("qrWrapper") .setAttribute()`, `document.getElementById()`, `setTimeout()`, `this._resetBackgroundQR()`, `this._styleParentDialog()`, `this.onError()`, `this.setupListeners()`
- 参照: `document.getElementById("qrContainer").style.backgroundImage`, `imgData.src`, `this._emitter`

## _styleParentDialog()
- 位置: L86-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialogParent.querySelector()`
- 参照: `dialogBox.style.borderRadius`, `dialogTitle.style.borderBottom`, `window.parent.document`

## _resetBackgroundQR()
- 位置: L98-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `QR.encodeToDataURI()`, `document.getElementById()`
- 参照: `document.getElementById("qrContainer").style.backgroundImage`, `imgData.src`

## onError()
- 位置: L108-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `document .getElementById()`, `document .getElementById("qrWrapper") .setAttribute()`, `this.teardownListeners()`

## _switchToUrl()
- 位置: L116-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `browser.fixupAndLoadURIString()`
- 参照: `window.docShell.chromeEventHandler`
- XPCOM: `Services.scriptSecurityManager`

## setupListeners()
- 位置: L125-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._emitter.on()`, `this._emitter.once()`
- 参照: `this._onError`, `this._switchToWebContent`

## this._switchToWebContent()
- 位置: L126-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._switchToUrl()`

## this._onError()
- 位置: L127-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onError()`

## teardownListeners()
- 位置: L132-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `this._emitter.off()`
- 参照: `this._onError`, `this._switchToWebContent`
