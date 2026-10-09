# browser/components/tabnotes/CanonicalURLParent.sys.mjs

source: browser/components/tabnotes/CanonicalURLParent.sys.mjs
source-hash: f890d787581a331b03c1d7e6a1c2ca0f004a46cc
lines: 71

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `console.createInstance()`

## CanonicalURLParent.receiveMessage()
- 位置: L26-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.dispatchEvent()`, `browser.documentGlobal.gBrowser?.getTabForBrowser()`, `lazy.logConsole.info()`
- 条件付き依存: `if (!browser)` → `lazy.logConsole.debug()`
- 条件付き依存: `if (!browser.documentGlobal.gBrowser?.getTabForBrowser(browser))` → `lazy.logConsole.debug()`
- 参照: `browser.documentGlobal.CustomEvent`, `msg.data`, `msg.name`, `this.browsingContext?.embedderElement`
