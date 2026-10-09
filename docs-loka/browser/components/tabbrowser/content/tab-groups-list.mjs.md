# browser/components/tabbrowser/content/tab-groups-list.mjs

source: browser/components/tabbrowser/content/tab-groups-list.mjs
source-hash: e8d39a7bd6c82bf3f90b53d44b2892bb262721e1
lines: 197

## <module>
- 役割: 開いている/保存済みタブグループを一覧表示する tab-groups-list カスタム要素(Lit)を定義する。
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`, `customElements.define()`

## TabGroupsList.constructor()
- 位置: L32-38
- 役割: 行の role、開いている/保存済みグループ、既定名の初期値を空にする。
- 触るとき: 要素のプロパティの初期値を変えるとき。
- 呼び出し先: `super()`

## TabGroupsList.createRenderRoot()
- 位置: L40-42
- 役割: shadow DOM を使わず要素自身を描画先にする。
- 触るとき: 一覧にページ側の CSS が効く理由を調べるとき。

## TabGroupsList.#win()
- 位置: L44-46
- 役割: この要素が属するウィンドウ(documentGlobal)を返す。
- 触るとき: ウィンドウ参照の取得方法を確認するとき。

## TabGroupsList.connectedCallback()
- 位置: L48-51
- 役割: DOM 接続時に一覧データを読み込む。
- 触るとき: 一覧が更新されるタイミングを調べるとき。
- 呼び出し先: `super.connectedCallback()`, `this.#populate()`

## TabGroupsList.firstUpdated()
- 位置: async L53-57
- 役割: 初回描画後に名前なしグループ用の既定名を l10n から取得する。
- 触るとき: 名前のないグループの表示名を調べるとき。
- 呼び出し先: `this.ownerDocument.l10n.formatValues()`

## TabGroupsList.#populate()
- 位置: L59-69
- 役割: 開いているグループを最終アクティブ順に、保存済みを閉じた日時の新しい順に取得する(プライベートウィンドウでは保存済みなし)。
- 触るとき: 一覧に出るグループや並び順を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `win.SessionStore.savedGroups.toSorted()`, `win.gBrowser.getAllTabGroups()`

## TabGroupsList.#handleGroupClick()
- 位置: L71-81
- 役割: パネルを閉じ、開いているグループは選択して前面に出し、保存済みは復元して開く。
- 触るとき: グループ行クリック時の動作を変えるとき。
- 呼び出し先: `(this.closest("panel"))?.hidePopup()`, `this.closest()`
- 条件付き依存: `if (isOpen)` → `group.select()`
- 条件付き依存: `if (isOpen)` → `group.documentGlobal.focus()`
- 条件付き依存: `if (!(isOpen))` → `this.#win.SessionStore.openSavedTabGroup()`

## TabGroupsList.#handleContextMenu()
- 位置: L83-92
- 役割: 右クリック時に、開いている/保存済みに応じたコンテキストメニューをクリック位置に表示する。
- 触るとき: グループ行の右クリックメニューを調べるとき。
- 呼び出し先: `event.preventDefault()`, `popup.openPopupAtScreen()`, `this.ownerDocument.getElementById()`

## TabGroupsList.#groupRow()
- 位置: L94-130
- 役割: グループ一つ分のボタン行(色、アイコン、名前、イベント)を描画するテンプレートを返す。
- 触るとき: グループ行の見た目や属性を変えるとき。
- 呼び出し先: `JSON.stringify()`, `classMap()`, `html()`, `styleMap()`, `this.#handleContextMenu()`, `this.#handleGroupClick()`

## TabGroupsList.#emptyState()
- 位置: L132-157
- 役割: グループが無いときの案内表示(画像、文言、作成ボタン)のテンプレートを返す。
- 触るとき: 空状態の表示を変えるとき。
- 呼び出し先: `html()`

## TabGroupsList.#handleCreateTabGroup()
- 位置: L159-168
- 役割: パネルを閉じ、新規タブを作ってそれを含む新しいタブグループを作成する。
- 触るとき: 一覧からのグループ新規作成の挙動を変えるとき。
- 呼び出し先: `(this.closest("panel"))?.hidePopup()`, `this.closest()`, `win.gBrowser.TabMetrics.userTriggeredContext()`, `win.gBrowser.addTabGroup()`, `win.gBrowser.addTrustedTab()`

## TabGroupsList.render()
- 位置: L170-193
- 役割: グループが無ければ空状態、あれば作成ボタンと開いている/保存済みの行を描画する。
- 触るとき: 一覧全体の構成を変えるとき。
- 呼び出し先: `html()`, `repeat()`, `this.#groupRow()`
- 条件付き依存: `if (!this._openGroups.length && !this._savedGroups.length)` → `this.#emptyState()`
