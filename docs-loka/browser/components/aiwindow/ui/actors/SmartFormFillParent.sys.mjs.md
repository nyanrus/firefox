# browser/components/aiwindow/ui/actors/SmartFormFillParent.sys.mjs

source: browser/components/aiwindow/ui/actors/SmartFormFillParent.sys.mjs
source-hash: 76d3939dc2714c6f8dc4acc830af5c9269c714f5
lines: 1658

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## SmartFormFillParent.constructor()
- 位置: L260-278
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `lazy.SmartFormFillTelemetry`, `this.#autocompleteFormId`, `this.#autofillGeneration`, `this.#controller`, `this.#destroyed`, `this.#fieldDecisionsByFormId`, `this.#flowIdByFormId`, `this.#formMetadataById`, `this.#formReviewSession`, `this.#smartWindowIds`, `this.#sourceEditorByFormId`, `this.#tabSelectorAborted`, `this.#tabSelectorDialog`, `this.#tabsChangedDuringValueGeneration`, `this.#telemetry`, `this.#userSelectedTabsByFormId`

## SmartFormFillParent.actorCreated()
- 位置: L283-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NonPrivateTabs.addEventListener()`, `this.#getSmartWindowIds()`
- 参照: `this.#smartWindowIds`

## SmartFormFillParent.handleEvent()
- 位置: L293-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["TabOpen", "TabClose", "TabAttrModified"].includes()`, `currentSmartWindowIds.has()`, `event.detail.sourceEvents.some()`, `event.detail.windowIds.some()`, `this.#abortTabSelector()`, `this.#getSmartWindowIds()`, `this.#invalidateTabMetadata()`, `this.#smartWindowIds.has()`, `this.#userSelectedTabsByFormId.clear()`
- 参照: `event.type`, `this.#formReviewSession?.generationPending`, `this.#smartWindowIds`, `this.#tabsChangedDuringValueGeneration`

## SmartFormFillParent.#getSelectedTabsFor()
- 位置: L330-336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `selectedTabs.map()`, `this.#controller.getRelevantTabsFor()`, `this.#userSelectedTabsByFormId.get()`

## SmartFormFillParent.triggerAutofill()
- 位置: async L343-377
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `lazy.Region.init()`, `lazy.Region.init().catch()`, `lazy.console.error()`, `this.#cannotAutofill()`, `this.#getFocusedForm()`, `this.#getFormMetadataState()`, `this.#getSelectedTabsFor()`, `this.#onIsSmartWindow()`, `this.#performAutofill()`, `this.#startFormMetadataRequests()`
- 参照: `METADATA_STATUS.FAILED`, `METADATA_STATUS.READY`, `focusedForm.id`, `metadata.classificationPromise`, `metadata.classificationStatus`, `metadata.relevantTabsPromise`, `metadata.relevantTabsStatus`, `this.#destroyed`

## SmartFormFillParent.#editSources()
- 位置: async L384-420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cannotAutofill()`, `this.#getFocusedForm()`, `this.#getFormMetadataState()`, `this.#selectTabs()`, `this.#startFormMetadataRequests()`
- 条件付き依存: `if (selectedTabs)` → `this.#userSelectedTabsByFormId.set()`
- 条件付き依存: `if (browser?.isConnected)` → `browser.focus()`
- 条件付き依存: `if (!this.#destroyed)` → `this.sendAsyncMessage()`
- 参照: `METADATA_STATUS.READY`, `browser?.isConnected`, `focusedForm.id`, `metadata.relevantTabsPromise`, `metadata.relevantTabsStatus`, `this.#destroyed`, `this.browsingContext?.embedderElement`

## SmartFormFillParent.#selectTabs()
- 位置: async L429-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `[...suggestedTabs, ...otherTabs].map()`, `[...tabsById.values()] .filter()`, `[...tabsById.values()] .filter( tab => !suggestedTabIds.has(tab.id) && tab.url !== this.manager.documentURI.spec ) .map()`, `chromeWindow.gBrowser .getTabDialogBox()`, `chromeWindow.gBrowser .getTabDialogBox(browser) .open()`, `initiallySelectedTabIds.has()`, `relevantTabs .map()`, `relevantTabs .map(({ id }) => tabsById.get(id)) .filter()`, `relevantTabs .map(({ id }) => tabsById.get(id)) .filter(Boolean) .map()`, `selectableTabIds.has()`, `selectedTabIds.map()`, `selectedTabIds.some()`, `suggestedTabIds.has()`, `suggestedTabs.map()`, `tabsById.get()`, `tabsById.values()`, `this.#controller.getRelevantTabsFor()`, `this.#controller.getTabs()`, `this.#controller.getTabs().map()`, `this.#getSelectedTabsFor()`, `this.#getSelectedTabsFor(formId).map()`, `this.#getSourceEditorState()`, `toDialogTab()`
- 参照: `chromeWindow?.gBrowser`, `dialogArguments.result?.selectedTabIds`, `editorState.opens`, `editorState.result`, `lazy.MAX_SELECTED_TABS`, `lazy.SOURCE_EDITOR_RESULT.ABORTED`, `lazy.SOURCE_EDITOR_RESULT.CANCEL`, `lazy.SOURCE_EDITOR_RESULT.DONE`, `new Set(selectedTabIds).size`, `selectedTabIds.length`, `tab.id`, `tab.url`, `this.#tabSelectorAborted`, `this.#tabSelectorDialog`, `this.browsingContext.embedderElement`, `this.browsingContext.topChromeWindow`, `this.manager.documentURI.spec`

## toDialogTab()
- 位置: L441-445
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `tab.url`

## SmartFormFillParent.#abortTabSelector()
- 位置: L524-531
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabSelectorDialog.abort()`
- 参照: `this.#tabSelectorAborted`, `this.#tabSelectorDialog`

## SmartFormFillParent.receiveMessage()
- 位置: L542-566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Region.init()`, `lazy.Region.init() .catch()`, `lazy.Region.init() .catch(error => lazy.console.error("Could not initialize Region", error) ) .then()`, `lazy.console.error()`, `this.#onFieldOutcomes()`, `this.#onFieldsFilled()`, `this.#onFormUpdate()`, `this.#onIsSmartWindow()`
- 参照: `data.fieldIds`, `data.fields`, `data.id`

## SmartFormFillParent.didDestroy()
- 位置: L571-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.NonPrivateTabs.removeEventListener()`, `this.#abortTabSelector()`, `this.#controller?.destroy()`, `this.#fieldDecisionsByFormId.clear()`, `this.#flowIdByFormId.clear()`, `this.#formMetadataById.clear()`, `this.#formReviewSession?.abort()`, `this.#smartWindowIds.clear()`, `this.#sourceEditorByFormId.clear()`, `this.#userSelectedTabsByFormId.clear()`
- 参照: `this.#controller`, `this.#destroyed`, `this.#formReviewSession`, `this.#tabSelectorDialog`, `this.#tabsChangedDuringValueGeneration`

## SmartFormFillParent.#getController()
- 位置: L594-603
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#controller)` → `this.#getPageInfo()`
- 条件付き依存: `if (!this.#controller)` → `this.#getRequestObserver()`
- 参照: `lazy.SmartFormFillController`, `this.#controller`

## SmartFormFillParent.#getFocusedForm()
- 位置: L610-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendQuery()`, `this.sendQuery("SmartFormFill:GetFocusedForm").catch()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `this.#destroyed`

## SmartFormFillParent.#getFormMetadataState()
- 位置: L626-650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#formMetadataById.get()`
- 条件付き依存: `if (!metadata)` → `this.#formMetadataById.set()`
- 条件付き依存: `if (!metadata)` → `this.#flowIdByFormId.set()`
- 条件付き依存: `if (!metadata)` → `crypto.randomUUID()`
- 条件付き依存: `if (!(!metadata))` → `this.#hasFormStructureChanged()`
- 条件付き依存: `if (this.#hasFormStructureChanged(metadata.formData, formData))` → `this.#invalidateFormMetadata()`
- 参照: `METADATA_STATUS.IDLE`, `focusedForm.fields`, `focusedForm.id`, `metadata.formData`

## SmartFormFillParent.#hasFormStructureChanged()
- 位置: L659-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formData.fields.some()`, `previousFieldIds.has()`, `previousFormData.fields.map()`
- 参照: `formData.fields.length`, `previousFormData.fields.length`

## SmartFormFillParent.#invalidateFormMetadata()
- 位置: L676-691
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `crypto.randomUUID()`, `this.#controller.invalidateForm()`, `this.#fieldDecisionsByFormId.delete()`, `this.#flowIdByFormId.set()`, `this.#sourceEditorByFormId.delete()`
- 参照: `METADATA_STATUS.IDLE`, `formData.id`, `metadata.classificationPromise`, `metadata.classificationRevision`, `metadata.classificationStatus`, `metadata.formData`, `metadata.relevantTabsPromise`, `metadata.relevantTabsRevision`, `metadata.relevantTabsStatus`

## SmartFormFillParent.#startFormMetadataRequests()
- 位置: L698-706
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (metadata.relevantTabsStatus === METADATA_STATUS.IDLE)` → `this.#loadRelevantTabs()`
- 条件付き依存: `if (metadata.classificationStatus === METADATA_STATUS.IDLE)` → `this.#loadFieldClassifications()`
- 参照: `METADATA_STATUS.IDLE`, `metadata.classificationStatus`, `metadata.relevantTabsStatus`

## SmartFormFillParent.#loadRelevantTabs()
- 位置: L714-741
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getController()`, `this.#getController() .findRelevantTabs()`, `this.#getController() .findRelevantTabs(metadata.formData) .catch()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (revision === metadata.relevantTabsRevision && !this.#destroyed)` → `lazy.console.error()`
- 参照: `METADATA_STATUS.LOADING`, `METADATA_STATUS.READY`, `metadata.formData`, `metadata.relevantTabsPromise`, `metadata.relevantTabsRevision`, `metadata.relevantTabsStatus`, `this.#destroyed`

## SmartFormFillParent.#loadFieldClassifications()
- 位置: L749-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.error()`, `this.#getController()`, `this.#getController() .classifyFields()`, `this.#getController() .classifyFields(metadata.formData) .then()`, `this.sendAsyncMessage()`
- 参照: `METADATA_STATUS.FAILED`, `METADATA_STATUS.LOADING`, `METADATA_STATUS.READY`, `metadata.classificationPromise`, `metadata.classificationRevision`, `metadata.classificationStatus`, `metadata.formData`, `this.#destroyed`

## SmartFormFillParent.#performAutofill()
- 位置: async L787-881
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.ceil()`, `Promise.all()`, `this.#cancelFormReviewGeneration()`, `this.#cannotApplyAutofill()`, `this.#controller .autofill()`, `this.#controller .autofill( focusedForm.id, focusedForm.emptyFieldIds, selectedTabs, tabContentById, pageText ) .then()`, `this.#finishFormReviewGeneration()`, `this.#getFormReviewFields()`, `this.#getPageText()`, `this.#getTabsContent()`, `this.#openFormReview()`, `this.#recordTabSelectionOutcome()`, `this.#setReviewValues()`
- 条件付き依存: `if (!reviewSession)` → `this.#cancelFormReviewGeneration()`
- 条件付き依存: `if (generationResult.error)` → `this.#cannotApplyAutofill()`
- 条件付き依存: `if (!this.#cannotApplyAutofill(generation))` → `lazy.console.error()`
- 条件付き依存: `if (!this.#cannotApplyAutofill(generation))` → `this.#finishFormReviewGeneration()`
- 参照: `fields.length`, `focusedForm.emptyFieldIds`, `focusedForm.id`, `generationResult.error`, `generationResult.result`, `lazy.FORM_REVIEW_ERRORS.GENERATION_FAILED`, `lazy.FORM_REVIEW_ERRORS.NO_SUGGESTIONS`, `selectedTabs.length`, `this.#autofillGeneration`, `this.#formReviewSession`, `this.manager.documentURI.spec`

## SmartFormFillParent.#openFormReview()
- 位置: async L892-923
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `session.open()`
- 参照: `chromeWindow?.gBrowser`, `lazy.SmartFormFillReviewSession`, `this.#destroyed`, `this.#formReviewSession`, `this.browsingContext.embedderElement`, `this.browsingContext.topChromeWindow`

## onCancelGeneration()
- 位置: L906-907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cancelFormReviewGeneration()`

## onClose()
- 位置: L908-908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onFormReviewClosed()`

## onFill()
- 位置: L909-909
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fillReviewedFields()`

## SmartFormFillParent.#finishFormReviewGeneration()
- 位置: L934-945
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `session.completeGeneration()`, `this.#cannotApplyAutofill()`
- 条件付き依存: `if (session.completeGeneration(result))` → `this.#refreshDeferredTabData()`
- 参照: `this.#formReviewSession`

## SmartFormFillParent.#onFormReviewClosed()
- 位置: L953-960
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#refreshDeferredTabData()`
- 参照: `this.#formReviewSession`

## SmartFormFillParent.#refreshDeferredTabData()
- 位置: L967-974
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#invalidateTabMetadata()`
- 参照: `this.#tabsChangedDuringValueGeneration`

## SmartFormFillParent.#cancelFormReviewGeneration()
- 位置: L983-990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.cancelAutofill()`
- 参照: `this.#autofillGeneration`, `this.#destroyed`

## SmartFormFillParent.#getFormReviewFields()
- 位置: L1001-1024
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fieldDataById.get()`, `formData?.fields.map()`, `reviewFields.push()`, `this.#formMetadataById.get()`
- 参照: `field.id`, `fieldData.label`, `fieldData.name`, `fieldData.placeholder`, `result.fields`, `result.id`, `this.#formMetadataById.get(result.id)?.formData`

## SmartFormFillParent.#fillReviewedFields()
- 位置: async L1034-1074
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fields.filter()`, `this.#recordFieldReviewOutcomes()`, `this.sendQuery()`, `value.trim()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `result.cancelled`, `result.filledFieldCount`, `result.hasErrors`, `this.#destroyed`

## SmartFormFillParent.#getTabsContent()
- 位置: async L1084-1104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `Promise.resolve()`, `selectedTabs.map()`, `this.#controller.getTabData()`
- 条件付き依存: `if (tabData)` → `this.#getPageText(tabData.url, textCharLimitPerTab).then()`
- 条件付き依存: `if (tabData)` → `this.#getPageText()`
- 条件付き依存: `if (tabData)` → `tabContentById.set()`
- 参照: `selectedTab.id`, `tabData.url`

## SmartFormFillParent.#getPageText()
- 位置: async L1114-1143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pageExtractor.getText()`, `windowGlobal.getActor()`
- 条件付き依存: `if (windowGlobal.documentURI.spec !== sourceUrl)` → `lazy.GetPageContent.getTabWithURL()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 参照: `extraction?.text`, `tab?.linkedBrowser.browsingContext?.currentWindowGlobal`, `this.#destroyed`, `this.manager`, `windowGlobal.documentURI.spec`

## SmartFormFillParent.#getPageInfo()
- 位置: L1150-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.manager`, `windowGlobal.documentTitle`, `windowGlobal.documentURI.spec`

## SmartFormFillParent.#getSmartWindowIds()
- 位置: L1164-1170
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `lazy.BrowserWindowTracker.orderedWindows .filter()`, `lazy.BrowserWindowTracker.orderedWindows .filter(window => lazy.AIWindow.isAIWindowActive(window)) .map()`
- 参照: `window.windowGlobalChild.innerWindowId`

## SmartFormFillParent.#invalidateTabMetadata()
- 位置: L1175-1188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.invalidateTabs()`, `this.#formMetadataById.values()`, `this.sendAsyncMessage()`
- 参照: `METADATA_STATUS.IDLE`, `metadata.relevantTabsPromise`, `metadata.relevantTabsRevision`, `metadata.relevantTabsStatus`, `this.#controller`, `this.#destroyed`

## SmartFormFillParent.#cannotAutofill()
- 位置: L1195-1201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#onIsSmartWindow()`
- 参照: `this.#controller`

## SmartFormFillParent.#cannotApplyAutofill()
- 位置: L1210-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#cannotAutofill()`
- 参照: `this.#autofillGeneration`

## SmartFormFillParent.#onIsSmartWindow()
- 位置: L1219-1228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AIWindow.isAIWindowActive()`, `this.#isDisallowedRegion()`
- 参照: `this.#destroyed`, `this.browsingContext.topChromeWindow`

## SmartFormFillParent.#isDisallowedRegion()
- 位置: L1236-1244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.Region.home?.toUpperCase()`, `lazy.disallowedRegions .split()`, `lazy.disallowedRegions .split(",") .map()`, `lazy.disallowedRegions .split(",") .map(region => region.trim().toUpperCase()) .filter()`, `lazy.disallowedRegions .split(",") .map(region => region.trim().toUpperCase()) .filter(Boolean) .includes()`, `region.trim()`, `region.trim().toUpperCase()`

## SmartFormFillParent.#onFormUpdate()
- 位置: L1251-1279
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `focusedForm?.emptyFieldIds.has()`, `lazy.SmartFormFillAutocomplete.createItemsAsync()`, `this.#controller.getTabs()`, `this.#getFocusedForm()`, `this.#getFormMetadataState()`, `this.#startFormMetadataRequests()`
- 参照: `METADATA_STATUS.FAILED`, `entries.length`, `focusedForm.focusedFieldId`, `focusedForm.id`, `metadata.classificationStatus`, `options.focusElementId`, `this.#autocompleteFormId`, `this.#controller.getTabs().length`, `this.#destroyed`

## SmartFormFillParent.onAutoCompletePopupOpened()
- 位置: L1340-1342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateAutoCompletePopupSources()`

## SmartFormFillParent.onAutoCompletePopupUpdated()
- 位置: L1347-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateAutoCompletePopupSources()`

## SmartFormFillParent.#updateAutoCompletePopupSources()
- 位置: L1354-1368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SmartFormFillAutocomplete.updatePopupSources()`, `this.areRelevantTabsReady()`, `this.getSelectedTabSources()`
- 参照: `this.#autocompleteFormId`, `this.#destroyed`, `this.browsingContext.top.embedderElement`

## SmartFormFillParent.onAutoCompleteEntrySelected()
- 位置: L1382-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#editSources()`, `this.triggerAutofill()`
- 参照: `this.#destroyed`

## SmartFormFillParent.getSelectedTabSources()
- 位置: L1405-1417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.getTabData()`, `this.#getSelectedTabsFor()`, `this.#getSelectedTabsFor(formId) .map()`, `this.#getSelectedTabsFor(formId) .map(({ id }) => this.#controller.getTabData(id)) .filter()`, `this.#getSelectedTabsFor(formId) .map(({ id }) => this.#controller.getTabData(id)) .filter(Boolean) .map()`
- 参照: `tab.title`, `tab.url`, `this.#controller`

## SmartFormFillParent.areRelevantTabsReady()
- 位置: L1425-1434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#formMetadataById.get()`
- 参照: `METADATA_STATUS.READY`, `this.#destroyed`, `this.#formMetadataById.get(formId)?.relevantTabsStatus`

## SmartFormFillParent.hasSourceTabs()
- 位置: L1441-1443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Boolean()`
- 参照: `this.#controller?.hasSourceTabs`

## SmartFormFillParent.#getFlowId()
- 位置: L1453-1455
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#flowIdByFormId.get()`

## SmartFormFillParent.#getSourceEditorState()
- 位置: L1465-1474
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#sourceEditorByFormId.get()`
- 条件付き依存: `if (!state)` → `this.#sourceEditorByFormId.set()`

## SmartFormFillParent.#recordTabSelectionOutcome()
- 位置: L1482-1488
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#controller.getRelevantTabsFor()`, `this.#getFlowId()`, `this.#sourceEditorByFormId.get()`, `this.#telemetry.sendRelevantTabsOutcomeTelemetry()`

## SmartFormFillParent.#setReviewValues()
- 位置: L1497-1504
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fields.map()`, `this.#fieldDecisionsByFormId.get()`
- 参照: `round.reviewValues`

## SmartFormFillParent.#recordFieldReviewOutcomes()
- 位置: L1514-1528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldDecisionsByFormId.get()`, `this.#telemetry.sendFillFieldReviewOutcomeTelemetry()`
- 参照: `round.decisions`, `round.flowId`, `round.reviewValues`, `round?.reviewValues`

## SmartFormFillParent.#onFieldsFilled()
- 位置: L1537-1548
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldDecisionsByFormId.get()`, `this.#telemetry.sendFillFieldTelemetry()`
- 参照: `round.decisions`, `round.flowId`

## SmartFormFillParent.#onFieldOutcomes()
- 位置: L1563-1574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldDecisionsByFormId.get()`, `this.#telemetry.sendFillFieldOutcomeTelemetry()`
- 参照: `round.decisions`, `round.flowId`

## SmartFormFillParent.#getRequestObserver()
- 位置: L1581-1656
- 役割: (未記入)
- 触るとき: (未記入)

## onRelevantTabsDispatched()
- 位置: L1583-1589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getFlowId()`, `this.#telemetry.startRelevantTabsRequest()`

## onRelevantTabsAnswered()
- 位置: L1591-1596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#telemetry.sendRelevantTabsResponseTelemetry()`

## onRelevantTabsFailed()
- 位置: L1598-1599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#telemetry.sendRelevantTabsErrorTelemetry()`

## onClassifyDispatched()
- 位置: L1601-1606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getFlowId()`, `this.#telemetry.startClassifyRequest()`

## onClassifyAnswered()
- 位置: L1608-1609
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#telemetry.sendClassifyResponseTelemetry()`

## onClassifyFailed()
- 位置: L1611-1612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#telemetry.sendClassifyErrorTelemetry()`

## onGenerateDispatched()
- 位置: L1614-1619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getFlowId()`, `this.#telemetry.startGenerateRequest()`

## onGenerateAnswered()
- 位置: L1621-1651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldDecisionsByFormId.set()`, `this.#telemetry.resolveFieldDecisions()`, `this.#telemetry.sendGenerateResponseTelemetry()`
- 参照: `flow.flowId`

## onGenerateFailed()
- 位置: L1653-1654
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#telemetry.sendGenerateErrorTelemetry()`
