# nsIASWebAuthSessionRequest (toolkit/xre/nsIASWebAuthSessionRequest.idl)

source: toolkit/xre/nsIASWebAuthSessionRequest.idl
source-hash: fc80965e10c162b1327a39dd860fe7cee9253e1f

- 継承: nsISupports
- 役割: Represents a single web authentication request from macOS.
- 実装: (未記入)
- 使っているJS: [`browser/modules/ASWebAuthSessionService.sys.mjs`](../../browser/modules/ASWebAuthSessionService.sys.mjs.md)

## メソッド / 属性
- `readonly attribute AString uuid`: macOS-assigned identifier for the request.
- `readonly attribute AString url`: The authorization URL to load.
- `readonly attribute AString callbackScheme`: The custom callback scheme the flow completes with, or the empty string
- `readonly attribute boolean hasCallback`: True when the request uses an HTTPS callback. Use matchesCallbackURL()
- `readonly attribute boolean useEphemeralSession`: True when the session must use a private browsing session.
- `readonly attribute Array<AString> additionalHeaderNames`: Names of the app-supplied headers to send with the initial request.
- `AString getAdditionalHeader(AString name)`: Value of an app-supplied header, or the empty string if not present.
- `boolean matchesCallbackURL(AString url)`: Tests a candidate navigation URL against the request's opaque HTTPS
- `void complete(AString callbackURL)`: Completes the request with the resolved callback URL.
- `void cancel()`: Cancels the request.
