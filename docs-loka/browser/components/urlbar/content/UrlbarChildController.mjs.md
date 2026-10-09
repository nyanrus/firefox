# browser/components/urlbar/content/UrlbarChildController.mjs

source: browser/components/urlbar/content/UrlbarChildController.mjs
source-hash: a04f963921743cf011a84c7c298cdbe02ece57a3
lines: 889

## <module>
- 役割: urlbar の content 側コントローラーで、ビューやイベントバッファーへの通知の配信、キー操作、クエリ開始を担い、親側の UrlbarParentController への転送を行う。

## UrlbarChildController.logger()
- 位置: L53-60
- 役割: ChildController 用のロガーを一度だけ作って返す。
- 触るとき: ChildController のデバッグログを追加するとき。
- 条件付き依存: `if (!UrlbarChildController.#logger)` → `UrlbarShared.getLogger()`
- 参照: `UrlbarChildController.#logger`

## UrlbarChildController.constructor()
- 位置: L105-121
- 役割: input から親コントローラーを生成し(メッセージ経路なら代理、直接なら本体)、自分を setChild で登録する。検索エンジンストアも作る。
- 触るとき: urlbar 生成時に親との接続経路が正しく選ばれるか確認するとき。
- 呼び出し先: `UrlbarContentUtils.usesMessagePath()`, `options.input.window.windowGlobalChild.getActor()`, `this.#parentController.setChild()`
- 参照: `lazy.UrlbarParentController`, `options.input`, `options.input.isPrivate`, `options.input.sapName`, `this.#input`, `this.#parentController`, `this.engineStore`

## UrlbarChildController.input()
- 位置: L123-125
- 役割: このコントローラーが紐づく input を返す。
- 触るとき: コントローラーから入力欄の状態を参照するとき。
- 参照: `this.#input`

## UrlbarChildController.window()
- 位置: L131-133
- 役割: input が属するウィンドウを返す。chrome ならブラウザーウィンドウ、子プロセスなら content ウィンドウ。
- 触るとき: ウィンドウ単位の処理がどのウィンドウに対して行われるかを確かめるとき。
- 参照: `this.#input.window`

## UrlbarChildController.view()
- 位置: L135-137
- 役割: 登録済みのビューを返す。
- 触るとき: ビューへ処理を渡す前に、ビューが設定されているかを確かめるとき。
- 参照: `this.#view`

## UrlbarChildController.parentController()
- 位置: L145-147
- 役割: 親側の控え(本体または代理)を返す。
- 触るとき: 親側の API を直接呼ぶ箇所を追うとき。
- 参照: `this.#parentController`

## UrlbarChildController.engagementEvent()
- 位置: L156-160
- 役割: エンゲージメントの記録先を返す。代理経路では content 側の収集器を遅延生成し、直接経路では親の記録器を返す。
- 触るとき: エンゲージメント計測が子プロセスで欠落する問題を調べるとき。
- 参照: `this.#childTelemetry`, `this.#parentController`, `this.#parentController.engagementEvent`

## UrlbarChildController.userSelectionBehavior()
- 位置: L169-171
- 役割: ユーザーが結果を選んだ方法(arrow, tab, none)を返す。
- 触るとき: 選択方法の計測値がどう決まるかを確かめるとき。
- 参照: `this.#userSelectionBehavior`

## UrlbarChildController.userSelectionBehavior()
- 位置: L173-180
- 役割: 選択方法を設定する。tab が記録済みのあとは arrow で上書きしない。
- 触るとき: Tab と矢印のどちらが先に使われたかを判定する仕組みを変えるとき。
- 参照: `this.#userSelectionBehavior`

## UrlbarChildController.setView()
- 位置: L182-184
- 役割: ビューを登録する。
- 触るとき: ビューの生成順序を変えたり、ビューを差し替えたりするとき。
- 参照: `this.#view`

## UrlbarChildController.resolveFallbackNavigation()
- 位置: async L186-191
- 役割: エンジンストアの準備を待ってから、親側でフォールバック遷移の解決を依頼する。
- 触るとき: 貼り付けて Enter のような即時遷移が、検索エンジン未準備でも正しく動くか調べるとき。
- 呼び出し先: `this.#engineStoreReady()`, `this.#parentController.resolveFallbackNavigation()`

## UrlbarChildController.addListener()
- 位置: L193-198
- 役割: 通知を受けるリスナーを登録する。オブジェクトでなければ TypeError。
- 触るとき: ビューや他のコンポーネントが通知を受け取る仕組みを追加するとき。
- 呼び出し先: `this.#listeners.add()`

## UrlbarChildController.removeListener()
- 位置: L200-202
- 役割: 登録済みのリスナーを外す。
- 触るとき: リスナーの解除漏れで通知が届き続ける問題を調べるとき。
- 呼び出し先: `this.#listeners.delete()`

## UrlbarChildController.notifyFromWire()
- 位置: L213-222
- 役割: ワイヤー上の引数のうち serializedQueryContext を持つものを UrlbarQueryContext に戻してから notify に渡す。
- 触るとき: 親から届いた通知の引数の形を変えるとき。
- 呼び出し先: `UrlbarQueryContext.fromWire()`, `params.map()`, `this.notify()`
- 参照: `param.serializedQueryContext`, `param?.serializedQueryContext`

## UrlbarChildController.notify()
- 位置: L234-271
- 役割: 古いクエリ ID の結果と終了通知を捨て、先頭結果が変わったら推測接続を起こし、残りの通知をリスナーへ配る。
- 触るとき: クエリの通知が古いまま届く、または結果が出ない問題を調べるとき。
- 条件付き依存: `if ( notification === UrlbarShared.NOTIFICATIONS.QUERY_RESULTS && params[0].firstResultChanged )` → `this.#parentController.speculativeConnect()`
- 条件付き依存: `if (typeof listener[notification] != "undefined")` → `listener[notification]()`
- 条件付き依存: `if (typeof listener[notification] != "undefined")` → `console.error()`
- 参照: `UrlbarShared.NOTIFICATIONS.QUERY_FINISHED`, `UrlbarShared.NOTIFICATIONS.QUERY_FIRST_RESULT`, `UrlbarShared.NOTIFICATIONS.QUERY_RESULTS`, `params[0].firstResultChanged`, `params[0].id`, `params[0].results`, `this.#listeners`, `this.#queryId`

## UrlbarChildController.startQuery()
- 位置: L289-308
- 役割: クエリ ID とキャンセル状態を更新し、エンジンストア未準備ならその準備を待ってから、準備できていれば直ちに dispatchQuery を呼ぶ。
- 触るとき: エンジンが未初期化の状態で検索が始まる問題や、クエリの開始タイミングを変えるとき。
- 呼び出し先: `this.#dispatchQuery()`, `this.#engineStoreReady()`, `this.#engineStoreReady().then()`, `this.#input.eventBufferer.queryStarting()`
- 条件付き依存: `if (this.engineStore.initialized || this.engineStore.failed)` → `this.#dispatchQuery()`
- 参照: `queryContext.id`, `this.#queryCancelled`, `this.#queryId`, `this.engineStore.failed`, `this.engineStore.initialized`

## UrlbarChildController.#dispatchQuery()
- 位置: L316-325
- 役割: 親コントローラーへクエリを渡し、その後にイベントバッファーをクエリ開始状態にする。
- 触るとき: クエリ開始時の Enter 遅延処理と親への依頼の順序を変えるとき。
- 呼び出し先: `this.#input.eventBufferer.queryStarting()`, `this.#parentController.startQuery()`

## UrlbarChildController.#engineStoreReady()
- 位置: async L336-345
- 役割: エンジンストアが使えるまで待つ。初期化に失敗しても reject せず、そのまま戻る。
- 触るとき: 検索サービスの失敗時に入力が止まってしまわないか確かめるとき。
- 呼び出し先: `this.engineStore.init()`
- 参照: `this.engineStore.failed`, `this.engineStore.initialized`

## UrlbarChildController.cancelQuery()
- 位置: L347-351
- 役割: 待機中のクエリを開始させないようにフラグを立て、親にもキャンセルを依頼する。
- 触るとき: クエリのキャンセルが親と子の両方で正しく効くか調べるとき。
- 呼び出し先: `this.#parentController.cancelQuery()`
- 参照: `this.#queryCancelled`

## UrlbarChildController.discardResults()
- 位置: L364-367
- 役割: クエリ ID を進めて、そのクエリをリスナーにはキャンセル扱いで通知する。
- 触るとき: 検索モードへの切り替えなどで結果を捨てて再検索する処理を変えるとき。
- 呼び出し先: `this.notify()`
- 参照: `UrlbarShared.NOTIFICATIONS.QUERY_CANCELLED`, `this.#queryId`

## UrlbarChildController.handleKeyNavigation()
- 位置: L382-675
- 役割: キー入力を受け、ビューの選択移動、Enter の実行、Escape での閉じや戻し、Tab の循環、矢印や Page キーの移動、Backspace や Delete の処理を行う。executeAction が偽なら実行せず、既定動作の抑止だけ行う。
- 触るとき: キーボード操作の挙動を変えるとき、特に smartbar での Tab 循環や Mac の ctrl+n/p、検索モードの解除を確認するとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `UrlbarPrefs.get()`, `event.preventDefault()`, `this.input.getAttribute()`, `this.input.maybeConfirmSearchModeFromResult()`, `this.logger.debug()`, `this.view.isResultMenuOpen()`, `this.view.removeAccessibleFocus()`, `this.view.shouldSpaceActivateSelectedElement()`
- 条件付き依存: `if (executeAction)` → `this.view.selectBy()`
- 条件付き依存: `if ( isMac && this.view.isOpen && event.ctrlKey && (event.key == "n" || event.key == "p") )` → `event.preventDefault()`
- 条件付き依存: `if (executeAction)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `this.input.searchModeSwitcher.handleKeyDown()`
- 条件付き依存: `if ( this.view.isOpen && this.#parentController._lastQueryContextWrapper )` → `this.view.oneOffSearchButtons?.handleKeyDown()`
- 条件付き依存: `if (this.view.isOpen)` → `this.view.close()`
- 条件付き依存: `if (!(this.view.isOpen))` → `UrlbarPrefs.get()`
- 条件付き依存: `if ( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...)` → `this.input.blur()`
- 条件付き依存: `if (!( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...))` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...))` → `this.input.getAttribute()`
- 条件付き依存: `if (!( // An in-page urlbar returns focus to the host page. !this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.searchMode && this...))` → `this.window.isBlankPageURL()`
- 条件付き依存: `if ( // A chrome urlbar moves focus into the content document instead. this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.search...)` → `this.window.gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (!( // A chrome urlbar moves focus into the content document instead. this.window.gBrowser && UrlbarPrefs.get("focusContentDocumentOnEsc") && !this.input.search...))` → `this.input.handleRevert()`
- 条件付き依存: `if (executeAction)` → `this.input.handleCommand()`
- 条件付き依存: `if ( this.input.sapName == "smartbar" && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getLastSelectableElement()`
- 条件付き依存: `if ( this.input.sapName == "smartbar" && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getFirstSelectableElement()`
- 条件付き依存: `if (atEnd)` → `smartbar.focusFirstActionButton()`
- 条件付き依存: `if (!(atEnd))` → `smartbar.focusLastActionButton()`
- 条件付き依存: `if (atEnd || atStart)` → `event.preventDefault()`
- 条件付き依存: `if ( UrlbarPrefs.get("scotchBonnet.enableOverride") && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getFirstSelectableElement()`
- 条件付き依存: `if ( UrlbarPrefs.get("scotchBonnet.enableOverride") && this.view.isOpen && !event.ctrlKey && !event.altKey )` → `this.view.getLastSelectableElement()`
- 条件付き依存: `if ( (event.shiftKey && this.view.selectedElement == this.view.getFirstSelectableElement()) || (!event.shiftKey && this.view.selectedElement == this.view.getLast...)` → `event.preventDefault()`
- 条件付き依存: `if ( (event.shiftKey && this.view.selectedElement == this.view.getFirstSelectableElement()) || (!event.shiftKey && this.view.selectedElement == this.view.getLast...)` → `this.focusOnUnifiedSearchButton()`
- 条件付き依存: `if (event.shiftKey)` → `this.focusOnUnifiedSearchButton()`
- 条件付き依存: `if (!(event.shiftKey))` → `this.view.selectBy()`
- 条件付き依存: `if ( !this.view.selectedElement && this.input.focusedViaMousedown )` → `event.preventDefault()`
- 条件付き依存: `if ( // Even if the view is closed, we may be waiting results, and in // such a case we don't want to tab out of the urlbar. (this.view.isOpen || !executeAction)...)` → `event.preventDefault()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.keyEventMovesCaret()`
- 条件付き依存: `if (executeAction)` → `this.input.startQuery()`
- 条件付き依存: `if ( this.input.searchMode && this.input.selectionStart == 0 && this.input.selectionEnd == 0 && !event.shiftKey )` → `this.input.startQuery()`
- 条件付き依存: `if (event.shiftKey)` → `this.#dismissSelectedResult()`
- 条件付き依存: `if (!executeAction || this.#dismissSelectedResult(event))` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_END`, `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_HOME`, `KeyEvent.DOM_VK_LEFT`, `KeyEvent.DOM_VK_PAGE_DOWN`, `KeyEvent.DOM_VK_PAGE_UP`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_RIGHT`, `KeyEvent.DOM_VK_SPACE`, `KeyEvent.DOM_VK_TAB`, `KeyEvent.DOM_VK_UP`, `UrlbarShared.PAGE_UP_DOWN_DELTA`, `UrlbarShared.RESULT_SOURCE.ACTIONS`, `event.altKey`, `event.ctrlKey`, `event.key`, `event.keyCode`, `event.shiftKey`, `queryContext.searchString`, `this.#parentController._lastQueryContextWrapper`, `this.input`, `this.input.focusedViaMousedown`, `this.input.sapName`, `this.input.searchMode`, `this.input.searchMode?.isPreview`, `this.input.searchMode?.source`, `this.input.selectionEnd`, `this.input.selectionStart`, `this.input.value`, `this.input.view.oneOffSearchButtons`, `this.input.view.oneOffSearchButtons.selectedButton`, `this.userSelectionBehavior`, `this.view.allowEmptySelection`, `this.view.isOpen`, `this.view.selectedElement`, `this.view.selectedRowIndex`, `this.view.visibleRowCount`, `this.window.gBrowser`, `this.window.gBrowser.currentURI.spec`

## UrlbarChildController.#dismissSelectedResult()
- 位置: L689-719
- 役割: 選択中の結果に対して dismiss のエンゲージメントを記録する。ボタン上の選択や先頭の heuristic 結果は対象外。
- 触るとき: 結果の削除(Shift+Delete)の対象判定を変えるとき。
- 呼び出し先: `selectedElement?.classList.contains()`, `this.engagementEvent.record()`, `this.input.getSearchSource()`
- 条件付き依存: `if (!this.#parentController._lastQueryContextWrapper)` → `console.error()`
- 参照: `queryContext.searchString`, `result.autofill`, `result.heuristic`, `this.#parentController._lastQueryContextWrapper`, `this.input.view`, `this.input.view.selectedResult`

## UrlbarChildController.keyEventMovesCaret()
- 位置: L734-759
- 役割: 上下キーがビューを開く代わりにキャレットを動かすべきかを判定する。Mac と Linux で、選択範囲があるか入力の先頭末尾でない場合に真を返す。
- 触るとき: 上下キーでビューが開かず文字列内のカーソルだけが動く条件を変えるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_UP`, `event.keyCode`, `this.input.selectionEnd`, `this.input.selectionStart`, `this.input.value.length`, `this.view.isOpen`

## UrlbarChildController.isCanonizeKeyboardEvent()
- 位置: L769-785
- 役割: Enter に修飾キー(Mac は Meta、他は Ctrl)が付き、ctrlCanonizesURLs が有効な場合に正規化要求と判定する。searchbar では常に偽。
- 触るとき: Ctrl+Enter などで URL 正規化が起きる条件を変えるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `UrlbarPrefs.get()`, `UrlbarShared.isInstance()`
- 参照: `(event)._disableCanonization`, `KeyEvent.DOM_VK_RETURN`, `keyEvent.ctrlKey`, `keyEvent.keyCode`, `keyEvent.metaKey`, `this.#input.sapName`

## UrlbarChildController.whereToOpen()
- 位置: L797-838
- 役割: イベントから開き先を決める。Alt は別タブ、正規化は現在のタブ、それ以外は whereToOpenLink を使う。openintab の設定で反転し、空のタブは再利用する。
- 触るとき: アドレスバーから開くときに新規タブになるか現在のタブになるかを変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isInstance()`, `event.getModifierState()`
- 条件付き依存: `if (!( isKeyboardEvent && (event.altKey || event.getModifierState("AltGraph")) ))` → `this.isCanonizeKeyboardEvent()`
- 条件付き依存: `if (!(this.isCanonizeKeyboardEvent(event)))` → `UrlbarContentUtils.whereToOpenLink()`
- 参照: `event.altKey`, `event.shiftKey`, `this.#input.sapName`, `this.window.gBrowser?.selectedTab.isEmpty`

## UrlbarChildController.focusOnUnifiedSearchButton()
- 位置: L840-872
- 役割: 検索モード切替ボタンへフォーカスを移す。移動中は入力欄の blur で閉じないよう一時的にリスナーを外し、外れたら blur を発火させる。
- 触るとき: Tab でボタンへ移動したときにビューが閉じてしまう問題を調べるとき。
- 呼び出し先: `switcher.addEventListener()`, `switcher.focus()`, `this.input.contains()`, `this.input.hasAttribute()`, `this.input.inputField.addEventListener()`, `this.input.inputField.removeEventListener()`, `this.input.querySelector()`, `this.input.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if ( this.input.hasAttribute("focused") && !this.input.contains(relatedTarget) )` → `this.input.inputField.dispatchEvent()`
- 参照: `e.relatedTarget`, `this.input`

## UrlbarChildController.maybeInitEngineStore()
- 位置: L874-880
- 役割: 直接経路なら親のエンジンストア初期化を同期で呼び、代理経路では初期化を行わず false を返す。
- 触るとき: エンジンストアを初期化するタイミングや経路の違いを確かめるとき。
- 呼び出し先: `this.#parentController.maybeInitEngineStore()`
- 参照: `this.#parentController`

## UrlbarChildController.updateEngineStore()
- 位置: L885-887
- 役割: 受け取った情報でエンジンストアを更新する。
- 触るとき: 親からエンジン一覧が届いたときの反映処理を変えるとき。
- 呼び出し先: `this.engineStore.receive()`
