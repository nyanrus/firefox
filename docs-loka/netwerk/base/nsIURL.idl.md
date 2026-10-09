# nsIURL (netwerk/base/nsIURL.idl)

source: netwerk/base/nsIURL.idl
source-hash: 42337ccda9b18c310d6a09771e4158bdf8b47841

- 継承: nsIURI
- 役割: The nsIURL interface provides convenience methods that further
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-safebrowsing.js`](../../browser/base/content/browser-safebrowsing.js.md), [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/base/content/pageinfo/pageInfo.js`](../../browser/base/content/pageinfo/pageInfo.js.md), [`browser/components/asrouter/modules/PinnableSitesProvider.sys.mjs`](../../browser/components/asrouter/modules/PinnableSitesProvider.sys.mjs.md), [`browser/components/downloads/DownloadsCommon.sys.mjs`](../../browser/components/downloads/DownloadsCommon.sys.mjs.md), [`browser/components/places/PlacesUIUtils.sys.mjs`](../../browser/components/places/PlacesUIUtils.sys.mjs.md), [`browser/components/preferences/dialogs/permissions.js`](../../browser/components/preferences/dialogs/permissions.js.md), [`browser/components/taskbartabs/TaskbarTabsPageAction.sys.mjs`](../../browser/components/taskbartabs/TaskbarTabsPageAction.sys.mjs.md), [`browser/components/taskbartabs/TaskbarTabsRegistry.sys.mjs`](../../browser/components/taskbartabs/TaskbarTabsRegistry.sys.mjs.md)

## メソッド / 属性
- `readonly attribute AUTF8String directory`: The URL path is broken down into the following principal components:
- `readonly attribute AUTF8String fileName`: Returns the file name portion of a URL.  If the URL denotes a path to a
- `readonly attribute AUTF8String fileBaseName`: The URL filename is broken down even further:
- `readonly attribute AUTF8String fileExtension`: Returns the file extension portion of a filename in a url.  If a file
- `AUTF8String getCommonBaseSpec(nsIURI aURIToCompare)`: This method takes a uri and compares the two.  The common uri portion
- `AUTF8String getRelativeSpec(nsIURI aURIToCompare)`: This method tries to create a string which specifies the location of the

# nsIURLMutator (netwerk/base/nsIURL.idl)

source: netwerk/base/nsIURL.idl
source-hash: 42337ccda9b18c310d6a09771e4158bdf8b47841

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `nsIURIMutator setFileName(AUTF8String aFileName)`: (未記入)
- `nsIURIMutator setFileBaseName(AUTF8String aFileBaseName)`: (未記入)
- `nsIURIMutator setFileExtension(AUTF8String aFileExtension)`: (未記入)
