# browser/components/urlbar/UrlbarProviderActionsSearchMode.sys.mjs

source: browser/components/urlbar/UrlbarProviderActionsSearchMode.sys.mjs
source-hash: d9d7f9dd834f345d391bc9926cff230bab0e1dac
lines: 147

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## UrlbarProviderActionsSearchMode.type()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.PROVIDER_TYPE.PROFILE`

## UrlbarProviderActionsSearchMode.isActive()
- 位置: async L36-40
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `queryContext.searchMode?.source`

## UrlbarProviderActionsSearchMode.startQuery()
- 位置: async L49-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.isUnsupported()`, `addCallback()`, `lazy.ActionsProviderQuickActions.getAction()`, `lazy.ActionsProviderQuickActions.getActions()`, `results.forEach()`
- 参照: `lazy.UrlbarResult`, `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `lazy.UrlbarShared.RESULT_TYPE.DYNAMIC`, `queryContext.trimmedLowerCaseSearchString`, `queryContext.trimmedLowerCaseSearchString.length`

## UrlbarProviderActionsSearchMode.#isActionInactive()
- 位置: L82-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.isInactive()`

## UrlbarProviderActionsSearchMode.onEngagement()
- 位置: L91-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ActionsProviderQuickActions.getAction()`, `lazy.ActionsProviderQuickActions.pickAction()`, `this.#isActionInactive()`
- 参照: `details.result.payload`

## UrlbarProviderActionsSearchMode.getViewTemplate()
- 位置: L105-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ActionsProviderQuickActions.getAction()`, `this.#isActionInactive()`
- 参照: `action.icon`, `result.payload.inputLength`, `result.payload.key`

## UrlbarProviderActionsSearchMode.getViewUpdate()
- 位置: L137-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ActionsProviderQuickActions.getAction()`
- 参照: `action.label`, `result.payload.key`
