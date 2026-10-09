# browser/actors/DOMFullscreenParent.sys.mjs

source: browser/actors/DOMFullscreenParent.sys.mjs
source-hash: 3ec1dc8cfa3ae53e7786a66cd3b3130217ec14b5
lines: 374

## <module>
- 役割: DOM フルスクリーンの親側アクター。子プロセスからの入退出要求を受けて、ウィンドウのフルスクリーン状態と要求元の追跡、キーボードロック警告を管理する。

## DOMFullscreenParent.updateFullscreenWindowReference()
- 位置: L20-26
- 役割: ウィンドウに inDOMFullscreen 属性があれば、そのウィンドウを保持し、無ければ参照を消す。
- 触るとき: フルスクリーン中のウィンドウを後で参照する条件を変えるときに見る。
- 呼び出し先: `aWindow.document.documentElement.hasAttribute()`
- 参照: `this._fullscreenWindow`

## DOMFullscreenParent.cleanupDomFullscreen()
- 位置: L28-43
- 役割: FullScreen の後始末を呼び、フルスクリーンでもその処理が無い場合は描画完了の通知を出す。
- 触るとき: フルスクリーンを抜けた後に描画完了の待ちが残る問題を調べるときに見る。
- 呼び出し先: `aWindow.FullScreen.cleanupDomFullscreen()`
- 条件付き依存: `if ( !aWindow.FullScreen.cleanupDomFullscreen(this) && !aWindow.document.fullscreen )` → `Services.obs.notifyObservers()`
- 参照: `aWindow.FullScreen`, `aWindow.document.fullscreen`
- XPCOM: `Services.obs`

## DOMFullscreenParent._cleanupFullscreenStateAndResumeChromeUI()
- 位置: L50-55
- 役割: 後始末を行い、要求元かつフルスクリーン中なら、リモートフレームのフルスクリーンを戻す。
- 触るとき: フルスクリーンから戻る際にクローム UI が固まる問題を調べるときに見る。
- 呼び出し先: `this.cleanupDomFullscreen()`
- 条件付き依存: `if (this.requestOrigin == this && aWindow.document.fullscreen)` → `aWindow.windowUtils.remoteFrameFullscreenReverted()`
- 参照: `aWindow.document.fullscreen`, `this.requestOrigin`

## DOMFullscreenParent.didDestroy()
- 位置: L57-119
- 役割: 破棄時に、入退出の待ちを解消し、ウィンドウがまだフルスクリーンなら UI を戻して参照を更新する。
- 触るとき: 子プロセスの遷移中にウィンドウがフルスクリーンのまま戻らない問題を調べるときに見る。
- 呼び出し先: `this.updateFullscreenWindowReference()`, `window.document.documentElement.hasAttribute()`
- 条件付き依存: `if ( this.waitingForChildExitFullscreen || this.waitingForChildEnterFullscreen )` → `this._cleanupFullscreenStateAndResumeChromeUI()`
- 条件付き依存: `if (this != this.requestOrigin)` → `this.removeListeners()`
- 条件付き依存: `if (window.document.fullscreen)` → `window.document.exitFullscreen().catch()`
- 条件付き依存: `if (window.document.fullscreen)` → `window.document.exitFullscreen()`
- 条件付き依存: `if (this.waitingForChildEnterFullscreen)` → `this.cleanupDomFullscreen()`
- 条件付き依存: `if (window.document.documentElement.hasAttribute("inDOMFullscreen"))` → `this.cleanupDomFullscreen()`
- 条件付き依存: `if (window.windowUtils)` → `window.windowUtils.remoteFrameFullscreenReverted()`
- 条件付き依存: `if (this.waitingForChildExitFullscreen)` → `this._cleanupFullscreenStateAndResumeChromeUI()`
- 参照: `browser.documentGlobal`, `this._didDestroy`, `this._fullscreenWindow`, `this.browsingContext.top`, `this.requestOrigin`, `this.waitingForChildEnterFullscreen`, `this.waitingForChildExitFullscreen`, `topBrowsingContext.embedderElement`, `window.document.fullscreen`, `window.windowUtils`

## DOMFullscreenParent.receiveMessage()
- 位置: L121-215
- 役割: Request・NewOrigin・Entered・Exit・Exited・Painted・UpdateKeyboardLock を処理し、要求元の設定とフルスクリーン状態を変える。キーボードロックの値は検証して受け入れる。
- 触るとき: フルスクリーンの要求から完了までの親側の状態遷移を変えるときに見る。
- 呼び出し先: `Glean.fullscreen.change.stopAndAccumulate()`, `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `this.addListeners()`, `this.cleanupDomFullscreen()`, `this.sendAsyncMessage()`, `this.updateFullscreenWindowReference()`, `window.FullScreen.enterDomFullscreen()`, `window.windowUtils.remoteFrameFullscreenChanged()`, `window.windowUtils.remoteFrameFullscreenReverted()`
- 条件付き依存: `if (window.document.fullscreen)` → `window.PointerlockFsWarning.showFullScreen()`
- 条件付き依存: `if (window.document.fullscreenKeyboardLock != newLock)` → `this.manager.updateFullscreenKeyboardLockStatus()`
- 条件付き依存: `if (window.document.fullscreenKeyboardLock != newLock)` → `window.PointerlockFsWarning.close()`
- 条件付き依存: `if (window.document.fullscreenKeyboardLock != newLock)` → `window.PointerlockFsWarning.showFullScreen()`
- 参照: `aMessage.data.fullscreenKeyboardLock`, `aMessage.name`, `browser.documentGlobal`, `this.browsingContext`, `this.browsingContext.top`, `this.fullscreenKeyboardLock`, `this.manager.fullscreen`, `this.nextMsgRecipient`, `this.requestOrigin`, `this.timerId`, `this.waitingForChildEnterFullscreen`, `this.waitingForChildExitFullscreen`, `topBrowsingContext.embedderElement`, `window.document.fullscreen`, `window.document.fullscreenKeyboardLock`
- XPCOM: `Services.obs` / `Services.prefs`

## DOMFullscreenParent.handleEvent()
- 位置: L217-295
- 役割: 要求元のアクターだけが、Entered・Exited・WarnAboutKeyboardLock を処理する。インストール通知を消し、計測を始め、警告を出す。
- 触るとき: フルスクリーンのイベント処理や計測の開始・停止を変えるときに見る。
- 呼び出し先: `Glean.fullscreen.change.start()`, `this.cleanupDomFullscreen()`, `this.hasBeenDestroyed()`, `this.updateFullscreenWindowReference()`, `window.FullScreen.enterDomFullscreen()`, `window.browsingContext.fullscreenRequestOrigin?.get()`
- 条件付き依存: `if (this != requestOrigin)` → `this.removeListeners()`
- 条件付き依存: `if (window.gXPInstallObserver)` → `window.gXPInstallObserver.removeAllNotifications()`
- 条件付き依存: `if (!this.hasBeenDestroyed() && this.requestOrigin)` → `window.PointerlockFsWarning.showFullScreen()`
- 条件付き依存: `if (!this.manager.fullscreen)` → `this.removeListeners()`
- 参照: `aEvent.currentTarget`, `aEvent.target`, `aEvent.target.documentGlobal`, `aEvent.target.documentGlobal.docShell.chromeEventHandler`, `aEvent.type`, `browser.documentGlobal.document.fullscreenKeyboardLock`, `this.manager.fullscreen`, `this.requestOrigin`, `this.requestOrigin.browsingContext`, `this.timerId`, `window.document.fullscreenKeyboardLock`, `window.gXPInstallObserver`

## DOMFullscreenParent.addListeners()
- 位置: L297-317
- 役割: ウィンドウに、フルスクリーン関連の 3 種類のイベントを捕捉フェーズで登録する。
- 触るとき: フルスクリーンのイベントを受ける対象を増やすときに見る。
- 呼び出し先: `aWindow.addEventListener()`

## DOMFullscreenParent.removeListeners()
- 位置: L319-327
- 役割: addListeners で登録した 3 種類のフルスクリーンイベントの登録を外す。
- 触るとき: リスナーの解除漏れや二重登録を調べるときに見る。
- 呼び出し先: `aWindow.removeEventListener()`

## DOMFullscreenParent.requestOrigin()
- 位置: L333-337
- 役割: トップのクローム BrowsingContext に保存された、フルスクリーン要求元のアクターを弱参照から取り出して返す。
- 触るとき: どの子が要求元かを判定する条件を見直すときに見る。
- 呼び出し先: `requestOrigin.get()`
- 参照: `chromeBC?.fullscreenRequestOrigin`, `this.browsingContext.topChromeWindow?.browsingContext`

## DOMFullscreenParent.requestOrigin()
- 位置: L344-356
- 役割: フルスクリーン要求元のアクターを、クローム BrowsingContext へ弱参照で保存し、null なら削除する。
- 触るとき: 要求元の記録・消去の仕組みを変えるときに見る。
- 条件付き依存: `if (!chromeBC)` → `console.error()`
- 条件付き依存: `if (aActor)` → `Cu.getWeakReference()`
- 参照: `chromeBC.fullscreenRequestOrigin`, `this.browsingContext.topChromeWindow?.browsingContext`

## DOMFullscreenParent.hasBeenDestroyed()
- 位置: L358-372
- 役割: didDestroy 済みか、ブラウジングコンテキストにアクセスできるかで、アクターが破棄済みかを判定する。
- 触るとき: 破棄済みアクターを使って例外になる問題を調べるときに見る。
- 参照: `this._didDestroy`, `this.browsingContext`
