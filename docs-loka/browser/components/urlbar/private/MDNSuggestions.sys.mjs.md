# browser/components/urlbar/private/MDNSuggestions.sys.mjs

source: browser/components/urlbar/private/MDNSuggestions.sys.mjs
source-hash: 36946f67baaa02cc3dd409d015c85808a9407965
lines: 195

## <module>
- 役割: MDN(Web ドキュメント)の提案を urlbar の URL 結果として作り、結果メニューの操作と「少なく表示」の回数上限を管理する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## MDNSuggestions.enablingPreferences()
- 位置: L27-29
- 役割: MDN 提案を有効にする判定に使う pref 名を返す(mdn.featureGate、suggest.mdn、suggest.quicksuggest.all)。
- 触るとき: MDN 提案が出ない原因がどの pref で止まっているかを調べるとき、または有効条件を増やすとき。

## MDNSuggestions.primaryUserControlledPreferences()
- 位置: L31-33
- 役割: 利用者が設定画面から直接切り替える pref として suggest.mdn を返す。
- 触るとき: 設定画面に MDN の項目を出す条件を見直すとき。

## MDNSuggestions.merinoProvider()
- 位置: L35-37
- 役割: Merino の provider 名 'mdn' を返す。
- 触るとき: Merino から来た MDN 提案が別の種別として扱われる問題を調べるとき。

## MDNSuggestions.rustSuggestionType()
- 位置: L39-41
- 役割: Rust backend の提案種別名 'Mdn' を返す。
- 触るとき: Rust 側の提案種別と突き合わせるとき。

## MDNSuggestions.makeResult()
- 位置: async L43-86
- 役割: 機能が無効なら null を返す。「少なく表示」の上限内で入力が最小長に満たなければ null を返す。URL に utm パラメータを付けて URL 結果を作る。
- 触るとき: MDN の結果の見た目や計測用の URL パラメータを変えるとき、または MDN の結果が出ない理由を調べるとき。
- 呼び出し先: `url.searchParams.set()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_NETWORK`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `searchString.length`, `suggestion.description`, `suggestion.title`, `suggestion.url`, `this.#minKeywordLength`, `this.isEnabled`, `this.showLessFrequentlyCount`, `url.href`

## MDNSuggestions.getResultCommands()
- 位置: L94-130
- 役割: 結果メニューのコマンドを組み立てる。「少なく表示」は上限内のときだけ入れ、続けて「削除」「表示しない」、区切り、「管理」を入れる。
- 触るとき: 結果メニューの項目や並びを変えるとき、または上限に達して「少なく表示」が消える理由を確かめるとき。
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## MDNSuggestions.onEngagement()
- 位置: L138-166
- 役割: 選ばれたメニューを処理する。dismiss は結果を削除して確認文を出し、not_interested は suggest.mdn を false にし、show_less_frequently は最小キーワード長を入力長+1 に設定する。manage は UrlbarInput が扱うので何もしない。
- 触るとき: メニュー操作のあとに結果や pref がどう変わるかを追うとき。
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `searchString.length`

## MDNSuggestions.incrementShowLessFrequentlyCount()
- 位置: L168-175
- 役割: 上限内であれば「少なく表示」の回数を1増やして pref に保存する。
- 触るとき: 回数の数え方や上限の判定を変えるとき。
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## MDNSuggestions.showLessFrequentlyCount()
- 位置: L177-180
- 役割: pref の「少なく表示」回数を読み、0 未満にならないよう丸めて返す。pref が無ければ 0 とみなす。
- 触るとき: 回数が期待どおりに増えない、または上限判定の値がずれるときに確認するとき。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## MDNSuggestions.canShowLessFrequently()
- 位置: L182-188
- 役割: 上限を mdn 用の pref、無ければ config の showLessFrequentlyCap、どちらも無ければ 0 から求め、上限が 0 か回数が上限未満なら true を返す。
- 触るとき: 「少なく表示」を結果メニューに出し続けるかの条件を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## MDNSuggestions.#minKeywordLength()
- 位置: L190-193
- 役割: 最小キーワード長の pref を 0 以上に丸めて返す。
- 触るとき: 短い入力で MDN 提案が出る・出ないの境目を調べるとき。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`
