# browser/components/urlbar/UrlbarSearchOneOffs.sys.mjs

source: browser/components/urlbar/UrlbarSearchOneOffs.sys.mjs
source-hash: 14414b803359093024f200d3dde57f89f3a81002
lines: 404

## <module>
- 役割: urlbar の下に並ぶ検索エンジンとローカル検索モード(ブックマーク、履歴、タブ、アクション)のワンオフボタンの振る舞いを定義する UrlbarSearchOneOffs を定義する。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## UrlbarSearchOneOffs.constructor()
- 位置: L29-36
- 役割: 親ビューの入力欄から一覧の要素を取り、設定の監視を登録し、横方向のキー移動を無効にする。
- 触るとき: ワンオフボタンの初期化や、urlbar 専用の設定を増やすとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.addObserver()`, `super()`, `view.input.querySelector()`
- 参照: `this.disableOneOffsHorizontalKeyNavigation`, `this.input`, `this.view`, `view.input`

## UrlbarSearchOneOffs.localButtons()
- 位置: L44-46
- 役割: 選択可能なボタンのうち、ローカル検索モードの source を持つものだけを返す。
- 触るとき: ブックマーク、履歴などのローカルボタンの一覧を使う箇所を変えるとき見る。
- 呼び出し先: `this.getSelectableButtons()`, `this.getSelectableButtons(false).filter()`
- 参照: `b.source`

## UrlbarSearchOneOffs.updateWebEngines()
- 位置: L51-56
- 役割: ウェブ提供の検索エンジン一覧が変わったとき、キャッシュを無効にし、ビューが開いていれば作り直す。
- 触るとき: 検索エンジンの追加や削除がボタンに反映されない問題を調べるとき見る。
- 呼び出し先: `this.invalidateCache()`
- 条件付き依存: `if (this.view.isOpen)` → `this._rebuild()`
- 参照: `this.view.isOpen`

## UrlbarSearchOneOffs.enable()
- 位置: L64-82
- 役割: scotchBonnet.disableOneOffs が有効なら無効扱いにし、有効化時はテレメトリの発生元を urlbar にしてビューの監視を登録、無効化時は表示を隠して監視を外す。
- 触るとき: ワンオフボタンの表示の切り替えや、無効化の条件を変えるとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (this.view.isOpen)` → `this._rebuild()`
- 条件付き依存: `if (enable)` → `this.view.controller.addListener()`
- 条件付き依存: `if (!(enable))` → `this.view.controller.removeListener()`
- 参照: `this.style.display`, `this.telemetryOrigin`, `this.textbox`, `this.view.input.inputField`, `this.view.isOpen`

## UrlbarSearchOneOffs.onViewOpen()
- 位置: L87-89
- 役割: ビューが開いたときに、基底クラスの popupshowing の処理へ委譲する。
- 触るとき: ビューを開いたときにボタンを準備する処理を変えたいとき見る。
- 呼び出し先: `this._on_popupshowing()`

## UrlbarSearchOneOffs.onViewClose()
- 位置: L94-96
- 役割: ビューが閉じたときに、基底クラスの popuphidden の処理へ委譲する。
- 触るとき: ビューを閉じたときの後始末を変えたいとき見る。
- 呼び出し先: `this._on_popuphidden()`

## UrlbarSearchOneOffs.hasView()
- 位置: L102-107
- 役割: ワンオフが無効化されておらず、コンテナーが隠れていなければ true を返す。
- 触るとき: ワンオフが表示されていない理由を調べるとき見る。
- 参照: `this.container.hidden`, `this.style.display`

## UrlbarSearchOneOffs.isViewOpen()
- 位置: L113-115
- 役割: 親ビューが開いているかを返す。
- 触るとき: ビューの開閉状態を参照する箇所の判定を確かめるとき見る。
- 参照: `this.view.isOpen`

## UrlbarSearchOneOffs.selectedButton()
- 位置: L123-143
- 役割: 選択ボタンを設定し、設定ボタン以外ならそのエンジンと種別で検索モードに入る。設定ボタンを選んだときや検索モードでないときは、前の検索モードを戻す。
- 触るとき: 選択中のボタンを切り替えたときに検索モードが入る、または戻る条件を変えるとき見る。
- 条件付き依存: `if (this.input.searchMode)` → `this.input.restoreSearchModeState()`
- 参照: `button.engine?.name`, `button.source`, `super.selectedButton`, `this.input.searchMode`, `this.selectedButton`, `this.view.oneOffSearchButtons.settingsButton`

## UrlbarSearchOneOffs.selectedButton()
- 位置: L145-147
- 役割: 基底クラスで保持している選択ボタンをそのまま返す。
- 触るとき: 選択ボタンの参照を取る箇所を調べるとき見る。
- 参照: `super.selectedButton`

## UrlbarSearchOneOffs.selectedViewIndex()
- 位置: L154-156
- 役割: 親ビューで選ばれている行の番号を返す。
- 触るとき: ワンオフ選択と一覧の行選択の対応を調べるとき見る。
- 参照: `this.view.selectedRowIndex`

## UrlbarSearchOneOffs.selectedViewIndex()
- 位置: L157-159
- 役割: 親ビューの選択行を、与えられた番号に設定する。
- 触るとき: ワンオフからビューの行選択を動かす箇所を変えるとき見る。
- 参照: `this.view.selectedRowIndex`

## UrlbarSearchOneOffs.closeView()
- 位置: L164-168
- 役割: 親ビューがあれば閉じる。
- 触るとき: ボタン操作の後にビューを閉じる箇所を調べるとき見る。
- 条件付き依存: `if (this.view)` → `this.view.close()`
- 参照: `this.view`

## UrlbarSearchOneOffs.handleSearchCommand()
- 位置: L179-261
- 役割: 設定ボタンや engine 追加は即座に実行する。それ以外は、入力と修飾キー(Shift や新しいタブ)の組合せで検索を即実行するか、現在のタブ、新しいタブ、既定の別の動きで検索モードに入る。
- 触るとき: ワンオフボタンを押したときの遷移先(同じタブ、新しいタブ、バックグラウンド)や、自動補完を許すかどうかを変えるとき見る。
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `this._whereToOpen()`, `this.input.getAttribute()`, `this.input.select()`, `this.input.setSearchMode()`, `this.input.startQuery()`, `this.input.window.gBrowser.addTrustedTab()`, `this.selectedButton.classList.contains()`
- 条件付き依存: `if ( this.selectedButton == this.view.oneOffSearchButtons.settingsButton || this.selectedButton.classList.contains( "searchbar-engine-one-off-add-engine" ) )` → `this.input.controller.engagementEvent.discard()`
- 条件付き依存: `if ( this.selectedButton == this.view.oneOffSearchButtons.settingsButton || this.selectedButton.classList.contains( "searchbar-engine-one-off-add-engine" ) )` → `this.selectedButton.doCommand()`
- 条件付き依存: `if ( userTypedSearchString && engine && (event.shiftKey || where != "current") )` → `this.input.handleNavigation()`
- 条件付き依存: `if (!params?.inBackground)` → `newTab.documentGlobal.gURLBar.startQuery()`
- 参照: `event.shiftKey`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `newTab.linkedBrowser`, `newTab.linkedBrowser.userTypedValue`, `params?.inBackground`, `searchMode.engineName`, `searchMode.isPreview`, `searchMode.source`, `this.input.searchMode`, `this.input.value`, `this.input.window.gBrowser.selectedTab`, `this.selectedButton`, `this.selectedButton.engine`, `this.view.oneOffSearchButtons.settingsButton`

## UrlbarSearchOneOffs.setTooltipForEngineButton()
- 位置: L270-284
- 役割: エンジンに別名があれば、その別名を含む説明を、無ければ基底の説明を設定する。
- 触るとき: ボタンのツールチップの文言を変えるとき見る。
- 呼び出し先: `this.document.l10n.setAttributes()`
- 条件付き依存: `if (!aliases.length)` → `super.setTooltipForEngineButton()`
- 参照: `aliases.length`, `button.engine.aliases`, `button.engine.name`

## UrlbarSearchOneOffs.willHide()
- 位置: async L293-308
- 役割: 基底の判定を行い、ワンオフを無効化する設定があれば隠す。ローカル検索モードのいずれかが有効なら隠さない。
- 触るとき: ワンオフを隠す条件(設定、ローカルボタンの有無)を変えるとき見る。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.some()`, `super.willHide()`
- 参照: `m.pref`

## UrlbarSearchOneOffs.onPrefChanged()
- 位置: L317-329
- 役割: ローカル検索モードの設定や、scotchBonnet の上書き、無効化の設定が変わったら、キャッシュを無効にする。
- 触るとき: 設定を切り替えたのにボタンが更新されない問題を調べるとき、監視対象の設定を確かめる。
- 呼び出し先: `lazy.UrlbarShared.LOCAL_SEARCH_MODES.map()`
- 条件付き依存: `if ( [ ...lazy.UrlbarShared.LOCAL_SEARCH_MODES.map(m => m.pref), "scotchBonnet.enableOverride", "scotchBonnet.disableOneOffs", ].includes(changedPref) )` → `this.invalidateCache()`
- 参照: `m.pref`

## UrlbarSearchOneOffs._rebuildEngineList()
- 位置: async L339-364
- 役割: 基底の一覧を作った後に、有効なローカル検索モードごとに、その名前の ID を持つボタンを末尾へ追加する。
- 触るとき: ローカル検索モードのボタンを増やすとき、または表示順や ID を変えるとき見る。
- 呼び出し先: `button.setAttribute()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.getResultSourceName()`, `super._rebuildEngineList()`, `this.buttons.appendChild()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`
- 参照: `button.id`, `button.source`, `lazy.UrlbarShared .LOCAL_SEARCH_MODES`

## UrlbarSearchOneOffs._on_click()
- 位置: L373-391
- 役割: 右クリックは無視し、エンジンかローカルのボタンなら選択してから handleSearchCommand を呼ぶ。
- 触るとき: クリック時の遷移やボタンの対象を変えるとき見る。
- 呼び出し先: `this.handleSearchCommand()`
- 参照: `button.engine`, `button.engine?.name`, `button.source`, `event.button`, `event.originalTarget`, `this.selectedButton`

## UrlbarSearchOneOffs._on_contextmenu()
- 位置: L399-402
- 役割: 右クリックのメニューを表示させないよう、既定の動作を止める。
- 触るとき: ワンオフ上の右クリックメニューの扱いを変えたいとき見る。
- 呼び出し先: `event.preventDefault()`
