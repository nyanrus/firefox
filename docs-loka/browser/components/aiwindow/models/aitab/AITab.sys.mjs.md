# browser/components/aiwindow/models/aitab/AITab.sys.mjs

source: browser/components/aiwindow/models/aitab/AITab.sys.mjs
source-hash: a2698912c7966ac6d1bd9744dd7234aeb8cd3114
lines: 1624

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `JSON.parse()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`, `prefValue.trim()`

## AITab.loadAssets()
- 位置: async L341-345
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#loadPackagedCatalog()`, `AITab.#makeEnv()`
- 参照: `lazy.overrideCatalog`

## AITab.buildSurface()
- 位置: L359-454
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#checkBindings()`, `AITab.#checkBoundArrays()`, `AITab.#checkRefs()`, `AITab.#propsOf()`, `Array.isArray()`, `components.filter()`, `components.map()`, `validator.validate()`
- 条件付き依存: `if (typeof id != "string" || !id)` → `errors.push()`
- 条件付き依存: `if (!(typeof id != "string" || !id))` → `idSet.has()`
- 条件付き依存: `if (idSet.has(id))` → `errors.push()`
- 条件付き依存: `if (!(idSet.has(id)))` → `idSet.add()`
- 条件付き依存: `if (roots.length !== 1)` → `errors.push()`
- 条件付き依存: `if (roots[0].component !== ROOT_COMPONENT)` → `errors.push()`
- 条件付き依存: `if (!validator)` → `errors.push()`
- 条件付き依存: `if (!valid)` → `errors.push()`
- 参照: `c?.id`, `comp.component`, `comp.id`, `comp?.children`, `comp?.component`, `comp?.header`, `comp?.id`, `env.catalog`, `env.catalog.components`, `env.validators`, `errors.length`, `roots.length`, `roots[0].component`, `surface.dataModel`, `surface?.components`

## AITab.#loadPackagedCatalog()
- 位置: L461-471
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `fetch(COMPONENT_SCHEMA_URL) .then(r => r.json()) .catch()`
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `fetch(COMPONENT_SCHEMA_URL) .then()`
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `fetch()`
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `r.json()`
- 参照: `AITab.#packagedCatalogPromise`

## AITab.#makeEnv()
- 位置: L482-503
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 参照: `catalog.$defs`, `catalog.components`, `lazy.JsonSchema.Validator`

## AITab.#checkRefs()
- 位置: L515-537
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof value == "string")` → `idSet.has()`
- 条件付き依存: `if (!idSet.has(value))` → `errors.push()`
- 条件付き依存: `if (!(typeof value == "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.#checkRefs()`
- 条件付き依存: `if ( typeof value == "object" && typeof value.componentId == "string" )` → `idSet.has()`
- 条件付き依存: `if (!idSet.has(value.componentId))` → `errors.push()`
- 参照: `value.componentId`

## AITab.#checkBindings()
- 位置: L550-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#checkBindings()`, `Array.isArray()`, `Object.keys()`, `Object.values()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.#checkBindings()`
- 条件付き依存: `if (keys.length === 1 && typeof value.path == "string")` → `value.path.startsWith()`
- 条件付き依存: `if (keys.length === 1 && typeof value.path == "string")` → `AITab.#resolvePath()`
- 条件付き依存: `if ( value.path.startsWith("/") && AITab.#resolvePath(dataModel, value.path) === undefined )` → `errors.push()`
- 参照: `keys.length`, `value.path`

## AITab.#propsOf()
- 位置: L584-589
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `props.component`, `props.id`

## AITab.#resolvePath()
- 位置: L600-610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pointer.slice()`, `pointer.slice(1).split()`, `seg.replace()`, `seg.replace(/~1/g, "/").replace()`

## AITab.#isBinding()
- 位置: L619-627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.keys()`
- 参照: `Object.keys(v).length`, `v.path`

## AITab.#resolveDef()
- 位置: L636-642
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (schema && typeof schema.$ref == "string")` → `schema.$ref.replace()`
- 参照: `catalog.$defs`, `schema.$ref`

## AITab.#itemValidator()
- 位置: L652-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `cache.getOrInsertComputed()`
- 参照: `catalog.$defs`, `lazy.JsonSchema.Validator`

## AITab.#checkBoundArrays()
- 位置: L683-742
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#resolveDef()`, `Array.isArray()`
- 条件付き依存: `if (Array.isArray(schema.oneOf))` → `schema.oneOf.find()`
- 条件付き依存: `if (Array.isArray(schema.oneOf))` → `AITab.#isBinding()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `value.path.startsWith()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `AITab.#resolvePath()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `Array.isArray()`
- 条件付き依存: `if (!Array.isArray(arr))` → `errors.push()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `AITab.#itemValidator()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `arr.forEach()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `iv.validate()`
- 条件付き依存: `if (!valid)` → `errors.push()`
- 条件付き依存: `if (props && typeof value == "object" && !Array.isArray(value))` → `Object.entries()`
- 条件付き依存: `if (k in value)` → `AITab.#checkBoundArrays()`
- 参照: `arrayBranch.items`, `s.items`, `s.type`, `schema.oneOf`, `schema.properties`, `value.path`

## AITab.buildViewerURL()
- 位置: L752-754
- 役割: (未記入)
- 触るとき: (未記入)

## AITab.generateAITab()
- 位置: async L788-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#capped()`, `AITab.#collectSources()`, `AITab.#generateStructuredSurface()`, `AITab.#hydrateFavicons()`, `AITab.#mergeSources()`, `AITab.#slugify()`, `AITab.#titleFromSurface()`, `Array.isArray()`, `Date.now()`, `lazy.console.error()`, `lazy.l10n.formatValueSync()`, `modifySlug.trim()`, `rawContent.trim()`, `toolConversation .save()`, `toolConversation .save() .catch()`, `toolConversation.addSeenUrls()`, `toolConversation.addSerpUrlsForAnonymousFetch()`, `toolConversation.securityProperties.commit()`, `toolConversation.securityProperties.setPrivateData()`, `toolConversation.securityProperties.setUntrustedInput()`, `urlList.filter()`, `urlList.filter(url => typeof url == "string").slice()`
- 条件付き依存: `if (slug)` → `AITab.#loadPageToModify()`
- 条件付き依存: `if (prior)` → `AITab.#capped()`
- 参照: `conversation?.seenUrls`, `conversation?.serpUrlsForAnonymousFetch`, `prior.error`, `prior.page.slug`, `prior?.conversation`, `prior?.page.context?.creationPrompt`, `prior?.page.context?.urlsUsed`, `prior?.page.title`, `signal?.aborted`, `sources.error`, `structured.conversation`, `structured.error`, `structured.surface`, `toolConversation.id`, `toolConversation.updatedDate`, `urls.length`, `urlsUsed[0].title`

## AITab.#capped()
- 位置: L943-947
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `text.trim()`, `text.trim().slice()`

## AITab.#collectSources()
- 位置: async L964-1040
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#getPageImage()`, `Math.floor()`, `headLines.join()`, `lazy.GetPageContent.getTabWithURL()`, `lazy.GetPageContent.isContentAllowed()`, `sourceParts.join()`, `sourceParts.push()`, `text.slice()`, `urls.entries()`, `urlsUsed.push()`
- 条件付き依存: `if (urls.length)` → `lazy.GetPageContent.getPageContent()`
- 条件付き依存: `if (urls.length)` → `contents.some()`
- 条件付き依存: `if (imageUrl)` → `headLines.push()`
- 条件付き依存: `if (rawText)` → `sourceParts.push()`
- 条件付き依存: `if (rawText)` → `rawText.slice()`
- 参照: `contents[index]?.content`, `result.ok`, `signal?.aborted`, `tab?.label`, `text.length`, `urls.length`

## AITab.#loadPageToModify()
- 位置: async L1057-1088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AITabStore.getBySlug()`, `lazy.console.error()`
- 条件付き依存: `if (page?.toolConvId)` → `lazy.ConversationStore.findConversationById()`
- 参照: `conversation?.id`, `page.convId`, `page.toolConvId`, `page?.toolConvId`, `priorConversation?.messageCount`

## AITab.#mergeSources()
- 位置: L1099-1108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.isArray()`, `byUrl.set()`, `byUrl.values()`, `previous.map()`
- 参照: `previous.length`, `source.url`, `source?.url`

## AITab.#titleFromSurface()
- 位置: L1117-1132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(surface?.components || []).find()`
- 条件付き依存: `if (title && typeof title == "object" && typeof title.path == "string")` → `title.path.startsWith()`
- 条件付き依存: `if (title && typeof title == "object" && typeof title.path == "string")` → `AITab.#resolvePath()`
- 参照: `c?.component`, `header?.title`, `surface.dataModel`, `surface?.components`, `title.path`

## AITab.#getPageImage()
- 位置: async L1141-1152
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PlacesUtils.history .fetch()`, `lazy.PlacesUtils.history .fetch(url, { includeMeta: true }) .catch()`, `lazy.console.debug()`
- 参照: `pageInfo.previewImageURL.href`, `pageInfo?.previewImageURL`

## AITab.#hydrateFavicons()
- 位置: async L1171-1224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `faviconByHref.get()`, `faviconByHref.has()`, `itemsOf()`, `linkItems.push()`
- 条件付き依存: `if (!faviconByHref.has(item.href))` → `faviconByHref.set()`
- 条件付き依存: `if (!faviconByHref.has(item.href))` → `AITab.#getFaviconURL()`
- 参照: `component.items`, `component.references?.items`, `component?.component`, `item.favicon`, `item.href`, `item?.sources?.items`, `signal?.aborted`, `surface?.components`, `surface?.dataModel`

## itemsOf()
- 位置: L1173-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#isBinding()`, `Array.isArray()`
- 条件付き依存: `if (AITab.#isBinding(value))` → `value.path.startsWith()`
- 条件付き依存: `if (AITab.#isBinding(value))` → `AITab.#resolvePath()`
- 参照: `value.path`

## AITab.#getFaviconURL()
- 位置: async L1233-1243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`, `lazy.console.debug()`
- 参照: `favicon?.uri?.spec`
- XPCOM: `Services.io`

## AITab.parsePageConfig()
- 位置: L1253-1274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#parseJsonSpan()`, `lazy.console.error()`, `text.indexOf()`, `text.slice()`

## AITab.expandSurfaceUrlTokens()
- 位置: L1290-1331
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.expandSurfaceUrlTokens()`, `Array.isArray()`, `LINK_FIELDS.has()`, `Object.entries()`
- 条件付き依存: `if (typeof value == "string")` → `stripUnresolvedUrlTokens()`
- 条件付き依存: `if (typeof value == "string")` → `expandUrlTokens()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map(item => AITab.expandSurfaceUrlTokens(item, urlTokenizer, recursionDepth + 1) ) .filter()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.expandSurfaceUrlTokens()`
- 条件付き依存: `if (LINK_FIELDS.has(key))` → `urlTokenizer.resolveExactToken()`
- 条件付き依存: `if (key == "href")` → `lazy.console.warn()`
- 参照: `urlTokenizer.tokenToUrl`

## AITab.tokenizeSurfaceUrls()
- 位置: L1345-1373
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.tokenizeSurfaceUrls()`, `Array.isArray()`, `LINK_FIELDS.has()`, `Object.entries()`, `urlTokenizer.formatToken()`
- 条件付き依存: `if (typeof value == "string")` → `urlTokenizer.tokenizeText()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map(item => AITab.tokenizeSurfaceUrls(item, urlTokenizer, recursionDepth + 1) ) .filter()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.tokenizeSurfaceUrls()`

## AITab.#tokenizedMessages()
- 位置: L1385-1399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.parsePageConfig()`, `AITab.tokenizeSurfaceUrls()`, `JSON.stringify()`, `conversation.getMessagesInChatCompletionsFormat()`, `conversation.getMessagesInChatCompletionsFormat().map()`, `urlTokenizer.tokenizeText()`
- 参照: `message.content`, `message.role`

## AITab.#generateStructuredSurface()
- 位置: async L1419-1528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AITab.#resolvePromptSet()`, `AITab.#schemaText()`, `AITab.#tokenizedMessages()`, `AITab.buildSurface()`, `AITab.expandSurfaceUrlTokens()`, `AITab.loadAssets()`, `AITab.parsePageConfig()`, `JSON.stringify()`, `conversation.addAssistantMessage()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `lazy.console.debug()`, `lazy.console.error()`, `lazy.openAIEngine.getFxAccountToken()`, `lazy.renderPrompt()`, `response?.finalOutput?.trim()`, `text.slice()`, `userParts.join()`
- 条件付き依存: `if (sourceText)` → `userParts.push()`
- 条件付き依存: `if (sourceText)` → `lazy.renderPrompt()`
- 条件付き依存: `if (modifyInstructions)` → `userParts.push()`
- 条件付き依存: `if (priorConversation)` → `JSON.stringify()`
- 条件付き依存: `if (history.length > MAX_HISTORY_CHARS)` → `lazy.console.warn()`
- 条件付き依存: `if (!parsed)` → `lazy.console.error()`
- 条件付き依存: `if (!result.ok)` → `lazy.console.error()`
- 参照: `error?.message`, `history.length`, `result.errors`, `result.ok`, `result.surface`, `signal?.aborted`, `text?.length`, `userParts.length`

## AITab.#resolvePromptSet()
- 位置: async L1543-1561
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.loadPrompt()`
- 条件付き依存: `if (conversation)` → `lazy.buildEngineForFeature()`
- 条件付き依存: `if (!(conversation))` → `lazy.buildConversation()`
- 参照: `conversation.engine`, `conversation.parameters`, `lazy.MODEL_FEATURES.AITAB`

## AITab.#schemaText()
- 位置: L1573-1585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `parts.join()`, `parts.push()`
- 条件付き依存: `if (catalog.$defs)` → `parts.push()`
- 条件付き依存: `if (catalog.$defs)` → `JSON.stringify()`
- 参照: `catalog.$defs`, `catalog.components`

## AITab.#parseJsonSpan()
- 位置: L1594-1605
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `text.indexOf()`, `text.lastIndexOf()`, `text.slice()`

## AITab.#slugify()
- 位置: L1613-1622
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `title .toLowerCase()`, `title .toLowerCase() .replace()`, `title .toLowerCase() .replace(/[^a-z0-9]+/g, "_") .replace()`, `title .toLowerCase() .replace(/[^a-z0-9]+/g, "_") .replace(/^_+|_+$/g, "") .slice()`
