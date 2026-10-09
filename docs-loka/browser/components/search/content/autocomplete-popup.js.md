# browser/components/search/content/autocomplete-popup.js

source: browser/components/search/content/autocomplete-popup.js
source-hash: 3ebd43a3fe78c28467fa69ba1bb10e2a20e7aba6
lines: 344

## <module>
- 役割: 検索バーの自動補完ポップアップ search-autocomplete-richlistbox-popup を定義するファイル。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## MozSearchAutocompleteRichlistboxPopup.constructor()
- 位置: L29-90
- 役割: popupshowing で設定だけの表示か候補表示かを切り替え、popuphiding で one-off 監視を外す。候補クリックも処理する。
- 触るとき: ポップアップを開いたときのヘッダーや候補リストの表示を変えるとき、または検索バーの glass アイコンからの表示切り替えを直すとき。
- 呼び出し先: `super()`, `this._oneOffButtons.addEventListener()`, `this._oneOffButtons.removeEventListener()`, `this.addEventListener()`, `this.searchbar.hasAttribute()`, `this.updateHeader()`, `this.updateHeader().catch()`
- 条件付き依存: `if (this.searchbar.hasAttribute("showonlysettings"))` → `this.searchbar.removeAttribute()`
- 条件付き依存: `if (this.searchbar.hasAttribute("showonlysettings"))` → `this.setAttribute()`
- 条件付き依存: `if (!(this.searchbar.hasAttribute("showonlysettings")))` → `this.removeAttribute()`
- 条件付き依存: `if (this.searchbar.value)` → `this.oneOffButtons.handleSearchCommand()`
- 条件付き依存: `if (event.shiftKey)` → `this.openSearchForm()`
- 参照: `button.parentNode.engine`, `console.error`, `event.button`, `event.originalTarget`, `event.shiftKey`, `this._bundle`, `this.matchCount`, `this.richlistbox.collapsed`, `this.searchbar.value`

## MozSearchAutocompleteRichlistboxPopup.inheritedAttributes()
- 位置: L92-97
- 役割: ヘッダーの showonlysettings を .search-panel-current-engine に、src を .searchbar-engine-image に継承させる対応表を返す。
- 触るとき: ポップアップ内の要素へ属性を引き継がせる対象を増やすとき、または継承先のセレクタを変えるとき。

## MozSearchAutocompleteRichlistboxPopup.getElementForAttrInheritance()
- 位置: L101-103
- 役割: 属性継承の対象を shadow root ではなく light DOM の querySelector で探す。
- 触るとき: 継承させたい子要素がポップアップの light DOM に無い、と属性が届かないとき。
- 呼び出し先: `this.querySelector()`

## MozSearchAutocompleteRichlistboxPopup.initialize()
- 位置: L105-116
- 役割: 基底の初期化の後、ポップアップの子要素(ヘッダー、one-off コンテナ)と SearchOneOffs と searchbar の参照を用意する。
- 触るとき: markup の子要素のクラス名を変えたとき、または遅延初期化の参照がずれていないか確かめるとき。
- 呼び出し先: `document.getElementById()`, `super.initialize()`, `this.initializeAttributeInheritance()`, `this.querySelector()`
- 参照: `lazy.SearchOneOffs`, `this._oneOffButtons`, `this._searchOneOffsContainer`, `this._searchbar`, `this._searchbarEngine`, `this._searchbarEngineName`

## MozSearchAutocompleteRichlistboxPopup.oneOffButtons()
- 位置: L118-123
- 役割: SearchOneOffs が未生成なら initialize を呼んでから返す。
- 触るとき: ポップアップの外から one-off ボタン群を操作するコードを足すとき。
- 条件付き依存: `if (!this._oneOffButtons)` → `this.initialize()`
- 参照: `this._oneOffButtons`

## MozSearchAutocompleteRichlistboxPopup.markup()
- 位置: L125-136
- 役割: ポップアップの XUL 子要素(エンジンヘッダー、候補リスト、one-off コンテナ)の文字列を返す。
- 触るとき: ポップアップの構成要素を追加・削除したり、initialize や inheritedAttributes が参照するクラス名を変えるとき。

## MozSearchAutocompleteRichlistboxPopup.searchOneOffsContainer()
- 位置: L138-143
- 役割: one-off コンテナ要素を返す遅延 getter。未初期化なら initialize を呼ぶ。
- 触るとき: one-off コンテナを直接参照する処理を書くとき。
- 条件付き依存: `if (!this._searchOneOffsContainer)` → `this.initialize()`
- 参照: `this._searchOneOffsContainer`

## MozSearchAutocompleteRichlistboxPopup.searchbarEngine()
- 位置: L145-150
- 役割: エンジンヘッダー要素 .search-panel-header を返す遅延 getter。
- 触るとき: updateHeader が設定するヘッダーのエンジン情報を他から読むとき。
- 条件付き依存: `if (!this._searchbarEngine)` → `this.initialize()`
- 参照: `this._searchbarEngine`

## MozSearchAutocompleteRichlistboxPopup.searchbarEngineName()
- 位置: L152-157
- 役割: ヘッダーのエンジン名ラベル .searchbar-engine-name を返す遅延 getter。
- 触るとき: ヘッダーの表示文言を別の場所から書き換えるとき。
- 条件付き依存: `if (!this._searchbarEngineName)` → `this.initialize()`
- 参照: `this._searchbarEngineName`

## MozSearchAutocompleteRichlistboxPopup.searchbar()
- 位置: L159-164
- 役割: document の searchbar 要素を返す遅延 getter。
- 触るとき: 検索の実行や検索フォームを開く処理で searchbar の API を呼ぶとき。
- 条件付き依存: `if (!this._searchbar)` → `this.initialize()`
- 参照: `this._searchbar`

## MozSearchAutocompleteRichlistboxPopup.bundle()
- 位置: L166-172
- 役割: chrome://browser/locale/search.properties の文字列バンドルを初回だけ作って返す。
- 触るとき: ヘッダーの文言の翻訳キー(searchHeader など)を追加・変更するとき。
- 条件付き依存: `if (!this._bundle)` → `Services.strings.createBundle()`
- 参照: `this._bundle`
- XPCOM: `Services.strings`

## MozSearchAutocompleteRichlistboxPopup.openAutocompletePopup()
- 位置: L174-181
- 役割: 非表示の panel を表示状態にしてから基底の _openAutocompletePopup を呼ぶ。
- 触るとき: 起動や新規ウィンドウ時の表示タイミングを変えて、パフォーマンスへの影響を確かめるとき。
- 呼び出し先: `this._openAutocompletePopup()`
- 参照: `aInput.popup.hidden`

## MozSearchAutocompleteRichlistboxPopup.onPopupClick()
- 位置: L183-240
- 役割: 左クリックは基底の handleEnter に任せ、それ以外は開き先(現在のタブ、新規タブ、背景タブ)を決めて searchbar.doSearch を呼ぶ。
- 触るとき: 候補の中クリックや修飾キー付きクリックで開く場所の判定を変えるとき、または候補クリック時のテレメトリを直すとき。
- 呼び出し先: `MouseEvent.isInstance()`, `lazy.BrowserSearchTelemetry.recordSearchSuggestionSelectionMethod()`, `lazy.BrowserUtils.whereToOpenLink()`, `this.input.controller.getValueAt()`, `this.searchbar.doSearch()`
- 条件付き依存: `if ( aEvent.button == 0 && !aEvent.shiftKey && !aEvent.ctrlKey && !aEvent.altKey && !aEvent.metaKey )` → `this.input.controller.handleEnter()`
- 条件付き依存: `if (!(where == "tab" && params.inBackground))` → `this.closePopup()`
- 条件付き依存: `if (!(where == "tab" && params.inBackground))` → `this.input.controller.handleEscape()`
- 条件付き依存: `if (where == "tab" && params.inBackground)` → `this.searchbar.focus()`
- 参照: `AppConstants.platform`, `aEvent.altKey`, `aEvent.button`, `aEvent.ctrlKey`, `aEvent.metaKey`, `aEvent.shiftKey`, `params.inBackground`, `this.searchbar.telemetrySelectedIndex`, `this.searchbar.value`, `this.selectedIndex`

## MozSearchAutocompleteRichlistboxPopup.updateHeader()
- 位置: async L254-287
- 役割: 指定エンジン(無ければ通常かプライベートの既定エンジン)のアイコンと名前でヘッダーを更新する。待機中に名前が変わったら適用せず戻る。
- 触るとき: 既定の検索エンジンを変えたときや、one-off で選んだエンジンをヘッダーに出すときに表示がずれないか確かめるとき。
- 呼び出し先: `engine.getIconURL()`, `this.bundle.formatStringFromName()`, `this.searchbarEngineName.setAttribute()`
- 条件付き依存: `if (!engine)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `lazy.SearchService.getDefaultPrivate()`
- 条件付き依存: `if (!(PrivateBrowsingUtils.isWindowPrivate(window)))` → `lazy.SearchService.getDefault()`
- 条件付き依存: `if (uri)` → `this.setAttribute()`
- 条件付き依存: `if (!(uri))` → `this.removeAttribute()`
- 参照: `engine.name`, `this.#currentEngineName`, `this.searchbarEngine.engine`

## MozSearchAutocompleteRichlistboxPopup.handleOneOffSearch()
- 位置: L302-304
- 役割: one-off のクリックや「新しいタブで検索」を searchbar.handleSearchCommandWhere に渡す。
- 触るとき: one-off からの検索の開き先や params を変えるとき。
- 呼び出し先: `this.searchbar.handleSearchCommandWhere()`

## MozSearchAutocompleteRichlistboxPopup.openSearchForm()
- 位置: L306-312
- 役割: _whereToOpen で開き先を決め、searchbar.openSearchFormWhere で検索エンジンのフォームを開く。
- 触るとき: Shift クリックや右クリックメニューから検索フォームを開く経路を調べるとき。
- 呼び出し先: `this.oneOffButtons._whereToOpen()`, `this.searchbar.openSearchFormWhere()`

## MozSearchAutocompleteRichlistboxPopup.handleEvent()
- 位置: L320-327
- 役割: DOM イベントを _on_<イベント種別> メソッドへ振り分け、無ければ例外を投げる。
- 触るとき: 新しいイベントを購読させるとき、対応する _on_ メソッドを足し忘れていないか確かめるとき。
- 条件付き依存: `if (methodName in this)` → `this[methodName]()`
- 参照: `event.type`

## MozSearchAutocompleteRichlistboxPopup._on_SelectedOneOffButtonChanged()
- 位置: L328-333
- 役割: 選択中の one-off ボタンのエンジンで updateHeader を呼び、ヘッダーを合わせる。
- 触るとき: one-off の選択移動に伴ってヘッダーが古いエンジンのままになるとき。
- 呼び出し先: `this.updateHeader()`, `this.updateHeader(engine).catch()`
- 参照: `console.error`, `this.oneOffButtons.selectedButton`, `this.oneOffButtons.selectedButton.engine`
