# browser/components/aiwindow/ui/modules/AIWindow.sys.mjs

source: browser/components/aiwindow/ui/modules/AIWindow.sys.mjs
source-hash: 75005a4dad5fc61e8da004ff3bc483239b3bb2fe
lines: 1731

## <module>
- 役割: AI ウィンドウ機能の本体。起動、ウィンドウの切り替え、ウィジェット登録、利用計測、機能の有効可否を一か所で管理する
- 呼び出し先: `AIWindow._forEachWindow()`, `AIWindow._onAIWindowEnabledPrefChange.bind()`, `AIWindow._startSchedulers()`, `AIWindow._updateGroupTabsWidgetRegistration()`, `AIWindow._updateMonitorButtonForWindow()`, `AIWindow._updateMonitorWidgetRegistration()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.setPrototypeOf()`, `Services.io.newURI()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## init()
- 位置: L166-222
- 役割: ウィンドウごとの初期化(ボタン位置、タブ状態管理、スケジューラ開始)と、全体で一度だけの購読を行う
- 触るとき: 起動時に何が張られ、ウィンドウが開いたときに何が動くかを追うとき
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `lazy.NimbusFeatures.smartWindow.onUpdate()`, `lazy.PlacesUtils.observers.addListener()`, `lazy.SmartWindowTelemetry.init()`, `lazy.getAllModelsData()`, `this._aiWindowTabStateManagers.has()`, `this._updateGroupTabsWidgetRegistration()`, `this._updateMonitorWidgetRegistration()`, `this._updateSwitcherWidgetRegistration()`, `this._windowStates.has()`, `this.isAIWindowActive()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._windowStates.set()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._updateHamburgerMenuPosition()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._initializeAskButtonOnToolbox()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (!this._windowStates.has(win))` → `windowArgs.hasKey()`
- 条件付き依存: `if ( windowArgs instanceof Ci.nsIPropertyBag2 && windowArgs.hasKey("aiwindow-trigger") )` → `this.recordOpenWindowTelemetry()`
- 条件付き依存: `if ( windowArgs instanceof Ci.nsIPropertyBag2 && windowArgs.hasKey("aiwindow-trigger") )` → `windowArgs.getPropertyAsAString()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `this._aiWindowTabStateManagers.set()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `this._markActiveStart()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `win.delayedStartupPromise.then()`
- 条件付き依存: `if ( !this._aiWindowTabStateManagers.has(win) && this.isAIWindowActive(win) )` → `this._startSchedulers()`
- 参照: `Ci.nsIPropertyBag2`, `lazy.AIWindowTabStatesManager`, `lazy.ChatStore`, `lazy.ONLOGOUT_NOTIFICATION`, `this._initialized`, `this.handlePlacesEvents`, `this.onNimbusUpdate`, `win?.arguments`
- XPCOM: [`nsIPropertyBag2`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.obs` / `Services.prefs`

## _startSchedulers()
- 位置: L224-227
- 役割: 記憶のスケジューラと利用計測のスケジューラを開始する
- 触るとき: 定期処理がいつ動き出すか、起動条件を変えるとき
- 呼び出し先: `lazy.MemoriesSchedulers.maybeRunAndSchedule()`, `lazy.TelemetryScheduler.maybeInit()`

## handlePlacesEvents()
- 位置: L229-248
- 役割: 履歴の削除やクリアを受けて、チャットのメッセージから該当 URL を消す
- 触るとき: 履歴削除が会話の内容にどう反映されるかを調べるとき
- 呼び出し先: `lazy.ChatStore.deleteAllUrlsFromMessages()`
- 条件付き依存: `if ( event.reason == PlacesVisitRemoved.REASON_DELETED && !event.isPartialVisistsRemoval )` → `lazy.ChatStore.deleteUrlFromMessages()`
- 参照: `PlacesVisitRemoved.REASON_DELETED`, `event.isPartialVisistsRemoval`, `event.reason`, `event.type`, `event.url`

## uninit()
- 位置: L250-267
- 役割: init で張った購読(監視、Places、Nimbus)を解除し、初期化済みフラグを戻す
- 触るとき: 終了時や再初期化時の後始末に漏れがないか確認するとき
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`, `lazy.NimbusFeatures.smartWindow.offUpdate()`, `lazy.PlacesUtils.observers.removeListener()`
- 参照: `lazy.ONLOGOUT_NOTIFICATION`, `this._initialized`, `this.handlePlacesEvents`, `this.onNimbusUpdate`
- XPCOM: `Services.obs` / `Services.prefs`

## onNimbusUpdate()
- 位置: L269-273
- 役割: Nimbus の enabled 変数が真なら browser.smartwindow.enabled を true にする
- 触るとき: 実験側から機能を有効にする経路を変えるとき
- 呼び出し先: `lazy.NimbusFeatures.smartWindow.getVariable()`
- 条件付き依存: `if (lazy.NimbusFeatures.smartWindow.getVariable("enabled"))` → `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## observe()
- 位置: L275-291
- 役割: ログアウト、タブ帯の向き、リージョン変更、監視の通知を受けて対応する処理に振り分ける
- 触るとき: 通知の種類ごとの反応を追加・変更するとき
- 条件付き依存: `if (topic === lazy.ONLOGOUT_NOTIFICATION)` → `this._onAccountLogout()`
- 条件付き依存: `if (topic === "tabstrip-orientation-change")` → `this._onTabstripOrientationChange()`
- 条件付き依存: `if ( topic === "browser-region-updated" || topic === "nsPref:changed" )` → `this._updateMonitorWidgetRegistration()`
- 条件付き依存: `if (topic === lazy.MONITOR_CONDITION_MET_TOPIC)` → `this.showMonitorAttention()`
- 条件付き依存: `if (topic === lazy.MONITOR_RUN_FAILED_TOPIC)` → `this.showMonitorErrorAttention()`
- 参照: `lazy.MONITOR_CONDITION_MET_TOPIC`, `lazy.MONITOR_RUN_FAILED_TOPIC`, `lazy.ONLOGOUT_NOTIFICATION`

## _onAccountLogout()
- 位置: L295-301
- 役割: ログアウト時に開いている AI ウィンドウをすべて通常ウィンドウに戻す
- 触るとき: サインアウト時の挙動を変えるとき
- 呼び出し先: `Services.wm.getEnumerator()`, `this.isAIWindowActive()`
- 条件付き依存: `if (!win.closed && this.isAIWindowActive(win))` → `this.toggleAIWindow()`
- 参照: `win.closed`
- XPCOM: `Services.wm`

## hasActiveAIWindows()
- 位置: L306-313
- 役割: 利用可能な AI ウィンドウが 1 つでも開いていれば真を返す
- 触るとき: サインアウト時の警告を出すかどうかを判定する箇所を調べるとき
- 呼び出し先: `Services.wm.getEnumerator()`, `this.isAIWindowActiveAndEnabled()`
- 参照: `win.closed`
- XPCOM: `Services.wm`

## _reconcileNewTabPages()
- 位置: L315-354
- 役割: 新規タブ、about:home、ホームページのタブを、AI ウィンドウの新規タブ URL へ差し替える
- 触るとき: 切り替え時に既存タブがどう置き換わるかを変えるとき
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `currentURI.equalsExceptRef()`, `homePagePrefURIs.some()`, `lazy.HomePage.parseCustomHomepageURLs()`, `lazy.HomePage.parseCustomHomepageURLs( homePagePref ).flatMap()`
- 条件付き依存: `if ( currentURI.equalsExceptRef(newTabPrefURI) || currentURI.equalsExceptRef(aboutNewTabURI) || currentURI.equalsExceptRef(aboutHomeURI) || homePagePrefURIs.some...)` → `this.hasActiveChatInBrowser()`
- 条件付き依存: `if ( currentURI.equalsExceptRef(newTabPrefURI) || currentURI.equalsExceptRef(aboutNewTabURI) || currentURI.equalsExceptRef(aboutHomeURI) || homePagePrefURIs.some...)` → `browser.loadURI()`
- 参照: `browser.currentURI`, `browser?.currentURI`, `tab.linkedBrowser`, `win.BROWSER_NEW_TAB_URL`, `win.gBrowser.tabs`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## hasActiveChatInBrowser()
- 位置: L356-363
- 役割: ブラウザ内の ai-window 要素が chat-active なら真を返す
- 触るとき: チャット表示中のタブを新規タブ差し替えから除外する条件を調べるとき
- 呼び出し先: `aiWindowElement.classList.contains()`, `browser?.contentDocument?.querySelector()`

## _forEachWindow()
- 位置: L365-373
- 役割: 管理中の生きているウィンドウそれぞれに関数を適用する
- 触るとき: 全ウィンドウに一括で更新をかける処理を追加・確認するとき
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`, `ChromeUtils.nondeterministicGetWeakMapKeys(this._windowStates).forEach()`
- 条件付き依存: `if (win && !win.closed)` → `callback()`
- 参照: `this._windowStates`, `win.closed`

## _onAIWindowEnabledPrefChange()
- 位置: L375-390
- 役割: 有効設定が変わったら各ウィジェットとボタンを更新し、無効化時はログアウト扱いにする
- 触るとき: 機能の有効・無効切り替えに伴う後片付けを変えるとき
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.CustomizableUI.getWidget()`, `this._updateButtonVisibility()`, `this._updateGroupTabsWidgetRegistration()`, `this._updateMonitorWidgetRegistration()`, `this._updateSwitcherWidgetRegistration()`
- 条件付き依存: `if (!this.isAvailable)` → `this._onAccountLogout()`
- 参照: `this.isAvailable`, `widget?.instances`
- XPCOM: `Services.prefs`

## _updateButtonVisibility()
- 位置: L392-396
- 役割: ボタンを、AI ウィンドウが有効な時だけ表示する
- 触るとき: 切り替えボタンの表示条件を変えるとき
- 条件付き依存: `if (node)` → `this.isAIWindowEnabled()`
- 参照: `node.hidden`

## _onTabstripOrientationChange()
- 位置: L398-400
- 役割: タブ帯の向きが変わったとき、全ウィンドウでハンバーガーメニューの位置を更新する
- 触るとき: 縦タブ切り替え時のメニュー位置の不具合を調べるとき
- 呼び出し先: `this._forEachWindow()`, `this._updateHamburgerMenuPosition()`

## _updateHamburgerMenuPosition()
- 位置: L412-430
- 役割: AI ウィンドウか縦タブ時はメニューをタイトルバー横へ移し、切り替え中は標準の位置へ戻す
- 触るとき: メニューボタンの位置やタブ帯との関係を変えるとき
- 呼び出し先: `targetToolbar.querySelector()`, `this.isAIWindowActive()`, `win.document.getElementById()`
- 条件付き依存: `if (this.isAIWindowActive(win) || this.verticalTabsEnabled)` → `titlebarContainer.after()`
- 条件付き依存: `if (isToggling)` → `win.document .getElementById("nav-bar") .querySelector()`
- 条件付き依存: `if (isToggling)` → `win.document .getElementById()`
- 条件付き依存: `if (isToggling)` → `postTabsSpacer.before()`
- 参照: `this.verticalTabsEnabled`

## _initializeAskButtonOnToolbox()
- 位置: L435-441
- 役割: ツールボックスの「質問」ボタンを、AI ウィンドウでなければ隠す
- 触るとき: 質問ボタンの表示条件を変えるとき
- 呼び出し先: `this.isAIWindowActive()`, `win.document.getElementById()`
- 参照: `askButton.hidden`

## _updateGroupTabsButtonVisibility()
- 位置: L449-461
- 役割: AI ウィンドウかつ自動グループ化が有効なときだけ整理ボタンを出し、表示時にモデルを先読みする
- 触るとき: 整理ボタンの表示条件や先読みのタイミングを変えるとき
- 呼び出し先: `this.isAIWindowActive()`
- 条件付き依存: `if (!node.hidden)` → `lazy.AutoTabGroupingSuggestions.preloadModels()`
- 参照: `lazy.AutoTabGroupingSuggestions.isAvailable`, `lazy.autoTabGroupingEnabled`, `node.documentGlobal`, `node.hidden`

## monitorButtonEnabled()
- 位置: L472-479
- 役割: AI ウィンドウ有効、エージェント有効、ツールバー有効、地域対応の 4 条件が揃うと真
- 触るとき: 監視ボタンを出す条件を追加・変更するとき
- 呼び出し先: `lazy.MonitorUIUtils.isMonitorRegionSupported()`, `this.isAIWindowEnabled()`
- 参照: `lazy.agentEnabled`, `lazy.agentToolbarEnabled`

## _updateMonitorWidgetRegistration()
- 位置: L485-491
- 役割: 監視ボタンが有効で遮断されていなければ登録し、そうでなければ破棄する
- 触るとき: 監視ボタンの登録・破棄の判定を変えるとき
- 呼び出し先: `this._destroyMonitorWidget()`
- 条件付き依存: `if (this.monitorButtonEnabled && !this.isBlocked)` → `this._createMonitorWidget()`
- 参照: `this.isBlocked`, `this.monitorButtonEnabled`

## _createMonitorWidget()
- 位置: L493-520
- 役割: 監視ボタン(CustomizableUI)を作り、監視の通知を購読する
- 触るとき: 監視ボタンの属性や押したときの動作を変えるとき
- 呼び出し先: `Services.obs.addObserver()`, `lazy.CustomizableUI.createWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.MONITOR_CONDITION_MET_TOPIC`, `lazy.MONITOR_RUN_FAILED_TOPIC`, `this._monitorWidgetCreated`
- XPCOM: `Services.obs`

## onCreated()
- 位置: L504-512
- 役割: 作られた監視ボタンに ARIA 属性、バッジ、表示状態、注意表示を設定する
- 触るとき: 監視ボタンの初期属性や注意マークの扱いを変えるとき
- 呼び出し先: `node.setAttribute()`, `this._shouldShowMonitorButton()`, `this._updateMonitorAttentionForNode()`
- 参照: `node.documentGlobal`, `node.hidden`

## onCommand()
- 位置: L513-515
- 役割: 監視ボタンの押下で監視パネルを開く
- 触るとき: 監視パネルの開き方を変えるとき
- 呼び出し先: `lazy.AIWindowUI.toggleMonitorPanel()`
- 参照: `event.view`

## _destroyMonitorWidget()
- 位置: L522-531
- 役割: 監視の通知購読を外し、監視ボタンを CustomizableUI から破棄する
- 触るとき: 監視機能を無効にしたときのボタン撤去を確認するとき
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.CustomizableUI.destroyWidget()`
- 参照: `lazy.MONITOR_CONDITION_MET_TOPIC`, `lazy.MONITOR_RUN_FAILED_TOPIC`, `this._monitorWidgetCreated`
- XPCOM: `Services.obs`

## _updateMonitorButtonForWindow()
- 位置: L540-547
- 役割: ウィンドウごとに監視ボタンの表示と注意表示を更新する
- 触るとき: クラシックウィンドウでボタンが出ないことを保つ判定を変えるとき
- 呼び出し先: `this._shouldShowMonitorButton()`, `this._updateMonitorAttentionForNode()`, `win.document.getElementById()`
- 参照: `button.hidden`

## monitorAttentionIds()
- 位置: L556-558
- 役割: 条件に一致した監視の ID 一覧を返す
- 触るとき: パネルで強調する監視の決まり方を調べるとき
- 参照: `lazy.MonitorAttention.matchedIds`

## hasMonitorAnnouncement()
- 位置: L567-569
- 役割: 監視機能の「新着」告知が出ているかを返す
- 触るとき: 告知の出し方や表示期間を変えるとき
- 参照: `lazy.monitorAnnouncement`

## hasMonitorAttention()
- 位置: L577-579
- 役割: 一致・失敗の注意、または告知があれば真を返す(ボタンの点の表示判定)
- 触るとき: 監視ボタンの点を出す条件を変えるとき
- 参照: `lazy.MonitorAttention.hasAttention`, `this.hasMonitorAnnouncement`

## takeMonitorAttentionIds()
- 位置: L588-592
- 役割: 注意の ID を読み取り、そのあと注意を消す
- 触るとき: パネルを開いたときに強調を一度だけ出す挙動を変えるとき
- 呼び出し先: `this.clearMonitorAttention()`
- 参照: `this.monitorAttentionIds`

## showMonitorAttention()
- 位置: L597-600
- 役割: 監視の条件一致を記録し、全ウィンドウのボタンを更新する
- 触るとき: 条件一致時の点の表示経路を追うとき
- 呼び出し先: `lazy.MonitorAttention.recordMatch()`, `this._forEachWindow()`, `this._updateMonitorButtonForWindow()`

## showMonitorErrorAttention()
- 位置: L608-611
- 役割: 監視の実行失敗を記録し、全ウィンドウのボタンを更新する
- 触るとき: 実行失敗時の点の表示経路を追うとき
- 呼び出し先: `lazy.MonitorAttention.recordError()`, `this._forEachWindow()`, `this._updateMonitorButtonForWindow()`

## clearMonitorAttention()
- 位置: L617-626
- 役割: 注意を消し、告知が出ていれば pref を false にして以後出さない
- 触るとき: パネルを開いた後の点の消え方や告知の終わり方を変えるとき
- 呼び出し先: `lazy.MonitorAttention.clearAttention()`, `this._forEachWindow()`, `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (lazy.monitorAnnouncement)` → `Services.prefs.setBoolPref()`
- 参照: `lazy.monitorAnnouncement`
- XPCOM: `Services.prefs`

## _updateMonitorAttentionForNode()
- 位置: L628-630
- 役割: ボタンに monitor-attention 属性を注意の有無に合わせて付ける
- 触るとき: 点の見た目を制御する属性の付け方を変えるとき
- 呼び出し先: `node.toggleAttribute()`
- 参照: `this.hasMonitorAttention`

## _shouldShowMonitorButton()
- 位置: L632-634
- 役割: 監視ボタンが有効で、そのウィンドウが AI ウィンドウのとき真
- 触るとき: ウィンドウ単位の監視ボタン表示条件を変えるとき
- 呼び出し先: `this.isAIWindowActive()`
- 参照: `this.monitorButtonEnabled`

## isDefaultWindow()
- 位置: L636-642
- 役割: 既定ウィンドウに設定済みかつ機能が有効なら真を返す
- 触るとき: 起動時に AI ウィンドウで開くかの前提を調べるとき
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.isAIWindowEnabled()`
- 参照: `this.AIWindowEnabledPref`
- XPCOM: `Services.prefs`

## shouldOpenAsSmartWindow()
- 位置: L644-652
- 役割: 既定ウィンドウで、永続プライベートでなければ真を返す
- 触るとき: 起動時に AI ウィンドウで開く条件を変えるとき
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this.isDefaultWindow`

## onFirstWindowReady()
- 位置: async L662-685
- 役割: 起動後の最初のウィンドウを既定設定に従って AI ウィンドウへ昇格させ、必要ならサインインを求める
- 触るとき: 起動直後の AI ウィンドウ化の流れを追うとき
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStartup.willRestore()`, `this._authorizeAndToggleWindow()`, `this.isAIWindowActive()`, `this.recordLaunchCommandTelemetry()`, `this.shouldOpenAsSmartWindow()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `lazy.AIWindowAccountAuth.ensureAIWindowAccess()`
- 参照: `win.gBrowser.selectedBrowser`

## _recordSmartWindowUsage()
- 位置: L693-698
- 役割: AI ウィンドウを使っていた最後の時刻(秒)を pref に保存する
- 触るとき: 最後の利用時刻に依存する案内の判定を調べるとき
- 呼び出し先: `Date.now()`, `Math.floor()`, `Services.prefs.setIntPref()`
- XPCOM: `Services.prefs`

## handleAIWindowOptions()
- 位置: L714-786
- 役割: 新しいウィンドウを AI ウィンドウで開くか判定し、起動 URL と AI フラグ、没入表示の属性を引数に付ける
- 触るとき: 新規ウィンドウを開くときに AI 状態をどう引き継ぐかを変えるとき
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `args.queryElementAt()`, `console.error()`, `propBag.setPropertyAsBool()`, `this.immersiveViewURIs.some()`, `this.isAIWindowActiveAndEnabled()`, `this.isAIWindowEnabled()`
- 条件付き依存: `if (!args.length)` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if (!args.length)` → `args.appendElement()`
- 条件付き依存: `if (!restoreSessionURL)` → `args.queryElementAt()`
- 条件付き依存: `if (!restoreSessionURL)` → `firstArg.data.split()`
- 条件付き依存: `if (!propBag)` → `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`
- 条件付き依存: `if (!propBag)` → `args.appendElement()`
- 条件付き依存: `if (canInheritAIWindow)` → `propBag.setPropertyAsAString()`
- 条件付き依存: `if (willOpenImmersive)` → `propBag.setPropertyAsBool()`
- 参照: `Ci.nsIMutableArray`, `Ci.nsIPropertyBag2`, `Ci.nsISupportsString`, `Ci.nsIWritablePropertyBag2`, `aiWindowURI.data`, `args.length`, `this.initialStartupURL`, `uri.spec`
- XPCOM: [`nsIMutableArray`](../../../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIPropertyBag2`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / [`nsISupportsString`](../../../../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../../../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-string;1`

## handleAIWindowSwitcher()
- 位置: L793-833
- 役割: 切り替えボタンの表示を現在の状態に合わせ、初回だけ切り替え操作のイベントを登録する
- 触るとき: 切り替えメニューの選択状態や操作の結果を変えるとき
- 呼び出し先: `lazy.PanelMultiView.getViewNode()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this._windowStates.get()`, `this.isAIWindowActive()`, `this.launchWindow()`, `this.toggleAIWindow()`, `view.addEventListener()`
- 条件付き依存: `if (!isPrivateWindow)` → `view.querySelector()`
- 条件付き依存: `if (!isPrivateWindow)` → `classicSwitchButton.toggleAttribute()`
- 条件付き依存: `if (!isPrivateWindow)` → `smartSwitchButton.toggleAttribute()`
- 条件付き依存: `if (!windowState)` → `this._windowStates.set()`
- 参照: `classicSwitchButton.hidden`, `event.target.id`, `smartSwitchButton.hidden`, `win.document`, `win.gBrowser.selectedBrowser`, `windowState.viewInitialized`

## isAIWindowActive()
- 位置: L841-843
- 役割: ウィンドウの ai-window 属性があれば真を返す
- 触るとき: そのウィンドウが AI ウィンドウかどうかを判定する箇所を追うとき
- 呼び出し先: `win.document.documentElement.hasAttribute()`

## isAIWindowEnabled()
- 位置: L850-852
- 役割: isAvailable の値をそのまま返す(機能が使えるか)
- 触るとき: 機能の利用可否の判定を調べるとき
- 参照: `this.isAvailable`

## isAIWindowActiveAndEnabled()
- 位置: L854-856
- 役割: AI ウィンドウであり、かつ機能が使える場合に真を返す
- 触るとき: AI ウィンドウ向けの処理を行う前提条件を確認するとき
- 呼び出し先: `this.isAIWindowActive()`, `this.isAIWindowEnabled()`

## isOpeningAIWindow()
- 位置: L864-871
- 役割: 開こうとしているウィンドウの引数に ai-window が含まれるかを返す
- 触るとき: 開く途中のウィンドウの状態を判定するとき
- 呼び出し先: `windowArgs.hasKey()`
- 参照: `Ci.nsIPropertyBag2`, `win?.arguments`
- XPCOM: [`nsIPropertyBag2`](../../../../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## isAIWindowContentPage()
- 位置: L879-883
- 役割: URI が AI ウィンドウの新規タブかオンボーディングのページなら真を返す
- 触るとき: AI ウィンドウ用のページかどうかで挙動を分けるとき
- 呼び出し先: `AIWINDOW_URI.equalsExceptRef()`, `FIRSTRUN_URI.equalsExceptRef()`

## isAIWindowNewTabPage()
- 位置: L892-894
- 役割: URI が AI ウィンドウの新規タブページなら真を返す(オンボーディングは含まない)
- 触るとき: 新規タブ特有の処理の範囲を決めるとき
- 呼び出し先: `AIWINDOW_URI.equalsExceptRef()`

## getChatTabConversationId()
- 位置: L900-910
- 役割: AI ウィンドウの新規タブに紐づく会話 ID を返す。無ければ null
- 触るとき: タブと会話の対応を調べるとき
- 呼び出し先: `this._aiWindowTabStateManagers .get()`, `this._aiWindowTabStateManagers .get(tab.documentGlobal) ?.getTabConversationId()`, `this.isAIWindowNewTabPage()`
- 参照: `tab.documentGlobal`, `tab.linkedBrowser?.currentURI`

## appMenu()
- 位置: L920-926
- 役割: AI ウィンドウ用のメニュー項目を遅延生成して追加する
- 触るとき: メニューの項目を追加・変更するとき
- 呼び出し先: `this._aiWindowMenu.addMenuitems()`
- 参照: `lazy.AIWindowMenu`, `this._aiWindowMenu`

## newTabURL()
- 位置: L928-930
- 役割: AI ウィンドウの新規タブ URL を返す
- 触るとき: 新規タブの遷移先を変えるとき

## firstrunURL()
- 位置: L932-934
- 役割: 初回案内ページの URL を返す
- 触るとき: 初回案内の URL を変えるとき

## initialStartupURL()
- 位置: L943-945
- 役割: 初回案内が完了していなければ初回案内、完了していれば新規タブ URL を返す
- 触るとき: AI ウィンドウを新規に開いたときの最初のページを変えるとき
- 参照: `lazy.hasFirstrunCompleted`

## performSearch()
- 位置: async L954-978
- 役割: 既定の検索エンジンでクエリを検索し、サイドバーにフォーカスを移す
- 触るとき: AI ウィンドウからの検索の挙動を変えるとき
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `console.error()`, `lazy.AIWindowUI.focusSidebar()`, `lazy.SearchService.getDefault()`, `lazy.SearchUIUtils.loadSearch()`
- XPCOM: `Services.scriptSecurityManager`

## moveConversationToSidebar()
- 位置: async L987-989
- 役割: 全画面の会話をサイドバーへ移す
- 触るとき: 全画面からサイドバーへの移動の仕組みを追うとき
- 呼び出し先: `lazy.AIWindowUI.moveFullPageToSidebar()`

## focusSidebar()
- 位置: L991-993
- 役割: サイドバーにフォーカスを移す
- 触るとき: サイドバーのフォーカス動作を調べるとき
- 呼び出し先: `lazy.AIWindowUI.focusSidebar()`

## openSidebarAndContinue()
- 位置: L1002-1028
- 役割: サイドバーを開いて会話を渡し、読み込み済みなら続きの応答を再開し、未読込なら属性で後から再開させる
- 触るとき: ツール実行の後にサイドバーで応答を続ける流れを変えるとき
- 呼び出し先: `aiBrowser?.contentDocument?.querySelector()`, `lazy.AIWindowUI.focusSidebar()`, `lazy.AIWindowUI.openSidebar()`, `sidebar?.querySelector()`, `win.document.getElementById()`
- 条件付き依存: `if (aiWindow?.reloadAndContinue)` → `aiWindow.reloadAndContinue()`
- 条件付き依存: `if (aiBrowser)` → `aiBrowser.setAttribute()`
- 参照: `aiWindow?.reloadAndContinue`

## createAITab()
- 位置: L1040-1092
- 役割: http(s) の URL だけを含むプロンプトで AI タブ用の背景タブを開き、チャットに送信する
- 触るとき: 複数タブから AI タブを作る操作の入力内容や送信タイミングを変えるとき
- 呼び出し先: `URL.parse()`, `[ lazy.l10n.formatValueSync("ai-tab-create-page-prompt", { tabCount: pageUrls.length, }), ...pageUrls, ].join()`, `["http:", "https:"].includes()`, `lazy.URILoadingHelper.openTrustedLinkIn()`, `lazy.l10n.formatValueSync()`, `urls.filter()`
- 参照: `URL.parse(url)?.protocol`, `pageUrls.length`

## resolveOnContentBrowserCreated()
- 位置: L1057-1090
- 役割: 新しいタブの ai-window が準備できていれば即送信し、そうでなければ接続を待つ
- 触るとき: 新規タブの読み込み完了を待つ条件を変えるとき
- 呼び出し先: `browser.contentDocument?.querySelector()`, `controller.abort()`, `submit()`, `tab.addEventListener()`, `win.addEventListener()`, `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (browser.contentDocument?.querySelector("ai-window")?.conversation)` → `submit()`
- 参照: `browser.contentDocument?.querySelector("ai-window")?.conversation`, `event.detail.tab`

## submit()
- 位置: L1058-1063
- 役割: 作ったプロンプトを ai-window の submitChatMessage で送る
- 触るとき: 送信時に渡す種類(submitType)や文脈を変えるとき
- 呼び出し先: `browser.contentDocument.querySelector()`, `browser.contentDocument.querySelector("ai-window").submitChatMessage()`

## recordOpenWindowTelemetry()
- 位置: L1104-1119
- 役割: AI ウィンドウを開いた理由、サインイン状態、初回かどうか、タブ数を Glean に記録する
- 触るとき: AI ウィンドウを開いた計測項目を追加・修正するとき
- 呼び出し先: `Glean.smartWindow.openWindow.record()`, `lazy.AIWindowAccountAuth.isSignedIn()`, `lazy.AIWindowAccountAuth.isSignedIn() .then()`, `lazy.AIWindowAccountAuth.isSignedIn() .then(result => { signedIn = result; }) .finally()`
- 参照: `lazy.hasFirstrunCompleted`, `win?.gBrowser?.tabs.length`

## recordLaunchCommandTelemetry()
- 位置: L1130-1143
- 役割: 起動の操作(きっかけ、サインイン状態、新規ウィンドウか)を Glean に記録する
- 触るとき: 起動操作の計測内容を変えるとき
- 呼び出し先: `Glean.smartWindow.launchCommandInvoked.record()`, `lazy.AIWindowAccountAuth.isSignedIn()`, `lazy.AIWindowAccountAuth.isSignedIn() .then()`, `lazy.AIWindowAccountAuth.isSignedIn() .then(result => { signedIn = result; }) .finally()`

## toggleAIWindow()
- 位置: L1155-1210
- 役割: ウィンドウの AI 状態を切り替え、新規タブ・ボタン・状態管理・計測を更新する
- 触るとき: AI ウィンドウと通常ウィンドウの切り替えで何が変わるかを追うとき
- 呼び出し先: `this.isAIWindowActive()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `lazy.NewTabPagePreloading.removePreloadedBrowser()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `win.document.documentElement.toggleAttribute()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._reconcileNewTabPages()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._updateHamburgerMenuPosition()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._initializeAskButtonOnToolbox()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `this._updateGroupTabsButtonVisibility()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `win.document.getElementById()`
- 条件付き依存: `if (isActive != isTogglingToAIWindow)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this._aiWindowTabStateManagers.has()`
- 条件付き依存: `if (!this._aiWindowTabStateManagers.has(win))` → `this._aiWindowTabStateManagers.set()`
- 条件付き依存: `if (lazy.hasFirstrunCompleted)` → `this._aiWindowTabStateManagers .get(win) ?.openSidebarForReturningUser()`
- 条件付き依存: `if (lazy.hasFirstrunCompleted)` → `this._aiWindowTabStateManagers .get()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this._startSchedulers()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this._markActiveStart()`
- 条件付き依存: `if (isTogglingToAIWindow)` → `this.recordOpenWindowTelemetry()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `this._consumeActiveDuration()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `this._uninitTabStateManager()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `this._recordSmartWindowUsage()`
- 条件付き依存: `if (!(isTogglingToAIWindow))` → `Glean.smartWindow.classicSwitch.record()`
- 参照: `lazy.AIWindowTabStatesManager`, `lazy.hasFirstrunCompleted`, `win.BROWSER_NEW_TAB_URL`, `win.gBrowser.tabs.length`
- XPCOM: `Services.obs` / `Services.prefs`

## _uninitTabStateManager()
- 位置: L1212-1219
- 役割: ウィンドウのタブ状態管理を終了して登録を外す
- 触るとき: 切り替えや閉じるときに状態管理が残る問題を調べるとき
- 呼び出し先: `manager.uninit()`, `this._aiWindowTabStateManagers.delete()`, `this._aiWindowTabStateManagers.get()`

## getActiveConversation()
- 位置: L1221-1225
- 役割: ウィンドウで今アクティブな会話を返す。無ければ null
- 触るとき: 今表示中の会話を取得する経路を調べるとき
- 呼び出し先: `this._aiWindowTabStateManagers.get()`, `this._aiWindowTabStateManagers.get(win)?.getActiveConversation()`

## _getTabStateManager()
- 位置: L1227-1229
- 役割: ウィンドウのタブ状態管理を返す。無ければ null
- 触るとき: タブ状態管理へアクセスする箇所を調べるとき
- 呼び出し先: `this._aiWindowTabStateManagers.get()`

## restoreTabConversation()
- 位置: L1237-1244
- 役割: ブラウザに紐づくタブへ指定の会話を設定する
- 触るとき: タブの会話を復元する流れを追うとき
- 呼び出し先: `this._getTabStateManager()`, `this._getTabStateManager(win)?.setTabStateConversation()`, `win?.gBrowser.getTabForBrowser()`
- 参照: `browser.documentGlobal`

## unloadWindow()
- 位置: L1246-1255
- 役割: ウィンドウを閉じるとき、利用時間と閉じた計測を記録し、タブ状態管理と登録を解放する
- 触るとき: ウィンドウ終了時の計測や後片付けを変えるとき
- 呼び出し先: `this._uninitTabStateManager()`, `this._windowStates.delete()`, `this.isAIWindowActive()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `this._consumeActiveDuration()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `Glean.smartWindow.closeWindow.record()`
- 条件付き依存: `if (this.isAIWindowActive(win))` → `this._recordSmartWindowUsage()`
- 参照: `win.gBrowser?.tabs.length`

## _markActiveStart()
- 位置: L1257-1262
- 役割: AI ウィンドウの利用開始時刻をウィンドウ状態に記録する
- 触るとき: 利用時間の計測の始まりを調べるとき
- 呼び出し先: `this._windowStates.get()`
- 条件付き依存: `if (windowState)` → `Date.now()`
- 参照: `windowState.aiActiveStartTime`

## _consumeActiveDuration()
- 位置: L1264-1271
- 役割: 利用開始からの経過ミリ秒を返し、開始時刻を消す
- 触るとき: 利用時間の計測の終わりを調べるとき
- 呼び出し先: `Date.now()`, `this._windowStates.get()`
- 参照: `windowState.aiActiveStartTime`, `windowState?.aiActiveStartTime`

## _authorizeAndToggleWindow()
- 位置: async L1273-1302
- 役割: サインインを確認してから AI 状態にし、初回案内が未完了なら初回案内へ移す
- 触るとき: AI ウィンドウに入る前の認可と初回案内への移動を変えるとき
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.AIWindowAccountAuth.ensureAIWindowAccess()`, `this.toggleAIWindow()`
- 条件付き依存: `if (!lazy.hasFirstrunCompleted)` → `win.gBrowser.loadURI()`
- 条件付き依存: `if (trigger === "startup")` → `Services.io.newURI()`
- 条件付き依存: `if (tab.linkedBrowser?.currentURI?.spec === "about:blank")` → `tab.linkedBrowser.loadURI()`
- 参照: `lazy.hasFirstrunCompleted`, `tab.linkedBrowser?.currentURI?.spec`, `win.gBrowser.selectedBrowser`, `win.gBrowser.tabs`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## launchWindow()
- 位置: async L1304-1347
- 役割: AI ウィンドウの起動を、現在のウィンドウへの切り替えか新規ウィンドウで行い、必要なら認可を挟む
- 触るとき: 起動ボタンやショートカットの動作を変えるとき
- 呼び出し先: `console.error()`, `lazy.AIWindowAccountAuth.canAccessAIWindow()`, `lazy.BrowserWindowTracker.promiseOpenWindow()`, `this.recordLaunchCommandTelemetry()`, `this.recordOpenWindowTelemetry()`
- 条件付き依存: `if (!this.isAllowed)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!openNewWindow)` → `this._authorizeAndToggleWindow()`
- 条件付き依存: `if (!isAuthorized)` → `this._authorizeAndToggleWindow()`
- 参照: `browser.documentGlobal`, `browser?.documentGlobal`, `this.isAllowed`, `this.isBlocked`
- XPCOM: `Services.prefs`

## launchSignInFlow()
- 位置: async L1355-1362
- 役割: FxA のサインインを開始し、成功したかを返す。失敗時は false
- 触るとき: サインインの開始方法や失敗時の扱いを変えるとき
- 呼び出し先: `console.error()`, `lazy.AIWindowAccountAuth.promptSignIn()`

## updateImmersiveView()
- 位置: L1370-1435
- 役割: ページに応じて没入表示(サイドバーの隠し、タブの無効化、ボタンの表示)を切り替える
- 触るとき: 没入表示の対象ページや見た目の切り替えを変えるとき
- 呼び出し先: `Services.io.newURI()`, `currentURI.equalsExceptRef()`, `root.hasAttribute()`, `root.toggleAttribute()`, `this._updateMonitorButtonForWindow()`, `this.isAIWindowActiveAndEnabled()`, `this.shouldUseImmersiveView()`, `win.document.getElementById()`, `win.gBrowser.selectedBrowser?.toggleAttribute()`
- 条件付き依存: `if (!this.isAIWindowActiveAndEnabled(win))` → `root.toggleAttribute()`
- 条件付き依存: `if (!this.isAIWindowActiveAndEnabled(win))` → `root.removeAttribute()`
- 条件付き依存: `if (!this.isAIWindowActiveAndEnabled(win))` → `this._updateMonitorButtonForWindow()`
- 条件付き依存: `if (isImmersiveView)` → `lazy.AIWindowUI.closeSidebar()`
- 条件付き依存: `if (root.hasAttribute("aiwindow-first-run") && !isFirstRunView)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (isFirstRun)` → `selectedTab?.setAttribute()`
- 条件付き依存: `if (!(isFirstRun))` → `selectedTab?.removeAttribute()`
- 参照: `askButton.hidden`, `win.gBrowser.selectedTab`
- XPCOM: `Services.io` / `Services.obs`

## shouldUseImmersiveView()
- 位置: L1443-1450
- 役割: URI が没入表示の対象(初回案内か AI 新規タブ)なら真を返す
- 触るとき: 没入表示の対象ページを増やすとき
- 呼び出し先: `immersiveURI.equalsExceptRef()`, `this.immersiveViewURIs.some()`

## getSmartbarForWindow()
- 位置: L1459-1467
- 役割: 選択中タブの ai-window 内にあるスマートバー要素を返す。無ければ null
- 触るとき: スマートバーへ外から触る経路を調べるとき
- 呼び出し先: `aiWindowCE?.shadowRoot.getElementById()`, `contentDocument?.querySelector()`
- 参照: `window.gBrowser.selectedBrowser`

## _createSwitcherWidget()
- 位置: L1469-1494
- 役割: AI 切り替えのツールバーウィジェットを作り、表示時にメニューの状態を合わせる
- 触るとき: 切り替えボタンの配置や属性を変えるとき
- 呼び出し先: `lazy.CustomizableUI.createWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.CustomizableUI.AREA_TABSTRIP`, `this._switcherWidgetCreated`

## onCreated()
- 位置: L1483-1487
- 役割: 切り替えボタンに CSS クラス、ARIA 属性、表示状態を設定する
- 触るとき: 切り替えボタンの初期属性を変えるとき
- 呼び出し先: `node.classList.add()`, `node.setAttribute()`, `this._updateButtonVisibility()`

## onViewShowing()
- 位置: L1488-1491
- 役割: 切り替えメニューが開くとき、そのウィンドウの切り替え状態を更新する
- 触るとき: メニューを開いたときの表示内容を変えるとき
- 呼び出し先: `this.handleAIWindowSwitcher()`
- 参照: `event.target.documentGlobal`

## _createGroupTabsWidget()
- 位置: L1496-1518
- 役割: タブ整理ボタン(CustomizableUI)を作る
- 触るとき: 整理ボタンの配置や属性を変えるとき
- 呼び出し先: `lazy.CustomizableUI.createWidget()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.CustomizableUI.AREA_TABSTRIP`, `this._groupTabsWidgetCreated`

## onCreated()
- 位置: L1508-1512
- 役割: 整理ボタンに ARIA 属性を付け、表示条件を反映する
- 触るとき: 整理ボタンの初期属性を変えるとき
- 呼び出し先: `node.setAttribute()`, `this._updateGroupTabsButtonVisibility()`

## onCommand()
- 位置: L1513-1515
- 役割: 整理ボタンの押下で、そのウィンドウの整理パネルを開く
- 触るとき: 整理パネルの開き方を変えるとき
- 呼び出し先: `lazy.AIWindowUI.toggleGroupTabsPanel()`
- 参照: `event.target.documentGlobal`

## _destroyGroupTabsWidget()
- 位置: L1520-1527
- 役割: タブ整理ボタンを CustomizableUI から破棄する
- 触るとき: 整理ボタンを撤去する条件を確認するとき
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`
- 参照: `this._groupTabsWidgetCreated`

## _updateGroupTabsWidgetRegistration()
- 位置: L1534-1540
- 役割: 自動グループ化が有効で遮断されていなければ整理ボタンを作り、そうでなければ破棄する
- 触るとき: 整理ボタンの登録条件を変えるとき
- 呼び出し先: `this._destroyGroupTabsWidget()`
- 条件付き依存: `if (lazy.autoTabGroupingEnabled && !this.isBlocked)` → `this._createGroupTabsWidget()`
- 参照: `lazy.autoTabGroupingEnabled`, `this.isBlocked`

## _destroySwitcherWidget()
- 位置: L1542-1549
- 役割: 切り替えボタンを CustomizableUI から破棄する
- 触るとき: 切り替えボタンを撤去する条件を確認するとき
- 呼び出し先: `lazy.CustomizableUI.destroyWidget()`
- 参照: `this._switcherWidgetCreated`

## _updateSwitcherWidgetRegistration()
- 位置: L1554-1560
- 役割: 遮断されていなければ切り替えボタンを作り、遮断されていれば破棄する
- 触るとき: AI Controls による切り替えボタンの出し分けを変えるとき
- 条件付き依存: `if (this.isBlocked)` → `this._destroySwitcherWidget()`
- 条件付き依存: `if (!(this.isBlocked))` → `this._createSwitcherWidget()`
- 参照: `this.isBlocked`

## id()
- 位置: L1570-1572
- 役割: AIFeature 用の機能 ID smartWindow を返す
- 触るとき: AI Controls や設定画面で機能を識別する箇所を調べるとき

## hasDistinctEnabledState()
- 位置: L1579-1582
- 役割: 「有効」の状態を別に持つことを示し、常に真を返す
- 触るとき: AI Controls の状態表示を変えるとき

## isBlocked()
- 位置: L1589-1594
- 役割: AI Controls の設定から遮断されているかを返す(smartWindow が default なら browser.ai.control.default を見る)
- 触るとき: 遮断の判定ロジックを変えるとき
- 参照: `this.AIControlDefault`, `this.AIControlSmartWindow`

## isEnabled()
- 位置: L1601-1606
- 役割: 使える状態かつ同意時刻が保存されていれば真を返す
- 触るとき: 同意済みかどうかの判定を変えるとき
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 参照: `this.isAvailable`
- XPCOM: `Services.prefs`

## isAvailable()
- 位置: L1608-1610
- 役割: 許可されていて遮断されていなければ真を返す
- 触るとき: 機能の利用可否の基準を変えるとき
- 参照: `this.isAllowed`, `this.isBlocked`

## isAllowed()
- 位置: L1617-1619
- 役割: 機能の pref(browser.smartwindow.enabled)の値を返す
- 触るとき: 機能の許可判定の元の pref を追うとき
- 参照: `this.AIWindowEnabledPref`

## canRunOnDevice()
- 位置: L1626-1629
- 役割: 常に真を返す(端末の制限は無い)
- 触るとき: 端末による制限を追加するとき

## isManagedByPolicy()
- 位置: L1636-1641
- 役割: AI Controls か機能 pref がポリシーで固定されていれば真を返す
- 触るとき: 企業ポリシーによる固定の扱いを変えるとき
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## makeAvailable()
- 位置: async L1648-1653
- 役割: 同意時刻を消し、記憶の生成設定を既定の真に戻す
- 触るとき: 機能を利用可能な初期状態に戻す処理を変えるとき
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## enable()
- 位置: async L1660-1663
- 役割: 機能の pref と AI Controls を有効にする
- 触るとき: 有効化の操作で何が変わるかを追うとき
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setStringPref()`
- XPCOM: `Services.prefs`

## block()
- 位置: async L1670-1676
- 役割: AI Controls を遮断にし、会話をすべて消して記憶も削除する
- 触るとき: 遮断時に消すデータの範囲を変えるとき
- 呼び出し先: `Services.prefs.setStringPref()`, `lazy.ChatStore.deleteAllConversations()`, `this._removeMemories()`
- XPCOM: `Services.prefs`

## _removeMemories()
- 位置: async L1684-1696
- 役割: 記憶を一件ずつ完全削除し、記憶の生成設定を両方とも偽にする
- 触るとき: 遮断時の記憶の消去や生成停止の挙動を変えるとき
- 呼び出し先: `Services.prefs.setBoolPref()`, `console.error()`, `lazy.MemoryStore.getMemories()`, `lazy.MemoryStore.hardDeleteMemory()`
- 参照: `memory.id`
- XPCOM: `Services.prefs`
