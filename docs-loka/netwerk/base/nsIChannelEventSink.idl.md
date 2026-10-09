# nsIChannelEventSink (netwerk/base/nsIChannelEventSink.idl)

source: netwerk/base/nsIChannelEventSink.idl
source-hash: 7898c907779e6807fb82a00cd9943855c1da8393

- 継承: nsISupports
- 役割: Implement this interface to receive control over various channel events.
- 実装: (未記入)
- 使っているJS: [`browser/modules/FaviconLoader.sys.mjs`](../../browser/modules/FaviconLoader.sys.mjs.md)

## メソッド / 属性
- `const unsigned long REDIRECT_TEMPORARY`: This is a temporary redirect. New requests for this resource should
- `const unsigned long REDIRECT_PERMANENT`: This is a permanent redirect. New requests for this resource should use
- `const unsigned long REDIRECT_INTERNAL`: This is an internal redirect, i.e. it was not initiated by the remote
- `const unsigned long REDIRECT_STS_UPGRADE`: This is a special-cased redirect coming from hitting HSTS upgrade
- `const unsigned long REDIRECT_AUTH_RETRY`: This is a internal redirect used to handle http authentication retries.
- `const unsigned long REDIRECT_TRANSPARENT`: This is a special-case internal redirect triggered by
- `void asyncOnChannelRedirect(nsIChannel oldChannel, nsIChannel newChannel, unsigned long flags, nsIAsyncVerifyRedirectCallback callback)`: Called when a redirect occurs. This may happen due to an HTTP 3xx status
