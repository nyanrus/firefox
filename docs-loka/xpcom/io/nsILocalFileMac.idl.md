# nsILocalFileMac (xpcom/io/nsILocalFileMac.idl)

source: xpcom/io/nsILocalFileMac.idl
source-hash: c9e0850e58ee8a514782bd6db456cfd65752f1a1

- 継承: nsIFile
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md)

## メソッド / 属性
- `void initWithCFURL(CFURLRef aCFURL)`: initWithCFURL
- `void initWithFSRef(FSRefPtr aFSRef)`: initWithFSRef
- `CFURLRef getCFURL()`: getCFURL
- `FSRef getFSRef()`: getFSRef
- `attribute OSType fileType`: fileType, creator
- `attribute OSType fileCreator`: (未記入)
- `void launchWithDoc(nsIFile aDocToLoad, boolean aLaunchInBackground)`: launchWithDoc
- `boolean isPackage()`: isPackage
- `readonly attribute AString bundleDisplayName`: bundleDisplayName
- `boolean hasXAttr(ACString aAttrName)`: Return whether or not the file has an extended attribute.
- `Array<uint8_t> getXAttr(ACString aAttrName)`: Get the value of the extended attribute.
- `void setXAttr(ACString aAttrName, Array<uint8_t> aAttrValue)`: Set an extended attribute.
- `void delXAttr(ACString aAttrName)`: Delete an extended attribute.
