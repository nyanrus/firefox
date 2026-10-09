# browser/components/urlbar/UrlbarProviderTokenAliasEngines.sys.mjs

source: browser/components/urlbar/UrlbarProviderTokenAliasEngines.sys.mjs
source-hash: 2f2b35301b26fa4fdcc88fc369c9377ea76314a8
lines: 232

## <module>
- 役割: 「@」とトークン別名の付いた検索エンジンを候補として出す UrlbarProviderTokenAliasEngines を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderTokenAliasEngines.constructor()
- 位置: L29-32
- 役割: 基底の初期化に加えて、取得したエンジン一覧を入れる _engines を空配列で用意する。
- 触るとき: エンジン一覧の保持方法を変えるとき、ここでの初期値を確かめる。
- 呼び出し先: `super()`
- 参照: `this._engines`

## UrlbarProviderTokenAliasEngines.type()
- 位置: L37-39
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: エイリアス候補の表示位置や muxer での扱いを変えたいとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderTokenAliasEngines.PRIORITY()
- 位置: L41-44
- 役割: 優先度を 1 とし、検索候補(SearchSuggestions)や履歴(Places)より先に出るようにする。
- 触るとき: エイリアス候補と検索候補・履歴候補の前後関係を変えたいとき、この値を見る。

## UrlbarProviderTokenAliasEngines.isActive()
- 位置: async L54-100
- 役割: 「@」で始まる一語の入力で、検索モード外かつエンジンがあるときだけ有効にし、「@」単独なら true、途中入力なら自動補完結果を保持する。
- 触るとき: 「@」入力でエンジン候補が出ない、または検索モード中に出てしまう問題を調べるとき、有効化条件と自動補完の分岐を確かめる。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarSearchUtils.tokenAliasEngines()`, `queryContext.restrictInSearchMode()`, `queryContext.searchString.startsWith()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("autoFill") && queryContext.allowAutofill)` → `this._getAutofillResult()`
- 参照: `queryContext.allowAutofill`, `queryContext.tokens.length`, `queryContext.trimmedSearchString`, `this._autofillData`, `this._engines`, `this._engines.length`, `this.queryInstance`

## UrlbarProviderTokenAliasEngines.startQuery()
- 位置: async L110-153
- 役割: 保持した補完結果を先に追加し、残りのエンジンのうち別名が入力の前方一致するものを SEARCH 結果として順に追加する。
- 触るとき: 候補の並び、表示するエンジンの絞り込み、検索モードへ入る payload を変えるとき見る。
- 呼び出し先: `tokenAliases[0].startsWith()`
- 条件付き依存: `if ( this._autofillData && this._autofillData.instance == this.queryInstance )` → `addCallback()`
- 条件付き依存: `if ( tokenAliases[0].startsWith(queryContext.trimmedSearchString) && engine.name != this._autofillData?.result.payload.engine )` → `tokenAliases.join()`
- 条件付き依存: `if ( tokenAliases[0].startsWith(queryContext.trimmedSearchString) && engine.name != this._autofillData?.result.payload.engine )` → `UrlbarUtils.getEngineIconUrl()`
- 条件付き依存: `if ( tokenAliases[0].startsWith(queryContext.trimmedSearchString) && engine.name != this._autofillData?.result.payload.engine )` → `addCallback()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.trimmedSearchString`, `this._autofillData`, `this._autofillData.instance`, `this._autofillData.result`, `this._autofillData?.result.payload.engine`, `this._engines`, `this._engines.length`, `this.queryInstance`

## UrlbarProviderTokenAliasEngines.getPriority()
- 位置: L160-162
- 役割: 静的な PRIORITY の値を返す。
- 触るとき: 優先度を動的に変える必要が出たとき、ここを書き換える。
- 参照: `UrlbarProviderTokenAliasEngines.PRIORITY`

## UrlbarProviderTokenAliasEngines.cancelQuery()
- 位置: L167-171
- 役割: 同じクエリインスタンスの保持済み補完結果を破棄する。
- 触るとき: 途中でキャンセルされた後に古い補完が残る不具合を調べるとき見る。
- 参照: `this._autofillData`, `this._autofillData?.instance`, `this.queryInstance`

## UrlbarProviderTokenAliasEngines._getAutofillResult()
- 位置: async L173-230
- 役割: 入力と前方一致する別名を探し、別名の後に空白が続いたら補完を止め、途中なら末尾に空白を付けた補完結果を返す。
- 触るとき: エイリアスの補完文字列や、補完を止める条件(空白で検索モードへ入る)を変えるとき見る。
- 呼び出し先: `alias.startsWith()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `lowerCaseSearchString.startsWith()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `lazy.UrlUtils.REGEXP_SPACES_START.test()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `lowerCaseSearchString.substring()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `alias.substr()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `tokenAliases.join()`
- 条件付き依存: `if (alias.startsWith(lowerCaseSearchString))` → `UrlbarUtils.getEngineIconUrl()`
- 参照: `alias.length`, `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.searchString`, `queryContext.searchString.length`, `this._engines`, `value.length`
