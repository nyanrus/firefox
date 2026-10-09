# nsIHttpUpgradeListener (netwerk/protocol/http/nsIHttpChannelInternal.idl)

source: netwerk/protocol/http/nsIHttpChannelInternal.idl
source-hash: 261c8a69cfb009e113c87af74e1e0bd0f579e0e9

- 継承: nsISupports
- 役割: The callback interface for nsIHttpChannelInternal::HTTPUpgrade()
- 実装: (未記入)

## メソッド / 属性
- `void onTransportAvailable(nsISocketTransport aTransport, nsIAsyncInputStream aSocketIn, nsIAsyncOutputStream aSocketOut)`: (未記入)
- `void onUpgradeFailed(nsresult aErrorCode)`: (未記入)
- `void onWebSocketConnectionAvailable(WebSocketConnectionBase aConnection)`: (未記入)

# nsIHttpChannelInternal (netwerk/protocol/http/nsIHttpChannelInternal.idl)

source: netwerk/protocol/http/nsIHttpChannelInternal.idl
source-hash: 261c8a69cfb009e113c87af74e1e0bd0f579e0e9

- 継承: nsISupports
- 役割: Dumping ground for http.  This interface will never be frozen.  If you are
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/modules/FaviconLoader.sys.mjs`](../../../browser/modules/FaviconLoader.sys.mjs.md)

## メソッド / 属性
- `attribute nsIURI documentURI`: An http channel can own a reference to the document URI
- `void getRequestVersion(unsigned long major, unsigned long minor)`: Get the major/minor version numbers for the request
- `void getResponseVersion(unsigned long major, unsigned long minor)`: Get the major/minor version numbers for the response
- `void takeAllSecurityMessages(securityMessagesArray aMessages)`: Retrieves all security messages from the security message queue
- `readonly attribute boolean isAuthChannel`: Returns true in case this channel is used for auth;
- `const unsigned long THIRD_PARTY_FORCE_ALLOW`: This flag is set to force relevant cookies to be sent with this load
- `attribute unsigned long thirdPartyFlags`: When set, these flags modify the algorithm used to decide whether to
- `attribute boolean forceAllowThirdPartyCookie`: This attribute was added before the "flags" above and is retained here
- `attribute boolean channelIsForDownload`: External handlers may set this to true to notify the channel
- `readonly attribute AUTF8String localAddress`: The local IP address to which this channel is bound, in the
- `readonly attribute int32_t localPort`: The local port number to which this channel is bound.
- `readonly attribute AUTF8String remoteAddress`: The IP address of the remote host that this channel is
- `readonly attribute int32_t remotePort`: The remote port number that this channel is connected to.
- `void setCacheKeysRedirectChain(StringArray cacheKeys)`: Transfer chain of redirected cache-keys.
- `void HTTPUpgrade(ACString aProtocolName, nsIHttpUpgradeListener aListener)`: HTTPUpgrade allows for the use of HTTP to bootstrap another protocol
- `void setConnectOnly(boolean tlsTunnel)`: Enable only CONNECT to a proxy. Fails if no HTTPUpgrade listener
- `readonly attribute boolean onlyConnect`: True iff the channel is CONNECT only.
- `attribute boolean allowSpdy`: Enable/Disable Spdy negotiation on per channel basis.
- `attribute boolean allowHttp3`: Enable/Disable HTTP3 negotiation on per channel basis.
- `attribute boolean responseTimeoutEnabled`: This attribute en/disables the timeout for the first byte of an HTTP
- `attribute unsigned long initialRwin`: If the underlying transport supports RWIN manipulation, this is the
- `attribute boolean allowAltSvc`: Enable/Disable use of Alternate Services with this channel.
- `attribute boolean beConservative`: If true, do not use newer protocol features that might have interop problems
- `attribute boolean bypassProxy`: If true, do not resolve any proxy for this request. Intended only for use with
- `readonly attribute nsIHttpChannelInternal_ProxyDNSStrategy proxyDNSStrategy`: (未記入)
- `attribute boolean isTRRServiceChannel`: True if channel is used by the internal trusted recursive resolver
- `readonly attribute boolean isResolvedByTRR`: If the channel's remote IP was resolved using TRR.
- `readonly attribute nsIRequest_TRRMode effectiveTRRMode`: The effective TRR mode used to resolve this channel.
- `readonly attribute nsITRRSkipReason_value trrSkipReason`: If the DNS request triggered by this channel didn't use TRR, this value
- `readonly attribute boolean isLoadedBySocketProcess`: True if channel is loaded by socket process.
- `attribute boolean isOCSP`: Set to true if the channel is an OCSP check.
- `const unsigned long TLS_FLAG_CONFIGURE_AS_RETRY`: An opaque flags for non-standard behavior of the TLS system.
- `attribute unsigned long tlsFlags`: (未記入)
- `readonly attribute PRTime lastModifiedTime`: (未記入)
- `attribute boolean corsIncludeCredentials`: Set by nsCORSListenerProxy if credentials should be included in
- `attribute RequestMode requestMode`: Set by nsCORSListenerProxy to indicate CORS load type. Defaults to CORS_MODE_NO_CORS.
- `const unsigned long REDIRECT_MODE_FOLLOW`: (未記入)
- `const unsigned long REDIRECT_MODE_ERROR`: (未記入)
- `const unsigned long REDIRECT_MODE_MANUAL`: (未記入)
- `attribute unsigned long redirectMode`: Set to indicate Request.redirect mode exposed during ServiceWorker
- `const unsigned long FETCH_CACHE_MODE_DEFAULT`: (未記入)
- `const unsigned long FETCH_CACHE_MODE_NO_STORE`: (未記入)
- `const unsigned long FETCH_CACHE_MODE_RELOAD`: (未記入)
- `const unsigned long FETCH_CACHE_MODE_NO_CACHE`: (未記入)
- `const unsigned long FETCH_CACHE_MODE_FORCE_CACHE`: (未記入)
- `const unsigned long FETCH_CACHE_MODE_ONLY_IF_CACHED`: (未記入)
- `attribute unsigned long fetchCacheMode`: Set to indicate Request.cache mode, which simulates the fetch API
- `readonly attribute nsIURI topWindowURI`: The URI of the top-level window that's associated with this channel.
- `void setTopWindowURIIfUnknown(nsIURI topWindowURI)`: Set top-level window URI to this channel only when the topWindowURI
- `readonly attribute nsIURI proxyURI`: Read the proxy URI, which, if non-null, will be used to resolve
- `void setCorsPreflightParameters(CStringArrayRef unsafeHeaders, boolean shouldStripRequestBodyHeader, boolean shouldStripAuthHeader)`: Make cross-origin CORS loads happen with a CORS preflight, and specify
- `void setAltDataForChild(boolean aIsForChild)`: (未記入)
- `void disableAltDataCache()`: Prevent the use of alt-data cache for this request.  Use by the
- `attribute boolean blockAuthPrompt`: When set to true, the channel will not pop any authentication prompts up
- `readonly attribute ACString connectionInfoHashKey`: The connection info's hash key. We use it to test connection separation.
- `attribute unsigned long lastRedirectFlags`: If this channel was created as the result of a redirect, then this
- `attribute TimeStamp navigationStartTimeStamp`: (未記入)
- `void cancelByURLClassifier(nsresult aErrorCode)`: Cancel a channel because we have determined that it needs to be blocked
- `void setIPv4Disabled()`: The channel will be loaded over IPv6, disabling IPv4.
- `void setIPv6Disabled()`: The channel will be loaded over IPv4, disabling IPv6.
- `readonly attribute nsILoadInfo_CrossOriginOpenerPolicy crossOriginOpenerPolicy`: Returns a cached CrossOriginOpenerPolicy that is computed just before we
- `nsILoadInfo_CrossOriginOpenerPolicy computeCrossOriginOpenerPolicy(nsILoadInfo_CrossOriginOpenerPolicy aInitiatorPolicy)`: Called during onStartRequest to compute the cross-origin-opener-policy
- `boolean hasCrossOriginOpenerPolicyMismatch()`: (未記入)
- `nsILoadInfo_CrossOriginEmbedderPolicy getResponseEmbedderPolicy(boolean aIsOriginTrialCoepCredentiallessEnabled)`: (未記入)
- `boolean getOriginAgentClusterHeader()`: Returns the parsed boolean value of the "Origin-Agent-Cluster" header.
- `void DoDiagnosticAssertWhenOnStopNotCalledOnDestroy()`: (未記入)
- `readonly attribute boolean supportsHTTP3`: This attribute indicates if the channel has support for HTTP3
- `readonly attribute boolean hasHTTPSRR`: This attribute indicates if the HTTPS RR is used for this channel.
- `void setEarlyHintObserver(nsIEarlyHintObserver aObserver)`: Set Early Hint Observer.
- `attribute unsigned long long earlyHintPreloaderId`: id of the EarlyHintPreloader to connect back from PreloadService to
- `void setConnectionInfo(nsHttpConnectionInfo aInfo)`: (未記入)
- `readonly attribute boolean isProxyUsed`: This attribute indicates if the channel was loaded via Proxy.
- `void setWebTransportSessionEventListener(WebTransportSessionEventListener aListener)`: Set mWebTransportSessionEventListener.
- `attribute unsigned long earlyHintLinkType`: This attribute indicates the type of Link header in the received
- `attribute boolean isUserAgentHeaderModified`: Indicates whether the User-Agent request header has been modified since
- `void setResponseOverride(nsIReplacedHttpResponse aReplacedHttpResponse)`: The nsIReplacedHttpResponse will be used to override the response of the
- `void setResponseStatus(unsigned long aStatus, ACString aStatusText)`: Updates the status and statusText for the response. Must be called after
- `readonly attribute nsresult lastTransportStatus`: (未記入)
- `void transparentRedirectTo(nsIURI aTargetURI)`: Same as redirectTo in nsIHttpChannel, but handles internal redirect
- `readonly attribute unsigned long caps`: For testing purposes only.
