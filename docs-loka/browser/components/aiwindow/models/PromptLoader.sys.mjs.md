# browser/components/aiwindow/models/PromptLoader.sys.mjs

source: browser/components/aiwindow/models/PromptLoader.sys.mjs
source-hash: e4231a54813980171fd67e1aa8ad6dff38b33f2c
lines: 629

## <module>
- 役割: Remote Settings のレコードからプロンプト本文、モデル設定、会話の生成を組み立てる PromptLoader。チャットのプロンプトは v2 のモジュール群から組み、その他の機能は v1 の設定レコードを読む。
- 呼び出し先: `Object.freeze()`

## getDefaultServiceType()
- 位置: L67-74
- 役割: 機能名の接頭辞から、記憶用・エージェント用・既定の AI のサービス種別を返す。
- 触るとき: 機能を新しく追加して課金や利用区分の種別が合わないとき。
- 呼び出し先: `feature.startsWith()`
- 条件付き依存: `if (!(feature.startsWith("memories")))` → `feature.startsWith()`
- 参照: `SERVICE_TYPES.AGENT`, `SERVICE_TYPES.AI`, `SERVICE_TYPES.MEMORIES`

## loadV2Records()
- 位置: async L78-81
- 役割: Remote Settings の全レコードから kind が module・skill・params のものだけを返す。
- 触るとき: v2 レコードの種類を増やす、または読み込み対象を絞るとき。
- 呼び出し先: `V2_RECORD_KINDS.has()`, `getRemoteRecords()`, `records.filter()`
- 参照: `r.kind`

## versionOf()
- 位置: L84-88
- 役割: レコードの version(例 1.1)を major*1000000+minor の数値にし、解釈できなければ 0 を返す。
- 触るとき: 版の比較規則を変えるとき。
- 呼び出し先: `parseVersion()`
- 参照: `record.version`, `version.major`, `version.minor`

## pickRecord()
- 位置: L90-115
- 役割: 条件に合うレコードの中から、指定の major 版、無ければ最大版を選び、モデル名一致、汎用モデルの順で 1 件返す。
- 触るとき: レコードの版選択やモデルの優先順位を変えるとき。
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
- 役割: 機能・モジュール名・モデル・版を指定してモジュールのレコードを探す。
- 触るとき: モジュールの解決が効かず prompt が欠けるとき。
- 呼び出し先: `pickRecord()`
- 参照: `r.feature`, `r.kind`, `r.module`

## findParams()
- 位置: L128-142
- 役割: 機能の params レコードを、対応する major 版とモジュール一覧を持つものに絞り、モデル一致、汎用、既定の順で返す。
- 触るとき: 機能ごとのモデルの選び方や版の互換規則を変えるとき。
- 呼び出し先: `Array.isArray()`, `candidates.find()`, `checkMajorVersion()`, `records.filter()`
- 参照: `r.feature`, `r.is_default`, `r.kind`, `r.model`, `r.modules`, `r.version`

## findSkill()
- 位置: L144-148
- 役割: 名前と（任意で）モデルから skill レコードを探す。
- 触るとき: スキルの解決規則を変えるとき。
- 呼び出し先: `pickRecord()`
- 参照: `r.kind`, `r.name`

## listSkills()
- 位置: L150-173
- 役割: 指定モデルか汎用モデルの skill を名前ごとに最新版 1 件にまとめ、名前順に返す。
- 触るとき: システムプロンプトに載るスキル一覧の内容を変えるとき。
- 呼び出し先: `[...byName.values()].sort()`, `a.name.localeCompare()`, `byName.get()`, `byName.values()`, `versionOf()`
- 条件付き依存: `if ( !current || versionOf(r) > versionOf(current) || (versionOf(r) === versionOf(current) && current.model === GENERIC_MODEL_NAME && isExactModel) )` → `byName.set()`
- 参照: `b.name`, `current.model`, `r.kind`, `r.model`, `r.name`

## renderTemplate()
- 位置: L175-181
- 役割: テンプレート中の {名前} を値で置き換える(値が無ければ空文字)。
- 触るとき: プロンプトの置換変数を追加するとき。
- 呼び出し先: `Object.entries()`, `rendered.replaceAll()`

## buildChatSystemPrompt()
- 位置: async L200-264
- 役割: チャットの params の manifest 順に識別やレスポンス規則などのモジュールを集め、スキル一覧・ロケール・時刻を埋めて返す。必須モジュールが欠けると promptLoadFailure を投げる。
- 触るとき: チャットのシステムプロンプトの構成や順序を変えるとき、または「Missing required chat module」の例外を調べるとき。
- 呼び出し先: `GATED_CHAT_MODULES.get()`, `Intl.DateTimeFormat()`, `Intl.DateTimeFormat().resolvedOptions()`, `Services.prefs.getBoolPref()`, `findModule()`, `findParams()`, `getLocalIsoTime()`, `isoTimestamp.split()`, `listSkills()`, `listSkills(records, model) .map()`, `loadV2Records()`, `params.modules.some()`, `record?.prompts?.trim()`, `renderTemplate()`, `sections.join()`
- 条件付き依存: `if (text)` → `sections.push()`
- 条件付き依存: `if (!(text))` → `REQUIRED_CHAT_MODULES.has()`
- 参照: `Intl.DateTimeFormat().resolvedOptions().timeZone`, `MODEL_FEATURES.CHAT`, `Services.locale.appLocaleAsBCP47`, `entry.name`, `entry.version`, `err.clientReason`, `m.name`, `params.modules`, `params.version`
- XPCOM: `Services.locale` / `Services.prefs`

## getSkillPrompt()
- 位置: async L275-289
- 役割: スキル名を英数字・_・- に限って検証し、skill レコードの本文を返す。見つからなければ error を返す。
- 触るとき: モデルからのスキル呼び出しの受け付け条件や結果の形式を変えるとき。
- 呼び出し先: `/^[A-Za-z0-9_-]+$/.test()`, `String()`, `String(name || "").trim()`, `findSkill()`, `loadV2Records()`
- 参照: `record.prompts`, `record?.prompts`

## renderMentionedUrls()
- 位置: L298-320
- 役割: @メンションされた URL をタブグループごとに整え、URL は無加工、タイトルは無害化して箇条書きの文字列にする。
- 触るとき: メンションされたタブをモデルに見せる形式を変えるとき。
- 呼び出し先: `lines.join()`, `lines.push()`, `mentionsWithUrl .map()`, `sanitizeUntrustedContent()`
- 条件付き依存: `if (groupId && groupId !== lastGroupId)` → `sanitizeUntrustedContent()`
- 条件付き依存: `if (groupId && groupId !== lastGroupId)` → `lines.push()`

## buildBrowserContextPrompt()
- 位置: async L333-387
- 役割: 現在のタブ情報とメンションの URL を、対応する browser-context の断片に当てはめて描画する。個人データを含むと判断したら私的フラグを立て、何も無ければ null を返す。
- 触るとき: 毎ターンのブラウザ文脈の注入内容や、どの場合に私的データのフラグを立てるかを変えるとき。
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
- 役割: buildBrowserContextPrompt 内で、browser-context の指定モジュールを探す閉包。
- 触るとき: 断片の名前(tab や mentions)を変えるとき。
- 呼び出し先: `findModule()`

## selectFeatureConfig()
- 位置: async L405-449
- 役割: Remote Settings から機能の設定を選ぶ。v2 の params があればそれを、無ければ v1 の設定を候補にし、版・ユーザー指定モデル・選択肢で 1 件に絞る。見つからなければ例外を投げる。
- 触るとき: 機能ごとのモデル選択や Remote Settings が見つからない例外を調べるとき。
- 呼び出し先: `Services.prefs.getStringPref()`, `Services.prefs.prefHasUserValue()`, `allRecords.filter()`, `allRecords.some()`, `getRemoteRecords()`, `selectMainConfig()`
- 参照: `err.clientReason`, `featureConfigs.length`, `opts.majorVersionOverride`, `opts.modelChoiceIdOverride`, `r.feature`, `r.kind`
- XPCOM: `Services.prefs`

## buildEngineForFeature()
- 位置: async L459-509
- 役割: 設定からパラメータ、サービス種別、用途、エンドポイントを求め、必要なら対象機能に限ってチャットのモデルへ切り替えて openAIEngine を作る。
- 触るとき: 機能ごとに使うモデルや用途の決め方を変えるとき。
- 呼び出し先: `CHAT_MODEL_FALLBACK_FEATURES.has()`, `Services.prefs.getStringPref()`, `getDefaultServiceType()`, `openAIEngine.build()`, `openAIEngine.resolveEndpointConfig()`, `selectFeatureConfig()`
- 条件付き依存: `if (typeof parameters === "string")` → `JSON.parse()`
- 条件付き依存: `if ( model === GENERIC_MODEL_NAME && CHAT_MODEL_FALLBACK_FEATURES.has(feature) )` → `selectFeatureConfig()`
- 参照: `MODEL_FEATURES.AGENT_MONITOR`, `MODEL_FEATURES.AITAB`, `MODEL_FEATURES.CHAT`, `MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION`, `MODEL_FEATURES.RESUME_ACTIVITY_CONVERSATION_STARTER`, `chatConfig.model`, `mainConfig.model`, `mainConfig.parameters`, `mainConfig.purpose`, `mainConfig.service_type`, `opts.flowId`, `opts.modelChoiceIdOverride`
- XPCOM: `Services.prefs`

## buildConversation()
- 位置: async L520-523
- 役割: 機能名から engine とパラメータを作り、それを持つ新しい Conversation を返す。
- 触るとき: 新しい機能で会話を作るときの入口を確認するとき。
- 呼び出し先: `buildEngineForFeature()`

## loadPrompt()
- 位置: async L541-575
- 役割: カスタムプロンプトの pref による上書きを先に見て、module 指定があれば v2 から、チャットは組み立てから、その他は v1 設定の prompts を返す。
- 触るとき: プロンプトの読み込み元を変えるとき。上書きは機能単位なので module 指定の場合も同じ本文になる点に注意(要確認)。
- 呼び出し先: `Services.prefs.getStringPref()`, `selectFeatureConfig()`
- 条件付き依存: `if (customPromptsRaw)` → `JSON.parse()`
- 条件付き依存: `if (opts.module)` → `loadPromptV2()`
- 条件付き依存: `if (feature === MODEL_FEATURES.CHAT)` → `buildChatSystemPrompt()`
- 参照: `MODEL_FEATURES.CHAT`, `err.clientReason`, `mainConfig.prompts`, `mainConfig.version`, `opts.model`, `opts.module`
- XPCOM: `Services.prefs`

## loadPromptV2()
- 位置: async L584-628
- 役割: 機能・モデルの params を引き、モジュールの版を manifest から決めて、その版のモジュール本文を返す。見つからなければ例外。
- 触るとき: v2 モジュールのプロンプトが読めないとき、または版の選び方を変えるとき。
- 呼び出し先: `Services.prefs.getStringPref()`, `findModule()`, `findParams()`, `loadV2Records()`, `moduleRecord.prompts.trim()`, `paramsRecord.modules?.find()`
- 参照: `err.clientReason`, `m.name`, `moduleRecord?.prompts`, `opts.model`, `opts.module`, `paramsRecord.model`, `paramsRecord.modules?.find(m => m.name === opts.module)?.version`, `paramsRecord.version`
- XPCOM: `Services.prefs`
