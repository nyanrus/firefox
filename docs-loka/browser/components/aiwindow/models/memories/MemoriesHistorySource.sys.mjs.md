# browser/components/aiwindow/models/memories/MemoriesHistorySource.sys.mjs

source: browser/components/aiwindow/models/memories/MemoriesHistorySource.sys.mjs
source-hash: 62635e660f0c1985c55587863e006e3dd6da7c06
lines: 1164

## <module>
- 役割: Places(閲覧履歴)から記憶生成用の材料を取り出し、セッション化、ドメインとタイトルと検索語の集計とランク付け、記憶に紐づくURLの解決までを担う。
- 呼び出し先: `BlockListManager.initializeFromDefault()`, `ChromeUtils.defineESModuleGetters()`

## getDistanceThreshold()
- 位置: L47-52
- 役割: 意味的な距離の閾値を、prefの文字列から読む。読めなければ既定値0.6を返す。
- 触るとき: 記憶に紐づく再開用URLの距離判定を調整したいとき、prefの値を確かめるとき。
- 呼び出し先: `Number.isFinite()`, `Number.parseFloat()`, `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## getRecentHistory()
- 位置: async L124-337
- 役割: moz_places_metadataの滞在時間の長いページ閲覧と、検索エンジンへの訪問から取り出した検索語を、SQLで最新順に集める。機微情報を含む行を除き、タイトルと検索語をサニタイズして返す。
- 触るとき: 記憶生成に入る閲覧の件数や期間が少ない・多いと感じるとき、検索語の抽出規則を変えるとき、機微情報の除外が効いているか確かめるとき。
- 呼び出し先: `PlacesUtils.withConnectionWrapper()`, `_mgr.matchAtWordBoundary()`, `_sensitiveInfoDetector.containsSensitiveInfo()`, `_sensitiveInfoDetector.containsSensitiveKeywords()`, `console.error()`, `db.execute()`, `out.push()`, `row.getResultByName()`, `safeDecodeURIComponent()`, `sanitizeUntrustedContent()`, `title.toLowerCase()`
- 条件付き依存: `if (sinceMicros != null)` → `Math.max()`
- 条件付き依存: `if (!(sinceMicros != null))` → `Math.max()`
- 条件付き依存: `if (!(sinceMicros != null))` → `Date.now()`
- 条件付き依存: `if (onlyTitle)` → `sanitizeTitle()`

## sessionizeVisits()
- 位置: L352-390
- 役割: 行を時刻順に並べ、直前の訪問からの間隔がgapSecを超えるか、セッションの長さがmaxSessionSecを超えたら新しいセッションの開始時刻を振る。
- 触るとき: 閲覧のセッションの区切り方を変えるとき、同じ時間帯の訪問が別々のセッションに割れると調べるとき。
- 呼び出し先: `Math.floor()`, `Number.isFinite()`, `new Date(curStartMs).toISOString()`, `rows // Keep only rows with a valid timestamp .filter()`, `rows // Keep only rows with a valid timestamp .filter(row => Number.isFinite(row.visitDateMicros)) .map()`
- 参照: `a.visitTimeMs`, `b.visitTimeMs`, `opts.gapSec`, `opts.maxSessionSec`, `row.session_id`, `row.session_start_iso`, `row.session_start_ms`, `row.visitDateMicros`, `row.visitTimeMs`

## generateProfileInputs()
- 位置: L413-513
- 役割: セッションごとに、タイトルとドメインのスコア、検索の件数と検索語、開始と終了の時刻をまとめた入力レコードを作る。
- 触るとき: プロファイル用の入力データの形を変えるとき、セッションの時刻が欠けると調べるとき。
- 呼び出し先: `Math.max()`, `Number()`, `Object.entries()`, `Object.keys()`, `bySession.get()`, `bySession.get(sessionId).push()`, `bySession.has()`, `bySession.keys()`, `isFiniteNumber()`, `items .filter()`, `items .filter(Number.isFinite) .map()`, `items.filter()`, `normalizeEpochSeconds()`, `preparedInputs.push()`, `searchItems.map()`, `searchItems.map(r => r.title).filter()`
- 条件付き依存: `if (!bySession.has(sessionId))` → `bySession.set()`
- 条件付き依存: `if (tsList.length)` → `Math.min()`
- 条件付き依存: `if (tsList.length)` → `Math.max()`
- 参照: `Number.isFinite`, `Object.keys(m).length`, `r.domain`, `r.domainFrequencyPct`, `r.frequencyPct`, `r.host`, `r.source`, `r.title`, `r.visitDateMicros`, `row.session_id`, `searchItems.length`, `sessionTimes.end_time`, `sessionTimes.start_time`, `tsList.length`

## aggregateSessions()
- 位置: L528-615
- 役割: セッションの入力を横断して、ドメイン、タイトル、検索ごとに最後の値のスコア、最終閲覧時刻、セッション数、重要度(総セッション数÷出現セッション数)を集計する。
- 触るとき: どのドメインやタイトルが上位に来るかの集計結果を調べるとき、重要度の式を変えるとき。
- 呼び出し先: `Array.isArray()`, `Date.now()`, `Math.max()`, `Number()`, `Number.isFinite()`, `Object.create()`, `Object.entries()`, `Object.keys()`, `Object.values()`, `getOrInit()`, `rec.sessions.add()`, `round2()`
- 条件付き依存: `if (hasSearchContent)` → `getOrInit()`
- 条件付き依存: `if (hasSearchContent)` → `Number()`
- 条件付き依存: `if (hasSearchContent)` → `rec.search_titles.add()`
- 条件付き依存: `if (hasSearchContent)` → `Math.max()`
- 条件付き依存: `if (hasSearchContent)` → `toSeconds()`
- 参照: `preparedInputs.length`, `rec.last_searched`, `rec.last_seen`, `rec.num_sessions`, `rec.score`, `rec.search_count`, `rec.search_titles`, `rec.session_importance`, `rec.sessions`, `rec.sessions.size`, `search_titles.length`, `session.domain_scores`, `session.search_events`, `session.session_end_time`, `session.session_id`, `session.session_start_time`, `session.title_scores`

## topkAggregates()
- 位置: L663-769
- 役割: 集計結果に時間減衰を掛けたランクを付け、ドメイン30件、タイトル60件、検索10件を上位から切り出す。
- 触るとき: 記憶生成に渡す上位の閲覧候補を増減させるとき、ランクの並びが想定と違うとき。
- 呼び出し先: `Array.isArray()`, `Number()`, `Number.isFinite()`, `Object.entries()`, `Object.entries(aggDomains).map()`, `Object.entries(aggSearches).map()`, `Object.entries(aggTitles).map()`, `domainRanked .slice()`, `domainRanked .slice(0, k_domains) .map()`, `domainRanked.sort()`, `round2()`, `searchRanked .slice()`, `searchRanked .slice(0, k_searches) .map()`, `searchRanked.sort()`, `titleRanked .slice()`, `titleRanked .slice(0, k_titles) .map()`, `titleRanked.sort()`, `withRecency()`
- 条件付き依存: `if (now == null)` → `Date.now()`
- 条件付き依存: `if (!(now == null))` → `Number()`
- 参照: `a.cnt`, `a.last_seen`, `a.ls`, `a.num_sessions`, `a.rank`, `b.cnt`, `b.last_seen`, `b.ls`, `b.num_sessions`, `b.rank`, `info.last_searched`, `info.last_seen`, `info.num_sessions`, `info.score`, `info.search_count`, `info.search_titles`, `info.session_importance`

## withRecency()
- 位置: L798-818
- 役割: スコアと重要度の積に、半減期14日の時間減衰を下限0.5まで掛けて、小数2桁のランクを返す。
- 触るとき: 新しい閲覧を優先する度合いを変えるとき。引数の時刻の単位を変えるときは、toSecondsの扱いを必ず見る。
- 呼び出し先: `Date.now()`, `Math.max()`, `Math.pow()`, `Number()`, `round2()`, `toSeconds()`

## isFiniteNumber()
- 位置: L820-822
- 役割: 値が有限の数値かを判定する。
- 触るとき: 集計入力の数値チェックを見直すとき。
- 呼び出し先: `Number.isFinite()`

## normalizeEpochSeconds()
- 位置: L830-835
- 役割: エポックマイクロ秒を整数の秒に変換する。有限でなければnullを返す。
- 触るとき: プロファイル入力の時刻の単位を変えるとき。
- 呼び出し先: `Math.floor()`, `Number.isFinite()`

## toSeconds()
- 位置: L837-843
- 役割: 値が1e13より大きければマイクロ秒、それ以外はミリ秒と見なして秒に変換する。有限でなければ0を返す。
- 触るとき: 時刻の単位が想定と違うとき。秒の値を渡している箇所があると、ここで桁がずれるので確かめるとき。
- 呼び出し先: `Number()`, `Number.isFinite()`

## getOrInit()
- 位置: L845-850
- 役割: マップに鍵が無ければ初期化関数の結果を入れ、その値を返す。
- 触るとき: 集計マップの初期化の仕方を変えるとき。
- 条件付き依存: `if (!(key in mapObj))` → `initFn()`

## round2()
- 位置: L852-854
- 役割: 数値を小数2桁に丸める。
- 触るとき: ランクや重要度の丸め方を変えるとき。
- 呼び出し先: `Math.round()`, `Number()`

## safeDecodeURIComponent()
- 位置: L856-865
- 役割: URLの検索語をデコードする。不正な符号化なら元の文字列を返す。
- 触るとき: 検索語が文字化けする、または不正なURLでエラーになると調べるとき。
- 呼び出し先: `decodeURIComponent()`

## sanitizeTitle()
- 位置: L876-889
- 役割: タイトルのバックスラッシュをスラッシュに置き換え、制御文字を空白にし、連続する空白を詰めて前後を削る。
- 触るとき: LLMのJSON出力が崩れる原因がタイトルにあると調べるとき、サニタイズの規則を増やすとき。
- 呼び出し先: `title .replace()`, `title .replace(/\\/g, "/") // Replace backslash with forward slash // eslint-disable-next-line no-control-regex .replace()`

## _setBlockListManagerForTesting()
- 位置: L892-894
- 役割: テスト用にブロックリストマネージャーを差し替える。
- 触るとき: ブロックリストに関わる単体テストを書くとき。

## _sanitizeTitleForTesting()
- 位置: L896-898
- 役割: テスト用にタイトルのサニタイズ関数を公開する。
- 触るとき: タイトルのサニタイズを単体テストするとき。
- 呼び出し先: `sanitizeTitle()`

## countRecentVisits()
- 位置: async L907-938
- 役割: 過去N日のタイトルと頻度のある訪問の件数をSQLで数える。失敗時は0を返す。
- 触るとき: 記憶生成を実行すべき閲覧量があるかを判断する前提を確かめるとき。
- 呼び出し先: `Date.now()`, `Math.max()`, `Number()`, `PlacesUtils.withConnectionWrapper()`, `console.error()`, `db.execute()`, `row.getResultByName()`

## getHistorySourceIdsFromMemory()
- 位置: L946-948
- 役割: 記憶のsource_idsから履歴のURLハッシュ配列を取り出す。無ければ空配列を返す。
- 触るとき: 記憶から閲覧履歴のIDをたどる処理を変えるとき。
- 参照: `memory?.source_ids?.history_source_ids`

## resolveUrlsForMemories()
- 位置: async L965-1041
- 役割: 記憶が持つURLハッシュをmoz_placesで引き、URLとタイトルと最終訪問日の対応表を返す。履歴が無効か私用ブラウズ中なら空を返す。要約との類似で絞るときは意味検索の結果を優先し、使えなければ全件の解決に戻る。
- 触るとき: 記憶に紐づく再開用のURLが出ない、または多すぎるとき。履歴の無効化や私用ブラウズの扱いを変えるとき。
- 呼び出し先: `PlacesUtils.withConnectionWrapper()`, `Services.prefs.getBoolPref()`, `bindUrlHashes()`, `console.error()`, `db.execute()`, `getDistanceThreshold()`, `getHistorySourceIdsFromMemory()`, `memories.flatMap()`, `placeholders.join()`, `row.getResultByName()`, `rows.map()`
- 条件付き依存: `if (filterBySummary)` → `resolveUrlsBySummarySimilarity()`
- 参照: `urlHashes.length`
- XPCOM: `Services.prefs`

## bindUrlHashes()
- 位置: L1049-1057
- 役割: URLハッシュの配列を名前付きのSQLバインド変数とプレースホルダーに変換する。
- 触るとき: IN句に渡すURLハッシュの数や名前を変えるとき。
- 呼び出し先: `urlHashes.map()`

## getMemoryEmbeddingText()
- 位置: L1065-1069
- 役割: 記憶の要約と理由を小文字にして連結し、埋め込みに使う文字列を作る。
- 触るとき: 意味検索の問い合わせ文を変えるとき。
- 呼び出し先: `[summary, reasoning].filter()`, `[summary, reasoning].filter(part => part?.trim()).join()`, `memory?.memory_summary?.toLowerCase()`, `memory?.reasoning?.toLowerCase()`, `part?.trim()`

## resolveUrlsBySummarySimilarity()
- 位置: async L1080-1163
- 役割: 意味検索が使えるときだけ、記憶ごとの埋め込みと履歴ベクトルのコサイン距離を求め、閾値以内のURLを距離の近い順に返す。使えなければnullを返す。
- 触るとき: 要約に近いURLだけを残す挙動を調べるとき。意味検索が効かずに全件へ戻る原因を追うとき。
- 呼び出し先: `PlacesUtils.tensorToSQLBindable()`, `[...resolved].sort()`, `bindUrlHashes()`, `conn.execute()`, `console.error()`, `getHistorySourceIdsFromMemory()`, `getMemoryEmbeddingText()`, `lazy.extractVectorFromTensor()`, `lazy.getPlacesSemanticHistoryManager()`, `placeholders.join()`, `resolved.get()`, `resolved.set()`, `row.getResultByName()`, `semanticManager.embedder.embed()`, `semanticManager.embedder.ensureEngine()`, `semanticManager.getConnection()`, `semanticManager.hasSufficientEntriesForSearching()`
- 条件付き依存: `if (existing)` → `Math.min()`
- 参照: `a.distance`, `b.distance`, `existing.distance`, `semanticManager.isEnabledForSmartWindow`, `urlHashes.length`
