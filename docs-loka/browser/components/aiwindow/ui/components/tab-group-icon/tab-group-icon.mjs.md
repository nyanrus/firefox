# browser/components/aiwindow/ui/components/tab-group-icon/tab-group-icon.mjs

source: browser/components/aiwindow/ui/components/tab-group-icon/tab-group-icon.mjs
source-hash: e749da7167d6a31fea8c567e5d772454e1490da4
lines: 60

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## TabGroupIcon.constructor()
- 位置: L23-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.color`, `this.label`

## TabGroupIcon.willUpdate()
- 位置: L29-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `changedProperties.has()`, `this.style.setProperty()`
- 参照: `this.color`

## TabGroupIcon.#initial()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(Array.from(this.label?.trim() ?? "")[0] ?? "").toUpperCase()`, `Array.from()`, `this.label?.trim()`

## TabGroupIcon.render()
- 位置: L48-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.#initial`
