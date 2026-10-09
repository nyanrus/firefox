# nsINestedURI (netwerk/base/nsINestedURI.idl)

source: netwerk/base/nsINestedURI.idl
source-hash: f687d53f574c8af2aa08a28432042ad0c8a830fd

- 継承: nsISupports
- 役割: nsINestedURI is an interface that must be implemented by any nsIURI
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-siteIdentity.js`](../../browser/base/content/browser-siteIdentity.js.md), [`browser/base/content/browser-trustPanel.js`](../../browser/base/content/browser-trustPanel.js.md), [`browser/components/BrowserContentHandler.sys.mjs`](../../browser/components/BrowserContentHandler.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIURI innerURI`: The inner URI for this nested URI.  This must not return null if the
- `readonly attribute nsIURI innermostURI`: The innermost URI for this nested URI.  This must not return null if the

# nsINestedURIMutator (netwerk/base/nsINestedURI.idl)

source: netwerk/base/nsINestedURI.idl
source-hash: f687d53f574c8af2aa08a28432042ad0c8a830fd

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void init(nsIURI innerURI)`: (未記入)

# nsINestedAboutURIMutator (netwerk/base/nsINestedURI.idl)

source: netwerk/base/nsINestedURI.idl
source-hash: f687d53f574c8af2aa08a28432042ad0c8a830fd

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void initWithBase(nsIURI innerURI, nsIURI baseURI)`: (未記入)

# nsIJSURIMutator (netwerk/base/nsINestedURI.idl)

source: netwerk/base/nsINestedURI.idl
source-hash: f687d53f574c8af2aa08a28432042ad0c8a830fd

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void setBase(nsIURI aBaseURI)`: (未記入)
