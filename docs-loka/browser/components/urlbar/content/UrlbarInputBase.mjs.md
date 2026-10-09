# browser/components/urlbar/content/UrlbarInputBase.mjs

source: browser/components/urlbar/content/UrlbarInputBase.mjs
source-hash: 9bf6ad33a0f777638ee5929526978cb801d245ef
lines: 6715

## <module>
- 役割: urlbar や searchbar など検索入力欄(search access point)の共通基盤となるカスタム要素 UrlbarInputBase を定義し、DOM の組み立て・初期化・イベント処理・検索と結果選択までを担う。
- 呼び出し先: `Promise.resolve()`

## logger()
- 位置: L123-123
- 役割: "Input" 接頭辞付きの UrlbarShared ロガーを返す。
- 触るとき: urlbar 入力欄まわりのログ出力を追加・調整し、どの経路が動いたかを確かめたいとき。
- 呼び出し先: `UrlbarShared.getLogger()`

## parseMarkupToFragment()
- 位置: L142-168
- 役割: 入力欄のマークアップ文字列を XHTML 名前空間の XML として解析し、空白だけのテキストノードを除いた DocumentFragment を返す。
- 触るとき: #markup の HTML を変えて、要素間の空白テキストが a11y ツリーに混ざっていないか確かめるとき。
- 呼び出し先: `blank.forEach()`, `doc.createTreeWalker()`, `node.data.trim()`, `node.remove()`, `parser.parseFromString()`, `walker.nextNode()`
- 条件付き依存: `if (!node.data.trim())` → `blank.push()`
- 参照: `(doc.documentElement) .content`, `NodeFilter.SHOW_TEXT`, `doc.documentElement`, `doc.documentElement.localName`, `walker.currentNode`

## UrlbarInputBase.#markup()
- 位置: L175-241
- 役割: 入力欄の DOM 構造(検索モード切替ボタン、input 要素、Go ボタン、結果ビュー、one-off 用スロットなど)を文字列で定義する。browser.nova.enabled の値で hr の並びが変わる。
- 触るとき: 入力欄に子要素や属性(role、data-l10n-id、スロット名など)を足す、または nova 切替時の表示崩れを調べるとき。
- 呼び出し先: `UrlbarPrefs.get()`

## UrlbarInputBase.fragment()
- 位置: L244-252
- 役割: 解析済みマークアップを初回だけ作ってキャッシュし、以後は importNode で複製した DocumentFragment を返す getter。
- 触るとき: 入力欄の初期 DOM が生成されない、または複数の入力欄で要素が共有されてしまうように見えるとき。
- 呼び出し先: `document.importNode()`
- 条件付き依存: `if (!UrlbarInputBase.#fragment)` → `parseMarkupToFragment()`
- 参照: `UrlbarInputBase.#fragment`, `UrlbarInputBase.#markup`

## UrlbarInputBase.observedAttributes()
- 位置: L254-256
- 役割: 監視対象の属性として "open" だけを返す。
- 触るとき: open 属性の変化でポップオーバーの表示を更新する仕組みを増やすか、ポップオーバーが開閉に追従しないとき。

## UrlbarInputBase.constructor()
- 位置: L347-360
- 役割: window と document の参照と isPrivate を設定し、プリファレンス監視を登録して unload 時に監視を外す。
- 触るとき: プライベートウィンドウ判定に依存する処理を変えるとき、または閉じたウィンドウで pref 監視が残るのを調べるとき。
- 呼び出し先: `UrlbarContentUtils.isWindowPrivate()`, `UrlbarPrefs.addObserver()`, `UrlbarPrefs.removeObserver()`, `super()`, `window.addEventListener()`
- 参照: `this.document`, `this.isPrivate`, `this.window`, `this.window.document`

## UrlbarInputBase.#populateSlots()
- 位置: L368-395
- 役割: moz-urlbar-slot を名前で探し、対応する urlbar-slot 属性の子を slot の前へ移し、slot 要素を削除する。あわせて identity-box などの内部参照を取得する。
- 触るとき: 入力欄の子要素をスロット経由で差し込む仕組みや、スロット名を追加・変更するとき。
- 呼び出し先: `slot.getAttribute()`, `slot.parentNode.insertBefore()`, `slot.remove()`, `this._searchModeIndicator?.querySelector()`, `this.querySelector()`, `this.querySelectorAll()`
- 参照: `this._identityBox`, `this._revertButton`, `this._searchModeIndicator`, `this._searchModeIndicatorClose`, `this._searchModeIndicatorTitle`

## UrlbarInputBase.#addStylesheet()
- 位置: L401-413
- 役割: chrome ウィンドウ以外では urlbar.css の link 要素を head に追加する。同じ href の link が既にあれば何もしない。
- 触るとき: コンテンツ文書で入力欄のスタイルが当たらないとき。
- 呼び出し先: `document.createElement()`, `document.head.appendChild()`, `document.querySelector()`
- 参照: `link.href`, `link.rel`

## UrlbarInputBase.#init()
- 位置: L418-537
- 役割: 初回接続時に sap-name と navigation 可否を読み、DOM 断片とスタイルを付け、結果リストと入力要素の属性を設定し、controller、view、searchModeSwitcher、eventBufferer を生成してプレースホルダーとエンジンストアを初期化する。
- 触るとき: 初期化の順序を変えるとき、または接続後に入力欄が機能しない、プレースホルダーが更新されないと感じたとき。
- 呼び出し先: `Object.defineProperty()`, `UrlbarPrefs.get()`, `UrlbarShared.navigationEnabled()`, `searchModeSwitcherDescription.setAttribute()`, `this.#addStylesheet()`, `this._setPlaceholder()`, `this.appendChild()`, `this.controller.addListener()`, `this.getAttribute()`, `this.inputField.setAttribute()`, `this.querySelector()`, `this.sapInit()`
- 条件付き依存: `if (document.readyState === "loading")` → `document.addEventListener()`
- 条件付き依存: `if (document.readyState === "loading")` → `this.#populateSlots()`
- 条件付き依存: `if (!(document.readyState === "loading"))` → `this.#populateSlots()`
- 条件付き依存: `if (this.#isAddressbar)` → `document.createElement()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.inputField.before()`
- 条件付き依存: `if (this.sapName != "newtab_searchbar")` → `this.controller.maybeInitEngineStore()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#initEngineStoreAfterPaint().then()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#initEngineStoreAfterPaint()`
- 条件付き依存: `if (!(this.controller.maybeInitEngineStore()))` → `this.#deferUpdatePlaceholder()`
- 条件付き依存: `if (!(this.sapName != "newtab_searchbar"))` → `this.controller.engineStore.init().then()`
- 条件付き依存: `if (!(this.sapName != "newtab_searchbar"))` → `this.controller.engineStore.init()`
- 条件付き依存: `if (!(this.sapName != "newtab_searchbar"))` → `this.searchModeSwitcher.updateSearchIcon()`
- 参照: `UrlbarInputBase.fragment`, `document.readyState`, `schemeField.id`, `schemeField.required`, `this.#isAddressbar`, `this.#navigationEnabled`, `this.#sapName`, `this._inputContainer`, `this.controller`, `this.eventBufferer`, `this.inputField`, `this.inputField.dir`, `this.inputField.id`, `this.inputField.inputMode`, `this.panel`, `this.querySelector(".urlbarView-results").id`, `this.sapName`, `this.searchModeSwitcher`, `this.view`

## UrlbarInputBase.get()
- 位置: L502-504
- 役割: placeholder、selectionStart、selectionEnd の読み取りを内部の input 要素へ転送する。
- 触るとき: 外から入力欄の値や選択範囲を読む経路を追うとき。
- 参照: `this.inputField`

## UrlbarInputBase.set()
- 位置: L505-507
- 役割: placeholder、selectionStart、selectionEnd の書き込みを内部の input 要素へ転送する。
- 触るとき: 外から入力欄のプレースホルダーや選択位置を書き換えても反映されないとき。
- 参照: `this.inputField`

## UrlbarInputBase.attributeChangedCallback()
- 位置: L539-545
- 役割: open 属性が変わったときだけ updatePopover を呼ぶ。
- 触るとき: ポップオーバーの開閉が属性変更と連動しないとき。
- 呼び出し先: `this.updatePopover()`

## UrlbarInputBase.sapInit()
- 位置: L551-551
- 役割: サブクラス向けの空のフックで、#init の中から呼ばれる。
- 触るとき: UrlbarInput や SearchbarInput など検索窓の種類ごとに初期化処理を足すとき。

## UrlbarInputBase.initSapContextMenuItems()
- 位置: L556-556
- 役割: サブクラス向けの空のフックで、コンテキストメニュー項目を追加する場として使われる。
- 触るとき: 検索窓の種類ごとに右クリックメニューの項目を変えるとき。

## UrlbarInputBase.sapConnectedCallback()
- 位置: L561-561
- 役割: サブクラス向けの空のフックで、接続の最後に呼ばれる。
- 触るとき: 検索窓の接続完了後に種類ごとの処理を足すとき。

## UrlbarInputBase.sapDisconnectedCallback()
- 位置: L567-567
- 役割: サブクラス向けの空のフックで、切断の最初に呼ばれる。
- 触るとき: 検索窓が DOM から外れる時の後始末を種類ごとに足すとき。

## UrlbarInputBase.connectedCallback()
- 位置: L569-646
- 役割: 接続時に未初期化なら #init を呼び、文脈メニュー・検索モード切替・キーとマウスのリスナーを登録して、プレースホルダーとポップオーバーの可否を整える。readOnly のときはリスナーを付けずポップオーバーを無効にして戻る。
- 触るとき: 入力欄が DOM に付け直されたときにイベントが二重登録されないか、読み取り専用の切り替えで操作や表示が変わるかを調べるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `document.documentElement.hasAttribute()`, `this.#initContextMenuItems()`, `this._addObservers()`, `this._initCopyCutController()`, `this._inputContainer.addEventListener()`, `this.addEventListener()`, `this.closest()`, `this.hasAttribute()`, `this.inputField.addEventListener()`, `this.sapConnectedCallback()`, `this.searchModeSwitcher.connect()`, `this.toggleAttribute()`, `this.updatePopover()`, `this.view.panel.addEventListener()`, `this.window.addEventListener()`
- 条件付き依存: `if (!this.controller)` → `this.#init()`
- 条件付き依存: `if (this.inOverflowPanel && this.view.isOpen)` → `this.view.close()`
- 条件付き依存: `if (this.readOnly)` → `this.updatePopover()`
- 条件付き依存: `if (this.readOnly)` → `this.removeAttribute()`
- 条件付き依存: `if (UrlbarContentUtils.getPlatform() == "win")` → `this.window.addEventListener()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.addGBrowserListeners()`
- 条件付き依存: `if (this.controller.engineStore.initialized)` → `this.searchModeSwitcher.updateSearchIcon()`
- 条件付き依存: `if (this.controller.engineStore.initialized)` → `this.updatePlaceholder()`
- 条件付き依存: `if (!(this.controller.engineStore.initialized))` → `this.#initPlaceholderFromPref()`
- 参照: `UrlbarInputBase.#inputFieldEvents`, `this.#popoverAllowed`, `this.controller`, `this.controller.engineStore.initialized`, `this.focused`, `this.inOverflowPanel`, `this.readOnly`, `this.view.isOpen`, `this.window.gBrowser`

## UrlbarInputBase.disconnectedCallback()
- 位置: L648-691
- 役割: connectedCallback で登録したリスナー、コピー・カットのコントローラー、gBrowser のタブ監視、文脈メニュー項目、オブザーバーを外して後始末する。
- 触るとき: 検索窓を閉じた後にイベントやメニュー項目が残り、別の入力欄に影響するのを調べるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `this.#removeContextMenuItems()`, `this._inputContainer.removeEventListener()`, `this._removeObservers()`, `this.inputField.removeEventListener()`, `this.removeEventListener()`, `this.sapDisconnectedCallback()`, `this.searchModeSwitcher.disconnect()`, `this.view.panel.removeEventListener()`, `this.window.removeEventListener()`
- 条件付き依存: `if (this._copyCutController)` → `this.inputField.controllers.removeController()`
- 条件付き依存: `if (UrlbarContentUtils.getPlatform() == "win")` → `this.window.removeEventListener()`
- 条件付き依存: `if (this.#gBrowserListenersAdded)` → `this.window.gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (this.#gBrowserListenersAdded)` → `this.window.gBrowser.removeTabsProgressListener()`
- 参照: `UrlbarInputBase.#inputFieldEvents`, `this.#gBrowserListenersAdded`, `this._copyCutController`

## UrlbarInputBase.#initContextMenuItems()
- 位置: L704-721
- 役割: 文脈メニューに入力欄固有の項目を登録する。EditContextMenu がない窓では何もしない。アドレスバーでは macOS なら共有グループの項目、他の OS は strip-on-share 項目を登録し、さらに自動補完の削除項目と検索エンジン追加項目も登録する。
- 触るとき: 右クリックメニューに項目を足すとき、または macOS と他の OS で項目の出し分けが違う理由を追うとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`, `this.#initAddSearchEngines()`, `this._initPasteAndGo()`, `this.initSapContextMenuItems()`
- 条件付き依存: `if (this.#isAddressbar && UrlbarContentUtils.getPlatform() == "macosx")` → `this.#initShareURL()`
- 条件付き依存: `if (!(this.#isAddressbar && UrlbarContentUtils.getPlatform() == "macosx"))` → `this._initStripOnShare()`
- 条件付き依存: `if (this.#isAddressbar)` → `this._initAutofillDismiss()`
- 参照: `this.#isAddressbar`, `this.window.EditContextMenu`

## UrlbarInputBase.#initAddSearchEngines()
- 位置: L727-741
- 役割: 検索エンジン追加用の項目セットを EditContextMenu に登録する。メニューを開くたびに AddSearchEngineHelper の最新項目で中身を差し替える。
- 触るとき: 「検索エンジンを追加」メニューの項目が古いまま表示されるとき。
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L729-735
- 役割: 検索エンジン追加メニュー用に、区切り線だけを含む DocumentFragment を作って返す。
- 触るとき: 検索エンジン追加メニューの区切り線の位置や内容を変えるとき。
- 呼び出し先: `fragment.appendChild()`, `this.addSearchEngineHelper.createContextSeparator()`, `this.document.createDocumentFragment()`

## onShowing()
- 位置: L736-739
- 役割: メニュー表示時に項目配列を空にし、AddSearchEngineHelper.refreshContextMenu の結果で入れ替える。
- 触るとき: メニューを開くたびに検索エンジン項目が重複したり欠けたりするとき。
- 呼び出し先: `items.push()`, `this.addSearchEngineHelper.refreshContextMenu()`
- 参照: `items.length`

## UrlbarInputBase.addContextMenuItems()
- 位置: L749-756
- 役割: 項目セットを EditContextMenu に登録し、返された登録情報を保持して切断時に外せるようにする。対象は matches で絞る。
- 触るとき: 入力欄ごとに文脈メニューの項目を追加するとき。
- 呼び出し先: `this.#contextMenuItemSets.push()`, `this.window.EditContextMenu.addItems()`

## matches()
- 位置: L753-753
- 役割: 文脈メニューの項目を出す対象が、この入力欄の inputField かどうかを判定する。
- 触るとき: 同じ窓の別の入力欄に項目が出てしまうとき。
- 参照: `this.inputField`

## UrlbarInputBase.#removeContextMenuItems()
- 位置: L762-767
- 役割: 保持している項目セットを EditContextMenu から外し、保持配列を空にする。
- 触るとき: 切断後も文脈メニューの項目が残るのを調べるとき。
- 呼び出し先: `this.window.EditContextMenu.removeItems()`
- 参照: `this.#contextMenuItemSets`

## UrlbarInputBase.addGBrowserListeners()
- 位置: L769-776
- 役割: gBrowser があり、まだ未登録のときだけ TabSelect と TabClose のリスナーとタブ進捗リスナーを登録する。
- 触るとき: タブを切り替えたときに入力欄の表示が更新されないとき。
- 条件付き依存: `if (this.window.gBrowser && !this.#gBrowserListenersAdded)` → `this.window.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (this.window.gBrowser && !this.#gBrowserListenersAdded)` → `this.window.gBrowser.addTabsProgressListener()`
- 参照: `this.#gBrowserListenersAdded`, `this.window.gBrowser`

## UrlbarInputBase.addSearchEngineHelper()
- 位置: L785-787
- 役割: AddSearchEngineHelper を初回アクセス時に生成して保持する getter。
- 触るとき: 検索エンジン追加メニューの状態を参照または更新する箇所を追うとき。
- 参照: `this.#addSearchEngineHelper`

## UrlbarInputBase.#getValueFormatter()
- 位置: L789-791
- 役割: UrlbarValueFormatter を初回だけ生成して返す。
- 触るとき: 入力欄の値の装飾(表示の整形)の仕組みを変えるとき。
- 参照: `lazy.UrlbarValueFormatter`, `this.#valueFormatter`

## UrlbarInputBase.sapName()
- 位置: L793-795
- 役割: 初期化時に読んだ検索窓の名前(urlbar、searchbar など)を返す getter。
- 触るとき: テレメトリやログで検索窓の種類を区別するとき。
- 参照: `this.#sapName`

## UrlbarInputBase.isSidebarMode()
- 位置: L797-799
- 役割: 常に false を返す。サイドバー表示の判定用で、派生クラスが上書きする想定。
- 触るとき: サイドバーでの検索窓の挙動を区別する処理を足すとき。

## UrlbarInputBase.isSearchbarSAP()
- 位置: L808-810
- 役割: sapName を UrlbarShared.isSearchbarSAP に渡し、検索専用の窓かどうかを返す。
- 触るとき: 検索専用の窓だけ挙動を変えたいとき。
- 呼び出し先: `UrlbarShared.isSearchbarSAP()`
- 参照: `this.#sapName`

## UrlbarInputBase.variantA()
- 位置: L818-820
- 役割: variant-a 属性があるかを返す。New Tab 側が urlbar の newtabVariantA の Nimbus 変数から属性を設定する。
- 触るとき: レイアウト variant A の表示切替を追うとき。
- 呼び出し先: `this.hasAttribute()`

## UrlbarInputBase.variantB()
- 位置: L829-831
- 役割: variant-b 属性があるかを返す。検索エンジンボタンを入力欄の上段に置くレイアウトを示す。
- 触るとき: レイアウト variant B の表示切替を追うとき。
- 呼び出し先: `this.hasAttribute()`

## UrlbarInputBase.windowMode()
- 位置: L838-845
- 役割: テレメトリ用の窓種別を返す。プライベートなら private、AI ウィンドウが有効なら smartwindow、それ以外は classic。
- 触るとき: テレメトリの窓種別の値を変えるとき、または AI ウィンドウの判定が合わないとき。
- 呼び出し先: `lazy?.AIWindow.isAIWindowActive()`
- 参照: `this.isPrivate`, `this.window`

## UrlbarInputBase.parentController()
- 位置: L847-849
- 役割: controller の parentController を返す。
- 触るとき: 検索結果を親側へ渡す経路を追うとき。
- 参照: `this.controller.parentController`

## UrlbarInputBase.blur()
- 位置: L851-853
- 役割: 内部の input 要素からフォーカスを外す。
- 触るとき: 入力欄からフォーカスを外す処理を変えるとき。
- 呼び出し先: `this.inputField.blur()`

## UrlbarInputBase.readOnly()
- 位置: L855-863
- 役割: 内部 input の readOnly を設定する。値が変わり接続中なら disconnectedCallback と connectedCallback をやり直して、読み取り専用に応じたリスナーとポップオーバーの状態を作り直す。
- 触るとき: 読み取り専用に切り替えた後に文脈メニューやポップオーバーの状態が残るとき。
- 条件付き依存: `if (this.isConnected)` → `this.disconnectedCallback()`
- 条件付き依存: `if (this.isConnected)` → `this.connectedCallback()`
- 参照: `this.inputField.readOnly`, `this.isConnected`

## UrlbarInputBase.readOnly()
- 位置: L868-870
- 役割: 内部 input の readOnly を返す getter。
- 触るとき: 読み取り専用かどうかで分岐する箇所を追うとき。
- 参照: `this.inputField.readOnly`

## UrlbarInputBase.onPrefChanged()
- 位置: L893-899
- 役割: keyword.enabled が変わったときだけ updatePlaceholder を呼ぶ。
- 触るとき: キーワード検索の設定変更がプレースホルダーに反映されないとき。
- 呼び出し先: `this.updatePlaceholder()`

## UrlbarInputBase.formatValue()
- 位置: L904-909
- 役割: アドレスバーで editor があるときだけ UrlbarValueFormatter.update を呼び、値の装飾を更新する。
- 触るとき: URL の色分けや装飾が古いままになるとき。
- 条件付き依存: `if (this.#isAddressbar && this.editor)` → `this.#getValueFormatter().update()`
- 条件付き依存: `if (this.#isAddressbar && this.editor)` → `this.#getValueFormatter()`
- 参照: `this.#isAddressbar`, `this.editor`

## UrlbarInputBase.focus()
- 位置: L911-922
- 役割: beforefocus イベントを内部 input に発行し、キャンセルされなければ内部 input にフォーカスする。
- 触るとき: 外部からのフォーカス要求を横取りしたいとき、またはフォーカスが来ない原因を調べるとき。
- 呼び出し先: `this.inputField.dispatchEvent()`, `this.inputField.focus()`
- 参照: `beforeFocus.defaultPrevented`

## UrlbarInputBase.select()
- 位置: L924-939
- 役割: beforeselect を発行し、キャンセルされなければ主選択の書き換えを抑えたまま内部 input を全選択する。
- 触るとき: 全選択で主選択が書き換わるなどの問題を調べるとき。
- 呼び出し先: `this.inputField.dispatchEvent()`, `this.inputField.select()`
- 参照: `beforeSelect.defaultPrevented`, `this._suppressPrimaryAdjustment`

## UrlbarInputBase.setSelectionRange()
- 位置: L941-956
- 役割: beforeselect を発行し、キャンセルされなければ主選択の書き換えを抑えたまま指定範囲を選択する。
- 触るとき: 任意範囲の選択処理を変えるとき。
- 呼び出し先: `this.inputField.dispatchEvent()`, `this.inputField.setSelectionRange()`
- 参照: `beforeSelect.defaultPrevented`, `this._suppressPrimaryAdjustment`

## UrlbarInputBase.saveSelectionStateForBrowser()
- 位置: L958-970
- 役割: ブラウザごとの状態に選択範囲と、URL を再整形(untrim)するかどうかを保存する。値が空なら先頭から末尾までを全選択として扱う。
- 触るとき: タブを切り替えて戻ったときに選択位置が復元されないとき。
- 呼び出し先: `this.getBrowserState()`
- 参照: `Number.MAX_SAFE_INTEGER`, `state.selection`, `this._protocolIsTrimmed`, `this._wwwIsTrimmed`, `this.selectionEnd`, `this.selectionStart`, `this.value`

## UrlbarInputBase.restoreSelectionStateForBrowser()
- 位置: L972-986
- 役割: まずフォーカスし、保存された状態があれば必要なら URL を untrim してから、終端を値の長さで丸めて選択範囲を戻す。
- 触るとき: タブに戻ったときに選択やテキストの復元がずれるとき。
- 呼び出し先: `this.focus()`, `this.getBrowserState()`
- 条件付き依存: `if (state.selection.shouldUntrim)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (state.selection)` → `this.setSelectionRange()`
- 条件付き依存: `if (state.selection)` → `Math.min()`
- 参照: `state.selection`, `state.selection.end`, `state.selection.shouldUntrim`, `state.selection.start`, `this.value.length`

## UrlbarInputBase.setURI()
- 位置: L1005-1202
- 役割: アドレスバーに表示する URL を設定する。ユーザーが結果を選択中ならそのままにし、値が空やタブ切り替えの場合は認証プロンプトの URL か現在の URI を資格情報を除いて表示し、初期ページなら空にする。最後に選択範囲、proxy state、検索モードを整えて SetURI を発行する。
- 触るとき: タブ切り替えや読み込み完了で入力欄の値が差し替わらない、または選択位置や検索モードが戻らないとき。
- 呼び出し先: `UrlbarPrefs.getScotchBonnetPref()`, `lazy.UrlbarSearchTermsPersistence.searchModeMatchesState()`, `this.#handlePersistedSearchTerms()`, `this.getBrowserState()`, `this.inputField.dispatchEvent()`, `this.setPageProxyState()`, `this.setValue()`, `this.toggleAttribute()`, `uri.spec.startsWith()`
- 条件付き依存: `if ( dueToTabSwitch && UrlbarPrefs.getScotchBonnetPref("scotchBonnet.persistSearchMode") )` → `this._updateSearchModeUI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `Services.io.createExposableURI()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `this.window.isInitialPage()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if (!( this.window.isInitialPage(uri) && lazy.BrowserUIUtils.checkEmptyPageOrigin( this.window.gBrowser.selectedBrowser, uri ) ))` → `losslessDecodeDisplaySpec()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `this.#canHandleAsBlankPage()`
- 条件付き依存: `if (value === null || (!value && dueToTabSwitch))` → `lazy.ExtensionUtils.isExtensionUrl()`
- 条件付き依存: `if (!(value === null || (!value && dueToTabSwitch)))` → `this.window.isInitialPage()`
- 条件付き依存: `if (!(value === null || (!value && dueToTabSwitch)))` → `lazy.BrowserUIUtils.checkEmptyPageOrigin()`
- 条件付き依存: `if (this.focused && value != previousUntrimmedValue)` → `value.substring()`
- 条件付き依存: `if (this.focused && value != previousUntrimmedValue)` → `previousUntrimmedValue.substring()`
- 条件付き依存: `if ( previousSelectionStart != previousSelectionEnd && value.substring(previousSelectionStart, previousSelectionEnd) === previousUntrimmedValue.substring( previo...)` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if ( previousSelectionEnd && (previousUntrimmedValue.length === previousSelectionEnd || value.length <= previousSelectionEnd) )` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if (!( previousSelectionEnd && (previousUntrimmedValue.length === previousSelectionEnd || value.length <= previousSelectionEnd) ))` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if (dueToTabSwitch && !valid)` → `this.restoreSearchModeState()`
- 参照: `"www.".length`, `UrlbarShared.RESULT_SOURCE.SEARCH`, `lazy.BrowserUIUtils.trimURLProtocol.length`, `previousUntrimmedValue.length`, `state.persist.isDefaultEngine`, `state.persist.originalEngineName`, `state.persist?.shouldPersist`, `this.#isAddressbar`, `this.#isOpenedPageInBlankTargetLoading`, `this._protocolIsTrimmed`, `this._wwwIsTrimmed`, `this.focused`, `this.getBrowserState(this.window.gBrowser.selectedBrowser) .isUnifiedSearchButtonAvailable`, `this.searchMode`, `this.selectionEnd`, `this.selectionStart`, `this.untrimmedValue`, `this.userTypedValue`, `this.view.selectedResult`, `this.window.browsingContext.isDocumentPiP`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser`, `this.window.gBrowser.selectedBrowser.currentAuthPromptURI`, `uri.displaySpec`, `uri.spec`, `value.length`
- XPCOM: `Services.io`

## UrlbarInputBase.makeURIReadable()
- 位置: L1213-1228
- 役割: リーダーモードの原 URL を取り出し、取れなければ createExposableURI で資格情報を除いた URI を返す。どちらも失敗すれば元の URI を返す。
- 触るとき: 表示用に URL を整えて、ユーザー名やパスワードが入力欄に出ないようにしたいとき。
- 呼び出し先: `Services.io.createExposableURI()`, `lazy.ReaderMode.getOriginalUrlObjectForDisplay()`
- 参照: `uri.displaySpec`
- XPCOM: `Services.io`

## UrlbarInputBase.onLocationChange()
- 位置: L1241-1260
- 役割: トップレベルの場所変更を受け、選択中でないタブの読み込みなら統合検索ボタンを使用不可にし、履歴ボタンによる移動ならバウンスのテレメトリを記録する。
- 触るとき: タブを戻ったときに統合検索ボタンが出ない、または履歴移動の計測が合わないとき。
- 呼び出し先: `this.#canHandleAsBlankPage()`
- 条件付き依存: `if ( browser != this.window.gBrowser.selectedBrowser && !this.#canHandleAsBlankPage(locationURI.spec) )` → `this.getBrowserState()`
- 条件付き依存: `if (webProgress.loadType & Ci.nsIDocShell.LOAD_CMD_HISTORY)` → `lazy.handleBounceEventTrigger()`
- 参照: `Ci.nsIDocShell.LOAD_CMD_HISTORY`, `locationURI.spec`, `this.getBrowserState(browser).isUnifiedSearchButtonAvailable`, `this.window.gBrowser.selectedBrowser`, `webProgress.isTopLevel`, `webProgress.loadType`
- XPCOM: [`nsIDocShell`](../../../../docshell/base/nsIDocShell.idl.md)

## UrlbarInputBase.handleEvent()
- 位置: L1267-1278
- 役割: DOM イベントの type から _on_<type> のメソッドを呼び分ける。例外は console.error に出し、対応がなければ例外を投げる。
- 触るとき: 新しい DOM イベントを入力欄で扱いたいとき、または「Unrecognized UrlbarInput event」が出るとき。
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 条件付き依存: `if (methodName in this)` → `console.error()`
- 参照: `event.type`

## UrlbarInputBase.handleCommand()
- 位置: L1286-1315
- 役割: 右クリック以外のコマンドで、開いている結果ビューに選択中の one-off ボタンがあればその検索を実行する。なければ統合検索ボタンのアイコンを更新してから handleNavigation を呼ぶ。
- 触るとき: Enter やクリックで検索や移動を始める入口の振る舞いを変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isInstance()`, `this.handleNavigation()`
- 条件付き依存: `if (selectedOneOff && (!isMouseEvent || event.target == selectedOneOff))` → `this.view.oneOffSearchButtons.handleSearchCommand()`
- 条件付き依存: `if (UrlbarPrefs.get("unifiedSearchButton.always"))` → `this.searchModeSwitcher?.updateSearchIcon()`
- 参照: `event.button`, `event.target`, `selectedOneOff.engine?.name`, `selectedOneOff.source`, `this.view.isOpen`, `this.view.oneOffSearchButtons?.selectedButton`

## UrlbarInputBase.#searchModeEngineForEnterKey()
- 位置: L1340-1365
- 役割: 検索モードのエンジンで Enter の検索を行うべきときだけそのエンジンを返し、それ以外は null を返す。アドレスバー以外、IME 変換中、one-off 指定、検索モードでない場合は null。選択結果が検索の heuristic でない場合や、結果がなく URL 結果が出ている場合も null になる。
- 触るとき: 検索モード中に Enter を押したとき古いエンジンで検索される現象や、URL 結果を開く分岐を調べるとき。
- 呼び出し先: `UrlbarShared.navigationInSearchModeEnabled()`, `this.controller.engineStore.getEngineByName()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.URL`, `oneOffParams?.engine`, `result.heuristic`, `result.type`, `this.#isAddressbar`, `this.#sapName`, `this._resultForCurrentValue?.type`, `this.searchMode.engineName`, `this.searchMode?.engineName`

## UrlbarInputBase.#engineSearchStringForResult()
- 位置: L1374-1379
- 役割: 結果の suggestion か query を検索文字列とし、無ければ直前の検索文字列を返す。
- 触るとき: 結果からエンジン検索の文字列がどう決まるかを確かめるとき。
- 参照: `result.payload.query`, `result.payload.suggestion`, `this._lastSearchString`

## UrlbarInputBase.#selectedBrowserId()
- 位置: L1386-1388
- 役割: 選択中のブラウザの browserId を返す。gBrowser がなければ null。
- 触るとき: 検索結果を開く先のブラウザを読み込み処理に渡す経路を追うとき。
- 参照: `this.window.gBrowser?.selectedBrowser?.browserId`

## UrlbarInputBase.#openEngineSearch()
- 位置: L1409-1440
- 役割: エンゲージメントを記録し、検索をテレメトリに記録したうえで、親コントローラーの openSERP で選んだエンジンの検索結果ページを開く。
- 触るとき: one-off や検索モードの Enter で検索結果ページを開く処理や、その計測を変えるとき。
- 呼び出し先: `this._recordSearch()`, `this.controller.engagementEvent.record()`, `this.getSearchSource()`, `this.parentController.openSERP()`
- 参照: `engine.id`, `this.#selectedBrowserId`, `this._resultForCurrentValue`, `this.view.selectedResult`, `this.windowMode`

## UrlbarInputBase.handleNavigation()
- 位置: L1457-1672
- 役割: 選択中の要素と結果から開く先を順に決める。要素があり安全なら pickElement に回し、検索モードや one-off のエンジンなら検索結果ページを開き、URL なら #loadURL で読み込み、結果が無ければ親の resolveFallbackNavigation で heuristic か補正 URL を得て読み込む。
- 触るとき: Enter で検索になるかURLを開くかの分岐を変えるとき、または想定と違う読み込み経路を調べるとき。
- 呼び出し先: `URL.canParse()`, `UrlbarPrefs.get()`, `this.#getValueFromResult()`, `this.#searchModeEngineForEnterKey()`, `this._maybeCanonizeURL()`, `this.controller .resolveFallbackNavigation()`, `this.controller .resolveFallbackNavigation({ searchString: url, where, searchMode: this.searchMode, browserId, }) .then()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.value.startsWith()`, `this.view.getResultFromElement()`, `this.view.telemetryTypeFromElement()`, `url.trim()`
- 条件付き依存: `if ( !isComposing && element && !searchModeEngine && (!oneOffParams?.engine || selectedPrivateEngineResult) && safeToPickResult )` → `this.pickElement()`
- 条件付き依存: `if ( UrlbarPrefs.get("experimental.hideHeuristic") && !element && !isComposing && !oneOffParams?.engine && !searchModeEngine && this._resultForCurrentValue?.heur...)` → `this.pickResult()`
- 条件付き依存: `if (!result && this.value.startsWith("@"))` → `this.view.getResultAtIndex()`
- 条件付き依存: `if (tokenAliasResult?.autofill && tokenAliasResult?.payload.keyword)` → `this.pickResult()`
- 条件付き依存: `if (oneOffParams?.engine)` → `this.#openEngineSearch()`
- 条件付き依存: `if (oneOffParams?.engine)` → `this.#engineSearchStringForResult()`
- 条件付き依存: `if (searchModeEngine)` → `this.#openEngineSearch()`
- 条件付き依存: `if (searchModeEngine)` → `this.controller.whereToOpen()`
- 条件付き依存: `if (!url)` → `this.handleEmptyValueNavigation()`
- 条件付き依存: `if (this.#isAddressbar && URL.canParse(url))` → `this.#getSchemelessInput()`
- 条件付き依存: `if (this.#isAddressbar && URL.canParse(url))` → `this.#loadURL()`
- 条件付き依存: `if (!isComposing && this._resultForCurrentValue)` → `this.pickResult()`
- 条件付き依存: `if (heuristicResult)` → `this.pickResult()`
- 条件付き依存: `if (!fixup.keywordAsSent)` → `this.#getSchemelessInput()`
- 条件付き依存: `if (fixup)` → `this.#loadURL()`
- 参照: `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TIP`, `console.error`, `fixup.keywordAsSent`, `fixup.postData`, `fixup.url`, `oneOffParams.engine`, `oneOffParams.openWhere`, `oneOffParams?.engine`, `oneOffParams?.openParams`, `oneOffParams?.openWhere`, `openParams.allowInheritPrincipal`, `openParams.inBackground`, `openParams.private`, `openParams.schemelessInput`, `result.heuristic`, `result.payload.inPrivateWindow`, `result.payload.isPrivateEngine`, `result.type`, `this.#isAddressbar`, `this.#selectedBrowserId`, `this._lastSearchString`, `this._resultForCurrentValue`, `this._resultForCurrentValue?.heuristic`, `this.isComposing`, `this.searchMode`, `this.searchMode.engineName`, `this.untrimmedValue`, `this.value`, `this.valueIsTyped`, `this.view.selectedElement`, `this.view.selectedResult`, `this.windowMode`, `tokenAliasResult?.autofill`, `tokenAliasResult?.payload.keyword`

## UrlbarInputBase.handleEmptyValueNavigation()
- 位置: L1682-1682
- 役割: 空の基底実装で何もしない。サブクラス(searchbar など)が値が空のときに検索エンジンのページを開くように上書きする。
- 触るとき: 空の入力で Enter を押したときの動作を検索窓ごとに変えたいとき。

## UrlbarInputBase.handleRevert()
- 位置: L1684-1702
- 役割: 検索モードと入力値を取り消す。アドレスバーでは setURI で現在の URL に戻して、フォーカスがあれば全選択する。それ以外の入力では値を空にする。
- 触るとき: Escape などで入力を取り消した後に表示が現在のページと合わないとき。
- 呼び出し先: `this.setURI()`
- 条件付き依存: `if (!this.#isAddressbar)` → `this.toggleAttribute()`
- 条件付き依存: `if (this.value && this.focused)` → `this.select()`
- 参照: `this.#isAddressbar`, `this.focused`, `this.searchMode`, `this.userTypedValue`, `this.value`

## UrlbarInputBase.maybeHandleRevertFromPopup()
- 位置: L1704-1710
- 役割: アンカーが #urlbar 内にあり、永続検索語が有効なら handleRevert を呼び、ポップアップ経由の取り消し回数を Glean に記録する。
- 触るとき: 永続検索語をポップアップから戻すときの条件や計測を変えるとき。
- 呼び出し先: `anchorElement?.closest()`, `this.getBrowserState()`
- 条件付き依存: `if (anchorElement?.closest("#urlbar") && state.persist?.shouldPersist)` → `this.handleRevert()`
- 条件付き依存: `if (anchorElement?.closest("#urlbar") && state.persist?.shouldPersist)` → `Glean.urlbarPersistedsearchterms.revertByPopupCount.add()`
- 参照: `state.persist?.shouldPersist`, `this.window.gBrowser.selectedBrowser`

## UrlbarInputBase.handoff()
- 位置: L1725-1736
- 役割: 新しいタブページなど擬似的な検索窓からの入力を受け取り、ハンドオフのフラグを立てて search を呼ぶ。対象エンジンと設定があれば検索モードに入れる。
- 触るとき: 新しいタブや about:privatebrowsing からの検索引き渡しの挙動を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get("shouldHandOffToSearchMode") && searchEngine)` → `this.search()`
- 条件付き依存: `if (!(UrlbarPrefs.get("shouldHandOffToSearchMode") && searchEngine))` → `this.search()`
- 参照: `this._handoffSession`, `this._isHandoffSession`

## UrlbarInputBase.pickElement()
- 位置: L1744-1753
- 役割: 要素から結果を引き、見つかれば pickResult に渡す。
- 触るとき: 結果ビューの要素を選んだときの経路を追うとき。
- 呼び出し先: `logger()`, `logger().debug()`, `this.pickResult()`, `this.view.getResultFromElement()`
- 参照: `event?.type`

## UrlbarInputBase.handlesOpenInCommands()
- 位置: L1761-1763
- 役割: 常に true を返し、pickResult が結果メニューの新しいタブや窓で開く命令を扱うことを示す。
- 触るとき: サブクラスで結果メニューの開く命令の扱いを変えるとき。

## UrlbarInputBase.pickResult()
- 位置: L1778-2309
- 役割: 結果が選ばれたときの中心処理。メニューボタン、結果メニューのコマンド、検索モードの確定、タブへ切り替え、履歴の削除などを先に振り分け、残りは結果種別ごとに読み込み先(where)と読み込み要求を決めて、URL なら入力履歴に追加してから #loadURL で開く。
- 触るとき: 結果をクリックや Enter で選んだ後の開き先、エンゲージメントの記録、入力履歴への追加のどれかが想定と違うとき。
- 呼び出し先: `UrlbarContentUtils.willLoadInBackground()`, `UrlbarPrefs.get()`, `UrlbarShared.getLoadRequestFromResult()`, `UrlbarShared.looksLikeSingleWordHost()`, `element?.classList.contains()`, `lazy.ExtensionSearchHandler.handleInputEntered()`, `logger()`, `logger().error()`, `this.#loadURL()`, `this.#providesSearchMode()`, `this._recordSearch()`, `this.controller.engagementEvent .startTrackingBounceEvent()`, `this.controller.engagementEvent.record()`, `this.controller.engineStore.getEngineByName()`, `this.getSearchSource()`, `this.handleRevert()`, `this.hasAttribute()`, `this.maybeConfirmSearchModeFromResult()`, `this.parentController.switchToTab()`, `this.setValueFromResult()`, `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (element?.classList.contains("urlbarView-button-menu"))` → `this.view.openResultMenu()`
- 条件付き依存: `if (element?.dataset.command)` → `this.#pickMenuResult()`
- 条件付き依存: `if ( UrlbarPrefs.get("autoFill.adaptiveHistory.enabled") && result.autofill && result.payload?.url && !this.isPrivate )` → `this.parentController.clearAutofillBackspaceEntryForUrl()`
- 条件付き依存: `if ( result.providerName == "UrlbarProviderGlobalActions" && this.#providesSearchMode(result) && !this.view.selectedElement?.dataset.immediateSearch )` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( (this.searchMode?.isPreview && result.providerName == "UrlbarProviderGlobalActions" && !this.view.selectedElement?.dataset.immediateSearch) || (result.heuri...)` → `this.confirmSearchMode()`
- 条件付き依存: `if ( (this.searchMode?.isPreview && result.providerName == "UrlbarProviderGlobalActions" && !this.view.selectedElement?.dataset.immediateSearch) || (result.heuri...)` → `this.search()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.getSearchSource()`
- 条件付き依存: `if ( result.type == UrlbarShared.RESULT_TYPE.TIP && result.payload.type == "dismissalAcknowledgment" )` → `this.view.onQueryResultRemoved()`
- 条件付き依存: `if (openIn)` → `parseInt()`
- 条件付き依存: `if (!(openIn))` → `this.controller.whereToOpen()`
- 条件付き依存: `if (!this.#providesSearchMode(result) && !keepViewOpen)` → `this.view.close()`
- 条件付き依存: `if (isCanonized)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (isCanonized)` → `this.getSearchSource()`
- 条件付き依存: `if (isCanonized)` → `this.#loadURL()`
- 条件付き依存: `if (result.heuristic)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (result.heuristic)` → `UrlbarShared.looksLikeSingleWordHost()`
- 条件付き依存: `if (result.heuristic)` → `this.#getSchemelessInput()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.getSearchSource()`
- 条件付き依存: `if (result.payload.providesSearchMode)` → `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( this.#isAddressbar && !this.searchMode && result.heuristic && // If we asked the DNS earlier, avoid the post-facto check. !UrlbarPrefs.get("browser.fixup.dn...)` → `this.parentController.checkKeywordURIFixup()`
- 条件付き依存: `if ( this.#isAddressbar && !this.searchMode && result.heuristic && // If we asked the DNS earlier, avoid the post-facto check. !UrlbarPrefs.get("browser.fixup.dn...)` → `originalUntrimmedValue.trim()`
- 条件付き依存: `if ( this.#isAddressbar && !actionDetails.isFormHistory && !result.payload.inPrivateWindow && !this.isPrivate && engine.isAppProvided && engine == this.controlle...)` → `lazy.QuickSuggest.getFeature()`
- 条件付き依存: `if (merinoBackend?.isEnabled)` → `( result.payload.suggestion || result.payload.query )?.trim()`
- 条件付き依存: `if (merinoBackend?.isEnabled)` → `lazy.UrlUtils.looksLikeOrigin()`
- 条件付き依存: `if ( selection && lazy.UrlUtils.looksLikeOrigin(selection) == lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE )` → `this.#makeQueryContext()`
- 条件付き依存: `if ( selection && lazy.UrlUtils.looksLikeOrigin(selection) == lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE )` → `lazy.UrlbarTokenizer.tokenize()`
- 条件付き依存: `if ( selection && lazy.UrlUtils.looksLikeOrigin(selection) == lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE )` → `merinoBackend .query(selection, { queryContext: context }) .catch()`
- 条件付き依存: `if ( selection && lazy.UrlUtils.looksLikeOrigin(selection) == lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE )` → `merinoBackend .query()`
- 条件付き依存: `if (!this.isSearchbarSAP)` → `this.handleRevert()`
- 条件付き依存: `if (!loadRequest)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (!loadRequest)` → `this.view.telemetryTypeFromElement()`
- 条件付き依存: `if (!loadRequest)` → `this.getSearchSource()`
- 条件付き依存: `if (!loadRequest)` → `JSON.stringify()`
- 条件付き依存: `if (!( result.autofill?.type == "adaptive_url" || result.autofill?.type == "adaptive_origin" ))` → `UrlbarPrefs.get()`
- 条件付き依存: `if ( UrlbarPrefs.get("autoFill.adaptiveHistory.enabled") && result.autofill?.type == "origin" && // Bug: 2026227: Investigate if we want to use a higher threshol...)` → `this.parentController.addToInputHistory()`
- 条件付き依存: `if (input !== undefined)` → `this.parentController.addToInputHistory()`
- 条件付き依存: `if (!this.isPrivate && loadRequest.urlLoad)` → `UrlbarPrefs.get()`
- 条件付き依存: `if ( UrlbarPrefs.get("autoFill.adaptiveHistory.enabled") && (!result.autofill || result.autofill.type == "url") && result.type == UrlbarShared.RESULT_TYPE.URL )` → `this.parentController.handleAutofillReintegration()`
- 参照: `UrlbarShared.RESULT_SOURCE.HISTORY`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.TIP`, `UrlbarShared.RESULT_TYPE.URL`, `actionDetails.isFormHistory`, `console.error`, `context.tokens`, `element?.dataset.action`, `element?.dataset.command`, `element?.dataset.openIn`, `element?.dataset.url`, `element?.dataset.usercontextid`, `engine.isAppProvided`, `lazy.UrlUtils.LOOKS_LIKE_ORIGIN.NONE`, `loadRequest.urlLoad`, `loadRequest.urlLoad.url`, `merinoBackend?.isEnabled`, `openParams.allowInheritPrincipal`, `openParams.avoidBrowserFocus`, `openParams.eventDetail`, `openParams.forceForeground`, `openParams.private`, `openParams.schemelessInput`, `openParams.userContextId`, `result.autofill`, `result.autofill.adaptiveHistoryInput`, `result.autofill.type`, `result.autofill?.type`, `result.heuristic`, `result.id`, `result.payload.content`, `result.payload.engine`, `result.payload.inPrivateWindow`, `result.payload.keyword`, `result.payload.providesSearchMode`, `result.payload.query`, `result.payload.suggestion`, `result.payload.tabGroup`, `result.payload.type`, `result.payload.url`, `result.payload.userContext?.id`, `result.payload?.engine`, `result.payload?.isSponsored`, `result.payload?.url`, `result.providerName`, `result.source`, `result.type`, `this.#isAddressbar`, `this.#sapName`, `this.#selectedBrowserId`, `this._lastSearchString`, `this._lastSearchString?.length`, `this._untrimmedValue`, `this.controller.engineStore.default`, `this.isPrivate`, `this.isSearchbarSAP`, `this.searchMode`, `this.searchMode?.isPreview`, `this.untrimmedValue`, `this.value`, `this.view.oneOffSearchButtons?.selectedButton`, `this.view.selectedElement?.dataset.immediateSearch`, `this.windowMode`

## UrlbarInputBase.setValueFromResult()
- 位置: L2334-2441
- 役割: 選ばれた結果から入力欄の値を設定し、その結果を現在の値に紐づける。ページ状態を invalid にし、プレビュー中の検索モードを解除してから、正規化(canonize)、オートフィル値の適用、検索モードの確定、通常の値の設定の順に処理する。戻り値は正規化されたかどうか。
- 触るとき: 結果を選んだとき入力欄に入る値が想定と違うとき、または正規化の判定を変えたいとき。
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

## UrlbarInputBase.setResultForCurrentValue()
- 位置: L2454-2456
- 役割: 入力値に対応する結果を _resultForCurrentValue に保存するだけで、入力値は変えない。
- 触るとき: 選択を解除したときや、heuristic 結果を入力値を変えずに対応付けたいとき。
- 参照: `this._resultForCurrentValue`

## UrlbarInputBase._autofillFirstResult()
- 位置: L2466-2492
- 役割: 最初の結果がオートフィル結果なら、カーソルが末尾にあるか自動補完のプレースホルダーが選ばれている場合だけ setValueFromResult で補完する。それ以外は何もしない。
- 触るとき: 入力中に自動補完が出るべきなのに出ない、または出すぎるとき。
- 呼び出し先: `this._autofillPlaceholder.value .toLocaleLowerCase()`, `this._autofillPlaceholder.value .toLocaleLowerCase() .startsWith()`, `this._lastSearchString.toLocaleLowerCase()`, `this.setValueFromResult()`
- 参照: `result.autofill`, `this._autofillIgnoresSelection`, `this._autofillPlaceholder`, `this._autofillPlaceholder.value.length`, `this._lastSearchString.length`, `this.selectionEnd`, `this.selectionStart`

## UrlbarInputBase.#clearAutofill()
- 位置: L2496-2511
- 役割: 自動補完のプレースホルダーがあれば、入力値を補完前の部分だけに戻してプレースホルダーを外し、元の選択範囲を復元する。
- 触るとき: 補完された文字を取り消す場面の表示や選択を調べるとき。
- 呼び出し先: `this.setSelectionRange()`, `this.value.substring()`
- 参照: `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionStart`, `this.inputField.value`, `this.selectionEnd`, `this.selectionStart`

## UrlbarInputBase.onFirstResult()
- 位置: L2519-2553
- 役割: 新しい検索の最初の結果を受けて、キーワード付きの heuristic なら検索モードに入り既存の結果を破棄する。オートフィル結果なら補完を試み、そうでなければ先に表示した補完を外して入力中の文字列に戻す。
- 触るとき: 最初の結果による自動補完や、キーワードでの検索モード突入の挙動を変えるとき。
- 呼び出し先: `this.#providesSearchMode()`, `this.maybeConfirmSearchModeFromResult()`
- 条件付き依存: `if ( firstResult.heuristic && firstResult.payload.keyword && !this.#providesSearchMode(firstResult) && this.maybeConfirmSearchModeFromResult({ result: firstResul...)` → `this.controller.discardResults()`
- 条件付き依存: `if (firstResult.autofill)` → `this._autofillFirstResult()`
- 条件付き依存: `if (!(firstResult.autofill))` → `this.value.endsWith()`
- 条件付き依存: `if ( this._autofillPlaceholder && // Avoid clobbering added spaces (for token aliases, for example). !this.value.endsWith(" ") )` → `this.setValue()`
- 参照: `firstResult.autofill`, `firstResult.heuristic`, `firstResult.payload.keyword`, `queryContext.results`, `this._autofillPlaceholder`, `this.userTypedValue`

## UrlbarInputBase.startQuery()
- 位置: L2582-2636
- 役割: 入力値(または指定の検索文字列)から検索のクエリ文脈を作る。event があればエンゲージメントの記録を開始し、検索モードを確定し、オーバーフローパネル内では検索を始めずに controller.startQuery に渡す。
- 触るとき: 入力や Enter で検索が始まらない、または検索状態が前回から引き継がれるとき。
- 呼び出し先: `this.#makeQueryContext()`, `this.controller.startQuery()`
- 条件付き依存: `if (!searchString)` → `this.getAttribute()`
- 条件付き依存: `if (!(!searchString))` → `this.value.startsWith()`
- 条件付き依存: `if (event)` → `this.controller.engagementEvent.start()`
- 条件付き依存: `if (resetSearchState)` → `this._resetSearchState()`
- 条件付き依存: `if (this.searchMode)` → `this.confirmSearchMode()`
- 参照: `this._autofillIgnoresSelection`, `this._lastSearchString`, `this._suppressStartQuery`, `this._valueOnLastSearch`, `this.inOverflowPanel`, `this.lastQueryContextPromise`, `this.searchMode`, `this.value`

## UrlbarInputBase.search()
- 位置: L2659-2741
- 役割: 値を設定して検索を始める公開メソッド。先頭の語が検索エンジンの別名や制限トークンなら検索モードに入り、必要ならフォーカスし、input イベントを発行して検索を起動する。検索サービスが未初期化の検索トークンは初期化を待って再実行する。
- 触るとき: 外部から検索文字列を流し込んだときに検索モードに入るか、またはフォーカスや検索の起動が想定どおりか調べるとき。
- 呼び出し先: `this.searchModeForToken()`, `trimmedValue.search()`, `trimmedValue.substring()`, `value.trim()`
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
- 参照: `UrlbarShared.REGEXP_SPACES`, `UrlbarShared.RESTRICT_TOKENS`, `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `options.focus`, `searchEngine.name`, `searchMode.entry`, `this._lastSearchString`, `this.controller.engineStore.failed`, `this.controller.engineStore.initialized`, `this.inputField.value`, `this.searchMode`, `this.selectionStart`, `this.window`

## UrlbarInputBase.searchModeForToken()
- 位置: L2752-2768
- 役割: 制限トークンから検索モードの設定を作る。検索トークンなら既定エンジン、アドレスバーでは LOCAL_SEARCH_MODES に一致するもののコピーを返し、一致しなければ null を返す。
- 触るとき: 新しい制限トークンを足すとき、または既定エンジンでの検索モードの決まり方を変えるとき。
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.SEARCH`, `m.restrict`, `this.#isAddressbar`, `this.controller.engineStore.default?.name`

## UrlbarInputBase.openSearchEnginePage()
- 位置: L2782-2835
- 役割: 値があれば、その検索語で選んだエンジンの検索結果ページを開く。現在のタブで開く場合は検索モードに入れてから開く。値が空ならエンジンの検索フォームを開く。
- 触るとき: 検索窓のボタンや Enter で検索結果ページが開かない、または現在のタブで検索モードが残らないとき。
- 呼び出し先: `value.trim()`
- 条件付き依存: `if (!searchEngine || !event || !where)` → `console.warn()`
- 条件付き依存: `if (trimmedValue)` → `this._recordSearch()`
- 条件付き依存: `if (where == "current")` → `this.setSearchMode()`
- 条件付き依存: `if (trimmedValue)` → `this.parentController.openSERP()`
- 条件付き依存: `if (!(trimmedValue))` → `this.parentController.openSearchForm()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `searchEngine.id`, `searchEngine.name`, `this.#selectedBrowserId`, `this._lastSearchString`, `this.window.gBrowser?.selectedBrowser`

## UrlbarInputBase.setHiddenFocus()
- 位置: L2841-2848
- 役割: フォーカス枠を出さずにフォーカスする。_hideFocus を立て、既にフォーカスがあれば focused 属性を外し、なければ focus を呼ぶ。
- 触るとき: 新しいタブページなどから検索語を渡すときに、フォーカス枠を出したくないとき。
- 条件付き依存: `if (this.focused)` → `this.removeAttribute()`
- 条件付き依存: `if (!(this.focused))` → `this.focus()`
- 参照: `this._hideFocus`, `this.focused`

## UrlbarInputBase.removeHiddenFocus()
- 位置: L2857-2866
- 役割: _hideFocus を外し、フォーカス中なら focused 属性を戻す。引数が真なら suppress-focus-border も付ける。
- 触るとき: 隠していたフォーカス枠を元に戻すとき、または枠の抑制を追加するとき。
- 条件付き依存: `if (this.focused)` → `this.toggleAttribute()`
- 条件付き依存: `if (forceSuppressFocusBorder)` → `this.toggleAttribute()`
- 参照: `this._hideFocus`, `this.focused`

## UrlbarInputBase.getSearchMode()
- 位置: L2883-2894
- 役割: ブラウザに対応する検索モードを返す。confirmedOnly が偽なら preview を優先し、無ければ confirmed を返す。どちらも無ければ null。
- 触るとき: プレビュー中と確定済みの検索モードのどちらが使われているかを確かめたいとき。
- 呼び出し先: `this.#getSearchModesObject()`
- 参照: `modes.confirmed`, `modes.preview`

## UrlbarInputBase.setSearchMode()
- 位置: async L2907-3004
- 役割: ブラウザごとの検索モードを設定する。エンジン名が無効なら検索モードを解除し、確定かプレビューかに応じて保存する。選択中のブラウザなら表示を更新し、確定かつ新規の検索モードは recordSearchMode で記録する。最後に searchmodechanged を発行する。
- 触るとき: 検索モードに入る、または抜けるときの保存先や表示、記録の条件を変えるとき。
- 呼び出し先: `UrlbarShared.SEARCH_MODE_ENTRY.has()`, `UrlbarShared.deepEqual()`, `lazy?.UrlbarSearchTermsPersistence.onSearchModeChanged()`, `this.#getSearchModesObject()`, `this.dispatchEvent()`, `this.getSearchMode()`
- 条件付き依存: `if (!this.controller.engineStore.initialized)` → `this.controller.engineStore.init()`
- 条件付き依存: `if (searchMode?.engineName)` → `this.controller.engineStore.getEngineByName()`
- 条件付き依存: `if (source)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (!(sourceName))` → `console.error()`
- 条件付き依存: `if ( !this.#isAddressbar || browser == this.window.gBrowser.selectedBrowser )` → `this._updateSearchModeUI()`
- 条件付き依存: `if (!newSearchMode.isPreview && !areSearchModesSame)` → `this.parentController.recordSearchMode()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `engine.isGeneralPurposeEngine`, `modes.confirmed`, `modes.preview`, `newSearchMode.isGeneralPurposeEngine`, `newSearchMode.isPreview`, `newSearchMode.restrictType`, `newSearchMode.source`, `searchMode.engineName`, `searchMode?.engineName`, `this.#isAddressbar`, `this.controller.engineStore.initialized`, `this.untrimmedValue`, `this.userTypedValue`, `this.valueIsTyped`, `this.window`, `this.window.gBrowser.selectedBrowser`

## UrlbarInputBase.#getSearchModesObject()
- 位置: L3032-3042
- 役割: 検索モードを保存するオブジェクトを返す。検索窓は窓全体で1つを使い、アドレスバーはブラウザごとの状態の中に保存する。
- 触るとき: 検索モードの保存先がタブごとか窓全体かを確かめるとき。
- 呼び出し先: `this.getBrowserState()`
- 参照: `state.searchModes`, `this.#isAddressbar`, `this.#searchbarSearchModes`

## UrlbarInputBase.restoreSearchModeState()
- 位置: L3047-3051
- 役割: 選択中のブラウザに保存された確定済みの検索モードを searchMode に戻す。
- 触るとき: タブを切り替えて戻ったときに検索モードが復元されないとき。
- 呼び出し先: `this.#getSearchModesObject()`
- 参照: `this.#getSearchModesObject( this.window.gBrowser?.selectedBrowser ).confirmed`, `this.searchMode`, `this.window.gBrowser?.selectedBrowser`

## UrlbarInputBase.searchModeShortcut()
- 位置: async L3056-3078
- 役割: 既定エンジンの検索モードに入るショートカットの処理。エンジン未初期化なら初期化を待ち、失敗したら何もしない。検索結果だけを対象にする検索モードを設定し、現在の値で検索して全選択する。
- 触るとき: 検索モードのショートカットの動作を変えるとき、または既定エンジンが使われない原因を調べるとき。
- 呼び出し先: `this.search()`, `this.select()`
- 条件付き依存: `if (!this.controller.engineStore.initialized)` → `this.controller.engineStore.init()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `this.controller.engineStore.default.name`, `this.controller.engineStore.initialized`, `this.searchMode`, `this.value`

## UrlbarInputBase.confirmSearchMode()
- 位置: L3083-3094
- 役割: プレビュー中の検索モードを確定に切り替え、選ばれていた one-off ボタンの選択を外す。
- 触るとき: プレビューの検索モードが確定されないとき、または one-off の選択表示が残るとき。
- 参照: `searchMode.isPreview`, `searchMode?.isPreview`, `this.searchMode`, `this.view.oneOffSearchButtons`, `this.view.oneOffSearchButtons.selectedButton`

## UrlbarInputBase.editor()
- 位置: L3098-3100
- 役割: 内部 input 要素の editor を返す getter。
- 触るとき: 入力欄の編集機能にアクセスする箇所を追うとき。
- 参照: `this.inputField.editor`

## UrlbarInputBase.focused()
- 位置: L3102-3104
- 役割: 内部 input 要素が document の activeElement かどうかを返す getter。
- 触るとき: 入力欄にフォーカスがあるかの判定を変えたいとき。
- 参照: `this.document.activeElement`, `this.inputField`

## UrlbarInputBase.goButton()
- 位置: L3106-3108
- 役割: urlbar-go-button クラスの要素を返す getter。
- 触るとき: Go ボタンの状態や表示を変えるとき。
- 呼び出し先: `this.querySelector()`

## UrlbarInputBase.value()
- 位置: L3110-3112
- 役割: 内部 input 要素の値を返す getter。
- 触るとき: 入力欄の現在の値を読む箇所を追うとき。
- 参照: `this.inputField.value`

## UrlbarInputBase.value()
- 位置: L3114-3116
- 役割: 値を設定する setter。allowTrim を真にして setValue を呼ぶ。
- 触るとき: 入力欄に値を入れた後に先頭の http や www が削られる挙動を調べるとき。
- 呼び出し先: `this.setValue()`

## UrlbarInputBase.untrimmedValue()
- 位置: L3118-3120
- 役割: プロトコルや www を削る前の値(_untrimmedValue)を返す getter。
- 触るとき: 表示用に削られた値ではなく元の文字列が必要なとき。
- 参照: `this._untrimmedValue`

## UrlbarInputBase.userTypedValue()
- 位置: L3122-3126
- 役割: ユーザーが入力した値を返す getter。アドレスバーではタブ側の値を、検索窓では自身の値を読む。
- 触るとき: タブごとに入力中の文字列がどう保たれるかを追うとき。
- 参照: `this.#isAddressbar`, `this._userTypedValue`, `this.window.gBrowser.userTypedValue`

## UrlbarInputBase.userTypedValue()
- 位置: L3128-3134
- 役割: ユーザーが入力した値を設定する setter。アドレスバーではタブ側に、検索窓では自身に保存する。
- 触るとき: タブを切り替えて戻ったときに入力中の文字列が戻らないとき。
- 参照: `this.#isAddressbar`, `this._userTypedValue`, `this.window.gBrowser.userTypedValue`

## UrlbarInputBase.lastSearchString()
- 位置: L3136-3138
- 役割: 直前の検索文字列を返す getter。
- 触るとき: 直前の検索語を使う処理(テレメトリやエンジン検索)を追うとき。
- 参照: `this._lastSearchString`

## UrlbarInputBase.searchMode()
- 位置: L3150-3158
- 役割: 選択中のブラウザの検索モードを返す getter。アドレスバーでブラウザがまだ無いときは null を返す。
- 触るとき: 今の入力欄が検索モードかどうかを判定する箇所を追うとき。
- 呼び出し先: `this.getSearchMode()`
- 参照: `this.#isAddressbar`, `this.window.gBrowser`, `this.window.gBrowser?.selectedBrowser`

## UrlbarInputBase.searchMode()
- 位置: L3160-3169
- 役割: 検索モードを設定する setter。setSearchMode を呼んで完了を #searchModeApplied に保持し、現在の検索モードのエンジンを使用済みとして記録する。
- 触るとき: 検索モードを設定した後、エンジンの使用履歴や適用完了のタイミングを調べるとき。
- 呼び出し先: `this.controller.engineStore .getEngineByName()`, `this.controller.engineStore .getEngineByName(this.searchMode?.engineName) ?.markAsUsed()`, `this.setSearchMode()`
- 参照: `this.#searchModeApplied`, `this.searchMode?.engineName`, `this.window.gBrowser?.selectedBrowser`

## UrlbarInputBase.getBrowserState()
- 位置: L3171-3178
- 役割: ブラウザごとの状態オブジェクトを WeakMap から返し、無ければ空のものを作って保存する。
- 触るとき: タブごとに保存する状態(選択範囲や検索モードなど)を追加するとき。
- 呼び出し先: `this.#browserStates.get()`
- 条件付き依存: `if (!state)` → `this.#browserStates.set()`

## UrlbarInputBase.#openPopover()
- 位置: L3180-3186
- 役割: 結果パネルがまだ開いていなければ showPopover で表示する。
- 触るとき: 結果パネルが表示されない原因を調べるとき。
- 呼び出し先: `this.panel.matches()`, `this.panel.showPopover()`

## UrlbarInputBase.#closePopover()
- 位置: L3188-3194
- 役割: 結果パネルが開いていれば hidePopover で閉じる。
- 触るとき: 結果パネルが閉じない原因を調べるとき。
- 呼び出し先: `this.panel.hidePopover()`, `this.panel.matches()`

## UrlbarInputBase.updatePopover()
- 位置: L3201-3209
- 役割: 表示条件(ポップオーバーが許可され、結果ビューが開いている)を満たせば結果パネルを開き、そうでなければ閉じる。open 属性も同じ結果に合わせる。
- 触るとき: 結果パネルが開いたまま残る、または開くべきときに出ないとき。
- 呼び出し先: `this.toggleAttribute()`
- 条件付き依存: `if (popoverOpen)` → `this.#openPopover()`
- 条件付き依存: `if (!(popoverOpen))` → `this.#closePopover()`
- 参照: `this.#popoverAllowed`, `this.view.isOpen`

## UrlbarInputBase.setPageProxyState()
- 位置: L3231-3256
- 役割: 入力欄とその容器、identity-box の pageproxystate 属性を設定し、統合検索ボタンの可否を更新する。valid になったら値を _lastValidURLStr に保存し、state が変わったときだけ必要に応じてポップアップ通知の表示を更新する。
- 触るとき: アドレスバーの鍵や保護表示が現在のページと合わないとき、または統合検索ボタンが出ない原因を調べるとき。
- 呼び出し先: `this._identityBox?.setAttribute()`, `this._inputContainer.setAttribute()`, `this.getAttribute()`, `this.setAttribute()`, `this.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if ( updatePopupNotifications && prevState != state && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 参照: `this._lastValidURLStr`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`

## UrlbarInputBase.afterTabSwitchFocusChange()
- 位置: L3263-3266
- 役割: フォーカス変化を記録し、タブ切り替えとフォーカスの両方が揃ったときの後処理を行う。
- 触るとき: タブを素早く切り替えた時に結果パネルがちらつく場合など、タブ切り替えとフォーカスの順序を調べるとき。
- 呼び出し先: `this._afterTabSelectAndFocusChange()`
- 参照: `this._gotFocusChange`

## UrlbarInputBase.maybeConfirmSearchModeFromResult()
- 位置: L3287-3329
- 役割: 結果がキーワードに一致し検索モードを作れるなら、その検索モードに入り、結果のクエリを入力欄に入れる。startQuery が真なら検索モードを確定し、入力を保存して、検索モードが適用された後に検索を始める。入ったかどうかを返す。
- 触るとき: キーワードや結果から検索モードに入る条件、またはプレビューと確定の違いを変えるとき。
- 呼び出し先: `result.payload.autofillKeyword?.trim()`, `result.payload.keyword?.trim()`, `result.payload.query?.trimStart()`, `this._searchModeForResult()`, `this.setValue()`, `this.value.trim()`
- 条件付き依存: `if (startQuery)` → `this.#searchModeApplied.then()`
- 条件付き依存: `if (startQuery)` → `this.startQuery()`
- 参照: `searchMode.isPreview`, `this._resultForCurrentValue`, `this.searchMode`, `this.untrimmedValue`, `this.userTypedValue`

## UrlbarInputBase.onSearchEngineUpdate()
- 位置: L3335-3352
- 役割: 検索エンジンの削除や変更では、現在の検索モードのエンジンならモードを再設定する。既定エンジンの変更ではプレースホルダーを更新し、キャッシュした結果を捨てる。
- 触るとき: エンジンを削除や既定変更したときに検索モードや表示が古いままになるとき。
- 呼び出し先: `this.updatePlaceholder()`
- 参照: `engine.name`, `searchMode?.engineName`, `this._resultForCurrentValue`, `this.searchMode`

## UrlbarInputBase.getSearchSource()
- 位置: L3363-3395
- 役割: テレメトリ用の検索元の名前を決める。アドレスバーでは、ハンドオフ、検索モード切替パネル、検索モード中(one-off 以外)、永続検索語の順に判定し、いずれでもなければ sapName を返す。
- 触るとき: 検索の計測で urlbar_searchmode や urlbar_persisted などの値がどう付くかを確かめるとき。
- 条件付き依存: `if (this.#isAddressbar)` → `this.searchModeSwitcher?.eventTargetIsPanelItem()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.view.oneOffSearchButtons?.eventTargetIsAOneOff()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 参照: `state.persist?.searchTerms`, `this.#isAddressbar`, `this.#sapName`, `this._isHandoffSession`, `this.searchMode`, `this.window.gBrowser.selectedBrowser`

## UrlbarInputBase.#providesSearchMode()
- 位置: L3404-3415
- 役割: 結果が検索モードを提供するかを返す。グローバルアクションでは選択中の要素の data-provides-searchmode を見て判定する。
- 触るとき: 一部のボタンだけが検索モードを提供する結果の扱いを変えるとき。
- 参照: `result.payload.providesSearchMode`, `result.providerName`, `this.view.selectedElement`, `this.view.selectedElement.dataset.providesSearchmode`

## UrlbarInputBase._addObservers()
- 位置: L3417-3423
- 役割: 一度だけ engineStore に onSearchEngineUpdate を登録する。
- 触るとき: 検索エンジンの変更通知が届かないと感じるとき。
- 呼び出し先: `this.controller.engineStore.addObserver()`
- 参照: `this._observersAdded`, `this.onSearchEngineUpdate`

## UrlbarInputBase._removeObservers()
- 位置: L3425-3431
- 役割: 登録済みなら engineStore から onSearchEngineUpdate を外す。
- 触るとき: 切断後も検索エンジンの通知を受け続けるのを防ぐ後始末を確かめるとき。
- 呼び出し先: `this.controller.engineStore.removeObserver()`
- 参照: `this._observersAdded`, `this.onSearchEngineUpdate`

## UrlbarInputBase._afterTabSelectAndFocusChange()
- 位置: L3433-3468
- 役割: タブ切り替えとフォーカス変化の両方を受けたときだけ、値の装飾を更新し検索状態を戻す。フォーカス中なら engagement を記録し、自動で開けなければ検索モード切替パネルと結果ビューを閉じる。
- 触るとき: タブを切り替えた後に結果ビューが開く、または閉じないときの条件を調べるとき。
- 呼び出し先: `this._resetSearchState()`, `this.formatValue()`, `this.searchModeSwitcher.closePanel()`, `this.view.autoOpen()`, `this.view.close()`
- 条件付き依存: `if (this.focused)` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (this.focused)` → `this.getSearchSource()`
- 参照: `this._gotFocusChange`, `this._gotTabSelect`, `this._lastSearchString`, `this.focused`, `this.windowMode`

## UrlbarInputBase.setValue()
- 位置: L3482-3535
- 役割: 入力欄の値を設定する中心処理。about:reader の URL を元の URL に直し、アドレスバーで allowTrim が真なら http や www を削って削除されたプレフィックスを記録する。値、valueIsTyped、actiontype を設定し、値の装飾を更新する。
- 触るとき: 入力欄に表示される値(プロトコル省略の有無や actiontype)が想定と違うとき。
- 呼び出し先: `event.initEvent()`, `lazy?.ReaderMode.getOriginalUrlObjectForDisplay()`, `this.document.createEvent()`, `this.formatValue()`, `this.inputField.dispatchEvent()`
- 条件付き依存: `if (allowTrim && this.#isAddressbar)` → `this._trimValue()`
- 条件付き依存: `if (allowTrim && this.#isAddressbar)` → `lazy.BrowserUIUtils.getTrimmedURLPrefix()`
- 条件付き依存: `if (allowTrim && this.#isAddressbar)` → `val.startsWith()`
- 条件付き依存: `if (trimmedPrefix && !val.startsWith(trimmedPrefix))` → `trimmedPrefix.startsWith()`
- 条件付き依存: `if (trimmedPrefix && !val.startsWith(trimmedPrefix))` → `trimmedPrefix.endsWith()`
- 条件付き依存: `if (actionType !== undefined)` → `this.setAttribute()`
- 条件付き依存: `if (!(actionType !== undefined))` → `this.removeAttribute()`
- 参照: `lazy.BrowserUIUtils.trimURLProtocol`, `originalUrl.displaySpec`, `this.#isAddressbar`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.inputField.value`, `this.valueIsTyped`

## UrlbarInputBase.#getValueFromResult()
- 位置: L3563-3641
- 役割: 選ばれた結果から入力欄に入れる文字列を作る。キーワードや検索は キーワード と候補(または検索語)を連結し、DYNAMIC や TIP は要素の data 属性を優先する。URL 系は urlOverride があればそれを使い、無ければ結果の URL を読み、アドレスバーの暫定 http:// を入力に戻すかを判定する。
- 触るとき: 結果を選んだ後に入力欄へ入る文字(検索語か URL か)が結果の種類ごとに違うとき。
- 呼び出し先: `URL.parse()`, `UrlbarContentUtils.getFixupPrimitives()`, `UrlbarShared.stripPrefixAndTrim()`, `losslessDecodeURL()`, `result.payload.url.startsWith()`, `this.#getSchemelessInput()`
- 条件付き依存: `if (urlOverride !== null)` → `URL.parse()`
- 条件付き依存: `if (urlOverride !== null)` → `losslessDecodeURL()`
- 参照: `UrlbarContentUtils.getFixupPrimitives( trimmedUrl, this.isPrivate )?.keywordAsSent`, `UrlbarShared.RESULT_TYPE.AI_CHAT`, `UrlbarShared.RESULT_TYPE.DYNAMIC`, `UrlbarShared.RESULT_TYPE.KEYWORD`, `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.RESTRICT`, `UrlbarShared.RESULT_TYPE.SEARCH`, `UrlbarShared.RESULT_TYPE.TIP`, `element?.dataset.input`, `element?.dataset.query`, `element?.dataset.url`, `result.heuristic`, `result.payload.autofillKeyword`, `result.payload.content`, `result.payload.input`, `result.payload.keyword`, `result.payload.query`, `result.payload.suggestion`, `result.payload.url`, `result.type`, `this.#isAddressbar`, `this.isPrivate`, `this.userTypedValue`

## UrlbarInputBase.#getActionTypeFromResult()
- 位置: L3650-3659
- 役割: タブ切り替えは switchtab、OMNIBOX は extension を返し、それ以外は undefined を返す。この値が actiontype 属性になる。
- 触るとき: 入力欄の actiontype 属性が結果の種類で変わる箇所を確かめるとき。
- 参照: `UrlbarShared.RESULT_TYPE.OMNIBOX`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `result.type`

## UrlbarInputBase._resetSearchState()
- 位置: L3665-3668
- 役割: 検索開始前に、直前の入力値を _lastSearchString にし、自動補完のプレースホルダーを捨てる。
- 触るとき: 操作をまたいで前回の検索の状態が残り、次の検索に影響するのを防ぎたいとき。
- 参照: `this._autofillPlaceholder`, `this._lastSearchString`, `this.value`

## UrlbarInputBase._maybeAutofillPlaceholder()
- 位置: L3680-3739
- 役割: カーソルが末尾で、ローカル検索モードかエンジン検索でなければ自動補完を許可する。許可されない場合は補完を消して false を返す。許可された場合、プレースホルダーが入力に合うなら、残りの補完文字列を入力欄に入れて true を返す。
- 触るとき: 入力中にどこまで自動補完されるか、またはモードで補完が止まる条件を変えるとき。
- 条件付き依存: `if (!allowAutofill)` → `this.#clearAutofill()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `this._autofillPlaceholder.value .toLocaleLowerCase() .startsWith()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `this._autofillPlaceholder.value .toLocaleLowerCase()`
- 条件付き依存: `if ( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" )` → `value.toLocaleLowerCase()`
- 条件付き依存: `if (!( this._autofillPlaceholder.type == "adaptive_url" || this._autofillPlaceholder.type == "adaptive_origin" ))` → `UrlbarShared.canAutofillURL()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.selectionEnd == this.value.length && this._enableAutofillPlaceholder )` → `this._autofillPlaceholder.value.substring()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.selectionEnd == this.value.length && this._enableAutofillPlaceholder )` → `this._autofillValue()`
- 参照: `UrlbarShared.RESULT_SOURCE.SEARCH`, `autofillValue.length`, `this._autofillPlaceholder`, `this._autofillPlaceholder.adaptiveHistoryInput`, `this._autofillPlaceholder.adaptiveHistoryInput.length`, `this._autofillPlaceholder.type`, `this._autofillPlaceholder.untrimmedValue`, `this._autofillPlaceholder.value`, `this._enableAutofillPlaceholder`, `this.searchMode?.engineName`, `this.searchMode?.source`, `this.selectionEnd`, `this.value.length`, `value.length`

## UrlbarInputBase.updateTextOverflow()
- 位置: L3746-3798
- 役割: アドレスバーで文字があふれているときだけ、スクロール位置から左右どちらの側でフェードさせるかを決めて textoverflow 属性に設定する。RTL の場合は向きを反転して判定する。
- 触るとき: 長い URL の左右のフェード表示が逆になる、または消えないとき。
- 呼び出し先: `UrlbarContentUtils.isTextDirectionRTL()`, `this.getAttribute()`, `this.window.promiseDocumentFlushed()`
- 条件付き依存: `if (!this._overflowing)` → `this.removeAttribute()`
- 条件付き依存: `if (input && this._overflowing)` → `this.window.requestAnimationFrame()`
- 条件付き依存: `if (this._overflowing)` → `this.setAttribute()`
- 参照: `input.scrollLeft`, `input.scrollLeftMax`, `input.scrollLeftMin`, `this.#isAddressbar`, `this._overflowing`, `this.inputField`, `this.value`

## UrlbarInputBase.inOverflowPanel()
- 位置: L3800-3809
- 役割: 親要素が CustomizableUI のはみ出しパネル内にあるか、または overflowedItem 属性があるかを返す getter。
- 触るとき: はみ出しパネルに入った入力欄で検索が始まらない、または表示が変わるとき。
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`, `this.parentElement.getAttribute()`
- 参照: `lazy.CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `lazy.CustomizableUI.getPlacementOfWidget(this.parentElement.id)?.area`, `this.parentElement.id`, `this.parentElement?.id`

## UrlbarInputBase._updateUrlTooltip()
- 位置: L3811-3817
- 役割: フォーカスがなく、あふれている場合だけ input の title に元の URL を入れ、それ以外は title を外す。
- 触るとき: あふれた URL にマウスを載せたときのツールチップの表示条件を変えるとき。
- 条件付き依存: `if (this.focused || !this._overflowing)` → `this.inputField.removeAttribute()`
- 条件付き依存: `if (!(this.focused || !this._overflowing))` → `this.inputField.setAttribute()`
- 参照: `this._overflowing`, `this.focused`, `this.untrimmedValue`

## UrlbarInputBase._getSelectedValueForClipboard()
- 位置: L3819-3918
- 役割: コピーされる選択文字列を決める。先頭から URL 全体(または先頭部分)が選ばれているときは、表示用の完全な URL や省略されたプレフィックスを補い、decodeURLsOnCopy が偽なら encodeURI で符号化する。それ以外は選択文字列をそのまま返す。
- 触るとき: アドレスバーでコピーした URL の形式(http の省略、エンコードの有無)が想定と違うとき。
- 呼び出し先: `UrlbarPrefs.get()`, `lazy.BrowserUIUtils.getTrimmedURLPrefix()`, `selectedVal.includes()`, `selectedVal.startsWith()`, `this.getAttribute()`, `this.makeURIReadable()`, `uri.schemeIs()`
- 条件付き依存: `if (!selectedVal.includes("/"))` → `this.value.replace()`
- 条件付き依存: `if (!(this.getAttribute("pageproxystate") == "valid"))` → `URL.parse()`
- 条件付き依存: `if (!UrlbarPrefs.get("decodeURLsOnCopy") && !uri.schemeIs("data"))` → `URL.canParse()`
- 条件付き依存: `if (URL.canParse(selectedVal))` → `encodeURI()`
- 参照: `URL.parse(this._untrimmedValue)?.URI`, `result.payload.url`, `result?.autofill?.value`, `this.#isOpenedPageInBlankTargetLoading`, `this.#selectedText`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.editor.selection.rangeCount`, `this.selectionStart`, `this.value`, `this.valueIsTyped`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser.browsingContext .nonWebControlledLoadingURI`, `uri.displaySpec`

## UrlbarInputBase._toggleActionOverride()
- 位置: L3920-3940
- 役割: Shift、Alt、macOS は Meta、他は Control の押下を数え、押下中は action-override 属性を入力欄と結果パネルに付け、全て離れたら解除する。
- 触るとき: 修飾キーで結果の動作を変える(別タブなど)表示や挙動を調べるとき。
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 条件付き依存: `if (event.type == "keydown")` → `this.toggleAttribute()`
- 条件付き依存: `if (event.type == "keydown")` → `this.view.panel.toggleAttribute()`
- 条件付き依存: `if ( this._actionOverrideKeyCount && --this._actionOverrideKeyCount == 0 )` → `this._clearActionOverride()`
- 参照: `KeyEvent.DOM_VK_ALT`, `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_META`, `KeyEvent.DOM_VK_SHIFT`, `event.keyCode`, `event.type`, `this._actionOverrideKeyCount`

## UrlbarInputBase._clearActionOverride()
- 位置: L3942-3946
- 役割: 押下カウントを 0 に戻し、入力欄と結果パネルの action-override 属性を外す。
- 触るとき: 修飾キーを離しても動作の上書きが残るとき。
- 呼び出し先: `this.removeAttribute()`, `this.view.panel.removeAttribute()`
- 参照: `this._actionOverrideKeyCount`

## UrlbarInputBase._recordSearch()
- 位置: L3978-4005
- 役割: 検索のテレメトリ情報(エンジン ID、検索元、検索語、一時的な窓か、one-off か、新規タブのセッション ID)をまとめ、タブで開く場合は recordSearchInOpenedTab、それ以外は recordSearch に渡す。
- 触るとき: 検索のテレメトリや検索履歴の記録項目を追加、変更するとき。
- 呼び出し先: `this.getSearchSource()`, `this.view.oneOffSearchButtons?.eventTargetIsAOneOff()`, `where.startsWith()`
- 条件付き依存: `if (where.startsWith("tab"))` → `this.parentController.recordSearchInOpenedTab()`
- 条件付き依存: `if (!(where.startsWith("tab")))` → `this.parentController.recordSearch()`
- 参照: `engine.id`, `this._handoffSession`

## UrlbarInputBase._trimValue()
- 位置: L4015-4028
- 役割: アドレスバーで trimURLs が真なら BrowserUIUtils.trimURL で http や末尾のスラッシュを削る。ただし削ると RTL になる場合や混在コンテンツの取り消し線を出す場合は削らず元の値を返す。
- 触るとき: アドレスバーの表示で http や末尾スラッシュが消える、または消えないとき。
- 呼び出し先: `UrlbarContentUtils.isTextDirectionRTL()`, `UrlbarPrefs.get()`, `lazy.BrowserUIUtils.trimURL()`, `this.#getValueFormatter()`, `this.#getValueFormatter().willShowFormattedMixedContentProtocol()`
- 参照: `this.#isAddressbar`

## UrlbarInputBase._maybeCanonizeURL()
- 位置: L4041-4083
- 役割: キーボード操作で、URL らしくない単語だけの入力なら、locale の urlFixupSuffix を付けて URIFixup で補正し、補正後の値を入力欄にセットして返す。条件を満たさなければ null を返す。
- 触るとき: Enter で単語だけの入力が .com などの URL に補正される条件を変えるとき。
- 呼び出し先: `/^\s*[^.:\/\s]+(?:\/.*|\s*)$/i.test()`, `Services.uriFixup.getFixupURIInfo()`, `console.error()`, `suffix.endsWith()`, `this.controller.isCanonizeKeyboardEvent()`, `value.indexOf()`, `value.trim()`
- 条件付き依存: `if (firstSlash >= 0)` → `value.substring()`
- 参照: `Ci.nsIURIFixup.FIXUP_FLAGS_MAKE_ALTERNATE_URI`, `Services.locale.urlFixupSuffix`, `info.fixedURI.spec`, `this.value`
- XPCOM: [`nsIURIFixup`](../../../../docshell/base/nsIURIFixup.idl.md) / `Services.locale` / `Services.uriFixup`

## UrlbarInputBase._autofillValue()
- 位置: L4092-4119
- 役割: 自動補完の値を setValue で入れ、スクロールを先頭の端に合わせ、補完範囲を選択して、その内容を _autofillPlaceholder に保存する。
- 触るとき: 入力欄の補完文字列が入る位置や選択範囲、次の入力での再利用を調べるとき。
- 呼び出し先: `this.inputField.setSelectionRange()`, `this.setValue()`
- 参照: `this._autofillPlaceholder`, `this.inputField.scrollLeft`, `this.inputField.scrollLeftMin`

## UrlbarInputBase.#pickMenuResult()
- 位置: L4128-4174
- 役割: 結果メニューのコマンドを処理する。エンゲージメントを記録し、manage なら検索の設定画面を開き、help なら helpUrl、その他は要素の URL を開く。閉じてから #loadURL で読み込む(help は現在のタブなら新しいタブで開く)。
- 触るとき: 結果メニューの項目(ヘルプや設定など)を押したときの動作を変えるとき。
- 呼び出し先: `this.#loadURL()`, `this.controller.engagementEvent.record()`, `this.controller.whereToOpen()`, `this.getSearchSource()`, `this.view.close()`
- 条件付き依存: `if (element.dataset.command == "manage")` → `this.parentController.openPreferences()`
- 参照: `element.dataset.command`, `element.dataset.url`, `result.payload.helpUrl`, `result.source`, `result.type`, `this._lastSearchString`, `this.isPrivate`, `this.windowMode`

## UrlbarInputBase.#loadURL()
- 位置: async L4207-4300
- 役割: URL または検索を実際に読み込む。Enter のとき読み込みが終わるまで Enter 押下状態を保持し、アドレスバーで現在のタブならまず入力欄の値を書き換える。親の loadURL に渡し、結果が取り消し扱いなら handleRevert し、必要なら結果ビューを閉じる。
- 触るとき: URL の読み込み先、読み込み後の表示(入力欄の値、ビューを閉じるか)を変えるとき。
- 呼び出し先: `UrlbarShared.isInstance()`, `keyDownEnterDeferred?.resolve()`, `this.#notifyStartNavigation()`, `this.parentController.loadURL()`
- 条件付き依存: `if (!(loadRequest.engineSearch))` → `losslessDecodeURL()`
- 条件付き依存: `if (where == "current")` → `loadRequest.urlLoad?.url.startsWith()`
- 条件付き依存: `if (this.#isAddressbar && !params.avoidBrowserFocus)` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if (where != "current" && !this.isSearchbarSAP)` → `this.handleRevert()`
- 条件付き依存: `if (loadStatus.reverted)` → `this.handleRevert()`
- 条件付き依存: `if (!keepViewOpen)` → `this.view.close()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `event.keyCode`, `loadRequest.engineSearch`, `loadRequest.engineSearch.query`, `loadRequest.urlLoad`, `loadStatus.browserId`, `loadStatus.reverted`, `params.allowPinnedTabHostChange`, `params.allowPopups`, `params.allowThirdPartyFixup`, `params.avoidBrowserFocus`, `params.indicateErrorPageLoad`, `params.private`, `this.#isAddressbar`, `this._keyDownEnterDeferred`, `this._keyDownEnterDeferred.loadedContent`, `this.isPrivate`, `this.isSearchbarSAP`, `this.value`

## UrlbarInputBase._initCopyCutController()
- 位置: L4302-4313
- 役割: アドレスバーに一度だけコピー・カットのコントローラーを先頭に挿入する。他の入力欄は何もしない。
- 触るとき: アドレスバーでコピーされる URL が非トリミングの形で出ない、またはコントローラーが二重に入るとき。
- 呼び出し先: `this.inputField.controllers.insertControllerAt()`
- 参照: `this.#isAddressbar`, `this._copyCutController`

## UrlbarInputBase.#stripURI()
- 位置: L4322-4342
- 役割: 選択中の文字列を URI にして QueryStringStripper.stripForCopyOrShare で追跡用パラメータを除き、読める形に直して返す。失敗すれば元の URI を返す。
- 触るとき: 「リンクのクリーンコピー」で除去される対象や結果を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `console.warn()`, `lazy.QueryStringStripper.stripForCopyOrShare()`, `this._getSelectedValueForClipboard()`
- 条件付き依存: `if (strippedURI)` → `this.makeURIReadable()`
- 参照: `e.message`
- XPCOM: `Services.io`

## UrlbarInputBase.#isClipboardURIValid()
- 位置: L4349-4356
- 役割: コピーされる選択文字列が URL として解析できるかを返す。
- 触るとき: URL のコピー項目を表示するかどうかの条件を変えるとき。
- 呼び出し先: `URL.canParse()`, `this._getSelectedValueForClipboard()`

## UrlbarInputBase.#canStrip()
- 位置: L4363-4376
- 役割: コピーされる選択文字列に除去可能なパラメータがあるかを canStripForShare で判定する。解析できなければ false を返す。
- 触るとき: クリーンコピーが無効表示になる条件を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `console.warn()`, `lazy.QueryStringStripper.canStripForShare()`, `this._getSelectedValueForClipboard()`
- XPCOM: `Services.io`

## UrlbarInputBase.#maybeUntrimUrl()
- 位置: L4388-4463
- 役割: プロトコルや www を省いている値を、フォーカス中かつ全選択でないときに元の URL に戻し、カーソルや選択範囲を省いた分だけずらして補正する。moveCursorToStart が真なら先頭にカーソルを置く。
- 触るとき: 入力欄で省略された http や www が戻るタイミングや、戻った後の選択位置がずれるとき。
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

## UrlbarInputBase._initStripOnShare()
- 位置: L4467-4479
- 役割: 文脈メニューの copy の後に、リンクのクリーンコピー項目を登録する。開くたびに項目の表示状態を更新する。
- 触るとき: 文脈メニューのクリーンコピー項目の位置や表示条件を変えるとき。
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L4470-4474
- 役割: クリーンコピーの menuitem を1つ入れた DocumentFragment を作る。
- 触るとき: クリーンコピー項目を別の形で出したいとき。
- 呼び出し先: `fragment.appendChild()`, `this.#createStripOnShareItem()`, `this.document.createDocumentFragment()`

## onShowing()
- 位置: L4475-4477
- 役割: メニューを開くとクリーンコピー項目の表示状態を更新する。
- 触るとき: 項目が出るべきときに出ない、または逆のとき。
- 呼び出し先: `this.#updateStripOnShareItem()`

## UrlbarInputBase.#createStripOnShareItem()
- 位置: L4487-4504
- 役割: クリーンコピーの menuitem を作り、押されたら追跡用パラメータを除いた URL をクリップボードへコピーする。
- 触るとき: クリーンコピーの押下時にコピーされる値を調べるとき。
- 呼び出し先: `lazy.ClipboardHelper.copyString()`, `stripOnShare.addEventListener()`, `stripOnShare.setAttribute()`, `this.#stripURI()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`
- 参照: `stripOnShare.id`, `strippedURI.displaySpec`

## UrlbarInputBase.#updateStripOnShareItem()
- 位置: L4507-4528
- 役割: 機能が無効なら隠す。コピーが不可能、または URL でない場合も隠す。除去できるパラメータが無いなら無効にし、それ以外は有効にして表示する。
- 触るとき: クリーンコピー項目の隠れる、無効になる条件を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `controller.isCommandEnabled()`, `stripOnShare.removeAttribute()`, `this.#canStrip()`, `this.#isClipboardURIValid()`, `this.document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if (!UrlbarPrefs.get("privacy.query_stripping.strip_on_share.enabled"))` → `stripOnShare.setAttribute()`
- 条件付き依存: `if ( !controller.isCommandEnabled("cmd_copy") || !this.#isClipboardURIValid() )` → `stripOnShare.setAttribute()`
- 条件付き依存: `if (!this.#canStrip())` → `stripOnShare.setAttribute()`

## UrlbarInputBase._initPasteAndGo()
- 位置: L4530-4590
- 役割: 文脈メニューの paste の後に、貼り付けて移動の項目を登録する。押されたら検索開始を抑止し、選択して貼り付け、結果を解除してから handleCommand で移動する。
- 触るとき: 貼り付けて移動の項目の動作を変えるとき。
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L4533-4556
- 役割: 貼り付けて移動の menuitem を作り、ラベルを browser.properties から読んで入れた DocumentFragment を返す。
- 触るとき: 貼り付けて移動のラベルや項目の作りを変えるとき。
- 呼び出し先: `Services.strings .createBundle()`, `Services.strings .createBundle("chrome://browser/locale/browser.properties") .GetStringFromName()`, `fragment.appendChild()`, `pasteAndGo.addEventListener()`, `pasteAndGo.setAttribute()`, `this.document.createDocumentFragment()`, `this.document.createXULElement()`, `this.handleCommand()`, `this.parentController.clearLastQueryContextCache()`, `this.select()`, `this.setResultForCurrentValue()`, `this.window.goDoCommand()`
- 参照: `pasteAndGo.id`, `this._suppressStartQuery`
- XPCOM: `Services.strings`

## onShowing()
- 位置: L4557-4588
- 役割: 貼り付けて移動のメニューを開くときに結果ビューを閉じ、共有の文脈メニューに衝突マーカーを付ける(閉じたら外す)。クリップボードに貼り付け可能なものがあるかで項目の有効・無効を切り替える。
- 触るとき: 文脈メニューの貼り付けて移動が有効にならない、または結果ビューが勝手に閉じるとき。
- 呼び出し先: `controller.isCommandEnabled()`, `popup.addEventListener()`, `popup.setAttribute()`, `this.document.commandDispatcher.getControllerForCommand()`, `this.view.close()`
- 条件付き依存: `if (popup.state == "closed")` → `popup.removeAttribute()`
- 条件付き依存: `if (enabled)` → `pasteAndGo.removeAttribute()`
- 条件付き依存: `if (!(enabled))` → `pasteAndGo.setAttribute()`
- 参照: `popup.state`, `this.window.EditContextMenu.popup`

## UrlbarInputBase._initAutofillDismiss()
- 位置: L4594-4637
- 役割: 文脈メニューの select-all の後に、自動補完の「除外」と「履歴から削除」の項目と区切り線を登録する。
- 触るとき: 自動補完の除外や削除を文脈メニューから行う項目を追加・変更するとき。
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L4597-4628
- 役割: 区切り線、除外、履歴から削除の3つの要素を作り、それぞれの押下で #dismissAdaptiveAutofillFromContextMenu を呼ぶ DocumentFragment を返す。
- 触るとき: 除外や削除の項目の文言や押下時の動作を変えるとき。
- 呼び出し先: `dismiss.addEventListener()`, `dismiss.setAttribute()`, `forget.addEventListener()`, `forget.setAttribute()`, `fragment.append()`, `separator.setAttribute()`, `this.#dismissAdaptiveAutofillFromContextMenu()`, `this.document.createDocumentFragment()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`

## onShowing()
- 位置: L4629-4635
- 役割: メニューを開くたびに #autofillDismissContextMenuVisibility の結果で区切り線、除外、削除の hidden を設定する。
- 触るとき: 自動補完の項目がいつ出る・消えるかを調べるとき。
- 呼び出し先: `this.#autofillDismissContextMenuVisibility()`
- 参照: `dismiss.hidden`, `forget.hidden`, `separator.hidden`

## UrlbarInputBase.#autofillDismissContextMenuVisibility()
- 位置: L4651-4677
- 役割: 適応履歴の自動補完が有効で、ヒューリスティック結果が adaptive_url か adaptive_origin か origin の自動補完なら、除外は非プライベートのとき、削除は URL がオリジンでないときに表示すると判定する。それ以外は両方非表示。
- 触るとき: 除外や削除の項目が出る条件(種類、プライベート窓、深いリンクか)を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isOriginUrl()`
- 参照: `result.autofill`, `result.autofill.type`, `result.payload.url`, `result?.heuristic`, `this._resultForCurrentValue`, `this.isPrivate`

## UrlbarInputBase.#dismissAdaptiveAutofillFromContextMenu()
- 位置: async L4686-4702
- 役割: ヒューリスティックな自動補完結果を、指定の動作(除外か削除)で親に伝える。完了後、入力値を直前の検索語に戻し、自動補完なしで検索し直す。
- 触るとき: 除外や削除を押した後に入力欄の値や結果がどう戻るかを調べるとき。
- 呼び出し先: `this.parentController .dismissAutofill()`, `this.parentController .dismissAutofill(result.payload.url, action) .catch()`, `this.setValue()`, `this.startQuery()`
- 参照: `console.error`, `result.autofill`, `result.payload.url`, `result?.heuristic`, `this._lastSearchString`, `this._resultForCurrentValue`

## UrlbarInputBase.#initShareURL()
- 位置: L4708-4752
- 役割: macOS のアドレスバーだけに、共有、QR コード、リンクのクリーンコピーを含む共有グループを文脈メニューの select-all の後に登録する。
- 触るとき: macOS の共有メニューの項目や並びを変えるとき。
- 呼び出し先: `this.addContextMenuItems()`

## createItems()
- 位置: L4711-4734
- 役割: 区切り線、共有(Mac の共有ピッカー)、QR コード、クリーンコピーの項目を並べた DocumentFragment を作る。
- 触るとき: macOS の共有グループの項目構成を変えるとき。
- 呼び出し先: `fragment.appendChild()`, `lazy.SharingUtils.shareOnMacPicker()`, `lazy.SharingUtils.showQRCode()`, `qrCodeItem.addEventListener()`, `qrCodeItem.classList.add()`, `shareItem.addEventListener()`, `shareItem.classList.add()`, `this.#createStripOnShareItem()`, `this.document.createDocumentFragment()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`
- 参照: `qrCodeItem.id`

## onShowing()
- 位置: L4735-4750
- 役割: メニューを開くたびに、クリーンコピーの状態を更新し、選択中ブラウザの URL を共有対象として両項目に設定する。共有可能かどうかで項目を無効にし、QR コードは browser.shareqrcode.enabled で表示を切り替える。
- 触るとき: 共有項目が無効になる、または QR コードが出ない条件を調べるとき。
- 呼び出し先: `Cu.getWeakReference()`, `Services.prefs.getBoolPref()`, `lazy.SharingUtils.getLinkToShare()`, `qrCodeItem.toggleAttribute()`, `shareItem.toggleAttribute()`, `this.#updateStripOnShareItem()`
- 参照: `lazy.SharingUtils.getLinkToShare(shareItem).urlToShare`, `qrCodeItem.contextBrowserToShare`, `qrCodeItem.hidden`, `shareItem.browsersToShare`, `shareItem.contextBrowserToShare`, `this.window.gBrowser?.selectedBrowser`
- XPCOM: `Services.prefs`

## UrlbarInputBase.#notifyStartNavigation()
- 位置: L4764-4771
- 役割: アドレスバーでだけ urlbar-user-start-navigation を監視者に通知する。
- 触るとき: ナビゲーション開始を監視する仕組みに影響するかを確かめるとき。
- 条件付き依存: `if (this.#isAddressbar)` → `Services.obs.notifyObservers()`
- 参照: `this.#isAddressbar`
- XPCOM: `Services.obs`

## UrlbarInputBase._searchModeForResult()
- 位置: L4785-4839
- 役割: 結果のキーワードやエンジンから検索モードの設定を作る。キーワードに対応する検索モードがなければエンジン名を使い、制限の種類と入り口(topsites_urlbar、tabtosearch、keywordoffer など)を付ける。作れなければ null を返す。
- 触るとき: 結果を選んだときに検索モードへ入る条件や入り口の記録を変えるとき。
- 呼び出し先: `this.searchModeForToken()`
- 条件付き依存: `if (!(result.type == UrlbarShared.RESULT_TYPE.RESTRICT))` → `UrlbarShared.SEARCH_MODE_RESTRICT.has()`
- 参照: `UrlbarShared.RESULT_TYPE.RESTRICT`, `result.payload.dynamicType`, `result.payload.engine`, `result.payload.keyword`, `result.payload.originalEngine`, `result.providerName`, `result.type`, `searchMode.entry`, `searchMode.restrictType`, `this.view.selectedElement.dataset.engine`, `this.view.selectedElement.dataset?.engine`, `this.view.selectedElement?.dataset.engine`

## UrlbarInputBase._updateSearchModeUI()
- 位置: L4847-4915
- 役割: 検索モードの表示を更新する。モードを抜けるなら searchmode 属性と placeholder を戻す。入るならエンジン名または結果の種類を見出しに出し、プレースホルダーを切り替える。固定ページの値は消し、自動補完を外す。
- 触るとき: 検索モードの見出しやプレースホルダーの文言、または入った時の値の扱いを変えるとき。
- 呼び出し先: `lazy?.UrlbarSearchTermsPersistence.onSearchModeChanged()`, `this.dispatchEvent()`, `this.getAttribute()`, `this.hasAttribute()`, `this.toggleAttribute()`
- 条件付き依存: `if (this._searchModeIndicatorTitle)` → `this._searchModeIndicatorTitle.removeAttribute()`
- 条件付き依存: `if (!engineName && !source)` → `this.removeAttribute()`
- 条件付き依存: `if (!engineName && !source)` → `this.updatePlaceholder()`
- 条件付き依存: `if (engineName)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (source)` → `UrlbarShared.getResultSourceName()`
- 条件付き依存: `if (this._searchModeIndicatorTitle)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (source)` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (this.getAttribute("pageproxystate") == "valid")` → `this.setPageProxyState()`
- 参照: `this.#navigationEnabled`, `this._autofillPlaceholder`, `this._searchModeIndicatorTitle`, `this._searchModeIndicatorTitle.textContent`, `this.inputField`, `this.userTypedValue`, `this.value`, `this.window`

## UrlbarInputBase.#handlePersistedSearchTerms()
- 位置: L4935-5002
- 役割: 永続検索語が有効なときだけ、ブラウザごとの状態から永続の判定を行い、必要なら検索語を入力欄の値にする。永続しなくなったら入力値を外す。永続の表示状態と計測も更新する。
- 触るとき: 検索結果ページで入力欄に検索語が残る、または消える条件を調べるとき。
- 呼び出し先: `lazy.UrlbarSearchTermsPersistence.shouldPersist()`, `lazy.UrlbarUtils.isPersistedSearchTermsEnabled()`, `state.persist.originalURI.equals()`, `this.toggleAttribute()`
- 条件付き依存: `if (state.persist)` → `this.removeAttribute()`
- 条件付き依存: `if (firstView || cachedUriDidChange)` → `lazy.UrlbarSearchTermsPersistence.setPersistenceState()`
- 条件付き依存: `if (state.persist.shouldPersist && !isSameDocument)` → `Glean.urlbarPersistedsearchterms.viewCount.add()`
- 参照: `state.persist`, `state.persist.searchTerms`, `state.persist.shouldPersist`, `state.persist?.originalURI`, `state.persist?.shouldPersist`, `this.userTypedValue`, `this.window.gBrowser.currentURI`, `this.window.gBrowser.selectedBrowser.originalURI`

## UrlbarInputBase.#initPlaceholderFromPref()
- 位置: L5011-5022
- 役割: navigation が有効で、エンジンストアが失敗していなければ、保存された placeholderName の pref からエンジン名を読み、プレースホルダーに使う。
- 触るとき: 起動直後にプレースホルダーのエンジン名が一時的に空になる、または古い名前が出るとき。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (engineName)` → `this._setPlaceholder()`
- 参照: `this.#navigationEnabled`, `this.controller.engineStore.failed`, `this.isPrivate`

## UrlbarInputBase.#initEngineStoreAfterPaint()
- 位置: async L5035-5044
- 役割: 文書が読み込み中なら DOMContentLoaded の後、idle callback を待ってから engineStore.init を呼ぶ。起動時の検索サービス初期化を描画後まで遅らせる。
- 触るとき: 起動時の検索サービスの初期化タイミングや、描画後の遅延を変えるとき。
- 呼び出し先: `this.controller.engineStore.init()`
- 条件付き依存: `if (document.readyState == "loading")` → `document.addEventListener()`
- 条件付き依存: `if (document.readyState == "loading")` → `this.window.requestIdleCallback()`
- 参照: `document.readyState`

## UrlbarInputBase.#deferUpdatePlaceholder()
- 位置: async L5056-5099
- 役割: smartbar 以外で、値が空ならプレースホルダーを更新し、入力か TabSelect の最初の時点で検索アイコンとプレースホルダーを更新するリスナーを付ける。値があれば即座に updatePlaceholder を呼ぶ。
- 触るとき: 起動直後のプレースホルダーや検索アイコンの更新がいつ行われるかを調べるとき。
- 条件付き依存: `if (this.inputField.dataset.l10nId == "urlbar-placeholder-with-name")` → `this.updatePlaceholder()`
- 条件付き依存: `if (!this.value)` → `this.inputField.addEventListener()`
- 条件付き依存: `if (!this.value)` → `tabContainer?.addEventListener()`
- 条件付き依存: `if (!(!this.value))` → `this.updatePlaceholder()`
- 参照: `this.#isAddressbar`, `this.inputField.dataset.l10nId`, `this.sapName`, `this.value`, `this.window.gBrowser.tabContainer`

## updateListener()
- 位置: L5081-5092
- 役割: 入力されるか、タブが切り替わった時点で、検索モードでなければ検索アイコンとプレースホルダーを更新し、自分を外す。
- 触るとき: 入力後や別タブへ切り替えた後にプレースホルダーが更新されないとき。
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.searchModeSwitcher.updateSearchIcon().catch()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.searchModeSwitcher.updateSearchIcon()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.updatePlaceholder()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `this.inputField.removeEventListener()`
- 条件付き依存: `if (this.value && !this.searchMode)` → `tabContainer?.removeEventListener()`
- 参照: `console.error`, `this.searchMode`, `this.value`

## UrlbarInputBase.setUnifiedSearchButtonAvailability()
- 位置: L5106-5123
- 役割: 統合検索ボタンの表示可否を設定する。検索窓か unifiedSearchButton.always の設定なら常に可能にし、オフスクリーンと aria-hidden を切り替える。アドレスバーではタブごとの状態にも保存する。
- 触るとき: 統合検索ボタンが出ない、またはタブごとに戻らないとき。
- 呼び出し先: `UrlbarPrefs.get()`, `switcher.toggleAttribute()`, `this.querySelector()`
- 条件付き依存: `if (available)` → `switcher.removeAttribute()`
- 条件付き依存: `if (!(available))` → `switcher.setAttribute()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 参照: `this.#isAddressbar`, `this.getBrowserState( this.window.gBrowser.selectedBrowser ).isUnifiedSearchButtonAvailable`, `this.isSearchbarSAP`, `this.window.gBrowser.selectedBrowser`

## UrlbarInputBase.updatePlaceholder()
- 位置: L5128-5143
- 役割: 検索モードでなく navigation が有効なら、既定エンジンが設定エンジンならその名前、それ以外は名前なしのプレースホルダーを設定する。
- 触るとき: 既定エンジンを変えたときにプレースホルダーの名前が変わらないとき。
- 条件付き依存: `if (defaultEngine?.isConfigEngine)` → `this._setPlaceholder()`
- 条件付き依存: `if (!(defaultEngine?.isConfigEngine))` → `this._setPlaceholder()`
- 参照: `defaultEngine.name`, `defaultEngine?.isConfigEngine`, `this.#navigationEnabled`, `this.controller.engineStore.default`, `this.searchMode`

## UrlbarInputBase._setPlaceholder()
- 位置: L5152-5174
- 役割: navigation が無効なら searchbar-input を使う。キーワードが有効なら、名前ありか無しかで urlbar-placeholder-with-name か urlbar-placeholder を選び、無効なら keyword-disabled の文言を使って l10n 属性を設定する。
- 触るとき: プレースホルダーの文言を変えるとき、またはキーワードの有効・無効で表示が変わる仕組みを調べるとき。
- 呼び出し先: `UrlbarShared.keywordEnabled()`, `this.document.l10n.setAttributes()`
- 条件付き依存: `if (!this.#navigationEnabled)` → `this.document.l10n.setAttributes()`
- 参照: `this.#navigationEnabled`, `this.#sapName`, `this.inputField`

## UrlbarInputBase.#maybeSelectAll()
- 位置: L5186-5195
- 役割: クリックで、既にフォーカスがなく、変換中でなく、選択が空のときだけ全選択する。
- 触るとき: クリック時の全選択の条件を変えるとき。
- 条件付き依存: `if ( !this.#preventClickSelectsAll && this.#compositionState != UrlbarShared.COMPOSITION.COMPOSING && this.focused && this.inputField.selectionStart == this.inpu...)` → `this.select()`
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionState`, `this.#preventClickSelectsAll`, `this.focused`, `this.inputField.selectionEnd`, `this.inputField.selectionStart`

## UrlbarInputBase._on_command()
- 位置: L5199-5211
- 役割: コマンド実行によるフォーカス移動をエンゲージメントの放棄とみなさないよう、結果メニュー項目や one-off からの検索モード入りなら記録を捨てずに残す。それ以外は記録を捨てる。
- 触るとき: 結果メニューや one-off を押したときに放棄として記録されてしまうとき。
- 呼び出し先: `event.target.classList.contains()`
- 条件付き依存: `if ( !event.target.classList.contains("urlbarView-result-menuitem") && (!event.target.classList.contains("searchbar-engine-one-off-item") || this.searchMode?.ent...)` → `this.controller.engagementEvent.discard()`
- 参照: `this.searchMode?.entry`

## UrlbarInputBase._on_blur()
- 位置: L5213-5295
- 役割: フォーカスを外れたときの後始末。結果メニューが開いていれば何もしない。エンゲージメントを記録し、フォーカス関連の状態を消し、入力値を入力中の文字列か元の URL に戻し、補完や操作の上書きを解除し、結果ビューを閉じ、Enter の保留を解く。
- 触るとき: 入力欄から離れた後に値や結果ビューがどう戻るかを調べるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `lazy?.ExtensionSearchHandler.hasActiveInputSession()`, `logger()`, `logger().debug()`, `this._clearActionOverride()`, `this._resetSearchState()`, `this.controller.engagementEvent.record()`, `this.getAttribute()`, `this.getSearchSource()`, `this.removeAttribute()`, `this.view.isResultMenuOpen()`
- 条件付き依存: `if (!( this.value == this._untrimmedValue && !this.userTypedValue && !this.focused ))` → `this.formatValue()`
- 条件付き依存: `if (lazy?.ExtensionSearchHandler.hasActiveInputSession())` → `lazy.ExtensionSearchHandler.handleInputCancelled()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") != "valid" && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 条件付き依存: `if (this._keyDownEnterDeferred)` → `this._keyDownEnterDeferred.resolve()`
- 条件付き依存: `if (typeof ChromeUtils != "undefined")` → `Services.obs.notifyObservers()`
- 参照: `this.#preventClickSelectsAll`, `this._autofillPlaceholder`, `this._handoffSession`, `this._isHandoffSession`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._lastSearchString`, `this._untrimmedValue`, `this.focused`, `this.focusedViaMousedown`, `this.userTypedValue`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`, `this.windowMode`
- XPCOM: `Services.obs`

## UrlbarInputBase._on_click()
- 位置: L5297-5328
- 役割: 入力欄かそのコンテナのクリックで全選択と URL の再整形を行い、検索モード解除ボタンなら検索モードを外して結果があれば検索し直し、戻すボタンなら handleRevert、Go ボタンなら handleCommand を呼ぶ。
- 触るとき: 入力欄や周辺ボタンのクリックで起きる動作を変えるとき。
- 呼び出し先: `this.#maybeSelectAll()`, `this.#maybeUntrimUrl()`, `this.handleCommand()`, `this.handleRevert()`, `this.select()`
- 条件付き依存: `if (this.view.isOpen)` → `this.startQuery()`
- 参照: `event.button`, `event.target`, `this._inputContainer`, `this._revertButton`, `this._searchModeIndicatorClose`, `this.goButton`, `this.inputField`, `this.searchMode`, `this.view.isOpen`, `this.view.oneOffSearchButtons`, `this.view.oneOffSearchButtons.selectedButton`

## UrlbarInputBase._on_auxclick()
- 位置: L5330-5342
- 役割: 中ボタンなどの補助クリックで、入力欄なら全選択と URL の再整形、Go ボタンなら handleCommand を呼ぶ。
- 触るとき: 中ボタンクリックの挙動を変えるとき。
- 呼び出し先: `this.#maybeSelectAll()`, `this.#maybeUntrimUrl()`, `this.handleCommand()`
- 参照: `event.target`, `this._inputContainer`, `this.goButton`, `this.inputField`

## UrlbarInputBase._on_contextmenu()
- 位置: L5344-5351
- 役割: マウス操作による文脈メニューの表示時だけ、全選択を試みる。キーボードでの表示では何もしない。
- 触るとき: 右クリックで全選択される条件を変えるとき。
- 呼び出し先: `this.#maybeSelectAll()`
- 参照: `event.button`

## UrlbarInputBase._on_focus()
- 位置: L5353-5426
- 役割: フォーカスを受けたとき、focused 属性を付け、トリムされた URL を必要なら元に戻す判定を行い、マウス由来なら結果ビューを自動で開き、キー操作ならすぐに再整形する。ツールチップ、装飾、ポップアップ通知を更新する。
- 触るとき: フォーカス時に URL が元に戻る条件、または結果ビューの自動表示を変えるとき。
- 呼び出し先: `logger()`, `logger().debug()`, `this._updateUrlTooltip()`, `this.formatValue()`, `this.getAttribute()`
- 条件付き依存: `if (!this._hideFocus)` → `this.toggleAttribute()`
- 条件付き依存: `if (!untrim)` → `UrlbarContentUtils.getFixupPrimitives()`
- 条件付き依存: `if (fixedDisplaySpec)` → `UrlbarContentUtils.getDisplaySpec()`
- 条件付き依存: `if (!(expectedDisplaySpec == null))` → `UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (!(expectedDisplaySpec == null))` → `this._untrimmedValue.startsWith()`
- 条件付き依存: `if ( UrlbarPrefs.getScotchBonnetPref("trimHttps") && this._untrimmedValue.startsWith("https://") )` → `fixedDisplaySpec.replace()`
- 条件付き依存: `if (untrim)` → `this.setValue()`
- 条件付き依存: `if (this.focusedViaMousedown)` → `this.view.autoOpen()`
- 条件付き依存: `if (this._untrimOnFocusAfterKeydown)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (!(this.focusedViaMousedown))` → `this.inputField.hasAttribute()`
- 条件付き依存: `if (this.inputField.hasAttribute("refocused-by-panel"))` → `this.#maybeSelectAll()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") != "valid" && this.window.UpdatePopupNotificationsVisibility )` → `this.window.UpdatePopupNotificationsVisibility()`
- 条件付き依存: `if (typeof ChromeUtils != "undefined")` → `Services.obs.notifyObservers()`
- 参照: `UrlbarContentUtils.getFixupPrimitives( this.value, this.isPrivate )?.preferredURIDisplaySpec`, `this.#isAddressbar`, `this._hideFocus`, `this._protocolIsTrimmed`, `this._untrimOnFocusAfterKeydown`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.focusedViaMousedown`, `this.isPrivate`, `this.value`, `this.window.UpdatePopupNotificationsVisibility`
- XPCOM: `Services.obs`

## UrlbarInputBase._on_mouseover()
- 位置: L5428-5430
- 役割: マウスが載ったときにツールチップを更新する。
- 触るとき: あふれた URL のツールチップの出方を調べるとき。
- 呼び出し先: `this._updateUrlTooltip()`

## UrlbarInputBase._on_draggableregionleftmousedown()
- 位置: L5432-5436
- 役割: Windows で、ドラッグ領域を左クリックしたとき、自動非表示が有効なら結果ビューを閉じる。
- 触るとき: タイトルバー付近の操作で結果ビューが閉じない、または閉じすぎるとき。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`

## UrlbarInputBase._on_mousedown()
- 位置: L5438-5513
- 役割: 入力欄や window へのマウス押下を処理する。入力欄の押下ではマウス由来のフォーカスを記録し、左クリックなら選択を消して結果ビューを自動表示する。window 側の押下では、タブ以外なら自動非表示のときに結果ビューを閉じ、閉じる前に放棄のエンゲージメントを記録する。
- 触るとき: クリックで結果ビューが開く・閉じる条件や、放棄の記録のタイミングを変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `event.target.closest()`, `this.hasAttribute()`, `this.view.autoOpen()`
- 条件付き依存: `if (event.target != this.inputField)` → `this.focus()`
- 条件付き依存: `if (this.focusedViaMousedown)` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.hasAttribute()`
- 条件付き依存: `if (this.view.isOpen && !this.hasAttribute("focused"))` → `this.controller.engagementEvent.record()`
- 条件付き依存: `if (this.view.isOpen && !this.hasAttribute("focused"))` → `this.getSearchSource()`
- 条件付き依存: `if (!UrlbarPrefs.get("ui.popup.disable_autohide"))` → `this.view.close()`
- 参照: `event.button`, `event.currentTarget`, `event.target`, `this.#preventClickSelectsAll`, `this._inputContainer`, `this._lastSearchString`, `this._mousedownOnUrlbarDescendant`, `this.focused`, `this.focusedViaMousedown`, `this.inputField`, `this.inputField.parentNode`, `this.view.isOpen`, `this.window`, `this.windowMode`

## UrlbarInputBase._on_input()
- 位置: L5515-5642
- 役割: 入力で起きる検索の中心。自動補完の削除を記録し、入力値を未加工の値と入力値として保存し、構成の状態を整える。IME 変換中は検索を止め、それ以外は自動補完を判定して startQuery で検索を始める。
- 触るとき: 文字を入力したときに検索が始まらない、補完が出ない、IME 変換中の挙動が変なとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isPasteEvent()`, `event.inputType?.startsWith()`, `this._maybeAutofillPlaceholder()`, `this.getAttribute()`, `this.removeAttribute()`, `this.startQuery()`, `this.toggleAttribute()`, `this.view.removeAccessibleFocus()`
- 条件付き依存: `if ( this._autofillPlaceholder && this.value === this.userTypedValue && (event.inputType === "deleteContentBackward" || event.inputType === "deleteContentForward") )` → `this.parentController.recordAutofillDeletion()`
- 条件付き依存: `if ( UrlbarPrefs.get("autoFill.adaptiveHistory.enabled") && event.inputType?.startsWith("deleteContent") && !this.isPrivate && this._autofillPlaceholder && this....)` → `this.parentController.recordAutofillBackspace()`
- 条件付き依存: `if ( this.getAttribute("pageproxystate") == "valid" && this.value != this._lastValidURLStr )` → `this.setPageProxyState()`
- 条件付き依存: `if (this.#isAddressbar)` → `this.getBrowserState()`
- 条件付き依存: `if ( state.persist?.shouldPersist && this.value !== state.persist.searchTerms )` → `this.removeAttribute()`
- 条件付き依存: `if (this.view.isOpen)` → `this.view.maybeRollupPopups()`
- 条件付き依存: `if (this.view.isOpen)` → `UrlbarPrefs.get()`
- 条件付き依存: `if (!value && !UrlbarPrefs.get("suggest.topsites"))` → `this.view.clear()`
- 条件付き依存: `if (!this.searchMode || !this.view.oneOffSearchButtons?.hasView)` → `this.view.close()`
- 条件付き依存: `if (!(this.view.isOpen))` → `this.view.clear()`
- 参照: `UrlbarShared.COMPOSITION.CANCELED`, `UrlbarShared.COMPOSITION.COMPOSING`, `UrlbarShared.COMPOSITION.NONE`, `event.data`, `event.inputType`, `state.persist.searchTerms`, `state.persist.shouldPersist`, `state.persist?.shouldPersist`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this.#inputEpoch`, `this.#isAddressbar`, `this._autofillPlaceholder`, `this._lastValidURLStr`, `this._protocolIsTrimmed`, `this._resultForCurrentValue`, `this._resultForCurrentValue.payload.url`, `this._resultForCurrentValue?.payload?.url`, `this._untrimmedValue`, `this._wwwIsTrimmed`, `this.controller.userSelectionBehavior`, `this.isPrivate`, `this.searchMode`, `this.userTypedValue`, `this.value`, `this.valueIsTyped`, `this.view.isOpen`, `this.view.oneOffSearchButtons?.hasView`, `this.window.gBrowser.selectedBrowser`

## UrlbarInputBase._on_selectionchange()
- 位置: L5644-5657
- 役割: 自動補完のプレースホルダーが選択を外されたら、その補完を入力値として確定し、ユーザー入力の値にする。
- 触るとき: 補完された文字をカーソル移動で編集したときに補完が確定しない、または残るとき。
- 参照: `this._autofillPlaceholder`, `this._autofillPlaceholder.selectionEnd`, `this._autofillPlaceholder.selectionStart`, `this._autofillPlaceholder.value`, `this.selectionEnd`, `this.selectionStart`, `this.userTypedValue`, `this.value`

## UrlbarInputBase._on_select()
- 位置: L5659-5693
- 役割: ユーザーの選択をプライマリ選択へコピーする。プログラムによる選択、またはプライマリ選択に対応していない環境では何もしない。
- 触るとき: 選択したテキストが中クリックで貼られる内容(プライマリ選択)を調べるとき。
- 呼び出し先: `Services.clipboard.isClipboardTypeSupported()`, `lazy.ClipboardHelper.copyStringToClipboard()`, `this._getSelectedValueForClipboard()`
- 参照: `Services.clipboard.kSelectionClipboard`, `this._suppressPrimaryAdjustment`, `this.window.windowUtils.isHandlingUserInput`
- XPCOM: `Services.clipboard`

## UrlbarInputBase._on_overflow()
- 位置: L5695-5698
- 役割: 文字があふれたことを記録し、テキストのあふれ表示を更新する。
- 触るとき: 長い URL のあふれ表示が出ない、または残るとき。
- 呼び出し先: `this.updateTextOverflow()`
- 参照: `this._overflowing`

## UrlbarInputBase._on_underflow()
- 位置: L5700-5704
- 役割: あふれの解消を記録し、テキストのあふれ表示とツールチップを更新する。
- 触るとき: あふれ表示やツールチップが解消されないとき。
- 呼び出し先: `this._updateUrlTooltip()`, `this.updateTextOverflow()`
- 参照: `this._overflowing`

## UrlbarInputBase._on_paste()
- 位置: L5706-5757
- 役割: 貼り付けた文字列をサニタイズし、元の内容と違えばイベントを止めて、貼り付けた値を入力欄へ入れ直す。カーソルを貼り付け後へ移し、検索を始める。先頭に空でない文字がある場合は何もしない。
- 触るとき: URL を貼り付けたときに値が書き換わる、または書き換わらない条件を調べるとき。
- 呼び出し先: `UrlbarContentUtils.getFixupPrimitives()`, `UrlbarShared.sanitizeTextFromClipboard()`, `event.clipboardData.getData()`, `oldStart.trim()`, `oldValue.substring()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `event.preventDefault()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `event.stopImmediatePropagation()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.setValue()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("pageproxystate") == "valid")` → `this.setPageProxyState()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.toggleAttribute()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if (originalPasteData != pasteData)` → `this.startQuery()`
- 参照: `oldStart.length`, `pasteData.length`, `this._untrimmedValue`, `this.isPrivate`, `this.selectionEnd`, `this.selectionStart`, `this.userTypedValue`, `this.value`

## UrlbarInputBase.#makeQueryContext()
- 位置: L5773-5823
- 役割: 検索のクエリ文脈を作る。検索モードのときはその元とソースを設定し、ブラウザ窓では利用者のコンテキスト ID、タブグループ、現在のページを加える。貼り付け時は長すぎる文字列でリモート結果を止める。結果件数は maxRichResults(アクション検索では無制限の 99)。
- 触るとき: 検索の結果件数、リモート候補の可否、現在のページ情報などクエリの条件を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.isPasteEvent()`
- 条件付き依存: `if (this.window.gBrowser)` → `parseInt()`
- 条件付き依存: `if (this.window.gBrowser)` → `this.window.gBrowser.selectedBrowser?.getAttribute()`
- 条件付き依存: `if (this.searchMode)` → `UrlbarPrefs.get()`
- 参照: `UrlbarShared.RESULT_SOURCE.ACTIONS`, `event.data?.length`, `options.currentPage`, `options.searchMode`, `options.sources`, `options.tabGroup`, `options.userContextId`, `this.isPrivate`, `this.sapName`, `this.searchMode`, `this.searchMode.source`, `this.searchMode?.source`, `this.window.gBrowser`, `this.window.gBrowser.currentURI?.spec`, `this.window.gBrowser.selectedTab.group?.id`

## UrlbarInputBase._on_scrollend()
- 位置: L5825-5827
- 役割: スクロールが終わったら、テキストのあふれ表示を更新する。
- 触るとき: スクロール後のあふれ表示の向きが合わないとき。
- 呼び出し先: `this.updateTextOverflow()`

## UrlbarInputBase._on_TabSelect()
- 位置: L5829-5835
- 役割: タブ切り替えの通知を受け、キー操作による全展開(untrim)の予定を取り消してから、タブ切り替えとフォーカス変化の後処理を呼ぶ。
- 触るとき: タブ切り替え時に結果ビューや入力欄の値が戻るタイミングを調べるとき。
- 呼び出し先: `this._afterTabSelectAndFocusChange()`
- 参照: `this._gotTabSelect`, `this._untrimOnFocusAfterKeydown`

## UrlbarInputBase._on_TabClose()
- 位置: L5837-5846
- 役割: 閉じたタブのバウンス計測を送り、結果ビューが開いていれば検索を始め直して、閉じたタブへの切り替え候補を消す。
- 触るとき: タブを閉じた後も切り替え候補が残るとき。
- 呼び出し先: `lazy.handleBounceEventTrigger()`
- 条件付き依存: `if (this.view.isOpen)` → `this.startQuery()`
- 参照: `event.target.linkedBrowser`, `this.view.isOpen`

## UrlbarInputBase._on_beforeinput()
- 位置: L5848-5857
- 役割: Enter 処理中の文字入力を止め、スペースで結果メニューが開く場合はスペースの入力を止める。
- 触るとき: Enter や Space を押したときに文字が入ってしまう、または入らないとき。
- 呼び出し先: `this.view.shouldSpaceActivateSelectedElement()`
- 条件付き依存: `if ( // Ignore char key input while processing enter key. (event.data && this._keyDownEnterDeferred) || // Ignore space key while the result menu will be activat...)` → `event.preventDefault()`
- 参照: `event.data`, `this._keyDownEnterDeferred`

## UrlbarInputBase._on_keydown()
- 位置: L5859-5925
- 役割: キーダウンを処理する。結果メニューが開いていれば何もしない。Enter なら遅延用の Promise を作って修飾キーの状態を記録し、修飾キーの押下を追跡し、イベントの遅延を経て controller.handleKeyNavigation に渡す。
- 触るとき: キー操作(矢印、Enter、Tab など)で結果が選ばれない、または二重に動くとき。
- 呼び出し先: `this.controller.handleKeyNavigation()`, `this.eventBufferer.maybeDeferEvent()`, `this.eventBufferer.shouldDeferEvent()`, `this.view.isResultMenuOpen()`
- 条件付き依存: `if (this._keyDownEnterDeferred)` → `this._keyDownEnterDeferred.reject()`
- 条件付き依存: `if (event.keyCode === KeyEvent.DOM_VK_RETURN)` → `Promise.withResolvers()`
- 条件付き依存: `if (event.keyCode === KeyEvent.DOM_VK_RETURN)` → `UrlbarContentUtils.getPlatform()`
- 条件付き依存: `if (!event.repeat)` → `this._toggleActionOverride()`
- 条件付き依存: `if (this.eventBufferer.shouldDeferEvent(event))` → `this.controller.handleKeyNavigation()`
- 参照: `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_LEFT`, `KeyEvent.DOM_VK_META`, `KeyEvent.DOM_VK_RETURN`, `event._disableCanonization`, `event.ctrlKey`, `event.currentTarget`, `event.keyCode`, `event.metaKey`, `event.repeat`, `event.shiftKey`, `this.#allTextSelected`, `this.#allTextSelectedOnKeyDown`, `this.#inputEpoch`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._keyDownEnterDeferred.inputEpoch`, `this._untrimOnFocusAfterKeydown`, `this.focused`, `this.window`

## UrlbarInputBase._on_keyup()
- 位置: L5927-5962
- 役割: キーアップを処理する。全選択されていた場合は Home 押下でカーソルを先頭に置き、URL を再整形する。修飾キーの状態を解除し、Enter の遅延処理が残っていれば #finishDeferredEnter を呼ぶ。
- 触るとき: Enter の後の読み込みや修飾キー解除の順序を調べるとき。
- 呼び出し先: `this._toggleActionOverride()`
- 条件付き依存: `if (this.#allTextSelectedOnKeyDown)` → `this.#isHomeKeyUpEvent()`
- 条件付き依存: `if (this.#allTextSelectedOnKeyDown)` → `this.#maybeUntrimUrl()`
- 条件付き依存: `if (this._keyDownEnterDeferred && !this._finishingDeferredEnter)` → `this.#finishDeferredEnter()`
- 参照: `KeyEvent.DOM_VK_CONTROL`, `KeyEvent.DOM_VK_META`, `event.currentTarget`, `event.keyCode`, `this.#allTextSelectedOnKeyDown`, `this._finishingDeferredEnter`, `this._isKeyDownWithCtrl`, `this._isKeyDownWithMeta`, `this._isKeyDownWithMetaAndLeft`, `this._keyDownEnterDeferred`, `this._untrimOnFocusAfterKeydown`, `this.selectionEnd`, `this.selectionStart`, `this.window`

## UrlbarInputBase.#finishDeferredEnter()
- 位置: async L5968-6009
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (keyDownEnterDeferred.loadedContent)` → `this.parentController.focusBrowser()`
- 条件付き依存: `if ( this.#isAddressbar && focused && keyDownEnterDeferred.inputEpoch === this.#inputEpoch )` → `this.inputField.setSelectionRange()`
- 条件付き依存: `if (!(keyDownEnterDeferred.loadedContent))` → `keyDownEnterDeferred.resolve()`
- 参照: `keyDownEnterDeferred.inputEpoch`, `keyDownEnterDeferred.loadedContent`, `keyDownEnterDeferred.promise`, `this.#inputEpoch`, `this.#isAddressbar`, `this._finishingDeferredEnter`, `this._keyDownEnterDeferred`

## UrlbarInputBase.isComposing()
- 位置: L6017-6019
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionState`

## UrlbarInputBase._on_compositionstart()
- 位置: L6021-6051
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (this.searchMode)` → `this.confirmSearchMode()`
- 条件付き依存: `if (this.view.isOpen)` → `this.view.close()`
- 参照: `UrlbarShared.COMPOSITION.COMPOSING`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this.searchMode`, `this.userTypedValue`, `this.value`, `this.view.isOpen`

## UrlbarInputBase._on_compositionend()
- 位置: L6053-6086
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!UrlbarPrefs.get("keepPanelOpenDuringImeComposition"))` → `this.view.clearSelection()`
- 条件付き依存: `if ( !event.data && !this.#compositionHadText && this.#compositionClosedPopup && !UrlbarPrefs.get("keepPanelOpenDuringImeComposition") )` → `this.startQuery()`
- 参照: `UrlbarShared.COMPOSITION.CANCELED`, `UrlbarShared.COMPOSITION.COMMIT`, `UrlbarShared.COMPOSITION.COMPOSING`, `UrlbarShared.COMPOSITION.NONE`, `event.data`, `this.#compositionClosedPopup`, `this.#compositionHadText`, `this.#compositionState`, `this._resultForCurrentValue`

## UrlbarInputBase._on_dragstart()
- 位置: L6088-6124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.escapeHtmlEntities()`, `event.dataTransfer.setData()`, `event.stopPropagation()`, `this.getAttribute()`, `this.inputField.compareDocumentPosition()`, `this.makeURIReadable()`, `this.view.close()`
- 参照: `Node.DOCUMENT_POSITION_CONTAINED_BY`, `event.dataTransfer.effectAllowed`, `event.originalTarget`, `event.target`, `this.#allTextSelected`, `this.inputField`, `this.window.gBrowser.contentTitle`, `this.window.gBrowser.currentURI`, `uri.displaySpec`

## UrlbarInputBase._on_dragover()
- 位置: L6131-6142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.droppedLinkHandler.canDropLink()`
- 条件付き依存: `if (!this.#isAddressbar)` → `event.dataTransfer.types.includes()`
- 参照: `event.dataTransfer.dropEffect`, `this.#isAddressbar`
- XPCOM: `Services.droppedLinkHandler`

## UrlbarInputBase._on_drop()
- 位置: L6149-6193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.droppedLinkHandler.getTriggeringPrincipal()`, `UrlbarShared.isInstance()`, `getDroppableData()`, `this.#makeQueryContext()`, `this.controller.engagementEvent.start()`, `this.focus()`, `this.handleNavigation()`, `this.parentController.setLastQueryContextCache()`, `this.setPageProxyState()`, `this.setURI()`
- 参照: `droppedData.href`, `this.#isAddressbar`, `this.userTypedValue`, `this.value`, `this.window.gBrowser.currentURI.spec`
- XPCOM: `Services.droppedLinkHandler`

## UrlbarInputBase.#allTextSelected()
- 位置: L6196-6198
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.selectionEnd`, `this.selectionStart`, `this.value.length`

## UrlbarInputBase.#getSchemelessInput()
- 位置: L6208-6214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["http://", "https://", "file://"].every()`, `value.trim()`, `value.trim().startsWith()`

## UrlbarInputBase.#isOpenedPageInBlankTargetLoading()
- 位置: L6216-6223
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.window.gBrowser.selectedBrowser.browsingContext .nonWebControlledLoadingURI`, `this.window.gBrowser.selectedBrowser.browsingContext.sessionHistory ?.count`

## UrlbarInputBase.#selectedText()
- 位置: L6245-6252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.editor.selection.toStringWithFormat()`
- 参照: `Ci.nsIDocumentEncoder.OutputPreformatted`, `Ci.nsIDocumentEncoder.OutputRaw`
- XPCOM: [`nsIDocumentEncoder`](../../../../dom/serializers/nsIDocumentEncoder.idl.md)

## UrlbarInputBase.#isHomeKeyUpEvent()
- 位置: L6260-6284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getPlatform()`
- 参照: `KeyEvent.DOM_VK_HOME`, `KeyEvent.DOM_VK_META`, `KeyboardEvent.DOM_VK_A`, `KeyboardEvent.DOM_VK_LEFT`, `event.ctrlKey`, `event.keyCode`, `event.shiftKey`, `this._isKeyDownWithMetaAndLeft`

## UrlbarInputBase.#canHandleAsBlankPage()
- 位置: L6286-6288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.window.isBlankPageURL()`

## getDroppableData()
- 位置: L6302-6349
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

## losslessDecodeDisplaySpec()
- 位置: L6360-6440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/%25(?:3B|2F|3F|3A|40|26|3D|2B|24|2C|23)/i.test()`, `displaySpec.indexOf()`, `displaySpec.slice()`, `value.replace()`
- 条件付き依存: `if (!/%25(?:3B|2F|3F|3A|40|26|3D|2B|24|2C|23)/i.test(value))` → `["https", "http", "file", "ftp"].includes()`
- 条件付き依存: `if (decodeASCIIOnly)` → `value.replace()`
- 条件付き依存: `if (!(decodeASCIIOnly))` → `decodeURI()`

## losslessDecodeURL()
- 位置: L6450-6454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.getDisplaySpec()`, `losslessDecodeDisplaySpec()`
- 参照: `url.href`

## CopyCutController.constructor()
- 位置: L6464-6466
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.urlbar`

## CopyCutController.doCommand()
- 位置: L6472-6497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ClipboardHelper.copyString()`, `this.isCommandEnabled()`, `urlbar._getSelectedValueForClipboard()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.value.substring()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.setSelectionRange()`
- 条件付き依存: `if (command == "cmd_cut" && this.isCommandEnabled(command))` → `urlbar.inputField.dispatchEvent()`
- 参照: `this.urlbar`, `urlbar.inputField.value`, `urlbar.selectionEnd`, `urlbar.selectionStart`, `urlbar.window`

## CopyCutController.supportsCommand()
- 位置: L6505-6512
- 役割: (未記入)
- 触るとき: (未記入)

## CopyCutController.isCommandEnabled()
- 位置: L6520-6526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.supportsCommand()`
- 参照: `this.urlbar.readOnly`, `this.urlbar.selectionEnd`, `this.urlbar.selectionStart`

## CopyCutController.onEvent()
- 位置: L6528-6528
- 役割: (未記入)
- 触るとき: (未記入)

## AddSearchEngineHelper.constructor()
- 位置: L6557-6560
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `input.view.oneOffSearchButtons`, `this.input`, `this.shortcutButtons`

## AddSearchEngineHelper.maxInlineEngines()
- 位置: L6568-6570
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `SearchModeSwitcher.MAX_OPENSEARCH_ENGINES`

## AddSearchEngineHelper.setEnginesFromBrowser()
- 位置: L6578-6586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engines.slice()`, `this._sameEngines()`
- 条件付き依存: `if (!this._sameEngines(this.engines, engines))` → `this.shortcutButtons?.updateWebEngines()`
- 参照: `browser.browsingContext`, `this.browsingContext`, `this.engines`

## AddSearchEngineHelper._sameEngines()
- 位置: L6588-6596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.deepEqual()`, `engines1.map()`, `engines2.map()`
- 参照: `e.title`, `engines1?.length`, `engines2?.length`

## AddSearchEngineHelper._createMenuitem()
- 位置: L6598-6614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elt.addEventListener()`, `elt.classList.add()`, `elt.setAttribute()`, `this._onCommand.bind()`, `this.input.document.createXULElement()`, `this.input.document.l10n.setAttributes()`
- 条件付き依存: `if (engine.icon)` → `elt.setAttribute()`
- 条件付き依存: `if (!(engine.icon))` → `elt.removeAttribute()`
- 参照: `engine.icon`, `engine.title`, `engine.uri`

## AddSearchEngineHelper._createMenu()
- 位置: L6616-6631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `elt.appendChild()`, `elt.classList.add()`, `elt.setAttribute()`, `this.input.document.createXULElement()`, `this.input.document.l10n.setAttributes()`
- 条件付き依存: `if (engine.icon)` → `elt.setAttribute()`
- 条件付き依存: `if (engine.icon)` → `ChromeUtils.encodeURIForSrcset()`
- 参照: `engine.icon`

## AddSearchEngineHelper.createContextSeparator()
- 位置: L6648-6655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.contextSeparator.classList.add()`, `this.contextSeparator.setAttribute()`, `this.input.document.createXULElement()`
- 参照: `this.contextSeparator`, `this.contextSeparator.collapsed`

## AddSearchEngineHelper.refreshContextMenu()
- 位置: L6663-6700
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
- 位置: async L6702-6713
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.target.getAttribute()`, `lazy.SearchUIUtils.addOpenSearchEngine()`
- 条件付き依存: `if (added)` → `this.refreshContextMenu()`
- 参照: `console.error`, `this.browsingContext`
