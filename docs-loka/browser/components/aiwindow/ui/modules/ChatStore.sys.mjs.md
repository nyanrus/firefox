# browser/components/aiwindow/ui/modules/ChatStore.sys.mjs

source: browser/components/aiwindow/ui/modules/ChatStore.sys.mjs
source-hash: 580e3215ec51366d34ff35dc228a949d564531b3
lines: 1710

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## ChatStore.constructor()
- 位置: L174-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.obs.addObserver()`
- 参照: `this.#asyncShutdownBlocker`, `this.#lastRecordedSize`, `this.QueryInterface`
- XPCOM: `Services.obs`

## this.#asyncShutdownBlocker()
- 位置: async L175-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeConnection()`, `this.#sizeRecordTask?.finalize()`
- 参照: `this.#sizeRecordTask`

## ChatStore.observe()
- 位置: L194-200
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "idle-daily")` → `this.pruneDatabase().catch()`
- 条件付き依存: `if (topic === "idle-daily")` → `this.pruneDatabase()`
- 条件付き依存: `if (topic === "idle-daily")` → `lazy.log.error()`
- 参照: `e.message`, `e.stack`

## ChatStore.updateConversation()
- 位置: async L207-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `JSON.stringify()`, `URL.parse()`, `conversation.messages.map()`, `lazy.log.error()`, `this.#applyToolResults()`, `this.#conn .executeTransaction()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`, `this.#toMessageRow()`, `toJSONOrNull()`
- 参照: `conversation.activeBranchTipMessageId`, `conversation.createdDate`, `conversation.description`, `conversation.id`, `conversation.memoriesToggled`, `conversation.pageMeta`, `conversation.pageUrl`, `conversation.securityProperties`, `conversation.seenUrls`, `conversation.serpUrlsForAnonymousFetch`, `conversation.status`, `conversation.title`, `conversation.updatedDate`, `e.message`, `e.stack`, `pageUrl?.href`

## ChatStore.#toMessageRow()
- 位置: L254-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toJSONOrNull()`
- 参照: `m.content`, `m.createdDate`, `m.id`, `m.isActiveBranch`, `m.memoriesApplied`, `m.memoriesEnabled`, `m.memoriesFlagSource`, `m.modelId`, `m.ordinal`, `m.pageUrl?.href`, `m.params`, `m.parentMessageId`, `m.revisionRootMessageId`, `m.role`, `m.turnIndex`, `m.usage`, `m.webSearchQueries`

## ChatStore.persistStreamingMessage()
- 位置: L295-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(async () => { await this.#endStreamingEntry(previous); await this.updateConversation(conversation); })()`, `entry.ready.catch()`, `lazy.log.error()`, `this.#endStreamingEntry()`, `this.#streamingWrites.get()`, `this.#streamingWrites.set()`, `this.#writeStreamingMessage()`, `this.updateConversation()`
- 条件付き依存: `if (previous?.message === message)` → `previous.task.arm()`
- 参照: `conversation.id`, `e.message`, `e.stack`, `entry.ready`, `entry.task`, `lazy.DeferredTask`, `previous?.message`

## ChatStore.endStreamingWrites()
- 位置: async L339-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Promise.all()`, `entries.map()`, `this.#endStreamingEntry()`, `this.#streamingWrites.get()`, `this.#streamingWrites.values()`
- 条件付き依存: `if (convId === null)` → `this.#streamingWrites.clear()`
- 条件付き依存: `if (!(convId === null))` → `this.#streamingWrites.delete()`

## ChatStore.#endStreamingEntry()
- 位置: async L364-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `entry.task.finalize()`, `lazy.log.error()`
- 条件付き依存: `if (!flush)` → `entry.task.disarm()`
- 参照: `e.message`, `e.stack`, `entry.ready`

## ChatStore.#writeStreamingMessage()
- 位置: async L390-395
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#toMessageRow()`

## ChatStore.#applyToolResults()
- 位置: async L397-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `m.citations.forEach()`, `m.historyResults.forEach()`, `stripResolvedAssets()`, `toJSONOrNull()`, `toolResults.push()`
- 条件付き依存: `if (m.toolUIData)` → `toolResults.push()`
- 条件付き依存: `if (m.toolUIData)` → `toJSONOrNull()`
- 条件付き依存: `if (toolResults.length)` → `this.#conn.executeCached()`
- 参照: `TOOL_RESULT_TYPE.CITATIONS`, `TOOL_RESULT_TYPE.HISTORY_RESULTS`, `TOOL_RESULT_TYPE.TOOL_UI`, `conversation.messages`, `m.id`, `m.toolUIData`, `toolResults.length`

## ChatStore.deleteAllUrlsFromMessages()
- 位置: async L443-466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#conn .executeCached()`, `this.#conn .executeCached(REMOVE_ALL_SITE_URLS_FROM_MESSAGES) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.deleteUrlFromMessages()
- 位置: async L475-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#conn .executeCached()`, `this.#conn .executeCached(REMOVE_SITE_URL_FROM_MESSAGES, { page_url }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.findOldestConversations()
- 位置: async L506-535
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached(CONVERSATIONS_OLDEST, { limit: numberOfConversations, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.findRecentConversations()
- 位置: async L543-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached(CONVERSATIONS_MOST_RECENT, { limit: numberOfConversations, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.findConversationById()
- 位置: async L582-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#findConversationsWithMessages()`, `this.#findConversationsWithMessages( CONVERSATION_BY_ID, { conv_id: conversationId, } ).catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.findConversationsByDate()
- 位置: async L610-615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#findConversationsWithMessages()`

## ChatStore.findConversationsByURL()
- 位置: async L624-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#findConversationsWithMessages()`
- 参照: `pageUrl.href`

## ChatStore.findMessagesByDate()
- 位置: async L644-676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `endDate.getTime()`, `lazy.log.error()`, `parseMessageRows()`, `startDate.getTime()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`, `params.role`

## ChatStore.getMostRecentMessages()
- 位置: async L690-692
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.findMessagesByDate()`

## ChatStore.#escapeForLike()
- 位置: L694-699
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `searchString .replaceAll()`, `searchString .replaceAll(ESCAPE_CHAR, `${ESCAPE_CHAR}${ESCAPE_CHAR}`) .replaceAll()`, `searchString .replaceAll(ESCAPE_CHAR, `${ESCAPE_CHAR}${ESCAPE_CHAR}`) .replaceAll("%", `${ESCAPE_CHAR}%`) .replaceAll()`

## ChatStore.searchContent()
- 位置: async L713-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `rows.map()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#getMessagesForConversations()`
- 参照: `e.message`, `e.stack`, `params.role`, `rows.length`

## ChatStore.search()
- 位置: async L760-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `parseConversationRow()`, `row.getResultByName()`, `rows.map()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#escapeForLike()`, `this.#getMessagesForConversations()`
- 参照: `conv.matchingSnippet`, `e.message`, `e.stack`, `rows.length`

## ChatStore.chatHistoryView()
- 位置: async L802-826
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CONVERSATION_HISTORY.replace()`, `SORTS.find()`, `lazy.log.error()`, `parseChatHistoryViewRows()`, `sort.toUpperCase()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.getDbBytesInUse()
- 位置: async L834-840
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rows[0].getResultByName()`, `this.#conn.execute()`

## ChatStore.pruneDatabase()
- 位置: async L851-915
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`, `Math.max()`, `lazy.log.error()`, `oldestConversations.map()`, `this.#conn.execute()`, `this.#deleteConversationsByIds()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.findOldestConversations()`, `this.getDbBytesInUse()`, `this.recordDatabaseSizeNow()`
- 参照: `chat.id`, `e.message`, `e.stack`, `oldestConversations.length`, `this.databaseFilePath`

## ChatStore.#deleteConversationsByIds()
- 位置: async L924-934
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getDeleteConversationsByIdsSql()`, `ids.slice()`, `this.#conn.execute()`, `this.#conn.executeTransaction()`
- 参照: `chunk.length`, `ids.length`

## ChatStore.deleteMessages()
- 位置: async L941-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Promise.all()`, `chunk.map()`, `chunk.reduce()`, `chunks.push()`, `convs.add()`, `getDeleteEmptyConversationsSql()`, `getDeleteMessagesByIdsSql()`, `lazy.log.error()`, `messages.map()`, `messages.slice()`, `this.#conn.execute()`, `this.#conn.executeTransaction()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`, `this.endStreamingWrites()`
- 参照: `chunk.length`, `conversations.length`, `e.message`, `e.stack`, `m.convId`, `m.id`, `message.convId`, `messages.length`

## ChatStore.getDatabaseSize()
- 位置: async L998-1010
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.stat()`, `lazy.log.error()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`, `stats.size`, `this.databaseFilePath`

## ChatStore.deleteConversationById()
- 位置: async L1017-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#conn.execute()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`, `this.endStreamingWrites()`
- 参照: `e.message`, `e.stack`

## ChatStore.deleteConversationsByDateRange()
- 位置: async L1043-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `endDate.getTime()`, `lazy.log.error()`, `startDate.getTime()`, `this.#conn.execute()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.endStreamingWrites()`
- 参照: `e.message`, `e.stack`

## ChatStore.deleteAllConversations()
- 位置: async L1064-1077
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#conn.execute()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.endStreamingWrites()`
- 参照: `e.message`, `e.stack`

## ChatStore.destroyDatabase()
- 位置: async L1082-1092
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#promiseConn?.catch()`, `this.#recordDatabaseSizeValue()`, `this.#removeDatabaseFiles()`, `this.#sizeRecordTask?.disarm()`, `this.endStreamingWrites()`
- 参照: `this.#promiseConn`

## ChatStore.recordDatabaseSizeNow()
- 位置: async L1099-1102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordDatabaseSize()`, `this.#sizeRecordTask?.disarm()`

## ChatStore.#queueDatabaseSizeRecord()
- 位置: L1109-1115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#recordDatabaseSize()`, `this.#sizeRecordTask.arm()`
- 参照: `lazy.DeferredTask`, `this.#sizeRecordTask`

## ChatStore.#recordDatabaseSize()
- 位置: async L1117-1127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#recordDatabaseSizeValue()`, `this.getDatabaseSize()`
- 参照: `e.message`, `e.stack`

## ChatStore.#recordDatabaseSizeValue()
- 位置: L1129-1135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.chatStorage.set()`
- 参照: `this.#lastRecordedSize`

## ChatStore.getDatabaseSchemaVersion()
- 位置: async L1142-1148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.getSchemaVersion()`
- 条件付き依存: `if (!this.#conn)` → `this.#ensureDatabase()`
- 参照: `this.#conn`

## ChatStore.#getMessagesForConversations()
- 位置: async L1150-1202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `conversation.rehydrateCitationsPool()`, `conversation.rehydrateHistoryResultsPool()`, `conversations.forEach()`, `conversations.map()`, `conversations.reduce()`, `getConversationMessagesSql()`, `lazy.log.error()`, `parseMessageRows()`, `parseMessageRows(rows).forEach()`, `this.#conn .executeCached()`, `this.#conn .executeCached( getConversationMessagesSql(conversations.length), conversations.map(c => c.id) ) .catch()`
- 条件付き依存: `if (convs[message.convId])` → `lazy.CONFIRMATION_UI_TYPES.includes()`
- 条件付き依存: `if (convs[message.convId])` → `(byConv[message.convId] ??= []).push()`
- 参照: `c.id`, `conv.id`, `conversations.length`, `convs[convId].messages`, `e.message`, `e.stack`, `message.convId`, `message.isRestored`, `message.toolUIData?.properties?.actionType`, `message.toolUIData?.uiType`

## ChatStore.#openConnection()
- 位置: async L1204-1252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.profiler.IsActive()`, `lazy.Sqlite.openConnection()`, `lazy.Sqlite.shutdown.addBlocker()`, `lazy.log.debug()`, `lazy.log.error()`, `lazy.log.warn()`, `this.#conn.execute()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `IOUtils.stat()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `(stat.size / 1048576).toFixed()`
- 条件付き依存: `if (Services.profiler.IsActive())` → `ChromeUtils.now()`
- 条件付き依存: `if (markerData)` → `ChromeUtils.addProfilerMarker()`
- 参照: `e.message`, `e.stack`, `markerData.sizeLabel`, `markerData.startTime`, `stat.size`, `this.#asyncShutdownBlocker`, `this.#conn`, `this.databaseFilePath`
- XPCOM: `Services.profiler`

## ChatStore.#closeConnection()
- 位置: async L1254-1271
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Sqlite.shutdown.removeBlocker()`, `lazy.log.debug()`, `lazy.log.warn()`, `this.#conn.close()`, `this.endStreamingWrites()`
- 参照: `e.message`, `this.#asyncShutdownBlocker`, `this.#conn`

## ChatStore.#ensureDatabase()
- 位置: async L1278-1334
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.setSchemaVersion()`

## ChatStore.#initializeSchema()
- 位置: async L1340-1365
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.executeTransaction()`, `this.applyMigrations()`, `this.getDatabaseSchemaVersion()`, `this.setSchemaVersion()`
- 条件付き依存: `if (version > this.CURRENT_SCHEMA_VERSION)` → `this.setSchemaVersion()`
- 条件付き依存: `if (version == 0)` → `this.#createDatabaseEntities()`
- 条件付き依存: `if (version == 0)` → `this.#conn.setSchemaVersion()`
- 参照: `this.CURRENT_SCHEMA_VERSION`

## ChatStore.applyMigrations()
- 位置: async L1367-1375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `migration()`
- 参照: `this.#conn`

## ChatStore.#removeDatabaseFiles()
- 位置: async L1377-1401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.remove()`, `PathUtils.join()`, `lazy.log.debug()`, `lazy.log.warn()`, `this.#closeConnection()`
- 参照: `this.#removeDatabaseOnStartup`, `this.databaseFileName`, `this.databaseFilePath`

## ChatStore.#findConversationsWithMessages()
- 位置: async L1403-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `rows.map()`, `this.#conn.executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#getMessagesForConversations()`, `this.#hydrateTelemetryState()`
- 参照: `e.message`, `e.stack`

## ChatStore.#hydrateTelemetryState()
- 位置: async L1432-1465
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversations.map()`, `getUniformSamplingByConvIdsSql()`, `lazy.log.error()`, `probByConvId.get()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached( getUniformSamplingByConvIdsSql(conversations.length), conversations.map(c => c.id) ) .catch()`
- 参照: `c.id`, `conversation._telemetryUniformProbability`, `conversation._telemetryUniformSample`, `conversation.id`, `conversations.length`, `e.message`, `e.stack`

## ChatStore.markLLMTelemetryUnprocessed()
- 位置: async L1475-1499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.log.error()`, `this.#conn .executeCached()`, `this.#conn .executeCached(MARK_LLM_TELEMETRY_UNPROCESSED, { conv_id: conversationId, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.updateLLMTelemetryRecord()
- 位置: async L1511-1546
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `lazy.log.error()`, `this.#conn .executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`, `this.#queueDatabaseSizeRecord()`
- 参照: `e.message`, `e.stack`

## ChatStore.findLLMTelemetryByConversationId()
- 位置: async L1554-1595
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.log.error()`, `rows[0].getResultByName()`, `this.#conn .executeCached()`, `this.#conn .executeCached(GET_LLM_TELEMETRY_BY_CONV_ID, { conv_id: conversationId, }) .catch()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`, `rows.length`

## ChatStore.markLLMTelemetryProcessed()
- 位置: async L1605-1633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `Object.fromEntries()`, `Object.keys()`, `Object.keys(telemetryPrompts).map()`, `lazy.log.error()`, `this.#conn .executeCached()`, `this.#ensureDatabase()`, `this.#ensureDatabase().catch()`
- 参照: `e.message`, `e.stack`

## ChatStore.getConversationsForTelemetry()
- 位置: async L1635-1658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `lazy.log.error()`, `row.getResultByName()`, `rows.map()`, `this.#conn .executeCached()`, `this.#conn .executeCached(GET_CONVERSATIONS_FOR_TELEMETRY) .catch()`, `this.#ensureDatabase()`
- 参照: `e.message`, `e.stack`

## ChatStore.#createDatabaseEntities()
- 位置: async L1660-1673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#conn.execute()`

## ChatStore.#removeDatabaseOnStartup()
- 位置: L1675-1680
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## ChatStore.#removeDatabaseOnStartup()
- 位置: L1682-1685
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.log.debug()`
- XPCOM: `Services.prefs`

## ChatStore.CONVERSATION_STATUS()
- 位置: L1687-1689
- 役割: (未記入)
- 触るとき: (未記入)

## ChatStore.CURRENT_SCHEMA_VERSION()
- 位置: L1691-1693
- 役割: (未記入)
- 触るとき: (未記入)

## ChatStore.connection()
- 位置: L1695-1697
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#conn`

## ChatStore.databaseFileName()
- 位置: L1699-1701
- 役割: (未記入)
- 触るとき: (未記入)

## ChatStore.databaseFilePath()
- 位置: L1703-1705
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`
- 参照: `PathUtils.profileDir`, `this.databaseFileName`
