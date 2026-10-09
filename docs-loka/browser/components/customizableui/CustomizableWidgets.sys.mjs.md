# browser/components/customizableui/CustomizableWidgets.sys.mjs

source: browser/components/customizableui/CustomizableWidgets.sys.mjs
source-hash: 488c6036ddeb844b995a316d7ac0a048ef8b2a46
lines: 846

## <module>
- 役割: 組み込みウィジェット(履歴、ズーム、編集、同期、パニックボタンなど)の定義配列 CustomizableWidgets を作り、設定に応じて項目を追加する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `CustomizableWidgets.push()`, `Services.prefs.getBoolPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## setAttributes()
- 位置: L67-96
- 役割: DOM 要素へ属性の辞書を反映する。false 値の属性は外し、label/tooltiptext はローカライズ文字列にし、shortcutId があればショートカット表記を付ける。
- 触るとき: ツールバーボタンの label や tooltiptext が正しく出ない、またはショートカットの表記が付かないときに見る。
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (!value)` → `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute(name))` → `aNode.removeAttribute()`
- 条件付き依存: `if (aAttrs.shortcutId)` → `doc.getElementById()`
- 条件付き依存: `if (shortcut)` → `additionalArgs.push()`
- 条件付き依存: `if (shortcut)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (name == "label" || name == "tooltiptext")` → `lazy.CustomizableUI.getLocalizedProperty()`
- 条件付き依存: `if (!(!value))` → `aNode.setAttribute()`
- 参照: `aAttrs.id`, `aAttrs.shortcutId`, `aNode.ownerDocument`

## handleEvent()
- 位置: L113-139
- 役割: 履歴ボタンのイベントを種類ごとに振り分ける。PanelMultiViewHidden, ViewShowing, unload, command を各処理へ渡し、未知のイベントは例外にする。
- 触るとき: 最近閉じたタブ/ウィンドウのサブビューが開かない、または履歴メニューの項目を押しても反応しないときに見る。
- 呼び出し先: `this.onPanelMultiViewHidden()`, `this.onSubViewShowing()`, `this.onWindowUnload()`
- 条件付き依存: `if (target.id == "appMenuRecentlyClosedTabs")` → `PanelUI.showSubView()`
- 条件付き依存: `if (target.id == "appMenuRecentlyClosedWindows")` → `PanelUI.showSubView()`
- 条件付き依存: `if (target.id == "appMenuSearchHistory")` → `PlacesCommandHook.searchHistory()`
- 参照: `event.type`, `target.documentGlobal`, `target.id`, `this.id`, `this.recentlyClosedTabsPanel`, `this.recentlyClosedWindowsPanel`

## onViewShowing()
- 位置: L140-192
- 役割: 履歴パネルを開くとき、最近閉じたタブ・ウィンドウの有効/無効と「セッションを復元」の表示を更新し、PlacesPanelview を一度だけ作る。
- 触るとき: 履歴パネルを開いた時点で閉じたタブ数の表示や履歴件数(42 件)がおかしいときに見る。
- 呼び出し先: `document.getElementById()`, `lazy.PanelMultiView.getViewNode()`, `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedTabsPanel ).addEventListener()`, `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedWindowsPanel ).addEventListener()`, `lazy.SessionStore.getClosedTabCount()`, `lazy.SessionStore.getClosedWindowCount()`, `panelview.addEventListener()`, `panelview.panelMultiView.addEventListener()`, `window.addEventListener()`
- 参照: `Ci.nsINavHistoryQueryOptions.QUERY_TYPE_HISTORY`, `Ci.nsINavHistoryQueryOptions.SORT_BY_DATE_DESCENDING`, `document.defaultView`, `event.target`, `lazy.PanelMultiView.getViewNode( document, "appMenu-restoreSession" ).hidden`, `lazy.PanelMultiView.getViewNode( document, "appMenuRecentlyClosedTabs" ).disabled`, `lazy.PanelMultiView.getViewNode( document, "appMenuRecentlyClosedWindows" ).disabled`, `lazy.SessionStore.canRestoreLastSession`, `panelview.ownerDocument`, `this._panelMenuView`, `this.recentlyClosedTabsPanel`, `this.recentlyClosedWindowsPanel`, `window.PlacesPanelview`
- XPCOM: [`nsINavHistoryQueryOptions`](../../../toolkit/components/places/nsINavHistoryService.idl.md)

## onViewHiding()
- 位置: L193-195
- 役割: 履歴パネルが隠れるときにデバッグログを出すだけの処理。
- 触るとき: 履歴パネルを閉じる処理を足すとき、またはパネルの非表示が呼ばれているか確かめるときに見る。
- 呼び出し先: `lazy.log.debug()`

## onPanelMultiViewHidden()
- 位置: L196-216
- 役割: パネルが閉じたとき PlacesPanelview を破棄し、サブビューと command のリスナーを外す。
- 触るとき: 履歴パネルを閉じた後も履歴の更新やリスナーが残るように見えるときに見る。
- 呼び出し先: `panelMultiView.removeEventListener()`
- 条件付き依存: `if (this._panelMenuView)` → `this._panelMenuView.uninit()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedTabsPanel ).removeEventListener()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode( document, this.recentlyClosedWindowsPanel ).removeEventListener()`
- 条件付き依存: `if (this._panelMenuView)` → `lazy.PanelMultiView.getViewNode( document, this.viewId ).removeEventListener()`
- 参照: `event.target`, `panelMultiView.ownerDocument`, `this._panelMenuView`, `this.recentlyClosedTabsPanel`, `this.recentlyClosedWindowsPanel`, `this.viewId`

## onWindowUnload()
- 位置: L217-221
- 役割: ウィンドウの unload 時に保持している _panelMenuView の参照を削除する(uninit は呼ばない)。
- 触るとき: ウィンドウを閉じた後に履歴パネルの後始末が足りないと感じるとき、uninit との役割分担を確かめるときに見る。
- 参照: `this._panelMenuView`

## onSubViewShowing()
- 位置: L222-258
- 役割: 最近閉じたタブ/ウィンドウのサブビューを SessionStore 由来の要素で作り直す。要素が無ければ空状態を示し、あればショートカット表示を付けて追加する。
- 触るとき: 最近閉じたタブ・ウィンドウの一覧の中身、または「すべて復元」項目の位置がおかしいときに見る。
- 呼び出し先: `body.appendChild()`, `document.createXULElement()`, `element.classList.contains()`, `lazy.CustomizableUI.addShortcut()`, `panelview.appendChild()`, `this._panelMenuView._setEmptyPopupStatus()`, `this._panelMenuView.clearAllContents()`, `utils.getTabsFragment()`, `utils.getWindowsFragment()`
- 参照: `body.children`, `body.className`, `document.defaultView`, `element.tagName`, `event.target`, `event.target.ownerDocument`, `fragment.childElementCount`, `lazy.RecentlyClosedTabsAndWindowsMenuUtils`, `panelview.id`, `this.recentlyClosedTabsPanel`

## onCreated()
- 位置: L264-266
- 役割: 保存ボタンのノードに command として Browser:SavePage を設定する。
- 触るとき: 保存ボタンを押しても保存が始まらないときに、コマンド名を確かめるために見る。
- 呼び出し先: `aNode.setAttribute()`

## onCreated()
- 位置: L273-275
- 役割: 印刷ボタンのノードに command として cmd_printPreviewToggle を設定する。
- 触るとき: 印刷ボタンが印刷プレビューを開かないときや、印刷コマンドを差し替えるときに見る。
- 呼び出し先: `aNode.setAttribute()`

## onCommand()
- 位置: L281-286
- 役割: 現在のウィンドウの gLazyFindCommand があれば onFindCommand で検索バーを開く。
- 触るとき: 検索ボタンを押しても検索バーが出ないときに、gLazyFindCommand が存在するかを確かめるために見る。
- 条件付き依存: `if (win.gLazyFindCommand)` → `win.gLazyFindCommand()`
- 参照: `aEvent.target.documentGlobal`, `win.gLazyFindCommand`

## onCreated()
- 位置: L292-294
- 役割: ファイルを開くボタンのノードに command として Browser:OpenFile を設定する。
- 触るとき: ファイルを開くボタンの動作を変えるとき、またはコマンド名の食い違いを調べるときに見る。
- 呼び出し先: `aNode.setAttribute()`

## onCommand()
- 位置: L301-308
- 役割: サイドバーボタン押下時、sidebar.revamp が有効なら handleToolbarButtonClick、無効なら toggle を呼ぶ。
- 触るとき: サイドバーボタンが開閉しない、または新旧サイドバーで挙動が違うときに sidebar.revamp の値と合わせて見る。
- 条件付き依存: `if (lazy.sidebarRevampEnabled)` → `SidebarController.handleToolbarButtonClick()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `SidebarController.toggle()`
- 参照: `aEvent.target.documentGlobal`, `lazy.sidebarRevampEnabled`

## onCreated()
- 位置: L309-329
- 役割: 新サイドバーならボタン表示を更新して overflows=false と badged を付け、旧サイドバーなら sidebar-box の checked と positionend を observes で監視させる。
- 触るとき: サイドバーボタンのチェック状態や位置の表示が追従しないときに見る。
- 条件付き依存: `if (lazy.sidebarRevampEnabled)` → `SidebarController.updateToolbarButton()`
- 条件付き依存: `if (lazy.sidebarRevampEnabled)` → `aNode.setAttribute()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `doc.createXULElement()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `obChecked.setAttribute()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `obPosition.setAttribute()`
- 条件付き依存: `if (!(lazy.sidebarRevampEnabled))` → `aNode.appendChild()`
- 参照: `aNode.documentGlobal`, `aNode.ownerDocument`, `lazy.sidebarRevampEnabled`

## onBuild()
- 位置: L335-389
- 役割: 拡大・縮小・リセットの 3 ボタンを、区切りとともに combined な toolbaritem にまとめて返す。
- 触るとき: ズームボタン群の並び、ラベル、ショートカットの割り当てを変えるときに見る。
- 呼び出し先: `aDocument.createXULElement()`, `buttons.forEach()`, `lazy.CustomizableUI.getLocalizedProperty()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `setAttributes()`
- 条件付き依存: `if (aIndex != 0)` → `node.appendChild()`
- 条件付き依存: `if (aIndex != 0)` → `aDocument.createXULElement()`

## onBuild()
- 位置: L395-468
- 役割: 切り取り・コピー・貼り付けの 3 ボタンをまとめた toolbaritem を作り、オーバーフローの変化を受ける listener を CustomizableUI に登録する。
- 触るとき: 編集ボタン群がツールバーのはみ出しで消えたり戻らなかったりするときに見る。
- 呼び出し先: `aDocument.createXULElement()`, `buttons.forEach()`, `lazy.CustomizableUI.addListener()`, `lazy.CustomizableUI.getLocalizedProperty()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `setAttributes()`
- 条件付き依存: `if (aIndex != 0)` → `node.appendChild()`
- 条件付き依存: `if (aIndex != 0)` → `aDocument.createXULElement()`

## onWidgetInstanceRemoved()
- 位置: L448-453
- 役割: このウィジェットのインスタンスが取り除かれたとき、登録した listener を CustomizableUI から外す。
- 触るとき: ウィジェットを削除した後も listener が残るように見えるときに見る。
- 呼び出し先: `lazy.CustomizableUI.removeListener()`
- 参照: `this.id`

## onWidgetOverflow()
- 位置: L454-458
- 役割: このノードがオーバーフローに入ったとき、updateEditUIVisibility で編集 UI の表示を更新する。
- 触るとき: 編集ボタン群がはみ出したときの表示が崩れるときに見る。
- 条件付き依存: `if (aWidgetNode == node)` → `node.documentGlobal.updateEditUIVisibility()`

## onWidgetUnderflow()
- 位置: L459-463
- 役割: このノードがオーバーフローから戻ったとき、updateEditUIVisibility で編集 UI の表示を更新する。
- 触るとき: はみ出しから戻った後に編集ボタンが正しく出ないときに見る。
- 条件付き依存: `if (aWidgetNode == node)` → `node.documentGlobal.updateEditUIVisibility()`

## onCommand()
- 位置: L473-475
- 役割: 文字化け修復ボタンで、BrowserCommands.forceEncodingDetection により文字コードの自動判定をやり直す。
- 触るとき: 文字コードの修復ボタンが効かないときに見る。
- 呼び出し先: `aEvent.view.BrowserCommands.forceEncodingDetection()`

## onCommand()
- 位置: L480-483
- 役割: 表示中のブラウザの URL を MailIntegration.sendLinkForBrowser でメールに送る。
- 触るとき: リンクをメールで送るボタンが反応しないときに見る。
- 呼び出し先: `win.MailIntegration.sendLinkForBrowser()`
- 参照: `aEvent.view`, `win.gBrowser.selectedBrowser`

## onCommand()
- 位置: L488-491
- 役割: ログインボタンで、Toolbar の entryPoint 付きにパスワードマネージャーを開く。
- 触るとき: ログインボタンからパスワード管理画面が開かないとき、または入口の識別を変えるときに見る。
- 呼び出し先: `lazy.LoginHelper.openPasswordManager()`
- 参照: `aEvent.view`

## onBuild()
- 位置: L501-539
- 役割: 共有ボタンを作る。macOS では共有ピッカーを開き、それ以外では popupshowing で共有メニューを埋める。
- 触るとき: 共有ボタンの表示やメニューの中身を直すとき、OS による分岐を追うときに見る。
- 呼び出し先: `Cu.getWeakReference()`, `aDocument.createXULElement()`, `aDocument.l10n.setAttributes()`, `lazy.SharingUtils.populateSharePopup()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `popup.addEventListener()`, `popup.setAttribute()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `node.classList.add()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `node.addEventListener()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Cu.getWeakReference()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `lazy.SharingUtils.shareOnMacPicker()`
- 参照: `AppConstants.platform`, `aDocument.defaultView.gBrowser.selectedBrowser`, `node.browsersToShare`, `node.contextBrowserToShare`

## onViewShowing()
- 位置: L549-574
- 役割: 同期パネルを開くとき、同期ボタンの文言を同期中かどうかで切り替え、SyncedTabsPanelList を作って各イベントを登録する。
- 触るとき: 同期パネルのボタン文言が古いままのときや、タブ一覧が出ないときに見る。
- 呼び出し先: `doc.l10n.setAttributes()`, `lazy.PanelMultiView.getViewNode()`, `panelview.addEventListener()`, `panelview.querySelector()`, `syncNowBtn.getAttribute()`, `syncNowButton.addEventListener()`
- 参照: `aEvent.target`, `aEvent.target.ownerDocument`, `doc.defaultView.SyncedTabsPanelList`, `panelview.documentGlobal.gSync._isCurrentlySyncing`, `panelview.ownerDocument`, `panelview.syncedTabsPanelList`

## onViewHiding()
- 位置: L575-586
- 役割: 同期パネルを閉じるとき、タブ一覧を破棄し、登録したイベントリスナーを外す。
- 触るとき: 同期パネルを開き直すとリスナーが重複するように見えるときに見る。
- 呼び出し先: `lazy.PanelMultiView.getViewNode()`, `panelview.removeEventListener()`, `panelview.syncedTabsPanelList.destroy()`, `syncNowButton.removeEventListener()`
- 参照: `aEvent.target`, `aEvent.target.ownerDocument`, `panelview.syncedTabsPanelList`

## handleEvent()
- 位置: L587-621
- 役割: 同期パネル内の mouseover, command, click を gSync の対応処理(ツールチップ更新、同期、設定を開く、デバイス接続)へ振り分ける。
- 触るとき: 同期パネルのボタンを押しても目的の画面が開かないときに、ボタン id と呼び出す関数を照合するために見る。
- 呼び出し先: `gSync.doSync()`, `gSync.openConnectAnotherDevice()`, `gSync.openDevicesManagementPage()`, `gSync.openPrefs()`, `gSync.refreshSyncButtonsTooltip()`
- 参照: `aEvent.target`, `aEvent.type`, `button.documentGlobal`, `button.id`

## onBuild()
- 位置: L630-711
- 役割: タブ送信ボタンを作り、同期の状態変化、タブ切り替え、場所変更の各通知で有効状態を更新する listener を登録する。
- 触るとき: タブ送信ボタンが有効にならない、または削除後も監視が残るときに見る。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `aDocument.createXULElement()`, `aDocument.documentGlobal.addEventListener()`, `aDocument.documentGlobal.gBrowser.addTabsProgressListener()`, `aDocument.documentGlobal.gSync.populateSendTabToolbarButton()`, `aDocument.l10n.setAttributes()`, `enableDisableButton()`, `lazy.CustomizableUI.addListener()`, `node.appendChild()`, `node.classList.add()`, `node.setAttribute()`, `popup.addEventListener()`, `popup.setAttribute()`
- 参照: `this.id`
- XPCOM: `Services.obs` / `Services.prefs`

## enableDisableButton()
- 位置: L639-644
- 役割: 現在のブラウザの URI で sendTabToolbarButtonShouldBeEnabled を問い合わせ、ボタンの disabled を設定する。
- 触るとき: タブを送れる条件を変えたとき、またはボタンが押せない理由を調べるときに見る。
- 呼び出し先: `aDocument.documentGlobal.gSync.sendTabToolbarButtonShouldBeEnabled()`
- 参照: `aDocument.documentGlobal.gBrowser.currentURI`, `node.disabled`

## onLocationChange()
- 位置: L661-665
- 役割: トップレベルの場所が変わったとき enableDisableButton を呼び、有効状態を取り直す。
- 触るとき: ページ遷移の後にタブ送信ボタンの有効状態が古いままのときに見る。
- 条件付き依存: `if (webProgress.isTopLevel)` → `enableDisableButton()`
- 参照: `webProgress.isTopLevel`

## onWidgetInstanceRemoved()
- 位置: L674-698
- 役割: ボタンが取り除かれたとき、CustomizableUI の listener、各 observer、タブのイベントと進捗 listener を外す。
- 触るとき: タブ送信ボタンを外した後もオブザーバーが動き続けるときに見る。
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `aDocument.documentGlobal.gBrowser.removeTabsProgressListener()`, `aDocument.documentGlobal.removeEventListener()`, `lazy.CustomizableUI.removeListener()`
- 参照: `this.id`
- XPCOM: `Services.obs` / `Services.prefs`

## onCommand()
- 位置: L718-721
- 役割: 設定ボタン押下で openPreferences を呼ぶ。
- 触るとき: 設定ボタンの遷移先を変えるとき、または開く画面が違うときに見る。
- 呼び出し先: `win.openPreferences()`
- 参照: `aEvent.target.documentGlobal`

## forgetButtonCalled()
- 位置: L734-768
- 役割: パニックボタンの忘れる操作で、選んだ時間範囲の履歴・Cookie 等を Sanitizer で消し、完了後に別ウィンドウの PanicButtonNotifier へ通知する。
- 触るとき: パニックボタンで消す対象や範囲、通知の経路を変えるときに見る。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.wm.getMostRecentWindow()`, `doc.getElementById()`, `lazy.Sanitizer.getClearRange()`, `lazy.Sanitizer.sanitize()`, `promise.then()`
- 条件付き依存: `if (otherWindow.closed)` → `console.error()`
- 条件付き依存: `if (otherWindow.PanicButtonNotifier)` → `otherWindow.PanicButtonNotifier.notify()`
- 参照: `aEvent.target.ownerDocument`, `doc.defaultView`, `group.value`, `otherWindow.PanicButtonNotifier`, `otherWindow.PanicButtonNotifierShouldNotify`, `otherWindow.closed`
- XPCOM: `Services.wm`

## handleEvent()
- 位置: L769-775
- 役割: パニックボタンの command イベントを forgetButtonCalled へ渡し、他のイベントは無視する。
- 触るとき: パニックボタンにイベントの扱いを足すとき、または忘れる操作が起きないときに見る。
- 呼び出し先: `this.forgetButtonCalled()`
- 参照: `aEvent.type`

## onViewShowing()
- 位置: L776-792
- 役割: パニックビューを開くとき、時間範囲を 5 分に合わせ、忘れるボタンに command の listener を付け、翻訳の完了を待つ blocker を登録する。
- 触るとき: パニックビューを開いた直後の既定時間範囲や、ボタンの反応がおかしいときに見る。
- 呼び出し先: `aEvent.target.querySelector()`, `doc.getElementById()`, `doc.l10n.translateElements()`, `forgetButton.addEventListener()`
- 条件付き依存: `if (eventBlocker)` → `aEvent.detail.addBlocker()`
- 参照: `aEvent.target`, `aEvent.target.documentGlobal`, `group.selectedItem`, `win.document`

## onViewHiding()
- 位置: L793-798
- 役割: パニックビューを閉じるとき、忘れるボタンの command listener を外す。
- 触るとき: パニックビューを閉じた後にボタンが反応し続けるときに見る。
- 呼び出し先: `aEvent.target.querySelector()`, `forgetButton.removeEventListener()`

## onCommand()
- 位置: L807-810
- 役割: プライベートブラウズのボタンで、private 指定の新しいブラウザウィンドウを開く。
- 触るとき: プライベートウィンドウを開くボタンの挙動を変えるときに見る。
- 呼び出し先: `win.OpenBrowserWindow()`
- 参照: `e.target.documentGlobal`

## onCreated()
- 位置: L826-829
- 役割: Firefox View ボタンに role=button と aria-pressed=false を付ける。
- 触るとき: Firefox View ボタンの状態がスクリーンリーダーで正しく読まれないときに見る。
- 呼び出し先: `node.setAttribute()`

## onCommand()
- 位置: L836-843
- 役割: ミニウィンドウボタンで、選択中のブラウザに対しスクリーンショットの範囲選択を MINI_WINDOW モードで開始する。
- 触るとき: ミニウィンドウボタンが範囲選択を起動しないとき、または選択モードを変えるときに見る。
- 呼び出し先: `lazy.ScreenshotsUtils.toggle()`
- 参照: `aEvent.currentTarget.documentGlobal`, `lazy.SELECTION_MODES.MINI_WINDOW`, `win.gBrowser.selectedBrowser`
