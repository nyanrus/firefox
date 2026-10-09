# browser/components/aiwindow/ui/modules/SmartFormFillController.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillController.sys.mjs
source-hash: 1a73eda3876c68beee9866d66e07c0de8765f3c5
lines: 1070

## <module>
- 役割: Smart Form Fill の制御役。フォームごとの関連タブ選択、項目分類、値の生成を、モデル呼び出しとリトライ付きで仲介し、結果を入力指示に変換する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SmartFormFillController.constructor()
- 位置: L188-200
- 役割: ページ情報と要求オブザーバを保持し、フォーム・タブ・中止コントローラ用の Map を初期化する。
- 触るとき: ページごとの状態の持ち方を変えるとき、または状態の Map を新しく足すとき。
- 参照: `this.#abortClassificationControllers`, `this.#abortRelevantTabsControllers`, `this.#abortValueGenerationControllers`, `this.#classifiedFieldsByFormId`, `this.#formDataById`, `this.#pageInfo`, `this.#relevantTabsByFormId`, `this.#requestObserver`, `this.#tabCounter`, `this.#tabsById`

## SmartFormFillController.getRelevantTabsFor()
- 位置: L209-211
- 役割: フォームについて LLM が選んだ関連タブを返す。未取得なら空配列。
- 触るとき: 関連タブの選択結果を候補表示に使う箇所を変えるとき。
- 呼び出し先: `this.#relevantTabsByFormId.get()`
- 参照: `this.#relevantTabsByFormId.get(formId)?.selectedTabs`

## SmartFormFillController.hasSourceTabs()
- 位置: L218-220
- 役割: フォームのタブ以外に候補元のタブが 1 つ以上あるかを返す。
- 触るとき: 候補元が無いときの案内文言の出し分けを調べるとき。
- 参照: `this.#tabList?.length`

## SmartFormFillController.getTabData()
- 位置: L229-231
- 役割: 安定したタブ ID に対応する、モデル用のタブ情報を返す。
- 触るとき: タブ ID から URL やタイトルを引いた値が合わないとき。
- 呼び出し先: `this.#tabsById.get()`

## SmartFormFillController.#setFormData()
- 位置: L238-240
- 役割: フォーム情報を ID をキーにしてキャッシュへ保存する。モデルは呼ばない。
- 触るとき: フォーム情報の保存先や ID の扱いを変えるとき。
- 呼び出し先: `this.#formDataById.set()`
- 参照: `formData.id`

## SmartFormFillController.findRelevantTabs()
- 位置: async L248-269
- 役割: フォームの関連タブ選択をモデルに依頼して結果を保存する。同じフォームの前回の依頼は中止する。
- 触るとき: 関連タブの選択が重複して走る、または古い応答が残るとき、中止と保存の流れを確認する。
- 呼び出し先: `this.#abortRelevantTabsControllers.get()`, `this.#abortRelevantTabsControllers.get(formData.id)?.abort()`, `this.#abortRelevantTabsControllers.set()`, `this.#ensureTabData()`, `this.#findRelevantTabsForForm()`, `this.#removeAbortController()`, `this.#requestWithRetries()`, `this.#setFormData()`
- 参照: `abortController.signal`, `formData.id`, `this.#abortRelevantTabsControllers`

## SmartFormFillController.classifyFields()
- 位置: async L277-297
- 役割: フォームの項目分類をモデルに依頼して結果を保存する。同じフォームの前回の依頼は中止する。
- 触るとき: 項目の分類結果が反映されない、または再分類が効かないとき。
- 呼び出し先: `this.#abortClassificationControllers.get()`, `this.#abortClassificationControllers.get(formData.id)?.abort()`, `this.#abortClassificationControllers.set()`, `this.#classifyFormFields()`, `this.#removeAbortController()`, `this.#requestWithRetries()`, `this.#setFormData()`
- 参照: `abortController.signal`, `formData.id`, `this.#abortClassificationControllers`

## SmartFormFillController.#invalidateRelevantTabs()
- 位置: L304-308
- 役割: フォームの関連タブ依頼を中止し、その結果のキャッシュを消す。
- 触るとき: フォームの内容が変わったあとに古い関連タブが残らないようにするとき。
- 呼び出し先: `this.#abortRelevantTabsControllers.delete()`, `this.#abortRelevantTabsControllers.get()`, `this.#abortRelevantTabsControllers.get(formId)?.abort()`, `this.#relevantTabsByFormId.delete()`

## SmartFormFillController.invalidateForm()
- 位置: L315-321
- 役割: フォームに関するモデルの結果 (関連タブ、分類、フォーム情報) を、中止したうえですべて消す。
- 触るとき: フォームの DOM が大きく変わったとき、どのキャッシュが消えるかを確かめるとき。
- 呼び出し先: `this.#abortClassificationControllers.delete()`, `this.#abortClassificationControllers.get()`, `this.#abortClassificationControllers.get(formId)?.abort()`, `this.#classifiedFieldsByFormId.delete()`, `this.#formDataById.delete()`, `this.#invalidateRelevantTabs()`

## SmartFormFillController.invalidateTabs()
- 位置: L326-330
- 役割: 開いているタブ一覧に依存する関連タブの結果を中止して消し、タブ一覧も破棄する。
- 触るとき: タブを開いたり閉じたりした後に、次の関連タブ選択で最新のタブ一覧を使わせたいとき。
- 呼び出し先: `this.#abortRequests()`, `this.#relevantTabsByFormId.clear()`
- 参照: `this.#abortRelevantTabsControllers`, `this.#tabList`

## SmartFormFillController.getTabs()
- 位置: L337-339
- 役割: 開いているタブ情報の浅いコピーの配列を返す。未取得なら空配列。
- 触るとき: タブ一覧を外へ渡すとき、内部の状態を書き換えられないようにしたいとき。
- 呼び出し先: `this.#tabList?.map()`

## SmartFormFillController.cancelAutofill()
- 位置: L348-350
- 役割: フォームの値生成の依頼を中止する。
- 触るとき: 利用者が入力を取り消したあとも生成が止まらない問題を追うとき。
- 呼び出し先: `this.#abortValueGenerationControllers.get()`, `this.#abortValueGenerationControllers.get(formId)?.abort()`

## SmartFormFillController.autofill()
- 位置: async L363-390
- 役割: 空欄の項目だけを対象に値生成を依頼する。対象が無ければ null を返す。
- 触るとき: 自動入力の対象項目の選び方や、呼び出し元からの流れを変えるとき。
- 呼び出し先: `emptyFieldIds.has()`, `formData.fields.filter()`, `this.#formDataById.get()`, `this.#generateFormValues()`
- 参照: `emptyFields.length`, `field.id`, `formData.fields`

## SmartFormFillController.#generateFormValues()
- 位置: async L406-534
- 役割: 候補値とタブ本文を集めて値生成をモデルに依頼し、応答を入力指示に変換する。送信後に起きた失敗だけを通知する。
- 触るとき: 生成された値が入らない、または失敗が記録されないとき。記憶の参照は v0 では無効化されている。
- 呼び出し先: `(this.#classifiedFieldsByFormId.get(id)?.fields ?? []).map()`, `abortCtrl.signal.throwIfAborted()`, `classifications.get()`, `lazy.SmartFormFillModel.generateFormValues()`, `relevantMemories.map()`, `selectedTabs.map()`, `tabContentById.get()`, `this.#abortValueGenerationControllers.get()`, `this.#abortValueGenerationControllers.get(id)?.abort()`, `this.#abortValueGenerationControllers.set()`, `this.#classifiedFieldsByFormId.get()`, `this.#getCandidates()`, `this.#getFieldDataForClassification()`, `this.#getFieldDataForClassification(fields).map()`, `this.#getFillInstructions()`, `this.#removeAbortController()`, `this.#requestObserver.onGenerateAnswered()`, `this.#tabsById.get()`
- 条件付き依存: `if (flow && !abortCtrl.signal.aborted)` → `this.#requestObserver.onGenerateFailed()`
- 参照: `abortCtrl.signal`, `abortCtrl.signal.aborted`, `classification?.confidence`, `classification?.type`, `field.id`, `fillInstructions.length`, `memory.id`, `memory.memory_summary`, `memory.similarity`, `result.id`, `selectedTab.id`, `this.#abortValueGenerationControllers`, `this.#classifiedFieldsByFormId.get(id)?.fields`, `this.#pageInfo`

## onDispatch()
- 位置: L490-497
- 役割: 最初のバッチが送られた時点で生成要求の計測を開始し、以後のバッチでは何もしない。
- 触るとき: 生成要求の計測が二重に記録される、または送信前なのに記録されるとき。
- 呼び出し先: `this.#requestObserver.onGenerateDispatched()`

## SmartFormFillController.#getMemories()
- 位置: async L549-577
- 役割: ページ情報と項目から問い合わせ文を作り、関連する記憶の ID、要約、類似度だけを返す。
- 触るとき: 記憶を生成時に参照する機能を有効にするとき。現在は呼ばれていない。
- 呼び出し先: `URL.parse()`, `[ field.label, field.inputType, field.placeholder, field.textBefore, field.textAfter, ] .filter()`, `[ field.label, field.inputType, field.placeholder, field.textBefore, field.textAfter, ] .filter(Boolean) .join()`, `fields.map()`, `lazy.MemoriesManager.getRelevantMemories()`, `relevantMemories.map()`
- 参照: `URL.parse(pageInfo.url)?.hostname`, `field.inputType`, `field.label`, `field.placeholder`, `field.textAfter`, `field.textBefore`, `pageInfo.title`, `pageInfo.url`

## SmartFormFillController.#getFillInstructions()
- 位置: L588-626
- 役割: モデルの応答を確信度の閾値で絞り、トークンなら保存値に置き換えて、id と value の配列にする。
- 触るとき: 入力指示に入る値の閾値や、トークンの解決の扱いを変えるとき。
- 呼び出し先: `CONFIDENCE_RANK.get()`, `fieldIds.has()`, `fields.map()`, `fillInstructions.push()`, `resolvedFieldIds.add()`, `resolvedFieldIds.has()`, `valuesByToken.get()`
- 参照: `field.id`, `result.action`, `result.confidence`, `result.id`, `result.value`, `values.fields`

## SmartFormFillController.#getCandidates()
- 位置: async L634-670
- 役割: 分類済みの項目ごとに、保存済み住所か Form History の最新値を探し、候補トークンと値の対応表を作る。
- 触るとき: モデルに渡す保存値の候補を変えるとき、またはトークンの形式を変えるとき。
- 呼び出し先: `candidates.push()`, `lazy.FormAutofillUtils.isAddressField()`, `this.#getFormHistoryValue()`, `tokensByFieldId.set()`, `type.toUpperCase()`, `type.toUpperCase().replaceAll()`, `typeCounts.get()`, `typeCounts.set()`, `valuesByToken.set()`
- 条件付き依存: `if (lazy.FormAutofillUtils.isAddressField(type))` → `this.#getSavedAddresses()`
- 条件付き依存: `if (lazy.FormAutofillUtils.isAddressField(type))` → `savedAddresses.find()`
- 参照: `field.id`, `field.localGuess`

## SmartFormFillController.#getSavedAddresses()
- 位置: async L681-698
- 役割: 住所の自動入力が有効なら、保存済みの住所を最近使った順に返す。カード情報は含めない。
- 触るとき: 住所候補の取得条件を変えるとき。カード番号は復号に再認証が要るため除外しており、その判断を崩すような変更を検討するとき。
- 呼び出し先: `addresses.sort()`, `lazy.FormAutofill.isAutofillTypeEnabled()`, `lazy.formAutofillStorage.addresses.getAll()`, `lazy.formAutofillStorage.initialize()`
- 参照: `a.timeLastUsed`, `b.timeLastUsed`, `lazy.AutofillDataTypes.ADDRESS`

## SmartFormFillController.#getFormHistoryValue()
- 位置: async L706-726
- 役割: 項目の formHistoryName で Form History を検索し、最後に使われた値を返す。
- 触るとき: 履歴由来の候補が出ない、または古い値が出るとき。
- 呼び出し先: `lazy.FormHistory.search()`, `results.sort()`
- 参照: `a.lastUsed`, `b.lastUsed`, `field.formHistoryName`, `results?.length`, `results[0].value`

## SmartFormFillController.#abortRequests()
- 位置: L733-743
- 役割: 渡された複数の Map に入っている中止コントローラをすべて中止し、Map を空にする。
- 触るとき: 一括中止の対象になる要求の種類を増やすとき。
- 呼び出し先: `controller.abort()`, `controllerMaps.flatMap()`, `map.clear()`, `map.values()`

## SmartFormFillController.#removeAbortController()
- 位置: L752-756
- 役割: Map の中身が引数のコントローラと同じときだけ削除する。
- 触るとき: 後から始まった要求の登録を、古い要求の終了処理が消してしまう問題を追うとき。
- 呼び出し先: `controllers?.get()`
- 条件付き依存: `if (controllers?.get(id) === controller)` → `controllers.delete()`

## SmartFormFillController.destroy()
- 位置: L761-785
- 役割: 保持している状態をすべて空にして、残っている要求を中止する。以後は保持先を null にする。
- 触るとき: ページを離れるときの後片付けに項目を足すとき、または解放漏れを調べるとき。
- 呼び出し先: `this.#abortRequests()`, `this.#classifiedFieldsByFormId.clear()`, `this.#formDataById.clear()`, `this.#relevantTabsByFormId.clear()`, `this.#tabsById.clear()`
- 参照: `this.#abortClassificationControllers`, `this.#abortRelevantTabsControllers`, `this.#abortValueGenerationControllers`, `this.#classifiedFieldsByFormId`, `this.#formDataById`, `this.#relevantTabsByFormId`, `this.#tabCounter`, `this.#tabList`, `this.#tabsById`

## SmartFormFillController.#ensureTabData()
- 位置: L790-798
- 役割: タブ一覧が未取得のときだけ、上限付きで取得し直してモデル用のタブ情報を作る。
- 触るとき: 取得するタブ数の上限や、タブ情報の再取得の条件を変えるとき。
- 呼び出し先: `lazy.getTabList()`, `this.#getTabData()`, `this.#tabsById.clear()`
- 参照: `this.#tabCounter`, `this.#tabList`

## SmartFormFillController.#requestWithRetries()
- 位置: async L809-828
- 役割: 依頼を最大 3 回まで、再試行可能なエラーに限って指数バックオフでやり直す。中止された場合は直ちに投げる。
- 触るとき: モデル依頼の再試行条件や回数を変えるとき。
- 呼び出し先: `lazy.SmartFormFillModel.isRetryableRequestError()`, `request()`, `signal.throwIfAborted()`, `this.#waitBeforeRetry()`

## SmartFormFillController.#waitBeforeRetry()
- 位置: L838-856
- 役割: 1 秒を基準に試行ごとに 2 倍し、0 から 250 ミリ秒の揺らぎを足した時間だけ待つ。中止されたら待ちを打ち切る。
- 触るとき: 再試行の待ち時間を調整するとき。
- 呼び出し先: `Math.floor()`, `Math.pow()`, `Math.random()`, `lazy.setTimeout()`, `resolve()`, `signal.addEventListener()`, `signal.removeEventListener()`

## onAbort()
- 位置: L844-847
- 役割: 中止を受けて待ち用のタイマーを止め、待機を拒否して終える。
- 触るとき: 中止後もタイマーが残る、または待機が終わらない問題を追うとき。
- 呼び出し先: `lazy.clearTimeout()`, `reject()`
- 参照: `signal.reason`

## SmartFormFillController.#getValidRelevantTabs()
- 位置: L864-889
- 役割: モデルが選んだタブから、既知かつ重複しておらず関連度が閾値以上のものを、上限数まで取り出す。
- 触るとき: 選ばれたタブが候補に出ない、または多すぎるとき、閾値や上限を確かめるとき。
- 呼び出し先: `Array.isArray()`, `CONFIDENCE_RANK.get()`, `seen.add()`, `seen.has()`, `selectedTabs .filter()`, `this.#tabsById.has()`
- 参照: `lazy.MAX_SELECTED_TABS`, `tab?.id`, `tab?.relevance`

## SmartFormFillController.#findRelevantTabsForForm()
- 位置: async L899-942
- 役割: 関連タブ選択をモデルに送り、有効なタブを保存して応答を通知する。送信後の失敗だけを通知する。
- 触るとき: 関連タブの応答が保存されない、または失敗の通知が抜けるとき。
- 呼び出し先: `lazy.SmartFormFillModel.findRelevantTabs()`, `signal.throwIfAborted()`, `this.#getRelevantTabRequestBody()`, `this.#getValidRelevantTabs()`, `this.#relevantTabsByFormId.set()`, `this.#requestObserver.onRelevantTabsAnswered()`
- 条件付き依存: `if (flow && !signal.aborted)` → `this.#requestObserver.onRelevantTabsFailed()`
- 参照: `relevantTabCandidates?.selectedTabs`, `relevantTabs.selectedTabs.length`, `signal.aborted`

## onDispatch()
- 位置: L910-917
- 役割: 送信時に関連タブ依頼の開始を通知し、その戻り値を後の応答・失敗の通知に使うため保持する。
- 触るとき: 関連タブ依頼の計測の対応付けを変えるとき。
- 呼び出し先: `this.#requestObserver.onRelevantTabsDispatched()`

## SmartFormFillController.#classifyFormFields()
- 位置: async L951-985
- 役割: 項目分類をモデルに送り、結果を保存して応答を通知する。送信後の失敗だけを通知する。
- 触るとき: 分類結果が保存されない、または分類の失敗が記録されないとき。
- 呼び出し先: `lazy.SmartFormFillModel.classifyFields()`, `signal.throwIfAborted()`, `this.#classifiedFieldsByFormId.set()`, `this.#getClassifyFieldsRequestBody()`, `this.#requestObserver.onClassifyAnswered()`
- 条件付き依存: `if (flow && !signal.aborted)` → `this.#requestObserver.onClassifyFailed()`
- 参照: `signal.aborted`

## onDispatch()
- 位置: L963-969
- 役割: 送信時に分類依頼の開始を通知し、その戻り値を保持する。
- 触るとき: 分類依頼の計測の対応付けを変えるとき。
- 呼び出し先: `this.#requestObserver.onClassifyDispatched()`

## SmartFormFillController.#getFieldDataForClassification()
- 位置: L993-1008
- 役割: 項目情報のうち、モデルに渡す属性 (ラベル、名前、入力型、ヒントなど) を取り出す。
- 触るとき: モデルに渡す項目の情報を増やす、または減らすとき。
- 呼び出し先: `fields.map()`
- 参照: `field.autocomplete`, `field.id`, `field.inputType`, `field.label`, `field.localConfidence`, `field.localGuess`, `field.maxlength`, `field.name`, `field.options`, `field.placeholder`, `field.textAfter`, `field.textBefore`

## SmartFormFillController.#getClassifyFieldsRequestBody()
- 位置: L1016-1023
- 役割: 分類タスク名、列挙のバージョン、ページ情報、項目情報をまとめて、分類依頼の本体を作る。
- 触るとき: 分類依頼の形式や列挙のバージョンを変えるとき。
- 呼び出し先: `this.#getFieldDataForClassification()`
- 参照: `this.#pageInfo`

## SmartFormFillController.#getRelevantTabRequestBody()
- 位置: L1031-1045
- 役割: タブ選択タスク用に、ページ、タブ一覧、項目、選択上限をまとめた依頼の本体を作る。
- 触るとき: タブ選択の依頼の形式を変えるとき。
- 呼び出し先: `this.#getFieldDataForClassification()`
- 参照: `lazy.MAX_SELECTED_TABS`, `this.#pageInfo`, `this.#tabList`

## SmartFormFillController.#getTabData()
- 位置: L1053-1068
- 役割: タブ情報に t1, t2 のような連番 ID を振り、ID 付きのタブ情報を作って ID 対応表に保存する。
- 触るとき: モデルに見せるタブ ID の形式を変えるとき。
- 呼び出し先: `tabList.map()`, `this.#tabsById.set()`
- 参照: `this.#tabCounter`
