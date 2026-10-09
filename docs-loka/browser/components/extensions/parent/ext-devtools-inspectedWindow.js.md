# browser/components/extensions/parent/ext-devtools-inspectedWindow.js

source: browser/components/extensions/parent/ext-devtools-inspectedWindow.js
source-hash: e3c5b0e7dca76a22b7fde27b6894023f8418a287
lines: 52

## <module>
- 役割: devtools.inspectedWindow と devtools.network の API を実装し、拡張から DevTools の評価・再読み込み・HAR・リクエスト完了通知を利用できるようにする。

## getAPI()
- 位置: L10-50
- 役割: devtools.inspectedWindow の API を組み立て、拡張の ID と URL を呼び出し元情報として eval と reload に渡す。
- 触るとき: 拡張が inspectedWindow を呼んだときの呼び出し元情報の中身を変えるとき。
- 参照: `context.extension.baseURI.spec`, `context.extension.id`

## eval()
- 位置: async L22-36
- 役割: ツールボックスの評価オプションを付けて、検査中のページで式を評価し、結果と例外情報を SpreadArgs で返す。
- 触るとき: 拡張の eval の戻り値や例外の扱いを変えるとき。
- 呼び出し先: `Object.assign()`, `commands.inspectedWindowCommand.eval()`, `context.getDevToolsCommands()`, `getToolboxEvalOptions()`
- 参照: `evalResult.exceptionInfo`, `evalResult.value`

## reload()
- 位置: async L37-46
- 役割: キャッシュ無視・UserAgent・注入スクリプトの指定を付けて、検査中のページを再読み込みする。
- 触るとき: 拡張からのページ再読み込みのオプションを追加するとき。
- 呼び出し先: `commands.inspectedWindowCommand.reload()`, `context.getDevToolsCommands()`
