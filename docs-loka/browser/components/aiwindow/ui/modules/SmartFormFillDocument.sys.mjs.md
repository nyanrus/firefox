# browser/components/aiwindow/ui/modules/SmartFormFillDocument.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillDocument.sys.mjs
source-hash: 2a0f6437d92411b5a14d4d370f46d2d1ce5658c5
lines: 1289

## <module>
- 役割: ページ内のフォーム入力欄を検出してフォーム単位にまとめ、モデル向けの項目データを作る。また値の書き込みと、入力後の結果の報告を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## SmartFormFillDocument.constructor()
- 位置: L266-286
- 役割: 文書ごとの状態 (フォーム、項目 ID、監視対象、カウンタ) を初期値にする。
- 触るとき: 文書単位で新しい状態を持たせるとき。
- 参照: `lazy.SmartFormFillUtils`, `this.#destroyed`, `this.#doc`, `this.#fieldCounter`, `this.#fieldIds`, `this.#fieldsById`, `this.#fillGeneration`, `this.#filledFields`, `this.#formCounter`, `this.#formRoots`, `this.#formUpdateAffectedGroupsMap`, `this.#formUpdateTimeout`, `this.#forms`, `this.#initialized`, `this.#observedRoots`, `this.#observer`, `this.#onFieldOutcomes`, `this.#onFieldsFilled`, `this.#onFormUpdate`, `this.#utils`

## SmartFormFillDocument.initialize()
- 位置: async L300-335
- 役割: 文書の監視を始め、既存の項目を検出してからコールバックを登録する。失敗時は破棄して例外を投げる。
- 触るとき: 初期化に失敗して Smart Form Fill が使えなくなるとき、または起動時の検出の順序を変えるとき。
- 呼び出し先: `this.#detectFields()`, `this.#monitorDocument()`, `this.#monitorFilledFields()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 条件付き依存: `if (!this.#destroyed)` → `this.destroy()`
- 参照: `this.#destroyed`, `this.#initialized`, `this.#onFieldOutcomes`, `this.#onFieldsFilled`, `this.#onFormUpdate`

## SmartFormFillDocument.destroy()
- 位置: L340-382
- 役割: 監視を外し、保持しているマップや参照を空または null にして、破棄済みの状態にする。
- 触るとき: ページを離れるときの解放漏れを調べるとき、または新しい監視対象を足すとき。
- 呼び出し先: `this.#fieldsById.clear()`, `this.#filledFields.clear()`, `this.#formRoots.clear()`, `this.#forms.clear()`, `this.#observer?.disconnect()`, `this.#stopMonitoringFilledFields()`
- 条件付き依存: `if (this.#formUpdateTimeout)` → `this.#doc.defaultView.clearTimeout()`
- 参照: `this.#destroyed`, `this.#doc`, `this.#fieldCounter`, `this.#fieldIds`, `this.#fieldsById`, `this.#fillGeneration`, `this.#filledFields`, `this.#formCounter`, `this.#formRoots`, `this.#formUpdateAffectedGroupsMap`, `this.#formUpdateTimeout`, `this.#forms`, `this.#observedRoots`, `this.#observer`, `this.#onFieldOutcomes`, `this.#onFormUpdate`, `this.#utils`

## SmartFormFillDocument.getFormData()
- 位置: L390-398
- 役割: 検出済みのフォームのうち項目があるものを、id と項目データの形にして返す。
- 触るとき: モデルに送るフォーム情報の形を変えるとき。
- 呼び出し先: `formFields.map()`, `forms.map()`, `this.#getFieldData()`, `this.#getForms()`

## SmartFormFillDocument.getFocusedForm()
- 位置: L407-444
- 役割: フォーカス中の項目が追跡中のフォームに属し、編集可能な項目が十分あれば、そのフォームの情報と空欄の項目 ID を返す。
- 触るとき: フォーカス時に候補を出す判定や、空欄項目の集め方を変えるとき。
- 呼び出し先: `group.fields .filter()`, `group.fields .filter( formField => this.#isSupportedField(formField) && this.#isFillableField(formField) ) .map()`, `group.fields.includes()`, `lazy.FormLikeFactory.findRootForField()`, `this.#formRoots.get()`, `this.#getFieldId()`, `this.#getFocusedField()`, `this.#hasEnoughEditableFields()`, `this.#isFillableField()`, `this.#isSupportedField()`, `this.getFormData()`, `this.getFormData().find()`
- 参照: `formData.fields`, `formData.id`, `group.formId`, `group?.formId`

## SmartFormFillDocument.fillForm()
- 位置: async L457-564
- 役割: レビュー済みの値を、空欄で有効な項目に一つずつ書き込む。中止されたら途中で止め、書いた項目は自動入力済みにして記録する。
- 触るとき: 書き込みの順序、中止の扱い、エラーの扱いを変えるとき。
- 呼び出し先: `Array.isArray()`, `Services.obs.notifyObservers()`, `filledFieldIds.has()`, `this.#allowCancellationCheck()`, `this.#forms?.get()`, `this.#onFieldsFilled()`
- 条件付き依存: `if (typeof value === "string" && !filledFieldIds.has(fieldId))` → `this.#fieldsById.get()`
- 条件付き依存: `if (typeof value === "string" && !filledFieldIds.has(fieldId))` → `formFields.has()`
- 条件付き依存: `if (field && field.isConnected && formFields.has(field))` → `lazy.FormLikeFactory.findRootForField()`
- 条件付き依存: `if (field && field.isConnected && formFields.has(field))` → `this.#isSupportedField()`
- 条件付き依存: `if (field && field.isConnected && formFields.has(field))` → `this.#isFillableField()`
- 条件付き依存: `if (field && field.isConnected && formFields.has(field))` → `lazy.console.error()`
- 条件付き依存: `if (valid)` → `field.setUserInput()`
- 条件付き依存: `if (valid)` → `filledFieldIds.add()`
- 条件付き依存: `if (valid)` → `lazy.console.error()`
- 条件付き依存: `if (valid)` → `filledFieldIds.has()`
- 条件付き依存: `if (filledFieldIds.has(fieldId))` → `lazy.console.error()`
- 条件付き依存: `if (filledFieldIds.has(fieldId))` → `this.#filledFields.set()`
- 参照: `field.autofillState`, `field.isConnected`, `filledFieldIds.size`, `group.fields`, `group.formLike.rootElement`, `lazy.FormAutofillUtils.FIELD_STATES.AUTO_FILLED`, `this.#destroyed`, `this.#fillGeneration`, `value.length`
- XPCOM: `Services.obs`

## SmartFormFillDocument.stopFilling()
- 位置: L575-577
- 役割: 進行中の入力操作の世代を進めて、中止の対象にする。
- 触るとき: 入力の中止を UI から使えるようにするとき。現在は UI に出ていない。
- 参照: `this.#fillGeneration`

## SmartFormFillDocument.#allowCancellationCheck()
- 位置: L584-586
- 役割: メインスレッドのイベントを一度流してから解決する Promise を返し、中止の通知を処理できるようにする。
- 触るとき: 書き込みの途中で中止を確かめる間隔を変えるとき。
- 呼び出し先: `Services.tm.dispatchToMainThread()`
- XPCOM: `Services.tm`

## SmartFormFillDocument.handleEvent()
- 位置: L593-621
- 役割: input、focusout、submit、pagehide のイベントを、埋めた項目の編集の記録や結果の報告に振り分ける。
- 触るとき: 埋めた項目の結果が抜ける、または二重に報告されるとき。
- 呼び出し先: `lazy.FormLikeFactory.findRootForField()`, `this.#onFilledFieldInput()`, `this.#reportOutcomes()`
- 参照: `event.target`, `event.type`, `this.#filledFields?.size`

## SmartFormFillDocument.#monitorFilledFields()
- 位置: L630-637
- 役割: input、focusout、submit、pagehide をシステムグループで監視する。ページ側のスクリプトに止められないようにするため。
- 触るとき: 監視するイベントの種類を増やすとき。
- 呼び出し先: `this.#doc.addEventListener()`, `this.#doc.defaultView?.addEventListener()`

## SmartFormFillDocument.#stopMonitoringFilledFields()
- 位置: L642-649
- 役割: #monitorFilledFields で付けた監視を、同じ対象とオプションで外す。
- 触るとき: 監視の付け方と外し方がずれて、リスナーが残るのを防ぐとき。
- 呼び出し先: `this.#doc.defaultView?.removeEventListener()`, `this.#doc.removeEventListener()`

## SmartFormFillDocument.#onFilledFieldInput()
- 位置: L658-665
- 役割: 入力された要素が埋めた項目であれば、その項目を編集済みとして印を付ける。
- 触るとき: 利用者が編集したかどうかの判定がずれるとき。
- 呼び出し先: `this.#fieldIds.get()`, `this.#filledFields.get()`
- 参照: `filled.edited`

## SmartFormFillDocument.#reportOutcomes()
- 位置: L677-707
- 役割: 条件に合う埋めた項目の状態 (編集の有無、空か、長さ) を集め、フォームごとに報告して、追跡の対象から外す。
- 触るとき: 埋めた後の結果が二重に、または抜けて報告されるとき。
- 呼び出し先: `field.value.trim()`, `matches()`, `statesByFormId.get()`, `statesByFormId.get(formId).push()`, `statesByFormId.has()`, `this.#fieldsById.get()`, `this.#filledFields.delete()`, `this.#onFieldOutcomes()`
- 条件付き依存: `if (!statesByFormId.has(formId))` → `statesByFormId.set()`
- 参照: `field.value.length`, `this.#filledFields`, `this.#onFieldOutcomes`

## SmartFormFillDocument.getSupportedFields()
- 位置: L714-718
- 役割: 全フォームの対応する型の項目を、一つの配列にまとめて返す。
- 触るとき: 対応項目の一覧を外へ渡す箇所を変えるとき。
- 呼び出し先: `Array.from()`, `Array.from(this.#forms.values()).flatMap()`, `fields.filter()`, `this.#forms.values()`, `this.#isSupportedField()`

## SmartFormFillDocument.isSupportedField()
- 位置: L727-729
- 役割: 公開のインターフェースで、判定を内部の #isSupportedField に委ねる。
- 触るとき: 外部から対応項目の判定を使う箇所を調べるとき。
- 呼び出し先: `this.#isSupportedField()`

## SmartFormFillDocument.shouldOfferFill()
- 位置: L740-753
- 役割: 項目が対応型で空欄かつ入力可能で、フォームのグループに属し編集可能な項目が十分にあるときに true を返す。
- 触るとき: 入力欄に候補を出すかどうかの条件を変えるとき。
- 呼び出し先: `lazy.FormLikeFactory.findRootForField()`, `this.#formRoots.get()`, `this.#hasEnoughEditableFields()`, `this.#isFillableField()`, `this.#isSupportedField()`
- 参照: `group?.formId`

## SmartFormFillDocument.#getFieldData()
- 位置: L764-785
- 役割: 項目からラベル、名前、入力型、ヒント、前後の近傍テキスト、ローカル推定の値などを集め、モデル向けの項目データにする。
- 触るとき: モデルに渡す項目の情報を増やす、または減らすとき。
- 呼び出し先: `this.#getFieldLabel()`, `this.#utils.findNearbyText()`
- 参照: `details.confidence`, `details.fieldName`, `details.reason`, `details?.confidence`, `details?.fieldName`, `field.autocomplete`, `field.id`, `field.maxLength`, `field.name`, `field.placeholder`, `field.type`

## SmartFormFillDocument.#normalize()
- 位置: L794-796
- 役割: 連続する空白を一つにまとめ、前後の空白を取り除く。null や undefined は空文字にする。
- 触るとき: ラベルの文字列の正規化ルールを変えるとき。
- 呼び出し先: `value?.replace()`, `value?.replace(/\s+/g, " ").trim()`

## SmartFormFillDocument.#getFieldLabel()
- 位置: L806-825
- 役割: 関連付けられたラベル、aria-labelledby、aria-label の順に、最初に得られたものをラベルとして返す。
- 触るとき: ラベルの取得順や優先順位を変えるとき、または項目のラベルが空に見えるとき。
- 呼び出し先: `Array.from()`, `Array.from(field.labels ?? []) .map()`, `Array.from(field.labels ?? []) .map(labelEl => this.#normalize(labelEl.textContent)) .filter()`, `Array.from(field.labels ?? []) .map(labelEl => this.#normalize(labelEl.textContent)) .filter(Boolean) .join()`, `field .getAttribute()`, `field .getAttribute("aria-labelledby") ?.split()`, `field .getAttribute("aria-labelledby") ?.split(/\s+/) .map()`, `field.getAttribute()`, `field.getRootNode()`, `root.getElementById()`, `this.#normalize()`
- 参照: `field.labels`, `labelEl.textContent`, `root.getElementById?.(id)?.textContent`

## SmartFormFillDocument.#getFieldId()
- 位置: L832-843
- 役割: 項目に f_ で始まる連番の ID を一度だけ振り、ID と項目の対応を両方向に保存する。
- 触るとき: 項目 ID の形式や、再利用の扱いを変えるとき。
- 呼び出し先: `this.#fieldIds.get()`
- 条件付き依存: `if (!fieldId)` → `this.#fieldIds.set()`
- 条件付き依存: `if (!fieldId)` → `this.#fieldsById.set()`
- 参照: `this.#fieldCounter`

## SmartFormFillDocument.#getForms()
- 位置: L851-872
- 役割: フォームごとに対応する項目を ID 付きで集め、推定情報を添える。対応項目が無いフォームは除く。
- 触るとき: フォームのまとめ方や、項目の推定情報の結び付けを変えるとき。
- 呼び出し先: `fieldMap.get()`, `fields .filter()`, `fields .filter(field => this.#isSupportedField(field)) .map()`, `this.#forms.entries()`, `this.#getFieldId()`, `this.#isSupportedField()`, `this.#toFieldMap()`
- 条件付き依存: `if (formFields.length)` → `forms.push()`
- 参照: `formFields.length`

## SmartFormFillDocument.#toFieldMap()
- 位置: L883-887
- 役割: 項目の詳細の配列を、要素をキーにした Map に変換する。
- 触るとき: 項目の詳細を要素と結び付ける方法を変えるとき。
- 呼び出し先: `fieldDetailsList.map()`
- 参照: `fieldDetails.element`

## SmartFormFillDocument.#isSupportedField()
- 位置: L898-911
- 役割: テキストエリアと対応する入力型の input を対象にする。名前の無いコンボボックスの絞り込み欄は除外する。
- 触るとき: 対応する入力欄の範囲を変えるとき。
- 呼び出し先: `HTMLInputElement.isInstance()`, `HTMLTextAreaElement.isInstance()`, `SUPPORTED_INPUT_TYPES.includes()`, `element?.closest()`
- 参照: `element.name`, `element.type`

## SmartFormFillDocument.#getFocusedField()
- 位置: L920-928
- 役割: シャドウ DOM の中まで辿ってフォーカス中の要素を求め、対応する項目ならそれを返す。
- 触るとき: シャドウ DOM 内の入力欄でフォーカスが正しく取れないとき。
- 呼び出し先: `this.#isSupportedField()`
- 参照: `field.shadowRoot.activeElement`, `field?.shadowRoot?.activeElement`, `this.#doc.activeElement`

## SmartFormFillDocument.#isEditableField()
- 位置: L939-945
- 役割: 表示されていて、無効でも読み取り専用でもない項目かどうかを返す。
- 触るとき: 編集可能の判定条件を変えるとき。
- 呼び出し先: `lazy.FormAutofillUtils.isFieldVisible()`
- 参照: `field.disabled`, `field.readOnly`

## SmartFormFillDocument.#isFillableField()
- 位置: L956-958
- 役割: 値が空で、かつ編集可能な項目かどうかを返す。
- 触るとき: 入力可能な項目の判定を変えるとき。
- 呼び出し先: `this.#isEditableField()`
- 参照: `field.value`

## SmartFormFillDocument.#monitorDocument()
- 位置: L966-976
- 役割: 文書に対する MutationObserver を作り、文書のルートの監視を始める。
- 触るとき: DOM の変化の監視対象を変えるとき。文書全体を見るのは、ルート要素が差し替えられても追えるようにするため。
- 呼び出し先: `this.#observeRoot()`, `this.#onMutation()`
- 参照: `this.#doc`, `this.#doc.defaultView.MutationObserver`, `this.#observer`

## SmartFormFillDocument.#observeRoot()
- 位置: L986-993
- 役割: まだ監視していないルートを記録し、MutationObserver の監視を付ける。
- 触るとき: シャドウルートを監視対象に加える条件を変えるとき。
- 呼び出し先: `this.#observedRoots.add()`, `this.#observedRoots.has()`, `this.#observer.observe()`

## SmartFormFillDocument.#removeStaleFields()
- 位置: L1003-1030
- 役割: 各グループから、切り離された項目や別のルートに属する項目を外して ID を解放し、変わったグループを影響リストに入れる。
- 触るとき: 消えた入力欄が候補に残る問題を追うとき。
- 呼び出し先: `group.fields.filter()`, `lazy.FormLikeFactory.findRootForField()`
- 条件付き依存: `if (currentFields.length !== group.fields.length)` → `currentFieldSet.has()`
- 条件付き依存: `if (currentFields.length !== group.fields.length)` → `this.#fieldIds.get()`
- 条件付き依存: `if (fieldId)` → `this.#fieldsById.delete()`
- 条件付き依存: `if (fieldId)` → `this.#fieldIds.delete()`
- 条件付き依存: `if (currentFields.length !== group.fields.length)` → `group.fields.splice()`
- 条件付き依存: `if (currentFields.length !== group.fields.length)` → `affectedGroups.set()`
- 参照: `currentFields.length`, `field.isConnected`, `group.fields`, `group.fields.length`, `this.#formRoots`

## SmartFormFillDocument.#getAddedFields()
- 位置: L1042-1048
- 役割: 追加されたノードのうち要素のものから、項目を再帰的に集める。
- 触るとき: 動的に追加された入力欄が検出されないとき。
- 呼び出し先: `Array.from()`, `Array.from(mutation.addedNodes) .filter()`, `Array.from(mutation.addedNodes) .filter(addedNode => !!addedNode.matches) .flatMap()`, `this.#getFields()`
- 参照: `addedNode.matches`, `mutation.addedNodes`

## SmartFormFillDocument.#addFieldToGroup()
- 位置: L1060-1081
- 役割: 項目のルート要素に対応するグループを既存のものか新規作成で得て、項目をそのグループに加える。
- 触るとき: フォームのグループ分けの基準を変えるとき。
- 呼び出し先: `group.fields.includes()`, `lazy.FormLikeFactory.createFromField()`, `this.#formRoots.get()`
- 条件付き依存: `if (!group)` → `Object.defineProperty()`
- 条件付き依存: `if (!group)` → `this.#formRoots.set()`
- 条件付き依存: `if (!group.fields.includes(field))` → `group.fields.push()`
- 参照: `formLike.rootElement`, `group.fields`

## SmartFormFillDocument.#hasEnoughSupportedFields()
- 位置: L1094-1104
- 役割: グループ内の対応項目が最低数 (既定値 4) 以上あるかを返す。
- 触るとき: フォームとみなす最低項目数の判定を変えるとき。
- 呼び出し先: `group.fields.reduce()`, `this.#isSupportedField()`
- 参照: `lazy.MIN_FORM_FIELDS`

## SmartFormFillDocument.#hasEnoughEditableFields()
- 位置: L1117-1127
- 役割: グループ内の対応かつ編集可能な項目が最低数以上あるかを返す。
- 触るとき: 候補を出すための編集可能項目数の条件を変えるとき。
- 呼び出し先: `group.fields.reduce()`, `this.#isEditableField()`, `this.#isSupportedField()`
- 参照: `lazy.MIN_FORM_FIELDS`

## SmartFormFillDocument.#updateFormGroups()
- 位置: L1139-1167
- 役割: 影響を受けたグループごとに、対応項目が足りなければ登録を外し、足りれば ID を振ってフォームとして登録し、推定情報を更新する。
- 触るとき: フォームとして登録される条件や、フォーム ID の付け方を変えるとき。
- 呼び出し先: `affectedGroups.values()`, `lazy.FormAutofillHeuristics.getFormInfo()`, `this.#hasEnoughSupportedFields()`
- 条件付き依存: `if (affectedGroup.formId)` → `this.#forms.delete()`
- 条件付き依存: `if (!affectedGroup.fields.length)` → `this.#formRoots.delete()`
- 条件付き依存: `if (!affectedGroup.formId)` → `this.#forms.set()`
- 参照: `affectedGroup.fieldDetailsList`, `affectedGroup.fields.length`, `affectedGroup.formId`, `affectedGroup.formLike`, `affectedGroup.formLike.rootElement`, `this.#formCounter`

## SmartFormFillDocument.#onMutation()
- 位置: L1177-1227
- 役割: DOM の変化から、削除された項目を外し、追加された項目をグループに入れる。変化は 300 ミリ秒まとめてから、フォーム更新を発火する。
- 触るとき: 動的な画面でフォームの更新が遅い、または取りこぼすとき。
- 呼び出し先: `affectedGroups.set()`, `mutations.some()`, `this.#addFieldToGroup()`, `this.#doc.defaultView.setTimeout()`, `this.#getAddedFields()`, `this.#triggerFormUpdate()`
- 条件付き依存: `if ( mutations.some( mutation => mutation.type === "childList" && mutation.removedNodes.length ) )` → `this.#removeStaleFields()`
- 条件付き依存: `if (this.#formUpdateTimeout)` → `this.#doc.defaultView.clearTimeout()`
- 参照: `addedField.isConnected`, `affectedGroups.size`, `group.formLike.rootElement`, `mutation.removedNodes.length`, `mutation.type`, `this.#formUpdateAffectedGroupsMap`, `this.#formUpdateTimeout`

## SmartFormFillDocument.#triggerFormUpdate()
- 位置: L1234-1241
- 役割: 近傍テキストのキャッシュを消してからグループを更新し、フォーム情報を更新コールバックに渡す。
- 触るとき: フォーム更新の通知の順序を変えるとき。
- 呼び出し先: `this.#updateFormGroups()`, `this.#utils.clearCache()`
- 条件付き依存: `if (typeof this.#onFormUpdate === "function")` → `this.#onFormUpdate()`
- 条件付き依存: `if (typeof this.#onFormUpdate === "function")` → `this.getFormData()`
- 参照: `this.#onFormUpdate`

## SmartFormFillDocument.#detectFields()
- 位置: async L1250-1256
- 役割: 文書内の全項目をグループに入れ、初期のフォーム登録を行う。
- 触るとき: 起動時に検出する範囲を変えるとき。
- 呼び出し先: `this.#addFieldToGroup()`, `this.#getFields()`, `this.#updateFormGroups()`
- 参照: `this.#doc`, `this.#formRoots`

## SmartFormFillDocument.#getFields()
- 位置: L1267-1287
- 役割: 要素とその子を再帰的に巡って対応する入力欄を生成し、開いているシャドウルートを監視対象に加える。
- 触るとき: シャドウ DOM の中の入力欄の検出範囲を変えるとき。
- 呼び出し先: `element.matches()`, `rootElement.matches()`, `rootElement.querySelectorAll()`
- 条件付き依存: `if (rootElement.shadowRoot)` → `this.#observeRoot()`
- 条件付き依存: `if (rootElement.shadowRoot)` → `this.#getFields()`
- 条件付き依存: `if (element.shadowRoot)` → `this.#observeRoot()`
- 条件付き依存: `if (element.shadowRoot)` → `this.#getFields()`
- 参照: `element.shadowRoot`, `rootElement.matches`, `rootElement.shadowRoot`
