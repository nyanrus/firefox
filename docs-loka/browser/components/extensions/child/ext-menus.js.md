# browser/components/extensions/child/ext-menus.js

source: browser/components/extensions/child/ext-menus.js
source-hash: a3b6539b079d7b3b0f407f46638eaffa746b0922
lines: 306

## <module>
- 役割: (未記入)

## ContextMenusClickPropHandler.constructor()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent.bind()`
- 参照: `this.context`, `this.dispatchEvent`, `this.onclickMap`

## ContextMenusClickPropHandler.dispatchEvent()
- 位置: L31-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onclickMap.get()`
- 条件付き依存: `if (onclick)` → `withHandlingUserInput()`
- 条件付き依存: `if (onclick)` → `onclick()`
- 参照: `info.menuItemId`, `this.context.contentWindow`

## ContextMenusClickPropHandler.setListener()
- 位置: L45-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPropHandlers.get()`, `gPropHandlers.set()`, `propHandlerMap.set()`, `this.onclickMap.set()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent("menusInternal.onClicked") .addListener()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.callOnClose()`
- 条件付き依存: `if (!(!propHandlerMap))` → `propHandlerMap.get()`
- 条件付き依存: `if (propHandler && propHandler !== this)` → `propHandler.unsetListener()`
- 参照: `this.context.extension`, `this.dispatchEvent`, `this.onclickMap.size`

## ContextMenusClickPropHandler.unsetListener()
- 位置: L71-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPropHandlers.get()`, `propHandlerMap.delete()`, `this.onclickMap.delete()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent("menusInternal.onClicked") .removeListener()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.forgetOnClose()`
- 条件付き依存: `if (propHandlerMap.size === 0)` → `gPropHandlers.delete()`
- 参照: `propHandlerMap.size`, `this.context.extension`, `this.dispatchEvent`, `this.onclickMap.size`

## ContextMenusClickPropHandler.unsetListenerFromAnyContext()
- 位置: L90-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPropHandlers.get()`, `propHandlerMap.get()`
- 条件付き依存: `if (propHandler)` → `propHandler.unsetListener()`
- 参照: `this.context.extension`

## ContextMenusClickPropHandler.deleteAllListenersFromExtension()
- 位置: L99-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gPropHandlers.get()`
- 条件付き依存: `if (propHandlerMap)` → `propHandler.unsetListener()`
- 参照: `this.context.extension`

## ContextMenusClickPropHandler.close()
- 位置: L109-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.onclickMap.keys()`, `this.unsetListener()`

## getAPI()
- 位置: L117-304
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.extension.hasPermission()`
- 参照: `api.menus`, `result.contextMenus`, `result.menus`

## create()
- 位置: L124-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager .callParentAsyncFunction()`, `context.childManager .callParentAsyncFunction("menusInternal.create", [createProperties]) .then()`, `context.getCaller()`, `context.withLastError()`
- 条件付き依存: `if (onclick)` → `onClickedProp.setListener()`
- 条件付き依存: `if (callback)` → `context.runSafeWithoutClone()`
- 参照: `context.extension.persistentBackground`, `createProperties.id`, `createProperties.onclick`, `extension.persistentBackground`

## update()
- 位置: L157-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager .callParentAsyncFunction()`, `context.childManager .callParentAsyncFunction("menusInternal.update", [ id, updateProperties, ]) .then()`
- 条件付き依存: `if (onclick)` → `onClickedProp.setListener()`
- 条件付き依存: `if (onclick === null)` → `onClickedProp.unsetListenerFromAnyContext()`
- 参照: `context.extension.persistentBackground`, `updateProperties.onclick`

## remove()
- 位置: L180-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `onClickedProp.unsetListenerFromAnyContext()`

## removeAll()
- 位置: L188-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `onClickedProp.deleteAllListenersFromExtension()`

## overrideContext()
- 位置: L197-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.tm.dispatchToMainThread()`, `checkValidArg()`
- 条件付き依存: `if (checkValidArg("tab", "tabId"))` → `context.extension.hasPermission()`
- 条件付き依存: `if (checkValidArg("bookmark", "bookmarkId"))` → `context.extension.hasPermission()`
- 参照: `context.extension.id`, `contextOptions.bookmarkId`, `contextOptions.context`, `contextOptions.showDefaults`, `contextOptions.tabId`, `pendingMenuEvent.webExtContextData`
- XPCOM: `Services.obs` / `Services.tm`

## checkValidArg()
- 位置: L198-218
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `contextOptions.context`, `contextOptions.showDefaults`

## observe()
- 位置: L249-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `context.principal.subsumes()`
- 条件付き依存: `if (context.principal.subsumes(subject.principal))` → `subject.setWebExtContextData()`
- 参照: `subject.principal`, `subject.wrappedJSObject`, `this.webExtContextData`
- XPCOM: `Services.obs`

## run()
- 位置: L257-266
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pendingMenuEvent === this)` → `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## register()
- 位置: L277-291
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.childManager.getParentEvent()`, `event.addListener()`, `event.removeListener()`

## listener()
- 位置: L278-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fire.sync()`, `withHandlingUserInput()`
- 参照: `context.contentWindow`
