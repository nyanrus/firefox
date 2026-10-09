# browser/components/urlbar/UrlbarProviderRestrictKeywordsAutofill.sys.mjs

source: browser/components/urlbar/UrlbarProviderRestrictKeywordsAutofill.sys.mjs
source-hash: 8558c84fda435d2abf23a760e15331ab54327879
lines: 216

## <module>
- 役割: 検索モードの制限キーワードを、入力中の「@」に対するオートフィルと完全一致の heuristic 結果として出す UrlbarProviderRestrictKeywordsAutofill を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderRestrictKeywordsAutofill.constructor()
- 位置: L31-33
- 役割: 基底の UrlbarProvider をそのまま初期化するだけのコンストラクターである。
- 触るとき: プロバイダーに初期状態を持たせるとき、ここに処理を足す。
- 呼び出し先: `super()`

## UrlbarProviderRestrictKeywordsAutofill.type()
- 位置: L38-40
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: オートフィル結果の muxer での扱いを変えたいとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderRestrictKeywordsAutofill.getPriority()
- 位置: L42-44
- 役割: プロバイダーの優先度として 1 を返す。
- 触るとき: オートフィル結果を他の候補より前後させたいとき、この値を見直す。

## UrlbarProviderRestrictKeywordsAutofill.#getLowerCaseTokenToKeywords()
- 位置: async L46-57
- 役割: L10n の制限キーワードを小文字化した Map を作ってインスタンスに保存し、それを返す。
- 触るとき: キーワードの大文字小文字の扱いを変えたり、マッチ対象を増やしたりするとき見る。保存された Map は #getKeywordAliases からも使われる。
- 呼び出し先: `[...tokenToKeywords].map()`, `keyword.toLowerCase()`, `keywords.map()`, `lazy.UrlbarTokenizer.getL10nRestrictKeywords()`
- 参照: `this.#lowerCaseTokenToKeywords`

## UrlbarProviderRestrictKeywordsAutofill.#getKeywordAliases()
- 位置: async L59-63
- 役割: 保存済みキーワードの全てに「@」を付けた別名の配列を返す。
- 触るとき: 「@history 」のように完全一致で検索モードへ入る判定に使う別名の形式を変えるとき見る。(要確認: #lowerCaseTokenToKeywords が未設定のまま呼ばれると、値の取得で例外になり得る。)
- 呼び出し先: `Array.from()`, `Array.from(await this.#lowerCaseTokenToKeywords.values()) .flat()`, `Array.from(await this.#lowerCaseTokenToKeywords.values()) .flat() .map()`, `this.#lowerCaseTokenToKeywords.values()`

## UrlbarProviderRestrictKeywordsAutofill.isActive()
- 位置: async L65-105
- 役割: feature gate の確認後、単一トークンの「@」入力で部分オートフィル結果を先に作って保持し、なければ「@キーワード 」の完全一致があるときだけ有効にする。
- 触るとき: 「@h」のような途中入力で補完が出ない、または余計に出るときに有効化条件を確かめる。autoFill 設定や allowAutofill の影響もここで見る。
- 呼び出し先: `keyword.startsWith()`, `keywordAliases.some()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`, `queryContext.restrictInSearchMode()`, `queryContext.searchString.startsWith()`, `this.#getKeywordAliases()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("autoFill") && queryContext.allowAutofill)` → `this.#getAutofillResult()`
- 参照: `queryContext.allowAutofill`, `queryContext.restrictSource`, `queryContext.searchString.length`, `queryContext.tokens.length`, `queryContext.trimmedLowerCaseSearchString`, `this.#autofillData`, `this.queryInstance`

## UrlbarProviderRestrictKeywordsAutofill.startQuery()
- 位置: async L114-159
- 役割: isActive で保持した補完結果があればそれを追加し、無ければ入力全体が「@キーワード 」に一致するときだけ heuristic の RESTRICT 結果を追加する。
- 触るとき: 補完後の Enter で検索モードに入る挙動や、heuristic 結果として出す条件を変えたいとき、この関数を見る。
- 呼び出し先: `keywords.includes()`, `queryContext.trimmedLowerCaseSearchString.substring()`, `this.#getLowerCaseTokenToKeywords()`
- 条件付き依存: `if ( this.#autofillData && this.#autofillData.instance == this.queryInstance )` → `addCallback()`
- 条件付き依存: `if (restrictSymbol && typedKeyword == aliasKeyword)` → `addCallback()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `queryContext.lowerCaseSearchString`, `this.#autofillData`, `this.#autofillData.instance`, `this.#autofillData.result`, `this.queryInstance`

## UrlbarProviderRestrictKeywordsAutofill.cancelQuery()
- 位置: L161-165
- 役割: 同じクエリインスタンスの保持済み補完結果を破棄する。
- 触るとき: クエリを途中で止めたあとに古い補完が残る不具合を調べるとき見る。
- 参照: `this.#autofillData`, `this.#autofillData?.instance`, `this.queryInstance`

## UrlbarProviderRestrictKeywordsAutofill.#getAutofillResult()
- 位置: async L167-214
- 役割: 入力された「@」の前方一致でキーワードを探し、一致したら末尾に空白を付けた autofill 付き RESTRICT 結果を返す。
- 触るとき: 補完文字列の末尾の空白や、ユーザーの入力の大文字小文字をどう残すかを変えるとき見る。
- 呼び出し先: `[...l10nRestrictKeywords].map()`, `keyword.startsWith()`, `keywords.find()`, `this.#getLowerCaseTokenToKeywords()`, `tokenToKeywords.entries()`
- 条件付き依存: `if (autofillKeyword)` → `autofillKeyword.substr()`
- 条件付き依存: `if (autofillKeyword)` → `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.find( mode => mode.restrict == token )?.icon`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_TYPE.RESTRICT`, `mode.restrict`, `queryContext.searchString`, `queryContext.searchString.length`, `value.length`
