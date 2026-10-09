# nsINetUtil (netwerk/base/nsINetUtil.idl)

source: netwerk/base/nsINetUtil.idl
source-hash: ad9174ac778bd43ed57f9cf99c924c8feb798a24

- 継承: nsISupports
- 役割: nsINetUtil provides various network-related utility methods.
- 実装: (未記入)

## メソッド / 属性
- `AUTF8String parseRequestContentType(AUTF8String aTypeHeader, AUTF8String aCharset, boolean aHadCharset)`: Parse a Content-Type header value in strict mode.  This is a more
- `AUTF8String parseResponseContentType(AUTF8String aTypeHeader, AUTF8String aCharset, boolean aHadCharset)`: Parse a Content-Type header value in relaxed mode.  This is a more
- `boolean protocolHasFlags(nsIURI aURI, unsigned long aFlag)`: Test whether the given URI's handler has the given protocol flags.
- `boolean URIChainHasFlags(nsIURI aURI, unsigned long aFlags)`: Test whether the protocol handler for this URI or that for any of
- `const unsigned long ESCAPE_ALL`: Escape every character with its %XX-escaped equivalent
- `const unsigned long ESCAPE_XALPHAS`: Leave alphanumeric characters intact and %XX-escape all others
- `const unsigned long ESCAPE_XPALPHAS`: Leave alphanumeric characters intact, convert spaces to '+',
- `const unsigned long ESCAPE_URL_PATH`: Leave alphanumeric characters and forward slashes intact,
- `const unsigned long ESCAPE_URL_APPLE_EXTRA`: Additional encoding for Apple's NSURL compatibility.
- `ACString escapeString(ACString aString, unsigned long aEscapeType)`: escape a string with %00-style escaping
- `const unsigned long ESCAPE_URL_SCHEME`: %XX-escape URL scheme
- `const unsigned long ESCAPE_URL_USERNAME`: %XX-escape username in the URL
- `const unsigned long ESCAPE_URL_PASSWORD`: %XX-escape password in the URL
- `const unsigned long ESCAPE_URL_HOST`: %XX-escape URL host
- `const unsigned long ESCAPE_URL_DIRECTORY`: %XX-escape URL directory
- `const unsigned long ESCAPE_URL_FILE_BASENAME`: %XX-escape file basename in the URL
- `const unsigned long ESCAPE_URL_FILE_EXTENSION`: %XX-escape file extension in the URL
- `const unsigned long ESCAPE_URL_PARAM`: %XX-escape URL parameters
- `const unsigned long ESCAPE_URL_QUERY`: %XX-escape URL query
- `const unsigned long ESCAPE_URL_REF`: %XX-escape URL ref
- `const unsigned long ESCAPE_URL_FILEPATH`: %XX-escape URL path - same as escaping directory, basename and extension
- `const unsigned long ESCAPE_URL_MINIMAL`: %XX-escape scheme, username, password, host, path, params, query and ref
- `const unsigned long ESCAPE_URL_FORCED`: Force %XX-escaping of already escaped sequences
- `const unsigned long ESCAPE_URL_ONLY_ASCII`: Skip non-ascii octets, %XX-escape all others
- `const unsigned long ESCAPE_URL_ONLY_NONASCII`: Skip graphic octets (0x20-0x7E) when escaping
- `const unsigned long ESCAPE_URL_COLON`: Force %XX-escape of colon
- `const unsigned long ESCAPE_URL_SKIP_CONTROL`: Skip C0 and DEL from unescaping
- `const unsigned long ESCAPE_URL_EXT_HANDLER`: %XX-escape external protocol handler URL
- `ACString escapeURL(ACString aStr, unsigned long aFlags)`: %XX-Escape invalid chars in a URL segment.
- `ACString unescapeString(AUTF8String aStr, unsigned long aFlags)`: Expands URL escape sequences
- `boolean extractCharsetFromContentType(AUTF8String aTypeHeader, AUTF8String aCharset, long aCharsetStart, long aCharsetEnd)`: Extract the charset parameter location and value from a content-type
- `void socketProcessTelemetryPing()`: This is test-only. Send an IPC message to let socket process send a
- `void notImplemented()`: This is a void method that is C++ implemented and always
