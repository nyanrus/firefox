# browser/components/ipprotection/IPProtectionAlertManager.sys.mjs

source: browser/components/ipprotection/IPProtectionAlertManager.sys.mjs
source-hash: 8d85a586a37a7faaba3b2477100c8251ff9fd2a6
lines: 303

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## IPProtectionAlertManagerClass.initialized()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#initialized`

## IPProtectionAlertManagerClass.init()
- 位置: L35-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.addEventListener()`
- 参照: `this.#initialized`

## IPProtectionAlertManagerClass.uninit()
- 位置: L45-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.IPPProxyManager.removeEventListener()`, `this.#closeAllPrompts()`
- 参照: `this.#initialized`

## IPProtectionAlertManagerClass.localizationMessages()
- 位置: L60-92
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.#localizationMessages)` → `lazy.ipProtectionLocalization.formatMessagesSync()`
- 条件付き依存: `if (!this.#localizationMessages)` → `this.#getMaxBandwidthUsage()`
- 参照: `closeTabsButton.value`, `continueButton.value`, `errorBody.value`, `errorTitle.value`, `pausedBody.value`, `pausedTitle.value`, `this.#localizationMessages`

## IPProtectionAlertManagerClass.#getMaxBandwidthUsage()
- 位置: L100-112
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (lazy.IPPProxyManager.usageInfo?.max != null)` → `Number()`
- 条件付き依存: `if (lazy.IPProtectionService.authProvider.maxBytes != null)` → `Number()`
- 参照: `BANDWIDTH.BYTES_IN_GB`, `BANDWIDTH.MAX_IN_GB`, `lazy.IPPProxyManager.usageInfo.max`, `lazy.IPPProxyManager.usageInfo?.max`, `lazy.IPProtectionService.authProvider.maxBytes`

## IPProtectionAlertManagerClass.handleEvent()
- 位置: L114-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#closeAllPrompts()`, `this.showErrorPrompts()`, `this.showPausedPrompts()`
- 参照: `event.detail.state`, `event.type`, `lazy.IPPProxyStates.ACTIVE`, `lazy.IPPProxyStates.ERROR`, `lazy.IPPProxyStates.NOT_READY`, `lazy.IPPProxyStates.PAUSED`, `lazy.IPPProxyStates.READY`

## IPProtectionAlertManagerClass.#createAllPrompts()
- 位置: L147-176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prompt.asyncConfirmEx()`, `promises.push()`
- 参照: `Ci.nsIPromptService.BUTTON_POS_0`, `Ci.nsIPromptService.BUTTON_POS_0_DEFAULT`, `Ci.nsIPromptService.BUTTON_POS_1`, `Ci.nsIPromptService.BUTTON_TITLE_IS_STRING`, `Services.prompt.MODAL_TYPE_INTERNAL_WINDOW`, `lazy.EveryWindow.readyWindows`, `this.#promptsOpen`, `window.browsingContext`
- XPCOM: [`nsIPromptService`](../../../toolkit/components/windowwatcher/nsIPromptService.idl.md) / `Services.prompt`

## IPProtectionAlertManagerClass.#closeAllPrompts()
- 位置: L181-191
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.gDialogBox.dialog?.close()`
- 参照: `lazy.EveryWindow.readyWindows`, `this.#promptsOpen`

## IPProtectionAlertManagerClass.showPausedPrompts()
- 位置: async L200-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.any()`, `result.getProperty()`, `this.#createAllPrompts()`, `this.#handlePromptAction()`
- 参照: `lazy.IPPProxyManager.active`, `promises.length`, `this.localizationMessages`

## IPProtectionAlertManagerClass.showErrorPrompts()
- 位置: async L232-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.any()`, `result.getProperty()`, `this.#createAllPrompts()`, `this.#handlePromptAction()`
- 参照: `lazy.IPPProxyManager.active`, `promises.length`, `this.localizationMessages`

## IPProtectionAlertManagerClass.#handlePromptAction()
- 位置: L266-279
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.ipprotection.alertButtonClicked.record()`, `this.#closeAllPrompts()`
- 条件付き依存: `if (buttonClicked === 0)` → `lazy.IPPProxyManager.stop()`
- 条件付き依存: `if (buttonClicked === 1)` → `this.#closeAllTabs()`

## IPProtectionAlertManagerClass.#closeAllTabs()
- 位置: async L281-298
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.wm.getMostRecentBrowserWindow()`, `lazy.IPPProxyManager.stop()`, `mostRecentWindow.gBrowser.removeTabs()`, `mostRecentWindow.openTrustedLinkIn()`, `window.close()`
- 参照: `lazy.EveryWindow.readyWindows`, `mostRecentWindow.gBrowser.tabs`
- XPCOM: `Services.wm`
