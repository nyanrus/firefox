# browser/components/aiwindow/ui/components/ai-website-chip/ai-website-chip.mjs

source: browser/components/aiwindow/ui/components/ai-website-chip/ai-website-chip.mjs
source-hash: 8f22c7ca2bee1de7aa1a6955c019906b3a467fbe
lines: 233

## <module>
- 役割: サイトやタブを示すチップ ai-website-chip(入力欄用の in-line と文脈用の context-chip)を定義する。
- 呼び出し先: `customElements.define()`

## AIWebsiteChip.constructor()
- 位置: L59-71
- 役割: type、size、label などを既定値にし、openLinkEvent を AIChatContent:OpenLink にする。
- 触るとき: チップの既定の種類や既定のリンクイベント名を変えたいとき。
- 呼び出し先: `super()`
- 参照: `this.href`, `this.iconSrc`, `this.isTabGroup`, `this.itemRole`, `this.label`, `this.openLinkEvent`, `this.removable`, `this.size`, `this.tabGroupColor`, `this.type`

## AIWebsiteChip.connectedCallback()
- 位置: L73-76
- 役割: 取り付けられた時点のルートノードのホスト要素を親として覚えておく。
- 触るとき: チップの削除を親へ通知する先がずれるとき。
- 呼び出し先: `super.connectedCallback()`, `this.getRootNode()`
- 参照: `this.#parentHost`, `this.getRootNode()?.host`

## AIWebsiteChip.disconnectedCallback()
- 位置: L78-95
- 役割: 親がまだ接続されていれば ai-website-chip:disconnected を親へ送る。親ごと外れた時は送らない。
- 触るとき: ユーザーの削除だけを親に伝えたいとき、または親の切り替えで通知が出ない原因を調べるとき。
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.#parentHost?.isConnected)` → `this.#parentHost.dispatchEvent()`
- 参照: `this.#parentHost`, `this.#parentHost?.isConnected`, `this.label`, `this.type`

## AIWebsiteChip.#isEmpty()
- 位置: L97-99
- 役割: in-line 型でラベルが空のとき true を返す。
- 触るとき: 空の入力欄チップ(@ と案内文)の表示条件を変えるとき。
- 参照: `this.label`, `this.type`

## AIWebsiteChip.#isRemovable()
- 位置: L101-103
- 役割: removable プロパティをそのまま返す。
- 触るとき: 削除ボタンの出し分けの判定を増やすとき。
- 参照: `this.removable`

## AIWebsiteChip.#handleClick()
- 位置: L105-113
- 役割: ボタン型のチップがクリックされたら、label を載せた ai-website-chip:click を発火する。
- 触るとき: チップのクリックを親が受け取る経路を変えるとき。
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.label`

## AIWebsiteChip.#handleRemove()
- 位置: L115-125
- 役割: 削除ボタンの伝播と既定動作を止め、label を載せた ai-website-chip:remove を発火する。
- 触るとき: 削除で親が何をするかを追うとき、または削除ボタンがリンクを開いてしまうとき。
- 呼び出し先: `e.preventDefault()`, `e.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.label`

## AIWebsiteChip.#handleAnchorClick()
- 位置: L127-150
- 役割: href があれば既定の遷移を止め、修飾キーとボタンの状態を添えて openLinkEvent を発火する。修飾キーなしなら既存タブへの切り替えを要求する。
- 触るとき: リンクの開き方(新しいタブか既存タブか)を変えるとき、または修飾キーの扱いを調べるとき。
- 呼び出し先: `e.preventDefault()`, `this.dispatchEvent()`
- 参照: `e.altKey`, `e.button`, `e.ctrlKey`, `e.metaKey`, `e.shiftKey`, `this.href`, `this.openLinkEvent`

## AIWebsiteChip.render()
- 位置: L152-229
- 役割: 空、タブグループ、favicon の順にアイコンを選び、削除ボタンとラベルを付けて、href の有無で a か button を描画する。
- 触るとき: チップの見た目の出し分けや、タブグループ時のアイコンの扱いを変えるとき。
- 呼び出し先: `html()`, `ifDefined()`
- 条件付き依存: `if (isEmpty)` → `html()`
- 条件付き依存: `if (this.isTabGroup)` → `html()`
- 条件付き依存: `if (!(this.isTabGroup))` → `html()`
- 参照: `e.target.src`, `this.#handleAnchorClick`, `this.#handleClick`, `this.#handleRemove`, `this.#isEmpty`, `this.#isRemovable`, `this.href`, `this.iconSrc`, `this.isTabGroup`, `this.itemRole`, `this.label`, `this.tabGroupColor`
