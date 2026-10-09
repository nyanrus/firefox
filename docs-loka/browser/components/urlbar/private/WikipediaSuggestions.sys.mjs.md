# browser/components/urlbar/private/WikipediaSuggestions.sys.mjs

source: browser/components/urlbar/private/WikipediaSuggestions.sys.mjs
source-hash: a2ccdce00c10b64e88f1bc25172b373aee65b1bf
lines: 110

## <module>
- 役割: Wikipedia の提案を URL 結果として作る。オフライン(Rust)とオンライン(Merino)の両方を扱い、削除操作を受け持つ。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## WikipediaSuggestions.enablingPreferences()
- 位置: L20-26
- 役割: 有効判定に使う pref として wikipediaFeatureGate、suggest.wikipedia、suggest.quicksuggest.all を返す。
- 触るとき: Wikipedia 提案が出ないときにどの pref が条件になっているか調べるとき。

## WikipediaSuggestions.primaryUserControlledPreferences()
- 位置: L28-30
- 役割: 利用者が設定画面で操作する pref として suggest.wikipedia を返す。
- 触るとき: 設定画面の Wikipedia の項目を見直すとき。

## WikipediaSuggestions.merinoProvider()
- 位置: L32-34
- 役割: Merino の provider 名 'wikipedia' を返す。
- 触るとき: Merino から来る Wikipedia の結果を確かめるとき。

## WikipediaSuggestions.rustSuggestionType()
- 位置: L36-38
- 役割: Rust の提案種別名 'Wikipedia' を返す。
- 触るとき: Rust backend の提案種別と突き合わせるとき。

## WikipediaSuggestions.isSuggestionSponsored()
- 位置: L40-42
- 役割: 常に false を返し、Wikipedia 提案はスポンサー扱いにしない。
- 触るとき: Wikipedia 提案に広告の扱いを付けるかを検討するとき。

## WikipediaSuggestions.getSuggestionTelemetryType()
- 位置: L44-48
- 役割: Merino の提案は 'wikipedia'、それ以外(Rust)は 'adm_nonsponsored' を返す。旧来のオンライン提案のテレメトリ種別を引き継いでいる。
- 触るとき: Wikipedia のテレメトリ種別の集計がずれるときに確かめるとき。
- 参照: `suggestion.source`

## WikipediaSuggestions.makeResult()
- 位置: L50-66
- 役割: URL 結果を作る。タイトルは fullKeyword か full_keyword を使い、サブタイトルに提案の title を入れる。アイコンの大きさは 16 にする。
- 触るとき: Wikipedia の結果の見た目や、タイトルに使う値を変えるとき。Rust は camelCase、Merino は snake_case の名前を使う点に注意する。
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `suggestion.fullKeyword`, `suggestion.full_keyword`, `suggestion.title`, `suggestion.url`

## WikipediaSuggestions.getResultCommands()
- 位置: L74-90
- 役割: 結果メニューに「削除」、区切り、「管理」を返す。
- 触るとき: Wikipedia の結果メニューの項目を変えるとき。

## WikipediaSuggestions.onEngagement()
- 位置: L98-108
- 役割: 選ばれた操作が dismiss のときだけ、提案を除外して結果を削除する。「管理」は UrlbarInput が扱うので何もしない。
- 触るとき: 削除操作が効かない、または削除後に再び出るかを追うとき。
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.QuickSuggest.dismissResult()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `details.selType`
