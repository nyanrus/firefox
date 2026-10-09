# nsIWebNavigation (docshell/base/nsIWebNavigation.idl)

source: docshell/base/nsIWebNavigation.idl
source-hash: d5271dfedb404850797391de661c4aa2aac1880a

- 継承: nsISupports
- 役割: The nsIWebNavigation interface defines an interface for navigating the web.
- 実装: `nsDocShell` (docshell/base/nsDocShell.cpp)
- 使っているJS: [`browser/actors/BlockedSiteParent.sys.mjs`](../../browser/actors/BlockedSiteParent.sys.mjs.md), [`browser/actors/SwitchDocumentDirectionChild.sys.mjs`](../../browser/actors/SwitchDocumentDirectionChild.sys.mjs.md), [`browser/base/content/browser-commands.js`](../../browser/base/content/browser-commands.js.md), [`browser/base/content/browser-siteIdentity.js`](../../browser/base/content/browser-siteIdentity.js.md), [`browser/base/content/browser-trustPanel.js`](../../browser/base/content/browser-trustPanel.js.md), [`browser/components/extensions/parent/ext-browser.js`](../../browser/components/extensions/parent/ext-browser.js.md), [`browser/components/extensions/parent/ext-tabs.js`](../../browser/components/extensions/parent/ext-tabs.js.md), [`browser/components/sessionstore/SessionStore.sys.mjs`](../../browser/components/sessionstore/SessionStore.sys.mjs.md), [`browser/components/tabbrowser/Tabbrowser.sys.mjs`](../../browser/components/tabbrowser/Tabbrowser.sys.mjs.md), [`browser/modules/BrowserDOMWindow.sys.mjs`](../../browser/modules/BrowserDOMWindow.sys.mjs.md), [`browser/modules/URILoadingHelper.sys.mjs`](../../browser/modules/URILoadingHelper.sys.mjs.md)

## メソッド / 属性
- `readonly attribute boolean canGoBack`: Indicates if the object can go back.  If true this indicates that
- `readonly attribute boolean canGoBackIgnoringUserInteraction`: Indicates if the object can go back.  If true this indicates that
- `readonly attribute boolean canGoForward`: Indicates if the object can go forward.  If true this indicates that
- `void goBack(boolean aRequireUserInteraction, boolean aUserActivation)`: Tells the object to navigate to the previous session history item.  When a
- `void goForward(boolean aRequireUserInteraction, boolean aUserActivation)`: Tells the object to navigate to the next session history item.  When a
- `void gotoIndex(long index, boolean aUserActivation)`: Tells the object to navigate to the session history item at a given index.
- `const unsigned long LOAD_FLAGS_MASK`: The following flags may be bitwise combined to form the load flags
- `const unsigned long LOAD_FLAGS_NONE`: This is the default value for the load flags parameter.
- `const unsigned long LOAD_FLAGS_IS_REFRESH`: Flags 0x1, 0x2, 0x4, 0x8 are reserved for internal use by
- `const unsigned long LOAD_FLAGS_IS_LINK`: This flag specifies that the load should have the semantics of a link
- `const unsigned long LOAD_FLAGS_BYPASS_HISTORY`: This flag specifies that history should not be updated.  This flag is only
- `const unsigned long LOAD_FLAGS_REPLACE_HISTORY`: This flag specifies that any existing history entry should be replaced.
- `const unsigned long LOAD_FLAGS_BYPASS_CACHE`: This flag specifies that the local web cache should be bypassed, but an
- `const unsigned long LOAD_FLAGS_BYPASS_PROXY`: This flag specifies that any intermediate proxy caches should be bypassed
- `const unsigned long LOAD_FLAGS_CHARSET_CHANGE`: This flag specifies that a reload was triggered as a result of detecting
- `const unsigned long LOAD_FLAGS_STOP_CONTENT`: If this flag is set, Stop() will be called before the load starts
- `const unsigned long LOAD_FLAGS_FROM_EXTERNAL`: A hint this load was prompted by an external program: take care!
- `const unsigned long LOAD_FLAGS_FIRST_LOAD`: This flag specifies that this is the first load in this object.
- `const unsigned long LOAD_FLAGS_ALLOW_POPUPS`: This flag specifies that the load should not be subject to popup
- `const unsigned long LOAD_FLAGS_BYPASS_CLASSIFIER`: This flag specifies that the URI classifier should not be checked for
- `const unsigned long LOAD_FLAGS_DISALLOW_INHERIT_PRINCIPAL`: Prevent the owner principal from being inherited for this load.
- `const unsigned long LOAD_FLAGS_ERROR_LOAD_CHANGES_RV`: Overwrite the returned error code with a specific result code
- `const unsigned long LOAD_FLAGS_ALLOW_THIRD_PARTY_FIXUP`: This flag specifies that the URI may be submitted to a third-party
- `const unsigned long LOAD_FLAGS_FIXUP_SCHEME_TYPOS`: This flag specifies that common scheme typos should be corrected.
- `const unsigned long LOAD_FLAGS_FORCE_ALLOW_DATA_URI`: Allows a top-level data: navigation to occur. E.g. view-image
- `const unsigned long LOAD_FLAGS_IS_REDIRECT`: This load is the result of an HTTP redirect.
- `const unsigned long LOAD_FLAGS_DISABLE_TRR`: These flags force TRR_DISABLED_MODE or TRR_ONLY_MODE on the
- `const unsigned long LOAD_FLAGS_FORCE_TRR`: LOAD_FLAGS_DISABLE_TRR と対になり、browsingContext の defaultLoadFlags に TRR_DISABLED_MODE または TRR_ONLY_MODE を強制するフラグ群の一つ。
- `const unsigned long LOAD_FLAGS_BYPASS_LOAD_URI_DELEGATE`: This load should bypass the LoadURIDelegate.loadUri.
- `const unsigned long LOAD_FLAGS_USER_ACTIVATION`: This load has a user activation. (e.g: reload button was clicked)
- `void loadURI(nsIURI aURI, jsval aLoadURIOptions)`: Loads a given URI.  This will give priority to loading the requested URI
- `void fixupAndLoadURIString(AString aURIString, jsval aLoadURIOptions)`: Parse / fix up a URI out of the string and load it.
- `void binaryLoadURI(nsIURI aURI, LoadURIOptionsRef aLoadURIOptions)`: A C++ friendly version of loadURI
- `void binaryFixupAndLoadURIString(AString aURIString, LoadURIOptionsRef aLoadURIOptions)`: A C++ friendly version of fixupAndLoadURIString
- `void reload(unsigned long aReloadFlags)`: Tells the Object to reload the current page.  There may be cases where the
- `const unsigned long STOP_NETWORK`: The following flags may be passed as the stop flags parameter to the stop
- `const unsigned long STOP_CONTENT`: This flag specifies that all content activity should be stopped.  This
- `const unsigned long STOP_ALL`: This flag specifies that all activity should be stopped.
- `void stop(unsigned long aStopFlags)`: Stops a load of a URI.
- `readonly attribute Document document`: Retrieves the current DOM document for the frame, or lazily creates a
- `readonly attribute nsIURI currentURI`: The currently loaded URI or null.
- `readonly attribute nsISupports sessionHistory`: The session history object used by this web navigation instance. This
- `void resumeRedirectedLoad(unsigned long long aLoadIdentifier)`: Resume a load which has been redirected from another process.
