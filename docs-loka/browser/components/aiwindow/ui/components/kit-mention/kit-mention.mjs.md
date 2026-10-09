# browser/components/aiwindow/ui/components/kit-mention/kit-mention.mjs

source: browser/components/aiwindow/ui/components/kit-mention/kit-mention.mjs
source-hash: d47dd8adb1bcd4ead16879c42714c14d82804971
lines: 86

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## KitMention.constructor()
- 位置: L31-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.show`

## KitMention.disconnectedCallback()
- 位置: L36-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.#hideTimeoutId !== null)` → `clearTimeout()`
- 参照: `this.#hideTimeoutId`

## KitMention.trigger()
- 位置: L44-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`
- 参照: `this.#hideTimeoutId`, `this.#shownForConvId`, `this.show`

## KitMention.reset()
- 位置: L59-66
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#hideTimeoutId !== null)` → `clearTimeout()`
- 参照: `this.#hideTimeoutId`, `this.#shownForConvId`, `this.show`

## KitMention.render()
- 位置: L68-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.show`
