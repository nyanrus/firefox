# nsIURIFixupInfo (docshell/base/nsIURIFixup.idl)

source: docshell/base/nsIURIFixup.idl
source-hash: c6fdf87520ed4adece8a0feaf714bf907fb0f03c

- 継承: nsISupports
- 役割: Interface indicating what we found/corrected when fixing up a URI
- 実装: (未記入)

## メソッド / 属性
- `attribute BrowsingContext consumer`: Consumer that asked for fixed up URI.
- `attribute nsIURI preferredURI`: Our best guess as to what URI the consumer will want. Might
- `attribute nsIURI fixedURI`: The fixed-up original input, *never* using a keyword search.
- `attribute AString keywordProviderId`: The id of the search engine used to provide a keyword search;
- `attribute AString keywordAsSent`: The keyword as used for the search (post trimming etc.)
- `attribute nsILoadInfo_SchemelessInputType schemelessInput`: Whether there was no protocol at all and we had to add one in the first place.
- `attribute boolean fixupChangedProtocol`: Whether we changed the protocol instead of using one from the input as-is.
- `attribute boolean fixupCreatedAlternateURI`: Whether we created an alternative URI. We might have added a prefix and/or
- `attribute AUTF8String originalInput`: The original input
- `attribute nsIInputStream postData`: The POST data to submit with the returned URI.

# nsIURIFixup (docshell/base/nsIURIFixup.idl)

source: docshell/base/nsIURIFixup.idl
source-hash: c6fdf87520ed4adece8a0feaf714bf907fb0f03c

- 継承: nsISupports
- 役割: Interface implemented by objects capable of fixing up strings into URIs
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/Tabbrowser.sys.mjs`](../../browser/components/tabbrowser/Tabbrowser.sys.mjs.md)

## メソッド / 属性
- `const unsigned long FIXUP_FLAG_NONE`: No fixup flags.
- `const unsigned long FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`: Allow the fixup to use a keyword lookup service to complete the URI.
- `const unsigned long FIXUP_FLAGS_MAKE_ALTERNATE_URI`: Tell the fixup to make an alternate URI from the input URI, for example
- `const unsigned long FIXUP_FLAG_PRIVATE_CONTEXT`: (未記入)
- `const unsigned long FIXUP_FLAG_FIX_SCHEME_TYPOS`: (未記入)
- `const unsigned long FIXUP_FLAG_FORCE_KEYWORD_LOOKUP`: Like FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP, but does the lookup even when
- `nsIURIFixupInfo getFixupURIInfo(AUTF8String aURIText, unsigned long aFixupFlags)`: Tries to converts the specified string into a URI, first attempting
- `unsigned long webNavigationFlagsToFixupFlags(AUTF8String aURIText, unsigned long aDocShellFlags)`: Convert load flags from nsIWebNavigation to URI fixup flags for use in
- `nsIURIFixupInfo keywordToURI(AUTF8String aKeyword, boolean aIsPrivateContext)`: Converts the specified keyword string into a URI.  Note that it's the
- `nsIURIFixupInfo forceHttpFixup(AUTF8String aUriString)`: Given a uri-like string with a protocol, attempt to fix and convert it
- `void checkHost(nsIURI aURI, nsIDNSListener aListener, jsval aOriginAttributes)`: With the host associated with the URI, use nsIDNSService to determine
- `boolean isDomainKnown(AUTF8String aDomain)`: Returns true if the specified domain is known and false otherwise.
