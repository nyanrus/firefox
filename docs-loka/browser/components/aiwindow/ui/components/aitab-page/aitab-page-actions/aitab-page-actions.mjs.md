# browser/components/aiwindow/ui/components/aitab-page/aitab-page-actions/aitab-page-actions.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-page-actions/aitab-page-actions.mjs
source-hash: 98a24a73d94ead60efa32b6bc2e0ec287dd4c27c
lines: 119

## <module>
- 役割: AI Tab ページの再取得・削除ボタンを定義する aitab-page-actions
- 呼び出し先: `customElements.define()`

## AITabPageActions.constructor()
- 位置: L31-34
- 役割: refreshing を false で初期化する
- 触るとき: 再取得中フラグの既定値を変えるとき。
- 呼び出し先: `super()`
- 参照: `this.refreshing`

## AITabPageActions.#dialog()
- 位置: L36-38
- 役割: shadow root 内の dialog 要素を取り出す
- 触るとき: 削除確認ダイアログの要素参照が外れる構造変更をするとき。
- 呼び出し先: `this.renderRoot.querySelector()`

## AITabPageActions.#emit()
- 位置: L40-44
- 役割: 指定の名前のカスタムイベントを bubbles・composed で発火する
- 触るとき: ホスト側へ通知するイベント名や伝播の仕方を変えるとき。
- 呼び出し先: `this.dispatchEvent()`

## AITabPageActions.#onRefresh()
- 位置: L46-51
- 役割: 再取得中でなければ refresh イベントを発火する
- 触るとき: 再取得の二重実行を防ぐ条件を変えるとき。実際の再取得はホストが行う。
- 呼び出し先: `this.#emit()`
- 参照: `this.refreshing`

## AITabPageActions.#onDeleteRequested()
- 位置: L53-55
- 役割: 削除確認の dialog をモーダルで開く
- 触るとき: 削除ボタンを押した後の確認手順を変えるとき。
- 呼び出し先: `this.#dialog?.showModal()`

## AITabPageActions.#onConfirmDelete()
- 位置: L57-60
- 役割: dialog を閉じて delete イベントを発火する
- 触るとき: 削除の確定時に行う処理を追加・変更するとき。
- 呼び出し先: `this.#dialog?.close()`, `this.#emit()`

## AITabPageActions.#renderDeleteDialog()
- 位置: L62-85
- 役割: 削除確認ダイアログの本文と確定・取消ボタンを描画する
- 触るとき: 確認文言の構成やボタンの種類、初期フォーカス先を変えるとき。
- 呼び出し先: `html()`, `this.#dialog?.close()`, `this.#onConfirmDelete()`

## AITabPageActions.render()
- 位置: L87-115
- 役割: 再取得ボタンと削除ボタンを並べ、確認ダイアログを添える
- 触るとき: 再取得中の表示切り替えや、ボタンのアイコン・並びを変えるとき。
- 呼び出し先: `html()`, `this.#onDeleteRequested()`, `this.#onRefresh()`, `this.#renderDeleteDialog()`
- 参照: `this.refreshing`
