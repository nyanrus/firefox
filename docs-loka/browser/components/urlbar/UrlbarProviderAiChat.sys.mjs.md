# browser/components/urlbar/UrlbarProviderAiChat.sys.mjs

source: browser/components/urlbar/UrlbarProviderAiChat.sys.mjs
source-hash: 176fcfff0171b8dc3a060608b778480703fe608c
lines: 307

## <module>
- 役割: スマートウィンドウのチャット機能の結果を、urlbar の候補として返すプロバイダーを定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## stringsAreUnrelated()
- 位置: L46-55
- 役割: 一方が他方の部分文字列でなく、長さの差が3文字を超えるときに無関係とみなす。
- 触るとき: 入力が少し変わっただけなのに意図判定がやり直される、または逆に判定が古いままになるとき、デバウンスの条件を確かめるとき。
- 呼び出し先: `Math.abs()`, `str1.includes()`, `str2.includes()`
- 参照: `str1.length`, `str2.length`

## UrlbarProviderAiChat.constructor()
- 位置: L61-63
- 役割: 親クラスの初期化だけを行う。
- 触るとき: コンストラクタで初期化すべき状態を足すかどうかを確かめるとき。
- 呼び出し先: `super()`

## UrlbarProviderAiChat.type()
- 位置: L75-79
- 役割: プロバイダー種別として HEURISTIC を返す。SAP と意図によって振る舞いが変わるため即時のヒューリスティックとして扱い、後で遅らせる。
- 触るとき: チャットの候補が先頭に固定されるのか、後から並び替えられるのかを確かめるとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.HEURISTIC`

## UrlbarProviderAiChat.isActive()
- 位置: async L90-97
- 役割: AI ウィンドウが有効で、入力が3文字以上あり、検索モード外のときだけ有効にする。
- 触るとき: チャット候補が出ない原因が、AI ウィンドウの無効化か文字数の条件かを切り分けるとき。
- 呼び出し先: `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `queryContext.restrictInSearchMode()`
- 参照: `UrlbarProviderAiChat.MIN_CHARS_FOR_CHAT`, `controller.browserWindow`, `queryContext.trimmedSearchString.length`

## UrlbarProviderAiChat.startQuery()
- 位置: async L113-183
- 役割: urlbar 以外の SAP では遅延を入れ、意図を判定する。チャットならヒューリスティックのチャット結果と、直後に既定エンジンの検索結果を追加する。
- 触るとき: 意図判定の結果によって候補がどう出し分けられるか、遅延や並び位置を変えたいとき。
- 呼び出し先: `addCallback()`, `this.#determineIntent()`
- 条件付き依存: `if (!canReturnHeuristicResult)` → `this.logger.info()`
- 条件付き依存: `if (!canReturnHeuristicResult)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (heuristic)` → `lazy.UrlbarSearchUtils.getDefaultEngine()`
- 条件付き依存: `if (heuristic)` → `UrlbarUtils.getEngineIconUrl()`
- 条件付き依存: `if (heuristic)` → `addCallback()`
- 参照: `UrlbarProviderAiChat.CHAT_ICON_URL`, `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.OTHER_LOCAL`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.AI_CHAT`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `new SkippableTimer({ name: "ProviderAiChat", time: lazy.UrlbarPrefs.get("delay"), logger: this.logger, }).promise`, `queryContext.isPrivate`, `queryContext.sapName`, `queryContext.searchString`, `this.logger`, `this.queryInstance`

## UrlbarProviderAiChat.onEngagement()
- 位置: async L190-232
- 役割: SAP に応じて AISmartBar アクターを取得し、入力内容と検出した意図、送信方法を付けて ask を呼ぶ。
- 触るとき: チャットの候補を選んだときに質問がどのような文脈で送られるかを確かめるとき。
- 呼び出し先: `actor.ask()`, `controller.input.getContextPageUrl()`, `controller.input.getResolvedContextWebsites()`, `details.event?.type.startsWith()`
- 条件付き依存: `if (queryContext.sapName == "urlbar")` → `lazy.AIWindow.isAIWindowNewTabPage()`
- 条件付き依存: `if ( selectedBrowser && lazy.AIWindow.isAIWindowNewTabPage(selectedBrowser.currentURI) )` → `selectedBrowser.browsingContext?.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (!( selectedBrowser && lazy.AIWindow.isAIWindowNewTabPage(selectedBrowser.currentURI) ))` → `this.#getSidebarBrowser()`
- 条件付き依存: `if (!( selectedBrowser && lazy.AIWindow.isAIWindowNewTabPage(selectedBrowser.currentURI) ))` → `browser.browsingContext?.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (!(queryContext.sapName == "urlbar"))` → `win.browsingContext?.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (!actor)` → `this.logger.error()`
- 参照: `controller.input.inputField.documentGlobal`, `controller.input.sapLocation`, `queryContext.sapName`, `queryContext.searchString`, `selectedBrowser.currentURI`, `this.#lastIntentEvaluation.intent`, `win.closed`, `win.gBrowser?.selectedBrowser`

## UrlbarProviderAiChat.#getSidebarBrowser()
- 位置: async L234-253
- 役割: サイドバーが閉じていれば開き、AI ウィンドウの読み込み完了を待ってそのブラウザを返す。
- 触るとき: サイドバーに送るべき質問が届かないときや、読み込み待ちの挙動を変えたいとき。
- 呼び出し先: `lazy.AIWindowUI.isSidebarOpen()`, `win.document.getElementById()`
- 条件付き依存: `if (!lazy.AIWindowUI.isSidebarOpen(win))` → `lazy.AIWindowUI.openSidebar()`
- 条件付き依存: `if (browser.currentURI?.spec !== lazy.AIWINDOW_URL)` → `browser.addEventListener()`
- 条件付き依存: `if (browser.currentURI.spec === lazy.AIWINDOW_URL)` → `resolve()`
- 参照: `browser.currentURI.spec`, `browser.currentURI?.spec`, `lazy.AIWINDOW_URL`, `lazy.AIWindowUI.BROWSER_ID`

## UrlbarProviderAiChat.#determineIntent()
- 位置: async L261-297
- 役割: URL らしい入力は navigate とし、それ以外は前回の判定から大きく変わったとき(時間か文字列の差)だけ IntentClassifier で判定し直す。失敗時は search にする。
- 触るとき: チャットと検索の振り分けが不安定なとき、判定の呼び出し頻度やデバウンスの条件を見直すとき。
- 呼び出し先: `Date.now()`, `lazy.UrlbarProviderHeuristicFallback.matchUnknownUrl()`, `stringsAreUnrelated()`
- 条件付き依存: `if ( !intent || Date.now() - this.#lastIntentEvaluation.timestamp > MAX_TIME_FOR_DEBOUNCE_MS || stringsAreUnrelated( queryContext.searchString, this.#lastIntentE...)` → `lazy.IntentClassifier.getPromptIntent()`
- 条件付き依存: `if ( !intent || Date.now() - this.#lastIntentEvaluation.timestamp > MAX_TIME_FOR_DEBOUNCE_MS || stringsAreUnrelated( queryContext.searchString, this.#lastIntentE...)` → `this.logger.error()`
- 条件付き依存: `if ( !intent || Date.now() - this.#lastIntentEvaluation.timestamp > MAX_TIME_FOR_DEBOUNCE_MS || stringsAreUnrelated( queryContext.searchString, this.#lastIntentE...)` → `Date.now()`
- 参照: `queryContext.searchString`, `this.#lastIntentEvaluation`, `this.#lastIntentEvaluation.intent`, `this.#lastIntentEvaluation.queryString`, `this.#lastIntentEvaluation.timestamp`
