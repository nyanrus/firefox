# browser/components/urlbar/private/ImportantDatesSuggestions.sys.mjs

source: browser/components/urlbar/private/ImportantDatesSuggestions.sys.mjs
source-hash: ccdb697be1875535513b9937f276c4e3b1ee76d3
lines: 262

## <module>
- 役割: 重要な日付(イベント)の候補を、設定や Rust の候補種別に従って表示用の結果にする提供元。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ImportantDatesSuggestions.enablingPreferences()
- 位置: L24-26
- 役割: この機能を有効にする設定として、feature gate と suggest.importantDates を返す。
- 触るとき: 重要な日付の候補が出ない原因が設定のどちらで止まっているかを調べるとき、または有効化条件を変えるときに見る。

## ImportantDatesSuggestions.primaryUserControlledPreferences()
- 位置: L28-30
- 役割: 利用者が直接切り替える設定として "suggest.importantDates" を返す。
- 触るとき: 利用者向けの設定画面に出す項目を変えるとき、または候補の表示を止める設定の対象を確かめるときに見る。

## ImportantDatesSuggestions.rustSuggestionType()
- 位置: L32-34
- 役割: Rust 側の候補種別として "Dynamic" を返す。
- 触るとき: 重要な日付の候補を Rust の動的候補として受け取る経路を調べるとき、または候補種別の対応を変えるときに見る。

## ImportantDatesSuggestions.dynamicRustSuggestionTypes()
- 位置: L36-38
- 役割: この提供元が扱う動的候補の種類として "important_dates" だけを返す。
- 触るとき: 重要な日付として扱う動的候補の種類名を変えるとき、または種類名が Rust 側の名前と一致しているかを確かめるときに見る。

## ImportantDatesSuggestions.isSuggestionSponsored()
- 位置: L40-45
- 役割: payload に isSponsored があればその値を、無ければ false を返す。
- 触るとき: 重要な日付の候補をスポンサー扱いする条件を変えるとき、またはスポンサー表示が出ない理由を調べるときに見る。
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.isSponsored`

## ImportantDatesSuggestions.getSuggestionTelemetryType()
- 位置: L47-52
- 役割: payload の telemetryType があればそれを、無ければ動的候補の先頭の種類名を返す。
- 触るとき: 重要な日付の計測上の種類名を変えるとき、または計測で候補が正しく集計されない原因を調べるときに見る。
- 呼び出し先: `suggestion.data?.result?.payload?.hasOwnProperty()`
- 参照: `suggestion.data.result.payload.telemetryType`, `this.dynamicRustSuggestionTypes`

## ImportantDatesSuggestions.makeResult()
- 位置: async L54-64
- 役割: payload が無い、またはオブジェクトでなければ警告を出して null を返し、そうでなければ日付の結果を作る。
- 触るとき: Remote Settings から届いた候補が表示されない理由を調べるとき、または payload の形式を変えるときに見る。
- 呼び出し先: `this.#makeDateResult()`
- 条件付き依存: `if ( !suggestion.data?.result?.payload || typeof suggestion.data.result.payload != "object" )` → `this.logger.warn()`
- 参照: `suggestion.data.result.payload`, `suggestion.data?.result?.payload`

## ImportantDatesSuggestions.#formatDateOrRange()
- 位置: L86-106
- 役割: 単一日付は曜日付きの長い形式、期間は開始と終了の範囲形式で、アプリの言語に合わせた日付文字列にする。
- 触るとき: 日付の表示形式(曜日の有無や範囲の書き方)を変えるとき、または表示言語での日付の出方を確かめるときに見る。
- 呼び出し先: `Array.isArray()`, `format.format()`
- 条件付き依存: `if (Array.isArray(dateStr))` → `format.formatRange()`
- 参照: `Intl.DateTimeFormat`, `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## ImportantDatesSuggestions.#formatDateCountdown()
- 位置: L120-159
- 役割: 残り日数に応じた l10n 情報(期間の開始まで、進行中、終了日、単日の残り日数、当日)を返す。過去の日付は例外を投げる。
- 触るとき: カウントダウンの文言の出し分けを変えるとき、または過去の日付で例外が出る原因を調べるときに見る。
- 呼び出し先: `Array.isArray()`, `this.#getDaysUntil()`
- 条件付き依存: `if (Array.isArray(dateStr))` → `this.#getDaysUntil()`

## ImportantDatesSuggestions.#getDaysUntil()
- 位置: L169-177
- 役割: 今日の 0 時から指定日の 0 時までの日数を、ミリ秒を 1 日で割って丸めて返す。
- 触るとき: 残り日数の計算を変えるとき、または夏時間の切り替えで日数が 1 日ずれる原因を調べるときに見る。
- 呼び出し先: `Math.round()`, `date.getTime()`, `now.getTime()`, `now.setHours()`

## ImportantDatesSuggestions.#makeDateResult()
- 位置: L189-236
- 役割: 今日以降に終わる最初の日付を選び、30 日より後なら説明を名前だけにし、30 日以内ならカウントダウンを付けた検索結果を作る。全て過去なら null を返す。
- 触るとき: 表示する日付の選び方や、カウントダウンへ切り替わる 30 日の境界を変えるとき、または候補が出ない理由を調べるときに見る。
- 呼び出し先: `Array.isArray()`, `lazy.UrlbarSearchUtils.getDefaultEngine()`, `payload.dates.find()`, `payload.name.toLowerCase()`, `this.#formatDateOrRange()`, `this.#getDaysUntil()`
- 条件付き依存: `if (!(daysUntilStart > SHOW_COUNTDOWN_THRESHOLD_DAYS))` → `this.#formatDateCountdown()`
- 参照: `lazy.QuickSuggest.HELP_URL`, `lazy.UrlbarResult`, `lazy.UrlbarSearchUtils.getDefaultEngine(queryContext.isPrivate) .name`, `lazy.UrlbarShared.HIGHLIGHT.ALL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `payload.name`, `queryContext.isPrivate`

## ImportantDatesSuggestions.onEngagement()
- 位置: L244-260
- 役割: "dismiss" で候補を非表示にして結果を削除し、"manage" は UrlbarInput に任せる。
- 触るとき: 重要な日付の結果メニューの操作を増やすとき、または「非表示」後に候補が消えない原因を調べるときに見る。
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`
- 参照: `details.selType`
