# nsILoginManagerCrypto (toolkit/components/passwordmgr/nsILoginManagerCrypto.idl)

source: toolkit/components/passwordmgr/nsILoginManagerCrypto.idl
source-hash: 936228548afdfed8f5287aae53c733d5676d36fd

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-sync.js`](../../../browser/base/content/browser-sync.js.md)

## メソッド / 属性
- `const unsigned long ENCTYPE_BASE64`: (未記入)
- `const unsigned long ENCTYPE_SDR`: (未記入)
- `AString encrypt(AString plainText)`: encrypt
- `Promise encryptMany(jsval plainTexts)`: (未記入)
- `AString decrypt(AString cipherText)`: decrypt
- `Promise decryptMany(jsval cipherTexts)`: @param cipherTexts
- `readonly attribute boolean uiBusy`: uiBusy
- `readonly attribute boolean isLoggedIn`: isLoggedIn
- `readonly attribute unsigned long defaultEncType`: defaultEncType
