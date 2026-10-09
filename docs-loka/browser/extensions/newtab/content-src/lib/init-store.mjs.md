# browser/extensions/newtab/content-src/lib/init-store.mjs

source: browser/extensions/newtab/content-src/lib/init-store.mjs
source-hash: 98edb45eaf8e5ce6beb5b70e4edf2810f9367836
lines: 175

## <module>
- 役割: (未記入)

## mergeStateReducer()
- 位置: L35-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mainReducer()`
- 参照: `action.data`, `action.type`

## messageMiddleware()
- 位置: L48-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.isSendToMain()`
- 条件付き依存: `if (au.isSendToMain(action))` → `RPMSendAsyncMessage()`
- 条件付き依存: `if (!skipLocal)` → `next()`
- 参照: `action.meta`, `action.meta.skipLocal`

## widgetsOptInMiddleware()
- 位置: L70-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `next()`
- 条件付き依存: `if (action.type === at.WIDGETS_OPT_IN)` → `dispatch()`
- 条件付き依存: `if (action.type === at.WIDGETS_OPT_IN)` → `ac.SetPref()`
- 条件付き依存: `if (size)` → `dispatch()`
- 条件付き依存: `if (size)` → `ac.SetPref()`
- 参照: `action.data?.widgets`, `action.type`, `at.WIDGETS_OPT_IN`

## rehydrationMiddleware()
- 位置: L87-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `au.isBroadcastToContent()`, `au.isSendToOneContent()`, `au.isSendToPreloaded()`, `next()`
- 条件付き依存: `if (getState.didRehydrate || window.__FROM_STARTUP_CACHE__)` → `next()`
- 条件付き依存: `if (isRehydrationRequest)` → `next()`
- 条件付き依存: `if (isMergeStoreAction)` → `next()`
- 条件付き依存: `if (getState.didRequestInitialState && action.type === at.INIT)` → `next()`
- 条件付き依存: `if (getState.didRequestInitialState && action.type === at.INIT)` → `ac.AlsoToMain()`
- 参照: `action.meta`, `action.meta.isStartup`, `action.type`, `at.INIT`, `at.NEW_TAB_STATE_REQUEST`, `getState.didRehydrate`, `getState.didRequestInitialState`, `window.__FROM_STARTUP_CACHE__`

## initStore()
- 位置: L146-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `applyMiddleware()`, `combineReducers()`, `createStore()`, `mergeStateReducer()`
- 条件付き依存: `if (globalThis.RPMAddMessageListener)` → `globalThis.RPMAddMessageListener()`
- 条件付き依存: `if (globalThis.RPMAddMessageListener)` → `store.dispatch()`
- 条件付き依存: `if (globalThis.RPMAddMessageListener)` → `console.error()`
- 条件付き依存: `if (globalThis.RPMAddMessageListener)` → `dump()`
- 条件付き依存: `if (globalThis.RPMAddMessageListener)` → `JSON.stringify()`
- 参照: `ex.stack`, `globalThis.RPMAddMessageListener`, `msg.data`
