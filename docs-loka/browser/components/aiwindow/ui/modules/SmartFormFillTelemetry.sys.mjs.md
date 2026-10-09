# browser/components/aiwindow/ui/modules/SmartFormFillTelemetry.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillTelemetry.sys.mjs
source-hash: 08f4e7a36dce6de920106786b199ada8e08a009f
lines: 633

## <module>
- 役割: Smart Form Fill の利用状況を Glean に送る。分類・関連タブ・値生成の各要求の開始と応答・失敗、タブ選択の結果、項目ごとの採否を記録する。
- 呼び出し先: `Object.freeze()`

## SmartFormFillTelemetry.#getLatency()
- 位置: L155-157
- 役割: 開始時刻からの経過時間を、ミリ秒の整数で返す。
- 触るとき: 応答の遅延の計測値がずれて見えるとき。
- 呼び出し先: `ChromeUtils.now()`, `Math.round()`
- 参照: `flow.startTime`

## SmartFormFillTelemetry.#getErrorName()
- 位置: L167-171
- 役割: 失敗の理由が既知の一覧にあればその理由名を、なければ genericError を返す。
- 触るとき: 失敗理由の分類を増やす、または一般エラーとして丸められる失敗を見直すとき。
- 呼び出し先: `REQUEST_ERROR_REASONS.has()`
- 参照: `error?.clientReason`

## SmartFormFillTelemetry.#getDecisionSource()
- 位置: L181-183
- 役割: モデルの動作名を token・generated・none のどれかに対応付ける。対応表に無い動作は none になる。
- 触るとき: 項目の値の出所の計測の分類を変えるとき。
- 呼び出し先: `DECISION_SOURCE_BY_ACTION.get()`

## SmartFormFillTelemetry.#getPercent()
- 位置: L193-195
- 役割: 0 から 1 の値を四捨五入して、百分率の整数にする。
- 触るとき: 類似度や確信度の計測値の単位や丸め方を調べるとき。
- 呼び出し先: `Math.round()`

## SmartFormFillTelemetry.#getSimilarityStats()
- 位置: L205-217
- 役割: 類似度の配列から最小、最大、平均 (百分率) を作る。空の配列なら null を返す。
- 触るとき: 記憶の類似度の計測値の集計方法を変えるとき。
- 呼び出し先: `Math.max()`, `Math.min()`, `scores.reduce()`, `this.#getPercent()`
- 参照: `scores.length`

## SmartFormFillTelemetry.#getTypedFieldCount()
- 位置: L226-230
- 役割: 型が付いた項目の数を数える。other と unknown は含めない。
- 触るとき: 分類できた項目数の計測の定義を変えるとき。
- 呼び出し先: `UNTYPED_FIELD_KINDS.has()`, `fields.filter()`
- 参照: `field.type`, `fields.filter( field => field.type && !UNTYPED_FIELD_KINDS.has(field.type) ).length`

## SmartFormFillTelemetry.#getUnknownFieldCount()
- 位置: L239-241
- 役割: 応答はあったが型を付けなかった項目の数 (other または unknown) を数える。
- 触るとき: 分類できなかった項目数の定義を変えるとき。
- 呼び出し先: `UNTYPED_FIELD_KINDS.has()`, `fields.filter()`
- 参照: `field.type`, `fields.filter(field => UNTYPED_FIELD_KINDS.has(field.type)).length`

## SmartFormFillTelemetry.startClassifyRequest()
- 位置: L252-262
- 役割: 分類要求の送信を、項目数やモデル情報と共に記録し、開始時刻を持つ流れの情報を返す。
- 触るとき: 分類要求の計測項目を足すとき、または分類の開始が記録されないとき。
- 呼び出し先: `ChromeUtils.now()`, `Glean.smartWindow.formFillClassifyRequest.record()`
- 参照: `modelInfo.model`, `modelInfo.promptVersion`, `request.fields.length`

## SmartFormFillTelemetry.sendClassifyResponseTelemetry()
- 位置: L270-281
- 役割: 分類の成功を、型の付いた項目数と未知の項目数などと共に記録する。
- 触るとき: 分類の成功時の計測項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.formFillClassifyResponse.record()`, `this.#getLatency()`, `this.#getTypedFieldCount()`, `this.#getUnknownFieldCount()`
- 参照: `flow.flowId`, `response.fields`, `response.pageType`

## SmartFormFillTelemetry.sendClassifyErrorTelemetry()
- 位置: L289-296
- 役割: 分類の失敗を、遅延と失敗理由と共に記録する。
- 触るとき: 分類の失敗が計測に出ない、または失敗理由が正しく出ないとき。
- 呼び出し先: `Glean.smartWindow.formFillClassifyResponse.record()`, `this.#getErrorName()`, `this.#getLatency()`
- 参照: `flow.flowId`

## SmartFormFillTelemetry.startRelevantTabsRequest()
- 位置: L308-318
- 役割: 関連タブ要求の送信を、送ったタブ数や閾値と共に記録し、流れの情報を返す。
- 触るとき: 関連タブ要求の計測項目を変えるとき。
- 呼び出し先: `ChromeUtils.now()`, `Glean.smartWindow.formRelevantTabsRequest.record()`
- 参照: `modelInfo.model`, `modelInfo.promptVersion`, `request.tabs.length`

## SmartFormFillTelemetry.sendRelevantTabsResponseTelemetry()
- 位置: L328-343
- 役割: 関連タブの応答を、選ばれた数、使われた数、関連度ごとの数と共に記録する。
- 触るとき: 関連タブの応答計測の内訳を変えるとき。
- 呼び出し先: `Glean.smartWindow.formRelevantTabsResponse.record()`, `rated()`, `this.#getLatency()`
- 参照: `flow.flowId`, `response?.selectedTabs`, `response?.selectedTabs?.length`

## rated()
- 位置: L330-331
- 役割: 選ばれたタブのうち、指定の関連度のものの数を数える。
- 触るとき: 関連度ごとの内訳の数え方を変えるとき。
- 呼び出し先: `selectedTabs.filter()`
- 参照: `selectedTabs.filter(tab => tab?.relevance === level).length`, `tab?.relevance`

## SmartFormFillTelemetry.sendRelevantTabsErrorTelemetry()
- 位置: L351-360
- 役割: 関連タブの失敗を、遅延と失敗理由と共に記録する。タブ数は送らない。
- 触るとき: 関連タブの失敗時にタブ数を送るべきかを検討するとき。
- 呼び出し先: `Glean.smartWindow.formRelevantTabsResponse.record()`, `this.#getErrorName()`, `this.#getLatency()`
- 参照: `flow.flowId`

## SmartFormFillTelemetry.sendRelevantTabsOutcomeTelemetry()
- 位置: L368-384
- 役割: 提案されたタブと最終的なタブを比べ、残った数、外した数、追加した数、エディタの開閉を記録する。
- 触るとき: 利用者がタブ選択をどう直したかの計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.formRelevantTabsOutcome.record()`, `[...final].filter()`, `[...suggested].filter()`, `final.has()`, `finalTabs.map()`, `suggested.has()`, `suggestedTabs.map()`
- 参照: `[...final].filter(id => !suggested.has(id)).length`, `[...suggested].filter(id => !final.has(id)).length`, `[...suggested].filter(id => final.has(id)).length`, `editor?.opens`, `editor?.result`, `final.size`

## SmartFormFillTelemetry.startGenerateRequest()
- 位置: L395-416
- 役割: 値生成要求の送信を、トークン数、タブ数、記憶の類似度の集計などと共に記録し、流れの情報を返す。
- 触るとき: 値生成要求の計測項目を変えるとき。
- 呼び出し先: `ChromeUtils.now()`, `Glean.smartWindow.formFillGenerateRequest.record()`, `similarityByMemory.values()`, `this.#getSimilarityStats()`
- 参照: `modelInfo.model`, `modelInfo.promptVersion`, `request.context.memories.length`, `request.context.relevantTabs.length`, `similarity?.avg`, `similarity?.max`, `similarity?.min`, `valuesByToken.size`

## SmartFormFillTelemetry.sendGenerateResponseTelemetry()
- 位置: L428-452
- 役割: 値生成の成功を、埋めた数、使われた記憶と類似度、タブ数、バッチの成否と共に記録する。
- 触るとき: 値生成の応答計測の中身や、バッチ数の意味を変えるとき。
- 呼び出し先: `(response.memories_used ?? []) .map()`, `(response.memories_used ?? []) .map(memoryId => similarityByMemory.get(memoryId)) .filter()`, `Glean.smartWindow.formFillGenerateResponse.record()`, `similarityByMemory.get()`, `this.#getLatency()`, `this.#getSimilarityStats()`
- 参照: `flow.flowId`, `response.batches?.failed`, `response.batches?.total`, `response.memories_used`, `response.memories_used?.length`, `response.tabs_used?.length`, `similarity?.avg`, `similarity?.max`, `similarity?.min`

## SmartFormFillTelemetry.sendGenerateErrorTelemetry()
- 位置: L460-470
- 役割: 値生成の失敗を、埋めた数 0、遅延、失敗理由と共に記録する。バッチ数は送らない。
- 触るとき: 値生成の失敗時に送る値を変えるとき。
- 呼び出し先: `Glean.smartWindow.formFillGenerateResponse.record()`, `this.#getErrorName()`, `this.#getLatency()`
- 参照: `flow.flowId`

## SmartFormFillTelemetry.resolveFieldDecisions()
- 位置: L480-505
- 役割: 送られた項目ごとに、分類、出所、確信度、トークンの有無などのモデルの判断をまとめ、フォーム内の位置も求める。
- 触るとき: 項目ごとの判断の記録内容を変えるとき、または項目の位置番号がずれて見えるとき。
- 呼び出し先: `classifications.get()`, `fields.map()`, `formFields.findIndex()`, `this.#getDecisionSource()`, `this.#getPercent()`, `tokensByFieldId.get()`, `tokensByFieldId.has()`, `values.fields?.find()`
- 参照: `classifications.get(field.id)?.type`, `field.id`, `field.inputType`, `field.localConfidence`, `field.localGuess`, `field.localSource`, `result?.action`, `result?.confidence`

## SmartFormFillTelemetry.sendFillFieldTelemetry()
- 位置: L515-532
- 役割: 項目ごとの判断を、埋められたかどうかと併せて記録する。
- 触るとき: 項目単位の計測を増やす、または埋めたかどうかの判定を変えるとき。
- 呼び出し先: `Glean.smartWindow.formFillField.record()`, `filledFieldIds.includes()`
- 参照: `decision.confidence`, `decision.fieldId`, `decision.fieldKind`, `decision.fieldSeq`, `decision.inputType`, `decision.preLLMConfidence`, `decision.preLLMFieldKind`, `decision.preLLMSource`, `decision.source`, `decision.tokenAvailable`, `decision.tokenKind`

## SmartFormFillTelemetry.#getFieldOutcome()
- 位置: L542-548
- 役割: ページが報告した状態から、kept、edited、cleared のどれかを返す。
- 触るとき: 利用者の編集の分類の定義を変えるとき。

## SmartFormFillTelemetry.sendFillFieldOutcomeTelemetry()
- 位置: L565-586
- 役割: 埋めた項目が後にどうなったか (残った、編集された、消された) を、長さと共に記録する。
- 触るとき: 埋めた後の結果の計測項目を変えるとき。
- 呼び出し先: `Glean.smartWindow.formFillFieldOutcome.record()`, `decisions.find()`, `this.#getFieldOutcome()`
- 参照: `decision.confidence`, `decision.fieldKind`, `decision.fieldSeq`, `decision.source`, `field.filledLength`, `field.finalLength`, `field.id`

## SmartFormFillTelemetry.sendFillFieldReviewOutcomeTelemetry()
- 位置: L601-631
- 役割: レビューで提示した値と送信された値を比べ、利用者が編集したかを記録する。
- 触るとき: レビュー画面での編集の計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.formFillFieldReviewOutcome.record()`, `decisions.find()`, `generated.get()`, `this.#getFieldOutcome()`, `value.trim()`
- 参照: `decision.fieldSeq`, `generatedValue.length`, `value.length`
