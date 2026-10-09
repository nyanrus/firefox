# browser/components/aiwindow/models/PromptOptimizer.sys.mjs

source: browser/components/aiwindow/models/PromptOptimizer.sys.mjs
source-hash: 7a3a531a734a195a7b395c6418891f7397fce910
lines: 142

## <module>
- 役割: (未記入)

## deduplicatePageContent()
- 位置: L34-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if ( toolCall.type === "function" && toolCall.function?.name === "get_page_content" )` → `JSON.parse()`
- 条件付き依存: `if ( toolCall.type === "function" && toolCall.function?.name === "get_page_content" )` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(args.url_list))` → `callIdToUrls.set()`
- 条件付き依存: `if (Array.isArray(args.url_list))` → `urlToLatestCallId.set()`
- 条件付き依存: `if ( toolCall.type === "function" && toolCall.function?.name === "get_page_content" )` → `console.warn()`
- 条件付き依存: `if ( msg.role === "tool" && msg.name === "get_page_content" && msg.tool_call_id )` → `callIdToUrls.get()`
- 条件付き依存: `if (requestedUrls)` → `JSON.parse()`
- 条件付き依存: `if (requestedUrls)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(contentArray))` → `contentArray.map()`
- 条件付き依存: `if (Array.isArray(contentArray))` → `urlToLatestCallId.get()`
- 条件付き依存: `if (Array.isArray(contentArray))` → `JSON.stringify()`
- 条件付き依存: `if (requestedUrls)` → `console.warn()`
- 参照: `args.url_list`, `msg.content`, `msg.name`, `msg.role`, `msg.tool_call_id`, `msg.tool_calls`, `toolCall.function.arguments`, `toolCall.function?.name`, `toolCall.id`, `toolCall.type`

## compactMessages()
- 位置: L126-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `deduplicatePageContent()`
