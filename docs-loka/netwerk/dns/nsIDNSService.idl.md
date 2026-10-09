# nsIDNSService (netwerk/dns/nsIDNSService.idl)

source: netwerk/dns/nsIDNSService.idl
source-hash: 46fcebe51d85a68483dead2a3ce67a2407cc8993

- 継承: nsISupports
- 役割: nsIDNSService
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/privacy.mjs`](../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/preferences/privacy.js`](../../browser/components/preferences/privacy.js.md)

## メソッド / 属性
- `nsICancelable asyncResolve(AUTF8String aHostName, nsIDNSService_ResolveType aType, nsIDNSService_DNSFlags aFlags, nsIDNSAdditionalInfo aInfo, nsIDNSListener aListener, nsIEventTarget aListenerTarget, jsval aOriginAttributes)`: kicks off an asynchronous host lookup.
- `nsresult asyncResolveNative(AUTF8String aHostName, nsIDNSService_ResolveType aType, nsIDNSService_DNSFlags aFlags, nsIDNSAdditionalInfo aInfo, nsIDNSListener aListener, nsIEventTarget aListenerTarget, OriginAttributes aOriginAttributes, nsICancelable aResult)`: (未記入)
- `nsIDNSAdditionalInfo newAdditionalInfo(AUTF8String aTrrURL, int32_t aPort)`: Returns a new nsIDNSAdditionalInfo object containing the URL we pass to it.
- `void cancelAsyncResolve(AUTF8String aHostName, nsIDNSService_ResolveType aType, nsIDNSService_DNSFlags aFlags, nsIDNSAdditionalInfo aResolver, nsIDNSListener aListener, nsresult aReason, jsval aOriginAttributes)`: Attempts to cancel a previously requested async DNS lookup
- `nsresult cancelAsyncResolveNative(AUTF8String aHostName, nsIDNSService_ResolveType aType, nsIDNSService_DNSFlags aFlags, nsIDNSAdditionalInfo aResolver, nsIDNSListener aListener, nsresult aReason, OriginAttributes aOriginAttributes)`: (未記入)
- `nsIDNSRecord resolve(AUTF8String aHostName, nsIDNSService_DNSFlags aFlags, jsval aOriginAttributes)`: called to synchronously resolve a hostname.
- `nsresult resolveNative(AUTF8String aHostName, nsIDNSService_DNSFlags aFlags, OriginAttributes aOriginAttributes, nsIDNSRecord aResult)`: (未記入)
- `void getDNSCacheEntries(EntriesArray args)`: The method takes a pointer to an nsTArray
- `void clearCache(boolean aTrrToo)`: Clears the DNS cache.
- `void reloadParentalControlEnabled()`: The method is used only for test purpose. We use this to recheck if
- `void setDetectedTrrURI(AUTF8String aURI)`: Notifies the TRR service of a TRR that was automatically detected based
- `void setHeuristicDetectionResult(nsITRRSkipReason_value value)`: Stores the result of the TRR heuristic detection.
- `readonly attribute nsITRRSkipReason_value heuristicDetectionResult`: Returns the result of the last TRR heuristic detection.
- `ACString getTRRSkipReasonName(nsITRRSkipReason_value value)`: (未記入)
- `readonly attribute nsresult lastConfirmationStatus`: The channel status of the last TRR confirmation attempt.
- `readonly attribute nsITRRSkipReason_value lastConfirmationSkipReason`: The TRR skip reason of the last TRR confirmation attempt.
- `void ReportFailedSVCDomainName(ACString aOwnerName, ACString aSVCDomainName)`: Notifies the DNS service that we failed to connect to this alternative
- `boolean IsSVCDomainNameFailed(ACString aOwnerName, ACString aSVCDomainName)`: Check if the given domain name was failed to connect to before.
- `void ResetExcludedSVCDomainName(ACString aOwnerName)`: Reset the exclusion list.
- `readonly attribute AUTF8String currentTrrURI`: Returns a string containing the URI currently used by the TRR service.
- `readonly attribute nsIDNSService_ResolverMode currentTrrMode`: Returns the value of the TRR Service's current default mode.
- `readonly attribute unsigned long currentTrrConfirmationState`: The TRRService's current confirmation state.
- `readonly attribute AUTF8String myHostName`: @return the hostname of the operating system.
- `readonly attribute ACString trrDomain`: returns the current TRR domain.
- `readonly attribute ACString TRRDomainKey`: returns the telemetry key for current TRR domain.
- `void setHttp3FirstForServer(AUTF8String aServer, boolean aEnabled)`: Sets whether a TRR server supports HTTP/3 first for connection attempts.
