# browser/components/search/content/searchbar.js

source: browser/components/search/content/searchbar.js
source-hash: bebd239f31ac9179d75514892091e9bc671dde77
lines: 1032

## <module>
- 役割: ブラウザのツールバーに置く検索バー要素(searchbar)を定義する。エンジンの選択、検索の実行、提案パネルの開閉、文脈メニューを担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## MozSearchbar.inheritedAttributes()
- 位置: L32-38
- 役割: 内部の入力欄とボタンへ引き継ぐ属性の対応表を返す。
- 触るとき: 検索バーの属性を内部要素へ渡す条件を変えるとき。disabled、searchengine などが対象。

## MozSearchbar.markup()
- 位置: L40-53
- 役割: 検索バーの内部マークアップ(検索アイコン、入力欄、文脈メニュー、移動ボタン)の文字列を返す。
- 触るとき: 検索バーの構造や data-l10n-id を変えるとき。

## MozSearchbar.constructor()
- 位置: L55-97
- 役割: FTL を読み込み、イベントを張り、新旧の検索ウィジェットの切り替え設定と検索エンジンの変更通知を監視する。
- 触るとき: 検索バーの作成時に監視する通知を増やすとき。ウィンドウのアンロード時に destroy が呼ばれる。
- 呼び出し先: `ChromeUtils.generateQI()`, `MozXULElement.insertFTLIfNeeded()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`, `super()`, `this._setupEventListeners()`, `this.destroy()`, `window.addEventListener()`
- 参照: `this._engines`, `this._ignoreFocus`, `this.observer`, `this.telemetrySelectedIndex`
- XPCOM: `Services.prefs`

## MozSearchbar.observe()
- 位置: L62-80
- 役割: エンジン変更の通知で一覧を取り直して表示を更新し、browser.search.widget.new の変更で接続と切断を切り替える。
- 触るとき: 検索エンジンの設定変更が検索バーに反映されないとき、またはウィジェットの切り替えを調べるとき。
- 条件付き依存: `if (aTopic == "browser-search-engine-modified")` → `searchbar._textbox.popup.updateHeader()`
- 条件付き依存: `if (aTopic == "browser-search-engine-modified")` → `searchbar.updateDisplay()`
- 条件付き依存: `if ( aData == "browser.search.widget.new" && searchbar.isConnected )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.search.widget.new"))` → `searchbar.disconnectedCallback()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref("browser.search.widget.new")))` → `searchbar.connectedCallback()`
- 参照: `searchbar._engines`, `searchbar.isConnected`
- XPCOM: `Services.prefs`

## MozSearchbar.connectedCallback()
- 位置: L99-188
- 役割: 表示される場合だけ内部要素を組み立て、保存された幅を戻し、入力欄と提案パネルを設定し、検索サービスの初期化後に表示を更新する。
- 触るとき: 検索バーが画面に出るまでの初期化順序を変えるとき。ツールバーのパレット内、カスタマイズ中、新しい検索ウィジェット使用時は何もしない。
- 呼び出し先: `(window.delayedStartupPromise || Promise.resolve()).then()`, `OpenSearchManager.updateOpenSearchBadge()`, `Promise.resolve()`, `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.xulStore.getValue()`, `console.error()`, `lazy.SearchService.init()`, `lazy.SearchService.init() .then()`, `this._initTextbox()`, `this._setupTextboxEventListeners()`, `this._textbox.popup.updateHeader()`, `this.appendChild()`, `this.closest()`, `this.handleSearchCommand()`, `this.initializeAttributeInheritance()`, `this.querySelector()`, `this.querySelector(".search-go-button").addEventListener()`, `this.textbox.popup.addEventListener()`, `this.updateDisplay()`, `window.requestIdleCallback()`
- 条件付き依存: `if (storedWidth)` → `this.parentNode.setAttribute()`
- 参照: `document.documentURI`, `oneOffButtons.popup`, `oneOffButtons.telemetryOrigin`, `oneOffButtons.textbox`, `this._initialized`, `this._menupopup`, `this._pasteAndSearchMenuItem`, `this._stringBundle`, `this._textbox`, `this.constructor.fragment`, `this.observer`, `this.parentNode.id`, `this.parentNode.parentNode.localName`, `this.parentNode.style.width`, `this.textbox`, `this.textbox.popup`, `this.textbox.popup.oneOffButtons`, `window.delayedStartupPromise`
- XPCOM: `Services.obs` / `Services.prefs` / `Services.xulStore`

## MozSearchbar.getEngines()
- 位置: async L190-195
- 役割: 表示対象の検索エンジン一覧を、未取得なら検索サービスから取って返す。
- 触るとき: エンジン切り替えの候補範囲を変えるとき。キャッシュはエンジン変更通知で消される。
- 条件付き依存: `if (!this._engines)` → `lazy.SearchService.getVisibleEngines()`
- 参照: `this._engines`

## MozSearchbar.currentEngine()
- 位置: L197-209
- 役割: 現在の既定エンジンを設定する。プライベートウィンドウでは非公開用の既定、そうでなければ通常の既定を変え、変更理由は USER_SEARCHBAR。
- 触るとき: 検索バーからエンジンを切り替える処理を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `lazy.SearchService.setDefaultPrivate()`
- 条件付き依存: `if (!(PrivateBrowsingUtils.isWindowPrivate(window)))` → `lazy.SearchService.setDefault()`
- 参照: `lazy.SearchService.CHANGE_REASON.USER_SEARCHBAR`

## MozSearchbar.currentEngine()
- 位置: L211-220
- 役割: プライベートかどうかに応じた既定エンジンを返す。無ければ名前が空のダミーを返す。
- 触るとき: エンジンが未設定のときの扱いを調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`
- 参照: `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`

## MozSearchbar.textbox()
- 位置: L228-230
- 役割: 内部の入力欄要素を返す。
- 触るとき: 外から検索バーの入力欄を操作する箇所を探すとき。サニタイズの処理がこの入力欄の undo 履歴を消す。
- 参照: `this._textbox`

## MozSearchbar.inputField()
- 位置: L235-237
- 役割: UrlbarInput と同じ API のため、入力欄を返す。
- 触るとき: URL バーと同じ形で扱う処理を書くとき。
- 参照: `this.textbox`

## MozSearchbar.value()
- 位置: L239-241
- 役割: 入力欄に値を設定する。
- 触るとき: 外から検索語を入れる処理を変えるとき。
- 参照: `this._textbox.value`

## MozSearchbar.value()
- 位置: L243-245
- 役割: 入力欄の値を返す。
- 触るとき: 検索語の取得元を追うとき。
- 参照: `this._textbox.value`

## MozSearchbar.destroy()
- 位置: L247-271
- 役割: エンジン変更通知の監視を外し、入力欄からこの要素への参照を切って循環参照を断つ。
- 触るとき: 検索バーの破棄時に解放されない参照が残るとき。
- 条件付き依存: `if (this._initialized)` → `Services.obs.removeObserver()`
- 参照: `this._initialized`, `this._textbox`, `this._textbox.mController`, `this._textbox.mController.input`, `this._textbox.mController.input.wrappedJSObject`, `this.nsIAutocompleteInput`, `this.observer`
- XPCOM: `Services.obs`

## MozSearchbar.focus()
- 位置: L273-275
- 役割: 入力欄にフォーカスを当てる。
- 触るとき: 検索バーへのフォーカス要求の経路を調べるとき。
- 呼び出し先: `this._textbox.focus()`

## MozSearchbar.select()
- 位置: L277-279
- 役割: 入力欄の文字を全選択する。
- 触るとき: 全選択の挙動を変えるとき。
- 呼び出し先: `this._textbox.select()`

## MozSearchbar.setIcon()
- 位置: L281-283
- 役割: 要素の src 属性に指定の URI を設定する。
- 触るとき: アイコン画像を差し替える箇所を探すとき。
- 呼び出し先: `element.setAttribute()`

## MozSearchbar.updateDisplay()
- 位置: L285-289
- 役割: 入力欄のツールチップに、現在のエンジン名を入れた案内文を設定する。
- 触るとき: ツールチップの文言を変えるとき。
- 呼び出し先: `this._stringBundle.getFormattedString()`
- 参照: `this._textbox.title`, `this.currentEngine.name`

## MozSearchbar.updateGoButtonVisibility()
- 位置: L291-293
- 役割: 入力欄が空なら移動ボタンを隠し、値があれば表示する。
- 触るとき: 入力時の移動ボタンの表示条件を変えるとき。
- 呼び出し先: `this.querySelector()`
- 参照: `this._textbox.value`, `this.querySelector(".search-go-button").hidden`

## MozSearchbar.openSuggestionsPanel()
- 位置: L295-311
- 役割: 提案パネルを開き、検索アイコンの expanded を真にする。入力があれば提案を取り直し、入力が無く設定だけ見せる場合はその属性を付ける。
- 触るとき: 提案パネルがいつどう開くかを変えるとき。既に開いていれば何もしない。
- 呼び出し先: `document.querySelector()`, `searchIcon.setAttribute()`, `this._textbox.showHistoryPopup()`
- 条件付き依存: `if (this._textbox.value)` → `this._textbox.mController.handleText()`
- 条件付き依存: `if (aShowOnlySettingsIfEmpty)` → `this.setAttribute()`
- 参照: `this._textbox.open`, `this._textbox.value`

## MozSearchbar.selectEngine()
- 位置: async L313-340
- 役割: Accel と上下キーで前後の検索エンジンへ切り替え、提案パネルを開く。先頭と末尾は循環する。
- 触るとき: エンジンの切り替え順や循環の挙動を変えるとき。イベントの伝播は止める。
- 呼び出し先: `aEvent.preventDefault()`, `aEvent.stopPropagation()`, `this.getEngines()`, `this.openSuggestionsPanel()`
- 参照: `engines.length`, `engines[i].name`, `this.currentEngine`, `this.currentEngine.name`

## MozSearchbar.handleSearchCommand()
- 位置: L342-352
- 役割: 移動ボタンの右クリックを除き、検索結果の開き先を決めて handleSearchCommandWhere に渡す。
- 触るとき: 検索の開き先を決める入口を変えるとき。
- 呼び出し先: `aEvent.originalTarget.classList.contains()`, `this._whereToOpen()`, `this.handleSearchCommandWhere()`
- 参照: `aEvent.button`

## MozSearchbar.handleSearchCommandWhere()
- 位置: L354-385
- 役割: 提案の選択番号と一つのワンオフかどうかを記録し、Enter の場合はブラウザ本体へのフォーカス移動を後にずらして doSearch を呼ぶ。
- 触るとき: 提案の選択や一つのワンオフの計測を変えるとき。
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchSuggestionSelectionMethod()`, `this.doSearch()`
- 条件付き依存: `if (selectedIndex == -1)` → `this.textbox.popup.oneOffButtons.eventTargetIsAOneOff()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.keyCode`, `aParams.avoidBrowserFocus`, `aParams.inBackground`, `textBox.value`, `this._needBrowserFocusAtEnterKeyUp`, `this._textbox`, `this.telemetrySelectedIndex`

## MozSearchbar.doSearch()
- 位置: L387-460
- 役割: 条件を満たす場合にフォーム履歴へ検索語を保存し、検索 URL を作り、計測を記録してから開く。
- 触るとき: 検索結果の開き方や履歴保存の条件を変えるとき。履歴は通常ウィンドウで、履歴が有効で、長さが上限以内のときだけ保存する。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.setStringPref()`, `engine.getSubmission()`, `new Date().toISOString()`, `openTrustedLinkIn()`
- 条件付き依存: `if ( aData && !PrivateBrowsingUtils.isWindowPrivate(window) && lazy.FormHistory.enabled && aData.length <= lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VAL...)` → `lazy.FormHistory.update()`
- 条件付き依存: `if ( aData && !PrivateBrowsingUtils.isWindowPrivate(window) && lazy.FormHistory.enabled && aData.length <= lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VAL...)` → `textBox.getAttribute()`
- 条件付き依存: `if ( aData && !PrivateBrowsingUtils.isWindowPrivate(window) && lazy.FormHistory.enabled && aData.length <= lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VAL...)` → `console.error()`
- 条件付き依存: `if (aWhere == "tab")` → `gBrowser.tabContainer.addEventListener()`
- 条件付き依存: `if (aWhere == "tab")` → `lazy.BrowserSearchTelemetry.recordSearch()`
- 条件付き依存: `if (!(aWhere == "tab"))` → `lazy.BrowserSearchTelemetry.recordSearch()`
- 参照: `aData.length`, `engine.name`, `event.target.linkedBrowser`, `gBrowser.selectedBrowser`, `lazy.FormHistory.enabled`, `lazy.SearchSuggestionController.SEARCH_HISTORY_MAX_VALUE_LENGTH`, `submission.postData`, `submission.uri.spec`, `this._textbox`, `this.currentEngine`, `this.telemetrySelectedIndex`
- XPCOM: `Services.prefs`

## MozSearchbar._whereToOpen()
- 位置: L474-519
- 役割: 修飾キー、中クリック、設定から、検索結果を今のタブ、新しいタブ、背景の新しいタブのどれで開くかを決める。
- 触るとき: 検索結果の開き方の設定や修飾キーの組み合わせを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `aEvent?.originalTarget.classList.contains()`
- 条件付き依存: `if (aEvent?.originalTarget.classList.contains("search-go-button"))` → `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (aEvent?.originalTarget.classList.contains("search-go-button"))` → `aEvent.getModifierState()`
- 条件付き依存: `if (aForceNewTab)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(aForceNewTab))` → `KeyboardEvent.isInstance()`
- 条件付き依存: `if (!(aForceNewTab))` → `aEvent.getModifierState()`
- 条件付き依存: `if (!(aForceNewTab))` → `MouseEvent.isInstance()`
- 参照: `aEvent.altKey`, `aEvent.button`, `gBrowser.selectedTab.isEmpty`
- XPCOM: `Services.prefs`

## MozSearchbar.openSearchFormWhere()
- 位置: L534-552
- 役割: エンジンの検索フォームのページを指定の場所で開き、その計測を記録する。
- 触るとき: 検索フォームを開く操作を変えるとき。
- 呼び出し先: `lazy.BrowserSearchTelemetry.recordSearchForm()`, `openTrustedLinkIn()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `aEvent.keyCode`, `engine.searchForm`, `params.avoidBrowserFocus`, `params.inBackground`, `this._needBrowserFocusAtEnterKeyUp`, `this.currentEngine`

## MozSearchbar.disconnectedCallback()
- 位置: L554-559
- 役割: 破棄してから子要素をすべて取り除く。
- 触るとき: 検索バーがツールバーから外れたときの後始末を変えるとき。
- 呼び出し先: `this.destroy()`, `this.firstChild.remove()`
- 参照: `this.firstChild`

## MozSearchbar._maybeSelectAll()
- 位置: L565-573
- 役割: 入力欄にフォーカスがあり選択が空のとき全選択する。マウス押下時点で既にフォーカスされていた場合は行わない。
- 触るとき: クリックで全選択される条件を変えるとき。
- 条件付き依存: `if ( !this._preventClickSelectsAll && document.activeElement == this._textbox && this._textbox.selectionStart == this._textbox.selectionEnd )` → `this.select()`
- 参照: `document.activeElement`, `this._preventClickSelectsAll`, `this._textbox`, `this._textbox.selectionEnd`, `this._textbox.selectionStart`

## MozSearchbar._setupEventListeners()
- 位置: L575-679
- 役割: 検索バー全体のイベントを張る。クリックで全選択、Accel 付きスクロールでエンジン切り替え、入力とドロップで移動ボタンを更新、フォーカスで提案を開き、マウス押下で提案パネルを開閉する。
- 触るとき: 検索バーでのマウス、キー、フォーカスの操作を変えるとき。
- 呼び出し先: `Services.focus.getLastFocusMethod()`, `event.getModifierState()`, `event.originalTarget.classList.contains()`, `this._maybeSelectAll()`, `this.addEventListener()`, `this.currentEngine.speculativeConnect()`, `this.openSuggestionsPanel()`, `this.updateGoButtonVisibility()`
- 条件付き依存: `if (event.getModifierState("Accel"))` → `this.selectEngine()`
- 条件付き依存: `if (isIconClick && this.textbox.popup.popupOpen)` → `this.textbox.popup.closePopup()`
- 条件付き依存: `if (isIconClick && this.textbox.popup.popupOpen)` → `document.querySelector()`
- 条件付き依存: `if (isIconClick && this.textbox.popup.popupOpen)` → `searchIcon.setAttribute()`
- 条件付き依存: `if (isIconClick || this._textbox.value)` → `this.openSuggestionsPanel()`
- 参照: `Services.focus.FLAG_BYMOUSE`, `document.activeElement`, `event.button`, `event.detail`, `event.originalTarget.localName`, `gBrowser.contentPrincipal.originAttributes`, `this._ignoreFocus`, `this._needBrowserFocusAtEnterKeyUp`, `this._preventClickSelectsAll`, `this._textbox`, `this._textbox.focused`, `this._textbox.value`, `this.textbox.popup.popupOpen`
- XPCOM: `Services.focus`

## MozSearchbar._setupTextboxEventListeners()
- 位置: L681-739
- 役割: 入力欄に入力、ドラッグ、ドロップ、文脈メニューのイベントを張る。ドロップされた文字列は入力欄に入れて提案を開く。
- 触るとき: 入力欄への文字列のドロップや文脈メニューの挙動を変えるとき。
- 呼び出し先: `controller.isCommandEnabled()`, `dataTransfer.getData()`, `document.commandDispatcher .getControllerForCommand()`, `document.commandDispatcher .getControllerForCommand("cmd_paste") .isCommandEnabled()`, `document.commandDispatcher.getControllerForCommand()`, `event.preventDefault()`, `item.getAttribute()`, `this._menupopup.openPopupAtScreen()`, `this._menupopup.querySelectorAll()`, `this._textbox.closePopup()`, `this.textbox.addEventListener()`, `this.textbox.popup.removeAttribute()`, `types.includes()`
- 条件付き依存: `if ( types.includes("text/plain") || types.includes("text/x-moz-text-internal") )` → `event.preventDefault()`
- 条件付き依存: `if (!data)` → `dataTransfer.getData()`
- 条件付き依存: `if (data)` → `event.preventDefault()`
- 条件付き依存: `if (data)` → `this.openSuggestionsPanel()`
- 条件付き依存: `if (!this._menupopup)` → `this._buildContextMenu()`
- 条件付き依存: `if (event.button)` → `this._maybeSelectAll()`
- 参照: `event.button`, `event.dataTransfer`, `event.dataTransfer.types`, `event.screenX`, `event.screenY`, `item.disabled`, `this._menupopup`, `this._pasteAndSearchMenuItem.disabled`, `this.textbox.value`

## MozSearchbar._initTextbox()
- 位置: L741-961
- 役割: 入力欄に検索用の属性と各種の上書き関数(キー操作、提案の開閉、Enter、入力確定など)を設定する。ツールバーのパレット内では何もしない。
- 触るとき: 入力欄のキー操作や提案パネルの開閉を変えるとき。上書きされる各関数は this.textbox で始まる項目を参照。
- 呼び出し先: `Object.defineProperty()`, `this.setAttribute()`
- 参照: `this.parentNode.parentNode.localName`, `this.textbox`, `this.textbox.handleEnter`, `this.textbox.onBeforeHandleKeyDown`, `this.textbox.onBeforeValueSet`, `this.textbox.onTextEntered`, `this.textbox.onbeforeinput`, `this.textbox.onkeyup`, `this.textbox.openPopup`, `this.textbox.openSearch`, `this.textbox.popup.id`

## MozSearchbar.get()
- 位置: L756-761
- 役割: 検索履歴の名前を返す。プライベートウィンドウでは末尾に |private が付く。
- 触るとき: プライベートウィンドウの検索履歴をどの履歴として扱うかを変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `this.getAttribute()`

## MozSearchbar.set()
- 位置: L762-764
- 役割: 検索履歴の名前の属性を設定する。
- 触るとき: 履歴の名前の属性を外から書き換える箇所を調べるとき。
- 呼び出し先: `this.setAttribute()`

## MozSearchbar.get()
- 位置: L768-770
- 役割: 提案パネルで選択中のワンオフボタンを返す。
- 触るとき: 選択中の検索ボタンを外から参照する処理を書くとき。
- 参照: `this.popup.oneOffButtons.selectedButton`

## MozSearchbar.set()
- 位置: L771-773
- 役割: 提案パネルで選択中のワンオフボタンを設定する。
- 触るとき: 外部からワンオフの選択を変える処理を書くとき。
- 参照: `this.popup.oneOffButtons.selectedButton`

## this.textbox.onBeforeValueSet()
- 位置: L778-783
- 役割: 入力欄の値が直接設定されたとき、ワンオフの検索語を同じ値に更新する。
- 触るとき: テストなどで値を直接入れたときに、ワンオフの検索語が追従するかを確認するとき。
- 参照: `this.textbox.popup._oneOffButtons`, `this.textbox.popup.oneOffButtons.query`

## this.textbox.onBeforeHandleKeyDown()
- 位置: L786-829
- 役割: Accel と上下でエンジンを切り替える。Alt と上下、または macOS の F4 で提案を開く。提案が開いていれば提案パネルに処理を任せ、Escape では入力を取り消すか全選択する。処理したかを返す。
- 触るとき: キーボード操作の割り振りを変えるとき。
- 呼び出し先: `aEvent.getModifierState()`, `document.querySelector()`, `searchIcon.setAttribute()`
- 条件付き依存: `if ( aEvent.keyCode == KeyEvent.DOM_VK_DOWN || aEvent.keyCode == KeyEvent.DOM_VK_UP )` → `this.selectEngine()`
- 条件付き依存: `if ( (AppConstants.platform == "macosx" && aEvent.keyCode == KeyEvent.DOM_VK_F4) || (aEvent.getModifierState("Alt") && (aEvent.keyCode == KeyEvent.DOM_VK_DOWN ||...)` → `this.textbox.openSearch()`
- 条件付き依存: `if (!this.textbox.openSearch())` → `aEvent.preventDefault()`
- 条件付き依存: `if (!this.textbox.openSearch())` → `aEvent.stopPropagation()`
- 条件付き依存: `if (popup.popupOpen)` → `popup.richlistbox.hasAttribute()`
- 条件付き依存: `if (popup.popupOpen)` → `popup.oneOffButtons.handleKeyDown()`
- 条件付き依存: `if (this.textbox.editor.canUndo)` → `this.textbox.editor.undoAll()`
- 条件付き依存: `if (!(this.textbox.editor.canUndo))` → `this.textbox.select()`
- 条件付き依存: `if (aEvent.keyCode == KeyEvent.DOM_VK_ESCAPE)` → `aEvent.preventDefault()`
- 参照: `AppConstants.platform`, `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_F4`, `KeyEvent.DOM_VK_UP`, `aEvent.keyCode`, `popup.matchCount`, `popup.popupOpen`, `this.textbox.editor.canUndo`, `this.textbox.popup`

## this.textbox.openPopup()
- 位置: L835-878
- 役割: 提案パネルを検索バーに揃えて開く。幅は検索バーの幅と、ワンオフ一つ分の 4 個分の幅のうち大きい方にする。カスタマイズ中は開かない。
- 触るとき: 提案パネルの位置や幅を変えるとき。
- 呼び出し先: `document.documentElement.hasAttribute()`, `document.querySelector()`
- 条件付き依存: `if (popup.id == "PopupSearchAutoComplete")` → `popup.setAttribute()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (popup.oneOffButtons)` → `Math.max()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `popup.style.setProperty()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `popup._invalidate()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `popup.openPopup()`
- 条件付き依存: `if (!popup.mPopupOpen)` → `searchIcon.setAttribute()`
- 参照: `popup.hidden`, `popup.id`, `popup.mInput`, `popup.mPopupOpen`, `popup.oneOffButtons`, `popup.oneOffButtons.buttonWidth`, `popup.selectedIndex`, `this.textbox`, `this.textbox.popup`

## this.textbox.openSearch()
- 位置: L880-886
- 役割: パネルが閉じていれば開いて偽を返し、開いていれば何もせず真を返す。
- 触るとき: Alt と下キーでパネルを開くだけにするか、閉じる処理にするかを判断する箇所を調べるとき。
- 条件付き依存: `if (!this.textbox.popupOpen)` → `this.openSuggestionsPanel()`
- 参照: `this.textbox.popupOpen`

## this.textbox.handleEnter()
- 位置: L888-922
- 役割: Enter で、追加ボタンの開閉を切り替え、検索語が空なら無視する(設定ボタンや追加ボタンが選ばれている場合を除く)。それ以外は既定の処理に委ねる。Shift と Enter なら検索フォームを開く。
- 触るとき: Enter の振る舞いを変えるとき。
- 呼び出し先: `this.textbox.mController.handleEnter()`, `this.textbox.selectedButton.getAttribute()`, `this.textbox.selectedButton?.classList.contains()`, `this.textbox.selectedButton?.getAttribute()`
- 条件付き依存: `if (event.shiftKey)` → `this._whereToOpen()`
- 条件付き依存: `if (event.shiftKey)` → `this.openSearchFormWhere()`
- 参照: `event.shiftKey`, `this.textbox.selectedButton`, `this.textbox.selectedButton.open`, `this.textbox.selectedButton?.engine`, `this.textbox.value`

## this.textbox.onTextEntered()
- 位置: L925-942
- 役割: 入力の確定時、選択中のワンオフがあればそのエンジンを使い、提案の選択番号を記録して検索を実行する。
- 触るとき: 確定時にどのエンジンで検索するかを変えるとき。
- 呼び出し先: `this.handleSearchCommand()`, `this.textbox.editor.clearUndoRedo()`
- 条件付き依存: `if (!oneOff.engine)` → `oneOff.doCommand()`
- 参照: `oneOff.engine`, `this.telemetrySelectedIndex`, `this.textbox.popupSelectedIndex`, `this.textbox.selectedButton`

## this.textbox.onbeforeinput()
- 位置: L944-949
- 役割: Enter の処理中に入る文字入力を止める。
- 触るとき: Enter の直後に入る入力の扱いを調べるとき。
- 条件付き依存: `if (event.data && this._needBrowserFocusAtEnterKeyUp)` → `event.preventDefault()`
- 参照: `event.data`, `this._needBrowserFocusAtEnterKeyUp`

## this.textbox.onkeyup()
- 位置: L951-960
- 役割: Enter の離しを検知し、ブラウザ本体へフォーカスを移す。
- 触るとき: Enter で検索した後のフォーカス移動を変えるとき。Meta キーの組み合わせで keyup が来ない場合も対象にしている。
- 条件付き依存: `if (this._needBrowserFocusAtEnterKeyUp)` → `gBrowser.selectedBrowser.focus()`
- 参照: `this._needBrowserFocusAtEnterKeyUp`

## MozSearchbar._buildContextMenu()
- 位置: L963-1027
- 役割: 文脈メニューの項目(元に戻す、やり直し、切り取り、コピー、貼り付け、貼り付けて検索、削除、すべて選択、履歴の消去)を作り、クリック時の処理を登録する。
- 触るとき: 文脈メニューの項目を増減するとき。履歴の消去は検索履歴の項目を消して入力欄を空にする。
- 呼び出し先: `MozXULElement.parseXULToFragment()`, `clearHistoryItem.setAttribute()`, `event.originalTarget.getAttribute()`, `frag.querySelector()`, `goDoCommand()`, `lazy.FormHistory.update()`, `this._menupopup.addEventListener()`, `this._menupopup.appendChild()`, `this._pasteAndSearchMenuItem.setAttribute()`, `this._stringBundle.getString()`, `this.handleSearchCommand()`, `this.querySelector()`, `this.select()`, `this.textbox.getAttribute()`
- 条件付き依存: `if (cmd)` → `document.commandDispatcher.getControllerForCommand()`
- 条件付き依存: `if (cmd)` → `controller.doCommand()`
- 参照: `event.originalTarget`, `this._menupopup`, `this._pasteAndSearchMenuItem`, `this.textbox.value`
