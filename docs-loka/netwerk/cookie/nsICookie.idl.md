# nsICookie (netwerk/cookie/nsICookie.idl)

source: netwerk/cookie/nsICookie.idl
source-hash: c1825ba1159e5743bbd1b7aaf4de907a965eb148

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/sessionstore/SessionCookies.sys.mjs`](../../browser/components/sessionstore/SessionCookies.sys.mjs.md)

## メソッド / 属性
- `const uint32_t SAMESITE_NONE`: (未記入)
- `const uint32_t SAMESITE_LAX`: (未記入)
- `const uint32_t SAMESITE_STRICT`: (未記入)
- `const uint32_t SAMESITE_UNSET`: (未記入)
- `readonly attribute ACString name`: the name of the cookie
- `readonly attribute AUTF8String value`: the cookie value
- `readonly attribute boolean isDomain`: true if the cookie is a domain cookie, false otherwise
- `readonly attribute AUTF8String host`: the host (possibly fully qualified) of the cookie
- `readonly attribute AUTF8String rawHost`: the host (possibly fully qualified) of the cookie,
- `readonly attribute AUTF8String path`: the path pertaining to the cookie
- `readonly attribute boolean isSecure`: true if the cookie was transmitted over ssl, false otherwise
- `readonly attribute uint64_t expires`: @DEPRECATED use nsICookie.expiry and nsICookie.isSession instead.
- `readonly attribute int64_t expiry`: the actual expiry time of the cookie, in milliseconds
- `readonly attribute jsval originAttributes`: The origin attributes for this cookie
- `const_OriginAttributes OriginAttributesNative()`: Native getter for origin attributes
- `const_Cookie AsCookie()`: (未記入)
- `readonly attribute boolean isSession`: true if the cookie is a session cookie.
- `readonly attribute boolean isHttpOnly`: true if the cookie is an http only cookie
- `readonly attribute int64_t creationTime`: the creation time of the cookie, in microseconds
- `readonly attribute int64_t updateTime`: the update time of the cookie, in microseconds
- `readonly attribute int64_t lastAccessed`: the last time the cookie was accessed (i.e. created,
- `readonly attribute int32_t sameSite`: the SameSite attribute; this controls the cookie behavior for cross-site
- `readonly attribute nsICookie_schemeType schemeMap`: Bitmap of schemes.
- `readonly attribute boolean isPartitioned`: true if the cookie's OriginAttributes PartitionKey is NOT empty
