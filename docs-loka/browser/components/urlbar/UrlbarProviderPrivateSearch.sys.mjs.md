# browser/components/urlbar/UrlbarProviderPrivateSearch.sys.mjs

source: browser/components/urlbar/UrlbarProviderPrivateSearch.sys.mjs
source-hash: 1d1ed7e40e9c5016d9e83d5056e3ad3e907244b6
lines: 125

## <module>
- 役割: 通常ウィンドウのユーザーに、プライベートウィンドウ用の検索エントリー(プライベート既定エンジンでの検索)を出すプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderPrivateSearch.constructor()
- 位置: L29-31
- 役割: プロバイダーを生成する(super のみ)。
- 触るとき: コンストラクタに初期状態を足すときのみ。
- 呼び出し先: `super()`

## UrlbarProviderPrivateSearch.type()
- 位置: L36-38
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: プライベート検索結果の種別と並び順を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderPrivateSearch.isActive()
- 位置: async L47-53
- 役割: プライベート既定検索の UI が有効で、現在のウィンドウがプライベートでなく、トークンがあるときに起動する。
- 触るとき: プライベート検索候補を出す条件を変えるとき。
- 参照: `lazy.UrlbarSearchUtils.separatePrivateDefaultUIEnabled`, `queryContext.isPrivate`, `queryContext.tokens.length`

## UrlbarProviderPrivateSearch.startQuery()
- 位置: async L63-123
- 役割: 検索制限トークンを除いた検索語で、検索モードのエンジンまたはプライベート既定エンジンを選ぶ。100ms の待機後にアイコンを取り、suggestedIndex 1 で検索結果を追加する。
- 触るとき: プライベート検索の表示遅延(フリッカー防止)、既定エンジンの選び方、表示される検索語を変えるとき。
- 呼び出し先: `UrlbarUtils.getEngineIconUrl()`, `addCallback()`, `lazy.SearchService.getDefault()`, `lazy.SearchService.getDefaultPrivate()`, `lazy.SearchService.getEngineByName()`, `queryContext.tokens.some()`, `this.logger.info()`
- 条件付き依存: `if ( queryContext.tokens.some( t => t.type == lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH ) )` → `queryContext.tokens .filter(t => t.type != lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH) .map(t => t.value) .join()`
- 条件付き依存: `if ( queryContext.tokens.some( t => t.type == lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH ) )` → `queryContext.tokens .filter(t => t.type != lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH) .map()`
- 条件付き依存: `if ( queryContext.tokens.some( t => t.type == lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH ) )` → `queryContext.tokens .filter()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarSearchUtils.separatePrivateDefault`, `lazy.UrlbarShared.HIGHLIGHT.TYPED`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`, `lazy.UrlbarShared.TOKEN_TYPE.RESTRICT_SEARCH`, `new SkippableTimer({ name: "ProviderPrivateSearch", time: 100, logger: this.logger, }).promise`, `queryContext.searchMode.engineName`, `queryContext.searchMode?.engineName`, `queryContext.tokens.length`, `queryContext.trimmedSearchString`, `t.type`, `t.value`, `this.logger`, `this.queryInstance`
