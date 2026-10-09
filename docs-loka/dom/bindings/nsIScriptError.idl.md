# nsIScriptErrorNote (dom/bindings/nsIScriptError.idl)

source: dom/bindings/nsIScriptError.idl
source-hash: 2e1736545c4ee3142d0deb27a470311c6678edb3

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString errorMessage`: (未記入)
- `readonly attribute ACString sourceName`: (未記入)
- `readonly attribute uint32_t sourceId`: Unique identifier within the process for the script source this note is
- `readonly attribute uint32_t lineNumber`: (未記入)
- `readonly attribute uint32_t columnNumber`: (未記入)
- `AUTF8String toString()`: (未記入)

# nsIScriptError (dom/bindings/nsIScriptError.idl)

source: dom/bindings/nsIScriptError.idl
source-hash: 2e1736545c4ee3142d0deb27a470311c6678edb3

- 継承: nsIConsoleMessage
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-addons.js`](../../browser/base/content/browser-addons.js.md), [`browser/base/content/browser-fullScreenAndPointerLock.js`](../../browser/base/content/browser-fullScreenAndPointerLock.js.md), [`browser/modules/PermissionUI.sys.mjs`](../../browser/modules/PermissionUI.sys.mjs.md)

## メソッド / 属性
- `const unsigned long errorFlag`: pseudo-flag for default case
- `const unsigned long warningFlag`: message is warning
- `const unsigned long infoFlag`: just a log message
- `readonly attribute AString errorMessage`: The error message without any context/line number information.
- `readonly attribute ACString sourceName`: (未記入)
- `readonly attribute uint32_t sourceId`: Unique identifier within the process for the script source this error is
- `readonly attribute uint32_t lineNumber`: (未記入)
- `readonly attribute uint32_t columnNumber`: (未記入)
- `readonly attribute uint32_t flags`: (未記入)
- `readonly attribute string category`: Categories I know about -
- `readonly attribute unsigned long long outerWindowID`: (未記入)
- `readonly attribute unsigned long long innerWindowID`: (未記入)
- `readonly attribute boolean isFromPrivateWindow`: (未記入)
- `readonly attribute boolean isFromChromeContext`: (未記入)
- `readonly attribute boolean isPromiseRejection`: (未記入)
- `void initIsPromiseRejection(boolean isPromiseRejection)`: (未記入)
- `attribute jsval exception`: (未記入)
- `readonly attribute boolean hasException`: (未記入)
- `attribute jsval stack`: (未記入)
- `readonly attribute jsval stackGlobal`: If |stack| is an object, then stackGlobal must be a global object that's
- `attribute AString errorMessageName`: The name of a template string associated with the error message.  See
- `readonly attribute nsIArray notes`: (未記入)
- `attribute AString cssSelectors`: If the ScriptError is a CSS parser error, this value will contain the
- `void init(AString message, ACString sourceName, uint32_t lineNumber, uint32_t columnNumber, uint32_t flags, ACString category, boolean fromPrivateWindow, boolean fromChromeContext)`: (未記入)
- `void initWithWindowID(AString message, ACString sourceName, uint32_t lineNumber, uint32_t columnNumber, uint32_t flags, ACString category, unsigned long long innerWindowID, boolean fromChromeContext)`: (未記入)
- `void initWithSanitizedSource(AString message, ACString sourceName, uint32_t lineNumber, uint32_t columnNumber, uint32_t flags, ACString category, unsigned long long innerWindowID, boolean fromChromeContext)`: (未記入)
- `void initWithSourceURI(AString message, nsIURI sourceURI, uint32_t lineNumber, uint32_t columnNumber, uint32_t flags, ACString category, unsigned long long innerWindowID, boolean fromChromeContext)`: (未記入)
- `void initSourceId(uint32_t sourceId)`: (未記入)
