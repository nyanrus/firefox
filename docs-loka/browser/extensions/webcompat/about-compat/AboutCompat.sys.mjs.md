# browser/extensions/webcompat/about-compat/AboutCompat.sys.mjs

source: browser/extensions/webcompat/about-compat/AboutCompat.sys.mjs
source-hash: bedcdd668d51d2f3912cb517efe2ac6545c6a391
lines: 36

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## AboutCompat()
- 位置: L8-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WebExtensionPolicy.getByID()`, `WebExtensionPolicy.getByID(addonID).getURL()`
- 参照: `this.chromeURL`

## getURIFlags()
- 位置: L15-20
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `Ci.nsIAboutModule.URI_MUST_LOAD_IN_EXTENSION_PROCESS`
- XPCOM: [`nsIAboutModule`](../../../../netwerk/protocol/about/nsIAboutModule.idl.md)

## newChannel()
- 位置: L22-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newChannelFromURIWithLoadInfo()`, `Services.io.newURI()`
- 参照: `Services.scriptSecurityManager.createCodebasePrincipal`, `Services.scriptSecurityManager.createContentPrincipal`, `aLoadInfo.originAttributes`, `channel.originalURI`, `channel.owner`, `this.chromeURL`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`
