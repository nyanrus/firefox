# browser/components/aiwindow/models/ChatUtils.sys.mjs

source: browser/components/aiwindow/models/ChatUtils.sys.mjs
source-hash: 4014eab459610d67d5e54d4492a54c7d816eaf02
lines: 492

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## _setLoadPromptForTesting()
- 位置: L37-49
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedLoadPromptDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.loadPrompt`

## sanitizeUntrustedContent()
- 位置: L76-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fixedText .replace()`, `fixedText .replace(/\\/g, "\\\\") .replace()`, `fixedText .replace(/\\/g, "\\\\") .replace(/"/g, '\\"') .replace()`
- 条件付き依存: `if (text.length > MAX_METADATA_LENGTH)` → `fixedText.slice()`
- 参照: `text.length`

## getLocalIsoTime()
- 位置: L105-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `date.getDate()`, `date.getFullYear()`, `date.getHours()`, `date.getMinutes()`, `date.getMonth()`, `date.getSeconds()`, `pad()`

## pad()
- 位置: L108-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(n).padStart()`

## getCurrentTabMetadata()
- 位置: async L125-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contextMentions.find()`, `sanitizeUntrustedContent()`
- 参照: `contextWebsite.type`, `currentTab.label`, `currentTab.url`

## constructRealTimeInfoInjectionMessage()
- 位置: async L156-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`, `Intl.DateTimeFormat()`, `Intl.DateTimeFormat().resolvedOptions()`, `getCurrentTabMetadata()`, `getLocalIsoTime()`, `isNewPageUrl()`, `isoTimestamp?.split()`
- 参照: `Intl.DateTimeFormat().resolvedOptions().timeZone`, `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## constructRelevantMemoriesContextMessage()
- 位置: async L194-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await lazy.MemoriesManager.getRelevantMemories(message) ).map()`, `contextMemories .map()`, `contextMemories .map(memory => { return `${memory.id} - ${memory.memory_summary}`; }) .join()`, `lazy.MemoriesManager.getRelevantMemories()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `seenIds.has()`
- 条件付き依存: `if (!seenIds.has(memory.id))` → `seenIds.add()`
- 条件付き依存: `if (!seenIds.has(memory.id))` → `contextMemories.push()`
- 参照: `contextMemories.length`, `lazy.MODEL_FEATURES.MEMORIES_CONTEXT`, `memory.id`, `memory.memory_summary`

## parseContentWithTokens()
- 位置: async L253-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...searchTokens, ...memoriesTokens].sort()`, `cleanContent.slice()`, `cleanContent.trim()`, `detectTokens()`
- 条件付き依存: `if (token.query)` → `searchQueries.unshift()`
- 条件付き依存: `if (token.memories)` → `usedMemories.unshift()`
- 参照: `a.startIndex`, `allTokens.length`, `b.startIndex`, `token.endIndex`, `token.memories`, `token.query`, `token.startIndex`

## detectTokens()
- 位置: L304-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `match[1].trim()`, `matches.push()`, `regexPattern.exec()`
- 参照: `match.index`, `match[0].length`

## isNewPageUrl()
- 位置: L324-326
- 役割: (未記入)
- 触るとき: (未記入)

## resolveMentionUrls()
- 位置: L335-340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new URLSearchParams(query).get()`, `text.replace()`

## resolveUrlTokenItem()
- 位置: L350-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `expandUrlTokens()`, `item.matchAll()`
- 条件付き依存: `if (matches.length === 1)` → `tokenToUrl.get()`
- 参照: `matches.length`

## expandUrlTokensInToolParams()
- 位置: L368-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (typeof value === "string")` → `expandUrlTokens()`
- 条件付き依存: `if (!(typeof value === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(value))` → `value.map()`
- 条件付き依存: `if (Array.isArray(value))` → `resolveUrlTokenItem()`
- 参照: `tokenToUrl.size`

## constructUrlTokensFromMessageContent()
- 位置: L394-431
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (role === "tool")` → `JSON.parse()`
- 条件付き依存: `if (role === "tool")` → `constructUrlTokensFromMessageContent()`
- 条件付き依存: `if (typeof content === "string")` → `lazy.md.parse()`
- 条件付き依存: `if (child.type === "link_open")` → `child.attrGet()`
- 条件付き依存: `if (child.type === "link_open")` → `URL.parse()`
- 条件付き依存: `if (href && URL.parse(href))` → `urls.add()`
- 条件付き依存: `if (typeof content === "string")` → `conversation.convertUrlToToken()`
- 条件付き依存: `if (!(typeof content === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(content))` → `constructUrlTokensFromMessageContent()`
- 条件付き依存: `if (typeof content === "object")` → `Object.values()`
- 条件付き依存: `if (typeof content === "object")` → `constructUrlTokensFromMessageContent()`
- 参照: `child.type`, `tok.children`

## replaceUrlsWithTokens()
- 位置: L443-491
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if (msg.role != "system" && typeof msg.content === "string")` → `constructUrlTokensFromMessageContent()`
- 条件付き依存: `if (typeof args === "string")` → `constructUrlTokensFromMessageContent()`
- 条件付き依存: `if (conversation.tokenToUrl.size)` → `[...conversation.tokenToUrl.entries()].sort()`
- 条件付き依存: `if (conversation.tokenToUrl.size)` → `conversation.tokenToUrl.entries()`
- 条件付き依存: `if (msg.role != "system" && typeof msg.content === "string")` → `tokenizeUrls()`
- 条件付き依存: `if (conversation.tokenToUrl.size)` → `Array.isArray()`
- 条件付き依存: `if (typeof toolCall.function?.arguments === "string")` → `tokenizeUrls()`
- 参照: `a.length`, `b.length`, `conversation.tokenToUrl.size`, `msg.content`, `msg.role`, `msg.tool_calls`, `toolCall.function.arguments`, `toolCall.function?.arguments`

## tokenizeUrls()
- 位置: L469-474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.replaceAll()`
