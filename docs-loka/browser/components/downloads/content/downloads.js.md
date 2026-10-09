# browser/components/downloads/content/downloads.js

source: browser/components/downloads/content/downloads.js
source-hash: 311e0d736c78077b3e095156b35f558012e29883
lines: 1891

## <module>
- 役割: 各ウィンドウのダウンロードパネル(一覧、件数表示、コマンド処理、ブロック時と非公開時のサブビュー)のUIを提供する。DownloadsPanel、DownloadsView、DownloadsViewItem、DownloadsViewController などを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Integration.downloads.defineESModuleGetter()`, `XPCOMUtils.defineConstant()`, `document.getElementById()`

## initialize()
- 位置: L79-127
- 役割: DownloadsPanel を初期化し、イベントリスナ、ビュー、データ取得を接続する。
- 触るとき: パネル起動時の購読処理や、ダウンロードデータがいつ読み込まれるかを変えるとき。spam 保護の register もここで呼ばれる。
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getData(window).addView()`, `DownloadsCommon.getSummary()`, `DownloadsCommon.getSummary(window, DownloadsView.kItemCountLimit).addView()`, `DownloadsCommon.initializeAllDataLinks()`, `DownloadsCommon.log()`, `DownloadsPanel._attachEventListeners()`, `DownloadsViewController.initialize()`, `document.getElementById()`, `downloadPanelCommands.addEventListener()`, `goUpdateCommand()`, `window.addEventListener()`
- 条件付き依存: `if (DownloadIntegration.downloadSpamProtection)` → `DownloadIntegration.downloadSpamProtection.register()`
- 条件付き依存: `if (this._initialized)` → `DownloadsCommon.log()`
- 参照: `DownloadIntegration.downloadSpamProtection`, `DownloadsView.kItemCountLimit`, `this._initialized`, `this.onWindowUnload`, `this.panel.hidden`

## terminate()
- 位置: L134-167
- 役割: 初期化の逆操作として、パネルを閉じ、ビューとサマリーの購読とリスナを外す。
- 触るとき: ウィンドウを閉じるときや再初期化の後始末で、登録した購読の解除漏れを確かめるとき。
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getData(window).removeView()`, `DownloadsCommon.getSummary()`, `DownloadsCommon.getSummary( window, DownloadsView.kItemCountLimit ).removeView()`, `DownloadsCommon.log()`, `DownloadsViewController.terminate()`, `document .getElementById()`, `document .getElementById("downloadPanelCommands") .removeEventListener()`, `this._unattachEventListeners()`, `this.hidePanel()`, `window.removeEventListener()`
- 条件付き依存: `if (!this._initialized)` → `DownloadsCommon.log()`
- 条件付き依存: `if (DownloadIntegration.downloadSpamProtection)` → `DownloadIntegration.downloadSpamProtection.unregister()`
- 参照: `DownloadIntegration.downloadSpamProtection`, `DownloadsSummary.active`, `DownloadsView.kItemCountLimit`, `this._initialized`, `this.onWindowUnload`

## panel()
- 位置: L174-177
- 役割: downloadsPanel 要素を遅延取得し、以後はゲッターを値に置き換える。
- 触るとき: パネルの DOM 要素 ID を変えるとき、または要素を参照する前の初期化順序を確かめるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.panel`

## showPanel()
- 位置: L185-211
- 役割: パネルの表示を要求する。表示中ならフォーカスだけ行い、未表示なら初期化してデータ準備後に開く。
- 触るとき: ダウンロードボタンやショートカットからパネルを開く経路を変えるとき。Glean の panelShown 計測もここにある。
- 呼び出し先: `DownloadsButton.unhide()`, `DownloadsCommon.log()`, `Glean.downloads.panelShown.add()`, `setTimeout()`, `this._openPopupIfDataReady()`, `this.initialize()`
- 条件付き依存: `if (this.isPanelShowing)` → `DownloadsCommon.log()`
- 条件付き依存: `if (this.isPanelShowing)` → `this._focusPanel()`
- 参照: `this._openedManually`, `this._preventFocusRing`, `this._waitingDataForOpen`, `this.isPanelShowing`

## hidePanel()
- 位置: L217-227
- 役割: パネルが表示中なら閉じる。内部状態は残して再表示を速くする。
- 触るとき: 別の操作から閉じる処理を呼ぶとき、または履歴画面を開く前に閉じる順序を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `PanelMultiView.hidePopup()`
- 条件付き依存: `if (!this.isPanelShowing)` → `DownloadsCommon.log()`
- 参照: `this.isPanelShowing`, `this.panel`

## isPanelShowing()
- 位置: L234-236
- 役割: 待機中の表示要求か、パネルの state が closed 以外かで表示中を判定する。閉じている途中も含む。
- 触るとき: 表示状態の判定条件を変えるとき、または閉じている途中の扱いを確かめるとき。
- 参照: `this._waitingDataForOpen`, `this.panel.state`

## handleEvent()
- 位置: L238-314
- 役割: パネルと一覧に登録したイベントを種類ごとに振り分け、対応するハンドラへ渡す。
- 触るとき: パネルに新しいイベントを購読させるとき、または特定のイベントがどの処理に届くかを追うとき。
- 呼び出し先: `DownloadsPanel.showDownloadsHistory()`, `DownloadsView._onDownloadContextMenu()`, `DownloadsView._onDownloadDragStart()`, `DownloadsView._onDownloadMouseOut()`, `DownloadsView._onDownloadMouseOver()`, `DownloadsView.richListBox.hasAttribute()`, `goDoCommand()`, `this._onKeyDown()`, `this._onKeyPress()`, `this._onPopupHidden()`, `this._onPopupShown()`, `this._onSelect()`, `this.panel.contains()`
- 条件付き依存: `if (aEvent.currentTarget == DownloadsView.downloadsHistory)` → `DownloadsPanel.showDownloadsHistory()`
- 条件付き依存: `if ( aEvent.currentTarget == DownloadsBlockedSubview.elements.deleteButton )` → `DownloadsBlockedSubview.confirmBlock()`
- 条件付き依存: `if ( !DownloadsView.contextMenuOpen && !DownloadsView.subViewOpen && this.panel.contains(document.activeElement) )` → `document.activeElement.blur()`
- 条件付き依存: `if ( !DownloadsView.contextMenuOpen && !DownloadsView.subViewOpen && this.panel.contains(document.activeElement) )` → `DownloadsView.richListBox.removeAttribute()`
- 条件付き依存: `if ( !DownloadsView.contextMenuOpen && !DownloadsView.subViewOpen && this.panel.contains(document.activeElement) )` → `this._focusPanel()`
- 条件付き依存: `if (DownloadsView.richListBox.hasAttribute("disabled"))` → `this._handlePotentiallySpammyDownloadActivation()`
- 条件付き依存: `if (aEvent.currentTarget == DownloadsSummary._summaryNode)` → `DownloadsSummary._onKeyDown()`
- 参照: `DownloadsBlockedSubview.elements.deleteButton`, `DownloadsSummary._summaryNode`, `DownloadsView.contextMenuOpen`, `DownloadsView.downloadsHistory`, `DownloadsView.subViewOpen`, `aEvent.currentTarget`, `aEvent.target.id`, `aEvent.type`, `document.activeElement`, `this._preventFocusRing`

## onViewLoadCompleted()
- 位置: L321-323
- 役割: データ読み込み完了の通知を受け、開く保留があればパネルを開く。
- 触るとき: 読み込み完了後にパネルを開くタイミングを変えるとき。
- 呼び出し先: `this._openPopupIfDataReady()`

## onWindowUnload()
- 位置: L327-330
- 役割: ウィンドウのアンロード時に DownloadsPanel.terminate を呼ぶ。
- 触るとき: ウィンドウ終了時の後始末を変えるとき。イベントから呼ばれるため this を使わず DownloadsPanel を直接参照する。
- 呼び出し先: `DownloadsPanel.terminate()`

## _onPopupShown()
- 位置: L332-350
- 役割: パネル自身の popupshown で、注目抑制フラグを立て、先頭項目を選んでフォーカスを移す。
- 触るとき: パネルが開いたときの選択位置、フォーカス移動、通知の抑制を変えるとき。
- 呼び出し先: `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.log()`, `this._focusPanel()`
- 参照: `DownloadsCommon.SUPPRESS_PANEL_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `DownloadsView.richListBox.itemCount`, `DownloadsView.richListBox.selectedIndex`, `aEvent.target`, `this.panel`

## _onPopupHidden()
- 位置: L352-375
- 役割: パネルが閉じたとき、遅延タイマーと抑制フラグを解除し、アンカーボタンの固定を解く。
- 触るとき: 閉じた後の後始末(遅延の解除、フラグ、アンカーの解放)に抜けがないか確かめるとき。
- 呼び出し先: `DownloadsButton.releaseAnchor()`, `DownloadsCommon.getIndicatorData()`, `DownloadsCommon.log()`, `DownloadsView.richListBox.removeAttribute()`
- 条件付き依存: `if (this._delayTimeout)` → `DownloadsView.richListBox.removeAttribute()`
- 条件付き依存: `if (this._delayTimeout)` → `clearTimeout()`
- 条件付き依存: `if (this._delayTimeout)` → `this._stopWatchingForSpammyDownloadActivation()`
- 参照: `DownloadsCommon.SUPPRESS_PANEL_OPEN`, `DownloadsCommon.getIndicatorData(window).attentionSuppressed`, `aEvent.target`, `this._delayTimeout`, `this.panel`

## showDownloadsHistory()
- 位置: L382-389
- 役割: パネルを閉じてから BrowserCommands.downloadsUI で履歴画面を開く。
- 触るとき: 「すべてのダウンロードを表示」の動作や、パネルを閉じる順序を変えるとき。
- 呼び出し先: `BrowserCommands.downloadsUI()`, `DownloadsCommon.log()`, `this.hidePanel()`

## _attachEventListeners()
- 位置: L398-423
- 役割: パネル、一覧、履歴ボタン、ブロック解除ボタン、サマリーに必要なイベントリスナを登録する。
- 触るとき: パネルに新しい購読を足すとき。対になる _unattachEventListeners と同じ内容に揃える必要がある。
- 呼び出し先: `DownloadsBlockedSubview.elements.deleteButton.addEventListener()`, `DownloadsSummary._summaryNode.addEventListener()`, `DownloadsView.downloadsHistory.addEventListener()`, `DownloadsView.richListBox.addEventListener()`, `this.panel.addEventListener()`

## _unattachEventListeners()
- 位置: L429-449
- 役割: _attachEventListeners で登録したリスナを同じ組み合わせで解除する。
- 触るとき: リスナを追加または削除するとき、解除漏れがないか突き合わせるとき。
- 呼び出し先: `DownloadsBlockedSubview.elements.deleteButton.removeEventListener()`, `DownloadsSummary._summaryNode.removeEventListener()`, `DownloadsView.downloadsHistory.removeEventListener()`, `DownloadsView.richListBox.removeEventListener()`, `this.panel.removeEventListener()`

## _onKeyPress()
- 位置: L451-461
- 役割: 修飾キーなしの keypress を、一覧が直接フォーカスされている時だけ onDownloadKeyPress へ渡す。
- 触るとき: パネルでのスペースや Enter の扱いを変えるとき。
- 条件付き依存: `if (document.activeElement === DownloadsView.richListBox)` → `DownloadsView.onDownloadKeyPress()`
- 参照: `DownloadsView.richListBox`, `aEvent.altKey`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `document.activeElement`

## _onKeyDown()
- 位置: L468-551
- 役割: keydown で、無効化中の警告、上下キーのフォーカス移動、Accel+V による貼り付けダウンロードを処理する。
- 触るとき: キーボードでのフォーカス移動を変えるとき、またはクリップボードの URL からダウンロードを始める経路を調べるとき。貼り付けは text/x-moz-url か text/plain の先頭行を URL として DownloadURL に渡し、失敗は握りつぶす。
- 呼び出し先: `Cc["@mozilla.org/widget/transferable;1"].createInstance()`, `DownloadURL()`, `DownloadsCommon.log()`, `DownloadsView.richListBox.hasAttribute()`, `NetUtil.newURI()`, `Services.clipboard.getData()`, `aEvent.getModifierState()`, `data.value .QueryInterface()`, `data.value .QueryInterface(Ci.nsISupportsString) .data.split()`, `flavors.forEach()`, `trans.getAnyTransferData()`, `trans.init()`
- 条件付き依存: `if (DownloadsView.richListBox.hasAttribute("disabled"))` → `this._handlePotentiallySpammyDownloadActivation()`
- 条件付き依存: `if ( aEvent.keyCode == aEvent.DOM_VK_UP || aEvent.keyCode == aEvent.DOM_VK_DOWN )` → `richListBox.setAttribute()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_UP && richListBox.firstElementChild)` → `document .getElementById("downloadsFooter") .contains()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_UP && richListBox.firstElementChild)` → `document .getElementById()`
- 条件付き依存: `if ( document .getElementById("downloadsFooter") .contains(document.activeElement) )` → `richListBox.focus()`
- 条件付き依存: `if ( document .getElementById("downloadsFooter") .contains(document.activeElement) )` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_DOWN)` → `document .getElementById("downloadsFooter") .contains()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_DOWN)` → `document .getElementById()`
- 条件付き依存: `if ( DownloadsView.canChangeSelectedItem && (richListBox.selectedItem === richListBox.lastElementChild || document .getElementById("downloadsFooter") .contains(d...)` → `DownloadsFooter.focus()`
- 条件付き依存: `if ( DownloadsView.canChangeSelectedItem && (richListBox.selectedItem === richListBox.lastElementChild || document .getElementById("downloadsFooter") .contains(d...)` → `aEvent.preventDefault()`
- 参照: `Ci.nsISupportsString`, `Ci.nsITransferable`, `DownloadsView.canChangeSelectedItem`, `DownloadsView.richListBox`, `Services.clipboard.kGlobalClipboard`, `aEvent.DOM_VK_DOWN`, `aEvent.DOM_VK_UP`, `aEvent.DOM_VK_V`, `aEvent.keyCode`, `document.activeElement`, `richListBox.firstElementChild`, `richListBox.lastElementChild`, `richListBox.selectedIndex`, `richListBox.selectedItem`, `trans.addDataFlavor`, `uri.spec`
- XPCOM: [`nsISupportsString`](../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsITransferable`](../../../../dom/interfaces/base/nsIDOMWindowUtils.idl.md) / `@mozilla.org/widget/transferable;1` / `Services.clipboard`

## _onSelect()
- 位置: L553-563
- 役割: 一覧の各項目のボタンについて、選択中は tabindex を外し、それ以外は -1 にして Tab の移動から外す。
- 触るとき: 項目内のボタンのフォーカス順序を変えるとき。
- 呼び出し先: `item.querySelector()`, `richlistbox.itemChildren.forEach()`
- 条件付き依存: `if (item.selected)` → `button.removeAttribute()`
- 条件付き依存: `if (!(item.selected))` → `button.setAttribute()`
- 参照: `DownloadsView.richListBox`, `item.selected`

## _focusPanel()
- 位置: L569-594
- 役割: パネルが開いていて内部にフォーカスがない時だけ、一覧の先頭項目か、項目がなければフッターへフォーカスを移す。
- 触るとき: パネルを開いた直後のフォーカス先や、フォーカスリングの表示を変えるとき。
- 呼び出し先: `this.panel.contains()`, `this.panel.shadowRoot.contains()`
- 条件付き依存: `if (DownloadsView.richListBox.itemCount > 0)` → `DownloadsView.richListBox.focus()`
- 条件付き依存: `if (!(DownloadsView.richListBox.itemCount > 0))` → `DownloadsFooter.focus()`
- 参照: `DownloadsView.canChangeSelectedItem`, `DownloadsView.richListBox.itemCount`, `DownloadsView.richListBox.selectedIndex`, `document.activeElement`, `focusOptions.focusVisible`, `this._preventFocusRing`, `this.panel.state`

## _delayPopupItems()
- 位置: L596-601
- 役割: 一覧を disabled にし、誤操作防止の監視と遅延タイマーを始める。
- 触るとき: 自動で表示したパネルで誤クリックを防ぐ遅延の仕組みを変えるとき。
- 呼び出し先: `DownloadsView.richListBox.setAttribute()`, `this._refreshDelayTimer()`, `this._startWatchingForSpammyDownloadActivation()`

## _refreshDelayTimer()
- 位置: L603-616
- 役割: security.dialog_enable_delay の時間だけ一覧の無効化を遅らせるタイマーを張り直す。
- 触るとき: 遅延時間の設定を変えるとき、またはタイマーを延長する条件を変えるとき。
- 呼び出し先: `DownloadsView.richListBox.removeAttribute()`, `Services.prefs.getIntPref()`, `setTimeout()`, `this._focusPanel()`, `this._stopWatchingForSpammyDownloadActivation()`
- 条件付き依存: `if (this._delayTimeout)` → `clearTimeout()`
- 参照: `this._delayTimeout`
- XPCOM: `Services.prefs`

## _startWatchingForSpammyDownloadActivation()
- 位置: L618-623
- 役割: ウィンドウに capture 段階の keydown リスナを付け、無効化中の入力の監視を始める。
- 触るとき: 遅延中の入力監視の範囲を変えるとき。
- 呼び出し先: `window.addEventListener()`

## _handlePotentiallySpammyDownloadActivation()
- 位置: L626-641
- 役割: 無効化中に Enter、スペース、主ボタンが押されたら警告音を鳴らし(1秒に1回まで)、遅延タイマーを張り直す。
- 触るとき: 無効化中の入力への反応や音の扱いを変えるとき。
- 呼び出し先: `aEvent.type.startsWith()`
- 条件付き依存: `if (isSpammyKey || isSpammyMouse)` → `Date.now()`
- 条件付き依存: `if (Date.now() - this._lastBeepTime > 1000)` → `Cc["@mozilla.org/sound;1"].getService(Ci.nsISound).beep()`
- 条件付き依存: `if (Date.now() - this._lastBeepTime > 1000)` → `Cc["@mozilla.org/sound;1"].getService()`
- 条件付き依存: `if (Date.now() - this._lastBeepTime > 1000)` → `Date.now()`
- 条件付き依存: `if (isSpammyKey || isSpammyMouse)` → `this._refreshDelayTimer()`
- 参照: `Ci.nsISound`, `aEvent.button`, `aEvent.key`, `this._lastBeepTime`
- XPCOM: `nsISound` / `@mozilla.org/sound;1`

## _stopWatchingForSpammyDownloadActivation()
- 位置: L643-648
- 役割: _startWatchingForSpammyDownloadActivation で付けた keydown リスナを外す。
- 触るとき: 監視の解除漏れを確かめるとき。
- 呼び出し先: `window.removeEventListener()`

## _openPopupIfDataReady()
- 位置: L653-728
- 役割: 読み込み完了済みで保留中なら、アンカーを確かめてパネルを開く。非公開ブラウズでは削除の選択を促す。
- 触るとき: パネルを開く条件(最小化、読み込み中、アンカー不在)や非公開時の確認を変えるとき。
- 呼び出し先: `DownloadsButton.getAnchor()`, `DownloadsCommon.log()`, `DownloadsView._visibleViewItems.values()`, `PanelMultiView.openPopup()`, `PanelMultiView.openPopup( this.panel, anchor, "bottomright topright", 0, 0, false, null ).then()`, `PrivateBrowsingUtils.isContentWindowPrivate()`, `Services.prefs.getBoolPref()`, `anchor.closest()`, `setTimeout()`, `this.panel.classList.toggle()`, `viewItem.download.refresh()`, `viewItem.download.refresh().catch()`
- 条件付き依存: `if (!anchor)` → `DownloadsCommon.error()`
- 条件付き依存: `if (!this._openedManually)` → `this._delayPopupItems()`
- 条件付き依存: `if ( // If private, show message asking whether to delete files at end of session isPrivate && Services.prefs.getBoolPref( "browser.download.enableDeletePrivate"...)` → `PrivateDownloadsSubview.openWhenReady()`
- 参照: `DownloadsView.loading`, `console.error`, `this._openedManually`, `this._waitingDataForOpen`, `this.panel`, `window.STATE_MINIMIZED`, `window.windowState`
- XPCOM: `Services.prefs`

## _itemCountChanged()
- 位置: L776-799
- 役割: 件数に応じて hasdownloads 属性を付け外しし、上限を超えた分があればサマリーを有効にする。
- 触るとき: 件数表示やサマリーを出す条件を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`
- 条件付き依存: `if (count > 0)` → `DownloadsCommon.log()`
- 条件付き依存: `if (count > 0)` → `DownloadsPanel.panel.setAttribute()`
- 条件付き依存: `if (!(count > 0))` → `DownloadsCommon.log()`
- 条件付き依存: `if (!(count > 0))` → `DownloadsPanel.panel.removeAttribute()`
- 参照: `DownloadsSummary.active`, `this._downloads.length`, `this.kItemCountLimit`

## richListBox()
- 位置: L804-807
- 役割: downloadsListBox 要素を遅延取得する。
- 触るとき: 一覧の要素 ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.richListBox`

## downloadsHistory()
- 位置: L812-816
- 役割: 「すべて表示」ボタン downloadsHistory を遅延取得する。
- 触るとき: 履歴ボタンの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.downloadsHistory`

## onDownloadBatchStarting()
- 位置: L823-826
- 役割: まとめ読み込みの開始時に loading を true にする。
- 触るとき: 読み込み中に件数更新を抑える条件を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`
- 参照: `this.loading`

## onDownloadBatchEnded()
- 位置: L831-843
- 役割: 読み込み終了時に loading を戻し、件数を一度だけ更新して、パネルへ読み込み完了を通知する。
- 触るとき: 読み込み完了後の処理を足すか変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `DownloadsPanel.onViewLoadCompleted()`, `this._itemCountChanged()`
- 参照: `this.loading`

## onDownloadAdded()
- 位置: L852-870
- 役割: 新しいデータを配列の先頭に入れ、項目を上に挿入する。上限を超えたら末尾の表示項目を外す。
- 触るとき: 新着ダウンロードが一覧に出る経路や、表示上限(kItemCountLimit)の扱いを変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `this._addViewItem()`, `this._downloads.unshift()`
- 条件付き依存: `if (this._downloads.length > this.kItemCountLimit)` → `this._removeViewItem()`
- 条件付き依存: `if (!this.loading)` → `this._itemCountChanged()`
- 参照: `this._downloads`, `this._downloads.length`, `this.kItemCountLimit`, `this.loading`

## onDownloadChanged()
- 位置: L872-877
- 役割: 表示中の項目なら、その項目の onChanged に状態更新を任せる。
- 触るとき: ダウンロードの状態変化が表示にどう届くかを追うとき。
- 呼び出し先: `this._visibleViewItems.get()`
- 条件付き依存: `if (viewItem)` → `viewItem.onChanged()`

## onDownloadRemoved()
- 位置: L886-902
- 役割: データ配列から取り除き、表示中なら項目を外す。残りがあれば配列の次の項目を表示に入れる。
- 触るとき: 削除時に表示が詰まって次の項目が出る挙動を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `this._downloads.indexOf()`, `this._downloads.splice()`, `this._itemCountChanged()`
- 条件付き依存: `if (itemIndex < this.kItemCountLimit)` → `this._removeViewItem()`
- 条件付き依存: `if (this._downloads.length >= this.kItemCountLimit)` → `this._addViewItem()`
- 参照: `this._downloads`, `this._downloads.length`, `this.kItemCountLimit`

## itemForElement()
- 位置: L910-912
- 役割: richlistitem 要素から対応する DownloadsViewItem を引く。
- 触るとき: 要素から項目を取り出す箇所を追うとき、またはマップの持ち方を変えるとき。
- 呼び出し先: `this._itemsForElements.get()`

## _addViewItem()
- 位置: L918-940
- 役割: richlistitem を作って DownloadsViewItem と結び付け、先頭か末尾に挿入して有効化する。
- 触るとき: 項目の DOM を生成する処理や挿入位置を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `document.createXULElement()`, `element.setAttribute()`, `this._itemsForElements.set()`, `this._visibleViewItems.set()`, `viewItem.ensureActive()`
- 条件付き依存: `if (aNewest)` → `this.richListBox.insertBefore()`
- 条件付き依存: `if (!(aNewest))` → `this.richListBox.appendChild()`
- 参照: `this.richListBox.firstElementChild`

## _removeViewItem()
- 位置: L945-960
- 役割: 項目の要素を一覧から外して選択位置を補正し、2つのマップから対応を消す。
- 触るとき: 項目を消したときの選択位置の扱いや、マップの解放を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `this._itemsForElements.delete()`, `this._visibleViewItems.delete()`, `this._visibleViewItems.get()`, `this.richListBox.removeChild()`
- 条件付き依存: `if (previousSelectedIndex != -1)` → `Math.min()`
- 参照: `this._visibleViewItems.get(download).element`, `this.richListBox.itemCount`, `this.richListBox.selectedIndex`

## onDownloadClick()
- 位置: L964-996
- 役割: 主ボタン領域のクリックを、修飾キーに応じた開く系コマンドに変換して実行する。ブロック時は詳細表示にする。
- 触るとき: クリックで開く、タブで開く、ブロック情報を出す挙動を変えるとき。完了後に開く設定の切り替えもここで行う。
- 呼び出し先: `aEvent.target.closest()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `aEvent.target.closest()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `target.closest("richlistbox").hasAttribute()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `target.closest()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `DownloadsView.itemForElement()`
- 条件付き依存: `if (aEvent.shiftKey || aEvent.ctrlKey || aEvent.metaKey)` → `BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (aEvent.shiftKey || aEvent.ctrlKey || aEvent.metaKey)` → `["tab", "window", "tabshifted"].includes()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `command.startsWith()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `DownloadsCommon.log()`
- 条件付き依存: `if (aEvent.button == 0 && aEvent.target.closest(".downloadMainArea"))` → `goDoCommand()`
- 参照: `DownloadsView.itemForElement(target).download`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `download._launchedFromPanel`, `download.hasBlockedData`, `download.launchWhenSucceeded`, `download.stopped`, `download.succeeded`

## onDownloadButton()
- 位置: L998-1001
- 役割: 項目内のボタンが押されたとき、対応する項目の onButton を呼ぶ。
- 触るとき: 項目のボタン押下時の処理を追うとき。
- 呼び出し先: `DownloadsView.itemForElement()`, `DownloadsView.itemForElement(target).onButton()`, `event.target.closest()`

## onDownloadKeyPress()
- 位置: L1006-1028
- 役割: 項目上のキー入力で、スペースは一時停止と再開、Enter は既定の動作を実行する。
- 触るとき: 項目へのキーボード操作を変えるとき。
- 呼び出し先: `" ".charCodeAt()`, `aEvent.originalTarget.hasAttribute()`
- 条件付き依存: `if (aEvent.charCode == " ".charCodeAt(0))` → `aEvent.preventDefault()`
- 条件付き依存: `if (aEvent.charCode == " ".charCodeAt(0))` → `goDoCommand()`
- 条件付き依存: `if (readyToDownload)` → `goDoCommand()`
- 参照: `DownloadsView.richListBox.disabled`, `KeyEvent.DOM_VK_RETURN`, `aEvent.charCode`, `aEvent.keyCode`

## contextMenu()
- 位置: L1030-1037
- 役割: downloadsContextMenu を取得する。見つかれば以後のアクセス用に値を固定する。
- 触るとき: コンテキストメニューの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.contextMenu`

## contextMenuOpen()
- 位置: L1042-1044
- 役割: コンテキストメニューが閉じていなければ true を返す。
- 触るとき: メニューの開閉中に選択変更を抑える条件を調べるとき。
- 参照: `this.contextMenu.state`

## canChangeSelectedItem()
- 位置: L1049-1053
- 役割: コンテキストメニューもサブビューも開いていない時だけ、選択を変えてよいと返す。
- 触るとき: マウスやキーで選択を移せる条件を変えるとき。
- 参照: `this.contextMenuOpen`, `this.subViewOpen`

## _onDownloadMouseOver()
- 位置: L1058-1076
- 役割: マウスが項目に入ると、ホバー用のクラスを付け、選択可能なら項目を選択する。
- 触るとき: マウスホバー時の見た目や選択の連動を変えるとき。
- 呼び出し先: `aEvent.target.classList.contains()`, `aEvent.target.closest()`, `item.classList.toggle()`
- 条件付き依存: `if (aEvent.target.classList.contains("downloadButton"))` → `item.classList.add()`
- 参照: `item.localName`, `this.canChangeSelectedItem`, `this.richListBox.selectedItem`

## _onDownloadMouseOut()
- 位置: L1078-1093
- 役割: マウスが項目の外へ出たとき、ホバー用のクラスを外し、選択を解除する。
- 触るとき: マウスが離れたときの選択解除を変えるとき。
- 呼び出し先: `aEvent.target.classList.contains()`, `aEvent.target.closest()`, `item.contains()`
- 条件付き依存: `if (aEvent.target.classList.contains("downloadButton"))` → `item.classList.remove()`
- 参照: `aEvent.relatedTarget`, `item.localName`, `this.canChangeSelectedItem`, `this.richListBox.selectedIndex`

## _onDownloadContextMenu()
- 位置: L1095-1116
- 役割: 右クリックされた項目を選択し、メニューを更新して、コピーと参照元メニューの表示を調整する。
- 触るとき: 右クリックメニューの内容や表示条件を変えるとき。
- 呼び出し先: `DownloadsViewController.updateCommands()`, `DownloadsViewUI.updateContextMenuForElement()`, `aEvent.originalTarget.closest()`, `element._shell.isCommandEnabled()`, `this.contextMenu.querySelector()`
- 条件付き依存: `if (!element)` → `aEvent.preventDefault()`
- 参照: `this.contextMenu`, `this.contextMenu.querySelector(".downloadCopyLocationMenuItem").hidden`, `this.contextMenu.querySelector(".downloadLinksSeparator").hidden`, `this.contextMenu.querySelector(".downloadOpenReferrerMenuItem").hidden`, `this.richListBox.selectedItem`

## _onDownloadDragStart()
- 位置: L1118-1140
- 役割: ファイルが存在すれば、ドラッグのデータにファイルと URI を載せる。
- 触るとき: ダウンロード項目をほかのアプリへドラッグする挙動を変えるとき。
- 呼び出し先: `DownloadsView.itemForElement()`, `NetUtil.newURI()`, `aEvent.stopPropagation()`, `aEvent.target.closest()`, `dataTransfer.addElement()`, `dataTransfer.mozSetDataAt()`, `dataTransfer.setData()`, `file.exists()`
- 参照: `DownloadsView.itemForElement(element).download.target.path`, `FileUtils.File`, `NetUtil.newURI(file).spec`, `aEvent.dataTransfer`, `dataTransfer.effectAllowed`

## DownloadsViewItem.constructor()
- 位置: L1159-1170
- 役割: 項目に download と要素を結び付け、要素に状態のクラスと種類の属性を付ける。
- 触るとき: 項目生成時に要素へ付く属性やクラスを変えるとき。
- 呼び出し先: `super()`, `this.element.classList.add()`, `this.element.setAttribute()`
- 参照: `this.download`, `this.element`, `this.element._shell`, `this.isPanel`

## DownloadsViewItem.onChanged()
- 位置: L1172-1180
- 役割: 状態が変わったら _updateState、変わらなければ _updateStateInner で表示を更新する。
- 触るとき: ダウンロードの状態変化に対する表示更新の分岐を変えるとき。
- 呼び出し先: `DownloadsCommon.stateOfDownload()`
- 条件付き依存: `if (this.downloadState !== newState)` → `this._updateState()`
- 条件付き依存: `if (!(this.downloadState !== newState))` → `this._updateStateInner()`
- 参照: `this.download`, `this.downloadState`

## DownloadsViewItem.isCommandEnabled()
- 位置: L1182-1224
- 役割: コマンドごとに有効かを判定する。開く系は成功済みでファイルが存在するとき、表示は本体か部分ファイルが存在するとき、コピーは URL があるとき。
- 触るとき: メニューや項目のコマンドの有効と無効の条件を変えるとき。個別に扱わないコマンドは基底クラスへ回す。
- 呼び出し先: `DownloadsViewUI.DownloadElementShell.prototype.isCommandEnabled.call()`, `file.exists()`, `partFile.exists()`
- 参照: `FileUtils.File`, `this.download.hasBlockedData`, `this.download.source.isDataURICleared`, `this.download.source?.url`, `this.download.succeeded`, `this.download.target.partFilePath`, `this.download.target.path`

## DownloadsViewItem.doCommand()
- 位置: L1226-1233
- 役割: isCommandEnabled が true の時だけ、コマンド名の「:」より後ろを引数にしてメソッドを呼ぶ。
- 触るとき: downloadsCmd_open:window のような修飾付きコマンドの実行先を追うとき。
- 呼び出し先: `this.isCommandEnabled()`
- 条件付き依存: `if (this.isCommandEnabled(aCommand))` → `aCommand.split()`
- 条件付き依存: `if (this.isCommandEnabled(aCommand))` → `this[command]()`

## DownloadsViewItem.downloadsCmd_unblock()
- 位置: L1237-1240
- 役割: パネルを閉じてから、確認付きでブロックを解除する。
- 触るとき: ブロック解除の確認動作を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.confirmUnblock()`

## DownloadsViewItem.downloadsCmd_chooseUnblock()
- 位置: L1242-1245
- 役割: パネルを閉じてから、解除方法を選ぶ確認を出す。
- 触るとき: 解除方法の選択ダイアログへの経路を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.confirmUnblock()`

## DownloadsViewItem.downloadsCmd_unblockAndOpen()
- 位置: L1247-1250
- 役割: パネルを閉じ、ブロックを解除してから開く。失敗は console.error に出す。
- 触るとき: 解除の後に開く流れを変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.unblockAndOpenDownload()`, `this.unblockAndOpenDownload().catch()`
- 参照: `console.error`

## DownloadsViewItem.downloadsCmd_unblockAndSave()
- 位置: L1251-1254
- 役割: パネルを閉じ、ブロックを解除してから保存する。
- 触るとき: 解除後の保存処理を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `this.unblockAndSave()`

## DownloadsViewItem.downloadsCmd_open()
- 位置: L1256-1265
- 役割: 基底の開く処理を呼んだ後、パネルを閉じてクリックが受理されたことを示す。
- 触るとき: 開いた後にパネルを閉じる順序や、二重に開くのを防ぐ仕組みを変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_open()`

## DownloadsViewItem.downloadsCmd_openInSystemViewer()
- 位置: L1267-1273
- 役割: 基底のシステムビューアで開いた後、パネルを閉じる。
- 触るとき: OS の既定アプリで開く操作を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_openInSystemViewer()`

## DownloadsViewItem.downloadsCmd_alwaysOpenInSystemViewer()
- 位置: L1275-1281
- 役割: 基底の、常にシステムビューアで開く設定を実行し、パネルを閉じる。
- 触るとき: 種類ごとの既定の開き方の設定を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_alwaysOpenInSystemViewer()`

## DownloadsViewItem.downloadsCmd_alwaysOpenSimilarFiles()
- 位置: L1283-1289
- 役割: 基底の、同種のファイルを常に開く設定を実行し、パネルを閉じる。
- 触るとき: 同種ファイルの自動起動の設定を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `super.downloadsCmd_alwaysOpenSimilarFiles()`

## DownloadsViewItem.downloadsCmd_show()
- 位置: L1291-1301
- 役割: ファイルの場所を OS のファイルマネージャーで表示し、パネルを閉じる。
- 触るとき: フォルダーに表示する操作を変えるとき。
- 呼び出し先: `DownloadsCommon.showDownloadedFile()`, `DownloadsPanel.hidePanel()`
- 参照: `FileUtils.File`, `this.download.target.path`

## DownloadsViewItem.downloadsCmd_deleteFile()
- 位置: async L1303-1317
- 役割: 基底でファイルを削除した後、同じ対象の別項目も含めて表示中の全項目を refresh する。
- 触るとき: 削除後に同じファイルの重複項目の表示が古いままにならないかを確かめるとき。
- 呼び出し先: `DownloadsView._visibleViewItems.values()`, `super.downloadsCmd_deleteFile()`, `viewItem.download.refresh()`, `viewItem.download.refresh().catch()`
- 参照: `console.error`

## DownloadsViewItem.downloadsCmd_showBlockedInfo()
- 位置: L1319-1324
- 役割: ブロックされた項目の詳細サブビューを開く。
- 触るとき: ブロック時の説明画面の表示内容を変えるとき。
- 呼び出し先: `DownloadsBlockedSubview.toggle()`
- 参照: `this.element`, `this.rawBlockedTitleAndDetails`

## DownloadsViewItem.downloadsCmd_openReferrer()
- 位置: L1326-1328
- 役割: 参照元ページの URL を開く。
- 触るとき: 参照元を開くメニューの動作を変えるとき。
- 呼び出し先: `openURL()`
- 参照: `this.download.source.referrerInfo.originalReferrer`

## DownloadsViewItem.downloadsCmd_copyLocation()
- 位置: L1330-1332
- 役割: ダウンロード元の URL をクリップボードへコピーする。
- 触るとき: URL のコピー内容(data URI の扱いなど)を変えるとき。
- 呼び出し先: `DownloadsCommon.copyDownloadLink()`
- 参照: `this.download`

## DownloadsViewItem.downloadsCmd_doDefault()
- 位置: L1334-1339
- 役割: その項目の既定コマンドが有効なら実行する。
- 触るとき: Enter などの既定操作で何が起きるかを変えるとき。
- 呼び出し先: `this.isCommandEnabled()`
- 条件付き依存: `if (defaultCommand && this.isCommandEnabled(defaultCommand))` → `this.doCommand()`
- 参照: `this.currentDefaultCommandName`

## initialize()
- 位置: L1352-1354
- 役割: ウィンドウのコントローラ群の先頭に自身を挿入し、コマンドを受け取れるようにする。
- 触るとき: コマンドの受け口の順序を変えるとき。
- 呼び出し先: `window.controllers.insertControllerAt()`

## terminate()
- 位置: L1356-1358
- 役割: ウィンドウのコントローラ群から自身を外す。
- 触るとき: ウィンドウ終了時の解除を確かめるとき。
- 呼び出し先: `window.controllers.removeController()`

## supportsCommand()
- 位置: L1362-1399
- 役割: このコントローラがコマンドを処理するかを判定する。サブビュー表示中は限られたコマンドだけ、通常時は一覧にフォーカスがある時だけ true を返す。
- 触るとき: どのコマンドを一覧側が受け持つかを変えるとき。
- 呼び出し先: `DownloadsViewUI.isCommandName()`, `aCommand.split()`
- 条件付き依存: `if (DownloadsView.subViewOpen)` → `blockedSubviewCmds.includes()`
- 参照: `DownloadsView.richListBox`, `DownloadsView.subViewOpen`, `DownloadsViewItem.prototype`, `document.commandDispatcher.focusedElement`, `element.parentNode`

## isCommandEnabled()
- 位置: L1401-1419
- 役割: 全体のコマンドは件数や非公開設定で判定し、それ以外は選択中の項目へ問い合わせる。
- 触るとき: コマンドの有効と無効の表示が決まる経路を変えるとき。
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsView.itemForElement()`, `DownloadsView.itemForElement(element).isCommandEnabled()`
- 参照: `DownloadsCommon.getData(window).canRemoveFinished`, `DownloadsView.richListBox.selectedItem`

## doCommand()
- 位置: L1421-1434
- 役割: 全体のコマンドは自身のメソッドを呼び、それ以外は選択中の項目へ渡して実行する。
- 触るとき: コマンドの振り分け先を変えるとき。
- 条件付き依存: `if (aCommand in this)` → `this[aCommand]()`
- 条件付き依存: `if (element)` → `DownloadsView.itemForElement(element).doCommand()`
- 条件付き依存: `if (element)` → `DownloadsView.itemForElement()`
- 参照: `DownloadsView.richListBox.selectedItem`

## onEvent()
- 位置: L1436-1436
- 役割: 何もしない空の実装。
- 触るとき: このコントローラにイベント処理を足すときは、購読の追加もあわせて必要になる。

## updateCommands()
- 位置: L1440-1450
- 役割: このオブジェクトと項目のプロトタイプから、命名規則に合うコマンド名を集めて有効状態を更新する。
- 触るとき: 新しいコマンドを足したのに表示が古いままのとき。
- 呼び出し先: `updateCommandsForObject()`
- 参照: `DownloadsViewItem.prototype`

## updateCommandsForObject()
- 位置: L1441-1447
- 役割: 渡されたオブジェクトの各プロパティのうち、コマンド名の規則に合うものを goUpdateCommand で更新する。
- 触るとき: コマンドの更新対象に含まれる名前の規則を変えるとき。updateCommands の内側で使われる。
- 呼び出し先: `DownloadsViewUI.isCommandName()`
- 条件付き依存: `if (DownloadsViewUI.isCommandName(name))` → `goUpdateCommand()`

## downloadsCmd_clearList()
- 位置: L1454-1456
- 役割: 取得済み(終了済み)のダウンロードを一覧から削除する。
- 触るとき: 一覧のクリア操作の対象を変えるとき。
- 呼び出し先: `DownloadsCommon.getData()`, `DownloadsCommon.getData(window).removeFinished()`

## downloadsCmd_deletePrivate()
- 位置: L1458-1460
- 役割: 非公開ダウンロードを終了時に削除する選択をする。
- 触るとき: 非公開ブラウズの削除選択の仕組みを追うとき。
- 呼び出し先: `PrivateDownloadsSubview.choose()`

## downloadsCmd_dismissDeletePrivate()
- 位置: L1462-1464
- 役割: 非公開ダウンロードの同じ選択画面で、削除しない方を選ぶ。
- 触るとき: 非公開の削除確認を閉じる動作を変えるとき。
- 呼び出し先: `PrivateDownloadsSubview.choose()`

## active()
- 位置: L1487-1501
- 役割: アクティブ状態を切り替える。有効化時は集計データに表示の更新を依頼し、無効化時はフッターのサマリー表示を消す。
- 触るとき: 件数が上限を超えたときにサマリーを出すきっかけを変えるとき。
- 条件付き依存: `if (aActive)` → `DownloadsCommon.getSummary( window, DownloadsView.kItemCountLimit ).refreshView()`
- 条件付き依存: `if (aActive)` → `DownloadsCommon.getSummary()`
- 参照: `DownloadsFooter.showingSummary`, `DownloadsView.kItemCountLimit`, `this._active`, `this._summaryNode`

## active()
- 位置: L1506-1508
- 役割: サマリーの現在のアクティブ状態を返す。
- 触るとき: サマリーが有効かを他の処理から判定するとき。
- 参照: `this._active`

## showingProgress()
- 位置: L1518-1526
- 役割: 進捗バーの表示属性を付け外しし、表示する時だけフッターにサマリーを出す。
- 触るとき: 進捗表示と集計サマリーの出し分けを変えるとき。
- 条件付き依存: `if (aShowingProgress)` → `this._summaryNode.setAttribute()`
- 条件付き依存: `if (!(aShowingProgress))` → `this._summaryNode.removeAttribute()`
- 参照: `DownloadsFooter.showingSummary`

## percentComplete()
- 位置: L1535-1539
- 役割: 進捗バーの value 属性に進捗率を設定する。
- 触るとき: 進捗率の計算結果をバーに反映する経路を調べるとき。
- 条件付き依存: `if (this._progressNode)` → `this._progressNode.setAttribute()`
- 参照: `this._progressNode`

## description()
- 位置: L1548-1553
- 役割: サマリーの主説明文を value と tooltiptext に設定する。
- 触るとき: 件数や状態を説明する文言の表示を変えるとき。
- 条件付き依存: `if (this._descriptionNode)` → `this._descriptionNode.setAttribute()`
- 参照: `this._descriptionNode`

## details()
- 位置: L1563-1568
- 役割: サマリーの補足情報(残り時間や転送量など)を value と tooltiptext に設定する。
- 触るとき: 補足情報の表示内容を変えるとき。
- 条件付き依存: `if (this._detailsNode)` → `this._detailsNode.setAttribute()`
- 参照: `this._detailsNode`

## focus()
- 位置: L1573-1577
- 役割: サマリー要素があればフォーカスを移す。
- 触るとき: フッターからのフォーカス移動先を変えるとき。
- 条件付き依存: `if (this._summaryNode)` → `this._summaryNode.focus()`
- 参照: `this._summaryNode`

## _onKeyDown()
- 位置: L1585-1592
- 役割: サマリーでスペースか Enter が押されたら、ダウンロード履歴を開く。
- 触るとき: サマリーのキー操作を変えるとき。
- 呼び出し先: `" ".charCodeAt()`
- 条件付き依存: `if ( aEvent.charCode == " ".charCodeAt(0) || aEvent.keyCode == KeyEvent.DOM_VK_RETURN )` → `DownloadsPanel.showDownloadsHistory()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.charCode`, `aEvent.keyCode`

## _summaryNode()
- 位置: L1597-1604
- 役割: downloadsSummary 要素を取得し、見つかれば値を固定する。
- 触るとき: サマリー要素の ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._summaryNode`

## _progressNode()
- 位置: L1609-1616
- 役割: 進捗バー downloadsSummaryProgress を遅延取得する。
- 触るとき: 進捗バーの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._progressNode`

## _descriptionNode()
- 位置: L1622-1629
- 役割: 説明文の要素 downloadsSummaryDescription を遅延取得する。
- 触るとき: 説明文の ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._descriptionNode`

## _detailsNode()
- 位置: L1635-1642
- 役割: 補足文の要素 downloadsSummaryDetails を遅延取得する。
- 触るとき: 補足文の ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._detailsNode`

## focus()
- 位置: L1659-1665
- 役割: サマリーを表示中ならサマリーへ、そうでなければ「すべて表示」ボタンへフォーカスを移す。
- 触るとき: パネル下部のフォーカス先を変えるとき。
- 条件付き依存: `if (this._showingSummary)` → `DownloadsSummary.focus()`
- 条件付き依存: `if (!(this._showingSummary))` → `DownloadsView.downloadsHistory.focus()`
- 参照: `this._showingSummary`

## showingSummary()
- 位置: L1673-1682
- 役割: フッター要素の showingsummary 属性を付け外しし、その状態を保持する。
- 触るとき: サマリーと「すべて表示」ボタンの切り替えを変えるとき。
- 条件付き依存: `if (aValue)` → `this._footerNode.setAttribute()`
- 条件付き依存: `if (!(aValue))` → `this._footerNode.removeAttribute()`
- 参照: `this._footerNode`, `this._showingSummary`

## _footerNode()
- 位置: L1687-1694
- 役割: downloadsFooter 要素を遅延取得する。
- 触るとき: フッターの ID を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this._footerNode`

## elements()
- 位置: L1708-1722
- 役割: ブロック表示サブビューの各部品を ID の接尾辞から集め、以後は値を固定する。
- 触るとき: サブビューの部品の ID を変えるとき。
- 呼び出し先: `document.getElementById()`, `idSuffixes.reduce()`
- 参照: `this.elements`

## toggle()
- 位置: L1740-1791
- 役割: ブロック項目のサブビューに題、詳細、ボタンを設定して表示する。解除ボタンは安全性の設定で隠れ、ラベルは完了後に開く設定で切り替わる。
- 触るとき: ブロック時の説明や解除、削除ボタンの出し分けを変えるとき。
- 呼び出し先: `DownloadsPanel.panel.addEventListener()`, `DownloadsView.itemForElement()`, `DownloadsViewController.updateCommands()`, `Services.prefs.getBoolPref()`, `document.l10n.setAttributes()`, `element.getAttribute()`, `this.mainView.addEventListener()`, `this.panelMultiView.showSubView()`, `this.subview.setAttribute()`, `window.getComputedStyle()`
- 参照: `DownloadsCommon.strings`, `DownloadsView.subViewOpen`, `details[0].l10n`, `details[0].l10n.args`, `details[0].l10n.id`, `download.error?.becauseBlockedByContentAnalysis`, `download.error?.reputationCheckVerdict`, `download.launchWhenSucceeded`, `e.deleteButton.hidden`, `e.deleteButton.label`, `e.details1`, `e.details1.textContent`, `e.details2.textContent`, `e.title`, `e.title.textContent`, `e.unblockButton.command`, `e.unblockButton.hidden`, `e.unblockButton.label`, `s.unblockButtonConfirmBlock`, `s.unblockButtonOpen`, `s.unblockButtonUnblock`, `this.elements`, `this.mainView.style.minWidth`, `this.subview`, `title.l10n`, `title.l10n.args`, `title.l10n.id`, `window.getComputedStyle(this.subview).width`
- XPCOM: `Services.prefs`

## handleEvent()
- 位置: L1793-1802
- 役割: メイン画面の表示またはパネルを閉じたときに、サブビューの状態を戻す。メイン画面に戻った時はパネルを開き直す。
- 触るとき: サブビューから戻るときのフォーカスや状態の戻し方を変えるとき。
- 呼び出し先: `DownloadsPanel.panel.removeEventListener()`, `this.mainView.removeEventListener()`
- 条件付き依存: `if (event.type == "ViewShown")` → `DownloadsPanel.showPanel()`
- 参照: `DownloadsView.subViewOpen`, `event.type`

## confirmBlock()
- 位置: L1807-1810
- 役割: 削除コマンドを実行してからパネルを閉じる。
- 触るとき: ブロック項目の削除確定の動作を変えるとき。
- 呼び出し先: `DownloadsPanel.hidePanel()`, `goDoCommand()`

## openWhenReady()
- 位置: L1839-1845
- 役割: 非公開ダウンロードのサブビューを表示中に設定し、メイン画面の表示を待ってから選択画面を見せる。
- 触るとき: 非公開ダウンロードの選択画面をいつ出すかを変えるとき。
- 呼び出し先: `DownloadsViewController.updateCommands()`, `this.mainView.addEventListener()`, `this.mainView.toggleAttribute()`
- 参照: `DownloadsView.subViewOpen`

## handleEvent()
- 位置: L1847-1854
- 役割: メイン画面が表示されたら、非公開の選択サブビューへ切り替える。
- 触るとき: 非公開の選択画面への遷移経路を変えるとき。
- 条件付き依存: `if (event.type == "ViewShown")` → `this.panelMultiView.showSubView()`
- 参照: `event.type`, `this.subview`

## choose()
- 位置: L1863-1871
- 役割: 選択結果を browser.download.deletePrivate と deletePrivate.chosen の pref に保存し、サブビューを閉じてメイン画面へ戻る。
- 触るとき: 非公開ダウンロードの削除設定の保存先や戻り方を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.mainView.toggleAttribute()`, `this.panelMultiView.goBack()`
- 条件付き依存: `if (deletePrivate)` → `Services.prefs.setBoolPref()`
- 参照: `DownloadsView.subViewOpen`
- XPCOM: `Services.prefs`
