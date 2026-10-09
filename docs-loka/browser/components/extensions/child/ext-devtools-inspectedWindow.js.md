# browser/components/extensions/child/ext-devtools-inspectedWindow.js

source: browser/components/extensions/child/ext-devtools-inspectedWindow.js
source-hash: 566ab6b197f0f165cba0a89b6c8f89fab9e93345
lines: 28

## <module>
- 役割: devtools.inspectedWindow の子側 API を定義し、検査中のタブ ID を拡張へ公開する。

## getAPI()
- 位置: L8-26
- 役割: 子コンテキストのツールボックス情報から検査対象のタブ ID を取り出し、devtools.inspectedWindow として返す。
- 触るとき: devtools.inspectedWindow API の内容を変えるとき。
- 参照: `context.devtoolsToolboxInfo`, `context.devtoolsToolboxInfo.inspectedWindowTabId`

## tabId()
- 位置: L20-22
- 役割: ツールボックス情報の inspectedWindowTabId を読み取り専用で返す。
- 触るとき: 拡張が検査中のタブを知る経路を変えるとき。
