# browser/components/qrcode/QRCodeGenerator.sys.mjs

source: browser/components/qrcode/QRCodeGenerator.sys.mjs
source-hash: a4c8d7633c663848b4654b040d25b3a3a0153da7
lines: 60

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## generateQRCode()
- 位置: async L44-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.logConsole.debug()`, `lazy.logConsole.warn()`, `worker.generateFullQRCode()`, `worker.terminate()`
- 参照: `lazy.QRCodeWorker`, `lazy.embedLogo`
