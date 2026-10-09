# browser/components/urlbar/content/UrlbarChildTelemetry.mjs

source: browser/components/urlbar/content/UrlbarChildTelemetry.mjs
source-hash: 73fef3a888a18f2284a81e82aca222fb4137c935
lines: 375

## <module>
- 役割: メッセージ経路の content 側で、urlbar のエンゲージメント計測セッションを管理し、確定した記録を親の記録器へ送るコレクター。

## UrlbarChildTelemetry.constructor()
- 位置: L56-58
- 役割: 紐づく UrlbarChildController を保持する。
- 触るとき: 計測コレクターが入力と親にどう接続されるかを確かめるとき。
- 参照: `this.#controller`

## UrlbarChildTelemetry.start()
- 位置: L73-127
- 役割: ユーザー操作からセッションを一度だけ開始する。既存セッションの種類(topsites や returned)を更新し、有効なイベント種別のみ受け付ける。
- 触るとき: セッションの開始条件や interactionType の判定を変えるとき。
- 呼び出し先: `UrlbarTelemetryUtils.startInteractionType()`, `validEvents.includes()`
- 条件付き依存: `if (this.#startEventInfo.interactionType == "topsites")` → `UrlbarTelemetryUtils.startInteractionType()`
- 条件付き依存: `if (!event)` → `console.error()`
- 条件付き依存: `if (this.#controller.input.sapName === "smartbar")` → `validEvents.push()`
- 条件付き依存: `if (!validEvents.includes(event.type))` → `console.error()`
- 条件付き依存: `if (!this.#controller.parentController._lastQueryContextWrapper)` → `this.#controller.parentController.setLastQueryContextCache()`
- 参照: `event.timeStamp`, `event.type`, `this.#controller.input.sapName`, `this.#controller.parentController._lastQueryContextWrapper`, `this.#startEventInfo`, `this.#startEventInfo.interactionType`, `this.#startEventInfo.searchString`

## UrlbarChildTelemetry.record()
- 位置: L141-211
- 役割: 入力とビューの状態からエンゲージメントのスナップショットを組み立て、Suggest 表示時は無効化候補も添えて、親の recordEngagement へ送る。セッションが続いていなければ開始情報を消す。
- 触るとき: エンゲージメント計測の中身や送信タイミングを変えるとき。
- 呼び出し先: `UrlbarTelemetryUtils.collectSnapshot()`, `console.error()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.engagementData()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.smartbarData()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.buildRecordedEngagement()`
- 条件付き依存: `if (snapshot)` → `engagementData.visibleResults.some()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.buildRecordedDisableCandidate()`
- 条件付き依存: `if (snapshot)` → `this.#resolveExposures()`
- 条件付き依存: `if (snapshot)` → `this.#controller.parentController.recordEngagement()`
- 条件付き依存: `if (snapshot)` → `UrlbarTelemetryUtils.recordedEngagementToWire()`
- 参照: `details.isSessionOngoing`, `engagementData.visibleResults`, `r.providerName`, `snapshot.internalDetails`, `snapshot.internalDetails.searchSource`, `snapshot.method`, `this.#controller`, `this.#handlingRecord`, `this.#previousSearchWords`, `this.#startEventInfo`, `view.queryContext`

## UrlbarChildTelemetry.discard()
- 位置: L216-218
- 役割: 進行中のセッションを破棄し、記録させない。
- 触るとき: 記録すべきでない操作で計測を取り消す箇所を追うとき。
- 参照: `this.#startEventInfo`

## UrlbarChildTelemetry.reset()
- 位置: L224-227
- 役割: 直前のセッションの検索語を消し、親側の計測状態もリセットする。
- 触るとき: 連続した検索の判定(refined など)がセッション間で持ち越される問題を調べるとき。
- 呼び出し先: `this.#controller.parentController.resetEngagement()`
- 参照: `this.#previousSearchWords`

## UrlbarChildTelemetry.addExposure()
- 位置: L235-239
- 役割: 露出テレメトリを持つ結果を、一件につき一度だけ露出として積む。
- 触るとき: 結果が表示されたときの露出記録の条件を変えるとき。
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#addExposureInternal()`
- 参照: `result.exposureTelemetry`

## UrlbarChildTelemetry.addTentativeExposure()
- 位置: L247-251
- 役割: 露出テレメトリを持つ結果を仮の露出として保留する。
- 触るとき: 非表示のまま保留される結果の露出を後から確定させるとき。
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#tentativeExposures.push()`
- 参照: `result.exposureTelemetry`

## UrlbarChildTelemetry.acceptTentativeExposures()
- 位置: L256-261
- 役割: 保留中の仮の露出を正式な露出に昇格させ、保留を空にする。
- 触るとき: 保留していた結果が実際に表示されたと判明したときの処理を変えるとき。
- 呼び出し先: `this.#addExposureInternal()`
- 参照: `this.#tentativeExposures`

## UrlbarChildTelemetry.discardTentativeExposures()
- 位置: L266-268
- 役割: 保留中の仮の露出を破棄する。
- 触るとき: 表示されなかった結果の露出を記録しないようにするとき。
- 参照: `this.#tentativeExposures`

## UrlbarChildTelemetry.#addExposureInternal()
- 位置: L270-280
- 役割: 結果ごとに一度だけ、結果種別とキーワードを求めて露出の一覧に入れる。
- 触るとき: 露出の種別やキーワードの決め方を変えるとき。
- 呼び出し先: `this.#exposureResults.has()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposureResults.add()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `UrlbarTelemetryUtils.exposureEntry()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposures.push()`

## UrlbarChildTelemetry.#resolveExposures()
- 位置: L292-308
- 役割: 積んだ露出を、セッション終了時点の表示結果に照らして terminal の値を付けた形にし、キューを空にする。
- 触るとき: 露出の terminal 判定や、セッション終了時の露出の送り方を変えるとき。
- 呼び出し先: `UrlbarTelemetryUtils.exposureTerminal()`, `exposures.map()`, `this.#exposureResults.delete()`
- 参照: `this.#exposures`, `this.#tentativeExposures`

## UrlbarChildTelemetry.startTrackingBounceEvent()
- 位置: async L321-373
- 役割: エンゲージメント後のバウンス候補を入力の状態から組み立て、親に渡して追跡と記録を任せる。
- 触るとき: タブ遷移後の離脱(バウンス)計測の内容や送信条件を変えるとき。
- 呼び出し先: `UrlbarTelemetryUtils.buildEventInfo()`, `UrlbarTelemetryUtils.collectBounceSnapshot()`, `UrlbarTelemetryUtils.engagementData()`, `UrlbarTelemetryUtils.getInteractionType()`, `UrlbarTelemetryUtils.smartbarData()`, `this.#controller.parentController.startTrackingBuiltBounce()`
- 参照: `engagementData.searchMode`, `engagementData.viewIsOpen`, `engagementData.visibleResults`, `smartbarData.chatId`, `smartbarData.intent`, `smartbarData.model`, `snapshot.action`, `snapshot.location`, `snapshot.numChars`, `snapshot.numWords`, `snapshot.provider`, `snapshot.searchMode`, `snapshot.searchWords`, `snapshot.selIndex`, `snapshot.selType`, `snapshot.startEventInfo`, `snapshot.visibleResults`, `snapshot.windowMode`, `this.#controller`, `this.#previousSearchWords`, `this.#startEventInfo`
