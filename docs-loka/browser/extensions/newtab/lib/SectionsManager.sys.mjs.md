# browser/extensions/newtab/lib/SectionsManager.sys.mjs

source: browser/extensions/newtab/lib/SectionsManager.sys.mjs
source-hash: 0efb66b79fa580f684efeeddcc31eb04bd6e7feb
lines: 570

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `EventEmitter.decorate()`

## BUILT_IN_SECTIONS()
- 位置: L35-85
- 役割: (未記入)
- 触るとき: (未記入)

## "feeds.section.topstories"()
- 位置: L36-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `options.provider_icon`

## "feeds.section.highlights"()
- 位置: L69-84
- 役割: (未記入)
- 触るとき: (未記入)

## init()
- 位置: async L129-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BUILT_IN_SECTIONS()`, `Object.keys()`, `Object.keys(this.CONTEXT_MENU_PREFS).forEach()`, `Services.prefs.addObserver()`, `lazy.NimbusFeatures.newtab.getAllVariables()`, `lazy.NimbusFeatures.pocketNewtab.getAllVariables()`, `this.addBuiltInSection()`, `this.emit()`, `this.sections.forEach()`
- 条件付き依存: `if (section.dedupeFrom)` → `this._dedupeConfiguration.push()`
- 参照: `section.dedupeFrom`, `section.id`, `this.CONTEXT_MENU_PREFS`, `this.INIT`, `this._dedupeConfiguration`, `this.initialized`
- XPCOM: `Services.prefs`

## observe()
- 位置: L157-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 条件付き依存: `if (data === this.CONTEXT_MENU_PREFS[pref])` → `this.updateSections()`
- 参照: `this.CONTEXT_MENU_PREFS`

## addBuiltInSection()
- 位置: async L168-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BUILT_IN_SECTIONS()`, `BUILT_IN_SECTIONS(featureConfig)[feedPrefName]()`, `JSON.parse()`, `Object.assign()`, `console.error()`, `lazy.NimbusFeatures.newtab.getAllVariables()`, `lazy.NimbusFeatures.pocketNewtab.getAllVariables()`, `this.addSection()`
- 参照: `defaultSection.pref`, `section.id`, `section.pref.feed`

## addSection()
- 位置: L189-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.sections.set()`, `this.updateLinkMenuOptions()`
- 参照: `this.ADD_SECTION`

## removeSection()
- 位置: L194-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.sections.delete()`
- 参照: `this.REMOVE_SECTION`

## enableSection()
- 位置: L198-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.updateSection()`
- 参照: `this.ENABLE_SECTION`

## disableSection()
- 位置: L202-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.emit()`, `this.updateSection()`
- 参照: `this.DISABLE_SECTION`

## updateSections()
- 位置: L210-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sections.forEach()`, `this.updateSection()`

## updateSection()
- 位置: L215-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sections.has()`, `this.updateLinkMenuOptions()`
- 条件付き依存: `if (this.sections.has(id))` → `Object.assign()`
- 条件付き依存: `if (this.sections.has(id))` → `this.sections.set()`
- 条件付き依存: `if (this.sections.has(id))` → `this.sections.get()`
- 条件付き依存: `if (this.sections.has(id))` → `this.emit()`
- 参照: `this.UPDATE_SECTION`, `this._dedupeConfiguration`

## updateBookmarkMetadata()
- 位置: L235-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sections.forEach()`
- 条件付き依存: `if (section.rows)` → `section.rows.forEach()`
- 条件付き依存: `if ( card.url === url && card.description && card.title && card.image )` → `lazy.PlacesUtils.history.update()`
- 条件付き依存: `if ( card.url === url && card.description && card.title && card.image )` → `lazy.PlacesUtils.history.insert()`
- 参照: `card.description`, `card.image`, `card.title`, `card.url`, `section.rows`

## updateLinkMenuOptions()
- 位置: L275-290
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options.availableLinkMenuOptions)` → `options.availableLinkMenuOptions.filter()`
- 条件付き依存: `if (options.availableLinkMenuOptions)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (options.rows && id === "highlights")` → `this._addCardTypeLinkMenuOptions()`
- 参照: `options.availableLinkMenuOptions`, `options.contextMenuOptions`, `options.rows`, `this.CONTEXT_MENU_PREFS`
- XPCOM: `Services.prefs`

## _addCardTypeLinkMenuOptions()
- 位置: L298-318
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.CONTEXT_MENU_OPTIONS_FOR_HIGHLIGHT_TYPES[card.type])` → `console.error()`
- 条件付き依存: `if (!(!this.CONTEXT_MENU_OPTIONS_FOR_HIGHLIGHT_TYPES[card.type]))` → `card.contextMenuOptions.filter()`
- 条件付き依存: `if (!(!this.CONTEXT_MENU_OPTIONS_FOR_HIGHLIGHT_TYPES[card.type]))` → `Services.prefs.getBoolPref()`
- 参照: `card.contextMenuOptions`, `card.type`, `this.CONTEXT_MENU_OPTIONS_FOR_HIGHLIGHT_TYPES`, `this.CONTEXT_MENU_PREFS`
- XPCOM: `Services.prefs`

## updateSectionCard()
- 位置: L331-346
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sections.has()`
- 条件付き依存: `if (this.sections.has(id))` → `this.sections.get(id).rows.find()`
- 条件付き依存: `if (this.sections.has(id))` → `this.sections.get()`
- 条件付き依存: `if (card)` → `Object.assign()`
- 条件付き依存: `if (this.sections.has(id))` → `this.emit()`
- 参照: `elem.url`, `this.UPDATE_SECTION_CARD`

## removeSectionCard()
- 位置: L347-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sections .get()`, `this.sections .get(sectionId) .rows.filter()`, `this.sections.has()`, `this.updateSection()`
- 参照: `row.url`

## onceInitialized()
- 位置: L356-362
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.initialized)` → `callback()`
- 条件付き依存: `if (!(this.initialized))` → `this.once()`
- 参照: `this.INIT`, `this.initialized`

## uninit()
- 位置: L363-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(this.CONTEXT_MENU_PREFS).forEach()`, `Services.prefs.removeObserver()`
- 参照: `SectionsManager.initialized`, `this.CONTEXT_MENU_PREFS`
- XPCOM: `Services.prefs`

## SectionsFeed.constructor()
- 位置: L391-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init.bind()`, `this.onAddSection.bind()`, `this.onRemoveSection.bind()`, `this.onUpdateSection.bind()`, `this.onUpdateSectionCard.bind()`
- 参照: `this.init`, `this.onAddSection`, `this.onRemoveSection`, `this.onUpdateSection`, `this.onUpdateSectionCard`

## SectionsFeed.init()
- 位置: L399-416
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.on()`, `SectionsManager.sections.forEach()`, `this.onAddSection()`
- 参照: `SectionsManager.ADD_SECTION`, `SectionsManager.REMOVE_SECTION`, `SectionsManager.UPDATE_SECTION`, `SectionsManager.UPDATE_SECTION_CARD`, `this.onAddSection`, `this.onRemoveSection`, `this.onUpdateSection`, `this.onUpdateSectionCard`

## SectionsFeed.uninit()
- 位置: L418-428
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.emit()`, `SectionsManager.off()`, `SectionsManager.uninit()`
- 参照: `SectionsManager.ADD_SECTION`, `SectionsManager.REMOVE_SECTION`, `SectionsManager.UNINIT`, `SectionsManager.UPDATE_SECTION`, `SectionsManager.UPDATE_SECTION_CARD`, `this.onAddSection`, `this.onRemoveSection`, `this.onUpdateSection`, `this.onUpdateSectionCard`

## SectionsFeed.onAddSection()
- 位置: L430-451
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options)` → `this.store.dispatch()`
- 条件付き依存: `if (options)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (options)` → `Object.assign()`
- 条件付き依存: `if (options)` → `orderedSections.includes()`
- 条件付き依存: `if (!orderedSections.includes(id))` → `orderedSections.unshift()`
- 条件付き依存: `if (!orderedSections.includes(id))` → `this.store.dispatch()`
- 条件付き依存: `if (!orderedSections.includes(id))` → `ac.SetPref()`
- 条件付き依存: `if (!orderedSections.includes(id))` → `orderedSections.join()`
- 参照: `at.SECTION_REGISTER`, `this.orderedSectionIds`

## SectionsFeed.onRemoveSection()
- 位置: L453-457
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.store.dispatch()`
- 参照: `at.SECTION_DEREGISTER`

## SectionsFeed.onUpdateSection()
- 位置: L459-480
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options)` → `Object.assign()`
- 条件付き依存: `if (options)` → `this.store.dispatch()`
- 条件付き依存: `if (options)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (options)` → `ac.AlsoToPreloaded()`
- 参照: `at.SECTION_UPDATE`

## SectionsFeed.onUpdateSectionCard()
- 位置: L482-504
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options)` → `this.store.dispatch()`
- 条件付き依存: `if (options)` → `ac.BroadcastToContent()`
- 条件付き依存: `if (options)` → `ac.AlsoToPreloaded()`
- 参照: `at.SECTION_UPDATE_CARD`

## SectionsFeed.orderedSectionIds()
- 位置: L506-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`, `this.store.getState().Prefs.values.sectionOrder.split()`

## SectionsFeed.onAction()
- 位置: async L510-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SectionsManager.ACTIONS_TO_PROXY.includes()`, `SectionsManager.disableSection()`, `SectionsManager.enableSection()`, `SectionsManager.init()`, `SectionsManager.onceInitialized()`, `SectionsManager.updateBookmarkMetadata()`, `this.uninit()`
- 条件付き依存: `if (action.data)` → `action.data.name.match()`
- 条件付き依存: `if (matched)` → `SectionsManager.addBuiltInSection()`
- 条件付き依存: `if (matched)` → `this.store.dispatch()`
- 条件付き依存: `if (action.data)` → `SectionsManager.removeSectionCard()`
- 条件付き依存: `if ( SectionsManager.ACTIONS_TO_PROXY.includes(action.type) && SectionsManager.sections.size > 0 )` → `SectionsManager.emit()`
- 参照: `SectionsManager.ACTION_DISPATCHED`, `SectionsManager.sections.size`, `action.data`, `action.data.source`, `action.data.url`, `action.data.value`, `action.type`, `at.INIT`, `at.PLACES_BOOKMARK_ADDED`, `at.PREFS_INITIAL_VALUES`, `at.PREF_CHANGED`, `at.SECTION_DISABLE`, `at.SECTION_ENABLE`, `at.SECTION_OPTIONS_CHANGED`, `at.UNINIT`, `at.WEBEXT_DISMISS`, `this.init`
