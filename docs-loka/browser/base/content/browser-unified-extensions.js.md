# browser/base/content/browser-unified-extensions.js

source: browser/base/content/browser-unified-extensions.js
source-hash: 49d61666662d989c1f3fcdeb1a6c4dfeacd0a737
lines: 209

## <module>
- 役割: ツールバーの拡張機能ボタン一覧で各拡張を表す unified-extensions-item カスタム要素を定義し、OriginControls を読み込む。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## setExtension()
- 位置: L31-33
- 役割: 表示対象の Extension を保持する。描画は connectedCallback 後の render() で行われる。
- 触るとき: 一覧項目に別の拡張を渡す経路を変えるとき、項目が古い拡張を表示し続ける不具合を調べるとき。
- 参照: `this.extension`

## connectedCallback()
- 位置: L35-70
- 役割: テンプレートを複製して子要素を組み立て、ボタンとメッセージ欄への参照を取り、イベントを登録してから render() を呼ぶ。二重初期化は _menuButton の有無で防ぐ。
- 触るとき: 項目の DOM 構造を変えるとき、項目がページに挿入されたときの初期化順や、イベント登録漏れを調べるとき。
- 呼び出し先: `document.getElementById()`, `template.content.cloneNode()`, `this._actionButton.addEventListener()`, `this._menuButton.addEventListener()`, `this.addEventListener()`, `this.appendChild()`, `this.querySelector()`, `this.render()`
- 参照: `this._actionButton`, `this._menuButton`, `this._messageBarWrapper`, `this._messageBarWrapper.extensionId`, `this._messageDeck`, `this.extension?.id`

## handleEvent()
- 位置: L72-118
- 役割: command では menu ボタンならコンテキストメニューを開き、action ボタンなら選択中タブに activeTab 権限を付けてスクリプトを有効化する。blur と mouseout は既定のメッセージ、focus と mouseover はボタンごとのメッセージに切り替える。
- 触るとき: 拡張のボタンを押したときの動作を変えるとき、ホバーやフォーカスで表示するメッセージが切り替わらないときに確認する。
- 条件付き依存: `if (target === this._menuButton)` → `target.ownerDocument.getElementById()`
- 条件付き依存: `if (target === this._menuButton)` → `popup.openPopup()`
- 条件付き依存: `if (target === this._actionButton)` → `this.extension.tabManager.addActiveTabPermission()`
- 条件付き依存: `if (target === this._actionButton)` → `this.extension.tabManager.activateScripts()`
- 参照: `event.target.documentGlobal`, `event.type`, `gUnifiedExtensions.MESSAGE_DECK_INDEX_DEFAULT`, `gUnifiedExtensions.MESSAGE_DECK_INDEX_HOVER`, `gUnifiedExtensions.MESSAGE_DECK_INDEX_MENU_HOVER`, `target.firstElementChild`, `this._actionButton`, `this._menuButton`, `this._messageDeck.selectedIndex`, `win.gBrowser.selectedTab`

## #setStateMessage()
- 位置: L120-145
- 役割: OriginControls の状態からメッセージ ID を取り、通常時とホバー時の二種類の文言を l10n で設定する。
- 触るとき: 拡張のサイト権限状態メッセージの文言や切り替え条件を変えるとき、メッセージが空のままになる原因を調べるとき。
- 呼び出し先: `OriginControls.getStateMessageIDs()`, `this.ownerDocument.l10n.setAttributes()`, `this.querySelector()`
- 参照: `messages.default`, `messages.onHover`, `this.documentGlobal.gBrowser.selectedTab`, `this.extension.policy`

## #hasAction()
- 位置: L147-154
- 役割: 現在のタブで拡張の状態が whenClicked を持ち、かつアクセス権がないときに true を返す。アクションボタンの有効・無効に使う。
- 触るとき: アクションボタンが押せない条件を変えるとき、権限付与後もボタンが無効のままになる不具合を調べるとき。
- 呼び出し先: `OriginControls.getState()`
- 参照: `state.hasAccess`, `state.whenClicked`, `this.documentGlobal.gBrowser.selectedTab`, `this.extension.policy`

## render()
- 位置: L156-206
- 役割: 拡張の ID、名前、アイコン、注意状態、アクションボタンの有効状態、メニューボタンのラベル、メッセージを反映する。extension が未設定なら例外を投げる。
- 触るとき: 一覧項目に表示される情報を増やすとき、タブ切り替え後も表示が更新されない不具合を追うとき。
- 呼び出し先: `AddonManager.getAddonByID()`, `AddonManager.getAddonByID(this.extension.id).then()`, `AddonManager.getPreferredIconURL()`, `OriginControls.getAttentionState()`, `this.#hasAction()`, `this.#setStateMessage()`, `this._messageBarWrapper?.refresh()`, `this.classList.add()`, `this.ownerDocument.l10n.setAttributes()`, `this.querySelector()`, `this.setAttribute()`, `this.toggleAttribute()`
- 条件付き依存: `if (iconURL)` → `this.querySelector(".unified-extensions-item-icon").setAttribute()`
- 条件付き依存: `if (iconURL)` → `this.querySelector()`
- 参照: `this._actionButton.dataset.extensionid`, `this._actionButton.disabled`, `this._menuButton`, `this._menuButton.dataset.extensionid`, `this.documentGlobal`, `this.extension`, `this.extension.id`, `this.extension.name`, `this.extension.policy`, `this.querySelector(".unified-extensions-item-name").textContent`
