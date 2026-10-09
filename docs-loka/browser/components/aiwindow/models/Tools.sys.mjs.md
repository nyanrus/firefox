# browser/components/aiwindow/models/Tools.sys.mjs

source: browser/components/aiwindow/models/Tools.sys.mjs
source-hash: 8d47e4d3093669626ce086a0eecd76043f372104
lines: 1821

## <module>
- 役割: LLM ツールの定義と実装をまとめたモジュール。タブ一覧、履歴検索、ページ本文取得、検索実行、メモリ、AI タブ生成、タブ操作などのツール関数を提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `console.createInstance()`

## getEmbeddingsGenerator()
- 位置: L93-98
- 役割: 汎用の EmbeddingsGenerator を初回だけ生成し、以後は同じインスタンスを返す。
- 触るとき: タブ順位付けに使う埋め込みモデルの初期化タイミングや取得方法を変えるとき。
- 条件付き依存: `if (!_embeddingsGenerator)` → `EmbeddingsGenerator.forGeneral()`

## embedTexts()
- 位置: async L100-103
- 役割: テキスト配列を embedMany で埋め込みベクトルにし、結果の output(無ければ結果そのもの)を返す。
- 触るとき: get_open_tabs の topic 順位付けで埋め込みの戻り値の形が変わり、読み取りに失敗していると疑うとき。
- 呼び出し先: `getEmbeddingsGenerator()`, `getEmbeddingsGenerator().embedMany()`
- 参照: `result.output`

## keywordRecall()
- 位置: L105-117
- 役割: トピックのトークンのうち、タイトルのトークン集合に含まれる割合(0〜1)を返す。トピックが空なら 0。
- 触るとき: get_open_tabs の語彙一致スコアの計算を変えるとき。埋め込みスコアとの重み KEYWORD_WEIGHT と合わせて見る。
- 呼び出し先: `titleTokens.has()`
- 参照: `topicTokens.size`

## selectSearchTheWebPath()
- 位置: L189-199
- 役割: search_the_web の実行経路(answers、fast、grounded)を prefs から決める。answers はカスタムエンドポイントでは選ばれない。
- 触るとき: search_the_web の経路を切り替える pref の優先順位を変えるとき、またはカスタムエンドポイント利用時に answers が選ばれない理由を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `openAIEngine.usesCustomEndpoint()`
- 参照: `SEARCH_THE_WEB_PATH.ANSWERS`, `SEARCH_THE_WEB_PATH.FAST`, `SEARCH_THE_WEB_PATH.GROUNDED`
- XPCOM: `Services.prefs`

## searchTheWebToolConfig()
- 位置: L351-360
- 役割: 選ばれた経路に応じたツール定義(answers または fast)を返し、grounded なら null を返す。
- 触るとき: 経路ごとにモデルへ渡す search_the_web のパラメータ(context の有無など)を変えるとき。null のときは既存の toolsConfig が使われる。
- 呼び出し先: `selectSearchTheWebPath()`
- 参照: `SEARCH_THE_WEB_PATH.ANSWERS`, `SEARCH_THE_WEB_PATH.FAST`

## getTabList()
- 位置: L636-667
- 役割: AI ウィンドウ内のタブを最終アクセスの新しい順に並べ、上限件数まで {url, title, lastAccessed, windowId} を返す。
- 触るとき: タブ一覧に含める条件(http(s) 以外や新規タブの除外)や件数上限を変えるとき。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `tabs.slice()`, `tabs.sort()`
- 条件付き依存: `if (!win.closed && win.gBrowser)` → `lazy.SessionStore.getWindowId()`
- 条件付き依存: `if (!win.closed && win.gBrowser)` → `isAllowedURLProtocol()`
- 条件付き依存: `if (!win.closed && win.gBrowser)` → `isNewPageUrl()`
- 条件付き依存: `if (isAllowedURLProtocol(url) && !isNewPageUrl(url))` → `tabs.push()`
- 条件付き依存: `if (isAllowedURLProtocol(url) && !isNewPageUrl(url))` → `sanitizeUntrustedContent()`
- 参照: `a.lastAccessed`, `b.lastAccessed`, `browser?.currentURI?.spec`, `lazy.BrowserWindowTracker.orderedWindows`, `tab.label`, `tab.lastAccessed`, `tab.linkedBrowser`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## getOpenTabs()
- 位置: async L690-752
- 役割: 開いているタブを返す。topic 指定時は埋め込みとキーワード一致の混合スコアで並べ替え、失敗時は最終アクセス順のまま返す。
- 触るとき: get_open_tabs の順位付けや返す件数を変えるとき。topic 検索で無関係なタブが上位に来る原因を調べるときも見る。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation.addSeenUrls()`, `conversation.securityProperties.setPrivateData()`, `getTabList()`, `lazy.console.log()`, `recentTabs.map()`, `tabs.slice()`
- 条件付き依存: `if (topic)` → `ChromeUtils.now()`
- 条件付き依存: `if (topic)` → `tabs.map()`
- 条件付き依存: `if (topic)` → `SmartTabGroupingManager.preprocessText()`
- 条件付き依存: `if (topic)` → `_embeddingFunctions.embedTexts()`
- 条件付き依存: `if (topic)` → `tokenizer.tokenize()`
- 条件付き依存: `if (topic)` → `cosSim()`
- 条件付き依存: `if (topic)` → `_embeddingFunctions.keywordRecall()`
- 条件付き依存: `if (topic)` → `scored.sort()`
- 条件付き依存: `if (topic)` → `tabs.push()`
- 条件付き依存: `if (topic)` → `scored.map()`
- 条件付き依存: `if (topic)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (topic)` → `lazy.console.warn()`
- 参照: `a.score`, `b.score`, `recentTabs.length`, `s.tab`, `t.title`, `tabs.length`

## searchBrowsingHistory()
- 位置: async L780-825
- 役割: 履歴検索を実装側へ委譲し、結果を会話の閲覧済み URL と履歴表示用データに登録したうえで、モデル向けには重いフィールドを除いた結果を返す。
- 触るとき: search_browsing_history がモデルに返す項目を増減するとき。サムネイルなどがモデルに渡らないことを確認するときにも見る。
- 呼び出し先: `conversation.addHistoryResults()`, `conversation.addSeenUrls()`, `conversation.securityProperties.setPrivateData()`, `implSearchBrowsingHistory()`, `lazy.console.log()`, `result.results.map()`, `sanitizeUntrustedContent()`
- 参照: `result.results`

## RunSearch.#ensureTabSelected()
- 位置: L836-840
- 役割: 対象タブが選択されていなければ、その所属ウィンドウで selectedTab を切り替える。
- 触るとき: run_search の前に元のタブを前面に出す処理を変えるとき。
- 参照: `tab.documentGlobal.gBrowser.selectedTab`, `tab.selected`

## RunSearch.runSearch()
- 位置: async L848-927
- 役割: 既定の検索エンジンで検索し SERP の本文を返す。query が無ければ直近のユーザー発言を使い、元タブを選んで検索し、会話に機微データと未信頼入力を記録する。
- 触るとき: run_search の入力検証や失敗文言を変えるとき、または検索後に履歴の戻る操作が飛ばされないよう hasUserInteraction を立てている処理を変えるとき。
- 呼び出し先: `RunSearch.#extractSerpContent()`, `RunSearch.#performSearchAndWait()`, `RunSearch.#showSearchingIndicator()`, `console.error()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `lazy.AIWindow.isAIWindowContentPage()`, `lazy.console.log()`, `query.trim()`, `sh.getEntryAtIndex()`, `win.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (!(toolParams.query))` → `ChatStore.getMostRecentMessages()`
- 条件付き依存: `if (targetTab)` → `RunSearch.#ensureTabSelected()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowContentPage(originalBrowser.currentURI))` → `RunSearch.#moveToSidebarIfNeeded()`
- 条件付き依存: `if (lazy.AIWindow.isAIWindowContentPage(originalBrowser.currentURI))` → `RunSearch.#ensureTabSelected()`
- 参照: `MESSAGE_ROLE.USER`, `browsingContext.embedderElement`, `browsingContext.topChromeWindow`, `e.message`, `entry.hasUserInteraction`, `originalBrowser.browsingContext?.sessionHistory`, `originalBrowser.currentURI`, `recentUserMessages.length`, `recentUserMessages[0].content.body`, `sh.index`, `toolParams.query`, `win.closed`

## RunSearch.#showSearchingIndicator()
- 位置: L939-956
- 役割: サイドバーの ai-window 要素に検索中表示を出し入れする。要素が無い場合や例外時は何もしない。
- 触るとき: 検索中インジケータが出ない、または消えないという表示の不具合を調べるとき。コメントにある通り廃止候補でもある。
- 呼び出し先: `aiBrowser.contentDocument.querySelector()`, `sidebar.querySelector()`, `win.document.getElementById()`
- 条件付き依存: `if (aiWindow?.showSearchingIndicator)` → `aiWindow.showSearchingIndicator()`
- 参照: `aiBrowser?.contentDocument`, `aiWindow?.showSearchingIndicator`

## RunSearch.#moveToSidebarIfNeeded()
- 位置: async L958-960
- 役割: 元タブが AI Window のコンテンツページなら、その会話をサイドバーへ移す。
- 触るとき: 検索を始めるときに AI Window ページをサイドバーへ退避させる挙動を変えるとき。
- 呼び出し先: `lazy.AIWindow.moveConversationToSidebar()`

## RunSearch.#performSearchAndWait()
- 位置: async L969-1007
- 役割: 検索を開始し、読み込み完了の通知を最大 15 秒待ち、サイドバーへフォーカスを戻してから 2 秒描画を待つ。
- 触るとき: 検索結果の読み込み待ちがタイムアウトする、または描画途中の SERP を読んでしまう問題を調べるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `lazy.AIWindow.focusSidebar()`, `lazy.AIWindow.performSearch()`, `lazy.setTimeout()`, `reject()`, `win.gBrowser.addProgressListener()`, `win.gBrowser.removeProgressListener()`
- 参照: `RunSearch.CONTENT_SETTLE_MS`, `RunSearch.NAVIGATION_TIMEOUT_MS`

## RunSearch.onStateChange()
- 位置: L981-990
- 役割: STATE_STOP かつ STATE_IS_NETWORK を受けると、タイムアウトを解除してリスナーを外し、読み込み完了として解決する。
- 触るとき: 検索結果の読み込み完了と判定する状態の組み合わせを変えるとき。
- 条件付き依存: `if ((stateFlags & complete) === complete)` → `lazy.clearTimeout()`
- 条件付き依存: `if ((stateFlags & complete) === complete)` → `win.gBrowser.removeProgressListener()`
- 条件付き依存: `if ((stateFlags & complete) === complete)` → `resolve()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## RunSearch.onLocationChange()
- 位置: L991-991
- 役割: 進捗通知のうち位置変更を受け取るが、何もしない空の実装。
- 触るとき: 検索の進行を位置変更で判定する必要が出たとき、ここに処理を足す。

## RunSearch.onProgressChange()
- 位置: L992-992
- 役割: 進捗通知を受け取るが、何もしない空の実装。
- 触るとき: 進捗率で検索状態を判定する必要が出たとき、ここに処理を足す。

## RunSearch.onStatusChange()
- 位置: L993-993
- 役割: ステータス通知を受け取るが、何もしない空の実装。
- 触るとき: 読み込みのステータス文言を検索処理で使う必要が出たとき、ここに処理を足す。

## RunSearch.onSecurityChange()
- 位置: L994-994
- 役割: セキュリティ状態の通知を受け取るが、何もしない空の実装。
- 触るとき: 証明書やセキュリティ状態によって検索結果の扱いを変える必要が出たとき、ここに処理を足す。

## RunSearch.onContentBlockingEvent()
- 位置: L995-995
- 役割: コンテンツブロックの通知を受け取るが、何もしない空の実装。
- 触るとき: ブロック発生時に検索を中断する処理を足すとき、ここに書く。

## RunSearch.#extractSerpContent()
- 位置: async L1016-1046
- 役割: SERP の PageExtractor でテキストとリンクを取り、リンクを閲覧済みと匿名取得候補に登録して、URL 付きの検索結果文字列を返す。
- 触るとき: 検索結果をモデルへ渡す形式や文字数上限(15000)を変えるとき、または SERP のリンクが後続の get_page_content で匿名取得される条件を追うとき。
- 呼び出し先: `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `pageExtractor.getText()`, `windowContext.getActor()`
- 参照: `RunSearch.MAX_CHARACTERS`, `browser.browsingContext?.currentWindowContext`, `browser.currentURI?.spec`, `result.links`, `result.text`

## raceAbort()
- 位置: L1058-1082
- 役割: promise と AbortSignal のうち先に決まった方で待ちを終える。中断時は AbortError で reject し、中断後に遅れて来た失敗は握りつぶす。
- 触るとき: ページ読み取りなどの非同期処理に中断(タイムアウトやキャンセル)を効かせるとき。
- 呼び出し先: `promise.catch()`, `promise.then()`, `reject()`, `resolve()`, `signal.addEventListener()`, `signal.removeEventListener()`
- 条件付き依存: `if (signal.aborted)` → `onAbort()`
- 参照: `signal.aborted`

## onAbort()
- 位置: L1065-1065
- 役割: 中断シグナルが発火したとき、AbortError の DOMException で待ちを reject する。
- 触るとき: 中断時のエラー名を変えるとき。呼び出し側は name で判定しているので影響範囲を確認する。
- 呼び出し先: `reject()`

## GetPageContent.getPageContentText()
- 位置: async L1101-1107
- 役割: getPageContent の結果から content だけを取り出した文字列の配列を返す。失敗した URL は失敗文がそのまま入る。
- 触るとき: テキストだけ必要な呼び出し元を追加するとき。成功と失敗を区別する必要があるなら getPageContent を使う。
- 呼び出し先: `GetPageContent.getPageContent()`, `results.map()`
- 参照: `result.content`

## GetPageContent.getPageContent()
- 位置: async L1124-1207
- 役割: url_list の各 URL を並列に読み、{url, ok, content} を入力順で返す。不許可 URL、タイムアウト、ブロックはそれぞれ固定の文言で ok を false にする。
- 触るとき: get_page_content の結果形式や失敗時の文言を変えるとき。再試行しないよう指示する文言もここにある。
- 呼び出し先: `Array.isArray()`, `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `GetPageContent.#getPageContentsForSingleURL()`, `Promise.all()`, `console.error()`, `conversation.getAllMentionURLs()`, `isAllowedURLProtocol()`, `lazy.console.log()`, `url_list.map()`
- 条件付き依存: `if (error?.name === "TimeoutError")` → `lazy.console.log()`
- 条件付き依存: `if (error?.name === "BlockedError")` → `lazy.console.log()`
- 参照: `error?.name`, `signal?.aborted`

## GetPageContent.isContentAllowed()
- 位置: L1218-1251
- 役割: URL の本文をこの会話で読んでよいか判定する。http(s) 以外は不可、開いているタブかメンション済みの URL は可、未信頼入力と機微データが両方ある会話では SERP 由来以外の URL を不可にする。
- 触るとき: 本文取得の経路を新しく足すとき、または読めない理由を会話状態から調べるとき。AI タブの og:image 取得も同じ判定を使う。
- 呼び出し先: `GetPageContent.getTabWithURL()`, `conversation.getAllMentionURLs()`, `conversation.getAllMentionURLs().has()`, `conversation.serpUrlsForAnonymousFetch.has()`, `isAllowedURLProtocol()`
- 参照: `conversation.securityProperties.privateData`, `conversation.securityProperties.untrustedInput`

## GetPageContent.getTabWithURL()
- 位置: L1259-1273
- 役割: AI Window の全タブから URL が完全一致するタブを探し、最初に見つかったものを返す。無ければ null。
- 触るとき: 開いているタブの本文を、ヘッドレス取得せずに読む分岐を変えるとき。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `tab?.linkedBrowser?.currentURI?.spec`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## GetPageContent.#getPageContentsForSingleURL()
- 位置: async L1285-1370
- 役割: 開いているタブがあればその PageExtractor で、無ければヘッドレス取得で本文を読む。未信頼かつ機微な会話では、メンション済みでも SERP 由来でもない URL を拒否する。
- 触るとき: 本文取得の経路(タブ、匿名取得、通常のヘッドレス)を追加や変更するとき。「Access is not allowed」が出る条件を調べるときにも見る。
- 呼び出し先: `GetPageContent.getTabWithURL()`, `PageExtractorParent.getHeadlessExtractor()`, `mentionedUrls.has()`
- 条件付き依存: `if (!currentWindowContext)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if (tab)` → `currentWindowContext.getActor()`
- 条件付き依存: `if (tab)` → `GetPageContent.#runExtraction()`
- 条件付き依存: `if (tab)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if ( !mentionedUrls.has(url) && conversation.securityProperties.untrustedInput && conversation.securityProperties.privateData )` → `conversation.serpUrlsForAnonymousFetch.has()`
- 条件付き依存: `if (conversation.serpUrlsForAnonymousFetch.has(url))` → `PageExtractorParent.getHeadlessExtractor()`
- 参照: `conversation.securityProperties.privateData`, `conversation.securityProperties.untrustedInput`, `signal?.aborted`, `tab.label`, `tab.linkedBrowser.browsingContext?.currentWindowContext`

## callback()
- 位置: L1338-1346
- 役割: SERP 由来 URL の匿名取得(anonymousFetch)用ヘッドレス抽出器に渡すコールバックで、#runExtraction を呼ぶ。
- 触るとき: 匿名取得の結果の扱いを変えるとき。
- 呼び出し先: `GetPageContent.#runExtraction()`

## callback()
- 位置: L1360-1368
- 役割: 通常のヘッドレス抽出器に渡すコールバックで、#runExtraction を呼ぶ。
- 触るとき: ヘッドレス取得で得た本文の後処理を変えるとき。
- 呼び出し先: `GetPageContent.#runExtraction()`

## GetPageContent.#runExtraction()
- 位置: async L1389-1434
- 役割: PageExtractor で本文を読み、リンクを閲覧済みに登録し、会話を機微かつ未信頼として記録する。空の本文は失敗扱いにし、成功時は Content from ラベル付きの文字列を返す。
- 触るとき: 抽出の文字数上限(10000)や本文の前置き形式を変えるとき、または本文が空と判定される理由を調べるとき。
- 呼び出し先: `conversation.addSeenUrls()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `pageExtractor.getText()`, `raceAbort()`, `text?.trim()`
- 参照: `GetPageContent.MAX_CHARACTERS`

## getNavigationInfo()
- 位置: async L1445-1457
- 役割: クエリが空なら空配列、それ以外は Firefox 設定の案内候補を関連度順に返す。会話状態は使わない。
- 触るとき: 設定案内の候補内容や照合方法を変えるとき。
- 呼び出し先: `lazy.SmartWindowNavigationInfo.getRelevantNavigation()`, `query.trim()`

## getUserMemories()
- 位置: async L1465-1475
- 役割: 保存済みメモリの要約一覧を返し、会話を機微データ扱いにする。
- 触るとき: モデルに渡すメモリの項目を変えるとき、またはメモリを参照した後に会話の安全フラグがどう変わるかを確認するとき。
- 呼び出し先: `conversation.securityProperties.setPrivateData()`, `lazy.MemoriesManager.getAllMemories()`, `lazy.console.log()`, `memories.map()`
- 参照: `memory.memory_summary`

## addMemory()
- 位置: async L1488-1513
- 役割: 未信頼入力がある会話や個人情報を含むメモリは保存せず、それ以外は MemoriesManager に保存して分類を非同期で追記する。
- 触るとき: メモリ保存の条件(未信頼入力、個人情報判定)を変えるとき。
- 呼び出し先: `lazy.MemoriesManager.enrichExistingMemory()`, `lazy.MemoriesManager.enrichExistingMemory( result.memory.id, memorySummary ).catch()`, `lazy.MemoriesManager.saveRequestedMemory()`, `lazy.console.error()`, `lazy.console.log()`
- 参照: `conversation.securityProperties.untrustedInput`, `result.action`, `result.memory`, `result.memory.id`, `result.memory.memory_summary`, `result.ok`, `result.reason`

## persistAITabPage()
- 位置: async L1530-1561
- 役割: 生成した AI タブを新規作成するか、既存 slug の次版として更新し、更新時は古い版を削除して保存された行を返す。
- 触るとき: AI タブの保存形式や版管理を変えるとき。古い版を消す理由と失敗時の扱いはコメントを参照する。
- 呼び出し先: `lazy.AITabStore.deleteVersionsBefore()`, `lazy.AITabStore.deleteVersionsBefore(stored.slug, stored.version).catch()`, `lazy.AITabStore.edit()`, `lazy.console.error()`
- 条件付き依存: `if (!isModification)` → `lazy.AITabStore.create()`
- 参照: `conversation.id`, `e.message`, `metadata.id`, `metadata.title`, `stored.slug`, `stored.version`

## createAITab()
- 位置: async L1580-1657
- 役割: AITab でページを生成して保存し、閲覧用 URL をトークン化してモデル向けの文と UI データを組み立てる。失敗時は作成または更新できなかった旨の文を返す。
- 触るとき: AI タブのツール結果文やモデルに返す slug と uuid を変えるとき、または保存失敗時の表示を調べるとき。
- 呼び出し先: `JSON.stringify()`, `conversation.addSeenUrls()`, `conversation.convertUrlToToken()`, `lazy.AITab.buildViewerURL()`, `lazy.AITab.generateAITab()`, `lazy.console.error()`, `lazy.console.log()`, `modify_slug.trim()`, `persistAITabPage()`, `sanitizeUntrustedContent()`
- 参照: `UI_TYPES.AITAB`, `e.message`, `result.error`, `result.metadata?.title`, `stored.slug`, `stored.uuid`

## getSkill()
- 位置: async L1661-1663
- 役割: 指定名のスキルのプロンプトを getSkillPrompt で取得して返す。
- 触るとき: get_skill の参照先や、どのモデル向けに取得するかを変えるとき。
- 呼び出し先: `getSkillPrompt()`
- 参照: `toolParams?.name`

## countOpenAIWindowTabs()
- 位置: L1671-1685
- 役割: AI Window 内の http(s) の通常タブ数を数える。
- 触るとき: browser_action_submit の tabs_open テレメトリの定義を変えるとき。
- 呼び出し先: `isAllowedURLProtocol()`, `isNewPageUrl()`, `lazy.AIWindow.isAIWindowActive()`
- 参照: `lazy.BrowserWindowTracker.orderedWindows`, `tab.linkedBrowser?.currentURI?.spec`, `win.closed`, `win.gBrowser`, `win.gBrowser.tabs`

## getActionTrigger()
- 位置: L1694-1701
- 役割: manage_tabs の action が未対応なら unsupported、会話にメンションがあれば tab_mention、無ければ description を返す。
- 触るとき: manage_tabs のテレメトリ上の発動経路の分類を変えるとき。
- 呼び出し先: `TAB_ACTIONS.includes()`, `conversation.getLatestUserMentionCount()`

## manageTabs()
- 位置: async L1718-1809
- 役割: manage_tabs の入力を検証してテレメトリを記録し、問題なければ manageTabsAction に渡す。未対応の action、url_tokens の不正、有効な URL なしは即エラーを返す。
- 触るとき: manage_tabs の入力チェックや失敗時の返答を変えるとき、またはタブ操作の確認(ask_confirmation)に進む条件を確認するとき。
- 呼び出し先: `Array.isArray()`, `TAB_ACTIONS.includes()`, `conversation.getLatestUserMentionCount()`, `countOpenAIWindowTabs()`, `getActionTrigger()`, `isAllowedURLProtocol()`, `lazy.ToolUITelemetry.recordBrowserActionSubmit()`, `manageTabsAction()`, `url_tokens.filter()`
- 条件付き依存: `if (actionTrigger === "unsupported")` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 条件付き依存: `if (!Array.isArray(url_tokens))` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 条件付き依存: `if (!validUrls.size)` → `lazy.ToolUITelemetry.recordBrowserActionComplete()`
- 参照: `conversation.id`, `conversation.lastSubmitType`, `conversation.messageCount`, `conversation.systemPromptVersion`, `validUrls.size`
