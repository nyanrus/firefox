# browser/components/extensions/parent/ext-pageAction.js

source: browser/components/extensions/parent/ext-pageAction.js
source-hash: 72c1b3fd63d94648f6015b584a27a83e033a0658
lines: 417

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## PageAction.constructor()
- 位置: L28-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.getContextData()`
- 参照: `this.buttonDelegate`

## PageAction.updateOnChange()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buttonDelegate.updateButton()`
- 参照: `target.documentGlobal`

## PageAction.dispatchClick()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.buttonDelegate.emit()`

## PageAction.getTab()
- 位置: L42-47
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (tabId !== null)` → `tabTracker.getTab()`

## PageAction.isPanelShownBlockingOpenPopup()
- 位置: L49-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isGloballyBlockingOpenPopup()`
- 参照: `panel.documentGlobal`, `panel.state`, `this.buttonDelegate.popupNode?.panel`

## for()
- 位置: L59-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pageActionMap.get()`

## onUpdate()
- 位置: L63-70
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!("page_action" in manifest))` → `BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (!("page_action" in manifest))` → `makeWidgetId()`

## onDisable()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.recordWidgetChange()`, `makeWidgetId()`

## onUninstall()
- 位置: L76-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `BrowserUsageTelemetry.recordWidgetChange()`, `makeWidgetId()`

## onManifestEntry()
- 位置: async L82-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `makeWidgetId()`, `pageActionMap.set()`, `this.action.loadIconData()`
- 条件付き依存: `if (!this.browserPageAction)` → `PageActions.addAction()`
- 条件付き依存: `if (!this.browserPageAction)` → `this.action.getProperty()`
- 条件付き依存: `if (!this.browserPageAction)` → `this.action.getPinned()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `ExtensionParent.browserStartupPromise.then()`
- 条件付き依存: `if (this.extension.startupReason != "APP_STARTUP")` → `BrowserUsageTelemetry.recordWidgetChange()`
- 条件付き依存: `if (this.action.getProperty(null, "enabled") === undefined)` → `windowTracker.browserWindows()`
- 条件付き依存: `if (this.action.getProperty(null, "enabled") === undefined)` → `this.action.isShownForTab()`
- 条件付き依存: `if (this.action.isShownForTab(tab))` → `this.updateButton()`
- 参照: `PageActions.Action`, `extension.id`, `extension.manifest.page_action`, `extension.tabManager`, `options.browser_style`, `this.action`, `this.browserPageAction`, `this.browserPageAction.pinnedToUrlbar`, `this.browserStyle`, `this.extension.startupReason`, `this.id`, `this.lastValues`, `this.tabManager`, `window.gBrowser.selectedTab`

## onPlacedHandler()
- 位置: L101-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buttonNode.addEventListener()`, `clickModifiersFromEvent()`, `this.action.dispatchClick()`, `this.tabManager.addActiveTabPermission()`
- 条件付き依存: `if (isPanel)` → `buttonNode.closest("#pageActionPanel").hidePopup()`
- 条件付き依存: `if (isPanel)` → `buttonNode.closest()`
- 参照: `event.button`, `event.target.disabled`, `event.target.documentGlobal`, `window.gBrowser.selectedTab`

## onCommand()
- 位置: L130-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clickModifiersFromEvent()`, `this.handleClick()`
- 参照: `event.button`, `event.target.documentGlobal`

## onBeforePlacedInWindow()
- 位置: L136-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.extension.hasPermission()`
- 条件付き依存: `if ( this.extension.hasPermission("menus") || this.extension.hasPermission("contextMenus") )` → `browserWindow.document.addEventListener()`

## onPlacedInPanel()
- 位置: L144-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onPlacedHandler()`

## onPlacedInUrlbar()
- 位置: L145-145
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onPlacedHandler()`

## onRemovedFromWindow()
- 位置: L146-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browserWindow.document.removeEventListener()`

## onShutdown()
- 位置: L179-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pageActionMap.delete()`, `this.action.onShutdown()`
- 条件付き依存: `if (!isAppShutdown && this.browserPageAction)` → `this.browserPageAction.remove()`
- 参照: `this.browserPageAction`, `this.extension`

## updateButton()
- 位置: L199-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.action.getContextData()`, `this.lastValues.get()`, `window.requestAnimationFrame()`
- 条件付き依存: `if (last.title !== title)` → `this.browserPageAction.setTitle()`
- 条件付き依存: `if (last.enabled !== enabled)` → `this.browserPageAction.setDisabled()`
- 条件付き依存: `if (last.icon !== icon)` → `this.browserPageAction.setIconURL()`
- 参照: `last.enabled`, `last.icon`, `last.title`, `tabData.enabled`, `tabData.icon`, `tabData.patternMatching`, `tabData.title`, `this.browserPageAction`, `this.extension.name`, `window.gBrowser.selectedTab`

## triggerAction()
- 位置: L240-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleClick()`

## handleEvent()
- 位置: L244-286
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getActionId()`, `this.browserPageAction.getDisabled()`, `this.extension.hasPermission()`
- 条件付き依存: `if ( menu.id === "pageActionContextMenu" && trigger && getActionId() === this.browserPageAction.id && !this.browserPageAction.getDisabled(trigger.documentGlobal)...)` → `global.actionContextMenu()`
- 参照: `event.target`, `event.type`, `menu.id`, `menu.triggerNode`, `this.browserPageAction.id`, `this.extension`, `trigger.documentGlobal`

## getActionId()
- 位置: L249-268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.getAttribute()`, `trigger.getAttribute()`
- 参照: `n.id`, `n.localName`, `n.parentElement`

## handleClick()
- 位置: async L293-360
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExtensionTelemetry.pageActionPopupOpen.stopwatchStart()`, `this.action.triggerClickOrPopup()`
- 条件付き依存: `if (this.popupNode && this.popupNode.panel.state !== "closed")` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (this.popupNode && this.popupNode.panel.state !== "closed")` → `window.BrowserPageActions.togglePanelForAction()`
- 条件付き依存: `if (popupURL)` → `popup.panel.addEventListener()`
- 条件付き依存: `if (popup.destroyed)` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (popupURL)` → `window.BrowserPageActions.togglePanelForAction()`
- 条件付き依存: `if (popupURL)` → `popup.destroy()`
- 条件付き依存: `if (popupURL)` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 条件付き依存: `if (popupURL)` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchFinish()`
- 条件付き依存: `if (!(popupURL))` → `ExtensionTelemetry.pageActionPopupOpen.stopwatchCancel()`
- 参照: `popup.contentReady`, `popup.destroyed`, `popup.panel`, `this.browserPageAction`, `this.browserStyle`, `this.popupNode`, `this.popupNode.panel`, `this.popupNode.panel.state`, `window.document`, `window.gBrowser.selectedTab`

## onClicked()
- 位置: L363-388
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.on()`

## listener()
- 位置: async L367-376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `context?.withPendingBrowser()`, `fire.sync()`, `tabManager.convert()`
- 条件付き依存: `if (fire.wakeup)` → `fire.wakeup()`
- 参照: `fire.wakeup`, `tab.linkedBrowser`

## unregister()
- 位置: L380-382
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.off()`

## convert()
- 位置: L383-386
- 役割: (未記入)
- 触るとき: (未記入)

## getAPI()
- 位置: L391-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.api()`, `new EventManager({ context, module: "pageAction", event: "onClicked", inputHandling: true, extensionApi: this, }).api()`

## openPopup()
- 位置: L406-410
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `action.throwIfOpenPopupIsBlockedByAnyAction()`, `this.triggerAction()`
- 参照: `windowTracker.topWindow`
