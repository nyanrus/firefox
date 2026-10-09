# browser/components/extensions/ExtensionBrowsingData.sys.mjs

source: browser/components/extensions/ExtensionBrowsingData.sys.mjs
source-hash: 9ca3be643dd1158afb06de65c78375a940afbd7b
lines: 76

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## BrowsingDataDelegate.constructor()
- 位置: L21-21
- 役割: (未記入)
- 触るとき: (未記入)

## BrowsingDataDelegate.handleRemoval()
- 位置: L25-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Sanitizer.items.downloads.clear()`, `lazy.Sanitizer.items.formdata.clear()`, `lazy.Sanitizer.items.history.clear()`, `lazy.makeRange()`

## BrowsingDataDelegate.settings()
- 位置: L41-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Services.prefs.getBoolPref()`, `lazy.Sanitizer.getClearRange()`
- XPCOM: `Services.prefs`
