# browser/components/aiwindow/ui/modules/ChatStore.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatStore.sys.mjs
source-hash: 580e3215ec51366d34ff35dc228a949d564531b3
lines: 1710

## <module>
- 役割: チャット会話を SQLite に保存・検索・削除する ChatStore のシングルトンを定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## ChatStore.constructor()
- 位置: L174-192
- 役割: 終了ブロッカーを用意し、idle-daily の通知を購読する。
- 触るとき: 起動時の監視登録や定期削除の仕組みを変えるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.obs.addObserver()`
- 参照: `this.#asyncShutdownBlocker`, `this.#lastRecordedSize`, `this.QueryInterface`
- XPCOM: `Services.obs`

## this.#asyncShutdownBlocker()
- 位置: async L175-183
- 役割: 終了時に計測待ちを確定させてから接続を閉じるブロッカー関数。
- 触るとき: アプリ終了時に書き込みや接続クローズの順序が崩れる問題を調べるとき。
- 呼び出し先: `this.#closeConnection()`, `this.#sizeRecordTask?.finalize()`
- 参照: `this.#sizeRecordTask`

## ChatStore.observe()
- 位置: L194-200
- 役割: idle-daily の通知を受けて、古い会話を削除する pruneDatabase を呼ぶ。
- 触るとき: 定期的な DB 整理がなぜ動かない・過剰に消すかを調べるとき。
- 条件付き依存: `if (topic === "idle-daily")` → `this.pruneDatabase().catch()`
- 条件付き依存: `if (topic === "idle-daily")` → `this.pruneDatabase()`
- 条件付き依存: `if (topic === "idle-daily")` → `lazy.log.error()`
- 参照: `e.message`, `e.stack`

## ChatStore.updateConversation()
- 位置: async L207-252
- 役割: 会話行とメッセージ行、ツール結果を一つのトランザクションで保存し、DB サイズ計測を予約する。
- 触るとき: 会話の保存項目を増やす・保存タイミングを変えるとき。ストリーム中の書き込みは persistStreamingMessage 側なので混同しないよう注意。
- 呼び出し先: `Array.from()`, `JSON.stringify()`, `URL.parse()`, `conversation.messages.map()`, `lazy.log.error()`, `this.#applyToolResults()`, `this.#conn .executeTransaction()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`, `this.#toMessageRow()`, `toJSONOrNull()`
- 参照: `conversation.activeBranchTipMessageId`, `conversation.createdDate`, `conversation.description`, `conversation.id`, `conversation.memoriesToggled`, `conversation.pageMeta`, `conversation.pageUrl`, `conversation.securityProperties`, `conversation.seenUrls`, `conversation.serpUrlsForAnonymousFetch`, `conversation.status`, `conversation.title`, `conversation.updatedDate`, `e.message`, `e.stack`, `pageUrl?.href`

## ChatStore.#toMessageRow()
- 位置: L254-275
- 役割: ChatMessage を DB のメッセージ行の形に変換し、JSON 項目を文字列化する。
- 触るとき: メッセージに保存する項目を増やすとき、または保存されたのに読み直すと値が消える問題を調べるとき。
- 呼び出し先: `toJSONOrNull()`
- 参照: `m.content`, `m.createdDate`, `m.id`, `m.isActiveBranch`, `m.memoriesApplied`, `m.memoriesEnabled`, `m.memoriesFlagSource`, `m.modelId`, `m.ordinal`, `m.pageUrl?.href`, `m.params`, `m.parentMessageId`, `m.revisionRootMessageId`, `m.role`, `m.turnIndex`, `m.usage`, `m.webSearchQueries`

## ChatStore.persistStreamingMessage()
- 位置: L295-328
- 役割: ストリーム中のメッセージを、最初のチャンクでは会話全体、以降は一定間隔でそのメッセージの行だけ書き込む。
- 触るとき: ストリーミング中の保存頻度や、途中で落ちた時に何が残るかを変えるとき。呼び出し側は endStreamingWrites で必ず終える必要がある。
- 呼び出し先: `(async () => { await this.#endStreamingEntry(previous); await this.updateConversation(conversation); })()`, `entry.ready.catch()`, `lazy.log.error()`, `this.#endStreamingEntry()`, `this.#streamingWrites.get()`, `this.#streamingWrites.set()`, `this.#writeStreamingMessage()`, `this.updateConversation()`
- 条件付き依存: `if (previous?.message === message)` → `previous.task.arm()`
- 参照: `conversation.id`, `e.message`, `e.stack`, `entry.ready`, `entry.task`, `lazy.DeferredTask`, `previous?.message`

## ChatStore.endStreamingWrites()
- 位置: async L339-354
- 役割: 保留中のストリーム書き込みを止め、必要ならその場で書き切ってから完了を待つ。
- 触るとき: 会話の削除や終了の前に書き込みが後から走る問題を調べるとき。flush を false にするのは直後に全体保存する場合だけ。
- 呼び出し先: `Array.from()`, `Promise.all()`, `entries.map()`, `this.#endStreamingEntry()`, `this.#streamingWrites.get()`, `this.#streamingWrites.values()`
- 条件付き依存: `if (convId === null)` → `this.#streamingWrites.clear()`
- 条件付き依存: `if (!(convId === null))` → `this.#streamingWrites.delete()`

## ChatStore.#endStreamingEntry()
- 位置: async L364-377
- 役割: 一件のストリーム書き込みを終了させる（必要なら保留分を捨てる）。
- 触るとき: ストリーム書き込みの終了処理の順序を変えるとき。呼び出し前に一覧から外しておく必要がある。
- 呼び出し先: `entry.task.finalize()`, `lazy.log.error()`
- 条件付き依存: `if (!flush)` → `entry.task.disarm()`
- 参照: `e.message`, `e.stack`, `entry.ready`

## ChatStore.#writeStreamingMessage()
- 位置: async L390-395
- 役割: ストリーム中のメッセージの行だけを書き直す。
- 触るとき: ストリーム中に保存されるフィールドを増やすとき。会話行は触らない点に注意。
- 呼び出し先: `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#toMessageRow()`

## ChatStore.#applyToolResults()
- 位置: async L397-436
- 役割: メッセージのツール UI、履歴結果、引用を tool_result 表へ追加する（上書きで挿入）。
- 触るとき: ツール結果の保存形式を変えるとき、または再読み込み後に履歴グリッドや引用が欠ける問題を調べるとき。
- 呼び出し先: `m.citations.forEach()`, `m.historyResults.forEach()`, `stripResolvedAssets()`, `toJSONOrNull()`, `toolResults.push()`
- 条件付き依存: `if (m.toolUIData)` → `toolResults.push()`
- 条件付き依存: `if (m.toolUIData)` → `toJSONOrNull()`
- 条件付き依存: `if (toolResults.length)` → `this.#conn.executeCached()`
- 参照: `TOOL_RESULT_TYPE.CITATIONS`, `TOOL_RESULT_TYPE.HISTORY_RESULTS`, `TOOL_RESULT_TYPE.TOOL_UI`, `conversation.messages`, `m.id`, `m.toolUIData`, `toolResults.length`

## ChatStore.deleteAllUrlsFromMessages()
- 位置: async L443-466
- 役割: 全メッセージの page_url を消し、履歴削除フラグを立てる。
- 触るとき: 全サイト履歴の削除処理を変えるとき。
- 呼び出し先: `lazy.log.error()`, `this.#conn .executeCached()`, `this.#conn .executeCached(REMOVE_ALL_SITE_URLS_FROM_MESSAGES) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.deleteUrlFromMessages()
- 位置: async L475-498
- 役割: 指定の page_url を持つメッセージの URL を消し、履歴削除フラグを立てる。
- 触るとき: 特定サイトの履歴削除（ページごと忘れる操作）の範囲を調べるとき。
- 呼び出し先: `lazy.log.error()`, `this.#conn .executeCached()`, `this.#conn .executeCached(REMOVE_SITE_URL_FROM_MESSAGES, { page_url }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.findOldestConversations()
- 位置: async L506-535
- 役割: 最も古い会話を指定件数分、ID とタイトル付きで返す。
- 触るとき: 古い会話から削除する対象の選び方を変えるとき。
- 呼び出し先: `lazy.log.error()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached(CONVERSATIONS_OLDEST, { limit: numberOfConversations, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.findRecentConversations()
- 位置: async L543-573
- 役割: 最近の会話を指定件数分、ID・タイトル・ページ URL 付きで返す。
- 触るとき: 最近の会話の一覧（メニューなど）の内容や件数を変えるとき。
- 呼び出し先: `lazy.log.error()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached(CONVERSATIONS_MOST_RECENT, { limit: numberOfConversations, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.findConversationById()
- 位置: async L582-600
- 役割: ID で会話を一件読み込み、そのメッセージも含めて返す。見つからなければ null。
- 触るとき: 会話を開く処理で読み込み内容が欠ける問題を調べるとき。
- 呼び出し先: `lazy.log.error()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#findConversationsWithMessages()`, `this.#findConversationsWithMessages( CONVERSATION_BY_ID, { conv_id: conversationId, } ).catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.findConversationsByDate()
- 位置: async L610-615
- 役割: 作成日時の範囲で会話を読み込む（メッセージ込み）。
- 触るとき: 日付範囲での会話検索や、そこに使う SQL を変えるとき。
- 呼び出し先: `this.#findConversationsWithMessages()`

## ChatStore.findConversationsByURL()
- 位置: async L624-628
- 役割: 指定ページ URL に紐づく会話を読み込む（メッセージ込み）。
- 触るとき: ページごとの会話一覧が期待どおりか調べるとき。
- 呼び出し先: `this.#findConversationsWithMessages()`
- 参照: `pageUrl.href`

## ChatStore.findMessagesByDate()
- 位置: async L644-676
- 役割: 期間と役割で絞ったメッセージを、件数とオフセット付きで返す。
- 触るとき: 期間指定のメッセージ取得やページングを変えるとき。役割指定がある時だけ別の SQL を使う。
- 呼び出し先: `endDate.getTime()`, `lazy.log.error()`, `parseMessageRows()`, `startDate.getTime()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`, `params.role`

## ChatStore.getMostRecentMessages()
- 位置: async L690-692
- 役割: 全期間を対象に findMessagesByDate を呼び、役割と件数で絞ったメッセージを返す。
- 触るとき: 直近メッセージを使う機能（文脈の取り込みなど）の件数や役割の指定を変えるとき。
- 呼び出し先: `this.findMessagesByDate()`

## ChatStore.#escapeForLike()
- 位置: L694-699
- 役割: LIKE 検索用に、エスケープ文字と % _ をエスケープする。
- 触るとき: 検索語に記号を含むと結果がずれる問題を調べるとき。
- 呼び出し先: `searchString .replaceAll()`, `searchString .replaceAll(ESCAPE_CHAR, `${ESCAPE_CHAR}${ESCAPE_CHAR}`) .replaceAll()`, `searchString .replaceAll(ESCAPE_CHAR, `${ESCAPE_CHAR}${ESCAPE_CHAR}`) .replaceAll("%", `${ESCAPE_CHAR}%`) .replaceAll()`

## ChatStore.searchContent()
- 位置: async L713-745
- 役割: メッセージ内容の JSON の指定パスの値を検索し、一致した会話をメッセージ付きで返す。
- 触るとき: ツール結果や内容の特定フィールドを検索する機能を追加・変更するとき。
- 呼び出し先: `lazy.log.error()`, `rows.map()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#getMessagesForConversations()`
- 参照: `e.message`, `e.stack`, `params.role`, `rows.length`

## ChatStore.search()
- 位置: async L760-793
- 役割: 会話のタイトルと本文を部分一致で検索し、一致箇所の抜粋付きで返す。
- 触るとき: チャット履歴の検索結果や抜粋の内容を変えるとき、または検索にヒットしない問題を調べるとき。
- 呼び出し先: `lazy.log.error()`, `parseConversationRow()`, `row.getResultByName()`, `rows.map()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#escapeForLike()`, `this.#getMessagesForConversations()`
- 参照: `conv.matchingSnippet`, `e.message`, `e.stack`, `rows.length`

## ChatStore.chatHistoryView()
- 位置: async L802-826
- 役割: 履歴画面用に、ページ番号と並び順で会話の一覧を読む。
- 触るとき: 履歴画面のページング・並び替えを変えるとき。
- 呼び出し先: `CONVERSATION_HISTORY.replace()`, `SORTS.find()`, `lazy.log.error()`, `parseChatHistoryViewRows()`, `sort.toUpperCase()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.getDbBytesInUse()
- 位置: async L834-840
- 役割: DB が実際に使っているバイト数を dbstat から求める。
- 触るとき: DB 容量の上限判定やサイズ計測の値を調べるとき。
- 呼び出し先: `rows[0].getResultByName()`, `this.#conn.execute()`

## ChatStore.pruneDatabase()
- 位置: async L851-915
- 役割: DB が上限を超えていれば古い会話を少しずつ削除し、空き領域を回収して計測する。
- 触るとき: DB の容量上限や削除の量・回数を変えるとき、または削除が進まない（停滞）問題を調べるとき。
- 呼び出し先: `IOUtils.exists()`, `Math.max()`, `lazy.log.error()`, `oldestConversations.map()`, `this.#conn.execute()`, `this.#deleteConversationsByIds()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.findOldestConversations()`, `this.getDbBytesInUse()`, `this.recordDatabaseSizeNow()`
- 参照: `chat.id`, `e.message`, `e.stack`, `oldestConversations.length`, `this.databaseFilePath`

## ChatStore.#deleteConversationsByIds()
- 位置: async L924-934
- 役割: 会話 ID を一定件数ずつトランザクションで削除する。
- 触るとき: 一括削除の分割サイズや削除対象の扱いを変えるとき。
- 呼び出し先: `getDeleteConversationsByIdsSql()`, `ids.slice()`, `this.#conn.execute()`, `this.#conn.executeTransaction()`
- 参照: `chunk.length`, `ids.length`

## ChatStore.deleteMessages()
- 位置: async L941-989
- 役割: 指定メッセージを削除し、その結果メッセージの無くなった会話も削除する。
- 触るとき: メッセージ単位の削除後に空の会話が残る・消えすぎる問題を調べるとき。
- 呼び出し先: `Array.from()`, `Promise.all()`, `chunk.map()`, `chunk.reduce()`, `chunks.push()`, `convs.add()`, `getDeleteEmptyConversationsSql()`, `getDeleteMessagesByIdsSql()`, `lazy.log.error()`, `messages.map()`, `messages.slice()`, `this.#conn.execute()`, `this.#conn.executeTransaction()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`, `this.endStreamingWrites()`
- 参照: `chunk.length`, `conversations.length`, `e.message`, `e.stack`, `m.convId`, `m.id`, `message.convId`, `messages.length`

## ChatStore.getDatabaseSize()
- 位置: async L998-1010
- 役割: DB ファイルのサイズをバイトで返す（必要なら接続を開く）。
- 触るとき: DB サイズの計測値や上限判定の入力を確認するとき。
- 呼び出し先: `IOUtils.stat()`, `lazy.log.error()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`, `stats.size`, `this.databaseFilePath`

## ChatStore.deleteConversationById()
- 位置: async L1017-1034
- 役割: 指定の会話を削除し、ストリーム書き込みを先に止める。
- 触るとき: 会話の削除で書き込みが後から戻る問題を調べるとき。
- 呼び出し先: `lazy.log.error()`, `this.#conn.execute()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`, `this.endStreamingWrites()`
- 参照: `e.message`, `e.stack`

## ChatStore.deleteConversationsByDateRange()
- 位置: async L1043-1059
- 役割: 作成日時の範囲に入る会話を、ストリーム書き込みを止めてから削除する。
- 触るとき: 期間指定の削除の範囲や条件を変えるとき。
- 呼び出し先: `endDate.getTime()`, `lazy.log.error()`, `startDate.getTime()`, `this.#conn.execute()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.endStreamingWrites()`
- 参照: `e.message`, `e.stack`

## ChatStore.deleteAllConversations()
- 位置: async L1064-1077
- 役割: 全会話を、ストリーム書き込みを止めてから削除する。
- 触るとき: 全削除の処理（履歴の消去など）を変えるとき。
- 呼び出し先: `lazy.log.error()`, `this.#conn.execute()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.endStreamingWrites()`
- 参照: `e.message`, `e.stack`

## ChatStore.destroyDatabase()
- 位置: async L1082-1092
- 役割: テスト後片付け用に、保留の書き込みを捨て DB ファイルを消してサイズを 0 として記録する。
- 触るとき: テストの後片付けが他のテストに影響する問題を調べるとき。本番経路からは呼ばない前提。
- 呼び出し先: `this.#promiseConn?.catch()`, `this.#recordDatabaseSizeValue()`, `this.#removeDatabaseFiles()`, `this.#sizeRecordTask?.disarm()`, `this.endStreamingWrites()`
- 参照: `this.#promiseConn`

## ChatStore.recordDatabaseSizeNow()
- 位置: async L1099-1102
- 役割: 保留中の計測を取り消し、DB サイズを今すぐ計測して記録する。
- 触るとき: DB 容量の計測値がプルーニング後に確実に更新されているかを確認するとき。
- 呼び出し先: `this.#recordDatabaseSize()`, `this.#sizeRecordTask?.disarm()`

## ChatStore.#queueDatabaseSizeRecord()
- 位置: L1109-1115
- 役割: DB サイズの計測を短い遅延でまとめて予約する。
- 触るとき: 書き込み経路から計測を呼ぶ際の頻度を変えるとき。計測は書き込み経路で直接呼ばない。
- 呼び出し先: `this.#recordDatabaseSize()`, `this.#sizeRecordTask.arm()`
- 参照: `lazy.DeferredTask`, `this.#sizeRecordTask`

## ChatStore.#recordDatabaseSize()
- 位置: async L1117-1127
- 役割: DB のサイズを取得し、値を記録する。取得に失敗したら記録しない。
- 触るとき: サイズ計測が記録されない問題を調べるとき。
- 呼び出し先: `lazy.log.error()`, `this.#recordDatabaseSizeValue()`, `this.getDatabaseSize()`
- 参照: `e.message`, `e.stack`

## ChatStore.#recordDatabaseSizeValue()
- 位置: L1129-1135
- 役割: 前回と同じ値なら記録を省き、違えば Glean のチャット保存サイズに設定する。
- 触るとき: サイズのテレメトリが更新されない・多すぎる問題を調べるとき。force で同値でも記録できる。
- 呼び出し先: `Glean.smartWindow.chatStorage.set()`
- 参照: `this.#lastRecordedSize`

## ChatStore.getDatabaseSchemaVersion()
- 位置: async L1142-1148
- 役割: DB に記録されたスキーマ版を返す（必要なら接続を開く）。
- 触るとき: スキーマ移行の判定や、バージョン不一致の調査をするとき。
- 呼び出し先: `this.#conn.getSchemaVersion()`
- 条件付き依存: `if (!this.#conn)` → `this.#ensureDatabase()`
- 参照: `this.#conn`

## ChatStore.#getMessagesForConversations()
- 位置: async L1150-1202
- 役割: 会話群のメッセージをまとめて読んで会話に割り当て、履歴結果と引用のプールを組み直す。
- 触るとき: 会話の読み込み結果にメッセージや引用が無い問題を調べるとき。確認 UI の復元フラグもここで立てる。
- 呼び出し先: `Object.entries()`, `conversation.rehydrateCitationsPool()`, `conversation.rehydrateHistoryResultsPool()`, `conversations.forEach()`, `conversations.map()`, `conversations.reduce()`, `getConversationMessagesSql()`, `lazy.log.error()`, `parseMessageRows()`, `parseMessageRows(rows).forEach()`, `this.#conn .executeCached()`, `this.#conn .executeCached( getConversationMessagesSql(conversations.length), conversations.map(c => c.id) ) .catch()`
- 条件付き依存: `if (convs[message.convId])` → `lazy.CONFIRMATION_UI_TYPES.includes()`
- 条件付き依存: `if (convs[message.convId])` → `(byConv[message.convId] ??= []).push()`
- 参照: `c.id`, `conv.id`, `conversations.length`, `convs[convId].messages`, `e.message`, `e.stack`, `message.convId`, `message.isRestored`, `message.toolUIData?.properties?.actionType`, `message.toolUIData?.uiType`

## ChatStore.#openConnection()
- 位置: async L1204-1252
- 役割: SQLite 接続を開き、終了ブロッカーを登録して WAL などの設定を行う。
- 触るとき: DB の接続設定（ページサイズ、WAL、外部キーなど）を変えるとき。
- 呼び出し先: `Services.profiler.IsActive()`, `lazy.Sqlite.openConnection()`, `lazy.Sqlite.shutdown.addBlocker()`, `lazy.log.debug()`, `lazy.log.error()`, `lazy.log.warn()`, `this.#conn.execute()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `IOUtils.stat()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `(stat.size / 1048576).toFixed()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `ChromeUtils.now()`
- 条件付き依存: `if (markerData)` → `ChromeUtils.addProfilerMarker()`
- 参照: `e.message`, `e.stack`, `markerData.sizeLabel`, `markerData.startTime`, `stat.size`, `this.#asyncShutdownBlocker`, `this.#conn`, `this.databaseFilePath`
- XPCOM: `Services.profiler`

## ChatStore.#closeConnection()
- 位置: async L1254-1271
- 役割: 保留中の書き込みを終えてから接続を閉じ、終了ブロッカーを外す。
- 触るとき: 接続の閉じ方や終了時の書き込み漏れを調べるとき。
- 呼び出し先: `lazy.Sqlite.shutdown.removeBlocker()`, `lazy.log.debug()`, `lazy.log.warn()`, `this.#conn.close()`, `this.endStreamingWrites()`
- 参照: `e.message`, `this.#asyncShutdownBlocker`, `this.#conn`

## ChatStore.#ensureDatabase()
- 位置: async L1278-1334
- 役割: 接続とスキーマを一度だけ整える。壊れた DB は作り直す。
- 触るとき: DB が開けない・壊れた DB が消えるなどの起動時の挙動を変えるとき。どの呼び出しもここを通る。
- 呼び出し先: `Promise.withResolvers()`, `deferred.resolve()`, `e.errors?.some()`, `lazy.log.warn()`, `this.#initializeSchema()`, `this.#openConnection()`, `this.#removeDatabaseFiles()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `lazy.log.debug()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `this.#removeDatabaseFiles()`
- 条件付き依存: `if (this.#removeDatabaseOnStartup)` → `deferred.reject()`
- 条件付き依存: `if ( e.result == Cr.NS_ERROR_FILE_CORRUPTED || e.errors?.some(error => error.result == Ci.mozIStorageError.NOTADB) )` → `lazy.log.warn()`
- 条件付き依存: `if ( e.result == Cr.NS_ERROR_FILE_CORRUPTED || e.errors?.some(error => error.result == Ci.mozIStorageError.NOTADB) )` → `this.#removeDatabaseFiles()`
- 条件付き依存: `if (!this.#conn)` → `this.#openConnection()`
- 条件付き依存: `if (!this.#conn)` → `lazy.log.error()`
- 条件付き依存: `if (!this.#conn)` → `deferred.reject()`
- 参照: `Ci.mozIStorageError.NOTADB`, `Cr.NS_ERROR_FILE_CORRUPTED`, `deferred.promise`, `e.message`, `e.result`, `e.stack`, `error.result`, `this.#conn`, `this.#promiseConn`, `this.#removeDatabaseOnStartup`

## ChatStore.setSchemaVersion()
- 位置: async L1336-1338
- 役割: DB のスキーマ版を書き込む。
- 触るとき: 移行の完了時に版を更新する処理を調べるとき。
- 呼び出し先: `this.#conn.setSchemaVersion()`

## ChatStore.#initializeSchema()
- 位置: async L1340-1365
- 役割: DB の版を見て、新規作成・移行・何もしない、のいずれかを行う。
- 触るとき: 新しいスキーマ版を追加するとき、または版ずれで移行が走らない問題を調べるとき。
- 呼び出し先: `this.#conn.executeTransaction()`, `this.applyMigrations()`, `this.getDatabaseSchemaVersion()`, `this.setSchemaVersion()`
- 条件付き依存: `if (version > this.CURRENT_SCHEMA_VERSION)` → `this.setSchemaVersion()`
- 条件付き依存: `if (version == 0)` → `this.#createDatabaseEntities()`
- 条件付き依存: `if (version == 0)` → `this.#conn.setSchemaVersion()`
- 参照: `this.CURRENT_SCHEMA_VERSION`

## ChatStore.applyMigrations()
- 位置: async L1367-1375
- 役割: ChatMigrations の移行関数を順に、現在の版を渡して実行する。
- 触るとき: 移行の実行順や対象を変えるとき。
- 呼び出し先: `migration()`
- 参照: `this.#conn`

## ChatStore.#removeDatabaseFiles()
- 位置: async L1377-1401
- 役割: DB 本体と WAL・SHM ファイルを消す。失敗時は次回起動で消すよう印を残す。
- 触るとき: DB 初期化や破損時の作り直しの挙動を変えるとき。
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `lazy.log.debug()`, `lazy.log.warn()`, `this.#closeConnection()`
- 参照: `this.#removeDatabaseOnStartup`, `this.databaseFileName`, `this.databaseFilePath`

## ChatStore.#findConversationsWithMessages()
- 位置: async L1403-1421
- 役割: SQL で会話を読み、メッセージと LLM テレメトリの状態を補って返す。
- 触るとき: 会話の検索系処理に共通の読み込み手順を変えるとき。
- 呼び出し先: `lazy.log.error()`, `rows.map()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#getMessagesForConversations()`, `this.#hydrateTelemetryState()`
- 参照: `e.message`, `e.stack`

## ChatStore.#hydrateTelemetryState()
- 位置: async L1432-1465
- 役割: 読み込んだ会話にテレメトリのサンプリング状態を戻す。
- 触るとき: 再読み込み後にテレメトリのトリガーが発火しない問題を調べるとき。
- 呼び出し先: `conversations.map()`, `getUniformSamplingByConvIdsSql()`, `lazy.log.error()`, `probByConvId.get()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached( getUniformSamplingByConvIdsSql(conversations.length), conversations.map(c => c.id) ) .catch()`
- 参照: `c.id`, `conversation._telemetryUniformProbability`, `conversation._telemetryUniformSample`, `conversation.id`, `conversations.length`, `e.message`, `e.stack`

## ChatStore.markLLMTelemetryUnprocessed()
- 位置: async L1475-1499
- 役割: 会話の LLM テレメトリを未処理に戻す（無ければ作る）。
- 触るとき: テレメトリの再処理の対象を変えるとき。
- 呼び出し先: `lazy.log.error()`, `this.#conn .executeCached()`, `this.#conn .executeCached(MARK_LLM_TELEMETRY_UNPROCESSED, { conv_id: conversationId, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.updateLLMTelemetryRecord()
- 位置: async L1511-1546
- 役割: 会話の LLM テレメトリのプロンプトと確率を統合して保存し、処理済みフラグを更新する。
- 触るとき: テレメトリに記録する項目や統合の仕方を変えるとき。
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `lazy.log.error()`, `this.#conn .executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.findLLMTelemetryByConversationId()
- 位置: async L1554-1595
- 役割: 会話の LLM テレメトリ行を取り出し、JSON を展開して返す。無ければ null。
- 触るとき: テストやテレメトリの内容を確認するとき。
- 呼び出し先: `JSON.parse()`, `lazy.log.error()`, `rows[0].getResultByName()`, `this.#conn .executeCached()`, `this.#conn .executeCached(GET_LLM_TELEMETRY_BY_CONV_ID, { conv_id: conversationId, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`, `rows.length`

## ChatStore.markLLMTelemetryProcessed()
- 位置: async L1605-1633
- 役割: 処理したプロンプトごとに、そのターン番号を記録する。
- 触るとき: どのターンでテレメトリを送ったかの記録方法を変えるとき。
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `Object.fromEntries()`, `Object.keys()`, `Object.keys(telemetryPrompts).map()`, `lazy.log.error()`, `this.#conn .executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.getConversationsForTelemetry()
- 位置: async L1635-1658
- 役割: テレメトリ送信の対象になる会話の一覧を、ジョブと確率付きで返す。
- 触るとき: テレメトリ送信対象の条件や送る項目を変えるとき。
- 呼び出し先: `JSON.parse()`, `lazy.log.error()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached(GET_CONVERSATIONS_FOR_TELEMETRY) .catch()`, `this.#ensureDatabase()`
- 参照: `e.message`, `e.stack`

## ChatStore.#createDatabaseEntities()
- 位置: async L1660-1673
- 役割: 新規 DB に表と索引を一通り作る。
- 触るとき: 新しい表や索引を追加するとき（移行だけでなくここにも足す必要がある）。
- 呼び出し先: `this.#conn.execute()`

## ChatStore.#removeDatabaseOnStartup()
- 位置: L1675-1680
- 役割: 起動時に DB を消すべきかを示す設定値を読む。
- 触るとき: 起動時の DB 削除フラグの扱いを調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## ChatStore.#removeDatabaseOnStartup()
- 位置: L1682-1685
- 役割: 起動時に DB を消すかどうかの設定値を書き込む。
- 触るとき: DB 削除の要求が残り続ける問題を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.log.debug()`
- XPCOM: `Services.prefs`

## ChatStore.CONVERSATION_STATUS()
- 位置: L1687-1689
- 役割: 会話の状態（有効・アーカイブ・削除）の定数を返す。
- 触るとき: 会話状態の値を外から参照する箇所を確認するとき。

## ChatStore.CURRENT_SCHEMA_VERSION()
- 位置: L1691-1693
- 役割: このビルドが想定するスキーマの版を返す。
- 触るとき: スキーマ版を上げるとき、または移行の判定値を確認するとき。

## ChatStore.connection()
- 位置: L1695-1697
- 役割: 現在の SQLite 接続を返す。
- 触るとき: テストなどで DB を直接読むとき。
- 参照: `this.#conn`

## ChatStore.databaseFileName()
- 位置: L1699-1701
- 役割: DB ファイル名を返す。
- 触るとき: DB のファイル名を変えるとき、または削除対象を確かめるとき。

## ChatStore.databaseFilePath()
- 位置: L1703-1705
- 役割: プロファイル直下の DB ファイルの絶対パスを返す。
- 触るとき: DB の保存場所を変えるとき。
- 呼び出し先: `PathUtils.join()`
- 参照: `PathUtils.profileDir`, `this.databaseFileName`
