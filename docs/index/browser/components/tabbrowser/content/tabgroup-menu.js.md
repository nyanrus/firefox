# browser/components/tabbrowser/content/tabgroup-menu.js

source: browser/components/tabbrowser/content/tabgroup-menu.js
source-hash: 1902d2d40887aba210d5abc1b8bd1c3326bb561f
lines: 1549

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## MozTabbrowserTabGroupMenu.constructor()
- 位置: L362-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`, `this.#onSmartTabGroupsOptInPrefChange.bind()`, `this.#onSmartTabGroupsPrefChange.bind()`

## MozTabbrowserTabGroupMenu.connectedCallback()
- 位置: L404-562
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContentSharingUtils.handleShareTabGroup()`, `Glean.tabgroup.groupInteractions.copy_all_links.add()`, `Glean.tabgroup.smartTabEnabled.set()`, `TabMetrics.userTriggeredContext()`, `document.getElementById()`, `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.removeTabGroup()`, `gBrowser.replaceGroupWithWindow()`, `lazy.AIWindow.createAITab()`, `this.#cancelButton.addEventListener()`, `this.#commandButtons.addNewTabInGroup.addEventListener()`, `this.#commandButtons.copyAllLinks.addEventListener()`, `this.#commandButtons.createAITab.addEventListener()`, `this.#commandButtons.deleteGroup.addEventListener()`, `this.#commandButtons.moveGroupToNewWindow.addEventListener()`, `this.#commandButtons.saveAndCloseGroup.addEventListener()`, `this.#commandButtons.shareTabGroup.addEventListener()`, `this.#commandButtons.ungroupTabs.addEventListener()`, `this.#createButton.addEventListener()`, `this.#getGroupLinks()`, `this.#handleMlTelemetry()`, `this.#handleNewTabInGroup()`, `this.#initSuggestions()`, `this.#nameField.addEventListener()`, `this.#panel.addEventListener()`, `this.#populateSwatches()`, `this.#swatchesContainer.addEventListener()`, `this.activeGroup.saveAndClose()`, `this.activeGroup.tabs.map()`, `this.activeGroup.ungroupTabs()`, `this.appendChild()`, `this.close()`, `this.initializeAttributeInheritance()`, `this.panel.addEventListener()`, `this.querySelector()`
- 条件付き依存: `if (e.target !== this.#nameField)` → `this.#nameField.blur()`
- 条件付き依存: `if (links.length)` → `BrowserUtils.copyLinks()`

## this.canShowAIUserInterface()
- 位置: L467-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tabs.forEach()`

## MozTabbrowserTabGroupMenu.smartTabGroupsEnabled()
- 位置: L564-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.locale.appLocaleAsBCP47.startsWith()`
- XPCOM: `Services.locale`

## MozTabbrowserTabGroupMenu.smartTabGroupsPrefEnabled()
- 位置: L574-580
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.#onSmartTabGroupsPrefChange()
- 位置: L582-596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.smartTab.record()`, `Glean.tabgroup.smartTabEnabled.set()`
- 条件付き依存: `if (!this.#smartTabGroupsInitiated && this.smartTabGroupsEnabled)` → `this.#initSuggestions()`

## MozTabbrowserTabGroupMenu.#onSmartTabGroupsOptInPrefChange()
- 位置: L598-603
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.smartTab.record()`, `Glean.tabgroup.smartTabEnabled.set()`

## MozTabbrowserTabGroupMenu.#initSmartTabGroupsOptin()
- 位置: L605-674
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `document.createElement()`, `openTrustedLinkIn()`, `this.#handleFirstDownloadAndSuggest()`, `this.#handleMLOptinTelemetry()`, `this.#setFormToDisabled()`, `this.#smartTabGroupingManager.terminateProcess()`, `this.#suggestionsOptin.addEventListener()`, `this.#suggestionsOptinContainer.appendChild()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabGroupMenu.#initSuggestions()
- 位置: L676-765
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `this.#cancelSuggestionsButton.addEventListener()`, `this.#createSuggestionsButton.addEventListener()`, `this.#handleLoadSuggestionsCancel()`, `this.#handleMlTelemetry()`, `this.#handleSmartSuggest()`, `this.#initSmartTabGroupsOptin()`, `this.#selectSuggestionsCheckbox.addEventListener()`, `this.#suggestionButton.addEventListener()`, `this.#suggestionsLoadCancel.addEventListener()`, `this.activeGroup.addTabs()`, `this.close()`, `this.querySelector()`
- 条件付き依存: `if (e.target.checked)` → `this.#handleSelectAll()`
- 条件付き依存: `if (!(e.target.checked))` → `this.#handleDeselectAll()`

## MozTabbrowserTabGroupMenu.#populateSwatches()
- 位置: L767-793
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `label.classList.add()`, `label.setAttribute()`, `label.style.setProperty()`, `this.#clearSwatches()`, `this.#swatches.push()`, `this.#swatchesContainer.append()`

## MozTabbrowserTabGroupMenu.#clearSwatches()
- 位置: L795-798
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.createMode()
- 位置: L800-802
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.createMode()
- 位置: L804-817
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel.classList.toggle()`, `this.#panel.setAttribute()`

## MozTabbrowserTabGroupMenu.activeGroup()
- 位置: L819-821
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.activeGroup()
- 位置: L823-833
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#swatches.forEach()`

## MozTabbrowserTabGroupMenu.nextUnusedColor()
- 位置: L835-851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MozTabbrowserTabGroupMenu.COLORS.find()`, `gBrowser.getAllTabGroups()`, `gBrowser.getAllTabGroups().forEach()`, `usedColors.includes()`, `usedColors.push()`
- 条件付き依存: `if (!color)` → `Math.floor()`
- 条件付き依存: `if (!color)` → `Math.random()`

## MozTabbrowserTabGroupMenu.panel()
- 位置: L853-855
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.#panelPosition()
- 位置: L857-864
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.#initMlGroupLabel()
- 位置: async L869-884
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.visibleTabs.filter()`, `tabs.includes()`, `this.#setMlGroupLabel()`, `this.#smartTabGroupingManager.getPredictedLabelForGroup()`

## MozTabbrowserTabGroupMenu.#shouldUpdateLabelWithMlLabel()
- 位置: L891-893
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.#setMlGroupLabel()
- 位置: L902-910
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#nameField.select()`, `this.#shouldUpdateLabelWithMlLabel()`

## MozTabbrowserTabGroupMenu.openCreateModal()
- 位置: L912-933
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#initMlGroupLabel()`, `this.#maybeUpdateLayoutForNova()`, `this.#panel.openPopup()`
- 条件付き依存: `if (this.smartTabGroupsEnabled)` → `this.#smartTabGroupingManager.initEmbeddingEngine()`

## MozTabbrowserTabGroupMenu.mlLabel()
- 位置: L938-940
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.mlLabel()
- 位置: L942-944
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.hasSuggestedMlTabs()
- 位置: L949-951
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.hasSuggestedMlTabs()
- 位置: L953-955
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.openEditModal()
- 位置: L957-979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `this.#getGroupLinks()`, `this.#maybeDisableOrHideSaveButton()`, `this.#maybeUpdateLayoutForNova()`, `this.#panel.openPopup()`

## MozTabbrowserTabGroupMenu.#maybeUpdateLayoutForNova()
- 位置: L981-991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (isNovaEnabled)` → `this.#nameContainer.before()`
- 条件付き依存: `if (!(isNovaEnabled))` → `this.#tabGroupPropertiesActions.prepend()`
- XPCOM: `Services.prefs`

## MozTabbrowserTabGroupMenu.#maybeDisableOrHideSaveButton()
- 位置: L993-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Promise.allSettled()`, `Promise.allSettled(flushes).then()`, `TabStateFlusher.flush()`, `document.getElementById()`, `flushes.push()`, `this.activeGroup.tabs.forEach()`
- 条件付き依存: `if (this.activeGroup?.tabs)` → `SessionStore.shouldSaveTabsToGroup()`

## MozTabbrowserTabGroupMenu.close()
- 位置: L1017-1022
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel.hidePopup()`

## MozTabbrowserTabGroupMenu.on_popupshown()
- 位置: L1024-1044
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `["http", "https"].includes()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `this.#nameField.focus()`, `this.activeGroup?.tabs.some()`

## MozTabbrowserTabGroupMenu.on_popuphidden()
- 位置: L1046-1075
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#smartTabGroupingManager?.terminateProcess()`
- 条件付き依存: `if (this.#keepNewlyCreatedGroup)` → `this.dispatchEvent()`
- 条件付き依存: `if ( this.smartTabGroupsEnabled && this.smartTabGroupsOptin && (this.#suggestedMlLabel !== null || this.#hasSuggestedMlTabs) )` → `this.#handleMlTelemetry()`
- 条件付き依存: `if (!(this.#keepNewlyCreatedGroup))` → `this.activeGroup.ungroupTabs()`
- 条件付き依存: `if (!(this.#keepNewlyCreatedGroup))` → `TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (this.#nameField.disabled)` → `this.#setFormToDisabled()`
- 条件付き依存: `if (this.activeGroup?.label != this.#initialTabGroupName)` → `Glean.tabgroup.groupInteractions.rename.add()`

## MozTabbrowserTabGroupMenu.on_keypress()
- 位置: L1077-1098
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.close()`
- 条件付き依存: `if ( event.target.localName != "toolbarbutton" && event.target.localName != "moz-button" )` → `this.close()`

## MozTabbrowserTabGroupMenu.on_change()
- 位置: L1103-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.activeGroup)` → `Glean.tabgroup.groupInteractions.change_color.add()`

## MozTabbrowserTabGroupMenu.#handleNewTabInGroup()
- 位置: async L1113-1128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.addAdjacentNewTab()`, `this.activeGroup?.tabs.at()`, `window.addEventListener()`, `window.focus()`

## onTabOpened()
- 位置: async L1115-1119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.activeGroup?.addTabs()`, `this.close()`, `window.removeEventListener()`

## MozTabbrowserTabGroupMenu.#getGroupLinks()
- 位置: L1134-1147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUtils.getShareableURL()`
- 条件付き依存: `if (shareableURL)` → `links.push()`
- 条件付き依存: `if (shareableURL)` → `gURLBar.makeURIReadable()`

## MozTabbrowserTabGroupMenu.suggestionState()
- 位置: L1152-1158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#renderSuggestionState()`

## MozTabbrowserTabGroupMenu.#handleLoadSuggestionsCancel()
- 位置: L1160-1166
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.#handleSelectAll()
- 位置: L1168-1176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelectorAll()`, `document .querySelectorAll(".tab-group-suggestion-checkbox") .forEach()`

## MozTabbrowserTabGroupMenu.#handleDeselectAll()
- 位置: L1178-1185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document .querySelectorAll()`, `document .querySelectorAll(".tab-group-suggestion-checkbox") .forEach()`

## MozTabbrowserTabGroupMenu.#setFormToDisabled()
- 位置: L1192-1206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `swatches.forEach()`, `this.#swatchesContainer.querySelectorAll()`, `this.#tabGroupMain.querySelectorAll()`, `toolbarButtons.forEach()`

## MozTabbrowserTabGroupMenu.#handleFirstDownloadAndSuggest()
- 位置: async L1208-1238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `this.#handleMLOptinTelemetry()`, `this.#handleSmartSuggest()`, `this.#initMlGroupLabel()`, `this.#setFormToDisabled()`, `this.#smartTabGroupingManager.preloadAllModels()`

## MozTabbrowserTabGroupMenu.#handleSmartSuggest()
- 位置: async L1240-1280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `tabs.forEach()`, `this.#createRow()`, `this.#smartTabGroupingManager.smartTabGroupingForGroup()`
- 条件付き依存: `if (!this.#createMode)` → `this.#handleMlTelemetry()`

## MozTabbrowserTabGroupMenu.#handleMlTelemetry()
- 位置: L1287-1314
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#suggestedMlLabel !== null)` → `this.#smartTabGroupingManager.handleLabelTelemetry()`
- 条件付き依存: `if (this.#hasSuggestedMlTabs)` → `this.#smartTabGroupingManager.handleSuggestTelemetry()`

## MozTabbrowserTabGroupMenu.#handleMLOptinTelemetry()
- 位置: L1321-1325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.smartTabOptin.record()`

## MozTabbrowserTabGroupMenu.#createRow()
- 位置: L1327-1349
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkbox.addEventListener()`, `checkbox.classList.add()`, `document.createElement()`, `this.#suggestions.appendChild()`
- 条件付き依存: `if (e.target.checked)` → `this.#selectedSuggestedTabs.push()`
- 条件付き依存: `if (!(e.target.checked))` → `this.#selectedSuggestedTabs.filter()`

## MozTabbrowserTabGroupMenu.#setElementVisibility()
- 位置: L1358-1363
- 役割: (未記入)
- 触るとき: (未記入)

## MozTabbrowserTabGroupMenu.#showDefaultTabGroupActions()
- 位置: L1365-1367
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#showSmartSuggestionsContainer()
- 位置: L1369-1371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#showSuggestionButton()
- 位置: L1373-1375
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#showSuggestionMessageContainer()
- 位置: L1377-1379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#showSuggestionsSeparator()
- 位置: L1381-1383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#setLoadingState()
- 位置: L1385-1388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#setSuggestionsButtonCreateModeState()
- 位置: L1390-1396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#suggestionButton.setAttribute()`

## MozTabbrowserTabGroupMenu.#setSuggestModeSuggestionState()
- 位置: L1404-1410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panel.classList.toggle()`, `this.#setElementVisibility()`

## MozTabbrowserTabGroupMenu.#resetCommonUI()
- 位置: L1412-1428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setLoadingState()`, `this.#setSuggestModeSuggestionState()`, `this.#showSmartSuggestionsContainer()`
- 条件付き依存: `if (this.#suggestions)` → `this.#suggestions.replaceChildren()`
- 条件付き依存: `if (this.#suggestionsOptinContainer)` → `this.#suggestionsOptinContainer.replaceChildren()`

## MozTabbrowserTabGroupMenu.#renderSuggestionState()
- 位置: L1430-1544
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#resetCommonUI()`, `this.#setLoadingState()`, `this.#setSuggestModeSuggestionState()`, `this.#setSuggestionsButtonCreateModeState()`, `this.#showDefaultTabGroupActions()`, `this.#showSmartSuggestionsContainer()`, `this.#showSuggestionButton()`, `this.#showSuggestionMessageContainer()`, `this.#showSuggestionsSeparator()`
