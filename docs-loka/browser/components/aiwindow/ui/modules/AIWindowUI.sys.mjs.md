# browser/components/aiwindow/ui/modules/AIWindowUI.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindowUI.sys.mjs
source-hash: d24f44e2668d56df7b9f83dff3eb186bda61bfce
lines: 829

## <module>
- 役割: Smart Window のサイドバーの表示と開閉、サイドバー内の ai-window への入力・モデル・チップの反映をまとめる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## _getSidebarElements()
- 位置: L44-56
- 役割: ウィンドウ内のサイドバーの box と splitter を ID で取り出す。どちらかがなければ null を返す。
- 触るとき: サイドバーの DOM が見つからない不具合を調べるとき、要素 ID を変えるとき。
- 呼び出し先: `chromeDoc.getElementById()`
- 参照: `this.BOX_ID`, `this.SPLITTER_ID`, `win.document`

## updateSidebarMaxWidth()
- 位置: L63-83
- 役割: ウィンドウ幅と CSS 変数の比からサイドバーの最大幅を設定し、初回のみリサイズ時の再計算を登録する。
- 触るとき: サイドバーの最大幅の計算式や、ウィンドウのリサイズへの追従を変えるとき。
- 呼び出し先: `Math.round()`, `gSidebarWidthHandlers.has()`, `nodes.box.style.setProperty()`, `parseFloat()`, `this._getSidebarElements()`, `win .getComputedStyle()`, `win .getComputedStyle(win.document.documentElement) .getPropertyValue()`
- 条件付き依存: `if (!gSidebarWidthHandlers.has(win))` → `gSidebarWidthHandlers.set()`
- 条件付き依存: `if (!gSidebarWidthHandlers.has(win))` → `win.addEventListener()`
- 参照: `win.document.documentElement`, `win.innerWidth`

## sidebarResizeHandler()
- 位置: L79-79
- 役割: ウィンドウのリサイズ時に updateSidebarMaxWidth を呼び直すハンドラー。
- 触るとき: リサイズ時にサイドバーの最大幅がずれる不具合を調べるとき。
- 呼び出し先: `this.updateSidebarMaxWidth()`

## _removeSidebarWidthHandler()
- 位置: L90-96
- 役割: ウィンドウに登録したリサイズ用のハンドラーを外し、記録からも消す。
- 触るとき: サイドバーを閉じた後もリサイズ監視が残る不具合を調べるとき。
- 呼び出し先: `gSidebarWidthHandlers.get()`
- 条件付き依存: `if (handler)` → `win.removeEventListener()`
- 条件付き依存: `if (handler)` → `gSidebarWidthHandlers.delete()`

## _getConversationFromSidebar()
- 位置: L102-108
- 役割: サイドバーで選ばれている会話の id とメッセージ数を返す。会話がなければ空文字と 0。
- 触るとき: サイドバーの計測イベントに載せる会話の情報を変えるとき。
- 呼び出し先: `AIWindow.getActiveConversation()`
- 参照: `conversation?.id`, `conversation?.messageCount`

## ensureBrowserIsAppended()
- 位置: L117-142
- 役割: サイドバーに ai-window 用の browser 要素がなければ作ってスタックに追加し、あれば既存の要素を返す。
- 触るとき: サイドバーの browser の生成条件や属性(src、tooltip など)を変えるとき。
- 呼び出し先: `box.querySelector()`, `browser.setAttribute()`, `chromeDoc.createXULElement()`, `chromeDoc.getElementById()`, `stack.appendChild()`
- 条件付き依存: `if (!stack.isConnected)` → `stack.setAttribute()`
- 条件付き依存: `if (!stack.isConnected)` → `box.appendChild()`
- 参照: `browser.id`, `stack.className`, `stack.isConnected`, `this.BROWSER_ID`, `this.STACK_CLASS`

## isSidebarOpen()
- 位置: L148-156
- 役割: サイドバーが開いているかを返す。閉じるアニメーションの途中では、記録した意図の状態を優先する。
- 触るとき: 開閉の判定を変えるとき、閉じる途中で開閉判定がずれる不具合を調べるとき。
- 呼び出し先: `this._getSidebarElements()`
- 参照: `nodes.box._aiWindowOpen`, `nodes.box.collapsed`

## _setSidebarCollapsed()
- 位置: L176-200
- 役割: 開閉の意図を記録し、内容領域の属性と最大幅を更新する。動きが必要なら滑らせ、不要か動きの軽減が有効なら即時に反映する。
- 触るとき: サイドバーの開閉を即時にするか滑らせるかを変えるとき、動きの軽減の扱いを確かめるとき。
- 呼び出し先: `this._animateSidebarToggle()`, `win.document .getElementById()`, `win.document .getElementById("tabbrowser-tabbox") .toggleAttribute()`, `win.matchMedia()`
- 条件付き依存: `if (!collapse)` → `this.updateSidebarMaxWidth()`
- 条件付き依存: `if (!(!collapse))` → `this._removeSidebarWidthHandler()`
- 条件付き依存: `if (!animate || reduceMotion)` → `this._cancelSidebarAnimation()`
- 条件付き依存: `if (!animate || reduceMotion)` → `this._commitSidebarCollapsed()`
- 参照: `box._aiWindowOpen`, `win.matchMedia( "(prefers-reduced-motion: reduce)" ).matches`

## _commitSidebarCollapsed()
- 位置: L202-209
- 役割: アニメーション用のスタイルを消し、box と splitter の collapsed を設定する。開くときは親要素も表示する。
- 触るとき: 開閉の最終状態が反映されない不具合を調べるとき。
- 呼び出し先: `this._clearSidebarAnimationStyles()`
- 参照: `box.collapsed`, `box.parentElement.collapsed`, `splitter.collapsed`

## _clearSidebarAnimationStyles()
- 位置: L211-220
- 役割: box の位置指定に使ったインラインスタイルと、親の overflow を空に戻す。
- 触るとき: アニメーションの後に位置のスタイルが残る不具合を調べるとき。
- 参照: `box.parentElement.style.overflow`, `box.style.bottom`, `box.style.left`, `box.style.position`, `box.style.right`, `box.style.top`, `box.style.width`

## _cancelSidebarAnimation()
- 位置: L222-228
- 役割: box に進行中の Web Animation があれば止め、記録から消す。
- 触るとき: 開閉の途中で別の操作が入ったときの挙動を変えるとき。
- 呼び出し先: `gSidebarAnimations.get()`
- 条件付き依存: `if (animations)` → `gSidebarAnimations.delete()`
- 条件付き依存: `if (animations)` → `animations.forEach()`
- 条件付き依存: `if (animations)` → `animation.cancel()`

## _animateSidebarToggle()
- 位置: L230-307
- 役割: box と内容領域を Web Animation で滑らせ、終わったら collapsed を確定させる。サイドバーが右か左かで方向と切り抜き量を決める。
- 触るとき: サイドバーの開閉アニメーションの見た目や時間、方向の判定を変えるとき。
- 呼び出し先: `Promise.allSettled()`, `Promise.allSettled(animations.map(animation => animation.finished)).then()`, `animations.map()`, `box.animate()`, `box.getBoundingClientRect()`, `browserEl.getBoundingClientRect()`, `gSidebarAnimations.delete()`, `gSidebarAnimations.get()`, `gSidebarAnimations.set()`, `parseFloat()`, `tabbox.animate()`, `tabbox.getBoundingClientRect()`, `this._cancelSidebarAnimation()`, `this._clearSidebarAnimationStyles()`, `this._commitSidebarCollapsed()`, `win.document.getElementById()`, `win.getComputedStyle()`
- 条件付き依存: `if (boxRect.width <= 0 || clipAmount <= 0)` → `this._commitSidebarCollapsed()`
- 参照: `animation.finished`, `box.collapsed`, `box.parentElement`, `box.style`, `box.style.bottom`, `box.style.position`, `box.style.top`, `box.style.width`, `boxRect.bottom`, `boxRect.left`, `boxRect.right`, `boxRect.top`, `boxRect.width`, `browserEl.collapsed`, `browserEl.style.overflow`, `browserRect.bottom`, `browserRect.left`, `browserRect.right`, `browserRect.top`, `browserStyle.paddingLeft`, `browserStyle.paddingRight`, `splitter.collapsed`, `tabboxRect.left`, `tabboxRect.right`, `this.SIDEBAR_ANIMATION_MS`

## openInFullWindow()
- 位置: L315-326
- 役割: サイドバーを閉じ、会話 id を属性に入れ、全画面の ai-window へ OpenConversation イベントを送って会話を開く。
- 触るとき: サイドバーの会話を全画面チャットへ移す処理を変えるとき。
- 呼び出し先: `browser.setAttribute()`, `contentDocument.dispatchEvent()`, `this.closeSidebar()`
- 参照: `browser.contentWindow.CustomEvent`, `browser.documentGlobal`, `conversation.id`

## reopenConversationInTab()
- 位置: L336-349
- 役割: 会話で最後に見たページ(なければ新規タブ)を指定の場所に開き、ブラウザーができたら会話を復元する。
- 触るとき: 最近のチャットを別のタブや新しいウィンドウで開く動きを変えるとき。
- 呼び出し先: `conversation.getMostRecentPageVisited()`, `lazy.URILoadingHelper.openTrustedLinkIn()`
- 参照: `mostRecentPage?.href`, `win.BROWSER_NEW_TAB_URL`

## resolveOnContentBrowserCreated()
- 位置: async L340-347
- 役割: 開かれたブラウザーに、新規タブなら全画面で会話を開き、それ以外なら会話を復元してサイドバーでも開く。
- 触るとき: 最近のチャットを開いた後の表示先の振り分けを変えるとき。
- 条件付き依存: `if (url === win.BROWSER_NEW_TAB_URL)` → `this.openInFullWindow()`
- 条件付き依存: `if (!(url === win.BROWSER_NEW_TAB_URL))` → `AIWindow.restoreTabConversation()`
- 条件付き依存: `if (!(url === win.BROWSER_NEW_TAB_URL))` → `this.openSidebar()`
- 参照: `targetBrowser.documentGlobal`, `win.BROWSER_NEW_TAB_URL`

## openSidebar()
- 位置: async L361-414
- 役割: サイドバーを即時に開き、会話があれば開き、なければ新しい会話を作る。開いたことを sidebar-toggle イベントで通知し、閉じた計測の対象にもする。
- 触るとき: サイドバーを開く全経路の挙動、特に会話の指定と計測の値を変えるとき。
- 呼び出し先: `Glean.smartWindow.sidebarOpen.record()`, `aiWindowElement.onCreateNewChatClick()`, `this._getSidebarElements()`, `this.ensureBrowserIsAppended()`, `this.getAiWindowElement()`, `this.isSidebarOpen()`, `win.dispatchEvent()`
- 条件付き依存: `if (!this.isSidebarOpen(win))` → `this._setSidebarCollapsed()`
- 条件付き依存: `if (!this.isSidebarOpen(win))` → `this._updateAskButtonChecked()`
- 条件付き依存: `if (conversation)` → `aiBrowser.setAttribute()`
- 条件付き依存: `if (!(conversation))` → `aiBrowser.removeAttribute()`
- 条件付き依存: `if (conversation)` → `aiWindowElement.openConversation()`
- 参照: `conversation.id`, `conversation?.id`, `conversation?.messageCount`, `win.CustomEvent`, `win.document`, `win.gBrowser.selectedTab`

## getAiWindowElement()
- 位置: async L425-435
- 役割: サイドバーの browser の中で ai-window のカスタム要素が定義されるまで 50ms 間隔で待つ。AI_WINDOW_ELEMENT_TIMEOUT(1.5秒)で打ち切る。
- 触るとき: サイドバーの読み込みが遅く要素が見つからない不具合を調べるとき、待ち時間を変えるとき。
- 呼び出し先: `Date.now()`, `aiBrowser.contentDocument?.querySelector()`, `win.setTimeout()`
- 参照: `AIWindowUI.AI_WINDOW_ELEMENT_TIMEOUT`

## focusSidebar()
- 位置: async L437-452
- 役割: サイドバーが開いていれば browser にフォーカスし、ai-window ができたらスマートバーへフォーカスを移す。
- 触るとき: サイドバーを開いた後のフォーカスの位置を変えるとき。
- 呼び出し先: `aiBrowser.focus()`, `aiWindowElement.focusSmartbar()`, `this.getAiWindowElement()`, `this.isSidebarOpen()`, `win.document.getElementById()`
- 参照: `this.BROWSER_ID`

## closeSidebar()
- 位置: L463-490
- 役割: サイドバーを閉じる。ユーザーのトグル操作の時だけ滑らせ、sidebar-toggle イベントと閉じた計測を発する。
- 触るとき: サイドバーを閉じる経路の演出や計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.sidebarClose.record()`, `this._getConversationFromSidebar()`, `this._getSidebarElements()`, `this._setSidebarCollapsed()`, `this._updateAskButtonChecked()`, `this.isSidebarOpen()`, `win.dispatchEvent()`
- 参照: `win.CustomEvent`, `win.gBrowser?.selectedTab`

## toggleGroupTabsPanel()
- 位置: L499-501
- 役割: タブ整理パネル(AutoTabGrouping)の開閉を AutoTabGrouping に任せる。
- 触るとき: タブ整理パネルの入口を追うとき。
- 呼び出し先: `lazy.AutoTabGrouping.toggleGroupTabsPanel()`

## toggleMonitorPanel()
- 位置: L508-510
- 役割: モニターパネルの開閉を MonitorPanel に任せる。
- 触るとき: モニターパネルの入口を追うとき。
- 呼び出し先: `lazy.MonitorPanel.toggleMonitorPanel()`

## showMonitorCreateForm()
- 位置: L517-519
- 役割: モニターパネルを作成フォームの状態で開く。
- 触るとき: モニター作成の入口を変えるとき。
- 呼び出し先: `lazy.MonitorPanel.showCreateForm()`

## toggleSidebar()
- 位置: L527-557
- 役割: 開いていれば閉じ、閉じていれば開いてスマートバーにフォーカスする。開いたかどうかを返す。
- 触るとき: Ask ボタンでの開閉の挙動を変えるとき。
- 呼び出し先: `this._getSidebarElements()`, `this._setSidebarCollapsed()`, `this._updateAskButtonChecked()`, `this.ensureBrowserIsAppended()`, `this.focusSidebar()`, `this.isSidebarOpen()`, `win.dispatchEvent()`
- 条件付き依存: `if (this.isSidebarOpen(win))` → `this.closeSidebar()`
- 参照: `win.CustomEvent`, `win.gBrowser?.selectedTab`

## restoreMemoriesState()
- 位置: L565-572
- 役割: メモリーのアイコンの状態を、サイドバーか指定タブの全画面 ai-window の会話に合わせて戻す。
- 触るとき: メモリーの表示が切り替え後に元に戻らない不具合を調べるとき。
- 呼び出し先: `tab.linkedBrowser?.contentDocument?.querySelector()`, `this._getSidebarAiWindow()`
- 条件付き依存: `if (aiWindowEl)` → `aiWindowEl.syncSmartbarMemoriesStateFromConversation()`

## _updateAskButtonChecked()
- 位置: L580-586
- 役割: Ask ボタンの aria-expanded を、サイドバーの開閉に合わせて設定する。
- 触るとき: Ask ボタンの状態表示やアクセシビリティ属性を変えるとき。
- 呼び出し先: `String()`, `askBtn.setAttribute()`, `win.document.querySelector()`

## moveFullPageToSidebar()
- 位置: async L595-628
- 役割: 全画面の ai-window の会話 id から会話を引き、サイドバーで開いてフォーカスする。
- 触るとき: 全画面チャットをサイドバーへ移す操作を変えるとき。
- 呼び出し先: `AIWindow.isAIWindowContentPage()`, `fullPageBrowser.contentDocument?.querySelector()`, `nodes.chromeDoc.getElementById()`, `this._getSidebarElements()`, `this.focusSidebar()`, `this.openSidebar()`
- 条件付き依存: `if (conversationId)` → `AIWindow.chatStore.findConversationById()`
- 参照: `aiWindowEl?.conversationId`, `fullPageBrowser.currentURI`, `fullPageBrowser?.currentURI`, `tab.linkedBrowser`, `this.BROWSER_ID`

## updateSidebarInput()
- 位置: L638-649
- 役割: サイドバーが開いていれば、ai-window にスマートバーの入力状態を渡す。
- 触るとき: サイドバーに入力を反映させる経路を追うとき。
- 呼び出し先: `aiWindowEl.updateInput()`, `this._getSidebarAiWindow()`, `this.isSidebarOpen()`
- 参照: `aiWindowEl?.updateInput`

## updateSidebarModel()
- 位置: L658-669
- 役割: サイドバーが開いていれば、ai-window にタブごとのモデル選択を渡す。null なら既定のモデルになる。
- 触るとき: タブごとのモデル選択がサイドバーに反映されない不具合を調べるとき。
- 呼び出し先: `aiWindowEl.restoreModelChoiceOverride()`, `this._getSidebarAiWindow()`, `this.isSidebarOpen()`
- 参照: `aiWindowEl?.restoreModelChoiceOverride`

## updateSidebarContextChips()
- 位置: L679-694
- 役割: サイドバーが開いていれば、ai-window にコンテキストチップと暗黙チップの削除状態を渡す。
- 触るとき: チップの復元や表示を変えるとき。
- 呼び出し先: `aiWindowEl.restoreContextChips()`, `this._getSidebarAiWindow()`, `this.isSidebarOpen()`
- 参照: `aiWindowEl?.restoreContextChips`

## updateStarterPrompts()
- 位置: L707-714
- 役割: モードに応じた ai-window を選び、開始プロンプトを読み込む。clear が true なら先に消す。
- 触るとき: 空のチャットに開始プロンプトが出ない不具合を調べるとき、読み込みの順序を変えるとき。
- 呼び出し先: `aiWindow.loadStarterPrompts()`, `this._getActiveAiWindow()`
- 参照: `win.gBrowser.selectedTab`

## _getSidebarAiWindow()
- 位置: L723-730
- 役割: サイドバーが開いていれば、その browser の中の ai-window 要素を返す。閉じていれば null。
- 触るとき: サイドバーの ai-window を操作する前提条件を変えるとき。
- 呼び出し先: `aiWindowBrowser?.contentDocument?.querySelector()`, `this.isSidebarOpen()`, `win.document.getElementById()`
- 参照: `this.BROWSER_ID`

## _getActiveAiWindow()
- 位置: L743-755
- 役割: モードが sidebar ならサイドバーの、fullpage なら指定タブの ai-window を返す。それ以外は null。
- 触るとき: イベントの送り先の ai-window の選び方を変えるとき。
- 条件付き依存: `if (mode === "sidebar")` → `this._getSidebarAiWindow()`
- 条件付き依存: `if (mode === "fullpage" && tab)` → `tab.linkedBrowser.contentDocument.querySelector()`

## _getFadeTarget()
- 位置: L757-760
- 役割: タブパネルのうち選択中のパネルを返す。
- 触るとき: タブ切り替え時のフェードの対象を変えるとき。
- 呼び出し先: `win?.document?.getElementById()`
- 参照: `tabPanels?.selectedPanel`

## _prefersReducedMotion()
- 位置: L762-764
- 役割: 動きの軽減(prefers-reduced-motion)が指定されているかを返す。
- 触るとき: 動きを減らす設定の判定を変えるとき。
- 呼び出し先: `win?.matchMedia()`
- 参照: `win?.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches`

## _fadeToOpacity()
- 位置: L766-787
- 役割: 要素の opacity を指定値へ CSS transition で変え、transitionend か タイムアウトで resolve する。
- 触るとき: フェードの時間や終了判定を変えるとき。
- 呼び出し先: `String()`, `el.addEventListener()`, `el.removeEventListener()`, `resolve()`, `win.setTimeout()`
- 参照: `el.style.opacity`, `el.style.transition`, `this.TAB_FADE_MS`, `this.TAB_FADE_TIMEOUT_MS`

## onEnd()
- 位置: L768-775
- 役割: transitionend のうち opacity の終了を受けて、タイマーを解除しリスナーを外し resolve する。
- 触るとき: フェードが途中で終わらない、または待ち続ける不具合を調べるとき。
- 呼び出し先: `el.removeEventListener()`, `resolve()`, `win.clearTimeout()`
- 参照: `event.propertyName`

## _runTabPanelsFade()
- 位置: async L789-811
- 役割: 動きの軽減が無効なら、タブパネルを 0.25 まで薄くしてから 1 に戻す。終わったら元の transition と opacity に戻す。
- 触るとき: 同じページへのリンク移動時の点滅の見た目や長さを変えるとき。
- 呼び出し先: `target.getBoundingClientRect()`, `this._fadeToOpacity()`, `this._getFadeTarget()`, `this._prefersReducedMotion()`
- 参照: `target.style.opacity`, `target.style.transition`

## handleSameLinkClick()
- 位置: L818-827
- 役割: 引用リンクが現在のページと同じときに、タブパネルのフェードを1回だけ実行する。実行中の同じウィンドウへは重ねて実行しない。
- 触るとき: 現在のページへの引用リンクを押したときの反応を変えるとき。
- 呼び出し先: `gFadingWindows.add()`, `gFadingWindows.delete()`, `gFadingWindows.has()`, `this._runTabPanelsFade()`, `this._runTabPanelsFade(win).finally()`
