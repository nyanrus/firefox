# browser/components/urlbar/private/AmpSuggestions.sys.mjs

source: browser/components/urlbar/private/AmpSuggestions.sys.mjs
source-hash: 3f7ed5fa6dc7e86a297fb49bc25314e591eacf64
lines: 517

## <module>
- 役割: AMP(スポンサー付き)候補の表示、結果メニュー、計測用の quick-suggest ping の送信を担う提供元。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Promise.resolve()`

## AmpSuggestions.enablingPreferences()
- 位置: L45-52
- 役割: この機能を有効にする設定として、feature gate、suggest.amp、suggest.quicksuggest.all、suggest.quicksuggest.sponsored を返す。
- 触るとき: AMP 候補が出ない原因がどの設定で止まっているかを調べるとき、またはスポンサー候補の有効化条件を変えるときに見る。

## AmpSuggestions.primaryUserControlledPreferences()
- 位置: L54-56
- 役割: 利用者が直接切り替える設定として "suggest.amp" を返す。
- 触るとき: 利用者向けの設定画面に出す項目を変えるとき、または AMP 候補の表示を止める設定の対象を確かめるときに見る。

## AmpSuggestions.merinoProvider()
- 位置: L58-60
- 役割: Merino に問い合わせるときのプロバイダ名 "adm" を返す。
- 触るとき: AMP 候補の取得元を変えるとき、または Merino 側のプロバイダ名と合っているか確かめるときに見る。

## AmpSuggestions.rustSuggestionType()
- 位置: L62-64
- 役割: Rust 側の候補種別として "Amp" を返す。
- 触るとき: Rust 側の候補種別との対応を変えるとき、または Rust から届いた AMP 候補を追うときに見る。

## AmpSuggestions.rustProviderConstraints()
- 位置: L66-83
- 役割: ampMatchingStrategy の設定値が有効なら ampAlternativeMatching を指定して返し、未設定や不明な値なら null を返す。
- 触るとき: AMP のキーワード照合方式を変えるとき、または設定値を変えたのに照合方式が反映されないときに見る。
- 呼び出し先: `Object.values()`, `Object.values(lazy.AmpMatchingStrategy).includes()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!Object.values(lazy.AmpMatchingStrategy).includes(intValue))` → `this.logger.error()`
- 参照: `lazy.AmpMatchingStrategy`

## AmpSuggestions.isSuggestionSponsored()
- 位置: L85-87
- 役割: AMP 候補は常にスポンサー付きとして true を返す。
- 触るとき: AMP 候補のスポンサー扱いを変えるとき、または AMP 以外の候補と判定を分けるときに見る。

## AmpSuggestions.getSuggestionTelemetryType()
- 位置: L89-91
- 役割: 計測上の種類名として "adm_sponsored" を返す。
- 触るとき: AMP 候補の計測名を変えるとき、またはダッシュボードで AMP の集計が出ない原因を調べるときに見る。

## AmpSuggestions.enable()
- 位置: L93-111
- 役割: 有効化されたときだけ quick-suggest ping を有効にする。無効化時の削除要求ピングは送らない。
- 触るとき: ping の有効・無効の切り替え条件を変えるとき、または AMP 無効化時にどのピングが送られるかを確かめるときに見る。
- 条件付き依存: `if (enabled)` → `GleanPings.quickSuggest.setEnabled()`

## AmpSuggestions.makeResult()
- 位置: L113-198
- 役割: Merino 候補を Rust 候補と同じ形に正規化し、タイムスタンプを置換し、先頭表示かアイコンサイズを決めて URL 結果を作る。表示回数が 1 以上で検索語が最小長に届かなければ null。
- 触るとき: AMP 候補の表示内容、先頭表示の判定(文字数しきい値や Merino の is_top_pick)、アイコンサイズを変えるとき、または候補の項目が欠ける理由を調べるときに見る。
- 呼び出し先: `Object.assign()`
- 条件付き依存: `if (suggestion.source == "merino")` → `this.#replaceSuggestionTemplates()`
- 条件付き依存: `if (!( suggestion.source == "merino" && typeof suggestion.is_top_pick == "boolean" ))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!isTopPick))` → `lazy.UrlbarPrefs.get()`
- 参照: `amp.header_text`, `amp.suggestion_id`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `normalized.advertiser`, `normalized.blockId`, `normalized.clickUrl`, `normalized.fullKeyword`, `normalized.iabCategory`, `normalized.impressionUrl`, `normalized.rawUrl`, `normalized.requestId`, `normalized.suggestionId`, `normalized.title`, `normalized.url`, `normalized.urlTimestampIndex`, `queryContext.trimmedLowerCaseSearchString.length`, `searchString.length`, `suggestion.block_id`, `suggestion.click_url`, `suggestion.custom_details`, `suggestion.custom_details?.amp`, `suggestion.full_keyword`, `suggestion.iab_category`, `suggestion.impression_url`, `suggestion.is_top_pick`, `suggestion.request_id`, `suggestion.source`, `suggestion.url`, `this.#minKeywordLength`, `this.showLessFrequentlyCount`

## AmpSuggestions.getResultCommands()
- 位置: L200-236
- 役割: 結果メニューの項目(少なくなるよう表示、削除、管理、ヘルプ)を並べて返す。少なくなるよう表示は上限に達していなければ出す。
- 触るとき: AMP 候補の結果メニューに項目を追加したり並び順を変えたりするとき、または表示回数の上限で項目が消える理由を調べるときに見る。
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `this.canShowLessFrequently`

## AmpSuggestions.onImpression()
- 位置: L245-259
- 役割: 状態が engagement のとき、表示されていた各結果について impression ping を送る。
- 触るとき: impression ping を送るタイミングを変えるとき、または engagement 時に計測が欠ける原因を調べるときに見る。
- 条件付き依存: `if (state == "engagement")` → `this.#submitQuickSuggestImpressionPing()`

## AmpSuggestions.onEngagement()
- 位置: L267-316
- 役割: メニューの操作に応じて候補の削除や表示回数の更新を行い、セッション継続時は impression ping を送り、クリックとブロックの ping を送る。
- 触るとき: クリックやブロック時に送る ping の内容を変えるとき、または engagement の後に ping が二重送信または欠落する原因を調べるときに見る。
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 条件付き依存: `if (details.isSessionOngoing)` → `this.#submitQuickSuggestImpressionPing()`
- 条件付き依存: `if (pingData)` → `this.#submitQuickSuggestPing()`
- 参照: `QUICK_SUGGEST_PING_TYPE.BLOCK`, `QUICK_SUGGEST_PING_TYPE.CLICK`, `details.isSessionOngoing`, `details.selType`, `result.payload.sponsoredClickUrl`, `result.payload.sponsoredIabCategory`, `searchString.length`

## AmpSuggestions.incrementShowLessFrequentlyCount()
- 位置: L318-325
- 役割: 上限に達していなければ amp.showLessFrequentlyCount を 1 増やす。
- 触るとき: AMP の少なくなるよう表示の回数の数え方を変えるとき、または回数が想定より早く増える原因を調べるときに見る。
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## AmpSuggestions.showLessFrequentlyCount()
- 位置: L327-330
- 役割: amp.showLessFrequentlyCount の設定値を 0 以上に丸めて返す。
- 触るとき: 表示上限の判定に使われる回数の扱いを変えるとき、または設定が負の値になったときの挙動を確かめるときに見る。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## AmpSuggestions.canShowLessFrequently()
- 位置: L332-335
- 役割: Quick Suggest の表示上限(無ければ 0)に達していないかを返す。上限 0 は無制限扱い。
- 触るとき: 少なくなるよう表示の項目を出す条件を変えるとき、または上限値の出どころを確かめるときに見る。
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## AmpSuggestions.#minKeywordLength()
- 位置: L337-340
- 役割: amp.minKeywordLength の設定値を 0 以上に丸めて返す。
- 触るとき: AMP 候補を出す最小の検索語の長さを変えるとき、または少なくなるよう表示の後に候補が出なくなる理由を調べるときに見る。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## AmpSuggestions.isUrlEquivalentToResultUrl()
- 位置: L342-381
- 役割: Rust 候補は専用の照合関数に任せる。それ以外は長さを比べ、タイムスタンプ位置より前後の文字列が一致し、その部分が 10 桁の数字なら同じ URL とみなす。
- 触るとき: 表示中の結果と同じ候補かを判定する条件を変えるとき、または URL のタイムスタンプ位置がずれて一致しない理由を調べるときに見る。
- 呼び出し先: `TIMESTAMP_REGEXP.test()`, `resultURL.substring()`, `url.substring()`
- 条件付き依存: `if (result.payload.source == "rust")` → `lazy.rawSuggestionUrlMatches()`
- 参照: `result.payload`, `result.payload.originalUrl`, `result.payload.source`, `result.payload.url`, `resultURL.length`, `url.length`

## AmpSuggestions.#submitQuickSuggestPing()
- 位置: L383-431
- 役割: プライベートウィンドウ以外で、設定値を Glean に書き込み quick-suggest ping を送る。送信は前の送信の完了後に直列で行う。
- 触るとき: ping に載せる項目を追加・変更するとき、または ping の送信順序や送信されない条件を調べるときに見る。
- 呼び出し先: `GleanPings.quickSuggest.submit()`, `Object.entries()`, `lazy.ContextId.request()`, `lazy.NimbusFeatures.urlbar.getEnrollmentMetadata()`, `lazy.UrlbarPrefs.get()`, `result.payload.sponsoredAdvertiser.toLocaleLowerCase()`, `result.suggestedIndex.toString()`, `submission.catch()`, `this.#lastPingSubmission.then()`
- 条件付き依存: `if (queryContext.isPrivate)` → `Promise.resolve()`
- 条件付き依存: `if (value !== undefined && value !== "")` → `glean.set()`
- 参照: `Glean.quickSuggest`, `console.error`, `lazy.Region.home`, `nimbusEnrollment?.branch`, `nimbusEnrollment?.slug`, `queryContext.isPrivate`, `result.isBestMatch`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.requestId`, `result.payload.source`, `result.payload.sponsoredBlockId`, `result.payload.suggestionId`, `result.rowIndex`, `this.#lastPingSubmission`

## AmpSuggestions.#submitQuickSuggestImpressionPing()
- 位置: L433-446
- 役割: 表示された結果について、クリックされたかを判定して impression ping を送る。
- 触るとき: impression ping の isClicked の判定を変えるとき、または表示回数の計測がずれる原因を調べるときに見る。
- 呼び出し先: `this.#submitQuickSuggestPing()`
- 参照: `QUICK_SUGGEST_PING_TYPE.IMPRESSION`, `details.result?.id`, `details.selType`, `result.id`, `result.payload.sponsoredImpressionUrl`

## AmpSuggestions.#submitQuickSuggestDeletionRequestPing()
- 位置: async L449-458
- 役割: ContextId のローテーションが有効なら強制ローテーションし、無効なら contextId を設定して削除要求ピングを送る。現在 enable() からは呼ばれていない。
- 触るとき: 削除要求ピングを再び有効にするときや、context_id の計測を削除する作業を進めるときに見る。
- 条件付き依存: `if (lazy.ContextId.rotationEnabled)` → `lazy.ContextId.forceRotation()`
- 条件付き依存: `if (!(lazy.ContextId.rotationEnabled))` → `Glean.quickSuggest.contextId.set()`
- 条件付き依存: `if (!(lazy.ContextId.rotationEnabled))` → `lazy.ContextId.request()`
- 条件付き依存: `if (!(lazy.ContextId.rotationEnabled))` → `GleanPings.quickSuggestDeletionRequest.submit()`
- 参照: `lazy.ContextId.rotationEnabled`

## AmpSuggestions.#replaceSuggestionTemplates()
- 位置: L475-507
- 役割: url と clickUrl に含まれる %YYYYMMDDHH% を現在時刻の 10 桁に置き換え、url の置換位置を urlTimestampIndex に記録する。
- 触るとき: AMP の URL のタイムスタンプ形式を変えるとき、または Merino 経由の URL の時刻が正しくない原因を調べるときに見る。
- 呼び出し先: `n.toString()`, `n.toString().padStart()`, `now.getDate()`, `now.getFullYear()`, `now.getHours()`, `now.getMonth()`, `timestampParts .map()`, `timestampParts .map(n => n.toString().padStart(2, "0")) .join()`, `value.indexOf()`
- 条件付き依存: `if (timestampIndex >= 0)` → `value.substring()`
- 参照: `TIMESTAMP_TEMPLATE.length`, `suggestion.urlTimestampIndex`

## AmpSuggestions.TIMESTAMP_TEMPLATE()
- 位置: L509-511
- 役割: URL 内のタイムスタンプ置換文字列 "%YYYYMMDDHH%" を返す。
- 触るとき: 置換対象の文字列を変えるとき、または他の箇所が同じ文字列を使っているかを確かめるときに見る。

## AmpSuggestions.TIMESTAMP_LENGTH()
- 位置: L513-515
- 役割: タイムスタンプの長さとして 10 を返す。
- 触るとき: タイムスタンプの書式(桁数)を変えるとき、または URL の一致判定で長さがずれる原因を調べるときに見る。
