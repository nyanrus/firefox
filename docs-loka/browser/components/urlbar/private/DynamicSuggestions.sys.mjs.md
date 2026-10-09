# browser/components/urlbar/private/DynamicSuggestions.sys.mjs

source: browser/components/urlbar/private/DynamicSuggestions.sys.mjs
source-hash: 2487dd1027dcaf5755220dc22200b1759a15e5e7
lines: 163

## <module>
- 役割: quicksuggest.dynamicSuggestionTypes で定義された動的 Rust 候補の種類を管理し、候補を結果に変換する提供元。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## DynamicSuggestions.enablingPreferences()
- 位置: L31-33
- 役割: この機能を有効にする設定として "quicksuggest.dynamicSuggestionTypes" を返す。
- 触るとき: 動的候補の有効化条件に別の設定を加えるとき、または動的候補が出ない原因が設定の有無にあるか確かめるときに見る。

## DynamicSuggestions.shouldEnable()
- 位置: L35-37
- 役割: 動的候補の種類が 1 つ以上定義されているときに true を返し、機能を有効にするかを決める。
- 触るとき: 種類の設定が空でも機能を動かしたいとき、または種類を入れたのに機能が無効のままになるときに見る。
- 参照: `this.dynamicRustSuggestionTypes.length`

## DynamicSuggestions.rustSuggestionType()
- 位置: L39-41
- 役割: Rust 側の候補種別として "Dynamic" を返す。
- 触るとき: Rust 側の候補種別との対応を変えるとき、または動的候補を Rust から受け取る経路を調べるときに見る。

## DynamicSuggestions.dynamicRustSuggestionTypes()
- 位置: L43-46
- 役割: 設定の "quicksuggest.dynamicSuggestionTypes" を Set から配列にして、動的候補の種類一覧を返す。
- 触るとき: 動的候補の種類の集め方を変えるとき、または他の機能が種類を追加する仕組みに組み込むときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`

## DynamicSuggestions.isSuggestionSponsored()
- 位置: L48-50
- 役割: 候補の payload の isSponsored が真かどうかを返す。
- 触るとき: 動的候補をスポンサー扱いする判定を変えるとき、またはスポンサー表示が出ない原因を調べるときに見る。
- 参照: `suggestion.data?.result?.payload?.isSponsored`

## DynamicSuggestions.getSuggestionTelemetryType()
- 位置: L52-60
- 役割: payload の telemetryType があればそれを、隠し露出の候補なら "exposure"、それ以外は候補の suggestionType を返す。
- 触るとき: 動的候補の計測上の種類名を変えるとき、または露出候補がどの種類で集計されるかを確かめるときに見る。
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.telemetryType`, `suggestion.data?.result?.isHiddenExposure`, `suggestion.suggestionType`

## DynamicSuggestions.makeResult()
- 位置: L62-117
- 役割: 候補の data.result を検査し、隠し露出なら露出結果を作り、通常の候補なら表示可否を判定して URL 結果を組み立てる。
- 触るとき: 動的候補の表示条件(bypassSuggestAll、スポンサー、Suggest 全体の設定)を変えるとき、または候補が無視される理由を警告ログから調べるときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `result.hasOwnProperty()`
- 条件付き依存: `if (!data || typeof data != "object")` → `this.logger.warn()`
- 条件付き依存: `if (!result || typeof result != "object")` → `this.logger.warn()`
- 条件付き依存: `if (typeof result.payload != "object")` → `this.logger.warn()`
- 条件付き依存: `if (result.isHiddenExposure)` → `this.#makeExposureResult()`
- 参照: `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `payload.helpUrl`, `payload.isManageable`, `payload.isSponsored`, `result.bypassSuggestAll`, `result.isHiddenExposure`, `result.payload`, `resultProperties.payload`

## DynamicSuggestions.onEngagement()
- 位置: L125-141
- 役割: "dismiss" の選択で候補を非表示にして結果を削除し、"manage" は UrlbarInput に任せる。
- 触るとき: 候補の結果メニューで選べる操作を増やすとき、または「非表示」を押しても結果が消えない原因を調べるときに見る。
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`
- 参照: `details.selType`

## DynamicSuggestions.#makeExposureResult()
- 位置: L143-161
- 役割: 表示されない隠し露出用の動的結果を作り、露出計測を HIDDEN にして dynamicType を "exposure" にする。
- 触るとき: 露出候補の計測設定や dynamicType の値を変えるとき、または露出計測が記録されない原因を調べるときに見る。
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.EXPOSURE_TELEMETRY.HIDDEN`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`
