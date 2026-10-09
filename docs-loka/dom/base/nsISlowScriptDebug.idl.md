# nsISlowScriptDebugCallback (dom/base/nsISlowScriptDebug.idl)

source: dom/base/nsISlowScriptDebug.idl
source-hash: 39cbc8206e300a2b8ecc392c97635d6f12871d46

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void handleSlowScriptDebug(nsIDOMWindow aWindow)`: (未記入)

# nsISlowScriptDebuggerStartupCallback (dom/base/nsISlowScriptDebug.idl)

source: dom/base/nsISlowScriptDebug.idl
source-hash: 39cbc8206e300a2b8ecc392c97635d6f12871d46

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void finishDebuggerStartup()`: (未記入)

# nsISlowScriptDebugRemoteCallback (dom/base/nsISlowScriptDebug.idl)

source: dom/base/nsISlowScriptDebug.idl
source-hash: 39cbc8206e300a2b8ecc392c97635d6f12871d46

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void handleSlowScriptDebug(EventTarget aBrowser, nsISlowScriptDebuggerStartupCallback aCallback)`: (未記入)

# nsISlowScriptDebug (dom/base/nsISlowScriptDebug.idl)

source: dom/base/nsISlowScriptDebug.idl
source-hash: 39cbc8206e300a2b8ecc392c97635d6f12871d46

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/modules/ProcessHangMonitor.sys.mjs`](../../browser/modules/ProcessHangMonitor.sys.mjs.md)

## メソッド / 属性
- `attribute nsISlowScriptDebugCallback activationHandler`: (未記入)
- `attribute nsISlowScriptDebugRemoteCallback remoteActivationHandler`: (未記入)
