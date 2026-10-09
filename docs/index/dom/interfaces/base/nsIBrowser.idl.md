# nsIBrowser (dom/interfaces/base/nsIBrowser.idl)

source: dom/interfaces/base/nsIBrowser.idl
source-hash: f8f5fec38560cb642ae835daf68375a1c82182b0

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void dropLinks(Array<AString> links, nsIPrincipal triggeringPrincipal)`: (未記入)
- `void swapBrowsers(nsIBrowser aOtherBrowser)`: Swapping of frameloaders are usually initiated from a frameloader owner
- `void closeBrowser()`: Close the browser (usually means to remove a tab).
- `readonly attribute boolean isRemoteBrowser`: A browser can change from remote to non-remote and vice versa.
- `readonly attribute jsval permanentKey`: The browser's permanent key. This was added temporarily for Session Store,
- `readonly attribute nsIPrincipal contentPrincipal`: (未記入)
- `readonly attribute nsIPrincipal contentPartitionedPrincipal`: (未記入)
- `readonly attribute nsIPolicyContainer policyContainer`: (未記入)
- `readonly attribute nsIReferrerInfo referrerInfo`: (未記入)
- `attribute boolean isNavigating`: Whether or not the browser is in the process of an nsIWebNavigation
- `attribute boolean mayEnableCharacterEncodingMenu`: Whether or not the character encoding menu may be enabled.
- `void updateForStateChange(AString aCharset, nsIURI aDocumentURI, AString aContentType)`: Called by Gecko to update the browser when its state changes.
- `void updateWebNavigationForLocationChange(boolean aCanGoBack, boolean aCanGoBackIgnoringUserInteraction, boolean aCanGoForward)`: Called by Gecko to update the nsIWebNavigation when a location change occurs.
- `void updateForLocationChange(nsIURI aLocation, AString aCharset, boolean aMayEnableCharacterEncodingMenu, nsIURI aDocumentURI, AString aTitle, nsIPrincipal aContentPrincipal, nsIPrincipal aContentPartitionedPrincipal, nsIPolicyContainer aPolicyContainer, nsIReferrerInfo aReferrerInfo, boolean aIsSynthetic, boolean aHasRequestContextID, uint64_t aRequestContextID, AString aContentType)`: Called by Gecko to update the browser when a location change occurs.
- `Promise prepareToChangeRemoteness()`: Called to perform any async tasks which must be completed before changing
- `void beforeChangeRemoteness()`: Called immediately before changing remoteness
- `boolean finishChangeRemoteness(uint64_t aPendingSwitchId)`: Called immediately after changing remoteness.
