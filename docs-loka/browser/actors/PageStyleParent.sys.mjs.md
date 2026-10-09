# browser/actors/PageStyleParent.sys.mjs

source: browser/actors/PageStyleParent.sys.mjs
source-hash: 3f7bb8b14bc40edd8a004c32cb7854e0f4781a07
lines: 74

## <module>
- 役割: (未記入)

## PageStyleParent.receiveMessage()
- 位置: L29-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.addSheetInfo()`, `this.browsingContext.top.currentWindowGlobal.getActor()`
- 参照: `browser.documentGlobal.closed`, `msg.data`, `msg.name`, `this.#styleSheetInfo`, `this.browsingContext.top.embedderElement`

## PageStyleParent.addSheetInfo()
- 位置: L58-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `info.filteredStyleSheets.push()`, `this.getSheetInfo()`
- 参照: `info.preferredStyleSheetSet`, `newSheetData.filteredStyleSheets`, `newSheetData.preferredStyleSheetSet`

## PageStyleParent.getSheetInfo()
- 位置: L64-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#styleSheetInfo`
