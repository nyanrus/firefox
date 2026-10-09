# browser/components/urlbar/UrlbarSearchUtils.sys.mjs

source: browser/components/urlbar/UrlbarSearchUtils.sys.mjs
source-hash: 6dff789de49de7446db5dd1191b2dd39e5803f6e
lines: 490

## <module>
- 役割: urlbar が検索エンジンを参照するための共通処理をまとめ、別名、ドメイン、既定エンジン、SERP 判定の窓口となる UrlbarSearchUtils を定義する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## SearchUtils.constructor()
- 位置: L44-50
- 役割: 初期化 Promise を解決済みにし、オブザーバーとして扱うための QueryInterface を用意する。
- 触るとき: オブザーバーとして登録できる形を変えるとき見る。
- 呼び出し先: `ChromeUtils.generateQI()`, `Promise.resolve()`
- 参照: `this.QueryInterface`, `this._refreshEnginesByAliasPromise`

## SearchUtils.init()
- 位置: async L55-60
- 役割: 初期化を一度だけ _initInternal で走らせ、完了まで待つ。
- 触るとき: 検索エンジンの初期化前に呼ばれた箇所の挙動を調べるとき、この一回限りの初期化を確かめる。
- 条件付き依存: `if (!this._initPromise)` → `this._initInternal()`
- 参照: `this._initPromise`

## SearchUtils.enginesForDomainPrefix()
- 位置: async L76-134
- 役割: 表示可能なエンジンのうち、ドメインが入力の前方一致するものを先に、サブドメインの途中一致のものを後に並べて返す。hideOneOffButton のエンジンは除く。
- 触るとき: ドメイン入力(Tab to Search や トップサイトの検索)で候補エンジンが漏れる、または多すぎるときに見る。matchAllDomainLevels の扱いもここで決まる。
- 呼び出し先: `domain.startsWith()`, `engineSet.has()`, `lazy.SearchService.getVisibleEngines()`, `prefix.toLowerCase()`, `this.init()`
- 条件付き依存: `if (domain.startsWith(prefix) || domain.startsWith("www." + prefix))` → `perfectMatchEngines.push()`
- 条件付き依存: `if (domain.startsWith(prefix) || domain.startsWith("www." + prefix))` → `perfectMatchEngineSet.add()`
- 条件付き依存: `if (matchAllDomainLevels)` → `prefix.includes()`
- 条件付き依存: `if (prefix.includes("."))` → `matchPrefix()`
- 条件付き依存: `if (matchAllDomainLevels)` → `matchPrefix()`
- 条件付き依存: `if (matchAllDomainLevels)` → `domain.substr()`
- 条件付き依存: `if (!engineSet.has(engine))` → `engineSet.add()`
- 条件付き依存: `if (!engineSet.has(engine))` → `engines.push()`
- 参照: `domain.length`, `engine.hideOneOffButton`, `engine.searchUrlDomain`, `engine.searchUrlPublicSuffix.length`

## matchPrefix()
- 位置: L86-93
- 役割: エンジンのホストをドットで分けた各サブドメインについて、入力が前方一致するならその部分一致候補に加える。
- 触るとき: サブドメインの途中一致の判定条件を変えるとき見る。
- 呼び出し先: `engineHost.split()`, `parts.slice()`, `parts.slice(i).join()`, `parts.slice(i).join(".").startsWith()`
- 条件付き依存: `if (parts.slice(i).join(".").startsWith(prefix))` → `partialMatchEngines.push()`
- 参照: `parts.length`

## SearchUtils.engineForAlias()
- 位置: async L151-168
- 役割: 別名を小文字にして _enginesByAlias から引き、検索語が与えられたときは別名の後に空白があるものだけを返す。
- 触るとき: 別名での検索モードへの移行が効かない原因を調べるとき、空白の条件を確かめる。
- 呼び出し先: `Promise.all()`, `alias.toLocaleLowerCase()`, `this._enginesByAlias.get()`, `this.init()`
- 条件付き依存: `if (engine && searchString)` → `lazy.UrlbarUtils.substringAfter()`
- 条件付き依存: `if (engine && searchString)` → `lazy.UrlUtils.REGEXP_SPACES_START.test()`
- 参照: `this._refreshEnginesByAliasPromise`

## SearchUtils.tokenAliasEngines()
- 位置: async L174-194
- 役割: 表示可能なエンジンを優先順に並べ、「@」で始まる別名を持つものだけを {engine, tokenAliases} の配列として返す。
- 触るとき: 「@」入力の候補一覧の元データを変えるとき、またはエンジンの並び順を確かめるとき見る。
- 呼び出し先: `a.startsWith()`, `lazy.SearchService.getVisibleEngines()`, `this.#orderEnginesForAliases()`, `this._aliasesForEngine()`, `this._aliasesForEngine(engine).filter()`, `this.init()`
- 条件付き依存: `if (tokenAliases.length)` → `tokenAliasEngines.push()`
- 参照: `tokenAliases.length`

## SearchUtils.getRootDomainFromEngine()
- 位置: L204-221
- 役割: エンジンの検索 URL のドメインから公開サフィックスを除き、残った最後のラベル(例: 例えば example.com の example)を返す。公開サフィックスが無ければドメインをそのまま返す。
- 触るとき: エンジンの識別名を使う箇所で、サブドメインを含むドメインからどこを取り出すかを確かめるとき見る。
- 呼び出し先: `domain.split()`, `domain.substr()`, `domainParts.pop()`
- 条件付き依存: `if (!suffix)` → `domain.endsWith()`
- 参照: `domain.length`, `engine.searchUrlDomain`, `engine.searchUrlPublicSuffix`, `suffix.length`

## SearchUtils.getDefaultEngine()
- 位置: L229-239
- 役割: 検索サービスの初期化が済んでいなければ null を返し、非公開ウィンドウで別の既定が有効なら非公開用の既定エンジンを、それ以外は通常の既定エンジンを返す。
- 触るとき: 既定エンジンが期待と違う、または初期化前に null が返る問題を調べるとき見る。非公開用の既定の切り替え条件もここで確かめる。
- 参照: `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `lazy.separatePrivateDefault`, `lazy.separatePrivateDefaultUIEnabled`

## SearchUtils.separatePrivateDefaultUIEnabled()
- 位置: L245-247
- 役割: 非公開ウィンドウ用の別の既定エンジンを設定する UI の機能フラグの値を返す。
- 触るとき: 非公開用の既定の設定画面を出す条件を確かめるとき見る。
- 参照: `lazy.separatePrivateDefaultUIEnabled`

## SearchUtils.separatePrivateDefault()
- 位置: L253-255
- 役割: 非公開用に別の既定エンジンが設定されているかどうかの値を返す。
- 触るとき: 非公開ウィンドウで既定を切り替えるかを判断する箇所を調べるとき見る。
- 参照: `lazy.separatePrivateDefault`

## SearchUtils.getSearchModeScalarKey()
- 位置: L267-292
- 役割: 検索モードをテレメトリのキーに変換する。標準エンジンは名前を、Amazon や Wikipedia の各国サイトはまとめて記録し、それ以外の非標準エンジンは other とする。結果種別の場合はその名前に制限種別を足す。
- 触るとき: 検索モードのテレメトリの集計キーを変えるとき、または集計結果の項目名が想定と違うときに見る。
- 条件付き依存: `if (searchMode.engineName)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (!(!(engine instanceof lazy.ConfigSearchEngine)))` → `resultDomain.includes()`
- 条件付き依存: `if (!(resultDomain.includes("amazon.")))` → `resultDomain.endsWith()`
- 条件付き依存: `if (searchMode.source)` → `lazy.UrlbarShared.getResultSourceName()`
- 参照: `engine.searchUrlDomain`, `lazy.ConfigSearchEngine`, `searchMode.engineName`, `searchMode.restrictType`, `searchMode.source`

## SearchUtils.resultIsSERP()
- 位置: L305-315
- 役割: 結果の URL が既知の検索エンジンの SERP として解析できるかを返す。allowedSources が指定され、結果の種別が含まれなければ false を返す。
- 触るとき: 検索結果ページかどうかで履歴の扱いを分ける箇所の判定を変えるとき見る。解析の例外は false として扱う。
- 呼び出し先: `allowedSources?.includes()`, `lazy.SearchService.parseSubmissionURL()`
- 参照: `lazy.SearchService.parseSubmissionURL(result.payload.url) ?.engine`, `result.payload.url`, `result.source`

## SearchUtils.resetInitPromiseForTests()
- 位置: L323-325
- 役割: テスト専用で初期化 Promise を消し、次の init で初期化をやり直させる。
- 触るとき: テストで検索サービスの状態を戻した後に、別名の再構築が必要になったとき使う。本番のコードからは呼ばない。
- 参照: `this._initPromise`

## SearchUtils._initInternal()
- 位置: async L327-331
- 役割: 検索サービスを初期化し、別名の対応表を作り、engine の変更通知の監視を登録する。
- 触るとき: 初期化の順序や、変更通知を受ける条件を変えるとき見る。
- 呼び出し先: `Services.obs.addObserver()`, `lazy.SearchService.init()`, `this._refreshEnginesByAlias()`
- XPCOM: `Services.obs`

## SearchUtils.#orderEnginesForAliases()
- 位置: L349-372
- 役割: 別名が重なるとき勝たせる順に並べる。既定、非公開の既定、アプリ同梱のエンジン、その他の順に重複を除く。
- 触るとき: 同じ別名を持つエンジンのどちらが選ばれるかを変えるとき、またはユーザーの期待と違う結果を調べるとき見る。
- 呼び出し先: `orderedEngines.add()`, `orderedEngines.values()`
- 条件付き依存: `if (engine instanceof lazy.AppProvidedConfigEngine)` → `orderedEngines.add()`
- 参照: `lazy.AppProvidedConfigEngine`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`

## SearchUtils._refreshEnginesByAlias()
- 位置: async L374-385
- 役割: 別名の対応表を作り直し、優先順に並べたエンジンの別名を一つずつ登録する。
- 触るとき: エンジンの追加や既定の変更の後に別名が効かない問題を調べるとき見る。
- 呼び出し先: `lazy.SearchService.getVisibleEngines()`, `this.#addAliasesForEngine()`, `this.#orderEnginesForAliases()`
- 参照: `this._enginesByAlias`

## SearchUtils.#addAliasesForEngine()
- 位置: L393-397
- 役割: エンジンの別名を対応表に登録する。既に同じ別名があれば上書きしない。
- 触るとき: 別名の重複を後勝ちにするか先勝ちにするかを変えるとき見る。
- 呼び出し先: `this._aliasesForEngine()`, `this._enginesByAlias.getOrInsert()`

## SearchUtils.serpsAreEquivalent()
- 位置: L421-434
- 役割: 履歴の SERP の全クエリパラメーターについて、無視するもの以外は生成された SERP と値が同じかを確かめ、同等なら true を返す。
- 触るとき: 履歴の SERP と生成した検索 URL を重複として扱うかどうかの条件を変えるとき見る。オリジンやパスは比べない点に注意する。
- 呼び出し先: `Array.from()`, `Array.from(historyParams.entries()).every()`, `generatedParams.get()`, `historyParams.entries()`, `ignoreParams.includes()`
- 参照: `new URL(generatedSerp).searchParams`, `new URL(historySerp).searchParams`

## SearchUtils._aliasesForEngine()
- 位置: L449-459
- 役割: エンジンの別名を小文字にし、「@」が付いていない別名には「@」付きの版も加えて返す。
- 触るとき: 「@」付きでも別名が効くようにする仕組みを変えるとき見る。
- 呼び出し先: `alias.startsWith()`, `aliasWithCase.toLocaleLowerCase()`, `aliases.push()`, `engine.aliases.reduce()`
- 条件付き依存: `if (!alias.startsWith("@"))` → `aliases.push()`

## SearchUtils.getEngineByName()
- 位置: L468-474
- 役割: 検索サービスの初期化が済んでいなければ null を返し、済んでいれば名前でエンジンを返す。
- 触るとき: エンジン名からの引き当てが失敗する原因を調べるとき見る。
- 呼び出し先: `lazy.SearchService.getEngineByName()`
- 参照: `lazy.SearchService.hasSuccessfullyInitialized`

## SearchUtils.observe()
- 位置: L476-486
- 役割: エンジンの追加、変更、削除、既定の変更の通知を受けたとき、別名の対応表を作り直す。
- 触るとき: エンジン関連の通知の種類を増やしたいとき、またはエンジンの変更が別名に反映されない問題を調べるとき見る。
- 呼び出し先: `this._refreshEnginesByAlias()`
- 参照: `this._refreshEnginesByAliasPromise`
