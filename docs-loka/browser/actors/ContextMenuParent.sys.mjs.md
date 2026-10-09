# browser/actors/ContextMenuParent.sys.mjs

source: browser/actors/ContextMenuParent.sys.mjs
source-hash: 9e0ef4f14fdf455c3a8693dbfc3741faecb6fc08
lines: 259

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`

## ContextMenuParent.receiveMessage()
- 位置: L27-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.hasAttribute()`, `this.#openContextMenu()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.docShell.chromeEventHandler`, `lazy.FirefoxRelay.isEnabled`, `message.data`, `message.data.context.showRelay`, `this.manager.rootFrameLoader.ownerElement`, `topBrowser.documentGlobal`, `win.nsContextMenu`

## ContextMenuParent.hiding()
- 位置: L49-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.reloadFrame()
- 位置: L58-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.getImageText()
- 位置: L65-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.toggleRevealPassword()
- 位置: L71-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.useRelayMask()
- 位置: async L77-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FirefoxRelay.generateUsername()`
- 条件付き依存: `if (emailMask)` → `this.sendAsyncMessage()`
- 参照: `this.manager.browsingContext.currentWindowGlobal`, `windowGlobal.rootFrameLoader.ownerElement`

## ContextMenuParent.reloadImage()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.getFrameTitle()
- 位置: L97-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.mediaCommand()
- 位置: L101-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `browser.documentGlobal`, `this.manager.browsingContext.currentWindowGlobal`, `win.windowUtils`, `windowGlobal.rootFrameLoader.ownerElement`, `windowUtils.isHandlingUserInput`

## ContextMenuParent.canvasToBlobURL()
- 位置: L114-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.canvasToBlob()
- 位置: L118-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.saveVideoFrameAsImage()
- 位置: L122-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.setAsDesktopBackground()
- 位置: L128-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.getSearchFieldEngineData()
- 位置: L134-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.getTextDirective()
- 位置: L140-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`
- 参照: `lazy.TEXT_FRAGMENTS_ENABLED`

## ContextMenuParent.removeAllTextFragments()
- 位置: L146-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.#openContextMenu()
- 位置: L160-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.E10SUtils.deserializeReferrerInfo()`, `lazy.WebNavigationFrames.getFrameId()`, `popup.openPopupAtScreen()`, `win.document.getElementById()`
- 条件付き依存: `if (frameReferrerInfo)` → `lazy.E10SUtils.deserializeReferrerInfo()`
- 条件付き依存: `if (linkReferrerInfo)` → `lazy.E10SUtils.deserializeReferrerInfo()`
- 参照: `MouseEvent.MOZ_SOURCE_CURSOR`, `MouseEvent.MOZ_SOURCE_ERASER`, `MouseEvent.MOZ_SOURCE_KEYBOARD`, `MouseEvent.MOZ_SOURCE_MOUSE`, `MouseEvent.MOZ_SOURCE_PEN`, `MouseEvent.MOZ_SOURCE_TOUCH`, `context.frameBrowsingContextID`, `context.frameID`, `context.frameOuterWindowID`, `context.inputSource`, `context.principal`, `context.screenXDevPx`, `context.screenYDevPx`, `context.storagePrincipal`, `data.charSet`, `data.contentDisposition`, `data.contentType`, `data.context`, `data.disableSetDesktopBackground`, `data.editFlags`, `data.frameReferrerInfo`, `data.linkReferrerInfo`, `data.loginFillInfo`, `data.referrerInfo`, `data.selectionInfo`, `data.showRelay`, `data.spellInfo`, `data.webExtContextData`, `documentURIObject.spec`, `lazy.BrowserHandler.kiosk`, `newEvent.screenX`, `newEvent.screenY`, `this.manager`, `wgp.browsingContext`, `wgp.browsingContext.currentURI`, `wgp.browsingContext.id`, `wgp.browsingContext.originAttributes.userContextId`, `wgp.cookieJarSettings`, `wgp.documentPrincipal`, `wgp.documentStoragePrincipal`, `wgp.isCurrentGlobal`, `wgp.outerWindowId`, `win.devicePixelRatio`, `win.nsContextMenu.contentData`, `win.nsContextMenu.contentData.context`
