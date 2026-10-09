# browser/components/tabbrowser/content/browser-allTabsMenu.js

source: browser/components/tabbrowser/content/browser-allTabsMenu.js
source-hash: b79e3da63737ace75a2195107f6c9562fa4f35f8
lines: 270

## <module>
- 役割: 「すべてのタブ」パネルの要素管理・初期化・表示を担う gTabsPanel オブジェクトを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## initElements()
- 位置: L30-41
- 役割: テンプレートを展開し、kElements の ID から各要素を取得して保持する(一度だけ)。
- 触るとき: すべてのタブパネルの要素 ID を追加・変更するとき。
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `template.replaceWith()`
- 参照: `template.content`, `this._initializedElements`, `this.kElements`

## hasHiddenTabsExcludingFxView()
- 位置: L43-48
- 役割: Firefox View を除いて非表示のタブがあるかを返す。
- 触るとき: 非表示タブのボタンを出す条件を調べるとき。
- 呼び出し先: `gBrowser.tabs.some()`
- 参照: `FirefoxViewHandler.tab`, `tab.hidden`

## init()
- 位置: L50-210
- 役割: 各タブ一覧パネルを作り、表示時の項目更新、コマンド処理、コンテナ一覧の生成のリスナーを登録する。
- 触るとき: すべてのタブパネルの内容や項目、コマンドの動作を変えるとき。
- 呼び出し先: `ContextualIdentityService.getPublicIdentities()`, `ContextualIdentityService.getPublicIdentities().forEach()`, `FirefoxViewHandler.openTab()`, `Glean.browserUiInteraction.listAllTabsAction.close_all_duplicates.add()`, `Glean.browserUiInteraction.listAllTabsAction.search_tabs.add()`, `PanelUI._ensureShortcutsShown()`, `PanelUI.showSubView()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `containerTabsMenuSeparator.parentNode.insertBefore()`, `document.createDocumentFragment()`, `document.createXULElement()`, `document.getElementById()`, `e.target.addEventListener()`, `element.remove()`, `elements.push()`, `frag.appendChild()`, `gBrowser.getAllDuplicateTabsToClose()`, `gBrowser.removeAllDuplicateTabs()`, `menuitem.classList.add()`, `menuitem.setAttribute()`, `this.allTabsView .querySelector()`, `this.allTabsView .querySelector(".all-tabs-item[selected]") ?.scrollIntoView()`, `this.allTabsView.addEventListener()`, `this.containerTabsView.addEventListener()`, `this.containerTabsView.querySelector()`, `this.hasHiddenTabsExcludingFxView()`, `this.hiddenAudioTabs.hasChildNodes()`, `this.initElements()`, `this.searchTabs()`
- 条件付き依存: `if (hasHiddenAudioTabs)` → `this.allTabsViewTabs.prepend()`
- 条件付き依存: `if (!(hasHiddenAudioTabs))` → `this.allTabsViewTabs.append()`
- 条件付き依存: `if (identity.name)` → `menuitem.setAttribute()`
- 条件付き依存: `if (!(identity.name))` → `document.l10n.setAttributes()`
- 参照: `closeDuplicateTabsItem.hidden`, `document.getElementById("allTabsMenu-containerTabsButton").hidden`, `gBrowser.getAllDuplicateTabsToClose().length`, `hiddenTabsButton.hidden`, `hiddenTabsSeparator.hidden`, `identity.color`, `identity.icon`, `identity.l10nId`, `identity.name`, `identity.userContextId`, `target.documentGlobal`, `target.id`, `this._initialized`, `this.allTabsPanel`, `this.allTabsView`, `this.allTabsViewTabs`, `this.dropIndicator`, `this.groupsPanel`, `this.groupsSubView`, `this.groupsView`, `this.hiddenAudioTabs`, `this.hiddenAudioTabs.hidden`, `this.hiddenAudioTabsPopup`, `this.hiddenTabsPopup`, `this.hiddenTabsView`, `this.hiddenTabsViewTabs`, `this.kElements.containerTabsView`, `this.kElements.groupsSubView`, `this.kElements.hiddenTabsView`, `this.showAllGroupsPanel`
- XPCOM: `Services.prefs`

## filterFn()
- 位置: L60-60
- 役割: 音を出している、またはミュート中のタブだけを通す。
- 触るとき: 非表示タブのうち音声タブを上部に出す条件を変えるとき。
- 参照: `tab.muted`, `tab.soundPlaying`

## filterFn()
- 位置: L66-66
- 役割: 非表示でないタブだけを通す。
- 触るとき: すべてのタブ一覧に載せるタブの条件を変えるとき。
- 参照: `tab.hidden`

## filterFn()
- 位置: L205-205
- 役割: Firefox View 以外のタブを通す。
- 触るとき: 非表示タブ一覧に載せるタブの条件を変えるとき。
- 参照: `FirefoxViewHandler.tab`

## canOpen()
- 位置: L212-215
- 役割: 要素を初期化し、すべてのタブボタンが表示されているかを返す。
- 触るとき: ボタンが見えないときパネルを開けない理由を調べるとき。
- 呼び出し先: `isElementVisible()`, `this.initElements()`
- 参照: `this.allTabsButton`

## showAllTabsPanel()
- 位置: L217-237
- 役割: Enter かスペース以外のキー入力を除き、telemetry を記録してすべてのタブパネルを開く。
- 触るとき: パネルを開く入口や、キー操作と telemetry を変えるとき。
- 呼び出し先: `this.init()`
- 条件付き依存: `if (this.canOpen)` → `Glean.browserUiInteraction.allTabsPanelEntrypoint[entrypoint].add()`
- 条件付き依存: `if (this.canOpen)` → `BrowserUsageTelemetry.recordInteractionEvent()`
- 条件付き依存: `if (this.canOpen)` → `PanelUI.showSubView()`
- 参照: `Glean.browserUiInteraction.allTabsPanelEntrypoint`, `event.key`, `event?.type`, `this.allTabsButton`, `this.canOpen`, `this.kElements.allTabsView`

## hideAllTabsPanel()
- 位置: L239-244
- 役割: すべてのタブパネルを含むポップアップを閉じる。
- 触るとき: 他の操作の後にこのパネルを閉じる処理を調べるとき。
- 呼び出し先: `this.allTabsView?.closest()`
- 条件付き依存: `if (panel)` → `PanelMultiView.hidePopup()`

## showHiddenTabsPanel()
- 位置: L246-262
- 役割: すべてのタブパネルを開いた後に、非表示タブのサブビューを開く。
- 触るとき: 非表示タブ一覧への直接の入口を調べるとき。
- 呼び出し先: `PanelUI.showSubView()`, `this.allTabsView.addEventListener()`, `this.init()`, `this.showAllTabsPanel()`
- 参照: `this.canOpen`, `this.hiddenTabsButton`, `this.kElements.hiddenTabsView`

## searchTabs()
- 位置: L264-268
- 役割: アドレスバーをオープンタブ検索モードで開く。
- 触るとき: パネルからのタブ検索の動作を変えるとき。
- 呼び出し先: `gURLBar.search()`
- 参照: `UrlbarShared.RESTRICT_TOKENS.OPENPAGE`
