# nsIDebug2 (xpcom/base/nsIDebug2.idl)

source: xpcom/base/nsIDebug2.idl
source-hash: a730cbd77a3a01dfad1314336ac7a19fda5b9c14

- 継承: nsISupports
- 役割: @note C/C++ consumers who are planning to use the nsIDebug2 interface with
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserGlue.sys.mjs`](../../browser/components/BrowserGlue.sys.mjs.md)

## メソッド / 属性
- `readonly attribute boolean isDebugBuild`: Whether XPCOM was compiled with DEBUG defined.  This often
- `readonly attribute long assertionCount`: The number of assertions since process start.
- `readonly attribute boolean isDebuggerAttached`: Whether a debugger is currently attached.
- `void assertion(string aStr, string aExpr, string aFile, long aLine)`: Show an assertion and trigger nsIDebug2.break().
- `void warning(string aStr, string aFile, long aLine)`: Show a warning.
- `void break(string aFile, long aLine)`: Request to break into a debugger.
- `void abort(string aFile, long aLine)`: Request the process to trigger a fatal abort.
- `void rustPanic(string aMessage)`: Request the process to trigger a fatal panic!() from Rust code.
- `void rustLog(string aTarget, string aMessage)`: Request the process to log a message for a target and level from Rust code.
- `void crashWithOOM()`: Cause an Out of Memory Crash.
