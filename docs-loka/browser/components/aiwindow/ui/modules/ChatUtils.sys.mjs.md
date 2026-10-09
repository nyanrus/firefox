# browser/components/aiwindow/ui/modules/ChatUtils.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatUtils.sys.mjs
source-hash: ff05252e15059b31e9802c410baebeefc04f1546
lines: 390

## <module>
- 役割: チャットの DB 行の変換、JSON の安全な読み書き、フィードバック送信用の正規化など、チャット全体で使う補助関数を集める。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## getCurrentTabUrl()
- 位置: L28-30
- 役割: ウィンドウで選択中のタブの現在の URL を返す。
- 触るとき: メッセージのページ URL やコンテキストのチップに使う URL を取り直す処理を変えるとき。
- 参照: `window?.gBrowser?.selectedTab?.linkedBrowser?.currentURI`

## makeGuid()
- 位置: L37-41
- 役割: 72 ビットのランダム値を base64url の 12 文字 ID にする。
- 触るとき: 会話やメッセージの ID の形式や長さを変えるとき。
- 呼び出し先: `ChromeUtils.base64URLEncode()`, `lazy.CryptoUtils.generateRandomBytes()`

## parseConversationRow()
- 位置: L50-73
- 役割: DB の会話行を ChatConversation に変換する。
- 触るとき: 会話の保存列を増やすとき、または再読み込みで会話の属性が欠ける問題を調べるとき。
- 呼び出し先: `Array.isArray()`, `URL.parse()`, `parseJSONOrNull()`, `row.getResultByName()`

## parseMessageRows()
- 位置: L82-113
- 役割: DB のメッセージ行を ChatMessage に変換し、ツール結果を種類別に振り分ける。
- 触るとき: メッセージの保存列やツール結果の種類を変えるとき、または読み込み後に履歴・引用が消える問題を調べるとき。
- 呼び出し先: `URL.parse()`, `parseJSONOrNull()`, `row.getResultByName()`, `rows.map()`
- 参照: `TOOL_RESULT_TYPE.CITATIONS`, `TOOL_RESULT_TYPE.HISTORY_RESULTS`, `TOOL_RESULT_TYPE.TOOL_UI`

## parseChatHistoryViewRows()
- 位置: L122-136
- 役割: 履歴画面の行を ChatHistoryResult に変換し、URL を検証して URL オブジェクトにする。
- 触るとき: 履歴画面の一覧に出る項目や URL の扱いを変えるとき。
- 呼び出し先: `(parseJSONOrNull(row.getResultByName("urls")) ?? []) .filter()`, `(parseJSONOrNull(row.getResultByName("urls")) ?? []) .filter(url => url && url.trim()) .map()`, `parseJSONOrNull()`, `row.getResultByName()`, `rows.map()`, `url.trim()`

## parseJSONOrNull()
- 位置: L144-153
- 役割: JSON 文字列を読み、空や壊れた値は null として扱う。
- 触るとき: DB の JSON 列の読み込みで例外を出さずに既定値へ落としたいとき。
- 呼び出し先: `JSON.parse()`

## toJSONOrNull()
- 位置: L162-164
- 役割: 値があれば JSON 文字列にし、無ければ null を返す。
- 触るとき: DB に保存する JSON 列の書式を変えるとき。
- 呼び出し先: `JSON.stringify()`

## stripResolvedAssets()
- 位置: L175-180
- 役割: 保存前に、サムネイルの画像とファビコン有無の欄を取り除いた複製を返す。
- 触るとき: 履歴や引用に保存する項目を増やす・減らすとき。画像は読み込み時に解決し直す前提。
- 参照: `persisted.hasFavicon`, `persisted.image`

## getRoleLabel()
- 位置: L189-205
- 役割: メッセージの役割の数値をユーザー、アシスタントなどの英語の表示名に変える。
- 触るとき: 役割の表示名を変えるとき、または新しい役割を追加するとき。
- 参照: `MESSAGE_ROLE.ASSISTANT`, `MESSAGE_ROLE.SYSTEM`, `MESSAGE_ROLE.TOOL`, `MESSAGE_ROLE.USER`

## getKeepSidebarOpenState()
- 位置: L219-225
- 役割: タブごとのサイドバー状態と既定値から、開いておくかを決める。
- 触るとき: サイドバーを開いたままにする条件を変えるとき。値が null なら既定値に従う。
- 参照: `state?.keepSidebarOpen`

## normalizeTokens()
- 位置: L233-242
- 役割: トークン欄のうち、スキーマで定めた検索・記憶・提案の 3 項目だけを残す。
- 触るとき: フィードバックや Glean に送るトークン項目を増減するとき。
- 参照: `tokens.existing_memory`, `tokens.followup`, `tokens.search`

## normalizeToolUIData()
- 位置: L250-272
- 役割: ツール UI データから、スキーマで定めた項目だけを取り出してタブ情報も整える。
- 触るとき: ツール UI の項目を Glean に送る形を変えるとき。
- 呼び出し先: `toolUIData.properties.tabs?.map()`
- 参照: `toolUIData.properties`, `toolUIData.properties.originalUserPrompt`, `toolUIData.toolCallId`, `toolUIData.uiType`

## normalizeToolCalls()
- 位置: L283-289
- 役割: tool_calls の type 欄を call_type に改名し、関数の名前と引数だけを残す。
- 触るとき: ツール呼び出しを送信データに載せ方を変えるとき。type を使うと Glean の生成で問題になる点に注意。
- 呼び出し先: `toolCalls?.map()`
- 参照: `fn.arguments`, `fn.name`

## normalizeContent()
- 位置: L302-339
- 役割: メッセージ内容を Glean に送れる形に揃える（本文は文字列、配列、tool_calls のいずれかに分ける）。
- 触るとき: フィードバックや Glean に送るメッセージ内容の形を変えるとき、または送信で項目が欠ける問題を調べるとき。
- 呼び出し先: `contextMentions?.map()`
- 条件付き依存: `if (!(typeof body === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(body))` → `body.map()`
- 条件付き依存: `if (Array.isArray(body))` → `JSON.stringify()`
- 条件付き依存: `if (body?.tool_calls)` → `normalizeToolCalls()`
- 参照: `body.tool_calls`, `body?.tool_calls`, `content.contextPageUrl`, `content.name`, `content.tool_call_id`, `content.userContext`, `content.userContext.realTimeContext`

## normalizeChatLog()
- 位置: L361-389
- 役割: チャットログを、フィードバック表示と Glean 送信用に、必要な項目だけの形に整える。
- 触るとき: フィードバックで送る項目を増やす・減らすとき。会話 ID は意図して含めていない（追跡されないため）。
- 呼び出し先: `Array.isArray()`, `chat.log.map()`, `normalizeContent()`, `normalizeTokens()`, `normalizeToolUIData()`
- 参照: `chat?.log`, `msg.content`, `msg.createdDate`, `msg.followUpSuggestions`, `msg.id`, `msg.isActiveBranch`, `msg.memoriesApplied`, `msg.memoriesEnabled`, `msg.memoriesFlagSource`, `msg.modelId`, `msg.ordinal`, `msg.pageHistoryDeleted`, `msg.pageUrl`, `msg.parentMessageId`, `msg.revisionRootMessageId`, `msg.role`, `msg.tokens`, `msg.toolUIData`, `msg.turnIndex`, `msg.webSearchQueries`
