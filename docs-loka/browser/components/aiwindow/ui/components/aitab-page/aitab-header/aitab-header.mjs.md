# browser/components/aiwindow/ui/components/aitab-page/aitab-header/aitab-header.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-header/aitab-header.mjs
source-hash: 06838b91731519349a06bd409f63a0fd463980ef
lines: 99

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITabHeader.constructor()
- 位置: L39-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.createdAt`, `this.references`, `this.refreshing`, `this.subhead`, `this.title`

## AITabHeader.#renderCreatedAt()
- 位置: L48-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.createdAt`

## AITabHeader.#renderReferences()
- 位置: L56-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.references.map()`
- 参照: `source.favicon`, `source.href`, `source.title`, `this.references.length`

## AITabHeader.render()
- 位置: L72-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#renderCreatedAt()`, `this.#renderReferences()`
- 参照: `this.refreshing`, `this.subhead`, `this.title`
