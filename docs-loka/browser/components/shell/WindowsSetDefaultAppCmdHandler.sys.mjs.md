# browser/components/shell/WindowsSetDefaultAppCmdHandler.sys.mjs

source: browser/components/shell/WindowsSetDefaultAppCmdHandler.sys.mjs
source-hash: 88de305e30d84721307953a070b98e4fac34a1f1
lines: 98

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Components.ID()`, `console.createInstance()`

## CommandLineHandler.handle()
- 位置: L42-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/supports-string;1"].createInstance()`, `aCmdLine.findFlag()`, `aCmdLine.getArgument()`, `aCmdLine.handleFlagWithParam()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.BrowserWindowTracker.openWindow()`, `lazy.WindowsSetDefaultRedirect.consume()`, `lazy.logConsole.debug()`, `lazy.logConsole.error()`, `lazy.logConsole.info()`
- 条件付き依存: `if (win)` → `win.openTrustedLinkIn()`
- 参照: `Ci.nsISupportsString`, `aCmdLine.preventDefault`, `aCmdLine.state`, `args.data`
- XPCOM: [`nsISupportsString`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-string;1`
