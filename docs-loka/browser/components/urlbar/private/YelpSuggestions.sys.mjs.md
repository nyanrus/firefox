# browser/components/urlbar/private/YelpSuggestions.sys.mjs

source: browser/components/urlbar/private/YelpSuggestions.sys.mjs
source-hash: 5474ec145da4fac55d6179f17a03d575fbe971f6
lines: 586

## <module>
- 役割: Yelp 提案(都市・地域つきの店探し候補)を検索結果に変える提供元モジュール。Rust 提案と ML 提案の両方を扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## YelpSuggestions.enablingPreferences()
- 位置: L39-46
- 役割: Yelp 提案を有効にする条件の pref 名一覧を返す。
- 触るとき: Yelp 提案が出ない・止まらない原因を pref から追うとき、有効化条件に pref を足す・外すとき。

## YelpSuggestions.primaryUserControlledPreferences()
- 位置: L48-50
- 役割: ユーザーが直接切り替える pref(suggest.yelp)だけを返す。
- 触るとき: 設定画面の Yelp の on/off 項目を変えるとき。

## YelpSuggestions.rustSuggestionType()
- 位置: L52-54
- 役割: Rust バックエンドで Yelp 提案を指す種別名 'Yelp' を返す。
- 触るとき: Rust 側の提案種別名が変わり、取得対象の指定を合わせる必要があるとき。

## YelpSuggestions.mlIntent()
- 位置: L56-58
- 役割: ML 意図判定で Yelp を表すラベル 'yelp_intent' を返す。
- 触るとき: ML 意図判定のラベル名を変えるとき。

## YelpSuggestions.isMlIntentEnabled()
- 位置: L60-65
- 役割: pref yelpMlEnabled を読み、ML 提案を使うかを返す。
- 触るとき: ML 提案の切り替え条件を変えるとき。ML 有効時も Rust 提案は取得し続ける理由がコメントにあるので、取得の止め方を変えるときに読む。
- 呼び出し先: `lazy.UrlbarPrefs.get()`

## YelpSuggestions.showLessFrequentlyCount()
- 位置: L67-70
- 役割: 「表示を減らす」が押された回数を pref から読み、0 以上に丸める。
- 触るとき: 表示回数の保存先 pref や、上限判定に使う値を変えるとき。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## YelpSuggestions.canShowLessFrequently()
- 位置: L72-78
- 役割: 上限(pref か Rust の showLessFrequentlyCap)に達していないかを返す。上限が 0 なら常に true。
- 触るとき: 「表示を減らす」をメニューに出す条件を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## YelpSuggestions.isSuggestionSponsored()
- 位置: L80-82
- 役割: 常に true を返し、Yelp 提案をスポンサー扱いにする。
- 触るとき: Yelp 提案のスポンサー表示や表示ラベルの扱いを変えるとき。

## YelpSuggestions.getSuggestionTelemetryType()
- 位置: L84-86
- 役割: テレメトリで使う提案種別 'yelp' を返す。
- 触るとき: Yelp 提案のテレメトリ集計の種別名を変えるとき。

## YelpSuggestions.enable()
- 位置: L88-92
- 役割: 無効化されたときメタデータキャッシュを捨てる。
- 触るとき: 無効化後も古い ML 用キャッシュが使われる不具合を調べるとき。
- 参照: `this.#metadataCache`

## YelpSuggestions.filterSuggestions()
- 位置: async L94-135
- 役割: pref に応じて Rust か ML のどちらかの Yelp 提案を選び、URL と位置を正規化して 1 件返す。
- 触るとき: ML と Rust のどちらを出すかの判定、重複候補の選び方、非表示判定に使われる URL の形を変えるとき。ML 有効時は初回にキャッシュを作る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("yelpMlEnabled"))` → `suggestions.find()`
- 条件付き依存: `if (suggestion)` → `this.#normalizeRustSuggestion()`
- 条件付き依存: `if (!(!lazy.UrlbarPrefs.get("yelpMlEnabled")))` → `suggestions.find()`
- 条件付き依存: `if (!this.#metadataCache)` → `this.#makeMetadataCache()`
- 条件付き依存: `if (suggestion)` → `this.#normalizeMlSuggestion()`
- 参照: `s.source`, `this.#metadataCache`

## YelpSuggestions.makeResult()
- 位置: async L137-228
- 役割: 提案を URL 付きの検索結果に組み立て、位置情報・表示タイトル・表示位置を決める。
- 触るとき: 結果の表示文言、位置の補完、最短入力長による除外を変えるとき。都市・地域が見つからない場合や最短長未満の場合は null を返す。
- 呼び出し先: `[city, region].filter()`, `[city, region].filter(s => !!s).join()`, `lazy.UrlbarPrefs.get()`, `url.searchParams.set()`, `url.toString()`
- 条件付き依存: `if (!city && !region)` → `lazy.GeolocationUtils.geolocation()`
- 条件付き依存: `if (!(!city && !region))` → `this.#bestCityRegion()`
- 条件付き依存: `if (locationStr)` → `url.searchParams.set()`
- 条件付き依存: `if (!resultProperties.isBestMatch)` → `lazy.UrlbarPrefs.get()`
- 参照: `geo.city`, `geo.region_code`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `lazy.YelpSubjectType.SERVICE`, `match.city`, `match.region`, `payload.title`, `payload.titleL10n`, `resultProperties.isBestMatch`, `resultProperties.isSuggestedIndexRelativeToGroup`, `resultProperties.suggestedIndex`, `searchString.length`, `suggestion.hasLocationSign`, `suggestion.icon_blob`, `suggestion.locationParam`, `suggestion.subjectExactMatch`, `suggestion.subjectType`, `suggestion.title`, `suggestion.url`, `this.#minKeywordLength`, `this.showLessFrequentlyCount`

## YelpSuggestions.getResultCommands()
- 位置: L244-287
- 役割: 結果メニューの項目(位置の誤り報告、表示を減らす、非表示、管理、ヘルプ)を組み立てる。
- 触るとき: メニューの項目や並びを変えるとき。「表示を減らす」は上限に達していないときだけ入る。
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## YelpSuggestions.onEngagement()
- 位置: L295-332
- 役割: メニュー操作ごとに処理する。非表示は結果を消し、not_interested は suggest.yelp を false にし、表示を減らすは最短長を入力長+1 に上げる。
- 触るとき: メニュー操作後の動作(非表示、無効化、表示を減らす)を変えるとき。
- 呼び出し先: `controller.removeResult()`, `controller.view.acknowledgeFeedback()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `result.id`, `searchString.length`

## YelpSuggestions.incrementShowLessFrequentlyCount()
- 位置: L334-341
- 役割: 上限に達していなければ「表示を減らす」の回数を 1 増やす。
- 触るとき: 表示を減らす回数の数え方や上限の扱いを変えるとき。
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## YelpSuggestions.#minKeywordLength()
- 位置: L343-357
- 役割: 最短キーワード長を決める。ユーザーが値を変えた時か Nimbus 値が無い時は pref、それ以外は Nimbus 値を使い、0 以上に丸める。
- 触るとき: 最短長の既定値や Nimbus による上書きの優先順位を変えるとき。
- 呼び出し先: `Math.max()`, `Services.prefs.prefHasUserValue()`, `lazy.UrlbarPrefs.get()`
- XPCOM: `Services.prefs`

## YelpSuggestions.#normalizeRustSuggestion()
- 位置: L359-388
- 役割: Rust 提案の URL から位置パラメータを取り出して city に入れ、URL とタイトルから位置を取り除く。
- 触るとき: Rust 側の提案形式が変わり、位置の抽出規則を直すとき。
- 呼び出し先: `url.searchParams.get()`
- 条件付き依存: `if (loc)` → `url.searchParams.delete()`
- 条件付き依存: `if (loc)` → `url.toString()`
- 条件付き依存: `if (loc)` → `suggestion.title.endsWith()`
- 条件付き依存: `if (suggestion.title.endsWith(loc))` → `suggestion.title .substring(0, suggestion.title.length - loc.length) .trimEnd()`
- 条件付き依存: `if (suggestion.title.endsWith(loc))` → `suggestion.title .substring()`
- 参照: `loc.length`, `suggestion.city`, `suggestion.locationParam`, `suggestion.title`, `suggestion.title.length`, `suggestion.url`

## YelpSuggestions.#normalizeMlSuggestion()
- 位置: L390-413
- 役割: subject の無い ML 提案は捨て、残りは URL や score を補って Rust 提案と同じ形にする。
- 触るとき: ML 提案の形式を変えたり、位置だけの誤検出を除く条件を変えるとき。
- 呼び出し先: `url.searchParams.set()`, `url.toString()`
- 参照: `ml.location?.city`, `ml.location?.state`, `ml.subject`, `this.#metadataCache.findDesc`, `this.#metadataCache.findLoc`, `this.#metadataCache.iconBlob`, `this.#metadataCache.score`, `this.#metadataCache.urlOrigin`, `this.#metadataCache.urlPathname`, `url.pathname`

## YelpSuggestions.#makeMetadataCache()
- 位置: async L423-466
- 役割: ML 提案用のアイコン・URL・スコアを、Rust に固定クエリ 'coffee in atlanta' を投げて得た結果から作り、足りない項目は既定値で埋める。
- 触るとき: ML 提案に出るアイコンや URL を変えるとき。Rust から結果が無い場合は既定値だけになる。
- 呼び出し先: `Object.entries()`, `lazy.QuickSuggest.rustBackend.query()`, `this.logger.debug()`
- 条件付き依存: `if (!rs.length)` → `this.logger.debug()`
- 条件付き依存: `if (!(!rs.length))` → `findParamWithValue()`
- 参照: `rs.length`, `suggestion.icon_blob`, `suggestion.score`, `suggestion.url`, `url.origin`, `url.pathname`

## findParamWithValue()
- 位置: L436-441
- 役割: URL のクエリから、指定した値を持つパラメータ名を探す。
- 触るとき: Yelp の検索 URL のパラメータ名が変わり、説明や場所のパラメータを見つけ直す必要があるとき。
- 呼び出し先: `[...url.searchParams.entries()].find()`, `url.searchParams.entries()`

## YelpSuggestions.#bestCityRegion()
- 位置: async L493-558
- 役割: 入力された地域・都市を地名 DB で照合し、端末の位置に最も近い候補を返す。一致しなければ null。
- 触るとき: 都市・地域の判定を変えるとき。略語や空港コードを除く規則(NAME 以外は除外)もここにある。
- 呼び出し先: `regionMatches?.filter()`
- 条件付き依存: `if (region)` → `lazy.QuickSuggest.rustBackend.fetchGeonames()`
- 条件付き依存: `if (city)` → `lazy.QuickSuggest.rustBackend.fetchGeonames()`
- 条件付き依存: `if (city)` → `regionMatches?.map()`
- 条件付き依存: `if (city)` → `cityMatches.filter()`
- 条件付き依存: `if (city)` → `lazy.GeolocationUtils.best()`
- 条件付き依存: `if (city)` → `best.geoname.adminDivisionCodes.get()`
- 条件付き依存: `if (regionMatches?.length)` → `lazy.GeolocationUtils.best()`
- 参照: `best.geoname.name`, `cityMatches.length`, `lazy.GeonameMatchType.NAME`, `m.geoname`, `match.matchType`, `match.prefix`, `regionMatches.length`, `regionMatches?.length`

## YelpSuggestions._test_invalidateMetadataCache()
- 位置: L560-562
- 役割: テスト用にメタデータキャッシュを捨てる。
- 触るとき: テストで ML 用キャッシュの状態をリセットしたいとき。
- 参照: `this.#metadataCache`

## locationFromGeonameMatch()
- 位置: L577-585
- 役割: 地名の照合結果を、GeolocationUtils が使う位置情報(緯度・経度・国・地域・人口)に変換する。
- 触るとき: 最寄りの都市を選ぶのに使う情報を増減するとき。
- 呼び出し先: `match.geoname.adminDivisionCodes.get()`
- 参照: `match.geoname.countryCode`, `match.geoname.latitude`, `match.geoname.longitude`, `match.geoname.population`
