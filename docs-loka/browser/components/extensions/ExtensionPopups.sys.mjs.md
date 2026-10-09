# browser/components/extensions/ExtensionPopups.sys.mjs

source: browser/components/extensions/ExtensionPopups.sys.mjs
source-hash: 71bbfb4be0bf9cf0dd7895dba779f30e72cf688a
lines: 793

## <module>
- 役割: 拡張機能のポップアップ(ブラウザアクションやページアクションのパネル)を作って表示する基底クラスと、その派生の PanelPopup と ViewPopup を定義する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## promisePopupShown()
- 位置: L25-39
- 役割: パネルが既に開いていれば即座に、そうでなければ popupshown を一度だけ待つ Promise を返す。
- 触るとき: パネルが開いてから後続の処理を行う必要がある箇所で、待ち方を変えるとき。
- 条件付き依存: `if (popup.state == "open")` → `resolve()`
- 条件付き依存: `if (!(popup.state == "open"))` → `popup.addEventListener()`
- 条件付き依存: `if (!(popup.state == "open"))` → `resolve()`
- 参照: `popup.state`

## addPanelHidingHandler()
- 位置: L41-66
- 役割: パネルが閉じ始めたとき、直後の一定時間だけパネル外やパネル内へのクリックを無視する仕組みを張る。
- 触るとき: 閉じた直後の誤クリックを防ぐ時間や対象を変えるとき。
- 呼び出し先: `panel.addEventListener()`, `window.addEventListener()`, `window.removeEventListener()`, `window.setTimeout()`
- 参照: `lazy.delayBeforeEnablingButtons`, `panel.documentGlobal`

## handleClick()
- 位置: L42-54
- 役割: 無視期間中のクリックを、パネル(unified-extensions-panel を除く)と通知ツールバーの内側なら止めて、コンソールに記録する。
- 触るとき: 閉じた直後に無視するクリックの範囲を変えるとき。
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if ( event.target.closest( "panel:not(#unified-extensions-panel),#notifications-toolbar" ) )` → `event.preventDefault()`
- 条件付き依存: `if ( event.target.closest( "panel:not(#unified-extensions-panel),#notifications-toolbar" ) )` → `event.stopImmediatePropagation()`
- 条件付き依存: `if ( event.target.closest( "panel:not(#unified-extensions-panel),#notifications-toolbar" ) )` → `Services.console.logStringMessage()`
- XPCOM: `Services.console`

## BasePopup.constructor()
- 位置: L71-108
- 役割: 拡張、表示ノード、URL、スタイルを保持し、ブラウザ要素を作成する。文書の unload、DESTROY_EVENT、popuppositioned を監視し、ウィンドウごとの登録表に自身を入れる。
- 触るとき: ポップアップの生成時の監視やブラウザ要素の初期化順序を変えるとき。
- 呼び出し先: `BasePopup.instances.get()`, `BasePopup.instances.get(this.window).set()`, `extension.callOnClose()`, `this.createBrowser()`, `this.panel.addEventListener()`, `this.viewNode.addEventListener()`, `this.window.addEventListener()`
- 参照: `this.DESTROY_EVENT`, `this._resolveContentReady`, `this.blockParser`, `this.browser`, `this.browserLoaded`, `this.browserLoadedDeferred`, `this.browserReady`, `this.browserStyle`, `this.contentReady`, `this.destroyed`, `this.extension`, `this.fixedWidth`, `this.popupURL`, `this.viewNode`, `this.window`, `viewNode.documentGlobal`

## BasePopup.for()
- 位置: L110-112
- 役割: ウィンドウと拡張から、そこで開いている BasePopup を探す。
- 触るとき: 拡張のポップアップを外から参照する経路を変えるとき。
- 呼び出し先: `BasePopup.instances.get()`, `BasePopup.instances.get(window).get()`

## BasePopup.close()
- 位置: L114-116
- 役割: ポップアップを閉じる処理を呼ぶ。
- 触るとき: 閉じる要求の経路を追うとき。
- 呼び出し先: `this.closePopup()`

## BasePopup.destroy()
- 位置: L118-162
- 役割: 監視と登録を外し、待機中の Promise を失敗させ、ブラウザとノードを取り除いてパネルのスタイルを戻す。
- 触るとき: ポップアップを破棄する際の後始末に抜けがないかを確かめるとき。
- 呼び出し先: `BasePopup.instances.get()`, `BasePopup.instances.get(this.window).delete()`, `this._resolveContentReady()`, `this.browserLoaded.catch()`, `this.browserLoadedDeferred.reject()`, `this.browserReady.then()`, `this.extension.forgetOnClose()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this.browser)` → `this.destroyBrowser()`
- 条件付き依存: `if (this.browser)` → `this.browser.parentNode.remove()`
- 条件付き依存: `if (this.stack)` → `this.stack.remove()`
- 条件付き依存: `if (this.viewNode)` → `this.viewNode.removeEventListener()`
- 条件付き依存: `if (panel)` → `panel.removeEventListener()`
- 条件付き依存: `if (panel && panel.id !== REMOTE_PANEL_ID)` → `panel.style.removeProperty()`
- 条件付き依存: `if (panel && panel.id !== REMOTE_PANEL_ID)` → `panel.removeAttribute()`
- 参照: `panel.id`, `this.DESTROY_EVENT`, `this.browser`, `this.destroyed`, `this.extension`, `this.stack`, `this.viewNode`, `this.viewNode.customRectGetter`, `this.window`

## BasePopup.destroyBrowser()
- 位置: L164-180
- 役割: ブラウザのメッセージリスナと各種イベントを外す。既に文書から外れていて、最終破棄なら受信処理を空にする。
- 触るとき: ブラウザの差し替えや破棄でリスナが残らないようにするとき。
- 呼び出し先: `browser.removeEventListener()`
- 条件付き依存: `if (mm)` → `mm.removeMessageListener()`
- 参照: `browser.messageManager`, `this.receiveMessage`

## this.receiveMessage()
- 位置: L174-174
- 役割: 文書から外れたブラウザに届く後続のメッセージを捨てるための空の関数。
- 触るとき: 破棄後に古いブラウザからのメッセージが届いても例外にならないようにする仕組みを変えるとき。

## BasePopup.DESTROY_EVENT()
- 位置: L184-186
- 役割: サブクラスで実装する、破棄のきっかけになるイベント名。基底では例外を投げる。
- 触るとき: 新しいポップアップの種類を足すとき、そのイベント名を決める必要がある。

## BasePopup.STYLESHEETS()
- 位置: L188-199
- 役割: ブラウザ用のスタイルと、固定幅でなければポップアップ用のスタイルの一覧を返す。
- 触るとき: ポップアップに当てるスタイルシートを変えるとき。
- 条件付き依存: `if (this.browserStyle)` → `sheets.push()`
- 条件付き依存: `if (!this.fixedWidth)` → `sheets.push()`
- 参照: `this.browserStyle`, `this.fixedWidth`

## BasePopup.panel()
- 位置: L201-207
- 役割: 表示ノードを祖先へたどり、localName が panel の要素を返す。
- 触るとき: ポップアップを包んでいるパネルの取得方法を変えるとき。
- 参照: `panel.localName`, `panel.parentNode`, `this.viewNode`

## BasePopup.receiveMessage()
- 位置: L209-228
- 役割: ブラウザからの background の変更、読み込み完了、リサイズの各メッセージを処理する。
- 触るとき: 子プロセス側から届くメッセージの種類を増やすとき。
- 呼び出し先: `this._resolveContentReady()`, `this.browserLoadedDeferred.resolve()`, `this.setBackground()`
- 条件付き依存: `if (!(this.ignoreResizes))` → `this.resizeBrowser()`
- 参照: `data.background`, `this.dimensions`, `this.ignoreResizes`

## BasePopup.handleEvent()
- 位置: L230-299
- 役割: unload や破棄イベントで destroy し、popuppositioned でフォーカスを移す準備をし、ページタイトルの反映、閉じる要求、ズームの増減を処理する。
- 触るとき: ポップアップのイベント処理の分岐を変えるとき。popuppositioned 後のフォーカス移動は描画の完了を待ってから行う。
- 呼び出し先: `this.closePopup()`, `this.viewNode.setAttribute()`
- 条件付き依存: `if (!this.destroyed)` → `this.destroy()`
- 条件付き依存: `if (!this.destroyed)` → `this.browserLoaded .then()`
- 条件付き依存: `if (!this.destroyed)` → `this.browser.documentGlobal.promiseDocumentFlushed()`
- 条件付き依存: `if (!this.destroyed)` → `this.browser.messageManager.sendAsyncMessage()`
- 参照: `ZoomManager.MAX`, `ZoomManager.MIN`, `browser.documentGlobal`, `browser.fullZoom`, `event.target`, `event.type`, `this.DESTROY_EVENT`, `this.browser.contentTitle`, `this.browser.fullZoom`, `this.destroyed`

## BasePopup.createBrowser()
- 位置: L301-417
- 役割: XUL の browser 要素を作り、拡張のグループと remote の属性を付け、読み込みを開始する。URL があれば読み込み後にそれを開き、なければ準備だけ行う。
- 触るとき: ポップアップのブラウザの属性や読み込みの順序を変えるとき。
- 呼び出し先: `browser.addEventListener()`, `browser.fixupAndLoadURIString()`, `browser.setAttribute()`, `document.createXULElement()`, `initBrowser()`, `readyPromise.then()`, `stack.appendChild()`, `stack.setAttribute()`, `viewNode.appendChild()`
- 条件付き依存: `if (this.extension.remote)` → `browser.setAttribute()`
- 条件付き依存: `if (this.extension.remote)` → `promiseEvent()`
- 条件付き依存: `if (!(this.extension.remote))` → `promiseEvent()`
- 条件付き依存: `if (this.extension.remote)` → `readyPromise.then()`
- 条件付き依存: `if (this.extension.remote)` → `setupBrowser()`
- 条件付き依存: `if (!popupURL)` → `setupBrowser()`
- 参照: `browser.contentWindow`, `this.browser`, `this.extension.policy.browsingContextGroupId`, `this.extension.principal`, `this.extension.remote`, `this.extension.remoteType`, `this.stack`, `viewNode.ownerDocument`

## setupBrowser()
- 位置: L362-377
- 役割: ブラウザのメッセージとイベントのリスナを登録し、extension-browser-inserted を発火させる。
- 触るとき: ブラウザに付けるリスナを増やすとき。
- 呼び出し先: `browser.addEventListener()`, `lazy.ExtensionParent.apiManager.emit()`, `mm.addMessageListener()`
- 参照: `browser.messageManager`

## initBrowser()
- 位置: L379-397
- 役割: setupBrowser を呼び、コンテンツ側のスクリプトを読み込んで、サイズの上限やスタイルなどを Extension:InitBrowser で送る。
- 触るとき: 子プロセス側に渡す初期化の内容を変えるとき。
- 呼び出し先: `mm.loadFrameScript()`, `mm.sendAsyncMessage()`, `setupBrowser()`
- 参照: `browser.messageManager`, `this.STYLESHEETS`, `this.blockParser`, `this.fixedWidth`

## BasePopup.unblockParser()
- 位置: L419-432
- 役割: 事前読み込みされたブラウザについて、パーサーのブロックを解き、Extension:UnblockParser を送る。破棄済みなら何もしない。
- 触るとき: 事前読み込みの後にポップアップを表示する順序を変えるとき。Bug 1747813 の理由から、移動後の再初期化ではブロックしない。
- 呼び出し先: `this.browser.messageManager.sendAsyncMessage()`, `this.browserReady.then()`
- 参照: `this.blockParser`, `this.destroyed`

## BasePopup.resizeBrowser()
- 位置: L434-456
- 役割: 固定幅なら高さだけを親の高さの上限まで広げ、それ以外は幅と高さを設定する。WebExtPopupResized のイベントを発火させる。
- 触るとき: ポップアップの大きさの決め方を変えるとき。
- 呼び出し先: `this.browser.dispatchEvent()`
- 条件付き依存: `if (this.fixedWidth)` → `this.panel.getAttribute()`
- 条件付き依存: `if (this.fixedWidth)` → `Math.min()`
- 条件付き依存: `if (this.fixedWidth)` → `Math.max()`
- 参照: `this.browser.style.height`, `this.browser.style.minHeight`, `this.browser.style.minWidth`, `this.browser.style.width`, `this.extraHeight`, `this.fixedWidth`, `this.lastCalculatedInViewHeight`, `this.viewHeight`, `this.window.CustomEvent`

## BasePopup.setBackground()
- 位置: L458-478
- 役割: 背景色を省略時は白にし、パネルの背景色と枠の色の変数に設定する。
- 触るとき: 拡張のポップアップの背景色や枠の見た目を変えるとき。
- 条件付き依存: `if (this.panel.id != "widget-overflow")` → `this.panel.style.setProperty()`
- 条件付き依存: `if (background == "#fff")` → `this.panel.style.setProperty()`
- 参照: `this.background`, `this.panel.id`

## PanelPopup.constructor()
- 位置: L489-517
- 役割: arrow 型の panel 要素を作り、mainPopupSet に追加して、開く時に WebExtPopupLoaded を発火させる。その後、基底クラスを初期化する。
- 触るとき: ブラウザアクションのパネルの作られ方を変えるとき。
- 呼び出し先: `addPanelHidingHandler()`, `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mainPopupSet").appendChild()`, `makeWidgetId()`, `panel.addEventListener()`, `panel.setAttribute()`, `super()`, `this.browser.dispatchEvent()`
- 条件付き依存: `if (extension.remote)` → `panel.setAttribute()`
- 参照: `extension.id`, `extension.remote`, `this.window.CustomEvent`

## PanelPopup.DESTROY_EVENT()
- 位置: L519-521
- 役割: 破棄の合図として popuphidden を返す。
- 触るとき: パネルの破棄がいつ始まるかを変えるとき。

## PanelPopup.destroy()
- 位置: L523-527
- 役割: 基底の破棄の後、パネル要素を文書から取り除く。
- 触るとき: パネルの要素が残らないようにするとき。
- 呼び出し先: `super.destroy()`, `this.viewNode.remove()`
- 参照: `this.viewNode`

## PanelPopup.closePopup()
- 位置: L529-543
- 役割: まだ開き始めていなければ破棄し、開いた後に hidePopup を呼ぶ。
- 触るとき: 閉じる要求が開く前に来た場合の扱いを変えるとき。
- 呼び出し先: `promisePopupShown()`, `promisePopupShown(this.viewNode).then()`
- 条件付き依存: `if (this.viewNode.state == "closed")` → `this.destroy()`
- 条件付き依存: `if (this.viewNode && this.viewNode.hidePopup)` → `this.viewNode.hidePopup()`
- 参照: `this.viewNode`, `this.viewNode.hidePopup`, `this.viewNode.state`

## ViewPopup.constructor()
- 位置: L547-599
- 役割: 事前読み込み用の一時的な panel を作る。remote の拡張なら共有の panel を使う。基底を初期化した後、事前読み込みのブラウザに目印のクラスを付ける。
- 触るとき: 事前読み込みの仕組みや、remote の拡張で panel を共有する条件を変えるとき。
- 呼び出し先: `super()`, `this.browser.classList.add()`
- 条件付き依存: `if (extension.remote)` → `document.getElementById()`
- 条件付き依存: `if (!panel)` → `createPanel()`
- 条件付き依存: `if (!(extension.remote))` → `createPanel()`
- 参照: `extension.remote`, `panel.id`, `this.attached`, `this.browser`, `this.ignoreResizes`, `this.shown`, `this.tempBrowser`, `this.tempPanel`, `window.document`

## createPanel()
- 位置: L557-567
- 役割: arrow 型の panel 要素を作り、remote なら remote 属性を付けて mainPopupSet に追加する。
- 触るとき: 事前読み込み用の panel の属性を変えるとき。
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mainPopupSet").appendChild()`, `panel.setAttribute()`
- 条件付き依存: `if (remote)` → `panel.setAttribute()`

## ViewPopup.attach()
- 位置: async L612-732
- 役割: 事前読み込みのブラウザを表示ノードへ付け替える。ブラウザの準備と最大200ミリ秒の猶予を待ち、高さの上限を計算し、新しいブラウザと docShell を入れ替えて、一時的な panel を取り除く。
- 触るとき: サブビューへのポップアップの表示の流れや、読み込み待ちの猶予を変えるとき。待機中に破棄されたら false を返す。
- 呼び出し先: `Math.max()`, `Promise.all()`, `Promise.race()`, `addPanelHidingHandler()`, `lazy.setTimeout()`, `panel.getBoundingClientRect()`, `this.browser.dispatchEvent()`, `this.browser.swapDocShells()`, `this.browserLoaded.catch()`, `this.createBrowser()`, `this.destroyBrowser()`, `this.panel.addEventListener()`, `this.panel.removeEventListener()`, `this.removeTempPanel()`, `this.setBackground()`, `this.viewNode.addEventListener()`, `this.viewNode.removeEventListener()`, `this.viewNode.setAttribute()`, `this.window.promiseDocumentFlushed()`, `viewNode.getBoundingClientRect()`
- 条件付き依存: `if (this.extension.remote)` → `this.panel.setAttribute()`
- 条件付き依存: `if (!this.destroyed && !panel)` → `this.destroy()`
- 条件付き依存: `if (this.destroyed)` → `lazy.CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (this.destroyed)` → `this.closePopup()`
- 条件付き依存: `if (this.destroyed)` → `this.destroy()`
- 条件付き依存: `if (this.dimensions)` → `this.resizeBrowser()`
- 参照: `popupRect.bottom`, `popupRect.top`, `this.DESTROY_EVENT`, `this.attached`, `this.background`, `this.browser`, `this.browserReady`, `this.destroyed`, `this.dimensions`, `this.dimensions.width`, `this.extension`, `this.extension.remote`, `this.extraHeight`, `this.fixedWidth`, `this.ignoreResizes`, `this.panel`, `this.shown`, `this.viewHeight`, `this.viewNode`, `this.viewNode.customRectGetter`, `this.window`, `this.window.CustomEvent`, `viewNode.getBoundingClientRect().height`, `win.mozInnerScreenY`, `win.screen.availHeight`, `win.screen.availTop`

## this.viewNode.customRectGetter()
- 位置: L711-713
- 役割: 表示ノードの高さを、計算済みの高さか初期の高さで返す関数。
- 触るとき: サブビューの高さがメニューの大きさに合わせて決まる仕組みを変えるとき。
- 参照: `this.lastCalculatedInViewHeight`, `this.viewHeight`

## ViewPopup.removeTempPanel()
- 位置: L734-745
- 役割: 一時的な panel とブラウザを取り除き、参照を消す。共有の REMOTE_PANEL_ID は残す。
- 触るとき: 事前読み込みの後片付けを変えるとき。
- 条件付き依存: `if (this.tempPanel.id !== REMOTE_PANEL_ID)` → `this.tempPanel.remove()`
- 条件付き依存: `if (this.tempBrowser)` → `this.tempBrowser.parentNode.remove()`
- 参照: `this.tempBrowser`, `this.tempPanel`, `this.tempPanel.id`

## ViewPopup.destroy()
- 位置: L747-751
- 役割: 基底の破棄の後、一時的な panel を取り除く。
- 触るとき: サブビューの破棄後に残る要素の扱いを変えるとき。
- 呼び出し先: `super.destroy()`, `super.destroy().then()`, `this.removeTempPanel()`

## ViewPopup.DESTROY_EVENT()
- 位置: L753-755
- 役割: 破棄の合図として ViewHiding を返す。
- 触るとき: サブビューが隠れたときに破棄を始める条件を変えるとき。

## ViewPopup.closePopup()
- 位置: L757-765
- 役割: 表示中なら CustomizableUI でパネルを隠し、付け替え済みなら destroyed を立て、どちらでもなければ破棄する。
- 触るとき: サブビューを閉じる場合の分岐を変えるとき。
- 条件付き依存: `if (this.shown)` → `lazy.CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (!(this.attached))` → `this.destroy()`
- 参照: `this.attached`, `this.destroyed`, `this.shown`, `this.viewNode`

## isGloballyBlockingOpenPopup()
- 位置: L770-792
- 役割: 開いているメニューやパネルがあれば true を返す。タブのホバープレビューだけは例外として無視する。
- 触るとき: ポップアップを開く前に、他の開いた UI と重なるのを避ける条件を変えるとき。
- 呼び出し先: `window.document.querySelectorAll()`
- 条件付き依存: `if (elem.state !== "closed" && elem.state !== "hiding")` → `previewPanel?.isHoverPanel()`
- 参照: `elem.state`, `window.gBrowser.tabContainer.previewPanel`
