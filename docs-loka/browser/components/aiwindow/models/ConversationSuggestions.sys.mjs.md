# browser/components/aiwindow/models/ConversationSuggestions.sys.mjs

source: browser/components/aiwindow/models/ConversationSuggestions.sys.mjs
source-hash: 165a67894edb49d1c1df35cd7e69afdb93f853a1
lines: 978

## <module>
- 役割: 新規タブや サイドバーに出す会話の開始候補・フォローアップ候補・「前回の続き」候補を、記憶と閲覧履歴を材料に LLM で生成する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## _setLoadPromptForTesting()
- 位置: L58-70
- 役割: テスト用に lazy.loadPrompt を差し替え、null で元のプロパティ記述子に戻す。
- 触るとき: この候補生成のプロンプト読み込みをテストでモックするとき。
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedLoadPromptDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.loadPrompt`

## _setBuildConversationForTesting()
- 位置: L73-89
- 役割: テスト用に lazy.buildConversation を差し替え、null で元に戻す。
- 触るとき: 会話生成をテストで差し替えるとき。
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedBuildConversationDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.buildConversation`

## _setGetConversationsByIdForTesting()
- 位置: L92-108
- 役割: テスト用に lazy.getConversationsById を差し替え、null で元に戻す。
- 触るとき: 過去チャットの取得をテストで差し替えるとき。
- 条件付き依存: `if (fn !== null)` → `Object.getOwnPropertyDescriptor()`
- 条件付き依存: `if (_savedGetConversationsByIdDescriptor)` → `Object.defineProperty()`
- 参照: `lazy.getConversationsById`

## _clearResumeActivityCacheForTesting()
- 位置: L125-127
- 役割: 「前回の続き」候補のキャッシュを空にする。
- 触るとき: テスト間でキャッシュが残って結果が変わるとき。
- 呼び出し先: `_resumeActivityCache.clear()`

## trimConversation()
- 位置: L136-151
- 役割: user と assistant の空でない発言だけを残し、末尾 maxMessages 件に切り詰める。tool や system は含めない。
- 触るとき: フォローアップ候補の入力に渡す履歴の範囲を変えるとき。
- 呼び出し先: `m.content.trim()`, `out.slice()`
- 条件付き依存: `if ( (m.role === MESSAGE_ROLE.USER || m.role === MESSAGE_ROLE.ASSISTANT) && m.content && m.content.trim() )` → `out.push()`
- 参照: `MESSAGE_ROLE.ASSISTANT`, `MESSAGE_ROLE.USER`, `m.content`, `m.role`

## addMemoriesToPrompt()
- 位置: async L160-173
- 役割: 記憶の要約を最大 MAX_NUM_MEMORIES 件取り、記憶用プロンプトを描画してベース文の後ろに連結する。記憶が無ければベース文をそのまま返す。
- 触るとき: 候補生成のプロンプトに記憶を入れる件数や書式を変えるとき。
- 呼び出し先: `MemoriesGetterForSuggestionPrompts.getMemorySummariesForPrompt()`
- 条件付き依存: `if (memorySummaries.length)` → `memorySummaries.map(s => `- ${s}`).join()`
- 条件付き依存: `if (memorySummaries.length)` → `memorySummaries.map()`
- 条件付き依存: `if (memorySummaries.length)` → `lazy.renderPrompt()`
- 参照: `memorySummaries.length`

## cleanInferenceOutput()
- 位置: L181-193
- 役割: 出力を行に分け、行頭の箇条書き記号や番号と末尾の句点、「ラベル:」の接頭辞を取り除いて候補文の配列にする。
- 触るとき: モデル出力の行が候補文として表示されない・余計な記号が残るとき。
- 呼び出し先: `(result.finalOutput || "").trim()`, `l.trim()`, `line.replace()`, `lines .map()`, `lines .map(line => line.replace(/^[-*\d.)\[\]]+\s*/, "")) .filter()`, `lines .map(line => line.replace(/^[-*\d.)\[\]]+\s*/, "")) .filter(p => p.length) .map()`, `p.replace()`, `p.replace(/\.$/, "").replace()`, `text .split()`, `text .split(/\n+/) .map()`, `text .split(/\n+/) .map(l => l.trim()) .filter()`
- 参照: `p.length`, `result.finalOutput`

## unpackJsonArrayOutput()
- 位置: L201-227
- 役割: 出力を JSON 配列として解析し、id・headline・status が揃うオブジェクトだけを残す。配列でなければ空配列を返す。
- 触るとき: 前回の続き候補のモデル出力の形式を変えるとき、または候補が欠落するとき。
- 呼び出し先: `Array.isArray()`, `lazy.console.warn()`, `lazy.parseAndExtractJSON()`, `parsed.filter()`
- 条件付き依存: `if (!Array.isArray(parsed))` → `lazy.console.warn()`
- 参照: `item.headline`, `item.id`, `item.status`

## formatJson()
- 位置: L235-241
- 役割: 値を JSON 文字列にし、失敗時は String() で文字列化する。
- 触るとき: プロンプトに埋める構造化データの書式を変えるとき。
- 呼び出し先: `JSON.stringify()`, `String()`

## getRandom()
- 位置: L275-277
- 役割: 配列から一様乱数で 1 要素を選ぶ。
- 触るとき: 候補文の出し分けを確率的でなく固定にするなど、ランダム性を変えるとき。
- 呼び出し先: `Math.floor()`, `Math.random()`
- 参照: `arr.length`

## getPrompts()
- 位置: async L288-311
- 役割: タブ数と履歴設定(places.history.enabled と private browsing)から使える候補 ID を選び、執筆・計画と閲覧系 1 件の l10n ID を返す。
- 触るとき: 新規タブの定型候補の内容や条件(タブ数や履歴の有無による出し分け)を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `ids.map()`, `this.browsingPrompts.filter()`, `this.getRandom()`
- 条件付き依存: `if (browsingPrompt)` → `ids.push()`
- 参照: `browsingPrompt.id`, `p.minTabs`, `p.needsHistory`, `this.planningPrompts`, `this.writingPrompts`, `validBrowsingPrompts.length`
- XPCOM: `Services.prefs`

## generateConversationStartersSidebar()
- 位置: async L324-428
- 役割: 現在タブと開いているタブを整形してプロンプトに入れ、必要なら記憶を足して、モデルの応答から候補 n 件を返す。失敗やキャンセル時は空配列。
- 触るとき: サイドバーの会話開始候補の内容や入力データを変えるとき、またはキャンセル時の振る舞いを調べるとき。
- 呼び出し先: `Promise.all()`, `Promise.race()`, `String()`, `cleanInferenceOutput()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `formatJson()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `new Date().toISOString()`, `new Date().toISOString().slice()`, `openAIEngine.getFxAccountToken()`, `prompts.slice()`, `prompts.slice(0, n).map()`, `sanitizeUntrustedContent()`, `signal.throwIfAborted()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `formatJson()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `contextTabs.slice(1).map()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `contextTabs.slice()`
- 条件付き依存: `if (contextTabs.length >= 1)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if (useMemories)` → `lazy.loadPrompt()`
- 条件付き依存: `if (useMemories)` → `addMemoriesToPrompt()`
- 条件付き依存: `if (signal.aborted)` → `reject()`
- 条件付き依存: `if (!(signal.aborted))` → `signal.addEventListener()`
- 条件付き依存: `if (!(signal.aborted))` → `reject()`
- 条件付き依存: `if (e.name !== "AbortError")` → `lazy.console.warn()`
- 参照: `Services.locale.appLocaleAsBCP47`, `contextTabs.length`, `contextTabs[0].title`, `contextTabs[0].url`, `e.name`, `lazy.MODEL_FEATURES.CONVERSATION_STARTERS_SIDEBAR_SYSTEM`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_ASSISTANT_LIMITATIONS`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_MEMORIES`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_SIDEBAR_STARTER`, `new AbortController().signal`, `signal.aborted`, `signal.reason`, `t.title`, `t.url`
- XPCOM: `Services.locale`

## generateFollowupPrompts()
- 位置: async L440-504
- 役割: 直近の会話と現在タブをプロンプトに入れ、システム指示を 1 行 1 候補の形に固定して候補 n 件を返す。失敗時は空配列。
- 触るとき: 回答後に出るフォローアップ候補の入力や件数を変えるとき。
- 呼び出し先: `Object.keys()`, `Promise.all()`, `String()`, `cleanInferenceOutput()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `formatJson()`, `lazy.buildConversation()`, `lazy.console.warn()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `new Date().toISOString()`, `new Date().toISOString().slice()`, `openAIEngine.getFxAccountToken()`, `prompts.slice()`, `prompts.slice(0, n).map()`, `sanitizeUntrustedContent()`, `trimConversation()`
- 条件付き依存: `if (useMemories)` → `lazy.loadPrompt()`
- 条件付き依存: `if (useMemories)` → `addMemoriesToPrompt()`
- 参照: `Object.keys(currentTab).length`, `currentTab.title`, `currentTab.url`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_ASSISTANT_LIMITATIONS`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_FOLLOWUP`, `lazy.MODEL_FEATURES.CONVERSATION_SUGGESTIONS_MEMORIES`

## getMemorySummariesForPrompt()
- 位置: async L514-536
- 役割: 全記憶から空でない要約を大文字小文字を無視して重複除去し、最大件数まで集めて返す。
- 触るとき: プロンプトに入れる記憶要約の選び方(重複や件数)を変えるとき。
- 呼び出し先: `MemoriesManager.getAllMemories()`, `String()`, `String(memory_summary ?? "").trim()`, `memorySummaries.push()`, `seenSummaries.add()`, `seenSummaries.has()`, `summaryText.toLowerCase()`
- 参照: `memorySummaries.length`

## getMemoriesForResumeActivityConversationStarter()
- 位置: async L547-579
- 役割: 非機密の記憶のうち履歴 ID を持つものを、作成日とマージ日の新しい順に count 件まで返す。
- 触るとき: 「前回の続き」の候補にどの記憶を使うかを変えるとき。
- 呼び出し先: `Array.isArray()`, `MemoriesManager.getMemoriesByAttribute()`, `memories.filter()`, `memories.slice()`, `memories.sort()`
- 参照: `a.created_at`, `a.last_merged`, `b.created_at`, `b.last_merged`, `lazy.MEMORY_FILTER_COMPARATOR.EQUAL_TO`, `lazy.MEMORY_SENSITIVITY_CATEGORY_NOT_SENSITIVE`, `memory?.source_ids`, `sourceIds.history_source_ids`, `sourceIds.history_source_ids.length`

## attachUrlsToMemory()
- 位置: L590-600
- 役割: 記憶の履歴 ID を URL 情報に解決し、解決できないものを除いて最終訪問が新しい順に上限件数まで付ける。
- 触るとき: 前回の続きカードに出すページ一覧の数や並びを変えるとき。
- 呼び出し先: `lazy .getHistorySourceIdsFromMemory()`, `lazy .getHistorySourceIdsFromMemory(memory) .map()`, `lazy .getHistorySourceIdsFromMemory(memory) .map(urlHash => urlsByHash.get(urlHash)) .filter()`, `lazy .getHistorySourceIdsFromMemory(memory) .map(urlHash => urlsByHash.get(urlHash)) .filter(Boolean) .sort()`, `urlsByHash.get()`
- 参照: `a.lastVisitDate`, `b.lastVisitDate`

## formatChatsForResumeActivityPrompt()
- 位置: async L608-645
- 役割: 記憶に紐づく過去チャットを取得し、system と tool を除いた末尾数件を役割付きの文字列に整えて、会話 ID ごとの Map にする。長い本文は切り詰める。
- 触るとき: 前回の続き候補のプロンプトに過去チャットをどこまで入れるかを変えるとき。
- 呼び出し先: `[MESSAGE_ROLE.SYSTEM, MESSAGE_ROLE.TOOL].includes()`, `chatsById.set()`, `conversation.messages .filter()`, `conversation.messages .filter( message => ![MESSAGE_ROLE.SYSTEM, MESSAGE_ROLE.TOOL].includes(message.role) ) .slice()`, `lazy.getConversationSourceIdsFromMemory()`, `lazy.getConversationsById()`, `memories.flatMap()`
- 条件付き依存: `if ( bodyOrContent && bodyOrContent.length > lazy.MESSAGE_LENGTH_THRESHOLD )` → `bodyOrContent.substring()`
- 参照: `MESSAGE_ROLE.SYSTEM`, `MESSAGE_ROLE.TOOL`, `bodyOrContent.length`, `conversation.id`, `lazy.MESSAGE_LENGTH_THRESHOLD`, `lazy.ROLE_LABEL`, `message.content`, `message.content?.body`, `message.role`

## buildMemoryInputBlock()
- 位置: L656-689
- 役割: 記憶 1 件分の要約・頻度・理由・ページ・過去チャットを、プロンプト用のテキストブロックにまとめる。index があれば id 行を付ける。
- 触るとき: モデルへ渡す記憶データの項目や書式を変えるとき。
- 呼び出し先: `Number.isInteger()`, `chatsById.get()`, `formattedMessagesForResumeActivity .split()`, `formattedMessagesForResumeActivity .split("\n") .map()`, `formattedMessagesForResumeActivity .split("\n") .map(line => ` ${line}`) .join()`, `lazy .getConversationSourceIdsFromMemory()`, `lazy .getConversationSourceIdsFromMemory(memory) .map()`, `lazy .getConversationSourceIdsFromMemory(memory) .map(conversationId => chatsById.get(conversationId)) .filter()`, `sanitizeUntrustedContent()`, `urls .map()`, `urls .map(url => ` - ${sanitizeUntrustedContent(url.title)}`) .join()`
- 条件付き依存: `if (chats.length)` → `chats.join()`
- 参照: `a.updatedDate`, `b.updatedDate`, `chats.length`, `memory.frecency`, `memory.memory_summary`, `memory.reasoning`, `url.title`

## _getCachedResumeActivity()
- 位置: L698-704
- 役割: ウォーターマークに対応するキャッシュ済み結果、または実行中の Promise を返す。無ければ undefined。
- 触るとき: 前回の続きのキャッシュ戦略(キーの決め方)を変えるとき。
- 呼び出し先: `_resumeActivityCache.get()`
- 参照: `entry.inFlight`, `entry.result`

## filterDeletedMemoriesFromResumeActivity()
- 位置: async L712-722
- 役割: キャッシュ結果から、現在削除されていない記憶に対応するものだけを残す。
- 触るとき: 削除した記憶の候補がキャッシュ経由で残るときに確認する。
- 呼び出し先: `(await MemoriesManager.getAllMemories({ includeSoftDeleted: false })).map()`, `MemoriesManager.getAllMemories()`, `currentMemoryIds.has()`, `result.filter()`
- 参照: `filteredResult.length`, `memory.id`, `result.length`

## generateUncachedResumeActivityConversationStarters()
- 位置: async L727-822
- 役割: 記憶と閲覧履歴を集めて前回の続き用プロンプトを組み、セキュリティ属性を立ててから推論し、見出しと状態つきのカード配列を返す。失敗時は空配列。
- 触るとき: 前回の続き候補の生成手順(記憶選択、URL 解決、プロンプト組み立て、結果の整形)を変えるとき。
- 呼び出し先: `(card?.headline || "").replace()`, `(card?.status || "").replace()`, `Promise.all()`, `attachUrlsToMemory()`, `buildMemoryInputBlock()`, `cardsById.get()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.securityProperties.commit()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `conversation.setSystemMessage()`, `formatChatsForResumeActivityPrompt()`, `getMemoriesForResumeActivityConversationStarter()`, `lazy.buildConversation()`, `lazy.console.warn()`, `lazy.indexInferenceResultsById()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`, `lazy.resolveUrlsForMemories()`, `memoriesWithPlaceHashes .map()`, `memoriesWithPlaceHashes .map(memory => attachUrlsToMemory(memory, urlsByHash, MAX_NUM_URLS_PER_MEMORY) ) .filter()`, `memoriesWithUrlsAndTitles.map()`, `memoryInput.join()`, `openAIEngine.getFxAccountToken()`, `result.filter()`, `unpackJsonArrayOutput()`, `urls.map()`
- 参照: `card?.headline`, `card?.status`, `lazy.MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION_STARTER`, `m.memory`, `memoriesWithPlaceHashes.length`, `memoriesWithUrlsAndTitles.length`, `memoryInput.length`, `s.urls.length`

## isResumeActivityLocaleSupported()
- 位置: L824-829
- 役割: アプリのロケールが対応リスト(現在は en)に含まれるかを判定する。
- 触るとき: 前回の続きを対応する言語を増やすとき。
- 呼び出し先: `RESUME_ACTIVITY_SUPPORTED_LOCALES.some()`, `Services.locale.appLocaleAsBCP47.toLowerCase()`, `appLocale.startsWith()`
- XPCOM: `Services.locale`

## generateResumeActivityConversationStarters()
- 位置: async L840-862
- 役割: 対応ロケールなら、記憶のウォーターマークでキャッシュを引き、無ければ生成して結果を 1 件だけキャッシュする。
- 触るとき: 前回の続き候補の再生成条件やキャッシュの持ち方を変えるとき、または古い候補が出続けるとき。
- 呼び出し先: `MemoriesManager.getLastSessionMemoryTimestamp()`, `_getCachedResumeActivity()`, `_resumeActivityCache.clear()`, `_resumeActivityCache.get()`, `_resumeActivityCache.set()`, `generateUncachedResumeActivityConversationStarters()`, `isResumeActivityLocaleSupported()`
- 条件付き依存: `if (cached !== undefined)` → `filterDeletedMemoriesFromResumeActivity()`
- 条件付き依存: `if (_resumeActivityCache.get(watermark) === entry)` → `_resumeActivityCache.set()`

## constructConversationToResumeActivity()
- 位置: async L880-977
- 役割: 選ばれた候補から ChatConversation を作り、システム指示と記憶入りのユーザーメッセージを設定して、個人データと未信頼入力のフラグを立てて返す。
- 触るとき: 候補のクリックで開く会話の初期内容やセキュリティフラグを変えるとき。
- 呼び出し先: `Array.isArray()`, `Array.of()`, `Promise.all()`, `[chatSystemPrompt, resumeActivitySystemPrompt].join()`, `buildMemoryInputBlock()`, `conversation.addUserMessage()`, `conversation.securityProperties.commit()`, `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `conversation.setSystemMessage()`, `formatChatsForResumeActivityPrompt()`, `lazy.loadPrompt()`, `lazy.renderPrompt()`
- 条件付き依存: `if ( !resumeActivitySuggestion || !resumeActivitySuggestion.memory || !resumeActivitySuggestion.content )` → `lazy.console.warn()`
- 条件付き依存: `if ( !content.headline || !content.status || !content.previewTabs || !Array.isArray(content.previewTabs) || content.previewTabs.length === 0 )` → `lazy.console.warn()`
- 参照: `content.headline`, `content.previewTabs`, `content.previewTabs.length`, `content.status`, `conversation.engine?.model`, `conversation.promptEmbeddedMemories`, `lazy.ChatConversation`, `lazy.MODEL_FEATURES.CHAT`, `lazy.MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION`, `lazy.SYSTEM_PROMPT_TYPE.TEXT`, `resumeActivitySuggestion.content`, `resumeActivitySuggestion.content.headline`, `resumeActivitySuggestion.content.previewTabs`, `resumeActivitySuggestion.content.status`, `resumeActivitySuggestion.memory`, `resumeActivitySuggestion.memory.id`, `resumeActivitySuggestion.memory.memory_summary`, `userMessage.content.relevantMemories`
