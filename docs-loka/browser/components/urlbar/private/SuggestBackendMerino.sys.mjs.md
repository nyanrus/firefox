# browser/components/urlbar/private/SuggestBackendMerino.sys.mjs

source: browser/components/urlbar/private/SuggestBackendMerino.sys.mjs
source-hash: 4507c83dc7bb9e7b1a0926a41129fc4eb0787091
lines: 84

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SuggestBackendMerino.enablingPreferences()
- 位置: L22-24
- 役割: (未記入)
- 触るとき: (未記入)

## SuggestBackendMerino.client()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#client`

## SuggestBackendMerino.enable()
- 位置: async L35-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#client`

## SuggestBackendMerino.query()
- 位置: async L41-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queryContext.allowRemoteResults()`, `this.#client.fetch()`, `this.logger.debug()`
- 参照: `lazy.MerinoClient`, `this.#client`, `this.name`

## SuggestBackendMerino.cancelQuery()
- 位置: L61-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#client?.cancelTimeoutTimer()`

## SuggestBackendMerino.onSearchSessionEnd()
- 位置: L75-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#client?.resetSession()`
