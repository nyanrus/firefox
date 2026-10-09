# browser/components/urlbar/UrlbarProviderTabToSearch.sys.mjs

source: browser/components/urlbar/UrlbarProviderTabToSearch.sys.mjs
source-hash: 68d96a8de2703d91b1e23cdd2c4184b552f307fc
lines: 383

## <module>
- 役割: 入力が検索エンジンのドメインの前半と一致するとき、そのエンジンで検索を始める結果を出す UrlbarProviderTabToSearch を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderTabToSearch.constructor()
- 位置: L99-101
- 役割: 基底の UrlbarProvider をそのまま初期化するだけのコンストラクターである。
- 触るとき: プロバイダーに初期状態を持たせるとき、ここに処理を足す。
- 呼び出し先: `super()`

## UrlbarProviderTabToSearch.type()
- 位置: L106-108
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: Tab to Search の結果を他の結果種別とどう並べるかを変えるとき見る。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderTabToSearch.isActive()
- 位置: async L117-130
- 役割: 入力が一語で検索モード外、suggest.engines が有効、かつ GlobalActions と文脈検索の候補が出ていないときだけ有効にする。
- 触るとき: ドメイン入力で Tab to Search が出ない、または他の候補と競合して消える問題を調べるとき見る。
- 呼び出し先: `lazy.ActionsProviderContextualSearch.isActive()`, `lazy.UrlbarPrefs.get()`, `queryContext.restrictInSearchMode()`, `this.queryInstance .getProvider()`, `this.queryInstance .getProvider(lazy.UrlbarProviderGlobalActions.name) ?.isActive()`
- 参照: `lazy.UrlbarProviderGlobalActions.name`, `queryContext.searchString`, `queryContext.tokens.length`

## UrlbarProviderTabToSearch.getPriority()
- 位置: L137-139
- 役割: プロバイダーの優先度として 0 を返す。
- 触るとき: Tab to Search 結果を他の候補より前後させたいとき、この値を見直す。

## UrlbarProviderTabToSearch.getViewTemplate()
- 位置: L141-143
- 役割: 表示部品の構造として VIEW_TEMPLATE を返す。
- 触るとき: Tab to Search の表示レイアウトを変えるとき、VIEW_TEMPLATE を見る。

## UrlbarProviderTabToSearch.getViewUpdate()
- 位置: L151-182
- 役割: アイコン、エンジン名、アクションの文言、オンボーディングの説明文を動的結果の表示内容として設定する。汎用エンジンかどうかで文言を分ける。
- 触るとき: 表示文言を変えたいとき、または汎用エンジンと個別エンジンの文言の出し分けを確かめるとき見る。
- 参照: `result.payload.engine`, `result.payload.icon`, `result.payload.isGeneralPurposeEngine`

## UrlbarProviderTabToSearch.onSelection()
- 位置: L193-219
- 役割: オンボーディング結果が選ばれたとき、直前の操作から 5 分以上経っていれば tabToSearch.onboard.interactionsLeft を一つ減らす。
- 触るとき: オンボーディング表示の回数制限が想定より早く減る、または減らない問題を調べるとき、この 5 分の抑止と減算の条件を見る。
- 呼び出し先: `Date.now()`
- 条件付き依存: `if ( result.payload.dynamicType && (!UrlbarProviderTabToSearch.onboardingInteractionAtTime || UrlbarProviderTabToSearch.onboardingInteractionAtTime < Date.now() ...)` → `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (interactionsLeft > 0)` → `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if ( result.payload.dynamicType && (!UrlbarProviderTabToSearch.onboardingInteractionAtTime || UrlbarProviderTabToSearch.onboardingInteractionAtTime < Date.now() ...)` → `Date.now()`
- 参照: `UrlbarProviderTabToSearch.onboardingInteractionAtTime`, `result.payload.dynamicType`

## UrlbarProviderTabToSearch.deferUserSelection()
- 位置: L228-230
- 役割: 最初の結果が届くまでユーザーの選択イベントを保留させるため true を返す。
- 触るとき: 選択操作の取りこぼしや、結果が出る前の選択の扱いを調べるとき見る。

## UrlbarProviderTabToSearch.startQuery()
- 位置: async L239-340
- 役割: 入力から www とスラッシュを除き、公開サフィックスを除いた上でエンジンのドメインと前方一致または途中一致するものを探し、オンボーディング結果か通常の検索結果として追加する。
- 触るとき: ドメイン入力に対する一致の判定(部分一致、閾値、公開サフィックス)を変えるとき見る。オートフィル閾値を満たす場合の satisfiesAutofillThreshold の付与もここで行われる。
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `baseDomain.startsWith()`, `host.includes()`, `host.startsWith()`, `lazy.UrlUtils.looksLikeOrigin()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarSearchUtils.enginesForDomainPrefix()`, `lazy.UrlbarShared.stripPrefixAndTrim()`, `searchStr.includes()`, `searchStr.toLocaleLowerCase()`
- 条件付き依存: `if (searchStr.includes("."))` → `UrlbarUtils.stripPublicSuffixFromHost()`
- 条件付き依存: `if (onboardingInteractionsLeft > 0)` → `addCallback()`
- 条件付き依存: `if (onboardingInteractionsLeft > 0)` → `makeOnboardingResult()`
- 条件付き依存: `if (!(onboardingInteractionsLeft > 0))` → `addCallback()`
- 条件付き依存: `if (!(onboardingInteractionsLeft > 0))` → `makeResult()`
- 条件付き依存: `if (host.includes("." + searchStr.toLocaleLowerCase()))` → `partialMatchEnginesByHost.set()`
- 条件付き依存: `if (baseDomain.startsWith(searchStr))` → `partialMatchEnginesByHost.set()`
- 条件付き依存: `if (partialMatchEnginesByHost.size)` → `lazy.UrlbarProviderAutofill.getTopHostOverThreshold()`
- 条件付き依存: `if (partialMatchEnginesByHost.size)` → `Array.from()`
- 条件付き依存: `if (partialMatchEnginesByHost.size)` → `partialMatchEnginesByHost.keys()`
- 条件付き依存: `if (host)` → `partialMatchEnginesByHost.get()`
- 参照: `engine.searchUrlDomain`, `engines.length`, `partialMatchEnginesByHost.size`, `queryContext.searchString`
- XPCOM: `Services.eTLD`

## makeOnboardingResult()
- 位置: L343-358
- 役割: オンボーディング用の DYNAMIC 型の検索結果を作り、suggestedIndex を 1 にして二行分の枠を取る。
- 触るとき: オンボーディング表示の見た目や枠の大きさを変えるとき見る。
- 呼び出し先: `searchUrlDomainWithoutSuffix()`
- 参照: `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.ICON.SEARCH_GLASS`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`

## makeResult()
- 位置: L360-375
- 役割: 通常の SEARCH 型の Tab to Search 結果を、エンジン名、汎用フラグ、ドメイン表示用の文字列などの payload 付きで作る。
- 触るとき: Tab to Search 結果の payload を増減させるとき見る。
- 呼び出し先: `searchUrlDomainWithoutSuffix()`
- 参照: `engine.isGeneralPurposeEngine`, `engine.name`, `lazy.UrlbarResult`, `lazy.UrlbarShared.ICON.SEARCH_GLASS`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.UrlbarShared.RESULT_TYPE.SEARCH`

## searchUrlDomainWithoutSuffix()
- 位置: L377-382
- 役割: エンジンの検索 URL のドメインから www と公開サフィックスを除いた文字列を返す。
- 触るとき: 結果に表示するドメイン名の形式を変えるとき、または公開サフィックスの除去が意図どおりか確かめるとき見る。
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`, `value.substr()`
- 参照: `engine.searchUrlDomain`, `engine.searchUrlPublicSuffix.length`, `value.length`
