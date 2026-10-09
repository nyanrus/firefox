# browser/components/extensions/child/ext-tabs.js

source: browser/components/extensions/child/ext-tabs.js
source-hash: b1ea0c7dcc4ad8c08adf0ec69efdcf15708e7c69
lines: 34

## <module>
- 役割: 拡張の子側で tabs.connect と tabs.sendMessage を提供する ExtensionAPI 定義のファイル。

## getAPI()
- 位置: L7-32
- 役割: tabs.connect と tabs.sendMessage を持つ API オブジェクトを返す。
- 触るとき: tabs API の公開メソッドを増減するとき。

## connect()
- 位置: L10-18
- 役割: options から frameId、name、documentId を既定値付きで取り出し、tabId と共に context.messenger.connect へ渡す。
- 触るとき: 特定フレームや文書への接続先指定が効かない問題を調べるとき。
- 呼び出し先: `context.messenger.connect()`

## sendMessage()
- 位置: L20-29
- 役割: tabId、frameId、documentId、message、callback をまとめ、context.messenger.sendRuntimeMessage へ渡す。
- 触るとき: tabs.sendMessage の宛先指定や callback の扱いを変えるとき。
- 呼び出し先: `context.messenger.sendRuntimeMessage()`
- 参照: `options?.documentId`, `options?.frameId`
