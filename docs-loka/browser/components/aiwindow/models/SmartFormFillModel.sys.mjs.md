# browser/components/aiwindow/models/SmartFormFillModel.sys.mjs

source: browser/components/aiwindow/models/SmartFormFillModel.sys.mjs
source-hash: d25ee50d4a54bdb64fa819b960c2f998c4142702
lines: 701

## <module>
- 役割: (未記入)

## startPendingValuesBatchRequests()
- 位置: L212-236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `generateFormValuesBatch()`, `generateFormValuesBatch(request, options).then()`, `options.signal?.removeEventListener()`, `pendingValuesBatchRequests.shift()`, `reject()`, `resolve()`, `startPendingValuesBatchRequests()`
- 参照: `pendingRequest.onAbort`, `pendingValuesBatchRequests.length`

## queueValuesBatchRequest()
- 位置: L247-275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `pendingValuesBatchRequests.push()`, `signal?.throwIfAborted()`, `startPendingValuesBatchRequests()`
- 条件付き依存: `if (signal)` → `signal.addEventListener()`
- 参照: `pendingRequest.onAbort`

## pendingRequest.onAbort()
- 位置: L261-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pendingValuesBatchRequests.indexOf()`, `pendingValuesBatchRequests.splice()`, `reject()`
- 参照: `signal.reason`

## tokenizeUrl()
- 位置: L372-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `urlTokenizer.encodeToken()`

## resolveUrlTokens()
- 位置: L386-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `expandUrlTokens()`, `stripUnresolvedUrlTokens()`

## generateFormValuesBatch()
- 位置: async L405-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `buildConversation()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `loadPrompt()`, `makeJSONSchemaBlob()`, `onDispatch()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `request.context.relevantTabs.map()`, `request.page.title.substring()`, `signal?.throwIfAborted()`, `tab.title.substring()`, `tokenizeUrl()`
- 参照: `MODEL_FEATURES.SMART_FORM_FILL`, `conversation.engine.model`, `request.candidates`, `request.context.memories`, `request.context.pageText`, `request.fields`, `request.page.url`, `tab.url`

## isRetryableRequestError()
- 位置: L485-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openAIEngine.isRetryableError()`

## classifyFields()
- 位置: async L499-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `buildConversation()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `loadPrompt()`, `makeJSONSchemaBlob()`, `onDispatch()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `request.page.title.substring()`, `signal?.throwIfAborted()`, `urlTokenizer.encodeToken()`
- 参照: `MODEL_FEATURES.SMART_FORM_FILL`, `conversation.engine.model`, `request.fields`, `request.page.url`

## findRelevantTabs()
- 位置: async L562-625
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Promise.all()`, `buildConversation()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `loadPrompt()`, `makeJSONSchemaBlob()`, `onDispatch()`, `openAIEngine.getFxAccountToken()`, `parseAndExtractJSON()`, `renderPrompt()`, `request.page.title.substring()`, `request.tabs.map()`, `signal?.throwIfAborted()`, `tab.title.substring()`, `urlTokenizer.encodeToken()`
- 参照: `MODEL_FEATURES.SMART_FORM_FILL`, `conversation.engine.model`, `request.fields`, `request.maxSelectedTabs`, `request.page.url`, `tab.url`

## generateFormValues()
- 位置: async L640-699
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `fulfilled .flatMap()`, `fulfilled .flatMap(({ value }) => value.fields ?? []) .map()`, `fulfilled.flatMap()`, `queueValuesBatchRequest()`, `request.fields.slice()`, `requests.push()`, `resolveUrlTokens()`, `results.filter()`, `signal?.throwIfAborted()`
- 条件付き依存: `if (tabUrl)` → `tabsUsed.add()`
- 参照: `field.value`, `fulfilled.length`, `request.fields.length`, `results.length`, `results[0].reason`, `value.fields`, `value.memories_used`, `value.tabs_used`
