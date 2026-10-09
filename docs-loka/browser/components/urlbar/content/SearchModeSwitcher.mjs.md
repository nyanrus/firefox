# browser/components/urlbar/content/SearchModeSwitcher.mjs

source: browser/components/urlbar/content/SearchModeSwitcher.mjs
source-hash: 4d1c2c0aa625a6cd69bc0f21fad362103aed01ae
lines: 1189

## <module>
- 役割: urlbar の検索モード切り替えボタン(SearchModeSwitcher)を定義する。ボタンのアイコンとタイトル、ポップアップ内の検索エンジン一覧、Alt/Accel+上下キーでのエンジン切り替え、エンジン追加バッジを扱う。

## getL10n()
- 位置: L32-35
- 役割: browser.ftl を読む Localization を初回だけ作り、以後は同じものを返す。
- 触るとき: 検索モードのラベルを取得する経路で、翻訳の読み込み先を変えるときに見る。

## SearchModeSwitcher.constructor()
- 位置: L111-145
- 役割: 入力欄の中からボタン、パネル、閉じるボタンを取り、パネルを XUL の panel で包んで ID を振る。variantB ではボタンを ghost にする。キーワードが無効なら検索アイコンをすぐ更新する。
- 触るとき: 検索モードボタンが表示されない、ポップアップが前面に出ない、初期アイコンがおかしいときに見る。
- 呼び出し先: `UrlbarShared.keywordEnabled()`, `input.querySelector()`, `this.#button.setAttribute()`, `window.matchMedia()`
- 条件付き依存: `if (input.variantB)` → `this.#button.setAttribute()`
- 条件付き依存: `if (document.createXULElement)` → `document.createXULElement()`
- 条件付き依存: `if (document.createXULElement)` → `panel.setAttribute()`
- 条件付き依存: `if (document.createXULElement)` → `panel.classList.add()`
- 条件付き依存: `if (document.createXULElement)` → `this.#panelList.replaceWith()`
- 条件付き依存: `if (document.createXULElement)` → `panel.appendChild()`
- 条件付き依存: `if (!UrlbarShared.keywordEnabled(this.#input.sapName))` → `this.updateSearchIcon()`
- 参照: `document.createXULElement`, `input.sapName`, `input.variantB`, `this.#button`, `this.#closebutton`, `this.#input`, `this.#input.sapName`, `this.#noWordmarkQuery`, `this.#panelList`, `this.#panelList.id`

## SearchModeSwitcher.connect()
- 位置: L150-156
- 役割: UrlbarPrefs のオブザーバーを登録し、有効ならイベントの監視を始める。
- 触るとき: 入力欄を接続したあとに検索モードボタンが反応しない問題を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.addObserver()`, `this.#isEnabled()`
- 条件付き依存: `if (this.#isEnabled())` → `this.#enableObservers()`

## SearchModeSwitcher.disconnect()
- 位置: L161-164
- 役割: オブザーバーを外し、イベントの監視を止める。
- 触るとき: 入力欄を外した後も通知やイベントが残る問題を調べるときに見る。
- 呼び出し先: `UrlbarPrefs.removeObserver()`, `this.#disableObservers()`

## SearchModeSwitcher.#isEnabled()
- 位置: L166-171
- 役割: scotchBonnet.enableOverride が真、または入力欄が検索バーの SAP のときに真を返す。
- 触るとき: 検索モードボタンを有効にする条件を変えるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `this.#input.isSearchbarSAP`

## SearchModeSwitcher.#onPopupShowing()
- 位置: async L173-185
- 役割: ポップアップを開く時に engagement を破棄(記録しない)し、ビューを閉じてから一覧を組み立てる。urlbar では開いた回数を記録する。
- 触るとき: ポップアップを開いたときの計測やビューの閉じるタイミングを調べるときに見る。
- 呼び出し先: `this.#buildSearchModeList()`, `this.#input.controller.engagementEvent.discard()`, `this.#input.view.close()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.opened.add()`
- 参照: `this.#input.sapName`

## SearchModeSwitcher.closePanel()
- 位置: L190-192
- 役割: パネルを強制的に隠す。
- 触るとき: 項目を選んだ後にパネルが閉じない、または早く閉じすぎる問題を調べるときに見る。
- 呼び出し先: `this.#panelList.hide()`

## SearchModeSwitcher.#openPreferences()
- 位置: L194-200
- 役割: 設定の検索ペインを開き、urlbar なら設定を選んだ記録を送る。
- 触るとき: 設定項目から開く画面を変えるときに見る。
- 呼び出し先: `this.#input.parentController.openPreferences()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked.settings.add()`
- 参照: `this.#input.sapName`

## SearchModeSwitcher.exitSearchMode()
- 位置: L208-215
- 役割: イベントの既定動作を止め、検索モードを解除し、選択位置とエンジン一覧を初期化したうえで、既定のエンジンで検索を開始し直す。
- 触るとき: 検索モードの閉じるボタンで結果が変わらない、または解除後の選択がずれる問題を調べるときに見る。
- 呼び出し先: `event.preventDefault()`, `this.#input.startQuery()`
- 参照: `this.#engines`, `this.#input.searchMode`, `this.#selectedIndex`

## SearchModeSwitcher.onSearchModeChanged()
- 位置: L220-228
- 役割: ウィンドウが閉じていなければ、有効時にアイコンを searchModeChanged 付きで更新する。
- 触るとき: 検索モードの切り替え時にアイコンが古いままになる問題を調べるときに見る。
- 呼び出し先: `this.#isEnabled()`
- 条件付き依存: `if (this.#isEnabled())` → `this.updateSearchIcon()`
- 参照: `window.closed`

## SearchModeSwitcher.handleEvent()
- 位置: L230-309
- 役割: イベントの発生元と種類で振り分ける。パネル項目、閉じるボタン、searchmodechanged、wordmark のメディアクエリ変更、focus、focusin と focusout、showing と hidden、keydown を処理する。keydown では、ビューが開いていれば Tab と Escape、下キーでパネルを表示する。
- 触るとき: キーボードやフォーカスの挙動を変える、またはボタンのイベントが効かない問題を調べるときに見る。
- 条件付き依存: `if (event.currentTarget.localName == "panel-item")` → `this.#handlePanelItemEvent()`
- 条件付き依存: `if (event.currentTarget == this.#closebutton)` → `event.stopPropagation()`
- 条件付き依存: `if (event.type == "click")` → `this.#input.focus()`
- 条件付き依存: `if (event.type == "click")` → `this.exitSearchMode()`
- 条件付き依存: `if (event.type == "searchmodechanged")` → `this.onSearchModeChanged()`
- 条件付き依存: `if (this.#input.variantA || this.#input.variantB)` → `this.updateSearchIcon()`
- 条件付き依存: `if (event.type == "focus")` → `this.#input.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if (event.type == "focusout")` → `this.#input.contains()`
- 条件付き依存: `if (event.type == "showing")` → `this.#onPopupShowing()`
- 条件付き依存: `if (document.activeElement == this.#button)` → `this.#input.focus()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `this.#input.focus()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `this.#input.view.selectBy()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `event.preventDefault()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `this.#input.view.close()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_DOWN)` → `this.#panelList.show()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_TAB`, `document.activeElement`, `event.currentTarget`, `event.currentTarget.localName`, `event.keyCode`, `event.relatedTarget`, `event.shiftKey`, `event.type`, `this.#button`, `this.#button.tabIndex`, `this.#closebutton`, `this.#input.variantA`, `this.#input.variantB`, `this.#input.view.isOpen`, `this.#noWordmarkQuery`

## SearchModeSwitcher.#handlePanelItemEvent()
- 位置: L318-381
- 役割: click、keydown、auxclick の種類を確かめ、キーボードの click は keydown 側で扱う。panel item の data-action に応じて、設定を開く、エンジンの検索モードに入る、ローカル検索モードに入る、追加エンジンを導入するを実行する。
- 触るとき: パネル項目の選び方や data-action ごとの動作を変えるときに見る。
- 呼び出し先: `event.preventDefault()`, `mouseEvent.stopPropagation()`, `this.#input.controller.engineStore.getEngine()`, `this.#installOpenSearchEngine()`, `this.#localSearch()`, `this.#openPreferences()`, `this.#remoteSearch()`, `this.closePanel()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `MouseEvent.MOZ_SOURCE_KEYBOARD`, `event.currentTarget`, `event.type`, `keyboardEvent.keyCode`, `mouseEvent.button`, `mouseEvent.inputSource`, `panelItem._engine`, `panelItem.dataset.action`, `panelItem.dataset.engineId`, `panelItem.dataset.restrict`

## SearchModeSwitcher.#addCommandListeners()
- 位置: L386-390
- 役割: 項目に click、keydown、auxclick のリスナーを付ける。
- 触るとき: パネル項目に新しい操作を加えるときに見る。
- 呼び出し先: `panelItem.addEventListener()`

## SearchModeSwitcher.onSearchEngineUpdate()
- 位置: L392-402
- 役割: ウィンドウが閉じていなければ、changed か default の変更でアイコンを更新する。
- 触るとき: エンジンの変更や既定の変更がボタンに反映されないときに見る。
- 呼び出し先: `this.updateSearchIcon()`
- 参照: `window.closed`

## SearchModeSwitcher.onPrefChanged()
- 位置: L410-448
- 役割: SKIP_TAB_STOP_PREF の変更で skipTabStop を有効または無効にする。検索バーの SAP では他の設定は無視する。それ以外は、scotchBonnet.enableOverride の切り替えで監視を開始・停止し、keyword.enabled の変更でアイコンを更新する。
- 触るとき: 設定変更の直後にボタンの状態が合わないときに見る。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (pref == SKIP_TAB_STOP_PREF)` → `this.#isEnabled()`
- 条件付き依存: `if (this.#isEnabled())` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get(pref))` → `this.#enableSkipTabStop()`
- 条件付き依存: `if (!(UrlbarPrefs.get(pref)))` → `this.#disableSkipTabStop()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `this.#enableObservers()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `this.updateSearchIcon()`
- 条件付き依存: `if (!(UrlbarPrefs.get("scotchBonnet.enableOverride")))` → `this.#disableObservers()`
- 参照: `this.#input.isSearchbarSAP`, `window.closed`

## SearchModeSwitcher.handleKeyDown()
- 位置: L456-472
- 役割: Alt+上下なら一覧を開き、Accel+上下ならエンジンを切り替える。どちらでもイベントを止めて true を返し、それ以外は false を返す。
- 触るとき: 上下キーのショートカットを変える、または入力欄側の keydown から呼ばれる経路を追うときに見る。
- 呼び出し先: `event.getModifierState()`
- 条件付き依存: `if (event.altKey)` → `this.#handleAltUpDown()`
- 条件付き依存: `if (!(event.altKey))` → `event.getModifierState()`
- 条件付き依存: `if (event.getModifierState("Accel"))` → `this.#handleAccelUpDown()`
- 条件付き依存: `if ( (event.keyCode == KeyEvent.DOM_VK_UP || event.keyCode == KeyEvent.DOM_VK_DOWN) && (event.altKey || event.getModifierState("Accel")) )` → `event.stopPropagation()`
- 条件付き依存: `if ( (event.keyCode == KeyEvent.DOM_VK_UP || event.keyCode == KeyEvent.DOM_VK_DOWN) && (event.altKey || event.getModifierState("Accel")) )` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_UP`, `event.altKey`, `event.keyCode`

## SearchModeSwitcher.#handleAltUpDown()
- 位置: L474-477
- 役割: 統合検索ボタンにフォーカスを移し、パネルをボタン基準で表示する。
- 触るとき: Alt+上下で一覧が出る位置やフォーカス先を調べるときに見る。
- 呼び出し先: `this.#input.controller.focusOnUnifiedSearchButton()`, `this.#panelList.show()`
- 参照: `this.#button`

## SearchModeSwitcher.#handleAccelUpDown()
- 位置: async L479-505
- 役割: エンジン一覧が空なら読み込み、選択インデックスを上下に循環させ、そのエンジンを検索モードに設定する。検索語があれば autofill を無効にして検索を開始する。
- 触るとき: Accel+上下で切り替わる順番や循環の仕方を変えるときに見る。
- 呼び出し先: `this.#getSearchString()`, `this.#input.setSearchMode()`
- 条件付き依存: `if (!this.#engines.length)` → `this.#populateEngines()`
- 条件付き依存: `if (searchString)` → `this.#input.startQuery()`
- 参照: `KeyEvent.DOM_VK_UP`, `UrlbarShared.RESULT_SOURCE.SEARCH`, `event.keyCode`, `selectedEngine?.name`, `selectedEngine?.source`, `this.#engines`, `this.#engines.length`, `this.#input.window.gBrowser.selectedBrowser`, `this.#selectedIndex`

## SearchModeSwitcher.#populateEngines()
- 位置: async L507-533
- 役割: エンジンストアを初期化し、hideOneOffButton でないエンジンを取る。初期化に失敗してもローカル検索は残す。urlbar では設定画面の再設計が有効なら全ローカル検索を、無効なら設定で有効なものだけを加える。
- 触るとき: ポップアップに出すエンジンやローカル検索モードの絞り込みを変えるときに見る。
- 呼び出し先: `this.#input.controller.engineStore .getEngines()`, `this.#input.controller.engineStore .getEngines() .filter()`, `this.#input.controller.engineStore.init()`
- 条件付き依存: `if (!(this.#input.sapName != "urlbar"))` → `searchEngines.concat()`
- 条件付き依存: `if (!(this.#input.sapName != "urlbar"))` → `UrlbarShared.LOCAL_SEARCH_MODES.filter()`
- 条件付き依存: `if (!(this.#input.sapName != "urlbar"))` → `UrlbarPrefs.get()`
- 参照: `engine.hideOneOffButton`, `engine.pref`, `this.#engines`, `this.#input.sapName`

## SearchModeSwitcher.toggleAddEnginesBadge()
- 位置: L541-557
- 役割: 表示しない指定、常時表示オプションが偽、隣接する検索バーがある場合はバッジを外す。それ以外は #badgeIfUnderSiteCap で上限を確かめて付ける。SAP では属性を直接切り替える。
- 触るとき: エンジン追加のバッジが出ない、または出すぎるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#badgeIfUnderSiteCap()`
- 条件付き依存: `if (this.#input.isSearchbarSAP)` → `this.#button.toggleAttribute()`
- 条件付き依存: `if ( !show || !UrlbarPrefs.get("unifiedSearchButton.always") || this.#hasAdjacentSearchbar )` → `this.#button.removeAttribute()`
- 参照: `this.#hasAdjacentSearchbar`, `this.#input.isSearchbarSAP`

## SearchModeSwitcher.#hasAdjacentSearchbar()
- 位置: L564-571
- 役割: SAP から呼ばれたら例外を投げる。そうでなければ search-container ウィジェットが CustomizableUI に配置されているかを返す。
- 触るとき: ツールバーに検索バーがあるときにバッジを隠す条件を変えるときに見る。
- 呼び出し先: `lazy?.CustomizableUI.getPlacementOfWidget()`
- 参照: `this.#input.isSearchbarSAP`

## SearchModeSwitcher.#contentPrefs()
- 位置: L576-580
- 役割: nsIContentPrefService2 のサービスを取得して返す。
- 触るとき: サイトごとの設定の保存先や取得方法を変えるときに見る。
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`
- 参照: `Ci.nsIContentPrefService2`
- XPCOM: [`nsIContentPrefService2`](../../../../dom/interfaces/base/nsIContentPrefService2.idl.md) / `@mozilla.org/content-pref/service;1` → `ContentPrefService2` (toolkit/components/contentprefs/components.conf)

## SearchModeSwitcher.#badgeIfUnderSiteCap()
- 位置: L586-638
- 役割: 選択中ブラウザの URL について表示回数を content pref から読み、上限(3 回)未満ならバッジを付けて表示回数を増やす。キャッシュがあれば同期的に使う。chrome 専用で、content から呼ぶと例外。
- 触るとき: 同じサイトでのバッジ表示回数の上限や数え方を変えるときに見る。
- 呼び出し先: `this.#contentPrefs.getByDomainAndName()`, `this.#contentPrefs.getCachedByDomainAndName()`
- 条件付き依存: `if (cached)` → `apply()`
- 条件付き依存: `if (cached)` → `Number()`
- 参照: `browser.loadContext`, `browser?.currentURI`, `cached.value`, `this.#input.window.gBrowser?.selectedBrowser`, `uri.spec`

## apply()
- 位置: L599-613
- 役割: 読み出した回数に応じて表示を決める。既に表示済みのページなら維持し、それ以外は上限未満なら表示して数える。読み出し中にページが変わっていれば何もしない。
- 触るとき: バッジ表示の判定条件や、読み出し中のページ切り替えの扱いを変えるときに見る。
- 呼び出し先: `this.#button.toggleAttribute()`, `this.#countedBadgeFor.get()`
- 条件付き依存: `if (show)` → `this.#countBadgeShown()`
- 参照: `this.#input.window.gBrowser?.selectedBrowser`

## SearchModeSwitcher.handleResult()
- 位置: L631-633
- 役割: content pref の値を数値にして count に格納する。
- 触るとき: 表示回数の読み出し結果がバッジ判定に使われない問題を調べるときに見る。
- 呼び出し先: `Number()`
- 参照: `pref.value`

## SearchModeSwitcher.handleError()
- 位置: L634-634
- 役割: 読み出しのエラーを何もせず無視する。
- 触るとき: 読み出しに失敗したときにバッジが出ない挙動を確かめるときに見る。

## handleCompletion()
- 位置: L635-635
- 役割: 読み出しが完了したら、読んだ回数を使って apply を呼ぶ。
- 触るとき: 読み出し完了後の判定の順序を変えるときに見る。
- 呼び出し先: `apply()`

## SearchModeSwitcher.#countBadgeShown()
- 位置: L648-660
- 役割: 同じブラウザと同じページについて既に数えていれば何もしない。数えていなければページを記録し、表示回数を 1 増やして content pref に保存する。
- 触るとき: 表示回数が二重に増える、または増えない問題を調べるときに見る。
- 呼び出し先: `this.#contentPrefs.set()`, `this.#countedBadgeFor.get()`, `this.#countedBadgeFor.set()`
- 参照: `browser.loadContext`

## SearchModeSwitcher.updateSearchIcon()
- 位置: async L670-712
- 役割: 検索モードのエンジン(無ければ既定エンジン)の情報を取得し、アイコンかワードマーク、ラベル、ボタンのタイトルを更新する。現在の検索モードと一致しない結果は捨てる。キーワード無効時は専用のタイトルを使う。
- 触るとき: 検索モードボタンの見た目や、読み上げ名がずれるときに見る。
- 呼び出し先: `UrlbarShared.keywordEnabled()`, `this.#getSearchIcon()`, `this.#input.querySelector()`
- 条件付き依存: `if (wordmark)` → `this.#button.removeAttribute()`
- 条件付き依存: `if (wordmark)` → `this.#button.setAttribute()`
- 条件付き依存: `if (!(wordmark))` → `this.#button.setAttribute()`
- 条件付き依存: `if (!(wordmark))` → `this.#button.removeAttribute()`
- 条件付き依存: `if (!(showLabel))` → `labelEl.replaceChildren()`
- 条件付き依存: `if (!UrlbarShared.keywordEnabled(this.#input.sapName))` → `this.#setButtonTitle()`
- 条件付き依存: `if (label)` → `this.#setButtonTitle()`
- 条件付き依存: `if (!(label))` → `this.#setButtonTitle()`
- 参照: `labelEl.textContent`, `searchMode?.engineName`, `searchMode?.source`, `this.#input.sapName`, `this.#input.searchMode`, `this.#input.variantA`, `this.#input.variantB`

## SearchModeSwitcher.#setButtonTitle()
- 位置: async L726-736
- 役割: Fluent のメッセージを取得し、最後に出した要求と一致する場合だけ、タイトルと aria-label に設定する。
- 触るとき: ボタンのツールチップや読み上げ名が古いまま残る問題を調べるときに見る。
- 呼び出し先: `document.l10n.formatMessages()`, `message.attributes.find()`, `this.#button.removeAttribute()`
- 参照: `a.name`, `message.attributes.find(a => a.name == "title").value`, `this.#button.ariaLabel`, `this.#button.title`, `this.#buttonTitleRequest`

## SearchModeSwitcher.#getSearchIcon()
- 位置: async L738-775
- 役割: キーワード無効で検索モードでなければグローブのアイコンを返す。urlbar で入力中、先頭の結果が URL かタブ切り替えならグローブを返す。それ以外は #getDisplayedEngineDetails の結果を返す。
- 触るとき: ボタンのアイコンの出し分けの条件を変えるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.keywordEnabled()`, `this.#getDisplayedEngineDetails()`
- 条件付き依存: `if ( UrlbarPrefs.get("unifiedSearchButton.always") && !this.#lastInputValue && this.#input.focused && this.#input.value.length )` → `this.#input.view?.getResultAtIndex()`
- 参照: `SearchModeSwitcher.ICON_GLOBE`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.URL`, `result.type`, `this.#input.focused`, `this.#input.sapName`, `this.#input.searchMode`, `this.#input.value`, `this.#input.value.length`, `this.#lastInputValue`

## SearchModeSwitcher.#getEngineWordmark()
- 位置: L786-796
- 役割: variantA または variantB で、設定エンジンかつ prefers-contrast でない場合に、エンジン id の先頭部分が WORDMARK_ENGINE_FAMILIES にあればその値を返す。それ以外は null。
- 触るとき: New Tab 検索バーでワードマークを出すエンジンを増減させるときに見る。
- 呼び出し先: `WORDMARK_ENGINE_FAMILIES.has()`, `engine.id.split()`
- 参照: `engine.isConfigEngine`, `this.#input.variantA`, `this.#input.variantB`, `this.#noWordmarkQuery.matches`

## SearchModeSwitcher.#getSearchModeLabel()
- 位置: async L798-802
- 役割: source に対応するローカル検索モードの uiLabel を Fluent から取り、その値を返す。
- 触るとき: ローカル検索モードの表示名が誤るときに見る。
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`, `getL10n()`, `getL10n().formatMessages()`
- 参照: `m.source`, `mode.uiLabel`, `str.value`

## SearchModeSwitcher.#getDisplayedEngineDetails()
- 位置: async L804-835
- 役割: エンジン指定の検索モードでは、エンジンストアの初期化後に該当エンジン(無ければ既定)のラベル、アイコン、ワードマークを返す。取得できなければ虫眼鏡アイコン。ローカル検索モードではラベルとアイコンを返す。
- 触るとき: ボタンに出るエンジン名やアイコンが誤るときに見る。
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`, `this.#getSearchModeLabel()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `this.#input.controller.engineStore.init()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `this.#input.controller.engineStore.getEngineByName()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `engine.getIconURL()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `this.#getEngineWordmark()`
- 参照: `SearchModeSwitcher.ICON_GLASS`, `engine.name`, `m.source`, `mode.icon`, `searchMode.engineName`, `searchMode.source`, `this.#input.controller.engineStore.default`

## SearchModeSwitcher.#buildSearchModeList()
- 位置: async L840-908
- 役割: 既存の panel-item を消し、ローカル検索とエンジンの項目を区切りの前に入れ、設定項目を追加する。続けて追加可能な OpenSearch エンジンを最大 3 件、フッター区切りの後に入れる。最後に区切り線の表示を調整し、rebuild イベントを出す。
- 触るとき: ポップアップの項目の並びや数を変えるときに見る。
- 呼び出し先: `document.l10n.setAttributes()`, `footerSeparator.after()`, `footerSeparator.toggleAttribute()`, `item.remove()`, `lazy.OpenSearchManager.getInstallableEngines()`, `menuitem.classList.add()`, `openSearchEngines.slice()`, `this.#addCommandListeners()`, `this.#buildSettingsButton()`, `this.#createButton()`, `this.#panelList.dispatchEvent()`, `this.#panelList.querySelector()`, `this.#panelList.querySelectorAll()`, `this.#populateEngines()`
- 条件付き依存: `if (engine.source)` → `footerSeparator.before()`
- 条件付き依存: `if (engine.source)` → `this.#buildLocalSearchButton()`
- 条件付き依存: `if (engine.name)` → `this.#buildEngineSearchButton()`
- 条件付き依存: `if (engine.name)` → `installedEngineSeparator.before()`
- 条件付き依存: `if (this.#panelList.wasOpenedByKeyboard)` → `this.#panelList.focusWalker.nextNode()`
- 参照: `SearchModeSwitcher.MAX_OPENSEARCH_ENGINES`, `browser.selectedBrowser`, `engine.icon`, `engine.name`, `engine.source`, `engine.title`, `footerSeparator.previousElementSibling`, `menuitem._engine`, `menuitem.dataset.action`, `menuitem.dataset.engineName`, `this.#engines`, `this.#input.window.gBrowser`, `this.#panelList`, `this.#panelList.focusWalker.currentNode`, `this.#panelList.wasOpenedByKeyboard`

## SearchModeSwitcher.#whereToOpenSerp()
- 位置: L915-924
- 役割: リンクの開き方を whereToOpenLink で求める。タブ系ならそのまま返し、それ以外は current を返す。ウィンドウで開くことはない。
- 触るとき: 検索結果ページの開き先の決め方(Shift の意味など)を変えるときに見る。
- 呼び出し先: `UrlbarContentUtils.whereToOpenLink()`, `where.startsWith()`

## SearchModeSwitcher.#buildSettingsButton()
- 位置: L930-943
- 役割: 設定の項目を作り、data-action を openpreferences にする。browser.nova.enabled に応じて文言を選ぶ。
- 触るとき: 設定項目の文言や位置を変えるときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `document.l10n.setAttributes()`, `menuitem.classList.add()`, `this.#addCommandListeners()`, `this.#createButton()`, `this.#panelList.appendChild()`
- 参照: `menuitem.dataset.action`

## SearchModeSwitcher.#buildEngineSearchButton()
- 位置: async L948-966
- 役割: エンジンのアイコンを取得して項目を作り、新規かつ app 提供のエンジンには new バッジを付ける。data-action を searchmode にする。
- 触るとき: エンジン項目の見た目や動作の割り当てを変えるときに見る。
- 呼び出し先: `engine.getIconURL()`, `engine.isNew()`, `menuitem.classList.add()`, `menuitem.setAttribute()`, `this.#addCommandListeners()`, `this.#createButton()`
- 条件付き依存: `if (engine.isNew() && engine.isAppProvided)` → `menuitem.setAttribute()`
- 参照: `engine.id`, `engine.isAppProvided`, `engine.name`, `menuitem.dataset.action`, `menuitem.dataset.engineId`, `menuitem.dataset.engineName`

## SearchModeSwitcher.#buildLocalSearchButton()
- 位置: async L972-989
- 役割: ローカル検索モードの項目を作り、data-action を localsearchmode にする。キーボードショートカットがあれば CustomizableUI に登録する。
- 触るとき: ローカル検索の項目やそのショートカットを変えるときに見る。
- 呼び出し先: `UrlbarShared.getResultSourceName()`, `document.l10n.setAttributes()`, `menuitem.classList.add()`, `this.#addCommandListeners()`, `this.#createButton()`, `this.#getDisplayedEngineDetails()`
- 条件付き依存: `if (mode.keyId)` → `menuitem.setAttribute()`
- 条件付き依存: `if (mode.keyId)` → `lazy.CustomizableUI.addShortcut()`
- 参照: `menuitem.dataset.action`, `menuitem.dataset.restrict`, `mode.keyId`, `mode.restrict`, `mode.source`, `mode.uiLabel`

## SearchModeSwitcher.#localSearch()
- 位置: L997-1005
- 役割: restrict トークンと検索語を連結して、searchbutton の入り口で検索する。urlbar なら local_search の記録を送る。
- 触るとき: ローカル検索の入り方や検索語の組み立てを変えるときに見る。
- 呼び出し先: `this.#getSearchString()`, `this.#input.search()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked.local_search.add()`
- 参照: `this.#input.sapName`

## SearchModeSwitcher.#remoteSearch()
- 位置: L1016-1046
- 役割: 開き先が current で Shift が無ければ、パネルを閉じてエンジンの検索モードに入る。それ以外は、current なら閉じてから検索結果ページを開く。urlbar では、ビルトインか追加エンジンかを記録する。
- 触るとき: エンジンを選んだときに検索モードに入るか検索結果ページを開くかを変えるときに見る。
- 呼び出し先: `this.#getSearchString()`, `this.#whereToOpenSerp()`
- 条件付き依存: `if (!event.shiftKey && whereToOpenSerp == "current")` → `this.closePanel()`
- 条件付き依存: `if (!event.shiftKey && whereToOpenSerp == "current")` → `this.#input.search()`
- 条件付き依存: `if (whereToOpenSerp == "current")` → `this.closePanel()`
- 条件付き依存: `if (!(!event.shiftKey && whereToOpenSerp == "current"))` → `this.#input.openSearchEnginePage()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked[ searchEngine.isConfigEngine ? "builtin_search" : "addon_search" ].add()`
- 参照: `Glean.urlbarUnifiedsearchbutton.picked`, `event.shiftKey`, `searchEngine.isConfigEngine`, `this.#input.sapName`

## SearchModeSwitcher.#getSearchString()
- 位置: L1053-1058
- 役割: pageproxystate が valid(表示中ページの URL が入っている)なら空文字を返し、それ以外は入力値を返す。
- 触るとき: 表示中ページの URL が検索語として送られる問題を調べるときに見る。
- 呼び出し先: `this.#input.getAttribute()`
- 参照: `this.#input.value`

## SearchModeSwitcher.eventTargetIsPanelItem()
- 位置: L1067-1079
- 役割: イベントの対象が追加エンジン、インストール済みエンジン、ローカル検索のいずれかの class を持つかを返す。
- 触るとき: パネル項目かどうかの判定条件に項目の種類を足すときに見る。
- 呼び出し先: `classList.contains()`
- 参照: `event?.target`, `target.classList`

## SearchModeSwitcher.#enableObservers()
- 位置: L1081-1099
- 役割: エンジンストアの変更監視を登録し、ボタンの focus と keydown、skipTabStop、パネルの表示と非表示、閉じるボタン、検索モードの変更、wordmark のメディアクエリ変更にリスナーを付ける。
- 触るとき: 監視対象を増やす、またはボタンのイベントが届かないときに見る。
- 呼び出し先: `UrlbarPrefs.get()`, `this.#button.addEventListener()`, `this.#closebutton.addEventListener()`, `this.#input.addEventListener()`, `this.#input.controller.engineStore.addObserver()`, `this.#noWordmarkQuery.addEventListener()`, `this.#panelList.addEventListener()`
- 条件付き依存: `if (UrlbarPrefs.get(SKIP_TAB_STOP_PREF))` → `this.#enableSkipTabStop()`
- 参照: `this.onSearchEngineUpdate`

## SearchModeSwitcher.#disableObservers()
- 位置: L1101-1119
- 役割: #enableObservers で付けたリスナーをすべて外し、skipTabStop も無効にする。
- 触るとき: 入力欄を外した後にイベントが残る問題を調べるときに見る。
- 呼び出し先: `this.#button.removeEventListener()`, `this.#closebutton.removeEventListener()`, `this.#disableSkipTabStop()`, `this.#input.controller.engineStore.removeObserver()`, `this.#input.removeEventListener()`, `this.#noWordmarkQuery.removeEventListener()`, `this.#panelList.removeEventListener()`
- 参照: `this.onSearchEngineUpdate`

## SearchModeSwitcher.#enableSkipTabStop()
- 位置: L1127-1131
- 役割: ボタンに keyNav=skipTabStop を付け、入力欄の focusin と focusout を監視する。
- 触るとき: Tab キーの順序でボタンが飛ばされる、または入ってしまう問題を調べるときに見る。
- 呼び出し先: `this.#button.setAttribute()`, `this.#input.addEventListener()`

## SearchModeSwitcher.#disableSkipTabStop()
- 位置: L1133-1138
- 役割: keyNav 属性を外し、tabIndex を -1 にして、入力欄の focusin と focusout の監視を外す。
- 触るとき: skipTabStop をオフにしたあとに Tab の順序が戻らない問題を調べるときに見る。
- 呼び出し先: `this.#button.removeAttribute()`, `this.#input.removeEventListener()`
- 参照: `this.#button.tabIndex`

## SearchModeSwitcher.#createButton()
- 位置: L1146-1159
- 役割: panel-item を作り、ラベルがあれば本文に設定し、--icon-url に icon か既定のエンジンアイコンを設定して返す。
- 触るとき: パネル項目の作り方や既定のアイコンを変えるときに見る。
- 呼び出し先: `document.createElement()`, `panelitem.style.setProperty()`
- 参照: `panelitem.textContent`

## SearchModeSwitcher.#installOpenSearchEngine()
- 位置: async L1167-1187
- 役割: エンジンストアへの追加を待つオブザーバーを登録し、urlbar では addon_search を記録し、SearchUIUtils.addOpenSearchEngine でエンジンを導入する。
- 触るとき: ページ上の OpenSearch エンジンを導入する流れや、導入後の記録を変えるときに見る。
- 呼び出し先: `lazy.SearchUIUtils.addOpenSearchEngine()`, `this.#input.controller.engineStore.addObserver()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked.addon_search.add()`
- 参照: `engine.icon`, `engine.uri`, `this.#input.sapName`, `this.#input.window.gBrowser.selectedBrowser.browsingContext`

## observer()
- 位置: L1169-1176
- 役割: 導入された新しいエンジンで検索モードに入り、自分自身をエンジンストアのオブザーバーから外す。
- 触るとき: 導入直後に検索モードへ入らない問題を調べるときに見る。
- 呼び出し先: `this.#getSearchString()`, `this.#input.controller.engineStore.removeObserver()`, `this.#input.search()`
