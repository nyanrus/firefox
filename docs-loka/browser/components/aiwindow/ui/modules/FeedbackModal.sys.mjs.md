# browser/components/aiwindow/ui/modules/FeedbackModal.sys.mjs

source: browser/components/aiwindow/ui/modules/FeedbackModal.sys.mjs
source-hash: c28acdd71914a56f220d956b7a41cfec68ec0879
lines: 81

## <module>
- 役割: チャットへのフィードバック（good / bad）の画面を、ASRouter のメッセージに会話ログを差し込んで Spotlight で開くモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## open()
- 位置: async L19-79
- 役割: フィードバック用メッセージを取得し、会話のメタデータとログを報告用の文面に差し込んで Spotlight を表示する。取得できなければ何もしない。
- 触るとき: フィードバック画面に載る内容（ログの版、ページ内容なしの版、表示する見出し）を変えるとき。
- 呼び出し先: `console.error()`, `lazy.ASRouter.handleMessageRequest()`, `lazy.Spotlight.showSpotlightDialog()`, `structuredClone()`
- 条件付き依存: `if (metadata)` → `tiles?.find()`
- 条件付き依存: `if (textboxTile && metadata.chatLog)` → `JSON.stringify()`
- 条件付き依存: `if (textboxTile && metadata.chatLog)` → `lazy.normalizeChatLog()`
- 条件付き依存: `if (metadata.chatLogWithoutPageContent)` → `JSON.stringify()`
- 条件付き依存: `if (metadata.chatLogWithoutPageContent)` → `lazy.normalizeChatLog()`
- 参照: `clonedMessage.content.feedbackData`, `clonedMessage.content.screens`, `contentToggleTile.data.visible`, `lazy.ASRouter.waitForInitialized`, `metadata.chatLog`, `metadata.chatLogWithoutPageContent`, `metadata.metadata`, `screen.content`, `t.type`, `textboxTile.data.alternateContent`, `textboxTile.data.content`, `textboxTile.header.title.string_id`, `textboxTile.header?.title`
