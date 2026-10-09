# browser/components/customizableui/PanelMultiView.sys.mjs

source: browser/components/customizableui/PanelMultiView.sys.mjs
source-hash: 122165dba992614f41a7fdafe23dd74a74e0ed8c
lines: 2200

## <module>
- 役割: <panelmultiview> と <panelview> を管理し、パネル表示、サブビューの遷移、キーボードとタブによる項目移動を担う。
- 呼び出し先: `Cc["@mozilla.org/inspector/deep-tree-walker;1"].createInstance()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `Services.strings.createBundle()`

## constructor()
- 位置: L43-62
- 役割: ルート要素の文書とツリー走査用の inDeepTreeWalker を初期化し、要素だけを対象に走査するよう設定する。
- 触るとき: パネル内の走査範囲や、シャドウ DOM を含めるかの条件を変えるとき。
- 呼び出し先: `Cu.isDeadWrapper()`, `this.#walker.init()`
- 参照: `node.documentGlobal`, `node.documentGlobal.location`, `this.#onlyWantElements`, `this.#showAnonymousContent`, `this.#walker.showAnonymousContent`, `this.#walker.showDocumentsAsNodes`, `this.#walker.showSubDocuments`, `this.filter`

## currentNode()
- 位置: L64-66
- 役割: 走査器が現在指しているノードを返す。
- 触るとき: 走査の現在位置を参照する処理を変えるとき。
- 参照: `this.#walker.currentNode`

## currentNode()
- 位置: L68-70
- 役割: 現在位置を設定する。null なら走査器のルートに戻す。
- 触るとき: フォーカス移動の開始位置を指定する箇所を変えるとき。
- 参照: `this.#walker.currentNode`, `this.#walker.root`

## parentNode()
- 位置: L72-74
- 役割: 走査器の現在位置の親ノードへ移動する。
- 触るとき: キーボード移動で親要素へ戻る処理を調べるとき。
- 呼び出し先: `this.#walker.parentNode()`

## root()
- 位置: L76-78
- 役割: 走査器のルートノードを返す。
- 触るとき: 走査の起点や終点の判定を変えるとき。
- 参照: `this.#walker.root`

## previousNode()
- 位置: L80-82
- 役割: 1つ前の、フィルタを通過する要素を返す（シャドウ DOM のホストを優先する）。
- 触るとき: 上方向のフォーカス移動の挙動を変えるとき。
- 呼び出し先: `this.#previousGoodNodeInRoot()`

## nextNode()
- 位置: L84-86
- 役割: 1つ後の、フィルタを通過する要素を返す。
- 触るとき: 下方向または Tab のフォーカス移動の挙動を変えるとき。
- 呼び出し先: `this.#nextGoodNodeInRoot()`

## #getLastPreOrderDepthFirstNodeIn()
- 位置: L88-94
- 役割: 与えたノードの子孫のうち、前順で最後のノードを返す。
- 触るとき: 最後の子を求める処理（lastChild）を変えるとき。
- 参照: `last.lastChild`, `last?.lastChild`

## previousSibling()
- 位置: L96-102
- 役割: 前の兄弟のうち、スキップ対象でないものを返す。
- 触るとき: 兄弟要素をたどる移動を変えるとき。
- 呼び出し先: `this.#walker.previousSibling()`, `this.isSkippedNode()`

## #previousGoodNodeInRoot()
- 位置: L104-125
- 役割: 前の対象ノードを探す。シャドウ DOM に入った場合はホストを返し、スキップ対象は読み飛ばす。
- 触るとき: シャドウ DOM を含むパネルで上移動が二重にフォーカスする問題を調べるとき。
- 呼び出し先: `previousNode?.getRootNode()`, `this.#walker.previousNode()`, `this.isSkippedNode()`
- 参照: `previousNode?.getRootNode()?.host`, `this.#walker`, `this.#walker.currentNode`

## #nextGoodNodeInRoot()
- 位置: L127-156
- 役割: 次の対象ノードを探す。対象が Web コンポーネントなら、その内部のシャドウ DOM を一時的に降りないようにする。
- 触るとき: moz-button などの内部要素に二重にフォーカスが当たる問題を調べるとき。
- 呼び出し先: `this.#walker.nextNode()`, `this.isSkippedNode()`
- 参照: `currentNode.shadowRoot`, `this.#showAnonymousContent`, `this.#walker`, `this.#walker.showAnonymousContent`

## firstChild()
- 位置: L158-167
- 役割: ルートの最初の対象ノードを返す（ルート自身がスキップ対象なら次の対象へ進む）。
- 触るとき: パネルの最初にフォーカスすべき要素の決め方を変えるとき。
- 呼び出し先: `this.#nextGoodNodeInRoot()`, `this.isSkippedNode()`
- 参照: `this.#walker.currentNode`, `this.#walker.root`

## lastChild()
- 位置: L169-181
- 役割: ルート配下の最後の対象ノードを返す。
- 触るとき: End キーで最後の項目へ移る動作を変えるとき。
- 呼び出し先: `this.#getLastPreOrderDepthFirstNodeIn()`, `this.#previousGoodNodeInRoot()`, `this.isSkippedNode()`
- 参照: `this.#walker.currentNode`, `this.#walker.root`

## isSkippedNode()
- 位置: L183-188
- 役割: 要素でない、または filter が ACCEPT を返さないノードを true とする。
- 触るとき: どの要素を移動の対象にするかの条件を変えるとき。
- 呼び出し先: `this.filter()`
- 参照: `Node.ELEMENT_NODE`, `NodeFilter.FILTER_ACCEPT`, `node.nodeType`, `this.#onlyWantElements`

## constructor()
- 位置: L213-224
- 役割: 関連付けられたノードを保持し、ブロッカーの処理を待つ Promise を初期化する。
- 触るとき: ノードとオブジェクトの対応や、非同期イベントの待ち合わせを変えるとき。
- 呼び出し先: `Promise.resolve()`
- 参照: `this._blockersPromise`, `this.node`

## forNode()
- 位置: L235-242
- 役割: ノードに対応するインスタンスを WeakMap から取得し、無ければ作って登録する。
- 触るとき: パネル要素から対応する PanelMultiView や PanelView を引く経路を変えるとき。
- 呼び出し先: `gNodeToObjectMap.get()`
- 条件付き依存: `if (!associatedToNode)` → `gNodeToObjectMap.set()`

## document()
- 位置: L249-251
- 役割: 関連ノードの所有ドキュメントを返す。
- 触るとき: ドキュメント参照を使う処理の前提を確かめるとき。
- 参照: `this.node.ownerDocument`

## window()
- 位置: L258-260
- 役割: 関連ノードが属する window global を返す。
- 触るとき: ウィンドウ単位の API を呼ぶ箇所を変えるとき。
- 参照: `this.node.documentGlobal`

## _getBoundsWithoutFlushing()
- 位置: L274-276
- 役割: レイアウトを強制せず、要素の矩形を取得する。
- 触るとき: サイズ測定時の reflow 負荷を抑える箇所を変えるとき。
- 呼び出し先: `this.window.windowUtils.getBoundsWithoutFlushing()`

## dispatchCustomEvent()
- 位置: L290-298
- 役割: 指定名のカスタムイベントを bubbles 付きで発火し、preventDefault されたかを返す。
- 触るとき: パネルの独自イベント（ViewShown など）の送出を変えるとき。
- 呼び出し先: `this.node.dispatchEvent()`
- 参照: `event.defaultPrevented`, `this.window.CustomEvent`

## dispatchAsyncEvent()
- 位置: async L326-365
- 役割: 前の処理の完了を待ってからイベントを発火し、addBlocker で登録された Promise をすべて待つ。false が返されたか preventDefault されたときにキャンセル扱いにする。タイムアウト（BLOCKERS_TIMEOUT_MS）でもキャンセルする。
- 触るとき: ViewShowing の処理を遅らせたり、キャンセルさせたりする仕組みを変えるとき。
- 呼び出し先: `blockersPromise.then()`, `this._blockersPromise.catch()`, `this.dispatchCustomEvent()`
- 条件付き依存: `if (blockers.size)` → `this.window.setTimeout()`
- 条件付き依存: `if (blockers.size)` → `Promise.race()`
- 条件付き依存: `if (blockers.size)` → `Promise.all()`
- 条件付き依存: `if (blockers.size)` → `results.some()`
- 条件付き依存: `if (blockers.size)` → `console.error()`
- 参照: `blockers.size`, `this._blockersPromise`

## addBlocker()
- 位置: L334-342
- 役割: 渡された Promise を待ち合わせ対象に加える。例外は console に出すが、結果は true として扱われる。
- 触るとき: ブロッカーの例外時の扱い（キャンセルにするか）を変えるとき。
- 呼び出し先: `blockers.add()`, `console.error()`, `promise.catch()`

## openPopup()
- 位置: async L393-400
- 役割: panelmultiview を含むパネルなら、その PanelMultiView 経由で開き、含まなければパネルを直接開く。
- 触るとき: ページアクションなど別種のパネルを同じ API で開くときの分岐を変えるとき。
- 呼び出し先: `panelNode.openPopup()`, `panelNode.querySelector()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode(panelMultiViewNode).openPopup()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode()`

## hidePopup()
- 位置: L417-424
- 役割: panelmultiview を含むパネルなら PanelMultiView 経由で閉じ、そうでなければパネルを直接閉じる。
- 触るとき: パネルを閉じる入口を変えるとき。
- 呼び出し先: `panelNode.querySelector()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode(panelMultiViewNode).hidePopup()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode()`
- 条件付き依存: `if (!(panelMultiViewNode))` → `panelNode.hidePopup()`

## removePopup()
- 位置: L440-452
- 役割: パネルを削除する。先にサブビューを view cache へ戻し、接続を解除してから、失敗しても必ずパネル要素を削除する。
- 触るとき: 一時パネルを消す際にサブビューが失われる問題を調べるとき。
- 呼び出し先: `panelNode.querySelector()`, `panelNode.remove()`
- 条件付き依存: `if (panelMultiViewNode)` → `this.forNode()`
- 条件付き依存: `if (panelMultiViewNode)` → `panelMultiView._moveOutKids()`
- 条件付き依存: `if (panelMultiViewNode)` → `panelMultiView.disconnect()`

## getViewNode()
- 位置: L467-474
- 役割: 文書内、なければ appMenu-viewCache のテンプレートから、指定 ID のビュー要素を探す。
- 触るとき: 遅延読み込みのビューを参照する箇所の探索順を変えるとき。
- 呼び出し先: `doc.getElementById()`, `viewCacheTemplate?.content.querySelector()`

## ensureUnloadHandlerRegistered()
- 位置: L483-501
- 役割: ウィンドウごとに一度だけ、unload 時に全 panelmultiview の接続を解除する登録を行う。
- 触るとき: ウィンドウを閉じたときの後始末漏れを調べるとき。
- 呼び出し先: `gWindowsWithUnloadHandler.add()`, `gWindowsWithUnloadHandler.has()`, `this.forNode()`, `this.forNode(panelMultiViewNode).disconnect()`, `window.addEventListener()`, `window.document.querySelectorAll()`

## #panel()
- 位置: L507-509
- 役割: panelmultiview の親要素（panel）を返す。
- 触るとき: パネル要素への参照経路を変えるとき。
- 参照: `this.node.parentNode`

## #transitioning()
- 位置: L517-523
- 役割: panelmultiview の transitioning 属性を付けたり外したりする setter。
- 触るとき: アニメーション中の状態表示を変えるとき。
- 条件付き依存: `if (val)` → `this.node.setAttribute()`
- 条件付き依存: `if (!(val))` → `this.node.removeAttribute()`

## constructor()
- 位置: L525-528
- 役割: PanelMultiView を初期化し、開く処理の Promise を解決済みにする。
- 触るとき: 開く処理の直列化の初期状態を変えるとき。
- 呼び出し先: `Promise.resolve()`, `super()`
- 参照: `this._openPopupPromise`

## connect()
- 位置: L536-574
- 役割: viewContainer、viewStack、オフスクリーン用の要素を作り、popup イベントを監視し、goBack と showSubView を公開する。
- 触るとき: パネルの内部構造を変えるとき、または接続前後の状態を調べるとき。
- 呼び出し先: `Object.defineProperty()`, `PanelMultiView.ensureUnloadHandlerRegistered()`, `["goBack", "showSubView"].forEach()`, `offscreenViewContainer.append()`, `offscreenViewContainer.classList.add()`, `offscreenViewStack.classList.add()`, `this.#panel.addEventListener()`, `this.document.createXULElement()`, `this.node.prepend()`, `viewContainer.append()`, `viewContainer.classList.add()`, `viewStack.classList.add()`
- 参照: `this._offscreenViewStack`, `this._viewContainer`, `this._viewStack`, `this.connected`, `this.node`, `this.openViews`, `this.window`

## value()
- 位置: L571-571
- 役割: 公開メソッド（goBack, showSubView）を node に付けるための薄いラッパー。
- 触るとき: node に公開するメソッドを増減するとき。
- 呼び出し先: `this[method]()`

## disconnect()
- 位置: L581-599
- 役割: リスナーを外し、参照を null にする。二重呼び出しは無視する。
- 触るとき: パネルを破棄する際の解除漏れを調べるとき。
- 呼び出し先: `this.#panel.removeEventListener()`, `this.document.documentElement.removeEventListener()`
- 参照: `this._openPopupCancelCallback`, `this._openPopupPromise`, `this._transitionDetails`, `this._viewContainer`, `this._viewStack`, `this.connected`, `this.node`

## openPopup()
- 位置: async L642-753
- 役割: メインビューを表示する準備（ViewShowing）を直列に行い、キャンセル可能な形でパネルを開く。既に開いていれば何もしない。
- 触るとき: パネルを開く際の待ち合わせやキャンセルの条件を変えるとき。
- 呼び出し先: `["open", "showing"].includes()`, `cancelCallback()`, `openPopupPromise.then()`, `this.#panel.openPopup()`, `this.#panel.setAttribute()`, `this.#showMainView()`, `this._openPopupPromise.catch()`, `this.dispatchCustomEvent()`
- 条件付き依存: `if (!this.connected)` → `this.connect()`
- 条件付き依存: `if (!(await this.#showMainView()))` → `cancelCallback()`
- 条件付き依存: `if (this.#panel.state == "closed" && this.openViews.length)` → `this.dispatchCustomEvent()`
- 参照: `MouseEvent.MOZ_SOURCE_KEYBOARD`, `options.triggerEvent`, `options.triggerEvent.type`, `options.triggerEvent?.inputSource`, `this.#panel.state`, `this._openPopupCancelCallback`, `this._openPopupPromise`, `this.connected`, `this.node`, `this.openViews`, `this.openViews.length`, `this.openViews[0].focusWhenActive`

## this._openPopupCancelCallback()
- 位置: L649-664
- 役割: 開く処理の途中で閉じられたときに、開かずに popuphidden を発火させて状態を戻す。
- 触るとき: 開く処理と閉じる処理が競合するケースを調べるとき。
- 条件付き依存: `if (canCancel && this.node)` → `this.dispatchCustomEvent()`
- 参照: `this._openPopupCancelCallback`, `this.node`

## hidePopup()
- 位置: L775-794
- 役割: パネルが開いていれば閉じ、開く途中なら開く処理をキャンセルし、すべてのビューを同期的に閉じる。
- 触るとき: 閉じる際のビューの後始末順序を変えるとき。
- 呼び出し先: `["open", "showing"].includes()`, `this.closeAllViews()`
- 条件付き依存: `if (["open", "showing"].includes(this.#panel.state))` → `this.#panel.hidePopup()`
- 条件付き依存: `if (!(["open", "showing"].includes(this.#panel.state)))` → `this._openPopupCancelCallback()`
- 参照: `this.#panel.state`, `this.connected`, `this.node`

## _moveOutKids()
- 位置: L803-817
- 役割: viewCacheId が指定されていれば、サブビューを appMenu-viewCache へ移す。
- 触るとき: パネル削除時にサブビューを残す条件を変えるとき。
- 呼び出し先: `Array.from()`, `this.document.getElementById()`, `this.node?.getAttribute()`, `viewCache.moveBefore()`
- 参照: `this._viewStack.children`

## showSubView()
- 位置: L831-833
- 役割: サブビューの表示を非同期処理へ渡し、失敗はログに出す。
- 触るとき: サブビュー表示の公開 API を変えるとき。
- 呼び出し先: `this.#showSubView()`, `this.#showSubView(viewIdOrNode, anchor).catch()`
- 参照: `console.error`

## #showSubView()
- 位置: async L849-946
- 役割: 現在のビューを非アクティブにし、ViewShowing を経てタイトルと幅・高さを設定し、スライドで次のビューへ移す。
- 触るとき: サブビューの遷移順序、タイトル決め、再入防止を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelView.forNode()`, `anchor?.getAttribute()`, `anchor?.removeAttribute()`, `anchor?.setAttribute()`, `prevPanelView.captureKnownSize()`, `this.#activateView()`, `this.#openView()`, `this.#transitionViews()`, `this.openViews.includes()`, `this.openViews[0].node.getAttribute()`, `viewNode.getAttribute()`
- 条件付き依存: `if (!viewNode)` → `console.error()`
- 条件付き依存: `if (!this.openViews.length)` → `console.error()`
- 条件付き依存: `if (this.openViews.includes(nextPanelView))` → `console.error()`
- 条件付き依存: `if (!(await this.#openView(nextPanelView)))` → `prevPanelView.isOpenIn()`
- 条件付き依存: `if (l10nId)` → `viewNode.getAttribute()`
- 条件付き依存: `if (l10nId)` → `JSON.parse()`
- 条件付き依存: `if (l10nId)` → `viewNode.ownerDocument.l10n.formatMessages()`
- 条件付き依存: `if (l10nId)` → `msg.attributes.find()`
- 条件付き依存: `if (anchor)` → `viewNode.classList.add()`
- 参照: `a.name`, `msg.attributes.find(a => a.name === "title")?.value`, `nextPanelView.focusWhenActive`, `nextPanelView.headerText`, `nextPanelView.mainview`, `nextPanelView.minMaxHeight`, `nextPanelView.minMaxWidth`, `prevPanelView._doingKeyboardActivation`, `prevPanelView.active`, `prevPanelView.knownHeight`, `prevPanelView.knownWidth`, `prevPanelView.node`, `this.document`, `this.openViews`, `this.openViews.length`, `viewNode.id`

## goBack()
- 位置: L951-953
- 役割: 戻る操作を非同期処理へ渡す。
- 触るとき: 戻る操作の公開 API を変えるとき。
- 呼び出し先: `this.#goBack()`, `this.#goBack().catch()`
- 参照: `console.error`

## #goBack()
- 位置: async L962-986
- 役割: 2つ以上ビューが開いているときに、最後のビューを逆向きに滑らせて閉じ、前のビューを有効にする。
- 触るとき: 戻る遷移の順序や条件を変えるとき。
- 呼び出し先: `prevPanelView.captureKnownSize()`, `this.#activateView()`, `this.#closeLatestView()`, `this.#transitionViews()`
- 参照: `nextPanelView.node`, `prevPanelView.active`, `prevPanelView.node`, `this.openViews`, `this.openViews.length`

## #showMainView()
- 位置: async L994-1027
- 役割: メインビューを別のパネルが持っていれば先に閉じ、ViewShowing を経てメインビューとして表示する状態にする。
- 触るとき: パネルを開く際のメインビューの準備順序を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelView.forNode()`, `this.#openView()`, `this.node.getAttribute()`
- 条件付き依存: `if (oldPanelMultiViewNode)` → `PanelMultiView.forNode(oldPanelMultiViewNode).hidePopup()`
- 条件付き依存: `if (oldPanelMultiViewNode)` → `PanelMultiView.forNode()`
- 条件付き依存: `if (oldPanelMultiViewNode)` → `this.window.promiseDocumentFlushed()`
- 参照: `nextPanelView.headerText`, `nextPanelView.mainview`, `nextPanelView.minMaxHeight`, `nextPanelView.minMaxWidth`, `nextPanelView.node.panelMultiView`, `nextPanelView.visible`, `this.document`

## #openView()
- 位置: async L1041-1083
- 役割: ビューをビュースタックに入れ、ViewShowing を発火する。キャンセルされたら閉じ、成功すれば遷移用の style を消す。
- 触るとき: ViewShowing によるキャンセルの扱いを変えるとき。
- 呼び出し先: `panelView.dispatchAsyncEvent()`, `panelView.node.hasAttribute()`, `style.removeProperty()`, `this.#panel.toggleAttribute()`, `this.openViews.push()`
- 条件付き依存: `if (panelView.node.parentNode != this._viewStack)` → `this._viewStack.appendChild()`
- 条件付き依存: `if (canceled)` → `this.#closeLatestView()`
- 参照: `panelView.node`, `panelView.node.panelMultiView`, `panelView.node.parentNode`, `this._viewStack`, `this.node`, `this.openViews.length`

## #activateView()
- 位置: L1092-1101
- 役割: ビューが自分の PanelMultiView にまだ開いていれば、有効化し、必要ならフォーカスして ViewShown を発火する。
- 触るとき: ビューの有効化タイミングや初回フォーカスを変えるとき。
- 呼び出し先: `panelView.isOpenIn()`
- 条件付き依存: `if (panelView.focusWhenActive)` → `panelView.focusFirstNavigableElement()`
- 条件付き依存: `if (panelView.isOpenIn(this))` → `panelView.dispatchCustomEvent()`
- 参照: `panelView.active`, `panelView.focusWhenActive`

## #closeLatestView()
- 位置: L1110-1119
- 役割: 最後に開いたビューを外し、キーボード移動を解除して ViewHiding を発火し、非表示にする。
- 触るとき: ビューを閉じる際の後始末を変えるとき。
- 呼び出し先: `panelView.clearNavigation()`, `panelView.dispatchCustomEvent()`, `this.openViews.pop()`
- 参照: `panelView.node.panelMultiView`, `panelView.visible`

## closeAllViews()
- 位置: L1124-1129
- 役割: 開いているすべてのビューを後ろから順に閉じる。
- 触るとき: パネルを閉じる際の全ビューの後始末を調べるとき。
- 呼び出し先: `this.#closeLatestView()`
- 参照: `this.openViews.length`

## #transitionViews()
- 位置: async L1148-1341
- 役割: 前のビューと次のビューの寸法を固定し、transform を使ってスライド遷移させ、終わったら後始末してフォーカスを戻す。reduced motion では遷移を省く。
- 触るとき: サブビューのアニメーションや寸法計算を変えるとき。
- 呼び出し先: `PanelView.forNode()`, `deepestNode.style.removeProperty()`, `nextPanelView.focusSelectedElement()`, `nextPanelView.isOpenIn()`, `nextPanelView.node.style.removeProperty()`, `this.#cleanupTransitionPhase()`, `this.#panel.style.removeProperty()`, `this._getBoundsWithoutFlushing()`, `this.window.matchMedia()`, `this.window.promiseDocumentFlushed()`, `viewNode.getAttribute()`, `window.promiseDocumentFlushed()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `Object.assign()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `viewNode.customRectGetter()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `header.classList.contains()`
- 条件付き依存: `if (header && header.classList.contains("panel-header"))` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (header && header.classList.contains("panel-header"))` → `this._getBoundsWithoutFlushing()`
- 条件付き依存: `if (viewNode.customRectGetter)` → `nextPanelView.isOpenIn()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._offscreenViewStack.appendChild()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `window.promiseDocumentFlushed()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._getBoundsWithoutFlushing()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `nextPanelView.isOpenIn()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._viewStack.appendChild()`
- 条件付き依存: `if (!(viewNode.customRectGetter))` → `this._offscreenViewStack.style.removeProperty()`
- 条件付き依存: `if (viewNode.getAttribute("mainview"))` → `this._viewContainer.style.removeProperty()`
- 条件付き依存: `if (viewNode.getAttribute("mainview"))` → `this.#panel.setAttribute()`
- 条件付き依存: `if (!(viewNode.getAttribute("mainview")))` → `this.#panel.removeAttribute()`
- 条件付き依存: `if ( this.window.matchMedia("(prefers-reduced-motion: no-preference)") .matches && !viewNode.getAttribute("no-panelview-transition") )` → `this._viewContainer.addEventListener()`
- 参照: `TRANSITION_PHASES.PREPARE`, `TRANSITION_PHASES.START`, `TRANSITION_PHASES.TRANSITION`, `deepestNode.style.outline`, `details.cancelListener`, `details.listener`, `details.phase`, `details.resolve`, `nextPanelView.knownHeight`, `nextPanelView.knownWidth`, `nextPanelView.visible`, `olderView.knownHeight`, `prevPanelView.knownHeight`, `prevPanelView.knownWidth`, `prevPanelView.visible`, `rect.height`, `rect.width`, `this.#panel`, `this.#panel.style.height`, `this.#panel.style.width`, `this.#transitioning`, `this._getBoundsWithoutFlushing(header).height`, `this._offscreenViewStack.style.minHeight`, `this._transitionDetails`, `this._viewContainer.style.height`, `this._viewContainer.style.minHeight`, `this._viewContainer.style.width`, `this._viewStack.style.marginInlineStart`, `this._viewStack.style.transform`, `this._viewStack.style.transition`, `this._viewStack.style.willChange`, `this.window.RTL_UI`, `this.window.matchMedia("(prefers-reduced-motion: no-preference)") .matches`, `viewNode.customRectGetter`, `viewNode.firstElementChild`, `viewNode.style.width`, `viewRect.height`, `viewRect.width`

## details.listener()
- 位置: L1290-1306
- 役割: スライドの transitionend を受けて、遷移の完了を通知する。
- 触るとき: 遷移の終了判定を変えるとき。
- 呼び出し先: `resolve()`, `this._viewContainer.removeEventListener()`
- 参照: `details.listener`, `ev.propertyName`, `ev.target`, `this._viewStack`

## details.cancelListener()
- 位置: L1310-1320
- 役割: スライドの transitioncancel を受けて、遷移を完了扱いにする。
- 触るとき: 遷移が中断された場合の後始末を変えるとき。
- 呼び出し先: `resolve()`, `this._viewContainer.removeEventListener()`
- 参照: `details.cancelListener`, `ev.target`, `this._viewStack`

## #cleanupTransitionPhase()
- 位置: L1348-1382
- 役割: 遷移がどの段階まで進んだかに応じて、設定した属性・style・リスナーを取り除く。
- 触るとき: 遷移途中で閉じられた場合に style が残る問題を調べるとき。
- 条件付き依存: `if (phase >= TRANSITION_PHASES.START)` → `this.#panel.removeAttribute()`
- 条件付き依存: `if (phase >= TRANSITION_PHASES.START)` → `this._viewContainer.style.removeProperty()`
- 条件付き依存: `if (phase >= TRANSITION_PHASES.PREPARE)` → `this._viewStack.style.removeProperty()`
- 条件付き依存: `if (phase >= TRANSITION_PHASES.TRANSITION)` → `this._viewStack.style.removeProperty()`
- 条件付き依存: `if (listener)` → `this._viewContainer.removeEventListener()`
- 条件付き依存: `if (cancelListener)` → `this._viewContainer.removeEventListener()`
- 条件付き依存: `if (resolve)` → `resolve()`
- 参照: `TRANSITION_PHASES.PREPARE`, `TRANSITION_PHASES.START`, `TRANSITION_PHASES.TRANSITION`, `this.#transitioning`, `this._transitionDetails`

## handleEvent()
- 位置: L1390-1467
- 役割: keydown、mousemove、popupshowing、popupshown、popuphidden を処理し、キー操作、ハイライト解除、初期化と後始末を行う。
- 触るとき: パネルのイベント処理の流れを変えるとき。
- 呼び出し先: `aEvent.type.startsWith()`, `currentView.keyNavigation()`, `this.#activateView()`, `this.#cleanupTransitionPhase()`, `this.#panel.removeEventListener()`, `this._viewContainer.removeAttribute()`, `this._viewContainer.setAttribute()`, `this._viewContainer.style.removeProperty()`, `this._viewStack.style.removeProperty()`, `this.closeAllViews()`, `this.dispatchCustomEvent()`, `this.document.documentElement.removeEventListener()`, `this.node.hasAttribute()`, `this.openViews.forEach()`
- 条件付き依存: `if (!panelView.ignoreMouseMove)` → `panelView.clearNavigation()`
- 条件付き依存: `if (!this.node.hasAttribute("disablekeynav"))` → `this.document.documentElement.addEventListener()`
- 条件付き依存: `if (!this.node.hasAttribute("disablekeynav"))` → `this.#panel.addEventListener()`
- 参照: `aEvent.target`, `aEvent.type`, `panelView.ignoreMouseMove`, `this.#panel`, `this.#transitioning`, `this.node`, `this.openViews`, `this.openViews.length`

## constructor()
- 位置: L1474-1501
- 役割: PanelView の状態（active, focusWhenActive）を初期化し、unload で走査器の参照を解放する。
- 触るとき: パネルビューの初期状態や解放処理を変えるとき。
- 呼び出し先: `super()`, `this.window.addEventListener()`
- 参照: `this.#_arrowNavigableWalker`, `this.#_tabNavigableWalker`, `this.active`, `this.focusWhenActive`

## isOpenIn()
- 位置: L1511-1513
- 役割: このビューが指定の PanelMultiView に開いているかを返す。
- 触るとき: ビューの所属判定を使う箇所を変えるとき。
- 参照: `panelMultiView.node`, `this.node.panelMultiView`

## mainview()
- 位置: L1525-1531
- 役割: mainview 属性を付けたり外したりする setter。
- 触るとき: 同じビューをメインビューとサブビューで使い分ける処理を変えるとき。
- 条件付き依存: `if (value)` → `this.node.setAttribute()`
- 条件付き依存: `if (!(value))` → `this.node.removeAttribute()`

## visible()
- 位置: L1541-1549
- 役割: visible 属性を設定し、false のときは active と focusWhenActive も戻す。
- 触るとき: ビューの表示状態と操作可能状態の連動を変えるとき。
- 条件付き依存: `if (value)` → `this.node.setAttribute()`
- 条件付き依存: `if (!(value))` → `this.node.removeAttribute()`
- 参照: `this.active`, `this.focusWhenActive`

## minMaxWidth()
- 位置: L1558-1566
- 役割: min-width と max-width を設定する。0 なら制約を外す。
- 触るとき: サブビューの幅の固定方法を変えるとき。
- 条件付き依存: `if (!(value))` → `style.removeProperty()`
- 参照: `style.maxWidth`, `style.minWidth`, `this.node.style`

## minMaxHeight()
- 位置: L1575-1583
- 役割: min-height と max-height を設定する。0 なら制約を外す。
- 触るとき: サブビューの高さの固定方法を変えるとき。
- 条件付き依存: `if (!(value))` → `style.removeProperty()`
- 参照: `style.maxHeight`, `style.minHeight`, `this.node.style`

## headerText()
- 位置: L1600-1674
- 役割: パネルのヘッダー（戻るボタンとタイトル、区切り線）を作る、更新する、消すを行う。メインビューには戻るボタンを付けない。
- 触るとき: ヘッダーのタイトルや戻るボタンの有無を変えるとき。
- 呼び出し先: `ensureHeaderSeparator()`, `h1.appendChild()`, `header.append()`, `header.classList.add()`, `this.document.createElement()`, `this.document.createXULElement()`, `this.node.getAttribute()`, `this.node.prepend()`, `this.node.querySelector()`
- 条件付き依存: `if (header)` → `header.querySelector()`
- 条件付き依存: `if (headerBackButton)` → `headerBackButton.remove()`
- 条件付き依存: `if (value)` → `this.node.getAttribute()`
- 条件付き依存: `if ( !isMainView && !headerBackButton && !this.node.getAttribute("no-back-button") )` → `header.prepend()`
- 条件付き依存: `if ( !isMainView && !headerBackButton && !this.node.getAttribute("no-back-button") )` → `this.createHeaderBackButton()`
- 条件付き依存: `if (value)` → `header.querySelector()`
- 条件付き依存: `if (value)` → `ensureHeaderSeparator()`
- 条件付き依存: `if (!(value))` → `this.node.getAttribute()`
- 条件付き依存: `if (header.nextSibling.tagName == "toolbarseparator")` → `header.nextSibling.remove()`
- 条件付き依存: `if ( !this.node.getAttribute("has-custom-header") && !this.node.getAttribute("mainview-with-header") )` → `header.remove()`
- 条件付き依存: `if (!isMainView)` → `this.createHeaderBackButton()`
- 条件付き依存: `if (!isMainView)` → `header.append()`
- 参照: `header.nextSibling.tagName`, `header.querySelector(".panel-header > h1 > span").textContent`, `span.textContent`

## ensureHeaderSeparator()
- 位置: L1601-1606
- 役割: ヘッダーの直後に区切り線が無ければ挿入する。
- 触るとき: ヘッダー直後の区切り線の扱いを変えるとき。
- 条件付き依存: `if (headerNode.nextSibling.tagName != "toolbarseparator")` → `this.document.createXULElement()`
- 条件付き依存: `if (headerNode.nextSibling.tagName != "toolbarseparator")` → `this.node.insertBefore()`
- 参照: `headerNode.nextSibling`, `headerNode.nextSibling.tagName`

## createHeaderBackButton()
- 位置: L1679-1695
- 役割: 戻るボタン（subviewbutton-back）を作り、押されたら goBack を呼ぶ。
- 触るとき: 戻るボタンの見た目やラベルを変えるとき。
- 呼び出し先: `backButton.addEventListener()`, `backButton.blur()`, `backButton.setAttribute()`, `lazy.gBundle.GetStringFromName()`, `this.document.createXULElement()`, `this.node.panelMultiView.goBack()`
- 参照: `backButton.className`

## dispatchCustomEvent()
- 位置: L1706-1709
- 役割: CustomizableUI のサブビュー用リスナーを用意してから、カスタムイベントを発火する。
- 触るとき: サブビューのイベントを CustomizableUI と結びつける仕組みを変えるとき。
- 呼び出し先: `lazy.CustomizableUI.ensureSubviewListeners()`, `super.dispatchCustomEvent()`
- 参照: `this.node`

## captureKnownSize()
- 位置: L1718-1722
- 役割: ビューの現在の幅と高さを knownWidth と knownHeight に保存する。
- 触るとき: 遷移中の寸法の基準を変えるとき。
- 呼び出し先: `this._getBoundsWithoutFlushing()`
- 参照: `rect.height`, `rect.width`, `this.knownHeight`, `this.knownWidth`, `this.node`

## #isNavigableWithTabOnly()
- 位置: L1733-1749
- 役割: select、input などの Tab でしか移動しない要素かを判定する。data-navigable-with-tab-only 指定も見る。
- 触るとき: 矢印キーで移動させない要素を増やすとき。
- 参照: `element.dataset?.navigableWithTabOnly`, `element.localName`

## #makeNavigableTreeWalker()
- 位置: L1759-1816
- 役割: キー移動の対象を選ぶ走査器を作る。無効・非表示・寸法ゼロは除き、ボタン類には tabindex を付けて対象にする。
- 触るとき: どの要素がキーボードで移動できるかを変えるとき。
- 参照: `this.node`

## filter()
- 位置: L1760-1812
- 役割: 走査器の判定関数。無効、非表示、寸法ゼロを除き、矢印キーでは Tab 専用要素を除く。
- 触るとき: キーボードフォーカスの対象判定を変えるとき。
- 呼び出し先: `node.checkVisibility()`, `node.classList.contains()`, `node.localName.toLowerCase()`, `this.#isNavigableWithTabOnly()`, `this._getBoundsWithoutFlushing()`
- 条件付き依存: `if ( localName == "button" || localName == "toolbarbutton" || localName == "checkbox" || localName == "a" || localName == "moz-button" || localName == "moz-box-b...)` → `node.hasAttribute()`
- 条件付き依存: `if ( localName != "browser" && localName != "iframe" && localName != "input" && !node.hasAttribute("tabindex") && node.dataset?.capturesFocus !== "true" )` → `node.setAttribute()`
- 参照: `NodeFilter.FILTER_ACCEPT`, `NodeFilter.FILTER_REJECT`, `NodeFilter.FILTER_SKIP`, `bounds.height`, `bounds.width`, `node.dataset?.capturesFocus`, `node.disabled`

## _tabNavigableWalker()
- 位置: L1828-1833
- 役割: Tab と Shift+Tab で移動する要素の走査器を遅延生成して返す。
- 触るとき: Tab 移動の対象を変えるとき。AccessibilityUtils からも参照される。
- 条件付き依存: `if (!this.#_tabNavigableWalker)` → `this.#makeNavigableTreeWalker()`
- 参照: `this.#_tabNavigableWalker`

## #arrowNavigableWalker()
- 位置: L1842-1847
- 役割: 上下矢印キーで移動する要素の走査器を遅延生成して返す。
- 触るとき: 矢印キーの移動対象を変えるとき。
- 条件付き依存: `if (!this.#_arrowNavigableWalker)` → `this.#makeNavigableTreeWalker()`
- 参照: `this.#_arrowNavigableWalker`

## selectedElement()
- 位置: L1857-1859
- 役割: キーボードで選ばれている要素を弱参照から取り出して返す。
- 触るとき: 選択中の要素を参照する箇所を調べるとき。
- 呼び出し先: `this._selectedElement.get()`
- 参照: `this._selectedElement`

## selectedElement()
- 位置: L1861-1867
- 役割: 選択要素を弱参照で保存する。null なら参照を消す。
- 触るとき: 選択要素の保持方法を変えるとき。
- 条件付き依存: `if (!(!value))` → `Cu.getWeakReference()`
- 参照: `this._selectedElement`

## focusFirstNavigableElement()
- 位置: L1878-1894
- 役割: 最初の移動可能な要素を選んでフォーカスする。Home キーなら矢印用の走査器を使い、スキップ指定の戻るボタンは飛ばせる。
- 触るとき: パネルを開いた直後の初期フォーカスや Home キーの挙動を変えるとき。
- 呼び出し先: `this.focusSelectedElement()`, `walker.currentNode.classList.contains()`, `walker.firstChild()`, `walker.nextNode()`
- 参照: `this.#arrowNavigableWalker`, `this._tabNavigableWalker`, `this.selectedElement`, `walker.currentNode`, `walker.root`

## focusLastNavigableElement()
- 位置: L1903-1909
- 役割: 最後の移動可能な要素を選んでフォーカスする。End キーなら矢印用の走査器を使う。
- 触るとき: End キーの挙動を変えるとき。
- 呼び出し先: `this.focusSelectedElement()`, `walker.lastChild()`
- 参照: `this.#arrowNavigableWalker`, `this._tabNavigableWalker`, `this.selectedElement`, `walker.currentNode`, `walker.root`

## moveSelection()
- 位置: L1920-1959
- 役割: 現在の選択（なければ activeElement）から前後の移動可能な要素を選び、無ければ先頭か末尾に回す。
- 触るとき: 上下移動や Tab での選択の決まり方を変えるとき。
- 条件付き依存: `if (!oldSel)` → `this.node.compareDocumentPosition()`
- 条件付き依存: `if (oldSel)` → `walker.nextNode()`
- 条件付き依存: `if (oldSel)` → `walker.previousNode()`
- 条件付き依存: `if (!newSel)` → `walker.firstChild()`
- 条件付き依存: `if (!newSel)` → `walker.lastChild()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `oldSel.shadowRoot.activeElement`, `oldSel?.shadowRoot?.activeElement`, `this.#arrowNavigableWalker`, `this._tabNavigableWalker`, `this.document.activeElement`, `this.selectedElement`, `walker.currentNode`, `walker.root`

## keyNavigation()
- 位置: L1980-2172
- 役割: 矢印キー、Tab、Home、End、Enter、左右キーを解釈する。埋め込み文書や状態によっては処理をしない。選択中の要素は mousedown、mouseup、click を発火して押下を再現する。
- 触るとき: パネル内のキーボード操作を変えるとき、またはキーが効かない条件を調べるとき。
- 呼び出し先: `button.classList.contains()`, `button.focus()`, `isContextMenuOpen()`, `stop()`, `tabOnly()`, `target.dispatchEvent()`, `this.focusFirstNavigableElement()`, `this.focusLastNavigableElement()`, `this.moveSelection()`, `this.node.compareDocumentPosition()`
- 条件付き依存: `if ( (!this.window.RTL_UI && keyCode == "ArrowLeft") || (this.window.RTL_UI && keyCode == "ArrowRight") )` → `this.node.panelMultiView.goBack()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `button.buttonEl`, `button.localName`, `button?.localName`, `details.composed`, `event.altKey`, `event.code`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `event.target.documentGlobal.MouseEvent`, `event.target.documentGlobal.PointerEvent`, `focus.dataset?.capturesFocus`, `focus.localName`, `focus.open`, `focus.shadowRoot.activeElement`, `focus.tagName`, `focus?.shadowRoot?.activeElement`, `this._doingKeyboardActivation`, `this.active`, `this.document.activeElement`, `this.ignoreMouseMove`, `this.selectedElement`, `this.window.RTL_UI`

## stop()
- 位置: L2018-2021
- 役割: キーイベントの伝播と既定動作を止める。
- 触るとき: キーイベントを他に渡さない条件を変えるとき。
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`

## tabOnly()
- 位置: L2027-2032
- 役割: 実際のフォーカス要素が Tab 専用かを判定する。
- 触るとき: 矢印キーをフォーカス先に任せる条件を変えるとき。
- 呼び出し先: `this.#isNavigableWithTabOnly()`

## isContextMenuOpen()
- 位置: L2038-2052
- 役割: フォーカス要素の context 属性が指すポップアップが開いているかを返す。
- 触るとき: コンテキストメニューが開いているときにキーを奪わないよう判定を変えるとき。
- 呼び出し先: `contextNode.getAttribute()`, `focus.closest()`, `this.document.getElementById()`
- 参照: `popup.state`

## focusSelectedElement()
- 位置: L2181-2187
- 役割: 選択中の要素があればフォーカスする。byKey なら FLAG_BYKEY を付けてキー操作としてフォーカスを移す。
- 触るとき: キー操作によるフォーカスの見た目（フォーカス表示）を変えるとき。
- 条件付き依存: `if (selected)` → `Services.focus.setFocus()`
- 参照: `Services.focus.FLAG_BYKEY`, `this.selectedElement`
- XPCOM: `Services.focus`

## clearNavigation()
- 位置: L2192-2198
- 役割: 選択中の要素からフォーカスを外し、選択をクリアする。
- 触るとき: マウス移動などでキーボード選択を解除する処理を変えるとき。
- 条件付き依存: `if (selected)` → `selected.blur()`
- 参照: `this.selectedElement`
