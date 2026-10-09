# browser/components/asrouter/content/components/menu-message/menu-message.mjs

source: browser/components/asrouter/content/components/menu-message/menu-message.mjs
source-hash: 3a7fd6b672c5169b1c7f642c78700c7db5803a17
lines: 244

## <module>
- 役割: パネルのメニューに表示する menu-message 要素。サインインや既定ブラウザ設定への誘導を、列・行・分割のレイアウトで描画する Lit の Web Component。
- 呼び出し先: `customElements.define()`

## MenuMessage.constructor()
- 位置: L41-69
- 役割: 既定のレイアウト(column)とボタンサイズを設定し、矢印キーでプライマリボタンと閉じるボタンの間を移動させるキー操作を登録する。
- 触るとき: キーボード操作の移動順や既定のレイアウトを変えるとき。
- 呼び出し先: `super()`, `this.addEventListener()`
- 条件付き依存: `if (this.shadowRoot.activeElement === this.primaryButton)` → `this.closeButton.focus()`
- 条件付き依存: `if (!(this.shadowRoot.activeElement === this.primaryButton))` → `this.primaryButton.focus()`
- 参照: `event.code`, `this.imagePosition`, `this.layout`, `this.primaryButton`, `this.primaryButtonSize`, `this.shadowRoot.activeElement`

## MenuMessage.handleClose()
- 位置: L71-78
- 役割: クリックの伝播を止めてメニューを開いたままにし、MenuMessage:Close を発火する。
- 触るとき: 閉じる操作のイベント名やメニューを閉じる条件を変えるとき。
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`

## MenuMessage.handlePrimaryButton()
- 位置: L80-84
- 役割: プライマリボタンが押されたことを MenuMessage:PrimaryButton として発火する。
- 触るとき: プライマリボタン押下の通知を受け取る側が反応しないと調べるとき。
- 呼び出し先: `this.dispatchEvent()`

## MenuMessage.isRowLayout()
- 位置: L86-88
- 役割: layout が row かを返す。
- 触るとき: row レイアウトの判定条件を変えるとき。
- 参照: `this.layout`

## MenuMessage.isSplitLayout()
- 位置: L90-92
- 役割: layout が split かを返す。
- 触るとき: split レイアウトの判定条件を変えるとき。
- 参照: `this.layout`

## MenuMessage.renderIllustration()
- 位置: L94-107
- 役割: 文字方向が rtl なら rtlImageURL を、そうでなければ imageURL を使うイラスト画像を描画する。
- 触るとき: イラストの左右反転や画像の切り替えを変えるとき。
- 呼び出し先: `html()`, `this.documentGlobal.getComputedStyle()`
- 参照: `this.documentGlobal.getComputedStyle(this).direction`, `this.imageURL`, `this.rtlImageURL`

## MenuMessage.renderSplitLayout()
- 位置: L109-142
- 役割: 上段に本文と閉じるボタン、下段に本文・プライマリボタンとイラストを並べた分割レイアウトを描画する。
- 触るとき: 分割レイアウトの配置を変えるとき。
- 呼び出し先: `html()`, `this.renderIllustration()`
- 参照: `this.buttonText`, `this.handleClose`, `this.handlePrimaryButton`, `this.primaryButtonSize`, `this.primaryText`, `this.secondaryText`

## MenuMessage.renderRowLayout()
- 位置: L144-180
- 役割: ロゴと閉じるボタンを上段に、本文・ボタン・イラストを下段に並べた行レイアウトを描画する。
- 触るとき: 行レイアウトの配置を変えるとき。
- 呼び出し先: `html()`, `this.renderIllustration()`
- 参照: `this.buttonText`, `this.handleClose`, `this.handlePrimaryButton`, `this.logoURL`, `this.primaryButtonSize`, `this.primaryText`, `this.secondaryText`

## MenuMessage.renderColumnLayout()
- 位置: L182-214
- 役割: ロゴ、閉じるボタン、イラスト、本文、ボタンを縦に並べた列レイアウトを描画する。
- 触るとき: 既定の縦並びレイアウトを変えるとき。
- 呼び出し先: `html()`, `this.renderIllustration()`
- 参照: `this.buttonText`, `this.handleClose`, `this.handlePrimaryButton`, `this.logoURL`, `this.primaryButtonSize`, `this.primaryText`, `this.secondaryText`

## MenuMessage.renderBody()
- 位置: L216-224
- 役割: layout の値に応じて分割、行、列のいずれかを描画する。
- 触るとき: レイアウトの種類を増やすとき。
- 呼び出し先: `this.renderColumnLayout()`
- 条件付き依存: `if (this.isSplitLayout)` → `this.renderSplitLayout()`
- 条件付き依存: `if (this.isRowLayout)` → `this.renderRowLayout()`
- 参照: `this.isRowLayout`, `this.isSplitLayout`

## MenuMessage.render()
- 位置: L226-240
- 役割: レイアウトと画像位置の属性を持つコンテナに、本体を入れて描画する。
- 触るとき: メニューメッセージ全体のスタイルの読み込みや属性を変えるとき。
- 呼び出し先: `html()`, `this.renderBody()`
- 参照: `this.imagePosition`, `this.imageURL`, `this.layout`, `this.logoURL`
