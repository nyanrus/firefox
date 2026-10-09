# browser/components/extensions/parent/ext-browserAction.js

source: browser/components/extensions/parent/ext-browserAction.js
source-hash: 45ce82b3efb50bdf6252aae99a51b46723157ad6
lines: 1133

## <module>
- 役割: browserAction と action の WebExtension API の親側実装。ツールバーや拡張メニューのボタン作成、ポップアップの事前読み込みと表示、クリックの配送を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## actionWidgetId()
- 位置: L44-46
- 役割: ウィジェット ID から -browser-action を付けた CustomizableUI 上の ID を作る。
- 触るとき: 拡張のボタンの ID が他の要素と衝突する問題を調べるとき。

## BrowserAction.constructor()
- 位置: L49-58
- 役割: タブごとの拡張データを BrowserActionBase に渡し、タブ、ウィンドウの既定値は getContextData(null) から取るように設定する。
- 触るとき: ボタンの表示に使うタブごとの値が既定値に戻る問題を調べるとき。
- 呼び出し先: `ChromeUtils.getClassName()`, `super()`, `tabContext.get()`
- 条件付き依存: `if (ChromeUtils.getClassName(target) == "Window")` → `this.getContextData()`
- 参照: `target.documentGlobal`, `this.buttonDelegate`

## BrowserAction.updateOnChange()
- 位置: L60-72
- 役割: タブかウィンドウが与えられれば対象ウィンドウのボタンを更新し、無ければ開いている全ブラウザウィンドウを更新する。
- 触るとき: タブの切り替えや設定変更でボタンの表示が古いままになる問題を調べるとき。
- 条件付き依存: `if (target)` → `ChromeUtils.getClassName()`
- 条件付き依存: `if (ChromeUtils.getClassName(target) == "Window")` → `this.buttonDelegate.updateWindow()`
- 条件付き依存: `if (target.selected)` → `this.buttonDelegate.updateWindow()`
- 条件付き依存: `if (!(target))` → `windowTracker.browserWindows()`
- 条件付き依存: `if (!(target))` → `this.buttonDelegate.updateWindow()`
- 参照: `target.documentGlobal`, `target.selected`

## BrowserAction.getTab()
- 位置: L74-79
- 役割: タブ ID が null でなければ tabTracker からタブ要素を引き、null なら null を返す。
- 触るとき: アクションの呼び出しで tabId が不正になる問題を調べるとき。
- 条件付き依存: `if (tabId !== null)` → `tabTracker.getTab()`

## BrowserAction.getWindow()
- 位置: L81-86
- 役割: ウィンドウ ID が null でなければ windowTracker からウィンドウを引き、null なら null を返す。
- 触るとき: アクションの呼び出しで windowId が不正になる問題を調べるとき。
- 条件付き依存: `if (windowId !== null)` → `windowTracker.getWindow()`

## BrowserAction.dispatchClick()
- 位置: L88-90
- 役割: ボタンの delegate に click イベントを発行し、onClicked に流す。
- 触るとき: onClicked のリスナーにクリックが届かない問題を調べるとき。
- 呼び出し先: `this.buttonDelegate.emit()`

## BrowserAction.isPanelShownBlockingOpenPopup()
- 位置: L92-108
- 役割: 拡張パネルが開いている、グローバルにポップアップを止める設定がある、またはボタンのメニューが開いているときに true を返す。
- 触るとき: openPopup が拒否される条件を変えるとき。
- 呼び出し先: `isGloballyBlockingOpenPopup()`, `window.document.getElementById()`, `window.gUnifiedExtensions.isPanelOpen()`
- 参照: `this.buttonDelegate.buttonViewId`, `this.buttonDelegate.widget`, `window.document.getElementById(this.buttonDelegate.buttonViewId) ?.open`

## for()
- 位置: L112-114
- 役割: 拡張に紐づく browserAction のインスタンスを WeakMap から返す。
- 触るとき: 拡張の browserAction インスタンスを他の処理から取り出すとき。
- 呼び出し先: `browserActionMap.get()`

## onManifestEntry()
- 位置: async L116-151
- 役割: manifest の browser_action か action から設定を読み、ボタンのアイコン、ID、ビュー ID を決めてウィジェットを作る。
- 触るとき: 拡張の読み込み時にボタンが出ない、またはアイコンが出ない問題を調べるとき。
- 呼び出し先: `StartupCache.get()`, `actionWidgetId()`, `browserActionMap.set()`, `makeWidgetId()`, `this.action.getIcon()`, `this.action.loadIconData()`, `this.build()`, `this.getIconData()`, `this.iconData.set()`
- 参照: `extension.id`, `extension.manifest.action`, `extension.manifest.browser_action`, `extension.tabManager`, `options.browser_style`, `this.action`, `this.browserStyle`, `this.buttonViewId`, `this.eventQueue`, `this.iconData`, `this.id`, `this.pendingPopup`, `this.pendingPopupTimeout`, `this.tabManager`, `this.viewId`, `this.widget`

## onUpdate()
- 位置: L153-164
- 役割: 新しい版に browser_action も action も無ければ、ウィジェットを非表示として telemetry に記録する。
- 触るとき: 拡張の更新でボタンが消えた後の telemetry の状態を調べるとき。
- 条件付き依存: `if (!("browser_action" in manifest || "action" in manifest))` → `BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (!("browser_action" in manifest || "action" in manifest))` → `actionWidgetId()`
- 条件付き依存: `if (!("browser_action" in manifest || "action" in manifest))` → `makeWidgetId()`

## onDisable()
- 位置: L166-172
- 役割: 拡張が無効化されたとき、ウィジェットを非表示として telemetry に記録する。
- 触るとき: 無効化後のボタンの telemetry 記録を調べるとき。
- 呼び出し先: `BrowserUsageTelemetry.recordWidgetChange()`, `actionWidgetId()`, `makeWidgetId()`

## onUninstall()
- 位置: L174-182
- 役割: 拡張がアンインストールされたとき、ウィジェットを非表示として telemetry に記録する。
- 触るとき: アンインストール後の telemetry の記録を調べるとき。
- 呼び出し先: `BrowserUsageTelemetry.recordWidgetChange()`, `actionWidgetId()`, `makeWidgetId()`

## onShutdown()
- 位置: L184-191
- 役割: インスタンスの登録を外し、アクションとウィジェットを破棄し、表示中のポップアップを閉じる。
- 触るとき: 拡張の終了時にボタンやポップアップが残る問題を調べるとき。
- 呼び出し先: `CustomizableUI.destroyWidget()`, `browserActionMap.delete()`, `this.action.onShutdown()`, `this.clearPopup()`
- 参照: `this.extension`, `this.id`

## build()
- 位置: L193-487
- 役割: CustomizableUI にカスタムウィジェットを作り、ビルド、作成前、作成後、破棄の各コールバックを渡す。作成後は telemetry の状態も更新する。
- 触るとき: ボタンの配置、既定の領域、プライベートブラウジングでの表示を変えるとき。
- 呼び出し先: `CustomizableUI.createWidget()`, `this.action.getDefaultArea()`, `this.action.getProperty()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `ExtensionParent.browserStartupPromise.then()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `BrowserUsageTelemetry.recordWidgetChange()`
- 参照: `extension.privateBrowsingAllowed`, `placement?.area`, `this.extension.startupReason`, `this.id`, `this.viewId`, `this.widget`, `widget.id`

## onBuild()
- 位置: L213-301
- 役割: 拡張のボタンの DOM を組み立てる。アクションボタン、メニューボタン、ラベル、メッセージ用のデッキ、メッセージバーを作る。
- 触るとき: ツールバーやパネルのボタンの構造、CSS クラス、属性を変えるとき。
- 呼び出し先: `button.appendChild()`, `button.classList.add()`, `button.setAttribute()`, `contents.appendChild()`, `contents.classList.add()`, `contents.setAttribute()`, `deck.appendChild()`, `deck.classList.add()`, `document.createElement()`, `document.createXULElement()`, `document.l10n.setAttributes()`, `menuButton.classList.add()`, `menuButton.setAttribute()`, `messageDefault.classList.add()`, `messageHover.classList.add()`, `messageHoverForMenuButton.classList.add()`, `name.classList.add()`, `node.append()`, `node.classList.add()`, `node.setAttribute()`, `rowWrapper.append()`, `rowWrapper.classList.add()`
- 参照: `extension.id`, `messagebarWrapper.extensionId`, `node.viewButton`, `this.buttonViewId`

## onBeforeCreated()
- 位置: L303-319
- 役割: appMenu のビューキャッシュにパネルビューを作る。menus か contextMenus の権限があれば popupshowing を監視する。
- 触るとき: パネル内のポップアップの表示先や、コンテキストメニューの監視条件を変えるとき。
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `document.getElementById("appMenu-viewCache").appendChild()`, `this.extension.hasPermission()`, `view.setAttribute()`
- 条件付き依存: `if ( this.extension.hasPermission("menus") || this.extension.hasPermission("contextMenus") )` → `document.addEventListener()`
- 参照: `this.viewId`, `view.id`

## onDestroyed()
- 位置: L321-330
- 役割: popupshowing の監視を外し、表示中のポップアップを閉じてパネルビューを削除する。
- 触るとき: 拡張の無効化でパネルの残骸が残る問題を調べるとき。
- 呼び出し先: `document.getElementById()`, `document.removeEventListener()`
- 条件付き依存: `if (view)` → `this.clearPopup()`
- 条件付き依存: `if (view)` → `CustomizableUI.hidePanelForNode()`
- 条件付き依存: `if (view)` → `view.remove()`
- 参照: `this.viewId`

## onCreated()
- 位置: L332-369
- 役割: 作成されたボタンに CSS クラス、属性、マウス・フォーカスのハンドラを付け、メニューボタンのラベルを設定し、同期的に表示を更新する。
- 触るとき: ボタンのイベントハンドラや初期表示を変えるとき。
- 呼び出し先: `actionButton.classList.add()`, `actionButton.setAttribute()`, `node.ownerDocument.l10n.setAttributes()`, `node.querySelector()`, `this.action.getContextData()`, `this.updateButton()`
- 参照: `actionButton.onauxclick`, `actionButton.onblur`, `actionButton.onfocus`, `actionButton.onmousedown`, `actionButton.onmouseout`, `actionButton.onmouseover`, `menuButton.onblur`, `menuButton.onfocus`, `menuButton.onmouseout`, `menuButton.onmouseover`, `this.extension.id`, `this.extension.name`

## actionButton.onmousedown()
- 位置: L342-342
- 役割: マウスダウンを handleEvent に渡す。
- 触るとき: マウスダウン時のポップアップの事前読み込みを調べるとき。
- 呼び出し先: `this.handleEvent()`

## actionButton.onmouseover()
- 位置: L343-343
- 役割: マウスオーバーを handleEvent に渡す。
- 触るとき: ホバー時の表示とポップアップの事前読み込みを調べるとき。
- 呼び出し先: `this.handleEvent()`

## actionButton.onmouseout()
- 位置: L344-344
- 役割: マウスアウトを handleEvent に渡す。
- 触るとき: ホバーを外したときの表示と事前読み込みの解除を調べるとき。
- 呼び出し先: `this.handleEvent()`

## actionButton.onauxclick()
- 位置: L345-345
- 役割: 中ボタンクリックを handleEvent に渡す。
- 触るとき: 中クリックで onClicked が発火する条件を調べるとき。
- 呼び出し先: `this.handleEvent()`

## menuButton.onblur()
- 位置: L356-356
- 役割: メニューボタンのフォーカス喪失を handleMenuButtonEvent に渡す。
- 触るとき: メニューボタンのメッセージ表示が元に戻らない問題を調べるとき。
- 呼び出し先: `this.handleMenuButtonEvent()`

## menuButton.onfocus()
- 位置: L357-357
- 役割: メニューボタンのフォーカスを handleMenuButtonEvent に渡す。
- 触るとき: メニューボタンにフォーカスしたときのメッセージ表示を調べるとき。
- 呼び出し先: `this.handleMenuButtonEvent()`

## menuButton.onmouseout()
- 位置: L358-358
- 役割: メニューボタンのマウスアウトを handleMenuButtonEvent に渡す。
- 触るとき: メニューボタンのホバー表示が消えない問題を調べるとき。
- 呼び出し先: `this.handleMenuButtonEvent()`

## menuButton.onmouseover()
- 位置: L359-359
- 役割: メニューボタンのマウスオーバーを handleMenuButtonEvent に渡す。
- 触るとき: メニューボタンのホバー表示を調べるとき。
- 呼び出し先: `this.handleMenuButtonEvent()`

## actionButton.onblur()
- 位置: L361-361
- 役割: アクションボタンのフォーカス喪失を handleEvent に渡す。
- 触るとき: アクションボタンのフォーカス時の表示を調べるとき。
- 呼び出し先: `this.handleEvent()`

## actionButton.onfocus()
- 位置: L362-362
- 役割: アクションボタンのフォーカスを handleEvent に渡す。
- 触るとき: キーボード操作で事前読み込みを始める条件を調べるとき。
- 呼び出し先: `this.handleEvent()`

## onBeforeCommand()
- 位置: L371-392
- 役割: クリックの button と修飾キーを lastClickInfo に保存し、openPopupWithoutUserInteraction を読む。アクションボタンなら view、メニューボタンなら command を返す。
- 触るとき: クリック種別でポップアップを出すか拡張メニューを出すかの振り分けを変えるとき。
- 呼び出し先: `clickModifiersFromEvent()`, `event.target.classList.contains()`
- 条件付き依存: `if (!( event.target.classList.contains( "unified-extensions-item-action-button" ) ))` → `event.target.classList.contains()`
- 参照: `event.button`, `event.detail?.openPopupWithoutUserInteraction`, `this.lastClickInfo`, `this.openPopupWithoutUserInteraction`

## onCommand()
- 位置: L394-416
- 役割: 左クリックのメニューボタンで、ユーザーの拡張コンテキストメニューを対象ボタンの位置に開く。
- 触るとき: 拡張のメニューボタンの開き方や位置を変えるとき。
- 呼び出し先: `popup.openPopup()`, `target.ownerDocument.getElementById()`
- 参照: `event.button`, `target.firstElementChild`

## onViewShowing()
- 位置: async L418-470
- 役割: ビューを開くとき、クリックかポップアップの URL を決め、ポップアップを attach する。URL が無ければビューを閉じる。失敗はログに残して既定の動作を止める。
- 触るとき: ボタンを押したときにポップアップが出ない、または不要に出る問題を調べるとき。
- 呼び出し先: `ExtensionTelemetry.browserActionPopupOpen.stopwatchStart()`, `this.action.getPopupUrl()`, `this.action.triggerClickOrPopup()`
- 条件付き依存: `if (popupURL)` → `this.getPopup()`
- 条件付き依存: `if (popupURL)` → `popup.attach()`
- 条件付き依存: `if (popupURL)` → `event.detail.addBlocker()`
- 条件付き依存: `if (popupURL)` → `ExtensionTelemetry.browserActionPopupOpen.stopwatchFinish()`
- 条件付き依存: `if (this.eventQueue.length)` → `ExtensionTelemetry.browserActionPreloadResult.histogramAdd()`
- 条件付き依存: `if (popupURL)` → `ExtensionTelemetry.browserActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (popupURL)` → `Cu.reportError()`
- 条件付き依存: `if (popupURL)` → `event.preventDefault()`
- 条件付き依存: `if (!(popupURL))` → `ExtensionTelemetry.browserActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (!(popupURL))` → `event.preventDefault()`
- 条件付き依存: `if (!(popupURL))` → `CustomizableUI.hidePanelForNode()`
- 参照: `document.defaultView`, `document.defaultView.gBrowser`, `event.target`, `event.target.ownerDocument`, `tabbrowser.selectedTab`, `this.eventQueue`, `this.eventQueue.length`, `this.lastClickInfo`, `this.openPopupWithoutUserInteraction`

## openPopup()
- 位置: async L497-544
- 役割: ウィンドウがフォーカスされておりポップアップ URL があるときに、ボタンへ command イベントを送ってポップアップを開く。パネル内なら先にパネルを開く。
- 触るとき: プログラムからポップアップを開く経路や、拒否される条件を変えるとき。
- 呼び出し先: `this.action.getPopupUrl()`, `this.widget.forWindow()`, `toolbarButton.dispatchEvent()`, `widgetForWindow.node.querySelector()`
- 条件付き依存: `if (Services.focus.activeWindow !== window)` → `this.extension.logger.warn()`
- 条件付き依存: `if (this.widget.areaType == CustomizableUI.TYPE_PANEL)` → `window.gUnifiedExtensions.openPanel()`
- 参照: `CustomizableUI.TYPE_PANEL`, `Services.focus.activeWindow`, `this.widget.areaType`, `toolbarButton.open`, `widgetForWindow.node`, `window.CustomEvent`, `window.gBrowser.selectedTab`
- XPCOM: `Services.focus`

## triggerAction()
- 位置: L555-571
- 役割: 開いているポップアップは閉じ、無ければ URL を決めてポップアップを開く。ユーザーのクリックと同じ効果を持つ。
- 触るとき: 拡張の操作を外部から起動する経路（ショートカットなど）を調べるとき。
- 呼び出し先: `ViewPopup.for()`, `this.action.triggerClickOrPopup()`
- 条件付き依存: `if (!this.pendingPopup && popup)` → `popup.closePopup()`
- 条件付き依存: `if (popupUrl)` → `this.openPopup()`
- 参照: `this.extension`, `this.pendingPopup`, `window.gBrowser.selectedTab`

## handleMenuButtonEvent()
- 位置: L578-604
- 役割: メニューボタンのフォーカスやホバーで、メッセージ用デッキの表示を MENU_HOVER と DEFAULT の間で切り替える。
- 触るとき: メニューボタンのホバーやフォーカスの表示が正しく切り替わらないとき。
- 呼び出し先: `node?.querySelector()`, `this.widget.forWindow()`
- 参照: `event.target.documentGlobal`, `event.type`, `messageDeck.selectedIndex`, `window.gBrowser`, `window.gUnifiedExtensions.MESSAGE_DECK_INDEX_DEFAULT`, `window.gUnifiedExtensions.MESSAGE_DECK_INDEX_MENU_HOVER`

## handleEvent()
- 位置: L606-744
- 役割: マウスダウンでポップアップを事前読み込みし、マウスアップで必要なら一定時間後に破棄する。ホバーとフォーカスで表示を切り替え、popupshowing では拡張コンテキストメニューを更新し、中クリックでは onClicked を発火する。
- 触るとき: ボタンのマウス操作の一連の流れや事前読み込みのタイミングを変えるとき。
- 呼び出し先: `ViewPopup.for()`, `contexts.includes()`, `node.contains()`, `this.action.getPopupUrl()`, `this.action.getProperty()`, `this.widget.forWindow()`, `window.document.getElementById()`
- 条件付き依存: `if (event.button == 0)` → `this.action.getPopupUrl()`
- 条件付き依存: `if (event.button == 0)` → `ViewPopup.for()`
- 条件付き依存: `if ( popupURL && (this.pendingPopup || !ViewPopup.for(this.extension, window)) )` → `this.action.setActiveTabForPreload()`
- 条件付き依存: `if ( popupURL && (this.pendingPopup || !ViewPopup.for(this.extension, window)) )` → `this.eventQueue.push()`
- 条件付き依存: `if ( popupURL && (this.pendingPopup || !ViewPopup.for(this.extension, window)) )` → `this.getPopup()`
- 条件付き依存: `if ( popupURL && (this.pendingPopup || !ViewPopup.for(this.extension, window)) )` → `window.addEventListener()`
- 条件付き依存: `if (!( popupURL && (this.pendingPopup || !ViewPopup.for(this.extension, window)) ))` → `this.clearPopup()`
- 条件付き依存: `if (event.button == 0)` → `this.clearPopupTimeout()`
- 条件付き依存: `if (this.pendingPopup)` → `this.widget.forWindow()`
- 条件付き依存: `if (this.pendingPopup)` → `node.contains()`
- 条件付き依存: `if (node && node.contains(event.originalTarget))` → `setTimeout()`
- 条件付き依存: `if (node && node.contains(event.originalTarget))` → `this.clearPopup()`
- 条件付き依存: `if (!(node && node.contains(event.originalTarget)))` → `this.clearPopup()`
- 条件付き依存: `if (node)` → `node.querySelector()`
- 条件付き依存: `if (this.eventQueue.length)` → `ExtensionTelemetry.browserActionPreloadResult.histogramAdd()`
- 条件付き依存: `if (this.eventQueue.length)` → `this.eventQueue.pop()`
- 条件付き依存: `if (this.pendingPopup)` → `this.clearPopup()`
- 条件付き依存: `if (contexts.includes(menu.id) && node && node.contains(trigger))` → `this.updateContextMenu()`
- 条件付き依存: `if (this.action.getProperty(tab, "enabled"))` → `this.action.setActiveTabForPreload()`
- 条件付き依存: `if (this.action.getProperty(tab, "enabled"))` → `this.tabManager.addActiveTabPermission()`
- 条件付き依存: `if (this.action.getProperty(tab, "enabled"))` → `this.action.dispatchClick()`
- 条件付き依存: `if (this.action.getProperty(tab, "enabled"))` → `clickModifiersFromEvent()`
- 条件付き依存: `if (this.action.getProperty(tab, "enabled"))` → `CustomizableUI.hidePanelForNode()`
- 参照: `button.documentGlobal`, `event.button`, `event.originalTarget`, `event.target`, `event.type`, `menu.id`, `menu.triggerNode`, `node.querySelector( ".unified-extensions-item-message-deck" ).selectedIndex`, `this.eventQueue`, `this.eventQueue.length`, `this.extension`, `this.id`, `this.pendingPopup`, `this.pendingPopupTimeout`, `this.widget.forWindow(window).node`, `window.gBrowser`, `window.gBrowser.selectedTab`, `window.gUnifiedExtensions.MESSAGE_DECK_INDEX_DEFAULT`, `window.gUnifiedExtensions.MESSAGE_DECK_INDEX_HOVER`

## updateContextMenu()
- 位置: L752-766
- 役割: menus か contextMenus の権限があれば、拡張のアクション用の項目を指定のメニューに追加する。
- 触るとき: ボタンの右クリックメニューに拡張の項目が出ない問題を調べるとき。
- 呼び出し先: `this.extension.hasPermission()`
- 条件付き依存: `if ( this.extension.hasPermission("contextMenus") || this.extension.hasPermission("menus") )` → `global.actionContextMenu()`
- 参照: `this.extension`, `this.extension.manifestVersion`

## getPopup()
- 位置: L784-811
- 役割: 事前読み込み済みのポップアップが同じウィンドウと URL なら再利用し、違えば破棄して新しい ViewPopup を作る。
- 触るとき: ポップアップの再利用条件や、事前読み込みの扱いを変えるとき。
- 呼び出し先: `this.clearPopupTimeout()`
- 条件付き依存: `if (!blockParser)` → `pendingPopup.unblockParser()`
- 条件付き依存: `if (pendingPopup)` → `pendingPopup.destroy()`
- 参照: `pendingPopup.popupURL`, `pendingPopup.window`, `this.browserStyle`, `this.extension`, `this.pendingPopup`

## clearPopup()
- 位置: L816-823
- 役割: タイムアウトを解除し、事前読み込み中のポップアップを破棄して、アクティブタブの事前読み込み設定を消す。
- 触るとき: 事前読み込みしたポップアップが残って次の表示を妨げる問題を調べるとき。
- 呼び出し先: `this.action.setActiveTabForPreload()`, `this.clearPopupTimeout()`
- 条件付き依存: `if (this.pendingPopup)` → `this.pendingPopup.destroy()`
- 参照: `this.pendingPopup`

## clearPopupTimeout()
- 位置: L828-837
- 役割: 待機中の事前読み込みのマウスアップ監視と、タイムアウトを解除する。
- 触るとき: 事前読み込みのタイムアウトが二重に動く問題を調べるとき。
- 条件付き依存: `if (this.pendingPopup)` → `this.pendingPopup.window.removeEventListener()`
- 条件付き依存: `if (this.pendingPopupTimeout)` → `clearTimeout()`
- 参照: `this.pendingPopup`, `this.pendingPopupTimeout`

## updateButton()
- 位置: L841-934
- 役割: タブのデータからボタンのラベル、タイトル、ホバー時のメッセージ、バッジ、無効状態、バッジの色、アイコン、注意状態を反映する。sync が false なら次の描画で更新する。
- 触るとき: ボタンの見た目（バッジ、アイコン、無効表示、注意表示）が更新されない問題を調べるとき。
- 呼び出し先: `OriginControls.getStateMessageIDs()`, `WebExtensionPolicy.getByID()`, `node.querySelector()`
- 条件付き依存: `if (sync)` → `callback()`
- 条件付き依存: `if (!(sync))` → `node.documentGlobal.requestAnimationFrame()`
- 参照: `node.documentGlobal.gBrowser.selectedTab`, `tabData.popup`, `tabData.title`, `this.extension.id`, `this.extension.name`

## callback()
- 位置: L860-928
- 役割: ボタンの属性と文言を実際に設定する本体。注意状態で文言を切り替え、バッジ、無効状態、色、アイコン、メッセージバーを反映する。
- 触るとき: ボタン表示の反映処理そのものを変えるとき。
- 呼び出し先: `button.querySelector()`, `button.setAttribute()`, `messagebarWrapper.refresh()`, `node.ownerDocument.l10n.setAttributes()`, `node.querySelector()`, `node.toggleAttribute()`, `serializeColor()`, `this.action.getTextColor()`, `this.iconData.get()`
- 条件付き依存: `if (messages)` → `button.querySelector()`
- 条件付き依存: `if (messages)` → `node.ownerDocument.l10n.setAttributes()`
- 条件付き依存: `if (tabData.badgeText)` → `button.setAttribute()`
- 条件付き依存: `if (!(tabData.badgeText))` → `button.removeAttribute()`
- 条件付き依存: `if (tabData.enabled)` → `button.removeAttribute()`
- 条件付き依存: `if (!(tabData.enabled))` → `button.setAttribute()`
- 参照: `button.querySelector(".unified-extensions-item-name").textContent`, `messages.default`, `messages.onHover`, `tabData.badgeBackgroundColor`, `tabData.badgeText`, `tabData.enabled`, `tabData.icon`, `this.extension?.name`

## serializeColor()
- 位置: L905-906
- 役割: RGBA の配列を rgba() の CSS 文字列に変換する。
- 触るとき: バッジ色の表示が違って見えるときに確かめる。

## getIconData()
- 位置: L936-973
- 役割: 16、32、64 の各サイズで最適なアイコンを選び、明るい背景と暗い背景の CSS 変数を作る。
- 触るとき: 拡張のアイコンがテーマや解像度によって違って見える問題を調べるとき。
- 呼び出し先: `IconDetails.getPreferredIcon()`, `getStyle()`
- 参照: `IconDetails.getPreferredIcon(icons, this.extension, 16).icon`, `IconDetails.getPreferredIcon(icons, this.extension, 32).icon`, `IconDetails.getPreferredIcon(icons, this.extension, 64).icon`, `this.extension`

## getIcon()
- 位置: L937-942
- 役割: アイコンがテーマごとの辞書なら指定テーマのものを、そうでなければそのまま取り出し、URL をエスケープする。
- 触るとき: テーマ別のアイコンの選び方を変えるとき。
- 呼び出し先: `IconDetails.escapeUrl()`
- 条件付き依存: `if (typeof icon === "object")` → `IconDetails.escapeUrl()`

## getBackgroundImage()
- 位置: L944-952
- 役割: 1 倍と 2 倍の URL から、解像度に応じた image-set を作る。同じなら単一の url を返す。
- 触るとき: 高解像度ディスプレイでのアイコンの表示を調べるとき。

## getStyle()
- 位置: L954-963
- 役割: 通常時とダーク時の CSS 変数の組を作り、指定の変数名で返す。
- 触るとき: アイコン用の CSS 変数名や組み合わせを変えるとき。
- 呼び出し先: `getBackgroundImage()`, `getIcon()`

## updateWindow()
- 位置: L981-998
- 役割: ウィンドウの現在のタブのデータと注意状態を取り、そのウィンドウのボタンを更新する。
- 触るとき: タブを切り替えたあとに表示が古いままの問題を調べるとき。
- 呼び出し先: `this.widget.forWindow()`
- 条件付き依存: `if (node)` → `OriginControls.getAttentionState()`
- 条件付き依存: `if (node)` → `this.updateButton()`
- 条件付き依存: `if (node)` → `this.action.getContextData()`
- 参照: `this.extension.policy`, `this.widget.forWindow(window).node`, `window.gBrowser.selectedTab`

## onClicked()
- 位置: L1001-1024
- 役割: click の内容を、タブを拡張側へ変換して fire.sync で届ける。起動直後はリスナーを再開してから送る。
- 触るとき: onClicked が再起動後に届かない、または早く届く問題を調べるとき。
- 呼び出し先: `this.on()`

## listener()
- 位置: async L1004-1013
- 役割: 起動待ちを済ませてから、タブを拡張の形式に変えて click を送る。
- 触るとき: onClicked の引数やタイミングを変えるとき。
- 呼び出し先: `context?.withPendingBrowser()`, `fire.sync()`, `tabManager.convert()`
- 条件付き依存: `if (fire.wakeup)` → `fire.wakeup()`
- 参照: `fire.wakeup`, `tab.linkedBrowser`

## unregister()
- 位置: L1016-1018
- 役割: click のリスナーを外す。
- 触るとき: onClicked の購読解除が効かない問題を調べるとき。
- 呼び出し先: `this.off()`

## convert()
- 位置: L1019-1022
- 役割: 永続イベントの復元時に、新しい fire と context を受け取って差し替える。
- 触るとき: onClicked が再起動後に別の context へ届く問題を調べるとき。

## onUserSettingsChanged()
- 位置: L1025-1055
- 役割: ウィジェットがツールバーと拡張メニューの間で移動したときに、isOnToolbar を付けて通知する。
- 触るとき: ツールバーへの配置の変化が拡張に通知されない問題を調べるとき。
- 呼び出し先: `CustomizableUI.addListener()`

## onWidgetRemoved()
- 位置: L1027-1035
- 役割: このウィジェットが拡張メニューから外れたら、isOnToolbar を true にして通知する。
- 触るとき: ツールバーへの移動の通知内容を変えるとき。
- 条件付き依存: `if (oldArea === CustomizableUI.AREA_ADDONS)` → `fire.async()`
- 参照: `CustomizableUI.AREA_ADDONS`, `this.id`

## onWidgetAdded()
- 位置: L1036-1044
- 役割: このウィジェットが拡張メニューへ入ったら、isOnToolbar を false にして通知する。
- 触るとき: 拡張メニューへの移動の通知内容を変えるとき。
- 条件付き依存: `if (newArea === CustomizableUI.AREA_ADDONS)` → `fire.async()`
- 参照: `CustomizableUI.AREA_ADDONS`, `this.id`

## unregister()
- 位置: L1048-1050
- 役割: 配置の変更の監視を外す。
- 触るとき: onUserSettingsChanged の購読解除が効かない問題を調べるとき。
- 呼び出し先: `CustomizableUI.removeListener()`

## convert()
- 位置: L1051-1053
- 役割: 永続イベントの復元時に、新しい fire を受け取って差し替える。
- 触るとき: onUserSettingsChanged が再起動後に届かない問題を調べるとき。

## getAPI()
- 位置: L1058-1129
- 役割: manifest のバージョンに応じて browserAction か action の名前空間を作り、イベント、getUserSettings、openPopup を加える。
- 触るとき: 拡張から見えるボタン API の名前空間や関数を変えるとき。
- 呼び出し先: `action.api()`
- 参照: `extension.manifestVersion`

## getUserSettings()
- 位置: L1086-1091
- 役割: ウィジェットの配置先が拡張メニュー以外ならツールバーにあると返す。
- 触るとき: getUserSettings の isOnToolbar の判定を変えるとき。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`
- 参照: `CustomizableUI.AREA_ADDONS`, `action.buttonDelegate.id`

## openPopup()
- 位置: async L1092-1126
- 役割: ユーザー操作があるかを確かめ、ウィンドウがフォーカス中かを確かめてから、ポップアップ URL があれば開く。ユーザー操作がなければ openPopupWithoutUserInteraction を付ける。
- 触るとき: openPopup が拒否される条件や、ユーザー操作の要件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `action.getPopupUrl()`, `windowTracker.getTopNormalWindow()`, `windowTracker.getWindow()`
- 条件付き依存: `if (action.getPopupUrl(window.gBrowser.selectedTab, true))` → `action.throwIfOpenPopupIsBlockedByAnyAction()`
- 条件付き依存: `if (action.getPopupUrl(window.gBrowser.selectedTab, true))` → `this.openPopup()`
- 参照: `BrowserActionBase.ERROR_WIN_NOT_FOCUSED`, `Services.focus.activeWindow`, `context.callContextData?.isHandlingUserInput`, `options.windowId`, `options?.windowId`, `window.STATE_MINIMIZED`, `window.gBrowser.selectedTab`, `window.windowState`
- XPCOM: `Services.focus` / `Services.prefs`
