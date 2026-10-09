# browser/components/migration/ChromeMacOSLoginCrypto.sys.mjs

source: browser/components/migration/ChromeMacOSLoginCrypto.sys.mjs
source-hash: 74870dddaeff815cdc7ab84eda4d2b53fb43b1d4
lines: 186

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`, `new Uint8Array(kCCBlockSizeAES128).fill()`

## ChromeMacOSLoginCrypto.constructor()
- 位置: L82-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.subtle .importKey()`, `crypto.subtle .importKey("raw", gTextEncoder.encode(encKey), "PBKDF2", false, [ "deriveKey", ]) .then()`, `crypto.subtle.deriveKey()`, `gTextEncoder.encode()`, `lazy.gKeychainUtils.getGenericPassword()`
- 参照: `console.error`, `this.ALGORITHM`, `this._keyPromise`

## ChromeMacOSLoginCrypto.arrayToString()
- 位置: L125-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String.fromCharCode()`
- 参照: `arr.length`

## ChromeMacOSLoginCrypto.stringToArray()
- 位置: L133-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `binary_string.charCodeAt()`
- 参照: `binary_string.length`

## ChromeMacOSLoginCrypto.decryptData()
- 位置: async L147-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ciphertext.startsWith()`, `ciphertext.substring()`, `crypto.subtle.decrypt()`, `gTextDecoder.decode()`, `this.arrayToString()`, `this.stringToArray()`
- 参照: `ENCRYPTION_VERSION_PREFIX.length`, `this.ALGORITHM`, `this._keyPromise`

## ChromeMacOSLoginCrypto.encryptData()
- 位置: async L169-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String.fromCharCode()`, `crypto.subtle.encrypt()`, `gTextEncoder.encode()`
- 参照: `this.ALGORITHM`, `this._keyPromise`
