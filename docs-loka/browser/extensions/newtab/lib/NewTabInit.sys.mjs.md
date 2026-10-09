# browser/extensions/newtab/lib/NewTabInit.sys.mjs

source: browser/extensions/newtab/lib/NewTabInit.sys.mjs
source-hash: d7f70b62e2f9245236df5ce4489a093e643462dc
lines: 61

## <module>
- 役割: (未記入)

## NewTabInit.constructor()
- 位置: L20-22
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._repliedEarlyTabs`

## NewTabInit.reply()
- 位置: L24-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToOneContent()`, `this._repliedEarlyTabs.get()`, `this._repliedEarlyTabs.has()`, `this.store.dispatch()`, `this.store.getState()`
- 条件付き依存: `if (this._repliedEarlyTabs.has(target))` → `this._repliedEarlyTabs.set()`
- 参照: `at.NEW_TAB_INITIAL_STATE`

## NewTabInit.onAction()
- 位置: L43-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._repliedEarlyTabs.delete()`, `this.reply()`
- 条件付き依存: `if (action.data.simulated)` → `this._repliedEarlyTabs.set()`
- 参照: `action.data.portID`, `action.data.simulated`, `action.meta.fromTarget`, `action.type`, `at.NEW_TAB_INIT`, `at.NEW_TAB_STATE_REQUEST`, `at.NEW_TAB_UNLOAD`
