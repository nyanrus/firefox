# browser/components/tabbrowser/content/browser-ctrlTab.js

source: browser/components/tabbrowser/content/browser-ctrlTab.js
source-hash: 3878a29a91aef0911f0260082847ed416ddf16d4
lines: 859

## <module>
- 役割: Ctrl+Tab のサムネイル取得(tabPreviews)とプレビューパネル(ctrlTab)を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Math.max()`, `Math.min()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## aspectRatio()
- 位置: L9-16
- 役割: サムネイルサイズから縦横比を計算し、初回のみ値として固定する。
- 触るとき: プレビューの縦横比がおかしいとき。
- 呼び出し先: `ChromeUtils.importESModule()`, `PageThumbUtils.getThumbnailSize()`
- 参照: `this.aspectRatio`

## tabPreviews_loadImage()
- 位置: async L27-49
- 役割: ページ URL の保存済みサムネイル画像を最大1秒待って読み込み、失敗時は null を返す。
- 触るとき: サムネイル画像の読み込み待ちや失敗時の扱いを調べるとき。
- 呼び出し先: `PageThumbs.getThumbnailURL()`, `finish()`, `img.addEventListener()`, `setTimeout()`
- 参照: `controller.signal`, `img.complete`, `img.naturalWidth`, `img.src`

## finish()
- 位置: L36-40
- 役割: タイマーとリスナーを片付けて値で解決する。
- 触るとき: loadImage の待機終了処理を調べるとき。
- 呼び出し先: `clearTimeout()`, `controller.abort()`, `resolve()`

## tabPreviews_get()
- 位置: async L70-93
- 役割: タブのキャッシュ済みサムネイルを返し、無ければ保存画像の読み込みか新規キャプチャを行う。
- 触るとき: プレビュー画像の取得経路やキャッシュ無効化を調べるとき。
- 呼び出し先: `aTab.hasAttribute()`, `this.capture()`
- 条件付き依存: `if (!browser.browsingContext)` → `this.loadImage()`
- 参照: `aTab.__thumbnail`, `aTab.__thumbnail_lastURI`, `aTab.linkedBrowser`, `browser.browsingContext`, `browser.currentURI.spec`

## tabPreviews_capture()
- 位置: async L110-144
- 役割: タブのサムネイルを canvas に取得し、条件が合えば保存・キャッシュする。
- 触るとき: サムネイルの撮影・保存処理を調べるとき。
- 呼び出し先: `PageThumbs.captureToCanvas()`, `PageThumbs.createCanvas()`, `PageThumbs.shouldStoreThumbnail()`, `console.error()`
- 条件付き依存: `if (doStore && aShouldCache)` → `PageThumbs.captureAndStore()`
- 条件付き依存: `if (doStore && aShouldCache)` → `this.loadImage()`
- 条件付き依存: `if (img)` → `canvas.getContext("2d").drawImage()`
- 条件付き依存: `if (img)` → `canvas.getContext()`
- 参照: `aTab.__thumbnail`, `aTab.__thumbnail_lastURI`, `aTab.linkedBrowser`, `browser.currentURI.spec`

## opening()
- 位置: L148-156
- 役割: プレビューパネルを表示可能にし、表示・非表示用ハンドラを登録して直前のフォーカスを記録する。
- 触るとき: パネル表示開始時の共通処理を調べるとき。
- 呼び出し先: `host.panel.addEventListener()`, `this._generateHandler()`
- 参照: `document.commandDispatcher.focusedElement`, `host._prevFocus`, `host.panel.hidden`

## _generateHandler()
- 位置: L157-165
- 役割: パネル自身のポップアップイベントを一度だけ対応する処理へ振り分けるリスナーを作る。
- 触るとき: パネルのイベント処理の仕組みを調べるとき。

## listener()
- 位置: L159-164
- 役割: パネルのイベントなら自身を外して _popupshown か _popuphiding を呼ぶ。
- 触るとき: ポップアップイベントの振り分けを調べるとき。
- 条件付き依存: `if (event.target == host.panel)` → `host.panel.removeEventListener()`
- 条件付き依存: `if (event.target == host.panel)` → `self["_" + event.type]()`
- 参照: `event.target`, `event.type`, `host.panel`

## _popupshown()
- 位置: L166-170
- 役割: ホストに setupGUI があれば呼ぶ。
- 触るとき: パネル表示直後の初期化を調べるとき。
- 条件付き依存: `if ("setupGUI" in host)` → `host.setupGUI()`

## _popuphiding()
- 位置: L171-195
- 役割: パネルを閉じる際に GUI を片付け、フォーカスを戻し、選択予定のタブがあれば選択する。
- 触るとき: パネルを閉じた後のフォーカスやタブ選択を調べるとき。
- 条件付き依存: `if ("suspendGUI" in host)` → `host.suspendGUI()`
- 条件付き依存: `if (host._prevFocus)` → `Services.focus.setFocus()`
- 条件付き依存: `if (!(host._prevFocus))` → `gBrowser.selectedBrowser.focus()`
- 条件付き依存: `if (host.tabToSelect)` → `gBrowser.setSelectedTab()`
- 条件付き依存: `if (host.tabToSelect)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 参照: `Ci.nsIFocusManager.FLAG_NOSCROLL`, `gBrowser.TabMetrics.METRIC_SOURCE.CTRL_TAB`, `host._prevFocus`, `host.tabToSelect`
- XPCOM: [`nsIFocusManager`](../../../../dom/interfaces/base/nsIFocusManager.idl.md) / `Services.focus`

## panel()
- 位置: L203-206
- 役割: ctrlTab-panel 要素を取得して初回のみ保持する。
- 触るとき: パネル要素の参照元を調べるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.panel`

## previewsContainer()
- 位置: L207-211
- 役割: ctrlTab-previews 要素を取得して初回のみ保持する。
- 触るとき: プレビュー配置先の参照元を調べるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `this.previewsContainer`

## showAllButton()
- 位置: L212-223
- 役割: 「すべてのタブ」ボタンを作って各リスナーを付けコンテナに追加し、初回のみ保持する。
- 触るとき: すべて表示ボタンの生成を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("ctrlTab-showAll-container") .appendChild()`, `document.createXULElement()`, `this.showAllButton.addEventListener()`
- 参照: `this.showAllButton`, `this.showAllButton.id`

## previews()
- 位置: L224-228
- 役割: プレビュー要素の配列を初回に構築して返す。
- 触るとき: プレビュー要素の生成タイミングを調べるとき。
- 呼び出し先: `this._buildPreviews()`
- 参照: `this.previews`

## keys()
- 位置: L229-240
- 役割: 閉じる・検索・全選択のショートカット文字コードを取得して保持する。
- 触るとき: パネル内ショートカットキーの判定を調べるとき。
- 呼び出し先: `["close", "find", "selectAll"].forEach()`, `document .getElementById()`, `document .getElementById("key_" + key) .getAttribute()`, `document .getElementById("key_" + key) .getAttribute("key") .toLocaleLowerCase()`, `document .getElementById("key_" + key) .getAttribute("key") .toLocaleLowerCase() .charCodeAt()`
- 参照: `this.keys`

## selected()
- 位置: L242-246
- 役割: 現在選択中のプレビュー、フォーカスがパネル内ならフォーカス中の要素を返す。
- 触るとき: 選択中のプレビューの判定を調べるとき。
- 参照: `document.activeElement`, `this._selectedIndex`, `this.previews`

## isOpen()
- 位置: L247-251
- 役割: パネルが開いている、開く途中、または遅延タイマー待ちかを返す。
- 触るとき: 開閉状態の判定を調べるとき。
- 参照: `this._timer`, `this.panel.state`

## tabCount()
- 位置: L252-254
- 役割: 最近使ったタブ一覧の件数を返す。
- 触るとき: 対象タブ数の算出を調べるとき。
- 参照: `this.tabList.length`

## tabPreviewCount()
- 位置: L255-257
- 役割: プレビューの最大数とタブ数の小さい方を返す。
- 触るとき: 表示するプレビュー数を調べるとき。
- 呼び出し先: `Math.min()`
- 参照: `this.maxTabPreviews`, `this.tabCount`

## previewColumnCount()
- 位置: L262-264
- 役割: プレビューの列数(1行の最大数)を返す。
- 触るとき: プレビューの列数やパネル幅を調べるとき。
- 呼び出し先: `Math.min()`
- 参照: `this.previewsPerRow`, `this.tabPreviewCount`

## tabList()
- 位置: L266-268
- 役割: 最近使った順のタブ配列を返す。
- 触るとき: MRU 順タブ一覧の参照元を調べるとき。
- 参照: `this._recentlyUsedTabs`

## ctrlTab_init()
- 位置: L270-275
- 役割: 未初期化なら最近使ったタブ一覧を作り、イベント登録を有効にする。
- 触るとき: Ctrl+Tab 機能の有効化を調べるとき。
- 条件付き依存: `if (!this._recentlyUsedTabs)` → `this._initRecentlyUsedTabs()`
- 条件付き依存: `if (!this._recentlyUsedTabs)` → `this._init()`
- 参照: `this._recentlyUsedTabs`

## ctrlTab_uninit()
- 位置: L277-282
- 役割: タブ一覧を破棄してイベント登録を解除する。
- 触るとき: Ctrl+Tab 機能の無効化を調べるとき。
- 条件付き依存: `if (this._recentlyUsedTabs)` → `this._init()`
- 参照: `this._recentlyUsedTabs`

## ctrlTab_observePref()
- 位置: L286-289
- 役割: 設定項目の監視を始めて現在値を読む。
- 触るとき: pref の監視開始を調べるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `this.readPref()`
- 参照: `this.prefName`
- XPCOM: `Services.prefs`

## ctrlTab_stopObservingPref()
- 位置: L291-294
- 役割: 設定項目の監視を止めて無効化する。
- 触るとき: pref の監視停止を調べるとき。
- 呼び出し先: `Services.prefs.removeObserver()`, `this.uninit()`
- 参照: `this.prefName`
- XPCOM: `Services.prefs`

## ctrlTab_readPref()
- 位置: L296-309
- 役割: MRU 並び替え pref とスクリーンリーダー向け除外 pref を見て有効・無効を切り替える。
- 触るとき: pref による有効条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (enable)` → `this.init()`
- 条件付き依存: `if (!(enable))` → `this.uninit()`
- 参照: `this.prefName`
- XPCOM: `Services.prefs`

## observe()
- 位置: L310-312
- 役割: pref 変更通知を受けて設定を読み直す。
- 触るとき: pref 変更への追従を調べるとき。
- 呼び出し先: `this.readPref()`

## _buildPreviews()
- 位置: L314-323
- 役割: 最大数のプレビュー要素と末尾のすべて表示ボタンを作り直す。
- 触るとき: プレビュー要素群の構築を調べるとき。
- 呼び出し先: `this._makePreview()`, `this.previews.push()`, `this.previewsContainer.appendChild()`, `this.previewsContainer.replaceChildren()`
- 参照: `this.maxTabPreviews`, `this.previews`, `this.showAllButton`

## _makePreview()
- 位置: L325-355
- 役割: canvas・favicon・ラベルを持つプレビューボタン一つを作る。
- 触るとき: プレビュー一つの DOM 構造を変えるとき。
- 呼び出し先: `document.createXULElement()`, `faviconContainer.appendChild()`, `label.setAttribute()`, `preview.addEventListener()`, `preview.appendChild()`, `preview.setAttribute()`, `previewInner.appendChild()`
- 参照: `canvas.className`, `favicon.className`, `faviconContainer.className`, `label.className`, `preview._canvas`, `preview._favicon`, `preview._label`, `preview.className`, `previewInner.className`

## ctrlTab_updatePreviews()
- 位置: L357-373
- 役割: 列数を設定し、全プレビューを更新して、すべて表示ボタンの文言と表示可否を設定する。
- 触るとき: プレビュー一覧全体の更新を調べるとき。
- 呼び出し先: `document.l10n.setAttributes()`, `this.previewsContainer.style.setProperty()`, `this.updatePreview()`
- 参照: `gTabsPanel.canOpen`, `this.previewColumnCount`, `this.previews`, `this.previews.length`, `this.showAllButton`, `this.showAllButton.hidden`, `this.tabCount`, `this.tabList`

## ctrlTab_updatePreview()
- 位置: L375-419
- 役割: プレビュー一つにタブのサムネイル・ラベル・favicon を反映し、タブが無ければ空にして隠す。
- 触るとき: 個々のプレビューの表示内容を調べるとき。
- 呼び出し先: `aPreview._canvas.replaceChildren()`, `aPreview._label.setAttribute()`, `aPreview.setAttribute()`, `console.error()`, `tabPreviews .get()`, `tabPreviews .get(aTab) .then()`
- 条件付き依存: `if (!aTab)` → `aPreview._canvas.replaceChildren()`
- 条件付き依存: `if (!aTab)` → `aPreview._label.removeAttribute()`
- 条件付き依存: `if (!aTab)` → `aPreview.removeAttribute()`
- 条件付き依存: `if (!aTab)` → `aPreview._favicon.removeAttribute()`
- 条件付き依存: `if (tabChanged)` → `aPreview._canvas.replaceChildren()`
- 条件付き依存: `if (tabChanged)` → `this._makePlaceholder()`
- 条件付き依存: `if (aTab.image)` → `aPreview._favicon.setAttribute()`
- 条件付き依存: `if (!(aTab.image))` → `aPreview._favicon.removeAttribute()`
- 参照: `aPreview._tab`, `aPreview.hidden`, `aTab.image`, `aTab.label`, `img.style.height`, `img.style.width`, `this.canvasHeight`, `this.canvasWidth`, `this.showAllButton`

## _makePlaceholder()
- 位置: L421-428
- 役割: サムネイル枠の大きさを保つ透明な画像要素を作る。
- 触るとき: サムネイル未取得時の枠のずれを調べるとき。
- 呼び出し先: `document.createElement()`, `placeholder.setAttribute()`
- 参照: `placeholder.className`, `this.canvasHeight`, `this.canvasWidth`

## ctrlTab_advanceFocus()
- 位置: L430-457
- 役割: 非表示を飛ばして次/前のプレビューへ選択を進め、タブを温め、待機中なら即パネルを開く。
- 触るとき: Tab キー送りの選択移動を調べるとき。
- 呼び出し先: `this.previews.indexOf()`
- 条件付き依存: `if (this._selectedIndex == -1)` → `this.previews[selectedIndex].focus()`
- 条件付き依存: `if (this.previews[selectedIndex]._tab)` → `gBrowser.warmupTab()`
- 条件付き依存: `if (this._timer)` → `clearTimeout()`
- 条件付き依存: `if (this._timer)` → `this._openPanel()`
- 参照: `this._selectedIndex`, `this._timer`, `this.previews`, `this.previews.length`, `this.previews[selectedIndex]._tab`, `this.previews[selectedIndex].hidden`, `this.selected`

## ctrlTab_pick()
- 位置: L459-471
- 役割: 選択したプレビューを確定し、すべて表示なら一覧を開き、タブならそのタブを選んで閉じる。
- 触るとき: プレビュー確定時の動作を調べるとき。
- 条件付き依存: `if (select == this.showAllButton)` → `this.showAllTabs()`
- 条件付き依存: `if (!(select == this.showAllButton))` → `this.close()`
- 参照: `select._tab`, `this.selected`, `this.showAllButton`, `this.tabCount`

## ctrlTab_showAllTabs()
- 位置: L473-476
- 役割: Ctrl+Tab パネルを閉じて、すべてのタブパネルを開く。
- 触るとき: すべてのタブ表示への遷移を調べるとき。
- 呼び出し先: `gTabsPanel.showAllTabsPanel()`, `this.close()`

## ctrlTab_remove()
- 位置: L478-482
- 役割: プレビューに対応するタブを閉じる。
- 触るとき: パネルからのタブ閉じを調べるとき。
- 条件付き依存: `if (aPreview._tab)` → `gBrowser.removeTab()`
- 参照: `aPreview._tab`

## ctrlTab_attachTab()
- 位置: L484-502
- 役割: 閉じ中や非選択の非表示タブを除き、タブを最近使った順一覧の指定位置に入れる。
- 触るとき: MRU 一覧への追加規則を調べるとき。
- 呼び出し先: `this.detachTab()`
- 条件付き依存: `if (aPos == 0)` → `this._recentlyUsedTabs.unshift()`
- 条件付き依存: `if (aPos)` → `this._recentlyUsedTabs.splice()`
- 条件付き依存: `if (!(aPos))` → `this._recentlyUsedTabs.push()`
- 参照: `aTab.closing`, `aTab.hidden`, `aTab.selected`

## ctrlTab_detachTab()
- 位置: L504-509
- 役割: タブを最近使った順一覧から取り除く。
- 触るとき: MRU 一覧からの削除を調べるとき。
- 呼び出し先: `this._recentlyUsedTabs.indexOf()`
- 条件付き依存: `if (i >= 0)` → `this._recentlyUsedTabs.splice()`

## ctrlTab_open()
- 位置: L511-533
- 役割: プレビューを準備して初期選択を設定し、200ms 後にパネルを開く予約をする。
- 触るとき: Ctrl+Tab 押下から表示までの流れを調べるとき。
- 呼び出し先: `Math.ceil()`, `Math.round()`, `gBrowser.warmupTab()`, `setTimeout()`, `this._openPanel()`, `this.updatePreviews()`
- 条件付き依存: `if (this.previews.length != this.maxTabPreviews + 1)` → `this._buildPreviews()`
- 参照: `screen.availWidth`, `tabPreviews.aspectRatio`, `this._selectedIndex`, `this._timer`, `this.canvasHeight`, `this.canvasWidth`, `this.isOpen`, `this.maxTabPreviews`, `this.previews.length`, `this.previewsPerRow`, `this.selected._tab`

## ctrlTab_openPanel()
- 位置: L535-550
- 役割: パネル幅と位置を計算して画面中央付近にポップアップを開く。
- 触るとき: パネルの大きさや表示位置を変えるとき。
- 呼び出し先: `Math.ceil()`, `Math.min()`, `tabPreviewPanelHelper.opening()`, `this.panel.openPopupAtScreen()`
- 参照: `screen.availHeight`, `screen.availLeft`, `screen.availTop`, `screen.availWidth`, `this.canvasHeight`, `this.canvasWidth`, `this.panel.style.width`, `this.previewColumnCount`, `this.previewsPerRow`, `this.tabPreviewCount`

## ctrlTab_close()
- 位置: L552-574
- 役割: 待機中ならタイマーを止めて直接タブを選び、表示中ならパネルを閉じて選択予定のタブを設定する。
- 触るとき: パネルを閉じるときのタブ選択を調べるとき。
- 呼び出し先: `this.panel.hidePopup()`
- 条件付き依存: `if (this._timer)` → `clearTimeout()`
- 条件付き依存: `if (this._timer)` → `this.suspendGUI()`
- 条件付き依存: `if (aTabToSelect)` → `gBrowser.setSelectedTab()`
- 条件付き依存: `if (aTabToSelect)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 参照: `gBrowser.TabMetrics.METRIC_SOURCE.CTRL_TAB`, `this._timer`, `this.isOpen`, `this.tabToSelect`

## ctrlTab_setupGUI()
- 位置: L576-579
- 役割: 選択中のプレビューにフォーカスを移し、内部の選択位置を解除する。
- 触るとき: 表示直後のフォーカス設定を調べるとき。
- 呼び出し先: `this.selected.focus()`
- 参照: `this._selectedIndex`

## ctrlTab_suspendGUI()
- 位置: L581-585
- 役割: 全プレビューを空にして片付ける。
- 触るとき: パネルを閉じた後のプレビューの後始末を調べるとき。
- 呼び出し先: `this.updatePreview()`
- 参照: `this.previews`

## onKeyDown()
- 位置: L587-628
- 役割: タブ循環のキーを受け、パネル表示中はフォーカスを進め、そうでなければ開くか2枚なら直接切り替える。
- 触るとき: Ctrl+Tab のキー押下処理を調べるとき。
- 呼び出し先: `ShortcutUtils.getSystemActionForEvent()`, `document.addEventListener()`, `event.preventDefault()`, `event.stopPropagation()`, `this.KeyboardLockUtils.mustWaitForKeyboardLockRequestedReply()`
- 条件付き依存: `if (this.isOpen)` → `this.advanceFocus()`
- 条件付き依存: `if (event.shiftKey)` → `this.showAllTabs()`
- 条件付き依存: `if (tabs.length > 2)` → `this.open()`
- 条件付き依存: `if (tabs.length == 2)` → `gBrowser.setSelectedTab()`
- 条件付き依存: `if (tabs.length == 2)` → `gBrowser.TabMetrics.userTriggeredContext()`
- 参照: `ShortcutUtils.CYCLE_TABS`, `event.defaultPrevented`, `event.shiftKey`, `gBrowser.TabMetrics.METRIC_SOURCE.CTRL_TAB`, `gBrowser.visibleTabs`, `tabs.length`, `tabs[0].selected`, `this.isOpen`

## onKeyPress()
- 位置: L630-654
- 役割: パネル表示中の Ctrl 付きキーで、閉じる・検索・全選択・Delete に対応する操作を行う。
- 触るとき: パネル内のショートカット動作を変えるとき。
- 呼び出し先: `event.preventDefault()`, `event.stopPropagation()`, `this.remove()`, `this.showAllTabs()`
- 条件付き依存: `if (event.keyCode == event.DOM_VK_DELETE)` → `this.remove()`
- 参照: `event.DOM_VK_DELETE`, `event.charCode`, `event.ctrlKey`, `event.keyCode`, `this.isOpen`, `this.keys.close`, `this.keys.find`, `this.keys.selectAll`, `this.selected`

## ctrlTab_removeClosingTabFromUI()
- 位置: L656-681
- 役割: 閉じられるタブをパネルから外し、残りが少なければ閉じ、選択やフォーカスを調整する。
- 触るとき: パネル表示中にタブが閉じられた時の挙動を調べるとき。
- 呼び出し先: `this.updatePreviews()`
- 条件付き依存: `if (this.tabCount == 2)` → `this.close()`
- 条件付き依存: `if (this.selected.hidden)` → `this.advanceFocus()`
- 条件付き依存: `if (this.selected == this.showAllButton)` → `this.advanceFocus()`
- 条件付き依存: `if (aTab.selected && this.panel.state == "open")` → `setTimeout()`
- 条件付き依存: `if (aTab.selected && this.panel.state == "open")` → `selected.focus()`
- 参照: `aTab.selected`, `this.panel.state`, `this.selected`, `this.selected.hidden`, `this.showAllButton`, `this.tabCount`

## ctrlTab_handleEvent()
- 位置: L683-778
- 役割: タブの開閉・選択・属性変更・表示切替とキー・マウス・コマンドの各イベントを処理する。
- 触るとき: Ctrl+Tab 周りのイベント処理全般を調べるとき。
- 呼び出し先: `["label", "busy", "image"].includes()`, `event.detail.changed.some()`, `event.preventDefault()`, `event.stopPropagation()`, `this._initRecentlyUsedTabs()`, `this._sortRecentlyUsedTabs()`, `this.attachTab()`, `this.detachTab()`, `this.onKeyDown()`, `this.onKeyPress()`, `this.pick()`
- 条件付き依存: `if ( this.previews[i]._tab && this.previews[i]._tab == event.target )` → `this.updatePreview()`
- 条件付き依存: `if (previousTab.hidden)` → `this.detachTab()`
- 条件付き依存: `if (this.isOpen)` → `this.removeClosingTabFromUI()`
- 条件付き依存: `if (event.keyCode === event.DOM_VK_CONTROL)` → `document.removeEventListener()`
- 条件付き依存: `if (this.isOpen)` → `this.pick()`
- 条件付き依存: `if (event.target.id == "menu_viewPopup")` → `document.getElementById()`
- 条件付き依存: `if (event.relatedTarget)` → `event.currentTarget.focus()`
- 条件付き依存: `if (event.button == 1)` → `this.remove()`
- 条件付き依存: `if (AppConstants.platform == "macosx" && event.button == 2)` → `this.pick()`
- 参照: `AppConstants.platform`, `document.getElementById("menu_showAllTabs").hidden`, `event.DOM_VK_CONTROL`, `event.button`, `event.currentTarget`, `event.detail.previousTab`, `event.keyCode`, `event.relatedTarget`, `event.target`, `event.target.id`, `event.type`, `gTabsPanel.canOpen`, `previousTab.hidden`, `this.isOpen`, `this.previews`, `this.previews.length`, `this.previews[i]._tab`

## filterForThumbnailExpiration()
- 位置: L780-795
- 役割: 表示分より少し多めのタブの URL を、サムネイル期限切れの除外対象として渡す。
- 触るとき: サムネイルが消える/残る条件を調べるとき。
- 呼び出し先: `Math.min()`, `aCallback()`, `urls.push()`
- 参照: `this.tabCount`, `this.tabList`, `this.tabList[i].linkedBrowser.currentURI.spec`, `this.tabPreviewCount`

## _sortRecentlyUsedTabs()
- 位置: L796-800
- 役割: タブ一覧を最終アクセス時刻の新しい順に並べる。
- 触るとき: MRU の並び順を調べるとき。
- 呼び出し先: `this._recentlyUsedTabs.sort()`
- 参照: `tab1.lastAccessed`, `tab2.lastAccessed`

## _initRecentlyUsedTabs()
- 位置: L801-807
- 役割: 閉じ中と非表示を除くタブから最近使った順一覧を作る。
- 触るとき: MRU 一覧の初期構築を調べるとき。
- 呼び出し先: `Array.prototype.filter.call()`, `this._sortRecentlyUsedTabs()`
- 参照: `gBrowser.tabs`, `tab.closing`, `tab.hidden`, `this._recentlyUsedTabs`

## ctrlTab__init()
- 位置: L809-844
- 役割: 機能の有効・無効に合わせ各種イベントリスナー、サムネイル除外フィルター、メニュー項目を登録または解除する。
- 触るとき: 有効化時に登録されるリスナーや副作用を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("menu_viewPopup") [toggleEventListener]()`, `document.getElementById()`, `document[toggleEventListener]()`, `tabContainer[toggleEventListener]()`, `window[toggleEventListener]()`
- 条件付き依存: `if (enable)` → `document.addEventListener()`
- 条件付き依存: `if (!(enable))` → `document.removeEventListener()`
- 条件付き依存: `if (enable)` → `PageThumbs.addExpirationFilter()`
- 条件付き依存: `if (!(enable))` → `PageThumbs.removeExpirationFilter()`
- 参照: `document.getElementById("menu_showAllTabs").hidden`, `gBrowser.tabContainer`, `gBrowser.tabbox.handleCtrlTab`
