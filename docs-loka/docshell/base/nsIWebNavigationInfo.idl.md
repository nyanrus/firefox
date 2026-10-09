# nsIWebNavigationInfo (docshell/base/nsIWebNavigationInfo.idl)

source: docshell/base/nsIWebNavigationInfo.idl
source-hash: b6cf45bc0053af4e6763b03e7300027ed7a5dbc5

- 継承: nsISupports
- 役割: The nsIWebNavigationInfo interface exposes a way to get information
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserContentHandler.sys.mjs`](../../browser/components/BrowserContentHandler.sys.mjs.md)

## メソッド / 属性
- `const unsigned long UNSUPPORTED`: Returned by isTypeSupported to indicate lack of support for a type.
- `const unsigned long IMAGE`: Returned by isTypeSupported to indicate that a type is supported as an
- `const unsigned long OTHER`: Returned by isTypeSupported to indicate that a type is supported via some
- `unsigned long isTypeSupported(ACString aType)`: Query whether aType is supported.
