# browser/components/aiwindow/ui/components/input-cta/input-cta.mjs

source: browser/components/aiwindow/ui/components/input-cta/input-cta.mjs
source-hash: acb20e58b6a092cd70d83717e0ffed7660f9a2f3
lines: 273

## <module>
- 役割: スマートバーの送信ボタンを、意図(chat・search・navigate)に応じて切り替わる分割ボタン input-cta として定義するモジュール。
- 呼び出し先: `customElements.define()`

## InputCta.constructor()
- 位置: L54-62
- 役割: action を空、submitDisabled を false、検索エンジン情報と一覧を空にし、メニューとサブメニューの ID を乱数で作る。
- 触るとき: 初期状態を変えるとき、またはメニューの ID が衝突して開閉がおかしくなると疑うとき。
- 呼び出し先: `crypto.randomUUID()`, `super()`
- 参照: `this._menuId`, `this._searchSubpanelId`, `this.action`, `this.searchEngineInfo`, `this.searchEngines`, `this.submitDisabled`

## InputCta.actionLabelId()
- 位置: L64-66
- 役割: action に対応する送信ラベルの Fluent ID を返し、action が空なら空文字を返す。
- 触るとき: action ごとの送信ボタンの文言を変えるとき。
- 参照: `this.action`

## InputCta.buttonIconSrc()
- 位置: L68-73
- 役割: stop なら停止アイコン、action が空なら転送アイコン、それ以外は undefined を返す。
- 触るとき: action ごとにボタンのアイコンを変えるとき。
- 参照: `this.action`

## InputCta.searchIconUrl()
- 位置: L75-79
- 役割: 検索エンジンのアイコンがあればその url() を、無ければ検索虫眼鏡のアイコンパスを返す。
- 触るとき: 検索エンジンのアイコン表示を変えるとき、またはアイコンが出ないエンジンを調べるとき。
- 参照: `this.searchEngineInfo.icon`, `this.searchEngineInfo?.icon`

## InputCta.#mainPanel()
- 位置: L81-83
- 役割: shadow DOM 内のメインメニュー panel-list を ID で取得する。
- 触るとき: メインメニューの参照先を変えるとき。
- 呼び出し先: `this.shadowRoot?.getElementById()`
- 参照: `this._menuId`

## InputCta.#searchSubpanel()
- 位置: L85-87
- 役割: shadow DOM 内の検索エンジン用サブメニュー panel-list を ID で取得する。
- 触るとき: 検索サブメニューの参照先を変えるとき。
- 呼び出し先: `this.shadowRoot?.getElementById()`
- 参照: `this._searchSubpanelId`

## InputCta.#mozButton()
- 位置: L89-91
- 役割: shadow DOM 内の moz-button を取得する。
- 触るとき: 内部の moz-button を操作するコード(aria-disabled の付与など)を変えるとき。
- 呼び出し先: `this.shadowRoot?.querySelector()`

## InputCta.#setAction()
- 位置: L93-109
- 役割: ACTIONS に含まれる値なら action を更新し、同じ値でも aiwindow-input-cta:on-action-change を発火する。
- 触るとき: メニューからの action 切り替えを変えるとき、または変更通知が親に届かない理由を調べるとき。
- 呼び出し先: `InputCta.ACTIONS.includes()`, `this.dispatchEvent()`
- 参照: `this.action`

## InputCta.#onAction()
- 位置: L111-123
- 役割: submitDisabled かつ stop 以外なら何もせず、stop なら on-stop、それ以外は on-action を発火する。
- 触るとき: 送信ボタンを押したときの挙動や、ガードで送信が止まる条件を変えるとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.action`, `this.submitDisabled`

## InputCta.#onSearchEngineSelect()
- 位置: L125-133
- 役割: 選ばれた検索エンジン名を入れた on-search-engine-select イベントを発火する。
- 触るとき: 検索エンジンの選択結果を親へ渡す経路を変えるとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `engine.name`

## InputCta.#onSearchItemClick()
- 位置: L135-141
- 役割: メインメニューを強制的に閉じ、次のフレームで検索サブメニューを chevron の位置に開く。
- 触るとき: 「検索に使う」項目からサブメニューへの切り替えの順序や見た目を変えるとき。
- 呼び出し先: `event.stopPropagation()`, `requestAnimationFrame()`, `this.#mainPanel?.hide()`, `this.#searchSubpanel?.show()`
- 参照: `this.#mozButton.chevronButtonEl`

## InputCta.#onBackClick()
- 位置: L143-149
- 役割: 検索サブメニューを閉じ、次のフレームでメインメニューを開き直す。
- 触るとき: サブメニューの戻る操作の挙動を変えるとき。
- 呼び出し先: `event.stopPropagation()`, `requestAnimationFrame()`, `this.#mainPanel?.show()`, `this.#searchSubpanel?.hide()`
- 参照: `this.#mozButton.chevronButtonEl`

## InputCta.willUpdate()
- 位置: L151-170
- 役割: 許可されていない action を警告して空に戻し、searchEngineInfo が変わったら --search-icon を設定または削除する。
- 触るとき: action の許容値を変えるとき、または検索アイコンで分割ボタンのレイアウトが崩れる理由を追うとき。
- 呼び出し先: `InputCta.ACTIONS.includes()`, `changedProps.has()`
- 条件付き依存: `if ( changedProps.has("action") && this.action && !InputCta.ACTIONS.includes(this.action) )` → `console.warn()`
- 条件付き依存: `if (this.searchIconUrl)` → `this.style.setProperty()`
- 条件付き依存: `if (!(this.searchIconUrl))` → `this.style.removeProperty()`
- 参照: `this.action`, `this.searchIconUrl`

## InputCta.updated()
- 位置: async L172-189
- 役割: submitDisabled か action が変わったとき、内部の main ボタンに aria-disabled を付けるか外す。
- 触るとき: 送信ガードを支援技術に伝える扱いを変えるとき。
- 呼び出し先: `changedProps.has()`
- 条件付き依存: `if (this.submitDisabled && this.action != "stop")` → `mainButton.setAttribute()`
- 条件付き依存: `if (!(this.submitDisabled && this.action != "stop"))` → `mainButton.removeAttribute()`
- 参照: `this.#mozButton?.buttonEl`, `this.#mozButton?.updateComplete`, `this.action`, `this.submitDisabled`

## InputCta.render()
- 位置: L191-269
- 役割: action と stop の状態に応じて split か ghost の moz-button、メインメニュー、検索サブメニューを組み立てる。
- 触るとき: 送信ボタンの構成、メニューの項目、無効化の条件を変えるとき。
- 呼び出し先: `InputCta.ACTIONS.filter()`, `JSON.stringify()`, `html()`, `repeat()`, `styleMap()`, `this.#onBackClick()`, `this.#onSearchEngineSelect()`, `this.#onSearchItemClick()`, `this.#setAction()`
- 参照: `engine.icon`, `engine.name`, `this.#onAction`, `this._menuId`, `this._searchSubpanelId`, `this.action`, `this.actionLabelId`, `this.buttonIconSrc`, `this.searchEngineInfo.name`, `this.searchEngines`
