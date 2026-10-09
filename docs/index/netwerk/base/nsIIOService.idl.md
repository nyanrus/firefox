# nsIIOService (netwerk/base/nsIIOService.idl)

source: netwerk/base/nsIIOService.idl
source-hash: b349ed351c30ffc5b26d8908d88027fe22aa27a4

- 継承: nsISupports
- 役割: nsIIOService provides a set of network utility functions.  This interface
- 実装: (未記入)

## メソッド / 属性
- `nsIProtocolHandler getProtocolHandler(string aScheme)`: Returns a protocol handler for a given URI scheme.
- `unsigned long getProtocolFlags(string aScheme)`: Returns the protocol flags for a given scheme.
- `unsigned long getDynamicProtocolFlags(nsIURI aURI)`: Returns the dynamic protocol flags for a given URI.
- `long getDefaultPort(string aScheme)`: Returns the default port for a given scheme.
- `nsIURI newURI(AUTF8String aSpec, string aOriginCharset, nsIURI aBaseURI)`: This method constructs a new URI based on the scheme of the URI spec.
- `nsIURI newFileURI(nsIFile aFile)`: This method constructs a new URI from a nsIFile.
- `nsIURI createExposableURI(nsIURI aURI)`: Converts an internal URI (e.g. one that has a username and password in
- `nsIChannel newChannelFromURI(nsIURI aURI, Node aLoadingNode, nsIPrincipal aLoadingPrincipal, nsIPrincipal aTriggeringPrincipal, unsigned long aSecurityFlags, nsContentPolicyType aContentPolicyType)`: Creates a channel for a given URI.
- `nsresult NewChannelFromURIWithClientAndController(nsIURI aURI, Node aLoadingNode, nsIPrincipal aLoadingPrincipal, nsIPrincipal aTriggeringPrincipal, const_MaybeClientInfoRef aLoadingClientInfo, const_MaybeServiceWorkerDescriptorRef aController, unsigned long aSecurityFlags, nsContentPolicyType aContentPolicyType, unsigned long aSandboxFlags, unsigned long long aAssociatedBrowsingContextID, nsIChannel aResult)`: (未記入)
- `nsIChannel newChannelFromURIWithProxyFlagsAndLoadInfo(nsIURI aURI, nsIURI aProxyURI, unsigned long aProxyFlags, nsILoadInfo aLoadInfo)`: Equivalent to newChannelFromURIWithLoadInfo(aURI, aLoadInfo), but also
- `nsIChannel newChannelFromURIWithLoadInfo(nsIURI aURI, nsILoadInfo aLoadInfo)`: Equivalent to newChannelFromURI(aURI, aLoadingNode, ...)
- `nsIChannel newChannel(AUTF8String aSpec, string aOriginCharset, nsIURI aBaseURI, Node aLoadingNode, nsIPrincipal aLoadingPrincipal, nsIPrincipal aTriggeringPrincipal, unsigned long aSecurityFlags, nsContentPolicyType aContentPolicyType)`: Equivalent to newChannelFromURI(newURI(...))
- `nsISuspendableChannelWrapper newSuspendableChannelWrapper(nsIChannel innerChannel)`: Creates a channel that wraps an innerChannel. The
- `nsIWebTransport newWebTransport()`: Creates a WebTransport.
- `jsval originAttributesForNetworkState(nsIChannel aChannel)`: Calls GetOriginAttributesForNetworkState
- `attribute boolean offline`: Returns true if networking is in "offline" mode. When in offline mode,
- `readonly attribute boolean connectivity`: Returns false if there are no interfaces for a network request
- `void setConnectivityForTesting(boolean connectivity)`: This is a method to set connectivity for testing purposes
- `boolean allowPort(long aPort, string aScheme)`: Checks if a port number is banned. This involves consulting a list of
- `void addBlockedLocalPort(long aPort)`: Prevents connections to aPort on the local machine, i.e. to loopback,
- `void removeBlockedLocalPort(long aPort)`: Removes a port previously added with addBlockedLocalPort.
- `ACString extractScheme(AUTF8String urlString)`: Utility to extract the scheme from a URL string, consistently and
- `boolean hostnameIsLocalIPAddress(nsIURI aURI)`: Checks if a URI host is a local IPv4 or IPv6 address literal.
- `boolean hostnameIsSharedIPAddress(nsIURI aURI)`: Checks if a URI host is a shared IPv4 address literal.
- `boolean hostnameIsIPAddressAny(nsIURI aURI)`: (未記入)
- `boolean isValidHostname(AUTF8String hostname)`: Checks if characters not allowed in DNS are present in the hostname
- `attribute boolean manageOfflineStatus`: While this is set, IOService will monitor an nsINetworkLinkService
- `nsIChannel newChannelFromURIWithProxyFlags(nsIURI aURI, nsIURI aProxyURI, unsigned long aProxyFlags, Node aLoadingNode, nsIPrincipal aLoadingPrincipal, nsIPrincipal aTriggeringPrincipal, unsigned long aSecurityFlags, nsContentPolicyType aContentPolicyType)`: Creates a channel for a given URI.
- `readonly attribute boolean socketProcessLaunched`: Return true if socket process is launched.
- `readonly attribute unsigned long long socketProcessId`: The pid for socket process.
- `void registerProtocolHandler(ACString aScheme, nsIProtocolHandler aHandler, unsigned long aProtocolFlags, long aDefaultPort)`: Register a protocol handler at runtime, given protocol flags and a
- `void unregisterProtocolHandler(ACString aScheme)`: Unregister a protocol handler which was previously registered using
- `void setSimpleURIUnknownRemoteSchemes(Array<ACString> aRemoteSchemes)`: Updates the RemoteSettings-specified portion of the defaultURI bypass
- `boolean isSimpleURIUnknownScheme(ACString aScheme)`: Checks if the provided scheme is in the list of unknown schemes that
- `Array<ACString> getSimpleURIUnknownRemoteSchemes()`: returns an array of the remote-settings specified unknown schemes that
- `void addEssentialDomainMapping(ACString aFrom, ACString aTo)`: When a failure is encountered connecting to an essential domain
- `void clearEssentialDomainMapping()`: Clears the essential domain mapping.
- `jsval parseCacheControlHeader(ACString aCacheControlHeader)`: Runs a string through the CacheControlParser and attempts to extract

# nsIIOServiceInternal (netwerk/base/nsIIOService.idl)

source: netwerk/base/nsIIOService.idl
source-hash: b349ed351c30ffc5b26d8908d88027fe22aa27a4

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void SetConnectivity(boolean connectivity)`: This is an internal method that should only be called from ContentChild
- `void NotifyWakeup()`: An internal method to asynchronously run our notifications that happen
