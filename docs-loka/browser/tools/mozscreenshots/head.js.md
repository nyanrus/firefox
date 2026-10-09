# browser/tools/mozscreenshots/head.js

source: browser/tools/mozscreenshots/head.js
source-hash: ca19e7cd7e11d9057d2136811cebfdd59bedbad8
lines: 71

## <module>
- 役割: (未記入)
- 呼び出し先: `Cc["@mozilla.org/chrome/chrome-registry;1"].getService()`, `add_setup()`

## setup()
- 位置: async L17-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AddonManager.getAddonByID()`, `AddonManager.installTemporaryAddon()`, `ChromeUtils.importESModule()`, `Services.io.newURI()`, `SimpleTest.requestCompleteLog()`, `TestRunner.initTest()`, `chromeRegistry .convertChromeURL()`, `chromeRegistry .convertChromeURL(chromeURL) .QueryInterface()`, `info()`, `isnot()`, `requestLongerTimeout()`
- 参照: `ChromeUtils.importESModule( "resource://mozscreenshots/TestRunner.sys.mjs" ).TestRunner`, `Ci.nsIFileURL`, `chromeRegistry .convertChromeURL(chromeURL) .QueryInterface(Ci.nsIFileURL).file`
- XPCOM: [`nsIFileURL`](../../../netwerk/base/nsIFileURL.idl.md) / `Services.io`

## shouldCapture()
- 位置: L49-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.get()`
- 条件付き依存: `if (Services.env.get("MOZSCREENSHOTS_SETS"))` → `ok()`
- 条件付き依存: `if (!Services.env.get("MOZ_UPLOAD_DIR"))` → `ok()`
- XPCOM: `Services.env`
