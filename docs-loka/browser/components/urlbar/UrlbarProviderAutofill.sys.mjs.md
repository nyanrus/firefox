# browser/components/urlbar/UrlbarProviderAutofill.sys.mjs

source: browser/components/urlbar/UrlbarProviderAutofill.sys.mjs
source-hash: 92d7a4b1da39753d3db65c9066abd885bd053aa1
lines: 1313

## <module>
- 役割: URL バーの自動補完(autofill)プロバイダー。入力文字列の先頭をオリジン・URL・適応型履歴から補完し、ヒューリスティック結果として返す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `lazy.PlacesUtils.history.pageFrecencyThreshold()`, `originQuery()`, `parseFloat()`, `urlQuery()`

## inputHistoryPicksToUseCount()
- 位置: L84-90
- 役割: 選択回数(picks)を、一度に選んで放置した後の moz_inputhistory.use_count 相当の値に換算する。
- 触るとき: 適応型履歴の閾値(urlMinPicks や urlPicksAgeDays)の意味を変えたり、減衰の計算を確認したいとき。
- 参照: `lazy.frecencyDecayRate`

## urlUseCountThreshold()
- 位置: L98-104
- 役割: urlMinPicks と urlPicksAgeDays から use_count 閾値を一度だけ計算し、メモ化して返す。
- 触るとき: 適応型 URL 補完の閾値が古い値のまま残る、またはプレファレンス変更時に再計算されないと疑うとき。
- 呼び出し先: `inputHistoryPicksToUseCount()`
- 参照: `lazy.urlMinPicks`, `lazy.urlPicksAgeDays`

## effectiveSources()
- 位置: L110-119
- 役割: クエリの sources と places.history.enabled から、履歴・ブックマークのどちらを補完対象にできるかを返す。
- 触るとき: 履歴オプトアウト時にブックマークのみの経路へ落ちる挙動を変える、またはソース指定の扱いを調べるとき。
- 呼び出し先: `queryContext.sources.includes()`
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.historyEnabled`

## originQuery()
- 位置: L173-266
- 役割: moz_origins を対象に、オリジン補完用の SQL を組み立てる。where 句を差し替えて複数の変種を作る。
- 触るとき: オリジン補完の候補選定(frecency 閾値、ブックマーク件数、https 優先)を変えるときに読む。
- 呼び出し先: `where.includes()`

## urlQuery()
- 位置: L268-318
- 役割: moz_places を対象に、URL 補完用の SQL を組み立てる。www. 付きと無しの両方を検索して最良の 1 件を選ぶ。
- 触るとき: パス付きの入力に対する URL 補完の一致ロジックや、ブックマークのタイトル採用を変えるとき。

## UrlbarProviderAutofill.constructor()
- 位置: L441-443
- 役割: プロバイダーを生成し、_autofillData を null で初期化する。
- 触るとき: プロバイダーの初期状態に新しいフィールドを足すとき。
- 呼び出し先: `super()`

## UrlbarProviderAutofill.type()
- 位置: L448-450
- 役割: プロバイダー種別として HEURISTIC を返す。
- 触るとき: 補完結果を他のヒューリスティック結果とどう並べ替えるか、種別の扱いを確認したいとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderAutofill.isActive()
- 位置: async L459-527
- 役割: 補完を試すかを判定し、条件を満たせば補完結果を取得して _autofillData に保存する。
- 触るとき: 特定の入力で補完が始まらない(prefs、トークン数、空白、タグ・タイトル検索など)原因を調べるとき。
- 呼び出し先: `UrlbarUtils.stripURLPrefix()`, `lazy.UrlUtils.REGEXP_SPACES.test()`, `lazy.UrlbarPrefs.get()`, `queryContext.sources.includes()`, `queryContext.tokens.some()`, `this._getAutofillResult()`, `this._strippedPrefix.toLowerCase()`
- 参照: `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TAG`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_TITLE`, `queryContext.allowAutofill`, `queryContext.searchString`, `queryContext.searchString.length`, `queryContext.tokens.length`, `t.type`, `this._autofillData`, `this._searchString`, `this._strippedPrefix`, `this.queryInstance`

## UrlbarProviderAutofill.getPriority()
- 位置: L534-536
- 役割: 優先度として常に 0 を返す。
- 触るとき: 補完プロバイダーの優先度を変えたいと考えたとき。現状は固定値である点に注意する。

## UrlbarProviderAutofill.startQuery()
- 位置: async L545-562
- 役割: isActive で取得済みの _autofillData を結果として追加し、fallbackResult があれば続けて追加する。
- 触るとき: 補完結果が画面に出ない、または fallback(オリジン結果)が重複・欠落するのを調べるとき。
- 呼び出し先: `addCallback()`
- 条件付き依存: `if ( !this._autofillData || this._autofillData.instance != this.queryInstance )` → `this.logger.error()`
- 条件付き依存: `if (this._autofillData.fallbackResult)` → `addCallback()`
- 参照: `this._autofillData`, `this._autofillData.fallbackResult`, `this._autofillData.instance`, `this._autofillData.result`, `this.queryInstance`

## UrlbarProviderAutofill.cancelQuery()
- 位置: L567-571
- 役割: 現在のクエリに属する _autofillData を破棄する。
- 触るとき: 入力が変わった後に古い補完結果が残る問題を調べるとき。
- 参照: `this._autofillData`, `this._autofillData?.instance`, `this.queryInstance`

## UrlbarProviderAutofill.onEngagement()
- 位置: async L578-606
- 役割: 補完結果の「提案を削除」「履歴から削除」メニューを処理し、削除後に同じ検索文字列で再検索する。
- 触るとき: 補完結果の削除メニューの動作や、削除後の再検索を変えるとき。
- 呼び出し先: `UrlbarUtils.dismissAutofill()`
- 条件付き依存: `if (didRemove)` → `controller.input.setValue()`
- 条件付き依存: `if (didRemove)` → `controller.input.startQuery()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `RESULT_MENU_COMMANDS.DISMISS_AUTOFILL`, `details.selType`, `queryContext.searchString`, `result.payload.url`

## UrlbarProviderAutofill.getResultCommands()
- 位置: L608-645
- 役割: 補完結果の種類と非公開モードに応じて、結果メニューに出す削除コマンドを組み立てる。
- 触るとき: 補完結果のメニュー項目(提案を削除、履歴から削除)の出し分けを変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( result.autofill.type === "adaptive_url" || result.autofill.type === "adaptive_origin" || result.autofill.type === "origin" )` → `lazy.UrlbarShared.isOriginUrl()`
- 条件付き依存: `if (!isPrivate)` → `resultArray.push()`
- 条件付き依存: `if (!isOrigin)` → `resultArray.push()`
- 参照: `RESULT_MENU_COMMANDS.DISMISS`, `RESULT_MENU_COMMANDS.DISMISS_AUTOFILL`, `result.autofill`, `result.autofill.type`, `result.payload.url`, `resultArray.length`

## UrlbarProviderAutofill.getTopHostOverThreshold()
- 位置: async L657-711
- 役割: 与えられたホスト群から、履歴・ブックマーク条件と frecency 閾値を満たす最も frecency の高いホストを 1 件返す。
- 触るとき: 複数ホストの中から補完対象のホストを選ぶ処理を変えたり、閾値条件を確認したいとき。
- 呼び出し先: `conditions.join()`, `db.executeCached()`, `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `new Array(hosts.length).fill()`, `new Array(hosts.length).fill("?").join()`, `rows[0].getResultByName()`, `sources.includes()`
- 条件付き依存: `if ( sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY) && sources.includes(lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS) )` → `conditions.push()`
- 条件付き依存: `if (!( sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY) && sources.includes(lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS) ))` → `sources.includes()`
- 条件付き依存: `if (sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY))` → `conditions.push()`
- 条件付き依存: `if (!(sources.includes(lazy.UrlbarShared.RESULT_SOURCE.HISTORY)))` → `sources.includes()`
- 条件付き依存: `if (sources.includes(lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS))` → `conditions.push()`
- 参照: `conditions.length`, `hosts.length`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `queryContext.sources`, `rows.length`

## UrlbarProviderAutofill._getOriginQuery()
- 位置: L727-777
- 役割: 検索文字列の末尾スラッシュを除き、オリジン補完用のクエリと引数を選んで返す(履歴・ブックマーク・prefix の有無で分岐)。
- 触るとき: オリジン補完で使われる SQL の選択条件や引数(prefix、query_type)を変えるとき。
- 呼び出し先: `Date.now()`, `effectiveSources()`, `lazy.UrlbarPrefs.get()`, `searchStr.toLowerCase()`, `this._searchString.endsWith()`, `this._searchString.slice()`
- 参照: `QUERYTYPE.AUTOFILL_ORIGIN`, `opts.prefix`, `this._searchString`, `this._strippedPrefix`

## UrlbarProviderAutofill._getUrlQuery()
- 位置: L787-851
- 役割: 入力からホスト部分を取り出して逆順の rev_host を作り、URL 補完用のクエリと引数を返す。ホストが取れなければ null を返す。
- 触るとき: パス付き URL の補完が出ない、または URL 補完のクエリ引数を変えるとき。
- 呼び出し先: `effectiveSources()`, `host.split()`, `host.split("").reverse()`, `host.split("").reverse().join()`, `hostMatch[0].toLowerCase()`, `strippedURL.substr()`, `urlQueryHostRegexp.exec()`
- 条件付き依存: `if (this._strippedPrefix)` → `strippedURL.substr()`
- 条件付き依存: `if (historyAllowed && bookmarksAllowed)` → `lazy.UrlbarPrefs.get()`
- 参照: `QUERYTYPE.AUTOFILL_URL`, `host.length`, `lazy.pageFrecencyThreshold`, `opts.adaptiveAutofillEnabled`, `opts.pageFrecencyThreshold`, `opts.prefix`, `queryContext.trimmedSearchString`, `this._searchString`, `this._strippedPrefix`, `this._strippedPrefix.length`

## UrlbarProviderAutofill._getAdaptiveHistoryQuery()
- 位置: L853-947
- 役割: moz_inputhistory と閾値(use_count、frecency、ブロック状態)を使い、適応型履歴補完のクエリと引数を組み立てる。
- 触るとき: 利用者の入力履歴に基づく補完が出ない、またはブロックされたオリジンの扱いを調べるとき。
- 呼び出し先: `Date.now()`, `Object.assign()`, `effectiveSources()`, `lazy.UrlbarPrefs.get()`, `urlUseCountThreshold()`
- 参照: `QUERYTYPE.AUTOFILL_ADAPTIVE`, `lazy.UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `lazy.pageFrecencyThreshold`, `params.pageFrecencyThreshold`, `queryContext.lowerCaseSearchString`, `this._searchString`, `this._strippedPrefix`

## UrlbarProviderAutofill._processRow()
- 位置: L958-1132
- 役割: クエリ種別ごとにDB行を補完結果へ変換する。補完テキスト、タイトル、アイコン、大文字小文字の扱いを決めて UrlbarResult を作る。
- 触るとき: 補完される文字列の形(次のスラッシュまで補完する、大文字小文字を保つ等)やタイトルの表示を変えるとき。
- 呼び出し先: `fixedURL.substring()`, `lazy.UrlbarShared.canAutofillURL()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.isOriginUrl()`, `row.getResultByName()`, `strippedURL.toLowerCase()`, `url .toLowerCase()`, `url .toLowerCase() .indexOf()`, `url.indexOf()`, `url.substr()`, `url.substring()`
- 条件付き依存: `if ( queryType != QUERYTYPE.AUTOFILL_ORIGIN && queryContext.searchString.length == autofilledValue.length )` → `autofilledValue.substring()`
- 条件付き依存: `if ( queryType != QUERYTYPE.AUTOFILL_ORIGIN && queryContext.searchString.length == autofilledValue.length )` → `finalCompleteValue.substring()`
- 条件付き依存: `if (!(title))` → `lazy.UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (!(title))` → `lazy.UrlbarShared.prepareUrlForDisplay()`
- 条件付き依存: `if (!(title))` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if (!(title))` → `this._searchString.includes()`
- 参照: `QUERYTYPE.AUTOFILL_ADAPTIVE`, `QUERYTYPE.AUTOFILL_ORIGIN`, `QUERYTYPE.AUTOFILL_URL`, `autofilledValue.length`, `finalCompleteValue.length`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `new URL(finalCompleteValue).href`, `payload.title`, `queryContext.searchString`, `queryContext.searchString.length`, `searchString.length`, `strippedAutofilledValue.length`, `strippedURL.length`, `this._strippedPrefix.length`

## UrlbarProviderAutofill._getAutofillResult()
- 位置: async L1134-1143
- 役割: about: ページの補完を先に試し、なければ既知 URL の補完を返す。
- 触るとき: 補完の経路(about ページか DB か)の順序を変えるとき。
- 呼び出し先: `this._matchAboutPageForAutofill()`, `this._matchKnownUrl()`

## UrlbarProviderAutofill._matchAboutPageForAutofill()
- 位置: L1145-1185
- 役割: about: で始まる入力に対し、表示対象の about ページから最初に前方一致するものを補完結果にする。
- 触るとき: about: ページの補完候補の選び方や表示タイトルを変えるとき。
- 呼び出し先: `aboutUrl.startsWith()`, `this._searchString.toLowerCase()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `lazy.UrlbarShared.stripPrefixAndTrim()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `this._searchString.includes()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `aboutUrl.substring()`
- 条件付き依存: `if (aboutUrl.startsWith(`about:${this._searchString.toLowerCase()}`))` → `lazy.UrlbarShared.getIconForUrl()`
- 参照: `autofilledValue.length`, `lazy.AboutPagesUtils.visibleAboutUrls`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `queryContext.searchString`, `queryContext.searchString.length`, `this._searchString`, `this._strippedPrefix`

## UrlbarProviderAutofill._matchKnownUrl()
- 位置: async L1187-1250
- 役割: 適応型履歴、オリジン、URL の順に DB を照会し、最初に一致した行を補完結果にする。適応型のときは fallback のオリジン結果も付ける。
- 触るとき: 補完の優先順位(適応型履歴 > オリジン > URL)や、入力がオリジンか URL かの判定を変えるとき。
- 呼び出し先: `lazy.PlacesUtils.promiseLargeCacheDBConnection()`, `lazy.UrlUtils.looksLikeOrigin()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.get("autoFill.adaptiveHistory.enabled") && lazy.UrlbarPrefs.get("autoFill.adaptiveHistory.minCharsThreshold") <= queryContext.searchString....)` → `this._getAdaptiveHistoryQuery()`
- 条件付き依存: `if (query)` → `conn.executeCached()`
- 条件付き依存: `if (resultSet.length)` → `this._processRow()`
- 条件付き依存: `if (result)` → `this._getFallbackOriginResult()`
- 条件付き依存: `if ( lazy.UrlUtils.looksLikeOrigin(this._searchString, { ignoreKnownDomains: true, allowPartialNumericalTLDs: true, }) )` → `this._getOriginQuery()`
- 条件付き依存: `if (!( lazy.UrlUtils.looksLikeOrigin(this._searchString, { ignoreKnownDomains: true, allowPartialNumericalTLDs: true, }) ))` → `this._getUrlQuery()`
- 条件付き依存: `if (rows.length)` → `this._processRow()`
- 参照: `queryContext.searchString.length`, `result.payload.url`, `resultSet.length`, `rows.length`, `this._searchString`, `this._searchString.length`

## UrlbarProviderAutofill._getFallbackOriginResult()
- 位置: async L1270-1311
- 役割: パス付きの補完 URL に対し、同じオリジンのルート URL が frecency > 0 で存在すればその結果を返す。
- 触るとき: パス付き補完のときに、ルートへ直接移動できる候補を出すかどうかを変えるとき。
- 呼び出し先: `Date.now()`, `Services.urlFormatter.formatURLPref()`, `URL.parse()`, `conn.executeCached()`, `lazy.UrlbarShared.getIconForUrl()`, `lazy.UrlbarShared.isOriginUrl()`, `rows[0].getResultByName()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.HISTORY`, `lazy.UrlbarShared.RESULT_TYPE.URL`, `parsedUrl.origin`, `rows.length`
- XPCOM: `Services.urlFormatter`
