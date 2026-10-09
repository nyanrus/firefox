# nsIAuthPrompt2 (netwerk/base/nsIAuthPrompt2.idl)

source: netwerk/base/nsIAuthPrompt2.idl
source-hash: d94d50dfcce173afc9ed402e8f22ea10fbe00d5a

- 継承: nsISupports
- 役割: An interface allowing to prompt for a username and password. This interface
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md)

## メソッド / 属性
- `const uint32_t LEVEL_NONE`: @name Security Levels
- `const uint32_t LEVEL_PW_ENCRYPTED`: Password will be sent encrypted, but the connection is otherwise
- `const uint32_t LEVEL_SECURE`: The connection, both for password and data, is secure.
- `boolean promptAuth(nsIChannel aChannel, uint32_t level, nsIAuthInformation authInfo)`: Requests a username and a password. Implementations will commonly show a
- `nsICancelable asyncPromptAuth(nsIChannel aChannel, nsIAuthPromptCallback aCallback, nsISupports aContext, uint32_t level, nsIAuthInformation authInfo)`: Asynchronously prompt the user for a username and password.
