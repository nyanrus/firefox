# browser/components/urlbar/content/SearchModeSwitcher.mjs

source: browser/components/urlbar/content/SearchModeSwitcher.mjs
source-hash: 4d1c2c0aa625a6cd69bc0f21fad362103aed01ae
lines: 1189

## <module>
- 役割: (未記入)

## getL10n()
- 位置: L32-35
- 役割: (未記入)
- 触るとき: (未記入)

## SearchModeSwitcher.constructor()
- 位置: L111-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.keywordEnabled()`, `input.querySelector()`, `this.#button.setAttribute()`, `window.matchMedia()`
- 条件付き依存: `if (input.variantB)` → `this.#button.setAttribute()`
- 条件付き依存: `if (document.createXULElement)` → `document.createXULElement()`
- 条件付き依存: `if (document.createXULElement)` → `panel.setAttribute()`
- 条件付き依存: `if (document.createXULElement)` → `panel.classList.add()`
- 条件付き依存: `if (document.createXULElement)` → `this.#panelList.replaceWith()`
- 条件付き依存: `if (document.createXULElement)` → `panel.appendChild()`
- 条件付き依存: `if (!UrlbarShared.keywordEnabled(this.#input.sapName))` → `this.updateSearchIcon()`
- 参照: `document.createXULElement`, `input.sapName`, `input.variantB`, `this.#button`, `this.#closebutton`, `this.#input`, `this.#input.sapName`, `this.#noWordmarkQuery`, `this.#panelList`, `this.#panelList.id`

## SearchModeSwitcher.connect()
- 位置: L150-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.addObserver()`, `this.#isEnabled()`
- 条件付き依存: `if (this.#isEnabled())` → `this.#enableObservers()`

## SearchModeSwitcher.disconnect()
- 位置: L161-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.removeObserver()`, `this.#disableObservers()`

## SearchModeSwitcher.#isEnabled()
- 位置: L166-171
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 参照: `this.#input.isSearchbarSAP`

## SearchModeSwitcher.#onPopupShowing()
- 位置: async L173-185
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#buildSearchModeList()`, `this.#input.controller.engagementEvent.discard()`, `this.#input.view.close()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.opened.add()`
- 参照: `this.#input.sapName`

## SearchModeSwitcher.closePanel()
- 位置: L190-192
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#panelList.hide()`

## SearchModeSwitcher.#openPreferences()
- 位置: L194-200
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#input.parentController.openPreferences()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked.settings.add()`
- 参照: `this.#input.sapName`

## SearchModeSwitcher.exitSearchMode()
- 位置: L208-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `this.#input.startQuery()`
- 参照: `this.#engines`, `this.#input.searchMode`, `this.#selectedIndex`

## SearchModeSwitcher.onSearchModeChanged()
- 位置: L220-228
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#isEnabled()`
- 条件付き依存: `if (this.#isEnabled())` → `this.updateSearchIcon()`
- 参照: `window.closed`

## SearchModeSwitcher.handleEvent()
- 位置: L230-309
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.currentTarget.localName == "panel-item")` → `this.#handlePanelItemEvent()`
- 条件付き依存: `if (event.currentTarget == this.#closebutton)` → `event.stopPropagation()`
- 条件付き依存: `if (event.type == "click")` → `this.#input.focus()`
- 条件付き依存: `if (event.type == "click")` → `this.exitSearchMode()`
- 条件付き依存: `if (event.type == "searchmodechanged")` → `this.onSearchModeChanged()`
- 条件付き依存: `if (this.#input.variantA || this.#input.variantB)` → `this.updateSearchIcon()`
- 条件付き依存: `if (event.type == "focus")` → `this.#input.setUnifiedSearchButtonAvailability()`
- 条件付き依存: `if (event.type == "focusout")` → `this.#input.contains()`
- 条件付き依存: `if (event.type == "showing")` → `this.#onPopupShowing()`
- 条件付き依存: `if (document.activeElement == this.#button)` → `this.#input.focus()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `this.#input.focus()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `this.#input.view.selectBy()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `event.preventDefault()`
- 条件付き依存: `if (this.#input.view.isOpen)` → `this.#input.view.close()`
- 条件付き依存: `if (event.keyCode == KeyEvent.DOM_VK_DOWN)` → `this.#panelList.show()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_TAB`, `document.activeElement`, `event.currentTarget`, `event.currentTarget.localName`, `event.keyCode`, `event.relatedTarget`, `event.shiftKey`, `event.type`, `this.#button`, `this.#button.tabIndex`, `this.#closebutton`, `this.#input.variantA`, `this.#input.variantB`, `this.#input.view.isOpen`, `this.#noWordmarkQuery`

## SearchModeSwitcher.#handlePanelItemEvent()
- 位置: L318-381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `mouseEvent.stopPropagation()`, `this.#input.controller.engineStore.getEngine()`, `this.#installOpenSearchEngine()`, `this.#localSearch()`, `this.#openPreferences()`, `this.#remoteSearch()`, `this.closePanel()`
- 参照: `KeyEvent.DOM_VK_RETURN`, `KeyEvent.DOM_VK_SPACE`, `MouseEvent.MOZ_SOURCE_KEYBOARD`, `event.currentTarget`, `event.type`, `keyboardEvent.keyCode`, `mouseEvent.button`, `mouseEvent.inputSource`, `panelItem._engine`, `panelItem.dataset.action`, `panelItem.dataset.engineId`, `panelItem.dataset.restrict`

## SearchModeSwitcher.#addCommandListeners()
- 位置: L386-390
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelItem.addEventListener()`

## SearchModeSwitcher.onSearchEngineUpdate()
- 位置: L392-402
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.updateSearchIcon()`
- 参照: `window.closed`

## SearchModeSwitcher.onPrefChanged()
- 位置: L410-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (pref == SKIP_TAB_STOP_PREF)` → `this.#isEnabled()`
- 条件付き依存: `if (this.#isEnabled())` → `UrlbarPrefs.get()`
- 条件付き依存: `if (UrlbarPrefs.get(pref))` → `this.#enableSkipTabStop()`
- 条件付き依存: `if (!(UrlbarPrefs.get(pref)))` → `this.#disableSkipTabStop()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `this.#enableObservers()`
- 条件付き依存: `if (UrlbarPrefs.get("scotchBonnet.enableOverride"))` → `this.updateSearchIcon()`
- 条件付き依存: `if (!(UrlbarPrefs.get("scotchBonnet.enableOverride")))` → `this.#disableObservers()`
- 参照: `this.#input.isSearchbarSAP`, `window.closed`

## SearchModeSwitcher.handleKeyDown()
- 位置: L456-472
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.getModifierState()`
- 条件付き依存: `if (event.altKey)` → `this.#handleAltUpDown()`
- 条件付き依存: `if (!(event.altKey))` → `event.getModifierState()`
- 条件付き依存: `if (event.getModifierState("Accel"))` → `this.#handleAccelUpDown()`
- 条件付き依存: `if ( (event.keyCode == KeyEvent.DOM_VK_UP || event.keyCode == KeyEvent.DOM_VK_DOWN) && (event.altKey || event.getModifierState("Accel")) )` → `event.stopPropagation()`
- 条件付き依存: `if ( (event.keyCode == KeyEvent.DOM_VK_UP || event.keyCode == KeyEvent.DOM_VK_DOWN) && (event.altKey || event.getModifierState("Accel")) )` → `event.preventDefault()`
- 参照: `KeyEvent.DOM_VK_DOWN`, `KeyEvent.DOM_VK_UP`, `event.altKey`, `event.keyCode`

## SearchModeSwitcher.#handleAltUpDown()
- 位置: L474-477
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#input.controller.focusOnUnifiedSearchButton()`, `this.#panelList.show()`
- 参照: `this.#button`

## SearchModeSwitcher.#handleAccelUpDown()
- 位置: async L479-505
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSearchString()`, `this.#input.setSearchMode()`
- 条件付き依存: `if (!this.#engines.length)` → `this.#populateEngines()`
- 条件付き依存: `if (searchString)` → `this.#input.startQuery()`
- 参照: `KeyEvent.DOM_VK_UP`, `UrlbarShared.RESULT_SOURCE.SEARCH`, `event.keyCode`, `selectedEngine?.name`, `selectedEngine?.source`, `this.#engines`, `this.#engines.length`, `this.#input.window.gBrowser.selectedBrowser`, `this.#selectedIndex`

## SearchModeSwitcher.#populateEngines()
- 位置: async L507-533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#input.controller.engineStore .getEngines()`, `this.#input.controller.engineStore .getEngines() .filter()`, `this.#input.controller.engineStore.init()`
- 条件付き依存: `if (!(this.#input.sapName != "urlbar"))` → `searchEngines.concat()`
- 条件付き依存: `if (!(this.#input.sapName != "urlbar"))` → `UrlbarShared.LOCAL_SEARCH_MODES.filter()`
- 条件付き依存: `if (!(this.#input.sapName != "urlbar"))` → `UrlbarPrefs.get()`
- 参照: `engine.hideOneOffButton`, `engine.pref`, `this.#engines`, `this.#input.sapName`

## SearchModeSwitcher.toggleAddEnginesBadge()
- 位置: L541-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#badgeIfUnderSiteCap()`
- 条件付き依存: `if (this.#input.isSearchbarSAP)` → `this.#button.toggleAttribute()`
- 条件付き依存: `if ( !show || !UrlbarPrefs.get("unifiedSearchButton.always") || this.#hasAdjacentSearchbar )` → `this.#button.removeAttribute()`
- 参照: `this.#hasAdjacentSearchbar`, `this.#input.isSearchbarSAP`

## SearchModeSwitcher.#hasAdjacentSearchbar()
- 位置: L564-571
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy?.CustomizableUI.getPlacementOfWidget()`
- 参照: `this.#input.isSearchbarSAP`

## SearchModeSwitcher.#contentPrefs()
- 位置: L576-580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/content-pref/service;1"].getService()`
- 参照: `Ci.nsIContentPrefService2`
- XPCOM: [`nsIContentPrefService2`](../../../../dom/interfaces/base/nsIContentPrefService2.idl.md) / `@mozilla.org/content-pref/service;1` → `ContentPrefService2` (toolkit/components/contentprefs/components.conf)

## SearchModeSwitcher.#badgeIfUnderSiteCap()
- 位置: L586-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contentPrefs.getByDomainAndName()`, `this.#contentPrefs.getCachedByDomainAndName()`
- 条件付き依存: `if (cached)` → `apply()`
- 条件付き依存: `if (cached)` → `Number()`
- 参照: `browser.loadContext`, `browser?.currentURI`, `cached.value`, `this.#input.window.gBrowser?.selectedBrowser`, `uri.spec`

## apply()
- 位置: L599-613
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#button.toggleAttribute()`, `this.#countedBadgeFor.get()`
- 条件付き依存: `if (show)` → `this.#countBadgeShown()`
- 参照: `this.#input.window.gBrowser?.selectedBrowser`

## SearchModeSwitcher.handleResult()
- 位置: L631-633
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`
- 参照: `pref.value`

## SearchModeSwitcher.handleError()
- 位置: L634-634
- 役割: (未記入)
- 触るとき: (未記入)

## handleCompletion()
- 位置: L635-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `apply()`

## SearchModeSwitcher.#countBadgeShown()
- 位置: L648-660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#contentPrefs.set()`, `this.#countedBadgeFor.get()`, `this.#countedBadgeFor.set()`
- 参照: `browser.loadContext`

## SearchModeSwitcher.updateSearchIcon()
- 位置: async L670-712
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.keywordEnabled()`, `this.#getSearchIcon()`, `this.#input.querySelector()`
- 条件付き依存: `if (wordmark)` → `this.#button.removeAttribute()`
- 条件付き依存: `if (wordmark)` → `this.#button.setAttribute()`
- 条件付き依存: `if (!(wordmark))` → `this.#button.setAttribute()`
- 条件付き依存: `if (!(wordmark))` → `this.#button.removeAttribute()`
- 条件付き依存: `if (!(showLabel))` → `labelEl.replaceChildren()`
- 条件付き依存: `if (!UrlbarShared.keywordEnabled(this.#input.sapName))` → `this.#setButtonTitle()`
- 条件付き依存: `if (label)` → `this.#setButtonTitle()`
- 条件付き依存: `if (!(label))` → `this.#setButtonTitle()`
- 参照: `labelEl.textContent`, `searchMode?.engineName`, `searchMode?.source`, `this.#input.sapName`, `this.#input.searchMode`, `this.#input.variantA`, `this.#input.variantB`

## SearchModeSwitcher.#setButtonTitle()
- 位置: async L726-736
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatMessages()`, `message.attributes.find()`, `this.#button.removeAttribute()`
- 参照: `a.name`, `message.attributes.find(a => a.name == "title").value`, `this.#button.ariaLabel`, `this.#button.title`, `this.#buttonTitleRequest`

## SearchModeSwitcher.#getSearchIcon()
- 位置: async L738-775
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `UrlbarShared.keywordEnabled()`, `this.#getDisplayedEngineDetails()`
- 条件付き依存: `if ( UrlbarPrefs.get("unifiedSearchButton.always") && !this.#lastInputValue && this.#input.focused && this.#input.value.length )` → `this.#input.view?.getResultAtIndex()`
- 参照: `SearchModeSwitcher.ICON_GLOBE`, `UrlbarShared.RESULT_TYPE.TAB_SWITCH`, `UrlbarShared.RESULT_TYPE.URL`, `result.type`, `this.#input.focused`, `this.#input.sapName`, `this.#input.searchMode`, `this.#input.value`, `this.#input.value.length`, `this.#lastInputValue`

## SearchModeSwitcher.#getEngineWordmark()
- 位置: L786-796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `WORDMARK_ENGINE_FAMILIES.has()`, `engine.id.split()`
- 参照: `engine.isConfigEngine`, `this.#input.variantA`, `this.#input.variantB`, `this.#noWordmarkQuery.matches`

## SearchModeSwitcher.#getSearchModeLabel()
- 位置: async L798-802
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`, `getL10n()`, `getL10n().formatMessages()`
- 参照: `m.source`, `mode.uiLabel`, `str.value`

## SearchModeSwitcher.#getDisplayedEngineDetails()
- 位置: async L804-835
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.LOCAL_SEARCH_MODES.find()`, `this.#getSearchModeLabel()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `this.#input.controller.engineStore.init()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `this.#input.controller.engineStore.getEngineByName()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `engine.getIconURL()`
- 条件付き依存: `if (!searchMode || searchMode.engineName)` → `this.#getEngineWordmark()`
- 参照: `SearchModeSwitcher.ICON_GLASS`, `engine.name`, `m.source`, `mode.icon`, `searchMode.engineName`, `searchMode.source`, `this.#input.controller.engineStore.default`

## SearchModeSwitcher.#buildSearchModeList()
- 位置: async L840-908
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `footerSeparator.after()`, `footerSeparator.toggleAttribute()`, `item.remove()`, `lazy.OpenSearchManager.getInstallableEngines()`, `menuitem.classList.add()`, `openSearchEngines.slice()`, `this.#addCommandListeners()`, `this.#buildSettingsButton()`, `this.#createButton()`, `this.#panelList.dispatchEvent()`, `this.#panelList.querySelector()`, `this.#panelList.querySelectorAll()`, `this.#populateEngines()`
- 条件付き依存: `if (engine.source)` → `footerSeparator.before()`
- 条件付き依存: `if (engine.source)` → `this.#buildLocalSearchButton()`
- 条件付き依存: `if (engine.name)` → `this.#buildEngineSearchButton()`
- 条件付き依存: `if (engine.name)` → `installedEngineSeparator.before()`
- 条件付き依存: `if (this.#panelList.wasOpenedByKeyboard)` → `this.#panelList.focusWalker.nextNode()`
- 参照: `SearchModeSwitcher.MAX_OPENSEARCH_ENGINES`, `browser.selectedBrowser`, `engine.icon`, `engine.name`, `engine.source`, `engine.title`, `footerSeparator.previousElementSibling`, `menuitem._engine`, `menuitem.dataset.action`, `menuitem.dataset.engineName`, `this.#engines`, `this.#input.window.gBrowser`, `this.#panelList`, `this.#panelList.focusWalker.currentNode`, `this.#panelList.wasOpenedByKeyboard`

## SearchModeSwitcher.#whereToOpenSerp()
- 位置: L915-924
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarContentUtils.whereToOpenLink()`, `where.startsWith()`

## SearchModeSwitcher.#buildSettingsButton()
- 位置: L930-943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `document.l10n.setAttributes()`, `menuitem.classList.add()`, `this.#addCommandListeners()`, `this.#createButton()`, `this.#panelList.appendChild()`
- 参照: `menuitem.dataset.action`

## SearchModeSwitcher.#buildEngineSearchButton()
- 位置: async L948-966
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `engine.getIconURL()`, `engine.isNew()`, `menuitem.classList.add()`, `menuitem.setAttribute()`, `this.#addCommandListeners()`, `this.#createButton()`
- 条件付き依存: `if (engine.isNew() && engine.isAppProvided)` → `menuitem.setAttribute()`
- 参照: `engine.id`, `engine.isAppProvided`, `engine.name`, `menuitem.dataset.action`, `menuitem.dataset.engineId`, `menuitem.dataset.engineName`

## SearchModeSwitcher.#buildLocalSearchButton()
- 位置: async L972-989
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getResultSourceName()`, `document.l10n.setAttributes()`, `menuitem.classList.add()`, `this.#addCommandListeners()`, `this.#createButton()`, `this.#getDisplayedEngineDetails()`
- 条件付き依存: `if (mode.keyId)` → `menuitem.setAttribute()`
- 条件付き依存: `if (mode.keyId)` → `lazy.CustomizableUI.addShortcut()`
- 参照: `menuitem.dataset.action`, `menuitem.dataset.restrict`, `mode.keyId`, `mode.restrict`, `mode.source`, `mode.uiLabel`

## SearchModeSwitcher.#localSearch()
- 位置: L997-1005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSearchString()`, `this.#input.search()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked.local_search.add()`
- 参照: `this.#input.sapName`

## SearchModeSwitcher.#remoteSearch()
- 位置: L1016-1046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSearchString()`, `this.#whereToOpenSerp()`
- 条件付き依存: `if (!event.shiftKey && whereToOpenSerp == "current")` → `this.closePanel()`
- 条件付き依存: `if (!event.shiftKey && whereToOpenSerp == "current")` → `this.#input.search()`
- 条件付き依存: `if (whereToOpenSerp == "current")` → `this.closePanel()`
- 条件付き依存: `if (!(!event.shiftKey && whereToOpenSerp == "current"))` → `this.#input.openSearchEnginePage()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked[ searchEngine.isConfigEngine ? "builtin_search" : "addon_search" ].add()`
- 参照: `Glean.urlbarUnifiedsearchbutton.picked`, `event.shiftKey`, `searchEngine.isConfigEngine`, `this.#input.sapName`

## SearchModeSwitcher.#getSearchString()
- 位置: L1053-1058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#input.getAttribute()`
- 参照: `this.#input.value`

## SearchModeSwitcher.eventTargetIsPanelItem()
- 位置: L1067-1079
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `classList.contains()`
- 参照: `event?.target`, `target.classList`

## SearchModeSwitcher.#enableObservers()
- 位置: L1081-1099
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `this.#button.addEventListener()`, `this.#closebutton.addEventListener()`, `this.#input.addEventListener()`, `this.#input.controller.engineStore.addObserver()`, `this.#noWordmarkQuery.addEventListener()`, `this.#panelList.addEventListener()`
- 条件付き依存: `if (UrlbarPrefs.get(SKIP_TAB_STOP_PREF))` → `this.#enableSkipTabStop()`
- 参照: `this.onSearchEngineUpdate`

## SearchModeSwitcher.#disableObservers()
- 位置: L1101-1119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#button.removeEventListener()`, `this.#closebutton.removeEventListener()`, `this.#disableSkipTabStop()`, `this.#input.controller.engineStore.removeObserver()`, `this.#input.removeEventListener()`, `this.#noWordmarkQuery.removeEventListener()`, `this.#panelList.removeEventListener()`
- 参照: `this.onSearchEngineUpdate`

## SearchModeSwitcher.#enableSkipTabStop()
- 位置: L1127-1131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#button.setAttribute()`, `this.#input.addEventListener()`

## SearchModeSwitcher.#disableSkipTabStop()
- 位置: L1133-1138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#button.removeAttribute()`, `this.#input.removeEventListener()`
- 参照: `this.#button.tabIndex`

## SearchModeSwitcher.#createButton()
- 位置: L1146-1159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `panelitem.style.setProperty()`
- 参照: `panelitem.textContent`

## SearchModeSwitcher.#installOpenSearchEngine()
- 位置: async L1167-1187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchUIUtils.addOpenSearchEngine()`, `this.#input.controller.engineStore.addObserver()`
- 条件付き依存: `if (this.#input.sapName == "urlbar")` → `Glean.urlbarUnifiedsearchbutton.picked.addon_search.add()`
- 参照: `engine.icon`, `engine.uri`, `this.#input.sapName`, `this.#input.window.gBrowser.selectedBrowser.browsingContext`

## observer()
- 位置: L1169-1176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getSearchString()`, `this.#input.controller.engineStore.removeObserver()`, `this.#input.search()`
