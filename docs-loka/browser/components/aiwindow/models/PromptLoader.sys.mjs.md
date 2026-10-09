# browser/components/aiwindow/models/PromptLoader.sys.mjs

source: browser/components/aiwindow/models/PromptLoader.sys.mjs
source-hash: e4231a54813980171fd67e1aa8ad6dff38b33f2c
lines: 629

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## getDefaultServiceType()
- 位置: L67-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `feature.startsWith()`
- 条件付き依存: `if (!(feature.startsWith("memories")))` → `feature.startsWith()`
- 参照: `SERVICE_TYPES.AGENT`, `SERVICE_TYPES.AI`, `SERVICE_TYPES.MEMORIES`

## loadV2Records()
- 位置: async L78-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `V2_RECORD_KINDS.has()`, `getRemoteRecords()`, `records.filter()`
- 参照: `r.kind`

## versionOf()
- 位置: L84-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parseVersion()`
- 参照: `record.version`, `version.major`, `version.minor`

## pickRecord()
- 位置: L90-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `matching.find()`, `parseVersion()`, `records.filter()`
- 条件付き依存: `if (requestedVersion)` → `matching.filter()`
- 条件付き依存: `if (requestedVersion)` → `parseVersion()`
- 条件付き依存: `if (!(requestedVersion))` → `Math.max()`
- 条件付き依存: `if (!(requestedVersion))` → `matching.map()`
- 条件付き依存: `if (!(requestedVersion))` → `matching.filter()`
- 条件付き依存: `if (!(requestedVersion))` → `versionOf()`
- 参照: `matching.length`, `parseVersion(r.version)?.major`, `r.model`, `r.version`, `requestedVersion.major`

## findModule()
- 位置: L117-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pickRecord()`
- 参照: `r.feature`, `r.kind`, `r.module`

## findParams()
- 位置: L128-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `candidates.find()`, `checkMajorVersion()`, `records.filter()`
- 参照: `r.feature`, `r.is_default`, `r.kind`, `r.model`, `r.modules`, `r.version`

## findSkill()
- 位置: L144-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pickRecord()`
- 参照: `r.kind`, `r.name`

## listSkills()
- 位置: L150-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...byName.values()].sort()`, `a.name.localeCompare()`, `byName.get()`, `byName.values()`, `versionOf()`
- 条件付き依存: `if ( !current || versionOf(r) > versionOf(current) || (versionOf(r) === versionOf(current) && current.model === GENERIC_MODEL_NAME && isExactModel) )` → `byName.set()`
- 参照: `b.name`, `current.model`, `r.kind`, `r.model`, `r.name`

## renderTemplate()
- 位置: L175-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `rendered.replaceAll()`

## buildChatSystemPrompt()
- 位置: async L200-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `GATED_CHAT_MODULES.get()`, `Intl.DateTimeFormat()`, `Intl.DateTimeFormat().resolvedOptions()`, `Services.prefs.getBoolPref()`, `findModule()`, `findParams()`, `getLocalIsoTime()`, `isoTimestamp.split()`, `listSkills()`, `listSkills(records, model) .map()`, `loadV2Records()`, `params.modules.some()`, `record?.prompts?.trim()`, `renderTemplate()`, `sections.join()`
- 条件付き依存: `if (text)` → `sections.push()`
- 条件付き依存: `if (!(text))` → `REQUIRED_CHAT_MODULES.has()`
- 参照: `Intl.DateTimeFormat().resolvedOptions().timeZone`, `MODEL_FEATURES.CHAT`, `Services.locale.appLocaleAsBCP47`, `entry.name`, `entry.version`, `err.clientReason`, `m.name`, `params.modules`, `params.version`
- XPCOM: `Services.locale` / `Services.prefs`

## getSkillPrompt()
- 位置: async L275-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^[A-Za-z0-9_-]+$/.test()`, `String()`, `String(name || "").trim()`, `findSkill()`, `loadV2Records()`
- 参照: `record.prompts`, `record?.prompts`

## renderMentionedUrls()
- 位置: L298-320
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lines.join()`, `lines.push()`, `mentionsWithUrl .map()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (groupId && groupId !== lastGroupId)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if (groupId && groupId !== lastGroupId)` → `lines.push()`

## buildBrowserContextPrompt()
- 位置: async L333-387
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fragments.join()`, `getRealTimeMapping()`, `loadV2Records()`, `renderPrompt()`
- 条件付き依存: `if (browserContextMapping.hasTabInfo)` → `securityProperties.setPrivateData()`
- 条件付き依存: `if (browserContextMapping.hasTabInfo)` → `findFragment()`
- 条件付き依存: `if (record?.prompts)` → `fragments.push()`
- 条件付き依存: `if (contextMentions?.length)` → `contextMentions.filter()`
- 条件付き依存: `if (mentionsWithUrl.length)` → `securityProperties.setPrivateData()`
- 条件付き依存: `if (mentionsWithUrl.length)` → `renderMentionedUrls()`
- 条件付き依存: `if (mentionsWithUrl.length)` → `findFragment()`
- 参照: `browserContextMapping.contextUrls`, `browserContextMapping.description`, `browserContextMapping.hasTabInfo`, `browserContextMapping.title`, `browserContextMapping.url`, `contextMentions?.length`, `fragments.length`, `mention.url`, `mentionsWithUrl.length`, `record.prompts`, `record?.prompts`

## findFragment()
- 位置: L347-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `findModule()`

## selectFeatureConfig()
- 位置: async L405-449
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`, `allRecords.filter()`, `allRecords.some()`, `getRemoteRecords()`, `selectMainConfig()`
- 参照: `err.clientReason`, `featureConfigs.length`, `opts.majorVersionOverride`, `opts.modelChoiceIdOverride`, `r.feature`, `r.kind`
- XPCOM: `Services.prefs`

## buildEngineForFeature()
- 位置: async L459-509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CHAT_MODEL_FALLBACK_FEATURES.has()`, `Services.prefs.getStringPref()`, `getDefaultServiceType()`, `openAIEngine.build()`, `openAIEngine.resolveEndpointConfig()`, `selectFeatureConfig()`
- 条件付き依存: `if (typeof parameters === "string")` → `JSON.parse()`
- 条件付き依存: `if ( model === GENERIC_MODEL_NAME && CHAT_MODEL_FALLBACK_FEATURES.has(feature) )` → `selectFeatureConfig()`
- 参照: `MODEL_FEATURES.AGENT_MONITOR`, `MODEL_FEATURES.AITAB`, `MODEL_FEATURES.CHAT`, `MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION`, `MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION_STARTER`, `chatConfig.model`, `mainConfig.model`, `mainConfig.parameters`, `mainConfig.purpose`, `mainConfig.service_type`, `opts.flowId`, `opts.modelChoiceIdOverride`
- XPCOM: `Services.prefs`

## buildConversation()
- 位置: async L520-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildEngineForFeature()`

## loadPrompt()
- 位置: async L541-575
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `selectFeatureConfig()`
- 条件付き依存: `if (customPromptsRaw)` → `JSON.parse()`
- 条件付き依存: `if (opts.module)` → `loadPromptV2()`
- 条件付き依存: `if (feature === MODEL_FEATURES.CHAT)` → `buildChatSystemPrompt()`
- 参照: `MODEL_FEATURES.CHAT`, `err.clientReason`, `mainConfig.prompts`, `mainConfig.version`, `opts.model`, `opts.module`
- XPCOM: `Services.prefs`

## loadPromptV2()
- 位置: async L584-628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `findModule()`, `findParams()`, `loadV2Records()`, `moduleRecord.prompts.trim()`, `paramsRecord.modules?.find()`
- 参照: `err.clientReason`, `m.name`, `moduleRecord?.prompts`, `opts.model`, `opts.module`, `paramsRecord.model`, `paramsRecord.modules?.find(m => m.name === opts.module)?.version`, `paramsRecord.version`
- XPCOM: `Services.prefs`
