# browser/components/aiwindow/models/TitleGeneration.sys.mjs

source: browser/components/aiwindow/models/TitleGeneration.sys.mjs
source-hash: 2d4fdadd2f962d43186de3ad6949ef1bf782207e
lines: 89

## <module>
- 役割: チャットのタイトルを決める。既定はメッセージ先頭 4 語の文字列、LLM が使えるときは会話の内容から生成したタイトルを返す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## generateDefaultTitle()
- 位置: L28-44
- 役割: メッセージの先頭 4 語に「...」を付けて返す。空や非文字列なら「New Chat」を返す。
- 触るとき: LLM を使わない場合のタイトルの見え方を変えるとき。
- 呼び出し先: `message .trim()`, `message .trim() .split()`, `message .trim() .split(/\s+/) .filter()`, `titleWords.join()`, `words.slice()`
- 参照: `word.length`, `words.length`

## generateChatTitle()
- 位置: async L56-88
- 役割: タブ情報(タイトルは無害化)とユーザー発言、必要なら最初のアシスタント応答を入れてタイトル生成の会話を実行し、失敗や空のときは既定タイトルに戻す。
- 触るとき: タイトル生成の入力や失敗時の扱いを変えるとき。current_tab のタイトルは呼び出し元のオブジェクトを書き換える点に注意。
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `console.error()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `generateDefaultTitle()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `openAIEngine.getFxAccountToken()`, `renderPrompt()`, `response?.finalOutput?.trim()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (assistantResponse)` → `conversation.addAssistantMessage()`
- 参照: `MODEL_FEATURES.TITLE_GENERATION`, `tabInfo.title`
