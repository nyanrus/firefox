# browser/components/preferences/translations.js

source: browser/components/preferences/translations.js
source-hash: c1f37f2dc908847b67dff95083f05723cba463f0
lines: 2158

## <module>
- 役割: (未記入)
- 呼び出し先: `document.addEventListener()`

## dispatchTestEvent()
- 位置: L81-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`
- 参照: `globalThis.Cu?.isInAutomation`

## handleEvent()
- 位置: async L216-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `target.closest()`, `this.handlePaneShown()`, `this.teardown()`
- 条件付き依存: `if (event.target === this.elements?.alwaysTranslateLanguagesSelect)` → `this.onAlwaysTranslateLanguageSelectionChanged()`
- 条件付き依存: `if ( event.target === this.elements?.neverTranslateLanguagesSelect )` → `this.onNeverTranslateLanguageSelectionChanged()`
- 条件付き依存: `if (event.target === this.elements?.downloadLanguagesSelect)` → `this.onDownloadSelectionChanged()`
- 条件付き依存: `if ( target === this.elements?.alwaysTranslateLanguagesButton || target.closest?.("#translationsAlwaysTranslateLanguagesButton") )` → `this.onAlwaysTranslateLanguageChosen()`
- 条件付き依存: `if ( target === this.elements?.neverTranslateLanguagesButton || target.closest?.("#translationsNeverTranslateLanguagesButton") )` → `this.onNeverTranslateLanguageChosen()`
- 条件付き依存: `if ( target === this.elements?.downloadLanguagesButton || target.closest?.("#translationsDownloadLanguagesButton") )` → `this.onDownloadLanguageButtonClicked()`
- 条件付き依存: `if (downloadRemoveButton?.dataset.langTag)` → `this.onDeleteButtonClicked()`
- 条件付き依存: `if (downloadDeleteConfirmButton?.dataset.langTag)` → `this.confirmDeleteLanguage()`
- 条件付き依存: `if (downloadDeleteCancelButton?.dataset.langTag)` → `this.cancelDeleteLanguage()`
- 条件付き依存: `if (downloadRetryButton?.dataset.langTag)` → `this.retryDownloadLanguage()`
- 条件付き依存: `if (alwaysRemoveButton?.dataset.langTag)` → `this.removeAlwaysTranslateLanguage()`
- 条件付き依存: `if (neverRemoveButton?.dataset.langTag)` → `this.removeNeverTranslateLanguage()`
- 条件付き依存: `if (neverSiteRemoveButton?.dataset.origin)` → `this.removeNeverTranslateSite()`
- 参照: `(event).detail?.category`, `alwaysRemoveButton.dataset.langTag`, `alwaysRemoveButton?.dataset.langTag`, `downloadDeleteCancelButton.dataset.langTag`, `downloadDeleteCancelButton?.dataset.langTag`, `downloadDeleteConfirmButton.dataset.langTag`, `downloadDeleteConfirmButton?.dataset.langTag`, `downloadRemoveButton.dataset.langTag`, `downloadRemoveButton?.dataset.langTag`, `downloadRetryButton.dataset.langTag`, `downloadRetryButton?.dataset.langTag`, `event.target`, `event.type`, `neverRemoveButton.dataset.langTag`, `neverRemoveButton?.dataset.langTag`, `neverSiteRemoveButton.dataset.origin`, `neverSiteRemoveButton?.dataset.origin`, `this.elements?.alwaysTranslateLanguagesButton`, `this.elements?.alwaysTranslateLanguagesSelect`, `this.elements?.alwaysTranslateLanguagesSelect?.value`, `this.elements?.downloadLanguagesButton`, `this.elements?.downloadLanguagesSelect`, `this.elements?.neverTranslateLanguagesButton`, `this.elements?.neverTranslateLanguagesSelect`, `this.elements?.neverTranslateLanguagesSelect?.value`

## observe()
- 位置: L336-346
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (data === ALWAYS_TRANSLATE_LANGS_PREF)` → `this.refreshAlwaysTranslateLanguages().catch()`
- 条件付き依存: `if (data === ALWAYS_TRANSLATE_LANGS_PREF)` → `this.refreshAlwaysTranslateLanguages()`
- 条件付き依存: `if (data === NEVER_TRANSLATE_LANGS_PREF)` → `this.refreshNeverTranslateLanguages().catch()`
- 条件付き依存: `if (data === NEVER_TRANSLATE_LANGS_PREF)` → `this.refreshNeverTranslateLanguages()`
- 条件付き依存: `if (topic === "perm-changed")` → `this.handlePermissionChange()`
- 参照: `console.error`

## handlePaneShown()
- 位置: async L354-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 条件付き依存: `if (this.initPromise)` → `this.refreshAlwaysTranslateLanguages()`
- 条件付き依存: `if (this.initPromise)` → `this.refreshNeverTranslateLanguages()`
- 条件付き依存: `if (this.initPromise)` → `this.refreshNeverTranslateSites()`
- 条件付き依存: `if (this.initPromise)` → `this.refreshDownloadedLanguages()`
- 条件付き依存: `if (this.initPromise)` → `this.dispatchInitializedTestEvent()`
- 条件付き依存: `if (this.initialized)` → `this.refreshAlwaysTranslateLanguages()`
- 条件付き依存: `if (this.initialized)` → `this.refreshNeverTranslateLanguages()`
- 条件付き依存: `if (this.initialized)` → `this.refreshNeverTranslateSites()`
- 条件付き依存: `if (this.initialized)` → `this.refreshDownloadedLanguages()`
- 条件付き依存: `if (this.initialized)` → `this.dispatchInitializedTestEvent()`
- 参照: `this.initPromise`, `this.initialized`

## ensurePaneRendered()
- 位置: async L388-426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `document.querySelector()`, `document.querySelectorAll()`
- 条件付き依存: `if (pane?.getUpdateComplete)` → `promises.push()`
- 条件付き依存: `if (pane?.getUpdateComplete)` → `pane.getUpdateComplete()`
- 条件付き依存: `if (group?.getUpdateComplete)` → `promises.push()`
- 条件付き依存: `if (group?.getUpdateComplete)` → `group.getUpdateComplete()`
- 条件付き依存: `if (promises.length)` → `Promise.allSettled()`
- 条件付き依存: `if (promises.length)` → `results.find()`
- 条件付き依存: `if (failure && failure.reason)` → `console.warn()`
- 参照: `failure.reason`, `group?.getUpdateComplete`, `pane?.getUpdateComplete`, `promises.length`, `result.status`, `this.paneRenderPromise`

## init()
- 位置: async L433-519
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `TranslationsParent.createLanguageDisplayNames()`, `TranslationsParent.getLanguageList()`, `TranslationsParent.getSupportedLanguages()`, `console.error()`, `this.buildAlwaysTranslateSelectOptions()`, `this.buildDownloadSelectOptions()`, `this.buildNeverTranslateSelectOptions()`, `this.cacheElements()`, `this.dispatchInitializedTestEvent()`, `this.elements.alwaysTranslateLanguagesButton.addEventListener()`, `this.elements.alwaysTranslateLanguagesGroup.addEventListener()`, `this.elements.alwaysTranslateLanguagesSelect.addEventListener()`, `this.elements.downloadLanguagesButton.addEventListener()`, `this.elements.downloadLanguagesGroup.addEventListener()`, `this.elements.downloadLanguagesSelect.addEventListener()`, `this.elements.neverTranslateLanguagesButton.addEventListener()`, `this.elements.neverTranslateLanguagesGroup.addEventListener()`, `this.elements.neverTranslateLanguagesSelect.addEventListener()`, `this.elements.neverTranslateSitesGroup.addEventListener()`, `this.ensurePaneRendered()`, `this.loadLanguageSizes()`, `this.refreshAlwaysTranslateLanguages()`, `this.refreshDownloadedLanguages()`, `this.refreshNeverTranslateLanguages()`, `this.refreshNeverTranslateSites()`, `this.renderDownloadLanguages()`, `this.resetDownloadSelect()`, `this.setDownloadLanguageButtonDisabledState()`, `window.addEventListener()`
- 条件付き依存: `if ( !this.elements?.alwaysTranslateLanguagesGroup || !this.elements?.alwaysTranslateLanguagesSelect || !this.elements?.alwaysTranslateLanguagesButton || !this.e...)` → `this.dispatchInitializedTestEvent()`
- 参照: `this.elements.alwaysTranslateLanguagesButton.disabled`, `this.elements.alwaysTranslateLanguagesSelect.disabled`, `this.elements.downloadLanguagesSelect.disabled`, `this.elements.neverTranslateLanguagesButton.disabled`, `this.elements.neverTranslateLanguagesSelect.disabled`, `this.elements?.alwaysTranslateLanguagesButton`, `this.elements?.alwaysTranslateLanguagesGroup`, `this.elements?.alwaysTranslateLanguagesNoneRow`, `this.elements?.alwaysTranslateLanguagesSelect`, `this.elements?.downloadLanguagesButton`, `this.elements?.downloadLanguagesGroup`, `this.elements?.downloadLanguagesNoneRow`, `this.elements?.downloadLanguagesSelect`, `this.elements?.neverTranslateLanguagesButton`, `this.elements?.neverTranslateLanguagesGroup`, `this.elements?.neverTranslateLanguagesNoneRow`, `this.elements?.neverTranslateLanguagesSelect`, `this.elements?.neverTranslateSitesGroup`, `this.initialized`, `this.languageDisplayNames`, `this.languageList`, `this.numberFormatter`, `this.supportedLanguages`
- XPCOM: `Services.obs`

## dispatchInitializedTestEvent()
- 位置: L524-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchTestEvent()`

## cacheElements()
- 位置: L531-596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `elements.alwaysTranslateLanguagesGroup`, `elements.alwaysTranslateLanguagesNoneRow`, `elements.alwaysTranslateLanguagesSelect`, `elements.neverTranslateLanguagesGroup`, `elements.neverTranslateLanguagesNoneRow`, `elements.neverTranslateLanguagesSelect`, `this.elements`

## loadLanguageSizes()
- 位置: async L603-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `TranslationsParent.getLanguageSize()`, `console.error()`, `this.languageList.map()`
- 参照: `this.languageList?.length`, `this.languageSizes`

## formatLanguageSize()
- 位置: L632-644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `this.getNumberFormatter()`, `this.getNumberFormatter().format()`, `this.languageSizes?.get()`

## getNumberFormatter()
- 位置: L651-663
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Intl.NumberFormat`, `Services.locale.appLocaleAsBCP47`, `this.numberFormatter`
- XPCOM: `Services.locale`

## formatDownloadLabel()
- 位置: async L671-686
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `document.l10n.formatValue()`, `this.formatLanguageLabel()`, `this.formatLanguageSize()`

## buildDownloadSelectOptions()
- 位置: async L693-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( this.formatLanguageLabel(lhs.langTag) ?? lhs.displayName ).localeCompare()`, `[...this.supportedLanguages.sourceLanguages] .filter()`, `[...this.supportedLanguages.sourceLanguages] .filter(({ langTag }) => langTag !== "en") .sort()`, `document.createElement()`, `option.setAttribute()`, `select.appendChild()`, `select.querySelector()`, `select.querySelectorAll()`, `this.formatDownloadLabel()`, `this.formatLanguageLabel()`, `this.formatLanguageSize()`, `this.resetDownloadSelect()`, `this.updateDownloadSelectOptionState()`
- 条件付き依存: `if (option !== placeholder)` → `option.remove()`
- 条件付き依存: `if (sizeLabel)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (sizeLabel)` → `this.formatLanguageLabel()`
- 参照: `lhs.displayName`, `lhs.langTag`, `rhs.displayName`, `rhs.langTag`, `this.elements?.downloadLanguagesSelect`, `this.supportedLanguages.sourceLanguages`, `this.supportedLanguages?.sourceLanguages?.length`

## updateDownloadSelectOptionState()
- 位置: L744-767
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchTestEvent()`, `option.getAttribute()`, `option.toggleAttribute()`, `select.querySelectorAll()`, `this.downloadedLanguageTags.has()`, `this.downloadingLanguageTags.has()`
- 条件付き依存: `if (preserveSelection)` → `this.updateDownloadLanguageButtonDisabled()`
- 条件付き依存: `if (!(preserveSelection))` → `this.resetDownloadSelect()`
- 参照: `this.elements?.downloadLanguagesSelect`

## onAlwaysTranslateLanguageChosen()
- 位置: async L774-791
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.addLangTagToPref()`, `TranslationsParent.removeLangTagFromPref()`, `this.resetAlwaysTranslateSelect()`, `this.shouldDisableAlwaysTranslateAddButton()`
- 条件付き依存: `if (!langTag)` → `this.updateAlwaysTranslateAddButtonDisabledState()`
- 条件付き依存: `if (this.shouldDisableAlwaysTranslateAddButton())` → `this.updateAlwaysTranslateAddButtonDisabledState()`

## onAlwaysTranslateLanguageSelectionChanged()
- 位置: L796-798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateAlwaysTranslateAddButtonDisabledState()`

## shouldDisableAlwaysTranslateAddButton()
- 位置: L805-820
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `option?.hasAttribute()`, `select.querySelector()`
- 参照: `select.disabled`, `select.value`, `this.elements?.alwaysTranslateLanguagesSelect`

## setAlwaysTranslateAddButtonDisabledState()
- 位置: L827-841
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (wasDisabled !== isDisabled)` → `dispatchTestEvent()`
- 参照: `this.elements.alwaysTranslateLanguagesButton.disabled`, `this.elements?.alwaysTranslateLanguagesButton`

## updateAlwaysTranslateAddButtonDisabledState()
- 位置: L846-850
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setAlwaysTranslateAddButtonDisabledState()`, `this.shouldDisableAlwaysTranslateAddButton()`

## removeAlwaysTranslateLanguage()
- 位置: L857-862
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.removeLangTagFromPref()`

## resetSelect()
- 位置: async L864-886
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`
- 参照: `select.inputEl`, `select.inputEl.value`, `select.updateComplete`, `select.value`, `setting.value`

## resetAlwaysTranslateSelect()
- 位置: async L891-897
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetSelect()`, `this.updateAlwaysTranslateAddButtonDisabledState()`
- 参照: `this.elements?.alwaysTranslateLanguagesSelect`

## refreshAlwaysTranslateLanguages()
- 位置: async L902-927
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `TranslationsParent.getAlwaysTranslateLanguages()`, `this.renderAlwaysTranslateLanguages()`, `this.updateAlwaysTranslateSelectOptionState()`
- 条件付き依存: `if (this.alwaysTranslateLanguageTags)` → `this.alwaysTranslateLanguageTags.has()`
- 条件付き依存: `if (this.alwaysTranslateLanguageTags)` → `TranslationsParent.removeLangTagFromPref()`
- 参照: `this.alwaysTranslateLanguageTags`, `this.elements?.alwaysTranslateLanguagesGroup`

## renderAlwaysTranslateLanguages()
- 位置: L934-1019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...langTags].sort()`, `alwaysTranslateLanguagesGroup.querySelectorAll()`, `dispatchTestEvent()`, `document.createElement()`, `item.appendChild()`, `item.classList.add()`, `item.remove()`, `item.setAttribute()`, `labelA.localeCompare()`, `removeButton.classList.add()`, `removeButton.setAttribute()`, `this.formatLanguageLabel()`
- 条件付き依存: `if (hasLanguages && alwaysTranslateLanguagesNoneRow.isConnected)` → `alwaysTranslateLanguagesNoneRow.remove()`
- 条件付き依存: `if ( !hasLanguages && !alwaysTranslateLanguagesNoneRow.isConnected )` → `alwaysTranslateLanguagesGroup.appendChild()`
- 条件付き依存: `if ( alwaysTranslateLanguagesNoneRow && alwaysTranslateLanguagesNoneRow.parentElement === alwaysTranslateLanguagesGroup )` → `alwaysTranslateLanguagesGroup.insertBefore()`
- 条件付き依存: `if (!( alwaysTranslateLanguagesNoneRow && alwaysTranslateLanguagesNoneRow.parentElement === alwaysTranslateLanguagesGroup ))` → `alwaysTranslateLanguagesGroup.appendChild()`
- 条件付き依存: `if (previousEmptyStateVisible && !currentEmptyStateVisible)` → `dispatchTestEvent()`
- 条件付き依存: `if (!previousEmptyStateVisible && currentEmptyStateVisible)` → `dispatchTestEvent()`
- 参照: `alwaysTranslateLanguagesNoneRow.hidden`, `alwaysTranslateLanguagesNoneRow.isConnected`, `alwaysTranslateLanguagesNoneRow.parentElement`, `item.dataset.langTag`, `langTags.length`, `removeButton.dataset.langTag`, `this.elements`

## formatLanguageLabel()
- 位置: L1027-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `this.languageDisplayNames?.of()`

## buildAlwaysTranslateSelectOptions()
- 位置: async L1039-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( this.formatLanguageLabel(lhs.langTag) ?? lhs.displayName ).localeCompare()`, `[...this.supportedLanguages.sourceLanguages].sort()`, `document.createElement()`, `option.setAttribute()`, `select.appendChild()`, `select.querySelector()`, `select.querySelectorAll()`, `this.formatLanguageLabel()`, `this.resetAlwaysTranslateSelect()`
- 条件付き依存: `if (option !== placeholder)` → `option.remove()`
- 参照: `lhs.displayName`, `lhs.langTag`, `rhs.displayName`, `rhs.langTag`, `this.elements?.alwaysTranslateLanguagesSelect`, `this.supportedLanguages.sourceLanguages`, `this.supportedLanguages?.sourceLanguages?.length`

## updateAlwaysTranslateSelectOptionState()
- 位置: async L1076-1093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchTestEvent()`, `option.getAttribute()`, `select.querySelectorAll()`, `this.alwaysTranslateLanguageTags.has()`, `this.resetAlwaysTranslateSelect()`
- 参照: `option.disabled`, `this.elements?.alwaysTranslateLanguagesSelect`

## onNeverTranslateLanguageChosen()
- 位置: async L1100-1117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.addLangTagToPref()`, `TranslationsParent.removeLangTagFromPref()`, `this.resetNeverTranslateSelect()`, `this.shouldDisableNeverTranslateAddButton()`
- 条件付き依存: `if (!langTag)` → `this.updateNeverTranslateAddButtonDisabledState()`
- 条件付き依存: `if (this.shouldDisableNeverTranslateAddButton())` → `this.updateNeverTranslateAddButtonDisabledState()`

## onNeverTranslateLanguageSelectionChanged()
- 位置: L1122-1124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateNeverTranslateAddButtonDisabledState()`

## shouldDisableNeverTranslateAddButton()
- 位置: L1131-1146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `option?.hasAttribute()`, `select.querySelector()`
- 参照: `select.disabled`, `select.value`, `this.elements?.neverTranslateLanguagesSelect`

## setNeverTranslateAddButtonDisabledState()
- 位置: L1153-1167
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (wasDisabled !== isDisabled)` → `dispatchTestEvent()`
- 参照: `this.elements.neverTranslateLanguagesButton.disabled`, `this.elements?.neverTranslateLanguagesButton`

## updateNeverTranslateAddButtonDisabledState()
- 位置: L1172-1176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setNeverTranslateAddButtonDisabledState()`, `this.shouldDisableNeverTranslateAddButton()`

## removeNeverTranslateLanguage()
- 位置: L1183-1188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.removeLangTagFromPref()`

## resetNeverTranslateSelect()
- 位置: async L1193-1199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.resetSelect()`, `this.updateNeverTranslateAddButtonDisabledState()`
- 参照: `this.elements?.neverTranslateLanguagesSelect`

## refreshNeverTranslateLanguages()
- 位置: async L1204-1216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `TranslationsParent.getNeverTranslateLanguages()`, `this.renderNeverTranslateLanguages()`, `this.updateNeverTranslateSelectOptionState()`
- 参照: `this.elements?.neverTranslateLanguagesGroup`, `this.neverTranslateLanguageTags`

## renderNeverTranslateLanguages()
- 位置: L1223-1303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...langTags].sort()`, `dispatchTestEvent()`, `document.createElement()`, `item.appendChild()`, `item.classList.add()`, `item.remove()`, `item.setAttribute()`, `labelA.localeCompare()`, `neverTranslateLanguagesGroup.querySelectorAll()`, `removeButton.classList.add()`, `removeButton.setAttribute()`, `this.formatLanguageLabel()`
- 条件付き依存: `if (neverTranslateLanguagesNoneRow)` → `Boolean()`
- 条件付き依存: `if (hasLanguages && neverTranslateLanguagesNoneRow.isConnected)` → `neverTranslateLanguagesNoneRow.remove()`
- 条件付き依存: `if (!hasLanguages && !neverTranslateLanguagesNoneRow.isConnected)` → `neverTranslateLanguagesGroup.appendChild()`
- 条件付き依存: `if ( neverTranslateLanguagesNoneRow && neverTranslateLanguagesNoneRow.parentElement === neverTranslateLanguagesGroup )` → `neverTranslateLanguagesGroup.insertBefore()`
- 条件付き依存: `if (!( neverTranslateLanguagesNoneRow && neverTranslateLanguagesNoneRow.parentElement === neverTranslateLanguagesGroup ))` → `neverTranslateLanguagesGroup.appendChild()`
- 条件付き依存: `if (previousEmptyStateVisible && !currentEmptyStateVisible)` → `dispatchTestEvent()`
- 条件付き依存: `if (!previousEmptyStateVisible && currentEmptyStateVisible)` → `dispatchTestEvent()`
- 参照: `item.dataset.langTag`, `langTags.length`, `neverTranslateLanguagesNoneRow.hidden`, `neverTranslateLanguagesNoneRow.isConnected`, `neverTranslateLanguagesNoneRow.parentElement`, `removeButton.dataset.langTag`, `this.elements`

## buildNeverTranslateSelectOptions()
- 位置: async L1308-1340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( this.formatLanguageLabel(lhs.langTag) ?? lhs.displayName ).localeCompare()`, `[...this.supportedLanguages.sourceLanguages].sort()`, `document.createElement()`, `option.setAttribute()`, `select.appendChild()`, `select.querySelector()`, `select.querySelectorAll()`, `this.formatLanguageLabel()`, `this.resetNeverTranslateSelect()`
- 条件付き依存: `if (option !== placeholder)` → `option.remove()`
- 参照: `lhs.displayName`, `lhs.langTag`, `rhs.displayName`, `rhs.langTag`, `this.elements?.neverTranslateLanguagesSelect`, `this.supportedLanguages.sourceLanguages`, `this.supportedLanguages?.sourceLanguages?.length`

## updateNeverTranslateSelectOptionState()
- 位置: async L1345-1362
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatchTestEvent()`, `option.getAttribute()`, `select.querySelectorAll()`, `this.neverTranslateLanguageTags.has()`, `this.resetNeverTranslateSelect()`
- 参照: `option.disabled`, `this.elements?.neverTranslateLanguagesSelect`

## refreshNeverTranslateSites()
- 位置: L1367-1382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.listNeverTranslateSites()`, `console.error()`, `this.renderNeverTranslateSites()`
- 参照: `this.elements?.neverTranslateSitesGroup`, `this.neverTranslateSiteOrigins`

## renderNeverTranslateSites()
- 位置: L1389-1461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...siteOrigins].sort()`, `dispatchTestEvent()`, `document.createElement()`, `item.appendChild()`, `item.classList.add()`, `item.remove()`, `item.setAttribute()`, `neverTranslateSitesGroup.querySelectorAll()`, `removeButton.classList.add()`, `removeButton.setAttribute()`, `this.getSiteSortKey()`, `this.getSiteSortKey(originA).localeCompare()`
- 条件付き依存: `if (neverTranslateSitesNoneRow)` → `Boolean()`
- 条件付き依存: `if (hasSites && neverTranslateSitesNoneRow.isConnected)` → `neverTranslateSitesNoneRow.remove()`
- 条件付き依存: `if (!hasSites && !neverTranslateSitesNoneRow.isConnected)` → `neverTranslateSitesGroup.appendChild()`
- 条件付き依存: `if ( neverTranslateSitesNoneRow && neverTranslateSitesNoneRow.parentElement === neverTranslateSitesGroup )` → `neverTranslateSitesGroup.insertBefore()`
- 条件付き依存: `if (!( neverTranslateSitesNoneRow && neverTranslateSitesNoneRow.parentElement === neverTranslateSitesGroup ))` → `neverTranslateSitesGroup.appendChild()`
- 条件付き依存: `if (previousEmptyStateVisible && !currentEmptyStateVisible)` → `dispatchTestEvent()`
- 条件付き依存: `if (!previousEmptyStateVisible && currentEmptyStateVisible)` → `dispatchTestEvent()`
- 参照: `item.dataset.origin`, `neverTranslateSitesNoneRow.hidden`, `neverTranslateSitesNoneRow.isConnected`, `neverTranslateSitesNoneRow.parentElement`, `removeButton.dataset.origin`, `siteOrigins.length`, `this.elements`

## removeNeverTranslateSite()
- 位置: L1468-1481
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.setNeverTranslateSiteByOrigin()`, `console.error()`, `this.neverTranslateSiteOrigins.has()`, `this.refreshNeverTranslateSites()`

## getSiteSortKey()
- 位置: L1489-1495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `Services.io.newURI(origin).asciiHostPort`
- XPCOM: `Services.io`

## onDownloadSelectionChanged()
- 位置: L1500-1502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateDownloadLanguageButtonDisabled()`

## shouldDisableDownloadLanguageButton()
- 位置: L1509-1524
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `option?.hasAttribute()`, `select.querySelector()`
- 参照: `select.value`, `this.currentDownloadLangTag`, `this.elements?.downloadLanguagesSelect`

## setDownloadLanguageButtonDisabledState()
- 位置: L1531-1547
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (wasDisabled !== isDisabled)` → `dispatchTestEvent()`
- 参照: `button.disabled`, `this.elements?.downloadLanguagesButton`

## updateDownloadLanguageButtonDisabled()
- 位置: L1552-1556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setDownloadLanguageButtonDisabledState()`, `this.shouldDisableDownloadLanguageButton()`

## onDownloadLanguageButtonClicked()
- 位置: async L1563-1598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.downloadLanguageFiles()`, `console.error()`, `dispatchTestEvent()`, `this.downloadFailedLanguageTags.add()`, `this.downloadFailedLanguageTags.clear()`, `this.downloadPendingDeleteLanguageTags.clear()`, `this.downloadedLanguageTags.add()`, `this.downloadingLanguageTags.add()`, `this.downloadingLanguageTags.delete()`, `this.renderDownloadLanguages()`, `this.setDownloadControlsDisabled()`, `this.updateDownloadLanguageButtonDisabled()`, `this.updateDownloadSelectOptionState()`
- 参照: `this.currentDownloadLangTag`, `this.elements?.downloadLanguagesSelect?.value`

## setDownloadControlsDisabled()
- 位置: L1605-1612
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setDownloadLanguageButtonDisabledState()`, `this.shouldDisableDownloadLanguageButton()`
- 参照: `this.elements.downloadLanguagesSelect.disabled`, `this.elements?.downloadLanguagesSelect`

## setIconButtonGhostState()
- 位置: L1620-1628
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.getAttribute()`
- 条件付き依存: `if (button.getAttribute("type") !== type)` → `button.setAttribute()`

## resetDownloadSelect()
- 位置: L1633-1644
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`, `this.updateDownloadLanguageButtonDisabled()`
- 参照: `setting.value`, `this.elements.downloadLanguagesSelect.value`, `this.elements?.downloadLanguagesSelect`

## refreshDownloadedLanguages()
- 位置: async L1651-1689
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `TranslationsParent.hasAllFilesForLanguage()`, `console.error()`, `downloaded.filter()`, `downloaded.filter(([, isDownloaded]) => isDownloaded).map()`, `this.downloadPendingDeleteLanguageTags.clear()`, `this.languageList.map()`, `this.renderDownloadLanguages()`, `this.updateDownloadLanguageButtonDisabled()`, `this.updateDownloadSelectOptionState()`
- 条件付き依存: `if (isDownloaded)` → `this.downloadingLanguageTags.delete()`
- 条件付き依存: `if (isDownloaded)` → `this.downloadFailedLanguageTags.delete()`
- 条件付き依存: `if (!(isDownloaded))` → `this.downloadPendingDeleteLanguageTags.delete()`
- 参照: `this.downloadedLanguageTags`, `this.languageList?.length`

## createDeleteConfirmationItem()
- 位置: async L1698-1762
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttonGroup.append()`, `cancelButton.classList.add()`, `cancelButton.setAttribute()`, `confirmContent.appendChild()`, `deleteButton.classList.add()`, `deleteButton.setAttribute()`, `document.createElement()`, `document.l10n.formatValue()`, `document.l10n.setAttributes()`, `item.appendChild()`, `this.formatLanguageLabel()`, `this.formatLanguageSize()`, `this.setIconButtonGhostState()`, `warningButton.classList.add()`, `warningButton.setAttribute()`
- 条件付き依存: `if (!deleteButton.disabled)` → `requestAnimationFrame()`
- 条件付き依存: `if (deleteButton.isConnected)` → `deleteButton.focus()`
- 参照: `cancelButton.dataset.langTag`, `cancelButton.disabled`, `confirmContent.style.cssText`, `confirmText.textContent`, `deleteButton.dataset.langTag`, `deleteButton.disabled`, `deleteButton.isConnected`, `warningButton.dataset.langTag`, `warningButton.style.color`, `warningButton.style.pointerEvents`

## createFailedDownloadItem()
- 位置: async L1771-1822
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `document.l10n.setAttributes()`, `errorButton.classList.add()`, `errorButton.setAttribute()`, `errorContent.appendChild()`, `item.appendChild()`, `retryButton.classList.add()`, `retryButton.setAttribute()`, `this.formatLanguageLabel()`, `this.formatLanguageSize()`, `this.setIconButtonGhostState()`
- 条件付き依存: `if (!retryButton.disabled)` → `requestAnimationFrame()`
- 条件付き依存: `if (retryButton.isConnected)` → `retryButton.focus()`
- 参照: `errorButton.dataset.langTag`, `errorButton.style.color`, `errorButton.style.pointerEvents`, `errorContent.style.cssText`, `retryButton.dataset.langTag`, `retryButton.disabled`, `retryButton.isConnected`

## createDownloadLanguageItem()
- 位置: async L1833-1874
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `item.appendChild()`, `item.setAttribute()`, `removeButton.classList.add()`, `removeButton.getAttribute()`, `removeButton.setAttribute()`, `this.formatDownloadLabel()`, `this.setIconButtonGhostState()`
- 条件付き依存: `if (isDownloading)` → `item.setAttribute()`
- 参照: `removeButton.dataset.langTag`, `removeButton.disabled`, `removeButton.style.pointerEvents`

## renderDownloadLanguages()
- 位置: async L1881-1990
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Boolean()`, `[...langTags].sort()`, `dispatchTestEvent()`, `document.createElement()`, `document.l10n.formatValue()`, `downloadLanguagesGroup.querySelectorAll()`, `item.classList.add()`, `item.remove()`, `labelA.localeCompare()`, `sortedLangTags.filter()`, `this.downloadFailedLanguageTags.has()`, `this.downloadPendingDeleteLanguageTags.has()`, `this.downloadingLanguageTags.has()`, `this.formatLanguageLabel()`
- 条件付き依存: `if (hasLanguages && downloadLanguagesNoneRow.isConnected)` → `downloadLanguagesNoneRow.remove()`
- 条件付き依存: `if (!hasLanguages && !downloadLanguagesNoneRow.isConnected)` → `downloadLanguagesGroup.appendChild()`
- 条件付き依存: `if (previousEmptyStateVisible && !currentEmptyStateVisible)` → `dispatchTestEvent()`
- 条件付き依存: `if (!previousEmptyStateVisible && currentEmptyStateVisible)` → `dispatchTestEvent()`
- 条件付き依存: `if (isPendingDelete)` → `this.createDeleteConfirmationItem()`
- 条件付き依存: `if (isFailed)` → `item.classList.add()`
- 条件付き依存: `if (isFailed)` → `this.createFailedDownloadItem()`
- 条件付き依存: `if (!(isFailed))` → `this.createDownloadLanguageItem()`
- 条件付き依存: `if ( downloadLanguagesNoneRow && downloadLanguagesNoneRow.parentElement === downloadLanguagesGroup )` → `downloadLanguagesGroup.insertBefore()`
- 条件付き依存: `if (!( downloadLanguagesNoneRow && downloadLanguagesNoneRow.parentElement === downloadLanguagesGroup ))` → `downloadLanguagesGroup.appendChild()`
- 参照: `downloadLanguagesNoneRow.hidden`, `downloadLanguagesNoneRow.isConnected`, `downloadLanguagesNoneRow.parentElement`, `item.dataset.langTag`, `langTags.length`, `sortedLangTags.length`, `this.currentDownloadLangTag`, `this.downloadFailedLanguageTags`, `this.downloadedLanguageTags`, `this.downloadingLanguageTags`, `this.elements`

## onDeleteButtonClicked()
- 位置: async L1998-2007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.downloadFailedLanguageTags.clear()`, `this.downloadPendingDeleteLanguageTags.add()`, `this.downloadPendingDeleteLanguageTags.clear()`, `this.downloadedLanguageTags.has()`, `this.renderDownloadLanguages()`

## confirmDeleteLanguage()
- 位置: async L2015-2035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.deleteLanguageFiles()`, `console.error()`, `dispatchTestEvent()`, `this.downloadPendingDeleteLanguageTags.delete()`, `this.downloadPendingDeleteLanguageTags.has()`, `this.downloadedLanguageTags.delete()`, `this.renderDownloadLanguages()`, `this.updateDownloadLanguageButtonDisabled()`, `this.updateDownloadSelectOptionState()`

## cancelDeleteLanguage()
- 位置: async L2043-2050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.downloadPendingDeleteLanguageTags.delete()`, `this.downloadPendingDeleteLanguageTags.has()`, `this.renderDownloadLanguages()`

## retryDownloadLanguage()
- 位置: async L2058-2091
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TranslationsParent.downloadLanguageFiles()`, `console.error()`, `dispatchTestEvent()`, `this.downloadFailedLanguageTags.add()`, `this.downloadFailedLanguageTags.delete()`, `this.downloadFailedLanguageTags.has()`, `this.downloadedLanguageTags.add()`, `this.downloadingLanguageTags.add()`, `this.downloadingLanguageTags.delete()`, `this.renderDownloadLanguages()`, `this.setDownloadControlsDisabled()`, `this.updateDownloadLanguageButtonDisabled()`, `this.updateDownloadSelectOptionState()`
- 参照: `this.currentDownloadLangTag`

## handlePermissionChange()
- 位置: L2099-2112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subject?.QueryInterface()`, `this.refreshNeverTranslateSites()`
- 条件付き依存: `if (data === "cleared")` → `this.renderNeverTranslateSites()`
- 参照: `Ci.nsIPermission`, `perm?.type`, `this.neverTranslateSiteOrigins`
- XPCOM: [`nsIPermission`](../../../netwerk/base/nsIPermission.idl.md)

## teardown()
- 位置: L2117-2154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `document.removeEventListener()`, `this.elements?.alwaysTranslateLanguagesButton?.removeEventListener()`, `this.elements?.alwaysTranslateLanguagesGroup?.removeEventListener()`, `this.elements?.alwaysTranslateLanguagesSelect?.removeEventListener()`, `this.elements?.downloadLanguagesButton?.removeEventListener()`, `this.elements?.downloadLanguagesGroup?.removeEventListener()`, `this.elements?.downloadLanguagesSelect?.removeEventListener()`, `this.elements?.neverTranslateLanguagesButton?.removeEventListener()`, `this.elements?.neverTranslateLanguagesGroup?.removeEventListener()`, `this.elements?.neverTranslateLanguagesSelect?.removeEventListener()`, `this.elements?.neverTranslateSitesGroup?.removeEventListener()`, `window.removeEventListener()`
- XPCOM: `Services.obs`
