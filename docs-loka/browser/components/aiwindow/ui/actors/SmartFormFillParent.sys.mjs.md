# browser/components/aiwindow/ui/actors/SmartFormFillParent.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillParent.sys.mjs
source-hash: 76d3939dc2714c6f8dc4acc830af5c9269c714f5
lines: 1658

## <module>
- 役割: Smart Form Fill の親アクター。関連タブと欄の分類を要求し、自動入力の生成、レビューダイアログ、タブ選択、補完候補、テレメトリを統括する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## SmartFormFillParent.constructor()
- 位置: L260-278
- 役割: コントローラ、タブ選択、フォームごとの要求状態、テレメトリなどの状態を初期値で作る。
- 触るとき: 状態を新しく足すとき、または初期値の前提を変えるときに見る。
- 呼び出し先: `super()`
- 参照: `lazy.SmartFormFillTelemetry`, `this.#autocompleteFormId`, `this.#autofillGeneration`, `this.#controller`, `this.#destroyed`, `this.#fieldDecisionsByFormId`, `this.#flowIdByFormId`, `this.#formMetadataById`, `this.#formReviewSession`, `this.#smartWindowIds`, `this.#sourceEditorByFormId`, `this.#tabSelectorAborted`, `this.#tabSelectorDialog`, `this.#tabsChangedDuringValueGeneration`, `this.#telemetry`, `this.#userSelectedTabsByFormId`

## SmartFormFillParent.actorCreated()
- 位置: L283-286
- 役割: 現在の Smart Window の ID を控え、タブの TabChange の購読を始める。
- 触るとき: タブ操作で Smart Window の候補が更新されない、または購読が二重になるときに見る。
- 呼び出し先: `lazy.NonPrivateTabs.addEventListener()`, `this.#getSmartWindowIds()`
- 参照: `this.#smartWindowIds`

## SmartFormFillParent.handleEvent()
- 位置: L293-322
- 役割: タブの開閉や属性変更が Smart Window のタブに関わるときだけ、タブ選択を中止して選択を捨て、タブ情報を無効化する。生成中なら無効化を後回しにする。
- 触るとき: タブを閉じたり開いたりした後に候補タブや生成結果が古いまま残るときに見る。
- 呼び出し先: `["TabOpen", "TabClose", "TabAttrModified"].includes()`, `currentSmartWindowIds.has()`, `event.detail.sourceEvents.some()`, `event.detail.windowIds.some()`, `this.#abortTabSelector()`, `this.#getSmartWindowIds()`, `this.#invalidateTabMetadata()`, `this.#smartWindowIds.has()`, `this.#userSelectedTabsByFormId.clear()`
- 参照: `event.type`, `this.#formReviewSession?.generationPending`, `this.#smartWindowIds`, `this.#tabsChangedDuringValueGeneration`

## SmartFormFillParent.#getSelectedTabsFor()
- 位置: L330-336
- 役割: フォームについて、ユーザーが選んだタブがあればそれを、無ければ関連タブの推定結果を id だけの形にして返す。
- 触るとき: 自動入力に使われるタブが選択画面と食い違うときに見る。
- 呼び出し先: `selectedTabs.map()`, `this.#controller.getRelevantTabsFor()`, `this.#userSelectedTabsByFormId.get()`

## SmartFormFillParent.triggerAutofill()
- 位置: async L343-377
- 役割: リージョンを初期化し、Smart Window とフォームを確かめたうえで、関連タブと分類の両方が揃えば選んだタブで自動入力を実行する。分類が失敗していれば何もしない。
- 触るとき: 自動入力を選んでも何も起きないとき、または要求の完了を待つ場所を変えるときに見る。
- 呼び出し先: `Promise.all()`, `lazy.Region.init()`, `lazy.Region.init().catch()`, `lazy.console.error()`, `this.#cannotAutofill()`, `this.#getFocusedForm()`, `this.#getFormMetadataState()`, `this.#getSelectedTabsFor()`, `this.#onIsSmartWindow()`, `this.#performAutofill()`, `this.#startFormMetadataRequests()`
- 参照: `METADATA_STATUS.FAILED`, `METADATA_STATUS.READY`, `focusedForm.id`, `metadata.classificationPromise`, `metadata.classificationStatus`, `metadata.relevantTabsPromise`, `metadata.relevantTabsStatus`, `this.#destroyed`

## SmartFormFillParent.#editSources()
- 位置: async L384-420
- 役割: 関連タブの取得を待ってタブ選択ダイアログを開き、選ばれたタブを保存する。終わったら元のブラウザにフォーカスを戻し、候補ポップアップを再表示させる。
- 触るとき: タブ編集の後にフォーカスが失われる、または選んだタブが次の入力に反映されないときに見る。
- 呼び出し先: `this.#cannotAutofill()`, `this.#getFocusedForm()`, `this.#getFormMetadataState()`, `this.#selectTabs()`, `this.#startFormMetadataRequests()`
- 条件付き依存: `if (selectedTabs)` → `this.#userSelectedTabsByFormId.set()`
- 条件付き依存: `if (browser?.isConnected)` → `browser.focus()`
- 条件付き依存: `if (!this.#destroyed)` → `this.sendAsyncMessage()`
- 参照: `METADATA_STATUS.READY`, `browser?.isConnected`, `focusedForm.id`, `metadata.relevantTabsPromise`, `metadata.relevantTabsStatus`, `this.#destroyed`, `this.browsingContext?.embedderElement`

## SmartFormFillParent.#selectTabs()
- 位置: async L429-519
- 役割: 関連タブを先頭にしてその他のタブと合わせてダイアログへ渡す。戻った id が候補内で、重複がなく上限以内なら採用し、そうでなければ null を返す。
- 触るとき: タブ選択の検証条件を変えるとき、またはダイアログに出すタブが抜けるときに見る。
- 呼び出し先: `Array.isArray()`, `[...suggestedTabs, ...otherTabs].map()`, `[...tabsById.values()] .filter()`, `[...tabsById.values()] .filter( tab => !suggestedTabIds.has(tab.id) && tab.url !== this.manager.documentURI.spec ) .map()`, `chromeWindow.gBrowser .getTabDialogBox()`, `chromeWindow.gBrowser .getTabDialogBox(browser) .open()`, `initiallySelectedTabIds.has()`, `relevantTabs .map()`, `relevantTabs .map(({ id }) => tabsById.get(id)) .filter()`, `relevantTabs .map(({ id }) => tabsById.get(id)) .filter(Boolean) .map()`, `selectableTabIds.has()`, `selectedTabIds.map()`, `selectedTabIds.some()`, `suggestedTabIds.has()`, `suggestedTabs.map()`, `tabsById.get()`, `tabsById.values()`, `this.#controller.getRelevantTabsFor()`, `this.#controller.getTabs()`, `this.#controller.getTabs().map()`, `this.#getSelectedTabsFor()`, `this.#getSelectedTabsFor(formId).map()`, `this.#getSourceEditorState()`, `toDialogTab()`
- 参照: `chromeWindow?.gBrowser`, `dialogArguments.result?.selectedTabIds`, `editorState.opens`, `editorState.result`, `lazy.MAX_SELECTED_TABS`, `lazy.SOURCE_EDITOR_RESULT.ABORTED`, `lazy.SOURCE_EDITOR_RESULT.CANCEL`, `lazy.SOURCE_EDITOR_RESULT.DONE`, `new Set(selectedTabIds).size`, `selectedTabIds.length`, `tab.id`, `tab.url`, `this.#tabSelectorAborted`, `this.#tabSelectorDialog`, `this.browsingContext.embedderElement`, `this.browsingContext.topChromeWindow`, `this.manager.documentURI.spec`

## toDialogTab()
- 位置: L441-445
- 役割: タブ情報に page-icon の URL と選択状態を付けて、ダイアログ用の形にする。
- 触るとき: タブ選択ダイアログのアイコンや選択状態がおかしいときに見る。
- 参照: `tab.url`

## SmartFormFillParent.#abortTabSelector()
- 位置: L524-531
- 役割: 開いているタブ選択ダイアログがあれば、中止扱いで閉じる。
- 触るとき: タブ選択が勝手に閉じられる経路を調べるとき、または中止と完了の区別が崩れるときに見る。
- 呼び出し先: `this.#tabSelectorDialog.abort()`
- 参照: `this.#tabSelectorAborted`, `this.#tabSelectorDialog`

## SmartFormFillParent.receiveMessage()
- 位置: L542-566
- 役割: 子からの IsSmartWindow、FormUpdate、FieldsFilled、FieldOutcomes を対応する処理へ振り分ける。Smart Window でなければ null を返す。
- 触るとき: 子からのメッセージが親で処理されないとき、または新しいメッセージを足すときに見る。
- 呼び出し先: `lazy.Region.init()`, `lazy.Region.init() .catch()`, `lazy.Region.init() .catch(error => lazy.console.error("Could not initialize Region", error) ) .then()`, `lazy.console.error()`, `this.#onFieldOutcomes()`, `this.#onFieldsFilled()`, `this.#onFormUpdate()`, `this.#onIsSmartWindow()`
- 参照: `data.fieldIds`, `data.fields`, `data.id`

## SmartFormFillParent.didDestroy()
- 位置: L571-587
- 役割: タブの購読を外し、ダイアログと生成セッションを中止し、状態をすべて消してコントローラを破棄する。
- 触るとき: ページを離れた後も処理が残るとき、または破棄時の後始末を増やすときに見る。
- 呼び出し先: `lazy.NonPrivateTabs.removeEventListener()`, `this.#abortTabSelector()`, `this.#controller?.destroy()`, `this.#fieldDecisionsByFormId.clear()`, `this.#flowIdByFormId.clear()`, `this.#formMetadataById.clear()`, `this.#formReviewSession?.abort()`, `this.#smartWindowIds.clear()`, `this.#sourceEditorByFormId.clear()`, `this.#userSelectedTabsByFormId.clear()`
- 参照: `this.#controller`, `this.#destroyed`, `this.#formReviewSession`, `this.#tabSelectorDialog`, `this.#tabsChangedDuringValueGeneration`

## SmartFormFillParent.#getController()
- 位置: L594-603
- 役割: コントローラが無ければ、ページ情報と要求の観測者を渡して作る。
- 触るとき: コントローラの生成条件や渡す観測者を変えるときに見る。
- 条件付き依存: `if (!this.#controller)` → `this.#getPageInfo()`
- 条件付き依存: `if (!this.#controller)` → `this.#getRequestObserver()`
- 参照: `lazy.SmartFormFillController`, `this.#controller`

## SmartFormFillParent.#getFocusedForm()
- 位置: L610-618
- 役割: 子にフォーカス中のフォームを問い合わせる。失敗したら null を返す。
- 触るとき: フォーカス中のフォームが取れず何も起きないときに見る。
- 呼び出し先: `this.sendQuery()`, `this.sendQuery("SmartFormFill:GetFocusedForm").catch()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `this.#destroyed`

## SmartFormFillParent.#getFormMetadataState()
- 位置: L626-650
- 役割: フォームごとの要求状態を返す。無ければ作ってフロー ID を発行し、欄の構造が変わっていれば状態を無効化する。
- 触るとき: 欄の増減の後に要求が出し直されない、または別フォームの状態が混ざるときに見る。
- 呼び出し先: `this.#formMetadataById.get()`
- 条件付き依存: `if (!metadata)` → `this.#formMetadataById.set()`
- 条件付き依存: `if (!metadata)` → `this.#flowIdByFormId.set()`
- 条件付き依存: `if (!metadata)` → `crypto.randomUUID()`
- 条件付き依存: `if (!(!metadata))` → `this.#hasFormStructureChanged()`
- 条件付き依存: `if (this.#hasFormStructureChanged(metadata.formData, formData))` → `this.#invalidateFormMetadata()`
- 参照: `METADATA_STATUS.IDLE`, `focusedForm.fields`, `focusedForm.id`, `metadata.formData`

## SmartFormFillParent.#hasFormStructureChanged()
- 位置: L659-668
- 役割: 欄の数が変わったか、新しい欄 id が増えたときに true を返す。値の変化は見ない。
- 触るとき: 構造変化の判定条件を変えるときに見る。
- 呼び出し先: `formData.fields.some()`, `previousFieldIds.has()`, `previousFormData.fields.map()`
- 参照: `formData.fields.length`, `previousFormData.fields.length`

## SmartFormFillParent.#invalidateFormMetadata()
- 位置: L676-691
- 役割: フォームの要求リビジョンを進め、状態を未取得に戻し、コントローラの該当フォームを無効化する。新しいフロー ID を発行し、そのフォームの判定とエディタ状態を消す。
- 触るとき: 欄が増減した後に古い分類や関連タブが使われるとき、またはテレメトリのフローの区切りを確かめるときに見る。
- 呼び出し先: `crypto.randomUUID()`, `this.#controller.invalidateForm()`, `this.#fieldDecisionsByFormId.delete()`, `this.#flowIdByFormId.set()`, `this.#sourceEditorByFormId.delete()`
- 参照: `METADATA_STATUS.IDLE`, `formData.id`, `metadata.classificationPromise`, `metadata.classificationRevision`, `metadata.classificationStatus`, `metadata.formData`, `metadata.relevantTabsPromise`, `metadata.relevantTabsRevision`, `metadata.relevantTabsStatus`

## SmartFormFillParent.#startFormMetadataRequests()
- 位置: L698-706
- 役割: 関連タブと分類のうち、まだ未取得のものだけ要求を始める。
- 触るとき: 同じ要求が二重に出る、または取得されないときに見る。
- 条件付き依存: `if (metadata.relevantTabsStatus === METADATA_STATUS.IDLE)` → `this.#loadRelevantTabs()`
- 条件付き依存: `if (metadata.classificationStatus === METADATA_STATUS.IDLE)` → `this.#loadFieldClassifications()`
- 参照: `METADATA_STATUS.IDLE`, `metadata.classificationStatus`, `metadata.relevantTabsStatus`

## SmartFormFillParent.#loadRelevantTabs()
- 位置: L714-741
- 役割: 関連タブを要求し、結果が古くなければ状態を ready にして補完の更新を子へ送る。
- 触るとき: 関連タブの取得が終わっても候補が更新されないとき、または失敗の扱いを変えるときに見る。
- 呼び出し先: `this.#getController()`, `this.#getController() .findRelevantTabs()`, `this.#getController() .findRelevantTabs(metadata.formData) .catch()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (revision === metadata.relevantTabsRevision && !this.#destroyed)` → `lazy.console.error()`
- 参照: `METADATA_STATUS.LOADING`, `METADATA_STATUS.READY`, `metadata.formData`, `metadata.relevantTabsPromise`, `metadata.relevantTabsRevision`, `metadata.relevantTabsStatus`, `this.#destroyed`

## SmartFormFillParent.#loadFieldClassifications()
- 位置: L749-777
- 役割: 欄の分類を要求する。成功なら ready、失敗なら failed にして補完の更新を子へ送る。
- 触るとき: 分類が failed のまま自動入力が止まるときに見る。
- 呼び出し先: `lazy.console.error()`, `this.#getController()`, `this.#getController() .classifyFields()`, `this.#getController() .classifyFields(metadata.formData) .then()`, `this.sendAsyncMessage()`
- 参照: `METADATA_STATUS.FAILED`, `METADATA_STATUS.LOADING`, `METADATA_STATUS.READY`, `metadata.classificationPromise`, `metadata.classificationRevision`, `metadata.classificationStatus`, `metadata.formData`, `this.#destroyed`

## SmartFormFillParent.#performAutofill()
- 位置: async L787-881
- 役割: レビューダイアログを開き、ページ本文と選んだタブの本文を集めて生成を依頼する。結果があればレビューに値を渡し、失敗や候補なしならその旨を伝える。世代が古くなったら途中で止める。
- 触るとき: 自動入力の流れ全体を変えるとき、またはレビューに候補が出ない、生成失敗と表示されるときに見る。本文は全タブ合わせて約 10000 字に分ける。
- 呼び出し先: `Math.ceil()`, `Promise.all()`, `this.#cancelFormReviewGeneration()`, `this.#cannotApplyAutofill()`, `this.#controller .autofill()`, `this.#controller .autofill( focusedForm.id, focusedForm.emptyFieldIds, selectedTabs, tabContentById, pageText ) .then()`, `this.#finishFormReviewGeneration()`, `this.#getFormReviewFields()`, `this.#getPageText()`, `this.#getTabsContent()`, `this.#openFormReview()`, `this.#recordTabSelectionOutcome()`, `this.#setReviewValues()`
- 条件付き依存: `if (!reviewSession)` → `this.#cancelFormReviewGeneration()`
- 条件付き依存: `if (generationResult.error)` → `this.#cannotApplyAutofill()`
- 条件付き依存: `if (!this.#cannotApplyAutofill(generation))` → `lazy.console.error()`
- 条件付き依存: `if (!this.#cannotApplyAutofill(generation))` → `this.#finishFormReviewGeneration()`
- 参照: `fields.length`, `focusedForm.emptyFieldIds`, `focusedForm.id`, `generationResult.error`, `generationResult.result`, `lazy.FORM_REVIEW_ERRORS.GENERATION_FAILED`, `lazy.FORM_REVIEW_ERRORS.NO_SUGGESTIONS`, `selectedTabs.length`, `this.#autofillGeneration`, `this.#formReviewSession`, `this.manager.documentURI.spec`

## SmartFormFillParent.#openFormReview()
- 位置: async L892-923
- 役割: レビューのセッションを作って開き、準備できたセッションを返す。開けなければ null を返す。
- 触るとき: レビューダイアログが開かないとき、またはダイアログとの結び付け方を変えるときに見る。
- 呼び出し先: `session.open()`
- 参照: `chromeWindow?.gBrowser`, `lazy.SmartFormFillReviewSession`, `this.#destroyed`, `this.#formReviewSession`, `this.browsingContext.embedderElement`, `this.browsingContext.topChromeWindow`

## onCancelGeneration()
- 位置: L906-907
- 役割: このフォームと世代の生成をキャンセルする。
- 触るとき: ダイアログのキャンセルが生成に届かないときに見る。
- 呼び出し先: `this.#cancelFormReviewGeneration()`

## onClose()
- 位置: L908-908
- 役割: 閉じたセッションを #onFormReviewClosed に渡す。
- 触るとき: ダイアログを閉じた後に状態が残るときに見る。
- 呼び出し先: `this.#onFormReviewClosed()`

## onFill()
- 位置: L909-909
- 役割: レビュー済みの値を #fillReviewedFields に渡して、フィルを実行する。
- 触るとき: レビュー後の入力が埋まらないときに見る。
- 呼び出し先: `this.#fillReviewedFields()`

## SmartFormFillParent.#finishFormReviewGeneration()
- 位置: L934-945
- 役割: 同じセッションで世代が最新なら、生成結果をセッションに渡す。完了したら後回しのタブ情報を更新する。
- 触るとき: 生成結果がダイアログに届かない、または古い結果が表示されるときに見る。
- 呼び出し先: `session.completeGeneration()`, `this.#cannotApplyAutofill()`
- 条件付き依存: `if (session.completeGeneration(result))` → `this.#refreshDeferredTabData()`
- 参照: `this.#formReviewSession`

## SmartFormFillParent.#onFormReviewClosed()
- 位置: L953-960
- 役割: 閉じたセッションが現在のものなら参照を消し、後回しのタブ情報を更新する。
- 触るとき: 次のレビューが開けないとき、または閉じた後もセッションが残るときに見る。
- 呼び出し先: `this.#refreshDeferredTabData()`
- 参照: `this.#formReviewSession`

## SmartFormFillParent.#refreshDeferredTabData()
- 位置: L967-974
- 役割: 生成中に変わったタブ情報があれば、タブ情報を無効化する。
- 触るとき: 生成中にタブを変えた結果が反映されないときに見る。
- 呼び出し先: `this.#invalidateTabMetadata()`
- 参照: `this.#tabsChangedDuringValueGeneration`

## SmartFormFillParent.#cancelFormReviewGeneration()
- 位置: L983-990
- 役割: 世代が最新で破棄されていなければ世代を進め、コントローラの自動入力をキャンセルする。
- 触るとき: キャンセル後も生成が続くとき、または古いキャンセルが新しい生成を止めるときに見る。
- 呼び出し先: `this.#controller.cancelAutofill()`
- 参照: `this.#autofillGeneration`, `this.#destroyed`

## SmartFormFillParent.#getFormReviewFields()
- 位置: L1001-1024
- 役割: 生成された値に現在の欄のラベル、プレースホルダ、名前を付けてレビュー用の一覧にする。欄が無くなった値は除く。
- 触るとき: レビュー画面の欄の情報が空になる、または消えた欄の値が残るときに見る。
- 呼び出し先: `fieldDataById.get()`, `formData?.fields.map()`, `reviewFields.push()`, `this.#formMetadataById.get()`
- 参照: `field.id`, `fieldData.label`, `fieldData.name`, `fieldData.placeholder`, `result.fields`, `result.id`, `this.#formMetadataById.get(result.id)?.formData`

## SmartFormFillParent.#fillReviewedFields()
- 位置: async L1034-1074
- 役割: レビュー結果を記録し、値が空でないものだけを子の SmartFormFill:FillForm に送る。結果は hasErrors、cancelled、件数の形に整えて返す。失敗時は hasErrors を立てる。
- 触るとき: レビュー後の入力が埋まらない、または件数の表示が合わないときに見る。
- 呼び出し先: `fields.filter()`, `this.#recordFieldReviewOutcomes()`, `this.sendQuery()`, `value.trim()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `result.cancelled`, `result.filledFieldCount`, `result.hasErrors`, `this.#destroyed`

## SmartFormFillParent.#getTabsContent()
- 位置: async L1084-1104
- 役割: 選んだタブごとに本文を取り、id をキーにした Map にまとめる。取得できなかったタブは含めない。
- 触るとき: 選んだタブの本文が生成に入らないときに見る。
- 呼び出し先: `Promise.allSettled()`, `Promise.resolve()`, `selectedTabs.map()`, `this.#controller.getTabData()`
- 条件付き依存: `if (tabData)` → `this.#getPageText(tabData.url, textCharLimitPerTab).then()`
- 条件付き依存: `if (tabData)` → `this.#getPageText()`
- 条件付き依存: `if (tabData)` → `tabContentById.set()`
- 参照: `selectedTab.id`, `tabData.url`

## SmartFormFillParent.#getPageText()
- 位置: async L1114-1143
- 役割: 指定 URL の文書から PageExtractor で本文を取る。文書が開いていなければそのタブから取る。取れなければ空文字を返す。
- 触るとき: 本文が空になって生成が弱くなるとき、または抽出の条件(除去の有無、文字数)を変えるときに見る。
- 呼び出し先: `pageExtractor.getText()`, `windowGlobal.getActor()`
- 条件付き依存: `if (windowGlobal.documentURI.spec !== sourceUrl)` → `lazy.GetPageContent.getTabWithURL()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `extraction?.text`, `tab?.linkedBrowser.browsingContext?.currentWindowGlobal`, `this.#destroyed`, `this.manager`, `windowGlobal.documentURI.spec`

## SmartFormFillParent.#getPageInfo()
- 位置: L1150-1157
- 役割: 文書の URL とタイトルを PageInfo として返す。
- 触るとき: コントローラに渡すページ情報が古いとき、または項目を増やすときに見る。
- 参照: `this.manager`, `windowGlobal.documentTitle`, `windowGlobal.documentURI.spec`

## SmartFormFillParent.#getSmartWindowIds()
- 位置: L1164-1170
- 役割: 有効な AI Window のウィンドウ内部 ID の集合を返す。
- 触るとき: Smart Window の判定がタブの変化と合わないときに見る。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows .filter()`, `lazy.BrowserWindowTracker.orderedWindows .filter(window => lazy.AIWindow.isAIWindowActive(window)) .map()`
- 参照: `window.windowGlobalChild.innerWindowId`

## SmartFormFillParent.#invalidateTabMetadata()
- 位置: L1175-1188
- 役割: 全フォームの関連タブ状態を未取得に戻し、コントローラのタブ情報を無効化して、補完の更新を子へ送る。
- 触るとき: タブを開閉した後に古い関連タブが使われるときに見る。
- 呼び出し先: `this.#controller.invalidateTabs()`, `this.#formMetadataById.values()`, `this.sendAsyncMessage()`
- 参照: `METADATA_STATUS.IDLE`, `metadata.relevantTabsPromise`, `metadata.relevantTabsRevision`, `metadata.relevantTabsStatus`, `this.#controller`, `this.#destroyed`

## SmartFormFillParent.#cannotAutofill()
- 位置: L1195-1201
- 役割: Smart Window でないか、コントローラが無いときに true を返す。
- 触るとき: 自動入力が効かない条件を足す、または外すときに見る。
- 呼び出し先: `this.#onIsSmartWindow()`
- 参照: `this.#controller`

## SmartFormFillParent.#cannotApplyAutofill()
- 位置: L1210-1212
- 役割: 自動入力を止める条件に加えて、世代が最新でないときも true を返す。結果を適用してよいかの判定に使う。
- 触るとき: 古い世代の結果が適用される、または有効な結果が捨てられるときに見る。
- 呼び出し先: `this.#cannotAutofill()`
- 参照: `this.#autofillGeneration`

## SmartFormFillParent.#onIsSmartWindow()
- 位置: L1219-1228
- 役割: 破棄されておらず、トップのウィンドウが有効な Smart Window で、地域が禁止リストに無ければ true を返す。
- 触るとき: Smart Form Fill の提供条件を変えるとき、または有効な Smart Window で機能が出ないときに見る。
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `this.#isDisallowedRegion()`
- 参照: `this.#destroyed`, `this.browsingContext.topChromeWindow`

## SmartFormFillParent.#isDisallowedRegion()
- 位置: L1236-1244
- 役割: ホーム地域を禁止リストと照合する。地域が不明なら許可扱いにする。
- 触るとき: 禁止地域の設定の扱いを変えるとき、または特定の地域だけ止まるときに見る。
- 呼び出し先: `lazy.Region.home?.toUpperCase()`, `lazy.disallowedRegions .split()`, `lazy.disallowedRegions .split(",") .map()`, `lazy.disallowedRegions .split(",") .map(region => region.trim().toUpperCase()) .filter()`, `lazy.disallowedRegions .split(",") .map(region => region.trim().toUpperCase()) .filter(Boolean) .includes()`, `region.trim()`, `region.trim().toUpperCase()`

## SmartFormFillParent.#onFormUpdate()
- 位置: L1251-1279
- 役割: 子から届いた現在のフォーム一覧と突き合わせる。無くなったフォームの状態はすべて消し、欄の構造が変わったフォームは状態を無効化する。
- 触るとき: フォームが消えた後も古い状態が残る、または欄が増えたのに候補が更新されないときに見る。
- 呼び出し先: `Array.isArray()`, `formDataList.map()`, `formsById.get()`, `this.#hasFormStructureChanged()`
- 条件付き依存: `if (!formData)` → `this.#controller.invalidateForm()`
- 条件付き依存: `if (!formData)` → `this.#formMetadataById.delete()`
- 条件付き依存: `if (!formData)` → `this.#flowIdByFormId.delete()`
- 条件付き依存: `if (!formData)` → `this.#fieldDecisionsByFormId.delete()`
- 条件付き依存: `if (!formData)` → `this.#sourceEditorByFormId.delete()`
- 条件付き依存: `if (!formData)` → `this.#userSelectedTabsByFormId.delete()`
- 条件付き依存: `if (this.#hasFormStructureChanged(metadata.formData, formData))` → `this.#invalidateFormMetadata()`
- 参照: `formData.id`, `metadata.classificationRevision`, `metadata.formData`, `metadata.relevantTabsRevision`, `this.#destroyed`, `this.#formMetadataById`

## SmartFormFillParent.searchAutoCompleteEntries()
- 位置: async L1300-1335
- 役割: フォーカス中の欄が空のときだけ Smart Form Fill の補完項目を作って返す。欄に値が入っている、または分類が失敗していれば null を返す。
- 触るとき: 補完候補が出ない、または入力済みの欄に候補が出るときに見る。候補を出すかどうかの判定はこの関数だけで行う。
- 呼び出し先: `focusedForm?.emptyFieldIds.has()`, `lazy.SmartFormFillAutocomplete.createItemsAsync()`, `this.#controller.getTabs()`, `this.#getFocusedForm()`, `this.#getFormMetadataState()`, `this.#startFormMetadataRequests()`
- 参照: `METADATA_STATUS.FAILED`, `entries.length`, `focusedForm.focusedFieldId`, `focusedForm.id`, `metadata.classificationStatus`, `options.focusElementId`, `this.#autocompleteFormId`, `this.#controller.getTabs().length`, `this.#destroyed`

## SmartFormFillParent.onAutoCompletePopupOpened()
- 位置: L1340-1342
- 役割: 補完ポップアップが開いたときに、タブの出どころ情報を更新する。
- 触るとき: ポップアップの行にタブ名が出ないときに見る。
- 呼び出し先: `this.#updateAutoCompletePopupSources()`

## SmartFormFillParent.onAutoCompletePopupUpdated()
- 位置: L1347-1349
- 役割: 補完ポップアップが更新されたときに、タブの出どころ情報を更新する。
- 触るとき: ポップアップ更新後もタブ名が古いままのときに見る。
- 呼び出し先: `this.#updateAutoCompletePopupSources()`

## SmartFormFillParent.#updateAutoCompletePopupSources()
- 位置: L1354-1368
- 役割: 対象フォームの関連タブが ready なら、選んだタブの情報をポップアップの出どころとして渡す。
- 触るとき: 補完の行に出どころが空や古いまま出るときに見る。
- 呼び出し先: `lazy.SmartFormFillAutocomplete.updatePopupSources()`, `this.areRelevantTabsReady()`, `this.getSelectedTabSources()`
- 参照: `this.#autocompleteFormId`, `this.#destroyed`, `this.browsingContext.top.embedderElement`

## SmartFormFillParent.onAutoCompleteEntrySelected()
- 位置: L1382-1396
- 役割: 選ばれた補完項目の名前に応じて、自動入力(SmartFormFill:Start)かタブ編集(SmartFormFill:EditSources)を始める。他の名前は何もしない。
- 触るとき: 補完項目を選んでも動かないとき、または補完項目の種類を増やすときに見る。
- 呼び出し先: `this.#editSources()`, `this.triggerAutofill()`
- 参照: `this.#destroyed`

## SmartFormFillParent.getSelectedTabSources()
- 位置: L1405-1417
- 役割: 選んだタブ(無ければ推定のタブ)について、タイトル(無ければ URL)とファビコンの表示用データを返す。
- 触るとき: 補完行の出どころ表示が合わないときに見る。
- 呼び出し先: `this.#controller.getTabData()`, `this.#getSelectedTabsFor()`, `this.#getSelectedTabsFor(formId) .map()`, `this.#getSelectedTabsFor(formId) .map(({ id }) => this.#controller.getTabData(id)) .filter()`, `this.#getSelectedTabsFor(formId) .map(({ id }) => this.#controller.getTabData(id)) .filter(Boolean) .map()`
- 参照: `tab.title`, `tab.url`, `this.#controller`

## SmartFormFillParent.areRelevantTabsReady()
- 位置: L1425-1434
- 役割: フォームの関連タブの状態が ready なら true を返す。
- 触るとき: 関連タブの取得前に補完行が出る条件を変えるときに見る。
- 呼び出し先: `this.#formMetadataById.get()`
- 参照: `METADATA_STATUS.READY`, `this.#destroyed`, `this.#formMetadataById.get(formId)?.relevantTabsStatus`

## SmartFormFillParent.hasSourceTabs()
- 位置: L1441-1443
- 役割: コントローラにタブの出どころがあるかを返す。
- 触るとき: 出どころが無いのに出どころ欄が出る、または出るべきなのに出ないときに見る。
- 呼び出し先: `Boolean()`
- 参照: `this.#controller?.hasSourceTabs`

## SmartFormFillParent.#getFlowId()
- 位置: L1453-1455
- 役割: フォームの現在のフロー ID を返す。無ければ空文字を返す。
- 触るとき: テレメトリのイベントが同じフローにまとまるかを確かめるときに見る。
- 呼び出し先: `this.#flowIdByFormId.get()`

## SmartFormFillParent.#getSourceEditorState()
- 位置: L1465-1474
- 役割: フォームのタブ編集の状態を返す。無ければ開いた回数 0 の状態を作る。
- 触るとき: タブ編集の開いた回数や結果が記録に出ないときに見る。
- 呼び出し先: `this.#sourceEditorByFormId.get()`
- 条件付き依存: `if (!state)` → `this.#sourceEditorByFormId.set()`

## SmartFormFillParent.#recordTabSelectionOutcome()
- 位置: L1482-1488
- 役割: 自動入力の開始時点で、提案されたタブ、最終的なタブ、編集の状態をテレメトリに送る。
- 触るとき: タブ選択の計測項目を増やす、または提案と最終選択が合わないときに見る。
- 呼び出し先: `this.#controller.getRelevantTabsFor()`, `this.#getFlowId()`, `this.#sourceEditorByFormId.get()`, `this.#telemetry.sendRelevantTabsOutcomeTelemetry()`

## SmartFormFillParent.#setReviewValues()
- 位置: L1497-1504
- 役割: レビューに出した値を、フォームの判定の記録に保存する。判定の記録が無ければ何もしない。
- 触るとき: レビューの値がテレメトリの比較に使われないときに見る。
- 呼び出し先: `fields.map()`, `this.#fieldDecisionsByFormId.get()`
- 参照: `round.reviewValues`

## SmartFormFillParent.#recordFieldReviewOutcomes()
- 位置: L1514-1528
- 役割: 生成値と送信された値を比べて、レビュー結果をテレメトリに送る。一度送ったら保存値を消す。
- 触るとき: レビュー結果の計測が重複する、または欠けるときに見る。
- 呼び出し先: `this.#fieldDecisionsByFormId.get()`, `this.#telemetry.sendFillFieldReviewOutcomeTelemetry()`
- 参照: `round.decisions`, `round.flowId`, `round.reviewValues`, `round?.reviewValues`

## SmartFormFillParent.#onFieldsFilled()
- 位置: L1537-1548
- 役割: ページが埋めたと報告した欄の id を、判定の記録と合わせてフィル結果のテレメトリとして送る。
- 触るとき: どの欄が埋まったかの計測がずれるときに見る。
- 呼び出し先: `this.#fieldDecisionsByFormId.get()`, `this.#telemetry.sendFillFieldTelemetry()`
- 参照: `round.decisions`, `round.flowId`

## SmartFormFillParent.#onFieldOutcomes()
- 位置: L1563-1574
- 役割: 欄ごとの編集の有無、空かどうか、文字数の変化を、判定の記録と合わせて結果のテレメトリに送る。
- 触るとき: 入力後の欄の状態の計測項目を増やすときに見る。
- 呼び出し先: `this.#fieldDecisionsByFormId.get()`, `this.#telemetry.sendFillFieldOutcomeTelemetry()`
- 参照: `round.decisions`, `round.flowId`

## SmartFormFillParent.#getRequestObserver()
- 位置: L1581-1656
- 役割: コントローラが要求を出したときに呼ばれる観測者を作る。関連タブ、分類、生成の開始、成功、失敗をそれぞれテレメトリに渡す。
- 触るとき: 要求の計測が抜けるとき、または観測者が受け取る引数を変えるときに見る。

## onRelevantTabsDispatched()
- 位置: L1583-1589
- 役割: 関連タブ要求の開始を、フォームのフロー ID つきでテレメトリに記録し、そのフローを返す。
- 触るとき: 関連タブ要求の計測の開始点を確かめるときに見る。
- 呼び出し先: `this.#getFlowId()`, `this.#telemetry.startRelevantTabsRequest()`

## onRelevantTabsAnswered()
- 位置: L1591-1596
- 役割: 関連タブの応答を、対応するフローに紐づけてテレメトリに送る。
- 触るとき: 関連タブの応答の計測が欠けるときに見る。
- 呼び出し先: `this.#telemetry.sendRelevantTabsResponseTelemetry()`

## onRelevantTabsFailed()
- 位置: L1598-1599
- 役割: 関連タブ要求の失敗を、対応するフローに紐づけてテレメトリに送る。
- 触るとき: 関連タブの失敗が計測に出ないときに見る。
- 呼び出し先: `this.#telemetry.sendRelevantTabsErrorTelemetry()`

## onClassifyDispatched()
- 位置: L1601-1606
- 役割: 分類要求の開始を、フォームのフロー ID つきでテレメトリに記録し、そのフローを返す。
- 触るとき: 分類要求の計測の開始点を確かめるときに見る。
- 呼び出し先: `this.#getFlowId()`, `this.#telemetry.startClassifyRequest()`

## onClassifyAnswered()
- 位置: L1608-1609
- 役割: 分類の応答を、対応するフローに紐づけてテレメトリに送る。
- 触るとき: 分類の応答の計測が欠けるときに見る。
- 呼び出し先: `this.#telemetry.sendClassifyResponseTelemetry()`

## onClassifyFailed()
- 位置: L1611-1612
- 役割: 分類要求の失敗を、対応するフローに紐づけてテレメトリに送る。
- 触るとき: 分類の失敗が計測に出ないときに見る。
- 呼び出し先: `this.#telemetry.sendClassifyErrorTelemetry()`

## onGenerateDispatched()
- 位置: L1614-1619
- 役割: 生成要求の開始を、フォームのフロー ID つきでテレメトリに記録し、そのフローを返す。
- 触るとき: 生成要求の計測の開始点を確かめるときに見る。
- 呼び出し先: `this.#getFlowId()`, `this.#telemetry.startGenerateRequest()`

## onGenerateAnswered()
- 位置: L1621-1651
- 役割: 生成結果を計測に送り、欄ごとの判断をフィールド、分類、トークン、生成値から解決して、フォームの判定の記録に保存する。
- 触るとき: 生成後の欄ごとの判断の記録が合わないとき、または判断の項目を増やすときに見る。
- 呼び出し先: `this.#fieldDecisionsByFormId.set()`, `this.#telemetry.resolveFieldDecisions()`, `this.#telemetry.sendGenerateResponseTelemetry()`
- 参照: `flow.flowId`

## onGenerateFailed()
- 位置: L1653-1654
- 役割: 生成要求の失敗を、対応するフローに紐づけてテレメトリに送る。
- 触るとき: 生成の失敗が計測に出ないときに見る。
- 呼び出し先: `this.#telemetry.sendGenerateErrorTelemetry()`
