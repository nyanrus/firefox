# browser/extensions/newtab/lib/NewTabMessaging.sys.mjs

source: browser/extensions/newtab/lib/NewTabMessaging.sys.mjs
source-hash: 4b6c99a03363eba18d88eacd2332f8a01d7c9700
lines: 206

## <module>
- 役割: (未記入)

## NewTabMessaging.constructor()
- 位置: L16-20
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.ASRouterDispatch`, `this.browserSet`, `this.initialized`

## NewTabMessaging.init()
- 位置: L22-28
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.initialized)` → `Services.obs.addObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## NewTabMessaging.uninit()
- 位置: L30-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## NewTabMessaging.observe()
- 位置: L35-46
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "newtab-message")` → `this.showMessage()`
- 条件付き依存: `if (topic === "newtab-message-query")` → `this.browserSet.has()`
- 参照: `browser.selectedBrowser`, `subject.wrappedJSObject`, `subject.wrappedJSObject.activeNewtabMessage`, `this.ASRouterDispatch`

## NewTabMessaging.showMessage()
- 位置: async L48-108
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (targetBrowser)` → `targetBrowser.browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (actor)` → `actor.getTabDetails()`
- 条件付き依存: `if (tabDetails)` → `this.store.dispatch()`
- 条件付き依存: `if (tabDetails)` → `ac.OnlyToOneContent()`
- 条件付き依存: `if (!(targetBrowser))` → `this.store.dispatch()`
- 条件付き依存: `if (!(targetBrowser))` → `ac.AlsoToPreloaded()`
- 条件付き依存: `if (!(targetBrowser))` → `this.ASRouterDispatch()`
- 参照: `at.MESSAGE_SET`, `at.MESSAGE_TOGGLE_VISIBILITY`, `tabDetails.portID`

## NewTabMessaging.blockMessage()
- 位置: L114-123
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (id)` → `this.ASRouterDispatch()`

## NewTabMessaging.handleImpression()
- 位置: L132-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ASRouterDispatch()`, `this.sendTelemetry()`

## NewTabMessaging.sendTelemetry()
- 位置: L141-152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.ASRouterDispatch()`
- 参照: `message.id`

## NewTabMessaging.notifyVisiblity()
- 位置: L154-167
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (action.data)` → `this.browserSet.has()`
- 条件付き依存: `if (!this.browserSet.has(browser))` → `this.browserSet.add()`
- 条件付き依存: `if (!(action.data))` → `this.browserSet.has()`
- 条件付き依存: `if (this.browserSet.has(browser))` → `this.browserSet.delete()`
- 参照: `action._target`, `action.data`

## NewTabMessaging.onAction()
- 位置: L169-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToPreloaded()`, `this.blockMessage()`, `this.browserSet.delete()`, `this.handleImpression()`, `this.init()`, `this.notifyVisiblity()`, `this.sendTelemetry()`, `this.store.dispatch()`, `this.uninit()`
- 参照: `action._target?.browser`, `action.data`, `action.data.message`, `action.data.source`, `action.type`, `at.INIT`, `at.MESSAGE_BLOCK`, `at.MESSAGE_CLICK`, `at.MESSAGE_DISMISS`, `at.MESSAGE_IMPRESSION`, `at.MESSAGE_NOTIFY_VISIBILITY`, `at.MESSAGE_TOGGLE_VISIBILITY`, `at.NEW_TAB_UNLOAD`, `at.UNINIT`
