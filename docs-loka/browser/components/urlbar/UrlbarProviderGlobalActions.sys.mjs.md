# browser/components/urlbar/UrlbarProviderGlobalActions.sys.mjs

source: browser/components/urlbar/UrlbarProviderGlobalActions.sys.mjs
source-hash: 60029b53c6e7ff23447d0b9207e33d31d9887d3b
lines: 231

## <module>
- 役割: 全体のアクション(検索アクション、クイックアクション、タブグループ等)を 1 行の動的結果にまとめて表示するプロバイダー。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderGlobalActions.type()
- 位置: L54-56
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: アクション行の種別と並び順を確認するとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderGlobalActions.isActive()
- 位置: async L65-72
- 役割: scotchBonnet または secondaryActions の機能フラグ、もしくは sapName が searchbar のとき、かつ suggest.quickactions が有効なら起動する。
- 触るとき: アクション行を出す条件(フラグや検索バーからの呼び出し)を変えるとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `queryContext.sapName`

## UrlbarProviderGlobalActions.startQuery()
- 位置: async L81-127
- 役割: 登録済みの各アクションプロバイダーで isActive を確認し、queryActions の結果を集め、上限件数まで切り詰めて動的結果を 1 件追加する。
- 触るとき: アクションの集約方法、上限数(maxActionsShown)、オンボーディングラベルの表示条件を変えるとき。
- 呼び出し先: `actionsResults.some()`, `addCallback()`, `lazy.UrlbarPrefs.get()`, `provider.isActive()`
- 条件付き依存: `if (provider.isActive(queryContext))` → `actionsResults.push()`
- 条件付き依存: `if (provider.isActive(queryContext))` → `provider.queryActions()`
- 条件付き依存: `if (actionsResults.length > lazy.UrlbarPrefs.get(MAX_ACTIONS_PREF))` → `lazy.UrlbarPrefs.get()`
- 参照: `a.key`, `actionsResults.length`, `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `lazy.UrlbarShared.RESULT_SOURCE.TABS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.restrictSource`, `queryContext.searchString`, `queryContext.searchString.length`

## UrlbarProviderGlobalActions.onEngagement()
- 位置: async L134-141
- 役割: 選ばれたアクションキーに対応するアクションプロバイダーを探し、その onPick へ処理を渡す。
- 触るとき: アクションを選んだときの実行先を追加・変更するとき。
- 呼び出し先: `details.result.payload.actionsResults.find()`, `globalActionsProviders.find()`, `provider.onPick()`
- 参照: `a.key`, `action.providerName`, `details.pickedActionKey`, `p.name`

## UrlbarProviderGlobalActions.onSearchSessionEnd()
- 位置: L148-161
- 役割: オンボーディングラベルが表示されていれば表示回数を 1 増やし、各アクションプロバイダーの onSearchSessionEnd を呼ぶ。
- 触るとき: オンボーディングラベルを何回表示するかを変えるとき、またはセッション終了時の後処理を追加するとき。
- 呼び出し先: `provider.onSearchSessionEnd()`, `queryContext.results?.find()`
- 条件付き依存: `if (showOnboardingLabel)` → `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if (showOnboardingLabel)` → `lazy.UrlbarPrefs.get()`
- 参照: `queryContext.results?.find( r => r.providerName == this.name )?.payload.showOnboardingLabel`, `r.providerName`, `this.name`

## UrlbarProviderGlobalActions.getViewTemplate()
- 位置: L163-214
- 役割: アクションごとにボタン(アイコン、ラベル、data-action 属性、検索モード関連の属性)を持つ表示テンプレートを作る。
- 触るとき: アクション行のボタンの DOM 構造や属性を変えるとき。
- 呼び出し先: `result.payload.actionsResults.map()`
- 条件付き依存: `if (result.payload.showOnboardingLabel)` → `children.unshift()`
- 参照: `action.dataset?.immediateSearch`, `action.dataset?.providesSearchMode`, `action.engine`, `action.icon`, `action.key`, `action.style`, `btn.attributes`, `btn.style`, `result.payload.inputLength`, `result.payload.showOnboardingLabel`

## UrlbarProviderGlobalActions.getViewUpdate()
- 位置: L216-229
- 役割: オンボーディングラベルと各アクションのラベルを l10n ID と引数で更新する。
- 触るとき: アクション行のラベル文言の出し方を変えるとき。
- 呼び出し先: `result.payload.actionsResults.forEach()`
- 参照: `action.l10nArgs`, `action.l10nId`, `result.payload.showOnboardingLabel`
