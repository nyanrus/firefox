# browser/components/firefoxview/chats-tab-list.mjs

source: browser/components/firefoxview/chats-tab-list.mjs
source-hash: c06bb64bb7bd17d7390874dbc0bf09effa1d9e50
lines: 209

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## ChatsTabList.itemTemplate()
- 位置: L32-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`
- 条件付き依存: `if (tabItem.time || tabItem.closedAt)` → `(tabItem.time || tabItem.closedAt).toString()`
- 参照: `stringTime.length`, `tabItem.closedAt`, `tabItem.closedId`, `tabItem.convId`, `tabItem.icon`, `tabItem.matchingSnippet`, `tabItem.pageUrl`, `tabItem.primaryL10nArgs`, `tabItem.primaryL10nId`, `tabItem.secondaryL10nArgs`, `tabItem.secondaryL10nId`, `tabItem.sourceClosedId`, `tabItem.sourceWindowId`, `tabItem.tertiaryL10nArgs`, `tabItem.tertiaryL10nId`, `tabItem.time`, `tabItem.title`, `tabItem.url`, `this.activeIndex`, `this.compactRows`, `this.currentActiveElementId`, `this.dateTimeFormat`, `this.hasPopup`, `this.searchQuery`, `this.secondaryActionClass`, `this.tertiaryActionClass`, `this.timeMsPref`

## ChatsTabRow.faviconTemplate()
- 位置: L91-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classMap()`, `html()`, `styleMap()`, `this.pageUrl.startsWith()`
- 条件付き依存: `if (hasExternalUrl)` → `this.getImageUrl()`
- 参照: `this.favicon`, `this.pageUrl`

## ChatsTabRow.urlTemplate()
- 位置: L125-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.highlightSearchMatches()`, `this.pageUrl.startsWith()`, `when()`
- 参照: `this.pageUrl`, `this.searchQuery`

## ChatsTabRow.snippetTemplate()
- 位置: L142-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `defaultMarkdownParser.parse()`, `doc .textBetween()`, `doc .textBetween(0, doc.content.size, " ") .replace()`, `doc .textBetween(0, doc.content.size, " ") .replace(/\*{2,}/g, "") // remove unparsed bold markers .trim()`, `html()`, `text.toLowerCase()`, `text.toLowerCase().indexOf()`, `this.highlightSearchMatches()`, `this.searchQuery.toLowerCase()`
- 条件付き依存: `if (idx === -1)` → `text.substring()`
- 条件付き依存: `if (!(idx === -1))` → `Math.max()`
- 条件付き依存: `if (!(idx === -1))` → `Math.min()`
- 条件付き依存: `if (!(idx === -1))` → `text.substring()`
- 参照: `doc.content.size`, `text.length`, `this.matchingSnippet`, `this.searchQuery`, `this.searchQuery.length`

## ChatsTabRow.render()
- 位置: L173-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `ifDefined()`, `this.dateTemplate()`, `this.faviconTemplate()`, `this.secondaryButtonTemplate()`, `this.snippetTemplate()`, `this.stylesheets()`, `this.tertiaryButtonTemplate()`, `this.timeTemplate()`, `this.titleTemplate()`, `this.urlTemplate()`, `when()`
- 参照: `this.active`, `this.compact`, `this.convId`, `this.currentActiveElementId`, `this.primaryActionHandler`, `this.primaryL10nArgs`, `this.primaryL10nId`, `this.url`
