# browser/components/aiwindow/ui/components/aitab-tool-ui/aitab-tool-ui.mjs

source: browser/components/aiwindow/ui/components/aitab-tool-ui/aitab-tool-ui.mjs
source-hash: 9f6c2e4f6e5e8b8a03e81607b7cae337bd54bf96
lines: 146

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITabToolUI.constructor()
- 位置: L21-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.completeStateOpen`, `this.state`, `this.title`

## AITabToolUI.#handleKeyboardActivation()
- 位置: L28-33
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "Enter" || event.key === " ")` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Enter" || event.key === " ")` → `this.#toggleCompleteMessage()`
- 参照: `event.key`

## AITabToolUI.#toggleCompleteMessage()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.completeStateOpen`

## AITabToolUI.#requestOpen()
- 位置: L39-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## AITabToolUI.#renderCreating()
- 位置: L49-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## AITabToolUI.#renderChoose()
- 位置: L57-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#requestOpen()`
- 参照: `this.title`

## AITabToolUI.#renderComplete()
- 位置: L85-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#handleKeyboardActivation()`, `this.#toggleCompleteMessage()`
- 参照: `this.completeStateOpen`, `this.title`

## AITabToolUI.#renderState()
- 位置: L118-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderChoose()`, `this.#renderComplete()`, `this.#renderCreating()`
- 参照: `this.state`

## AITabToolUI.render()
- 位置: L134-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderState()`
