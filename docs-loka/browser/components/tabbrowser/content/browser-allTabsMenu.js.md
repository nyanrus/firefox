# browser/components/tabbrowser/content/browser-allTabsMenu.js

source: browser/components/tabbrowser/content/browser-allTabsMenu.js
source-hash: b79e3da63737ace75a2195107f6c9562fa4f35f8
lines: 270

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## initElements()
- 位置: L30-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `document.getElementById()`, `template.replaceWith()`

## hasHiddenTabsExcludingFxView()
- 位置: L43-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBrowser.tabs.some()`

## init()
- 位置: L50-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ContextualIdentityService.getPublicIdentities()`, `ContextualIdentityService.getPublicIdentities().forEach()`, `FirefoxViewHandler.openTab()`, `Glean.browserUiInteraction.listAllTabsAction.close_all_duplicates.add()`, `Glean.browserUiInteraction.listAllTabsAction.search_tabs.add()`, `PanelUI._ensureShortcutsShown()`, `PanelUI.showSubView()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.prefs.getBoolPref()`, `containerTabsMenuSeparator.parentNode.insertBefore()`, `document.createDocumentFragment()`, `document.createXULElement()`, `document.getElementById()`, `e.target.addEventListener()`, `element.remove()`, `elements.push()`, `frag.appendChild()`, `gBrowser.getAllDuplicateTabsToClose()`, `gBrowser.removeAllDuplicateTabs()`, `menuitem.classList.add()`, `menuitem.setAttribute()`, `this.allTabsView .querySelector()`, `this.allTabsView .querySelector(".all-tabs-item[selected]") ?.scrollIntoView()`, `this.allTabsView.addEventListener()`, `this.containerTabsView.addEventListener()`, `this.containerTabsView.querySelector()`, `this.hasHiddenTabsExcludingFxView()`, `this.hiddenAudioTabs.hasChildNodes()`, `this.initElements()`, `this.searchTabs()`
- 条件付き依存: `if (hasHiddenAudioTabs)` → `this.allTabsViewTabs.prepend()`
- 条件付き依存: `if (!(hasHiddenAudioTabs))` → `this.allTabsViewTabs.append()`
- 条件付き依存: `if (identity.name)` → `menuitem.setAttribute()`
- 条件付き依存: `if (!(identity.name))` → `document.l10n.setAttributes()`
- XPCOM: `Services.prefs`

## filterFn()
- 位置: L60-60
- 役割: (未記入)
- 触るとき: (未記入)

## filterFn()
- 位置: L66-66
- 役割: (未記入)
- 触るとき: (未記入)

## filterFn()
- 位置: L205-205
- 役割: (未記入)
- 触るとき: (未記入)

## canOpen()
- 位置: L212-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isElementVisible()`, `this.initElements()`

## showAllTabsPanel()
- 位置: L217-237
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.init()`
- 条件付き依存: `if (this.canOpen)` → `Glean.browserUiInteraction.allTabsPanelEntrypoint[entrypoint].add()`
- 条件付き依存: `if (this.canOpen)` → `BrowserUsageTelemetry.recordInteractionEvent()`
- 条件付き依存: `if (this.canOpen)` → `PanelUI.showSubView()`

## hideAllTabsPanel()
- 位置: L239-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.allTabsView?.closest()`
- 条件付き依存: `if (panel)` → `PanelMultiView.hidePopup()`

## showHiddenTabsPanel()
- 位置: L246-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PanelUI.showSubView()`, `this.allTabsView.addEventListener()`, `this.init()`, `this.showAllTabsPanel()`

## searchTabs()
- 位置: L264-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gURLBar.search()`
