# browser/components/firefoxview/recentbrowsing.mjs

source: browser/components/firefoxview/recentbrowsing.mjs
source-hash: 57ed188b8a8cfa62b75baef5393fe9e0877e3d70
lines: 69

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## RecentBrowsingInView.constructor()
- 位置: L9-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.pageType`

## RecentBrowsingInView.viewVisibleCallback()
- 位置: L22-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `childView.viewVisibleCallback()`
- 参照: `child.firstElementChild`, `childView.paused`, `this.children`

## RecentBrowsingInView.viewHiddenCallback()
- 位置: L30-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `childView.viewHiddenCallback()`
- 参照: `child.firstElementChild`, `childView.paused`, `this.children`

## RecentBrowsingInView.onSearchQuery()
- 位置: L38-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.searchInitiatedSearch.record()`

## RecentBrowsingInView.render()
- 位置: L46-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.onSearchQuery`
