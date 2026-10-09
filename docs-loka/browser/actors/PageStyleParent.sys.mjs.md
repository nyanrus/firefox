# browser/actors/PageStyleParent.sys.mjs

source: browser/actors/PageStyleParent.sys.mjs
source-hash: 3f7bb8b14bc40edd8a004c32cb7854e0f4781a07
lines: 74

## <module>
- 役割: 子から届いたページのスタイルシート情報を、最上位フレームのアクターに保持する親側アクター。

## PageStyleParent.receiveMessage()
- 位置: L29-49
- 役割: PageStyle:Add は最上位のアクターに情報を追加し、Clear は自分が最上位のときだけ情報を消す。
- 触るとき: スタイル情報の追加やクリアの条件を変えるとき。
- 呼び出し先: `actor.addSheetInfo()`, `this.browsingContext.top.currentWindowGlobal.getActor()`
- 参照: `browser.documentGlobal.closed`, `msg.data`, `msg.name`, `this.#styleSheetInfo`, `this.browsingContext.top.embedderElement`

## PageStyleParent.addSheetInfo()
- 位置: L58-62
- 役割: 受け取ったシート一覧を末尾に追加し、既定のスタイル選択フラグを OR で更新する。
- 触るとき: スタイル情報の蓄積方法を変えるとき。
- 呼び出し先: `info.filteredStyleSheets.push()`, `this.getSheetInfo()`
- 参照: `info.preferredStyleSheetSet`, `newSheetData.filteredStyleSheets`, `newSheetData.preferredStyleSheetSet`

## PageStyleParent.getSheetInfo()
- 位置: L64-72
- 役割: 情報がまだなければ空の一覧と既定値 true を作って返す。
- 触るとき: スタイル情報の初期値を変えるとき。
- 参照: `this.#styleSheetInfo`
