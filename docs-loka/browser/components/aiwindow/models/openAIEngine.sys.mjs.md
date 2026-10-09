# browser/components/aiwindow/models/openAIEngine.sys.mjs

source: browser/components/aiwindow/models/openAIEngine.sys.mjs
source-hash: ae91b41e84d3292d5516a6880a99c30527f61aad
lines: 510

## <module>
- 役割: AIウィンドウのLLM呼び出しを担う openAIEngine クラスを定義する。エンドポイントの選択、FxAccountトークンの取得、エラーの分類、401時のトークン再取得と再試行を扱う。
- 呼び出し先: `XPCOMUtils.declareLazy()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## openAIEngine.hasCustomEndpoint()
- 位置: L104-106
- 役割: 独自エンドポイントのprefにユーザー設定の値があるかを返す。
- 触るとき: 独自エンドポイントが設定されているかで表示や機能を分けるとき。
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## openAIEngine.isCustomEndpoint()
- 位置: L113-115
- 役割: このインスタンスの接続先が既定のエンドポイントと違うかを返す。
- 触るとき: 独自エンドポイントの時に401の再取得を止める判定など、接続先による分岐を調べるとき。
- 参照: `openAIEngine.endpoint`, `this.#baseURL`

## openAIEngine.usesCustomEndpoint()
- 位置: L128-133
- 役割: 独自モデルの選択か、エンドポイントのpref上書きがあれば、プロファイル全体として独自エンドポイントを使うと判定する。エンジンを作らずに判定できる。
- 触るとき: Mozilla提供のサービスに頼る機能を、独自エンドポイントの時に隠すかを決めるとき。
- 呼び出し先: `Services.prefs.getStringPref()`
- 参照: `openAIEngine.endpoint`
- XPCOM: `Services.prefs`

## openAIEngine.resolveEndpointConfig()
- 位置: L142-154
- 役割: 独自モデルの選択なら独自のエンドポイントとAPIキーを返し、未設定なら例外を投げる。それ以外は既定のエンドポイントとキー無しを返す。
- 触るとき: モデルの選択ごとに接続先が変わらない、または独自設定の例外が出るとき。
- 条件付き依存: `if (modelChoiceId === CUSTOM_MODEL_CHOICE_ID)` → `Services.prefs.getStringPref()`
- 参照: `openAIEngine.endpoint`
- XPCOM: `Services.prefs`

## openAIEngine.build()
- 位置: async L169-199
- 役割: インスタンスを作り、機能とモデルからエンジンIDを組み立て、エンジン本体を生成して返す。
- 触るとき: LLMの接続を新しく作る箇所の引数や、エンジンIDの決まり方を調べるとき。
- 呼び出し先: `openAIEngine.#createOpenAIEngine()`
- 参照: `engine.#apiKey`, `engine.#baseURL`, `engine.#engineId`, `engine.#flowId`, `engine.#purpose`, `engine.#serviceType`, `engine.engineInstance`, `engine.feature`, `engine.model`, `openAIEngine.endpoint`

## openAIEngine.getFxAccountToken()
- 位置: async L206-217
- 役割: FxAccountsからスマートウィンドウとプロフィールの範囲のOAuthトークンを取る。失敗時は警告を出してnullを返す。
- 触るとき: LLMや検索のリクエストに認証が付かないと調べるとき、要求する範囲を変えるとき。
- 呼び出し先: `console.warn()`, `fxAccounts.getOAuthToken()`, `lazy.getFxAccountsSingleton()`

## openAIEngine.is429Error()
- 位置: L226-231
- 役割: エラーのstatusが429か、メッセージに429の文字列が含まれるかで判定する。
- 触るとき: レート制限時に待機させる処理を追うとき、429の判定を増やすとき。
- 呼び出し先: `error.message?.includes()`
- 参照: `error.status`

## openAIEngine.isRetryableError()
- 位置: L241-265
- 役割: 429と408、409、5xxの応答、ネットワーク層の失敗を再試行可能と判定する。400番台の他のエラーは再試行しない。
- 触るとき: 一時的な失敗で再試行させるか決めるとき、新しいエラーの種類を再試行の対象に加えるとき。
- 呼び出し先: `/NS_ERROR_(NET_|CONNECTION|PROXY)|NetworkError|connection (refused|reset)|timed? ?out/i.test()`, `Number()`, `error.message?.match()`, `isRetryableStatus()`, `this.is429Error()`
- 参照: `error.message`, `error.name`, `error.status`

## isRetryableStatus()
- 位置: L248-249
- 役割: HTTPステータスが408、409、500から599のいずれかかを判定する。
- 触るとき: 再試行対象のステータスを変えるとき。

## openAIEngine.#createOpenAIEngine()
- 位置: async L280-322
- 役割: 追加ヘッダーのprefをJSONとして読み、失敗時はprefを消して空にする。その後、createEngineに接続先、キー、モデル、ヘッダーなどを渡してエンジンを生成する。
- 触るとき: エンジン生成時に渡す値や、追加ヘッダーの扱いを変えるとき。
- 呼び出し先: `JSON.parse()`, `Services.prefs.clearUserPref()`, `Services.prefs.getStringPref()`, `console.error()`, `openAIEngine._createEngine()`
- XPCOM: `Services.prefs`

## openAIEngine.run()
- 位置: async L331-333
- 役割: メッセージを、401時の再試行付きのrunに渡す。
- 触るとき: 非ストリーミングのLLM呼び出しの入口を追うとき。
- 呼び出し先: `this._runWithAuth()`

## openAIEngine._runWithAuth()
- 位置: async L341-384
- 役割: エンジンでrunを実行し、401なら独自エンドポイントでない場合に限り、古いトークンを捨ててエンジンを作り直し、新しいトークンで1回だけ再実行する。再度401なら新しいトークンも捨てて投げる。
- 触るとき: 401の再試行の挙動を変えるとき、トークンの失効が効かないと調べるとき。
- 呼び出し先: `console.warn()`, `lazy.getFxAccountsSingleton()`, `openAIEngine.getFxAccountToken()`, `this._is401Error()`, `this._recreateEngine()`, `this.engineInstance.run()`
- 条件付き依存: `if (oldToken)` → `fxAccounts.removeCachedOAuthToken()`
- 条件付き依存: `if (newToken)` → `fxAccounts.removeCachedOAuthToken()`
- 参照: `content.fxAccountToken`, `this.isCustomEndpoint`

## openAIEngine._recreateEngine()
- 位置: async L392-408
- 役割: 保存しておいたエンジンIDや接続先などを使って、エンジンを作り直す。IDかサービス種別が無ければ警告して何もしない。
- 触るとき: エンジンの再生成で必要な情報が欠けて再試行が効かないと調べるとき。
- 呼び出し先: `openAIEngine.#createOpenAIEngine()`
- 条件付き依存: `if (!this.#engineId || !this.#serviceType)` → `console.warn()`
- 参照: `this.#apiKey`, `this.#baseURL`, `this.#engineId`, `this.#flowId`, `this.#purpose`, `this.#serviceType`, `this.engineInstance`, `this.feature`, `this.model`

## openAIEngine._is401Error()
- 位置: L417-423
- 役割: エラーのstatusが401か、メッセージに401の文字列が含まれるかで判定する。
- 触るとき: 認証エラーの判定を変えるとき。
- 呼び出し先: `error.message?.includes()`
- 参照: `error.status`

## openAIEngine._runWithGeneratorAuth()
- 位置: async L431-488
- 役割: ストリーミングの応答を1チャンクずつ流し、中断されていれば止める。401の時は_runWithAuthと同じく、トークンを捨てて作り直し、新しいトークンで流し直す。
- 触るとき: ストリーミング応答の途中で止まる、または401の再試行が二重に起きると調べるとき。
- 呼び出し先: `console.warn()`, `lazy.getFxAccountsSingleton()`, `openAIEngine.getFxAccountToken()`, `this._is401Error()`, `this._recreateEngine()`, `this.engineInstance.runWithGenerator()`
- 条件付き依存: `if (oldToken)` → `fxAccounts.removeCachedOAuthToken()`
- 条件付き依存: `if (newToken)` → `fxAccounts.removeCachedOAuthToken()`
- 参照: `options.fxAccountToken`, `signal?.aborted`, `this.isCustomEndpoint`

## openAIEngine.runWithGenerator()
- 位置: L497-499
- 役割: ストリーミングの呼び出しを_runWithGeneratorAuthに渡し、非同期ジェネレーターを返す。
- 触るとき: 会話や検索の回答をストリーミングで受け取る入口を追うとき。
- 呼び出し先: `this._runWithGeneratorAuth()`
