# nsIStandardURL (netwerk/base/nsIStandardURL.idl)

source: netwerk/base/nsIStandardURL.idl
source-hash: 80c345f0a8567e9f64ab4d9fb31d6f4ee7464d28

- 継承: nsISupports
- 役割: nsIStandardURL defines the interface to an URL with the standard
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-addons.js`](../../browser/base/content/browser-addons.js.md), [`browser/modules/PermissionUI.sys.mjs`](../../browser/modules/PermissionUI.sys.mjs.md)

## メソッド / 属性
- `const unsigned long URLTYPE_STANDARD`: blah:foo/bar    => blah://foo/bar
- `const unsigned long URLTYPE_AUTHORITY`: blah:foo/bar    => blah://foo/bar
- `const unsigned long URLTYPE_NO_AUTHORITY`: blah:foo/bar    => blah:///foo/bar

# nsIStandardURLMutator (netwerk/base/nsIStandardURL.idl)

source: netwerk/base/nsIStandardURL.idl
source-hash: 80c345f0a8567e9f64ab4d9fb31d6f4ee7464d28

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `nsIURIMutator init(unsigned long aUrlType, long aDefaultPort, AUTF8String aSpec, string aOriginCharset, nsIURI aBaseURI)`: Initialize a standard URL.
- `nsIURIMutator setDefaultPort(long aNewDefaultPort)`: Set the default port.
