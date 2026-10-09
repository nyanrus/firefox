# browser/components/aiwindow/models/PromptOptimizer.sys.mjs

source: browser/components/aiwindow/models/PromptOptimizer.sys.mjs
source-hash: 7a3a531a734a195a7b395c6418891f7397fce910
lines: 142

## <module>
- 役割: 会話の履歴を LLM に送る前に圧縮する処理の入口。現状はページ内容の重複除去(Stage 1)だけを行い、後段の圧縮段階を置く予定の場所になっている。

## deduplicatePageContent()
- 位置: L34-111
- 役割: get_page_content の呼び出しごとに URL と最新の呼び出し ID を集め、古い呼び出しの結果本文を「内容省略」の注記に置き換える。
- 触るとき: ページ内容の履歴が重複して膨らむ問題を調べるとき、または get_page_content の返却形式を変えるとき(配列の順序に依存しているので要注意)。
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
- 役割: 圧縮段階を順に適用する公開入口で、例外時は元の配列を返す。現状は重複除去だけを実行する。
- 触るとき: 送信前の履歴圧縮に新しい段階を足すとき、または圧縮が効かないときに呼び出し元を確認するとき。
- 呼び出し先: `console.error()`, `deduplicatePageContent()`
