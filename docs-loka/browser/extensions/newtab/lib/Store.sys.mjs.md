# browser/extensions/newtab/lib/Store.sys.mjs

source: browser/extensions/newtab/lib/Store.sys.mjs
source-hash: ee8e28369eb8a30d83aef5560e1b7bd51b93b25b
lines: 170

## <module>
- 役割: (未記入)

## Store.constructor()
- 位置: L22-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `redux.applyMiddleware()`, `redux.combineReducers()`, `redux.createStore()`, `this._middleware.bind()`
- 参照: `this._messageChannel`, `this._messageChannel.middleware`, `this._middleware`, `this._prefs`, `this._store`, `this.dispatch`, `this.feeds`, `this.getState`, `this.subscribe`

## this.dispatch()
- 位置: L26-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.dispatch()`

## this.getState()
- 位置: L27-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.getState()`

## this.subscribe()
- 位置: L28-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._store.subscribe()`

## Store._middleware()
- 位置: L45-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `next()`
- 条件付き依存: `if (store.onAction)` → `store.onAction()`
- 条件付き依存: `if (store.onAction)` → `console.error()`
- 参照: `action.type`, `store.onAction`, `this.feeds`

## Store.initFeed()
- 位置: L70-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._feedFactories.get()`, `this._feedFactories.get(feedName)()`, `this.feeds.set()`
- 条件付き依存: `if (initAction && feed.onAction)` → `feed.onAction()`
- 参照: `feed.onAction`, `feed.store`

## Store.uninitFeed()
- 位置: L86-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.feeds.delete()`, `this.feeds.get()`
- 条件付き依存: `if (uninitAction && feed.onAction)` → `feed.onAction()`
- 参照: `feed.onAction`

## Store.onPrefChanged()
- 位置: L100-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._feedFactories.has()`
- 条件付き依存: `if (value)` → `this.initFeed()`
- 条件付き依存: `if (!(value))` → `this.uninitFeed()`
- 参照: `this._initAction`, `this._uninitAction`

## Store.init()
- 位置: L123-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feedFactories.has()`, `feedFactories.keys()`, `this._messageChannel.simulateMessagesForExistingTabs()`, `this._prefs.get()`, `this._prefs.observeBranch()`
- 条件付き依存: `if (feedFactories.has(telemetryKey) && this._prefs.get(telemetryKey))` → `this.initFeed()`
- 条件付き依存: `if (pref !== telemetryKey && this._prefs.get(pref))` → `this.initFeed()`
- 条件付き依存: `if (initAction)` → `this.dispatch()`
- 参照: `this._feedFactories`, `this._initAction`, `this._uninitAction`

## Store.uninit()
- 位置: L154-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._prefs.ignoreBranch()`, `this.feeds.clear()`
- 条件付き依存: `if (this._uninitAction)` → `this.dispatch()`
- 参照: `this._feedFactories`, `this._uninitAction`

## Store.getMessageChannel()
- 位置: L166-168
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._messageChannel`
