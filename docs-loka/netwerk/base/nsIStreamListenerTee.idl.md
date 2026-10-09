# nsIStreamListenerTee (netwerk/base/nsIStreamListenerTee.idl)

source: netwerk/base/nsIStreamListenerTee.idl
source-hash: 2aa9c34877ffc0e4b3fa6cfa54742bc081caf44d

- 継承: nsIThreadRetargetableStreamListener
- 役割: As data "flows" into a stream listener tee, it is copied to the output stream
- 実装: (未記入)
- 使っているJS: [`browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs`](../../browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs.md)

## メソッド / 属性
- `void init(nsIStreamListener listener, nsIOutputStream sink, nsIRequestObserver requestObserver)`: Initalize the tee.
- `void initAsync(nsIStreamListener listener, nsIEventTarget eventTarget, nsIOutputStream sink, nsIRequestObserver requestObserver)`: Initalize the tee like above, but with the extra parameter to make it
