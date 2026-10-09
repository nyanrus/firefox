# browser/components/search/BrowserSearchTelemetry.sys.mjs

source: browser/components/search/BrowserSearchTelemetry.sys.mjs
source-hash: f9af3f2bd8c27a5caa30de05bd1c432907d5c754
lines: 419

## <module>
- 役割: 検索の計測(検索回数、アクセスポイント別の計測、Glean による検索報告)を行うハンドラーを提供する
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## BrowserSearchTelemetryHandler.shouldRecordSearchCount()
- 位置: L87-92
- 役割: プライベートウィンドウでは browser.engagement.search_counts.pbm が true のときだけ記録を止める
- 触るとき: プライベートブラウジング中に検索が計測されるかを変えるとき、または記録されない理由を調べるとき
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `browser.documentGlobal`
- XPCOM: `Services.prefs`

## BrowserSearchTelemetryHandler.recordSearchSuggestionSelectionMethod()
- 位置: L103-123
- 役割: 検索候補の選択方法をクリック・候補選択・Enter のいずれかに分けて searchbar の指標に加算する
- 触るとき: 検索バーの候補選択の計測区分を増やすとき。コンテキストメニュー由来の command イベントもクリック扱いになる
- 呼び出し先: `ChromeUtils.getClassName()`, `Glean.searchbar.selectedResultMethod[category].add()`
- 参照: `Glean.searchbar.selectedResultMethod`, `event.type`

## BrowserSearchTelemetryHandler.recordSearchMode()
- 位置: L135-145
- 役割: URL バーの検索モードへの移行を urlbarSearchmode の指標に記録する。プレビューは記録しない
- 触るとき: 検索モードの開始をどう数えるかを変えるとき、またはプレビューで計測が増える不具合を調べるとき
- 呼び出し先: `Glean.urlbarSearchmode[name]?.[label].add()`, `lazy.UrlbarSearchUtils.getSearchModeScalarKey()`, `p.toUpperCase()`, `searchMode.entry.replace()`
- 参照: `Glean.urlbarSearchmode`, `searchMode.isPreview`

## BrowserSearchTelemetryHandler.recordSearch()
- 位置: L179-299
- 役割: 検索 1 件の計測を行う中心の関数。clickUrl があれば検索報告を送り、sap.counts と旧 deprecatedCounts に記録し、source ごとに振り分ける
- 触るとき: 検索の計測値が二重になる、または欠けるとき。内部の例外は握りつぶされて console.error に出るだけなので、ログも併せて見る
- 呼び出し先: `Glean.sap.counts.record()`, `[ "about_home", "about_newtab", "newtab_searchbar", "urlbar_handoff", ].includes()`, `console.error()`, `engine.getURLOfType()`, `isOverridden.toString()`, `source.startsWith()`, `this.#recordSearch()`, `this._handleSearchAndUrlbar()`, `this.shouldRecordSearchCount()`
- 条件付き依存: `if (typeof engine == "string")` → `lazy.SearchService.getEngineById()`
- 条件付き依存: `if (engine.clickUrl)` → `this.#reportSearchInGlean()`
- 条件付き依存: `if (!(source in this.KNOWN_SEARCH_SOURCES))` → `console.error()`
- 条件付き依存: `if (source.startsWith("urlbar"))` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (source.startsWith("urlbar"))` → `Math.round()`
- 条件付き依存: `if (source.startsWith("urlbar"))` → `Date.now()`
- 条件付き依存: `if (source != "contextmenu_visual")` → `engine.aliases.includes()`
- 条件付き依存: `if ( details.alias && engine instanceof lazy.ConfigSearchEngine && engine.aliases.includes(details.alias) )` → `Glean.sap.deprecatedCounts[countIdPrefix + "alias"].add()`
- 条件付き依存: `if (!( details.alias && engine instanceof lazy.ConfigSearchEngine && engine.aliases.includes(details.alias) ))` → `Glean.sap.deprecatedCounts[countIdSource].add()`
- 条件付き依存: `if ( [ "about_home", "about_newtab", "newtab_searchbar", "urlbar_handoff", ].includes(source) )` → `Glean.newtabSearch.issued.record()`
- 条件付き依存: `if ( [ "about_home", "about_newtab", "newtab_searchbar", "urlbar_handoff", ].includes(source) )` → `lazy.SearchSERPTelemetry.recordBrowserNewtabSession()`
- 参照: `Glean.sap.deprecatedCounts`, `details.alias`, `details.newtabSessionId`, `details.searchUrlType`, `details.submission`, `details.submission.partnerCode`, `details.submission?.telemetryId`, `engine.clickUrl`, `engine.getURLOfType(searchUrlType)?.excludePartnerCodeFromTelemetry`, `engine.id`, `engine.name`, `engine.overriddenById`, `engine.partnerCode`, `engine.telemetryId`, `lazy.ConfigSearchEngine`, `lazy.SearchUtils.URL_TYPE.SEARCH`, `this.KNOWN_SEARCH_SOURCES`
- XPCOM: `Services.prefs`

## BrowserSearchTelemetryHandler.recordSearchForm()
- 位置: L310-316
- 役割: 検索エンジンのフォームを開いた訪問を sap.searchFormCounts に記録する。ConfigSearchEngine 以外は other と記録する
- 触るとき: 検索フォームへの訪問の計測を変えるとき、またはラベルが other になる理由を調べるとき
- 呼び出し先: `Glean.sap.searchFormCounts.record()`
- 参照: `engine.id`, `lazy.ConfigSearchEngine`

## BrowserSearchTelemetryHandler.recordSapImpression()
- 位置: L331-343
- 役割: 検索アクセスポイントの表示を sapImpressionCounts に記録する。エンジンが設定版でなければ none と記録する
- 触るとき: アクセスポイントの表示回数が想定外のラベルで数えられているとき
- 呼び出し先: `Glean.sapImpressionCounts[name][label].add()`, `p.toUpperCase()`, `source.replace()`, `this.shouldRecordSearchCount()`
- 条件付き依存: `if (!(source in this.KNOWN_SEARCH_SOURCES))` → `console.error()`
- 参照: `Glean.sapImpressionCounts`, `engine.id`, `lazy.ConfigSearchEngine`, `this.KNOWN_SEARCH_SOURCES`

## BrowserSearchTelemetryHandler._handleSearchAndUrlbar()
- 位置: L358-372
- 役割: URL バーと検索バー由来の source について、one-off、フォーム履歴、候補、エイリアス、通常入力の順に action を決めて #recordSearch に渡す
- 触るとき: URL バーや検索バーからの検索を、どの操作として分類するかを変えるとき
- 呼び出し先: `this.#recordSearch()`
- 参照: `details.alias`, `details.isFormHistory`, `details.isOneOff`, `details.isSuggestion`

## BrowserSearchTelemetryHandler.#recordSearch()
- 位置: L382-388
- 役割: SERP 側へ source を伝え、browserEngagementNavigation の該当する指標に加算する
- 触るとき: 検索の入口ごとのナビゲーション指標に新しい入口を足すとき
- 呼び出し先: `Glean.browserEngagementNavigation[name][label].add()`, `lazy.SearchSERPTelemetry.recordBrowserSource()`, `p.toUpperCase()`, `source.replace()`
- 参照: `Glean.browserEngagementNavigation`

## BrowserSearchTelemetryHandler.#reportSearchInGlean()
- 位置: async L396-415
- 役割: 検索の clickUrl を、contextId を添えて searchWith の Glean ping として送る
- 触るとき: コンテキスト系サービスへの検索報告の中身や送信タイミングを調べるとき
- 呼び出し先: `lazy.ContextId.request()`, `sendGleanPing()`

## sendGleanPing()
- 位置: L401-410
- 役割: contextId と引数の値を searchWith の指標に設定し、ping を送信する。undefined と空文字は設定しない
- 触るとき: searchWith の ping に載る項目を増やすとき
- 呼び出し先: `GleanPings.searchWith.submit()`, `Object.entries()`
- 条件付き依存: `if (value !== undefined && value !== "")` → `glean.set()`
- 参照: `Glean.searchWith`
