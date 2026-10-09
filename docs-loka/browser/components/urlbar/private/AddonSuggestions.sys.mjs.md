# browser/components/urlbar/private/AddonSuggestions.sys.mjs

source: browser/components/urlbar/private/AddonSuggestions.sys.mjs
source-hash: f40a1a58bb3e7b53254aeaa77d6739c5a197f166
lines: 215

## <module>
- 役割: アドオン(拡張機能)の推奨候補を作り、結果メニューやクリック後の処理を担う提供元。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AddonSuggestions.enablingPreferences()
- 位置: L33-35
- 役割: この機能を有効にする設定として、アドオン用の feature gate、suggest.addons、suggest.quicksuggest.all を返す。
- 触るとき: アドオン候補が出なくなる原因が設定のどれで無効化されているかを調べるとき、または有効化条件を変えるときに見る。

## AddonSuggestions.primaryUserControlledPreferences()
- 位置: L37-39
- 役割: 利用者が直接切り替える設定として "suggest.addons" を返す。
- 触るとき: 利用者向けの設定画面に出す項目を変えるとき、または候補の表示を止める設定の対象を確かめるときに見る。

## AddonSuggestions.merinoProvider()
- 位置: L41-43
- 役割: Merino に問い合わせるときのプロバイダ名 "amo" を返す。
- 触るとき: アドオン候補の取得元を変えるとき、または Merino 側のプロバイダ名と合っているか確かめるときに見る。

## AddonSuggestions.rustSuggestionType()
- 位置: L45-47
- 役割: Rust 側の候補種別として "Amo" を返す。
- 触るとき: Rust 側の候補種別との対応を変えるとき、または Rust から届いたアドオン候補を追うときに見る。

## AddonSuggestions.makeResult()
- 位置: async L49-103
- 役割: 機能が無効なら null を返す。表示回数が 1 以上で検索語が最小長に届かない場合や、アドオンが導入済みの場合も null を返す。それ以外は UTM パラメータを補って URL 結果を作る。
- 触るとき: アドオン候補の表示条件(導入済みの判定や最小キーワード長)を変えるとき、または候補が出ない理由を調べるときに見る。
- 呼び出し先: `Object.entries()`, `lazy.AddonManager.getAddonByID()`, `url.searchParams.has()`
- 条件付き依存: `if (!url.searchParams.has(key))` → `url.searchParams.set()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `searchString.length`, `suggestion.custom_details.amo`, `suggestion.description`, `suggestion.icon`, `suggestion.iconUrl`, `suggestion.source`, `suggestion.title`, `suggestion.url`, `this.#minKeywordLength`, `this.isEnabled`, `this.showLessFrequentlyCount`, `url.href`

## AddonSuggestions.getResultCommands()
- 位置: L111-147
- 役割: 結果メニューの項目(少なくなるよう表示、削除、興味なし、管理)を並べて返す。少なくなるよう表示は表示上限に達すると出さない。
- 触るとき: 結果メニューに項目を追加したり並び順を変えたりするとき、または表示回数の上限に達したときに項目が消える理由を調べるときに見る。
- 呼び出し先: `commands.push()`
- 条件付き依存: `if (this.canShowLessFrequently)` → `commands.push()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `this.canShowLessFrequently`

## AddonSuggestions.onEngagement()
- 位置: L155-186
- 役割: メニューの選択に応じて、候補の削除、設定の "suggest.addons" を false にする、表示回数の増加と最小キーワード長の更新を行う。
- 触るとき: メニューの各操作が何を保存するかを変えるとき、または「興味なし」や「少なくなるよう表示」の後の挙動を調べるときに見る。
- 呼び出し先: `controller.removeResult()`, `lazy.QuickSuggest.dismissResult()`, `lazy.UrlbarPrefs.set()`, `this.handleShowLessFrequently()`
- 参照: `RESULT_MENU_COMMAND.DISMISS`, `RESULT_MENU_COMMAND.MANAGE`, `RESULT_MENU_COMMAND.NOT_INTERESTED`, `RESULT_MENU_COMMAND.SHOW_LESS_FREQUENTLY`, `details.selType`, `searchString.length`

## AddonSuggestions.incrementShowLessFrequentlyCount()
- 位置: L188-195
- 役割: 上限に達していなければ addons.showLessFrequentlyCount を 1 増やす。
- 触るとき: 少なくなるよう表示の回数の数え方を変えるとき、または表示回数が想定より早く増える原因を調べるときに見る。
- 条件付き依存: `if (this.canShowLessFrequently)` → `lazy.UrlbarPrefs.set()`
- 参照: `this.canShowLessFrequently`, `this.showLessFrequentlyCount`

## AddonSuggestions.showLessFrequentlyCount()
- 位置: L197-200
- 役割: addons.showLessFrequentlyCount の設定値を 0 以上に丸めて返す。
- 触るとき: 表示回数の上限判定に使われる値の扱いを変えるとき、または設定値が負になったときの挙動を確かめるときに見る。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`

## AddonSuggestions.canShowLessFrequently()
- 位置: L202-208
- 役割: 表示上限(設定値、無ければ Quick Suggest の設定値、どちらも無ければ 0)に達していないかを返す。上限 0 は無制限扱い。
- 触るとき: 少なくなるよう表示の項目を出す条件を変えるとき、または上限の値をどこから読むかを確かめるときに見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.config.showLessFrequentlyCap`, `this.showLessFrequentlyCount`

## AddonSuggestions.#minKeywordLength()
- 位置: L210-213
- 役割: addons.minKeywordLength の設定値を 0 以上に丸めて返す。
- 触るとき: アドオン候補を出す最小の検索語の長さを変えるとき、または少なくなるよう表示の後に候補が出なくなる理由を調べるときに見る。
- 呼び出し先: `Math.max()`, `lazy.UrlbarPrefs.get()`
