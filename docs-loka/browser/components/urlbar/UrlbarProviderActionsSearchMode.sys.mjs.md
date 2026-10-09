# browser/components/urlbar/UrlbarProviderActionsSearchMode.sys.mjs

source: browser/components/urlbar/UrlbarProviderActionsSearchMode.sys.mjs
source-hash: d9d7f9dd834f345d391bc9926cff230bab0e1dac
lines: 147

## <module>
- 役割: アクション検索モードで、利用可能なクイックアクションを一覧として出すプロバイダーを定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderActionsSearchMode.type()
- 位置: L32-34
- 役割: プロバイダー種別として PROFILE を返す。
- 触るとき: アクション検索モードの候補が、どの種別の結果として扱われるかを確かめるとき。
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderActionsSearchMode.isActive()
- 位置: async L36-40
- 役割: searchMode の source が ACTIONS のときだけ有効にする。
- 触るとき: アクション検索モードに入っても一覧が出ない場合に、検索モードの source 判定を確かめるとき。
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `queryContext.searchMode?.source`

## UrlbarProviderActionsSearchMode.startQuery()
- 位置: async L49-71
- 役割: 入力に一致するアクションを取得し、サポート外のものを除いて DYNAMIC の結果として追加する。
- 触るとき: 一覧に出るアクションの絞り込みや並びを変えたい、またはサポート外のアクションが消える条件を調べるとき。
- 呼び出し先: `action.isUnsupported()`, `addCallback()`, `lazy.ActionsProviderQuickActions.getAction()`, `lazy.ActionsProviderQuickActions.getActions()`, `results.forEach()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.trimmedLowerCaseSearchString`, `queryContext.trimmedLowerCaseSearchString.length`

## UrlbarProviderActionsSearchMode.#isActionInactive()
- 位置: L82-84
- 役割: アクションが無効状態(isInactive が真)かどうかを返す。ビューとエンゲージメントの両方で同じ判定を使う。
- 触るとき: 無効表示のボタンが押せてしまう、または表示と実際の挙動が食い違うとき。
- 呼び出し先: `action.isInactive()`

## UrlbarProviderActionsSearchMode.onEngagement()
- 位置: L91-103
- 役割: 選ばれた結果のアクションを取得し、無効でなければ pickAction で実行する。
- 触るとき: アクションを選んだときに何が起きないのか(無効で無視される条件)を調べるとき。
- 呼び出し先: `lazy.ActionsProviderQuickActions.getAction()`, `lazy.ActionsProviderQuickActions.pickAction()`, `this.#isActionInactive()`
- 参照: `details.result.payload`

## UrlbarProviderActionsSearchMode.getViewTemplate()
- 位置: L105-135
- 役割: アクションをボタン状の span として描画するテンプレートを作る。無効なら aria-disabled と disabled を付け、アイコンは既定値にフォールバックする。
- 触るとき: アクションのボタンの見た目や属性(data-action、ロール、無効表示)を変えるとき。
- 呼び出し先: `lazy.ActionsProviderQuickActions.getAction()`, `this.#isActionInactive()`
- 参照: `action.icon`, `result.payload.inputLength`, `result.payload.key`

## UrlbarProviderActionsSearchMode.getViewUpdate()
- 位置: L137-145
- 役割: アクションのラベルを l10n の ID から更新するビュー更新内容を返す。
- 触るとき: アクションの表示名がローカライズされずに出る、またはラベルの ID を差し替えるとき。
- 呼び出し先: `lazy.ActionsProviderQuickActions.getAction()`
- 参照: `action.label`, `result.payload.key`
