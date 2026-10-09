# nsICookieManager (netwerk/cookie/nsICookieManager.idl)

source: netwerk/cookie/nsICookieManager.idl
source-hash: 064d86ff1c351479205df8aa5358b173daf7ece9

- 継承: nsISupports
- 役割: An optional interface for accessing or removing the cookies
- 実装: (未記入)

## メソッド / 属性
- `void removeAll()`: Called to remove all cookies from the cookie list
- `readonly attribute Array<nsICookie> cookies`: Returns an array of cookies in the cookie list.
- `readonly attribute Array<nsICookie> sessionCookies`: Returns an array of session cookies in the cookie list.
- `uint32_t getCookieBehavior(boolean aIsPrivate)`: Returns current effective value of the cookieBehavior. It will return the
- `void remove(AUTF8String aHost, ACString aName, AUTF8String aPath, jsval aOriginAttributes)`: Called to remove an individual cookie from the cookie list, specified
- `nsresult removeNative(AUTF8String aHost, ACString aName, AUTF8String aPath, OriginAttributesPtr aOriginAttributes, boolean aFromHttp, nsIDPtr aOperationID)`: (未記入)
- `nsICookieValidation add(AUTF8String aHost, AUTF8String aPath, ACString aName, AUTF8String aValue, boolean aIsSecure, boolean aIsHttpOnly, boolean aIsSession, int64_t aExpiry, jsval aOriginAttributes, int32_t aSameSite, nsICookie_schemeType aSchemeMap, boolean aIsPartitioned)`: Add a cookie. nsICookieService is the normal way to do this. This
- `nsresult addNative(nsIURI aCookieURI, AUTF8String aHost, AUTF8String aPath, ACString aName, AUTF8String aValue, boolean aIsSecure, boolean aIsHttpOnly, boolean aIsSession, int64_t aExpiry, OriginAttributesPtr aOriginAttributes, int32_t aSameSite, nsICookie_schemeType aSchemeMap, boolean aIsPartitioned, boolean aFromHttp, nsIDPtr aOperationID, nsICookieValidation aValidation)`: This method is the non-xpcom version of add(). In case of an invalid
- `boolean cookieExists(AUTF8String aHost, AUTF8String aPath, ACString aName, jsval aOriginAttributes)`: Find whether a given cookie already exists.
- `nsresult cookieExistsNative(AUTF8String aHost, AUTF8String aPath, ACString aName, OriginAttributesPtr aOriginAttributes, boolean aExists)`: (未記入)
- `nsresult getCookieNative(AUTF8String aHost, AUTF8String aPath, ACString aName, OriginAttributesPtr aOriginAttributes, nsICookie aCookie)`: Get a specific cookie by host, path, name and OriginAttributes.
- `boolean hasCookiesForSite(AUTF8String aHost, AString aPattern)`: Greedily check whether any cookie exists for the site (base domain of
- `Array<nsICookie> getCookiesFromHost(AUTF8String aHost, jsval aOriginAttributes, boolean aSorted)`: Returns an array of cookies that exist within the base domain of
- `nsresult getCookiesFromHostNative(AUTF8String aHost, OriginAttributesPtr aOriginAttributes, boolean aSorted, Array<nsICookie> aCookies)`: (未記入)
- `Array<nsICookie> getCookiesWithOriginAttributes(AString aPattern, AUTF8String aHost, boolean aSorted)`: Returns an array of all cookies whose origin attributes matches aPattern
- `void removeCookiesWithOriginAttributes(AString aPattern, AUTF8String aHost)`: Remove all the cookies whose origin attributes matches aPattern
- `void removeCookiesFromExactHost(AUTF8String aHost, AString aPattern)`: Remove all the cookies whose origin attributes matches aPattern and the
- `Promise removeAllSince(int64_t aSinceWhen)`: Removes all cookies that were created on or after aSinceWhen, and returns
- `Array<nsICookie> getCookiesSince(int64_t aSinceWhen)`: Retrieves all the cookies that were created on or after aSinceWhen, order
- `void addThirdPartyCookieBlockingExceptions(Array<nsIThirdPartyCookieExceptionEntry> aExcpetions)`: Adds a list of exceptions to the third party cookie blocking exception
- `void removeThirdPartyCookieBlockingExceptions(Array<nsIThirdPartyCookieExceptionEntry> aExceptions)`: Removes a list of exceptions from the third party cookie blocking
- `Array<ACString> testGet3PCBExceptions()`: (未記入)
- `void testCloseCookieDB()`: (未記入)
- `void testOpenCookieDB()`: (未記入)
- `int64_t maybeCapExpiry(int64_t aExpiryInMSec)`: Helper to cap an expiry time using the network.cookie.maxageCap pref.
