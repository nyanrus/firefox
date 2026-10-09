# nsIFileURL (netwerk/base/nsIFileURL.idl)

source: netwerk/base/nsIFileURL.idl
source-hash: 3e81ea044d31879dcd5cc1b0fc8ee1adc34a2c97

- 継承: nsIURL
- 役割: nsIFileURL provides access to the underlying nsIFile object corresponding to
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserContentHandler.sys.mjs`](../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/components/newtab/AboutNewTabResourceMapping.sys.mjs`](../../browser/components/newtab/AboutNewTabResourceMapping.sys.mjs.md), [`browser/tools/mozscreenshots/head.js`](../../browser/tools/mozscreenshots/head.js.md), [`browser/tools/mozscreenshots/mozscreenshots/extension/TestRunner.sys.mjs`](../../browser/tools/mozscreenshots/mozscreenshots/extension/TestRunner.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIFile file`: Get the nsIFile corresponding to this URL.

# nsIFileURLMutator (netwerk/base/nsIFileURL.idl)

source: netwerk/base/nsIFileURL.idl
source-hash: 3e81ea044d31879dcd5cc1b0fc8ee1adc34a2c97

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void markFileURL()`: (未記入)
- `void setFile(nsIFile aFile)`: (未記入)
