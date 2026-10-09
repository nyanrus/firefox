# nsIRefreshURI (docshell/base/nsIRefreshURI.idl)

source: docshell/base/nsIRefreshURI.idl
source-hash: 17bd7c678b34757067e06a3f480881b6ac973cdb

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/RefreshBlockerChild.sys.mjs`](../../browser/actors/RefreshBlockerChild.sys.mjs.md)

## メソッド / 属性
- `void refreshURI(nsIURI aURI, nsIPrincipal aPrincipal, unsigned long aMillis)`: Load a uri after waiting for aMillis milliseconds (as a result of a
- `void forceRefreshURI(nsIURI aURI, nsIPrincipal aPrincipal, unsigned long aMillis)`: Loads a URI immediately as if it were a meta refresh.
- `void cancelRefreshURITimers()`: Cancels all timer loads.
- `readonly attribute boolean refreshPending`: True when there are pending refreshes, false otherwise.
