# browser/components/preferences/FocusHistory.mjs

source: browser/components/preferences/FocusHistory.mjs
source-hash: fa4fa31ed7fc7df5735b3b2c2e74164379dccdd7
lines: 48

## <module>
- 役割: (未記入)

## FocusHistory.save()
- 位置: L22-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#focused.set()`
- 条件付き依存: `if (!el || el === document.body || el === document.documentElement)` → `this.#focused.delete()`
- 参照: `document.activeElement`, `document.body`, `document.documentElement`

## FocusHistory.restore()
- 位置: L39-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#focused.get()`, `this.#focused.get(historyId)?.deref()`
- 条件付き依存: `if (el?.isConnected)` → `el.focus()`
- 参照: `el?.isConnected`
