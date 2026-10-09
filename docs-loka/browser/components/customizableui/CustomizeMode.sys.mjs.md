# browser/components/customizableui/CustomizeMode.sys.mjs

source: browser/components/customizableui/CustomizeMode.sys.mjs
source-hash: 0226177206cf5a7940a756ba33c3de2e374545fd
lines: 4017

## <module>
- 役割: カスタマイズモード(ツールバー・パレット・オーバーフローの並べ替え UI)を窓ごとに管理する CustomizeMode クラスと、そのドラッグ&ドロップ処理を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyServiceGetter()`

## closeGlobalTab()
- 位置: L62-69
- 役割: カスタマイズモード用のタブを閉じる。窓にタブが 1 つだけならその前に新しいタブを開く。
- 触るとき: カスタマイズを終えた後にタブが残る、または窓が空になるような挙動を調べるときに見る。
- 呼び出し先: `win.gBrowser.removeTab()`
- 条件付き依存: `if (win.gBrowser.browsers.length == 1)` → `win.BrowserCommands.openTab()`
- 参照: `gTab.documentGlobal`, `win.gBrowser.browsers.length`

## onLocationChange()
- 位置: L72-85
- 役割: カスタマイズ用タブが別のページへ遷移したら、タブの登録を解除する。about:blank への遷移は無視する。
- 触るとき: カスタマイズ用タブで別ページを開いたときにモードを終えるかどうかの条件を変えるときに見る。
- 呼び出し先: `unregisterGlobalTab()`
- 参照: `aLocation.spec`, `gTab.linkedBrowser`

## unregisterGlobalTab()
- 位置: L88-97
- 役割: カスタマイズ用タブのイベントと進捗リスナーを外し、customizemode 属性を消して参照を null にする。
- 触るとき: タブを閉じた後もリスナーが残る、または次の入場で古い参照が使われるときに見る。
- 呼び出し先: `gTab.removeAttribute()`, `gTab.removeEventListener()`, `win.gBrowser.removeTabsProgressListener()`, `win.removeEventListener()`
- 参照: `gTab.documentGlobal`

## CustomizeMode.constructor()
- 位置: L104-150
- 役割: 窓の参照と要素を保持し、翻訳監視とカスタマイズ用パネルの準備、ドラッグ系リスナー、タイトルバーとブックマークツールバーの pref 監視を設定する。
- 触るとき: 窓ごとの初期化で追加の DOM や pref 監視が必要になったとき、または起動時にカスタマイズ画面の一部が欠けるときに見る。
- 呼び出し先: `Services.prefs.addObserver()`, `this.#attachEventListeners()`, `this.#canDrawInTitlebar()`, `this.#ensureCustomizationPanels()`, `this.#onTranslations()`, `this.#window.addEventListener()`, `this.$()`
- 条件付き依存: `if (!content)` → `this.#window.MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!content)` → `this.$()`
- 条件付き依存: `if (!content)` → `container.replaceChild()`
- 条件付き依存: `if (!content)` → `this.#window.MozXULElement.parseXULToFragment()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `this.#updateTitlebarCheckbox()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `Services.prefs.addObserver()`
- 条件付き依存: `if (!(this.#canDrawInTitlebar()))` → `this.$()`
- 参照: `aWindow.MutationObserver`, `aWindow.document`, `aWindow.gBrowser`, `container.firstChild.data`, `container.lastChild`, `this.#browser`, `this.#document`, `this.#translationObserver`, `this.#window`, `this.$("customization-titlebar-visibility-checkbox").hidden`, `this.areas`, `this.pongArena`, `this.visiblePalette`
- XPCOM: `Services.prefs`

## CustomizeMode.#handler()
- 位置: L301-303
- 役割: 窓の CustomizationHandler(browser-customization.js 側)を返す。
- 触るとき: 入退場の状態フラグ(isEnteringCustomizeMode など)がどこで管理されているかを確かめるときに見る。
- 参照: `this.#window.CustomizationHandler`

## CustomizeMode.#uninit()
- 位置: L309-314
- 役割: タイトルバーとブックマークツールバーの pref 監視を外す。
- 触るとき: 窓を閉じた後に pref のオブザーバーが残るように見えるときに見る。
- 呼び出し先: `Services.prefs.removeObserver()`, `this.#canDrawInTitlebar()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## CustomizeMode.$()
- 位置: L323-325
- 役割: 窓の文書で id から要素を取得する短縮メソッド。
- 触るとき: カスタマイズ画面の要素参照を追加・変更するときに、対象 id が実際に存在するかを確かめるために見る。
- 呼び出し先: `this.#document.getElementById()`

## CustomizeMode.setTab()
- 位置: L342-373
- 役割: カスタマイズ用の疑似タブを登録し、タブの属性・タイトル・アイコンと閉じる・遷移時のリスナーを設定する。タブが選択中なら enter を呼ぶ。
- 触るとき: カスタマイズ用タブの見た目を変えるとき、またはタブを閉じても入退場が連動しないときに見る。
- 呼び出し先: `gTab.addEventListener()`, `gTab.setAttribute()`, `win.addEventListener()`, `win.gBrowser.addTabsProgressListener()`, `win.gBrowser.setIcon()`, `win.gBrowser.setTabTitle()`
- 条件付き依存: `if (gTab)` → `closeGlobalTab()`
- 条件付き依存: `if (gTab.linkedPanel)` → `gTab.linkedBrowser.stop()`
- 条件付き依存: `if (gTab.selected)` → `win.gCustomizeMode.enter()`
- 参照: `gTab.documentGlobal`, `gTab.linkedPanel`, `gTab.selected`

## CustomizeMode.enter()
- 位置: L388-573
- 役割: カスタマイズモードに入る。ツールバーが隠れている窓や特殊な窓では対象の窓へ回し、タブを用意し、非同期に UI を切り替えてパレットを表示する。
- 触るとき: 入場の前後に処理を挟みたいとき、または入場が途中で止まって入れないときに見る。
- 呼び出し先: `CustomizableUI.addListener()`, `CustomizableUI.dispatchToolboxEvent()`, `CustomizableUI.notifyStartCustomizing()`, `Services.prefs.getBoolPref()`, `Services.prefs.getPrefType()`, `document.addEventListener()`, `document.getElementById()`, `document.getElementById("mainPopupSet").appendChild()`, `document.querySelectorAll()`, `gTab.documentGlobal.focus()`, `lazy.log.error()`, `panelHolder.appendChild()`, `resetButton.setAttribute()`, `this.#document.documentElement.toggleAttribute()`, `this.#populatePalette()`, `this.#setupDownloadAutoHideToggle()`, `this.#setupPaletteDragging()`, `this.#updateDensityMenu()`, `this.#updateEmptyPaletteNotice()`, `this.#updateOverflowPanelArrowOffset()`, `this.#updateResetButton()`, `this.#updateTouchBarButton()`, `this.#updateUndoResetButton()`, `this.#window.document.documentElement.hasAttribute()`, `this.#wrapAllAreaItems()`, `this.#wrapAreaItemsSync()`, `this.$()`, `this.exit()`, `this.visiblePalette.setAttribute()`, `toolbar.toggleAttribute()`, `window.PanelUI.hide()`, `window.PanelUI.overflowFixedList.toggleAttribute()`, `window.gNavToolbox.addEventListener()`, `window.setTimeout()`
- 条件付き依存: `if ( !this.#window.toolbar.visible || this.#window.document.documentElement.hasAttribute("taskbartab") || this.#window.document.documentElement.hasAttribute("min...)` → `lazy.URILoadingHelper.getTargetWindow()`
- 条件付き依存: `if (w)` → `w.gCustomizeMode.enter()`
- 条件付き依存: `if ( !this.#window.toolbar.visible || this.#window.document.documentElement.hasAttribute("taskbartab") || this.#window.document.documentElement.hasAttribute("min...)` → `Services.obs.addObserver()`
- 条件付き依存: `if ( !this.#window.toolbar.visible || this.#window.document.documentElement.hasAttribute("taskbartab") || this.#window.document.documentElement.hasAttribute("min...)` → `this.#window.openTrustedLinkIn()`
- 条件付き依存: `if (this.#handler.isExitingCustomizeMode)` → `lazy.log.debug()`
- 条件付き依存: `if (!gTab)` → `this.setTab()`
- 条件付き依存: `if (!gTab)` → `this.#browser.addTab()`
- 条件付き依存: `if (!gTab)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (!this.#window.gBrowserInit.delayedStartupFinished)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._wantToBeInCustomizeMode)` → `this.exit()`
- 参照: `Ci.nsIPrefBranch.PREF_BOOL`, `CustomizableUI.AREA_TABSTRIP`, `browser.hidden`, `customizer.hidden`, `document.getElementById("nav-bar-overflow-button").disabled`, `gTab.documentGlobal.gBrowser.selectedTab`, `gTab.ownerDocument`, `gTab.selected`, `panelContextMenu.parentNode`, `this.#customizing`, `this.#document`, `this.#handler.isEnteringCustomizeMode`, `this.#handler.isExitingCustomizeMode`, `this.#skipSourceNodeCheck`, `this.#transitioning`, `this.#window`, `this.#window.gBrowserInit.delayedStartupFinished`, `this.#window.toolbar.visible`, `this._previousPanelContextMenuParent`, `this._wantToBeInCustomizeMode`, `this.visiblePalette.clientTop`, `this.visiblePalette.hidden`, `window.PanelUI.menuButton.disabled`, `window.PanelUI.overflowFixedList`
- XPCOM: [`nsIPrefBranch`](../../../netwerk/base/nsINetUtil.idl.md) / `Services.obs` / `Services.prefs` / `Services.scriptSecurityManager`

## obs()
- 位置: L402-409
- 役割: about:newtab を開いた別窓で delayed startup が終わったとき、対象の窓で enter を呼び直す。
- 触るとき: ツールバーが隠れた窓から入場したときに、開いた先で入場が完了しないときに見る。
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.URILoadingHelper.getTargetWindow()`, `w.gCustomizeMode.enter()`
- 参照: `this.#window`
- XPCOM: `Services.obs`

## delayedStartupObserver()
- 位置: L466-474
- 役割: browser-delayed-startup-finished を受け、この窓の通知なら待ちを解決する。
- 触るとき: 起動直後にカスタマイズモードを開くと入場が待ち続けるときに見る。
- 条件付き依存: `if (aSubject == this.#window)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (aSubject == this.#window)` → `resolve()`
- 参照: `this.#window`
- XPCOM: `Services.obs`

## CustomizeMode.exit()
- 位置: L584-693
- 役割: カスタマイズモードを終える。パレットを片付け、ツールバーとメニューを元に戻し、非同期の後始末の後に入り直しの要求があれば enter を呼ぶ。
- 触るとき: 終了時に元に戻すべき状態を増やすときや、終了が途中で止まるときに見る。
- 呼び出し先: `CustomizableUI.dispatchToolboxEvent()`, `CustomizableUI.notifyEndCustomizing()`, `CustomizableUI.removeListener()`, `document.documentElement.removeAttribute()`, `document.getElementById()`, `document.querySelectorAll()`, `document.removeEventListener()`, `lazy.log.error()`, `overflowContainer.appendChild()`, `this.#depopulatePalette()`, `this.#maybeMoveDownloadsButtonToNavBar()`, `this.#teardownDownloadAutoHideToggle()`, `this.#teardownPaletteDragging()`, `this.#togglePong()`, `this.#translationObserver.disconnect()`, `this.#unwrapAllAreaItems()`, `this.$()`, `this._previousPanelContextMenuParent.appendChild()`, `this.areas.clear()`, `toolbar.removeAttribute()`, `window.gNavToolbox.removeEventListener()`
- 条件付き依存: `if (this.#handler.isEnteringCustomizeMode)` → `lazy.log.debug()`
- 条件付き依存: `if (this.resetting)` → `lazy.log.debug()`
- 条件付き依存: `if (this.#browser.selectedTab == gTab)` → `closeGlobalTab()`
- 条件付き依存: `if (this._wantToBeInCustomizeMode)` → `this.enter()`
- 参照: `browser.hidden`, `customizer.hidden`, `document.getElementById( "widget-overflow-mainView" ).firstElementChild`, `document.getElementById("nav-bar-overflow-button").disabled`, `resetButton.disabled`, `this.#browser.selectedTab`, `this.#customizing`, `this.#document`, `this.#handler.isEnteringCustomizeMode`, `this.#handler.isExitingCustomizeMode`, `this.#transitioning`, `this.#window`, `this._lastLightweightTheme`, `this._wantToBeInCustomizeMode`, `this.resetting`, `undoResetButton.hidden`, `window.PanelUI.menuButton.disabled`, `window.PanelUI.overflowFixedList`

## CustomizeMode.#updateOverflowPanelArrowOffset()
- 位置: async L706-730
- 役割: オーバーフローボタンの位置から、パネル矢印の水平オフセットを求めて --panel-arrow-offset に設定する。
- 触るとき: オーバーフローパネルの矢印の位置がずれるとき、または密度変更の後の再計算を見直すときに見る。
- 呼び出し先: `overflowButton.getBoundingClientRect()`, `this.#document.documentElement.getAttribute()`, `this.#window.promiseDocumentFlushed()`, `this.$()`, `this.$("customization-panelWrapper").style.setProperty()`
- 参照: `buttonRect.left`, `buttonRect.right`, `buttonRect.width`, `this.#document`, `this.#window.RTL_UI`, `this.#window.innerWidth`

## CustomizeMode.#getCustomizableChildForNode()
- 位置: L742-772
- 役割: ノードの祖先をたどり、カスタマイズ可能なエリアの直下の子を返す。パレットと既定のオーバーフロー先も対象に含める。
- 触るとき: ドラッグや右クリックで対象がどの子として扱われるかを確かめるとき、または新しいエリアを増やしたときに見る。
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `aNode.ownerDocument.getElementById()`, `areaNode.getAttribute()`, `areas.includes()`, `areas.push()`
- 条件付き依存: `if (customizationTarget && customizationTarget != areaNode)` → `areas.push()`
- 条件付き依存: `if (overflowTarget)` → `areas.push()`
- 参照: `CustomizableUI.areas`, `aNode.parentNode`, `areas.length`, `customizationTarget.id`, `parent.id`

## CustomizeMode.#promiseWidgetAnimationOut()
- 位置: L791-849
- 役割: ツールバーから外れる項目に animate-out クラスを付け、アニメーション終了か customizationending で解決する Promise を返す。モーション低減時などは null を返す。
- 触るとき: ツールバーから項目を外すときの縮小アニメーションを変えるとき、またはアニメーションが終わらず処理が止まるときに見る。
- 呼び出し先: `aNode.getAttribute()`, `aNode.parentNode.id.startsWith()`, `animationNode.addEventListener()`, `animationNode.classList.add()`, `animationNode.documentGlobal.gNavToolbox.addEventListener()`, `this.#window.requestAnimationFrame()`
- 参照: `aNode.hidden`, `aNode.id`, `aNode.parentNode`, `aNode.tagName`, `this.#window.gReduceMotion`

## cleanupCustomizationExit()
- 位置: L808-810
- 役割: カスタマイズが終わったとき、アニメーション待ちを解決する。
- 触るとき: カスタマイズを抜けたときに項目のアニメーション待ちが残るときに見る。
- 呼び出し先: `resolveAnimationPromise()`

## cleanupWidgetAnimationEnd()
- 位置: L812-819
- 役割: animate-out のアニメーションが終わったとき、対象ノードの待ちを解決する。
- 触るとき: 項目を外すアニメーションが終わったのに次の処理へ進まないときに見る。
- 条件付き依存: `if ( e.animationName == "widget-animate-out" && e.target.id == animationNode.id )` → `resolveAnimationPromise()`
- 参照: `animationNode.id`, `e.animationName`, `e.target.id`

## resolveAnimationPromise()
- 位置: L821-831
- 役割: アニメーションの待ちに付けた animationend と customizationending の listener を外し、Promise を解決する。
- 触るとき: アニメーション待ちの後片付けに漏れがあるとき、または待ちの終わり方を変えるときに見る。
- 呼び出し先: `animationNode.removeEventListener()`, `resolve()`

## CustomizeMode.addToToolbar()
- 位置: async L864-905
- 役割: 項目をナビゲーションバーの末尾へ移す。必要ならアニメーションの後に移し、テレメトリを記録し、ダウンロードボタンの自動非表示を解除する。
- 触るとき: コンテキストメニューの「ツールバーに追加」が効かないとき、またはダウンロードボタンの自動非表示が勝手に変わるときに見る。
- 呼び出し先: `CustomizableUI.addWidgetToArea()`, `CustomizableUI.isSpecialWidget()`, `aNode.closest()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `this.#getCustomizableChildForNode()`, `this.#promiseWidgetAnimationOut()`
- 条件付き依存: `if ( CustomizableUI.isSpecialWidget(widgetToAdd) && aNode.closest("#customization-palette") )` → `widgetToAdd.match()`
- 条件付き依存: `if (!this.#customizing)` → `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (aNode.id == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.#customizing)` → `this.#showDownloadsAutoHidePanel()`
- 条件付き依存: `if (animationNode)` → `animationNode.classList.remove()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `aNode.firstElementChild`, `aNode.id`, `aNode.localName`, `this.#customizing`
- XPCOM: `Services.prefs`

## CustomizeMode.addToPanel()
- 位置: async L934-976
- 役割: 項目をオーバーフローパネルへ移す。アニメーションの後に移し、テレメトリを記録し、オーバーフローボタンを一時的に動かす。
- 触るとき: パネルへ移す操作の挙動を変えるとき、またはオーバーフローボタンのアニメーションが残るときに見る。
- 呼び出し先: `CustomizableUI.addWidgetToArea()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `this.#getCustomizableChildForNode()`, `this.#promiseWidgetAnimationOut()`
- 条件付き依存: `if (!this.#customizing)` → `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (aNode.id == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.#customizing)` → `this.#showDownloadsAutoHidePanel()`
- 条件付き依存: `if (animationNode)` → `animationNode.classList.remove()`
- 条件付き依存: `if (!this.#window.gReduceMotion)` → `this.$()`
- 条件付き依存: `if (!this.#window.gReduceMotion)` → `overflowButton.setAttribute()`
- 条件付き依存: `if (!this.#window.gReduceMotion)` → `overflowButton.addEventListener()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `aNode.firstElementChild`, `aNode.id`, `aNode.localName`, `this.#customizing`, `this.#window.gReduceMotion`
- XPCOM: `Services.prefs`

## onAnimationEnd()
- 位置: L968-973
- 役割: オーバーフローボタンの overflow-animation が終わったとき、animate 属性を外し listener を外す。
- 触るとき: オーバーフローボタンが動いた後に animate 属性が残るときに見る。
- 呼び出し先: `event.animationName.startsWith()`
- 条件付き依存: `if (event.animationName.startsWith("overflow-animation"))` → `this.removeEventListener()`
- 条件付き依存: `if (event.animationName.startsWith("overflow-animation"))` → `this.removeAttribute()`

## CustomizeMode.removeFromArea()
- 位置: async L1006-1033
- 役割: 項目をエリアから外してパレットへ送る。必要ならアニメーションの後に外し、テレメトリを記録し、ダウンロードボタンの自動非表示を解除する。
- 触るとき: ツールバーから項目を外す操作(コンテキストメニューなど)の挙動を変えるとき、特定の項目だけ挙動が違うときに見る。
- 呼び出し先: `CustomizableUI.removeWidgetFromArea()`, `lazy.BrowserUsageTelemetry.recordWidgetChange()`, `this.#getCustomizableChildForNode()`, `this.#promiseWidgetAnimationOut()`
- 条件付き依存: `if (!this.#customizing)` → `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (aNode.id == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (this.#customizing)` → `this.#showDownloadsAutoHidePanel()`
- 条件付き依存: `if (animationNode)` → `animationNode.classList.remove()`
- 参照: `aNode.firstElementChild`, `aNode.id`, `aNode.localName`, `this.#customizing`
- XPCOM: `Services.prefs`

## CustomizeMode.#populatePalette()
- 位置: L1041-1072
- 役割: エリアに無いウィジェットを palette 用の wrapper にして visiblePalette に並べ、gNavToolbox.palette を差し替え、コマンドを無効にする。
- 触るとき: カスタマイズに入ったときにパレットの中身が欠けるとき、またはパレットの初期配置を変えるときに見る。
- 呼び出し先: `CustomizableUI.createSpecialWidget()`, `CustomizableUI.getUnusedWidgets()`, `fragment.appendChild()`, `lazy.log.error()`, `this.#document.createDocumentFragment()`, `this.#makePaletteItem()`, `this.#updateCommandsDisabledState()`, `this.visiblePalette.appendChild()`, `this.wrapToolbarItem()`
- 参照: `this.#document`, `this.#stowedPalette`, `this.#window.gNavToolbox.palette`, `this.visiblePalette`

## CustomizeMode.#makePaletteItem()
- 位置: L1082-1098
- 役割: ウィジェットのノードを取り、非表示でなければ palette 用の wrapper で包んで返す。
- 触るとき: パレットに出てこないウィジェットがあるとき、または非表示の判定を変えるときに見る。
- 呼び出し先: `aWidget.forWindow()`, `this.createOrUpdateWrapper()`, `wrapper.appendChild()`
- 条件付き依存: `if (!widgetNode)` → `lazy.log.error()`
- 参照: `aWidget.forWindow(this.#window).node`, `aWidget.id`, `this.#window`, `widgetNode.hidden`

## CustomizeMode.#depopulatePalette()
- 位置: L1106-1132
- 役割: パレット内の項目を unwrap して隠れたパレットへ戻し、特殊項目は取り除き、ツールボックスの palette 参照を元に戻す。
- 触るとき: カスタマイズを抜けた後にパレットの項目が元の場所に戻らないときに見る。
- 呼び出し先: `CustomizableUI.isSpecialWidget()`, `this.#updateCommandsDisabledState()`
- 条件付き依存: `if (CustomizableUI.isSpecialWidget(itemId))` → `this.visiblePalette.removeChild()`
- 条件付き依存: `if (!(CustomizableUI.isSpecialWidget(itemId)))` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (!(CustomizableUI.isSpecialWidget(itemId)))` → `this.#stowedPalette.appendChild()`
- 参照: `paletteChild.firstElementChild.id`, `paletteChild.nextElementSibling`, `this.#stowedPalette`, `this.#window.gNavToolbox.palette`, `this.visiblePalette.firstElementChild`, `this.visiblePalette.hidden`

## CustomizeMode.#updateCommandsDisabledState()
- 位置: L1148-1164
- 役割: id が無い、または enabledCommands に無い command を無効にし、元から無効だったものには wasdisabled を付ける。解除時は逆の処理をする。
- 触るとき: カスタマイズ中に無効にするコマンドを増減するとき、または終了後にコマンドが無効のまま残るときに見る。
- 呼び出し先: `this.#document.querySelectorAll()`, `this.#enabledCommands.has()`
- 条件付き依存: `if (shouldBeDisabled)` → `command.hasAttribute()`
- 条件付き依存: `if (!command.hasAttribute("disabled"))` → `command.setAttribute()`
- 条件付き依存: `if (!(!command.hasAttribute("disabled")))` → `command.setAttribute()`
- 条件付き依存: `if (!(shouldBeDisabled))` → `command.getAttribute()`
- 条件付き依存: `if (command.getAttribute("wasdisabled") != "true")` → `command.removeAttribute()`
- 条件付き依存: `if (!(command.getAttribute("wasdisabled") != "true"))` → `command.removeAttribute()`
- 参照: `command.id`

## CustomizeMode.#isCustomizableItem()
- 位置: L1176-1184
- 役割: ノードの localName が toolbarbutton, toolbaritem, toolbarseparator, toolbarspring, toolbarspacer のいずれかかを判定する。
- 触るとき: カスタマイズ可能な要素の種類を増やすとき、または wrap されない要素があるときに見る。
- 参照: `aNode.localName`

## CustomizeMode.isWrappedToolbarItem()
- 位置: L1195-1197
- 役割: ノードが toolbarpaletteitem(wrapper)かを判定する。
- 触るとき: 同じ項目を二重に wrap していないか、または wrap が漏れていないかを調べるときに見る。
- 参照: `aNode.localName`

## CustomizeMode.#deferredWrapToolbarItem()
- 位置: L1213-1220
- 役割: 次のメインスレッドのタスクで wrapToolbarItem を呼ぶ Promise を返す。
- 触るとき: wrap を非同期にしてタイミングをずらす必要があるとき、またはその遅延の影響を調べるときに見る。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `resolve()`, `this.wrapToolbarItem()`
- XPCOM: `Services.tm`

## CustomizeMode.wrapToolbarItem()
- 位置: L1236-1252
- 役割: カスタマイズ可能な項目を createOrUpdateWrapper で包み、元の位置へ差し替えて wrapper の子にする。
- 触るとき: 項目が移動中で親を失っているときや、wrap 後に DOM の位置がずれるときに見る。
- 呼び出し先: `this.#isCustomizableItem()`, `this.createOrUpdateWrapper()`, `wrapper.appendChild()`
- 条件付き依存: `if (aNode.parentNode)` → `aNode.parentNode.replaceChild()`
- 参照: `aNode.parentNode`

## CustomizeMode.#updateWrapperLabel()
- 位置: L1270-1283
- 役割: wrapper の title と tooltiptext を、項目の label か title から設定する。どちらも無いときは Fluent の翻訳後に付く属性を監視する。
- 触るとき: パレットの項目のツールチップが空または古いときに見る。
- 呼び出し先: `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("label"))` → `aWrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("label"))` → `aNode.getAttribute()`
- 条件付き依存: `if (!(aNode.hasAttribute("label")))` → `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("title"))` → `aWrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("title"))` → `aNode.getAttribute()`
- 条件付き依存: `if (!(aNode.hasAttribute("title")))` → `aNode.hasAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("data-l10n-id") && !aIsUpdate)` → `this.#translationObserver.observe()`
- 参照: `aNode.parentElement`

## CustomizeMode.#onTranslations()
- 位置: L1292-1302
- 役割: 翻訳で後から label や title が付いた項目について、wrapper のラベルを更新する。
- 触るとき: 翻訳後にパレットのツールチップが更新されないときに見る。
- 呼び出し先: `mut.target.hasAttribute()`, `target.hasAttribute()`
- 条件付き依存: `if ( target.parentElement?.localName == "toolbarpaletteitem" && (target.hasAttribute("label") || mut.target.hasAttribute("title")) )` → `this.#updateWrapperLabel()`
- 参照: `target.parentElement?.localName`

## CustomizeMode.createOrUpdateWrapper()
- 位置: L1321-1414
- 役割: toolbarpaletteitem を作るか更新し、command・observes・checked・id・flex・removable・コンテキストメニューとマウスリスナーを付け替える。
- 触るとき: パレット表示で項目の属性が消える・残るといった問題を調べるとき、または wrapper に付ける属性を増やすときに見る。
- 呼び出し先: `CustomizableUI.isSpecialWidget()`, `CustomizableUI.isWidgetRemovable()`, `aNode.getAttribute()`, `aNode.hasAttribute()`, `this.#updateWrapperLabel()`, `wrapper.setAttribute()`
- 条件付き依存: `if ( aIsUpdate && aNode.parentNode && aNode.parentNode.localName == "toolbarpaletteitem" )` → `wrapper.getAttribute()`
- 条件付き依存: `if (!( aIsUpdate && aNode.parentNode && aNode.parentNode.localName == "toolbarpaletteitem" ))` → `this.#document.createXULElement()`
- 条件付き依存: `if (!( aIsUpdate && aNode.parentNode && aNode.parentNode.localName == "toolbarpaletteitem" ))` → `wrapper.setAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("command") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `wrapper.setAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("command") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.getAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("command") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.removeAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("observes") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `wrapper.setAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("observes") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.getAttribute()`
- 条件付き依存: `if ( aNode.hasAttribute("observes") && aNode.getAttribute(kKeepBroadcastAttributes) != "true" )` → `aNode.removeAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("checked"))` → `wrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("checked"))` → `aNode.removeAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("id"))` → `wrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("id"))` → `aNode.getAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("flex"))` → `wrapper.setAttribute()`
- 条件付き依存: `if (aNode.hasAttribute("flex"))` → `aNode.getAttribute()`
- 条件付き依存: `if (!(aNode.getAttribute("context")))` → `aNode.getAttribute()`
- 条件付き依存: `if (aPlace != "toolbar")` → `wrapper.setAttribute()`
- 条件付き依存: `if (currentContextMenu && currentContextMenu != contextMenuForPlace)` → `aNode.setAttribute()`
- 条件付き依存: `if (currentContextMenu && currentContextMenu != contextMenuForPlace)` → `aNode.removeAttribute()`
- 条件付き依存: `if (currentContextMenu == contextMenuForPlace)` → `aNode.removeAttribute()`
- 条件付き依存: `if (!aIsUpdate)` → `wrapper.addEventListener()`
- 条件付き依存: `if (CustomizableUI.isSpecialWidget(aNode.id))` → `wrapper.setAttribute()`
- 条件付き依存: `if (CustomizableUI.isSpecialWidget(aNode.id))` → `lazy.gWidgetsBundle.GetStringFromName()`
- 参照: `aNode.id`, `aNode.nodeName`, `aNode.parentNode`, `aNode.parentNode.localName`

## CustomizeMode.#deferredUnwrapToolbarItem()
- 位置: L1426-1438
- 役割: 次のメインスレッドのタスクで unwrapToolbarItem を呼ぶ Promise を返す。例外はログに出し、結果は null になる。
- 触るとき: unwrap で例外が起きたときに、どこで握りつぶされるかを確かめるときに見る。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `console.error()`, `resolve()`, `this.unwrapToolbarItem()`
- XPCOM: `Services.tm`

## CustomizeMode.unwrapToolbarItem()
- 位置: L1451-1505
- 役割: wrapper の属性(observes, checked, command, context など)を中身へ戻し、中身を wrapper の位置へ差し替える。
- 触るとき: カスタマイズを抜けた後に属性が元に戻らないとき、または unwrap の処理を変えるときに見る。
- 呼び出し先: `aWrapper.getAttribute()`, `aWrapper.hasAttribute()`, `aWrapper.removeEventListener()`, `toolbarItem.getAttribute()`
- 条件付き依存: `if (!toolbarItem)` → `lazy.log.error()`
- 条件付き依存: `if (!toolbarItem)` → `aWrapper.remove()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemobserves"))` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemobserves"))` → `aWrapper.getAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `aWrapper.getAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `this.$()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `toolbarItem.toggleAttribute()`
- 条件付き依存: `if (aWrapper.hasAttribute("itemcommand"))` → `command?.hasAttribute()`
- 条件付き依存: `if (wrappedContext)` → `toolbarItem.getAttribute()`
- 条件付き依存: `if (wrappedContext)` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (wrappedContext)` → `toolbarItem.removeAttribute()`
- 条件付き依存: `if (place == "panel")` → `toolbarItem.setAttribute()`
- 条件付き依存: `if (aWrapper.parentNode)` → `aWrapper.parentNode.replaceChild()`
- 参照: `aWrapper.firstElementChild`, `aWrapper.id`, `aWrapper.nodeName`, `aWrapper.parentNode`, `aWrapper.tagName`, `toolbarItem.checked`

## CustomizeMode.#wrapAreaItems()
- 位置: async L1521-1541
- 役割: エリアの customize target を取得し、ドラッグ系リスナーを付けてから直下の項目を非同期に wrap し、areas へ登録する。
- 触るとき: カスタマイズに入ったときにエリアの項目が wrap されないときに見る。
- 呼び出し先: `CustomizableUI.getCustomizeTargetForArea()`, `this.#addCustomizeTargetDragAndDropHandlers()`, `this.#isCustomizableItem()`, `this.areas.add()`, `this.areas.has()`, `this.isWrappedToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `this.#deferredWrapToolbarItem( child, CustomizableUI.getPlaceForItem(child) ).catch()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `this.#deferredWrapToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `CustomizableUI.getPlaceForItem()`
- 参照: `lazy.log.error`, `target.children`, `this.#window`

## CustomizeMode.#wrapAreaItemsSync()
- 位置: L1555-1577
- 役割: #wrapAreaItems の同期版。直下の項目をその場で wrap して areas へ登録する。
- 触るとき: 入場時にタブストリップの項目を同期的に wrap する理由を調べるとき、または非同期化の影響を確かめるときに見る。
- 呼び出し先: `CustomizableUI.getCustomizeTargetForArea()`, `lazy.log.error()`, `this.#addCustomizeTargetDragAndDropHandlers()`, `this.#isCustomizableItem()`, `this.areas.add()`, `this.areas.has()`, `this.isWrappedToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `this.wrapToolbarItem()`
- 条件付き依存: `if ( this.#isCustomizableItem(child) && !this.isWrappedToolbarItem(child) )` → `CustomizableUI.getPlaceForItem()`
- 参照: `ex.stack`, `target.children`, `this.#window`

## CustomizeMode.#wrapAllAreaItems()
- 位置: async L1587-1591
- 役割: CustomizableUI の全エリアについて #wrapAreaItems を順に待つ。
- 触るとき: 入場時やリセット時に、いずれかのエリアが wrap されないときに見る。
- 呼び出し先: `this.#wrapAreaItems()`
- 参照: `CustomizableUI.areas`

## CustomizeMode.#addCustomizeTargetDragAndDropHandlers()
- 位置: L1601-1611
- 役割: customize target に dragstart, dragover, dragleave, drop, dragend を捕捉フェーズで登録する。オーバーフローパネルは customization-panelHolder に付ける。
- 触るとき: 特定のエリアでドラッグが効かないときに、どのノードにリスナーが付いているかを確かめるときに見る。
- 呼び出し先: `aTarget.addEventListener()`
- 条件付き依存: `if (aTarget.id == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `this.$()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `aTarget.id`

## CustomizeMode.#wrapItemsInArea()
- 位置: L1620-1626
- 役割: customize target の直下にあるカスタマイズ可能な項目を、同期で全て wrap する。
- 触るとき: 新しく登録されたエリアの項目が wrap されないときに見る。
- 呼び出し先: `this.#isCustomizableItem()`
- 条件付き依存: `if (this.#isCustomizableItem(child))` → `this.wrapToolbarItem()`
- 条件付き依存: `if (this.#isCustomizableItem(child))` → `CustomizableUI.getPlaceForItem()`
- 参照: `target.children`

## CustomizeMode.#removeCustomizeTargetDragAndDropHandlers()
- 位置: L1635-1646
- 役割: #addCustomizeTargetDragAndDropHandlers で付けた捕捉フェーズのドラッグ系リスナーを外す。
- 触るとき: エリアを外した後もドラッグ処理が走り続けるときに見る。
- 呼び出し先: `aTarget.removeEventListener()`
- 条件付き依存: `if (aTarget.id == CustomizableUI.AREA_FIXED_OVERFLOW_PANEL)` → `this.$()`
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `aTarget.id`

## CustomizeMode.#unwrapItemsInArea()
- 位置: L1656-1662
- 役割: customize target の直下にある wrapper を同期で unwrap する。
- 触るとき: エリアの登録解除時に wrapper が残るときに見る。
- 呼び出し先: `this.isWrappedToolbarItem()`
- 条件付き依存: `if (this.isWrappedToolbarItem(toolbarItem))` → `this.unwrapToolbarItem()`
- 参照: `target.children`

## CustomizeMode.#unwrapAllAreaItems()
- 位置: L1673-1685
- 役割: 登録済みの全エリアで wrapper を unwrap し、ドラッグのリスナーを外して areas を空にする。
- 触るとき: カスタマイズを抜けるときやリセットの前に、全エリアを元に戻す処理を変えるときに見る。
- 呼び出し先: `this.#removeCustomizeTargetDragAndDropHandlers()`, `this.areas.clear()`, `this.isWrappedToolbarItem()`
- 条件付き依存: `if (this.isWrappedToolbarItem(toolbarItem))` → `this.#deferredUnwrapToolbarItem()`
- 参照: `lazy.log.error`, `target.children`, `this.areas`

## CustomizeMode.reset()
- 位置: L1694-1717
- 役割: パレットを外し、全エリアを unwrap してから CustomizableUI.reset で既定に戻し、再 wrap してパレットを組み直す。
- 触るとき: 既定に戻した後に項目が消えたり重複したりするとき、またはリセットの後始末を変えるときに見る。
- 呼び出し先: `CustomizableUI.reset()`, `this.#depopulatePalette()`, `this.#populatePalette()`, `this.#unwrapAllAreaItems()`, `this.#updateEmptyPaletteNotice()`, `this.#updateResetButton()`, `this.#updateUndoResetButton()`, `this.#wrapAllAreaItems()`, `this.$()`
- 条件付き依存: `if (!this._wantToBeInCustomizeMode)` → `this.exit()`
- 参照: `btn.disabled`, `lazy.log.error`, `this.#moveDownloadsButtonToNavBar`, `this._wantToBeInCustomizeMode`, `this.resetting`

## CustomizeMode.undoReset()
- 位置: L1725-1743
- 役割: 直前のリセットを CustomizableUI.undoReset で取り消し、reset と同じ手順で項目を組み直す。
- 触るとき: 元に戻す操作の結果が画面に反映されないときに見る。
- 呼び出し先: `CustomizableUI.undoReset()`, `this.#depopulatePalette()`, `this.#populatePalette()`, `this.#unwrapAllAreaItems()`, `this.#updateEmptyPaletteNotice()`, `this.#updateResetButton()`, `this.#updateUndoResetButton()`, `this.#wrapAllAreaItems()`
- 参照: `lazy.log.error`, `this.#moveDownloadsButtonToNavBar`, `this.resetting`

## CustomizeMode.#onToolbarVisibilityChange()
- 位置: L1752-1759
- 役割: toolbarvisibilitychange を受けて、カスタマイズ可能なツールバーの customizing 属性を付け外しし、UI 変更の処理を呼ぶ。
- 触るとき: ツールバーの表示切り替えの後に customizing の表示が残るときに見る。
- 呼び出し先: `this.#onUIChange()`, `toolbar.getAttribute()`, `toolbar.toggleAttribute()`
- 参照: `aEvent.detail.visible`, `aEvent.target`

## CustomizeMode.onWidgetMoved()
- 位置: L1764-1766
- 役割: CustomizableUI からの移動通知を #onUIChange に渡す。
- 触るとき: ウィジェットを動かした後にリセットボタンなどが更新されないときに見る。
- 呼び出し先: `this.#onUIChange()`

## CustomizeMode.onWidgetAdded()
- 位置: L1771-1773
- 役割: CustomizableUI からの追加通知を #onUIChange に渡す。
- 触るとき: ウィジェットを追加した後の UI 更新を変えるときに見る。
- 呼び出し先: `this.#onUIChange()`

## CustomizeMode.onWidgetRemoved()
- 位置: L1779-1781
- 役割: CustomizableUI からの削除通知を #onUIChange に渡す。
- 触るとき: ウィジェットを削除した後にリセットボタンや空パレットの表示が古いときに見る。
- 呼び出し先: `this.#onUIChange()`

## CustomizeMode.onWidgetBeforeDOMChange()
- 位置: L1795-1807
- 役割: DOM が変わる前に、対象ノードの親と挿入先の親の wrapper を外す。リセット中やこの窓以外への変更では何もしない。
- 触るとき: ウィジェットを移動・追加するときに wrapper の状態が崩れるとき、または DOM 変更前の処理を見直すときに見る。
- 条件付き依存: `if (aNodeToChange.parentNode)` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (aSecondaryNode)` → `this.unwrapToolbarItem()`
- 参照: `aContainer.documentGlobal`, `aNodeToChange.parentNode`, `aSecondaryNode.parentNode`, `this.#window`, `this.resetting`

## CustomizeMode.onWidgetAfterDOMChange()
- 位置: L1821-1846
- 役割: DOM 変更の後、ノードが残っていれば再び wrap する。消えていて API 提供のウィジェットなら、パレットへ新しい項目として追加する。
- 触るとき: API 提供のウィジェットを削除したときにパレットへ戻るかを確かめるとき、または再 wrap の条件を変えるときに見る。
- 条件付き依存: `if (aNodeToChange.parentNode)` → `CustomizableUI.getPlaceForItem()`
- 条件付き依存: `if (aNodeToChange.parentNode)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (aSecondaryNode)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (!(aNodeToChange.parentNode))` → `CustomizableUI.getWidget()`
- 条件付き依存: `if (widget.provider == CustomizableUI.PROVIDER_API)` → `this.#makePaletteItem()`
- 条件付き依存: `if (widget.provider == CustomizableUI.PROVIDER_API)` → `this.visiblePalette.appendChild()`
- 参照: `CustomizableUI.PROVIDER_API`, `aContainer.documentGlobal`, `aNodeToChange.id`, `aNodeToChange.parentNode`, `this.#window`, `this.resetting`, `widget.provider`

## CustomizeMode.onWidgetDestroyed()
- 位置: L1855-1860
- 役割: 破棄された API ウィジェットの wrapper を DOM から削除する。
- 触るとき: API で作ったウィジェットを破棄した後にパレットへ残骸が出るときに見る。
- 呼び出し先: `this.$()`
- 条件付き依存: `if (wrapper)` → `wrapper.remove()`

## CustomizeMode.onWidgetAfterCreation()
- 位置: L1875-1887
- 役割: パレットへ行くウィジェットが作られたとき、窓にノードがあれば palette 用に wrap し、無ければ wrapper を作ってパレットへ追加する。
- 触るとき: API ウィジェットを作った直後にパレットへ出ないときに見る。
- 条件付き依存: `if (!aArea)` → `this.$()`
- 条件付き依存: `if (widgetNode)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (!(widgetNode))` → `CustomizableUI.getWidget()`
- 条件付き依存: `if (!(widgetNode))` → `this.visiblePalette.appendChild()`
- 条件付き依存: `if (!(widgetNode))` → `this.#makePaletteItem()`

## CustomizeMode.onAreaNodeRegistered()
- 位置: L1898-1904
- 役割: この窓の文書にエリアが登録されたとき、項目を wrap し、ドラッグ系リスナーを付けて areas へ加える。
- 触るとき: API で新しいエリアを登録したときに、カスタマイズ中の並べ替えが効かないときに見る。
- 条件付き依存: `if (aContainer.ownerDocument == this.#document)` → `this.#wrapItemsInArea()`
- 条件付き依存: `if (aContainer.ownerDocument == this.#document)` → `this.#addCustomizeTargetDragAndDropHandlers()`
- 条件付き依存: `if (aContainer.ownerDocument == this.#document)` → `this.areas.add()`
- 参照: `aContainer.ownerDocument`, `this.#document`

## CustomizeMode.onAreaNodeUnregistered()
- 位置: L1918-1927
- 役割: この窓のエリアの登録が解除されたとき、項目を unwrap し、ドラッグ系リスナーを外して areas から除く。
- 触るとき: エリアを外した後に wrapper やドラッグの残骸が残るときに見る。
- 条件付き依存: `if ( aContainer.ownerDocument == this.#document && aReason == CustomizableUI.REASON_AREA_UNREGISTERED )` → `this.#unwrapItemsInArea()`
- 条件付き依存: `if ( aContainer.ownerDocument == this.#document && aReason == CustomizableUI.REASON_AREA_UNREGISTERED )` → `this.#removeCustomizeTargetDragAndDropHandlers()`
- 条件付き依存: `if ( aContainer.ownerDocument == this.#document && aReason == CustomizableUI.REASON_AREA_UNREGISTERED )` → `this.areas.delete()`
- 参照: `CustomizableUI.REASON_AREA_UNREGISTERED`, `aContainer.ownerDocument`, `this.#document`

## CustomizeMode.#openUIDensityPreferences()
- 位置: L1932-1934
- 役割: about:preferences の外観にあるウィンドウ密度の節を開く。
- 触るとき: 密度設定へのリンク先を変えるときに見る。
- 呼び出し先: `this.#window.openPreferences()`

## CustomizeMode.#updateDensityMenu()
- 位置: L1942-1966
- 役割: Nova が有効なら密度ボタンを隠して設定へのリンクを出す。無効なら、コンパクトモードの表示 pref に応じて密度ボタンを出し分ける。
- 触るとき: 密度の表示条件を変えるとき、特にコンパクトモードの表示規則を見直すときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `button.querySelector()`, `gUIDensity.getCurrentDensity()`, `this.#document.getElementById()`
- 条件付き依存: `if (gUIDensity.getCurrentDensity().mode == gUIDensity.MODE_COMPACT)` → `Services.prefs.setBoolPref()`
- 参照: `button.hidden`, `gUIDensity.MODE_COMPACT`, `gUIDensity.getCurrentDensity().mode`, `link.hidden`, `this.#window.gUIDensity`, `this.#window.gUIDensity.novaEnabled`
- XPCOM: `Services.prefs`

## CustomizeMode.#openAddonsManagerThemes()
- 位置: L1971-1973
- 役割: about:addons をテーマの一覧で開く。
- 触るとき: テーマ管理画面へのリンク先を変えるときに見る。
- 呼び出し先: `this.#window.BrowserAddonUI.openAddonsMgr()`

## CustomizeMode.#previewUIDensity()
- 位置: L1985-1988
- 役割: 指定された密度を一時的に適用し、オーバーフロー矢印の位置を更新する。
- 触るとき: 密度メニューにホバーしたときのプレビューを変えるとき、またはプレビューの後に位置がずれるときに見る。
- 呼び出し先: `this.#updateOverflowPanelArrowOffset()`, `this.#window.gUIDensity.update()`

## CustomizeMode.#resetUIDensity()
- 位置: L1994-1997
- 役割: プレビューを終えたとき、現在設定されている密度へ戻し、矢印の位置を更新する。
- 触るとき: 密度メニューから離れた後に元の密度へ戻らないときに見る。
- 呼び出し先: `this.#updateOverflowPanelArrowOffset()`, `this.#window.gUIDensity.update()`

## CustomizeMode.setUIDensity()
- 位置: L2006-2016
- 役割: uiDensity の pref を設定し、変更を通知して矢印の位置を更新し、密度メニューを閉じる。
- 触るとき: 密度を選んだときの保存処理を変えるとき、または選んだ密度が反映されないときに見る。
- 呼び出し先: `Services.prefs.setIntPref()`, `panel.hidePopup()`, `this.#onUIChange()`, `this.#updateOverflowPanelArrowOffset()`, `win.document.getElementById()`
- 参照: `gUIDensity.uiDensityPref`, `this.#window`, `win.gUIDensity`
- XPCOM: `Services.prefs`

## CustomizeMode.#onUIDensityMenuShowing()
- 位置: L2022-2098
- 役割: 密度メニューの各項目を現在の設定に合わせて表示し、現在の密度に aria-checked と active を付ける。Windows ではタブレットモードの自動切替の項目も更新する。
- 触るとき: 密度メニューで現在の選択が正しく示されないときや、Windows 限定の項目を変えるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `doc.getElementById()`, `gUIDensity.getCurrentDensity()`
- 条件付き依存: `if (Services.prefs.getBoolPref(kCompactModeShowPref))` → `items.push()`
- 条件付き依存: `if (touchItem)` → `items.push()`
- 条件付き依存: `if (item.mode == currentDensity.mode)` → `item.setAttribute()`
- 条件付き依存: `if (!(item.mode == currentDensity.mode))` → `item.removeAttribute()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `doc.getElementById()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `spacer.removeAttribute()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `checkbox.removeAttribute()`
- 条件付き依存: `if (currentDensity.overridden)` → `Services.strings.createBundle()`
- 条件付き依存: `if (currentDensity.overridden)` → `touchItem.setAttribute()`
- 条件付き依存: `if (currentDensity.overridden)` → `sb.GetStringFromName()`
- 条件付き依存: `if (!(currentDensity.overridden))` → `touchItem.removeAttribute()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (autoTouchMode)` → `checkbox.setAttribute()`
- 条件付き依存: `if (!(autoTouchMode))` → `checkbox.removeAttribute()`
- 参照: `AppConstants.platform`, `compactItem.hidden`, `compactItem.mode`, `currentDensity.mode`, `currentDensity.overridden`, `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_NORMAL`, `gUIDensity.MODE_TOUCH`, `item.mode`, `normalItem.mode`, `this.#window`, `touchItem.mode`, `win.document`, `win.gUIDensity`, `win.gUIDensity.autoTouchModePref`
- XPCOM: `Services.prefs` / `Services.strings`

## CustomizeMode.#updateAutoTouchMode()
- 位置: L2108-2114
- 役割: タブレットモードの自動切替の pref を設定し、密度メニューを描き直して UI の変更を通知する。
- 触るとき: 自動切替のチェックを切り替えた後に密度メニューが古いままのときに見る。
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.#onUIChange()`, `this.#onUIDensityMenuShowing()`
- XPCOM: `Services.prefs`

## CustomizeMode.#onUIChange()
- 位置: L2120-2127
- 役割: リセット関連のボタンと空パレット表示を更新し、customizationchange を送る。リセット中はボタンと表示の更新を省く。
- 触るとき: カスタマイズ中の変更でボタンの状態が追従しないとき、またはリセット中の表示を変えるときに見る。
- 呼び出し先: `CustomizableUI.dispatchToolboxEvent()`
- 条件付き依存: `if (!this.resetting)` → `this.#updateResetButton()`
- 条件付き依存: `if (!this.resetting)` → `this.#updateUndoResetButton()`
- 条件付き依存: `if (!this.resetting)` → `this.#updateEmptyPaletteNotice()`
- 参照: `this.resetting`

## CustomizeMode.#updateEmptyPaletteNotice()
- 位置: L2134-2148
- 役割: パレットに伸縮スペースしか無いとき whimsy ボタンを表示し、それ以外では pong を止めてボタンを隠す。
- 触るとき: パレットを空にしたときのヒント表示や隠しゲームの出し方を変えるときに見る。
- 呼び出し先: `paletteItems[0].id.includes()`, `this.$()`, `this.visiblePalette.getElementsByTagName()`
- 条件付き依存: `if (!( paletteItems.length == 1 && paletteItems[0].id.includes("wrapper-customizableui-special-spring") ))` → `this.#togglePong()`
- 参照: `paletteItems.length`, `whimsyButton.hidden`

## CustomizeMode.#updateResetButton()
- 位置: L2154-2157
- 役割: 既定の状態なら、既定に戻すボタンを無効にする。
- 触るとき: カスタマイズを変えたのに既定に戻すボタンが押せないとき、または既定の判定を変えるときに見る。
- 呼び出し先: `this.$()`
- 参照: `CustomizableUI.inDefaultState`, `btn.disabled`

## CustomizeMode.#updateUndoResetButton()
- 位置: L2163-2166
- 役割: 直前のリセットを取り消せるときだけ、取り消しボタンを表示する。
- 触るとき: リセット後に取り消しボタンの表示が正しく切り替わらないときに見る。
- 呼び出し先: `this.$()`
- 参照: `CustomizableUI.canUndoReset`, `undoResetButton.hidden`

## CustomizeMode.#updateTouchBarButton()
- 位置: L2172-2182
- 役割: macOS で Touch Bar が使えるときだけ、Touch Bar の設定ボタンとスペーサーを表示する。
- 触るとき: Touch Bar の設定ボタンの表示条件を変えるとき、または macOS 以外での表示を確かめるときに見る。
- 呼び出し先: `lazy.gTouchBarUpdater.isTouchBarInitialized()`, `this.$()`
- 参照: `AppConstants.platform`, `touchBarButton.hidden`, `touchBarSpacer.hidden`

## CustomizeMode.handleEvent()
- 位置: L2192-2227
- 役割: カスタマイズ中のイベントを種類ごとに対応する処理へ振り分ける。ドラッグ系、マウス、Escape での終了、unload での後始末を扱う。
- 触るとき: カスタマイズ中に新しいイベントへ反応させたいとき、またはイベントが届かないときに見る。
- 呼び出し先: `this.#onDragDrop()`, `this.#onDragEnd()`, `this.#onDragLeave()`, `this.#onDragOver()`, `this.#onDragStart()`, `this.#onMouseDown()`, `this.#onMouseUp()`, `this.#onToolbarVisibilityChange()`, `this.#uninit()`
- 条件付き依存: `if (aEvent.keyCode == aEvent.DOM_VK_ESCAPE)` → `this.exit()`
- 参照: `aEvent.DOM_VK_ESCAPE`, `aEvent.keyCode`, `aEvent.type`

## CustomizeMode.#setupPaletteDragging()
- 位置: L2234-2260
- 役割: パレットと内容コンテナにドラッグ系のリスナーを付け、パレット上の dragover と drop をパレット向けの処理へ渡す。
- 触るとき: パレットの周辺でもドラッグを受けさせたいとき、または他のドロップ先と競合するときに見る。
- 呼び出し先: `contentContainer.addEventListener()`, `this.#addCustomizeTargetDragAndDropHandlers()`, `this.$()`
- 参照: `this.paletteDragHandler`, `this.visiblePalette`

## this.paletteDragHandler()
- 位置: L2237-2252
- 役割: dragover と drop を、パレット内部や固定パネルの外のものに限ってパレット向けの処理へ渡す。
- 触るとき: パレット周辺でのドロップ判定がずれるとき、またはパネル領域を除外する条件を変えるときに見る。
- 呼び出し先: `this.#isUnwantedDragDrop()`, `this.$()`, `this.$("customization-panelHolder").contains()`, `this.visiblePalette.contains()`
- 条件付き依存: `if (aEvent.type == "dragover")` → `this.#onDragOver()`
- 条件付き依存: `if (!(aEvent.type == "dragover"))` → `this.#onDragDrop()`
- 参照: `aEvent.originalTarget`, `aEvent.type`, `this.visiblePalette`

## CustomizeMode.#teardownPaletteDragging()
- 位置: L2266-2278
- 役割: ドラッグ位置管理を止め、パレットと内容コンテナのドラッグ系リスナーを外し、paletteDragHandler を消す。
- 触るとき: カスタマイズを抜けた後にパレットのドラッグが残るときや、ハンドラを作り直す順序を確かめるときに見る。
- 呼び出し先: `contentContainer.removeEventListener()`, `lazy.DragPositionManager.stop()`, `this.#removeCustomizeTargetDragAndDropHandlers()`, `this.$()`
- 参照: `this.paletteDragHandler`, `this.visiblePalette`

## CustomizeMode.observe()
- 位置: L2289-2299
- 役割: pref の変化を受けて、リセットボタン、取り消しボタン、タイトルバーのチェックを更新する。
- 触るとき: pref を変えた後にボタンやチェックボックスが古いままのときに見る。
- 呼び出し先: `this.#canDrawInTitlebar()`, `this.#updateResetButton()`, `this.#updateUndoResetButton()`
- 条件付き依存: `if (this.#canDrawInTitlebar())` → `this.#updateTitlebarCheckbox()`

## CustomizeMode.#canDrawInTitlebar()
- 位置: L2307-2309
- 役割: CustomTitlebar がこの環境でタイトルバーへの描画に対応しているかを返す。
- 触るとき: タイトルバー描画の対応条件を変えるとき、またはチェックボックスの表示が環境によって変わるか確かめるときに見る。
- 参照: `this.#window.CustomTitlebar.systemSupported`

## CustomizeMode.#ensureCustomizationPanels()
- 位置: L2317-2323
- 役割: カスタマイズ用テンプレートの中身を実際の DOM へ差し替え、パネルを使える状態にする。
- 触るとき: カスタマイズ用パネルのテンプレート名や構造を変えるときに見る。
- 呼び出し先: `template.replaceWith()`, `this.$()`, `wrapper.replaceWith()`
- 参照: `template.content`, `wrapper.content`

## CustomizeMode.#attachEventListeners()
- 位置: L2329-2453
- 役割: カスタマイズ画面の command と popupshowing、密度メニューの hover と focus、各リンク、パレットのコンテキストメニュー、ダウンロード自動非表示パネルのイベントを登録する。
- 触るとき: カスタマイズ画面に新しいボタンを配線するとき、またはボタンを押しても動作しないときに見る。
- 呼び出し先: `autohidePanel.addEventListener()`, `container.addEventListener()`, `densityMenu.addEventListener()`, `event.target.hidePopup()`, `this.#customizeTouchBar()`, `this.#document.getElementById()`, `this.#onDownloadsAutoHideChange()`, `this.#onPaletteContextMenuShowing()`, `this.#onUIDensityMenuShowing()`, `this.#openAddonsManagerThemes()`, `this.#openUIDensityPreferences()`, `this.#togglePong()`, `this.#toggleTitlebar()`, `this.#updateAutoTouchMode()`, `this.#window.ToolbarContextMenu.onViewToolbarsPopupShowing()`, `this.#window.clearTimeout()`, `this.#window.setTimeout()`, `this.$()`, `this.$("customization-lwtheme-link").addEventListener()`, `this.$("customization-uidensity-link").addEventListener()`, `this.$(kDownloadAutohideCheckboxId).addEventListener()`, `this.$(kPaletteItemContextMenu).addEventListener()`, `this.addToPanel()`, `this.addToToolbar()`, `this.exit()`, `this.reset()`, `this.setUIDensity()`, `this.undoReset()`
- 参照: `event.target.checked`, `event.target.id`, `event.target.mode`, `event.target.parentNode.triggerNode`, `this._downloadPanelAutoHideTimeout`

## updateDensity()
- 位置: L2376-2383
- 役割: 密度メニューの項目にフォーカスかホバーが来たとき、その密度をプレビューする。
- 触るとき: プレビューの対象項目を増やすとき、または対象外の項目で反応してしまうときに見る。
- 呼び出し先: `this.#previewUIDensity()`
- 参照: `event.target.id`, `event.target.mode`

## resetDensity()
- 位置: L2390-2397
- 役割: 密度メニューの項目からフォーカスかホバーが外れたとき、プレビューを元に戻す。
- 触るとき: プレビュー後に密度が元へ戻らないときに見る。
- 呼び出し先: `this.#resetUIDensity()`
- 参照: `event.target.id`

## CustomizeMode.#updateTitlebarCheckbox()
- 位置: L2460-2471
- 役割: タイトルバーを描画しているかに応じて、表示切替チェックボックスの checked 属性を付け外しする。
- 触るとき: タイトルバーの表示切替の初期状態がずれるときに見る。
- 呼び出し先: `this.$()`
- 条件付き依存: `if (drawInTitlebar)` → `checkbox.removeAttribute()`
- 条件付き依存: `if (!(drawInTitlebar))` → `checkbox.setAttribute()`
- 参照: `Services.appinfo.drawInTitlebar`
- XPCOM: `Services.appinfo`

## CustomizeMode.#toggleTitlebar()
- 位置: L2480-2483
- 役割: チェックボックスの値を、タイトルバー描画の pref(browser.tabs.inTitlebar)に反転して保存する。
- 触るとき: タイトルバー表示切替の保存先や符号を変えるときに見る。
- 呼び出し先: `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## CustomizeMode.#getBoundsWithoutFlushing()
- 位置: L2494-2496
- 役割: windowUtils.getBoundsWithoutFlushing で、レイアウトを確定させずに要素の矩形を取得する。
- 触るとき: ドラッグ中に矩形を取るとき、レイアウトを強制していないか確かめる必要があるときに見る。
- 呼び出し先: `this.#window.windowUtils.getBoundsWithoutFlushing()`

## CustomizeMode.#onDragStart()
- 位置: L2505-2584
- 役割: ドラッグ開始時に、項目を包む wrapper を探して転送データを設定し、掴んだ位置を記録する。移動後に元の項目を隠す準備も行う。
- 触るとき: ドラッグの開始時に転送データや掴み位置がずれるとき、または開始直後の見た目を変えるときに見る。
- 呼び出し先: `CustomizableUI.getPlaceForItem()`, `__dumpDragData()`, `draggedItem.closest()`, `dt.mozSetDataAt()`, `this.#getBoundsWithoutFlushing()`, `this.#window.setTimeout()`
- 条件付き依存: `if (toolbarParent)` → `this.#getBoundsWithoutFlushing()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.dataTransfer`, `aEvent.target`, `aEvent.target.ownerDocument.documentElement.id`, `draggedItem.id`, `dt.effectAllowed`, `item.firstElementChild`, `item.id`, `item.localName`, `item.parentNode`, `itemCenter.x`, `itemCenter.y`, `itemRect.height`, `itemRect.left`, `itemRect.top`, `itemRect.width`, `this._dragInitializeTimeout`, `this._dragOffset`, `this._initializeDragAfterMove`, `toolbarParent.style.minHeight`, `toolbarRect.height`

## this._initializeDragAfterMove()
- 位置: L2548-2579
- 役割: ドラッグ開始の次の処理で、元の項目を隠し、DragPositionManager を始め、隣の項目に before か after のドロップ位置表示を付ける。
- 触るとき: ドラッグ開始直後にプレースホルダーの位置が違うとき、または元の項目の隠し方を変えるときに見る。
- 呼び出し先: `this.#window.clearTimeout()`
- 条件付き依存: `if (this.#customizing && !this.#transitioning)` → `lazy.DragPositionManager.start()`
- 条件付き依存: `if (item.nextElementSibling)` → `this.#setDragActive()`
- 条件付き依存: `if (canUsePrevSibling && item.previousElementSibling)` → `this.#setDragActive()`
- 条件付き依存: `if (this.#customizing && !this.#transitioning)` → `this.#getCustomizableParent()`
- 条件付き依存: `if (this.#customizing && !this.#transitioning)` → `currentArea.setAttribute()`
- 参照: `draggedItem.id`, `item.hidden`, `item.nextElementSibling`, `item.previousElementSibling`, `this.#customizing`, `this.#dragOverItem`, `this.#transitioning`, `this.#window`, `this._dragInitializeTimeout`, `this._initializeDragAfterMove`

## CustomizeMode.#onDragOver()
- 位置: L2595-2731
- 役割: ドラッグ中に対象エリアと移動元を判定し、その場所に応じた before か after の表示を付ける。ツールバーとパネルとパレットでは位置の求め方が違う。
- 触るとき: ドラッグ先のプレースホルダーがずれるとき、ツールバーとパネルの判定の違いを確かめるとき、または移動を禁止する条件を増やすときに見る。
- 呼び出し先: `CustomizableUI.canWidgetMoveToArea()`, `CustomizableUI.getCustomizationTarget()`, `CustomizableUI.getPlaceForItem()`, `CustomizableUI.isWidgetRemovable()`, `__dumpDragData()`, `aEvent.dataTransfer.mozGetDataAt()`, `aEvent.dataTransfer.mozTypesAt()`, `aEvent.preventDefault()`, `aEvent.stopPropagation()`, `document.getElementById()`, `dragOverItem.getAttribute()`, `this.#getCustomizableParent()`, `this.#getDragOverNode()`, `this.#isUnwantedDragDrop()`
- 条件付き依存: `if (this._initializeDragAfterMove)` → `this._initializeDragAfterMove()`
- 条件付き依存: `if (targetNode == CustomizableUI.getCustomizationTarget(targetArea))` → `this.#findVisiblePreviousSiblingNode()`
- 条件付き依存: `if (!(targetNode == CustomizableUI.getCustomizationTarget(targetArea)))` → `Array.prototype.indexOf.call()`
- 条件付き依存: `if (position == -1)` → `this.#findVisiblePreviousSiblingNode()`
- 条件付き依存: `if (targetAreaType == "toolbar")` → `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (targetAreaType == "toolbar")` → `dragOverItem.getAttribute()`
- 条件付き依存: `if (existingDir == "before")` → `parseInt()`
- 条件付き依存: `if (!(existingDir == "before"))` → `parseInt()`
- 条件付き依存: `if (targetAreaType == "panel")` → `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (targetAreaType == "panel")` → `dragOverItem.getAttribute()`
- 条件付き依存: `if (this.#dragOverItem && dragOverItem != this.#dragOverItem)` → `this.#cancelDragActive()`
- 条件付き依存: `if ( dragOverItem != this.#dragOverItem || dragValue != dragOverItem.getAttribute("dragover") )` → `CustomizableUI.getCustomizationTarget()`
- 条件付き依存: `if (dragOverItem != CustomizableUI.getCustomizationTarget(targetArea))` → `this.#setDragActive()`
- 条件付き依存: `if ( dragOverItem != this.#dragOverItem || dragValue != dragOverItem.getAttribute("dragover") )` → `targetArea.setAttribute()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.currentTarget`, `aEvent.dataTransfer.mozTypesAt(0).length`, `aEvent.target.ownerDocument`, `document.documentElement.id`, `dragOverItem.style.borderBlockEndWidth`, `dragOverItem.style.borderBlockStartWidth`, `dragOverItem.style.borderInlineEndWidth`, `dragOverItem.style.borderInlineStartWidth`, `itemRect.height`, `itemRect.left`, `itemRect.top`, `itemRect.width`, `targetArea.id`, `targetNode.lastElementChild`, `targetNode.parentNode`, `targetParent.children`, `this.#dragOverItem`, `this.#window.RTL_UI`, `this._initializeDragAfterMove`

## CustomizeMode.#onDragDrop()
- 位置: L2742-2802
- 役割: ドロップ時に対象ノードと挿入位置を決め、#applyDrop で移動させる。最後にダウンロードボタンの自動非表示を解除する。
- 触るとき: ドロップ位置が 1 つずれるとき、またはドロップ後の処理を増やすときに見る。
- 呼び出し先: `__dumpDragData()`, `aEvent.dataTransfer.mozGetDataAt()`, `document.getElementById()`, `lazy.log.error()`, `targetNode.getAttribute()`, `this.#applyDrop()`, `this.#cancelDragActive()`, `this.#getCustomizableParent()`, `this.#isUnwantedDragDrop()`, `this.#window.clearTimeout()`
- 条件付き依存: `if (draggedItemId == "downloads-button")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (draggedItemId == "downloads-button")` → `this.#showDownloadsAutoHidePanel()`
- 参照: `aEvent.currentTarget`, `aEvent.target.ownerDocument`, `document.documentElement.id`, `ex.stack`, `targetNode.firstElementChild`, `targetNode.nextElementSibling`, `targetNode.tagName`, `this.#dragOverItem`, `this.#dragSizeMap`, `this._dragInitializeTimeout`, `this._initializeDragAfterMove`
- XPCOM: `Services.prefs`

## CustomizeMode.#applyDrop()
- 位置: L2819-2982
- 役割: 移動元と移動先に応じて、パレットへ戻す、同じエリア内で動かす、別エリアへ追加するなどの配置変更を実行する。
- 触るとき: ドラッグで項目を別エリアへ入れる、パレットへ戻す、特殊項目を作るといった結果が違うとき、またはドロップの規則を変えるときに見る。
- 呼び出し先: `CustomizableUI.canWidgetMoveToArea()`, `CustomizableUI.getCustomizationTarget()`, `CustomizableUI.isSpecialWidget()`, `document.getElementById()`, `draggedItem.closest()`, `draggedItem.getAttribute()`, `draggedItem.removeAttribute()`, `itemForPlacement.getAttribute()`, `this.#onDragEnd()`
- 条件付き依存: `if (toolbarParent)` → `toolbarParent.style.removeProperty()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `CustomizableUI.isWidgetRemovable()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `CustomizableUI.removeWidgetFromArea()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (aOriginArea.id !== kPaletteId)` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if (aTargetNode == this.visiblePalette)` → `this.visiblePalette.appendChild()`
- 条件付き依存: `if (!(aTargetNode == this.visiblePalette))` → `this.visiblePalette.insertBefore()`
- 条件付き依存: `if (aTargetArea.id == kPaletteId)` → `this.#onDragEnd()`
- 条件付き依存: `if (draggedItem.getAttribute("skipintoolbarset") == "true")` → `draggedItem.parentNode.getAttribute()`
- 条件付き依存: `if (draggedItem.getAttribute("skipintoolbarset") == "true")` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `areaCustomizationTarget.appendChild()`
- 条件付き依存: `if (!(aTargetNode == areaCustomizationTarget))` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (!(aTargetNode == areaCustomizationTarget))` → `areaCustomizationTarget.insertBefore()`
- 条件付き依存: `if (!(aTargetNode == areaCustomizationTarget))` → `this.wrapToolbarItem()`
- 条件付き依存: `if (draggedItem.getAttribute("skipintoolbarset") == "true")` → `this.wrapToolbarItem()`
- 条件付き依存: `if ( CustomizableUI.isSpecialWidget(aDroppedItemId) && aOriginArea.id == kPaletteId )` → `aDroppedItemId.match()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (aTargetNode == areaCustomizationTarget)` → `this.#onDragEnd()`
- 条件付き依存: `if (itemForPlacement)` → `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!placement)` → `lazy.log.debug()`
- 条件付き依存: `if (aTargetArea == aOriginArea)` → `CustomizableUI.moveWidgetWithinArea()`
- 条件付き依存: `if (aTargetArea == aOriginArea)` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (!(aTargetArea == aOriginArea))` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (!(aTargetArea == aOriginArea))` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (aTargetNode != itemForPlacement)` → `container.insertBefore()`
- 参照: `aEvent.target.ownerDocument`, `aOriginArea.id`, `aTargetArea.id`, `aTargetNode.className`, `aTargetNode.id`, `aTargetNode.nodeName`, `aTargetNode.parentNode`, `draggedItem.hidden`, `draggedItem.parentNode`, `draggedWrapper.parentNode`, `itemForPlacement.firstElementChild`, `itemForPlacement.firstElementChild.id`, `itemForPlacement.id`, `itemForPlacement.nodeName`, `itemForPlacement.parentNode`, `itemForPlacement.parentNode.nextElementSibling`, `itemForPlacement.parentNode.nodeName`, `placement.position`, `this.visiblePalette`

## CustomizeMode.#onDragLeave()
- 位置: L2990-3006
- 役割: ドラッグがエリアの外へ出たとき(イベントの対象がエリア自身のとき)、ドラッグ表示を取り消して dragOverItem を空にする。
- 触るとき: ドラッグを外へ出した後もドロップ位置の表示が残るときに見る。
- 呼び出し先: `__dumpDragData()`, `this.#isUnwantedDragDrop()`
- 条件付き依存: `if (this.#dragOverItem && aEvent.target == aEvent.currentTarget)` → `this.#cancelDragActive()`
- 参照: `aEvent.currentTarget`, `aEvent.target`, `this.#dragOverItem`

## CustomizeMode.#onDragEnd()
- 位置: L3014-3057
- 役割: ドラッグ終了時に wrapper の hidden と mousedown を戻し、ドラッグ表示を取り消してドラッグ位置管理を止める。
- 触るとき: ドラッグを離した後も項目が隠れたままのとき、または bug 460801 の回避策を見直すときに見る。(コメントは drop の転送に触れるが、本体はその処理を行わない)
- 呼び出し先: `__dumpDragData()`, `aEvent.dataTransfer.mozGetDataAt()`, `aEvent.dataTransfer.mozTypesAt()`, `document.getElementById()`, `lazy.DragPositionManager.stop()`, `this.#isUnwantedDragDrop()`, `this.#window.clearTimeout()`
- 条件付き依存: `if (draggedWrapper)` → `draggedWrapper.removeAttribute()`
- 条件付き依存: `if (draggedWrapper)` → `draggedWrapper.closest()`
- 条件付き依存: `if (toolbarParent)` → `toolbarParent.style.removeProperty()`
- 条件付き依存: `if (this.#dragOverItem)` → `this.#cancelDragActive()`
- 参照: `aEvent.target.ownerDocument`, `document.documentElement.id`, `draggedWrapper.hidden`, `this.#dragOverItem`, `this._dragInitializeTimeout`, `this._initializeDragAfterMove`

## CustomizeMode.#isUnwantedDragDrop()
- 位置: L3069-3086
- 役割: ドラッグの発生元がこの窓の要素でなければ無視すべきと判定する。テスト用の pref で発生元の確認を省ける。
- 触るとき: 外部からのドラッグを受け付ける条件を変えるとき、またはテストでドロップが無視されるときに見る。
- 参照: `aEvent.dataTransfer.mozSourceNode`, `mozSourceNode.documentGlobal`, `this.#skipSourceNodeCheck`, `this.#window`

## CustomizeMode.#setDragActive()
- 位置: L3107-3156
- 役割: 対象の項目に dragover 属性と before か after の枠幅を付ける。パレットはグリッド処理へ回し、ツールバーとパネルは枠線で隙間を作る。
- 触るとき: ドラッグ中のプレースホルダーの見た目や隙間の幅を変えるとき、またはツールバーで隙間の向きが逆になるときに見る。
- 呼び出し先: `aDraggedOverItem.getAttribute()`
- 条件付き依存: `if (aDraggedOverItem.getAttribute("dragover") != aValue)` → `aDraggedOverItem.setAttribute()`
- 条件付き依存: `if (aDraggedOverItem.getAttribute("dragover") != aValue)` → `window.document.getElementById()`
- 条件付き依存: `if (aPlace == "palette")` → `this.#setGridDragActive()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `this.#getCustomizableParent()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `gDraggingInToolbars.has()`
- 条件付き依存: `if (!gDraggingInToolbars.has(targetArea.id))` → `gDraggingInToolbars.add()`
- 条件付き依存: `if (!gDraggingInToolbars.has(targetArea.id))` → `this.$()`
- 条件付き依存: `if (!gDraggingInToolbars.has(targetArea.id))` → `this.#getCustomizableParent()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `this.#getDragItemSize()`
- 条件付き依存: `if (aValue == "before")` → `layoutSide.toLowerCase()`
- 条件付き依存: `if (!(aValue == "before"))` → `layoutSide.toLowerCase()`
- 条件付き依存: `if (makeSpaceImmediately)` → `aDraggedOverItem.setAttribute()`
- 条件付き依存: `if (!(aPlace == "palette"))` → `aDraggedOverItem.style.removeProperty()`
- 条件付き依存: `if (makeSpaceImmediately)` → `aDraggedOverItem.getBoundingClientRect()`
- 条件付き依存: `if (makeSpaceImmediately)` → `aDraggedOverItem.removeAttribute()`
- 参照: `aDraggedOverItem.documentGlobal`, `aDraggedOverItem.style`, `targetArea.id`

## CustomizeMode.#cancelDragActive()
- 位置: L3171-3212
- 役割: ドラッグ表示を取り消す。エリアの種類で処理が分かれ、ツールバーとパネルでは項目の枠を消し、パレットでは位置管理の placeholder を消す。
- 触るとき: ドラッグ表示が取り消されないとき、またはエリアごとに取消方法を変えるときに見る。
- 呼び出し先: `CustomizableUI.getAreaType()`, `this.#getCustomizableParent()`
- 条件付き依存: `if (currentArea != nextArea)` → `currentArea.removeAttribute()`
- 条件付き依存: `if (aNoTransition)` → `aDraggedOverItem.setAttribute()`
- 条件付き依存: `if (areaType)` → `aDraggedOverItem.removeAttribute()`
- 条件付き依存: `if (areaType)` → `aDraggedOverItem.style.removeProperty()`
- 条件付き依存: `if (aNoTransition)` → `aDraggedOverItem.getBoundingClientRect()`
- 条件付き依存: `if (aNoTransition)` → `aDraggedOverItem.removeAttribute()`
- 条件付き依存: `if (!(areaType))` → `aDraggedOverItem.removeAttribute()`
- 条件付き依存: `if (!(areaType))` → `lazy.DragPositionManager.getManagerForArea()`
- 条件付き依存: `if (!(areaType))` → `positionManager.clearPlaceholders()`
- 参照: `currentArea.id`

## CustomizeMode.#setGridDragActive()
- 位置: L3223-3236
- 役割: パレットで、ドラッグ中の項目の大きさを使い、DragPositionManager に placeholder を挿入させる。
- 触るとき: パレット上のグリッドのプレースホルダーがずれるときに見る。
- 呼び出し先: `lazy.DragPositionManager.getManagerForArea()`, `positionManager.insertPlaceholder()`, `this.#getCustomizableParent()`, `this.#getDragItemSize()`, `this.$()`
- 参照: `aDraggedItem.id`

## CustomizeMode.#getDragItemSize()
- 位置: L3249-3313
- 役割: ドラッグ中の項目を一時的に移動先へ置いて大きさを測り、元の位置へ戻す。結果は移動先ごとにキャッシュする。
- 触るとき: 移動先によって項目の大きさが変わる不具合を調べるとき、またはサイズの測り方を変えるときに見る。
- 呼び出し先: `aDraggedItem.parentNode.getBoundingClientRect()`, `itemMap.get()`, `itemMap.set()`, `this.#dragSizeMap.get()`, `this.#dragSizeMap.has()`, `this.#getCustomizableParent()`
- 条件付き依存: `if (!this.#dragSizeMap.has(aDraggedItem))` → `this.#dragSizeMap.set()`
- 条件付き依存: `if (targetArea != currentArea)` → `aDragOverNode.parentNode.insertBefore()`
- 条件付き依存: `if (targetArea != currentArea)` → `CustomizableUI.getAreaType()`
- 条件付き依存: `if (targetArea != currentArea)` → `aDraggedItem.hasAttribute()`
- 条件付き依存: `if (targetArea != currentArea)` → `aDraggedItem.getAttribute()`
- 条件付き依存: `if (areaType)` → `aDraggedItem.setAttribute()`
- 条件付き依存: `if (targetArea != currentArea)` → `this.wrapToolbarItem()`
- 条件付き依存: `if (targetArea != currentArea)` → `CustomizableUI.onWidgetDrag()`
- 条件付き依存: `if (targetArea != currentArea)` → `this.unwrapToolbarItem()`
- 条件付き依存: `if (targetArea != currentArea)` → `currentParent.insertBefore()`
- 条件付き依存: `if (currentType === false)` → `aDraggedItem.removeAttribute()`
- 条件付き依存: `if (!(currentType === false))` → `aDraggedItem.setAttribute()`
- 条件付き依存: `if (targetArea != currentArea)` → `this.createOrUpdateWrapper()`
- 参照: `aDraggedItem.id`, `aDraggedItem.nextElementSibling`, `aDraggedItem.parentNode`, `aDraggedItem.parentNode.hidden`, `rect.height`, `rect.width`, `targetArea.id`, `this.#dragSizeMap`

## CustomizeMode.#getCustomizableParent()
- 位置: L3325-3341
- 役割: パネルの枠内なら固定リストを返し、それ以外は要素の祖先から CustomizableUI のエリアかパレットを探す。
- 触るとき: ドロップ先のエリアが誤判定されるとき、特にパネルの余白上での扱いを調べるときに見る。
- 呼び出し先: `CSS.escape()`, `aElement.closest()`, `areas.map()`, `areas.map(a => "#" + CSS.escape(a)).join()`, `areas.push()`
- 条件付き依存: `if (aElement)` → `aElement.closest()`
- 条件付き依存: `if (containingPanelHolder)` → `containingPanelHolder.querySelector()`
- 参照: `CustomizableUI.areas`

## CustomizeMode.#getDragOverNode()
- 位置: L3365-3398
- 役割: ドラッグ位置から、エリア内で実際に重なっている項目を探す。ツールバーとパネルは要素の位置で、パレットは DragPositionManager の find で求める。
- 触るとき: ドラッグ中に指している項目が期待とずれるとき、またはツールバーとパレットの判定の違いを調べるときに見る。
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `Math.max()`, `Math.min()`, `expectedParent.contains()`, `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (aPlace == "toolbar" || aPlace == "panel")` → `aAreaElement.ownerDocument.elementFromPoint()`
- 条件付き依存: `if (!(aPlace == "toolbar" || aPlace == "panel"))` → `lazy.DragPositionManager.getManagerForArea()`
- 条件付き依存: `if (!(aPlace == "toolbar" || aPlace == "panel"))` → `positionManager.find()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.target`, `bounds.bottom`, `bounds.left`, `bounds.right`, `bounds.top`, `targetNode.parentNode`, `this._dragOffset.x`, `this._dragOffset.y`

## CustomizeMode.#onMouseDown()
- 位置: L3408-3417
- 役割: 主ボタンの mousedown で、項目の wrapper に mousedown 属性を付ける。
- 触るとき: ドラッグの開始条件に mousedown 属性を使うとき、またはクリック中の見た目を変えるときに見る。
- 呼び出し先: `lazy.log.debug()`, `this.#getWrapper()`
- 条件付き依存: `if (item)` → `item.toggleAttribute()`
- 参照: `aEvent.button`, `aEvent.target`

## CustomizeMode.#onMouseUp()
- 位置: L3427-3436
- 役割: 主ボタンの mouseup で、wrapper の mousedown 属性を外す。
- 触るとき: クリックの後に mousedown 属性が残るときに見る。
- 呼び出し先: `lazy.log.debug()`, `this.#getWrapper()`
- 条件付き依存: `if (item)` → `item.removeAttribute()`
- 参照: `aEvent.button`, `aEvent.target`

## CustomizeMode.#getWrapper()
- 位置: L3449-3457
- 役割: 要素の祖先をたどって toolbarpaletteitem を探す。途中で toolbar に当たったら null を返す。
- 触るとき: wrapper を特定する経路を変えるとき、またはツールバー内の要素で誤った wrapper を取るときに見る。
- 参照: `aElement.localName`, `aElement.parentNode`

## CustomizeMode.#findVisiblePreviousSiblingNode()
- 位置: L3474-3483
- 役割: 前の兄弟を、中身が表示されている wrapper まで遡って探す。
- 触るとき: ツールバーのドロップ位置で非表示の項目を飛ばす判定を見直すときに見る。
- 参照: `aReferenceNode.firstElementChild.hidden`, `aReferenceNode.localName`, `aReferenceNode.previousElementSibling`

## CustomizeMode.#onPaletteContextMenuShowing()
- 位置: L3492-3498
- 役割: パレットのコンテキストメニューを開くとき、伸縮スペースの項目ではパネルへ追加する項目を無効にする。
- 触るとき: 伸縮スペースに対するメニュー項目の有効・無効を変えるときに見る。
- 呼び出し先: `event.target.querySelector()`, `event.target.triggerNode.id.includes()`
- 参照: `event.target.querySelector(".customize-context-addToPanel").disabled`

## CustomizeMode.onPanelContextMenuShowing()
- 位置: L3508-3525
- 役割: パネル項目のメニューで、固定エリアの項目ならピン留め解除を、それ以外ならピン留めを表示する。FTL を読み込み、遅延ローカライズの属性を付け替える。
- 触るとき: パネル項目のメニューの表示が正しくないとき、または遅延ローカライズの扱いを変えるときに見る。
- 呼び出し先: `doc.documentGlobal.MozXULElement.insertFTLIfNeeded()`, `doc.getElementById()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `event.target.querySelectorAll()`, `event.target.querySelectorAll("[data-lazy-l10n-id]").forEach()`, `event.target.triggerNode.closest()`
- 参照: `doc.getElementById("customizationPanelItemContextMenuPin").hidden`, `doc.getElementById("customizationPanelItemContextMenuUnpin").hidden`, `event.target.ownerDocument`

## CustomizeMode.#checkForDownloadsClick()
- 位置: L3535-3542
- 役割: 窓のクリックが、ダウンロードボタンの wrapper に対する主ボタンのクリックなら、自動非表示パネルを開く。
- 触るとき: カスタマイズ中にダウンロードボタンを押してもパネルが出ない、または二重に出るときに見る。
- 呼び出し先: `event.target.closest()`
- 条件付き依存: `if ( event.target.closest("#wrapper-downloads-button") && event.button == 0 )` → `event.view.gCustomizeMode.#showDownloadsAutoHidePanel()`
- 参照: `event.button`

## CustomizeMode.#setupDownloadAutoHideToggle()
- 位置: L3550-3552
- 役割: 窓に capture フェーズの click リスナーを付け、ダウンロードボタンのクリックを検出できるようにする。
- 触るとき: カスタマイズ中にダウンロードボタンのクリックを捉える仕組みを変えるときに見る。
- 呼び出し先: `this.#window.addEventListener()`
- 参照: `this.#checkForDownloadsClick`

## CustomizeMode.#teardownDownloadAutoHideToggle()
- 位置: L3558-3565
- 役割: 窓の click リスナーを外し、ダウンロード自動非表示パネルを閉じる。
- 触るとき: カスタマイズを終えた後にパネルが残るときに見る。
- 呼び出し先: `this.#window.removeEventListener()`, `this.$()`, `this.$(kDownloadAutohidePanelId).hidePopup()`
- 参照: `this.#checkForDownloadsClick`

## CustomizeMode.#maybeMoveDownloadsButtonToNavBar()
- 位置: L3572-3604
- 役割: 自動非表示をパレット上で切り替えたまま項目を動かしていない場合、ダウンロードボタンをナビゲーションバーの検索欄の後ろへ戻す。
- 触るとき: カスタマイズを抜けた後にダウンロードボタンの位置が戻らないときや、ナビバーでの挿入位置を変えるときに見る。
- 呼び出し先: `CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `navbarPlacements.indexOf()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `widget.includes()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if ( !CustomizableUI.getPlacementOfWidget("downloads-button") && this.#moveDownloadsButtonToNavBar && this.#window.DownloadsButton.autoHideDownloadsButton )` → `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 参照: `navbarPlacements.length`, `this.#moveDownloadsButtonToNavBar`, `this.#window.DownloadsButton.autoHideDownloadsButton`

## CustomizeMode.#showDownloadsAutoHidePanel()
- 位置: async L3614-3672
- 役割: ダウンロードボタンの横に自動非表示の切替パネルを開く。オーバーフロー内では開かない。ナビバーでは項目の並びで左右を決め、他ではレイアウトを確定させてから位置を計算する。
- 触るとき: 自動非表示パネルの位置や表示条件を変えるときに見る。
- 呼び出し先: `button.closest()`, `doc.getElementById()`, `panel.hidePopup()`, `panel.openPopup()`
- 条件付き依存: `if (toolbarContainer && toolbarContainer.id == "nav-bar")` → `CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (toolbarContainer && toolbarContainer.id == "nav-bar")` → `navbarWidgets.indexOf()`
- 条件付き依存: `if (!(toolbarContainer && toolbarContainer.id == "nav-bar"))` → `this.#window.promiseDocumentFlushed()`
- 条件付き依存: `if (!(toolbarContainer && toolbarContainer.id == "nav-bar"))` → `this.#getBoundsWithoutFlushing()`
- 条件付き依存: `if (this.#window.DownloadsButton.autoHideDownloadsButton)` → `checkbox.setAttribute()`
- 条件付き依存: `if (!(this.#window.DownloadsButton.autoHideDownloadsButton))` → `checkbox.removeAttribute()`
- 参照: `buttonBounds.left`, `buttonBounds.width`, `doc.documentElement`, `this.#customizing`, `this.#document`, `this.#window.DownloadsButton.autoHideDownloadsButton`, `this._wantToBeInCustomizeMode`, `toolbarContainer.id`, `windowBounds.width`

## CustomizeMode.#onDownloadsAutoHideChange()
- 位置: L3680-3687
- 役割: 自動非表示のチェックの値を pref に保存し、離脱時にボタンを移すかどうかの状態を保持する。
- 触るとき: 自動非表示の切替が保存されないときや、離脱時の移動条件を変えるときに見る。
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.target.ownerDocument.getElementById()`
- 参照: `checkbox.checked`, `event.view.gCustomizeMode.#moveDownloadsButtonToNavBar`
- XPCOM: `Services.prefs`

## CustomizeMode.#customizeTouchBar()
- 位置: L3692-3697
- 役割: macOS の Touch Bar のカスタマイズ画面を開始する。
- 触るとき: Touch Bar のカスタマイズの起動の仕方を変えるときに見る。
- 呼び出し先: `Cc["@mozilla.org/widget/touchbarupdater;1"].getService()`, `updater.enterCustomizeMode()`
- 参照: `Ci.nsITouchBarUpdater`
- XPCOM: `nsITouchBarUpdater` / `@mozilla.org/widget/touchbarupdater;1`

## CustomizeMode.#togglePong()
- 位置: L3705-3726
- 役割: 隠しゲームの表示をオンオフし、オフにするときは起動中のゲームを止める。
- 触るとき: 隠しゲームの表示条件を変えるとき、または終了時に止まらないときに見る。
- 呼び出し先: `this.$()`
- 条件付き依存: `if (enabled)` → `this.visiblePalette.setAttribute()`
- 条件付き依存: `if (!this.uninitWhimsy)` → `this.#whimsypong()`
- 条件付き依存: `if (!(enabled))` → `this.visiblePalette.removeAttribute()`
- 条件付き依存: `if (this.uninitWhimsy)` → `this.uninitWhimsy()`
- 参照: `this.pongArena.hidden`, `this.uninitWhimsy`, `whimsyButton.checked`

## CustomizeMode.#whimsypong()
- 位置: L3735-3973
- 役割: パレット上で動く pong 風の隠しゲームを作る。特定のキー列で特別な表示が出る。終了時の後始末関数を返す。
- 触るとき: 隠しゲームの挙動や画面要素を変えるとき、または終了後にアニメーションが残るときに見る。
- 呼び出し先: `document.addEventListener()`, `document.createXULElement()`, `document.getElementById()`, `elements.arena.appendChild()`, `elements.arena.querySelector()`, `this.visiblePalette.querySelector()`, `window.requestAnimationFrame()`
- 参照: `el.id`, `elements.arena.querySelector(player).style.background`, `spacer.id`, `this.#document`, `this.#window`, `this.uninitWhimsy`

## update()
- 位置: L3736-3739
- 役割: ボールとプレイヤーを 1 フレーム分進める。
- 触るとき: 隠しゲームの 1 フレームの処理を変えるときに見る。
- 呼び出し先: `updateBall()`, `updatePlayers()`

## updateBall()
- 位置: L3741-3776
- 役割: ボールの反射、パドルとの判定、得点、速度の変化を計算して位置を更新する。
- 触るとき: ボールの動きや得点の条件を変えるときに見る。
- 呼び出し先: `Math.max()`, `Math.min()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] < p1 || ball[0] > p1 + paddleWidth)) || (ball[1] >= gameSide && (ball[0] < p2 || ball[0] > p2 + paddleWidth)) )` → `updateScore()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.random()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.max()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.min()`
- 条件付き依存: `if ( (ball[1] <= 0 && (ball[0] - p1 < paddleEdge || p1 + paddleWidth - ball[0] < paddleEdge)) || (ball[1] >= gameSide && (ball[0] - p2 < paddleEdge || p2 + paddl...)` → `Math.abs()`
- 条件付き依存: `if (Math.abs(ballDxDy[0]) == 6)` → `Math.sign()`
- 条件付き依存: `if (Math.abs(ballDxDy[0]) == 6)` → `Math.random()`

## updatePlayers()
- 位置: L3778-3809
- 役割: 左右キーでプレイヤー 1 を動かし、プレイヤー 2 をボールに追わせ、いずれも可動範囲に収める。
- 触るとき: パドルの動きや相手の追従を変えるときに見る。
- 呼び出し先: `Math.max()`, `Math.min()`, `Math.sign()`
- 参照: `window.RTL_UI`

## updateScore()
- 位置: L3811-3820
- 役割: 得点時は score を増やし、失点時は lives を減らす。その後ボールと速度を初期値に戻す。
- 触るとき: 得点やライフの扱いを変えるとき、または失点の後で速度がおかしいときに見る。
- 呼び出し先: `ballDef.slice()`, `ballDxDyDef.slice()`

## draw()
- 位置: L3822-3855
- 役割: プレイヤー、ボール、得点、残機の要素の位置と属性を描画する。勝利後は背景画像を重ねていく。
- 触るとき: 隠しゲームの表示を変えるとき、または勝利後に背景が増え続ける理由を調べるときに見る。
- 呼び出し先: `elements["wp-lives"].setAttribute()`
- 条件付き依存: `if (arena.style.backgroundImage)` → `arena.style.backgroundImage.split()`
- 参照: `arena.style.backgroundImage`, `arena.style.backgroundImage.split(",").length`, `arena.style.backgroundPosition`, `arena.style.backgroundRepeat`, `arena.style.backgroundSize`, `elements.arena`, `elements["wp-ball"].style.transform`, `elements["wp-player1"].style.transform`, `elements["wp-player2"].style.transform`, `elements["wp-score"].textContent`, `window.RTL_UI`

## onkeydown()
- 位置: L3857-3880
- 役割: 押されたキーを記録し、決められた 10 キーの並びと照合する。左右キーでは押下状態と加速量を更新する。
- 触るとき: 隠しゲームの入力や隠し表示の条件を変えるときに見る。
- 呼び出し先: `keys.push()`
- 条件付き依存: `if (keys.length > 10)` → `keys.shift()`
- 条件付き依存: `if (codeEntered)` → `elements.arena.setAttribute()`
- 条件付き依存: `if (codeEntered)` → `document.querySelector()`
- 条件付き依存: `if (codeEntered)` → `spacer.setAttribute()`
- 参照: `event.which`, `keys.length`

## onkeyup()
- 位置: L3882-3887
- 役割: 左右キーを離したとき、押下状態と加速量を初期値に戻す。
- 触るとき: キーを離した後もパドルが動き続けるときに見る。
- 参照: `event.which`

## uninit()
- 位置: L3889-3913
- 役割: キーのリスナーを外し、描画の予約を止め、表示要素と属性を消して参照を解放する。
- 触るとき: 隠しゲームを閉じた後に要素や背景の属性が残るときに見る。
- 呼び出し先: `arena.firstChild.remove()`, `arena.removeAttribute()`, `arena.style.removeProperty()`, `document.querySelector()`, `document.removeEventListener()`, `spacer.removeAttribute()`
- 条件付き依存: `if (rAFHandle)` → `window.cancelAnimationFrame()`
- 参照: `arena.firstChild`, `elements.arena`

## animate()
- 位置: L3958-3970
- 役割: 1 フレームごとに update と draw を呼び、終了条件を満たすまで requestAnimationFrame を予約し続ける。
- 触るとき: 隠しゲームの描画ループの止め方や速度を変えるときに見る。
- 呼び出し先: `draw()`, `update()`
- 条件付き依存: `if (quit)` → `elements["wp-lives"].setAttribute()`
- 条件付き依存: `if (quit)` → `elements.arena.setAttribute()`
- 条件付き依存: `if (!(quit))` → `window.requestAnimationFrame()`
- 参照: `elements["wp-score"].textContent`

## __dumpDragData()
- 位置: L3985-4016
- 役割: debug の設定が有効なときだけ、ドラッグイベントの種類、対象、dataTransfer の内容をログに出す。
- 触るとき: ドラッグのデバッグ時にログへ出す情報を変えるときに見る。
- 呼び出し先: `lazy.log.debug()`
- 参照: `aEvent.dataTransfer`, `aEvent.type`, `aEvent[el].id`, `aEvent[el].localName`
