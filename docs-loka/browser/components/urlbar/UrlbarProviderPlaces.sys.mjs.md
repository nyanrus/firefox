# browser/components/urlbar/UrlbarProviderPlaces.sys.mjs

source: browser/components/urlbar/UrlbarProviderPlaces.sys.mjs
source-hash: d4f7db9d7debb99f3e6727d785a6bf94227e323b
lines: 1662

## <module>
- 役割: Places データベース(履歴、ブックマーク、開いているタブ)から URL バーの候補を作るプロバイダー。SQL で候補を引き、タブ切り替え・検索・ブックマーク・履歴の結果へ変換して重複を除く。
- 呼び出し先: `Object.freeze()`, `Object.values()`, `Object.values(MATCH_TYPE).reduce()`, `XPCOMUtils.declareLazy()`

## defaultQuery()
- 位置: L42-73
- 役割: moz_places を検索する SQL を組み立てる。ブックマーク情報とタグを付け、開いているタブ情報を結合し、AUTOCOMPLETE_MATCH で絞って頻度順に最大件数まで返す。
- 触るとき: 履歴・ブックマークの検索条件や並び順(frecency)、件数の上限を変えるとき。
- 参照: `lazy.PAGES_FRECENCY_FIELD`

## PAGES_FRECENCY_FIELD()
- 位置: L114-118
- 役割: 代替 frecency が有効なら alt_frecency、そうでなければ frecency の列名を返す遅延ゲッター。
- 触るとき: 並び順に使う frecency 列を切り替える条件を確認するとき。
- 参照: `lazy.PlacesUtils.history.isAlternativeFrecencyEnabled`

## typeToBehaviorMap()
- 位置: L120-132
- 役割: 制限トークンの種類(履歴、ブックマーク、タグ、開いているページ、検索、タイトル、URL)を動作名に対応させる。
- 触るとき: 新しい制限文字を足すとき、またはある制限文字が効かない原因を調べるとき。
- 参照: `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_BOOKMARK`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_HISTORY`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_OPENPAGE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_URL`

## sourceToBehaviorMap()
- 位置: L133-142
- 役割: 検索ソース(履歴、ブックマーク、タブ、検索)を動作名に対応させる。
- 触るとき: ソース指定(restrictSource)で絞り込んだときの動作を変えるとき。
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`

## setTimeout()
- 位置: L145-149
- 役割: nsITimer で一回だけ呼び出すタイマーを作る、setTimeout 相当の小さな関数。
- 触るとき: 結果の通知遅延の仕組みを変えるとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `timer.initWithCallback()`
- 参照: `Ci.nsITimer`, `timer.TYPE_ONE_SHOT`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`

## makeMapKeyForResult()
- 位置: L163-172
- 役割: URL と(必要なら)ユーザーコンテキスト ID を連結して、重複判定用のキー文字列を作る。
- 触るとき: コンテナが違う同一 URL を別物として扱うかどうかを変えるとき。
- 呼び出し先: `UrlbarUtils.tupleString()`, `lazy.PlacesUtils.parseActionUrl()`, `lazy.UrlbarShared.isNonPrivateUserContextId()`
- 参照: `action?.type`, `match.userContextId`, `match.value`

## makeKeyForMatch()
- 位置: L185-228
- 役割: 一致結果の重複判定キー、prefix(http/https/www)、アクションを返す。検索エンジン候補は エンジン名と検索語の組、それ以外は接頭辞を除いた URL で判定する。
- 触るとき: 検索候補の重複判定や、http と https、www の違いをどう扱うかを変えるとき。
- 呼び出し先: `( action.params.searchSuggestion || action.params.searchQuery ).toLocaleLowerCase()`, `lazy.PlacesUtils.parseActionUrl()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `makeMapKeyForResult()`
- 条件付き依存: `if (!action)` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if (!action)` → `makeMapKeyForResult()`
- 参照: `action.params.engineName`, `action.params.searchQuery`, `action.params.searchSuggestion`, `action.params.url`, `action.type`, `match.value`

## makeActionUrl()
- 位置: L239-250
- 役割: moz-action: 形式の URL を作る。各パラメータは null や undefined を除き、URI エンコードして JSON にする。
- 触るとき: タブ切り替えや検索エンジン候補に埋め込むパラメータの形式を変えるとき。
- 呼び出し先: `JSON.stringify()`, `encodeURIComponent()`

## convertLegacyMatches()
- 位置: L263-298
- 役割: 従来形式の一致データを UrlbarResult の配列に変換する。既に追加した URL は urls 集合で除外する。
- 触るとき: 従来の一致データから結果を作る処理や、重複の除外順を調べるとき。
- 呼び出し先: `makeMapKeyForResult()`, `makeUrlbarResult()`, `results.push()`, `urls.add()`, `urls.has()`
- 参照: `match.bookmarkDateMs`, `match.comment`, `match.finalCompleteValue`, `match.frecency`, `match.icon`, `match.lastVisit`, `match.style`, `match.tabGroup`, `match.userContextId`, `match.value`

## makeUrlbarResult()
- 位置: L315-437
- 役割: moz-action の種類(検索エンジン、タブ切り替え)か通常の URL かを判定して UrlbarResult を作る。ブックマーク・タグ・履歴の属性(削除可否、ヘルプ)も決める。
- 触るとき: 履歴・ブックマーク・タブ切り替えの結果の payload(タイトル、タグ、削除メニュー)を変えるとき。
- 呼び出し先: `info.style.includes()`, `lazy.PlacesUtils.parseActionUrl()`
- 条件付き依存: `if (action)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (action)` → `action.params.searchSuggestion.toLocaleLowerCase()`
- 条件付き依存: `if (action)` → `UrlbarUtils.getUserContextData()`
- 条件付き依存: `if (action)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (action)` → `UrlbarUtils.createTabSwitchSecondaryAction()`
- 条件付き依存: `if (action)` → `console.error()`
- 条件付き依存: `if (!(info.style.includes("bookmark")))` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (info.style.includes("tag"))` → `info.title.split()`
- 条件付き依存: `if (info.style.includes("tag"))` → `titleTags.split(",").filter()`
- 条件付き依存: `if (info.style.includes("tag"))` → `titleTags.split()`
- 条件付き依存: `if (info.style.includes("tag"))` → `tag.toLocaleLowerCase()`
- 条件付き依存: `if (info.style.includes("tag"))` → `queryContext.tokens.some()`
- 条件付き依存: `if (info.style.includes("tag"))` → `lowerCaseTag.includes()`
- 参照: `action.params.engineName`, `action.params.searchSuggestion`, `action.params.url`, `action.type`, `info.bookmarkDateMs`, `info.frecency`, `info.icon`, `info.lastVisit`, `info.tabGroup`, `info.title`, `info.url`, `info.userContextId`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.SUGGESTED`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `lazy.UrlbarShared.TITLE_TAGS_SEPARATOR`, `token.lowerCaseValue`
- XPCOM: `Services.urlFormatter`

## Search.constructor()
- 位置: L459-574
- 役割: クエリ文字列の接頭辞を取り除き、トークンを分析して、制限トークン、既定の動作、ヒューリスティックトークン、最大件数(要求の 1.5 倍)を決める。
- 触るとき: 検索の開始時に入力がどう解釈されるか(about: の扱い、制限トークン、件数)を調べるとき。
- 呼び出し先: `Math.round()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.unEscapeURIForUI()`, `lazy.UrlbarTokenizer.tokenize()`, `lazy.sourceToBehaviorMap.has()`, `queryContext.restrictInSearchMode()`, `this.filterTokens()`, `unescapedSearchString.startsWith()`, `unescapedSearchString.trim()`
- 条件付き依存: `if (!(unescapedSearchString.startsWith("about:")))` → `UrlbarUtils.stripURLPrefix()`
- 条件付き依存: `if (this.#searchModeEngine && queryContext.restrictInSearchMode())` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (tokens.length)` → `lazy.UrlbarTokenizer.isRestrictionToken()`
- 条件付き依存: `if ( prefix && prefix != "about:" && tokens[0].value.length > prefix.length )` → `tokens[0].value.substring()`
- 条件付き依存: `if ( queryContext && queryContext.restrictSource && lazy.sourceToBehaviorMap.has(queryContext.restrictSource) )` → `this.setBehavior()`
- 条件付き依存: `if ( queryContext && queryContext.restrictSource && lazy.sourceToBehaviorMap.has(queryContext.restrictSource) )` → `lazy.sourceToBehaviorMap.get()`
- 条件付き依存: `if (!( queryContext && queryContext.restrictSource && lazy.sourceToBehaviorMap.has(queryContext.restrictSource) ))` → `this.#trimmedOriginalSearchString.startsWith()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("filter.javascript"))` → `this.setBehavior()`
- 参照: `engine.searchUrlDomain`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `prefix.length`, `queryContext.currentPage`, `queryContext.isPrivate`, `queryContext.maxResults`, `queryContext.restrictSource`, `queryContext.restrictToken`, `queryContext.searchMode?.engineName`, `queryContext.searchString`, `queryContext.trimmedSearchString`, `queryContext.userContextId`, `this.#behavior`, `this.#currentPage`, `this.#emptySearchDefaultBehavior`, `this.#filterOnHost`, `this.#heuristicToken`, `this.#inPrivateWindow`, `this.#leadingRestrictionToken`, `this.#listener`, `this.#maxResults`, `this.#originalSearchString`, `this.#provider`, `this.#queryContext`, `this.#searchModeEngine`, `this.#searchString`, `this.#searchTokens`, `this.#searchTokens.length`, `this.#searchTokens[0].value`, `this.#trimmedOriginalSearchString`, `this.#userContextId`, `tokens.length`, `tokens[0].type`, `tokens[0].value`, `tokens[0].value.length`

## Search.setBehavior()
- 位置: L582-585
- 役割: 指定の動作名に対応する mozIPlacesAutoComplete のビットを立てる。
- 触るとき: 検索動作の組み合わせを追加するとき。
- 呼び出し先: `type.toUpperCase()`
- 参照: `Ci.mozIPlacesAutoComplete`, `this.#behavior`

## Search.hasBehavior()
- 位置: L594-597
- 役割: 指定の動作名のビットが立っているかを返す。
- 触るとき: 検索の対象(履歴、ブックマーク、タブなど)を判定する箇所を追うとき。
- 呼び出し先: `type.toUpperCase()`
- 参照: `Ci.mozIPlacesAutoComplete`, `this.#behavior`

## Search.filterTokens()
- 位置: L607-636
- 役割: 制限トークンを検出して動作を restrict に切り替え、トークンから取り除く。通常トークンだけを残して返す。
- 触るとき: 制限トークンの効き方(ブックマーク限定や履歴限定)を変えるとき。
- 呼び出し先: `lazy.UrlbarTokenizer.isRestrictionToken()`, `lazy.typeToBehaviorMap.get()`, `this.setBehavior()`
- 条件付き依存: `if (!lazy.UrlbarTokenizer.isRestrictionToken(token))` → `filtered.push()`
- 条件付き依存: `if (!foundToken)` → `this.setBehavior()`
- 条件付き依存: `if (behavior == "tag")` → `this.setBehavior()`
- 参照: `this.#behavior`, `token.type`

## Search.stop()
- 位置: L643-656
- 役割: 検索を止める。保留中の通知タイマーを解除し、実行中の SQL を中断して pending を false にする。
- 触るとき: 入力が変わった後に古い検索が結果を出し続ける問題を調べるとき。
- 条件付き依存: `if (this.#notifyTimer)` → `this.#notifyTimer.cancel()`
- 条件付き依存: `if (typeof this.#interrupt == "function")` → `this.#interrupt()`
- 参照: `this.#interrupt`, `this.#notifyDelaysCount`, `this.#notifyTimer`, `this.pending`

## Search.execute()
- 位置: async L669-761
- 役割: 必要に応じて開いているタブの問い合わせと通常の問い合わせを実行し、件数が足りなければ MATCH_ANYWHERE で再検索する。「@」だけの入力や検索限定時は早めに終える。
- 触るとき: 検索の実行順、件数不足時の再検索、早期終了の条件を変えるとき。
- 呼び出し先: `conn.executeCached()`, `lazy.UrlbarSearchUtils.tokenAliasEngines()`, `queries.push()`, `this.#checkIfFirstTokenIsKeyword()`, `this.#onResultRow.bind()`, `this.hasBehavior()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString == "@" && tokenAliasEngines.length)` → `this.#provider.finishSearch()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString)` → `/\s*\S?$/.test()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString)` → `this.#trimmedOriginalSearchString.startsWith()`
- 条件付き依存: `if (this.#trimmedOriginalSearchString)` → `this.hasBehavior()`
- 条件付き依存: `if ( emptySearchRestriction || (tokenAliasEngines.length && this.#trimmedOriginalSearchString.startsWith("@")) || (this.hasBehavior("search") && this.hasBehavior...)` → `this.#provider.finishSearch()`
- 条件付き依存: `if (this.hasBehavior("openpage"))` → `queries.push()`
- 条件付き依存: `if (count < this.#maxResults)` → `this.hasBehavior()`
- 条件付き依存: `if (this.hasBehavior("openpage"))` → `queries.unshift()`
- 条件付き依存: `if (count < this.#maxResults)` → `conn.executeCached()`
- 条件付き依存: `if (count < this.#maxResults)` → `this.#onResultRow.bind()`
- 参照: `Ci.mozIPlacesAutoComplete.MATCH_ANYWHERE`, `MATCH_TYPE.GENERAL`, `lazy.UrlbarProviderOpenTabs.promiseDBPopulated`, `lazy.UrlbarShared.RESTRICT_TOKENS.SEARCH`, `this.#counts`, `this.#firstTokenIsKeyword`, `this.#interrupt`, `this.#leadingRestrictionToken`, `this.#matchBehavior`, `this.#maxResults`, `this.#searchQuery`, `this.#switchToTabQuery`, `this.#trimmedOriginalSearchString`, `this.#trimmedOriginalSearchString.length`, `this.pending`, `tokenAliasEngines.length`

## this.#interrupt()
- 位置: L676-681
- 役割: stop() から呼ばれ、実行中の SQL を conn.interrupt() で中断する。ProvidersManager の割り込みレベルが 0 のときだけ中断する。
- 触るとき: 検索の中断タイミングや、他のプロバイダーとの割り込み条件を変えるとき。
- 条件付き依存: `if (!lazy.ProvidersManager.interruptLevel)` → `conn.interrupt()`
- 参照: `lazy.ProvidersManager.interruptLevel`

## Search.#checkIfFirstTokenIsKeyword()
- 位置: async L818-842
- 役割: 先頭語が検索エンジンのエイリアスかキーワードブックマークなら true を返す。キーワードの場合はサイトのホストで絞り込む。
- 触るとき: キーワード検索の先頭語を結果から除く挙動を調べるとき。
- 呼び出し先: `lazy.KeywordUtils.getBindableKeyword()`, `lazy.UrlbarSearchUtils.engineForAlias()`
- 参照: `entry.url.host`, `this.#filterOnHost`, `this.#heuristicToken`, `this.#originalSearchString`

## Search.#onResultRow()
- 位置: L844-853
- 役割: SQL の 1 行を一致データに変換する。一般の結果が上限に達するか検索が止まったら、SQL の読み出しを打ち切る。
- 触るとき: 行ごとの処理と、結果上限での打ち切り条件を変えるとき。
- 呼び出し先: `this.#addFilteredQueryMatch()`
- 条件付き依存: `if (!this.pending || count >= this.#maxResults)` → `cancel()`
- 参照: `MATCH_TYPE.GENERAL`, `this.#counts`, `this.#maxResults`, `this.pending`

## Search.#maybeRestyleSearchMatch()
- 位置: L876-925
- 役割: 履歴にある検索結果ページ(SERP)が、入力語と同じ検索 URL に相当すれば、検索エンジン候補に書き換える。
- 触るとき: 履歴の検索ページを検索候補として表示する(restyleSearches)条件を変えるとき。
- 呼び出し先: `UrlbarUtils.getSearchQueryUrl()`, `lazy.SearchService.parseSubmissionURL()`, `lazy.UrlbarSearchUtils.serpsAreEquivalent()`, `makeActionUrl()`, `parseResult.terms.toLowerCase()`, `terms.includes()`, `this.#searchTokens.every()`, `this.#searchTokens.map()`, `this.#searchTokens.map(t => t.value).join()`
- 参照: `match.comment`, `match.icon`, `match.iconUrl`, `match.style`, `match.value`, `parseResult.engine`, `parseResult.engine.name`, `parseResult.terms`, `parseResult.termsParameterName`, `parseResult?.engine`, `t.value`, `this.#searchTokens.length`, `token.value`

## Search.#addMatch()
- 位置: L927-974
- 役割: 頻度と種類を確かめ、検索履歴の書き換えや、アイコンと最終値の既定値(空文字)を補ってから挿入位置を求め、一致一覧に入れる。挿入後に結果を通知する。
- 触るとき: 一致結果を一覧に追加する前後の処理(検索履歴の扱い、結果の通知)を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#getInsertIndexForMatch()`, `this.#matches.splice()`, `this.notifyResult()`
- 条件付き依存: `if ( match.style == "favicon" && (lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine) )` → `this.#maybeRestyleSearchMatch()`
- 条件付き依存: `if ( match.style == "favicon" && (lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine) )` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (replace)` → `this.#matches.splice()`
- 参照: `MATCH_TYPE.GENERAL`, `match.finalCompleteValue`, `match.frecency`, `match.icon`, `match.style`, `match.type`, `this.#counts`, `this.#searchModeEngine`, `this.pending`

## Search.#getInsertIndexForMatch()
- 位置: L997-1127
- 役割: 重複を判定し、重複なら捨てるか既存の結果と置き換える(切り替えタブは優先、https は www の有無で判断)。重複でなければ結果グループ内の挿入位置を決める。
- 触るとき: 同じ URL の複数候補(http と https、www の有無、タブ切り替えと履歴)のどれを残すかを変えるとき。
- 呼び出し先: `lazy.ObjectUtils.deepEqual()`, `makeKeyForMatch()`, `makeMapKeyForResult()`, `this.#usedPlaceIds.has()`, `this.#usedURLs.some()`
- 条件付き依存: `if ( (match.placeId && this.#usedPlaceIds.has(makeMapKeyForResult(match.placeId, match))) || this.#usedURLs.some(e => lazy.ObjectUtils.deepEqual(e.key, urlMapKey)) )` → `["switchtab", "remotetab"].includes()`
- 条件付き依存: `if (action && ["switchtab", "remotetab"].includes(action.type))` → `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (!(action && ["switchtab", "remotetab"].includes(action.type)))` → `UrlbarUtils.getPrefixRank()`
- 条件付き依存: `if (!(action && ["switchtab", "remotetab"].includes(action.type)))` → `lazy.ObjectUtils.deepEqual()`
- 条件付き依存: `if (lazy.ObjectUtils.deepEqual(existingKey, urlMapKey))` → `prefix.endsWith()`
- 条件付き依存: `if (lazy.ObjectUtils.deepEqual(existingKey, urlMapKey))` → `existingPrefix.endsWith()`
- 条件付き依存: `if (match.placeId)` → `this.#usedPlaceIds.add()`
- 条件付き依存: `if (match.placeId)` → `makeMapKeyForResult()`
- 条件付き依存: `if (!this.#groups)` → `this.#makeGroups()`
- 条件付き依存: `if (!this.#groups)` → `lazy.UrlbarPrefs.getResultGroups()`
- 参照: `action.type`, `e.key`, `group.available`, `group.count`, `group.insertIndex`, `group.type`, `match.comment`, `match.placeId`, `match.type`, `this.#groups`, `this.#maxResults`, `this.#queryContext`, `this.#usedURLs`, `this.#usedURLs.length`

## Search.#makeGroups()
- 位置: L1129-1186
- 役割: 結果グループの設定を、一致の種類(ヒューリスティック、一般、候補、拡張機能)ごとの枠(利用可能数、挿入位置、件数)に変換する。
- 触るとき: 結果グループごとの表示枠の割り当てや、どのグループが先に埋まるかを変えるとき。
- 呼び出し先: `Math.min()`, `this.#makeGroups()`
- 条件付き依存: `if (!resultGroup.children)` → `this.#groups.push()`
- 参照: `MATCH_TYPE.EXTENSION`, `MATCH_TYPE.GENERAL`, `MATCH_TYPE.HEURISTIC`, `MATCH_TYPE.SUGGESTION`, `last.type`, `lazy.UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_SEARCH_TIP`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `lazy.UrlbarShared.RESULT_GROUP.HEURISTIC_TOKEN_ALIAS_ENGINE`, `lazy.UrlbarShared.RESULT_GROUP.OMNIBOX`, `lazy.UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `lazy.UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `resultGroup.availableSpan`, `resultGroup.children`, `resultGroup.group`, `resultGroup.maxResultCount`, `this.#groups`, `this.#groups.length`, `this.#maxResults`

## Search.#addFilteredQueryMatch()
- 位置: L1188-1250
- 役割: SQL の行から一致データを作り、開いているタブならタブ切り替え、履歴のみの検索で該当しなければ favicon 表示、タグ付きならタグ、ブックマークなら bookmark のスタイルを付けて追加する。
- 触るとき: 1 件の候補の表示スタイル(タブ切り替え、ブックマーク、タグ、履歴)の決め方を変えるとき。
- 呼び出し先: `lazy.PlacesUtils.toDate()`, `lazy.PlacesUtils.toDate(bookmarkDatePRTime).getTime()`, `lazy.PlacesUtils.toDate(lastVisitPRTime).getTime()`, `lazy.UrlbarShared.getIconForUrl()`, `row.getResultByName()`, `this.#addMatch()`, `this.hasBehavior()`
- 条件付き依存: `if (openPageCount > 0 && this.hasBehavior("openpage"))` → `makeActionUrl()`
- 条件付き依存: `if (!(openPageCount > 0 && this.hasBehavior("openpage")))` → `this.hasBehavior()`
- 条件付き依存: `if (tags)` → `this.hasBehavior()`
- 参照: `lazy.UrlbarShared.TITLE_TAGS_SEPARATOR`, `match.comment`, `match.style`, `match.userContextId`, `match.value`, `this.#currentPage`, `this.#userContextId`

## Search.#suggestionPrefQuery()
- 位置: L1257-1327
- 役割: 検索条件に応じて、履歴・ブックマーク・タグの絞り込み句を組み、ホスト絞り込み時は不要なリダイレクト等を除いて defaultQuery に渡す。
- 触るとき: サイト内検索やキーワードでの絞り込みの条件、または制限トークンごとの対象を変えるとき。
- 呼び出し先: `conditions.join()`, `defaultQuery()`, `this.hasBehavior()`
- 条件付き依存: `if (this.#filterOnHost)` → `conditions.push()`
- 条件付き依存: `if (this.#filterOnHost)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine)` → `conditions.push()`
- 条件付き依存: `if (!(lazy.UrlbarPrefs.get("restyleSearches") || this.#searchModeEngine))` → `conditions.push()`
- 条件付き依存: `if ( this.hasBehavior("restrict") || (!this.hasBehavior("openpage") && (!this.hasBehavior("history") || !this.hasBehavior("bookmark"))) )` → `this.hasBehavior()`
- 条件付き依存: `if (this.hasBehavior("history"))` → `conditions.push()`
- 条件付き依存: `if (this.hasBehavior("bookmark"))` → `conditions.push()`
- 条件付き依存: `if (this.hasBehavior("tag"))` → `conditions.push()`
- 参照: `this.#filterOnHost`, `this.#searchModeEngine`

## Search.#emptySearchDefaultBehavior()
- 位置: L1329-1343
- 役割: 検索語が空のときの既定動作を決める。履歴が有効なら履歴、そうでなければブックマーク、どちらも無効ならタブ。
- 触るとき: 空の入力で何が出るかを変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(lazy.UrlbarPrefs.get("suggest.history")))` → `lazy.UrlbarPrefs.get()`
- 参照: `Ci.mozIPlacesAutoComplete.BEHAVIOR_BOOKMARK`, `Ci.mozIPlacesAutoComplete.BEHAVIOR_HISTORY`, `Ci.mozIPlacesAutoComplete.BEHAVIOR_OPENPAGE`, `Ci.mozIPlacesAutoComplete.BEHAVIOR_RESTRICT`

## Search.#keywordFilteredSearchString()
- 位置: L1351-1357
- 役割: キーワードの先頭語が検索されていれば、それを除いたトークンを空白で連結した検索語を返す。
- 触るとき: キーワード付きの入力で、先頭語を検索語に含めないようにする挙動を確認するとき。
- 呼び出し先: `this.#searchTokens.map()`, `tokens.join()`
- 条件付き依存: `if (this.#firstTokenIsKeyword)` → `tokens.slice()`
- 参照: `t.value`, `this.#firstTokenIsKeyword`

## Search.#searchQuery()
- 位置: L1367-1389
- 役割: 通常の検索 SQL と引数(検索語、動作、件数、タブ切り替えの有効性、ユーザーコンテキスト、ホスト)を組み立てる。
- 触るとき: 通常の検索に渡す引数を追加・変更するとき。
- 呼び出し先: `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`, `this.hasBehavior()`
- 参照: `lazy.PlacesUtils.tagsFolderId`, `params.host`, `params.userContextId`, `this.#behavior`, `this.#filterOnHost`, `this.#inPrivateWindow`, `this.#keywordFilteredSearchString`, `this.#matchBehavior`, `this.#maxResults`, `this.#suggestionPrefQuery`

## Search.#switchToTabQuery()
- 位置: L1398-1414
- 役割: 履歴にない開いているタブを探すための SQL と引数を返す。
- 触るとき: 履歴に無いタブ切り替え候補の出方を変えるとき。
- 呼び出し先: `lazy.UrlbarShared.getUserContextIdForOpenPagesTable()`
- 参照: `this.#behavior`, `this.#inPrivateWindow`, `this.#keywordFilteredSearchString`, `this.#matchBehavior`, `this.#maxResults`

## Search.notifyResult()
- 位置: L1432-1458
- 役割: 一致一覧をリスナーへ通知する。通知は約 16ms の遅延で一括化し、検索が終わったら通知後に検索を停止する。
- 触るとき: 結果の通知頻度(ちらつき防止)や検索終了時の後始末を変えるとき。
- 条件付き依存: `if (this.#notifyTimer)` → `this.#notifyTimer.cancel()`
- 条件付き依存: `if (this.#notifyDelaysCount > 3)` → `notify()`
- 条件付き依存: `if (!(this.#notifyDelaysCount > 3))` → `setTimeout()`
- 参照: `this.#notifyDelaysCount`, `this.#notifyTimer`

## notify()
- 位置: L1433-1445
- 役割: 保留中の検索ならリスナーへ一覧を渡し、検索終了時はリスナーとプロバイダーの参照を外して停止する。
- 触るとき: 検索終了時に循環参照を切る処理を調べるとき。
- 呼び出し先: `this.#listener()`
- 条件付き依存: `if (!searchOngoing)` → `this.stop()`
- 参照: `this.#listener`, `this.#matches`, `this.#notifyDelaysCount`, `this.#provider`, `this.pending`

## UrlbarProviderPlaces.type()
- 位置: L1481-1483
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: Places 結果の種別と並び順を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderPlaces.getDatabaseHandle()
- 位置: L1492-1512
- 役割: Places の大きなキャッシュ DB 接続を一度だけ取得して共有する。終了時にはブロッカーで検索参照を外す。
- 触るとき: DB 接続の取得や終了時の扱いを変えるとき。接続失敗時はログに出す。
- 条件付き依存: `if (!_promiseDatabase)` → `lazy.PlacesUtils.promiseLargeCacheDBConnection()`
- 条件付き依存: `if (!_promiseDatabase)` → `lazy.Sqlite.shutdown.addBlocker()`
- 条件付き依存: `if (!_promiseDatabase)` → `dump()`
- 条件付き依存: `if (!_promiseDatabase)` → `this.logger.error()`
- 参照: `this.#currentSearch`

## UrlbarProviderPlaces.isActive()
- 位置: async L1521-1529
- 役割: 検索語が空で検索エンジンのモードに入っているときだけ false を返し、それ以外は常に起動する。
- 触るとき: Places 検索を止める条件を追加するとき。
- 参照: `queryContext.searchMode?.engineName`, `queryContext.trimmedSearchString`

## UrlbarProviderPlaces.startQuery()
- 位置: L1538-1551
- 役割: 従来の検索を開始し、一致が届くたびに UrlbarResult に変換して追加する。終了を待つ Promise を返す。
- 触るとき: Places の検索結果が届く流れや、クエリが古くなったときの無視の仕方を調べるとき。
- 呼び出し先: `addCallback()`, `convertLegacyMatches()`, `this.#startLegacyQuery()`
- 参照: `this.#deferred.promise`, `this.queryInstance`

## UrlbarProviderPlaces.cancelQuery()
- 位置: L1556-1566
- 役割: 実行中の検索を止め、待っている Promise を解決し、通知なしで検索を終える。
- 触るとき: 入力が変わったときに Places の検索を止める挙動を調べるとき。
- 呼び出し先: `this.finishSearch()`
- 条件付き依存: `if (this.#currentSearch)` → `this.#currentSearch.stop()`
- 条件付き依存: `if (this.#deferred)` → `this.#deferred.resolve()`
- 参照: `this.#currentSearch`, `this.#deferred`

## UrlbarProviderPlaces.finishSearch()
- 位置: L1575-1596
- 役割: 通知を求められて検索が保留中なら、残りの結果を最終通知として送る。現在の検索を取り違えないよう、通知を最後に呼ぶ。
- 触るとき: 検索の最終通知のタイミングを変えるとき。順序を入れ替えると競合が起きる点に注意する。
- 呼び出し先: `search.notifyResult()`
- 参照: `search.pending`, `this.#currentSearch`

## UrlbarProviderPlaces.onEngagement()
- 位置: L1603-1624
- 役割: 削除が選ばれたとき、検索結果から作った URL、または通常の URL を履歴から削除し、結果を一覧から消す。
- 触るとき: 履歴からの削除メニューの範囲を変えるとき。
- 条件付き依存: `if (details.selType == "dismiss")` → `UrlbarUtils.getUrlFromResult()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove(url).catch()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (details.selType == "dismiss")` → `controller.removeResult()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history .remove(result.payload.url) .catch()`
- 条件付き依存: `if (details.selType == "dismiss")` → `lazy.PlacesUtils.history .remove()`
- 参照: `console.error`, `details.selType`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `result.payload.url`, `result.type`

## UrlbarProviderPlaces.#startLegacyQuery()
- 位置: L1626-1636
- 役割: 通知の受け口を作って検索を開始し、検索が終わったら完了を知らせる Promise を保持する。
- 触るとき: 従来検索の完了判定を変えるとき。
- 呼び出し先: `Promise.withResolvers()`, `this.#startSearch()`
- 参照: `queryContext.searchString`, `this.#deferred`

## listener()
- 位置: L1628-1633
- 役割: 一致を受け取って呼び出し元へ渡し、検索が終わったら完了の Promise を解決する。
- 触るとき: 検索の完了判定への応答を変えるとき。
- 呼び出し先: `callback()`
- 条件付き依存: `if (!searchOngoing)` → `deferred.resolve()`

## UrlbarProviderPlaces.#startSearch()
- 位置: L1638-1660
- 役割: 実行中の検索があれば止めてから新しい Search を作り、DB 接続が得られたら実行する。終了時に完了処理を呼ぶ。
- 触るとき: 検索の開始・置き換え・失敗時の扱いを変えるとき。
- 呼び出し先: `dump()`, `search.execute()`, `this.getDatabaseHandle()`, `this.getDatabaseHandle() .then()`, `this.getDatabaseHandle() .then(conn => search.execute(conn)) .catch()`, `this.logger.error()`
- 条件付き依存: `if (this.#currentSearch)` → `this.cancelQuery()`
- 条件付き依存: `if (search == this.#currentSearch)` → `this.finishSearch()`
- 参照: `this.#currentSearch`
