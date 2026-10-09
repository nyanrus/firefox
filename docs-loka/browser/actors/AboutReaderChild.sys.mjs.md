# browser/actors/AboutReaderChild.sys.mjs

source: browser/actors/AboutReaderChild.sys.mjs
source-hash: 3d70b963f360f308b8dd82884be5e59b5f4d6d6b
lines: 252

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutReaderChild.constructor()
- 位置: L17-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._articlePromise`, `this._isLeavingReaderableReaderMode`, `this._reader`

## AboutReaderChild.didDestroy()
- 位置: L25-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.cancelPotentialPendingReadabilityCheck()`, `this.readerModeHidden()`

## AboutReaderChild.readerModeHidden()
- 位置: L30-35
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._reader)` → `this._reader.clearActor()`
- 参照: `this._reader`

## AboutReaderChild.receiveMessage()
- 位置: async L37-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ReaderMode.enterReaderMode()`, `lazy.ReaderMode.leaveReaderMode()`, `this.updateReaderButton()`
- 条件付き依存: `if (!this.isAboutReader)` → `gUrlsToDocContentType.set()`
- 条件付き依存: `if (!this.isAboutReader)` → `gUrlsToDocTitle.set()`
- 条件付き依存: `if (!this.isAboutReader)` → `lazy.ReaderMode.parseDocument( this.document ).catch()`
- 条件付き依存: `if (!this.isAboutReader)` → `lazy.ReaderMode.parseDocument()`
- 条件付き依存: `if (!this.isAboutReader)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!(!this.isAboutReader))` → `this.closeReaderMode()`
- 条件付き依存: `if (this._reader)` → `this._reader.receiveMessage()`
- 参照: `console.error`, `message.data`, `message.data.isArticle`, `message.name`, `this._articlePromise`, `this._reader`, `this.contentWindow`, `this.docShell`, `this.document`, `this.document.URL`, `this.document.contentType`, `this.document.title`, `this.isAboutReader`

## AboutReaderChild.isAboutReader()
- 位置: L78-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.documentURI.startsWith()`
- 参照: `this.document`

## AboutReaderChild.isReaderableAboutReader()
- 位置: L85-87
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.document.documentElement.dataset.isError`, `this.isAboutReader`

## AboutReaderChild.handleEvent()
- 位置: L89-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canDoReadabilityCheck()`, `this.cancelPotentialPendingReadabilityCheck()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!this.isAboutReader)` → `this.updateReaderButton()`
- 条件付き依存: `if (!this._articlePromise)` → `decodeURIComponent()`
- 条件付き依存: `if (!this._articlePromise)` → `url.substr()`
- 条件付き依存: `if (!this._articlePromise)` → `this.sendQuery()`
- 条件付き依存: `if (this.document.body)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (this.document.body)` → `gUrlsToDocContentType.get()`
- 条件付き依存: `if (this.document.body)` → `gUrlsToDocTitle.get()`
- 条件付き依存: `if (aEvent.persisted && this.canDoReadabilityCheck())` → `this.performReadabilityCheckNow()`
- 参照: `"about:reader?url=".length`, `aEvent.originalTarget.defaultView`, `aEvent.persisted`, `aEvent.type`, `lazy.AboutReader`, `this._articlePromise`, `this._isLeavingReaderableReaderMode`, `this._reader`, `this.contentWindow`, `this.document.body`, `this.document.documentURI`, `this.isAboutReader`

## AboutReaderChild.updateReaderButton()
- 位置: L154-160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.canDoReadabilityCheck()`, `this.scheduleReadabilityCheckPostPaint()`

## AboutReaderChild.canDoReadabilityCheck()
- 位置: L162-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.HTMLDocument.isInstance()`
- 参照: `lazy.Readerable.isEnabledForParseOnLoad`, `this.contentWindow`, `this.contentWindow.windowRoot`, `this.document`, `this.document.mozSyntheticDocument`, `this.isAboutReader`

## AboutReaderChild.cancelPotentialPendingReadabilityCheck()
- 位置: L173-184
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this._listenerWindow)` → `this._listenerWindow.removeEventListener()`
- 参照: `this._listenerWindow`, `this._pendingReadabilityCheck`

## AboutReaderChild.scheduleReadabilityCheckPostPaint()
- 位置: L186-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contentWindow.windowRoot.addEventListener()`, `this.onPaintWhenWaitedFor.bind()`
- 条件付き依存: `if (this._pendingReadabilityCheck)` → `this.cancelPotentialPendingReadabilityCheck()`
- 参照: `this._listenerWindow`, `this._pendingReadabilityCheck`, `this.contentWindow.windowRoot`

## AboutReaderChild.onPaintWhenWaitedFor()
- 位置: L204-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.performReadabilityCheckNow()`
- 参照: `event.clientRects.length`

## AboutReaderChild.performReadabilityCheckNow()
- 位置: L217-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Readerable.isProbablyReaderable()`, `lazy.Readerable.shouldCheckUri()`, `this.cancelPotentialPendingReadabilityCheck()`
- 条件付き依存: `if ( lazy.Readerable.shouldCheckUri(document.baseURIObject, true) && lazy.Readerable.isProbablyReaderable(document) )` → `this.sendAsyncMessage()`
- 条件付き依存: `if (forceNonArticle)` → `this.sendAsyncMessage()`
- 参照: `document.baseURIObject`, `this.document`

## AboutReaderChild.closeReaderMode()
- 位置: L245-250
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isAboutReader)` → `this.sendAsyncMessage()`
- 参照: `this._isLeavingReaderableReaderMode`, `this.isAboutReader`, `this.isReaderableAboutReader`
