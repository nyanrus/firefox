# nsIAuthPrompt (netwerk/base/nsIAuthPrompt.idl)

source: netwerk/base/nsIAuthPrompt.idl
source-hash: c5525ccb28c02e03f15e09e05b6979088413d87e

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md)

## メソッド / 属性
- `const uint32_t SAVE_PASSWORD_NEVER`: (未記入)
- `const uint32_t SAVE_PASSWORD_FOR_SESSION`: (未記入)
- `const uint32_t SAVE_PASSWORD_PERMANENTLY`: (未記入)
- `boolean prompt(wstring dialogTitle, wstring text, wstring passwordRealm, uint32_t savePassword, wstring defaultText, wstring result)`: Puts up a text input dialog with OK and Cancel buttons.
- `boolean promptUsernameAndPassword(wstring dialogTitle, wstring text, wstring passwordRealm, uint32_t savePassword, wstring user, wstring pwd)`: Puts up a username/password dialog with OK and Cancel buttons.
- `Promise asyncPromptUsernameAndPassword(wstring dialogTitle, wstring text, wstring passwordRealm, uint32_t savePassword, wstring user, wstring pwd)`: Puts up an async username/password dialog with OK and Cancel buttons.
- `boolean promptPassword(wstring dialogTitle, wstring text, wstring passwordRealm, uint32_t savePassword, wstring pwd)`: Puts up a password dialog with OK and Cancel buttons.
- `Promise asyncPromptPassword(wstring dialogTitle, wstring text, wstring passwordRealm, uint32_t savePassword, wstring pwd)`: Puts up an async password dialog with OK and Cancel buttons.
