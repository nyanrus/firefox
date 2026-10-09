# browser/components/urlbar/UrlbarProviderQuickSuggest.sys.mjs

source: browser/components/urlbar/UrlbarProviderQuickSuggest.sys.mjs
source-hash: 410ed98058deb64ac1f2006fbf9f5be8bb542b52
lines: 641

## <module>
- 役割: Firefox Suggest(QuickSuggest バックエンドと Merino 由来の提案)を URL バーの結果にするネットワーク系プロバイダー。提案の取得、スコア付け、結果化、表示・削除を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderQuickSuggest.type()
- 位置: L35-37
- 役割: プロバイダー種別として NETWORK を返す。
- 触るとき: Suggest 結果の種別と、ネットワーク系としての扱いを確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.NETWORK`

## UrlbarProviderQuickSuggest.DEFAULT_SUGGESTION_SCORE()
- 位置: L45-47
- 役割: スコアの無い提案に使う既定値(0.2)を返す静的ゲッター。
- 触るとき: スコアの無い提案の既定順位を変えるとき。

## UrlbarProviderQuickSuggest.isActive()
- 位置: async L56-88
- 役割: 検索ソースに含まれ、絞り込みが無いか検索指定のみで、Suggest が有効、非プライベート、検索モードでなく、入力が末尾の空白を除いて 2 文字以上のとき起動する。
- 触るとき: Suggest を問い合わせる入力条件(文字数、プライベート、検索モード)を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`, `queryContext.searchString.trimStart()`, `queryContext.sources.includes()`, `trimmedSearchString.trimEnd()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.isPrivate`, `queryContext.restrictSource`, `this._trimmedSearchString`, `trimmedSearchString.trimEnd().length`

## UrlbarProviderQuickSuggest.startQuery()
- 位置: async L97-141
- 役割: 有効な全バックエンドに問い合わせ、結果を集めてフィルタ・並べ替えし、maxResults の残数が尽きるまで結果化して追加する。
- 触るとき: 提案の問い合わせ、表示件数の上限(表示専用の結果を除く)、クエリ切り替え時の打ち切りを変えるとき。
- 呼び出し先: `Promise.all()`, `backend.query()`, `lazy.QuickSuggest.enabledBackends.map()`, `this.#filterAndSortSuggestions()`, `this.#makeResult()`, `values.flat()`
- 条件付き依存: `if (result)` → `this.#canAddResult()`
- 条件付き依存: `if (canAdd)` → `addCallback()`
- 参照: `queryContext.maxResults`, `result.isHiddenExposure`, `this._trimmedSearchString`, `this.queryInstance`

## UrlbarProviderQuickSuggest.#filterAndSortSuggestions()
- 位置: async L143-218
- 役割: source と provider が無い提案を捨て、スコアを補い、乱数や関連度でのランキングと scoreMap での上書きを適用する。機能ごとの filterSuggestions を通し、スコア降順・元の順で並べる。
- 触るとき: 提案の順位付けやスコア上書き(quickSuggestScoreMap)の挙動を変えるとき。
- 呼び出し先: `Promise.all()`, `Promise.resolve()`, `[...suggestionsByFeature].map()`, `feature.filterSuggestions()`, `featureSuggestions.push()`, `filteredSuggestions.sort()`, `indexesBySuggestion.get()`, `indexesBySuggestion.set()`, `isNaN()`, `lazy.QuickSuggest.getFeatureBySource()`, `lazy.UrlbarPrefs.get()`, `requiredKeys.every()`, `suggestionsByFeature.get()`, `this.#applyRanking()`
- 条件付き依存: `if (!requiredKeys.every(key => suggestion[key]))` → `this.logger.error()`
- 条件付き依存: `if (scoreMap)` → `this.#getSuggestionTelemetryType()`
- 条件付き依存: `if (scoreMap)` → `scoreMap.hasOwnProperty()`
- 条件付き依存: `if (scoreMap.hasOwnProperty(telemetryType))` → `parseFloat()`
- 条件付き依存: `if (scoreMap.hasOwnProperty(telemetryType))` → `isNaN()`
- 条件付き依存: `if (!featureSuggestions)` → `suggestionsByFeature.set()`
- 参照: `a.score`, `b.score`, `suggestion.score`, `suggestions.length`

## UrlbarProviderQuickSuggest.onImpression()
- 位置: L227-252
- 役割: 表示された結果を機能ごとにまとめ、各機能の onImpression へ通知する。
- 触るとき: 表示回数の記録(機能側)を追加・変更するとき。
- 呼び出し先: `feature.onImpression()`, `lazy.QuickSuggest.getFeatureByResult()`, `resultsAndIndexes.reduce()`
- 条件付き依存: `if (feature)` → `memo.get()`
- 条件付き依存: `if (!featureResults)` → `memo.set()`
- 条件付き依存: `if (feature)` → `featureResults.push()`

## UrlbarProviderQuickSuggest.onEngagement()
- 位置: L259-282
- 役割: 結果に機能があればその onEngagement へ委譲する。機能が無ければ、削除が選ばれたとき結果を Suggest の削除として記録し、一覧から消す。
- 触るとき: 提案を選んだ時や削除した時の後処理を変えるとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`
- 条件付き依存: `if (feature)` → `feature.onEngagement()`
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `lazy.QuickSuggest.dismissResult()`
- 条件付き依存: `if (details.selType == "dismiss" && result.payload.isBlockable)` → `controller.removeResult()`
- 参照: `details.selType`, `result.payload.isBlockable`, `this._trimmedSearchString`

## UrlbarProviderQuickSuggest.onSearchSessionEnd()
- 位置: L289-293
- 役割: 有効な各バックエンドへ検索セッション終了を通知する。
- 触るとき: 検索セッション終了時にバックエンドの後処理を足すとき。
- 呼び出し先: `backend.onSearchSessionEnd()`
- 参照: `lazy.QuickSuggest.enabledBackends`

## UrlbarProviderQuickSuggest.getViewTemplate()
- 位置: L301-305
- 役割: 結果の機能が表示テンプレートを持てばそれを返す(動的結果のみで使われる)。
- 触るとき: 機能ごとの Suggest 表示構造を確認するとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.getFeatureByResult(result)?.getViewTemplate()`

## UrlbarProviderQuickSuggest.getViewUpdate()
- 位置: L314-319
- 役割: 結果の機能が表示更新を返せばそれを返す(動的結果のみで使われる)。
- 触るとき: 機能ごとの表示更新内容を確認するとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.getFeatureByResult(result)?.getViewUpdate()`

## UrlbarProviderQuickSuggest.getResultCommands()
- 位置: L330-334
- 役割: 結果の機能が持つ結果メニューのコマンドをそのまま返す。
- 触るとき: Suggest 結果のメニュー項目を機能ごとに変えるとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.getFeatureByResult(result)?.getResultCommands()`

## UrlbarProviderQuickSuggest.#getSuggestionTelemetryType()
- 位置: L349-355
- 役割: 機能があればその telemetry type を返し、無ければ Merino の provider 名を返す。
- 触るとき: テレメトリの種別名を追加・変更するとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureBySource()`
- 条件付き依存: `if (feature)` → `feature.getSuggestionTelemetryType()`
- 参照: `suggestion.provider`

## UrlbarProviderQuickSuggest.#makeResult()
- 位置: async L357-466
- 役割: 機能(または Merino の top_picks)から結果を作り、source、provider、スポンサー判定、テレメトリ種別、アイコン、削除用キーを設定する。提案の位置(suggestedIndex)も決める。
- 触るとき: 提案の結果に載るプロパティや、スポンサー提案の表示位置(quickSuggestNonSponsoredIndex や quickSuggestSponsoredIndex)を変えるとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureBySource()`, `result.payload.hasOwnProperty()`, `this.#getSuggestionTelemetryType()`
- 条件付き依存: `if (!feature)` → `this.#makeUnmanagedResult()`
- 条件付き依存: `if (feature.isEnabled)` → `feature.makeResult()`
- 条件付き依存: `if (!result.payload.hasOwnProperty("isSponsored"))` → `feature?.isSuggestionSponsored()`
- 条件付き依存: `if (result.payload.icon)` → `UrlbarUtils.getRemoteImageUrl()`
- 条件付き依存: `if (!result.payload.isSponsored)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `this.queryInstance .getProvider("UrlbarProviderSearchSuggestions") ?.isActive()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `this.queryInstance .getProvider()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `lazy.UrlbarSearchUtils.getDefaultEngine( queryContext.isPrivate ).supportsResponseType()`
- 条件付き依存: `if (!(!result.payload.isSponsored))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("showSearchSuggestionsFirst") && (await this.queryInstance .getProvider("UrlbarProviderSearchSuggestions") ?.isActive(queryContext, thi...)` → `lazy.UrlbarPrefs.get()`
- 参照: `feature.isEnabled`, `lazy.SearchUtils.URL_TYPE.SUGGEST_JSON`, `lazy.UrlbarShared.TOP_PICK_ICON_SIZE`, `queryContext.isPrivate`, `result.hasSuggestedIndex`, `result.isBestMatch`, `result.isRichSuggestion`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.dismissalKey`, `result.payload.icon`, `result.payload.iconBlob`, `result.payload.isSponsored`, `result.payload.provider`, `result.payload.source`, `result.payload.suggestionObject`, `result.payload.suggestionType`, `result.payload.telemetryType`, `result.richSuggestionIconSize`, `result.suggestedIndex`, `suggestion.dismissal_key`, `suggestion.icon`, `suggestion.icon_blob`, `suggestion.provider`, `suggestion.source`, `suggestion.suggestionType`, `this._trimmedSearchString`, `this.queryInstance.controller`

## UrlbarProviderQuickSuggest.#makeUnmanagedResult()
- 位置: L484-524
- 役割: 機能を持たない Merino の top_picks 提案だけを URL 結果にする。それ以外は null を返す。
- 触るとき: 機能に属さない Merino の提案をどう表示するか変えるとき。
- 条件付き依存: `if (suggestion.full_keyword)` → `lazy.QuickSuggest.getFullKeywordTitleAndHighlights()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `payload.shouldShowUrl`, `payload.title`, `queryContext.tokens`, `suggestion.full_keyword`, `suggestion.is_sponsored`, `suggestion.is_top_pick`, `suggestion.original_url`, `suggestion.provider`, `suggestion.source`, `suggestion.title`, `suggestion.url`

## UrlbarProviderQuickSuggest.cancelQuery()
- 位置: L529-533
- 役割: 有効な各バックエンドのクエリを取り消す。
- 触るとき: 入力が変わったときに提案の問い合わせを止める挙動を調べるとき。
- 呼び出し先: `backend.cancelQuery()`
- 参照: `lazy.QuickSuggest.enabledBackends`

## UrlbarProviderQuickSuggest.#applyRanking()
- 位置: async L541-563
- 役割: quickSuggestRankingMode が random なら乱数、interest なら関連度でスコアを更新し、default では何もしない。
- 触るとき: ランキングモードの扱いや追加のモードを足すとき。
- 呼び出し先: `Math.random()`, `lazy.UrlbarPrefs.get()`, `suggestion.score.toFixed()`, `this.#updateScoreByRelevance()`, `this.logger.debug()`
- 参照: `suggestion.score`

## UrlbarProviderQuickSuggest.#updateScoreByRelevance()
- 位置: async L574-594
- 役割: 提案のカテゴリから ContentRelevancyManager でスコアを取り、既存スコアとの平均を新しいスコアにする。失敗時は元のスコアを残す。
- 触るとき: 関連度に基づく提案の順位付けの計算式を変えるとき。
- 呼び出し先: `Glean.suggestRelevance.outcome[ suggestion.score >= oldScore ? "boosted" : "decreased" ].add()`, `Glean.suggestRelevance.status.failure.add()`, `Glean.suggestRelevance.status.success.add()`, `lazy.ContentRelevancyManager.score()`, `this.logger.error()`
- 参照: `Glean.suggestRelevance.outcome`, `suggestion.categories`, `suggestion.categories?.length`, `suggestion.score`

## UrlbarProviderQuickSuggest.#canAddResult()
- 位置: async L605-635
- 役割: 機能に属さない結果は suggest.quicksuggest.all と sponsored の設定で可否を決め、削除済みの結果は追加しない。
- 触るとき: スポンサー提案や全 Suggest の表示設定が効かない問題を調べるとき。
- 呼び出し先: `lazy.QuickSuggest.getFeatureByResult()`, `lazy.QuickSuggest.isResultDismissed()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (await lazy.QuickSuggest.isResultDismissed(result))` → `this.logger.debug()`
- 参照: `result.payload.isSponsored`

## UrlbarProviderQuickSuggest._test_applyRanking()
- 位置: async L637-639
- 役割: テスト用に #applyRanking を外から呼べるようにする。
- 触るとき: ランキング処理を単体テストするときのみ。
- 呼び出し先: `this.#applyRanking()`
