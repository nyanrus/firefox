# browser/components/downloads/content/allDownloadsView.js

source: browser/components/downloads/content/allDownloadsView.js
source-hash: e82abc481aaa14c4c90c89ef9eeb855fdf1acf40
lines: 954

## <module>
- 役割: ダウンロードの一覧ページ (about:downloads とサイドバー) の要素シェル、一覧ビュー、コントローラー、ドラッグ&ドロップを実装する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Object.setPrototypeOf()`, `document.addEventListener()`, `document.getElementById()`, `dropNode.addEventListener()`, `richListBox._placesView.onDragOver()`, `richListBox._placesView.onDrop()`, `richListBox.addEventListener()`, `this._placesView.onContextMenu()`, `this._placesView.onDoubleClick()`, `this._placesView.onDragStart()`, `this._placesView.onKeyPress()`, `this._placesView.onScroll()`, `this._placesView.onSelect()`

## HistoryDownloadElementShell()
- 位置: L45-53
- 役割: 履歴または現在のダウンロード 1 件分の richlistitem を作り、表示用の状態を持たせる。
- 触るとき: 一覧の 1 行の生成や属性を変えるとき。
- 呼び出し先: `document.createXULElement()`, `this.element.classList.add()`
- 参照: `this._download`, `this.element`, `this.element._shell`

## download()
- 位置: L60-62
- 役割: 要素が表しているダウンロード (または履歴のダウンロード) を返す。
- 触るとき: 一覧の行がどのダウンロードに対応しているかを追うとき。
- 参照: `this._download`

## onStateChanged()
- 位置: L64-77
- 役割: 状態が変わったとき、ターゲットの存在確認をやり直して表示を更新し、コマンドの有効状態を再計算する。
- 触るとき: 完了や失敗のときに一覧の行とメニューが同期しない問題を調べるとき。
- 呼び出し先: `this._updateState()`
- 条件付き依存: `if (this.element.selected)` → `goUpdateDownloadCommands()`
- 条件付き依存: `if (!(this.element.selected))` → `goUpdateCommand()`
- 参照: `this._targetFileChecked`, `this.element.selected`

## onChanged()
- 位置: L79-92
- 役割: 状態が変わったら onStateChanged を呼び、同じなら表示だけ更新する。表示範囲外の項目は何もしない。
- 触るとき: 進捗の更新で行が再描画されすぎる、または更新されない問題を見るとき。
- 呼び出し先: `DownloadsCommon.stateOfDownload()`
- 条件付き依存: `if (this._downloadState !== newState)` → `this.onStateChanged()`
- 条件付き依存: `if (!(this._downloadState !== newState))` → `this._updateStateInner()`
- 参照: `this._downloadState`, `this.active`, `this.download`

## isCommandEnabled()
- 位置: L95-104
- 役割: 非有効な項目では cmd_delete 以外のコマンドを拒否し、有効な場合は DownloadElementShell の判定に任せる。
- 触るとき: 表示範囲外の行でコマンドの扱いを変えるとき。
- 呼び出し先: `DownloadsViewUI.DownloadElementShell.prototype.isCommandEnabled.call()`
- 参照: `this.active`

## downloadsCmd_unblock()
- 位置: L106-108
- 役割: ブロック解除の確認ダイアログ (unblock) を開く。
- 触るとき: ブロック解除の確認の種類を変えるとき。
- 呼び出し先: `this.confirmUnblock()`

## downloadsCmd_unblockAndSave()
- 位置: L109-111
- 役割: 保存のためのブロック解除として、確認ダイアログ (unblock) を開く。
- 触るとき: 「ブロックを解除して保存」の挙動を変えるとき。現在は unblock と同じ種類を使っている。
- 呼び出し先: `this.confirmUnblock()`

## downloadsCmd_chooseUnblock()
- 位置: L113-115
- 役割: ブロック解除かファイル削除かを選ぶ確認ダイアログ (chooseUnblock) を開く。
- 触るとき: ブロック時の選択肢を変えるとき。
- 呼び出し先: `this.confirmUnblock()`

## downloadsCmd_chooseOpen()
- 位置: L117-119
- 役割: 開くかファイル削除かを選ぶ確認ダイアログ (chooseOpen) を開く。
- 触るとき: ブロック後に開く操作の確認を変えるとき。
- 呼び出し先: `this.confirmUnblock()`

## matchesSearchTerm()
- 位置: L124-136
- 役割: 表示名と元 URL のどちらかに検索語が含まれるかを大文字小文字を無視して判定する。
- 触るとき: 一覧の検索結果に出る項目の条件を変えるとき。
- 呼び出し先: `(this.download.source.originalUrl || this.download.source.url) .toLowerCase()`, `(this.download.source.originalUrl || this.download.source.url) .toLowerCase() .includes()`, `DownloadsViewUI.getDisplayName()`, `aTerm.toLowerCase()`, `displayName.toLowerCase()`, `displayName.toLowerCase().includes()`
- 参照: `this.download`, `this.download.source.originalUrl`, `this.download.source.url`

## doDefaultCommand()
- 位置: L140-161
- 役割: ダブルクリックや Enter の既定コマンドを求め、Shift、Ctrl、Meta、中ボタンの修飾があれば開き先 (窓、タブ) を付けて実行する。
- 触るとき: ダブルクリックや Enter で開き先が想定と違うときに見る。
- 呼び出し先: `this.isCommandEnabled()`
- 条件付き依存: `if ( command == "downloadsCmd_open" && event && (event.shiftKey || event.ctrlKey || event.metaKey || event.button == 1) )` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if ( command == "downloadsCmd_open" && event && (event.shiftKey || event.ctrlKey || event.metaKey || event.button == 1) )` → `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if ( command == "downloadsCmd_open" && event && (event.shiftKey || event.ctrlKey || event.metaKey || event.button == 1) )` → `["window", "tabshifted", "tab"].includes()`
- 条件付き依存: `if (command && this.isCommandEnabled(command))` → `this.doCommand()`
- 参照: `event.button`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `this.currentDefaultCommandName`

## onSelect()
- 位置: L169-191
- 役割: ターゲットのパスがあり未確認なら refresh で存在を確認する。確認は 1 回だけ行う。失敗しても再確認しない。
- 触るとき: 選択すると存在しないファイルのボタン状態が変わらない問題を調べるとき。
- 条件付き依存: `if (!this._targetFileChecked)` → `this.download .refresh() .catch(console.error) .then()`
- 条件付き依存: `if (!this._targetFileChecked)` → `this.download .refresh() .catch()`
- 条件付き依存: `if (!this._targetFileChecked)` → `this.download .refresh()`
- 参照: `console.error`, `this._targetFileChecked`, `this.active`, `this.download.target.path`

## onDownloadButton()
- 位置: L202-204
- 役割: 押されたボタンの richlistitem の shell に onButton を依頼する。
- 触るとき: 行内ボタンの押下が効かない問題を追うとき。
- 呼び出し先: `event.target.closest()`, `event.target.closest("richlistitem")._shell.onButton()`

## onDownloadClick()
- 位置: L206-206
- 役割: クリックは何もしない (空の処理)。
- 触るとき: クリック時に何か追加したいときに、ここに処理を足す。

## DownloadsPlacesView()
- 位置: L221-272
- 役割: 一覧ビューのコンストラクター。コントローラーを登録し、DownloadsData を購読し、表示範囲の要素を有効化する。ウィンドウを閉じたら登録を外して指示器の抑止も戻す。
- 触るとき: 一覧の初期化順序や、閉じたときに後始末されるかを確認するとき。
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getIndicatorData()`, `this._downloadsData.addView()`, `this._downloadsData.removeView()`, `this._ensureVisibleElementsAreActive()`, `window.addEventListener()`, `window.controllers.insertControllerAt()`, `window.controllers.removeController()`
- 条件付き依存: `if (aSuppressionFlag === DownloadsCommon.SUPPRESS_ALL_DOWNLOADS_OPEN)` → `DownloadsCommon.getIndicatorData()`
- 参照: `DownloadsCommon.SUPPRESS_ALL_DOWNLOADS_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `this._active`, `this._downloadsData`, `this._initiallySelectedElement`, `this._richlistbox`, `this._richlistbox._placesView`, `this._searchTerm`, `this._viewItemsForDownloads`, `this._waitingForInitialData`, `this.result`, `window.opener`

## associatedElement()
- 位置: L275-277
- 役割: 一覧の richlistbox を返す。
- 触るとき: ビューに紐づく要素を取り出す箇所を追うとき。
- 参照: `this._richlistbox`

## active()
- 位置: L279-281
- 役割: ビューが有効 (表示中) かを返す。
- 触るとき: 非表示時に一覧の更新を止める仕組みを確認するとき。
- 参照: `this._active`

## active()
- 位置: L282-287
- 役割: 有効化されたら、表示範囲の要素を有効化する。
- 触るとき: タブが再表示されたときに項目の中身が描画されない問題を調べるとき。
- 条件付き依存: `if (this._active)` → `this._ensureVisibleElementsAreActive()`
- 参照: `this._active`

## _ensureVisibleElementsAreActive()
- 位置: L298-314
- 役割: 有効でなければ何もしない。debounce 指定時は 10ms 後に実行するタイマーを張る。
- 触るとき: スクロールやリサイズで要素の有効化が遅れる問題を調べるとき。
- 条件付き依存: `if (debounce)` → `setTimeout()`
- 条件付き依存: `if (debounce)` → `this._internalEnsureVisibleElementsAreActive()`
- 条件付き依存: `if (!(debounce))` → `this._internalEnsureVisibleElementsAreActive()`
- 参照: `this._ensureVisibleTimer`, `this._richlistbox.firstChild`, `this.active`

## _internalEnsureVisibleElementsAreActive()
- 位置: L316-375
- 役割: nodesFromRect で見えている項目を求め、その上下の隣接項目も含めて ensureActive を呼ぶ。
- 触るとき: 表示範囲の判定 (キーボード移動に必要な上下の 1 項目を含めるか) を変えるとき。
- 呼び出し先: `this._richlistbox.getBoundingClientRect()`, `winUtils.nodesFromRect()`
- 条件付き依存: `if (this._ensureVisibleTimer)` → `clearTimeout()`
- 条件付き依存: `if (node.localName === "richlistitem" && node._shell)` → `node._shell.ensureActive()`
- 条件付き依存: `if (nodeBelowVisibleArea && nodeBelowVisibleArea._shell)` → `nodeBelowVisibleArea._shell.ensureActive()`
- 条件付き依存: `if (nodeAboveVisibleArea && nodeAboveVisibleArea._shell)` → `nodeAboveVisibleArea._shell.ensureActive()`
- 参照: `firstVisibleNode.previousSibling`, `lastVisibleNode.nextSibling`, `node._shell`, `node.localName`, `nodeAboveVisibleArea._shell`, `nodeBelowVisibleArea._shell`, `rlbRect.height`, `rlbRect.left`, `rlbRect.top`, `rlbRect.width`, `this._ensureVisibleTimer`, `this._richlistbox.firstChild`, `window.windowUtils`

## place()
- 位置: L378-380
- 役割: 現在の履歴の検索 (place) を返す。
- 触るとき: 一覧がどの検索条件で履歴を読むかを追うとき。
- 参照: `this._place`

## place()
- 位置: L381-388
- 役割: 検索 place を設定する。同じ値なら検索語を空にする。
- 触るとき: 一覧の表示対象を切り替える処理を変えるとき。
- 参照: `this._place`, `this.searchTerm`

## selectedNodes()
- 位置: L390-395
- 役割: 選択されている項目のうち、履歴のノードを持つものだけを返す。
- 触るとき: 履歴の削除や並べ替えの対象になる項目を絞るとき。
- 呼び出し先: `Array.prototype.filter.call()`
- 参照: `element._shell.download.placesNode`, `this._richlistbox.selectedItems`

## selectedNode()
- 位置: L397-400
- 役割: 履歴ノードが 1 件だけ選ばれていれば、そのノードを返す。
- 触るとき: 1 件選択時だけ有効な操作の判定を変えるとき。
- 参照: `selectedNodes.length`, `this.selectedNodes`

## hasSelection()
- 位置: L402-404
- 役割: 履歴ノードが 1 件以上選ばれているかを返す。
- 触るとき: 選択があるときだけ有効になるコマンドを変えるとき。
- 参照: `this.selectedNodes.length`

## controller()
- 位置: L406-408
- 役割: richlistbox のコントローラーを返す。
- 触るとき: コマンド処理の委譲先を確認するとき。
- 参照: `this._richlistbox.controller`

## searchTerm()
- 位置: L410-412
- 役割: 現在の検索語を返す。
- 触るとき: 検索語が保持されているかを確認するとき。
- 参照: `this._searchTerm`

## searchTerm()
- 位置: L413-425
- 役割: 検索語が変わったら選択を解除し、各項目の hidden を一致判定で更新して、表示範囲を再度有効化する。
- 触るとき: 検索で項目が消えない、または選択が残るといった問題を調べるとき。
- 条件付き依存: `if (this._searchTerm != aValue)` → `this._richlistbox.clearSelection()`
- 条件付き依存: `if (this._searchTerm != aValue)` → `element._shell.matchesSearchTerm()`
- 条件付き依存: `if (this._searchTerm != aValue)` → `this._ensureVisibleElementsAreActive()`
- 参照: `element.hidden`, `this._richlistbox.childNodes`, `this._searchTerm`

## _ensureInitialSelection()
- 位置: L442-455
- 役割: 初期データの読み込み中にユーザーが選択を変えていなければ、先頭項目を選択する。
- 触るとき: 一覧を開いた直後に先頭が選ばれない問題を調べるとき。
- 条件付き依存: `if (firstDownloadElement != this._initiallySelectedElement)` → `firstDownloadElement._shell.ensureActive()`
- 参照: `this._initiallySelectedElement`, `this._richlistbox.currentItem`, `this._richlistbox.firstChild`, `this._richlistbox.selectedItem`

## onDownloadBatchStarting()
- 位置: L466-471
- 役割: 新しい DocumentFragment を用意し、一括追加中は選択時の通知を止める。
- 触るとき: 大量のダウンロードを読み込むときの描画回数を変えるとき。
- 呼び出し先: `document.createDocumentFragment()`
- 参照: `this._richlistbox.suppressOnSelect`, `this.batchFragment`, `this.oldSuppressOnSelect`

## onDownloadBatchEnded()
- 位置: L473-491
- 役割: 通知を戻し、溜めた要素を一度に挿入して初期選択と表示範囲の有効化を行う。初回読み込みならイベントを発火する。
- 触るとき: 起動直後の一覧が読み込み完了後に正しく選ばれないときに見る。
- 呼び出し先: `goUpdateDownloadCommands()`, `this._ensureInitialSelection()`, `this._ensureVisibleElementsAreActive()`
- 条件付き依存: `if (this.batchFragment.childElementCount)` → `this._prependBatchFragment()`
- 条件付き依存: `if (this._waitingForInitialData)` → `this._richlistbox.dispatchEvent()`
- 参照: `this._richlistbox.suppressOnSelect`, `this._waitingForInitialData`, `this.batchFragment`, `this.batchFragment.childElementCount`, `this.oldSuppressOnSelect`

## _prependBatchFragment()
- 位置: L493-518
- 役割: richlistbox を一度外して断片を先頭に入れ、戻す。XBL の状態は退避して復元する。
- 触るとき: 一括挿入の描画性能や選択状態の崩れを調べるとき。
- 呼び出し先: `Object.getOwnPropertyNames()`, `parentNode.insertBefore()`, `parentNode.removeChild()`, `this._richlistbox.prepend()`, `xblFields.set()`
- 条件付き依存: `if (oldActiveElement && oldActiveElement != document.activeElement)` → `oldActiveElement.focus()`
- 参照: `document.activeElement`, `this._richlistbox`, `this._richlistbox.nextSibling`, `this._richlistbox.parentNode`, `this.batchFragment`

## onDownloadAdded()
- 位置: L520-543
- 役割: 新しい shell を作って先頭か指定位置に挿入し、検索語に合わなければ隠す。一括中でなければ表示範囲とコマンドを更新する。
- 触るとき: 新規ダウンロードが一覧の先頭に出ない、または検索中に隠れない問題を見るとき。
- 呼び出し先: `this._viewItemsForDownloads.set()`
- 条件付き依存: `if (insertBefore)` → `this._viewItemsForDownloads .get(insertBefore) .element.insertAdjacentElement()`
- 条件付き依存: `if (insertBefore)` → `this._viewItemsForDownloads .get()`
- 条件付き依存: `if (!(insertBefore))` → `(this.batchFragment || this._richlistbox).prepend()`
- 条件付き依存: `if (this.searchTerm)` → `shell.matchesSearchTerm()`
- 条件付き依存: `if (!this.batchFragment)` → `this._ensureVisibleElementsAreActive()`
- 条件付き依存: `if (!this.batchFragment)` → `goUpdateCommand()`
- 参照: `shell.element`, `shell.element.hidden`, `this._richlistbox`, `this.batchFragment`, `this.searchTerm`

## onDownloadChanged()
- 位置: L545-547
- 役割: 該当項目の onChanged を呼ぶ。
- 触るとき: 項目の更新が一覧に反映されないときに送り先を確認する。
- 呼び出し先: `this._viewItemsForDownloads.get()`, `this._viewItemsForDownloads.get(download).onChanged()`

## onDownloadRemoved()
- 位置: L549-573
- 役割: 削除対象が 1 件だけ選ばれていれば次か前の項目へ選択を移し、その要素を削除する。
- 触るとき: 項目を消した後に選択がどこへ移るかを変えるとき。
- 呼び出し先: `element.remove()`, `this._richlistbox.removeItemFromSelection()`, `this._viewItemsForDownloads.get()`
- 条件付き依存: `if ( (element.nextSibling || element.previousSibling) && this._richlistbox.selectedItems && this._richlistbox.selectedItems.length == 1 && this._richlistbox.sele...)` → `this._richlistbox.selectItem()`
- 条件付き依存: `if (!this.batchFragment)` → `this._ensureVisibleElementsAreActive()`
- 条件付き依存: `if (!this.batchFragment)` → `goUpdateCommand()`
- 参照: `element.nextSibling`, `element.previousSibling`, `this._richlistbox.selectedItems`, `this._richlistbox.selectedItems.length`, `this._viewItemsForDownloads.get(download).element`, `this.batchFragment`

## supportsCommand()
- 位置: L576-597
- 役割: 一覧が扱うコマンド名かを判定する。クリアは常に対象だが、他のコマンドは一覧にフォーカスがあるときだけ対象にする。
- 触るとき: コピーや貼り付けが一覧外で効いてしまう、または効かない問題を調べるとき。
- 呼び出し先: `DownloadsViewUI.isCommandName()`
- 参照: `HistoryDownloadElementShell.prototype`, `document.activeElement`, `this._richlistbox`

## isCommandEnabled()
- 位置: L600-629
- 役割: コマンドごとに有効性を判定する。コピーは URL を持つ選択がある時、選択済みの項目は各 shell の判定を満たす時に有効。
- 触るとき: 一覧のメニューやショートカットの有効・無効が想定と違うときに見る。
- 呼び出し先: `Array.prototype.every.call()`, `Array.prototype.some.call()`, `Services.clipboard.hasDataMatchingFlavors()`, `element._shell.isCommandEnabled()`, `this.canClearDownloads()`
- 参照: `Ci.nsIClipboard.kGlobalClipboard`, `element._shell.download`, `source?.originalUrl`, `source?.url`, `this._richlistbox`, `this._richlistbox.selectedItems`, `this._richlistbox.selectedItems.length`
- XPCOM: `nsIClipboard` / `Services.clipboard`

## _copySelectedDownloadsToClipboard()
- 位置: L631-640
- 役割: 選択された項目の元 URL (なければ source.url) を改行で繋いでクリップボードに入れる。
- 触るとき: リンクのコピーで出力する形式を変えるとき。
- 呼び出し先: `Array.from()`, `Cc["@mozilla.org/widget/clipboardhelper;1"] .getService()`, `Cc["@mozilla.org/widget/clipboardhelper;1"] .getService(Ci.nsIClipboardHelper) .copyString()`, `urls.join()`
- 参照: `Ci.nsIClipboardHelper`, `element._shell.download`, `source?.originalUrl`, `source?.url`, `this._richlistbox.selectedItems`
- XPCOM: `nsIClipboardHelper` / `@mozilla.org/widget/clipboardhelper;1`

## _getURLFromClipboardData()
- 位置: L642-665
- 役割: クリップボードから text/x-moz-url か text/plain を読み、1 行目を URL、2 行目を名前として返す。失敗時は空文字を返す。
- 触るとき: 貼り付けで URL を読み取れない問題を調べるとき。
- 呼び出し先: `CLIPBOARD_URL_FLAVORS.forEach()`, `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `Services.clipboard.getData()`, `data.value .QueryInterface()`, `data.value .QueryInterface(Ci.nsISupportsString) .data.split()`, `trans.getAnyTransferData()`, `trans.init()`
- 条件付き依存: `if (url)` → `NetUtil.newURI()`
- 参照: `Ci.nsISupportsString`, `Ci.nsITransferable`, `NetUtil.newURI(url).spec`, `Services.clipboard.kGlobalClipboard`, `trans.addDataFlavor`
- XPCOM: [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## doCommand()
- 位置: L668-688
- 役割: 有効なコマンドのうち、一覧自身のメソッドがあればそれを実行し、なければ選択された各項目の shell に渡す。
- 触るとき: 選択項目にだけ効くコマンドの委譲経路を確認するとき。
- 呼び出し先: `element._shell.doCommand()`, `this.isCommandEnabled()`
- 条件付き依存: `if (aCommand in this)` → `this[aCommand]()`
- 参照: `this._richlistbox.selectedItems`

## onEvent()
- 位置: L691-691
- 役割: nsIController 用の空実装。
- 触るとき: コントローラーのイベント処理を追加するときに、ここを置き換える。

## cmd_copy()
- 位置: L693-695
- 役割: 選択された項目の URL をコピーする。
- 触るとき: コピーの対象や形式を変えるとき。
- 呼び出し先: `this._copySelectedDownloadsToClipboard()`

## cmd_selectAll()
- 位置: L697-715
- 役割: 検索語がなければ全選択し、検索語があれば隠れていない項目だけを選択する。
- 触るとき: 検索中の全選択で隠れた項目が選ばれる問題を調べるとき。
- 呼び出し先: `this._richlistbox.clearSelection()`, `this._richlistbox.getItemAtIndex()`, `this._richlistbox.getNextItem()`
- 条件付き依存: `if (!this.searchTerm)` → `this._richlistbox.selectAll()`
- 条件付き依存: `if (!item.hidden)` → `this._richlistbox.addItemToSelection()`
- 参照: `item.hidden`, `this._richlistbox.suppressOnSelect`, `this.searchTerm`

## cmd_paste()
- 位置: L717-724
- 役割: クリップボードの URL を読み、既定のダウンロード処理に渡す。
- 触るとき: URL の貼り付けでダウンロードを開始する挙動を変えるとき。
- 呼び出し先: `this._getURLFromClipboardData()`
- 条件付き依存: `if (url)` → `BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (url)` → `DownloadURL()`
- 参照: `browserWin.document`

## downloadsCmd_clearDownloads()
- 位置: L726-738
- 役割: 終了済みのダウンロードを一覧から消し、履歴の表示中ならダウンロード遷移の訪問履歴も消す。
- 触るとき: 「ダウンロードを消去」の範囲を変えるとき。
- 呼び出し先: `goUpdateCommand()`, `this._downloadsData.removeFinished()`
- 条件付き依存: `if (this._place)` → `PlacesUtils.history .removeVisitsByFilter({ transition: PlacesUtils.history.TRANSITIONS.DOWNLOAD, }) .catch()`
- 条件付き依存: `if (this._place)` → `PlacesUtils.history .removeVisitsByFilter()`
- 参照: `PlacesUtils.history.TRANSITIONS.DOWNLOAD`, `console.error`, `this._place`

## onContextMenu()
- 位置: L740-771
- 役割: 選択項目に合わせて右クリックメニューを更新し、URL の項目を URL の有無で隠す。未完了なら一時停止のコマンドも更新する。
- 触るとき: 右クリックメニューの項目が項目の状態と合わないときに見る。
- 呼び出し先: `Array.prototype.some.call()`, `DownloadsViewUI.updateContextMenuForElement()`, `contextMenu.querySelector()`, `document.getElementById()`
- 条件付き依存: `if (!download.stopped)` → `goUpdateCommand()`
- 参照: `contextMenu.querySelector(".downloadCopyLocationMenuItem").hidden`, `contextMenu.querySelector(".downloadLinksSeparator").hidden`, `contextMenu.querySelector(".downloadOpenReferrerMenuItem").hidden`, `download.stopped`, `el._shell.download.source?.isDataURICleared`, `el._shell.download.source?.url`, `element._shell`, `element._shell.download`, `this._richlistbox.selectedItem`, `this._richlistbox.selectedItems`

## onKeyPress()
- 位置: L773-799
- 役割: Enter は 1 件選択時に既定操作を行い、スペースは選択中の項目の一時停止と再開を切り替える。
- 触るとき: キーボード操作の割り当てを変えるとき。
- 条件付き依存: `if (element._shell)` → `element._shell.doDefaultCommand()`
- 条件付き依存: `if (!(aEvent.keyCode == KeyEvent.DOM_VK_RETURN))` → `" ".charCodeAt()`
- 条件付き依存: `if (aEvent.charCode == " ".charCodeAt(0))` → `element._shell.isCommandEnabled()`
- 条件付き依存: `if (element._shell.isCommandEnabled("downloadsCmd_pauseResume"))` → `element._shell.doCommand()`
- 条件付き依存: `if (atLeastOneDownloadToggled)` → `aEvent.preventDefault()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.charCode`, `aEvent.keyCode`, `element._shell`, `selectedElements.length`, `this._richlistbox.selectedItems`

## onDoubleClick()
- 位置: L801-815
- 役割: 左ボタンのダブルクリックで、1 件だけ選択されていれば既定操作を実行する。
- 触るとき: ダブルクリックの既定操作が効かない問題を調べるとき。
- 条件付き依存: `if (element._shell)` → `element._shell.doDefaultCommand()`
- 参照: `aEvent.button`, `element._shell`, `selectedElements.length`, `this._richlistbox.selectedItems`

## onScroll()
- 位置: L817-819
- 役割: スクロールに合わせて、表示範囲の要素を遅延して有効化する。
- 触るとき: スクロールしたときに項目が遅れて描画される問題を調べるとき。
- 呼び出し先: `this._ensureVisibleElementsAreActive()`

## onSelect()
- 位置: L821-830
- 役割: コマンドの有効状態を更新し、選択された各項目に存在確認を依頼する。
- 触るとき: 選択変更でメニューやボタンの状態が古いままになる問題を調べるとき。
- 呼び出し先: `goUpdateDownloadCommands()`
- 条件付き依存: `if (elt._shell)` → `elt._shell.onSelect()`
- 参照: `elt._shell`, `this._richlistbox.selectedItems`

## onDragStart()
- 位置: L832-857
- 役割: 選択中の 1 件のターゲットファイルが存在すれば、そのファイルを URI とファイル型で転送データにセットする。
- 触るとき: 一覧からファイルをドラッグしたときに渡る形式を変えるとき。複数選択は未対応 (Bug 831358)。
- 呼び出し先: `Services.io.newFileURI()`, `dt.addElement()`, `dt.mozSetDataAt()`, `dt.setData()`, `file.exists()`
- 参照: `FileUtils.File`, `Services.io.newFileURI(file).spec`, `aEvent.dataTransfer`, `dt.effectAllowed`, `selectedItem._shell.download.target.path`, `this._richlistbox.selectedItem`
- XPCOM: `Services.io`

## onDragOver()
- 位置: L859-868
- 役割: URL か文字列のドラッグを受け付けるため、dragover の既定動作を止める。
- 触るとき: ドロップできるデータの種類を増やすとき。
- 呼び出し先: `types.includes()`
- 条件付き依存: `if ( types.includes("text/uri-list") || types.includes("text/x-moz-url") || types.includes("text/plain") )` → `aEvent.preventDefault()`
- 参照: `aEvent.dataTransfer.types`

## onDrop()
- 位置: L870-891
- 役割: 自身から出たファイルのドロップは無視し、それ以外のリンクは about: を除いてダウンロードとして開始する。
- 触るとき: ドロップされた URL からダウンロードを開始する条件を変えるとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `DownloadURL()`, `Services.droppedLinkHandler.dropLinks()`, `aEvent.preventDefault()`, `dt.mozGetDataAt()`, `link.url.startsWith()`
- 参照: `aEvent.dataTransfer`, `browserWin.document`, `link.name`, `link.url`, `links.length`
- XPCOM: `Services.droppedLinkHandler`

## DownloadsPlacesView.prototype[methodName]()
- 位置: L899-903
- 役割: load や applyFilter など、一覧では使わないメソッドを呼ぶと例外を投げるように置き換える。
- 触るとき: この一覧で使えないメソッドを追加・削除するとき。

## goUpdateDownloadCommands()
- 位置: L906-916
- 役割: 一覧と要素 shell の prototype から cmd_ と downloadsCmd_ のコマンドを列挙し、すべて更新する。
- 触るとき: 新しいコマンドを追加したのにメニューの状態が更新されないときに見る。
- 呼び出し先: `updateCommandsForObject()`
- 参照: `DownloadsPlacesView.prototype`, `HistoryDownloadElementShell.prototype`

## updateCommandsForObject()
- 位置: L907-913
- 役割: オブジェクトのうちコマンド名のプロパティを、goUpdateCommand で更新する。
- 触るとき: コマンドの更新対象の列挙方法を変えるとき。
- 呼び出し先: `DownloadsViewUI.isCommandName()`
- 条件付き依存: `if (DownloadsViewUI.isCommandName(name))` → `goUpdateCommand()`
