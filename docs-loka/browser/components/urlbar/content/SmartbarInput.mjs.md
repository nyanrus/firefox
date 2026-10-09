# browser/components/urlbar/content/SmartbarInput.mjs

source: browser/components/urlbar/content/SmartbarInput.mjs
source-hash: 62b27dc8d0cce96ec4382194406edcedd55f7039
lines: 8002

## <module>
- 役割: スマートバー(アドレスバーと検索・チャット入力を兼ねる欄)の入力部分を実装する custom element SmartbarInput を定義する。
- 呼び出し先: `ChromeUtils.importESModule()`, `Promise.resolve()`, `XPCOMUtils.declareLazy()`, `customElements.define()`

## logger()
- 位置: L97-97
- 役割: UrlbarShared のロガーを prefix "SmartbarInput" 付きで返す。
- 触るとき: SmartbarInput のデバッグログを出す箇所を追加・確認するとき。
- 呼び出し先: `UrlbarShared.getLogger()`

## getBoundsWithoutFlushing()
- 位置: L106-107
- 役割: windowUtils.getBoundsWithoutFlushing で要素の矩形を取得し、レイアウトを強制再計算させない。
- 触るとき: ポップオーバーのアンカー高さを測る #measurePopoverAnchor のように、描画を伴わずに寸法だけ欲しいとき。
- 呼び出し先: `element.documentGlobal.windowUtils.getBoundsWithoutFlushing()`

## px()
- 位置: L108-108
- 役割: 数値を小数点以下2桁の文字列にして末尾に px を付ける。
- 触るとき: 測った寸法を style に設定する箇所で単位付きの値が必要なとき。
- 呼び出し先: `number.toFixed()`

## SmartbarInput.#markup()
- 位置: L153-230
- 役割: スマートバーの内部 DOM(検索モード切替ボタン、入力欄、結果ビュー、ボタン列)のマークアップ文字列を返す。nova 有効時と無効時で区切り線の構成が変わる。
- 触るとき: 入力欄や結果ビューの子要素・属性を追加・変更するとき、または nova の区切り線の出し分けを見直すとき。
- 呼び出し先: `UrlbarPrefs.get()`

## SmartbarInput.observedAttributes()
- 位置: L232-234
- 役割: 監視対象の属性を open だけにする。
- 触るとき: 属性変化の通知対象に別の属性を加えたいとき。

## SmartbarInput.fragment()
- 位置: L244-250
- 役割: マークアップを初回だけ XUL フラグメントにパースしてキャッシュし、呼び出しごとに importNode で複製して返す。
- 触るとき: 生成される DOM を変えたいとき、またはスマートバーを複数作る際の複製コストを見直すとき。
- 呼び出し先: `document.importNode()`
- 条件付き依存: `if (!this.#fragment)` → `window.MozXULElement.parseXULToFragment()`
- 参照: `this.#fragment`, `this.#markup`

## SmartbarInput.#popoverAnchor()
- 位置: L286-288
- 役割: ポップオーバーのアンカーとして親ノード(parentNode)を返す。
- 触るとき: ポップオーバーの位置決めの基準要素を変えたいとき。
- 参照: `this.parentNode`

## SmartbarInput.constructor()
- 位置: L365-385
- 役割: gBrowser を持つ窓を親窓として解決し、document と private 判定を用意して UrlbarPrefs の監視を登録する。unload で監視を外す。
- 触るとき: 検索バーなど gBrowser を持たない文脈でスマートバーが生成されたときの窓の決まり方を調べるとき。
- 呼び出し先: `UrlbarPrefs.addObserver()`, `UrlbarPrefs.removeObserver()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `super()`, `window.addEventListener()`
- 条件付き依存: `if (!this.window.gBrowser)` → `logger().debug()`
- 条件付き依存: `if (!this.window.gBrowser)` → `logger()`
- 参照: `this.document`, `this.documentGlobal`, `this.isPrivate`, `this.window`, `this.window.document`, `this.window.gBrowser`, `window.browsingContext.topChromeWindow`

## SmartbarInput.#populateSlots()
- 位置: L393-420
- 役割: moz-urlbar-slot[name] の位置へ urlbar-slot 属性の子要素を移し、slot を削除する。identity box や検索モード表示などの参照も取得する。
- 触るとき: 新しいスロットを追加する、または子要素の指定方法(urlbar-slot 属性)を変えるとき。
- 呼び出し先: `slot.getAttribute()`, `slot.parentNode.insertBefore()`, `slot.remove()`, `this._searchModeIndicator?.querySelector()`, `this.querySelector()`, `this.querySelectorAll()`
- 参照: `this._identityBox`, `this._revertButton`, `this._searchModeIndicator`, `this._searchModeIndicatorClose`, `this._searchModeIndicatorTitle`

## SmartbarInput.#initOnce()
- 位置: L425-536
- 役割: 初回接続時に sap-name を読んでマークアップを挿入し、スマートバーなら CTA と文脈チップを初期化する。controller、view、eventBufferer を作り、プロパティ転送と placeholder、engine store の初期化を行う。
- 触るとき: 初回描画の初期化順序を変えるとき、またはスマートバー専用の初期化処理を追加するとき。
- 呼び出し先: `Object.defineProperty()`, `this._setPlaceholder()`, `this.appendChild()`, `this.controller.addListener()`, `this.controller.maybeInitEngineStore()`, `this.dispatchEvent()`, `this.documentGlobal.requestAnimationFrame()`, `this.getAttribute()`, `this.querySelector()`
- 条件付き依存: `if (document.readyState === "loading")` → `document.addEventListener()`
- 条件付き依存: `if (document.readyState === "loading")` → `this.#populateSlots()`
- 条件付き依存: `if (!(document.readyState === "loading"))` → `this.#populateSlots()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#ensureSmartbarEditor()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.querySelector()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this._inputCta.addEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.addEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#findWebsiteContextChipsContainer()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#updateContextChips()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#updateCtaSearchEngineInfo()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#initEngineStoreAfterPaint().then()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#initEngineStoreAfterPaint()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#deferUpdatePlaceholder()`
- 参照: `SmartbarInput.fragment`, `document.readyState`, `smartbarGlow.referenceElement`, `this.#isAddressbar`, `this.#isSmartbarMode`, `this.#sapName`, `this._inputContainer`, `this._inputCta`, `this.controller`, `this.eventBufferer`, `this.inputField`, `this.panel`, `this.searchModeSwitcher`, `this.smartbarAction`, `this.view`

## SmartbarInput.get()
- 位置: L505-507
- 役割: 転送対象の入力欄プロパティ(placeholder、readOnly、selectionStart、selectionEnd のいずれか)を内部の inputField から読む。
- 触るとき: 外部から入力欄の値や選択位置を読む経路を変えるとき。
- 参照: `this.inputField`

## SmartbarInput.set()
- 位置: L508-510
- 役割: 転送対象の入力欄プロパティへ、内部の inputField を通して値を書き込む。
- 触るとき: 外部から入力欄のプロパティを書き換える経路を変えるとき。
- 参照: `this.inputField`

## SmartbarInput.attributeChangedCallback()
- 位置: L538-544
- 役割: open 属性が変わったときだけ updatePopover を呼ぶ。
- 触るとき: ポップオーバーの開閉を属性の変化で駆動している箇所を追うとき。
- 呼び出し先: `this.updatePopover()`

## SmartbarInput.connectedCallback()
- 位置: L546-555
- 役割: searchbar で新検索ウィジェットが無効なら何もせず、それ以外は #init を呼ぶ。
- 触るとき: 接続時の初期化を省く条件(browser.search.widget.new など)を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#init()`, `this.getAttribute()`

## SmartbarInput.#init()
- 位置: L557-633
- 役割: 未初期化なら #initOnce を呼び、コンテキストメニューと検索モード切替を接続する。ツールバーが非表示、taskbartab、readOnly のいずれかならアンカーを解放して終える。そうでなければ入力欄とウィンドウのイベント、パネルのイベントを登録し、placeholder とポップオーバーのアンカーを設定する。
- 触るとき: イベントリスナーを登録する条件(ツールバーの可視性や readOnly)を変えるとき、または新しいリスナーを足すとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `this.#initContextMenuItems()`, `this.#updatePopoverAnchor()`, `this._addObservers()`, `this._initCopyCutController()`, `this._inputContainer.addEventListener()`, `this.addEventListener()`, `this.closest()`, `this.inputField.addEventListener()`, `this.searchModeSwitcher.connect()`, `this.view.panel.addEventListener()`, `this.window.addEventListener()`, `this.window.document.documentElement.hasAttribute()`
- 条件付き依存: `if (!this.controller)` → `this.#initOnce()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `this.parentNode.setAttribute()`
- 条件付き依存: `if ( !this.window.toolbar.visible || this.window.document.documentElement.hasAttribute("taskbartab") || this.readOnly )` → `this.#releasePopoverAnchor()`
- 条件付き依存: `if (UrlbarContentUtils.getPlatform() == "win")` → `this.window.addEventListener()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.addGBrowserListeners()`
- 条件付き依存: `if (this.controller.engineStore.initialized)` → `this.searchModeSwitcher.updateSearchIcon()`
- 条件付き依存: `if (this.controller.engineStore.initialized)` → `this.updatePlaceholder()`
- 条件付き依存: `if (!(this.controller.engineStore.initialized))` → `this.#initPlaceholderFromPref()`
- 参照: `SmartbarInput.#inputFieldEvents`, `this.#canOpenPopover`, `this.controller`, `this.controller.engineStore.initialized`, `this.readOnly`, `this.sapName`, `this.window.gBrowser`, `this.window.toolbar.visible`

## SmartbarInput.disconnectedCallback()
- 位置: L635-644
- 役割: connectedCallback と同じ条件で #uninit を呼ぶ。
- 触るとき: 切断時の後始末を行う条件を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#uninit()`, `this.getAttribute()`

## SmartbarInput.#uninit()
- 位置: L646-727
- 役割: #init で登録したリスナー、controller の購読、検索モード切替、copy/cut コントローラーを解除する。searchbar では overflows 属性も外す。
- 触るとき: #init にリスナーを追加したとき、対応する解除を忘れていないか確かめるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `UrlbarPrefs.removeObserver()`, `this.#removeContextMenuItems()`, `this._inputContainer.removeEventListener()`, `this._removeObservers()`, `this.controller.removeListener()`, `this.inputField.removeEventListener()`, `this.removeEventListener()`, `this.searchModeSwitcher.disconnect()`, `this.view.panel.removeEventListener()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this.sapName == "searchbar")` → `this.parentNode.removeAttribute()`
- 条件付き依存: `if (this._copyCutController)` → `this.inputField.controllers.removeController()`
- 条件付き依存: `if (UrlbarContentUtils.getPlatform() == "win")` → `this.window.removeEventListener()`
- 条件付き依存: `if (this.#scrollAnimationId)` → `this.window.cancelAnimationFrame()`
- 条件付き依存: `if (this.#gBrowserListenersAdded)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this.#gBrowserListenersAdded)` → `this.window.gBrowser.removeTabsProgressListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this._inputCta.removeEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.removeEventListener()`
- 参照: `SmartbarInput.#inputFieldEvents`, `this.#gBrowserListenersAdded`, `this.#isSmartbarMode`, `this.#scrollAnimationId`, `this._copyCutController`, `this.document`, `this.sapName`, `this.window`

## SmartbarInput.#editContextMenu()
- 位置: L736-738
- 役割: 入力欄を含むドキュメントの共有 EditContextMenu を返す。スマートバーではこれが chrome 文書の側にある。
- 触るとき: 文脈メニューの項目を登録・削除する先を変えるとき、またはスマートバーが別ドキュメントに置かれる場合の参照先を確かめるとき。
- 参照: `this.documentGlobal.EditContextMenu`

## SmartbarInput.#initContextMenuItems()
- 位置: L751-766
- 役割: EditContextMenu が無ければ何もしない。アドレスバーとスマートバーでは自動除去の項目を、スマートバーでは貼り付けして開く項目を登録し、アドレスバーでは共有時の除去と検索エンジン追加の項目も加える。
- 触るとき: 文脈メニューに出す項目を、アドレスバーとスマートバーのどちらで出すかを変えるとき。
- 呼び出し先: `this.#initAddSearchEngines()`, `this._initPasteAndGo()`, `this._initStripOnShare()`
- 条件付き依存: `if (this.#isAddressbar || this.#isSmartbarMode)` → `this._initAutofillDismiss()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this._initPasteAndGo()`
- 参照: `this.#editContextMenu`, `this.#isAddressbar`, `this.#isSmartbarMode`

## SmartbarInput.#initAddSearchEngines()
- 位置: L772-786
- 役割: 検索エンジン追加メニュー用の項目セットを登録する。区切り線は createItems で作り、項目は開くたび onShowing で AddSearchEngineHelper から取り直す。
- 触るとき: 検索エンジン追加メニューの表示内容や更新のタイミングを変えるとき。
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L774-780
- 役割: 検索エンジン追加メニューの先頭に入れる区切り線を含む DocumentFragment を作って返す。
- 触るとき: 検索エンジン追加メニューの区切り線の構成を変えるとき。
- 呼び出し先: `fragment.appendChild()`, `this.addSearchEngineHelper.createContextSeparator()`, `this.ownerDocument.createDocumentFragment()`

## onShowing()
- 位置: L781-784
- 役割: メニューを開くたびに項目配列を空にし、AddSearchEngineHelper が返す最新の項目で入れ直す。
- 触るとき: メニューを開いた時点で検索エンジン項目が古くならないようにする仕組みを追うとき。
- 呼び出し先: `items.push()`, `this.addSearchEngineHelper.refreshContextMenu()`
- 参照: `items.length`

## SmartbarInput.#addContextMenuItems()
- 位置: L794-801
- 役割: 項目セットに「入力欄がこの input のときだけ対象」という matches を足して EditContextMenu に登録し、返された項目セットを保持する。
- 触るとき: 文脈メニューの項目を新しく追加し、他の入力欄に出ないようにしたいとき。
- 呼び出し先: `this.#contextMenuItemSets.push()`, `this.#editContextMenu.addItems()`

## matches()
- 位置: L798-798
- 役割: 文脈メニューが開かれた入力欄が、この SmartbarInput の inputField と同じかを判定する。
- 触るとき: 共有メニューに対して項目の出し分けを変えるとき。
- 参照: `this.inputField`

## SmartbarInput.#removeContextMenuItems()
- 位置: L807-812
- 役割: 保持している項目セットをすべて EditContextMenu から外し、配列を空にする。
- 触るとき: 切断時に項目が残って他の入力欄のメニューに出ないか確かめるとき。
- 呼び出し先: `this.#editContextMenu.removeItems()`
- 参照: `this.#contextMenuItemSets`

## SmartbarInput.#initSmartbarContextMenu()
- 位置: L817-829
- 役割: マルチライン編集部の contextmenu を受け、全選択、貼り付け用の初期化を行ってから、カーソル位置に共有の文脈メニューを開く。
- 触るとき: スマートバーで右クリックしたときのメニューの開き方を変えるとき。
- 呼び出し先: `event.preventDefault()`, `this.#editContextMenu.open()`, `this.#initSmartbarContextMenuPaste()`, `this.#maybeSelectAll()`, `this.inputField.addEventListener()`
- 参照: `event.button`, `this.#editContextMenu`, `this.inputField`

## SmartbarInput.#initSmartbarContextMenuPaste()
- 位置: L839-866
- 役割: cmd_paste の command を横取りし、編集部の paste に直接渡す。一度だけ登録される。
- 触るとき: Windows の shadow DOM で貼り付けが届かない問題(Bug 2047067 の回避)を扱うとき、またはその回避を外すとき。
- 呼び出し先: `event.stopPropagation()`, `this.#ensureSmartbarEditor()`, `this.#readClipboardData()`, `this.ownerDocument .getElementById()`, `this.ownerDocument .getElementById("cmd_paste") .addEventListener()`
- 条件付き依存: `if (editor && dt)` → `editor.paste()`
- 参照: `this.#editContextMenu.input`, `this.#smartbarContextMenuPasteInitialized`, `this.#smartbarInputController?.input`, `this.inputField`

## SmartbarInput.#readClipboardData()
- 位置: L868-898
- 役割: クリップボードの text/plain を読み、DataTransfer に詰めて返す。読めない場合や例外時は null を返す。
- 触るとき: スマートバーで貼り付け内容を取得する経路を調べるとき、またはクリップボードの型を増やすとき。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `data.value?.QueryInterface()`, `dt.setData()`, `xferable.addDataFlavor()`, `xferable.getTransferData()`, `xferable.init()`
- 条件付き依存: `if (windowContext)` → `Services.clipboard.getData()`
- 条件付き依存: `if (!(windowContext))` → `Services.clipboard.getData()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `Ci.nsISupportsString`, `Ci.nsITransferable`, `data.value?.QueryInterface(Ci.nsISupportsString).data`, `this.documentGlobal?.browsingContext?.currentWindowContext`
- XPCOM: `nsIClipboard` / [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## SmartbarInput.addGBrowserListeners()
- 位置: L900-920
- 役割: gBrowser が使えて未登録なら進捗リスナーを付け、アドレスバーかスマートバーなら TabSelect と TabClose、スマートバーなら TabAttrModified を登録する。
- 触るとき: タブ切り替えや閉じるに応じて入力欄を更新する経路を追加・変更するとき。
- 呼び出し先: `this.window.gBrowser.addTabsProgressListener()`
- 条件付き依存: `if (this.#isAddressbar || this.#isSmartbarMode)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 参照: `this.#gBrowserListenersAdded`, `this.#isAddressbar`, `this.#isSmartbarMode`, `this.window.gBrowser`

## SmartbarInput.#initSmartbarEditor()
- 位置: L922-929
- 役割: 入力欄から editor アダプターを作り、最大文字数を設定して SmartbarInputController を組み立てる。その後、文脈メニューを初期化する。
- 触るとき: スマートバーの編集部の初期化手順や文字数上限を変えるとき。
- 呼び出し先: `createEditor()`, `this.#initSmartbarContextMenu()`
- 参照: `adapter.editor`, `adapter.input`, `adapter.input.maxLength`, `lazy.SmartbarInputController`, `this.#smartbarEditor`, `this.#smartbarInputController`, `this.inputField`

## SmartbarInput.#ensureSmartbarEditor()
- 位置: L931-936
- 役割: まだ controller が無ければ編集部を初期化し、スマートバーの editor を返す。
- 触るとき: 編集部を使う前に必ず初期化されているかを確かめる箇所を追うとき。
- 条件付き依存: `if (!this.#smartbarInputController)` → `this.#initSmartbarEditor()`
- 参照: `this.#smartbarEditor`, `this.#smartbarInputController`

## SmartbarInput.#setInputValue()
- 位置: L938-944
- 役割: スマートバーなら controller の setValue、そうでなければ inputField.value に値を設定する。
- 触るとき: 入力欄への値の設定経路を変えるとき。
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.setValue()`
- 参照: `this.#smartbarInputController`, `this.inputField.value`

## SmartbarInput.#setInputRangeText()
- 位置: L946-957
- 役割: スマートバーなら controller の setRangeText、そうでなければ inputField の setRangeText で範囲を置き換える。
- 触るとき: 入力欄の一部だけを差し替える処理を変えるとき。
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.setRangeText()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.setRangeText()`
- 参照: `this.#smartbarInputController`

## SmartbarInput.addSearchEngineHelper()
- 位置: L966-968
- 役割: AddSearchEngineHelper を遅延生成して返す。
- 触るとき: 検索エンジン追加の項目を生成する起点を追うとき。
- 参照: `this.#addSearchEngineHelper`

## SmartbarInput.#getValueFormatter()
- 位置: L970-972
- 役割: UrlbarValueFormatter を遅延生成して返す。
- 触るとき: 入力欄の値の装飾(URL の色分けなど)の担当を追うとき。
- 参照: `lazy.UrlbarValueFormatter`, `this.#valueFormatter`

## SmartbarInput.sapName()
- 位置: L974-976
- 役割: sap-name(newtab_searchbar、searchbar、smartbar、urlbar のいずれか)を返す。
- 触るとき: テレメトリやログで呼び出し元の種類を判断する箇所を追うとき。
- 参照: `this.#sapName`

## SmartbarInput.isSearchbarSAP()
- 位置: L984-986
- 役割: sap-name から UrlbarShared.isSearchbarSAP で検索専用のバーかどうかを返す。
- 触るとき: 検索バー専用の挙動と URL バー共通の挙動を分けている箇所を変えるとき。
- 呼び出し先: `UrlbarShared.isSearchbarSAP()`
- 参照: `this.#sapName`

## SmartbarInput.parentController()
- 位置: L988-990
- 役割: controller の親 controller を返す。
- 触るとき: 子の入力欄から親の検索コントローラーに届く経路を追うとき。
- 参照: `this.controller.parentController`

## SmartbarInput.smartbarAction()
- 位置: L992-996
- 役割: smartbar-action 属性があればそれを、無ければ内部の値を SmartbarAction として返す。
- 触るとき: CTA ボタンの現在の動作を読む箇所を追うとき。
- 呼び出し先: `this.getAttribute()`
- 参照: `this.#smartbarAction`

## SmartbarInput.detectedIntent()
- 位置: L1001-1003
- 役割: インテント判定で検出された操作(SmartbarAction)を返す。
- 触るとき: 入力内容から推定された操作を、CTA の表示や送信先の判断に使う箇所を確かめるとき。
- 参照: `this.#detectedIntent`

## SmartbarInput.assistantIsGenerating()
- 位置: L1008-1010
- 役割: アシスタントが回答を生成中かどうかを返す。
- 触るとき: 生成中の表示や停止ボタンの状態を確かめるとき。
- 参照: `this.#smartbarAssistantIsGenerating`

## SmartbarInput.assistantIsGenerating()
- 位置: L1012-1022
- 役割: 値が変わったときだけ内部状態を更新し、生成中なら CTA を stop にし、そうでなければ現在の smartbarAction に戻す。
- 触るとき: 生成開始・終了時に CTA の表示が切り替わらない不具合を調べるとき。
- 条件付き依存: `if (value)` → `this._inputCta.setAttribute()`
- 条件付き依存: `if (!(value))` → `this._inputCta.setAttribute()`
- 参照: `this.#smartbarAssistantIsGenerating`, `this.smartbarAction`

## SmartbarInput.sapLocation()
- 位置: L1029-1031
- 役割: サイドバー表示なら sidebar、それ以外は fullpage を返す。
- 触るとき: テレメトリに載せる表示場所を変えるとき。
- 参照: `this.#isSidebarMode`

## SmartbarInput.windowMode()
- 位置: L1038-1041
- 役割: 常に smartwindow を返す(スマートウィンドウ内に置かれる前提)。
- 触るとき: テレメトリの window_mode の値を見直すとき。

## SmartbarInput.#aiWindow()
- 位置: L1046-1049
- 役割: ルートノードの host から最も近い ai-window 要素を返す。
- 触るとき: 会話情報やモデル名を親の AI ウィンドウから取る経路を追うとき。
- 呼び出し先: `root.host?.closest()`, `this.getRootNode()`

## SmartbarInput.conversationTelemetryInfo()
- 位置: L1056-1061
- 役割: 親の ai-window から chat_id(会話 ID、無ければ空文字)と message_seq(メッセージ数、無ければ 0)を返す。
- 触るとき: 会話単位のテレメトリに載せる値を変えるとき。
- 参照: `this.#aiWindow?.conversationId`, `this.#aiWindow?.conversationMessageCount`

## SmartbarInput.modelName()
- 位置: L1068-1070
- 役割: 親の ai-window のモデル名を返し、無ければ空文字を返す。
- 触るとき: テレメトリや表示で使うモデル名の取得元を確かめるとき。
- 参照: `this.#aiWindow?.modelName`

## SmartbarInput.contextWebsitesCount()
- 位置: L1077-1079
- 役割: 解決済みの文脈サイトの件数を返す。
- 触るとき: 選択中の文脈タブ数を表示や送信内容に反映する箇所を変えるとき。
- 呼び出し先: `this.getResolvedContextWebsites()`
- 参照: `this.getResolvedContextWebsites().length`

## SmartbarInput.smartbarAction()
- 位置: L1086-1094
- 役割: 値が変わったときだけ内部値と smartbar-action 属性を更新し、生成中でなければ CTA の action にも反映する。
- 触るとき: CTA の動作を外部から切り替える処理を変えるとき。
- 条件付き依存: `if (this.#smartbarAction != action)` → `this.setAttribute()`
- 条件付き依存: `if (!this.#smartbarAssistantIsGenerating)` → `this._inputCta.setAttribute()`
- 参照: `this.#smartbarAction`, `this.#smartbarAssistantIsGenerating`

## SmartbarInput.blur()
- 位置: L1096-1102
- 役割: controller があればその blur、無ければ inputField の blur を呼ぶ。
- 触るとき: スマートバーからフォーカスを外す経路を変えるとき。
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.blur()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.blur()`
- 参照: `this.#smartbarInputController`

## SmartbarInput.placeholder()
- 位置: L1107-1111
- 役割: controller の placeholder、無ければ inputField の placeholder を返す。
- 触るとき: placeholder を読む側が何を見ているかを確かめるとき。
- 参照: `this.#smartbarInputController?.placeholder`, `this.inputField?.placeholder`

## SmartbarInput.placeholder()
- 位置: L1113-1121
- 役割: controller があればそこへ、無ければ inputField へ placeholder を設定する。
- 触るとき: placeholder の設定先の切り替えを変えるとき。
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.placeholder`, `this.inputField`, `this.inputField.placeholder`

## SmartbarInput.readOnly()
- 位置: L1126-1128
- 役割: controller の readOnly、無ければ inputField の readOnly を返す。
- 触るとき: 読み取り専用状態の判定元を確かめるとき。
- 参照: `this.#smartbarInputController?.readOnly`, `this.inputField?.readOnly`

## SmartbarInput.readOnly()
- 位置: L1130-1138
- 役割: controller があればそこへ、無ければ inputField へ readOnly を設定する。
- 触るとき: 読み取り専用の切り替え経路を変えるとき。
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.readOnly`, `this.inputField`, `this.inputField.readOnly`

## SmartbarInput.selectionStart()
- 位置: L1143-1149
- 役割: controller の selectionStart、無ければ inputField の値、どちらも無ければ 0 を返す。
- 触るとき: 選択開始位置を読む箇所を追うとき。
- 参照: `this.#smartbarInputController?.selectionStart`, `this.inputField?.selectionStart`

## SmartbarInput.selectionStart()
- 位置: L1151-1159
- 役割: controller があればそこへ、無ければ inputField の selectionStart に値を設定する。
- 触るとき: 選択開始位置の書き込み経路を変えるとき。
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.selectionStart`, `this.inputField`, `this.inputField.selectionStart`

## SmartbarInput.selectionEnd()
- 位置: L1164-1170
- 役割: controller の selectionEnd、無ければ inputField の値、どちらも無ければ 0 を返す。
- 触るとき: 選択終了位置を読む箇所を追うとき。
- 参照: `this.#smartbarInputController?.selectionEnd`, `this.inputField?.selectionEnd`

## SmartbarInput.selectionEnd()
- 位置: L1172-1180
- 役割: controller があればそこへ、無ければ inputField の selectionEnd に値を設定する。
- 触るとき: 選択終了位置の書き込み経路を変えるとき。
- 参照: `this.#smartbarInputController`, `this.#smartbarInputController.selectionEnd`, `this.inputField`, `this.inputField.selectionEnd`

## SmartbarInput.onPrefChanged()
- 位置: L1188-1205
- 役割: keyword.enabled の変更で placeholder を更新する。browser.search.widget.new が変わったら、検索バーが接続中なら #init か #uninit を呼ぶ。
- 触るとき: 設定変更に応じて検索バーの初期化状態を切り替える処理を変えるとき。
- 呼び出し先: `this.getAttribute()`, `this.updatePlaceholder()`
- 条件付き依存: `if (this.getAttribute("sap-name") == "searchbar" && this.isConnected)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("browser.search.widget.new"))` → `this.#init()`
- 条件付き依存: `if (!(UrlbarPrefs.get("browser.search.widget.new")))` → `this.#uninit()`
- 参照: `this.isConnected`

## SmartbarInput.formatValue()
- 位置: L1210-1215
- 役割: アドレスバーで editor があるとき、値の装飾を UrlbarValueFormatter で更新する。
- 触るとき: 入力欄の文字の装飾が古いまま残る不具合を調べるとき。
- 条件付き依存: `if (this.#isAddressbar && this.editor)` → `this.#getValueFormatter().update()`
- 条件付き依存: `if (this.#isAddressbar && this.editor)` → `this.#getValueFormatter()`
- 参照: `this.#isAddressbar`, `this.editor`

## SmartbarInput.focus()
- 位置: L1217-1232
- 役割: beforefocus を発火し、キャンセルされなければ controller か inputField にフォーカスを移す。
- 触るとき: フォーカス要求を外部から受けたときの経路を変えるとき。
- 呼び出し先: `this.inputField.dispatchEvent()`
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.focus()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.focus()`
- 参照: `beforeFocus.defaultPrevented`, `this.#smartbarInputController`

## SmartbarInput.select()
- 位置: L1234-1253
- 役割: beforeselect を発火し、キャンセルされなければ全選択する。選択中は _suppressPrimaryAdjustment を立てて primary selection を変えないようにする。
- 触るとき: 全選択の動作や、プライマリ選択を書き換えないための抑止を変えるとき。
- 呼び出し先: `this.inputField.dispatchEvent()`
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController?.select()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.select()`
- 参照: `beforeSelect.defaultPrevented`, `this.#smartbarInputController`, `this._suppressPrimaryAdjustment`

## SmartbarInput.setSelectionRange()
- 位置: L1255-1277
- 役割: beforeselect を発火し、キャンセルされなければ指定範囲を選択する。その間は _suppressPrimaryAdjustment を立てる。
- 触るとき: 選択範囲の指定を外部から受ける経路を変えるとき。
- 呼び出し先: `this.inputField.dispatchEvent()`
- 条件付き依存: `if (this.#smartbarInputController)` → `this.#smartbarInputController.setSelectionRange()`
- 条件付き依存: `if (!(this.#smartbarInputController))` → `this.inputField.setSelectionRange()`
- 参照: `beforeSelect.defaultPrevented`, `this.#smartbarInputController`, `this._suppressPrimaryAdjustment`

## SmartbarInput.saveSelectionStateForBrowser()
- 位置: L1279-1291
- 役割: 値が空なら全選択扱いにして、選択位置と shouldUntrim(URL の前置き除去を戻すか)を browser の状態へ保存する。
- 触るとき: タブを切り替える前に入力欄の選択状態を保存する挙動を変えるとき。
- 呼び出し先: `this.getBrowserState()`
- 参照: `Number.MAX_SAFE_INTEGER`, `state.selection`, `this._protocolIsTrimmed`, `this._wwwIsTrimmed`, `this.selectionEnd`, `this.selectionStart`, `this.value`

## SmartbarInput.restoreSelectionStateForBrowser()
- 位置: L1293-1307
- 役割: フォーカスしたうえで、保存された shouldUntrim が真なら URL を展開し、保存された範囲を値の長さに収めて選択し直す。
- 触るとき: タブを戻したときに入力欄の選択と URL の表示が復元されない問題を調べるとき。
- 呼び出し先: `this.focus()`, `this.getBrowserState()`
- 条件付き依存: `if (state.selection.shouldUntrim)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (state.selection)` → `this.setSelectionRange()`
- 条件付き依存: `if (state.selection)` → `Math.min()`
- 参照: `state.selection`, `state.selection.end`, `state.selection.shouldUntrim`, `state.selection.start`, `this.value.length`

## SmartbarInput.setURI()
- 位置: L1326-1508
- 役割: アドレスバーに表示する URI を設定する。値が空のときはブラウザの現在 URI(認証プロンプト URI を含む)から表示文字列を作り、有効性と選択位置を計算してプロキシ状態と検索モードを更新し、SetURI イベントを出す。
- 触るとき: タブ切り替え、セッション復元、ページ遷移で URL 欄の表示が古いままになる、または選択が飛ぶ不具合を調べるとき。
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`, `lazy.UrlbarSearchTermsPersistence.searchModeMatchesState()`, `this.#handlePersistedSearchTerms()`, `this.getBrowserState()`, `this.inputField.dispatchEvent()`, `this.setPageProxyState()`, `this.setValue()`, `this.toggleAttribute()`
- 条件付き依存: `if ( dueToTabSwitch && UrlbarPrefs.getScotchBonnetPref("scotchBonnet.persistSearchMode") )` → `this._updateSearchModeUI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `Services.io.createExposableURI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `this.window.isInitialPage()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if (!( this.window.isInitialPage(uri) && lazy.BrowserUIUtils.checkEmptyPageOrigin( this.window.gBrowser.selectedBrowser, uri ) ))` → `losslessDecodeURI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `this.window.isBlankPageURL()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `lazy.ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (!(value === null || (!value && dueToTabSwitch)))` → `this.window.isInitialPage()`
- 条件付き依存: `if (!(value === null || (!value && dueToTabSwitch)))` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if (this.focused && value != previousUntrimmedValue)` → `value.substring()`
- 条件付き依存: `if (this.focused && value != previousUntrimmedValue)` → `previousUntrimmedValue.substring()`
- 条件付き依存: `if ( previousSelectionStart != previousSelectionEnd && value.substring(previousSelectionStart, previousSelectionEnd) === previousUntrimmedValue.substring( previo...)` → `this.setSelectionRange()`
- 条件付き依存: `if ( previousSelectionEnd && (previousUntrimmedValue.length === previousSelectionEnd || value.length <= previousSelectionEnd) )` → `this.setSelectionRange()`
- 条件付き依存: `if (!( previousSelectionEnd && (previousUntrimmedValue.length === previousSelectionEnd || value.length <= previousSelectionEnd) ))` → `this.setSelectionRange()`
- 条件付き依存: `if (dueToTabSwitch && !valid)` → `this.restoreSearchModeState()`
- 参照: `"www.".length`, `UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.BrowserUIUtils.trimURLProtocol.length`, `previousUntrimmedValue.length`, `state.persist.isDefaultEngine`, `state.persist.originalEngineName`, `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.#isOpenedPageInBlankTargetLoading`, `this._protocolIsTrimmed`, `this._wwwIsTrimmed`, `this.focused`, `this.getBrowserState(this.window.gBrowser.selectedBrowser) .isUnifiedSearchButtonAvailable`, `this.searchMode`, `this.selectionEnd`, `this.selectionStart`, `this.untrimmedValue`, `this.userTypedValue`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser`, `this.window.gBrowser.selectedBrowser.currentAuthPromptURI`, `uri.spec`, `value.length`
- XPCOM: `Services.io`

## SmartbarInput.makeURIReadable()
- 位置: L1519-1534
- 役割: リーダー表示の URI なら元の URL に戻し、そうでなければ createExposableURI で認証情報を除いた URI を返す。変換できなければ元の URI を返す。
- 触るとき: ユーザー名やパスワードを含む URI が URL 欄に出ないように見せる経路を変えるとき。
- 呼び出し先: `Services.io.createExposableURI()`, `lazy.ReaderMode.getOriginalUrlObjectForDisplay()`
- 参照: `uri.displaySpec`
- XPCOM: `Services.io`

## SmartbarInput.onLocationChange()
- 位置: L1547-1573
- 役割: トップレベルの遷移だけを扱う。スマートバーなら選択中のブラウザのときに文脈チップを更新する。アドレスバーでは背景タブの統合検索ボタンを無効にし、履歴による移動なら bounce イベントを送る。
- 触るとき: ページ遷移に合わせて文脈チップや統合検索ボタンの状態が古くならない経路を調べるとき。
- 呼び出し先: `this.window.isBlankPageURL()`
- 条件付き依存: `if (browser == this.window.gBrowser.selectedBrowser)` → `this.#updateContextChips()`
- 条件付き依存: `if ( browser != this.window.gBrowser.selectedBrowser && !this.window.isBlankPageURL(locationURI.spec) )` → `this.getBrowserState()`
- 条件付き依存: `if (webProgress.loadType & Ci.nsIDocShell.LOAD_CMD_HISTORY)` → `lazy.handleBounceEventTrigger()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `locationURI.spec`, `this.#isSmartbarMode`, `this.getBrowserState(browser).isUnifiedSearchButtonAvailable`, `this.window.gBrowser.selectedBrowser`, `webProgress.isTopLevel`, `webProgress.loadType`
- XPCOM: [`nsIDocShell`](../../../../docshell/base/nsIDocShell.idl.md)

## SmartbarInput.handleEvent()
- 位置: L1580-1622
- 役割: DOM イベントの振り分け口。shown では intentChangePreview を記録し、aiwindow-input-cta の事件は #handleSmartbarCtaAction へ送り、ai-website-chip:remove では文脈項目を外して記録する。それ以外は _on_<type> を呼び、無ければ例外を投げる。
- 触るとき: 新しいイベントを購読させたい、またはイベント名から処理メソッドへの対応を確かめたいとき。
- 呼び出し先: `event.type.startsWith()`
- 条件付き依存: `if (event.type === "shown")` → `Glean.smartWindow.intentChangePreview.record()`
- 条件付き依存: `if (event.type === "shown")` → `String()`
- 条件付き依存: `if (event.type.startsWith("aiwindow-input-cta:"))` → `this.#handleSmartbarCtaAction()`
- 条件付き依存: `if (event.type === "ai-website-chip:remove")` → `this.removeContextMention()`
- 条件付き依存: `if (event.type === "ai-website-chip:remove")` → `Glean.smartWindow.removeTab.record()`
- 条件付き依存: `if (event.type === "ai-website-chip:remove")` → `String()`
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 条件付き依存: `if (methodName in this)` → `console.error()`
- 参照: `(event).detail`, `event.type`, `this.#contextWebsites.length`, `this.conversationTelemetryInfo`, `this.sapLocation`, `this.smartbarAction`

## SmartbarInput.handleCommand()
- 位置: L1630-1655
- 役割: 右クリックは無視する。パネルが開いていて one-off 検索ボタンが選択されていれば、その検索を実行する。それ以外は handleNavigation に渡す。
- 触るとき: Enter やクリックで入力内容を送信する経路で、one-off の選択が優先される条件を変えるとき。
- 呼び出し先: `MouseEvent.isInstance()`, `this.handleNavigation()`
- 条件付き依存: `if (selectedOneOff && (!isMouseEvent || event.target == selectedOneOff))` → `this.view.oneOffSearchButtons.handleSearchCommand()`
- 参照: `event.button`, `event.target`, `selectedOneOff.engine?.name`, `selectedOneOff.source`, `this.view.isOpen`, `this.view.oneOffSearchButtons?.selectedButton`

## SmartbarInput.#dispatchSmartbarCommitEvent()
- 位置: L1668-1691
- 役割: smartbar-commit イベントを発火し、値、動作、解決済みの文脈項目、ページ URL、検出された意図、送信方法、既定の検索エンジン名を detail に入れる。
- 触るとき: 送信時にチャット側へ渡す情報を増やす、または送信イベントの項目を変えるとき。
- 呼び出し先: `this.dispatchEvent()`, `this.getContextPageUrl()`, `this.getResolvedContextWebsites()`
- 参照: `this.controller.engineStore.default?.name`, `this.detectedIntent`, `this.sapLocation`, `this.smartbarAction`

## SmartbarInput.submitChat()
- 位置: L1701-1709
- 役割: 動作を chat に切り替えたうえで、その値を smartbar-commit イベントとして送る。
- 触るとき: 入力をチャットとして送る経路の挙動を追うとき。
- 呼び出し先: `this.#dispatchSmartbarCommitEvent()`
- 参照: `this.smartbarAction`

## SmartbarInput.#handleSuppressedNavigation()
- 位置: L1720-1735
- 役割: クエリが抑止されている場合の Enter 処理。動作がロックされていればその動作で送信し、URL 候補があれば pickResult で開き、それ以外は値をチャットとして送る。
- 触るとき: クエリ抑止中に Enter を押したとき、URL として開くかチャットに送るかの分岐を変えるとき。
- 呼び出し先: `this.submitChat()`
- 条件付き依存: `if (this.#smartbarActionLocked)` → `this.#submitLockedAction()`
- 条件付き依存: `if (this._resultForCurrentValue?.type == UrlbarShared.RESULT_TYPE.URL)` → `this.pickResult()`
- 参照: `UrlbarShared.RESULT_TYPE.URL`, `this.#smartbarActionLocked`, `this._lastSearchString`, `this._resultForCurrentValue`, `this._resultForCurrentValue?.type`, `this.untrimmedValue`, `this.value`

## SmartbarInput.#shouldHandleSuppressedNavigation()
- 位置: L1737-1743
- 役割: 永続的な抑止、メンションの有無、エージェントコマンドのいずれかに当たるかを返す。
- 触るとき: Enter を抑止経路に流す条件を増減させるとき。
- 参照: `this.#isAgentCommand`, `this._permanentlySuppressStartQuery`, `this.inputField.hasMention`

## SmartbarInput.#handleSmartbarCtaAction()
- 位置: L1761-1800
- 役割: 停止要求は smartbar-stop-generation として送る。動作や検索エンジンの選択では動作をロックして入力欄へフォーカスを戻すだけで送信しない。それ以外は動作を設定し、必要なら engagement を開始して handleNavigation に進む。
- 触るとき: CTA のクリックで送信されるか、動作の選択だけで止まるかの違いを調べるとき。
- 呼び出し先: `this.handleNavigation()`
- 条件付き依存: `if (event.type === "aiwindow-input-cta:on-stop")` → `this.dispatchEvent()`
- 条件付き依存: `if (isExplicitAction)` → `this.#updateGoGuardrail()`
- 条件付き依存: `if (isExplicitAction)` → `this.#updateCtaSearchEngineInfo()`
- 条件付き依存: `if (isExplicitAction)` → `this.focus()`
- 条件付き依存: `if (!this.focused)` → `this.controller.engagementEvent.start()`
- 参照: `event.detail.action`, `event.detail.engineName`, `event.type`, `this.#smartbarActionLocked`, `this.#smartbarSearchEngineName`, `this.focused`, `this.smartbarAction`, `this.value`

## SmartbarInput.#isSafeToPickResult()
- 位置: L1810-1819
- 役割: 結果が無ければ安全でない。自動選択の見出し、チップ、AI チャット結果、入力が結果の値と一致する場合は安全とみなし、入力後に値を変えた選択は安全としない。
- 触るとき: 選択中の候補を送信時に採用してよいかの判定を変えるとき。
- 呼び出し先: `this.#getValueFromResult()`
- 参照: `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.TIP`, `result.heuristic`, `result.type`, `this.value`, `this.valueIsTyped`

## SmartbarInput.#shouldSubmitLockedAction()
- 位置: L1835-1848
- 役割: スマートバーで動作がロックされ、IME 変換中でないときに、キーボードで選んだ候補行や one-off 検索が無ければロックされた動作で送信すべきと判断する。
- 触るとき: 手動で選んだ動作と候補選択のどちらを優先するかの判定を変えるとき。
- 参照: `oneOffParams?.engine`, `result.heuristic`, `this.#isSmartbarMode`, `this.#smartbarActionLocked`

## SmartbarInput.#submitLockedAction()
- 位置: L1857-1877
- 役割: 空の値は何もせず、ロックされた動作が chat なら送信、search なら検索、navigate なら guardrail を確かめてから URL へ移動する。
- 触るとき: ユーザーが選んだ動作で送信されない不具合を調べるとき。
- 呼び出し先: `this.#submitNavigate()`, `this.#submitSearch()`, `this.submitChat()`, `value.trim()`
- 参照: `this.#goBlocked`, `this.smartbarAction`, `this.untrimmedValue`

## SmartbarInput.#submitSearch()
- 位置: L1886-1919
- 役割: 覚えていた検索エンジン、無ければ既定のエンジンで検索する。engagement を記録し、検索履歴を残してから parentController.openSERP で結果ページを開く。
- 触るとき: 検索ボタンや Enter による検索の開き方、記録される検索元を変えるとき。
- 呼び出し先: `this.#dispatchSmartbarCommitEvent()`, `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.controller.engineStore.getEngineByName()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.parentController.openSERP()`
- 参照: `engine.id`, `this.#selectedBrowserId`, `this.#smartbarSearchEngineName`, `this.controller.engineStore.default`, `this.sapLocation`, `this.windowMode`

## SmartbarInput.#submitNavigate()
- 位置: L1927-1952
- 役割: 入力を URI fixup(スキームの typo 修正を含む)で正規化し、engagement を記録してから loadURL で開く。
- 触るとき: 入力を URL として開くときの正規化やロード方法を変えるとき。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `this.#dispatchSmartbarCommitEvent()`, `this.#loadURL()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`, `Ci.nsIURIFixup.FIXUP_FLAG_PRIVATE_CONTEXT`, `fixupInfo.preferredURI.spec`, `this.isPrivate`, `this.sapLocation`, `this.windowMode`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.uriFixup`

## SmartbarInput.#goBlocked()
- 位置: L1961-1968
- 役割: 動作が navigate にロックされ、入力が空でなく、検出された意図も navigate でないときに true を返す。URL らしくない文字列の移動を止める。
- 触るとき: Go ボタンの guardrail(URL でない入力を移動させない条件)を調整するとき。
- 呼び出し先: `this.untrimmedValue.trim()`
- 参照: `this.#detectedIntent`, `this.#smartbarActionLocked`, `this.smartbarAction`

## SmartbarInput.#updateGoGuardrail()
- 位置: L1974-1976
- 役割: #goBlocked の結果を CTA の submit-disabled 属性に反映する。
- 触るとき: guardrail 中に送信ボタンが押せない見た目になっているかを確かめるとき。
- 呼び出し先: `this._inputCta?.toggleAttribute()`
- 参照: `this.#goBlocked`

## SmartbarInput.#searchModeEngineForEnterKey()
- 位置: L1990-2008
- 役割: アドレスバーで検索モードのエンジンがあり、IME 変換中でなく、結果が無いか自動選択の見出し検索の場合に、そのエンジンを返す。それ以外は null。
- 触るとき: 検索モード中の Enter で、どのエンジンで検索するかの判定を変えるとき。
- 呼び出し先: `this.controller.engineStore.getEngineByName()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `oneOffParams?.engine`, `result.heuristic`, `result.type`, `this.#isAddressbar`, `this.searchMode.engineName`, `this.searchMode?.engineName`

## SmartbarInput.#engineSearchStringForResult()
- 位置: L2017-2022
- 役割: 結果の候補文字列、無ければ検索文字列、最後に直前の検索文字列を返す。
- 触るとき: エンジン検索に使う文字列の取り方を変えるとき。
- 参照: `result.payload.query`, `result.payload.suggestion`, `this._lastSearchString`

## SmartbarInput.#selectedBrowserId()
- 位置: L2029-2031
- 役割: 選択中ブラウザの browserId を返す。gBrowser が無ければ null。
- 触るとき: 検索結果ページをどのブラウザに開くかの指定を追うとき。
- 参照: `this.window.gBrowser?.selectedBrowser?.browserId`

## SmartbarInput.#openEngineSearch()
- 位置: L2052-2084
- 役割: エンジン検索を記録(engagement と検索履歴)し、parentController.openSERP で検索結果ページを開く。ワンオフ・検索モード・Enter の各経路から共通に使われる。
- 触るとき: ワンオフや検索モードの Enter で開かれる検索結果ページの扱い(記録、開く場所、バックグラウンド指定)を変えるとき。
- 呼び出し先: `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.getSearchSource()`, `this.parentController.openSERP()`
- 参照: `engine.id`, `this.#selectedBrowserId`, `this._resultForCurrentValue`, `this.sapLocation`, `this.view.selectedResult`, `this.windowMode`

## SmartbarInput.#isAgentCommand()
- 位置: L2093-2095
- 役割: スマートバーで、入力が "/" で始まるエージェントコマンドかどうかを返す。
- 触るとき: エージェントコマンドを URL として読まずチャットに送る判定を見直すとき。
- 呼び出し先: `isAgentCommand()`
- 参照: `this.#isSmartbarMode`, `this.untrimmedValue`

## SmartbarInput.handleNavigation()
- 位置: L2112-2363
- 役割: Enter やクリックの送信処理の中心。エージェントコマンドはチャットへ送り、抑止中や @メンションありはチャットへ回す。それ以外は選択中の候補、ワンオフ、検索モード、ロックされた動作の順に判断し、URL なら loadURL、非 URL なら pickResult か resolveFallbackNavigation の結果で開く。
- 触るとき: Enter で何が開かれるかの優先順位(候補、ワンオフ、検索モード、URL 入力)を変えたり、送信時の不具合を追ったりするとき。
- 呼び出し先: `URL.canParse()`, `UrlbarPrefs.get()`, `this.#isSafeToPickResult()`, `this.#searchModeEngineForEnterKey()`, `this.#shouldSubmitLockedAction()`, `this._maybeCanonizeURL()`, `this.controller .resolveFallbackNavigation()`, `this.controller .resolveFallbackNavigation({ searchString: url, where, searchMode: this.searchMode, browserId, }) .then()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.value.startsWith()`, `this.view.getResultFromElement()`, `this.view.telemetryTypeFromElement()`, `url.trim()`
- 条件付き依存: `if (this.#isAgentCommand)` → `getAgentCommandId()`
- 条件付き依存: `if (commandId)` → `Glean.smartWindow.agentCommandSelect.record()`
- 条件付き依存: `if (commandId)` → `String()`
- 条件付き依存: `if (this.#isAgentCommand)` → `this.submitChat()`
- 条件付き依存: `if (this.#isSmartbarMode && this.#shouldHandleSuppressedNavigation)` → `this.#handleSuppressedNavigation()`
- 条件付き依存: `if ( this.#shouldSubmitLockedAction({ element, result, safeToPickResult, isComposing, oneOffParams, }) )` → `this.#submitLockedAction()`
- 条件付き依存: `if ( !isComposing && element && !searchModeEngine && (!oneOffParams?.engine || selectedPrivateEngineResult) && safeToPickResult )` → `this.pickElement()`
- 条件付き依存: `if ( UrlbarPrefs.get("experimental.hideHeuristic") && !element && !isComposing && !oneOffParams?.engine && !searchModeEngine && this._resultForCurrentValue?.heur...)` → `this.pickResult()`
- 条件付き依存: `if (!result && this.value.startsWith("@"))` → `this.view.getResultAtIndex()`
- 条件付き依存: `if (tokenAliasResult?.autofill && tokenAliasResult?.payload.keyword)` → `this.pickResult()`
- 条件付き依存: `if (oneOffParams?.engine)` → `this.#openEngineSearch()`
- 条件付き依存: `if (oneOffParams?.engine)` → `this.#engineSearchStringForResult()`
- 条件付き依存: `if (searchModeEngine)` → `this.#openEngineSearch()`
- 条件付き依存: `if (searchModeEngine)` → `this.controller.whereToOpen()`
- 条件付き依存: `if (URL.canParse(url))` → `this.#getSchemelessInput()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#dispatchSmartbarCommitEvent()`
- 条件付き依存: `if (URL.canParse(url))` → `this.#loadURL()`
- 条件付き依存: `if (!isComposing && this._resultForCurrentValue)` → `this.pickResult()`
- 条件付き依存: `if (heuristicResult)` → `this.pickResult()`
- 条件付き依存: `if (!fixup.keywordAsSent)` → `this.#getSchemelessInput()`
- 条件付き依存: `if (fixup)` → `this.#loadURL()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `console.error`, `fixup.keywordAsSent`, `fixup.postData`, `fixup.url`, `oneOffParams.engine`, `oneOffParams.openWhere`, `oneOffParams?.engine`, `oneOffParams?.openParams`, `oneOffParams?.openWhere`, `openParams.allowInheritPrincipal`, `openParams.inBackground`, `openParams.private`, `openParams.schemelessInput`, `result.payload.inPrivateWindow`, `result.payload.isPrivateEngine`, `result.type`, `this.#isAgentCommand`, `this.#isSmartbarMode`, `this.#selectedBrowserId`, `this.#shouldHandleSuppressedNavigation`, `this._lastSearchString`, `this._resultForCurrentValue`, `this._resultForCurrentValue?.heuristic`, `this.conversationTelemetryInfo`, `this.editor.composing`, `this.sapLocation`, `this.searchMode`, `this.searchMode.engineName`, `this.untrimmedValue`, `this.value`, `this.view.selectedElement`, `this.view.selectedResult`, `this.windowMode`, `tokenAliasResult?.autofill`, `tokenAliasResult?.payload.keyword`

## SmartbarInput.handleRevert()
- 位置: L2365-2381
- 役割: 入力を元に戻す。検索モードを解除し、アドレスバーでは setURI で現在のページ URL に戻し、スマートバーでは値を空にする。フォーカス中なら全選択する。
- 触るとき: Esc などで入力を取り消したときの表示が正しいかを確かめるとき。
- 条件付き依存: `if (this.#isAddressbar)` → `this.setURI()`
- 条件付き依存: `if (this.#isAddressbar && this.value && this.focused)` → `this.select()`
- 参照: `this.#isAddressbar`, `this.#isSmartbarMode`, `this.focused`, `this.searchMode`, `this.userTypedValue`, `this.value`

## SmartbarInput.maybeHandleRevertFromPopup()
- 位置: L2383-2392
- 役割: アドレスバーで、永続化された検索語を持つページのポップアップ由来なら handleRevert を呼び、テレメトリを 1 件増やす。
- 触るとき: 検索語の永続化があるときの、ポップアップからの取り消し動作を変えるとき。
- 呼び出し先: `anchorElement?.closest()`, `this.getBrowserState()`
- 条件付き依存: `if (anchorElement?.closest("#urlbar") && state.persist?.shouldPersist)` → `this.handleRevert()`
- 条件付き依存: `if (anchorElement?.closest("#urlbar") && state.persist?.shouldPersist)` → `Glean.urlbarPersistedsearchterms.revertByPopupCount.add()`
- 参照: `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.handoff()
- 位置: L2407-2418
- 役割: 新しいタブページなどの偽の検索欄から渡された文字列を検索する。エンジンがあり shouldHandOffToSearchMode が有効なら検索モードに入れて search を呼び、それ以外は通常の search を呼ぶ。
- 触るとき: 新しいタブページからの検索受け渡しで検索モードに入る条件を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("shouldHandOffToSearchMode") && searchEngine)` → `this.search()`
- 条件付き依存: `if (!(UrlbarPrefs.get("shouldHandOffToSearchMode") && searchEngine))` → `this.search()`
- 参照: `this._handoffSession`, `this._isHandoffSession`

## SmartbarInput.handlesOpenInCommands()
- 位置: L2426-2428
- 役割: 常に false を返す。pickResult が「新しいタブで開く」などの結果メニュー項目を扱わないことを示す。
- 触るとき: 結果メニューから新しいタブや新しいウィンドウで開く項目を出せるように実装したとき、この値を見直すとき。

## SmartbarInput.pickElement()
- 位置: L2436-2445
- 役割: ビューの要素から結果を取り出し、pickResult に渡す。結果が無ければ何もしない。
- 触るとき: 候補をクリックや Enter で選んだときに要素から結果への対応を追うとき。
- 呼び出し先: `logger()`, `logger().debug()`, `this.pickResult()`, `this.view.getResultFromElement()`
- 参照: `event?.type`

## SmartbarInput.pickResult()
- 位置: L2460-2906
- 役割: 選ばれた結果を、結果の種類ごとに開く。メニュー、コマンド、検索モード確定、ヒントの閉じ、URL 読み込み、タブ切り替え、検索、拡張のオムニボックス、動的結果などに振り分け、各々で engagement を記録する。URL は #loadURL で読み込み、スマートバーでは結果の種類に応じた動作を commit イベントに載せる。
- 触るとき: 候補の種類ごとの扱い(タブ切り替え、検索モードへの移行、ヒントの閉じ方、どの種類で何を読み込むか)を変えたり、特定の候補で開かれない不具合を追うとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.getLoadRequestFromResult()`, `UrlbarShared.looksLikeSingleWordHost()`, `element?.classList.contains()`, `lazy.ExtensionSearchHandler.handleInputEntered()`, `this.#loadURL()`, `this.#providesSearchMode()`, `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.controller.engineStore.getEngineByName()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.handleRevert()`, `this.hasAttribute()`, `this.maybeConfirmSearchModeFromResult()`, `this.parentController.switchToTab()`, `this.setValueFromResult()`, `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (element?.classList.contains("urlbarView-button-menu"))` → `this.view.openResultMenu()`
- 条件付き依存: `if (element?.dataset.command)` → `this.#pickMenuResult()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderGlobalActions" && this.#providesSearchMode(result) && !this.view.selectedElement?.dataset.immediateSearch )` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( (this.searchMode?.isPreview && result.providerName == "UrlbarProviderGlobalActions" && !this.view.selectedElement?.dataset.immediateSearch) || (result.heuri...)` → `this.confirmSearchMode()`
- 条件付き依存: `if ( (this.searchMode?.isPreview && result.providerName == "UrlbarProviderGlobalActions" && !this.view.selectedElement?.dataset.immediateSearch) || (result.heuri...)` → `this.search()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.getSearchSource()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.view.onQueryResultRemoved()`
- 条件付き依存: `if (!this.#providesSearchMode(result))` → `this.view.close()`
- 条件付き依存: `if (isCanonized)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (isCanonized)` → `this.getSearchSource()`
- 条件付き依存: `if (isCanonized)` → `this.#loadURL()`
- 条件付き依存: `if (result.heuristic)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (result.heuristic)` → `UrlbarShared.looksLikeSingleWordHost()`
- 条件付き依存: `if (result.heuristic)` → `this.#getSchemelessInput()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.getSearchSource()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( this.#isAddressbar && !this.searchMode && result.heuristic && // If we asked the DNS earlier, avoid the post-facto check. !UrlbarPrefs.get("browser.fixup.dn...)` → `this.parentController.checkKeywordURIFixup()`
- 条件付き依存: `if ( this.#isAddressbar && !this.searchMode && result.heuristic && // If we asked the DNS earlier, avoid the post-facto check. !UrlbarPrefs.get("browser.fixup.dn...)` → `originalUntrimmedValue.trim()`
- 条件付き依存: `if (!loadRequest)` → `this.handleRevert()`
- 条件付き依存: `if (!loadRequest)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (!loadRequest)` → `this.getSearchSource()`
- 条件付き依存: `if (!loadRequest)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (!loadRequest)` → `JSON.stringify()`
- 条件付き依存: `if (input !== undefined)` → `this.parentController.addToInputHistory()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.controller.engagementEvent .startTrackingBounceEvent()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.getSearchSource()`
- 条件付き依存: `if (this.window.gBrowser)` → `logger().error()`
- 条件付き依存: `if (this.window.gBrowser)` → `logger()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#dispatchSmartbarCommitEvent()`
- 参照: `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `element?.dataset.action`, `element?.dataset.command`, `element?.dataset.url`, `loadRequest.urlLoad`, `loadRequest.urlLoad.url`, `openParams.allowInheritPrincipal`, `openParams.private`, `openParams.schemelessInput`, `result.autofill.adaptiveHistoryInput`, `result.autofill?.type`, `result.heuristic`, `result.id`, `result.payload.content`, `result.payload.engine`, `result.payload.inPrivateWindow`, `result.payload.keyword`, `result.payload.providesSearchMode`, `result.payload.query`, `result.payload.suggestion`, `result.payload.tabGroup`, `result.payload.type`, `result.payload.url`, `result.payload.userContext?.id`, `result.payload?.engine`, `result.payload?.isSponsored`, `result.providerName`, `result.source`, `result.type`, `this.#isAddressbar`, `this.#isSmartbarMode`, `this.#sapName`, `this._lastSearchString`, `this._untrimmedValue`, `this.isPrivate`, `this.sapLocation`, `this.searchMode`, `this.searchMode?.isPreview`, `this.untrimmedValue`, `this.value`, `this.view.oneOffSearchButtons?.selectedButton`, `this.view.selectedElement?.dataset.immediateSearch`, `this.window.gBrowser`, `this.window.gBrowser.selectedBrowser.browserId`, `this.window.gBrowser.selectedTab.splitview`, `this.windowMode`

## SmartbarInput.clearSmartbarInput()
- 位置: L2908-2930
- 役割: スマートバーの値、入力の控え、検索文字列、結果、ロックされた動作と検索エンジン名を初期化し、既定の動作 chat に戻して意図の推定を再開させる。
- 触るとき: 送信後に入力欄を空にしたとき、前回のロック状態や推定が残らないようにするとき。
- 呼び出し先: `this.#updateContextChips()`, `this.#updateCtaSearchEngineInfo()`, `this.#updateGoGuardrail()`, `this.dispatchEvent()`, `this.setSelectionRange()`, `this.view.close()`
- 参照: `this.#contextWebsites`, `this.#detectedIntent`, `this.#smartbarActionLocked`, `this.#smartbarSearchEngineName`, `this._autofillPlaceholder`, `this._lastSearchString`, `this._resultForCurrentValue`, `this.smartbarAction`, `this.userTypedValue`, `this.value`

## SmartbarInput.setValueFromResult()
- 位置: L2955-3061
- 役割: 選択中の結果で入力欄の値を置き換え、ページプロキシ状態を無効にする。結果が無ければ直前の検索文字列に戻す。自動補完とプレビュー中の検索モードも結果に合わせて更新し、正規化された URL なら true を返す。
- 触るとき: 上下キーで候補を移動したときに入力欄の値が候補に追従しない、または検索モードのプレビューが残る不具合を調べるとき。
- 呼び出し先: `this.#providesSearchMode()`, `this._maybeCanonizeURL()`, `this.setPageProxyState()`, `this.setResultForCurrentValue()`
- 条件付き依存: `if (!result)` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (canonizedUrl)` → `this.setValue()`
- 条件付き依存: `if (canonizedUrl)` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (result.autofill)` → `this._autofillValue()`
- 条件付き依存: `if (this.#providesSearchMode(result))` → `this.view.resultIsSelected()`
- 条件付き依存: `if (this.view.resultIsSelected(result))` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if (this.view.resultIsSelected(result))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!enteredSearchMode)` → `this.setValue()`
- 条件付き依存: `if (!enteredSearchMode)` → `this.#getValueFromResult()`
- 条件付き依存: `if (!enteredSearchMode)` → `this.#getActionTypeFromResult()`
- 条件付き依存: `if (this.#providesSearchMode(result))` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (!result.autofill)` → `this.#getValueFromResult()`
- 条件付き依存: `if (!result.autofill)` → `this.setValue()`
- 条件付き依存: `if (!result.autofill)` → `this.#getActionTypeFromResult()`
- 参照: `result.autofill`, `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._autofillPlaceholder.value`, `this._lastSearchString`, `this._valueOnLastSearch`, `this.searchMode`, `this.searchMode?.isPreview`, `this.value`, `this.value.length`, `this.view.oneOffSearchButtons?.selectedButton`, `this.view.visibleResults.length`

## SmartbarInput.setResultForCurrentValue()
- 位置: L3074-3076
- 役割: 現在の入力値に対応する結果として _resultForCurrentValue を保存するだけで、入力値は変えない。
- 触るとき: 値を変えずに結果だけを紐づけたい経路(ヒューリスティック結果の保持など)を確かめるとき。
- 参照: `this._resultForCurrentValue`

## SmartbarInput._autofillFirstResult()
- 位置: L3086-3117
- 役割: 先頭結果が自動補完のとき、メンションパネルが開いていなければ、選択がなく入力末尾にいる場合に限り setValueFromResult で補完を適用する。
- 触るとき: 入力途中で自動補完が出る条件(カーソル位置や選択の有無)を変えるとき。
- 呼び出し先: `this._autofillPlaceholder.value .toLocaleLowerCase()`, `this._autofillPlaceholder.value .toLocaleLowerCase() .startsWith()`, `this._lastSearchString.toLocaleLowerCase()`, `this.setValueFromResult()`
- 参照: `result.autofill`, `this._autofillIgnoresSelection`, `this._autofillPlaceholder`, `this._autofillPlaceholder.value.length`, `this._lastSearchString.length`, `this.inputField.isHandlingMentions`, `this.selectionEnd`, `this.selectionStart`

## SmartbarInput.#clearAutofill()
- 位置: L3121-3135
- 役割: 自動補完の表示を消す。入力値を補完位置までに切り詰め、自動補完のプレースホルダーを外してから選択を元に戻す。
- 触るとき: 補完文字が残ったまま入力が確定してしまう不具合を調べるとき。
- 呼び出し先: `this.#setInputValue()`, `this.setSelectionRange()`, `this.value.substring()`
- 参照: `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionStart`, `this.selectionEnd`, `this.selectionStart`

## SmartbarInput.onFirstResult()
- 位置: L3143-3177
- 役割: 先頭結果の判定を受ける。キーワード付きのヒューリスティックなら検索モードに入り、そのクエリを捨てる。自動補完なら _autofillFirstResult を呼び、補完が外れたら入力値を元の文字列に戻す。
- 触るとき: 先頭候補による自動補完や検索モード移行のタイミングを追うとき。
- 呼び出し先: `this.#providesSearchMode()`, `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( firstResult.heuristic && firstResult.payload.keyword && !this.#providesSearchMode(firstResult) && this.maybeConfirmSearchModeFromResult({ result: firstResul...)` → `this.controller.discardResults()`
- 条件付き依存: `if (firstResult.autofill)` → `this._autofillFirstResult()`
- 条件付き依存: `if (!(firstResult.autofill))` → `this.value.endsWith()`
- 条件付き依存: `if ( this._autofillPlaceholder && // Avoid clobbering added spaces (for token aliases, for example). !this.value.endsWith(" ") )` → `this.setValue()`
- 参照: `firstResult.autofill`, `firstResult.heuristic`, `firstResult.payload.keyword`, `queryContext.results`, `this._autofillPlaceholder`, `this.userTypedValue`

## SmartbarInput.onQueryStarted()
- 位置: L3184-3186
- 役割: クエリ開始時に動作の推定を保留状態にする(smartbarActionPending を立てる)。
- 触るとき: スマートバーの CTA の動作推定がいつ更新されるかを追うとき。
- 参照: `this.#smartbarActionPending`

## SmartbarInput.onQueryResults()
- 位置: L3193-3203
- 役割: スマートバーで保留中の推定があり、ヒューリスティック提供元がすべて終わっていれば、先頭結果から CTA ボタンの状態を更新する。
- 触るとき: 結果到着後に CTA の表示(検索、移動、チャットなど)が切り替わるタイミングを変えるとき。
- 呼び出し先: `this.#updateSmartbarCTAButton()`
- 参照: `queryContext.pendingHeuristicProviders.size`, `queryContext.results`, `this.#isSmartbarMode`, `this.#smartbarActionPending`

## SmartbarInput.onQueryFinished()
- 位置: L3205-3208
- 役割: クエリ終了時に結果一覧のスクロールフェード表示(has-overflow)を更新する。
- 触るとき: 結果一覧の端の影が古いまま残る不具合を調べるとき。
- 呼び出し先: `this.#updatePanelScrollFade()`

## SmartbarInput.suppressStartQuery()
- 位置: L3216-3221
- 役割: 検索クエリの開始を抑止するフラグを立てる。permanent を指定すると、unsuppressStartQuery で解除するまで続く。
- 触るとき: チャット表示中など、入力で検索を走らせたくない場面の抑止条件を追うとき。
- 参照: `this._permanentlySuppressStartQuery`, `this._suppressStartQuery`

## SmartbarInput.unsuppressStartQuery()
- 位置: L3226-3229
- 役割: 通常の抑止と永続抑止の両方を解除する。
- 触るとき: 抑止を解いて検索を再開させる箇所が漏れていないかを確かめるとき。
- 参照: `this._permanentlySuppressStartQuery`, `this._suppressStartQuery`

## SmartbarInput.startQuery()
- 位置: L3255-3332
- 役割: 入力値から検索文脈を作って開始する。メンションやコマンドのパネル、エージェントコマンドが開いているときは検索せず CTA だけ更新する。抑止中は URL らしい入力を heuristic で拾い、それ以外は検索結果を取得する。
- 触るとき: 入力に応じて検索を走らせる条件や、抑止中に URL 候補を出す仕組みを変えるとき。
- 呼び出し先: `this.#makeQueryContext()`, `this.controller.startQuery()`
- 条件付き依存: `if ( (isHandlingMentions || isHandlingCommands || this.#isAgentCommand) && event )` → `this.view.close()`
- 条件付き依存: `if ( (isHandlingMentions || isHandlingCommands || this.#isAgentCommand) && event )` → `this.#updateSmartbarCTAButton()`
- 条件付き依存: `if (!searchString)` → `this.getAttribute()`
- 条件付き依存: `if (!(!searchString))` → `this.value.startsWith()`
- 条件付き依存: `if (event)` → `this.controller.engagementEvent.start()`
- 条件付き依存: `if (this._suppressStartQuery)` → `lazy.UrlbarProviderHeuristicFallback.matchUnknownUrl()`
- 条件付き依存: `if (this._suppressStartQuery)` → `this.setResultForCurrentValue()`
- 条件付き依存: `if (this._suppressStartQuery)` → `this.#updateSmartbarCTAButton()`
- 条件付き依存: `if (resetSearchState)` → `this._resetSearchState()`
- 条件付き依存: `if (this.searchMode)` → `this.confirmSearchMode()`
- 参照: `this.#isAgentCommand`, `this._autofillIgnoresSelection`, `this._lastSearchString`, `this._suppressStartQuery`, `this._valueOnLastSearch`, `this.inputField.isHandlingCommands`, `this.inputField.isHandlingMentions`, `this.lastQueryContextPromise`, `this.searchMode`, `this.value`

## SmartbarInput.search()
- 位置: L3355-3437
- 役割: 値の先頭トークンを見て検索モードに入れ、その語を値から取り除いてから入力欄に設定する。search 制限トークンでエンジンが未初期化なら初期化を待って再実行する。startQuery が真なら入力イベントを発火して検索を走らせる。
- 触るとき: @ などの制限トークンやエンジンのエイリアスで検索モードに入る流れを追うとき、または新タブからの受け渡しを変えるとき。
- 呼び出し先: `this.#setInputValue()`, `this.searchModeForToken()`, `trimmedValue.search()`, `trimmedValue.substring()`, `value.trim()`
- 条件付き依存: `if (options.focus ?? true)` → `this.focus()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.controller.engineStore .init() .catch(() => {}) .then()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.controller.engineStore .init() .catch()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.controller.engineStore .init()`
- 条件付き依存: `if ( firstToken == UrlbarShared.RESTRICT_TOKENS.SEARCH && !this.controller.engineStore.initialized && !this.controller.engineStore.failed )` → `this.search()`
- 条件付き依存: `if (!searchMode && searchEngine)` → `searchEngine.aliases.includes()`
- 条件付き依存: `if (firstTokenIsRestriction)` → `value.replace()`
- 条件付き依存: `if (searchMode)` → `UrlbarShared.REGEXP_SPACES.test()`
- 条件付き依存: `if (UrlbarShared.REGEXP_SPACES.test(value[0]))` → `value.slice()`
- 条件付き依存: `if (!(searchMode))` → `( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes()`
- 条件付き依存: `if (!(searchMode))` → `Object.values()`
- 条件付き依存: `if ( /** @type {string[]} */ ( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes(firstToken) )` → `( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes()`
- 条件付き依存: `if ( /** @type {string[]} */ ( Object.values(UrlbarShared.RESTRICT_TOKENS) ).includes(firstToken) )` → `Object.values()`
- 条件付き依存: `if (startQuery)` → `this.inputField.dispatchEvent()`
- 参照: `UrlbarShared.REGEXP_SPACES`, `UrlbarShared.RESTRICT_TOKENS`, `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `options.focus`, `searchEngine.name`, `searchMode.entry`, `this._lastSearchString`, `this.controller.engineStore.failed`, `this.controller.engineStore.initialized`, `this.searchMode`, `this.selectionStart`, `this.window`

## SmartbarInput.searchModeForToken()
- 位置: L3448-3464
- 役割: 先頭トークンが search 制限ならその既定エンジンの検索モードを、アドレスバーならローカル検索モードの一覧から該当するものを返す。それ以外は null。
- 触るとき: どの制限トークンで検索モードに入るかを増やしたり、アドレスバーとスマートバーで差を付けたりするとき。
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `m.restrict`, `this.#isAddressbar`, `this.controller.engineStore.default?.name`

## SmartbarInput.openSearchEnginePage()
- 位置: L3477-3530
- 役割: 検索ボタン経由で、空白を除いた文字列を検索結果として開く。検索を記録し、現在のタブで開く場合は検索モードに入れてから SERP を開く。空の場合はエンジンのホームページ(searchform)を開く。
- 触るとき: 検索ボタンから検索結果を開く経路や、どのタブで開くかの判断を変えるとき。
- 呼び出し先: `value.trim()`
- 条件付き依存: `if (!searchEngine || !event || !where)` → `console.warn()`
- 条件付き依存: `if (trimmedValue)` → `this._recordSearch()`
- 条件付き依存: `if (where == "current")` → `this.setSearchMode()`
- 条件付き依存: `if (trimmedValue)` → `this.parentController.openSERP()`
- 条件付き依存: `if (!(trimmedValue))` → `this.parentController.openSearchForm()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `searchEngine.id`, `searchEngine.name`, `this.#selectedBrowserId`, `this._lastSearchString`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.setHiddenFocus()
- 位置: L3536-3543
- 役割: フォーカス枠を見せずに入力欄へフォーカスを置く。フォーカス中ならフォーカス属性だけ外す。
- 触るとき: 新しいタブページなど、検索の受け渡し元で入力欄の枠を出したくない場面を確かめるとき。
- 条件付き依存: `if (this.focused)` → `this.removeAttribute()`
- 条件付き依存: `if (!(this.focused))` → `this.focus()`
- 参照: `this._hideFocus`, `this.focused`

## SmartbarInput.removeHiddenFocus()
- 位置: L3552-3561
- 役割: 隠していたフォーカス枠を戻す。フォーカス中なら focused 属性を付け、指定があれば suppress-focus-border も付ける。
- 触るとき: 受け渡し後にフォーカス枠が正しく戻るかを確かめるとき。
- 条件付き依存: `if (this.focused)` → `this.toggleAttribute()`
- 条件付き依存: `if (forceSuppressFocusBorder)` → `this.toggleAttribute()`
- 参照: `this._hideFocus`, `this.focused`

## SmartbarInput.getSearchMode()
- 位置: L3577-3588
- 役割: ブラウザの検索モードを返す。確定のみ指定がなければプレビューを優先し、無ければ確定したものを、どちらも無ければ null を返す。どちらも複製して返す。
- 触るとき: 検索モードの状態を読む側が、プレビューと確定のどちらを見ているかを確かめるとき。
- 呼び出し先: `this.#getSearchModesObject()`
- 参照: `modes.confirmed`, `modes.preview`

## SmartbarInput.setSearchMode()
- 位置: async L3601-3697
- 役割: スマートバーでは何もしない。アドレスバーでは、指定のエンジンを検索して無効なら検索モードを外し、確定かプレビューかに応じて保存する。選択中のブラウザなら UI を更新し、確定時は検索モードの記録を送る。
- 触るとき: 検索モードの保存や UI 更新の流れ、確定と仮の区別を変えるとき。
- 呼び出し先: `UrlbarShared.SEARCH_MODE_ENTRY.has()`, `UrlbarShared.deepEqual()`, `lazy.UrlbarSearchTermsPersistence.onSearchModeChanged()`, `this.#getSearchModesObject()`, `this.dispatchEvent()`, `this.getSearchMode()`
- 条件付き依存: `if (!this.controller.engineStore.initialized)` → `this.controller.engineStore.init()`
- 条件付き依存: `if (searchMode?.engineName)` → `this.controller.engineStore.getEngineByName()`
- 条件付き依存: `if (source)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (!(sourceName))` → `console.error()`
- 条件付き依存: `if (browser == this.window.gBrowser.selectedBrowser)` → `this._updateSearchModeUI()`
- 条件付き依存: `if (!newSearchMode.isPreview && !areSearchModesSame)` → `this.parentController.recordSearchMode()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `engine.isGeneralPurposeEngine`, `modes.confirmed`, `modes.preview`, `newSearchMode.isGeneralPurposeEngine`, `newSearchMode.isPreview`, `newSearchMode.restrictType`, `newSearchMode.source`, `searchMode.engineName`, `searchMode?.engineName`, `this.#isSmartbarMode`, `this.controller.engineStore.initialized`, `this.untrimmedValue`, `this.userTypedValue`, `this.valueIsTyped`, `this.window`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.#getSearchModesObject()
- 位置: L3725-3735
- 役割: アドレスバーではブラウザごとの状態、検索バーではウィンドウ全体の検索モード格納先を返す。無ければ作る。
- 触るとき: 検索モードをタブごとに持つか、ウィンドウで共有するかの扱いを変えるとき。
- 呼び出し先: `this.getBrowserState()`
- 参照: `state.searchModes`, `this.#isAddressbar`, `this.#searchbarSearchModes`

## SmartbarInput.restoreSearchModeState()
- 位置: L3740-3746
- 役割: スマートバーでは何もしない。それ以外は選択中ブラウザに保存された確定の検索モードを復元する。
- 触るとき: タブを切り替えたあとに検索モードが戻らない不具合を調べるとき。
- 呼び出し先: `this.getBrowserState()`
- 参照: `state.searchModes?.confirmed`, `this.#isSmartbarMode`, `this.searchMode`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.searchModeShortcut()
- 位置: async L3751-3773
- 役割: 必要ならエンジンを初期化し、既定のエンジンで検索結果限定の検索モードに入る。入力値を検索し、入力欄を全選択する。初期化に失敗したら何もしない。
- 触るとき: 検索モードへの入り方のショートカットで、結果の種類を検索に絞る既存の挙動を守るとき。
- 呼び出し先: `this.search()`, `this.select()`
- 条件付き依存: `if (!this.controller.engineStore.initialized)` → `this.controller.engineStore.init()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `this.controller.engineStore.default.name`, `this.controller.engineStore.initialized`, `this.searchMode`, `this.value`

## SmartbarInput.confirmSearchMode()
- 位置: L3778-3789
- 役割: プレビュー中の検索モードを確定に切り替え、一つ選ばれていたワンオフ検索ボタンの選択を外す。
- 触るとき: 候補のプレビューを確定させて検索モードを残す場面の挙動を確かめるとき。
- 参照: `searchMode.isPreview`, `searchMode?.isPreview`, `this.searchMode`, `this.view.oneOffSearchButtons`, `this.view.oneOffSearchButtons.selectedButton`

## SmartbarInput.editor()
- 位置: L3793-3798
- 役割: スマートバーでは編集部を初期化して返し、それ以外は inputField の editor を返す。
- 触るとき: 入力欄の編集部を参照する箇所で、スマートバーとアドレスバーのどちらの editor を使うかを確かめるとき。
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.#ensureSmartbarEditor()`
- 参照: `this.#isSmartbarMode`, `this.inputField.editor`

## SmartbarInput.focused()
- 位置: L3800-3803
- 役割: 入力欄(controller 経由があればそちら)が、ルートノードのアクティブ要素かを返す。
- 触るとき: フォーカス判定が shadow DOM の中で正しく働くかを確かめるとき。
- 呼び出し先: `input.getRootNode()`
- 参照: `input.getRootNode().activeElement`, `this.#smartbarInputController?.input`, `this.inputField`

## SmartbarInput.goButton()
- 位置: L3805-3807
- 役割: 内部の Go ボタン要素を返す。
- 触るとき: Go ボタンの表示や状態を外から操作する箇所を追うとき。
- 呼び出し先: `this.querySelector()`

## SmartbarInput.smartbarButtonContainer()
- 位置: L3809-3811
- 役割: スマートバーのボタン列の要素を返す。
- 触るとき: ボタン列にフォーカスを移す処理や Tab の循環を変えるとき。
- 呼び出し先: `this.querySelector()`

## SmartbarInput.focusFirstActionButton()
- 位置: L3819-3825
- 役割: ボタン列の中で、隠れておらず無効でもない最初の要素にフォーカスを移す。
- 触るとき: 入力欄から Tab でボタン列に入るときの移動先を変えるとき。
- 呼び出し先: `( this.smartbarButtonContainer.querySelector( ":scope > :not([hidden]):not([disabled])" ) ).focus()`, `this.smartbarButtonContainer.querySelector()`

## SmartbarInput.focusLastActionButton()
- 位置: L3835-3859
- 役割: ボタン列の最後の要素を起点に、可視な shadow DOM まで辿って最後に Tab できる要素を探し、そこにフォーカスを移す。逆方向の Tab 循環を対称にする。
- 触るとき: 分割ボタン(input-cta の chevron など)を含むボタン列で、Shift+Tab の移動先がずれる不具合を調べるとき。
- 呼び出し先: `(last).focus()`, `this.smartbarButtonContainer.querySelectorAll()`, `walk()`
- 参照: `buttons.length`

## walk()
- 位置: L3841-3856
- 役割: 表示されている要素を深さ優先で辿り、Tab 可能なものを最後の候補として記録する。shadow root の子も辿る。
- 触るとき: ボタン列の中で最後に Tab できる要素の判定条件を変えるとき。
- 呼び出し先: `node.checkVisibility()`, `this.#isTabbable()`, `walk()`
- 条件付き依存: `if (node.shadowRoot)` → `walk()`
- 参照: `node.checkVisibility`, `node.children`, `node.shadowRoot`, `node.shadowRoot.children`

## SmartbarInput.#isTabbable()
- 位置: L3869-3871
- 役割: 要素が無効でなく、tabIndex が 0 以上で、link ではないなら Tab 移動の対象とみなす。
- 触るとき: Tab 循環の対象判定を調整するとき。
- 参照: `el.disabled`, `el.localName`, `el.tabIndex`

## SmartbarInput.#isInsideContainer()
- 位置: L3882-3887
- 役割: target から親や shadow host をたどり、container の子孫かどうかを返す。
- 触るとき: closed の shadow root の内側にあるイベント元がボタン列の中かを判定するとき。
- 参照: `target.host`, `target.parentNode`

## SmartbarInput.#onActionButtonsKeyDown()
- 位置: L3897-3948
- 役割: ボタン列上の keydown を処理する。Escape で候補を閉じて入力欄に戻り、ビューが開いている Tab では分割ボタンの隣の要素へ進めてから、最後または最初のボタンで候補側へ循環させる。
- 触るとき: ボタン列からキーボードで候補一覧へ抜ける、または戻る操作の挙動を直すとき。
- 呼び出し先: `buttons.includes()`, `container.querySelectorAll()`, `this.#isTabbable()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE && this.view.isOpen)` → `this.view.close()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE && this.view.isOpen)` → `this.focus()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_ESCAPE && this.view.isOpen)` → `event.preventDefault()`
- 条件付き依存: `if (event.shiftKey && focused == buttons[0])` → `this.focus()`
- 条件付き依存: `if (event.shiftKey && focused == buttons[0])` → `this.view.selectBy()`
- 条件付き依存: `if (event.shiftKey && focused == buttons[0])` → `event.preventDefault()`
- 条件付き依存: `if (!event.shiftKey && focused == buttons[buttons.length - 1])` → `this.focus()`
- 条件付き依存: `if (!event.shiftKey && focused == buttons[buttons.length - 1])` → `this.view.selectBy()`
- 条件付き依存: `if (!event.shiftKey && focused == buttons[buttons.length - 1])` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_TAB`, `buttons.length`, `event.composedTarget`, `event.keyCode`, `event.shiftKey`, `focused.host`, `focused.parentNode`, `innerTarget?.nextElementSibling`, `innerTarget?.previousElementSibling`, `this.smartbarButtonContainer`, `this.view.isOpen`

## SmartbarInput.value()
- 位置: L3950-3952
- 役割: controller の value があればそれを、無ければ inputField の値を返す。
- 触るとき: 入力欄の現在の文字列を読む箇所で、スマートバーと URL バーのどちらの値を見ているかを確かめるとき。
- 参照: `this.#smartbarInputController?.value`, `this.inputField.value`

## SmartbarInput.value()
- 位置: L3954-3956
- 役割: 値を trim を許して setValue に渡す。
- 触るとき: 外部から入力欄の値を書き換えたときの trim の扱いを確かめるとき。
- 呼び出し先: `this.setValue()`

## SmartbarInput.untrimmedValue()
- 位置: L3958-3960
- 役割: トリムされていない入力値(_untrimmedValue)を返す。
- 触るとき: プロトコルや www を外した表示と、実際に送る文字列を区別する箇所を追うとき。
- 参照: `this._untrimmedValue`

## SmartbarInput.userTypedValue()
- 位置: L3962-3966
- 役割: アドレスバーではタブごとの入力値を、検索バーなどでは内部の値を返す。
- 触るとき: タブを切り替えたときに、ユーザーが入力していた文字列が戻るかを確かめるとき。
- 参照: `this.#isAddressbar`, `this._userTypedValue`, `this.window.gBrowser.userTypedValue`

## SmartbarInput.userTypedValue()
- 位置: L3968-3974
- 役割: アドレスバーではタブ側に、それ以外では内部に入力値を保存する。
- 触るとき: 入力値の保存先(タブごとか全体か)を変えるとき。
- 参照: `this.#isAddressbar`, `this._userTypedValue`, `this.window.gBrowser.userTypedValue`

## SmartbarInput.lastSearchString()
- 位置: L3976-3978
- 役割: 直近に検索した文字列(_lastSearchString)を返す。
- 触るとき: エンジン検索や engagement の記録に使われる検索文字列を追うとき。
- 参照: `this._lastSearchString`

## SmartbarInput.searchMode()
- 位置: L3990-3999
- 役割: スマートバーでは null、ウィンドウ未初期化時も null を返し、それ以外は選択中ブラウザの検索モードを返す。
- 触るとき: 検索モードの判定が現在のタブに対して正しいかを確かめるとき。
- 呼び出し先: `this.getSearchMode()`
- 参照: `this.#isSmartbarMode`, `this.window.gBrowser`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.searchMode()
- 位置: L4001-4014
- 役割: スマートバーでは何もしない。それ以外は選択中ブラウザへ検索モードを設定し、対象エンジンを使用済みとして記録する。
- 触るとき: 検索モードの設定が非同期に終わるまでの待ち合わせ(searchModeApplied)を追うとき。
- 呼び出し先: `this.controller.engineStore .getEngineByName()`, `this.controller.engineStore .getEngineByName(this.searchMode?.engineName) ?.markAsUsed()`, `this.setSearchMode()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `Promise.resolve()`
- 参照: `this.#isSmartbarMode`, `this.#searchModeApplied`, `this.searchMode?.engineName`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.getBrowserState()
- 位置: L4016-4023
- 役割: ブラウザごとの状態オブジェクトを返す。無ければ作って登録する。
- 触るとき: タブごとに保存する情報(選択範囲、検索モード、永続化された検索語)を追加するとき。
- 呼び出し先: `this.#browserStates.get()`
- 条件付き依存: `if (!state)` → `this.#browserStates.set()`

## SmartbarInput.#updatePopoverAnchor()
- 位置: async L4025-4042
- 役割: ポップオーバーを使えるツールバーにあるときだけ、アンカーの高さを測り直す。全画面中は fullscreen イベントを待ってから測る。
- 触るとき: 全画面からの復帰後やツールバーの表示変化でアンカーの高さが合わない不具合を調べるとき。
- 呼び出し先: `this.#measurePopoverAnchor()`
- 条件付き依存: `if (this.document.fullscreenElement)` → `this.window.addEventListener()`
- 条件付き依存: `if (this.document.fullscreenElement)` → `this.#updatePopoverAnchor()`
- 参照: `this.#canOpenPopover`, `this.document.fullscreenElement`

## SmartbarInput.#openPopover()
- 位置: L4044-4065
- 役割: 展開できる状態で、ビューが開いていて未展開なら expanded を付け、初回だけ次フレームで popover-animate を付けてアニメーションを有効にする。
- 触るとき: 入力欄を展開するアニメーションの開始条件を変えるとき。
- 呼び出し先: `this.hasAttribute()`, `this.setAttribute()`
- 条件付き依存: `if (!this.hasAttribute("popover-animate"))` → `this.window.promiseDocumentFlushed()`
- 条件付き依存: `if (!this.hasAttribute("popover-animate"))` → `this.window.requestAnimationFrame()`
- 条件付き依存: `if (!this.hasAttribute("popover-animate"))` → `this.setAttribute()`
- 参照: `this.#canOpenPopover`, `this.view.isOpen`

## SmartbarInput.#closePopover()
- 位置: L4067-4076
- 役割: 展開中でビューが閉じていれば expanded を外す。
- 触るとき: 候補一覧を閉じたあとに入力欄が縮まらない不具合を調べるとき。
- 呼び出し先: `this.hasAttribute()`, `this.removeAttribute()`
- 参照: `this.view.isOpen`

## SmartbarInput.updatePopover()
- 位置: L4078-4084
- 役割: ビューが開いていれば展開し、閉じていれば縮める。
- 触るとき: 候補一覧の開閉に入力欄の展開状態を追従させる箇所を変えるとき。
- 条件付き依存: `if (this.view.isOpen)` → `this.#openPopover()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.#closePopover()`
- 参照: `this.view.isOpen`

## SmartbarInput.setPageProxyState()
- 位置: L4106-4134
- 役割: アドレスバーでのみ、pageproxystate を入力欄、入力コンテナ、identity box に設定し、統合検索ボタンの可否を更新する。valid なら表示中 URL を保存し、必要なら通知の表示を更新する。
- 触るとき: ページの URL と入力欄の表示が一致しているかどうかの状態が正しく伝わるかを確かめるとき。
- 呼び出し先: `this._identityBox?.setAttribute()`, `this._inputContainer.setAttribute()`, `this.getAttribute()`, `this.setAttribute()`, `this.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if ( updatePopupNotifications && prevState != state && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 参照: `this.#isAddressbar`, `this._lastValidURLStr`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`

## SmartbarInput.afterTabSwitchFocusChange()
- 位置: L4141-4144
- 役割: フォーカス変更が済んだことを記録し、タブ切替後の処理を呼ぶ。
- 触るとき: タブ切替とフォーカス変更の順序が入れ替わったときに結果一覧が点滅する問題を追うとき。
- 呼び出し先: `this._afterTabSelectAndFocusChange()`
- 参照: `this._gotFocusChange`

## SmartbarInput.maybeConfirmSearchModeFromResult()
- 位置: L4165-4207
- 役割: 結果がキーワードに一致すれば(checkValue が真なら入力値も一致が必要)、その結果の検索モードを確定して入力値を結果の query に置き換える。startQuery なら確定後に検索を走らせる。入れたら true を返す。
- 触るとき: キーワード入力や候補の選択で検索モードに入る条件、またはクエリを再実行するタイミングを変えるとき。
- 呼び出し先: `result.payload.autofillKeyword?.trim()`, `result.payload.keyword?.trim()`, `result.payload.query?.trimStart()`, `this._searchModeForResult()`, `this.setValue()`, `this.value.trim()`
- 条件付き依存: `if (startQuery)` → `this.#searchModeApplied.then()`
- 条件付き依存: `if (startQuery)` → `this.startQuery()`
- 参照: `searchMode.isPreview`, `this._resultForCurrentValue`, `this.searchMode`, `this.untrimmedValue`, `this.userTypedValue`

## SmartbarInput.onSearchEngineUpdate()
- 位置: L4213-4229
- 役割: エンジンの更新で CTA の情報を更新する。削除または変更されたエンジンが検索モードに使われていれば検索モードを設定し直し、既定のエンジンが変わったら placeholder を更新する。
- 触るとき: 検索エンジンの削除や既定の変更が入力欄の表示に反映されない不具合を調べるとき。
- 呼び出し先: `this.#updateCtaSearchEngineInfo()`, `this.updatePlaceholder()`
- 参照: `engine.name`, `searchMode?.engineName`, `this.searchMode`

## SmartbarInput.getSearchSource()
- 位置: L4239-4271
- 役割: アドレスバーでは、引き継ぎセッション、検索モード切替、検索モード中、永続化された検索語の順に検索元の名前を決める。それ以外は sap-name を返す。
- 触るとき: テレメトリに記録される検索元の分類を追加・変更するとき。
- 条件付き依存: `if (this.#isAddressbar)` → `this.searchModeSwitcher?.eventTargetIsPanelItem()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.view.oneOffSearchButtons?.eventTargetIsAOneOff()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 参照: `state.persist?.searchTerms`, `this.#isAddressbar`, `this.#sapName`, `this._isHandoffSession`, `this.searchMode`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.#providesSearchMode()
- 位置: L4280-4291
- 役割: 結果が検索モードを提供するかを返す。グローバルアクションでは選択中の要素の属性を見る。
- 触るとき: ボタン単位で検索モードの提供有無が変わる結果の判定を追うとき。
- 参照: `result.payload.providesSearchMode`, `result.providerName`, `this.view.selectedElement`, `this.view.selectedElement.dataset.providesSearchmode`

## SmartbarInput._addObservers()
- 位置: L4293-4298
- 役割: まだ登録していなければ、エンジンストアに検索エンジン更新の監視を登録する。
- 触るとき: 検索エンジンの変化を入力欄が受け取る経路を確かめるとき。
- 条件付き依存: `if (!this._observersAdded)` → `this.controller.engineStore.addObserver()`
- 参照: `this._observersAdded`, `this.onSearchEngineUpdate`

## SmartbarInput._removeObservers()
- 位置: L4300-4305
- 役割: 登録済みなら、エンジンストアから検索エンジン更新の監視を外す。
- 触るとき: 切断時に監視が残らないかを確かめるとき。
- 条件付き依存: `if (this._observersAdded)` → `this.controller.engineStore.removeObserver()`
- 参照: `this._observersAdded`, `this.onSearchEngineUpdate`

## SmartbarInput._afterTabSelectAndFocusChange()
- 位置: L4307-4343
- 役割: タブ選択とフォーカス変更の両方を受けてから、値の装飾を更新し、検索状態を初期化する。フォーカス中なら engagement を記録し、候補を自動で開けなければ検索モードの切替パネルと候補を閉じる。
- 触るとき: タブを切り替えたときに候補一覧が開いたまま残る、または意図せず開く不具合を調べるとき。
- 呼び出し先: `this._resetSearchState()`, `this.formatValue()`, `this.searchModeSwitcher.closePanel()`, `this.view.autoOpen()`, `this.view.close()`
- 条件付き依存: `if (this.focused)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (this.focused)` → `this.getSearchSource()`
- 参照: `this._gotFocusChange`, `this._gotTabSelect`, `this._lastSearchString`, `this.focused`, `this.sapLocation`, `this.windowMode`

## SmartbarInput.#releasePopoverAnchor()
- 位置: L4345-4352
- 役割: ポップオーバーを隠し、アンカーの更新キーを作り直して、進行中の測定を無効にする。
- 触るとき: ポップオーバーのアンカーが古い測定で表示される問題を追うとき。
- 呼び出し先: `this.hidePopover()`
- 参照: `this.#popoverAnchorUpdateKey`

## SmartbarInput.incrementPopoverBlockerCount()
- 位置: L4354-4359
- 役割: ポップオーバーの表示を止める数を 1 増やし、初めて 1 になったらアンカーを解放する。
- 触るとき: 別のポップアップ表示中に入力欄のポップオーバーを出さないようにする箇所を追うとき。
- 条件付き依存: `if (this.#popoverBlockerCount == 1)` → `this.#releasePopoverAnchor()`
- 参照: `this.#popoverBlockerCount`

## SmartbarInput.decrementPopoverBlockerCount()
- 位置: L4361-4368
- 役割: 止めている数を 1 減らし、0 になったらアンカーの測定を行い直す。
- 触るとき: ブロッカーの数がずれて入力欄のポップオーバーが出なくなる不具合を調べるとき。
- 条件付き依存: `if (this.#popoverBlockerCount === 0)` → `this.#updatePopoverAnchor()`
- 参照: `this.#popoverBlockerCount`

## SmartbarInput.#measurePopoverAnchor()
- 位置: async L4370-4398
- 役割: アンカーを解放してから、描画を待って高さを測り --urlbar-container-height に設定する。ブロッカーがなければポップオーバーを表示する。新しい測定が来た場合は古い測定を捨てる。
- 触るとき: 入力欄の展開時の高さがずれる、または表示が出ない不具合を調べるとき。
- 呼び出し先: `getBoundsWithoutFlushing()`, `px()`, `resolve()`, `this.#popoverAnchor.style.setProperty()`, `this.#releasePopoverAnchor()`, `this.showPopover()`, `this.window.promiseDocumentFlushed()`, `this.window.requestAnimationFrame()`
- 参照: `getBoundsWithoutFlushing(this.#popoverAnchor).height`, `this.#popoverAnchor`, `this.#popoverAnchorUpdateKey`, `this.#popoverBlockerCount`, `this.isConnected`

## SmartbarInput.setValue()
- 位置: L4412-4462
- 役割: 入力欄の値を設定する。about:reader は元 URL に戻し、allowTrim なら http(s) や www. を外して表示用の値にし、外した接頭辞を記録する。actiontype 属性を設定して ValueChange を発火する。
- 触るとき: URL の表示でプロトコルや www. が出たり消えたりする、または貼り付けや復元で値が変わる不具合を調べるとき。
- 呼び出し先: `event.initEvent()`, `lazy.ReaderMode.getOriginalUrlObjectForDisplay()`, `this.#setInputValue()`, `this.document.createEvent()`, `this.formatValue()`, `this.inputField.dispatchEvent()`
- 条件付き依存: `if (allowTrim)` → `this._trimValue()`
- 条件付き依存: `if (allowTrim)` → `lazy.BrowserUIUtils.getTrimmedURLPrefix()`
- 条件付き依存: `if (allowTrim)` → `val.startsWith()`
- 条件付き依存: `if (trimmedPrefix && !val.startsWith(trimmedPrefix))` → `trimmedPrefix.startsWith()`
- 条件付き依存: `if (trimmedPrefix && !val.startsWith(trimmedPrefix))` → `trimmedPrefix.endsWith()`
- 条件付き依存: `if (actionType !== undefined)` → `this.setAttribute()`
- 条件付き依存: `if (!(actionType !== undefined))` → `this.removeAttribute()`
- 参照: `lazy.BrowserUIUtils.trimURLProtocol`, `originalUrl.displaySpec`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.valueIsTyped`

## SmartbarInput.#getValueFromResult()
- 位置: L4490-4567
- 役割: 結果の種類ごとに入力欄へ入れる文字列を決める(キーワード、検索はキーワード付きの候補文、オムニボックスは content、動的結果は data 属性、制限は接頭語とスペース、ヒントは URL など)。URL 結果では、ユーザーがスキームを入れていなければ http:// を外すが、外すと検索に変わる場合は元の URL を残す。
- 触るとき: 候補を選んだときに入力欄へ入る文字列の形式を変えたり、http の表示が意図せず消える不具合を調べるとき。
- 呼び出し先: `URL.parse()`, `UrlbarContentUtils.getFixupPrimitives()`, `UrlbarShared.stripPrefixAndTrim()`, `losslessDecodeURI()`, `result.payload.url.startsWith()`, `this.#getSchemelessInput()`
- 条件付き依存: `if (urlOverride !== null)` → `URL.parse()`
- 条件付き依存: `if (urlOverride !== null)` → `losslessDecodeURI()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeSchemeless`, `UrlbarContentUtils.getFixupPrimitives( trimmedUrl, this.isPrivate )?.keywordAsSent`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TIP`, `element?.dataset.input`, `element?.dataset.query`, `element?.dataset.url`, `parsedUrl.URI`, `result.heuristic`, `result.payload.autofillKeyword`, `result.payload.content`, `result.payload.input`, `result.payload.keyword`, `result.payload.query`, `result.payload.suggestion`, `result.payload.url`, `result.type`, `this.isPrivate`, `this.userTypedValue`, `url.URI`
- XPCOM: [`nsILoadInfo`](../../../../dom/base/nsIContentPolicy.idl.md)

## SmartbarInput.#getActionTypeFromResult()
- 位置: L4576-4585
- 役割: タブ切り替えなら switchtab、オムニボックスなら extension を返し、それ以外は undefined を返す。
- 触るとき: 入力欄の actiontype 属性で見た目(タブ切替やオムニボックス用)を切り替える条件を変えるとき。
- 参照: `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.type`

## SmartbarInput._resetSearchState()
- 位置: L4591-4594
- 役割: 直近の検索文字列を現在の入力値にし、自動補完の placeholder を消す。
- 触るとき: 新しい操作で前回の検索状態が残って補完が誤って出る不具合を調べるとき。
- 参照: `this._autofillPlaceholder`, `this._lastSearchString`, `this.value`

## SmartbarInput._maybeAutofillPlaceholder()
- 位置: L4606-4674
- 役割: カーソルが末尾で、ローカル検索モードや mentions 表示中でなければ補完を許可する。補完 placeholder が新しい入力に一致すれば、残りを補完して選択を末尾に置く。一致しなければ placeholder を消す。
- 触るとき: 入力途中の即時補完(先頭結果が届く前のちらつき防止)の条件を変えるとき。
- 条件付き依存: `if (!allowAutofill)` → `this.#clearAutofill()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `this._autofillPlaceholder.value .toLocaleLowerCase() .startsWith()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `this._autofillPlaceholder.value .toLocaleLowerCase()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `value.toLocaleLowerCase()`
- 条件付き依存: `if (!( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" ))` → `UrlbarShared.canAutofillURL()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.selectionEnd == this.value.length && this._enableAutofillPlaceholder )` → `this._autofillPlaceholder.value.substring()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.selectionEnd == this.value.length && this._enableAutofillPlaceholder )` → `this._autofillValue()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `autofillValue.length`, `this._autofillPlaceholder`, `this._autofillPlaceholder.adaptiveHistoryInput`, `this._autofillPlaceholder.adaptiveHistoryInput.length`, `this._autofillPlaceholder.type`, `this._autofillPlaceholder.untrimmedValue`, `this._autofillPlaceholder.value`, `this._enableAutofillPlaceholder`, `this.inputField.isHandlingMentions`, `this.searchMode?.engineName`, `this.searchMode?.source`, `this.selectionEnd`, `this.selectionStart`, `this.value`, `this.value.length`, `value.length`

## SmartbarInput.updateTextOverflow()
- 位置: L4681-4725
- 役割: 入力欄がはみ出していれば、スクロール位置から textoverflow 属性(left、right、both)を決める。フレーム確定後に再確認してから反映する。
- 触るとき: 長い URL の左右のフェード表示が逆になる、または残る不具合を調べるとき。
- 呼び出し先: `UrlbarContentUtils.isTextDirectionRTL()`, `this.getAttribute()`, `this.window.promiseDocumentFlushed()`
- 条件付き依存: `if (!this._overflowing)` → `this.removeAttribute()`
- 条件付き依存: `if (input && this._overflowing)` → `this.window.requestAnimationFrame()`
- 条件付き依存: `if (this._overflowing)` → `this.setAttribute()`
- 参照: `input.scrollLeft`, `input.scrollLeftMax`, `input.scrollLeftMin`, `this._overflowing`, `this.inputField`, `this.value`

## SmartbarInput._updateUrlTooltip()
- 位置: L4727-4733
- 役割: フォーカス中でなく、はみ出していれば、入力欄の title に untrimmedValue を設定する。それ以外は title を外す。
- 触るとき: はみ出した URL をホバーで全文確認できる挙動を変えるとき。
- 条件付き依存: `if (this.focused || !this._overflowing)` → `this.inputField.removeAttribute()`
- 条件付き依存: `if (!(this.focused || !this._overflowing))` → `this.inputField.setAttribute()`
- 参照: `this._overflowing`, `this.focused`, `this.untrimmedValue`

## SmartbarInput._getSelectedValueForClipboard()
- 位置: L4735-4834
- 役割: 選択範囲が URL の全体または先頭から始まり、ドメインを含んでいれば、コピーする文字列を実際の URL(表示用に整形し、必要なら encodeURI で符号化)に置き換える。それ以外は選択された文字をそのまま返す。
- 触るとき: URL の一部だけを選んでコピーしたときの結果(デコード設定の影響を含む)を調べるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `lazy.BrowserUIUtils.getTrimmedURLPrefix()`, `selectedVal.includes()`, `selectedVal.startsWith()`, `this.getAttribute()`, `this.makeURIReadable()`, `uri.schemeIs()`
- 条件付き依存: `if (!selectedVal.includes("/"))` → `this.value.replace()`
- 条件付き依存: `if (!(this.getAttribute("pageproxystate") == "valid"))` → `URL.parse()`
- 条件付き依存: `if (!UrlbarPrefs.get("decodeURLsOnCopy") && !uri.schemeIs("data"))` → `URL.canParse()`
- 条件付き依存: `if (URL.canParse(selectedVal))` → `encodeURI()`
- 参照: `URL.parse(this._untrimmedValue)?.URI`, `result.payload.url`, `result?.autofill?.value`, `this.#isOpenedPageInBlankTargetLoading`, `this.#selectedText`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.editor.selection.rangeCount`, `this.selectionStart`, `this.value`, `this.valueIsTyped`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser.browsingContext .nonWebControlledLoadingURI`, `uri.displaySpec`

## SmartbarInput._toggleActionOverride()
- 位置: L4836-4856
- 役割: Shift、Alt、Mac では Cmd、それ以外では Ctrl の押下数を数え、押している間は action-override 属性を入力欄と結果パネルに付け、全部離すと外す。
- 触るとき: 修飾キーを押したときに Enter の動作(タブで開く等)が変わる仕組みを調べるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 条件付き依存: `if (event.type == "keydown")` → `this.toggleAttribute()`
- 条件付き依存: `if (event.type == "keydown")` → `this.view.panel.toggleAttribute()`
- 条件付き依存: `if ( this._actionOverrideKeyCount && --this._actionOverrideKeyCount == 0 )` → `this._clearActionOverride()`
- 参照: `KeyEvent.DOM_VK_ALT`, `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_META`, `KeyEvent.DOM_VK_SHIFT`, `event.keyCode`, `event.type`, `this._actionOverrideKeyCount`

## SmartbarInput._clearActionOverride()
- 位置: L4858-4862
- 役割: 押下数を 0 に戻し、action-override 属性を入力欄と結果パネルから外す。
- 触るとき: 修飾キーが離されず action-override が残る不具合を調べるとき。
- 呼び出し先: `this.removeAttribute()`, `this.view.panel.removeAttribute()`
- 参照: `this._actionOverrideKeyCount`

## SmartbarInput._recordSearch()
- 位置: L4894-4921
- 役割: 検索の記録データ(エンジン、検索元、検索語、新しいタブ用のセッション、ワンオフかどうか)を作り、タブで開く場合は recordSearchInOpenedTab、それ以外は recordSearch に渡す。
- 触るとき: 検索テレメトリや検索履歴に載る項目を増やすとき、またはタブで開く検索の記録先を調べるとき。
- 呼び出し先: `this.getSearchSource()`, `this.view.oneOffSearchButtons?.eventTargetIsAOneOff()`, `where.startsWith()`
- 条件付き依存: `if (where.startsWith("tab"))` → `this.parentController.recordSearchInOpenedTab()`
- 条件付き依存: `if (!(where.startsWith("tab")))` → `this.parentController.recordSearch()`
- 参照: `engine.id`, `this._handoffSession`

## SmartbarInput._trimValue()
- 位置: L4931-4944
- 役割: アドレスバーで trimURLs が有効なら値の http:// や末尾のスラッシュを外す。ただし外すと RTL になる値と、混合コンテンツ表示の値は外さない。
- 触るとき: trimURLs の設定でどの値が短く表示されるかを確かめるとき、または RTL の表示崩れを調べるとき。
- 呼び出し先: `UrlbarContentUtils.isTextDirectionRTL()`, `UrlbarPrefs.get()`, `lazy.BrowserUIUtils.trimURL()`, `this.#getValueFormatter()`, `this.#getValueFormatter().willShowFormattedMixedContentProtocol()`
- 参照: `this.#isAddressbar`

## SmartbarInput._maybeCanonizeURL()
- 位置: L4957-4999
- 役割: キーボード操作で、URL らしくない語だけの入力に www. とドメインの接尾辞を付けて URI fixup し、値を置き換えて返す。条件に合わなければ null を返す。
- 触るとき: Ctrl+Enter などで入力に .com 相当の接尾辞を付ける挙動を変えるとき。
- 呼び出し先: `/^\s*[^.:\/\s]+(?:\/.*|\s*)$/i.test()`, `Services.uriFixup.getFixupURIInfo()`, `console.error()`, `suffix.endsWith()`, `this.controller.isCanonizeKeyboardEvent()`, `value.indexOf()`, `value.trim()`
- 条件付き依存: `if (firstSlash >= 0)` → `value.substring()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAGS_MAKE_ALTERNATE_URI`, `Services.locale.urlFixupSuffix`, `info.fixedURI.spec`, `this.value`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.locale` / `Services.uriFixup`

## SmartbarInput._autofillValue()
- 位置: L5021-5061
- 役割: 自動補完の値を入力欄に入れ、末尾に続く補完部分だけなら範囲置換で、そうでなければ全体を設定して選択範囲を指定する。その後、補完 placeholder を保存する。処理中は _applyingAutofill を立てて selectionchange による誤適用を防ぐ。
- 触るとき: 自動補完が入力欄に出る経路や、補完中の選択が崩れる不具合を調べるとき。
- 呼び出し先: `value.substring()`
- 条件付き依存: `if (this.value === value.substring(0, selectionStart))` → `this.#setInputRangeText()`
- 条件付き依存: `if (this.value === value.substring(0, selectionStart))` → `value.substring()`
- 条件付き依存: `if (this.value === value.substring(0, selectionStart))` → `this.formatValue()`
- 条件付き依存: `if (!(this.value === value.substring(0, selectionStart)))` → `this.setValue()`
- 条件付き依存: `if (!(this.value === value.substring(0, selectionStart)))` → `this.setSelectionRange()`
- 参照: `this._applyingAutofill`, `this._autofillPlaceholder`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this.value`, `this.value.length`

## SmartbarInput.#pickMenuResult()
- 位置: L5070-5117
- 役割: 結果メニューの項目(manage、help、その他 URL)を処理する。manage は検索設定画面を開き、それ以外は URL を開く。helpは新しいタブで開く。engagement を記録し、ビューを閉じる。
- 触るとき: 結果の右メニューから開く項目の動作(設定画面、ヘルプ、URL)を変えるとき。
- 呼び出し先: `this.#loadURL()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.view.close()`
- 条件付き依存: `if (element.dataset.command == "manage")` → `this.window.openPreferences()`
- 参照: `element.dataset.command`, `element.dataset.url`, `result.payload.helpUrl`, `result.source`, `result.type`, `this._lastSearchString`, `this.isPrivate`, `this.sapLocation`, `this.windowMode`

## SmartbarInput.#loadURL()
- 位置: async L5148-5238
- 役割: URL または検索を、指定の場所(現在のタブ、新規タブ、ウィンドウ)で読み込む中心。Enter の keydown と keyup の連携を処理し、アドレスバーでは表示をロード先の URL に合わせ、読み込みを parentController に渡す。元に戻すか、エラー時には再度 revert する。最後にビューを閉じる。
- 触るとき: 読み込み先の決め方、読み込み時のパラメータ、Enter 押下からフォーカス移動までの流れを変えるとき。
- 呼び出し先: `KeyboardEvent.isInstance()`, `keyDownEnterDeferred?.resolve()`, `this.#notifyStartNavigation()`, `this.parentController.loadURL()`, `this.view.close()`
- 条件付き依存: `if (!(loadRequest.engineSearch))` → `losslessDecodeURI()`
- 条件付き依存: `if (where == "current")` → `loadRequest.urlLoad?.url.startsWith()`
- 条件付き依存: `if (!params.avoidBrowserFocus)` → `this.setSelectionRange()`
- 条件付き依存: `if (where != "current")` → `this.handleRevert()`
- 条件付き依存: `if (loadStatus.reverted)` → `this.handleRevert()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `event.keyCode`, `loadRequest.engineSearch`, `loadRequest.engineSearch.query`, `loadRequest.urlLoad`, `loadStatus.browserId`, `loadStatus.reverted`, `new URL(url).URI`, `params.allowPinnedTabHostChange`, `params.allowPopups`, `params.allowThirdPartyFixup`, `params.avoidBrowserFocus`, `params.indicateErrorPageLoad`, `params.private`, `this.#isAddressbar`, `this._keyDownEnterDeferred`, `this._keyDownEnterDeferred.loadedContent`, `this.isPrivate`, `this.value`

## SmartbarInput._initCopyCutController()
- 位置: L5240-5250
- 役割: スマートバーでなければ、入力欄に CopyCutController を一度だけ先頭で差し込む。
- 触るとき: コピーとカットの処理がどのコントローラーで行われるかを追うとき。
- 呼び出し先: `this.inputField.controllers.insertControllerAt()`
- 参照: `this.#isSmartbarMode`, `this._copyCutController`

## SmartbarInput.#stripURI()
- 位置: L5259-5279
- 役割: 選択中の値(コピー対象)を URI にして QueryStringStripper の stripForCopyOrShare で追跡用パラメータを除き、表示可能な URL を返す。失敗時は元の URI を返す。
- 触るとき: 「クリーンなリンクをコピー」の結果が想定の URL にならないときに、どのパラメータが外されるかを追うとき。
- 呼び出し先: `Services.io.newURI()`, `console.warn()`, `lazy.QueryStringStripper.stripForCopyOrShare()`, `this._getSelectedValueForClipboard()`
- 条件付き依存: `if (strippedURI)` → `this.makeURIReadable()`
- 参照: `e.message`
- XPCOM: `Services.io`

## SmartbarInput.#isClipboardURIValid()
- 位置: L5286-5293
- 役割: コピー対象の文字列が URL として解釈できるかを返す。
- 触るとき: URL でない選択で「クリーンなリンクをコピー」を出す条件を変えるとき。
- 呼び出し先: `URL.canParse()`, `this._getSelectedValueForClipboard()`

## SmartbarInput.#canStrip()
- 位置: L5300-5313
- 役割: コピー対象の URL に、共有時に除去できるクエリパラメータがあるかを canStripForShare で判定する。解釈できなければ false。
- 触るとき: 除去できるものが無いときに項目を無効にする判断を確かめるとき。
- 呼び出し先: `Services.io.newURI()`, `console.warn()`, `lazy.QueryStringStripper.canStripForShare()`, `this._getSelectedValueForClipboard()`
- XPCOM: `Services.io`

## SmartbarInput.#maybeUntrimUrl()
- 位置: L5325-5400
- 役割: フォーカス中で、表示から除いた http:// や www. があるときに、値を元の URL に戻す。選択位置はその分ずらし、末尾のスラッシュも考慮する。全選択中は戻さない。
- 触るとき: URL を編集するときに省略表示が戻って選択がずれる不具合を調べるとき。
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`, `this.setSelectionRange()`, `this.setValue()`
- 条件付き依存: `if (moveCursorToStart)` → `this.setValue()`
- 条件付き依存: `if (moveCursorToStart)` → `this.setSelectionRange()`
- 条件付き依存: `if (!(selectionStart != 0))` → `Services.io.newURI()`
- 条件付き依存: `if (!(selectionStart != 0))` → `[uri.userPass, uri.displayHost] .filter(Boolean) .join()`
- 条件付き依存: `if (!(selectionStart != 0))` → `[uri.userPass, uri.displayHost] .filter()`
- 条件付き依存: `if (!(selectionStart != 0))` → `logger().error()`
- 条件付き依存: `if (!(selectionStart != 0))` → `logger()`
- 条件付き依存: `if (!(selectionStart != 0))` → `this.#selectedText.startsWith()`
- 参照: `"www.".length`, `lazy.BrowserUIUtils.trimURLProtocol.length`, `this.#allTextSelected`, `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._protocolIsTrimmed`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.focused`, `this.selectionEnd`, `this.selectionStart`, `this.value.length`, `this.valueIsTyped`, `uri.displayHost`, `uri.userPass`
- XPCOM: `Services.io`

## SmartbarInput._initStripOnShare()
- 位置: L5404-5451
- 役割: 文脈メニューに「クリーンなリンクをコピー」を、コピーの後ろに入れる項目セットを登録する。
- 触るとき: この項目を出す位置、表示条件、無効化の条件を変えるとき。
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L5407-5424
- 役割: 「クリーンなリンクをコピー」の menuitem を作り、押されたら #stripURI の結果の表示文字列をクリップボードへ入れる。
- 触るとき: コピーされる値の決め方や、項目の見た目を変えるとき。
- 呼び出し先: `doc.createDocumentFragment()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `fragment.appendChild()`, `lazy.ClipboardHelper.copyString()`, `stripOnShare.addEventListener()`, `stripOnShare.setAttribute()`, `this.#stripURI()`
- 参照: `stripOnShare.id`, `strippedURI.displaySpec`, `this.ownerDocument`

## onShowing()
- 位置: L5426-5449
- 役割: 機能が無効なら隠し、コピーが有効でコピー対象が URL のときだけ表示する。除去できるものが無ければ無効にする。
- 触るとき: メニューを開いたときに項目を出す条件を調整するとき。
- 呼び出し先: `UrlbarPrefs.get()`, `controller.isCommandEnabled()`, `stripOnShare.removeAttribute()`, `this.#canStrip()`, `this.#isClipboardURIValid()`, `this.document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if ( !UrlbarPrefs.get("privacy.query_stripping.strip_on_share.enabled") )` → `stripOnShare.setAttribute()`
- 条件付き依存: `if ( !controller.isCommandEnabled("cmd_copy") || !this.#isClipboardURIValid() )` → `stripOnShare.setAttribute()`
- 条件付き依存: `if (!this.#canStrip())` → `stripOnShare.setAttribute()`

## SmartbarInput.#pasteAndGoEnabled()
- 位置: L5458-5468
- 役割: スマートバーでは、クリップボードに text/plain があるかを返す。それ以外は cmd_paste が有効かを返す。
- 触るとき: 貼り付けて移動の項目が無効に見える不具合を追うとき。
- 呼び出し先: `this.document.commandDispatcher .getControllerForCommand()`, `this.document.commandDispatcher .getControllerForCommand("cmd_paste") .isCommandEnabled()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `Services.clipboard.hasDataMatchingFlavors()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `this.#isSmartbarMode`
- XPCOM: `nsIClipboard` / `Services.clipboard`

## SmartbarInput.#pasteForPasteAndGo()
- 位置: L5473-5483
- 役割: スマートバーでは、クリップボードの text/plain を入力欄に入れる。それ以外は cmd_paste を実行する。
- 触るとき: 貼り付けて移動の貼り付けの仕方を変えるとき。
- 呼び出し先: `this.#readClipboardData()`, `this.#readClipboardData()?.getData()`
- 条件付き依存: `if (!this.#isSmartbarMode)` → `this.window.goDoCommand()`
- 参照: `this.#isSmartbarMode`, `this.value`

## SmartbarInput._initPasteAndGo()
- 位置: L5485-5545
- 役割: 文脈メニューに「貼り付けて移動」を、貼り付けの後ろに入れる項目セットを登録する。
- 触るとき: この項目の位置や表示条件を変えるとき。
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L5488-5514
- 役割: 「貼り付けて移動」の menuitem を作る。押すと検索開始を抑止し、全選択して貼り付け、結果を外してから handleCommand で送信し、抑止を解除する(永続抑止中は解除しない)。
- 触るとき: 貼り付けてすぐ移動する動作の流れ(抑止、送信、キャッシュの掃除)を変えるとき。
- 呼び出し先: `Services.strings .createBundle()`, `Services.strings .createBundle("chrome://browser/locale/browser.properties") .GetStringFromName()`, `doc.createDocumentFragment()`, `doc.createXULElement()`, `fragment.appendChild()`, `pasteAndGo.addEventListener()`, `pasteAndGo.setAttribute()`, `this.#pasteForPasteAndGo()`, `this.handleCommand()`, `this.parentController.clearLastQueryContextCache()`, `this.select()`, `this.setResultForCurrentValue()`, `this.suppressStartQuery()`
- 条件付き依存: `if (!this._permanentlySuppressStartQuery)` → `this.unsuppressStartQuery()`
- 参照: `pasteAndGo.id`, `this._permanentlySuppressStartQuery`, `this.ownerDocument`
- XPCOM: `Services.strings`

## onShowing()
- 位置: L5515-5543
- 役割: メニューを開くときに結果一覧を閉じ、編集メニューに accesskey の衝突注記を一時的に付ける(閉じたら外す)。貼り付けできなければ項目を無効にする。
- 触るとき: メニューを開いたときの結果一覧の扱いや、アクセスキーの衝突対策を変えるとき。
- 呼び出し先: `popup.addEventListener()`, `popup.setAttribute()`, `this.#pasteAndGoEnabled()`, `this.view.close()`
- 条件付き依存: `if (popup.state == "closed")` → `popup.removeAttribute()`
- 条件付き依存: `if (this.#pasteAndGoEnabled())` → `pasteAndGo.removeAttribute()`
- 条件付き依存: `if (!(this.#pasteAndGoEnabled()))` → `pasteAndGo.setAttribute()`
- 参照: `popup.state`, `this.#editContextMenu.popup`

## SmartbarInput._initAutofillDismiss()
- 位置: L5549-5591
- 役割: 文脈メニューに「候補から除外」と「履歴から削除」を、すべて選択の後ろに入れる項目セットを登録する。
- 触るとき: 自動補完の取り消し項目の位置や対象を変えるとき。
- 呼び出し先: `this.#addContextMenuItems()`

## createItems()
- 位置: L5552-5582
- 役割: 区切り線、「候補から除外」「履歴から削除」の3つの要素を作り、それぞれ dismiss と forget の処理を呼ぶ。
- 触るとき: 自動補完の取り消し項目の文言や動作を変えるとき。
- 呼び出し先: `dismiss.addEventListener()`, `dismiss.setAttribute()`, `doc.createDocumentFragment()`, `doc.createXULElement()`, `doc.l10n.setAttributes()`, `forget.addEventListener()`, `forget.setAttribute()`, `fragment.append()`, `separator.setAttribute()`, `this.#dismissAdaptiveAutofillFromContextMenu()`
- 参照: `this.ownerDocument`

## onShowing()
- 位置: L5583-5589
- 役割: #autofillDismissContextMenuVisibility の結果に応じて、区切り線と2つの項目の hidden を切り替える。
- 触るとき: 自動補完の取り消し項目をいつ出すかを変えるとき。
- 呼び出し先: `this.#autofillDismissContextMenuVisibility()`
- 参照: `dismiss.hidden`, `forget.hidden`, `separator.hidden`

## SmartbarInput.#autofillDismissContextMenuVisibility()
- 位置: L5605-5631
- 役割: 適応履歴が有効で、見出しが適応的な自動補完または origin 補完のときに「候補から除外」を出し(私用ウィンドウでは出さない)、補完先が深いリンクなら「履歴から削除」を出す。
- 触るとき: 自動補完の取り消し項目が出る条件(履歴設定、補完の種類、私用ウィンドウ)を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isOriginUrl()`
- 参照: `result.autofill`, `result.autofill.type`, `result.payload.url`, `result?.heuristic`, `this._resultForCurrentValue`, `this.isPrivate`

## SmartbarInput.#dismissAdaptiveAutofillFromContextMenu()
- 位置: async L5640-5656
- 役割: 見出しが自動補完のときに parentController.dismissAutofill で「除外」か「削除」を行い、入力欄を直前の検索文字列に戻して補完を無効にしたまま検索し直す。
- 触るとき: 自動補完を除外・削除したあとに入力欄の表示や再検索が正しいかを確かめるとき。
- 呼び出し先: `this.parentController .dismissAutofill()`, `this.parentController .dismissAutofill(result.payload.url, action) .catch()`, `this.setValue()`, `this.startQuery()`
- 参照: `console.error`, `result.autofill`, `result.payload.url`, `result?.heuristic`, `this._lastSearchString`, `this._resultForCurrentValue`

## SmartbarInput.#notifyStartNavigation()
- 位置: L5668-5675
- 役割: アドレスバーで、ユーザーが移動を始めたことを observer service に通知する。結果情報を一緒に渡す。
- 触るとき: 移動開始を監視する側(テレメトリや他の機能)が受け取る情報を変えるとき。
- 条件付き依存: `if (this.#isAddressbar)` → `Services.obs.notifyObservers()`
- 参照: `this.#isAddressbar`
- XPCOM: `Services.obs`

## SmartbarInput._searchModeForResult()
- 位置: L5689-5737
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.searchModeForToken()`
- 条件付き依存: `if (!(result.type == UrlbarShared.RESULT_TYPE.RESTRICT))` → `UrlbarShared.SEARCH_MODE_RESTRICT.has()`
- 参照: `UrlbarShared.RESULT_TYPE.RESTRICT`, `result.payload.dynamicType`, `result.payload.engine`, `result.payload.keyword`, `result.payload.originalEngine`, `result.providerName`, `result.type`, `searchMode.entry`, `searchMode.restrictType`

## SmartbarInput.#updateCtaSearchEngineInfo()
- 位置: async L5742-5777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `e.getIconURL()`, `engine.getIconURL()`, `this.controller.engineStore .getEngines()`, `this.controller.engineStore .getEngines() .filter()`, `this.controller.engineStore .getEngines() .filter(e => !e.hideOneOffButton) .map()`, `this.controller.engineStore.getEngineByName()`, `this.controller.engineStore.init()`
- 参照: `e.hideOneOffButton`, `e.name`, `engine.name`, `this.#isSmartbarMode`, `this.#smartbarSearchEngineName`, `this._inputCta.searchEngineInfo`, `this._inputCta.searchEngines`, `this.controller.engineStore.default`

## SmartbarInput._updateSearchModeUI()
- 位置: L5785-5850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarSearchTermsPersistence.onSearchModeChanged()`, `this.dispatchEvent()`, `this.getAttribute()`, `this.hasAttribute()`, `this.toggleAttribute()`
- 条件付き依存: `if (this._searchModeIndicatorTitle)` → `this._searchModeIndicatorTitle.removeAttribute()`
- 条件付き依存: `if (!engineName && !source)` → `this.removeAttribute()`
- 条件付き依存: `if (!engineName && !source)` → `this.updatePlaceholder()`
- 条件付き依存: `if (engineName)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (source)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (source)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (this.getAttribute("pageproxystate") == "valid")` → `this.setPageProxyState()`
- 参照: `this.#isAddressbar`, `this._autofillPlaceholder`, `this._searchModeIndicatorTitle`, `this._searchModeIndicatorTitle.textContent`, `this.inputField`, `this.userTypedValue`, `this.value`, `this.window`

## SmartbarInput.#handlePersistedSearchTerms()
- 位置: L5870-5940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarSearchTermsPersistence.shouldPersist()`, `lazy.UrlbarUtils.isPersistedSearchTermsEnabled()`, `state.persist.originalURI.equals()`, `this.toggleAttribute()`
- 条件付き依存: `if (state.persist)` → `this.removeAttribute()`
- 条件付き依存: `if (firstView || cachedUriDidChange)` → `lazy.UrlbarSearchTermsPersistence.setPersistenceState()`
- 条件付き依存: `if (state.persist.shouldPersist && !isSameDocument)` → `Glean.urlbarPersistedsearchterms.viewCount.add()`
- 参照: `state.persist`, `state.persist.searchTerms`, `state.persist.shouldPersist`, `state.persist?.originalURI`, `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.userTypedValue`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser.originalURI`

## SmartbarInput.#initPlaceholderFromPref()
- 位置: L5949-5960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (engineName)` → `this._setPlaceholder()`
- 参照: `this.#isAddressbar`, `this.controller.engineStore.failed`, `this.isPrivate`

## SmartbarInput.#initEngineStoreAfterPaint()
- 位置: async L5973-5982
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.engineStore.init()`
- 条件付き依存: `if (document.readyState == "loading")` → `document.addEventListener()`
- 条件付き依存: `if (document.readyState == "loading")` → `this.window.requestIdleCallback()`
- 参照: `document.readyState`

## SmartbarInput.#deferUpdatePlaceholder()
- 位置: async L5994-6037
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.inputField.dataset.l10nId == "urlbar-placeholder-with-name")` → `this.updatePlaceholder()`
- 条件付き依存: `if (!this.value)` → `this.inputField.addEventListener()`
- 条件付き依存: `if (!this.value)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (!(!this.value))` → `this.updatePlaceholder()`
- 参照: `this.inputField.dataset.l10nId`, `this.sapName`, `this.value`

## updateListener()
- 位置: L6013-6027
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.searchModeSwitcher.updateSearchIcon().catch()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.searchModeSwitcher.updateSearchIcon()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.updatePlaceholder()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.inputField.removeEventListener()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 参照: `console.error`, `this.searchMode`, `this.value`

## SmartbarInput.setUnifiedSearchButtonAvailability()
- 位置: L6044-6058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getBrowserState()`, `this.querySelector()`, `this.toggleAttribute()`
- 条件付き依存: `if (available)` → `switcher.removeAttribute()`
- 条件付き依存: `if (!(available))` → `switcher.setAttribute()`
- 参照: `this.#isSmartbarMode`, `this.getBrowserState( this.window.gBrowser.selectedBrowser ).isUnifiedSearchButtonAvailable`, `this.window.gBrowser.selectedBrowser`

## SmartbarInput.updatePlaceholder()
- 位置: L6063-6078
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (defaultEngine?.isConfigEngine)` → `this._setPlaceholder()`
- 条件付き依存: `if (!(defaultEngine?.isConfigEngine))` → `this._setPlaceholder()`
- 参照: `defaultEngine.name`, `defaultEngine?.isConfigEngine`, `this.#isAddressbar`, `this.controller.engineStore.default`, `this.searchMode`

## SmartbarInput._setPlaceholder()
- 位置: L6087-6114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.document.l10n.setAttributes()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (!this.#isAddressbar)` → `this.document.l10n.setAttributes()`
- 参照: `this.#isAddressbar`, `this.#isSmartbarMode`, `this.inputField`

## SmartbarInput.#maybeSelectAll()
- 位置: L6120-6132
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this._preventClickSelectsAll && this.#compositionState != UrlbarShared.COMPOSITION.COMPOSING && this.focused && this.selectionStart == this.selectionEnd )` → `this.select()`
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionState`, `this.#isSmartbarMode`, `this._preventClickSelectsAll`, `this.focused`, `this.selectionEnd`, `this.selectionStart`

## SmartbarInput._on_command()
- 位置: L6136-6148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if ( !event.target.classList.contains("urlbarView-result-menuitem") && (!event.target.classList.contains("searchbar-engine-one-off-item") || this.searchMode?.ent...)` → `this.controller.engagementEvent.discard()`
- 参照: `this.searchMode?.entry`

## SmartbarInput._on_blur()
- 位置: L6150-6237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `UrlbarPrefs.get()`, `lazy.ExtensionSearchHandler.hasActiveInputSession()`, `logger()`, `logger().debug()`, `this.#isInsideContainer()`, `this._clearActionOverride()`, `this._resetSearchState()`, `this.controller.engagementEvent.record()`, `this.getAttribute()`, `this.getSearchSource()`, `this.removeAttribute()`, `this.view.resultMenu.hasAttribute()`
- 条件付き依存: `if (!( this.value == this._untrimmedValue && !this.userTypedValue && !this.focused ))` → `this.formatValue()`
- 条件付き依存: `if (lazy.ExtensionSearchHandler.hasActiveInputSession())` → `lazy.ExtensionSearchHandler.handleInputCancelled()`
- 条件付き依存: `if ( !UrlbarPrefs.get("ui.popup.disable_autohide") && !this.#isInsideContainer( event.relatedTarget, this.smartbarButtonContainer ) )` → `this.view.close()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") != "valid" && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 条件付き依存: `if (this._keyDownEnterDeferred)` → `this._keyDownEnterDeferred.resolve()`
- 参照: `event.relatedTarget`, `this._autofillPlaceholder`, `this._handoffSession`, `this._isHandoffSession`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._lastSearchString`, `this._untrimmedValue`, `this.focused`, `this.focusedViaMousedown`, `this.sapLocation`, `this.smartbarButtonContainer`, `this.userTypedValue`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`, `this.windowMode`
- XPCOM: `Services.obs`

## SmartbarInput._on_click()
- 位置: L6239-6270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeSelectAll()`, `this.#maybeUntrimUrl()`, `this.handleCommand()`, `this.handleRevert()`, `this.select()`
- 条件付き依存: `if (this.view.isOpen)` → `this.startQuery()`
- 参照: `event.button`, `event.target`, `this._inputContainer`, `this._revertButton`, `this._searchModeIndicatorClose`, `this.goButton`, `this.inputField`, `this.searchMode`, `this.view.isOpen`, `this.view.oneOffSearchButtons`, `this.view.oneOffSearchButtons.selectedButton`

## SmartbarInput._on_contextmenu()
- 位置: L6272-6279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#maybeSelectAll()`
- 参照: `event.button`

## SmartbarInput._on_focus()
- 位置: L6281-6350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `logger()`, `logger().debug()`, `this._updateUrlTooltip()`, `this.formatValue()`, `this.getAttribute()`
- 条件付き依存: `if (!this._hideFocus)` → `this.toggleAttribute()`
- 条件付き依存: `if (!untrim)` → `UrlbarContentUtils.getFixupPrimitives()`
- 条件付き依存: `if (fixedDisplaySpec)` → `UrlbarContentUtils.getDisplaySpec()`
- 条件付き依存: `if (!(expectedDisplaySpec == null))` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (!(expectedDisplaySpec == null))` → `this._untrimmedValue.startsWith()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && this._untrimmedValue.startsWith("https://") )` → `fixedDisplaySpec.replace()`
- 条件付き依存: `if (untrim)` → `this.setValue()`
- 条件付き依存: `if (this.focusedViaMousedown && !this._permanentlySuppressStartQuery)` → `this.view.autoOpen()`
- 条件付き依存: `if (this._untrimOnFocusAfterKeydown)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (!(this.focusedViaMousedown && !this._permanentlySuppressStartQuery))` → `this.inputField.hasAttribute()`
- 条件付き依存: `if (this.inputField.hasAttribute("refocused-by-panel"))` → `this.#maybeSelectAll()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") != "valid" && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 参照: `UrlbarContentUtils.getFixupPrimitives( this.value, this.isPrivate )?.preferredURIDisplaySpec`, `this._hideFocus`, `this._permanentlySuppressStartQuery`, `this._protocolIsTrimmed`, `this._untrimOnFocusAfterKeydown`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.focusedViaMousedown`, `this.isPrivate`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`
- XPCOM: `Services.obs`

## SmartbarInput._on_mouseover()
- 位置: L6352-6354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateUrlTooltip()`

## SmartbarInput._on_draggableregionleftmousedown()
- 位置: L6356-6360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`

## SmartbarInput._on_mousedown()
- 位置: L6362-6445
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `event.target.closest()`, `this.#isInsideContainer()`, `this.hasAttribute()`, `this.view.autoOpen()`
- 条件付き依存: `if ( !this.#isInsideContainer(event.composedTarget, this.inputField) && event.composedTarget != this._inputContainer )` → `this.#isInsideContainer()`
- 条件付き依存: `if ( this.#isInsideContainer( event.composedTarget, this.smartbarButtonContainer ) )` → `event.preventDefault()`
- 条件付き依存: `if (!this.#isInsideContainer(event.composedTarget, this.inputField))` → `this.focus()`
- 条件付き依存: `if (this.focusedViaMousedown && !this.#isSmartbarMode)` → `this.setSelectionRange()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.hasAttribute()`
- 条件付き依存: `if (this.view.isOpen && !this.hasAttribute("focused"))` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (this.view.isOpen && !this.hasAttribute("focused"))` → `this.getSearchSource()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`
- 参照: `event.button`, `event.composedTarget`, `event.currentTarget`, `this.#isSmartbarMode`, `this._inputContainer`, `this._lastSearchString`, `this._mousedownOnUrlbarDescendant`, `this._preventClickSelectsAll`, `this.focused`, `this.focusedViaMousedown`, `this.inputField`, `this.sapLocation`, `this.smartbarButtonContainer`, `this.view.isOpen`, `this.window`, `this.windowMode`

## SmartbarInput._on_input()
- 位置: L6447-6596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isPasteEvent()`, `event.inputType?.startsWith()`, `getAgentCommandId()`, `this._maybeAutofillPlaceholder()`, `this.getAttribute()`, `this.removeAttribute()`, `this.startQuery()`, `this.toggleAttribute()`, `this.view.removeAccessibleFocus()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.value === this.userTypedValue && (event.inputType === "deleteContentBackward" || event.inputType === "deleteContentForward") )` → `this.parentController.recordAutofillDeletion()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") == "valid" && this.value != this._lastValidURLStr )` → `this.setPageProxyState()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 条件付き依存: `if ( state.persist?.shouldPersist && this.value !== state.persist.searchTerms )` → `this.removeAttribute()`
- 条件付き依存: `if (previousCommandId && event.inputType && !this.#isAgentCommand)` → `Glean.smartWindow.agentCommandRemove.record()`
- 条件付き依存: `if (previousCommandId && event.inputType && !this.#isAgentCommand)` → `String()`
- 条件付き依存: `if (this.inputField.hasMention || this.#isAgentCommand)` → `this.suppressStartQuery()`
- 条件付き依存: `if (!this._permanentlySuppressStartQuery)` → `this.unsuppressStartQuery()`
- 条件付き依存: `if (!value)` → `this.#updateSmartbarCTAButton()`
- 条件付き依存: `if (this.view.isOpen)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("closeOtherPanelsOnOpen"))` → `this.window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface(Ci.nsIAppWindow) .rollupAllPopups()`
- 条件付き依存: `if (UrlbarPrefs.get("closeOtherPanelsOnOpen"))` → `this.window.docShell.treeOwner .QueryInterface(Ci.nsIInterfaceRequestor) .getInterface()`
- 条件付き依存: `if (UrlbarPrefs.get("closeOtherPanelsOnOpen"))` → `this.window.docShell.treeOwner .QueryInterface()`
- 条件付き依存: `if (!willShowResults)` → `this.view.clear()`
- 条件付き依存: `if (!this.searchMode || !this.view.oneOffSearchButtons?.hasView)` → `this.view.close()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.view.clear()`
- 参照: `Ci.nsIAppWindow`, `Ci.nsIInterfaceRequestor`, `UrlbarShared.COMPOSITION.CANCELED`, `UrlbarShared.COMPOSITION.COMPOSING`, `UrlbarShared.COMPOSITION.NONE`, `event.data`, `event.inputType`, `state.persist.searchTerms`, `state.persist.shouldPersist`, `state.persist?.shouldPersist`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this.#inputEpoch`, `this.#isAddressbar`, `this.#isAgentCommand`, `this.#isSmartbarMode`, `this._autofillPlaceholder`, `this._lastValidURLStr`, `this._permanentlySuppressStartQuery`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.controller.userSelectionBehavior`, `this.conversationTelemetryInfo`, `this.inputField.hasMention`, `this.sapLocation`, `this.searchMode`, `this.untrimmedValue`, `this.userTypedValue`, `this.value`, `this.valueIsTyped`, `this.view.isOpen`, `this.view.oneOffSearchButtons?.hasView`, `this.window.gBrowser.selectedBrowser`
- XPCOM: `nsIAppWindow` / [`nsIInterfaceRequestor`](../../../../netwerk/base/nsIChannel.idl.md)

## SmartbarInput._on_selectionchange()
- 位置: L6598-6612
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._applyingAutofill`, `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._autofillPlaceholder.value`, `this.selectionEnd`, `this.selectionStart`, `this.userTypedValue`, `this.value`

## SmartbarInput._on_select()
- 位置: L6614-6648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.clipboard.isClipboardTypeSupported()`, `lazy.ClipboardHelper.copyStringToClipboard()`, `this._getSelectedValueForClipboard()`
- 参照: `Services.clipboard.kSelectionClipboard`, `this._suppressPrimaryAdjustment`, `this.window.windowUtils.isHandlingUserInput`
- XPCOM: `Services.clipboard`

## SmartbarInput._on_overflow()
- 位置: L6650-6653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateTextOverflow()`
- 参照: `this._overflowing`

## SmartbarInput._on_underflow()
- 位置: L6655-6659
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._updateUrlTooltip()`, `this.updateTextOverflow()`
- 参照: `this._overflowing`

## SmartbarInput._on_paste()
- 位置: L6661-6712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getFixupPrimitives()`, `UrlbarShared.sanitizeTextFromClipboard()`, `event.clipboardData.getData()`, `oldStart.trim()`, `oldValue.substring()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `event.preventDefault()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `event.stopImmediatePropagation()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.setValue()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("pageproxystate") == "valid")` → `this.setPageProxyState()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.toggleAttribute()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.setSelectionRange()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.startQuery()`
- 参照: `oldStart.length`, `pasteData.length`, `this._untrimmedValue`, `this.isPrivate`, `this.selectionEnd`, `this.selectionStart`, `this.userTypedValue`, `this.value`

## SmartbarInput.#makeQueryContext()
- 位置: L6728-6783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isPasteEvent()`
- 条件付き依存: `if (this.#isSmartbarMode)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!(this.#isSmartbarMode))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (this.window.gBrowser)` → `parseInt()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.window.gBrowser.selectedBrowser?.getAttribute()`
- 条件付き依存: `if (this.searchMode)` → `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_SOURCE.ACTIONS`, `event.data?.length`, `lazy.UrlbarQueryContext`, `options.currentPage`, `options.searchMode`, `options.sources`, `options.tabGroup`, `options.userContextId`, `this.#isSmartbarMode`, `this.isPrivate`, `this.sapName`, `this.searchMode`, `this.searchMode.source`, `this.searchMode?.source`, `this.window.gBrowser`, `this.window.gBrowser.currentURI?.spec`, `this.window.gBrowser.selectedTab.group?.id`

## SmartbarInput._on_scroll()
- 位置: L6794-6802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CSS.supports()`, `this.#updatePanelScrollFade()`
- 参照: `event.target`, `this.view.panel`

## SmartbarInput.#updatePanelScrollFade()
- 位置: L6804-6823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `progress.toFixed()`, `this.view.panel.style.setProperty()`, `this.view.panel.toggleAttribute()`, `this.window.requestAnimationFrame()`
- 参照: `this.#scrollAnimationId`, `this.view.panel`

## SmartbarInput._on_scrollend()
- 位置: L6825-6827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateTextOverflow()`

## SmartbarInput._on_TabSelect()
- 位置: L6829-6840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._afterTabSelectAndFocusChange()`
- 条件付き依存: `if (this.#isSidebarMode)` → `this.#updateContextChips()`
- 参照: `this.#isSidebarMode`, `this._gotTabSelect`, `this._untrimOnFocusAfterKeydown`

## SmartbarInput._on_TabAttrModified()
- 位置: L6842-6851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.detail.changed.includes()`
- 条件付き依存: `if ( this.#isSidebarMode && event.target == this.window.gBrowser.selectedTab && (event.detail.changed.includes("image") || event.detail.changed.includes("label")) )` → `this.#updateContextChips()`
- 参照: `event.target`, `this.#isSidebarMode`, `this.window.gBrowser.selectedTab`

## SmartbarInput._on_TabClose()
- 位置: L6853-6862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.handleBounceEventTrigger()`
- 条件付き依存: `if (this.view.isOpen)` → `this.startQuery()`
- 参照: `event.target.linkedBrowser`, `this.view.isOpen`

## SmartbarInput._on_beforeinput()
- 位置: L6864-6881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.view?.shouldSpaceActivateSelectedElement()`
- 条件付き依存: `if (event.data && this._keyDownEnterDeferred)` → `event.preventDefault()`
- 条件付き依存: `if ( this.#isSmartbarMode && event.data == " " && this.view?.shouldSpaceActivateSelectedElement?.() )` → `event.preventDefault()`
- 参照: `event.data`, `this.#isSmartbarMode`, `this._keyDownEnterDeferred`

## SmartbarInput._on_keydown()
- 位置: L6883-6974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.handleKeyNavigation()`, `this.eventBufferer.maybeDeferEvent()`, `this.eventBufferer.shouldDeferEvent()`, `this.view.resultMenu.hasAttribute()`
- 条件付き依存: `if (event.currentTarget == this.window)` → `this.#isInsideContainer()`
- 条件付き依存: `if ( this.#isInsideContainer( event.composedTarget, this.smartbarButtonContainer ) )` → `this.#onActionButtonsKeyDown()`
- 条件付き依存: `if ( this.#isSmartbarMode && event.keyCode === KeyEvent.DOM_VK_RETURN && (event.shiftKey || this.#smartbarAssistantIsGenerating) )` → `event.preventDefault()`
- 条件付き依存: `if (this._keyDownEnterDeferred)` → `this._keyDownEnterDeferred.reject()`
- 条件付き依存: `if (event.keyCode === KeyEvent.DOM_VK_RETURN)` → `Promise.withResolvers()`
- 条件付き依存: `if (event.keyCode === KeyEvent.DOM_VK_RETURN)` → `UrlbarContentUtils.getPlatform()`
- 条件付き依存: `if (!event.repeat)` → `this._toggleActionOverride()`
- 条件付き依存: `if (this.eventBufferer.shouldDeferEvent(event))` → `this.controller.handleKeyNavigation()`
- 参照: `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_LEFT`, `KeyEvent.DOM_VK_META`, `KeyEvent.DOM_VK_RETURN`, `event._disableCanonization`, `event.composedTarget`, `event.ctrlKey`, `event.currentTarget`, `event.keyCode`, `event.metaKey`, `event.repeat`, `event.shiftKey`, `this.#allTextSelected`, `this.#allTextSelectedOnKeyDown`, `this.#inputEpoch`, `this.#isSmartbarMode`, `this.#smartbarAssistantIsGenerating`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._keyDownEnterDeferred.inputEpoch`, `this._untrimOnFocusAfterKeydown`, `this.controller`, `this.focused`, `this.smartbarButtonContainer`, `this.window`

## SmartbarInput._on_keyup()
- 位置: L6976-7009
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._toggleActionOverride()`
- 条件付き依存: `if (this.#allTextSelectedOnKeyDown)` → `this.#isHomeKeyUpEvent()`
- 条件付き依存: `if (this.#allTextSelectedOnKeyDown)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (this._keyDownEnterDeferred && !this._finishingDeferredEnter)` → `this.#finishDeferredEnter()`
- 参照: `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_META`, `event.currentTarget`, `event.keyCode`, `this.#allTextSelectedOnKeyDown`, `this._finishingDeferredEnter`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._untrimOnFocusAfterKeydown`, `this.selectionEnd`, `this.selectionStart`, `this.window`

## SmartbarInput.#finishDeferredEnter()
- 位置: async L7015-7052
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (keyDownEnterDeferred.loadedContent)` → `this.parentController.focusBrowser()`
- 条件付き依存: `if (focused && keyDownEnterDeferred.inputEpoch === this.#inputEpoch)` → `this.setSelectionRange()`
- 条件付き依存: `if (!(keyDownEnterDeferred.loadedContent))` → `keyDownEnterDeferred.resolve()`
- 参照: `keyDownEnterDeferred.inputEpoch`, `keyDownEnterDeferred.loadedContent`, `keyDownEnterDeferred.promise`, `this.#inputEpoch`, `this._finishingDeferredEnter`, `this._keyDownEnterDeferred`

## SmartbarInput._on_compositionstart()
- 位置: L7054-7084
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (this.searchMode)` → `this.confirmSearchMode()`
- 条件付き依存: `if (this.view.isOpen)` → `this.view.close()`
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this.searchMode`, `this.userTypedValue`, `this.value`, `this.view.isOpen`

## SmartbarInput._on_compositionend()
- 位置: L7086-7119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("keepPanelOpenDuringImeComposition"))` → `this.view.clearSelection()`
- 条件付き依存: `if ( !event.data && !this.#compositionHadText && this.#compositionClosedPopup && !UrlbarPrefs.get("keepPanelOpenDuringImeComposition") )` → `this.startQuery()`
- 参照: `UrlbarShared.COMPOSITION.CANCELED`, `UrlbarShared.COMPOSITION.COMMIT`, `UrlbarShared.COMPOSITION.COMPOSING`, `UrlbarShared.COMPOSITION.NONE`, `event.data`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this._resultForCurrentValue`

## SmartbarInput._on_dragstart()
- 位置: L7121-7157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.escapeHtmlEntities()`, `event.dataTransfer.setData()`, `event.stopPropagation()`, `this.getAttribute()`, `this.inputField.compareDocumentPosition()`, `this.makeURIReadable()`, `this.view.close()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `event.dataTransfer.effectAllowed`, `event.originalTarget`, `event.target`, `this.#allTextSelected`, `this.inputField`, `this.window.gBrowser.contentTitle`, `this.window.gBrowser.currentURI`, `uri.displaySpec`

## SmartbarInput._on_dragover()
- 位置: L7164-7168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getDroppableData()`
- 参照: `event.dataTransfer.dropEffect`

## SmartbarInput._on_drop()
- 位置: L7175-7200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.isInstance()`, `getDroppableData()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `Services.droppedLinkHandler.getTriggeringPrincipal()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.setPageProxyState()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.focus()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.#makeQueryContext()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.parentController.setLastQueryContextCache()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.controller.engagementEvent.start()`
- 条件付き依存: `if (droppedURL && droppedURL !== this.window.gBrowser.currentURI.spec)` → `this.handleNavigation()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.setURI()`
- 参照: `droppedItem.href`, `this.#isAddressbar`, `this.userTypedValue`, `this.value`, `this.window.gBrowser.currentURI.spec`
- XPCOM: `Services.droppedLinkHandler`

## SmartbarInput._on_customizationstarting()
- 位置: L7202-7205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.blur()`, `this.incrementPopoverBlockerCount()`

## SmartbarInput._on_aftercustomization()
- 位置: L7207-7210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePopoverAnchor()`, `this.decrementPopoverBlockerCount()`

## SmartbarInput.uiDensityChanged()
- 位置: L7212-7217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updatePopoverAnchor()`
- 参照: `this.#popoverBlockerCount`

## SmartbarInput.#allTextSelected()
- 位置: L7220-7222
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectionEnd`, `this.selectionStart`, `this.value.length`

## SmartbarInput.#getSchemelessInput()
- 位置: L7233-7239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http://", "https://", "file://"].every()`, `value.trim()`, `value.trim().startsWith()`
- 参照: `Ci.nsILoadInfo.SchemelessInputTypeSchemeful`, `Ci.nsILoadInfo.SchemelessInputTypeSchemeless`
- XPCOM: [`nsILoadInfo`](../../../../dom/base/nsIContentPolicy.idl.md)

## SmartbarInput.#isOpenedPageInBlankTargetLoading()
- 位置: L7241-7248
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.gBrowser.selectedBrowser.browsingContext .nonWebControlledLoadingURI`, `this.window.gBrowser.selectedBrowser.browsingContext.sessionHistory ?.count`

## SmartbarInput.#selectedText()
- 位置: L7270-7277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.editor.selection.toStringWithFormat()`
- 参照: `Ci.nsIDocumentEncoder.OutputPreformatted`, `Ci.nsIDocumentEncoder.OutputRaw`
- XPCOM: [`nsIDocumentEncoder`](../../../../dom/serializers/nsIDocumentEncoder.idl.md)

## SmartbarInput.#isHomeKeyUpEvent()
- 位置: L7285-7309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_HOME`, `KeyEvent.DOM_VK_META`, `KeyboardEvent.DOM_VK_A`, `KeyboardEvent.DOM_VK_LEFT`, `event.ctrlKey`, `event.keyCode`, `event.shiftKey`, `this._isKeyDownWithMetaAndLeft`

## SmartbarInput.#updateSmartbarCTAButton()
- 位置: L7317-7345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateGoGuardrail()`
- 参照: `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.URL`, `firstResult.heuristic`, `firstResult.type`, `this.#detectedIntent`, `this.#smartbarActionLocked`, `this.smartbarAction`, `this.value`

## SmartbarInput.getCurrentContextData()
- 位置: L7354-7359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getContextPageUrl()`, `this.getResolvedContextWebsites()`

## SmartbarInput.getContextPageUrl()
- 位置: L7367-7376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `lazy.getCurrentTabUrl()`
- 参照: `currentTabUrl?.spec`, `this.#isSidebarMode`, `this.#removedImplicitTabUrl`, `this.window`

## SmartbarInput.getResolvedContextWebsites()
- 位置: L7384-7411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidates .filter()`, `getContextMentionKey()`, `seen.add()`, `seen.has()`
- 条件付き依存: `if (url && url != this.#removedImplicitTabUrl)` → `candidates.unshift()`
- 条件付き依存: `if (url && url != this.#removedImplicitTabUrl)` → `this.#resolveTabIconSrc()`
- 参照: `tab.image`, `tab.label`, `tab?.linkedBrowser.currentURI?.spec`, `this.#contextWebsites`, `this.#isSidebarMode`, `this.#removedImplicitTabUrl`, `this.window.gBrowser?.selectedTab`

## SmartbarInput.#updateContextChips()
- 位置: L7416-7426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `finalWebsites.forEach()`, `this.#ensureWebsiteIcon()`, `this.#findWebsiteContextChipsContainer()`, `this.getResolvedContextWebsites()`
- 参照: `container.hidden`, `container.removable`, `container.websites`, `finalWebsites.length`

## SmartbarInput.updateContextChips()
- 位置: L7432-7434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`

## SmartbarInput.contextChips()
- 位置: L7442-7444
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#contextWebsites`

## SmartbarInput.removedImplicitContextChip()
- 位置: L7452-7454
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#removedImplicitTabUrl`

## SmartbarInput.restoreContextChips()
- 位置: L7465-7473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`
- 参照: `this.#contextWebsites`, `this.#removedImplicitTabUrl`, `this.window.gBrowser?.selectedTab?.linkedBrowser?.currentURI?.spec`

## SmartbarInput.#resolveTabIconSrc()
- 位置: L7485-7489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getIconForUrl()`, `tabImage?.startsWith()`

## SmartbarInput.#ensureWebsiteIcon()
- 位置: L7496-7501
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getIconForUrl()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `site.iconSrc`, `site.type`, `site.url`

## SmartbarInput.#findWebsiteContextChipsContainer()
- 位置: L7507-7517
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.querySelector()`
- 参照: `this.#websiteContextChipsContainer`, `this.#websiteContextChipsContainer?.isConnected`

## SmartbarInput.isSidebarMode()
- 位置: L7519-7521
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#isSidebarMode`

## SmartbarInput.isSidebarMode()
- 位置: L7526-7535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateContextChips()`, `this.querySelector()`
- 参照: `modelSelect.sidebarMode`, `this.#isSidebarMode`

## SmartbarInput.addContextMention()
- 位置: L7542-7563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getContextMentionKey()`, `this.#contextWebsites.some()`, `this.#updateContextChips()`, `this.dispatchEvent()`
- 参照: `mention.url`, `this.#contextWebsites`, `this.#removedImplicitTabUrl`

## SmartbarInput.removeContextMention()
- 位置: L7570-7594
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contextWebsites.filter()`
- 条件付き依存: `if (this.#contextWebsites.length !== originalLength || isCurrentTab)` → `this.#updateContextChips()`
- 条件付き依存: `if (this.#contextWebsites.length !== originalLength || isCurrentTab)` → `this.dispatchEvent()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `site.groupId`, `site.type`, `site.url`, `this.#contextWebsites`, `this.#contextWebsites.length`, `this.#isSidebarMode`, `this.#removedImplicitTabUrl`, `this.window.gBrowser.selectedTab.linkedBrowser.currentURI?.spec`

## getDroppableData()
- 位置: L7606-7653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.droppedLinkHandler.dropLinks()`, `event.dataTransfer.getData()`
- 条件付き依存: `if (links[0]?.url)` → `event.preventDefault()`
- 条件付き依存: `if (links[0]?.url)` → `UrlbarShared.stripUnsafeProtocolOnPaste()`
- 条件付き依存: `if (UrlbarShared.stripUnsafeProtocolOnPaste(href) != href)` → `event.stopImmediatePropagation()`
- 条件付き依存: `if (links[0]?.url)` → `URL.parse()`
- 条件付き依存: `if (url)` → `Services.droppedLinkHandler.getTriggeringPrincipal()`
- 条件付き依存: `if (url)` → `Services.scriptSecurityManager.checkLoadURIStrWithPrincipal()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_INHERIT_PRINCIPAL`, `links[0].url`, `links[0]?.url`, `url.href`
- XPCOM: `nsIScriptSecurityManager` / `Services.droppedLinkHandler` / `Services.scriptSecurityManager`

## losslessDecodeURI()
- 位置: L7664-7744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/%25(?:3B|2F|3F|3A|40|26|3D|2B|24|2C|23)/i.test()`, `value.replace()`
- 条件付き依存: `if (!/%25(?:3B|2F|3F|3A|40|26|3D|2B|24|2C|23)/i.test(value))` → `["https", "http", "file", "ftp"].includes()`
- 条件付き依存: `if (decodeASCIIOnly)` → `value.replace()`
- 条件付き依存: `if (!(decodeASCIIOnly))` → `decodeURI()`
- 参照: `aURI.displaySpec`, `aURI.scheme`

## CopyCutController.constructor()
- 位置: L7754-7756
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.urlbar`

## CopyCutController.doCommand()
- 位置: L7762-7787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClipboardHelper.copyString()`, `this.isCommandEnabled()`, `urlbar._getSelectedValueForClipboard()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.value.substring()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.setSelectionRange()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.dispatchEvent()`
- 参照: `this.urlbar`, `urlbar.inputField.value`, `urlbar.selectionEnd`, `urlbar.selectionStart`, `urlbar.window`

## CopyCutController.supportsCommand()
- 位置: L7795-7802
- 役割: (未記入)
- 触るとき: (未記入)

## CopyCutController.isCommandEnabled()
- 位置: L7810-7816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.supportsCommand()`
- 参照: `this.urlbar.readOnly`, `this.urlbar.selectionEnd`, `this.urlbar.selectionStart`

## CopyCutController.onEvent()
- 位置: L7818-7818
- 役割: (未記入)
- 触るとき: (未記入)

## AddSearchEngineHelper.constructor()
- 位置: L7843-7846
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `input.view.oneOffSearchButtons`, `this.input`, `this.shortcutButtons`

## AddSearchEngineHelper.maxInlineEngines()
- 位置: L7854-7856
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.shortcutButtons._maxInlineAddEngines`

## AddSearchEngineHelper.setEnginesFromBrowser()
- 位置: L7864-7872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engines.slice()`, `this._sameEngines()`
- 条件付き依存: `if (!this._sameEngines(this.engines, engines))` → `this.shortcutButtons?.updateWebEngines()`
- 参照: `browser.browsingContext`, `this.browsingContext`, `this.engines`

## AddSearchEngineHelper._sameEngines()
- 位置: L7874-7882
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.deepEqual()`, `engines1.map()`, `engines2.map()`
- 参照: `e.title`, `engines1?.length`, `engines2?.length`

## AddSearchEngineHelper._createMenuitem()
- 位置: L7884-7901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `doc.l10n.setAttributes()`, `elt.addEventListener()`, `elt.classList.add()`, `elt.setAttribute()`, `this._onCommand.bind()`
- 条件付き依存: `if (engine.icon)` → `elt.setAttribute()`
- 条件付き依存: `if (!(engine.icon))` → `elt.removeAttribute()`
- 参照: `engine.icon`, `engine.title`, `engine.uri`, `this.input.ownerDocument`

## AddSearchEngineHelper._createMenu()
- 位置: L7903-7916
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.createXULElement()`, `doc.l10n.setAttributes()`, `elt.appendChild()`, `elt.classList.add()`, `elt.setAttribute()`
- 条件付き依存: `if (engine.icon)` → `elt.setAttribute()`
- 条件付き依存: `if (engine.icon)` → `ChromeUtils.encodeURIForSrcset()`
- 参照: `engine.icon`, `this.input.ownerDocument`

## AddSearchEngineHelper.createContextSeparator()
- 位置: L7933-7940
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextSeparator.classList.add()`, `this.contextSeparator.setAttribute()`, `this.input.ownerDocument.createXULElement()`
- 参照: `this.contextSeparator`, `this.contextSeparator.collapsed`

## AddSearchEngineHelper.refreshContextMenu()
- 位置: L7948-7985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elt.remove()`, `this._createMenuitem()`
- 条件付き依存: `if (engines.length > this.maxInlineEngines)` → `this._createMenu()`
- 条件付き依存: `if (engines.length > this.maxInlineEngines)` → `this.contextSeparator.insertAdjacentElement()`
- 条件付き依存: `if (engines.length > this.maxInlineEngines)` → `this.#contextItems.push()`
- 条件付き依存: `if (curElt.localName == "menupopup")` → `curElt.appendChild()`
- 条件付き依存: `if (!(curElt.localName == "menupopup"))` → `curElt.insertAdjacentElement()`
- 条件付き依存: `if (!(curElt.localName == "menupopup"))` → `this.#contextItems.push()`
- 参照: `curElt.localName`, `elt.lastElementChild`, `engines.length`, `this.#contextItems`, `this.contextSeparator`, `this.contextSeparator.collapsed`, `this.engines`, `this.maxInlineEngines`

## AddSearchEngineHelper._onCommand()
- 位置: async L7987-7998
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `lazy.SearchUIUtils.addOpenSearchEngine()`
- 条件付き依存: `if (added)` → `this.refreshContextMenu()`
- 参照: `console.error`, `this.browsingContext`
