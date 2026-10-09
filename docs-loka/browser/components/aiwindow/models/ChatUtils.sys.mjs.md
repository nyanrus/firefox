# browser/components/aiwindow/models/ChatUtils.sys.mjs

source: browser/components/aiwindow/models/ChatUtils.sys.mjs
source-hash: 4014eab459610d67d5e54d4492a54c7d816eaf02
lines: 492

## <module>
- 役割: AI ウィンドウのチャットで使う補助関数群(信頼できないページ情報の無害化、現在時刻・タブ情報・記憶の注入メッセージ生成、URL のトークン化と復元)をまとめる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## _setLoadPromptForTesting()
- 位置: L37-49
- 役割: テスト用に lazy.loadPrompt を差し替え、null が渡されたら元の property descriptor に戻す。
- 触るとき: ChatUtils のプロンプト読み込みをテストでモックするとき、またはテスト後に元へ戻す処理が効かないとき。
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedLoadPromptDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.loadPrompt`

## sanitizeUntrustedContent()
- 位置: L76-98
- 役割: 100 字で切り詰め、truncateOnly でなければ引用符とバックスラッシュをエスケープし空白を畳んで「(Untrusted webpage data)」の印を付ける。
- 触るとき: ページタイトルなど Web 由来の文字列をプロンプトに入れる経路を変えるとき。変更にはセキュリティレビューが要る(関数の注記参照)。
- 呼び出し先: `fixedText .replace()`, `fixedText .replace(/\\/g, "\\\\") .replace()`, `fixedText .replace(/\\/g, "\\\\") .replace(/"/g, '\\"') .replace()`
- 条件付き依存: `if (text.length > MAX_METADATA_LENGTH)` → `fixedText.slice()`
- 参照: `text.length`

## getLocalIsoTime()
- 位置: L105-116
- 役割: ローカル時刻を YYYY-MM-DDTHH:MM:SS 形式の文字列で返し、失敗時は null を返す。
- 触るとき: モデルへ渡す現在時刻の書式やタイムゾーンの扱いを変えるとき。
- 呼び出し先: `date.getDate()`, `date.getFullYear()`, `date.getHours()`, `date.getMinutes()`, `date.getMonth()`, `date.getSeconds()`, `pad()`

## pad()
- 位置: L108-108
- 役割: 数値を 2 桁のゼロ埋め文字列にする getLocalIsoTime 内の補助関数。
- 触るとき: 時刻の桁埋めを他の箇所でも使いたくなったとき(通常は getLocalIsoTime を直接見る)。
- 呼び出し先: `String()`, `String(n).padStart()`

## getCurrentTabMetadata()
- 位置: async L125-145
- 役割: コンテキストのうち currentTab の URL とサニタイズ済みタイトルを返す。説明文は未実装で空文字になる。
- 触るとき: 現在のタブ情報をモデルに渡す内容を変えるとき、または説明文の取得(BUG 2015574 の関連)を実装するとき。
- 呼び出し先: `contextMentions.find()`, `sanitizeUntrustedContent()`
- 参照: `contextWebsite.type`, `currentTab.label`, `currentTab.url`

## constructRealTimeInfoInjectionMessage()
- 位置: async L156-177
- 役割: タブ情報、ロケール、タイムゾーン、ISO 時刻、今日の日付を集め、リアルタイム情報の注入用オブジェクトにまとめる。
- 触るとき: モデルに毎ターン渡す現在の状況(日付や開いているページ)を増やす、または減らすとき。
- 呼び出し先: `Boolean()`, `Intl.DateTimeFormat()`, `Intl.DateTimeFormat().resolvedOptions()`, `getCurrentTabMetadata()`, `getLocalIsoTime()`, `isNewPageUrl()`, `isoTimestamp?.split()`
- 参照: `Intl.DateTimeFormat().resolvedOptions().timeZone`, `Services.locale.appLocaleAsBCP47`
- XPCOM: `Services.locale`

## constructRelevantMemoriesContextMessage()
- 位置: async L194-244
- 役割: 今の発言に関連する記憶を取得し、前ターンの記憶と ID で重複除去してから、関連記憶用プロンプトを描画したメッセージを返す。該当が無ければ null。
- 触るとき: 記憶の注入で取りこぼしや重複が出るとき、または関連記憶プロンプトの中身を変えるとき。
- 呼び出し先: `( await lazy.MemoriesManager.getRelevantMemories(message) ).map()`, `contextMemories .map()`, `contextMemories .map(memory => { return `${memory.id} - ${memory.memory_summary}`; }) .join()`, `lazy.MemoriesManager.getRelevantMemories()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `seenIds.has()`
- 条件付き依存: `if (!seenIds.has(memory.id))` → `seenIds.add()`
- 条件付き依存: `if (!seenIds.has(memory.id))` → `contextMemories.push()`
- 参照: `contextMemories.length`, `lazy.MODEL_FEATURES.MEMORIES_CONTEXT`, `memory.id`, `memory.memory_summary`

## parseContentWithTokens()
- 位置: async L253-294
- 役割: 応答中の §search: と §existing_memory: の印を末尾から取り除き、検索クエリと使われた記憶の一覧と整形後の本文を返す。
- 触るとき: モデル応答から検索指示や記憶参照を抜き出す仕組みを変えるとき、または応答本文に印が残って見えるとき。
- 呼び出し先: `[...searchTokens, ...memoriesTokens].sort()`, `cleanContent.slice()`, `cleanContent.trim()`, `detectTokens()`
- 条件付き依存: `if (token.query)` → `searchQueries.unshift()`
- 条件付き依存: `if (token.memories)` → `usedMemories.unshift()`
- 参照: `a.startIndex`, `allTokens.length`, `b.startIndex`, `token.endIndex`, `token.memories`, `token.query`, `token.startIndex`

## detectTokens()
- 位置: L304-316
- 役割: 正規表現の全一致を走査して、一致文字列・キーの値・開始と終了の位置を配列で返す。
- 触るとき: 新しい印(トークン)の形式を追加して検出するとき。
- 呼び出し先: `match[1].trim()`, `matches.push()`, `regexPattern.exec()`
- 参照: `match.index`, `match[0].length`

## isNewPageUrl()
- 位置: L324-326
- 役割: URL が AI ウィンドウの新規ページ(chrome://browser/content/aiwindow/aiWindow.html)かを判定する。
- 触るとき: 新規ページのときタブ情報を注入しない挙動を変えるとき、またはページ URL を変えたとき。

## resolveMentionUrls()
- 位置: L335-340
- 役割: スマートバーの [ラベル](mention:?href=...) 形式のメンションを、href の URL に置き換える。
- 触るとき: メンションの書式を変えるとき、またはメンション由来の URL がモデルに届かないとき。
- 呼び出し先: `new URLSearchParams(query).get()`, `text.replace()`

## resolveUrlTokenItem()
- 位置: L350-359
- 役割: 1 つの文字列が URL トークン 1 件だけなら対応する URL を返し、それ以外は expandUrlTokens で展開する。
- 触るとき: ツール引数の配列要素に含まれるトークン展開が合わないとき。
- 呼び出し先: `expandUrlTokens()`, `item.matchAll()`
- 条件付き依存: `if (matches.length === 1)` → `tokenToUrl.get()`
- 参照: `matches.length`

## expandUrlTokensInToolParams()
- 位置: L368-381
- 役割: ツール引数の文字列と文字列配列にある URL トークンを、tokenToUrl の対応 URL へ in-place で展開する。
- 触るとき: モデルが出したトークンをツール実行前に実 URL に戻す処理を変えるとき。
- 呼び出し先: `Object.entries()`
- 条件付き依存: `if (typeof value === "string")` → `expandUrlTokens()`
- 条件付き依存: `if (!(typeof value === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(value))` → `value.map()`
- 条件付き依存: `if (Array.isArray(value))` → `resolveUrlTokenItem()`
- 参照: `tokenToUrl.size`

## constructUrlTokensFromMessageContent()
- 位置: L394-431
- 役割: メッセージ本文を markdown-it で解析して link の href を集め、会話の tokenToUrl に登録する。tool 役割では JSON として再帰的に走査する。
- 触るとき: どの URL をトークン化対象にするか(リンクの抽出規則)を変えるとき。
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
- 役割: 送信前のメッセージから URL を集めて登録し、長い URL から順に §url_token: ...§ へ置き換える(system 以外の本文とツール引数)。
- 触るとき: モデルに送る前に URL をトークン化する範囲や順序を変えるとき、またはモデルが URL を幻覚する問題を調べるとき。
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
- 役割: replaceUrlsWithTokens 内の閉包で、tokenToUrl の全 URL を文字列中で §url_token§ に置換する。
- 触るとき: 置換の順序(長い URL 優先)や置換対象の文字列を変えるとき。
- 呼び出し先: `text.replaceAll()`
