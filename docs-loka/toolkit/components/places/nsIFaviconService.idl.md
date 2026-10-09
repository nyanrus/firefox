# nsIFaviconService (toolkit/components/places/nsIFaviconService.idl)

source: toolkit/components/places/nsIFaviconService.idl
source-hash: 2728e3f4273de695c832878ccf1d0422c70c3258

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser.js`](../../../browser/base/content/browser.js.md), [`browser/components/taskbartabs/TaskbarTabsChrome.sys.mjs`](../../../browser/components/taskbartabs/TaskbarTabsChrome.sys.mjs.md), [`browser/components/taskbartabs/TaskbarTabsUtils.sys.mjs`](../../../browser/components/taskbartabs/TaskbarTabsUtils.sys.mjs.md)

## メソッド / 属性
- `const unsigned long FAVICON_LOAD_PRIVATE`: (未記入)
- `const unsigned long FAVICON_LOAD_NON_PRIVATE`: (未記入)
- `const unsigned short ICONDATA_FLAGS_RICH`: (未記入)
- `const unsigned long MAX_FAVICON_BUFFER_SIZE`: The limit in bytes of the size of favicons in memory and passed via the
- `nsIURI getFaviconLinkForIcon(nsIURI aFaviconURI)`: For a given icon URI, this will return a URI that will result in the image.
- `void expireAllFavicons()`: Expire all known favicons from the database.
- `void setDefaultIconURIPreferredSize(unsigned short aDefaultSize)`: Sets the default size returned by preferredSizeFromURI when the uri doesn't
- `unsigned short preferredSizeFromURI(nsIURI aURI)`: Tries to extract the preferred size from an icon uri ref fragment.
- `readonly attribute nsIURI defaultFavicon`: The default favicon URI
- `readonly attribute AUTF8String defaultFaviconMimeType`: The default favicon mimeType
- `Promise setFaviconForPage(nsIURI aPageURI, nsIURI aFaviconURI, nsIURI aDataURL, PRTime aExpiration, boolean isRichIcon)`: Stores the relation between a page URI and a favicon URI, whose icon data
- `Promise getFaviconForPage(nsIURI aPageURI, unsigned short aPreferredWidth)`: Retrieves the favicon URI and data URL associated to the given page, if any.
- `Promise expireFaviconsForPage(nsIURI aPageURI)`: Removes all favicon associations for the given page URI. Typically called
- `Promise tryCopyFavicons(nsIURI aFromPageURI, nsIURI aToPageURI, unsigned long aFaviconLoadType)`: Try to copy cached favicons from a page to another one.

# nsIFavicon (toolkit/components/places/nsIFaviconService.idl)

source: toolkit/components/places/nsIFaviconService.idl
source-hash: 2728e3f4273de695c832878ccf1d0422c70c3258

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIURI uri`: Favicon location.
- `readonly attribute nsIURI dataURI`: Favicon data as Data URL.
- `readonly attribute Array<octet> rawData`: Favicon raw data.
- `readonly attribute ACString mimeType`: Favicon mime type.
- `readonly attribute unsigned short width`: Favicon width.
