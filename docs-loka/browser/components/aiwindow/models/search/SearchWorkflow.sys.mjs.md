# browser/components/aiwindow/models/search/SearchWorkflow.sys.mjs

source: browser/components/aiwindow/models/search/SearchWorkflow.sys.mjs
source-hash: 8c613a4f954a55ab47f7a7b4218e10a6efeedfc6
lines: 1116

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `console.createInstance()`

## resultIdFor()
- 位置: L270-272
- 役割: (未記入)
- 触るとき: (未記入)

## normalizeAndTruncateText()
- 位置: L287-299
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `collapsed.slice()`, `text.replace()`, `text.replace(/\s+/g, " ").trim()`
- 参照: `collapsed.length`

## isValidHttpUrl()
- 位置: L309-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`
- 参照: `parsed?.protocol`

## buildUserMessage()
- 位置: L329-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context.trim()`, `lines.join()`, `lines.push()`, `resultIdFor()`, `results.forEach()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (context && context.trim())` → `lines.push()`
- 条件付き依存: `if (snippet)` → `lines.push()`
- 参照: `result.snippet`, `result.title`, `result.url`

## validateSearchAnswer()
- 位置: L359-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.JsonSchema.validate()`, `parsed.answer.trim()`
- 参照: `SEARCH_ANSWER_SCHEMA.schema`, `parsed.answer`, `parsed.confidence`, `parsed.could_answer`

## generateAnswer()
- 位置: async L407-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(Array.isArray(ids) ? ids : []) .map()`, `(Array.isArray(ids) ? ids : []) .map(id => idToUrl.get(id)) .filter()`, `Array.isArray()`, `JSON.parse()`, `Promise.all()`, `String()`, `buildUserMessage()`, `conversation.addAssistantMessage()`, `conversation.addToolMessage()`, `conversation.addUserMessage()`, `conversation.receiveResponse()`, `conversation.run()`, `conversation.runWithGenerator()`, `conversation.setSystemMessage()`, `idToUrl.get()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `pageReadCalls.map()`, `parseAndExtractJSON()`, `pendingToolCalls.filter()`, `readPage()`, `renderPrompt()`, `resultIdFor()`, `results.map()`, `texts.join()`
- 参照: `JSON.parse(call.function.arguments || "{}").result_ids`, `MODEL_FEATURES.SEARCH_ANSWER_GENERATION`, `assistantMessage.content`, `call.function.arguments`, `call.function.name`, `call.function?.name`, `call.id`, `conversation.id`, `pageReadCalls.length`, `result.url`, `signal?.aborted`

## failure()
- 位置: L524-534
- 役割: (未記入)
- 触るとき: (未記入)

## fastFailure()
- 位置: L542-548
- 役割: (未記入)
- 触るとき: (未記入)

## answersFailure()
- 位置: L557-563
- 役割: (未記入)
- 触るとき: (未記入)

## shouldCallSearchHandoff()
- 位置: L565-567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.currentTurnIndex()`
- 参照: `conversation._searchTheWebTurn`

## runSearchTheWeb()
- 位置: async L583-605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.securityProperties.setPrivateData()`, `conversation.securityProperties.setUntrustedInput()`, `runAnswersSearch()`, `runFastSearch()`, `runGroundedSearch()`, `selectSearchTheWebPath()`, `shouldCallSearchHandoff()`
- 参照: `SEARCH_THE_WEB_PATH.ANSWERS`, `SEARCH_THE_WEB_PATH.FAST`

## recordAnswerCitations()
- 位置: L620-648
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `conversation.addCitations()`, `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `isValidHttpUrl()`, `records.map()`, `records.push()`, `seen.add()`, `seen.has()`
- 参照: `citation.title`, `citation.url`, `citation?.url`, `records.length`

## requestAnswer()
- 位置: async L665-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(response?.finalOutput ?? "").trim()`, `answer.slice()`, `engine.run()`, `openAIEngine.build()`, `openAIEngine.getFxAccountToken()`, `recordAnswerCitations()`
- 参照: `MODEL_FEATURES.SEARCH_ANSWERS`, `SERVICE_TYPES.SW_ANSWER`, `answer.length`, `conversation.id`, `response?.finalOutput`, `response?.providerSpecificFields?.citations`, `signal?.aborted`

## answerAsStream()
- 位置: async L718-736
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `chunks.entries()`, `text.match()`
- 条件付き依存: `if (index)` → `lazy.setTimeout()`
- 参照: `chunks.length`, `signal?.aborted`

## runAnswersSearch()
- 位置: async L752-782
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `answerAsStream()`, `answersFailure()`, `conversation.currentTurnIndex()`, `lazy.console.error()`, `lazy.console.log()`, `query.trim()`, `requestAnswer()`
- 条件付き依存: `if (typeof query !== "string" || !query.trim())` → `answersFailure()`
- 参照: `conversation._searchTheWebTurn`, `e.message`, `readUrls.length`, `toolParams?.query`

## recordFastSearchTelemetry()
- 位置: L794-814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.searchTheWeb.record()`, `Math.round()`
- 参照: `conversation.id`, `conversation.messageCount`, `stats.error`, `stats.httpStatus`, `stats.processing`, `stats.retrieval`, `stats.retrieved`, `stats.returned`, `stats.snippetChars`, `stats.snippetCharsDropped`

## runFastSearch()
- 位置: async L832-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.now()`, `recordFastSearchTelemetry()`, `runFastSearchFlow()`
- 参照: `SEARCH_TELEMETRY_ERRORS.INTERNAL_ERROR`, `stats.error`

## runFastSearchFlow()
- 位置: async L872-966
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `conversation.addCitations()`, `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `conversation.currentTurnIndex()`, `fastFailure()`, `isValidHttpUrl()`, `kept.map()`, `lazy.console.error()`, `lazy.console.log()`, `normalizeAndTruncateText()`, `provider.search()`, `query.trim()`, `retrieved .filter()`, `retrieved .filter( item => isValidHttpUrl(item?.url) && item?.snippet?.length > MIN_SNIPPET_LENGTH ) .slice()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (typeof query !== "string" || !query.trim())` → `fastFailure()`
- 条件付き依存: `if (!kept.length)` → `fastFailure()`
- 参照: `SEARCH_TELEMETRY_ERRORS.INVALID_QUERY`, `SEARCH_TELEMETRY_ERRORS.NO_RESULTS`, `SEARCH_TELEMETRY_ERRORS.RETRIEVAL_FAILED`, `conversation._searchTheWebTurn`, `e.message`, `e?.httpStatus`, `e?.searchErrorCategory`, `item.snippet`, `item.title`, `item.url`, `item?.snippet?.length`, `item?.url`, `kept.length`, `response.results`, `response.status`, `retrieved.length`, `snippet.droppedChars`, `snippet.text`, `snippet.text.length`, `stats.error`, `stats.httpStatus`, `stats.processing`, `stats.retrieval`, `stats.retrieved`, `stats.returned`, `stats.snippetChars`, `stats.snippetCharsDropped`, `toolParams?.query`

## runGroundedSearch()
- 位置: async L983-1115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `conversation.addCitations()`, `conversation.addSeenUrls()`, `conversation.addSerpUrlsForAnonymousFetch()`, `conversation.currentTurnIndex()`, `failure()`, `generateAnswer()`, `isValidHttpUrl()`, `lazy.console.error()`, `lazy.console.log()`, `new Date().toISOString()`, `new Date().toISOString().slice()`, `openAIEngine.getFxAccountToken()`, `provider.search()`, `query.trim()`, `readUrls.map()`, `results.filter()`, `results.map()`, `titlesByUrl.get()`, `validateSearchAnswer()`
- 条件付き依存: `if (typeof query !== "string" || !query.trim())` → `failure()`
- 条件付き依存: `if (!searchedUrls.length)` → `failure()`
- 参照: `ExaSearchProvider.MAX_RESULTS`, `conversation._searchTheWebTurn`, `e.message`, `item.title`, `item.url`, `item?.url`, `readUrls.length`, `response.results`, `searchedUrls.length`, `toolParams.context`, `toolParams?.context`, `toolParams?.query`, `validated.could_answer`

## readPage()
- 位置: async L1021-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Services.prefs.getIntPref()`, `fetchableSet.has()`, `fresh.forEach()`, `fresh.map()`, `perUrl.flat()`, `readSet.add()`, `readSet.has()`, `readUrls.push()`, `requestedUrls .filter()`, `requestedUrls .filter(url => fetchableSet.has(url) && !readSet.has(url)) .slice()`
- 参照: `fresh.length`, `readUrls.length`
- XPCOM: `Services.prefs`

## readOne()
- 位置: async L1046-1072
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GetPageContent.getPageContentText()`, `Promise.race()`, `controller.abort()`, `fetchPromise.catch()`, `lazy.clearTimeout()`, `lazy.console.warn()`, `lazy.setTimeout()`, `resolve()`
- 参照: `controller.signal`
