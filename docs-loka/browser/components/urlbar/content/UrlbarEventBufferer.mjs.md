# browser/components/urlbar/content/UrlbarEventBufferer.mjs

source: browser/components/urlbar/content/UrlbarEventBufferer.mjs
source-hash: 4172241eafb52c6157adb6880e30a98c526f8702
lines: 414

## <module>
- 役割: 検索結果が届くまでの間に押されたキー(Enter、下矢印、Tab、Mac の ctrl+n/p)を一時的に溜め、結果が揃ってから再生するバッファー。
- 呼び出し先: `Object.freeze()`

## UrlbarEventBufferer.logger()
- 位置: L47-52
- 役割: EventBufferer 用のロガーを遅延生成して返す。
- 触るとき: バッファーの遅延や再生をログで追うとき。
- 呼び出し先: `UrlbarShared.getLogger()`
- 参照: `this.#logger`

## UrlbarEventBufferer.DEFERRING_TIMEOUT_MS()
- 位置: L55-57
- 役割: 遅延の上限時間を pref から読んで返す。
- 触るとき: キーを待たせる最長時間を調整するとき。
- 呼び出し先: `UrlbarPrefs.get()`

## UrlbarEventBufferer.constructor()
- 位置: L65-82
- 役割: input の blur を監視し、クエリ開始の状態を初期化し、コントローラーにリスナーとして登録する。
- 触るとき: バッファーの生成や監視の仕組みを変えるとき。
- 呼び出し先: `performance.now()`, `this.input.controller.addListener()`, `this.input.inputField.addEventListener()`
- 参照: `QUERY_STATUS.UKNOWN`, `this.#lastQuery`, `this.input`

## UrlbarEventBufferer.queryStarting()
- 位置: L93-103
- 役割: 新しいクエリの開始時刻と状態を記録し、遅延タイマーを解除する。コントローラーがクエリを送る前に呼ぶ。
- 触るとき: クエリ開始時点で遅延を有効にするタイミングを変えるとき。
- 呼び出し先: `performance.now()`
- 条件付き依存: `if (this.#deferringTimeout)` → `clearTimeout()`
- 参照: `QUERY_STATUS.RUNNING`, `this.#deferringTimeout`, `this.#lastQuery`

## UrlbarEventBufferer.onQueryCancelled()
- 位置: L107-109
- 役割: クエリがキャンセルされたら状態を完了にする。
- 触るとき: キャンセル後に遅延キーが待たされ続ける問題を調べるとき。
- 参照: `QUERY_STATUS.COMPLETE`, `this.#lastQuery.status`

## UrlbarEventBufferer.onQueryFinished()
- 位置: L111-113
- 役割: クエリが終わったら状態を完了にする。
- 触るとき: クエリ終了後も遅延が解けない問題を調べるとき。
- 参照: `QUERY_STATUS.COMPLETE`, `this.#lastQuery.status`

## UrlbarEventBufferer.onQueryResults()
- 位置: L120-133
- 役割: ヒューリスティック結果が揃ったら状態を更新し、コンテキストを差し替えて、次のタスクで溜めたイベントを安全な時だけ再生する。
- 触るとき: 結果が届いた後に遅延キーが再生されるタイミングを変えるとき。
- 呼び出し先: `setTimeout()`, `this.replayDeferredEvents()`
- 参照: `QUERY_STATUS.RUNNING_GOT_ALL_HEURISTIC_RESULTS`, `queryContext.pendingHeuristicProviders.size`, `this.#lastQuery.context`, `this.#lastQuery.status`

## UrlbarEventBufferer.handleEvent()
- 位置: L141-152
- 役割: input が blur したら溜めたイベントとタイマーを破棄する。
- 触るとき: フォーカスを失ったあとにキーが誤って再生されないことを確かめるとき。
- 条件付き依存: `if (event.type == "blur")` → `this.logger.debug()`
- 条件付き依存: `if (this.#deferringTimeout)` → `clearTimeout()`
- 参照: `event.type`, `this.#deferringTimeout`, `this.#eventsQueue.length`

## UrlbarEventBufferer.maybeDeferEvent()
- 位置: L162-172
- 役割: イベントを遅延すべきか判定し、遅延しなければ即座にコールバックを呼ぶ。
- 触るとき: キー処理の入口で遅延の有無を分ける箇所を変えるとき。
- 呼び出し先: `callback()`, `this.shouldDeferEvent()`
- 条件付き依存: `if (this.shouldDeferEvent(event))` → `this.deferEvent()`

## UrlbarEventBufferer.deferEvent()
- 位置: L181-206
- 役割: イベントを検索語とともに溜め、まだタイマーが無ければ残り時間に合わせて全件再生のタイマーを張る。同じイベントの二重遅延は例外にする。
- 触るとき: 溜めたイベントの破棄条件や、タイムアウトの計算を変えるとき。
- 呼び出し先: `this.#eventsQueue.find()`, `this.#eventsQueue.push()`, `this.logger.debug()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `performance.now()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `setTimeout()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `this.replayDeferredEvents()`
- 条件付き依存: `if (!this.#deferringTimeout)` → `Math.max()`
- 参照: `UrlbarEventBufferer.DEFERRING_TIMEOUT_MS`, `event.keyCode`, `event.type`, `item.event`, `this.#deferringTimeout`, `this.#lastQuery.context.searchString`, `this.#lastQuery.startDate`

## UrlbarEventBufferer.replayDeferredEvents()
- 位置: L216-238
- 役割: 溜めた先頭のイベントから順に再生する。検索語が変わっていれば破棄する。onlyIfSafe が真なら安全な場合だけ再生する。
- 触るとき: 溜めたキーの再生順や破棄条件を変えるとき。
- 呼び出し先: `setTimeout()`, `this.#eventsQueue.shift()`, `this.isSafeToPlayDeferredEvent()`, `this.replayDeferredEvents()`
- 条件付き依存: `if (searchString == this.#lastQuery.context.searchString)` → `callback()`
- 参照: `this.#eventsQueue`, `this.#eventsQueue.length`, `this.#lastQuery.context.searchString`

## UrlbarEventBufferer.shouldDeferEvent()
- 位置: L246-295
- 役割: 既に溜めがあれば後続も溜め、それ以外は Enter、Tab、下矢印などの条件と時間経過で遅延するかを決める。
- 触るとき: どのキーをどの状況で待たせるかの判定を変えるとき。
- 呼び出し先: `DEFERRED_KEY_CODES.has()`, `UrlbarContentUtils.getPlatform()`, `performance.now()`, `this.isSafeToPlayDeferredEvent()`
- 条件付き依存: `if (DEFERRED_KEY_CODES.has(event.keyCode))` → `this.input.controller.keyEventMovesCaret()`
- 参照: `KeyEvent.DOM_VK_TAB`, `UrlbarEventBufferer.DEFERRING_TIMEOUT_MS`, `event.ctrlKey`, `event.key`, `event.keyCode`, `this.#eventsQueue.length`, `this.#lastQuery.startDate`, `this.input.isComposing`, `this.input.view.isOpen`, `this.waitingDeferUserSelectionProviders`

## UrlbarEventBufferer.isDeferringEvents()
- 位置: L302-304
- 役割: 溜めたイベントが残っているかを返す。
- 触るとき: 呼び出し側が遅延中かどうかを判断する箇所を調べるとき。
- 参照: `this.#eventsQueue.length`

## UrlbarEventBufferer.waitingDeferUserSelectionProviders()
- 位置: L312-314
- 役割: 現在のクエリで、ユーザー選択を遅らせるよう要求したプロバイダーがあるかを返す。
- 触るとき: プロバイダーが選択の遅延を要求するケースの挙動を調べるとき。
- 参照: `this.#lastQuery.context?.deferUserSelectionProviders.size`

## UrlbarEventBufferer.isSafeToPlayDeferredEvent()
- 位置: L326-374
- 役割: 溜めたイベントを今再生して良いかを、クエリ状態、ビューの開閉、選択中の結果から判定する。
- 触るとき: 結果が揃う前に再生されて選択がずれる問題、または再生条件を変えるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_RETURN`, `QUERY_STATUS.COMPLETE`, `QUERY_STATUS.RUNNING`, `QUERY_STATUS.UKNOWN`, `event.ctrlKey`, `event.key`, `event.keyCode`, `selectedResult.heuristic`, `this.#lastQuery.status`, `this.input.view.isOpen`, `this.input.view.selectedResult`, `this.lastResultIsSelected`, `this.waitingDeferUserSelectionProviders`

## UrlbarEventBufferer.lastResultIsSelected()
- 位置: L376-384
- 役割: 最後の結果が選択中かどうかを返す。下矢印が一つ目のボタンへ飛ぶのを防ぐ判定に使う。
- 触るとき: 下矢印で検索モードのボタンへ誤って移る挙動を調べるとき。
- 参照: `results.length`, `this.#lastQuery.context.results`, `this.input.view.selectedResult`
