# browser/components/preferences/search.js

source: browser/components/preferences/search.js
source-hash: 019761b7765d69b29e0ebe7a5108dea4c1c560f2
lines: 1144

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`

## onUpdate()
- 位置: L24-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSearchPane._engineStore.notifyRebuildViews()`

## onUpdate()
- 位置: L29-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gSearchPane._engineStore.notifyRebuildViews()`

## init()
- 位置: L50-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.obs.removeObserver()`, `Services.policies.isAllowed()`, `initSettingGroup()`, `this._engineStore.init()`, `this._engineStore.init().catch()`, `window.addEventListener()`
- 条件付き依存: `if ( Services.policies && !Services.policies.isAllowed("installSearchEngine") )` → `document.getElementById()`
- 条件付き依存: `if (!( Services.policies && !Services.policies.isAllowed("installSearchEngine") ))` → `document.getElementById()`
- 条件付き依存: `if (!( Services.policies && !Services.policies.isAllowed("installSearchEngine") ))` → `addEnginesLink.setAttribute()`
- 参照: `Services.policies`, `console.error`, `document.getElementById("addEnginesBox").hidden`, `lazy.SearchUIUtils.searchEnginesURL`, `lazy.separatePrivateDefaultEnabledPrefValue`, `lazy.separatePrivateDefaultPrefValue`, `this._engineStore`
- XPCOM: `Services.obs` / `Services.policies`

## handleEvent()
- 位置: L84-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gEngineView.handleEvent()`
- 条件付き依存: `if (aEvent.target.parentNode.parentNode.id == "defaultEngine")` → `gSearchPane.setDefaultEngine()`
- 条件付き依存: `if ( aEvent.target.parentNode.parentNode.id == "defaultPrivateEngine" )` → `gSearchPane.setDefaultPrivateEngine()`
- 参照: `aEvent.target.id`, `aEvent.target.parentNode`, `aEvent.target.parentNode.parentNode`, `aEvent.target.parentNode.parentNode.id`, `aEvent.type`

## appLocalesChanged()
- 位置: async L108-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gEngineView.loadL10nNames()`
- 参照: `document.l10n.ready`

## observe()
- 位置: L116-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._engineStore.browserSearchEngineModified()`, `this.appLocalesChanged()`
- 参照: `subject.wrappedJSObject`

## showRestoreDefaults()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `document.getElementById("restoreDefaultSearchEngines").disabled`

## setDefaultEngine()
- 位置: async L136-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionSettingsStore.getSetting()`, `document.getElementById()`, `lazy.SearchService.setDefault()`
- 条件付き依存: `if (ExtensionSettingsStore.getSetting(SEARCH_TYPE, SEARCH_KEY) !== null)` → `ExtensionSettingsStore.select()`
- 参照: `ExtensionSettingsStore.SETTING_USER_SET`, `document.getElementById("defaultEngine").selectedItem.engine .originalEngine`, `lazy.SearchService.CHANGE_REASON.USER`

## setDefaultPrivateEngine()
- 位置: async L151-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `lazy.SearchService.setDefaultPrivate()`
- 参照: `document.getElementById("defaultPrivateEngine").selectedItem.engine .originalEngine`, `lazy.SearchService.CHANGE_REASON.USER`

## EngineStore.init()
- 位置: async L178-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engines.filter()`, `engines.some()`, `gSearchPane.showRestoreDefaults()`, `lazy.SearchService.getEngines()`, `this.addEngine()`, `this.notifyRowCountChanged()`
- 参照: `e.hidden`, `lazy.AppProvidedConfigEngine`, `visibleEngines.length`

## EngineStore.addListener()
- 位置: L197-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#listeners.push()`

## EngineStore.notifyRebuildViews()
- 位置: L205-213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `listener.rebuild()`
- 参照: `this.#listeners`, `this.engines`

## EngineStore.notifyRowCountChanged()
- 位置: L221-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener.rowCountChanged()`
- 参照: `this.#listeners`, `this.engines`

## EngineStore.notifyDefaultEngineChanged()
- 位置: L233-239
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("defaultEngineChanged" in listener)` → `listener.defaultEngineChanged()`
- 参照: `this.#listeners`, `this.engines`

## EngineStore.notifyEngineIconUpdated()
- 位置: L241-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getIndexForEngine()`
- 条件付き依存: `if (index != -1)` → `listener.engineIconUpdated()`
- 参照: `this.#listeners`, `this.engines`

## EngineStore._getIndexForEngine()
- 位置: L251-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engines.indexOf()`

## EngineStore._getEngineByName()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engines.find()`
- 参照: `engine.name`

## EngineStore._cloneEngine()
- 位置: L268-296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEngine.getIconURL()`, `aEngine.getIconURL().then()`, `this.notifyEngineIconUpdated()`
- 参照: `clonedObj.iconURL`, `clonedObj.isAddonEngine`, `clonedObj.isAppProvided`, `clonedObj.isUserEngine`, `clonedObj.originalEngine`, `lazy.AddonSearchEngine`, `lazy.AppProvidedConfigEngine`, `lazy.UserSearchEngine`, `window.devicePixelRatio`

## EngineStore._isSameEngine()
- 位置: L299-301
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `aEngineClone.originalEngine.id`, `this.originalEngine.id`

## EngineStore.addEngine()
- 位置: L303-305
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._cloneEngine()`, `this.engines.push()`

## EngineStore.updateEngine()
- 位置: L307-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.engines.findIndex()`
- 条件付き依存: `if (engineToUpdate != -1)` → `this._cloneEngine()`
- 参照: `e.originalEngine.id`, `newEngine.id`, `this.engines`

## EngineStore.moveEngine()
- 位置: L316-339
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.moveEngine()`, `this._getIndexForEngine()`, `this.engines.splice()`
- 条件付き依存: `if (index == aNewIndex)` → `Promise.resolve()`
- 参照: `aEngine.originalEngine`, `this.engines.length`

## EngineStore.removeEngine()
- 位置: L347-368
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("engineList").focus()`, `this.engines.findIndex()`, `this.engines.splice()`, `this.notifyRowCountChanged()`
- 条件付き依存: `if (aEngine instanceof lazy.AppProvidedConfigEngine)` → `gSearchPane.showRestoreDefaults()`
- 参照: `aEngine.id`, `element.id`, `lazy.AppProvidedConfigEngine`, `this.engines.length`

## EngineStore.browserSearchEngineModified()
- 位置: L377-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.addEngine()`, `this.notifyDefaultEngineChanged()`, `this.notifyRebuildViews()`, `this.notifyRowCountChanged()`, `this.removeEngine()`, `this.updateEngine()`
- 参照: `gEngineView.lastEngineIndex`

## EngineStore.restoreDefaultEngines()
- 位置: async L400-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( await lazy.SearchService.getAppProvidedEngines() ).map()`, `Services.policies.getActivePolicies()`, `gSearchPane.showRestoreDefaults()`, `lazy.SearchService.getAppProvidedEngines()`, `lazy.SearchService.getEngineByName()`, `lazy.SearchService.resetToAppDefaultEngine()`, `this.engines.some()`, `this.notifyRebuildViews()`
- 条件付き依存: `if (this.engines.some(this._isSameEngine, e))` → `this.moveEngine()`
- 条件付き依存: `if (this.engines.some(this._isSameEngine, e))` → `this._getEngineByName()`
- 条件付き依存: `if (!(this.engines.some(this._isSameEngine, e)))` → `this.engines.splice()`
- 条件付き依存: `if (!(this.engines.some(this._isSameEngine, e)))` → `lazy.SearchService.moveEngine()`
- 条件付き依存: `if (engine)` → `lazy.SearchService.removeEngine()`
- 参照: `Services.policies.getActivePolicies()?.SearchEngines?.Remove`, `appProvidedEngines.length`, `e.alias`, `e.name`, `e.originalEngine`, `engine.hidden`, `lazy.SearchService.CHANGE_REASON.ENTERPRISE`, `this._cloneEngine`, `this._isSameEngine`
- XPCOM: `Services.policies`

## EngineStore.changeEngine()
- 位置: L453-461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getIndexForEngine()`
- 参照: `aEngine.originalEngine`, `this.engines`

## EngineView.constructor()
- 位置: L475-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEngineStore.addListener()`, `document.getElementById()`, `lazy.UrlbarPrefs.addObserver()`, `this.#addListeners()`, `this.loadL10nNames()`
- 参照: `this._engineList`, `this._engineList.view`, `this._engineStore`

## EngineView.loadL10nNames()
- 位置: async L487-528
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `document.l10n.formatValues()`, `englishSearchStrings.formatValues()`, `getIDs()`, `lazy.UrlbarShared.LOCAL_SEARCH_MODES.forEach()`, `this._localShortcutL10nNames.set()`, `this.invalidate()`
- 参照: `this._localShortcutL10nNames`

## getIDs()
- 位置: L493-497
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarShared.LOCAL_SEARCH_MODES.map()`, `lazy.UrlbarShared.getResultSourceName()`
- 参照: `mode.source`

## EngineView.#addListeners()
- 位置: L530-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._engineList.addEventListener()`

## EngineView.lastEngineIndex()
- 位置: L538-540
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._engineStore.engines.length`

## EngineView.selectedIndex()
- 位置: L542-550
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `seln.getRangeCount()`
- 条件付き依存: `if (seln.getRangeCount() > 0)` → `seln.getRangeAt()`
- 参照: `min.value`, `this.selection`

## EngineView.selectedEngine()
- 位置: L552-554
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._engineStore.engines`, `this.selectedIndex`

## EngineView.rebuild()
- 位置: L557-559
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.invalidate()`

## EngineView.rowCountChanged()
- 位置: L561-572
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree.rowCountChanged()`
- 条件付き依存: `if (count < 0)` → `this.selection.select()`
- 条件付き依存: `if (count < 0)` → `Math.min()`
- 条件付き依存: `if (count < 0)` → `this.ensureRowIsVisible()`
- 参照: `this.currentIndex`, `this.rowCount`, `this.tree`

## EngineView.engineIconUpdated()
- 位置: L574-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree.columns.getNamedColumn()`, `this.tree?.invalidateCell()`

## EngineView.invalidate()
- 位置: L581-583
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree?.invalidate()`

## EngineView.ensureRowIsVisible()
- 位置: L585-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree.ensureRowIsVisible()`

## EngineView.getSourceIndexFromDrag()
- 位置: L589-591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dataTransfer.getData()`, `parseInt()`

## EngineView.isCheckBox()
- 位置: L593-595
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `column.id`

## EngineView.isEngineSelectedAndRemovable()
- 位置: L597-610
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getLocalShortcut()`
- 参照: `defaultEngine.name`, `defaultPrivateEngine.name`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `this.lastEngineIndex`, `this.selectedEngine.name`, `this.selectedIndex`

## EngineView.promptAndRemoveEngine()
- 位置: async L622-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.confirmExBC()`, `document.l10n.formatValues()`
- 条件付き依存: `if (engine.isAppProvided)` → `lazy.SearchService.removeEngine()`
- 条件付き依存: `if (engine.isAddonEngine)` → `document.l10n.formatValue()`
- 条件付き依存: `if (engine.isAddonEngine)` → `alert()`
- 条件付き依存: `if (button == 0)` → `lazy.SearchService.removeEngine()`
- 参照: `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_CONTENT`, `engine.isAddonEngine`, `engine.isAppProvided`, `lazy.SearchService.CHANGE_REASON.USER`, `this.selectedEngine.originalEngine`, `window.browsingContext`
- XPCOM: `Services.prompt`

## EngineView._getLocalShortcut()
- 位置: L676-682
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.UrlbarShared.LOCAL_SEARCH_MODES`, `this._engineStore.engines.length`

## EngineView.onPrefChanged()
- 位置: L690-697
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pref.split()`
- 条件付き依存: `if (parts[0] == "shortcuts" && parts[1] && parts.length == 2)` → `this.invalidate()`
- 参照: `parts.length`

## EngineView.handleEvent()
- 位置: L699-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEvent.target.classList.contains()`, `gSubDialog.open()`, `this.#onRestoreDefaults()`, `this.isEngineSelectedAndRemovable()`
- 条件付き依存: `if (aEvent.target.id == "engineChildren")` → `aEvent.target.parentNode.getCellAt()`
- 条件付き依存: `if (cell.col?.id == "engineKeyword")` → `this.#startEditingAlias()`
- 条件付き依存: `if (selection?.count > 0)` → `selection.toggleSelect()`
- 条件付き依存: `if (this._engineList.inputField.hidden && this._engineList.view)` → `this._engineList.blur()`
- 条件付き依存: `if (this.isEngineSelectedAndRemovable())` → `this.promptAndRemoveEngine()`
- 条件付き依存: `if (this.selectedEngine.isUserEngine)` → `gSubDialog.open()`
- 条件付き依存: `if (aEvent.target.id == "engineChildren")` → `this.#onDragEngineStart()`
- 条件付き依存: `if (aEvent.target.id == "engineList")` → `this.#onTreeKeyPress()`
- 条件付き依存: `if (aEvent.target.id == "engineList")` → `this.#onTreeSelect()`
- 参照: `aEvent.clientX`, `aEvent.clientY`, `aEvent.target.id`, `aEvent.type`, `cell.col?.id`, `selection.currentIndex`, `selection?.count`, `this._engineList.inputField.hidden`, `this._engineList.view`, `this._engineList.view.selection`, `this.selectedEngine`, `this.selectedEngine.isUserEngine`, `this.selectedEngine.originalEngine`, `this.selectedIndex`

## EngineView.#onRestoreDefaults()
- 位置: async L783-786
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._engineStore.restoreDefaultEngines()`, `this.rowCountChanged()`

## EngineView.#onDragEngineStart()
- 位置: L788-803
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._getLocalShortcut()`, `this.isCheckBox()`, `tree.getCellAt()`
- 条件付き依存: `if (this._getLocalShortcut(selectedIndex))` → `event.preventDefault()`
- 条件付き依存: `if (selectedIndex >= 0 && !this.isCheckBox(cell.row, cell.col))` → `event.dataTransfer.setData()`
- 条件付き依存: `if (selectedIndex >= 0 && !this.isCheckBox(cell.row, cell.col))` → `selectedIndex.toString()`
- 参照: `cell.col`, `cell.row`, `event.clientX`, `event.clientY`, `event.dataTransfer.effectAllowed`, `this.selectedIndex`

## EngineView.#onTreeSelect()
- 位置: L805-810
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.isEngineSelectedAndRemovable()`
- 参照: `document.getElementById("editEngineButton").disabled`, `document.getElementById("removeEngineButton").disabled`, `this.selectedEngine?.isUserEngine`

## EngineView.#onTreeKeyPress()
- 位置: L812-851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `tree.hasAttribute()`
- 条件付き依存: `if (aEvent.charCode == KeyEvent.DOM_VK_SPACE)` → `this.getCellValue()`
- 条件付き依存: `if (aEvent.charCode == KeyEvent.DOM_VK_SPACE)` → `tree.columns.getNamedColumn()`
- 条件付き依存: `if (aEvent.charCode == KeyEvent.DOM_VK_SPACE)` → `this.setCellValue()`
- 条件付き依存: `if (aEvent.charCode == KeyEvent.DOM_VK_SPACE)` → `tree.columns.getFirstColumn()`
- 条件付き依存: `if (aEvent.charCode == KeyEvent.DOM_VK_SPACE)` → `newValue.toString()`
- 条件付き依存: `if (aEvent.charCode == KeyEvent.DOM_VK_SPACE)` → `aEvent.preventDefault()`
- 条件付き依存: `if ( (isMac && aEvent.keyCode == KeyEvent.DOM_VK_RETURN) || (!isMac && aEvent.keyCode == KeyEvent.DOM_VK_F2) )` → `this.#startEditingAlias()`
- 条件付き依存: `if ( aEvent.keyCode == KeyEvent.DOM_VK_DELETE || (isMac && aEvent.shiftKey && aEvent.keyCode == KeyEvent.DOM_VK_BACK_SPACE) )` → `this.isEngineSelectedAndRemovable()`
- 条件付き依存: `if (this.isEngineSelectedAndRemovable())` → `this.promptAndRemoveEngine()`
- 参照: `KeyEvent.DOM_VK_BACK_SPACE`, `KeyEvent.DOM_VK_DELETE`, `KeyEvent.DOM_VK_F2`, `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `Services.appinfo.OS`, `aEvent.charCode`, `aEvent.keyCode`, `aEvent.shiftKey`, `this.selectedEngine`, `this.selectedIndex`
- XPCOM: `Services.appinfo`

## EngineView.#startEditingAlias()
- 位置: L858-868
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getLocalShortcut()`, `this.tree.columns.getLastColumn()`, `this.tree.inputField.select()`, `this.tree.startEditing()`
- 参照: `engine.alias`, `this._engineStore.engines`, `this.tree.inputField.value`

## EngineView.#startEditingName()
- 位置: L875-887
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tree.columns.getNamedColumn()`, `this.tree.inputField.select()`, `this.tree.startEditing()`
- 参照: `engine.isUserEngine`, `engine.name`, `this._engineStore.engines`, `this.tree.inputField.value`

## EngineView.rowCount()
- 位置: L890-898
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.UrlbarPrefs.get()`
- 条件付き依存: `if (!lazy.UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `localModes.filter()`
- 参照: `lazy.UrlbarShared.LOCAL_SEARCH_MODES`, `lazy.UrlbarShared.RESULT_SOURCE.ACTIONS`, `localModes.length`, `mode.source`, `this._engineStore.engines.length`

## EngineView.getImageSrc()
- 位置: L900-911
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.id == "engineName")` → `this._getLocalShortcut()`
- 参照: `column.id`, `shortcut.icon`, `this._engineStore.engines`, `this._engineStore.engines[index].iconURL`

## EngineView.getCellText()
- 位置: L913-941
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.id == "engineName")` → `this._getLocalShortcut()`
- 条件付き依存: `if (shortcut)` → `this._localShortcutL10nNames.get()`
- 条件付き依存: `if (column.id == "engineKeyword")` → `this._getLocalShortcut()`
- 条件付き依存: `if (shortcut)` → `lazy.UrlbarPrefs.getScotchBonnetPref()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.getScotchBonnetPref( "searchRestrictKeywords.featureGate" ) )` → `this._localShortcutL10nNames .get(shortcut.source) .map(keyword => `@${keyword.toLowerCase()}`) .join()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.getScotchBonnetPref( "searchRestrictKeywords.featureGate" ) )` → `this._localShortcutL10nNames .get(shortcut.source) .map()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.getScotchBonnetPref( "searchRestrictKeywords.featureGate" ) )` → `this._localShortcutL10nNames .get()`
- 条件付き依存: `if ( lazy.UrlbarPrefs.getScotchBonnetPref( "searchRestrictKeywords.featureGate" ) )` → `keyword.toLowerCase()`
- 条件付き依存: `if (column.id == "engineKeyword")` → `this._engineStore.engines[index].originalEngine.aliases.join()`
- 参照: `column.id`, `shortcut.restrict`, `shortcut.source`, `this._engineStore.engines`, `this._engineStore.engines[index].name`

## EngineView.setTree()
- 位置: L943-945
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.tree`

## EngineView.canDrop()
- 位置: L947-956
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getSourceIndexFromDrag()`
- 参照: `this._engineStore.engines.length`

## EngineView.drop()
- 位置: async L958-983
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSearchPane.showRestoreDefaults()`, `this._engineStore.moveEngine()`, `this.getSourceIndexFromDrag()`, `this.invalidate()`, `this.selection.select()`
- 参照: `Ci.nsITreeView`, `nsITreeView.DROP_AFTER`, `nsITreeView.DROP_BEFORE`, `this._engineStore.engines`, `this._engineStore.engines.length`
- XPCOM: `nsITreeView`

## EngineView.getRowProperties()
- 位置: L986-988
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.getCellProperties()
- 位置: L989-999
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.id == "engineName")` → `this._getLocalShortcut()`
- 条件付き依存: `if (shortcut)` → `lazy.UrlbarShared.getResultSourceName()`
- 参照: `column.id`, `shortcut.source`

## EngineView.getColumnProperties()
- 位置: L1000-1002
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.isContainer()
- 位置: L1003-1005
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.isContainerOpen()
- 位置: L1006-1008
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.isContainerEmpty()
- 位置: L1009-1011
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.isSeparator()
- 位置: L1012-1014
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.isSorted()
- 位置: L1015-1017
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.getParentIndex()
- 位置: L1018-1020
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.hasNextSibling()
- 位置: L1021-1023
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.getLevel()
- 位置: L1024-1026
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.getCellValue()
- 位置: L1027-1036
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.id == "engineShown")` → `this._getLocalShortcut()`
- 条件付き依存: `if (shortcut)` → `lazy.UrlbarPrefs.get()`
- 参照: `column.id`, `shortcut.pref`, `this._engineStore.engines`, `this._engineStore.engines[index].originalEngine.hideOneOffButton`

## EngineView.toggleOpenState()
- 位置: L1037-1037
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.cycleHeader()
- 位置: L1038-1038
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.selectionChanged()
- 位置: L1039-1039
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.cycleCell()
- 位置: L1040-1040
- 役割: (未記入)
- 触るとき: (未記入)

## EngineView.isEditable()
- 位置: L1041-1048
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._getLocalShortcut()`
- 参照: `column.id`, `this._engineStore.engines`, `this._engineStore.engines[index].isUserEngine`

## EngineView.setCellValue()
- 位置: L1049-1061
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.id == "engineShown")` → `this._getLocalShortcut()`
- 条件付き依存: `if (shortcut)` → `lazy.UrlbarPrefs.set()`
- 条件付き依存: `if (shortcut)` → `this.invalidate()`
- 条件付き依存: `if (column.id == "engineShown")` → `this.invalidate()`
- 参照: `column.id`, `shortcut.pref`, `this._engineStore.engines`, `this._engineStore.engines[index].originalEngine.hideOneOffButton`

## EngineView.setCellText()
- 位置: async L1062-1075
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (column.id == "engineKeyword")` → `this.#changeKeyword()`
- 条件付き依存: `if (!valid)` → `this.#startEditingAlias()`
- 条件付き依存: `if (column.id == "engineName" && engine.isUserEngine)` → `this.#changeName()`
- 条件付き依存: `if (!valid)` → `this.#startEditingName()`
- 参照: `column.id`, `engine.isUserEngine`, `this._engineStore.engines`

## EngineView.#changeKeyword()
- 位置: async L1088-1118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aNewKeyword.trim()`, `this._engineStore.changeEngine()`, `this.invalidate()`
- 条件付き依存: `if (keyword)` → `lazy.PlacesUtils.keywords.fetch()`
- 条件付き依存: `if (keyword)` → `lazy.SearchService.getEngineByAlias()`
- 条件付き依存: `if (isEngineDuplicate || isBookmarkDuplicate)` → `document.l10n.formatValue()`
- 条件付き依存: `if (isEngineDuplicate || isBookmarkDuplicate)` → `alert()`
- 参照: `aEngine.id`, `dupEngine.id`, `dupEngine.name`, `msgid.args`, `msgid.id`

## EngineView.#changeName()
- 位置: async L1131-1142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aEngine.originalEngine.rename()`
- 条件付き依存: `if (!valid)` → `document.l10n.formatValue()`
- 条件付き依存: `if (!valid)` → `alert()`
