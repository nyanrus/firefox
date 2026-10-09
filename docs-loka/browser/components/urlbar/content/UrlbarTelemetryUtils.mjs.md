# browser/components/urlbar/content/UrlbarTelemetryUtils.mjs

source: browser/components/urlbar/content/UrlbarTelemetryUtils.mjs
source-hash: 9596698cf94409785fb1d8507f3e1bade6c1a580
lines: 876

## <module>
- 役割: 検索エンゲージメント (結果の選択、離脱、無効化、バウンス) のテレメトリ値を組み立てるユーティリティ。

## UrlbarTelemetryUtils.actionFromEvent()
- 位置: L44-78
- 役割: イベントから操作の種類 (enter、click、go_button、blur、tab_switch、dismiss など) を決める。
- 触るとき: クリックや Enter、却下の操作が意図と違う計測名になった時。
- 呼び出し先: `UrlbarShared.isInstance()`
- 条件付き依存: `if (UrlbarShared.isInstance(event, MouseEvent))` → `(event.target).classList.contains()`
- 参照: `details.element.dataset.command`, `details.element?.dataset.command`, `details.selType`, `event.target`, `event.type`

## UrlbarTelemetryUtils.modifiersFromEvent()
- 位置: L88-100
- 役割: マウスやキーのイベントで押されていた修飾キー (accel、alt、altgraph、shift) を小文字のカンマ区切りで返す。
- 触るとき: 修飾キー付きの操作の計測がずれる時。
- 呼び出し先: `allModifiers .filter()`, `allModifiers .filter(m => inputEvent.getModifierState(m)) .map()`, `allModifiers .filter(m => inputEvent.getModifierState(m)) .map(m => m.toLowerCase()) .join()`, `inputEvent.getModifierState()`, `m.toLowerCase()`
- 参照: `inputEvent?.getModifierState`

## UrlbarTelemetryUtils.parseSearchString()
- 位置: L114-128
- 役割: 検索文字列の文字数と単語数を数え、単語の配列を返す。文字数は全体、単語は先頭 MAX_TEXT_LENGTH 文字から数える。
- 触るとき: 文字数や単語数の計測値を変える時、または長い入力の扱いを確かめる時。
- 呼び出し先: `searchString .substring()`, `searchString .substring(0, UrlbarShared.MAX_TEXT_LENGTH) .trim()`, `searchString .substring(0, UrlbarShared.MAX_TEXT_LENGTH) .trim() .split()`, `searchString .substring(0, UrlbarShared.MAX_TEXT_LENGTH) .trim() .split(UrlbarShared.REGEXP_SPACES) .filter()`, `searchString.length.toString()`, `searchWords.length.toString()`
- 参照: `UrlbarShared.MAX_TEXT_LENGTH`, `UrlbarShared.REGEXP_SPACES`

## UrlbarTelemetryUtils.startInteractionType()
- 位置: L141-156
- 役割: セッションを始めたイベントから interaction の種類 (typed、pasted、dropped、topsites) を決める。
- 触るとき: 入力の始まり方ごとに interaction の値が変わる時。
- 条件付き依存: `if (event.type == "input")` → `UrlbarShared.isPasteEvent()`
- 参照: `event.type`

## UrlbarTelemetryUtils.collectSnapshot()
- 位置: L175-241
- 役割: 選択時に結果と DOM イベントから engagement のスナップショットを同期的に作る。セッションが無い時は null、イベントが無いのは paste&go と drop&go だけ許し、それ以外は例外にする。
- 触るとき: 選択時に記録する内容を変える時や、paste&go や drop&go で例外が出る原因を調べる時。
- 呼び出し先: `this.actionFromEvent()`, `this.modifiersFromEvent()`, `this.parseSearchString()`
- 条件付き依存: `if (method == "engagement")` → `[ "dismiss", "inaccurate_location", "not_interested", "not_now", "opt_in", "show_less_frequently", ].includes()`
- 参照: `details.element?.dataset.action`, `details.isSessionOngoing`, `details.result?.payload.providesSearchMode`, `details.result?.providerName`, `details.result?.rowIndex`, `details.searchString`, `details.selType`, `startEventInfo.interactionType`

## UrlbarTelemetryUtils.engagementData()
- 位置: L254-261
- 役割: 入力欄と表示中の結果から、検索モード、表示された結果、表示中かどうか、検索源を取り出す。
- 触るとき: 記録に使うデータを content 側で増やす時。
- 呼び出し先: `input.getSearchSource()`
- 参照: `input.searchMode`, `view?.isOpen`, `view?.visibleResults`

## UrlbarTelemetryUtils.smartbarData()
- 位置: L271-280
- 役割: smartbar 専用の chat_id、intent、model を入力欄から取り出す。無ければ空文字にする。
- 触るとき: smartbar の計測項目の値が空になる時。
- 参照: `smartbar.conversationTelemetryInfo?.chat_id`, `smartbar.modelName`, `smartbar.smartbarAction`

## UrlbarTelemetryUtils.exposureEntry()
- 位置: L292-300
- 役割: 露出の結果種別と、キーワード露出が有効なら検索語を求める。私用ウィンドウでは検索語を記録しない。
- 触るとき: 露出の種別や keyword の記録条件を変える時。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarPrefs.get("keywordExposureResults").has()`, `UrlbarShared.searchEngagementTelemetryType()`
- 参照: `queryContext.isPrivate`, `queryContext.trimmedLowerCaseSearchString`

## UrlbarTelemetryUtils.exposureTerminal()
- 位置: L315-320
- 役割: 露出した結果がセッション終了時にまだ残っているかを判定する。非表示の露出は queryContext.results、表示の露出は visibleResults と照合する。
- 触るとき: 露出の終端判定が合わない時や、非表示の露出の扱いを変える時。
- 呼び出し先: `endResults?.includes()`
- 参照: `queryContext?.results`, `result.isHiddenExposure`

## UrlbarTelemetryUtils.recordedEngagementToWire()
- 位置: L335-352
- 役割: 記録する engagement を親に送れる形にする。event と element を落とし、結果と visibleResults を wire 形式にする。
- 触るとき: RecordEngagement で送る項目を増やす時や、親に event が届かない不具合を調べる時。
- 呼び出し先: `data.visibleResults?.map()`, `r.toWire()`, `result?.toWire()`
- 参照: `data.internalDetails`, `internalDetails.element`, `internalDetails.event`

## UrlbarTelemetryUtils.recordedEngagementFromWire()
- 位置: L365-380
- 役割: wire から engagement を復元する。event と element は null にし、結果は liveResults を優先して解決する。
- 触るとき: 親側で記録を組み直す時に、結果が同じものとして扱われているかを確かめる時。
- 呼び出し先: `UrlbarResult.fromWire()`, `wire.visibleResults?.map()`
- 参照: `wire.internalDetails`, `wire.internalDetails.result`

## UrlbarTelemetryUtils.collectBounceSnapshot()
- 位置: L400-442
- 役割: バウンス計測用に、選択時の結果とイベントから後で記録する情報を先に取り出す。セッションが無い時や分類できないイベントの時は null。
- 触るとき: バウンス計測の項目を変える時や、プログラムからの選択がバウンスとして数えられていないかを確かめる時。
- 呼び出し先: `this.actionFromEvent()`, `this.parseSearchString()`
- 参照: `details.location`, `details.result?.providerName`, `details.result?.rowIndex`, `details.searchMode`, `details.searchSource`, `details.searchString`, `details.selType`, `details.windowMode`, `startEventInfo.interactionType`

## UrlbarTelemetryUtils.getSearchMode()
- 位置: L450-461
- 役割: 検索モードを計測用の値にする。エンジンなら search_engine、局所モードならその telemetryLabel、未知なら unknown、無ければ空文字。
- 触るとき: search_mode の計測値が unknown になる時や、新しい検索モードを計測に加える時。
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `UrlbarShared.LOCAL_SEARCH_MODES.find( m => m.source == searchMode.source )?.telemetryLabel`, `m.source`, `searchMode.engineName`, `searchMode.source`

## UrlbarTelemetryUtils.#isRefined()
- 位置: L463-479
- 役割: 今回と前回の検索語の集合が一部だけ重なるかで、言い換えによる再検索 (refined) かを判定する。
- 触るとき: refined の判定が多すぎる、または少なすぎる時。
- 呼び出し先: `intersect()`

## intersect()
- 位置: L467-475
- 役割: setA の語のうち setB にも含まれるものを数え、一部だけが一致する (全部は一致しない) 時に true を返す。#isRefined の中の関数。
- 触るとき: 言い換え判定の条件を変える時。
- 呼び出し先: `setA.values()`, `setB.has()`
- 参照: `setA.size`

## UrlbarTelemetryUtils.getInteractionType()
- 位置: L495-540
- 役割: interaction の値を決める。トップサイトからの検索は topsite_search、returned や restarted で言い換えなら refined、永続検索語では persisted_ の接頭辞を付け、次回比較用の検索語も返す。
- 触るとき: interaction の計測値がずれる時や、永続検索語の計測の扱いを変える時。
- 呼び出し先: `lazy?.UrlbarUtils.isPersistedSearchTermsEnabled()`, `this.#isRefined()`
- 参照: `searchMode?.entry`, `startEventInfo.interactionType`

## UrlbarTelemetryUtils.buildEventInfo()
- 位置: L597-766
- 役割: method (engagement、abandonment、disable、bounce) ごとに Glean のイベント名と項目を組み立てる。smartbar なら追加項目を付ける。未知の method は null。
- 触るとき: 計測項目を新しく足す時や、selected_result などの値が期待と違う時。
- 呼び出し先: `(selIndex + 1).toString()`, `UrlbarPrefs.get()`, `UrlbarShared.searchEngagementTelemetryAction()`, `UrlbarShared.searchEngagementTelemetryGroup()`, `UrlbarShared.searchEngagementTelemetryType()`, `console.error()`, `numChars.toString()`, `numResults.toString()`, `numWords.toString()`, `this.getSearchMode()`, `viewTime.toString()`, `visibleResults .map()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryAction(r)) .filter()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryAction(r)) .filter(v => v) .join()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryGroup(r)) .join()`, `visibleResults .map(r => UrlbarShared.searchEngagementTelemetryType(r)) .join()`
- 条件付き依存: `if (selType == "action")` → `UrlbarShared.searchEngagementTelemetryAction()`
- 条件付き依存: `if (previousEvent == "engagement")` → `UrlbarShared.searchEngagementTelemetryType()`
- 参照: `visibleResults.length`

## UrlbarTelemetryUtils.buildRecordedEngagement()
- 位置: L785-798
- 役割: engagement のスナップショットから Glean 用のイベントと、次回の言い換え判定用の検索語を作る。内部では #buildRecorded を使う。
- 触るとき: content 側の収集と親側の直接経路が同じ計測値を出すかを確かめる時。
- 呼び出し先: `this.#buildRecorded()`
- 参照: `snapshot.method`

## UrlbarTelemetryUtils.buildRecordedDisableCandidate()
- 位置: L817-830
- 役割: Suggest を無効にした計測の候補イベントを作る。検索語の記録は更新しない。
- 触るとき: Suggest の無効化が計測されない時や、候補の作られるタイミングを変える時。
- 呼び出し先: `this.#buildRecorded()`
- 参照: `this.#buildRecorded( "disable", snapshot, engagementData, smartbarData, previousSearchWords ).built`

## UrlbarTelemetryUtils.#buildRecorded()
- 位置: L832-874
- 役割: スナップショットと入力・表示の情報から interaction を求め、buildEventInfo でイベントを作る。engagement、disable、abandonment に共通する組み立て部分。
- 触るとき: 3 種類の計測に共通する項目の値を変える時。
- 呼び出し先: `this.buildEventInfo()`, `this.getInteractionType()`
- 参照: `engagementData.searchMode`, `engagementData.viewIsOpen`, `engagementData.visibleResults`, `interactionResult.interaction`, `interactionResult.previousSearchWords`, `internalDetails.location`, `internalDetails.pickedActionKey`, `internalDetails.provider`, `internalDetails.searchMode`, `internalDetails.searchSource`, `internalDetails.selIndex`, `internalDetails.selType`, `internalDetails.windowMode`, `smartbarData.chatId`, `smartbarData.intent`, `smartbarData.model`, `snapshot.action`, `snapshot.modifiers`, `snapshot.numChars`, `snapshot.numWords`, `snapshot.searchWords`, `snapshot.startEventInfo`
