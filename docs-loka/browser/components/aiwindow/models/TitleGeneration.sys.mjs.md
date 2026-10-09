# browser/components/aiwindow/models/TitleGeneration.sys.mjs

source: browser/components/aiwindow/models/TitleGeneration.sys.mjs
source-hash: 2d4fdadd2f962d43186de3ad6949ef1bf782207e
lines: 89

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## generateDefaultTitle()
- 位置: L28-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `message .trim()`, `message .trim() .split()`, `message .trim() .split(/\s+/) .filter()`, `titleWords.join()`, `words.slice()`
- 参照: `word.length`, `words.length`

## generateChatTitle()
- 位置: async L56-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `console.error()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `generateDefaultTitle()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `openAIEngine.getFxAccountToken()`, `renderPrompt()`, `response?.finalOutput?.trim()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (assistantResponse)` → `conversation.addAssistantMessage()`
- 参照: `MODEL_FEATURES.TITLE_GENERATION`, `tabInfo.title`
