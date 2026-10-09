# nsIHttpChannel (netwerk/protocol/http/nsIHttpChannel.idl)

source: netwerk/protocol/http/nsIHttpChannel.idl
source-hash: 0444dad31c18389bb86012c8b62076b54b8ff1de

- 継承: nsIIdentChannel
- 役割: nsIHttpChannel
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/enterprisepolicies/Policies.sys.mjs`](../../../browser/components/enterprisepolicies/Policies.sys.mjs.md), [`browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs`](../../../browser/components/enterprisepolicies/helpers/WebsiteFilter.sys.mjs.md), [`browser/components/genai/LinkPreviewChild.sys.mjs`](../../../browser/components/genai/LinkPreviewChild.sys.mjs.md), [`browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs`](../../../browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs.md), [`browser/components/newtab/SponsorProtection.sys.mjs`](../../../browser/components/newtab/SponsorProtection.sys.mjs.md), [`browser/components/places/InteractionsChild.sys.mjs`](../../../browser/components/places/InteractionsChild.sys.mjs.md), [`browser/modules/ASWebAuthSessionService.sys.mjs`](../../../browser/modules/ASWebAuthSessionService.sys.mjs.md), [`browser/modules/FaviconLoader.sys.mjs`](../../../browser/modules/FaviconLoader.sys.mjs.md)

## メソッド / 属性
- `attribute ACString requestMethod`: REQUEST CONFIGURATION
- `attribute nsIReferrerInfo referrerInfo`: Get/set the referrer information.  This contains the referrer (URI) of the
- `void setReferrerInfoWithoutClone(nsIReferrerInfo aReferrerInfo)`: Set referrer Info without clone new object.
- `readonly attribute ACString protocolVersion`: Returns the network protocol used to fetch the resource as identified
- `readonly attribute uint64_t transferSize`: size consumed by the response header fields and the response payload body
- `readonly attribute uint64_t requestSize`: size consumed by the request header fields and the request payload body
- `readonly attribute uint64_t decodedBodySize`: The size of the message body received by the client,
- `readonly attribute uint64_t encodedBodySize`: The size in octets of the payload body, prior to removing content-codings
- `ACString getRequestHeader(ACString aHeader)`: Get the value of a particular request header.
- `void setRequestHeader(ACString aHeader, ACString aValue, boolean aMerge)`: Set the value of a particular request header.
- `void setNewReferrerInfo(ACString aUrl, nsIReferrerInfo_ReferrerPolicyIDL aPolicy, boolean aSendReferrer)`: Creates and sets new ReferrerInfo object
- `void setEmptyRequestHeader(ACString aHeader)`: Set a request header with empty value.
- `void visitRequestHeaders(nsIHttpHeaderVisitor aVisitor)`: Call this method to visit all request headers.  Calling setRequestHeader
- `void visitNonDefaultRequestHeaders(nsIHttpHeaderVisitor aVisitor)`: Call this method to visit all non-default (UA-provided) request headers.
- `boolean ShouldStripRequestBodyHeader(ACString aMethod)`: Call this method to see if we need to strip the request body headers
- `attribute boolean allowSTS`: This attribute of the channel indicates whether or not
- `attribute unsigned long redirectionLimit`: This attribute specifies the number of redirects this channel is allowed
- `readonly attribute unsigned long responseStatus`: RESPONSE INFO
- `readonly attribute ACString responseStatusText`: Get the HTTP response status text (e.g., "OK").
- `readonly attribute boolean requestSucceeded`: Returns true if the HTTP response code indicates success.  The value of
- `attribute boolean isMainDocumentChannel`: Indicates whether channel should be treated as the main one for the
- `ACString getResponseHeader(ACString header)`: Get the value of a particular response header.
- `void setResponseHeader(ACString header, ACString value, boolean merge)`: Set the value of a particular response header.
- `void visitResponseHeaders(nsIHttpHeaderVisitor aVisitor)`: Call this method to visit all response headers.  Calling
- `void getOriginalResponseHeader(ACString aHeader, nsIHttpHeaderVisitor aVisitor)`: Get the value(s) of a particular response header in the form and order
- `void visitOriginalResponseHeaders(nsIHttpHeaderVisitor aVisitor)`: Call this method to visit all response headers in the form and order as
- `boolean isNoStoreResponse()`: Returns true if the server sent a "Cache-Control: no-store" response
- `boolean isNoCacheResponse()`: Returns true if the server sent the equivalent of a "Cache-control:
- `void redirectTo(nsIURI aTargetURI)`: Instructs the channel to immediately redirect to a new destination.
- `void upgradeToSecure()`: Flags a channel to be upgraded to HTTPS.
- `attribute uint64_t requestContextID`: Identifies the request context for this load.
- `attribute uint64_t topLevelContentWindowId`: ID of the top-level document's inner window.  Identifies the content
- `attribute uint64_t browserId`: ID of the browser for this channel.
- `void logBlockedCORSRequest(AString aMessage, ACString aCategory, boolean aIsWarning)`: In e10s, the information that the CORS response blocks the load is in the
- `void logMimeTypeMismatch(ACString aMessageName, boolean aWarning, AString aURL, AString aContentType)`: (未記入)
- `void setSource(UniqueProfileChunkedBuffer aSource)`: (未記入)
- `attribute AString classicScriptHintCharset`: (未記入)
- `attribute AString documentCharacterSet`: (未記入)
- `attribute boolean requestObserversCalled`: Update the requestObserversCalled boolean flag.
- `attribute boolean isUserAgentHeaderOutdated`: Used to indicate that user agent was overridden or override was reset
- `attribute DictionaryCacheEntry decompressDictionary`: Dictionary for decompression, if any
