# browser/components/extensions/parent/ext-history.js

source: browser/components/extensions/parent/ext-history.js
source-hash: 864038ae3c049c6e33520ba82324bae029a02522
lines: 325

## <module>
- 役割: history API を実装し、閲覧履歴の追加・削除・検索・訪問一覧の取得と、訪問・削除・タイトル変更の各イベントを Places から拡張へ渡す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `TRANSITION_TYPE_TO_TRANSITIONS_MAP.set()`

## getTransitionType()
- 位置: L28-38
- 役割: API の遷移名(link や typed など)を Places の遷移種別に変換する。未知の名前は例外にする。
- 触るとき: history.addUrl が受け付ける遷移名を増やすとき、または未知の遷移での挙動を調べるとき。
- 呼び出し先: `TRANSITION_TO_TRANSITION_TYPES_MAP.get()`

## getTransition()
- 位置: L40-42
- 役割: Places の遷移種別を API の遷移名に戻す。未知の種別は link とする。
- 触るとき: getVisits が返す transition の値を変えるとき。
- 呼び出し先: `TRANSITION_TYPE_TO_TRANSITIONS_MAP.get()`

## convertRowToHistoryItem()
- 位置: L47-57
- 役割: 検索結果の1行を HistoryItem(id・url・タイトル・最終訪問時刻・訪問回数)に変換する。
- 触るとき: history.search の戻り値の項目を増減するとき。
- 呼び出し先: `PlacesUtils.toDate()`, `PlacesUtils.toDate( row.getResultByName("last_visit_date") ).getTime()`, `row.getResultByName()`

## convertRowToVisitItem()
- 位置: L62-70
- 役割: 1行を VisitItem(id・訪問 ID・訪問時刻・参照元の訪問 ID・遷移)に変換する。
- 触るとき: history.getVisits の戻り値の形式を変えるとき。
- 呼び出し先: `PlacesUtils.toDate()`, `PlacesUtils.toDate(row.getResultByName("visit_date")).getTime()`, `String()`, `getTransition()`, `row.getResultByName()`

## accumulateNavHistoryResults()
- 位置: L75-80
- 役割: 結果セットの行を順に読み、変換して配列に追加する。
- 触るとき: クエリ結果の集め方を変えるとき。
- 呼び出し先: `converter()`, `resultSet.getNextRow()`, `results.push()`

## executeAsyncQuery()
- 位置: L82-101
- 役割: Places のレガシークエリを非同期に実行し、完了したら結果の配列で解決する。エラー時は拒否する。
- 触るとき: 履歴検索の実行方法やエラーの扱いを変えるとき。
- 呼び出し先: `PlacesUtils.history.asyncExecuteLegacyQuery()`

## handleResult()
- 位置: L86-88
- 役割: 結果セットの行を変換して results に積む。
- 触るとき: 検索結果が欠ける問題を調べるとき。
- 呼び出し先: `accumulateNavHistoryResults()`

## handleError()
- 位置: L89-95
- 役割: エラーコードとメッセージを含む Error で拒否する。
- 触るとき: 履歴検索のエラーメッセージを変えるとき。
- 呼び出し先: `reject()`
- 参照: `error.message`, `error.result`

## handleCompletion()
- 位置: L96-98
- 役割: 検索完了時に、集めた結果の配列で解決する。
- 触るとき: 検索の完了判定や戻り値の形を変えるとき。
- 呼び出し先: `resolve()`

## onVisited()
- 位置: L105-129
- 役割: page-visited 通知を購読し、各訪問を URL・タイトル・訪問回数などを付けて拡張へ同期的に送る。
- 触るとき: onVisited に渡る項目や発火条件を変えるとき。
- 呼び出し先: `PlacesUtils.observers.addListener()`

## listener()
- 位置: L106-118
- 役割: 訪問イベントを1件ずつ拡張向けの形に変換して送る。
- 触るとき: onVisited のデータ項目を追加・変更するとき。
- 呼び出し先: `fire.sync()`
- 参照: `event.lastKnownTitle`, `event.pageGuid`, `event.typedCount`, `event.url`, `event.visitCount`, `event.visitTime`

## unregister()
- 位置: L122-124
- 役割: page-visited の購読を外す。
- 触るとき: onVisited のリスナーが残る問題を調べるとき。
- 呼び出し先: `PlacesUtils.observers.removeListener()`

## convert()
- 位置: L125-127
- 役割: onVisited の fire 関数を差し替える。
- 触るとき: 拡張の再読み込み後に onVisited が古い fire に送られるときに見る。

## onVisitRemoved()
- 位置: L130-169
- 役割: 履歴の全削除とページ削除の通知を購読し、拡張へ削除内容を同期的に送る。部分的な訪問削除は対象外にする。
- 触るとき: onVisitRemoved の対象(全削除か URL 単位か)を変えるとき。
- 呼び出し先: `PlacesUtils.observers.addListener()`

## listener()
- 位置: L131-152
- 役割: history-cleared は全削除として、page-removed は URL の一覧として送る。部分的な訪問削除の URL は含めない。
- 触るとき: 削除通知の形式や部分削除の扱いを見直すとき。
- 呼び出し先: `fire.sync()`
- 条件付き依存: `if (!event.isPartialVisistsRemoval)` → `removedURLs.push()`
- 条件付き依存: `if (removedURLs.length)` → `fire.sync()`
- 参照: `event.isPartialVisistsRemoval`, `event.type`, `event.url`, `removedURLs.length`

## unregister()
- 位置: L159-164
- 役割: 履歴削除の購読を外す。
- 触るとき: onVisitRemoved のリスナーが残るときに確認する。
- 呼び出し先: `PlacesUtils.observers.removeListener()`

## convert()
- 位置: L165-167
- 役割: onVisitRemoved の fire 関数を差し替える。
- 触るとき: 再読み込み後に削除通知が古い fire に届くときに見る。

## onTitleChanged()
- 位置: L170-194
- 役割: page-title-changed を購読し、変更されたページの ID・URL・タイトルを拡張へ同期的に送る。
- 触るとき: onTitleChanged の項目や発火タイミングを変えるとき。
- 呼び出し先: `PlacesUtils.observers.addListener()`

## listener()
- 位置: L171-180
- 役割: タイトル変更の各イベントを ID・URL・タイトルにまとめて送る。
- 触るとき: onTitleChanged のデータ形式を変えるとき。
- 呼び出し先: `fire.sync()`
- 参照: `event.pageGuid`, `event.title`, `event.url`

## unregister()
- 位置: L184-189
- 役割: page-title-changed の購読を外す。
- 触るとき: タイトル変更のリスナーが残るときに見る。
- 呼び出し先: `PlacesUtils.observers.removeListener()`

## convert()
- 位置: L190-192
- 役割: onTitleChanged の fire 関数を差し替える。
- 触るとき: 再読み込み後にタイトル変更が古い fire に届く問題を調べるとき。

## getAPI()
- 位置: L197-323
- 役割: history の API オブジェクトを組み立て、addUrl・deleteAll・deleteRange・deleteUrl・search・getVisits と3つのイベントを公開する。
- 触るとき: history 名前空間の公開メソッドやイベントを追加・変更するとき。
- 呼び出し先: `new EventManager({ context, module: "history", event: "onTitleChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "history", event: "onVisitRemoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "history", event: "onVisited", extensionApi: this, }).api()`

## addUrl()
- 位置: L200-225
- 役割: 遷移と日時を組み立て、PlacesUtils.history.insert で訪問を1件追加する。遷移名や時刻が不正なら拒否する。
- 触るとき: 拡張から履歴へ URL を追加するときの検証や既定値を変えるとき。
- 呼び出し先: `PlacesUtils.history.insert()`, `PlacesUtils.history.insert(pageInfo).then()`, `Promise.reject()`, `getTransitionType()`
- 条件付き依存: `if (details.visitTime)` → `normalizeTime()`
- 参照: `details.title`, `details.transition`, `details.url`, `details.visitTime`, `error.message`

## deleteAll()
- 位置: L227-229
- 役割: PlacesUtils.history.clear で履歴を全件削除する。
- 触るとき: 拡張からの履歴全削除が効かない問題を調べるとき。
- 呼び出し先: `PlacesUtils.history.clear()`

## deleteRange()
- 位置: L231-240
- 役割: 開始と終了の時刻を条件にして、その期間の訪問を削除する。戻り値は undefined にする。
- 触るとき: 期間指定の削除の境界や戻り値を変えるとき。
- 呼び出し先: `PlacesUtils.history .removeVisitsByFilter()`, `PlacesUtils.history .removeVisitsByFilter(newFilter) .then()`, `normalizeTime()`
- 参照: `filter.endTime`, `filter.startTime`

## deleteUrl()
- 位置: L242-246
- 役割: 指定した URL の履歴を削除する。戻り値は undefined にする。
- 触るとき: URL 単位の削除が期待どおり動かないときに見る。
- 呼び出し先: `PlacesUtils.history.remove()`, `PlacesUtils.history.remove(url).then()`
- 参照: `details.url`

## search()
- 位置: L248-277
- 役割: 期間(開始の既定は直近24時間)と検索語・最大件数(既定100)を指定して、履歴を新しい順に検索する。開始が終了より後なら拒否する。
- 触るとき: history.search の既定期間や最大件数を変えるとき。
- 呼び出し先: `Date.now()`, `PlacesUtils.history.getNewQuery()`, `PlacesUtils.history.getNewQueryOptions()`, `PlacesUtils.toPRTime()`, `executeAsyncQuery()`, `normalizeTime()`
- 条件付き依存: `if (beginTime > endTime)` → `Promise.reject()`
- 参照: `Number.MAX_VALUE`, `historyQuery.beginTime`, `historyQuery.endTime`, `historyQuery.searchTerms`, `options.SORT_BY_DATE_DESCENDING`, `options.includeHidden`, `options.maxResults`, `options.sortingMode`, `query.endTime`, `query.maxResults`, `query.startTime`, `query.text`

## getVisits()
- 位置: L279-299
- 役割: 指定 URL の訪問一覧を新しい順に取得する。URL が無ければ拒否する。
- 触るとき: getVisits の対象や並び順を変えるとき。
- 呼び出し先: `PlacesUtils.history.getNewQuery()`, `PlacesUtils.history.getNewQueryOptions()`, `Services.io.newURI()`, `executeAsyncQuery()`
- 条件付き依存: `if (!url)` → `Promise.reject()`
- 参照: `details.url`, `historyQuery.uri`, `options.RESULTS_AS_VISIT`, `options.SORT_BY_DATE_DESCENDING`, `options.includeHidden`, `options.resultType`, `options.sortingMode`
- XPCOM: `Services.io`
