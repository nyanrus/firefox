# nsIAboutModule (netwerk/protocol/about/nsIAboutModule.idl)

source: netwerk/protocol/about/nsIAboutModule.idl
source-hash: e304de18d6e13fb12f531ddbd0c1479c32a3905e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-siteIdentity.js`](../../../browser/base/content/browser-siteIdentity.js.md), [`browser/base/content/browser-trustPanel.js`](../../../browser/base/content/browser-trustPanel.js.md), [`browser/base/content/nsContextMenu.sys.mjs`](../../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/components/newtab/AboutNewTabRedirector.sys.mjs`](../../../browser/components/newtab/AboutNewTabRedirector.sys.mjs.md), [`browser/components/newtab/AboutNewTabResourceMapping.sys.mjs`](../../../browser/components/newtab/AboutNewTabResourceMapping.sys.mjs.md), [`browser/extensions/webcompat/about-compat/AboutCompat.sys.mjs`](../../../browser/extensions/webcompat/about-compat/AboutCompat.sys.mjs.md), [`browser/modules/AboutNewTab.sys.mjs`](../../../browser/modules/AboutNewTab.sys.mjs.md)

## メソッド / 属性
- `nsIChannel newChannel(nsIURI aURI, nsILoadInfo aLoadInfo)`: Constructs a new channel for the about protocol module.
- `const unsigned long URI_SAFE_FOR_UNTRUSTED_CONTENT`: A flag that indicates whether a URI should be run with content
- `const unsigned long ALLOW_SCRIPT`: A flag that indicates whether script should be enabled for the
- `const unsigned long HIDE_FROM_ABOUTABOUT`: A flag that indicates whether this about: URI doesn't want to be listed
- `const unsigned long ENABLE_INDEXED_DB`: A flag that indicates whether this about: URI wants Indexed DB enabled.
- `const unsigned long URI_CAN_LOAD_IN_CHILD`: A flag that indicates that this URI can be loaded in a child process
- `const unsigned long URI_MUST_LOAD_IN_CHILD`: A flag that indicates that this URI must be loaded in a child process
- `const unsigned long MAKE_UNLINKABLE`: Obsolete. This flag no longer has any effect and will be removed in future.
- `const unsigned long MAKE_LINKABLE`: A flag that indicates that this URI should be linkable from content.
- `const unsigned long URI_CAN_LOAD_IN_PRIVILEGEDABOUT_PROCESS`: A flag that indicates that this URI can be loaded in the privileged
- `const unsigned long URI_MUST_LOAD_IN_EXTENSION_PROCESS`: A flag that indicates that this URI must be loaded in an extension process (if available).
- `const unsigned long IS_SECURE_CHROME_UI`: A flag that indicates that this about: URI is a secure chrome UI
- `unsigned long getURIFlags(nsIURI aURI)`: A method to get the flags that apply to a given about: URI.  The URI
- `nsIURI getChromeURI(nsIURI aURI)`: A method to get the chrome URI that corresponds to a given about URI.
