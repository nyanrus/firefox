# browser/base/content/browser-pagestyle.js

source: browser/base/content/browser-pagestyle.js
source-hash: bcfc4c8c636fb33f191b34863068fcefcc99bfe5
lines: 127

## <module>
- 役割: (未記入)

## _getStyleSheetInfo()
- 位置: L6-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.browsingContext.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (actor)` → `actor.getSheetInfo()`

## fillPopup()
- 位置: L24-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `menuPopup.removeChild()`, `noStyle.toggleAttribute()`, `persistentOnly.toggleAttribute()`, `this._getStyleSheetInfo()`
- 条件付き依存: `if (!lastWithSameTitle)` → `document.createXULElement()`
- 条件付き依存: `if (!lastWithSameTitle)` → `menuItem.setAttribute()`
- 条件付き依存: `if (!lastWithSameTitle)` → `menuItem.toggleAttribute()`
- 条件付き依存: `if (!lastWithSameTitle)` → `menuItem.addEventListener()`
- 条件付き依存: `if (!lastWithSameTitle)` → `this.switchStyleSheet()`
- 条件付き依存: `if (!lastWithSameTitle)` → `event.currentTarget.getAttribute()`
- 条件付き依存: `if (!lastWithSameTitle)` → `menuPopup.appendChild()`
- 条件付き依存: `if (currentStyleSheet.disabled)` → `lastWithSameTitle.removeAttribute()`
- 参照: `currentStyleSheet.disabled`, `currentStyleSheet.title`, `gBrowser.selectedBrowser`, `gBrowser.selectedBrowser.browsingContext?.authorStyleDisabledDefault`, `menuPopup.firstElementChild`, `noStyle.hidden`, `noStyle.nextElementSibling`, `persistentOnly.hidden`, `persistentOnly.nextElementSibling`, `sep.hidden`, `sep.nextElementSibling`, `styleSheetInfo.filteredStyleSheets`, `styleSheetInfo.preferredStyleSheetSet`

## _sendMessageToAll()
- 位置: L90-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.sendAsyncMessage()`, `contextsToVisit.pop()`, `contextsToVisit.push()`, `global.getActor()`
- 参照: `contextsToVisit.length`, `currentContext.children`, `currentContext.currentWindowGlobal`, `gBrowser.selectedBrowser.browsingContext`

## switchStyleSheet()
- 位置: L112-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getStyleSheetInfo()`, `this._sendMessageToAll()`
- 参照: `gBrowser.selectedBrowser`, `sheet.disabled`, `sheet.title`, `sheetData.filteredStyleSheets`

## disableStyle()
- 位置: L123-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._sendMessageToAll()`
