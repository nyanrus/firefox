# browser/components/extensions/child/ext-omnibox.js

source: browser/components/extensions/child/ext-omnibox.js
source-hash: c144a1860ba10b035ebb0bbefc50b886516364f6
lines: 39

## <module>
- 役割: 拡張の子側で omnibox.onInputChanged イベントを提供する ExtensionAPI 定義のファイル。

## getAPI()
- 位置: L8-37
- 役割: omnibox.onInputChanged を持つ API オブジェクトを返す。
- 触るとき: omnibox の公開 API の形を変えるとき、または onInputChanged が見えない問題を調べるとき。

## register()
- 位置: L16-33
- 役割: 親側の onInputChanged に listener を付け、解除時に外す関数を返す。
- 触るとき: リスナーの登録・解除が二重になる、または解除されない問題を調べるとき。
- 呼び出し先: `context.childManager .getParentEvent()`, `context.childManager .getParentEvent("omnibox.onInputChanged") .addListener()`, `context.childManager .getParentEvent("omnibox.onInputChanged") .removeListener()`

## listener()
- 位置: L17-24
- 役割: 入力テキストを拡張のイベントへ渡し、返された候補を id と共に親の omnibox.addSuggestions へ送る。
- 触るとき: 候補が表示されない、または古い入力 ID の候補が混ざる問題を調べるとき。
- 呼び出し先: `context.childManager.callParentFunctionNoReturn()`, `fire.asyncWithoutClone()`
