# browser/components/storybook/component-status/component-status.stories.mjs

source: browser/components/storybook/component-status/component-status.stories.mjs
source-hash: 32dcec0d4c237e19840b8d2707a5c2e84d10c1d0
lines: 181

## <module>
- 役割: (未記入)
- 呼び出し先: `css()`, `customElements.define()`

## ComponentStatusList.constructor()
- 位置: L81-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `super()`
- 参照: `componentsData.items`, `componentsData?.items`, `this._components`

## ComponentStatusList.render()
- 位置: L89-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this._renderTable()`

## ComponentStatusList._storyHrefFromId()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)

## ComponentStatusList._renderLinkGroup()
- 位置: L116-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/bugzilla\.mozilla\.org/.test()`, `html()`, `links.map()`, `this._storyHrefFromId()`
- 条件付き依存: `if (it.sourceUrl)` → `links.push()`
- 条件付き依存: `if (bugUrl && /bugzilla\.mozilla\.org/.test(bugUrl))` → `links.push()`
- 参照: `it.bugUrl`, `it.sourceUrl`, `it.storyId`, `opts.top`

## ComponentStatusList._renderTable()
- 位置: L142-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this._components.map()`, `this._renderLinkGroup()`, `this._storyHrefFromId()`
- 参照: `it.component`, `it.status`, `it.storyId`

## Default()
- 位置: L178-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
