# browser/components/search/SearchOneOffs.sys.mjs

source: browser/components/search/SearchOneOffs.sys.mjs
source-hash: 7f6f1f35b2a1107e3a84b267831359042ae8c863
lines: 1183

## <module>
- 役割: 検索バーと URL バーの下に出る one-off 検索ボタン群 SearchOneOffs を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SearchOneOffs.constructor()
- 位置: L44-134
- 役割: コンテナに one-off 用の XUL を差し込み、子要素の参照を取り、クリック・キー・コンテキストメニューの各イベントと検索エンジン変更の通知を登録する。
- 触るとき: one-off の DOM 構造を変えたり、新しい通知や要素を購読させたりするとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.obs.addObserver()`, `aEvent.stopPropagation()`, `this.addEventListener()`, `this.container.appendChild()`, `this.contextMenuPopup.addEventListener()`, `this.querySelector()`, `this.window.MozXULElement.parseXULToFragment()`
- 参照: `container.documentGlobal`, `container.ownerDocument`, `this.QueryInterface`, `this._engineInfo`, `this._popup`, `this._query`, `this._rebuilding`, `this._selectedButton`, `this._textbox`, `this._textboxWidth`, `this.buttons`, `this.container`, `this.contextMenuPopup`, `this.disableOneOffsHorizontalKeyNavigation`, `this.document`, `this.header`, `this.settingsButton`, `this.telemetryOrigin`, `this.window`
- XPCOM: `Services.obs`

## listener()
- 位置: L108-108
- 役割: コンテキストメニューの popup イベントが外側の autocomplete に届かないよう伝播を止める。
- 触るとき: コンテキストメニューを開いたときに外側の候補リストが誤って反応するとき。
- 呼び出し先: `aEvent.stopPropagation()`

## SearchOneOffs.addEventListener()
- 位置: L136-138
- 役割: イベント登録をコンテナ要素へ転送する。
- 触るとき: one-off のイベントを購読する要素をコンテナに統一したいとき。
- 呼び出し先: `this.container.addEventListener()`

## SearchOneOffs.removeEventListener()
- 位置: L140-142
- 役割: イベントの登録解除をコンテナ要素へ転送する。
- 触るとき: addEventListener と対になる解除処理を追加・確認するとき。
- 呼び出し先: `this.container.removeEventListener()`

## SearchOneOffs.dispatchEvent()
- 位置: L144-146
- 役割: イベント発火をコンテナ要素へ転送する。
- 触るとき: SelectedOneOffButtonChanged などのイベントを外に知らせるとき。
- 呼び出し先: `this.container.dispatchEvent()`

## SearchOneOffs.getAttribute()
- 位置: L148-150
- 役割: 属性の取得をコンテナ要素へ転送する。
- 触るとき: includecurrentengine などの属性を one-off の挙動判定に使うとき。
- 呼び出し先: `this.container.getAttribute()`

## SearchOneOffs.hasAttribute()
- 位置: L152-154
- 役割: 属性の有無の判定をコンテナ要素へ転送する。
- 触るとき: is_searchbar など、コンテナの属性で分岐を書くとき。
- 呼び出し先: `this.container.hasAttribute()`

## SearchOneOffs.setAttribute()
- 位置: L156-158
- 役割: 属性の設定をコンテナ要素へ転送する。
- 触るとき: コンテナの表示状態を外から属性で切り替えるとき。
- 呼び出し先: `this.container.setAttribute()`

## SearchOneOffs.querySelector()
- 位置: L160-162
- 役割: セレクタによる検索をコンテナ要素へ転送する。
- 触るとき: one-off の子要素をセレクタで探す処理を書くとき。
- 呼び出し先: `this.container.querySelector()`

## SearchOneOffs.handleEvent()
- 位置: L164-171
- 役割: DOM イベントを _on_<種別> メソッドへ振り分け、無ければ例外を投げる。
- 触るとき: 新しいイベントを one-off で扱うとき、対応する _on_ メソッドを足し忘れていないか確かめるとき。
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## SearchOneOffs.willHide()
- 位置: async L177-188
- 役割: エンジン情報をもとに、one-off を隠すかどうかを判定して返す。結果は _engineInfo に保存する。
- 触るとき: 候補が既定エンジン 1 つだけのときに one-off を隠す条件を変えるとき。
- 呼び出し先: `this.getEngineInfo()`
- 参照: `engineInfo.default.name`, `engineInfo.engines`, `engineInfo.engines.length`, `engineInfo.engines[0].name`, `engineInfo.willHide`, `this._engineInfo.willHide`, `this._engineInfo?.willHide`

## SearchOneOffs.invalidateCache()
- 位置: L194-198
- 役割: 再構築中でなければエンジン情報のキャッシュを捨て、次の表示で作り直させる。
- 触るとき: エンジンの追加・削除後に one-off の一覧が古いままになるとき。
- 参照: `this._engineInfo`, `this._rebuilding`

## SearchOneOffs.buttonWidth()
- 位置: L206-208
- 役割: one-off ボタン 1 つの幅を 48 として返す。検索バー側でも使う。
- 触るとき: ボタンの見た目の幅を変えると検索バー側の計算も合わせる必要があるとき。

## SearchOneOffs.popup()
- 位置: L216-233
- 役割: popup を差し替えて popupshowing と popuphidden を購読し直し、開いていれば再構築する。
- 触るとき: one-off を載せるポップアップの種類を変えたり、開いた時の再構築を調べるとき。
- 条件付き依存: `if (this._popup)` → `this._popup.removeEventListener()`
- 条件付き依存: `if (val)` → `val.addEventListener()`
- 条件付き依存: `if (val && val.state != "closed")` → `this._rebuild()`
- 参照: `this._popup`, `val.state`

## SearchOneOffs.popup()
- 位置: L235-237
- 役割: 現在の popup 要素を返す。
- 触るとき: one-off の所属する popup を他から参照するとき。
- 参照: `this._popup`

## SearchOneOffs.textbox()
- 位置: L248-256
- 役割: テキスト入力の input 監視を付け替え、入力に応じて query を更新するようにする。
- 触るとき: one-off が追う入力欄を変えるとき、または入力が one-off に反映されないとき。
- 条件付き依存: `if (this._textbox)` → `this._textbox.removeEventListener()`
- 条件付き依存: `if (val)` → `val.addEventListener()`
- 参照: `this._textbox`

## SearchOneOffs.style()
- 位置: L258-260
- 役割: コンテナの style を返す。
- 触るとき: one-off の見た目をコードから直接変えるとき。
- 参照: `this.container.style`

## SearchOneOffs.textbox()
- 位置: L262-264
- 役割: 設定された入力欄を返す。
- 触るとき: one-off と入力欄の結び付きを他から確かめるとき。
- 参照: `this._textbox`

## SearchOneOffs.query()
- 位置: L274-292
- 役割: 検索語を保存し、入力中は選択中の設定ボタンや one-off 以外を選択解除する。
- 触るとき: 入力に応じて one-off の選択がどう外れるかを変えるとき。
- 条件付き依存: `if (this.isViewOpen)` → `this.selectedButton.classList.contains()`
- 条件付き依存: `if (this.isViewOpen)` → `this.hasAttribute()`
- 参照: `this._query`, `this.isViewOpen`, `this.selectedButton`, `this.settingsButton`

## SearchOneOffs.query()
- 位置: L294-296
- 役割: 現在の検索語を返す。
- 触るとき: one-off が表示中の検索語を他から読むとき。
- 参照: `this._query`

## SearchOneOffs.selectedButton()
- 位置: L305-327
- 役割: 選択中ボタンの selected 属性と aria-activedescendant を更新し、SelectedOneOffButtonChanged を発火する。
- 触るとき: one-off の選択表示や支援技術向けの状態の付け方を変えるとき。
- 呼び出し先: `this.dispatchEvent()`
- 条件付き依存: `if (previousButton)` → `previousButton.removeAttribute()`
- 条件付き依存: `if (val)` → `val.toggleAttribute()`
- 条件付き依存: `if (val)` → `this.textbox.setAttribute()`
- 条件付き依存: `if (!(val))` → `this.textbox.getAttribute()`
- 条件付き依存: `if (!(val))` → `active.includes()`
- 条件付き依存: `if (active && active.includes("-engine-one-off-item-"))` → `this.textbox.removeAttribute()`
- 参照: `this._selectedButton`, `this.textbox`, `val.id`

## SearchOneOffs.selectedButton()
- 位置: L329-331
- 役割: 現在選択中のボタンを返す。
- 触るとき: 選択中のエンジンを他の処理が使うとき。
- 参照: `this._selectedButton`

## SearchOneOffs.selectedButtonIndex()
- 位置: L340-343
- 役割: 選択可能なボタン一覧の index でボタンを選択する。
- 触るとき: キーボード操作で index 指定の選択をするとき。
- 呼び出し先: `this.getSelectableButtons()`
- 参照: `this.selectedButton`

## SearchOneOffs.selectedButtonIndex()
- 位置: L345-353
- 役割: 選択中ボタンの index を選択可能な一覧の中で返す。無ければ -1 を返す。
- 触るとき: キーボード操作で現在位置を求めるとき。
- 呼び出し先: `this.getSelectableButtons()`
- 参照: `buttons.length`, `this._selectedButton`

## SearchOneOffs.getEngineInfo()
- 位置: async L355-382
- 役割: 既定エンジンと表示対象の一覧を取得する。既定を除き、hideOneOffButton のエンジンも除く。結果は _engineInfo にキャッシュする。
- 触るとき: one-off に出すエンジンの絞り込み条件を変えるとき、または表示が古いキャッシュのせいで変わらないとき。
- 呼び出し先: `(await lazy.SearchService.getVisibleEngines()).filter()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SearchService.getVisibleEngines()`, `this.getAttribute()`
- 条件付き依存: `if (lazy.PrivateBrowsingUtils.isWindowPrivate(this.window))` → `lazy.SearchService.getDefaultPrivate()`
- 条件付き依存: `if (!(lazy.PrivateBrowsingUtils.isWindowPrivate(this.window)))` → `lazy.SearchService.getDefault()`
- 参照: `defaultEngine.name`, `e.hideOneOffButton`, `e.name`, `this._engineInfo`, `this.window`

## SearchOneOffs.observe()
- 位置: L390-409
- 役割: エンジンの変更でキャッシュを捨て、engine-icon-changed のときは該当ボタンの画像を更新する。
- 触るとき: エンジンのアイコン変更が one-off に反映されないとき、または通知を追加するとき。
- 条件付き依存: `if (aTopic != "browser-search-service" || aData == "engines-reloaded")` → `this.invalidateCache()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `engine.getIconURL().then()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `engine.getIconURL()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `this.getSelectableButtons(false) .find(b => b.engine?.id == engine.id) ?.setAttribute()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `this.getSelectableButtons(false) .find()`
- 条件付き依存: `if (aData === "engine-icon-changed")` → `this.getSelectableButtons()`
- 参照: `aSubject.wrappedJSObject`, `b.engine?.id`, `engine.id`

## SearchOneOffs._maxInlineAddEngines()
- 位置: L411-413
- 役割: 検索バーに並べる追加可能エンジンの上限を 3 として返す。
- 触るとき: インラインで出す追加エンジン数を変えるとき。

## SearchOneOffs._rebuild()
- 位置: async L418-432
- 役割: 再入を防ぎながら __rebuild を呼び、例外はログに出し、最後に rebuild イベントを発火する。
- 触るとき: one-off の再構築が失敗したときのログや rebuild 通知のタイミングを確かめるとき。
- 呼び出し先: `console.error()`, `this.__rebuild()`, `this.dispatchEvent()`
- 参照: `this._rebuilding`

## SearchOneOffs.__rebuild()
- 位置: async L437-505
- 役割: 一覧と幅が変わっていれば、エンジンのボタンと検索バー向け追加ボタンを作り直す。不要な時は早期に戻る。
- 触るとき: one-off の再構築条件や表示の隠し方を変えるとき。
- 呼び出し先: `lazy.OpenSearchManager.getInstallableEngines()`, `this._rebuildEngineList()`, `this.buttons.firstElementChild.remove()`, `this.buttons.setAttribute()`, `this.getEngineInfo()`, `this.hasAttribute()`, `this.header.querySelector()`, `this.willHide()`
- 条件付き依存: `if (this.popup && this._textbox)` → `this.window.promiseDocumentFlushed()`
- 参照: `(await this.getEngineInfo()).engines`, `addEngines.length`, `headerText.id`, `this._addEngines`, `this._engineInfo.domWasUpdated`, `this._engineInfo?.domWasUpdated`, `this._textbox`, `this._textbox.clientWidth`, `this._textboxWidth`, `this.buttons.firstElementChild`, `this.container.hidden`, `this.popup`, `this.settingsButton.id`, `this.telemetryOrigin`, `this.window.gBrowser.selectedBrowser`

## SearchOneOffs._rebuildEngineList()
- 位置: async L515-552
- 役割: エンジンごとにボタンを作って並べ、追加可能なエンジンは上限まで add-engine ボタンとして加える。
- 触るとき: one-off ボタンの属性や追加ボタンの見せ方を変えるとき。
- 呼び出し先: `Math.min()`, `button.classList.add()`, `button.setAttribute()`, `engine.getIconURL()`, `this._buttonIDForEngine()`, `this.buttons.appendChild()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`, `this.setTooltipForEngineButton()`
- 条件付き依存: `if (engine.icon)` → `button.setAttribute()`
- 参照: `addEngines.length`, `button.engine`, `button.id`, `engine.icon`, `engine.title`, `engine.uri`, `engines.length`, `this._maxInlineAddEngines`

## SearchOneOffs._buttonIDForEngine()
- 位置: L554-560
- 役割: エンジンの一覧内 index から、telemetryOrigin を含むボタン id を作る。
- 触るとき: ボタン id の形式を変えたり、id で要素を探す処理を書くとき。
- 呼び出し先: `this._engineInfo.engines.indexOf()`
- 参照: `this.telemetryOrigin`

## SearchOneOffs.getSelectableButtons()
- 位置: L562-572
- 役割: エンジンのボタン一覧を返し、指定時は設定ボタンも末尾に加える。
- 触るとき: キーボード移動の対象に含めるボタンを変えるとき。
- 呼び出し先: `this.buttons.querySelectorAll()`
- 条件付き依存: `if (aIncludeNonEngineButtons)` → `buttons.push()`
- 参照: `this.settingsButton`

## SearchOneOffs._whereToOpen()
- 位置: L586-617
- 役割: 強制タブ、openintab 設定と Alt、中クリックや Accel によって、現在のタブ・新規タブ・背景タブを決める。
- 触るとき: one-off で検索結果を開く場所を変えるとき、またはクリック修飾キーの挙動を直すとき。
- 条件付き依存: `if (aForceNewTab)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(aForceNewTab))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(aForceNewTab))` → `KeyboardEvent.isInstance()`
- 条件付き依存: `if (!(aForceNewTab))` → `MouseEvent.isInstance()`
- 条件付き依存: `if (!(aForceNewTab))` → `aEvent.getModifierState()`
- 参照: `aEvent.altKey`, `aEvent.button`, `this.window.gBrowser.selectedTab.isEmpty`
- XPCOM: `Services.prefs`

## SearchOneOffs.advanceSelection()
- 位置: L638-657
- 役割: 選択を前後に 1 つ動かし、wrap が無効なら端で -1 にして選択解除する。
- 触るとき: キーボードでの one-off の移動の仕方を変えるとき。
- 呼び出し先: `this.getSelectableButtons()`
- 条件付き依存: `if (this.selectedButton)` → `buttons.indexOf()`
- 参照: `buttons.length`, `this.selectedButton`

## SearchOneOffs.handleKeyDown()
- 位置: L688-703
- 役割: view が開いていればキー処理を _handleKeyDown に渡し、処理したら既定動作と伝播を止める。
- 触るとき: one-off が検索バーのキー操作を奪う条件を調べるとき。
- 呼び出し先: `this._handleKeyDown()`
- 条件付き依存: `if (handled)` → `event.preventDefault()`
- 条件付き依存: `if (handled)` → `event.stopPropagation()`
- 参照: `this.hasView`

## SearchOneOffs._handleKeyDown()
- 位置: L705-889
- 役割: Tab、上下、左右の各キーを、リスト内の選択と one-off ボタンの移動に振り分けて処理する。
- 触るとき: キーボード操作の仕様を変えるとき、特にリストと one-off の境界の動きを直すとき。
- 呼び出し先: `event.getModifierState()`, `this.selectedButton.classList.contains()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_TAB && !event.getModifierState("Alt") && !event.getModifierState("AltGraph") && !event.getModifierState("Control") && !even...)` → `this.getAttribute()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_TAB && !event.getModifierState("Alt") && !event.getModifierState("AltGraph") && !event.getModifierState("Control") && !even...)` → `this.getSelectableButtons()`
- 条件付き依存: `if ( event.keyCode == KeyEvent.DOM_VK_TAB && !event.getModifierState("Alt") && !event.getModifierState("AltGraph") && !event.getModifierState("Control") && !even...)` → `this.advanceSelection()`
- 条件付き依存: `if (event.altKey)` → `this.advanceSelection()`
- 条件付き依存: `if (numListItems == 0)` → `this.advanceSelection()`
- 条件付き依存: `if (this.selectedViewIndex == 0)` → `this.advanceSelection()`
- 条件付き依存: `if (!this.selectedButton)` → `this.advanceSelection()`
- 条件付き依存: `if (event.keyCode == KeyboardEvent.DOM_VK_UP)` → `this.advanceSelection()`
- 条件付き依存: `if (this.selectedButton)` → `this.getSelectableButtons()`
- 条件付き依存: `if (this.selectedButton)` → `this.advanceSelection()`
- 条件付き依存: `if ( this.selectedButton && this.selectedButton.engine && !this.disableOneOffsHorizontalKeyNavigation )` → `this.advanceSelection()`
- 参照: `KeyEvent.DOM_VK_RIGHT`, `KeyEvent.DOM_VK_TAB`, `KeyboardEvent.DOM_VK_DOWN`, `KeyboardEvent.DOM_VK_LEFT`, `KeyboardEvent.DOM_VK_RIGHT`, `KeyboardEvent.DOM_VK_UP`, `buttons.length`, `event.altKey`, `event.keyCode`, `event.shiftKey`, `this.container.hidden`, `this.disableOneOffsHorizontalKeyNavigation`, `this.getSelectableButtons(true).length`, `this.selectedButton`, `this.selectedButton.engine`, `this.selectedButton.open`, `this.selectedButtonIndex`, `this.selectedViewIndex`, `this.textbox`, `this.textbox.value`

## SearchOneOffs.eventTargetIsAOneOff()
- 位置: L899-925
- 役割: イベントの対象が one-off ボタン、または open-in-new-tab のメニュー項目かを判定する。
- 触るとき: one-off へのクリックやキーをテレメトリに記録すべきか判定するとき。
- 呼び出し先: `Element.isInstance()`, `KeyboardEvent.isInstance()`, `MouseEvent.isInstance()`, `target.classList.contains()`, `this.window.XULCommandEvent.isInstance()`
- 参照: `event.originalTarget`, `this.selectedButton`

## SearchOneOffs.hasView()
- 位置: L932-934
- 役割: one-off が popup に紐づいているかを返す。
- 触るとき: popup が無い状態でキー処理や操作が走らないか確かめるとき。
- 参照: `this.popup`

## SearchOneOffs.isViewOpen()
- 位置: L939-942
- 役割: 紐づく popup が開いているかを返す。
- 触るとき: popup の開閉状態で one-off の挙動を分けるとき。
- 参照: `this.popup`, `this.popup.popupOpen`

## SearchOneOffs.selectedViewIndex()
- 位置: L947-950
- 役割: popup 内の候補の選択 index を返す。
- 触るとき: 候補リストと one-off の選択を合わせるとき。
- 参照: `this.popup.selectedIndex`

## SearchOneOffs.selectedViewIndex()
- 位置: L958-961
- 役割: popup 内の候補の選択 index を設定する。
- 触るとき: one-off 側から候補リストの選択を移すとき。
- 参照: `this.popup.selectedIndex`

## SearchOneOffs.closeView()
- 位置: L966-968
- 役割: popup を閉じる。
- 触るとき: 設定ボタンを押した後などに one-off のポップアップを閉じるとき。
- 呼び出し先: `this.popup.hidePopup()`

## SearchOneOffs.handleSearchCommand()
- 位置: L981-985
- 役割: 開き先を決めて、popup の handleOneOffSearch に検索を渡す。
- 触るとき: one-off からの検索の実行経路を変えるとき。
- 呼び出し先: `this._whereToOpen()`, `this.popup.handleOneOffSearch()`

## SearchOneOffs.setTooltipForEngineButton()
- 位置: L994-996
- 役割: エンジンボタンの tooltiptext にエンジン名を入れる。
- 触るとき: one-off のツールチップの中身を変えるとき。
- 呼び出し先: `button.setAttribute()`
- 参照: `button.engine.name`

## SearchOneOffs._on_mousedown()
- 位置: L1000-1005
- 役割: mousedown の既定動作を止めて、入力欄がフォーカスを失って popup が閉じるのを防ぐ。
- 触るとき: one-off を押したときに入力欄のフォーカスや popup が閉じてしまうとき。
- 呼び出し先: `event.preventDefault()`

## SearchOneOffs._on_click()
- 位置: L1007-1030
- 役割: 右クリックとエンジン無しを除き、入力が空なら Shift で検索フォームを開き、入力があれば選択して検索を実行する。
- 触るとき: one-off のクリックで検索を開始する条件や Shift クリックの扱いを変えるとき。
- 呼び出し先: `this.handleSearchCommand()`
- 条件付き依存: `if (event.shiftKey)` → `this.popup.openSearchForm()`
- 参照: `button.engine`, `event.button`, `event.originalTarget`, `event.shiftKey`, `this.selectedButton`, `this.textbox.value`

## SearchOneOffs._on_command()
- 位置: async L1032-1118
- 役割: 設定ボタンで設定画面を開き、追加ボタンでエンジンを追加し、コンテキストメニューで新規タブ検索や既定エンジンの変更を行う。
- 触るとき: one-off のメニューや追加ボタンの動作を変えるとき、既定エンジンの変更経路を調べるとき。
- 呼び出し先: `target.classList.contains()`
- 条件付き依存: `if (target == this.settingsButton)` → `this.window.openPreferences()`
- 条件付き依存: `if (target == this.settingsButton)` → `this.closeView()`
- 条件付き依存: `if (target.classList.contains("searchbar-engine-one-off-add-engine"))` → `lazy.SearchUIUtils.addOpenSearchEngine()`
- 条件付き依存: `if (target.classList.contains("searchbar-engine-one-off-add-engine"))` → `target.getAttribute()`
- 条件付き依存: `if (result)` → `this._rebuild()`
- 条件付き依存: `if (target.classList.contains("search-one-offs-context-open-in-new-tab"))` → `target.closest()`
- 条件付き依存: `if (this.textbox.value)` → `this.handleSearchCommand()`
- 条件付き依存: `if (!(this.textbox.value))` → `this.popup.openSearchForm()`
- 条件付き依存: `if ( target.classList.contains("search-one-offs-context-set-default") || isPrivateButton )` → `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( target.classList.contains("search-one-offs-context-set-default") || isPrivateButton )` → `target.closest()`
- 条件付き依存: `if ( target.classList.contains("search-one-offs-context-set-default") || isPrivateButton )` → `this.getAttribute()`
- 条件付き依存: `if ( !this.getAttribute("includecurrentengine") && isPrivateButton == isPrivateWin )` → `currentEngine.getIconURL()`
- 条件付き依存: `if ( !this.getAttribute("includecurrentengine") && isPrivateButton == isPrivateWin )` → `button.setAttribute()`
- 条件付き依存: `if (isPrivateButton)` → `lazy.SearchService.setDefaultPrivate()`
- 条件付き依存: `if (!(isPrivateButton))` → `lazy.SearchService.setDefault()`
- 参照: `button.engine`, `console.error`, `currentEngine.name`, `event.target`, `lazy.SearchService`, `lazy.SearchService.CHANGE_REASON.USER_SEARCHBAR_CONTEXT`, `target.closest("menupopup")._triggerButton`, `this.selectedButton`, `this.selectedButton.engine`, `this.settingsButton`, `this.textbox.value`, `this.window`, `this.window.gBrowser.selectedBrowser.browsingContext`

## SearchOneOffs._on_contextmenu()
- 位置: L1120-1165
- 役割: one-off のボタン以外では右クリックメニューを出さず、出すときは既定設定の項目の有効・無効と表示を決める。
- 触るとき: 右クリックメニューに出す項目や、プライベート既定の項目を出す条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `event.preventDefault()`, `target.classList.contains()`, `this.contextMenuPopup .querySelector()`, `this.contextMenuPopup .querySelector(".search-one-offs-context-set-default") .setAttribute()`, `this.contextMenuPopup.openPopupAtScreen()`, `this.contextMenuPopup.querySelector()`
- 条件付き依存: `if ( !target.classList.contains("searchbar-engine-one-off-item") || target.classList.contains("search-setting-button") )` → `event.preventDefault()`
- 条件付き依存: `if ( Services.prefs.getBoolPref( "browser.search.separatePrivateDefault.featureGate", false ) && Services.prefs.getBoolPref( "browser.search.separatePrivateDefau...)` → `privateDefaultItem.setAttribute()`
- 参照: `event.originalTarget`, `event.screenX`, `event.screenY`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `privateDefaultItem.hidden`, `target.engine`, `this.contextMenuPopup._triggerButton`
- XPCOM: `Services.prefs`

## SearchOneOffs._on_input()
- 位置: L1167-1173
- 役割: 入力欄の値(oneOffSearchQuery があればそれ)を query に反映する。
- 触るとき: オートフィルや特殊な URL で one-off の検索語が入力と食い違うとき。
- 参照: `event.target.oneOffSearchQuery`, `event.target.value`, `this.query`

## SearchOneOffs._on_popupshowing()
- 位置: L1175-1177
- 役割: popup が開くときに one-off を再構築する。
- 触るとき: popup 表示時の再構築のタイミングを変えるとき。
- 呼び出し先: `this._rebuild()`

## SearchOneOffs._on_popuphidden()
- 位置: L1179-1181
- 役割: popup が閉じたときに選択中のボタンを解除する。
- 触るとき: popup を閉じた後に選択が残ってしまうとき。
- 参照: `this.selectedButton`
