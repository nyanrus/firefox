# browser/components/firefoxview/history.mjs

source: browser/components/firefoxview/history.mjs
source-hash: 6fdc996df2f1d8e8fedf9561c9b162694171fcd0
lines: 554

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## HistoryInView.constructor()
- 位置: L39-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._started`, `this.cumulativeSearches`, `this.fullyUpdated`, `this.maxTabsLength`, `this.profileAge`

## HistoryInView.start()
- 位置: L53-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.updateCache()`, `this.toggleVisibilityInCardContainer()`
- 参照: `this._started`

## HistoryInView.connectedCallback()
- 位置: async L64-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super.connectedCallback()`, `this.requestUpdate()`
- 条件付き依存: `if (!this.importHistoryDismissedPref && !this.hasImportedHistoryPrefs)` → `lazy.ProfileAge()`
- 条件付き依存: `if (!this.importHistoryDismissedPref && !this.hasImportedHistoryPrefs)` → `new Date().getTime()`
- 参照: `profileAccessor.created`, `this.hasImportedHistoryPrefs`, `this.importHistoryDismissedPref`, `this.profileAge`

## HistoryInView.stop()
- 位置: L95-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.toggleVisibilityInCardContainer()`
- 参照: `this._started`

## HistoryInView.disconnectedCallback()
- 位置: L104-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.disconnectedCallback()`, `this.migrationWizardDialog?.removeEventListener()`, `this.stop()`
- 参照: `this.migrationWizardDialog`

## HistoryInView.viewVisibleCallback()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.start()`

## HistoryInView.viewHiddenCallback()
- 位置: L117-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.stop()`

## HistoryInView.getUpdateComplete()
- 位置: async L137-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(this.cards).map()`, `Promise.all()`, `super.getUpdateComplete()`
- 参照: `card.updateComplete`, `this.cards`

## HistoryInView.onPrimaryAction()
- 位置: L142-153
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.historyVisits.record()`, `navigateToLink()`
- 条件付き依存: `if (this.controller.searchQuery)` → `Glean.firefoxview.cumulativeSearches.history.accumulateSingleSample()`
- 参照: `this.controller.searchQuery`, `this.cumulativeSearches`

## HistoryInView.forgetAboutThisSite()
- 位置: async L155-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `Services.io.newURI()`, `this.getWindow()`, `this.getWindow().gDialogBox.open()`, `this.recordContextMenuTelemetry()`
- 参照: `Services.io.newURI(this.triggerNode.url).host`, `this.triggerNode.url`
- XPCOM: `Services.eTLD` / `Services.io`

## HistoryInView.onSecondaryAction()
- 位置: L170-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.panelList.toggle()`
- 参照: `e.detail.originalEvent`, `e.originalTarget`, `this.triggerNode`

## HistoryInView.deleteFromHistory()
- 位置: L175-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.deleteFromHistory()`, `this.controller.deleteFromHistory().catch()`, `this.recordContextMenuTelemetry()`
- 参照: `console.error`

## HistoryInView.onChangeSortOption()
- 位置: L180-186
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.sortHistoryTabs.record()`, `this.controller.onChangeSortOption()`
- 参照: `this.controller.searchQuery`, `this.controller.sortOption`

## HistoryInView.onSearchQuery()
- 位置: L188-198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.controller.onSearchQuery()`
- 条件付き依存: `if (!this.recentBrowsing)` → `Glean.firefoxviewNext.searchInitiatedSearch.record()`
- 参照: `this.controller.searchQuery`, `this.cumulativeSearches`, `this.recentBrowsing`

## HistoryInView.showAllHistory()
- 位置: L200-206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.firefoxviewNext.showAllHistoryTabs.record()`, `this.getWindow()`, `this.getWindow().PlacesCommandHook.showPlacesOrganizer()`

## HistoryInView.openMigrationWizard()
- 位置: async L208-234
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customElements.whenDefined()`, `e.currentTarget.close()`, `migrationWizardDialog.firstElementChild.requestState()`, `migrationWizardDialog.showModal()`, `this.migrationWizardDialog.addEventListener()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `document.createElement()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `wizard.toggleAttribute()`
- 条件付き依存: `if (!migrationWizardDialog.firstElementChild)` → `migrationWizardDialog.appendChild()`
- 参照: `migrationWizardDialog.firstElementChild`, `migrationWizardDialog.open`, `this.migrationWizardDialog`

## HistoryInView.shouldShowImportBanner()
- 位置: L236-243
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.isAllowed()`
- 参照: `this.hasImportedHistoryPref`, `this.importHistoryDismissedPref`, `this.profileAge`
- XPCOM: `Services.policies`

## HistoryInView.dismissImportHistory()
- 位置: L245-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## HistoryInView.updated()
- 位置: L249-254
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.lists?.length)` → `this.toggleVisibilityInCardContainer()`
- 参照: `this.fullyUpdated`, `this.lists?.length`

## HistoryInView.panelListTemplate()
- 位置: L256-289
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `this.copyLink`, `this.deleteFromHistory`, `this.forgetAboutThisSite`, `this.openInNewPrivateWindow`, `this.openInNewWindow`

## HistoryInView.cardsTemplate()
- 位置: L294-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#emptyMessageTemplate()`
- 条件付き依存: `if (this.controller.searchResults)` → `this.#searchResultsTemplate()`
- 条件付き依存: `if (!this.controller.isHistoryEmpty)` → `this.#historyCardsTemplate()`
- 参照: `this.controller.isHistoryEmpty`, `this.controller.searchResults`

## HistoryInView.#historyCardsTemplate()
- 位置: L303-353
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `historyItem.l10nId.includes()`, `html()`, `ifDefined()`, `this.controller.historyVisits.map()`
- 参照: `historyItem.domain`, `historyItem.items`, `historyItem.items[0].time`, `historyItem.l10nId`, `this.controller.sortOption`, `this.maxTabsLength`, `this.onPrimaryAction`, `this.onSecondaryAction`

## HistoryInView.#emptyMessageTemplate()
- 位置: L355-403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `html()`
- 参照: `this.selectedTab`
- XPCOM: `Services.prefs`

## HistoryInView.#searchResultsTemplate()
- 位置: L405-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `escapeHtmlEntities()`, `html()`, `when()`
- 参照: `this.controller.searchQuery`, `this.controller.searchResults`, `this.controller.searchResults.length`, `this.onPrimaryAction`, `this.onSecondaryAction`

## HistoryInView.render()
- 位置: L440-547
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.panelListTemplate()`, `this.shouldShowImportBanner()`
- 参照: `this.cardsTemplate`, `this.controller.isHistoryEmpty`, `this.controller.searchResults`, `this.controller.sortOption`, `this.dismissImportHistory`, `this.onChangeSortOption`, `this.onSearchQuery`, `this.openMigrationWizard`, `this.selectedTab`, `this.showAllHistory`

## HistoryInView.willUpdate()
- 位置: L549-551
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.fullyUpdated`
