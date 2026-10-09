# browser/base/content/browser-pagestyle.js

source: browser/base/content/browser-pagestyle.js
source-hash: bcfc4c8c636fb33f191b34863068fcefcc99bfe5
lines: 127

## <module>
- 役割: 表示メニューの Page Style(代替スタイルシートの一覧表示と切り替え)を担う gPageStyleMenu 定義

## _getStyleSheetInfo()
- 位置: L6-22
- 役割: 選択中ブラウザの PageStyle アクターからスタイルシート情報を取得し、無ければ空の既定値を返す。
- 触るとき: ページのスタイルシート情報の取得経路を変えるとき。
- 呼び出し先: `browser.browsingContext.currentWindowGlobal?.getActor()`
- 条件付き依存: `if (actor)` → `actor.getSheetInfo()`

## fillPopup()
- 位置: L24-80
- 役割: Page Style メニューの項目を再構築し、No Style・Persistent のチェック状態と表示を更新する。
- 触るとき: メニュー項目の表示条件やチェック状態のルールを変えるとき。
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
- 役割: 選択中タブの BrowsingContext ツリーを辿り、各フレームの PageStyle アクターへメッセージを送る。
- 触るとき: スタイル切り替えを子フレームへ伝える経路を調べるとき。
- 呼び出し先: `actor.sendAsyncMessage()`, `contextsToVisit.pop()`, `contextsToVisit.push()`, `global.getActor()`
- 参照: `contextsToVisit.length`, `currentContext.children`, `currentContext.currentWindowGlobal`, `gBrowser.selectedBrowser.browsingContext`

## switchStyleSheet()
- 位置: L112-118
- 役割: 指定タイトル以外のスタイルシートを無効化し、全フレームへ切り替えを通知する。
- 触るとき: 代替スタイルの切り替え挙動を変えるとき。
- 呼び出し先: `this._getStyleSheetInfo()`, `this._sendMessageToAll()`
- 参照: `gBrowser.selectedBrowser`, `sheet.disabled`, `sheet.title`, `sheetData.filteredStyleSheets`

## disableStyle()
- 位置: L123-125
- 役割: 全フレームへ Page Style の無効化メッセージを送り、スタイルを外す(No Style)。
- 触るとき: No Style の動作を調べるとき。
- 呼び出し先: `this._sendMessageToAll()`
