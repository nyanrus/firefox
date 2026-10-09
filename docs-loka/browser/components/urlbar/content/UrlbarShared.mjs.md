# browser/components/urlbar/content/UrlbarShared.mjs

source: browser/components/urlbar/content/UrlbarShared.mjs
source-hash: f135f613f6ae34df77a040e61ecdf7d8261532c5
lines: 1933

## <module>
- 役割: urlbar 全体で共有する定数、判定関数、表示用の整形関数をまとめた名前空間 (UrlbarShared)。
- 呼び出し先: `Object.freeze()`, `element.documentGlobal.windowUtils.getBoundsWithoutFlushing()`, `element.getBoundingClientRect()`

## isInstance()
- 位置: L117-122
- 役割: 値が指定のインターフェース (例: KeyboardEvent) かを判定する。chrome では isInstance、content では instanceof を使う。
- 触るとき: content と chrome で型判定の結果が食い違う時。
- 条件付き依存: `if (typeof ChromeUtils != "undefined")` → `iface.isInstance()`

## LOCAL_SEARCH_MODES()
- 位置: L448-484
- 役割: 局所検索モード (ブックマーク、タブ、履歴、アクション) の定義一覧を返す。
- 触るとき: 局所検索モードを追加する時や、その表示順、テレメトリ名、設定の名前を変える時。
- 参照: `this.RESTRICT_TOKENS.ACTION`, `this.RESTRICT_TOKENS.BOOKMARK`, `this.RESTRICT_TOKENS.HISTORY`, `this.RESTRICT_TOKENS.OPENPAGE`, `this.RESULT_SOURCE.ACTIONS`, `this.RESULT_SOURCE.BOOKMARKS`, `this.RESULT_SOURCE.HISTORY`, `this.RESULT_SOURCE.TABS`

## SEARCH_MODE_RESTRICT()
- 位置: L489-501
- 役割: 検索モードで絞り込みに使う文字の集合を返す。scotchBonnet.enableOverride が有効ならアクション用の文字も加える。
- 触るとき: 検索モードに入る文字が増減した時や、scotchBonnet の有効化で挙動が変わる時。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `keys.push()`
- 参照: `this.RESTRICT_TOKENS.ACTION`, `this.RESTRICT_TOKENS.BOOKMARK`, `this.RESTRICT_TOKENS.HISTORY`, `this.RESTRICT_TOKENS.OPENPAGE`, `this.RESTRICT_TOKENS.SEARCH`

## getUserContextIdForOpenPagesTable()
- 位置: L513-515
- 役割: プライベートウィンドウなら専用の ID、それ以外は渡された container ID をそのまま返す。
- 触るとき: 開いているタブの検索で open-pages テーブルの ID がずれる時。

## normalizedUserContextId()
- 位置: L527-534
- 役割: container ID を open-pages テーブル用の ID に直し、0 になった場合は既定の ID にする。
- 触るとき: クエリ文脈の userContextId が想定外の値になる時。
- 呼び出し先: `this.getUserContextIdForOpenPagesTable()`

## isNonPrivateUserContextId()
- 位置: L542-544
- 役割: userContextId がプライベート用の ID でないかを判定する。
- 触るとき: プライベートウィンドウでコンテナ情報を使うかどうかを判定する箇所を調べる時。

## isContainerUserContextId()
- 位置: L552-554
- 役割: userContextId が 0 より大きい (コンテナのタブ) かを判定する。
- 触るとき: コンテナのタブだけ扱いを分けたい時。

## getLogger()
- 位置: L571-585
- 役割: 接頭辞ごとにロガーを作って再利用する。chrome では console.createInstance を使い、content では代わりの実装を使う。
- 触るとき: urlbar のログの接頭辞やレベル設定を変える時。
- 呼び出し先: `loggers.get()`, `loggers.set()`
- 条件付き依存: `if (console.createInstance)` → `createLoggerChrome()`
- 条件付き依存: `if (!(console.createInstance))` → `createLoggerContent()`
- 参照: `console.createInstance`

## getLoadRequestFromResult()
- 位置: L601-626
- 役割: 結果から読み込み要求を作る。検索結果は engineSearch (クエリとエンジン名)、URL を持つ結果は urlLoad を返し、どちらも無ければ null。
- 触るとき: 候補を選んだ時に検索として読み込むか URL として読み込むかの判定が違う時。
- 参照: `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.SEARCH`, `element?.dataset.query`, `result.payload.engine`, `result.payload.postData`, `result.payload.query`, `result.payload.suggestion`, `result.payload.url`, `result.type`

## deepEqual()
- 位置: L638-653
- 役割: 配列・オブジェクト・プリミティブを再帰的に比べる、JSON 的なデータ専用の等価判定。
- 触るとき: 表示キャッシュの比較など、プレーンなデータ同士の一致を判定する箇所を変える時。Map や Set には使えない点に注意。
- 呼び出し先: `Object.hasOwn()`, `Object.keys()`, `UrlbarShared.deepEqual()`, `aKeys.every()`
- 参照: `aKeys.length`, `bKeys.length`

## looksLikeSingleWordHost()
- 位置: L667-670
- 役割: 前後の空白を除いた文字列が、任意のポートを付けた単語 1 つのホストに見えるかを REGEXP_SINGLE_WORD で判定する。
- 触るとき: 単語だけの入力をホストとして扱うかの判定を変える時。(要確認: コメントはドットを含まないとするが、正規表現はドットを許す)
- 呼び出し先: `this.REGEXP_SINGLE_WORD.test()`, `value.trim()`

## isOriginUrl()
- 位置: L682-687
- 役割: URL がパスは / だけで、クエリもハッシュも無い origin かを判定する。解析できなければ false。
- 触るとき: origin だけの候補を判定する条件を変える時。
- 呼び出し先: `URL.parse()`
- 参照: `parsed.hash`, `parsed.pathname`, `parsed.search`

## isSearchbarSAP()
- 位置: L704-706
- 役割: sapName が SEARCHBAR_SAPS に含まれるかを返す。
- 触るとき: 検索バー専用の入力欄を新しく作り、判定の対象に入れるかを決める時。
- 呼び出し先: `this.SEARCHBAR_SAPS.includes()`

## keywordEnabled()
- 位置: L718-720
- 役割: 検索バー系の SAP なら常に true、それ以外は keyword.enabled の設定値を返す。
- 触るとき: URL でない入力を検索に回すかの判定がずれる時。
- 呼び出し先: `UrlbarPrefs.get()`, `this.isSearchbarSAP()`

## navigationEnabled()
- 位置: L731-733
- 役割: sapName が searchbar でなければ URL への移動を許可する。
- 触るとき: ツールバーの検索バーで URL が移動ではなく検索語として扱われる理由を確かめる時。

## navigationInSearchModeEnabled()
- 位置: L745-751
- 役割: エンジン検索モード中に URL への移動を許すかを、移動可能かどうかと検索バーか unifiedSearchButton.always で判定する。
- 触るとき: エンジン検索モード中に URL を入れた時の挙動を調べる時。
- 呼び出し先: `UrlbarPrefs.get()`, `this.isSearchbarSAP()`, `this.navigationEnabled()`

## getIconForUrl()
- 位置: L760-773
- 役割: URL の種類に応じて page-icon: 形式の URL か既定のアイコンを返す。
- 触るとき: URL 候補のアイコンが既定の画像になってしまう時。
- 呼び出し先: `this.PROTOCOLS_WITH_ICONS.includes()`, `this.isInstance()`
- 条件付き依存: `if (typeof url == "string")` → `this.PROTOCOLS_WITH_ICONS.some()`
- 条件付き依存: `if (typeof url == "string")` → `url.startsWith()`
- 参照: `this.ICON.DEFAULT`, `url.href`, `url.protocol`

## getResultSourceName()
- 位置: L784-794
- 役割: RESULT_SOURCE の値から小文字の名前 (bookmarks など) を返す。結果は初回に Map へまとめる。
- 触るとき: データ源の名前を文字列としてログや計測に出す時。
- 呼び出し先: `this._resultSourceNamesBySource.get()`
- 条件付き依存: `if (!this._resultSourceNamesBySource)` → `Object.entries()`
- 条件付き依存: `if (!this._resultSourceNamesBySource)` → `this._resultSourceNamesBySource.set()`
- 条件付き依存: `if (!this._resultSourceNamesBySource)` → `sourceName.toLowerCase()`
- 参照: `UrlbarShared.RESULT_SOURCE`, `this._resultSourceNamesBySource`

## stripPrefixAndTrim()
- 位置: L822-853
- 役割: 指定された接頭辞 (http://、https://、www.) と末尾の記号 (#、?、/、.) を取り除き、取り除いた部分も返す。
- 触るとき: 表示用の文字列から接頭辞や末尾の記号を落とす処理を変える時。
- 呼び出し先: `spec.endsWith()`, `spec.startsWith()`
- 条件付き依存: `if (options.stripHttp && spec.startsWith("http://"))` → `spec.slice()`
- 条件付き依存: `if (!(options.stripHttp && spec.startsWith("http://")))` → `spec.startsWith()`
- 条件付き依存: `if (options.stripHttps && spec.startsWith("https://"))` → `spec.slice()`
- 条件付き依存: `if (options.stripWww && spec.startsWith("www."))` → `spec.slice()`
- 条件付き依存: `if (options.trimEmptyHash && spec.endsWith("#"))` → `spec.slice()`
- 条件付き依存: `if (options.trimEmptyQuery && spec.endsWith("?"))` → `spec.slice()`
- 条件付き依存: `if (options.trimSlash && spec.endsWith("/"))` → `spec.slice()`
- 条件付き依存: `if (options.trimTrailingDot && spec.endsWith("."))` → `spec.slice()`
- 参照: `options.stripHttp`, `options.stripHttps`, `options.stripWww`, `options.trimEmptyHash`, `options.trimEmptyQuery`, `options.trimSlash`, `options.trimTrailingDot`

## unEscapeURIForUI()
- 位置: L863-867
- 役割: 表示用に URI のエスケープを戻す。MAX_TEXT_LENGTH を超える長さの文字列はそのまま返す。
- 触るとき: 表示 URL が文字化けする時や、エスケープを戻す範囲を変える時。
- 呼び出し先: `UrlbarContentUtils.unEscapeURIForUI()`
- 参照: `this.MAX_TEXT_LENGTH`, `uri.length`

## prepareUrlForDisplay()
- 位置: L880-909
- 役割: URL を表示用に整える。punycode を戻し、trimURLs が有効なら http と https のスキーム、末尾の / と www. を外す。schemeless なら接頭辞を全部外す。
- 触るとき: 表示 URL のスキームや末尾の / の有無が期待と違う時。
- 呼び出し先: `UrlbarContentUtils.getDisplaySpec()`, `this.unEscapeURIForUI()`
- 条件付き依存: `if (schemeless)` → `this.stripPrefixAndTrim()`
- 条件付き依存: `if (!(schemeless))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (trimURL && UrlbarPrefs.get("trimURLs"))` → `displayString.replace()`
- 条件付き依存: `if (trimURL && UrlbarPrefs.get("trimURLs"))` → `displayString.startsWith()`
- 条件付き依存: `if (displayString.startsWith("https://"))` → `displayString.substring()`
- 条件付き依存: `if (displayString.startsWith("https://"))` → `displayString.startsWith()`
- 条件付き依存: `if (displayString.startsWith("www."))` → `displayString.substring()`
- 参照: `url.href`

## canAutofillURL()
- 位置: L925-977
- 役割: URL が候補文字列で補完できるかを、origin や次の / までの規則で判定する。
- 触るとき: オートフィルの補完範囲 (次の / まで) がずれる時。
- 呼び出し先: `URL.parse()`, `candidate.href.endsWith()`, `candidateString.toLocaleLowerCase()`, `this.REGEXP_PREFIX.test()`, `url.hash.startsWith()`, `urlString .toLocaleLowerCase()`, `urlString .toLocaleLowerCase() .startsWith()`
- 条件付き依存: `if (checkFragmentOnly)` → `url.hash.startsWith()`
- 条件付き依存: `if (!candidate.href.endsWith("/"))` → `url.pathname.indexOf()`
- 参照: `candidate.hash`, `candidate.pathname.length`, `candidateString.length`, `url.hash`, `url.pathname.length`, `urlString.length`

## isPasteEvent()
- 位置: L985-991
- 役割: 入力イベントの inputType が貼り付けかどうかを判定する。
- 触るとき: 貼り付けとして扱うべき入力が通常の入力として扱われる時。
- 呼び出し先: `event.inputType.startsWith()`
- 参照: `event.inputType`

## sanitizeTextFromClipboard()
- 位置: L1006-1031
- 役割: クリップボードの文字列を整える。キーワードは空白を置換し、data URL は改行を整理し、それ以外は改行を除く。最後に javascript: を取り除く。
- 触るとき: 貼り付けの結果が改行や空白の点で想定と違う時、または貼り付け処理を変える時。
- 呼び出し先: `URL.parse()`, `this.stripUnsafeProtocolOnPaste()`
- 条件付き依存: `if (clipboardData.length < 500)` → `clipboardData.replace()`
- 条件付き依存: `if (!(fixupInfo?.keywordAsSent))` → `url.href.match()`
- 条件付き依存: `if ( url?.protocol == "data:" && !url.href.match(/^data:.+;base64,/) )` → `clipboardData.replace()`
- 条件付き依存: `if (!( url?.protocol == "data:" && !url.href.match(/^data:.+;base64,/) ))` → `clipboardData.replace()`
- 参照: `clipboardData.length`, `fixupInfo?.keywordAsSent`, `url?.protocol`

## stripUnsafeProtocolOnPaste()
- 位置: L1040-1045
- 役割: 貼り付けた文字列の先頭から javascript: を、取れなくなるまで取り除く。
- 触るとき: javascript: の貼り付けを無害化する安全策を調べる時。
- 呼び出し先: `URL.parse()`, `pasteData.indexOf()`, `pasteData.substring()`
- 参照: `URL.parse(pasteData)?.protocol`

## getSpanForResult()
- 位置: L1061-1075
- 役割: 結果が占める行数を返す。非表示の露出は 0、設定された resultSpan があればその値、TIP は 3、それ以外は 1。
- 触るとき: 結果の高さや占める行数が想定と違う時。
- 参照: `UrlbarShared.RESULT_TYPE.TIP`, `result.isHiddenExposure`, `result.resultSpan`, `result.type`

## getResultGroup()
- 位置: L1085-1177
- 役割: 結果を muxer が使うグループ (RESULT_GROUP) に振り分ける。heuristic はプロバイダー名、通常の結果は種類と源で決める。
- 触るとき: 候補がどのグループに入り、並び順が変わるかを調べる時、または新しいプロバイダーのグループを決める時。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (result.heuristic)` → `result.providerName.startsWith()`
- 条件付き依存: `if (result.heuristic)` → `console.error()`
- 参照: `UrlbarShared.PROVIDER_TYPE.EXTENSION`, `UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `UrlbarShared.RESULT_GROUP.AI`, `UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `UrlbarShared.RESULT_GROUP.GENERAL`, `UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `UrlbarShared.RESULT_GROUP.HEURISTIC_AI_CHAT`, `UrlbarShared.RESULT_GROUP.HEURISTIC_AUTOFILL`, `UrlbarShared.RESULT_GROUP.HEURISTIC_BOOKMARK_KEYWORD`, `UrlbarShared.RESULT_GROUP.HEURISTIC_ENGINE_ALIAS`, `UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `UrlbarShared.RESULT_GROUP.HEURISTIC_FALLBACK`, `UrlbarShared.RESULT_GROUP.HEURISTIC_HISTORY_URL`, `UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `UrlbarShared.RESULT_GROUP.HEURISTIC_RESTRICT_KEYWORD_AUTOFILL`, `UrlbarShared.RESULT_GROUP.HEURISTIC_SEARCH_TIP`, `UrlbarShared.RESULT_GROUP.HEURISTIC_TEST`, `UrlbarShared.RESULT_GROUP.HEURISTIC_TOKEN_ALIAS_ENGINE`, `UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `UrlbarShared.RESULT_GROUP.OMNIBOX`, `UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `UrlbarShared.RESULT_GROUP.RESTRICT_SEARCH_KEYWORD`, `UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `UrlbarShared.RESULT_GROUP.SUGGESTED_INDEX`, `UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `result.group`, `result.hasSuggestedIndex`, `result.heuristic`, `result.isRichSuggestion`, `result.isSuggestedIndexRelativeToGroup`, `result.payload.suggestion`, `result.payload.tail`, `result.providerName`, `result.providerType`, `result.source`, `result.type`

## searchEngagementTelemetryGroup()
- 位置: L1185-1249
- 役割: 結果を計測用のグループ名 (top_pick、search_suggest など) に変換する。
- 触るとき: 計測のグループ分けに新しい結果グループを足す時。
- 呼び出し先: `this.getResultGroup()`
- 参照: `UrlbarShared.RESULT_GROUP.ABOUT_PAGES`, `UrlbarShared.RESULT_GROUP.AI`, `UrlbarShared.RESULT_GROUP.FORM_HISTORY`, `UrlbarShared.RESULT_GROUP.GENERAL`, `UrlbarShared.RESULT_GROUP.GENERAL_PARENT`, `UrlbarShared.RESULT_GROUP.HEURISTIC_EXTENSION`, `UrlbarShared.RESULT_GROUP.HEURISTIC_OMNIBOX`, `UrlbarShared.RESULT_GROUP.INPUT_HISTORY`, `UrlbarShared.RESULT_GROUP.OMNIBOX`, `UrlbarShared.RESULT_GROUP.RECENT_SEARCH`, `UrlbarShared.RESULT_GROUP.REMOTE_SUGGESTION`, `UrlbarShared.RESULT_GROUP.REMOTE_TAB`, `UrlbarShared.RESULT_GROUP.RESTRICT_SEARCH_KEYWORD`, `UrlbarShared.RESULT_GROUP.SEMANTIC_HISTORY`, `UrlbarShared.RESULT_GROUP.SUGGESTED_INDEX`, `UrlbarShared.RESULT_GROUP.TAIL_SUGGESTION`, `result.heuristic`, `result.isBestMatch`, `result.isRichSuggestion`, `result.payload.trending`, `result.providerName`

## searchEngagementTelemetryAction()
- 位置: L1258-1266
- 役割: 結果のアクションのキーを返す。GlobalActions では選ばれたキー、無ければ提示された全キーをカンマ区切りで返す。
- 触るとき: アクション付きの候補の計測値がずれる時。
- 呼び出し先: `result.payload.actionsResults.map()`, `result.payload.actionsResults.map(({ key }) => key).join()`
- 参照: `result.payload.action?.key`, `result.providerName`

## searchEngagementTelemetryType()
- 位置: L1275-1430
- 役割: 結果から engagement 計測の種類名 (url、search_suggest、tip_* など) を決める。
- 触るとき: 新しい結果種別を計測に出す時、または計測値が unknown になる原因を調べる時。
- 呼び出し先: `checkForSubType()`
- 条件付き依存: `if (result.providerName == "UrlbarProviderQuickSuggest")` → `this._getQuickSuggestTelemetryType()`
- 条件付き依存: `if (result.source === UrlbarShared.RESULT_SOURCE.BOOKMARKS)` → `checkForSubType()`
- 参照: `UrlbarShared.INTERVENTION_TIP_TYPE.CLEAR`, `UrlbarShared.INTERVENTION_TIP_TYPE.REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_ASK`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_CHECKING`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_REFRESH`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_RESTART`, `UrlbarShared.INTERVENTION_TIP_TYPE.UPDATE_WEB`, `UrlbarShared.PROVIDER_TYPE.EXTENSION`, `UrlbarShared.RESTRICT_TOKENS.ACTION`, `UrlbarShared.RESTRICT_TOKENS.BOOKMARK`, `UrlbarShared.RESTRICT_TOKENS.HISTORY`, `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`, `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.REMOTE_TAB`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `UrlbarShared.SEARCH_TIP_TYPE.ONBOARD`, `UrlbarShared.SEARCH_TIP_TYPE.REDIRECT`, `result.autofill`, `result.autofill.type`, `result.heuristic`, `result.isRichSuggestion`, `result.payload.isAutofillFallback`, `result.payload.keyword`, `result.payload.suggestion`, `result.payload.trending`, `result.payload.type`, `result.providerName`, `result.providerType`, `result.source`, `result.type`

## checkForSubType()
- 位置: L1294-1311
- 役割: 履歴・ブックマーク・タブの結果に、adaptive、semantic、serp の接尾辞を付ける (searchEngagementTelemetryType の中の関数)。
- 触るとき: 計測の種類名に接尾辞が付かない、または余計に付く時。
- 呼び出し先: `[ UrlbarShared.RESULT_SOURCE.BOOKMARKS, UrlbarShared.RESULT_SOURCE.HISTORY, UrlbarShared.RESULT_SOURCE.TABS, ].includes()`
- 参照: `UrlbarShared.RESULT_SOURCE.BOOKMARKS`, `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_SOURCE.TABS`, `res.isSERP`, `res.providerName`, `res.source`

## _getQuickSuggestTelemetryType()
- 位置: L1432-1439
- 役割: クイックサジェストの結果を計測名にする。weather は接頭辞なし、それ以外は source_telemetryType の形にする。
- 触るとき: Suggest の計測名が変わった時、または新しい telemetryType を追加する時。
- 参照: `result.payload.source`, `result.payload.telemetryType`

## getTokenMatches()
- 位置: L1465-1579
- 役割: 入力のトークンが文字列に一致する範囲を求め、TYPED、SUGGESTED、ALL の方式で [開始, 長さ] の配列にする。小文字化して完全一致を探し、無ければ Intl.Collator で発音記号を無視して照合する。
- 触るとき: 候補の強調位置がずれる時や、発音記号付きの入力が一致しない時。
- 呼び出し先: `hits.fill()`, `hits.indexOf()`, `new Array(str.length).fill()`, `ranges.push()`, `str.indexOf()`, `str.substring()`, `str.substring(0, UrlbarShared.MAX_TEXT_LENGTH).toLocaleLowerCase()`
- 条件付き依存: `if (highlightType == UrlbarShared.HIGHLIGHT.SUGGESTED)` → `str.lastIndexOf()`
- 条件付き依存: `if (!found)` → `str.substr()`
- 条件付き依存: `if (!found)` → `compareIgnoringDiacritics()`
- 条件付き依存: `if (compareIgnoringDiacritics(needle, hay) === 0)` → `hits.fill()`
- 参照: `Intl.Collator`, `UrlbarShared.HIGHLIGHT.ALL`, `UrlbarShared.HIGHLIGHT.SUGGESTED`, `UrlbarShared.MAX_TEXT_LENGTH`, `hits.length`, `needle.length`, `new Intl.Collator("en", { sensitivity: "base", }).compare`, `str.length`, `this._compareIgnoringDiacritics`, `tokens.length`, `tokens?.length`

## addTextContentWithHighlights()
- 位置: L1593-1619
- 役割: ノードのテキストを空にしてから、強調範囲だけを strong 要素で包んで文字列を追加する。
- 触るとき: 候補の強調表示の DOM 構造や、強調範囲の崩れを直す時。
- 呼び出し先: `(highlights || []).concat()`
- 条件付き依存: `if (highlightIndex - index > 0)` → `parentNode.appendChild()`
- 条件付き依存: `if (highlightIndex - index > 0)` → `parentNode.ownerDocument.createTextNode()`
- 条件付き依存: `if (highlightIndex - index > 0)` → `textContent.substring()`
- 条件付き依存: `if (highlightLength > 0)` → `parentNode.ownerDocument.createElement()`
- 条件付き依存: `if (highlightLength > 0)` → `textContent.substring()`
- 条件付き依存: `if (highlightLength > 0)` → `parentNode.appendChild()`
- 参照: `parentNode.textContent`, `strong.textContent`, `textContent.length`

## formatDate()
- 位置: L1663-1753
- 役割: Date を相対表示 (昨日・今日・明日、N 日前、N 週間前、N か月前) か絶対表示 (曜日、月日、年付き) に整形し、未来なら時刻も付ける。
- 触るとき: 検索候補の日付の文言や形式を変える時、または日付表示の不具合を調べる時。
- 呼び出し先: `this.parseDate()`
- 条件付き依存: `if (!forceAbsoluteDate)` → `Math.abs()`
- 条件付き依存: `if (Math.abs(daysAgo) <= 1)` → `new Intl.RelativeTimeFormat(undefined, { numeric: "auto", }).format()`
- 条件付き依存: `if (0 < daysAgo && daysAgo <= 6)` → `new Intl.RelativeTimeFormat(undefined, { numeric: "always", }).format()`
- 条件付き依存: `if (0 < weeksAgo && (weeksAgo <= 4 || monthsAgo == 0))` → `new Intl.RelativeTimeFormat(undefined, { numeric: "always", }).format()`
- 条件付き依存: `if (0 < monthsAgo && monthsAgo <= 11)` → `new Intl.RelativeTimeFormat(undefined, { numeric: "always", }).format()`
- 条件付き依存: `if (capitalizeRelativeDate && formattedDate)` → `formattedDate[0].toLocaleUpperCase()`
- 条件付き依存: `if (capitalizeRelativeDate && formattedDate)` → `formattedDate.substring()`
- 条件付き依存: `if (!formattedDate)` → `new Intl.DateTimeFormat(undefined, opts).format()`
- 参照: `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, `opts.day`, `opts.month`, `opts.weekday`, `opts.year`, `this.DATE_FORMAT_TYPE.ABSOLUTE`, `this.DATE_FORMAT_TYPE.DAYS_WEEKS_MONTHS_AGO`, `this.DATE_FORMAT_TYPE.YESTERDAY_TODAY_TOMORROW`, `zonedDate.year`, `zonedNow.timeZoneId`, `zonedNow.year`

## parseDate()
- 位置: L1796-1832
- 役割: 与えられた Date を、今日との日数差、週数差、月数差と、未来かどうかに変換する。
- 触るとき: 今日、昨日、N 日前などの相対表示が違う時。
- 呼び出し先: `Temporal.ZonedDateTime.compare()`, `date.toTemporalInstant()`, `date.toTemporalInstant().toZonedDateTimeISO()`, `dateDay.subtract()`, `dateDay.with()`, `this._firstDayOfWeek()`, `this._zonedDateTimeISO()`, `thisMonth.since()`, `thisMonth.since(dateMonth).round()`, `thisWeek.since()`, `thisWeek.since(dateWeek).round()`, `today.since()`, `today.since(dateDay).round()`, `today.subtract()`, `today.with()`, `zonedDate.startOfDay()`, `zonedNow.startOfDay()`
- 参照: `dateDay.dayOfWeek`, `thisMonth.since(dateMonth).round({ smallestUnit: "months", relativeTo: thisMonth, }).months`, `thisWeek.since(dateWeek).round({ smallestUnit: "weeks", relativeTo: thisWeek, }).weeks`, `today.dayOfWeek`, `today.since(dateDay).round("days").days`

## _zonedDateTimeISO()
- 位置: L1836-1838
- 役割: 現在時刻を Temporal の ZonedDateTime として返す薄いラッパー。テストで現在時刻を差し替えられる。
- 触るとき: テストで現在時刻を固定したい時や、日付表示の基準になる時刻を変える時。
- 呼び出し先: `Temporal.Now.zonedDateTimeISO()`

## _firstDayOfWeek()
- 位置: L1842-1856
- 役割: ロケールの週の始まりを初回だけ求めてキャッシュし、取得できなければ日曜 (7) にする。
- 触るとき: N 週間前の計算がずれる時や、テストで週の始まりを差し替える時。
- 条件付き依存: `if (this.__firstDayOfWeek === undefined)` → `new Intl.Locale( Intl.DateTimeFormat().resolvedOptions().locale ).getWeekInfo()`
- 条件付き依存: `if (this.__firstDayOfWeek === undefined)` → `Intl.DateTimeFormat().resolvedOptions()`
- 条件付き依存: `if (this.__firstDayOfWeek === undefined)` → `Intl.DateTimeFormat()`
- 参照: `Intl.DateTimeFormat().resolvedOptions().locale`, `Intl.Locale`, `new Intl.Locale( Intl.DateTimeFormat().resolvedOptions().locale ).getWeekInfo().firstDay`, `this.__firstDayOfWeek`

## escapeHtmlEntities()
- 位置: L1864-1871
- 役割: 文字列の & < > " ' を HTML のエンティティに置き換える。null や undefined は空文字として扱う。
- 触るとき: 文字列を HTML に埋め込む箇所で、エスケープ漏れがないかを確かめる時。
- 呼び出し先: `(s || "") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace()`, `(s || "") .replace(/&/g, "&amp;") .replace(/</g, "&lt;") .replace(/>/g, "&gt;") .replace(/"/g, "&quot;") .replace()`

## createLoggerChrome()
- 位置: L1881-1886
- 役割: console.createInstance で、接頭辞と最大レベルの pref を持つロガーを作る。
- 触るとき: chrome 側の urlbar のログに接頭辞やレベル設定が効かない時。
- 呼び出し先: `console.createInstance()`

## createLoggerContent()
- 位置: L1895-1929
- 役割: content 側で global の console を包み、接頭辞と UrlbarPrefs の最大レベルでログを絞るプロキシを作る。
- 触るとき: content プロセスの urlbar のログが出ない原因を探す時。
- 呼び出し先: `maxLogLevelPref.replace()`

## shouldLog()
- 位置: L1912-1917
- 役割: UrlbarPrefs の最大ログレベルと比べて、そのレベルのログを出すかを判定する。最大レベルが不明なら warn とみなす。
- 触るとき: content 側でログが出ない、または出すぎる時に、ログレベル pref の効き方を確かめる時。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarPrefs.get(levelPref).toLowerCase()`
- 参照: `LEVEL_NUMBERS.warn`

## get()
- 位置: L1920-1927
- 役割: console のメソッドを取り出すプロキシの get トラップ。ログレベルの名前は shouldLog を通した関数に置き換え、その他はそのまま返す。
- 触るとき: content 側の console の呼び出しが想定どおりに絞られるかを確かめる時。
- 呼び出し先: `LEVELS.includes()`, `value.bind()`
- 条件付き依存: `if (typeof prop == "string" && LEVELS.includes(prop))` → `shouldLog()`
- 条件付き依存: `if (typeof prop == "string" && LEVELS.includes(prop))` → `target[prop]()`
