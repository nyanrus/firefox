# nsIStackFrame (xpcom/base/nsIException.idl)

source: xpcom/base/nsIException.idl
source-hash: 1cb855bab2a135cfa28805e57fce9d4a187f32f8

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AUTF8String filename`: (未記入)
- `readonly attribute AString name`: (未記入)
- `readonly attribute int32_t sourceId`: (未記入)
- `readonly attribute int32_t lineNumber`: (未記入)
- `readonly attribute int32_t columnNumber`: (未記入)
- `readonly attribute AString asyncCause`: (未記入)
- `readonly attribute nsIStackFrame asyncCaller`: (未記入)
- `readonly attribute nsIStackFrame caller`: (未記入)
- `readonly attribute AString formattedStack`: (未記入)
- `readonly attribute jsval nativeSavedFrame`: (未記入)
- `AUTF8String toString()`: (未記入)
- `void getFilename(JSContext aCx, AUTF8String aFilename)`: (未記入)
- `void getName(JSContext aCx, AString aName)`: (未記入)
- `int32_t getSourceId(JSContext aCx)`: (未記入)
- `int32_t getLineNumber(JSContext aCx)`: (未記入)
- `int32_t getColumnNumber(JSContext aCx)`: (未記入)
- `void getAsyncCause(JSContext aCx, AString aAsyncCause)`: (未記入)
- `StackFrameRef getAsyncCaller(JSContext aCx)`: (未記入)
- `StackFrameRef getCaller(JSContext aCx)`: (未記入)
- `void getFormattedStack(JSContext aCx, AString aFormattedStack)`: (未記入)
- `void toStringInfallible(JSContext aCx, AUTF8String aString)`: (未記入)

# nsIException (xpcom/base/nsIException.idl)

source: xpcom/base/nsIException.idl
source-hash: 1cb855bab2a135cfa28805e57fce9d4a187f32f8

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/attribution/AttributionCode.sys.mjs`](../../browser/components/attribution/AttributionCode.sys.mjs.md)

## メソッド / 属性
