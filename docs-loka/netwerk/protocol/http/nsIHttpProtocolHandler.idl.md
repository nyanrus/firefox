# nsIHttpProtocolHandler (netwerk/protocol/http/nsIHttpProtocolHandler.idl)

source: netwerk/protocol/http/nsIHttpProtocolHandler.idl
source-hash: e27ce449bd8bdb7d2d53054dd1a6f5b51b868e1d

- 継承: nsIProxiedProtocolHandler
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/extensions/newtab/lib/DiscoveryStreamFeed.sys.mjs`](../../../browser/extensions/newtab/lib/DiscoveryStreamFeed.sys.mjs.md), [`browser/extensions/newtab/lib/TopSitesFeed.sys.mjs`](../../../browser/extensions/newtab/lib/TopSitesFeed.sys.mjs.md)

## メソッド / 属性
- `readonly attribute ACString userAgent`: Get the HTTP advertised user agent string.
- `readonly attribute ACString documentAcceptHeader`: Get the default Accept header value for document requests.
- `readonly attribute ACString rfpUserAgent`: Get the HTTP advertised user agent string.
- `readonly attribute ACString appName`: Get the application name.
- `readonly attribute ACString appVersion`: Get the application version string.
- `readonly attribute ACString platform`: Get the current platform.
- `readonly attribute ACString oscpu`: Get the current oscpu.
- `readonly attribute ACString misc`: Get the application comment misc portion.
- `readonly attribute Array<ACString> altSvcCacheKeys`: Get the Alt-Svc cache keys (used for testing).
- `readonly attribute Array<ACString> authCacheKeys`: Get the auth cache keys (used for testing).
- `Promise EnsureHSTSDataReady()`: This function is used to ensure HSTS data storage is ready to read after
- `void EnsureHSTSDataReadyNative(HSTSDataCallbackWrapperAlreadyAddRefed aCallback)`: A C++ friendly version of EnsureHSTSDataReady
- `void clearCORSPreflightCache()`: (未記入)
