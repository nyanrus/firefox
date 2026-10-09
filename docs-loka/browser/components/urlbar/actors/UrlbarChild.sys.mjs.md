# browser/components/urlbar/actors/UrlbarChild.sys.mjs

source: browser/components/urlbar/actors/UrlbarChild.sys.mjs
source-hash: 7a1929d5c43c0e56fe48f68213746a504c5ed21b
lines: 304

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`, `this.#childControllers.delete()`, `this.#maybeSendAsyncMessage()`

## UrlbarChild.#maybeSendAsyncMessage()
- 位置: L60-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `ex.name`

## UrlbarChild.#maybeSendQuery()
- 位置: async L80-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`
- 参照: `ex.name`

## UrlbarChild.#wrapPromise()
- 位置: L106-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `String()`, `promise.then()`, `reject()`, `resolve()`
- 参照: `ex?.message`, `win.Error`, `win.Promise`

## UrlbarChild.#forContent()
- 位置: L133-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`
- 参照: `this.contentWindow`, `this.manager.parentActor`

## UrlbarChild.exposePort()
- 位置: L153-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `Cu.waiveXrays()`, `this.createPort()`
- 参照: `this.contentWindow`, `this.manager.parentActor`, `win.UrlbarActorPort`

## UrlbarChild.createPort()
- 位置: L170-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.UrlbarPrefs.addObserver.bind()`, `lazy.UrlbarPrefs.removeObserver.bind()`, `lazy.UrlbarPrefs.toggleResultMenuKeyboardAccessible.bind()`, `this.#maybeSendAsyncMessage.bind()`, `this.registerChildController.bind()`, `this.registerMessagePathInput.bind()`
- 参照: `UrlbarContentUtils.getDisplaySpec`, `UrlbarContentUtils.getPlatform`, `UrlbarContentUtils.getSupportUrl`, `UrlbarContentUtils.isTextDirectionRTL`, `UrlbarContentUtils.unEscapeURIForUI`, `UrlbarContentUtils.whereToOpenLink`, `UrlbarContentUtils.willLoadInBackground`, `lazy.UrlbarPrefs`, `this.contentWindow`

## sendQuery()
- 位置: L174-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeSendQuery()`, `this.#wrapPromise()`, `this.sendQuery()`

## getFixupPrimitives()
- 位置: L183-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getFixupPrimitives()`, `this.#forWindow()`

## getPref()
- 位置: L197-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#forWindow()`

## UrlbarChild.#forWindow()
- 位置: L218-220
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`
- 参照: `this.manager.parentActor`

## UrlbarChild.handleEvent()
- 位置: L227-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.usesMessagePath()`
- 条件付き依存: `if (UrlbarContentUtils.usesMessagePath())` → `this.exposePort()`

## UrlbarChild.registerMessagePathInput()
- 位置: L245-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#destroyRegistry.register()`
- 参照: `this.#nextInstanceId`

## UrlbarChild.registerChildController()
- 位置: L261-263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#childControllers.set()`

## UrlbarChild.receiveMessage()
- 位置: L265-271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#invokeContentAction()`
- 参照: `message.data`, `message.name`

## UrlbarChild.#invokeContentAction()
- 位置: L284-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowlist?.includes()`, `receiver?.[method]()`, `this.#childControllers.get()`, `this.#childControllers.get(instanceId)?.deref()`, `this.#forContent()`
- 条件付き依存: `if (!child)` → `this.#childControllers.delete()`
- 条件付き依存: `if (!this.manager.parentActor)` → `Cu.waiveXrays()`
- 参照: `lazy.UrlbarShared.INVOKABLE_CONTENT_ACTIONS`, `this.manager.parentActor`
