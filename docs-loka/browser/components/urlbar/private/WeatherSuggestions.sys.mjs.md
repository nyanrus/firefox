# browser/components/urlbar/private/WeatherSuggestions.sys.mjs

source: browser/components/urlbar/private/WeatherSuggestions.sys.mjs
source-hash: f78d312e18e520455aa645ff7858919d46398916
lines: 594

## <module>
- 役割: 天気提案を扱う SuggestProvider。Rust で都市と天気の意図を判定し、Merino から天気予報を取得して urlbar に表示する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WeatherSuggestions.constructor()
- 位置: L141-143
- 役割: 基底の SuggestProvider の初期化だけを行う。
- 触るとき: コンストラクタに初期化処理を追加するとき。
- 呼び出し先: `super()`

## WeatherSuggestions.enablingPreferences()
- 位置: L145-152
- 役割: 有効判定に使う pref として weatherFeatureGate、suggest.weather、suggest.quicksuggest.all、suggest.quicksuggest.sponsored を返す。
- 触るとき: 天気提案が出ないときに、どの pref が条件になっているかを確かめるとき。

## WeatherSuggestions.primaryUserControlledPreferences()
- 位置: L154-156
- 役割: 利用者が設定画面で操作する pref として suggest.weather を返す。
- 触るとき: 設定画面の天気の項目を見直すとき。

## WeatherSuggestions.rustSuggestionType()
- 位置: L158-160
- 役割: Rust の提案種別名 'Weather' を返す。
- 触るとき: Rust 側の天気提案と突き合わせるとき。

## WeatherSuggestions.showLessFrequentlyCount()
- 位置: L162-165
- 役割: weather.showLessFrequentlyCount の pref を読み、0 未満にならないよう丸めて返す。
- 触るとき: 「少なく表示」の回数が反映されないときに確かめるとき。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## WeatherSuggestions.canShowLessFrequently()
- 位置: L167-173
- 役割: 上限を weatherShowLessFrequentlyCap、無ければ config の showLessFrequentlyCap、どちらも無ければ 0 から求め、上限が 0 か回数が上限未満なら true を返す。
- 触るとき: 天気の「少なく表示」の上限の扱いを変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## WeatherSuggestions.isSuggestionSponsored()
- 位置: L175-177
- 役割: 常に true を返す。天気提案はスポンサー扱い。
- 触るとき: 天気提案のスポンサー表示や非表示の条件を変えるとき。

## WeatherSuggestions.getSuggestionTelemetryType()
- 位置: L179-181
- 役割: 常に 'weather' を返す。
- 触るとき: 天気のテレメトリ種別を変えるとき。

## WeatherSuggestions.enable()
- 位置: L183-187
- 役割: 無効化されたら Merino クライアントの参照を null にする。
- 触るとき: 天気を無効にしたあとに Merino の参照が残らないか確かめるとき。
- 参照: `this.#merino`

## WeatherSuggestions.filterSuggestions()
- 位置: async L189-207
- 役割: 1件以下ならそのまま返す。複数の都市がマッチしたときは GeolocationUtils.best で最も適したものを1件選んで返す。
- 触るとき: 同じ語句で複数の都市がマッチしたときの選び方を変えるとき。
- 呼び出し先: `lazy.GeolocationUtils.best()`, `s.city?.adminDivisionCodes.get()`
- 参照: `s.city?.countryCode`, `s.city?.latitude`, `s.city?.longitude`, `s.city?.population`, `suggestions.length`

## WeatherSuggestions.makeResult()
- 位置: async L209-257
- 役割: 入力が最小長に満たなければ null。Rust の提案の都市で Merino から天気予報を取得し、無ければ null。weatherUiTreatment が 1 か 2 なら動的結果、それ以外は URL 結果を作る。
- 触るとき: 天気の結果の作り方や、表示の種類による分岐を変えるとき。
- 呼び出し先: `String()`, `lazy.UrlbarPrefs.get()`, `this.#fetchMerinoSuggestion()`, `this.#getTitleL10n()`, `unit.toUpperCase()`
- 条件付き依存: `if (treatment == 1 || treatment == 2)` → `this.#makeDynamicResult()`
- 参照: `Services.locale.regionalPrefsLocales`, `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `merinoSuggestion.current_conditions.icon_id`, `merinoSuggestion.current_conditions.temperature`, `merinoSuggestion.url`, `searchString.length`, `suggestion.city`, `this.#minKeywordLength`, `titleL10n.args`, `titleL10n.id`
- XPCOM: `Services.locale`

## WeatherSuggestions.#makeDynamicResult()
- 位置: L259-281
- 役割: 動的な天気結果を作る。都市、地域、単位、気温、現在の状況、予報、最高・最低気温、ヘルプ URL を payload に入れる。
- 触るとき: 動的表示の天気の項目を増やすとき。
- 参照: `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `suggestion.city_name`, `suggestion.current_conditions.icon_id`, `suggestion.current_conditions.summary`, `suggestion.current_conditions.temperature`, `suggestion.forecast.high`, `suggestion.forecast.low`, `suggestion.forecast.summary`, `suggestion.region_code`, `suggestion.url`

## WeatherSuggestions.getViewTemplate()
- 位置: L283-285
- 役割: 固定の天気の表示テンプレートを返す。
- 触るとき: 天気の表示の要素の構造を変えるとき。

## WeatherSuggestions.getViewUpdate()
- 位置: L287-355
- 役割: payload の値を、現在の気温、タイトル、要約、最高・最低、提供元の表示の更新内容に変換する。weatherUiTreatment が 1 のときは要約を現在の状況だけにする。
- 触るとき: 天気の表示文言や気温の単位表示を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `result.payload.temperatureUnit.toUpperCase()`
- 参照: `result.payload.city`, `result.payload.currentConditions`, `result.payload.forecast`, `result.payload.high`, `result.payload.iconId`, `result.payload.low`, `result.payload.region`, `result.payload.temperature`, `result.payload.url`

## WeatherSuggestions.getResultCommands()
- 位置: L363-406
- 役割: 結果メニューに「位置が不正確」、上限内なら「少なく表示」、「表示しない」、区切り、「管理」、「ヘルプ」を返す。
- 触るとき: 天気の結果メニューの項目や並びを変えるとき。
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## WeatherSuggestions.onEngagement()
- 位置: L414-448
- 役割: ヘルプと管理は UrlbarInput に任せる。dismiss は suggest.weather を false にして結果を削除する。位置の不正確さは承認のフィードバックだけを出す。少なく表示は回数を増やし、最小長を入力長+1 に設定する。
- 触るとき: 天気の操作のあとに pref や結果がどう変わるかを追うとき。
- 呼び出し先: `controller.removeResult()`, `controller.view.acknowledgeFeedback()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`, `this.logger.info()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.HELP`, `RESULT_MENU_COMMAND.INACCURATE_LOCATION`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `result.id`, `searchString.length`

## WeatherSuggestions.incrementShowLessFrequentlyCount()
- 位置: L450-457
- 役割: 上限内であれば「少なく表示」の回数を1増やして pref に保存する。
- 触るとき: 回数の増やし方や上限判定を見直すとき。
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## WeatherSuggestions.#config()
- 位置: L459-465
- 役割: Rust バックエンドが有効なら、この種別の設定を取得して返す。取得できなければ空オブジェクトを返す。
- 触るとき: Rust から取る天気の設定値(最小キーワード長など)を扱うとき。
- 呼び出し先: `rustBackend.getConfigForSuggestionType()`
- 参照: `lazy.QuickSuggest`, `rustBackend.isEnabled`, `this.rustSuggestionType`

## WeatherSuggestions.#minKeywordLength()
- 位置: L467-486
- 役割: 利用者が pref を設定済みなら pref の値を使う。無ければ Nimbus の weatherKeywordsMinimumLength、それも null なら設定の minKeywordLength を使い、0 以上に丸めて返す。
- 触るとき: 最小キーワード長の優先順位(利用者の設定、Nimbus、config)を変えるとき。
- 呼び出し先: `Math.max()`, `Services.prefs.prefHasUserValue()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( !Services.prefs.prefHasUserValue( "browser.urlbar.weather.minKeywordLength" ) )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(nimbusValue !== null))` → `isNaN()`
- 参照: `this.#config.minKeywordLength`
- XPCOM: `Services.prefs`

## WeatherSuggestions.#fetchMerinoSuggestion()
- 位置: async L488-516
- 役割: Merino クライアントを必要なら作り、都市の情報をもとに天気予報を取得する。タイムアウトは #timeoutMs、キャッシュ期間は1分。取得中に新しい問い合わせが始まっていれば null を返し、古い応答を捨てる。
- 触るとき: 天気の取得、古い応答の破棄、タイムアウトの扱いを調べるとき。
- 呼び出し先: `[...cityGeoname.adminDivisionCodes.entries()] .sort()`, `[...cityGeoname.adminDivisionCodes.entries()] .sort(([level1, _admin1], [level2, _admin2]) => level1 - level2) .map()`, `cityGeoname.adminDivisionCodes.entries()`, `merino.fetchWeatherReport()`
- 参照: `cityGeoname?.adminDivisionCodes`, `cityGeoname?.countryCode`, `cityGeoname?.name`, `lazy.MerinoClient`, `this.#fetchInstance`, `this.#merino`, `this.#timeoutMs`, `this.constructor.name`

## WeatherSuggestions.#getTitleL10n()
- 位置: async L518-580
- 役割: 都市名、地域(米国とカナダは略称)、国(自国と違うときだけ)から、タイトルの Fluent ID と引数を決める。地域と国の有無に応じて3種類の ID を使い分ける。
- 触るとき: 天気のタイトルの表記を変えるとき。
- 条件付き依存: `if (!(!cityGeoname))` → `lazy.QuickSuggest.rustBackend.fetchGeonameAlternates()`
- 条件付き依存: `if (!(!cityGeoname))` → `NORTH_AMERICA_COUNTRY_CODES.has()`
- 条件付き依存: `if (NORTH_AMERICA_COUNTRY_CODES.has(cityGeoname.countryCode))` → `alts.adminDivisions.get()`
- 参照: `alts.adminDivisions.get(1)?.abbreviation`, `alts.adminDivisions.get(1)?.localized`, `alts.adminDivisions.get(1)?.primary`, `alts.country?.localized`, `alts.country?.primary`, `alts.geoname.localized`, `alts.geoname.primary`, `cityGeoname.countryCode`, `lazy.Region.home`, `merinoSuggestion.city_name`, `merinoSuggestion.region_code`

## WeatherSuggestions._test_merino()
- 位置: L582-584
- 役割: テスト用に Merino クライアントを返す getter。
- 触るとき: テストで Merino クライアントの状態を確かめるとき。
- 参照: `this.#merino`

## WeatherSuggestions._test_setTimeoutMs()
- 位置: L586-588
- 役割: テスト用にタイムアウトを変える。負の値なら既定の 5000ms に戻す。
- 触るとき: テストでタイムアウトを短くするとき。
- 参照: `this.#timeoutMs`
