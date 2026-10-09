# browser/components/preferences/config/aiFeatures.mjs

source: browser/components/preferences/config/aiFeatures.mjs
source-hash: 97ed7a73d1d10bb389733aac91062aca2f269474
lines: 1762

## <module>
- 役割: (未記入)
- 呼び出し先: `AI_CONTROL_OPTIONS.filter()`, `ChromeUtils.importESModule()`, `Object.freeze()`, `Preferences.addAll()`, `Preferences.addSetting()`, `Promise.withResolvers()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`, `buildPresetModelOptions()`, `customElements.define()`, `makeAiControlSetting()`

## getControlConfig()
- 位置: L73-84
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `config.options`, `control.id`, `deps[control.id].visible`, `option.controlAttrs`, `option.controlAttrs.class`, `option.items`

## visible()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.aiControlDefaultToggle.value`

## updateAiControlDefault()
- 位置: L111-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.globalAiControlToggled.record()`, `Object.values()`, `Services.prefs.setBoolPref()`
- 条件付き依存: `if (isBlocked)` → `OnDeviceModelManager.block()`
- 条件付き依存: `if (!(isBlocked))` → `OnDeviceModelManager.isEnabled()`
- 条件付き依存: `if (!isBlocked && !OnDeviceModelManager.isEnabled(feature))` → `OnDeviceModelManager.makeAvailable()`
- 条件付き依存: `if (isBlocked)` → `Services.prefs.setStringPref()`
- 参照: `AiControlGlobalStates.blocked`, `OnDeviceModelManager.features`
- XPCOM: `Services.prefs`

## BlockAiConfirmationDialog.constructor()
- 位置: L144-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.isGlobal`

## BlockAiConfirmationDialog.dialog()
- 位置: L149-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## BlockAiConfirmationDialog.confirmButton()
- 位置: L153-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## BlockAiConfirmationDialog.cancelButton()
- 位置: L157-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.renderRoot.querySelector()`

## BlockAiConfirmationDialog.showModal()
- 位置: L168-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `this.dialog.showModal()`, `this.updateComplete.then()`
- 参照: `this.#confirmed`, `this.#resolvers`, `this.#resolvers.promise`, `this.descriptionL10nId`, `this.headingL10nId`, `this.isGlobal`

## BlockAiConfirmationDialog.handleCancel()
- 位置: L178-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dialog.close()`
- 参照: `this.#confirmed`

## BlockAiConfirmationDialog.handleConfirm()
- 位置: L183-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dialog.close()`
- 参照: `this.#confirmed`

## BlockAiConfirmationDialog.globalTemplate()
- 位置: L188-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## BlockAiConfirmationDialog.descriptionTemplate()
- 位置: L227-229
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.descriptionL10nId`

## BlockAiConfirmationDialog.onToggle()
- 位置: L231-235
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.dialog.open)` → `this.#resolvers.resolve()`
- 参照: `this.#confirmed`, `this.dialog.open`

## BlockAiConfirmationDialog.render()
- 位置: L237-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.descriptionTemplate()`, `this.globalTemplate()`
- 参照: `this.handleCancel`, `this.handleConfirm`, `this.headingL10nId`, `this.isGlobal`, `this.onToggle`

## modelL10nArgs()
- 位置: L314-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.getCachedModelsData()`
- 参照: `lazy.getCachedModelsData()[key].model`, `lazy.getCachedModelsData()[key].ownerName`, `lazy.getCachedModelsData()[key].shortName`

## isMistralRelease()
- 位置: L323-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## buildPresetModelOptions()
- 位置: L361-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isMistralRelease()`, `lazy.getModelDisplayOrder()`, `lazy.getModelDisplayOrder().map()`

## l10nArgs()
- 位置: L370-372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `modelL10nArgs()`

## validateEndpointUrl()
- 位置: L384-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `principal.isOriginPotentiallyTrustworthy`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## setup()
- 位置: L403-407
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.body.append()`, `document.createElement()`

## get()
- 位置: L408-411
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AiControlGlobalStates.available`, `AiControlGlobalStates.blocked`

## set()
- 位置: L412-428
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (inputVal)` → `setting.onChange()`
- 条件付き依存: `if (inputVal)` → `document.querySelector()`
- 条件付き依存: `if (inputVal)` → `dialog.showModal({ all: true }).then()`
- 条件付き依存: `if (inputVal)` → `dialog.showModal()`
- 条件付き依存: `if (confirmed)` → `updateAiControlDefault()`
- 条件付き依存: `if (!(inputVal))` → `updateAiControlDefault()`
- 参照: `AiControlGlobalStates.available`, `AiControlGlobalStates.blocked`

## makeAiControlSetting()
- 位置: L439-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.addSetting()`

## recordTelemetry()
- 位置: L448-450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.aiControlChanged.record()`

## setup()
- 位置: L456-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `setup()`, `teardownSetup()`
- XPCOM: `Services.obs`

## featureChange()
- 位置: L462-466
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (changedFeature == feature)` → `emitChange()`

## get()
- 位置: L477-498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.getAiControlState()`, `OnDeviceModelManager.hasDistinctEnabledState()`
- 参照: `AiControlGlobalStates.blocked`, `AiControlStates.available`, `AiControlStates.blocked`, `AiControlStates.default`, `AiControlStates.enabled`, `deps.aiControlDefault.value`

## set()
- 位置: L499-520
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (prefVal == AiControlStates.blocked && onBeforeBlock)` → `setting.onChange()`
- 条件付き依存: `if (prefVal == AiControlStates.blocked && onBeforeBlock)` → `onBeforeBlock().then()`
- 条件付き依存: `if (prefVal == AiControlStates.blocked && onBeforeBlock)` → `onBeforeBlock()`
- 条件付き依存: `if (confirmed)` → `OnDeviceModelManager.block()`
- 条件付き依存: `if (confirmed)` → `recordTelemetry()`
- 条件付き依存: `if (prefVal == AiControlStates.available)` → `OnDeviceModelManager.makeAvailable()`
- 条件付き依存: `if (prefVal == AiControlStates.enabled)` → `OnDeviceModelManager.enable()`
- 条件付き依存: `if (prefVal == AiControlStates.blocked)` → `OnDeviceModelManager.block()`
- 参照: `AiControlStates.available`, `AiControlStates.blocked`, `AiControlStates.enabled`, `setting.value`

## disabled()
- 位置: L521-523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.isManagedByPolicy()`

## visible()
- 位置: L524-532
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.isAllowed()`, `visible()`
- 参照: `deps.aiControlsShowUnavailable.value`

## onUserChange()
- 位置: L533-539
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (selection === setting.value)` → `recordTelemetry()`
- 参照: `setting.value`

## getControlConfig()
- 位置: L540-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.hasDistinctEnabledState()`, `getControlConfig()`
- 条件付き依存: `if (!OnDeviceModelManager.hasDistinctEnabledState(feature))` → `config.options.filter()`
- 参照: `AiControlStates.enabled`, `config.options`, `option.value`

## getControlConfig()
- 位置: L557-563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.options.at()`
- 参照: `AiControlStates.blocked`, `config.supportPage`, `moreSettingsLink.hidden`, `setting.value`

## setup()
- 位置: L574-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## onTabGroupsEnabledChange()
- 位置: L575-579
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (changedPref == "browser.tabs.groups.enabled")` → `emitChange()`

## visible()
- 位置: L590-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## setup()
- 位置: L613-631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `lazy.GenAI.init()`
- XPCOM: `Services.obs`

## featureChange()
- 位置: L620-624
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (changedFeature == this.feature)` → `emitChange()`
- 参照: `this.feature`

## get()
- 位置: L632-649
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.getAiControlState()`
- 参照: `AiControlGlobalStates.blocked`, `AiControlStates.blocked`, `AiControlStates.default`, `AiControlStates.enabled`, `deps.aiControlDefault.value`, `deps.chatbotProvider.value`, `this.feature`

## set()
- 位置: L650-665
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (inputVal == AiControlStates.blocked)` → `OnDeviceModelManager.block()`
- 条件付き依存: `if (inputVal == AiControlStates.available)` → `OnDeviceModelManager.makeAvailable()`
- 条件付き依存: `if (inputVal)` → `OnDeviceModelManager.enable()`
- 参照: `AiControlStates.available`, `AiControlStates.blocked`, `AiControlStates.enabled`, `deps.chatbotProvider.value`, `this.feature`

## disabled()
- 位置: L666-668
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.isManagedByPolicy()`
- 参照: `this.feature`

## visible()
- 位置: L669-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `OnDeviceModelManager.isAllowed()`
- 参照: `deps.aiControlsShowUnavailable.value`, `this.feature`

## onUserChange()
- 位置: L675-683
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.aiControlChanged.record()`, `String()`
- 参照: `AiControlStates.enabled`, `OnDeviceModelManager.features.SidebarChatbot`

## getControlConfig()
- 位置: L684-708
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.options.slice()`, `lazy.GenAI.chatProviders.forEach()`, `options.push()`, `options.some()`
- 条件付き依存: `if (!options.some(opt => opt.value == providerUrl))` → `options.push()`
- 参照: `opt.value`, `provider.hidden`, `provider.name`, `setting.value`

## visible()
- 位置: L724-724
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.smartWindowEnabled.value`

## onBeforeBlock()
- 位置: async L736-762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialog.showModal()`, `document.querySelector()`, `lazy.ChatStore.findRecentConversations()`, `lazy.MemoryStore.getMemories()`
- 参照: `(await lazy.ChatStore.findRecentConversations(1)).length`, `(await lazy.MemoryStore.getMemories()).length`

## getControlConfig()
- 位置: L763-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AI_CONTROL_OPTIONS.filter()`, `OnDeviceModelManager.isEnabled()`
- 参照: `AiControlStates.available`, `AiControlStates.enabled`, `OnDeviceModelManager.features.SmartWindow`, `config.options`, `option.value`

## visible()
- 位置: L782-783
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AiControlStates.available`, `deps.aiControlSmartWindowSelect.value`

## onUserClick()
- 位置: L784-788
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `lazy.AIWindow.launchWindow()`
- 参照: `window.browsingContext.embedderElement`

## visible()
- 位置: L794-795
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `AiControlStates.enabled`, `deps.aiControlSmartWindowSelect.value`

## onUserClick()
- 位置: L796-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.gotoPref()`

## setup()
- 位置: L849-854
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## observer()
- 位置: L850-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`

## getControlConfig()
- 位置: L855-861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildPresetModelOptions()`, `config.options.find()`
- 参照: `option.value`

## get()
- 位置: L862-874
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.smartWindowFirstRunModelChoice.value`

## set()
- 位置: L875-894
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `lazy.getCachedModelsData()`
- 条件付き依存: `if (customRadioSelected)` → `setting.onChange()`
- 参照: `deps.smartWindowCustomEndpoint.value`, `deps.smartWindowFirstRunModelChoice.value`, `lazy.getCachedModelsData()[String(prev)].model`

## onUserChange()
- 位置: L895-906
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value !== "0")` → `lazy.getCachedModelsData()`
- 条件付き依存: `if (value !== "0")` → `String()`
- 条件付き依存: `if (value !== "0")` → `Glean.smartWindow.settingsModel.record()`
- 参照: `lazy.getCachedModelsData()[String(value)].model`

## getCustomModelFieldValue()
- 位置: L921-927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `editedCustomModelFields.has()`, `field.value?.trim()`

## getCustomModelFormValues()
- 位置: L929-944
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCustomModelFieldValue()`
- 参照: `deps.smartWindowApiKey.value`, `deps.smartWindowCustomEndpoint.value`, `deps.smartWindowModel.value`

## hasUnsavedCustomModelChanges()
- 位置: L946-954
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCustomModelFormValues()`
- 参照: `deps.smartWindowApiKey.value`, `deps.smartWindowCustomEndpoint.value`, `deps.smartWindowModel.value`

## isCustomModelSaveButtonDisabled()
- 位置: L956-959
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCustomModelFormValues()`, `hasUnsavedCustomModelChanges()`, `validateEndpointUrl()`

## setupCustomModelFormChangeListener()
- 位置: L964-977
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `document.removeEventListener()`

## handler()
- 位置: L965-970
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CUSTOM_MODEL_FIELD_IDS.has()`
- 条件付き依存: `if (CUSTOM_MODEL_FIELD_IDS.has(e.target?.id))` → `editedCustomModelFields.add()`
- 条件付き依存: `if (CUSTOM_MODEL_FIELD_IDS.has(e.target?.id))` → `emitChange()`
- 参照: `e.target`, `e.target?.id`

## visible()
- 位置: L982-982
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.modelSelection.value`

## get()
- 位置: L983-985
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.smartWindowModel.value`

## visible()
- 位置: L991-991
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.modelSelection.value`

## get()
- 位置: L992-994
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.smartWindowCustomEndpoint.value`

## visible()
- 位置: L1000-1000
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.modelSelection.value`

## get()
- 位置: L1001-1006
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.smartWindowApiKey.value`

## visible()
- 位置: L1012-1012
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.modelSelection.value`

## visible()
- 位置: L1018-1018
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.modelSelection.value`

## visible()
- 位置: L1032-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasUnsavedCustomModelChanges()`
- 参照: `deps.modelSelection.value`, `deps.smartWindowFirstRunModelChoice.value`

## visible()
- 位置: L1048-1048
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.modelSelection.value`

## onUserClick()
- 位置: L1050-1076
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.settingsModel.record()`, `doc.getElementById()`, `doc.getElementById("customModelAuthToken")?.value?.trim()`, `doc.getElementById("customModelEndpoint")?.value?.trim()`, `doc.getElementById("customModelName")?.value?.trim()`, `lazy.getCachedModelsData()`, `validateEndpointUrl()`
- 参照: `deps.smartWindowApiKey.value`, `deps.smartWindowCustomEndpoint.value`, `deps.smartWindowFirstRunModelChoice.value`, `deps.smartWindowModel.value`, `e.target.ownerDocument`, `lazy.getCachedModelsData()["0"].model`

## onUserChange()
- 位置: L1084-1089
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.settingsMemories.record()`

## onUserChange()
- 位置: L1094-1099
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.settingsMemories.record()`

## onUserClick()
- 位置: async L1104-1113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.memoriesPanelDisplayed.record()`, `e.preventDefault()`, `lazy.MemoryStore.getMemories()`, `window.gotoPref()`
- 参照: `memories?.length`

## onUserClick()
- 位置: L1120-1126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.target.getAttribute()`
- 条件付き依存: `if (action === "delete")` → `lazy.MemoryStore.hardDeleteMemory()`

## onUserClick()
- 位置: async L1131-1177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncConfirmEx()`, `document.l10n.formatValues()`, `lazy.MemoryStore.getMemories()`, `result.get()`
- 条件付き依存: `if (result.get("buttonNumClicked") === 0)` → `Glean.smartWindow.memoriesNuke.record()`
- 条件付き依存: `if (result.get("buttonNumClicked") === 0)` → `lazy.MemoryStore.hardDeleteMemory()`
- 条件付き依存: `if (result.get("buttonNumClicked") === 0)` → `console.error()`
- 参照: `CommonDialog.DEFAULT_APP_ICON_CSS`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_CONTENT`, `memories.length`, `memory.id`, `window.browsingContext`
- XPCOM: `Services.prompt`

## setup()
- 位置: L1187-1208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `Services.prefs.addObserver()`, `Services.prefs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs` / `Services.prefs`

## getMemories()
- 位置: async L1210-1212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MemoryStore.getMemories()`

## getControlConfig()
- 位置: async L1214-1277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `memories.map()`, `this.getMemories()`
- 参照: `memories.length`, `memory.id`, `memory.memory_summary`
- XPCOM: `Services.prefs`
