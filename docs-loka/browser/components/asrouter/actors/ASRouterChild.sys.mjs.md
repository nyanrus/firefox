# browser/components/asrouter/actors/ASRouterChild.sys.mjs

source: browser/components/asrouter/actors/ASRouterChild.sys.mjs
source-hash: 2f3879e93bc5641072e2626e1681d8f2377190c3
lines: 119

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## ASRouterChild.constructor()
- 位置: L18-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.observers`

## ASRouterChild.didDestroy()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observers.clear()`

## ASRouterChild.actorCreated()
- 位置: L27-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.exportFunction()`, `this.addParentListener.bind()`, `this.asRouterMessage.bind()`, `this.removeParentListener.bind()`
- 参照: `this.contentWindow`

## ASRouterChild.handleEvent()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)

## ASRouterChild.addParentListener()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observers.add()`

## ASRouterChild.removeParentListener()
- 位置: L51-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.observers.delete()`

## ASRouterChild.receiveMessage()
- 位置: L55-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `listener()`, `this.observers.forEach()`
- 参照: `this.contentWindow`

## ASRouterChild.wrapPromise()
- 位置: L74-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `promise.then()`
- 参照: `this.contentWindow.Promise`

## ASRouterChild.sendQuery()
- 位置: L80-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `resolve()`, `super.sendQuery()`, `super.sendQuery(aName, aData).then()`, `this.wrapPromise()`
- 参照: `this.contentWindow`

## ASRouterChild.asRouterMessage()
- 位置: L90-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `VALID_TYPES.has()`
- 条件付き依存: `if (type === "NEWTAB_MESSAGE_REQUEST")` → `this.wrapPromise()`
- 条件付き依存: `if (type === "NEWTAB_MESSAGE_REQUEST")` → `Promise.resolve()`
- 条件付き依存: `if (VALID_TYPES.has(type))` → `this.sendAsyncMessage()`
- 条件付き依存: `if (VALID_TYPES.has(type))` → `this.sendQuery()`
- 参照: `msg.DISABLE_PROVIDER`, `msg.ENABLE_PROVIDER`, `msg.EXPIRE_QUERY_CACHE`, `msg.FORCE_PRIVATE_BROWSING_WINDOW`, `msg.IMPRESSION`, `msg.RESET_PROVIDER_PREF`, `msg.SET_PROVIDER_USER_PREF`, `msg.USER_ACTION`
