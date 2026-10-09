# browser/components/aiwindow/ui/modules/SmartFormFillController.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillController.sys.mjs
source-hash: 1a73eda3876c68beee9866d66e07c0de8765f3c5
lines: 1070

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SmartFormFillController.constructor()
- 位置: L188-200
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#abortClassificationControllers`, `this.#abortRelevantTabsControllers`, `this.#abortValueGenerationControllers`, `this.#classifiedFieldsByFormId`, `this.#formDataById`, `this.#pageInfo`, `this.#relevantTabsByFormId`, `this.#requestObserver`, `this.#tabCounter`, `this.#tabsById`

## SmartFormFillController.getRelevantTabsFor()
- 位置: L209-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#relevantTabsByFormId.get()`
- 参照: `this.#relevantTabsByFormId.get(formId)?.selectedTabs`

## SmartFormFillController.hasSourceTabs()
- 位置: L218-220
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#tabList?.length`

## SmartFormFillController.getTabData()
- 位置: L229-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabsById.get()`

## SmartFormFillController.#setFormData()
- 位置: L238-240
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#formDataById.set()`
- 参照: `formData.id`

## SmartFormFillController.findRelevantTabs()
- 位置: async L248-269
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortRelevantTabsControllers.get()`, `this.#abortRelevantTabsControllers.get(formData.id)?.abort()`, `this.#abortRelevantTabsControllers.set()`, `this.#ensureTabData()`, `this.#findRelevantTabsForForm()`, `this.#removeAbortController()`, `this.#requestWithRetries()`, `this.#setFormData()`
- 参照: `abortController.signal`, `formData.id`, `this.#abortRelevantTabsControllers`

## SmartFormFillController.classifyFields()
- 位置: async L277-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortClassificationControllers.get()`, `this.#abortClassificationControllers.get(formData.id)?.abort()`, `this.#abortClassificationControllers.set()`, `this.#classifyFormFields()`, `this.#removeAbortController()`, `this.#requestWithRetries()`, `this.#setFormData()`
- 参照: `abortController.signal`, `formData.id`, `this.#abortClassificationControllers`

## SmartFormFillController.#invalidateRelevantTabs()
- 位置: L304-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortRelevantTabsControllers.delete()`, `this.#abortRelevantTabsControllers.get()`, `this.#abortRelevantTabsControllers.get(formId)?.abort()`, `this.#relevantTabsByFormId.delete()`

## SmartFormFillController.invalidateForm()
- 位置: L315-321
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortClassificationControllers.delete()`, `this.#abortClassificationControllers.get()`, `this.#abortClassificationControllers.get(formId)?.abort()`, `this.#classifiedFieldsByFormId.delete()`, `this.#formDataById.delete()`, `this.#invalidateRelevantTabs()`

## SmartFormFillController.invalidateTabs()
- 位置: L326-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortRequests()`, `this.#relevantTabsByFormId.clear()`
- 参照: `this.#abortRelevantTabsControllers`, `this.#tabList`

## SmartFormFillController.getTabs()
- 位置: L337-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#tabList?.map()`

## SmartFormFillController.cancelAutofill()
- 位置: L348-350
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortValueGenerationControllers.get()`, `this.#abortValueGenerationControllers.get(formId)?.abort()`

## SmartFormFillController.autofill()
- 位置: async L363-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emptyFieldIds.has()`, `formData.fields.filter()`, `this.#formDataById.get()`, `this.#generateFormValues()`
- 参照: `emptyFields.length`, `field.id`, `formData.fields`

## SmartFormFillController.#generateFormValues()
- 位置: async L406-534
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this.#classifiedFieldsByFormId.get(id)?.fields ?? []).map()`, `abortCtrl.signal.throwIfAborted()`, `classifications.get()`, `lazy.SmartFormFillModel.generateFormValues()`, `relevantMemories.map()`, `selectedTabs.map()`, `tabContentById.get()`, `this.#abortValueGenerationControllers.get()`, `this.#abortValueGenerationControllers.get(id)?.abort()`, `this.#abortValueGenerationControllers.set()`, `this.#classifiedFieldsByFormId.get()`, `this.#getCandidates()`, `this.#getFieldDataForClassification()`, `this.#getFieldDataForClassification(fields).map()`, `this.#getFillInstructions()`, `this.#removeAbortController()`, `this.#requestObserver.onGenerateAnswered()`, `this.#tabsById.get()`
- 条件付き依存: `if (flow && !abortCtrl.signal.aborted)` → `this.#requestObserver.onGenerateFailed()`
- 参照: `abortCtrl.signal`, `abortCtrl.signal.aborted`, `classification?.confidence`, `classification?.type`, `field.id`, `fillInstructions.length`, `memory.id`, `memory.memory_summary`, `memory.similarity`, `result.id`, `selectedTab.id`, `this.#abortValueGenerationControllers`, `this.#classifiedFieldsByFormId.get(id)?.fields`, `this.#pageInfo`

## onDispatch()
- 位置: L490-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#requestObserver.onGenerateDispatched()`

## SmartFormFillController.#getMemories()
- 位置: async L549-577
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `[ field.label, field.inputType, field.placeholder, field.textBefore, field.textAfter, ] .filter()`, `[ field.label, field.inputType, field.placeholder, field.textBefore, field.textAfter, ] .filter(Boolean) .join()`, `fields.map()`, `lazy.MemoriesManager.getRelevantMemories()`, `relevantMemories.map()`
- 参照: `URL.parse(pageInfo.url)?.hostname`, `field.inputType`, `field.label`, `field.placeholder`, `field.textAfter`, `field.textBefore`, `pageInfo.title`, `pageInfo.url`

## SmartFormFillController.#getFillInstructions()
- 位置: L588-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CONFIDENCE_RANK.get()`, `fieldIds.has()`, `fields.map()`, `fillInstructions.push()`, `resolvedFieldIds.add()`, `resolvedFieldIds.has()`, `valuesByToken.get()`
- 参照: `field.id`, `result.action`, `result.confidence`, `result.id`, `result.value`, `values.fields`

## SmartFormFillController.#getCandidates()
- 位置: async L634-670
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `candidates.push()`, `lazy.FormAutofillUtils.isAddressField()`, `this.#getFormHistoryValue()`, `tokensByFieldId.set()`, `type.toUpperCase()`, `type.toUpperCase().replaceAll()`, `typeCounts.get()`, `typeCounts.set()`, `valuesByToken.set()`
- 条件付き依存: `if (lazy.FormAutofillUtils.isAddressField(type))` → `this.#getSavedAddresses()`
- 条件付き依存: `if (lazy.FormAutofillUtils.isAddressField(type))` → `savedAddresses.find()`
- 参照: `field.id`, `field.localGuess`

## SmartFormFillController.#getSavedAddresses()
- 位置: async L681-698
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addresses.sort()`, `lazy.FormAutofill.isAutofillTypeEnabled()`, `lazy.formAutofillStorage.addresses.getAll()`, `lazy.formAutofillStorage.initialize()`
- 参照: `a.timeLastUsed`, `b.timeLastUsed`, `lazy.AutofillDataTypes.ADDRESS`

## SmartFormFillController.#getFormHistoryValue()
- 位置: async L706-726
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormHistory.search()`, `results.sort()`
- 参照: `a.lastUsed`, `b.lastUsed`, `field.formHistoryName`, `results?.length`, `results[0].value`

## SmartFormFillController.#abortRequests()
- 位置: L733-743
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.abort()`, `controllerMaps.flatMap()`, `map.clear()`, `map.values()`

## SmartFormFillController.#removeAbortController()
- 位置: L752-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controllers?.get()`
- 条件付き依存: `if (controllers?.get(id) === controller)` → `controllers.delete()`

## SmartFormFillController.destroy()
- 位置: L761-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#abortRequests()`, `this.#classifiedFieldsByFormId.clear()`, `this.#formDataById.clear()`, `this.#relevantTabsByFormId.clear()`, `this.#tabsById.clear()`
- 参照: `this.#abortClassificationControllers`, `this.#abortRelevantTabsControllers`, `this.#abortValueGenerationControllers`, `this.#classifiedFieldsByFormId`, `this.#formDataById`, `this.#relevantTabsByFormId`, `this.#tabCounter`, `this.#tabList`, `this.#tabsById`

## SmartFormFillController.#ensureTabData()
- 位置: L790-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getTabList()`, `this.#getTabData()`, `this.#tabsById.clear()`
- 参照: `this.#tabCounter`, `this.#tabList`

## SmartFormFillController.#requestWithRetries()
- 位置: async L809-828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SmartFormFillModel.isRetryableRequestError()`, `request()`, `signal.throwIfAborted()`, `this.#waitBeforeRetry()`

## SmartFormFillController.#waitBeforeRetry()
- 位置: L838-856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.pow()`, `Math.random()`, `lazy.setTimeout()`, `resolve()`, `signal.addEventListener()`, `signal.removeEventListener()`

## onAbort()
- 位置: L844-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.clearTimeout()`, `reject()`
- 参照: `signal.reason`

## SmartFormFillController.#getValidRelevantTabs()
- 位置: L864-889
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `CONFIDENCE_RANK.get()`, `seen.add()`, `seen.has()`, `selectedTabs .filter()`, `this.#tabsById.has()`
- 参照: `lazy.MAX_SELECTED_TABS`, `tab?.id`, `tab?.relevance`

## SmartFormFillController.#findRelevantTabsForForm()
- 位置: async L899-942
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SmartFormFillModel.findRelevantTabs()`, `signal.throwIfAborted()`, `this.#getRelevantTabRequestBody()`, `this.#getValidRelevantTabs()`, `this.#relevantTabsByFormId.set()`, `this.#requestObserver.onRelevantTabsAnswered()`
- 条件付き依存: `if (flow && !signal.aborted)` → `this.#requestObserver.onRelevantTabsFailed()`
- 参照: `relevantTabCandidates?.selectedTabs`, `relevantTabs.selectedTabs.length`, `signal.aborted`

## onDispatch()
- 位置: L910-917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#requestObserver.onRelevantTabsDispatched()`

## SmartFormFillController.#classifyFormFields()
- 位置: async L951-985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SmartFormFillModel.classifyFields()`, `signal.throwIfAborted()`, `this.#classifiedFieldsByFormId.set()`, `this.#getClassifyFieldsRequestBody()`, `this.#requestObserver.onClassifyAnswered()`
- 条件付き依存: `if (flow && !signal.aborted)` → `this.#requestObserver.onClassifyFailed()`
- 参照: `signal.aborted`

## onDispatch()
- 位置: L963-969
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#requestObserver.onClassifyDispatched()`

## SmartFormFillController.#getFieldDataForClassification()
- 位置: L993-1008
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fields.map()`
- 参照: `field.autocomplete`, `field.id`, `field.inputType`, `field.label`, `field.localConfidence`, `field.localGuess`, `field.maxlength`, `field.name`, `field.options`, `field.placeholder`, `field.textAfter`, `field.textBefore`

## SmartFormFillController.#getClassifyFieldsRequestBody()
- 位置: L1016-1023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getFieldDataForClassification()`
- 参照: `this.#pageInfo`

## SmartFormFillController.#getRelevantTabRequestBody()
- 位置: L1031-1045
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getFieldDataForClassification()`
- 参照: `lazy.MAX_SELECTED_TABS`, `this.#pageInfo`, `this.#tabList`

## SmartFormFillController.#getTabData()
- 位置: L1053-1068
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabList.map()`, `this.#tabsById.set()`
- 参照: `this.#tabCounter`
