# browser/components/sessionstore/content/aboutSessionRestore.js

source: browser/components/sessionstore/content/aboutSessionRestore.js
source-hash: 4cba943f1aafd8e738cc3fb85233d3e0e957d057
lines: 507

## <module>
- 役割: クラッシュ後などにセッション復元を選ばせる about:sessionrestore ページのスクリプトで、ウィンドウとタブの一覧ツリーと復元ボタンの動作を担う。
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`

## window.onload()
- 位置: L51-107
- 役割: ボタン・ツリーのイベントを結びつけ、sessionData から状態を読み、ツリーを描く準備をする。データがなければ再試行ボタンを無効にする。
- 触るとき: ページ読み込み時に復元画面の初期状態（ボタンの有効・無効や一覧の表示）がおかしいとき。
- 呼び出し先: `JSON.parse()`, `document.createEvent()`, `document.getElementById()`, `errorTryAgainButton.addEventListener()`, `errorTryAgainButton.focus()`, `event.initUIEvent()`, `getTabList()`, `getTryAgainButton()`, `initTreeView()`, `sessionData.dispatchEvent()`, `tabListTree.addEventListener()`
- 条件付き依存: `if (button)` → `button.addEventListener()`
- 条件付き依存: `if (errorCancelButton)` → `errorCancelButton.addEventListener()`
- 参照: `errorTryAgainButton.disabled`, `sessionData.value`, `toggleTabs.onclick`

## toggleHiddenTabs()
- 位置: L56-60
- 役割: タブ一覧の表示・非表示を切り替え、表示になったらツリーを初期化する。
- 触るとき: 「タブを選んで復元」の一覧の開閉動作を変えるとき。
- 呼び出し先: `getTabList()`, `initTreeView()`, `toggleTabs.classList.contains()`, `toggleTabs.classList.toggle()`
- 参照: `getTabList().hidden`

## isTreeViewVisible()
- 位置: L109-111
- 役割: タブ一覧ツリーが hidden でないかを返す。
- 触るとき: 一覧を表示しているときだけ動かす処理の条件を確かめるとき。
- 呼び出し先: `getTabList()`
- 参照: `getTabList().hidden`

## initTreeView()
- 位置: async L113-161
- 役割: 初回だけ、各ウィンドウの見出し（l10n）と各タブの表示名・アイコンから gTreeData を作り、ツリーに設定して 1 行目を選ぶ。
- 触るとき: 一覧の行の作り方（表示名の優先順やアイコン）を変えるとき。
- 呼び出し先: `aWinData.tabs.map()`, `document.l10n.formatValues()`, `gStateObject.windows.forEach()`, `gTreeData.push()`, `getTabList()`, `isTreeViewVisible()`, `l10nIds.push()`, `lazy.PlacesUIUtils.getImageURL()`, `tabList.view.selection.select()`
- 参照: `aTabData.entries`, `aTabData.image`, `aTabData.index`, `entry.title`, `entry.url`, `gStateObject.windows.length`, `tabList.view`, `winState.tabs`

## updateTabListVisibility()
- 位置: L164-171
- 役割: 「選んで復元」ラジオが選ばれたときだけ一覧を表示し、ツリーを初期化する。
- 触るとき: すべて復元と選択復元の切り替えの挙動を変えるとき。
- 呼び出し先: `document.getElementById()`, `getTabList()`, `initTreeView()`
- 参照: `( document.getElementById("radioRestoreChoose") ).checked`, `getTabList().hidden`

## restoreSession()
- 位置: L173-231
- 役割: 一覧で外された項目を状態から除いてから、この窓に状態を設定するか、新しい窓を開いて移してこのタブを閉じる。
- 触るとき: 「復元」ボタン押下後に何がどの窓に入るかを調べるとき。
- 呼び出し先: `JSON.stringify()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `getBrowserWindow()`, `getTryAgainButton()`, `isTreeViewVisible()`, `top.openDialog()`
- 条件付き依存: `if (isTreeViewVisible())` → `gTreeData.some()`
- 条件付き依存: `if (!gTreeData.some(aItem => aItem.checked))` → `startNewSession()`
- 条件付き依存: `if (isTreeViewVisible())` → `treeView.isContainer()`
- 条件付き依存: `if (gTreeData[t].checked === 0)` → `gStateObject.windows[ix].tabs.filter()`
- 条件付き依存: `if (!gTreeData[t].checked)` → `gStateObject.windows.splice()`
- 条件付き依存: `if (top.gBrowser.tabs.length == 1)` → `lazy.SessionStore.setWindowState()`
- 参照: `aItem.checked`, `gStateObject.windows`, `gStateObject.windows.length`, `gStateObject.windows[ix].tabs`, `gTreeData.length`, `gTreeData[t].checked`, `gTreeData[t].tabs`, `gTreeData[t].tabs[aIx].checked`, `getTryAgainButton().disabled`, `top.gBrowser.tabs.length`, `top.location.href`
- XPCOM: `Services.obs`

## observe()
- 位置: L218-230
- 役割: 新しい窓の起動完了を待ち、そこへ状態を設定してから元のタブを閉じる無名の監視関数。
- 触るとき: 新しい窓への復元が完了しないまま元タブが閉じる問題を追うとき。
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.SessionStore.setWindowState()`, `tabbrowser.getTabForBrowser()`, `tabbrowser.removeTab()`
- 参照: `top.gBrowser`, `window.docShell.chromeEventHandler`
- XPCOM: `Services.obs`

## startNewSession()
- 位置: L233-243
- 役割: browser.startup.page が 0 なら空白ページを、それ以外ならホームページを開く。
- 触るとき: 「新しいセッションを始める」の遷移先を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `getBrowserWindow().gBrowser.loadURI()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `getBrowserWindow()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `Services.io.newURI()`
- 条件付き依存: `if (Services.prefs.getIntPref("browser.startup.page") == 0)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (!(Services.prefs.getIntPref("browser.startup.page") == 0))` → `getBrowserWindow().BrowserCommands.home()`
- 条件付き依存: `if (!(Services.prefs.getIntPref("browser.startup.page") == 0))` → `getBrowserWindow()`
- XPCOM: `Services.io` / `Services.prefs` / `Services.scriptSecurityManager`

## onListClick()
- 位置: L245-270
- 役割: 右クリック以外のクリックで、タイトル列の中クリック・ダブルクリック・アクセラレータ付きクリックは 1 タブを復元し、チェック列はチェックを切り替える。
- 触るとき: 一覧のクリック操作で単一タブ復元が起きる条件を変えるとき。
- 呼び出し先: `treeView.treeBox.getCellAt()`
- 条件付き依存: `if (cell.col)` → `treeView.isContainer()`
- 条件付き依存: `if ( (aEvent.button == 1 || (aEvent.button == 0 && aEvent.detail == 2) || accelKey) && cell.col.id == "title" && !treeView.isContainer(cell.row) )` → `restoreSingleTab()`
- 条件付き依存: `if ( (aEvent.button == 1 || (aEvent.button == 0 && aEvent.detail == 2) || accelKey) && cell.col.id == "title" && !treeView.isContainer(cell.row) )` → `aEvent.stopPropagation()`
- 条件付き依存: `if (cell.col.id == "restore")` → `toggleRowChecked()`
- 参照: `AppConstants.platform`, `aEvent.button`, `aEvent.clientX`, `aEvent.clientY`, `aEvent.ctrlKey`, `aEvent.detail`, `aEvent.metaKey`, `aEvent.shiftKey`, `cell.col`, `cell.col.id`, `cell.row`

## onListKeyDown()
- 位置: L272-286
- 役割: スペースで現在行のチェックを切り替え、Ctrl+Enter で非コンテナ行を 1 タブ復元する。
- 触るとき: キーボードでの一覧操作を変えるとき。
- 呼び出し先: `aEvent.preventDefault()`, `getTabList()`, `toggleRowChecked()`, `treeView.isContainer()`
- 条件付き依存: `if (aEvent.ctrlKey && !treeView.isContainer(ix))` → `restoreSingleTab()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `aEvent.ctrlKey`, `aEvent.keyCode`, `aEvent.shiftKey`, `getTabList().currentIndex`

## getTabList()
- 位置: L293-295
- 役割: id が tabList の一覧要素を返す。
- 触るとき: 一覧要素の id を変えるとき、またはこの要素を参照する箇所を探すとき。
- 呼び出し先: `document.getElementById()`

## getTryAgainButton()
- 位置: L300-304
- 役割: id が errorTryAgain の再試行ボタンを返す。
- 触るとき: 再試行ボタンのイベントや無効化を調べるとき。
- 呼び出し先: `document.getElementById()`

## getBrowserWindow()
- 位置: L309-314
- 役割: このページが入っているトップの chrome ウィンドウを返す。
- 触るとき: 復元先のブラウザウィンドウの取り方を変えるとき。
- 参照: `(window.browsingContext) .topChromeWindow`, `window.browsingContext`

## toggleRowChecked()
- 位置: L316-349
- 役割: 行のチェックを反転する。窓の行なら配下のタブも揃え、タブの行なら窓の状態（全部・一部・なし）を更新し、必要なら再試行ボタンを無効にする。
- 触るとき: チェック状態が窓とタブ間で食い違う問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `treeView.isContainer()`, `treeView.treeBox.invalidateRow()`
- 条件付き依存: `if (treeView.isContainer(aIx))` → `treeView.treeBox.invalidateRow()`
- 条件付き依存: `if (treeView.isContainer(aIx))` → `gTreeData.indexOf()`
- 条件付き依存: `if (!(treeView.isContainer(aIx)))` → `item.parent.tabs.every()`
- 条件付き依存: `if (!(item.parent.tabs.every(isChecked)))` → `item.parent.tabs.some()`
- 条件付き依存: `if (!(treeView.isContainer(aIx)))` → `treeView.treeBox.invalidateRow()`
- 条件付き依存: `if (!(treeView.isContainer(aIx)))` → `gTreeData.indexOf()`
- 条件付き依存: `if (document.getElementById("errorCancel"))` → `getTryAgainButton()`
- 条件付き依存: `if (document.getElementById("errorCancel"))` → `gTreeData.some()`
- 参照: `getTryAgainButton().disabled`, `item.checked`, `item.parent`, `item.parent.checked`, `item.tabs`, `tab.checked`

## isChecked()
- 位置: L317-319
- 役割: 項目の checked 値を返す、every と some に渡すための小さな判定関数。
- 触るとき: チェック済みかどうかの判定を変えるとき。
- 参照: `aItem.checked`

## restoreSingleTab()
- 位置: L351-370
- 役割: 現在のブラウザに新しいタブを作り、対象のタブ状態を hidden を false にして設定する。Shift と loadInBackground の設定で前面に出すかを決める。
- 触るとき: 1 タブだけ復元した際の表示位置や前面化を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.getBoolPref()`, `gTreeData.indexOf()`, `getBrowserWindow()`, `lazy.SessionStore.setTabState()`, `tabbrowser.addWebTab()`
- 参照: `gStateObject.windows`, `gStateObject.windows[item.parent.ix].tabs`, `getBrowserWindow().gBrowser`, `item.parent`, `item.parent.ix`, `tabState.hidden`, `tabbrowser.selectedTab`
- XPCOM: `Services.prefs`

## rowCount()
- 位置: L378-380
- 役割: ツリーの行数（gTreeData の長さ）を返す。
- 触るとき: ツリーの行数の扱いを変えるとき。
- 参照: `gTreeData.length`

## setTree()
- 位置: L381-383
- 役割: ツリーの box を保持する。
- 触るとき: ツリーの初期化順序を変えるとき。
- 参照: `this.treeBox`

## getCellText()
- 位置: L384-386
- 役割: 行の表示名を返す。
- 触るとき: 一覧の表示名を変えるとき。
- 参照: `gTreeData[idx].label`

## isContainer()
- 位置: L387-389
- 役割: 行に open プロパティがあれば窓の行（コンテナ）と判定する。
- 触るとき: 窓の行とタブの行を区別する条件を変えるとき。

## getCellValue()
- 位置: L390-392
- 役割: 行の checked を文字列にして返す。
- 触るとき: チェック列の表示値の扱いを変えるとき。
- 呼び出し先: `String()`
- 参照: `gTreeData[idx].checked`

## isContainerOpen()
- 位置: L393-395
- 役割: 窓の行が展開されているかを返す。
- 触るとき: 窓の展開状態の表示を変えるとき。
- 参照: `gTreeData[idx].open`

## isContainerEmpty()
- 位置: L396-398
- 役割: 常に false を返す。
- 触るとき: 空の窓の行を表示する要件が出たとき。

## isSeparator()
- 位置: L399-401
- 役割: 常に false を返す（区切り行は使わない）。
- 触るとき: 一覧に区切り行を入れるとき。

## isSorted()
- 位置: L402-404
- 役割: 常に false を返す（並べ替えなし）。
- 触るとき: 一覧の並べ替えを追加するとき。

## isEditable()
- 位置: L405-407
- 役割: 常に false を返す（編集不可）。
- 触るとき: 一覧のセルを編集可能にするとき。

## canDrop()
- 位置: L408-410
- 役割: 常に false を返す（ドロップ不可）。
- 触るとき: 一覧へのドラッグ＆ドロップを追加するとき。

## getLevel()
- 位置: L411-413
- 役割: 窓の行を 0、タブの行を 1 の階層として返す。
- 触るとき: 一覧の階層表示を変えるとき。
- 呼び出し先: `this.isContainer()`

## getParentIndex()
- 位置: L415-424
- 役割: タブの行なら直前にある窓の行の位置を返し、窓の行は -1 を返す。
- 触るとき: 展開・折りたたみで親子の対応がずれるとき。
- 呼び出し先: `this.isContainer()`
- 条件付き依存: `if (!this.isContainer(idx))` → `this.isContainer()`

## hasNextSibling()
- 位置: L426-434
- 役割: 同じ階層の次の行があるかを、浅い階層に出会うまで前へ走査して判定する。
- 触るとき: ツリーの接続線の描画がずれるとき。
- 呼び出し先: `this.getLevel()`
- 条件付き依存: `if (this.getLevel(t) <= thisLevel)` → `this.getLevel()`
- 参照: `gTreeData.length`

## toggleOpenState()
- 位置: L436-464
- 役割: 窓の行を展開するとき配下のタブ行を挿入し、折りたたむとき配下の行を取り除き、行数の変化をツリーに通知する。
- 触るとき: 窓の展開・折りたたみで行がずれる問題を調べるとき。
- 呼び出し先: `this.isContainer()`, `this.treeBox.invalidateRow()`
- 条件付き依存: `if (item.open)` → `this.getLevel()`
- 条件付き依存: `if (item.open)` → `gTreeData.splice()`
- 条件付き依存: `if (item.open)` → `this.treeBox.rowCountChanged()`
- 条件付き依存: `if (!(item.open))` → `gTreeData.splice()`
- 条件付き依存: `if (!(item.open))` → `this.treeBox.rowCountChanged()`
- 参照: `gTreeData.length`, `gTreeData[idx].tabs`, `item.open`, `toinsert.length`

## getCellProperties()
- 位置: L466-479
- 役割: チェック列で一部だけ選ばれた窓に partial を、タイトル列にアイコンの有無に応じて icon か noicon を返す。
- 触るとき: 一部選択の窓の見た目や、アイコンの有無による表示を変えるとき。
- 呼び出し先: `this.isContainer()`
- 条件付き依存: `if (column.id == "title")` → `this.getImageSrc()`
- 参照: `column.id`, `gTreeData[idx].checked`

## getRowProperties()
- 位置: L481-488
- 役割: 窓の番号が奇数の行に alternate を返して縞模様にする。
- 触るとき: 行の縞模様の付け方を変えるとき。
- 参照: `gTreeData[idx].parent`, `winState.ix`

## getImageSrc()
- 位置: L490-495
- 役割: タイトル列でタブの favicon の URL を返し、なければ null を返す。
- 触るとき: 一覧のアイコンが出ないときに調べるとき。
- 参照: `column.id`, `gTreeData[idx].src`

## setCellValue()
- 位置: L497-497
- 役割: 何もしない（ツリーの値の書き込みは受け付けない）。
- 触るとき: セルの値を書き換える操作を足すとき。

## setCellText()
- 位置: L498-498
- 役割: 何もしない（セル文字列の書き込みは受け付けない）。
- 触るとき: セルの文字列を書き換える操作を足すとき。

## drop()
- 位置: L499-499
- 役割: 何もしない（ドロップ処理なし）。
- 触るとき: ドロップ処理を足すとき。

## cycleHeader()
- 位置: L500-500
- 役割: 何もしない（列見出しのクリック処理なし）。
- 触るとき: 列見出しの並べ替えを足すとき。

## cycleCell()
- 位置: L501-501
- 役割: 何もしない（セルのクリック処理なし）。
- 触るとき: セルの操作を足すとき。

## selectionChanged()
- 位置: L502-502
- 役割: 何もしない（選択変更の処理なし）。
- 触るとき: 選択に応じた処理を足すとき。

## getColumnProperties()
- 位置: L503-505
- 役割: 常に空文字を返す（列の追加プロパティなし）。
- 触るとき: 列ごとのスタイルを足すとき。
