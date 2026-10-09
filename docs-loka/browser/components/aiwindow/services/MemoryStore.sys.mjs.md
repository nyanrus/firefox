# browser/components/aiwindow/services/MemoryStore.sys.mjs

source: browser/components/aiwindow/services/MemoryStore.sys.mjs
source-hash: 89dc802d8341dae29ce514622ccbac94e652a10b
lines: 1083

## <module>
- 役割: 記憶と記憶のメタ情報をメモリ上に持ち、memories.json.lz4としてディスクに保存する記憶ストア。記憶の追加、更新、削除、類似検索、条件による取り出しを提供する。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `PathUtils.join()`, `Services.dirsvc.get()`, `console.createInstance()`

## normalizeSourceIds()
- 位置: L79-88
- 役割: 出典IDの入力を、重複を除いた history_source_ids と conversation_source_ids の配列に揃える。無ければ空配列にする。
- 触るとき: 出典IDが欠けたり重複したりしたときの扱いを変えるとき。
- 呼び出し先: `Array.isArray()`
- 参照: `raw.conversation_source_ids`, `raw.history_source_ids`, `raw?.conversation_source_ids`, `raw?.history_source_ids`

## unionSourceIds()
- 位置: L98-112
- 役割: 二つの出典ID束を両方の和集合にして返す。記憶を再生成したときに、出典を置き換えずに足すために使う。
- 触るとき: 記憶の出典が統合や更新で増えない、または消えると調べるとき。
- 呼び出し先: `normalizeSourceIds()`
- 参照: `an.conversation_source_ids`, `an.history_source_ids`, `bn.conversation_source_ids`, `bn.history_source_ids`

## isComponentSummaries()
- 位置: L120-131
- 役割: 値が、memory_summaryとreasoningの文字列を持つオブジェクトの配列かを判定する。
- 触るとき: 統合の構成要素の形を変えるとき、不正な構成要素が入る原因を調べるとき。
- 呼び出し先: `Array.isArray()`, `v.every()`
- 参照: `component.memory_summary`, `component.reasoning`

## migrateMemoryStoreVersionOneToTwo()
- 位置: L158-269
- 役割: 版1の記憶を版2の形に変える。種類、出典、感度、タグ(旧categoryとintentから作る)、キーワード、追跡項目を補い、旧scoreを消して頻度と強度を計算する。
- 触るとき: 保存形式の移行結果を確かめるとき、版2の項目の既定値を変えるとき。
- 呼び出し先: `Array.isArray()`, `computeMemoryFrecency()`, `computeMemoryStrength()`, `memories.map()`, `normalizeSourceIds()`
- 条件付き依存: `if (!m.tags)` → `m.hasOwnProperty()`
- 条件付き依存: `if (m.category)` → `m.tags.push()`
- 条件付き依存: `if (m.intent)` → `m.tags.push()`
- 条件付き依存: `if (!m.updated_at)` → `Date.now()`
- 条件付き依存: `if (!m.recent_accessed_counts)` → `Object.fromEntries()`
- 条件付き依存: `if (!m.recent_accessed_counts)` → `Array.from()`
- 参照: `m.category`, `m.component_summaries`, `m.created_at`, `m.entities`, `m.frecency`, `m.intent`, `m.is_deleted`, `m.keywords`, `m.last_accessed`, `m.reasoning`, `m.recent_accessed_counts`, `m.score`, `m.sensitivity_category`, `m.source`, `m.source_ids`, `m.source_ids.conversation_source_ids.length`, `m.source_ids.history_source_ids.length`, `m.sources`, `m.strength`, `m.tags`, `m.type`, `m.updated_at`

## loadMemories()
- 位置: async L276-368
- 役割: ディスクからJSONを読み、版2ならそのまま、版1なら移行してから状態に入れる。版が合わない場合は記憶を空にし、読めない場合は既定の状態で始める。
- 触るとき: 起動後に記憶が見えない、または移行で消えると調べるとき。
- 呼び出し先: `Services.profiler.IsActive()`, `console.error()`, `gJSONFile.load()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `IOUtils.stat()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `(stat.size / 1048576).toFixed()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `ChromeUtils.now()`
- 条件付き依存: `if (markerData)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (!(!data || typeof data !== "object"))` → `Array.isArray()`
- 条件付き依存: `if (!(data.version === MEMORY_STORE_VERSION && Array.isArray(data.memories)))` → `Array.isArray()`
- 条件付き依存: `if ( typeof data.version === "number" && data.version === 1 && Array.isArray(data.memories) )` → `migrateMemoryStoreVersionOneToTwo()`
- 条件付き依存: `if (!( typeof data.version === "number" && data.version === 1 && Array.isArray(data.memories) ))` → `lazy.console.warn()`
- 条件付き依存: `if (!(!data || typeof data !== "object"))` → `memories.map()`
- 条件付き依存: `if (isMemoriesMigrated)` → `gJSONFile?.saveSoon()`
- 条件付き依存: `if (isMemoriesMigrated)` → `Services.obs.notifyObservers()`
- 参照: `data.memories`, `data.meta?.last_chat_memory_ts`, `data.meta?.last_generation_run_ts`, `data.meta?.last_history_memory_ts`, `data.meta?.last_session_memory_ts`, `data.version`, `gJSONFile.data`, `lazy.gStorePath`, `markerData.sizeLabel`, `markerData.startTime`, `mem.merge_count`, `stat.size`
- XPCOM: `Services.obs` / `Services.profiler`

## ensureInitialized()
- 位置: async L385-395
- 役割: 初回だけloadMemoriesを呼び、完了を待つ。以後は即座に戻る。
- 触るとき: ストアの初期化が待てない、または二重に読み込むかを調べるとき。
- 条件付き依存: `if (!gInitPromise)` → `loadMemories()`

## requestSave()
- 位置: async L400-403
- 役割: 初期化を確かめたうえで、遅延付きの保存を予約する。
- 触るとき: 変更が保存されるタイミングを追うとき。
- 呼び出し先: `gJSONFile?.saveSoon()`, `this.ensureInitialized()`

## testOnlyFlush()
- 位置: async L410-416
- 役割: テスト向けに、今の状態を即座にディスクへ書く。
- 触るとき: 保存結果を確かめるテストを書くとき。呼び出しはソース内に見当たらない。
- 呼び出し先: `gJSONFile._save()`, `this.ensureInitialized()`

## addMemory()
- 位置: async L472-544
- 役割: IDが同じ記憶があれば更新し、無ければ既定値を埋めて新規に追加する。新規のときは保存を予約し、変更の通知と件数の指標を送る。
- 触るとき: 記憶が重複する、または既定値が想定と違うとき。新しい記憶の項目を足すとき。
- 呼び出し先: `Date.now()`, `makeMemoryId()`, `this.ensureInitialized()`, `this.updateMemory()`, `updateMemoriesCountMetric()`
- 条件付き依存: `if (!memory)` → `normalizeSourceIds()`
- 条件付き依存: `if (!memory)` → `Object.fromEntries()`
- 条件付き依存: `if (!memory)` → `Array.from()`
- 条件付き依存: `if (!memory)` → `gState.memories.push()`
- 条件付き依存: `if (!memory)` → `gJSONFile?.saveSoon()`
- 条件付き依存: `if (!memory)` → `Services.obs.notifyObservers()`
- 参照: `memoryPartial.component_summaries`, `memoryPartial.created_at`, `memoryPartial.frecency`, `memoryPartial.is_deleted`, `memoryPartial.keywords`, `memoryPartial.last_accessed`, `memoryPartial.last_merged`, `memoryPartial.lifetime_accessed_count`, `memoryPartial.memory_summary`, `memoryPartial.merge_count`, `memoryPartial.reasoning`, `memoryPartial.recent_accessed_counts`, `memoryPartial.sensitivity_category`, `memoryPartial.source_ids`, `memoryPartial.sources`, `memoryPartial.strength`, `memoryPartial.tags`, `memoryPartial.type`, `memoryPartial.updated_at`, `source_ids.conversation_source_ids.length`, `source_ids.history_source_ids.length`
- XPCOM: `Services.obs`

## updateMemory()
- 位置: async L553-642
- 役割: IDの記憶を探し、項目ごとに型を検査してから上書きまたは配列の和集合で更新する。出典IDは和集合にし、構成要素は要約で重複を除く。
- 触るとき: 記憶の項目が更新されない、または配列が増え続けると調べるとき。更新できる項目を変えるとき。
- 呼び出し先: `Array.isArray()`, `Date.now()`, `MEMORY_SENSIVITITY_CATEGORIES.includes()`, `MEMORY_TYPES.includes()`, `Number.isFinite()`, `Object.values()`, `Object.values(v).every()`, `Services.obs.notifyObservers()`, `gJSONFile?.saveSoon()`, `gState.memories.find()`, `isComponentSummaries()`, `this.ensureInitialized()`, `v.every()`, `val.every()`, `validator()`
- 条件付き依存: `if (prop in updates && validator(updates[prop]))` → `Array.isArray()`
- 条件付き依存: `if (updates.source_ids)` → `unionSourceIds()`
- 条件付き依存: `if (isComponentSummaries(updates.component_summaries))` → `[...memory.component_summaries, ...updates.component_summaries].map()`
- 参照: `component.memory_summary`, `i.id`, `memory.component_summaries`, `memory.source_ids`, `memory.updated_at`, `updates.component_summaries`, `updates.source_ids`, `updates.updated_at`
- XPCOM: `Services.obs`

## softDeleteMemory()
- 位置: async L652-657
- 役割: 記憶の論理削除フラグを立て、通知と件数の指標を送る。
- 触るとき: 取り消し可能な削除の挙動を調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `this.updateMemory()`, `updateMemoriesCountMetric()`
- XPCOM: `Services.obs`

## hardDeleteMemory()
- 位置: async L667-683
- 役割: IDの記憶を配列から取り除き、削除の記録を送ってから保存を予約する。見つからなければfalseを返す。
- 触るとき: 記憶が物理削除される経路を追うとき、削除の記録の項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.memoryRemovedPanel.record()`, `Services.obs.notifyObservers()`, `gJSONFile?.saveSoon()`, `gState.memories.findIndex()`, `gState.memories.splice()`, `this.ensureInitialized()`, `updateMemoriesCountMetric()`
- 参照: `gState.memories.length`, `i.id`
- XPCOM: `Services.obs`

## computeMemoriesHash()
- 位置: L693-707
- 役割: 記憶のIDと要約を連結した文字列をFNV-1aで畳み込み、32ビットの値を返す。
- 触るとき: 記憶が変わったかの判定に使うキャッシュの鍵を変えるとき。
- 呼び出し先: `str.charCodeAt()`
- 参照: `m.id`, `m.memory_summary`, `str.length`

## _clearEmbeddingsCache()
- 位置: L712-715
- 役割: 埋め込みキャッシュと、そのキャッシュの鍵を消す。テスト用。
- 触るとき: 埋め込みの単体テストでキャッシュを初期化するとき。
- 参照: `this.memoryCacheKey`, `this.memoryEmbeddingsCache`

## getRelevantMemories()
- 位置: async L728-784
- 役割: 削除されていない記憶の、タグ・要約・理由を連結した文を埋め込み、記憶の内容が変わったときだけ再計算する。問い合わせとのコサイン類似度を求め、閾値以上を上位k件返す。
- 触るとき: 会話に関連する記憶が出ない、または遅いとき。埋め込みの文の作り方や閾値を変えるとき。
- 呼び出し先: `Array.isArray()`, `cosSim()`, `message.toLowerCase()`, `similarities .filter()`, `similarities .filter(m => m.similarity >= similarityThreshold) .sort()`, `similarities .filter(m => m.similarity >= similarityThreshold) .sort((a, b) => b.similarity - a.similarity) .slice()`, `this.computeMemoriesHash()`, `this.embeddingsGenerator.embed()`, `this.getMemories()`, `this.memoryEmbeddingsCache.map()`
- 条件付き依存: `if (!this.embeddingsGenerator)` → `embeddingsGeneratorFactory.forGeneral()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `memories.map()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.memory_summary?.toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.reasoning?.toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.tags?.join(" ").toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `m.tags?.join()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `[tags, summary, reasoning] .filter(part => part?.trim()) .join(". ") .toLowerCase()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `[tags, summary, reasoning] .filter(part => part?.trim()) .join()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `[tags, summary, reasoning] .filter()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `part?.trim()`
- 条件付き依存: `if ( !this.memoryEmbeddingsCache || this.memoryCacheKey !== currentCacheKey )` → `this.embeddingsGenerator.embedMany()`
- 参照: `a.similarity`, `b.similarity`, `m.similarity`, `memories.length`, `queryEmbedding.length`, `queryResult.output`, `result.output`, `this.embeddingsGenerator`, `this.memoryCacheKey`, `this.memoryEmbeddingsCache`

## parseAggregateDays()
- 位置: L794-811
- 役割: 日の指定(例 0-2,4)を、重複のない日の番号の配列にする。0以上で7日未満のものだけ残す。
- 触るとき: recent_accessed_countsの日指定の解釈を変えるとき。
- 呼び出し先: `[...days].filter()`, `dayList.split()`, `token.trim()`, `trimmed.match()`
- 条件付き依存: `if (range)` → `Number()`
- 条件付き依存: `if (range)` → `days.add()`
- 条件付き依存: `if (!(range))` → `days.add()`
- 条件付き依存: `if (!(range))` → `Number()`

## resolveFilterField()
- 位置: L823-839
- 役割: 項目名がrecent_accessed_countsの日指定なら、指定の日の回数を合計して返す。それ以外は項目の値をそのまま返す。
- 触るとき: 日指定の集計の結果が想定と違うとき。
- 呼び出し先: `field.match()`, `this.parseAggregateDays()`, `this.parseAggregateDays(dayList).reduce()`

## getMemories()
- 位置: async L886-966
- 役割: 削除されていないもの(指定があれば含める)を、IDの指定で絞り、各条件を検査してから順に絞り込み、最後に並べ替えて返す。LIKE条件は意味検索に回す。条件が不正なら空を返す。
- 触るとき: 記憶の取り出しで結果が空になる、または並びが違うとき。条件の書式や並び順の既定値を変えるとき。
- 呼び出し先: `Object.values()`, `Object.values(MEMORY_FILTER_COMPARATOR).includes()`, `this.ensureInitialized()`, `validators.field()`, `validators.value()`
- 条件付き依存: `if (!includeSoftDeleted)` → `res.filter()`
- 条件付き依存: `if (memoryIds.size)` → `res.filter()`
- 条件付き依存: `if (memoryIds.size)` → `memoryIds.has()`
- 条件付き依存: `if (!Object.values(MEMORY_FILTER_COMPARATOR).includes(comparator))` → `lazy.console.error()`
- 条件付き依存: `if (!validators.field(field))` → `lazy.console.error()`
- 条件付き依存: `if (!validators.value(value))` → `lazy.console.error()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `( await this.getRelevantMemories(value, topK, similarityThreshold) ).map()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `this.getRelevantMemories()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `res.filter()`
- 条件付き依存: `if (comparator === MEMORY_FILTER_COMPARATOR.LIKE)` → `semanticMatches.has()`
- 条件付き依存: `if (predicate)` → `res.filter()`
- 条件付き依存: `if (predicate)` → `predicate()`
- 条件付き依存: `if (predicate)` → `this.resolveFilterField()`
- 条件付き依存: `if (sortBy)` → `[...res].sort()`
- 参照: `MEMORY_FILTER_COMPARATOR.LIKE`, `gState.memories`, `i.id`, `i.is_deleted`, `memoryIds.size`

## getMeta()
- 位置: async L973-976
- 役割: メタ情報(各種の時刻)を複製して返す。内部の状態は渡さない。
- 触るとき: 生成の時刻の判定が想定と違うとき、メタ情報の読み方を確かめるとき。
- 呼び出し先: `structuredClone()`, `this.ensureInitialized()`
- 参照: `gState.meta`

## updateMeta()
- 位置: async L989-1007
- 役割: メタ情報の時刻のうち、有限な数値のものだけ更新し、保存を予約して指標を送る。
- 触るとき: 処理済みの時刻が書き込まれない、または変な値になるとき。
- 呼び出し先: `Number.isFinite()`, `gJSONFile?.saveSoon()`, `this.ensureInitialized()`, `updateMemoriesLastUpdatedMetric()`, `validator()`
- 参照: `gState.meta`

## updateMemoriesCountMetric()
- 位置: L1010-1033
- 役割: 削除されていない記憶を出典ごとに数え、その数を指標として送る。最後に最終更新の指標も送る。
- 触るとき: 記憶の件数の指標が合わないとき。
- 呼び出し先: `Glean.smartWindow.memoriesCount.conversation.set()`, `Glean.smartWindow.memoriesCount.history.set()`, `Glean.smartWindow.memoriesCount.session.set()`, `memory.sources?.includes()`, `updateMemoriesLastUpdatedMetric()`
- 条件付き依存: `if (!(memory.sources?.includes(CONVERSATION)))` → `memory.sources?.includes()`
- 条件付き依存: `if (!(memory.sources?.includes(HISTORY)))` → `memory.sources?.includes()`
- 参照: `gState.memories`, `memory.is_deleted`

## updateMemoriesLastUpdatedMetric()
- 位置: L1035-1046
- 役割: メタ情報の三つの処理済み時刻の最大値を、最終更新の指標として送る。どれも無ければ今の時刻を使う。
- 触るとき: 最終更新の指標が古い、または今の時刻になると調べるとき。
- 呼び出し先: `Date.now()`, `Glean.smartWindow.memoriesLastUpdated.set()`, `Math.max()`
- 参照: `gState.meta.last_chat_memory_ts`, `gState.meta.last_history_memory_ts`, `gState.meta.last_session_memory_ts`

## hashStringToHex()
- 位置: L1055-1065
- 役割: 文字列をFNV-1aで32ビットの値にし、8桁の16進数の文字列にする。
- 触るとき: 記憶のIDの形を変えるとき。
- 呼び出し先: `hash.toString()`, `hash.toString(16).padStart()`, `str.charCodeAt()`
- 参照: `str.length`

## makeMemoryId()
- 位置: L1073-1082
- 役割: IDが指定されていればそれを返す。無ければ要約を小文字にして詰めた文字列の16進ハッシュから、mem.で始まるIDを作る。
- 触るとき: 同じ要約の記憶が同じIDになる仕組みを変えるとき、IDの衝突を調べるとき。
- 呼び出し先: `(memoryPartial.memory_summary || "").trim()`, `(memoryPartial.memory_summary || "").trim().toLowerCase()`, `hashStringToHex()`
- 参照: `memoryPartial.id`, `memoryPartial.memory_summary`
