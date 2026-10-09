# browser/components/aiwindow/ui/modules/AutoTabGroupingSuggestions.sys.mjs

source: browser/components/aiwindow/ui/modules/AutoTabGroupingSuggestions.sys.mjs
source-hash: 757b543529c54ba534da08d33abb06e5bb6cd9b3
lines: 432

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`, `console.createInstance()`, `parseFloat()`

## normalizeLabel()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `label.trim()`, `label.trim().toLocaleLowerCase()`

## isAvailable()
- 位置: L145-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `lazy.SmartTabGroupingManager.isAllowed`, `this.hasEnoughMemory`
- XPCOM: `Services.prefs`

## hasEnoughMemory()
- 位置: L159-165
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.checkForMemory`, `lazy.minimumPhysicalMemoryGiB`, `lazy.mlUtils.totalPhysicalMemory`

## manager()
- 位置: L167-175
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this._manager)` → `structuredClone()`
- 参照: `config.topicGeneration.engineId`, `config.topicGeneration.featureId`, `lazy.SMART_TAB_GROUPING_CONFIG`, `lazy.SmartTabGroupingManager`, `this._manager`

## preloadModels()
- 位置: L189-197
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!lazy.preloadEnabled || !this.isAvailable)` → `Promise.resolve()`
- 条件付き依存: `if (!this._preloadPromise)` → `this._preloadModels()`
- 参照: `lazy.preloadEnabled`, `this._preloadPromise`, `this.isAvailable`

## _preloadModels()
- 位置: async L199-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.warn()`, `this.manager.preloadAllModels()`

## getCandidateTabs()
- 位置: L215-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `tab.hasAttribute()`, `uri.schemeIs()`, `win.gBrowser.tabs.filter()`
- 参照: `tab.closing`, `tab.group`, `tab.hidden`, `tab.label`, `tab.linkedBrowser?.currentURI`, `tab.pinned`

## buildProposals()
- 位置: async L238-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `candidates.filter()`, `clusters.flatMap()`, `clusters.map()`, `groupedTabs.has()`, `label?.trim()`, `labeled .filter()`, `labeled .filter(proposal => proposal.label) .map()`, `lazy.console.warn()`, `takenLabels.map()`, `this._labelForGroup()`, `this.manager.generateClusters()`, `this.selectClusters()`, `this.uniqueLabel()`
- 参照: `c.tabs`, `cluster.tabs`, `clusters.length`, `proposal.label`, `result?.clusterRepresentations`

## uniqueLabel()
- 位置: L278-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalizeLabel()`, `taken.add()`, `taken.has()`

## _labelForGroup()
- 位置: async L294-316
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.console.warn()`, `tabs .map()`, `tabs .map(t => t.linkedBrowser?.currentURI?.spec ?? "") .sort()`, `tabs .map(t => t.linkedBrowser?.currentURI?.spec ?? "") .sort() .join()`, `this._labelCache.has()`, `this._labelCache.set()`, `this._llmLabelForGroup()`, `this.manager.getPredictedLabelForGroup()`
- 条件付き依存: `if (this._labelCache.has(key))` → `this._labelCache.get()`
- 条件付き依存: `if (this._labelCache.size >= MAX_LABEL_CACHE_ENTRIES)` → `this._labelCache.delete()`
- 条件付き依存: `if (this._labelCache.size >= MAX_LABEL_CACHE_ENTRIES)` → `this._labelCache.keys().next()`
- 条件付き依存: `if (this._labelCache.size >= MAX_LABEL_CACHE_ENTRIES)` → `this._labelCache.keys()`
- 参照: `t.linkedBrowser?.currentURI?.spec`, `this._labelCache.keys().next().value`, `this._labelCache.size`

## _llmLabelForGroup()
- 位置: async L320-358
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `label.replace()`, `label.replace(/\s+(and|or|&)$/i, "").trim()`, `lazy.buildConversation()`, `lazy.loadPrompt()`, `lazy.openAIEngine.getFxAccountToken()`, `lazy.renderPrompt()`, `lazy.sanitizeUntrustedContent()`, `lazy.sanitizeUntrustedContent(raw, true).trim()`, `response?.finalOutput?.trim()`, `tabs .slice()`, `tabs .slice(0, MAX_LABEL_TABS) .map()`, `tabs .slice(0, MAX_LABEL_TABS) .map(tab => lazy.sanitizeUntrustedContent(tab.label || "")) .filter()`, `tabs .slice(0, MAX_LABEL_TABS) .map(tab => lazy.sanitizeUntrustedContent(tab.label || "")) .filter(Boolean) .join()`
- 条件付き依存: `if (label.length > MAX_LABEL_LENGTH)` → `label.slice()`
- 条件付き依存: `if (label.length > MAX_LABEL_LENGTH)` → `cut.lastIndexOf()`
- 条件付き依存: `if (label.length > MAX_LABEL_LENGTH)` → `cut.slice()`
- 参照: `conversation.engine.model`, `label.length`, `lazy.MODEL_FEATURES.TAB_GROUP_NAMING`, `tab.label`

## selectClusters()
- 位置: L368-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clusterRepresentations .filter()`
- 参照: `a.tabs.length`, `b.tabs.length`, `c.cohesion`, `c.tabs`, `c.tabs.length`, `clusterRepresentations?.length`, `lazy.maxGroups`, `lazy.minCohesion`, `lazy.minTabsPerGroup`

## toSuggestionData()
- 位置: L392-399
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `proposal.tabs.map()`, `this.toTabInfo()`
- 参照: `TAB_GROUP_COLORS.length`, `proposal.label`, `proposal.tabs`

## toTabInfo()
- 位置: L407-421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._faviconUrl()`
- 条件付き依存: `if (uri)` → `lazy.BrowserUtils.formatURIForDisplay()`
- 参照: `tab.label`, `tab.linkedBrowser?.currentURI`

## _faviconUrl()
- 位置: L423-430
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `icon.startsWith()`
- 参照: `tab.linkedBrowser?.currentURI`, `tab.linkedBrowser?.mIconURL`, `uri.spec`
