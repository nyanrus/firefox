# browser/components/urlbar/UrlbarProviderSearchSuggestions.sys.mjs

source: browser/components/urlbar/UrlbarProviderSearchSuggestions.sys.mjs
source-hash: c8e07ac2164de89420b3a00e2d6c92e55e1ddf7e
lines: 719

## <module>
- 役割: 検索エンジンの検索候補(履歴由来、リモート候補、トレンド)を URL バーに出す UrlbarProviderSearchSuggestions を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Services.urlFormatter.formatURLPref()`

## looksLikeUrl()
- 位置: L59-68
- 役割: 空白を含まず、「/」「@」「:」「[」のいずれかを含むか、ドットを含む一語を URL らしいとみなす。
- 触るとき: URL に見える候補を検索候補から外す判定を変えるとき、またはドットを含む語の扱いを確かめるときに見る。
- 呼び出し先: `/^([\[\]A-Z0-9-]+\.){3,}[^.]+$/i.test()`, `["/", "@", ":", "["].some()`, `lazy.UrlUtils.REGEXP_SPACES.test()`, `str.includes()`

## UrlbarProviderSearchSuggestions.constructor()
- 位置: L77-79
- 役割: 基底の UrlbarProvider をそのまま初期化するだけのコンストラクターである。
- 触るとき: プロバイダーに初期状態を持たせるとき、ここに処理を足す。
- 呼び出し先: `super()`

## UrlbarProviderSearchSuggestions.type()
- 位置: L84-86
- 役割: プロバイダー種別として NETWORK を返し、リモートを使う候補として扱う。
- 触るとき: 検索候補の muxer での扱いや、ネットワーク候補としての分類を変えるとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.NETWORK`

## UrlbarProviderSearchSuggestions.isActive()
- 位置: async L95-127
- 役割: 検索ソースが含まれ、制限が検索のみか無いときに限って、空の入力は手掛かりがある場合だけ、履歴またはリモートの候補のどちらかが許されるときに有効にする。
- 触るとき: 検索候補が出ない原因を調べるとき、ソース制限、空入力、許可の順で弾かれていないかを確かめる。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.sources.includes()`, `this.#shouldFetchTrending()`, `this._allowRemoteSuggestions()`, `this._allowSuggestions()`, `this._isTokenOrRestrictionPresent()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `queryContext.restrictSource`, `queryContext.trimmedSearchString`

## UrlbarProviderSearchSuggestions._isTokenOrRestrictionPresent()
- 位置: L138-150
- 役割: 入力が「@」で始まる、検索の制限記号がある、検索モードでソースに検索が含まれる、のいずれかなら true を返す。
- 触るとき: 「@」や制限記号があるときに検索の設定を無視する扱いを変えるとき見る。
- 呼び出し先: `queryContext.searchString.startsWith()`, `queryContext.sources.includes()`, `queryContext.tokens.some()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `queryContext.restrictSource`, `queryContext.searchMode`, `t.type`

## UrlbarProviderSearchSuggestions._allowSuggestions()
- 位置: L161-179
- 役割: urlbar では suggest.searches が無効で、トークンや制限が無いときは false とし、検索バー以外では browser.search.suggest.enabled と非公開用の設定も確かめる。
- 触るとき: 検索候補の全体の設定(通常、非公開、検索バー)による無効化の条件を変えるとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this._isTokenOrRestrictionPresent()`
- 参照: `queryContext.isPrivate`, `queryContext.isSearchbarSAP`, `queryContext.sapName`

## UrlbarProviderSearchSuggestions._allowRemoteSuggestions()
- 位置: L189-231
- 役割: リモート候補の可否を判定する。禁止フラグ、トレンドの有効化、トークンの有無、直前の少件数の結果との関係を順に見て、最後に allowRemoteResults に任せる。
- 触るとき: リモート候補が出ない、または多すぎる問題を調べるとき見る。入力の伸ばし方による抑止条件もここで確かめる。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `queryContext.allowRemoteResults()`, `searchString.startsWith()`, `searchString.trim()`, `this.#shouldFetchTrending()`, `this._isTokenOrRestrictionPresent()`
- 参照: `queryContext.prohibitRemoteResults`, `queryContext.searchString`, `searchString.length`, `this._lastLowResultsSearchSuggestion`, `this._lastLowResultsSearchSuggestion.length`

## UrlbarProviderSearchSuggestions.startQuery()
- 位置: async L241-314
- 役割: 「@」の別名があればそのエンジンを、無ければ検索モードかトークンの既定エンジンを使い、#fetchSearchSuggestions の結果を追加する。別名が未確定の「@」入力では候補を出さない。
- 触るとき: どのエンジンで検索候補を取るかの選び方や、「@」入力時の振る舞いを変えるとき見る。
- 呼び出し先: `UrlbarUtils.substringAt()`, `UrlbarUtils.substringAt( queryContext.searchString, queryContext.tokens[0]?.value || "" ).trim()`, `addCallback()`, `lazy.UrlbarTokenizer.isRestrictionToken()`, `this.#fetchSearchSuggestions()`, `this._maybeGetAlias()`
- 条件付き依存: `if (!aliasEngine)` → `queryContext.searchString.startsWith()`
- 条件付き依存: `if (leadingRestrictionToken === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH)` → `UrlbarUtils.substringAfter(query, leadingRestrictionToken).trim()`
- 条件付き依存: `if (leadingRestrictionToken === lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH)` → `UrlbarUtils.substringAfter()`
- 条件付き依存: `if (queryContext.searchMode?.engineName)` → `lazy.UrlbarSearchUtils.getEngineByName()`
- 条件付き依存: `if (!(queryContext.searchMode?.engineName))` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 参照: `aliasEngine.alias`, `aliasEngine.engine`, `aliasEngine.query`, `lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `queryContext.isPrivate`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens.length`, `queryContext.tokens[0].type`, `queryContext.tokens[0].value`, `queryContext.tokens[0]?.value`, `this.queryInstance`

## UrlbarProviderSearchSuggestions.getPriority()
- 位置: L322-327
- 役割: トレンド候補を出すときは TopSites の優先度、それ以外は 0 を返す。
- 触るとき: トレンド候補を他の候補より前に出したいとき、この条件を見直す。
- 呼び出し先: `this.#shouldFetchTrending()`
- 参照: `lazy.UrlbarProviderTopSites.PRIORITY`

## UrlbarProviderSearchSuggestions.cancelQuery()
- 位置: L332-336
- 役割: 動いている検索候補の取得コントローラーを止める。
- 触るとき: 入力が変わった後も古い候補の取得が続く問題を調べるとき見る。
- 条件付き依存: `if (this.#suggestionsController)` → `this.#suggestionsController.stop()`
- 参照: `this.#suggestionsController`

## UrlbarProviderSearchSuggestions.getResultCommands()
- 位置: L344-361
- 役割: トレンド結果には「表示しない」「詳しく」のコマンドを返し、それ以外には何も返さない。
- 触るとき: トレンド結果の右クリックメニューの項目を変えたいとき見る。
- 参照: `RESULT_MENU_COMMANDS.TRENDING_BLOCK`, `RESULT_MENU_COMMANDS.TRENDING_HELP`, `result.payload.trending`

## UrlbarProviderSearchSuggestions.onEngagement()
- 位置: L368-396
- 役割: dismiss では履歴の該当語を削除して結果を外す。トレンドの「非表示」では設定を切り、テレメトリを記録し、確認メッセージに差し替える。
- 触るとき: 候補の削除や、トレンドを非表示にしたときの振る舞いを変えるとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.set()`, `this.#recordTrendingBlockedTelemetry()`, `this.#replaceTrendingResultWithAcknowledgement()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.FormHistory.update()`
- 条件付き依存: `if (details.selType == "dismiss")` → `console.error()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 参照: `RESULT_MENU_COMMANDS.TRENDING_BLOCK`, `RESULT_MENU_COMMANDS.TRENDING_HELP`, `details.selType`, `lazy.DEFAULT_FORM_HISTORY_PARAM`, `result.payload.suggestion`

## UrlbarProviderSearchSuggestions.#fetchSearchSuggestions()
- 位置: async L403-582
- 役割: ローカル候補の件数、リモート候補の件数(トレンド時は検索モードの有無で別の上限)を決めて候補を取得し、履歴結果と検索結果に変換する。尾部の候補は 100ms までの待ちを挟んで最後に出す。
- 触るとき: 候補の件数上限、尾部候補の扱い、リッチ候補のアイコン、履歴の表示を変えるときに見る。maxResults より 1 多く取る理由もここにある。
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `UrlbarUtils.getRemoteImageUrl()`, `entry.value.toLocaleLowerCase()`, `lazy.UrlbarPrefs.get()`, `looksLikeUrl()`, `results.push()`, `searchString.trim()`, `this.#shouldFetchTrending()`, `this.#suggestionsController.fetch()`, `this._allowRemoteSuggestions()`, `this._isTokenOrRestrictionPresent()`, `this.logger.error()`
- 条件付き依存: `if (allowRemote && this.#shouldFetchTrending(queryContext))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( queryContext.searchMode && lazy.UrlbarPrefs.get("trending.maxResultsSearchMode") != -1 )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!( queryContext.searchMode && lazy.UrlbarPrefs.get("trending.maxResultsSearchMode") != -1 ))` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( !queryContext.searchMode && lazy.UrlbarPrefs.get("trending.maxResultsNoSearchMode") != -1 )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("maxHistoricalSearchSuggestions"))` → `results.push()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("maxHistoricalSearchSuggestions"))` → `makeFormHistoryResult()`
- 条件付き依存: `if (!tail)` → `tailTimer.fire().catch()`
- 条件付き依存: `if (!tail)` → `tailTimer.fire()`
- 条件付き依存: `if (!tail)` → `this.logger.error()`
- 参照: `UrlbarProviderSearchSuggestions.RICH_ICON_SIZE`, `engine.name`, `entry.description`, `entry.icon`, `entry.matchPrefix`, `entry.tail`, `entry.tailOffsetIndex`, `entry.trending`, `entry.value`, `fetchData.local`, `fetchData.remote`, `fetchData.remote.length`, `lazy.SearchSuggestionController`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext.isPrivate`, `queryContext.maxResults`, `queryContext.sapName`, `queryContext.searchMode`, `queryContext.userContextId`, `searchString.length`, `tailTimer.promise`, `this.#suggestionsController`, `this._lastLowResultsSearchSuggestion`, `this.logger`

## UrlbarProviderSearchSuggestions._maybeGetAlias()
- 位置: async L603-639
- 役割: 検索モードでなく、先頭トークンが「@」以外の別名で、直後に空白があるときに、その別名のエンジンと残りの検索語を返す。
- 触るとき: 別名の判定条件(空白の要否や「@」の扱い)を変えるとき見る。
- 呼び出し先: `UrlbarUtils.substringAfter()`, `lazy.UrlUtils.REGEXP_SPACES_START.test()`, `lazy.UrlbarSearchUtils.engineForAlias()`
- 条件付き依存: `if (engineMatch)` → `query.trim()`
- 参照: `queryContext.searchMode`, `queryContext.searchString`, `queryContext.tokens`, `queryContext.tokens[0]?.value`

## UrlbarProviderSearchSuggestions.#shouldFetchTrending()
- 位置: L652-660
- 役割: 検索語が空で、トレンドの機能、設定が有効、かつ検索モードか検索モード不要の設定のときに true を返す。
- 触るとき: トレンド候補をいつ出すかを変えるとき、または出ない原因を調べるとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `queryContext.searchMode`, `queryContext.searchString`

## UrlbarProviderSearchSuggestions.#recordTrendingBlockedTelemetry()
- 位置: L665-667
- 役割: トレンドを非表示にした回数のテレメトリを一つ記録する。
- 触るとき: トレンドの非表示操作の計測が欠けるときに見る。
- 呼び出し先: `Glean.urlbarTrending.block.add()`

## UrlbarProviderSearchSuggestions.#replaceTrendingResultWithAcknowledgement()
- 位置: L676-696
- 役割: トレンド結果を全て取り除き、先頭の結果だけに「トレンドを非表示にした」旨の確認を付ける。
- 触るとき: トレンドを消したときの確認メッセージの出し方を変えるとき見る。
- 呼び出し先: `controller.removeResult()`, `queryContext.results.filter()`, `resultsToRemove.forEach()`, `resultsToRemove.reverse()`
- 参照: `result.payload.trending`

## makeFormHistoryResult()
- 位置: L699-718
- 役割: フォーム履歴の検索語を、履歴ソースの SEARCH 型の結果に変換する。ブロック可能で、履歴から削除するコマンドを持つ。
- 触るとき: 検索履歴の結果の表示や、削除操作の対象を変えるとき見る。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `entry.value.toLocaleLowerCase()`
- 参照: `engine.name`, `entry.value`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`
- XPCOM: `Services.urlFormatter`
