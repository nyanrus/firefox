# nsICaptivePortalServiceCallback (netwerk/base/nsICaptivePortalService.idl)

source: netwerk/base/nsICaptivePortalService.idl
source-hash: 0814ecb6651d297952aa7a74b72d2d728036f41d

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void complete(boolean success, nsresult error)`: Invoke callbacks after captive portal detection finished.

# nsICaptivePortalService (netwerk/base/nsICaptivePortalService.idl)

source: netwerk/base/nsICaptivePortalService.idl
source-hash: 0814ecb6651d297952aa7a74b72d2d728036f41d

- 継承: nsISupports
- 役割: Service used for captive portal detection.
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-captivePortal.js`](../../browser/base/content/browser-captivePortal.js.md)

## メソッド / 属性
- `const long UNKNOWN`: (未記入)
- `const long NOT_CAPTIVE`: (未記入)
- `const long UNLOCKED_PORTAL`: (未記入)
- `const long LOCKED_PORTAL`: (未記入)
- `void recheckCaptivePortal()`: Called from XPCOM to trigger a captive portal recheck.
- `readonly attribute long state`: Returns the state of the captive portal.
- `readonly attribute unsigned long long lastChecked`: Returns the time difference between NOW and the last time a request was
