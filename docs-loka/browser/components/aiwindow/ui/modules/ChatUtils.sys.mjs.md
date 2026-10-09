# browser/components/aiwindow/ui/modules/ChatUtils.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatUtils.sys.mjs
source-hash: ff05252e15059b31e9802c410baebeefc04f1546
lines: 390

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getCurrentTabUrl()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `window?.gBrowser?.selectedTab?.linkedBrowser?.currentURI`

## makeGuid()
- 位置: L37-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.base64URLEncode()`, `lazy.CryptoUtils.generateRandomBytes()`

## parseConversationRow()
- 位置: L50-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `URL.parse()`, `parseJSONOrNull()`, `row.getResultByName()`

## parseMessageRows()
- 位置: L82-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `parseJSONOrNull()`, `row.getResultByName()`, `rows.map()`
- 参照: `TOOL_RESULT_TYPE.CITATIONS`, `TOOL_RESULT_TYPE.HISTORY_RESULTS`, `TOOL_RESULT_TYPE.TOOL_UI`

## parseChatHistoryViewRows()
- 位置: L122-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(parseJSONOrNull(row.getResultByName("urls")) ?? []) .filter()`, `(parseJSONOrNull(row.getResultByName("urls")) ?? []) .filter(url => url && url.trim()) .map()`, `parseJSONOrNull()`, `row.getResultByName()`, `rows.map()`, `url.trim()`

## parseJSONOrNull()
- 位置: L144-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`

## toJSONOrNull()
- 位置: L162-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`

## stripResolvedAssets()
- 位置: L175-180
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `persisted.hasFavicon`, `persisted.image`

## getRoleLabel()
- 位置: L189-205
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `MESSAGE_ROLE.ASSISTANT`, `MESSAGE_ROLE.SYSTEM`, `MESSAGE_ROLE.TOOL`, `MESSAGE_ROLE.USER`

## getKeepSidebarOpenState()
- 位置: L219-225
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `state?.keepSidebarOpen`

## normalizeTokens()
- 位置: L233-242
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tokens.existing_memory`, `tokens.followup`, `tokens.search`

## normalizeToolUIData()
- 位置: L250-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolUIData.properties.tabs?.map()`
- 参照: `toolUIData.properties`, `toolUIData.properties.originalUserPrompt`, `toolUIData.toolCallId`, `toolUIData.uiType`

## normalizeToolCalls()
- 位置: L283-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toolCalls?.map()`
- 参照: `fn.arguments`, `fn.name`

## normalizeContent()
- 位置: L302-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contextMentions?.map()`
- 条件付き依存: `if (!(typeof body === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(body))` → `body.map()`
- 条件付き依存: `if (Array.isArray(body))` → `JSON.stringify()`
- 条件付き依存: `if (body?.tool_calls)` → `normalizeToolCalls()`
- 参照: `body.tool_calls`, `body?.tool_calls`, `content.contextPageUrl`, `content.name`, `content.tool_call_id`, `content.userContext`, `content.userContext.realTimeContext`

## normalizeChatLog()
- 位置: L361-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `chat.log.map()`, `normalizeContent()`, `normalizeTokens()`, `normalizeToolUIData()`
- 参照: `chat?.log`, `msg.content`, `msg.createdDate`, `msg.followUpSuggestions`, `msg.id`, `msg.isActiveBranch`, `msg.memoriesApplied`, `msg.memoriesEnabled`, `msg.memoriesFlagSource`, `msg.modelId`, `msg.ordinal`, `msg.pageHistoryDeleted`, `msg.pageUrl`, `msg.parentMessageId`, `msg.revisionRootMessageId`, `msg.role`, `msg.tokens`, `msg.toolUIData`, `msg.turnIndex`, `msg.webSearchQueries`
