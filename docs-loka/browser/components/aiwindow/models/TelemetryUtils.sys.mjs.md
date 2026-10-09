# browser/components/aiwindow/models/TelemetryUtils.sys.mjs

source: browser/components/aiwindow/models/TelemetryUtils.sys.mjs
source-hash: 3382b87e7872f439f566ebdd5dea49251816f032
lines: 529

## <module>
- 役割: 会話の終了や途中で、LLM を判定者(LLM-as-judge)にして会話を評価するテレメトリの仕組みを定義する。トリガー判定、評価プロンプトの実行、Glean への記録を担う。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `XPCOMUtils.declareLazy()`, `console.createInstance()`

## uniform_sample()
- 位置: L42-43
- 役割: 最初のターンだけ真を返す。全体から一様に抽出するための判定。
- 触るとき: 一様抽出の対象になる条件を変えるとき。
- 呼び出し先: `conversation.currentTurnIndex()`

## uniform_sample_at_turn()
- 位置: L44-46
- 役割: 一様抽出に選ばれた会話で、指定ターンに達したとき真を返す。
- 触るとき: 特定ターンで評価する仕組みを変えるとき。
- 呼び出し先: `conversation.currentTurnIndex()`
- 参照: `conversation._telemetryUniformSample`

## min_turns()
- 位置: L47-48
- 役割: 現在のターン番号が指定の最小ターン以上なら真を返す。
- 触るとき: 評価を始めるターン数の閾値を変えるとき。
- 呼び出し先: `conversation.currentTurnIndex()`

## Trigger.constructor()
- 位置: L76-81
- 役割: 名前、判定関数、抽出確率、説明を持つトリガーを作る。
- 触るとき: トリガーの持つ項目を増やすとき。
- 参照: `this.check`, `this.description`, `this.name`, `this.samplingProbability`

## TelemetryPromptEngine.build()
- 位置: async L108-142
- 役割: 評価用レコードの設定と拡張ヘッダーの pref から、判定用の openAIEngine を作って返す。
- 触るとき: 判定に使うモデルやヘッダーの指定を変えるとき。
- 呼び出し先: `JSON.parse()`, `Services.prefs.getStringPref()`, `lazy.console.error()`, `lazy.openAIEngine._createEngine()`
- 参照: `engine.#engineInstance`, `engine.#promptRecord`, `lazy.openAIEngine.endpoint`, `promptRecord.model`, `promptRecord.purpose`, `promptRecord.service_type`
- XPCOM: `Services.prefs`

## TelemetryPromptEngine.verifyResult()
- 位置: L144-164
- 役割: モデルの出力 JSON を解析し、各項目が許可値の一覧に含まれなければ unknown にする。JSON が壊れていれば全項目 unknown。
- 触るとき: 判定結果の許可値や形式を変えるとき。
- 呼び出し先: `JSON.parse()`, `Object.fromEntries()`, `Object.keys()`, `Object.keys(schema).map()`, `schema[key]?.includes()`
- 参照: `result.finalOutput`, `this.#promptRecord.output_schema`

## TelemetryPromptEngine.run()
- 位置: async L172-191
- 役割: URL を加工せずに会話のメッセージを作り、評価プロンプトに入れて判定モデルを実行し、結果を検証して返す。
- 触るとき: 判定に渡す会話の内容やプロンプトの埋め込みを変えるとき。
- 呼び出し先: `JSON.stringify()`, `Object.keys()`, `conversation.getMessagesInChatCompletionsFormat()`, `lazy.console.debug()`, `lazy.openAIEngine.getFxAccountToken()`, `renderPrompt()`, `this.#engineInstance.run()`, `this.verifyResult()`
- 参照: `this.#promptRecord.output_schema`, `this.#promptRecord.prompt`

## TelemetryEngine._fetchRecords()
- 位置: async L212-221
- 役割: Remote Settings のコレクションを取得し、失敗時は既定値を返す。
- 触るとき: テレメトリの設定が読めないときに既定値で続けるかを変えるとき。
- 呼び出し先: `client.get()`, `lazy.RemoteSettings()`, `lazy.console.error()`

## TelemetryEngine.getTriggerDefinitions()
- 位置: async L223-250
- 役割: Remote Settings からトリガー定義を読み、既知の判定とメジャー版が合うものだけを Trigger にして保持する。読み込み済みなら何もしない。
- 触るとき: トリガー定義の検証条件を変えるとき。
- 呼び出し先: `TRIGGER_CHECK_STRATEGIES[def.check]()`, `checkMajorVersion()`, `this._fetchRecords()`, `triggerRecords .filter()`, `triggerRecords .filter(def => TRIGGER_CHECK_STRATEGIES[def.check]) .filter()`
- 参照: `def.check`, `def.description`, `def.name`, `def.params`, `def.sampling_probability`, `def.version`, `this._triggers`

## TelemetryEngine._getRandom()
- 位置: L252-254
- 役割: 0 以上 1 未満の乱数を返す。
- 触るとき: テストで抽出を固定するための差し替え点として見るとき。
- 呼び出し先: `Math.random()`

## TelemetryEngine.getTriggers()
- 位置: async L256-294
- 役割: 会話に対して未判定のトリガーを評価し、判定が真で抽出に当たったものを返す。一様抽出に当たった会話には印を付ける。
- 触るとき: どのトリガーで評価が走るか、同じ会話で二重に判定しない条件を変えるとき。
- 呼び出し先: `conversation._checkedTelemetryTriggers.has()`, `conversation.currentTurnIndex()`, `lazy.console.debug()`, `this.getTriggerDefinitions()`, `trigger.check()`
- 条件付き依存: `if (conversation._checkedTelemetryTriggers.has(trigger.name))` → `lazy.console.debug()`
- 条件付き依存: `if (trigger.check(conversation))` → `conversation._checkedTelemetryTriggers.add()`
- 条件付き依存: `if (trigger.check(conversation))` → `this._getRandom()`
- 条件付き依存: `if (this._getRandom() < trigger.samplingProbability)` → `lazy.console.debug()`
- 条件付き依存: `if (this._getRandom() < trigger.samplingProbability)` → `fired.push()`
- 参照: `conversation._checkedTelemetryTriggers`, `conversation._telemetryUniformProbability`, `conversation._telemetryUniformSample`, `this._triggers`, `trigger.name`, `trigger.samplingProbability`

## TelemetryEngine.runTelemetry()
- 位置: async L305-345
- 役割: 発火したトリガーに対応する評価レコードを、名前の重複を除いて集め、評価を実行して抽出確率つきの結果を返す。
- 触るとき: 発火したトリガーからどの評価プロンプトを走らせるかを変えるとき。
- 呼び出し先: `checkMajorVersion()`, `results.map()`, `samplingProbabilities.get()`, `seen.has()`, `this._fetchRecords()`, `this._runPrompts()`, `triggers.map()`
- 条件付き依存: `if ( !seen.has(record.telemetry_name) && // sometimes multiple triggers will use the same telemetry checkMajorVersion( record.version, TELEMETRY_MAJOR_VERSIONS[r...)` → `recordTriggers.find()`
- 条件付き依存: `if ( !seen.has(record.telemetry_name) && // sometimes multiple triggers will use the same telemetry checkMajorVersion( record.version, TELEMETRY_MAJOR_VERSIONS[r...)` → `triggerByName.has()`
- 条件付き依存: `if (matchingTriggerName)` → `seen.add()`
- 条件付き依存: `if (matchingTriggerName)` → `promptsToRun.push()`
- 条件付き依存: `if (matchingTriggerName)` → `samplingProbabilities.set()`
- 条件付き依存: `if (matchingTriggerName)` → `triggerByName.get()`
- 参照: `r.telemetry_name`, `record.telemetry_name`, `record.triggers`, `record.version`, `t.name`, `triggerByName.get(matchingTriggerName).samplingProbability`, `triggers.length`

## TelemetryEngine.runTelemetryByName()
- 位置: async L355-376
- 役割: 名前で指定された評価レコードのうち、版が合い run_terminal が真のものだけを実行する。
- 触るとき: 会話終了時の評価対象を変えるとき。
- 呼び出し先: `allRecords .filter()`, `allRecords .filter(record => nameSet.has(record.telemetry_name)) .filter()`, `checkMajorVersion()`, `nameSet.has()`, `this._fetchRecords()`, `this._runPrompts()`
- 参照: `promptNames.length`, `record.run_terminal`, `record.telemetry_name`, `record.version`

## TelemetryEngine._runPrompts()
- 位置: async L378-419
- 役割: 評価を順に実行し、429 エラーだけ指数バックオフで最大 3 回まで再試行する。他のエラーは記録して次へ進む。
- 触るとき: 評価の再試行条件や待ち時間を変えるとき、またはレート制限の失敗を調べるとき。
- 呼び出し先: `TelemetryPromptEngine.build()`, `engine.run()`, `lazy.console.debug()`, `lazy.openAIEngine.is429Error()`, `results.push()`
- 条件付き依存: `if (attempt > 0)` → `lazy.setTimeout()`
- 条件付き依存: `if (attempt > 0)` → `Math.random()`
- 条件付き依存: `if (!(lazy.openAIEngine.is429Error(error)))` → `lazy.console.error()`
- 条件付き依存: `if (lastError)` → `lazy.console.error()`
- 参照: `record.telemetry_name`, `record.version`

## normalizeMetadata()
- 位置: L422-444
- 役割: メタデータの確率を 1000 分率の整数にし、トリガー一覧を JSON 文字列にして返す。
- 触るとき: Glean に送る指標の形式を変えるとき。
- 呼び出し先: `Array.isArray()`, `JSON.stringify()`, `Math.round()`

## submitTelemetryResult()
- 位置: L446-478
- 役割: 評価結果の各属性を Glean の llmajBasedTelemetry に記録する。ユニフォーム抽出かトリガー抽出かのフラグも付ける。
- 触るとき: 記録される項目や抽出フラグの判定を変えるとき。
- 呼び出し先: `(metadata.triggers ?? []).includes()`, `(metadata.triggers ?? []).some()`, `Glean.smartWindow.llmajBasedTelemetry.record()`, `Object.entries()`, `String()`, `conversation.currentTurnIndex()`, `normalizeMetadata()`
- 参照: `conversation.id`, `metadata.triggers`, `resultObject?.result`, `resultObject?.samplingProbability`, `resultObject?.telemetry_name`, `resultObject?.telemetry_version`

## runLLMaJTelemetry()
- 位置: async L486-528
- 役割: 会話を未処理にしてからトリガーを評価し、非同期で評価と記録を行い、結果があれば評価の記録を ChatStore に反映する。
- 触るとき: 会話の途中で評価を起動する条件、または評価結果が保存されない原因を調べるとき。トリガー名に対応する評価を TELEMETRY_MAJOR_VERSIONS にも登録しないと黙って飛ばされる(要確認)。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `Object.fromEntries()`, `console.error()`, `conversation.currentTurnIndex()`, `lazy.ChatStore.markLLMTelemetryUnprocessed()`, `lazy.ChatStore.markLLMTelemetryUnprocessed(conversation.id).catch()`, `lazy.ChatStore.updateLLMTelemetryRecord()`, `results.map()`, `submitTelemetryResult()`, `telemetryEngine .runTelemetry()`, `telemetryEngine .runTelemetry(triggers, conversation) .then()`, `telemetryEngine.getTriggers()`, `triggers.map()`
- 参照: `conversation._telemetryUniformProbability`, `conversation.engine?.model`, `conversation.id`, `conversation.systemPromptVersion`, `r.samplingProbability`, `r.telemetry_name`, `results.length`, `t.name`
