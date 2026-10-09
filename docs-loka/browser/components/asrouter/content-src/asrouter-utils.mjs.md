# browser/components/asrouter/content-src/asrouter-utils.mjs

source: browser/components/asrouter/content-src/asrouter-utils.mjs
source-hash: f728f6abf5cda7866afe39d16d6a3d32ec9f27c2
lines: 108

## <module>
- 役割: about:asrouter の管理画面などから、ページ側の ASRouterMessage を通して ASRouter へ操作要求を送るユーティリティ。

## addListener()
- 位置: L8-12
- 役割: ASRouterAddParentListener があれば、親からの通知を受けるリスナーを登録する。
- 触るとき: 親からの通知を受けるページを新しく作るとき。
- 条件付き依存: `if (globalThis.ASRouterAddParentListener)` → `globalThis.ASRouterAddParentListener()`
- 参照: `globalThis.ASRouterAddParentListener`

## removeListener()
- 位置: L13-17
- 役割: ASRouterRemoveParentListener があれば、リスナーを解除する。
- 触るとき: ページ破棄時に通知の購読が残る問題を調べるとき。
- 条件付き依存: `if (globalThis.ASRouterRemoveParentListener)` → `globalThis.ASRouterRemoveParentListener()`
- 参照: `globalThis.ASRouterRemoveParentListener`

## sendMessage()
- 位置: L18-23
- 役割: ASRouterMessage があればそれに action を渡して送る。なければ例外を投げる。
- 触るとき: ASRouter へのすべての操作の送信経路を変えるとき、または Unexpected call の例外が出る原因を調べるとき。
- 呼び出し先: `JSON.stringify()`
- 条件付き依存: `if (globalThis.ASRouterMessage)` → `globalThis.ASRouterMessage()`
- 参照: `globalThis.ASRouterMessage`

## blockById()
- 位置: L24-29
- 役割: 指定 ID のメッセージをブロックするよう BLOCK_MESSAGE_BY_ID を送る。
- 触るとき: 管理画面のブロック操作の引数を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.BLOCK_MESSAGE_BY_ID`

## modifyMessageJson()
- 位置: L30-35
- 役割: メッセージの JSON 内容を書き換えるよう MODIFY_MESSAGE_JSON を送る。
- 触るとき: 管理画面からのメッセージ編集の送信内容を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.MODIFY_MESSAGE_JSON`

## executeAction()
- 位置: L36-41
- 役割: ボタンのアクションを USER_ACTION として送り、そのアクションを実行させる。
- 触るとき: メッセージのボタン操作が ASRouter に届かない、または引数の形式を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.USER_ACTION`

## unblockById()
- 位置: L42-47
- 役割: 指定 ID のブロックを解除するよう UNBLOCK_MESSAGE_BY_ID を送る。
- 触るとき: ブロック解除の挙動を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.UNBLOCK_MESSAGE_BY_ID`

## unblockAll()
- 位置: L48-52
- 役割: 全ブロックを解除するよう UNBLOCK_ALL を送る。
- 触るとき: 管理画面の全解除操作を調べるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.UNBLOCK_ALL`

## resetGroupImpressions()
- 位置: L53-57
- 役割: グループの表示回数をリセットするよう RESET_GROUPS_STATE を送る。
- 触るとき: 表示回数のリセット対象を広げる、または狭めるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.RESET_GROUPS_STATE`

## resetMessageImpressions()
- 位置: L58-62
- 役割: メッセージ単位の表示回数をリセットするよう RESET_MESSAGE_STATE を送る。
- 触るとき: メッセージ単位のリセットが効かない問題を調べるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.RESET_MESSAGE_STATE`

## resetScreenImpressions()
- 位置: L63-67
- 役割: 画面の表示回数をリセットするよう RESET_SCREEN_IMPRESSIONS を送る。
- 触るとき: 画面単位の表示履歴の扱いを変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.RESET_SCREEN_IMPRESSIONS`

## blockBundle()
- 位置: L68-73
- 役割: バンドル単位でブロックするよう BLOCK_BUNDLE を送る。
- 触るとき: バンドル単位のブロックの対象や引数を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.BLOCK_BUNDLE`

## unblockBundle()
- 位置: L74-79
- 役割: バンドル単位のブロックを解除するよう UNBLOCK_BUNDLE を送る。
- 触るとき: バンドルのブロック解除が効かない問題を調べるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.UNBLOCK_BUNDLE`

## overrideMessage()
- 位置: L80-85
- 役割: 指定 ID のメッセージを優先表示するよう OVERRIDE_MESSAGE を送る。
- 触るとき: プレビューで特定メッセージを強制表示する仕組みを変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.OVERRIDE_MESSAGE`

## editState()
- 位置: L86-91
- 役割: ASRouter の状態の一つのキーに値を入れるよう EDIT_STATE を送る。
- 触るとき: 管理画面から状態を編集する項目を増やすとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.EDIT_STATE`

## openPBWindow()
- 位置: L92-97
- 役割: プライベートブラウジングのウィンドウで、与えられたメッセージを開くよう FORCE_PRIVATE_BROWSING_WINDOW を送る。
- 触るとき: プライベートウィンドウ表示の要求内容を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`

## sendTelemetry()
- 位置: L98-103
- 役割: ユーザーイベントのテレメトリを AS_ROUTER_TELEMETRY_USER_EVENT として送る。
- 触るとき: ページ側から送るテレメトリの経路を変えるとき。
- 呼び出し先: `ASRouterUtils.sendMessage()`
- 参照: `msg.AS_ROUTER_TELEMETRY_USER_EVENT`

## getPreviewEndpoint()
- 位置: L104-106
- 役割: プレビュー用のエンドポイントを持たないため、常に null を返す。
- 触るとき: プレビュー機能をこの画面で有効にするとき(現状は未実装)。
