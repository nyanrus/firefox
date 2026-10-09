# browser/components/aiwindow/ui/components/aitab-page/aitab-page-actions/aitab-page-actions.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-page-actions/aitab-page-actions.mjs
source-hash: 98a24a73d94ead60efa32b6bc2e0ec287dd4c27c
lines: 119

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITabPageActions.constructor()
- 位置: L31-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.refreshing`

## AITabPageActions.#dialog()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## AITabPageActions.#emit()
- 位置: L40-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AITabPageActions.#onRefresh()
- 位置: L46-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emit()`
- 参照: `this.refreshing`

## AITabPageActions.#onDeleteRequested()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dialog?.showModal()`

## AITabPageActions.#onConfirmDelete()
- 位置: L57-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#dialog?.close()`, `this.#emit()`

## AITabPageActions.#renderDeleteDialog()
- 位置: L62-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#dialog?.close()`, `this.#onConfirmDelete()`

## AITabPageActions.render()
- 位置: L87-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#onDeleteRequested()`, `this.#onRefresh()`, `this.#renderDeleteDialog()`
- 参照: `this.refreshing`
