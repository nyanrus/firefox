# browser/components/urlbar/UrlbarParentController.sys.mjs

source: browser/components/urlbar/UrlbarParentController.sys.mjs
source-hash: 7be7375183959d9f388b364a955e036164d2739d
lines: 2620

## <module>
- 役割: urlbar の親プロセス側コントローラー(UrlbarParentController)と、エンゲージメントやバウンスなどのテレメトリを記録する TelemetryEvent を定義するモジュール。入力と結果表示の橋渡し、検索・読み込み・タブ切替の実行、テレメトリの記録を親側で担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Promise.resolve()`, `lazy.UrlbarShared.getLogger()`

## engineToEngineInfo()
- 位置: L63-74
- 役割: 検索エンジンを、子プロセスへ送れる素のオブジェクト(名前、ID、別名、一般用途か、新規表示など)に変換する。
- 触るとき: エンジン一覧の表示に項目を足す、またはエンジンの別名や新規表示が子側に出ないときに確かめるとき。
- 呼び出し先: `engine.isNew()`
- 参照: `engine.aliases`, `engine.hideOneOffButton`, `engine.id`, `engine.isGeneralPurposeEngine`, `engine.isNewUntil`, `engine.name`, `lazy.AppProvidedConfigEngine`, `lazy.ConfigSearchEngine`

## UrlbarParentController.constructor()
- 位置: L144-163
- 役割: sapName、プライベート判定、アクターを受け取って ProvidersManager を選ぶ。TelemetryEvent、トップサイトの変更通知、ロケール変更の通知を登録する。sapName が無ければ例外を投げる。
- 触るとき: SAP ごとに検索の経路が変わるのか、テストで偽の manager を差し込めるのかを確かめるとき。
- 呼び出し先: `Services.obs.addObserver()`, `lazy.ProvidersManager.getInstanceForSap()`, `lazy.UrlbarProviderTopSites.addTopSitesListener()`
- 参照: `this.#actor`, `this.#isAddressbar`, `this.#topSitesListener`, `this.engagementEvent`, `this.isPrivate`, `this.manager`, `this.sapName`
- XPCOM: `Services.obs`

## UrlbarParentController.platform()
- 位置: L170-172
- 役割: AppConstants.platform を返す。
- 触るとき: 親側の処理でプラットフォームごとに分岐したいとき。
- 参照: `AppConstants.platform`

## UrlbarParentController.input()
- 位置: L179-181
- 役割: 子コントローラーが持つ入力欄(または転送用のプロキシ)を返す。
- 触るとき: 親側から入力欄の状態を読みたいのに値が取れないとき、子が設定されているかを確かめるとき。
- 参照: `this.#child?.input`

## UrlbarParentController.browserWindow()
- 位置: L190-192
- 役割: アクターの topChromeWindow を返す。親側のプロバイダーがアイコン取得、先読み接続、ヘルプ表示などに使う。
- 触るとき: 親側の処理で window が null になる原因(テスト時や終了中)を追うとき。
- 参照: `this.#actor?.browsingContext?.topChromeWindow`

## UrlbarParentController.rendersInContentProcess()
- 位置: L201-203
- 役割: アクターの browsingContext が内容プロセス側かを返す。
- 触るとき: 内容プロセス側の表示を前提にした分岐が、chrome の urlbar で誤って使われていないかを確かめるとき。
- 参照: `this.#actor?.browsingContext?.isContent`

## UrlbarParentController.resolveTargetBrowser()
- 位置: L215-224
- 役割: 内容プロセス側からなら自分のタブの埋め込み要素を、chrome 側なら browserId で指定されたブラウザを返す。見つからなければ null。
- 触るとき: 読み込み先のタブがずれる、または閉じたタブへ読み込もうとするときに、対象の解決方法を確かめるとき。
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`
- 参照: `browsingContext.top.embedderElement`, `browsingContext?.isContent`, `target?.embedderElement`, `this.#actor?.browsingContext`

## UrlbarParentController.view()
- 位置: L231-233
- 役割: 子コントローラーが持つ表示(または転送用のプロキシ)を返す。
- 触るとき: 親側から結果の表示を操作しようとして表示が取れないとき。
- 参照: `this.#child?.view`

## UrlbarParentController.onBeforeSelection()
- 位置: L245-249
- 役割: 結果の provider に onBeforeSelection を tryMethod で呼ぶ。provider が無ければ何もしない。
- 触るとき: 結果を選ぶ直前に provider 側の準備が走らないとき。
- 呼び出し先: `this.manager .getProvider()`, `this.manager .getProvider(result?.providerName) ?.tryMethod()`
- 参照: `result?.providerName`

## UrlbarParentController.onSelection()
- 位置: L257-261
- 役割: 結果の provider に onSelection を tryMethod で呼ぶ。
- 触るとき: 結果を選んだ後の provider 側の反応を確かめるとき。
- 呼び出し先: `this.manager .getProvider()`, `this.manager .getProvider(result?.providerName) ?.tryMethod()`
- 参照: `result?.providerName`

## UrlbarParentController.getHeuristicResult()
- 位置: async L272-275
- 役割: 渡された文脈でクエリを一度実行し、ヒューリスティックの結果を返す。ビューを開かずに先頭の候補を決める、貼り付けして移動やドロップして移動で使う。
- 触るとき: ビューを開かずに先頭の候補を決める処理を変えたいとき。
- 呼び出し先: `this.manager.startQuery()`
- 参照: `queryContext.heuristicResult`

## UrlbarParentController.resolveFallbackNavigation()
- 位置: async L304-391
- 役割: Enter で選べる結果がないとき、ヒューリスティックを限定的に実行して取得する。失敗したら URI フィックスアップで読み込み先を決める。待っている間にブラウザが移動していたら何もしない。
- 触るとき: 候補が無い状態で Enter を押したときに、検索されるのか、移動されるのか、何も起きないのかを調べるとき。
- 呼び出し先: `Glean.urlbar.heuristicResultMissing.addToDenominator()`, `Glean.urlbar.heuristicResultMissing.addToNumerator()`, `Services.uriFixup.getFixupURIInfo()`, `browser.getAttribute()`, `console.error()`, `gBrowser.getTabForBrowser()`, `lazy.UrlbarUtils.getPostDataString()`, `navigated()`, `parseInt()`, `this.getHeuristicResult()`, `this.resolveTargetBrowser()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_ALLOW_KEYWORD_LOOKUP`, `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `browser.lastLocationChange`, `gBrowser.getTabForBrowser(browser)?.group?.id`, `gBrowser.selectedBrowser`, `lazy.UrlbarQueryContext`, `options.searchMode`, `options.sources`, `preferredURI.spec`, `searchMode.source`, `this.browserWindow`, `this.isPrivate`, `this.sapName`
- XPCOM: [`nsIURIFixup`](../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## navigated()
- 位置: L320-321
- 役割: current の読み込みの場合に、待っている間にブラウザの読み込み位置が変わったかを返す。
- 触るとき: 非同期の待機中に別のページへ移動していたときに、古い結果で操作してしまう条件を確かめるとき。
- 参照: `browser.lastLocationChange`

## UrlbarParentController.startQuery()
- 位置: async L400-437
- 役割: 進行中のクエリを取り消してから、新しいクエリの計時を始め、開始通知を出し、ProvidersManager に渡す。取り消されていなければ完了通知を出す。
- 触るとき: 入力のたびに結果が更新されない、または完了通知が二重に出るとき、クエリの開始と終了の流れを追うとき。
- 呼び出し先: `Glean.urlbar.autocompleteFirstResultTime.start()`, `Glean.urlbar.autocompleteSixthResultTime.start()`, `this.cancelQuery()`, `this.manager.startQuery()`, `this.notify()`
- 条件付き依存: `if ( contextWrapper === this._lastQueryContextWrapper && !contextWrapper.done )` → `this.manager.cancelQuery()`
- 条件付き依存: `if ( contextWrapper === this._lastQueryContextWrapper && !contextWrapper.done )` → `this.notify()`
- 参照: `contextWrapper.done`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_FINISHED`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_STARTED`, `queryContext.firstTimerId`, `queryContext.lastResultCount`, `queryContext.sixthTimerId`, `this._lastQueryContextWrapper`

## UrlbarParentController.recordEngagement()
- 位置: L448-455
- 役割: 子側で作られたエンゲージメントの payload を復元し、TelemetryEvent の recordFromChild に渡す。
- 触るとき: メッセージ経由(内容プロセス側の urlbar)のエンゲージメントが記録されないとき。
- 呼び出し先: `lazy.UrlbarTelemetryUtils.recordedEngagementFromWire()`, `this.engagementEvent.recordFromChild()`
- 参照: `this.liveResults`

## UrlbarParentController.resetEngagement()
- 位置: L461-463
- 役割: TelemetryEvent の状態をリセットする。
- 触るとき: セッションの区切りで前の検索の情報が残るとき。
- 呼び出し先: `this.engagementEvent.reset()`

## UrlbarParentController.startTrackingBuiltBounce()
- 位置: L473-475
- 役割: 子側で作られたバウンスの情報を TelemetryEvent に渡し、追跡を始める。
- 触るとき: 内容プロセス側の New Tab 検索のバウンスイベントが記録されないとき。
- 呼び出し先: `this.engagementEvent.startTrackingBuiltBounce()`

## UrlbarParentController.recordSearchMode()
- 位置: L484-490
- 役割: 検索モードへの移行を BrowserSearchTelemetry に記録する。例外はログに出すだけで続ける。
- 触るとき: 検索モードの利用回数の集計がずれるとき。
- 呼び出し先: `console.error()`, `lazy.BrowserSearchTelemetry.recordSearchMode()`

## UrlbarParentController.recordAutofillBackspace()
- 位置: L500-502
- 役割: オートフィルの URL で Backspace が押された記録を UrlbarUtils に渡す。
- 触るとき: Backspace の連続でオートフィルが一時的に止まる仕組みを追うとき。
- 呼び出し先: `lazy.UrlbarUtils.recordAutofillBackspace()`

## UrlbarParentController.recordAutofillDeletion()
- 位置: L507-509
- 役割: オートフィルの値全体を削除した回数を、Glean の autofillDeletion に1件加える。
- 触るとき: オートフィルの削除の集計が増えない、または二重に数えられるとき。
- 呼び出し先: `Glean.urlbar.autofillDeletion.add()`

## UrlbarParentController.dismissAutofill()
- 位置: async L522-532
- 役割: action が dismiss か forget のときだけ対応する Glean を記録し、UrlbarUtils.dismissAutofill を呼ぶ。forget は履歴からも消す。それ以外の値では例外を投げる。
- 触るとき: オートフィルの候補を消した後に再表示されるか、履歴から消えるかを確かめるとき。
- 呼び出し先: `Glean.urlbarAutofill.inputContextMenuDismissal[action].add()`, `lazy.UrlbarUtils.dismissAutofill()`
- 参照: `Glean.urlbarAutofill.inputContextMenuDismissal`

## UrlbarParentController.clearAutofillBackspaceEntryForUrl()
- 位置: L541-543
- 役割: UrlbarUtils に依頼して、そのオートフィル URL の Backspace の記録を消す。
- 触るとき: 一度 Backspace で止めた URL を受け入れた後も、オートフィルが止まったままになるとき。
- 呼び出し先: `lazy.UrlbarUtils.clearAutofillBackspaceEntryForUrl()`

## UrlbarParentController.handleAutofillReintegration()
- 位置: L554-557
- 役割: オートフィル URL の再統合処理を非同期で始め、その Promise を静的な変数に保持する。テストはこの Promise を待つ。
- 触るとき: オートフィルのブロック解除後の集計が遅れる、またはテストで待ち合わせられないとき。
- 呼び出し先: `this.#doHandleAutofillReintegration()`, `this.#doHandleAutofillReintegration(url).catch()`
- 参照: `UrlbarParentController._lastAutofillReintegrationPromise`, `console.error`

## UrlbarParentController.#doHandleAutofillReintegration()
- 位置: async L559-575
- 役割: 再統合の結果、ブロック中だった場合だけ理由のレベル別の Glean を記録する。バックスペース由来のブロックなら、ブロックからの経過時間も記録する。
- 触るとき: オートフィルの再統合の集計値がおかしいとき、経過時間の計算の基準を確かめるとき。
- 呼び出し先: `Glean.urlbarAutofill.reintegration[level].add()`, `lazy.UrlbarUtils.reintegrateAutofill()`
- 条件付き依存: `if (backspaceBlock)` → `Glean.urlbarAutofill.reintegrationAfterBackspace[ level ].accumulateSingleSample()`
- 条件付き依存: `if (backspaceBlock)` → `Date.now()`
- 参照: `Glean.urlbarAutofill.reintegration`, `Glean.urlbarAutofill.reintegrationAfterBackspace`, `backspaceBlock.blockedAt`

## UrlbarParentController.recordSearchForm()
- 位置: L586-589
- 役割: エンジン ID からエンジンを引き、検索フォームへの訪問を BrowserSearchTelemetry に記録する。
- 触るとき: 検索フォームを開いた回数の集計がずれるとき。
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchForm()`, `lazy.SearchService.getEngineById()`
- 参照: `this.sapName`

## UrlbarParentController.recordSearch()
- 位置: L610-613
- 役割: 選択中のブラウザを求め、検索の記録の処理(#recordSearchForBrowser)に渡す。
- 触るとき: 検索の記録が選択中のタブに付くのか、別のタブに付くのかを確かめるとき。
- 呼び出し先: `this.#recordSearchForBrowser()`
- 参照: `this.browserWindow.gBrowser.selectedBrowser`

## UrlbarParentController.#recordSearchForBrowser()
- 位置: L621-681
- 役割: 検索回数(browser.search.totalSearches、100 で止まる)を増やす。searchbar なら最終利用時刻を保存し、newtab_searchbar なら訪問 ID を付ける。onSearch のトリガーを送り、検索の記録を行い、エンジンが見つかれば非公開でない限り検索語をフォーム履歴に追加する。
- 触るとき: 検索回数や最終利用の時刻が更新されない、または検索語がフォーム履歴に入らないとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `lazy.ASRouter.sendTriggerMessage()`, `lazy.BrowserSearchTelemetry.recordSearch()`, `lazy.SearchService.getEngineById()`
- 条件付き依存: `if (totalSearches < 100)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `new Date().toISOString()`
- 条件付き依存: `if (this.sapName == "newtab_searchbar")` → `lazy.AboutNewTab.getVisitId()`
- 条件付き依存: `if (engine)` → `lazy.UrlbarUtils.addToFormHistory( this.isPrivate || opensInPrivateWindow, query, engine.name ).catch()`
- 条件付き依存: `if (engine)` → `lazy.UrlbarUtils.addToFormHistory()`
- 参照: `console.error`, `details.isOneOff`, `details.isSuggestion`, `details.newtabSessionId`, `engine.name`, `this.#actor.browsingContext.top.embedderElement`, `this.isPrivate`, `this.sapName`
- XPCOM: `Services.prefs`

## UrlbarParentController.recordSearchInOpenedTab()
- 位置: L691-702
- 役割: 次に開かれるタブの TabOpen を一度だけ待ち、そのタブのブラウザに対して検索の記録を行う。
- 触るとき: 新しいタブで開く検索の記録が、開かれた別のタブに付いてしまうように見えるとき。
- 呼び出し先: `this.#recordSearchForBrowser()`, `this.browserWindow.gBrowser.tabContainer.addEventListener()`
- 参照: `tabEvent.target.linkedBrowser`

## UrlbarParentController.recordZeroPrefix()
- 位置: L710-712
- 役割: ゼロ入力の表示、エンゲージメント、放棄のいずれかの回数を、この SAP 名のついた Glean に1件加える。
- 触るとき: ゼロ入力の集計が SAP ごとに合わないとき。
- 呼び出し先: `Glean.urlbarZeroprefix2[kind][this.sapName].add()`
- 参照: `Glean.urlbarZeroprefix2`, `this.sapName`

## UrlbarParentController.checkKeywordURIFixup()
- 位置: L727-738
- 役割: 単一語を検索に変換するときに、URI フィックスアップの DNS 確認を gKeywordURIFixup に任せる。対象は指定のブラウザか、なければ選択中のブラウザ。
- 触るとき: 単一語の検索で、ホストとして開くかを尋ねる案内が出ない、または出すぎるとき。
- 呼び出し先: `lazy.UrlbarUtils.getURIFixupInfo()`, `this.resolveTargetBrowser()`
- 条件付き依存: `if (fixupInfo)` → `this.browserWindow.gKeywordURIFixup.check()`
- 参照: `this.browserWindow.gBrowser.selectedBrowser`, `this.isPrivate`

## UrlbarParentController.cancelQuery()
- 位置: L744-762
- 役割: 完了していないクエリを取り消し、計時を止め、ProvidersManager に取り消しを伝え、取り消しと完了の通知を出す。すでに終わっていれば何もしない。
- 触るとき: 前の検索結果が残る、またはキャンセル後も表示が更新されるとき。
- 呼び出し先: `Glean.urlbar.autocompleteFirstResultTime.cancel()`, `Glean.urlbar.autocompleteSixthResultTime.cancel()`, `this.manager.cancelQuery()`, `this.notify()`
- 参照: `lazy.UrlbarShared.NOTIFICATIONS.QUERY_CANCELLED`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_FINISHED`, `queryContext.firstTimerId`, `queryContext.sixthTimerId`, `this._lastQueryContextWrapper`, `this._lastQueryContextWrapper.done`

## UrlbarParentController.receiveResults()
- 位置: L769-793
- 役割: 結果が1件、6件に達した時点で対応する計時を記録して止める。先頭が変わったら先頭結果の通知を出し、そのあと結果の通知を出して件数を覚える。
- 触るとき: 結果が遅く見える、または先頭結果の通知が出ないとき、計時の記録の位置を確かめるとき。
- 呼び出し先: `this.notify()`
- 条件付き依存: `if (queryContext.lastResultCount < 1 && queryContext.results.length >= 1)` → `Glean.urlbar.autocompleteFirstResultTime.stopAndAccumulate()`
- 条件付き依存: `if (queryContext.lastResultCount < 6 && queryContext.results.length >= 6)` → `Glean.urlbar.autocompleteSixthResultTime.stopAndAccumulate()`
- 条件付き依存: `if (queryContext.firstResultChanged)` → `this.notify()`
- 参照: `lazy.UrlbarShared.NOTIFICATIONS.QUERY_FIRST_RESULT`, `lazy.UrlbarShared.NOTIFICATIONS.QUERY_RESULTS`, `queryContext.firstResultChanged`, `queryContext.firstTimerId`, `queryContext.lastResultCount`, `queryContext.results.length`, `queryContext.sixthTimerId`

## UrlbarParentController.setChild()
- 位置: L802-804
- 役割: 子コントローラーを設定する。クエリが走る前に設定されている必要がある。
- 触るとき: クエリの実行時に子が無くて通知が届かないとき。
- 参照: `this.#child`

## UrlbarParentController.openSERP()
- 位置: L821-845
- 役割: エンジンの検索 URL を作り、openTrustedLinkIn で開く。where が current なら指定の対象ブラウザを使う。
- 触るとき: 検索結果ページを開く場所(今のタブ、新しいタブ)や POST の扱いを変えたいとき。
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.UrlbarUtils.getSearchQueryUrl()`, `this.browserWindow.openTrustedLinkIn()`, `this.resolveTargetBrowser()`
- 参照: `searchEngine.name`, `this.sapName`

## UrlbarParentController.openSearchForm()
- 位置: L859-868
- 役割: 検索フォームの訪問を記録してから、エンジンの検索フォームの URL を開く。
- 触るとき: エンジンのホームやフォームを開く動作を変えたいとき。
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchForm()`, `lazy.SearchService.getEngineById()`, `this.browserWindow.openTrustedLinkIn()`, `this.resolveTargetBrowser()`
- 参照: `searchEngine.searchForm`, `this.sapName`

## UrlbarParentController.openPreferences()
- 位置: L880-882
- 役割: 親ウィンドウの openPreferences に、ペイン ID と追加の引数を渡す。
- 触るとき: 設定画面を開く経路を探すとき。
- 呼び出し先: `this.browserWindow.openPreferences()`

## UrlbarParentController.openContainerCreationPanel()
- 位置: L891-893
- 役割: 親ウィンドウにコンテナー作成パネルを開く。
- 触るとき: コンテナー作成の案内を urlbar の別の入口から出すとき。
- 呼び出し先: `lazy.ContainerCreationPanel.open()`
- 参照: `this.browserWindow`

## UrlbarParentController.getEngineIconURL()
- 位置: async L903-910
- 役割: エンジンを ID で探し、アイコンの URL を取得する。エンジンが無ければ警告を出して null を返す。
- 触るとき: 検索エンジンのアイコンが出ないとき、取得元を追うとき。
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.UrlbarUtils.getEngineIconUrl()`
- 条件付き依存: `if (!engine)` → `lazy.logger.warn()`

## UrlbarParentController.markEngineAsUsed()
- 位置: L918-927
- 役割: 未使用の標準エンジンを使用済みにする。
- 触るとき: エンジンの初回利用をいつ記録するかを変えるとき、使用済みの判定を確かめるとき。
- 呼び出し先: `lazy.SearchService.getEngineById()`
- 条件付き依存: `if (!engine)` → `lazy.logger.warn()`
- 条件付き依存: `if (engine instanceof lazy.ConfigSearchEngine && !engine.hasBeenUsed)` → `engine.markAsUsed()`
- 参照: `engine.hasBeenUsed`, `lazy.ConfigSearchEngine`

## UrlbarParentController.speculativeConnect()
- 位置: L942-1000
- 役割: resultsadded では、先頭がヒューリスティックかオートフィルの候補のときだけ、検索候補なら検索提案が有効な場合に限って先読み接続する。mousedown では http か https の URL にだけ先読み接続する。ウィンドウがない、またはプライベートなら何もしない。
- 触るとき: 先読み接続がどの候補で始まるか、または増えすぎていないかを確かめるとき。
- 呼び出し先: `lazy.UrlbarUtils.getUrlFromResult()`, `url.startsWith()`
- 条件付き依存: `if (result.type == lazy.UrlbarShared.RESULT_TYPE.SEARCH)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( (lazy.UrlbarPrefs.get("suggest.searches") || context.isSearchbarSAP) && lazy.UrlbarPrefs.get("browser.search.suggest.enabled") )` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if ( (lazy.UrlbarPrefs.get("suggest.searches") || context.isSearchbarSAP) && lazy.UrlbarPrefs.get("browser.search.suggest.enabled") )` → `lazy.UrlbarUtils.setupSpeculativeConnection()`
- 条件付き依存: `if (result.autofill)` → `lazy.UrlbarUtils.getUrlFromResult()`
- 条件付き依存: `if (result.autofill)` → `lazy.UrlbarUtils.setupSpeculativeConnection()`
- 条件付き依存: `if (url.startsWith("http"))` → `lazy.UrlbarUtils.setupSpeculativeConnection()`
- 参照: `context.isPrivate`, `context.isSearchbarSAP`, `context.results.length`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `result.autofill`, `result.heuristic`, `result.payload.engine`, `result.type`, `this.browserWindow`

## UrlbarParentController.loadURL()
- 位置: L1030-1085
- 役割: 読み込み先のブラウザを解決し、読み込み要求を URL に変換して、住所欄からの読み込みなら準備処理を行う。current なら対象ブラウザを指定し、新しく開くなら起点のドキュメントを指定する。openTrustedLinkIn で開き、例外が出ても、エラーページが出ていなければ入力欄を戻すように返す。閉じたタブへの current 読み込みは何もせず戻らない。
- 触るとき: URL を読み込む場所や、入力欄が元に戻る条件を変えたいとき、閉じたタブへの読み込みが黙って捨てられる理由を確かめるとき。
- 呼び出し先: `lazy.UrlbarUtils.loadRequestToUrl()`, `this.browserWindow.openTrustedLinkIn()`, `this.resolveTargetBrowser()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.#prepareAddressbarLoad()`
- 条件付き依存: `if (!params.avoidBrowserFocus)` → `browser.focus()`
- 参照: `Cr.NS_ERROR_LOAD_SHOWED_ERRORPAGE`, `browser.browserId`, `ex.result`, `params.avoidBrowserFocus`, `params.initiatedByURLBar`, `params.initiatingDoc`, `params.postData`, `params.targetBrowser`, `this.#isAddressbar`, `this.browserWindow.document`, `this.browserWindow.gBrowser.selectedBrowser`, `this.rendersInContentProcess`

## UrlbarParentController.focusBrowser()
- 位置: L1098-1106
- 役割: 対象ブラウザが選択中のブラウザなら、そのブラウザにフォーカスを移し focused を真で返す。
- 触るとき: Enter で読み込んだ後に、ページへフォーカスが移らないとき。
- 呼び出し先: `this.resolveTargetBrowser()`
- 条件付き依存: `if (browser && browser == selectedBrowser)` → `selectedBrowser.focus()`
- 参照: `this.browserWindow.gBrowser`

## UrlbarParentController.switchToTab()
- 位置: L1128-1172
- 役割: URL を持つタブに切り替える。切り替えられたら、前のタブが空なら閉じ、ヒューリスティックでなければ入力履歴を記録する。見つからなければエラーを出し、開いているタブの登録を外す。
- 触るとき: タブ切り替えの候補を選んだときに、前のタブが閉じるか残るかを確かめるとき。
- 呼び出し先: `Services.io.newURI()`, `console.error()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarProviderOpenTabs.unregisterOpenTab()`, `lazy.UrlbarShared.isNonPrivateUserContextId()`, `this.browserWindow.switchToTabHavingURI()`
- 条件付き依存: `if (!activeSplitView && prevTab.isEmpty)` → `gBrowser.removeTab()`
- 条件付き依存: `if (!heuristic)` → `this.addToInputHistory()`
- 参照: `gBrowser.selectedTab`, `prevTab.isEmpty`, `prevTab.splitview`, `this.browserWindow`, `this.isPrivate`
- XPCOM: `Services.io`

## UrlbarParentController.addToInputHistory()
- 位置: L1193-1201
- 役割: 非公開でなければ、URL と入力された検索語の組を入力履歴に保存する。whenReady のときは、URL が場所の記録に入るまで待ってから書く。失敗はログに出す。
- 触るとき: 入力履歴が増えない、または次の候補の並びに反映されないとき。
- 呼び出し先: `lazy.UrlbarUtils.addToInputHistory()`, `lazy.UrlbarUtils.addToInputHistoryWhenReady()`, `promise.catch()`
- 参照: `console.error`, `this.isPrivate`

## UrlbarParentController.#prepareAddressbarLoad()
- 位置: L1219-1258
- 役割: 住所欄からの読み込みの前に、対象ブラウザの入力値、初期ページの記録、URL の履歴、認証の再試行回数を整える。同じ URL の current 読み込みでは一時的なブロック権限を消す。
- 触るとき: 住所欄から読んだ後に権限が残る、または再読み込みで権限が消えないとき。
- 呼び出し先: `console.error()`, `lazy.UrlbarUtils.addToUrlbarHistory()`, `this.browserWindow.gInitialPages.includes()`
- 条件付き依存: `if ( where == "current" && browser.currentURI && url === browser.currentURI.spec )` → `this.browserWindow.SitePermissions.clearTemporaryBlockPermissions()`
- 参照: `browser.authPromptAbuseCounter`, `browser.currentURI`, `browser.currentURI.spec`, `browser.initialPageLoadedFromUserAction`, `browser.userTypedValue`, `params.triggeringPrincipal`, `params.triggeringPrincipal.isSystemPrincipal`, `this.browserWindow`

## UrlbarParentController.removeResult()
- 位置: L1274-1297
- 役割: ヒューリスティックでない結果を現在のクエリの結果から取り除き、取り除いた通知を出す。取り除けない場合はログに出して何もしない。
- 触るとき: 候補を削除しても別の候補が出てくる、または削除されないとき。
- 呼び出し先: `queryContext.results.findIndex()`, `queryContext.results.splice()`, `this.notify()`
- 条件付き依存: `if (!this._lastQueryContextWrapper)` → `console.error()`
- 条件付き依存: `if (index < 0)` → `console.error()`
- 参照: `lazy.UrlbarShared.NOTIFICATIONS.QUERY_RESULT_REMOVED`, `r.id`, `result.heuristic`, `result.id`, `this._lastQueryContextWrapper`

## UrlbarParentController.setLastQueryContextCache()
- 位置: L1304-1308
- 役割: クエリ文脈をキャッシュし、完了済みとして記録する。取り消しの対象にはならない。
- 触るとき: エンゲージメントがクエリを実行せずに起きたとき、文脈の出どころを確かめるとき。
- 参照: `this._lastQueryContextWrapper`

## UrlbarParentController.clearLastQueryContextCache()
- 位置: L1313-1315
- 役割: キャッシュ済みのクエリ文脈を消す。
- 触るとき: 前の検索の文脈が次の操作に残るとき。
- 参照: `this._lastQueryContextWrapper`

## UrlbarParentController.liveResults()
- 位置: L1323-1325
- 役割: 直前のクエリの結果を返す。無ければ空の配列を返す。
- 触るとき: メッセージ経由で受け取った結果の参照先を調べるとき。
- 参照: `this._lastQueryContextWrapper?.queryContext.results`

## UrlbarParentController.notify()
- 位置: L1334-1347
- 役割: 子が内容プロセス側のプロキシなら、クエリ文脈を直列化して送る。そうでなければ子の通知を直接呼ぶ。
- 触るとき: 通知が内容プロセス側に届かない、または文脈が直列化で壊れるとき。
- 条件付き依存: `if (this.#child.isProxy === true)` → `this.#child.notifyFromWire()`
- 条件付き依存: `if (this.#child.isProxy === true)` → `params.map()`
- 条件付き依存: `if (this.#child.isProxy === true)` → `param.toWire()`
- 条件付き依存: `if (!(this.#child.isProxy === true))` → `this.#child.notify()`
- 参照: `lazy.UrlbarQueryContext`, `this.#child.isProxy`

## UrlbarParentController.destroy()
- 位置: L1357-1363
- 役割: 検索エンジンの変更とロケールの変更の監視を外す。
- 触るとき: コントローラーを捨てた後にも通知が届き続けるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- 条件付き依存: `if (this.#engineObserverRegistered)` → `Services.obs.removeObserver()`
- 参照: `this.#engineObserverRegistered`
- XPCOM: `Services.obs`

## UrlbarParentController.maybeInitEngineStore()
- 位置: L1375-1386
- 役割: 検索サービスが読み込み済みなら、エンジン一覧の初期化を同期的に行い true を返す。読み込まれていなければ false を返す。
- 触るとき: 起動直後にエンジン一覧が空のままになるとき。
- 呼び出し先: `Cu.isESModuleLoaded()`
- 条件付き依存: `if ( Cu.isESModuleLoaded( "moz-src:///toolkit/components/search/SearchService.sys.mjs" ) && lazy.SearchService.isInitialized )` → `this.initEngineStore()`
- 参照: `lazy.SearchService.isInitialized`

## UrlbarParentController.initEngineStore()
- 位置: async L1388-1415
- 役割: 必要なら検索サービスを初期化し、表示対象のエンジン一覧と既定の位置を子に送る。失敗や既定が無ければ error を送る。成功後にエンジンの変更通知の監視を始める。一度しか実行しない。
- 触るとき: 検索エンジンの一覧が表示されない、または既定の位置がずれるとき。
- 呼び出し先: `Services.obs.addObserver()`, `engines.findIndex()`, `engines.map()`, `this.#child.updateEngineStore()`
- 条件付き依存: `if (!lazy.SearchService.hasSuccessfullyInitialized)` → `lazy.SearchService.init()`
- 条件付き依存: `if (!lazy.SearchService.hasSuccessfullyInitialized)` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (!defaultEngine || defaultIndex == -1)` → `this.#child.updateEngineStore()`
- 参照: `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `lazy.SearchService.visibleEngines`, `this.#engineObserverRegistered`, `this.#engineStoreInitStarted`, `this.isPrivate`
- XPCOM: `Services.obs`

## UrlbarParentController.#topSitesListener()
- 位置: L1417-1419
- 役割: トップサイトが変わったら、ビューのトップサイトのキャッシュを消す。
- 触るとき: トップサイトの表示が更新されないとき。
- 呼び出し先: `this.view.clearTopSitesCache()`

## UrlbarParentController.observe()
- 位置: L1431-1443
- 役割: 検索エンジンの変更は #onSearchEngineModified に渡し、ロケールの変更ではビューのローカライズのキャッシュを消す。
- 触るとき: エンジンの変更やロケールの変更の後に表示が古いままになるとき。
- 呼び出し先: `this.#onSearchEngineModified()`, `this.view.clearL10nCache()`

## UrlbarParentController.#onSearchEngineModified()
- 位置: L1449-1485
- 役割: 変更の種類(アイコン変更、追加、変更、削除、既定の変更、非公開の既定の変更)に応じて、子のエンジン一覧を changed、removed、default で更新する。非表示になったエンジンは removed として扱う。
- 触るとき: 検索エンジンの追加・削除・既定の変更が一覧に反映されないとき。
- 呼び出し先: `engineToEngineInfo()`, `sortedEngines.findIndex()`, `this.#child.updateEngineStore()`
- 条件付き依存: `if (!engine.hidden)` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (!(!engine.hidden))` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (!this.isPrivate)` → `this.#child.updateEngineStore()`
- 条件付き依存: `if (this.isPrivate)` → `this.#child.updateEngineStore()`
- 参照: `engine.hidden`, `lazy.SearchService.visibleEngines`, `subject.wrappedJSObject`, `this.isPrivate`

## handleBounceEventTrigger()
- 位置: async L1524-1560
- 役割: タブの追跡中のバウンス情報を取り出し、そのタブでの閲覧時間の合計を求める。合計が 0 でなく、events.bounce.maxSecondsFromLastSearch 秒未満のときだけ記録し、追跡を消す。
- 触るとき: バウンスイベントが記録されない、または閲覧時間の閾値の判定がずれるとき。
- 呼び出し先: `gTrackedBounces.delete()`, `gTrackedBounces.get()`, `gTrackedBounces.has()`, `lazy.Interactions.getRecentInteractionsForBrowser()`, `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if ( totalViewTime != 0 && totalViewTime < lazy.UrlbarPrefs.get("events.bounce.maxSecondsFromLastSearch") * 1000 )` → `tracking.record()`
- 参照: `interaction.created_at`, `interaction.totalViewTime`, `tracking.startTime`

## TelemetryEvent.constructor()
- 位置: L1577-1582
- 役割: コントローラーを保持し、pref のオブザーバーを登録して、テレメトリ用の pref の値を初期化する。
- 触るとき: テレメトリ用の pref の変更が反映されないとき。
- 呼び出し先: `lazy.UrlbarPrefs.addObserver()`, `this.#readPingPrefs()`
- 参照: `this._controller`, `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.start()
- 位置: L1601-1668
- 役割: 一度開始したら後続の入力は無視して最初の操作だけを数える。操作の種類を決め、クエリ文脈をキャッシュする。タブ一覧からの再開は restarted に変える。対象外のイベント種別では記録を始めない。
- 触るとき: エンゲージメントの開始がどの操作で数えられるか、または操作の種類(returned や topsites など)がずれるとき。
- 呼び出し先: `lazy.UrlbarTelemetryUtils.startInteractionType()`, `validEvents.includes()`
- 条件付き依存: `if (this._startEventInfo.interactionType == "topsites")` → `lazy.UrlbarTelemetryUtils.startInteractionType()`
- 条件付き依存: `if (!event)` → `console.error()`
- 条件付き依存: `if (this._controller.sapName === "smartbar")` → `validEvents.push()`
- 条件付き依存: `if (!validEvents.includes(event.type))` → `console.error()`
- 条件付き依存: `if (!this._controller._lastQueryContextWrapper)` → `this._controller.setLastQueryContextCache()`
- 参照: `event.timeStamp`, `event.type`, `this._controller._lastQueryContextWrapper`, `this._controller.sapName`, `this._startEventInfo`, `this._startEventInfo.interactionType`, `this._startEventInfo.searchString`

## TelemetryEvent.record()
- 位置: L1731-1761
- 役割: 同じ呼び出しの再入を防ぎながら内部の記録を行い、セッションが続いていなければ開始情報を消す。例外は console.error に出す。
- 触るとき: 同じセッションが二重に記録される、または記録後も開始情報が残るとき。
- 呼び出し先: `console.error()`, `this.#internalRecord()`
- 参照: `details.isSessionOngoing`, `this.#handlingRecord`, `this._startEventInfo`

## TelemetryEvent.#internalRecord()
- 位置: L1772-1818
- 役割: イベントから状態のスナップショットを作り、エンゲージメントの内容を組み立てる。Suggest 無効化の候補と露出の一覧を添えて recordFromChild に渡す。
- 触るとき: エンゲージメントの内容(選択位置や種別)が記録と違うとき、組み立ての流れを追うとき。
- 呼び出し先: `engagementData.visibleResults.some()`, `lazy.UrlbarTelemetryUtils.buildRecordedDisableCandidate()`, `lazy.UrlbarTelemetryUtils.buildRecordedEngagement()`, `lazy.UrlbarTelemetryUtils.collectSnapshot()`, `this.#resolveExposureList()`, `this.recordFromChild()`
- 参照: `details.isSessionOngoing`, `engagementData.visibleResults`, `r.providerName`, `snapshot.internalDetails`, `snapshot.internalDetails.searchSource`, `snapshot.method`, `this.#engagementData`, `this.#previousSearchWordsSet`, `this.#smartbarData`, `this._controller._lastQueryContextWrapper`, `this._startEventInfo`

## TelemetryEvent.#searchSourceToSap()
- 位置: L1834-1864
- 役割: 検索の出どころ(searchSource)から SAP 名を決める。ウィンドウが閉じかけなら null。新しいタブの URL や拡張機能のページでは専用の SAP を返す。
- 触るとき: テレメトリの sap が想定と違うとき、どの条件で分岐したかを確かめるとき。
- 呼び出し先: `browserWindow.isBlankPageURL()`, `lazy.ExtensionUtils.isExtensionUrl()`
- 参照: `browserWindow.closed`, `browserWindow.gBrowser.currentURI`, `browserWindow.gBrowser.currentURI.spec`, `this._controller.browserWindow`

## TelemetryEvent.#engagementData()
- 位置: L1874-1879
- 役割: 入力欄と表示から、エンゲージメントに必要な検索モード、表示中の結果、表示の開閉、検索の出どころを取り出す。
- 触るとき: エンゲージメントの記録に表示中の結果が入らないとき。
- 呼び出し先: `lazy.UrlbarTelemetryUtils.engagementData()`
- 参照: `this._controller.input`, `this._controller.view`

## TelemetryEvent.#smartbarData()
- 位置: L1886-1888
- 役割: 入力欄からスマートバーのテレメトリ項目(チャット ID、意図、モデル)を取り出す。
- 触るとき: スマートバーのエンゲージメントに意図やモデルが入らないとき。
- 呼び出し先: `lazy.UrlbarTelemetryUtils.smartbarData()`
- 参照: `this._controller.input`

## TelemetryEvent.recordFromChild()
- 位置: L1917-1959
- 役割: 組み立て済みのイベントについて SAP を解決して Glean に記録し、露出の一覧を記録し、Suggest 無効化の追跡を始め、マネージャーにエンゲージメントの変化を通知する。例外は console.error に出す。
- 触るとき: 子プロセス経由のエンゲージメントが記録されない、または露出や無効化の追跡が起きないとき。
- 呼び出し先: `console.error()`, `this.#searchSourceToSap()`, `this._controller.manager.notifyEngagementChange()`
- 条件付き依存: `if (!queryContext)` → `console.error()`
- 条件付き依存: `if (built && sap)` → `this.#fillAndRecord()`
- 条件付き依存: `if (sap && exposures?.length)` → `this.#recordExposureList()`
- 条件付き依存: `if (disableBuilt)` → `this.startTrackingDisableSuggest()`
- 参照: `exposures?.length`, `this._controller`, `this._controller._lastQueryContextWrapper`

## TelemetryEvent.#fillAndRecord()
- 位置: L1971-1986
- 役割: SAP、既定エンジンの telemetryId、エンゲージメントか放棄の場合は利用可能な意味検索の種別を埋めて、Glean に記録する。検索モードのエンゲージメントなら URL 風の検索語の割合も記録する。
- 触るとき: 記録される Glean イベントの項目を増やす、または変えるとき。
- 呼び出し先: `Glean.urlbar[metric].record()`, `lazy.logger.info()`
- 条件付き依存: `if (metric === "engagement" || metric === "abandonment")` → `this.#getAvailableSemanticSources().join()`
- 条件付き依存: `if (metric === "engagement" || metric === "abandonment")` → `this.#getAvailableSemanticSources()`
- 条件付き依存: `if (metric === "engagement" && eventInfo.search_mode)` → `this.#maybeRecordSearchModeUrlLikeQuery()`
- 参照: `Glean.urlbar`, `eventInfo.available_semantic_sources`, `eventInfo.sap`, `eventInfo.search_engine_default_id`, `eventInfo.search_mode`, `lazy.SearchService.defaultEngine.telemetryId`

## TelemetryEvent.#maybeRecordSearchModeUrlLikeQuery()
- 位置: L1996-2010
- 役割: ヒューリスティックが検索結果のエンゲージメントなら分母を1増やし、入力が URL として解釈できる(検索ではない)なら分子も1増やす。ローカルの検索モードは対象外。
- 触るとき: 検索モードでの URL 風の入力の割合が想定と違うとき。
- 呼び出し先: `Glean.urlbarSearchmode.urlLikeQuery.addToDenominator()`
- 条件付き依存: `if (fixupInfo?.href && !fixupInfo.isSearch)` → `Glean.urlbarSearchmode.urlLikeQuery.addToNumerator()`
- 参照: `fixupInfo.isSearch`, `fixupInfo?.href`, `heuristicResult.type`, `heuristicResult?.heuristic`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `queryContext?.heuristicResult`, `this._controller._lastQueryContextWrapper`

## TelemetryEvent.#recordSearchEngagementTelemetry()
- 位置: L2070-2146
- 役割: バウンスなどの検索のエンゲージメントを、検索語の状態と引数から組み立てて Glean に記録する。SAP が決まらなければ何もしない。smartbar で location が無いと例外を投げる。
- 触るとき: バウンスなど検索のエンゲージメントの項目が欠ける、または smartbar で例外が出るとき。
- 呼び出し先: `lazy.UrlbarTelemetryUtils.buildEventInfo()`, `lazy.UrlbarTelemetryUtils.getInteractionType()`, `this.#searchSourceToSap()`
- 条件付き依存: `if (built)` → `this.#fillAndRecord()`
- 参照: `engagementData.searchMode`, `engagementData.viewIsOpen`, `this.#engagementData`, `this.#previousSearchWordsSet`, `this._controller.sapName`

## TelemetryEvent.#getOptionalSmartbarTelemetry()
- 位置: L2156-2162
- 役割: 検索の出どころが smartbar のときだけスマートバーの項目を返す。それ以外は null を返す。
- 触るとき: スマートバー以外の記録にスマートバーの項目が混ざるとき。
- 呼び出し先: `this.#searchSourceToSap()`
- 参照: `this.#smartbarData`

## TelemetryEvent.#getAvailableSemanticSources()
- 位置: L2172-2192
- 役割: 意味検索が使えるかを確かめ、使えれば history を、使えなければ none を含む配列を返す。スマートバーではスマートウィンドウ向けの判定を使う。取得に失敗しても none を返す。
- 触るとき: available_semantic_sources が常に none になるとき、判定に使うマネージャーの状態を確かめるとき。
- 呼び出し先: `lazy.logger.error()`
- 条件付き依存: `if ( isSmartbar ? semanticManager.isEnabledForSmartWindow : semanticManager.canUseSemanticSearch )` → `sources.push()`
- 条件付き依存: `if (!sources.length)` → `sources.push()`
- 参照: `lazy.UrlbarProviderSemanticHistorySearch.semanticManager`, `semanticManager.canUseSemanticSearch`, `semanticManager.isEnabledForSmartWindow`, `sources.length`, `this._controller.sapName`

## TelemetryEvent.#resolveExposureList()
- 位置: L2207-2224
- 役割: キューに溜まった露出を、終端かどうかを付けた記録用の形に変え、露出の一覧と仮の露出を空にする。
- 触るとき: セッション終了時の露出の terminal の値がずれるとき。
- 呼び出し先: `exposures.map()`, `weakResult.get()`
- 条件付き依存: `if (result)` → `this.#exposureResults.delete()`
- 条件付き依存: `if (result)` → `lazy.UrlbarTelemetryUtils.exposureTerminal()`
- 参照: `this.#exposures`, `this.#tentativeExposures`

## TelemetryEvent.#recordExposureList()
- 位置: L2238-2273
- 役割: 露出の一覧から、キーワードのある露出ごとに keyword_exposure を記録し、結果の種別をまとめた露出イベントを1件記録する。キーワード露出があれば urlbar-keyword-exposure の ping を送る。
- 触るとき: 露出の集計や keyword_exposure の ping が送られないとき。
- 呼び出し先: `Glean.urlbar.exposure.record()`, `[...terminalByType].sort()`, `a[0].localeCompare()`, `lazy.logger.debug()`, `terminalByType.set()`, `tuples.map()`, `tuples.map(t => t[0]).join()`, `tuples.map(t => t[1]).join()`
- 条件付き依存: `if (keyword)` → `terminal.toString()`
- 条件付き依存: `if (keyword)` → `lazy.logger.debug()`
- 条件付き依存: `if (keyword)` → `Glean.urlbar.keywordExposure.record()`
- 条件付き依存: `if (keywordExposureRecorded)` → `GleanPings.urlbarKeywordExposure.submit()`

## TelemetryEvent.addExposure()
- 位置: L2288-2292
- 役割: 露出の対象(exposureTelemetry を持つ)の結果を、セッション中の露出に加える。
- 触るとき: 表示した結果が露出として数えられないとき。
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#addExposureInternal()`
- 参照: `result.exposureTelemetry`

## TelemetryEvent.addTentativeExposure()
- 位置: L2304-2311
- 役割: まだ表示が確定していない結果の露出を仮に登録する。確定しないまま終わればどの記録にも残らない。
- 触るとき: 隠し結果の露出の数が、クエリの完了前後で合わないとき。
- 条件付き依存: `if (result.exposureTelemetry)` → `this.#tentativeExposures.push()`
- 条件付き依存: `if (result.exposureTelemetry)` → `Cu.getWeakReference()`
- 参照: `result.exposureTelemetry`

## TelemetryEvent.acceptTentativeExposures()
- 位置: L2318-2329
- 役割: 仮の露出のうち、結果とクエリ文脈がまだ生きているものを正式な露出に変える。
- 触るとき: クエリの完了後に隠し結果の露出が数えられないとき。
- 条件付き依存: `if (this.#tentativeExposures.length)` → `weakResult.get()`
- 条件付き依存: `if (this.#tentativeExposures.length)` → `weakQueryContext.get()`
- 条件付き依存: `if (result && queryContext)` → `this.#addExposureInternal()`
- 参照: `this.#tentativeExposures`, `this.#tentativeExposures.length`

## TelemetryEvent.discardTentativeExposures()
- 位置: L2335-2339
- 役割: 仮の露出を破棄する。
- 触るとき: クエリが取り消されたときに、仮の露出が残っていないか確かめるとき。
- 参照: `this.#tentativeExposures`, `this.#tentativeExposures.length`

## TelemetryEvent.#addExposureInternal()
- 位置: L2341-2357
- 役割: 結果がまだ露出されていなければ、結果の種別とキーワードを求めて露出の一覧に加える。同じ結果は1回だけ数える。
- 触るとき: 同じ結果の露出が二重に数えられるとき。
- 呼び出し先: `this.#exposureResults.has()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposureResults.add()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `lazy.UrlbarTelemetryUtils.exposureEntry()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `this.#exposures.push()`
- 条件付き依存: `if (!this.#exposureResults.has(result))` → `Cu.getWeakReference()`

## TelemetryEvent.discard()
- 位置: L2364-2368
- 役割: 開始されたセッションの情報を消して、そのセッションを記録しない。
- 触るとき: 取り消された操作を記録させたくないとき。
- 参照: `this._startEventInfo`

## TelemetryEvent.reset()
- 位置: L2373-2376
- 役割: 前回の検索語の集合と、Suggest 無効化の追跡の状態を消す。テスト用。
- 触るとき: テストの間で状態が残ってしまうとき。
- 参照: `this.#previousSearchWordsSet`, `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.#readPingPrefs()
- 位置: L2394-2398
- 役割: テレメトリ対象の pref を一つずつ読み、現在の値を Glean に設定する。
- 触るとき: 起動時に ping 用の pref の値が入らないとき。
- 呼び出し先: `Object.keys()`, `this.#recordPref()`
- 参照: `this.#PING_PREFS`

## TelemetryEvent.#recordPref()
- 位置: L2400-2415
- 役割: pref に対応する Glean のメトリックに値を設定する。Suggest 全体、all、sponsored のいずれかが無効になったら Suggest 無効化の処理を呼ぶ。
- 触るとき: Suggest を無効にしたのに disable イベントが出ないとき、pref の値が Glean に反映されないとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (metric)` → `metric.set()`
- 条件付き依存: `if (metric)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get(pref))` → `this.handleDisableSuggest()`
- 参照: `this.#PING_PREFS`

## TelemetryEvent.onPrefChanged()
- 位置: L2417-2419
- 役割: 変わった pref を #recordPref に渡す。
- 触るとき: pref の変更がテレメトリに反映される経路を追うとき。
- 呼び出し先: `this.#recordPref()`

## TelemetryEvent.onNimbusChanged()
- 位置: L2421-2423
- 役割: 変わった Nimbus 変数を #recordPref に渡す。
- 触るとき: Nimbus 変数の変更がテレメトリに反映されないとき。
- 呼び出し先: `this.#recordPref()`

## TelemetryEvent.startTrackingDisableSuggest()
- 位置: L2479-2487
- 役割: Suggest の候補が操作された時刻と、組み立て済みの無効化イベントを保存する。
- 触るとき: Suggest の候補を操作した後に無効化したとき、その記録が付くかを確かめるとき。
- 呼び出し先: `this.getCurrentTime()`
- 参照: `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.handleDisableSuggest()
- 位置: L2489-2505
- 役割: 保存された無効化イベントを、events.disableSuggest.maxSecondsFromLastSearch 秒以内なら記録する。追跡は必ず消す。
- 触るとき: Suggest を無効にしても disable イベントが記録されないとき、秒数の判定を確かめるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#searchSourceToSap()`, `this.getCurrentTime()`
- 条件付き依存: `if (sap)` → `this.#fillAndRecord()`
- 参照: `state.built`, `state.interactionTime`, `state.searchSource`, `this._lastSearchDetailsForDisableSuggestTracking`

## TelemetryEvent.getCurrentTime()
- 位置: L2507-2509
- 役割: ChromeUtils.now() の値を返す。
- 触るとき: テストで時刻を差し替えたい、または経過時間の計算がずれるとき。
- 呼び出し先: `ChromeUtils.now()`

## TelemetryEvent.startTrackingBounceEvent()
- 位置: async L2525-2536
- 役割: バウンス用のスナップショットを作り、タブ内の閲覧時間が分かるまで待って記録する追跡を始める。
- 触るとき: 直接経路(chrome の urlbar)でバウンスが記録されないとき。
- 呼び出し先: `lazy.UrlbarTelemetryUtils.collectBounceSnapshot()`, `this.#recordBounce()`, `this.#searchSourceToSap()`, `this.#startTrackingBounce()`
- 参照: `snapshot.searchSource`, `this.#engagementData.visibleResults`, `this._startEventInfo`

## TelemetryEvent.startTrackingBuiltBounce()
- 位置: async L2548-2559
- 役割: 子側で作られたバウンスについて SAP を解決し、閲覧時間が分かった時点で view_time を入れて記録する。SAP が無ければ何もしない。
- 触るとき: 内容プロセス側のバウンスの閲覧時間(view_time)が入らないとき。
- 呼び出し先: `(viewTime / 1000).toString()`, `this.#fillAndRecord()`, `this.#searchSourceToSap()`, `this.#startTrackingBounce()`
- 参照: `built.eventInfo.view_time`

## TelemetryEvent.#startTrackingBounce()
- 位置: async L2573-2582
- 役割: タブが解決できれば、そのタブに追跡中のバウンスがあれば先に処理してから、今回の追跡を登録する。
- 触るとき: タブごとのバウンス追跡が上書きされる、または残ってしまうとき。
- 呼び出し先: `Date.now()`, `gTrackedBounces.has()`, `gTrackedBounces.set()`, `this._controller.resolveTargetBrowser()`
- 条件付き依存: `if (gTrackedBounces.has(browser))` → `handleBounceEventTrigger()`

## TelemetryEvent.#recordBounce()
- 位置: L2596-2618
- 役割: バウンスのスナップショットと、エンゲージメント時に決めた SAP、閲覧時間を使って、検索のエンゲージメントとして記録する。
- 触るとき: バウンスの記録の項目(閲覧時間や選択位置など)がずれるとき。
- 呼び出し先: `this.#getOptionalSmartbarTelemetry()`, `this.#recordSearchEngagementTelemetry()`
- 参照: `snapshot.action`, `snapshot.location`, `snapshot.numChars`, `snapshot.numWords`, `snapshot.provider`, `snapshot.searchMode`, `snapshot.searchSource`, `snapshot.searchWords`, `snapshot.selIndex`, `snapshot.selType`, `snapshot.startEventInfo`, `snapshot.visibleResults`, `snapshot.windowMode`
