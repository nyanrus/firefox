# browser/components/tabbrowser/content/tab-hover-preview.mjs

source: browser/components/tabbrowser/content/tab-hover-preview.mjs
source-hash: da8702a6d9b763f337edfa7ab9a981876545ca97
lines: 1337

## <module>
- 役割: タブ、折りたたまれたタブグループ、タブメモにマウスを載せたときのホバープレビューパネル群と、その表示遅延を管理するモジュール。
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`

## TabHoverPanelSet.constructor()
- 位置: L51-98
- 役割: pref の取得を設定し、タブ・グループ・メモの3パネルと遅延実行器を作り、他のポップアップの監視とタブのドラッグ開始時の非表示を登録する。
- 触るとき: ホバープレビュー全体の初期化と、ドラッグ開始時にプレビューが消える仕組みを調べるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `event.target.closest()`, `lazy.Tabbrowser.isTab()`, `lazy.Tabbrowser.isTabGroupLabel()`, `this.#setExternalPopupListeners()`, `this.#win.document.getElementById()`, `this.#win.gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if ( target && (lazy.Tabbrowser.isTab(target) || lazy.Tabbrowser.isTabGroupLabel(target)) )` → `this.deactivate()`
- 参照: `this.#activePanel`, `this.#deactivateTimers`, `this.#win`, `this.panelOpener`, `this.tabGroupPanel`, `this.tabNotePanel`, `this.tabPanel`

## TabHoverPanelSet.activate()
- 位置: L110-132
- 役割: 対象がタブならタブ用、折りたたみ済みグループならグループ用のパネルを有効にし、それ以外は例外を投げる。
- 触るとき: どのホバーでどのパネルが出るか、出ない条件を調べるとき。
- 呼び出し先: `lazy.Tabbrowser.isTab()`, `this.shouldActivate()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup))` → `this.#setActivePanel()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup))` → `this.tabPanel.activate()`
- 条件付き依存: `if (!(lazy.Tabbrowser.isTab(tabOrGroup)))` → `lazy.Tabbrowser.isTabGroup()`
- 条件付き依存: `if (lazy.Tabbrowser.isTabGroup(tabOrGroup))` → `this.#setActivePanel()`
- 条件付き依存: `if (lazy.Tabbrowser.isTabGroup(tabOrGroup))` → `this.tabGroupPanel.activate()`
- 参照: `tabOrGroup._noteIconHover`, `tabOrGroup.collapsed`, `this.tabGroupPanel`, `this.tabPanel`

## TabHoverPanelSet.deactivate()
- 位置: L147-160
- 役割: 対象に応じてタブ、メモ、グループの各パネルを非表示にする(force で待ち時間を省く)。自動非表示を無効にする pref があれば何もしない。
- 触るとき: マウスが離れたときにパネルが閉じる動きを変える・調べるとき。
- 呼び出し先: `lazy.Tabbrowser.isTab()`, `lazy.Tabbrowser.isTabGroup()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup) || !tabOrGroup)` → `this.tabPanel.deactivate()`
- 条件付き依存: `if (lazy.Tabbrowser.isTab(tabOrGroup) || !tabOrGroup)` → `this.tabNotePanel.deactivate()`
- 条件付き依存: `if (lazy.Tabbrowser.isTabGroup(tabOrGroup) || !tabOrGroup)` → `this.tabGroupPanel.deactivate()`
- 参照: `this._prefDisableAutohide`

## TabHoverPanelSet.activateNotePanel()
- 位置: L162-168
- 役割: 表示可能なら、メモパネルを現在のパネルとして指定の要素に固定して有効にする。
- 触るとき: タブメモのプレビューが出るきっかけを調べるとき。
- 呼び出し先: `this.#setActivePanel()`, `this.shouldActivate()`, `this.tabNotePanel.activate()`
- 参照: `this.tabNotePanel`

## TabHoverPanelSet.deactivateNotePanel()
- 位置: L170-175
- 役割: 自動非表示が有効なら、指定タブについてメモパネルの非表示を依頼する。
- 触るとき: メモアイコンからマウスが離れたときの閉じ方を調べるとき。
- 呼び出し先: `this.tabNotePanel.deactivate()`
- 参照: `this._prefDisableAutohide`

## TabHoverPanelSet.#setActivePanel()
- 位置: L177-184
- 役割: 別のパネルが有効なら即座に閉じ、指定パネルを有効として記録して保留中の非表示タイマーを解除する。
- 触るとき: パネル同士が同時に出ない仕組みを調べるとき。
- 呼び出し先: `this.#clearDeactivateTimer()`
- 条件付き依存: `if (this.#activePanel && this.#activePanel != panel)` → `this.requestDeactivate()`
- 参照: `this.#activePanel`

## TabHoverPanelSet.requestDeactivate()
- 位置: L186-201
- 役割: パネルの非表示を依頼し、force なら即時、そうでなければ短い待ち後にホバー中でないことを確認して閉じる。
- 触るとき: マウスがタブとパネルの間を移動する際に消えてしまう問題を調べるとき。
- 呼び出し先: `panel.hoverTargets?.some()`, `t.matches()`, `this.#clearDeactivateTimer()`, `this.#deactivateTimers.delete()`, `this.#deactivateTimers.set()`, `this.#doDeactivate()`, `this.#win.setTimeout()`
- 条件付き依存: `if (force)` → `this.#doDeactivate()`

## TabHoverPanelSet.#clearDeactivateTimer()
- 位置: L203-209
- 役割: パネルに登録された非表示タイマーがあれば解除して削除する。
- 触るとき: 非表示の取り消しが効かない問題を調べるとき。
- 呼び出し先: `this.#deactivateTimers.get()`
- 条件付き依存: `if (timer)` → `this.#win.clearTimeout()`
- 条件付き依存: `if (timer)` → `this.#deactivateTimers.delete()`

## TabHoverPanelSet.#doDeactivate()
- 位置: L211-239
- 役割: パネルを実際に閉じる。表示開始中なら表示完了を待ってから閉じ、通常は閉じた後に遅延を一時的にゼロにする。
- 触るとき: 表示途中で閉じられたときの不具合や、閉じた直後の再表示の速さを調べるとき。
- 呼び出し先: `panel.onBeforeHide()`, `panel.panelElement.hidePopup()`, `this.panelOpener.clear()`, `this.panelOpener.setZeroDelay()`
- 条件付き依存: `if (panel.panelElement.state == "showing")` → `panel.panelElement.addEventListener()`
- 条件付き依存: `if (this.#activePanel != panel)` → `this.#doDeactivate()`
- 参照: `panel.panelElement.state`, `this.#activePanel`

## TabHoverPanelSet.forceReset()
- 位置: L241-251
- 役割: 3つのパネルのタイマーを解除して全部閉じ、最後に遅延実行器と有効パネルをリセットする。
- 触るとき: ウィンドウ状態の変化などでプレビューを強制的に消す処理を調べるとき。
- 呼び出し先: `panel.onBeforeHide()`, `panel.panelElement.hidePopup()`, `this.#clearDeactivateTimer()`, `this.panelOpener.reset()`
- 参照: `this.#activePanel`, `this.tabGroupPanel`, `this.tabNotePanel`, `this.tabPanel`

## TabHoverPanelSet.isHoverPanel()
- 位置: L260-264
- 役割: 渡されたノードが管理下の3つのプレビューパネルのいずれかかを返す。
- 触るとき: 他のポップアップとホバーパネルを見分ける箇所を調べるとき。
- 呼び出し先: `[this.tabPanel, this.tabGroupPanel, this.tabNotePanel].some()`
- 参照: `panel.panelElement`, `this.tabGroupPanel`, `this.tabNotePanel`, `this.tabPanel`

## TabHoverPanelSet.shouldActivate()
- 位置: L266-276
- 役割: 他のポップアップが開いておらず、タブ移動中でなく、このウィンドウが最前面のときだけ true を返す。
- 触るとき: プレビューが出ない原因(他パネル、背面ウィンドウ、ドラッグ中)を調べるとき。
- 呼び出し先: `this.#win.gBrowser.tabContainer.hasAttribute()`
- 参照: `Services.focus.activeWindow`, `this.#openPopups.size`, `this.#win`
- XPCOM: `Services.focus`

## TabHoverPanelSet.#setExternalPopupListeners()
- 位置: L283-310
- 役割: 初期に開いている他のパネルを集め、popupshowing と popuphiding を監視して開いている外部ポップアップの集合を維持する。
- 触るとき: 他のメニューが開いている間にプレビューが抑止される仕組みを調べるとき。
- 呼び出し先: `handleExternalPopupEvent()`, `this.#win.document.querySelectorAll()`
- 参照: `this.#openPopups`

## handleExternalPopupEvent()
- 位置: L295-307
- 役割: 指定イベントで、プレビュー自身以外の panel または menupopup を開いているポップアップの集合に追加・削除する。
- 触るとき: 外部ポップアップの追跡対象の条件を調べるとき。
- 呼び出し先: `this.#win.addEventListener()`
- 条件付き依存: `if ( target !== this.tabPanel.panelElement && target !== this.tabGroupPanel.panelElement && target !== this.tabNotePanel.panelElement && (target.nodeName == "pan...)` → `this.#openPopups[setMethod]()`
- 参照: `target.nodeName`, `this.#openPopups`, `this.tabGroupPanel.panelElement`, `this.tabNotePanel.panelElement`, `this.tabPanel.panelElement`

## HoverPanel.constructor()
- 位置: L318-322
- 役割: パネル要素と所属する集合を保持し、要素から所属ウィンドウを取得する。
- 触るとき: 各ホバーパネルの共通の土台を調べるとき。
- 参照: `this.panelElement`, `this.panelElement.documentGlobal`, `this.panelSet`, `this.win`

## HoverPanel.isActive()
- 位置: L324-326
- 役割: パネル要素の状態が open のとき true を返す。
- 触るとき: パネルが開いているかの判定を調べるとき。
- 参照: `this.panelElement.state`

## HoverPanel.deactivate()
- 位置: L328-330
- 役割: 所属する集合に、このパネルの非表示を依頼する。
- 触るとき: サブクラスの deactivate が最終的に呼ぶ共通処理を調べるとき。
- 呼び出し先: `this.panelSet.requestDeactivate()`

## HoverPanel.hoverTargets()
- 位置: L332-334
- 役割: ホバー中とみなす要素として、パネル要素自身だけを返す(サブクラスが上書きする)。
- 触るとき: パネルから離れた判定の対象を調べるとき。
- 参照: `this.panelElement`

## HoverPanel.onBeforeHide()
- 位置: L336-336
- 役割: 非表示の直前に呼ばれる空の既定処理で、サブクラスが後始末のために上書きする。
- 触るとき: 閉じる前の後始末をサブクラスに追加するとき。

## TabPanel.constructor()
- 位置: L352-394
- 役割: サムネイル表示・ワイヤーフレーム収集・タブメモの pref を設定し、メモ追加ボタンをテンプレートから作ってクリックでメモパネルを開くようにする。
- 触るとき: タブ用プレビューの初期化と、メモ追加ボタンの生成を調べるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`, `this.#addNoteButton.addEventListener()`, `this.#openTabNotePanel()`, `this.panelElement.querySelector()`, `this.win.document.getElementById()`, `this.win.document.importNode()`
- 参照: `importedFragment.firstElementChild`, `tabPreviewTemplate.content`, `this.#addNoteButton`, `this.#interactiveArea`, `this.#tab`, `this.#thumbnailElement`

## TabPanel.handleEvent()
- 位置: async L399-422
- 役割: 表示直前に内容を更新し、タブ属性の変更で更新、タブ選択で即時非表示、操作領域からのマウス離脱で非表示にする。
- 触るとき: タブ用プレビューが更新・消去されるイベント条件を調べるとき。
- 呼び出し先: `this.#updatePreview()`, `this.deactivate()`, `this.mouseoutTarget.contains()`, `this.mouseoutTarget?.addEventListener()`
- 条件付き依存: `if ( this.mouseoutTarget && !this.mouseoutTarget.contains(e.relatedTarget) )` → `this.deactivate()`
- 参照: `e.relatedTarget`, `e.target`, `e.type`, `this.mouseoutTarget`

## TabPanel.activate()
- 位置: L424-464
- 役割: 対象タブを記録して位置を合わせ、サムネイルを要求し、開いていれば内容更新、閉じていれば遅延付きで開く。
- 触るとき: タブにホバーしたときのプレビュー表示の流れを調べるとき。
- 呼び出し先: `originalTab?.removeEventListener()`, `this.#maybeRequestThumbnail()`, `this.#movePanel()`, `this.#tab.addEventListener()`
- 条件付き依存: `if ( this.panelElement.state == "open" || this.panelElement.state == "showing" )` → `this.panelElement.removeEventListener()`
- 条件付き依存: `if ( this.panelElement.state == "open" || this.panelElement.state == "showing" )` → `this.#updatePreview()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.panelOpener.execute()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.shouldActivate()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.openPopup()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.win.addEventListener()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.addEventListener()`
- 参照: `this.#tab`, `this.#thumbnailElement`, `this.panelElement.state`, `this.popupOptions`

## TabPanel.deactivate()
- 位置: L471-487
- 役割: タブメモ無効時は強制扱いにし、離れたタブが現在のものなら次フレームで非表示を依頼する。
- 触るとき: タブから離れた直後にプレビューが残る・消えるタイミングを調べるとき。
- 呼び出し先: `super.deactivate()`
- 条件付き依存: `if (leavingTab)` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (this.#tab == leavingTab)` → `this.deactivate()`
- 参照: `this.#tab`, `this._prefUseTabNotes`

## TabPanel.onBeforeHide()
- 位置: L489-496
- 役割: 登録した各リスナーを外し、保持しているタブとサムネイルを破棄する。
- 触るとき: 閉じるときのリスナー解除漏れを調べるとき。
- 呼び出し先: `this.#tab?.removeEventListener()`, `this.mouseoutTarget?.removeEventListener()`, `this.panelElement.removeEventListener()`, `this.win.removeEventListener()`
- 参照: `this.#tab`, `this.#thumbnailElement`

## TabPanel.hoverTargets()
- 位置: L498-507
- 役割: 操作領域に子要素があればそれと、現在のタブを、ホバー中とみなす対象として返す。
- 触るとき: プレビュー上の移動で消えないための判定対象を調べるとき。
- 条件付き依存: `if (this.#interactiveArea.childNodes.length)` → `targets.push()`
- 条件付き依存: `if (this.#tab)` → `targets.push()`
- 参照: `this.#interactiveArea`, `this.#interactiveArea.childNodes.length`, `this.#tab`

## TabPanel.mouseoutTarget()
- 位置: L514-518
- 役割: 操作領域に子要素があるときその領域を、無ければ null を返す。
- 触るとき: マウス離脱で閉じる対象の決め方を調べるとき。
- 参照: `this.#interactiveArea`, `this.#interactiveArea.childNodes.length`

## TabPanel.getPrettyURI()
- 位置: L520-534
- 役割: URI からリーダー表示の元 URL や www を考慮して、表示用のホスト名か about: の文字列を返す。
- 触るとき: プレビューに表示される URL の見せ方を変えるとき。
- 呼び出し先: `URL.parse()`, `url.hostname.replace()`
- 条件付き依存: `if (url.protocol == "about:" && url.pathname == "reader")` → `URL.parse()`
- 条件付き依存: `if (url.protocol == "about:" && url.pathname == "reader")` → `url.searchParams.get()`
- 参照: `url.href`, `url.pathname`, `url.protocol`, `url?.protocol`

## TabPanel.#hasValidWireframeState()
- 位置: L536-544
- 役割: ワイヤーフレーム収集とサムネイル表示が有効で、未選択のタブにワイヤーフレームがあるかを返す。
- 触るとき: ワイヤーフレーム表示が使われる条件を調べるとき。
- 呼び出し先: `lazy.PageWireframes.getWireframeState()`
- 参照: `tab.selected`, `this._prefCollectWireframes`, `this._prefDisplayThumbnail`

## TabPanel.#hasValidThumbnailState()
- 位置: L546-554
- 役割: サムネイル表示が有効で、ブラウザがあり、未ロードでなく選択中でないタブかを返す。
- 触るとき: サムネイルが出ない条件を調べるとき。
- 呼び出し先: `tab.getAttribute()`
- 参照: `tab.linkedBrowser`, `tab.selected`, `this._prefDisplayThumbnail`

## TabPanel.#maybeRequestThumbnail()
- 位置: L556-586
- 役割: サムネイルが使えなければワイヤーフレームで代用し、使えれば canvas に撮影して、まだ有効なら表示を更新する。
- 触るとき: サムネイルの撮影サイズや取得失敗時の挙動を調べるとき。
- 呼び出し先: `console.error()`, `this.#hasValidThumbnailState()`, `this.win.PageThumbs.captureTabPreviewThumbnail()`, `this.win.PageThumbs.captureTabPreviewThumbnail( tab.linkedBrowser, thumbnailCanvas ) .then()`, `this.win.document.createElement()`
- 条件付き依存: `if (!this.#hasValidThumbnailState(tab))` → `lazy.PageWireframes.getWireframeElementForTab()`
- 条件付き依存: `if (wireframeElement)` → `this.#updatePreview()`
- 条件付き依存: `if (captured && this.#tab == tab && this.#hasValidThumbnailState(tab))` → `this.#updatePreview()`
- 参照: `tab.linkedBrowser`, `this.#tab`, `this.#thumbnailElement`, `this.win.devicePixelRatio`, `thumbnailCanvas.height`, `thumbnailCanvas.width`

## TabPanel.#displayTitle()
- 位置: L588-593
- 役割: 現在のタブのラベル文字列を返す(タブが無ければ空)。
- 触るとき: プレビューのタイトル表示の取得元を調べるとき。
- 参照: `this.#tab`, `this.#tab.textLabel.textContent`

## TabPanel.#displayURI()
- 位置: L595-600
- 役割: 現在のタブの URL を表示用に整形して返す(無ければ空)。
- 触るとき: プレビューの URL 表示の取得元を調べるとき。
- 呼び出し先: `this.getPrettyURI()`
- 参照: `this.#tab`, `this.#tab.linkedBrowser`, `this.#tab.linkedBrowser.currentURI.spec`

## TabPanel.#displayPids()
- 位置: L602-610
- 役割: タブに関わるプロセス ID を pid または pids の形式の文字列にして返す。
- 触るとき: デバッグ用のプロセス ID 表示を調べるとき。
- 呼び出し先: `pids.join()`, `this.win.gBrowser.getTabPids()`
- 参照: `pids.length`, `this.#tab`

## TabPanel.#displayActiveness()
- 位置: L612-614
- 役割: docShell が有効なら [A] を返す。
- 触るとき: デバッグ用の活性表示を調べるとき。
- 参照: `this.#tab?.linkedBrowser?.docShellIsActive`

## TabPanel.#displaySponsorProtection()
- 位置: L616-621
- 役割: スポンサー保護のデバッグが有効で保護対象のブラウザなら [S] を返す。
- 触るとき: スポンサー保護のデバッグ表示を調べるとき。
- 呼び出し先: `lazy.SponsorProtection.isProtectedBrowser()`
- 参照: `lazy.SponsorProtection.debugEnabled`, `this.#tab?.linkedBrowser`

## TabPanel.#updateContainerIndicator()
- 位置: L623-655
- 役割: タブのコンテナー(コンテキストアイデンティティ)の色・アイコン・名前を表示欄へ反映し、無ければ隠す。
- 触るとき: コンテナータブのプレビュー表示を調べるとき。
- 呼び出し先: `className.startsWith()`, `indicator.querySelector()`, `lazy.ContextualIdentityService.getPublicIdentityFromId()`, `lazy.ContextualIdentityService.getUserContextLabel()`, `this.panelElement.querySelector()`
- 条件付き依存: `if ( className.startsWith("identity-color-") || className.startsWith("identity-icon-") )` → `indicator.classList.remove()`
- 条件付き依存: `if (identity.color)` → `indicator.classList.add()`
- 条件付き依存: `if (identity.icon)` → `indicator.classList.add()`
- 参照: `identity.color`, `identity.icon`, `indicator.classList`, `indicator.hidden`, `indicator.querySelector(".tab-preview-container-label").textContent`, `this.#tab?.userContextId`

## TabPanel.#openTabNotePanel()
- 位置: L662-668
- 役割: 新着バッジ設定を無効にし、タブメモの編集パネルを開いてホバーパネルを閉じる。
- 触るとき: プレビューからタブメモを追加する操作の流れを調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `this.deactivate()`, `this.win.gBrowser.tabNoteMenu.openPanel()`
- 参照: `lazy.TabNotes.TELEMETRY_SOURCE.TAB_HOVER_PREVIEW_PANEL`, `this.#tab`
- XPCOM: `Services.prefs`

## TabPanel.#updatePreview()
- 位置: async L670-740
- 役割: タイトル、URL、コンテナー表示、デバッグ情報、メモ追加ボタン、サムネイルを更新し、位置を合わせて更新イベントを出す。
- 触るとき: プレビューの内容や表示更新のタイミングを変える・調べるとき。
- 呼び出し先: `lazy.TabNotes.isEligible()`, `this.#hasValidThumbnailState()`, `this.#hasValidWireframeState()`, `this.#movePanel()`, `this.#updateContainerIndicator()`, `this.panelElement.dispatchEvent()`, `this.panelElement.querySelector()`, `thumbnailContainer.classList.toggle()`
- 条件付き依存: `if (lazy.Tabbrowser.prefs.showPidAndActiveness)` → `this.panelElement.querySelector()`
- 条件付き依存: `if (!(lazy.Tabbrowser.prefs.showPidAndActiveness))` → `this.panelElement.querySelector()`
- 条件付き依存: `if (this._prefUseTabNotes && lazy.TabNotes.isEligible(this.#tab))` → `lazy.TabNotes.get()`
- 条件付き依存: `if (note)` → `this.#addNoteButton.remove()`
- 条件付き依存: `if (!(note))` → `this.#interactiveArea.append()`
- 条件付き依存: `if (!(note))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(note))` → `this.#addNoteButton .querySelector("moz-badge") .toggleAttribute()`
- 条件付き依存: `if (!(note))` → `this.#addNoteButton .querySelector()`
- 条件付き依存: `if (!(this._prefUseTabNotes && lazy.TabNotes.isEligible(this.#tab)))` → `this.#addNoteButton.remove()`
- 条件付き依存: `if (thumbnailContainer.firstChild != this.#thumbnailElement)` → `thumbnailContainer.replaceChildren()`
- 条件付き依存: `if (this.#thumbnailElement)` → `thumbnailContainer.appendChild()`
- 条件付き依存: `if (thumbnailContainer.firstChild != this.#thumbnailElement)` → `this.panelElement.dispatchEvent()`
- 参照: `lazy.Tabbrowser.prefs.showPidAndActiveness`, `this.#addNoteButton`, `this.#displayActiveness`, `this.#displayPids`, `this.#displaySponsorProtection`, `this.#displayTitle`, `this.#displayURI`, `this.#tab`, `this.#thumbnailElement`, `this._prefUseTabNotes`, `this.panelElement.querySelector(".tab-preview-activeness").textContent`, `this.panelElement.querySelector(".tab-preview-pid").textContent`, `this.panelElement.querySelector(".tab-preview-title").textContent`, `this.panelElement.querySelector(".tab-preview-uri").textContent`, `thumbnailContainer.firstChild`
- XPCOM: `Services.prefs`

## TabPanel.#movePanel()
- 位置: L742-751
- 役割: タブがあれば、パネルをそのタブの位置へ移動する。
- 触るとき: パネルの位置が合わない問題を調べるとき。
- 条件付き依存: `if (this.#tab)` → `this.panelElement.moveToAnchor()`
- 参照: `this.#tab`, `this.popupOptions.position`, `this.popupOptions.x`, `this.popupOptions.y`

## TabPanel.popupOptions()
- 位置: L753-784
- 役割: 横並び、縦並び、縦のピン留め格子の別と、サイドバーの位置から、パネルの表示位置とずれを返す。
- 触るとき: プレビューの出る位置を調整するとき。
- 呼び出し先: `tabContainer.isContainerVerticalPinnedGrid()`
- 参照: `tabContainer.verticalMode`, `this.#tab`, `this.win.SidebarController._positionStart`, `this.win.gBrowser.tabContainer`

## TabGroupPanel.constructor()
- 位置: L801-806
- 役割: パネルの内容領域を取得し、対象グループを空にして初期化する。
- 触るとき: グループ用プレビューの初期化を調べるとき。
- 呼び出し先: `panel.querySelector()`, `super()`
- 参照: `this.#group`, `this.panelContent`

## TabGroupPanel.activate()
- 位置: L808-828
- 役割: 対象グループを記録して位置と内容を整え、ホバー計測を加算し、閉じていれば遅延付きで開く。
- 触るとき: 折りたたみグループにホバーしたときの表示の流れを調べるとき。
- 呼び出し先: `Glean.tabgroup.groupInteractions.hover_preview.add()`, `this.#movePanel()`, `this.#updatePanelContent()`
- 条件付き依存: `if (this.#group && this.#group != group)` → `this.#removeGroupListeners()`
- 条件付き依存: `if (this.panelElement.state == "closed")` → `this.panelSet.panelOpener.execute()`
- 条件付き依存: `if (this.panelElement.state == "closed")` → `this.panelSet.shouldActivate()`
- 条件付き依存: `if (this.panelElement.state == "closed")` → `this.#doOpenPanel()`
- 条件付き依存: `if (!(this.panelElement.state == "closed"))` → `this.#addGroupListeners()`
- 参照: `this.#group`, `this.#group.collapsed`, `this.panelElement.state`

## TabGroupPanel.focusPanel()
- 位置: L835-838
- 役割: パネル内の先頭または末尾のボタンにキーボードフォーカスを移す。
- 触るとき: キーボードでグループのプレビューに入る操作を調べるとき。
- 呼び出し先: `this.panelContent.children[childIndex].focus()`
- 参照: `this.panelContent.children`, `this.panelContent.children.length`

## TabGroupPanel.#doOpenPanel()
- 位置: L840-847
- 役割: マウス離脱とコマンドの監視、グループのリスナー登録を行い、ラベル要素を基準にパネルを開く。
- 触るとき: グループ用パネルを実際に開く処理を調べるとき。
- 呼び出し先: `this.#addGroupListeners()`, `this.panelElement.addEventListener()`, `this.panelElement.openPopup()`
- 参照: `this.#popupTarget`, `this.popupOptions`

## TabGroupPanel.#updatePanelContent()
- 位置: L849-880
- 役割: グループ内の各タブを、アイコンとラベル付きのボタンとして作り直し、選択中のタブに印を付けて更新イベントを出す。
- 触るとき: グループのプレビューに並ぶタブ一覧の見た目や内容を変えるとき。
- 呼び出し先: `fragment.appendChild()`, `tabbutton.classList.add()`, `tabbutton.setAttribute()`, `this.panelContent.replaceChildren()`, `this.panelElement.dispatchEvent()`, `this.win.document.createDocumentFragment()`, `this.win.document.createXULElement()`
- 条件付き依存: `if (tab.linkedBrowser)` → `tabbutton.setAttribute()`
- 条件付き依存: `if (tab == this.win.gBrowser.selectedTab)` → `tabbutton.classList.add()`
- 参照: `tab.label`, `tab.linkedBrowser`, `tab.linkedBrowser.currentURI.spec`, `tabbutton.tab`, `this.#group.tabs`, `this.win.gBrowser.selectedTab`

## TabGroupPanel.handleEvent()
- 位置: L882-921
- 役割: ボタン押下でタブを切り替えて閉じ、パネル外へのマウス離脱で閉じ、タブ関連イベントで内容を更新する。
- 触るとき: グループ内タブ切り替え時のアニメーション抑止や更新イベントを調べるとき。
- 条件付き依存: `if (this.win.gBrowser.selectedTab == event.target.tab)` → `this.deactivate()`
- 条件付き依存: `if (event.type == "command")` → `switchingTabs.every()`
- 条件付き依存: `if (switchingTabs.every(tab => tab.group == this.#group))` → `this.win.addEventListener()`
- 条件付き依存: `if (switchingTabs.every(tab => tab.group == this.#group))` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (event.type == "command")` → `this.deactivate()`
- 条件付き依存: `if (!(event.type == "command"))` → `this.hoverTargets.every()`
- 条件付き依存: `if (!(event.type == "command"))` → `target.contains()`
- 条件付き依存: `if ( event.type == "mouseout" && this.hoverTargets.every(target => !target.contains(event.relatedTarget)) )` → `this.deactivate()`
- 条件付き依存: `if (!( event.type == "mouseout" && this.hoverTargets.every(target => !target.contains(event.relatedTarget)) ))` → `TabGroupPanel.PANEL_UPDATE_EVENTS.includes()`
- 条件付き依存: `if (TabGroupPanel.PANEL_UPDATE_EVENTS.includes(event.type))` → `this.#updatePanelContent()`
- 参照: `event.relatedTarget`, `event.target.tab`, `event.type`, `tab.animationsEnabled`, `tab.group`, `this.#group`, `this.win.gBrowser.selectedTab`

## TabGroupPanel.onBeforeHide()
- 位置: L923-928
- 役割: パネルのリスナーとグループのリスナーを解除する。
- 触るとき: 閉じるときのリスナー解除を調べるとき。
- 呼び出し先: `this.#removeGroupListeners()`, `this.panelElement.removeEventListener()`

## TabGroupPanel.hoverTargets()
- 位置: L930-936
- 役割: パネル要素と、あればグループのラベルコンテナーを、ホバー中とみなす対象として返す。
- 触るとき: グループラベルからパネルへ移動しても消えない判定を調べるとき。
- 条件付き依存: `if (this.#popupTarget)` → `targets.push()`
- 参照: `this.#popupTarget`, `this.panelElement`

## TabGroupPanel.popupOptions()
- 位置: L938-963
- 役割: 縦並びか横並びか、RTL か、Nova 有効かに応じて、パネルの表示位置とずれを返す。
- 触るとき: グループ用プレビューの出る位置を調整するとき。
- 参照: `this.panelSet._novaEnabled`, `this.win.RTL_UI`, `this.win.SidebarController._positionStart`, `this.win.gBrowser.tabContainer.verticalMode`

## TabGroupPanel.#popupTarget()
- 位置: L965-967
- 役割: グループのラベルコンテナー要素を返す。
- 触るとき: パネルの基準位置となる要素を調べるとき。
- 参照: `this.#group?.labelContainerElement`

## TabGroupPanel.#addGroupListeners()
- 位置: L969-977
- 役割: グループにプレビュー中の印を付け、更新対象のタブ関連イベントを監視する。
- 触るとき: グループ内の変化でプレビューが更新される仕組みを調べるとき。
- 呼び出し先: `this.#group.addEventListener()`
- 参照: `TabGroupPanel.PANEL_UPDATE_EVENTS`, `this.#group`, `this.#group.hoverPreviewPanelActive`

## TabGroupPanel.#removeGroupListeners()
- 位置: L979-987
- 役割: グループのプレビュー中の印を外し、タブ関連イベントの監視を解除する。
- 触るとき: 監視の解除漏れを調べるとき。
- 呼び出し先: `this.#group.removeEventListener()`
- 参照: `TabGroupPanel.PANEL_UPDATE_EVENTS`, `this.#group`, `this.#group.hoverPreviewPanelActive`

## TabGroupPanel.#movePanel()
- 位置: L989-999
- 役割: 基準要素があれば、パネルをラベルコンテナーの位置へ移動する。
- 触るとき: グループ用パネルの位置ずれを調べるとき。
- 呼び出し先: `this.panelElement.moveToAnchor()`
- 参照: `this.#popupTarget`, `this.popupOptions.position`, `this.popupOptions.x`, `this.popupOptions.y`

## TabNotePanel.constructor()
- 位置: L1009-1035
- 役割: 展開ボタンを設定し、編集アイコンを JS で作って追加し、アイコンのクリックとメモのダブルクリックでメモ編集を開くようにする。
- 触るとき: メモのプレビューの初期化と、編集アイコンを遅延生成する理由を調べるとき。
- 呼び出し先: `actionsContainer.appendChild()`, `editIcon.addEventListener()`, `editIcon.setAttribute()`, `super()`, `this.#openTabNotePanel()`, `this.panelElement .querySelector()`, `this.panelElement .querySelector(".tab-note-preview-expand") .addEventListener()`, `this.panelElement .querySelector(".tab-note-preview-text") .addEventListener()`, `this.panelElement.querySelector()`, `this.win.document.createElement()`
- 参照: `editIcon.className`, `editIcon.dataset.l10nId`, `editIcon.src`, `this.#anchorElement`, `this.#noteExpanded`, `this.#tab`

## TabNotePanel.handleEvent()
- 位置: L1037-1055
- 役割: 表示直前に内容を更新し、タブ属性変更で更新、タブ選択で即時非表示、パネル外へのマウス離脱で非表示にする。
- 触るとき: メモ用プレビューが更新・消去されるイベント条件を調べるとき。
- 呼び出し先: `this.#updatePanelContent()`, `this.deactivate()`, `this.panelElement.addEventListener()`, `this.panelElement.contains()`
- 条件付き依存: `if (!this.panelElement.contains(e.relatedTarget))` → `this.deactivate()`
- 参照: `e.relatedTarget`, `e.target`, `e.type`

## TabNotePanel.activate()
- 位置: L1057-1086
- 役割: 対象タブと基準要素を記録して位置を合わせ、メモを畳み、開いていれば内容更新、閉じていれば遅延付きで開く。
- 触るとき: タブのメモアイコンにホバーしたときの表示の流れを調べるとき。
- 呼び出し先: `originalTab?.removeEventListener()`, `this.#movePanel()`, `this.#tab.addEventListener()`
- 条件付き依存: `if ( this.panelElement.state == "open" || this.panelElement.state == "showing" )` → `this.#updatePanelContent()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.panelOpener.execute()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelSet.shouldActivate()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.openPopup()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.win.addEventListener()`
- 条件付き依存: `if (!( this.panelElement.state == "open" || this.panelElement.state == "showing" ))` → `this.panelElement.addEventListener()`
- 参照: `this.#anchorElement`, `this.#noteExpanded`, `this.#tab`, `this.panelElement.state`, `this.popupOptions`

## TabNotePanel.deactivate()
- 位置: L1093-1106
- 役割: 離れたタブが現在のものなら次フレームで非表示を依頼し、そうでなければ共通の非表示処理を呼ぶ。
- 触るとき: メモアイコンから離れた直後の閉じ方を調べるとき。
- 呼び出し先: `super.deactivate()`
- 条件付き依存: `if (leavingTab)` → `this.win.requestAnimationFrame()`
- 条件付き依存: `if (this.#tab == leavingTab)` → `this.deactivate()`
- 参照: `this.#tab`

## TabNotePanel.onBeforeHide()
- 位置: L1108-1116
- 役割: 各リスナーを解除し、保持情報を破棄して、パネル表示の遅延を一時的にゼロにする。
- 触るとき: メモを閉じた直後に別のパネルが素早く出る理由を調べるとき。
- 呼び出し先: `this.#tab?.removeEventListener()`, `this.panelElement.removeEventListener()`, `this.panelSet.panelOpener.setZeroDelay()`, `this.win.removeEventListener()`
- 参照: `this.#anchorElement`, `this.#tab`

## TabNotePanel.#updatePanelContent()
- 位置: async L1118-1155
- 役割: タブのメモを取得して表示し、はみ出し状態と展開ボタンの幅を更新して、更新イベントを出す(取得中にタブが変わったら中止)。
- 触るとき: メモのプレビューの表示内容や、はみ出しの判定を調べるとき。
- 呼び出し先: `lazy.TabNotes.get()`, `noteTextContainer.style.setProperty()`, `this.#movePanel()`, `this.panelElement.dispatchEvent()`, `this.panelElement.querySelector()`
- 参照: `actionsContainer.offsetWidth`, `currentTab?.canonicalUrl`, `note?.text`, `noteTextContainer.clientHeight`, `noteTextContainer.scrollHeight`, `noteTextContainer.textContent`, `this.#noteOverflow`, `this.#tab`, `this.#tab?.canonicalUrl`

## TabNotePanel.#movePanel()
- 位置: L1157-1166
- 役割: 基準要素があれば、パネルをその位置へ移動する。
- 触るとき: メモ用パネルの位置ずれを調べるとき。
- 条件付き依存: `if (this.#anchorElement)` → `this.panelElement.moveToAnchor()`
- 参照: `this.#anchorElement`, `this.popupOptions.position`, `this.popupOptions.x`, `this.popupOptions.y`

## TabNotePanel.#noteExpanded()
- 位置: L1168-1175
- 役割: メモの展開状態を属性に反映し、展開時にはタブへ展開イベントを送るセッター。
- 触るとき: メモの展開表示やそのテレメトリ用イベントを調べるとき。
- 呼び出し先: `this.panelElement.toggleAttribute()`
- 条件付き依存: `if (val && this.#tab)` → `this.#tab.dispatchEvent()`
- 参照: `this.#tab`

## TabNotePanel.#noteOverflow()
- 位置: L1177-1179
- 役割: メモがはみ出しているかを属性に反映するセッター。
- 触るとき: メモの展開ボタンを出す条件を調べるとき。
- 呼び出し先: `this.panelElement.toggleAttribute()`

## TabNotePanel.#openTabNotePanel()
- 位置: L1181-1186
- 役割: タブメモの編集パネルを開き、このホバーパネルを閉じる。
- 触るとき: プレビューからメモ編集に移る操作を調べるとき。
- 呼び出し先: `this.deactivate()`, `this.win.gBrowser.tabNoteMenu.openPanel()`
- 参照: `lazy.TabNotes.TELEMETRY_SOURCE.TAB_NOTE_PREVIEW_PANEL`, `this.#tab`

## TabNotePanel.popupOptions()
- 位置: L1188-1194
- 役割: メモ用パネルの表示位置とずれ(左下基準、縦に -2)を返す。
- 触るとき: メモ用プレビューの出る位置を調整するとき。

## TabPreviewPanelTimedFunction.constructor()
- 位置: L1220-1235
- 役割: 表示遅延の pref を設定し、ゼロ遅延の持続時間とウィンドウを保持して状態を初期化する。
- 触るとき: パネル表示の遅延実行器の初期化を調べるとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `this.#from`, `this.#target`, `this.#timer`, `this.#useZeroDelay`, `this.#win`, `this.#zeroDelayTime`

## TabPreviewPanelTimedFunction.execute()
- 位置: L1260-1278
- 役割: 指定の処理を遅延後に実行する。タイマーが動作中なら遅延を延ばさず実行内容だけ差し替え、ゼロ遅延中は即時に近く実行する。
- 触るとき: ホバーから表示までの待ち時間や、素早い移動での挙動を調べるとき。
- 呼び出し先: `this.#target()`, `this.#win.setTimeout()`
- 参照: `this.#from`, `this.#target`, `this.#timer`, `this.#useZeroDelay`, `this._prefPreviewDelay`, `this.delayActive`

## TabPreviewPanelTimedFunction.clear()
- 位置: L1292-1298
- 役割: 最後に実行を依頼したパネルからの呼び出しのときだけ、保留中のタイマーを解除する。
- 触るとき: タブとグループを素早く行き来したときに表示が取り消される問題を調べるとき。
- 条件付き依存: `if (from == this.#from && this.#timer)` → `this.#win.clearTimeout()`
- 参照: `this.#from`, `this.#timer`

## TabPreviewPanelTimedFunction.setZeroDelay()
- 位置: L1306-1314
- 役割: 遅延を一定時間だけ無効にし、時間経過後に自動で元へ戻す。
- 触るとき: パネルを閉じた直後に次のパネルが即座に出る仕組みを調べるとき。
- 呼び出し先: `this.#win.setTimeout()`
- 条件付き依存: `if (this.#useZeroDelay)` → `this.#win.clearTimeout()`
- 参照: `this.#useZeroDelay`, `this.#zeroDelayTime`

## TabPreviewPanelTimedFunction.delayActive()
- 位置: L1316-1318
- 役割: 遅延タイマーが動作中かを返すゲッター。
- 触るとき: 遅延中かどうかの判定を調べるとき。
- 参照: `this.#timer`

## TabPreviewPanelTimedFunction.zeroDelayActive()
- 位置: L1320-1322
- 役割: ゼロ遅延が有効かを返すゲッター。
- 触るとき: ゼロ遅延の状態の参照箇所を調べるとき。
- 参照: `this.#useZeroDelay`

## TabPreviewPanelTimedFunction.reset()
- 位置: L1324-1335
- 役割: 遅延タイマーとゼロ遅延のタイマーを解除し、保持している実行内容と呼び出し元も消す。
- 触るとき: 遅延実行器を完全に初期状態に戻す箇所を調べるとき。
- 条件付き依存: `if (this.#timer)` → `this.#win.clearTimeout()`
- 条件付き依存: `if (this.#useZeroDelay)` → `this.#win.clearTimeout()`
- 参照: `this.#from`, `this.#target`, `this.#timer`, `this.#useZeroDelay`
