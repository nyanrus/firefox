# browser/components/sessionstore/TabStateCache.sys.mjs

source: browser/components/sessionstore/TabStateCache.sys.mjs
source-hash: 4f633ff95222d6733f8dbcde7ff93879e2a85662
lines: 163

## <module>
- 役割: タブごとのセッションデータを WeakMap に保持し、子プロセスからの差分更新を取り込むキャッシュ。
- 呼び出し先: `Object.freeze()`

## get()
- 位置: L25-27
- 役割: TabStateCacheInternal.get を呼ぶ公開 getter。
- 触るとき: キャッシュの読み取り経路を変えるとき。
- 呼び出し先: `TabStateCacheInternal.get()`

## update()
- 位置: L38-40
- 役割: TabStateCacheInternal.update を呼ぶ公開の更新口。
- 触るとき: 子プロセスからの更新がキャッシュへどう届くかを追うとき。
- 呼び出し先: `TabStateCacheInternal.update()`

## get()
- 位置: L55-57
- 役割: 永続キー（タブまたはブラウザ）に対応するキャッシュ済みデータを WeakMap から返す。
- 触るとき: キャッシュがどのタブのデータを返すかを確かめるとき。
- 呼び出し先: `this._data.get()`

## updatePartialStorageChange()
- 位置: L69-96
- 役割: sessionStorage の差分を適用する。ドメイン全体が null なら削除し、値が null のキーは消し、それ以外は書き込む。
- 触るとき: sessionStorage が差分更新で欠けたり残ったりする問題を調べるとき。
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (!(!change[domain]))` → `Object.keys()`
- 参照: `data.storage`

## updatePartialHistoryChange()
- 位置: L110-128
- 役割: 履歴の差分（fromIdx より後ろの entries と index など）を適用する。fromIdx が最大値のときは entries を変えない。
- 触るとき: 履歴の差分更新で項目が消える、または重複する不具合を調べるとき。
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (change.fromIdx != kLastIndex)` → `history.entries.splice()`
- 参照: `Number.MAX_SAFE_INTEGER`, `change.entries`, `change.fromIdx`, `data.history`

## update()
- 位置: L138-161
- 役割: 新しいデータのキーごとに値を置く。null は削除し、storagechange と historychange は専用の差分処理に回す。
- 触るとき: キャッシュの更新規則（null の扱いや差分キーの追加）を変えるとき。
- 呼び出し先: `Object.keys()`, `this._data.get()`, `this._data.set()`
- 条件付き依存: `if (key == "storagechange")` → `this.updatePartialStorageChange()`
- 条件付き依存: `if (key == "historychange")` → `this.updatePartialHistoryChange()`
- 参照: `newData.historychange`, `newData.storagechange`
