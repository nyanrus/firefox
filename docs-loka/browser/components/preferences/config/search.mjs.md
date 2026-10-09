# browser/components/preferences/config/search.mjs

source: browser/components/preferences/config/search.mjs
source-hash: abaf8c5c4e52d8767015e35246b0d415cd536931
lines: 1289

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Preferences.addAll()`, `Preferences.addSetting()`, `SettingGroupManager.registerGroups()`, `XPCOMUtils.declareLazy()`, `createSearchEngineConfig()`

## getEngineIcon()
- 位置: async L77-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.getIconURL()`
- 参照: `window.devicePixelRatio`

## createSearchEngineConfig()
- 位置: L102-162
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Preferences.AsyncSetting`

## get()
- 位置: async L109-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getEngine()`
- 参照: `engine?.id`

## set()
- 位置: async L115-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setEngine()`

## getControlConfig()
- 位置: async L119-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.allSettled()`, `engines.map()`, `getEngineIcon()`, `lazy.SearchService.getVisibleEngines()`, `optionsInfo .filter()`, `optionsInfo .filter(o => o.status == "fulfilled") .map()`
- 参照: `engine.id`, `engine.name`, `o.status`, `o.value`

## setup()
- 位置: L140-147
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`
- XPCOM: `Services.obs`

## observe()
- 位置: L154-160
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic == lazy.SearchUtils.TOPIC_ENGINE_MODIFIED)` → `this.emitChange()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`

## getEngine()
- 位置: async L167-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getDefault()`

## setEngine()
- 位置: async L174-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.SearchService.setDefault()`
- 参照: `lazy.SearchService.CHANGE_REASON.USER`

## visible()
- 位置: L206-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`
- 参照: `scotchBonnetEnabled.value`, `showSearchTermsFeatureGate.value`

## setup()
- 位置: L212-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.addListener()`, `lazy.CustomizableUI.removeListener()`

## onWidgetAfterDOMChange()
- 位置: L217-221
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node.id == "search-container")` → `onChange()`
- 参照: `node.id`

## visible()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `separatePrivateDefaultUI.value`

## getEngine()
- 位置: async L245-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getDefaultPrivate()`

## setEngine()
- 位置: async L252-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineById()`, `lazy.SearchService.setDefaultPrivate()`
- 参照: `lazy.SearchService.CHANGE_REASON.USER`

## get()
- 位置: L295-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`
- 参照: `deps.searchSuggestionsEnabledPref.value`, `deps.urlbarSuggestionsEnabledPref.value`

## set()
- 位置: L303-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`
- 参照: `deps.searchSuggestionsEnabledPref.value`, `deps.urlbarSuggestionsEnabledPref.value`

## get()
- 位置: L322-333
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`
- 参照: `deps.suggestionsInSearchFieldsCheckbox.value`, `deps.urlbarSuggestionsEnabledPref.value`

## set()
- 位置: L334-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`
- 参照: `deps.suggestionsInSearchFieldsCheckbox.value`, `deps.urlbarSuggestionsEnabledPref.value`, `setting.disabled`

## setup()
- 位置: L347-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.addListener()`, `lazy.CustomizableUI.removeListener()`

## onWidgetAfterDOMChange()
- 位置: L352-356
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node.id == "search-container")` → `onChange()`
- 参照: `node.id`

## disabled()
- 位置: L361-366
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.permanentPBEnabledPref.value`, `deps.searchSuggestionsEnabledPref.value`

## visible()
- 位置: L367-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CustomizableUI.getPlacementOfWidget()`

## get()
- 位置: L383-388
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.searchSuggestionsEnabledPref.value`, `deps.urlbarSuggestionsEnabledPref.value`

## disabled()
- 位置: L389-395
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.permanentPBEnabledPref.value`, `deps.suggestionsInSearchFieldsCheckbox.value`, `deps.urlbarSuggestionsEnabledPref.value`

## disabled()
- 位置: L402-404
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.searchSuggestionsEnabledPref.value`

## visible()
- 位置: L417-417
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.trendingFeaturegatePref.value`

## disabled()
- 位置: L418-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.defaultEngine?.supportsResponseType()`
- 参照: `deps.permanentPBEnabledPref.value`, `deps.searchSuggestionsEnabledPref.value`, `lazy.SearchUtils.URL_TYPE.TRENDING_JSON`

## visible()
- 位置: L434-438
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.permanentPBEnabledPref.value`, `deps.urlBarSuggestionCheckbox.visible`

## setup()
- 位置: L453-456
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.NimbusFeatures.urlbar.offUpdate()`, `window.NimbusFeatures.urlbar.onUpdate()`

## getControlConfig()
- 位置: L466-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.SETTINGS_UI.NONE`

## visible()
- 位置: L498-500
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.clipboardFeaturegate.value`

## visible()
- 位置: L522-524
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.enableRecentSearchesFeatureGate.value`

## visible()
- 位置: L541-543
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.quickActionsShowPrefs.value`, `deps.scotchBonnetEnabled.value`

## determineSuggestionSettingsVisibility()
- 位置: L546-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!lazy.UrlbarPrefs.get("quickSuggestEnabled")))` → `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.SETTINGS_UI.NONE`

## disabled()
- 位置: L579-581
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.firefoxSuggestAll.value`

## visible()
- 位置: L593-606
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!(!lazy.UrlbarPrefs.get("quickSuggestEnabled")))` → `lazy.UrlbarPrefs.get()`
- 参照: `lazy.QuickSuggest.SETTINGS_UI.FULL`, `lazy.QuickSuggest.SETTINGS_UI.NONE`

## disabled()
- 位置: L607-609
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `deps.firefoxSuggestAll.value`

## setup()
- 位置: L615-626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `this.emitChange`
- XPCOM: `Services.obs`

## disabled()
- 位置: async L627-629
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.canClearDismissedSuggestions()`

## onUserClick()
- 位置: L630-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.QuickSuggest.clearDismissedSuggestions()`

## setup()
- 位置: L657-667
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._emitChange`

## searchEngineUpdateNotifier()
- 位置: L659-662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `emitChange()`
- 参照: `this._engineUpdateTriggered`

## onMessageBarDismiss()
- 位置: L668-672
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `this._emitChange()`
- 参照: `this._engineUpdateTriggered`

## visible()
- 位置: L673-675
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._engineUpdateTriggered`

## EngineListItemSetting()
- 位置: L686-727
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Preferences.AsyncSetting`

## setup()
- 位置: L690-711
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`
- XPCOM: `Services.obs`

## onTargetEngineChanged()
- 位置: L692-700
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (data == lazy.SearchUtils.MODIFIED_TYPE.CHANGED || data == lazy.SearchUtils.MODIFIED_TYPE.ICON_CHANGED) && subject.wrappedJSObject == engine )` → `this.emitChange()`
- 参照: `lazy.SearchUtils.MODIFIED_TYPE.CHANGED`, `lazy.SearchUtils.MODIFIED_TYPE.ICON_CHANGED`, `subject.wrappedJSObject`

## getControlConfig()
- 位置: async L713-725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.aliases.join()`, `getEngineIcon()`
- 参照: `engine.hidden`, `engine.name`

## visible()
- 位置: L731-733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- XPCOM: `Services.policies`

## onUserClick()
- 位置: L734-740
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`

## maybeMakeSetting()
- 位置: L746-750
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.getSetting()`
- 条件付き依存: `if (!Preferences.getSetting(config.id))` → `Preferences.addSetting()`
- 参照: `config.id`

## ToggleSetting()
- 位置: L760-792
- 役割: (未記入)
- 触るとき: (未記入)

## setup()
- 位置: L763-784
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 参照: `lazy.SearchUtils.TOPIC_ENGINE_MODIFIED`
- XPCOM: `Services.obs`

## onTargetEngineChanged()
- 位置: L765-773
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( (data == lazy.SearchUtils.MODIFIED_TYPE.CHANGED || data == lazy.SearchUtils.MODIFIED_TYPE.ICON_CHANGED) && subject.wrappedJSObject == engine )` → `emitChange()`
- 参照: `lazy.SearchUtils.MODIFIED_TYPE.CHANGED`, `lazy.SearchUtils.MODIFIED_TYPE.ICON_CHANGED`, `subject.wrappedJSObject`

## get()
- 位置: L785-787
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `engine.hidden`

## onUserChange()
- 位置: L788-790
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `engine.hidden`

## setup()
- 位置: L812-832
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (Services.policies?.status == Ci.nsIEnterprisePolicies.ACTIVE)` → `Services.policies.getActivePolicies()`
- 参照: `Ci.nsIEnterprisePolicies.ACTIVE`, `Services.policies?.status`, `activePolicies.SearchEngines?.Remove`, `this.#enterpriseDisabledEngineNames`, `this.emitChange`
- XPCOM: [`nsIEnterprisePolicies`](../../../../toolkit/components/enterprisepolicies/nsIEnterprisePolicies.idl.md) / `Services.obs` / `Services.policies`

## getL10nNames()
- 位置: async L837-878
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `document.l10n.formatValues()`, `englishSearchStrings.formatValues()`, `getIDs()`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.forEach()`, `this.#localShortcutL10nNames?.set()`
- 参照: `this.#localShortcutL10nNames`

## getIDs()
- 位置: L843-847
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.LOCAL_SEARCH_MODES.map()`, `lazy.UrlbarShared.getResultSourceName()`
- 参照: `mode.source`

## handleDeletionOptions()
- 位置: L886-944
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (engine instanceof lazy.ConfigSearchEngine)` → `maybeMakeSetting()`
- 条件付き依存: `if (engine instanceof lazy.ConfigSearchEngine)` → `ToggleSetting()`
- 条件付き依存: `if (!(engine instanceof lazy.ConfigSearchEngine))` → `maybeMakeSetting()`
- 参照: `engine.id`, `lazy.ConfigSearchEngine`

## onUserClick()
- 位置: async L903-931
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmExBC()`, `document.l10n.formatValues()`
- 条件付き依存: `if (button == 0)` → `lazy.SearchService.removeEngine()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_CONTENT`, `lazy.SearchService.CHANGE_REASON.USER`, `window.browsingContext`
- XPCOM: `Services.prompt`

## makeEngineList()
- 位置: async L950-1031
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `EngineListItemSetting()`, `configs.push()`, `lazy.SearchService.getEngines()`, `maybeMakeSetting()`, `this.#enterpriseDisabledEngineNames?.has()`
- 条件付き依存: `if (!(engine instanceof lazy.AddonSearchEngine))` → `config.items.push()`
- 条件付き依存: `if (!(engine instanceof lazy.AddonSearchEngine))` → `this.handleDeletionOptions()`
- 条件付き依存: `if (!(!(engine instanceof lazy.AddonSearchEngine)))` → `maybeMakeSetting()`
- 条件付き依存: `if (!(!(engine instanceof lazy.AddonSearchEngine)))` → `config.items.push()`
- 参照: `engine.id`, `engine.name`, `lazy.AddonSearchEngine`

## disabled()
- 位置: L968-968
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `engine.hidden`

## onUserClick()
- 位置: L969-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSubDialog.open()`

## closingCallback()
- 位置: L975-979
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.detail.button == "accept")` → `searchEngineUpdateNotifier()`
- 参照: `event.detail.button`

## onUserClick()
- 位置: L1009-1015
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `window.browsingContext.topChromeWindow.BrowserAddonUI.manageAddon()`
- 参照: `engine.extensionID`

## makeSearchModesList()
- 位置: async L1037-1073
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `configs.push()`, `keyword.toLowerCase()`, `l10nNames.get()`, `maybeMakeSetting()`, `names .map()`, `names .map(keyword => `@${keyword.toLowerCase()}`) .join()`, `this.getL10nNames()`
- 参照: `lazy.UrlbarShared.LOCAL_SEARCH_MODES`, `searchMode.icon`, `searchMode.restrict`, `searchMode.source`, `searchMode.telemetryLabel`

## onUserReorder()
- 位置: async L1076-1088
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `lazy.SearchService.moveEngine()`
- 参照: `draggedElement.label`, `event.detail`, `this.#enterpriseDisabledEngineNames`

## getControlConfig()
- 位置: async L1089-1097
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.makeEngineList()`, `this.makeSearchModesList()`
