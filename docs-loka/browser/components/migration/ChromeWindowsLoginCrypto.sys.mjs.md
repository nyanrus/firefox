# browser/components/migration/ChromeWindowsLoginCrypto.sys.mjs

source: browser/components/migration/ChromeWindowsLoginCrypto.sys.mjs
source-hash: 83822f444391b9ac276eabfac96cbde01b2b2eb8
lines: 175

## <module>
- 役割: (未記入)

## ChromeWindowsLoginCrypto.constructor()
- 位置: L39-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeMigrationUtils.getLocalState()`, `ChromeUtils.defineLazyGetter()`, `atob()`, `console.error()`, `crypto.subtle.importKey()`, `this.osCrypto.decryptData()`, `withHeader.slice()`, `withHeader.startsWith()`
- 参照: `DPAPI_KEY_PREFIX.length`, `localState.os_crypt.encrypted_key`, `this.osCrypto`

## ChromeWindowsLoginCrypto.finalize()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.osCrypto.finalize()`

## ChromeWindowsLoginCrypto.arrayToString()
- 位置: L86-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String.fromCharCode()`
- 参照: `arr.length`

## ChromeWindowsLoginCrypto.stringToArray()
- 位置: L94-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `binary_string.charCodeAt()`
- 参照: `binary_string.length`

## ChromeWindowsLoginCrypto.decryptData()
- 位置: async L108-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ciphertextString.startsWith()`, `this._decryptUnversioned()`, `this._decryptV10()`, `this.arrayToString()`

## ChromeWindowsLoginCrypto._decryptUnversioned()
- 位置: async L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.osCrypto.decryptData()`

## ChromeWindowsLoginCrypto._decryptV10()
- 位置: async L119-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ciphertext.slice()`, `crypto.subtle.decrypt()`, `gTextDecoder.decode()`
- 参照: `ENCRYPTION_VERSION_PREFIX.length`, `this._keyPromise`

## ChromeWindowsLoginCrypto.encryptData()
- 位置: async L144-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._encryptUnversioned()`, `this._encryptV10()`

## ChromeWindowsLoginCrypto._encryptUnversioned()
- 位置: async L150-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.osCrypto.encryptData()`

## ChromeWindowsLoginCrypto._encryptV10()
- 位置: async L154-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.getRandomValues()`, `crypto.subtle.encrypt()`, `gTextEncoder.encode()`, `this.arrayToString()`
- 参照: `this._keyPromise`
