# browser/actors/PromptParent.sys.mjs

source: browser/actors/PromptParent.sys.mjs
source-hash: e3694b8418faea9b38bf4304dea1764132c7c07c
lines: 384

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## PromptParent.didDestroy()
- 位置: L29-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.forceClosePrompts()`

## PromptParent.registerDialog()
- 位置: L46-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialogs.set()`, `gBrowserDialogs.get()`
- 条件付き依存: `if (!dialogs)` → `gBrowserDialogs.set()`
- 参照: `this.browsingContext`

## PromptParent.unregisterPrompt()
- 位置: L64-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialogs?.delete()`, `gBrowserDialogs.get()`
- 参照: `this.browsingContext`

## PromptParent.forceClosePrompts()
- 位置: L72-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dialog?.abort()`, `gBrowserDialogs.get()`
- 参照: `this.browsingContext`

## PromptParent.isAboutAddonsOptionsPage()
- 位置: L80-93
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `embedderWindowGlobal.documentPrincipal.isSystemPrincipal`, `embedderWindowGlobal.documentURI.spec`

## PromptParent.#isNestedInSidebarBrowser()
- 位置: L95-99
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `browser?.documentGlobal?.browsingContext.embedderElement?.id`

## PromptParent.isEmbeddedInSidebar()
- 位置: L103-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getAttribute()`, `this.#isNestedInSidebarBrowser()`

## PromptParent.shouldShowPromptOnSidebarBrowser()
- 位置: L121-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.getAttribute()`, `this.#isNestedInSidebarBrowser()`, `this.isEmbeddedInSidebar()`

## PromptParent.receiveMessage()
- 位置: L129-140
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.openPromptWithTabDialogBox()`
- 参照: `message.data`, `message.name`, `this.windowContext.isActiveInTab`

## PromptParent.openPromptWithTabDialogBox()
- 位置: async L153-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PromptUtils.propBagToObject()`, `this.isAboutAddonsOptionsPage()`, `this.shouldShowPromptOnSidebarBrowser()`
- 条件付き依存: `if (browsingContext.embedderElement)` → `browsingContext.embedderElement.enterModalState()`
- 条件付き依存: `if (browsingContext.embedderElement)` → `lazy.PromptUtils.fireDialogEvent()`
- 条件付き依存: `if (browsingContext.embedderElement)` → `this.getOpenEventDetail()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `win.gBrowser.getTabDialogBox()`
- 条件付き依存: `if (dialogBox._allowTabFocusByPromptPrincipal)` → `this.addTabSwitchCheckboxToArgs()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (browser == win.gBrowser.selectedBrowser)` → `win.gURLBar.setURI()`
- 条件付き依存: `if (args.isTopLevelCrossDomainAuth && targetTab)` → `win.gBrowser.setTabLabelForAuthPrompts()`
- 条件付き依存: `if (args.isTopLevelCrossDomainAuth && targetTab)` → `lazy.BrowserUtils.formatURIForDisplay()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `lazy.PromptUtils.objectToPropBag()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `dialogBox.open()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `this.registerDialog()`
- 条件付き依存: `if (args.isTopLevelCrossDomainAuth)` → `win.gBrowser.setTabLabelForAuthPrompts()`
- 条件付き依存: `if (promptRequiresBrowser && win?.gBrowser?.getTabDialogBox)` → `this.unregisterPrompt()`
- 条件付き依存: `if (!(promptRequiresBrowser && win?.gBrowser?.getTabDialogBox))` → `lazy.PromptUtils.objectToPropBag()`
- 条件付き依存: `if (!(promptRequiresBrowser && win?.gBrowser?.getTabDialogBox))` → `Services.ww.openWindow()`
- 条件付き依存: `if (browsingContext.embedderElement)` → `browsingContext.embedderElement.maybeLeaveModalState()`
- 参照: `Services.prompt.MODAL_TYPE_CONTENT`, `Services.prompt.MODAL_TYPE_TAB`, `Services.prompt.MODAL_TYPE_WINDOW`, `args._remoteId`, `args.allowFocusCheckbox`, `args.channel.URI`, `args.inPermitUnload`, `args.isTopLevelCrossDomainAuth`, `args.modalType`, `args.ok`, `args.openedWithTabDialog`, `args.owningBrowsingContext`, `args.promptAborted`, `args.promptType`, `args.value`, `browser.currentAuthPromptURI`, `browser.documentGlobal.browsingContext.embedderElement`, `browser?.documentGlobal`, `browsingContext.embedderElement`, `browsingContext.isContent`, `browsingContext.window`, `browsingContext?.webProgress`, `dialog.promptID`, `dialogBox._allowTabFocusByPromptPrincipal`, `targetTab.label`, `this.browsingContext`, `this.browsingContext.top`, `win.gBrowser.selectedBrowser`, `win.winUtils.isParentWindowMainWidgetVisible`, `win?.gBrowser?.getTabDialogBox`, `win?.winUtils`
- XPCOM: `Services.prefs` / `Services.prompt` / `Services.ww`

## PromptParent.getOpenEventDetail()
- 位置: L332-343
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `Services.prompt.MODAL_TYPE_CONTENT`, `args.inPermitUnload`, `args.modalType`, `args.promptPrincipal`
- XPCOM: `Services.prompt`

## PromptParent.addTabSwitchCheckboxToArgs()
- 位置: L354-382
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( allowTabFocusByPromptPrincipal && args.modalType === Services.prompt.MODAL_TYPE_CONTENT )` → `lazy.gTabBrowserLocalization.formatMessagesSync()`
- 条件付き依存: `if ( allowTabFocusByPromptPrincipal && args.modalType === Services.prompt.MODAL_TYPE_CONTENT )` → `allowFocusMsg.attributes.find()`
- 参照: `Services.prompt.MODAL_TYPE_CONTENT`, `a.name`, `allowTabFocusByPromptPrincipal.URI.displayHostPort`, `allowTabFocusByPromptPrincipal.URI.prePath`, `allowTabFocusByPromptPrincipal.addonPolicy?.name`, `args.allowFocusCheckbox`, `args.checkLabel`, `args.modalType`, `dialogBox._allowTabFocusByPromptPrincipal`, `labelAttr.value`
- XPCOM: `Services.prompt`
