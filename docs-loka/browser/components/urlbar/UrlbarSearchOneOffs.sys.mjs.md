# browser/components/urlbar/UrlbarSearchOneOffs.sys.mjs

source: browser/components/urlbar/UrlbarSearchOneOffs.sys.mjs
source-hash: 14414b803359093024f200d3dde57f89f3a81002
lines: 404

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## UrlbarSearchOneOffs.constructor()
- 位置: L29-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.addObserver()`, `super()`, `view.input.querySelector()`
- 参照: `this.disableOneOffsHorizontalKeyNavigation`, `this.input`, `this.view`, `view.input`

## UrlbarSearchOneOffs.localButtons()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSelectableButtons()`, `this.getSelectableButtons(false).filter()`
- 参照: `b.source`

## UrlbarSearchOneOffs.updateWebEngines()
- 位置: L51-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.invalidateCache()`
- 条件付き依存: `if (this.view.isOpen)` → `this._rebuild()`
- 参照: `this.view.isOpen`

## UrlbarSearchOneOffs.enable()
- 位置: L64-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if (this.view.isOpen)` → `this._rebuild()`
- 条件付き依存: `if (enable)` → `this.view.controller.addListener()`
- 条件付き依存: `if (!(enable))` → `this.view.controller.removeListener()`
- 参照: `this.style.display`, `this.telemetryOrigin`, `this.textbox`, `this.view.input.inputField`, `this.view.isOpen`

## UrlbarSearchOneOffs.onViewOpen()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._on_popupshowing()`

## UrlbarSearchOneOffs.onViewClose()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._on_popuphidden()`

## UrlbarSearchOneOffs.hasView()
- 位置: L102-107
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.container.hidden`, `this.style.display`

## UrlbarSearchOneOffs.isViewOpen()
- 位置: L113-115
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view.isOpen`

## UrlbarSearchOneOffs.selectedButton()
- 位置: L123-143
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.input.searchMode)` → `this.input.restoreSearchModeState()`
- 参照: `button.engine?.name`, `button.source`, `super.selectedButton`, `this.input.searchMode`, `this.selectedButton`, `this.view.oneOffSearchButtons.settingsButton`

## UrlbarSearchOneOffs.selectedButton()
- 位置: L145-147
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `super.selectedButton`

## UrlbarSearchOneOffs.selectedViewIndex()
- 位置: L154-156
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view.selectedRowIndex`

## UrlbarSearchOneOffs.selectedViewIndex()
- 位置: L157-159
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.view.selectedRowIndex`

## UrlbarSearchOneOffs.closeView()
- 位置: L164-168
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.view)` → `this.view.close()`
- 参照: `this.view`

## UrlbarSearchOneOffs.handleSearchCommand()
- 位置: L179-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `this._whereToOpen()`, `this.input.getAttribute()`, `this.input.select()`, `this.input.setSearchMode()`, `this.input.startQuery()`, `this.input.window.gBrowser.addTrustedTab()`, `this.selectedButton.classList.contains()`
- 条件付き依存: `if ( this.selectedButton == this.view.oneOffSearchButtons.settingsButton || this.selectedButton.classList.contains( "searchbar-engine-one-off-add-engine" ) )` → `this.input.controller.engagementEvent.discard()`
- 条件付き依存: `if ( this.selectedButton == this.view.oneOffSearchButtons.settingsButton || this.selectedButton.classList.contains( "searchbar-engine-one-off-add-engine" ) )` → `this.selectedButton.doCommand()`
- 条件付き依存: `if ( userTypedSearchString && engine && (event.shiftKey || where != "current") )` → `this.input.handleNavigation()`
- 条件付き依存: `if (!params?.inBackground)` → `newTab.documentGlobal.gURLBar.startQuery()`
- 参照: `event.shiftKey`, `lazy.UrlbarShared.RESULT_SOURCE.SEARCH`, `newTab.linkedBrowser`, `newTab.linkedBrowser.userTypedValue`, `params?.inBackground`, `searchMode.engineName`, `searchMode.isPreview`, `searchMode.source`, `this.input.searchMode`, `this.input.value`, `this.input.window.gBrowser.selectedTab`, `this.selectedButton`, `this.selectedButton.engine`, `this.view.oneOffSearchButtons.settingsButton`

## UrlbarSearchOneOffs.setTooltipForEngineButton()
- 位置: L270-284
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.document.l10n.setAttributes()`
- 条件付き依存: `if (!aliases.length)` → `super.setTooltipForEngineButton()`
- 参照: `aliases.length`, `button.engine.aliases`, `button.engine.name`

## UrlbarSearchOneOffs.willHide()
- 位置: async L293-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.getScotchBonnetPref()`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.some()`, `super.willHide()`
- 参照: `m.pref`

## UrlbarSearchOneOffs.onPrefChanged()
- 位置: L317-329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.LOCAL_SEARCH_MODES.map()`
- 条件付き依存: `if ( [ ...lazy.UrlbarShared.LOCAL_SEARCH_MODES.map(m => m.pref), "scotchBonnet.enableOverride", "scotchBonnet.disableOneOffs", ].includes(changedPref) )` → `this.invalidateCache()`
- 参照: `m.pref`

## UrlbarSearchOneOffs._rebuildEngineList()
- 位置: async L339-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.setAttribute()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarShared.getResultSourceName()`, `super._rebuildEngineList()`, `this.buttons.appendChild()`, `this.document.createXULElement()`, `this.document.l10n.setAttributes()`
- 参照: `button.id`, `button.source`, `lazy.UrlbarShared .LOCAL_SEARCH_MODES`

## UrlbarSearchOneOffs._on_click()
- 位置: L373-391
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleSearchCommand()`
- 参照: `button.engine`, `button.engine?.name`, `button.source`, `event.button`, `event.originalTarget`, `this.selectedButton`

## UrlbarSearchOneOffs._on_contextmenu()
- 位置: L399-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`
