# browser/components/preferences/preferences.js

source: browser/components/preferences/preferences.js
source-hash: 8b3acf475ad7be98c51eac0ddf65affb3c35846e
lines: 1189

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Integration.downloads.defineESModuleGetter()`, `Object.freeze()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `crypto.randomUUID()`, `document.addEventListener()`, `document.getElementById()`, `getFxAccountsSingleton()`, `srdSectionEnabled()`

## resizeCallback()
- 位置: async L135-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gSearchResultsPane.searchWithinNode()`
- 条件付き依存: `if (!node.tooltipNode)` → `gSearchResultsPane.createSearchTooltip()`
- 参照: `frame.contentDocument.firstElementChild`, `gSearchResultsPane.listSearchTooltips`, `gSearchResultsPane.query`, `node.tooltipNode`

## srdSectionEnabled()
- 位置: L174-184
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(section in srdSectionPrefs))` → `XPCOMUtils.defineLazyPreferenceGetter()`
- 参照: `srdSectionPrefs.all`

## visible()
- 位置: L248-248
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `srdSectionPrefs.all`

## visible()
- 位置: L261-261
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `srdSectionPrefs.all`

## visible()
- 位置: L274-274
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `srdSectionPrefs.all`

## visible()
- 位置: L281-282
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## visible()
- 位置: L289-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## visible()
- 位置: L331-331
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `srdSectionPrefs.all`

## visible()
- 位置: L355-355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `srdSectionEnabled()`

## visible()
- 位置: L398-398
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `srdSectionEnabled()`

## visible()
- 位置: L414-414
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `srdSectionEnabled()`

## visible()
- 位置: L467-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NimbusFeatures.moreFromMozilla.getVariable()`

## visible()
- 位置: L483-483
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `srdSectionEnabled()`

## visible()
- 位置: L494-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `srdSectionEnabled()`

## register_module()
- 位置: L515-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gCategoryInits.set()`, `gCategoryModules.set()`

## init()
- 位置: L519-543
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `categoryObject.init()`, `document.getElementById()`
- 条件付き依存: `if (template && !srdSectionPrefs.all)` → `template.replaceWith()`
- 条件付き依存: `if (template && !srdSectionPrefs.all)` → `Preferences.queueUpdateOfAllElements()`
- 参照: `srdSectionPrefs.all`, `template.content`, `this._initted`

## init_all()
- 位置: L549-673
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `Preferences.forceEnableInstantApply()`, `Preferences.queueUpdateOfAllElements()`, `Services.prefs.getBoolPref()`, `SettingPaneManager.registerPane()`, `categories.addEventListener()`, `document.dispatchEvent()`, `document.getElementById()`, `document.getElementById("addonsButton").addEventListener()`, `document.getElementById("focusSearch1").addEventListener()`, `document.querySelector()`, `e.preventDefault()`, `gMainPane.preInit()`, `gSearchResultsPane.init()`, `gSearchResultsPane.searchInput.focus()`, `gotoPref()`, `gotoPref().then()`, `mainWindow.BrowserAddonUI.openAddonsMgr()`, `maybeDisplayPoliciesNotice()`, `maybeDisplayTLSKeyLoggingNotice()`, `register_module()`, `window.addEventListener()`
- 条件付き依存: `if (!redesignEnabled)` → `register_module()`
- 条件付き依存: `if (!redesignEnabled)` → `document.getElementById()`
- 条件付き依存: `if (ExperimentAPI.labsEnabled)` → `document.getElementById()`
- 条件付き依存: `if (ExperimentAPI.labsEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (redesignEnabled)` → `categorySync.setAttribute()`
- 条件付き依存: `if (accountsEnabled)` → `register_module()`
- 条件付き依存: `if (redesignEnabled)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (redesignEnabled)` → `Services.sysinfo.getProperty()`
- 条件付き依存: `if ( AppConstants.platform == "win" && Services.prefs.getBoolPref("browser.shell.customIcon.enabled", false) && !Services.sysinfo.getProperty("hasWinPackageId") )` → `SettingPaneManager.registerPane()`
- 条件付き依存: `if (!(redesignEnabled))` → `NimbusFeatures.moreFromMozilla.recordExposureEvent()`
- 条件付き依存: `if (!(redesignEnabled))` → `NimbusFeatures.moreFromMozilla.getVariable()`
- 条件付き依存: `if (NimbusFeatures.moreFromMozilla.getVariable("enabled"))` → `document.getElementById()`
- 条件付き依存: `if (NimbusFeatures.moreFromMozilla.getVariable("enabled"))` → `NimbusFeatures.moreFromMozilla.getVariable()`
- 条件付き依存: `if (NimbusFeatures.moreFromMozilla.getVariable("enabled"))` → `register_module()`
- 参照: `AppConstants.platform`, `ExperimentAPI.labsEnabled`, `categorySync.hidden`, `categorySync.iconSrc`, `config.replaces`, `document.getElementById("category-experimental").hidden`, `document.getElementById("category-general").hidden`, `document.getElementById("category-more-from-mozilla").hidden`, `document.getElementById("nav-separator").hidden`, `e.button`, `event.target.view`, `gMoreFromMozillaPane.option`, `srdSectionPrefs.all`, `window.browsingContext.topChromeWindow`
- XPCOM: `Services.prefs` / `Services.sysinfo`

## onHashChange()
- 位置: L679-702
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gotoPref()`, `gotoPref(null, "Hash").then()`
- 条件付き依存: `if (restoredQuery)` → `gSearchResultsPane.searchFunction()`
- 参照: `document.location.hash`, `gSearchResultsPane.searchInput`, `gSearchResultsPane.searchInput.value`, `history.state.searchQuery`, `history.state?.searchQuery`

## onBeforeunload()
- 位置: L704-706
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.aboutpreferences.close.record()`

## recordSettingChangeTelemetry()
- 位置: L715-721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.aboutpreferences.change.record()`
- 参照: `gLastCategory.category`

## gotoPref()
- 位置: async L729-980
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.aboutpreferences[gleanId].record()`, `Services.prefs.getBoolPref()`, `SettingPaneManager.getWithParents()`, `category.indexOf()`, `category.substring()`, `categoryInfo.init()`, `categoryModule.handleSubcategory()`, `document.dispatchEvent()`, `document.getElementById()`, `friendlyPrefCategoryNameToInternalName()`, `gCategoryInits.get()`, `gCategoryModules.get()`, `hash.substring()`, `internalPrefCategoryNameToFriendlyName()`, `item.getAttribute()`, `scrollOffsets.newHistoryEntryId()`, `scrollOffsets.save()`, `scrollOffsets.setView()`, `search()`, `window.history.replaceState()`
- 条件付き依存: `if (subcategory)` → `category.substring()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.settings-redesign.enabled"))` → `resolveLegacyCategory()`
- 条件付き依存: `if (category != "paneSearchResults")` → `gSearchResultsPane.removeAllSearchIndicators()`
- 条件付き依存: `if (gLastCategory.category == category && !subcategory)` → `document.dispatchEvent()`
- 条件付き依存: `if (category != "paneSearchResults")` → `document.querySelectorAll()`
- 条件付き依存: `if (category != "paneSearchResults")` → `categories.querySelector()`
- 条件付き依存: `if (category != "paneSearchResults")` → `CSS.escape()`
- 条件付き依存: `if (!item || item.hidden)` → `categories.querySelector()`
- 条件付き依存: `if ( gLastCategory.category || unknownCategory || category != kDefaultCategoryInternalName || subcategory )` → `internalPrefCategoryNameToFriendlyName()`
- 条件付き依存: `if (aShowReason == "Click")` → `history.pushState()`
- 条件付き依存: `if (!(aShowReason == "Click"))` → `history.replaceState()`
- 条件付き依存: `if (prevCategory && prevCategory !== category)` → `gSubDialog.abortDialogs()`
- 条件付き依存: `if (gCurrentHistoryEntryId != null)` → `focusHistory.save()`
- 条件付き依存: `if (parentPanes.length > 1)` → `friendlyPrefCategoryNameToInternalName()`
- 条件付き依存: `if (aShowReason == "Click" && prevCategory)` → `internalPrefCategoryNameToFriendlyName()`
- 条件付き依存: `if (!categoryInfo)` → `console.error()`
- 条件付き依存: `if (document.hasPendingL10nMutations)` → `document.addEventListener()`
- 条件付き依存: `if (aShowReason != "Initial")` → `scrollOffsets.restore()`
- 条件付き依存: `if (aShowReason != "Initial")` → `focusHistory.restore()`
- 条件付き依存: `if (!categoryModule.handleSubcategory?.(subcategory))` → `spotlight()`
- 参照: `Glean.aboutpreferences`, `categories.currentView`, `document.hasPendingL10nMutations`, `document.location.hash`, `document.title`, `element.hidden`, `gLastCategory.category`, `gLastCategory.subcategory`, `gSearchResultsPane.query`, `gSearchResultsPane.searchInput.value`, `history.state`, `history.state?.historyEntryId`, `history.state?.previousCategory`, `item.hidden`, `parentPanes.length`, `resolved.category`, `resolved.subcategory`, `rootParent.id`, `srdSectionPrefs.all`
- XPCOM: `Services.prefs`

## search()
- 位置: L986-1023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `document.getElementById()`, `element.classList.remove()`, `element.getAttribute()`
- 条件付き依存: `if ( element.getAttribute("data-hidden-from-search") != "true" || element.getAttribute("data-subpanel") == "true" )` → `element.getAttribute()`
- 条件付き依存: `if (!( element.getAttribute("data-hidden-from-search") != "true" || element.getAttribute("data-subpanel") == "true" ))` → `element.getAttribute()`
- 条件付き依存: `if (element.localName === "setting-pane")` → `element.querySelectorAll()`
- 条件付き依存: `if (element.localName === "setting-pane")` → `group.classList.remove()`
- 参照: `(element).onSearchPane`, `element.hidden`, `element.localName`, `mainPrefPane.children`

## spotlight()
- 位置: L1025-1035
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelectorAll()`
- 条件付き依存: `if (highlightedElements.length)` → `element.classList.remove()`
- 条件付き依存: `if (subcategory)` → `scrollAndHighlight()`
- 参照: `highlightedElements.length`

## scrollAndHighlight()
- 位置: L1037-1052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelectorAll()`, `element.classList.add()`, `elements[0].scrollIntoView()`
- 参照: `elements.length`

## internalPrefCategoryNameToFriendlyName()
- 位置: L1055-1059
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aName || "").replace()`, `toReplace[4].toLowerCase()`

## confirmRestartPrompt()
- 位置: async L1070-1161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncConfirmEx()`, `button.get()`, `document.l10n.formatValues()`
- 条件付き依存: `if (buttonIndex == CONFIRM_RESTART_PROMPT_RESTART_NOW)` → `Cc["@mozilla.org/supports-PRBool;1"].createInstance()`
- 条件付き依存: `if (buttonIndex == CONFIRM_RESTART_PROMPT_RESTART_NOW)` → `Services.obs.notifyObservers()`
- 参照: `Ci.nsIPrompt.MODAL_TYPE_CONTENT`, `Ci.nsISupportsPRBool`, `Services.prompt.BUTTON_POS_0`, `Services.prompt.BUTTON_POS_0_DEFAULT`, `Services.prompt.BUTTON_POS_1`, `Services.prompt.BUTTON_POS_1_DEFAULT`, `Services.prompt.BUTTON_POS_2`, `Services.prompt.BUTTON_POS_2_DEFAULT`, `Services.prompt.BUTTON_TITLE_CANCEL`, `Services.prompt.BUTTON_TITLE_IS_STRING`, `cancelQuit.data`, `window.browsingContext`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsISupportsPRBool`](../../../xpcom/ds/nsISupportsPrimitives.idl.md) / `@mozilla.org/supports-PRBool;1` / `Services.obs` / `Services.prompt`

## appendSearchKeywords()
- 位置: L1165-1172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `element.getAttribute()`, `element.setAttribute()`, `keywords.join()`
- 条件付き依存: `if (searchKeywords)` → `keywords.push()`

## maybeDisplayPoliciesNotice()
- 位置: L1174-1180
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (Services.policies.status == Services.policies.ACTIVE)` → `document .getElementById("policies-container-content") .removeAttribute()`
- 条件付き依存: `if (Services.policies.status == Services.policies.ACTIVE)` → `document .getElementById()`
- 参照: `Services.policies.ACTIVE`, `Services.policies.status`
- XPCOM: `Services.policies`

## maybeDisplayTLSKeyLoggingNotice()
- 位置: L1182-1188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.exists()`
- 条件付き依存: `if (Services.env.exists("SSLKEYLOGFILE"))` → `document .getElementById("tls-key-logging-container-content") .removeAttribute()`
- 条件付き依存: `if (Services.env.exists("SSLKEYLOGFILE"))` → `document .getElementById()`
- XPCOM: `Services.env`
