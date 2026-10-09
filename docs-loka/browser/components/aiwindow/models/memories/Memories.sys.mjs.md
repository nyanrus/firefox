# browser/components/aiwindow/models/memories/Memories.sys.mjs

source: browser/components/aiwindow/models/memories/Memories.sys.mjs
source-hash: f658af0ec5e46ea7e26da9471d537d4c5fc4cad3
lines: 922

## <module>
- 役割: セッション束から記憶を生成し、品質と機微性でフィルタし、類似した記憶を統合するまでのパイプラインと、強度・種類・忘却・頻度の計算をまとめる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## runSessionMemoryPipeline()
- 位置: async L106-187
- 役割: セッションを10件ずつLLMに渡して候補記憶を集め、全体で品質と機微性のフィルタを1回かけ、残った要約を候補に戻す。処理済みの時刻も返す。
- 触るとき: 記憶生成が途中で止まる、または再試行されるとき。429などの一時エラーの扱いや、処理済み時刻の進め方を変えるときに見る。
- 呼び出し先: `Math.max()`, `applyQualityAndSensitivityFilter()`, `batch.reduce()`, `candidateMemories.map()`, `candidateMemories.push()`, `console.error()`, `generateInitialMemoriesList()`, `mapFilteredMemoriesToInitialList()`, `openAIEngine.isRetryableError()`, `sessions.slice()`
- 条件付き依存: `if (openAIEngine.isRetryableError(e))` → `lazy.setTimeout()`
- 参照: `candidateMemories.length`, `filteredSummaries.length`, `memory.memory_summary`, `session.session_end_ms`, `sessions.length`

## computeMemoryStrength()
- 位置: L214-249
- 役割: 基礎値に、ユーザー要求の加点、根拠数(上限付き)、最終アクセスと統合からの経過で減衰する項を足して、強度を0.01刻みで求める。
- 触るとき: 記憶が強くなりすぎる、または弱すぎると感じるとき。係数や半減期を変えるとき、作成日へのフォールバックを確認するとき。
- 呼び出し先: `Date.now()`, `Math.min()`, `Math.round()`, `Math.sqrt()`, `Object.values()`, `Object.values(memory.source_ids).reduce()`, `daysSince()`, `memory.sources.includes()`
- 参照: `memory.created_at`, `memory.last_accessed`, `memory.last_merged`, `memory.lifetime_accessed_count`, `memory.merge_count`, `memory.source_ids`, `sourceIds.length`

## daysSince()
- 位置: L228-228
- 役割: タイムスタンプから現在までの経過日数を求める。
- 触るとき: 強度や忘却の計算で経過日数の基準を変えるとき。

## classifyMemoryAndCapStrength()
- 位置: L265-279
- 役割: 作成からの日数と強度を段階表の上から順に照らし、条件を満たす最も強い種類を設定する。若すぎる記憶は段階の下限まで強度を抑える。
- 触るとき: 短期から長期、長期から永続への昇格条件を変えるとき、昇格されない理由を調べるとき。
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (daysSinceCreated < minAgeDays)` → `Math.min()`
- 参照: `memory.created_at`, `memory.strength`, `memory.type`

## isShouldDeleteMemoryDueToDecay()
- 位置: L298-311
- 役割: 最終アクセス(無ければ作成日)からの日数と強度で保持率exp(-t/s)を求め、閾値以下なら削除対象としてtrueを返す。
- 触るとき: 忘却で記憶が消えすぎる、または残りすぎると調べるとき。閾値を変えるとき。
- 呼び出し先: `Date.now()`, `Math.exp()`
- 参照: `memory.created_at`, `memory.last_accessed`, `memory.strength`

## computeMemoryFrecency()
- 位置: L319-329
- 役割: 直近7日の利用回数に日ごとの半減期の重みを掛けて合計し、頻度スコアを返す。
- 触るとき: 記憶の頻度スコアの値を確かめるとき、重みの減衰を変えるとき。
- 呼び出し先: `Math.pow()`
- 参照: `memory.recent_accessed_counts`

## formatListForPrompt()
- 位置: L337-339
- 役割: 文字列の配列をダブルクォートで囲んだ箇条書きの文字列にする。
- 触るとき: プロンプトに一覧を埋め込む書式を変えるとき。
- 呼び出し先: `list.map()`, `list.map(item => `- "${item}"`).join()`

## getFormattedMemoryAttributeList()
- 位置: L347-354
- 役割: カテゴリかインテントの名前を受け取り、対応する一覧を箇条書きにして返す。それ以外の名前は例外にする。
- 触るとき: プロンプトに載るカテゴリや意図の一覧を追加・変更するとき。
- 条件付き依存: `if (attributeName === CATEGORIES)` → `formatListForPrompt()`
- 条件付き依存: `if (attributeName === INTENTS)` → `formatListForPrompt()`

## renderSessionsForPrompt()
- 位置: L365-403
- 役割: セッションごとに日付の見出しを付け、検索語・タイトル・空でないチャット本文を節に分けてプロンプト用の文字列にする。ソースIDは含めない。
- 触るとき: LLMに渡る材料の見え方を変えるとき。ソースIDを送らない設計を保つか確かめるとき。
- 呼び出し先: `blocks.join()`, `blocks.join("\n\n").trim()`, `blocks.push()`, `lines.join()`, `lines.push()`, `new Date(session.session_start_ms).toISOString()`, `new Date(session.session_start_ms).toISOString().slice()`, `sessions.forEach()`
- 条件付き依存: `if (session.search_queries.length)` → `lines.push()`
- 条件付き依存: `if (session.titles.length)` → `lines.push()`
- 条件付き依存: `if (session.chats.length)` → `message.content.trim()`
- 条件付き依存: `if (content)` → `chatLines.push()`
- 条件付き依存: `if (chatLines.length)` → `lines.push()`
- 参照: `chatLines.length`, `message.content`, `session.chats`, `session.chats.length`, `session.search_queries`, `session.search_queries.length`, `session.session_start_ms`, `session.titles`, `session.titles.length`

## sanitizeMemory()
- 位置: L416-462
- 役割: LLM出力の1件を検査し、要約が100字を超えるか必須の文字列項目が欠けると棄却する。スコアは1から5に丸め、根拠からsourceを決める。
- 触るとき: LLMの出力から記憶が落ちる理由を調べるとき、必須項目やスコアの範囲を変えるとき。
- 呼び出し先: `Array.isArray()`, `Math.round()`, `Number.isFinite()`, `deriveSource()`
- 条件付き依存: `if ( memory.memory_summary && memory.memory_summary.length > MAX_MEMORY_SUMMARY_LENGTH )` → `console.warn()`
- 参照: `memory.category`, `memory.entities`, `memory.evidence`, `memory.intent`, `memory.memory_summary`, `memory.memory_summary.length`, `memory.reasoning`, `memory.score`

## deriveSource()
- 位置: L473-494
- 役割: 根拠の種類(title、search、chat、user)の組み合わせから、出典を履歴、会話、ユーザー、セッションのいずれかにする。
- 触るとき: 記憶の出典タグが想定と違うとき、出典の優先順位を変えるとき。
- 呼び出し先: `Array.isArray()`, `evidence.map()`, `types.has()`
- 参照: `e?.type`, `evidence.length`

## attributeSourceIds()
- 位置: L509-538
- 役割: 根拠の文字列が検索語かタイトルに含まれるセッションの履歴IDと、チャット本文に含まれるセッションの会話IDを、記憶のsource_idsに集める。
- 触るとき: 記憶から元の閲覧や会話をたどれないとき、紐付けが広がりすぎると調べるとき。
- 呼び出し先: `msg.content.includes()`, `session.chats?.some()`, `session.search_queries.includes()`, `session.titles.includes()`
- 条件付き依存: `if (inBrowse)` → `session.history_source_ids.forEach()`
- 条件付き依存: `if (inBrowse)` → `historyIds.add()`
- 条件付き依存: `if (inChat)` → `session.conversation_source_ids.forEach()`
- 条件付き依存: `if (inChat)` → `conversationIds.add()`
- 参照: `item.value`, `item?.value`, `msg.content`

## normalizeMemoryList()
- 位置: L551-571
- 役割: LLM出力が配列か、itemsを持つオブジェクトか、単独の記憶オブジェクトかを見て配列に揃え、sanitizeMemoryに通して有効な記憶だけ返す。
- 触るとき: LLMの出力形式のぶれに対してどこまで許すかを変えるとき。
- 呼び出し先: `Array.isArray()`, `list.map()`, `list.map(sanitizeMemory).filter()`
- 条件付き依存: `if (!Array.isArray(list))` → `Array.isArray()`
- 参照: `list.items`

## generateInitialMemoriesList()
- 位置: async L580-650
- 役割: セッションを埋め込んだプロンプトでLLMを1回呼び、出力から記憶オブジェクトを作る。種類・出典ID・強度・追跡用の初期値を設定する。
- 触るとき: 生成される記憶のフィールドや初期値を変えるとき。LLMに渡す入力を確かめるとき。
- 呼び出し先: `Array.from()`, `Date.now()`, `Object.fromEntries()`, `Promise.all()`, `attributeSourceIds()`, `classifyMemoryAndCapStrength()`, `computeMemoryStrength()`, `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `getFormattedMemoryAttributeList()`, `lazy.loadPrompt()`, `normalizeMemoryList()`, `normalizeMemoryList(parsed).map()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `sources.hasOwnProperty()`
- 条件付き依存: `if (sources.hasOwnProperty(SESSIONS))` → `renderSessionsForPrompt()`
- 参照: `MODEL_FEATURES.MEMORIES_INITIAL_GENERATION_SYSTEM`, `MODEL_FEATURES.MEMORIES_INITIAL_GENERATION_USER`, `m.strength`, `memory.category`, `memory.evidence`, `memory.intent`, `memory.keywords`, `memory.memory_summary`, `memory.reasoning`, `memory.source`

## applyQualityAndSensitivityFilter()
- 位置: async L660-697
- 役割: 候補の要約一覧をLLMに渡し、返された要約のうち入力に含まれるものだけを残す。LLMが言い換えた文は捨てる。
- 触るとき: 品質や機微性の判定で候補が落ちすぎる、または残りすぎるとき。プロンプトの判定基準を見直すとき。
- 呼び出し先: `Array.isArray()`, `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `formatListForPrompt()`, `inputSet.has()`, `lazy.loadPrompt()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `parsed.kept_memories.filter()`, `renderPrompt()`
- 参照: `MODEL_FEATURES.MEMORIES_QUALITY_AND_SENSITIVITY_FILTER_SYSTEM`, `MODEL_FEATURES.MEMORIES_QUALITY_AND_SENSITIVITY_FILTER_USER`, `parsed.kept_memories`

## mapFilteredMemoriesToInitialList()
- 位置: async L705-712
- 役割: 残った要約と一致する候補の記憶オブジェクトだけを残す。
- 触るとき: フィルタ後に記憶が消える原因を調べるとき。
- 呼び出し先: `filteredMemoriesList.includes()`, `initialMemories.filter()`
- 参照: `memory.memory_summary`

## getMergeMemoryCandidates()
- 位置: async L722-780
- 役割: 記憶の要約と理由をLLMに渡し、構成要素・新しい理由・新しい要約を持つ統合候補の配列を、JSONスキーマ付きで受け取る。
- 触るとき: 統合候補の質を変えるとき、統合の出力スキーマや要約の長さ上限を変えるとき。
- 呼び出し先: `Promise.all()`, `conversation.addUserMessage()`, `conversation.clearMessages()`, `conversation.run()`, `conversation.setSystemMessage()`, `lazy.loadPrompt()`, `makeJSONSchemaBlob()`, `memoriesForPrompt.join()`, `memoriesForPrompt.push()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`
- 参照: `conversation.engine?.model`, `lazy.MODEL_FEATURES.MEMORIES_MERGE`, `memoriesMergeSystemPrompt.prompt`, `memoriesMergeUserPrompt.prompt`, `memory.memory_summary`, `memory.reasoning`

## latestTimestamp()
- 位置: L790-793
- 役割: null以外のタイムスタンプの最大値を返す。全部nullならnullを返す。
- 触るとき: 統合後の最終アクセス時刻が0や不正な値になると調べるとき。
- 呼び出し先: `Math.max()`, `timestamps.filter()`
- 参照: `set.length`

## createMergedMemories()
- 位置: L804-921
- 役割: 統合候補を検査し、構成要素が2件以上そろう候補から統合記憶を作る。出典・ID・機微性を合わせ、強度と種類を再計算する。削除すべき元の記憶のIDも返す。
- 触るとき: 統合で元の記憶が消える、または統合結果が落ちる原因を調べるとき。統合時に引き継ぐフィールドを変えるとき。
- 呼び出し先: `Array.from()`, `Array.isArray()`, `Date.now()`, `Math.max()`, `Math.min()`, `Math.sumPrecise()`, `Object.fromEntries()`, `classifyMemoryAndCapStrength()`, `componentMemories.flatMap()`, `componentMemories.map()`, `componentMemories.reduce()`, `componentMemories.some()`, `componentMemoryIdsToDelete.add()`, `computeMemoryFrecency()`, `computeMemoryStrength()`, `finalMergedMemories.push()`, `latestTimestamp()`, `memories.filter()`, `mergedMemory.component_statements.includes()`
- 参照: `component.memory_summary`, `componentMemories.length`, `mem.component_summaries`, `mem.created_at`, `mem.id`, `mem.keywords`, `mem.last_accessed`, `mem.lifetime_accessed_count`, `mem.memory_summary`, `mem.merge_count`, `mem.reasoning`, `mem.recent_accessed_counts`, `mem.sensitivity_category`, `mem.source_ids?.conversation_source_ids`, `mem.source_ids?.history_source_ids`, `mem.sources`, `mem.tags`, `mem.updated_at`, `mergedMemory.component_statements`, `mergedMemory.new_reasoning`, `mergedMemory.new_reasoning.length`, `mergedMemory.new_statement`, `mergedMemory.new_statement.length`, `mergedMemoryToSave.frecency`, `mergedMemoryToSave.strength`
