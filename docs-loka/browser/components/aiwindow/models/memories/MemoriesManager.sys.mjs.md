# browser/components/aiwindow/models/memories/MemoriesManager.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesManager.sys.mjs
source-hash: 7965e44ff13e5c5700749a50f3f92a2b5001b4d9
lines: 860

## <module>
- 役割: 記憶機能の窓口となるMemoriesManagerクラスを定義する。記憶の生成と統合、保守、保存と削除、利用の記録、設定による有効判定をまとめる。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## takeMostRecentSessions()
- 位置: L98-107
- 役割: セッション数の上限を超えたら、終了時刻の新しい順に上限件数を取り、古い順に並べ直して返す。
- 触るとき: 1回の生成で処理するセッションの件数上限を変えるとき、どのセッションが切り捨てられるか調べるとき。
- 呼び出し先: `sessions .slice()`, `sessions .slice() .sort()`, `sessions .slice() .sort((a, b) => b.session_end_ms - a.session_end_ms) .slice()`, `sessions .slice() .sort((a, b) => b.session_end_ms - a.session_end_ms) .slice(0, maxSessions) .reverse()`
- 参照: `a.session_end_ms`, `b.session_end_ms`, `sessions.length`

## MemoriesManager.ensureConversationForGeneration()
- 位置: async L131-156
- 役割: 生成用の会話を返す。まだ無い、または準備できていなければ作り直す。
- 触るとき: 記憶生成で使う会話インスタンスの作られ方や再利用の条件を変えるとき。
- 呼び出し先: `buildFresh()`
- 条件付き依存: `if (!this.#generationConversationPromise)` → `buildFresh()`
- 条件付き依存: `if (!conversation?.isReady)` → `buildFresh()`
- 参照: `conversation?.isReady`, `this.#generationConversationPromise`

## buildFresh()
- 位置: async L132-137
- 役割: 生成用の会話を新しく作り、キャッシュに入れる。
- 触るとき: 生成用会話の初期化の内容を変えるとき。
- 呼び出し先: `buildConversation()`
- 参照: `MODEL_FEATURES.MEMORIES_INITIAL_GENERATION_SYSTEM`, `this.#generationConversationPromise`

## MemoriesManager.ensureConversationForUsage()
- 位置: async L164-189
- 役割: 利用(分類や関連記憶の取得)用の会話を返す。まだ無い、または準備できていなければ作り直す。
- 触るとき: 記憶の分類に使う会話の再利用条件を変えるとき。
- 呼び出し先: `buildFresh()`
- 条件付き依存: `if (!this.#usageConversationPromise)` → `buildFresh()`
- 条件付き依存: `if (!conversation?.isReady)` → `buildFresh()`
- 参照: `conversation?.isReady`, `this.#usageConversationPromise`

## buildFresh()
- 位置: async L165-170
- 役割: 利用用の会話を新しく作り、キャッシュに入れる。
- 触るとき: 利用用会話の初期化の内容を変えるとき。
- 呼び出し先: `buildConversation()`
- 参照: `MODEL_FEATURES.MEMORIES_MESSAGE_CLASSIFICATION_SYSTEM`, `this.#usageConversationPromise`

## MemoriesManager.runMemoryMaintenance()
- 位置: async L205-264
- 役割: 論理削除された記憶を物理削除し、残りのうち1日以上更新されていないものについて利用の窓を進め、強度と種類を更新する。忘却の閾値を下回るものは物理削除する。
- 触るとき: 記憶が勝手に消える、または溜まり続けるとき。1日ごとの保守の仕組みを変えるとき。
- 呼び出し先: `Date.now()`, `Math.floor()`, `MemoryStore.getMemories()`, `MemoryStore.hardDeleteMemory()`, `allMemories.filter()`, `classifyMemoryAndCapStrength()`, `computeMemoryFrecency()`, `computeMemoryStrength()`, `isShouldDeleteMemoryDueToDecay()`
- 条件付き依存: `if (isShouldDeleteMemoryDueToDecay(memory))` → `MemoryStore.hardDeleteMemory()`
- 条件付き依存: `if (changed)` → `MemoryStore.requestSave()`
- 参照: `mem.is_deleted`, `memory.frecency`, `memory.id`, `memory.is_deleted`, `memory.recent_accessed_counts`, `memory.strength`, `memory.updated_at`

## MemoriesManager.generateMemoriesFromSessions()
- 位置: async L289-395
- 役割: 履歴と会話を有効なものだけ取り、セッションを作って判定し上限件数に絞り、パイプラインで記憶を生成して保存する。成功した時刻まで記録を進め、再試行可能なエラーは呼び出し元へ投げる。
- 触るとき: 記憶生成が動かない、または同じ閲覧が何度も処理されると調べるとき。生成の上限やウォーターマークの進め方を変えるとき。
- 呼び出し先: `buildSessions()`, `console.error()`, `openAIEngine.isRetryableError()`, `runHeuristicGate()`, `runSessionMemoryPipeline()`, `sessions.filter()`, `takeMostRecentSessions()`, `this.ensureConversationForGeneration()`, `this.getLastSessionMemoryTimestamp()`, `this.getSessionMemoryDeltaStartMs()`, `this.saveMemories()`, `this.shouldEnableMemoriesFromSchedulers()`
- 条件付き依存: `if (historyEnabled)` → `this._getRecentHistory()`
- 条件付き依存: `if (conversationEnabled)` → `this._getRecentChats()`
- 条件付き依存: `if (retainedSessions.length < gatedSessions.length)` → `lazy.console.debug()`
- 条件付き依存: `if (!retainedSessions.length)` → `sessions.reduce()`
- 条件付き依存: `if (!retainedSessions.length)` → `Math.max()`
- 条件付き依存: `if (maxSessionEndMs > watermarkMs)` → `this.setLastSessionMemoryTimestamp()`
- 条件付き依存: `if (!retainedSessions.length)` → `lazy.console.debug()`
- 条件付き依存: `if (result.processedThroughMs > 0)` → `this.setLastSessionMemoryTimestamp()`
- 条件付き依存: `if (result.processedThroughMs > 0)` → `Math.max()`
- 参照: `gatedSessions.length`, `result.memories`, `result.processedThroughMs`, `retainedSessions.length`, `runHeuristicGate(session).decision`, `session.session_end_ms`

## MemoriesManager.mergeMemories()
- 位置: async L408-450
- 役割: プロファイル事実を除く記憶が閾値件数を超えたら、LLMに統合候補を作らせ、新しい記憶を保存して構成要素の記憶を物理削除する。
- 触るとき: 記憶の統合が起きない、または統合で元の記憶が消えすぎると調べるとき。統合の最小件数を変えるとき。
- 呼び出し先: `MemoryStore.addMemory()`, `MemoryStore.getMemories()`, `allMemories.filter()`, `createMergedMemories()`, `getMergeMemoryCandidates()`, `mergedMemoryIds.add()`, `mergedMemoryIds.has()`, `this.ensureConversationForGeneration()`, `this.hardDeleteMemoryById()`
- 参照: `memory.type`, `mergeableMemories.length`, `saved.id`

## MemoriesManager.getAllMemories()
- 位置: async L462-464
- 役割: MemoryStoreから記憶の一覧を、論理削除を含めるかどうかの指定付きで取得する。
- 触るとき: 記憶の一覧を取る呼び出しの既定値を変えるとき。
- 呼び出し先: `MemoryStore.getMemories()`

## MemoriesManager.getMemoriesByID()
- 位置: async L473-475
- 役割: 記憶のIDの集合を指定して、MemoryStoreから該当する記憶を取り出す。
- 触るとき: IDで記憶を引く経路の戻り値の形を確かめるとき。
- 呼び出し先: `MemoryStore.getMemories()`

## MemoriesManager.resolveUsedMemories()
- 位置: async L490-514
- 役割: 使われた記憶のIDから記憶を取り出し、累計利用数と当日の利用数を1増やし、最終利用時刻を今にして保存する。
- 触るとき: 会話で記憶が使われた回数が合わないとき、利用の記録の仕方を変えるとき。
- 呼び出し先: `(await this.getAllMemories()).filter()`, `Date.now()`, `MemoryStore.requestSave()`, `ids.has()`, `this.getAllMemories()`
- 参照: `ids.size`, `memory.id`, `memory.last_accessed`, `memory.lifetime_accessed_count`, `memory.recent_accessed_counts`, `used.length`

## MemoriesManager.getMemoriesByAttribute()
- 位置: async L525-527
- 役割: 属性の条件(項目、値、比較方法)を渡してMemoryStoreで記憶を絞り込む。
- 触るとき: カテゴリや意図などの属性で記憶を探す処理を変えるとき。
- 呼び出し先: `MemoryStore.getMemories()`

## MemoriesManager.getLastSessionMemoryTimestamp()
- 位置: async L540-550
- 役割: 統合された処理済みの時刻を読む。無ければ旧式の履歴と会話それぞれの時刻の古い方を使い、どちらも無ければ0を返す。
- 触るとき: 記憶生成の差分の起点が想定より古い、または新しいと感じるとき。旧形式からの移行の挙動を確かめるとき。
- 呼び出し先: `Math.min()`, `MemoryStore.getMeta()`, `[ meta.last_history_memory_ts, meta.last_chat_memory_ts, ].filter()`
- 参照: `legacy.length`, `meta.last_chat_memory_ts`, `meta.last_history_memory_ts`, `meta.last_session_memory_ts`

## MemoriesManager.getSessionMemoryDeltaStartMs()
- 位置: L560-562
- 役割: 処理済みの時刻に1ミリ秒を足して差分読み取りの開始時刻にする。初回は0を返す。
- 触るとき: 差分読み取りの境界で同じ閲覧が二重に処理される、または抜けると調べるとき。

## MemoriesManager.setLastSessionMemoryTimestamp()
- 位置: async L570-572
- 役割: 統合された処理済みの時刻をMemoryStoreのメタ情報に保存する。
- 触るとき: 処理済みの時刻がどこで進むかを追うとき。
- 呼び出し先: `MemoryStore.updateMeta()`

## MemoriesManager.getLastGenerationRunTimestamp()
- 位置: async L582-585
- 役割: 最後に生成を実行した時刻を読む。無ければ統合された処理済みの時刻、それも無ければ0を返す。
- 触るとき: スケジューラーの実行間隔の判定が想定と違うとき、旧データからの移行の挙動を確かめるとき。
- 呼び出し先: `MemoryStore.getMeta()`
- 参照: `meta.last_generation_run_ts`, `meta.last_session_memory_ts`

## MemoriesManager.setLastGenerationRunTimestamp()
- 位置: async L593-595
- 役割: 最後に生成を実行した時刻をMemoryStoreのメタ情報に保存する。
- 触るとき: 生成の実行時刻の記録のされ方を変えるとき。
- 呼び出し先: `MemoryStore.updateMeta()`

## MemoriesManager.saveMemories()
- 位置: async L607-618
- 役割: 生成された記憶の配列を1件ずつMemoryStoreに追加し、保存後の記憶の一覧を返す。配列でなければ何もしない。
- 触るとき: 生成された記憶が保存されない、または重複して保存されると調べるとき。
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if (Array.isArray(generatedMemories))` → `MemoryStore.addMemory()`
- 条件付き依存: `if (Array.isArray(generatedMemories))` → `persistedMemories.push()`

## MemoriesManager.saveRequestedMemory()
- 位置: async L629-666
- 役割: ユーザーの依頼による記憶を作る。空の要約を拒否し、要約を100字で切ったうえで、要約と直前の発話に個人情報が無いか確かめてから追加する。
- 触るとき: 依頼で記憶が作られない、または個人情報の判定で断られる理由を調べるとき。依頼の記憶の扱いを変えるとき。
- 呼び出し先: `ChatStore.getMostRecentMessages()`, `MemoryStore.addMemory()`, `_sensitiveInfoDetector.containsSensitiveInfo()`, `memorySummary.trim()`, `memorySummary.trim().slice()`
- 参照: `MESSAGE_ROLE.USER`, `recentUserMessages[0]?.content?.body`

## MemoriesManager.enrichExistingMemory()
- 位置: async L675-687
- 役割: 記憶の要約を分類し、最初のカテゴリと意図をタグにして既存の記憶を更新する。
- 触るとき: 記憶に付くカテゴリや意図のタグが欠けるとき。分類の後処理を変えるとき。
- 呼び出し先: `MemoryStore.updateMemory()`, `this.memoryClassifyMessage()`
- 条件付き依存: `if (categories[0])` → `tags.push()`
- 条件付き依存: `if (intents[0])` → `tags.push()`

## MemoriesManager.softDeleteMemoryById()
- 位置: async L699-701
- 役割: MemoryStoreで指定の記憶を論理削除する。物理的には残り、既定の取得では返らなくなる。
- 触るとき: 記憶を一旦消して取り消せるようにする挙動を変えるとき。
- 呼び出し先: `MemoryStore.softDeleteMemory()`

## MemoriesManager.hardDeleteMemoryById()
- 位置: async L713-715
- 役割: MemoryStoreで指定の記憶を物理削除する。削除の契機と、会話で使われている数を渡せる。
- 触るとき: 記憶の削除がUIや会話から呼ばれる経路を追うとき、削除の記録の項目を変えるとき。
- 呼び出し先: `MemoryStore.hardDeleteMemory()`

## MemoriesManager.memoryClassifyMessage()
- 位置: async L723-753
- 役割: 利用用の会話を使い、文を分類プロンプトに入れてLLMに送り、カテゴリと意図を受け取る。形が不正なら空の一覧を返す。
- 触るとき: 記憶の分類結果が空になる、または誤るとき。分類のプロンプトや出力の形を変えるとき。
- 呼び出し先: `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `getFormattedMemoryAttributeList()`, `loadPrompt()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `this.ensureConversationForUsage()`
- 参照: `MODEL_FEATURES.MEMORIES_MESSAGE_CLASSIFICATION_SYSTEM`, `MODEL_FEATURES.MEMORIES_MESSAGE_CLASSIFICATION_USER`, `parsed.categories`, `parsed.intents`

## MemoriesManager._clearEmbeddingsCache()
- 位置: L760-762
- 役割: MemoryStoreの埋め込みキャッシュを消す。テスト用。
- 触るとき: 埋め込みの単体テストを書くとき、キャッシュの状態をリセットしたいとき。
- 呼び出し先: `MemoryStore._clearEmbeddingsCache()`

## MemoriesManager.getRelevantMemories()
- 位置: async L774-784
- 役割: メッセージに関連する記憶を、件数と類似度の下限の指定付きでMemoryStoreから取り出す。
- 触るとき: 会話に関連記憶を差し込む件数や類似度の閾値を変えるとき。
- 呼び出し先: `MemoryStore.getRelevantMemories()`

## MemoriesManager.shouldEnableMemoriesFromSchedulers()
- 位置: L802-847
- 役割: AIウィンドウの有効、対象の設定、利用規約の同意、初回実行の完了を確かめ、さらに有効なAIウィンドウが開いていればtrueを返す。例外時はfalseにする。
- 触るとき: 記憶生成が動かない理由を調べるとき、有効条件を変えるとき。
- 呼び出し先: `AIWindow.isAIWindowActive()`, `AIWindow.isAIWindowEnabled()`, `EveryWindow.readyWindows.some()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (source === SOURCE_HISTORY)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (source === SOURCE_CONVERSATION)` → `Services.prefs.getBoolPref()`
- 参照: `AIWindowAccountAuth.hasToSConsent`
- XPCOM: `Services.prefs`

## MemoriesManager.countRecentVisits()
- 位置: async L856-858
- 役割: MemoriesHistorySourceのcountRecentVisitsに委譲し、過去の閲覧件数を返す。
- 触るとき: 閲覧件数による判定の入口を追うとき。
- 呼び出し先: `countRecentVisits()`
