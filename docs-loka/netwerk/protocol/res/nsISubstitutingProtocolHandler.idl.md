# nsISubstitutingProtocolHandler (netwerk/protocol/res/nsISubstitutingProtocolHandler.idl)

source: netwerk/protocol/res/nsISubstitutingProtocolHandler.idl
source-hash: 5c042ecdac4ab4c6d82c2a92a5e13178535647c7

- 継承: nsIProtocolHandler
- 役割: Protocol handler superinterface for a protocol which performs substitutions
- 実装: (未記入)
- 使っているJS: [`browser/components/newtab/AboutNewTabResourceMapping.sys.mjs`](../../../browser/components/newtab/AboutNewTabResourceMapping.sys.mjs.md), [`browser/extensions/formautofill/api.js`](../../../browser/extensions/formautofill/api.js.md), [`browser/extensions/webcompat/about-compat/aboutPage.js`](../../../browser/extensions/webcompat/about-compat/aboutPage.js.md), [`browser/tools/mozscreenshots/mozscreenshots/extension/api.js`](../../../browser/tools/mozscreenshots/mozscreenshots/extension/api.js.md)

## メソッド / 属性
- `const short ALLOW_CONTENT_ACCESS`: Content script may access files in this package.
- `const short RESOLVE_JAR_URI`: This substitution exposes nsIJARURI instead of a nsIFileURL.  By default
- `void setSubstitution(ACString root, nsIURI baseURI)`: Sets the substitution for the root key:
- `void setSubstitutionWithFlags(ACString root, nsIURI baseURI, uint32_t flags)`: Same as setSubstitution, but with specific flags.
- `nsIURI getSubstitution(ACString root)`: Gets the substitution for the root key.
- `boolean hasSubstitution(ACString root)`: Returns TRUE if the substitution exists and FALSE otherwise.
- `AUTF8String resolveURI(nsIURI resURI)`: Utility function to resolve a substituted URI.  A resolved URI is not
