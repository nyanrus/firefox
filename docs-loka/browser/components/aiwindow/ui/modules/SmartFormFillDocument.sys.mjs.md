# browser/components/aiwindow/ui/modules/SmartFormFillDocument.sys.mjs

source: browser/components/aiwindow/ui/modules/SmartFormFillDocument.sys.mjs
source-hash: 2a0f6437d92411b5a14d4d370f46d2d1ce5658c5
lines: 1289

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## SmartFormFillDocument.constructor()
- 位置: L266-286
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.SmartFormFillUtils`, `this.#destroyed`, `this.#doc`, `this.#fieldCounter`, `this.#fieldIds`, `this.#fieldsById`, `this.#fillGeneration`, `this.#filledFields`, `this.#formCounter`, `this.#formRoots`, `this.#formUpdateAffectedGroupsMap`, `this.#formUpdateTimeout`, `this.#forms`, `this.#initialized`, `this.#observedRoots`, `this.#observer`, `this.#onFieldOutcomes`, `this.#onFieldsFilled`, `this.#onFormUpdate`, `this.#utils`

## SmartFormFillDocument.initialize()
- 位置: async L300-335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#detectFields()`, `this.#monitorDocument()`, `this.#monitorFilledFields()`
- 条件付き依存: `if (!this.#destroyed)` → `lazy.console.error()`
- 条件付き依存: `if (!this.#destroyed)` → `this.destroy()`
- 参照: `this.#destroyed`, `this.#initialized`, `this.#onFieldOutcomes`, `this.#onFieldsFilled`, `this.#onFormUpdate`

## SmartFormFillDocument.destroy()
- 位置: L340-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldsById.clear()`, `this.#filledFields.clear()`, `this.#formRoots.clear()`, `this.#forms.clear()`, `this.#observer?.disconnect()`, `this.#stopMonitoringFilledFields()`
- 条件付き依存: `if (this.#formUpdateTimeout)` → `this.#doc.defaultView.clearTimeout()`
- 参照: `this.#destroyed`, `this.#doc`, `this.#fieldCounter`, `this.#fieldIds`, `this.#fieldsById`, `this.#fillGeneration`, `this.#filledFields`, `this.#formCounter`, `this.#formRoots`, `this.#formUpdateAffectedGroupsMap`, `this.#formUpdateTimeout`, `this.#forms`, `this.#observedRoots`, `this.#observer`, `this.#onFieldOutcomes`, `this.#onFormUpdate`, `this.#utils`

## SmartFormFillDocument.getFormData()
- 位置: L390-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `formFields.map()`, `forms.map()`, `this.#getFieldData()`, `this.#getForms()`

## SmartFormFillDocument.getFocusedForm()
- 位置: L407-444
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.fields .filter()`, `group.fields .filter( formField => this.#isSupportedField(formField) && this.#isFillableField(formField) ) .map()`, `group.fields.includes()`, `lazy.FormLikeFactory.findRootForField()`, `this.#formRoots.get()`, `this.#getFieldId()`, `this.#getFocusedField()`, `this.#hasEnoughEditableFields()`, `this.#isFillableField()`, `this.#isSupportedField()`, `this.getFormData()`, `this.getFormData().find()`
- 参照: `formData.fields`, `formData.id`, `group.formId`, `group?.formId`

## SmartFormFillDocument.fillForm()
- 位置: async L457-564
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#fillGeneration`

## SmartFormFillDocument.#allowCancellationCheck()
- 位置: L584-586
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.tm.dispatchToMainThread()`
- XPCOM: `Services.tm`

## SmartFormFillDocument.handleEvent()
- 位置: L593-621
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormLikeFactory.findRootForField()`, `this.#onFilledFieldInput()`, `this.#reportOutcomes()`
- 参照: `event.target`, `event.type`, `this.#filledFields?.size`

## SmartFormFillDocument.#monitorFilledFields()
- 位置: L630-637
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#doc.addEventListener()`, `this.#doc.defaultView?.addEventListener()`

## SmartFormFillDocument.#stopMonitoringFilledFields()
- 位置: L642-649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#doc.defaultView?.removeEventListener()`, `this.#doc.removeEventListener()`

## SmartFormFillDocument.#onFilledFieldInput()
- 位置: L658-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldIds.get()`, `this.#filledFields.get()`
- 参照: `filled.edited`

## SmartFormFillDocument.#reportOutcomes()
- 位置: L677-707
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `field.value.trim()`, `matches()`, `statesByFormId.get()`, `statesByFormId.get(formId).push()`, `statesByFormId.has()`, `this.#fieldsById.get()`, `this.#filledFields.delete()`, `this.#onFieldOutcomes()`
- 条件付き依存: `if (!statesByFormId.has(formId))` → `statesByFormId.set()`
- 参照: `field.value.length`, `this.#filledFields`, `this.#onFieldOutcomes`

## SmartFormFillDocument.getSupportedFields()
- 位置: L714-718
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.#forms.values()).flatMap()`, `fields.filter()`, `this.#forms.values()`, `this.#isSupportedField()`

## SmartFormFillDocument.isSupportedField()
- 位置: L727-729
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isSupportedField()`

## SmartFormFillDocument.shouldOfferFill()
- 位置: L740-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormLikeFactory.findRootForField()`, `this.#formRoots.get()`, `this.#hasEnoughEditableFields()`, `this.#isFillableField()`, `this.#isSupportedField()`
- 参照: `group?.formId`

## SmartFormFillDocument.#getFieldData()
- 位置: L764-785
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getFieldLabel()`, `this.#utils.findNearbyText()`
- 参照: `details.confidence`, `details.fieldName`, `details.reason`, `details?.confidence`, `details?.fieldName`, `field.autocomplete`, `field.id`, `field.maxLength`, `field.name`, `field.placeholder`, `field.type`

## SmartFormFillDocument.#normalize()
- 位置: L794-796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `value?.replace()`, `value?.replace(/\s+/g, " ").trim()`

## SmartFormFillDocument.#getFieldLabel()
- 位置: L806-825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(field.labels ?? []) .map()`, `Array.from(field.labels ?? []) .map(labelEl => this.#normalize(labelEl.textContent)) .filter()`, `Array.from(field.labels ?? []) .map(labelEl => this.#normalize(labelEl.textContent)) .filter(Boolean) .join()`, `field .getAttribute()`, `field .getAttribute("aria-labelledby") ?.split()`, `field .getAttribute("aria-labelledby") ?.split(/\s+/) .map()`, `field.getAttribute()`, `field.getRootNode()`, `root.getElementById()`, `this.#normalize()`
- 参照: `field.labels`, `labelEl.textContent`, `root.getElementById?.(id)?.textContent`

## SmartFormFillDocument.#getFieldId()
- 位置: L832-843
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#fieldIds.get()`
- 条件付き依存: `if (!fieldId)` → `this.#fieldIds.set()`
- 条件付き依存: `if (!fieldId)` → `this.#fieldsById.set()`
- 参照: `this.#fieldCounter`

## SmartFormFillDocument.#getForms()
- 位置: L851-872
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fieldMap.get()`, `fields .filter()`, `fields .filter(field => this.#isSupportedField(field)) .map()`, `this.#forms.entries()`, `this.#getFieldId()`, `this.#isSupportedField()`, `this.#toFieldMap()`
- 条件付き依存: `if (formFields.length)` → `forms.push()`
- 参照: `formFields.length`

## SmartFormFillDocument.#toFieldMap()
- 位置: L883-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fieldDetailsList.map()`
- 参照: `fieldDetails.element`

## SmartFormFillDocument.#isSupportedField()
- 位置: L898-911
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `HTMLInputElement.isInstance()`, `HTMLTextAreaElement.isInstance()`, `SUPPORTED_INPUT_TYPES.includes()`, `element?.closest()`
- 参照: `element.name`, `element.type`

## SmartFormFillDocument.#getFocusedField()
- 位置: L920-928
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isSupportedField()`
- 参照: `field.shadowRoot.activeElement`, `field?.shadowRoot?.activeElement`, `this.#doc.activeElement`

## SmartFormFillDocument.#isEditableField()
- 位置: L939-945
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.FormAutofillUtils.isFieldVisible()`
- 参照: `field.disabled`, `field.readOnly`

## SmartFormFillDocument.#isFillableField()
- 位置: L956-958
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isEditableField()`
- 参照: `field.value`

## SmartFormFillDocument.#monitorDocument()
- 位置: L966-976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observeRoot()`, `this.#onMutation()`
- 参照: `this.#doc`, `this.#doc.defaultView.MutationObserver`, `this.#observer`

## SmartFormFillDocument.#observeRoot()
- 位置: L986-993
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#observedRoots.add()`, `this.#observedRoots.has()`, `this.#observer.observe()`

## SmartFormFillDocument.#removeStaleFields()
- 位置: L1003-1030
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(mutation.addedNodes) .filter()`, `Array.from(mutation.addedNodes) .filter(addedNode => !!addedNode.matches) .flatMap()`, `this.#getFields()`
- 参照: `addedNode.matches`, `mutation.addedNodes`

## SmartFormFillDocument.#addFieldToGroup()
- 位置: L1060-1081
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.fields.includes()`, `lazy.FormLikeFactory.createFromField()`, `this.#formRoots.get()`
- 条件付き依存: `if (!group)` → `Object.defineProperty()`
- 条件付き依存: `if (!group)` → `this.#formRoots.set()`
- 条件付き依存: `if (!group.fields.includes(field))` → `group.fields.push()`
- 参照: `formLike.rootElement`, `group.fields`

## SmartFormFillDocument.#hasEnoughSupportedFields()
- 位置: L1094-1104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.fields.reduce()`, `this.#isSupportedField()`
- 参照: `lazy.MIN_FORM_FIELDS`

## SmartFormFillDocument.#hasEnoughEditableFields()
- 位置: L1117-1127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `group.fields.reduce()`, `this.#isEditableField()`, `this.#isSupportedField()`
- 参照: `lazy.MIN_FORM_FIELDS`

## SmartFormFillDocument.#updateFormGroups()
- 位置: L1139-1167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `affectedGroups.values()`, `lazy.FormAutofillHeuristics.getFormInfo()`, `this.#hasEnoughSupportedFields()`
- 条件付き依存: `if (affectedGroup.formId)` → `this.#forms.delete()`
- 条件付き依存: `if (!affectedGroup.fields.length)` → `this.#formRoots.delete()`
- 条件付き依存: `if (!affectedGroup.formId)` → `this.#forms.set()`
- 参照: `affectedGroup.fieldDetailsList`, `affectedGroup.fields.length`, `affectedGroup.formId`, `affectedGroup.formLike`, `affectedGroup.formLike.rootElement`, `this.#formCounter`

## SmartFormFillDocument.#onMutation()
- 位置: L1177-1227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `affectedGroups.set()`, `mutations.some()`, `this.#addFieldToGroup()`, `this.#doc.defaultView.setTimeout()`, `this.#getAddedFields()`, `this.#triggerFormUpdate()`
- 条件付き依存: `if ( mutations.some( mutation => mutation.type === "childList" && mutation.removedNodes.length ) )` → `this.#removeStaleFields()`
- 条件付き依存: `if (this.#formUpdateTimeout)` → `this.#doc.defaultView.clearTimeout()`
- 参照: `addedField.isConnected`, `affectedGroups.size`, `group.formLike.rootElement`, `mutation.removedNodes.length`, `mutation.type`, `this.#formUpdateAffectedGroupsMap`, `this.#formUpdateTimeout`

## SmartFormFillDocument.#triggerFormUpdate()
- 位置: L1234-1241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#updateFormGroups()`, `this.#utils.clearCache()`
- 条件付き依存: `if (typeof this.#onFormUpdate === "function")` → `this.#onFormUpdate()`
- 条件付き依存: `if (typeof this.#onFormUpdate === "function")` → `this.getFormData()`
- 参照: `this.#onFormUpdate`

## SmartFormFillDocument.#detectFields()
- 位置: async L1250-1256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#addFieldToGroup()`, `this.#getFields()`, `this.#updateFormGroups()`
- 参照: `this.#doc`, `this.#formRoots`

## SmartFormFillDocument.#getFields()
- 位置: L1267-1287
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `element.matches()`, `rootElement.matches()`, `rootElement.querySelectorAll()`
- 条件付き依存: `if (rootElement.shadowRoot)` → `this.#observeRoot()`
- 条件付き依存: `if (rootElement.shadowRoot)` → `this.#getFields()`
- 条件付き依存: `if (element.shadowRoot)` → `this.#observeRoot()`
- 条件付き依存: `if (element.shadowRoot)` → `this.#getFields()`
- 参照: `element.shadowRoot`, `rootElement.matches`, `rootElement.shadowRoot`
