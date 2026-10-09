# browser/components/urlbar/private/SuggestBackendMerino.sys.mjs

source: browser/components/urlbar/private/SuggestBackendMerino.sys.mjs
source-hash: 4507c83dc7bb9e7b1a0926a41129fc4eb0787091
lines: 84

## <module>
- 役割: オンライン Suggest の Merino バックエンド。オンライン提案が利用可能かつ有効なときに動き、Merino クライアント経由で提案を取得する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SuggestBackendMerino.enablingPreferences()
- 位置: L22-24
- 役割: 有効判定に使う pref として quickSuggestOnlineAvailable と quicksuggest.online.enabled を返す。
- 触るとき: Merino 経由の提案が出ないときに有効条件を確かめるとき。

## SuggestBackendMerino.client()
- 位置: L31-33
- 役割: Merino クライアントを返す。クライアントは遅延作成され、無効化されると破棄されるので null の場合がある。
- 触るとき: クライアントの生存期間や null の扱いを変えるとき。
- 参照: `this.#client`

## SuggestBackendMerino.enable()
- 位置: async L35-39
- 役割: 無効化されたら内部のクライアントを null にする。有効化時には何もしない。
- 触るとき: オンラインを切ったあとに Merino の参照が残らないか確かめるとき。
- 参照: `this.#client`

## SuggestBackendMerino.query()
- 位置: async L41-59
- 役割: 検索文字列が空、またはリモート結果が許可されていなければ空配列を返す。クライアントが無ければ OHTTP を許可して作成し、fetch の結果を返す。
- 触るとき: Merino への問い合わせ条件や OHTTP の利用を変えるとき。
- 呼び出し先: `queryContext.allowRemoteResults()`, `this.#client.fetch()`, `this.logger.debug()`
- 参照: `lazy.MerinoClient`, `this.#client`, `this.name`

## SuggestBackendMerino.cancelQuery()
- 位置: L61-68
- 役割: Merino のタイムアウトタイマーだけを止め、進行中の fetch は中断しない。完了までの遅延を計測するための設計。
- 触るとき: 取消時にタイムアウトが誤って記録される問題や、遅延計測の仕組みを調べるとき。
- 呼び出し先: `this.#client?.cancelTimeoutTimer()`

## SuggestBackendMerino.onSearchSessionEnd()
- 位置: L75-79
- 役割: 検索セッションが終わるとクライアントのセッション ID をリセットする。プライバシーのため、操作をまたいで保持しない。
- 触るとき: Merino のセッション ID の扱いを変えるとき。
- 呼び出し先: `this.#client?.resetSession()`
