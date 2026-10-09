# browser/components/sessionstore/SessionStoreFunctions.sys.mjs

source: browser/components/sessionstore/SessionStoreFunctions.sys.mjs
source-hash: 3b42523e4b96d09aedeace381229509ba7651242
lines: 93

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## SessionStoreFunctions.UpdateSessionStore()
- 位置: L7-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStoreFuncInternal.updateSessionStore()`

## SessionStoreFunctions.UpdateSessionStoreForStorage()
- 位置: L25-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStoreFuncInternal.updateSessionStoreForStorage()`

## SSF_updateSessionStore()
- 位置: L43-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.updateSessionStoreFromChild()`
- 条件付き依存: `if (formdata)` → `formdata.toJSON()`
- 条件付き依存: `if (scroll)` → `scroll.toJSON()`
- 参照: `aData.formdata`, `aData.scroll`

## SSF_updateSessionStoreForStorage()
- 位置: L73-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SessionStore.updateSessionStoreFromChild()`
