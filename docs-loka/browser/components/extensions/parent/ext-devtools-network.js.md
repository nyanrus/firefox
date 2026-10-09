# browser/components/extensions/parent/ext-devtools-network.js

source: browser/components/extensions/parent/ext-devtools-network.js
source-hash: 21bbd252147220d658c81b54d881b3cacf4a6502
lines: 81

## <module>
- 役割: devtools.inspectedWindow と devtools.network の API を実装し、拡張から DevTools の評価・再読み込み・HAR・リクエスト完了通知を利用できるようにする。

## getAPI()
- 位置: L12-79
- 役割: devtools.network の API を組み立て、onNavigated・getHAR・onRequestFinished と内部用の Request.getContent を公開する。
- 触るとき: devtools.network の公開メソッドを追加・変更するとき。

## register()
- 位置: L19-30
- 役割: ナビゲーション通知の購読を登録し、解除時に非同期で購読を外す関数を返す。
- 触るとき: onNavigated の購読開始・解除の順序で問題が起きたときに調べる。
- 呼び出し先: `context.addOnNavigatedListener()`, `context.removeOnNavigatedListener()`, `promise.then()`

## listener()
- 位置: L20-22
- 役割: ナビゲーションの URL を fire.async で拡張へ渡す。
- 触るとき: onNavigated に渡る値を変えるとき。
- 呼び出し先: `fire.async()`

## getHAR()
- 位置: L33-35
- 役割: ツールボックスのネットワークモニターから HAR を取得して返す。
- 触るとき: 拡張が取得する HAR の内容や取得方法を変えるとき。
- 呼び出し先: `context.devToolsToolbox.getHARFromNetMonitor()`

## register()
- 位置: L40-51
- 役割: リクエスト完了の購読をツールボックスに登録し、解除時にリスナーを外す関数を返す。
- 触るとき: onRequestFinished が届かない、または解除されないときに確認する。
- 呼び出し先: `toolbox.addRequestFinishedListener()`, `toolbox.removeRequestFinishedListener()`
- 参照: `context.devToolsToolbox`

## listener()
- 位置: L41-43
- 役割: 完了したリクエストのデータを fire.async で拡張へ渡す。
- 触るとき: onRequestFinished に渡るデータの形式を変えるとき。
- 呼び出し先: `fire.async()`

## getContent()
- 位置: async L58-74
- 役割: リクエストのレスポンス本文と MIME タイプを取得して返し、失敗時はエラーを報告して拡張用の ExtensionError を投げる。
- 触るとき: 拡張の request.getContent が失敗する原因を調べるとき、またはエラー文言を変えるとき。
- 呼び出し先: `Cu.reportError()`, `context.devToolsToolbox .fetchResponseContent()`, `context.devToolsToolbox .fetchResponseContent(requestId) .then()`
- 参照: `content.mimeType`, `content.text`, `context.extension.policy.debugName`
