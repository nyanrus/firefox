# browser/actors/DOMFullscreenChild.sys.mjs

source: browser/actors/DOMFullscreenChild.sys.mjs
source-hash: f9f8b556263fc0b94819d03030fa71d2caaf4a68
lines: 172

## <module>
- 役割: DOM フルスクリーンのコンテンツ側アクター。フルスクリーンの開始・終了要求を文書とウィンドウに反映し、描画完了や鍵盤ロックの状態を親へ伝える。

## DOMFullscreenChild.receiveMessage()
- 位置: L6-83
- 役割: 親からの Entered・CleanUp・Painted を処理し、フルスクリーンへの入出を実行して、描画完了を待つ状態を設定する。
- 触るとき: フルスクリーン開始・終了時の同期（描画待ち、リモートフレームの扱い）を変えるときに見る。
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (!windowUtils)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!remoteFrame)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (remoteFrameBC)` → `windowUtils.remoteFrameFullscreenChanged()`
- 条件付き依存: `if (!(remoteFrameBC))` → `windowUtils.handleFullscreenRequests()`
- 条件付き依存: `if ( !windowUtils.handleFullscreenRequests() && !this.document.fullscreenElement )` → `this.sendAsyncMessage()`
- 条件付き依存: `if (windowUtils)` → `windowUtils.exitFullscreen()`
- 条件付き依存: `if (isNotTheRequestSource)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!(isNotTheRequestSource))` → `this.sendAsyncMessage()`
- 参照: `aMessage.data.remoteFrameBC`, `aMessage.name`, `remoteFrameBC.embedderElement`, `this._isNotTheRequestSource`, `this._lastTransactionId`, `this._waitForMozAfterPaint`, `this.contentWindow`, `this.document.fullscreenElement`, `window?.windowUtils`, `windowUtils.lastTransactionId`
- XPCOM: `Services.obs`

## DOMFullscreenChild.handleEvent()
- 位置: L85-158
- 役割: 文書側の MozDOMFullscreen イベントを親向けメッセージに変換し、描画完了（MozAfterPaint）も待ってから Painted を送る。
- 触るとき: フルスクリーン要求・終了・オリジン変化の通知が親に届かない問題を調べるときに見る。
- 呼び出し先: `this.hasBeenDestroyed()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (this._isNotTheRequestSource)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (this._isNotTheRequestSource)` → `aEvent.type.replace()`
- 条件付き依存: `if (this._waitForMozAfterPaint)` → `this._listeningWindow.addEventListener()`
- 条件付き依存: `if (!this.document || !this.document.fullscreenElement)` → `this.sendAsyncMessage()`
- 条件付き依存: `if ( !this._lastTransactionId || aEvent.transactionId > this._lastTransactionId )` → `this._listeningWindow.removeEventListener()`
- 条件付き依存: `if ( !this._lastTransactionId || aEvent.transactionId > this._lastTransactionId )` → `this.sendAsyncMessage()`
- 参照: `aEvent.detail`, `aEvent.target.nodePrincipal.originNoSuffix`, `aEvent.transactionId`, `aEvent.type`, `this._isNotTheRequestSource`, `this._lastTransactionId`, `this._listeningWindow`, `this._waitForMozAfterPaint`, `this.contentWindow.windowRoot`, `this.document`, `this.document.fullscreenElement`

## DOMFullscreenChild.hasBeenDestroyed()
- 位置: L160-170
- 役割: ブラウジングコンテキストにアクセスできるかで、アクターが破棄済みかを判定する。
- 触るとき: 破棄後に送信して例外が出る問題を調べるときに見る。破棄通知が来ないことがあるため、この判定に頼っている。
- 参照: `this.browsingContext`
