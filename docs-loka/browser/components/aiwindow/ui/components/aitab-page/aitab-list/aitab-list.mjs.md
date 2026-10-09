# browser/components/aiwindow/ui/components/aitab-page/aitab-list/aitab-list.mjs

source: browser/components/aiwindow/ui/components/aitab-page/aitab-list/aitab-list.mjs
source-hash: 5cb359ac26a03c65804fd27af55e3e8cc46bc3d9
lines: 101

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## AITabList.constructor()
- 位置: L37-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.description`, `this.groups`, `this.layout`, `this.title`

## AITabList.#renderIntro()
- 位置: L45-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.description`, `this.title`

## AITabList.#renderGroup()
- 位置: L62-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.items.map()`, `html()`
- 参照: `group.heading`, `item?.text`

## AITabList.render()
- 位置: L75-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.groups ?? []).filter()`, `groups.map()`, `html()`, `this.#renderGroup()`, `this.#renderIntro()`
- 参照: `group?.items?.length`, `groups.length`, `this.groups`
